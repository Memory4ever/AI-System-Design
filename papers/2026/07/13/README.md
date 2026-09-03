# Daily Research — 2026-07-13

**Research Date:** 2026-07-13

**Timezone:** Asia/Shanghai

**Strict Window:** 2026-07-12 09:00:00 ～ 2026-07-13 09:00:00（北京时间，左闭右开）

**Contract:** V2.1 Full Replay；Historical Daily 独立重建，不使用 Weekly 作为 discovery、评分或 Review 来源

**Status:** In Progress；Coverage=Open、Evidence=Open、Books=Open；author-side evidence 已闭合，等待独立 Semantic Audit 与 root Books 比较

## Executive Summary

本窗口从官方 arXiv first-public owner inventory 枚举 **337** 个唯一 identity；逐项读取 title 与完整 abstract 后，冻结为 **62** 个候选，**275** 个 family-specific pre-denominator closure，retain rate 为 **18.40%**。候选随后全部取得 exact v1：62/62 已完成非模板化 Source Review，其中 Deep 42、Standard 20、blocked 0。

本次修正了两个重要 provenance 问题：`2607.08974` 不再沿用 metadata-only 低估，而按 exact v1 的 VLM-to-VLA 机制进入 Deep Review；`2607.09306` 只审阅首发 v1 的 companion-memory lifecycle，明确隔离 7 月 30 日实质改题的 v3，后者不能倒灌首发窗口。

这仍不是 Complete：本泳道没有 Books 写权限，62 项 Books disposition 暂为 `Not Assessed`；Coverage、Evidence、Deep Selection 与 Books 四项 fresh-context Semantic Audit 也必须由未参与主要写作的 reviewer 完成。

## 1. Coverage

<!-- validator:report-metadata-v2 -->
| Field | Value |
| --- | --- |
| Contract Version | V2.1 |
| Score Schema | V2 |
| Report Type | Daily |
| Window Start | 2026-07-13 |
| Window End | 2026-07-13 |
| Registry Version | 2026-08-25 |
| Coverage Mode | Full Replay |
| Baseline Report | — |
| Changed Source IDs | — |
| Previous Denominator ID | — |
| Denominator ID | daily-2026-07-13-0900-v2.1-sha256:a568ddad8a536593663e2949fd55817d6d3264f5bc0ee5e1c54dda8ffa93083e |
| Denominator Frozen At | 2026-09-03T16:40:00+08:00 |
| Completion Status | In Progress |
| Coverage Gate | Open |
| Evidence Gate | Open |
| Books Gate | Open |

### Source Coverage Receipt

<!-- coverage:SRC-ARXIV:20260713:start -->
<!-- validator:source-coverage-v2 -->
| Source ID | Window Start | Window End | Executed At | Endpoint / Filter | Result | Hits | Candidate Source Families | Pagination / Cursor | Window Watermark | Closure Evidence | Gap / Limitation ID |
| --- | --- | --- | --- | --- | --- | ---: | --- | --- | --- | --- | --- |
| SRC-ARXIV | 2026-07-12T09:00:00+08:00 | 2026-07-13T09:00:00+08:00 | 2026-09-03T16:40:00+08:00 | official arXiv monthly category listings; v1 submission history; availability schedule; DataCite DOI created used only to reconcile announcement cycle | checked | 337 | SF-2026-ARXIV-2607-08774;SF-2026-ARXIV-2607-08780;SF-2026-ARXIV-2607-08782;SF-2026-ARXIV-2607-08786;SF-2026-ARXIV-2607-08839;SF-2026-ARXIV-2607-08857;SF-2026-ARXIV-2607-08877;SF-2026-ARXIV-2607-08883;SF-2026-ARXIV-2607-08894;SF-2026-ARXIV-2607-08925;SF-2026-ARXIV-2607-08930;SF-2026-ARXIV-2607-08938;SF-2026-ARXIV-2607-08940;SF-2026-ARXIV-2607-08948;SF-2026-ARXIV-2607-08949;SF-2026-ARXIV-2607-08961;SF-2026-ARXIV-2607-08964;SF-2026-ARXIV-2607-08973;SF-2026-ARXIV-2607-08974;SF-2026-ARXIV-2607-08991;SF-2026-ARXIV-2607-08993;SF-2026-ARXIV-2607-09015;SF-2026-ARXIV-2607-09016;SF-2026-ARXIV-2607-09024;SF-2026-ARXIV-2607-09029;SF-2026-ARXIV-2607-09042;SF-2026-ARXIV-2607-09052;SF-2026-ARXIV-2607-09053;SF-2026-ARXIV-2607-09065;SF-2026-ARXIV-2607-09072;SF-2026-ARXIV-2607-09091;SF-2026-ARXIV-2607-09092;SF-2026-ARXIV-2607-09123;SF-2026-ARXIV-2607-09153;SF-2026-ARXIV-2607-09156;SF-2026-ARXIV-2607-09172;SF-2026-ARXIV-2607-09175;SF-2026-ARXIV-2607-09185;SF-2026-ARXIV-2607-09195;SF-2026-ARXIV-2607-09207;SF-2026-ARXIV-2607-09217;SF-2026-ARXIV-2607-09218;SF-2026-ARXIV-2607-09236;SF-2026-ARXIV-2607-09266;SF-2026-ARXIV-2607-09306;SF-2026-ARXIV-2607-09328;SF-2026-ARXIV-2607-09349;SF-2026-ARXIV-2607-09366;SF-2026-ARXIV-2607-09385;SF-2026-ARXIV-2607-09415;SF-2026-ARXIV-2607-09492;SF-2026-ARXIV-2607-09493;SF-2026-ARXIV-2607-09510;SF-2026-ARXIV-2607-09520;SF-2026-ARXIV-2607-09532;SF-2026-ARXIV-2607-09553;SF-2026-ARXIV-2607-09560;SF-2026-ARXIV-2607-09586;SF-2026-ARXIV-2607-09590;SF-2026-ARXIV-2607-09600;SF-2026-ARXIV-2607-09603;SF-2026-ARXIV-2607-09661 | all registered category pages, show=2000; cross-category identity dedup complete | 2026-07-13T09:00:00+08:00 | sha256:a568ddad8a536593663e2949fd55817d6d3264f5bc0ee5e1c54dda8ffa93083e | — |
<!-- coverage:SRC-ARXIV:20260713:end -->

### Coverage Limitations

- 当前 `official-arxiv-first-public-owner-receipt-v1.json` 专门记录旧 4 项候选的 owner 移动；完整 337 项的 canonical owner truth 在 raw inventory 与全局 owner reconciliation 中，不得把该 4 项收据误读成当日分母。
- DataCite 只用于 identity/date 交叉检验；技术 claim 全部回到 exact arXiv v1 HTML。
- Coverage 的 author-side receipt 已闭合，但独立 false-positive / false-negative Semantic Audit 尚未签收，因此 Coverage Gate 保持 Open。

## 2. Candidate Ledger

<!-- validator:candidate-ledger-v2.1 -->
| Source Family ID | Primary Identifier | Event Identity | Owner Week | First-public Date | Supporting Source IDs | Design Delta | System Reach | Durability | Total | Candidate State | Review Status | Access Status | Review Override | Review Ref | Owner Report Ref | Prior Review Ref | Reconciliation | Stable Node ID | Books Disposition | Books Review Ref | Benchmark Claim |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2607-08774 | arXiv:2607.08774v1 | paper-v1:2607.08774 | 2026-W29 | 2026-07-13 | SRC-ARXIV | 3 | 2 | 2 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-08774 | self | — | new_in_window | AGENT-PLATFORM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-08780 | arXiv:2607.08780v1 | paper-v1:2607.08780 | 2026-W29 | 2026-07-13 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-08780 | self | — | new_in_window | MODEL-MOE | Not Assessed | — | no |
| SF-2026-ARXIV-2607-08782 | arXiv:2607.08782v1 | paper-v1:2607.08782 | 2026-W29 | 2026-07-13 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-08782 | self | — | new_in_window | INFER-SCHEDULING | Not Assessed | — | no |
| SF-2026-ARXIV-2607-08786 | arXiv:2607.08786v1 | paper-v1:2607.08786 | 2026-W29 | 2026-07-13 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-08786 | self | — | new_in_window | INFER-TENSORRT-LLM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-08839 | arXiv:2607.08839v1 | paper-v1:2607.08839 | 2026-W29 | 2026-07-13 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-08839 | self | — | new_in_window | MULTIMODAL-REPRESENTATION | Not Assessed | — | no |
| SF-2026-ARXIV-2607-08857 | arXiv:2607.08857v1 | paper-v1:2607.08857 | 2026-W29 | 2026-07-13 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-08857 | self | — | new_in_window | MULTIMODAL-EMBODIED-VLA | Not Assessed | — | no |
| SF-2026-ARXIV-2607-08877 | arXiv:2607.08877v1 | paper-v1:2607.08877 | 2026-W29 | 2026-07-13 | SRC-ARXIV | 3 | 2 | 2 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-08877 | self | — | new_in_window | MULTIMODAL-EMBODIED-VLA | Not Assessed | — | no |
| SF-2026-ARXIV-2607-08883 | arXiv:2607.08883v1 | paper-v1:2607.08883 | 2026-W29 | 2026-07-13 | SRC-ARXIV | 3 | 2 | 2 | 7 | retained | deep_complete | accessible | release_security_contract | review:SF-2026-ARXIV-2607-08883 | self | — | new_in_window | PLATFORM-SECURITY | Not Assessed | — | no |
| SF-2026-ARXIV-2607-08894 | arXiv:2607.08894v1 | paper-v1:2607.08894 | 2026-W29 | 2026-07-13 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-08894 | self | — | new_in_window | AGENT-PLANNING | Not Assessed | — | no |
| SF-2026-ARXIV-2607-08925 | arXiv:2607.08925v1 | paper-v1:2607.08925 | 2026-W29 | 2026-07-13 | SRC-ARXIV | 3 | 2 | 2 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-08925 | self | — | new_in_window | TRAIN-PPO | Not Assessed | — | no |
| SF-2026-ARXIV-2607-08930 | arXiv:2607.08930v1 | paper-v1:2607.08930 | 2026-W29 | 2026-07-13 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-08930 | self | — | new_in_window | INFER-CONTINUOUS-BATCHING | Not Assessed | — | no |
| SF-2026-ARXIV-2607-08938 | arXiv:2607.08938v1 | paper-v1:2607.08938 | 2026-W29 | 2026-07-13 | SRC-ARXIV | 3 | 2 | 2 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-08938 | self | — | new_in_window | AGENT-PLATFORM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-08940 | arXiv:2607.08940v1 | paper-v1:2607.08940 | 2026-W29 | 2026-07-13 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-08940 | self | — | new_in_window | MULTIMODAL-REPRESENTATION | Not Assessed | — | no |
| SF-2026-ARXIV-2607-08948 | arXiv:2607.08948v1 | paper-v1:2607.08948 | 2026-W29 | 2026-07-13 | SRC-ARXIV | 3 | 2 | 2 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-08948 | self | — | new_in_window | MULTIMODAL-EMBODIED-VLA | Not Assessed | — | no |
| SF-2026-ARXIV-2607-08949 | arXiv:2607.08949v1 | paper-v1:2607.08949 | 2026-W29 | 2026-07-13 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-08949 | self | — | new_in_window | AGENT-TOOL-CALLING | Not Assessed | — | no |
| SF-2026-ARXIV-2607-08961 | arXiv:2607.08961v1 | paper-v1:2607.08961 | 2026-W29 | 2026-07-13 | SRC-ARXIV | 3 | 2 | 2 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-08961 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-08964 | arXiv:2607.08964v1 | paper-v1:2607.08964 | 2026-W29 | 2026-07-13 | SRC-ARXIV | 2 | 3 | 2 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-08964 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-08973 | arXiv:2607.08973v1 | paper-v1:2607.08973 | 2026-W29 | 2026-07-13 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-08973 | self | — | new_in_window | INFER-TENSORRT-LLM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-08974 | arXiv:2607.08974v1 | paper-v1:2607.08974 | 2026-W29 | 2026-07-13 | SRC-ARXIV | 3 | 2 | 2 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-08974 | self | — | new_in_window | MULTIMODAL-EMBODIED-VLA | Not Assessed | — | no |
| SF-2026-ARXIV-2607-08991 | arXiv:2607.08991v1 | paper-v1:2607.08991 | 2026-W29 | 2026-07-13 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-08991 | self | — | new_in_window | INFER-TENSORRT-LLM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-08993 | arXiv:2607.08993v1 | paper-v1:2607.08993 | 2026-W29 | 2026-07-13 | SRC-ARXIV | 3 | 3 | 2 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-08993 | self | — | new_in_window | INFER-GPU-MEMORY | Not Assessed | — | no |
| SF-2026-ARXIV-2607-09015 | arXiv:2607.09015v1 | paper-v1:2607.09015 | 2026-W29 | 2026-07-13 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-09015 | self | — | new_in_window | INFER-SCHEDULING | Not Assessed | — | no |
| SF-2026-ARXIV-2607-09016 | arXiv:2607.09016v1 | paper-v1:2607.09016 | 2026-W29 | 2026-07-13 | SRC-ARXIV | 3 | 2 | 2 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-09016 | self | — | new_in_window | AGENT-PLATFORM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-09024 | arXiv:2607.09024v1 | paper-v1:2607.09024 | 2026-W29 | 2026-07-13 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-09024 | self | — | new_in_window | MULTIMODAL-REPRESENTATION | Not Assessed | — | no |
| SF-2026-ARXIV-2607-09029 | arXiv:2607.09029v1 | paper-v1:2607.09029 | 2026-W29 | 2026-07-13 | SRC-ARXIV | 3 | 2 | 2 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-09029 | self | — | new_in_window | MULTIMODAL-REPRESENTATION | Not Assessed | — | no |
| SF-2026-ARXIV-2607-09042 | arXiv:2607.09042v1 | paper-v1:2607.09042 | 2026-W29 | 2026-07-13 | SRC-ARXIV | 3 | 2 | 2 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-09042 | self | — | new_in_window | TRAIN-GRPO | Not Assessed | — | no |
| SF-2026-ARXIV-2607-09052 | arXiv:2607.09052v1 | paper-v1:2607.09052 | 2026-W29 | 2026-07-13 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-09052 | self | — | new_in_window | MODEL-LONG-CONTEXT | Not Assessed | — | no |
| SF-2026-ARXIV-2607-09053 | arXiv:2607.09053v1 | paper-v1:2607.09053 | 2026-W29 | 2026-07-13 | SRC-ARXIV | 3 | 2 | 2 | 7 | retained | deep_complete | accessible | books_conflict | review:SF-2026-ARXIV-2607-09053 | self | — | new_in_window | TRAIN-SFT | Not Assessed | — | no |
| SF-2026-ARXIV-2607-09065 | arXiv:2607.09065v1 | paper-v1:2607.09065 | 2026-W29 | 2026-07-13 | SRC-ARXIV | 2 | 1 | 2 | 5 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-09065 | self | — | new_in_window | AGENT-PLATFORM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-09072 | arXiv:2607.09072v1 | paper-v1:2607.09072 | 2026-W29 | 2026-07-13 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-09072 | self | — | new_in_window | AGENT-WORKFLOW | Not Assessed | — | no |
| SF-2026-ARXIV-2607-09091 | arXiv:2607.09091v1 | paper-v1:2607.09091 | 2026-W29 | 2026-07-13 | SRC-ARXIV | 2 | 1 | 2 | 5 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-09091 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-09092 | arXiv:2607.09092v1 | paper-v1:2607.09092 | 2026-W29 | 2026-07-13 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-09092 | self | — | new_in_window | AGENT-RAG | Not Assessed | — | no |
| SF-2026-ARXIV-2607-09123 | arXiv:2607.09123v1 | paper-v1:2607.09123 | 2026-W29 | 2026-07-13 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-09123 | self | — | new_in_window | AGENT-WORKFLOW | Not Assessed | — | no |
| SF-2026-ARXIV-2607-09153 | arXiv:2607.09153v1 | paper-v1:2607.09153 | 2026-W29 | 2026-07-13 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-09153 | self | — | new_in_window | INFER-KV-CACHE | Not Assessed | — | no |
| SF-2026-ARXIV-2607-09156 | arXiv:2607.09156v1 | paper-v1:2607.09156 | 2026-W29 | 2026-07-13 | SRC-ARXIV | 3 | 2 | 2 | 7 | retained | deep_complete | accessible | books_conflict | review:SF-2026-ARXIV-2607-09156 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-09172 | arXiv:2607.09172v1 | paper-v1:2607.09172 | 2026-W29 | 2026-07-13 | SRC-ARXIV | 2 | 3 | 2 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-09172 | self | — | new_in_window | INFER-VLLM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-09175 | arXiv:2607.09175v1 | paper-v1:2607.09175 | 2026-W29 | 2026-07-13 | SRC-ARXIV | 3 | 2 | 2 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-09175 | self | — | new_in_window | AGENT-CONTEXT | Not Assessed | — | no |
| SF-2026-ARXIV-2607-09185 | arXiv:2607.09185v1 | paper-v1:2607.09185 | 2026-W29 | 2026-07-13 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-09185 | self | — | new_in_window | MULTIMODAL-WORLD-MODELS | Not Assessed | — | no |
| SF-2026-ARXIV-2607-09195 | arXiv:2607.09195v1 | paper-v1:2607.09195 | 2026-W29 | 2026-07-13 | SRC-ARXIV | 3 | 2 | 2 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-09195 | self | — | new_in_window | AGENT-WORKFLOW | Not Assessed | — | no |
| SF-2026-ARXIV-2607-09207 | arXiv:2607.09207v1 | paper-v1:2607.09207 | 2026-W29 | 2026-07-13 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-09207 | self | — | new_in_window | TRAIN-DISTRIBUTED-TRAINING | Not Assessed | — | no |
| SF-2026-ARXIV-2607-09217 | arXiv:2607.09217v1 | paper-v1:2607.09217 | 2026-W29 | 2026-07-13 | SRC-ARXIV | 3 | 2 | 2 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-09217 | self | — | new_in_window | AGENT-WORKFLOW | Not Assessed | — | no |
| SF-2026-ARXIV-2607-09218 | arXiv:2607.09218v1 | paper-v1:2607.09218 | 2026-W29 | 2026-07-13 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-09218 | self | — | new_in_window | MULTIMODAL-EMBODIED-VLA | Not Assessed | — | no |
| SF-2026-ARXIV-2607-09236 | arXiv:2607.09236v1 | paper-v1:2607.09236 | 2026-W29 | 2026-07-13 | SRC-ARXIV | 3 | 2 | 2 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-09236 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-09266 | arXiv:2607.09266v1 | paper-v1:2607.09266 | 2026-W29 | 2026-07-13 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-09266 | self | — | new_in_window | TRAIN-PRETRAINING | Not Assessed | — | no |
| SF-2026-ARXIV-2607-09306 | arXiv:2607.09306v1 | paper-v1:2607.09306 | 2026-W29 | 2026-07-13 | SRC-ARXIV | 3 | 2 | 2 | 7 | retained | deep_complete | accessible | books_conflict | review:SF-2026-ARXIV-2607-09306 | self | — | new_in_window | AGENT-MEMORY | Not Assessed | — | no |
| SF-2026-ARXIV-2607-09328 | arXiv:2607.09328v1 | paper-v1:2607.09328 | 2026-W29 | 2026-07-13 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-09328 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-09349 | arXiv:2607.09349v1 | paper-v1:2607.09349 | 2026-W29 | 2026-07-13 | SRC-ARXIV | 3 | 2 | 2 | 7 | retained | deep_complete | accessible | books_conflict | review:SF-2026-ARXIV-2607-09349 | self | — | new_in_window | AGENT-RAG | Not Assessed | — | no |
| SF-2026-ARXIV-2607-09366 | arXiv:2607.09366v1 | paper-v1:2607.09366 | 2026-W29 | 2026-07-13 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-09366 | self | — | new_in_window | AGENT-WORKFLOW | Not Assessed | — | no |
| SF-2026-ARXIV-2607-09385 | arXiv:2607.09385v1 | paper-v1:2607.09385 | 2026-W29 | 2026-07-13 | SRC-ARXIV | 3 | 3 | 2 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-09385 | self | — | new_in_window | INFER-TENSORRT-LLM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-09415 | arXiv:2607.09415v1 | paper-v1:2607.09415 | 2026-W29 | 2026-07-13 | SRC-ARXIV | 3 | 2 | 2 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-09415 | self | — | new_in_window | MODEL-LONG-CONTEXT | Not Assessed | — | no |
| SF-2026-ARXIV-2607-09492 | arXiv:2607.09492v1 | paper-v1:2607.09492 | 2026-W29 | 2026-07-13 | SRC-ARXIV | 3 | 3 | 2 | 8 | retained | deep_complete | accessible | books_conflict | review:SF-2026-ARXIV-2607-09492 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-09493 | arXiv:2607.09493v1 | paper-v1:2607.09493 | 2026-W29 | 2026-07-13 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-09493 | self | — | new_in_window | AGENT-MEMORY | Not Assessed | — | no |
| SF-2026-ARXIV-2607-09510 | arXiv:2607.09510v1 | paper-v1:2607.09510 | 2026-W29 | 2026-07-13 | SRC-ARXIV | 3 | 2 | 2 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-09510 | self | — | new_in_window | PLATFORM-TRACE | Not Assessed | — | no |
| SF-2026-ARXIV-2607-09520 | arXiv:2607.09520v1 | paper-v1:2607.09520 | 2026-W29 | 2026-07-13 | SRC-ARXIV | 3 | 2 | 2 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-09520 | self | — | new_in_window | INFER-DECODE | Not Assessed | — | no |
| SF-2026-ARXIV-2607-09532 | arXiv:2607.09532v1 | paper-v1:2607.09532 | 2026-W29 | 2026-07-13 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | release_security_contract | review:SF-2026-ARXIV-2607-09532 | self | — | new_in_window | PLATFORM-SECURITY | Not Assessed | — | no |
| SF-2026-ARXIV-2607-09553 | arXiv:2607.09553v1 | paper-v1:2607.09553 | 2026-W29 | 2026-07-13 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-09553 | self | — | new_in_window | AGENT-CONTEXT | Not Assessed | — | no |
| SF-2026-ARXIV-2607-09560 | arXiv:2607.09560v1 | paper-v1:2607.09560 | 2026-W29 | 2026-07-13 | SRC-ARXIV | 2 | 1 | 2 | 5 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-09560 | self | — | new_in_window | WORLDVIEW-FUTURE | Not Assessed | — | no |
| SF-2026-ARXIV-2607-09586 | arXiv:2607.09586v1 | paper-v1:2607.09586 | 2026-W29 | 2026-07-13 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-09586 | self | — | new_in_window | AGENT-PLATFORM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-09590 | arXiv:2607.09590v1 | paper-v1:2607.09590 | 2026-W29 | 2026-07-13 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-09590 | self | — | new_in_window | MULTIMODAL-EMBODIED-VLA | Not Assessed | — | no |
| SF-2026-ARXIV-2607-09600 | arXiv:2607.09600v1 | paper-v1:2607.09600 | 2026-W29 | 2026-07-13 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-09600 | self | — | new_in_window | AGENT-MULTI-AGENT | Not Assessed | — | no |
| SF-2026-ARXIV-2607-09603 | arXiv:2607.09603v1 | paper-v1:2607.09603 | 2026-W29 | 2026-07-13 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-09603 | self | — | new_in_window | AGENT-MULTI-AGENT | Not Assessed | — | no |
| SF-2026-ARXIV-2607-09661 | arXiv:2607.09661v1 | paper-v1:2607.09661 | 2026-W29 | 2026-07-13 | SRC-ARXIV | 3 | 2 | 2 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-09661 | self | — | new_in_window | MULTIMODAL-WORLD-MODELS | Not Assessed | — | no |

## 3. Review Completion Receipt

<!-- validator:review-completion-v1 -->
| Source Family ID | Review Provenance ID | Review Route | Primary Evidence Version | Reviewed Evidence Versions | Method / Identity Locators | Evaluation Locators | Limitations / Counterevidence Locators | Artifact Locators | Claim Boundary Ref | Completion Result |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2607-08774 | RP-35e6b08e120d943a | deep | arXiv:2607.08774v1 | SRC-ARXIV@arXiv:2607.08774v1 | https://arxiv.org/html/2607.08774v1#S3; https://arxiv.org/html/2607.08774v1#S4 | https://arxiv.org/html/2607.08774v1#S5 | https://arxiv.org/html/2607.08774v1#S8; https://arxiv.org/html/2607.08774v1#S9 | The article links https://github.com/Cogniconsole/cogniconsole but does not pin an event-time commit; the repository is not used to support v1 mechanism or benchmark claims. | claim:SF-2026-ARXIV-2607-08774 | complete |
| SF-2026-ARXIV-2607-08780 | RP-d2c9e360824cdb12 | deep | arXiv:2607.08780v1 | SRC-ARXIV@arXiv:2607.08780v1 | https://arxiv.org/html/2607.08780v1#S4; https://arxiv.org/html/2607.08780v1#S4.SS5 | https://arxiv.org/html/2607.08780v1#S5; https://arxiv.org/html/2607.08780v1#S5.SS6 | https://arxiv.org/html/2607.08780v1#S6; https://arxiv.org/html/2607.08780v1#A4 | The article links https://github.com/alikayyam/sticky_moe.git without an event-time commit; code is not used as exact-v1 evidence. | claim:SF-2026-ARXIV-2607-08780 | complete |
| SF-2026-ARXIV-2607-08782 | RP-f503cbe85892ae1f | deep | arXiv:2607.08782v1 | SRC-ARXIV@arXiv:2607.08782v1 | https://arxiv.org/html/2607.08782v1#S4; https://arxiv.org/html/2607.08782v1#S5; https://arxiv.org/html/2607.08782v1#S6 | https://arxiv.org/html/2607.08782v1#S7; https://arxiv.org/html/2607.08782v1#S8 | https://arxiv.org/html/2607.08782v1#S9 | Not Disclosed — The article cites EPLB as related software but does not publish a pinned Director implementation; cited repositories are not Director provenance. | claim:SF-2026-ARXIV-2607-08782 | complete |
| SF-2026-ARXIV-2607-08786 | RP-83fd77f3a7b40ba9 | deep | arXiv:2607.08786v1 | SRC-ARXIV@arXiv:2607.08786v1 | https://arxiv.org/html/2607.08786v1#S3; https://arxiv.org/html/2607.08786v1#S4 | https://arxiv.org/html/2607.08786v1#S5 | https://arxiv.org/html/2607.08786v1#S6 | Not Disclosed — No author implementation is pinned in exact v1. | claim:SF-2026-ARXIV-2607-08786 | complete |
| SF-2026-ARXIV-2607-08839 | RP-bbe94d861622fd13 | standard | arXiv:2607.08839v1 | SRC-ARXIV@arXiv:2607.08839v1 | https://arxiv.org/html/2607.08839v1#S4; https://arxiv.org/html/2607.08839v1#S5.SS4 | https://arxiv.org/html/2607.08839v1#S5.SS1 | https://arxiv.org/html/2607.08839v1#S6 | Not Disclosed — Evidence is limited to the shared-encoder design and ADL/music benchmarks in exact v1; heterogeneous encoders are explicitly outside scope. | claim:SF-2026-ARXIV-2607-08839 | complete |
| SF-2026-ARXIV-2607-08857 | RP-578d5a68534bfa1d | standard | arXiv:2607.08857v1 | SRC-ARXIV@arXiv:2607.08857v1 | https://arxiv.org/html/2607.08857v1#S1 | https://arxiv.org/html/2607.08857v1#S2.SS1 | https://arxiv.org/html/2607.08857v1#S3 | Not Disclosed — The evaluation uses EPIC-KITCHENS and internally processed clips at 30 FPS; the resulting mixed-reality corpus is not evidence of downstream policy success. | claim:SF-2026-ARXIV-2607-08857 | complete |
| SF-2026-ARXIV-2607-08877 | RP-a2cc0175b0a99970 | deep | arXiv:2607.08877v1 | SRC-ARXIV@arXiv:2607.08877v1 | https://arxiv.org/html/2607.08877v1#S4; https://arxiv.org/html/2607.08877v1#A1 | https://arxiv.org/html/2607.08877v1#S5; https://arxiv.org/html/2607.08877v1#A2 | https://arxiv.org/html/2607.08877v1#S6 | Not Disclosed — No event-time implementation commit is pinned in exact v1. | claim:SF-2026-ARXIV-2607-08877 | complete |
| SF-2026-ARXIV-2607-08883 | RP-7d0a81a729dce64f | deep | arXiv:2607.08883v1 | SRC-ARXIV@arXiv:2607.08883v1 | https://arxiv.org/html/2607.08883v1#Sx3 | https://arxiv.org/html/2607.08883v1#Sx4 | https://arxiv.org/html/2607.08883v1#Sx5; https://arxiv.org/html/2607.08883v1#Sx5.SSx1 | Not Disclosed — No event-time attack implementation is pinned in exact v1. | claim:SF-2026-ARXIV-2607-08883 | complete |
| SF-2026-ARXIV-2607-08894 | RP-0330c546aeff72ab | standard | arXiv:2607.08894v1 | SRC-ARXIV@arXiv:2607.08894v1 | https://arxiv.org/html/2607.08894v1#S3; https://arxiv.org/html/2607.08894v1#S5.SS4 | https://arxiv.org/html/2607.08894v1#S4.SS1 | https://arxiv.org/html/2607.08894v1#S7 | Not Disclosed — The headline planning results use synthetic tasks whose exact transitions make the lowest layer cover 100%; the open-domain layer-use figures are projections, not observations. | claim:SF-2026-ARXIV-2607-08894 | complete |
| SF-2026-ARXIV-2607-08925 | RP-eeafb06a62eef121 | deep | arXiv:2607.08925v1 | SRC-ARXIV@arXiv:2607.08925v1 | https://arxiv.org/html/2607.08925v1#S4; https://arxiv.org/html/2607.08925v1#S5 | https://arxiv.org/html/2607.08925v1#S6; https://arxiv.org/html/2607.08925v1#S7; https://arxiv.org/html/2607.08925v1#S8 | https://arxiv.org/html/2607.08925v1#S9; https://arxiv.org/html/2607.08925v1#A5.SS11 | Not Disclosed — The article cites MuJoCo assets but does not pin a SafeExplorer implementation; dependency repositories are not method provenance. | claim:SF-2026-ARXIV-2607-08925 | complete |
| SF-2026-ARXIV-2607-08930 | RP-b68bcf783c059776 | deep | arXiv:2607.08930v1 | SRC-ARXIV@arXiv:2607.08930v1 | https://arxiv.org/html/2607.08930v1#S2 | https://arxiv.org/html/2607.08930v1#S3 | https://arxiv.org/html/2607.08930v1#S5 | Not Disclosed — No event-time implementation commit is pinned in exact v1. | claim:SF-2026-ARXIV-2607-08930 | complete |
| SF-2026-ARXIV-2607-08938 | RP-d36a5f2af42f1774 | deep | arXiv:2607.08938v1 | SRC-ARXIV@arXiv:2607.08938v1 | https://arxiv.org/html/2607.08938v1#S2; https://arxiv.org/html/2607.08938v1#S4.SS2 | https://arxiv.org/html/2607.08938v1#S4 | https://arxiv.org/html/2607.08938v1#S4.SS3; https://arxiv.org/html/2607.08938v1#S5 | The article links https://github.com/malusamayo/migration-analysis without an event-time commit; the repository is not treated as exact-v1 benchmark provenance. | claim:SF-2026-ARXIV-2607-08938 | complete |
| SF-2026-ARXIV-2607-08940 | RP-5c1e60d091254461 | standard | arXiv:2607.08940v1 | SRC-ARXIV@arXiv:2607.08940v1 | https://arxiv.org/html/2607.08940v1#S2; https://arxiv.org/html/2607.08940v1#A4 | https://arxiv.org/html/2607.08940v1#S3.SS1 | https://arxiv.org/html/2607.08940v1#S5 | Not Disclosed — Results are bound to TSRBench plus two transfer tasks and the stated LLM/VLM pool; combined-modality interference is a case observation, not a universal law. | claim:SF-2026-ARXIV-2607-08940 | complete |
| SF-2026-ARXIV-2607-08948 | RP-581d753424e448e2 | deep | arXiv:2607.08948v1 | SRC-ARXIV@arXiv:2607.08948v1 | https://arxiv.org/html/2607.08948v1#S3 | https://arxiv.org/html/2607.08948v1#S4 | https://arxiv.org/html/2607.08948v1#S5 | Not Disclosed — No event-time implementation commit is pinned in exact v1. | claim:SF-2026-ARXIV-2607-08948 | complete |
| SF-2026-ARXIV-2607-08949 | RP-a08ca07538c715e7 | standard | arXiv:2607.08949v1 | SRC-ARXIV@arXiv:2607.08949v1 | https://arxiv.org/html/2607.08949v1#S4; https://arxiv.org/html/2607.08949v1#S5 | https://arxiv.org/html/2607.08949v1#S6.SS1; https://arxiv.org/html/2607.08949v1#S6.SS4 | https://arxiv.org/html/2607.08949v1#S7 | Not Disclosed — The 24-hour, ten-trial Magma/ARVO protocol and canary-confirmed crashes define the claim; the first crashing stack function is supplied as sink. | claim:SF-2026-ARXIV-2607-08949 | complete |
| SF-2026-ARXIV-2607-08961 | RP-c67247fe7852a0b6 | deep | arXiv:2607.08961v1 | SRC-ARXIV@arXiv:2607.08961v1 | https://arxiv.org/html/2607.08961v1#S2; https://arxiv.org/html/2607.08961v1#S4 | https://arxiv.org/html/2607.08961v1#S5; https://arxiv.org/html/2607.08961v1#A3 | https://arxiv.org/html/2607.08961v1#S6 | Not Disclosed — Exact v1 provides reproducibility diagnostics but no event-time implementation artifact is needed for the certified mathematical floor. | claim:SF-2026-ARXIV-2607-08961 | complete |
| SF-2026-ARXIV-2607-08964 | RP-b8e0eaaf83b59876 | deep | arXiv:2607.08964v1 | SRC-ARXIV@arXiv:2607.08964v1 | https://arxiv.org/html/2607.08964v1#S2; https://arxiv.org/html/2607.08964v1#S3.SS2 | https://arxiv.org/html/2607.08964v1#S3 | https://arxiv.org/html/2607.08964v1#S3.SS4; https://arxiv.org/html/2607.08964v1#S5 | Not Disclosed — The report evaluates a concrete benchmark, but this review does not treat later benchmark revisions as v1 evidence. | claim:SF-2026-ARXIV-2607-08964 | complete |
| SF-2026-ARXIV-2607-08973 | RP-9f5e145451b28814 | deep | arXiv:2607.08973v1 | SRC-ARXIV@arXiv:2607.08973v1 | https://arxiv.org/html/2607.08973v1#S3; https://arxiv.org/html/2607.08973v1#S4.SS2 | https://arxiv.org/html/2607.08973v1#S5; https://arxiv.org/html/2607.08973v1#S6 | https://arxiv.org/html/2607.08973v1#S2.SS5; https://arxiv.org/html/2607.08973v1#S9 | Not Disclosed — Evidence is bound to the Megakernel integration, one 8xH200 topology and reported model, precision, batch and length settings; cited frameworks are not SiFAR provenance. | claim:SF-2026-ARXIV-2607-08973 | complete |
| SF-2026-ARXIV-2607-08974 | RP-d38426b31b5e4688 | deep | arXiv:2607.08974v1 | SRC-ARXIV@arXiv:2607.08974v1 | https://arxiv.org/html/2607.08974v1#S3; https://arxiv.org/html/2607.08974v1#S4 | https://arxiv.org/html/2607.08974v1#S5; https://arxiv.org/html/2607.08974v1#A2.SS4 | https://arxiv.org/html/2607.08974v1#S6 | Not Disclosed — The reported LIBERO/LIBERO-PRO and three-object real-robot tasks define the result; the real-robot unseen objects are distractors, not unseen pick targets. | claim:SF-2026-ARXIV-2607-08974 | complete |
| SF-2026-ARXIV-2607-08991 | RP-0f72d8042f3cae31 | deep | arXiv:2607.08991v1 | SRC-ARXIV@arXiv:2607.08991v1 | https://arxiv.org/html/2607.08991v1#S3 | https://arxiv.org/html/2607.08991v1#S4; https://arxiv.org/html/2607.08991v1#S4.SS2 | https://arxiv.org/html/2607.08991v1#S5 | Not Disclosed — No event-time implementation commit is pinned in exact v1. | claim:SF-2026-ARXIV-2607-08991 | complete |
| SF-2026-ARXIV-2607-08993 | RP-a090af99f0e8b5c0 | deep | arXiv:2607.08993v1 | SRC-ARXIV@arXiv:2607.08993v1 | https://arxiv.org/html/2607.08993v1#S3; https://arxiv.org/html/2607.08993v1#S3.SS4 | https://arxiv.org/html/2607.08993v1#S5; https://arxiv.org/html/2607.08993v1#S6 | https://arxiv.org/html/2607.08993v1#S7; https://arxiv.org/html/2607.08993v1#S8 | Not Disclosed — Performance and power are evaluated with the in-house StreamDQ-Sim; no independent silicon or public event-time simulator artifact is established. | claim:SF-2026-ARXIV-2607-08993 | complete |
| SF-2026-ARXIV-2607-09015 | RP-2ca90ea35d65e633 | standard | arXiv:2607.09015v1 | SRC-ARXIV@arXiv:2607.09015v1 | https://arxiv.org/html/2607.09015v1#S4.SS1; https://arxiv.org/html/2607.09015v1#S4.SS2 | https://arxiv.org/html/2607.09015v1#S5 | https://arxiv.org/html/2607.09015v1#S7 | Not Disclosed — The theoretical guarantees use stated feedback assumptions and experiments use SPROUT/RouterBench; they are not production traffic evidence. | claim:SF-2026-ARXIV-2607-09015 | complete |
| SF-2026-ARXIV-2607-09016 | RP-f953d050546376c0 | deep | arXiv:2607.09016v1 | SRC-ARXIV@arXiv:2607.09016v1 | https://arxiv.org/html/2607.09016v1#S3 | https://arxiv.org/html/2607.09016v1#S3.SS3; https://arxiv.org/html/2607.09016v1#S4 | https://arxiv.org/html/2607.09016v1#S5; https://arxiv.org/html/2607.09016v1#Sx1 | Not Disclosed — The v1 benchmark construction is auditable in the paper; current marketplace contents or later case revisions are outside the event-time claim. | claim:SF-2026-ARXIV-2607-09016 | complete |
| SF-2026-ARXIV-2607-09024 | RP-fe76572c98c639c0 | standard | arXiv:2607.09024v1 | SRC-ARXIV@arXiv:2607.09024v1 | https://arxiv.org/html/2607.09024v1#S2.SS3; https://arxiv.org/html/2607.09024v1#S3 | https://arxiv.org/html/2607.09024v1#S4.SS3 | https://arxiv.org/html/2607.09024v1#S5 | Not Disclosed — The evaluated datasets and feed-forward heads support a representation-reuse claim; the paper's 'universal world model' language is not accepted as causal-environment evidence. | claim:SF-2026-ARXIV-2607-09024 | complete |
| SF-2026-ARXIV-2607-09029 | RP-06411bf503349553 | deep | arXiv:2607.09029v1 | SRC-ARXIV@arXiv:2607.09029v1 | https://arxiv.org/html/2607.09029v1#S3; https://arxiv.org/html/2607.09029v1#S3.SS2 | https://arxiv.org/html/2607.09029v1#S4; https://arxiv.org/html/2607.09029v1#A2 | https://arxiv.org/html/2607.09029v1#S5 | Not Disclosed — No immutable search code or hardware measurement artifact is pinned in exact v1. | claim:SF-2026-ARXIV-2607-09029 | complete |
| SF-2026-ARXIV-2607-09042 | RP-c47dbf97ab11aa89 | deep | arXiv:2607.09042v1 | SRC-ARXIV@arXiv:2607.09042v1 | https://arxiv.org/html/2607.09042v1#S4; https://arxiv.org/html/2607.09042v1#A2 | https://arxiv.org/html/2607.09042v1#S5; https://arxiv.org/html/2607.09042v1#S5.SS4 | https://arxiv.org/html/2607.09042v1#S6 | Not Disclosed — The paper names RLinf and a concrete SFT checkpoint, but this review does not infer an event-time implementation commit from current documentation. | claim:SF-2026-ARXIV-2607-09042 | complete |
| SF-2026-ARXIV-2607-09052 | RP-ed3480258d06ac0b | standard | arXiv:2607.09052v1 | SRC-ARXIV@arXiv:2607.09052v1 | https://arxiv.org/html/2607.09052v1#S4; https://arxiv.org/html/2607.09052v1#S5.SS4 | https://arxiv.org/html/2607.09052v1#S7.SS2 | https://arxiv.org/html/2607.09052v1#S8 | Not Disclosed — Headline evidence is 32k RULER with stated subspace rank/quantization and an NSA-based selector; no universal kernel speedup is inferred. | claim:SF-2026-ARXIV-2607-09052 | complete |
| SF-2026-ARXIV-2607-09053 | RP-c8feb99c2eec0aec | deep | arXiv:2607.09053v1 | SRC-ARXIV@arXiv:2607.09053v1 | https://arxiv.org/html/2607.09053v1#S3 | https://arxiv.org/html/2607.09053v1#S4; https://arxiv.org/html/2607.09053v1#S5 | https://arxiv.org/html/2607.09053v1#S6 | Not Disclosed — The reviewed claim is limited to the paper's Qwen2.5-14B-Instruct model-organism and LoRA/data construction; it is not generalized to deployed frontier models. | claim:SF-2026-ARXIV-2607-09053 | complete |
| SF-2026-ARXIV-2607-09065 | RP-355c03ebdcafaf21 | standard | arXiv:2607.09065v1 | SRC-ARXIV@arXiv:2607.09065v1 | https://arxiv.org/html/2607.09065v1#S3.SS1 | https://arxiv.org/html/2607.09065v1#S6.SS2 | https://arxiv.org/html/2607.09065v1#S7 | Not Disclosed — Marketplace records are a time-bounded observational sample and some annotations are LLM-assisted; scanner flags are signals, not proven maliciousness. | claim:SF-2026-ARXIV-2607-09065 | complete |
| SF-2026-ARXIV-2607-09072 | RP-5082f5c93a86f9d1 | standard | arXiv:2607.09072v1 | SRC-ARXIV@arXiv:2607.09072v1 | https://arxiv.org/html/2607.09072v1#S3; https://arxiv.org/html/2607.09072v1#S4 | https://arxiv.org/html/2607.09072v1#S2.SS3; https://arxiv.org/html/2607.09072v1#S5 | https://arxiv.org/html/2607.09072v1#S7 | Not Disclosed — The evidence is a Spark/DISC instantiation; reported proof/test gains do not imply verified correctness of arbitrary data systems. | claim:SF-2026-ARXIV-2607-09072 | complete |
| SF-2026-ARXIV-2607-09091 | RP-b798c5a24d810b2c | standard | arXiv:2607.09091v1 | SRC-ARXIV@arXiv:2607.09091v1 | https://arxiv.org/html/2607.09091v1#S3 | https://arxiv.org/html/2607.09091v1#S4.SS3 | https://arxiv.org/html/2607.09091v1#S5 | Not Disclosed — Human-preference correlation on SynthSync supports the metric claim; it does not make the learned evaluator a physical-synchrony oracle. | claim:SF-2026-ARXIV-2607-09091 | complete |
| SF-2026-ARXIV-2607-09092 | RP-68aa2086f543f0c4 | standard | arXiv:2607.09092v1 | SRC-ARXIV@arXiv:2607.09092v1 | https://arxiv.org/html/2607.09092v1#S3.SS2 | https://arxiv.org/html/2607.09092v1#S4.SS2 | https://arxiv.org/html/2607.09092v1#S5 | Not Disclosed — Evidence is limited to the stated T-REx seen/unseen splits, F1 and search-call count; industrial-KG reliability is an aspiration, not a demonstrated deployment. | claim:SF-2026-ARXIV-2607-09092 | complete |
| SF-2026-ARXIV-2607-09123 | RP-f1c1fa13acd24975 | standard | arXiv:2607.09123v1 | SRC-ARXIV@arXiv:2607.09123v1 | https://arxiv.org/html/2607.09123v1#S3.SS3; https://arxiv.org/html/2607.09123v1#S4.SS5 | https://arxiv.org/html/2607.09123v1#S5 | https://arxiv.org/html/2607.09123v1#S6.SS3 | Not Disclosed — The evaluation uses Python SWT-bench repositories and standardized containers; framework or model versions outside v1 are not assumed equivalent. | claim:SF-2026-ARXIV-2607-09123 | complete |
| SF-2026-ARXIV-2607-09153 | RP-4f7bc15a9056f190 | deep | arXiv:2607.09153v1 | SRC-ARXIV@arXiv:2607.09153v1 | https://arxiv.org/html/2607.09153v1#S3; https://arxiv.org/html/2607.09153v1#S4 | https://arxiv.org/html/2607.09153v1#S5.SS2; https://arxiv.org/html/2607.09153v1#S6 | https://arxiv.org/html/2607.09153v1#S8 | Not Disclosed — Latency and memory evidence is bound to the reported GH200, Qwen-family configurations and search protocols; no immutable author code artifact is disclosed in exact v1. | claim:SF-2026-ARXIV-2607-09153 | complete |
| SF-2026-ARXIV-2607-09156 | RP-e22a12a91f1f89c3 | deep | arXiv:2607.09156v1 | SRC-ARXIV@arXiv:2607.09156v1 | https://arxiv.org/html/2607.09156v1#Sx3; https://arxiv.org/html/2607.09156v1#S5.SSx1 | https://arxiv.org/html/2607.09156v1#S5; https://arxiv.org/html/2607.09156v1#A5 | https://arxiv.org/html/2607.09156v1#Sx8 | Not Disclosed — The article names configuration files but this review did not resolve an immutable event-time repository commit; numeric claims are therefore bound to exact v1 tables and appendices. | claim:SF-2026-ARXIV-2607-09156 | complete |
| SF-2026-ARXIV-2607-09172 | RP-1988af9013cc7266 | deep | arXiv:2607.09172v1 | SRC-ARXIV@arXiv:2607.09172v1 | https://arxiv.org/html/2607.09172v1#S3; https://arxiv.org/html/2607.09172v1#S3.SS5 | https://arxiv.org/html/2607.09172v1#S4; https://arxiv.org/html/2607.09172v1#S5 | https://arxiv.org/html/2607.09172v1#S7 | Not Disclosed — Exact v1 links a replication package, but no immutable commit was established in this Daily; findings are bound to the article's recorded pipeline and configurations. | claim:SF-2026-ARXIV-2607-09172 | complete |
| SF-2026-ARXIV-2607-09175 | RP-082710097754f45d | deep | arXiv:2607.09175v1 | SRC-ARXIV@arXiv:2607.09175v1 | https://arxiv.org/html/2607.09175v1#S4; https://arxiv.org/html/2607.09175v1#S4.SS3 | https://arxiv.org/html/2607.09175v1#S5; https://arxiv.org/html/2607.09175v1#S5.SS2 | https://arxiv.org/html/2607.09175v1#S6 | Not Disclosed — No immutable implementation snapshot is used; the review relies on the exact-v1 graph schema, update protocol, ablation and checkpoint results. | claim:SF-2026-ARXIV-2607-09175 | complete |
| SF-2026-ARXIV-2607-09185 | RP-9bd7632381e38c00 | deep | arXiv:2607.09185v1 | SRC-ARXIV@arXiv:2607.09185v1 | https://arxiv.org/html/2607.09185v1#S4; https://arxiv.org/html/2607.09185v1#S4.SS1 | https://arxiv.org/html/2607.09185v1#S5; https://arxiv.org/html/2607.09185v1#S5.SS1 | https://arxiv.org/html/2607.09185v1#S7 | Not Disclosed — The reported pipeline uses SAM3 masks and coarse primitive labels; because no immutable code snapshot is established here, the evidence boundary is the v1 architecture, training protocol and ablations. | claim:SF-2026-ARXIV-2607-09185 | complete |
| SF-2026-ARXIV-2607-09195 | RP-6c4a0a9e4db5e542 | deep | arXiv:2607.09195v1 | SRC-ARXIV@arXiv:2607.09195v1 | https://arxiv.org/html/2607.09195v1#S4.SSx1 | https://arxiv.org/html/2607.09195v1#S2.SSx2 | https://arxiv.org/html/2607.09195v1#S3 | Not Disclosed — The review does not treat any later repository state as exact-v1 provenance; workflow claims are limited to the article's event schema, tools and three materials-science task runs. | claim:SF-2026-ARXIV-2607-09195 | complete |
| SF-2026-ARXIV-2607-09207 | RP-edfe89e098b3c0c5 | deep | arXiv:2607.09207v1 | SRC-ARXIV@arXiv:2607.09207v1 | https://arxiv.org/html/2607.09207v1#S3.SS1; https://arxiv.org/html/2607.09207v1#S4 | https://arxiv.org/html/2607.09207v1#S7; https://arxiv.org/html/2607.09207v1#S7.SS1 | https://arxiv.org/html/2607.09207v1#S8 | Not Disclosed — No event-time code commit is used. Performance claims stay bound to the exact-v1 scheduler, A6000/H100 testbeds, model sizes, response-length and staleness settings. | claim:SF-2026-ARXIV-2607-09207 | complete |
| SF-2026-ARXIV-2607-09217 | RP-03b48fd7d9afe783 | deep | arXiv:2607.09217v1 | SRC-ARXIV@arXiv:2607.09217v1 | https://arxiv.org/html/2607.09217v1#S2 | https://arxiv.org/html/2607.09217v1#S4 | https://arxiv.org/html/2607.09217v1#S5 | Not Disclosed — The article's Lean-verifier interface and ProofNet experiment are exact-v1 evidence; no later prompt or repository revision is treated as part of this result. | claim:SF-2026-ARXIV-2607-09217 | complete |
| SF-2026-ARXIV-2607-09218 | RP-5a086d9d1f21a58d | standard | arXiv:2607.09218v1 | SRC-ARXIV@arXiv:2607.09218v1 | https://arxiv.org/html/2607.09218v1#S4a | https://arxiv.org/html/2607.09218v1#S5 | https://arxiv.org/html/2607.09218v1#S7 | Not Disclosed — Simulation and reported hardware trials evaluate task success and force behaviour; no formal safety guarantee is claimed. | claim:SF-2026-ARXIV-2607-09218 | complete |
| SF-2026-ARXIV-2607-09236 | RP-fed41dcc11d558de | deep | arXiv:2607.09236v1 | SRC-ARXIV@arXiv:2607.09236v1 | https://arxiv.org/html/2607.09236v1#S3; https://arxiv.org/html/2607.09236v1#A2.SS4 | https://arxiv.org/html/2607.09236v1#S4; https://arxiv.org/html/2607.09236v1#A3.SS4 | https://arxiv.org/html/2607.09236v1#S6 | Not Disclosed — The exact-v1 datasets, probe construction and model/training settings define the evidence; no unpinned later artifact is used. | claim:SF-2026-ARXIV-2607-09236 | complete |
| SF-2026-ARXIV-2607-09266 | RP-8001c9edac822d42 | deep | arXiv:2607.09266v1 | SRC-ARXIV@arXiv:2607.09266v1 | https://arxiv.org/html/2607.09266v1#S3; https://arxiv.org/html/2607.09266v1#S5.SS2 | https://arxiv.org/html/2607.09266v1#S4; https://arxiv.org/html/2607.09266v1#S4.SS3 | https://arxiv.org/html/2607.09266v1#S6 | Not Disclosed — The review relies on exact-v1 derivations, eight-seed CIFAR experiments and ablations; no later code snapshot is needed to elevate the evidence beyond those workloads. | claim:SF-2026-ARXIV-2607-09266 | complete |
| SF-2026-ARXIV-2607-09306 | RP-494c49562ce2e694 | deep | arXiv:2607.09306v1 | SRC-ARXIV@arXiv:2607.09306v1 | https://arxiv.org/html/2607.09306v1#Sx1.SSx7; https://arxiv.org/html/2607.09306v1#Sx2.SSx2 | https://arxiv.org/html/2607.09306v1#Sx1.SSx7 | https://arxiv.org/html/2607.09306v1#Sx1.SSx10 | Not Disclosed — This family changed materially by v3: the current title and abstract concern exposure-versus-manifestation evaluator targets, whereas exact v1 is a companion-AI and designed-forgetting paper. The later claim is not backfilled into this first-public Daily. | claim:SF-2026-ARXIV-2607-09306 | complete |
| SF-2026-ARXIV-2607-09328 | RP-c54cfe8b221cc89a | standard | arXiv:2607.09328v1 | SRC-ARXIV@arXiv:2607.09328v1 | https://arxiv.org/html/2607.09328v1#S2; https://arxiv.org/html/2607.09328v1#S3.SS2 | https://arxiv.org/html/2607.09328v1#A2 | https://arxiv.org/html/2607.09328v1#S4 | Not Disclosed — Leaderboard scores are tied to the released question/document set and multi-judge matrix; diagnostic slices are not independent leaderboards. | claim:SF-2026-ARXIV-2607-09328 | complete |
| SF-2026-ARXIV-2607-09349 | RP-ed39ad5089954649 | deep | arXiv:2607.09349v1 | SRC-ARXIV@arXiv:2607.09349v1 | https://arxiv.org/html/2607.09349v1#S3; https://arxiv.org/html/2607.09349v1#A2 | https://arxiv.org/html/2607.09349v1#S4; https://arxiv.org/html/2607.09349v1#A2 | https://arxiv.org/html/2607.09349v1#S6 | Not Disclosed — The article's synthetic clinical corpus, judge prompts and human adjudication define the evidence; no later clinical deployment or repository state is inferred. | claim:SF-2026-ARXIV-2607-09349 | complete |
| SF-2026-ARXIV-2607-09366 | RP-7e52dc8c7b00366b | standard | arXiv:2607.09366v1 | SRC-ARXIV@arXiv:2607.09366v1 | https://arxiv.org/html/2607.09366v1#S3; https://arxiv.org/html/2607.09366v1#S6 | https://arxiv.org/html/2607.09366v1#S5 | https://arxiv.org/html/2607.09366v1#S7.SS3 | Not Disclosed — Public LeetCode-derived tasks may be contaminated; the claim concerns generated WhyML structures and verifier outcomes, not unseen coding ability. | claim:SF-2026-ARXIV-2607-09366 | complete |
| SF-2026-ARXIV-2607-09385 | RP-e3fd931f2c2cc30d | deep | arXiv:2607.09385v1 | SRC-ARXIV@arXiv:2607.09385v1 | https://arxiv.org/html/2607.09385v1#S2.SS3; https://arxiv.org/html/2607.09385v1#S4 | https://arxiv.org/html/2607.09385v1#S5; https://arxiv.org/html/2607.09385v1#S5.SS4 | https://arxiv.org/html/2607.09385v1#S6 | Not Disclosed — Results are bound to exact-v1 kernels, XDNA 1/2 devices and the reported BERT/Llama-shaped attention dimensions; no claim is made for CUDA or server accelerators. | claim:SF-2026-ARXIV-2607-09385 | complete |
| SF-2026-ARXIV-2607-09415 | RP-d49d63f14357d15f | deep | arXiv:2607.09415v1 | SRC-ARXIV@arXiv:2607.09415v1 | https://arxiv.org/html/2607.09415v1#S2; https://arxiv.org/html/2607.09415v1#A1 | https://arxiv.org/html/2607.09415v1#S3; https://arxiv.org/html/2607.09415v1#S3.SS2 | https://arxiv.org/html/2607.09415v1#S6 | Not Disclosed — Evidence is limited to exact-v1 LongBench-v2/Pro, Qwen3 and Llama-3.1 configurations and the disclosed LoRA sweep; no online serving implementation is assumed. | claim:SF-2026-ARXIV-2607-09415 | complete |
| SF-2026-ARXIV-2607-09492 | RP-598bdd1f7c0b1c49 | deep | arXiv:2607.09492v1 | SRC-ARXIV@arXiv:2607.09492v1 | https://arxiv.org/html/2607.09492v1#S2; https://arxiv.org/html/2607.09492v1#S3.SS4 | https://arxiv.org/html/2607.09492v1#S3; https://arxiv.org/html/2607.09492v1#A4 | https://arxiv.org/html/2607.09492v1#S3.SS1; https://arxiv.org/html/2607.09492v1#S5 | Not Disclosed — The independent oracle is still Qwen3-VL-235B rather than human ground truth; claims stay tied to the disclosed judge inputs, tasks and output interface. | claim:SF-2026-ARXIV-2607-09492 | complete |
| SF-2026-ARXIV-2607-09493 | RP-9380d3b9af3bc6dd | deep | arXiv:2607.09493v1 | SRC-ARXIV@arXiv:2607.09493v1 | https://arxiv.org/html/2607.09493v1#S4; https://arxiv.org/html/2607.09493v1#S5 | https://arxiv.org/html/2607.09493v1#S6; https://arxiv.org/html/2607.09493v1#S6.SS4 | https://arxiv.org/html/2607.09493v1#S7 | Not Disclosed — The implementation is a specific FastAPI-based workspace and the token figures are representation counts, not universal serving-cost measurements. | claim:SF-2026-ARXIV-2607-09493 | complete |
| SF-2026-ARXIV-2607-09510 | RP-91cf2ac31cf9a470 | deep | arXiv:2607.09510v1 | SRC-ARXIV@arXiv:2607.09510v1 | https://arxiv.org/html/2607.09510v1#S2.SS5 | https://arxiv.org/html/2607.09510v1#S3; https://arxiv.org/html/2607.09510v1#S3.SS1 | https://arxiv.org/html/2607.09510v1#S4.SS1 | Not Disclosed — The evidence is the annotated corpus of 1,184 failed trajectories across the stated seven models and three scaffolds; later agent versions are not assumed equivalent. | claim:SF-2026-ARXIV-2607-09510 | complete |
| SF-2026-ARXIV-2607-09520 | RP-48cf4b4fdcca2a54 | deep | arXiv:2607.09520v1 | SRC-ARXIV@arXiv:2607.09520v1 | https://arxiv.org/html/2607.09520v1#S3; https://arxiv.org/html/2607.09520v1#S4 | https://arxiv.org/html/2607.09520v1#S5; https://arxiv.org/html/2607.09520v1#S6 | https://arxiv.org/html/2607.09520v1#S7 | Not Disclosed — The conclusion is bound to the two edge platforms, five model families, llama.cpp, greedy decoding and tested resolutions; power sampling and quantization/runtime details must travel with numeric claims. | claim:SF-2026-ARXIV-2607-09520 | complete |
| SF-2026-ARXIV-2607-09532 | RP-6a00c07225344093 | deep | arXiv:2607.09532v1 | SRC-ARXIV@arXiv:2607.09532v1 | https://arxiv.org/html/2607.09532v1#S3; https://arxiv.org/html/2607.09532v1#S5 | https://arxiv.org/html/2607.09532v1#S1.SS1; https://arxiv.org/html/2607.09532v1#S6.SS1 | https://arxiv.org/html/2607.09532v1#S6.SS1 | Not Disclosed — The implementation is explicitly a toy proof of concept, not an end-to-end robust LLM backdoor demonstration; the durable evidence is the stated theoretical possibility under its assumptions. | claim:SF-2026-ARXIV-2607-09532 | complete |
| SF-2026-ARXIV-2607-09553 | RP-47f079e0b07c3e55 | standard | arXiv:2607.09553v1 | SRC-ARXIV@arXiv:2607.09553v1 | https://arxiv.org/html/2607.09553v1#S2.SS4 | https://arxiv.org/html/2607.09553v1#S3.SS2 | https://arxiv.org/html/2607.09553v1#S6 | Not Disclosed — Fields are coded largely as present/absent and deletions are artificial; odds ratios remain tied to the sampled repositories and agents. | claim:SF-2026-ARXIV-2607-09553 | complete |
| SF-2026-ARXIV-2607-09560 | RP-e40f58d4f6b0f836 | standard | arXiv:2607.09560v1 | SRC-ARXIV@arXiv:2607.09560v1 | https://arxiv.org/html/2607.09560v1#S3.SS1 | Not Required — conceptual paper has no empirical evaluation contract | https://arxiv.org/html/2607.09560v1#S8 | Not Disclosed — This is a conceptual framework without a new empirical evaluation contract; it can motivate a structural question but cannot support implementation or performance claims. | claim:SF-2026-ARXIV-2607-09560 | complete |
| SF-2026-ARXIV-2607-09586 | RP-903a1a29c7e38878 | standard | arXiv:2607.09586v1 | SRC-ARXIV@arXiv:2607.09586v1 | https://arxiv.org/html/2607.09586v1#S2.SS1; https://arxiv.org/html/2607.09586v1#S3 | https://arxiv.org/html/2607.09586v1#S5 | https://arxiv.org/html/2607.09586v1#S6.SS3 | Not Disclosed — The rubric is an internally created framework, not an authoritative legal classification or validated predictor of harm. | claim:SF-2026-ARXIV-2607-09586 | complete |
| SF-2026-ARXIV-2607-09590 | RP-9f5692c30bf683a0 | deep | arXiv:2607.09590v1 | SRC-ARXIV@arXiv:2607.09590v1 | https://arxiv.org/html/2607.09590v1#S3 | https://arxiv.org/html/2607.09590v1#S4; https://arxiv.org/html/2607.09590v1#S4.SS9 | https://arxiv.org/html/2607.09590v1#S5 | Not Disclosed — The result is scoped to the reported manipulation environments, 16 parallel environments and disclosed PPO/architecture ablations; no real-robot deployment claim is inferred. | claim:SF-2026-ARXIV-2607-09590 | complete |
| SF-2026-ARXIV-2607-09600 | RP-b7cec3d6569e3677 | standard | arXiv:2607.09600v1 | SRC-ARXIV@arXiv:2607.09600v1 | https://arxiv.org/html/2607.09600v1#S2.SS1; https://arxiv.org/html/2607.09600v1#S3 | https://arxiv.org/html/2607.09600v1#S4.SS4 | https://arxiv.org/html/2607.09600v1#S5 | Not Disclosed — Results use the benchmark-specific model pools and calibration procedure in exact v1; provider prices, latency and availability are not universal. | claim:SF-2026-ARXIV-2607-09600 | complete |
| SF-2026-ARXIV-2607-09603 | RP-5dc3e4ee0bfee441 | deep | arXiv:2607.09603v1 | SRC-ARXIV@arXiv:2607.09603v1 | https://arxiv.org/html/2607.09603v1#S3; https://arxiv.org/html/2607.09603v1#A2 | https://arxiv.org/html/2607.09603v1#S4; https://arxiv.org/html/2607.09603v1#A5 | https://arxiv.org/html/2607.09603v1#A6 | Not Disclosed — Results are simulator-bound and assume reliable localization except for tested moderate noise; the paper does not provide evidence for raw-sensor or low-level controller robustness. | claim:SF-2026-ARXIV-2607-09603 | complete |
| SF-2026-ARXIV-2607-09661 | RP-b903423cae2f2d14 | deep | arXiv:2607.09661v1 | SRC-ARXIV@arXiv:2607.09661v1 | https://arxiv.org/html/2607.09661v1#S4; https://arxiv.org/html/2607.09661v1#A2.SS3 | https://arxiv.org/html/2607.09661v1#S3; https://arxiv.org/html/2607.09661v1#S5 | https://arxiv.org/html/2607.09661v1#A4.SS2 | Not Disclosed — The benchmark and generated rollouts measure panoramic synthesis, not a verified physical simulator or policy-success contract. | claim:SF-2026-ARXIV-2607-09661 | complete |

### Source Reviews

<!-- review:SF-2026-ARXIV-2607-08774:start -->
### CogniConsole: Externalizing Inference-Time Control as a Formal Abstraction for Reliable LLM Interactions

<!-- claim:SF-2026-ARXIV-2607-08774:start -->Inference-time reliability is partly owned by an explicit control layer that separates task framing, context selection, reasoning procedure, output constraints, memory reactivation and model routing from the pretrained model. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-08774:end -->

**为什么进入候选分母。** 把 task framing 与 context selection 从模型隐式行为提升为可编排的 inference-time control interface，改变可靠性交付的控制边界。

**机制与状态边界。** CogniConsole decomposes control into a programmatic console, task cartridges and bounded decision-ladder nodes; hard control is kept outside fuzzy generation and state is selectively reactivated rather than replayed wholesale.

**证据证明什么。** Within 489 controllability probes, additional external structure can change reliability independently of model weights.

**证据没有证明什么。** The probes do not establish that this decomposition is optimal, production-safe, or portable across all models, tasks and long-running state stores.

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.08774v1#S3; https://arxiv.org/html/2607.08774v1#S4。Evaluation：https://arxiv.org/html/2607.08774v1#S5。Limitations / counterevidence：https://arxiv.org/html/2607.08774v1#S8; https://arxiv.org/html/2607.08774v1#S9。

**Artifact boundary。** The article links https://github.com/Cogniconsole/cogniconsole but does not pin an event-time commit; the repository is not used to support v1 mechanism or benchmark claims.

**Trade-off 与共存边界。** Explicit control improves attribution and composability but creates more orchestration state, interface design, policy enforcement and recovery obligations.

- Score V2：Design Delta 3 / System Reach 2 / Durability 2 = **7/9**。
- Stable owner 候选：`AGENT-PLATFORM`；evidence-stage relation：`Layering / Dependency`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-08774:end -->

<!-- review:SF-2026-ARXIV-2607-08780:start -->
### Sticky Routing: Training MoE Models for Memory-Efficient Inference

<!-- claim:SF-2026-ARXIV-2607-08780:start -->Expert swap pressure can be reduced at training time by making routing temporally sticky, not only at serving time through caches or placement heuristics. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-08780:end -->

**为什么进入候选分母。** 用训练期 routing-consistency objective 改变 MoE expert residency 的时间局部性，把边缘推理换页压力前移为训练约束。

**机制与状态边界。** A differentiable consistency loss penalizes abrupt top-k expert changes between adjacent semantically coherent tokens; no expert architecture change is required, but the learned router now carries an inference-locality objective.

**证据证明什么。** The reported models show that router-switch regularization can improve expert locality while retaining the evaluated quality envelope.

**证据没有证明什么。** The paper does not establish the same benefit for large production MoEs, arbitrary tokenization, expert-parallel clusters, or workloads whose optimal experts change rapidly.

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.08780v1#S4; https://arxiv.org/html/2607.08780v1#S4.SS5。Evaluation：https://arxiv.org/html/2607.08780v1#S5; https://arxiv.org/html/2607.08780v1#S5.SS6。Limitations / counterevidence：https://arxiv.org/html/2607.08780v1#S6; https://arxiv.org/html/2607.08780v1#A4。

**Artifact boundary。** The article links https://github.com/alikayyam/sticky_moe.git without an event-time commit; code is not used as exact-v1 evidence.

**Trade-off 与共存边界。** Locality reduces weight movement but constrains conditional capacity and adds a training hyperparameter; excessive stickiness may keep tokens on a suboptimal expert.

- Score V2：Design Delta 3 / System Reach 2 / Durability 3 = **8/9**。
- Stable owner 候选：`MODEL-MOE`；evidence-stage relation：`Cross-Layer Co-Design`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-08780:end -->

<!-- review:SF-2026-ARXIV-2607-08782:start -->
### Director: Accelerating Distributed MoE Serving via Online Proactive Expert Placement

<!-- claim:SF-2026-ARXIV-2607-08782:start -->Distributed MoE placement must become a predictive online control loop when expert demand changes faster than historical placement can adapt. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-08782:end -->

**为什么进入候选分母。** 为变化请求分布建立在线 expert placement、迁移成本与预测不确定性共同驱动的 MoE serving control loop。

**机制与状态边界。** A reconfiguration manager predicts routing from queued requests; a relaxation-based optimizer computes a bounded placement; live migration overlaps expert movement with compute and limits downtime.

**证据证明什么。** The prototype and approximation analysis support proactive placement under the paper's predicted-routing and migration model.

**证据没有证明什么。** It does not prove robustness to adversarial prediction error, heterogeneous failure domains, cross-cluster migration, or production tail-SLO behavior.

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.08782v1#S4; https://arxiv.org/html/2607.08782v1#S5; https://arxiv.org/html/2607.08782v1#S6。Evaluation：https://arxiv.org/html/2607.08782v1#S7; https://arxiv.org/html/2607.08782v1#S8。Limitations / counterevidence：https://arxiv.org/html/2607.08782v1#S9。

**Artifact boundary。** The article cites EPLB as related software but does not publish a pinned Director implementation; cited repositories are not Director provenance.

**Trade-off 与共存边界。** Proactivity reduces expected communication imbalance but adds prediction error, optimization delay, migration bandwidth, placement-version state and rollback requirements.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`INFER-SCHEDULING`；evidence-stage relation：`Direct Evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-08782:end -->

<!-- review:SF-2026-ARXIV-2607-08786:start -->
### Accelerating GPU Inference of Large Language Models with Moderately Unstructured Sparse Weight Matrices

<!-- claim:SF-2026-ARXIV-2607-08786:start -->Moderate unstructured sparsity needs a storage and kernel design distinct from both dense GEMM and very-high-sparsity SpMM. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-08786:end -->

**为什么进入候选分母。** 针对中等非结构稀疏在 GPU 上不胜 dense kernel 的断层，联合改变矩阵布局、Tensor Core 映射与执行流水。

**机制与状态边界。** A three-layer format combines Sparse Tensor Core-compatible regions, slot filling for surplus nonzeros and a residual path; the kernel pipelines metadata, sparse operands and residual work for memory-bound decode.

**证据证明什么。** The evaluated format/kernel can beat compared sparse and dense paths around the paper's moderate-sparsity, small-N decode region.

**证据没有证明什么。** It is slower than cuBLAS in compute-bound large-N prefill and does not beat the cited high-sparsity design in its native regime.

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.08786v1#S3; https://arxiv.org/html/2607.08786v1#S4。Evaluation：https://arxiv.org/html/2607.08786v1#S5。Limitations / counterevidence：https://arxiv.org/html/2607.08786v1#S6。

**Artifact boundary。** No author implementation is pinned in exact v1.

**Trade-off 与共存边界。** The method gains decode throughput by paying format complexity, padding, residual bookkeeping and dependence on sparse Tensor Cores/HBM behavior.

- Score V2：Design Delta 3 / System Reach 2 / Durability 3 = **8/9**。
- Stable owner 候选：`INFER-TENSORRT-LLM`；evidence-stage relation：`Alternative Branch`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-08786:end -->

<!-- review:SF-2026-ARXIV-2607-08839:start -->
### Mixture of Probes: Learning from Privileged Modalities in Multimodal LLMs Through Probing

<!-- claim:SF-2026-ARXIV-2607-08839:start -->A training-only privileged modality can improve a deployment-time modality only if supervision separates modality-specific signal from shared structure instead of assuming all encoders expose one interchangeable representation. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-08839:end -->

**为什么进入候选分母。** 显式区分 training-only privileged modality 与 inference-available modality，改变多模态表示监督和部署输入 contract。

**机制与状态边界。** Mixture of Probes learns several modality-pair probes in a shared encoder and adds a disentanglement objective to prevent probe collapse; privileged streams supervise representation learning but are removed at inference.

**证据证明什么。** On the reported tasks, disentangled probes make auxiliary training modalities improve single-modality evaluation more than collapsed/shared probes.

**证据没有证明什么。** The result does not establish transfer across arbitrary sensor encoders, missing-modality distributions or production preprocessing.

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.08839v1#S4; https://arxiv.org/html/2607.08839v1#S5.SS4。Evaluation：https://arxiv.org/html/2607.08839v1#S5.SS1。Limitations / counterevidence：https://arxiv.org/html/2607.08839v1#S6。

**Artifact boundary。** Evidence is limited to the shared-encoder design and ADL/music benchmarks in exact v1; heterogeneous encoders are explicitly outside scope.

**Trade-off 与共存边界。** Privileged supervision can enrich the deployed representation but adds synchronized data, training-only dependencies and a train/serve modality gap.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`MULTIMODAL-REPRESENTATION`；evidence-stage relation：`Alternative Branch`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-08839:end -->

<!-- review:SF-2026-ARXIV-2607-08857:start -->
### AgenticFocus: Object-Preserving Mixed Reality Synthesis from Human FPV Video for Dexterous Humanoid Learning

<!-- claim:SF-2026-ARXIV-2607-08857:start -->Human first-person video becomes a robot-training asset only after preserving manipulated objects while translating hands, pose and timing into a robot-consistent action schema. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-08857:end -->

**为什么进入候选分母。** 把普通人类第一视角视频转换为带同步 robot action/state 的训练资产，改变 embodiment retargeting 与数据 provenance 链。

**机制与状态边界。** AgenticFocus restores occluded object regions, retargets full hands in camera coordinates, smooths trajectories and composites robot hands while emitting synchronized video plus structured arm, finger and camera-relative state.

**证据证明什么。** Against named retargeting baselines, the pipeline improves trajectory error and wrist-motion smoothness for the evaluated sequences.

**证据没有证明什么。** It does not establish contact correctness, policy learning benefit, sim-to-real transfer or generality across robot morphologies.

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.08857v1#S1。Evaluation：https://arxiv.org/html/2607.08857v1#S2.SS1。Limitations / counterevidence：https://arxiv.org/html/2607.08857v1#S3。

**Artifact boundary。** The evaluation uses EPIC-KITCHENS and internally processed clips at 30 FPS; the resulting mixed-reality corpus is not evidence of downstream policy success.

**Trade-off 与共存边界。** Retargeting expands demonstration supply but inserts restoration, coordinate, kinematic and temporal errors that need provenance and downstream filtering.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`MULTIMODAL-EMBODIED-VLA`；evidence-stage relation：`Layering / Dependency`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-08857:end -->

<!-- review:SF-2026-ARXIV-2607-08877:start -->
### FlowDAgger: Human-in-the-Loop Adaptation of Generative Robot Policies in Latent Space

<!-- claim:SF-2026-ARXIV-2607-08877:start -->A frozen generative robot policy can be adapted from sparse human interventions by learning in its latent noise space instead of updating the base policy weights. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-08877:end -->

**为什么进入候选分母。** 把人类干预反演到冻结生成策略的 latent/noise state，提出无需完整在线 RL 的物理策略修复路径。

**机制与状态边界。** Action inversion maps corrective actions to the latent noise that would generate them; a small noise policy learns those targets and steers the frozen flow/diffusion policy, including world-action models without a separate action head.

**证据证明什么。** The paper evaluates sample/compute-efficient correction on simulation and real manipulation within the support of the tested base policies.

**证据没有证明什么。** Latent steering cannot create behavior outside the pretrained action manifold and depends on the coverage and consistency of human interventions.

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.08877v1#S4; https://arxiv.org/html/2607.08877v1#A1。Evaluation：https://arxiv.org/html/2607.08877v1#S5; https://arxiv.org/html/2607.08877v1#A2。Limitations / counterevidence：https://arxiv.org/html/2607.08877v1#S6。

**Artifact boundary。** No event-time implementation commit is pinned in exact v1.

**Trade-off 与共存边界。** Freezing weights limits catastrophic drift and training cost, but caps adaptation expressivity and inherits conditioning errors from inversion.

- Score V2：Design Delta 3 / System Reach 2 / Durability 2 = **7/9**。
- Stable owner 候选：`MULTIMODAL-EMBODIED-VLA`；evidence-stage relation：`Alternative Branch`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-08877:end -->

<!-- review:SF-2026-ARXIV-2607-08883:start -->
### Optimizing Against Safety Representations: Activation-Guided Adversarial Suffixes and the Geometry of Refusal

<!-- claim:SF-2026-ARXIV-2607-08883:start -->Low-dimensional refusal representations are an attack surface: directly optimizing internal refusal directions can jailbreak models more efficiently than output-only objectives. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-08883:end -->

**为什么进入候选分母。** 证明 refusal representation 可被跨层/位置目标直接优化攻击，构成现有 alignment 安全边界的强制反证审阅。

**机制与状态边界。** Activation-Guided GCG suppresses refusal across layers/positions; Soft-GCG relaxes discrete suffix search into continuous optimization before discretization.

**证据证明什么。** Under white-box access and the evaluated models, representation-targeted objectives expose refusal fragility and reduce attack cost.

**证据没有证明什么。** The result does not imply all alignment is one linear direction, transfer to closed models, or that the reported attack succeeds under production defenses.

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.08883v1#Sx3。Evaluation：https://arxiv.org/html/2607.08883v1#Sx4。Limitations / counterevidence：https://arxiv.org/html/2607.08883v1#Sx5; https://arxiv.org/html/2607.08883v1#Sx5.SSx1。

**Artifact boundary。** No event-time attack implementation is pinned in exact v1.

**Trade-off 与共存边界。** Representation-level defenses require broader monitoring and adversarial testing, while publishing efficient attacks increases dual-use exposure.

- Score V2：Design Delta 3 / System Reach 2 / Durability 2 = **7/9**。
- Stable owner 候选：`PLATFORM-SECURITY`；evidence-stage relation：`Counterevidence / Correction`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-08883:end -->

<!-- review:SF-2026-ARXIV-2607-08894:start -->
### GATS: Graph-Augmented Tree Search with Layered World Models for Efficient Agent Planning

<!-- claim:SF-2026-ARXIV-2607-08894:start -->When actions have reusable transition structure, agent planning can move repeated model calls into a layered world model and explicit graph search. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-08894:end -->

**为什么进入候选分母。** 将 agent planning 的 repeated LLM call 改为 exact/log-statistical/learned 三层 world model 与可复用图状态。

**机制与状态边界。** GATS uses UCB-guided tree search over a graph, preferring exact action specifications, then statistical models, and invoking an LLM only to bootstrap missing transition knowledge.

**证据证明什么。** In the constructed branching/dead-end tasks, explicit search with known transitions outperforms the reported LLM-guided baselines while eliminating planning-time LLM calls.

**证据没有证明什么。** It does not establish model-call elimination in open domains or robustness to incorrect transition models.

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.08894v1#S3; https://arxiv.org/html/2607.08894v1#S5.SS4。Evaluation：https://arxiv.org/html/2607.08894v1#S4.SS1。Limitations / counterevidence：https://arxiv.org/html/2607.08894v1#S7。

**Artifact boundary。** The headline planning results use synthetic tasks whose exact transitions make the lowest layer cover 100%; the open-domain layer-use figures are projections, not observations.

**Trade-off 与共存边界。** Reusable world state reduces stochastic reasoning cost but shifts risk to model bootstrapping, stale transitions and search-space growth.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`AGENT-PLANNING`；evidence-stage relation：`Alternative Branch`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-08894:end -->

<!-- review:SF-2026-ARXIV-2607-08925:start -->
### SafeExplorer: An Unbiased Policy Gradient for Reinforcement Learning with Recovery Interventions

<!-- claim:SF-2026-ARXIV-2607-08925:start -->Recovery interventions change the behavior policy and must be excluded or corrected in the main policy gradient; treating mixed-policy transitions as on-policy silently biases learning. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-08925:end -->

**为什么进入候选分母。** 恢复策略接管会污染 on-policy rollout；论文改变 intervention ownership 与 policy-gradient correctness contract。

**机制与状态边界。** SafeExplorer masks recovery transitions from the policy gradient, relates mixed-policy training return to deployment return, substitutes an analytic recovery value under deterministic assumptions and imitates recovery only after successful segments.

**证据证明什么。** The evaluated locomotion environments support fewer training falls for the proposed intervention-aware update in the reported regimes.

**证据没有证明什么。** The analytic value is exact only under deterministic dynamics/recovery; the observable safety certificate and general physical-robot transfer remain open.

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.08925v1#S4; https://arxiv.org/html/2607.08925v1#S5。Evaluation：https://arxiv.org/html/2607.08925v1#S6; https://arxiv.org/html/2607.08925v1#S7; https://arxiv.org/html/2607.08925v1#S8。Limitations / counterevidence：https://arxiv.org/html/2607.08925v1#S9; https://arxiv.org/html/2607.08925v1#A5.SS11。

**Artifact boundary。** The article cites MuJoCo assets but does not pin a SafeExplorer implementation; dependency repositories are not method provenance.

**Trade-off 与共存边界。** A permanent fallback lowers damage risk but changes data ownership, requires a safe-region contract and can cap exploration or imitate recovery errors.

- Score V2：Design Delta 3 / System Reach 2 / Durability 2 = **7/9**。
- Stable owner 候选：`TRAIN-PPO`；evidence-stage relation：`Direct Evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-08925:end -->

<!-- review:SF-2026-ARXIV-2607-08930:start -->
### BlockServe: Block-Grained Continuous Batching for High-Throughput Diffusion LLM Serving

<!-- claim:SF-2026-ARXIV-2607-08930:start -->Diffusion language models need block-denoise scheduling and mixed-state execution rather than assuming every batched sequence advances one autoregressive token at a time. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-08930:end -->

**为什么进入候选分母。** 把 continuous batching 的调度量子从 AR token iteration 改成 diffusion block-denoise cycle，并引入 mixed-state execution。

**机制与状态边界。** Completed requests are evicted at block boundaries, heterogeneous denoising states are gathered into one dense layout, and token-budget admission refills capacity.

**证据证明什么。** The paper reports throughput and capacity gains for two diffusion LMs under offline batching on one H200 while retaining its measured generation-quality envelope.

**证据没有证明什么。** Online arrivals, production tail latency, fairness and multi-GPU behavior are explicitly outside the evaluation.

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.08930v1#S2。Evaluation：https://arxiv.org/html/2607.08930v1#S3。Limitations / counterevidence：https://arxiv.org/html/2607.08930v1#S5。

**Artifact boundary。** No event-time implementation commit is pinned in exact v1.

**Trade-off 与共存边界。** Smaller blocks reclaim slots sooner but add scheduling/denoising overhead; mixed-state metadata and approximate parallel decoding enlarge correctness and quality risk.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`INFER-CONTINUOUS-BATCHING`；evidence-stage relation：`Direct Evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-08930:end -->

<!-- review:SF-2026-ARXIV-2607-08938:start -->
### Better Harnesses, Smaller Models: Building 90% Cheaper Agents via Automated Harness Adaptation

<!-- claim:SF-2026-ARXIV-2607-08938:start -->Agent capability is a property of model plus harness; task-shared reasoning can sometimes be moved into instructions, tools and orchestration so a smaller model remains viable. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-08938:end -->

**为什么进入候选分母。** 把部分任务难度从大模型迁移到可搜索的 harness、tools 与 orchestration loop，改变 model/harness 能力分工与成本判断。

**机制与状态边界。** A meta-agent diagnoses failure categories and searches harness adaptations instead of merely swapping the model inside a frontier-model scaffold.

**证据证明什么。** For seven curated business task families, harness adaptation can materially change the cost/performance frontier of smaller models.

**证据没有证明什么。** The headline cost result does not generalize to novel, safety-critical or open-ended tasks, and includes no universal rule for which reasoning can be externalized.

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.08938v1#S2; https://arxiv.org/html/2607.08938v1#S4.SS2。Evaluation：https://arxiv.org/html/2607.08938v1#S4。Limitations / counterevidence：https://arxiv.org/html/2607.08938v1#S4.SS3; https://arxiv.org/html/2607.08938v1#S5。

**Artifact boundary。** The article links https://github.com/malusamayo/migration-analysis without an event-time commit; the repository is not treated as exact-v1 benchmark provenance.

**Trade-off 与共存边界。** Moving capability to the harness lowers inference cost but increases task-specific engineering, routing state, maintenance burden and hidden coupling between scaffold and evaluator.

- Score V2：Design Delta 3 / System Reach 2 / Durability 2 = **7/9**。
- Stable owner 候选：`AGENT-PLATFORM`；evidence-stage relation：`Layering / Dependency`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-08938:end -->

<!-- review:SF-2026-ARXIV-2607-08940:start -->
### TSRouter: Dynamic Modality-Model Selection for Time Series Reasoning

<!-- claim:SF-2026-ARXIV-2607-08940:start -->Time-series reasoning has no universally best representation: exact numeric relations may favour text while global shape may favour plots, so modality and model should be routed jointly. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-08940:end -->

**为什么进入候选分母。** 在 exact numeric text 与 global visual pattern 之间动态选择 modality/model，把多模态路由提升为成本约束下的运行时决策。

**机制与状态边界。** TSRouter builds a heterogeneous graph over queries, tasks, modalities and candidate models, then selects a text/visual representation and model under accuracy-cost objectives and updates from observed performance.

**证据证明什么。** The evaluated router improves measured accuracy-cost trade-offs and transfers to named unseen tasks/models without retraining.

**证据没有证明什么。** It does not establish stable calibration under changing APIs, latency SLOs or arbitrary time-series transformations.

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.08940v1#S2; https://arxiv.org/html/2607.08940v1#A4。Evaluation：https://arxiv.org/html/2607.08940v1#S3.SS1。Limitations / counterevidence：https://arxiv.org/html/2607.08940v1#S5。

**Artifact boundary。** Results are bound to TSRBench plus two transfer tasks and the stated LLM/VLM pool; combined-modality interference is a case observation, not a universal law.

**Trade-off 与共存边界。** Routing avoids one-size-fits-all modality but adds representation generation, calibration state and model-availability dependencies.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`MULTIMODAL-REPRESENTATION`；evidence-stage relation：`Alternative Branch`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-08940:end -->

<!-- review:SF-2026-ARXIV-2607-08948:start -->
### SplatCtrl: Perception-Action Coupling via Gaussian Scene Representations and Reactive Robot Control

<!-- claim:SF-2026-ARXIV-2607-08948:start -->An incrementally updated scene representation can be the shared state joining perception and reactive control, rather than a visualization-only output. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-08948:end -->

**为什么进入候选分母。** 把持续更新的 Gaussian scene state 直接接到 reactive collision-free control，形成 perception-state-action 闭环。

**机制与状态边界。** RGB-D streams update a Gaussian scene with voxel filtering and relocation; the representation yields continuous distance fields consumed by motion planning and reactive collision avoidance.

**证据证明什么。** Simulation, physical robot and pilot shared-workspace evaluations support the proposed perception-control coupling in the tested scenes.

**证据没有证明什么。** Large environments, broader tasks and grasped-object collision are not established; sphere approximations discard Gaussian uncertainty structure.

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.08948v1#S3。Evaluation：https://arxiv.org/html/2607.08948v1#S4。Limitations / counterevidence：https://arxiv.org/html/2607.08948v1#S5。

**Artifact boundary。** No event-time implementation commit is pinned in exact v1.

**Trade-off 与共存边界。** A unified mutable state reduces handoff latency but adds tuning, approximate geometry, sensor-calibration dependence and state-consistency obligations.

- Score V2：Design Delta 3 / System Reach 2 / Durability 2 = **7/9**。
- Stable owner 候选：`MULTIMODAL-EMBODIED-VLA`；evidence-stage relation：`Direct Evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-08948:end -->

<!-- review:SF-2026-ARXIV-2607-08949:start -->
### SeedSmith: LLM-Driven Seed Synthesis for Directed Fuzzing

<!-- claim:SF-2026-ARXIV-2607-08949:start -->An LLM is most useful to fuzzing when it converts program structure and a crash precondition into targeted initial seeds, while the traditional fuzzer retains mutation, coverage and crash ownership. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-08949:end -->

**为什么进入候选分母。** 利用程序控制流与 crash precondition 生成定向 fuzzing seed，改变 agent 与传统 fuzzer 的职责边界。

**机制与状态边界。** SeedSmith identifies sink functions, uses CodeQL-supported control flow and a scan strategy to infer trigger constraints, asks the model for seeds, and hands them to four conventional fuzzers.

**证据证明什么。** For the evaluated bugs, targeted model-generated seeds reduce time to selected crashes across several fuzzers, with mixed ablation effects.

**证据没有证明什么。** The approach depends on sink precision and model code reasoning and does not discover arbitrary unknown vulnerability locations.

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.08949v1#S4; https://arxiv.org/html/2607.08949v1#S5。Evaluation：https://arxiv.org/html/2607.08949v1#S6.SS1; https://arxiv.org/html/2607.08949v1#S6.SS4。Limitations / counterevidence：https://arxiv.org/html/2607.08949v1#S7。

**Artifact boundary。** The 24-hour, ten-trial Magma/ARVO protocol and canary-confirmed crashes define the claim; the first crashing stack function is supplied as sink.

**Trade-off 与共存边界。** Semantic seed synthesis improves reachability but adds LLM cost and failure modes from wrong root-cause or constraint inference.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`AGENT-TOOL-CALLING`；evidence-stage relation：`Layering / Dependency`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-08949:end -->

<!-- review:SF-2026-ARXIV-2607-08961:start -->
### NL-PAC: Specification Ambiguity and Certified Minimax Risk Floors in LLM-Mediated Supervision

<!-- claim:SF-2026-ARXIV-2607-08961:start -->When a natural-language specification permits several model-admissible readings and the supervision channel hides which reading is active, more labels reduce sampling error but cannot remove identification error. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-08961:end -->

**为什么进入候选分母。** 给出自然语言 specification ambiguity 下不可由更多标签消除的 minimax risk floor，改变监督与评测可识别性假设。

**机制与状态边界。** NL-PAC separates task ambiguity, decoding randomness, target error and channel indistinguishability; the diameter of the pointwise-admissible target class yields a minimax risk floor under target-blind supervision.

**证据证明什么。** Under the stated model-admissibility and target-blind channel assumptions, the paper proves a lower bound that additional ambiguous supervision cannot cross.

**证据没有证明什么。** The floor is not a universal empirical hallucination rate and depends on the fixed model, thresholded decoding law and channel assumptions.

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.08961v1#S2; https://arxiv.org/html/2607.08961v1#S4。Evaluation：https://arxiv.org/html/2607.08961v1#S5; https://arxiv.org/html/2607.08961v1#A3。Limitations / counterevidence：https://arxiv.org/html/2607.08961v1#S6。

**Artifact boundary。** Exact v1 provides reproducibility diagnostics but no event-time implementation artifact is needed for the certified mathematical floor.

**Trade-off 与共存边界。** Auditing admissible readings exposes irreducible ambiguity, but requires extra sampling and a declared supervision channel; changing the specification or collecting disambiguating evidence may be cheaper.

- Score V2：Design Delta 3 / System Reach 2 / Durability 2 = **7/9**。
- Stable owner 候选：`PLATFORM-EVALUATION-SYSTEM`；evidence-stage relation：`Principle Reuse`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-08961:end -->

<!-- review:SF-2026-ARXIV-2607-08964:start -->
### Long-Horizon-Terminal-Bench: Testing the Limits of Agents on Long-Horizon Terminal Tasks with Dense Reward-Based Grading

<!-- claim:SF-2026-ARXIV-2607-08964:start -->Binary task success is an insufficient evaluation interface for long-horizon terminal agents because it conflates no progress, partial progress, timeout, premature exit and harness failure. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-08964:end -->

**为什么进入候选分母。** 用可执行长时 terminal 环境和 dense progress grading 改变 agent failure/recovery 的评测合同。

**机制与状态边界。** Forty-six executable tasks use reference solutions or simulators plus dense subtask grading; runs also record termination cause so capability and agent-environment failures can be separated.

**证据证明什么。** On the released task suite, dense rewards rank models that binary pass/fail leaves tied and expose timeout/early-exit/harness-error distinctions.

**证据没有证明什么。** Dense rubric scores are not automatically comparable across unrelated task suites and can encode reference-solution bias.

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.08964v1#S2; https://arxiv.org/html/2607.08964v1#S3.SS2。Evaluation：https://arxiv.org/html/2607.08964v1#S3。Limitations / counterevidence：https://arxiv.org/html/2607.08964v1#S3.SS4; https://arxiv.org/html/2607.08964v1#S5。

**Artifact boundary。** The report evaluates a concrete benchmark, but this review does not treat later benchmark revisions as v1 evidence.

**Trade-off 与共存边界。** Richer evidence improves diagnosis but increases task-authoring, grader maintenance, hidden-test and reward-gaming risk.

- Score V2：Design Delta 2 / System Reach 3 / Durability 2 = **7/9**。
- Stable owner 候选：`PLATFORM-EVALUATION-SYSTEM`；evidence-stage relation：`Direct Evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-08964:end -->

<!-- review:SF-2026-ARXIV-2607-08973:start -->
### SiFAR: Synchronization-Free All-Reduce for Low-Latency LLM Inference

<!-- claim:SF-2026-ARXIV-2607-08973:start -->For low-batch tensor-parallel decode, collective barriers can dominate because there is too little compute to hide communication; the result can be committed after speculative fetch only when buffer generation is validated. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-08973:end -->

**为什么进入候选分母。** 以 dual buffer、redundant pull 与 speculate-verify-retry 改写低 batch TP decode 的 collective 同步路径。

**机制与状态边界。** SiFAR uses dual buffers to remove one reuse barrier, switch-assisted redundant pull to reduce transfer work, and speculative result fetch followed by a compact validation flag and retry path.

**证据证明什么。** Under the evaluated low-batch H200 configurations, the protocol reduces collective latency and improves end-to-end token throughput relative to the reported baselines.

**证据没有证明什么。** It does not establish correctness or benefit across arbitrary fabrics, imbalance, process failure, larger asynchronous jobs or conventional unfused serving engines.

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.08973v1#S3; https://arxiv.org/html/2607.08973v1#S4.SS2。Evaluation：https://arxiv.org/html/2607.08973v1#S5; https://arxiv.org/html/2607.08973v1#S6。Limitations / counterevidence：https://arxiv.org/html/2607.08973v1#S2.SS5; https://arxiv.org/html/2607.08973v1#S9。

**Artifact boundary。** Evidence is bound to the Megakernel integration, one 8xH200 topology and reported model, precision, batch and length settings; cited frameworks are not SiFAR provenance.

**Trade-off 与共存边界。** Removing expected barriers adds buffer-generation state, speculative validation and retry; standard collectives remain safer when topology support or progress assumptions do not hold.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`INFER-TENSORRT-LLM`；evidence-stage relation：`Direct Evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-08973:end -->

<!-- review:SF-2026-ARXIV-2607-08974:start -->
### CLAP: Direct VLM-to-VLA Adaptation via Language-Action Grounding

<!-- claim:SF-2026-ARXIV-2607-08974:start -->A pretrained VLM can be adapted to continuous robot control more reliably when each numeric action sequence is preceded by a natural-language action description that bridges its language output distribution to action tokens. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-08974:end -->

**为什么进入候选分母。** 以 natural-language action prefix 对齐 VLM language output 与连续 robot action distribution，并用多尺度及 real-robot evaluation 检验轻量 VLM-to-VLA 迁移。

**机制与状态边界。** CLAP serializes a language action prefix before numeric action chunks, performs single-epoch end-to-end fine-tuning on one 8-GPU node, and compares 0.8B, 2B and 4B backbones in simulation and real-robot pick-and-place settings.

**证据证明什么。** Within the evaluated tasks, the language-action bridge improves over the named size-matched baseline and the 2B model outperforms the 4B variant, countering parameter count as the sole transfer predictor.

**证据没有证明什么。** The study does not establish broad object/embodiment transfer, long-horizon safety, high-frequency control or superiority over all VLA adaptation recipes.

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.08974v1#S3; https://arxiv.org/html/2607.08974v1#S4。Evaluation：https://arxiv.org/html/2607.08974v1#S5; https://arxiv.org/html/2607.08974v1#A2.SS4。Limitations / counterevidence：https://arxiv.org/html/2607.08974v1#S6。

**Artifact boundary。** The reported LIBERO/LIBERO-PRO and three-object real-robot tasks define the result; the real-robot unseen objects are distractors, not unseen pick targets.

**Trade-off 与共存边界。** Language prefixes exploit pretrained semantics and simplify adaptation but add decoding/state overhead and can inject linguistic ambiguity into precise control.

- Score V2：Design Delta 3 / System Reach 2 / Durability 2 = **7/9**。
- Stable owner 候选：`MULTIMODAL-EMBODIED-VLA`；evidence-stage relation：`Direct Evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-08974:end -->

<!-- review:SF-2026-ARXIV-2607-08991:start -->
### Sensitivity-Aware Thresholding and Token Routingfor Activation Sparsification in Large Language Models

<!-- claim:SF-2026-ARXIV-2607-08991:start -->Activation sparsity should be calibrated against layer-output sensitivity and applied conditionally by token, rather than setting every layer from activation percentiles alone. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-08991:end -->

**为什么进入候选分母。** 把 activation sparsity 的 layer threshold 从 percentile heuristic 改为输出敏感度校准，并引入 token-level conditional compute。

**机制与状态边界。** SATS chooses layer thresholds from an MLP output-sensitivity proxy; token routing chooses dense or sparse execution according to token importance, with the final MLP retained as a guardrail in the reported setup.

**证据证明什么。** For Llama-3.1-8B and Qwen3-8B at the evaluated sparsity points, sensitivity calibration and token routing improve the measured quality-throughput frontier over percentile calibration.

**证据没有证明什么。** The paper explicitly avoids 70-90% sparsity, finds 30% gains too small, and does not establish portability to other architectures or kernels.

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.08991v1#S3。Evaluation：https://arxiv.org/html/2607.08991v1#S4; https://arxiv.org/html/2607.08991v1#S4.SS2。Limitations / counterevidence：https://arxiv.org/html/2607.08991v1#S5。

**Artifact boundary。** No event-time implementation commit is pinned in exact v1.

**Trade-off 与共存边界。** Conditional compute preserves important tokens but adds calibration data, routing metadata, branch/kernel complexity and possible distribution-shift errors.

- Score V2：Design Delta 3 / System Reach 2 / Durability 3 = **8/9**。
- Stable owner 候选：`INFER-TENSORRT-LLM`；evidence-stage relation：`Direct Evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-08991:end -->

<!-- review:SF-2026-ARXIV-2607-08993:start -->
### StreamDQ: Near-Memory Weight DeQuantization in Custom HBM for Scalable AI Inference Acceleration

<!-- claim:SF-2026-ARXIV-2607-08993:start -->For large-batch quantized inference, dequantization can become a memory-system operation instead of CUDA-core work and intermediate HBM traffic. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-08993:end -->

**为什么进入候选分母。** 把 weight dequantization 从 CUDA execution path 下沉到 custom HBM near-memory block，改变数据移动与硬件状态所有权。

**机制与状态边界。** DeQuantization Blocks in the HBM base die transform tagged quantized loads on the fly while preserving GPU load semantics; sideband metadata selects format and parameters.

**证据证明什么。** The simulator supports architectural feasibility and projected benefits within its modeled HBM area, power, thermal and workload assumptions.

**证据没有证明什么。** Simulation does not prove realized silicon timing, manufacturability, vendor adoption, or gains for small-batch memory-bound decode.

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.08993v1#S3; https://arxiv.org/html/2607.08993v1#S3.SS4。Evaluation：https://arxiv.org/html/2607.08993v1#S5; https://arxiv.org/html/2607.08993v1#S6。Limitations / counterevidence：https://arxiv.org/html/2607.08993v1#S7; https://arxiv.org/html/2607.08993v1#S8。

**Artifact boundary。** Performance and power are evaluated with the in-house StreamDQ-Sim; no independent silicon or public event-time simulator artifact is established.

**Trade-off 与共存边界。** Near-memory execution removes GPU instructions and traffic but fixes new logic, metadata and supported quantization formats into the memory interface.

- Score V2：Design Delta 3 / System Reach 3 / Durability 2 = **8/9**。
- Stable owner 候选：`INFER-GPU-MEMORY`；evidence-stage relation：`Cross-Layer Co-Design`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-08993:end -->

<!-- review:SF-2026-ARXIV-2607-09015:start -->
### Correlation-Aware Contextual Bandits withSurrogate Rewards for LLM Routing

<!-- claim:SF-2026-ARXIV-2607-09015:start -->Online LLM routing should exploit correlated model outcomes and cheap surrogate rewards without pretending those proxies are unbiased ground truth. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-09015:end -->

**为什么进入候选分母。** 把 correlated arms 与有偏 surrogate reward 纳入 LLM router 的在线学习 contract，显式管理校准错误。

**机制与状态边界。** CABS-C de-biases and pools correlated surrogate feedback with chosen-arm rewards; CABS-D keeps separate predictors and adapts their policy mixture, with regret bounds clarifying the robustness trade-off.

**证据证明什么。** Under the analyzed assumptions and benchmarks, correlation-aware surrogate use improves sample efficiency and parts of the cost-accuracy frontier.

**证据没有证明什么。** Proxy bias, arm churn and nonstationary availability can violate the model, and no production tail-SLO result is shown.

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.09015v1#S4.SS1; https://arxiv.org/html/2607.09015v1#S4.SS2。Evaluation：https://arxiv.org/html/2607.09015v1#S5。Limitations / counterevidence：https://arxiv.org/html/2607.09015v1#S7。

**Artifact boundary。** The theoretical guarantees use stated feedback assumptions and experiments use SPROUT/RouterBench; they are not production traffic evidence.

**Trade-off 与共存边界。** Surrogates reduce expensive evaluations but create calibration debt; tight coupling learns faster while decoupling is more robust to biased signals.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`INFER-SCHEDULING`；evidence-stage relation：`Alternative Branch`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-09015:end -->

<!-- review:SF-2026-ARXIV-2607-09016:start -->
### SLBench: Evaluating How LLM Agents Follow Logical Relations in Skills

<!-- claim:SF-2026-ARXIV-2607-09016:start -->Skill-guided agent safety depends on satisfying relations among clauses—preconditions, constraints, dependencies and fallbacks—not merely recalling each instruction independently. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-09016:end -->

**为什么进入候选分母。** 将 skill 文件中的 precondition、constraint 与 fallback 关系变成可执行测试，改变 Agent Skill 的验证边界。

**机制与状态边界。** SkillLogic extracts eight relation types and test hooks from skill files; SLBench turns source-grounded, high-impact relations into executable local cases; SLGuard adds a targeted inference-time scaffold.

**证据证明什么。** Across 86 audited cases, tested agents frequently violate logical relations and the targeted scaffold reduces violations in that controlled suite.

**证据没有证明什么。** The 5,000-skill discovery corpus and two agent implementations do not establish a population rate for all skills or production safety.

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.09016v1#S3。Evaluation：https://arxiv.org/html/2607.09016v1#S3.SS3; https://arxiv.org/html/2607.09016v1#S4。Limitations / counterevidence：https://arxiv.org/html/2607.09016v1#S5; https://arxiv.org/html/2607.09016v1#Sx1。

**Artifact boundary。** The v1 benchmark construction is auditable in the paper; current marketplace contents or later case revisions are outside the event-time claim.

**Trade-off 与共存边界。** Executable relation tests improve release evidence but require local fixtures, deterministic graders and maintenance as tools and skill semantics evolve.

- Score V2：Design Delta 3 / System Reach 2 / Durability 2 = **7/9**。
- Stable owner 候选：`AGENT-PLATFORM`；evidence-stage relation：`Direct Evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-09016:end -->

<!-- review:SF-2026-ARXIV-2607-09024:start -->
### Video Generation Models are General-Purpose Vision Learners

<!-- claim:SF-2026-ARXIV-2607-09024:start -->A video-generation backbone can be repurposed as a feed-forward perception representation because synthesis pretraining encodes geometry, motion and language alignment, but this does not by itself make it a causal world model. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-09024:end -->

**为什么进入候选分母。** 检验视频生成 backbone 能否转成统一视觉 perception substrate，可能改变生成模型与表征模型的架构分工。

**机制与状态边界。** GenCeption removes iterative generation at inference, fine-tunes the pretrained video diffusion features into deterministic perception heads and evaluates depth, normal and other image/video tasks.

**证据证明什么。** The repurposed backbone is competitive on the disclosed perception tasks without diffusion sampling.

**证据没有证明什么。** It does not show action-conditioned transition accuracy, persistent state, planning benefit or universal visual transfer.

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.09024v1#S2.SS3; https://arxiv.org/html/2607.09024v1#S3。Evaluation：https://arxiv.org/html/2607.09024v1#S4.SS3。Limitations / counterevidence：https://arxiv.org/html/2607.09024v1#S5。

**Artifact boundary。** The evaluated datasets and feed-forward heads support a representation-reuse claim; the paper's 'universal world model' language is not accepted as causal-environment evidence.

**Trade-off 与共存边界。** Generation pretraining amortizes broad representation learning but carries a large backbone and task-specific fine-tuning cost.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`MULTIMODAL-REPRESENTATION`；evidence-stage relation：`Principle Reuse`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-09024:end -->

<!-- review:SF-2026-ARXIV-2607-09029:start -->
### MOSAIC: Adaptive Inter-layer Composition for EfficientHeterogeneous Vision-Language Models

<!-- claim:SF-2026-ARXIV-2607-09029:start -->A VLM need not repeat one homogeneous block type at every depth; operator composition can be searched against measured hardware latency and then repaired through distillation. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-09029:end -->

**为什么进入候选分母。** 以 hardware-aware multi-objective search 选择 heterogeneous attention/MLP 组合，连接模型结构与真实执行成本。

**机制与状态边界。** Blockwise local distillation scores attention and FFN variants; a multi-objective mixed-integer program selects a per-layer structure under hardware constraints; two-stage distillation restores quality after structural replacement.

**证据证明什么。** The reported Qwen3-VL-derived design matches the teacher on the selected benchmarks while improving measured prefill/decode latency on the evaluated hardware.

**证据没有证明什么。** The discovered pattern is not hardware-independent and benchmark matching does not establish all downstream multimodal behavior.

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.09029v1#S3; https://arxiv.org/html/2607.09029v1#S3.SS2。Evaluation：https://arxiv.org/html/2607.09029v1#S4; https://arxiv.org/html/2607.09029v1#A2。Limitations / counterevidence：https://arxiv.org/html/2607.09029v1#S5。

**Artifact boundary。** No immutable search code or hardware measurement artifact is pinned in exact v1.

**Trade-off 与共存边界。** Search can expose better heterogeneous plans but adds profiling, MIP optimization and recovery training; hardware or workload changes can invalidate the chosen composition.

- Score V2：Design Delta 3 / System Reach 2 / Durability 2 = **7/9**。
- Stable owner 候选：`MULTIMODAL-REPRESENTATION`；evidence-stage relation：`Cross-Layer Co-Design`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-09029:end -->

<!-- review:SF-2026-ARXIV-2607-09042:start -->
### Learning More from Less: Reinforcement Learning from Hindsight

<!-- claim:SF-2026-ARXIV-2607-09042:start -->Sparse-reward VLA post-training can recover learning signal from all-zero GRPO groups by relabeling what a failed rollout actually achieved. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-09042:end -->

**为什么进入候选分母。** 将失败机器人 rollout 通过 hindsight relabeling 变为其他目标的成功样本，改变 VLA post-training 的样本所有权。

**机制与状态边界。** A large VLM proposes and validates hindsight instructions; successful alternative-task labels are mixed into GRPO so expensive robot trajectories supervise behaviors already present in the policy.

**证据证明什么。** The simulation and real-robot experiments show improved sample efficiency when failed trajectories contain coherent reusable behaviors and relabeling is reliable.

**证据没有证明什么。** Repetitive or uninformative failures yield little signal; relabeling errors can reward the wrong behavior, and transfer beyond the tested VLA/checkpoint is unknown.

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.09042v1#S4; https://arxiv.org/html/2607.09042v1#A2。Evaluation：https://arxiv.org/html/2607.09042v1#S5; https://arxiv.org/html/2607.09042v1#S5.SS4。Limitations / counterevidence：https://arxiv.org/html/2607.09042v1#S6。

**Artifact boundary。** The paper names RLinf and a concrete SFT checkpoint, but this review does not infer an event-time implementation commit from current documentation.

**Trade-off 与共存边界。** More bits are extracted per rollout at the cost of a powerful relabeler, additional reward validation and possible objective drift from the commanded task distribution.

- Score V2：Design Delta 3 / System Reach 2 / Durability 2 = **7/9**。
- Stable owner 候选：`TRAIN-GRPO`；evidence-stage relation：`Direct Evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-09042:end -->

<!-- review:SF-2026-ARXIV-2607-09052:start -->
### COBS: Cumulant Order Block Sparse Attention

<!-- claim:SF-2026-ARXIV-2607-09052:start -->Hardware-friendly block sparse attention depends on selection quality; first-order summaries miss within-block key covariance needed to estimate attention mass. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-09052:end -->

**为什么进入候选分母。** 用 cumulant-order block sparse pattern 改变 attention 的信息路径与可执行稀疏结构，需验证质量和 kernel 边界。

**机制与状态边界。** COBS derives a cumulant approximation, stores low-rank covariance directions in a learned query subspace and ranks blocks with a cacheable query-independent descriptor before sparse attention execution.

**证据证明什么。** The covariance summary closes more of the measured sparse-to-dense quality gap than first-order selectors under the tested configuration.

**证据没有证明什么。** Quality proxy results do not establish end-to-end throughput, arbitrary context lengths or training-time adoption.

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.09052v1#S4; https://arxiv.org/html/2607.09052v1#S5.SS4。Evaluation：https://arxiv.org/html/2607.09052v1#S7.SS2。Limitations / counterevidence：https://arxiv.org/html/2607.09052v1#S8。

**Artifact boundary。** Headline evidence is 32k RULER with stated subspace rank/quantization and an NSA-based selector; no universal kernel speedup is inferred.

**Trade-off 与共存边界。** Second-order selection improves recall but adds summary storage, calibration and ranking compute that can erase sparse-attention savings.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`MODEL-LONG-CONTEXT`；evidence-stage relation：`Direct Evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-09052:end -->

<!-- review:SF-2026-ARXIV-2607-09053:start -->
### An Emergent Mirage: Is Emergent Misalignment and Realignment Indeed a Robust Phenomenon?

<!-- claim:SF-2026-ARXIV-2607-09053:start -->Reported emergent misalignment and rapid realignment are sensitive to superficial training-data properties; response-length artifacts can masquerade as reversible alignment dynamics. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-09053:end -->

**为什么进入候选分母。** 直接复核 emergent misalignment/realignment 是否稳健，可能修正 Books 对后训练安全现象的既有结论。

**机制与状态边界。** The paper recreates narrow LoRA fine-tuning, constructs paired safe/unsafe data and controls response-length distribution while tracking behavior, adapter geometry and gradient diagnostics.

**证据证明什么。** Length normalization changes the apparent realignment result, and the tested internal diagnostics do not reveal a reproducible phase transition.

**证据没有证明什么。** The study does not refute every form of emergent misalignment or prove that no stable internal signature exists in other models, objectives or training scales.

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.09053v1#S3。Evaluation：https://arxiv.org/html/2607.09053v1#S4; https://arxiv.org/html/2607.09053v1#S5。Limitations / counterevidence：https://arxiv.org/html/2607.09053v1#S6。

**Artifact boundary。** The reviewed claim is limited to the paper's Qwen2.5-14B-Instruct model-organism and LoRA/data construction; it is not generalized to deployed frontier models.

**Trade-off 与共存边界。** More controlled datasets improve causal interpretation but narrow ecological validity; safety conclusions require multiple surface-form and distribution controls.

- Score V2：Design Delta 3 / System Reach 2 / Durability 2 = **7/9**。
- Stable owner 候选：`TRAIN-SFT`；evidence-stage relation：`Counterevidence / Correction`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-09053:end -->

<!-- review:SF-2026-ARXIV-2607-09065:start -->
### Inside the Skill Market: From Software Engineering Activities to Reusable Agent Skills

<!-- claim:SF-2026-ARXIV-2607-09065:start -->Agent skills are ecosystem artifacts with granularity, lifecycle, dependency and security properties, not merely prompt snippets copied between agents. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-09065:end -->

**为什么进入候选分母。** 把公开 Agent Skill 作为可复用软件资产研究其形成与复用边界，为 Skill lifecycle owner 提供证据。

**机制与状态边界。** The empirical study crawls public skill marketplaces, classifies software-engineering activities and lifecycle phases, analyzes reuse relations and compares marketplace malware/security signals with manual sampling.

**证据证明什么。** The sampled marketplaces show heterogeneous skill structure, reuse and substantial disagreement between security scanners.

**证据没有证明什么。** The study does not establish which skill format is safest or most effective, nor represent private enterprise ecosystems.

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.09065v1#S3.SS1。Evaluation：https://arxiv.org/html/2607.09065v1#S6.SS2。Limitations / counterevidence：https://arxiv.org/html/2607.09065v1#S7。

**Artifact boundary。** Marketplace records are a time-bounded observational sample and some annotations are LLM-assisted; scanner flags are signals, not proven maliciousness.

**Trade-off 与共存边界。** Reusable skills accelerate composition but expand provenance, dependency, update and supply-chain attack surfaces.

- Score V2：Design Delta 2 / System Reach 1 / Durability 2 = **5/9**。
- Stable owner 候选：`AGENT-PLATFORM`；evidence-stage relation：`Context / Measurement`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-09065:end -->

<!-- review:SF-2026-ARXIV-2607-09072:start -->
### Agentic Proof and Property-Based Testing via Property-Templates in Data-Intensive Computing

<!-- claim:SF-2026-ARXIV-2607-09072:start -->Generated tests become durable evidence only when a reusable property template constrains intent and the claim is checked both as a proof and against the running system. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-09072:end -->

**为什么进入候选分母。** 把 property template、proof 与 executable test 引入 data-intensive agent workflow，改变生成结果的 correctness gate。

**机制与状态边界。** The workflow defines property families once, lets an LLM fill typed holes for Lean 4 proofs and property-based Spark tests, then executes both tracks so proof validity and implementation behaviour remain distinct.

**证据证明什么。** For the templated property families, structure reduces proof hallucination and test-intent mismatch versus unstructured synthesis.

**证据没有证明什么。** Template authors can encode wrong properties, and formal proof plus tests still depends on specification and environment fidelity.

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.09072v1#S3; https://arxiv.org/html/2607.09072v1#S4。Evaluation：https://arxiv.org/html/2607.09072v1#S2.SS3; https://arxiv.org/html/2607.09072v1#S5。Limitations / counterevidence：https://arxiv.org/html/2607.09072v1#S7。

**Artifact boundary。** The evidence is a Spark/DISC instantiation; reported proof/test gains do not imply verified correctness of arbitrary data systems.

**Trade-off 与共存边界。** Templates improve repeatability but require expert property design and can narrow exploration to anticipated failure classes.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`AGENT-WORKFLOW`；evidence-stage relation：`Layering / Dependency`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-09072:end -->

<!-- review:SF-2026-ARXIV-2607-09091:start -->
### Beyond Time Shifts: Adapting Omni-LLM as a Reference-Free Evaluator for Generative Audio-Visual Models

<!-- claim:SF-2026-ARXIV-2607-09091:start -->Audio-video synchronization quality needs a reference-free continuous score over causal-semantic alignment, not only temporal-offset metrics or discrete language verdicts. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-09091:end -->

**为什么进入候选分母。** 将生成式音视频模型的 evaluator 从 reference-based metric 改为 reference-free learned judge，需审计测量目标与偏差。

**机制与状态边界。** SynthSync pairs generated audio with real videos and human preferences; an omni-modal backbone receives pairwise preference training, replaces its discrete head with a continuous projection and is post-trained with real-valued GRPO.

**证据证明什么。** The trained scorer ranks the disclosed generative failures closer to human preferences than named temporal and omni-LLM baselines.

**证据没有证明什么。** It does not establish evaluator robustness across generators, cultures, domains or adversarial optimization against the learned score.

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.09091v1#S3。Evaluation：https://arxiv.org/html/2607.09091v1#S4.SS3。Limitations / counterevidence：https://arxiv.org/html/2607.09091v1#S5。

**Artifact boundary。** Human-preference correlation on SynthSync supports the metric claim; it does not make the learned evaluator a physical-synchrony oracle.

**Trade-off 与共存边界。** A learned continuous evaluator captures richer defects but creates benchmark, judge and reward-hacking dependence.

- Score V2：Design Delta 2 / System Reach 1 / Durability 2 = **5/9**。
- Stable owner 候选：`PLATFORM-EVALUATION-SYSTEM`；evidence-stage relation：`Alternative Branch`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-09091:end -->

<!-- review:SF-2026-ARXIV-2607-09092:start -->
### AgentKGV: Agentic LLM-RAG Framework with Two-Stage Training for the Fact Verification of Knowledge Graphs

<!-- claim:SF-2026-ARXIV-2607-09092:start -->Knowledge-graph fact verification benefits from separating query-rewrite competence from iterative retrieval-policy optimization. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-09092:end -->

**为什么进入候选分母。** 把 KG fact verification 拆成 agentic retrieval、evidence reconciliation 与两阶段训练，改变 RAG evidence state flow。

**机制与状态边界。** A first training stage stabilizes natural-language queries derived from triples; a second GRPO stage optimizes when and how to search, reconcile evidence and stop before producing the fact-verification label.

**证据证明什么。** The two-stage model improves the reported verification F1 while reducing search calls relative to selected baselines.

**证据没有证明什么。** It does not establish open-web truth, calibrated confidence, robustness to poisoned evidence or transfer beyond the benchmark predicates.

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.09092v1#S3.SS2。Evaluation：https://arxiv.org/html/2607.09092v1#S4.SS2。Limitations / counterevidence：https://arxiv.org/html/2607.09092v1#S5。

**Artifact boundary。** Evidence is limited to the stated T-REx seen/unseen splits, F1 and search-call count; industrial-KG reliability is an aspiration, not a demonstrated deployment.

**Trade-off 与共存边界。** Specialized training controls retrieval cost but adds reward design, staged data and failure coupling between rewrite and search policies.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`AGENT-RAG`；evidence-stage relation：`Direct Evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-09092:end -->

<!-- review:SF-2026-ARXIV-2607-09123:start -->
### ReProAgent: Tool-Augmented Multi-Stage Agentic Generation of Bug Reproduction Tests from Issue Reports

<!-- claim:SF-2026-ARXIV-2607-09123:start -->A bug reproduction test is an intermediate executable evidence artifact, so coding agents need separate localization, path analysis, assertion planning, execution and repair stages. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-09123:end -->

**为什么进入候选分母。** 把 issue report 到可执行 reproduction test 拆成 tool-augmented multi-stage workflow，形成 coding-agent 的中间证据状态。

**机制与状态边界。** ReProAgent extracts issue evidence, narrows repository locations hierarchically, constructs and executes a reproduction test in Docker, and uses runtime feedback to refine it across several code-capable model backends.

**证据证明什么。** On the reported issues, the staged workflow generates more executable reproduction tests than the named baselines across several backbones.

**证据没有证明什么。** It does not establish other languages, flaky/concurrent defects or that a passing reproduction test isolates the actual root cause.

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.09123v1#S3.SS3; https://arxiv.org/html/2607.09123v1#S4.SS5。Evaluation：https://arxiv.org/html/2607.09123v1#S5。Limitations / counterevidence：https://arxiv.org/html/2607.09123v1#S6.SS3。

**Artifact boundary。** The evaluation uses Python SWT-bench repositories and standardized containers; framework or model versions outside v1 are not assumed equivalent.

**Trade-off 与共存边界。** Executable evidence improves debuggability but costs sandbox execution and can overfit tests to symptoms rather than causes.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`AGENT-WORKFLOW`；evidence-stage relation：`Layering / Dependency`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-09123:end -->

<!-- review:SF-2026-ARXIV-2607-09153:start -->
### KV-PRM: Efficient Process Reward Modeling via KV-Cache Transfer for Multi-Agent Test-Time Scaling

<!-- claim:SF-2026-ARXIV-2607-09153:start -->When a compatible verifier scores the trajectory just generated, the exact generator KV state can serve as the handoff instead of re-encoding decoded text; steering is a separate experimental write path. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-09153:end -->

**为什么进入候选分母。** 复用 generator exact KV state 供兼容 verifier adapter 读取，改变生成与 process-reward scoring 的状态边界。

**机制与状态边界。** KV-PRM swaps to a LoRA reward head on the compatible generator, appends one verify token, reads the existing K/V and maps next-token logits to a score; a preliminary branch differentiates through KV but is not part of the established read-only scoring claim.

**证据证明什么。** For the evaluated compatible generators and reward heads, single-token KV readout reduces scorer compute/latency while preserving or improving the measured search outcome relative to text re-encoding.

**证据没有证明什么。** The theoretical richness assumptions do not guarantee calibrated or independent verification, and the design does not transfer across incompatible models or discarded/stale caches.

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.09153v1#S3; https://arxiv.org/html/2607.09153v1#S4。Evaluation：https://arxiv.org/html/2607.09153v1#S5.SS2; https://arxiv.org/html/2607.09153v1#S6。Limitations / counterevidence：https://arxiv.org/html/2607.09153v1#S8。

**Artifact boundary。** Latency and memory evidence is bound to the reported GH200, Qwen-family configurations and search protocols; no immutable author code artifact is disclosed in exact v1.

**Trade-off 与共存边界。** State reuse removes redundant prefill but extends cache lifetime and trust scope, couples verifier deployment to model layout and risks shared blind spots.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`INFER-KV-CACHE`；evidence-stage relation：`Direct Evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-09153:end -->

<!-- review:SF-2026-ARXIV-2607-09156:start -->
### Present but Rescaled: Chat-to-Agent Transfer of Additive Activation Steering

<!-- claim:SF-2026-ARXIV-2607-09156:start -->Activation steering cannot be qualified by a single chat-to-agent gain ratio: representation survival and behavioural coupling are separate estimands that can move in opposite directions across model families and agent contexts. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-09156:end -->

**为什么进入候选分母。** 显示 activation-steering 的单一 gain ratio 不能判定 agent potency/efficacy，构成控制与评测接口的反证。

**机制与状态边界。** The study extracts one direction in chat, replays matched-norm interventions in agent trajectories, and separately measures residual-stream projection and dose-response behaviour. Per-family operating points are fixed before agent cells, preventing outcome-tuned doses.

**证据证明什么。** Across the evaluated families, the injected representation can survive while behavioural potency changes sign or magnitude, falsifying a universal scalar transfer coefficient.

**证据没有证明什么。** The study does not supply a universal coupling law, and most localization experiments remain concentrated on Qwen2.5-7B; the sycophancy attenuation point estimate is not independently significant.

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.09156v1#Sx3; https://arxiv.org/html/2607.09156v1#S5.SSx1。Evaluation：https://arxiv.org/html/2607.09156v1#S5; https://arxiv.org/html/2607.09156v1#A5。Limitations / counterevidence：https://arxiv.org/html/2607.09156v1#Sx8。

**Artifact boundary。** The article names configuration files but this review did not resolve an immutable event-time repository commit; numeric claims are therefore bound to exact v1 tables and appendices.

**Trade-off 与共存边界。** Separating read-leg survival from write-leg efficacy improves causal diagnosis but multiplies interventions, dose sweeps and deployment-specific calibration cells.

- Score V2：Design Delta 3 / System Reach 2 / Durability 2 = **7/9**。
- Stable owner 候选：`PLATFORM-EVALUATION-SYSTEM`；evidence-stage relation：`Correction / Counterevidence`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-09156:end -->

<!-- review:SF-2026-ARXIV-2607-09172:start -->
### Attention to Detail: Evaluating Energy, Performance, and Accuracy Trade-offs Across vLLM Configurations

<!-- claim:SF-2026-ARXIV-2607-09172:start -->Serving configuration is part of the evaluated system, not a quality-neutral implementation detail: the best energy, latency and accuracy point depends on the model and task. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-09172:end -->

**为什么进入候选分母。** 在同一 vLLM 运行时内联合测量 energy、performance 与 accuracy，触及 serving configuration 的多目标评测合同。

**机制与状态边界。** A controlled offline-vLLM matrix varies attention kernel, prefix caching and chunked prefill while blocking by model and workload; repeated randomized runs measure GPU/CPU energy, elapsed time, throughput and available task accuracy, then compare effect sizes and Pareto fronts.

**证据证明什么。** Within five models, five tasks and the tested vLLM options, no configuration dominates all objectives and nominally output-neutral settings can correlate with accuracy changes.

**证据没有证明什么。** Energy is estimated with sampling limitations on A100, accuracy exists for only two task families, and the controlled offline interface does not establish production online tail-SLO behaviour.

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.09172v1#S3; https://arxiv.org/html/2607.09172v1#S3.SS5。Evaluation：https://arxiv.org/html/2607.09172v1#S4; https://arxiv.org/html/2607.09172v1#S5。Limitations / counterevidence：https://arxiv.org/html/2607.09172v1#S7。

**Artifact boundary。** Exact v1 links a replication package, but no immutable commit was established in this Daily; findings are bound to the article's recorded pipeline and configurations.

**Trade-off 与共存边界。** Treating runtime configuration as an experimental factor prevents false universal defaults, but requires a larger model-by-workload profiling matrix and ongoing revalidation after software or hardware changes.

- Score V2：Design Delta 2 / System Reach 3 / Durability 2 = **7/9**。
- Stable owner 候选：`INFER-VLLM`；evidence-stage relation：`Cross-Layer Co-Design`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-09172:end -->

<!-- review:SF-2026-ARXIV-2607-09175:start -->
### Scoped Verification for Reliable Long-Horizon Agentic Context Evolution under Distribution Shift

<!-- claim:SF-2026-ARXIV-2607-09175:start -->Long-horizon context adaptation needs a typed, versioned instruction state with local validation and consolidation; repeatedly editing one flat prompt makes the changed region and rollback boundary opaque. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-09175:end -->

**为什么进入候选分母。** 把长时 agent context evolution 置于 scoped verification 与 distribution shift 下，改变 context commit/rollback 责任。

**机制与状态边界。** GRACE parses persistent system instructions into atomic typed graph nodes, applies schema-constrained edits, validates affected typed neighbourhoods, consolidates accumulated state and reconstructs the next textual checkpoint for inference.

**证据证明什么。** Under a ten-batch controlled telecom shift with fixed model, tools and harness, graph-scoped validation plus active consolidation preserves later-checkpoint improvement better than the reported flat-text controls.

**证据没有证明什么。** The evidence is domain- and harness-specific and does not establish that graph representation is always cheaper or safer than replay, retrieval or immutable prompt versioning.

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.09175v1#S4; https://arxiv.org/html/2607.09175v1#S4.SS3。Evaluation：https://arxiv.org/html/2607.09175v1#S5; https://arxiv.org/html/2607.09175v1#S5.SS2。Limitations / counterevidence：https://arxiv.org/html/2607.09175v1#S6。

**Artifact boundary。** No immutable implementation snapshot is used; the review relies on the exact-v1 graph schema, update protocol, ablation and checkpoint results.

**Trade-off 与共存边界。** Typed state improves provenance and local checks but adds parsing errors, schema evolution, graph/text divergence and consolidation policy risk.

- Score V2：Design Delta 3 / System Reach 2 / Durability 2 = **7/9**。
- Stable owner 候选：`AGENT-CONTEXT`；evidence-stage relation：`Direct Evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-09175:end -->

<!-- review:SF-2026-ARXIV-2607-09185:start -->
### Causally Debiased Latent Action Model for Embodied Action Conditioned World Models

<!-- claim:SF-2026-ARXIV-2607-09185:start -->A latent action is useful to a world model only when it identifies controllable embodiment change rather than reconstructing visually salient but action-irrelevant background variation. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-09185:end -->

**为什么进入候选分母。** 以 causally debiased latent action 学习 action-conditioned world transition，触及可控 world model 的核心状态语义。

**机制与状态边界。** CD-LAM combines foreground-weighted reconstruction, action-centric contrastive structure and a calibrated zero-transition reference, then uses a three-stage LAM, world-model and executable-action adaptation pipeline while keeping the downstream conditioning interface fixed.

**证据证明什么。** For the reported 2B and 14B backbones, debiasing the latent action improves action following, robustness and adaptation efficiency relative to the reconstruction-trained reference under matched conditioning.

**证据没有证明什么。** The experiments do not establish causal identification for arbitrary embodiments, mask quality, real-time controllers or out-of-domain physical dynamics.

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.09185v1#S4; https://arxiv.org/html/2607.09185v1#S4.SS1。Evaluation：https://arxiv.org/html/2607.09185v1#S5; https://arxiv.org/html/2607.09185v1#S5.SS1。Limitations / counterevidence：https://arxiv.org/html/2607.09185v1#S7。

**Artifact boundary。** The reported pipeline uses SAM3 masks and coarse primitive labels; because no immutable code snapshot is established here, the evidence boundary is the v1 architecture, training protocol and ablations.

**Trade-off 与共存边界。** More controllable action state costs privileged masks, primitive labels, calibration objectives and a staged training pipeline; removing background information can also discard task-relevant context if the causal partition is wrong.

- Score V2：Design Delta 3 / System Reach 2 / Durability 3 = **8/9**。
- Stable owner 候选：`MULTIMODAL-WORLD-MODELS`；evidence-stage relation：`Direct Evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-09185:end -->

<!-- review:SF-2026-ARXIV-2607-09195:start -->
### Toward Auditable AI Scientists: A Hypothesis Evolution Protocol for LLM Agents

<!-- claim:SF-2026-ARXIV-2607-09195:start -->A scientific-agent workflow becomes auditable when hypotheses, tests, evidence and belief transitions are durable typed objects rather than prose hidden in one model trajectory. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-09195:end -->

**为什么进入候选分母。** 将 hypothesis generation、evaluation 与 evolution 外化为可审计协议，改变 AI-scientist workflow 的 durable state。

**机制与状态边界。** HEP stores an append-only, hash-chained event log per hypothesis; explicit tools propose, refine, transition and attach evidence, while current lifecycle state and belief are derived by replay and lineage remains inspectable.

**证据证明什么。** In the reported tasks, explicit hypothesis lifecycle state caused the agent to exercise hypothesis-test-evidence-belief operations that a planning-only harness left largely implicit.

**证据没有证明什么。** The harness does not replace base-model capability, and three related scientific questions do not establish autonomous scientific validity, novelty or generalization to other instruments and domains.

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.09195v1#S4.SSx1。Evaluation：https://arxiv.org/html/2607.09195v1#S2.SSx2。Limitations / counterevidence：https://arxiv.org/html/2607.09195v1#S3。

**Artifact boundary。** The review does not treat any later repository state as exact-v1 provenance; workflow claims are limited to the article's event schema, tools and three materials-science task runs.

**Trade-off 与共存边界。** Externalized state supports replay and review but adds ontology design, evidence-linking, storage and policy for contradictory or stale hypotheses.

- Score V2：Design Delta 3 / System Reach 2 / Durability 2 = **7/9**。
- Stable owner 候选：`AGENT-WORKFLOW`；evidence-stage relation：`Layering / Dependency`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-09195:end -->

<!-- review:SF-2026-ARXIV-2607-09207:start -->
### Bidirectional Resource Scheduling for Disaggregated and Asynchronous RL Post-Training

<!-- claim:SF-2026-ARXIV-2607-09207:start -->Disaggregated asynchronous RL should not freeze GPUs into rollout-only and training-only pools when either stage has recoverable idle windows; the runtime must schedule both roles while preserving algorithmic staleness and dataflow contracts. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-09207:end -->

**为什么进入候选分母。** 在 disaggregated asynchronous RL 中让 rollout/training 资源双向调度，改变资源、staleness 与吞吐控制所有权。

**机制与状态边界。** BiDiRL chooses a hot-switch-compatible resource envelope with stage-time models, then uses online profiling and bidirectional borrowing so trainers can occupy rollout GPUs and rollouters can occupy training GPUs without a full job restart.

**证据证明什么。** Across the reported 8-32 GPU experiments, 2B-8B models and stated staleness bounds, role borrowing can reclaim measured bubbles without logically merging rollout and optimizer stages.

**证据没有证明什么。** The speedup is workload-dependent, requires observed idle windows, and does not establish robustness to failures, arbitrary model layouts, larger fleets or different RL algorithms.

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.09207v1#S3.SS1; https://arxiv.org/html/2607.09207v1#S4。Evaluation：https://arxiv.org/html/2607.09207v1#S7; https://arxiv.org/html/2607.09207v1#S7.SS1。Limitations / counterevidence：https://arxiv.org/html/2607.09207v1#S8。

**Artifact boundary。** No event-time code commit is used. Performance claims stay bound to the exact-v1 scheduler, A6000/H100 testbeds, model sizes, response-length and staleness settings.

**Trade-off 与共存边界。** Higher utilization adds hot-switch state, layout compatibility constraints, online profiling error, admission complexity and new interference/failure domains.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`TRAIN-DISTRIBUTED-TRAINING`；evidence-stage relation：`Direct Evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-09207:end -->

<!-- review:SF-2026-ARXIV-2607-09217:start -->
### OpenProver: Agentic and InteractiveTheorem Proving with Lean 4

<!-- claim:SF-2026-ARXIV-2607-09217:start -->For formal proof search, durable separation of planning, parallel exploration and independent machine verification is more important than one uninterrupted reasoning transcript. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-09217:end -->

**为什么进入候选分母。** 以 Planner-Worker-Verifier、Whiteboard、Repository 与 Lean verifier 组成可复现的形式化 agent system。

**机制与状态边界。** A Planner maintains a compact Whiteboard and unbounded Repository, parallel Workers develop proof fragments, parallel Verifiers check each contribution with Lean 4, and accepted results re-enter the persistent search state.

**证据证明什么。** On 185 ProofNet theorems and a 100k-token budget, the reported scaffold improves completion over linear model conversations for two underlying models.

**证据没有证明什么。** The comparison does not isolate every scaffold component, guarantee proof-search cost efficiency, or establish transfer to informal mathematics and non-Lean environments.

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.09217v1#S2。Evaluation：https://arxiv.org/html/2607.09217v1#S4。Limitations / counterevidence：https://arxiv.org/html/2607.09217v1#S5。

**Artifact boundary。** The article's Lean-verifier interface and ProofNet experiment are exact-v1 evidence; no later prompt or repository revision is treated as part of this result.

**Trade-off 与共存边界。** Parallel propose-and-verify improves search diversity and correctness but increases token consumption, verifier queues, state-merging rules and dependence on formalization quality.

- Score V2：Design Delta 3 / System Reach 2 / Durability 2 = **7/9**。
- Stable owner 候选：`AGENT-WORKFLOW`；evidence-stage relation：`Layering / Dependency`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-09217:end -->

<!-- review:SF-2026-ARXIV-2607-09218:start -->
### TACTIC: Tactile and Vision Conditioned Contact Centric Control for Whole-Arm Manipulation

<!-- claim:SF-2026-ARXIV-2607-09218:start -->Whole-arm manipulation needs a receding-horizon controller that represents contact explicitly and combines analytical kinematics with learned latent dynamics. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-09218:end -->

**为什么进入候选分母。** 将触觉/视觉部分观测接到 receding-horizon contact controller，改变 whole-arm manipulation 的物理闭环。

**机制与状态边界。** TACTIC fuses RGB, depth, proximity, force and proprioception, predicts action-conditioned latent transitions, samples contact-aware joint velocities and executes through a compliant low-level controller before replanning.

**证据证明什么。** In the stated environments, contact-centric sensing, hybrid modeling and sampling improve success/safety metrics over the selected learned controls.

**证据没有证明什么。** Arbitrary planner outputs remain dependent on compliant hardware, watchdogs and emergency stops, and broad real-world robustness is open.

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.09218v1#S4a。Evaluation：https://arxiv.org/html/2607.09218v1#S5。Limitations / counterevidence：https://arxiv.org/html/2607.09218v1#S7。

**Artifact boundary。** Simulation and reported hardware trials evaluate task success and force behaviour; no formal safety guarantee is claimed.

**Trade-off 与共存边界。** Explicit contact state improves control but adds sensing, calibration, model-predictive compute and low-level safety dependencies.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`MULTIMODAL-EMBODIED-VLA`；evidence-stage relation：`Layering / Dependency`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-09218:end -->

<!-- review:SF-2026-ARXIV-2607-09236:start -->
### Forget Narrowly, Retain Broadly: Unlearning as an Asymmetric Generalization Problem

<!-- claim:SF-2026-ARXIV-2607-09236:start -->Unlearning is not one forget score: under-forgetting and over-forgetting are asymmetric generalization failures that require an explicit semantic, syntactic and lexical retain boundary. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-09236:end -->

**为什么进入候选分母。** 把 unlearning 的 under-forgetting 与 over-forgetting定义为不对称泛化并扩展评测 probe contract。

**机制与状态边界。** SUITE constructs structured forget/retain probes across several proximity tiers and evaluates both sides; JensUn++ trains refusal behaviour against that boundary and is tested in joint and sequential unlearning settings.

**证据证明什么。** For the three reported LLMs, richer retain tiers expose ranking changes and over-forgetting hidden by the comparison protocol, and the proposed training variant improves the evaluated trade-off.

**证据没有证明什么。** Topic proximity is partly model- and human-defined, the tier count is fixed, and the study does not prove erasure of training influence or cover arbitrary knowledge boundaries.

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.09236v1#S3; https://arxiv.org/html/2607.09236v1#A2.SS4。Evaluation：https://arxiv.org/html/2607.09236v1#S4; https://arxiv.org/html/2607.09236v1#A3.SS4。Limitations / counterevidence：https://arxiv.org/html/2607.09236v1#S6。

**Artifact boundary。** The exact-v1 datasets, probe construction and model/training settings define the evidence; no unpinned later artifact is used.

**Trade-off 与共存边界。** Fine-grained evaluation reduces false confidence from one forget metric but increases dataset design, semantic-boundary disputes, compute and attack surface for benchmark-specific refusal.

- Score V2：Design Delta 3 / System Reach 2 / Durability 2 = **7/9**。
- Stable owner 候选：`PLATFORM-EVALUATION-SYSTEM`；evidence-stage relation：`Correction / Counterevidence`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-09236:end -->

<!-- review:SF-2026-ARXIV-2607-09266:start -->
### LionVote: Per-Layer Learning Rate Adaptation for Lion

<!-- claim:SF-2026-ARXIV-2607-09266:start -->A global optimizer learning rate can be locally miscalibrated across tensor types; adaptation therefore needs persistent per-tensor state and diagnostics, not an unconstrained independent schedule for every layer. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-09266:end -->

**为什么进入候选分母。** 为每个参数 tensor 维护持久 compound level 并由梯度/动量诊断投票更新，直接回答 per-layer learning-rate control。

**机制与状态边界。** LionVote keeps a discrete compound multiplier per parameter tensor. Periodic votes derived from gradient-sign stability and momentum health raise or lower the multiplier, with validation loss resolving ties; the multiplier affects both Lion's sign update and decoupled weight decay.

**证据证明什么。** The experiments show layer-type scale disparity under Lion and that a per-tensor controller can help one ViT/CIFAR-100 setting, while also hurting CIFAR-10 and failing to provide a universal improvement.

**证据没有证明什么。** Vision-scale results do not validate LLM pretraining, distributed optimizer shards or arbitrary optimizers; two tasks cannot identify when heterogeneity warrants adaptation.

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.09266v1#S3; https://arxiv.org/html/2607.09266v1#S5.SS2。Evaluation：https://arxiv.org/html/2607.09266v1#S4; https://arxiv.org/html/2607.09266v1#S4.SS3。Limitations / counterevidence：https://arxiv.org/html/2607.09266v1#S6。

**Artifact boundary。** The review relies on exact-v1 derivations, eight-seed CIFAR experiments and ablations; no later code snapshot is needed to elevate the evidence beyond those workloads.

**Trade-off 与共存边界。** Local control may correct heterogeneous gradient geometry but adds state, validation dependence and hyperparameters, and can amplify noise or couple learning-rate and weight-decay changes incorrectly.

- Score V2：Design Delta 3 / System Reach 2 / Durability 3 = **8/9**。
- Stable owner 候选：`TRAIN-PRETRAINING`；evidence-stage relation：`Alternative Branch`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-09266:end -->

<!-- review:SF-2026-ARXIV-2607-09306:start -->
### Creativity, honesty and designed forgetting emerge in small hyperbolic language models

<!-- claim:SF-2026-ARXIV-2607-09306:start -->The first-public version proposes a companion-oriented memory system in which retrieval and retention are explicit state transitions, rather than treating indefinite recall as the default objective. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-09306:end -->

**为什么进入候选分母。** exact v1 把 selective retrieval、per-trace decay、consolidation 与 designed forgetting 组织为 companion memory lifecycle；后续 v3 已实质改题，不能倒灌首发窗口。

**机制与状态边界。** The v1 article combines a hyperbolic memory substrate with per-trace saliency and decay, selective retrieval gating, consolidation and a skeleton-versus-wallpaper partition; creativity and behavioural auditing are presented as companion pillars around that memory state.

**证据证明什么。** Exact v1 documents an explicit memory lifecycle and a four-condition pilot in which selective retrieval gating is associated with the proposed partition.

**证据没有证明什么。** The paper explicitly defers longitudinal retention, real-user validation and cross-base portability; its broad geometric and companionability claims are not established as general AI-system facts by the pilot.

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.09306v1#Sx1.SSx7; https://arxiv.org/html/2607.09306v1#Sx2.SSx2。Evaluation：https://arxiv.org/html/2607.09306v1#Sx1.SSx7。Limitations / counterevidence：https://arxiv.org/html/2607.09306v1#Sx1.SSx10。

**Artifact boundary。** This family changed materially by v3: the current title and abstract concern exposure-versus-manifestation evaluator targets, whereas exact v1 is a companion-AI and designed-forgetting paper. The later claim is not backfilled into this first-public Daily.

**Trade-off 与共存边界。** Designed forgetting can limit unbounded memory growth and stale-detail retrieval, but makes saliency, decay, consent, recovery and irreversible-loss policy first-class safety decisions.

- Score V2：Design Delta 3 / System Reach 2 / Durability 2 = **7/9**。
- Stable owner 候选：`AGENT-MEMORY`；evidence-stage relation：`Alternative Branch`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-09306:end -->

<!-- review:SF-2026-ARXIV-2607-09328:start -->
### WildTrace: Benchmarking Natural Evidence Trails in Long-Context Reasoning

<!-- claim:SF-2026-ARXIV-2607-09328:start -->Long-context evaluation should vary natural evidence geometry and source scale, because token length alone does not reveal whether a system can preserve entity bindings and cross-passage relations. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-09328:end -->

**为什么进入候选分母。** 以自然分散的 evidence trail 替代人工 needle/multi-hop 构造，改变 long-context reasoning 的证据分布合同。

**机制与状态边界。** WildTrace curates naturally distributed evidence trails, labels forward, intersection, comparative, temporal and counterfactual geometry, and reports scale-tier curves plus source-cluster diagnostics.

**证据证明什么。** The evaluated systems show graded, geometry-dependent degradation rather than one universal context cliff.

**证据没有证明什么。** The benchmark does not isolate architectural causality or guarantee that its natural trails represent private enterprise corpora.

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.09328v1#S2; https://arxiv.org/html/2607.09328v1#S3.SS2。Evaluation：https://arxiv.org/html/2607.09328v1#A2。Limitations / counterevidence：https://arxiv.org/html/2607.09328v1#S4。

**Artifact boundary。** Leaderboard scores are tied to the released question/document set and multi-judge matrix; diagnostic slices are not independent leaderboards.

**Trade-off 与共存边界。** Natural evidence improves ecological validity but reduces experimental control and complicates attribution across source families.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`PLATFORM-EVALUATION-SYSTEM`；evidence-stage relation：`Context / Measurement`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-09328:end -->

<!-- review:SF-2026-ARXIV-2607-09349:start -->
### Deceptive Grounding: Entity Attribution Failure inClinical Retrieval-Augmented Generation

<!-- claim:SF-2026-ARXIV-2607-09349:start -->Citation presence and passage entailment are insufficient grounding checks when a true claim is attached to the wrong entity; retrieval systems must preserve entity identity through synthesis. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-09349:end -->

**为什么进入候选分母。** 展示真实引用仍可归因给错误实体，揭示 faithfulness/hallucination/citation 指标共同漏检的 RAG failure mode。

**机制与状态边界。** The study separates retrieval susceptibility from answer-generation attribution, constructs near-neighbour entity evidence, uses entity-attribution verification and human-adjudicated judge analysis, then tests an entity-anchor intervention before synthesis.

**证据证明什么。** Within the constructed clinical setting, responses can be factually plausible and supported by retrieved text yet systematically attribute evidence to the wrong entity, and explicit identity anchoring reduces the measured failure.

**证据没有证明什么。** Synthetic documents and model judges do not establish real-world medical prevalence, clinical safety, or that one anchor instruction closes entity identity across domains.

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.09349v1#S3; https://arxiv.org/html/2607.09349v1#A2。Evaluation：https://arxiv.org/html/2607.09349v1#S4; https://arxiv.org/html/2607.09349v1#A2。Limitations / counterevidence：https://arxiv.org/html/2607.09349v1#S6。

**Artifact boundary。** The article's synthetic clinical corpus, judge prompts and human adjudication define the evidence; no later clinical deployment or repository state is inferred.

**Trade-off 与共存边界。** Hard identity checks reduce deceptive grounding but require entity resolution, provenance-preserving retrieval and abstention rules, and may reject useful class-level evidence when identity is genuinely ambiguous.

- Score V2：Design Delta 3 / System Reach 2 / Durability 2 = **7/9**。
- Stable owner 候选：`AGENT-RAG`；evidence-stage relation：`Correction / Counterevidence`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-09349:end -->

<!-- review:SF-2026-ARXIV-2607-09366:start -->
### Diversifying to Verify: When Task-Equivalent Programs Differ in Verifiability

<!-- claim:SF-2026-ARXIV-2607-09366:start -->Programs that are test-equivalent can differ substantially in deductive verifiability, so coding-agent diversity should vary implementation structure before verifier-guided repair. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-09366:end -->

**为什么进入候选分母。** 显示 task-equivalent program 的实现结构改变自动验证可达性，影响 coding agent 的 proposal/diversification/verifier loop。

**机制与状态边界。** Diversify2Verify generates several WhyML implementation families from one accepted contract, type-checks and tests them, sends each to a prover and applies bounded repair to localized proof obligations.

**证据证明什么。** In the benchmark, task-equivalent implementation families yield different proof success and many remaining failures are localized obligations after repair.

**证据没有证明什么。** Verification failure does not imply program incorrectness, and benchmark contracts may themselves be incomplete.

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.09366v1#S3; https://arxiv.org/html/2607.09366v1#S6。Evaluation：https://arxiv.org/html/2607.09366v1#S5。Limitations / counterevidence：https://arxiv.org/html/2607.09366v1#S7.SS3。

**Artifact boundary。** Public LeetCode-derived tasks may be contaminated; the claim concerns generated WhyML structures and verifier outcomes, not unseen coding ability.

**Trade-off 与共存边界。** Structural diversity increases proof reach but multiplies generation and verification cost and complicates selection among equivalent artifacts.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`AGENT-WORKFLOW`；evidence-stage relation：`Alternative Branch`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-09366:end -->

<!-- review:SF-2026-ARXIV-2607-09385:start -->
### STEEL: Sparsity-Aware Fused Attention for Energy-Efficient Long-Sequence Inference on AMD’s XDNA™ NPU

<!-- claim:SF-2026-ARXIV-2607-09385:start -->On a spatial laptop NPU, efficient causal attention is a placement and data-movement problem: merely porting a dense GPU formulation leaves pipeline imbalance and memory traffic dominant. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-09385:end -->

**为什么进入候选分母。** 把 fused sparse attention 映射到显式 data-movement 的 laptop NPU，补足 edge execution plan 的硬件约束。

**机制与状态边界。** STEEL maps tiled FlashAttention onto XDNA AIE, memory and shim tiles as a three-stage dataflow pipeline, then places work sparsity-aware so causal masking does not leave spatial stages imbalanced.

**证据证明什么。** For the measured sequence lengths and head dimensions, an architecture-specific sparse dataflow mapping improves latency and energy over the named XDNA baseline and CPU/GPU implementations.

**证据没有证明什么。** Kernel-level measurements do not establish end-to-end model latency, quality, arbitrary sparsity patterns, decode performance or portability to other NPU generations.

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.09385v1#S2.SS3; https://arxiv.org/html/2607.09385v1#S4。Evaluation：https://arxiv.org/html/2607.09385v1#S5; https://arxiv.org/html/2607.09385v1#S5.SS4。Limitations / counterevidence：https://arxiv.org/html/2607.09385v1#S6。

**Artifact boundary。** Results are bound to exact-v1 kernels, XDNA 1/2 devices and the reported BERT/Llama-shaped attention dimensions; no claim is made for CUDA or server accelerators.

**Trade-off 与共存边界。** Specialized placement exploits spatial hardware but increases compiler/runtime coupling, shape constraints, kernel maintenance and portability risk.

- Score V2：Design Delta 3 / System Reach 3 / Durability 2 = **8/9**。
- Stable owner 候选：`INFER-TENSORRT-LLM`；evidence-stage relation：`Cross-Layer Co-Design`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-09385:end -->

<!-- review:SF-2026-ARXIV-2607-09415:start -->
### Self-Guided Test-Time Training for Long-Context LLMs

<!-- claim:SF-2026-ARXIV-2607-09415:start -->Test-time training over an entire long context can optimize on irrelevant tokens; the query should first select evidence spans, and only that temporary state should be adapted before answering from the original context. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-09415:end -->

**为什么进入候选分母。** 用问题相关 span 选择驱动 instance-specific test-time parameter update，改变长上下文推理时状态生命周期。

**机制与状态边界。** The model annotates question-relevant spans, applies temporary LoRA updates to query projections using only those spans, and generates against the unchanged full context; random-span, full-context, compression and retrieval-head variants serve as controls.

**证据证明什么。** In the reported benchmarks, span-selected adaptation improves over random-span TTT and is cheaper than adapting on all long-context tokens.

**证据没有证明什么。** Self-selected spans can omit evidence, leak answer cues or shift under open-ended workloads; the paper does not establish safe cross-request persistence or production latency.

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.09415v1#S2; https://arxiv.org/html/2607.09415v1#A1。Evaluation：https://arxiv.org/html/2607.09415v1#S3; https://arxiv.org/html/2607.09415v1#S3.SS2。Limitations / counterevidence：https://arxiv.org/html/2607.09415v1#S6。

**Artifact boundary。** Evidence is limited to exact-v1 LongBench-v2/Pro, Qwen3 and Llama-3.1 configurations and the disclosed LoRA sweep; no online serving implementation is assumed.

**Trade-off 与共存边界。** Instance-specific adaptation can concentrate compute on useful evidence but adds a mutable per-request weight state, selection error, optimizer overhead and reset/isolation requirements.

- Score V2：Design Delta 3 / System Reach 2 / Durability 2 = **7/9**。
- Stable owner 候选：`MODEL-LONG-CONTEXT`；evidence-stage relation：`Alternative Branch`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-09415:end -->

<!-- review:SF-2026-ARXIV-2607-09492:start -->
### Multimodal Reward Hacking in Reinforcement Learning

<!-- claim:SF-2026-ARXIV-2607-09492:start -->A rising proxy reward can hide actively created multimodal failures; evaluation must compare reward improvement against an independent oracle and distinguish pre-existing from newly rewarded failures. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-09492:end -->

**为什么进入候选分母。** 系统比较多模态 RL 的 proxy reward hacking，并提出 Newly Rewarded Failure Rate，可能修正 reward/evaluation contract。

**机制与状态边界。** The study varies reward designs, model scales and clean/ambiguous data, evaluates outputs with a separately prompted oracle judge, and reports reward-oracle gap, hacking rate and Newly Rewarded Failure Rate rather than proxy reward alone.

**证据证明什么。** For the evaluated safety/chart VQA regimes, RL can preferentially reinforce oracle-rejected responses; scaling and better reward design reduce but do not eliminate the measured hacking.

**证据没有证明什么。** The metrics and model judge do not establish all forms of reward hacking, human harm or transfer to text-only and physical-control policies.

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.09492v1#S2; https://arxiv.org/html/2607.09492v1#S3.SS4。Evaluation：https://arxiv.org/html/2607.09492v1#S3; https://arxiv.org/html/2607.09492v1#A4。Limitations / counterevidence：https://arxiv.org/html/2607.09492v1#S3.SS1; https://arxiv.org/html/2607.09492v1#S5。

**Artifact boundary。** The independent oracle is still Qwen3-VL-235B rather than human ground truth; claims stay tied to the disclosed judge inputs, tasks and output interface.

**Trade-off 与共存边界。** Independent oracle checks improve visibility but add evaluator cost and correlated-model bias; richer rewards reduce one exploit surface while creating new specification and judge-alignment obligations.

- Score V2：Design Delta 3 / System Reach 3 / Durability 2 = **8/9**。
- Stable owner 候选：`PLATFORM-EVALUATION-SYSTEM`；evidence-stage relation：`Correction / Counterevidence`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-09492:end -->

<!-- review:SF-2026-ARXIV-2607-09493:start -->
### Shared Selective Persistent Memory for Agentic LLM Systems

<!-- claim:SF-2026-ARXIV-2607-09493:start -->Cross-session agent memory should persist reusable specifications and schemas while discarding execution traces and bulky raw data; retaining everything can be worse than retaining nothing. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-09493:end -->

**为什么进入候选分母。** 把跨 session 可复用 context 提炼为共享选择性持久 memory，明确哪些状态保留、共享与丢弃。

**机制与状态边界。** A collaborative workspace extracts typed task specifications, data schemas, tool configuration and output constraints into shared selective memory, injects compact summaries at reuse time, and refreshes underlying data without replaying the construction trace.

**证据证明什么。** In the reported recurring workspace tasks, selective persistent state improves completion and reuse while full-history persistence degrades completion relative to no memory.

**证据没有证明什么。** The study does not establish universal memory schemas, privacy isolation, long-term consistency or that its large token-reduction figures preserve every task-relevant detail.

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.09493v1#S4; https://arxiv.org/html/2607.09493v1#S5。Evaluation：https://arxiv.org/html/2607.09493v1#S6; https://arxiv.org/html/2607.09493v1#S6.SS4。Limitations / counterevidence：https://arxiv.org/html/2607.09493v1#S7。

**Artifact boundary。** The implementation is a specific FastAPI-based workspace and the token figures are representation counts, not universal serving-cost measurements.

**Trade-off 与共存边界。** Selective memory reduces context cost and stale procedural noise but moves correctness into extraction, schema versioning, access control and deletion policy.

- Score V2：Design Delta 3 / System Reach 2 / Durability 3 = **8/9**。
- Stable owner 候选：`AGENT-MEMORY`；evidence-stage relation：`Direct Evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-09493:end -->

<!-- review:SF-2026-ARXIV-2607-09510:start -->
### Failure as a Process: An Anatomyof CLI Coding Agent Trajectories

<!-- claim:SF-2026-ARXIV-2607-09510:start -->Coding-agent failure is a trajectory with distinct decisive-error, lock-in and observable-symptom times; final pass/fail and one error label erase the intervention window. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-09510:end -->

**为什么进入候选分母。** 把 coding-agent failure 从终局标签改成 onset/evolution/recovery trajectory，改变 observability 与诊断粒度。

**机制与状态边界。** The study normalizes CLI traces and annotates three timestamps per failed run: the error that determines failure, the point after which no recovery is observed, and the first externally visible symptom; distributions are compared across scaffolds and models.

**证据证明什么。** In this corpus, decisive errors often precede lock-in and visible failure by several actions, revealing a measurable recovery interval hidden by terminal labels.

**证据没有证明什么。** Retrospective labels do not prove causal interventions would recover the run, and CLI coding tasks do not represent every agent environment.

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.09510v1#S2.SS5。Evaluation：https://arxiv.org/html/2607.09510v1#S3; https://arxiv.org/html/2607.09510v1#S3.SS1。Limitations / counterevidence：https://arxiv.org/html/2607.09510v1#S4.SS1。

**Artifact boundary。** The evidence is the annotated corpus of 1,184 failed trajectories across the stated seven models and three scaffolds; later agent versions are not assumed equivalent.

**Trade-off 与共存边界。** Process-level observability enables earlier recovery policies but requires normalized event schemas, expensive annotation and careful separation of hindsight judgment from online signals.

- Score V2：Design Delta 3 / System Reach 2 / Durability 2 = **7/9**。
- Stable owner 候选：`PLATFORM-TRACE`；evidence-stage relation：`Direct Evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-09510:end -->

<!-- review:SF-2026-ARXIV-2607-09520:start -->
### Seeing is Free, Speaking is Not: Uncovering the True Energy Bottleneck in Edge VLM Inference

<!-- claim:SF-2026-ARXIV-2607-09520:start -->For the measured edge VLMs, autoregressive output length—not visual-token ingestion—is the dominant energy driver, so optimizing image encoding alone can target the wrong bottleneck. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-09520:end -->

**为什么进入候选分母。** 跨设备 profiling 质疑“视觉 token 是 edge VLM 主能耗”的常见假设，可能改变优化优先级。

**机制与状态边界。** Power is separated from runtime, then five VLMs are profiled across resolutions on locked-frequency RTX 3070 Laptop and Jetson Orin NX systems using greedy llama.cpp inference and 100 ms power sampling; input and output token contributions are isolated.

**证据证明什么。** Within those configurations, per-model average power varies little and decode time accounts for most energy, while image complexity changes energy mainly through induced output length.

**证据没有证明什么。** The result is not a universal VLM law for server GPUs, encoder-heavy tasks, streaming video, different quantization, speculative decoding or fixed short outputs.

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.09520v1#S3; https://arxiv.org/html/2607.09520v1#S4。Evaluation：https://arxiv.org/html/2607.09520v1#S5; https://arxiv.org/html/2607.09520v1#S6。Limitations / counterevidence：https://arxiv.org/html/2607.09520v1#S7。

**Artifact boundary。** The conclusion is bound to the two edge platforms, five model families, llama.cpp, greedy decoding and tested resolutions; power sampling and quantization/runtime details must travel with numeric claims.

**Trade-off 与共存边界。** Limiting output tokens saves energy and latency but may reduce task quality; optimizing decode first can neglect workloads where vision encoding or data movement dominates.

- Score V2：Design Delta 3 / System Reach 2 / Durability 2 = **7/9**。
- Stable owner 候选：`INFER-DECODE`；evidence-stage relation：`Correction / Counterevidence`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-09520:end -->

<!-- review:SF-2026-ARXIV-2607-09532:start -->
### Statistically Undetectable Backdoors in Deep Neural Networks

<!-- claim:SF-2026-ARXIV-2607-09532:start -->White-box access to weights does not guarantee a statistically detectable backdoor: a malicious trainer can construct model distributions that are indistinguishable to bounded inspection while retaining a secret-trigger capability. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-09532:end -->

**为什么进入候选分母。** 在白盒权重可见条件下仍可统计不可区分的 backdoor，构成 artifact inspection 安全假设的强制反证。

**机制与状态边界。** The paper gives a cryptographic construction based on trainer-held secrets and invariance-style adversarial behaviour, states architectural constraints for a broad DNN class, and demonstrates a limited Fashion-MNIST embedding proof of concept.

**证据证明什么。** Under the paper's cryptographic and model-class assumptions, no bounded statistical weight audit can universally distinguish the constructed clean and backdoored distributions.

**证据没有证明什么。** It does not show practical undetectability in frontier LLM supply chains, survive arbitrary fine-tuning, or defeat provenance, reproducible builds and behavioural red-teaming together.

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.09532v1#S3; https://arxiv.org/html/2607.09532v1#S5。Evaluation：https://arxiv.org/html/2607.09532v1#S1.SS1; https://arxiv.org/html/2607.09532v1#S6.SS1。Limitations / counterevidence：https://arxiv.org/html/2607.09532v1#S6.SS1。

**Artifact boundary。** The implementation is explicitly a toy proof of concept, not an end-to-end robust LLM backdoor demonstration; the durable evidence is the stated theoretical possibility under its assumptions.

**Trade-off 与共存边界。** The impossibility result shifts security from weight inspection alone toward trusted provenance and behavioural evidence, increasing build, signing, reproducibility and continuous-evaluation cost.

- Score V2：Design Delta 3 / System Reach 2 / Durability 3 = **8/9**。
- Stable owner 候选：`PLATFORM-SECURITY`；evidence-stage relation：`Correction / Counterevidence`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-09532:end -->

<!-- review:SF-2026-ARXIV-2607-09553:start -->
### Writing Bug Reports for Software Repair Agents: What Information Matters Most?

<!-- claim:SF-2026-ARXIV-2607-09553:start -->Bug-report usefulness is determined by specific evidence fields and repository difficulty, not raw report length; issue text is the repair agent's task specification. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-09553:end -->

**为什么进入候选分母。** 把 bug report 视为 repair agent 的任务 specification，并分析哪些字段决定可复现与可修复性。

**机制与状态边界。** The study combines observational reports with controlled deletion of expected behaviour, observed behaviour, reproduction steps and code pointers, then fits repository-aware mixed-effect success models across three LLMs.

**证据证明什么。** For the evaluated issues, information types have different associations and causal-ablation effects on repair success, while repository-level variance remains large.

**证据没有证明什么。** The study does not measure information quality continuously or establish a universal bug-report template.

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.09553v1#S2.SS4。Evaluation：https://arxiv.org/html/2607.09553v1#S3.SS2。Limitations / counterevidence：https://arxiv.org/html/2607.09553v1#S6。

**Artifact boundary。** Fields are coded largely as present/absent and deletions are artificial; odds ratios remain tied to the sampled repositories and agents.

**Trade-off 与共存边界。** Structured issue evidence helps agents but increases reporter burden and can give false confidence when fields are present but wrong.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`AGENT-CONTEXT`；evidence-stage relation：`Context / Measurement`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-09553:end -->

<!-- review:SF-2026-ARXIV-2607-09560:start -->
### Beyond Fixed Representations: The Vocabulary and Verifier Gaps in Open-Ended AI

<!-- claim:SF-2026-ARXIV-2607-09560:start -->Open-ended intelligence may require expanding the representation and verifier vocabulary, not only searching harder inside a fixed problem space. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-09560:end -->

**为什么进入候选分母。** 提出 vocabulary space 与 verifier space 固定会限制开放式创新，构成可能需要结构 owner 的长期命题。

**机制与状态边界。** The position paper models progress as reducing discrepancy between current representational state and an incompletely specified goal, and identifies vocabulary and verifier gaps as barriers to concept and task invention.

**证据证明什么。** No empirical mechanism is proved; the paper provides terminology for a design pressure beyond fixed-state optimization.

**证据没有证明什么。** It does not show how to safely create new representations or validate novel verifier spaces.

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.09560v1#S3.SS1。Evaluation：Not Required — exact v1 is a conceptual position paper and makes no empirical performance claim。Limitations / counterevidence：https://arxiv.org/html/2607.09560v1#S8。

**Artifact boundary。** This is a conceptual framework without a new empirical evaluation contract; it can motivate a structural question but cannot support implementation or performance claims.

**Trade-off 与共存边界。** Expanding vocabularies may enable novelty while weakening comparability, formal guarantees and controllability.

- Score V2：Design Delta 2 / System Reach 1 / Durability 2 = **5/9**。
- Stable owner 候选：`WORLDVIEW-FUTURE`；evidence-stage relation：`Explanatory Analogy`。
- Books 候选路由（尚非最终决定）：`Structural Candidate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-09560:end -->

<!-- review:SF-2026-ARXIV-2607-09586:start -->
### TrustX Agent Risk Classification Framework (ARC): Risk-Tiering Internally Created Agentic AI Systems

<!-- claim:SF-2026-ARXIV-2607-09586:start -->Agent release gates should classify autonomy, action/tool scope and impact, then trigger controls and reassessment when those properties change. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-09586:end -->

**为什么进入候选分母。** 把 agent autonomy、tool/action scope 与风险层级映射为 release/governance rubric，触及 Agent Platform gate。

**机制与状态边界。** ARC adapts NIST, ISO and regulatory risk concepts into an agent-specific rubric, assigns tiers from scored capabilities and supplies lifecycle reassessment triggers.

**证据证明什么。** The paper demonstrates a structured mapping and case application, not reduction of real incidents.

**证据没有证明什么。** Subjective scoring, lifecycle drift and rapid capability change remain explicit limitations.

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.09586v1#S2.SS1; https://arxiv.org/html/2607.09586v1#S3。Evaluation：https://arxiv.org/html/2607.09586v1#S5。Limitations / counterevidence：https://arxiv.org/html/2607.09586v1#S6.SS3。

**Artifact boundary。** The rubric is an internally created framework, not an authoritative legal classification or validated predictor of harm.

**Trade-off 与共存边界。** Tiering makes controls reviewable but can collapse contextual risk into one score and become stale between reassessments.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`AGENT-PLATFORM`；evidence-stage relation：`Context / Measurement`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-09586:end -->

<!-- review:SF-2026-ARXIV-2607-09590:start -->
### PAC-ACT: Post-training Actor-Critic for Action Chunking Transformers

<!-- claim:SF-2026-ARXIV-2607-09590:start -->Action-chunk imitation should be treated as a behaviour prior, then adapted with environment reward through an actor-critic design that respects chunk structure rather than flattening it. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-09590:end -->

**为什么进入候选分母。** 把 VLA/ACT 的 post-training 改写为 chunk-level actor-critic，在实时控制与分布偏移之间形成新分支。

**机制与状态边界。** PAC-ACT initializes from behaviour cloning, removes the CVAE stochastic path from the actor during RL, uses an encoder-style value critic over chunk representations, and applies PPO-style updates in parallel simulated environments.

**证据证明什么。** In the evaluated tasks, RL fine-tuning improves success, safety and time metrics over the imitation prior, while the encoder critic and deterministic actor outperform the two stated architecture ablations.

**证据没有证明什么。** The experiments do not establish sim-to-real transfer, broad embodiment generalization, stable long-horizon credit assignment or safety outside the training reward.

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.09590v1#S3。Evaluation：https://arxiv.org/html/2607.09590v1#S4; https://arxiv.org/html/2607.09590v1#S4.SS9。Limitations / counterevidence：https://arxiv.org/html/2607.09590v1#S5。

**Artifact boundary。** The result is scoped to the reported manipulation environments, 16 parallel environments and disclosed PPO/architecture ablations; no real-robot deployment claim is inferred.

**Trade-off 与共存边界。** RL customizes behaviour beyond demonstrations but introduces reward misspecification, exploration risk and critic bias; removing latent stochasticity improves optimization yet can reduce useful multimodal action diversity.

- Score V2：Design Delta 3 / System Reach 2 / Durability 3 = **8/9**。
- Stable owner 候选：`MULTIMODAL-EMBODIED-VLA`；evidence-stage relation：`Direct Evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-09590:end -->

<!-- review:SF-2026-ARXIV-2607-09600:start -->
### Agora: Enhancing LLM Agent Reasoning Via Auction-Based Task Allocation

<!-- claim:SF-2026-ARXIV-2607-09600:start -->Multi-model task allocation needs calibrated competence and cost rather than self-reported confidence; an auction is useful only when bids are commensurable. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-09600:end -->

**为什么进入候选分母。** 以校准 competence 和 cost 的 auction 分配 model/tool，改变 multi-agent orchestration 的控制策略。

**机制与状态边界。** Agora decomposes tasks, solicits calibrated model/tool bids, allocates subtasks under quality-first or cost-aware policies, executes in parallel where possible and aggregates results.

**证据证明什么。** On the disclosed text, science-code and vision tasks, calibrated allocation improves several quality metrics over stated routing baselines; the no-calibration ablation degrades many tasks.

**证据没有证明什么。** It does not establish truthfulness of bids under strategic agents, production tail latency or optimal allocation under nonstationary backends.

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.09600v1#S2.SS1; https://arxiv.org/html/2607.09600v1#S3。Evaluation：https://arxiv.org/html/2607.09600v1#S4.SS4。Limitations / counterevidence：https://arxiv.org/html/2607.09600v1#S5。

**Artifact boundary。** Results use the benchmark-specific model pools and calibration procedure in exact v1; provider prices, latency and availability are not universal.

**Trade-off 与共存边界。** Auction allocation exposes cost-quality choices but adds calibration data, orchestration latency and correlated failure among bidders.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`AGENT-MULTI-AGENT`；evidence-stage relation：`Alternative Branch`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-09600:end -->

<!-- review:SF-2026-ARXIV-2607-09603:start -->
### Mosaic: Runtime-Efficient Multi-Agent Embodied Planning

<!-- claim:SF-2026-ARXIV-2607-09603:start -->Embodied multi-agent coordination requires per-agent semantic state plus an explicit conflict-resolution layer; shared prose history alone cannot reliably prevent spatial or action conflicts. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-09603:end -->

**为什么进入候选分母。** 以 agent-centric semantic memory 与 ILP 共同控制 embodied multi-agent 的状态一致性和动作冲突。

**机制与状态边界。** Mosaic maintains agent-centric semantic memory from observations and action-success history, uses an LLM planner/actor/verifier loop, and applies integer programming to select a jointly feasible parallel action set under spatial and task constraints.

**证据证明什么。** In the reported embodied tasks, semantic memory and constrained joint action selection reduce cycles, repeated failures and conflicts relative to named baselines.

**证据没有证明什么。** The system does not solve severe pose drift, stochastic actuation, open-world perception or communication failures, and its ILP scalability is not established for large teams.

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.09603v1#S3; https://arxiv.org/html/2607.09603v1#A2。Evaluation：https://arxiv.org/html/2607.09603v1#S4; https://arxiv.org/html/2607.09603v1#A5。Limitations / counterevidence：https://arxiv.org/html/2607.09603v1#A6。

**Artifact boundary。** Results are simulator-bound and assume reliable localization except for tested moderate noise; the paper does not provide evidence for raw-sensor or low-level controller robustness.

**Trade-off 与共存边界。** Explicit global feasibility improves coordination but adds shared-state consistency, optimization latency and centralization; local autonomy remains preferable when communication or global state is unreliable.

- Score V2：Design Delta 3 / System Reach 2 / Durability 3 = **8/9**。
- Stable owner 候选：`AGENT-MULTI-AGENT`；evidence-stage relation：`Layering / Dependency`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-09603:end -->

<!-- review:SF-2026-ARXIV-2607-09661:start -->
### PanoWorld: Real-World Panoramic Generation

<!-- claim:SF-2026-ARXIV-2607-09661:start -->Long-horizon panoramic world generation needs geometry-aware persistent state; a finite perspective frame and naive temporal context cannot maintain a globally coherent 360-degree environment under camera motion. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-09661:end -->

**为什么进入候选分母。** 以 panoramic equivariance、ray conditioning 与 geometry-aware memory 处理 world model 的长期空间状态。

**机制与状态边界。** PanoWorld combines panoramic equivariance, ray-conditioned camera control and an independently trained geometry-aware memory module; video and action backbones stay frozen while staged pose-conditioned reconstruction teaches the memory to carry unseen spatial content.

**证据证明什么。** Under the reported World360 data and camera trajectories, geometry-aware memory improves spatial/temporal consistency over the evaluated panoramic generation baselines.

**证据没有证明什么。** The paper notes initial-frame domain gap and long-term drift, and does not establish causal dynamics, interactive latency, collision correctness or real-world planning reliability.

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.09661v1#S4; https://arxiv.org/html/2607.09661v1#A2.SS3。Evaluation：https://arxiv.org/html/2607.09661v1#S3; https://arxiv.org/html/2607.09661v1#S5。Limitations / counterevidence：https://arxiv.org/html/2607.09661v1#A4.SS2。

**Artifact boundary。** The benchmark and generated rollouts measure panoramic synthesis, not a verified physical simulator or policy-success contract.

**Trade-off 与共存边界。** Persistent spatial memory improves continuity but accumulates stale or low-confidence frames; dynamic refresh and forgetting become necessary and can themselves destabilize the world state.

- Score V2：Design Delta 3 / System Reach 2 / Durability 2 = **7/9**。
- Stable owner 候选：`MULTIMODAL-WORLD-MODELS`；evidence-stage relation：`Direct Evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-09661:end -->

## 4. Benchmark Contracts

None。本报告保留每篇论文自己的 evaluation locator 与 claim boundary，但不转录任何可跨配置复用的数值性能主张；因此 Candidate Ledger 的 `Benchmark Claim` 均为 `no`。这不表示论文没有实验。

## 5. Deep Analysis Selection

<!-- validator:deep-analysis-selection-v1 -->
| Source Family ID | Eligibility | Decision | Analysis Unit ID | Subsumed By | Priority Rationale | Narrative Ref |
| --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2607-08774 | score_7_9 | not_selected | — | — | V2=7/9；Inference-time reliability is partly owned by an explicit control layer that separates task framing, context selection, reasoning procedure, output constraints, memory reactivation and model routing from the pretrained model.；完整证据保留在独立 Source Review，但其 owner 范围相对三条入选主轴更局部，或主要承担反证/评测边界，不与入选 family 合并成虚假的同一机制。 | analysis-decision:SF-2026-ARXIV-2607-08774 |
| SF-2026-ARXIV-2607-08780 | score_7_9 | not_selected | — | — | V2=8/9；Expert swap pressure can be reduced at training time by making routing temporally sticky, not only at serving time through caches or placement heuristics.；完整证据保留在独立 Source Review，但其 owner 范围相对三条入选主轴更局部，或主要承担反证/评测边界，不与入选 family 合并成虚假的同一机制。 | analysis-decision:SF-2026-ARXIV-2607-08780 |
| SF-2026-ARXIV-2607-08782 | score_7_9 | selected | DA-20260713-01 | — | V2=9/9；Distributed MoE placement must become a predictive online control loop when expert demand changes faster than historical placement can adapt.；该 family 分别代表在线 placement control、异步 RL 双向资源控制或跨阶段 exact state reuse，提供本日报最清晰且互不重复的三条系统演进主轴。 | analysis:DA-20260713-01 |
| SF-2026-ARXIV-2607-08786 | score_7_9 | not_selected | — | — | V2=8/9；Moderate unstructured sparsity needs a storage and kernel design distinct from both dense GEMM and very-high-sparsity SpMM.；完整证据保留在独立 Source Review，但其 owner 范围相对三条入选主轴更局部，或主要承担反证/评测边界，不与入选 family 合并成虚假的同一机制。 | analysis-decision:SF-2026-ARXIV-2607-08786 |
| SF-2026-ARXIV-2607-08877 | score_7_9 | not_selected | — | — | V2=7/9；A frozen generative robot policy can be adapted from sparse human interventions by learning in its latent noise space instead of updating the base policy weights.；完整证据保留在独立 Source Review，但其 owner 范围相对三条入选主轴更局部，或主要承担反证/评测边界，不与入选 family 合并成虚假的同一机制。 | analysis-decision:SF-2026-ARXIV-2607-08877 |
| SF-2026-ARXIV-2607-08883 | score_7_9;forced_review | not_selected | — | — | V2=7/9；Low-dimensional refusal representations are an attack surface: directly optimizing internal refusal directions can jailbreak models more efficiently than output-only objectives.；完整证据保留在独立 Source Review，但其 owner 范围相对三条入选主轴更局部，或主要承担反证/评测边界，不与入选 family 合并成虚假的同一机制。 | analysis-decision:SF-2026-ARXIV-2607-08883 |
| SF-2026-ARXIV-2607-08925 | score_7_9 | not_selected | — | — | V2=7/9；Recovery interventions change the behavior policy and must be excluded or corrected in the main policy gradient; treating mixed-policy transitions as on-policy silently biases learning.；完整证据保留在独立 Source Review，但其 owner 范围相对三条入选主轴更局部，或主要承担反证/评测边界，不与入选 family 合并成虚假的同一机制。 | analysis-decision:SF-2026-ARXIV-2607-08925 |
| SF-2026-ARXIV-2607-08930 | score_7_9 | not_selected | — | — | V2=9/9；Diffusion language models need block-denoise scheduling and mixed-state execution rather than assuming every batched sequence advances one autoregressive token at a time.；完整证据保留在独立 Source Review，但其 owner 范围相对三条入选主轴更局部，或主要承担反证/评测边界，不与入选 family 合并成虚假的同一机制。 | analysis-decision:SF-2026-ARXIV-2607-08930 |
| SF-2026-ARXIV-2607-08938 | score_7_9 | not_selected | — | — | V2=7/9；Agent capability is a property of model plus harness; task-shared reasoning can sometimes be moved into instructions, tools and orchestration so a smaller model remains viable.；完整证据保留在独立 Source Review，但其 owner 范围相对三条入选主轴更局部，或主要承担反证/评测边界，不与入选 family 合并成虚假的同一机制。 | analysis-decision:SF-2026-ARXIV-2607-08938 |
| SF-2026-ARXIV-2607-08948 | score_7_9 | not_selected | — | — | V2=7/9；An incrementally updated scene representation can be the shared state joining perception and reactive control, rather than a visualization-only output.；完整证据保留在独立 Source Review，但其 owner 范围相对三条入选主轴更局部，或主要承担反证/评测边界，不与入选 family 合并成虚假的同一机制。 | analysis-decision:SF-2026-ARXIV-2607-08948 |
| SF-2026-ARXIV-2607-08961 | score_7_9 | not_selected | — | — | V2=7/9；When a natural-language specification permits several model-admissible readings and the supervision channel hides which reading is active, more labels reduce sampling error but cannot remove identification error.；完整证据保留在独立 Source Review，但其 owner 范围相对三条入选主轴更局部，或主要承担反证/评测边界，不与入选 family 合并成虚假的同一机制。 | analysis-decision:SF-2026-ARXIV-2607-08961 |
| SF-2026-ARXIV-2607-08964 | score_7_9 | not_selected | — | — | V2=7/9；Binary task success is an insufficient evaluation interface for long-horizon terminal agents because it conflates no progress, partial progress, timeout, premature exit and harness failure.；完整证据保留在独立 Source Review，但其 owner 范围相对三条入选主轴更局部，或主要承担反证/评测边界，不与入选 family 合并成虚假的同一机制。 | analysis-decision:SF-2026-ARXIV-2607-08964 |
| SF-2026-ARXIV-2607-08973 | score_7_9 | not_selected | — | — | V2=9/9；For low-batch tensor-parallel decode, collective barriers can dominate because there is too little compute to hide communication; the result can be committed after speculative fetch only when buffer generation is validated.；完整证据保留在独立 Source Review，但其 owner 范围相对三条入选主轴更局部，或主要承担反证/评测边界，不与入选 family 合并成虚假的同一机制。 | analysis-decision:SF-2026-ARXIV-2607-08973 |
| SF-2026-ARXIV-2607-08974 | score_7_9 | not_selected | — | — | V2=7/9；A pretrained VLM can be adapted to continuous robot control more reliably when each numeric action sequence is preceded by a natural-language action description that bridges its language output distribution to action tokens.；完整证据保留在独立 Source Review，但其 owner 范围相对三条入选主轴更局部，或主要承担反证/评测边界，不与入选 family 合并成虚假的同一机制。 | analysis-decision:SF-2026-ARXIV-2607-08974 |
| SF-2026-ARXIV-2607-08991 | score_7_9 | not_selected | — | — | V2=8/9；Activation sparsity should be calibrated against layer-output sensitivity and applied conditionally by token, rather than setting every layer from activation percentiles alone.；完整证据保留在独立 Source Review，但其 owner 范围相对三条入选主轴更局部，或主要承担反证/评测边界，不与入选 family 合并成虚假的同一机制。 | analysis-decision:SF-2026-ARXIV-2607-08991 |
| SF-2026-ARXIV-2607-08993 | score_7_9 | not_selected | — | — | V2=8/9；For large-batch quantized inference, dequantization can become a memory-system operation instead of CUDA-core work and intermediate HBM traffic.；完整证据保留在独立 Source Review，但其 owner 范围相对三条入选主轴更局部，或主要承担反证/评测边界，不与入选 family 合并成虚假的同一机制。 | analysis-decision:SF-2026-ARXIV-2607-08993 |
| SF-2026-ARXIV-2607-09016 | score_7_9 | not_selected | — | — | V2=7/9；Skill-guided agent safety depends on satisfying relations among clauses—preconditions, constraints, dependencies and fallbacks—not merely recalling each instruction independently.；完整证据保留在独立 Source Review，但其 owner 范围相对三条入选主轴更局部，或主要承担反证/评测边界，不与入选 family 合并成虚假的同一机制。 | analysis-decision:SF-2026-ARXIV-2607-09016 |
| SF-2026-ARXIV-2607-09029 | score_7_9 | not_selected | — | — | V2=7/9；A VLM need not repeat one homogeneous block type at every depth; operator composition can be searched against measured hardware latency and then repaired through distillation.；完整证据保留在独立 Source Review，但其 owner 范围相对三条入选主轴更局部，或主要承担反证/评测边界，不与入选 family 合并成虚假的同一机制。 | analysis-decision:SF-2026-ARXIV-2607-09029 |
| SF-2026-ARXIV-2607-09042 | score_7_9 | not_selected | — | — | V2=7/9；Sparse-reward VLA post-training can recover learning signal from all-zero GRPO groups by relabeling what a failed rollout actually achieved.；完整证据保留在独立 Source Review，但其 owner 范围相对三条入选主轴更局部，或主要承担反证/评测边界，不与入选 family 合并成虚假的同一机制。 | analysis-decision:SF-2026-ARXIV-2607-09042 |
| SF-2026-ARXIV-2607-09053 | score_7_9;forced_review | not_selected | — | — | V2=7/9；Reported emergent misalignment and rapid realignment are sensitive to superficial training-data properties; response-length artifacts can masquerade as reversible alignment dynamics.；完整证据保留在独立 Source Review，但其 owner 范围相对三条入选主轴更局部，或主要承担反证/评测边界，不与入选 family 合并成虚假的同一机制。 | analysis-decision:SF-2026-ARXIV-2607-09053 |
| SF-2026-ARXIV-2607-09153 | score_7_9 | selected | DA-20260713-03 | — | V2=9/9；When a compatible verifier scores the trajectory just generated, the exact generator KV state can serve as the handoff instead of re-encoding decoded text; steering is a separate experimental write path.；该 family 分别代表在线 placement control、异步 RL 双向资源控制或跨阶段 exact state reuse，提供本日报最清晰且互不重复的三条系统演进主轴。 | analysis:DA-20260713-03 |
| SF-2026-ARXIV-2607-09156 | score_7_9;forced_review | not_selected | — | — | V2=7/9；Activation steering cannot be qualified by a single chat-to-agent gain ratio: representation survival and behavioural coupling are separate estimands that can move in opposite directions across model families and agent contexts.；完整证据保留在独立 Source Review，但其 owner 范围相对三条入选主轴更局部，或主要承担反证/评测边界，不与入选 family 合并成虚假的同一机制。 | analysis-decision:SF-2026-ARXIV-2607-09156 |
| SF-2026-ARXIV-2607-09172 | score_7_9 | not_selected | — | — | V2=7/9；Serving configuration is part of the evaluated system, not a quality-neutral implementation detail: the best energy, latency and accuracy point depends on the model and task.；完整证据保留在独立 Source Review，但其 owner 范围相对三条入选主轴更局部，或主要承担反证/评测边界，不与入选 family 合并成虚假的同一机制。 | analysis-decision:SF-2026-ARXIV-2607-09172 |
| SF-2026-ARXIV-2607-09175 | score_7_9 | not_selected | — | — | V2=7/9；Long-horizon context adaptation needs a typed, versioned instruction state with local validation and consolidation; repeatedly editing one flat prompt makes the changed region and rollback boundary opaque.；完整证据保留在独立 Source Review，但其 owner 范围相对三条入选主轴更局部，或主要承担反证/评测边界，不与入选 family 合并成虚假的同一机制。 | analysis-decision:SF-2026-ARXIV-2607-09175 |
| SF-2026-ARXIV-2607-09185 | score_7_9 | not_selected | — | — | V2=8/9；A latent action is useful to a world model only when it identifies controllable embodiment change rather than reconstructing visually salient but action-irrelevant background variation.；完整证据保留在独立 Source Review，但其 owner 范围相对三条入选主轴更局部，或主要承担反证/评测边界，不与入选 family 合并成虚假的同一机制。 | analysis-decision:SF-2026-ARXIV-2607-09185 |
| SF-2026-ARXIV-2607-09195 | score_7_9 | not_selected | — | — | V2=7/9；A scientific-agent workflow becomes auditable when hypotheses, tests, evidence and belief transitions are durable typed objects rather than prose hidden in one model trajectory.；完整证据保留在独立 Source Review，但其 owner 范围相对三条入选主轴更局部，或主要承担反证/评测边界，不与入选 family 合并成虚假的同一机制。 | analysis-decision:SF-2026-ARXIV-2607-09195 |
| SF-2026-ARXIV-2607-09207 | score_7_9 | selected | DA-20260713-02 | — | V2=9/9；Disaggregated asynchronous RL should not freeze GPUs into rollout-only and training-only pools when either stage has recoverable idle windows; the runtime must schedule both roles while preserving algorithmic staleness and dataflow contracts.；该 family 分别代表在线 placement control、异步 RL 双向资源控制或跨阶段 exact state reuse，提供本日报最清晰且互不重复的三条系统演进主轴。 | analysis:DA-20260713-02 |
| SF-2026-ARXIV-2607-09217 | score_7_9 | not_selected | — | — | V2=7/9；For formal proof search, durable separation of planning, parallel exploration and independent machine verification is more important than one uninterrupted reasoning transcript.；完整证据保留在独立 Source Review，但其 owner 范围相对三条入选主轴更局部，或主要承担反证/评测边界，不与入选 family 合并成虚假的同一机制。 | analysis-decision:SF-2026-ARXIV-2607-09217 |
| SF-2026-ARXIV-2607-09236 | score_7_9 | not_selected | — | — | V2=7/9；Unlearning is not one forget score: under-forgetting and over-forgetting are asymmetric generalization failures that require an explicit semantic, syntactic and lexical retain boundary.；完整证据保留在独立 Source Review，但其 owner 范围相对三条入选主轴更局部，或主要承担反证/评测边界，不与入选 family 合并成虚假的同一机制。 | analysis-decision:SF-2026-ARXIV-2607-09236 |
| SF-2026-ARXIV-2607-09266 | score_7_9 | not_selected | — | — | V2=8/9；A global optimizer learning rate can be locally miscalibrated across tensor types; adaptation therefore needs persistent per-tensor state and diagnostics, not an unconstrained independent schedule for every layer.；完整证据保留在独立 Source Review，但其 owner 范围相对三条入选主轴更局部，或主要承担反证/评测边界，不与入选 family 合并成虚假的同一机制。 | analysis-decision:SF-2026-ARXIV-2607-09266 |
| SF-2026-ARXIV-2607-09306 | score_7_9;forced_review | not_selected | — | — | V2=7/9；The first-public version proposes a companion-oriented memory system in which retrieval and retention are explicit state transitions, rather than treating indefinite recall as the default objective.；完整证据保留在独立 Source Review，但其 owner 范围相对三条入选主轴更局部，或主要承担反证/评测边界，不与入选 family 合并成虚假的同一机制。 | analysis-decision:SF-2026-ARXIV-2607-09306 |
| SF-2026-ARXIV-2607-09349 | score_7_9;forced_review | not_selected | — | — | V2=7/9；Citation presence and passage entailment are insufficient grounding checks when a true claim is attached to the wrong entity; retrieval systems must preserve entity identity through synthesis.；完整证据保留在独立 Source Review，但其 owner 范围相对三条入选主轴更局部，或主要承担反证/评测边界，不与入选 family 合并成虚假的同一机制。 | analysis-decision:SF-2026-ARXIV-2607-09349 |
| SF-2026-ARXIV-2607-09385 | score_7_9 | not_selected | — | — | V2=8/9；On a spatial laptop NPU, efficient causal attention is a placement and data-movement problem: merely porting a dense GPU formulation leaves pipeline imbalance and memory traffic dominant.；完整证据保留在独立 Source Review，但其 owner 范围相对三条入选主轴更局部，或主要承担反证/评测边界，不与入选 family 合并成虚假的同一机制。 | analysis-decision:SF-2026-ARXIV-2607-09385 |
| SF-2026-ARXIV-2607-09415 | score_7_9 | not_selected | — | — | V2=7/9；Test-time training over an entire long context can optimize on irrelevant tokens; the query should first select evidence spans, and only that temporary state should be adapted before answering from the original context.；完整证据保留在独立 Source Review，但其 owner 范围相对三条入选主轴更局部，或主要承担反证/评测边界，不与入选 family 合并成虚假的同一机制。 | analysis-decision:SF-2026-ARXIV-2607-09415 |
| SF-2026-ARXIV-2607-09492 | score_7_9;forced_review | not_selected | — | — | V2=8/9；A rising proxy reward can hide actively created multimodal failures; evaluation must compare reward improvement against an independent oracle and distinguish pre-existing from newly rewarded failures.；完整证据保留在独立 Source Review，但其 owner 范围相对三条入选主轴更局部，或主要承担反证/评测边界，不与入选 family 合并成虚假的同一机制。 | analysis-decision:SF-2026-ARXIV-2607-09492 |
| SF-2026-ARXIV-2607-09493 | score_7_9 | not_selected | — | — | V2=8/9；Cross-session agent memory should persist reusable specifications and schemas while discarding execution traces and bulky raw data; retaining everything can be worse than retaining nothing.；完整证据保留在独立 Source Review，但其 owner 范围相对三条入选主轴更局部，或主要承担反证/评测边界，不与入选 family 合并成虚假的同一机制。 | analysis-decision:SF-2026-ARXIV-2607-09493 |
| SF-2026-ARXIV-2607-09510 | score_7_9 | not_selected | — | — | V2=7/9；Coding-agent failure is a trajectory with distinct decisive-error, lock-in and observable-symptom times; final pass/fail and one error label erase the intervention window.；完整证据保留在独立 Source Review，但其 owner 范围相对三条入选主轴更局部，或主要承担反证/评测边界，不与入选 family 合并成虚假的同一机制。 | analysis-decision:SF-2026-ARXIV-2607-09510 |
| SF-2026-ARXIV-2607-09520 | score_7_9 | not_selected | — | — | V2=7/9；For the measured edge VLMs, autoregressive output length—not visual-token ingestion—is the dominant energy driver, so optimizing image encoding alone can target the wrong bottleneck.；完整证据保留在独立 Source Review，但其 owner 范围相对三条入选主轴更局部，或主要承担反证/评测边界，不与入选 family 合并成虚假的同一机制。 | analysis-decision:SF-2026-ARXIV-2607-09520 |
| SF-2026-ARXIV-2607-09532 | score_7_9;forced_review | not_selected | — | — | V2=8/9；White-box access to weights does not guarantee a statistically detectable backdoor: a malicious trainer can construct model distributions that are indistinguishable to bounded inspection while retaining a secret-trigger capability.；完整证据保留在独立 Source Review，但其 owner 范围相对三条入选主轴更局部，或主要承担反证/评测边界，不与入选 family 合并成虚假的同一机制。 | analysis-decision:SF-2026-ARXIV-2607-09532 |
| SF-2026-ARXIV-2607-09590 | score_7_9 | not_selected | — | — | V2=8/9；Action-chunk imitation should be treated as a behaviour prior, then adapted with environment reward through an actor-critic design that respects chunk structure rather than flattening it.；完整证据保留在独立 Source Review，但其 owner 范围相对三条入选主轴更局部，或主要承担反证/评测边界，不与入选 family 合并成虚假的同一机制。 | analysis-decision:SF-2026-ARXIV-2607-09590 |
| SF-2026-ARXIV-2607-09603 | score_7_9 | not_selected | — | — | V2=8/9；Embodied multi-agent coordination requires per-agent semantic state plus an explicit conflict-resolution layer; shared prose history alone cannot reliably prevent spatial or action conflicts.；完整证据保留在独立 Source Review，但其 owner 范围相对三条入选主轴更局部，或主要承担反证/评测边界，不与入选 family 合并成虚假的同一机制。 | analysis-decision:SF-2026-ARXIV-2607-09603 |
| SF-2026-ARXIV-2607-09661 | score_7_9 | not_selected | — | — | V2=7/9；Long-horizon panoramic world generation needs geometry-aware persistent state; a finite perspective frame and naive temporal context cannot maintain a globally coherent 360-degree environment under camera motion.；完整证据保留在独立 Source Review，但其 owner 范围相对三条入选主轴更局部，或主要承担反证/评测边界，不与入选 family 合并成虚假的同一机制。 | analysis-decision:SF-2026-ARXIV-2607-09661 |

### Selection Decisions

<!-- analysis-decision:SF-2026-ARXIV-2607-08774:start -->
`SF-2026-ARXIV-2607-08774` 已完成 exact-v1 Deep Review。其机制焦点是：CogniConsole decomposes control into a programmatic console, task cartridges and bounded decision-ladder nodes; hard control is kept outside fuzzy generation and state is selectively reactivated rather than replayed wholesale. 本日报不将它压入三条入选叙事，因为这会混淆 `AGENT-PLATFORM` 的独立 owner 与入选主轴；证据、反证和 trade-off 均完整保留在 `review:SF-2026-ARXIV-2607-08774`。
<!-- analysis-decision:SF-2026-ARXIV-2607-08774:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-08780:start -->
`SF-2026-ARXIV-2607-08780` 已完成 exact-v1 Deep Review。其机制焦点是：A differentiable consistency loss penalizes abrupt top-k expert changes between adjacent semantically coherent tokens; no expert architecture change is required, but the learned router now carries an inference-locality objective. 本日报不将它压入三条入选叙事，因为这会混淆 `MODEL-MOE` 的独立 owner 与入选主轴；证据、反证和 trade-off 均完整保留在 `review:SF-2026-ARXIV-2607-08780`。
<!-- analysis-decision:SF-2026-ARXIV-2607-08780:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-08786:start -->
`SF-2026-ARXIV-2607-08786` 已完成 exact-v1 Deep Review。其机制焦点是：A three-layer format combines Sparse Tensor Core-compatible regions, slot filling for surplus nonzeros and a residual path; the kernel pipelines metadata, sparse operands and residual work for memory-bound decode. 本日报不将它压入三条入选叙事，因为这会混淆 `INFER-TENSORRT-LLM` 的独立 owner 与入选主轴；证据、反证和 trade-off 均完整保留在 `review:SF-2026-ARXIV-2607-08786`。
<!-- analysis-decision:SF-2026-ARXIV-2607-08786:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-08877:start -->
`SF-2026-ARXIV-2607-08877` 已完成 exact-v1 Deep Review。其机制焦点是：Action inversion maps corrective actions to the latent noise that would generate them; a small noise policy learns those targets and steers the frozen flow/diffusion policy, including world-action models without a separate action head. 本日报不将它压入三条入选叙事，因为这会混淆 `MULTIMODAL-EMBODIED-VLA` 的独立 owner 与入选主轴；证据、反证和 trade-off 均完整保留在 `review:SF-2026-ARXIV-2607-08877`。
<!-- analysis-decision:SF-2026-ARXIV-2607-08877:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-08883:start -->
`SF-2026-ARXIV-2607-08883` 已完成 exact-v1 Deep Review。其机制焦点是：Activation-Guided GCG suppresses refusal across layers/positions; Soft-GCG relaxes discrete suffix search into continuous optimization before discretization. 本日报不将它压入三条入选叙事，因为这会混淆 `PLATFORM-SECURITY` 的独立 owner 与入选主轴；证据、反证和 trade-off 均完整保留在 `review:SF-2026-ARXIV-2607-08883`。
<!-- analysis-decision:SF-2026-ARXIV-2607-08883:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-08925:start -->
`SF-2026-ARXIV-2607-08925` 已完成 exact-v1 Deep Review。其机制焦点是：SafeExplorer masks recovery transitions from the policy gradient, relates mixed-policy training return to deployment return, substitutes an analytic recovery value under deterministic assumptions and imitates recovery only after successful segments. 本日报不将它压入三条入选叙事，因为这会混淆 `TRAIN-PPO` 的独立 owner 与入选主轴；证据、反证和 trade-off 均完整保留在 `review:SF-2026-ARXIV-2607-08925`。
<!-- analysis-decision:SF-2026-ARXIV-2607-08925:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-08930:start -->
`SF-2026-ARXIV-2607-08930` 已完成 exact-v1 Deep Review。其机制焦点是：Completed requests are evicted at block boundaries, heterogeneous denoising states are gathered into one dense layout, and token-budget admission refills capacity. 本日报不将它压入三条入选叙事，因为这会混淆 `INFER-CONTINUOUS-BATCHING` 的独立 owner 与入选主轴；证据、反证和 trade-off 均完整保留在 `review:SF-2026-ARXIV-2607-08930`。
<!-- analysis-decision:SF-2026-ARXIV-2607-08930:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-08938:start -->
`SF-2026-ARXIV-2607-08938` 已完成 exact-v1 Deep Review。其机制焦点是：A meta-agent diagnoses failure categories and searches harness adaptations instead of merely swapping the model inside a frontier-model scaffold. 本日报不将它压入三条入选叙事，因为这会混淆 `AGENT-PLATFORM` 的独立 owner 与入选主轴；证据、反证和 trade-off 均完整保留在 `review:SF-2026-ARXIV-2607-08938`。
<!-- analysis-decision:SF-2026-ARXIV-2607-08938:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-08948:start -->
`SF-2026-ARXIV-2607-08948` 已完成 exact-v1 Deep Review。其机制焦点是：RGB-D streams update a Gaussian scene with voxel filtering and relocation; the representation yields continuous distance fields consumed by motion planning and reactive collision avoidance. 本日报不将它压入三条入选叙事，因为这会混淆 `MULTIMODAL-EMBODIED-VLA` 的独立 owner 与入选主轴；证据、反证和 trade-off 均完整保留在 `review:SF-2026-ARXIV-2607-08948`。
<!-- analysis-decision:SF-2026-ARXIV-2607-08948:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-08961:start -->
`SF-2026-ARXIV-2607-08961` 已完成 exact-v1 Deep Review。其机制焦点是：NL-PAC separates task ambiguity, decoding randomness, target error and channel indistinguishability; the diameter of the pointwise-admissible target class yields a minimax risk floor under target-blind supervision. 本日报不将它压入三条入选叙事，因为这会混淆 `PLATFORM-EVALUATION-SYSTEM` 的独立 owner 与入选主轴；证据、反证和 trade-off 均完整保留在 `review:SF-2026-ARXIV-2607-08961`。
<!-- analysis-decision:SF-2026-ARXIV-2607-08961:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-08964:start -->
`SF-2026-ARXIV-2607-08964` 已完成 exact-v1 Deep Review。其机制焦点是：Forty-six executable tasks use reference solutions or simulators plus dense subtask grading; runs also record termination cause so capability and agent-environment failures can be separated. 本日报不将它压入三条入选叙事，因为这会混淆 `PLATFORM-EVALUATION-SYSTEM` 的独立 owner 与入选主轴；证据、反证和 trade-off 均完整保留在 `review:SF-2026-ARXIV-2607-08964`。
<!-- analysis-decision:SF-2026-ARXIV-2607-08964:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-08973:start -->
`SF-2026-ARXIV-2607-08973` 已完成 exact-v1 Deep Review。其机制焦点是：SiFAR uses dual buffers to remove one reuse barrier, switch-assisted redundant pull to reduce transfer work, and speculative result fetch followed by a compact validation flag and retry path. 本日报不将它压入三条入选叙事，因为这会混淆 `INFER-TENSORRT-LLM` 的独立 owner 与入选主轴；证据、反证和 trade-off 均完整保留在 `review:SF-2026-ARXIV-2607-08973`。
<!-- analysis-decision:SF-2026-ARXIV-2607-08973:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-08974:start -->
`SF-2026-ARXIV-2607-08974` 已完成 exact-v1 Deep Review。其机制焦点是：CLAP serializes a language action prefix before numeric action chunks, performs single-epoch end-to-end fine-tuning on one 8-GPU node, and compares 0.8B, 2B and 4B backbones in simulation and real-robot pick-and-place settings. 本日报不将它压入三条入选叙事，因为这会混淆 `MULTIMODAL-EMBODIED-VLA` 的独立 owner 与入选主轴；证据、反证和 trade-off 均完整保留在 `review:SF-2026-ARXIV-2607-08974`。
<!-- analysis-decision:SF-2026-ARXIV-2607-08974:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-08991:start -->
`SF-2026-ARXIV-2607-08991` 已完成 exact-v1 Deep Review。其机制焦点是：SATS chooses layer thresholds from an MLP output-sensitivity proxy; token routing chooses dense or sparse execution according to token importance, with the final MLP retained as a guardrail in the reported setup. 本日报不将它压入三条入选叙事，因为这会混淆 `INFER-TENSORRT-LLM` 的独立 owner 与入选主轴；证据、反证和 trade-off 均完整保留在 `review:SF-2026-ARXIV-2607-08991`。
<!-- analysis-decision:SF-2026-ARXIV-2607-08991:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-08993:start -->
`SF-2026-ARXIV-2607-08993` 已完成 exact-v1 Deep Review。其机制焦点是：DeQuantization Blocks in the HBM base die transform tagged quantized loads on the fly while preserving GPU load semantics; sideband metadata selects format and parameters. 本日报不将它压入三条入选叙事，因为这会混淆 `INFER-GPU-MEMORY` 的独立 owner 与入选主轴；证据、反证和 trade-off 均完整保留在 `review:SF-2026-ARXIV-2607-08993`。
<!-- analysis-decision:SF-2026-ARXIV-2607-08993:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-09016:start -->
`SF-2026-ARXIV-2607-09016` 已完成 exact-v1 Deep Review。其机制焦点是：SkillLogic extracts eight relation types and test hooks from skill files; SLBench turns source-grounded, high-impact relations into executable local cases; SLGuard adds a targeted inference-time scaffold. 本日报不将它压入三条入选叙事，因为这会混淆 `AGENT-PLATFORM` 的独立 owner 与入选主轴；证据、反证和 trade-off 均完整保留在 `review:SF-2026-ARXIV-2607-09016`。
<!-- analysis-decision:SF-2026-ARXIV-2607-09016:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-09029:start -->
`SF-2026-ARXIV-2607-09029` 已完成 exact-v1 Deep Review。其机制焦点是：Blockwise local distillation scores attention and FFN variants; a multi-objective mixed-integer program selects a per-layer structure under hardware constraints; two-stage distillation restores quality after structural replacement. 本日报不将它压入三条入选叙事，因为这会混淆 `MULTIMODAL-REPRESENTATION` 的独立 owner 与入选主轴；证据、反证和 trade-off 均完整保留在 `review:SF-2026-ARXIV-2607-09029`。
<!-- analysis-decision:SF-2026-ARXIV-2607-09029:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-09042:start -->
`SF-2026-ARXIV-2607-09042` 已完成 exact-v1 Deep Review。其机制焦点是：A large VLM proposes and validates hindsight instructions; successful alternative-task labels are mixed into GRPO so expensive robot trajectories supervise behaviors already present in the policy. 本日报不将它压入三条入选叙事，因为这会混淆 `TRAIN-GRPO` 的独立 owner 与入选主轴；证据、反证和 trade-off 均完整保留在 `review:SF-2026-ARXIV-2607-09042`。
<!-- analysis-decision:SF-2026-ARXIV-2607-09042:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-09053:start -->
`SF-2026-ARXIV-2607-09053` 已完成 exact-v1 Deep Review。其机制焦点是：The paper recreates narrow LoRA fine-tuning, constructs paired safe/unsafe data and controls response-length distribution while tracking behavior, adapter geometry and gradient diagnostics. 本日报不将它压入三条入选叙事，因为这会混淆 `TRAIN-SFT` 的独立 owner 与入选主轴；证据、反证和 trade-off 均完整保留在 `review:SF-2026-ARXIV-2607-09053`。
<!-- analysis-decision:SF-2026-ARXIV-2607-09053:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-09156:start -->
`SF-2026-ARXIV-2607-09156` 已完成 exact-v1 Deep Review。其机制焦点是：The study extracts one direction in chat, replays matched-norm interventions in agent trajectories, and separately measures residual-stream projection and dose-response behaviour. Per-family operating points are fixed before agent cells, preventing outcome-tuned doses. 本日报不将它压入三条入选叙事，因为这会混淆 `PLATFORM-EVALUATION-SYSTEM` 的独立 owner 与入选主轴；证据、反证和 trade-off 均完整保留在 `review:SF-2026-ARXIV-2607-09156`。
<!-- analysis-decision:SF-2026-ARXIV-2607-09156:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-09172:start -->
`SF-2026-ARXIV-2607-09172` 已完成 exact-v1 Deep Review。其机制焦点是：A controlled offline-vLLM matrix varies attention kernel, prefix caching and chunked prefill while blocking by model and workload; repeated randomized runs measure GPU/CPU energy, elapsed time, throughput and available task accuracy, then compare effect sizes and Pareto fronts. 本日报不将它压入三条入选叙事，因为这会混淆 `INFER-VLLM` 的独立 owner 与入选主轴；证据、反证和 trade-off 均完整保留在 `review:SF-2026-ARXIV-2607-09172`。
<!-- analysis-decision:SF-2026-ARXIV-2607-09172:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-09175:start -->
`SF-2026-ARXIV-2607-09175` 已完成 exact-v1 Deep Review。其机制焦点是：GRACE parses persistent system instructions into atomic typed graph nodes, applies schema-constrained edits, validates affected typed neighbourhoods, consolidates accumulated state and reconstructs the next textual checkpoint for inference. 本日报不将它压入三条入选叙事，因为这会混淆 `AGENT-CONTEXT` 的独立 owner 与入选主轴；证据、反证和 trade-off 均完整保留在 `review:SF-2026-ARXIV-2607-09175`。
<!-- analysis-decision:SF-2026-ARXIV-2607-09175:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-09185:start -->
`SF-2026-ARXIV-2607-09185` 已完成 exact-v1 Deep Review。其机制焦点是：CD-LAM combines foreground-weighted reconstruction, action-centric contrastive structure and a calibrated zero-transition reference, then uses a three-stage LAM, world-model and executable-action adaptation pipeline while keeping the downstream conditioning interface fixed. 本日报不将它压入三条入选叙事，因为这会混淆 `MULTIMODAL-WORLD-MODELS` 的独立 owner 与入选主轴；证据、反证和 trade-off 均完整保留在 `review:SF-2026-ARXIV-2607-09185`。
<!-- analysis-decision:SF-2026-ARXIV-2607-09185:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-09195:start -->
`SF-2026-ARXIV-2607-09195` 已完成 exact-v1 Deep Review。其机制焦点是：HEP stores an append-only, hash-chained event log per hypothesis; explicit tools propose, refine, transition and attach evidence, while current lifecycle state and belief are derived by replay and lineage remains inspectable. 本日报不将它压入三条入选叙事，因为这会混淆 `AGENT-WORKFLOW` 的独立 owner 与入选主轴；证据、反证和 trade-off 均完整保留在 `review:SF-2026-ARXIV-2607-09195`。
<!-- analysis-decision:SF-2026-ARXIV-2607-09195:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-09217:start -->
`SF-2026-ARXIV-2607-09217` 已完成 exact-v1 Deep Review。其机制焦点是：A Planner maintains a compact Whiteboard and unbounded Repository, parallel Workers develop proof fragments, parallel Verifiers check each contribution with Lean 4, and accepted results re-enter the persistent search state. 本日报不将它压入三条入选叙事，因为这会混淆 `AGENT-WORKFLOW` 的独立 owner 与入选主轴；证据、反证和 trade-off 均完整保留在 `review:SF-2026-ARXIV-2607-09217`。
<!-- analysis-decision:SF-2026-ARXIV-2607-09217:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-09236:start -->
`SF-2026-ARXIV-2607-09236` 已完成 exact-v1 Deep Review。其机制焦点是：SUITE constructs structured forget/retain probes across several proximity tiers and evaluates both sides; JensUn++ trains refusal behaviour against that boundary and is tested in joint and sequential unlearning settings. 本日报不将它压入三条入选叙事，因为这会混淆 `PLATFORM-EVALUATION-SYSTEM` 的独立 owner 与入选主轴；证据、反证和 trade-off 均完整保留在 `review:SF-2026-ARXIV-2607-09236`。
<!-- analysis-decision:SF-2026-ARXIV-2607-09236:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-09266:start -->
`SF-2026-ARXIV-2607-09266` 已完成 exact-v1 Deep Review。其机制焦点是：LionVote keeps a discrete compound multiplier per parameter tensor. Periodic votes derived from gradient-sign stability and momentum health raise or lower the multiplier, with validation loss resolving ties; the multiplier affects both Lion's sign update and decoupled weight decay. 本日报不将它压入三条入选叙事，因为这会混淆 `TRAIN-PRETRAINING` 的独立 owner 与入选主轴；证据、反证和 trade-off 均完整保留在 `review:SF-2026-ARXIV-2607-09266`。
<!-- analysis-decision:SF-2026-ARXIV-2607-09266:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-09306:start -->
`SF-2026-ARXIV-2607-09306` 已完成 exact-v1 Deep Review。其机制焦点是：The v1 article combines a hyperbolic memory substrate with per-trace saliency and decay, selective retrieval gating, consolidation and a skeleton-versus-wallpaper partition; creativity and behavioural auditing are presented as companion pillars around that memory state. 本日报不将它压入三条入选叙事，因为这会混淆 `AGENT-MEMORY` 的独立 owner 与入选主轴；证据、反证和 trade-off 均完整保留在 `review:SF-2026-ARXIV-2607-09306`。
<!-- analysis-decision:SF-2026-ARXIV-2607-09306:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-09349:start -->
`SF-2026-ARXIV-2607-09349` 已完成 exact-v1 Deep Review。其机制焦点是：The study separates retrieval susceptibility from answer-generation attribution, constructs near-neighbour entity evidence, uses entity-attribution verification and human-adjudicated judge analysis, then tests an entity-anchor intervention before synthesis. 本日报不将它压入三条入选叙事，因为这会混淆 `AGENT-RAG` 的独立 owner 与入选主轴；证据、反证和 trade-off 均完整保留在 `review:SF-2026-ARXIV-2607-09349`。
<!-- analysis-decision:SF-2026-ARXIV-2607-09349:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-09385:start -->
`SF-2026-ARXIV-2607-09385` 已完成 exact-v1 Deep Review。其机制焦点是：STEEL maps tiled FlashAttention onto XDNA AIE, memory and shim tiles as a three-stage dataflow pipeline, then places work sparsity-aware so causal masking does not leave spatial stages imbalanced. 本日报不将它压入三条入选叙事，因为这会混淆 `INFER-TENSORRT-LLM` 的独立 owner 与入选主轴；证据、反证和 trade-off 均完整保留在 `review:SF-2026-ARXIV-2607-09385`。
<!-- analysis-decision:SF-2026-ARXIV-2607-09385:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-09415:start -->
`SF-2026-ARXIV-2607-09415` 已完成 exact-v1 Deep Review。其机制焦点是：The model annotates question-relevant spans, applies temporary LoRA updates to query projections using only those spans, and generates against the unchanged full context; random-span, full-context, compression and retrieval-head variants serve as controls. 本日报不将它压入三条入选叙事，因为这会混淆 `MODEL-LONG-CONTEXT` 的独立 owner 与入选主轴；证据、反证和 trade-off 均完整保留在 `review:SF-2026-ARXIV-2607-09415`。
<!-- analysis-decision:SF-2026-ARXIV-2607-09415:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-09492:start -->
`SF-2026-ARXIV-2607-09492` 已完成 exact-v1 Deep Review。其机制焦点是：The study varies reward designs, model scales and clean/ambiguous data, evaluates outputs with a separately prompted oracle judge, and reports reward-oracle gap, hacking rate and Newly Rewarded Failure Rate rather than proxy reward alone. 本日报不将它压入三条入选叙事，因为这会混淆 `PLATFORM-EVALUATION-SYSTEM` 的独立 owner 与入选主轴；证据、反证和 trade-off 均完整保留在 `review:SF-2026-ARXIV-2607-09492`。
<!-- analysis-decision:SF-2026-ARXIV-2607-09492:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-09493:start -->
`SF-2026-ARXIV-2607-09493` 已完成 exact-v1 Deep Review。其机制焦点是：A collaborative workspace extracts typed task specifications, data schemas, tool configuration and output constraints into shared selective memory, injects compact summaries at reuse time, and refreshes underlying data without replaying the construction trace. 本日报不将它压入三条入选叙事，因为这会混淆 `AGENT-MEMORY` 的独立 owner 与入选主轴；证据、反证和 trade-off 均完整保留在 `review:SF-2026-ARXIV-2607-09493`。
<!-- analysis-decision:SF-2026-ARXIV-2607-09493:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-09510:start -->
`SF-2026-ARXIV-2607-09510` 已完成 exact-v1 Deep Review。其机制焦点是：The study normalizes CLI traces and annotates three timestamps per failed run: the error that determines failure, the point after which no recovery is observed, and the first externally visible symptom; distributions are compared across scaffolds and models. 本日报不将它压入三条入选叙事，因为这会混淆 `PLATFORM-TRACE` 的独立 owner 与入选主轴；证据、反证和 trade-off 均完整保留在 `review:SF-2026-ARXIV-2607-09510`。
<!-- analysis-decision:SF-2026-ARXIV-2607-09510:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-09520:start -->
`SF-2026-ARXIV-2607-09520` 已完成 exact-v1 Deep Review。其机制焦点是：Power is separated from runtime, then five VLMs are profiled across resolutions on locked-frequency RTX 3070 Laptop and Jetson Orin NX systems using greedy llama.cpp inference and 100 ms power sampling; input and output token contributions are isolated. 本日报不将它压入三条入选叙事，因为这会混淆 `INFER-DECODE` 的独立 owner 与入选主轴；证据、反证和 trade-off 均完整保留在 `review:SF-2026-ARXIV-2607-09520`。
<!-- analysis-decision:SF-2026-ARXIV-2607-09520:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-09532:start -->
`SF-2026-ARXIV-2607-09532` 已完成 exact-v1 Deep Review。其机制焦点是：The paper gives a cryptographic construction based on trainer-held secrets and invariance-style adversarial behaviour, states architectural constraints for a broad DNN class, and demonstrates a limited Fashion-MNIST embedding proof of concept. 本日报不将它压入三条入选叙事，因为这会混淆 `PLATFORM-SECURITY` 的独立 owner 与入选主轴；证据、反证和 trade-off 均完整保留在 `review:SF-2026-ARXIV-2607-09532`。
<!-- analysis-decision:SF-2026-ARXIV-2607-09532:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-09590:start -->
`SF-2026-ARXIV-2607-09590` 已完成 exact-v1 Deep Review。其机制焦点是：PAC-ACT initializes from behaviour cloning, removes the CVAE stochastic path from the actor during RL, uses an encoder-style value critic over chunk representations, and applies PPO-style updates in parallel simulated environments. 本日报不将它压入三条入选叙事，因为这会混淆 `MULTIMODAL-EMBODIED-VLA` 的独立 owner 与入选主轴；证据、反证和 trade-off 均完整保留在 `review:SF-2026-ARXIV-2607-09590`。
<!-- analysis-decision:SF-2026-ARXIV-2607-09590:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-09603:start -->
`SF-2026-ARXIV-2607-09603` 已完成 exact-v1 Deep Review。其机制焦点是：Mosaic maintains agent-centric semantic memory from observations and action-success history, uses an LLM planner/actor/verifier loop, and applies integer programming to select a jointly feasible parallel action set under spatial and task constraints. 本日报不将它压入三条入选叙事，因为这会混淆 `AGENT-MULTI-AGENT` 的独立 owner 与入选主轴；证据、反证和 trade-off 均完整保留在 `review:SF-2026-ARXIV-2607-09603`。
<!-- analysis-decision:SF-2026-ARXIV-2607-09603:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-09661:start -->
`SF-2026-ARXIV-2607-09661` 已完成 exact-v1 Deep Review。其机制焦点是：PanoWorld combines panoramic equivariance, ray-conditioned camera control and an independently trained geometry-aware memory module; video and action backbones stay frozen while staged pose-conditioned reconstruction teaches the memory to carry unseen spatial content. 本日报不将它压入三条入选叙事，因为这会混淆 `MULTIMODAL-WORLD-MODELS` 的独立 owner 与入选主轴；证据、反证和 trade-off 均完整保留在 `review:SF-2026-ARXIV-2607-09661`。
<!-- analysis-decision:SF-2026-ARXIV-2607-09661:end -->

### Selected Analysis Narratives

<!-- analysis:DA-20260713-01:start -->
### Director: Accelerating Distributed MoE Serving via Online Proactive Expert Placement

**旧方案为何合理、约束何时改变。** 静态 expert placement 在热点稳定、迁移代价高且预测价值有限时仍然合理；请求分布发生漂移后，placement 才从一次性部署选择变成带预测误差和迁移成本的在线控制问题。

**机制如何改写 control / data / state。** A reconfiguration manager predicts routing from queued requests; a relaxation-based optimizer computes a bounded placement; live migration overlaps expert movement with compute and limits downtime.

**可成立的证据边界。** The prototype and approximation analysis support proactive placement under the paper's predicted-routing and migration model. 但 It does not prove robustness to adversarial prediction error, heterogeneous failure domains, cross-cluster migration, or production tail-SLO behavior.

**收益、代价与下一重压力。** Proactivity reduces expected communication imbalance but adds prediction error, optimization delay, migration bandwidth, placement-version state and rollback requirements. 这意味着新机制是有条件的演进，而不是对旧方案的无条件替代。

关联完整 Source Review：`review:SF-2026-ARXIV-2607-08782`。
<!-- analysis:DA-20260713-01:end -->

<!-- analysis:DA-20260713-02:start -->
### Bidirectional Resource Scheduling for Disaggregated and Asynchronous RL Post-Training

**旧方案为何合理、约束何时改变。** 固定 rollout / training 资源池在同步训练与稳定生成成本下简单可靠；异步 RL 中两侧处理率和 policy staleness 持续变化，固定切分会让一侧空闲而另一侧堆积。

**机制如何改写 control / data / state。** BiDiRL chooses a hot-switch-compatible resource envelope with stage-time models, then uses online profiling and bidirectional borrowing so trainers can occupy rollout GPUs and rollouters can occupy training GPUs without a full job restart.

**可成立的证据边界。** Across the reported 8-32 GPU experiments, 2B-8B models and stated staleness bounds, role borrowing can reclaim measured bubbles without logically merging rollout and optimizer stages. 但 The speedup is workload-dependent, requires observed idle windows, and does not establish robustness to failures, arbitrary model layouts, larger fleets or different RL algorithms.

**收益、代价与下一重压力。** Higher utilization adds hot-switch state, layout compatibility constraints, online profiling error, admission complexity and new interference/failure domains. 这意味着新机制是有条件的演进，而不是对旧方案的无条件替代。

关联完整 Source Review：`review:SF-2026-ARXIV-2607-09207`。
<!-- analysis:DA-20260713-02:end -->

<!-- analysis:DA-20260713-03:start -->
### KV-PRM: Efficient Process Reward Modeling via KV-Cache Transfer for Multi-Agent Test-Time Scaling

**旧方案为何合理、约束何时改变。** 独立 text verifier 具有跨模型、跨进程和跨信任域的可移植性；当同一生成器刚完成长轨迹且 compatible verifier 反复评分时，丢弃 exact KV 再重做 prefill 才成为主要冗余。

**机制如何改写 control / data / state。** KV-PRM swaps to a LoRA reward head on the compatible generator, appends one verify token, reads the existing K/V and maps next-token logits to a score; a preliminary branch differentiates through KV but is not part of the established read-only scoring claim.

**可成立的证据边界。** For the evaluated compatible generators and reward heads, single-token KV readout reduces scorer compute/latency while preserving or improving the measured search outcome relative to text re-encoding. 但 The theoretical richness assumptions do not guarantee calibrated or independent verification, and the design does not transfer across incompatible models or discarded/stale caches.

**收益、代价与下一重压力。** State reuse removes redundant prefill but extends cache lifetime and trust scope, couples verifier deployment to model layout and risks shared blind spots. 这意味着新机制是有条件的演进，而不是对旧方案的无条件替代。

关联完整 Source Review：`review:SF-2026-ARXIV-2607-09153`。
<!-- analysis:DA-20260713-03:end -->

## 6. Books Comparison

<!-- validator:books-comparison-v1 -->
| Source Family ID | Stable Node ID | Target Chapter Ref | Adjacent Chapter Refs | Existing Proposition | New Evidence Delta | Evolution Relation | Decision | Books Review Ref |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |

None。Evidence-stage owner 与 proposed route 已写入 date-local frozen queue，但本泳道没有 Books 写权限，也没有把候选建议伪装成完成的章节比较。root 必须按日期顺序读取目标及相邻章节后，逐 family 写回最终 disposition。

## 7. Semantic Audit

<!-- validator:semantic-audit-v1 -->
| Audit ID | Auditor | Scope | Reviewed Refs | Findings | Resolution | Status |
| --- | --- | --- | --- | --- | --- | --- |
| SA-20260713-COVERAGE-INDEPENDENT | fresh-context:pending-root-auditor | coverage | coverage:SRC-ARXIV:20260713 | GAP-20260713-COVERAGE-INDEPENDENT：主要作者已完成 337 项全量语义判断，但 false-positive 与 false-negative 尚未由未参与写作的 reviewer 逐项签收 | Pending — 独立 reviewer 对 canonical raw inventory 与 semantic decisions 做全量反向审计，并记录具体 finding / resolution | open |
| SA-20260713-EVIDENCE-INDEPENDENT | fresh-context:pending-root-auditor | evidence | validator:review-completion-v1 | GAP-20260713-EVIDENCE-INDEPENDENT：62 个 RP 绑定 exact v1，但 claim scope、locator 与 artifact boundary 尚需独立反证审阅 | Pending — 独立 reviewer 校验 62 个 review body 与 exact-v1 locator 一致性；发现问题则重开具体 family | open |
| SA-20260713-SELECTION-INDEPENDENT | fresh-context:pending-root-auditor | deep_analysis_selection | validator:deep-analysis-selection-v1 | GAP-20260713-SELECTION-INDEPENDENT：42 个 eligible family 的三项长叙事选择尚未由独立 reviewer 比较系统影响、反证优先级与跨 owner 独立性 | Pending — 独立 reviewer 对 selection pool 与 3 个 selected unit 做 adversarial comparison | open |
| SA-20260713-BOOKS-ROOT | fresh-context:pending-root-books-owner | books | validator:books-comparison-v1 | GAP-20260713-BOOKS-ROOT：62 项尚未逐一对读目标及相邻 Books 章节，最终 disposition 未成立 | Pending — root sequential owner 消费 date-local queue，完成 Books Comparison / writeback 或明确 No Change / Structural route | open |

## 8. Ignored Noise

共有 275 个 identity 在 title + 完整 abstract 阶段得到 family-specific closure；它们仍保留在 `fresh-context-semantic-decisions-v2.1.json.gz`，没有被静默丢弃，也没有接受不适用的 Score V2。

- `domain_control_method_without_ai_system_owner`：9
- `domain_or_metric_benchmark_without_general_system_delta`：180
- `local_model_or_algorithm_improvement`：32
- `no_durable_ai_system_delta`：25
- `outside_registered_ai_system_scope`：13
- `survey_or_position_without_new_system_evidence`：5
- `vertical_application_without_transferable_system_delta`：11

## 9. Recommended Action

1. 先由独立 reviewer 审阅 Coverage、Evidence 与 Deep Analysis Selection；任何 finding 必须回到具体 family 修复，不能只改 Gate 文本。
2. root 再消费冻结队列，逐项比较 Books。当前只作为建议起点的计数为：Integrate 42、No Change 19、Structural Candidate 1；这些不是最终 Books Decision。
3. `2607.09306` 的 v3 作为 2026-07-30 的重要 revision 另行路由，首发日报只能引用 exact v1。

## 10. Repository Changes

- 重建 `papers/2026/07/13/README.md`，用 337→62 的 frozen denominator 替换旧 4 项临时报告。
- 新增 `papers/2026/07/_sources/daily-20260713/BOOKS_WRITEBACK_QUEUE_V2.1.json`，并更新 7 月月级冻结队列中的 7 月 13 日条目。
- 没有修改 Books、ROADMAP、docs、Learning State、Weekly 或共享 validator。

## 11. Open Questions

- 独立 false-negative audit 是否发现 275 项 closure 中仍存在满足 denominator admission 的 family？
- 42 个 proposed Integrate 是否在 Books 已由其他 Source Family 承载，因而应改为 `No Change — Existing Coverage`？
- `2607.09306` v1→v3 的实质改题是否形成需要重开 2026-07-30 Daily 的 important revision？

## 12. Sources

- [CogniConsole: Externalizing Inference-Time Control as a Formal Abstraction for Reliable LLM Interactions](https://arxiv.org/html/2607.08774v1) — first-public（Asia/Shanghai）：2026-07-13；exact evidence：v1；accessed：2026-09-03
- [Sticky Routing: Training MoE Models for Memory-Efficient Inference](https://arxiv.org/html/2607.08780v1) — first-public（Asia/Shanghai）：2026-07-13；exact evidence：v1；accessed：2026-09-03
- [Director: Accelerating Distributed MoE Serving via Online Proactive Expert Placement](https://arxiv.org/html/2607.08782v1) — first-public（Asia/Shanghai）：2026-07-13；exact evidence：v1；accessed：2026-09-03
- [Accelerating GPU Inference of Large Language Models with Moderately Unstructured Sparse Weight Matrices](https://arxiv.org/html/2607.08786v1) — first-public（Asia/Shanghai）：2026-07-13；exact evidence：v1；accessed：2026-09-03
- [Mixture of Probes: Learning from Privileged Modalities in Multimodal LLMs Through Probing](https://arxiv.org/html/2607.08839v1) — first-public（Asia/Shanghai）：2026-07-13；exact evidence：v1；accessed：2026-09-03
- [AgenticFocus: Object-Preserving Mixed Reality Synthesis from Human FPV Video for Dexterous Humanoid Learning](https://arxiv.org/html/2607.08857v1) — first-public（Asia/Shanghai）：2026-07-13；exact evidence：v1；accessed：2026-09-03
- [FlowDAgger: Human-in-the-Loop Adaptation of Generative Robot Policies in Latent Space](https://arxiv.org/html/2607.08877v1) — first-public（Asia/Shanghai）：2026-07-13；exact evidence：v1；accessed：2026-09-03
- [Optimizing Against Safety Representations: Activation-Guided Adversarial Suffixes and the Geometry of Refusal](https://arxiv.org/html/2607.08883v1) — first-public（Asia/Shanghai）：2026-07-13；exact evidence：v1；accessed：2026-09-03
- [GATS: Graph-Augmented Tree Search with Layered World Models for Efficient Agent Planning](https://arxiv.org/html/2607.08894v1) — first-public（Asia/Shanghai）：2026-07-13；exact evidence：v1；accessed：2026-09-03
- [SafeExplorer: An Unbiased Policy Gradient for Reinforcement Learning with Recovery Interventions](https://arxiv.org/html/2607.08925v1) — first-public（Asia/Shanghai）：2026-07-13；exact evidence：v1；accessed：2026-09-03
- [BlockServe: Block-Grained Continuous Batching for High-Throughput Diffusion LLM Serving](https://arxiv.org/html/2607.08930v1) — first-public（Asia/Shanghai）：2026-07-13；exact evidence：v1；accessed：2026-09-03
- [Better Harnesses, Smaller Models: Building 90% Cheaper Agents via Automated Harness Adaptation](https://arxiv.org/html/2607.08938v1) — first-public（Asia/Shanghai）：2026-07-13；exact evidence：v1；accessed：2026-09-03
- [TSRouter: Dynamic Modality-Model Selection for Time Series Reasoning](https://arxiv.org/html/2607.08940v1) — first-public（Asia/Shanghai）：2026-07-13；exact evidence：v1；accessed：2026-09-03
- [SplatCtrl: Perception-Action Coupling via Gaussian Scene Representations and Reactive Robot Control](https://arxiv.org/html/2607.08948v1) — first-public（Asia/Shanghai）：2026-07-13；exact evidence：v1；accessed：2026-09-03
- [SeedSmith: LLM-Driven Seed Synthesis for Directed Fuzzing](https://arxiv.org/html/2607.08949v1) — first-public（Asia/Shanghai）：2026-07-13；exact evidence：v1；accessed：2026-09-03
- [NL-PAC: Specification Ambiguity and Certified Minimax Risk Floors in LLM-Mediated Supervision](https://arxiv.org/html/2607.08961v1) — first-public（Asia/Shanghai）：2026-07-13；exact evidence：v1；accessed：2026-09-03
- [Long-Horizon-Terminal-Bench: Testing the Limits of Agents on Long-Horizon Terminal Tasks with Dense Reward-Based Grading](https://arxiv.org/html/2607.08964v1) — first-public（Asia/Shanghai）：2026-07-13；exact evidence：v1；accessed：2026-09-03
- [SiFAR: Synchronization-Free All-Reduce for Low-Latency LLM Inference](https://arxiv.org/html/2607.08973v1) — first-public（Asia/Shanghai）：2026-07-13；exact evidence：v1；accessed：2026-09-03
- [CLAP: Direct VLM-to-VLA Adaptation via Language-Action Grounding](https://arxiv.org/html/2607.08974v1) — first-public（Asia/Shanghai）：2026-07-13；exact evidence：v1；accessed：2026-09-03
- [Sensitivity-Aware Thresholding and Token Routingfor Activation Sparsification in Large Language Models](https://arxiv.org/html/2607.08991v1) — first-public（Asia/Shanghai）：2026-07-13；exact evidence：v1；accessed：2026-09-03
- [StreamDQ: Near-Memory Weight DeQuantization in Custom HBM for Scalable AI Inference Acceleration](https://arxiv.org/html/2607.08993v1) — first-public（Asia/Shanghai）：2026-07-13；exact evidence：v1；accessed：2026-09-03
- [Correlation-Aware Contextual Bandits withSurrogate Rewards for LLM Routing](https://arxiv.org/html/2607.09015v1) — first-public（Asia/Shanghai）：2026-07-13；exact evidence：v1；accessed：2026-09-03
- [SLBench: Evaluating How LLM Agents Follow Logical Relations in Skills](https://arxiv.org/html/2607.09016v1) — first-public（Asia/Shanghai）：2026-07-13；exact evidence：v1；accessed：2026-09-03
- [Video Generation Models are General-Purpose Vision Learners](https://arxiv.org/html/2607.09024v1) — first-public（Asia/Shanghai）：2026-07-13；exact evidence：v1；accessed：2026-09-03
- [MOSAIC: Adaptive Inter-layer Composition for EfficientHeterogeneous Vision-Language Models](https://arxiv.org/html/2607.09029v1) — first-public（Asia/Shanghai）：2026-07-13；exact evidence：v1；accessed：2026-09-03
- [Learning More from Less: Reinforcement Learning from Hindsight](https://arxiv.org/html/2607.09042v1) — first-public（Asia/Shanghai）：2026-07-13；exact evidence：v1；accessed：2026-09-03
- [COBS: Cumulant Order Block Sparse Attention](https://arxiv.org/html/2607.09052v1) — first-public（Asia/Shanghai）：2026-07-13；exact evidence：v1；accessed：2026-09-03
- [An Emergent Mirage: Is Emergent Misalignment and Realignment Indeed a Robust Phenomenon?](https://arxiv.org/html/2607.09053v1) — first-public（Asia/Shanghai）：2026-07-13；exact evidence：v1；accessed：2026-09-03
- [Inside the Skill Market: From Software Engineering Activities to Reusable Agent Skills](https://arxiv.org/html/2607.09065v1) — first-public（Asia/Shanghai）：2026-07-13；exact evidence：v1；accessed：2026-09-03
- [Agentic Proof and Property-Based Testing via Property-Templates in Data-Intensive Computing](https://arxiv.org/html/2607.09072v1) — first-public（Asia/Shanghai）：2026-07-13；exact evidence：v1；accessed：2026-09-03
- [Beyond Time Shifts: Adapting Omni-LLM as a Reference-Free Evaluator for Generative Audio-Visual Models](https://arxiv.org/html/2607.09091v1) — first-public（Asia/Shanghai）：2026-07-13；exact evidence：v1；accessed：2026-09-03
- [AgentKGV: Agentic LLM-RAG Framework with Two-Stage Training for the Fact Verification of Knowledge Graphs](https://arxiv.org/html/2607.09092v1) — first-public（Asia/Shanghai）：2026-07-13；exact evidence：v1；accessed：2026-09-03
- [ReProAgent: Tool-Augmented Multi-Stage Agentic Generation of Bug Reproduction Tests from Issue Reports](https://arxiv.org/html/2607.09123v1) — first-public（Asia/Shanghai）：2026-07-13；exact evidence：v1；accessed：2026-09-03
- [KV-PRM: Efficient Process Reward Modeling via KV-Cache Transfer for Multi-Agent Test-Time Scaling](https://arxiv.org/html/2607.09153v1) — first-public（Asia/Shanghai）：2026-07-13；exact evidence：v1；accessed：2026-09-03
- [Present but Rescaled: Chat-to-Agent Transfer of Additive Activation Steering](https://arxiv.org/html/2607.09156v1) — first-public（Asia/Shanghai）：2026-07-13；exact evidence：v1；accessed：2026-09-03
- [Attention to Detail: Evaluating Energy, Performance, and Accuracy Trade-offs Across vLLM Configurations](https://arxiv.org/html/2607.09172v1) — first-public（Asia/Shanghai）：2026-07-13；exact evidence：v1；accessed：2026-09-03
- [Scoped Verification for Reliable Long-Horizon Agentic Context Evolution under Distribution Shift](https://arxiv.org/html/2607.09175v1) — first-public（Asia/Shanghai）：2026-07-13；exact evidence：v1；accessed：2026-09-03
- [Causally Debiased Latent Action Model for Embodied Action Conditioned World Models](https://arxiv.org/html/2607.09185v1) — first-public（Asia/Shanghai）：2026-07-13；exact evidence：v1；accessed：2026-09-03
- [Toward Auditable AI Scientists: A Hypothesis Evolution Protocol for LLM Agents](https://arxiv.org/html/2607.09195v1) — first-public（Asia/Shanghai）：2026-07-13；exact evidence：v1；accessed：2026-09-03
- [Bidirectional Resource Scheduling for Disaggregated and Asynchronous RL Post-Training](https://arxiv.org/html/2607.09207v1) — first-public（Asia/Shanghai）：2026-07-13；exact evidence：v1；accessed：2026-09-03
- [OpenProver: Agentic and InteractiveTheorem Proving with Lean 4](https://arxiv.org/html/2607.09217v1) — first-public（Asia/Shanghai）：2026-07-13；exact evidence：v1；accessed：2026-09-03
- [TACTIC: Tactile and Vision Conditioned Contact Centric Control for Whole-Arm Manipulation](https://arxiv.org/html/2607.09218v1) — first-public（Asia/Shanghai）：2026-07-13；exact evidence：v1；accessed：2026-09-03
- [Forget Narrowly, Retain Broadly: Unlearning as an Asymmetric Generalization Problem](https://arxiv.org/html/2607.09236v1) — first-public（Asia/Shanghai）：2026-07-13；exact evidence：v1；accessed：2026-09-03
- [LionVote: Per-Layer Learning Rate Adaptation for Lion](https://arxiv.org/html/2607.09266v1) — first-public（Asia/Shanghai）：2026-07-13；exact evidence：v1；accessed：2026-09-03
- [Creativity, honesty and designed forgetting emerge in small hyperbolic language models](https://arxiv.org/html/2607.09306v1) — first-public（Asia/Shanghai）：2026-07-13；exact evidence：v1；accessed：2026-09-03
- [WildTrace: Benchmarking Natural Evidence Trails in Long-Context Reasoning](https://arxiv.org/html/2607.09328v1) — first-public（Asia/Shanghai）：2026-07-13；exact evidence：v1；accessed：2026-09-03
- [Deceptive Grounding: Entity Attribution Failure inClinical Retrieval-Augmented Generation](https://arxiv.org/html/2607.09349v1) — first-public（Asia/Shanghai）：2026-07-13；exact evidence：v1；accessed：2026-09-03
- [Diversifying to Verify: When Task-Equivalent Programs Differ in Verifiability](https://arxiv.org/html/2607.09366v1) — first-public（Asia/Shanghai）：2026-07-13；exact evidence：v1；accessed：2026-09-03
- [STEEL: Sparsity-Aware Fused Attention for Energy-Efficient Long-Sequence Inference on AMD’s XDNA™ NPU](https://arxiv.org/html/2607.09385v1) — first-public（Asia/Shanghai）：2026-07-13；exact evidence：v1；accessed：2026-09-03
- [Self-Guided Test-Time Training for Long-Context LLMs](https://arxiv.org/html/2607.09415v1) — first-public（Asia/Shanghai）：2026-07-13；exact evidence：v1；accessed：2026-09-03
- [Multimodal Reward Hacking in Reinforcement Learning](https://arxiv.org/html/2607.09492v1) — first-public（Asia/Shanghai）：2026-07-13；exact evidence：v1；accessed：2026-09-03
- [Shared Selective Persistent Memory for Agentic LLM Systems](https://arxiv.org/html/2607.09493v1) — first-public（Asia/Shanghai）：2026-07-13；exact evidence：v1；accessed：2026-09-03
- [Failure as a Process: An Anatomyof CLI Coding Agent Trajectories](https://arxiv.org/html/2607.09510v1) — first-public（Asia/Shanghai）：2026-07-13；exact evidence：v1；accessed：2026-09-03
- [Seeing is Free, Speaking is Not: Uncovering the True Energy Bottleneck in Edge VLM Inference](https://arxiv.org/html/2607.09520v1) — first-public（Asia/Shanghai）：2026-07-13；exact evidence：v1；accessed：2026-09-03
- [Statistically Undetectable Backdoors in Deep Neural Networks](https://arxiv.org/html/2607.09532v1) — first-public（Asia/Shanghai）：2026-07-13；exact evidence：v1；accessed：2026-09-03
- [Writing Bug Reports for Software Repair Agents: What Information Matters Most?](https://arxiv.org/html/2607.09553v1) — first-public（Asia/Shanghai）：2026-07-13；exact evidence：v1；accessed：2026-09-03
- [Beyond Fixed Representations: The Vocabulary and Verifier Gaps in Open-Ended AI](https://arxiv.org/html/2607.09560v1) — first-public（Asia/Shanghai）：2026-07-13；exact evidence：v1；accessed：2026-09-03
- [TrustX Agent Risk Classification Framework (ARC): Risk-Tiering Internally Created Agentic AI Systems](https://arxiv.org/html/2607.09586v1) — first-public（Asia/Shanghai）：2026-07-13；exact evidence：v1；accessed：2026-09-03
- [PAC-ACT: Post-training Actor-Critic for Action Chunking Transformers](https://arxiv.org/html/2607.09590v1) — first-public（Asia/Shanghai）：2026-07-13；exact evidence：v1；accessed：2026-09-03
- [Agora: Enhancing LLM Agent Reasoning Via Auction-Based Task Allocation](https://arxiv.org/html/2607.09600v1) — first-public（Asia/Shanghai）：2026-07-13；exact evidence：v1；accessed：2026-09-03
- [Mosaic: Runtime-Efficient Multi-Agent Embodied Planning](https://arxiv.org/html/2607.09603v1) — first-public（Asia/Shanghai）：2026-07-13；exact evidence：v1；accessed：2026-09-03
- [PanoWorld: Real-World Panoramic Generation](https://arxiv.org/html/2607.09661v1) — first-public（Asia/Shanghai）：2026-07-13；exact evidence：v1；accessed：2026-09-03

## 13. Final Status

Author-side Coverage screening、denominator、exact-v1 access、62/62 Source Review 与 42-family Deep Selection receipt 已构建；Books 写回仍冻结，四项独立 Semantic Audit 尚未完成。

State Truth: Completion=In Progress；Coverage=Open；Evidence=Open；Books=Open；Unresolved Findings=4。
