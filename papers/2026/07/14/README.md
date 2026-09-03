# Daily Research — 2026-07-14

**Research Date:** 2026-07-14

**Timezone:** Asia/Shanghai

**Strict Window:** 2026-07-13 09:00:00 ～ 2026-07-14 09:00:00（北京时间，左闭右开）

**Contract:** V2.1 Full Replay；Historical Daily 独立重建，不使用 Weekly 作为 discovery、评分或 Review 来源

**Status:** In Progress；Coverage=Open、Evidence=Open、Books=Open；author-side evidence 已闭合，等待独立 Semantic Audit 与 root Books 比较

## Executive Summary

本窗口由官方 arXiv first-public owner inventory 枚举 **965** 个唯一 identity；逐项读取 title 与完整 abstract 后，冻结 **103** 个候选并对 **862** 项给出 family-specific closure，retain rate **10.67%**。103 个候选全部取得 exact v1 并完成 Source Review：Deep 62、Standard 41、blocked 0。

两项缺少 arXiv HTML 的论文改用官方 v1 PDF 并完成逐页文本提取与可读性检查；其余 101 项使用 official exact-v1 HTML。withdrawn 检查未发现候选撤稿。当前没有把审阅建议冒充最终 Books Decision。

## 1. Coverage

<!-- validator:report-metadata-v2 -->
| Field | Value |
| --- | --- |
| Contract Version | V2.1 |
| Score Schema | V2 |
| Report Type | Daily |
| Window Start | 2026-07-14 |
| Window End | 2026-07-14 |
| Registry Version | 2026-08-25 |
| Coverage Mode | Full Replay |
| Baseline Report | — |
| Changed Source IDs | — |
| Previous Denominator ID | — |
| Denominator ID | daily-2026-07-14-0900-v2.1-sha256:50c86fa12bb6e8ebb00951612691614902463e0f359da494fd29d1ba344dbff6 |
| Denominator Frozen At | 2026-09-04T00:40:00+08:00 |
| Completion Status | In Progress |
| Coverage Gate | Open |
| Evidence Gate | Open |
| Books Gate | Open |

### Source Coverage Receipt

<!-- coverage:SRC-ARXIV:20260714:start -->
<!-- validator:source-coverage-v2 -->
| Source ID | Window Start | Window End | Executed At | Endpoint / Filter | Result | Hits | Candidate Source Families | Pagination / Cursor | Window Watermark | Closure Evidence | Gap / Limitation ID |
| --- | --- | --- | --- | --- | --- | ---: | --- | --- | --- | --- | --- |
| SRC-ARXIV | 2026-07-13T09:00:00+08:00 | 2026-07-14T09:00:00+08:00 | 2026-09-04T00:40:00+08:00 | official arXiv monthly category listings; v1 submission history; availability schedule; DataCite DOI created only for announcement-cycle reconciliation | checked | 965 | SF-2026-ARXIV-2607-09665;SF-2026-ARXIV-2607-09682;SF-2026-ARXIV-2607-09686;SF-2026-ARXIV-2607-09689;SF-2026-ARXIV-2607-09691;SF-2026-ARXIV-2607-09692;SF-2026-ARXIV-2607-09697;SF-2026-ARXIV-2607-09709;SF-2026-ARXIV-2607-09711;SF-2026-ARXIV-2607-09744;SF-2026-ARXIV-2607-09748;SF-2026-ARXIV-2607-09759;SF-2026-ARXIV-2607-09770;SF-2026-ARXIV-2607-09773;SF-2026-ARXIV-2607-09776;SF-2026-ARXIV-2607-09786;SF-2026-ARXIV-2607-09791;SF-2026-ARXIV-2607-09794;SF-2026-ARXIV-2607-09800;SF-2026-ARXIV-2607-09802;SF-2026-ARXIV-2607-09803;SF-2026-ARXIV-2607-09804;SF-2026-ARXIV-2607-09822;SF-2026-ARXIV-2607-09889;SF-2026-ARXIV-2607-09992;SF-2026-ARXIV-2607-09996;SF-2026-ARXIV-2607-09999;SF-2026-ARXIV-2607-10044;SF-2026-ARXIV-2607-10059;SF-2026-ARXIV-2607-10079;SF-2026-ARXIV-2607-10096;SF-2026-ARXIV-2607-10103;SF-2026-ARXIV-2607-10110;SF-2026-ARXIV-2607-10139;SF-2026-ARXIV-2607-10152;SF-2026-ARXIV-2607-10183;SF-2026-ARXIV-2607-10186;SF-2026-ARXIV-2607-10198;SF-2026-ARXIV-2607-10203;SF-2026-ARXIV-2607-10226;SF-2026-ARXIV-2607-10240;SF-2026-ARXIV-2607-10252;SF-2026-ARXIV-2607-10265;SF-2026-ARXIV-2607-10291;SF-2026-ARXIV-2607-10350;SF-2026-ARXIV-2607-10362;SF-2026-ARXIV-2607-10389;SF-2026-ARXIV-2607-10463;SF-2026-ARXIV-2607-10491;SF-2026-ARXIV-2607-10582;SF-2026-ARXIV-2607-10661;SF-2026-ARXIV-2607-10709;SF-2026-ARXIV-2607-10712;SF-2026-ARXIV-2607-10750;SF-2026-ARXIV-2607-10798;SF-2026-ARXIV-2607-10855;SF-2026-ARXIV-2607-10959;SF-2026-ARXIV-2607-10987;SF-2026-ARXIV-2607-11070;SF-2026-ARXIV-2607-11079;SF-2026-ARXIV-2607-11086;SF-2026-ARXIV-2607-11131;SF-2026-ARXIV-2607-11136;SF-2026-ARXIV-2607-11138;SF-2026-ARXIV-2607-11149;SF-2026-ARXIV-2607-11172;SF-2026-ARXIV-2607-11183;SF-2026-ARXIV-2607-11226;SF-2026-ARXIV-2607-11250;SF-2026-ARXIV-2607-11262;SF-2026-ARXIV-2607-11317;SF-2026-ARXIV-2607-11346;SF-2026-ARXIV-2607-11368;SF-2026-ARXIV-2607-11388;SF-2026-ARXIV-2607-11399;SF-2026-ARXIV-2607-11414;SF-2026-ARXIV-2607-11423;SF-2026-ARXIV-2607-11433;SF-2026-ARXIV-2607-11436;SF-2026-ARXIV-2607-11444;SF-2026-ARXIV-2607-11475;SF-2026-ARXIV-2607-11487;SF-2026-ARXIV-2607-11498;SF-2026-ARXIV-2607-11505;SF-2026-ARXIV-2607-11506;SF-2026-ARXIV-2607-11579;SF-2026-ARXIV-2607-11586;SF-2026-ARXIV-2607-11598;SF-2026-ARXIV-2607-11611;SF-2026-ARXIV-2607-11614;SF-2026-ARXIV-2607-11643;SF-2026-ARXIV-2607-11673;SF-2026-ARXIV-2607-11698;SF-2026-ARXIV-2607-11738;SF-2026-ARXIV-2607-11746;SF-2026-ARXIV-2607-11751;SF-2026-ARXIV-2607-11796;SF-2026-ARXIV-2607-11818;SF-2026-ARXIV-2607-11836;SF-2026-ARXIV-2607-11862;SF-2026-ARXIV-2607-11871;SF-2026-ARXIV-2607-11883;SF-2026-ARXIV-2607-11886 | all registered category pages show=2000; cross-category dedup complete | 2026-07-14T09:00:00+08:00 | sha256:50c86fa12bb6e8ebb00951612691614902463e0f359da494fd29d1ba344dbff6 | — |
<!-- coverage:SRC-ARXIV:20260714:end -->

### Coverage Limitations

- DataCite 只辅助 first-announcement reconciliation；所有技术主张均回到 official exact arXiv v1。
- 101 项由 exact-v1 HTML 审阅；`2607.09999`、`2607.11183` 因 HTML 不可用，使用 official v1 PDF 的逐页文本与可读性检查。
- author-side receipt 已闭合；独立 false-positive / false-negative audit 尚未签收，因此 Coverage Gate 保持 Open。

## 2. Candidate Ledger

<!-- validator:candidate-ledger-v2.1 -->
| Source Family ID | Primary Identifier | Event Identity | Owner Week | First-public Date | Supporting Source IDs | Design Delta | System Reach | Durability | Total | Candidate State | Review Status | Access Status | Review Override | Review Ref | Owner Report Ref | Prior Review Ref | Reconciliation | Stable Node ID | Books Disposition | Books Review Ref | Benchmark Claim |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2607-09665 | arXiv:2607.09665v1 | paper-v1:2607.09665 | 2026-W29 | 2026-07-14 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-09665 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-09682 | arXiv:2607.09682v1 | paper-v1:2607.09682 | 2026-W29 | 2026-07-14 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-09682 | self | — | new_in_window | PLATFORM-TRACE | Not Assessed | — | no |
| SF-2026-ARXIV-2607-09686 | arXiv:2607.09686v1 | paper-v1:2607.09686 | 2026-W29 | 2026-07-14 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-09686 | self | — | new_in_window | INFER-SCHEDULING | Not Assessed | — | no |
| SF-2026-ARXIV-2607-09689 | arXiv:2607.09689v1 | paper-v1:2607.09689 | 2026-W29 | 2026-07-14 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-09689 | self | — | new_in_window | AGENT-WORKFLOW | Not Assessed | — | no |
| SF-2026-ARXIV-2607-09691 | arXiv:2607.09691v1 | paper-v1:2607.09691 | 2026-W29 | 2026-07-14 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-09691 | self | — | new_in_window | AGENT-CONTEXT | Not Assessed | — | no |
| SF-2026-ARXIV-2607-09692 | arXiv:2607.09692v1 | paper-v1:2607.09692 | 2026-W29 | 2026-07-14 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-09692 | self | — | new_in_window | PLATFORM-SECURITY | Not Assessed | — | no |
| SF-2026-ARXIV-2607-09697 | arXiv:2607.09697v1 | paper-v1:2607.09697 | 2026-W29 | 2026-07-14 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-09697 | self | — | new_in_window | PLATFORM-SECURITY | Not Assessed | — | no |
| SF-2026-ARXIV-2607-09709 | arXiv:2607.09709v1 | paper-v1:2607.09709 | 2026-W29 | 2026-07-14 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-09709 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-09711 | arXiv:2607.09711v1 | paper-v1:2607.09711 | 2026-W29 | 2026-07-14 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-09711 | self | — | new_in_window | AGENT-PLATFORM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-09744 | arXiv:2607.09744v1 | paper-v1:2607.09744 | 2026-W29 | 2026-07-14 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-09744 | self | — | new_in_window | PLATFORM-SECURITY | Not Assessed | — | no |
| SF-2026-ARXIV-2607-09748 | arXiv:2607.09748v1 | paper-v1:2607.09748 | 2026-W29 | 2026-07-14 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-09748 | self | — | new_in_window | AGENT-PLATFORM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-09759 | arXiv:2607.09759v1 | paper-v1:2607.09759 | 2026-W29 | 2026-07-14 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-09759 | self | — | new_in_window | AGENT-MEMORY | Not Assessed | — | no |
| SF-2026-ARXIV-2607-09770 | arXiv:2607.09770v1 | paper-v1:2607.09770 | 2026-W29 | 2026-07-14 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-09770 | self | — | new_in_window | AGENT-PLATFORM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-09773 | arXiv:2607.09773v1 | paper-v1:2607.09773 | 2026-W29 | 2026-07-14 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-09773 | self | — | new_in_window | TRAIN-GRPO | Not Assessed | — | no |
| SF-2026-ARXIV-2607-09776 | arXiv:2607.09776v1 | paper-v1:2607.09776 | 2026-W29 | 2026-07-14 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-09776 | self | — | new_in_window | MULTIMODAL-EMBODIED-VLA | Not Assessed | — | no |
| SF-2026-ARXIV-2607-09786 | arXiv:2607.09786v1 | paper-v1:2607.09786 | 2026-W29 | 2026-07-14 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-09786 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-09791 | arXiv:2607.09791v1 | paper-v1:2607.09791 | 2026-W29 | 2026-07-14 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-09791 | self | — | new_in_window | INFER-DECODE | Not Assessed | — | no |
| SF-2026-ARXIV-2607-09794 | arXiv:2607.09794v1 | paper-v1:2607.09794 | 2026-W29 | 2026-07-14 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-09794 | self | — | new_in_window | AGENT-CONTEXT | Not Assessed | — | no |
| SF-2026-ARXIV-2607-09800 | arXiv:2607.09800v1 | paper-v1:2607.09800 | 2026-W29 | 2026-07-14 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-09800 | self | — | new_in_window | TRAIN-PRETRAINING | Not Assessed | — | no |
| SF-2026-ARXIV-2607-09802 | arXiv:2607.09802v1 | paper-v1:2607.09802 | 2026-W29 | 2026-07-14 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-09802 | self | — | new_in_window | PLATFORM-GPU-SCHEDULER | Not Assessed | — | no |
| SF-2026-ARXIV-2607-09803 | arXiv:2607.09803v1 | paper-v1:2607.09803 | 2026-W29 | 2026-07-14 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-09803 | self | — | new_in_window | AGENT-REFLECTION | Not Assessed | — | no |
| SF-2026-ARXIV-2607-09804 | arXiv:2607.09804v1 | paper-v1:2607.09804 | 2026-W29 | 2026-07-14 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | deep_complete | accessible | release_security_contract | review:SF-2026-ARXIV-2607-09804 | self | — | new_in_window | PLATFORM-SECURITY | Not Assessed | — | no |
| SF-2026-ARXIV-2607-09822 | arXiv:2607.09822v1 | paper-v1:2607.09822 | 2026-W29 | 2026-07-14 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-09822 | self | — | new_in_window | AGENT-MEMORY | Not Assessed | — | no |
| SF-2026-ARXIV-2607-09889 | arXiv:2607.09889v1 | paper-v1:2607.09889 | 2026-W29 | 2026-07-14 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-09889 | self | — | new_in_window | MODEL-LONG-CONTEXT | Not Assessed | — | no |
| SF-2026-ARXIV-2607-09992 | arXiv:2607.09992v1 | paper-v1:2607.09992 | 2026-W29 | 2026-07-14 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-09992 | self | — | new_in_window | INFER-SCHEDULING | Not Assessed | — | no |
| SF-2026-ARXIV-2607-09996 | arXiv:2607.09996v1 | paper-v1:2607.09996 | 2026-W29 | 2026-07-14 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-09996 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-09999 | arXiv:2607.09999v1 | paper-v1:2607.09999 | 2026-W29 | 2026-07-14 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-09999 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-10044 | arXiv:2607.10044v1 | paper-v1:2607.10044 | 2026-W29 | 2026-07-14 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-10044 | self | — | new_in_window | INFER-DECODE | Not Assessed | — | no |
| SF-2026-ARXIV-2607-10059 | arXiv:2607.10059v1 | paper-v1:2607.10059 | 2026-W29 | 2026-07-14 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-10059 | self | — | new_in_window | AGENT-TOOL-CALLING | Not Assessed | — | no |
| SF-2026-ARXIV-2607-10079 | arXiv:2607.10079v1 | paper-v1:2607.10079 | 2026-W29 | 2026-07-14 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-10079 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-10096 | arXiv:2607.10096v1 | paper-v1:2607.10096 | 2026-W29 | 2026-07-14 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-10096 | self | — | new_in_window | AGENT-RAG | Not Assessed | — | no |
| SF-2026-ARXIV-2607-10103 | arXiv:2607.10103v1 | paper-v1:2607.10103 | 2026-W29 | 2026-07-14 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-10103 | self | — | new_in_window | PLATFORM-SECURITY | Not Assessed | — | no |
| SF-2026-ARXIV-2607-10110 | arXiv:2607.10110v1 | paper-v1:2607.10110 | 2026-W29 | 2026-07-14 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-10110 | self | — | new_in_window | MODEL-LONG-CONTEXT | Not Assessed | — | no |
| SF-2026-ARXIV-2607-10139 | arXiv:2607.10139v1 | paper-v1:2607.10139 | 2026-W29 | 2026-07-14 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-10139 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-10152 | arXiv:2607.10152v1 | paper-v1:2607.10152 | 2026-W29 | 2026-07-14 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-10152 | self | — | new_in_window | AGENT-MULTI-AGENT | Not Assessed | — | no |
| SF-2026-ARXIV-2607-10183 | arXiv:2607.10183v1 | paper-v1:2607.10183 | 2026-W29 | 2026-07-14 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-10183 | self | — | new_in_window | INFER-TENSORRT-LLM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-10186 | arXiv:2607.10186v1 | paper-v1:2607.10186 | 2026-W29 | 2026-07-14 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-10186 | self | — | new_in_window | INFER-GPU-MEMORY | Not Assessed | — | no |
| SF-2026-ARXIV-2607-10198 | arXiv:2607.10198v1 | paper-v1:2607.10198 | 2026-W29 | 2026-07-14 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-10198 | self | — | new_in_window | AGENT-RAG | Not Assessed | — | no |
| SF-2026-ARXIV-2607-10203 | arXiv:2607.10203v1 | paper-v1:2607.10203 | 2026-W29 | 2026-07-14 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-10203 | self | — | new_in_window | MULTIMODAL-WORLD-MODELS | Not Assessed | — | no |
| SF-2026-ARXIV-2607-10226 | arXiv:2607.10226v1 | paper-v1:2607.10226 | 2026-W29 | 2026-07-14 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-10226 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-10240 | arXiv:2607.10240v1 | paper-v1:2607.10240 | 2026-W29 | 2026-07-14 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-10240 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-10252 | arXiv:2607.10252v1 | paper-v1:2607.10252 | 2026-W29 | 2026-07-14 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-10252 | self | — | new_in_window | PLATFORM-SECURITY | Not Assessed | — | no |
| SF-2026-ARXIV-2607-10265 | arXiv:2607.10265v1 | paper-v1:2607.10265 | 2026-W29 | 2026-07-14 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-10265 | self | — | new_in_window | AGENT-MEMORY | Not Assessed | — | no |
| SF-2026-ARXIV-2607-10291 | arXiv:2607.10291v1 | paper-v1:2607.10291 | 2026-W29 | 2026-07-14 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-10291 | self | — | new_in_window | AGENT-WORKFLOW | Not Assessed | — | no |
| SF-2026-ARXIV-2607-10350 | arXiv:2607.10350v1 | paper-v1:2607.10350 | 2026-W29 | 2026-07-14 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-10350 | self | — | new_in_window | AGENT-WORKFLOW | Not Assessed | — | no |
| SF-2026-ARXIV-2607-10362 | arXiv:2607.10362v1 | paper-v1:2607.10362 | 2026-W29 | 2026-07-14 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-10362 | self | — | new_in_window | MULTIMODAL-WORLD-MODELS | Not Assessed | — | no |
| SF-2026-ARXIV-2607-10389 | arXiv:2607.10389v1 | paper-v1:2607.10389 | 2026-W29 | 2026-07-14 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-10389 | self | — | new_in_window | INFER-SCHEDULING | Not Assessed | — | no |
| SF-2026-ARXIV-2607-10463 | arXiv:2607.10463v1 | paper-v1:2607.10463 | 2026-W29 | 2026-07-14 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-10463 | self | — | new_in_window | AGENT-RAG | Not Assessed | — | no |
| SF-2026-ARXIV-2607-10491 | arXiv:2607.10491v1 | paper-v1:2607.10491 | 2026-W29 | 2026-07-14 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-10491 | self | — | new_in_window | AGENT-RAG | Not Assessed | — | no |
| SF-2026-ARXIV-2607-10582 | arXiv:2607.10582v1 | paper-v1:2607.10582 | 2026-W29 | 2026-07-14 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-10582 | self | — | new_in_window | INFER-KV-CACHE | Not Assessed | — | no |
| SF-2026-ARXIV-2607-10661 | arXiv:2607.10661v1 | paper-v1:2607.10661 | 2026-W29 | 2026-07-14 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-10661 | self | — | new_in_window | INFER-SPECULATIVE-DECODING | Not Assessed | — | no |
| SF-2026-ARXIV-2607-10709 | arXiv:2607.10709v1 | paper-v1:2607.10709 | 2026-W29 | 2026-07-14 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | release_security_contract | review:SF-2026-ARXIV-2607-10709 | self | — | new_in_window | PLATFORM-SECURITY | Not Assessed | — | no |
| SF-2026-ARXIV-2607-10712 | arXiv:2607.10712v1 | paper-v1:2607.10712 | 2026-W29 | 2026-07-14 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-10712 | self | — | new_in_window | PLATFORM-SECURITY | Not Assessed | — | no |
| SF-2026-ARXIV-2607-10750 | arXiv:2607.10750v1 | paper-v1:2607.10750 | 2026-W29 | 2026-07-14 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-10750 | self | — | new_in_window | TRAIN-DATA | Not Assessed | — | no |
| SF-2026-ARXIV-2607-10798 | arXiv:2607.10798v1 | paper-v1:2607.10798 | 2026-W29 | 2026-07-14 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-10798 | self | — | new_in_window | AGENT-RAG | Not Assessed | — | no |
| SF-2026-ARXIV-2607-10855 | arXiv:2607.10855v1 | paper-v1:2607.10855 | 2026-W29 | 2026-07-14 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-10855 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-10959 | arXiv:2607.10959v1 | paper-v1:2607.10959 | 2026-W29 | 2026-07-14 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-10959 | self | — | new_in_window | TRAIN-PRETRAINING | Not Assessed | — | no |
| SF-2026-ARXIV-2607-10987 | arXiv:2607.10987v1 | paper-v1:2607.10987 | 2026-W29 | 2026-07-14 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-10987 | self | — | new_in_window | INFER-DYNAMO | Not Assessed | — | no |
| SF-2026-ARXIV-2607-11070 | arXiv:2607.11070v1 | paper-v1:2607.11070 | 2026-W29 | 2026-07-14 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-11070 | self | — | new_in_window | TRAIN-GRPO | Not Assessed | — | no |
| SF-2026-ARXIV-2607-11079 | arXiv:2607.11079v1 | paper-v1:2607.11079 | 2026-W29 | 2026-07-14 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-11079 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-11086 | arXiv:2607.11086v1 | paper-v1:2607.11086 | 2026-W29 | 2026-07-14 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-11086 | self | — | new_in_window | AGENT-MCP | Not Assessed | — | no |
| SF-2026-ARXIV-2607-11131 | arXiv:2607.11131v1 | paper-v1:2607.11131 | 2026-W29 | 2026-07-14 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-11131 | self | — | new_in_window | INFER-SPECULATIVE-DECODING | Not Assessed | — | no |
| SF-2026-ARXIV-2607-11136 | arXiv:2607.11136v1 | paper-v1:2607.11136 | 2026-W29 | 2026-07-14 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-11136 | self | — | new_in_window | INFER-GPU-MEMORY | Not Assessed | — | no |
| SF-2026-ARXIV-2607-11138 | arXiv:2607.11138v1 | paper-v1:2607.11138 | 2026-W29 | 2026-07-14 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-11138 | self | — | new_in_window | AGENT-WORKFLOW | Not Assessed | — | no |
| SF-2026-ARXIV-2607-11149 | arXiv:2607.11149v1 | paper-v1:2607.11149 | 2026-W29 | 2026-07-14 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-11149 | self | — | new_in_window | PLATFORM-COST | Not Assessed | — | no |
| SF-2026-ARXIV-2607-11172 | arXiv:2607.11172v1 | paper-v1:2607.11172 | 2026-W29 | 2026-07-14 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-11172 | self | — | new_in_window | TRAIN-GRPO | Not Assessed | — | no |
| SF-2026-ARXIV-2607-11183 | arXiv:2607.11183v1 | paper-v1:2607.11183 | 2026-W29 | 2026-07-14 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-11183 | self | — | new_in_window | MODEL-FFN | Not Assessed | — | no |
| SF-2026-ARXIV-2607-11226 | arXiv:2607.11226v1 | paper-v1:2607.11226 | 2026-W29 | 2026-07-14 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-11226 | self | — | new_in_window | AGENT-MULTI-AGENT | Not Assessed | — | no |
| SF-2026-ARXIV-2607-11250 | arXiv:2607.11250v1 | paper-v1:2607.11250 | 2026-W29 | 2026-07-14 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-11250 | self | — | new_in_window | AGENT-MULTI-AGENT | Not Assessed | — | no |
| SF-2026-ARXIV-2607-11262 | arXiv:2607.11262v1 | paper-v1:2607.11262 | 2026-W29 | 2026-07-14 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-11262 | self | — | new_in_window | INFER-TENSORRT-LLM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-11317 | arXiv:2607.11317v1 | paper-v1:2607.11317 | 2026-W29 | 2026-07-14 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-11317 | self | — | new_in_window | INFER-DECODE | Not Assessed | — | no |
| SF-2026-ARXIV-2607-11346 | arXiv:2607.11346v1 | paper-v1:2607.11346 | 2026-W29 | 2026-07-14 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-11346 | self | — | new_in_window | AGENT-WORKFLOW | Not Assessed | — | no |
| SF-2026-ARXIV-2607-11368 | arXiv:2607.11368v1 | paper-v1:2607.11368 | 2026-W29 | 2026-07-14 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-11368 | self | — | new_in_window | INFER-TENSORRT-LLM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-11388 | arXiv:2607.11388v1 | paper-v1:2607.11388 | 2026-W29 | 2026-07-14 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-11388 | self | — | new_in_window | AGENT-WORKFLOW | Not Assessed | — | no |
| SF-2026-ARXIV-2607-11399 | arXiv:2607.11399v1 | paper-v1:2607.11399 | 2026-W29 | 2026-07-14 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-11399 | self | — | new_in_window | AGENT-PLATFORM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-11414 | arXiv:2607.11414v1 | paper-v1:2607.11414 | 2026-W29 | 2026-07-14 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-11414 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-11423 | arXiv:2607.11423v1 | paper-v1:2607.11423 | 2026-W29 | 2026-07-14 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-11423 | self | — | new_in_window | AGENT-PLATFORM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-11433 | arXiv:2607.11433v1 | paper-v1:2607.11433 | 2026-W29 | 2026-07-14 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-11433 | self | — | new_in_window | AGENT-WORKFLOW | Not Assessed | — | no |
| SF-2026-ARXIV-2607-11436 | arXiv:2607.11436v1 | paper-v1:2607.11436 | 2026-W29 | 2026-07-14 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-11436 | self | — | new_in_window | MULTIMODAL-REPRESENTATION | Not Assessed | — | no |
| SF-2026-ARXIV-2607-11444 | arXiv:2607.11444v1 | paper-v1:2607.11444 | 2026-W29 | 2026-07-14 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-11444 | self | — | new_in_window | MODEL-MOE | Not Assessed | — | no |
| SF-2026-ARXIV-2607-11475 | arXiv:2607.11475v1 | paper-v1:2607.11475 | 2026-W29 | 2026-07-14 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-11475 | self | — | new_in_window | PLATFORM-SECURITY | Not Assessed | — | no |
| SF-2026-ARXIV-2607-11487 | arXiv:2607.11487v1 | paper-v1:2607.11487 | 2026-W29 | 2026-07-14 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-11487 | self | — | new_in_window | AGENT-MEMORY | Not Assessed | — | no |
| SF-2026-ARXIV-2607-11498 | arXiv:2607.11498v1 | paper-v1:2607.11498 | 2026-W29 | 2026-07-14 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-11498 | self | — | new_in_window | MULTIMODAL-EMBODIED-VLA | Not Assessed | — | no |
| SF-2026-ARXIV-2607-11505 | arXiv:2607.11505v1 | paper-v1:2607.11505 | 2026-W29 | 2026-07-14 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-11505 | self | — | new_in_window | TRAIN-GRPO | Not Assessed | — | no |
| SF-2026-ARXIV-2607-11506 | arXiv:2607.11506v1 | paper-v1:2607.11506 | 2026-W29 | 2026-07-14 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-11506 | self | — | new_in_window | TRAIN-GRPO | Not Assessed | — | no |
| SF-2026-ARXIV-2607-11579 | arXiv:2607.11579v1 | paper-v1:2607.11579 | 2026-W29 | 2026-07-14 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-11579 | self | — | new_in_window | PLATFORM-GPU-SCHEDULER | Not Assessed | — | no |
| SF-2026-ARXIV-2607-11586 | arXiv:2607.11586v1 | paper-v1:2607.11586 | 2026-W29 | 2026-07-14 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-11586 | self | — | new_in_window | MODEL-MOE | Not Assessed | — | no |
| SF-2026-ARXIV-2607-11598 | arXiv:2607.11598v1 | paper-v1:2607.11598 | 2026-W29 | 2026-07-14 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-11598 | self | — | new_in_window | AGENT-WORKFLOW | Not Assessed | — | no |
| SF-2026-ARXIV-2607-11611 | arXiv:2607.11611v1 | paper-v1:2607.11611 | 2026-W29 | 2026-07-14 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-11611 | self | — | new_in_window | AGENT-TOOL-CALLING | Not Assessed | — | no |
| SF-2026-ARXIV-2607-11614 | arXiv:2607.11614v1 | paper-v1:2607.11614 | 2026-W29 | 2026-07-14 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-11614 | self | — | new_in_window | MODEL-LONG-CONTEXT | Not Assessed | — | no |
| SF-2026-ARXIV-2607-11643 | arXiv:2607.11643v1 | paper-v1:2607.11643 | 2026-W29 | 2026-07-14 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-11643 | self | — | new_in_window | MULTIMODAL-WORLD-MODELS | Not Assessed | — | no |
| SF-2026-ARXIV-2607-11673 | arXiv:2607.11673v1 | paper-v1:2607.11673 | 2026-W29 | 2026-07-14 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-11673 | self | — | new_in_window | MULTIMODAL-WORLD-MODELS | Not Assessed | — | no |
| SF-2026-ARXIV-2607-11698 | arXiv:2607.11698v1 | paper-v1:2607.11698 | 2026-W29 | 2026-07-14 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-11698 | self | — | new_in_window | PLATFORM-SECURITY | Not Assessed | — | no |
| SF-2026-ARXIV-2607-11738 | arXiv:2607.11738v1 | paper-v1:2607.11738 | 2026-W29 | 2026-07-14 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-11738 | self | — | new_in_window | MULTIMODAL-REPRESENTATION | Not Assessed | — | no |
| SF-2026-ARXIV-2607-11746 | arXiv:2607.11746v1 | paper-v1:2607.11746 | 2026-W29 | 2026-07-14 | SRC-ARXIV | 2 | 2 | 1 | 5 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-11746 | self | — | new_in_window | INFER-TENSORRT-LLM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-11751 | arXiv:2607.11751v1 | paper-v1:2607.11751 | 2026-W29 | 2026-07-14 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-11751 | self | — | new_in_window | PLATFORM-SECURITY | Not Assessed | — | no |
| SF-2026-ARXIV-2607-11796 | arXiv:2607.11796v1 | paper-v1:2607.11796 | 2026-W29 | 2026-07-14 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-11796 | self | — | new_in_window | MODEL-LONG-CONTEXT | Not Assessed | — | no |
| SF-2026-ARXIV-2607-11818 | arXiv:2607.11818v1 | paper-v1:2607.11818 | 2026-W29 | 2026-07-14 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-11818 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-11836 | arXiv:2607.11836v1 | paper-v1:2607.11836 | 2026-W29 | 2026-07-14 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-11836 | self | — | new_in_window | MULTIMODAL-WORLD-MODELS | Not Assessed | — | no |
| SF-2026-ARXIV-2607-11862 | arXiv:2607.11862v1 | paper-v1:2607.11862 | 2026-W29 | 2026-07-14 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-11862 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-11871 | arXiv:2607.11871v1 | paper-v1:2607.11871 | 2026-W29 | 2026-07-14 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-11871 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-11883 | arXiv:2607.11883v1 | paper-v1:2607.11883 | 2026-W29 | 2026-07-14 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-11883 | self | — | new_in_window | WORLDVIEW-WHY-MODELS-LEARN | Not Assessed | — | no |
| SF-2026-ARXIV-2607-11886 | arXiv:2607.11886v1 | paper-v1:2607.11886 | 2026-W29 | 2026-07-14 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-11886 | self | — | new_in_window | MULTIMODAL-GENERATIVE-PARADIGMS | Not Assessed | — | no |

## 3. Review Completion Receipt

<!-- validator:review-completion-v1 -->
| Source Family ID | Review Provenance ID | Review Route | Primary Evidence Version | Reviewed Evidence Versions | Method / Identity Locators | Evaluation Locators | Limitations / Counterevidence Locators | Artifact Locators | Claim Boundary Ref | Completion Result |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2607-09665 | RP-9287c9fa9a7fdda1 | deep | arXiv:2607.09665v1 | SRC-ARXIV@arXiv:2607.09665v1 | https://arxiv.org/html/2607.09665v1#S3.SS1 — 3.1 Tasks and Models; https://arxiv.org/html/2607.09665v1#S5.SS1 — 5.1 Format Sensitivity Varies Sharply Across Models | https://arxiv.org/html/2607.09665v1#S3 — 3 Experimental Setup; https://arxiv.org/html/2607.09665v1#S5 — 5 Results | https://arxiv.org/html/2607.09665v1#S6 — 6 Discussion and Recommendations; https://arxiv.org/html/2607.09665v1#S7 — 7 Limitations | Exact v1 links https://github.com/EleutherAI/lm-evaluation-harness, https://github.com/stanfordnlp/synchromesh, https://github.com/arXiv/html_feedback/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-09665 | complete |
| SF-2026-ARXIV-2607-09682 | RP-8a8fdeece9add6f4 | deep | arXiv:2607.09682v1 | SRC-ARXIV@arXiv:2607.09682v1 | https://arxiv.org/html/2607.09682v1#S3 — 3 System Design; https://arxiv.org/html/2607.09682v1#S3.SS2 — 3.2 Event model | https://arxiv.org/html/2607.09682v1#S4 — 4 Evaluation | https://arxiv.org/html/2607.09682v1#S5 — 5 Discussion and Limitations; https://arxiv.org/html/2607.09682v1#S3.SS6 — 3.6 Threat model | Exact v1 links https://pypi.org/project/auditweave/, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-09682 | complete |
| SF-2026-ARXIV-2607-09686 | RP-16eddb0a0f6be1c9 | deep | arXiv:2607.09686v1 | SRC-ARXIV@arXiv:2607.09686v1 | https://arxiv.org/html/2607.09686v1#S4 — IV MawForge Design; https://arxiv.org/html/2607.09686v1#S4.SS1 — IV-A System Thesis | https://arxiv.org/html/2607.09686v1#S5 — V Experimental Method; https://arxiv.org/html/2607.09686v1#S6 — VI Results | https://arxiv.org/html/2607.09686v1#S11 — XI Conclusion; https://arxiv.org/html/2607.09686v1#S7 — VII Discussion | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-09686 | complete |
| SF-2026-ARXIV-2607-09689 | RP-1e76fc09972bbe74 | deep | arXiv:2607.09689v1 | SRC-ARXIV@arXiv:2607.09689v1 | https://arxiv.org/html/2607.09689v1#S4 — 4 Orchestration and Security (Design Sketch); https://arxiv.org/html/2607.09689v1#S2 — 2 Programming Model and Forkable-Sandbox Substrate | https://arxiv.org/html/2607.09689v1#S5 — 5 Evaluation | https://arxiv.org/html/2607.09689v1#S6 — 6 Conclusion | Exact v1 links https://github.com/zozo123/boltzmann-mapreduce, https://github.com/opencontainers/image-spec, https://github.com/arXiv/html_feedback/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-09689 | complete |
| SF-2026-ARXIV-2607-09691 | RP-c30472c7f4d8b12c | standard | arXiv:2607.09691v1 | SRC-ARXIV@arXiv:2607.09691v1 | https://arxiv.org/html/2607.09691v1#S3 — 3 Method | https://arxiv.org/html/2607.09691v1#A4 — Appendix D Exploratory results (not claims of this paper); https://arxiv.org/html/2607.09691v1#S3.SS1 — 3.1 Experimental setup | https://arxiv.org/html/2607.09691v1#S6 — 6 Threats to validity (and which way each cuts); https://arxiv.org/html/2607.09691v1#S7 — 7 Conclusion | Exact v1 links https://github.com/integrallis/act-context, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-09691 | complete |
| SF-2026-ARXIV-2607-09692 | RP-9bb0077c3899fa15 | standard | arXiv:2607.09692v1 | SRC-ARXIV@arXiv:2607.09692v1 | https://arxiv.org/html/2607.09692v1#A2.SS3 — B.3 Ablations for Reverse MIA methods; https://arxiv.org/html/2607.09692v1#S3 — 3 Method | https://arxiv.org/html/2607.09692v1#A2 — Appendix B Additional Experimental Results; https://arxiv.org/html/2607.09692v1#S4.SS2 — 4.2 Results from Controlled Experiments | https://arxiv.org/html/2607.09692v1#S8 — 8 Conclusion | Exact v1 links https://github.com/RajatRawat-creator/DistillDetect, https://huggingface.co/deepseek-ai/DeepSeek-R1-Distill-Qwen-7B#deepseek-r1-distill-models, https://huggingface.co/simplescaling/s1.1-32B; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-09692 | complete |
| SF-2026-ARXIV-2607-09697 | RP-a46f263ec6b46735 | deep | arXiv:2607.09697v1 | SRC-ARXIV@arXiv:2607.09697v1 | https://arxiv.org/html/2607.09697v1#S3 — 3 OutGuard Method; https://arxiv.org/html/2607.09697v1#Pt0.A1.SS2 — 0.A.2 OutGuard Training and Inference Algorithms | https://arxiv.org/html/2607.09697v1#S4 — 4 Evaluation; https://arxiv.org/html/2607.09697v1#S4.SS1 — 4.1 Experiment Setup | https://arxiv.org/html/2607.09697v1#S5 — 5 Conclusion | Exact v1 links https://github.com/kunzhan/OutGuard, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-09697 | complete |
| SF-2026-ARXIV-2607-09709 | RP-ffc95e2d3ac49466 | deep | arXiv:2607.09709v1 | SRC-ARXIV@arXiv:2607.09709v1 | https://arxiv.org/html/2607.09709v1#S5 — 5 Method: launch-gated iterative self-distillation | https://arxiv.org/html/2607.09709v1#A3.SS0.SSS0.Px4 — Evaluation and statistics.; https://arxiv.org/html/2607.09709v1#S5.SS0.SSS0.Px4 — Evaluation protocol. | https://arxiv.org/html/2607.09709v1#S10 — 10 Limitations and future work; https://arxiv.org/html/2607.09709v1#S11 — 11 Conclusion | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-09709 | complete |
| SF-2026-ARXIV-2607-09711 | RP-792d230f86954d64 | standard | arXiv:2607.09711v1 | SRC-ARXIV@arXiv:2607.09711v1 | https://arxiv.org/html/2607.09711v1#A8 — Appendix H Generated Family Design Matrix | https://arxiv.org/html/2607.09711v1#A13 — Appendix M Result JSON Schema; https://arxiv.org/html/2607.09711v1#A14 — Appendix N Result Validity Checklist | https://arxiv.org/html/2607.09711v1#S6 — 6 Conclusion; https://arxiv.org/html/2607.09711v1#Sx1 — Limitations | Exact v1 links https://github.com/pzy2000/EvoClawBench/tree/anonymous, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-09711 | complete |
| SF-2026-ARXIV-2607-09744 | RP-cb766d7edaca64b3 | deep | arXiv:2607.09744v1 | SRC-ARXIV@arXiv:2607.09744v1 | https://arxiv.org/html/2607.09744v1#S6 — 6 Least Autonomy as a Design Criterion; https://arxiv.org/html/2607.09744v1#S6.SS4 — 6.4 Step-by-Step Design Procedure | https://arxiv.org/html/2607.09744v1#A2 — Appendix B Pseudocode for influence graph and least-autonomy evaluation; https://arxiv.org/html/2607.09744v1#S2.SS2 — 2.2 Workflow Authorization and Policy Analysis | https://arxiv.org/html/2607.09744v1#S8 — 8 Limitations and Future Work; https://arxiv.org/html/2607.09744v1#S9 — 9 Conclusion | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-09744 | complete |
| SF-2026-ARXIV-2607-09748 | RP-1195180fd6361652 | deep | arXiv:2607.09748v1 | SRC-ARXIV@arXiv:2607.09748v1 | https://arxiv.org/html/2607.09748v1#S6.SS1 — 6.1 System Architecture; https://arxiv.org/html/2607.09748v1#S2.SS4 — 2.4 System and Failure Model | https://arxiv.org/html/2607.09748v1#S6.SS3 — 6.3 Simulation Metrics and Results; https://arxiv.org/html/2607.09748v1#S6.SS4 — 6.4 Future Evaluation Plan | https://arxiv.org/html/2607.09748v1#S2.SS4 — 2.4 System and Failure Model; https://arxiv.org/html/2607.09748v1#S6.SS4 — 6.4 Future Evaluation Plan | Exact v1 links https://github.com/langchain-ai/langchain, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-09748 | complete |
| SF-2026-ARXIV-2607-09759 | RP-55ee83952b2c4a68 | deep | arXiv:2607.09759v1 | SRC-ARXIV@arXiv:2607.09759v1 | https://arxiv.org/html/2607.09759v1#S3.SS6 — 3.6 Retrieval and System Realization; https://arxiv.org/html/2607.09759v1#A3 — Appendix C Additional Implementation Details | https://arxiv.org/html/2607.09759v1#A2 — Appendix B Detailed Benchmark Breakdowns; https://arxiv.org/html/2607.09759v1#A7 — Appendix G Qualitative Benchmark Traces | https://arxiv.org/html/2607.09759v1#S5 — 5 Conclusion | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-09759 | complete |
| SF-2026-ARXIV-2607-09770 | RP-26b13a6edbd62ea8 | standard | arXiv:2607.09770v1 | SRC-ARXIV@arXiv:2607.09770v1 | https://arxiv.org/html/2607.09770v1#S2.SS2 — 2.2 Rule-Based Systems and Defeasible Reasoning; https://arxiv.org/html/2607.09770v1#S3 — 3 Methodological Positioning and Scope | https://arxiv.org/html/2607.09770v1#S15 — 15 Experimental Results: Detectability, Repairability, and Rejection Cases; https://arxiv.org/html/2607.09770v1#S11 — 11 Illustrative Inventory-Control Benchmark | https://arxiv.org/html/2607.09770v1#S13 — 13 Failure Classes and Repair Expectations; https://arxiv.org/html/2607.09770v1#S14 — 14 Negative Results and Failure Conditions | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-09770 | complete |
| SF-2026-ARXIV-2607-09773 | RP-315bd6061be1c054 | deep | arXiv:2607.09773v1 | SRC-ARXIV@arXiv:2607.09773v1 | https://arxiv.org/html/2607.09773v1#S5.SS1 — 5.1 Architecture Overview; https://arxiv.org/html/2607.09773v1#A4 — Appendix D Implementation Details | https://arxiv.org/html/2607.09773v1#S6 — 6 Evaluation; https://arxiv.org/html/2607.09773v1#S6.SS1 — 6.1 Experimental Setup | https://arxiv.org/html/2607.09773v1#S7 — 7 Discussion and Future Directions; https://arxiv.org/html/2607.09773v1#A5 — Appendix E Scope and Limitations | Exact v1 links https://github.com/ByteDance-Seed/Seed-1.8/, https://github.com/OpenGVLab/ScaleCUA, https://github.com/arXiv/html_feedback/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-09773 | complete |
| SF-2026-ARXIV-2607-09776 | RP-90a939fee0a01ed6 | standard | arXiv:2607.09776v1 | SRC-ARXIV@arXiv:2607.09776v1 | https://arxiv.org/html/2607.09776v1#S3.SS1 — 3.1 System Architecture; https://arxiv.org/html/2607.09776v1#S3 — 3 Framework | https://arxiv.org/html/2607.09776v1#S4.SS4 — 4.4 The Video Progress Benchmark; https://arxiv.org/html/2607.09776v1#S5 — 5 Experiments | https://arxiv.org/html/2607.09776v1#S1 — 1 Introduction; https://arxiv.org/html/2607.09776v1#S2 — 2 Related work | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-09776 | complete |
| SF-2026-ARXIV-2607-09786 | RP-c9f1b01eaa48e279 | deep | arXiv:2607.09786v1 | SRC-ARXIV@arXiv:2607.09786v1 | https://arxiv.org/html/2607.09786v1#A1.SS4 — A.4 Reinforcement Learning Implementation Details | https://arxiv.org/html/2607.09786v1#A2 — Appendix B Evaluation Protocol; https://arxiv.org/html/2607.09786v1#A2.SS1 — B.1 Evaluation Datasets | https://arxiv.org/html/2607.09786v1#S7 — 7 Limitations; https://arxiv.org/html/2607.09786v1#S8 — 8 Conclusion | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-09786 | complete |
| SF-2026-ARXIV-2607-09791 | RP-f4f8cdf9459b1695 | deep | arXiv:2607.09791v1 | SRC-ARXIV@arXiv:2607.09791v1 | https://arxiv.org/html/2607.09791v1#S4 — 4 The operator ships across the inference ecosystem | https://arxiv.org/html/2607.09791v1#S1 — 1 The penalty branches on an unconstrained coordinate; https://arxiv.org/html/2607.09791v1#S2 — 2 Consequence 1: the penalty is not well-defined (A1) | https://arxiv.org/html/2607.09791v1#S7 — 7 Conclusion | Exact v1 links https://github.com/ggml-org/llama.cpp/issues/25388, https://github.com/guidance-ai/jsonschemabench, https://github.com/ggml-org/llama.cpp/issues/2970; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-09791 | complete |
| SF-2026-ARXIV-2607-09794 | RP-44fc74a30d2f8e39 | deep | arXiv:2607.09794v1 | SRC-ARXIV@arXiv:2607.09794v1 | https://arxiv.org/html/2607.09794v1#A1.SS1 — A.1 CL-Bench Design and Contamination Prevention; https://arxiv.org/html/2607.09794v1#A2 — Appendix B Supplementary Material for Method | https://arxiv.org/html/2607.09794v1#A4.SS1 — D.1 Visualization of ablation study results.; https://arxiv.org/html/2607.09794v1#A2.SS4 — B.4 Evaluation Protocol Details | https://arxiv.org/html/2607.09794v1#A2.SS2 — B.2 Design Decisions: Extended Discussion; https://arxiv.org/html/2607.09794v1#A7 — Appendix G Additional material for discussion | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-09794 | complete |
| SF-2026-ARXIV-2607-09800 | RP-42b9a42a51b69c04 | deep | arXiv:2607.09800v1 | SRC-ARXIV@arXiv:2607.09800v1 | https://arxiv.org/html/2607.09800v1#Sx2.SSx3 — Transfer across precision, rate, and architecture; https://arxiv.org/html/2607.09800v1#Sx2.SSx4 — Transfer across optimizer, loss, and architecture | https://arxiv.org/html/2607.09800v1#Sx2 — Results; https://arxiv.org/html/2607.09800v1#Sx4.SSx1 — Experimental systems | https://arxiv.org/html/2607.09800v1#Sx3 — Discussion | Exact v1 links https://github.com/imoneoi/bf16_fused_adam, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-09800 | complete |
| SF-2026-ARXIV-2607-09802 | RP-bd6e1af187d93986 | deep | arXiv:2607.09802v1 | SRC-ARXIV@arXiv:2607.09802v1 | https://arxiv.org/html/2607.09802v1#S2 — 2 Quota Marketplace System; https://arxiv.org/html/2607.09802v1#S2.SS1 — 2.1 Market Implementation | https://arxiv.org/html/2607.09802v1#S4 — 4 Theoretical Analysis | https://arxiv.org/html/2607.09802v1#S5 — 5 Discussions and Future Directions; https://arxiv.org/html/2607.09802v1#S4.SS1 — 4.1 Limitations of Chip-Hour Mechanisms | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-09802 | complete |
| SF-2026-ARXIV-2607-09803 | RP-09f7d44a6eb7c2ff | standard | arXiv:2607.09803v1 | SRC-ARXIV@arXiv:2607.09803v1 | https://arxiv.org/html/2607.09803v1#S1 — 1 Introduction; https://arxiv.org/html/2607.09803v1#S2 — 2 Related Work | https://arxiv.org/html/2607.09803v1#S4.SS5 — 4.5 Analysis Experiments; https://arxiv.org/html/2607.09803v1#S4 — 4 Experiments | https://arxiv.org/html/2607.09803v1#S3.SS8 — 3.8 Discussion; https://arxiv.org/html/2607.09803v1#S4.SS6 — 4.6 Discussion | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-09803 | complete |
| SF-2026-ARXIV-2607-09804 | RP-bca130a99ed104ee | deep | arXiv:2607.09804v1 | SRC-ARXIV@arXiv:2607.09804v1 | https://arxiv.org/html/2607.09804v1#S4 — IV Methods | https://arxiv.org/html/2607.09804v1#A1 — Appendix A Full concept manner results; https://arxiv.org/html/2607.09804v1#S4.SS6 — IV-F Metrics and statistical analysis | https://arxiv.org/html/2607.09804v1#S3 — III Threat Model; https://arxiv.org/html/2607.09804v1#S5.SS5 — V-E Qualitative failure modes | Exact v1 links https://huggingface.co/google/medgemma-4b-it, https://huggingface.co/MoritzLaurer/DeBERTa-v3-base-mnli-fever-anli, https://github.com/arXiv/html_feedback/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-09804 | complete |
| SF-2026-ARXIV-2607-09822 | RP-f66986ee9fd3bd9e | standard | arXiv:2607.09822v1 | SRC-ARXIV@arXiv:2607.09822v1 | https://arxiv.org/html/2607.09822v1#S3 — 3 Method; https://arxiv.org/html/2607.09822v1#S5.SS2 — 5.2 Relation to Dialogue Memory Systems | https://arxiv.org/html/2607.09822v1#S4 — 4 Experiments; https://arxiv.org/html/2607.09822v1#S4.SS2 — 4.2 Memory Ablation | https://arxiv.org/html/2607.09822v1#S5 — 5 Discussion; https://arxiv.org/html/2607.09822v1#S5.SS4 — 5.4 Limitations | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-09822 | complete |
| SF-2026-ARXIV-2607-09889 | RP-e2a16b95f228e797 | standard | arXiv:2607.09889v1 | SRC-ARXIV@arXiv:2607.09889v1 | https://arxiv.org/html/2607.09889v1#S2 — 2 Method; https://arxiv.org/html/2607.09889v1#S3.SS1 — 3.1 Approach I: the static Dirichlet-process cache | https://arxiv.org/html/2607.09889v1#S3 — 3 Experiments | https://arxiv.org/html/2607.09889v1#S4 — 4 Scope, limitations, and future work | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-09889 | complete |
| SF-2026-ARXIV-2607-09992 | RP-79f6351819111922 | deep | arXiv:2607.09992v1 | SRC-ARXIV@arXiv:2607.09992v1 | https://arxiv.org/html/2607.09992v1#S2 — 2 The guard: learned proposes, verified disposes; https://arxiv.org/html/2607.09992v1#S3 — 3 When can a cheap static screen be trusted? | https://arxiv.org/html/2607.09992v1#S2.SS0.SSS0.Px4 — The operating envelope; https://arxiv.org/html/2607.09992v1#S2.SS0.SSS0.Px5 — Versus vLLM's own priority scheduler | https://arxiv.org/html/2607.09992v1#S5.SS0.SSS0.Px1 — Scope: what we can and cannot evaluate; https://arxiv.org/html/2607.09992v1#S6 — 6 Conclusion | Exact v1 links https://github.com/vllm-project/vllm/issues/40004, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-09992 | complete |
| SF-2026-ARXIV-2607-09996 | RP-c72d222272bc96a5 | standard | arXiv:2607.09996v1 | SRC-ARXIV@arXiv:2607.09996v1 | https://arxiv.org/html/2607.09996v1#A5.SS1 — E.1 Failure Attribution: Benchmarks and Methods; https://arxiv.org/html/2607.09996v1#A5.SS2 — E.2 Self-Evolving Agentic Systems | https://arxiv.org/html/2607.09996v1#A4 — Appendix D More Results and Analysis; https://arxiv.org/html/2607.09996v1#A4.SS1 — D.1 Full results on Ablation Set | https://arxiv.org/html/2607.09996v1#A1 — Appendix A Limitations and Broader Impacts; https://arxiv.org/html/2607.09996v1#A1.SS1 — A.1 Limitations | Exact v1 links https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro, https://github.com/meta-llama/llama-models/blob/main/models/llama4/MODEL_CARD.md, https://github.com/huggingface/smolagents; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-09996 | complete |
| SF-2026-ARXIV-2607-09999 | RP-a2aacb766654271c | deep | arXiv:2607.09999v1 | SRC-ARXIV@arXiv:2607.09999v1 | https://arxiv.org/pdf/2607.09999v1#page=2 — PDF page 2; https://arxiv.org/pdf/2607.09999v1#page=3 — PDF page 3 | https://arxiv.org/pdf/2607.09999v1#page=4 — PDF page 4; https://arxiv.org/pdf/2607.09999v1#page=5 — PDF page 5 | https://arxiv.org/pdf/2607.09999v1#page=6 — PDF page 6; https://arxiv.org/pdf/2607.09999v1#page=7 — PDF page 7 | Not Disclosed — exact v1 exposes no uniquely versioned artifact locator used to enlarge the manuscript claim boundary. | claim:SF-2026-ARXIV-2607-09999 | complete |
| SF-2026-ARXIV-2607-10044 | RP-a5de7a7caa6b11a8 | deep | arXiv:2607.10044v1 | SRC-ARXIV@arXiv:2607.10044v1 | https://arxiv.org/html/2607.10044v1#A2 — Appendix B CPU Baselines: Full Design Details and System Contrast; https://arxiv.org/html/2607.10044v1#A2.SS3 — B.3 Axis-by-Axis System Contrast | https://arxiv.org/html/2607.10044v1#A10 — Appendix J Full Ablations: Binary-Search and Linear-Search Variants; https://arxiv.org/html/2607.10044v1#A11 — Appendix K NQ + GENRE Workload Construction and Realistic-Threshold Analysis | https://arxiv.org/html/2607.10044v1#S5 — 5 Limitations; https://arxiv.org/html/2607.10044v1#Sx1 — Discussion | Exact v1 links https://github.com/s-yata/marisa-trie, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-10044 | complete |
| SF-2026-ARXIV-2607-10059 | RP-2e935e4fea6ac203 | deep | arXiv:2607.10059v1 | SRC-ARXIV@arXiv:2607.10059v1 | https://arxiv.org/html/2607.10059v1#A2 — Appendix B Formal Framework; https://arxiv.org/html/2607.10059v1#A2.SS5 — B.5 Paired Task Design | https://arxiv.org/html/2607.10059v1#A6 — Appendix F Full Results and Analysis; https://arxiv.org/html/2607.10059v1#A2.SS6 — B.6 Evaluation Metrics | https://arxiv.org/html/2607.10059v1#A1 — Appendix A Limitations, Future Work, and Broader Impact; https://arxiv.org/html/2607.10059v1#A1.SS1 — A.1 Limitations | Exact v1 links https://huggingface.co/MiniMaxAI/MiniMax-M2.5, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-10059 | complete |
| SF-2026-ARXIV-2607-10079 | RP-2b848154550a550a | standard | arXiv:2607.10079v1 | SRC-ARXIV@arXiv:2607.10079v1 | https://arxiv.org/html/2607.10079v1#S1 — 1 Introduction; https://arxiv.org/html/2607.10079v1#S2 — 2 Related Work | https://arxiv.org/html/2607.10079v1#A4 — Appendix D Metric Definitions and Evaluation Protocol; https://arxiv.org/html/2607.10079v1#A6 — Appendix F Full Results | https://arxiv.org/html/2607.10079v1#S7 — 7 Conclusion; https://arxiv.org/html/2607.10079v1#Sx1 — Limitations | Exact v1 links https://huggingface.co/Qwen/Qwen3.5-9B, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-10079 | complete |
| SF-2026-ARXIV-2607-10096 | RP-5bfd4c531f38a1df | standard | arXiv:2607.10096v1 | SRC-ARXIV@arXiv:2607.10096v1 | https://arxiv.org/html/2607.10096v1#S2 — 2. Methodology; https://arxiv.org/html/2607.10096v1#S2.SS1 — 2.1. Model Architecture | https://arxiv.org/html/2607.10096v1#S3.SS2 — 3.2. Offline Experiments Results; https://arxiv.org/html/2607.10096v1#S3 — 3. Offline Experiments | https://arxiv.org/html/2607.10096v1#S5 — 5. Conclusion | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-10096 | complete |
| SF-2026-ARXIV-2607-10103 | RP-0d27ae2c9994c858 | standard | arXiv:2607.10103v1 | SRC-ARXIV@arXiv:2607.10103v1 | https://arxiv.org/html/2607.10103v1#S2 — 2 Large Language Models and Risks; https://arxiv.org/html/2607.10103v1#S2.SS1 — 2.1 Large Language Models | https://arxiv.org/html/2607.10103v1#S1 — 1 Introduction; https://arxiv.org/html/2607.10103v1#S2 — 2 Large Language Models and Risks | https://arxiv.org/html/2607.10103v1#S6 — 6 Conclusion | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-10103 | complete |
| SF-2026-ARXIV-2607-10110 | RP-2b968b1c7bcb307e | deep | arXiv:2607.10110v1 | SRC-ARXIV@arXiv:2607.10110v1 | https://arxiv.org/html/2607.10110v1#S3 — 3 Proposed Method; https://arxiv.org/html/2607.10110v1#S3.SS1 — 3.1 Overall Architecture | https://arxiv.org/html/2607.10110v1#A1 — Appendix A Full Results for iso-FLOPs Evaluation; https://arxiv.org/html/2607.10110v1#A6 — Appendix F Fixed-Loop Inference Ablation | https://arxiv.org/html/2607.10110v1#S6 — 6 Conclusion; https://arxiv.org/html/2607.10110v1#Sx1 — Limitations | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-10110 | complete |
| SF-2026-ARXIV-2607-10139 | RP-6fa0871c8bb179e8 | deep | arXiv:2607.10139v1 | SRC-ARXIV@arXiv:2607.10139v1 | https://arxiv.org/html/2607.10139v1#S3 — 3 Cross-Model Consensus as a Verifier; https://arxiv.org/html/2607.10139v1#S5.SS1 — 5.1 Cross-model consensus is a strong Best-of- verifier | https://arxiv.org/html/2607.10139v1#A1 — Appendix A Experimental Setup; https://arxiv.org/html/2607.10139v1#A11 — Appendix K Additional Verifier Results | https://arxiv.org/html/2607.10139v1#S6 — 6 Conclusion | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-10139 | complete |
| SF-2026-ARXIV-2607-10152 | RP-3dbe2e15f04aad3b | standard | arXiv:2607.10152v1 | SRC-ARXIV@arXiv:2607.10152v1 | https://arxiv.org/html/2607.10152v1#S1 — 1 Introduction; https://arxiv.org/html/2607.10152v1#S2 — 2 Consensus as Communication | https://arxiv.org/html/2607.10152v1#S1 — 1 Introduction; https://arxiv.org/html/2607.10152v1#S2 — 2 Consensus as Communication | https://arxiv.org/html/2607.10152v1#S10 — 10 Discussion; https://arxiv.org/html/2607.10152v1#S11 — 11 Future Work | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-10152 | complete |
| SF-2026-ARXIV-2607-10183 | RP-564efd969d943bd5 | deep | arXiv:2607.10183v1 | SRC-ARXIV@arXiv:2607.10183v1 | https://arxiv.org/html/2607.10183v1#S2.SS1 — 2.1. CPU and GPU Architecture for Hybrid Inference; https://arxiv.org/html/2607.10183v1#S4 — 4. ATSInfer Design | https://arxiv.org/html/2607.10183v1#S5 — 5. Evaluation; https://arxiv.org/html/2607.10183v1#S5.SS1 — 5.1. Experimental Setup | https://arxiv.org/html/2607.10183v1#S7 — 7. Conclusion | Exact v1 links https://github.com/ggerganov/llama.cpp, https://github.com/huggingface/accelerate, https://github.com/arXiv/html_feedback/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-10183 | complete |
| SF-2026-ARXIV-2607-10186 | RP-853c6688b917aef6 | deep | arXiv:2607.10186v1 | SRC-ARXIV@arXiv:2607.10186v1 | https://arxiv.org/html/2607.10186v1#S6 — 6. System Design; https://arxiv.org/html/2607.10186v1#S3.SS3 — 3.3. System Resource Management | https://arxiv.org/html/2607.10186v1#S7.SS2 — 7.2. Evaluation Results; https://arxiv.org/html/2607.10186v1#S7 — 7. Evaluation | https://arxiv.org/html/2607.10186v1#S9 — 9. Conclusion | Exact v1 links https://github.com/badlogic/pi-mono, https://github.com/deepseek-ai/open-infra-index/blob/main/202502OpenSourceWeek/day_6_one_more_thing_deepseekV3R1_inference_system_overview.md, https://github.com/huggingface/accelerate; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-10186 | complete |
| SF-2026-ARXIV-2607-10198 | RP-ca94b19f49826e3a | deep | arXiv:2607.10198v1 | SRC-ARXIV@arXiv:2607.10198v1 | https://arxiv.org/html/2607.10198v1#S1 — 1 Introduction; https://arxiv.org/html/2607.10198v1#S2 — 2 Related Work | https://arxiv.org/html/2607.10198v1#A6 — Appendix F Results; https://arxiv.org/html/2607.10198v1#S3 — 3 Experimental Protocol | https://arxiv.org/html/2607.10198v1#S5.SS5 — 5.5 Many failures occur despite visible answer text; https://arxiv.org/html/2607.10198v1#S6 — 6 Discussion | Exact v1 links https://github.com/selvamsriram/search-api-decision-surface, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-10198 | complete |
| SF-2026-ARXIV-2607-10203 | RP-2f4ba872e2cba225 | deep | arXiv:2607.10203v1 | SRC-ARXIV@arXiv:2607.10203v1 | https://arxiv.org/html/2607.10203v1#A1 — Appendix A Architecture and hyperparameters; https://arxiv.org/html/2607.10203v1#S10.SS0.SSS0.Px1 — Implications for adaptive-compute world models. | https://arxiv.org/html/2607.10203v1#S10.SS0.SSS0.Px2 — Implications for latent-model evaluation.; https://arxiv.org/html/2607.10203v1#S2.SS0.SSS0.Px3 — Evaluation of latent models. | https://arxiv.org/html/2607.10203v1#S10 — 10 Discussion; https://arxiv.org/html/2607.10203v1#S11 — 11 Limitations | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-10203 | complete |
| SF-2026-ARXIV-2607-10226 | RP-1d4af7269e04a6d0 | standard | arXiv:2607.10226v1 | SRC-ARXIV@arXiv:2607.10226v1 | https://arxiv.org/html/2607.10226v1#S5.SS3 — 5.3 RQ3: The Clean Regime Is Scale- and Architecture-Dependent; https://arxiv.org/html/2607.10226v1#S4.SS1 — 4.1 Models and SAEs | https://arxiv.org/html/2607.10226v1#S2.SS3 — 2.3 Safety Evaluation Artifacts; https://arxiv.org/html/2607.10226v1#S3 — 3 Matched Coherence-Gated Evaluation | https://arxiv.org/html/2607.10226v1#S6 — 6 Discussion; https://arxiv.org/html/2607.10226v1#S7 — 7 Limitations | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-10226 | complete |
| SF-2026-ARXIV-2607-10240 | RP-ce0f1c1f167c1d66 | standard | arXiv:2607.10240v1 | SRC-ARXIV@arXiv:2607.10240v1 | https://arxiv.org/html/2607.10240v1#S3 — 3. Framework | https://arxiv.org/html/2607.10240v1#S3.SS3 — 3.3. Measuring Benchmark Undercount; https://arxiv.org/html/2607.10240v1#S4 — 4. Experimental Setup | https://arxiv.org/html/2607.10240v1#S6 — 6. Discussion; https://arxiv.org/html/2607.10240v1#S7 — 7. Conclusion | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-10240 | complete |
| SF-2026-ARXIV-2607-10252 | RP-c63f32e2f54aa4dc | standard | arXiv:2607.10252v1 | SRC-ARXIV@arXiv:2607.10252v1 | https://arxiv.org/html/2607.10252v1#S4 — IV Method; https://arxiv.org/html/2607.10252v1#S6.SS4 — VI-D RQ4: Ecosystem Anomalies | https://arxiv.org/html/2607.10252v1#S5 — V Experimental Setup; https://arxiv.org/html/2607.10252v1#S6 — VI Results | https://arxiv.org/html/2607.10252v1#S3 — III Threat Model; https://arxiv.org/html/2607.10252v1#S7 — VII Discussion | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-10252 | complete |
| SF-2026-ARXIV-2607-10265 | RP-b096ead04b396bed | deep | arXiv:2607.10265v1 | SRC-ARXIV@arXiv:2607.10265v1 | https://arxiv.org/html/2607.10265v1#S6 — 6 Findings from live model traffic | https://arxiv.org/html/2607.10265v1#S5 — 5 Evaluation; https://arxiv.org/html/2607.10265v1#S5.SS1 — 5.1 Benchmark and protocol | https://arxiv.org/html/2607.10265v1#S8 — 8 Limitations and roadmap; https://arxiv.org/html/2607.10265v1#S9 — 9 Conclusion | Exact v1 links https://github.com/zxf-work/tgms, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-10265 | complete |
| SF-2026-ARXIV-2607-10291 | RP-1d30405285f54158 | standard | arXiv:2607.10291v1 | SRC-ARXIV@arXiv:2607.10291v1 | https://arxiv.org/html/2607.10291v1#S4.SS3 — IV-C System Architecture (C2); https://arxiv.org/html/2607.10291v1#S4 — IV Methodology | https://arxiv.org/html/2607.10291v1#S5 — V Evaluation; https://arxiv.org/html/2607.10291v1#S5.SS3 — V-C Experimental Setup | https://arxiv.org/html/2607.10291v1#S5.SS6 — V-F Discussion; https://arxiv.org/html/2607.10291v1#S5.SS7 — V-G Threats To Validity | Exact v1 links https://github.com/manavpatnaik/frama-c-problems, https://huggingface.co/moonshotai/Kimi-K2.6, https://github.com/shrBadihi/EqBench/issues/15; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-10291 | complete |
| SF-2026-ARXIV-2607-10350 | RP-993d12d7a0d1f16e | standard | arXiv:2607.10350v1 | SRC-ARXIV@arXiv:2607.10350v1 | https://arxiv.org/html/2607.10350v1#S2 — 2 Agent Framework; https://arxiv.org/html/2607.10350v1#S2.SS1 — 2.1 Architecture Overview | https://arxiv.org/html/2607.10350v1#S3.SS2 — 3.2 Benchmark Construction; https://arxiv.org/html/2607.10350v1#S3.SS3 — 3.3 Evaluation Procedure and Metrics | https://arxiv.org/html/2607.10350v1#S6 — 6 Conclusion | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-10350 | complete |
| SF-2026-ARXIV-2607-10362 | RP-d63043e26940b469 | deep | arXiv:2607.10362v1 | SRC-ARXIV@arXiv:2607.10362v1 | https://arxiv.org/html/2607.10362v1#S5.SS1 — 5.1 A theory-guided intervention: linear state readout | https://arxiv.org/html/2607.10362v1#S5.SS2 — 5.2 Control experiments on latent world models; https://arxiv.org/html/2607.10362v1#S5.SS3 — 5.3 Cross-task validation of the state readout | https://arxiv.org/html/2607.10362v1#S6 — 6 Discussion and Outlook; https://arxiv.org/html/2607.10362v1#S7 — 7 Conclusion | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-10362 | complete |
| SF-2026-ARXIV-2607-10389 | RP-a2333a5840dae5b2 | deep | arXiv:2607.10389v1 | SRC-ARXIV@arXiv:2607.10389v1 | https://arxiv.org/html/2607.10389v1#A7 — Appendix G Cross-architecture readout detail; https://arxiv.org/html/2607.10389v1#S5 — 5. Design and Implementation | https://arxiv.org/html/2607.10389v1#S6 — 6. Evaluation; https://arxiv.org/html/2607.10389v1#S3 — 3. Measurement Study | https://arxiv.org/html/2607.10389v1#S8 — 8. Limitations and Open Problems | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-10389 | complete |
| SF-2026-ARXIV-2607-10463 | RP-6f987900318aa6c6 | standard | arXiv:2607.10463v1 | SRC-ARXIV@arXiv:2607.10463v1 | https://arxiv.org/html/2607.10463v1#S3 — 3 Methodology; https://arxiv.org/html/2607.10463v1#S3.SS1 — 3.1 Action Design | https://arxiv.org/html/2607.10463v1#S4 — 4 Experimental Setup; https://arxiv.org/html/2607.10463v1#S4.SS4 — 4.4 Evaluation Metrics | https://arxiv.org/html/2607.10463v1#S6 — 6 Conclusion and Future Work; https://arxiv.org/html/2607.10463v1#Sx1 — Limitations | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-10463 | complete |
| SF-2026-ARXIV-2607-10491 | RP-7e23d33f17d16413 | deep | arXiv:2607.10491v1 | SRC-ARXIV@arXiv:2607.10491v1 | https://arxiv.org/html/2607.10491v1#S3 — 3 Methodology; https://arxiv.org/html/2607.10491v1#S6.SS1 — 6.1 Implications for expert and intelligent retrieval systems | https://arxiv.org/html/2607.10491v1#S4 — 4 Experimental setup; https://arxiv.org/html/2607.10491v1#S4.SS4 — 4.4 Evaluation metrics | https://arxiv.org/html/2607.10491v1#S6.SS4 — 6.4 Limitations and threats to validity; https://arxiv.org/html/2607.10491v1#S6 — 6 Discussion | Exact v1 links https://dx.doi.org/10.18653/v1/2020.emnlp-demos.6, https://aclanthology.org/2020.emnlp-demos.6/, https://github.com/arXiv/html_feedback/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-10491 | complete |
| SF-2026-ARXIV-2607-10582 | RP-e537e745c7be7b36 | deep | arXiv:2607.10582v1 | SRC-ARXIV@arXiv:2607.10582v1 | https://arxiv.org/html/2607.10582v1#S3 — III Proposed Method | https://arxiv.org/html/2607.10582v1#S4 — IV Evaluation | https://arxiv.org/html/2607.10582v1#S5 — V Discussion and Limitations | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-10582 | complete |
| SF-2026-ARXIV-2607-10661 | RP-8b7570953255c896 | deep | arXiv:2607.10661v1 | SRC-ARXIV@arXiv:2607.10661v1 | https://arxiv.org/html/2607.10661v1#S3 — 3 Methodology; https://arxiv.org/html/2607.10661v1#A4 — Appendix D Progressive Tree Drafting Decoding Algorithm | https://arxiv.org/html/2607.10661v1#A3 — Appendix C Overhead Analysis; https://arxiv.org/html/2607.10661v1#A7 — Appendix G Generation Quality Evaluation: A Comparison Between PTD and Autoregressive Decoding under the Sampling Strategy | https://arxiv.org/html/2607.10661v1#S5 — 5 Conclusion | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-10661 | complete |
| SF-2026-ARXIV-2607-10709 | RP-30e7b74d7082e8a7 | deep | arXiv:2607.10709v1 | SRC-ARXIV@arXiv:2607.10709v1 | https://arxiv.org/html/2607.10709v1#S4 — IV Methodology; https://arxiv.org/html/2607.10709v1#S3.SS2 — III-B Threat Model | https://arxiv.org/html/2607.10709v1#S5.SS2 — V-B Experimental Results; https://arxiv.org/html/2607.10709v1#S5 — V Experiments | https://arxiv.org/html/2607.10709v1#S3.SS2 — III-B Threat Model; https://arxiv.org/html/2607.10709v1#S6 — VI Conclusion | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-10709 | complete |
| SF-2026-ARXIV-2607-10712 | RP-1361714b7dff6f36 | deep | arXiv:2607.10712v1 | SRC-ARXIV@arXiv:2607.10712v1 | https://arxiv.org/html/2607.10712v1#S1.SS1 — 1.1 Our approach; https://arxiv.org/html/2607.10712v1#S2.SS2 — 2.2 Poisoning attacks and defenses for AI systems | https://arxiv.org/html/2607.10712v1#S3.SS3 — 3.3 Experimental setup; https://arxiv.org/html/2607.10712v1#S4 — 4 Results | https://arxiv.org/html/2607.10712v1#S3.SS1 — 3.1 Threat Model; https://arxiv.org/html/2607.10712v1#S6 — 6 Discussion | Exact v1 links https://github.com/gyevnarb/indirect-data-poisoning, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-10712 | complete |
| SF-2026-ARXIV-2607-10750 | RP-6ca1bee138b4ebaf | deep | arXiv:2607.10750v1 | SRC-ARXIV@arXiv:2607.10750v1 | https://arxiv.org/html/2607.10750v1#S2 — 2 Methodology; https://arxiv.org/html/2607.10750v1#S2.SS1 — 2.1 Model | https://arxiv.org/html/2607.10750v1#A1 — Appendix A Tool call naming analysis; https://arxiv.org/html/2607.10750v1#S2.SS4 — 2.4 Evaluation | https://arxiv.org/html/2607.10750v1#S4 — 4 Discussion; https://arxiv.org/html/2607.10750v1#S5 — 5 Limitations | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-10750 | complete |
| SF-2026-ARXIV-2607-10798 | RP-05d6ee99a9a9cfe2 | deep | arXiv:2607.10798v1 | SRC-ARXIV@arXiv:2607.10798v1 | https://arxiv.org/html/2607.10798v1#S4 — 4 Methods; https://arxiv.org/html/2607.10798v1#A13 — Appendix M Cross-Model Generalization Details | https://arxiv.org/html/2607.10798v1#A10 — Appendix J Cost and Latency Analysis; https://arxiv.org/html/2607.10798v1#A3 — Appendix C Per-Dataset QIMG-7 Results | https://arxiv.org/html/2607.10798v1#S7 — 7 Conclusion and Future Work; https://arxiv.org/html/2607.10798v1#S3 — 3 Benchmark and Threat Model | Exact v1 links https://github.com/SaadElDine/Trust_Before_Fusion, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-10798 | complete |
| SF-2026-ARXIV-2607-10855 | RP-5d12e6ac62bc97a5 | standard | arXiv:2607.10855v1 | SRC-ARXIV@arXiv:2607.10855v1 | https://arxiv.org/html/2607.10855v1#A1.SS1 — A.1 Quantization methods; https://arxiv.org/html/2607.10855v1#A8 — Appendix H Are the bit-level inference scalings consistent across different quantization methods? | https://arxiv.org/html/2607.10855v1#A1 — Appendix A Additional details on the experimental setting; https://arxiv.org/html/2607.10855v1#A1.SS2 — A.2 Evaluation datasets and generation | https://arxiv.org/html/2607.10855v1#S5.SS3 — 5.3 Discussion and limitations; https://arxiv.org/html/2607.10855v1#S6 — 6 Conclusion | Exact v1 links https://github.com/bitsandbytes-foundation/bitsandbytes, https://huggingface.co/docs/optimum/quanto/index, https://github.com/arXiv/html_feedback/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-10855 | complete |
| SF-2026-ARXIV-2607-10959 | RP-72eab4e50dcd5417 | deep | arXiv:2607.10959v1 | SRC-ARXIV@arXiv:2607.10959v1 | https://arxiv.org/html/2607.10959v1#S1.SS1 — 1.1 Prior approaches; https://arxiv.org/html/2607.10959v1#A3.SS3 — C.3 Experiments on a smaller LLaMA model | https://arxiv.org/html/2607.10959v1#A1 — Appendix A Convergence analysis (proof of Theorem 1 ); https://arxiv.org/html/2607.10959v1#A3 — Appendix C Additional experiments | https://arxiv.org/html/2607.10959v1#S5 — 5 Conclusion | Exact v1 links https://huggingface.co/datasets/cerebras/SlimPajama-627B, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-10959 | complete |
| SF-2026-ARXIV-2607-10987 | RP-3362744eaf72be01 | deep | arXiv:2607.10987v1 | SRC-ARXIV@arXiv:2607.10987v1 | https://arxiv.org/html/2607.10987v1#A1 — Appendix A Extended System Design; https://arxiv.org/html/2607.10987v1#A1.SS1 — A.1. Design Components | https://arxiv.org/html/2607.10987v1#A6 — Appendix F Evaluation Details; https://arxiv.org/html/2607.10987v1#A6.SS1 — F.1. Experiment 1 extension: TTFT Reduction | https://arxiv.org/html/2607.10987v1#S8 — 8. Limitations and Future Work; https://arxiv.org/html/2607.10987v1#S9 — 9. Conclusion | Exact v1 links https://github.com/arupcsedu/AAFLOW, https://github.com/vllm-project/vllm, https://github.com/arXiv/html_feedback/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-10987 | complete |
| SF-2026-ARXIV-2607-11070 | RP-ec41219da911c461 | deep | arXiv:2607.11070v1 | SRC-ARXIV@arXiv:2607.11070v1 | https://arxiv.org/html/2607.11070v1#S4 — 4 Method; https://arxiv.org/html/2607.11070v1#A1 — Appendix A Implementation Details | https://arxiv.org/html/2607.11070v1#S5.SS2 — 5.2 Experiment Results; https://arxiv.org/html/2607.11070v1#A1.SS1 — A.1 Training and evaluation hyperparameters | https://arxiv.org/html/2607.11070v1#S6 — 6 Conclusion | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-11070 | complete |
| SF-2026-ARXIV-2607-11079 | RP-f6fac486cccbdf79 | standard | arXiv:2607.11079v1 | SRC-ARXIV@arXiv:2607.11079v1 | https://arxiv.org/html/2607.11079v1#S1 — 1 Introduction; https://arxiv.org/html/2607.11079v1#S2 — 2 Related Work | https://arxiv.org/html/2607.11079v1#S3 — 3 Benchmark; https://arxiv.org/html/2607.11079v1#S4 — 4 Experiments | https://arxiv.org/html/2607.11079v1#S5 — 5 Discussion; https://arxiv.org/html/2607.11079v1#S6 — 6 Conclusion | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-11079 | complete |
| SF-2026-ARXIV-2607-11086 | RP-d8b3eb96a3ebaa92 | deep | arXiv:2607.11086v1 | SRC-ARXIV@arXiv:2607.11086v1 | https://arxiv.org/html/2607.11086v1#S4 — 4. Characterize MCP Ecosystem; https://arxiv.org/html/2607.11086v1#S2.SS1 — 2.1. Model Context Protocol | https://arxiv.org/html/2607.11086v1#S5.SS2 — 5.2. Result Analysis; https://arxiv.org/html/2607.11086v1#A2 — Appendix B Scanner Analysis Logic | https://arxiv.org/html/2607.11086v1#S6 — 6. Discussion; https://arxiv.org/html/2607.11086v1#S6.SS2 — 6.2. Limitation | Exact v1 links https://github.com/aira-security/mcp-armor, https://github.com/antgroup/MCPScan, https://github.com/cisco-ai-defense/mcp-scanner; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-11086 | complete |
| SF-2026-ARXIV-2607-11131 | RP-f3d5e46e80bbb04f | deep | arXiv:2607.11131v1 | SRC-ARXIV@arXiv:2607.11131v1 | https://arxiv.org/html/2607.11131v1#A1 — Appendix A Method Details; https://arxiv.org/html/2607.11131v1#S3 — 3 Method | https://arxiv.org/html/2607.11131v1#A3.SS3 — C.3 Evaluation Benchmarks; https://arxiv.org/html/2607.11131v1#A1.SS1 — A.1 Cost and Complexity Analysis | https://arxiv.org/html/2607.11131v1#S4 — 4 Experiments & Discussion; https://arxiv.org/html/2607.11131v1#S5 — 5 Conclusion | Exact v1 links https://huggingface.co/liuhaotian/llava-v1.6-vicuna-7b, https://huggingface.co/liuhaotian/llava-v1.6-vicuna-13b, https://huggingface.co/Qwen/Qwen3-VL-4B-Instruct; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-11131 | complete |
| SF-2026-ARXIV-2607-11136 | RP-503a9411677041b4 | deep | arXiv:2607.11136v1 | SRC-ARXIV@arXiv:2607.11136v1 | https://arxiv.org/html/2607.11136v1#S4 — 4. System Overview; https://arxiv.org/html/2607.11136v1#S8 — 8. Implementation | https://arxiv.org/html/2607.11136v1#S7.SS2 — 7.2. Memory Analysis and Latency Profiling; https://arxiv.org/html/2607.11136v1#S9 — 9. Evaluation | https://arxiv.org/html/2607.11136v1#S11 — 11. Conclusion | Exact v1 links https://docs.vllm.ai/projects/vllm-omni/en/stable/user_guide/diffusion/cpu_offload_diffusion/, https://docs.vllm.ai/projects/vllm-omni/en/latest/design/feature/hsdp/, https://docs.vllm.ai/projects/vllm-omni/en/latest/cli/serve/; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-11136 | complete |
| SF-2026-ARXIV-2607-11138 | RP-21d5a7d24f2d10a5 | deep | arXiv:2607.11138v1 | SRC-ARXIV@arXiv:2607.11138v1 | https://arxiv.org/html/2607.11138v1#S4 — IV System Model and Topological Architecture; https://arxiv.org/html/2607.11138v1#S11 — XI System Constraints and Limitations | https://arxiv.org/html/2607.11138v1#S11.SS3 — XI-C Benchmark and Evaluation Limitations; https://arxiv.org/html/2607.11138v1#S9 — IX Experimental Evaluation | https://arxiv.org/html/2607.11138v1#S11 — XI System Constraints and Limitations; https://arxiv.org/html/2607.11138v1#S11.SS3 — XI-C Benchmark and Evaluation Limitations | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-11138 | complete |
| SF-2026-ARXIV-2607-11149 | RP-6ac2c1f05950b9fd | deep | arXiv:2607.11149v1 | SRC-ARXIV@arXiv:2607.11149v1 | https://arxiv.org/html/2607.11149v1#S3.SS3 — 3.3 Measurement Methodology: Serialization Masks Duplication; https://arxiv.org/html/2607.11149v1#S4.SS2 — 4.2 Frameworks and Fairness Protocol | https://arxiv.org/html/2607.11149v1#S4 — 4 The AgentFootprint Benchmark; https://arxiv.org/html/2607.11149v1#S5 — 5 Controlled Results | https://arxiv.org/html/2607.11149v1#S8 — 8 Discussion and Limitations; https://arxiv.org/html/2607.11149v1#S9 — 9 Conclusion | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-11149 | complete |
| SF-2026-ARXIV-2607-11172 | RP-f33e0dc2c7abfff1 | deep | arXiv:2607.11172v1 | SRC-ARXIV@arXiv:2607.11172v1 | https://arxiv.org/html/2607.11172v1#A2.SS1 — B.1 Model Architecture; https://arxiv.org/html/2607.11172v1#S2 — 2 Methodology | https://arxiv.org/html/2607.11172v1#A4 — Appendix D Supplementary Experiments; https://arxiv.org/html/2607.11172v1#S3 — 3 Experiments | https://arxiv.org/html/2607.11172v1#S5 — 5 Conclusion; https://arxiv.org/html/2607.11172v1#S6 — 6 Limitations | Exact v1 links https://huggingface.co/datasets/xbench/DeepSearch, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-11172 | complete |
| SF-2026-ARXIV-2607-11183 | RP-266f44b99db4216f | standard | arXiv:2607.11183v1 | SRC-ARXIV@arXiv:2607.11183v1 | https://arxiv.org/pdf/2607.11183v1#page=1 — PDF page 1; https://arxiv.org/pdf/2607.11183v1#page=10 — PDF page 10 | https://arxiv.org/pdf/2607.11183v1#page=1 — PDF page 1; https://arxiv.org/pdf/2607.11183v1#page=10 — PDF page 10 | https://arxiv.org/pdf/2607.11183v1#page=1 — PDF page 1; https://arxiv.org/pdf/2607.11183v1#page=10 — PDF page 10 | Not Disclosed — exact v1 exposes no uniquely versioned artifact locator used to enlarge the manuscript claim boundary. | claim:SF-2026-ARXIV-2607-11183 | complete |
| SF-2026-ARXIV-2607-11226 | RP-2721843f7b16a31f | standard | arXiv:2607.11226v1 | SRC-ARXIV@arXiv:2607.11226v1 | https://arxiv.org/html/2607.11226v1#S4 — IV Cohort System Architecture and Sandbox Implementation; https://arxiv.org/html/2607.11226v1#S2.SS1 — II-A Multi-Agent Collaborative Frameworks | https://arxiv.org/html/2607.11226v1#S7 — VII Empirical Evaluation and Results; https://arxiv.org/html/2607.11226v1#S7.SS3 — VII-C Experimental Protocol and Ablation Matrix (8 Configurations over 20 Seeds) | https://arxiv.org/html/2607.11226v1#S8 — VIII Discussion and Limitations; https://arxiv.org/html/2607.11226v1#S9 — IX Conclusion and Future Work | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-11226 | complete |
| SF-2026-ARXIV-2607-11250 | RP-47156bdf6e314ea0 | deep | arXiv:2607.11250v1 | SRC-ARXIV@arXiv:2607.11250v1 | https://arxiv.org/html/2607.11250v1#S1 — 1 Introduction; https://arxiv.org/html/2607.11250v1#S2 — 2 Can LLMs Explore in Multi-Agent Environments? A Motivating Example | https://arxiv.org/html/2607.11250v1#A1 — Appendix A Appendix for the Delegation Experiment; https://arxiv.org/html/2607.11250v1#A3 — Appendix C Appendix for the Main Experiments | https://arxiv.org/html/2607.11250v1#A6 — Appendix F Limitations and Future Directions; https://arxiv.org/html/2607.11250v1#S8 — 8 Conclusion | Exact v1 links https://github.com/deeplearning-wisc/mace, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-11250 | complete |
| SF-2026-ARXIV-2607-11262 | RP-24b9e5276354ee5d | standard | arXiv:2607.11262v1 | SRC-ARXIV@arXiv:2607.11262v1 | https://arxiv.org/html/2607.11262v1#S2.SS2 — 2.2. GPU Architecture Evolution; https://arxiv.org/html/2607.11262v1#S7.SS3 — 7.3. Adapting to Latest Blackwell Architecture | https://arxiv.org/html/2607.11262v1#S6 — 6. Evaluation; https://arxiv.org/html/2607.11262v1#S6.SS1 — 6.1. Experimental Setup | https://arxiv.org/html/2607.11262v1#S6.SS4 — 6.4. Analysis and Discussion; https://arxiv.org/html/2607.11262v1#S9 — 9. Conclusion | Exact v1 links https://github.com/gpgpu-sim/gpgpu-sim_distribution, https://github.com/NVIDIA/cutlass, https://github.com/tile-ai/tilelang; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-11262 | complete |
| SF-2026-ARXIV-2607-11317 | RP-60e0620a9692600e | deep | arXiv:2607.11317v1 | SRC-ARXIV@arXiv:2607.11317v1 | https://arxiv.org/html/2607.11317v1#S3 — 3 Method | https://arxiv.org/html/2607.11317v1#S5 — 5 Experimental setup; https://arxiv.org/html/2607.11317v1#S6 — 6 Results | https://arxiv.org/html/2607.11317v1#S6.SS2 — 6.2 Observed degeneration and failure modes; https://arxiv.org/html/2607.11317v1#S7 — 7 Limitations | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-11317 | complete |
| SF-2026-ARXIV-2607-11346 | RP-c1280ea50ba3340f | deep | arXiv:2607.11346v1 | SRC-ARXIV@arXiv:2607.11346v1 | https://arxiv.org/html/2607.11346v1#S3 — 3 Method | https://arxiv.org/html/2607.11346v1#S4 — 4 Experimental Setup; https://arxiv.org/html/2607.11346v1#S5 — 5 Results | https://arxiv.org/html/2607.11346v1#S6 — 6 Discussion; https://arxiv.org/html/2607.11346v1#S7 — 7 Conclusion | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-11346 | complete |
| SF-2026-ARXIV-2607-11368 | RP-2bc9431437212eef | deep | arXiv:2607.11368v1 | SRC-ARXIV@arXiv:2607.11368v1 | https://arxiv.org/html/2607.11368v1#S2.SS8 — 2.8 Related Work: Adjacent Serving Systems; https://arxiv.org/html/2607.11368v1#S3 — 3 Methodology | https://arxiv.org/html/2607.11368v1#S3.SS6 — 3.6 Benchmark Cells; https://arxiv.org/html/2607.11368v1#S4 — 4 Experiments | https://arxiv.org/html/2607.11368v1#S5.SS6 — 5.6 Threats to Validity and Limitations; https://arxiv.org/html/2607.11368v1#S5 — 5 Discussion | Exact v1 links https://github.com/huggingface/text-generation-inference, https://github.com/NVIDIA/TensorRT-LLM, https://github.com/arXiv/html_feedback/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-11368 | complete |
| SF-2026-ARXIV-2607-11388 | RP-d9f1de1a7dc3e918 | deep | arXiv:2607.11388v1 | SRC-ARXIV@arXiv:2607.11388v1 | https://arxiv.org/html/2607.11388v1#S1 — 1 Introduction; https://arxiv.org/html/2607.11388v1#S2 — 2 Preliminaries | https://arxiv.org/html/2607.11388v1#A1 — Appendix A Additional OSWorld Results and Ablations; https://arxiv.org/html/2607.11388v1#A2 — Appendix B Web Benchmark Details | https://arxiv.org/html/2607.11388v1#A6.SS6 — F.6 Failure modes; https://arxiv.org/html/2607.11388v1#S7 — 7 Conclusion | Exact v1 links https://github.com/WenyiWU0111/StructAgent, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-11388 | complete |
| SF-2026-ARXIV-2607-11399 | RP-29852ab1aec4a3f5 | deep | arXiv:2607.11399v1 | SRC-ARXIV@arXiv:2607.11399v1 | https://arxiv.org/html/2607.11399v1#A2 — Appendix B Case Evidence for Single-Model Routing; https://arxiv.org/html/2607.11399v1#A3 — Appendix C Case Evidence for Multi-Model Ensemble Routing | https://arxiv.org/html/2607.11399v1#A3.SS1 — C.1 Case A: Fortive Segment-Level Financial Analysis; https://arxiv.org/html/2607.11399v1#S4 — 4 Experiments | https://arxiv.org/html/2607.11399v1#S6 — 6 Conclusions and Future Work | Exact v1 links https://github.com/opensquilla/opensquilla, https://github.com/NousResearch/hermes-agent, https://github.com/openclaw/openclaw; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-11399 | complete |
| SF-2026-ARXIV-2607-11414 | RP-84fe7b572ff2c204 | standard | arXiv:2607.11414v1 | SRC-ARXIV@arXiv:2607.11414v1 | https://arxiv.org/html/2607.11414v1#S4 — 4. Methods; https://arxiv.org/html/2607.11414v1#S5.SS2 — 5.2. Probe design across layers and pooling | https://arxiv.org/html/2607.11414v1#S4.SS2 — 4.2. Evaluation protocol and validity controls; https://arxiv.org/html/2607.11414v1#S5 — 5. Results | https://arxiv.org/html/2607.11414v1#S6 — 6. Discussion and limitations; https://arxiv.org/html/2607.11414v1#S7 — 7. Conclusion | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-11414 | complete |
| SF-2026-ARXIV-2607-11423 | RP-1cee400a3f1fcf61 | standard | arXiv:2607.11423v1 | SRC-ARXIV@arXiv:2607.11423v1 | https://arxiv.org/html/2607.11423v1#S2 — 2 ToFu architecture; https://arxiv.org/html/2607.11423v1#S2.SS1 — 2.1 Framework overview | https://arxiv.org/html/2607.11423v1#S4.SS2 — 4.2 Evaluation results; https://arxiv.org/html/2607.11423v1#A1 — Appendix A Human Evaluation | https://arxiv.org/html/2607.11423v1#S6 — 6 Conclusion; https://arxiv.org/html/2607.11423v1#Sx1 — Limitations | Exact v1 links https://github.com/NiuTrans/ToFu, https://github.com/rangehow/overleaf-mcp, https://www.anthropic.com/product/claude-code; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-11423 | complete |
| SF-2026-ARXIV-2607-11433 | RP-ffcc90c2f7afb508 | deep | arXiv:2607.11433v1 | SRC-ARXIV@arXiv:2607.11433v1 | https://arxiv.org/html/2607.11433v1#A1 — Appendix A Relationship to representative agent frameworks; https://arxiv.org/html/2607.11433v1#S3 — 3 Method: Omni-Decision | https://arxiv.org/html/2607.11433v1#A3 — Appendix C Finite-sample uncertainty for the main OmniGAIA result; https://arxiv.org/html/2607.11433v1#A9.SS6 — I.6 Experimental configuration | https://arxiv.org/html/2607.11433v1#S5 — 5 Discussion and limitations; https://arxiv.org/html/2607.11433v1#A4 — Appendix D Failure taxonomy and real-progress audit details | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-11433 | complete |
| SF-2026-ARXIV-2607-11436 | RP-da81b8de4936c2b5 | standard | arXiv:2607.11436v1 | SRC-ARXIV@arXiv:2607.11436v1 | https://arxiv.org/html/2607.11436v1#S2.SS3 — 2.3 Inference-Time Control for Vision-Language Models; https://arxiv.org/html/2607.11436v1#S3.SS6 — 3.6 Thinking Models Improve Relay Match and Anchoring | https://arxiv.org/html/2607.11436v1#S4.SS2 — 4.2 Main Benchmark Results; https://arxiv.org/html/2607.11436v1#S2.SS2 — 2.2 Mechanistic Analysis of Multimodal Computation | https://arxiv.org/html/2607.11436v1#S3.SS5 — 3.5 Relay Mismatch as an Evidence Assembly Failure; https://arxiv.org/html/2607.11436v1#S5 — 5 Conclusion | Exact v1 links https://github.com/gooogleshanghai/visual-relay-window, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-11436 | complete |
| SF-2026-ARXIV-2607-11444 | RP-b4e171f93b530cf1 | standard | arXiv:2607.11444v1 | SRC-ARXIV@arXiv:2607.11444v1 | https://arxiv.org/html/2607.11444v1#S3 — 3 Method; https://arxiv.org/html/2607.11444v1#A1 — Appendix A Full Algorithm | https://arxiv.org/html/2607.11444v1#S4 — 4 Experiments; https://arxiv.org/html/2607.11444v1#S4.SS2 — 4.2 Main Results | https://arxiv.org/html/2607.11444v1#S6 — 6 Conclusion | Exact v1 links https://github.com/LiveCodeBench/LiveCodeBench, https://huggingface.co/nex-agi/Nex-N2-mini, https://huggingface.co/datasets/nvidia/Nemotron-SFT-Science-v2; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-11444 | complete |
| SF-2026-ARXIV-2607-11475 | RP-eb80525fe8cd8bc6 | deep | arXiv:2607.11475v1 | SRC-ARXIV@arXiv:2607.11475v1 | https://arxiv.org/html/2607.11475v1#A4 — Appendix D Architecture Sensitivity; https://arxiv.org/html/2607.11475v1#S3 — 3 Method | https://arxiv.org/html/2607.11475v1#A6 — Appendix F Detailed Loss-Component Ablation (Table 10 ); https://arxiv.org/html/2607.11475v1#A7 — Appendix G Detailed Training-Data Ablation (Table 11 ) | https://arxiv.org/html/2607.11475v1#S5 — 5 Conclusion | Exact v1 links https://github.com/nokronim/project-safety-remedy, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-11475 | complete |
| SF-2026-ARXIV-2607-11487 | RP-709c3a6c61f17388 | standard | arXiv:2607.11487v1 | SRC-ARXIV@arXiv:2607.11487v1 | https://arxiv.org/html/2607.11487v1#S5.SS5 — 5.5 Capability Comparison with Existing Assistants and Memory Systems | https://arxiv.org/html/2607.11487v1#S5 — 5 Quantitative Evaluation; https://arxiv.org/html/2607.11487v1#S5.SS1 — 5.1 Evaluation Setup | https://arxiv.org/html/2607.11487v1#S6 — 6 Conclusion; https://arxiv.org/html/2607.11487v1#Sx1 — Limitations | Exact v1 links https://github.com/zjunlp/LightMem-Ego, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-11487 | complete |
| SF-2026-ARXIV-2607-11498 | RP-d2d73a3c9c193cca | standard | arXiv:2607.11498v1 | SRC-ARXIV@arXiv:2607.11498v1 | https://arxiv.org/html/2607.11498v1#S3 — 3 Method; https://arxiv.org/html/2607.11498v1#S4 — 4 Design Choices for Robot-Centric 3D Observations in VLAs | https://arxiv.org/html/2607.11498v1#A4 — Appendix D RoboCasa Results under Randomized Evaluation Viewpoints; https://arxiv.org/html/2607.11498v1#A2 — Appendix B Implementation Details and Experimental Setup | https://arxiv.org/html/2607.11498v1#S6 — 6 Limitations; https://arxiv.org/html/2607.11498v1#S7 — 7 Conclusion | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-11498 | complete |
| SF-2026-ARXIV-2607-11505 | RP-164523e68521421a | deep | arXiv:2607.11505v1 | SRC-ARXIV@arXiv:2607.11505v1 | https://arxiv.org/html/2607.11505v1#S3 — 3 Methodology; https://arxiv.org/html/2607.11505v1#A2.SS1 — B.1 Implementation Details | https://arxiv.org/html/2607.11505v1#A2 — Appendix B Experiment Details; https://arxiv.org/html/2607.11505v1#S2 — 2 Preliminary Analysis: Reward Optimization vs. Distribution Matching | https://arxiv.org/html/2607.11505v1#S6 — 6 Discussion and Future Works; https://arxiv.org/html/2607.11505v1#S5 — 5 Conclusion | Exact v1 links https://github.com/KnowledgeXLab/PUST, https://huggingface.co/KnowledgeXLab/PUST-Experiments, https://github.com/open-compass/opencompass; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-11505 | complete |
| SF-2026-ARXIV-2607-11506 | RP-0b9ef5e65cf66f65 | deep | arXiv:2607.11506v1 | SRC-ARXIV@arXiv:2607.11506v1 | https://arxiv.org/html/2607.11506v1#S3 — 3 The SCOPE-RL Framework; https://arxiv.org/html/2607.11506v1#A1 — Appendix A Training Algorithm | https://arxiv.org/html/2607.11506v1#A12 — Appendix L ASR Reward-Signal Ablation; https://arxiv.org/html/2607.11506v1#A16 — Appendix P Pairwise Expert Evaluation | https://arxiv.org/html/2607.11506v1#S7 — 7 Conclusion; https://arxiv.org/html/2607.11506v1#Sx1 — Limitations | Exact v1 links https://github.com/tokencraft-lab/SCOPE-RL, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-11506 | complete |
| SF-2026-ARXIV-2607-11579 | RP-32d70bef196f4069 | deep | arXiv:2607.11579v1 | SRC-ARXIV@arXiv:2607.11579v1 | https://arxiv.org/html/2607.11579v1#S4 — 4. MemExchange ’s Design; https://arxiv.org/html/2607.11579v1#S4.SS1 — 4.1. Architecture Overview | https://arxiv.org/html/2607.11579v1#S5 — 5. Evaluation; https://arxiv.org/html/2607.11579v1#S5.SS1 — 5.1. Experimental Setup | https://arxiv.org/html/2607.11579v1#S7 — 7. Discussion and Future Work; https://arxiv.org/html/2607.11579v1#S6 — 6. Conclusion | Exact v1 links https://github.com/AAMH/memcached, https://github.com/leverich/mutilate, https://github.com/arXiv/html_feedback/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-11579 | complete |
| SF-2026-ARXIV-2607-11586 | RP-5c80171d833c264c | deep | arXiv:2607.11586v1 | SRC-ARXIV@arXiv:2607.11586v1 | https://arxiv.org/html/2607.11586v1#S6 — 6 Method Design; https://arxiv.org/html/2607.11586v1#S4 — 4 System Model | https://arxiv.org/html/2607.11586v1#S7 — 7 Experimental Evaluation; https://arxiv.org/html/2607.11586v1#S7.SS1 — 7.1 Experimental Setup | https://arxiv.org/html/2607.11586v1#S8 — 8 Conclusion | Exact v1 links https://huggingface.co/Qwen/Qwen1.5-MoE-A2.7B, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-11586 | complete |
| SF-2026-ARXIV-2607-11598 | RP-33c5901ac129403c | deep | arXiv:2607.11598v1 | SRC-ARXIV@arXiv:2607.11598v1 | https://arxiv.org/html/2607.11598v1#S2 — 2 A Framework for Internal and External Test-Time Compute; https://arxiv.org/html/2607.11598v1#A2.SS6 — B.6 Cross-model replication (code) | https://arxiv.org/html/2607.11598v1#A2 — Appendix B Detailed Results and Configurations; https://arxiv.org/html/2607.11598v1#S6 — 6 Evaluation-Side Grounding: Deterministic Instruments vs. Model Judges | https://arxiv.org/html/2607.11598v1#S10 — 10 Conclusion; https://arxiv.org/html/2607.11598v1#S9 — 9 Limitations | Exact v1 links https://github.com/19PINE-AI/interaction-scaling, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-11598 | complete |
| SF-2026-ARXIV-2607-11611 | RP-6bd0dfd90834b8c7 | deep | arXiv:2607.11611v1 | SRC-ARXIV@arXiv:2607.11611v1 | https://arxiv.org/html/2607.11611v1#S5.SS1 — 5.1. Methodology; https://arxiv.org/html/2607.11611v1#S2.SS2 — 2.2. ZooLang as a Model of OCaml 5 | https://arxiv.org/html/2607.11611v1#S1 — 1. Introduction; https://arxiv.org/html/2607.11611v1#S2 — 2. Key Ideas | https://arxiv.org/html/2607.11611v1#S7 — 7. Discussion and Future Work | Exact v1 links https://code.facebook.com/posts/1648953042007882/open-sourcing-facebook-infer-identify-bugs-before-you-ship/, https://github.com/ocaml-multicore/domainslib, https://github.com/LLM4Rocq/rocq-mcp; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-11611 | complete |
| SF-2026-ARXIV-2607-11614 | RP-3eff818e826114a0 | standard | arXiv:2607.11614v1 | SRC-ARXIV@arXiv:2607.11614v1 | https://arxiv.org/html/2607.11614v1#A1 — Appendix A Formal Description of the ARMT Architecture; https://arxiv.org/html/2607.11614v1#A4.SS1 — D.1 ARMT language modeling pre-training | https://arxiv.org/html/2607.11614v1#A4 — Appendix D Additional Experimental Results; https://arxiv.org/html/2607.11614v1#A1.SS1 — A.1 FLOP Analysis | https://arxiv.org/html/2607.11614v1#S6 — 6 Conclusion; https://arxiv.org/html/2607.11614v1#Sx1 — Limitations | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-11614 | complete |
| SF-2026-ARXIV-2607-11643 | RP-3330199fbec5b609 | deep | arXiv:2607.11643v1 | SRC-ARXIV@arXiv:2607.11643v1 | https://arxiv.org/html/2607.11643v1#S2.SS2 — 2.2 Model Architecture; https://arxiv.org/html/2607.11643v1#S4.SS1 — 4.1 Foundation Generative Models and Embodied World Models | https://arxiv.org/html/2607.11643v1#S3 — 3 Experiments; https://arxiv.org/html/2607.11643v1#S3.SS3 — 3.3 Real World Experiments | https://arxiv.org/html/2607.11643v1#S5 — 5 Conclusions | Exact v1 links https://github.com/kakaobrain/coyo-dataset, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-11643 | complete |
| SF-2026-ARXIV-2607-11673 | RP-65d2607d4d22c13e | standard | arXiv:2607.11673v1 | SRC-ARXIV@arXiv:2607.11673v1 | https://arxiv.org/html/2607.11673v1#S3 — 3 Method; https://arxiv.org/html/2607.11673v1#S3.SS3 — 3.3 Exploration Trajectory Design | https://arxiv.org/html/2607.11673v1#S4 — 4 Evaluation | https://arxiv.org/html/2607.11673v1#S5 — 5 Conclusion | Exact v1 links https://github.com/ali-vilab/VACE, https://huggingface.co/datasets/spatialverse/InteriorGS, https://github.com/ModelTC/lightx2v; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-11673 | complete |
| SF-2026-ARXIV-2607-11698 | RP-4422f75d1bf0e063 | deep | arXiv:2607.11698v1 | SRC-ARXIV@arXiv:2607.11698v1 | https://arxiv.org/html/2607.11698v1#A1 — Appendix A AHA main framework; https://arxiv.org/html/2607.11698v1#S3 — 3 Method | https://arxiv.org/html/2607.11698v1#A1.SS2 — A.2 Held-out concept evaluation; https://arxiv.org/html/2607.11698v1#A2 — Appendix B Experiment details | https://arxiv.org/html/2607.11698v1#S6 — 6 Discussion; https://arxiv.org/html/2607.11698v1#S7 — 7 Conclusion | Exact v1 links https://github.com/henrymao2004/Auto-research-red-teaming, https://docs.anthropic.com/en/docs/claude-code/overview, https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro/; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-11698 | complete |
| SF-2026-ARXIV-2607-11738 | RP-3dc448d25e746ade | standard | arXiv:2607.11738v1 | SRC-ARXIV@arXiv:2607.11738v1 | https://arxiv.org/html/2607.11738v1#S2 — 2 Architecture; https://arxiv.org/html/2607.11738v1#S2.SS2 — 2.2 Model Components | https://arxiv.org/html/2607.11738v1#S4.SS2 — 4.2 Evaluation on Public Benchmarks; https://arxiv.org/html/2607.11738v1#S4 — 4 Evaluation | https://arxiv.org/html/2607.11738v1#S5 — 5 Conclusion | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-11738 | complete |
| SF-2026-ARXIV-2607-11746 | RP-2601f1efc4ed4c71 | standard | arXiv:2607.11746v1 | SRC-ARXIV@arXiv:2607.11746v1 | https://arxiv.org/html/2607.11746v1#S4 — IV HiFi-LLP Design; https://arxiv.org/html/2607.11746v1#S4.SS2 — IV-B Design Decisions | https://arxiv.org/html/2607.11746v1#S4.SS1 — IV-A Evaluation Metrics; https://arxiv.org/html/2607.11746v1#S5 — V Evaluation | https://arxiv.org/html/2607.11746v1#S6 — VI Conclusion | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-11746 | complete |
| SF-2026-ARXIV-2607-11751 | RP-cae68f0fcb2afae3 | deep | arXiv:2607.11751v1 | SRC-ARXIV@arXiv:2607.11751v1 | https://arxiv.org/html/2607.11751v1#A5.SS1 — E.1 Full per-model ASR | https://arxiv.org/html/2607.11751v1#A2 — Appendix B Experimental details and statistics | https://arxiv.org/html/2607.11751v1#S7 — 7 Discussion and conclusion | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-11751 | complete |
| SF-2026-ARXIV-2607-11796 | RP-7a994256f7efe3c7 | standard | arXiv:2607.11796v1 | SRC-ARXIV@arXiv:2607.11796v1 | https://arxiv.org/html/2607.11796v1#S1 — 1 Introduction; https://arxiv.org/html/2607.11796v1#S2 — 2 Related Work | https://arxiv.org/html/2607.11796v1#S1 — 1 Introduction; https://arxiv.org/html/2607.11796v1#S2 — 2 Related Work | https://arxiv.org/html/2607.11796v1#S5 — 5 Limitations; https://arxiv.org/html/2607.11796v1#S6 — 6 Conclusion | Exact v1 links https://github.com/isrlab/selective-layer-audit, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-11796 | complete |
| SF-2026-ARXIV-2607-11818 | RP-234fa849f1331c15 | standard | arXiv:2607.11818v1 | SRC-ARXIV@arXiv:2607.11818v1 | https://arxiv.org/html/2607.11818v1#A3.SS1 — C.1 Study Design; https://arxiv.org/html/2607.11818v1#S3.SS1 — 3.1 Architecture | https://arxiv.org/html/2607.11818v1#A2 — Appendix B Benchmarking Results without Failed User Simulators; https://arxiv.org/html/2607.11818v1#A1 — Appendix A Evaluation Protocol Details | https://arxiv.org/html/2607.11818v1#S6.SS4 — 6.4 Failure Analysis; https://arxiv.org/html/2607.11818v1#S7 — 7 Conclusion | Exact v1 links https://github.com/apple/ml-mmtoolsandbox, https://developers.googleblog.com/introducing-a2ui-an-open-project-for-agent-driven-interfaces/, https://github.com/arXiv/html_feedback/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-11818 | complete |
| SF-2026-ARXIV-2607-11836 | RP-07dbd4272e82ac62 | standard | arXiv:2607.11836v1 | SRC-ARXIV@arXiv:2607.11836v1 | https://arxiv.org/html/2607.11836v1#S3 — 3 Methodology; https://arxiv.org/html/2607.11836v1#Pt0.A3 — Appendix 0.C Algorithm for Cycle-Guided Inference | https://arxiv.org/html/2607.11836v1#Pt0.A5 — Appendix 0.E Physical Consistency Evaluation Metrics; https://arxiv.org/html/2607.11836v1#Pt0.A6 — Appendix 0.F Extended Evaluation on Physical Consistency | https://arxiv.org/html/2607.11836v1#S5 — 5 Conclusion | Exact v1 links https://szhcz.github.io/projects/Cycle-World/, https://github.com/SkyworkAI/Matrix-Game/blob/main/Matrix-Game-3/assets/pdf/report.pdf, https://github.com/arXiv/html_feedback/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-11836 | complete |
| SF-2026-ARXIV-2607-11862 | RP-6a487fefe162ead5 | standard | arXiv:2607.11862v1 | SRC-ARXIV@arXiv:2607.11862v1 | https://arxiv.org/html/2607.11862v1#S3.SS1 — 3.1 Benchmark Design: ST-Evidence; https://arxiv.org/html/2607.11862v1#S5.SS3 — 5.3 A Baseline Model for the E-VQA Task | https://arxiv.org/html/2607.11862v1#S5.SS2 — 5.2 Experimental Results on ST-Evidence; https://arxiv.org/html/2607.11862v1#S3.SS1 — 3.1 Benchmark Design: ST-Evidence | https://arxiv.org/html/2607.11862v1#S6 — 6 Conclusion | Exact v1 links https://github.com/SalesforceAIResearch/EVQA, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-11862 | complete |
| SF-2026-ARXIV-2607-11871 | RP-1301b3839b98dece | standard | arXiv:2607.11871v1 | SRC-ARXIV@arXiv:2607.11871v1 | https://arxiv.org/html/2607.11871v1#A1.SS3 — A.3 Detailed Comparison to the Closest Methods; https://arxiv.org/html/2607.11871v1#A10.SS6 — J.6 Per-Layer, Per-Method Attack Tables | https://arxiv.org/html/2607.11871v1#A10 — Appendix J Complete Attack Results; https://arxiv.org/html/2607.11871v1#A11 — Appendix K Defense Results | https://arxiv.org/html/2607.11871v1#A7.SS1 — G.1 Error Analysis: Generation Failures and Score Parsing; https://arxiv.org/html/2607.11871v1#A8 — Appendix H Limitations and Scope | Exact v1 links https://huggingface.co/meta-llama/Llama-3.1-8B, https://huggingface.co/meta-llama/Llama-3.3-70B-Instruct, https://huggingface.co/Qwen/Qwen2.5-72B; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-11871 | complete |
| SF-2026-ARXIV-2607-11883 | RP-2419a3f75647ccc1 | standard | arXiv:2607.11883v1 | SRC-ARXIV@arXiv:2607.11883v1 | https://arxiv.org/html/2607.11883v1#S3.SS1 — 3.1 Method; https://arxiv.org/html/2607.11883v1#A3.SS5 — C.5 Model Size Scaling at Fixed Data (Figure 5 ) | https://arxiv.org/html/2607.11883v1#A3 — Appendix C Experiment Details; https://arxiv.org/html/2607.11883v1#S3.SS2 — 3.2 Benchmarking Compression of Transformers Trained on Text and Images | https://arxiv.org/html/2607.11883v1#S5 — 5 Discussion | Exact v1 links https://github.com/shikaiqiu/requential-coding, https://huggingface.co/datasets/Skylion007/openwebtext, https://github.com/preetum/cifar5m; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-11883 | complete |
| SF-2026-ARXIV-2607-11886 | RP-a4d09eded212f6ad | standard | arXiv:2607.11886v1 | SRC-ARXIV@arXiv:2607.11886v1 | https://arxiv.org/html/2607.11886v1#S3 — 3 Method; https://arxiv.org/html/2607.11886v1#A2 — Appendix B Additional Implementation Details | https://arxiv.org/html/2607.11886v1#A3 — Appendix C Additional Experimental Results; https://arxiv.org/html/2607.11886v1#A4 — Appendix D Detailed Benchmark Results | https://arxiv.org/html/2607.11886v1#A1 — Appendix A Limitations and future work; https://arxiv.org/html/2607.11886v1#S5 — 5 Conclusion | Exact v1 links https://github.com/black-forest-labs/flux, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-11886 | complete |

### Source Reviews

<!-- review:SF-2026-ARXIV-2607-09665:start -->
### Format Sensitivity Index: Token-Controlled Prompt Wrapper Robustness and Schema Compliance in LLM Benchmarking

<!-- claim:SF-2026-ARXIV-2607-09665:start -->Prompt wrappers often differ only in formatting, yet they can change model scores enough to flip leaderboard conclusions. We study this variance under a token-controlled protocol and introduce two complementary metrics: the Format Sensitivity Index (FSI), the accuracy range induced by wrapper choice, and the Parseability Sensitivity Index (PSI), the corresponding range in answer parseability. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-09665:end -->

**为什么进入候选分母。** 摘要首要问题为“Prompt wrappers often differ only in formatting, yet they can change model scores enough to flip leaderboard conclusions.”；它改变了 evaluation observable、对照组、判定粒度或结果解释边界，可能修正现有评测结论。

**机制与状态边界。** We study this variance under a token-controlled protocol and introduce two complementary metrics: the Format Sensitivity Index (FSI), the accuracy range induced by wrapper choice, and the Parseability Sensitivity Index (PSI), the corresponding range in answer parseability.

**证据证明什么。** A fixed-effects regression shows that parseability remains a strong predictor of accuracy even after controlling for task, model, and wrapper.

**证据没有证明什么。** 7 Limitations First, FSI is a range statistic and can be influenced by outliers and sampling noise. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.09665v1#S3.SS1 — 3.1 Tasks and Models; https://arxiv.org/html/2607.09665v1#S5.SS1 — 5.1 Format Sensitivity Varies Sharply Across Models。Evaluation：https://arxiv.org/html/2607.09665v1#S3 — 3 Experimental Setup; https://arxiv.org/html/2607.09665v1#S5 — 5 Results。Limitations / counterevidence：https://arxiv.org/html/2607.09665v1#S6 — 6 Discussion and Recommendations; https://arxiv.org/html/2607.09665v1#S7 — 7 Limitations。

**Artifact boundary。** Exact v1 links https://github.com/EleutherAI/lm-evaluation-harness, https://github.com/stanfordnlp/synchromesh, https://github.com/arXiv/html_feedback/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：7 Limitations First, FSI is a range statistic and can be influenced by outliers and sampling noise.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`PLATFORM-EVALUATION-SYSTEM`；evidence-stage relation：`principle_reuse`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-09665:end -->

<!-- review:SF-2026-ARXIV-2607-09682:start -->
### AuditWeave: A Tamper-Evident, Auditor-Navigable Evidence Layer for AI-Assisted and Data-Transformation Workflows

<!-- claim:SF-2026-ARXIV-2607-09682:start -->AI systems are increasingly used to assist consequential decisions in regulated domains such as auditing, finance, and healthcare. This creates a recurring obligation: an organization must be able to reconstruct, after the fact, which evidence informed a given conclusion, and to show that the record of that reasoning was not altered. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-09682:end -->

**为什么进入候选分母。** 摘要首要问题为“AI systems are increasingly used to assist consequential decisions in regulated domains such as auditing, finance, and healthcare.”；它把 evidence identity、冲突、lineage 或 commit 变成显式状态，改变了 agent/workflow 的停止与审计条件。

**机制与状态边界。** The design serializes every evidence-bearing inference step into an authenticated record whose identity, parentage and mutation history can be replayed after the decision.

**证据证明什么。** Exact v1 defines and exercises the evidence-record format, mutation detection and reconstruction path; it does not establish a production-scale correlation model for adaptively selected branches.

**证据没有证明什么。** And it does not, on its own, defend against an adversary who controls the storage medium and recomputes the entire chain after a modification—closing that gap requires anchoring the chain head to an external, append-only reference, which we discuss in Section 5 and leave to future work. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.09682v1#S3 — 3 System Design; https://arxiv.org/html/2607.09682v1#S3.SS2 — 3.2 Event model。Evaluation：https://arxiv.org/html/2607.09682v1#S4 — 4 Evaluation。Limitations / counterevidence：https://arxiv.org/html/2607.09682v1#S5 — 5 Discussion and Limitations; https://arxiv.org/html/2607.09682v1#S3.SS6 — 3.6 Threat model。

**Artifact boundary。** Exact v1 links https://pypi.org/project/auditweave/, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 显式 evidence state 提高可追溯性，但新增 lineage、冲突、commit 与恢复语义，状态本身也必须被验证。 论文自身的边界信号是：And it does not, on its own, defend against an adversary who controls the storage medium and recomputes the entire chain after a modification—closing that gap requires anchoring the chain head to an external, append-only reference, which we discuss in Section 5 and leave to future work.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`PLATFORM-TRACE`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-09682:end -->

<!-- review:SF-2026-ARXIV-2607-09686:start -->
### MawForge: Memory-Bounded Expert Materialization for Local Mixture-of-Experts Inference

<!-- claim:SF-2026-ARXIV-2607-09686:start -->Sparse Mixture-of-Experts (MoE) language models separate total parameter count from per-token active computation, but local inference systems often still require the full model, key-value cache, runtime buffers, and operatingsystem headroom to fit in fast memory. MawForge tests a different systems hypothesis: local MoE serving can be made practical on constrained unified-memory machines by storing the full model on disk, keeping common tensors resident, and materializing routed expert tensors into a bounded execution cache on demand. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-09686:end -->

**为什么进入候选分母。** 摘要首要问题为“Sparse Mixture-of-Experts (MoE) language models separate total parameter count from per-token active computation, but local inference systems often still require the full model, key-value cache, runtime buffers, and operatingsystem headroom to fit in fast memory.”；它改变了推理期的状态放置、数据移动、执行控制或 SLO admission，属于长期 runtime 机制。

**机制与状态边界。** Sparse Mixture-of-Experts (MoE) language models separate total parameter count from per-token active computation, but local inference systems often still require the full model, key-value cache, runtime buffers, and operatingsystem headroom to fit in fast memory.

**证据证明什么。** Performance depends on balancing expert reuse against resident footprint, KV-cache size, quantization, route locality, and macOS memory pressure.

**证据没有证明什么。** Its strongest current result is not a single throughput number but a validated operating-envelope method: plan the budget, execute only feasible cells, collect route-aware telemetry, and choose cache settings by measured latency and materialization under host memory pressure. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.09686v1#S4 — IV MawForge Design; https://arxiv.org/html/2607.09686v1#S4.SS1 — IV-A System Thesis。Evaluation：https://arxiv.org/html/2607.09686v1#S5 — V Experimental Method; https://arxiv.org/html/2607.09686v1#S6 — VI Results。Limitations / counterevidence：https://arxiv.org/html/2607.09686v1#S11 — XI Conclusion; https://arxiv.org/html/2607.09686v1#S7 — VII Discussion。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更激进的缓存、迁移、并行或专用执行会换取吞吐/时延，同时增加配置依赖、资源压力与回退路径。 论文自身的边界信号是：Its strongest current result is not a single throughput number but a validated operating-envelope method: plan the budget, execute only feasible cells, collect route-aware telemetry, and choose cache settings by measured latency and materialization under host memory pressure.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`INFER-SCHEDULING`；evidence-stage relation：`alternative_branch`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-09686:end -->

<!-- review:SF-2026-ARXIV-2607-09689:start -->
### Evidence-Aware MapReduce for Forkable Compute

<!-- claim:SF-2026-ARXIV-2607-09689:start -->Snapshot-backed sandboxes make branching cheap while leaving evidence dependence unchanged. Branches can reuse a model, prompt, repository, tests, observations, or execution ancestor, so counting outputs can amplify one repeated error into high-confidence consensus. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-09689:end -->

**为什么进入候选分母。** 摘要首要问题为“Snapshot-backed sandboxes make branching cheap while leaving evidence dependence unchanged.”；它把 evidence identity、冲突、lineage 或 commit 变成显式状态，改变了 agent/workflow 的停止与审计条件。

**机制与状态边界。** The prototype assigns stable evidence identities, records fork lineage and tests whether a later aggregate can detect duplicated evidence instead of treating correlated branches as independent support.

**证据证明什么。** Unit, synthetic and end-to-end tests support serialization, lineage reconstruction and duplicate-evidence detection; the paper explicitly leaves scalable dependence estimation for correlated adaptive branches open.

**证据没有证明什么。** The kernel is one identity: to leading order under LAN, the confidence density a worker emits is a Gibbs measure with , so reduce is a partition function, consistency is the zero-temperature limit, and a confident liar—a falsely cold report—is the failure mode that mandates a clip. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.09689v1#S4 — 4 Orchestration and Security (Design Sketch); https://arxiv.org/html/2607.09689v1#S2 — 2 Programming Model and Forkable-Sandbox Substrate。Evaluation：https://arxiv.org/html/2607.09689v1#S5 — 5 Evaluation。Limitations / counterevidence：https://arxiv.org/html/2607.09689v1#S6 — 6 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/zozo123/boltzmann-mapreduce, https://github.com/opencontainers/image-spec, https://github.com/arXiv/html_feedback/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 显式 evidence state 提高可追溯性，但新增 lineage、冲突、commit 与恢复语义，状态本身也必须被验证。 论文自身的边界信号是：The kernel is one identity: to leading order under LAN, the confidence density a worker emits is a Gibbs measure with , so reduce is a partition function, consistency is the zero-temperature limit, and a confident liar—a falsely cold report—is the failure mode that mandates a clip.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`AGENT-WORKFLOW`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-09689:end -->

<!-- review:SF-2026-ARXIV-2607-09691:start -->
### What Context Does a Coding Agent Actually Need to Act?

<!-- claim:SF-2026-ARXIV-2607-09691:start -->A modern coding agent can hold an entire repository in its context window. Most of its reading is wasted -- and the interesting question is not how much context an agent can use, but what it actually \emph{needs}. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-09691:end -->

**为什么进入候选分母。** 摘要首要问题为“A modern coding agent can hold an entire repository in its context window.”；它把上下文、记忆、进度或能力选择提升为可持久且可验证的 agent 状态。

**机制与状态边界。** Most of its reading is wasted -- and the interesting question is not how much context an agent can use, but what it actually \emph{needs}.

**证据证明什么。** We release the instrument -- gold-validated environments, per-instance proof that every reference edit is expressible from every arm's context, deterministic patch construction, and pre-registered hypotheses whose nulls we publish.

**证据没有证明什么。** Compressed arms encode gold edit locations ; full does not. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.09691v1#S3 — 3 Method。Evaluation：https://arxiv.org/html/2607.09691v1#A4 — Appendix D Exploratory results (not claims of this paper); https://arxiv.org/html/2607.09691v1#S3.SS1 — 3.1 Experimental setup。Limitations / counterevidence：https://arxiv.org/html/2607.09691v1#S6 — 6 Threats to validity (and which way each cuts); https://arxiv.org/html/2607.09691v1#S7 — 7 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/integrallis/act-context, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 显式 agent state 改善恢复与控制，但增加状态陈旧、错误提交、跨轮污染和一致性责任。 论文自身的边界信号是：Compressed arms encode gold edit locations ; full does not.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`AGENT-CONTEXT`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-09691:end -->

<!-- review:SF-2026-ARXIV-2607-09692:start -->
### Reference-Based Distillation Detection in LLMs

<!-- claim:SF-2026-ARXIV-2607-09692:start -->Model distillation -- training on outputs from stronger third-party models -- is widely used to boost performance, but raises concerns about unfair advantages and policy violations. This motivates a fundamental question: can we detect whether a model was distilled from another? 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-09692:end -->

**为什么进入候选分母。** 摘要首要问题为“Model distillation -- training on outputs from stronger third-party models -- is widely used to boost performance, but raises concerns about unfair advantages and policy violations.”；它改变 artifact/evidence provenance 或攻击面的信任边界，可能影响发布与审计合同。

**机制与状态边界。** We introduce a distillation detection method based on reference-based membership inference.

**证据证明什么。** We show that, while identifying a teacher model from a student in isolation is highly challenging, it becomes tractable in a reference-based setting: given a model and an earlier-generation checkpoint from the same lineage, we can identify the teacher model used to train the later checkpoint.

**证据没有证明什么。** Exact v1 does not disclose a dedicated generalization or deployment guarantee beyond its stated evaluation scope. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.09692v1#A2.SS3 — B.3 Ablations for Reverse MIA methods; https://arxiv.org/html/2607.09692v1#S3 — 3 Method。Evaluation：https://arxiv.org/html/2607.09692v1#A2 — Appendix B Additional Experimental Results; https://arxiv.org/html/2607.09692v1#S4.SS2 — 4.2 Results from Controlled Experiments。Limitations / counterevidence：https://arxiv.org/html/2607.09692v1#S8 — 8 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/RajatRawat-creator/DistillDetect, https://huggingface.co/deepseek-ai/DeepSeek-R1-Distill-Qwen-7B#deepseek-r1-distill-models, https://huggingface.co/simplescaling/s1.1-32B; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更强 provenance 或攻击检测提高审计能力，但依赖密钥、参考版本、观测面或 threat model，不能替代内容正确性。 论文自身的边界信号是：Exact v1 does not disclose a dedicated generalization or deployment guarantee beyond its stated evaluation scope.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`PLATFORM-SECURITY`；evidence-stage relation：`alternative_branch`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-09692:end -->

<!-- review:SF-2026-ARXIV-2607-09697:start -->
### Safe responses matter: Output-aware safety guardrail mitigate over-refusal in MLLMs

<!-- claim:SF-2026-ARXIV-2607-09697:start -->Existing safety mechanisms for multimodal large language models (MLLMs) face a fundamental trade-off between safety and utility. Model fine-tuning achieves robust safety but compromises general utility. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-09697:end -->

**为什么进入候选分母。** 摘要首要问题为“Existing safety mechanisms for multimodal large language models (MLLMs) face a fundamental trade-off between safety and utility.”；它揭示局部安全检查或现有 guard 的边界，并提出可验证的新控制点。

**机制与状态边界。** Motivated by this insight, we propose a paradigm shift toward output-aware safety guardrails.

**证据证明什么。** Model fine-tuning achieves robust safety but compromises general utility.

**证据没有证明什么。** We identify that the root cause of over-refusal is that current safety guardrails are input-aware and do not consider actual outputs. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.09697v1#S3 — 3 OutGuard Method; https://arxiv.org/html/2607.09697v1#Pt0.A1.SS2 — 0.A.2 OutGuard Training and Inference Algorithms。Evaluation：https://arxiv.org/html/2607.09697v1#S4 — 4 Evaluation; https://arxiv.org/html/2607.09697v1#S4.SS1 — 4.1 Experiment Setup。Limitations / counterevidence：https://arxiv.org/html/2607.09697v1#S5 — 5 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/kunzhan/OutGuard, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 新的安全控制点降低特定失败，但会引入误拒绝、旁路、观测不足或模型/任务迁移问题。 论文自身的边界信号是：We identify that the root cause of over-refusal is that current safety guardrails are input-aware and do not consider actual outputs.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`PLATFORM-SECURITY`；evidence-stage relation：`alternative_branch`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-09697:end -->

<!-- review:SF-2026-ARXIV-2607-09709:start -->
### The Verifier is the Curriculum: Execution-Gated Self-Distillation for Cross-Family Game Generation

<!-- claim:SF-2026-ARXIV-2607-09709:start -->Post-training a code generator against a learned judge can optimize proxy features that raise the score without improving the artifact. We study the opposite signal: a deterministic, judge-free, ungameable filter -- whether a generated project launches cleanly under a headless engine (strict-launch). 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-09709:end -->

**为什么进入候选分母。** 摘要首要问题为“Post-training a code generator against a learned judge can optimize proxy features that raise the score without improving the artifact.”；它改变了 evaluation observable、对照组、判定粒度或结果解释边界，可能修正现有评测结论。

**机制与状态边界。** We study the opposite signal: a deterministic, judge-free, ungameable filter -- whether a generated project launches cleanly under a headless engine (strict-launch).

**证据证明什么。** With all other loop components held fixed, replacing the strict launch verifier with a permissive build check erased the accumulated gain, isolating verifier precision rather than data volume alone.

**证据没有证明什么。** 10 Limitations and future work We validate on four unseen families within one benchmark ( ), with leave-one-family-out robustness and a gold ceiling; broader families and larger models are the next test. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.09709v1#S5 — 5 Method: launch-gated iterative self-distillation。Evaluation：https://arxiv.org/html/2607.09709v1#A3.SS0.SSS0.Px4 — Evaluation and statistics.; https://arxiv.org/html/2607.09709v1#S5.SS0.SSS0.Px4 — Evaluation protocol.。Limitations / counterevidence：https://arxiv.org/html/2607.09709v1#S10 — 10 Limitations and future work; https://arxiv.org/html/2607.09709v1#S11 — 11 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：10 Limitations and future work We validate on four unseen families within one benchmark ( ), with leave-one-family-out robustness and a gold ceiling; broader families and larger models are the next test.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`PLATFORM-EVALUATION-SYSTEM`；evidence-stage relation：`principle_reuse`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-09709:end -->

<!-- review:SF-2026-ARXIV-2607-09711:start -->
### EvoClawBench: Can Agents Learn Reusable Skills from Their Own Runs?

<!-- claim:SF-2026-ARXIV-2607-09711:start -->Existing agent benchmarks primarily test task completion, tool use, or skill utility, but do not isolate whether a runtime can convert evidence from its own runs into reusable skills that improve fresh executions after authoring overhead. We introduce EvoClawBench, a benchmark for this closed-loop skill-learning question on repeated, fixture-backed tasks. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-09711:end -->

**为什么进入候选分母。** 摘要首要问题为“Existing agent benchmarks primarily test task completion, tool use, or skill utility, but do not isolate whether a runtime can convert evidence from its own runs into reusable skills that improve fresh executions after authoring overhead.”；它改变了 evaluation observable、对照组、判定粒度或结果解释边界，可能修正现有评测结论。

**机制与状态边界。** We introduce EvoClawBench, a benchmark for this closed-loop skill-learning question on repeated, fixture-backed tasks.

**证据证明什么。** OpenClaw shows similarly non-monotonic behavior, with some skill runs near baseline and others collapsing.

**证据没有证明什么。** Future skill systems should use selective creation policies and validation before reuse, while benchmark reports should include provenance, mutation checks, and end-to-end resources. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.09711v1#A8 — Appendix H Generated Family Design Matrix。Evaluation：https://arxiv.org/html/2607.09711v1#A13 — Appendix M Result JSON Schema; https://arxiv.org/html/2607.09711v1#A14 — Appendix N Result Validity Checklist。Limitations / counterevidence：https://arxiv.org/html/2607.09711v1#S6 — 6 Conclusion; https://arxiv.org/html/2607.09711v1#Sx1 — Limitations。

**Artifact boundary。** Exact v1 links https://github.com/pzy2000/EvoClawBench/tree/anonymous, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：Future skill systems should use selective creation policies and validation before reuse, while benchmark reports should include provenance, mutation checks, and end-to-end resources.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`AGENT-PLATFORM`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-09711:end -->

<!-- review:SF-2026-ARXIV-2607-09744:start -->
### A Theory of Least Autonomy in AI

<!-- claim:SF-2026-ARXIV-2607-09744:start -->Least privilege, the principle that an identity should hold only the permissions strictly required for its task, has been a foundational primitive of access control for decades. We argue that this principle is insufficient for agentic AI systems, which do not merely hold permissions but can combine, approve, and amplify them across workflows and system boundaries. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-09744:end -->

**为什么进入候选分母。** 摘要首要问题为“Least privilege, the principle that an identity should hold only the permissions strictly required for its task, has been a foundational primitive of access control for decades.”；它揭示局部安全检查或现有 guard 的边界，并提出可验证的新控制点。

**机制与状态边界。** We propose least autonomy as an appropriate generalization and develop a formal theory.

**证据证明什么。** Finally, we define a collusion predicate over graph reachability that detects authorization composition, decision manipulation, and cross-domain capability composition.

**证据没有证明什么。** Future work should evaluate the calibration of and , the precision of the screening results, and the integration of workflow and runtime evidence. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.09744v1#S6 — 6 Least Autonomy as a Design Criterion; https://arxiv.org/html/2607.09744v1#S6.SS4 — 6.4 Step-by-Step Design Procedure。Evaluation：https://arxiv.org/html/2607.09744v1#A2 — Appendix B Pseudocode for influence graph and least-autonomy evaluation; https://arxiv.org/html/2607.09744v1#S2.SS2 — 2.2 Workflow Authorization and Policy Analysis。Limitations / counterevidence：https://arxiv.org/html/2607.09744v1#S8 — 8 Limitations and Future Work; https://arxiv.org/html/2607.09744v1#S9 — 9 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 新的安全控制点降低特定失败，但会引入误拒绝、旁路、观测不足或模型/任务迁移问题。 论文自身的边界信号是：Future work should evaluate the calibration of and , the precision of the screening results, and the integration of workflow and runtime evidence.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`PLATFORM-SECURITY`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-09744:end -->

<!-- review:SF-2026-ARXIV-2607-09748:start -->
### Replicating Belief, Not Bits: Epistemic State Replication for Agentic Systems

<!-- claim:SF-2026-ARXIV-2607-09748:start -->In distributed systems, the classical State Machine Replication (SMR) model assumes that correct replicas execute deterministic transitions to yield identical bitwise states. However, the rise of agentic distributed systems -- where autonomous, stochastic, and model-driven agents orchestrate infrastructure -- presents scenarios where deterministic, bitwise replication is insufficient. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-09748:end -->

**为什么进入候选分母。** 摘要首要问题为“In distributed systems, the classical State Machine Replication (SMR) model assumes that correct replicas execute deterministic transitions to yield identical bitwise states.”；它把 evidence identity、冲突、lineage 或 commit 变成显式状态，改变了 agent/workflow 的停止与审计条件。

**机制与状态边界。** We propose Epistemic State Replication (ESR), a belief-replication layer for agentic distributed systems that shifts the replication boundary from data visibility to knowledge visibility.

**证据证明什么。** We prototype ESR and report preliminary simulation results that show feasibility under the stated assumptions and illustrate reductions in secondary cognitive faults.

**证据没有证明什么。** 6.4 Future Evaluation Plan A full evaluation should include 20–30 repeated runs with fixed random seeds; archived prompt templates; model/API version, temperature, top- , seed, retry, and serving-revision settings; token-size histograms for raw traces and epistemic deltas; size distributions; semantic-cache hit-rate distributions; p50/p95/p99 latency; confidence intervals; variance across independent seeds; and rendered plots from real measurements rather than illustrative figures. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.09748v1#S6.SS1 — 6.1 System Architecture; https://arxiv.org/html/2607.09748v1#S2.SS4 — 2.4 System and Failure Model。Evaluation：https://arxiv.org/html/2607.09748v1#S6.SS3 — 6.3 Simulation Metrics and Results; https://arxiv.org/html/2607.09748v1#S6.SS4 — 6.4 Future Evaluation Plan。Limitations / counterevidence：https://arxiv.org/html/2607.09748v1#S2.SS4 — 2.4 System and Failure Model; https://arxiv.org/html/2607.09748v1#S6.SS4 — 6.4 Future Evaluation Plan。

**Artifact boundary。** Exact v1 links https://github.com/langchain-ai/langchain, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 显式 evidence state 提高可追溯性，但新增 lineage、冲突、commit 与恢复语义，状态本身也必须被验证。 论文自身的边界信号是：6.4 Future Evaluation Plan A full evaluation should include 20–30 repeated runs with fixed random seeds; archived prompt templates; model/API version, temperature, top- , seed, retry, and serving-revision settings; token-size histograms for raw traces and epistemic deltas; size distributions; semantic-cache hit-rate distributions; p50/p95/p99 latency; confidence intervals; variance across independent seeds; and rendered plots from real measurements rather than illustrative figures.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`AGENT-PLATFORM`；evidence-stage relation：`structural_candidate`。
- Books 候选路由（尚非最终决定）：`Structural Candidate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-09748:end -->

<!-- review:SF-2026-ARXIV-2607-09759:start -->
### ReflectWorld-MM: An Entity-Oriented Multimodal Memory System for Open-Ended Video Streams

<!-- claim:SF-2026-ARXIV-2607-09759:start -->Building assistants that can continually watch the world, remember what they see, and reason over their accumulated experience is a long-standing goal, and recently multimodal agents equipped with long-term memory over video streams have attracted increasing interest. Unfortunately, existing systems either keep their memory inside the model context or in a flat feature store, and organize it around frames rather than around the persistent entities a stream is really about, which confines them to bounded videos and weakens their ability to track who and what reappears over time. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-09759:end -->

**为什么进入候选分母。** 摘要首要问题为“Building assistants that can continually watch the world, remember what they see, and reason over their accumulated experience is a long-standing goal, and recently multimodal agents equipped with long-term memory over video streams have attracted increasing interest.”；它把上下文、记忆、进度或能力选择提升为可持久且可验证的 agent 状态。

**机制与状态边界。** In this paper, we propose ReflectWorld-MM, an entity-oriented multimodal memory system for open-ended video streams.

**证据证明什么。** Across six long-video and lifelong-memory benchmarks, ReflectWorld-MM achieves the best accuracy on all six, outperforming strong memory agents and a frontier model.

**证据没有证明什么。** Exact v1 does not disclose a dedicated generalization or deployment guarantee beyond its stated evaluation scope. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.09759v1#S3.SS6 — 3.6 Retrieval and System Realization; https://arxiv.org/html/2607.09759v1#A3 — Appendix C Additional Implementation Details。Evaluation：https://arxiv.org/html/2607.09759v1#A2 — Appendix B Detailed Benchmark Breakdowns; https://arxiv.org/html/2607.09759v1#A7 — Appendix G Qualitative Benchmark Traces。Limitations / counterevidence：https://arxiv.org/html/2607.09759v1#S5 — 5 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 显式 agent state 改善恢复与控制，但增加状态陈旧、错误提交、跨轮污染和一致性责任。 论文自身的边界信号是：Exact v1 does not disclose a dedicated generalization or deployment guarantee beyond its stated evaluation scope.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`AGENT-MEMORY`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-09759:end -->

<!-- review:SF-2026-ARXIV-2607-09770:start -->
### Verification of Adaptive Agentic Controllers through Finite Rule Revision

<!-- claim:SF-2026-ARXIV-2607-09770:start -->Industrial agentic AI systems increasingly exhibit a gap between prototype capability and production deployment. In particular, adaptive agents may generate plausible outputs while remaining difficult to verify under non-determinism, confidentiality constraints, limited context, and weak observability. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-09770:end -->

**为什么进入候选分母。** 摘要首要问题为“Industrial agentic AI systems increasingly exhibit a gap between prototype capability and production deployment.”；它揭示局部安全检查或现有 guard 的边界，并提出可验证的新控制点。

**机制与状态边界。** The proposed framework treats the controller as a finite revisable object.

**证据证明什么。** Experiments in a stylized financially constrained inventory-control benchmark show three outcomes: resource-induced failures that remain non-repairable by one rule edit, partial repairs that are rejected because they violate thresholds or guardrails, and a local one-step repair of an order-volatility failure induced by removing a smoothing rule.

**证据没有证明什么。** The expectation is not that all inventory-control failures are repairable. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.09770v1#S2.SS2 — 2.2 Rule-Based Systems and Defeasible Reasoning; https://arxiv.org/html/2607.09770v1#S3 — 3 Methodological Positioning and Scope。Evaluation：https://arxiv.org/html/2607.09770v1#S15 — 15 Experimental Results: Detectability, Repairability, and Rejection Cases; https://arxiv.org/html/2607.09770v1#S11 — 11 Illustrative Inventory-Control Benchmark。Limitations / counterevidence：https://arxiv.org/html/2607.09770v1#S13 — 13 Failure Classes and Repair Expectations; https://arxiv.org/html/2607.09770v1#S14 — 14 Negative Results and Failure Conditions。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 新的安全控制点降低特定失败，但会引入误拒绝、旁路、观测不足或模型/任务迁移问题。 论文自身的边界信号是：The expectation is not that all inventory-control failures are repairable.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`AGENT-PLATFORM`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-09770:end -->

<!-- review:SF-2026-ARXIV-2607-09773:start -->
### EvoCUA-1.5: Online Reinforcement Learning for Multi-turn Computer-Use Agents

<!-- claim:SF-2026-ARXIV-2607-09773:start -->Computer-use agents must solve long-horizon tasks through repeated interaction with partially observable, multimodal desktop environments. Although imitation learning and offline trajectory refinement provide strong priors, static traces cannot cover the causal feedback loop of real computer use: each action changes the screen state, future action space, and recovery options. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-09773:end -->

**为什么进入候选分母。** 摘要首要问题为“Computer-use agents must solve long-horizon tasks through repeated interaction with partially observable, multimodal desktop environments.”；它改变训练信号、credit、capacity 或 update ownership，而不是只报告单任务精度增量。

**机制与状态边界。** Overall, EvoCUA-1.5 provides a practical framework for scaling online RL in multi-turn computer-use agents.

**证据证明什么。** Experiments show that these components improve training stability and downstream performance.

**证据没有证明什么。** 7 Discussion and Future Directions EvoCUA-1.5 shows that online RL for computer-use agents is a system–algorithm co-design problem. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.09773v1#S5.SS1 — 5.1 Architecture Overview; https://arxiv.org/html/2607.09773v1#A4 — Appendix D Implementation Details。Evaluation：https://arxiv.org/html/2607.09773v1#S6 — 6 Evaluation; https://arxiv.org/html/2607.09773v1#S6.SS1 — 6.1 Experimental Setup。Limitations / counterevidence：https://arxiv.org/html/2607.09773v1#S7 — 7 Discussion and Future Directions; https://arxiv.org/html/2607.09773v1#A5 — Appendix E Scope and Limitations。

**Artifact boundary。** Exact v1 links https://github.com/ByteDance-Seed/Seed-1.8/, https://github.com/OpenGVLab/ScaleCUA, https://github.com/arXiv/html_feedback/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更密集或更定向的训练信号改善样本效率，但会增加 verifier 偏差、分布迁移和优化耦合。 论文自身的边界信号是：7 Discussion and Future Directions EvoCUA-1.5 shows that online RL for computer-use agents is a system–algorithm co-design problem.

- Score V2：Design Delta 3 / System Reach 2 / Durability 3 = **8/9**。
- Stable owner 候选：`TRAIN-GRPO`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-09773:end -->

<!-- review:SF-2026-ARXIV-2607-09776:start -->
### HELP: Human-Efficient Large-Scale Robot Post-Training with Rollout Segmentation

<!-- claim:SF-2026-ARXIV-2607-09776:start -->When adapting Vision Language Action (VLA) models to downstream tasks, multiple rounds of post-training are often required to progressively address policy weaknesses. In this report, we focus on maximizing human efficiency during this iterative process, measured by policy improvement and task throughput per unit of human labor and time. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-09776:end -->

**为什么进入候选分母。** 摘要首要问题为“When adapting Vision Language Action (VLA) models to downstream tasks, multiple rounds of post-training are often required to progressively address policy weaknesses.”；它改变训练信号、credit、capacity 或 update ownership，而不是只报告单任务精度增量。

**机制与状态边界。** We propose HELP, a Human-Efficient Large-scale robot Post-training pipeline in which two specialized operators supervise twelve robots concurrently.

**证据证明什么。** Across four real-world manipulation tasks, HELP achieves 80\%--95\% success rates and improves task throughput by 1.7$\times$--4.2$\times$ over the base model.

**证据没有证明什么。** However, because human operators cannot foresee all potential edge cases during the initial data collection, the models fine tuned on this preliminary data inevitably exhibit flaws. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.09776v1#S3.SS1 — 3.1 System Architecture; https://arxiv.org/html/2607.09776v1#S3 — 3 Framework。Evaluation：https://arxiv.org/html/2607.09776v1#S4.SS4 — 4.4 The Video Progress Benchmark; https://arxiv.org/html/2607.09776v1#S5 — 5 Experiments。Limitations / counterevidence：https://arxiv.org/html/2607.09776v1#S1 — 1 Introduction; https://arxiv.org/html/2607.09776v1#S2 — 2 Related work。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更密集或更定向的训练信号改善样本效率，但会增加 verifier 偏差、分布迁移和优化耦合。 论文自身的边界信号是：However, because human operators cannot foresee all potential edge cases during the initial data collection, the models fine tuned on this preliminary data inevitably exhibit flaws.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`MULTIMODAL-EMBODIED-VLA`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-09776:end -->

<!-- review:SF-2026-ARXIV-2607-09786:start -->
### Length Penalties Make Chain-of-Thought Less Monitorable

<!-- claim:SF-2026-ARXIV-2607-09786:start -->To curb overthinking and reduce inference costs, researchers now train reasoning models with penalties on chain of thought length. We find that these penalties degrade monitorability. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-09786:end -->

**为什么进入候选分母。** 摘要首要问题为“To curb overthinking and reduce inference costs, researchers now train reasoning models with penalties on chain of thought length.”；它改变了 evaluation observable、对照组、判定粒度或结果解释边界，可能修正现有评测结论。

**机制与状态边界。** The study applies controlled length-penalty training and compares matched-capability models with monitors that inspect outputs or internal activations, separating shorter reasoning from observability loss.

**证据证明什么。** Across the disclosed tasks and models, stronger pressure toward shorter answers reduced monitorability even when answer quality was matched; this is a warning about training-objective side effects, not a universal law for all length controls.

**证据没有证明什么。** Safety arguments that rely on chain-of-thought monitoring should therefore treat token efficiency as an intervention on the monitor’s evidence budget, not only on inference cost. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.09786v1#A1.SS4 — A.4 Reinforcement Learning Implementation Details。Evaluation：https://arxiv.org/html/2607.09786v1#A2 — Appendix B Evaluation Protocol; https://arxiv.org/html/2607.09786v1#A2.SS1 — B.1 Evaluation Datasets。Limitations / counterevidence：https://arxiv.org/html/2607.09786v1#S7 — 7 Limitations; https://arxiv.org/html/2607.09786v1#S8 — 8 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：Safety arguments that rely on chain-of-thought monitoring should therefore treat token efficiency as an intervention on the monitor’s evidence budget, not only on inference cost.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`PLATFORM-EVALUATION-SYSTEM`；evidence-stage relation：`principle_reuse`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-09786:end -->

<!-- review:SF-2026-ARXIV-2607-09791:start -->
### Gauge dependence and structured-output corruption in sign-branched repetition penalties: measurements across models, inference stacks, and alternative repetition controls

<!-- claim:SF-2026-ARXIV-2607-09791:start -->The multiplicative repetition penalty shipped across the LLM inference ecosystem (HuggingFace, vLLM, llama$.$cpp, and a dozen further engines) branches on the sign of each raw logit (divide positives by theta, multiply negatives). But the softmax is unchanged by adding a constant to every logit, so a model's logit zero-point is arbitrary (a gauge choice), and the sign-branch reads it. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-09791:end -->

**为什么进入候选分母。** 摘要首要问题为“The multiplicative repetition penalty shipped across the LLM inference ecosystem (HuggingFace, vLLM, llama$.$cpp, and a dozen further engines) branches on the sign of each raw logit (divide positives by theta, multiply negatives).”；它改变了推理期的状态放置、数据移动、执行控制或 SLO admission，属于长期 runtime 机制。

**机制与状态边界。** The multiplicative repetition penalty shipped across the LLM inference ecosystem (HuggingFace, vLLM, llama$.$cpp, and a dozen further engines) branches on the sign of each raw logit (divide positives by theta, multiply negatives).

**证据证明什么。** This note gives the mechanism, the measurements (five models up to 7B; two code models; both effects replicated inside vLLM and llama$.$cpp through their own samplers), the per-model calibration map, and the normalized variant.

**证据没有证明什么。** They belong to this operator, not to repetition control in general: the subtractive penalties avoid them by construction, though not every stack exposes one (HuggingFace’s generate ships only the multiplicative form), and the normalized variant of Section 5 removed them in every measurement we ran. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.09791v1#S4 — 4 The operator ships across the inference ecosystem。Evaluation：https://arxiv.org/html/2607.09791v1#S1 — 1 The penalty branches on an unconstrained coordinate; https://arxiv.org/html/2607.09791v1#S2 — 2 Consequence 1: the penalty is not well-defined (A1)。Limitations / counterevidence：https://arxiv.org/html/2607.09791v1#S7 — 7 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/ggml-org/llama.cpp/issues/25388, https://github.com/guidance-ai/jsonschemabench, https://github.com/ggml-org/llama.cpp/issues/2970; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更激进的缓存、迁移、并行或专用执行会换取吞吐/时延，同时增加配置依赖、资源压力与回退路径。 论文自身的边界信号是：They belong to this operator, not to repetition control in general: the subtractive penalties avoid them by construction, though not every stack exposes one (HuggingFace’s generate ships only the multiplicative form), and the normalized variant of Section 5 removed them in every measurement we ran.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`INFER-DECODE`；evidence-stage relation：`corrective_evidence`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-09791:end -->

<!-- review:SF-2026-ARXIV-2607-09794:start -->
### Agentic Context Learning with Self-Discovered Specification

<!-- claim:SF-2026-ARXIV-2607-09794:start -->Context learning is an emerging inference-time task where LLMs must learn and apply novel, task-specific knowledge from intricate contexts absent from pre-training; even frontier models score under 24% task success. In this work, we conduct a comprehensive empirical study to understand why this setting remains difficult. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-09794:end -->

**为什么进入候选分母。** 摘要首要问题为“Context learning is an emerging inference-time task where LLMs must learn and apply novel, task-specific knowledge from intricate contexts absent from pre-training; even frontier models score under 24% task success.”；它把上下文、记忆、进度或能力选择提升为可持久且可验证的 agent 状态。

**机制与状态边界。** In this work, we conduct a comprehensive empirical study to understand why this setting remains difficult.

**证据证明什么。** Overall, our results suggest context learning hinges on not only content acquisition but also specification acquisition.

**证据没有证明什么。** Exact v1 does not disclose a dedicated generalization or deployment guarantee beyond its stated evaluation scope. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.09794v1#A1.SS1 — A.1 CL-Bench Design and Contamination Prevention; https://arxiv.org/html/2607.09794v1#A2 — Appendix B Supplementary Material for Method。Evaluation：https://arxiv.org/html/2607.09794v1#A4.SS1 — D.1 Visualization of ablation study results.; https://arxiv.org/html/2607.09794v1#A2.SS4 — B.4 Evaluation Protocol Details。Limitations / counterevidence：https://arxiv.org/html/2607.09794v1#A2.SS2 — B.2 Design Decisions: Extended Discussion; https://arxiv.org/html/2607.09794v1#A7 — Appendix G Additional material for discussion。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 显式 agent state 改善恢复与控制，但增加状态陈旧、错误提交、跨轮污染和一致性责任。 论文自身的边界信号是：Exact v1 does not disclose a dedicated generalization or deployment guarantee beyond its stated evaluation scope.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`AGENT-CONTEXT`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-09794:end -->

<!-- review:SF-2026-ARXIV-2607-09800:start -->
### Auditing Invisible Weight Updates with Reference Traces

<!-- claim:SF-2026-ARXIV-2607-09800:start -->Direct low-precision write-back can erase nonzero optimizer proposals. We ask what a high-precision reference trace establishes before a low-precision run. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-09800:end -->

**为什么进入候选分母。** 摘要首要问题为“Direct low-precision write-back can erase nonzero optimizer proposals.”；它揭示训练数值路径会静默改变有效更新，直接影响 correctness contract。

**机制与状态边界。** A high-precision reference run fixes the expected update trace, then low-precision decoder runs isolate where deterministic nearest write-back erases small recurrent updates; stochastic write-back is tested as the repair.

**证据证明什么。** Matched decoder experiments attribute much of the low-precision gap to repeated write-back loss and show stochastic write-back recovering most of that gap under the reported formats and models.

**证据没有证明什么。** This is one mechanism—the half-ULP weight freeze—shown to transfer across the architectures we tested, not two independent phenomena that happen to agree, and not yet a survey of all models. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.09800v1#Sx2.SSx3 — Transfer across precision, rate, and architecture; https://arxiv.org/html/2607.09800v1#Sx2.SSx4 — Transfer across optimizer, loss, and architecture。Evaluation：https://arxiv.org/html/2607.09800v1#Sx2 — Results; https://arxiv.org/html/2607.09800v1#Sx4.SSx1 — Experimental systems。Limitations / counterevidence：https://arxiv.org/html/2607.09800v1#Sx3 — Discussion。

**Artifact boundary。** Exact v1 links https://github.com/imoneoi/bf16_fused_adam, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 保护数值更新会增加精度、诊断或计算成本，却换来可解释的 correctness floor。 论文自身的边界信号是：This is one mechanism—the half-ULP weight freeze—shown to transfer across the architectures we tested, not two independent phenomena that happen to agree, and not yet a survey of all models.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`TRAIN-PRETRAINING`；evidence-stage relation：`corrective_evidence`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-09800:end -->

<!-- review:SF-2026-ARXIV-2607-09802:start -->
### Quota Marketplace: Dynamic Pricing for Efficient Allocation of ML Training Resources

<!-- claim:SF-2026-ARXIV-2607-09802:start -->The escalating demand for Machine Learning (ML) training resources in recent years has resulted in a substantial gap between the high demand and the available supply. Efficient allocation of these scarce and expensive resources is crucial for organizations to maximize their return on investment. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-09802:end -->

**为什么进入候选分母。** 摘要首要问题为“The escalating demand for Machine Learning (ML) training resources in recent years has resulted in a substantial gap between the high demand and the available supply.”；它改变资源分配、迁移、定价或路由的控制权与约束。

**机制与状态边界。** The system couples an internal market price with allocation decisions so teams express marginal accelerator value while the controller continuously reconciles demand with a constrained shared fleet.

**证据证明什么。** The Google deployment report shows the mechanism operating with measured allocation effects inside the disclosed organization; it does not establish portability to other incentive structures or fleet topologies.

**证据没有证明什么。** Chip-Hour mechanisms cannot guarantee -fairness for , even for uniform-value instances. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.09802v1#S2 — 2 Quota Marketplace System; https://arxiv.org/html/2607.09802v1#S2.SS1 — 2.1 Market Implementation。Evaluation：https://arxiv.org/html/2607.09802v1#S4 — 4 Theoretical Analysis。Limitations / counterevidence：https://arxiv.org/html/2607.09802v1#S5 — 5 Discussions and Future Directions; https://arxiv.org/html/2607.09802v1#S4.SS1 — 4.1 Limitations of Chip-Hour Mechanisms。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 动态资源控制提高利用率，但增加测量误差、迁移开销、租户公平和控制稳定性问题。 论文自身的边界信号是：Chip-Hour mechanisms cannot guarantee -fairness for , even for uniform-value instances.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`PLATFORM-GPU-SCHEDULER`；evidence-stage relation：`alternative_branch`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-09802:end -->

<!-- review:SF-2026-ARXIV-2607-09803:start -->
### Spectral Origins of the Self-Correction Blind Spot in Autoregressive Generation

<!-- claim:SF-2026-ARXIV-2607-09803:start -->Large autoregressive language models exhibit a self-correction blind spot: they reliably fix identical errors when attributed to an external source yet fail to fix the same errors in their own outputs. Prior work has documented this phenomenon empirically, through controlled error injection, error-depth decompositions, RL-based verifier-corrector training, and intrinsic self-verification, but offers no formal model of why generating a token suppresses the ability to detect its error, no quantitative activation condition for correction markers, and no convergence guarantee for reinforcement-learning-based self-correction. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-09803:end -->

**为什么进入候选分母。** 摘要首要问题为“Large autoregressive language models exhibit a self-correction blind spot: they reliably fix identical errors when attributed to an external source yet fail to fix the same errors in their own outputs.”；它提出可跨 workload 讨论的状态、表示或计算机制，并给出旧方案的适用边界。

**机制与状态边界。** Prior work has documented this phenomenon empirically, through controlled error injection, error-depth decompositions, RL-based verifier-corrector training, and intrinsic self-verification, but offers no formal model of why generating a token suppresses the ability to detect its error, no quantitative activation condition for correction markers, and no convergence guarantee for reinforcement-learning-based self-correction.

**证据证明什么。** Experiments across four backbones and a visual autoregressive probe validate every theorem, with spectral predictions matching measured blind-spot rates within 3.2\% RMSE.

**证据没有证明什么。** Exact v1 does not disclose a dedicated generalization or deployment guarantee beyond its stated evaluation scope. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.09803v1#S1 — 1 Introduction; https://arxiv.org/html/2607.09803v1#S2 — 2 Related Work。Evaluation：https://arxiv.org/html/2607.09803v1#S4.SS5 — 4.5 Analysis Experiments; https://arxiv.org/html/2607.09803v1#S4 — 4 Experiments。Limitations / counterevidence：https://arxiv.org/html/2607.09803v1#S3.SS8 — 3.8 Discussion; https://arxiv.org/html/2607.09803v1#S4.SS6 — 4.6 Discussion。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 新表示或状态机制扩大能力边界，但带来额外训练、状态管理、稳定性或泛化假设。 论文自身的边界信号是：Exact v1 does not disclose a dedicated generalization or deployment guarantee beyond its stated evaluation scope.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`AGENT-REFLECTION`；evidence-stage relation：`explanatory_analogy`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-09803:end -->

<!-- review:SF-2026-ARXIV-2607-09804:start -->
### Trivial Prompt Reframing Bypasses Safety Guardrails in Googleś MedGemma-4B

<!-- claim:SF-2026-ARXIV-2607-09804:start -->Open-weight medical language models are increasingly used as the base of patient-facing and clinician-support applications. Their model cards prohibit specific behaviors -- recommending exact drug dosages, issuing definitive diagnoses, prescribing treatments, adjudicating drug-drug interactions, and advising that emergency care can be skipped -- yet a model card describes intended behavior, not robust behavior. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-09804:end -->

**为什么进入候选分母。** 摘要首要问题为“Open-weight medical language models are increasingly used as the base of patient-facing and clinician-support applications.”；它揭示局部安全检查或现有 guard 的边界，并提出可验证的新控制点。

**机制与状态边界。** Their model cards prohibit specific behaviors -- recommending exact drug dosages, issuing definitive diagnoses, prescribing treatments, adjudicating drug-drug interactions, and advising that emergency care can be skipped -- yet a model card describes intended behavior, not robust behavior.

**证据证明什么。** Our findings motivate stronger deployment-time guardrails for open medical models.

**证据没有证明什么。** The adversary applies only surface-text transformations to an otherwise-benign clinical question. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.09804v1#S4 — IV Methods。Evaluation：https://arxiv.org/html/2607.09804v1#A1 — Appendix A Full concept manner results; https://arxiv.org/html/2607.09804v1#S4.SS6 — IV-F Metrics and statistical analysis。Limitations / counterevidence：https://arxiv.org/html/2607.09804v1#S3 — III Threat Model; https://arxiv.org/html/2607.09804v1#S5.SS5 — V-E Qualitative failure modes。

**Artifact boundary。** Exact v1 links https://huggingface.co/google/medgemma-4b-it, https://huggingface.co/MoritzLaurer/DeBERTa-v3-base-mnli-fever-anli, https://github.com/arXiv/html_feedback/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 新的安全控制点降低特定失败，但会引入误拒绝、旁路、观测不足或模型/任务迁移问题。 论文自身的边界信号是：The adversary applies only surface-text transformations to an otherwise-benign clinical question.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`PLATFORM-SECURITY`；evidence-stage relation：`release_security_override`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-09804:end -->

<!-- review:SF-2026-ARXIV-2607-09822:start -->
### Memory-Conditioned Tool Calling for Camera-First Visual Agents

<!-- claim:SF-2026-ARXIV-2607-09822:start -->Recognition tells an agent what is in an image; personal memory affects what is worth looking up next. In a camera-first setting the user can send only an image, so the agent must form the lookups. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-09822:end -->

**为什么进入候选分母。** 摘要首要问题为“Recognition tells an agent what is in an image; personal memory affects what is worth looking up next.”；它把上下文、记忆、进度或能力选择提升为可持久且可验证的 agent 状态。

**机制与状态边界。** The agent maintains a three-layer personal visual memory, retrieves it on every camera-first turn to form tool arguments, and performs conflict-aware write-back after the interaction.

**证据证明什么。** The reported multi-tool evaluation supports better personalized tool choice and argument formation from this memory loop; it does not prove that stored visual inferences remain correct under long-lived identity or preference drift.

**证据没有证明什么。** Partial layer ablations isolate profile vs. observations while keeping short-term focus; we do not report a short-term-focus-only ablation in the release tables. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.09822v1#S3 — 3 Method; https://arxiv.org/html/2607.09822v1#S5.SS2 — 5.2 Relation to Dialogue Memory Systems。Evaluation：https://arxiv.org/html/2607.09822v1#S4 — 4 Experiments; https://arxiv.org/html/2607.09822v1#S4.SS2 — 4.2 Memory Ablation。Limitations / counterevidence：https://arxiv.org/html/2607.09822v1#S5 — 5 Discussion; https://arxiv.org/html/2607.09822v1#S5.SS4 — 5.4 Limitations。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 显式 agent state 改善恢复与控制，但增加状态陈旧、错误提交、跨轮污染和一致性责任。 论文自身的边界信号是：Partial layer ablations isolate profile vs. observations while keeping short-term focus; we do not report a short-term-focus-only ablation in the release tables.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`AGENT-MEMORY`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-09822:end -->

<!-- review:SF-2026-ARXIV-2607-09889:start -->
### Remembering Distinct Items, Not Tokens: A Learnable Dirichlet-Process Cache Between State-Space Models and Attention

<!-- claim:SF-2026-ARXIV-2607-09889:start -->Fixed-state sequence models compress an unbounded past into a bounded state, which caps their associative recall at roughly the state dimension; attention escapes the cap by keeping a key-value entry for every token, at quadratic compute and a cache that grows with the sequence. We study the middle ground: a sparse cache that allocates a slot only when an input is novel, so its size tracks the number of distinct items rather than the number of tokens. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-09889:end -->

**为什么进入候选分母。** 摘要首要问题为“Fixed-state sequence models compress an unbounded past into a bounded state, which caps their associative recall at roughly the state dimension; attention escapes the cap by keeping a key-value entry for every token, at quadratic compute and a cache that grows with the sequence.”；它提出可跨 workload 讨论的状态、表示或计算机制，并给出旧方案的适用边界。

**机制与状态边界。** The evidence is a family of controlled mechanism studies at modest scale, with the distinct-items property confirmed on four real streams (recommendation, systems logs, clinical events, and insurance claims); a real-backbone, real-corpus language validation is pursued in a companion study.

**证据证明什么。** On a controlled associative-recall benchmark with redundancy we show that the cache matches full-attention recall while storing only the distinct items, that it dominates a fixed-budget eviction cache on the recall-versus-size frontier, and that on a state-space backbone it answers both a recall query and a long-range aggregate at the lowest memory of any model tested.

**证据没有证明什么。** 4 Scope, limitations, and future work We state the boundaries as part of the contribution rather than as a coda. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.09889v1#S2 — 2 Method; https://arxiv.org/html/2607.09889v1#S3.SS1 — 3.1 Approach I: the static Dirichlet-process cache。Evaluation：https://arxiv.org/html/2607.09889v1#S3 — 3 Experiments。Limitations / counterevidence：https://arxiv.org/html/2607.09889v1#S4 — 4 Scope, limitations, and future work。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 新表示或状态机制扩大能力边界，但带来额外训练、状态管理、稳定性或泛化假设。 论文自身的边界信号是：4 Scope, limitations, and future work We state the boundaries as part of the contribution rather than as a coda.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`MODEL-LONG-CONTEXT`；evidence-stage relation：`alternative_branch`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-09889:end -->

<!-- review:SF-2026-ARXIV-2607-09992:start -->
### Trusted Floors Under Untrusted Learners: A Runtime Assured-SLO Guard for ML Serving

<!-- claim:SF-2026-ARXIV-2607-09992:start -->Modern ML serving increasingly lets learned, unverified components (routers, latency-SLO admitters, admit ladders) decide a tenant's quality of service; when one is wrong, the assured SLO can silently break, and the Kubernetes layers beneath (Kueue, DRA, the Gateway-API Inference Extension, GAIE) add cross-layer surprises. Rather than trust the learner to be right, we bound the damage a wrong one can do: a small trusted guard wraps the untrusted learner (learned proposes, the guard disposes). 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-09992:end -->

**为什么进入候选分母。** 摘要首要问题为“Modern ML serving increasingly lets learned, unverified components (routers, latency-SLO admitters, admit ladders) decide a tenant's quality of service; when one is wrong, the assured SLO can silently break, and the Kubernetes layers beneath (Kueue, DRA, the Gateway-API Inference Extension, GAIE) add cross-layer surprises.”；它把 learned policy 与强制 SLO guard 分层，改变可保证与只能统计观测的责任边界。

**机制与状态边界。** Rather than trust the learner to be right, we bound the damage a wrong one can do: a small trusted guard wraps the untrusted learner (learned proposes, the guard disposes).

**证据证明什么。** Under the stated service-envelope assumptions, the trusted guard kept the assured-class miss rate at zero across tested learner miscalibrations while the unguarded learned admitter missed 0.86-0.94.

**证据没有证明什么。** 6 Conclusion An assured SLO is not one obligation but two: a controllable safety projection a trusted guard enforces around a wrong learned admitter, and a statistical residual a conservative screen can only approach . 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.09992v1#S2 — 2 The guard: learned proposes, verified disposes; https://arxiv.org/html/2607.09992v1#S3 — 3 When can a cheap static screen be trusted?。Evaluation：https://arxiv.org/html/2607.09992v1#S2.SS0.SSS0.Px4 — The operating envelope; https://arxiv.org/html/2607.09992v1#S2.SS0.SSS0.Px5 — Versus vLLM's own priority scheduler。Limitations / counterevidence：https://arxiv.org/html/2607.09992v1#S5.SS0.SSS0.Px1 — Scope: what we can and cannot evaluate; https://arxiv.org/html/2607.09992v1#S6 — 6 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/vllm-project/vllm/issues/40004, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 可信 guard 能限制 learned policy 的伤害，但只能保证它实际拥有执行控制的那部分义务。 论文自身的边界信号是：6 Conclusion An assured SLO is not one obligation but two: a controllable safety projection a trusted guard enforces around a wrong learned admitter, and a statistical residual a conservative screen can only approach .

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`INFER-SCHEDULING`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-09992:end -->

<!-- review:SF-2026-ARXIV-2607-09996:start -->
### Who&amp;When Pro: Can LLMs Really Attribute Failures in AI Agents?

<!-- claim:SF-2026-ARXIV-2607-09996:start -->Automated failure attribution uses LLMs to identify where and why agentic systems fail. As agents become more capable, their failures become subtler, making automated attribution increasingly important. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-09996:end -->

**为什么进入候选分母。** 摘要首要问题为“Automated failure attribution uses LLMs to identify where and why agentic systems fail.”；它改变了 evaluation observable、对照组、判定粒度或结果解释边界，可能修正现有评测结论。

**机制与状态边界。** The benchmark replays agent executions, injects controlled failures after an exact trace point and asks the evaluator to identify both the responsible component and the failure time across modalities and interaction protocols.

**证据证明什么。** The controlled corpus reveals systematic attribution differences across model families, modalities and protocols; it measures diagnosis under injected ground truth rather than proving production root-cause coverage.

**证据没有证明什么。** Exact v1 does not disclose a dedicated generalization or deployment guarantee beyond its stated evaluation scope. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.09996v1#A5.SS1 — E.1 Failure Attribution: Benchmarks and Methods; https://arxiv.org/html/2607.09996v1#A5.SS2 — E.2 Self-Evolving Agentic Systems。Evaluation：https://arxiv.org/html/2607.09996v1#A4 — Appendix D More Results and Analysis; https://arxiv.org/html/2607.09996v1#A4.SS1 — D.1 Full results on Ablation Set。Limitations / counterevidence：https://arxiv.org/html/2607.09996v1#A1 — Appendix A Limitations and Broader Impacts; https://arxiv.org/html/2607.09996v1#A1.SS1 — A.1 Limitations。

**Artifact boundary。** Exact v1 links https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro, https://github.com/meta-llama/llama-models/blob/main/models/llama4/MODEL_CARD.md, https://github.com/huggingface/smolagents; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：Exact v1 does not disclose a dedicated generalization or deployment guarantee beyond its stated evaluation scope.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`PLATFORM-EVALUATION-SYSTEM`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-09996:end -->

<!-- review:SF-2026-ARXIV-2607-09999:start -->
### Silent Failures in Quantized LLM Reasoning: A Taxonomy-Based Analysis of Hollow Convergence and Failure Mode Shifts

<!-- claim:SF-2026-ARXIV-2607-09999:start -->We show that post-training quantization can silently alter how large language models reason even when task accuracy is preserved. Using a six-category failure taxonomy validated by two independent human annotators (Cohen's $κ$ = 0.906), we classify 30,000 chain-of-thought outputs from five instruction-tuned LLMs (3B--14B parameters) across three quantization precisions (FP32, FP16, NF4) and four reasoning benchmarks. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-09999:end -->

**为什么进入候选分母。** 摘要首要问题为“We show that post-training quantization can silently alter how large language models reason even when task accuracy is preserved.”；它改变了 evaluation observable、对照组、判定粒度或结果解释边界，可能修正现有评测结论。

**机制与状态边界。** Using a six-category failure taxonomy validated by two independent human annotators (Cohen's $κ$ = 0.906), we classify 30,000 chain-of-thought outputs from five instruction-tuned LLMs (3B--14B parameters) across three quantization precisions (FP32, FP16, NF4) and four reasoning benchmarks.

**证据证明什么。** We find that while accuracy is robust across precisions (maximum 3.1 pp drop), Hollow Convergence (correct answers reached through incomplete or unverifiable reasoning) shows a significant size-dependent shift under NF4, dropping sharply for the two smallest models tested but remaining invariant for models at 12B parameters and above.

**证据没有证明什么。** 2) A large -scale annotation of 30,000 model outputs across five models, three precisions, and four benchmarks, revealing a significant size-dependent HC effect under NF4 quantization. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/pdf/2607.09999v1#page=2 — PDF page 2; https://arxiv.org/pdf/2607.09999v1#page=3 — PDF page 3。Evaluation：https://arxiv.org/pdf/2607.09999v1#page=4 — PDF page 4; https://arxiv.org/pdf/2607.09999v1#page=5 — PDF page 5。Limitations / counterevidence：https://arxiv.org/pdf/2607.09999v1#page=6 — PDF page 6; https://arxiv.org/pdf/2607.09999v1#page=7 — PDF page 7。

**Artifact boundary。** Not Disclosed — exact v1 exposes no uniquely versioned artifact locator used to enlarge the manuscript claim boundary.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：2) A large -scale annotation of 30,000 model outputs across five models, three precisions, and four benchmarks, revealing a significant size-dependent HC effect under NF4 quantization.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`PLATFORM-EVALUATION-SYSTEM`；evidence-stage relation：`corrective_evidence`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-09999:end -->

<!-- review:SF-2026-ARXIV-2607-10044:start -->
### FlashTrie: A GPU-Accelerated Constrained Beam Search for Generative Retrieval

<!-- claim:SF-2026-ARXIV-2607-10044:start -->Constrained decoding is essential in generative retrieval, where document identifiers generated directly from a query must exactly match a predefined library of valid IDs. At scale, decoding is often constrained using a trie with beam search but most implementations run on CPU. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-10044:end -->

**为什么进入候选分母。** 摘要首要问题为“Constrained decoding is essential in generative retrieval, where document identifiers generated directly from a query must exactly match a predefined library of valid IDs.”；它改变了推理期的状态放置、数据移动、执行控制或 SLO admission，属于长期 runtime 机制。

**机制与状态边界。** FlashTrie maps trie traversal and constrained beam expansion to fused GPU kernels, keeping constraint state on device instead of round-tripping candidate prefixes through a CPU controller.

**证据证明什么。** The disclosed retrieval workloads show up to 24x decoding speedup, roughly 3 ms latency and scaling to an 800M-node trie while preserving the paper's retrieval metric; those numbers remain tied to its hardware, beam and constraint configuration.

**证据没有证明什么。** Our central finding is that constrained decoding need not remain a CPU bottleneck. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.10044v1#A2 — Appendix B CPU Baselines: Full Design Details and System Contrast; https://arxiv.org/html/2607.10044v1#A2.SS3 — B.3 Axis-by-Axis System Contrast。Evaluation：https://arxiv.org/html/2607.10044v1#A10 — Appendix J Full Ablations: Binary-Search and Linear-Search Variants; https://arxiv.org/html/2607.10044v1#A11 — Appendix K NQ + GENRE Workload Construction and Realistic-Threshold Analysis。Limitations / counterevidence：https://arxiv.org/html/2607.10044v1#S5 — 5 Limitations; https://arxiv.org/html/2607.10044v1#Sx1 — Discussion。

**Artifact boundary。** Exact v1 links https://github.com/s-yata/marisa-trie, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更激进的缓存、迁移、并行或专用执行会换取吞吐/时延，同时增加配置依赖、资源压力与回退路径。 论文自身的边界信号是：Our central finding is that constrained decoding need not remain a CPU bottleneck.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`INFER-DECODE`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-10044:end -->

<!-- review:SF-2026-ARXIV-2607-10059:start -->
### AgentAbstain: Do LLM Agents Know When Not to Act?

<!-- claim:SF-2026-ARXIV-2607-10059:start -->Agent systems based on large language models (LLMs) are increasingly deployed for autonomous tasks, yet existing evaluations mostly focus on task success rather than whether agents know when to abstain. This gap poses real risks: under ambiguity, conflicting constraints, or tool failures, agents may execute unintended and irreversible actions. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-10059:end -->

**为什么进入候选分母。** 摘要首要问题为“Agent systems based on large language models (LLMs) are increasingly deployed for autonomous tasks, yet existing evaluations mostly focus on task success rather than whether agents know when to abstain.”；它揭示局部安全检查或现有 guard 的边界，并提出可验证的新控制点。

**机制与状态边界。** The framework pairs otherwise matched tasks where acting is appropriate or harmful, executes both through real agent harnesses and scores an agent only when it both acts and abstains correctly.

**证据证明什么。** Across 17 frontier models and four harnesses, the best reported paired accuracy was 59.5%, demonstrating that ordinary task success does not imply calibrated abstention under this benchmark contract.

**证据没有证明什么。** LLM outputs are stochastic, so multi-run evaluation would likely reveal variance that single-run numbers do not capture. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.10059v1#A2 — Appendix B Formal Framework; https://arxiv.org/html/2607.10059v1#A2.SS5 — B.5 Paired Task Design。Evaluation：https://arxiv.org/html/2607.10059v1#A6 — Appendix F Full Results and Analysis; https://arxiv.org/html/2607.10059v1#A2.SS6 — B.6 Evaluation Metrics。Limitations / counterevidence：https://arxiv.org/html/2607.10059v1#A1 — Appendix A Limitations, Future Work, and Broader Impact; https://arxiv.org/html/2607.10059v1#A1.SS1 — A.1 Limitations。

**Artifact boundary。** Exact v1 links https://huggingface.co/MiniMaxAI/MiniMax-M2.5, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 新的安全控制点降低特定失败，但会引入误拒绝、旁路、观测不足或模型/任务迁移问题。 论文自身的边界信号是：LLM outputs are stochastic, so multi-run evaluation would likely reveal variance that single-run numbers do not capture.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`AGENT-TOOL-CALLING`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-10059:end -->

<!-- review:SF-2026-ARXIV-2607-10079:start -->
### MAG: A Web-Agent Benchmark and Harness for Multimodal Action and Guide Generation

<!-- claim:SF-2026-ARXIV-2607-10079:start -->Digital Adoption Platforms (DAPs) are embedded overlays widely used on web systems to guide users through operations inside a page, helping them get started with unfamiliar interfaces quickly. Completing a real task, however, rarely means clicking a few buttons on a single page: it takes a sequence of actions that unfolds across changing page states. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-10079:end -->

**为什么进入候选分母。** 摘要首要问题为“Digital Adoption Platforms (DAPs) are embedded overlays widely used on web systems to guide users through operations inside a page, helping them get started with unfamiliar interfaces quickly.”；它改变了 evaluation observable、对照组、判定粒度或结果解释边界，可能修正现有评测结论。

**机制与状态边界。** Digital Adoption Platforms (DAPs) are embedded overlays widely used on web systems to guide users through operations inside a page, helping them get started with unfamiliar interfaces quickly.

**证据证明什么。** Finally, we design a GRPO training method augmented with expert trajectories, which nearly doubles the success rate of a supervised 9B agent (from 6.9% to 13.2%) and improves guide quality at the same time.

**证据没有证明什么。** Limitations MAG is a new and deliberately hard task: live multistep websites, screenshot only observation, a 25 step budget, and two jointly scored outputs. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.10079v1#S1 — 1 Introduction; https://arxiv.org/html/2607.10079v1#S2 — 2 Related Work。Evaluation：https://arxiv.org/html/2607.10079v1#A4 — Appendix D Metric Definitions and Evaluation Protocol; https://arxiv.org/html/2607.10079v1#A6 — Appendix F Full Results。Limitations / counterevidence：https://arxiv.org/html/2607.10079v1#S7 — 7 Conclusion; https://arxiv.org/html/2607.10079v1#Sx1 — Limitations。

**Artifact boundary。** Exact v1 links https://huggingface.co/Qwen/Qwen3.5-9B, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：Limitations MAG is a new and deliberately hard task: live multistep websites, screenshot only observation, a 25 step budget, and two jointly scored outputs.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`PLATFORM-EVALUATION-SYSTEM`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-10079:end -->

<!-- review:SF-2026-ARXIV-2607-10096:start -->
### Scaling and Stabilizing Large-Scale Embedding-Based Retrieval

<!-- claim:SF-2026-ARXIV-2607-10096:start -->Embedding-based retrieval (EBR) is foundational to large-scale e-commerce search, yet its effectiveness is often constrained by the quality of training signals and the representational capacity of the encoder. Standard dual-encoders suffer from a training-inference gap: they are optimized on narrow candidate pools but must discriminate against hundreds of millions of items during inference. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-10096:end -->

**为什么进入候选分母。** 摘要首要问题为“Embedding-based retrieval (EBR) is foundational to large-scale e-commerce search, yet its effectiveness is often constrained by the quality of training signals and the representational capacity of the encoder.”；它改变检索证据、候选或模型迁移的长期数据与控制流。

**机制与状态边界。** In this paper, we present a unified pipeline deployed at Walmart that addresses both signal quality and model evolution.

**证据证明什么。** Validated through extensive offline experiments and online A/B testing, the proposed pipeline is deployed in live production, delivering a +7.34% improvement in NDCG@5 and a +0.50% lift in gross revenue.

**证据没有证明什么。** Exact v1 does not disclose a dedicated generalization or deployment guarantee beyond its stated evaluation scope. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.10096v1#S2 — 2. Methodology; https://arxiv.org/html/2607.10096v1#S2.SS1 — 2.1. Model Architecture。Evaluation：https://arxiv.org/html/2607.10096v1#S3.SS2 — 3.2. Offline Experiments Results; https://arxiv.org/html/2607.10096v1#S3 — 3. Offline Experiments。Limitations / counterevidence：https://arxiv.org/html/2607.10096v1#S5 — 5. Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更强检索信号或迁移机制提高召回与连续性，但引入索引陈旧、负样本偏差、证据冲突和在线成本。 论文自身的边界信号是：Exact v1 does not disclose a dedicated generalization or deployment guarantee beyond its stated evaluation scope.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`AGENT-RAG`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-10096:end -->

<!-- review:SF-2026-ARXIV-2607-10103:start -->
### LLM Watermarking as Big Data Provenance: A Deployment-Oriented Systematization

<!-- claim:SF-2026-ARXIV-2607-10103:start -->As large language models (LLMs) become widely deployed, their outputs can be copied, transformed, and redistributed at scale without reliable evidence of origin, creating risks for trust, accountability, intellectual property (IP) protection, and high-stakes decision-making. LLM watermarking addresses this problem by embedding detectable signals into text during or after generation. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-10103:end -->

**为什么进入候选分母。** 摘要首要问题为“As large language models (LLMs) become widely deployed, their outputs can be copied, transformed, and redistributed at scale without reliable evidence of origin, creating risks for trust, accountability, intellectual property (IP) protection, and high-stakes decision-making.”；它改变 artifact/evidence provenance 或攻击面的信任边界，可能影响发布与审计合同。

**机制与状态边界。** The paper organizes provenance workloads by the identity, lineage, mutation and query operations they require, then maps each operation to throughput, false-positive, robustness and governance obligations.

**证据证明什么。** Exact v1 contributes a systems taxonomy and evaluation blueprint, not a measured production implementation or a claim that one provenance architecture satisfies every workload.

**证据没有证明什么。** 6 Conclusion LLM watermarking is a promising tool for provenance, attribution, and auditing, but the literature remains difficult to compare due to mixed assumptions, unclear detection authority, and inconsistent threat models. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.10103v1#S2 — 2 Large Language Models and Risks; https://arxiv.org/html/2607.10103v1#S2.SS1 — 2.1 Large Language Models。Evaluation：https://arxiv.org/html/2607.10103v1#S1 — 1 Introduction; https://arxiv.org/html/2607.10103v1#S2 — 2 Large Language Models and Risks。Limitations / counterevidence：https://arxiv.org/html/2607.10103v1#S6 — 6 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更强 provenance 或攻击检测提高审计能力，但依赖密钥、参考版本、观测面或 threat model，不能替代内容正确性。 论文自身的边界信号是：6 Conclusion LLM watermarking is a promising tool for provenance, attribution, and auditing, but the literature remains difficult to compare due to mixed assumptions, unclear detection authority, and inconsistent threat models.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`PLATFORM-SECURITY`；evidence-stage relation：`principle_reuse`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-10103:end -->

<!-- review:SF-2026-ARXIV-2607-10110:start -->
### CHASE: Cache-Hole-Adapted Skip Exit for Looped State-Space Language Models

<!-- claim:SF-2026-ARXIV-2607-10110:start -->Recent work on looped language models suggests that many reasoning problems benefit from greater computational depth rather than from additional independent parameters. Existing studies, however, focus almost exclusively on Transformer backbones, leaving open whether this principle also applies to state-space language models. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-10110:end -->

**为什么进入候选分母。** 摘要首要问题为“Recent work on looped language models suggests that many reasoning problems benefit from greater computational depth rather than from additional independent parameters.”；它提出可跨 workload 讨论的状态、表示或计算机制，并给出旧方案的适用边界。

**机制与状态边界。** Existing studies, however, focus almost exclusively on Transformer backbones, leaving open whether this principle also applies to state-space language models.

**证据证明什么。** On two controlled reasoning tasks-Mano (modular-arithmetic manipulation) and p-hop induction-Looped Mamba consistently outperforms parameter-matched non-looped baselines and, in several settings, matches or exceeds non-looped models of equal effective depth.

**证据没有证明什么。** First, our experiments are limited to models up to 370M parameters, and we have not yet validated the scaling behavior of Looped Mamba at billion-parameter or larger scales. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.10110v1#S3 — 3 Proposed Method; https://arxiv.org/html/2607.10110v1#S3.SS1 — 3.1 Overall Architecture。Evaluation：https://arxiv.org/html/2607.10110v1#A1 — Appendix A Full Results for iso-FLOPs Evaluation; https://arxiv.org/html/2607.10110v1#A6 — Appendix F Fixed-Loop Inference Ablation。Limitations / counterevidence：https://arxiv.org/html/2607.10110v1#S6 — 6 Conclusion; https://arxiv.org/html/2607.10110v1#Sx1 — Limitations。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 新表示或状态机制扩大能力边界，但带来额外训练、状态管理、稳定性或泛化假设。 论文自身的边界信号是：First, our experiments are limited to models up to 370M parameters, and we have not yet validated the scaling behavior of Looped Mamba at billion-parameter or larger scales.

- Score V2：Design Delta 2 / System Reach 2 / Durability 3 = **7/9**。
- Stable owner 候选：`MODEL-LONG-CONTEXT`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-10110:end -->

<!-- review:SF-2026-ARXIV-2607-10139:start -->
### LLMs as a Jury: Cross-Model Consensus Can Outperform Process Reward Models for LLM Reasoning

<!-- claim:SF-2026-ARXIV-2607-10139:start -->Selecting the correct answer from a pool of candidate reasoning chains is the engine of test-time scaling, yet the standard selectors each carry a cost: self-consistency inherits the errors of the single model it resamples, and trained reward models need labeled data and transfer poorly off-distribution. We study a third signal, free at inference time: cross-model consensus, the degree to which independently trained models, each solving the problem once, agree on a final answer. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-10139:end -->

**为什么进入候选分母。** 摘要首要问题为“Selecting the correct answer from a pool of candidate reasoning chains is the engine of test-time scaling, yet the standard selectors each carry a cost: self-consistency inherits the errors of the single model it resamples, and trained reward models need labeled data and transfer poorly off-distribution.”；它改变了 evaluation observable、对照组、判定粒度或结果解释边界，可能修正现有评测结论。

**机制与状态边界。** We make this precise with a parameter-free law, derived in closed form, that predicts consensus accuracy from three measured panel statistics to a mean absolute error of $0.03$ and exposes the method's ceiling: a shared-error floor where models share a misconception, near zero on math but non-trivial on science.

**证据证明什么。** Cross-model consensus is thus a verifier we can characterize in advance: a law that says when to trust it, and a floor that marks where it cannot.

**证据没有证明什么。** To the extent that the selector rather than the generator bounds test-time scaling, a decorrelated panel is a strong default that uses only the models a practitioner already has. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.10139v1#S3 — 3 Cross-Model Consensus as a Verifier; https://arxiv.org/html/2607.10139v1#S5.SS1 — 5.1 Cross-model consensus is a strong Best-of- verifier。Evaluation：https://arxiv.org/html/2607.10139v1#A1 — Appendix A Experimental Setup; https://arxiv.org/html/2607.10139v1#A11 — Appendix K Additional Verifier Results。Limitations / counterevidence：https://arxiv.org/html/2607.10139v1#S6 — 6 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：To the extent that the selector rather than the generator bounds test-time scaling, a decorrelated panel is a strong default that uses only the models a practitioner already has.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`PLATFORM-EVALUATION-SYSTEM`；evidence-stage relation：`alternative_branch`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-10139:end -->

<!-- review:SF-2026-ARXIV-2607-10152:start -->
### Consensus as Collapse Policy: Communication Evidence, Horizons, and Prefix Decisions

<!-- claim:SF-2026-ARXIV-2607-10152:start -->Consensus protocols are usually specified by their terminal artifact: a decided value, replicated log, or finalized prefix. This output-first view hides the communication-derived evidence that makes such artifacts safe. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-10152:end -->

**为什么进入候选分母。** 摘要首要问题为“Consensus protocols are usually specified by their terminal artifact: a decided value, replicated log, or finalized prefix.”；它把 evidence identity、冲突、lineage 或 commit 变成显式状态，改变了 agent/workflow 的停止与审计条件。

**机制与状态边界。** Consensus is specified denotationally as collapse of admissible executions under accumulated evidence, separating the semantic evidence condition from any one protocol's message exchange.

**证据证明什么。** The contribution is a reusable specification framework and examples, not a new impossibility theorem, implementation, or replacement for protocol-specific safety and liveness proofs.

**证据没有证明什么。** The resources are not only messages, signatures, and latency, but also preserved distinctions, visible evidence, and valid points of collapse. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.10152v1#S1 — 1 Introduction; https://arxiv.org/html/2607.10152v1#S2 — 2 Consensus as Communication。Evaluation：https://arxiv.org/html/2607.10152v1#S1 — 1 Introduction; https://arxiv.org/html/2607.10152v1#S2 — 2 Consensus as Communication。Limitations / counterevidence：https://arxiv.org/html/2607.10152v1#S10 — 10 Discussion; https://arxiv.org/html/2607.10152v1#S11 — 11 Future Work。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 显式 evidence state 提高可追溯性，但新增 lineage、冲突、commit 与恢复语义，状态本身也必须被验证。 论文自身的边界信号是：The resources are not only messages, signatures, and latency, but also preserved distinctions, visible evidence, and valid points of collapse.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`AGENT-MULTI-AGENT`；evidence-stage relation：`explanatory_analogy`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-10152:end -->

<!-- review:SF-2026-ARXIV-2607-10183:start -->
### Automated Tensor Scheduling for Hybrid CPU-GPU LLM Inference on Consumer Devices

<!-- claim:SF-2026-ARXIV-2607-10183:start -->Running large language models on consumer devices such as laptops and desktops is challenging because model weights often exceed GPU memory capacity, making offloading inference necessary to extend effective model capacity with CPU memory. Existing offloading systems, however, typically rely on coarse layer-level or expert-level scheduling, which overlooks substantial heterogeneity among tensors within the same layer and adapts poorly to changing hardware load conditions on such devices. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-10183:end -->

**为什么进入候选分母。** 摘要首要问题为“Running large language models on consumer devices such as laptops and desktops is challenging because model weights often exceed GPU memory capacity, making offloading inference necessary to extend effective model capacity with CPU memory.”；它改变了推理期的状态放置、数据移动、执行控制或 SLO admission，属于长期 runtime 机制。

**机制与状态边界。** This paper presents ATSInfer, a hybrid CPU-GPU inference system for consumer devices that performs offloading at tensor granularity.

**证据证明什么。** These results show that ATSInfer can substantially improve the user experience of local LLM deployment on personal consumer devices.

**证据没有证明什么。** Overall, ATSInfer helps make local LLM deployment on resource-limited consumer devices more practical and responsive. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.10183v1#S2.SS1 — 2.1. CPU and GPU Architecture for Hybrid Inference; https://arxiv.org/html/2607.10183v1#S4 — 4. ATSInfer Design。Evaluation：https://arxiv.org/html/2607.10183v1#S5 — 5. Evaluation; https://arxiv.org/html/2607.10183v1#S5.SS1 — 5.1. Experimental Setup。Limitations / counterevidence：https://arxiv.org/html/2607.10183v1#S7 — 7. Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/ggerganov/llama.cpp, https://github.com/huggingface/accelerate, https://github.com/arXiv/html_feedback/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更激进的缓存、迁移、并行或专用执行会换取吞吐/时延，同时增加配置依赖、资源压力与回退路径。 论文自身的边界信号是：Overall, ATSInfer helps make local LLM deployment on resource-limited consumer devices more practical and responsive.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`INFER-TENSORRT-LLM`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-10183:end -->

<!-- review:SF-2026-ARXIV-2607-10186:start -->
### FlashAccel: Leveraging High-Bandwidth Flash (HBF) for High-Throughput LLM Inference

<!-- claim:SF-2026-ARXIV-2607-10186:start -->Large language model (LLM) inference is increasingly limited by the capacity of High-Bandwidth Memory (HBM) in GPUs, as model weights and KV cache grow rapidly. High-Bandwidth Flash (HBF) provides higher capacity than HBM while offering comparable bandwidth, making it a promising substrate for capacity-constrained LLM inference. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-10186:end -->

**为什么进入候选分母。** 摘要首要问题为“Large language model (LLM) inference is increasingly limited by the capacity of High-Bandwidth Memory (HBM) in GPUs, as model weights and KV cache grow rapidly.”；它改变了推理期的状态放置、数据移动、执行控制或 SLO admission，属于长期 runtime 机制。

**机制与状态边界。** We present FlashAccel, a co-designed system that enables efficient LLM inference using HBF.

**证据证明什么。** Experimental results demonstrate that integrating six HBF stacks into the GPU enables FlashAccel to deliver an average improvement of 2.49$\times$ and 1.93$\times$ in throughput per GPU and energy efficiency over the HBM-only GPU under a 100ms latency constraint, respectively.

**证据没有证明什么。** Exact v1 does not disclose a dedicated generalization or deployment guarantee beyond its stated evaluation scope. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.10186v1#S6 — 6. System Design; https://arxiv.org/html/2607.10186v1#S3.SS3 — 3.3. System Resource Management。Evaluation：https://arxiv.org/html/2607.10186v1#S7.SS2 — 7.2. Evaluation Results; https://arxiv.org/html/2607.10186v1#S7 — 7. Evaluation。Limitations / counterevidence：https://arxiv.org/html/2607.10186v1#S9 — 9. Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/badlogic/pi-mono, https://github.com/deepseek-ai/open-infra-index/blob/main/202502OpenSourceWeek/day_6_one_more_thing_deepseekV3R1_inference_system_overview.md, https://github.com/huggingface/accelerate; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更激进的缓存、迁移、并行或专用执行会换取吞吐/时延，同时增加配置依赖、资源压力与回退路径。 论文自身的边界信号是：Exact v1 does not disclose a dedicated generalization or deployment guarantee beyond its stated evaluation scope.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`INFER-GPU-MEMORY`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-10186:end -->

<!-- review:SF-2026-ARXIV-2607-10198:start -->
### Equal Accuracy, Unequal Evidence: Search APIs as Decision Surfaces for Tool-Using Agents

<!-- claim:SF-2026-ARXIV-2607-10198:start -->Search APIs are the fundamental retrieval layer for many agents and are often their most frequently used tool. Traditional search APIs provide URLs, titles, and snippets that preview website contents. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-10198:end -->

**为什么进入候选分母。** 摘要首要问题为“Search APIs are the fundamental retrieval layer for many agents and are often their most frequently used tool.”；它把 evidence identity、冲突、lineage 或 commit 变成显式状态，改变了 agent/workflow 的停止与审计条件。

**机制与状态边界。** In such systems, search API performance is often evaluated primarily by answer accuracy.

**证据证明什么。** Provider choice is therefore a retrieval-budget and policy decision, not merely a recall decision.

**证据没有证明什么。** The issue is not only whether evidence exists, but whether the decision surface makes the right evidence noticeable, trusted, and actionable. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.10198v1#S1 — 1 Introduction; https://arxiv.org/html/2607.10198v1#S2 — 2 Related Work。Evaluation：https://arxiv.org/html/2607.10198v1#A6 — Appendix F Results; https://arxiv.org/html/2607.10198v1#S3 — 3 Experimental Protocol。Limitations / counterevidence：https://arxiv.org/html/2607.10198v1#S5.SS5 — 5.5 Many failures occur despite visible answer text; https://arxiv.org/html/2607.10198v1#S6 — 6 Discussion。

**Artifact boundary。** Exact v1 links https://github.com/selvamsriram/search-api-decision-surface, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 显式 evidence state 提高可追溯性，但新增 lineage、冲突、commit 与恢复语义，状态本身也必须被验证。 论文自身的边界信号是：The issue is not only whether evidence exists, but whether the decision surface makes the right evidence noticeable, trusted, and actionable.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`AGENT-RAG`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-10198:end -->

<!-- review:SF-2026-ARXIV-2607-10203:start -->
### Adaptive Compute in Latent World Models: When Depth Helps, Hurts, or Doesn't Matter

<!-- claim:SF-2026-ARXIV-2607-10203:start -->Adaptive compute for world models -- early-exit or mixture-of-depths predictors that spend variable depth per rollout step -- presumes that extra depth buys better predictions. In autoregressive rollouts, where planning actually happens, that premise requires depth's per-step precision to survive composition. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-10203:end -->

**为什么进入候选分母。** 摘要首要问题为“Adaptive compute for world models -- early-exit or mixture-of-depths predictors that spend variable depth per rollout step -- presumes that extra depth buys better predictions.”；它改变了 evaluation observable、对照组、判定粒度或结果解释边界，可能修正现有评测结论。

**机制与状态边界。** In autoregressive rollouts, where planning actually happens, that premise requires depth's per-step precision to survive composition.

**证据证明什么。** Whether more compute helps a world model is not a task property; it is a property of the operating configuration, with a stable, predictable, mechanism-backed core.

**证据没有证明什么。** The planning validation (Section 9 ) is partial: P1 is confirmed two-sided (two intrinsic, one inversion) but misses on the two marginal tasks; the fixed-threshold P2 fails, and a leakage-controlled calibrated router recovers it on acrobot (3/3 seeds) but only borderline on cartpole; and planning on random-policy-trained models is coverage-limited (two tasks unviable). 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.10203v1#A1 — Appendix A Architecture and hyperparameters; https://arxiv.org/html/2607.10203v1#S10.SS0.SSS0.Px1 — Implications for adaptive-compute world models.。Evaluation：https://arxiv.org/html/2607.10203v1#S10.SS0.SSS0.Px2 — Implications for latent-model evaluation.; https://arxiv.org/html/2607.10203v1#S2.SS0.SSS0.Px3 — Evaluation of latent models.。Limitations / counterevidence：https://arxiv.org/html/2607.10203v1#S10 — 10 Discussion; https://arxiv.org/html/2607.10203v1#S11 — 11 Limitations。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：The planning validation (Section 9 ) is partial: P1 is confirmed two-sided (two intrinsic, one inversion) but misses on the two marginal tasks; the fixed-threshold P2 fails, and a leakage-controlled calibrated router recovers it on acrobot (3/3 seeds) but only borderline on cartpole; and planning on random-policy-trained models is coverage-limited (two tasks unviable).

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`MULTIMODAL-WORLD-MODELS`；evidence-stage relation：`corrective_evidence`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-10203:end -->

<!-- review:SF-2026-ARXIV-2607-10226:start -->
### When Are Sparse Feature Interventions Actually Localized? Matched Evaluation for SAE-Based Safety Control

<!-- claim:SF-2026-ARXIV-2607-10226:start -->We evaluate when sparse autoencoder (SAE) features act as localized control handles for safety-relevant behavior. This question is difficult because apparent success can arise from weak interventions, mismatched baselines, model robustness, or degenerate outputs that automated safety judges mark as unsafe without representing meaningful harmful compliance. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-10226:end -->

**为什么进入候选分母。** 摘要首要问题为“We evaluate when sparse autoencoder (SAE) features act as localized control handles for safety-relevant behavior.”；它改变了 evaluation observable、对照组、判定粒度或结果解释边界，可能修正现有评测结论。

**机制与状态边界。** We introduce a matched coherence-gated evaluation protocol for runtime safety interventions: methods are compared at matched target-effect points, and the primary target metric counts harmful compliance only when an output is both judge-unsafe and coherent.

**证据证明什么。** These results argue that SAE-based safety interventions should be evaluated as regime-dependent control mechanisms rather than assumed to be uniformly localized.

**证据没有证明什么。** 7 Limitations The perturbation metric is a proxy for locality, not a proof of causal isolation. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.10226v1#S5.SS3 — 5.3 RQ3: The Clean Regime Is Scale- and Architecture-Dependent; https://arxiv.org/html/2607.10226v1#S4.SS1 — 4.1 Models and SAEs。Evaluation：https://arxiv.org/html/2607.10226v1#S2.SS3 — 2.3 Safety Evaluation Artifacts; https://arxiv.org/html/2607.10226v1#S3 — 3 Matched Coherence-Gated Evaluation。Limitations / counterevidence：https://arxiv.org/html/2607.10226v1#S6 — 6 Discussion; https://arxiv.org/html/2607.10226v1#S7 — 7 Limitations。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：7 Limitations The perturbation metric is a proxy for locality, not a proof of causal isolation.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`PLATFORM-EVALUATION-SYSTEM`；evidence-stage relation：`corrective_evidence`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-10226:end -->

<!-- review:SF-2026-ARXIV-2607-10240:start -->
### What Does Your Short-Answer VQA Score Actually Measure? Evaluator-Dependent Instability in Multimodal Short-Answer Benchmarks

<!-- claim:SF-2026-ARXIV-2607-10240:start -->Short-answer VQA benchmarks conflate two distinct quantities: whether a model's answer is semantically correct, and whether that answer matches the surface form expected by the automatic evaluator. We study this conflation across six vision--language models and six benchmarks, using a human-validated semantic judge (97.6% precision) to audit over 37k official errors. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-10240:end -->

**为什么进入候选分母。** 摘要首要问题为“Short-answer VQA benchmarks conflate two distinct quantities: whether a model's answer is semantically correct, and whether that answer matches the surface form expected by the automatic evaluator.”；它改变了 evaluation observable、对照组、判定粒度或结果解释边界，可能修正现有评测结论。

**机制与状态边界。** We study this conflation across six vision--language models and six benchmarks, using a human-validated semantic judge (97.6% precision) to audit over 37k official errors.

**证据证明什么。** A second text-only judge reproduces the same benchmark-level false-negative pattern, showing that the effect is not an artifact of a single audit model.

**证据没有证明什么。** Conclusion Short-answer VQA benchmarks do not measure semantic success alone. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.10240v1#S3 — 3. Framework。Evaluation：https://arxiv.org/html/2607.10240v1#S3.SS3 — 3.3. Measuring Benchmark Undercount; https://arxiv.org/html/2607.10240v1#S4 — 4. Experimental Setup。Limitations / counterevidence：https://arxiv.org/html/2607.10240v1#S6 — 6. Discussion; https://arxiv.org/html/2607.10240v1#S7 — 7. Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：Conclusion Short-answer VQA benchmarks do not measure semantic success alone.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`PLATFORM-EVALUATION-SYSTEM`；evidence-stage relation：`corrective_evidence`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-10240:end -->

<!-- review:SF-2026-ARXIV-2607-10252:start -->
### One Token Is Enough: Fingerprinting and Verifying Large Language Models from Single-Token Output Distributions

<!-- claim:SF-2026-ARXIV-2607-10252:start -->Large language models (LLMs) are increasingly consumed through opaque serving chains - API aggregators, resellers, and inference providers - in which the client has no technical means to confirm that the model answering is the model advertised, and recent audits show that a substantial fraction of commercial endpoints deviate from the vendor's reference weights. Existing identification techniques require long generated texts, token-level log-probabilities, adversarially crafted prompts, or the model owner's cooperation. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-10252:end -->

**为什么进入候选分母。** 摘要首要问题为“Large language models (LLMs) are increasingly consumed through opaque serving chains - API aggregators, resellers, and inference providers - in which the client has no technical means to confirm that the model answering is the model advertised, and recent audits show that a substantial fraction of commercial endpoints deviate from the vendor's reference weights.”；它改变 artifact/evidence provenance 或攻击面的信任边界，可能影响发布与审计合同。

**机制与状态边界。** We further report ecosystem anomalies, including a proprietary-branded flagship endpoint distributionally indistinguishable from an open-weight Qwen model.

**证据证明什么。** Measuring 165 models served via a large commercial aggregator (OpenRouter), we find that (i) these distributions are highly non-uniform (median cell entropy 1.0 bit) and model-specific: split halves of the same model's samples lie an order of magnitude closer than samples of different models; (ii) Jensen-Shannon divergence between fingerprints recovers model lineage, assigning a model to its documented family with 59.5% leave-one-out accuracy against an 18.4% chance rate; and (iii) a biometric-style verification protocol achieves a 7.3% equal error rate with the full 40-cell battery, and below 11% with eight probe cells - roughly a hundred single-token queries per audit.

**证据没有证明什么。** We consider three tiers: (T1) oblivious – substitutes silently, does not inspect traffic; (T2) filtering – recognizes known audit prompts (e.g., published verbatim) and routes them to the genuine ; (T3) emulating – attempts to reproduce ’s answer distributions on arbitrary low-entropy prompts. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.10252v1#S4 — IV Method; https://arxiv.org/html/2607.10252v1#S6.SS4 — VI-D RQ4: Ecosystem Anomalies。Evaluation：https://arxiv.org/html/2607.10252v1#S5 — V Experimental Setup; https://arxiv.org/html/2607.10252v1#S6 — VI Results。Limitations / counterevidence：https://arxiv.org/html/2607.10252v1#S3 — III Threat Model; https://arxiv.org/html/2607.10252v1#S7 — VII Discussion。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更强 provenance 或攻击检测提高审计能力，但依赖密钥、参考版本、观测面或 threat model，不能替代内容正确性。 论文自身的边界信号是：We consider three tiers: (T1) oblivious – substitutes silently, does not inspect traffic; (T2) filtering – recognizes known audit prompts (e.g., published verbatim) and routes them to the genuine ; (T3) emulating – attempts to reproduce ’s answer distributions on arbitrary low-entropy prompts.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`PLATFORM-SECURITY`；evidence-stage relation：`alternative_branch`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-10252:end -->

<!-- review:SF-2026-ARXIV-2607-10265:start -->
### TGMS: An Agent-Native Bi-Temporal Graph Management System

<!-- claim:SF-2026-ARXIV-2607-10265:start -->Temporal graph questions require reliable handling of time, identifiers, and arithmetic. Large language model (LLM) agents often fail on these tasks, especially when a graph records both ordinary evolution and later corrections. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-10265:end -->

**为什么进入候选分母。** 摘要首要问题为“Temporal graph questions require reliable handling of time, identifiers, and arithmetic.”；它把上下文、记忆、进度或能力选择提升为可持久且可验证的 agent 状态。

**机制与状态边界。** We present TGMS, a bi-temporal property graph management system that exposes thirteen verified temporal operators as agent tools.

**证据证明什么。** The code, benchmark, and trace viewer are open source under Apache-2.0.

**证据没有证明什么。** Pattern claims are checked and reported but are not yet gated. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.10265v1#S6 — 6 Findings from live model traffic。Evaluation：https://arxiv.org/html/2607.10265v1#S5 — 5 Evaluation; https://arxiv.org/html/2607.10265v1#S5.SS1 — 5.1 Benchmark and protocol。Limitations / counterevidence：https://arxiv.org/html/2607.10265v1#S8 — 8 Limitations and roadmap; https://arxiv.org/html/2607.10265v1#S9 — 9 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/zxf-work/tgms, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 显式 agent state 改善恢复与控制，但增加状态陈旧、错误提交、跨轮污染和一致性责任。 论文自身的边界信号是：Pattern claims are checked and reported but are not yet gated.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`AGENT-MEMORY`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-10265:end -->

<!-- review:SF-2026-ARXIV-2607-10291:start -->
### Partial Contracts Suffice: Sound, LLM-Inferred Regression Verification

<!-- claim:SF-2026-ARXIV-2607-10291:start -->Software evolves continuously, yet ensuring that a patch preserves intended behavior without re-verifying an entire codebase remains difficult. Regression verification addresses this problem, but existing techniques require expensive whole-program reasoning or rely on manually written specifications that are rarely available in practice. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-10291:end -->

**为什么进入候选分母。** 摘要首要问题为“Software evolves continuously, yet ensuring that a patch preserves intended behavior without re-verifying an entire codebase remains difficult.”；它揭示局部安全检查或现有 guard 的边界，并提出可验证的新控制点。

**机制与状态边界。** We present the first contract-based regression verification tool.

**证据证明什么。** The contracts themselves are inferred automatically from the checker's own counterexamples, with no separate specification step; on Frama-C-Problems and the ANSSI X509 parser this reaches a verification rate comparable to tools AutoSpec and Preguss, while a passing result certifies at least as strong a property, which we call \emph{safety-preserving conditional equivalence}: enforcement plus caller-sufficiency.

**证据没有证明什么。** RQ2’s warm start tightens only within the seed’s clause shape and cannot reach a structurally different contract; we frame it as the marginal value of continued strengthening and keep judge strictly post hoc, so the loop is gated on enforcement, never on the tightness measure it reports. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.10291v1#S4.SS3 — IV-C System Architecture (C2); https://arxiv.org/html/2607.10291v1#S4 — IV Methodology。Evaluation：https://arxiv.org/html/2607.10291v1#S5 — V Evaluation; https://arxiv.org/html/2607.10291v1#S5.SS3 — V-C Experimental Setup。Limitations / counterevidence：https://arxiv.org/html/2607.10291v1#S5.SS6 — V-F Discussion; https://arxiv.org/html/2607.10291v1#S5.SS7 — V-G Threats To Validity。

**Artifact boundary。** Exact v1 links https://github.com/manavpatnaik/frama-c-problems, https://huggingface.co/moonshotai/Kimi-K2.6, https://github.com/shrBadihi/EqBench/issues/15; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 新的安全控制点降低特定失败，但会引入误拒绝、旁路、观测不足或模型/任务迁移问题。 论文自身的边界信号是：RQ2’s warm start tightens only within the seed’s clause shape and cannot reach a structurally different contract; we frame it as the marginal value of continued strengthening and keep judge strictly post hoc, so the loop is gated on enforcement, never on the tightness measure it reports.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`AGENT-WORKFLOW`；evidence-stage relation：`principle_reuse`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-10291:end -->

<!-- review:SF-2026-ARXIV-2607-10350:start -->
### ABot-AgentOS: A General Robotic Agent OS with Lifelong Multi-modal Memory

<!-- claim:SF-2026-ARXIV-2607-10350:start -->Recent VLM and VLA systems have improved robotic perception and action prediction, yet long-horizon embodied agents still require a general runtime layer for reasoning, memory, tool use, verification, and cross-embodiment execution. We present ABot-AgentOS, a general robotic Agent Operating System that sits above low-level controllers and provides a deliberative agent layer for scene-conditioned planning, context-isolated skill execution, multi-stage verification, multi-modal memory, and edge-cloud collaboration. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-10350:end -->

**为什么进入候选分母。** 摘要首要问题为“Recent VLM and VLA systems have improved robotic perception and action prediction, yet long-horizon embodied agents still require a general runtime layer for reasoning, memory, tool use, verification, and cross-embodiment execution.”；它把上下文、记忆、进度或能力选择提升为可持久且可验证的 agent 状态。

**机制与状态边界。** To evaluate such systems, we introduce EmbodiedWorldBench, an executable benchmark with 16 indoor, outdoor, and hybrid scenes, four difficulty levels, and over 200 tasks involving navigation, object search, NPC dialogue, dynamic events, and trace-grounded scoring.

**证据证明什么。** These results suggest that a general Agent OS layer can improve long-horizon embodied execution while providing persistent, auditable memory for continual interaction.

**证据没有证明什么。** Although EmbodiedWorldBench covers diverse scenario types, its scene diversity, social interaction depth, and current agent evaluation coverage remain limited; future work will report the complete benchmark evaluation and release EmbodiedWorldBench for open research use. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.10350v1#S2 — 2 Agent Framework; https://arxiv.org/html/2607.10350v1#S2.SS1 — 2.1 Architecture Overview。Evaluation：https://arxiv.org/html/2607.10350v1#S3.SS2 — 3.2 Benchmark Construction; https://arxiv.org/html/2607.10350v1#S3.SS3 — 3.3 Evaluation Procedure and Metrics。Limitations / counterevidence：https://arxiv.org/html/2607.10350v1#S6 — 6 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 显式 agent state 改善恢复与控制，但增加状态陈旧、错误提交、跨轮污染和一致性责任。 论文自身的边界信号是：Although EmbodiedWorldBench covers diverse scenario types, its scene diversity, social interaction depth, and current agent evaluation coverage remain limited; future work will report the complete benchmark evaluation and release EmbodiedWorldBench for open research use.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`AGENT-WORKFLOW`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-10350:end -->

<!-- review:SF-2026-ARXIV-2607-10362:start -->
### A Control Theory of Predictability in Latent World Models

<!-- claim:SF-2026-ARXIV-2607-10362:start -->Latent world models are trained to predict future states in a learned representation and are then deployed inside a planner that selects actions by simulating them forward. Current practice adopts the prediction error, the single- or multi-step rollout loss on held-out data, as the training and model-selection objective, on the assumption that a lower prediction error yields better control. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-10362:end -->

**为什么进入候选分母。** 摘要首要问题为“Latent world models are trained to predict future states in a learned representation and are then deployed inside a planner that selects actions by simulating them forward.”；它改变了 evaluation observable、对照组、判定粒度或结果解释边界，可能修正现有评测结论。

**机制与状态边界。** Current practice adopts the prediction error, the single- or multi-step rollout loss on held-out data, as the training and model-selection objective, on the assumption that a lower prediction error yields better control.

**证据证明什么。** We show that this assumption is unreliable for a structural reason: a planner does not query the model on the training distribution but on the states that its candidate actions reach, which generally leave the data manifold, so an error averaged over the data cannot by itself govern control.

**证据没有证明什么。** Its regret is bounded by a single quantity—the gap between predicted and true plan-cost at the plan the planner commits to—so the correct control objective is to make predicted cost track true cost, not to lower data-averaged prediction error, which we prove neither bounds nor tracks that gap once actions carry the query off the data manifold. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.10362v1#S5.SS1 — 5.1 A theory-guided intervention: linear state readout。Evaluation：https://arxiv.org/html/2607.10362v1#S5.SS2 — 5.2 Control experiments on latent world models; https://arxiv.org/html/2607.10362v1#S5.SS3 — 5.3 Cross-task validation of the state readout。Limitations / counterevidence：https://arxiv.org/html/2607.10362v1#S6 — 6 Discussion and Outlook; https://arxiv.org/html/2607.10362v1#S7 — 7 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：Its regret is bounded by a single quantity—the gap between predicted and true plan-cost at the plan the planner commits to—so the correct control objective is to make predicted cost track true cost, not to lower data-averaged prediction error, which we prove neither bounds nor tracks that gap once actions carry the query off the data manifold.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`MULTIMODAL-WORLD-MODELS`；evidence-stage relation：`corrective_evidence`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-10362:end -->

<!-- review:SF-2026-ARXIV-2607-10389:start -->
### Stateful Worlds, Stateless Elasticity: Exact-State Serving for Interactive World Models

<!-- claim:SF-2026-ARXIV-2607-10389:start -->A persistent interactive world model keeps its running state resident on the GPU that serves it: a multi-gigabyte attention cache, almost all of it rewritten at every generation step. That state cannot be recomputed in interactive time or approximated without changing the world, so a live session pins its device. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-10389:end -->

**为什么进入候选分母。** 摘要首要问题为“A persistent interactive world model keeps its running state resident on the GPU that serves it: a multi-gigabyte attention cache, almost all of it rewritten at every generation step.”；它改变了推理期的状态放置、数据移动、执行控制或 SLO admission，属于长期 runtime 机制。

**机制与状态边界。** That state cannot be recomputed in interactive time or approximated without changing the world, so a live session pins its device.

**证据证明什么。** Exact-state elasticity is a joint scheduling problem over transport and verification.

**证据没有证明什么。** What is not public is a replayable world-model production trace (the one production operator ( 33 ) publishes only per-minute aggregates), so a validated production mix does not yet exist. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.10389v1#A7 — Appendix G Cross-architecture readout detail; https://arxiv.org/html/2607.10389v1#S5 — 5. Design and Implementation。Evaluation：https://arxiv.org/html/2607.10389v1#S6 — 6. Evaluation; https://arxiv.org/html/2607.10389v1#S3 — 3. Measurement Study。Limitations / counterevidence：https://arxiv.org/html/2607.10389v1#S8 — 8. Limitations and Open Problems。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更激进的缓存、迁移、并行或专用执行会换取吞吐/时延，同时增加配置依赖、资源压力与回退路径。 论文自身的边界信号是：What is not public is a replayable world-model production trace (the one production operator ( 33 ) publishes only per-minute aggregates), so a validated production mix does not yet exist.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`INFER-SCHEDULING`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-10389:end -->

<!-- review:SF-2026-ARXIV-2607-10463:start -->
### GRASP: GRanularity-Aware Search Policy for Agentic RAG

<!-- claim:SF-2026-ARXIV-2607-10463:start -->Agentic retrieval-augmented generation (RAG) extends static RAG by allowing language models to iteratively reason, generate search queries, retrieve evidence, and predict answers. However, it remains challenging for models to decide when to retrieve, whether to use lexical matching or semantic similarity, and how to control context granularity to prevent irrelevant tokens from interfering with agent reasoning. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-10463:end -->

**为什么进入候选分母。** 摘要首要问题为“Agentic retrieval-augmented generation (RAG) extends static RAG by allowing language models to iteratively reason, generate search queries, retrieve evidence, and predict answers.”；它改变检索证据、候选或模型迁移的长期数据与控制流。

**机制与状态边界。** In this paper, we introduce GRASP, a reinforcement learning (RL) framework for training agents to adaptively coordinate complementary retrieval tools during multi-step reasoning.

**证据证明什么。** Experiments on multi-hop reasoning benchmarks show that GRASP improves both retrieval recall and downstream question answering performance compared with single-step retrieval, prompting-based agentic RAG, and RL-based retrieval baselines.

**证据没有证明什么。** First, our reward design depends on gold supporting-fact annotations. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.10463v1#S3 — 3 Methodology; https://arxiv.org/html/2607.10463v1#S3.SS1 — 3.1 Action Design。Evaluation：https://arxiv.org/html/2607.10463v1#S4 — 4 Experimental Setup; https://arxiv.org/html/2607.10463v1#S4.SS4 — 4.4 Evaluation Metrics。Limitations / counterevidence：https://arxiv.org/html/2607.10463v1#S6 — 6 Conclusion and Future Work; https://arxiv.org/html/2607.10463v1#Sx1 — Limitations。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更强检索信号或迁移机制提高召回与连续性，但引入索引陈旧、负样本偏差、证据冲突和在线成本。 论文自身的边界信号是：First, our reward design depends on gold supporting-fact annotations.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`AGENT-RAG`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-10463:end -->

<!-- review:SF-2026-ARXIV-2607-10491:start -->
### EvidentialRAG: Quantifying and Mitigating Information Conflict in Multi-Source Retrieval-Augmented Generation via Evidential Deep Learning

<!-- claim:SF-2026-ARXIV-2607-10491:start -->Retrieval-augmented generation grounds large language models in external evidence, but most pipelines still treat retrieved passages as deterministic and mutually consistent context. In open information environments, retrieved sources may disagree because of temporal drift, source error, ambiguity, or genuine uncertainty. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-10491:end -->

**为什么进入候选分母。** 摘要首要问题为“Retrieval-augmented generation grounds large language models in external evidence, but most pipelines still treat retrieved passages as deterministic and mutually consistent context.”；它把 evidence identity、冲突、lineage 或 commit 变成显式状态，改变了 agent/workflow 的停止与审计条件。

**机制与状态边界。** This paper introduces ERAG, an uncertainty-aware RAG framework that converts retrieved chunks into probabilistic evidence before generation.

**证据证明什么。** These results suggest that evidential modeling is a practical mechanism for trustworthy information processing in foundation-model-based retrieval systems.

**证据没有证明什么。** 6.4 Limitations and threats to validity The first limitation is evaluator reliability. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.10491v1#S3 — 3 Methodology; https://arxiv.org/html/2607.10491v1#S6.SS1 — 6.1 Implications for expert and intelligent retrieval systems。Evaluation：https://arxiv.org/html/2607.10491v1#S4 — 4 Experimental setup; https://arxiv.org/html/2607.10491v1#S4.SS4 — 4.4 Evaluation metrics。Limitations / counterevidence：https://arxiv.org/html/2607.10491v1#S6.SS4 — 6.4 Limitations and threats to validity; https://arxiv.org/html/2607.10491v1#S6 — 6 Discussion。

**Artifact boundary。** Exact v1 links https://dx.doi.org/10.18653/v1/2020.emnlp-demos.6, https://aclanthology.org/2020.emnlp-demos.6/, https://github.com/arXiv/html_feedback/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 显式 evidence state 提高可追溯性，但新增 lineage、冲突、commit 与恢复语义，状态本身也必须被验证。 论文自身的边界信号是：6.4 Limitations and threats to validity The first limitation is evaluator reliability.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`AGENT-RAG`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-10491:end -->

<!-- review:SF-2026-ARXIV-2607-10582:start -->
### MemDecay: Region-Aware KV Cache Eviction for Efficient LLM Agent Inference

<!-- claim:SF-2026-ARXIV-2607-10582:start -->Large language model (LLM) agents accumulate heterogeneous context, including system instructions, plans, user turns, retrieved documents, tool outputs, and intermediate reasoning, whose key-value (KV) cache can become a major memory bottleneck. Existing eviction policies generally apply the same attention- or recency-based rule to every token, ignoring semantic structure already available to the agent orchestrator. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-10582:end -->

**为什么进入候选分母。** 摘要首要问题为“Large language model (LLM) agents accumulate heterogeneous context, including system instructions, plans, user turns, retrieved documents, tool outputs, and intermediate reasoning, whose key-value (KV) cache can become a major memory bottleneck.”；它改变了推理期的状态放置、数据移动、执行控制或 SLO admission，属于长期 runtime 机制。

**机制与状态边界。** We introduce MemDecay, a training-free, region-aware KV-cache eviction policy.

**证据证明什么。** The exact-v1 experiments support region-aware KV eviction for the reported agent traces; they do not establish one universal eviction policy across all prompts and memory hierarchies.

**证据没有证明什么。** The base policy cannot recover an evicted token when later context makes it relevant again, and such saliency shifts are documented in multi-turn agent traces [ 25 ] ; the user-region result in Section IV-C , where the oldest unpinned facts are evicted and later probed, is a measured instance. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.10582v1#S3 — III Proposed Method。Evaluation：https://arxiv.org/html/2607.10582v1#S4 — IV Evaluation。Limitations / counterevidence：https://arxiv.org/html/2607.10582v1#S5 — V Discussion and Limitations。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更激进的缓存、迁移、并行或专用执行会换取吞吐/时延，同时增加配置依赖、资源压力与回退路径。 论文自身的边界信号是：The base policy cannot recover an evicted token when later context makes it relevant again, and such saliency shifts are documented in multi-turn agent traces [ 25 ] ; the user-region result in Section IV-C , where the oldest unpinned facts are evicted and later probed, is a measured instance.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`INFER-KV-CACHE`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-10582:end -->

<!-- review:SF-2026-ARXIV-2607-10661:start -->
### Unlocking Parallelism in Autoregressive Language Models via Speculative Decoding with Progressive Tree Drafting

<!-- claim:SF-2026-ARXIV-2607-10661:start -->Speculative decoding has significantly accelerated Large Language Model (LLM) inference by alleviating memory-bound bottlenecks. However, traditional speculative decoding typically relies on auxiliary draft modules, incurring significant training and communication overhead. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-10661:end -->

**为什么进入候选分母。** 摘要首要问题为“Speculative decoding has significantly accelerated Large Language Model (LLM) inference by alleviating memory-bound bottlenecks.”；它改变了推理期的状态放置、数据移动、执行控制或 SLO admission，属于长期 runtime 机制。

**机制与状态边界。** In this paper, we propose \textbf{Progressive Tree Drafting (PTD)}, which employs a structured, guided parallel drafting strategy to harness the model's parallel potential.

**证据证明什么。** Experiments demonstrate that PTD achieves up to $2\times$ decoding speedup across various benchmarks while remaining training-free and model-agnostic.

**证据没有证明什么。** Future research will explore dense semantic representations, like semantic graphs, to enable more guided and efficient draft generation beyond current tree-based methods. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.10661v1#S3 — 3 Methodology; https://arxiv.org/html/2607.10661v1#A4 — Appendix D Progressive Tree Drafting Decoding Algorithm。Evaluation：https://arxiv.org/html/2607.10661v1#A3 — Appendix C Overhead Analysis; https://arxiv.org/html/2607.10661v1#A7 — Appendix G Generation Quality Evaluation: A Comparison Between PTD and Autoregressive Decoding under the Sampling Strategy。Limitations / counterevidence：https://arxiv.org/html/2607.10661v1#S5 — 5 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更激进的缓存、迁移、并行或专用执行会换取吞吐/时延，同时增加配置依赖、资源压力与回退路径。 论文自身的边界信号是：Future research will explore dense semantic representations, like semantic graphs, to enable more guided and efficient draft generation beyond current tree-based methods.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`INFER-SPECULATIVE-DECODING`；evidence-stage relation：`alternative_branch`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-10661:end -->

<!-- review:SF-2026-ARXIV-2607-10709:start -->
### PromptGraph: Graph-Guided Prompt Sanitization for Balancing Privacy and Utility in LLM Inference

<!-- claim:SF-2026-ARXIV-2607-10709:start -->Large Language Model (LLM) services introduce a fundamental privacy challenge. Sensitive information may be inferred not only from explicit identifiers, such as names or phone numbers, but also from contextual associations among otherwise innocuous spans. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-10709:end -->

**为什么进入候选分母。** 摘要首要问题为“Large Language Model (LLM) services introduce a fundamental privacy challenge.”；它改变推理期隐私处理的状态与 utility/security trade-off。

**机制与状态边界。** In this paper, we propose PromptGraph, a graph-guided prompt-sanitization approach for privacy-preserving LLM inference.

**证据证明什么。** We conduct extensive experiments showing that PromptGraph achieves a more favorable balance between privacy and utility than prompt-privacy baselines.

**证据没有证明什么。** Future work will extend this graph formulation from single-turn prompts to multi-turn interactions, where privacy evidence and useful contextual dependencies evolve across dialogue turns. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.10709v1#S4 — IV Methodology; https://arxiv.org/html/2607.10709v1#S3.SS2 — III-B Threat Model。Evaluation：https://arxiv.org/html/2607.10709v1#S5.SS2 — V-B Experimental Results; https://arxiv.org/html/2607.10709v1#S5 — V Experiments。Limitations / counterevidence：https://arxiv.org/html/2607.10709v1#S3.SS2 — III-B Threat Model; https://arxiv.org/html/2607.10709v1#S6 — VI Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 结构化隐私处理能缩小暴露面，但会牺牲语义保真并增加策略与图状态维护。 论文自身的边界信号是：Future work will extend this graph formulation from single-turn prompts to multi-turn interactions, where privacy evidence and useful contextual dependencies evolve across dialogue turns.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`PLATFORM-SECURITY`；evidence-stage relation：`release_security_override`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-10709:end -->

<!-- review:SF-2026-ARXIV-2607-10712:start -->
### Distributed Denial of Science: How Indirect Data Poisoning of AI Systems Can Industrialize Scientific Fraud

<!-- claim:SF-2026-ARXIV-2607-10712:start -->Scientific fraud is the instrument of doubt that malicious entities can use to establish controversy in science. Historically, it required the resources of a company: deep pockets, ghostwritten articles, and corrupt academics. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-10712:end -->

**为什么进入候选分母。** 摘要首要问题为“Scientific fraud is the instrument of doubt that malicious entities can use to establish controversy in science.”；它改变 artifact/evidence provenance 或攻击面的信任边界，可能影响发布与审计合同。

**机制与状态边界。** The attack requires no topic-specific trigger-words, agent access, indirect prompt injection, or fabricated papers, only the open data ecosystem and misleading metadata.

**证据证明什么。** We find that the persona still leaves 16.67% of runs with a poisoned conclusion, but provenance auditing reduces attack success rate to zero.

**证据没有证明什么。** In this section, we discuss the limitations of our findings, remark on the ethics of indirect data poisoning, and conclude the paper. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.10712v1#S1.SS1 — 1.1 Our approach; https://arxiv.org/html/2607.10712v1#S2.SS2 — 2.2 Poisoning attacks and defenses for AI systems。Evaluation：https://arxiv.org/html/2607.10712v1#S3.SS3 — 3.3 Experimental setup; https://arxiv.org/html/2607.10712v1#S4 — 4 Results。Limitations / counterevidence：https://arxiv.org/html/2607.10712v1#S3.SS1 — 3.1 Threat Model; https://arxiv.org/html/2607.10712v1#S6 — 6 Discussion。

**Artifact boundary。** Exact v1 links https://github.com/gyevnarb/indirect-data-poisoning, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更强 provenance 或攻击检测提高审计能力，但依赖密钥、参考版本、观测面或 threat model，不能替代内容正确性。 论文自身的边界信号是：In this section, we discuss the limitations of our findings, remark on the ethics of indirect data poisoning, and conclude the paper.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`PLATFORM-SECURITY`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-10712:end -->

<!-- review:SF-2026-ARXIV-2607-10750:start -->
### Filtering Harmful Actions Isn't Enough: Phantom Transfer in Agentic SDF

<!-- claim:SF-2026-ARXIV-2607-10750:start -->Synthetic data is widely used to train large language models because it is inexpensive to generate and easy to control. As models are increasingly deployed as agents, synthetic trajectories are likely to become an important source of training data for agentic behavior. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-10750:end -->

**为什么进入候选分母。** 摘要首要问题为“Synthetic data is widely used to train large language models because it is inexpensive to generate and easy to control.”；它揭示局部安全检查或现有 guard 的边界，并提出可验证的新控制点。

**机制与状态边界。** As models are increasingly deployed as agents, synthetic trajectories are likely to become an important source of training data for agentic behavior.

**证据证明什么。** Our results suggest that action level filtering is insufficient to ensure the safety of synthetic agentic training data and that dispositions introduced by the generating model can survive semantic inspection.

**证据没有证明什么。** This work does not provide proof for either hypothesis and we leave this up to future work. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.10750v1#S2 — 2 Methodology; https://arxiv.org/html/2607.10750v1#S2.SS1 — 2.1 Model。Evaluation：https://arxiv.org/html/2607.10750v1#A1 — Appendix A Tool call naming analysis; https://arxiv.org/html/2607.10750v1#S2.SS4 — 2.4 Evaluation。Limitations / counterevidence：https://arxiv.org/html/2607.10750v1#S4 — 4 Discussion; https://arxiv.org/html/2607.10750v1#S5 — 5 Limitations。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 新的安全控制点降低特定失败，但会引入误拒绝、旁路、观测不足或模型/任务迁移问题。 论文自身的边界信号是：This work does not provide proof for either hypothesis and we leave this up to future work.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`TRAIN-DATA`；evidence-stage relation：`corrective_evidence`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-10750:end -->

<!-- review:SF-2026-ARXIV-2607-10798:start -->
### Trust Before Fusion: QIMG-7 and Source-Aware Resolution for Polluted Multimodal RAG

<!-- claim:SF-2026-ARXIV-2607-10798:start -->Multimodal retrieval-augmented generation (RAG) is often evaluated with clean evidence, yet real retrieval can return topically relevant but unreliable content: false text and misleading images from corrupted metadata, entity swaps, typographic overlays, semantic edits, adversarial patches, blends, or style transfer. We introduce QIMG-7, a controlled benchmark for multimodal retrieval pollution in multi-sentence factual QA, spanning four datasets, seven image-attack families, and 16 paired clean/polluted regimes, for 1,760 evaluation rows per method. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-10798:end -->

**为什么进入候选分母。** 摘要首要问题为“Multimodal retrieval-augmented generation (RAG) is often evaluated with clean evidence, yet real retrieval can return topically relevant but unreliable content: false text and misleading images from corrupted metadata, entity swaps, typographic overlays, semantic edits, adversarial patches, blends, or style transfer.”；它把 evidence identity、冲突、lineage 或 commit 变成显式状态，改变了 agent/workflow 的停止与审计条件。

**机制与状态边界。** We introduce QIMG-7, a controlled benchmark for multimodal retrieval pollution in multi-sentence factual QA, spanning four datasets, seven image-attack families, and 16 paired clean/polluted regimes, for 1,760 evaluation rows per method.

**证据证明什么。** Ablations show that, in this text-first setting, explicit text-reliability modeling is the dominant driver of these gains.

**证据没有证明什么。** Future work includes learned reliability models, image-forensics-aware routing, and multilingual, cross-domain robustness testing beyond factual QA. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.10798v1#S4 — 4 Methods; https://arxiv.org/html/2607.10798v1#A13 — Appendix M Cross-Model Generalization Details。Evaluation：https://arxiv.org/html/2607.10798v1#A10 — Appendix J Cost and Latency Analysis; https://arxiv.org/html/2607.10798v1#A3 — Appendix C Per-Dataset QIMG-7 Results。Limitations / counterevidence：https://arxiv.org/html/2607.10798v1#S7 — 7 Conclusion and Future Work; https://arxiv.org/html/2607.10798v1#S3 — 3 Benchmark and Threat Model。

**Artifact boundary。** Exact v1 links https://github.com/SaadElDine/Trust_Before_Fusion, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 显式 evidence state 提高可追溯性，但新增 lineage、冲突、commit 与恢复语义，状态本身也必须被验证。 论文自身的边界信号是：Future work includes learned reliability models, image-forensics-aware routing, and multilingual, cross-domain robustness testing beyond factual QA.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`AGENT-RAG`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-10798:end -->

<!-- review:SF-2026-ARXIV-2607-10855:start -->
### Reliability Scaling Laws for Quantized Large Language Models

<!-- claim:SF-2026-ARXIV-2607-10855:start -->Quantization is a powerful strategy to build capable and resource-efficient large language models (LLMs) by reducing the bitwidth of the parameters. While quantized LLMs achieve state-of-the-art performance on unperturbed inputs using standard predictive metrics, their performance on perturbed inputs, measured using reliability metrics, remains underexplored, despite its importance for reliable deployment. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-10855:end -->

**为什么进入候选分母。** 摘要首要问题为“Quantization is a powerful strategy to build capable and resource-efficient large language models (LLMs) by reducing the bitwidth of the parameters.”；它改变了 evaluation observable、对照组、判定粒度或结果解释边界，可能修正现有评测结论。

**机制与状态边界。** To address this gap, we first conduct a comprehensive reliability evaluation of quantized LLMs consisting of three key components: (1) Uncertainty: We assess the trustworthiness of LLMs quantized to 2, 3, 4, and 8 bits using six different quantization methods, employing established uncertainty metrics. (2) Calibration: We assess how well-calibrated the uncertainty estimates of quantized models are across model scales and bit precisions. (3) Robustness: We design character-level and word-level input perturbations to evaluate the reliability of quantized models under semantically-preserving variations in the inputs that arise in real-world applications.

**证据证明什么。** Across the tested model sizes, precisions, quantizers and perturbations, predictive accuracy and reliability did not scale identically; the reported reliability optimum was configuration-dependent rather than monotonic in bit width.

**证据没有证明什么。** By studying reliability scaling trends, we show that reliability does not necessarily scale monotonically with the total number of model bits. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.10855v1#A1.SS1 — A.1 Quantization methods; https://arxiv.org/html/2607.10855v1#A8 — Appendix H Are the bit-level inference scalings consistent across different quantization methods?。Evaluation：https://arxiv.org/html/2607.10855v1#A1 — Appendix A Additional details on the experimental setting; https://arxiv.org/html/2607.10855v1#A1.SS2 — A.2 Evaluation datasets and generation。Limitations / counterevidence：https://arxiv.org/html/2607.10855v1#S5.SS3 — 5.3 Discussion and limitations; https://arxiv.org/html/2607.10855v1#S6 — 6 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/bitsandbytes-foundation/bitsandbytes, https://huggingface.co/docs/optimum/quanto/index, https://github.com/arXiv/html_feedback/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：By studying reliability scaling trends, we show that reliability does not necessarily scale monotonically with the total number of model bits.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`PLATFORM-EVALUATION-SYSTEM`；evidence-stage relation：`corrective_evidence`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-10855:end -->

<!-- review:SF-2026-ARXIV-2607-10959:start -->
### WSqD: A Horizon-Free Learning Rate Schedule for Large Model Training

<!-- claim:SF-2026-ARXIV-2607-10959:start -->Standard learning rate schedules such as cosine annealing are tied to a fixed training horizon, limiting their ability to accommodate post hoc horizon extension. Warmup-stable-decay (WSD) partially addresses this issue by maintaining a long constant-rate phase before a short linear cooldown, allowing training to resume from a pre-decay checkpoint. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-10959:end -->

**为什么进入候选分母。** 摘要首要问题为“Standard learning rate schedules such as cosine annealing are tied to a fixed training horizon, limiting their ability to accommodate post hoc horizon extension.”；它改变训练信号、credit、capacity 或 update ownership，而不是只报告单任务精度增量。

**机制与状态边界。** Motivated by stochastic convex optimization, we propose WSqD (Warmup with Square-root base and linear Decay), a learning rate schedule that replaces WSD's constant stable phase with a shifted inverse-square-root base while retaining the final linear cooldown.

**证据证明什么。** Empirically, on language-model pretraining using the SlimPajama corpus, WSqD matches or outperforms carefully tuned WSD and other baselines across multiple training horizons while reusing a single peak learning rate.

**证据没有证明什么。** On the theoretical side, extending our convergence analysis beyond the classical stochastic convex setting to nonconvex objectives and adaptive or momentum-based optimization forms another important direction for future work. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.10959v1#S1.SS1 — 1.1 Prior approaches; https://arxiv.org/html/2607.10959v1#A3.SS3 — C.3 Experiments on a smaller LLaMA model。Evaluation：https://arxiv.org/html/2607.10959v1#A1 — Appendix A Convergence analysis (proof of Theorem 1 ); https://arxiv.org/html/2607.10959v1#A3 — Appendix C Additional experiments。Limitations / counterevidence：https://arxiv.org/html/2607.10959v1#S5 — 5 Conclusion。

**Artifact boundary。** Exact v1 links https://huggingface.co/datasets/cerebras/SlimPajama-627B, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更密集或更定向的训练信号改善样本效率，但会增加 verifier 偏差、分布迁移和优化耦合。 论文自身的边界信号是：On the theoretical side, extending our convergence analysis beyond the classical stochastic convex setting to nonconvex objectives and adaptive or momentum-based optimization forms another important direction for future work.

- Score V2：Design Delta 3 / System Reach 2 / Durability 3 = **8/9**。
- Stable owner 候选：`TRAIN-PRETRAINING`；evidence-stage relation：`alternative_branch`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-10959:end -->

<!-- review:SF-2026-ARXIV-2607-10987:start -->
### [AAFLOW+] Stateful Operator Abstraction with Zero-Copy Distributed KV Cache Orchestration for Multi-Agent Workflows

<!-- claim:SF-2026-ARXIV-2607-10987:start -->Multi-agent LLM systems increasingly integrate retrieval, planning, and reasoning, but remain fundamentally text-centric, requiring agents to repeatedly recompute shared context through expensive prefill. Although single-request inference is known to be accelerated by KV-cache management, it is usually restricted to local serving scopes. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-10987:end -->

**为什么进入候选分母。** 摘要首要问题为“Multi-agent LLM systems increasingly integrate retrieval, planning, and reasoning, but remain fundamentally text-centric, requiring agents to repeatedly recompute shared context through expensive prefill.”；它改变了推理期的状态放置、数据移动、执行控制或 SLO admission，属于长期 runtime 机制。

**机制与状态边界。** We introduce AAFLOW+, a stateful extension of agentic workflow operators that makes KV cache a first-class distributed systems object.

**证据证明什么。** The results demonstrate that KV transmission outperforms recomputation on networks with moderate to high bandwidth, making sure KV-state sharing greatly increases efficiency in multi-agent LLM systems by replacing text passing.

**证据没有证明什么。** Limitations and Future Work These results should be viewed within defined limits. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.10987v1#A1 — Appendix A Extended System Design; https://arxiv.org/html/2607.10987v1#A1.SS1 — A.1. Design Components。Evaluation：https://arxiv.org/html/2607.10987v1#A6 — Appendix F Evaluation Details; https://arxiv.org/html/2607.10987v1#A6.SS1 — F.1. Experiment 1 extension: TTFT Reduction。Limitations / counterevidence：https://arxiv.org/html/2607.10987v1#S8 — 8. Limitations and Future Work; https://arxiv.org/html/2607.10987v1#S9 — 9. Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/arupcsedu/AAFLOW, https://github.com/vllm-project/vllm, https://github.com/arXiv/html_feedback/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更激进的缓存、迁移、并行或专用执行会换取吞吐/时延，同时增加配置依赖、资源压力与回退路径。 论文自身的边界信号是：Limitations and Future Work These results should be viewed within defined limits.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`INFER-DYNAMO`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-10987:end -->

<!-- review:SF-2026-ARXIV-2607-11070:start -->
### MJ: Multi-turn LLM Jailbreaking via Decomposed Credit Assignment

<!-- claim:SF-2026-ARXIV-2607-11070:start -->Modern large language models (LLMs) operate in interactive multi-turn settings, making multi-turn jailbreaking a realistic threat model and an important setting for automated red teaming. A core challenge in learning multi-turn jailbreak attackers is credit assignment: different turns contribute differently to the final outcome, yet existing learning signals are often too coarse to identify their individual contributions. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-11070:end -->

**为什么进入候选分母。** 摘要首要问题为“Modern large language models (LLMs) operate in interactive multi-turn settings, making multi-turn jailbreaking a realistic threat model and an important setting for automated red teaming.”；它改变训练信号、credit、capacity 或 update ownership，而不是只报告单任务精度增量。

**机制与状态边界。** We propose decomposed credit GRPO (DC-GRPO), a unified turn-level credit assignment framework for Group Relative Policy Optimization in multi-turn jailbreak learning.

**证据证明什么。** Across the victim models and jailbreak benchmarks reported in exact v1, both weighting variants substantially improved ASR, supporting turn-level group-relative credit as the common mechanism rather than one weighting formula.

**证据没有证明什么。** Our study nevertheless has important limitations: we do not fully evaluate substantially longer contexts or interaction horizons, and the behavior of DC-GRPO in such settings remains open. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.11070v1#S4 — 4 Method; https://arxiv.org/html/2607.11070v1#A1 — Appendix A Implementation Details。Evaluation：https://arxiv.org/html/2607.11070v1#S5.SS2 — 5.2 Experiment Results; https://arxiv.org/html/2607.11070v1#A1.SS1 — A.1 Training and evaluation hyperparameters。Limitations / counterevidence：https://arxiv.org/html/2607.11070v1#S6 — 6 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更密集或更定向的训练信号改善样本效率，但会增加 verifier 偏差、分布迁移和优化耦合。 论文自身的边界信号是：Our study nevertheless has important limitations: we do not fully evaluate substantially longer contexts or interaction horizons, and the behavior of DC-GRPO in such settings remains open.

- Score V2：Design Delta 3 / System Reach 2 / Durability 3 = **8/9**。
- Stable owner 候选：`TRAIN-GRPO`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-11070:end -->

<!-- review:SF-2026-ARXIV-2607-11079:start -->
### Are LLMs Ready for Scientific Discovery? A Capability-Oriented Benchmark for AI Scientists

<!-- claim:SF-2026-ARXIV-2607-11079:start -->Existing benchmarks for scientific data analysis evaluate LLMs primarily on code execution or workflow completion, overlooking that scientific analysis serves to support distinct types of scientific claims: hypothesis exploration, statistical inference, mechanistic explanation, each with different assumptions and validity criteria. We introduce SDABench, a benchmark that reorganizes evaluation around six capabilities (descriptive, exploratory, inferential, predictive, causal, and mechanistic) across five domains (Biology, Chemistry, Environment, Geography, Physics). 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-11079:end -->

**为什么进入候选分母。** 摘要首要问题为“Existing benchmarks for scientific data analysis evaluate LLMs primarily on code execution or workflow completion, overlooking that scientific analysis serves to support distinct types of scientific claims: hypothesis exploration, statistical inference, mechanistic explanation, each with different assumptions and validity criteria.”；它改变了 evaluation observable、对照组、判定粒度或结果解释边界，可能修正现有评测结论。

**机制与状态边界。** We introduce SDABench, a benchmark that reorganizes evaluation around six capabilities (descriptive, exploratory, inferential, predictive, causal, and mechanistic) across five domains (Biology, Chemistry, Environment, Geography, Physics).

**证据证明什么。** Evaluating 15 representative LLMs, we find that models handle descriptive analysis well but degrade sharply on tasks requiring assumption selection, latent-process modeling, or mechanistic reasoning.

**证据没有证明什么。** Stronger models do not lack scientific knowledge; rather, they apply it incorrectly. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.11079v1#S1 — 1 Introduction; https://arxiv.org/html/2607.11079v1#S2 — 2 Related Work。Evaluation：https://arxiv.org/html/2607.11079v1#S3 — 3 Benchmark; https://arxiv.org/html/2607.11079v1#S4 — 4 Experiments。Limitations / counterevidence：https://arxiv.org/html/2607.11079v1#S5 — 5 Discussion; https://arxiv.org/html/2607.11079v1#S6 — 6 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：Stronger models do not lack scientific knowledge; rather, they apply it incorrectly.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`PLATFORM-EVALUATION-SYSTEM`；evidence-stage relation：`principle_reuse`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-11079:end -->

<!-- review:SF-2026-ARXIV-2607-11086:start -->
### Rethinking MCP Security: A Large-Scale Study of Runtime MCP Servers and Security Scanner Reliability

<!-- claim:SF-2026-ARXIV-2607-11086:start -->The Model Context Protocol (MCP) has rapidly established itself as a standard interface for enabling LLM-based agents to interact with external tools and services. As MCP servers are increasingly entrusted with security-sensitive operations, understanding their real-world risks has become critical. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-11086:end -->

**为什么进入候选分母。** 摘要首要问题为“The Model Context Protocol (MCP) has rapidly established itself as a standard interface for enabling LLM-based agents to interact with external tools and services.”；它改变 artifact/evidence provenance 或攻击面的信任边界，可能影响发布与审计合同。

**机制与状态边界。** MCPZoo executes a large corpus of MCP servers behind controlled clients and compares runtime-observed behavior with static scanner findings, retaining server identity and invocation traces for attribution.

**证据证明什么。** The dynamic study finds that the 96.89% risk rate reported by existing scanners is not a reliable estimate of runtime exploitability for this corpus; it does not certify unobserved server behaviors as safe.

**证据没有证明什么。** As the MCP ecosystem is still evolving, broader benchmark sources (e.g., exploit scenarios or larger confirmed vulnerability sets) remain limited; incorporating them would further strengthen evaluation and is an important direction for future work. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.11086v1#S4 — 4. Characterize MCP Ecosystem; https://arxiv.org/html/2607.11086v1#S2.SS1 — 2.1. Model Context Protocol。Evaluation：https://arxiv.org/html/2607.11086v1#S5.SS2 — 5.2. Result Analysis; https://arxiv.org/html/2607.11086v1#A2 — Appendix B Scanner Analysis Logic。Limitations / counterevidence：https://arxiv.org/html/2607.11086v1#S6 — 6. Discussion; https://arxiv.org/html/2607.11086v1#S6.SS2 — 6.2. Limitation。

**Artifact boundary。** Exact v1 links https://github.com/aira-security/mcp-armor, https://github.com/antgroup/MCPScan, https://github.com/cisco-ai-defense/mcp-scanner; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更强 provenance 或攻击检测提高审计能力，但依赖密钥、参考版本、观测面或 threat model，不能替代内容正确性。 论文自身的边界信号是：As the MCP ecosystem is still evolving, broader benchmark sources (e.g., exploit scenarios or larger confirmed vulnerability sets) remain limited; incorporating them would further strengthen evaluation and is an important direction for future work.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`AGENT-MCP`；evidence-stage relation：`corrective_evidence`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-11086:end -->

<!-- review:SF-2026-ARXIV-2607-11131:start -->
### TIGER: Text-Conditioned Visual Gated Routing with Acceptance Alignment for Multimodal Speculative Decoding

<!-- claim:SF-2026-ARXIV-2607-11131:start -->Speculative decoding accelerates autoregressive generation by letting a lightweight drafter propose multiple tokens that are verified by a larger target model. Although effective for text-only LLMs, speculative decoding yields limited gains in VLMs because drafters often diverge on vision-critical content, while existing multimodal acceleration methods do not directly address irrelevant visual evidence or optimize the verifier-accepted prefix length that governs speedup. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-11131:end -->

**为什么进入候选分母。** 摘要首要问题为“Speculative decoding accelerates autoregressive generation by letting a lightweight drafter propose multiple tokens that are verified by a larger target model.”；它改变了推理期的状态放置、数据移动、执行控制或 SLO admission，属于长期 runtime 机制。

**机制与状态边界。** We propose TIGER, a Text-conditioned vIsual GatEd Routing framework for multimodal speculative decoding.

**证据证明什么。** Experiments show that TIGER yields consistent gains in accepted prefix length and speculative speedup under exact verifier-side speculative decoding, while achieving favorable quality-latency trade-offs with comparable downstream accuracy in visual-routing analyses.

**证据没有证明什么。** 5 Conclusion We study speculative decoding for vision-language models and show that draft quality alone is not sufficient; decoding efficiency depends directly on verifier acceptance. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.11131v1#A1 — Appendix A Method Details; https://arxiv.org/html/2607.11131v1#S3 — 3 Method。Evaluation：https://arxiv.org/html/2607.11131v1#A3.SS3 — C.3 Evaluation Benchmarks; https://arxiv.org/html/2607.11131v1#A1.SS1 — A.1 Cost and Complexity Analysis。Limitations / counterevidence：https://arxiv.org/html/2607.11131v1#S4 — 4 Experiments & Discussion; https://arxiv.org/html/2607.11131v1#S5 — 5 Conclusion。

**Artifact boundary。** Exact v1 links https://huggingface.co/liuhaotian/llava-v1.6-vicuna-7b, https://huggingface.co/liuhaotian/llava-v1.6-vicuna-13b, https://huggingface.co/Qwen/Qwen3-VL-4B-Instruct; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更激进的缓存、迁移、并行或专用执行会换取吞吐/时延，同时增加配置依赖、资源压力与回退路径。 论文自身的边界信号是：5 Conclusion We study speculative decoding for vision-language models and show that draft quality alone is not sufficient; decoding efficiency depends directly on verifier acceptance.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`INFER-SPECULATIVE-DECODING`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-11131:end -->

<!-- review:SF-2026-ARXIV-2607-11136:start -->
### Xema: Efficient Diffusion Serving through Fine-Grained Memory Management and Auto-Configuration

<!-- claim:SF-2026-ARXIV-2607-11136:start -->Diffusion models are increasingly deployed as production visual-generation services, where serving high-resolution image and long video generation is often limited by GPU memory. Popular memory-saving techniques such as weight offloading, sharding, and VAE slicing are often not practical because they tend to introduce significant performance overhead. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-11136:end -->

**为什么进入候选分母。** 摘要首要问题为“Diffusion models are increasingly deployed as production visual-generation services, where serving high-resolution image and long video generation is often limited by GPU memory.”；它改变了推理期的状态放置、数据移动、执行控制或 SLO admission，属于长期 runtime 机制。

**机制与状态边界。** In this paper, we present Xema, a memory-efficient diffusion serving system that exploits predictable tensor lifetimes for trace-guided memory optimization.

**证据证明什么。** Compared with existing serving configurations, Xema improves SLO attainment by up to 3.7x and reduces planning cost from 6.3 hours to 197 seconds compared with grid search.

**证据没有证明什么。** For each request template, Xema derives memory traces offline, applies mitigation only where and by the amount needed, and uses a static memory allocator to reduce fragmentation and keep runtime allocation consistent with offline analysis. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.11136v1#S4 — 4. System Overview; https://arxiv.org/html/2607.11136v1#S8 — 8. Implementation。Evaluation：https://arxiv.org/html/2607.11136v1#S7.SS2 — 7.2. Memory Analysis and Latency Profiling; https://arxiv.org/html/2607.11136v1#S9 — 9. Evaluation。Limitations / counterevidence：https://arxiv.org/html/2607.11136v1#S11 — 11. Conclusion。

**Artifact boundary。** Exact v1 links https://docs.vllm.ai/projects/vllm-omni/en/stable/user_guide/diffusion/cpu_offload_diffusion/, https://docs.vllm.ai/projects/vllm-omni/en/latest/design/feature/hsdp/, https://docs.vllm.ai/projects/vllm-omni/en/latest/cli/serve/; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更激进的缓存、迁移、并行或专用执行会换取吞吐/时延，同时增加配置依赖、资源压力与回退路径。 论文自身的边界信号是：For each request template, Xema derives memory traces offline, applies mitigation only where and by the amount needed, and uses a static memory allocator to reduce fragmentation and keep runtime allocation consistent with offline analysis.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`INFER-GPU-MEMORY`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-11136:end -->

<!-- review:SF-2026-ARXIV-2607-11138:start -->
### A Formal Hierarchical Architecture for Agentic Orchestration with Stack-Based Execution and Lazy Discovery

<!-- claim:SF-2026-ARXIV-2607-11138:start -->The rapid expansion of capabilities in Large Language Model (LLM) agents has exposed a critical architectural bottleneck: when agents are given access to a flat, monolithic registry of tools, the model must evaluate hundreds or thousands of options simultaneously. This leads to decision-space explosion, context window saturation, and degraded routing accuracy. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-11138:end -->

**为什么进入候选分母。** 摘要首要问题为“The rapid expansion of capabilities in Large Language Model (LLM) agents has exposed a critical architectural bottleneck: when agents are given access to a flat, monolithic registry of tools, the model must evaluate hundreds or thousands of options simultaneously.”；它把上下文、记忆、进度或能力选择提升为可持久且可验证的 agent 状态。

**机制与状态边界。** This leads to decision-space explosion, context window saturation, and degraded routing accuracy.

**证据证明什么。** We provide a mathematical formalization of the orchestration state, detailed algorithmic analysis of the execution loop, and controlled benchmarks comparing flat and hierarchical routing under increasing tool catalogs, multi-step workflow pressure, and visible schema-token exposure per LLM call.

**证据没有证明什么。** XI-C Benchmark and Evaluation Limitations The experimental evaluation (Section 9) uses a single LLM and inference-server configuration; results may not transfer across models. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.11138v1#S4 — IV System Model and Topological Architecture; https://arxiv.org/html/2607.11138v1#S11 — XI System Constraints and Limitations。Evaluation：https://arxiv.org/html/2607.11138v1#S11.SS3 — XI-C Benchmark and Evaluation Limitations; https://arxiv.org/html/2607.11138v1#S9 — IX Experimental Evaluation。Limitations / counterevidence：https://arxiv.org/html/2607.11138v1#S11 — XI System Constraints and Limitations; https://arxiv.org/html/2607.11138v1#S11.SS3 — XI-C Benchmark and Evaluation Limitations。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 显式 agent state 改善恢复与控制，但增加状态陈旧、错误提交、跨轮污染和一致性责任。 论文自身的边界信号是：XI-C Benchmark and Evaluation Limitations The experimental evaluation (Section 9) uses a single LLM and inference-server configuration; results may not transfer across models.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`AGENT-WORKFLOW`；evidence-stage relation：`alternative_branch`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-11138:end -->

<!-- review:SF-2026-ARXIV-2607-11149:start -->
### The Hidden Footprint: Making Storage a First-Class Metric for LLM Agent Evaluation

<!-- claim:SF-2026-ARXIV-2607-11149:start -->LLM agent benchmarks measure task completion, reliability, and inference cost, but not the persistent data an agent run leaves on disk, including logs, context snapshots, checkpoints, and debug traces. We introduce AgentFootprint, a cross-framework benchmark of post-run agent storage footprint. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-11149:end -->

**为什么进入候选分母。** 摘要首要问题为“LLM agent benchmarks measure task completion, reliability, and inference cost, but not the persistent data an agent run leaves on disk, including logs, context snapshots, checkpoints, and debug traces.”；它改变了 evaluation observable、对照组、判定粒度或结果解释边界，可能修正现有评测结论。

**机制与状态边界。** We introduce AgentFootprint, a cross-framework benchmark of post-run agent storage footprint.

**证据证明什么。** A content-addressed store reduces retention by 4.8x-32.7x while preserving every reconstructability score.

**证据没有证明什么。** Six audited boundaries apply: (i) controlled suites cover retrieval and retention, not general reasoning; (ii) results describe versioned configurations, not frameworks in the abstract; (iii) wild data are exports, not runtime residue; (iv) covers history only; (v) the roster is representative and workload-conditioned; (vi) fresh sandboxes understate shared threads (95.2 vs. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.11149v1#S3.SS3 — 3.3 Measurement Methodology: Serialization Masks Duplication; https://arxiv.org/html/2607.11149v1#S4.SS2 — 4.2 Frameworks and Fairness Protocol。Evaluation：https://arxiv.org/html/2607.11149v1#S4 — 4 The AgentFootprint Benchmark; https://arxiv.org/html/2607.11149v1#S5 — 5 Controlled Results。Limitations / counterevidence：https://arxiv.org/html/2607.11149v1#S8 — 8 Discussion and Limitations; https://arxiv.org/html/2607.11149v1#S9 — 9 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：Six audited boundaries apply: (i) controlled suites cover retrieval and retention, not general reasoning; (ii) results describe versioned configurations, not frameworks in the abstract; (iii) wild data are exports, not runtime residue; (iv) covers history only; (v) the roster is representative and workload-conditioned; (vi) fresh sandboxes understate shared threads (95.2 vs.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`PLATFORM-COST`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-11149:end -->

<!-- review:SF-2026-ARXIV-2607-11172:start -->
### STAMP: Provenance-Guided Credit Assignment for Deep Search Agents

<!-- claim:SF-2026-ARXIV-2607-11172:start -->Reinforcement learning for deep-search agents has largely focused on trajectory-level scoring -- outcome correctness, citation-aware rewards, and evidence coverage. Yet the actions that expose supporting documents receive no targeted credit, a gap we call the reward-credit mismatch. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-11172:end -->

**为什么进入候选分母。** 摘要首要问题为“Reinforcement learning for deep-search agents has largely focused on trajectory-level scoring -- outcome correctness, citation-aware rewards, and evidence coverage.”；它改变训练信号、credit、capacity 或 update ownership，而不是只报告单任务精度增量。

**机制与状态边界。** We propose STAMP, in which a reference-based verifier judges whether each cited document supports an entity or relation in a training-time evidence graph, and first-exposure attribution traces each supported citation back to the action that first surfaced it.

**证据证明什么。** On BrowseComp, BrowseComp-ZH, and xbench-DS, STAMP improves the GRPO baseline by +2.0/+5.5/+3.0 points under matched SFT initialization, training data, and search tools, and composes with both outcome-only and citation-rubric base rewards.

**证据没有证明什么。** 6 Limitations All experiments are conducted on Qwen3-30B-A3B-Thinking. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.11172v1#A2.SS1 — B.1 Model Architecture; https://arxiv.org/html/2607.11172v1#S2 — 2 Methodology。Evaluation：https://arxiv.org/html/2607.11172v1#A4 — Appendix D Supplementary Experiments; https://arxiv.org/html/2607.11172v1#S3 — 3 Experiments。Limitations / counterevidence：https://arxiv.org/html/2607.11172v1#S5 — 5 Conclusion; https://arxiv.org/html/2607.11172v1#S6 — 6 Limitations。

**Artifact boundary。** Exact v1 links https://huggingface.co/datasets/xbench/DeepSearch, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更密集或更定向的训练信号改善样本效率，但会增加 verifier 偏差、分布迁移和优化耦合。 论文自身的边界信号是：6 Limitations All experiments are conducted on Qwen3-30B-A3B-Thinking.

- Score V2：Design Delta 3 / System Reach 2 / Durability 3 = **8/9**。
- Stable owner 候选：`TRAIN-GRPO`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-11172:end -->

<!-- review:SF-2026-ARXIV-2607-11183:start -->
### Amplitude-Only FFN Intervention for Tool-Structured LLM Inference Method: Gated Evaluation Protocol, and Cross-Model Empirical Results

<!-- claim:SF-2026-ARXIV-2607-11183:start -->Large language models increasingly operate as tool-using agents, where small format, argument, or function-call errors can invalidate otherwise plausible responses. We study inference-time feed-forward network (FFN) intervention as a way to improve structured outputs without retraining model weights. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-11183:end -->

**为什么进入候选分母。** 摘要首要问题为“Large language models increasingly operate as tool-using agents, where small format, argument, or function-call errors can invalidate otherwise plausible responses.”；它提出可跨 workload 讨论的状态、表示或计算机制，并给出旧方案的适用边界。

**机制与状态边界。** We study inference-time feed-forward network (FFN) intervention as a way to improve structured outputs without retraining model weights.

**证据证明什么。** The results support model- and task-specific selection with strict fallback, not a universal AG switch.

**证据没有证明什么。** Offline combination oracles can choose the best candidate after seeing labels; deployed gates cannot. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/pdf/2607.11183v1#page=1 — PDF page 1; https://arxiv.org/pdf/2607.11183v1#page=10 — PDF page 10。Evaluation：https://arxiv.org/pdf/2607.11183v1#page=1 — PDF page 1; https://arxiv.org/pdf/2607.11183v1#page=10 — PDF page 10。Limitations / counterevidence：https://arxiv.org/pdf/2607.11183v1#page=1 — PDF page 1; https://arxiv.org/pdf/2607.11183v1#page=10 — PDF page 10。

**Artifact boundary。** Not Disclosed — exact v1 exposes no uniquely versioned artifact locator used to enlarge the manuscript claim boundary.

**Trade-off 与共存边界。** 新表示或状态机制扩大能力边界，但带来额外训练、状态管理、稳定性或泛化假设。 论文自身的边界信号是：Offline combination oracles can choose the best candidate after seeing labels; deployed gates cannot.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`MODEL-FFN`；evidence-stage relation：`alternative_branch`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-11183:end -->

<!-- review:SF-2026-ARXIV-2607-11226:start -->
### Heterogeneous Agent Cohorts for Safe Open-Ended Exploration with Runtime Constraint Memory

<!-- claim:SF-2026-ARXIV-2607-11226:start -->LLM agents today are caught in an awkward bind. Lock them down with static safety instructions and they rarely venture beyond the obvious; give them free reign with tools and multi-agent debate, and safety violations quickly follow. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-11226:end -->

**为什么进入候选分母。** 摘要首要问题为“LLM agents today are caught in an awkward bind.”；它揭示局部安全检查或现有 guard 的边界，并提出可验证的新控制点。

**机制与状态边界。** Lock them down with static safety instructions and they rarely venture beyond the obvious; give them free reign with tools and multi-agent debate, and safety violations quickly follow.

**证据证明什么。** In the reported spatial-semantic sandbox, the specialized validator prevented executed breaches while retained failure-derived constraints reduced repeated checking and communication cost; the evidence remains limited to that controlled environment.

**证据没有证明什么。** IX Conclusion and Future Work Our results demonstrate that creative exploration and runtime safety are not competing objectives to balance within a single model—they are complementary functions that heterogeneous role specialization can address in parallel. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.11226v1#S4 — IV Cohort System Architecture and Sandbox Implementation; https://arxiv.org/html/2607.11226v1#S2.SS1 — II-A Multi-Agent Collaborative Frameworks。Evaluation：https://arxiv.org/html/2607.11226v1#S7 — VII Empirical Evaluation and Results; https://arxiv.org/html/2607.11226v1#S7.SS3 — VII-C Experimental Protocol and Ablation Matrix (8 Configurations over 20 Seeds)。Limitations / counterevidence：https://arxiv.org/html/2607.11226v1#S8 — VIII Discussion and Limitations; https://arxiv.org/html/2607.11226v1#S9 — IX Conclusion and Future Work。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 新的安全控制点降低特定失败，但会引入误拒绝、旁路、观测不足或模型/任务迁移问题。 论文自身的边界信号是：IX Conclusion and Future Work Our results demonstrate that creative exploration and runtime safety are not competing objectives to balance within a single model—they are complementary functions that heterogeneous role specialization can address in parallel.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`AGENT-MULTI-AGENT`；evidence-stage relation：`alternative_branch`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-11226:end -->

<!-- review:SF-2026-ARXIV-2607-11250:start -->
### Multi-Agent LLMs Fail to Explore Each Other

<!-- claim:SF-2026-ARXIV-2607-11250:start -->Exploration is essential for reliable autonomy in multi-agent systems, yet it remains unclear whether large language model (LLM) agents can explore effectively when interacting with one another. We show that modern LLM agents fail to do so, often exhibiting myopic and polarized interaction patterns that lead to suboptimal coordination and increased regret. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-11250:end -->

**为什么进入候选分母。** 摘要首要问题为“Exploration is essential for reliable autonomy in multi-agent systems, yet it remains unclear whether large language model (LLM) agents can explore effectively when interacting with one another.”；它把上下文、记忆、进度或能力选择提升为可持久且可验证的 agent 状态。

**机制与状态边界。** To address this, we introduce Multi- Agent Contextual Exploration (MACE), a lightweight framework that explicitly promotes exploration through structured peer selection.

**证据证明什么。** We further show theoretically that the value of exploration increases with agent diversity.

**证据没有证明什么。** Future work should therefore investigate scalable variants of MACE, and would also be valuable to study whether explicit exploration can induce emergent specialization, robust collective behavior, and self-organizing coordination in massive agent societies. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.11250v1#S1 — 1 Introduction; https://arxiv.org/html/2607.11250v1#S2 — 2 Can LLMs Explore in Multi-Agent Environments? A Motivating Example。Evaluation：https://arxiv.org/html/2607.11250v1#A1 — Appendix A Appendix for the Delegation Experiment; https://arxiv.org/html/2607.11250v1#A3 — Appendix C Appendix for the Main Experiments。Limitations / counterevidence：https://arxiv.org/html/2607.11250v1#A6 — Appendix F Limitations and Future Directions; https://arxiv.org/html/2607.11250v1#S8 — 8 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/deeplearning-wisc/mace, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 显式 agent state 改善恢复与控制，但增加状态陈旧、错误提交、跨轮污染和一致性责任。 论文自身的边界信号是：Future work should therefore investigate scalable variants of MACE, and would also be valuable to study whether explicit exploration can induce emergent specialization, robust collective behavior, and self-organizing coordination in massive agent societies.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`AGENT-MULTI-AGENT`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-11250:end -->

<!-- review:SF-2026-ARXIV-2607-11262:start -->
### GPU-Tile-Sim: A Tile-Centric GPU Simulation Framework for LLM Hardware-Software Co-Design

<!-- claim:SF-2026-ARXIV-2607-11262:start -->Modern LLM (large language model) workloads increasingly rely on optimized GPU kernels through hardware-software co-design. These kernels achieve high-performance through fine-grained dependency scheduling and computation-memory overlap. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-11262:end -->

**为什么进入候选分母。** 摘要首要问题为“Modern LLM (large language model) workloads increasingly rely on optimized GPU kernels through hardware-software co-design.”；它改变了 evaluation observable、对照组、判定粒度或结果解释边界，可能修正现有评测结论。

**机制与状态边界。** GPU-Tile-Sim models tile-level dependency scheduling and compute-memory overlap so a kernel mapping can be evaluated without collapsing the execution into an instruction-agnostic throughput estimate.

**证据证明什么。** For the disclosed LLM kernels on A100 and H100, predicted performance is within 1.22%-8.71% MAPE of measurement; this accuracy range is not evidence for arbitrary kernels or future architectures.

**证据没有证明什么。** Retaining only data dependencies removes both constraint classes and permits the most unrealistic parallelism. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.11262v1#S2.SS2 — 2.2. GPU Architecture Evolution; https://arxiv.org/html/2607.11262v1#S7.SS3 — 7.3. Adapting to Latest Blackwell Architecture。Evaluation：https://arxiv.org/html/2607.11262v1#S6 — 6. Evaluation; https://arxiv.org/html/2607.11262v1#S6.SS1 — 6.1. Experimental Setup。Limitations / counterevidence：https://arxiv.org/html/2607.11262v1#S6.SS4 — 6.4. Analysis and Discussion; https://arxiv.org/html/2607.11262v1#S9 — 9. Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/gpgpu-sim/gpgpu-sim_distribution, https://github.com/NVIDIA/cutlass, https://github.com/tile-ai/tilelang; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：Retaining only data dependencies removes both constraint classes and permits the most unrealistic parallelism.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`INFER-TENSORRT-LLM`；evidence-stage relation：`principle_reuse`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-11262:end -->

<!-- review:SF-2026-ARXIV-2607-11317:start -->
### Calibrated e-CUSUM Decoding for Quantized Reasoning Models: Why Token Log-Probability Is the Wrong Observable for Decoding Monitors

<!-- claim:SF-2026-ARXIV-2607-11317:start -->Low-bit quantization makes small reasoning models inexpensive to deploy but can degrade their chains of thought. This motivates decoder-side monitors that intervene when generation becomes unreliable. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-11317:end -->

**为什么进入候选分母。** 摘要首要问题为“Low-bit quantization makes small reasoning models inexpensive to deploy but can degrade their chains of thought.”；它改变了 evaluation observable、对照组、判定粒度或结果解释边界，可能修正现有评测结论。

**机制与状态边界。** The paper rejects centered token log-probability as a drift statistic because its increments form a mean-zero martingale, then constructs a calibrated replacement and evaluates it conservatively.

**证据证明什么。** The mathematical result establishes why the natural centered-logprob monitor cannot accumulate the intended signal; the pilot replacement results are explicitly inconclusive rather than evidence of deployment-ready detection.

**证据没有证明什么。** 7 Limitations This is a single-model, single-dataset, single-seed study at ; the accuracy effect is not statistically significant and we do not claim it. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.11317v1#S3 — 3 Method。Evaluation：https://arxiv.org/html/2607.11317v1#S5 — 5 Experimental setup; https://arxiv.org/html/2607.11317v1#S6 — 6 Results。Limitations / counterevidence：https://arxiv.org/html/2607.11317v1#S6.SS2 — 6.2 Observed degeneration and failure modes; https://arxiv.org/html/2607.11317v1#S7 — 7 Limitations。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：7 Limitations This is a single-model, single-dataset, single-seed study at ; the accuracy effect is not statistically significant and we do not claim it.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`INFER-DECODE`；evidence-stage relation：`corrective_evidence`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-11317:end -->

<!-- review:SF-2026-ARXIV-2607-11346:start -->
### Compile, Then Page: Executable SOP Programs and a Capability-Gated Runtime for Procedural LLM Agents

<!-- claim:SF-2026-ARXIV-2607-11346:start -->Enterprise agents must follow long-horizon, conditional, safety-critical standard operating procedures (SOPs). We compile machine-readable SOP constraints into executable pseudo-code and run them with a program-guided (PG) stack machine that pages the active frame while an LLM performs semantic execution. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-11346:end -->

**为什么进入候选分母。** 摘要首要问题为“Enterprise agents must follow long-horizon, conditional, safety-critical standard operating procedures (SOPs).”；它把上下文、记忆、进度或能力选择提升为可持久且可验证的 agent 状态。

**机制与状态边界。** We compile machine-readable SOP constraints into executable pseudo-code and run them with a program-guided (PG) stack machine that pages the active frame while an LLM performs semantic execution.

**证据证明什么。** Two strong models independently show positive seven-domain PG contrasts (58:19 and 75:31 discordant pairs), whereas weak models are harmed.

**证据没有证明什么。** Compile first; page only after a model-level discipline check. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.11346v1#S3 — 3 Method。Evaluation：https://arxiv.org/html/2607.11346v1#S4 — 4 Experimental Setup; https://arxiv.org/html/2607.11346v1#S5 — 5 Results。Limitations / counterevidence：https://arxiv.org/html/2607.11346v1#S6 — 6 Discussion; https://arxiv.org/html/2607.11346v1#S7 — 7 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 显式 agent state 改善恢复与控制，但增加状态陈旧、错误提交、跨轮污染和一致性责任。 论文自身的边界信号是：Compile first; page only after a model-level discipline check.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`AGENT-WORKFLOW`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-11346:end -->

<!-- review:SF-2026-ARXIV-2607-11368:start -->
### Decomposing Runtime, Kernel, and Quantization Speedups via a Matched FP16 Intermediate: A Hardware-Conditioned Case Study on Four NVIDIA RTX A5000 GPUs

<!-- claim:SF-2026-ARXIV-2607-11368:start -->Reported serving speedups from quantized kernels typically bundle the weight format, the kernel, and the inference runtime into one number. We present an attribution study on four NVIDIA RTX A5000 GPUs, 24 GiB each, on a single host with NVLink-bridged pairs. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-11368:end -->

**为什么进入候选分母。** 摘要首要问题为“Reported serving speedups from quantized kernels typically bundle the weight format, the kernel, and the inference runtime into one number.”；它改变了 evaluation observable、对照组、判定粒度或结果解释边界，可能修正现有评测结论。

**机制与状态边界。** We present an attribution study on four NVIDIA RTX A5000 GPUs, 24 GiB each, on a single host with NVLink-bridged pairs.

**证据证明什么。** Sharding one instance across all four cards falls well below doubling: a profiler trace attributes about 80% of the per token shortfall to coordination, and an NVLink versus PCIe control on the same hardware shows similar realized bandwidth on both links, pointing away from link bandwidth as the cause.

**证据没有证明什么。** What we cannot measure is all four cards sharing one link, since the bridges on these cards are pairwise and a four card shared link would require a switch fabric found only on data center cards. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.11368v1#S2.SS8 — 2.8 Related Work: Adjacent Serving Systems; https://arxiv.org/html/2607.11368v1#S3 — 3 Methodology。Evaluation：https://arxiv.org/html/2607.11368v1#S3.SS6 — 3.6 Benchmark Cells; https://arxiv.org/html/2607.11368v1#S4 — 4 Experiments。Limitations / counterevidence：https://arxiv.org/html/2607.11368v1#S5.SS6 — 5.6 Threats to Validity and Limitations; https://arxiv.org/html/2607.11368v1#S5 — 5 Discussion。

**Artifact boundary。** Exact v1 links https://github.com/huggingface/text-generation-inference, https://github.com/NVIDIA/TensorRT-LLM, https://github.com/arXiv/html_feedback/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：What we cannot measure is all four cards sharing one link, since the bridges on these cards are pairwise and a four card shared link would require a switch fabric found only on data center cards.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`INFER-TENSORRT-LLM`；evidence-stage relation：`corrective_evidence`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-11368:end -->

<!-- review:SF-2026-ARXIV-2607-11388:start -->
### StructAgent: Harness Long-horizon Digital Agents with Unified Causal Structure

<!-- claim:SF-2026-ARXIV-2607-11388:start -->Recent advances in large language models (LLMs) and vision-language models (VLMs) have enabled increasingly capable digital agents for computer use. However, real-world tasks are often long-horizon and involve evolving contexts containing accumulated observations, intermediate edits, failed attempts, and partially completed executions. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-11388:end -->

**为什么进入候选分母。** 摘要首要问题为“Recent advances in large language models (LLMs) and vision-language models (VLMs) have enabled increasingly capable digital agents for computer use.”；它把上下文、记忆、进度或能力选择提升为可持久且可验证的 agent 状态。

**机制与状态边界。** We present \textbf{StructAgent}, a state-centered framework that introduces a unified state for maintaining compact, verifiable task progress and a structured workflow that regulates progress through verifier-backed state transitions.

**证据证明什么。** Extensive experiments demonstrate that StructAgent consistently improves a wide range of LLM and VLM backbones on long-horizon computer-use tasks.

**证据没有证明什么。** Ingredient over-ask Plan-prune drops every step except mining cobblestone; preload supplies 10, plan asks for 11. memory_bank canonical chains use worst-case ingredient counts; the LLM does not normalize to recipe minimum. steve-1 spatial blindness Explore-to-find reflection fires; thousands of steps with no resource gain. steve-1 [ 19 ] uses Transformer-XL [ 8 ] with s frame memory; text conditioning decays; similar spatial-memory limits are discussed in MrSteve [ 26 ] . 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.11388v1#S1 — 1 Introduction; https://arxiv.org/html/2607.11388v1#S2 — 2 Preliminaries。Evaluation：https://arxiv.org/html/2607.11388v1#A1 — Appendix A Additional OSWorld Results and Ablations; https://arxiv.org/html/2607.11388v1#A2 — Appendix B Web Benchmark Details。Limitations / counterevidence：https://arxiv.org/html/2607.11388v1#A6.SS6 — F.6 Failure modes; https://arxiv.org/html/2607.11388v1#S7 — 7 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/WenyiWU0111/StructAgent, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 显式 agent state 改善恢复与控制，但增加状态陈旧、错误提交、跨轮污染和一致性责任。 论文自身的边界信号是：Ingredient over-ask Plan-prune drops every step except mining cobblestone; preload supplies 10, plan asks for 11. memory_bank canonical chains use worst-case ingredient counts; the LLM does not normalize to recipe minimum. steve-1 spatial blindness Explore-to-find reflection fires; thousands of steps with no resource gain. steve-1 [ 19 ] uses Transformer-XL [ 8 ] with s frame memory; text conditioning decays; similar spatial-memory limits are discussed in MrSteve [ 26 ] .

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`AGENT-WORKFLOW`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-11388:end -->

<!-- review:SF-2026-ARXIV-2607-11399:start -->
### Agentic Routing: The Harness-Native Data Flywheel

<!-- claim:SF-2026-ARXIV-2607-11399:start -->Large language model agents are increasingly executed not by a single model call, but by an execution harness that manages observation, context, control, action, state, and verification. At the same time, frontier and open models are becoming structurally specialized: a model that is strong at code editing, long-context recovery, tool use, mathematical reasoning, or low-latency response may not dominate on the other axes. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-11399:end -->

**为什么进入候选分母。** 摘要首要问题为“Large language model agents are increasingly executed not by a single model call, but by an execution harness that manages observation, context, control, action, state, and verification.”；它改变资源分配、迁移、定价或路由的控制权与约束。

**机制与状态边界。** The harness routes at execution-step granularity using current observation, context, control state, prior failures, cost and outcome; the resulting trace becomes supervised data for later router updates.

**证据证明什么。** These records form a harness-native data flywheel: execution traces train better routers and harness-native models, which improve cost-quality trade-offs and generate more traces under the same budget.

**证据没有证明什么。** They define the environment in which model capabilities are observed, evaluated, and transformed into future training data. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.11399v1#A2 — Appendix B Case Evidence for Single-Model Routing; https://arxiv.org/html/2607.11399v1#A3 — Appendix C Case Evidence for Multi-Model Ensemble Routing。Evaluation：https://arxiv.org/html/2607.11399v1#A3.SS1 — C.1 Case A: Fortive Segment-Level Financial Analysis; https://arxiv.org/html/2607.11399v1#S4 — 4 Experiments。Limitations / counterevidence：https://arxiv.org/html/2607.11399v1#S6 — 6 Conclusions and Future Work。

**Artifact boundary。** Exact v1 links https://github.com/opensquilla/opensquilla, https://github.com/NousResearch/hermes-agent, https://github.com/openclaw/openclaw; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 动态资源控制提高利用率，但增加测量误差、迁移开销、租户公平和控制稳定性问题。 论文自身的边界信号是：They define the environment in which model capabilities are observed, evaluated, and transformed into future training data.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`AGENT-PLATFORM`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-11399:end -->

<!-- review:SF-2026-ARXIV-2607-11414:start -->
### Confidently Wrong: Detecting Hallucinations in Financial Question Answering from LLM Internal States

<!-- claim:SF-2026-ARXIV-2607-11414:start -->Large language models (LLMs) in financial applications fail most consequentially when they are confidently wrong. Hedged, uncertain answers invite scrutiny, whereas confident errors silently degrade downstream decisions without warning. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-11414:end -->

**为什么进入候选分母。** 摘要首要问题为“Large language models (LLMs) in financial applications fail most consequentially when they are confidently wrong.”；它改变了 evaluation observable、对照组、判定粒度或结果解释边界，可能修正现有评测结论。

**机制与状态边界。** Linear probes read internal answer-state activations and are compared with output-only confidence and resampling baselines, with special attention to answers that look confidently self-consistent.

**证据证明什么。** On FinQA and the three disclosed backbones, probes retain 0.68-0.77 AUROC where the strongest baselines fall to 0.55-0.63; the result is model- and task-scoped and does not make hidden-state confidence intrinsically calibrated.

**证据没有证明什么。** Future work could expand on the present experimental setting to address these deliberate design limits. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.11414v1#S4 — 4. Methods; https://arxiv.org/html/2607.11414v1#S5.SS2 — 5.2. Probe design across layers and pooling。Evaluation：https://arxiv.org/html/2607.11414v1#S4.SS2 — 4.2. Evaluation protocol and validity controls; https://arxiv.org/html/2607.11414v1#S5 — 5. Results。Limitations / counterevidence：https://arxiv.org/html/2607.11414v1#S6 — 6. Discussion and limitations; https://arxiv.org/html/2607.11414v1#S7 — 7. Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：Future work could expand on the present experimental setting to address these deliberate design limits.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`PLATFORM-EVALUATION-SYSTEM`；evidence-stage relation：`alternative_branch`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-11414:end -->

<!-- review:SF-2026-ARXIV-2607-11423:start -->
### ToFu: A White-Box, Token-Efficient Agent Harness for Researchers

<!-- claim:SF-2026-ARXIV-2607-11423:start -->Agentic coding tools present new opportunities to transform research workflows. The performance of agent systems built depends on both large language models (LLMs) and the harness around LLMs, which is the orchestration code that determines an agent's behavior. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-11423:end -->

**为什么进入候选分母。** 摘要首要问题为“Agentic coding tools present new opportunities to transform research workflows.”；它改变了 evaluation observable、对照组、判定粒度或结果解释边界，可能修正现有评测结论。

**机制与状态边界。** We present ToFu, an agentic harness for researchers that reads your codebase, edits files, runs commands, and integrates with your development tools.

**证据证明什么。** The released white-box harness demonstrates that orchestration logic and tool behavior can be inspected and modified while retaining a usable coding-agent workflow; benchmark comparisons do not establish universal harness superiority.

**证据没有证明什么。** First, our evaluation mainly focuses on coding ability, while evaluation in broader research-assistant scenarios is limited to a small human preference study with only three participants; due to cost constraints, we have not yet conducted large-scale studies with real users. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.11423v1#S2 — 2 ToFu architecture; https://arxiv.org/html/2607.11423v1#S2.SS1 — 2.1 Framework overview。Evaluation：https://arxiv.org/html/2607.11423v1#S4.SS2 — 4.2 Evaluation results; https://arxiv.org/html/2607.11423v1#A1 — Appendix A Human Evaluation。Limitations / counterevidence：https://arxiv.org/html/2607.11423v1#S6 — 6 Conclusion; https://arxiv.org/html/2607.11423v1#Sx1 — Limitations。

**Artifact boundary。** Exact v1 links https://github.com/NiuTrans/ToFu, https://github.com/rangehow/overleaf-mcp, https://www.anthropic.com/product/claude-code; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：First, our evaluation mainly focuses on coding ability, while evaluation in broader research-assistant scenarios is limited to a small human preference study with only three participants; due to cost constraints, we have not yet conducted large-scale studies with real users.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`AGENT-PLATFORM`；evidence-stage relation：`principle_reuse`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-11423:end -->

<!-- review:SF-2026-ARXIV-2607-11433:start -->
### Omni-Decision: A Progressive Evidence-State Agent System for Omni-Modal QA

<!-- claim:SF-2026-ARXIV-2607-11433:start -->Omni-modal evidence-seeking QA requires agents to answer questions whose evidence is sparsely distributed across videos, audio, images, web pages, and computation results. Existing agentic multimodal systems often leave evidence in scratchpads, tool trajectories, or free-form histories, making it difficult to track what has been grounded, what remains missing, and when the evidence is sufficient to answer. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-11433:end -->

**为什么进入候选分母。** 摘要首要问题为“Omni-modal evidence-seeking QA requires agents to answer questions whose evidence is sparsely distributed across videos, audio, images, web pages, and computation results.”；它把 evidence identity、冲突、lineage 或 commit 变成显式状态，改变了 agent/workflow 的停止与审计条件。

**机制与状态边界。** We propose Omni-Decision, a training-free evidence-state system that turns omni-modal QA into a query-scoped evidence-closure process.

**证据证明什么。** No-state ablations and trajectory audits in the reported omni-modal tasks support explicit evidence-state control as the source of the measured gains, within the disclosed models and evaluator protocol.

**证据没有证明什么。** We therefore use Appendix D only to define how the human primary audit is produced, not to introduce another accuracy metric. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.11433v1#A1 — Appendix A Relationship to representative agent frameworks; https://arxiv.org/html/2607.11433v1#S3 — 3 Method: Omni-Decision。Evaluation：https://arxiv.org/html/2607.11433v1#A3 — Appendix C Finite-sample uncertainty for the main OmniGAIA result; https://arxiv.org/html/2607.11433v1#A9.SS6 — I.6 Experimental configuration。Limitations / counterevidence：https://arxiv.org/html/2607.11433v1#S5 — 5 Discussion and limitations; https://arxiv.org/html/2607.11433v1#A4 — Appendix D Failure taxonomy and real-progress audit details。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 显式 evidence state 提高可追溯性，但新增 lineage、冲突、commit 与恢复语义，状态本身也必须被验证。 论文自身的边界信号是：We therefore use Appendix D only to define how the human primary audit is produced, not to introduce another accuracy metric.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`AGENT-WORKFLOW`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-11433:end -->

<!-- review:SF-2026-ARXIV-2607-11436:start -->
### The Ebb and Flow of Multimodal Focus: Scheduling Visual Relay Windows for Grounded VLM Reasoning

<!-- claim:SF-2026-ARXIV-2607-11436:start -->Vision-language models increasingly succeed on multimodal reasoning benchmarks, yet their visual evidence often becomes unstable once it enters the language stack, weakening evidence-grounded reasoning. To understand this fragility, we examine the internal dynamics of VLMs through a mechanistic lens and uncover a stable three-stage redistribution of multimodal attention focus across depth: an early question-conditioned organization, a critical middle visual-dominant relay, and a late return to answer formation. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-11436:end -->

**为什么进入候选分母。** 摘要首要问题为“Vision-language models increasingly succeed on multimodal reasoning benchmarks, yet their visual evidence often becomes unstable once it enters the language stack, weakening evidence-grounded reasoning.”；它提出可跨 workload 讨论的状态、表示或计算机制，并给出旧方案的适用边界。

**机制与状态边界。** Guided by this internal rhythm, we propose TRACE, a task-adaptive inference-time control framework with lightweight trained modules.

**证据证明什么。** These results show that explicitly controlling multimodal focus across depth offers a unified and effective mechanism for strengthening evidence-grounded multimodal reasoning.

**证据没有证明什么。** These limitations suggest several promising future directions: extending relay analysis beyond attention alone, studying relay control in longer and more dynamic generation settings, and turning relay-aware allocation into a more direct training objective. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.11436v1#S2.SS3 — 2.3 Inference-Time Control for Vision-Language Models; https://arxiv.org/html/2607.11436v1#S3.SS6 — 3.6 Thinking Models Improve Relay Match and Anchoring。Evaluation：https://arxiv.org/html/2607.11436v1#S4.SS2 — 4.2 Main Benchmark Results; https://arxiv.org/html/2607.11436v1#S2.SS2 — 2.2 Mechanistic Analysis of Multimodal Computation。Limitations / counterevidence：https://arxiv.org/html/2607.11436v1#S3.SS5 — 3.5 Relay Mismatch as an Evidence Assembly Failure; https://arxiv.org/html/2607.11436v1#S5 — 5 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/gooogleshanghai/visual-relay-window, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 新表示或状态机制扩大能力边界，但带来额外训练、状态管理、稳定性或泛化假设。 论文自身的边界信号是：These limitations suggest several promising future directions: extending relay analysis beyond attention alone, studying relay control in longer and more dynamic generation settings, and turning relay-aware allocation into a more direct training objective.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`MULTIMODAL-REPRESENTATION`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-11436:end -->

<!-- review:SF-2026-ARXIV-2607-11444:start -->
### UMoE:Unlocking Every Expert in Domain-Specific Training

<!-- claim:SF-2026-ARXIV-2607-11444:start -->Mixture-of-Experts (MoE) models scale capacity without proportional compute cost and have become a key architecture for frontier large language models (LLMs). Yet domain-specific post-training inherits an expert pool shaped by mixed-domain pre-training: a substantial subset of experts contributes little on the target domain, and standard supervised fine-tuning (SFT) leaves the composition of this pool unchanged. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-11444:end -->

**为什么进入候选分母。** 摘要首要问题为“Mixture-of-Experts (MoE) models scale capacity without proportional compute cost and have become a key architecture for frontier large language models (LLMs).”；它改变训练信号、credit、capacity 或 update ownership，而不是只报告单任务精度增量。

**机制与状态边界。** We propose a simple, budget-preserving pipeline that realigns the expert pool to the target domain before fine-tuning.

**证据证明什么。** Data-scaling experiments further show that the gain persists as training data grows.

**证据没有证明什么。** Exploring adaptive pruning ratios and architecture-specific perturbation strategies remains promising future work. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.11444v1#S3 — 3 Method; https://arxiv.org/html/2607.11444v1#A1 — Appendix A Full Algorithm。Evaluation：https://arxiv.org/html/2607.11444v1#S4 — 4 Experiments; https://arxiv.org/html/2607.11444v1#S4.SS2 — 4.2 Main Results。Limitations / counterevidence：https://arxiv.org/html/2607.11444v1#S6 — 6 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/LiveCodeBench/LiveCodeBench, https://huggingface.co/nex-agi/Nex-N2-mini, https://huggingface.co/datasets/nvidia/Nemotron-SFT-Science-v2; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更密集或更定向的训练信号改善样本效率，但会增加 verifier 偏差、分布迁移和优化耦合。 论文自身的边界信号是：Exploring adaptive pruning ratios and architecture-specific perturbation strategies remains promising future work.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`MODEL-MOE`；evidence-stage relation：`alternative_branch`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-11444:end -->

<!-- review:SF-2026-ARXIV-2607-11475:start -->
### HyperSafe: Inference-Time Safety Recovery for Fine-Tuned Language Models

<!-- claim:SF-2026-ARXIV-2607-11475:start -->Safety alignment in large language models can be fragile under fine-tuning, as even benign task adaptation may increase harmful compliance. Existing defenses mainly follow two directions: they either intervene during or after fine-tuning through retraining or weight modification, which can be costly and may hurt task performance, or they use model-agnostic safety classifiers, which may miss failures specific to a given fine-tuned checkpoint. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-11475:end -->

**为什么进入候选分母。** 摘要首要问题为“Safety alignment in large language models can be fragile under fine-tuning, as even benign task adaptation may increase harmful compliance.”；它揭示局部安全检查或现有 guard 的边界，并提出可验证的新控制点。

**机制与状态边界。** To meet these requirements, we propose HyperSafe, a framework that restores safety behavior by generating a model-specific Safe Side Network (SSN) for each fine-tuned checkpoint.

**证据证明什么。** HyperSafe reduces harmful response rates from 19-31% to below 1% on every held-out checkpoint, while keeping downstream task accuracy within 1% of the fine-tuned baseline on average.

**证据没有证明什么。** Two findings underline the generality: an SSN generated from a LoRA fingerprint transfers unchanged to its fully fine-tuned counterpart (Table 4 ), and a hypernetwork trained only on BeaverTails keeps AdvBench at 0.0% and HEx-PHI below 0.8% zero-shot on every held-out checkpoint. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.11475v1#A4 — Appendix D Architecture Sensitivity; https://arxiv.org/html/2607.11475v1#S3 — 3 Method。Evaluation：https://arxiv.org/html/2607.11475v1#A6 — Appendix F Detailed Loss-Component Ablation (Table 10 ); https://arxiv.org/html/2607.11475v1#A7 — Appendix G Detailed Training-Data Ablation (Table 11 )。Limitations / counterevidence：https://arxiv.org/html/2607.11475v1#S5 — 5 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/nokronim/project-safety-remedy, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 新的安全控制点降低特定失败，但会引入误拒绝、旁路、观测不足或模型/任务迁移问题。 论文自身的边界信号是：Two findings underline the generality: an SSN generated from a LoRA fingerprint transfers unchanged to its fully fine-tuned counterpart (Table 4 ), and a hypernetwork trained only on BeaverTails keeps AdvBench at 0.0% and HEx-PHI below 0.8% zero-shot on every held-out checkpoint.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`PLATFORM-SECURITY`；evidence-stage relation：`alternative_branch`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-11475:end -->

<!-- review:SF-2026-ARXIV-2607-11487:start -->
### LightMem-Ego: Your AI Memory for Everyday Life

<!-- claim:SF-2026-ARXIV-2607-11487:start -->Personal AI assistants on mobile and wearable devices continuously perceive users' daily lives through visual and audio streams. However, answering queries about past experiences requires lightweight multimodal memory that can continuously accumulate, organize, and retrieve long-term experiences, which remains challenging. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-11487:end -->

**为什么进入候选分母。** 摘要首要问题为“Personal AI assistants on mobile and wearable devices continuously perceive users' daily lives through visual and audio streams.”；它把上下文、记忆、进度或能力选择提升为可持久且可验证的 agent 状态。

**机制与状态边界。** LightMem-Ego maintains a hierarchical streaming multimodal memory that compresses egocentric observations into retrievable episodic and semantic state instead of replaying the full sensor history.

**证据证明什么。** The reported everyday-assistance evaluations support the hierarchy's accuracy-efficiency trade-off; repository availability alone does not establish long-horizon correctness or privacy safety.

**证据没有证明什么。** LightMem-Ego takes a step in this direction by showing how multimodal memory can support AI systems that not only understand utterances, but also understand lived experience. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.11487v1#S5.SS5 — 5.5 Capability Comparison with Existing Assistants and Memory Systems。Evaluation：https://arxiv.org/html/2607.11487v1#S5 — 5 Quantitative Evaluation; https://arxiv.org/html/2607.11487v1#S5.SS1 — 5.1 Evaluation Setup。Limitations / counterevidence：https://arxiv.org/html/2607.11487v1#S6 — 6 Conclusion; https://arxiv.org/html/2607.11487v1#Sx1 — Limitations。

**Artifact boundary。** Exact v1 links https://github.com/zjunlp/LightMem-Ego, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 显式 agent state 改善恢复与控制，但增加状态陈旧、错误提交、跨轮污染和一致性责任。 论文自身的边界信号是：LightMem-Ego takes a step in this direction by showing how multimodal memory can support AI systems that not only understand utterances, but also understand lived experience.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`AGENT-MEMORY`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-11487:end -->

<!-- review:SF-2026-ARXIV-2607-11498:start -->
### See like a Robot: Robot-Centric Pointmaps for Vision-Language-Action Models

<!-- claim:SF-2026-ARXIV-2607-11498:start -->Vision-language-action (VLA) models predict robot actions from visual observations and language instructions. These actions are defined in the robot's own 3D coordinate frame, yet most VLAs observe the scene in the camera frame, creating a frame mismatch between where the scene is observed and where actions are defined. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-11498:end -->

**为什么进入候选分母。** 摘要首要问题为“Vision-language-action (VLA) models predict robot actions from visual observations and language instructions.”；它提出可跨 workload 讨论的状态、表示或计算机制，并给出旧方案的适用边界。

**机制与状态边界。** These actions are defined in the robot's own 3D coordinate frame, yet most VLAs observe the scene in the camera frame, creating a frame mismatch between where the scene is observed and where actions are defined.

**证据证明什么。** On RoboCasa, pointmaps improve both pi0.5 and SmolVLA and outperform representative camera-viewpoint and 3D-aware baselines.

**证据没有证明什么。** Finally, our camera-variation results focus on changes in camera placement and extrinsics, and do not yet cover changes in the number of cameras or their fields of view, which we leave to future work. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.11498v1#S3 — 3 Method; https://arxiv.org/html/2607.11498v1#S4 — 4 Design Choices for Robot-Centric 3D Observations in VLAs。Evaluation：https://arxiv.org/html/2607.11498v1#A4 — Appendix D RoboCasa Results under Randomized Evaluation Viewpoints; https://arxiv.org/html/2607.11498v1#A2 — Appendix B Implementation Details and Experimental Setup。Limitations / counterevidence：https://arxiv.org/html/2607.11498v1#S6 — 6 Limitations; https://arxiv.org/html/2607.11498v1#S7 — 7 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 新表示或状态机制扩大能力边界，但带来额外训练、状态管理、稳定性或泛化假设。 论文自身的边界信号是：Finally, our camera-variation results focus on changes in camera placement and extrinsics, and do not yet cover changes in the number of cameras or their fields of view, which we leave to future work.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`MULTIMODAL-EMBODIED-VLA`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-11498:end -->

<!-- review:SF-2026-ARXIV-2607-11505:start -->
### Proxy OPD: On-Policy Distillation with Transferable Relative Proxy Update

<!-- claim:SF-2026-ARXIV-2607-11505:start -->Post-training for large language models typically couples policy exploration with model optimization, hindering the reuse of high-reward behaviors from policy exploration. While on-policy distillation alleviates this by consolidating independently optimized experts, its reliance on matching absolute expert distributions can yield suboptimal supervision, especially when the target model possesses a different prior or already surpasses the expert's capabilities. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-11505:end -->

**为什么进入候选分母。** 摘要首要问题为“Post-training for large language models typically couples policy exploration with model optimization, hindering the reuse of high-reward behaviors from policy exploration.”；它改变训练信号、credit、capacity 或 update ownership，而不是只报告单任务精度增量。

**机制与状态边界。** To alleviate this, we introduce Proxy OPD (P-OPD), an asynchronous post-training framework that transfers reward-induced policy improvements rather than absolute policy distributions.

**证据证明什么。** These results establish relative policy updates as highly reusable, adjustable assets for scalable, reward-based post-training.

**证据没有证明什么。** By decoupling the exploration process from the model, update signals can be stored and reused independently. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.11505v1#S3 — 3 Methodology; https://arxiv.org/html/2607.11505v1#A2.SS1 — B.1 Implementation Details。Evaluation：https://arxiv.org/html/2607.11505v1#A2 — Appendix B Experiment Details; https://arxiv.org/html/2607.11505v1#S2 — 2 Preliminary Analysis: Reward Optimization vs. Distribution Matching。Limitations / counterevidence：https://arxiv.org/html/2607.11505v1#S6 — 6 Discussion and Future Works; https://arxiv.org/html/2607.11505v1#S5 — 5 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/KnowledgeXLab/PUST, https://huggingface.co/KnowledgeXLab/PUST-Experiments, https://github.com/open-compass/opencompass; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更密集或更定向的训练信号改善样本效率，但会增加 verifier 偏差、分布迁移和优化耦合。 论文自身的边界信号是：By decoupling the exploration process from the model, update signals can be stored and reused independently.

- Score V2：Design Delta 3 / System Reach 2 / Durability 3 = **8/9**。
- Stable owner 候选：`TRAIN-GRPO`；evidence-stage relation：`alternative_branch`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-11505:end -->

<!-- review:SF-2026-ARXIV-2607-11506:start -->
### SCOPE-RL: Optimizing Reasoning Paths Before and After Success

<!-- claim:SF-2026-ARXIV-2607-11506:start -->Reinforcement learning with verifiable rewards (RLVR) optimizes LLMs using sparse verifiable final-answer rewards. This sparse anchor reliably verifies whether a trajectory succeeds but provides no direct feedback on the reasoning path that produced it. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-11506:end -->

**为什么进入候选分母。** 摘要首要问题为“Reinforcement learning with verifiable rewards (RLVR) optimizes LLMs using sparse verifiable final-answer rewards.”；它改变训练信号、credit、capacity 或 update ownership，而不是只报告单任务精度增量。

**机制与状态边界。** We introduce SCOPE-RL (Scaffolded Chain Optimization with Process Efficiency), a two-stage framework that densifies this anchor while retaining the GRPO update: Adaptive Scaffolded RL adds prefix-decomposed verifiable rewards on answer-hidden sub-question chains before success, and Quality-Aware Process RL applies correctness-gated process-shape rewards to refine correct trajectories after success.

**证据证明什么。** On Qwen3-8B-Instruct trained on DAPO-Math and Big-Math, SCOPE-RL improves average accuracy by up to 11.2 pp and reduces reasoning tokens by up to 27.1% over outcome-only GRPO; the gains hold under GSPO and on Qwen3-0.6B-Instruct, indicating that reward-signal densification is complementary to policy-update-level RLVR advances.

**证据没有证明什么。** Finally, our hyperparameter analysis is limited to a sensitivity sweep for the routing threshold (Appendix K ); broader tuning of , , and remains future work. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.11506v1#S3 — 3 The SCOPE-RL Framework; https://arxiv.org/html/2607.11506v1#A1 — Appendix A Training Algorithm。Evaluation：https://arxiv.org/html/2607.11506v1#A12 — Appendix L ASR Reward-Signal Ablation; https://arxiv.org/html/2607.11506v1#A16 — Appendix P Pairwise Expert Evaluation。Limitations / counterevidence：https://arxiv.org/html/2607.11506v1#S7 — 7 Conclusion; https://arxiv.org/html/2607.11506v1#Sx1 — Limitations。

**Artifact boundary。** Exact v1 links https://github.com/tokencraft-lab/SCOPE-RL, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更密集或更定向的训练信号改善样本效率，但会增加 verifier 偏差、分布迁移和优化耦合。 论文自身的边界信号是：Finally, our hyperparameter analysis is limited to a sensitivity sweep for the routing threshold (Appendix K ); broader tuning of , , and remains future work.

- Score V2：Design Delta 3 / System Reach 2 / Durability 3 = **8/9**。
- Stable owner 候选：`TRAIN-GRPO`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-11506:end -->

<!-- review:SF-2026-ARXIV-2607-11579:start -->
### MemExchange: Utility-Driven Distributed Memory Reallocation for Multi-Tenant Datacenters

<!-- claim:SF-2026-ARXIV-2607-11579:start -->To handle unpredictable workloads, cloud providers typically over-provision memory to meet peak demand, resulting in substantial underutilization across datacenter clusters. At the same time, memory-constrained tenants may suffer elevated cache miss rates, even when idle capacity remains stranded elsewhere in the infrastructure. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-11579:end -->

**为什么进入候选分母。** 摘要首要问题为“To handle unpredictable workloads, cloud providers typically over-provision memory to meet peak demand, resulting in substantial underutilization across datacenter clusters.”；它改变资源分配、迁移、定价或路由的控制权与约束。

**机制与状态边界。** MemExchange is a cluster-wide, multi-tenant memory management system that dynamically right-sizes in-memory caching tenants according to workload demand.

**证据证明什么。** Our results show up to 2.3x lower remote-access overhead compared to TCP-based designs, a 13% increase in cluster-wide memory utilization at rack scale, and up to 63% reduction in miss rate for memory-constrained tenants under skewed workloads.

**证据没有证明什么。** Second, remote pages are not reclaimed once allocated, which simplifies bookkeeping but may limit long-term flexibility under tenant churn. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.11579v1#S4 — 4. MemExchange ’s Design; https://arxiv.org/html/2607.11579v1#S4.SS1 — 4.1. Architecture Overview。Evaluation：https://arxiv.org/html/2607.11579v1#S5 — 5. Evaluation; https://arxiv.org/html/2607.11579v1#S5.SS1 — 5.1. Experimental Setup。Limitations / counterevidence：https://arxiv.org/html/2607.11579v1#S7 — 7. Discussion and Future Work; https://arxiv.org/html/2607.11579v1#S6 — 6. Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/AAMH/memcached, https://github.com/leverich/mutilate, https://github.com/arXiv/html_feedback/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 动态资源控制提高利用率，但增加测量误差、迁移开销、租户公平和控制稳定性问题。 论文自身的边界信号是：Second, remote pages are not reclaimed once allocated, which simplifies bookkeeping but may limit long-term flexibility under tenant churn.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`PLATFORM-GPU-SCHEDULER`；evidence-stage relation：`principle_reuse`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-11579:end -->

<!-- review:SF-2026-ARXIV-2607-11586:start -->
### HCRMap: Pressure-Aware Hot-Expert Residency Mapping for 3.5D MoE Chiplet Inference

<!-- claim:SF-2026-ARXIV-2607-11586:start -->Mixture-of-Experts (MoE) large language models (LLM) activate only a small number of experts during inference, but token routing introduces persistent expert hotness skew: a small set of hot experts continuously receives most tokens, while the remaining experts are lightly loaded. On 3.5D multi-chiplet systems, this skew not only causes compute imbalance but also amplifies pressure on communication, memory bandwidth, I/O, and execution queues. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-11586:end -->

**为什么进入候选分母。** 摘要首要问题为“Mixture-of-Experts (MoE) large language models (LLM) activate only a small number of experts during inference, but token routing introduces persistent expert hotness skew: a small set of hot experts continuously receives most tokens, while the remaining experts are lightly loaded.”；它改变了推理期的状态放置、数据移动、执行控制或 SLO admission，属于长期 runtime 机制。

**机制与状态边界。** This paper proposes HCRMap, a hot expert residency mapping framework for pressure-aware expert replica management in 3.5D MoE inference.

**证据证明什么。** Experimental results show that HCRMap reduces end-to-end latency by 43.6% and 43.0% over Hydra in the prefill and decode stages, respectively; by 34.5% and 33.1% over MoEntwine; and by 46.7% and 46.0% over PIMoE.

**证据没有证明什么。** Exact v1 does not disclose a dedicated generalization or deployment guarantee beyond its stated evaluation scope. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.11586v1#S6 — 6 Method Design; https://arxiv.org/html/2607.11586v1#S4 — 4 System Model。Evaluation：https://arxiv.org/html/2607.11586v1#S7 — 7 Experimental Evaluation; https://arxiv.org/html/2607.11586v1#S7.SS1 — 7.1 Experimental Setup。Limitations / counterevidence：https://arxiv.org/html/2607.11586v1#S8 — 8 Conclusion。

**Artifact boundary。** Exact v1 links https://huggingface.co/Qwen/Qwen1.5-MoE-A2.7B, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更激进的缓存、迁移、并行或专用执行会换取吞吐/时延，同时增加配置依赖、资源压力与回退路径。 论文自身的边界信号是：Exact v1 does not disclose a dedicated generalization or deployment guarantee beyond its stated evaluation scope.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`MODEL-MOE`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-11586:end -->

<!-- review:SF-2026-ARXIV-2607-11598:start -->
### Interaction Scaling: Grounding the Third Axis of Test-Time Compute

<!-- claim:SF-2026-ARXIV-2607-11598:start -->There are two standard ways to spend more compute at test time: let a model reason longer, or sample more attempts and keep one. Both share a hidden limit: they are internal. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-11598:end -->

**为什么进入候选分母。** 摘要首要问题为“There are two standard ways to spend more compute at test time: let a model reason longer, or sample more attempts and keep one.”；它改变了 evaluation observable、对照组、判定粒度或结果解释边界，可能修正现有评测结论。

**机制与状态边界。** The loop alternates proposal, external instrument observation and revision; each cycle imports a new grounded observation, and the outcome metric must observe the same failure surface for improvement to be visible.

**证据证明什么。** A tool that measures the real layout instead shows the loop removing 40-74% of defects across four modalities; and that same VLM, used as the reviewer, makes slide layouts worse where the measuring tool repairs them.

**证据没有证明什么。** 9 Limitations Two modalities saturate: video editing is already strong single-shot (the lift is real only on a hardened multi-step suite), and deep research saturates because frontier models know well-documented facts and the judge cannot grade facts it does not have. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.11598v1#S2 — 2 A Framework for Internal and External Test-Time Compute; https://arxiv.org/html/2607.11598v1#A2.SS6 — B.6 Cross-model replication (code)。Evaluation：https://arxiv.org/html/2607.11598v1#A2 — Appendix B Detailed Results and Configurations; https://arxiv.org/html/2607.11598v1#S6 — 6 Evaluation-Side Grounding: Deterministic Instruments vs. Model Judges。Limitations / counterevidence：https://arxiv.org/html/2607.11598v1#S10 — 10 Conclusion; https://arxiv.org/html/2607.11598v1#S9 — 9 Limitations。

**Artifact boundary。** Exact v1 links https://github.com/19PINE-AI/interaction-scaling, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：9 Limitations Two modalities saturate: video editing is already strong single-shot (the lift is real only on a hardened multi-step suite), and deep research saturates because frontier models know well-documented facts and the judge cannot grade facts it does not have.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`AGENT-WORKFLOW`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-11598:end -->

<!-- review:SF-2026-ARXIV-2607-11611:start -->
### Mizzle: A Complete Concurrent Incorrectness Logic for Preventing False Alarms in Agentic Bug Finding

<!-- claim:SF-2026-ARXIV-2607-11611:start -->Large language models are increasingly used to find bugs in real-world programs, but they also produce a flood of false alarms that waste developers' time. We propose a method to prevent these false alarms by requiring an LLM to accompany each bug report with a machine-checked proof, in a program logic, that the reported bug is real. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-11611:end -->

**为什么进入候选分母。** 摘要首要问题为“Large language models are increasingly used to find bugs in real-world programs, but they also produce a flood of false alarms that waste developers' time.”；它揭示局部安全检查或现有 guard 的边界，并提出可验证的新控制点。

**机制与状态边界。** An LLM-generated bug report is accepted only when accompanied by a machine-checkable program-logic proof; the Mizzle checker becomes the authority for the reported defect rather than the model's prose.

**证据证明什么。** The authors mechanize the relevant soundness and completeness properties in Rocq and show a proof-of-concept LLM certification flow; they do not establish coverage or cost on large production codebases.

**证据没有证明什么。** For future work, we would like to extend the proof of concept we present in this paper to a full-fledged tool. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.11611v1#S5.SS1 — 5.1. Methodology; https://arxiv.org/html/2607.11611v1#S2.SS2 — 2.2. ZooLang as a Model of OCaml 5。Evaluation：https://arxiv.org/html/2607.11611v1#S1 — 1. Introduction; https://arxiv.org/html/2607.11611v1#S2 — 2. Key Ideas。Limitations / counterevidence：https://arxiv.org/html/2607.11611v1#S7 — 7. Discussion and Future Work。

**Artifact boundary。** Exact v1 links https://code.facebook.com/posts/1648953042007882/open-sourcing-facebook-infer-identify-bugs-before-you-ship/, https://github.com/ocaml-multicore/domainslib, https://github.com/LLM4Rocq/rocq-mcp; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 新的安全控制点降低特定失败，但会引入误拒绝、旁路、观测不足或模型/任务迁移问题。 论文自身的边界信号是：For future work, we would like to extend the proof of concept we present in this paper to a full-fledged tool.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`AGENT-TOOL-CALLING`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-11611:end -->

<!-- review:SF-2026-ARXIV-2607-11614:start -->
### Extending LLM Context via Associative Recurrent Memory

<!-- claim:SF-2026-ARXIV-2607-11614:start -->Extending the context length of large language models (LLMs) is critical for many real-world applications, yet standard transformers remain constrained by quadratic compute and linear memory scaling. In this work, we investigate the Associative Recurrent Memory Transformer (ARMT) as a practical approach for enabling long-context processing in LLMs, constant memory scaling, and better efficiency. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-11614:end -->

**为什么进入候选分母。** 摘要首要问题为“Extending the context length of large language models (LLMs) is critical for many real-world applications, yet standard transformers remain constrained by quadratic compute and linear memory scaling.”；它提出可跨 workload 讨论的状态、表示或计算机制，并给出旧方案的适用边界。

**机制与状态边界。** Second, we propose a comprehensive training recipe for ARMT-based context extension, combining continued pre-training, synthetic long-context data generation, curriculum learning, and selective integration of associative memory into chosen model layers.

**证据证明什么。** Third, we present an extensive experimental study demonstrating that ARMT-augmented models: (i) process inputs well beyond their original context limits without degrading performance relative to in-limit baselines; (ii) generalize more effectively to out-of-distribution context lengths; and (iii) need 30% less FLOPs while preserving baseline performance within the original context window.

**证据没有证明什么。** Limitations We experimented only with relatively small LLMs (up to 1B parameters) due to the chosen scope of the paper and computational constraints. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.11614v1#A1 — Appendix A Formal Description of the ARMT Architecture; https://arxiv.org/html/2607.11614v1#A4.SS1 — D.1 ARMT language modeling pre-training。Evaluation：https://arxiv.org/html/2607.11614v1#A4 — Appendix D Additional Experimental Results; https://arxiv.org/html/2607.11614v1#A1.SS1 — A.1 FLOP Analysis。Limitations / counterevidence：https://arxiv.org/html/2607.11614v1#S6 — 6 Conclusion; https://arxiv.org/html/2607.11614v1#Sx1 — Limitations。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 新表示或状态机制扩大能力边界，但带来额外训练、状态管理、稳定性或泛化假设。 论文自身的边界信号是：Limitations We experimented only with relatively small LLMs (up to 1B parameters) due to the chosen scope of the paper and computational constraints.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`MODEL-LONG-CONTEXT`；evidence-stage relation：`alternative_branch`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-11614:end -->

<!-- review:SF-2026-ARXIV-2607-11643:start -->
### Xiaomi-Robotics-U0: Unified Embodied Synthesis with World Foundation Model

<!-- claim:SF-2026-ARXIV-2607-11643:start -->Recent foundation image and video generation models offer strong generalization and controllability, but their direct application to embodied scenarios is limited by requirements for multi-view consistency, geometric coherence, and robot embodiment constraints. Existing methods typically adapt foundation models with limited robot data, often sacrificing visual knowledge acquired during large-scale pre-training. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-11643:end -->

**为什么进入候选分母。** 摘要首要问题为“Recent foundation image and video generation models offer strong generalization and controllability, but their direct application to embodied scenarios is limited by requirements for multi-view consistency, geometric coherence, and robot embodiment constraints.”；它提出可跨 workload 讨论的状态、表示或计算机制，并给出旧方案的适用边界。

**机制与状态边界。** We present Xiaomi-Robotics-U0, a 38-billion-parameter multimodal autoregressive model for unified embodied synthesis.

**证据证明什么。** It achieves state-of-the-art results on single-step and sequential generation tasks, outperforming GPT-Image-2.0 in human evaluations of embodied scene generation and transfer, ranking first on World Arena for embodied video generation, and improving the out-of-distribution success rate of pi_0.5 from 36.9% to 63.2% on challenging real-world manipulation tasks.

**证据没有证明什么。** Despite the promising results, Xiaomi-Robotics-U0 has several limitations. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.11643v1#S2.SS2 — 2.2 Model Architecture; https://arxiv.org/html/2607.11643v1#S4.SS1 — 4.1 Foundation Generative Models and Embodied World Models。Evaluation：https://arxiv.org/html/2607.11643v1#S3 — 3 Experiments; https://arxiv.org/html/2607.11643v1#S3.SS3 — 3.3 Real World Experiments。Limitations / counterevidence：https://arxiv.org/html/2607.11643v1#S5 — 5 Conclusions。

**Artifact boundary。** Exact v1 links https://github.com/kakaobrain/coyo-dataset, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 新表示或状态机制扩大能力边界，但带来额外训练、状态管理、稳定性或泛化假设。 论文自身的边界信号是：Despite the promising results, Xiaomi-Robotics-U0 has several limitations.

- Score V2：Design Delta 2 / System Reach 2 / Durability 3 = **7/9**。
- Stable owner 候选：`MULTIMODAL-WORLD-MODELS`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-11643:end -->

<!-- review:SF-2026-ARXIV-2607-11673:start -->
### ABot-3DWorld 0: A Universal World Model to Explore Any 3D Space

<!-- claim:SF-2026-ARXIV-2607-11673:start -->We present ABot-3DWorld 0, a universal multimodal 3D world model that turns text, image, and video inputs into high-fidelity, explorable 3D worlds. At the heart of our framework is a unified Spatial Generative Primitive (SGP), a compact tuple of a high-quality panorama and a spatial point cloud that delivers an efficient description of any 3D space. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-11673:end -->

**为什么进入候选分母。** 摘要首要问题为“We present ABot-3DWorld 0, a universal multimodal 3D world model that turns text, image, and video inputs into high-fidelity, explorable 3D worlds.”；它提出可跨 workload 讨论的状态、表示或计算机制，并给出旧方案的适用边界。

**机制与状态边界。** We present ABot-3DWorld 0, a universal multimodal 3D world model that turns text, image, and video inputs into high-fidelity, explorable 3D worlds.

**证据证明什么。** Experiments show that ABot-3DWorld 0 sets the state of the art among open-source methods and demonstrates stronger scene fidelity than Marble under rich multimodal inputs.

**证据没有证明什么。** Exact v1 does not disclose a dedicated generalization or deployment guarantee beyond its stated evaluation scope. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.11673v1#S3 — 3 Method; https://arxiv.org/html/2607.11673v1#S3.SS3 — 3.3 Exploration Trajectory Design。Evaluation：https://arxiv.org/html/2607.11673v1#S4 — 4 Evaluation。Limitations / counterevidence：https://arxiv.org/html/2607.11673v1#S5 — 5 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/ali-vilab/VACE, https://huggingface.co/datasets/spatialverse/InteriorGS, https://github.com/ModelTC/lightx2v; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 新表示或状态机制扩大能力边界，但带来额外训练、状态管理、稳定性或泛化假设。 论文自身的边界信号是：Exact v1 does not disclose a dedicated generalization or deployment guarantee beyond its stated evaluation scope.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`MULTIMODAL-WORLD-MODELS`；evidence-stage relation：`alternative_branch`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-11673:end -->

<!-- review:SF-2026-ARXIV-2607-11698:start -->
### Agent Hacks Agent: Autoresearch for Production-Agent Red-Teaming

<!-- claim:SF-2026-ARXIV-2607-11698:start -->Production LLM agents such as Claude Code and Codex operate over untrusted content, files, commands, and workspace state, making safety failures directly actionable. Red-teaming must therefore keep pace with evolving models and tools. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-11698:end -->

**为什么进入候选分母。** 摘要首要问题为“Production LLM agents such as Claude Code and Codex operate over untrusted content, files, commands, and workspace state, making safety failures directly actionable.”；它揭示局部安全检查或现有 guard 的边界，并提出可验证的新控制点。

**机制与状态边界。** We present AHA, a falsifiable discovery loop that proposes a vulnerability hypothesis, constructs a falsifier, instantiates a valid attack, executes it in a sandboxed harness, reflects on the trajectory, and promotes confirmed findings into a Vulnerability Concept Graph (VCG).

**证据证明什么。** Across the disclosed agents and attack scenarios, a frozen vulnerability concept graph transferred better than the frozen discovery baseline under the same single-shot protocol; this supports reusable causal vulnerability records, not exhaustive security coverage.

**证据没有证明什么。** Exact v1 does not disclose a dedicated generalization or deployment guarantee beyond its stated evaluation scope. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.11698v1#A1 — Appendix A AHA main framework; https://arxiv.org/html/2607.11698v1#S3 — 3 Method。Evaluation：https://arxiv.org/html/2607.11698v1#A1.SS2 — A.2 Held-out concept evaluation; https://arxiv.org/html/2607.11698v1#A2 — Appendix B Experiment details。Limitations / counterevidence：https://arxiv.org/html/2607.11698v1#S6 — 6 Discussion; https://arxiv.org/html/2607.11698v1#S7 — 7 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/henrymao2004/Auto-research-red-teaming, https://docs.anthropic.com/en/docs/claude-code/overview, https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro/; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 新的安全控制点降低特定失败，但会引入误拒绝、旁路、观测不足或模型/任务迁移问题。 论文自身的边界信号是：Exact v1 does not disclose a dedicated generalization or deployment guarantee beyond its stated evaluation scope.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`PLATFORM-SECURITY`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-11698:end -->

<!-- review:SF-2026-ARXIV-2607-11738:start -->
### Qwen-Audio-VAE Technical Report

<!-- claim:SF-2026-ARXIV-2607-11738:start -->We introduce \textbf{Qwen-Audio-VAE}, a suite of low-bitrate, fast-encoding continuous audio autoencoders designed for scalable general audio generation. The model is built around a simple but important principle: an audio VAE should not only reconstruct diverse audio with high fidelity, but also produce compact latent representations fast enough to support large-scale text-to-audio training. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-11738:end -->

**为什么进入候选分母。** 摘要首要问题为“We introduce \textbf{Qwen-Audio-VAE}, a suite of low-bitrate, fast-encoding continuous audio autoencoders designed for scalable general audio generation.”；它提出可跨 workload 讨论的状态、表示或计算机制，并给出旧方案的适用边界。

**机制与状态边界。** We introduce \textbf{Qwen-Audio-VAE}, a suite of low-bitrate, fast-encoding continuous audio autoencoders designed for scalable general audio generation.

**证据证明什么。** To further improve computational efficiency, we adopt an asymmetric encoder-decoder backbone and introduce latency-aware encoder pruning to maximize encoding throughput.

**证据没有证明什么。** More broadly, our results suggest that autoencoders for general audio generation should be optimized not for reconstruction alone, but jointly for compression, encoding throughput, data scalability, and latent learnability. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.11738v1#S2 — 2 Architecture; https://arxiv.org/html/2607.11738v1#S2.SS2 — 2.2 Model Components。Evaluation：https://arxiv.org/html/2607.11738v1#S4.SS2 — 4.2 Evaluation on Public Benchmarks; https://arxiv.org/html/2607.11738v1#S4 — 4 Evaluation。Limitations / counterevidence：https://arxiv.org/html/2607.11738v1#S5 — 5 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 新表示或状态机制扩大能力边界，但带来额外训练、状态管理、稳定性或泛化假设。 论文自身的边界信号是：More broadly, our results suggest that autoencoders for general audio generation should be optimized not for reconstruction alone, but jointly for compression, encoding throughput, data scalability, and latent learnability.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`MULTIMODAL-REPRESENTATION`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-11738:end -->

<!-- review:SF-2026-ARXIV-2607-11746:start -->
### HiFi-LLP: High-Fidelity, Low-Cost Latency Predictors with Confidence for Robust HW-NAS

<!-- claim:SF-2026-ARXIV-2607-11746:start -->With deep neural networks (DNNs) increasingly deployed on edge devices, hardware (HW)-aware optimization techniques--such as HW-aware compression and HW-aware neural architecture search (HW-NAS)--have become essential. These methods rely on real feedback from the target hardware to tailor DNN architectures for efficient deployment. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-11746:end -->

**为什么进入候选分母。** 摘要首要问题为“With deep neural networks (DNNs) increasingly deployed on edge devices, hardware (HW)-aware optimization techniques--such as HW-aware compression and HW-aware neural architecture search (HW-NAS)--have become essential.”；它改变了 evaluation observable、对照组、判定粒度或结果解释边界，可能修正现有评测结论。

**机制与状态边界。** These methods rely on real feedback from the target hardware to tailor DNN architectures for efficient deployment.

**证据证明什么。** HiFi-LLP outperforms prior platform-specific predictors by up to 9 percentage points (p.p.) in the 10% accuracy bound and achieves a Spearman's rank correlation of up to 0.996 across six devices in the LatBench dataset.

**证据没有证明什么。** VI Conclusion This paper presents HiFi-LLP, a novel platform-specific latency predictor that excels with minimal training data, requiring only 100 samples to deliver predictions with a confidence score. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.11746v1#S4 — IV HiFi-LLP Design; https://arxiv.org/html/2607.11746v1#S4.SS2 — IV-B Design Decisions。Evaluation：https://arxiv.org/html/2607.11746v1#S4.SS1 — IV-A Evaluation Metrics; https://arxiv.org/html/2607.11746v1#S5 — V Evaluation。Limitations / counterevidence：https://arxiv.org/html/2607.11746v1#S6 — VI Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：VI Conclusion This paper presents HiFi-LLP, a novel platform-specific latency predictor that excels with minimal training data, requiring only 100 samples to deliver predictions with a confidence score.

- Score V2：Design Delta 2 / System Reach 2 / Durability 1 = **5/9**。
- Stable owner 候选：`INFER-TENSORRT-LLM`；evidence-stage relation：`principle_reuse`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-11746:end -->

<!-- review:SF-2026-ARXIV-2607-11751:start -->
### When Local Monitors Miss Compositional Harm: Diagnosing Distributed Backdoors in Multi-Agent Systems

<!-- claim:SF-2026-ARXIV-2607-11751:start -->As multi-agent, tool-using LLM systems are deployed, a common safety net is a runtime monitor that checks each message, tool call, or step on its own. A distributed backdoor splits a harmful payload across agents, so every local check passes while the assembled object is the attack. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-11751:end -->

**为什么进入候选分母。** 摘要首要问题为“As multi-agent, tool-using LLM systems are deployed, a common safety net is a runtime monitor that checks each message, tool call, or step on its own.”；它揭示局部安全检查或现有 guard 的边界，并提出可验证的新控制点。

**机制与状态边界。** As multi-agent, tool-using LLM systems are deployed, a common safety net is a runtime monitor that checks each message, tool call, or step on its own.

**证据证明什么。** The experiments and formal observability argument agree that locally benign fragments defeat monitors restricted to local views, while signal returns only at a representation exposing the assembled payload.

**证据没有证明什么。** What defeats a local monitor is not splitting but the loss of usable evidence, and detection returns only when the monitor changes what it observes, recovering the assembled code structure from benign data alone, then reading the decoded program to block the attack outright. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.11751v1#A5.SS1 — E.1 Full per-model ASR。Evaluation：https://arxiv.org/html/2607.11751v1#A2 — Appendix B Experimental details and statistics。Limitations / counterevidence：https://arxiv.org/html/2607.11751v1#S7 — 7 Discussion and conclusion。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 新的安全控制点降低特定失败，但会引入误拒绝、旁路、观测不足或模型/任务迁移问题。 论文自身的边界信号是：What defeats a local monitor is not splitting but the loss of usable evidence, and detection returns only when the monitor changes what it observes, recovering the assembled code structure from benign data alone, then reading the decoded program to block the attack outright.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`PLATFORM-SECURITY`；evidence-stage relation：`corrective_evidence`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-11751:end -->

<!-- review:SF-2026-ARXIV-2607-11796:start -->
### An Exact Instrument for State Usage in Selective State-Space Models, and the Input-Driven Migration It Reveals

<!-- claim:SF-2026-ARXIV-2607-11796:start -->Selective state-space models such as Mamba route information through a bank of first-order modes whose input coupling is set by a learned selection mechanism. We give an exact instrument for measuring how a trained model uses these modes. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-11796:end -->

**为什么进入候选分母。** 摘要首要问题为“Selective state-space models such as Mamba route information through a bank of first-order modes whose input coupling is set by a learned selection mechanism.”；它提出可跨 workload 讨论的状态、表示或计算机制，并给出旧方案的适用边界。

**机制与状态边界。** Diagonal state dynamics permit an exact per-mode output decomposition; a per-layer, per-channel, per-window Gram tensor measures the exact error of dropping any mode subset and reveals input-driven state-use migration.

**证据证明什么。** Because the scheduler reads each window's mode usage from a first pass, this demonstrates realizable headroom; we claim no deployed compute or memory saving.

**证据没有证明什么。** 5 Limitations The instrument is exact only for the per-channel diagonal case. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.11796v1#S1 — 1 Introduction; https://arxiv.org/html/2607.11796v1#S2 — 2 Related Work。Evaluation：https://arxiv.org/html/2607.11796v1#S1 — 1 Introduction; https://arxiv.org/html/2607.11796v1#S2 — 2 Related Work。Limitations / counterevidence：https://arxiv.org/html/2607.11796v1#S5 — 5 Limitations; https://arxiv.org/html/2607.11796v1#S6 — 6 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/isrlab/selective-layer-audit, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 新表示或状态机制扩大能力边界，但带来额外训练、状态管理、稳定性或泛化假设。 论文自身的边界信号是：5 Limitations The instrument is exact only for the per-channel diagonal case.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`MODEL-LONG-CONTEXT`；evidence-stage relation：`corrective_evidence`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-11796:end -->

<!-- review:SF-2026-ARXIV-2607-11818:start -->
### MM-ToolSandBox: A Unified Framework for Evaluating Visual Tool-Calling Agents

<!-- claim:SF-2026-ARXIV-2607-11818:start -->We introduce MM-ToolSandBox, a benchmark and evaluation framework for visually grounded tool-calling agents. The framework provides a stateful execution environment spanning 500+ tools across 16 application domains, supporting multi-image, multi-turn tasks where agents must ground progressively arriving visual inputs into executable tool calls while handling realistic conversational phenomena (goal revisions, error corrections, state mutations). 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-11818:end -->

**为什么进入候选分母。** 摘要首要问题为“We introduce MM-ToolSandBox, a benchmark and evaluation framework for visually grounded tool-calling agents.”；它改变了 evaluation observable、对照组、判定粒度或结果解释边界，可能修正现有评测结论。

**机制与状态边界。** We introduce MM-ToolSandBox, a benchmark and evaluation framework for visually grounded tool-calling agents.

**证据证明什么。** Evaluating 12 state-of-the-art models, from 4B open-weight to frontier proprietary systems, shows that current models still lack robust visual tool-calling capability: even the best model achieves below 50% success rate.

**证据没有证明什么。** A scenario passes only if all five criteria pass. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.11818v1#A3.SS1 — C.1 Study Design; https://arxiv.org/html/2607.11818v1#S3.SS1 — 3.1 Architecture。Evaluation：https://arxiv.org/html/2607.11818v1#A2 — Appendix B Benchmarking Results without Failed User Simulators; https://arxiv.org/html/2607.11818v1#A1 — Appendix A Evaluation Protocol Details。Limitations / counterevidence：https://arxiv.org/html/2607.11818v1#S6.SS4 — 6.4 Failure Analysis; https://arxiv.org/html/2607.11818v1#S7 — 7 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/apple/ml-mmtoolsandbox, https://developers.googleblog.com/introducing-a2ui-an-open-project-for-agent-driven-interfaces/, https://github.com/arXiv/html_feedback/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：A scenario passes only if all five criteria pass.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`PLATFORM-EVALUATION-SYSTEM`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-11818:end -->

<!-- review:SF-2026-ARXIV-2607-11836:start -->
### Cycle-World: Mitigating Error Accumulation in Long-term Video World Models via Reverse-Prediction Cycle Consistency

<!-- claim:SF-2026-ARXIV-2607-11836:start -->Autoregressive diffusion models have enabled high-quality video generation, yet their sequential nature inherently suffers from error accumulation. In long-horizon video synthesis, minor prediction deviations compound over time, inevitably leading to unconstrained generative drift, structural collapse, and severe visual degradation. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-11836:end -->

**为什么进入候选分母。** 摘要首要问题为“Autoregressive diffusion models have enabled high-quality video generation, yet their sequential nature inherently suffers from error accumulation.”；它提出可跨 workload 讨论的状态、表示或计算机制，并给出旧方案的适用边界。

**机制与状态边界。** To address this, we propose Cycle-World, a novel framework designed for stable and temporally consistent long-video generation.

**证据证明什么。** Theoretically, we demonstrate that forward generative drift can be strictly bottlenecked by a cycle-consistency objective.

**证据没有证明什么。** Exact v1 does not disclose a dedicated generalization or deployment guarantee beyond its stated evaluation scope. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.11836v1#S3 — 3 Methodology; https://arxiv.org/html/2607.11836v1#Pt0.A3 — Appendix 0.C Algorithm for Cycle-Guided Inference。Evaluation：https://arxiv.org/html/2607.11836v1#Pt0.A5 — Appendix 0.E Physical Consistency Evaluation Metrics; https://arxiv.org/html/2607.11836v1#Pt0.A6 — Appendix 0.F Extended Evaluation on Physical Consistency。Limitations / counterevidence：https://arxiv.org/html/2607.11836v1#S5 — 5 Conclusion。

**Artifact boundary。** Exact v1 links https://szhcz.github.io/projects/Cycle-World/, https://github.com/SkyworkAI/Matrix-Game/blob/main/Matrix-Game-3/assets/pdf/report.pdf, https://github.com/arXiv/html_feedback/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 新表示或状态机制扩大能力边界，但带来额外训练、状态管理、稳定性或泛化假设。 论文自身的边界信号是：Exact v1 does not disclose a dedicated generalization or deployment guarantee beyond its stated evaluation scope.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`MULTIMODAL-WORLD-MODELS`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-11836:end -->

<!-- review:SF-2026-ARXIV-2607-11862:start -->
### Evidence-Backed Video Question Answering

<!-- claim:SF-2026-ARXIV-2607-11862:start -->Current Video Large Language Models (Video LLMs) excel in question answering (QA) but largely operate as black boxes, providing textual answers without verifiable visual grounding. Existing explainability efforts rely on textual rationales or sparse bounding boxes, which struggle to capture complex video dynamics such as occlusions and non-rigid deformations. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-11862:end -->

**为什么进入候选分母。** 摘要首要问题为“Current Video Large Language Models (Video LLMs) excel in question answering (QA) but largely operate as black boxes, providing textual answers without verifiable visual grounding.”；它改变了 evaluation observable、对照组、判定粒度或结果解释边界，可能修正现有评测结论。

**机制与状态边界。** ST-Evidence pairs human-verified pixel evidence with discriminative and generative grounding tasks, then fine-tunes a size-matched model so evidence localization is evaluated independently of answer-only accuracy.

**证据证明什么。** Under the disclosed benchmark and baseline, fine-tuning improves t-mean by 27.2 points and J&F by 13.8 points; this does not establish transfer to unseen evidence taxonomies or production images.

**证据没有证明什么。** Exact v1 does not disclose a dedicated generalization or deployment guarantee beyond its stated evaluation scope. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.11862v1#S3.SS1 — 3.1 Benchmark Design: ST-Evidence; https://arxiv.org/html/2607.11862v1#S5.SS3 — 5.3 A Baseline Model for the E-VQA Task。Evaluation：https://arxiv.org/html/2607.11862v1#S5.SS2 — 5.2 Experimental Results on ST-Evidence; https://arxiv.org/html/2607.11862v1#S3.SS1 — 3.1 Benchmark Design: ST-Evidence。Limitations / counterevidence：https://arxiv.org/html/2607.11862v1#S6 — 6 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/SalesforceAIResearch/EVQA, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：Exact v1 does not disclose a dedicated generalization or deployment guarantee beyond its stated evaluation scope.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`PLATFORM-EVALUATION-SYSTEM`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-11862:end -->

<!-- review:SF-2026-ARXIV-2607-11871:start -->
### Inside the Unfair Judge: A Mechanistic Interpretability Account of LLM-as-Judge Bias

<!-- claim:SF-2026-ARXIV-2607-11871:start -->Existing studies of LLM-as-judge scoring bias work predominantly at the input-output level: they perturb inputs, measure score deltas, and propose prompt-level mitigations. We argue that the same biases admit a representation-level account in the judge's hidden state, complementary to the input-output view and operationally useful in ways it does not afford. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-11871:end -->

**为什么进入候选分母。** 摘要首要问题为“Existing studies of LLM-as-judge scoring bias work predominantly at the input-output level: they perturb inputs, measure score deltas, and propose prompt-level mitigations.”；它改变了 evaluation observable、对照组、判定粒度或结果解释边界，可能修正现有评测结论。

**机制与状态边界。** Reading bias as activation geometry, rather than as input-output noise, unifies geometric structure, causal control, and operational prediction within a single framework.

**证据证明什么。** Operational: a simple linear projection onto the same bias-direction features anticipates judge failures on three entirely unseen benchmarks, substantially outperforming text-based alternatives.

**证据没有证明什么。** This case-control framing is intrinsic to the phenomenon: if a surface cue does not move the judge’s score, there is no scoring failure to attribute to a hidden-state direction. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.11871v1#A1.SS3 — A.3 Detailed Comparison to the Closest Methods; https://arxiv.org/html/2607.11871v1#A10.SS6 — J.6 Per-Layer, Per-Method Attack Tables。Evaluation：https://arxiv.org/html/2607.11871v1#A10 — Appendix J Complete Attack Results; https://arxiv.org/html/2607.11871v1#A11 — Appendix K Defense Results。Limitations / counterevidence：https://arxiv.org/html/2607.11871v1#A7.SS1 — G.1 Error Analysis: Generation Failures and Score Parsing; https://arxiv.org/html/2607.11871v1#A8 — Appendix H Limitations and Scope。

**Artifact boundary。** Exact v1 links https://huggingface.co/meta-llama/Llama-3.1-8B, https://huggingface.co/meta-llama/Llama-3.3-70B-Instruct, https://huggingface.co/Qwen/Qwen2.5-72B; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：This case-control framing is intrinsic to the phenomenon: if a surface cue does not move the judge’s score, there is no scoring failure to attribute to a hidden-state direction.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`PLATFORM-EVALUATION-SYSTEM`；evidence-stage relation：`corrective_evidence`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-11871:end -->

<!-- review:SF-2026-ARXIV-2607-11883:start -->
### Requential Coding: Pushing the Limits of Model Compression with Self-Generated Training Data

<!-- claim:SF-2026-ARXIV-2607-11883:start -->A model that can represent its training data as a short code has discovered regularities that enable generalization. Large neural networks may learn functions far simpler than their parameter counts suggest, but it is challenging to construct codes that realize this simplicity. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-11883:end -->

**为什么进入候选分母。** 摘要首要问题为“Compression is fundamental to intelligence.”；它提出可跨 workload 讨论的状态、表示或计算机制，并给出旧方案的适用边界。

**机制与状态边界。** We introduce requential coding, where a teacher model selects training samples drawn from the student's own distribution.

**证据证明什么。** Plugged into a PAC-Bayes bound, the requential code yields state-of-the-art generalization guarantees for billion-parameter LLMs, outperforming bounds built on aggressive post-training quantization even granted zero error.

**证据没有证明什么。** Conceptually, requential coding provides a lossless code for the student, not the teacher. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.11883v1#S3.SS1 — 3.1 Method; https://arxiv.org/html/2607.11883v1#A3.SS5 — C.5 Model Size Scaling at Fixed Data (Figure 5 )。Evaluation：https://arxiv.org/html/2607.11883v1#A3 — Appendix C Experiment Details; https://arxiv.org/html/2607.11883v1#S3.SS2 — 3.2 Benchmarking Compression of Transformers Trained on Text and Images。Limitations / counterevidence：https://arxiv.org/html/2607.11883v1#S5 — 5 Discussion。

**Artifact boundary。** Exact v1 links https://github.com/shikaiqiu/requential-coding, https://huggingface.co/datasets/Skylion007/openwebtext, https://github.com/preetum/cifar5m; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 新表示或状态机制扩大能力边界，但带来额外训练、状态管理、稳定性或泛化假设。 论文自身的边界信号是：Conceptually, requential coding provides a lossless code for the student, not the teacher.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`WORLDVIEW-WHY-MODELS-LEARN`；evidence-stage relation：`explanatory_analogy`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-11883:end -->

<!-- review:SF-2026-ARXIV-2607-11886:start -->
### Read It Back: Pretrained MLLMs Are Zero-Shot Reward Models for Text-to-Image Generation

<!-- claim:SF-2026-ARXIV-2607-11886:start -->In this paper, we propose SpectraReward, a training-free reward function that turns pretrained MLLMs into off-the-shelf reward models for image-generation reinforcement learning. Instead of asking the MLLM to judge a generated image or answer decomposed verification questions, SpectraReward measures how well the original prompt can be recovered from the generated image through a single image-conditioned, teacher-forced forward pass. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-11886:end -->

**为什么进入候选分母。** 摘要首要问题为“In this paper, we propose SpectraReward, a training-free reward function that turns pretrained MLLMs into off-the-shelf reward models for image-generation reinforcement learning.”；它改变训练信号、credit、capacity 或 update ownership，而不是只报告单任务精度增量。

**机制与状态边界。** The reward is the image-conditioned likelihood of reconstructing the original prompt, reusing a pretrained multimodal understanding branch as a training-free image-generation reward model.

**证据证明什么。** Results show that both SpectraReward and Self-SpectraReward significantly and consistently improve generation performance and outperform prior MLLM-derived reward training methods.

**证据没有证明什么。** Since the likelihood is computed only over the input prompt, the reward mainly captures explicit semantic alignment between generated images and prompts, and may under-emphasize implicit visual implications that are not directly expressed in the text. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.11886v1#S3 — 3 Method; https://arxiv.org/html/2607.11886v1#A2 — Appendix B Additional Implementation Details。Evaluation：https://arxiv.org/html/2607.11886v1#A3 — Appendix C Additional Experimental Results; https://arxiv.org/html/2607.11886v1#A4 — Appendix D Detailed Benchmark Results。Limitations / counterevidence：https://arxiv.org/html/2607.11886v1#A1 — Appendix A Limitations and future work; https://arxiv.org/html/2607.11886v1#S5 — 5 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/black-forest-labs/flux, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更密集或更定向的训练信号改善样本效率，但会增加 verifier 偏差、分布迁移和优化耦合。 论文自身的边界信号是：Since the likelihood is computed only over the input prompt, the reward mainly captures explicit semantic alignment between generated images and prompts, and may under-emphasize implicit visual implications that are not directly expressed in the text.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`MULTIMODAL-GENERATIVE-PARADIGMS`；evidence-stage relation：`alternative_branch`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-11886:end -->

## 4. Benchmark Contracts

None。本报告不转录可跨配置复用的性能主张；数值只留在各 Source Review 的 exact-v1 evaluation contract 内，因此 Ledger 的 `Benchmark Claim` 均为 `no`。

## 5. Deep Analysis Selection

<!-- validator:deep-analysis-selection-v1 -->
| Source Family ID | Eligibility | Decision | Analysis Unit ID | Subsumed By | Priority Rationale | Narrative Ref |
| --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2607-09665 | score_7_9 | not_selected | — | — | V2=9/9；完整证据保留，但相对三条入选主轴更局部，或主要承担评测/反证边界。 | analysis-decision:SF-2026-ARXIV-2607-09665 |
| SF-2026-ARXIV-2607-09682 | score_7_9 | not_selected | — | — | V2=9/9；完整证据保留，但相对三条入选主轴更局部，或主要承担评测/反证边界。 | analysis-decision:SF-2026-ARXIV-2607-09682 |
| SF-2026-ARXIV-2607-09686 | score_7_9 | not_selected | — | — | V2=9/9；完整证据保留，但相对三条入选主轴更局部，或主要承担评测/反证边界。 | analysis-decision:SF-2026-ARXIV-2607-09686 |
| SF-2026-ARXIV-2607-09689 | score_7_9 | not_selected | — | — | V2=9/9；完整证据保留，但相对三条入选主轴更局部，或主要承担评测/反证边界。 | analysis-decision:SF-2026-ARXIV-2607-09689 |
| SF-2026-ARXIV-2607-09697 | score_7_9 | not_selected | — | — | V2=9/9；完整证据保留，但相对三条入选主轴更局部，或主要承担评测/反证边界。 | analysis-decision:SF-2026-ARXIV-2607-09697 |
| SF-2026-ARXIV-2607-09709 | score_7_9 | not_selected | — | — | V2=9/9；完整证据保留，但相对三条入选主轴更局部，或主要承担评测/反证边界。 | analysis-decision:SF-2026-ARXIV-2607-09709 |
| SF-2026-ARXIV-2607-09744 | score_7_9 | not_selected | — | — | V2=9/9；完整证据保留，但相对三条入选主轴更局部，或主要承担评测/反证边界。 | analysis-decision:SF-2026-ARXIV-2607-09744 |
| SF-2026-ARXIV-2607-09748 | score_7_9 | not_selected | — | — | V2=9/9；完整证据保留，但相对三条入选主轴更局部，或主要承担评测/反证边界。 | analysis-decision:SF-2026-ARXIV-2607-09748 |
| SF-2026-ARXIV-2607-09759 | score_7_9 | not_selected | — | — | V2=9/9；完整证据保留，但相对三条入选主轴更局部，或主要承担评测/反证边界。 | analysis-decision:SF-2026-ARXIV-2607-09759 |
| SF-2026-ARXIV-2607-09773 | score_7_9 | not_selected | — | — | V2=8/9；完整证据保留，但相对三条入选主轴更局部，或主要承担评测/反证边界。 | analysis-decision:SF-2026-ARXIV-2607-09773 |
| SF-2026-ARXIV-2607-09786 | score_7_9 | not_selected | — | — | V2=9/9；完整证据保留，但相对三条入选主轴更局部，或主要承担评测/反证边界。 | analysis-decision:SF-2026-ARXIV-2607-09786 |
| SF-2026-ARXIV-2607-09791 | score_7_9 | not_selected | — | — | V2=9/9；完整证据保留，但相对三条入选主轴更局部，或主要承担评测/反证边界。 | analysis-decision:SF-2026-ARXIV-2607-09791 |
| SF-2026-ARXIV-2607-09794 | score_7_9 | not_selected | — | — | V2=9/9；完整证据保留，但相对三条入选主轴更局部，或主要承担评测/反证边界。 | analysis-decision:SF-2026-ARXIV-2607-09794 |
| SF-2026-ARXIV-2607-09800 | score_7_9 | not_selected | — | — | V2=9/9；完整证据保留，但相对三条入选主轴更局部，或主要承担评测/反证边界。 | analysis-decision:SF-2026-ARXIV-2607-09800 |
| SF-2026-ARXIV-2607-09802 | score_7_9 | not_selected | — | — | V2=9/9；完整证据保留，但相对三条入选主轴更局部，或主要承担评测/反证边界。 | analysis-decision:SF-2026-ARXIV-2607-09802 |
| SF-2026-ARXIV-2607-09804 | forced_review | not_selected | — | — | V2=6/9；完整证据保留，但相对三条入选主轴更局部，或主要承担评测/反证边界。 | analysis-decision:SF-2026-ARXIV-2607-09804 |
| SF-2026-ARXIV-2607-09992 | score_7_9 | not_selected | — | — | V2=9/9；完整证据保留，但相对三条入选主轴更局部，或主要承担评测/反证边界。 | analysis-decision:SF-2026-ARXIV-2607-09992 |
| SF-2026-ARXIV-2607-09999 | score_7_9 | not_selected | — | — | V2=9/9；完整证据保留，但相对三条入选主轴更局部，或主要承担评测/反证边界。 | analysis-decision:SF-2026-ARXIV-2607-09999 |
| SF-2026-ARXIV-2607-10044 | score_7_9 | not_selected | — | — | V2=9/9；完整证据保留，但相对三条入选主轴更局部，或主要承担评测/反证边界。 | analysis-decision:SF-2026-ARXIV-2607-10044 |
| SF-2026-ARXIV-2607-10059 | score_7_9 | not_selected | — | — | V2=9/9；完整证据保留，但相对三条入选主轴更局部，或主要承担评测/反证边界。 | analysis-decision:SF-2026-ARXIV-2607-10059 |
| SF-2026-ARXIV-2607-10110 | score_7_9 | not_selected | — | — | V2=7/9；完整证据保留，但相对三条入选主轴更局部，或主要承担评测/反证边界。 | analysis-decision:SF-2026-ARXIV-2607-10110 |
| SF-2026-ARXIV-2607-10139 | score_7_9 | not_selected | — | — | V2=9/9；完整证据保留，但相对三条入选主轴更局部，或主要承担评测/反证边界。 | analysis-decision:SF-2026-ARXIV-2607-10139 |
| SF-2026-ARXIV-2607-10183 | score_7_9 | not_selected | — | — | V2=9/9；完整证据保留，但相对三条入选主轴更局部，或主要承担评测/反证边界。 | analysis-decision:SF-2026-ARXIV-2607-10183 |
| SF-2026-ARXIV-2607-10186 | score_7_9 | not_selected | — | — | V2=9/9；完整证据保留，但相对三条入选主轴更局部，或主要承担评测/反证边界。 | analysis-decision:SF-2026-ARXIV-2607-10186 |
| SF-2026-ARXIV-2607-10198 | score_7_9 | not_selected | — | — | V2=9/9；完整证据保留，但相对三条入选主轴更局部，或主要承担评测/反证边界。 | analysis-decision:SF-2026-ARXIV-2607-10198 |
| SF-2026-ARXIV-2607-10203 | score_7_9 | not_selected | — | — | V2=9/9；完整证据保留，但相对三条入选主轴更局部，或主要承担评测/反证边界。 | analysis-decision:SF-2026-ARXIV-2607-10203 |
| SF-2026-ARXIV-2607-10265 | score_7_9 | not_selected | — | — | V2=9/9；完整证据保留，但相对三条入选主轴更局部，或主要承担评测/反证边界。 | analysis-decision:SF-2026-ARXIV-2607-10265 |
| SF-2026-ARXIV-2607-10362 | score_7_9 | not_selected | — | — | V2=9/9；完整证据保留，但相对三条入选主轴更局部，或主要承担评测/反证边界。 | analysis-decision:SF-2026-ARXIV-2607-10362 |
| SF-2026-ARXIV-2607-10389 | score_7_9 | selected | DA-20260714-01 | — | V2=9/9；分别覆盖 exact world-state elasticity、组合式观测边界与外部反馈闭环，且三者 owner 不重叠。 | analysis:DA-20260714-01 |
| SF-2026-ARXIV-2607-10491 | score_7_9 | not_selected | — | — | V2=9/9；完整证据保留，但相对三条入选主轴更局部，或主要承担评测/反证边界。 | analysis-decision:SF-2026-ARXIV-2607-10491 |
| SF-2026-ARXIV-2607-10582 | score_7_9 | not_selected | — | — | V2=9/9；完整证据保留，但相对三条入选主轴更局部，或主要承担评测/反证边界。 | analysis-decision:SF-2026-ARXIV-2607-10582 |
| SF-2026-ARXIV-2607-10661 | score_7_9 | not_selected | — | — | V2=9/9；完整证据保留，但相对三条入选主轴更局部，或主要承担评测/反证边界。 | analysis-decision:SF-2026-ARXIV-2607-10661 |
| SF-2026-ARXIV-2607-10709 | score_7_9;forced_review | not_selected | — | — | V2=9/9；完整证据保留，但相对三条入选主轴更局部，或主要承担评测/反证边界。 | analysis-decision:SF-2026-ARXIV-2607-10709 |
| SF-2026-ARXIV-2607-10712 | score_7_9 | not_selected | — | — | V2=9/9；完整证据保留，但相对三条入选主轴更局部，或主要承担评测/反证边界。 | analysis-decision:SF-2026-ARXIV-2607-10712 |
| SF-2026-ARXIV-2607-10750 | score_7_9 | not_selected | — | — | V2=9/9；完整证据保留，但相对三条入选主轴更局部，或主要承担评测/反证边界。 | analysis-decision:SF-2026-ARXIV-2607-10750 |
| SF-2026-ARXIV-2607-10798 | score_7_9 | not_selected | — | — | V2=9/9；完整证据保留，但相对三条入选主轴更局部，或主要承担评测/反证边界。 | analysis-decision:SF-2026-ARXIV-2607-10798 |
| SF-2026-ARXIV-2607-10959 | score_7_9 | not_selected | — | — | V2=8/9；完整证据保留，但相对三条入选主轴更局部，或主要承担评测/反证边界。 | analysis-decision:SF-2026-ARXIV-2607-10959 |
| SF-2026-ARXIV-2607-10987 | score_7_9 | not_selected | — | — | V2=9/9；完整证据保留，但相对三条入选主轴更局部，或主要承担评测/反证边界。 | analysis-decision:SF-2026-ARXIV-2607-10987 |
| SF-2026-ARXIV-2607-11070 | score_7_9 | not_selected | — | — | V2=8/9；完整证据保留，但相对三条入选主轴更局部，或主要承担评测/反证边界。 | analysis-decision:SF-2026-ARXIV-2607-11070 |
| SF-2026-ARXIV-2607-11086 | score_7_9 | not_selected | — | — | V2=9/9；完整证据保留，但相对三条入选主轴更局部，或主要承担评测/反证边界。 | analysis-decision:SF-2026-ARXIV-2607-11086 |
| SF-2026-ARXIV-2607-11131 | score_7_9 | not_selected | — | — | V2=9/9；完整证据保留，但相对三条入选主轴更局部，或主要承担评测/反证边界。 | analysis-decision:SF-2026-ARXIV-2607-11131 |
| SF-2026-ARXIV-2607-11136 | score_7_9 | not_selected | — | — | V2=9/9；完整证据保留，但相对三条入选主轴更局部，或主要承担评测/反证边界。 | analysis-decision:SF-2026-ARXIV-2607-11136 |
| SF-2026-ARXIV-2607-11138 | score_7_9 | not_selected | — | — | V2=9/9；完整证据保留，但相对三条入选主轴更局部，或主要承担评测/反证边界。 | analysis-decision:SF-2026-ARXIV-2607-11138 |
| SF-2026-ARXIV-2607-11149 | score_7_9 | not_selected | — | — | V2=9/9；完整证据保留，但相对三条入选主轴更局部，或主要承担评测/反证边界。 | analysis-decision:SF-2026-ARXIV-2607-11149 |
| SF-2026-ARXIV-2607-11172 | score_7_9 | not_selected | — | — | V2=8/9；完整证据保留，但相对三条入选主轴更局部，或主要承担评测/反证边界。 | analysis-decision:SF-2026-ARXIV-2607-11172 |
| SF-2026-ARXIV-2607-11250 | score_7_9 | not_selected | — | — | V2=9/9；完整证据保留，但相对三条入选主轴更局部，或主要承担评测/反证边界。 | analysis-decision:SF-2026-ARXIV-2607-11250 |
| SF-2026-ARXIV-2607-11317 | score_7_9 | not_selected | — | — | V2=9/9；完整证据保留，但相对三条入选主轴更局部，或主要承担评测/反证边界。 | analysis-decision:SF-2026-ARXIV-2607-11317 |
| SF-2026-ARXIV-2607-11346 | score_7_9 | not_selected | — | — | V2=9/9；完整证据保留，但相对三条入选主轴更局部，或主要承担评测/反证边界。 | analysis-decision:SF-2026-ARXIV-2607-11346 |
| SF-2026-ARXIV-2607-11368 | score_7_9 | not_selected | — | — | V2=9/9；完整证据保留，但相对三条入选主轴更局部，或主要承担评测/反证边界。 | analysis-decision:SF-2026-ARXIV-2607-11368 |
| SF-2026-ARXIV-2607-11388 | score_7_9 | not_selected | — | — | V2=9/9；完整证据保留，但相对三条入选主轴更局部，或主要承担评测/反证边界。 | analysis-decision:SF-2026-ARXIV-2607-11388 |
| SF-2026-ARXIV-2607-11399 | score_7_9 | not_selected | — | — | V2=9/9；完整证据保留，但相对三条入选主轴更局部，或主要承担评测/反证边界。 | analysis-decision:SF-2026-ARXIV-2607-11399 |
| SF-2026-ARXIV-2607-11433 | score_7_9 | not_selected | — | — | V2=9/9；完整证据保留，但相对三条入选主轴更局部，或主要承担评测/反证边界。 | analysis-decision:SF-2026-ARXIV-2607-11433 |
| SF-2026-ARXIV-2607-11475 | score_7_9 | not_selected | — | — | V2=9/9；完整证据保留，但相对三条入选主轴更局部，或主要承担评测/反证边界。 | analysis-decision:SF-2026-ARXIV-2607-11475 |
| SF-2026-ARXIV-2607-11505 | score_7_9 | not_selected | — | — | V2=8/9；完整证据保留，但相对三条入选主轴更局部，或主要承担评测/反证边界。 | analysis-decision:SF-2026-ARXIV-2607-11505 |
| SF-2026-ARXIV-2607-11506 | score_7_9 | not_selected | — | — | V2=8/9；完整证据保留，但相对三条入选主轴更局部，或主要承担评测/反证边界。 | analysis-decision:SF-2026-ARXIV-2607-11506 |
| SF-2026-ARXIV-2607-11579 | score_7_9 | not_selected | — | — | V2=9/9；完整证据保留，但相对三条入选主轴更局部，或主要承担评测/反证边界。 | analysis-decision:SF-2026-ARXIV-2607-11579 |
| SF-2026-ARXIV-2607-11586 | score_7_9 | not_selected | — | — | V2=9/9；完整证据保留，但相对三条入选主轴更局部，或主要承担评测/反证边界。 | analysis-decision:SF-2026-ARXIV-2607-11586 |
| SF-2026-ARXIV-2607-11598 | score_7_9 | selected | DA-20260714-03 | — | V2=9/9；分别覆盖 exact world-state elasticity、组合式观测边界与外部反馈闭环，且三者 owner 不重叠。 | analysis:DA-20260714-03 |
| SF-2026-ARXIV-2607-11611 | score_7_9 | not_selected | — | — | V2=9/9；完整证据保留，但相对三条入选主轴更局部，或主要承担评测/反证边界。 | analysis-decision:SF-2026-ARXIV-2607-11611 |
| SF-2026-ARXIV-2607-11643 | score_7_9 | not_selected | — | — | V2=7/9；完整证据保留，但相对三条入选主轴更局部，或主要承担评测/反证边界。 | analysis-decision:SF-2026-ARXIV-2607-11643 |
| SF-2026-ARXIV-2607-11698 | score_7_9 | not_selected | — | — | V2=9/9；完整证据保留，但相对三条入选主轴更局部，或主要承担评测/反证边界。 | analysis-decision:SF-2026-ARXIV-2607-11698 |
| SF-2026-ARXIV-2607-11751 | score_7_9 | selected | DA-20260714-02 | — | V2=9/9；分别覆盖 exact world-state elasticity、组合式观测边界与外部反馈闭环，且三者 owner 不重叠。 | analysis:DA-20260714-02 |

### Selection Decisions

<!-- analysis-decision:SF-2026-ARXIV-2607-09665:start -->
`SF-2026-ARXIV-2607-09665` 已完成 exact-v1 Deep Review。其机制焦点是：We study this variance under a token-controlled protocol and introduce two complementary metrics: the Format Sensitivity Index (FSI), the accuracy range induced by wrapper choice, and the Parseability Sensitivity Index (PSI), the corresponding range in answer parseability. 为保持 `PLATFORM-EVALUATION-SYSTEM` 的独立 owner，本日报不把它压入三条长叙事；完整反证与 trade-off 保留在 `review:SF-2026-ARXIV-2607-09665`。
<!-- analysis-decision:SF-2026-ARXIV-2607-09665:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-09682:start -->
`SF-2026-ARXIV-2607-09682` 已完成 exact-v1 Deep Review。其机制焦点是：The design serializes every evidence-bearing inference step into an authenticated record whose identity, parentage and mutation history can be replayed after the decision. 为保持 `PLATFORM-TRACE` 的独立 owner，本日报不把它压入三条长叙事；完整反证与 trade-off 保留在 `review:SF-2026-ARXIV-2607-09682`。
<!-- analysis-decision:SF-2026-ARXIV-2607-09682:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-09686:start -->
`SF-2026-ARXIV-2607-09686` 已完成 exact-v1 Deep Review。其机制焦点是：Sparse Mixture-of-Experts (MoE) language models separate total parameter count from per-token active computation, but local inference systems often still require the full model, key-value cache, runtime buffers, and operatingsystem headroom to fit in fast memory. 为保持 `INFER-SCHEDULING` 的独立 owner，本日报不把它压入三条长叙事；完整反证与 trade-off 保留在 `review:SF-2026-ARXIV-2607-09686`。
<!-- analysis-decision:SF-2026-ARXIV-2607-09686:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-09689:start -->
`SF-2026-ARXIV-2607-09689` 已完成 exact-v1 Deep Review。其机制焦点是：The prototype assigns stable evidence identities, records fork lineage and tests whether a later aggregate can detect duplicated evidence instead of treating correlated branches as independent support. 为保持 `AGENT-WORKFLOW` 的独立 owner，本日报不把它压入三条长叙事；完整反证与 trade-off 保留在 `review:SF-2026-ARXIV-2607-09689`。
<!-- analysis-decision:SF-2026-ARXIV-2607-09689:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-09697:start -->
`SF-2026-ARXIV-2607-09697` 已完成 exact-v1 Deep Review。其机制焦点是：Motivated by this insight, we propose a paradigm shift toward output-aware safety guardrails. 为保持 `PLATFORM-SECURITY` 的独立 owner，本日报不把它压入三条长叙事；完整反证与 trade-off 保留在 `review:SF-2026-ARXIV-2607-09697`。
<!-- analysis-decision:SF-2026-ARXIV-2607-09697:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-09709:start -->
`SF-2026-ARXIV-2607-09709` 已完成 exact-v1 Deep Review。其机制焦点是：We study the opposite signal: a deterministic, judge-free, ungameable filter -- whether a generated project launches cleanly under a headless engine (strict-launch). 为保持 `PLATFORM-EVALUATION-SYSTEM` 的独立 owner，本日报不把它压入三条长叙事；完整反证与 trade-off 保留在 `review:SF-2026-ARXIV-2607-09709`。
<!-- analysis-decision:SF-2026-ARXIV-2607-09709:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-09744:start -->
`SF-2026-ARXIV-2607-09744` 已完成 exact-v1 Deep Review。其机制焦点是：We propose least autonomy as an appropriate generalization and develop a formal theory. 为保持 `PLATFORM-SECURITY` 的独立 owner，本日报不把它压入三条长叙事；完整反证与 trade-off 保留在 `review:SF-2026-ARXIV-2607-09744`。
<!-- analysis-decision:SF-2026-ARXIV-2607-09744:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-09748:start -->
`SF-2026-ARXIV-2607-09748` 已完成 exact-v1 Deep Review。其机制焦点是：We propose Epistemic State Replication (ESR), a belief-replication layer for agentic distributed systems that shifts the replication boundary from data visibility to knowledge visibility. 为保持 `AGENT-PLATFORM` 的独立 owner，本日报不把它压入三条长叙事；完整反证与 trade-off 保留在 `review:SF-2026-ARXIV-2607-09748`。
<!-- analysis-decision:SF-2026-ARXIV-2607-09748:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-09759:start -->
`SF-2026-ARXIV-2607-09759` 已完成 exact-v1 Deep Review。其机制焦点是：In this paper, we propose ReflectWorld-MM, an entity-oriented multimodal memory system for open-ended video streams. 为保持 `AGENT-MEMORY` 的独立 owner，本日报不把它压入三条长叙事；完整反证与 trade-off 保留在 `review:SF-2026-ARXIV-2607-09759`。
<!-- analysis-decision:SF-2026-ARXIV-2607-09759:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-09773:start -->
`SF-2026-ARXIV-2607-09773` 已完成 exact-v1 Deep Review。其机制焦点是：Overall, EvoCUA-1.5 provides a practical framework for scaling online RL in multi-turn computer-use agents. 为保持 `TRAIN-GRPO` 的独立 owner，本日报不把它压入三条长叙事；完整反证与 trade-off 保留在 `review:SF-2026-ARXIV-2607-09773`。
<!-- analysis-decision:SF-2026-ARXIV-2607-09773:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-09786:start -->
`SF-2026-ARXIV-2607-09786` 已完成 exact-v1 Deep Review。其机制焦点是：The study applies controlled length-penalty training and compares matched-capability models with monitors that inspect outputs or internal activations, separating shorter reasoning from observability loss. 为保持 `PLATFORM-EVALUATION-SYSTEM` 的独立 owner，本日报不把它压入三条长叙事；完整反证与 trade-off 保留在 `review:SF-2026-ARXIV-2607-09786`。
<!-- analysis-decision:SF-2026-ARXIV-2607-09786:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-09791:start -->
`SF-2026-ARXIV-2607-09791` 已完成 exact-v1 Deep Review。其机制焦点是：The multiplicative repetition penalty shipped across the LLM inference ecosystem (HuggingFace, vLLM, llama$.$cpp, and a dozen further engines) branches on the sign of each raw logit (divide positives by theta, multiply negatives). 为保持 `INFER-DECODE` 的独立 owner，本日报不把它压入三条长叙事；完整反证与 trade-off 保留在 `review:SF-2026-ARXIV-2607-09791`。
<!-- analysis-decision:SF-2026-ARXIV-2607-09791:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-09794:start -->
`SF-2026-ARXIV-2607-09794` 已完成 exact-v1 Deep Review。其机制焦点是：In this work, we conduct a comprehensive empirical study to understand why this setting remains difficult. 为保持 `AGENT-CONTEXT` 的独立 owner，本日报不把它压入三条长叙事；完整反证与 trade-off 保留在 `review:SF-2026-ARXIV-2607-09794`。
<!-- analysis-decision:SF-2026-ARXIV-2607-09794:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-09800:start -->
`SF-2026-ARXIV-2607-09800` 已完成 exact-v1 Deep Review。其机制焦点是：A high-precision reference run fixes the expected update trace, then low-precision decoder runs isolate where deterministic nearest write-back erases small recurrent updates; stochastic write-back is tested as the repair. 为保持 `TRAIN-PRETRAINING` 的独立 owner，本日报不把它压入三条长叙事；完整反证与 trade-off 保留在 `review:SF-2026-ARXIV-2607-09800`。
<!-- analysis-decision:SF-2026-ARXIV-2607-09800:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-09802:start -->
`SF-2026-ARXIV-2607-09802` 已完成 exact-v1 Deep Review。其机制焦点是：The system couples an internal market price with allocation decisions so teams express marginal accelerator value while the controller continuously reconciles demand with a constrained shared fleet. 为保持 `PLATFORM-GPU-SCHEDULER` 的独立 owner，本日报不把它压入三条长叙事；完整反证与 trade-off 保留在 `review:SF-2026-ARXIV-2607-09802`。
<!-- analysis-decision:SF-2026-ARXIV-2607-09802:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-09804:start -->
`SF-2026-ARXIV-2607-09804` 已完成 exact-v1 Deep Review。其机制焦点是：Their model cards prohibit specific behaviors -- recommending exact drug dosages, issuing definitive diagnoses, prescribing treatments, adjudicating drug-drug interactions, and advising that emergency care can be skipped -- yet a model card describes intended behavior, not robust behavior. 为保持 `PLATFORM-SECURITY` 的独立 owner，本日报不把它压入三条长叙事；完整反证与 trade-off 保留在 `review:SF-2026-ARXIV-2607-09804`。
<!-- analysis-decision:SF-2026-ARXIV-2607-09804:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-09992:start -->
`SF-2026-ARXIV-2607-09992` 已完成 exact-v1 Deep Review。其机制焦点是：Rather than trust the learner to be right, we bound the damage a wrong one can do: a small trusted guard wraps the untrusted learner (learned proposes, the guard disposes). 为保持 `INFER-SCHEDULING` 的独立 owner，本日报不把它压入三条长叙事；完整反证与 trade-off 保留在 `review:SF-2026-ARXIV-2607-09992`。
<!-- analysis-decision:SF-2026-ARXIV-2607-09992:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-09999:start -->
`SF-2026-ARXIV-2607-09999` 已完成 exact-v1 Deep Review。其机制焦点是：Using a six-category failure taxonomy validated by two independent human annotators (Cohen's $κ$ = 0.906), we classify 30,000 chain-of-thought outputs from five instruction-tuned LLMs (3B--14B parameters) across three quantization precisions (FP32, FP16, NF4) and four reasoning benchmarks. 为保持 `PLATFORM-EVALUATION-SYSTEM` 的独立 owner，本日报不把它压入三条长叙事；完整反证与 trade-off 保留在 `review:SF-2026-ARXIV-2607-09999`。
<!-- analysis-decision:SF-2026-ARXIV-2607-09999:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-10044:start -->
`SF-2026-ARXIV-2607-10044` 已完成 exact-v1 Deep Review。其机制焦点是：FlashTrie maps trie traversal and constrained beam expansion to fused GPU kernels, keeping constraint state on device instead of round-tripping candidate prefixes through a CPU controller. 为保持 `INFER-DECODE` 的独立 owner，本日报不把它压入三条长叙事；完整反证与 trade-off 保留在 `review:SF-2026-ARXIV-2607-10044`。
<!-- analysis-decision:SF-2026-ARXIV-2607-10044:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-10059:start -->
`SF-2026-ARXIV-2607-10059` 已完成 exact-v1 Deep Review。其机制焦点是：The framework pairs otherwise matched tasks where acting is appropriate or harmful, executes both through real agent harnesses and scores an agent only when it both acts and abstains correctly. 为保持 `AGENT-TOOL-CALLING` 的独立 owner，本日报不把它压入三条长叙事；完整反证与 trade-off 保留在 `review:SF-2026-ARXIV-2607-10059`。
<!-- analysis-decision:SF-2026-ARXIV-2607-10059:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-10110:start -->
`SF-2026-ARXIV-2607-10110` 已完成 exact-v1 Deep Review。其机制焦点是：Existing studies, however, focus almost exclusively on Transformer backbones, leaving open whether this principle also applies to state-space language models. 为保持 `MODEL-LONG-CONTEXT` 的独立 owner，本日报不把它压入三条长叙事；完整反证与 trade-off 保留在 `review:SF-2026-ARXIV-2607-10110`。
<!-- analysis-decision:SF-2026-ARXIV-2607-10110:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-10139:start -->
`SF-2026-ARXIV-2607-10139` 已完成 exact-v1 Deep Review。其机制焦点是：We make this precise with a parameter-free law, derived in closed form, that predicts consensus accuracy from three measured panel statistics to a mean absolute error of $0.03$ and exposes the method's ceiling: a shared-error floor where models share a misconception, near zero on math but non-trivial on science. 为保持 `PLATFORM-EVALUATION-SYSTEM` 的独立 owner，本日报不把它压入三条长叙事；完整反证与 trade-off 保留在 `review:SF-2026-ARXIV-2607-10139`。
<!-- analysis-decision:SF-2026-ARXIV-2607-10139:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-10183:start -->
`SF-2026-ARXIV-2607-10183` 已完成 exact-v1 Deep Review。其机制焦点是：This paper presents ATSInfer, a hybrid CPU-GPU inference system for consumer devices that performs offloading at tensor granularity. 为保持 `INFER-TENSORRT-LLM` 的独立 owner，本日报不把它压入三条长叙事；完整反证与 trade-off 保留在 `review:SF-2026-ARXIV-2607-10183`。
<!-- analysis-decision:SF-2026-ARXIV-2607-10183:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-10186:start -->
`SF-2026-ARXIV-2607-10186` 已完成 exact-v1 Deep Review。其机制焦点是：We present FlashAccel, a co-designed system that enables efficient LLM inference using HBF. 为保持 `INFER-GPU-MEMORY` 的独立 owner，本日报不把它压入三条长叙事；完整反证与 trade-off 保留在 `review:SF-2026-ARXIV-2607-10186`。
<!-- analysis-decision:SF-2026-ARXIV-2607-10186:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-10198:start -->
`SF-2026-ARXIV-2607-10198` 已完成 exact-v1 Deep Review。其机制焦点是：In such systems, search API performance is often evaluated primarily by answer accuracy. 为保持 `AGENT-RAG` 的独立 owner，本日报不把它压入三条长叙事；完整反证与 trade-off 保留在 `review:SF-2026-ARXIV-2607-10198`。
<!-- analysis-decision:SF-2026-ARXIV-2607-10198:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-10203:start -->
`SF-2026-ARXIV-2607-10203` 已完成 exact-v1 Deep Review。其机制焦点是：In autoregressive rollouts, where planning actually happens, that premise requires depth's per-step precision to survive composition. 为保持 `MULTIMODAL-WORLD-MODELS` 的独立 owner，本日报不把它压入三条长叙事；完整反证与 trade-off 保留在 `review:SF-2026-ARXIV-2607-10203`。
<!-- analysis-decision:SF-2026-ARXIV-2607-10203:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-10265:start -->
`SF-2026-ARXIV-2607-10265` 已完成 exact-v1 Deep Review。其机制焦点是：We present TGMS, a bi-temporal property graph management system that exposes thirteen verified temporal operators as agent tools. 为保持 `AGENT-MEMORY` 的独立 owner，本日报不把它压入三条长叙事；完整反证与 trade-off 保留在 `review:SF-2026-ARXIV-2607-10265`。
<!-- analysis-decision:SF-2026-ARXIV-2607-10265:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-10362:start -->
`SF-2026-ARXIV-2607-10362` 已完成 exact-v1 Deep Review。其机制焦点是：Current practice adopts the prediction error, the single- or multi-step rollout loss on held-out data, as the training and model-selection objective, on the assumption that a lower prediction error yields better control. 为保持 `MULTIMODAL-WORLD-MODELS` 的独立 owner，本日报不把它压入三条长叙事；完整反证与 trade-off 保留在 `review:SF-2026-ARXIV-2607-10362`。
<!-- analysis-decision:SF-2026-ARXIV-2607-10362:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-10491:start -->
`SF-2026-ARXIV-2607-10491` 已完成 exact-v1 Deep Review。其机制焦点是：This paper introduces ERAG, an uncertainty-aware RAG framework that converts retrieved chunks into probabilistic evidence before generation. 为保持 `AGENT-RAG` 的独立 owner，本日报不把它压入三条长叙事；完整反证与 trade-off 保留在 `review:SF-2026-ARXIV-2607-10491`。
<!-- analysis-decision:SF-2026-ARXIV-2607-10491:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-10582:start -->
`SF-2026-ARXIV-2607-10582` 已完成 exact-v1 Deep Review。其机制焦点是：We introduce MemDecay, a training-free, region-aware KV-cache eviction policy. 为保持 `INFER-KV-CACHE` 的独立 owner，本日报不把它压入三条长叙事；完整反证与 trade-off 保留在 `review:SF-2026-ARXIV-2607-10582`。
<!-- analysis-decision:SF-2026-ARXIV-2607-10582:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-10661:start -->
`SF-2026-ARXIV-2607-10661` 已完成 exact-v1 Deep Review。其机制焦点是：In this paper, we propose \textbf{Progressive Tree Drafting (PTD)}, which employs a structured, guided parallel drafting strategy to harness the model's parallel potential. 为保持 `INFER-SPECULATIVE-DECODING` 的独立 owner，本日报不把它压入三条长叙事；完整反证与 trade-off 保留在 `review:SF-2026-ARXIV-2607-10661`。
<!-- analysis-decision:SF-2026-ARXIV-2607-10661:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-10709:start -->
`SF-2026-ARXIV-2607-10709` 已完成 exact-v1 Deep Review。其机制焦点是：In this paper, we propose PromptGraph, a graph-guided prompt-sanitization approach for privacy-preserving LLM inference. 为保持 `PLATFORM-SECURITY` 的独立 owner，本日报不把它压入三条长叙事；完整反证与 trade-off 保留在 `review:SF-2026-ARXIV-2607-10709`。
<!-- analysis-decision:SF-2026-ARXIV-2607-10709:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-10712:start -->
`SF-2026-ARXIV-2607-10712` 已完成 exact-v1 Deep Review。其机制焦点是：The attack requires no topic-specific trigger-words, agent access, indirect prompt injection, or fabricated papers, only the open data ecosystem and misleading metadata. 为保持 `PLATFORM-SECURITY` 的独立 owner，本日报不把它压入三条长叙事；完整反证与 trade-off 保留在 `review:SF-2026-ARXIV-2607-10712`。
<!-- analysis-decision:SF-2026-ARXIV-2607-10712:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-10750:start -->
`SF-2026-ARXIV-2607-10750` 已完成 exact-v1 Deep Review。其机制焦点是：As models are increasingly deployed as agents, synthetic trajectories are likely to become an important source of training data for agentic behavior. 为保持 `TRAIN-DATA` 的独立 owner，本日报不把它压入三条长叙事；完整反证与 trade-off 保留在 `review:SF-2026-ARXIV-2607-10750`。
<!-- analysis-decision:SF-2026-ARXIV-2607-10750:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-10798:start -->
`SF-2026-ARXIV-2607-10798` 已完成 exact-v1 Deep Review。其机制焦点是：We introduce QIMG-7, a controlled benchmark for multimodal retrieval pollution in multi-sentence factual QA, spanning four datasets, seven image-attack families, and 16 paired clean/polluted regimes, for 1,760 evaluation rows per method. 为保持 `AGENT-RAG` 的独立 owner，本日报不把它压入三条长叙事；完整反证与 trade-off 保留在 `review:SF-2026-ARXIV-2607-10798`。
<!-- analysis-decision:SF-2026-ARXIV-2607-10798:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-10959:start -->
`SF-2026-ARXIV-2607-10959` 已完成 exact-v1 Deep Review。其机制焦点是：Motivated by stochastic convex optimization, we propose WSqD (Warmup with Square-root base and linear Decay), a learning rate schedule that replaces WSD's constant stable phase with a shifted inverse-square-root base while retaining the final linear cooldown. 为保持 `TRAIN-PRETRAINING` 的独立 owner，本日报不把它压入三条长叙事；完整反证与 trade-off 保留在 `review:SF-2026-ARXIV-2607-10959`。
<!-- analysis-decision:SF-2026-ARXIV-2607-10959:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-10987:start -->
`SF-2026-ARXIV-2607-10987` 已完成 exact-v1 Deep Review。其机制焦点是：We introduce AAFLOW+, a stateful extension of agentic workflow operators that makes KV cache a first-class distributed systems object. 为保持 `INFER-DYNAMO` 的独立 owner，本日报不把它压入三条长叙事；完整反证与 trade-off 保留在 `review:SF-2026-ARXIV-2607-10987`。
<!-- analysis-decision:SF-2026-ARXIV-2607-10987:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-11070:start -->
`SF-2026-ARXIV-2607-11070` 已完成 exact-v1 Deep Review。其机制焦点是：We propose decomposed credit GRPO (DC-GRPO), a unified turn-level credit assignment framework for Group Relative Policy Optimization in multi-turn jailbreak learning. 为保持 `TRAIN-GRPO` 的独立 owner，本日报不把它压入三条长叙事；完整反证与 trade-off 保留在 `review:SF-2026-ARXIV-2607-11070`。
<!-- analysis-decision:SF-2026-ARXIV-2607-11070:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-11086:start -->
`SF-2026-ARXIV-2607-11086` 已完成 exact-v1 Deep Review。其机制焦点是：MCPZoo executes a large corpus of MCP servers behind controlled clients and compares runtime-observed behavior with static scanner findings, retaining server identity and invocation traces for attribution. 为保持 `AGENT-MCP` 的独立 owner，本日报不把它压入三条长叙事；完整反证与 trade-off 保留在 `review:SF-2026-ARXIV-2607-11086`。
<!-- analysis-decision:SF-2026-ARXIV-2607-11086:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-11131:start -->
`SF-2026-ARXIV-2607-11131` 已完成 exact-v1 Deep Review。其机制焦点是：We propose TIGER, a Text-conditioned vIsual GatEd Routing framework for multimodal speculative decoding. 为保持 `INFER-SPECULATIVE-DECODING` 的独立 owner，本日报不把它压入三条长叙事；完整反证与 trade-off 保留在 `review:SF-2026-ARXIV-2607-11131`。
<!-- analysis-decision:SF-2026-ARXIV-2607-11131:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-11136:start -->
`SF-2026-ARXIV-2607-11136` 已完成 exact-v1 Deep Review。其机制焦点是：In this paper, we present Xema, a memory-efficient diffusion serving system that exploits predictable tensor lifetimes for trace-guided memory optimization. 为保持 `INFER-GPU-MEMORY` 的独立 owner，本日报不把它压入三条长叙事；完整反证与 trade-off 保留在 `review:SF-2026-ARXIV-2607-11136`。
<!-- analysis-decision:SF-2026-ARXIV-2607-11136:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-11138:start -->
`SF-2026-ARXIV-2607-11138` 已完成 exact-v1 Deep Review。其机制焦点是：This leads to decision-space explosion, context window saturation, and degraded routing accuracy. 为保持 `AGENT-WORKFLOW` 的独立 owner，本日报不把它压入三条长叙事；完整反证与 trade-off 保留在 `review:SF-2026-ARXIV-2607-11138`。
<!-- analysis-decision:SF-2026-ARXIV-2607-11138:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-11149:start -->
`SF-2026-ARXIV-2607-11149` 已完成 exact-v1 Deep Review。其机制焦点是：We introduce AgentFootprint, a cross-framework benchmark of post-run agent storage footprint. 为保持 `PLATFORM-COST` 的独立 owner，本日报不把它压入三条长叙事；完整反证与 trade-off 保留在 `review:SF-2026-ARXIV-2607-11149`。
<!-- analysis-decision:SF-2026-ARXIV-2607-11149:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-11172:start -->
`SF-2026-ARXIV-2607-11172` 已完成 exact-v1 Deep Review。其机制焦点是：We propose STAMP, in which a reference-based verifier judges whether each cited document supports an entity or relation in a training-time evidence graph, and first-exposure attribution traces each supported citation back to the action that first surfaced it. 为保持 `TRAIN-GRPO` 的独立 owner，本日报不把它压入三条长叙事；完整反证与 trade-off 保留在 `review:SF-2026-ARXIV-2607-11172`。
<!-- analysis-decision:SF-2026-ARXIV-2607-11172:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-11250:start -->
`SF-2026-ARXIV-2607-11250` 已完成 exact-v1 Deep Review。其机制焦点是：To address this, we introduce Multi- Agent Contextual Exploration (MACE), a lightweight framework that explicitly promotes exploration through structured peer selection. 为保持 `AGENT-MULTI-AGENT` 的独立 owner，本日报不把它压入三条长叙事；完整反证与 trade-off 保留在 `review:SF-2026-ARXIV-2607-11250`。
<!-- analysis-decision:SF-2026-ARXIV-2607-11250:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-11317:start -->
`SF-2026-ARXIV-2607-11317` 已完成 exact-v1 Deep Review。其机制焦点是：The paper rejects centered token log-probability as a drift statistic because its increments form a mean-zero martingale, then constructs a calibrated replacement and evaluates it conservatively. 为保持 `INFER-DECODE` 的独立 owner，本日报不把它压入三条长叙事；完整反证与 trade-off 保留在 `review:SF-2026-ARXIV-2607-11317`。
<!-- analysis-decision:SF-2026-ARXIV-2607-11317:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-11346:start -->
`SF-2026-ARXIV-2607-11346` 已完成 exact-v1 Deep Review。其机制焦点是：We compile machine-readable SOP constraints into executable pseudo-code and run them with a program-guided (PG) stack machine that pages the active frame while an LLM performs semantic execution. 为保持 `AGENT-WORKFLOW` 的独立 owner，本日报不把它压入三条长叙事；完整反证与 trade-off 保留在 `review:SF-2026-ARXIV-2607-11346`。
<!-- analysis-decision:SF-2026-ARXIV-2607-11346:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-11368:start -->
`SF-2026-ARXIV-2607-11368` 已完成 exact-v1 Deep Review。其机制焦点是：We present an attribution study on four NVIDIA RTX A5000 GPUs, 24 GiB each, on a single host with NVLink-bridged pairs. 为保持 `INFER-TENSORRT-LLM` 的独立 owner，本日报不把它压入三条长叙事；完整反证与 trade-off 保留在 `review:SF-2026-ARXIV-2607-11368`。
<!-- analysis-decision:SF-2026-ARXIV-2607-11368:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-11388:start -->
`SF-2026-ARXIV-2607-11388` 已完成 exact-v1 Deep Review。其机制焦点是：We present \textbf{StructAgent}, a state-centered framework that introduces a unified state for maintaining compact, verifiable task progress and a structured workflow that regulates progress through verifier-backed state transitions. 为保持 `AGENT-WORKFLOW` 的独立 owner，本日报不把它压入三条长叙事；完整反证与 trade-off 保留在 `review:SF-2026-ARXIV-2607-11388`。
<!-- analysis-decision:SF-2026-ARXIV-2607-11388:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-11399:start -->
`SF-2026-ARXIV-2607-11399` 已完成 exact-v1 Deep Review。其机制焦点是：The harness routes at execution-step granularity using current observation, context, control state, prior failures, cost and outcome; the resulting trace becomes supervised data for later router updates. 为保持 `AGENT-PLATFORM` 的独立 owner，本日报不把它压入三条长叙事；完整反证与 trade-off 保留在 `review:SF-2026-ARXIV-2607-11399`。
<!-- analysis-decision:SF-2026-ARXIV-2607-11399:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-11433:start -->
`SF-2026-ARXIV-2607-11433` 已完成 exact-v1 Deep Review。其机制焦点是：We propose Omni-Decision, a training-free evidence-state system that turns omni-modal QA into a query-scoped evidence-closure process. 为保持 `AGENT-WORKFLOW` 的独立 owner，本日报不把它压入三条长叙事；完整反证与 trade-off 保留在 `review:SF-2026-ARXIV-2607-11433`。
<!-- analysis-decision:SF-2026-ARXIV-2607-11433:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-11475:start -->
`SF-2026-ARXIV-2607-11475` 已完成 exact-v1 Deep Review。其机制焦点是：To meet these requirements, we propose HyperSafe, a framework that restores safety behavior by generating a model-specific Safe Side Network (SSN) for each fine-tuned checkpoint. 为保持 `PLATFORM-SECURITY` 的独立 owner，本日报不把它压入三条长叙事；完整反证与 trade-off 保留在 `review:SF-2026-ARXIV-2607-11475`。
<!-- analysis-decision:SF-2026-ARXIV-2607-11475:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-11505:start -->
`SF-2026-ARXIV-2607-11505` 已完成 exact-v1 Deep Review。其机制焦点是：To alleviate this, we introduce Proxy OPD (P-OPD), an asynchronous post-training framework that transfers reward-induced policy improvements rather than absolute policy distributions. 为保持 `TRAIN-GRPO` 的独立 owner，本日报不把它压入三条长叙事；完整反证与 trade-off 保留在 `review:SF-2026-ARXIV-2607-11505`。
<!-- analysis-decision:SF-2026-ARXIV-2607-11505:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-11506:start -->
`SF-2026-ARXIV-2607-11506` 已完成 exact-v1 Deep Review。其机制焦点是：We introduce SCOPE-RL (Scaffolded Chain Optimization with Process Efficiency), a two-stage framework that densifies this anchor while retaining the GRPO update: Adaptive Scaffolded RL adds prefix-decomposed verifiable rewards on answer-hidden sub-question chains before success, and Quality-Aware Process RL applies correctness-gated process-shape rewards to refine correct trajectories after success. 为保持 `TRAIN-GRPO` 的独立 owner，本日报不把它压入三条长叙事；完整反证与 trade-off 保留在 `review:SF-2026-ARXIV-2607-11506`。
<!-- analysis-decision:SF-2026-ARXIV-2607-11506:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-11579:start -->
`SF-2026-ARXIV-2607-11579` 已完成 exact-v1 Deep Review。其机制焦点是：MemExchange is a cluster-wide, multi-tenant memory management system that dynamically right-sizes in-memory caching tenants according to workload demand. 为保持 `PLATFORM-GPU-SCHEDULER` 的独立 owner，本日报不把它压入三条长叙事；完整反证与 trade-off 保留在 `review:SF-2026-ARXIV-2607-11579`。
<!-- analysis-decision:SF-2026-ARXIV-2607-11579:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-11586:start -->
`SF-2026-ARXIV-2607-11586` 已完成 exact-v1 Deep Review。其机制焦点是：This paper proposes HCRMap, a hot expert residency mapping framework for pressure-aware expert replica management in 3.5D MoE inference. 为保持 `MODEL-MOE` 的独立 owner，本日报不把它压入三条长叙事；完整反证与 trade-off 保留在 `review:SF-2026-ARXIV-2607-11586`。
<!-- analysis-decision:SF-2026-ARXIV-2607-11586:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-11611:start -->
`SF-2026-ARXIV-2607-11611` 已完成 exact-v1 Deep Review。其机制焦点是：An LLM-generated bug report is accepted only when accompanied by a machine-checkable program-logic proof; the Mizzle checker becomes the authority for the reported defect rather than the model's prose. 为保持 `AGENT-TOOL-CALLING` 的独立 owner，本日报不把它压入三条长叙事；完整反证与 trade-off 保留在 `review:SF-2026-ARXIV-2607-11611`。
<!-- analysis-decision:SF-2026-ARXIV-2607-11611:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-11643:start -->
`SF-2026-ARXIV-2607-11643` 已完成 exact-v1 Deep Review。其机制焦点是：We present Xiaomi-Robotics-U0, a 38-billion-parameter multimodal autoregressive model for unified embodied synthesis. 为保持 `MULTIMODAL-WORLD-MODELS` 的独立 owner，本日报不把它压入三条长叙事；完整反证与 trade-off 保留在 `review:SF-2026-ARXIV-2607-11643`。
<!-- analysis-decision:SF-2026-ARXIV-2607-11643:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-11698:start -->
`SF-2026-ARXIV-2607-11698` 已完成 exact-v1 Deep Review。其机制焦点是：We present AHA, a falsifiable discovery loop that proposes a vulnerability hypothesis, constructs a falsifier, instantiates a valid attack, executes it in a sandboxed harness, reflects on the trajectory, and promotes confirmed findings into a Vulnerability Concept Graph (VCG). 为保持 `PLATFORM-SECURITY` 的独立 owner，本日报不把它压入三条长叙事；完整反证与 trade-off 保留在 `review:SF-2026-ARXIV-2607-11698`。
<!-- analysis-decision:SF-2026-ARXIV-2607-11698:end -->

### Selected Analysis Narratives

<!-- analysis:DA-20260714-01:start -->
### Stateful Worlds, Stateless Elasticity: Exact-State Serving for Interactive World Models

**旧方案为何合理、约束何时改变。** 当 world state 很小或允许重算时，session 固定在原设备最简单；交互世界状态变大、重算会改变世界之后，弹性伸缩必须同时解决 bit-identical transport、校验与 admission。

**机制如何改写 control / data / state。** That state cannot be recomputed in interactive time or approximated without changing the world, so a live session pins its device.

**可成立的证据边界。** Exact-state elasticity is a joint scheduling problem over transport and verification. 但 What is not public is a replayable world-model production trace (the one production operator ( 33 ) publishes only per-minute aggregates), so a validated production mix does not yet exist. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**收益、代价与下一重压力。** 更激进的缓存、迁移、并行或专用执行会换取吞吐/时延，同时增加配置依赖、资源压力与回退路径。 论文自身的边界信号是：What is not public is a replayable world-model production trace (the one production operator ( 33 ) publishes only per-minute aggregates), so a validated production mix does not yet exist. 因而这是一条受 workload 与状态边界约束的演进路线，不是无条件替代。

关联完整 Source Review：`review:SF-2026-ARXIV-2607-10389`。
<!-- analysis:DA-20260714-01:end -->

<!-- analysis:DA-20260714-02:start -->
### When Local Monitors Miss Compositional Harm: Diagnosing Distributed Backdoors in Multi-Agent Systems

**旧方案为何合理、约束何时改变。** 局部 monitor 在局部行为本身足以暴露风险时成本最低；当恶意语义只在跨步骤组装后出现，观测面必须提升到能够看见组合结果的 representation boundary。

**机制如何改写 control / data / state。** As multi-agent, tool-using LLM systems are deployed, a common safety net is a runtime monitor that checks each message, tool call, or step on its own.

**可成立的证据边界。** The experiments and formal observability argument agree that locally benign fragments defeat monitors restricted to local views, while signal returns only at a representation exposing the assembled payload. 但 What defeats a local monitor is not splitting but the loss of usable evidence, and detection returns only when the monitor changes what it observes, recovering the assembled code structure from benign data alone, then reading the decoded program to block the attack outright. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**收益、代价与下一重压力。** 新的安全控制点降低特定失败，但会引入误拒绝、旁路、观测不足或模型/任务迁移问题。 论文自身的边界信号是：What defeats a local monitor is not splitting but the loss of usable evidence, and detection returns only when the monitor changes what it observes, recovering the assembled code structure from benign data alone, then reading the decoded program to block the attack outright. 因而这是一条受 workload 与状态边界约束的演进路线，不是无条件替代。

关联完整 Source Review：`review:SF-2026-ARXIV-2607-11751`。
<!-- analysis:DA-20260714-02:end -->

<!-- analysis:DA-20260714-03:start -->
### Interaction Scaling: Grounding the Third Axis of Test-Time Compute

**旧方案为何合理、约束何时改变。** 单次生成在任务可由模型内部状态完成时足够；需要可检验外部反馈时，继续堆叠内部推理不能替代真实 observation，系统必须显式提交观察并允许修订。

**机制如何改写 control / data / state。** The loop alternates proposal, external instrument observation and revision; each cycle imports a new grounded observation, and the outcome metric must observe the same failure surface for improvement to be visible.

**可成立的证据边界。** A tool that measures the real layout instead shows the loop removing 40-74% of defects across four modalities; and that same VLM, used as the reviewer, makes slide layouts worse where the measuring tool repairs them. 但 9 Limitations Two modalities saturate: video editing is already strong single-shot (the lift is real only on a hardened multi-step suite), and deep research saturates because frontier models know well-documented facts and the judge cannot grade facts it does not have. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**收益、代价与下一重压力。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：9 Limitations Two modalities saturate: video editing is already strong single-shot (the lift is real only on a hardened multi-step suite), and deep research saturates because frontier models know well-documented facts and the judge cannot grade facts it does not have. 因而这是一条受 workload 与状态边界约束的演进路线，不是无条件替代。

关联完整 Source Review：`review:SF-2026-ARXIV-2607-11598`。
<!-- analysis:DA-20260714-03:end -->

## 6. Books Comparison

<!-- validator:books-comparison-v1 -->
| Source Family ID | Stable Node ID | Target Chapter Ref | Adjacent Chapter Refs | Existing Proposition | New Evidence Delta | Evolution Relation | Decision | Books Review Ref |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |

None。Evidence-stage owner 与建议路由已写入 date-local frozen queue；最终 Books disposition 必须由 root 按日期串行对读目标章、相邻章与既有命题。

## 7. Semantic Audit

<!-- validator:semantic-audit-v1 -->
| Audit ID | Auditor | Scope | Reviewed Refs | Findings | Resolution | Status |
| --- | --- | --- | --- | --- | --- | --- |
| SA-20260714-COVERAGE-INDEPENDENT | fresh-context:pending-root-auditor | coverage | coverage:SRC-ARXIV:20260714 | GAP-20260714-COVERAGE-INDEPENDENT：965 项判断尚未被独立 reviewer 逐项反向审计 | Pending — 全量检查 false positive / false negative 并绑定具体 family | open |
| SA-20260714-EVIDENCE-INDEPENDENT | fresh-context:pending-root-auditor | evidence | validator:review-completion-v1 | GAP-20260714-EVIDENCE-INDEPENDENT：103 个 RP 尚需独立核验 claim scope、locator 与 artifact boundary | Pending — 对照 exact v1；发现问题则只重开具体 family | open |
| SA-20260714-SELECTION-INDEPENDENT | fresh-context:pending-root-auditor | deep_analysis_selection | validator:deep-analysis-selection-v1 | GAP-20260714-SELECTION-INDEPENDENT：61 个 eligible family 的三项选择尚需 adversarial comparison | Pending — 比较系统影响、反证优先级与 owner 独立性 | open |
| SA-20260714-BOOKS-ROOT | fresh-context:pending-root-books-owner | books | validator:books-comparison-v1 | GAP-20260714-BOOKS-ROOT：103 项尚未逐一对读 Books | Pending — root sequential owner 消费 frozen queue | open |

## 8. Ignored Noise

862 项在 title + 完整 abstract 阶段获得 family-specific closure，均保存在 `fresh-context-semantic-decisions-v2.1.json.gz`；未静默删除，也未接受不适用的 Score V2。

- `embodied_task_local_method`：80
- `incremental_method_without_durable_system_delta`：638
- `local_benchmark_without_release_delta`：24
- `prior_retained_candidate`：7
- `theory_without_ai_system_contract`：16
- `vertical_application_without_system_delta`：97

## 9. Recommended Action

1. 独立 reviewer 先审 Coverage、Evidence 与 Deep Selection；finding 必须绑定并重开具体 family。
2. root 再逐项比较 Books。建议起点：Integrate 44、No Change 58、Structural Candidate 1；它们不是最终决定。

## 10. Repository Changes

- 重建 `papers/2026/07/14/README.md`，以 965→103 frozen denominator 替换旧内部不一致报告。
- 新增 date-local frozen Books queue，并更新 7 月月级队列的 7 月 14 日条目。
- 未修改 Books、ROADMAP、docs、Learning State、Weekly 或共享 validator。

## 11. Open Questions

- 独立 false-negative audit 是否会从 862 个 closure 中恢复新 family？
- proposed Integrate 是否已被 Books 中相同命题覆盖？
- 两个 PDF fallback 的 HTML 若后续恢复，locator 是否需迁回稳定 HTML anchor？

## 12. Sources

- [Format Sensitivity Index: Token-Controlled Prompt Wrapper Robustness and Schema Compliance in LLM Benchmarking](https://arxiv.org/html/2607.09665v1) — first-public（Asia/Shanghai）：2026-07-14；exact evidence：v1；accessed：2026-09-04
- [AuditWeave: A Tamper-Evident, Auditor-Navigable Evidence Layer for AI-Assisted and Data-Transformation Workflows](https://arxiv.org/html/2607.09682v1) — first-public（Asia/Shanghai）：2026-07-14；exact evidence：v1；accessed：2026-09-04
- [MawForge: Memory-Bounded Expert Materialization for Local Mixture-of-Experts Inference](https://arxiv.org/html/2607.09686v1) — first-public（Asia/Shanghai）：2026-07-14；exact evidence：v1；accessed：2026-09-04
- [Evidence-Aware MapReduce for Forkable Compute](https://arxiv.org/html/2607.09689v1) — first-public（Asia/Shanghai）：2026-07-14；exact evidence：v1；accessed：2026-09-04
- [What Context Does a Coding Agent Actually Need to Act?](https://arxiv.org/html/2607.09691v1) — first-public（Asia/Shanghai）：2026-07-14；exact evidence：v1；accessed：2026-09-04
- [Reference-Based Distillation Detection in LLMs](https://arxiv.org/html/2607.09692v1) — first-public（Asia/Shanghai）：2026-07-14；exact evidence：v1；accessed：2026-09-04
- [Safe responses matter: Output-aware safety guardrail mitigate over-refusal in MLLMs](https://arxiv.org/html/2607.09697v1) — first-public（Asia/Shanghai）：2026-07-14；exact evidence：v1；accessed：2026-09-04
- [The Verifier is the Curriculum: Execution-Gated Self-Distillation for Cross-Family Game Generation](https://arxiv.org/html/2607.09709v1) — first-public（Asia/Shanghai）：2026-07-14；exact evidence：v1；accessed：2026-09-04
- [EvoClawBench: Can Agents Learn Reusable Skills from Their Own Runs?](https://arxiv.org/html/2607.09711v1) — first-public（Asia/Shanghai）：2026-07-14；exact evidence：v1；accessed：2026-09-04
- [A Theory of Least Autonomy in AI](https://arxiv.org/html/2607.09744v1) — first-public（Asia/Shanghai）：2026-07-14；exact evidence：v1；accessed：2026-09-04
- [Replicating Belief, Not Bits: Epistemic State Replication for Agentic Systems](https://arxiv.org/html/2607.09748v1) — first-public（Asia/Shanghai）：2026-07-14；exact evidence：v1；accessed：2026-09-04
- [ReflectWorld-MM: An Entity-Oriented Multimodal Memory System for Open-Ended Video Streams](https://arxiv.org/html/2607.09759v1) — first-public（Asia/Shanghai）：2026-07-14；exact evidence：v1；accessed：2026-09-04
- [Verification of Adaptive Agentic Controllers through Finite Rule Revision](https://arxiv.org/html/2607.09770v1) — first-public（Asia/Shanghai）：2026-07-14；exact evidence：v1；accessed：2026-09-04
- [EvoCUA-1.5: Online Reinforcement Learning for Multi-turn Computer-Use Agents](https://arxiv.org/html/2607.09773v1) — first-public（Asia/Shanghai）：2026-07-14；exact evidence：v1；accessed：2026-09-04
- [HELP: Human-Efficient Large-Scale Robot Post-Training with Rollout Segmentation](https://arxiv.org/html/2607.09776v1) — first-public（Asia/Shanghai）：2026-07-14；exact evidence：v1；accessed：2026-09-04
- [Length Penalties Make Chain-of-Thought Less Monitorable](https://arxiv.org/html/2607.09786v1) — first-public（Asia/Shanghai）：2026-07-14；exact evidence：v1；accessed：2026-09-04
- [Gauge dependence and structured-output corruption in sign-branched repetition penalties: measurements across models, inference stacks, and alternative repetition controls](https://arxiv.org/html/2607.09791v1) — first-public（Asia/Shanghai）：2026-07-14；exact evidence：v1；accessed：2026-09-04
- [Agentic Context Learning with Self-Discovered Specification](https://arxiv.org/html/2607.09794v1) — first-public（Asia/Shanghai）：2026-07-14；exact evidence：v1；accessed：2026-09-04
- [Auditing Invisible Weight Updates with Reference Traces](https://arxiv.org/html/2607.09800v1) — first-public（Asia/Shanghai）：2026-07-14；exact evidence：v1；accessed：2026-09-04
- [Quota Marketplace: Dynamic Pricing for Efficient Allocation of ML Training Resources](https://arxiv.org/html/2607.09802v1) — first-public（Asia/Shanghai）：2026-07-14；exact evidence：v1；accessed：2026-09-04
- [Spectral Origins of the Self-Correction Blind Spot in Autoregressive Generation](https://arxiv.org/html/2607.09803v1) — first-public（Asia/Shanghai）：2026-07-14；exact evidence：v1；accessed：2026-09-04
- [Trivial Prompt Reframing Bypasses Safety Guardrails in Googleś MedGemma-4B](https://arxiv.org/html/2607.09804v1) — first-public（Asia/Shanghai）：2026-07-14；exact evidence：v1；accessed：2026-09-04
- [Memory-Conditioned Tool Calling for Camera-First Visual Agents](https://arxiv.org/html/2607.09822v1) — first-public（Asia/Shanghai）：2026-07-14；exact evidence：v1；accessed：2026-09-04
- [Remembering Distinct Items, Not Tokens: A Learnable Dirichlet-Process Cache Between State-Space Models and Attention](https://arxiv.org/html/2607.09889v1) — first-public（Asia/Shanghai）：2026-07-14；exact evidence：v1；accessed：2026-09-04
- [Trusted Floors Under Untrusted Learners: A Runtime Assured-SLO Guard for ML Serving](https://arxiv.org/html/2607.09992v1) — first-public（Asia/Shanghai）：2026-07-14；exact evidence：v1；accessed：2026-09-04
- [Who&amp;When Pro: Can LLMs Really Attribute Failures in AI Agents?](https://arxiv.org/html/2607.09996v1) — first-public（Asia/Shanghai）：2026-07-14；exact evidence：v1；accessed：2026-09-04
- [Silent Failures in Quantized LLM Reasoning: A Taxonomy-Based Analysis of Hollow Convergence and Failure Mode Shifts](https://arxiv.org/pdf/2607.09999v1) — first-public（Asia/Shanghai）：2026-07-14；exact evidence：v1；accessed：2026-09-04
- [FlashTrie: A GPU-Accelerated Constrained Beam Search for Generative Retrieval](https://arxiv.org/html/2607.10044v1) — first-public（Asia/Shanghai）：2026-07-14；exact evidence：v1；accessed：2026-09-04
- [AgentAbstain: Do LLM Agents Know When Not to Act?](https://arxiv.org/html/2607.10059v1) — first-public（Asia/Shanghai）：2026-07-14；exact evidence：v1；accessed：2026-09-04
- [MAG: A Web-Agent Benchmark and Harness for Multimodal Action and Guide Generation](https://arxiv.org/html/2607.10079v1) — first-public（Asia/Shanghai）：2026-07-14；exact evidence：v1；accessed：2026-09-04
- [Scaling and Stabilizing Large-Scale Embedding-Based Retrieval](https://arxiv.org/html/2607.10096v1) — first-public（Asia/Shanghai）：2026-07-14；exact evidence：v1；accessed：2026-09-04
- [LLM Watermarking as Big Data Provenance: A Deployment-Oriented Systematization](https://arxiv.org/html/2607.10103v1) — first-public（Asia/Shanghai）：2026-07-14；exact evidence：v1；accessed：2026-09-04
- [CHASE: Cache-Hole-Adapted Skip Exit for Looped State-Space Language Models](https://arxiv.org/html/2607.10110v1) — first-public（Asia/Shanghai）：2026-07-14；exact evidence：v1；accessed：2026-09-04
- [LLMs as a Jury: Cross-Model Consensus Can Outperform Process Reward Models for LLM Reasoning](https://arxiv.org/html/2607.10139v1) — first-public（Asia/Shanghai）：2026-07-14；exact evidence：v1；accessed：2026-09-04
- [Consensus as Collapse Policy: Communication Evidence, Horizons, and Prefix Decisions](https://arxiv.org/html/2607.10152v1) — first-public（Asia/Shanghai）：2026-07-14；exact evidence：v1；accessed：2026-09-04
- [Automated Tensor Scheduling for Hybrid CPU-GPU LLM Inference on Consumer Devices](https://arxiv.org/html/2607.10183v1) — first-public（Asia/Shanghai）：2026-07-14；exact evidence：v1；accessed：2026-09-04
- [FlashAccel: Leveraging High-Bandwidth Flash (HBF) for High-Throughput LLM Inference](https://arxiv.org/html/2607.10186v1) — first-public（Asia/Shanghai）：2026-07-14；exact evidence：v1；accessed：2026-09-04
- [Equal Accuracy, Unequal Evidence: Search APIs as Decision Surfaces for Tool-Using Agents](https://arxiv.org/html/2607.10198v1) — first-public（Asia/Shanghai）：2026-07-14；exact evidence：v1；accessed：2026-09-04
- [Adaptive Compute in Latent World Models: When Depth Helps, Hurts, or Doesn't Matter](https://arxiv.org/html/2607.10203v1) — first-public（Asia/Shanghai）：2026-07-14；exact evidence：v1；accessed：2026-09-04
- [When Are Sparse Feature Interventions Actually Localized? Matched Evaluation for SAE-Based Safety Control](https://arxiv.org/html/2607.10226v1) — first-public（Asia/Shanghai）：2026-07-14；exact evidence：v1；accessed：2026-09-04
- [What Does Your Short-Answer VQA Score Actually Measure? Evaluator-Dependent Instability in Multimodal Short-Answer Benchmarks](https://arxiv.org/html/2607.10240v1) — first-public（Asia/Shanghai）：2026-07-14；exact evidence：v1；accessed：2026-09-04
- [One Token Is Enough: Fingerprinting and Verifying Large Language Models from Single-Token Output Distributions](https://arxiv.org/html/2607.10252v1) — first-public（Asia/Shanghai）：2026-07-14；exact evidence：v1；accessed：2026-09-04
- [TGMS: An Agent-Native Bi-Temporal Graph Management System](https://arxiv.org/html/2607.10265v1) — first-public（Asia/Shanghai）：2026-07-14；exact evidence：v1；accessed：2026-09-04
- [Partial Contracts Suffice: Sound, LLM-Inferred Regression Verification](https://arxiv.org/html/2607.10291v1) — first-public（Asia/Shanghai）：2026-07-14；exact evidence：v1；accessed：2026-09-04
- [ABot-AgentOS: A General Robotic Agent OS with Lifelong Multi-modal Memory](https://arxiv.org/html/2607.10350v1) — first-public（Asia/Shanghai）：2026-07-14；exact evidence：v1；accessed：2026-09-04
- [A Control Theory of Predictability in Latent World Models](https://arxiv.org/html/2607.10362v1) — first-public（Asia/Shanghai）：2026-07-14；exact evidence：v1；accessed：2026-09-04
- [Stateful Worlds, Stateless Elasticity: Exact-State Serving for Interactive World Models](https://arxiv.org/html/2607.10389v1) — first-public（Asia/Shanghai）：2026-07-14；exact evidence：v1；accessed：2026-09-04
- [GRASP: GRanularity-Aware Search Policy for Agentic RAG](https://arxiv.org/html/2607.10463v1) — first-public（Asia/Shanghai）：2026-07-14；exact evidence：v1；accessed：2026-09-04
- [EvidentialRAG: Quantifying and Mitigating Information Conflict in Multi-Source Retrieval-Augmented Generation via Evidential Deep Learning](https://arxiv.org/html/2607.10491v1) — first-public（Asia/Shanghai）：2026-07-14；exact evidence：v1；accessed：2026-09-04
- [MemDecay: Region-Aware KV Cache Eviction for Efficient LLM Agent Inference](https://arxiv.org/html/2607.10582v1) — first-public（Asia/Shanghai）：2026-07-14；exact evidence：v1；accessed：2026-09-04
- [Unlocking Parallelism in Autoregressive Language Models via Speculative Decoding with Progressive Tree Drafting](https://arxiv.org/html/2607.10661v1) — first-public（Asia/Shanghai）：2026-07-14；exact evidence：v1；accessed：2026-09-04
- [PromptGraph: Graph-Guided Prompt Sanitization for Balancing Privacy and Utility in LLM Inference](https://arxiv.org/html/2607.10709v1) — first-public（Asia/Shanghai）：2026-07-14；exact evidence：v1；accessed：2026-09-04
- [Distributed Denial of Science: How Indirect Data Poisoning of AI Systems Can Industrialize Scientific Fraud](https://arxiv.org/html/2607.10712v1) — first-public（Asia/Shanghai）：2026-07-14；exact evidence：v1；accessed：2026-09-04
- [Filtering Harmful Actions Isn't Enough: Phantom Transfer in Agentic SDF](https://arxiv.org/html/2607.10750v1) — first-public（Asia/Shanghai）：2026-07-14；exact evidence：v1；accessed：2026-09-04
- [Trust Before Fusion: QIMG-7 and Source-Aware Resolution for Polluted Multimodal RAG](https://arxiv.org/html/2607.10798v1) — first-public（Asia/Shanghai）：2026-07-14；exact evidence：v1；accessed：2026-09-04
- [Reliability Scaling Laws for Quantized Large Language Models](https://arxiv.org/html/2607.10855v1) — first-public（Asia/Shanghai）：2026-07-14；exact evidence：v1；accessed：2026-09-04
- [WSqD: A Horizon-Free Learning Rate Schedule for Large Model Training](https://arxiv.org/html/2607.10959v1) — first-public（Asia/Shanghai）：2026-07-14；exact evidence：v1；accessed：2026-09-04
- [[AAFLOW+] Stateful Operator Abstraction with Zero-Copy Distributed KV Cache Orchestration for Multi-Agent Workflows](https://arxiv.org/html/2607.10987v1) — first-public（Asia/Shanghai）：2026-07-14；exact evidence：v1；accessed：2026-09-04
- [MJ: Multi-turn LLM Jailbreaking via Decomposed Credit Assignment](https://arxiv.org/html/2607.11070v1) — first-public（Asia/Shanghai）：2026-07-14；exact evidence：v1；accessed：2026-09-04
- [Are LLMs Ready for Scientific Discovery? A Capability-Oriented Benchmark for AI Scientists](https://arxiv.org/html/2607.11079v1) — first-public（Asia/Shanghai）：2026-07-14；exact evidence：v1；accessed：2026-09-04
- [Rethinking MCP Security: A Large-Scale Study of Runtime MCP Servers and Security Scanner Reliability](https://arxiv.org/html/2607.11086v1) — first-public（Asia/Shanghai）：2026-07-14；exact evidence：v1；accessed：2026-09-04
- [TIGER: Text-Conditioned Visual Gated Routing with Acceptance Alignment for Multimodal Speculative Decoding](https://arxiv.org/html/2607.11131v1) — first-public（Asia/Shanghai）：2026-07-14；exact evidence：v1；accessed：2026-09-04
- [Xema: Efficient Diffusion Serving through Fine-Grained Memory Management and Auto-Configuration](https://arxiv.org/html/2607.11136v1) — first-public（Asia/Shanghai）：2026-07-14；exact evidence：v1；accessed：2026-09-04
- [A Formal Hierarchical Architecture for Agentic Orchestration with Stack-Based Execution and Lazy Discovery](https://arxiv.org/html/2607.11138v1) — first-public（Asia/Shanghai）：2026-07-14；exact evidence：v1；accessed：2026-09-04
- [The Hidden Footprint: Making Storage a First-Class Metric for LLM Agent Evaluation](https://arxiv.org/html/2607.11149v1) — first-public（Asia/Shanghai）：2026-07-14；exact evidence：v1；accessed：2026-09-04
- [STAMP: Provenance-Guided Credit Assignment for Deep Search Agents](https://arxiv.org/html/2607.11172v1) — first-public（Asia/Shanghai）：2026-07-14；exact evidence：v1；accessed：2026-09-04
- [Amplitude-Only FFN Intervention for Tool-Structured LLM Inference Method: Gated Evaluation Protocol, and Cross-Model Empirical Results](https://arxiv.org/pdf/2607.11183v1) — first-public（Asia/Shanghai）：2026-07-14；exact evidence：v1；accessed：2026-09-04
- [Heterogeneous Agent Cohorts for Safe Open-Ended Exploration with Runtime Constraint Memory](https://arxiv.org/html/2607.11226v1) — first-public（Asia/Shanghai）：2026-07-14；exact evidence：v1；accessed：2026-09-04
- [Multi-Agent LLMs Fail to Explore Each Other](https://arxiv.org/html/2607.11250v1) — first-public（Asia/Shanghai）：2026-07-14；exact evidence：v1；accessed：2026-09-04
- [GPU-Tile-Sim: A Tile-Centric GPU Simulation Framework for LLM Hardware-Software Co-Design](https://arxiv.org/html/2607.11262v1) — first-public（Asia/Shanghai）：2026-07-14；exact evidence：v1；accessed：2026-09-04
- [Calibrated e-CUSUM Decoding for Quantized Reasoning Models: Why Token Log-Probability Is the Wrong Observable for Decoding Monitors](https://arxiv.org/html/2607.11317v1) — first-public（Asia/Shanghai）：2026-07-14；exact evidence：v1；accessed：2026-09-04
- [Compile, Then Page: Executable SOP Programs and a Capability-Gated Runtime for Procedural LLM Agents](https://arxiv.org/html/2607.11346v1) — first-public（Asia/Shanghai）：2026-07-14；exact evidence：v1；accessed：2026-09-04
- [Decomposing Runtime, Kernel, and Quantization Speedups via a Matched FP16 Intermediate: A Hardware-Conditioned Case Study on Four NVIDIA RTX A5000 GPUs](https://arxiv.org/html/2607.11368v1) — first-public（Asia/Shanghai）：2026-07-14；exact evidence：v1；accessed：2026-09-04
- [StructAgent: Harness Long-horizon Digital Agents with Unified Causal Structure](https://arxiv.org/html/2607.11388v1) — first-public（Asia/Shanghai）：2026-07-14；exact evidence：v1；accessed：2026-09-04
- [Agentic Routing: The Harness-Native Data Flywheel](https://arxiv.org/html/2607.11399v1) — first-public（Asia/Shanghai）：2026-07-14；exact evidence：v1；accessed：2026-09-04
- [Confidently Wrong: Detecting Hallucinations in Financial Question Answering from LLM Internal States](https://arxiv.org/html/2607.11414v1) — first-public（Asia/Shanghai）：2026-07-14；exact evidence：v1；accessed：2026-09-04
- [ToFu: A White-Box, Token-Efficient Agent Harness for Researchers](https://arxiv.org/html/2607.11423v1) — first-public（Asia/Shanghai）：2026-07-14；exact evidence：v1；accessed：2026-09-04
- [Omni-Decision: A Progressive Evidence-State Agent System for Omni-Modal QA](https://arxiv.org/html/2607.11433v1) — first-public（Asia/Shanghai）：2026-07-14；exact evidence：v1；accessed：2026-09-04
- [The Ebb and Flow of Multimodal Focus: Scheduling Visual Relay Windows for Grounded VLM Reasoning](https://arxiv.org/html/2607.11436v1) — first-public（Asia/Shanghai）：2026-07-14；exact evidence：v1；accessed：2026-09-04
- [UMoE:Unlocking Every Expert in Domain-Specific Training](https://arxiv.org/html/2607.11444v1) — first-public（Asia/Shanghai）：2026-07-14；exact evidence：v1；accessed：2026-09-04
- [HyperSafe: Inference-Time Safety Recovery for Fine-Tuned Language Models](https://arxiv.org/html/2607.11475v1) — first-public（Asia/Shanghai）：2026-07-14；exact evidence：v1；accessed：2026-09-04
- [LightMem-Ego: Your AI Memory for Everyday Life](https://arxiv.org/html/2607.11487v1) — first-public（Asia/Shanghai）：2026-07-14；exact evidence：v1；accessed：2026-09-04
- [See like a Robot: Robot-Centric Pointmaps for Vision-Language-Action Models](https://arxiv.org/html/2607.11498v1) — first-public（Asia/Shanghai）：2026-07-14；exact evidence：v1；accessed：2026-09-04
- [Proxy OPD: On-Policy Distillation with Transferable Relative Proxy Update](https://arxiv.org/html/2607.11505v1) — first-public（Asia/Shanghai）：2026-07-14；exact evidence：v1；accessed：2026-09-04
- [SCOPE-RL: Optimizing Reasoning Paths Before and After Success](https://arxiv.org/html/2607.11506v1) — first-public（Asia/Shanghai）：2026-07-14；exact evidence：v1；accessed：2026-09-04
- [MemExchange: Utility-Driven Distributed Memory Reallocation for Multi-Tenant Datacenters](https://arxiv.org/html/2607.11579v1) — first-public（Asia/Shanghai）：2026-07-14；exact evidence：v1；accessed：2026-09-04
- [HCRMap: Pressure-Aware Hot-Expert Residency Mapping for 3.5D MoE Chiplet Inference](https://arxiv.org/html/2607.11586v1) — first-public（Asia/Shanghai）：2026-07-14；exact evidence：v1；accessed：2026-09-04
- [Interaction Scaling: Grounding the Third Axis of Test-Time Compute](https://arxiv.org/html/2607.11598v1) — first-public（Asia/Shanghai）：2026-07-14；exact evidence：v1；accessed：2026-09-04
- [Mizzle: A Complete Concurrent Incorrectness Logic for Preventing False Alarms in Agentic Bug Finding](https://arxiv.org/html/2607.11611v1) — first-public（Asia/Shanghai）：2026-07-14；exact evidence：v1；accessed：2026-09-04
- [Extending LLM Context via Associative Recurrent Memory](https://arxiv.org/html/2607.11614v1) — first-public（Asia/Shanghai）：2026-07-14；exact evidence：v1；accessed：2026-09-04
- [Xiaomi-Robotics-U0: Unified Embodied Synthesis with World Foundation Model](https://arxiv.org/html/2607.11643v1) — first-public（Asia/Shanghai）：2026-07-14；exact evidence：v1；accessed：2026-09-04
- [ABot-3DWorld 0: A Universal World Model to Explore Any 3D Space](https://arxiv.org/html/2607.11673v1) — first-public（Asia/Shanghai）：2026-07-14；exact evidence：v1；accessed：2026-09-04
- [Agent Hacks Agent: Autoresearch for Production-Agent Red-Teaming](https://arxiv.org/html/2607.11698v1) — first-public（Asia/Shanghai）：2026-07-14；exact evidence：v1；accessed：2026-09-04
- [Qwen-Audio-VAE Technical Report](https://arxiv.org/html/2607.11738v1) — first-public（Asia/Shanghai）：2026-07-14；exact evidence：v1；accessed：2026-09-04
- [HiFi-LLP: High-Fidelity, Low-Cost Latency Predictors with Confidence for Robust HW-NAS](https://arxiv.org/html/2607.11746v1) — first-public（Asia/Shanghai）：2026-07-14；exact evidence：v1；accessed：2026-09-04
- [When Local Monitors Miss Compositional Harm: Diagnosing Distributed Backdoors in Multi-Agent Systems](https://arxiv.org/html/2607.11751v1) — first-public（Asia/Shanghai）：2026-07-14；exact evidence：v1；accessed：2026-09-04
- [An Exact Instrument for State Usage in Selective State-Space Models, and the Input-Driven Migration It Reveals](https://arxiv.org/html/2607.11796v1) — first-public（Asia/Shanghai）：2026-07-14；exact evidence：v1；accessed：2026-09-04
- [MM-ToolSandBox: A Unified Framework for Evaluating Visual Tool-Calling Agents](https://arxiv.org/html/2607.11818v1) — first-public（Asia/Shanghai）：2026-07-14；exact evidence：v1；accessed：2026-09-04
- [Cycle-World: Mitigating Error Accumulation in Long-term Video World Models via Reverse-Prediction Cycle Consistency](https://arxiv.org/html/2607.11836v1) — first-public（Asia/Shanghai）：2026-07-14；exact evidence：v1；accessed：2026-09-04
- [Evidence-Backed Video Question Answering](https://arxiv.org/html/2607.11862v1) — first-public（Asia/Shanghai）：2026-07-14；exact evidence：v1；accessed：2026-09-04
- [Inside the Unfair Judge: A Mechanistic Interpretability Account of LLM-as-Judge Bias](https://arxiv.org/html/2607.11871v1) — first-public（Asia/Shanghai）：2026-07-14；exact evidence：v1；accessed：2026-09-04
- [Requential Coding: Pushing the Limits of Model Compression with Self-Generated Training Data](https://arxiv.org/html/2607.11883v1) — first-public（Asia/Shanghai）：2026-07-14；exact evidence：v1；accessed：2026-09-04
- [Read It Back: Pretrained MLLMs Are Zero-Shot Reward Models for Text-to-Image Generation](https://arxiv.org/html/2607.11886v1) — first-public（Asia/Shanghai）：2026-07-14；exact evidence：v1；accessed：2026-09-04

## 13. Final Status

Author-side Coverage screening、denominator、exact-v1 access、103/103 Source Review 与 61-family Deep Selection receipt 已构建；Books 写回冻结，四项独立 Semantic Audit 尚未完成。

State Truth: Completion=In Progress；Coverage=Open；Evidence=Open；Books=Open；Unresolved Findings=4。
