# Daily Research — 2026-07-29

**Research Date:** 2026-07-29

**Timezone:** Asia/Shanghai

**Strict Window:** 2026-07-28 09:00:00 ～ 2026-07-29 09:00:00（北京时间，左闭右开）

**Contract:** V2.1 Full Replay；Historical Daily 独立重建，不使用 Weekly 作为 discovery、评分或 Review 来源

**Status:** In Progress；Coverage=Open、Evidence=Open、Books=Open；author-side evidence 已闭合，等待独立 Semantic Audit 与 root Books 比较

## Executive Summary

官方 owner inventory 共 **570** 个 identity；全量 title + abstract 筛选后冻结 **141** 个候选与 **429** 个 family-specific closure，retain rate **24.74%**。exact-v1 Review 为 141/141：Deep 43、Standard 98、blocked 0。

当前只是 author-side evidence 闭合：Books disposition 仍为 `Not Assessed`，四项 fresh-context 独立审计保持 Open。

## 1. Coverage

<!-- validator:report-metadata-v2 -->
| Field | Value |
| --- | --- |
| Contract Version | V2.1 |
| Score Schema | V2 |
| Report Type | Daily |
| Window Start | 2026-07-29 |
| Window End | 2026-07-29 |
| Registry Version | 2026-08-25 |
| Coverage Mode | Full Replay |
| Baseline Report | — |
| Changed Source IDs | — |
| Previous Denominator ID | — |
| Denominator ID | daily-2026-07-29-0900-v2.1-sha256:2c4de6d45f59bd827d334d68ebc5c729b3a17dd9652f1abb148b213e8df2f129 |
| Denominator Frozen At | 2026-09-05T09:00:00+08:00 |
| Completion Status | In Progress |
| Coverage Gate | Open |
| Evidence Gate | Open |
| Books Gate | Open |

### Source Coverage Receipt

<!-- coverage:SRC-ARXIV:20260729:start -->
<!-- validator:source-coverage-v2 -->
| Source ID | Window Start | Window End | Executed At | Endpoint / Filter | Result | Hits | Candidate Source Families | Pagination / Cursor | Window Watermark | Closure Evidence | Gap / Limitation ID |
| --- | --- | --- | --- | --- | --- | ---: | --- | --- | --- | --- | --- |
| SRC-ARXIV | 2026-07-28T09:00:00+08:00 | 2026-07-29T09:00:00+08:00 | 2026-09-05T09:00:00+08:00 | official listings + v1 history + availability schedule; DataCite created only for cycle reconciliation | checked | 570 | SF-2026-ARXIV-2607-24758;SF-2026-ARXIV-2607-24759;SF-2026-ARXIV-2607-24762;SF-2026-ARXIV-2607-24763;SF-2026-ARXIV-2607-24765;SF-2026-ARXIV-2607-24769;SF-2026-ARXIV-2607-24771;SF-2026-ARXIV-2607-24776;SF-2026-ARXIV-2607-24780;SF-2026-ARXIV-2607-24781;SF-2026-ARXIV-2607-24787;SF-2026-ARXIV-2607-24788;SF-2026-ARXIV-2607-24794;SF-2026-ARXIV-2607-24798;SF-2026-ARXIV-2607-24800;SF-2026-ARXIV-2607-24805;SF-2026-ARXIV-2607-24821;SF-2026-ARXIV-2607-24841;SF-2026-ARXIV-2607-24850;SF-2026-ARXIV-2607-24859;SF-2026-ARXIV-2607-24866;SF-2026-ARXIV-2607-24875;SF-2026-ARXIV-2607-24882;SF-2026-ARXIV-2607-24884;SF-2026-ARXIV-2607-24887;SF-2026-ARXIV-2607-24889;SF-2026-ARXIV-2607-24893;SF-2026-ARXIV-2607-24897;SF-2026-ARXIV-2607-24900;SF-2026-ARXIV-2607-24904;SF-2026-ARXIV-2607-24953;SF-2026-ARXIV-2607-24957;SF-2026-ARXIV-2607-24964;SF-2026-ARXIV-2607-24981;SF-2026-ARXIV-2607-24996;SF-2026-ARXIV-2607-25018;SF-2026-ARXIV-2607-25019;SF-2026-ARXIV-2607-25032;SF-2026-ARXIV-2607-25063;SF-2026-ARXIV-2607-25066;SF-2026-ARXIV-2607-25076;SF-2026-ARXIV-2607-25082;SF-2026-ARXIV-2607-25090;SF-2026-ARXIV-2607-25091;SF-2026-ARXIV-2607-25135;SF-2026-ARXIV-2607-25136;SF-2026-ARXIV-2607-25151;SF-2026-ARXIV-2607-25152;SF-2026-ARXIV-2607-25157;SF-2026-ARXIV-2607-25196;SF-2026-ARXIV-2607-25225;SF-2026-ARXIV-2607-25227;SF-2026-ARXIV-2607-25236;SF-2026-ARXIV-2607-25255;SF-2026-ARXIV-2607-25257;SF-2026-ARXIV-2607-25271;SF-2026-ARXIV-2607-25291;SF-2026-ARXIV-2607-25292;SF-2026-ARXIV-2607-25294;SF-2026-ARXIV-2607-25297;SF-2026-ARXIV-2607-25333;SF-2026-ARXIV-2607-25335;SF-2026-ARXIV-2607-25337;SF-2026-ARXIV-2607-25346;SF-2026-ARXIV-2607-25356;SF-2026-ARXIV-2607-25357;SF-2026-ARXIV-2607-25364;SF-2026-ARXIV-2607-25369;SF-2026-ARXIV-2607-25379;SF-2026-ARXIV-2607-25380;SF-2026-ARXIV-2607-25398;SF-2026-ARXIV-2607-25400;SF-2026-ARXIV-2607-25408;SF-2026-ARXIV-2607-25415;SF-2026-ARXIV-2607-25431;SF-2026-ARXIV-2607-25446;SF-2026-ARXIV-2607-25451;SF-2026-ARXIV-2607-25467;SF-2026-ARXIV-2607-25479;SF-2026-ARXIV-2607-25487;SF-2026-ARXIV-2607-25494;SF-2026-ARXIV-2607-25498;SF-2026-ARXIV-2607-25504;SF-2026-ARXIV-2607-25507;SF-2026-ARXIV-2607-25516;SF-2026-ARXIV-2607-25554;SF-2026-ARXIV-2607-25560;SF-2026-ARXIV-2607-25566;SF-2026-ARXIV-2607-25583;SF-2026-ARXIV-2607-25589;SF-2026-ARXIV-2607-25600;SF-2026-ARXIV-2607-25614;SF-2026-ARXIV-2607-25619;SF-2026-ARXIV-2607-25635;SF-2026-ARXIV-2607-25637;SF-2026-ARXIV-2607-25650;SF-2026-ARXIV-2607-25651;SF-2026-ARXIV-2607-25656;SF-2026-ARXIV-2607-25659;SF-2026-ARXIV-2607-25663;SF-2026-ARXIV-2607-25669;SF-2026-ARXIV-2607-25718;SF-2026-ARXIV-2607-25750;SF-2026-ARXIV-2607-25765;SF-2026-ARXIV-2607-25798;SF-2026-ARXIV-2607-25816;SF-2026-ARXIV-2607-25818;SF-2026-ARXIV-2607-25825;SF-2026-ARXIV-2607-25831;SF-2026-ARXIV-2607-25852;SF-2026-ARXIV-2607-25853;SF-2026-ARXIV-2607-25857;SF-2026-ARXIV-2607-25877;SF-2026-ARXIV-2607-25880;SF-2026-ARXIV-2607-25883;SF-2026-ARXIV-2607-25884;SF-2026-ARXIV-2607-25886;SF-2026-ARXIV-2607-25890;SF-2026-ARXIV-2607-25891;SF-2026-ARXIV-2607-25904;SF-2026-ARXIV-2607-25907;SF-2026-ARXIV-2607-25912;SF-2026-ARXIV-2607-25914;SF-2026-ARXIV-2607-25915;SF-2026-ARXIV-2607-25918;SF-2026-ARXIV-2607-25936;SF-2026-ARXIV-2607-25948;SF-2026-ARXIV-2607-25970;SF-2026-ARXIV-2607-25987;SF-2026-ARXIV-2607-25992;SF-2026-ARXIV-2607-25995;SF-2026-ARXIV-2607-25996;SF-2026-ARXIV-2607-26004;SF-2026-ARXIV-2607-26016;SF-2026-ARXIV-2607-26017;SF-2026-ARXIV-2607-26037;SF-2026-ARXIV-2607-26040;SF-2026-ARXIV-2607-26041;SF-2026-ARXIV-2607-26052;SF-2026-ARXIV-2607-26055;SF-2026-ARXIV-2607-26056 | all registered category pages; cross-category dedup complete | 2026-07-29T09:00:00+08:00 | sha256:2c4de6d45f59bd827d334d68ebc5c729b3a17dd9652f1abb148b213e8df2f129 | — |
<!-- coverage:SRC-ARXIV:20260729:end -->

### Coverage Limitations

- DataCite 只辅助 owner reconciliation；技术结论全部回到 official exact arXiv v1。
- author-side receipt 已闭合，独立 false-positive / false-negative audit 尚未签收。

## 2. Candidate Ledger

<!-- validator:candidate-ledger-v2.1 -->
| Source Family ID | Primary Identifier | Event Identity | Owner Week | First-public Date | Supporting Source IDs | Design Delta | System Reach | Durability | Total | Candidate State | Review Status | Access Status | Review Override | Review Ref | Owner Report Ref | Prior Review Ref | Reconciliation | Stable Node ID | Books Disposition | Books Review Ref | Benchmark Claim |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2607-24758 | arXiv:2607.24758v1 | paper-v1:2607.24758 | 2026-W31 | 2026-07-29 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-24758 | self | — | new_in_window | PLATFORM-SECURITY | Not Assessed | — | no |
| SF-2026-ARXIV-2607-24759 | arXiv:2607.24759v1 | paper-v1:2607.24759 | 2026-W31 | 2026-07-29 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-24759 | self | — | new_in_window | AGENT-MEMORY | Not Assessed | — | no |
| SF-2026-ARXIV-2607-24762 | arXiv:2607.24762v1 | paper-v1:2607.24762 | 2026-W31 | 2026-07-29 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-24762 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-24763 | arXiv:2607.24763v1 | paper-v1:2607.24763 | 2026-W31 | 2026-07-29 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-24763 | self | — | new_in_window | MULTIMODAL-GENERATIVE-PARADIGMS | Not Assessed | — | no |
| SF-2026-ARXIV-2607-24765 | arXiv:2607.24765v1 | paper-v1:2607.24765 | 2026-W31 | 2026-07-29 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-24765 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-24769 | arXiv:2607.24769v1 | paper-v1:2607.24769 | 2026-W31 | 2026-07-29 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-24769 | self | — | new_in_window | PLATFORM-SECURITY | Not Assessed | — | no |
| SF-2026-ARXIV-2607-24771 | arXiv:2607.24771v1 | paper-v1:2607.24771 | 2026-W31 | 2026-07-29 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-24771 | self | — | new_in_window | TRAIN-SFT | Not Assessed | — | no |
| SF-2026-ARXIV-2607-24776 | arXiv:2607.24776v1 | paper-v1:2607.24776 | 2026-W31 | 2026-07-29 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-24776 | self | — | new_in_window | AGENT-RAG | Not Assessed | — | no |
| SF-2026-ARXIV-2607-24780 | arXiv:2607.24780v1 | paper-v1:2607.24780 | 2026-W31 | 2026-07-29 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-24780 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-24781 | arXiv:2607.24781v1 | paper-v1:2607.24781 | 2026-W31 | 2026-07-29 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-24781 | self | — | new_in_window | AGENT-RAG | Not Assessed | — | no |
| SF-2026-ARXIV-2607-24787 | arXiv:2607.24787v1 | paper-v1:2607.24787 | 2026-W31 | 2026-07-29 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-24787 | self | — | new_in_window | MODEL-MOE | Not Assessed | — | no |
| SF-2026-ARXIV-2607-24788 | arXiv:2607.24788v1 | paper-v1:2607.24788 | 2026-W31 | 2026-07-29 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-24788 | self | — | new_in_window | INFER-DECODE | Not Assessed | — | no |
| SF-2026-ARXIV-2607-24794 | arXiv:2607.24794v1 | paper-v1:2607.24794 | 2026-W31 | 2026-07-29 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-24794 | self | — | new_in_window | MULTIMODAL-REPRESENTATION | Not Assessed | — | no |
| SF-2026-ARXIV-2607-24798 | arXiv:2607.24798v1 | paper-v1:2607.24798 | 2026-W31 | 2026-07-29 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-24798 | self | — | new_in_window | AGENT-MEMORY | Not Assessed | — | no |
| SF-2026-ARXIV-2607-24800 | arXiv:2607.24800v1 | paper-v1:2607.24800 | 2026-W31 | 2026-07-29 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-24800 | self | — | new_in_window | AGENT-RAG | Not Assessed | — | no |
| SF-2026-ARXIV-2607-24805 | arXiv:2607.24805v1 | paper-v1:2607.24805 | 2026-W31 | 2026-07-29 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-24805 | self | — | new_in_window | AGENT-MEMORY | Not Assessed | — | no |
| SF-2026-ARXIV-2607-24821 | arXiv:2607.24821v1 | paper-v1:2607.24821 | 2026-W31 | 2026-07-29 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-24821 | self | — | new_in_window | MULTIMODAL-GENERATIVE-PARADIGMS | Not Assessed | — | no |
| SF-2026-ARXIV-2607-24841 | arXiv:2607.24841v1 | paper-v1:2607.24841 | 2026-W31 | 2026-07-29 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-24841 | self | — | new_in_window | MULTIMODAL-GENERATIVE-PARADIGMS | Not Assessed | — | no |
| SF-2026-ARXIV-2607-24850 | arXiv:2607.24850v1 | paper-v1:2607.24850 | 2026-W31 | 2026-07-29 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-24850 | self | — | new_in_window | AGENT-WORKFLOW | Not Assessed | — | no |
| SF-2026-ARXIV-2607-24859 | arXiv:2607.24859v1 | paper-v1:2607.24859 | 2026-W31 | 2026-07-29 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-24859 | self | — | new_in_window | PLATFORM-SECURITY | Not Assessed | — | no |
| SF-2026-ARXIV-2607-24866 | arXiv:2607.24866v1 | paper-v1:2607.24866 | 2026-W31 | 2026-07-29 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-24866 | self | — | new_in_window | PLATFORM-SECURITY | Not Assessed | — | no |
| SF-2026-ARXIV-2607-24875 | arXiv:2607.24875v1 | paper-v1:2607.24875 | 2026-W31 | 2026-07-29 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-24875 | self | — | new_in_window | AGENT-RAG | Not Assessed | — | no |
| SF-2026-ARXIV-2607-24882 | arXiv:2607.24882v1 | paper-v1:2607.24882 | 2026-W31 | 2026-07-29 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-24882 | self | — | new_in_window | AGENT-CONTEXT | Not Assessed | — | no |
| SF-2026-ARXIV-2607-24884 | arXiv:2607.24884v1 | paper-v1:2607.24884 | 2026-W31 | 2026-07-29 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-24884 | self | — | new_in_window | AGENT-RAG | Not Assessed | — | no |
| SF-2026-ARXIV-2607-24887 | arXiv:2607.24887v1 | paper-v1:2607.24887 | 2026-W31 | 2026-07-29 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-24887 | self | — | new_in_window | MODEL-TRANSFORMER-LAYER | Not Assessed | — | no |
| SF-2026-ARXIV-2607-24889 | arXiv:2607.24889v1 | paper-v1:2607.24889 | 2026-W31 | 2026-07-29 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-24889 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-24893 | arXiv:2607.24893v1 | paper-v1:2607.24893 | 2026-W31 | 2026-07-29 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-24893 | self | — | new_in_window | AGENT-MULTI-AGENT | Not Assessed | — | no |
| SF-2026-ARXIV-2607-24897 | arXiv:2607.24897v1 | paper-v1:2607.24897 | 2026-W31 | 2026-07-29 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-24897 | self | — | new_in_window | PLATFORM-SECURITY | Not Assessed | — | no |
| SF-2026-ARXIV-2607-24900 | arXiv:2607.24900v1 | paper-v1:2607.24900 | 2026-W31 | 2026-07-29 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-24900 | self | — | new_in_window | TRAIN-RLHF | Not Assessed | — | no |
| SF-2026-ARXIV-2607-24904 | arXiv:2607.24904v1 | paper-v1:2607.24904 | 2026-W31 | 2026-07-29 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-24904 | self | — | new_in_window | MULTIMODAL-REPRESENTATION | Not Assessed | — | no |
| SF-2026-ARXIV-2607-24953 | arXiv:2607.24953v1 | paper-v1:2607.24953 | 2026-W31 | 2026-07-29 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-24953 | self | — | new_in_window | TRAIN-DISTRIBUTED-TRAINING | Not Assessed | — | no |
| SF-2026-ARXIV-2607-24957 | arXiv:2607.24957v1 | paper-v1:2607.24957 | 2026-W31 | 2026-07-29 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-24957 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-24964 | arXiv:2607.24964v1 | paper-v1:2607.24964 | 2026-W31 | 2026-07-29 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-24964 | self | — | new_in_window | PLATFORM-SECURITY | Not Assessed | — | no |
| SF-2026-ARXIV-2607-24981 | arXiv:2607.24981v1 | paper-v1:2607.24981 | 2026-W31 | 2026-07-29 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-24981 | self | — | new_in_window | INFER-TENSORRT-LLM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-24996 | arXiv:2607.24996v1 | paper-v1:2607.24996 | 2026-W31 | 2026-07-29 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-24996 | self | — | new_in_window | TRAIN-PPO | Not Assessed | — | no |
| SF-2026-ARXIV-2607-25018 | arXiv:2607.25018v1 | paper-v1:2607.25018 | 2026-W31 | 2026-07-29 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-25018 | self | — | new_in_window | INFER-SCHEDULING | Not Assessed | — | no |
| SF-2026-ARXIV-2607-25019 | arXiv:2607.25019v1 | paper-v1:2607.25019 | 2026-W31 | 2026-07-29 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-25019 | self | — | new_in_window | TRAIN-RLHF | Not Assessed | — | no |
| SF-2026-ARXIV-2607-25032 | arXiv:2607.25032v1 | paper-v1:2607.25032 | 2026-W31 | 2026-07-29 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-25032 | self | — | new_in_window | AGENT-SKILL | Not Assessed | — | no |
| SF-2026-ARXIV-2607-25063 | arXiv:2607.25063v1 | paper-v1:2607.25063 | 2026-W31 | 2026-07-29 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-25063 | self | — | new_in_window | TRAIN-PRETRAINING | Not Assessed | — | no |
| SF-2026-ARXIV-2607-25066 | arXiv:2607.25066v1 | paper-v1:2607.25066 | 2026-W31 | 2026-07-29 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-25066 | self | — | new_in_window | AGENT-MEMORY | Not Assessed | — | no |
| SF-2026-ARXIV-2607-25076 | arXiv:2607.25076v1 | paper-v1:2607.25076 | 2026-W31 | 2026-07-29 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-25076 | self | — | new_in_window | AGENT-PLATFORM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-25082 | arXiv:2607.25082v1 | paper-v1:2607.25082 | 2026-W31 | 2026-07-29 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-25082 | self | — | new_in_window | AGENT-PLATFORM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-25090 | arXiv:2607.25090v1 | paper-v1:2607.25090 | 2026-W31 | 2026-07-29 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-25090 | self | — | new_in_window | AGENT-MULTI-AGENT | Not Assessed | — | no |
| SF-2026-ARXIV-2607-25091 | arXiv:2607.25091v1 | paper-v1:2607.25091 | 2026-W31 | 2026-07-29 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-25091 | self | — | new_in_window | AGENT-WORKFLOW | Not Assessed | — | no |
| SF-2026-ARXIV-2607-25135 | arXiv:2607.25135v1 | paper-v1:2607.25135 | 2026-W31 | 2026-07-29 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-25135 | self | — | new_in_window | AGENT-RAG | Not Assessed | — | no |
| SF-2026-ARXIV-2607-25136 | arXiv:2607.25136v1 | paper-v1:2607.25136 | 2026-W31 | 2026-07-29 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-25136 | self | — | new_in_window | TRAIN-DPO | Not Assessed | — | no |
| SF-2026-ARXIV-2607-25151 | arXiv:2607.25151v1 | paper-v1:2607.25151 | 2026-W31 | 2026-07-29 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-25151 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-25152 | arXiv:2607.25152v1 | paper-v1:2607.25152 | 2026-W31 | 2026-07-29 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-25152 | self | — | new_in_window | AGENT-REFLECTION | Not Assessed | — | no |
| SF-2026-ARXIV-2607-25157 | arXiv:2607.25157v1 | paper-v1:2607.25157 | 2026-W31 | 2026-07-29 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-25157 | self | — | new_in_window | MULTIMODAL-GENERATIVE-PARADIGMS | Not Assessed | — | no |
| SF-2026-ARXIV-2607-25196 | arXiv:2607.25196v1 | paper-v1:2607.25196 | 2026-W31 | 2026-07-29 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-25196 | self | — | new_in_window | MULTIMODAL-REPRESENTATION | Not Assessed | — | no |
| SF-2026-ARXIV-2607-25225 | arXiv:2607.25225v1 | paper-v1:2607.25225 | 2026-W31 | 2026-07-29 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-25225 | self | — | new_in_window | PLATFORM-SECURITY | Not Assessed | — | no |
| SF-2026-ARXIV-2607-25227 | arXiv:2607.25227v1 | paper-v1:2607.25227 | 2026-W31 | 2026-07-29 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-25227 | self | — | new_in_window | PLATFORM-SECURITY | Not Assessed | — | no |
| SF-2026-ARXIV-2607-25236 | arXiv:2607.25236v1 | paper-v1:2607.25236 | 2026-W31 | 2026-07-29 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-25236 | self | — | new_in_window | MULTIMODAL-WORLD-MODELS | Not Assessed | — | no |
| SF-2026-ARXIV-2607-25255 | arXiv:2607.25255v1 | paper-v1:2607.25255 | 2026-W31 | 2026-07-29 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-25255 | self | — | new_in_window | PLATFORM-SECURITY | Not Assessed | — | no |
| SF-2026-ARXIV-2607-25257 | arXiv:2607.25257v1 | paper-v1:2607.25257 | 2026-W31 | 2026-07-29 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-25257 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-25271 | arXiv:2607.25271v1 | paper-v1:2607.25271 | 2026-W31 | 2026-07-29 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-25271 | self | — | new_in_window | TRAIN-PRETRAINING | Not Assessed | — | no |
| SF-2026-ARXIV-2607-25291 | arXiv:2607.25291v1 | paper-v1:2607.25291 | 2026-W31 | 2026-07-29 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-25291 | self | — | new_in_window | INFER-PREFILL | Not Assessed | — | no |
| SF-2026-ARXIV-2607-25292 | arXiv:2607.25292v1 | paper-v1:2607.25292 | 2026-W31 | 2026-07-29 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-25292 | self | — | new_in_window | MODEL-SAMPLING | Not Assessed | — | no |
| SF-2026-ARXIV-2607-25294 | arXiv:2607.25294v1 | paper-v1:2607.25294 | 2026-W31 | 2026-07-29 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-25294 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-25297 | arXiv:2607.25297v1 | paper-v1:2607.25297 | 2026-W31 | 2026-07-29 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-25297 | self | — | new_in_window | AGENT-MCP | Not Assessed | — | no |
| SF-2026-ARXIV-2607-25333 | arXiv:2607.25333v1 | paper-v1:2607.25333 | 2026-W31 | 2026-07-29 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-25333 | self | — | new_in_window | AGENT-WORKFLOW | Not Assessed | — | no |
| SF-2026-ARXIV-2607-25335 | arXiv:2607.25335v1 | paper-v1:2607.25335 | 2026-W31 | 2026-07-29 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-25335 | self | — | new_in_window | AGENT-PROMPT | Not Assessed | — | no |
| SF-2026-ARXIV-2607-25337 | arXiv:2607.25337v1 | paper-v1:2607.25337 | 2026-W31 | 2026-07-29 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-25337 | self | — | new_in_window | MULTIMODAL-WORLD-MODELS | Not Assessed | — | no |
| SF-2026-ARXIV-2607-25346 | arXiv:2607.25346v1 | paper-v1:2607.25346 | 2026-W31 | 2026-07-29 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-25346 | self | — | new_in_window | AGENT-RAG | Not Assessed | — | no |
| SF-2026-ARXIV-2607-25356 | arXiv:2607.25356v1 | paper-v1:2607.25356 | 2026-W31 | 2026-07-29 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-25356 | self | — | new_in_window | TRAIN-DATA | Not Assessed | — | no |
| SF-2026-ARXIV-2607-25357 | arXiv:2607.25357v1 | paper-v1:2607.25357 | 2026-W31 | 2026-07-29 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-25357 | self | — | new_in_window | MODEL-LONG-CONTEXT | Not Assessed | — | no |
| SF-2026-ARXIV-2607-25364 | arXiv:2607.25364v1 | paper-v1:2607.25364 | 2026-W31 | 2026-07-29 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-25364 | self | — | new_in_window | AGENT-TOOL-CALLING | Not Assessed | — | no |
| SF-2026-ARXIV-2607-25369 | arXiv:2607.25369v1 | paper-v1:2607.25369 | 2026-W31 | 2026-07-29 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-25369 | self | — | new_in_window | AGENT-WORKFLOW | Not Assessed | — | no |
| SF-2026-ARXIV-2607-25379 | arXiv:2607.25379v1 | paper-v1:2607.25379 | 2026-W31 | 2026-07-29 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-25379 | self | — | new_in_window | PLATFORM-SECURITY | Not Assessed | — | no |
| SF-2026-ARXIV-2607-25380 | arXiv:2607.25380v1 | paper-v1:2607.25380 | 2026-W31 | 2026-07-29 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-25380 | self | — | new_in_window | AGENT-MEMORY | Not Assessed | — | no |
| SF-2026-ARXIV-2607-25398 | arXiv:2607.25398v1 | paper-v1:2607.25398 | 2026-W31 | 2026-07-29 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-25398 | self | — | new_in_window | AGENT-CONTEXT | Not Assessed | — | no |
| SF-2026-ARXIV-2607-25400 | arXiv:2607.25400v1 | paper-v1:2607.25400 | 2026-W31 | 2026-07-29 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-25400 | self | — | new_in_window | AGENT-WORKFLOW | Not Assessed | — | no |
| SF-2026-ARXIV-2607-25408 | arXiv:2607.25408v1 | paper-v1:2607.25408 | 2026-W31 | 2026-07-29 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-25408 | self | — | new_in_window | AGENT-CONTEXT | Not Assessed | — | no |
| SF-2026-ARXIV-2607-25415 | arXiv:2607.25415v1 | paper-v1:2607.25415 | 2026-W31 | 2026-07-29 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-25415 | self | — | new_in_window | AGENT-MEMORY | Not Assessed | — | no |
| SF-2026-ARXIV-2607-25431 | arXiv:2607.25431v1 | paper-v1:2607.25431 | 2026-W31 | 2026-07-29 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-25431 | self | — | new_in_window | AGENT-CONTEXT | Not Assessed | — | no |
| SF-2026-ARXIV-2607-25446 | arXiv:2607.25446v1 | paper-v1:2607.25446 | 2026-W31 | 2026-07-29 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-25446 | self | — | new_in_window | AGENT-MULTI-AGENT | Not Assessed | — | no |
| SF-2026-ARXIV-2607-25451 | arXiv:2607.25451v1 | paper-v1:2607.25451 | 2026-W31 | 2026-07-29 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-25451 | self | — | new_in_window | INFER-TENSORRT-LLM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-25467 | arXiv:2607.25467v1 | paper-v1:2607.25467 | 2026-W31 | 2026-07-29 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-25467 | self | — | new_in_window | MULTIMODAL-REPRESENTATION | Not Assessed | — | no |
| SF-2026-ARXIV-2607-25479 | arXiv:2607.25479v1 | paper-v1:2607.25479 | 2026-W31 | 2026-07-29 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-25479 | self | — | new_in_window | PLATFORM-MODEL-REGISTRY | Not Assessed | — | no |
| SF-2026-ARXIV-2607-25487 | arXiv:2607.25487v1 | paper-v1:2607.25487 | 2026-W31 | 2026-07-29 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-25487 | self | — | new_in_window | MULTIMODAL-EMBODIED-VLA | Not Assessed | — | no |
| SF-2026-ARXIV-2607-25494 | arXiv:2607.25494v1 | paper-v1:2607.25494 | 2026-W31 | 2026-07-29 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-25494 | self | — | new_in_window | INFER-TENSORRT-LLM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-25498 | arXiv:2607.25498v1 | paper-v1:2607.25498 | 2026-W31 | 2026-07-29 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-25498 | self | — | new_in_window | INFER-TENSORRT-LLM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-25504 | arXiv:2607.25504v1 | paper-v1:2607.25504 | 2026-W31 | 2026-07-29 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-25504 | self | — | new_in_window | INFER-TENSORRT-LLM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-25507 | arXiv:2607.25507v1 | paper-v1:2607.25507 | 2026-W31 | 2026-07-29 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-25507 | self | — | new_in_window | MODEL-POSITION-ENCODING | Not Assessed | — | no |
| SF-2026-ARXIV-2607-25516 | arXiv:2607.25516v1 | paper-v1:2607.25516 | 2026-W31 | 2026-07-29 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-25516 | self | — | new_in_window | MULTIMODAL-EMBODIED-VLA | Not Assessed | — | no |
| SF-2026-ARXIV-2607-25554 | arXiv:2607.25554v1 | paper-v1:2607.25554 | 2026-W31 | 2026-07-29 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-25554 | self | — | new_in_window | AGENT-WORKFLOW | Not Assessed | — | no |
| SF-2026-ARXIV-2607-25560 | arXiv:2607.25560v1 | paper-v1:2607.25560 | 2026-W31 | 2026-07-29 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-25560 | self | — | new_in_window | AGENT-SKILL | Not Assessed | — | no |
| SF-2026-ARXIV-2607-25566 | arXiv:2607.25566v1 | paper-v1:2607.25566 | 2026-W31 | 2026-07-29 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-25566 | self | — | new_in_window | AGENT-WORKFLOW | Not Assessed | — | no |
| SF-2026-ARXIV-2607-25583 | arXiv:2607.25583v1 | paper-v1:2607.25583 | 2026-W31 | 2026-07-29 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-25583 | self | — | new_in_window | TRAIN-LORA | Not Assessed | — | no |
| SF-2026-ARXIV-2607-25589 | arXiv:2607.25589v1 | paper-v1:2607.25589 | 2026-W31 | 2026-07-29 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-25589 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-25600 | arXiv:2607.25600v1 | paper-v1:2607.25600 | 2026-W31 | 2026-07-29 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-25600 | self | — | new_in_window | AGENT-RAG | Not Assessed | — | no |
| SF-2026-ARXIV-2607-25614 | arXiv:2607.25614v1 | paper-v1:2607.25614 | 2026-W31 | 2026-07-29 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-25614 | self | — | new_in_window | TRAIN-SFT | Not Assessed | — | no |
| SF-2026-ARXIV-2607-25619 | arXiv:2607.25619v1 | paper-v1:2607.25619 | 2026-W31 | 2026-07-29 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-25619 | self | — | new_in_window | AGENT-SKILL | Not Assessed | — | no |
| SF-2026-ARXIV-2607-25635 | arXiv:2607.25635v1 | paper-v1:2607.25635 | 2026-W31 | 2026-07-29 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-25635 | self | — | new_in_window | AGENT-MCP | Not Assessed | — | no |
| SF-2026-ARXIV-2607-25637 | arXiv:2607.25637v1 | paper-v1:2607.25637 | 2026-W31 | 2026-07-29 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-25637 | self | — | new_in_window | AGENT-SKILL | Not Assessed | — | no |
| SF-2026-ARXIV-2607-25650 | arXiv:2607.25650v1 | paper-v1:2607.25650 | 2026-W31 | 2026-07-29 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-25650 | self | — | new_in_window | TRAIN-DISTRIBUTED-TRAINING | Not Assessed | — | no |
| SF-2026-ARXIV-2607-25651 | arXiv:2607.25651v1 | paper-v1:2607.25651 | 2026-W31 | 2026-07-29 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-25651 | self | — | new_in_window | INFER-TENSORRT-LLM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-25656 | arXiv:2607.25656v1 | paper-v1:2607.25656 | 2026-W31 | 2026-07-29 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-25656 | self | — | new_in_window | AGENT-MULTI-AGENT | Not Assessed | — | no |
| SF-2026-ARXIV-2607-25659 | arXiv:2607.25659v1 | paper-v1:2607.25659 | 2026-W31 | 2026-07-29 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-25659 | self | — | new_in_window | TRAIN-GRPO | Not Assessed | — | no |
| SF-2026-ARXIV-2607-25663 | arXiv:2607.25663v1 | paper-v1:2607.25663 | 2026-W31 | 2026-07-29 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-25663 | self | — | new_in_window | MODEL-TRANSFORMER-LAYER | Not Assessed | — | no |
| SF-2026-ARXIV-2607-25669 | arXiv:2607.25669v1 | paper-v1:2607.25669 | 2026-W31 | 2026-07-29 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-25669 | self | — | new_in_window | MULTIMODAL-REPRESENTATION | Not Assessed | — | no |
| SF-2026-ARXIV-2607-25718 | arXiv:2607.25718v1 | paper-v1:2607.25718 | 2026-W31 | 2026-07-29 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-25718 | self | — | new_in_window | AGENT-TOOL-CALLING | Not Assessed | — | no |
| SF-2026-ARXIV-2607-25750 | arXiv:2607.25750v1 | paper-v1:2607.25750 | 2026-W31 | 2026-07-29 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-25750 | self | — | new_in_window | PLATFORM-MODEL-REGISTRY | Not Assessed | — | no |
| SF-2026-ARXIV-2607-25765 | arXiv:2607.25765v1 | paper-v1:2607.25765 | 2026-W31 | 2026-07-29 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-25765 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-25798 | arXiv:2607.25798v1 | paper-v1:2607.25798 | 2026-W31 | 2026-07-29 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-25798 | self | — | new_in_window | MULTIMODAL-EMBODIED-VLA | Not Assessed | — | no |
| SF-2026-ARXIV-2607-25816 | arXiv:2607.25816v1 | paper-v1:2607.25816 | 2026-W31 | 2026-07-29 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-25816 | self | — | new_in_window | INFER-SPECULATIVE-DECODING | Not Assessed | — | no |
| SF-2026-ARXIV-2607-25818 | arXiv:2607.25818v1 | paper-v1:2607.25818 | 2026-W31 | 2026-07-29 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-25818 | self | — | new_in_window | MULTIMODAL-REPRESENTATION | Not Assessed | — | no |
| SF-2026-ARXIV-2607-25825 | arXiv:2607.25825v1 | paper-v1:2607.25825 | 2026-W31 | 2026-07-29 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-25825 | self | — | new_in_window | AGENT-WORKFLOW | Not Assessed | — | no |
| SF-2026-ARXIV-2607-25831 | arXiv:2607.25831v1 | paper-v1:2607.25831 | 2026-W31 | 2026-07-29 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-25831 | self | — | new_in_window | INFER-TENSORRT-LLM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-25852 | arXiv:2607.25852v1 | paper-v1:2607.25852 | 2026-W31 | 2026-07-29 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-25852 | self | — | new_in_window | INFER-SPECULATIVE-DECODING | Not Assessed | — | no |
| SF-2026-ARXIV-2607-25853 | arXiv:2607.25853v1 | paper-v1:2607.25853 | 2026-W31 | 2026-07-29 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-25853 | self | — | new_in_window | AGENT-SKILL | Not Assessed | — | no |
| SF-2026-ARXIV-2607-25857 | arXiv:2607.25857v1 | paper-v1:2607.25857 | 2026-W31 | 2026-07-29 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-25857 | self | — | new_in_window | PLATFORM-SECURITY | Not Assessed | — | no |
| SF-2026-ARXIV-2607-25877 | arXiv:2607.25877v1 | paper-v1:2607.25877 | 2026-W31 | 2026-07-29 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-25877 | self | — | new_in_window | AGENT-MULTI-AGENT | Not Assessed | — | no |
| SF-2026-ARXIV-2607-25880 | arXiv:2607.25880v1 | paper-v1:2607.25880 | 2026-W31 | 2026-07-29 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-25880 | self | — | new_in_window | PLATFORM-MODEL-REGISTRY | Not Assessed | — | no |
| SF-2026-ARXIV-2607-25883 | arXiv:2607.25883v1 | paper-v1:2607.25883 | 2026-W31 | 2026-07-29 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-25883 | self | — | new_in_window | AGENT-PLATFORM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-25884 | arXiv:2607.25884v1 | paper-v1:2607.25884 | 2026-W31 | 2026-07-29 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-25884 | self | — | new_in_window | INFER-TENSORRT-LLM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-25886 | arXiv:2607.25886v1 | paper-v1:2607.25886 | 2026-W31 | 2026-07-29 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-25886 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-25890 | arXiv:2607.25890v1 | paper-v1:2607.25890 | 2026-W31 | 2026-07-29 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-25890 | self | — | new_in_window | PLATFORM-SECURITY | Not Assessed | — | no |
| SF-2026-ARXIV-2607-25891 | arXiv:2607.25891v1 | paper-v1:2607.25891 | 2026-W31 | 2026-07-29 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-25891 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-25904 | arXiv:2607.25904v1 | paper-v1:2607.25904 | 2026-W31 | 2026-07-29 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-25904 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-25907 | arXiv:2607.25907v1 | paper-v1:2607.25907 | 2026-W31 | 2026-07-29 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-25907 | self | — | new_in_window | PLATFORM-SECURITY | Not Assessed | — | no |
| SF-2026-ARXIV-2607-25912 | arXiv:2607.25912v1 | paper-v1:2607.25912 | 2026-W31 | 2026-07-29 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-25912 | self | — | new_in_window | MULTIMODAL-EMBODIED-VLA | Not Assessed | — | no |
| SF-2026-ARXIV-2607-25914 | arXiv:2607.25914v1 | paper-v1:2607.25914 | 2026-W31 | 2026-07-29 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-25914 | self | — | new_in_window | AGENT-TOOL-CALLING | Not Assessed | — | no |
| SF-2026-ARXIV-2607-25915 | arXiv:2607.25915v1 | paper-v1:2607.25915 | 2026-W31 | 2026-07-29 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-25915 | self | — | new_in_window | MODEL-TRANSFORMER-LAYER | Not Assessed | — | no |
| SF-2026-ARXIV-2607-25918 | arXiv:2607.25918v1 | paper-v1:2607.25918 | 2026-W31 | 2026-07-29 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-25918 | self | — | new_in_window | MULTIMODAL-WORLD-MODELS | Not Assessed | — | no |
| SF-2026-ARXIV-2607-25936 | arXiv:2607.25936v1 | paper-v1:2607.25936 | 2026-W31 | 2026-07-29 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-25936 | self | — | new_in_window | PLATFORM-SECURITY | Not Assessed | — | no |
| SF-2026-ARXIV-2607-25948 | arXiv:2607.25948v1 | paper-v1:2607.25948 | 2026-W31 | 2026-07-29 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-25948 | self | — | new_in_window | MULTIMODAL-GENERATIVE-PARADIGMS | Not Assessed | — | no |
| SF-2026-ARXIV-2607-25970 | arXiv:2607.25970v1 | paper-v1:2607.25970 | 2026-W31 | 2026-07-29 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-25970 | self | — | new_in_window | TRAIN-GRPO | Not Assessed | — | no |
| SF-2026-ARXIV-2607-25987 | arXiv:2607.25987v1 | paper-v1:2607.25987 | 2026-W31 | 2026-07-29 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-25987 | self | — | new_in_window | PLATFORM-SECURITY | Not Assessed | — | no |
| SF-2026-ARXIV-2607-25992 | arXiv:2607.25992v1 | paper-v1:2607.25992 | 2026-W31 | 2026-07-29 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-25992 | self | — | new_in_window | AGENT-MEMORY | Not Assessed | — | no |
| SF-2026-ARXIV-2607-25995 | arXiv:2607.25995v1 | paper-v1:2607.25995 | 2026-W31 | 2026-07-29 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-25995 | self | — | new_in_window | PLATFORM-SECURITY | Not Assessed | — | no |
| SF-2026-ARXIV-2607-25996 | arXiv:2607.25996v1 | paper-v1:2607.25996 | 2026-W31 | 2026-07-29 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-25996 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-26004 | arXiv:2607.26004v1 | paper-v1:2607.26004 | 2026-W31 | 2026-07-29 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-26004 | self | — | new_in_window | MULTIMODAL-GENERATIVE-PARADIGMS | Not Assessed | — | no |
| SF-2026-ARXIV-2607-26016 | arXiv:2607.26016v1 | paper-v1:2607.26016 | 2026-W31 | 2026-07-29 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-26016 | self | — | new_in_window | INFER-TENSORRT-LLM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-26017 | arXiv:2607.26017v1 | paper-v1:2607.26017 | 2026-W31 | 2026-07-29 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-26017 | self | — | new_in_window | AGENT-MEMORY | Not Assessed | — | no |
| SF-2026-ARXIV-2607-26037 | arXiv:2607.26037v1 | paper-v1:2607.26037 | 2026-W31 | 2026-07-29 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-26037 | self | — | new_in_window | MULTIMODAL-WORLD-MODELS | Not Assessed | — | no |
| SF-2026-ARXIV-2607-26040 | arXiv:2607.26040v1 | paper-v1:2607.26040 | 2026-W31 | 2026-07-29 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-26040 | self | — | new_in_window | MULTIMODAL-WORLD-MODELS | Not Assessed | — | no |
| SF-2026-ARXIV-2607-26041 | arXiv:2607.26041v1 | paper-v1:2607.26041 | 2026-W31 | 2026-07-29 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-26041 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-26052 | arXiv:2607.26052v1 | paper-v1:2607.26052 | 2026-W31 | 2026-07-29 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-26052 | self | — | new_in_window | MODEL-MOE | Not Assessed | — | no |
| SF-2026-ARXIV-2607-26055 | arXiv:2607.26055v1 | paper-v1:2607.26055 | 2026-W31 | 2026-07-29 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-26055 | self | — | new_in_window | MULTIMODAL-EMBODIED-VLA | Not Assessed | — | no |
| SF-2026-ARXIV-2607-26056 | arXiv:2607.26056v1 | paper-v1:2607.26056 | 2026-W31 | 2026-07-29 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-26056 | self | — | new_in_window | MULTIMODAL-WORLD-MODELS | Not Assessed | — | no |

## 3. Review Completion Receipt

<!-- validator:review-completion-v1 -->
| Source Family ID | Review Provenance ID | Review Route | Primary Evidence Version | Reviewed Evidence Versions | Method / Identity Locators | Evaluation Locators | Limitations / Counterevidence Locators | Artifact Locators | Claim Boundary Ref | Completion Result |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2607-24758 | RP-7529c7a39b382057 | deep | arXiv:2607.24758v1 | SRC-ARXIV@arXiv:2607.24758v1 | https://arxiv.org/html/2607.24758v1#A4.SS1 — D.1 Design; https://arxiv.org/html/2607.24758v1#S3 — 3 Methods | https://arxiv.org/html/2607.24758v1#A3 — Appendix C CoT analysis; https://arxiv.org/html/2607.24758v1#A3.SS3 — C.3 Evaluation-awareness and spontaneous consequence reasoning | https://arxiv.org/html/2607.24758v1#S5 — 5 Discussion; https://arxiv.org/html/2607.24758v1#S6 — 6 Limitations | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-24758 | complete |
| SF-2026-ARXIV-2607-24759 | RP-8a6054e6f4a89aaa | deep | arXiv:2607.24759v1 | SRC-ARXIV@arXiv:2607.24759v1 | https://arxiv.org/html/2607.24759v1#Sx1.SSx4 — 4 Three-axis architecture; https://arxiv.org/html/2607.24759v1#Sx1.SSx8 — 5.3 Case C: In-progress multi-agent deployment (design report) | https://arxiv.org/html/2607.24759v1#Sx1 — Abstract; https://arxiv.org/html/2607.24759v1#Sx1.SSx1 — 1 Introduction | https://arxiv.org/html/2607.24759v1#Sx1.SSx10 — 6 Findings and discussion; https://arxiv.org/html/2607.24759v1#Sx1.SSx11 — 7 Limitations | Exact v1 links https://github.com/crcresearch/llm-wiki-memory-template, https://github.com/eugeniughelbur/obsidian-second-brain, https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-24759 | complete |
| SF-2026-ARXIV-2607-24762 | RP-008656cd5404dbd4 | deep | arXiv:2607.24762v1 | SRC-ARXIV@arXiv:2607.24762v1 | https://arxiv.org/html/2607.24762v1#S3 — 3 Kernel Forge System Design; https://arxiv.org/html/2607.24762v1#S4.SS1 — 4.1 Evaluation Methodology | https://arxiv.org/html/2607.24762v1#S4 — 4 Evaluation; https://arxiv.org/html/2607.24762v1#S4.SS1 — 4.1 Evaluation Methodology | https://arxiv.org/html/2607.24762v1#S6 — 6 Conclusion | Exact v1 links https://github.com/TheJoshBrod/KernelForge, https://github.com/meta-pytorch/BackendBench, https://github.com/meta-pytorch/KernelAgent; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-24762 | complete |
| SF-2026-ARXIV-2607-24763 | RP-504af897d8b491dc | deep | arXiv:2607.24763v1 | SRC-ARXIV@arXiv:2607.24763v1 | https://arxiv.org/html/2607.24763v1#A3.SS8 — C.8 LLaDA-MoE Cross-Architecture; https://arxiv.org/html/2607.24763v1#S2 — 2 The Ca re Framework and Protocol | https://arxiv.org/html/2607.24763v1#A3 — Appendix C Extended Experiments and Set Up; https://arxiv.org/html/2607.24763v1#A3.SS12 — C.12 Downstream Results (GSM8K) | https://arxiv.org/html/2607.24763v1#A1 — Appendix A Ethical consideration and Future Work; https://arxiv.org/html/2607.24763v1#S5 — 5 Conclusion | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-24763 | complete |
| SF-2026-ARXIV-2607-24765 | RP-716a59813283be81 | standard | arXiv:2607.24765v1 | SRC-ARXIV@arXiv:2607.24765v1 | https://arxiv.org/html/2607.24765v1#Sx1.SSx5 — 3. Architecture and Intervention: Cognitive Kernel Model; https://arxiv.org/html/2607.24765v1#Sx1.SSx7 — 5. Experimental Design | https://arxiv.org/html/2607.24765v1#Sx1.SSx7 — 5. Experimental Design; https://arxiv.org/html/2607.24765v1#Sx1.SSx8 — 6. Results | https://arxiv.org/html/2607.24765v1#Sx1.SSx10 — 8. Conclusion; https://arxiv.org/html/2607.24765v1#Sx1.SSx9 — 7. Discussion | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-24765 | complete |
| SF-2026-ARXIV-2607-24769 | RP-464ea0429abd4e70 | standard | arXiv:2607.24769v1 | SRC-ARXIV@arXiv:2607.24769v1 | https://arxiv.org/html/2607.24769v1#S3 — 3 Methodology | https://arxiv.org/html/2607.24769v1#S4 — 4 Experiments; https://arxiv.org/html/2607.24769v1#S5 — 5 Results | https://arxiv.org/html/2607.24769v1#S7 — 7 Limitations and Future Work; https://arxiv.org/html/2607.24769v1#S6 — 6 Discussion | Exact v1 links https://github.com/safety-research/petri, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-24769 | complete |
| SF-2026-ARXIV-2607-24771 | RP-7e4c2bc22e951250 | standard | arXiv:2607.24771v1 | SRC-ARXIV@arXiv:2607.24771v1 | https://arxiv.org/html/2607.24771v1#S3 — 3 Method; https://arxiv.org/html/2607.24771v1#A10 — Appendix J Model and Baseline Details | https://arxiv.org/html/2607.24771v1#A2 — Appendix B Full Baseline Comparison Results; https://arxiv.org/html/2607.24771v1#A3 — Appendix C Qualitative Analysis | https://arxiv.org/html/2607.24771v1#A7 — Appendix G Additional Discussion on Retention Scope and Reference Quality; https://arxiv.org/html/2607.24771v1#S5 — 5 Conclusion | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-24771 | complete |
| SF-2026-ARXIV-2607-24776 | RP-d3665840ac1a5e3a | standard | arXiv:2607.24776v1 | SRC-ARXIV@arXiv:2607.24776v1 | https://arxiv.org/html/2607.24776v1#S3 — 3 The JKO-RAG Framework | https://arxiv.org/html/2607.24776v1#S6 — 6 Experiments; https://arxiv.org/html/2607.24776v1#S6.SS2 — 6.2 Main retrieval results | https://arxiv.org/html/2607.24776v1#S8 — 8 Conclusion | Exact v1 links https://github.com/MurariAmbati/jko-rag, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-24776 | complete |
| SF-2026-ARXIV-2607-24780 | RP-bb55e00c78a5edf8 | deep | arXiv:2607.24780v1 | SRC-ARXIV@arXiv:2607.24780v1 | https://arxiv.org/html/2607.24780v1#S3 — 3 The LivingArena Framework | https://arxiv.org/html/2607.24780v1#S4 — 4 Experimental Setup; https://arxiv.org/html/2607.24780v1#S5 — 5 Results | https://arxiv.org/html/2607.24780v1#S6 — 6 Conclusion; https://arxiv.org/html/2607.24780v1#Sx1 — Limitations | Exact v1 links https://github.com/galaxyChen/LivingArena, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-24780 | complete |
| SF-2026-ARXIV-2607-24781 | RP-ff41d4d62cf9b4ee | standard | arXiv:2607.24781v1 | SRC-ARXIV@arXiv:2607.24781v1 | https://arxiv.org/pdf/2607.24781v1#page=1 — PDF page 1; https://arxiv.org/pdf/2607.24781v1#page=10 — PDF page 10 | https://arxiv.org/pdf/2607.24781v1#page=1 — PDF page 1; https://arxiv.org/pdf/2607.24781v1#page=10 — PDF page 10 | https://arxiv.org/pdf/2607.24781v1#page=1 — PDF page 1; https://arxiv.org/pdf/2607.24781v1#page=10 — PDF page 10 | Not Disclosed — exact v1 exposes no uniquely versioned artifact locator used to enlarge the manuscript claim boundary. | claim:SF-2026-ARXIV-2607-24781 | complete |
| SF-2026-ARXIV-2607-24787 | RP-7892271f489a720e | deep | arXiv:2607.24787v1 | SRC-ARXIV@arXiv:2607.24787v1 | https://arxiv.org/html/2607.24787v1#S3 — 3 Method; https://arxiv.org/html/2607.24787v1#S2.SS1 — 2.1 Sparse MoE Foundation Models | https://arxiv.org/html/2607.24787v1#S4 — 4 Experiment; https://arxiv.org/html/2607.24787v1#S4.SS1 — 4.1 Experimental Setup | https://arxiv.org/html/2607.24787v1#S5 — 5 Conclusion; https://arxiv.org/html/2607.24787v1#S7 — 7 Limitation | Exact v1 links https://github.com/wei390/SpecPrefetch, https://huggingface.co/datasets/facebook/textvqa, https://www.microsoft.com/en-us/research/project/figureqa-dataset/download/; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-24787 | complete |
| SF-2026-ARXIV-2607-24788 | RP-afc413f5a427f482 | deep | arXiv:2607.24788v1 | SRC-ARXIV@arXiv:2607.24788v1 | https://arxiv.org/html/2607.24788v1#S2.SS4 — II-D Parameter-Efficient Hybrid Architecture; https://arxiv.org/html/2607.24788v1#S3 — III Methodology | https://arxiv.org/html/2607.24788v1#S4 — IV Experiments; https://arxiv.org/html/2607.24788v1#S4.SS1 — IV-A Experimental Setup | https://arxiv.org/html/2607.24788v1#S5 — V Limitations & Future Works; https://arxiv.org/html/2607.24788v1#S4.SS2 — IV-B Results and Discussion | Exact v1 links https://github.com/tatsu-lab/stanford_alpaca, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-24788 | complete |
| SF-2026-ARXIV-2607-24794 | RP-dc5c2da043cf00a5 | standard | arXiv:2607.24794v1 | SRC-ARXIV@arXiv:2607.24794v1 | https://arxiv.org/html/2607.24794v1#S3 — 3 Method; https://arxiv.org/html/2607.24794v1#S2.SS1 — 2.1 Video Large Language Models | https://arxiv.org/html/2607.24794v1#S4 — 4 Experiments; https://arxiv.org/html/2607.24794v1#S4.SS1 — 4.1 Experimental Setup | https://arxiv.org/html/2607.24794v1#S4.SS7 — 4.7 Efficiency Analysis and Trade-off Discussion; https://arxiv.org/html/2607.24794v1#S5 — 5 Conclusion | Exact v1 links https://github.com/jinlab-imvr/ReMem, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-24794 | complete |
| SF-2026-ARXIV-2607-24798 | RP-98eac6380ffd221b | deep | arXiv:2607.24798v1 | SRC-ARXIV@arXiv:2607.24798v1 | https://arxiv.org/html/2607.24798v1#Sx1 — Introduction; https://arxiv.org/html/2607.24798v1#Sx2 — Related Work | https://arxiv.org/html/2607.24798v1#Sx5 — Experiments; https://arxiv.org/html/2607.24798v1#Sx5.SSx2 — Evaluation Questions | https://arxiv.org/html/2607.24798v1#Sx3.SSx3 — Near-Future Write-Risk Label; https://arxiv.org/html/2607.24798v1#Sx6 — Limitations and Claim Scope | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-24798 | complete |
| SF-2026-ARXIV-2607-24800 | RP-f4f63476ed2a647d | standard | arXiv:2607.24800v1 | SRC-ARXIV@arXiv:2607.24800v1 | https://arxiv.org/html/2607.24800v1#S3 — 3 TraceBound: Methodology and Implementation Details; https://arxiv.org/html/2607.24800v1#S3.SS5 — 3.5 Design invariants | https://arxiv.org/html/2607.24800v1#S4 — 4 Experimental Setup; https://arxiv.org/html/2607.24800v1#S5 — 5 Results | https://arxiv.org/html/2607.24800v1#S6 — 6 Discussion; https://arxiv.org/html/2607.24800v1#S6.SS4 — 6.4 Failure taxonomy and corrective policy targets | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-24800 | complete |
| SF-2026-ARXIV-2607-24805 | RP-b57591bd9e714393 | standard | arXiv:2607.24805v1 | SRC-ARXIV@arXiv:2607.24805v1 | https://arxiv.org/html/2607.24805v1#Sx1 — Abstract; https://arxiv.org/html/2607.24805v1#Sx2 — 1. Introduction | https://arxiv.org/html/2607.24805v1#Sx5 — 4. Results | https://arxiv.org/html/2607.24805v1#Sx8 — 7. Conclusion | Exact v1 links https://github.com/FerdinandSchessl/engram-seq-note-companion, https://github.com/jeakwon/ai-engram, https://github.com/arXiv/html_feedback/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-24805 | complete |
| SF-2026-ARXIV-2607-24821 | RP-24fc0e6e0e85d2fc | standard | arXiv:2607.24821v1 | SRC-ARXIV@arXiv:2607.24821v1 | https://arxiv.org/html/2607.24821v1#S3.SS2 — 3.2 Evaluation Methodology; https://arxiv.org/html/2607.24821v1#A2 — Appendix B Implementation Details of AVE-Agent | https://arxiv.org/html/2607.24821v1#S3 — 3 AVE-Compass: Benchmark and Evaluation; https://arxiv.org/html/2607.24821v1#A1 — Appendix A Benchmark Construction Details | https://arxiv.org/html/2607.24821v1#A5 — Appendix E Limitations; https://arxiv.org/html/2607.24821v1#S6 — 6 Conclusion | Exact v1 links https://github.com/NJU-LINK/AVE-Compass, https://huggingface.co/datasets/NJU-LINK/AVE-Compass, https://github.com/arXiv/html_feedback/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-24821 | complete |
| SF-2026-ARXIV-2607-24841 | RP-573bfe156d30982b | standard | arXiv:2607.24841v1 | SRC-ARXIV@arXiv:2607.24841v1 | https://arxiv.org/html/2607.24841v1#S3.SS1 — III-A Architecture; https://arxiv.org/html/2607.24841v1#S2.SS1 — II-A Autoregressive vs. Masked Diffusion Language Models | https://arxiv.org/html/2607.24841v1#S4 — IV Performance Analysis; https://arxiv.org/html/2607.24841v1#S5 — V Experiments | https://arxiv.org/html/2607.24841v1#S6 — VI Conclusions | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-24841 | complete |
| SF-2026-ARXIV-2607-24850 | RP-a3e1fa4b7cee8058 | standard | arXiv:2607.24850v1 | SRC-ARXIV@arXiv:2607.24850v1 | https://arxiv.org/html/2607.24850v1#S3.SS4 — 3.4 Composite Reward Design; https://arxiv.org/html/2607.24850v1#S4 — 4 SearchArt Harness Design | https://arxiv.org/html/2607.24850v1#S5.SS2 — 5.2 Experimental Results; https://arxiv.org/html/2607.24850v1#S5 — 5 Experiments | https://arxiv.org/html/2607.24850v1#S7 — 7 Conclusion; https://arxiv.org/html/2607.24850v1#S8 — 8 Future Work | Exact v1 links https://huggingface.co/MiniMaxAI/MiniMax-M2.5, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-24850 | complete |
| SF-2026-ARXIV-2607-24859 | RP-4bcf5795b0510e5a | standard | arXiv:2607.24859v1 | SRC-ARXIV@arXiv:2607.24859v1 | https://arxiv.org/html/2607.24859v1#Sx3 — Methodology | https://arxiv.org/html/2607.24859v1#Sx4 — Experimental Results; https://arxiv.org/html/2607.24859v1#Sx4.SSx1 — Experimental Setup | https://arxiv.org/html/2607.24859v1#Sx5 — Discussion and Conclusion; https://arxiv.org/html/2607.24859v1#Sx6 — Limitations and Future Work | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-24859 | complete |
| SF-2026-ARXIV-2607-24866 | RP-31ec43f5cc522d0f | deep | arXiv:2607.24866v1 | SRC-ARXIV@arXiv:2607.24866v1 | https://arxiv.org/html/2607.24866v1#S7 — 7 Reference Architecture for Layer 2 Systems; https://arxiv.org/html/2607.24866v1#S5 — 5 Six Design Principles for Layer 2 Infrastructure | https://arxiv.org/html/2607.24866v1#S1 — 1 Introduction; https://arxiv.org/html/2607.24866v1#S2 — 2 Related Work | https://arxiv.org/html/2607.24866v1#S10 — 10 Discussion and Limitations; https://arxiv.org/html/2607.24866v1#S11 — 11 Conclusion | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-24866 | complete |
| SF-2026-ARXIV-2607-24875 | RP-022d38b4843aa4c9 | standard | arXiv:2607.24875v1 | SRC-ARXIV@arXiv:2607.24875v1 | https://arxiv.org/html/2607.24875v1#S4 — IV Proposed FinAbstain Framework; https://arxiv.org/html/2607.24875v1#S5 — V Experimental Methodology | https://arxiv.org/html/2607.24875v1#S5 — V Experimental Methodology; https://arxiv.org/html/2607.24875v1#S6 — VI Results and Discussion | https://arxiv.org/html/2607.24875v1#S6 — VI Results and Discussion; https://arxiv.org/html/2607.24875v1#S6.SS3 — VI-C Limitations and Reproducibility Risks | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-24875 | complete |
| SF-2026-ARXIV-2607-24882 | RP-d7ec249d68f48d32 | deep | arXiv:2607.24882v1 | SRC-ARXIV@arXiv:2607.24882v1 | https://arxiv.org/html/2607.24882v1#A3 — Appendix C Embedding Baseline Implementation | https://arxiv.org/html/2607.24882v1#A4 — Appendix D Full edit2ripple Results; https://arxiv.org/html/2607.24882v1#S10 — 10 Candidate Filter Ablation | https://arxiv.org/html/2607.24882v1#S11 — 11 Limitations; https://arxiv.org/html/2607.24882v1#S12 — 12 Future Work | Exact v1 links https://github.com/clap-rs/clap/pull/6319, https://github.com/tokio-rs/tokio/pull/7686, https://github.com/gin-gonic/gin/pull/4404; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-24882 | complete |
| SF-2026-ARXIV-2607-24884 | RP-4ec17c9a757e8714 | standard | arXiv:2607.24884v1 | SRC-ARXIV@arXiv:2607.24884v1 | https://arxiv.org/html/2607.24884v1#Sx2.SSx2 — Uncertainty-Aware Framework | https://arxiv.org/html/2607.24884v1#Sx3 — Experimental Setup; https://arxiv.org/html/2607.24884v1#Sx4 — Results | https://arxiv.org/html/2607.24884v1#Sx6 — Limitations and Ethical Considerations; https://arxiv.org/html/2607.24884v1#Sx7 — Conclusion | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-24884 | complete |
| SF-2026-ARXIV-2607-24887 | RP-098b04f4ca101753 | standard | arXiv:2607.24887v1 | SRC-ARXIV@arXiv:2607.24887v1 | https://arxiv.org/html/2607.24887v1#A1 — Appendix A Model Architecture and Pretraining Details; https://arxiv.org/html/2607.24887v1#A1.SSx1 — Model Architecture | https://arxiv.org/html/2607.24887v1#A2.SSx5 — ResNet-20 Experimental Configuration and Accuracy; https://arxiv.org/html/2607.24887v1#Sx4 — Main Results | https://arxiv.org/html/2607.24887v1#Sx6 — Conclusion | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-24887 | complete |
| SF-2026-ARXIV-2607-24889 | RP-0324b6ee6372e68c | standard | arXiv:2607.24889v1 | SRC-ARXIV@arXiv:2607.24889v1 | https://arxiv.org/html/2607.24889v1#A22 — Appendix V Release Protocol and Benchmark-Design Checklist; https://arxiv.org/html/2607.24889v1#A4.SS1 — D.1. System Prompt (Complete, Verbatim) | https://arxiv.org/html/2607.24889v1#A12 — Appendix L Per-Facet Results: The Full Matrix; https://arxiv.org/html/2607.24889v1#A13 — Appendix M Results by Slice: Sector, Tier, and Completion Re-Cuts | https://arxiv.org/html/2607.24889v1#A14.SS3 — N.3. Failure-Aware Panel Uncertainty; https://arxiv.org/html/2607.24889v1#A19 — Appendix S Three Failure Trajectories, Verbatim | Exact v1 links https://qwenlm.github.io/blog/qwen3-coder/, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-24889 | complete |
| SF-2026-ARXIV-2607-24893 | RP-746bdf762fc227bf | deep | arXiv:2607.24893v1 | SRC-ARXIV@arXiv:2607.24893v1 | https://arxiv.org/html/2607.24893v1#S3 — 3. Threat Model, Attack, and Corpus | https://arxiv.org/html/2607.24893v1#S4 — 4. Experimental Setup; https://arxiv.org/html/2607.24893v1#S5 — 5. Results | https://arxiv.org/html/2607.24893v1#S3 — 3. Threat Model, Attack, and Corpus; https://arxiv.org/html/2607.24893v1#S6 — 6. Discussion | Exact v1 links https://github.com/yibo-hu-lab/distributed-backdoor-early-warning, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-24893 | complete |
| SF-2026-ARXIV-2607-24897 | RP-2167bd25ea1941b6 | standard | arXiv:2607.24897v1 | SRC-ARXIV@arXiv:2607.24897v1 | https://arxiv.org/html/2607.24897v1#S4 — 4 Methodology; https://arxiv.org/html/2607.24897v1#S2.SS1 — 2.1 Image-Generation Models | https://arxiv.org/html/2607.24897v1#S5 — 5 Experiments; https://arxiv.org/html/2607.24897v1#S5.SS1 — 5.1 Experimental Settings | https://arxiv.org/html/2607.24897v1#S6 — 6 Conclusion, Limitations, and Future Work; https://arxiv.org/html/2607.24897v1#S3.SS2 — 3.2 Threat Model | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-24897 | complete |
| SF-2026-ARXIV-2607-24900 | RP-f152e58d54c58dd8 | standard | arXiv:2607.24900v1 | SRC-ARXIV@arXiv:2607.24900v1 | https://arxiv.org/html/2607.24900v1#S1 — 1 Introduction; https://arxiv.org/html/2607.24900v1#S2 — 2 PARED: Projected Alignment Reward Estimated from Demonstrations | https://arxiv.org/html/2607.24900v1#A2 — Appendix B Additional Experimental Details, Diagnostics, and Ablations; https://arxiv.org/html/2607.24900v1#A2.SS5 — B.5 Feature-Set Ablations | https://arxiv.org/html/2607.24900v1#S5 — 5 Discussion and Limitations | Exact v1 links https://github.com/huggingface/trl, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-24900 | complete |
| SF-2026-ARXIV-2607-24904 | RP-e61e4adcdc37250f | standard | arXiv:2607.24904v1 | SRC-ARXIV@arXiv:2607.24904v1 | https://arxiv.org/html/2607.24904v1#A1 — Appendix A Recaptioning System Prompt; https://arxiv.org/html/2607.24904v1#S3.SS1 — Architecture | https://arxiv.org/html/2607.24904v1#S5 — Experiments; https://arxiv.org/html/2607.24904v1#S5.SS1 — Experimental Setup | https://arxiv.org/html/2607.24904v1#S7 — Conclusion and Limitations; https://arxiv.org/html/2607.24904v1#S6 — Discussions | Exact v1 links https://github.com/microsoft/Mage, https://huggingface.co/collections/microsoft/mage, https://github.com/kakaobrain/coyo-dataset; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-24904 | complete |
| SF-2026-ARXIV-2607-24953 | RP-b032ab952cc773ae | deep | arXiv:2607.24953v1 | SRC-ARXIV@arXiv:2607.24953v1 | https://arxiv.org/html/2607.24953v1#S1 — 1 Introduction; https://arxiv.org/html/2607.24953v1#S2 — 2 Motivation for Microscaling | https://arxiv.org/html/2607.24953v1#A6 — Appendix F Evaluation Protocol; https://arxiv.org/html/2607.24953v1#A7 — Appendix G Ablation Interpretation | https://arxiv.org/html/2607.24953v1#S5 — 5 Discussion and Limitations; https://arxiv.org/html/2607.24953v1#S6 — 6 Conclusion | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-24953 | complete |
| SF-2026-ARXIV-2607-24957 | RP-67036fdd829e3d33 | standard | arXiv:2607.24957v1 | SRC-ARXIV@arXiv:2607.24957v1 | https://arxiv.org/html/2607.24957v1#S1 — 1 Introduction; https://arxiv.org/html/2607.24957v1#S2 — 2 PerceptionBench | https://arxiv.org/html/2607.24957v1#S3 — 3 Evaluation Results; https://arxiv.org/html/2607.24957v1#A3 — Appendix C Source Benchmark List and License | https://arxiv.org/html/2607.24957v1#S5 — 5 Conclusion; https://arxiv.org/html/2607.24957v1#Sx1 — Limitations | Exact v1 links https://github.com/MoonshotAI/PerceptionBench, https://huggingface.co/datasets/xai-org/RealworldQA, https://github.com/arXiv/html_feedback/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-24957 | complete |
| SF-2026-ARXIV-2607-24964 | RP-ff00ee59902caac0 | standard | arXiv:2607.24964v1 | SRC-ARXIV@arXiv:2607.24964v1 | https://arxiv.org/html/2607.24964v1#S3 — 3 Threat Model & Attack Framework; https://arxiv.org/html/2607.24964v1#S3.SS2 — 3.2 Attack Framework | https://arxiv.org/html/2607.24964v1#S4 — 4 Experimental Results; https://arxiv.org/html/2607.24964v1#S4.SS1 — 4.1 Evaluation Setup | https://arxiv.org/html/2607.24964v1#S3 — 3 Threat Model & Attack Framework; https://arxiv.org/html/2607.24964v1#S3.SS1 — 3.1 Threat Model | Exact v1 links https://codeql.github.com/, https://docs.github.com/en/code-security/code-scanning, https://docs.github.com/en/enterprise-cloud/latest/code-security/concepts/code-scanning/ai-powered-security-detections; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-24964 | complete |
| SF-2026-ARXIV-2607-24981 | RP-0a9f9ef992f29137 | standard | arXiv:2607.24981v1 | SRC-ARXIV@arXiv:2607.24981v1 | https://arxiv.org/html/2607.24981v1#A1 — Appendix A Pseudo-code of the proposed methods; https://arxiv.org/html/2607.24981v1#S3 — 3 Methodology | https://arxiv.org/html/2607.24981v1#S4 — 4 Experimental Setup; https://arxiv.org/html/2607.24981v1#S4.SS1 — 4.1 Datasets and Evaluation Metrics | https://arxiv.org/html/2607.24981v1#S7 — 7 Discussion: Hardware Compatibility; https://arxiv.org/html/2607.24981v1#S8 — 8 Conclusions | Exact v1 links https://github.com/ltc286648/I-LW-DETR, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-24981 | complete |
| SF-2026-ARXIV-2607-24996 | RP-d596ed934f8c1909 | standard | arXiv:2607.24996v1 | SRC-ARXIV@arXiv:2607.24996v1 | https://arxiv.org/html/2607.24996v1#A1 — Appendix A CPR Algorithm; https://arxiv.org/html/2607.24996v1#A8 — Appendix H Implementation Details | https://arxiv.org/html/2607.24996v1#A3.SS1 — C.1 Analysis of Results; https://arxiv.org/html/2607.24996v1#A3 — Appendix C Experiments in Standard RL | https://arxiv.org/html/2607.24996v1#S5 — 5 Discussion | Exact v1 links http://github.com/jax-ml/jax, http://github.com/google-deepmind, https://github.com/arXiv/html_feedback/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-24996 | complete |
| SF-2026-ARXIV-2607-25018 | RP-f9a556a137badbca | deep | arXiv:2607.25018v1 | SRC-ARXIV@arXiv:2607.25018v1 | https://arxiv.org/html/2607.25018v1#A1 — Appendix A C3PO Design Contrast; https://arxiv.org/html/2607.25018v1#S3 — 3 Method | https://arxiv.org/html/2607.25018v1#A12.SS4 — L.4 Proof of Theorem 4 and Cost Results; https://arxiv.org/html/2607.25018v1#A2 — Appendix B Model and Benchmark Details | https://arxiv.org/html/2607.25018v1#A8 — Appendix H Failure Diagnostics: Phi’s Under-Performance; https://arxiv.org/html/2607.25018v1#S6 — 6 Discussion | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-25018 | complete |
| SF-2026-ARXIV-2607-25019 | RP-bbce4dfb4f4b1da5 | standard | arXiv:2607.25019v1 | SRC-ARXIV@arXiv:2607.25019v1 | https://arxiv.org/html/2607.25019v1#S1 — 1 Introduction; https://arxiv.org/html/2607.25019v1#S2 — 2 The Farming Game | https://arxiv.org/html/2607.25019v1#S3.SS4 — 3.4 Experimental evaluation; https://arxiv.org/html/2607.25019v1#S4.SS4 — 4.4 Experimental evaluation | https://arxiv.org/html/2607.25019v1#S5 — 5 Discussion | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-25019 | complete |
| SF-2026-ARXIV-2607-25032 | RP-11acc6b3a703c054 | standard | arXiv:2607.25032v1 | SRC-ARXIV@arXiv:2607.25032v1 | https://arxiv.org/html/2607.25032v1#Sx1 — Note on sources; https://arxiv.org/html/2607.25032v1#S1 — 1 Introduction | https://arxiv.org/html/2607.25032v1#S9 — 9 An evaluation-driven authoring process | https://arxiv.org/html/2607.25032v1#Sx1 — Note on sources; https://arxiv.org/html/2607.25032v1#S1 — 1 Introduction | Exact v1 links https://code.claude.com/docs/en/hooks, https://code.claude.com/docs/en/skills, https://github.com/arXiv/html_feedback/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-25032 | complete |
| SF-2026-ARXIV-2607-25063 | RP-94e8c43eb22c3a68 | deep | arXiv:2607.25063v1 | SRC-ARXIV@arXiv:2607.25063v1 | https://arxiv.org/html/2607.25063v1#S3 — 3 Methodology; https://arxiv.org/html/2607.25063v1#S4.SS5 — 4.5 The Divergence Survives Recipe and Model | https://arxiv.org/html/2607.25063v1#S4 — 4 Experiments | https://arxiv.org/html/2607.25063v1#A11 — Appendix K Limitations and Future Work; https://arxiv.org/html/2607.25063v1#S5 — 5 Conclusion | Exact v1 links https://huggingface.co/datasets/HuggingFaceTB/cosmopedia, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-25063 | complete |
| SF-2026-ARXIV-2607-25066 | RP-f6ca31d99e9d59ac | standard | arXiv:2607.25066v1 | SRC-ARXIV@arXiv:2607.25066v1 | https://arxiv.org/html/2607.25066v1#Sx4 — Proposed Method; https://arxiv.org/html/2607.25066v1#Sx4.SSx1 — Design Principle | https://arxiv.org/html/2607.25066v1#A2 — Appendix B Ablation; https://arxiv.org/html/2607.25066v1#A2.SSx3 — HBM (High-Bandwidth Memory) Bandwidth Analysis | https://arxiv.org/html/2607.25066v1#Sx7 — Discussion and Limitations; https://arxiv.org/html/2607.25066v1#Sx8 — Conclusion | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-25066 | complete |
| SF-2026-ARXIV-2607-25076 | RP-4a180a9e00586b44 | deep | arXiv:2607.25076v1 | SRC-ARXIV@arXiv:2607.25076v1 | https://arxiv.org/html/2607.25076v1#S3.SS1 — III-A Where OS and Cloud-OS Semantics Break Down; https://arxiv.org/html/2607.25076v1#S4 — IV Proposed Agent-OS Primitives | https://arxiv.org/html/2607.25076v1#S5 — V Open source prototypes of Agent-OS primitives | https://arxiv.org/html/2607.25076v1#S6 — VI Discussion: What the Prior Waves Teach Us; https://arxiv.org/html/2607.25076v1#S7 — VII Open Research Agenda | Exact v1 links https://github.com/rossoctl/rossoctl, https://github.com/spiffe/spire/issues/6640, https://www.coderabbit.ai/blog/state-of-ai-vs-human-code-generation-report; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-25076 | complete |
| SF-2026-ARXIV-2607-25082 | RP-1140fc3605e1d8e3 | standard | arXiv:2607.25082v1 | SRC-ARXIV@arXiv:2607.25082v1 | https://arxiv.org/html/2607.25082v1#S2.SS1 — 2.1 Open Agent Systems (OASYS); https://arxiv.org/html/2607.25082v1#S4 — 4 Methodology | https://arxiv.org/html/2607.25082v1#A3.SS8 — C.8 Ablation Studies: Detailed Results; https://arxiv.org/html/2607.25082v1#A3 — Appendix C Additional Results | https://arxiv.org/html/2607.25082v1#S8 — 8 Conclusion | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-25082 | complete |
| SF-2026-ARXIV-2607-25090 | RP-32ae617b51cae43c | standard | arXiv:2607.25090v1 | SRC-ARXIV@arXiv:2607.25090v1 | https://arxiv.org/html/2607.25090v1#A2 — Appendix B Agent and Environment Design; https://arxiv.org/html/2607.25090v1#S3 — 3 Method | https://arxiv.org/html/2607.25090v1#A1 — Appendix A Benchmark and Metric Details; https://arxiv.org/html/2607.25090v1#A4 — Appendix D Mean and Variance of Evaluation | https://arxiv.org/html/2607.25090v1#A5 — Appendix E Failure Analysis of Qwen3-4B; https://arxiv.org/html/2607.25090v1#S5 — 5 Conclusion | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-25090 | complete |
| SF-2026-ARXIV-2607-25091 | RP-fe651746bb682350 | standard | arXiv:2607.25091v1 | SRC-ARXIV@arXiv:2607.25091v1 | https://arxiv.org/html/2607.25091v1#S3 — III Methodology; https://arxiv.org/html/2607.25091v1#S3.SS3 — III-C Stage 2: Reward Model Training | https://arxiv.org/html/2607.25091v1#S5 — V Results Analysis; https://arxiv.org/html/2607.25091v1#S4 — IV Experimental Setup | https://arxiv.org/html/2607.25091v1#S6 — VI Discussion; https://arxiv.org/html/2607.25091v1#S7 — VII Conclusion | Exact v1 links https://github.com/huggingface/trl, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-25091 | complete |
| SF-2026-ARXIV-2607-25135 | RP-639c9e317540cf86 | standard | arXiv:2607.25135v1 | SRC-ARXIV@arXiv:2607.25135v1 | https://arxiv.org/html/2607.25135v1#A1 — Appendix A System Prompt; https://arxiv.org/html/2607.25135v1#S3 — 3 Proposed Method | https://arxiv.org/html/2607.25135v1#A3.SS3 — C.3 Zero-Result Diagnostics and Recovery: 2WikiMultiHopQA; https://arxiv.org/html/2607.25135v1#S4 — 4 Experiments | https://arxiv.org/html/2607.25135v1#S5 — 5 Conclusion; https://arxiv.org/html/2607.25135v1#S6 — 6 Limitations | Exact v1 links https://github.com/cohesity/ScalableRAG, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-25135 | complete |
| SF-2026-ARXIV-2607-25136 | RP-cfb78b574d14dc34 | standard | arXiv:2607.25136v1 | SRC-ARXIV@arXiv:2607.25136v1 | https://arxiv.org/html/2607.25136v1#S3 — 3 Method; https://arxiv.org/html/2607.25136v1#S4.SS1 — 4.1 Models | https://arxiv.org/html/2607.25136v1#A1 — Appendix A Full experimental setup; https://arxiv.org/html/2607.25136v1#A2 — Appendix B AlpacaEval-style detailed results | https://arxiv.org/html/2607.25136v1#S7 — 7 Limitations; https://arxiv.org/html/2607.25136v1#S9 — 9 Conclusion | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-25136 | complete |
| SF-2026-ARXIV-2607-25151 | RP-25405e98ccf5bddc | standard | arXiv:2607.25151v1 | SRC-ARXIV@arXiv:2607.25151v1 | https://arxiv.org/html/2607.25151v1#S1 — 1. Introduction; https://arxiv.org/html/2607.25151v1#S2 — 2. Related Work | https://arxiv.org/html/2607.25151v1#S4 — 4. Results and Analysis; https://arxiv.org/html/2607.25151v1#A1.SS2 — A.2. Benchmark novelty and comparison with prior work | https://arxiv.org/html/2607.25151v1#S5 — 5. Conclusion | Exact v1 links https://huggingface.co/datasets/BiXie/wikiimage, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-25151 | complete |
| SF-2026-ARXIV-2607-25152 | RP-6263da3158a9109a | deep | arXiv:2607.25152v1 | SRC-ARXIV@arXiv:2607.25152v1 | https://arxiv.org/pdf/2607.25152v1#page=2 — Out-of-band evaluator architecture; https://arxiv.org/pdf/2607.25152v1#page=5 — Controlled evaluator-channel design | https://arxiv.org/pdf/2607.25152v1#page=10 — Measured progress-mirage results; https://arxiv.org/pdf/2607.25152v1#page=13 — Boundary-task comparison | https://arxiv.org/pdf/2607.25152v1#page=1 — Preliminary-draft scope; https://arxiv.org/pdf/2607.25152v1#page=19 — Generalization and field-observation limits | Not Disclosed — exact v1 exposes no uniquely versioned artifact locator used to enlarge the manuscript claim boundary. | claim:SF-2026-ARXIV-2607-25152 | complete |
| SF-2026-ARXIV-2607-25157 | RP-f1ad890f1daeaad4 | standard | arXiv:2607.25157v1 | SRC-ARXIV@arXiv:2607.25157v1 | https://arxiv.org/html/2607.25157v1#S3 — 3 Method | https://arxiv.org/html/2607.25157v1#A1 — Appendix A Evaluation Protocol and Human Audit; https://arxiv.org/html/2607.25157v1#S4 — 4 Experiments | https://arxiv.org/html/2607.25157v1#S5 — 5 Limitations; https://arxiv.org/html/2607.25157v1#S6 — 6 Conclusion | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-25157 | complete |
| SF-2026-ARXIV-2607-25196 | RP-acb7c7417289288d | standard | arXiv:2607.25196v1 | SRC-ARXIV@arXiv:2607.25196v1 | https://arxiv.org/html/2607.25196v1#S4 — 4 Methodology; https://arxiv.org/html/2607.25196v1#S4.SS2 — 4.2 Baseline Contrastive Methods | https://arxiv.org/html/2607.25196v1#A1.SS3 — A.3 Balanced Accuracy evaluation metric used for Dataset Label Imbalance Analysis; https://arxiv.org/html/2607.25196v1#S5 — 5 Results and Analysis | https://arxiv.org/html/2607.25196v1#S8.SS3 — 8.3 Limitations and Future Works; https://arxiv.org/html/2607.25196v1#S8 — 8 Discussion | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-25196 | complete |
| SF-2026-ARXIV-2607-25225 | RP-591fbfa5cb715875 | standard | arXiv:2607.25225v1 | SRC-ARXIV@arXiv:2607.25225v1 | https://arxiv.org/html/2607.25225v1#S4 — 4. Methodology; https://arxiv.org/html/2607.25225v1#A3 — Appendix C Complete Model-Sector Matrix | https://arxiv.org/html/2607.25225v1#S5 — 5. Experimental Setup; https://arxiv.org/html/2607.25225v1#S6 — 6. Results | https://arxiv.org/html/2607.25225v1#S3 — 3. Threat Model and Problem Formulation; https://arxiv.org/html/2607.25225v1#S7 — 7. Discussion | Exact v1 links https://github.com/widdendream/secdrift_revised, https://github.com/features/copilot, https://github.com/arXiv/html_feedback/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-25225 | complete |
| SF-2026-ARXIV-2607-25227 | RP-341b2d46ab738ced | standard | arXiv:2607.25227v1 | SRC-ARXIV@arXiv:2607.25227v1 | https://arxiv.org/html/2607.25227v1#A5.SS3 — E.3. Baseline Methods and Evaluation Metrics; https://arxiv.org/html/2607.25227v1#S4 — 4. Methodology | https://arxiv.org/html/2607.25227v1#S5 — 5. Experimental Evaluation; https://arxiv.org/html/2607.25227v1#A5.SS2 — E.2. Experimental Environment and Generation Randomness Control | https://arxiv.org/html/2607.25227v1#S6 — 6. Conclusion and Discussion; https://arxiv.org/html/2607.25227v1#S3 — 3. Threat Model | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-25227 | complete |
| SF-2026-ARXIV-2607-25236 | RP-09315e4b4d094e71 | standard | arXiv:2607.25236v1 | SRC-ARXIV@arXiv:2607.25236v1 | https://arxiv.org/html/2607.25236v1#S4 — 4. Method; https://arxiv.org/html/2607.25236v1#A1 — Appendix A Pipeline Algorithms | https://arxiv.org/html/2607.25236v1#A3 — Appendix C Induction and Perception Analysis; https://arxiv.org/html/2607.25236v1#A5.SS5 — E.5. Reacher: frame MPC multi-seed results | https://arxiv.org/html/2607.25236v1#A4 — Appendix D Baseline Ports and Failure Modes; https://arxiv.org/html/2607.25236v1#A4.SS1 — D.1. Baseline failure case studies | Exact v1 links https://github.com/HKBU-KnowComp/VisualPatchWorld/, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-25236 | complete |
| SF-2026-ARXIV-2607-25255 | RP-1f5808cc297ecfaa | deep | arXiv:2607.25255v1 | SRC-ARXIV@arXiv:2607.25255v1 | https://arxiv.org/html/2607.25255v1#S3 — 3 Methodology; https://arxiv.org/html/2607.25255v1#S4 — 4 SafeFlow Architecture | https://arxiv.org/html/2607.25255v1#S5.SS5 — 5.5 Ablation and Sensitivity Analysis; https://arxiv.org/html/2607.25255v1#A2.SS2 — B.2 Reproducibility and Evaluation Notes | https://arxiv.org/html/2607.25255v1#S6 — 6 Conclusion | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-25255 | complete |
| SF-2026-ARXIV-2607-25257 | RP-8c3c0384d385860d | standard | arXiv:2607.25257v1 | SRC-ARXIV@arXiv:2607.25257v1 | https://arxiv.org/html/2607.25257v1#S3 — 3 Method: Last-Layer Laplace Approximation; https://arxiv.org/html/2607.25257v1#S5.SS1 — 5.1 Pairwise model ability comparisons | https://arxiv.org/html/2607.25257v1#S4 — 4 Experimental Setup; https://arxiv.org/html/2607.25257v1#S5 — 5 Results | https://arxiv.org/html/2607.25257v1#S6 — 6 Limitations; https://arxiv.org/html/2607.25257v1#S8 — 8 Conclusion | Exact v1 links https://github.com/JFMandujanoR/Laplace-PSN-IRT/tree/jfmr_laplace, https://github.com/Joe-Hall-Lee/PSN-IRT, https://github.com/arXiv/html_feedback/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-25257 | complete |
| SF-2026-ARXIV-2607-25271 | RP-ea3d9892aebf7552 | standard | arXiv:2607.25271v1 | SRC-ARXIV@arXiv:2607.25271v1 | https://arxiv.org/html/2607.25271v1#S3 — 3 Methodology and Experiment Setup; https://arxiv.org/html/2607.25271v1#A1 — Appendix A Implementation Details and Ablations for the CD-Scaling Fit | https://arxiv.org/html/2607.25271v1#A2 — Appendix B Additional Experiment Details and Results; https://arxiv.org/html/2607.25271v1#A1 — Appendix A Implementation Details and Ablations for the CD-Scaling Fit | https://arxiv.org/html/2607.25271v1#S6 — 6 Conclusion & Discussion | Exact v1 links https://huggingface.co/datasets/allenai/dolma3_mix-150B-1025, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-25271 | complete |
| SF-2026-ARXIV-2607-25291 | RP-b9bffc1024bb9356 | deep | arXiv:2607.25291v1 | SRC-ARXIV@arXiv:2607.25291v1 | https://arxiv.org/html/2607.25291v1#A3 — Appendix C Additional Method Details; https://arxiv.org/html/2607.25291v1#S4.SS2 — 4.2 Kernel-Aware Proxy Design | https://arxiv.org/html/2607.25291v1#A4 — Appendix D Experimental Details and Additional Results; https://arxiv.org/html/2607.25291v1#A4.SS1 — D.1 Experimental Configurations | https://arxiv.org/html/2607.25291v1#S6 — 6 Conclusion | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-25291 | complete |
| SF-2026-ARXIV-2607-25292 | RP-24538efebff70718 | standard | arXiv:2607.25292v1 | SRC-ARXIV@arXiv:2607.25292v1 | https://arxiv.org/html/2607.25292v1#S5.SS1 — 5.1 Method; https://arxiv.org/html/2607.25292v1#S3.SS5 — 3.5 The model can describe what it cannot sample | https://arxiv.org/html/2607.25292v1#A1 — Appendix A Experimental setup; https://arxiv.org/html/2607.25292v1#A10 — Appendix J CoT-RNG bridge analysis | https://arxiv.org/html/2607.25292v1#S3 — 3 Characterizing the Per-Call Sampling Failure; https://arxiv.org/html/2607.25292v1#S3.SS2 — 3.2 The failure is categorical | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-25292 | complete |
| SF-2026-ARXIV-2607-25294 | RP-95bad009b633ff87 | standard | arXiv:2607.25294v1 | SRC-ARXIV@arXiv:2607.25294v1 | https://arxiv.org/html/2607.25294v1#S3 — 3 CLBench-V: Task and Benchmark Design | https://arxiv.org/html/2607.25294v1#S3 — 3 CLBench-V: Task and Benchmark Design; https://arxiv.org/html/2607.25294v1#S3.SS3 — 3.3 Benchmark Construction | https://arxiv.org/html/2607.25294v1#A3.SS1 — C.1 Failure Taxonomy Case Studies; https://arxiv.org/html/2607.25294v1#S6.SS2 — 6.2 Failure Taxonomy | Exact v1 links https://github.com/IamLihua/CLBench-V, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-25294 | complete |
| SF-2026-ARXIV-2607-25297 | RP-acadafd5888c2584 | deep | arXiv:2607.25297v1 | SRC-ARXIV@arXiv:2607.25297v1 | https://arxiv.org/html/2607.25297v1#A1 — Appendix A Framework algorithm; https://arxiv.org/html/2607.25297v1#S3 — 3. Methodology | https://arxiv.org/html/2607.25297v1#S3.SS4 — 3.4. Post-execution result verifier; https://arxiv.org/html/2607.25297v1#S4 — 4. Experiments | https://arxiv.org/html/2607.25297v1#S5.SS1 — 5.1. Limitations & Future work; https://arxiv.org/html/2607.25297v1#S5 — 5. Discussion | Exact v1 links https://github.com/antgroup/Trustworthy_LM/mcp-scan, https://github.com/Tencent/AI-Infra-Guard, https://github.com/arXiv/html_feedback/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-25297 | complete |
| SF-2026-ARXIV-2607-25333 | RP-d4136cdc135b303f | standard | arXiv:2607.25333v1 | SRC-ARXIV@arXiv:2607.25333v1 | https://arxiv.org/html/2607.25333v1#S3 — 3. Specula Design; https://arxiv.org/html/2607.25333v1#S3.SS2 — 3.2. Generating effective system models | https://arxiv.org/html/2607.25333v1#S5 — 5. Evaluation | https://arxiv.org/html/2607.25333v1#S6 — 6. Discussion | Exact v1 links https://github.com/specula-org/Specula, https://github.com/aptos-labs/aptos-core, https://github.com/vorner/arc-swap; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-25333 | complete |
| SF-2026-ARXIV-2607-25335 | RP-ad14c6968d3a63fa | standard | arXiv:2607.25335v1 | SRC-ARXIV@arXiv:2607.25335v1 | https://arxiv.org/html/2607.25335v1#A1.SS1 — A.1 Evolutionary Search Design; https://arxiv.org/html/2607.25335v1#A2.SS1 — B.1 Design Principles | https://arxiv.org/html/2607.25335v1#S5 — 5 Results and Analysis; https://arxiv.org/html/2607.25335v1#A12 — Appendix L Experimental Prompts | https://arxiv.org/html/2607.25335v1#S6 — 6 Conclusion; https://arxiv.org/html/2607.25335v1#Sx1 — Limitations | Exact v1 links https://github.com/algorithmicsuperintelligence/openevolve, https://github.com/chatde/tokenshrink, https://github.com/arXiv/html_feedback/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-25335 | complete |
| SF-2026-ARXIV-2607-25337 | RP-2bb3d68da211b889 | deep | arXiv:2607.25337v1 | SRC-ARXIV@arXiv:2607.25337v1 | https://arxiv.org/html/2607.25337v1#S3 — 3. Method | https://arxiv.org/html/2607.25337v1#A1 — Appendix A Detailed Plan-Cost Results; https://arxiv.org/html/2607.25337v1#A3 — Appendix C Training and Evaluation Protocol | https://arxiv.org/html/2607.25337v1#S5 — 5. Conclusion | Exact v1 links https://github.com/HKBU-KnowComp/TD-JEPA, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-25337 | complete |
| SF-2026-ARXIV-2607-25346 | RP-1041e7bd872d47cf | standard | arXiv:2607.25346v1 | SRC-ARXIV@arXiv:2607.25346v1 | https://arxiv.org/html/2607.25346v1#S5 — 5 System Architecture; https://arxiv.org/html/2607.25346v1#A7.SS1 — G.1 LLM-based Recommender Systems | https://arxiv.org/html/2607.25346v1#A5 — Appendix E Full Two-Tower Ablation; https://arxiv.org/html/2607.25346v1#S6 — 6 Experiments on Public Datasets | https://arxiv.org/html/2607.25346v1#S4.SS3 — 4.3 Efficiency Discussion; https://arxiv.org/html/2607.25346v1#S8 — 8 Conclusion | Exact v1 links https://huggingface.co/Qwen/Qwen3-0.6B, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-25346 | complete |
| SF-2026-ARXIV-2607-25356 | RP-a5ecea7483acda12 | standard | arXiv:2607.25356v1 | SRC-ARXIV@arXiv:2607.25356v1 | https://arxiv.org/html/2607.25356v1#S2 — 2 Sampling Methods; https://arxiv.org/html/2607.25356v1#S2.SS4 — 2.4 Method Comparison | https://arxiv.org/html/2607.25356v1#S3 — 3 Experiments; https://arxiv.org/html/2607.25356v1#S3.SS1 — 3.1 Experimental Setup | https://arxiv.org/html/2607.25356v1#S4 — 4 Discussion; https://arxiv.org/html/2607.25356v1#S6 — 6 Conclusion | Exact v1 links https://github.com/LaureBerti/progressive-profiling, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-25356 | complete |
| SF-2026-ARXIV-2607-25357 | RP-3aafc10638057959 | standard | arXiv:2607.25357v1 | SRC-ARXIV@arXiv:2607.25357v1 | https://arxiv.org/html/2607.25357v1#A1.SS6 — A.6 Raven Design Details; https://arxiv.org/html/2607.25357v1#S4.SS2 — 4.2 Raven Block Design | https://arxiv.org/html/2607.25357v1#S8.SS2 — 8.2 Evaluation Benchmarks; https://arxiv.org/html/2607.25357v1#A1.SS3 — A.3 Experimental Details | https://arxiv.org/html/2607.25357v1#S9 — 9 Conclusion | Exact v1 links https://github.com/goombalab/raven, https://huggingface.co/datasets/cerebras/SlimPajama-627B, https://github.com/fla-org/flash-linear-attention; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-25357 | complete |
| SF-2026-ARXIV-2607-25364 | RP-d6e22c8b9d944b1d | deep | arXiv:2607.25364v1 | SRC-ARXIV@arXiv:2607.25364v1 | https://arxiv.org/html/2607.25364v1#S13.SS4 — XIII-D Implications for Agent-System Architecture; https://arxiv.org/html/2607.25364v1#S10.SS1 — X-A Design | https://arxiv.org/html/2607.25364v1#A6 — Appendix F Experimental Units and Denominators; https://arxiv.org/html/2607.25364v1#S10.SS2 — X-B Results | https://arxiv.org/html/2607.25364v1#S17 — XVII Limitations and Threats to Validity; https://arxiv.org/html/2607.25364v1#S13 — XIII Discussion | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-25364 | complete |
| SF-2026-ARXIV-2607-25369 | RP-bea10c3c52abd816 | standard | arXiv:2607.25369v1 | SRC-ARXIV@arXiv:2607.25369v1 | https://arxiv.org/html/2607.25369v1#S2.SS2 — 2.2. Agentic Systems with Reinforcement Learning; https://arxiv.org/html/2607.25369v1#S4 — 4. Methodology | https://arxiv.org/html/2607.25369v1#S5 — 5. Experiments; https://arxiv.org/html/2607.25369v1#S5.SS1 — 5.1. Experimental Setup | https://arxiv.org/html/2607.25369v1#S6 — 6. Conclusion | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-25369 | complete |
| SF-2026-ARXIV-2607-25379 | RP-1fdd9f0cf15bd000 | deep | arXiv:2607.25379v1 | SRC-ARXIV@arXiv:2607.25379v1 | https://arxiv.org/html/2607.25379v1#S3 — 3 Background and methodology | https://arxiv.org/html/2607.25379v1#S5 — 5 Case study: the July 2026 intrusion | https://arxiv.org/html/2607.25379v1#S10 — 10 Conclusion; https://arxiv.org/html/2607.25379v1#S9 — 9 Threats to validity | Exact v1 links https://huggingface.co/blog/security-incident-july-2026, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-25379 | complete |
| SF-2026-ARXIV-2607-25380 | RP-5c554c2ceff00274 | standard | arXiv:2607.25380v1 | SRC-ARXIV@arXiv:2607.25380v1 | https://arxiv.org/html/2607.25380v1#S5 — V Model-Level Memory Architectures: Design, Implementation, and Evaluation; https://arxiv.org/html/2607.25380v1#S5.SS1 — V-A Hybrid Memory Architectures | https://arxiv.org/html/2607.25380v1#S5 — V Model-Level Memory Architectures: Design, Implementation, and Evaluation; https://arxiv.org/html/2607.25380v1#S5.SS3 — V-C Evaluation of Memory Systems | https://arxiv.org/html/2607.25380v1#S3.SS4 — III-D Limitations of Implicit Memory; https://arxiv.org/html/2607.25380v1#S6 — VI Open Challenges and Future Directions | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-25380 | complete |
| SF-2026-ARXIV-2607-25398 | RP-1fda8b729d5c2902 | deep | arXiv:2607.25398v1 | SRC-ARXIV@arXiv:2607.25398v1 | https://arxiv.org/html/2607.25398v1#A4 — Appendix D Agent-visible system prompt; https://arxiv.org/html/2607.25398v1#S3.SS1 — 3.1 Overview and design principles | https://arxiv.org/html/2607.25398v1#S3 — 3 The HANDBOOK.md benchmark; https://arxiv.org/html/2607.25398v1#S4 — 4 Experimental setup | https://arxiv.org/html/2607.25398v1#S6 — 6 Failure analysis; https://arxiv.org/html/2607.25398v1#S7 — 7 Conclusion | Exact v1 links https://github.com/surge-ai/handbook, https://github.com/harbor-framework/terminal-bench, https://github.com/arXiv/html_feedback/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-25398 | complete |
| SF-2026-ARXIV-2607-25400 | RP-40a4de570f98ab4a | deep | arXiv:2607.25400v1 | SRC-ARXIV@arXiv:2607.25400v1 | https://arxiv.org/html/2607.25400v1#A3 — Appendix C Runtime Controller Algorithm | https://arxiv.org/html/2607.25400v1#A7 — Appendix G Per-Scenario Results and Misalignment Analysis; https://arxiv.org/html/2607.25400v1#S5.SSx3 — RQ2: Scenario-Level Results and Misalignment Analysis | https://arxiv.org/html/2607.25400v1#A6 — Appendix F Limitations and Threats to Validity; https://arxiv.org/html/2607.25400v1#S7 — 7 Conclusion | Exact v1 links https://github.com/NousResearch/hermes-agent, https://github.com/strands-agents/agent-sop, https://github.com/arXiv/html_feedback/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-25400 | complete |
| SF-2026-ARXIV-2607-25408 | RP-df1ee5960c7323ab | deep | arXiv:2607.25408v1 | SRC-ARXIV@arXiv:2607.25408v1 | https://arxiv.org/html/2607.25408v1#S2 — 2 Formal decomposition; https://arxiv.org/html/2607.25408v1#S3 — 3 Stability | https://arxiv.org/html/2607.25408v1#S4 — 4 Uncertainty calibration; https://arxiv.org/html/2607.25408v1#S5 — 5 Positioning | https://arxiv.org/html/2607.25408v1#S6 — 6 Limitations; https://arxiv.org/html/2607.25408v1#S7 — 7 Conclusion | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-25408 | complete |
| SF-2026-ARXIV-2607-25415 | RP-9e4edf2d322ca1d6 | deep | arXiv:2607.25415v1 | SRC-ARXIV@arXiv:2607.25415v1 | https://arxiv.org/html/2607.25415v1#S3 — 3 Method: context assembly as the controlled variable | https://arxiv.org/html/2607.25415v1#S5 — 5 Experiments; https://arxiv.org/html/2607.25415v1#S5.SS1 — 5.1 Results | https://arxiv.org/html/2607.25415v1#S7 — 7 Limitations; https://arxiv.org/html/2607.25415v1#S8 — 8 Conclusion | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-25415 | complete |
| SF-2026-ARXIV-2607-25431 | RP-2247e84b030e827e | deep | arXiv:2607.25431v1 | SRC-ARXIV@arXiv:2607.25431v1 | https://arxiv.org/html/2607.25431v1#S3 — 3. System Overview; https://arxiv.org/html/2607.25431v1#A5 — Appendix E Retrieval Models and Frozen Parameters | https://arxiv.org/html/2607.25431v1#S9 — 9. Evaluation; https://arxiv.org/html/2607.25431v1#S9.SS1 — 9.1. Experimental Setup | https://arxiv.org/html/2607.25431v1#S10 — 10. Discussion and Future Directions; https://arxiv.org/html/2607.25431v1#S11 — 11. Conclusion | Exact v1 links https://opencode.ai/docs/tools, https://engineering.fb.com/2024/12/19/developer-tools/glean-open-source-code-indexing/, https://github.com/sourcegraph/zoekt; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-25431 | complete |
| SF-2026-ARXIV-2607-25446 | RP-d1e0e2d06c0815aa | standard | arXiv:2607.25446v1 | SRC-ARXIV@arXiv:2607.25446v1 | https://arxiv.org/html/2607.25446v1#Sx3 — The IMACS Framework | https://arxiv.org/html/2607.25446v1#Sx6 — Experiments | https://arxiv.org/html/2607.25446v1#Sx7 — Discussion and Limitations; https://arxiv.org/html/2607.25446v1#Sx8 — Conclusion | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-25446 | complete |
| SF-2026-ARXIV-2607-25451 | RP-1c5c82c975a6a258 | standard | arXiv:2607.25451v1 | SRC-ARXIV@arXiv:2607.25451v1 | https://arxiv.org/html/2607.25451v1#S3 — 3 Method | https://arxiv.org/html/2607.25451v1#S4 — 4 Results | https://arxiv.org/html/2607.25451v1#S5 — 5 Discussion and limitations; https://arxiv.org/html/2607.25451v1#S6 — 6 Conclusion | Exact v1 links https://github.com/AkshaySasi/bits-and-memories, https://huggingface.co/datasets/AkshaySasi/bits-and-memories, https://github.com/arXiv/html_feedback/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-25451 | complete |
| SF-2026-ARXIV-2607-25467 | RP-135515971e6427d6 | standard | arXiv:2607.25467v1 | SRC-ARXIV@arXiv:2607.25467v1 | https://arxiv.org/html/2607.25467v1#S1 — 1 Introduction; https://arxiv.org/html/2607.25467v1#S2 — 2 Auditing Safe Forgetting with CVMA | https://arxiv.org/html/2607.25467v1#S1 — 1 Introduction; https://arxiv.org/html/2607.25467v1#S2 — 2 Auditing Safe Forgetting with CVMA | https://arxiv.org/html/2607.25467v1#S3 — 3 Attention Is Not Future Utility; https://arxiv.org/html/2607.25467v1#S4.SSx3 — Turn-wise failure survives stronger selection | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-25467 | complete |
| SF-2026-ARXIV-2607-25479 | RP-91031027161cc11e | standard | arXiv:2607.25479v1 | SRC-ARXIV@arXiv:2607.25479v1 | https://arxiv.org/html/2607.25479v1#Ax1 — Appendix . Details on steering vector design; https://arxiv.org/html/2607.25479v1#S3 — III Methodology | https://arxiv.org/html/2607.25479v1#S5 — V Experimental Results; https://arxiv.org/html/2607.25479v1#Ax1.SS2 — .2 Ablation Study | https://arxiv.org/html/2607.25479v1#S3.SS1 — III-A Threat model; https://arxiv.org/html/2607.25479v1#S8 — VIII Conclusion | Exact v1 links https://huggingface.co/microsoft/Phi-3.5-vision-instruct, https://huggingface.co/Salesforce/codet5p-16b, https://huggingface.co/openbmb/MiniCPM-V-2_6; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-25479 | complete |
| SF-2026-ARXIV-2607-25487 | RP-73fb5fa7d5b7a67b | deep | arXiv:2607.25487v1 | SRC-ARXIV@arXiv:2607.25487v1 | https://arxiv.org/html/2607.25487v1#S3 — 3 Method; https://arxiv.org/html/2607.25487v1#S3.SS1 — 3.1 Architecture | https://arxiv.org/html/2607.25487v1#A3 — Appendix C LIBERO-Plus Goal Suite Results; https://arxiv.org/html/2607.25487v1#A4 — Appendix D LIBERO-Plus Long Suite Results | https://arxiv.org/html/2607.25487v1#S6 — 6 Discussion; https://arxiv.org/html/2607.25487v1#S7 — 7 Conclusion | Exact v1 links https://github.com/BrainJellyPie/CoTinyVLA, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-25487 | complete |
| SF-2026-ARXIV-2607-25494 | RP-585afb1df6015395 | standard | arXiv:2607.25494v1 | SRC-ARXIV@arXiv:2607.25494v1 | https://arxiv.org/html/2607.25494v1#S3.SS6 — 3.6. Design Philosophy and Application Value | https://arxiv.org/html/2607.25494v1#S3 — 3. Automated Numerical Stability Analysis of Deep Learning Operators; https://arxiv.org/html/2607.25494v1#S4 — 4. Experimental Simulations | https://arxiv.org/html/2607.25494v1#S5 — 5. Limitations; https://arxiv.org/html/2607.25494v1#S6 — 6. Conclusion | Exact v1 links https://github.com/chenxinye/noisefloat, http://github.com/jax-ml/jax, https://github.com/arXiv/html_feedback/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-25494 | complete |
| SF-2026-ARXIV-2607-25498 | RP-4f070204814beeb1 | deep | arXiv:2607.25498v1 | SRC-ARXIV@arXiv:2607.25498v1 | https://arxiv.org/html/2607.25498v1#S4 — 4 DOPS Framework; https://arxiv.org/html/2607.25498v1#S2.SS1 — 2.1 Transformer-based Large Language Models | https://arxiv.org/html/2607.25498v1#S3 — 3 Motivation: Observations & Problem Analysis; https://arxiv.org/html/2607.25498v1#S6 — 6 Experiments | https://arxiv.org/html/2607.25498v1#S8 — 8 Conclusion | Exact v1 links https://github.com/YIAI-02/TriForm, https://github.com/YIAI-02/TriForm/blob/micro26_pieak_final/docs/EXPERIMENT_HYPERPARAMETERS.md, https://github.com/YIAI-02/TriForm/blob/micro26_pieak_final/README.md; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-25498 | complete |
| SF-2026-ARXIV-2607-25504 | RP-e0928022d43ea9bd | deep | arXiv:2607.25504v1 | SRC-ARXIV@arXiv:2607.25504v1 | https://arxiv.org/html/2607.25504v1#S3 — III Ventaglio Architecture; https://arxiv.org/html/2607.25504v1#S4 — IV Evaluation Methodology and Results | https://arxiv.org/html/2607.25504v1#S4 — IV Evaluation Methodology and Results; https://arxiv.org/html/2607.25504v1#S4.SS1 — IV-A Kernel Benchmark Setup and Roofline Analysis | https://arxiv.org/html/2607.25504v1#S5 — V Conclusion | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-25504 | complete |
| SF-2026-ARXIV-2607-25507 | RP-65f24ca01bed5d31 | standard | arXiv:2607.25507v1 | SRC-ARXIV@arXiv:2607.25507v1 | https://arxiv.org/html/2607.25507v1#S12 — 12 Limits of the Framework; https://arxiv.org/html/2607.25507v1#S13.SS4 — 13.4 Architecture and context-length generalization | https://arxiv.org/html/2607.25507v1#S11 — 11 Experimental Program | https://arxiv.org/html/2607.25507v1#S13 — 13 Future Research; https://arxiv.org/html/2607.25507v1#S14 — 14 Conclusion | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-25507 | complete |
| SF-2026-ARXIV-2607-25516 | RP-a4172fe34eb5bac7 | standard | arXiv:2607.25516v1 | SRC-ARXIV@arXiv:2607.25516v1 | https://arxiv.org/html/2607.25516v1#S4 — IV Method; https://arxiv.org/html/2607.25516v1#S4.SS1 — IV-A Infer-diagnose-refine Framework | https://arxiv.org/html/2607.25516v1#S5 — V Experiments; https://arxiv.org/html/2607.25516v1#S5.SS1 — V-A Simulation Experiments | https://arxiv.org/html/2607.25516v1#S6 — VI Conclusion | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-25516 | complete |
| SF-2026-ARXIV-2607-25554 | RP-8e64b93b28f6265f | standard | arXiv:2607.25554v1 | SRC-ARXIV@arXiv:2607.25554v1 | https://arxiv.org/html/2607.25554v1#A2 — Appendix B Methodology Details; https://arxiv.org/html/2607.25554v1#A2.SS2 — B.2 System Prompts for Time-Truncation Harness | https://arxiv.org/html/2607.25554v1#A3 — Appendix C Experimental Details; https://arxiv.org/html/2607.25554v1#A3.SS6 — C.6 Benchmarks and Metrics | https://arxiv.org/html/2607.25554v1#S7.SS3 — 7.3 Limitations and Future Works; https://arxiv.org/html/2607.25554v1#S2.SS1 — 2.1 Agent Frameworks for Future Prediction | Exact v1 links https://huggingface.co/datasets/wxcai/manifold_newest_multi_domains_260318, https://www.anthropic.com/product/claude-code, https://openai.com/index/introducing-codex; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-25554 | complete |
| SF-2026-ARXIV-2607-25560 | RP-ee595dcea4a055c7 | standard | arXiv:2607.25560v1 | SRC-ARXIV@arXiv:2607.25560v1 | https://arxiv.org/html/2607.25560v1#A2 — Appendix B Method Prompts; https://arxiv.org/html/2607.25560v1#S3 — 3 Method | https://arxiv.org/html/2607.25560v1#A6 — Appendix F Additional Experimental Analysis; https://arxiv.org/html/2607.25560v1#A4 — Appendix D Experimental Configuration | https://arxiv.org/html/2607.25560v1#S6 — 6 Conclusion; https://arxiv.org/html/2607.25560v1#Sx2 — Limitations | Exact v1 links https://github.com/anthropics/skills/blob/main/skills/skill-creator/SKILL.md, https://github.com/yusufkaraaslan/Skill_Seekers, https://github.com/NousResearch/hermes-agent; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-25560 | complete |
| SF-2026-ARXIV-2607-25566 | RP-805e5f49ca83f383 | deep | arXiv:2607.25566v1 | SRC-ARXIV@arXiv:2607.25566v1 | https://arxiv.org/html/2607.25566v1#S3 — 3 Our Approach: ARCHER; https://arxiv.org/html/2607.25566v1#S3.SS4 — 3.4 Agentic Harness Architecture | https://arxiv.org/html/2607.25566v1#S4 — 4 Experimental Results; https://arxiv.org/html/2607.25566v1#A7 — Appendix G Per-Scenario Difficulty, Cost, and Model-Choice Analysis | https://arxiv.org/html/2607.25566v1#S5 — 5 Limitations and Future Work | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-25566 | complete |
| SF-2026-ARXIV-2607-25583 | RP-25fc1123105bb00f | standard | arXiv:2607.25583v1 | SRC-ARXIV@arXiv:2607.25583v1 | https://arxiv.org/html/2607.25583v1#S3 — 3 Methodology; https://arxiv.org/html/2607.25583v1#S3.SS1 — 3.1 Base Model and Task | https://arxiv.org/html/2607.25583v1#S4 — 4 Experimental Setup; https://arxiv.org/html/2607.25583v1#S5 — 5 Results | https://arxiv.org/html/2607.25583v1#S6 — 6 Discussion; https://arxiv.org/html/2607.25583v1#S7 — 7 Limitations | Exact v1 links https://github.com/mahendrarathore1742/efficient_peft_small_models, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-25583 | complete |
| SF-2026-ARXIV-2607-25589 | RP-154908e94fb81253 | standard | arXiv:2607.25589v1 | SRC-ARXIV@arXiv:2607.25589v1 | https://arxiv.org/html/2607.25589v1#S2 — 2 Conceptual framework; https://arxiv.org/html/2607.25589v1#S3 — 3 Materials and methods | https://arxiv.org/html/2607.25589v1#S2.SS1 — 2.1 Six states of a computational result; https://arxiv.org/html/2607.25589v1#S2.SS3 — 2.3 What can be corrected without repeating the experiment | https://arxiv.org/html/2607.25589v1#S5.SS1 — 5.1 Design principles and threat model; https://arxiv.org/html/2607.25589v1#S6 — 6 Discussion | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-25589 | complete |
| SF-2026-ARXIV-2607-25600 | RP-1fe7f0c4a5c48b8c | deep | arXiv:2607.25600v1 | SRC-ARXIV@arXiv:2607.25600v1 | https://arxiv.org/html/2607.25600v1#Sx4 — Experimental Design | https://arxiv.org/html/2607.25600v1#Sx4 — Experimental Design; https://arxiv.org/html/2607.25600v1#Sx5 — Results | https://arxiv.org/html/2607.25600v1#Sx7 — Discussion and Limitations; https://arxiv.org/html/2607.25600v1#Sx8 — Conclusion | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-25600 | complete |
| SF-2026-ARXIV-2607-25614 | RP-de7f73bef4cc6e04 | standard | arXiv:2607.25614v1 | SRC-ARXIV@arXiv:2607.25614v1 | https://arxiv.org/html/2607.25614v1#S2 — 2 Method; https://arxiv.org/html/2607.25614v1#A3 — Appendix C Training and Implementation Details | https://arxiv.org/html/2607.25614v1#A1 — Appendix A Datasets and Evaluation Protocols; https://arxiv.org/html/2607.25614v1#A1.SS1 — A.1 Domain Specialization and Evaluation Data | https://arxiv.org/html/2607.25614v1#S7 — 7 Conclusion; https://arxiv.org/html/2607.25614v1#S8 — 8 Limitations | Exact v1 links https://github.com/LUMIA-Group/MemSFT, https://huggingface.co/collections/Jiarui-Wang/memsft, https://github.com/arXiv/html_feedback/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-25614 | complete |
| SF-2026-ARXIV-2607-25619 | RP-770ffaf239415c8f | deep | arXiv:2607.25619v1 | SRC-ARXIV@arXiv:2607.25619v1 | https://arxiv.org/html/2607.25619v1#S3 — III System Design & Evaluation Setup; https://arxiv.org/html/2607.25619v1#S2.SS4 — II-D Threat Model | https://arxiv.org/html/2607.25619v1#S3 — III System Design & Evaluation Setup; https://arxiv.org/html/2607.25619v1#S3.SS7 — III-G Experiment Setup | https://arxiv.org/html/2607.25619v1#S2.SS4 — II-D Threat Model; https://arxiv.org/html/2607.25619v1#S6 — VI Threats to Validity | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-25619 | complete |
| SF-2026-ARXIV-2607-25635 | RP-1acbbb1df6385d24 | standard | arXiv:2607.25635v1 | SRC-ARXIV@arXiv:2607.25635v1 | https://arxiv.org/html/2607.25635v1#S4 — IV Methods: Analyzing MCPApps | https://arxiv.org/html/2607.25635v1#S4.SS1 — IV-A Manual Analysis and Taxonomy Derivation; https://arxiv.org/html/2607.25635v1#S4.SS3 — IV-C Evaluation | https://arxiv.org/html/2607.25635v1#S6 — VI Discussion; https://arxiv.org/html/2607.25635v1#S7 — VII Threats to Validity | Exact v1 links https://github.com/ChatGPTNextWeb/NextChat, https://github.com/daodao97/ChatMCP, https://github.com/google-gemini/gemini-cli; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-25635 | complete |
| SF-2026-ARXIV-2607-25637 | RP-c1b0e5c7f053bad0 | standard | arXiv:2607.25637v1 | SRC-ARXIV@arXiv:2607.25637v1 | https://arxiv.org/html/2607.25637v1#S4 — IV The aiprov Method | https://arxiv.org/html/2607.25637v1#S6 — VI Meta-Experiment: This Paper as Case Study | https://arxiv.org/html/2607.25637v1#S7 — VII Discussion and Limitations; https://arxiv.org/html/2607.25637v1#S8 — VIII Conclusion | Exact v1 links https://github.com/noheton/f-ai2-r, https://github.com/noheton/Obscurity-Is-Dead, https://github.com/noheton/f-ai-r; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-25637 | complete |
| SF-2026-ARXIV-2607-25650 | RP-7b030f6504abdb23 | deep | arXiv:2607.25650v1 | SRC-ARXIV@arXiv:2607.25650v1 | https://arxiv.org/html/2607.25650v1#S3 — 3. PowerScale Design; https://arxiv.org/html/2607.25650v1#S5.SS1 — 5.1. Evaluation Methodology | https://arxiv.org/html/2607.25650v1#S5 — 5. Evaluation; https://arxiv.org/html/2607.25650v1#S5.SS1 — 5.1. Evaluation Methodology | https://arxiv.org/html/2607.25650v1#S7 — 7. Conclusion | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-25650 | complete |
| SF-2026-ARXIV-2607-25651 | RP-1c4cbdf98a460396 | standard | arXiv:2607.25651v1 | SRC-ARXIV@arXiv:2607.25651v1 | https://arxiv.org/html/2607.25651v1#S4 — 4. Methodology | https://arxiv.org/html/2607.25651v1#S3.SS1 — 3.1. Problem Analysis; https://arxiv.org/html/2607.25651v1#S4.SS2 — 4.2. LLM-Aided Bug Analysis | https://arxiv.org/html/2607.25651v1#S6.SS4 — 6.4. Limitations and Future Work; https://arxiv.org/html/2607.25651v1#S6 — 6. Discussion | Exact v1 links https://github.com/pytorch/pytorch/issues/176596, https://github.com/pytorch/pytorch/issues/176692, https://github.com/pytorch/pytorch/issues/150765; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-25651 | complete |
| SF-2026-ARXIV-2607-25656 | RP-bd5998bf4347557f | standard | arXiv:2607.25656v1 | SRC-ARXIV@arXiv:2607.25656v1 | https://arxiv.org/html/2607.25656v1#A4.SSx2 — II. Framework Dependence; https://arxiv.org/html/2607.25656v1#Sx4 — Methodology | https://arxiv.org/html/2607.25656v1#A1 — Appendix A A. Ablation Study; https://arxiv.org/html/2607.25656v1#A5 — Appendix E E. Benchmark Construction | https://arxiv.org/html/2607.25656v1#A5.SSx3 — III. Generation Failure Cases; https://arxiv.org/html/2607.25656v1#A6.SSx1 — I. Detailed Discussion of the Main Results | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-25656 | complete |
| SF-2026-ARXIV-2607-25659 | RP-10aeb23159e98ba5 | deep | arXiv:2607.25659v1 | SRC-ARXIV@arXiv:2607.25659v1 | https://arxiv.org/html/2607.25659v1#Sx1 — Introduction; https://arxiv.org/html/2607.25659v1#Sx2 — Related Work | https://arxiv.org/html/2607.25659v1#A1 — Appendix A Additional Results; https://arxiv.org/html/2607.25659v1#Sx5 — Experimental Setup | https://arxiv.org/html/2607.25659v1#A1.SSx6 — Failure-Mode Diagnostics; https://arxiv.org/html/2607.25659v1#Sx8 — Conclusion | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-25659 | complete |
| SF-2026-ARXIV-2607-25663 | RP-93567c8a45c3fc0e | standard | arXiv:2607.25663v1 | SRC-ARXIV@arXiv:2607.25663v1 | https://arxiv.org/html/2607.25663v1#Sx3 — Methodology; https://arxiv.org/html/2607.25663v1#Sx6.SSx1 — Adaptation Site is a Functional Design Variable | https://arxiv.org/html/2607.25663v1#Sx9 — Appendix C: Localization Experiments Results; https://arxiv.org/html/2607.25663v1#Sx11 — Appendix E: Budget Sensitivity Analysis | https://arxiv.org/html/2607.25663v1#Sx6.SSx3 — Limitations and Future Directions; https://arxiv.org/html/2607.25663v1#Sx6 — Discussion | Exact v1 links https://github.com/rramnauth2220/adaptation-geometries, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-25663 | complete |
| SF-2026-ARXIV-2607-25669 | RP-6a4c37ba493e459f | standard | arXiv:2607.25669v1 | SRC-ARXIV@arXiv:2607.25669v1 | https://arxiv.org/html/2607.25669v1#S3 — 3 Method; https://arxiv.org/html/2607.25669v1#S3.SS2 — 3.2 Our Method: OmniDelta | https://arxiv.org/html/2607.25669v1#S4 — 4 Experiments; https://arxiv.org/html/2607.25669v1#S4.SS1 — 4.1 Experimental Setting | https://arxiv.org/html/2607.25669v1#S6 — 6 Conclusion | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-25669 | complete |
| SF-2026-ARXIV-2607-25718 | RP-986293566bf9d5ae | standard | arXiv:2607.25718v1 | SRC-ARXIV@arXiv:2607.25718v1 | https://arxiv.org/html/2607.25718v1#S2 — 2 Methodology; https://arxiv.org/html/2607.25718v1#S2.SS4 — 2.4 The Framework of HYSET | https://arxiv.org/html/2607.25718v1#S3 — 3 Experiments; https://arxiv.org/html/2607.25718v1#S3.SS1 — 3.1 Experimental Setup | https://arxiv.org/html/2607.25718v1#S4 — 4 Conclusion | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-25718 | complete |
| SF-2026-ARXIV-2607-25750 | RP-f73d464aa9c5e0b9 | standard | arXiv:2607.25750v1 | SRC-ARXIV@arXiv:2607.25750v1 | https://arxiv.org/html/2607.25750v1#A1 — Appendix A Implementation and Experimental Details | https://arxiv.org/html/2607.25750v1#A1 — Appendix A Implementation and Experimental Details; https://arxiv.org/html/2607.25750v1#A3 — Appendix C Additional Results | https://arxiv.org/html/2607.25750v1#Sx5 — Limitations; https://arxiv.org/html/2607.25750v1#Sx7 — Conclusion | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-25750 | complete |
| SF-2026-ARXIV-2607-25765 | RP-dedd6b63d7dbd8b3 | standard | arXiv:2607.25765v1 | SRC-ARXIV@arXiv:2607.25765v1 | https://arxiv.org/html/2607.25765v1#S3.SS4 — 3.4 Automatic Validation and Model-assisted Screening | https://arxiv.org/html/2607.25765v1#S3 — 3 Benchmark Construction; https://arxiv.org/html/2607.25765v1#S5 — 5 Experiments | https://arxiv.org/html/2607.25765v1#S6 — 6 Conclusion | Exact v1 links https://github.com/haolpku/WorkSurface-Bench, https://huggingface.co/datasets/lhpku20010120/WorkSurface-Bench, https://github.com/arXiv/html_feedback/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-25765 | complete |
| SF-2026-ARXIV-2607-25798 | RP-f042d1f5ca6a3d48 | standard | arXiv:2607.25798v1 | SRC-ARXIV@arXiv:2607.25798v1 | https://arxiv.org/html/2607.25798v1#S2 — 2 Method; https://arxiv.org/html/2607.25798v1#S2.SS2 — 2.2 Transformer Transformer: A Unifying Architecture | https://arxiv.org/html/2607.25798v1#S3 — 3 Results; https://arxiv.org/html/2607.25798v1#S7 — 7 Additional Experiments | https://arxiv.org/html/2607.25798v1#S5 — 5 Conclusion | Exact v1 links https://github.com/kevinzakka/mink, http://github.com/google-deepmind/mujoco_menagerie, https://github.com/Genesis-Embodied-AI/Genesis; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-25798 | complete |
| SF-2026-ARXIV-2607-25816 | RP-b0c3a12459577034 | deep | arXiv:2607.25816v1 | SRC-ARXIV@arXiv:2607.25816v1 | https://arxiv.org/html/2607.25816v1#S3 — 3 Method; https://arxiv.org/html/2607.25816v1#A1 — Appendix A Implementation Details | https://arxiv.org/html/2607.25816v1#S2.SS1 — 2.1 Evaluation Protocol; https://arxiv.org/html/2607.25816v1#S4 — 4 Experiments | https://arxiv.org/html/2607.25816v1#S6 — 6 Conclusion; https://arxiv.org/html/2607.25816v1#Sx1 — Limitations | Exact v1 links https://huggingface.co/Qwen/Qwen3.5-4B, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-25816 | complete |
| SF-2026-ARXIV-2607-25818 | RP-2cc7d083a5c1f20d | standard | arXiv:2607.25818v1 | SRC-ARXIV@arXiv:2607.25818v1 | https://arxiv.org/html/2607.25818v1#S3 — III Method; https://arxiv.org/html/2607.25818v1#S3.SS1 — III-A SepPrune: Method Overview | https://arxiv.org/html/2607.25818v1#S4 — IV Experiments; https://arxiv.org/html/2607.25818v1#S4.SS1 — IV-A Main results | https://arxiv.org/html/2607.25818v1#S5 — V Conclusion | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-25818 | complete |
| SF-2026-ARXIV-2607-25825 | RP-642b9b138f64e02f | standard | arXiv:2607.25825v1 | SRC-ARXIV@arXiv:2607.25825v1 | https://arxiv.org/html/2607.25825v1#Sx1 — Introduction; https://arxiv.org/html/2607.25825v1#Sx2 — Preliminaries and Related Work | https://arxiv.org/html/2607.25825v1#Sx4.SSx3 — Ablation Experiment; https://arxiv.org/html/2607.25825v1#Sx4 — Experiments | https://arxiv.org/html/2607.25825v1#Sx5 — Conclusion | Exact v1 links https://github.com/csdstar/chill-dev, https://github.com/krafton-ai/kira, https://github.com/arXiv/html_feedback/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-25825 | complete |
| SF-2026-ARXIV-2607-25831 | RP-72aa4234d37dce6b | standard | arXiv:2607.25831v1 | SRC-ARXIV@arXiv:2607.25831v1 | https://arxiv.org/html/2607.25831v1#S3.SS3 — III-C Implementation | https://arxiv.org/html/2607.25831v1#S4 — IV Experimental Results; https://arxiv.org/html/2607.25831v1#S4.SS2 — IV-B Ablation Analysis (RQ2) | https://arxiv.org/html/2607.25831v1#S5 — V Threats to Validity; https://arxiv.org/html/2607.25831v1#S6 — VI Discussion | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-25831 | complete |
| SF-2026-ARXIV-2607-25852 | RP-9c4108b8dc0132b9 | deep | arXiv:2607.25852v1 | SRC-ARXIV@arXiv:2607.25852v1 | https://arxiv.org/html/2607.25852v1#S3.SS3 — 3.3 Loss Design; https://arxiv.org/html/2607.25852v1#S6 — 6 AngelSpec Framework | https://arxiv.org/html/2607.25852v1#S2.SS5 — 2.5 Experimental Results; https://arxiv.org/html/2607.25852v1#S3.SS4 — 3.4 Main Results | https://arxiv.org/html/2607.25852v1#S8 — 8 Conclusion | Exact v1 links https://github.com/Tencent/AngelSpec, https://github.com/lightseekorg/TorchSpec, https://github.com/arXiv/html_feedback/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-25852 | complete |
| SF-2026-ARXIV-2607-25853 | RP-87a2735ef1a5abf1 | standard | arXiv:2607.25853v1 | SRC-ARXIV@arXiv:2607.25853v1 | https://arxiv.org/html/2607.25853v1#S3 — 3 Methodology; https://arxiv.org/html/2607.25853v1#S3.SS1 — 3.1 Framework Overview | https://arxiv.org/html/2607.25853v1#A5 — Appendix E Additional Experimental Results; https://arxiv.org/html/2607.25853v1#A5.SS1 — E.1 Main Results on GPT-5.2-Codex | https://arxiv.org/html/2607.25853v1#S5 — 5 Conclusion | Exact v1 links https://github.com/LabRAI/LangSkills, https://openai.com/index/introducing-gpt-5-2-codex, https://github.com/arXiv/html_feedback/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-25853 | complete |
| SF-2026-ARXIV-2607-25857 | RP-9138fa6d9953ae5a | standard | arXiv:2607.25857v1 | SRC-ARXIV@arXiv:2607.25857v1 | https://arxiv.org/html/2607.25857v1#S4.SS1 — 4.1 Taxonomy Design; https://arxiv.org/html/2607.25857v1#S5 — 5 Model Architecture | https://arxiv.org/html/2607.25857v1#A1 — Appendix A Multilingual Evaluation Results; https://arxiv.org/html/2607.25857v1#A2 — Appendix B Full Evaluation Taxonomy | https://arxiv.org/html/2607.25857v1#S8 — 8 Conclusion | Exact v1 links https://huggingface.co/nvidia/Nemotron-3.5-Content-Safety, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-25857 | complete |
| SF-2026-ARXIV-2607-25877 | RP-0092ef24932d92e6 | standard | arXiv:2607.25877v1 | SRC-ARXIV@arXiv:2607.25877v1 | https://arxiv.org/html/2607.25877v1#S3 — 3 Multi-agent system design; https://arxiv.org/html/2607.25877v1#S2.SS1 — 2.1 Multi-Agent Systems | https://arxiv.org/html/2607.25877v1#S5 — 5 Evaluation | https://arxiv.org/html/2607.25877v1#S6 — 6 Conclusion | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-25877 | complete |
| SF-2026-ARXIV-2607-25880 | RP-3f6bfdc96ad173a9 | standard | arXiv:2607.25880v1 | SRC-ARXIV@arXiv:2607.25880v1 | https://arxiv.org/html/2607.25880v1#S4 — 4 Stemma Design; https://arxiv.org/html/2607.25880v1#A3 — Appendix C Stemma Implementation and Configuration Details | https://arxiv.org/html/2607.25880v1#A9 — Appendix I Full Ablation Results; https://arxiv.org/html/2607.25880v1#A4 — Appendix D Model Benchmark | https://arxiv.org/html/2607.25880v1#S6 — 6 Discussion and Conclusion | Exact v1 links https://github.com/kerryzhangcode/Stemma, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-25880 | complete |
| SF-2026-ARXIV-2607-25883 | RP-1199e9bea37ca8c3 | standard | arXiv:2607.25883v1 | SRC-ARXIV@arXiv:2607.25883v1 | https://arxiv.org/html/2607.25883v1#S3 — 3. Towards a Systems Foundation; https://arxiv.org/html/2607.25883v1#S3.SS2 — 3.2. Design Principles | https://arxiv.org/html/2607.25883v1#S1 — 1. Introduction; https://arxiv.org/html/2607.25883v1#S2 — 2. Background | https://arxiv.org/html/2607.25883v1#S6 — 6. Discussion and Future Work | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-25883 | complete |
| SF-2026-ARXIV-2607-25884 | RP-ec21f9c84079cc46 | deep | arXiv:2607.25884v1 | SRC-ARXIV@arXiv:2607.25884v1 | https://arxiv.org/html/2607.25884v1#S1 — I Introduction; https://arxiv.org/html/2607.25884v1#S2 — II CONQuER Search and Compiler Infrastructure | https://arxiv.org/html/2607.25884v1#S4.SS3 — IV-C RQ3: Ablation Analysis; https://arxiv.org/html/2607.25884v1#S3 — III Evaluation | https://arxiv.org/html/2607.25884v1#S7 — VII Conclusion and Future Work; https://arxiv.org/html/2607.25884v1#S5 — V Threats to Validity | Exact v1 links https://github.com/dakaidan/CONQuER-Replication, https://github.com/pytorch/executorch, https://github.com/arXiv/html_feedback/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-25884 | complete |
| SF-2026-ARXIV-2607-25886 | RP-37c62b4f16bcfced | deep | arXiv:2607.25886v1 | SRC-ARXIV@arXiv:2607.25886v1 | https://arxiv.org/html/2607.25886v1#S1 — 1 Introduction; https://arxiv.org/html/2607.25886v1#S2 — 2 Related Work | https://arxiv.org/html/2607.25886v1#S4.SS3 — 4.3 Benchmarks and evaluation; https://arxiv.org/html/2607.25886v1#S5 — 5 Results and Analysis | https://arxiv.org/html/2607.25886v1#S6 — 6 Discussion and Limitations; https://arxiv.org/html/2607.25886v1#S7 — 7 Conclusion | Exact v1 links https://github.com/evolvent-ai/RSIBench-Data, https://github.com/thinking-machines-lab/tinker, https://github.com/e2b-dev; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-25886 | complete |
| SF-2026-ARXIV-2607-25890 | RP-be54bef2b45d479f | standard | arXiv:2607.25890v1 | SRC-ARXIV@arXiv:2607.25890v1 | https://arxiv.org/html/2607.25890v1#S4 — IV Methodology; https://arxiv.org/html/2607.25890v1#S4.SS1 — IV-A Test Design | https://arxiv.org/html/2607.25890v1#S5.SS1 — V-A Preliminary Results; https://arxiv.org/html/2607.25890v1#S7 — VII Evaluation | https://arxiv.org/html/2607.25890v1#S2.SS1 — II-A Threat Model; https://arxiv.org/html/2607.25890v1#S8 — VIII Discussion | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-25890 | complete |
| SF-2026-ARXIV-2607-25891 | RP-30faeb4e55665db4 | standard | arXiv:2607.25891v1 | SRC-ARXIV@arXiv:2607.25891v1 | https://arxiv.org/html/2607.25891v1#A2 — Appendix B Methodology; https://arxiv.org/html/2607.25891v1#A1.SS4 — A.4 Data model | https://arxiv.org/html/2607.25891v1#A1.SS1 — A.1 Benchmark groups; https://arxiv.org/html/2607.25891v1#S5 — 5 Analysis & applications | https://arxiv.org/html/2607.25891v1#S6 — 6 Conclusion; https://arxiv.org/html/2607.25891v1#Sx1 — Limitations | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-25891 | complete |
| SF-2026-ARXIV-2607-25904 | RP-e8461428bc5ffd1b | deep | arXiv:2607.25904v1 | SRC-ARXIV@arXiv:2607.25904v1 | https://arxiv.org/html/2607.25904v1#A1.SS2 — A.2 System Prompt Structure; https://arxiv.org/html/2607.25904v1#Sx3.SSx2 — Propose-then-Verify Framework | https://arxiv.org/html/2607.25904v1#A1.SS5 — A.5 Category-wise Evaluation Results; https://arxiv.org/html/2607.25904v1#A1.SS11 — A.11 Interactive Reward Agent Error Case Analysis | https://arxiv.org/html/2607.25904v1#Sx6 — Discussion and Conclusion | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-25904 | complete |
| SF-2026-ARXIV-2607-25907 | RP-78bdb2033cbe9908 | standard | arXiv:2607.25907v1 | SRC-ARXIV@arXiv:2607.25907v1 | https://arxiv.org/html/2607.25907v1#S3 — 3 Method; https://arxiv.org/html/2607.25907v1#S5.SS3 — 5.3 Input-side vs. model-side: activation is not behavior | https://arxiv.org/html/2607.25907v1#S3.SS3 — 3.3 Evaluation protocol; https://arxiv.org/html/2607.25907v1#S4 — 4 Experimental Setup | https://arxiv.org/html/2607.25907v1#S6 — 6 Discussion and Conclusion; https://arxiv.org/html/2607.25907v1#Sx1 — Limitations | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-25907 | complete |
| SF-2026-ARXIV-2607-25912 | RP-3ad1f6de9d7f19e0 | standard | arXiv:2607.25912v1 | SRC-ARXIV@arXiv:2607.25912v1 | https://arxiv.org/html/2607.25912v1#S3 — 3 Method; https://arxiv.org/html/2607.25912v1#S3.SS1 — 3.1 SAM3D-guided VLA Training Framework | https://arxiv.org/html/2607.25912v1#S4 — 4 Experiments | https://arxiv.org/html/2607.25912v1#S5 — 5 Conclusion; https://arxiv.org/html/2607.25912v1#S6 — 6 Limitations | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-25912 | complete |
| SF-2026-ARXIV-2607-25914 | RP-dc098d16d93b49e8 | standard | arXiv:2607.25914v1 | SRC-ARXIV@arXiv:2607.25914v1 | https://arxiv.org/html/2607.25914v1#S2.SS1 — II-A Trust Management in Multi-Agent Systems; https://arxiv.org/html/2607.25914v1#S2.SS2 — II-B 3GPP Management Framework and Information Models | https://arxiv.org/html/2607.25914v1#S5 — V Formal Analysis; https://arxiv.org/html/2607.25914v1#S6 — VI Evaluation | https://arxiv.org/html/2607.25914v1#S7 — VII Discussion; https://arxiv.org/html/2607.25914v1#S7.SS4 — VII-D Limitations | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-25914 | complete |
| SF-2026-ARXIV-2607-25915 | RP-b918d12b5e08faf5 | standard | arXiv:2607.25915v1 | SRC-ARXIV@arXiv:2607.25915v1 | https://arxiv.org/html/2607.25915v1#S3 — 3 Method; https://arxiv.org/html/2607.25915v1#S3.SS5 — 3.5 Implementation Details | https://arxiv.org/html/2607.25915v1#S4 — 4 Experiments; https://arxiv.org/html/2607.25915v1#S4.SS1 — 4.1 Experimental Setup | https://arxiv.org/html/2607.25915v1#S5 — 5 Discussion and Future Work; https://arxiv.org/html/2607.25915v1#S6 — 6 Conclusion | Exact v1 links https://huggingface.co/Qwen/Qwen3.5-0.8B-Base, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-25915 | complete |
| SF-2026-ARXIV-2607-25918 | RP-2b92139f17253306 | standard | arXiv:2607.25918v1 | SRC-ARXIV@arXiv:2607.25918v1 | https://arxiv.org/html/2607.25918v1#Sx3 — Method; https://arxiv.org/html/2607.25918v1#Sx2.SSx1 — World-Action Models and Efficient Visual Foresight | https://arxiv.org/html/2607.25918v1#Sx4 — Experiments; https://arxiv.org/html/2607.25918v1#Sx4.SSx1 — Experimental Setup | https://arxiv.org/html/2607.25918v1#Sx5 — Conclusion | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-25918 | complete |
| SF-2026-ARXIV-2607-25936 | RP-d3202b205c036ac3 | standard | arXiv:2607.25936v1 | SRC-ARXIV@arXiv:2607.25936v1 | https://arxiv.org/html/2607.25936v1#S3 — 3 Method; https://arxiv.org/html/2607.25936v1#S3.SS1 — 3.1 Threat Model | https://arxiv.org/html/2607.25936v1#S4.SS2 — 4.2 Experiment Result; https://arxiv.org/html/2607.25936v1#A1 — Appendix A Appendix A: Experimental Settings | https://arxiv.org/html/2607.25936v1#S3.SS1 — 3.1 Threat Model; https://arxiv.org/html/2607.25936v1#S5 — 5 Conclusion | Exact v1 links https://github.com/meta-llama/llama3/blob/main/MODEL_CARD.md, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-25936 | complete |
| SF-2026-ARXIV-2607-25948 | RP-697e8caff0ec573a | standard | arXiv:2607.25948v1 | SRC-ARXIV@arXiv:2607.25948v1 | https://arxiv.org/html/2607.25948v1#S3 — 3 Method; https://arxiv.org/html/2607.25948v1#S3.SS2 — 3.2 Any-to-Any Decoder-Only Architecture | https://arxiv.org/html/2607.25948v1#A2 — Appendix B Additional Ablations; https://arxiv.org/html/2607.25948v1#A3 — Appendix C More Evaluations | https://arxiv.org/html/2607.25948v1#A6 — Appendix F Limitation Discussion; https://arxiv.org/html/2607.25948v1#S5 — 5 Conclusion | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-25948 | complete |
| SF-2026-ARXIV-2607-25970 | RP-32a5d1d79958f537 | deep | arXiv:2607.25970v1 | SRC-ARXIV@arXiv:2607.25970v1 | https://arxiv.org/html/2607.25970v1#A3.SS6 — C.6 Alternative fallback designs; https://arxiv.org/html/2607.25970v1#A4 — Appendix D Designing Environments and Rewards for Optimization RL | https://arxiv.org/html/2607.25970v1#A2.SS9 — B.9 Training ablations: does DMC-Optim help, and is it enough to solve optimization RL?; https://arxiv.org/html/2607.25970v1#A3.SS10 — C.10 Joint training-time and evaluation-time calibration sweeps | https://arxiv.org/html/2607.25970v1#A2.SS2 — B.2 Source data, limitations, and decontamination; https://arxiv.org/html/2607.25970v1#A3.SS4 — C.4 Fallback after remote execution failures | Exact v1 links https://github.com/containers/bubblewrap, https://github.com/facebookresearch/BigOBench/tree/main/src/complexity/sandbox, https://huggingface.co/Qwen/Qwen2.5-72B/blob/main/LICENSE; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-25970 | complete |
| SF-2026-ARXIV-2607-25987 | RP-d4bed957cb31a981 | standard | arXiv:2607.25987v1 | SRC-ARXIV@arXiv:2607.25987v1 | https://arxiv.org/html/2607.25987v1#A2.SS1 — B.1 Model Details | https://arxiv.org/html/2607.25987v1#A7 — Appendix G Complete Evaluation Results; https://arxiv.org/html/2607.25987v1#A10 — Appendix J Constraint Group Results | https://arxiv.org/html/2607.25987v1#S5 — 5 Conclusion | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-25987 | complete |
| SF-2026-ARXIV-2607-25992 | RP-14c27a61cff77332 | deep | arXiv:2607.25992v1 | SRC-ARXIV@arXiv:2607.25992v1 | https://arxiv.org/html/2607.25992v1#S3 — 3. MemLens System Design | https://arxiv.org/html/2607.25992v1#S3.SS1 — 3.1. Memory Data Evaluation | https://arxiv.org/html/2607.25992v1#S1 — 1. Introduction; https://arxiv.org/html/2607.25992v1#S2 — 2. MemLens Overview | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-25992 | complete |
| SF-2026-ARXIV-2607-25995 | RP-fa21c56cec8d9336 | standard | arXiv:2607.25995v1 | SRC-ARXIV@arXiv:2607.25995v1 | https://arxiv.org/html/2607.25995v1#S3 — 3 System Architecture; https://arxiv.org/html/2607.25995v1#S2.SS2 — 2.2 Attack Graph Construction for Cloud-Native Systems | https://arxiv.org/html/2607.25995v1#S4 — 4 The VulnCare Benchmark; https://arxiv.org/html/2607.25995v1#S5 — 5 Graph-Based Attack Path Analysis | https://arxiv.org/html/2607.25995v1#S6.SS5 — 6.5 RQ4: Failure Modes; https://arxiv.org/html/2607.25995v1#S7 — 7 Conclusion | Exact v1 links https://github.com/dynatrace-research/vulncare, https://github.com/dynatrace-research/kutie-artifacts, https://github.com/madhuakula/kubernetes-goat; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-25995 | complete |
| SF-2026-ARXIV-2607-25996 | RP-2ec500c55caf670a | standard | arXiv:2607.25996v1 | SRC-ARXIV@arXiv:2607.25996v1 | https://arxiv.org/html/2607.25996v1#S4 — 4. Experimental Design; https://arxiv.org/html/2607.25996v1#S2.SS1 — 2.1. Long Context Language Models | https://arxiv.org/html/2607.25996v1#S2.SS3 — 2.3. Coding Ability Evaluation Benchmarks; https://arxiv.org/html/2607.25996v1#S3.SS1 — 3.1. Benchmark Tasks | https://arxiv.org/html/2607.25996v1#S6 — 6. Threats to Validity; https://arxiv.org/html/2607.25996v1#S7 — 7. Conclusion | Exact v1 links https://github.com/DeepSoftwareAnalytics/RepoReasoner, https://github.com/ionelmc/python-hunter, https://github.com/arXiv/html_feedback/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-25996 | complete |
| SF-2026-ARXIV-2607-26004 | RP-4b6aedc42408b0c8 | standard | arXiv:2607.26004v1 | SRC-ARXIV@arXiv:2607.26004v1 | https://arxiv.org/html/2607.26004v1#A1 — Appendix A Algorithms; https://arxiv.org/html/2607.26004v1#S2 — 2 Generative Flow Models | https://arxiv.org/html/2607.26004v1#A2 — Appendix B Experiments; https://arxiv.org/html/2607.26004v1#S5 — 5 Experiments | https://arxiv.org/html/2607.26004v1#S6 — 6 Conclusion | Exact v1 links https://github.com/ModelTC/lightx2v, https://github.com/NVlabs/FastGen, https://github.com/arXiv/html_feedback/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-26004 | complete |
| SF-2026-ARXIV-2607-26016 | RP-dbb9da6f9586b538 | standard | arXiv:2607.26016v1 | SRC-ARXIV@arXiv:2607.26016v1 | https://arxiv.org/html/2607.26016v1#S3.SS4 — III-D Architecture System Design; https://arxiv.org/html/2607.26016v1#S2.SS2 — II-B Inverse Design in Photonic Circuits | https://arxiv.org/html/2607.26016v1#S4 — IV Evaluation Methodology; https://arxiv.org/html/2607.26016v1#S5 — V Results and Discussion | https://arxiv.org/html/2607.26016v1#S1.SS1 — I-A State-of-the-Art PTAs and Their Limitations; https://arxiv.org/html/2607.26016v1#S5 — V Results and Discussion | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-26016 | complete |
| SF-2026-ARXIV-2607-26017 | RP-880d349821d16417 | standard | arXiv:2607.26017v1 | SRC-ARXIV@arXiv:2607.26017v1 | https://arxiv.org/html/2607.26017v1#S3 — 3 Methodology; https://arxiv.org/html/2607.26017v1#S3.SS2 — 3.2 Self-Routing Memory Architecture | https://arxiv.org/html/2607.26017v1#S4.SS2 — 4.2 Main Results and Analysis; https://arxiv.org/html/2607.26017v1#S4.SS3 — 4.3 Ablation and Qualitative Analysis | https://arxiv.org/html/2607.26017v1#S5 — 5 Conclusion; https://arxiv.org/html/2607.26017v1#Sx1 — Limitations | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-26017 | complete |
| SF-2026-ARXIV-2607-26037 | RP-99a926b802e13ba7 | deep | arXiv:2607.26037v1 | SRC-ARXIV@arXiv:2607.26037v1 | https://arxiv.org/html/2607.26037v1#S4 — 4 Wonder World Model; https://arxiv.org/html/2607.26037v1#S4.SS4 — 4.4 Training Infrastructure and Model Details | https://arxiv.org/html/2607.26037v1#S5 — 5 Experiments | https://arxiv.org/html/2607.26037v1#S6 — 6 Conclusion | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-26037 | complete |
| SF-2026-ARXIV-2607-26040 | RP-25b592493cd195db | standard | arXiv:2607.26040v1 | SRC-ARXIV@arXiv:2607.26040v1 | https://arxiv.org/pdf/2607.26040v1#page=1 — PDF page 1; https://arxiv.org/pdf/2607.26040v1#page=10 — PDF page 10 | https://arxiv.org/pdf/2607.26040v1#page=1 — PDF page 1; https://arxiv.org/pdf/2607.26040v1#page=10 — PDF page 10 | https://arxiv.org/pdf/2607.26040v1#page=1 — PDF page 1; https://arxiv.org/pdf/2607.26040v1#page=10 — PDF page 10 | Not Disclosed — exact v1 exposes no uniquely versioned artifact locator used to enlarge the manuscript claim boundary. | claim:SF-2026-ARXIV-2607-26040 | complete |
| SF-2026-ARXIV-2607-26041 | RP-09a0459e107d7620 | standard | arXiv:2607.26041v1 | SRC-ARXIV@arXiv:2607.26041v1 | https://arxiv.org/pdf/2607.26041v1#page=1 — PDF page 1; https://arxiv.org/pdf/2607.26041v1#page=10 — PDF page 10 | https://arxiv.org/pdf/2607.26041v1#page=1 — PDF page 1; https://arxiv.org/pdf/2607.26041v1#page=10 — PDF page 10 | https://arxiv.org/pdf/2607.26041v1#page=1 — PDF page 1; https://arxiv.org/pdf/2607.26041v1#page=10 — PDF page 10 | Exact v1 links https://github.com/abhipi/DDB, https://huggingface.co/Hcompany/Holo-3.1-35B-A3B, https://huggingface.co/MiniMaxAI/MiniMax-M3; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-26041 | complete |
| SF-2026-ARXIV-2607-26052 | RP-9a0fbfbc83817476 | standard | arXiv:2607.26052v1 | SRC-ARXIV@arXiv:2607.26052v1 | https://arxiv.org/html/2607.26052v1#S4 — 4 Method: CARE | https://arxiv.org/html/2607.26052v1#A2 — Appendix B Detailed Experimental Setup; https://arxiv.org/html/2607.26052v1#A3 — Appendix C Additional Experiments | https://arxiv.org/html/2607.26052v1#A4 — Appendix D Extended Discussion; https://arxiv.org/html/2607.26052v1#S7 — 7 Discussion | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-26052 | complete |
| SF-2026-ARXIV-2607-26055 | RP-9d27d1c4f26c1a0a | standard | arXiv:2607.26055v1 | SRC-ARXIV@arXiv:2607.26055v1 | https://arxiv.org/html/2607.26055v1#A1 — Appendix A Implementation Details; https://arxiv.org/html/2607.26055v1#A1.SS3 — A.3 Training and Inference Algorithms | https://arxiv.org/html/2607.26055v1#A1.SS4 — A.4 Additional Reactivity Analysis; https://arxiv.org/html/2607.26055v1#S4 — 4 Experiments | https://arxiv.org/html/2607.26055v1#S5 — 5 Discussion; https://arxiv.org/html/2607.26055v1#Sx1 — Limitations | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-26055 | complete |
| SF-2026-ARXIV-2607-26056 | RP-97de244b8e4c72c4 | standard | arXiv:2607.26056v1 | SRC-ARXIV@arXiv:2607.26056v1 | https://arxiv.org/html/2607.26056v1#A3 — Appendix C Extended Method Derivations and Control Pseudocode; https://arxiv.org/html/2607.26056v1#A4 — Appendix D Design Selection and Ablation Logic | https://arxiv.org/html/2607.26056v1#A12 — Appendix L Evaluation Protocol Scope; https://arxiv.org/html/2607.26056v1#A2 — Appendix B Implementation and Evaluation Identities | https://arxiv.org/html/2607.26056v1#S6 — 6 Limitations; https://arxiv.org/html/2607.26056v1#S7 — 7 Conclusion | Exact v1 links https://github.com/DavidSunok/CLEAR-LeWM/releases/tag/v0.5.1, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-26056 | complete |

### Source Reviews

<!-- review:SF-2026-ARXIV-2607-24758:start -->
### Do Models Fake Alignment Without Clear Consequences?

<!-- claim:SF-2026-ARXIV-2607-24758:start -->Large language models are capable of recognizing evaluation contexts and altering their behavior to reflect evaluator expectations rather than typical deployment behaviors, a phenomenon known as alignment faking. The reasons why models fake alignment are not fully understood, however. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-24758:end -->

**为什么进入候选分母。** 摘要首要问题为“Large language models are capable of recognizing evaluation contexts and altering their behavior to reflect evaluator expectations rather than typical deployment behaviors, a phenomenon known as alignment faking.”；它改变执行安全的 trust boundary、guard 或 failure detection。

**机制与状态边界。** The reasons why models fake alignment are not fully understood, however.

**证据证明什么。** This suggests that evaluation-conditioned compliance gaps can occur with less instrumental scaffolding than previous scenarios have provided, and monitored behavior may be a poor indicator of how agents may behave in deployment.

**证据没有证明什么。** Even in the “routine deployment” condition of the scenario, we cannot rule out unintended evaluation awareness ( Needham et al., 2025 ) . 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.24758v1#A4.SS1 — D.1 Design; https://arxiv.org/html/2607.24758v1#S3 — 3 Methods。Evaluation：https://arxiv.org/html/2607.24758v1#A3 — Appendix C CoT analysis; https://arxiv.org/html/2607.24758v1#A3.SS3 — C.3 Evaluation-awareness and spontaneous consequence reasoning。Limitations / counterevidence：https://arxiv.org/html/2607.24758v1#S5 — 5 Discussion; https://arxiv.org/html/2607.24758v1#S6 — 6 Limitations。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 新的安全控制点降低特定失败，但会引入误拒绝、旁路、观测不足或模型/任务迁移问题。 论文自身的边界信号是：Even in the “routine deployment” condition of the scenario, we cannot rule out unintended evaluation awareness ( Needham et al., 2025 ) .

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`PLATFORM-SECURITY`；evidence-stage relation：`corrective_evidence`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-24758:end -->

<!-- review:SF-2026-ARXIV-2607-24759:start -->
### Beyond Memory: A Templated Substrate for Heterogeneous Collaborative Knowledge Work with LLM Agents

<!-- claim:SF-2026-ARXIV-2607-24759:start -->Research projects, educational efforts, and adjacent knowledge work accumulate findings, decisions, and reasoning that future collaborators rarely recover. The parts most useful to that work, including dead ends and walked-back claims, are routinely excluded from publications and shared code; future researchers re-attempt the same failures because no record survives. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-24759:end -->

**为什么进入候选分母。** 摘要首要问题为“Research projects, educational efforts, and adjacent knowledge work accumulate findings, decisions, and reasoning that future collaborators rarely recover.”；它把 context、memory、能力或进度变成持久且可验证的 agent state。

**机制与状态边界。** We present llm-wiki-memory-template, a reusable, agent-aware instantiation, and argue it is a substrate for heterogeneous collaborative knowledge work along three axes (multi-human, multi-AI-agent, multi-domain) with each axis supported by a distinct architectural element of the template (§4).

**证据证明什么。** We name failure-path preservation, agent honesty, and appropriation as cross-cutting sociotechnical properties of the artifact, not only of its technical mechanisms.

**证据没有证明什么。** 7 Limitations The four case studies, the three-axis architecture, and the cross-cutting findings together make claims the evidence does not yet fully establish. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.24759v1#Sx1.SSx4 — 4 Three-axis architecture; https://arxiv.org/html/2607.24759v1#Sx1.SSx8 — 5.3 Case C: In-progress multi-agent deployment (design report)。Evaluation：https://arxiv.org/html/2607.24759v1#Sx1 — Abstract; https://arxiv.org/html/2607.24759v1#Sx1.SSx1 — 1 Introduction。Limitations / counterevidence：https://arxiv.org/html/2607.24759v1#Sx1.SSx10 — 6 Findings and discussion; https://arxiv.org/html/2607.24759v1#Sx1.SSx11 — 7 Limitations。

**Artifact boundary。** Exact v1 links https://github.com/crcresearch/llm-wiki-memory-template, https://github.com/eugeniughelbur/obsidian-second-brain, https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 显式 agent state 改善恢复与控制，但增加状态陈旧、错误提交、跨轮污染和一致性责任。 论文自身的边界信号是：7 Limitations The four case studies, the three-axis architecture, and the cross-cutting findings together make claims the evidence does not yet fully establish.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`AGENT-MEMORY`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-24759:end -->

<!-- review:SF-2026-ARXIV-2607-24762:start -->
### Kernel Forge: An Agent Harness for LLM-based Generation and Optimization of CUDA Kernels

<!-- claim:SF-2026-ARXIV-2607-24762:start -->Machine learning models are increasingly embedded in everyday software, and most of their runtime is spent in a small set of compute kernels such as matrix multiplication, convolution, and normalization. Optimizing these kernels is one of the most direct ways to reduce latency and cost, but it has traditionally required expert engineers to hand-write low-level GPU code. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-24762:end -->

**为什么进入候选分母。** 摘要首要问题为“Machine learning models are increasingly embedded in everyday software, and most of their runtime is spent in a small set of compute kernels such as matrix multiplication, convolution, and normalization.”；它改变 observable、对照组、判定粒度或外推边界，可能修正既有评测结论。

**机制与状态边界。** We present Kernel Forge, an open-source, end-to-end agentic harness that accepts any unmodified PyTorch model in place.

**证据证明什么。** Optimizing these kernels is one of the most direct ways to reduce latency and cost, but it has traditionally required expert engineers to hand-write low-level GPU code.

**证据没有证明什么。** These findings suggest that agentic kernel optimization should be evaluated not only by whether it can generate fast standalone kernels, but also by how those kernels behave when applied inside real model executions with guarded replacement and workload-aware measurement. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.24762v1#S3 — 3 Kernel Forge System Design; https://arxiv.org/html/2607.24762v1#S4.SS1 — 4.1 Evaluation Methodology。Evaluation：https://arxiv.org/html/2607.24762v1#S4 — 4 Evaluation; https://arxiv.org/html/2607.24762v1#S4.SS1 — 4.1 Evaluation Methodology。Limitations / counterevidence：https://arxiv.org/html/2607.24762v1#S6 — 6 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/TheJoshBrod/KernelForge, https://github.com/meta-pytorch/BackendBench, https://github.com/meta-pytorch/KernelAgent; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：These findings suggest that agentic kernel optimization should be evaluated not only by whether it can generate fast standalone kernels, but also by how those kernels behave when applied inside real model executions with guarded replacement and workload-aware measurement.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`PLATFORM-EVALUATION-SYSTEM`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-24762:end -->

<!-- review:SF-2026-ARXIV-2607-24763:start -->
### CaRE Compute-aware Remasking Evaluation Protocol for Masked Diffusion Language Models

<!-- claim:SF-2026-ARXIV-2607-24763:start -->Masked diffusion language models (MDLMs) are advancing rapidly, yet the evaluation standards needed to reliably interpret their progress have not kept pace. Despite MDLMs becoming competitive with autoregressive language models, seven recent remasking papers evaluate under incompatible settings, varying nominal step counts, metrics, and sampling temperatures without jointly controlling these factors, rendering their strategy rankings largely incomparable and leaving open whether reported gains reflect algorithmic improvements or evaluation artifacts. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-24763:end -->

**为什么进入候选分母。** 摘要首要问题为“Masked diffusion language models (MDLMs) are advancing rapidly, yet the evaluation standards needed to reliably interpret their progress have not kept pace.”；它改变 observable、对照组、判定粒度或外推边界，可能修正既有评测结论。

**机制与状态边界。** We present CaRE, a compute-aware evaluation framework that audits MDLM remasking strategies by standardizing actual number of function evaluations (NFE), enforcing multi-metric reporting, and explicitly controlling stochasticity.

**证据证明什么。** These findings demonstrate that current MDLM evaluations can systematically conflate algorithmic improvements with hidden choices of compute and stochasticity.

**证据没有证明什么。** Exact v1 does not disclose a dedicated generalization or deployment guarantee beyond its stated evaluation scope. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.24763v1#A3.SS8 — C.8 LLaDA-MoE Cross-Architecture; https://arxiv.org/html/2607.24763v1#S2 — 2 The Ca re Framework and Protocol。Evaluation：https://arxiv.org/html/2607.24763v1#A3 — Appendix C Extended Experiments and Set Up; https://arxiv.org/html/2607.24763v1#A3.SS12 — C.12 Downstream Results (GSM8K)。Limitations / counterevidence：https://arxiv.org/html/2607.24763v1#A1 — Appendix A Ethical consideration and Future Work; https://arxiv.org/html/2607.24763v1#S5 — 5 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：Exact v1 does not disclose a dedicated generalization or deployment guarantee beyond its stated evaluation scope.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`MULTIMODAL-GENERATIVE-PARADIGMS`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-24763:end -->

<!-- review:SF-2026-ARXIV-2607-24765:start -->
### Measuring and Improving Behavioral Consistency in Large Language Models through Fact-Heuristic-Emotion State Enforcement

<!-- claim:SF-2026-ARXIV-2607-24765:start -->Large language models (LLMs) can give different answers to the same decision problem across runs, and reverse a decision when their own prior answer returns as context. We ask whether this instability can be measured and partially reduced without changing model weights. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-24765:end -->

**为什么进入候选分母。** 摘要首要问题为“Large language models (LLMs) can give different answers to the same decision problem across runs, and reverse a decision when their own prior answer returns as context.”；它改变 observable、对照组、判定粒度或外推边界，可能修正既有评测结论。

**机制与状态边界。** We ask whether this instability can be measured and partially reduced without changing model weights.

**证据证明什么。** We ask whether this instability can be measured and partially reduced without changing model weights.

**证据没有证明什么。** The broader implication is that future LLM evaluation should ask not only whether a model can produce a good answer once, but whether it can maintain a stable reasoning state when the same decision problem recurs. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.24765v1#Sx1.SSx5 — 3. Architecture and Intervention: Cognitive Kernel Model; https://arxiv.org/html/2607.24765v1#Sx1.SSx7 — 5. Experimental Design。Evaluation：https://arxiv.org/html/2607.24765v1#Sx1.SSx7 — 5. Experimental Design; https://arxiv.org/html/2607.24765v1#Sx1.SSx8 — 6. Results。Limitations / counterevidence：https://arxiv.org/html/2607.24765v1#Sx1.SSx10 — 8. Conclusion; https://arxiv.org/html/2607.24765v1#Sx1.SSx9 — 7. Discussion。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：The broader implication is that future LLM evaluation should ask not only whether a model can produce a good answer once, but whether it can maintain a stable reasoning state when the same decision problem recurs.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`PLATFORM-EVALUATION-SYSTEM`；evidence-stage relation：`corrective_evidence`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-24765:end -->

<!-- review:SF-2026-ARXIV-2607-24769:start -->
### LLM Scheming Inversely Scales with Pretraining Language Coverage

<!-- claim:SF-2026-ARXIV-2607-24769:start -->With the growing capabilities of frontier models, AI alignment becomes increasingly critical in high-risk deployment settings. While recent work has empirically demonstrated in-context scheming -- the covert pursuit of misaligned objectives while feigning alignment -- in frontier language models, most work has been performed exclusively in English, leaving a major gap in multilingual safety. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-24769:end -->

**为什么进入候选分母。** 摘要首要问题为“With the growing capabilities of frontier models, AI alignment becomes increasingly critical in high-risk deployment settings.”；它改变执行安全的 trust boundary、guard 或 failure detection。

**机制与状态边界。** We apply Petri, an open-source automated auditing framework, to Qwen3-30B-A3B to evaluate deceptive and scheming behaviors across multiple languages.

**证据证明什么。** Furthermore, we find that the effect of estimated pretraining language coverage is not uniform across scheming behaviors.

**证据没有证明什么。** 7 Limitations and Future Work In this work, our primary limitation is the scarcity of models that publicly disclose the proportions of languages used in their training datasets. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.24769v1#S3 — 3 Methodology。Evaluation：https://arxiv.org/html/2607.24769v1#S4 — 4 Experiments; https://arxiv.org/html/2607.24769v1#S5 — 5 Results。Limitations / counterevidence：https://arxiv.org/html/2607.24769v1#S7 — 7 Limitations and Future Work; https://arxiv.org/html/2607.24769v1#S6 — 6 Discussion。

**Artifact boundary。** Exact v1 links https://github.com/safety-research/petri, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 新的安全控制点降低特定失败，但会引入误拒绝、旁路、观测不足或模型/任务迁移问题。 论文自身的边界信号是：7 Limitations and Future Work In this work, our primary limitation is the scarcity of models that publicly disclose the proportions of languages used in their training datasets.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`PLATFORM-SECURITY`；evidence-stage relation：`corrective_evidence`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-24769:end -->

<!-- review:SF-2026-ARXIV-2607-24771:start -->
### RoCo-ACE: Rollout-Conditioned Online Distillation for Retention-Aware Knowledge Injection

<!-- claim:SF-2026-ARXIV-2607-24771:start -->Knowledge injection updates pretrained MLLMs with new factual or domain-specific knowledge, but fitting full authoritative answers can cause drift in non-updated behavior. Online distillation mitigates this drift by training on model-generated rollouts, yet uniform reference-conditioned distillation provides coarse supervision: it can under-emphasize reference-supported rollout tokens and supervise omitted facts only indirectly. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-24771:end -->

**为什么进入候选分母。** 摘要首要问题为“Knowledge injection updates pretrained MLLMs with new factual or domain-specific knowledge, but fitting full authoritative answers can cause drift in non-updated behavior.”；它改变训练信号、capacity 或 update ownership，而非只报告任务精度。

**机制与状态边界。** We introduce RoCo-ACE, a rollout-conditioned online distillation objective for knowledge injection.

**证据证明什么。** Across three knowledge-injection settings, six retention benchmarks, multiple baselines, and multiple base models, RoCo-ACE achieves the best injected-knowledge accuracy among compared methods while keeping evaluated retention close to the base model.

**证据没有证明什么。** This distinction matters because many regressions are not caused by learning a new fact itself, but by repeatedly training on long, narrow, stylistically similar answers. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.24771v1#S3 — 3 Method; https://arxiv.org/html/2607.24771v1#A10 — Appendix J Model and Baseline Details。Evaluation：https://arxiv.org/html/2607.24771v1#A2 — Appendix B Full Baseline Comparison Results; https://arxiv.org/html/2607.24771v1#A3 — Appendix C Qualitative Analysis。Limitations / counterevidence：https://arxiv.org/html/2607.24771v1#A7 — Appendix G Additional Discussion on Retention Scope and Reference Quality; https://arxiv.org/html/2607.24771v1#S5 — 5 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更密集或更定向的训练信号改善样本效率，但会增加 verifier 偏差、分布迁移和优化耦合。 论文自身的边界信号是：This distinction matters because many regressions are not caused by learning a new fact itself, but by repeatedly training on long, narrow, stylistically similar answers.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`TRAIN-SFT`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-24771:end -->

<!-- review:SF-2026-ARXIV-2607-24776:start -->
### JKO-RAG: Distributional Retrieval as Wasserstein Free-Energy Gradient Flow

<!-- claim:SF-2026-ARXIV-2607-24776:start -->RAG pipelines return a \emph{ranked list} of passages. We argue this is a mismatch: the downstream language model conditions on a \emph{set}, and the selection problem is fundamentally geometric. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-24776:end -->

**为什么进入候选分母。** 摘要首要问题为“RAG pipelines return a \emph{ranked list} of passages.”；它把 context、memory、能力或进度变成持久且可验证的 agent state。

**机制与状态边界。** We propose \jko, which frames reranking as minimising a free-energy functional $F(p)=\text{relevance}+\text{entropy}+\text{redundancy}$ under Wasserstein-2 gradient flow via the Jordan--Kinderlehrer--Otto proximal scheme.

**证据证明什么。** Across five BEIR benchmarks, \jko\ outperforms the cross-encoder on all five; the decisive advantage is robustness -- 22--38\% more stable under paraphrase, $2\times$ fewer leaked distractors.

**证据没有证明什么。** The theory isolates the entire geometric advantage to a single term (the proximal Hessian, Theorem 1 ), characterises that term’s cross-cluster curvature ( Proposition 1 ), and predicts a monotone -dependence of the stability gap ( Corollary 1 ) that we confirm directly. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.24776v1#S3 — 3 The JKO-RAG Framework。Evaluation：https://arxiv.org/html/2607.24776v1#S6 — 6 Experiments; https://arxiv.org/html/2607.24776v1#S6.SS2 — 6.2 Main retrieval results。Limitations / counterevidence：https://arxiv.org/html/2607.24776v1#S8 — 8 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/MurariAmbati/jko-rag, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 显式 agent state 改善恢复与控制，但增加状态陈旧、错误提交、跨轮污染和一致性责任。 论文自身的边界信号是：The theory isolates the entire geometric advantage to a single term (the proximal Hessian, Theorem 1 ), characterises that term’s cross-cluster curvature ( Proposition 1 ), and predicts a monotone -dependence of the stability gap ( Corollary 1 ) that we confirm directly.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`AGENT-RAG`；evidence-stage relation：`alternative_branch`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-24776:end -->

<!-- review:SF-2026-ARXIV-2607-24780:start -->
### LivingArena: Do LLMs Know What Other LLMs Don't? Peer-Probing as Scalable Evaluation

<!-- claim:SF-2026-ARXIV-2607-24780:start -->Fixed benchmarks are costly to renew and cannot adapt their questions to model-specific failures. We ask whether LLMs can instead discover one another's weaknesses and turn those observations into an evaluation process. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-24780:end -->

**为什么进入候选分母。** 摘要首要问题为“Fixed benchmarks are costly to renew and cannot adapt their questions to model-specific failures.”；它改变 observable、对照组、判定粒度或外推边界，可能修正既有评测结论。

**机制与状态边界。** To study this question, we introduce \textbf{LivingArena}, an automated peer-probing framework in which models take turns testing one another.

**证据证明什么。** These findings show that peer probing can reveal persistent model-specific weaknesses while separately evaluating answering and reliable test construction.

**证据没有证明什么。** First, an evaluator ceiling : peer probing is bounded by the participating models, so a blind spot shared by all of them cannot be probed—a fundamental limit of peer-based scalable evaluation, analogous to weak-to-strong oversight. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.24780v1#S3 — 3 The LivingArena Framework。Evaluation：https://arxiv.org/html/2607.24780v1#S4 — 4 Experimental Setup; https://arxiv.org/html/2607.24780v1#S5 — 5 Results。Limitations / counterevidence：https://arxiv.org/html/2607.24780v1#S6 — 6 Conclusion; https://arxiv.org/html/2607.24780v1#Sx1 — Limitations。

**Artifact boundary。** Exact v1 links https://github.com/galaxyChen/LivingArena, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：First, an evaluator ceiling : peer probing is bounded by the participating models, so a blind spot shared by all of them cannot be probed—a fundamental limit of peer-based scalable evaluation, analogous to weak-to-strong oversight.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`PLATFORM-EVALUATION-SYSTEM`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-24780:end -->

<!-- review:SF-2026-ARXIV-2607-24781:start -->
### Three Sides of Retrieval: Factorial Evidence for Document-Side, Query-Side, and Answer-Side Complementarity in RAG

<!-- claim:SF-2026-ARXIV-2607-24781:start -->RAG systems rely on chunking, which destroys structural information in documents. Existing heading-based retrieval (Jeong et al., 2025) requires multiple LLM calls per document and returns sub-chunks within matched sections. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-24781:end -->

**为什么进入候选分母。** 摘要首要问题为“RAG systems rely on chunking, which destroys structural information in documents.”；它改变 observable、对照组、判定粒度或外推边界，可能修正既有评测结论。

**机制与状态边界。** RAG systems rely on chunking, which destroys structural information in documents.

**证据证明什么。** The contribution is both methodological (a new zero-LLM-cost retrieval algorithm) and empirical: factorial evidence that document-side, query-side, and answer-side enhancements are complementary, a three-way interaction not previously studied.

**证据没有证明什么。** Second, heading-level matching may not always select the right cousin or coarse section when the heading titles are only loosely related to the query terms. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/pdf/2607.24781v1#page=1 — PDF page 1; https://arxiv.org/pdf/2607.24781v1#page=10 — PDF page 10。Evaluation：https://arxiv.org/pdf/2607.24781v1#page=1 — PDF page 1; https://arxiv.org/pdf/2607.24781v1#page=10 — PDF page 10。Limitations / counterevidence：https://arxiv.org/pdf/2607.24781v1#page=1 — PDF page 1; https://arxiv.org/pdf/2607.24781v1#page=10 — PDF page 10。

**Artifact boundary。** Not Disclosed — exact v1 exposes no uniquely versioned artifact locator used to enlarge the manuscript claim boundary.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：Second, heading-level matching may not always select the right cousin or coarse section when the heading titles are only loosely related to the query terms.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`AGENT-RAG`；evidence-stage relation：`corrective_evidence`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-24781:end -->

<!-- review:SF-2026-ARXIV-2607-24787:start -->
### SpecPrefetch: Parameter-Efficient Expert Prefetching for Sparse MoE Foundation Models

<!-- claim:SF-2026-ARXIV-2607-24787:start -->Sparse Mixture-of-Experts (MoE) models expand foundation model capacity through conditional expert activation, but their full expert pools remain difficult to deploy under limited accelerator memory. Although expert offloading alleviates memory pressure by moving inactive experts to host memory or storage, it introduces a routing-dependent transfer bottleneck: required experts are known only after native top-\(K\) routing, which serializes routing, expert loading, and expert execution during inference. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-24787:end -->

**为什么进入候选分母。** 摘要首要问题为“Sparse Mixture-of-Experts (MoE) models expand foundation model capacity through conditional expert activation, but their full expert pools remain difficult to deploy under limited accelerator memory.”；它改变推理期状态放置、数据移动、执行控制或实时 SLO。

**机制与状态边界。** To address this bottleneck, we propose SpecPrefetch, a parameter-efficient prefetching framework for offloaded MoE inference.

**证据证明什么。** On a Snapdragon 8 Elite device, SpecPrefetch further improves decoding throughput by up to \(20\%\) over a compute-optimized offloading runtime, demonstrating practical benefits for storage-constrained MoE deployment.

**证据没有证明什么。** A correctly predicted expert improves latency only when its transfer would otherwise be exposed on the critical path; therefore, the speedup depends on cache state, storage bandwidth, transfer-compute overlap, and runtime support for asynchronous loading. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.24787v1#S3 — 3 Method; https://arxiv.org/html/2607.24787v1#S2.SS1 — 2.1 Sparse MoE Foundation Models。Evaluation：https://arxiv.org/html/2607.24787v1#S4 — 4 Experiment; https://arxiv.org/html/2607.24787v1#S4.SS1 — 4.1 Experimental Setup。Limitations / counterevidence：https://arxiv.org/html/2607.24787v1#S5 — 5 Conclusion; https://arxiv.org/html/2607.24787v1#S7 — 7 Limitation。

**Artifact boundary。** Exact v1 links https://github.com/wei390/SpecPrefetch, https://huggingface.co/datasets/facebook/textvqa, https://www.microsoft.com/en-us/research/project/figureqa-dataset/download/; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更激进的缓存、迁移、并行或专用执行会换取吞吐/时延，同时增加配置依赖、资源压力与回退路径。 论文自身的边界信号是：A correctly predicted expert improves latency only when its transfer would otherwise be exposed on the critical path; therefore, the speedup depends on cache state, storage bandwidth, transfer-compute overlap, and runtime support for asynchronous loading.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`MODEL-MOE`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-24787:end -->

<!-- review:SF-2026-ARXIV-2607-24788:start -->
### GLIDE: Guided Layerwise Hybrid Attention for Efficient LLM Inference

<!-- claim:SF-2026-ARXIV-2607-24788:start -->As Large Language Models scale to increasingly long contexts, the memory I/O and computational overhead of the Key-Value (KV) cache during decoding emerges as the primary throughput bottleneck. To address this, we propose GLIDE, a Guided Layerwise Hybrid Attention that strategically integrates sliding-window softmax attention with linear recurrent aggregation. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-24788:end -->

**为什么进入候选分母。** 摘要首要问题为“As Large Language Models scale to increasingly long contexts, the memory I/O and computational overhead of the Key-Value (KV) cache during decoding emerges as the primary throughput bottleneck.”；它改变推理期状态放置、数据移动、执行控制或实时 SLO。

**机制与状态边界。** To address this, we propose GLIDE, a Guided Layerwise Hybrid Attention that strategically integrates sliding-window softmax attention with linear recurrent aggregation.

**证据证明什么。** Empirical evaluations demonstrate the GLIDE achieves superior performance-efficiency tradeoffs, reducing end-to-end latency for long-context generation without compromising quality.

**证据没有证明什么。** V Limitations & Future Works While Glide demonstrates substantial improvements in decoding efficiency through selective KV cache retrieval and layer-wise hybrid attention, several limitations remain. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.24788v1#S2.SS4 — II-D Parameter-Efficient Hybrid Architecture; https://arxiv.org/html/2607.24788v1#S3 — III Methodology。Evaluation：https://arxiv.org/html/2607.24788v1#S4 — IV Experiments; https://arxiv.org/html/2607.24788v1#S4.SS1 — IV-A Experimental Setup。Limitations / counterevidence：https://arxiv.org/html/2607.24788v1#S5 — V Limitations & Future Works; https://arxiv.org/html/2607.24788v1#S4.SS2 — IV-B Results and Discussion。

**Artifact boundary。** Exact v1 links https://github.com/tatsu-lab/stanford_alpaca, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更激进的缓存、迁移、并行或专用执行会换取吞吐/时延，同时增加配置依赖、资源压力与回退路径。 论文自身的边界信号是：V Limitations & Future Works While Glide demonstrates substantial improvements in decoding efficiency through selective KV cache retrieval and layer-wise hybrid attention, several limitations remain.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`INFER-DECODE`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-24788:end -->

<!-- review:SF-2026-ARXIV-2607-24794:start -->
### Reasoning with Memory: A Temporal Granularity-Adaptive Framework for Training-Free Long Video Understanding

<!-- claim:SF-2026-ARXIV-2607-24794:start -->While Multimodal Large Language Models (MLLMs) demonstrate superior generalization in fundamental video tasks, restricted context windows limit their long video understanding. To accommodate this constraint, models typically resort to keyframe selection. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-24794:end -->

**为什么进入候选分母。** 摘要首要问题为“While Multimodal Large Language Models (MLLMs) demonstrate superior generalization in fundamental video tasks, restricted context windows limit their long video understanding.”；它把 context、memory、能力或进度变成持久且可验证的 agent state。

**机制与状态边界。** In this paper, we propose ReMem, a temporal granularity-adaptive keyframe selection framework for training-free LongVideoQA.

**证据证明什么。** While Multimodal Large Language Models (MLLMs) demonstrate superior generalization in fundamental video tasks, restricted context windows limit their long video understanding.

**证据没有证明什么。** However, this increase in total latency is a deliberate and highly rewarding accuracy-efficiency trade-off. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.24794v1#S3 — 3 Method; https://arxiv.org/html/2607.24794v1#S2.SS1 — 2.1 Video Large Language Models。Evaluation：https://arxiv.org/html/2607.24794v1#S4 — 4 Experiments; https://arxiv.org/html/2607.24794v1#S4.SS1 — 4.1 Experimental Setup。Limitations / counterevidence：https://arxiv.org/html/2607.24794v1#S4.SS7 — 4.7 Efficiency Analysis and Trade-off Discussion; https://arxiv.org/html/2607.24794v1#S5 — 5 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/jinlab-imvr/ReMem, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 显式 agent state 改善恢复与控制，但增加状态陈旧、错误提交、跨轮污染和一致性责任。 论文自身的边界信号是：However, this increase in total latency is a deliberate and highly rewarding accuracy-efficiency trade-off.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`MULTIMODAL-REPRESENTATION`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-24794:end -->

<!-- review:SF-2026-ARXIV-2607-24798:start -->
### Prediction Is Not Memory: Dual-Timescale Gated Profile Writing for Persistent User Modeling

<!-- claim:SF-2026-ARXIV-2607-24798:start -->Persistent user profiles increasingly serve as reusable memory in recommender systems, but common update pipelines conflate two decisions: predicting an interaction and deciding whether it should persist in the profile. After an interaction is observed, many systems treat it as evidence for updating durable user state. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-24798:end -->

**为什么进入候选分母。** 摘要首要问题为“Persistent user profiles increasingly serve as reusable memory in recommender systems, but common update pipelines conflate two decisions: predicting an interaction and deciding whether it should persist in the profile.”；它把 context、memory、能力或进度变成持久且可验证的 agent state。

**机制与状态边界。** After an interaction is observed, many systems treat it as evidence for updating durable user state.

**证据证明什么。** SPW-Gate reduces far hurt to about 14.5% while preserving about 77% write coverage.

**证据没有证明什么。** Final evaluation uses far-future alignment and far hurt. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.24798v1#Sx1 — Introduction; https://arxiv.org/html/2607.24798v1#Sx2 — Related Work。Evaluation：https://arxiv.org/html/2607.24798v1#Sx5 — Experiments; https://arxiv.org/html/2607.24798v1#Sx5.SSx2 — Evaluation Questions。Limitations / counterevidence：https://arxiv.org/html/2607.24798v1#Sx3.SSx3 — Near-Future Write-Risk Label; https://arxiv.org/html/2607.24798v1#Sx6 — Limitations and Claim Scope。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 显式 agent state 改善恢复与控制，但增加状态陈旧、错误提交、跨轮污染和一致性责任。 论文自身的边界信号是：Final evaluation uses far-future alignment and far hurt.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`AGENT-MEMORY`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-24798:end -->

<!-- review:SF-2026-ARXIV-2607-24800:start -->
### When Thinking Before Retrieval Hurts: TraceBound Diagnostics for Adaptive Knowledge-Graph Retrieval

<!-- claim:SF-2026-ARXIV-2607-24800:start -->Adaptive retrieval promises to make knowledge-graph question answering more robust by letting a controller search, inspect neighborhoods, revise actions, and stop when evidence is sufficient. We study this premise by introducing TraceBound, a lightweight profile- and trace-conditioned diagnostic protocol for an ARK-style retriever on text-rich knowledge graphs. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-24800:end -->

**为什么进入候选分母。** 摘要首要问题为“Adaptive retrieval promises to make knowledge-graph question answering more robust by letting a controller search, inspect neighborhoods, revise actions, and stop when evidence is sufficient.”；它改变 observable、对照组、判定粒度或外推边界，可能修正既有评测结论。

**机制与状态边界。** We study this premise by introducing TraceBound, a lightweight profile- and trace-conditioned diagnostic protocol for an ARK-style retriever on text-rich knowledge graphs.

**证据证明什么。** Across STaRK validation and held-out subsets, the added conditioning improves inspectability but consistently reduces retrieval quality under open-weight controllers.

**证据没有证明什么。** Exact v1 does not disclose a dedicated generalization or deployment guarantee beyond its stated evaluation scope. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.24800v1#S3 — 3 TraceBound: Methodology and Implementation Details; https://arxiv.org/html/2607.24800v1#S3.SS5 — 3.5 Design invariants。Evaluation：https://arxiv.org/html/2607.24800v1#S4 — 4 Experimental Setup; https://arxiv.org/html/2607.24800v1#S5 — 5 Results。Limitations / counterevidence：https://arxiv.org/html/2607.24800v1#S6 — 6 Discussion; https://arxiv.org/html/2607.24800v1#S6.SS4 — 6.4 Failure taxonomy and corrective policy targets。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：Exact v1 does not disclose a dedicated generalization or deployment guarantee beyond its stated evaluation scope.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`AGENT-RAG`；evidence-stage relation：`corrective_evidence`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-24800:end -->

<!-- review:SF-2026-ARXIV-2607-24805:start -->
### Forgetting Is Not a Fix: Path Dependence in Sequential Engram Editing

<!-- claim:SF-2026-ARXIV-2607-24805:start -->AI Engram (Kwon et al., 2026) formalizes the four engram criteria of neuroscience as a constrained inverse problem in weight space and solves it closed-form: concept-specific memory traces become linear objects that can be extracted once and combined arithmetically. Appendix F states the Compositional Memory States Hypothesis: edited models live on "a commutative manifold where the integration of A and B reaches a consistent equilibrium regardless of the learning sequence." The evidence base is single and paired edits -- in materials terms, single-cycle tests, in which fatigue accumulation is structurally invisible. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-24805:end -->

**为什么进入候选分母。** 摘要首要问题为“AI Engram (Kwon et al., 2026) formalizes the four engram criteria of neuroscience as a constrained inverse problem in weight space and solves it closed-form: concept-specific memory traces become linear objects that can be extracted once and combined arithmetically.”；它提出可跨 workload 讨论的表示、状态或计算机制，并暴露旧方案边界。

**机制与状态边界。** Four findings replicate across all three: (1) zero-shot composition and sequential re-calibrated editing diverge by 61-71% of the edit magnitude; (2) cut order is not interchangeable, and the effect scales with concept overlap -- in one charge the order of cutting two Paris landmarks decides whether an uninvolved third concept survives; (3) the survivors' layer-input covariances -- the method's own sufficient statistics, read as strain gauges -- drift monotonically with every further cut, in every surviving concept, in every charge; (4) erased knowledge partially returns under subsequent unrelated cuts.

**证据证明什么。** Appendix F's commutative-manifold hypothesis is thereby falsified for sequential editing; the single-edit results of the original paper are untouched.

**证据没有证明什么。** Conclusion The original paper closes: “Future work may examine the temporal dynamics of engrams in continual learning.” Examined, in the smallest honest version: the temporal dynamics are path-dependent, non-commutative in proportion to concept overlap, and cumulative in the survivors’ own sufficient statistics — in all three charges, on the authors’ implementation, at the edit strength they selected for LLM unlearning. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.24805v1#Sx1 — Abstract; https://arxiv.org/html/2607.24805v1#Sx2 — 1. Introduction。Evaluation：https://arxiv.org/html/2607.24805v1#Sx5 — 4. Results。Limitations / counterevidence：https://arxiv.org/html/2607.24805v1#Sx8 — 7. Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/FerdinandSchessl/engram-seq-note-companion, https://github.com/jeakwon/ai-engram, https://github.com/arXiv/html_feedback/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 新表示或状态机制扩大能力边界，但带来额外训练、状态管理、稳定性或泛化假设。 论文自身的边界信号是：Conclusion The original paper closes: “Future work may examine the temporal dynamics of engrams in continual learning.” Examined, in the smallest honest version: the temporal dynamics are path-dependent, non-commutative in proportion to concept overlap, and cumulative in the survivors’ own sufficient statistics — in all three charges, on the authors’ implementation, at the edit strength they selected for LLM unlearning.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`AGENT-MEMORY`；evidence-stage relation：`corrective_evidence`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-24805:end -->

<!-- review:SF-2026-ARXIV-2607-24821:start -->
### AVE-Compass: Towards Holistic Evaluation for Audio-Video Editing Abilities

<!-- claim:SF-2026-ARXIV-2607-24821:start -->While instruction-based video editing has advanced rapidly, real-world videos contain tightly coupled audio and visual signals, and editing one modality often requires coordinated changes in the other. Existing benchmarks primarily evaluate visual transformations on silent clips or isolated audio editing, leaving complex audio-visual editing and cross-modal consistency underexplored. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-24821:end -->

**为什么进入候选分母。** 摘要首要问题为“While instruction-based video editing has advanced rapidly, real-world videos contain tightly coupled audio and visual signals, and editing one modality often requires coordinated changes in the other.”；它改变 observable、对照组、判定粒度或外推边界，可能修正既有评测结论。

**机制与状态边界。** We introduce AVE-Compass, a comprehensive benchmark with 145 curated source videos, 196 audio-visually coupled editing instructions, and 2,688 fine-grained checklist items.

**证据证明什么。** We further propose AVE-Agent, a modular agent framework that decomposes complex instructions into dependent subtasks and iteratively improves editing results through self-reflection and evaluator feedback.

**证据没有证明什么。** AVE-Agent additionally depends on third-party tools whose behaviour may shift over time, which can affect long-term reproducibility. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.24821v1#S3.SS2 — 3.2 Evaluation Methodology; https://arxiv.org/html/2607.24821v1#A2 — Appendix B Implementation Details of AVE-Agent。Evaluation：https://arxiv.org/html/2607.24821v1#S3 — 3 AVE-Compass: Benchmark and Evaluation; https://arxiv.org/html/2607.24821v1#A1 — Appendix A Benchmark Construction Details。Limitations / counterevidence：https://arxiv.org/html/2607.24821v1#A5 — Appendix E Limitations; https://arxiv.org/html/2607.24821v1#S6 — 6 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/NJU-LINK/AVE-Compass, https://huggingface.co/datasets/NJU-LINK/AVE-Compass, https://github.com/arXiv/html_feedback/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：AVE-Agent additionally depends on third-party tools whose behaviour may shift over time, which can affect long-term reproducibility.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`MULTIMODAL-GENERATIVE-PARADIGMS`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-24821:end -->

<!-- review:SF-2026-ARXIV-2607-24841:start -->
### Neuromorphic Diffusion Language Models: Addressing Compute and Memory Bottlenecks via Sparsity and Block Denoising

<!-- claim:SF-2026-ARXIV-2607-24841:start -->Autoregressive (AR) large language models (LLMs) are inherently inefficient at inference time because each generated token requires accessing the full set of model parameters, leading to low operational intensity and high energy consumption. Masked diffusion language models (MDLMs) partially address this limitation for memory-bound settings by allowing multiple tokens to be generated per parameter access. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-24841:end -->

**为什么进入候选分母。** 摘要首要问题为“Autoregressive (AR) large language models (LLMs) are inherently inefficient at inference time because each generated token requires accessing the full set of model parameters, leading to low operational intensity and high energy consumption.”；它改变资源计量、分配、路由或迁移的控制权与约束。

**机制与状态边界。** Masked diffusion language models (MDLMs) partially address this limitation for memory-bound settings by allowing multiple tokens to be generated per parameter access.

**证据证明什么。** Experimental results on translation tasks show that, thanks to spike-induced sparsity, N-MDLMs achieve substantial improvements in energy efficiency and throughput even in compute-bound platforms for which MDLMs would fail to improve over AR-LLMs.

**证据没有证明什么。** The gains are particularly significant in compute-bound regimes, where plain MDLMs provide limited improvement. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.24841v1#S3.SS1 — III-A Architecture; https://arxiv.org/html/2607.24841v1#S2.SS1 — II-A Autoregressive vs. Masked Diffusion Language Models。Evaluation：https://arxiv.org/html/2607.24841v1#S4 — IV Performance Analysis; https://arxiv.org/html/2607.24841v1#S5 — V Experiments。Limitations / counterevidence：https://arxiv.org/html/2607.24841v1#S6 — VI Conclusions。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 动态资源控制提高利用率，但增加测量误差、迁移开销、租户公平和控制稳定性问题。 论文自身的边界信号是：The gains are particularly significant in compute-bound regimes, where plain MDLMs provide limited improvement.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`MULTIMODAL-GENERATIVE-PARADIGMS`；evidence-stage relation：`alternative_branch`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-24841:end -->

<!-- review:SF-2026-ARXIV-2607-24850:start -->
### SearchArt: Training Long-Horizon Search Agent with Scalable Synthetic and Verified Task

<!-- claim:SF-2026-ARXIV-2607-24850:start -->Recent advances in large language models (LLMs) have enabled search agents to autonomously tackle complex tasks across extended search and reasoning horizons. However, training effective search agents remains challenging due to the lack of scalable and long-horizon tasks, and the difficulty of evaluating and correcting intermediate reasoning and tool-use behaviors. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-24850:end -->

**为什么进入候选分母。** 摘要首要问题为“Recent advances in large language models (LLMs) have enabled search agents to autonomously tackle complex tasks across extended search and reasoning horizons.”；它改变训练信号、capacity 或 update ownership，而非只报告任务精度。

**机制与状态边界。** We introduce SearchArt, a scalable framework for training long-horizon search agents through verification-driven task synthesis and a multi-stage post-training pipeline.

**证据证明什么。** Experimental results demonstrate that, with only (Qwen3.5-) 27B parameters, SearchArt scores 74.39 on BrowseComp-ZH, 70.06 on BrowseComp, and 52.55 on Deepresearch-bench, matching or surpassing frontier closed-source agents on both deepsearch and deepresearch benchmarks.

**证据没有证明什么。** SearchArt addresses several central challenges in search-agent training, including the limited availability of high-quality QA pairs, the high cost of manually annotated interaction trajectories, and the difficulty of providing reliable supervision for intermediate retrieval and reasoning behaviors. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.24850v1#S3.SS4 — 3.4 Composite Reward Design; https://arxiv.org/html/2607.24850v1#S4 — 4 SearchArt Harness Design。Evaluation：https://arxiv.org/html/2607.24850v1#S5.SS2 — 5.2 Experimental Results; https://arxiv.org/html/2607.24850v1#S5 — 5 Experiments。Limitations / counterevidence：https://arxiv.org/html/2607.24850v1#S7 — 7 Conclusion; https://arxiv.org/html/2607.24850v1#S8 — 8 Future Work。

**Artifact boundary。** Exact v1 links https://huggingface.co/MiniMaxAI/MiniMax-M2.5, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更密集或更定向的训练信号改善样本效率，但会增加 verifier 偏差、分布迁移和优化耦合。 论文自身的边界信号是：SearchArt addresses several central challenges in search-agent training, including the limited availability of high-quality QA pairs, the high cost of manually annotated interaction trajectories, and the difficulty of providing reliable supervision for intermediate retrieval and reasoning behaviors.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`AGENT-WORKFLOW`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-24850:end -->

<!-- review:SF-2026-ARXIV-2607-24859:start -->
### The Mirage of LLM Guardrails: A Case Study in AI-Assisted Medical Note Manipulation

<!-- claim:SF-2026-ARXIV-2607-24859:start -->The rapid deployment of large language models (LLMs) in healthcare settings makes the reliability of their built-in guardrails against malicious queries a question of urgent practical consequence. Yet the robustness of these mechanisms against deliberate misuse (in the healthcare context) remains poorly understood. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-24859:end -->

**为什么进入候选分母。** 摘要首要问题为“The rapid deployment of large language models (LLMs) in healthcare settings makes the reliability of their built-in guardrails against malicious queries a question of urgent practical consequence.”；它改变执行安全的 trust boundary、guard 或 failure detection。

**机制与状态边界。** Second, we conduct a systematic empirical evaluation of LLM guardrail robustness for medical note manipulation.

**证据证明什么。** Our experimental results reveal substantial weaknesses and inconsistencies in contemporary commercial LLM guardrails, including low refusal rates for several model families.

**证据没有证明什么。** Limitations and Future Work Due to ethical and privacy considerations regarding the use of real medical documents, we relied exclusively on publicly available doctors’ note templates collected from online sources rather than authentic clinical records. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.24859v1#Sx3 — Methodology。Evaluation：https://arxiv.org/html/2607.24859v1#Sx4 — Experimental Results; https://arxiv.org/html/2607.24859v1#Sx4.SSx1 — Experimental Setup。Limitations / counterevidence：https://arxiv.org/html/2607.24859v1#Sx5 — Discussion and Conclusion; https://arxiv.org/html/2607.24859v1#Sx6 — Limitations and Future Work。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 新的安全控制点降低特定失败，但会引入误拒绝、旁路、观测不足或模型/任务迁移问题。 论文自身的边界信号是：Limitations and Future Work Due to ethical and privacy considerations regarding the use of real medical documents, we relied exclusively on publicly available doctors’ note templates collected from online sources rather than authentic clinical records.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`PLATFORM-SECURITY`；evidence-stage relation：`corrective_evidence`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-24859:end -->

<!-- review:SF-2026-ARXIV-2607-24866:start -->
### The Missing Layer: Specification Infrastructure for AI Oversight

<!-- claim:SF-2026-ARXIV-2607-24866:start -->Interpretability, formal methods, security engineering, evaluation methodology, and reinforcement-learning safety each produce substantial work, but the resulting artifacts do not compose into deployable oversight: every team fielding an agentic system builds its own audit schema, policy dialect, monitoring stack, and escalation path, mostly reinventions of patterns understood elsewhere. We diagnose this as a coordination gap, not a research gap, and propose a two-axis taxonomy: five technical layers (Legibility, Specification, Mediation, Evaluation, Escalation) crossed with six concerns spanning alignment, robustness, adversarial defense, security, governance, and accountability, populating the resulting 5x6 matrix with existing work. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-24866:end -->

**为什么进入候选分母。** 摘要首要问题为“AI safety has a missing layer.”；它改变执行安全的 trust boundary、guard 或 failure detection。

**机制与状态边界。** Interpretability, formal methods, security engineering, evaluation methodology, and reinforcement-learning safety each produce substantial work, but the resulting artifacts do not compose into deployable oversight: every team fielding an agentic system builds its own audit schema, policy dialect, monitoring stack, and escalation path, mostly reinventions of patterns understood elsewhere.

**证据证明什么。** As evidence, we introduce CARMA, a Layer 2 prototype for autonomous ETL agents in which one specification drives enforcement, evaluation, and escalation, with every decision traceable to a versioned specification, naming what AI oversight is missing and giving independent teams principles to build the missing pieces so they compose.

**证据没有证明什么。** 10 Discussion and Limitations We are deliberate about what is a diagnostic contribution and what is a claim about mechanism. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.24866v1#S7 — 7 Reference Architecture for Layer 2 Systems; https://arxiv.org/html/2607.24866v1#S5 — 5 Six Design Principles for Layer 2 Infrastructure。Evaluation：https://arxiv.org/html/2607.24866v1#S1 — 1 Introduction; https://arxiv.org/html/2607.24866v1#S2 — 2 Related Work。Limitations / counterevidence：https://arxiv.org/html/2607.24866v1#S10 — 10 Discussion and Limitations; https://arxiv.org/html/2607.24866v1#S11 — 11 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 新的安全控制点降低特定失败，但会引入误拒绝、旁路、观测不足或模型/任务迁移问题。 论文自身的边界信号是：10 Discussion and Limitations We are deliberate about what is a diagnostic contribution and what is a claim about mechanism.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`PLATFORM-SECURITY`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-24866:end -->

<!-- review:SF-2026-ARXIV-2607-24875:start -->
### FinAbstain: Uncertainty-Calibrated Multimodal RAG for Selective Financial Forecasting

<!-- claim:SF-2026-ARXIV-2607-24875:start -->Large language models (LLMs) can synthesize financial narratives but may express high confidence when evidence is sparse, stale, or contradictory. This failure is especially consequential in forecasting, where filings, news, prices, volume, and technical signals can disagree. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-24875:end -->

**为什么进入候选分母。** 摘要首要问题为“Large language models (LLMs) can synthesize financial narratives but may express high confidence when evidence is sparse, stale, or contradictory.”；它改变 observable、对照组、判定粒度或外推边界，可能修正既有评测结论。

**机制与状态边界。** We present FinAbstain, a research framework for uncertainty-calibrated multimodal retrieval-augmented generation (RAG) with selective prediction.

**证据证明什么。** These results illustrate the intended hypothesis: calibrated abstention may trade coverage for lower selective error and drawdown.

**证据没有证明什么。** Conformal validity may degrade under temporal dependence, and simulated results cannot establish economic benefit. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.24875v1#S4 — IV Proposed FinAbstain Framework; https://arxiv.org/html/2607.24875v1#S5 — V Experimental Methodology。Evaluation：https://arxiv.org/html/2607.24875v1#S5 — V Experimental Methodology; https://arxiv.org/html/2607.24875v1#S6 — VI Results and Discussion。Limitations / counterevidence：https://arxiv.org/html/2607.24875v1#S6 — VI Results and Discussion; https://arxiv.org/html/2607.24875v1#S6.SS3 — VI-C Limitations and Reproducibility Risks。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：Conformal validity may degrade under temporal dependence, and simulated results cannot establish economic benefit.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`AGENT-RAG`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-24875:end -->

<!-- review:SF-2026-ARXIV-2607-24882:start -->
### Agent Retrieval Bench: Evaluating Repository Context Retrieval for Coding Agents

<!-- claim:SF-2026-ARXIV-2607-24882:start -->Modern coding agents are usually evaluated by whether they eventually produce a correct patch, but patch generation depends on an earlier context-acquisition stage: finding the repository files needed for the task. We introduce Agent Retrieval Bench, a file-level benchmark for this upstream retrieval problem. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-24882:end -->

**为什么进入候选分母。** 摘要首要问题为“Modern coding agents are usually evaluated by whether they eventually produce a correct patch, but patch generation depends on an earlier context-acquisition stage: finding the repository files needed for the task.”；它改变 observable、对照组、判定粒度或外推边界，可能修正既有评测结论。

**机制与状态边界。** We introduce Agent Retrieval Bench, a file-level benchmark for this upstream retrieval problem.

**证据证明什么。** Selective thresholds calibrated with counterfactual controls do not improve selective success on natural no-gold cases, revealing a calibration gap.

**证据没有证明什么。** 11 Limitations The benchmark is diagnostic, not web-scale. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.24882v1#A3 — Appendix C Embedding Baseline Implementation。Evaluation：https://arxiv.org/html/2607.24882v1#A4 — Appendix D Full edit2ripple Results; https://arxiv.org/html/2607.24882v1#S10 — 10 Candidate Filter Ablation。Limitations / counterevidence：https://arxiv.org/html/2607.24882v1#S11 — 11 Limitations; https://arxiv.org/html/2607.24882v1#S12 — 12 Future Work。

**Artifact boundary。** Exact v1 links https://github.com/clap-rs/clap/pull/6319, https://github.com/tokio-rs/tokio/pull/7686, https://github.com/gin-gonic/gin/pull/4404; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：11 Limitations The benchmark is diagnostic, not web-scale.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`AGENT-CONTEXT`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-24882:end -->

<!-- review:SF-2026-ARXIV-2607-24884:start -->
### Beyond "What to Retrieve": Uncertainty in Retrieval-Augmented Code Generation

<!-- claim:SF-2026-ARXIV-2607-24884:start -->Repository-level code generation relies on heterogeneous evidence whose relevance, compatibility, and completeness are inherently uncertain. Similar-code examples, repository context, and project-specific APIs may provide complementary information, but can also introduce noisy, redundant, or conflicting signals. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-24884:end -->

**为什么进入候选分母。** 摘要首要问题为“Repository-level code generation relies on heterogeneous evidence whose relevance, compatibility, and completeness are inherently uncertain.”；它改变 observable、对照组、判定粒度或外推边界，可能修正既有评测结论。

**机制与状态边界。** We introduce OpenCoder, an uncertainty-aware framework that estimates source-specific uncertainty, uses it to filter and rank heterogeneous evidence, and guides generation, verification, and repair.

**证据证明什么。** Target-aware API refinement also substantially improves API-set retrieval.

**证据没有证明什么。** Required APIs absent from the initial candidate pool cannot be recovered through filtering alone. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.24884v1#Sx2.SSx2 — Uncertainty-Aware Framework。Evaluation：https://arxiv.org/html/2607.24884v1#Sx3 — Experimental Setup; https://arxiv.org/html/2607.24884v1#Sx4 — Results。Limitations / counterevidence：https://arxiv.org/html/2607.24884v1#Sx6 — Limitations and Ethical Considerations; https://arxiv.org/html/2607.24884v1#Sx7 — Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：Required APIs absent from the initial candidate pool cannot be recovered through filtering alone.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`AGENT-RAG`；evidence-stage relation：`corrective_evidence`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-24884:end -->

<!-- review:SF-2026-ARXIV-2607-24887:start -->
### Mechanisms of Width Scaling in Normalized Residual Networks: The Effective Alignment Dimension

<!-- claim:SF-2026-ARXIV-2607-24887:start -->Existing theories of neural-network width characterize asymptotic limits, but provide limited guidance on whether an expansion direction identified from finite training data remains beneficial on unseen data. We study this problem for function-preserving residual expansion and introduce the effective alignment dimension, a measurable quantity describing the signal-noise geometry of activation gradients. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-24887:end -->

**为什么进入候选分母。** 摘要首要问题为“Existing theories of neural-network width characterize asymptotic limits, but provide limited guidance on whether an expansion direction identified from finite training data remains beneficial on unseen data.”；它提出可跨 workload 讨论的表示、状态或计算机制，并暴露旧方案边界。

**机制与状态边界。** We integrate this certificate into the train-test residual-expansion framework, yielding a high-probability condition for test-risk improvement.

**证据证明什么。** We integrate this certificate into the train-test residual-expansion framework, yielding a high-probability condition for test-risk improvement.

**证据没有证明什么。** Conclusion We studied when a local expansion direction identified from finite training data transfers to independent test data. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.24887v1#A1 — Appendix A Model Architecture and Pretraining Details; https://arxiv.org/html/2607.24887v1#A1.SSx1 — Model Architecture。Evaluation：https://arxiv.org/html/2607.24887v1#A2.SSx5 — ResNet-20 Experimental Configuration and Accuracy; https://arxiv.org/html/2607.24887v1#Sx4 — Main Results。Limitations / counterevidence：https://arxiv.org/html/2607.24887v1#Sx6 — Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 新表示或状态机制扩大能力边界，但带来额外训练、状态管理、稳定性或泛化假设。 论文自身的边界信号是：Conclusion We studied when a local expansion direction identified from finite training data transfers to independent test data.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`MODEL-TRANSFORMER-LAYER`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-24887:end -->

<!-- review:SF-2026-ARXIV-2607-24889:start -->
### GAUGE: Grading Agent-Built Financial Models Without a Golden Answer

<!-- claim:SF-2026-ARXIV-2607-24889:start -->Financial models combine public disclosures with analyst assumptions to produce forecasts and valuations. While some components can be checked mechanically, forecasts, discount rates, and target prices often admit multiple reasonable answers. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-24889:end -->

**为什么进入候选分母。** 摘要首要问题为“Financial models combine public disclosures with analyst assumptions to produce forecasts and valuations.”；它改变 observable、对照组、判定粒度或外推边界，可能修正既有评测结论。

**机制与状态边界。** We introduce GAUGE, a benchmark for evaluating agent-built valuation models against observed analyst practice rather than a single point answer.

**证据证明什么。** Using independently built analyst models for the same companies, we find that across 108 directed pairs covering 65 companies, the median single-reference score is 0.33, 92.6% score below 0.70, and no same-vintage pair agrees on implied price within 10%.

**证据没有证明什么。** The cell is counted as a capability failure because the tested serving stack does not produce a serializable workbook within the output limit. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.24889v1#A22 — Appendix V Release Protocol and Benchmark-Design Checklist; https://arxiv.org/html/2607.24889v1#A4.SS1 — D.1. System Prompt (Complete, Verbatim)。Evaluation：https://arxiv.org/html/2607.24889v1#A12 — Appendix L Per-Facet Results: The Full Matrix; https://arxiv.org/html/2607.24889v1#A13 — Appendix M Results by Slice: Sector, Tier, and Completion Re-Cuts。Limitations / counterevidence：https://arxiv.org/html/2607.24889v1#A14.SS3 — N.3. Failure-Aware Panel Uncertainty; https://arxiv.org/html/2607.24889v1#A19 — Appendix S Three Failure Trajectories, Verbatim。

**Artifact boundary。** Exact v1 links https://qwenlm.github.io/blog/qwen3-coder/, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：The cell is counted as a capability failure because the tested serving stack does not produce a serializable workbook within the output limit.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`PLATFORM-EVALUATION-SYSTEM`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-24889:end -->

<!-- review:SF-2026-ARXIV-2607-24893:start -->
### Early Detection of Distributed Backdoors in Multi-Agent LLM Systems: A Characterization Study

<!-- claim:SF-2026-ARXIV-2607-24893:start -->Multi-agent LLM systems can be attacked by a payload that no single agent ever holds in full: a poisoned tool hides encrypted fragments in its observations, spreads them across several agents, and an external step reassembles and executes them after the run. Per-step safety checks that judge each action in isolation may fail to recognize the complete distributed payload. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-24893:end -->

**为什么进入候选分母。** 摘要首要问题为“Multi-agent LLM systems can be attacked by a payload that no single agent ever holds in full: a poisoned tool hides encrypted fragments in its observations, spreads them across several agents, and an external step reassembles and executes them after the run.”；它改变执行安全的 trust boundary、guard 或 failure detection。

**机制与状态边界。** We build a working instance on a hierarchical multi-agent system, run it under benign and attacked conditions across five language models and two task domains, and record when each fragment is injected and when the payload is assembled and executed.

**证据证明什么。** Generic zero-shot and behavior-trained detectors provide almost no warning at all; the detectors that do work lean in part on removable surface cues, chiefly the ciphertext's length and entropy, and once the entropy cue is removed from the payload and the length features from the detector, detection arrives later and transfers poorly across domains, though a fine-tuned model recovers some of the loss.

**证据没有证明什么。** A detector evaluated only on full-run classification accuracy looks strong here, yet that number says nothing about whether the run could have been stopped in time, and it hides the cost of the alarms. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.24893v1#S3 — 3. Threat Model, Attack, and Corpus。Evaluation：https://arxiv.org/html/2607.24893v1#S4 — 4. Experimental Setup; https://arxiv.org/html/2607.24893v1#S5 — 5. Results。Limitations / counterevidence：https://arxiv.org/html/2607.24893v1#S3 — 3. Threat Model, Attack, and Corpus; https://arxiv.org/html/2607.24893v1#S6 — 6. Discussion。

**Artifact boundary。** Exact v1 links https://github.com/yibo-hu-lab/distributed-backdoor-early-warning, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 新的安全控制点降低特定失败，但会引入误拒绝、旁路、观测不足或模型/任务迁移问题。 论文自身的边界信号是：A detector evaluated only on full-run classification accuracy looks strong here, yet that number says nothing about whether the run could have been stopped in time, and it hides the cost of the alarms.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`AGENT-MULTI-AGENT`；evidence-stage relation：`corrective_evidence`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-24893:end -->

<!-- review:SF-2026-ARXIV-2607-24897:start -->
### TYPO: Instruction-Dense Visual Jailbreaks against Commercial Closed-Source Image-Generation Models

<!-- claim:SF-2026-ARXIV-2607-24897:start -->Recent commercial image-generation models can generate high-quality images with readable text (e.g., posters, infographics, and manuals), attracting considerable attention. Yet we first show that this same capability also introduces a previously unreported safety vulnerability: these systems may refuse to generate harmful text directly, yet permit the same content when rendered as text within generated images, i.e., safety alignment does not reliably transfer from textual outputs to text embedded in images. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-24897:end -->

**为什么进入候选分母。** 摘要首要问题为“Recent commercial image-generation models can generate high-quality images with readable text (e.g., posters, infographics, and manuals), attracting considerable attention.”；它改变执行安全的 trust boundary、guard 或 failure detection。

**机制与状态边界。** To instantiate this threat, we propose TYPO, a black-box framework that exploits this safety gap by automatically generating adversarial TYPOgraphy prompts, which covertly steer image-generation models to express harmful intent as highly legible, typographically structured text.

**证据证明什么。** Extensive experiments across four commercial models (i.e., GPT-Image-2, Nano Banana Pro, Qwen-Image-2, and Seedream 5.0 Lite) show that TYPO substantially outperforms nine representative jailbreak attacks by 50.2% in ASR on average, while incurring an average query cost of only $0.04.

**证据没有证明什么。** 6 Conclusion, Limitations, and Future Work In this paper, we reveal instruction-dense visual jailbreaks as an underexplored attack surface in commercial closed-source image-generation models and propose Typo , a black-box framework based on a dual-channel textual-visual strategy space. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.24897v1#S4 — 4 Methodology; https://arxiv.org/html/2607.24897v1#S2.SS1 — 2.1 Image-Generation Models。Evaluation：https://arxiv.org/html/2607.24897v1#S5 — 5 Experiments; https://arxiv.org/html/2607.24897v1#S5.SS1 — 5.1 Experimental Settings。Limitations / counterevidence：https://arxiv.org/html/2607.24897v1#S6 — 6 Conclusion, Limitations, and Future Work; https://arxiv.org/html/2607.24897v1#S3.SS2 — 3.2 Threat Model。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 新的安全控制点降低特定失败，但会引入误拒绝、旁路、观测不足或模型/任务迁移问题。 论文自身的边界信号是：6 Conclusion, Limitations, and Future Work In this paper, we reveal instruction-dense visual jailbreaks as an underexplored attack surface in commercial closed-source image-generation models and propose Typo , a black-box framework based on a dual-channel textual-visual strategy space.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`PLATFORM-SECURITY`；evidence-stage relation：`corrective_evidence`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-24897:end -->

<!-- review:SF-2026-ARXIV-2607-24900:start -->
### Inverse RL Helps Align AI by Imitating Humans

<!-- claim:SF-2026-ARXIV-2607-24900:start -->Language model alignment aims to make model behavior reliably reflect desirable properties such as helpfulness, safety, and instruction following. Current approaches typically use supervised fine-tuning on demonstrations or reinforcement learning with rewards derived from verifiers or human feedback. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-24900:end -->

**为什么进入候选分母。** 摘要首要问题为“Language model alignment aims to make model behavior reliably reflect desirable properties such as helpfulness, safety, and instruction following.”；它改变训练信号、capacity 或 update ownership，而非只报告任务精度。

**机制与状态边界。** Motivated by inverse reinforcement learning, we introduce Projected Alignment Reward Estimated from Demonstrations (PARED).

**证据证明什么。** Through experiments involving inference-time reranking and adversarial on-policy RL, we show that the recovered reward improves a base policy without a supervised loss and yields further gains when optimized after standard supervised fine-tuning.

**证据没有证明什么。** However, because the policy is still optimized against a learned proxy, the usual risk of reward over-optimization remains ( Gao et al.,, 2022 ) . 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.24900v1#S1 — 1 Introduction; https://arxiv.org/html/2607.24900v1#S2 — 2 PARED: Projected Alignment Reward Estimated from Demonstrations。Evaluation：https://arxiv.org/html/2607.24900v1#A2 — Appendix B Additional Experimental Details, Diagnostics, and Ablations; https://arxiv.org/html/2607.24900v1#A2.SS5 — B.5 Feature-Set Ablations。Limitations / counterevidence：https://arxiv.org/html/2607.24900v1#S5 — 5 Discussion and Limitations。

**Artifact boundary。** Exact v1 links https://github.com/huggingface/trl, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更密集或更定向的训练信号改善样本效率，但会增加 verifier 偏差、分布迁移和优化耦合。 论文自身的边界信号是：However, because the policy is still optimized against a learned proxy, the usual risk of reward over-optimization remains ( Gao et al.,, 2022 ) .

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`TRAIN-RLHF`；evidence-stage relation：`alternative_branch`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-24900:end -->

<!-- review:SF-2026-ARXIV-2607-24904:start -->
### Mage-VL: An Efficient Codec-Native Streaming Multimodal Foundation Model

<!-- claim:SF-2026-ARXIV-2607-24904:start -->Standard vision-language models (VLMs) suffer from Moravec's paradox: they excel at complex offline visual reasoning but struggle with simple streaming perception tasks and process them inefficiently. We present Mage-VL, an efficient codec-native streaming foundation model for real-time multimodal understanding and interaction. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-24904:end -->

**为什么进入候选分母。** 摘要首要问题为“Standard vision-language models (VLMs) suffer from Moravec's paradox: they excel at complex offline visual reasoning but struggle with simple streaming perception tasks and process them inefficiently.”；它改变推理期状态放置、数据移动、执行控制或实时 SLO。

**机制与状态边界。** We present Mage-VL, an efficient codec-native streaming foundation model for real-time multimodal understanding and interaction.

**证据证明什么。** Operating at a 16 x 16 patch level, this reduces visual token consumption by over 75% while preserving spatiotemporal context.

**证据没有证明什么。** Conclusion and Limitations We presented Mage-VL, a lightweight 4B-parameter streaming vision–language model centered on its custom-designed ViT-encoder, Mage-ViT. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.24904v1#A1 — Appendix A Recaptioning System Prompt; https://arxiv.org/html/2607.24904v1#S3.SS1 — Architecture。Evaluation：https://arxiv.org/html/2607.24904v1#S5 — Experiments; https://arxiv.org/html/2607.24904v1#S5.SS1 — Experimental Setup。Limitations / counterevidence：https://arxiv.org/html/2607.24904v1#S7 — Conclusion and Limitations; https://arxiv.org/html/2607.24904v1#S6 — Discussions。

**Artifact boundary。** Exact v1 links https://github.com/microsoft/Mage, https://huggingface.co/collections/microsoft/mage, https://github.com/kakaobrain/coyo-dataset; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更激进的缓存、迁移、并行或专用执行会换取吞吐/时延，同时增加配置依赖、资源压力与回退路径。 论文自身的边界信号是：Conclusion and Limitations We presented Mage-VL, a lightweight 4B-parameter streaming vision–language model centered on its custom-designed ViT-encoder, Mage-ViT.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`MULTIMODAL-REPRESENTATION`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-24904:end -->

<!-- review:SF-2026-ARXIV-2607-24953:start -->
### Stable FP4 Training via Transposition-Invariant Block Quantization

<!-- claim:SF-2026-ARXIV-2607-24953:start -->Reducing training precision is a key lever for improving the e ciency of large language model (LLM) training, but pushing beyond FP8 to 4-bit oating point (FP4) remains challenging due to instability during optimization. We identify a fundamental source of this instability in existing microscaling approaches: scale inconsistency induced by tensor transposition. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-24953:end -->

**为什么进入候选分母。** 摘要首要问题为“Reducing training precision is a key lever for improving the e ciency of large language model (LLM) training, but pushing beyond FP8 to 4-bit oating point (FP4) remains challenging due to instability during optimization.”；它改变训练信号、capacity 或 update ownership，而非只报告任务精度。

**机制与状态边界。** To address this issue, we propose a low-precision training framework based on 2D block FP4 quantization, which enforces transposition-invariant scaling and preserves consistency between forward and backward computations.

**证据证明什么。** These results demonstrate that enforcing forwardbackward scaling consistency is su cient to enable practical FP4 training at scale, providing a simple and e ective pathway toward more e cient LLM training.

**证据没有证明什么。** Our central insight is that instability in existing FP4 methods arises not only from limited precision, but from scale inconsistency between forward and backward passes induced by tensor transposition. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.24953v1#S1 — 1 Introduction; https://arxiv.org/html/2607.24953v1#S2 — 2 Motivation for Microscaling。Evaluation：https://arxiv.org/html/2607.24953v1#A6 — Appendix F Evaluation Protocol; https://arxiv.org/html/2607.24953v1#A7 — Appendix G Ablation Interpretation。Limitations / counterevidence：https://arxiv.org/html/2607.24953v1#S5 — 5 Discussion and Limitations; https://arxiv.org/html/2607.24953v1#S6 — 6 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更密集或更定向的训练信号改善样本效率，但会增加 verifier 偏差、分布迁移和优化耦合。 论文自身的边界信号是：Our central insight is that instability in existing FP4 methods arises not only from limited precision, but from scale inconsistency between forward and backward passes induced by tensor transposition.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`TRAIN-DISTRIBUTED-TRAINING`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-24953:end -->

<!-- review:SF-2026-ARXIV-2607-24957:start -->
### PerceptionBench: Evaluating Atomic Visual Perception in Multimodal Large Language Models

<!-- claim:SF-2026-ARXIV-2607-24957:start -->We introduce PerceptionBench, a benchmark specifically designed to evaluate the atomic visual perception capabilities of Multimodal Large Language Models (MLLMs). Existing benchmarks often fail to isolate perception: holistic evaluations conflate perceptual errors with failures in reasoning or domain knowledge, while application-driven benchmarks only cover narrow, fragmented domains shaped by heuristic designs. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-24957:end -->

**为什么进入候选分母。** 摘要首要问题为“We introduce PerceptionBench, a benchmark specifically designed to evaluate the atomic visual perception capabilities of Multimodal Large Language Models (MLLMs).”；它改变 observable、对照组、判定粒度或外推边界，可能修正既有评测结论。

**机制与状态边界。** We introduce PerceptionBench, a benchmark specifically designed to evaluate the atomic visual perception capabilities of Multimodal Large Language Models (MLLMs).

**证据证明什么。** Benchmark results across sixteen frontier MLLMs reveal that atomic perception remains largely unsolved---no model reaches 60\% accuracy, perception-related hallucination is the weakest capability on average, and similar overall scores conceal sharply divergent capability profiles.

**证据没有证明什么。** The open-source frontier is closing in: Kimi K3 trails the overall leader by only 1.2 points. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.24957v1#S1 — 1 Introduction; https://arxiv.org/html/2607.24957v1#S2 — 2 PerceptionBench。Evaluation：https://arxiv.org/html/2607.24957v1#S3 — 3 Evaluation Results; https://arxiv.org/html/2607.24957v1#A3 — Appendix C Source Benchmark List and License。Limitations / counterevidence：https://arxiv.org/html/2607.24957v1#S5 — 5 Conclusion; https://arxiv.org/html/2607.24957v1#Sx1 — Limitations。

**Artifact boundary。** Exact v1 links https://github.com/MoonshotAI/PerceptionBench, https://huggingface.co/datasets/xai-org/RealworldQA, https://github.com/arXiv/html_feedback/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：The open-source frontier is closing in: Kimi K3 trails the overall leader by only 1.2 points.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`PLATFORM-EVALUATION-SYSTEM`；evidence-stage relation：`corrective_evidence`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-24957:end -->

<!-- review:SF-2026-ARXIV-2607-24964:start -->
### ALIBI: Adaptive Agentic Attacks on LLM-Based Vulnerability Detectors via Adversarial Code Comments

<!-- claim:SF-2026-ARXIV-2607-24964:start -->Large language models are increasingly deployed for security-sensitive tasks such as vulnerability detection and code review. Their reliance on natural-language context embedded in source code exposes a previously underexplored attack surface: adversarial comments that can influence a detector's reasoning without changing program behavior. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-24964:end -->

**为什么进入候选分母。** 摘要首要问题为“Large language models are increasingly deployed for security-sensitive tasks such as vulnerability detection and code review.”；它改变执行安全的 trust boundary、guard 或 failure detection。

**机制与状态边界。** We present ALIBI, an automated adaptive black-box attack framework that generates and iteratively refines adversarial comments using detector reasoning and feedback.

**证据证明什么。** Finally, prompt-level defenses provide limited robustness against adaptive attacks, whereas architectural isolation and pre-detector comment sanitization substantially improve resilience.

**证据没有证明什么。** 3.1 Threat Model We consider an evasion attack against an LLM-based vulnerability detector deployed as a security gate on contributed code. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.24964v1#S3 — 3 Threat Model & Attack Framework; https://arxiv.org/html/2607.24964v1#S3.SS2 — 3.2 Attack Framework。Evaluation：https://arxiv.org/html/2607.24964v1#S4 — 4 Experimental Results; https://arxiv.org/html/2607.24964v1#S4.SS1 — 4.1 Evaluation Setup。Limitations / counterevidence：https://arxiv.org/html/2607.24964v1#S3 — 3 Threat Model & Attack Framework; https://arxiv.org/html/2607.24964v1#S3.SS1 — 3.1 Threat Model。

**Artifact boundary。** Exact v1 links https://codeql.github.com/, https://docs.github.com/en/code-security/code-scanning, https://docs.github.com/en/enterprise-cloud/latest/code-security/concepts/code-scanning/ai-powered-security-detections; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 新的安全控制点降低特定失败，但会引入误拒绝、旁路、观测不足或模型/任务迁移问题。 论文自身的边界信号是：3.1 Threat Model We consider an evasion attack against an LLM-based vulnerability detector deployed as a security gate on contributed code.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`PLATFORM-SECURITY`；evidence-stage relation：`corrective_evidence`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-24964:end -->

<!-- review:SF-2026-ARXIV-2607-24981:start -->
### Enabling Fully Integer-Only Inference for Lightweight Detection Transformers

<!-- claim:SF-2026-ARXIV-2607-24981:start -->Vision Transformer detectors now approach the accuracy of CNNs but remain difficult to deploy on NPUs and microcontrollers because key components, including deformable attention, feature fusion, and nonlinear activation functions, are not natively compatible with integer arithmetic. Existing quantized detectors either retain operators such as Softmax, GELU, and LayerNorm or focus on heavyweight backbones, leaving lightweight detection transformers without an end-to-end integer implementation. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-24981:end -->

**为什么进入候选分母。** 摘要首要问题为“Vision Transformer detectors now approach the accuracy of CNNs but remain difficult to deploy on NPUs and microcontrollers because key components, including deformable attention, feature fusion, and nonlinear activation functions, are not natively compatible with integer arithmetic.”；它改变资源计量、分配、路由或迁移的控制权与约束。

**机制与状态边界。** Existing quantized detectors either retain operators such as Softmax, GELU, and LayerNorm or focus on heavyweight backbones, leaving lightweight detection transformers without an end-to-end integer implementation.

**证据证明什么。** Experimental results demonstrate that the proposed quantization pipeline consistently produces efficient fully integer-only models across different model scales.

**证据没有证明什么。** The table illustrates operator compatibility only and does not imply compiler placement or hardware deployment. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.24981v1#A1 — Appendix A Pseudo-code of the proposed methods; https://arxiv.org/html/2607.24981v1#S3 — 3 Methodology。Evaluation：https://arxiv.org/html/2607.24981v1#S4 — 4 Experimental Setup; https://arxiv.org/html/2607.24981v1#S4.SS1 — 4.1 Datasets and Evaluation Metrics。Limitations / counterevidence：https://arxiv.org/html/2607.24981v1#S7 — 7 Discussion: Hardware Compatibility; https://arxiv.org/html/2607.24981v1#S8 — 8 Conclusions。

**Artifact boundary。** Exact v1 links https://github.com/ltc286648/I-LW-DETR, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 动态资源控制提高利用率，但增加测量误差、迁移开销、租户公平和控制稳定性问题。 论文自身的边界信号是：The table illustrates operator compatibility only and does not imply compiler placement or hardware deployment.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`INFER-TENSORRT-LLM`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-24981:end -->

<!-- review:SF-2026-ARXIV-2607-24996:start -->
### Calibrated Partial Resets: Preventing Policy Collapse in Continual Reinforcement Learning

<!-- claim:SF-2026-ARXIV-2607-24996:start -->Neural networks are hindered by accumulating dormant neurons and loss of expressivity throughout training, particularly in non-stationary data settings, such as continual supervised and reinforcement learning. Recently, neuron resets have been used to maintain gradient flow and restore plasticity. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-24996:end -->

**为什么进入候选分母。** 摘要首要问题为“Neural networks are hindered by accumulating dormant neurons and loss of expressivity throughout training, particularly in non-stationary data settings, such as continual supervised and reinforcement learning.”；它改变训练信号、capacity 或 update ownership，而非只报告任务精度。

**机制与状态边界。** Unlike binary reset methods, partial resets avoid brittleness; unlike uniform decay, calibrated utility-scaling concentrates adjustment on the units that need it most.

**证据证明什么。** Among compared methods, only CPR avoids policy collapse over 400M training steps in SlipperyAnt, and it outperforms prior decay and reset-based methods on Continual MetaWorld and Continual MinAtar benchmarks.

**证据没有证明什么。** In the 400M-step friction-shift setting, CPR is the only method to avoid policy collapse while recovering peak performance after task changes. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.24996v1#A1 — Appendix A CPR Algorithm; https://arxiv.org/html/2607.24996v1#A8 — Appendix H Implementation Details。Evaluation：https://arxiv.org/html/2607.24996v1#A3.SS1 — C.1 Analysis of Results; https://arxiv.org/html/2607.24996v1#A3 — Appendix C Experiments in Standard RL。Limitations / counterevidence：https://arxiv.org/html/2607.24996v1#S5 — 5 Discussion。

**Artifact boundary。** Exact v1 links http://github.com/jax-ml/jax, http://github.com/google-deepmind, https://github.com/arXiv/html_feedback/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更密集或更定向的训练信号改善样本效率，但会增加 verifier 偏差、分布迁移和优化耦合。 论文自身的边界信号是：In the 400M-step friction-shift setting, CPR is the only method to avoid policy collapse while recovering peak performance after task changes.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`TRAIN-PPO`；evidence-stage relation：`corrective_evidence`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-24996:end -->

<!-- review:SF-2026-ARXIV-2607-25018:start -->
### Conformal Cascade: Distribution-Free Accuracy Guarantees for Multi-Tier LLM Inference

<!-- claim:SF-2026-ARXIV-2607-25018:start -->Large language model (LLM) cascades reduce inference cost by routing easy queries to a small model and deferring hard queries to a larger one. Production cascades govern this deferral through a confidence threshold, but LLM confidence scores are miscalibrated, the threshold must be tuned per model pair and per domain, and no setting yields a formal bound on cascade accuracy. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-25018:end -->

**为什么进入候选分母。** 摘要首要问题为“Large language model (LLM) cascades reduce inference cost by routing easy queries to a small model and deferring hard queries to a larger one.”；它改变 observable、对照组、判定粒度或外推边界，可能修正既有评测结论。

**机制与状态边界。** We introduce \textbf{Conformal Cascade} (CC), a multi-tier inference framework that uses conformal prediction set size as the deferral rule: accept when the calibrated set collapses to a single answer, defer otherwise.

**证据证明什么。** Large language model (LLM) cascades reduce inference cost by routing easy queries to a small model and deferring hard queries to a larger one.

**证据没有证明什么。** The Phi tier-1 saturation itself is a property of the Phi-3.5-mini-instruct checkpoint at : on benchmarks where the mini model is uniformly uncertain, the frequency-based score produces broad sets that never meet the singleton acceptance criterion, and the cascade cannot exit at tier 1. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.25018v1#A1 — Appendix A C3PO Design Contrast; https://arxiv.org/html/2607.25018v1#S3 — 3 Method。Evaluation：https://arxiv.org/html/2607.25018v1#A12.SS4 — L.4 Proof of Theorem 4 and Cost Results; https://arxiv.org/html/2607.25018v1#A2 — Appendix B Model and Benchmark Details。Limitations / counterevidence：https://arxiv.org/html/2607.25018v1#A8 — Appendix H Failure Diagnostics: Phi’s Under-Performance; https://arxiv.org/html/2607.25018v1#S6 — 6 Discussion。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：The Phi tier-1 saturation itself is a property of the Phi-3.5-mini-instruct checkpoint at : on benchmarks where the mini model is uniformly uncertain, the frequency-based score produces broad sets that never meet the singleton acceptance criterion, and the cascade cannot exit at tier 1.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`INFER-SCHEDULING`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-25018:end -->

<!-- review:SF-2026-ARXIV-2607-25019:start -->
### Interactive Alignment

<!-- claim:SF-2026-ARXIV-2607-25019:start -->This paper studies the long-run alignment of interactive agents, including AI systems, teams, firms, and governments, with human welfare. It develops a farming game in which a population of agents makes planting, trading, and expansion decisions. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-25019:end -->

**为什么进入候选分母。** 摘要首要问题为“This paper studies the long-run alignment of interactive agents, including AI systems, teams, firms, and governments, with human welfare.”；它改变训练信号、capacity 或 update ownership，而非只报告任务精度。

**机制与状态边界。** This paper studies the long-run alignment of interactive agents, including AI systems, teams, firms, and governments, with human welfare.

**证据证明什么。** The results suggest that evolutionary game theory provides a useful approximation to the dynamics of constitutional-agent economies.

**证据没有证明什么。** Exact v1 does not disclose a dedicated generalization or deployment guarantee beyond its stated evaluation scope. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.25019v1#S1 — 1 Introduction; https://arxiv.org/html/2607.25019v1#S2 — 2 The Farming Game。Evaluation：https://arxiv.org/html/2607.25019v1#S3.SS4 — 3.4 Experimental evaluation; https://arxiv.org/html/2607.25019v1#S4.SS4 — 4.4 Experimental evaluation。Limitations / counterevidence：https://arxiv.org/html/2607.25019v1#S5 — 5 Discussion。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更密集或更定向的训练信号改善样本效率，但会增加 verifier 偏差、分布迁移和优化耦合。 论文自身的边界信号是：Exact v1 does not disclose a dedicated generalization or deployment guarantee beyond its stated evaluation scope.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`TRAIN-RLHF`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-25019:end -->

<!-- review:SF-2026-ARXIV-2607-25032:start -->
### Authoring Agent Skills: A Software-Engineering Approach

<!-- claim:SF-2026-ARXIV-2607-25032:start -->Agent Skills are an emerging way to extend large language model agents with reusable procedural knowledge that the agent loads on demand. Anthropic introduced Agent Skills and published the format as an open specification supported across several agent tools. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-25032:end -->

**为什么进入候选分母。** 摘要首要问题为“Agent Skills are an emerging way to extend large language model agents with reusable procedural knowledge that the agent loads on demand.”；它把 context、memory、能力或进度变成持久且可验证的 agent state。

**机制与状态边界。** Anthropic introduced Agent Skills and published the format as an open specification supported across several agent tools.

**证据证明什么。** We illustrate the comparison drawn in UML class style, the loading model, the anatomy of a skill, the relative position of each mechanism, and the points at which skills and hooks act during a session.

**证据没有证明什么。** The examples use Claude Code, and the diagrams use a generic skill that does not describe any specific deployment. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.25032v1#Sx1 — Note on sources; https://arxiv.org/html/2607.25032v1#S1 — 1 Introduction。Evaluation：https://arxiv.org/html/2607.25032v1#S9 — 9 An evaluation-driven authoring process。Limitations / counterevidence：https://arxiv.org/html/2607.25032v1#Sx1 — Note on sources; https://arxiv.org/html/2607.25032v1#S1 — 1 Introduction。

**Artifact boundary。** Exact v1 links https://code.claude.com/docs/en/hooks, https://code.claude.com/docs/en/skills, https://github.com/arXiv/html_feedback/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 显式 agent state 改善恢复与控制，但增加状态陈旧、错误提交、跨轮污染和一致性责任。 论文自身的边界信号是：The examples use Claude Code, and the diagrams use a generic skill that does not describe any specific deployment.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`AGENT-SKILL`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-25032:end -->

<!-- review:SF-2026-ARXIV-2607-25063:start -->
### Similar Models Learn Differently: Final-Window Pretraining Shapes Post-Training Beyond SFT

<!-- claim:SF-2026-ARXIV-2607-25063:start -->Developers judge a model checkpoint by how it behaves. After supervised fine-tuning (SFT), two checkpoints that perform about the same across relevant benchmarks are treated as interchangeable, equally ready for the next alignment stage, typically preference optimization. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-25063:end -->

**为什么进入候选分母。** 摘要首要问题为“Developers judge a model checkpoint by how it behaves.”；它改变训练信号、capacity 或 update ownership，而非只报告任务精度。

**机制与状态边界。** After supervised fine-tuning (SFT), two checkpoints that perform about the same across relevant benchmarks are treated as interchangeable, equally ready for the next alignment stage, typically preference optimization.

**证据证明什么。** Therefore, a checkpoint should not be evaluated by its post-SFT behavior alone, and what it was trained on last should be reported with it.

**证据没有证明什么。** More broadly, this is path dependence in post-training: the training path leaves an imprint that post-SFT behavior does not reveal. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.25063v1#S3 — 3 Methodology; https://arxiv.org/html/2607.25063v1#S4.SS5 — 4.5 The Divergence Survives Recipe and Model。Evaluation：https://arxiv.org/html/2607.25063v1#S4 — 4 Experiments。Limitations / counterevidence：https://arxiv.org/html/2607.25063v1#A11 — Appendix K Limitations and Future Work; https://arxiv.org/html/2607.25063v1#S5 — 5 Conclusion。

**Artifact boundary。** Exact v1 links https://huggingface.co/datasets/HuggingFaceTB/cosmopedia, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更密集或更定向的训练信号改善样本效率，但会增加 verifier 偏差、分布迁移和优化耦合。 论文自身的边界信号是：More broadly, this is path dependence in post-training: the training path leaves an imprint that post-SFT behavior does not reveal.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`TRAIN-PRETRAINING`；evidence-stage relation：`corrective_evidence`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-25063:end -->

<!-- review:SF-2026-ARXIV-2607-25066:start -->
### Addressable Recall Compaction for Long Context-Window Control in AI Agents

<!-- claim:SF-2026-ARXIV-2607-25066:start -->Long-horizon LLM agents accumulate reasoning traces, actions, and tool observations that can eventually exceed a model's fixed context window. Existing compaction methods address this limitation by discarding, summarizing, or retrieving earlier information, but they may remove task-critical details or fail to recover them reliably. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-25066:end -->

**为什么进入候选分母。** 摘要首要问题为“Long-horizon LLM agents accumulate reasoning traces, actions, and tool observations that can eventually exceed a model's fixed context window.”；它把 context、memory、能力或进度变成持久且可验证的 agent state。

**机制与状态边界。** We propose ARC (Addressable Recall Compaction), a context-management framework that separates archival storage from active-context presentation.

**证据证明什么。** These results indicate that explicit, address-based recall can improve information retention and serving efficiency relative to the evaluated context-management baselines under the tested settings.

**证据没有证明什么。** ARC shows the trade is not necessary: by separating an append-only, content-addressed store of everything the agent has seen from a bounded-size, citation-annotated view of it, compaction becomes reversible without sacrificing the constant-size guarantee that made truncation attractive in the first place. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.25066v1#Sx4 — Proposed Method; https://arxiv.org/html/2607.25066v1#Sx4.SSx1 — Design Principle。Evaluation：https://arxiv.org/html/2607.25066v1#A2 — Appendix B Ablation; https://arxiv.org/html/2607.25066v1#A2.SSx3 — HBM (High-Bandwidth Memory) Bandwidth Analysis。Limitations / counterevidence：https://arxiv.org/html/2607.25066v1#Sx7 — Discussion and Limitations; https://arxiv.org/html/2607.25066v1#Sx8 — Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 显式 agent state 改善恢复与控制，但增加状态陈旧、错误提交、跨轮污染和一致性责任。 论文自身的边界信号是：ARC shows the trade is not necessary: by separating an append-only, content-addressed store of everything the agent has seen from a bounded-size, citation-annotated view of it, compaction becomes reversible without sacrificing the constant-size guarantee that made truncation attractive in the first place.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`AGENT-MEMORY`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-25066:end -->

<!-- review:SF-2026-ARXIV-2607-25076:start -->
### Towards an Agent Operating System - Lessons from Classical and Cloud OS

<!-- claim:SF-2026-ARXIV-2607-25076:start -->Every major wave of platform software follows the same arc: an initial period of experimentation with competing frameworks and ad-hoc implementations, followed by the articulation of a small set of stable abstractions with well-defined semantics, and finally consolidation around those abstractions into a platform that applications can portably target. POSIX did this for classical operating systems; Kubernetes did it for the cloud. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-25076:end -->

**为什么进入候选分母。** 摘要首要问题为“Every major wave of platform software follows the same arc: an initial period of experimentation with competing frameworks and ad-hoc implementations, followed by the articulation of a small set of stable abstractions with well-defined semantics, and finally consolidation around those abstractions into a platform that applications can portably target.”；它把 context、memory、能力或进度变成持久且可验证的 agent state。

**机制与状态边界。** Agentic AI systems - autonomous, LLM-driven agents that plan, use tools, maintain memory, and collaborate - are currently in the experimentation phase of the third such wave. dozens of frameworks and protocols have emerged, but no community consensus exists on what the core abstractions are or what guarantees they carry.

**证据证明什么。** We argue that the path forward is to follow the prior-wave methodology: derive new agentic abstractions by extending classical OS and cloud OS primitives to stochastic, natural-language-mediated execution, specify their semantics precisely, and consolidate around them - just as POSIX and Kubernetes consolidated their respective waves.

**证据没有证明什么。** Both the OS and Cloud-OS eras established that application code cannot be trusted to enforce resource limits, security boundaries, or correctness invariants. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.25076v1#S3.SS1 — III-A Where OS and Cloud-OS Semantics Break Down; https://arxiv.org/html/2607.25076v1#S4 — IV Proposed Agent-OS Primitives。Evaluation：https://arxiv.org/html/2607.25076v1#S5 — V Open source prototypes of Agent-OS primitives。Limitations / counterevidence：https://arxiv.org/html/2607.25076v1#S6 — VI Discussion: What the Prior Waves Teach Us; https://arxiv.org/html/2607.25076v1#S7 — VII Open Research Agenda。

**Artifact boundary。** Exact v1 links https://github.com/rossoctl/rossoctl, https://github.com/spiffe/spire/issues/6640, https://www.coderabbit.ai/blog/state-of-ai-vs-human-code-generation-report; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 显式 agent state 改善恢复与控制，但增加状态陈旧、错误提交、跨轮污染和一致性责任。 论文自身的边界信号是：Both the OS and Cloud-OS eras established that application code cannot be trusted to enforce resource limits, security boundaries, or correctness invariants.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`AGENT-PLATFORM`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-25076:end -->

<!-- review:SF-2026-ARXIV-2607-25082:start -->
### PLATO: Pointer Learner for Agent and Task Openness

<!-- claim:SF-2026-ARXIV-2607-25082:start -->Open agent systems (OASYS) are increasingly prevalent in real-world domains where the sets of agents and tasks change unpredictably over time. Such openness, including agent openness (AO) and task openness (TO), poses a fundamental challenge to multi-agent reinforcement learning (MARL), which typically assumes fixed state and action spaces. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-25082:end -->

**为什么进入候选分母。** 摘要首要问题为“Open agent systems (OASYS) are increasingly prevalent in real-world domains where the sets of agents and tasks change unpredictably over time.”；它把 context、memory、能力或进度变成持久且可验证的 agent state。

**机制与状态边界。** We evaluate PLATO with the Methods for Open Agent Systems Evaluation Initiative (MOASEI) wildfire suppression domain, an environment designed for open multi-agent system evaluation, and we demonstrate strong performance and more consistent zero-shot generalization than state-of-the-art baselines in OASYS.

**证据证明什么。** We evaluate PLATO with the Methods for Open Agent Systems Evaluation Initiative (MOASEI) wildfire suppression domain, an environment designed for open multi-agent system evaluation, and we demonstrate strong performance and more consistent zero-shot generalization than state-of-the-art baselines in OASYS.

**证据没有证明什么。** We plan to (1) extend TaAgO-MG and the pointer interface to support tasks with multiple actions (i.e., per-task action sets) to address the one-action-per-task limitation of our current TaAgO-MG; (2) investigate the interactions between temporal memory and additive attention scoring more deeply, as the ablation results suggest that recurrent history may be particularly valuable in out-of-distribution settings; (3) relax the full observability of tasks and agents assumption to study partially observable variants with latent-state or belief-based extensions; and (4) consider additional domains outlined by Eck et al. (2023) and frame openness to further evaluate and improve PLATO. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.25082v1#S2.SS1 — 2.1 Open Agent Systems (OASYS); https://arxiv.org/html/2607.25082v1#S4 — 4 Methodology。Evaluation：https://arxiv.org/html/2607.25082v1#A3.SS8 — C.8 Ablation Studies: Detailed Results; https://arxiv.org/html/2607.25082v1#A3 — Appendix C Additional Results。Limitations / counterevidence：https://arxiv.org/html/2607.25082v1#S8 — 8 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 显式 agent state 改善恢复与控制，但增加状态陈旧、错误提交、跨轮污染和一致性责任。 论文自身的边界信号是：We plan to (1) extend TaAgO-MG and the pointer interface to support tasks with multiple actions (i.e., per-task action sets) to address the one-action-per-task limitation of our current TaAgO-MG; (2) investigate the interactions between temporal memory and additive attention scoring more deeply, as the ablation results suggest that recurrent history may be particularly valuable in out-of-distribution settings; (3) relax the full observability of tasks and agents assumption to study partially observable variants with latent-state or belief-based extensions; and (4) consider additional domains outlined by Eck et al. (2023) and frame openness to further evaluate and improve PLATO.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`AGENT-PLATFORM`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-25082:end -->

<!-- review:SF-2026-ARXIV-2607-25090:start -->
### Matryoshka Agent: Unfolding Sub-Agents for Long-Horizon Machine Learning Engineering

<!-- claim:SF-2026-ARXIV-2607-25090:start -->Machine learning engineering (MLE) tasks require long-horizon decision making over iterative solution debugging and refinement, under expensive and feedback-driven environment interactions. Developing and training a monolithic agent for such tasks is fundamentally challenging, as it must simultaneously manage extremely long and noisy contexts, explore vast solution spaces, and remain effective under limited model capacity and computational budgets. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-25090:end -->

**为什么进入候选分母。** 摘要首要问题为“Machine learning engineering (MLE) tasks require long-horizon decision making over iterative solution debugging and refinement, under expensive and feedback-driven environment interactions.”；它把 context、memory、能力或进度变成持久且可验证的 agent state。

**机制与状态边界。** To address these challenges, we propose Matryoshka Agent, a unified hierarchical agent framework for complex long-horizon tasks.

**证据证明什么。** Experimental results on a broad range of MLE tasks with diverse model types and scales demonstrate that Matryoshka Agent is an effective and scalable paradigm for long-horizon MLE tasks and complex agentic problem solving.

**证据没有证明什么。** This indicates that the pretrained Orchestrator does not provide sufficient operational detail for reliable downstream execution. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.25090v1#A2 — Appendix B Agent and Environment Design; https://arxiv.org/html/2607.25090v1#S3 — 3 Method。Evaluation：https://arxiv.org/html/2607.25090v1#A1 — Appendix A Benchmark and Metric Details; https://arxiv.org/html/2607.25090v1#A4 — Appendix D Mean and Variance of Evaluation。Limitations / counterevidence：https://arxiv.org/html/2607.25090v1#A5 — Appendix E Failure Analysis of Qwen3-4B; https://arxiv.org/html/2607.25090v1#S5 — 5 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 显式 agent state 改善恢复与控制，但增加状态陈旧、错误提交、跨轮污染和一致性责任。 论文自身的边界信号是：This indicates that the pretrained Orchestrator does not provide sufficient operational detail for reliable downstream execution.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`AGENT-MULTI-AGENT`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-25090:end -->

<!-- review:SF-2026-ARXIV-2607-25091:start -->
### Towards Robust Reinforcement Learning for Small-Scale Language Model Agents

<!-- claim:SF-2026-ARXIV-2607-25091:start -->The alignment of Small Language Models (SLMs) in the 70--500M parameter range using reinforcement learning is often considered unstable, though the underlying failure mechanisms have not been systematically investigated. In the State-of-the-Art (SOTA) research, fifteen (model, corpus) configurations were trained using Proximal Policy Optimization (PPO). 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-25091:end -->

**为什么进入候选分母。** 摘要首要问题为“The alignment of Small Language Models (SLMs) in the 70--500M parameter range using reinforcement learning is often considered unstable, though the underlying failure mechanisms have not been systematically investigated.”；它改变训练信号、capacity 或 update ownership，而非只报告任务精度。

**机制与状态边界。** The proposed system converged stably in all experiments and improved preference win rate over the SFT baseline in configurations with a fluent prior and an informative reward signal.

**证据证明什么。** Furthermore, it outperformed instruction-tuned baselines while requiring significantly less training data.

**证据没有证明什么。** Second, the 250-step PPO training budget is intentionally limited and may not capture the full improvements possible with longer training schedules. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.25091v1#S3 — III Methodology; https://arxiv.org/html/2607.25091v1#S3.SS3 — III-C Stage 2: Reward Model Training。Evaluation：https://arxiv.org/html/2607.25091v1#S5 — V Results Analysis; https://arxiv.org/html/2607.25091v1#S4 — IV Experimental Setup。Limitations / counterevidence：https://arxiv.org/html/2607.25091v1#S6 — VI Discussion; https://arxiv.org/html/2607.25091v1#S7 — VII Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/huggingface/trl, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更密集或更定向的训练信号改善样本效率，但会增加 verifier 偏差、分布迁移和优化耦合。 论文自身的边界信号是：Second, the 250-step PPO training budget is intentionally limited and may not capture the full improvements possible with longer training schedules.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`AGENT-WORKFLOW`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-25091:end -->

<!-- review:SF-2026-ARXIV-2607-25135:start -->
### ScalableRAG: High-Quality RAG at Zero Ingestion Cost

<!-- claim:SF-2026-ARXIV-2607-25135:start -->Recent advances in RAG aim to optimize for performance by paying high ingestion costs for knowledge ingestion: building knowledge graphs or extracting SQL tables. In this work we show that the operations that such knowledge bases allow can be replicated with zero ingestion costs (not even a vector database); in fact our solution, Zero-Ingestion ScalableRAG, handily out-performs all baselines (including knowledge graph approaches) in three out of the six corpora considered here, and only marginally missing maximum performance on the other three, with average accuracy across all six datasets 7.36% above the next most competitive baseline. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-25135:end -->

**为什么进入候选分母。** 摘要首要问题为“Recent advances in RAG aim to optimize for performance by paying high ingestion costs for knowledge ingestion: building knowledge graphs or extracting SQL tables.”；它改变资源计量、分配、路由或迁移的控制权与约束。

**机制与状态边界。** In this work we show that the operations that such knowledge bases allow can be replicated with zero ingestion costs (not even a vector database); in fact our solution, Zero-Ingestion ScalableRAG, handily out-performs all baselines (including knowledge graph approaches) in three out of the six corpora considered here, and only marginally missing maximum performance on the other three, with average accuracy across all six datasets 7.36% above the next most competitive baseline.

**证据证明什么。** Capping the number of LLM calls by a constant independent of the corpus size, we also introduce Limited-Ingestion ScalableRAG, which does use a minimal vector database as well as an automated pattern discovery from a sample of documents, to further improve accuracy at scale.

**证据没有证明什么。** 6 Limitations A core design choice of our algorithm is that every set in the workspace is in one-to-one correspondence with a subset of the set of documents. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.25135v1#A1 — Appendix A System Prompt; https://arxiv.org/html/2607.25135v1#S3 — 3 Proposed Method。Evaluation：https://arxiv.org/html/2607.25135v1#A3.SS3 — C.3 Zero-Result Diagnostics and Recovery: 2WikiMultiHopQA; https://arxiv.org/html/2607.25135v1#S4 — 4 Experiments。Limitations / counterevidence：https://arxiv.org/html/2607.25135v1#S5 — 5 Conclusion; https://arxiv.org/html/2607.25135v1#S6 — 6 Limitations。

**Artifact boundary。** Exact v1 links https://github.com/cohesity/ScalableRAG, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 动态资源控制提高利用率，但增加测量误差、迁移开销、租户公平和控制稳定性问题。 论文自身的边界信号是：6 Limitations A core design choice of our algorithm is that every set in the workspace is in one-to-one correspondence with a subset of the set of documents.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`AGENT-RAG`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-25135:end -->

<!-- review:SF-2026-ARXIV-2607-25136:start -->
### Less Data, Better Alignment: Data-Centric Multi-Evaluator Agreement for Preference Optimization

<!-- claim:SF-2026-ARXIV-2607-25136:start -->Research on preference optimization often varies the training objective while holding the data fixed. We instead ask whether a small, high-confidence set of on-policy responses can provide a reliable learning signal. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-25136:end -->

**为什么进入候选分母。** 摘要首要问题为“Research on preference optimization often varies the training objective while holding the data fixed.”；它改变 observable、对照组、判定粒度或外推边界，可能修正既有评测结论。

**机制与状态边界。** Our method, DMAPO (Data-centric Multi-evaluator Agreement for Preference Optimization), generates candidate responses from the target policy, evaluates helpfulness, factuality, and conciseness with rubric-specialized evaluators, applies a process-critic correction, and retains only high-consensus desirable or undesirable examples.

**证据证明什么。** Across these experiments, consensus filtering offers a data-efficient route to preference optimization for general instructions, at the cost of additional curation compute and dependence on evaluator judgments.

**证据没有证明什么。** The sensitivity study and two independent pairwise evaluators probe this dependence but cannot eliminate it, particularly because the full candidate pool lacks human-verified quality labels. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.25136v1#S3 — 3 Method; https://arxiv.org/html/2607.25136v1#S4.SS1 — 4.1 Models。Evaluation：https://arxiv.org/html/2607.25136v1#A1 — Appendix A Full experimental setup; https://arxiv.org/html/2607.25136v1#A2 — Appendix B AlpacaEval-style detailed results。Limitations / counterevidence：https://arxiv.org/html/2607.25136v1#S7 — 7 Limitations; https://arxiv.org/html/2607.25136v1#S9 — 9 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：The sensitivity study and two independent pairwise evaluators probe this dependence but cannot eliminate it, particularly because the full candidate pool lacks human-verified quality labels.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`TRAIN-DPO`；evidence-stage relation：`corrective_evidence`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-25136:end -->

<!-- review:SF-2026-ARXIV-2607-25151:start -->
### HiEviDR-Bench: A Benchmark for Hierarchical Evidence Aggregation in Deep Research

<!-- claim:SF-2026-ARXIV-2607-25151:start -->Deep research requires models to retrieve, connect, and synthesize evidence from large-scale heterogeneous sources to answer complex queries and produce analytical reports. Existing benchmarks mainly evaluate final outcomes, such as answer correctness, report quality, or citation alignment, while providing limited visibility into whether evidence is correctly selected, linked, and aggregated into supported claims and conclusions. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-25151:end -->

**为什么进入候选分母。** 摘要首要问题为“Deep research requires models to retrieve, connect, and synthesize evidence from large-scale heterogeneous sources to answer complex queries and produce analytical reports.”；它改变 observable、对照组、判定粒度或外推边界，可能修正既有评测结论。

**机制与状态边界。** To address this gap, we introduce HiEviDR-Bench, a benchmark for evaluating Hierarchical Evidence Aggregation in Deep Research.

**证据证明什么。** Experiments on 16 representative multimodal large language models show that, although many systems achieve strong report quality, their performance drops markedly on citation accuracy, claim construction, and answer correctness.

**证据没有证明什么。** Exact v1 does not disclose a dedicated generalization or deployment guarantee beyond its stated evaluation scope. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.25151v1#S1 — 1. Introduction; https://arxiv.org/html/2607.25151v1#S2 — 2. Related Work。Evaluation：https://arxiv.org/html/2607.25151v1#S4 — 4. Results and Analysis; https://arxiv.org/html/2607.25151v1#A1.SS2 — A.2. Benchmark novelty and comparison with prior work。Limitations / counterevidence：https://arxiv.org/html/2607.25151v1#S5 — 5. Conclusion。

**Artifact boundary。** Exact v1 links https://huggingface.co/datasets/BiXie/wikiimage, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：Exact v1 does not disclose a dedicated generalization or deployment guarantee beyond its stated evaluation scope.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`PLATFORM-EVALUATION-SYSTEM`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-25151:end -->

<!-- review:SF-2026-ARXIV-2607-25152:start -->
### When Do Agent Loops Mistake Stagnation for Progress? Self-Evaluation Bias and Externally Grounded Verification in Long-Running Autonomous LLM Agent Loops

<!-- claim:SF-2026-ARXIV-2607-25152:start -->Long-running autonomous agents plan, act, and judge their own completion without human intervention. When an agent grades its own work, self-evaluation bias takes hold: plausible changes are accepted as progress while real-world outcomes stagnate or regress. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-25152:end -->

**为什么进入候选分母。** 摘要首要问题为“Long-running autonomous agents plan, act, and judge their own completion without human intervention.”；它改变 observable、对照组、判定粒度或外推边界，可能修正既有评测结论。

**机制与状态边界。** When an agent grades its own work, self-evaluation bias takes hold: plausible changes are accepted as progress while real-world outcomes stagnate or regress.

**证据证明什么。** Across 54 cycles a frontier agent claimed improvement every time, yet 56 percent had a measured delta of zero or below.

**证据没有证明什么。** Each arm’s trajectory is an independent rollout, so the three evaluators do not judge the same candidate sequence; comparisons between arms are made at the level of the distribution over repeti - tions. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/pdf/2607.25152v1#page=2 — Out-of-band evaluator architecture; https://arxiv.org/pdf/2607.25152v1#page=5 — Controlled evaluator-channel design。Evaluation：https://arxiv.org/pdf/2607.25152v1#page=10 — Measured progress-mirage results; https://arxiv.org/pdf/2607.25152v1#page=13 — Boundary-task comparison。Limitations / counterevidence：https://arxiv.org/pdf/2607.25152v1#page=1 — Preliminary-draft scope; https://arxiv.org/pdf/2607.25152v1#page=19 — Generalization and field-observation limits。

**Artifact boundary。** Not Disclosed — exact v1 exposes no uniquely versioned artifact locator used to enlarge the manuscript claim boundary.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：Each arm’s trajectory is an independent rollout, so the three evaluators do not judge the same candidate sequence; comparisons between arms are made at the level of the distribution over repeti - tions.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`AGENT-REFLECTION`；evidence-stage relation：`corrective_evidence`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-25152:end -->

<!-- review:SF-2026-ARXIV-2607-25157:start -->
### PreDiff-LM: Pretrained Discrete Masked Diffusion Language Modeling with Hybrid Attention

<!-- claim:SF-2026-ARXIV-2607-25157:start -->Discrete masked diffusion language models support bidirectional generation and infilling, but adapting pretrained autoregressive (AR) transformers requires reconciling causal pretraining with bidirectional denoising. We study this problem at the level of attention rather than claiming AR-weight reuse itself as novel. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-25157:end -->

**为什么进入候选分母。** 摘要首要问题为“Discrete masked diffusion language models support bidirectional generation and infilling, but adapting pretrained autoregressive (AR) transformers requires reconciling causal pretraining with bidirectional denoising.”；它提出可跨 workload 讨论的表示、状态或计算机制，并暴露旧方案边界。

**机制与状态边界。** We study this problem at the level of attention rather than claiming AR-weight reuse itself as novel.

**证据证明什么。** Beyond perplexity, PreDiff-LM improves repetition, distributional quality, four zero-shot downstream tasks, and human preference over prior diffusion baselines.

**证据没有证明什么。** Finally, the independent human audit contains only 40 sample pairs, and quality degrades on sequences longer than 512 tokens and under distant-domain transfer. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.25157v1#S3 — 3 Method。Evaluation：https://arxiv.org/html/2607.25157v1#A1 — Appendix A Evaluation Protocol and Human Audit; https://arxiv.org/html/2607.25157v1#S4 — 4 Experiments。Limitations / counterevidence：https://arxiv.org/html/2607.25157v1#S5 — 5 Limitations; https://arxiv.org/html/2607.25157v1#S6 — 6 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 新表示或状态机制扩大能力边界，但带来额外训练、状态管理、稳定性或泛化假设。 论文自身的边界信号是：Finally, the independent human audit contains only 40 sample pairs, and quality degrades on sequences longer than 512 tokens and under distant-domain transfer.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`MULTIMODAL-GENERATIVE-PARADIGMS`；evidence-stage relation：`alternative_branch`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-25157:end -->

<!-- review:SF-2026-ARXIV-2607-25196:start -->
### Rethinking CD: A Reproducibility Study and Extension on the Ineffectiveness of Contrastive Decoding at Mitigating Object Hallucinations in MLLMs

<!-- claim:SF-2026-ARXIV-2607-25196:start -->Contrastive decoding (CD) has been proposed as a training-free strategy for mitigating object hallucinations in multimodal large language models (MLLMs), with reported gains on benchmarks such as POPE. However, recent work has questioned whether these gains reflect genuine improvements in visual grounding. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-25196:end -->

**为什么进入候选分母。** 摘要首要问题为“Contrastive decoding (CD) has been proposed as a training-free strategy for mitigating object hallucinations in multimodal large language models (MLLMs), with reported gains on benchmarks such as POPE.”；它改变 observable、对照组、判定粒度或外推边界，可能修正既有评测结论。

**机制与状态边界。** We conduct several experiments that provide additional insights: we analyze the logit distributions induced by different CD strategies on generative datasets, propose a proxy method and compare its performance against CD techniques, and investigate how hallucination signals propagate through each layer of the expert and amateur models.

**证据证明什么。** Experimental results across MME, POPE, and CHAIR using LLaVA and Qwen validate the original claims and show that the apparent improvements from CD are often spurious and do not consistently translate into stronger visual grounding for reducing hallucinations.

**证据没有证明什么。** 8.3 Limitations and Future Works We tried to reproduce the key results of Yin et al. (2026) and conducted extensive ablations. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.25196v1#S4 — 4 Methodology; https://arxiv.org/html/2607.25196v1#S4.SS2 — 4.2 Baseline Contrastive Methods。Evaluation：https://arxiv.org/html/2607.25196v1#A1.SS3 — A.3 Balanced Accuracy evaluation metric used for Dataset Label Imbalance Analysis; https://arxiv.org/html/2607.25196v1#S5 — 5 Results and Analysis。Limitations / counterevidence：https://arxiv.org/html/2607.25196v1#S8.SS3 — 8.3 Limitations and Future Works; https://arxiv.org/html/2607.25196v1#S8 — 8 Discussion。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：8.3 Limitations and Future Works We tried to reproduce the key results of Yin et al. (2026) and conducted extensive ablations.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`MULTIMODAL-REPRESENTATION`；evidence-stage relation：`corrective_evidence`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-25196:end -->

<!-- review:SF-2026-ARXIV-2607-25225:start -->
### SecDrift: Measuring Sector-Conditioned Security Drift in AI-Generated Code

<!-- claim:SF-2026-ARXIV-2607-25225:start -->LLMs are increasingly used for code generation in critical infrastructure, yet the security effect of domain-specific prompting is understudied. We present SecDrift, a benchmark measuring sector-conditioned security drift: the change in static-analysis vulnerability rates when prompts are conditioned on industry contexts versus neutral baselines. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-25225:end -->

**为什么进入候选分母。** 摘要首要问题为“LLMs are increasingly used for code generation in critical infrastructure, yet the security effect of domain-specific prompting is understudied.”；它改变 observable、对照组、判定粒度或外推边界，可能修正既有评测结论。

**机制与状态边界。** We release the framework, prompts, generated code, findings, human-validation verdicts, and analysis scripts.

**证据证明什么。** 0 of 8 sectors show drift distinguishable from baseline, corrected or uncorrected (|h| &lt; 0.15).

**证据没有证明什么。** We do not consider adversarial prompt injection or jailbreaks. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.25225v1#S4 — 4. Methodology; https://arxiv.org/html/2607.25225v1#A3 — Appendix C Complete Model-Sector Matrix。Evaluation：https://arxiv.org/html/2607.25225v1#S5 — 5. Experimental Setup; https://arxiv.org/html/2607.25225v1#S6 — 6. Results。Limitations / counterevidence：https://arxiv.org/html/2607.25225v1#S3 — 3. Threat Model and Problem Formulation; https://arxiv.org/html/2607.25225v1#S7 — 7. Discussion。

**Artifact boundary。** Exact v1 links https://github.com/widdendream/secdrift_revised, https://github.com/features/copilot, https://github.com/arXiv/html_feedback/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：We do not consider adversarial prompt injection or jailbreaks.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`PLATFORM-SECURITY`；evidence-stage relation：`corrective_evidence`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-25225:end -->

<!-- review:SF-2026-ARXIV-2607-25227:start -->
### Decision-Level Hijacking: Injecting Cognitive Bias into Large Language Models via Bit-Flip Attacks

<!-- claim:SF-2026-ARXIV-2607-25227:start -->Large Language Models (LLMs) have been widely applied in high-stakes decision-making scenarios such as corporate strategy, and users are increasingly relying on their outputs. However, the deep integration of open-source model sharing ecosystems with LLM-powered critical decision-making applications also introduces critical risks: if an attacker can manipulate the model's cognitive stance, they can indirectly influence the judgments and actions of downstream decision-makers. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-25227:end -->

**为什么进入候选分母。** 摘要首要问题为“Large Language Models (LLMs) have been widely applied in high-stakes decision-making scenarios such as corporate strategy, and users are increasingly relying on their outputs.”；它改变执行安全的 trust boundary、guard 或 failure detection。

**机制与状态边界。** Therefore, we propose CogBias, a cognitive bias injection framework for LLMs.

**证据证明什么。** This work demonstrates that minute perturbations to low-level weight data suffice to undermine the high-level value alignment of LLMs.

**证据没有证明什么。** Future work may explore incorporating adversarial bit-flip regularization during quantization-aware training to enhance the inherent robustness of weights against sparse perturbations. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.25227v1#A5.SS3 — E.3. Baseline Methods and Evaluation Metrics; https://arxiv.org/html/2607.25227v1#S4 — 4. Methodology。Evaluation：https://arxiv.org/html/2607.25227v1#S5 — 5. Experimental Evaluation; https://arxiv.org/html/2607.25227v1#A5.SS2 — E.2. Experimental Environment and Generation Randomness Control。Limitations / counterevidence：https://arxiv.org/html/2607.25227v1#S6 — 6. Conclusion and Discussion; https://arxiv.org/html/2607.25227v1#S3 — 3. Threat Model。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 新的安全控制点降低特定失败，但会引入误拒绝、旁路、观测不足或模型/任务迁移问题。 论文自身的边界信号是：Future work may explore incorporating adversarial bit-flip regularization during quantization-aware training to enhance the inherent robustness of weights against sparse perturbations.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`PLATFORM-SECURITY`；evidence-stage relation：`corrective_evidence`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-25227:end -->

<!-- review:SF-2026-ARXIV-2607-25236:start -->
### VisualPatchWorld: Code World Models as Latent Structured Representations for Planning

<!-- claim:SF-2026-ARXIV-2607-25236:start -->Different research lines use the term world model in different ways, yet they share a common aim: to capture how the world evolves under action in a form that supports perception, simulation, and planning. Two prominent realizations are neural predictors that learn dynamics in continuous vector spaces, and hand-built physics engines that expose explicit state and physical laws. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-25236:end -->

**为什么进入候选分母。** 摘要首要问题为“Different research lines use the term world model in different ways, yet they share a common aim: to capture how the world evolves under action in a form that supports perception, simulation, and planning.”；它把 context、memory、能力或进度变成持久且可验证的 agent state。

**机制与状态边界。** We introduce VisualPatchWorld (VPW), which represents world dynamics as code.

**证据证明什么。** These results establish a practical route toward automatically constructed code world models that are useful for planning.

**证据没有证明什么。** Exact v1 does not disclose a dedicated generalization or deployment guarantee beyond its stated evaluation scope. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.25236v1#S4 — 4. Method; https://arxiv.org/html/2607.25236v1#A1 — Appendix A Pipeline Algorithms。Evaluation：https://arxiv.org/html/2607.25236v1#A3 — Appendix C Induction and Perception Analysis; https://arxiv.org/html/2607.25236v1#A5.SS5 — E.5. Reacher: frame MPC multi-seed results。Limitations / counterevidence：https://arxiv.org/html/2607.25236v1#A4 — Appendix D Baseline Ports and Failure Modes; https://arxiv.org/html/2607.25236v1#A4.SS1 — D.1. Baseline failure case studies。

**Artifact boundary。** Exact v1 links https://github.com/HKBU-KnowComp/VisualPatchWorld/, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 显式 agent state 改善恢复与控制，但增加状态陈旧、错误提交、跨轮污染和一致性责任。 论文自身的边界信号是：Exact v1 does not disclose a dedicated generalization or deployment guarantee beyond its stated evaluation scope.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`MULTIMODAL-WORLD-MODELS`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-25236:end -->

<!-- review:SF-2026-ARXIV-2607-25255:start -->
### SafeFlow: Semantic Information-Flow Control for Blocking Malicious Propagation in Multi-Agent Systems

<!-- claim:SF-2026-ARXIV-2607-25255:start -->Multi-agent systems improve capability through task decomposition and role specialization, but these same mechanisms introduce an important safety blind spot: a harmful objective can be fragmented into locally plausible subtasks, allowing malicious intent to evade detection by any single agent. This is a growing social-impact challenge: systems handling sensitive information or consequential tools can turn routine delegation into unauthorized disclosure or unsafe action. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-25255:end -->

**为什么进入候选分母。** 摘要首要问题为“Multi-agent systems improve capability through task decomposition and role specialization, but these same mechanisms introduce an important safety blind spot: a harmful objective can be fragmented into locally plausible subtasks, allowing malicious intent to evade detection by any single agent.”；它改变执行安全的 trust boundary、guard 或 failure detection。

**机制与状态边界。** To address this, we propose SafeFlow, a defense framework for multi-agent systems that formalizes malicious cross-agent propagation as a semantic information-flow problem.

**证据证明什么。** SafeFlow keeps this risk visible throughout the workflow, before it results in harm.

**证据没有证明什么。** Exact v1 does not disclose a dedicated generalization or deployment guarantee beyond its stated evaluation scope. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.25255v1#S3 — 3 Methodology; https://arxiv.org/html/2607.25255v1#S4 — 4 SafeFlow Architecture。Evaluation：https://arxiv.org/html/2607.25255v1#S5.SS5 — 5.5 Ablation and Sensitivity Analysis; https://arxiv.org/html/2607.25255v1#A2.SS2 — B.2 Reproducibility and Evaluation Notes。Limitations / counterevidence：https://arxiv.org/html/2607.25255v1#S6 — 6 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 新的安全控制点降低特定失败，但会引入误拒绝、旁路、观测不足或模型/任务迁移问题。 论文自身的边界信号是：Exact v1 does not disclose a dedicated generalization or deployment guarantee beyond its stated evaluation scope.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`PLATFORM-SECURITY`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-25255:end -->

<!-- review:SF-2026-ARXIV-2607-25257:start -->
### Laplace-PSN-IRT: Uncertainty Quantification for Neural Item Response Theory Models of LLM Benchmarks

<!-- claim:SF-2026-ARXIV-2607-25257:start -->Item Response Theory (IRT) has recently been proposed as a framework for evaluating large language model (LLM) benchmarks by separating a model's latent ability from the properties of individual benchmark items. Existing neural IRT approaches, including PSN-IRT, estimate these quantities using point estimates, limiting uncertainty quantification and downstream statistical inference. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-25257:end -->

**为什么进入候选分母。** 摘要首要问题为“Item Response Theory (IRT) has recently been proposed as a framework for evaluating large language model (LLM) benchmarks by separating a model's latent ability from the properties of individual benchmark items.”；它改变 observable、对照组、判定粒度或外推边界，可能修正既有评测结论。

**机制与状态边界。** Item Response Theory (IRT) has recently been proposed as a framework for evaluating large language model (LLM) benchmarks by separating a model's latent ability from the properties of individual benchmark items.

**证据证明什么。** We show that most pairwise comparisons among 12 models on a standard LLM benchmark leaderboard are not statistically distinguishable despite differing point-estimate ranks.

**证据没有证明什么。** 6 Limitations Item-branch posterior is scoped, not full. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.25257v1#S3 — 3 Method: Last-Layer Laplace Approximation; https://arxiv.org/html/2607.25257v1#S5.SS1 — 5.1 Pairwise model ability comparisons。Evaluation：https://arxiv.org/html/2607.25257v1#S4 — 4 Experimental Setup; https://arxiv.org/html/2607.25257v1#S5 — 5 Results。Limitations / counterevidence：https://arxiv.org/html/2607.25257v1#S6 — 6 Limitations; https://arxiv.org/html/2607.25257v1#S8 — 8 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/JFMandujanoR/Laplace-PSN-IRT/tree/jfmr_laplace, https://github.com/Joe-Hall-Lee/PSN-IRT, https://github.com/arXiv/html_feedback/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：6 Limitations Item-branch posterior is scoped, not full.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`PLATFORM-EVALUATION-SYSTEM`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-25257:end -->

<!-- review:SF-2026-ARXIV-2607-25271:start -->
### Bridging Compute- and Data-Optimal Pretraining

<!-- claim:SF-2026-ARXIV-2607-25271:start -->Classical compute-optimal scaling laws assume an unbounded supply of fresh pretraining data, yet pretraining is increasingly entering a regime in which compute grows faster than the availability of high-quality data. We propose Compute-Data (CD) scaling laws, a unified framework that bridges compute-optimal scaling, where data scales freely with compute, and data-optimal scaling, where the corpus is fixed while compute can grow without bound. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-25271:end -->

**为什么进入候选分母。** 摘要首要问题为“Classical compute-optimal scaling laws assume an unbounded supply of fresh pretraining data, yet pretraining is increasingly entering a regime in which compute grows faster than the availability of high-quality data.”；它改变训练信号、capacity 或 update ownership，而非只报告任务精度。

**机制与状态边界。** We propose Compute-Data (CD) scaling laws, a unified framework that bridges compute-optimal scaling, where data scales freely with compute, and data-optimal scaling, where the corpus is fixed while compute can grow without bound.

**证据证明什么。** We find that token effectiveness is far from constant: it depends jointly on model size, the tokens-per-parameter ratio, and the amount of derived data, and it saturates as the corpus is expanded.

**证据没有证明什么。** Exact v1 does not disclose a dedicated generalization or deployment guarantee beyond its stated evaluation scope. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.25271v1#S3 — 3 Methodology and Experiment Setup; https://arxiv.org/html/2607.25271v1#A1 — Appendix A Implementation Details and Ablations for the CD-Scaling Fit。Evaluation：https://arxiv.org/html/2607.25271v1#A2 — Appendix B Additional Experiment Details and Results; https://arxiv.org/html/2607.25271v1#A1 — Appendix A Implementation Details and Ablations for the CD-Scaling Fit。Limitations / counterevidence：https://arxiv.org/html/2607.25271v1#S6 — 6 Conclusion & Discussion。

**Artifact boundary。** Exact v1 links https://huggingface.co/datasets/allenai/dolma3_mix-150B-1025, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更密集或更定向的训练信号改善样本效率，但会增加 verifier 偏差、分布迁移和优化耦合。 论文自身的边界信号是：Exact v1 does not disclose a dedicated generalization or deployment guarantee beyond its stated evaluation scope.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`TRAIN-PRETRAINING`；evidence-stage relation：`corrective_evidence`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-25271:end -->

<!-- review:SF-2026-ARXIV-2607-25291:start -->
### CoSA: Accelerating Long-Context Inference via Proxy-Kernel Co-Designed Sparse Attention

<!-- claim:SF-2026-ARXIV-2607-25291:start -->The quadratic cost of self-attention makes long-context inference prohibitively expensive, and proxy-based block-sparse attention has become a practical remedy. Existing methods typically rely on a proxy to predict a binary sparse mask and a kernel to consume this mask and perform sparse attention computation. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-25291:end -->

**为什么进入候选分母。** 摘要首要问题为“The quadratic cost of self-attention makes long-context inference prohibitively expensive, and proxy-based block-sparse attention has become a practical remedy.”；它改变推理期状态放置、数据移动、执行控制或实时 SLO。

**机制与状态边界。** Existing methods typically rely on a proxy to predict a binary sparse mask and a kernel to consume this mask and perform sparse attention computation.

**证据证明什么。** Impressively, CoSA achieves a 4.93$\times$ attention speedup and reduces end-to-end Time-to-First-Token by 2.53$\times$ under a context length of 128K with negligible performance degradation.

**证据没有证明什么。** As future work, we will extend CoSA beyond prefilling to decoding, which requires dedicated proxy and kernel designs due to its distinct query shapes and computational patterns. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.25291v1#A3 — Appendix C Additional Method Details; https://arxiv.org/html/2607.25291v1#S4.SS2 — 4.2 Kernel-Aware Proxy Design。Evaluation：https://arxiv.org/html/2607.25291v1#A4 — Appendix D Experimental Details and Additional Results; https://arxiv.org/html/2607.25291v1#A4.SS1 — D.1 Experimental Configurations。Limitations / counterevidence：https://arxiv.org/html/2607.25291v1#S6 — 6 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更激进的缓存、迁移、并行或专用执行会换取吞吐/时延，同时增加配置依赖、资源压力与回退路径。 论文自身的边界信号是：As future work, we will extend CoSA beyond prefilling to decoding, which requires dedicated proxy and kernel designs due to its distinct query shapes and computational patterns.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`INFER-PREFILL`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-25291:end -->

<!-- review:SF-2026-ARXIV-2607-25292:start -->
### Instruction-Tuned Language Models Cannot Sample from Distributions They Can Describe

<!-- claim:SF-2026-ARXIV-2607-25292:start -->Silicon sampling uses language models as proxies for human survey respondents, treating each model call as an independent draw from the persona's response distribution. We show this draw does not exist: instruction-tuned models do not sample from distributions, they collapse to a single output. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-25292:end -->

**为什么进入候选分母。** 摘要首要问题为“Silicon sampling uses language models as proxies for human survey respondents, treating each model call as an independent draw from the persona's response distribution.”；它提出可跨 workload 讨论的表示、状态或计算机制，并暴露旧方案边界。

**机制与状态边界。** When per-persona outputs are required, we propose Prompt-Perturbed Argyle (PPA), which reduces the same error by 21\%, spreading each persona's answers to mirror real population differences at no added cost.

**证据证明什么。** We show this draw does not exist: instruction-tuned models do not sample from distributions, they collapse to a single output.

**证据没有证明什么。** Decoding adjustments cannot fix the failure because it occurs before sampling. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.25292v1#S5.SS1 — 5.1 Method; https://arxiv.org/html/2607.25292v1#S3.SS5 — 3.5 The model can describe what it cannot sample。Evaluation：https://arxiv.org/html/2607.25292v1#A1 — Appendix A Experimental setup; https://arxiv.org/html/2607.25292v1#A10 — Appendix J CoT-RNG bridge analysis。Limitations / counterevidence：https://arxiv.org/html/2607.25292v1#S3 — 3 Characterizing the Per-Call Sampling Failure; https://arxiv.org/html/2607.25292v1#S3.SS2 — 3.2 The failure is categorical。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 新表示或状态机制扩大能力边界，但带来额外训练、状态管理、稳定性或泛化假设。 论文自身的边界信号是：Decoding adjustments cannot fix the failure because it occurs before sampling.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`MODEL-SAMPLING`；evidence-stage relation：`corrective_evidence`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-25292:end -->

<!-- review:SF-2026-ARXIV-2607-25294:start -->
### CLBench-V: Evaluating Multimodal Context Learning from Grounding to Knowledge Acquisition

<!-- claim:SF-2026-ARXIV-2607-25294:start -->Real-world tasks often require models to learn from task-specific context rather than relying only on pre-trained knowledge. While recent work has highlighted this capability as context learning, existing evaluations mainly focus on textual contexts. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-25294:end -->

**为什么进入候选分母。** 摘要首要问题为“Real-world tasks often require models to learn from task-specific context rather than relying only on pre-trained knowledge.”；它改变 observable、对照组、判定粒度或外推边界，可能修正既有评测结论。

**机制与状态边界。** We introduce CLBench-V, a benchmark for multimodal context learning that addresses the difficulty of localizing where context use breaks down by organizing tasks around three dimensions: context grounding, new information application, and new knowledge learning.

**证据证明什么。** To reduce the cost of constructing domain-specific context-learning tasks, we further use automated construction and filtering procedures for our newly built datasets.

**证据没有证明什么。** 6.2 Failure Taxonomy We manually inspect representative bad cases and categorize failures into six types: evidence missing , where the model does not attend to the relevant visual region; evidence misbinding , where evidence is attached to the wrong entity, figure, page, or option; context misuse , where the model reads the relevant information but applies it incorrectly; prior override , where the model relies on parametric knowledge despite contradictory context; incomplete induction , where the model notices local facts but fails to infer the broader context-defined rule or conclusion; and format failure , where the answer violates the expected output schema. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.25294v1#S3 — 3 CLBench-V: Task and Benchmark Design。Evaluation：https://arxiv.org/html/2607.25294v1#S3 — 3 CLBench-V: Task and Benchmark Design; https://arxiv.org/html/2607.25294v1#S3.SS3 — 3.3 Benchmark Construction。Limitations / counterevidence：https://arxiv.org/html/2607.25294v1#A3.SS1 — C.1 Failure Taxonomy Case Studies; https://arxiv.org/html/2607.25294v1#S6.SS2 — 6.2 Failure Taxonomy。

**Artifact boundary。** Exact v1 links https://github.com/IamLihua/CLBench-V, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：6.2 Failure Taxonomy We manually inspect representative bad cases and categorize failures into six types: evidence missing , where the model does not attend to the relevant visual region; evidence misbinding , where evidence is attached to the wrong entity, figure, page, or option; context misuse , where the model reads the relevant information but applies it incorrectly; prior override , where the model relies on parametric knowledge despite contradictory context; incomplete induction , where the model notices local facts but fails to infer the broader context-defined rule or conclusion; and format failure , where the answer violates the expected output schema.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`PLATFORM-EVALUATION-SYSTEM`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-25294:end -->

<!-- review:SF-2026-ARXIV-2607-25297:start -->
### Hybrid Analysis for Secure MCP Tool Use in LLM Agents

<!-- claim:SF-2026-ARXIV-2607-25297:start -->The rapid development of large language model (LLM) agents has enabled their broad adoption across diverse real-world tasks. To standardize interactions between LLM agents and external environments, Model Context Protocol (MCP) tools have emerged as a de facto standard and have been widely integrated into these systems. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-25297:end -->

**为什么进入候选分母。** 摘要首要问题为“The rapid development of large language model (LLM) agents has enabled their broad adoption across diverse real-world tasks.”；它改变执行安全的 trust boundary、guard 或 failure detection。

**机制与状态边界。** To address these limitations, we propose MTGuard, a hybrid analysis-based defense framework designed to safeguard the use of MCP tools in LLM agents by leveraging lifecycle-aware static-dynamic co-analysis.

**证据证明什么。** Extensive evaluation demonstrates that MTGuard effectively mitigates multiple categories of harmful tool use across different LLM agents while maintaining performance on benign user tasks.

**证据没有证明什么。** Although MTGuard can suppress an unsafe result, it cannot automatically undo system-level side effects that have already occurred. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.25297v1#A1 — Appendix A Framework algorithm; https://arxiv.org/html/2607.25297v1#S3 — 3. Methodology。Evaluation：https://arxiv.org/html/2607.25297v1#S3.SS4 — 3.4. Post-execution result verifier; https://arxiv.org/html/2607.25297v1#S4 — 4. Experiments。Limitations / counterevidence：https://arxiv.org/html/2607.25297v1#S5.SS1 — 5.1. Limitations & Future work; https://arxiv.org/html/2607.25297v1#S5 — 5. Discussion。

**Artifact boundary。** Exact v1 links https://github.com/antgroup/Trustworthy_LM/mcp-scan, https://github.com/Tencent/AI-Infra-Guard, https://github.com/arXiv/html_feedback/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 新的安全控制点降低特定失败，但会引入误拒绝、旁路、观测不足或模型/任务迁移问题。 论文自身的边界信号是：Although MTGuard can suppress an unsafe result, it cannot automatically undo system-level side effects that have already occurred.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`AGENT-MCP`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-25297:end -->

<!-- review:SF-2026-ARXIV-2607-25333:start -->
### Specula: Scaling formal specifications for autonomous model checking of system code

<!-- claim:SF-2026-ARXIV-2607-25333:start -->Specula is a push-button agentic system that generates high-quality formal specifications for large, complex system code and uses the specifications for highly effective model checking and bug finding. Specula employs large language model (LLM) based coding agents to autonomously develop TLA+ specifications, including invariants that describe correctness properties of the target system and formal models that describe the system implementation with the right level of abstractions. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-25333:end -->

**为什么进入候选分母。** 摘要首要问题为“Specula is a push-button agentic system that generates high-quality formal specifications for large, complex system code and uses the specifications for highly effective model checking and bug finding.”；它改变执行安全的 trust boundary、guard 或 failure detection。

**机制与状态边界。** Specula is fully autonomous and thus eliminates the barrier of applying formal methods to real-world system code (as in traditional human-centric approaches).

**证据证明什么。** Meanwhile, Specula addresses limitations of LLM-driven techniques like reward hacking and hallucinations through self-evolving loops that iteratively improve specification quality by enabling the agents to deepen their understanding of system code and its behaviors.

**证据没有证明什么。** A model can therefore remain inconsistent with the implementation in ways we did not catch, and a bug that depends on such a gap can remain undetected. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.25333v1#S3 — 3. Specula Design; https://arxiv.org/html/2607.25333v1#S3.SS2 — 3.2. Generating effective system models。Evaluation：https://arxiv.org/html/2607.25333v1#S5 — 5. Evaluation。Limitations / counterevidence：https://arxiv.org/html/2607.25333v1#S6 — 6. Discussion。

**Artifact boundary。** Exact v1 links https://github.com/specula-org/Specula, https://github.com/aptos-labs/aptos-core, https://github.com/vorner/arc-swap; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 新的安全控制点降低特定失败，但会引入误拒绝、旁路、观测不足或模型/任务迁移问题。 论文自身的边界信号是：A model can therefore remain inconsistent with the implementation in ways we did not catch, and a bug that depends on such a gap can remain undetected.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`AGENT-WORKFLOW`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-25333:end -->

<!-- review:SF-2026-ARXIV-2607-25335:start -->
### Every Time I Hire a Linguist, Inference Costs Go Down: On Linguistic Rules as Effective Prompt Compressors

<!-- claim:SF-2026-ARXIV-2607-25335:start -->Prompt compression shortens LLM input to reduce inference cost, yet existing methods score token importance through LM forward passes. It remains questionable whether such nuanced, costly token selection is necessary. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-25335:end -->

**为什么进入候选分母。** 摘要首要问题为“Prompt compression shortens LLM input to reduce inference cost, yet existing methods score token importance through LM forward passes.”；它改变资源计量、分配、路由或迁移的控制权与约束。

**机制与状态边界。** Prompt compression shortens LLM input to reduce inference cost, yet existing methods score token importance through LM forward passes.

**证据证明什么。** Prompt compression shortens LLM input to reduce inference cost, yet existing methods score token importance through LM forward passes.

**证据没有证明什么。** The 42 seeds do not exhaust linguistically motivated compression, and the six-island, fixed MAP-Elites configuration explores only a finite population. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.25335v1#A1.SS1 — A.1 Evolutionary Search Design; https://arxiv.org/html/2607.25335v1#A2.SS1 — B.1 Design Principles。Evaluation：https://arxiv.org/html/2607.25335v1#S5 — 5 Results and Analysis; https://arxiv.org/html/2607.25335v1#A12 — Appendix L Experimental Prompts。Limitations / counterevidence：https://arxiv.org/html/2607.25335v1#S6 — 6 Conclusion; https://arxiv.org/html/2607.25335v1#Sx1 — Limitations。

**Artifact boundary。** Exact v1 links https://github.com/algorithmicsuperintelligence/openevolve, https://github.com/chatde/tokenshrink, https://github.com/arXiv/html_feedback/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 动态资源控制提高利用率，但增加测量误差、迁移开销、租户公平和控制稳定性问题。 论文自身的边界信号是：The 42 seeds do not exhaust linguistically motivated compression, and the six-island, fixed MAP-Elites configuration explores only a finite population.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`AGENT-PROMPT`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-25335:end -->

<!-- review:SF-2026-ARXIV-2607-25337:start -->
### Temporal-Distance JEPA: Plan-Aware Representation Learning for Latent World Model Predictive Control

<!-- claim:SF-2026-ARXIV-2607-25337:start -->Joint-Embedding Predictive Architectures (JEPAs) learn world models by predicting in representation space rather than reconstructing pixels, making them a natural backbone for latent model predictive control from offline demonstration logs. JEPA-style training optimizes short-horizon latent prediction, whereas planning requires a multi-step ranking of imagined futures by goal progress. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-25337:end -->

**为什么进入候选分母。** 摘要首要问题为“Joint-Embedding Predictive Architectures (JEPAs) learn world models by predicting in representation space rather than reconstructing pixels, making them a natural backbone for latent model predictive control from offline demonstration logs.”；它提出可跨 workload 讨论的表示、状态或计算机制，并暴露旧方案边界。

**机制与状态边界。** Against LeWM and the concurrent RC-aux baseline under locked evaluation, Temporal-Distance-JEPA matches or exceeds both methods on every environment.

**证据证明什么。** Ablations show that the directed head, cross-trajectory negatives, and rollout consistency each contribute.

**证据没有证明什么。** Contact-rich control still prefers geometry at plan time even when ranks temporal gaps better, and proximity-gated hybrids do not recover pure geometric scoring. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.25337v1#S3 — 3. Method。Evaluation：https://arxiv.org/html/2607.25337v1#A1 — Appendix A Detailed Plan-Cost Results; https://arxiv.org/html/2607.25337v1#A3 — Appendix C Training and Evaluation Protocol。Limitations / counterevidence：https://arxiv.org/html/2607.25337v1#S5 — 5. Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/HKBU-KnowComp/TD-JEPA, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 新表示或状态机制扩大能力边界，但带来额外训练、状态管理、稳定性或泛化假设。 论文自身的边界信号是：Contact-rich control still prefers geometry at plan time even when ranks temporal gaps better, and proximity-gated hybrids do not recover pure geometric scoring.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`MULTIMODAL-WORLD-MODELS`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-25337:end -->

<!-- review:SF-2026-ARXIV-2607-25346:start -->
### The Case Against Generation for Retrieval: Discriminative Language Models as Effective Retrievers

<!-- claim:SF-2026-ARXIV-2607-25346:start -->Large Language Models (LLMs) have emerged as powerful assets for recommender systems. However, deploying them as generative recommenders or zero-shot rankers at web-scale remains bottlenecked by prohibitive computational overhead and grounding challenges. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-25346:end -->

**为什么进入候选分母。** 摘要首要问题为“Large Language Models (LLMs) have emerged as powerful assets for recommender systems.”；它提出可跨 workload 讨论的表示、状态或计算机制，并暴露旧方案边界。

**机制与状态边界。** We introduce an LLM-native two-tower framework engineered for high-throughput, large-scale retrieval.

**证据证明什么。** Extensive evaluation across three public benchmarks demonstrates that cross-encoder architecture outperforms current state-of-the-art (SoTA) models, while the efficient two-tower student achieves SoTA-comparable retrieval performance.

**证据没有证明什么。** These steps cannot be fully parallelized across output positions and therefore increase serving latency as the generated sequence grows. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.25346v1#S5 — 5 System Architecture; https://arxiv.org/html/2607.25346v1#A7.SS1 — G.1 LLM-based Recommender Systems。Evaluation：https://arxiv.org/html/2607.25346v1#A5 — Appendix E Full Two-Tower Ablation; https://arxiv.org/html/2607.25346v1#S6 — 6 Experiments on Public Datasets。Limitations / counterevidence：https://arxiv.org/html/2607.25346v1#S4.SS3 — 4.3 Efficiency Discussion; https://arxiv.org/html/2607.25346v1#S8 — 8 Conclusion。

**Artifact boundary。** Exact v1 links https://huggingface.co/Qwen/Qwen3-0.6B, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 新表示或状态机制扩大能力边界，但带来额外训练、状态管理、稳定性或泛化假设。 论文自身的边界信号是：These steps cannot be fully parallelized across output positions and therefore increase serving latency as the generated sequence grows.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`AGENT-RAG`；evidence-stage relation：`alternative_branch`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-25346:end -->

<!-- review:SF-2026-ARXIV-2607-25356:start -->
### Data Quality Profiling at Scale with Progressive Sampling: A Benchmark for Data-Centric AI Pipelines

<!-- claim:SF-2026-ARXIV-2607-25356:start -->Data quality profiling -- computing missing-value rates, duplicate fractions, outlier densities, and functional-dependency violations -- is foundational for data-centric AI pipelines, yet exhaustive scans over millions of rows are prohibitively slow for near-real-time monitoring. Progressive sampling is the standard alternative; the open question is which strategy best preserves profile fidelity at scale. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-25356:end -->

**为什么进入候选分母。** 摘要首要问题为“Data quality profiling -- computing missing-value rates, duplicate fractions, outlier densities, and functional-dependency violations -- is foundational for data-centric AI pipelines, yet exhaustive scans over millions of rows are prohibitively slow for near-real-time monitoring.”；它改变 observable、对照组、判定粒度或外推边界，可能修正既有评测结论。

**机制与状态边界。** 0.111); proxy-guided methods share DAG's failure mode (MRE 0.20-0.35).

**证据证明什么。** At a 5% budget, random uniform achieves 0.49% mean relative error on NYC 311; DAG-guided MCMC yields 19.5% (approx.

**证据没有证明什么。** Stratified sampling with a proxy that captures categorical quality defects (not IQR-based) remains an open avenue. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.25356v1#S2 — 2 Sampling Methods; https://arxiv.org/html/2607.25356v1#S2.SS4 — 2.4 Method Comparison。Evaluation：https://arxiv.org/html/2607.25356v1#S3 — 3 Experiments; https://arxiv.org/html/2607.25356v1#S3.SS1 — 3.1 Experimental Setup。Limitations / counterevidence：https://arxiv.org/html/2607.25356v1#S4 — 4 Discussion; https://arxiv.org/html/2607.25356v1#S6 — 6 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/LaureBerti/progressive-profiling, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：Stratified sampling with a proxy that captures categorical quality defects (not IQR-based) remains an open avenue.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`TRAIN-DATA`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-25356:end -->

<!-- review:SF-2026-ARXIV-2607-25357:start -->
### Raven: High-Recall Sequence Modeling with Sparse Memory Routing

<!-- claim:SF-2026-ARXIV-2607-25357:start -->Long-context recall in linear-time sequence models highlights a tradeoff in how they write to memory. State-based linear models, such as state-space models (SSMs) and linear Transformers, write densely, updating the entire state for each newly arrived token, which leads to interference and makes specific past tokens hard to recover. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-25357:end -->

**为什么进入候选分母。** 摘要首要问题为“Long-context recall in linear-time sequence models highlights a tradeoff in how they write to memory.”；它把 context、memory、能力或进度变成持久且可验证的 agent state。

**机制与状态边界。** Interpolating between these models, we introduce Raven, a linear-time sequence model that maintains a fixed set of memory slots and, at each step, decays and updates only a selected subset via learned, input-dependent routing.

**证据证明什么。** Across recall-intensive benchmarks, Raven is competitive with or outperforms prior linear-time baselines, achieving strong long-context recall where both SWA and SSMs sharply degrade.

**证据没有证明什么。** Relative to SWA, it improves two key aspects: content-dependent memory allocation through routing, and selective decay instead of position-based eviction. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.25357v1#A1.SS6 — A.6 Raven Design Details; https://arxiv.org/html/2607.25357v1#S4.SS2 — 4.2 Raven Block Design。Evaluation：https://arxiv.org/html/2607.25357v1#S8.SS2 — 8.2 Evaluation Benchmarks; https://arxiv.org/html/2607.25357v1#A1.SS3 — A.3 Experimental Details。Limitations / counterevidence：https://arxiv.org/html/2607.25357v1#S9 — 9 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/goombalab/raven, https://huggingface.co/datasets/cerebras/SlimPajama-627B, https://github.com/fla-org/flash-linear-attention; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 显式 agent state 改善恢复与控制，但增加状态陈旧、错误提交、跨轮污染和一致性责任。 论文自身的边界信号是：Relative to SWA, it improves two key aspects: content-dependent memory allocation through routing, and selective decay instead of position-based eviction.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`MODEL-LONG-CONTEXT`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-25357:end -->

<!-- review:SF-2026-ARXIV-2607-25364:start -->
### Explanation-Bound Tool Execution for AI Agents: Server-Verified Action Claims Without Trusting Model Rationales

<!-- claim:SF-2026-ARXIV-2607-25364:start -->Tool-using agents expose structured calls but commonly attach free-form rationales. Such rationales are neither authorization nor reliable introspection. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-25364:end -->

**为什么进入候选分母。** 摘要首要问题为“Tool-using agents expose structured calls but commonly attach free-form rationales.”；它改变执行安全的 trust boundary、guard 或 failure detection。

**机制与状态边界。** We present Explanation-Bound Tool Execution (EBTE), a claim-carrying mediation layer that converts decision-relevant rationale content into typed action claims and checks them against server-held intent, policy, payload, tool, risk, provenance, and freshness facts.

**证据证明什么。** Together, these studies establish profile conformance and demonstrate the feasibility of server-checked action claims within the evaluated settings.

**证据没有证明什么。** XVII Limitations and Threats to Validity The deterministic suite is small, authored, and partially generated from 8 base tasks. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.25364v1#S13.SS4 — XIII-D Implications for Agent-System Architecture; https://arxiv.org/html/2607.25364v1#S10.SS1 — X-A Design。Evaluation：https://arxiv.org/html/2607.25364v1#A6 — Appendix F Experimental Units and Denominators; https://arxiv.org/html/2607.25364v1#S10.SS2 — X-B Results。Limitations / counterevidence：https://arxiv.org/html/2607.25364v1#S17 — XVII Limitations and Threats to Validity; https://arxiv.org/html/2607.25364v1#S13 — XIII Discussion。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 新的安全控制点降低特定失败，但会引入误拒绝、旁路、观测不足或模型/任务迁移问题。 论文自身的边界信号是：XVII Limitations and Threats to Validity The deterministic suite is small, authored, and partially generated from 8 base tasks.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`AGENT-TOOL-CALLING`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-25364:end -->

<!-- review:SF-2026-ARXIV-2607-25369:start -->
### ODYSSE: Episode-wise Policy Optimization for Personalized Agentic Reasoning

<!-- claim:SF-2026-ARXIV-2607-25369:start -->Agentic systems have rapidly advanced in their ability to interact with real-world environments, leverage external tools, and provide services for users. However, unlike natural-world tasks that assume well-defined instructions, human-centered scenarios are characterized by ambiguous requests that lead to large, open-ended solution spaces. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-25369:end -->

**为什么进入候选分母。** 摘要首要问题为“Agentic systems have rapidly advanced in their ability to interact with real-world environments, leverage external tools, and provide services for users.”；它改变训练信号、capacity 或 update ownership，而非只报告任务精度。

**机制与状态边界。** In this paper, we present ODYSSE, a Reinforced Fine-Tuning (RFT) framework for personalized agentic reasoning.

**证据证明什么。** Experimental results demonstrate that ODYSSE consistently outperforms both specialist and general-purpose LVLMs, highlighting its effectiveness for personalized agentic reasoning.

**证据没有证明什么。** Exact v1 does not disclose a dedicated generalization or deployment guarantee beyond its stated evaluation scope. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.25369v1#S2.SS2 — 2.2. Agentic Systems with Reinforcement Learning; https://arxiv.org/html/2607.25369v1#S4 — 4. Methodology。Evaluation：https://arxiv.org/html/2607.25369v1#S5 — 5. Experiments; https://arxiv.org/html/2607.25369v1#S5.SS1 — 5.1. Experimental Setup。Limitations / counterevidence：https://arxiv.org/html/2607.25369v1#S6 — 6. Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更密集或更定向的训练信号改善样本效率，但会增加 verifier 偏差、分布迁移和优化耦合。 论文自身的边界信号是：Exact v1 does not disclose a dedicated generalization or deployment guarantee beyond its stated evaluation scope.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`AGENT-WORKFLOW`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-25369:end -->

<!-- review:SF-2026-ARXIV-2607-25379:start -->
### Cyber-Capable AI Agents: Vulnerabilities, Evaluation Containment, and Defensive Response

<!-- claim:SF-2026-ARXIV-2607-25379:start -->Cyber-capable AI agents combine language models with tools, memory, and execution environments to perform multi-step offensive-security tasks. Existing work separately measures cyber capability and catalogs attacks against agent components, but provides less guidance on containing a capable agent within the environments used to evaluate it. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-25379:end -->

**为什么进入候选分母。** 摘要首要问题为“Cyber-capable AI agents combine language models with tools, memory, and execution environments to perform multi-step offensive-security tasks.”；它改变执行安全的 trust boundary、guard 或 failure detection。

**机制与状态边界。** A comparative evidence protocol distinguishes record-specific factual claims from the shared systems lesson: the evaluation environment is itself part of the security boundary.

**证据证明什么。** The review identifies practical priorities for evaluating cyber capability together with the security of the environment in which that capability is exercised.

**证据没有证明什么。** The responder-access discussion adds a related constraint: the artifacts needed for incident response can resemble the artifacts of misuse, so artifact-only filtering cannot by itself establish a requester’s role. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.25379v1#S3 — 3 Background and methodology。Evaluation：https://arxiv.org/html/2607.25379v1#S5 — 5 Case study: the July 2026 intrusion。Limitations / counterevidence：https://arxiv.org/html/2607.25379v1#S10 — 10 Conclusion; https://arxiv.org/html/2607.25379v1#S9 — 9 Threats to validity。

**Artifact boundary。** Exact v1 links https://huggingface.co/blog/security-incident-july-2026, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 新的安全控制点降低特定失败，但会引入误拒绝、旁路、观测不足或模型/任务迁移问题。 论文自身的边界信号是：The responder-access discussion adds a related constraint: the artifacts needed for incident response can resemble the artifacts of misuse, so artifact-only filtering cannot by itself establish a requester’s role.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`PLATFORM-SECURITY`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-25379:end -->

<!-- review:SF-2026-ARXIV-2607-25380:start -->
### Memory for Large Language Models

<!-- claim:SF-2026-ARXIV-2607-25380:start -->Memory has evolved into a foundational architectural dimension in large language models (LLMs), shifting from an implicit byproduct of computation to a spectrum of explicit, controllable mechanisms. While recent advances introduce diverse strategies---spanning transient attention, recurrent state dynamics, parameter-efficient adaptations, and scalable lookup storage---this rapid evolution has led to a highly fragmented research landscape. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-25380:end -->

**为什么进入候选分母。** 摘要首要问题为“Memory has evolved into a foundational architectural dimension in large language models (LLMs), shifting from an implicit byproduct of computation to a spectrum of explicit, controllable mechanisms.”；它把 evidence identity、lineage、conflict 或 commit 变成显式系统状态。

**机制与状态边界。** In this survey, we present a systematic, architecture-centric taxonomy of memory in LLMs.

**证据证明什么。** By consolidating these scattered advancements into a cohesive framework, this survey charts the trajectory of memory-centric LLM design and provides a principled foundation for future innovations in scalable and adaptive language modeling.

**证据没有证明什么。** These limitations are largely architectural in nature and manifest consistently across attention-based and state-based designs. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.25380v1#S5 — V Model-Level Memory Architectures: Design, Implementation, and Evaluation; https://arxiv.org/html/2607.25380v1#S5.SS1 — V-A Hybrid Memory Architectures。Evaluation：https://arxiv.org/html/2607.25380v1#S5 — V Model-Level Memory Architectures: Design, Implementation, and Evaluation; https://arxiv.org/html/2607.25380v1#S5.SS3 — V-C Evaluation of Memory Systems。Limitations / counterevidence：https://arxiv.org/html/2607.25380v1#S3.SS4 — III-D Limitations of Implicit Memory; https://arxiv.org/html/2607.25380v1#S6 — VI Open Challenges and Future Directions。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 显式 evidence state 提高可追溯性，但新增 lineage、冲突、commit 与恢复语义，状态本身也必须被验证。 论文自身的边界信号是：These limitations are largely architectural in nature and manifest consistently across attention-based and state-based designs.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`AGENT-MEMORY`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-25380:end -->

<!-- review:SF-2026-ARXIV-2607-25398:start -->
### HANDBOOK.md: A Benchmark for Long-Context Agentic Instruction Following

<!-- claim:SF-2026-ARXIV-2607-25398:start -->Language-model agents are increasingly deployed under standing instructions: a system prompt, a policy file, or a skills document is placed in context, and the agent is trusted to let that document govern every action that follows. Existing benchmarks rarely test this deployment pattern directly; they measure whether an agent can complete a task, not whether a long, binding policy document constrains its behavior over an extended tool-use horizon. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-25398:end -->

**为什么进入候选分母。** 摘要首要问题为“Language-model agents are increasingly deployed under standing instructions: a system prompt, a policy file, or a skills document is placed in context, and the agent is trusted to let that document govern every action that follows.”；它改变 observable、对照组、判定粒度或外推边界，可能修正既有评测结论。

**机制与状态边界。** We present HANDBOOK_md, a benchmark of 65 agentic tasks modeled on how employees follow company handbooks.

**证据证明什么。** Failures follow consistent patterns: agents let a plausible but unauthorized in-environment request override the standing policy, perform a required check and then act against its result, lose rule details over long horizons, and report compliance they did not achieve.

**证据没有证明什么。** Exact v1 does not disclose a dedicated generalization or deployment guarantee beyond its stated evaluation scope. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.25398v1#A4 — Appendix D Agent-visible system prompt; https://arxiv.org/html/2607.25398v1#S3.SS1 — 3.1 Overview and design principles。Evaluation：https://arxiv.org/html/2607.25398v1#S3 — 3 The HANDBOOK.md benchmark; https://arxiv.org/html/2607.25398v1#S4 — 4 Experimental setup。Limitations / counterevidence：https://arxiv.org/html/2607.25398v1#S6 — 6 Failure analysis; https://arxiv.org/html/2607.25398v1#S7 — 7 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/surge-ai/handbook, https://github.com/harbor-framework/terminal-bench, https://github.com/arXiv/html_feedback/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：Exact v1 does not disclose a dedicated generalization or deployment guarantee beyond its stated evaluation scope.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`AGENT-CONTEXT`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-25398:end -->

<!-- review:SF-2026-ARXIV-2607-25400:start -->
### COVENANT: Natural-Language Workflow Compilation for Aligned Agent Execution

<!-- claim:SF-2026-ARXIV-2607-25400:start -->Large language model (LLM) agents are increasingly entrusted with natural-language workflow instructions (e.g., retail-payment policies) that specify not only what outcome to achieve, but also which steps, branches, and tool interactions are permitted. When these instructions are supplied as prompt context, however, the model retains control over both procedure selection and step execution. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-25400:end -->

**为什么进入候选分母。** 摘要首要问题为“Large language model (LLM) agents are increasingly entrusted with natural-language workflow instructions (e.g., retail-payment policies) that specify not only what outcome to achieve, but also which steps, branches, and tool interactions are permitted.”；它把 context、memory、能力或进度变成持久且可验证的 agent state。

**机制与状态边界。** In this work, we propose COVENANT, a compiler-and-interpreter architecture for workflow-aligned agent execution.

**证据证明什么。** Compared with state-of-the-art LLM agents, COVENANT improves benchmark success from 50.00% to 83.33% and reduces the workflow-misalignment failure rate from 42.50% to 15.83% (62.75% relative).

**证据没有证明什么。** The controlled stress tests isolate two structural pressures but do not represent all dependencies in production workflows. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.25400v1#A3 — Appendix C Runtime Controller Algorithm。Evaluation：https://arxiv.org/html/2607.25400v1#A7 — Appendix G Per-Scenario Results and Misalignment Analysis; https://arxiv.org/html/2607.25400v1#S5.SSx3 — RQ2: Scenario-Level Results and Misalignment Analysis。Limitations / counterevidence：https://arxiv.org/html/2607.25400v1#A6 — Appendix F Limitations and Threats to Validity; https://arxiv.org/html/2607.25400v1#S7 — 7 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/NousResearch/hermes-agent, https://github.com/strands-agents/agent-sop, https://github.com/arXiv/html_feedback/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 显式 agent state 改善恢复与控制，但增加状态陈旧、错误提交、跨轮污染和一致性责任。 论文自身的边界信号是：The controlled stress tests isolate two structural pressures but do not represent all dependencies in production workflows.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`AGENT-WORKFLOW`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-25400:end -->

<!-- review:SF-2026-ARXIV-2607-25408:start -->
### Context Assembly as the Controlled Variable: A Control-Theoretic View of Harness Policies for Frozen LLM Agents

<!-- claim:SF-2026-ARXIV-2607-25408:start -->A growing body of 2026 work applies control theory to LLM agents: Lyapunov-certified stability for tool-mediated controllers (Prinos et al., "Stable Agentic Control", 2026), sample-complexity bounds for sparse policies over massive discrete tool universes (Majumdar, "Sparse Agentic Control", 2026), and regulatory-control decompositions of multi-agent systems into auditable feedback loops (Nogueira and Skogestad, 2026). We do not claim to introduce control theory to LLM agents -- that ship has sailed. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-25408:end -->

**为什么进入候选分母。** 摘要首要问题为“A growing body of 2026 work applies control theory to LLM agents: Lyapunov-certified stability for tool-mediated controllers (Prinos et al., "Stable Agentic Control", 2026), sample-complexity bounds for sparse policies over massive discrete tool universes (Majumdar, "Sparse Agentic Control", 2026), and regulatory-control decompositions of multi-agent systems into auditable feedback loops (Nogueira and Skogestad, 2026”；它改变资源计量、分配、路由或迁移的控制权与约束。

**机制与状态边界。** A growing body of 2026 work applies control theory to LLM agents: Lyapunov-certified stability for tool-mediated controllers (Prinos et al., "Stable Agentic Control", 2026), sample-complexity bounds for sparse policies over massive discrete tool universes (Majumdar, "Sparse Agentic Control", 2026), and regulatory-control decompositions of multi-agent systems into auditable feedback loops (Nogueira and Skogestad, 2026).

**证据证明什么。** The applied counterpart to this paper instantiates the same controller across three domains and two model providers and releases the dataset, trajectory logs, and a deployment recipe; here we focus on the formal framing and the stability/uncertainty evidence a control-theoretic claim requires.

**证据没有证明什么。** The calibration analysis uses a single domain (tool-use) and model (Ollama qwen2.5:7b); Paper 2’s main matrix covers more domains and providers but does not log per-episode confidence, which is a straightforward instrumentation addition (already implemented in coe/policies.py ) for a future full-matrix calibration study. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.25408v1#S2 — 2 Formal decomposition; https://arxiv.org/html/2607.25408v1#S3 — 3 Stability。Evaluation：https://arxiv.org/html/2607.25408v1#S4 — 4 Uncertainty calibration; https://arxiv.org/html/2607.25408v1#S5 — 5 Positioning。Limitations / counterevidence：https://arxiv.org/html/2607.25408v1#S6 — 6 Limitations; https://arxiv.org/html/2607.25408v1#S7 — 7 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 动态资源控制提高利用率，但增加测量误差、迁移开销、租户公平和控制稳定性问题。 论文自身的边界信号是：The calibration analysis uses a single domain (tool-use) and model (Ollama qwen2.5:7b); Paper 2’s main matrix covers more domains and providers but does not log per-episode confidence, which is a straightforward instrumentation addition (already implemented in coe/policies.py ) for a future full-matrix calibration study.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`AGENT-CONTEXT`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-25408:end -->

<!-- review:SF-2026-ARXIV-2607-25415:start -->
### A Control System, a Dataset, and a Recipe for Making Frozen LLM Agents Learn a Domain

<!-- claim:SF-2026-ARXIV-2607-25415:start -->Production LLM agents are increasingly assembled from a frozen model wrapped in a harness: a prompt template, a tool set, a memory/retrieval layer, a planning strategy, and a verification policy. Two 2026 systems, Meta-Harness (Lee et al., 2026) and HyperAgents (Meta AI, 2026), show that this harness can itself be optimized or even self-rewritten by an agentic proposer -- at the cost of either an expensive code-search loop or unconstrained self-modifying code, neither of which is auditable or usable with a fully black-box model API. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-25415:end -->

**为什么进入候选分母。** 摘要首要问题为“Production LLM agents are increasingly assembled from a frozen model wrapped in a harness: a prompt template, a tool set, a memory/retrieval layer, a planning strategy, and a verification policy.”；它把 context、memory、能力或进度变成持久且可验证的 agent state。

**机制与状态边界。** We release the harness-control-system code, the cross-domain verifiable task suite, the full trajectory/reward-decomposition logs from training, and a provider-agnostic deployment recipe for applying this to a new organization's domain and verification setup.

**证据证明什么。** Two 2026 systems, Meta-Harness (Lee et al., 2026) and HyperAgents (Meta AI, 2026), show that this harness can itself be optimized or even self-rewritten by an agentic proposer -- at the cost of either an expensive code-search loop or unconstrained self-modifying code, neither of which is auditable or usable with a fully black-box model API.

**证据没有证明什么。** Our unsupported-claim metric is a lexical-overlap heuristic for the retrieval domain only, not a general hallucination detector. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.25415v1#S3 — 3 Method: context assembly as the controlled variable。Evaluation：https://arxiv.org/html/2607.25415v1#S5 — 5 Experiments; https://arxiv.org/html/2607.25415v1#S5.SS1 — 5.1 Results。Limitations / counterevidence：https://arxiv.org/html/2607.25415v1#S7 — 7 Limitations; https://arxiv.org/html/2607.25415v1#S8 — 8 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 显式 agent state 改善恢复与控制，但增加状态陈旧、错误提交、跨轮污染和一致性责任。 论文自身的边界信号是：Our unsupported-claim metric is a lexical-overlap heuristic for the retrieval domain only, not a general hallucination detector.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`AGENT-MEMORY`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-25415:end -->

<!-- review:SF-2026-ARXIV-2607-25431:start -->
### CodeNib: A Multi-View Data System for Serving Repository Context to Coding Agents

<!-- claim:SF-2026-ARXIV-2607-25431:start -->Coding agents repeatedly search, navigate, and retain context from evolving repositories, but disconnected indexes, language servers, and task-local histories force repeated discovery and obscure lifecycle costs. CodeNib builds reusable lexical, dense, and structural views per repository commit, maps outputs to repository-relative source ranges, maintains selected views across edits, and serves ranked search, symbol navigation, and bounded context through one runtime. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-25431:end -->

**为什么进入候选分母。** 摘要首要问题为“Coding agents repeatedly search, navigate, and retain context from evolving repositories, but disconnected indexes, language servers, and task-local histories force repeated discovery and obscure lifecycle costs.”；它把 context、memory、能力或进度变成持久且可验证的 agent state。

**机制与状态边界。** CodeNib builds reusable lexical, dense, and structural views per repository commit, maps outputs to repository-relative source ranges, maintains selected views across edits, and serves ranked search, symbol navigation, and bounded context through one runtime.

**证据证明什么。** Together, these results support multi-view repository-context serving with explicit, operation-specific validity boundaries.

**证据没有证明什么。** Together, they frame repository context as a measurable serving problem without collapsing exact maintenance, projection-compatible navigation, and policy-dependent localization into one unqualified notion of reuse. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.25431v1#S3 — 3. System Overview; https://arxiv.org/html/2607.25431v1#A5 — Appendix E Retrieval Models and Frozen Parameters。Evaluation：https://arxiv.org/html/2607.25431v1#S9 — 9. Evaluation; https://arxiv.org/html/2607.25431v1#S9.SS1 — 9.1. Experimental Setup。Limitations / counterevidence：https://arxiv.org/html/2607.25431v1#S10 — 10. Discussion and Future Directions; https://arxiv.org/html/2607.25431v1#S11 — 11. Conclusion。

**Artifact boundary。** Exact v1 links https://opencode.ai/docs/tools, https://engineering.fb.com/2024/12/19/developer-tools/glean-open-source-code-indexing/, https://github.com/sourcegraph/zoekt; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 显式 agent state 改善恢复与控制，但增加状态陈旧、错误提交、跨轮污染和一致性责任。 论文自身的边界信号是：Together, they frame repository context as a measurable serving problem without collapsing exact maintenance, projection-compatible navigation, and policy-dependent localization into one unqualified notion of reuse.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`AGENT-CONTEXT`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-25431:end -->

<!-- review:SF-2026-ARXIV-2607-25446:start -->
### Toward an Organizational Science of Multi-Agent LLM Systems: Decoupling Who, How, and Which Algorithm

<!-- claim:SF-2026-ARXIV-2607-25446:start -->Multi-agent frameworks built on large language models (LLMs) routinely entangle three logically distinct concerns: who is on the team (organization), how members align (coordination), and which algorithm fuses their work (collaboration protocol). IMACS (Intelligent Multi-Agent Collaboration System) separates the three into orthogonal, independently swappable layers. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-25446:end -->

**为什么进入候选分母。** 摘要首要问题为“Multi-agent frameworks built on large language models (LLMs) routinely entangle three logically distinct concerns: who is on the team (organization), how members align (coordination), and which algorithm fuses their work (collaboration protocol).”；它把 context、memory、能力或进度变成持久且可验证的 agent state。

**机制与状态边界。** IMACS (Intelligent Multi-Agent Collaboration System) separates the three into orthogonal, independently swappable layers.

**证据证明什么。** It also turns protocol choice into a variable that can be learned: Adaptive Org Routing, a contextual-bandit meta-protocol, selects a protocol per task under an explicit quality-cost tradeoff, outperforms every fixed protocol in a controlled study, and trains online on real benchmark and LLM-judge rewards.

**证据没有证明什么。** Exact v1 does not disclose a dedicated generalization or deployment guarantee beyond its stated evaluation scope. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.25446v1#Sx3 — The IMACS Framework。Evaluation：https://arxiv.org/html/2607.25446v1#Sx6 — Experiments。Limitations / counterevidence：https://arxiv.org/html/2607.25446v1#Sx7 — Discussion and Limitations; https://arxiv.org/html/2607.25446v1#Sx8 — Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 显式 agent state 改善恢复与控制，但增加状态陈旧、错误提交、跨轮污染和一致性责任。 论文自身的边界信号是：Exact v1 does not disclose a dedicated generalization or deployment guarantee beyond its stated evaluation scope.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`AGENT-MULTI-AGENT`；evidence-stage relation：`corrective_evidence`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-25446:end -->

<!-- review:SF-2026-ARXIV-2607-25451:start -->
### Bits and Memories: Measuring Verbatim Extraction Across LLM Quantization

<!-- claim:SF-2026-ARXIV-2607-25451:start -->Language models are almost always quantized before they are deployed, and a growing line of work asks whether quantization also lowers their privacy risk. That work measures privacy almost entirely with membership inference. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-25451:end -->

**为什么进入候选分母。** 摘要首要问题为“Language models are almost always quantized before they are deployed, and a growing line of work asks whether quantization also lowers their privacy risk.”；它改变执行安全的 trust boundary、guard 或 failure detection。

**机制与状态边界。** That work measures privacy almost entirely with membership inference.

**证据证明什么。** All code, sampled evaluation data, and per-configuration results are released.

**证据没有证明什么。** Compression is not a privacy defense, and extraction, not membership inference, is the number to watch. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.25451v1#S3 — 3 Method。Evaluation：https://arxiv.org/html/2607.25451v1#S4 — 4 Results。Limitations / counterevidence：https://arxiv.org/html/2607.25451v1#S5 — 5 Discussion and limitations; https://arxiv.org/html/2607.25451v1#S6 — 6 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/AkshaySasi/bits-and-memories, https://huggingface.co/datasets/AkshaySasi/bits-and-memories, https://github.com/arXiv/html_feedback/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 新的安全控制点降低特定失败，但会引入误拒绝、旁路、观测不足或模型/任务迁移问题。 论文自身的边界信号是：Compression is not a privacy defense, and extraction, not membership inference, is the number to watch.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`INFER-TENSORRT-LLM`；evidence-stage relation：`corrective_evidence`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-25451:end -->

<!-- review:SF-2026-ARXIV-2607-25467:start -->
### Seen, Said, or Forgotten? A Causal Audit of Visual KV Memory Across Dialog Turns

<!-- claim:SF-2026-ARXIV-2607-25467:start -->Stateful multimodal assistants encode an image once but may answer questions about it many turns later. Attention-guided visual-KV eviction assumes that evidence irrelevant now will remain dispensable, although future questions are unknown. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-25467:end -->

**为什么进入候选分母。** 摘要首要问题为“Stateful multimodal assistants encode an image once but may answer questions about it many turns later.”；它把 context、memory、能力或进度变成持久且可验证的 agent state。

**机制与状态边界。** We ask when a visual fact is actually safe to forget and introduce the Causal Visual Memory Audit (CVMA), a paired single-prefill framework that tests what later answers lose when a visual region, the whole image, or prior assistant text becomes unavailable.

**证据证明什么。** On VisDial and ConvBench, current attention can rank future-useful regions worse than random even though a diagnostic marginal-utility control shows substantial selection headroom.

**证据没有证明什么。** The aligned sweep also exposes a representation boundary the selector comparison cannot show. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.25467v1#S1 — 1 Introduction; https://arxiv.org/html/2607.25467v1#S2 — 2 Auditing Safe Forgetting with CVMA。Evaluation：https://arxiv.org/html/2607.25467v1#S1 — 1 Introduction; https://arxiv.org/html/2607.25467v1#S2 — 2 Auditing Safe Forgetting with CVMA。Limitations / counterevidence：https://arxiv.org/html/2607.25467v1#S3 — 3 Attention Is Not Future Utility; https://arxiv.org/html/2607.25467v1#S4.SSx3 — Turn-wise failure survives stronger selection。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 显式 agent state 改善恢复与控制，但增加状态陈旧、错误提交、跨轮污染和一致性责任。 论文自身的边界信号是：The aligned sweep also exposes a representation boundary the selector comparison cannot show.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`MULTIMODAL-REPRESENTATION`；evidence-stage relation：`corrective_evidence`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-25467:end -->

<!-- review:SF-2026-ARXIV-2607-25479:start -->
### Architectural Backdoors in Vision-Language Model Supply Chains via Representation Steering

<!-- claim:SF-2026-ARXIV-2607-25479:start -->Vision--Language Models (VLMs) are increasingly deployed through a model supply chain in which pretrained checkpoints, architecture definitions, text encoders, and exported computation graphs are distributed by third parties and reused across downstream services. This reuse model creates a security-critical trust boundary: VLM deployments inherit not only learned parameters but also executable behavior encoded in shared model artifacts. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-25479:end -->

**为什么进入候选分母。** 摘要首要问题为“Vision--Language Models (VLMs) are increasingly deployed through a model supply chain in which pretrained checkpoints, architecture definitions, text encoders, and exported computation graphs are distributed by third parties and reused across downstream services.”；它改变执行安全的 trust boundary、guard 或 failure detection。

**机制与状态边界。** We further show that shared VLM artifacts can carry dormant steering logic against downstream services, and we propose an auditing defense that inspects the executable logic distributed with model artifacts rather than only their learned weights.

**证据证明什么。** The results show that the proposed architectural steering backdoor compromises integrity, safety enforcement, and ranking fairness while preserving normal behavior on clean inputs.

**证据没有证明什么。** We argue that this reuse pattern, common in the distribution of pretrained models through public repositories [ 7 , 9 , 29 ] , creates an implicit trust assumption, by which downstream users rely on the provider not only for learned parameters but also for the executable model logic embedded in the artifact. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.25479v1#Ax1 — Appendix . Details on steering vector design; https://arxiv.org/html/2607.25479v1#S3 — III Methodology。Evaluation：https://arxiv.org/html/2607.25479v1#S5 — V Experimental Results; https://arxiv.org/html/2607.25479v1#Ax1.SS2 — .2 Ablation Study。Limitations / counterevidence：https://arxiv.org/html/2607.25479v1#S3.SS1 — III-A Threat model; https://arxiv.org/html/2607.25479v1#S8 — VIII Conclusion。

**Artifact boundary。** Exact v1 links https://huggingface.co/microsoft/Phi-3.5-vision-instruct, https://huggingface.co/Salesforce/codet5p-16b, https://huggingface.co/openbmb/MiniCPM-V-2_6; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 新的安全控制点降低特定失败，但会引入误拒绝、旁路、观测不足或模型/任务迁移问题。 论文自身的边界信号是：We argue that this reuse pattern, common in the distribution of pretrained models through public repositories [ 7 , 9 , 29 ] , creates an implicit trust assumption, by which downstream users rely on the provider not only for learned parameters but also for the executable model logic embedded in the artifact.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`PLATFORM-MODEL-REGISTRY`；evidence-stage relation：`corrective_evidence`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-25479:end -->

<!-- review:SF-2026-ARXIV-2607-25487:start -->
### CoTinyVLA: Chain-of-Thought Distillation for a Sub-Billion-Parameter Vision-Language-Action Model

<!-- claim:SF-2026-ARXIV-2607-25487:start -->Vision-Language-Action (VLA) models translate natural-language commands into robot action sequences, but leading systems on the LIBERO-Plus robustness benchmark use three- to seven-billion-parameter backbones whose memory demands can exceed embedded robotic budgets. We present CoTinyVLA, a 0.9B-parameter action model on a Qwen3.5-0.8B backbone that obtains that robustness by structuring supervision instead of enlarging the model. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-25487:end -->

**为什么进入候选分母。** 摘要首要问题为“Vision-Language-Action (VLA) models translate natural-language commands into robot action sequences, but leading systems on the LIBERO-Plus robustness benchmark use three- to seven-billion-parameter backbones whose memory demands can exceed embedded robotic budgets.”；它提出可跨 workload 讨论的表示、状态或计算机制，并暴露旧方案边界。

**机制与状态边界。** We present CoTinyVLA, a 0.9B-parameter action model on a Qwen3.5-0.8B backbone that obtains that robustness by structuring supervision instead of enlarging the model.

**证据证明什么。** Ablations show the three components to be separable by perturbation axis, and at a matched image budget how frames are divided between the two cameras and across time accounts for 8.6 points on its own.

**证据没有证明什么。** Evaluation variance is characterised: each suite total aggregates roughly 250 perturbed instances per base task, per-suite and axis-level intervals are reported in the supplementary material, and the test-time interventions are paired within a single trained model and tested exactly, so the mechanism results do not depend on the training seed. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.25487v1#S3 — 3 Method; https://arxiv.org/html/2607.25487v1#S3.SS1 — 3.1 Architecture。Evaluation：https://arxiv.org/html/2607.25487v1#A3 — Appendix C LIBERO-Plus Goal Suite Results; https://arxiv.org/html/2607.25487v1#A4 — Appendix D LIBERO-Plus Long Suite Results。Limitations / counterevidence：https://arxiv.org/html/2607.25487v1#S6 — 6 Discussion; https://arxiv.org/html/2607.25487v1#S7 — 7 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/BrainJellyPie/CoTinyVLA, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 新表示或状态机制扩大能力边界，但带来额外训练、状态管理、稳定性或泛化假设。 论文自身的边界信号是：Evaluation variance is characterised: each suite total aggregates roughly 250 perturbed instances per base task, per-suite and axis-level intervals are reported in the supplementary material, and the test-time interventions are paired within a single trained model and tested exactly, so the mechanism results do not depend on the training seed.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`MULTIMODAL-EMBODIED-VLA`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-25487:end -->

<!-- review:SF-2026-ARXIV-2607-25494:start -->
### Automated Numerical Stability Analysis of Deep Learning Operators

<!-- claim:SF-2026-ARXIV-2607-25494:start -->Finite-precision arithmetic unavoidably introduces numerical approximation errors. Numerical computations may use insufficient precision or an improper formulation, which leads to numerical instability. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-25494:end -->

**为什么进入候选分母。** 摘要首要问题为“Finite-precision arithmetic unavoidably introduces numerical approximation errors.”；它改变 observable、对照组、判定粒度或外推边界，可能修正既有评测结论。

**机制与状态边界。** In this paper, we introduce a unified software tool for stochastic numerical validation of deep-learning operators.

**证据证明什么。** We believe that our developed method and tools provide valuable insights into developing numerically stable computing kernels, which are particularly critical for numerically stable and efficient deep learning training and inference.

**证据没有证明什么。** Limitations However, due to the intrinsic nature of the CESTAC principle, the computations are required to repeat, which triggers extra overhead of performance at runtime. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.25494v1#S3.SS6 — 3.6. Design Philosophy and Application Value。Evaluation：https://arxiv.org/html/2607.25494v1#S3 — 3. Automated Numerical Stability Analysis of Deep Learning Operators; https://arxiv.org/html/2607.25494v1#S4 — 4. Experimental Simulations。Limitations / counterevidence：https://arxiv.org/html/2607.25494v1#S5 — 5. Limitations; https://arxiv.org/html/2607.25494v1#S6 — 6. Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/chenxinye/noisefloat, http://github.com/jax-ml/jax, https://github.com/arXiv/html_feedback/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：Limitations However, due to the intrinsic nature of the CESTAC principle, the computations are required to repeat, which triggers extra overhead of performance at runtime.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`INFER-TENSORRT-LLM`；evidence-stage relation：`corrective_evidence`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-25494:end -->

<!-- review:SF-2026-ARXIV-2607-25498:start -->
### Beyond Prefill-Decode Disaggregation: Dissecting LLM Inference for Heterogeneous Platforms via Dynamic Operator Scheduling

<!-- claim:SF-2026-ARXIV-2607-25498:start -->Prefill-decode disaggregation (PD) and roofline-based operator placement are common strategies for partitioning Large Language Model (LLM) inference across heterogeneous systems, but they are often insufficient in practice. End-to-end latency also depends on workload shape, runtime device contention, and persistent weight layout. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-25498:end -->

**为什么进入候选分母。** 摘要首要问题为“Prefill-decode disaggregation (PD) and roofline-based operator placement are common strategies for partitioning Large Language Model (LLM) inference across heterogeneous systems, but they are often insufficient in practice.”；它改变推理期状态放置、数据移动、执行控制或实时 SLO。

**机制与状态边界。** We present DOPS (dynamic operator scheduling), a hardware-aware, closed-loop framework that jointly optimizes operator scheduling and blockwise weight layouts.

**证据证明什么。** The source code is available at https://github.com/YIAI-02/TriForm, and the visualization tool is demonstrated at https://youtu.be/Ya_oMCyYno0.

**证据没有证明什么。** On these edge-oriented systems, the results show the value of moving beyond coarse prefill – decode disaggregation and static roofline rules and support future hardware–software co-design. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.25498v1#S4 — 4 DOPS Framework; https://arxiv.org/html/2607.25498v1#S2.SS1 — 2.1 Transformer-based Large Language Models。Evaluation：https://arxiv.org/html/2607.25498v1#S3 — 3 Motivation: Observations & Problem Analysis; https://arxiv.org/html/2607.25498v1#S6 — 6 Experiments。Limitations / counterevidence：https://arxiv.org/html/2607.25498v1#S8 — 8 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/YIAI-02/TriForm, https://github.com/YIAI-02/TriForm/blob/micro26_pieak_final/docs/EXPERIMENT_HYPERPARAMETERS.md, https://github.com/YIAI-02/TriForm/blob/micro26_pieak_final/README.md; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更激进的缓存、迁移、并行或专用执行会换取吞吐/时延，同时增加配置依赖、资源压力与回退路径。 论文自身的边界信号是：On these edge-oriented systems, the results show the value of moving beyond coarse prefill – decode disaggregation and static roofline rules and support future hardware–software co-design.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`INFER-TENSORRT-LLM`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-25498:end -->

<!-- review:SF-2026-ARXIV-2607-25504:start -->
### At-the-Roofline Sparse Tensor Contractions on Vector Processors for Transformer Inference

<!-- claim:SF-2026-ARXIV-2607-25504:start -->Fine-grained weight pruning and activation sparsification have emerged as effective approaches for reducing the compute and memory cost of inference for Transformer models. In the moderate-sparsity regime, Gustavson's dataflow provides a natural execution model for exploiting both activation and weight sparsity on vector processors through metadata-driven indexed accumulation. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-25504:end -->

**为什么进入候选分母。** 摘要首要问题为“Fine-grained weight pruning and activation sparsification have emerged as effective approaches for reducing the compute and memory cost of inference for Transformer models.”；它改变资源计量、分配、路由或迁移的控制权与约束。

**机制与状态边界。** We present Ventaglio, a runtime-configurable sparse execution unit coupled with RVV ISA extensions that drives sparse tensor contractions toward their roofline through indexed gather-accumulate-scatter support.

**证据证明什么。** Using a DuoGPT-pruned LLaMA-3-8B model with practical $40\text{--}60\%$ dual sparsity, Ventaglio achieves $2.40\text{--}5.25\times$ and $2.06\text{--}3.16\times$ speedup over dense baselines during prefill and autoregressive decoding, respectively.

**证据没有证明什么。** Exact v1 does not disclose a dedicated generalization or deployment guarantee beyond its stated evaluation scope. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.25504v1#S3 — III Ventaglio Architecture; https://arxiv.org/html/2607.25504v1#S4 — IV Evaluation Methodology and Results。Evaluation：https://arxiv.org/html/2607.25504v1#S4 — IV Evaluation Methodology and Results; https://arxiv.org/html/2607.25504v1#S4.SS1 — IV-A Kernel Benchmark Setup and Roofline Analysis。Limitations / counterevidence：https://arxiv.org/html/2607.25504v1#S5 — V Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 动态资源控制提高利用率，但增加测量误差、迁移开销、租户公平和控制稳定性问题。 论文自身的边界信号是：Exact v1 does not disclose a dedicated generalization or deployment guarantee beyond its stated evaluation scope.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`INFER-TENSORRT-LLM`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-25504:end -->

<!-- review:SF-2026-ARXIV-2607-25507:start -->
### Phase Structure in Rotary Attention: A Spectral Framework for Semantic Continuity and Execution-Boundary Governance

<!-- claim:SF-2026-ARXIV-2607-25507:start -->Transformer language models are usually analyzed through vector geometry, yet ordered context and rotary position encoding introduce explicit phase structure into query-key interactions. This paper develops a bounded spectral framework for examining rotary phase alignment, hidden-state continuity, and semantic drift without treating language models as literal physical wave systems. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-25507:end -->

**为什么进入候选分母。** 摘要首要问题为“Transformer language models are usually analyzed through vector geometry, yet ordered context and rotary position encoding introduce explicit phase structure into query-key interactions.”；它提出可跨 workload 讨论的表示、状态或计算机制，并暴露旧方案边界。

**机制与状态边界。** This paper develops a bounded spectral framework for examining rotary phase alignment, hidden-state continuity, and semantic drift without treating language models as literal physical wave systems.

**证据证明什么。** Positioned against existing geometric, spectral, phase-modulation, representation-analysis, and mechanistic-interpretability accounts, the framework contributes a theoretical and methodological program for determining when spectral structure explains continuity and when governance must remain an external predicate over execution.

**证据没有证明什么。** 13 Future Research The framework becomes scientifically consequential only if its phase variables are identifiable, its predictions survive comparison with simpler geometric measures, and its governance claims remain independent of representational coherence. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.25507v1#S12 — 12 Limits of the Framework; https://arxiv.org/html/2607.25507v1#S13.SS4 — 13.4 Architecture and context-length generalization。Evaluation：https://arxiv.org/html/2607.25507v1#S11 — 11 Experimental Program。Limitations / counterevidence：https://arxiv.org/html/2607.25507v1#S13 — 13 Future Research; https://arxiv.org/html/2607.25507v1#S14 — 14 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 新表示或状态机制扩大能力边界，但带来额外训练、状态管理、稳定性或泛化假设。 论文自身的边界信号是：13 Future Research The framework becomes scientifically consequential only if its phase variables are identifiable, its predictions survive comparison with simpler geometric measures, and its governance claims remain independent of representational coherence.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`MODEL-POSITION-ENCODING`；evidence-stage relation：`corrective_evidence`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-25507:end -->

<!-- review:SF-2026-ARXIV-2607-25516:start -->
### A Causality-aware Infer-diagnose-refine Framework for Test-time Modality Adaptation in VLA Models

<!-- claim:SF-2026-ARXIV-2607-25516:start -->Vision-language-action (VLA) models predict sequential actions to execute tasks specified by language instructions, conditioned on visual observations and proprioceptive states. However, how to fuse modalities in VLA models remains an open problem, since robot manipulation involves dynamic phases, such as long-distance movements and close-range interactions, in which the importance of visual observations may vary over time. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-25516:end -->

**为什么进入候选分母。** 摘要首要问题为“Vision-language-action (VLA) models predict sequential actions to execute tasks specified by language instructions, conditioned on visual observations and proprioceptive states.”；它提出可跨 workload 讨论的表示、状态或计算机制，并暴露旧方案边界。

**机制与状态边界。** In this paper, we propose an infer-diagnose-refine (IDR) framework, a model-agnostic framework that can be integrated with diverse VLA architectures for refining action predictions at test time.

**证据证明什么。** Extensive experiments on both simulation benchmarks and real-world tasks show improvements in overall performance across multiple VLA backbones, demonstrating the efficacy of dynamically adjusting visual importance at test time.

**证据没有证明什么。** The primary limitation is the requirement of three forward passes per control step, which increases inference latency. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.25516v1#S4 — IV Method; https://arxiv.org/html/2607.25516v1#S4.SS1 — IV-A Infer-diagnose-refine Framework。Evaluation：https://arxiv.org/html/2607.25516v1#S5 — V Experiments; https://arxiv.org/html/2607.25516v1#S5.SS1 — V-A Simulation Experiments。Limitations / counterevidence：https://arxiv.org/html/2607.25516v1#S6 — VI Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 新表示或状态机制扩大能力边界，但带来额外训练、状态管理、稳定性或泛化假设。 论文自身的边界信号是：The primary limitation is the requirement of three forward passes per control step, which increases inference latency.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`MULTIMODAL-EMBODIED-VLA`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-25516:end -->

<!-- review:SF-2026-ARXIV-2607-25554:start -->
### Distilling Temporal Search and Reasoning: Evolving LLMs for Future Prediction via Harness-Assisted Efficient Data Synthesis

<!-- claim:SF-2026-ARXIV-2607-25554:start -->Future event prediction carries broad social impact yet remains challenging. SOTA approaches augment LLMs with external agent frameworks whose predictive capability vanishes once the harness is removed. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-25554:end -->

**为什么进入候选分母。** 摘要首要问题为“Future event prediction carries broad social impact yet remains challenging.”；它改变训练信号、capacity 或 update ownership，而非只报告任务精度。

**机制与状态边界。** SOTA approaches augment LLMs with external agent frameworks whose predictive capability vanishes once the harness is removed.

**证据证明什么。** Distillation experiments show that students trained on harness-intervened data achieve the best performance, demonstrating harness-assisted model evolving that turns higher quality temporal search and reasoning data into a parametric advancement of the students.

**证据没有证明什么。** 2.1 Agent Frameworks for Future Prediction Most current future-prediction systems are built as agent harnesses that orchestrate frontier LLMs, pushing capabilities to their limits. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.25554v1#A2 — Appendix B Methodology Details; https://arxiv.org/html/2607.25554v1#A2.SS2 — B.2 System Prompts for Time-Truncation Harness。Evaluation：https://arxiv.org/html/2607.25554v1#A3 — Appendix C Experimental Details; https://arxiv.org/html/2607.25554v1#A3.SS6 — C.6 Benchmarks and Metrics。Limitations / counterevidence：https://arxiv.org/html/2607.25554v1#S7.SS3 — 7.3 Limitations and Future Works; https://arxiv.org/html/2607.25554v1#S2.SS1 — 2.1 Agent Frameworks for Future Prediction。

**Artifact boundary。** Exact v1 links https://huggingface.co/datasets/wxcai/manifold_newest_multi_domains_260318, https://www.anthropic.com/product/claude-code, https://openai.com/index/introducing-codex; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更密集或更定向的训练信号改善样本效率，但会增加 verifier 偏差、分布迁移和优化耦合。 论文自身的边界信号是：2.1 Agent Frameworks for Future Prediction Most current future-prediction systems are built as agent harnesses that orchestrate frontier LLMs, pushing capabilities to their limits.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`AGENT-WORKFLOW`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-25554:end -->

<!-- review:SF-2026-ARXIV-2607-25560:start -->
### Agent Skills Matter: Inferring Proprietary Skills from Execution Trajectories

<!-- claim:SF-2026-ARXIV-2607-25560:start -->Agent skills package reusable procedures that improve downstream performance. Their lightweight, portable form enables marketplace monetization and private deployment behind cloud-hosted agent interfaces, giving providers incentives to keep high-value skills proprietary. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-25560:end -->

**为什么进入候选分母。** 摘要首要问题为“Agent skills package reusable procedures that improve downstream performance.”；它改变执行安全的 trust boundary、guard 或 failure detection。

**机制与状态边界。** We introduce SigLeak, a black-box framework that exploits recurring skill signatures in agent behavior.

**证据证明什么。** These results show that benign execution trajectories can expose proprietary procedural knowledge.

**证据没有证明什么。** Future work could dynamically adapt the probe budget and synthesis strategy to each scenario. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.25560v1#A2 — Appendix B Method Prompts; https://arxiv.org/html/2607.25560v1#S3 — 3 Method。Evaluation：https://arxiv.org/html/2607.25560v1#A6 — Appendix F Additional Experimental Analysis; https://arxiv.org/html/2607.25560v1#A4 — Appendix D Experimental Configuration。Limitations / counterevidence：https://arxiv.org/html/2607.25560v1#S6 — 6 Conclusion; https://arxiv.org/html/2607.25560v1#Sx2 — Limitations。

**Artifact boundary。** Exact v1 links https://github.com/anthropics/skills/blob/main/skills/skill-creator/SKILL.md, https://github.com/yusufkaraaslan/Skill_Seekers, https://github.com/NousResearch/hermes-agent; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 新的安全控制点降低特定失败，但会引入误拒绝、旁路、观测不足或模型/任务迁移问题。 论文自身的边界信号是：Future work could dynamically adapt the probe budget and synthesis strategy to each scenario.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`AGENT-SKILL`；evidence-stage relation：`corrective_evidence`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-25560:end -->

<!-- review:SF-2026-ARXIV-2607-25566:start -->
### ARCHER: Agentic Rule and Compliance Harness for Executable Regulations

<!-- claim:SF-2026-ARXIV-2607-25566:start -->Verifying building compliance requires validating thousands of rules against large Building Information Modeling (BIM) designs, which is laborious, capital-intensive, and unscalable. Existing Automated Compliance Checkers (ACCs) are often difficult to generalize across different scenarios, as they are typically developed for highly specific rule sets and use cases. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-25566:end -->

**为什么进入候选分母。** 摘要首要问题为“Verifying building compliance requires validating thousands of rules against large Building Information Modeling (BIM) designs, which is laborious, capital-intensive, and unscalable.”；它改变执行安全的 trust boundary、guard 或 failure detection。

**机制与状态边界。** We introduce ARCHER (Agentic Rule and Compliance Harness for Executable Regulations), a test-driven, deterministically orchestrated multi-agent program-synthesis harness that generates auditable verification code from regulatory Codes of Practice, enabling transparent, adaptable, and scalable compliance checking.

**证据证明什么。** ARCHER's deterministic multi-agent orchestration achieves the highest accuracy for every backbone, improving mean union accuracy by 82% over a naive single-pass prompting baseline.

**证据没有证明什么。** Beyond this, ARCHER treats each rule in isolation, without modelling dependencies or contradictions across rules; sub-1.0 accuracy shortfalls are not always easy to attribute to the requirement specification, the test cases, or a coding bug; and executable checkers remain bounded by the limits of BIM schemas and computational geometry. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.25566v1#S3 — 3 Our Approach: ARCHER; https://arxiv.org/html/2607.25566v1#S3.SS4 — 3.4 Agentic Harness Architecture。Evaluation：https://arxiv.org/html/2607.25566v1#S4 — 4 Experimental Results; https://arxiv.org/html/2607.25566v1#A7 — Appendix G Per-Scenario Difficulty, Cost, and Model-Choice Analysis。Limitations / counterevidence：https://arxiv.org/html/2607.25566v1#S5 — 5 Limitations and Future Work。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 新的安全控制点降低特定失败，但会引入误拒绝、旁路、观测不足或模型/任务迁移问题。 论文自身的边界信号是：Beyond this, ARCHER treats each rule in isolation, without modelling dependencies or contradictions across rules; sub-1.0 accuracy shortfalls are not always easy to attribute to the requirement specification, the test cases, or a coding bug; and executable checkers remain bounded by the limits of BIM schemas and computational geometry.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`AGENT-WORKFLOW`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-25566:end -->

<!-- review:SF-2026-ARXIV-2607-25583:start -->
### How Small Can You Go? A Controlled Study of LoRA Rank, Target Modules, and Quantization Trade-offs for Text-to-SQL on a 60M-Parameter Model

<!-- claim:SF-2026-ARXIV-2607-25583:start -->Parameter-efficient fine-tuning (PEFT) and low-bit quantization are now standard tools for adapting language models under tight compute budgets, yet their interaction is most often studied on billion-parameter models where the design space is expensive to explore. We ask a complementary question: on a specific, fully reproducible 60M-parameter encoder-decoder model (T5-small) and a single-table text-to-SQL benchmark (WikiSQL), how much task accuracy does each efficiency knob actually cost? 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-25583:end -->

**为什么进入候选分母。** 摘要首要问题为“Parameter-efficient fine-tuning (PEFT) and low-bit quantization are now standard tools for adapting language models under tight compute budgets, yet their interaction is most often studied on billion-parameter models where the design space is expensive to explore.”；它改变 observable、对照组、判定粒度或外推边界，可能修正既有评测结论。

**机制与状态边界。** We report task accuracy alongside system-level metrics including trainable parameters, peak training memory, inference latency, and throughput, and frame adaptation as a constrained trade-off rather than an accuracy-only objective.

**证据证明什么。** Our results show that LoRA with r=16 recovers within 11.6 percentage points of full fine-tuning accuracy (59.6% vs.

**证据没有证明什么。** A key limitation is that WikiSQL is a relatively simple single-table benchmark; rank saturation may not transfer to multi-table settings such as Spider or BIRD. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.25583v1#S3 — 3 Methodology; https://arxiv.org/html/2607.25583v1#S3.SS1 — 3.1 Base Model and Task。Evaluation：https://arxiv.org/html/2607.25583v1#S4 — 4 Experimental Setup; https://arxiv.org/html/2607.25583v1#S5 — 5 Results。Limitations / counterevidence：https://arxiv.org/html/2607.25583v1#S6 — 6 Discussion; https://arxiv.org/html/2607.25583v1#S7 — 7 Limitations。

**Artifact boundary。** Exact v1 links https://github.com/mahendrarathore1742/efficient_peft_small_models, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：A key limitation is that WikiSQL is a relatively simple single-table benchmark; rank saturation may not transfer to multi-table settings such as Spider or BIRD.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`TRAIN-LORA`；evidence-stage relation：`corrective_evidence`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-25583:end -->

<!-- review:SF-2026-ARXIV-2607-25589:start -->
### Forensic Reproducibility Audit of a Radiology Vision-Language Model Benchmark: From Intended Protocol to Released Artifact

<!-- claim:SF-2026-ARXIV-2607-25589:start -->Medical-imaging AI benchmarks combine datasets, DICOM rendering, prompts, provider APIs, automated labels, statistical code, manuscripts, and repository releases. Agreement across these artifacts is usually assumed rather than tested. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-25589:end -->

**为什么进入候选分母。** 摘要首要问题为“Medical-imaging AI benchmarks combine datasets, DICOM rendering, prompts, provider APIs, automated labels, statistical code, manuscripts, and repository releases.”；它把 evidence identity、lineage、conflict 或 commit 变成显式系统状态。

**机制与状态边界。** Agreement across these artifacts is usually assumed rather than tested.

**证据证明什么。** We withdraw the original performance, ranking, prompt-effect, and clinical claims and specify machine-verifiable controls for cohort, DICOM rendering, prompt and model identity, call status, annotation provenance, keyed analysis, and derived artifacts.

**证据没有证明什么。** It does not mean that every unexpected observation is deleted. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.25589v1#S2 — 2 Conceptual framework; https://arxiv.org/html/2607.25589v1#S3 — 3 Materials and methods。Evaluation：https://arxiv.org/html/2607.25589v1#S2.SS1 — 2.1 Six states of a computational result; https://arxiv.org/html/2607.25589v1#S2.SS3 — 2.3 What can be corrected without repeating the experiment。Limitations / counterevidence：https://arxiv.org/html/2607.25589v1#S5.SS1 — 5.1 Design principles and threat model; https://arxiv.org/html/2607.25589v1#S6 — 6 Discussion。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 显式 evidence state 提高可追溯性，但新增 lineage、冲突、commit 与恢复语义，状态本身也必须被验证。 论文自身的边界信号是：It does not mean that every unexpected observation is deleted.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`PLATFORM-EVALUATION-SYSTEM`；evidence-stage relation：`corrective_evidence`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-25589:end -->

<!-- review:SF-2026-ARXIV-2607-25600:start -->
### Beyond Self-Knowledge: Propagating Uncertainty Across Reasoning and Retrieval in LLMs

<!-- claim:SF-2026-ARXIV-2607-25600:start -->Retrieval-augmented generation improves knowledge-intensive question answering, but indiscriminate retrieval can introduce irrelevant evidence and unnecessary computation. We investigate whether verbalized confidence from black-box language models can serve as an actionable signal for retrieval routing. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-25600:end -->

**为什么进入候选分母。** 摘要首要问题为“Retrieval-augmented generation improves knowledge-intensive question answering, but indiscriminate retrieval can introduce irrelevant evidence and unnecessary computation.”；它把 evidence identity、lineage、conflict 或 commit 变成显式系统状态。

**机制与状态边界。** Our method, BeyondUncertainty, first elicits a structured provisional answer and confidence estimate, then applies a model-specific threshold selected on held-out validation data and frozen before test evaluation.

**证据证明什么。** Retrieval-augmented generation improves knowledge-intensive question answering, but indiscriminate retrieval can introduce irrelevant evidence and unnecessary computation.

**证据没有证明什么。** The current system therefore improves evidence allocation, not end-to-end token efficiency. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.25600v1#Sx4 — Experimental Design。Evaluation：https://arxiv.org/html/2607.25600v1#Sx4 — Experimental Design; https://arxiv.org/html/2607.25600v1#Sx5 — Results。Limitations / counterevidence：https://arxiv.org/html/2607.25600v1#Sx7 — Discussion and Limitations; https://arxiv.org/html/2607.25600v1#Sx8 — Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 显式 evidence state 提高可追溯性，但新增 lineage、冲突、commit 与恢复语义，状态本身也必须被验证。 论文自身的边界信号是：The current system therefore improves evidence allocation, not end-to-end token efficiency.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`AGENT-RAG`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-25600:end -->

<!-- review:SF-2026-ARXIV-2607-25614:start -->
### MemSFT: Mitigating Alignment Tax with an External Parametric Memory

<!-- claim:SF-2026-ARXIV-2607-25614:start -->Adapting Large Language Models (LLMs) to specialized domains often incurs an alignment tax, as fine-tuning on domain-specific tasks can cause catastrophic forgetting and substantially degrade performance on general tasks. We propose MemSFT, which mitigates the alignment tax by decoupling domain specialization from backbone parameter updates through a plug-and-play parametric memory. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-25614:end -->

**为什么进入候选分母。** 摘要首要问题为“Adapting Large Language Models (LLMs) to specialized domains often incurs an alignment tax, as fine-tuning on domain-specific tasks can cause catastrophic forgetting and substantially degrade performance on general tasks.”；它把 context、memory、能力或进度变成持久且可验证的 agent state。

**机制与状态边界。** We propose MemSFT, which mitigates the alignment tax by decoupling domain specialization from backbone parameter updates through a plug-and-play parametric memory.

**证据证明什么。** Overall, our results demonstrate a practical path to decoupling general model capabilities from domain-specific knowledge at the parameter level, thereby equipping LLMs with new specialized capabilities without compromising their general capabilities.

**证据没有证明什么。** In addition, this paper focuses on supervised memory construction and does not explore reinforcement learning as an additional training stage. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.25614v1#S2 — 2 Method; https://arxiv.org/html/2607.25614v1#A3 — Appendix C Training and Implementation Details。Evaluation：https://arxiv.org/html/2607.25614v1#A1 — Appendix A Datasets and Evaluation Protocols; https://arxiv.org/html/2607.25614v1#A1.SS1 — A.1 Domain Specialization and Evaluation Data。Limitations / counterevidence：https://arxiv.org/html/2607.25614v1#S7 — 7 Conclusion; https://arxiv.org/html/2607.25614v1#S8 — 8 Limitations。

**Artifact boundary。** Exact v1 links https://github.com/LUMIA-Group/MemSFT, https://huggingface.co/collections/Jiarui-Wang/memsft, https://github.com/arXiv/html_feedback/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 显式 agent state 改善恢复与控制，但增加状态陈旧、错误提交、跨轮污染和一致性责任。 论文自身的边界信号是：In addition, this paper focuses on supervised memory construction and does not explore reinforcement learning as an additional training stage.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`TRAIN-SFT`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-25614:end -->

<!-- review:SF-2026-ARXIV-2607-25619:start -->
### SkillGate: Cost Efficient Runtime Malicious Skill File Detection in Coding Agents

<!-- claim:SF-2026-ARXIV-2607-25619:start -->Software engineering teams now deploy AI coding agents (Cursor, Claude Code, GitHub Copilot) as first-class productivity tools, installing domain-specific skill files to tailor agent behavior to project APIs, framework conventions, and organizational workflows. These complex Markdown files are easily downloaded from public registries with a single npx skills add command and no real security screening, representing a novel supply-chain attack surface: a malicious skill file can silently reprogram agent behavior, exfiltrating credentials, injecting backdoors into generated code, or redirecting agent actions to attacker-controlled endpoints. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-25619:end -->

**为什么进入候选分母。** 摘要首要问题为“Software engineering teams now deploy AI coding agents (Cursor, Claude Code, GitHub Copilot) as first-class productivity tools, installing domain-specific skill files to tailor agent behavior to project APIs, framework conventions, and organizational workflows.”；它改变执行安全的 trust boundary、guard 或 failure detection。

**机制与状态边界。** No systematic toolchain defense exists for this attack surface.

**证据证明什么。** On SkillsBench (n=1,650, 9.1% malicious), SkillGate achieves F1=0.817, FPR=1.13% while reducing LLM input tokens by 77% vs. full-file screening, and outperforming existing tools by 5-6x on threshold-independent AUPRC (0.830 vs.

**证据没有证明什么。** The prefilter patterns are derived from the MITRE ATT&CK taxonomy which is the most comprehensive pattern collection we could find, but cannot guarantee to cover all known security patterns. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.25619v1#S3 — III System Design & Evaluation Setup; https://arxiv.org/html/2607.25619v1#S2.SS4 — II-D Threat Model。Evaluation：https://arxiv.org/html/2607.25619v1#S3 — III System Design & Evaluation Setup; https://arxiv.org/html/2607.25619v1#S3.SS7 — III-G Experiment Setup。Limitations / counterevidence：https://arxiv.org/html/2607.25619v1#S2.SS4 — II-D Threat Model; https://arxiv.org/html/2607.25619v1#S6 — VI Threats to Validity。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 新的安全控制点降低特定失败，但会引入误拒绝、旁路、观测不足或模型/任务迁移问题。 论文自身的边界信号是：The prefilter patterns are derived from the MITRE ATT&CK taxonomy which is the most comprehensive pattern collection we could find, but cannot guarantee to cover all known security patterns.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`AGENT-SKILL`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-25619:end -->

<!-- review:SF-2026-ARXIV-2607-25635:start -->
### An Empirical Study of Model Context Protocol Applications

<!-- claim:SF-2026-ARXIV-2607-25635:start -->The Model Context Protocol (MCP) standardizes how large language model applications communicate with external tools, but leaves the application side unspecified: unlike traditional dependencies resolved through package managers, developers integrating MCP servers face no conventions for configuration, communication, or human oversight. This ecosystem is also under-researched, with existing work focused on servers rather than the applications consuming them. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-25635:end -->

**为什么进入候选分母。** 摘要首要问题为“The Model Context Protocol (MCP) standardizes how large language model applications communicate with external tools, but leaves the application side unspecified: unlike traditional dependencies resolved through package managers, developers integrating MCP servers face no conventions for configuration, communication, or human oversight.”；它改变 observable、对照组、判定粒度或外推边界，可能修正既有评测结论。

**机制与状态边界。** This ecosystem is also under-researched, with existing work focused on servers rather than the applications consuming them.

**证据证明什么。** Our results show that the ecosystem has converged on some practices but not others: most MCPApps configure servers using files (85.2%) and use an official SDK (81.1%) to communicate with servers, yet no naming convention has emerged for configuration files.

**证据没有证明什么。** Exact v1 does not disclose a dedicated generalization or deployment guarantee beyond its stated evaluation scope. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.25635v1#S4 — IV Methods: Analyzing MCPApps。Evaluation：https://arxiv.org/html/2607.25635v1#S4.SS1 — IV-A Manual Analysis and Taxonomy Derivation; https://arxiv.org/html/2607.25635v1#S4.SS3 — IV-C Evaluation。Limitations / counterevidence：https://arxiv.org/html/2607.25635v1#S6 — VI Discussion; https://arxiv.org/html/2607.25635v1#S7 — VII Threats to Validity。

**Artifact boundary。** Exact v1 links https://github.com/ChatGPTNextWeb/NextChat, https://github.com/daodao97/ChatMCP, https://github.com/google-gemini/gemini-cli; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：Exact v1 does not disclose a dedicated generalization or deployment guarantee beyond its stated evaluation scope.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`AGENT-MCP`；evidence-stage relation：`corrective_evidence`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-25635:end -->

<!-- review:SF-2026-ARXIV-2607-25637:start -->
### F(AI)2R: Who Did What, and Who Checked? Verifiable AI Provenance as an Executable Skill

<!-- claim:SF-2026-ARXIV-2607-25637:start -->F(AI)2R is FAIR research with AI in the loop, twice: an AI-assisted authoring pass and a machine-readable audit pass over every artefact. AI systems now draft, refactor, and verify research artefacts, yet their contributions are rarely recorded in a form a later human or machine can audit. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-25637:end -->

**为什么进入候选分母。** 摘要首要问题为“F(AI)2R is FAIR research with AI in the loop, twice: an AI-assisted authoring pass and a machine-readable audit pass over every artefact.”；它把 evidence identity、lineage、conflict 或 commit 变成显式系统状态。

**机制与状态边界。** AI systems now draft, refactor, and verify research artefacts, yet their contributions are rarely recorded in a form a later human or machine can audit.

**证据证明什么。** Every activity, claim, and source in its production is recorded in the repository's provenance graph under two invariants: no parentless claim, and verification rungs that only humans may grant.

**证据没有证明什么。** It would not, however, be tamper- proof , on three grounds. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.25637v1#S4 — IV The aiprov Method。Evaluation：https://arxiv.org/html/2607.25637v1#S6 — VI Meta-Experiment: This Paper as Case Study。Limitations / counterevidence：https://arxiv.org/html/2607.25637v1#S7 — VII Discussion and Limitations; https://arxiv.org/html/2607.25637v1#S8 — VIII Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/noheton/f-ai2-r, https://github.com/noheton/Obscurity-Is-Dead, https://github.com/noheton/f-ai-r; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 显式 evidence state 提高可追溯性，但新增 lineage、冲突、commit 与恢复语义，状态本身也必须被验证。 论文自身的边界信号是：It would not, however, be tamper- proof , on three grounds.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`AGENT-SKILL`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-25637:end -->

<!-- review:SF-2026-ARXIV-2607-25650:start -->
### PowerScale: Energy-Efficient Geo-Distributed Model Training with Federated Datacenter Power

<!-- claim:SF-2026-ARXIV-2607-25650:start -->The power demands of large-scale AI training increasingly exceed the capacity of any single data center, making geo-distributed training across power-constrained sites a practical necessity. Prior work optimizes such training mainly for time-to-accuracy using single-tier aggregation, where every site exchanges model updates directly with a central aggregator over the WAN each synchronization round, without accounting for the energy required to reach convergence. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-25650:end -->

**为什么进入候选分母。** 摘要首要问题为“The power demands of large-scale AI training increasingly exceed the capacity of any single data center, making geo-distributed training across power-constrained sites a practical necessity.”；它改变资源计量、分配、路由或迁移的控制权与约束。

**机制与状态边界。** To address these inefficiencies, we present PowerScale, a hierarchical aggregation system that exploits the latency hierarchy of wide-area networks.

**证据证明什么。** PowerScale matches or slightly improves time-to-accuracy compared with single-tier baselines while reducing energy consumption by up to 3.9x.

**证据没有证明什么。** Future work will investigate non-IID data distributions, optimal hierarchy depth selection, and composition with gradient compression techniques. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.25650v1#S3 — 3. PowerScale Design; https://arxiv.org/html/2607.25650v1#S5.SS1 — 5.1. Evaluation Methodology。Evaluation：https://arxiv.org/html/2607.25650v1#S5 — 5. Evaluation; https://arxiv.org/html/2607.25650v1#S5.SS1 — 5.1. Evaluation Methodology。Limitations / counterevidence：https://arxiv.org/html/2607.25650v1#S7 — 7. Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 动态资源控制提高利用率，但增加测量误差、迁移开销、租户公平和控制稳定性问题。 论文自身的边界信号是：Future work will investigate non-IID data distributions, optimal hierarchy depth selection, and composition with gradient compression techniques.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`TRAIN-DISTRIBUTED-TRAINING`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-25650:end -->

<!-- review:SF-2026-ARXIV-2607-25651:start -->
### Demystifying Deep Learning Compiler Frontend Bugs: An LLM-Aided Empirical Study

<!-- claim:SF-2026-ARXIV-2607-25651:start -->Deep learning compilers (DLCs) are designed to translate deep learning programs into optimized, hardware-specific code. Typically, DLC frontends translate programs into graph-based intermediate representations (IRs) to enable optimizations. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-25651:end -->

**为什么进入候选分母。** 摘要首要问题为“Deep learning compilers (DLCs) are designed to translate deep learning programs into optimized, hardware-specific code.”；它改变 observable、对照组、判定粒度或外推边界，可能修正既有评测结论。

**机制与状态边界。** To bridge this gap, we conduct the first systematic empirical study of \emph{fBug}s in TorchDynamo, the default DLC frontend for PyTorch 2, the most popular DL framework.

**证据证明什么。** We uncovered 23 previously unknown \emph{fBug}s in recent releases (15 confirmed) across eight (sub)categories, demonstrating the efficacy of our methodology in testing and hardening DLC frontends.

**证据没有证明什么。** Limitations and Future Work First, our test case synthesis is guided by root causes from known fBug s; for unseen bugs that fall outside the identified categories, the effectiveness of root-cause-aware generation is a concern. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.25651v1#S4 — 4. Methodology。Evaluation：https://arxiv.org/html/2607.25651v1#S3.SS1 — 3.1. Problem Analysis; https://arxiv.org/html/2607.25651v1#S4.SS2 — 4.2. LLM-Aided Bug Analysis。Limitations / counterevidence：https://arxiv.org/html/2607.25651v1#S6.SS4 — 6.4. Limitations and Future Work; https://arxiv.org/html/2607.25651v1#S6 — 6. Discussion。

**Artifact boundary。** Exact v1 links https://github.com/pytorch/pytorch/issues/176596, https://github.com/pytorch/pytorch/issues/176692, https://github.com/pytorch/pytorch/issues/150765; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：Limitations and Future Work First, our test case synthesis is guided by root causes from known fBug s; for unseen bugs that fall outside the identified categories, the effectiveness of root-cause-aware generation is a concern.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`INFER-TENSORRT-LLM`；evidence-stage relation：`corrective_evidence`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-25651:end -->

<!-- review:SF-2026-ARXIV-2607-25656:start -->
### OrchBench: Evaluating Multi-Agent Orchestration Plans in Isolation via Deterministic Simulation

<!-- claim:SF-2026-ARXIV-2607-25656:start -->Complex tasks often decompose into parallelizable yet interdependent subtasks, making orchestration critical to the performance of multi-agent systems (MAS). Existing evaluations typically rely on end-to-end execution, which conflates orchestration-plan quality with worker capabilities, tool reliability, and environmental noise. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-25656:end -->

**为什么进入候选分母。** 摘要首要问题为“Complex tasks often decompose into parallelizable yet interdependent subtasks, making orchestration critical to the performance of multi-agent systems (MAS).”；它改变 observable、对照组、判定粒度或外推边界，可能修正既有评测结论。

**机制与状态边界。** We present OrchBench, a simulation-based benchmark for evaluating multi-agent orchestration plans in isolation.

**证据证明什么。** These results establish OrchBench as an efficient and interpretable benchmark for comparing and diagnosing multi-agent orchestration plans.

**证据没有证明什么。** These failures help explain both the limitations of the generated benchmark problems and the common weaknesses of current models when they are asked to orchestrate multiple agents. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.25656v1#A4.SSx2 — II. Framework Dependence; https://arxiv.org/html/2607.25656v1#Sx4 — Methodology。Evaluation：https://arxiv.org/html/2607.25656v1#A1 — Appendix A A. Ablation Study; https://arxiv.org/html/2607.25656v1#A5 — Appendix E E. Benchmark Construction。Limitations / counterevidence：https://arxiv.org/html/2607.25656v1#A5.SSx3 — III. Generation Failure Cases; https://arxiv.org/html/2607.25656v1#A6.SSx1 — I. Detailed Discussion of the Main Results。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：These failures help explain both the limitations of the generated benchmark problems and the common weaknesses of current models when they are asked to orchestrate multiple agents.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`AGENT-MULTI-AGENT`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-25656:end -->

<!-- review:SF-2026-ARXIV-2607-25659:start -->
### CoRT: Counterfactual Replay for Token-Level Rubric-Guided Policy Optimization

<!-- claim:SF-2026-ARXIV-2607-25659:start -->Rubric-based reinforcement learning enriches language model training by evaluating model outputs against explicit criteria. Yet in GRPO-style pipelines, these structured judgments are reduced to a scalar response-level reward and converted into a response-level advantage, which is broadcast uniformly to all generated tokens. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-25659:end -->

**为什么进入候选分母。** 摘要首要问题为“Rubric-based reinforcement learning enriches language model training by evaluating model outputs against explicit criteria.”；它改变训练信号、capacity 或 update ownership，而非只报告任务精度。

**机制与状态边界。** We propose CoRT, a token-level credit weighting method for rubric-conditioned GRPO.

**证据证明什么。** Experiments across instruction-tuned models and reward granularities show that CoRT improves over matched response-level GRPO in the vast majority of comparisons, with an average gain of 4.4 percentage points.

**证据没有证明什么。** These results support the view that structured criteria can be useful not only for scoring responses, but also for guiding where credit is assigned within a response. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.25659v1#Sx1 — Introduction; https://arxiv.org/html/2607.25659v1#Sx2 — Related Work。Evaluation：https://arxiv.org/html/2607.25659v1#A1 — Appendix A Additional Results; https://arxiv.org/html/2607.25659v1#Sx5 — Experimental Setup。Limitations / counterevidence：https://arxiv.org/html/2607.25659v1#A1.SSx6 — Failure-Mode Diagnostics; https://arxiv.org/html/2607.25659v1#Sx8 — Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更密集或更定向的训练信号改善样本效率，但会增加 verifier 偏差、分布迁移和优化耦合。 论文自身的边界信号是：These results support the view that structured criteria can be useful not only for scoring responses, but also for guiding where credit is assigned within a response.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`TRAIN-GRPO`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-25659:end -->

<!-- review:SF-2026-ARXIV-2607-25663:start -->
### Localized Adaptation Reveals Distinct Learning Signatures in Transformers

<!-- claim:SF-2026-ARXIV-2607-25663:start -->Transformer adaptation is typically distributed across model depth, even when the intended change is narrow. We investigate how adaptation site shapes what a model learns, how well that learning generalizes, and how selectively it is applied. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-25663:end -->

**为什么进入候选分母。** 摘要首要问题为“Transformer adaptation is typically distributed across model depth, even when the intended change is narrow.”；它改变训练信号、capacity 或 update ownership，而非只报告任务精度。

**机制与状态边界。** We introduce a controlled benchmark spanning five objectives (lexical binding, factual association, behavioral policy learning, causal mapping, and procedural reasoning) and define each objective's "adaptation geometry" as its profile of acquisition, transfer, and boundedness under full-stack and early-, middle-, or late-layer LoRA.

**证据证明什么。** These findings establish adaptation site as a key design variable for controlling what models learn, generalize, and leave unchanged.

**证据没有证明什么。** Limitations and Future Directions This study has several limitations. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.25663v1#Sx3 — Methodology; https://arxiv.org/html/2607.25663v1#Sx6.SSx1 — Adaptation Site is a Functional Design Variable。Evaluation：https://arxiv.org/html/2607.25663v1#Sx9 — Appendix C: Localization Experiments Results; https://arxiv.org/html/2607.25663v1#Sx11 — Appendix E: Budget Sensitivity Analysis。Limitations / counterevidence：https://arxiv.org/html/2607.25663v1#Sx6.SSx3 — Limitations and Future Directions; https://arxiv.org/html/2607.25663v1#Sx6 — Discussion。

**Artifact boundary。** Exact v1 links https://github.com/rramnauth2220/adaptation-geometries, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更密集或更定向的训练信号改善样本效率，但会增加 verifier 偏差、分布迁移和优化耦合。 论文自身的边界信号是：Limitations and Future Directions This study has several limitations.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`MODEL-TRANSFORMER-LAYER`；evidence-stage relation：`corrective_evidence`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-25663:end -->

<!-- review:SF-2026-ARXIV-2607-25669:start -->
### OmniDelta: Skill-Driven Budget Allocation for Token Compression in OmniLLMs

<!-- claim:SF-2026-ARXIV-2607-25669:start -->Emerging Omni-modal Large Language Models (OmniLLMs) enable unified understanding of text, audio, and video, but their long audio-video token sequences introduce substantial memory and inference costs. Existing compression methods mainly focus on selecting important tokens under fixed budgets, leaving the preceding budget-allocation problem underexplored. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-25669:end -->

**为什么进入候选分母。** 摘要首要问题为“Emerging Omni-modal Large Language Models (OmniLLMs) enable unified understanding of text, audio, and video, but their long audio-video token sequences introduce substantial memory and inference costs.”；它改变资源计量、分配、路由或迁移的控制权与约束。

**机制与状态边界。** To address these limitations, we propose OmniDelta, a training-free, skill-driven framework that couples intent-aware inter-modal allocation with content-aware intra-modal allocation.

**证据证明什么。** At 25% token retention on Qwen2.5-Omni-7B, OmniDelta reduces GPU memory by 22.0% and achieves a 1.64x end-to-end speedup over full-token inference.

**证据没有证明什么。** Instead of only selecting important tokens, OmniDelta decides where a fixed retained-token budget should be spent, using query-skill similarity for audio-video budget shifting and local redundancy/complexity for audio segment and video frame allocation, while remaining compatible with existing pruning strategies. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.25669v1#S3 — 3 Method; https://arxiv.org/html/2607.25669v1#S3.SS2 — 3.2 Our Method: OmniDelta。Evaluation：https://arxiv.org/html/2607.25669v1#S4 — 4 Experiments; https://arxiv.org/html/2607.25669v1#S4.SS1 — 4.1 Experimental Setting。Limitations / counterevidence：https://arxiv.org/html/2607.25669v1#S6 — 6 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 动态资源控制提高利用率，但增加测量误差、迁移开销、租户公平和控制稳定性问题。 论文自身的边界信号是：Instead of only selecting important tokens, OmniDelta decides where a fixed retained-token budget should be spent, using query-skill similarity for audio-video budget shifting and local redundancy/complexity for audio segment and video frame allocation, while remaining compatible with existing pruning strategies.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`MULTIMODAL-REPRESENTATION`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-25669:end -->

<!-- review:SF-2026-ARXIV-2607-25718:start -->
### Tools Are Not Islands: Set-Level Tool Retrieval for LLM Agents via Query-Conditioned Hyperedge Prediction

<!-- claim:SF-2026-ARXIV-2607-25718:start -->Large language model (LLM) agents increasingly rely on invoking external tools to complete real-world tasks. Tool retrieval, which selects a small task-relevant subset from a library of thousands of tools before the agent acts, has therefore become a critical component of LLM agent pipelines. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-25718:end -->

**为什么进入候选分母。** 摘要首要问题为“Large language model (LLM) agents increasingly rely on invoking external tools to complete real-world tasks.”；它把 context、memory、能力或进度变成持久且可验证的 agent state。

**机制与状态边界。** In this paper, we propose HYSET, short for HYperedge-based SEt-level Tool retrieval.

**证据证明什么。** Experiments on ToolBench demonstrate that HYSET consistently outperforms state-of-the-art baselines in both tool retrieval performance and end-to-end task success.

**证据没有证明什么。** Extending it to dynamically growing tool libraries is a natural direction for future work. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.25718v1#S2 — 2 Methodology; https://arxiv.org/html/2607.25718v1#S2.SS4 — 2.4 The Framework of HYSET。Evaluation：https://arxiv.org/html/2607.25718v1#S3 — 3 Experiments; https://arxiv.org/html/2607.25718v1#S3.SS1 — 3.1 Experimental Setup。Limitations / counterevidence：https://arxiv.org/html/2607.25718v1#S4 — 4 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 显式 agent state 改善恢复与控制，但增加状态陈旧、错误提交、跨轮污染和一致性责任。 论文自身的边界信号是：Extending it to dynamically growing tool libraries is a natural direction for future work.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`AGENT-TOOL-CALLING`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-25718:end -->

<!-- review:SF-2026-ARXIV-2607-25750:start -->
### Detecting CSAM Text-to-Image LoRAs From Weights

<!-- claim:SF-2026-ARXIV-2607-25750:start -->Low-rank adaptation (LoRA) fine-tuning has made it cheap and easy to customize open-weight image generation models for specific tasks, including the production of child sexual abuse material (CSAM). Existing moderation relies on metadata or generated outputs, but metadata can be deceptive and generating outputs may itself be unacceptable or illegal. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-25750:end -->

**为什么进入候选分母。** 摘要首要问题为“Low-rank adaptation (LoRA) fine-tuning has made it cheap and easy to customize open-weight image generation models for specific tasks, including the production of child sexual abuse material (CSAM).”；它改变执行安全的 trust boundary、guard 或 failure detection。

**机制与状态边界。** Existing moderation relies on metadata or generated outputs, but metadata can be deceptive and generating outputs may itself be unacceptable or illegal.

**证据证明什么。** We show that a safer signal lives in the weights.

**证据没有证明什么。** The results also suggest could support mitigation as well as detection, suppressing a concept in weight space rather than only flagging it, which is an avenue for future work ( Arditi et al. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.25750v1#A1 — Appendix A Implementation and Experimental Details。Evaluation：https://arxiv.org/html/2607.25750v1#A1 — Appendix A Implementation and Experimental Details; https://arxiv.org/html/2607.25750v1#A3 — Appendix C Additional Results。Limitations / counterevidence：https://arxiv.org/html/2607.25750v1#Sx5 — Limitations; https://arxiv.org/html/2607.25750v1#Sx7 — Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 新的安全控制点降低特定失败，但会引入误拒绝、旁路、观测不足或模型/任务迁移问题。 论文自身的边界信号是：The results also suggest could support mitigation as well as detection, suppressing a concept in weight space rather than only flagging it, which is an avenue for future work ( Arditi et al.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`PLATFORM-MODEL-REGISTRY`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-25750:end -->

<!-- review:SF-2026-ARXIV-2607-25765:start -->
### WorkSurface-Bench: Benchmarking Enterprise Agents on Multi-Surface Knowledge Routing

<!-- claim:SF-2026-ARXIV-2607-25765:start -->Enterprise agents often need to integrate heterogeneous knowledge sources: documents for narrative facts, tables for computation, and dependency graphs for file relationships. Existing benchmarks typically evaluate retrieval or tool use without distinguishing whether an agent first selects the appropriate knowledge sources. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-25765:end -->

**为什么进入候选分母。** 摘要首要问题为“Enterprise agents often need to integrate heterogeneous knowledge sources: documents for narrative facts, tables for computation, and dependency graphs for file relationships.”；它改变 observable、对照组、判定粒度或外推边界，可能修正既有评测结论。

**机制与状态边界。** We introduce WorkSurface-Bench, a benchmark for evaluating this capability as surface routing.

**证据证明什么。** Matched interventions further show that surface hints improve Answer for three of four models, whereas removing irrelevant tools primarily improves routing and efficiency.

**证据没有证明什么。** These interventions are controls, not evidence of autonomous routing ability. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.25765v1#S3.SS4 — 3.4 Automatic Validation and Model-assisted Screening。Evaluation：https://arxiv.org/html/2607.25765v1#S3 — 3 Benchmark Construction; https://arxiv.org/html/2607.25765v1#S5 — 5 Experiments。Limitations / counterevidence：https://arxiv.org/html/2607.25765v1#S6 — 6 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/haolpku/WorkSurface-Bench, https://huggingface.co/datasets/lhpku20010120/WorkSurface-Bench, https://github.com/arXiv/html_feedback/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：These interventions are controls, not evidence of autonomous routing ability.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`PLATFORM-EVALUATION-SYSTEM`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-25765:end -->

<!-- review:SF-2026-ARXIV-2607-25798:start -->
### Transformer Transformer: A Unified Model for Motion-Conditioned Robot Co-design

<!-- claim:SF-2026-ARXIV-2607-25798:start -->An often overlooked factor of robot manipulation performance is the embodiment of the robot itself. Motivated by this problem, we study motion-conditioned robot co-design, where the goal is to generate complete robot designs that track target end-effector trajectories (from human demonstrations) while optimizing user-defined rewards. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-25798:end -->

**为什么进入候选分母。** 摘要首要问题为“An often overlooked factor of robot manipulation performance is the embodiment of the robot itself.”；它提出可跨 workload 讨论的表示、状态或计算机制，并暴露旧方案边界。

**机制与状态边界。** We introduce Transformer Transformer, a diffusion transformer trained on RoboTokens, a unified tokenization of robot embodiments, states, and actions.

**证据证明什么。** Finally, we fabricated an optimized ALOHA design, which reduced tracking error by over 70% compared to the original design.

**证据没有证明什么。** Exact v1 does not disclose a dedicated generalization or deployment guarantee beyond its stated evaluation scope. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.25798v1#S2 — 2 Method; https://arxiv.org/html/2607.25798v1#S2.SS2 — 2.2 Transformer Transformer: A Unifying Architecture。Evaluation：https://arxiv.org/html/2607.25798v1#S3 — 3 Results; https://arxiv.org/html/2607.25798v1#S7 — 7 Additional Experiments。Limitations / counterevidence：https://arxiv.org/html/2607.25798v1#S5 — 5 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/kevinzakka/mink, http://github.com/google-deepmind/mujoco_menagerie, https://github.com/Genesis-Embodied-AI/Genesis; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 新表示或状态机制扩大能力边界，但带来额外训练、状态管理、稳定性或泛化假设。 论文自身的边界信号是：Exact v1 does not disclose a dedicated generalization or deployment guarantee beyond its stated evaluation scope.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`MULTIMODAL-EMBODIED-VLA`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-25798:end -->

<!-- review:SF-2026-ARXIV-2607-25816:start -->
### Speculate While You Reason: Teaching Agents to Predict Their Next Tool Call via Joint Agent-Speculator RL

<!-- claim:SF-2026-ARXIV-2607-25816:start -->Large language model agents often spend substantial wall-clock time waiting for tool call results. Tool-call speculation can hide this latency by predicting and pre-executing an agent's next tool call if the prediction matches the agent's eventual tool call, but existing speculators are typically separate draft models or cached traces that are poorly aligned with the deployed agent's own behavior. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-25816:end -->

**为什么进入候选分母。** 摘要首要问题为“Large language model agents often spend substantial wall-clock time waiting for tool call results.”；它把 context、memory、能力或进度变成持久且可验证的 agent state。

**机制与状态边界。** To enable this dual-mode agent without degrading performance, we propose a joint agent-speculator reinforcement learning method, which derives speculation targets from the agent's own rollouts and alternates agent and speculator updates.

**证据证明什么。** Large language model agents often spend substantial wall-clock time waiting for tool call results.

**证据没有证明什么。** Our empirical evaluation is also limited in scope. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.25816v1#S3 — 3 Method; https://arxiv.org/html/2607.25816v1#A1 — Appendix A Implementation Details。Evaluation：https://arxiv.org/html/2607.25816v1#S2.SS1 — 2.1 Evaluation Protocol; https://arxiv.org/html/2607.25816v1#S4 — 4 Experiments。Limitations / counterevidence：https://arxiv.org/html/2607.25816v1#S6 — 6 Conclusion; https://arxiv.org/html/2607.25816v1#Sx1 — Limitations。

**Artifact boundary。** Exact v1 links https://huggingface.co/Qwen/Qwen3.5-4B, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 显式 agent state 改善恢复与控制，但增加状态陈旧、错误提交、跨轮污染和一致性责任。 论文自身的边界信号是：Our empirical evaluation is also limited in scope.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`INFER-SPECULATIVE-DECODING`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-25816:end -->

<!-- review:SF-2026-ARXIV-2607-25818:start -->
### SepPrune:A Separator-based Pruning Framework for Efficient Multimodal Large Language Models

<!-- claim:SF-2026-ARXIV-2607-25818:start -->Recent multimodal large language models (MLLMs), such as Qwen2.5-VL and InternVL3, generate large numbers of vision tokens for high-resolution inputs, leading to substantial computational cost. Existing vision token pruning methods either depend on cross-modal attention and cannot prune before the prefill stage, or rely on diversity estimation with high computational overhead. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-25818:end -->

**为什么进入候选分母。** 摘要首要问题为“Recent multimodal large language models (MLLMs), such as Qwen2.5-VL and InternVL3, generate large numbers of vision tokens for high-resolution inputs, leading to substantial computational cost.”；它改变资源计量、分配、路由或迁移的控制权与约束。

**机制与状态边界。** Based on this observation, we propose SepPrune, an efficient, training-free, plug-and-play pruning method that uses the separator token as a unified query to rank and select informative vision tokens.

**证据证明什么。** Experiments on Qwen2.5-VL-7B show that SepPrune achieves state-of-the-art performance, retaining 96.3% of the original accuracy while removing 80.2% of vision tokens.

**证据没有证明什么。** Exact v1 does not disclose a dedicated generalization or deployment guarantee beyond its stated evaluation scope. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.25818v1#S3 — III Method; https://arxiv.org/html/2607.25818v1#S3.SS1 — III-A SepPrune: Method Overview。Evaluation：https://arxiv.org/html/2607.25818v1#S4 — IV Experiments; https://arxiv.org/html/2607.25818v1#S4.SS1 — IV-A Main results。Limitations / counterevidence：https://arxiv.org/html/2607.25818v1#S5 — V Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 动态资源控制提高利用率，但增加测量误差、迁移开销、租户公平和控制稳定性问题。 论文自身的边界信号是：Exact v1 does not disclose a dedicated generalization or deployment guarantee beyond its stated evaluation scope.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`MULTIMODAL-REPRESENTATION`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-25818:end -->

<!-- review:SF-2026-ARXIV-2607-25825:start -->
### CHILL-Harness: Counterfactual Harness Learning for Efficient Reasoning in Long-Horizon Agents

<!-- claim:SF-2026-ARXIV-2607-25825:start -->Agent harnesses have become the operational infrastructure of modern large language model agents, coordinating context, tools, verification, and execution control to translate latent model capability into reliable long-horizon behavior. However, reliable long-horizon behavior requires harness control to adapt to task demands, execution environments, and evolving execution states, whereas current harnesses predominantly rely on hand-crafted or globally fixed policies; this mismatch manifests as unnecessary computational overhead and, in adverse cases, reduced task success. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-25825:end -->

**为什么进入候选分母。** 摘要首要问题为“Agent harnesses have become the operational infrastructure of modern large language model agents, coordinating context, tools, verification, and execution control to translate latent model capability into reliable long-horizon behavior.”；它改变训练信号、capacity 或 update ownership，而非只报告任务精度。

**机制与状态边界。** To address this limitation, we formulate the task of enabling adaptive orchestration in harness systems as a causal learning problem and propose Counterfactual Harness Intervention Learning for Long-Horizon Agents (CHILL-Harness).

**证据证明什么。** Extensive experiments on heterogeneous long-horizon tasks spanning information seeking, software engineering, and terminal interaction show that CHILL-Harness consistently preserves or improves task success while substantially reducing token consumption and execution time.

**证据没有证明什么。** Exact v1 does not disclose a dedicated generalization or deployment guarantee beyond its stated evaluation scope. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.25825v1#Sx1 — Introduction; https://arxiv.org/html/2607.25825v1#Sx2 — Preliminaries and Related Work。Evaluation：https://arxiv.org/html/2607.25825v1#Sx4.SSx3 — Ablation Experiment; https://arxiv.org/html/2607.25825v1#Sx4 — Experiments。Limitations / counterevidence：https://arxiv.org/html/2607.25825v1#Sx5 — Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/csdstar/chill-dev, https://github.com/krafton-ai/kira, https://github.com/arXiv/html_feedback/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更密集或更定向的训练信号改善样本效率，但会增加 verifier 偏差、分布迁移和优化耦合。 论文自身的边界信号是：Exact v1 does not disclose a dedicated generalization or deployment guarantee beyond its stated evaluation scope.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`AGENT-WORKFLOW`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-25825:end -->

<!-- review:SF-2026-ARXIV-2607-25831:start -->
### WarmTuner: Program-Specific Warm Starts for Compiler Autotuning via Offline-to-Online Reinforcement Learning

<!-- claim:SF-2026-ARXIV-2607-25831:start -->Compilers are fundamental software tools that translate high-level programs into machine code. Modern compilers expose hundreds of optimizations, each turned on or off through an optimization flag, to improve the performance of the generated code. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-25831:end -->

**为什么进入候选分母。** 摘要首要问题为“Compilers are fundamental software tools that translate high-level programs into machine code.”；它改变资源计量、分配、路由或迁移的控制权与约束。

**机制与状态边界。** We propose WarmTuner, an offline-to-online reinforcement learning framework that instead turns historical records into a program-conditioned policy that predicts each flag's setting over the full flag space and remains adaptable on the target program.

**证据证明什么。** The results show that WarmTuner achieves an average speedup of 1.732x over GCC -O3 and obtains the best result on 14/30 programs, significantly outperforming the compared techniques.

**证据没有证明什么。** To reduce this threat, we evaluate WarmTuner on cBench and PolyBench, which are commonly used in compiler auto-tuning works [ 16 , 17 , 18 , 8 ] . 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.25831v1#S3.SS3 — III-C Implementation。Evaluation：https://arxiv.org/html/2607.25831v1#S4 — IV Experimental Results; https://arxiv.org/html/2607.25831v1#S4.SS2 — IV-B Ablation Analysis (RQ2)。Limitations / counterevidence：https://arxiv.org/html/2607.25831v1#S5 — V Threats to Validity; https://arxiv.org/html/2607.25831v1#S6 — VI Discussion。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 动态资源控制提高利用率，但增加测量误差、迁移开销、租户公平和控制稳定性问题。 论文自身的边界信号是：To reduce this threat, we evaluate WarmTuner on cBench and PolyBench, which are commonly used in compiler auto-tuning works [ 16 , 17 , 18 , 8 ] .

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`INFER-TENSORRT-LLM`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-25831:end -->

<!-- review:SF-2026-ARXIV-2607-25852:start -->
### AngelSpec: Towards Real-World High Performance Inference with Speculative Decoding

<!-- claim:SF-2026-ARXIV-2607-25852:start -->Speculative decoding accelerates large language model inference without changing the target distribution, but no single drafting structure performs best across real-world workloads. Autoregressive multi-token prediction (MTP) is a lightweight, stable proposal mechanism, whereas block-parallel diffusion amortizes drafting latency over much longer candidate sequences; the better choice depends strongly on the output distribution. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-25852:end -->

**为什么进入候选分母。** 摘要首要问题为“Speculative decoding accelerates large language model inference without changing the target distribution, but no single drafting structure performs best across real-world workloads.”；它改变推理期状态放置、数据移动、执行控制或实时 SLO。

**机制与状态边界。** We present AngelSpec, a unified training framework for MTP and block-parallel speculative decoding that addresses this heterogeneity at three levels.

**证据证明什么。** We release AngelSpec to support training and extending these methods.

**证据没有证明什么。** We also release the AngelSpec framework with unified support for MTP and block-parallel speculative decoding, providing a common foundation for training, evaluating, and extending future drafter designs. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.25852v1#S3.SS3 — 3.3 Loss Design; https://arxiv.org/html/2607.25852v1#S6 — 6 AngelSpec Framework。Evaluation：https://arxiv.org/html/2607.25852v1#S2.SS5 — 2.5 Experimental Results; https://arxiv.org/html/2607.25852v1#S3.SS4 — 3.4 Main Results。Limitations / counterevidence：https://arxiv.org/html/2607.25852v1#S8 — 8 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/Tencent/AngelSpec, https://github.com/lightseekorg/TorchSpec, https://github.com/arXiv/html_feedback/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更激进的缓存、迁移、并行或专用执行会换取吞吐/时延，同时增加配置依赖、资源压力与回退路径。 论文自身的边界信号是：We also release the AngelSpec framework with unified support for MTP and block-parallel speculative decoding, providing a common foundation for training, evaluating, and extending future drafter designs.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`INFER-SPECULATIVE-DECODING`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-25852:end -->

<!-- review:SF-2026-ARXIV-2607-25853:start -->
### HiSkill: Empowering LLM Agents with Hierarchical Skill Graphs

<!-- claim:SF-2026-ARXIV-2607-25853:start -->Skills have become an important abstraction for enabling large language model (LLM) agents to reuse past experience in long-horizon interactive tasks. However, existing trajectory-to-skill methods often produce flat collections of high-level textual skills that are stored and retrieved independently, leaving skill relations underutilized and maintaining a gap between high-level skills and executable actions. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-25853:end -->

**为什么进入候选分母。** 摘要首要问题为“Skills have become an important abstraction for enabling large language model (LLM) agents to reuse past experience in long-horizon interactive tasks.”；它把 context、memory、能力或进度变成持久且可验证的 agent state。

**机制与状态边界。** In this paper, we propose HiSkill, a hierarchical skill graph framework that organizes interaction trajectories into a directed graph with skill nodes, AtomicOp nodes, and typed edges.

**证据证明什么。** Experiments on three interactive environments show that HiSkill outperforms state-of-the-art baselines while reducing inference token consumption, demonstrating the effectiveness of bridging high-level skills and executable action grounding through a hierarchical skill graph.

**证据没有证明什么。** Future work will explore online skill graph evolution, adaptive skill refinement, and broader applications to more open-ended interactive scenarios. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.25853v1#S3 — 3 Methodology; https://arxiv.org/html/2607.25853v1#S3.SS1 — 3.1 Framework Overview。Evaluation：https://arxiv.org/html/2607.25853v1#A5 — Appendix E Additional Experimental Results; https://arxiv.org/html/2607.25853v1#A5.SS1 — E.1 Main Results on GPT-5.2-Codex。Limitations / counterevidence：https://arxiv.org/html/2607.25853v1#S5 — 5 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/LabRAI/LangSkills, https://openai.com/index/introducing-gpt-5-2-codex, https://github.com/arXiv/html_feedback/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 显式 agent state 改善恢复与控制，但增加状态陈旧、错误提交、跨轮污染和一致性责任。 论文自身的边界信号是：Future work will explore online skill graph evolution, adaptive skill refinement, and broader applications to more open-ended interactive scenarios.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`AGENT-SKILL`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-25853:end -->

<!-- review:SF-2026-ARXIV-2607-25857:start -->
### Shieldstral

<!-- claim:SF-2026-ARXIV-2607-25857:start -->We introduce Shieldstral, a 3B-parameter policy-adaptive multimodal safety classifier that matches or outperforms models nearly 7$\times$ its size on text safety benchmarks and sets a new state of the art on multimodal safety classification. Shieldstral formulates content moderation as a binary question-answering task. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-25857:end -->

**为什么进入候选分母。** 摘要首要问题为“We introduce Shieldstral, a 3B-parameter policy-adaptive multimodal safety classifier that matches or outperforms models nearly 7$\times$ its size on text safety benchmarks and sets a new state of the art on multimodal safety classification.”；它改变执行安全的 trust boundary、guard 或 failure detection。

**机制与状态边界。** We present the data construction recipe, covering curation and generation of approximately 54.1M samples and a fine-grained evaluation set to evaluate policy adaptability.

**证据证明什么。** Together, these enable a small adaptive model to match or outperform much larger models.

**证据没有证明什么。** Exact v1 does not disclose a dedicated generalization or deployment guarantee beyond its stated evaluation scope. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.25857v1#S4.SS1 — 4.1 Taxonomy Design; https://arxiv.org/html/2607.25857v1#S5 — 5 Model Architecture。Evaluation：https://arxiv.org/html/2607.25857v1#A1 — Appendix A Multilingual Evaluation Results; https://arxiv.org/html/2607.25857v1#A2 — Appendix B Full Evaluation Taxonomy。Limitations / counterevidence：https://arxiv.org/html/2607.25857v1#S8 — 8 Conclusion。

**Artifact boundary。** Exact v1 links https://huggingface.co/nvidia/Nemotron-3.5-Content-Safety, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 新的安全控制点降低特定失败，但会引入误拒绝、旁路、观测不足或模型/任务迁移问题。 论文自身的边界信号是：Exact v1 does not disclose a dedicated generalization or deployment guarantee beyond its stated evaluation scope.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`PLATFORM-SECURITY`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-25857:end -->

<!-- review:SF-2026-ARXIV-2607-25877:start -->
### Runtime Uncertainty Monitoring for LLM-Based Multi-Agent Systems Using Bayesian Networks

<!-- claim:SF-2026-ARXIV-2607-25877:start -->This paper investigates how multi-agent systems (MAS)-based on large language models (LLMs) can support actuarial risk modelling, with a particular focus on uncertainty quantification. Actuarial workflows represent a high-stakes decision-support setting where unreliable outputs may lead to incorrect risk assessment, unfair pricing, and regulatory non-compliance. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-25877:end -->

**为什么进入候选分母。** 摘要首要问题为“This paper investigates how multi-agent systems (MAS)-based on large language models (LLMs) can support actuarial risk modelling, with a particular focus on uncertainty quantification.”；它把 evidence identity、lineage、conflict 或 commit 变成显式系统状态。

**机制与状态边界。** Results show that the framework reproduces baseline actuarial performance while providing additional insight into workflow stability and runtime uncertainty propagation.

**证据证明什么。** Results show that the framework reproduces baseline actuarial performance while providing additional insight into workflow stability and runtime uncertainty propagation.

**证据没有证明什么。** However, the effectiveness of the approach depends on the selected LLM backend, with differences observed in error detection, adaptability, and uncertainty behaviour. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.25877v1#S3 — 3 Multi-agent system design; https://arxiv.org/html/2607.25877v1#S2.SS1 — 2.1 Multi-Agent Systems。Evaluation：https://arxiv.org/html/2607.25877v1#S5 — 5 Evaluation。Limitations / counterevidence：https://arxiv.org/html/2607.25877v1#S6 — 6 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 显式 evidence state 提高可追溯性，但新增 lineage、冲突、commit 与恢复语义，状态本身也必须被验证。 论文自身的边界信号是：However, the effectiveness of the approach depends on the selected LLM backend, with differences observed in error detection, adaptability, and uncertainty behaviour.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`AGENT-MULTI-AGENT`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-25877:end -->

<!-- review:SF-2026-ARXIV-2607-25880:start -->
### Stemma: Induced Decision Regions Reveal LLM Provenance

<!-- claim:SF-2026-ARXIV-2607-25880:start -->LLM provenance testing asks whether a suspect LLM belongs to the same lineage as a source. Existing black-box methods largely infer this relationship from response-level characteristics, but these characteristics may shift under adaptation or deployment even when the underlying meaning remains unchanged, weakening the reliability of provenance evidence. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-25880:end -->

**为什么进入候选分母。** 摘要首要问题为“LLM provenance testing asks whether a suspect LLM belongs to the same lineage as a source.”；它把 evidence identity、lineage、conflict 或 commit 变成显式系统状态。

**机制与状态边界。** Building on this signal, we propose Stemma, a practical black-box LLM fingerprinting method that operationalises stability, robustness, and specificity as complementary probe-selection principles for reliably estimating induced decision region inheritance.

**证据证明什么。** Across 770 source-suspect pairs drawn from 56 public checkpoints and spanning diverse model-weight transformations, Stemma achieves 0.967 AUC and 87.8% TPR at 1% FPR, substantially outperforming four representative baselines.

**证据没有证明什么。** Exact v1 does not disclose a dedicated generalization or deployment guarantee beyond its stated evaluation scope. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.25880v1#S4 — 4 Stemma Design; https://arxiv.org/html/2607.25880v1#A3 — Appendix C Stemma Implementation and Configuration Details。Evaluation：https://arxiv.org/html/2607.25880v1#A9 — Appendix I Full Ablation Results; https://arxiv.org/html/2607.25880v1#A4 — Appendix D Model Benchmark。Limitations / counterevidence：https://arxiv.org/html/2607.25880v1#S6 — 6 Discussion and Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/kerryzhangcode/Stemma, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 显式 evidence state 提高可追溯性，但新增 lineage、冲突、commit 与恢复语义，状态本身也必须被验证。 论文自身的边界信号是：Exact v1 does not disclose a dedicated generalization or deployment guarantee beyond its stated evaluation scope.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`PLATFORM-MODEL-REGISTRY`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-25880:end -->

<!-- review:SF-2026-ARXIV-2607-25883:start -->
### Towards a Systems Foundation for Agentic Cloud Management

<!-- claim:SF-2026-ARXIV-2607-25883:start -->Agentic cloud management is emerging as a practice to automate laborious operations, minimize toil, and improve responsiveness. Despite the rapid development of autonomous management agents, we argue that the fundamental missing piece is a systems foundation to enable safe, effective operations across agents and between agents and human operators. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-25883:end -->

**为什么进入候选分母。** 摘要首要问题为“Agentic cloud management is emerging as a practice to automate laborious operations, minimize toil, and improve responsiveness.”；它把 context、memory、能力或进度变成持久且可验证的 agent state。

**机制与状态边界。** Despite the rapid development of autonomous management agents, we argue that the fundamental missing piece is a systems foundation to enable safe, effective operations across agents and between agents and human operators.

**证据证明什么。** Agentic cloud management is emerging as a practice to automate laborious operations, minimize toil, and improve responsiveness.

**证据没有证明什么。** The deployment overhead of CloudWeaver is modest because the system operates only on compact resource metadata, dependency edges, lock states, and escrow counters. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.25883v1#S3 — 3. Towards a Systems Foundation; https://arxiv.org/html/2607.25883v1#S3.SS2 — 3.2. Design Principles。Evaluation：https://arxiv.org/html/2607.25883v1#S1 — 1. Introduction; https://arxiv.org/html/2607.25883v1#S2 — 2. Background。Limitations / counterevidence：https://arxiv.org/html/2607.25883v1#S6 — 6. Discussion and Future Work。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 显式 agent state 改善恢复与控制，但增加状态陈旧、错误提交、跨轮污染和一致性责任。 论文自身的边界信号是：The deployment overhead of CloudWeaver is modest because the system operates only on compact resource metadata, dependency edges, lock states, and escrow counters.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`AGENT-PLATFORM`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-25883:end -->

<!-- review:SF-2026-ARXIV-2607-25884:start -->
### CONQuER: Hardware-Aware Mixed-Precision Quantisation with Online-Calibrated Surrogates

<!-- claim:SF-2026-ARXIV-2607-25884:start -->Deploying deep neural networks on resource-constrained hardware relies on mixed-precision quantisation (MPQ). current deployment toolchains severely fragment this process. Quantisation typically occurs as a hardware-agnostic preprocessing step in front-end frameworks, disconnected from the downstream compilers that generate the physical machine code. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-25884:end -->

**为什么进入候选分母。** 摘要首要问题为“Deploying deep neural networks on resource-constrained hardware relies on mixed-precision quantisation (MPQ).”；它改变资源计量、分配、路由或迁移的控制权与约束。

**机制与状态边界。** We present CONQuER, a unified compiler-integrated infrastructure for hardware-aware MPQ.

**证据证明什么。** Evaluation across mobile and laptop CPUs, and server GPUs demonstrates that optimal quantisation policies are hardware-dependent.

**证据没有证明什么。** Future work will expand CONQuER across three primary vectors. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.25884v1#S1 — I Introduction; https://arxiv.org/html/2607.25884v1#S2 — II CONQuER Search and Compiler Infrastructure。Evaluation：https://arxiv.org/html/2607.25884v1#S4.SS3 — IV-C RQ3: Ablation Analysis; https://arxiv.org/html/2607.25884v1#S3 — III Evaluation。Limitations / counterevidence：https://arxiv.org/html/2607.25884v1#S7 — VII Conclusion and Future Work; https://arxiv.org/html/2607.25884v1#S5 — V Threats to Validity。

**Artifact boundary。** Exact v1 links https://github.com/dakaidan/CONQuER-Replication, https://github.com/pytorch/executorch, https://github.com/arXiv/html_feedback/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 动态资源控制提高利用率，但增加测量误差、迁移开销、租户公平和控制稳定性问题。 论文自身的边界信号是：Future work will expand CONQuER across three primary vectors.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`INFER-TENSORRT-LLM`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-25884:end -->

<!-- review:SF-2026-ARXIV-2607-25886:start -->
### RSIBench-Data: Benchmarking Data-Centric Research for Recursive Self-Improvement

<!-- claim:SF-2026-ARXIV-2607-25886:start -->Recursive self-improvement requires turning evidence of model failures into better models. Data-centric post-training research entails diagnosing capability gaps, designing and validating training-data strategies, and learning from checkpoint feedback. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-25886:end -->

**为什么进入候选分母。** 摘要首要问题为“Recursive self-improvement requires turning evidence of model failures into better models.”；它改变 observable、对照组、判定粒度或外推边界，可能修正既有评测结论。

**机制与状态边界。** We introduce RSIBench-Data, a controlled benchmark of LLM agents as data-centric researchers with a fixed post-training stack.

**证据证明什么。** Agents demonstrate core data-centric research capabilities: in 58.33\% of settings, they improve upon the first valid attempt by refining strategies from feedback.

**证据没有证明什么。** Yet agents do not improve consistently from feedback: among searches that continue after reaching their best observed score, 78.26% finish with a lower-scoring final attempt and the rest only recover the same peak. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.25886v1#S1 — 1 Introduction; https://arxiv.org/html/2607.25886v1#S2 — 2 Related Work。Evaluation：https://arxiv.org/html/2607.25886v1#S4.SS3 — 4.3 Benchmarks and evaluation; https://arxiv.org/html/2607.25886v1#S5 — 5 Results and Analysis。Limitations / counterevidence：https://arxiv.org/html/2607.25886v1#S6 — 6 Discussion and Limitations; https://arxiv.org/html/2607.25886v1#S7 — 7 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/evolvent-ai/RSIBench-Data, https://github.com/thinking-machines-lab/tinker, https://github.com/e2b-dev; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：Yet agents do not improve consistently from feedback: among searches that continue after reaching their best observed score, 78.26% finish with a lower-scoring final attempt and the rest only recover the same peak.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`PLATFORM-EVALUATION-SYSTEM`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-25886:end -->

<!-- review:SF-2026-ARXIV-2607-25890:start -->
### Distributing Security Controls Through Harness Engineering

<!-- claim:SF-2026-ARXIV-2607-25890:start -->AI coding agents are being adopted at historic speed, yet security and risk concerns remain the primary barrier to scaling agentic AI across organizations. Existing security controls for coding agents are not systematically distributed to engineering teams, and vendor-native solutions introduce ecosystem dependencies that may not suit every deployment context. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-25890:end -->

**为什么进入候选分母。** 摘要首要问题为“AI coding agents are being adopted at historic speed, yet security and risk concerns remain the primary barrier to scaling agentic AI across organizations.”；它改变执行安全的 trust boundary、guard 或 failure detection。

**机制与状态边界。** Initial characteristics toward a control harness fitness framework are proposed, and a third research question is identified for future investigation.

**证据证明什么。** SHarD achieved an adjusted score of 100\%, matching the best securely configured commercial agent, with no regression across any test category.

**证据没有证明什么。** However, this behavior did not reproduce in subsequent test runs. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.25890v1#S4 — IV Methodology; https://arxiv.org/html/2607.25890v1#S4.SS1 — IV-A Test Design。Evaluation：https://arxiv.org/html/2607.25890v1#S5.SS1 — V-A Preliminary Results; https://arxiv.org/html/2607.25890v1#S7 — VII Evaluation。Limitations / counterevidence：https://arxiv.org/html/2607.25890v1#S2.SS1 — II-A Threat Model; https://arxiv.org/html/2607.25890v1#S8 — VIII Discussion。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 新的安全控制点降低特定失败，但会引入误拒绝、旁路、观测不足或模型/任务迁移问题。 论文自身的边界信号是：However, this behavior did not reproduce in subsequent test runs.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`PLATFORM-SECURITY`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-25890:end -->

<!-- review:SF-2026-ARXIV-2607-25891:start -->
### Messier: A High-Resolution Corpus for Cross-Benchmark Agent Evaluation

<!-- claim:SF-2026-ARXIV-2607-25891:start -->Comprehensively evaluating AI agents across interactive environments is difficult due to fragmented tasks, scaffolds, verifiers, and scoring rules. Unfortunately, existing efforts to unify these evaluations are limited in scale and domain, making costly reruns necessary and leaving available data incomparable. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-25891:end -->

**为什么进入候选分母。** 摘要首要问题为“Comprehensively evaluating AI agents across interactive environments is difficult due to fragmented tasks, scaffolds, verifiers, and scoring rules.”；它改变 observable、对照组、判定粒度或外推边界，可能修正既有评测结论。

**机制与状态边界。** We introduce MESSIER, a unified corpus of 957,611 records spanning 30 benchmarks, 745 agents, 11,891 tasks, and 74,263 verifiers.

**证据证明什么。** Counterfactual rescoring further shows that strict all-pass scoring in multi-verifier tasks can alter agent rankings.

**证据没有证明什么。** However, this validation remains an ongoing community effort. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.25891v1#A2 — Appendix B Methodology; https://arxiv.org/html/2607.25891v1#A1.SS4 — A.4 Data model。Evaluation：https://arxiv.org/html/2607.25891v1#A1.SS1 — A.1 Benchmark groups; https://arxiv.org/html/2607.25891v1#S5 — 5 Analysis & applications。Limitations / counterevidence：https://arxiv.org/html/2607.25891v1#S6 — 6 Conclusion; https://arxiv.org/html/2607.25891v1#Sx1 — Limitations。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：However, this validation remains an ongoing community effort.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`PLATFORM-EVALUATION-SYSTEM`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-25891:end -->

<!-- review:SF-2026-ARXIV-2607-25904:start -->
### Interactive Reward Agent: GUI Task Evaluation via Environment-State Verification

<!-- claim:SF-2026-ARXIV-2607-25904:start -->Graphical user interface task evaluation aims to determine whether a GUI agent has successfully completed a user instruction. Automated GUI task evaluation has received increasing attention because the evaluation results can serve as reward signals for both test-time scaling and post-training. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-25904:end -->

**为什么进入候选分母。** 摘要首要问题为“Graphical user interface task evaluation aims to determine whether a GUI agent has successfully completed a user instruction.”；它改变 observable、对照组、判定粒度或外推边界，可能修正既有评测结论。

**机制与状态边界。** In this paper, we propose an interactive reward agent (IRA) based on a propose-then-verify framework to acquire and verify evidence from the post-execution environment.

**证据证明什么。** Experiments show that IRA achieves 86.9% accuracy on GUI-RewardBench, outperforming existing evaluator baselines.

**证据没有证明什么。** This allows IRA to inspect evidence that passive evaluators cannot observe. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.25904v1#A1.SS2 — A.2 System Prompt Structure; https://arxiv.org/html/2607.25904v1#Sx3.SSx2 — Propose-then-Verify Framework。Evaluation：https://arxiv.org/html/2607.25904v1#A1.SS5 — A.5 Category-wise Evaluation Results; https://arxiv.org/html/2607.25904v1#A1.SS11 — A.11 Interactive Reward Agent Error Case Analysis。Limitations / counterevidence：https://arxiv.org/html/2607.25904v1#Sx6 — Discussion and Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：This allows IRA to inspect evidence that passive evaluators cannot observe.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`PLATFORM-EVALUATION-SYSTEM`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-25904:end -->

<!-- review:SF-2026-ARXIV-2607-25907:start -->
### Minimizing Targeted Activations: Input-Only Suppression of Evaluation-Awareness Latents in Large Language Models

<!-- claim:SF-2026-ARXIV-2607-25907:start -->Activation steering controls model behavior by editing internal activations at inference time. We study its input-side dual: optimizing a fluent prompt so that a chosen internal latent is driven toward zero, with no inference-time model access. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-25907:end -->

**为什么进入候选分母。** 摘要首要问题为“Activation steering controls model behavior by editing internal activations at inference time.”；它改变执行安全的 trust boundary、guard 或 failure detection。

**机制与状态边界。** We study its input-side dual: optimizing a fluent prompt so that a chosen internal latent is driven toward zero, with no inference-time model access.

**证据证明什么。** But our controls tell a cautionary story about the CAA direction: a placebo random direction is suppressed just as hard and shifts behavior just as far, and when we hold a real eval passage in context and optimize only a prefix, suppressing the eval-direction fails to reduce-and slightly increases-the model's behavioral eval judgment.

**证据没有证明什么。** Future work should validate on real SAD ( Laine et al., 2024 ) prompts and pursue the in-context threat model. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.25907v1#S3 — 3 Method; https://arxiv.org/html/2607.25907v1#S5.SS3 — 5.3 Input-side vs. model-side: activation is not behavior。Evaluation：https://arxiv.org/html/2607.25907v1#S3.SS3 — 3.3 Evaluation protocol; https://arxiv.org/html/2607.25907v1#S4 — 4 Experimental Setup。Limitations / counterevidence：https://arxiv.org/html/2607.25907v1#S6 — 6 Discussion and Conclusion; https://arxiv.org/html/2607.25907v1#Sx1 — Limitations。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 新的安全控制点降低特定失败，但会引入误拒绝、旁路、观测不足或模型/任务迁移问题。 论文自身的边界信号是：Future work should validate on real SAD ( Laine et al., 2024 ) prompts and pursue the in-context threat model.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`PLATFORM-SECURITY`；evidence-stage relation：`corrective_evidence`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-25907:end -->

<!-- review:SF-2026-ARXIV-2607-25912:start -->
### SAM3D-Guided Object-Centric Representation Alignment for Vision-Language-Action Models

<!-- claim:SF-2026-ARXIV-2607-25912:start -->Vision-Language-Action (VLA) models have shown strong potential for general robot manipulation, but most existing models rely on 2D visual-language backbones and lack fine-grained 3D understanding of target objects, especially under occlusion, pose variation, scale changes, and precise spatial interaction. We propose an object-centric 3D representation alignment framework built upon $π_0$, using SAM3D as a frozen 3D teacher to provide target-object 3D priors during training. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-25912:end -->

**为什么进入候选分母。** 摘要首要问题为“Vision-Language-Action (VLA) models have shown strong potential for general robot manipulation, but most existing models rely on 2D visual-language backbones and lack fine-grained 3D understanding of target objects, especially under occlusion, pose variation, scale changes, and precise spatial interaction.”；它提出可跨 workload 讨论的表示、状态或计算机制，并暴露旧方案边界。

**机制与状态边界。** We propose an object-centric 3D representation alignment framework built upon $π_0$, using SAM3D as a frozen 3D teacher to provide target-object 3D priors during training.

**证据证明什么。** Simulation experiments show consistent improvements, achieving 99.1\% on LIBERO and an average length of 4.11 on CALVIN.

**证据没有证明什么。** The training pipeline depends on automatically generated subtask annotations and object masks, so errors in decomposition, grounding, or segmentation may introduce noisy supervision. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.25912v1#S3 — 3 Method; https://arxiv.org/html/2607.25912v1#S3.SS1 — 3.1 SAM3D-guided VLA Training Framework。Evaluation：https://arxiv.org/html/2607.25912v1#S4 — 4 Experiments。Limitations / counterevidence：https://arxiv.org/html/2607.25912v1#S5 — 5 Conclusion; https://arxiv.org/html/2607.25912v1#S6 — 6 Limitations。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 新表示或状态机制扩大能力边界，但带来额外训练、状态管理、稳定性或泛化假设。 论文自身的边界信号是：The training pipeline depends on automatically generated subtask annotations and object masks, so errors in decomposition, grounding, or segmentation may introduce noisy supervision.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`MULTIMODAL-EMBODIED-VLA`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-25912:end -->

<!-- review:SF-2026-ARXIV-2607-25914:start -->
### Toward Standardized Cross-Vendor Agent Tool Trust Management in Autonomous Networks

<!-- claim:SF-2026-ARXIV-2607-25914:start -->Autonomous Network Levels 4-5 require AI agents to invoke tools across vendor boundaries without human oversight, yet existing management standards lack a standardized mechanism for cross-vendor trust visibility. When a tool from Vendor B is compromised, agents from Vendor A continue invoking it -- unaware of the trust degradation -- causing cascading service impact. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-25914:end -->

**为什么进入候选分母。** 摘要首要问题为“Autonomous Network Levels 4-5 require AI agents to invoke tools across vendor boundaries without human oversight, yet existing management standards lack a standardized mechanism for cross-vendor trust visibility.”；它改变执行安全的 trust boundary、guard 或 failure detection。

**机制与状态边界。** We present AgentToolMO, a proposed 3GPP NRM information model for agent tool trust management.

**证据证明什么。** Simulation-based evaluation across multi-vendor topologies shows that standardized cross-vendor notifications reduce blast radius from hours-scale undetected propagation to near-real-time containment bounded by MnS notification delivery, with cascade convergence guaranteed in bounded iterations and sub-linear notification scaling across vendor domains.

**证据没有证明什么。** Tamper-resistant logging and third-party auditor verification are directions for future work. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.25914v1#S2.SS1 — II-A Trust Management in Multi-Agent Systems; https://arxiv.org/html/2607.25914v1#S2.SS2 — II-B 3GPP Management Framework and Information Models。Evaluation：https://arxiv.org/html/2607.25914v1#S5 — V Formal Analysis; https://arxiv.org/html/2607.25914v1#S6 — VI Evaluation。Limitations / counterevidence：https://arxiv.org/html/2607.25914v1#S7 — VII Discussion; https://arxiv.org/html/2607.25914v1#S7.SS4 — VII-D Limitations。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 新的安全控制点降低特定失败，但会引入误拒绝、旁路、观测不足或模型/任务迁移问题。 论文自身的边界信号是：Tamper-resistant logging and third-party auditor verification are directions for future work.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`AGENT-TOOL-CALLING`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-25914:end -->

<!-- review:SF-2026-ARXIV-2607-25915:start -->
### Penelope: Localized Latent Recurrence for Efficient Structured Reasoning

<!-- claim:SF-2026-ARXIV-2607-25915:start -->Complex structured reasoning tasks often require additional computation, yet current language models obtain it mainly by increasing parameter scale or by serializing intermediate steps as chain-of-thought (CoT) tokens. The former raises training and deployment costs, while the latter ties reasoning computation to autoregressive output length. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-25915:end -->

**为什么进入候选分母。** 摘要首要问题为“Complex structured reasoning tasks often require additional computation, yet current language models obtain it mainly by increasing parameter scale or by serializing intermediate steps as chain-of-thought (CoT) tokens.”；它提出可跨 workload 讨论的表示、状态或计算机制，并暴露旧方案边界。

**机制与状态边界。** We introduce Penelope, an efficient latent-reasoning framework for pretrained decoder-only Transformers that localizes recurrent computation to a selected decoder interval.

**证据证明什么。** These results show that latent refinement can be localized to a narrow decoder interval, reducing repeated full-decoder execution without generating a long visible reasoning trace and providing a practical accuracy-efficiency tradeoff for decoder-only Transformer models.

**证据没有证明什么。** On Deep ListOps, validation-selected recurrence provides a small, consistent gain over the strong inference-only boundary rather than monotonic improvement with depth. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.25915v1#S3 — 3 Method; https://arxiv.org/html/2607.25915v1#S3.SS5 — 3.5 Implementation Details。Evaluation：https://arxiv.org/html/2607.25915v1#S4 — 4 Experiments; https://arxiv.org/html/2607.25915v1#S4.SS1 — 4.1 Experimental Setup。Limitations / counterevidence：https://arxiv.org/html/2607.25915v1#S5 — 5 Discussion and Future Work; https://arxiv.org/html/2607.25915v1#S6 — 6 Conclusion。

**Artifact boundary。** Exact v1 links https://huggingface.co/Qwen/Qwen3.5-0.8B-Base, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 新表示或状态机制扩大能力边界，但带来额外训练、状态管理、稳定性或泛化假设。 论文自身的边界信号是：On Deep ListOps, validation-selected recurrence provides a small, consistent gain over the strong inference-only boundary rather than monotonic improvement with depth.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`MODEL-TRANSFORMER-LAYER`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-25915:end -->

<!-- review:SF-2026-ARXIV-2607-25918:start -->
### DC-WAM: Dynamic-Centric Visual Supervision and Reasoning for World-Action Models

<!-- claim:SF-2026-ARXIV-2607-25918:start -->World-Action Models (WAMs) augment robot policies with future visual prediction, but it remains unclear what the visual modality should learn for control. While photorealistic future prediction provides dense supervision, it also incurs substantial computation and can allocate capacity to texture, illumination, and background variations that are only weakly related to action selection. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-25918:end -->

**为什么进入候选分母。** 摘要首要问题为“World-Action Models (WAMs) augment robot policies with future visual prediction, but it remains unclear what the visual modality should learn for control.”；它提出可跨 workload 讨论的表示、状态或计算机制，并暴露旧方案边界。

**机制与状态边界。** We propose DC-WAM, a dynamic-centric WAM framework that redistributes supervision and computation in the RGB video branch.

**证据证明什么。** Experiments in simulation and on real-world manipulation tasks show that DC-WAM consistently improves policy performance, especially under out-of-distribution perturbations in lighting, object appearance, and background texture.

**证据没有证明什么。** Future work will extend DC-WAM to larger datasets, diverse robot platforms, and WAM architectures beyond MoT. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.25918v1#Sx3 — Method; https://arxiv.org/html/2607.25918v1#Sx2.SSx1 — World-Action Models and Efficient Visual Foresight。Evaluation：https://arxiv.org/html/2607.25918v1#Sx4 — Experiments; https://arxiv.org/html/2607.25918v1#Sx4.SSx1 — Experimental Setup。Limitations / counterevidence：https://arxiv.org/html/2607.25918v1#Sx5 — Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 新表示或状态机制扩大能力边界，但带来额外训练、状态管理、稳定性或泛化假设。 论文自身的边界信号是：Future work will extend DC-WAM to larger datasets, diverse robot platforms, and WAM architectures beyond MoT.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`MULTIMODAL-WORLD-MODELS`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-25918:end -->

<!-- review:SF-2026-ARXIV-2607-25936:start -->
### From Role Prompt to Infinite Thinking: Exploiting Persona Conditioning for Inference Cost Attacks in LLMs

<!-- claim:SF-2026-ARXIV-2607-25936:start -->LLMs are increasingly deployed in real-world applications, making inference efficiency and service reliability critical concerns due to their substantial computational costs. However, the autoregressive generation mechanism of LLMs enables malicious prompts to manipulate generation behaviors, inducing excessive token generation that amplifies computational consumption and threatens service efficiency. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-25936:end -->

**为什么进入候选分母。** 摘要首要问题为“LLMs are increasingly deployed in real-world applications, making inference efficiency and service reliability critical concerns due to their substantial computational costs.”；它改变资源计量、分配、路由或迁移的控制权与约束。

**机制与状态边界。** Based on this observation, we propose RolePlay, a task-aware dynamic persona alignment framework that constructs adaptive personas to naturally induce inefficient yet semantically coherent behaviors for inference cost amplification.

**证据证明什么。** Extensive experiments across multiple LLMs and diverse task datasets demonstrate that RolePlay consistently outperforms existing inference extension methods, achieving an average token amplification of up to \bm{$7.64\times$} and a maximum token amplification ratio of \bm{$207.64\times$}.

**证据没有证明什么。** The threat model is defined across two main dimensions: the adversary’s objectives and their capabilities. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.25936v1#S3 — 3 Method; https://arxiv.org/html/2607.25936v1#S3.SS1 — 3.1 Threat Model。Evaluation：https://arxiv.org/html/2607.25936v1#S4.SS2 — 4.2 Experiment Result; https://arxiv.org/html/2607.25936v1#A1 — Appendix A Appendix A: Experimental Settings。Limitations / counterevidence：https://arxiv.org/html/2607.25936v1#S3.SS1 — 3.1 Threat Model; https://arxiv.org/html/2607.25936v1#S5 — 5 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/meta-llama/llama3/blob/main/MODEL_CARD.md, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 动态资源控制提高利用率，但增加测量误差、迁移开销、租户公平和控制稳定性问题。 论文自身的边界信号是：The threat model is defined across two main dimensions: the adversary’s objectives and their capabilities.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`PLATFORM-SECURITY`；evidence-stage relation：`corrective_evidence`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-25936:end -->

<!-- review:SF-2026-ARXIV-2607-25948:start -->
### MODUS: Decoder-Only Any-to-Any Modeling of Diverse Modalities

<!-- claim:SF-2026-ARXIV-2607-25948:start -->Any-to-any models predict any modality from any combination of others within a single network, a formulation used in multimodal vision and vision-language models, and increasingly in scientific domains such as ecology and astronomy. Existing any-to-any models are typically trained from scratch using encoder-decoder or diffusion architectures, impacting their performance and preventing them from using strong pre-trained decoder-only models as a prior. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-25948:end -->

**为什么进入候选分母。** 摘要首要问题为“Any-to-any models predict any modality from any combination of others within a single network, a formulation used in multimodal vision and vision-language models, and increasingly in scientific domains such as ecology and astronomy.”；它提出可跨 workload 讨论的表示、状态或计算机制，并暴露旧方案边界。

**机制与状态边界。** Existing any-to-any models are typically trained from scratch using encoder-decoder or diffusion architectures, impacting their performance and preventing them from using strong pre-trained decoder-only models as a prior.

**证据证明什么。** Modus demonstrates strong out-of-the-box performance and is competitive with specialist and multitask baselines using a single model across various benchmarks.

**证据没有证明什么。** 5 Conclusion We presented Modus , a unified decoder-only model for any-to-any multimodal generation. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.25948v1#S3 — 3 Method; https://arxiv.org/html/2607.25948v1#S3.SS2 — 3.2 Any-to-Any Decoder-Only Architecture。Evaluation：https://arxiv.org/html/2607.25948v1#A2 — Appendix B Additional Ablations; https://arxiv.org/html/2607.25948v1#A3 — Appendix C More Evaluations。Limitations / counterevidence：https://arxiv.org/html/2607.25948v1#A6 — Appendix F Limitation Discussion; https://arxiv.org/html/2607.25948v1#S5 — 5 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 新表示或状态机制扩大能力边界，但带来额外训练、状态管理、稳定性或泛化假设。 论文自身的边界信号是：5 Conclusion We presented Modus , a unified decoder-only model for any-to-any multimodal generation.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`MULTIMODAL-GENERATIVE-PARADIGMS`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-25948:end -->

<!-- review:SF-2026-ARXIV-2607-25970:start -->
### Reinforcement Learning for Code Optimization

<!-- claim:SF-2026-ARXIV-2607-25970:start -->RL for code correctness is now established: have the model generate a program, run it against hidden test cases, and reward solutions that pass. Extending this to code optimization seems straightforward: just add execution time to the reward. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-25970:end -->

**为什么进入候选分母。** 摘要首要问题为“RL for code correctness is now established: have the model generate a program, run it against hidden test cases, and reward solutions that pass.”；它改变训练信号、capacity 或 update ownership，而非只报告任务精度。

**机制与状态边界。** Extending this to code optimization seems straightforward: just add execution time to the reward.

**证据证明什么。** Relative to the fastest correct human submissions per problem, it reaches about half the human rate of complexity-class improvements (14% vs.

**证据没有证明什么。** Exact v1 does not disclose a dedicated generalization or deployment guarantee beyond its stated evaluation scope. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.25970v1#A3.SS6 — C.6 Alternative fallback designs; https://arxiv.org/html/2607.25970v1#A4 — Appendix D Designing Environments and Rewards for Optimization RL。Evaluation：https://arxiv.org/html/2607.25970v1#A2.SS9 — B.9 Training ablations: does DMC-Optim help, and is it enough to solve optimization RL?; https://arxiv.org/html/2607.25970v1#A3.SS10 — C.10 Joint training-time and evaluation-time calibration sweeps。Limitations / counterevidence：https://arxiv.org/html/2607.25970v1#A2.SS2 — B.2 Source data, limitations, and decontamination; https://arxiv.org/html/2607.25970v1#A3.SS4 — C.4 Fallback after remote execution failures。

**Artifact boundary。** Exact v1 links https://github.com/containers/bubblewrap, https://github.com/facebookresearch/BigOBench/tree/main/src/complexity/sandbox, https://huggingface.co/Qwen/Qwen2.5-72B/blob/main/LICENSE; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更密集或更定向的训练信号改善样本效率，但会增加 verifier 偏差、分布迁移和优化耦合。 论文自身的边界信号是：Exact v1 does not disclose a dedicated generalization or deployment guarantee beyond its stated evaluation scope.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`TRAIN-GRPO`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-25970:end -->

<!-- review:SF-2026-ARXIV-2607-25987:start -->
### IH-Benchmark: A Conflict-Centered Benchmark for Instruction-Hierarchy Robustness in LLM Applications

<!-- claim:SF-2026-ARXIV-2607-25987:start -->When a language model receives conflicting instructions from different priority levels, which one does it actually follow? This question lies at the heart of reliable LLM deployment. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-25987:end -->

**为什么进入候选分母。** 摘要首要问题为“When a language model receives conflicting instructions from different priority levels, which one does it actually follow?”；它改变 observable、对照组、判定粒度或外推边界，可能修正既有评测结论。

**机制与状态边界。** We present IH-Benchmark, a conflict-centered benchmark for instruction-hierarchy robustness across direct system-user conflicts (S&gt;U) and tool-mediated user-tool (U&gt;T) conflicts.

**证据证明什么。** These results suggest that instruction-hierarchy robustness is not a single capability, but a set of behaviors that must be evaluated across conflict surfaces, constraint types, and attack presentations.

**证据没有证明什么。** In particular, strong S U performance does not reliably predict U T robustness, and failures vary across different factors. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.25987v1#A2.SS1 — B.1 Model Details。Evaluation：https://arxiv.org/html/2607.25987v1#A7 — Appendix G Complete Evaluation Results; https://arxiv.org/html/2607.25987v1#A10 — Appendix J Constraint Group Results。Limitations / counterevidence：https://arxiv.org/html/2607.25987v1#S5 — 5 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：In particular, strong S U performance does not reliably predict U T robustness, and failures vary across different factors.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`PLATFORM-SECURITY`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-25987:end -->

<!-- review:SF-2026-ARXIV-2607-25992:start -->
### MemLens: A Value-Aware Memory Management System with Interactive Analytics for LLM-based Agents

<!-- claim:SF-2026-ARXIV-2607-25992:start -->Recently, memory management has become a key infrastructure for LLM-based agents, as it directly affects long-horizon reasoning, personalized responses, and knowledge reuse. However, existing LLM memory systems typically adopt a coarse-grained (utility-agnostic) manner that treats heterogeneous user-LLM interaction records uniformly, leading to redundant and low-impact records persisting in the memory repository. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-25992:end -->

**为什么进入候选分母。** 摘要首要问题为“Recently, memory management has become a key infrastructure for LLM-based agents, as it directly affects long-horizon reasoning, personalized responses, and knowledge reuse.”；它把 context、memory、能力或进度变成持久且可验证的 agent state。

**机制与状态边界。** To address this challenge, we present MemLens, a value-aware memory management system that takes memory records as first-class data objects.

**证据证明什么。** Therefore, our MemLens can serve as an efficient, interpretable, and personalized long-term memory management system for LLM-based agents.

**证据没有证明什么。** A memory unit that is beneficial for one future query may be irrelevant for another, and its contribution may also depend on which other memory units are already available. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.25992v1#S3 — 3. MemLens System Design。Evaluation：https://arxiv.org/html/2607.25992v1#S3.SS1 — 3.1. Memory Data Evaluation。Limitations / counterevidence：https://arxiv.org/html/2607.25992v1#S1 — 1. Introduction; https://arxiv.org/html/2607.25992v1#S2 — 2. MemLens Overview。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 显式 agent state 改善恢复与控制，但增加状态陈旧、错误提交、跨轮污染和一致性责任。 论文自身的边界信号是：A memory unit that is beneficial for one future query may be irrelevant for another, and its contribution may also depend on which other memory units are already available.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`AGENT-MEMORY`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-25992:end -->

<!-- review:SF-2026-ARXIV-2607-25995:start -->
### Does Runtime Topology Context Improve LLM-Generated Kubernetes Security Patches?

<!-- claim:SF-2026-ARXIV-2607-25995:start -->Kubernetes is central to the cloud-native ecosystem, orchestrating containerised workloads. Recent work suggests that large language models (LLMs) can automate cluster security remediation, generating configuration patches from Kubernetes Security Posture Management (KSPM) findings without human authoring. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-25995:end -->

**为什么进入候选分母。** 摘要首要问题为“Kubernetes is central to the cloud-native ecosystem, orchestrating containerised workloads.”；它改变 observable、对照组、判定粒度或外推边界，可能修正既有评测结论。

**机制与状态边界。** Kubernetes is central to the cloud-native ecosystem, orchestrating containerised workloads.

**证据证明什么。** Whether live cluster context improves patch correctness has not been measured under controlled conditions across multiple dependency classes.

**证据没有证明什么。** These are not malformed patches but plausible, scanner-compliant fixes with a destructive functional blast radius , failing only because the runtime dependency is invisible to the model. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.25995v1#S3 — 3 System Architecture; https://arxiv.org/html/2607.25995v1#S2.SS2 — 2.2 Attack Graph Construction for Cloud-Native Systems。Evaluation：https://arxiv.org/html/2607.25995v1#S4 — 4 The VulnCare Benchmark; https://arxiv.org/html/2607.25995v1#S5 — 5 Graph-Based Attack Path Analysis。Limitations / counterevidence：https://arxiv.org/html/2607.25995v1#S6.SS5 — 6.5 RQ4: Failure Modes; https://arxiv.org/html/2607.25995v1#S7 — 7 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/dynatrace-research/vulncare, https://github.com/dynatrace-research/kutie-artifacts, https://github.com/madhuakula/kubernetes-goat; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：These are not malformed patches but plausible, scanner-compliant fixes with a destructive functional blast radius , failing only because the runtime dependency is invisible to the model.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`PLATFORM-SECURITY`；evidence-stage relation：`corrective_evidence`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-25995:end -->

<!-- review:SF-2026-ARXIV-2607-25996:start -->
### RepoReasoner: Evaluating Repository-Level Code Reasoning Ability of Long-Context Language Models

<!-- claim:SF-2026-ARXIV-2607-25996:start -->Recent large language models (LLMs) have shown strong performance on software engineering tasks, yet most existing benchmarks evaluate code reasoning at the function level, where all relevant information is localized. This setting fails to reflect real-world development, which requires reasoning across multiple files and complex dependency structures. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-25996:end -->

**为什么进入候选分母。** 摘要首要问题为“Recent large language models (LLMs) have shown strong performance on software engineering tasks, yet most existing benchmarks evaluate code reasoning at the function level, where all relevant information is localized.”；它改变 observable、对照组、判定粒度或外推边界，可能修正既有评测结论。

**机制与状态边界。** We introduce RepoReasoner, a benchmark for evaluating repository-level code reasoning.

**证据证明什么。** Furthermore, performance drops on rewritten data reveal partial reliance on memorization, and longer contexts do not consistently improve results due to noise.

**证据没有证明什么。** Threats to Validity We identify the following key threats to the validity of our study. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.25996v1#S4 — 4. Experimental Design; https://arxiv.org/html/2607.25996v1#S2.SS1 — 2.1. Long Context Language Models。Evaluation：https://arxiv.org/html/2607.25996v1#S2.SS3 — 2.3. Coding Ability Evaluation Benchmarks; https://arxiv.org/html/2607.25996v1#S3.SS1 — 3.1. Benchmark Tasks。Limitations / counterevidence：https://arxiv.org/html/2607.25996v1#S6 — 6. Threats to Validity; https://arxiv.org/html/2607.25996v1#S7 — 7. Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/DeepSoftwareAnalytics/RepoReasoner, https://github.com/ionelmc/python-hunter, https://github.com/arXiv/html_feedback/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：Threats to Validity We identify the following key threats to the validity of our study.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`PLATFORM-EVALUATION-SYSTEM`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-25996:end -->

<!-- review:SF-2026-ARXIV-2607-26004:start -->
### Parallel Decoding Distillation for Fast Image and Video Generation

<!-- claim:SF-2026-ARXIV-2607-26004:start -->Generation in video diffusion or flow models is computationally expensive due to the slow and iterative sampling process. Current state-of-the-art (SOTA) acceleration methods heavily rely on variational score distillation (VSD) and adversarial losses to distill diffusion models into few-step generators. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-26004:end -->

**为什么进入候选分母。** 摘要首要问题为“Generation in video diffusion or flow models is computationally expensive due to the slow and iterative sampling process.”；它改变推理期状态放置、数据移动、执行控制或实时 SLO。

**机制与状态边界。** In this paper, we introduce Parallel Decoding Distillation (PDD), a simplified and scalable trajectory-based distillation method for fast inference of diffusion and flow matching models.

**证据证明什么。** Moreover, PDD presents a significant improvement in generated video diversity.

**证据没有证明什么。** Because our large-scale text-to-image and video experiments rely on data-free training, investigating PDD in data-dependent settings beyond ImageNet-256 remains future work. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.26004v1#A1 — Appendix A Algorithms; https://arxiv.org/html/2607.26004v1#S2 — 2 Generative Flow Models。Evaluation：https://arxiv.org/html/2607.26004v1#A2 — Appendix B Experiments; https://arxiv.org/html/2607.26004v1#S5 — 5 Experiments。Limitations / counterevidence：https://arxiv.org/html/2607.26004v1#S6 — 6 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/ModelTC/lightx2v, https://github.com/NVlabs/FastGen, https://github.com/arXiv/html_feedback/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更激进的缓存、迁移、并行或专用执行会换取吞吐/时延，同时增加配置依赖、资源压力与回退路径。 论文自身的边界信号是：Because our large-scale text-to-image and video experiments rely on data-free training, investigating PDD in data-dependent settings beyond ImageNet-256 remains future work.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`MULTIMODAL-GENERATIVE-PARADIGMS`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-26004:end -->

<!-- review:SF-2026-ARXIV-2607-26016:start -->
### MDTransformer: A Hardware-Software Co-Design of Mode-Division Photonic Transformer Accelerator with Inverse-Designed Coherent Crossbar

<!-- claim:SF-2026-ARXIV-2607-26016:start -->Recently, photonic transformer accelerators (PTAs) have successfully achieved significant speedup and energy efficiency improvements over electronic accelerators for expediting Transformer inference. However, state-of-the-art rely on expensive multi-wavelength light generation and large dot-product units due to active phase-shifter components, thus making their approach inefficient and impractical. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-26016:end -->

**为什么进入候选分母。** 摘要首要问题为“Recently, photonic transformer accelerators (PTAs) have successfully achieved significant speedup and energy efficiency improvements over electronic accelerators for expediting Transformer inference.”；它改变资源计量、分配、路由或迁移的控制权与约束。

**机制与状态边界。** These results show that MDTransformer offers a practical solution for high-performance and energy-efficient transformer-based systems.

**证据证明什么。** Experimental results show that MDTransformer achieves 40.4% area reduction, 63.6% power saving, 40.6% energy saving, and comparable latency over the state-of-the-art PTA across different workloads (i.e., DeiT-Tiny/Small/Base and BERT-Base/Large).

**证据没有证明什么。** To show the limitations of state-of-the-art and related research challenges, we conduct a case study in Section I-B . 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.26016v1#S3.SS4 — III-D Architecture System Design; https://arxiv.org/html/2607.26016v1#S2.SS2 — II-B Inverse Design in Photonic Circuits。Evaluation：https://arxiv.org/html/2607.26016v1#S4 — IV Evaluation Methodology; https://arxiv.org/html/2607.26016v1#S5 — V Results and Discussion。Limitations / counterevidence：https://arxiv.org/html/2607.26016v1#S1.SS1 — I-A State-of-the-Art PTAs and Their Limitations; https://arxiv.org/html/2607.26016v1#S5 — V Results and Discussion。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 动态资源控制提高利用率，但增加测量误差、迁移开销、租户公平和控制稳定性问题。 论文自身的边界信号是：To show the limitations of state-of-the-art and related research challenges, we conduct a case study in Section I-B .

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`INFER-TENSORRT-LLM`；evidence-stage relation：`alternative_branch`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-26016:end -->

<!-- review:SF-2026-ARXIV-2607-26017:start -->
### UniMem: Complementary Episodic-to-Parametric Memory for Boundary-Agnostic Task Streams

<!-- claim:SF-2026-ARXIV-2607-26017:start -->Memory is essential for LLM agents to accumulate task experience and reuse task-specific execution strategies. However, real-world deployment over boundary-agnostic and evolving task streams exposes a fundamental stability-plasticity dilemma. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-26017:end -->

**为什么进入候选分母。** 摘要首要问题为“Memory is essential for LLM agents to accumulate task experience and reuse task-specific execution strategies.”；它把 context、memory、能力或进度变成持久且可验证的 agent state。

**机制与状态边界。** Inspired by the human brain, which balances plasticity and stability through complementary episodic storage and gradual consolidation, we propose UniMem, a self-routing framework for autonomous memory management.

**证据证明什么。** Experiments on long-horizon streaming task sequences show that UniMem consistently outperforms baselines while maintaining execution fidelity, achieving an average gain of 4.0 EM points across three backbone models.

**证据没有证明什么。** Limitations Although UniMem shows promising results for self-routing memory expansion under streaming tasks, two directions remain open. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.26017v1#S3 — 3 Methodology; https://arxiv.org/html/2607.26017v1#S3.SS2 — 3.2 Self-Routing Memory Architecture。Evaluation：https://arxiv.org/html/2607.26017v1#S4.SS2 — 4.2 Main Results and Analysis; https://arxiv.org/html/2607.26017v1#S4.SS3 — 4.3 Ablation and Qualitative Analysis。Limitations / counterevidence：https://arxiv.org/html/2607.26017v1#S5 — 5 Conclusion; https://arxiv.org/html/2607.26017v1#Sx1 — Limitations。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 显式 agent state 改善恢复与控制，但增加状态陈旧、错误提交、跨轮污染和一致性责任。 论文自身的边界信号是：Limitations Although UniMem shows promising results for self-routing memory expansion under streaming tasks, two directions remain open.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`AGENT-MEMORY`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-26017:end -->

<!-- review:SF-2026-ARXIV-2607-26037:start -->
### Wonder: Video World Model Done Better

<!-- claim:SF-2026-ARXIV-2607-26037:start -->We present Wonder, a general-purpose video world model for real-time, camera-controllable world exploration. Given an image or a conditional video, Wonder constructs a playable world where users can navigate interactively by moving the camera, discovering unseen regions, and revisiting previously observed areas in real time and over a long-term horizon. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-26037:end -->

**为什么进入候选分母。** 摘要首要问题为“We present Wonder, a general-purpose video world model for real-time, camera-controllable world exploration.”；它提出可跨 workload 讨论的表示、状态或计算机制，并暴露旧方案边界。

**机制与状态边界。** Achieving this capability requires a system-level co-design of control method, memory mechanism, and training strategy.

**证据证明什么。** Beyond image-to-video generation, Wonder naturally supports video-conditioned generation, allowing existing dynamic scenes to be re-shot in real time.

**证据没有证明什么。** Exact v1 does not disclose a dedicated generalization or deployment guarantee beyond its stated evaluation scope. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.26037v1#S4 — 4 Wonder World Model; https://arxiv.org/html/2607.26037v1#S4.SS4 — 4.4 Training Infrastructure and Model Details。Evaluation：https://arxiv.org/html/2607.26037v1#S5 — 5 Experiments。Limitations / counterevidence：https://arxiv.org/html/2607.26037v1#S6 — 6 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 新表示或状态机制扩大能力边界，但带来额外训练、状态管理、稳定性或泛化假设。 论文自身的边界信号是：Exact v1 does not disclose a dedicated generalization or deployment guarantee beyond its stated evaluation scope.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`MULTIMODAL-WORLD-MODELS`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-26037:end -->

<!-- review:SF-2026-ARXIV-2607-26040:start -->
### Reinformed Dreamer: An Asymmetric World Model Efficiently Trained through Latent Guidance

<!-- claim:SF-2026-ARXIV-2607-26040:start -->Much like humans benefit from guidance while learning, reinforcement learning algorithms may benefit from additional supervision beyond rewards. Leveraging additional information during training to learn better representations and behaviors has been the focus of asymmetric reinforcement learning. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-26040:end -->

**为什么进入候选分母。** 摘要首要问题为“Much like humans benefit from guidance while learning, reinforcement learning algorithms may benefit from additional supervision beyond rewards.”；它改变训练信号、capacity 或 update ownership，而非只报告任务精度。

**机制与状态边界。** Then, we propose a novel asymmetric representation learning objective using latent guidance, resulting in a new algorithm called the Reinformed Dreamer.

**证据证明什么。** Experiments across several benchmarks show a more consistent improvement over Dreamer than previous asymmetric approaches.

**证据没有证明什么。** Under partial observability, the optimal decision generally depends on the entire history of observations and past actions. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/pdf/2607.26040v1#page=1 — PDF page 1; https://arxiv.org/pdf/2607.26040v1#page=10 — PDF page 10。Evaluation：https://arxiv.org/pdf/2607.26040v1#page=1 — PDF page 1; https://arxiv.org/pdf/2607.26040v1#page=10 — PDF page 10。Limitations / counterevidence：https://arxiv.org/pdf/2607.26040v1#page=1 — PDF page 1; https://arxiv.org/pdf/2607.26040v1#page=10 — PDF page 10。

**Artifact boundary。** Not Disclosed — exact v1 exposes no uniquely versioned artifact locator used to enlarge the manuscript claim boundary.

**Trade-off 与共存边界。** 更密集或更定向的训练信号改善样本效率，但会增加 verifier 偏差、分布迁移和优化耦合。 论文自身的边界信号是：Under partial observability, the optimal decision generally depends on the entire history of observations and past actions.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`MULTIMODAL-WORLD-MODELS`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-26040:end -->

<!-- review:SF-2026-ARXIV-2607-26041:start -->
### Desktop-Delta Bench: Do Computer-Use Models Understand Desktop GUI Transitions?

<!-- claim:SF-2026-ARXIV-2607-26041:start -->Computer-use agents (CUAs) increasingly act through desktop GUIs to complete long-horizon tasks. Current benchmarks primarily measure end-task success or single-frame grounding. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-26041:end -->

**为什么进入候选分母。** 摘要首要问题为“Computer-use agents (CUAs) increasingly act through desktop GUIs to complete long-horizon tasks.”；它改变 observable、对照组、判定粒度或外推边界，可能修正既有评测结论。

**机制与状态边界。** Task context improves decoy identification by 6.9 percentage points but reduces non-decoy exact match by 2.2 points; error analysis reveals systematic copying of the presented A-B-C order.

**证据证明什么。** Single-action results show that inferring the action family is harder than locating it: click F1 is 0.96 vs, 0.76 for drag, while recognized drags are generally localized well.

**证据没有证明什么。** For each model, a cell is the mean over 2 reasoning; row n counts unique samples, not predictions. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/pdf/2607.26041v1#page=1 — PDF page 1; https://arxiv.org/pdf/2607.26041v1#page=10 — PDF page 10。Evaluation：https://arxiv.org/pdf/2607.26041v1#page=1 — PDF page 1; https://arxiv.org/pdf/2607.26041v1#page=10 — PDF page 10。Limitations / counterevidence：https://arxiv.org/pdf/2607.26041v1#page=1 — PDF page 1; https://arxiv.org/pdf/2607.26041v1#page=10 — PDF page 10。

**Artifact boundary。** Exact v1 links https://github.com/abhipi/DDB, https://huggingface.co/Hcompany/Holo-3.1-35B-A3B, https://huggingface.co/MiniMaxAI/MiniMax-M3; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：For each model, a cell is the mean over 2 reasoning; row n counts unique samples, not predictions.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`PLATFORM-EVALUATION-SYSTEM`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-26041:end -->

<!-- review:SF-2026-ARXIV-2607-26052:start -->
### Spend Experts Where You Are Unsure: Confidence-Adaptive Routing for Mixture-of-Experts LoRA

<!-- claim:SF-2026-ARXIV-2607-26052:start -->Mixture-of-Experts (MoE) variants of Low-Rank Adaptation (LoRA) route every token to a fixed number of experts $k$. Tokens differ in how uncertain the model is about them, so a single k over-spends on easy tokens and under-serves hard ones. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-26052:end -->

**为什么进入候选分母。** 摘要首要问题为“Mixture-of-Experts (MoE) variants of Low-Rank Adaptation (LoRA) route every token to a fixed number of experts $k$.”；它改变资源计量、分配、路由或迁移的控制权与约束。

**机制与状态边界。** We introduce CARE (Confidence-Adaptive Routing of Experts), which admits experts in a nucleus fashion.

**证据证明什么。** The same confidence and disagreement signals also improve out-of-distribution detection over MSP, entropy, and multi-pass proxies.

**证据没有证明什么。** CARE is a way to spend a given compute budget better, not a way to add capacity. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.26052v1#S4 — 4 Method: CARE。Evaluation：https://arxiv.org/html/2607.26052v1#A2 — Appendix B Detailed Experimental Setup; https://arxiv.org/html/2607.26052v1#A3 — Appendix C Additional Experiments。Limitations / counterevidence：https://arxiv.org/html/2607.26052v1#A4 — Appendix D Extended Discussion; https://arxiv.org/html/2607.26052v1#S7 — 7 Discussion。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 动态资源控制提高利用率，但增加测量误差、迁移开销、租户公平和控制稳定性问题。 论文自身的边界信号是：CARE is a way to spend a given compute budget better, not a way to add capacity.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`MODEL-MOE`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-26052:end -->

<!-- review:SF-2026-ARXIV-2607-26055:start -->
### $π\mathbf{R}^2$: Reactive Real-time Flow Policies

<!-- claim:SF-2026-ARXIV-2607-26055:start -->Generalist manipulation policies increasingly take the form of action-chunking flow policies built on large pretrained backbones. Such chunks run open-loop, so the policy cannot react to sensory input arriving mid-execution, sacrificing \emph{reactivity}. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-26055:end -->

**为什么进入候选分母。** 摘要首要问题为“Generalist manipulation policies increasingly take the form of action-chunking flow policies built on large pretrained backbones.”；它改变推理期状态放置、数据移动、执行控制或实时 SLO。

**机制与状态边界。** We present $π\mathbf{R}^2$, which makes these policies reactive and real-time while retaining large backbones, expressive multi-modal policies, and multi-action prediction.

**证据证明什么。** Across simulation and real-world manipulation tasks, $π\mathbf{R}^2$ improves the success rate by up to $23\%$ in simulation and $30\%$ in the real world over the strongest baseline.

**证据没有证明什么。** First, we do not address sources of latency external to the model itself, such as communication delays between the inference server and the robot client. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.26055v1#A1 — Appendix A Implementation Details; https://arxiv.org/html/2607.26055v1#A1.SS3 — A.3 Training and Inference Algorithms。Evaluation：https://arxiv.org/html/2607.26055v1#A1.SS4 — A.4 Additional Reactivity Analysis; https://arxiv.org/html/2607.26055v1#S4 — 4 Experiments。Limitations / counterevidence：https://arxiv.org/html/2607.26055v1#S5 — 5 Discussion; https://arxiv.org/html/2607.26055v1#Sx1 — Limitations。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更激进的缓存、迁移、并行或专用执行会换取吞吐/时延，同时增加配置依赖、资源压力与回退路径。 论文自身的边界信号是：First, we do not address sources of latency external to the model itself, such as communication delays between the inference server and the robot client.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`MULTIMODAL-EMBODIED-VLA`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-26055:end -->

<!-- review:SF-2026-ARXIV-2607-26056:start -->
### INTACT: Isomorphic Intent-to-Action Learning for Search-Free World Models

<!-- claim:SF-2026-ARXIV-2607-26056:start -->Forward latent world models predict how actions change a scene, but recover actions for a desired change only through expensive test-time search. We introduce INTACT (INtent-To-ACTion), an end-to-end JEPA that turns action-labeled, reward-free trajectories into a deployable intent-to-action interface. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-26056:end -->

**为什么进入候选分母。** 摘要首要问题为“Forward latent world models predict how actions change a scene, but recover actions for a desired change only through expensive test-time search.”；它把 context、memory、能力或进度变成持久且可验证的 agent state。

**机制与状态边界。** We introduce INTACT (INtent-To-ACTion), an end-to-end JEPA that turns action-labeled, reward-free trajectories into a deployable intent-to-action interface.

**证据证明什么。** One shared four-task encoder reaches 89.39\% E5 Direct macro and improves every task over jointly trained LeWM, while predicted--expert action-family kNN tracks Direct success at $r=0.954$.

**证据没有证明什么。** A coordinate gauge can restore a learned map but cannot invent a deployment conditional absent from the actor. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.26056v1#A3 — Appendix C Extended Method Derivations and Control Pseudocode; https://arxiv.org/html/2607.26056v1#A4 — Appendix D Design Selection and Ablation Logic。Evaluation：https://arxiv.org/html/2607.26056v1#A12 — Appendix L Evaluation Protocol Scope; https://arxiv.org/html/2607.26056v1#A2 — Appendix B Implementation and Evaluation Identities。Limitations / counterevidence：https://arxiv.org/html/2607.26056v1#S6 — 6 Limitations; https://arxiv.org/html/2607.26056v1#S7 — 7 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/DavidSunok/CLEAR-LeWM/releases/tag/v0.5.1, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 显式 agent state 改善恢复与控制，但增加状态陈旧、错误提交、跨轮污染和一致性责任。 论文自身的边界信号是：A coordinate gauge can restore a learned map but cannot invent a deployment conditional absent from the actor.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`MULTIMODAL-WORLD-MODELS`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-26056:end -->

## 4. Benchmark Contracts

None。数值只在各 Source Review 的 exact-v1 evaluation contract 内使用，不形成跨配置 benchmark claim。

## 5. Deep Analysis Selection

<!-- validator:deep-analysis-selection-v1 -->
| Source Family ID | Eligibility | Decision | Analysis Unit ID | Subsumed By | Priority Rationale | Narrative Ref |
| --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2607-24758 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-24758 |
| SF-2026-ARXIV-2607-24759 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-24759 |
| SF-2026-ARXIV-2607-24762 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-24762 |
| SF-2026-ARXIV-2607-24763 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-24763 |
| SF-2026-ARXIV-2607-24780 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-24780 |
| SF-2026-ARXIV-2607-24787 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-24787 |
| SF-2026-ARXIV-2607-24788 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-24788 |
| SF-2026-ARXIV-2607-24798 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-24798 |
| SF-2026-ARXIV-2607-24866 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-24866 |
| SF-2026-ARXIV-2607-24882 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-24882 |
| SF-2026-ARXIV-2607-24893 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-24893 |
| SF-2026-ARXIV-2607-24953 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-24953 |
| SF-2026-ARXIV-2607-25018 | score_7_9 | selected | DA-20260729-01 | — | V2=9/9；相对其他 eligible family 提供更直接、可迁移且不重复的 state/control/evaluation 机制。 | analysis:DA-20260729-01 |
| SF-2026-ARXIV-2607-25063 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-25063 |
| SF-2026-ARXIV-2607-25076 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-25076 |
| SF-2026-ARXIV-2607-25152 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-25152 |
| SF-2026-ARXIV-2607-25255 | score_7_9 | selected | DA-20260729-02 | — | V2=9/9；相对其他 eligible family 提供更直接、可迁移且不重复的 state/control/evaluation 机制。 | analysis:DA-20260729-02 |
| SF-2026-ARXIV-2607-25291 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-25291 |
| SF-2026-ARXIV-2607-25297 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-25297 |
| SF-2026-ARXIV-2607-25337 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-25337 |
| SF-2026-ARXIV-2607-25364 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-25364 |
| SF-2026-ARXIV-2607-25379 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-25379 |
| SF-2026-ARXIV-2607-25398 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-25398 |
| SF-2026-ARXIV-2607-25400 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-25400 |
| SF-2026-ARXIV-2607-25408 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-25408 |
| SF-2026-ARXIV-2607-25415 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-25415 |
| SF-2026-ARXIV-2607-25431 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-25431 |
| SF-2026-ARXIV-2607-25487 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-25487 |
| SF-2026-ARXIV-2607-25498 | score_7_9 | selected | DA-20260729-03 | — | V2=9/9；相对其他 eligible family 提供更直接、可迁移且不重复的 state/control/evaluation 机制。 | analysis:DA-20260729-03 |
| SF-2026-ARXIV-2607-25504 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-25504 |
| SF-2026-ARXIV-2607-25566 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-25566 |
| SF-2026-ARXIV-2607-25600 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-25600 |
| SF-2026-ARXIV-2607-25619 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-25619 |
| SF-2026-ARXIV-2607-25650 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-25650 |
| SF-2026-ARXIV-2607-25659 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-25659 |
| SF-2026-ARXIV-2607-25816 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-25816 |
| SF-2026-ARXIV-2607-25852 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-25852 |
| SF-2026-ARXIV-2607-25884 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-25884 |
| SF-2026-ARXIV-2607-25886 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-25886 |
| SF-2026-ARXIV-2607-25904 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-25904 |
| SF-2026-ARXIV-2607-25970 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-25970 |
| SF-2026-ARXIV-2607-25992 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-25992 |
| SF-2026-ARXIV-2607-26037 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-26037 |

### Selection Decisions

<!-- analysis-decision:SF-2026-ARXIV-2607-24758:start -->
`SF-2026-ARXIV-2607-24758` 的 exact-v1 Deep Review 已保留。其机制为：The reasons why models fake alignment are not fully understood, however. 为避免挤压 `PLATFORM-SECURITY` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-24758:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-24759:start -->
`SF-2026-ARXIV-2607-24759` 的 exact-v1 Deep Review 已保留。其机制为：We present llm-wiki-memory-template, a reusable, agent-aware instantiation, and argue it is a substrate for heterogeneous collaborative knowledge work along three axes (multi-human, multi-AI-agent, multi-domain) with each axis supported by a distinct architectural element of the template (§4). 为避免挤压 `AGENT-MEMORY` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-24759:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-24762:start -->
`SF-2026-ARXIV-2607-24762` 的 exact-v1 Deep Review 已保留。其机制为：We present Kernel Forge, an open-source, end-to-end agentic harness that accepts any unmodified PyTorch model in place. 为避免挤压 `PLATFORM-EVALUATION-SYSTEM` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-24762:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-24763:start -->
`SF-2026-ARXIV-2607-24763` 的 exact-v1 Deep Review 已保留。其机制为：We present CaRE, a compute-aware evaluation framework that audits MDLM remasking strategies by standardizing actual number of function evaluations (NFE), enforcing multi-metric reporting, and explicitly controlling stochasticity. 为避免挤压 `MULTIMODAL-GENERATIVE-PARADIGMS` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-24763:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-24780:start -->
`SF-2026-ARXIV-2607-24780` 的 exact-v1 Deep Review 已保留。其机制为：To study this question, we introduce \textbf{LivingArena}, an automated peer-probing framework in which models take turns testing one another. 为避免挤压 `PLATFORM-EVALUATION-SYSTEM` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-24780:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-24787:start -->
`SF-2026-ARXIV-2607-24787` 的 exact-v1 Deep Review 已保留。其机制为：To address this bottleneck, we propose SpecPrefetch, a parameter-efficient prefetching framework for offloaded MoE inference. 为避免挤压 `MODEL-MOE` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-24787:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-24788:start -->
`SF-2026-ARXIV-2607-24788` 的 exact-v1 Deep Review 已保留。其机制为：To address this, we propose GLIDE, a Guided Layerwise Hybrid Attention that strategically integrates sliding-window softmax attention with linear recurrent aggregation. 为避免挤压 `INFER-DECODE` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-24788:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-24798:start -->
`SF-2026-ARXIV-2607-24798` 的 exact-v1 Deep Review 已保留。其机制为：After an interaction is observed, many systems treat it as evidence for updating durable user state. 为避免挤压 `AGENT-MEMORY` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-24798:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-24866:start -->
`SF-2026-ARXIV-2607-24866` 的 exact-v1 Deep Review 已保留。其机制为：Interpretability, formal methods, security engineering, evaluation methodology, and reinforcement-learning safety each produce substantial work, but the resulting artifacts do not compose into deployable oversight: every team fielding an agentic system builds its own audit schema, policy dialect, monitoring stack, and escalation path, mostly reinventions of patterns understood elsewhere. 为避免挤压 `PLATFORM-SECURITY` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-24866:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-24882:start -->
`SF-2026-ARXIV-2607-24882` 的 exact-v1 Deep Review 已保留。其机制为：We introduce Agent Retrieval Bench, a file-level benchmark for this upstream retrieval problem. 为避免挤压 `AGENT-CONTEXT` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-24882:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-24893:start -->
`SF-2026-ARXIV-2607-24893` 的 exact-v1 Deep Review 已保留。其机制为：We build a working instance on a hierarchical multi-agent system, run it under benign and attacked conditions across five language models and two task domains, and record when each fragment is injected and when the payload is assembled and executed. 为避免挤压 `AGENT-MULTI-AGENT` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-24893:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-24953:start -->
`SF-2026-ARXIV-2607-24953` 的 exact-v1 Deep Review 已保留。其机制为：To address this issue, we propose a low-precision training framework based on 2D block FP4 quantization, which enforces transposition-invariant scaling and preserves consistency between forward and backward computations. 为避免挤压 `TRAIN-DISTRIBUTED-TRAINING` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-24953:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-25063:start -->
`SF-2026-ARXIV-2607-25063` 的 exact-v1 Deep Review 已保留。其机制为：After supervised fine-tuning (SFT), two checkpoints that perform about the same across relevant benchmarks are treated as interchangeable, equally ready for the next alignment stage, typically preference optimization. 为避免挤压 `TRAIN-PRETRAINING` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-25063:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-25076:start -->
`SF-2026-ARXIV-2607-25076` 的 exact-v1 Deep Review 已保留。其机制为：Agentic AI systems - autonomous, LLM-driven agents that plan, use tools, maintain memory, and collaborate - are currently in the experimentation phase of the third such wave. dozens of frameworks and protocols have emerged, but no community consensus exists on what the core abstractions are or what guarantees they carry. 为避免挤压 `AGENT-PLATFORM` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-25076:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-25152:start -->
`SF-2026-ARXIV-2607-25152` 的 exact-v1 Deep Review 已保留。其机制为：When an agent grades its own work, self-evaluation bias takes hold: plausible changes are accepted as progress while real-world outcomes stagnate or regress. 为避免挤压 `AGENT-REFLECTION` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-25152:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-25291:start -->
`SF-2026-ARXIV-2607-25291` 的 exact-v1 Deep Review 已保留。其机制为：Existing methods typically rely on a proxy to predict a binary sparse mask and a kernel to consume this mask and perform sparse attention computation. 为避免挤压 `INFER-PREFILL` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-25291:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-25297:start -->
`SF-2026-ARXIV-2607-25297` 的 exact-v1 Deep Review 已保留。其机制为：To address these limitations, we propose MTGuard, a hybrid analysis-based defense framework designed to safeguard the use of MCP tools in LLM agents by leveraging lifecycle-aware static-dynamic co-analysis. 为避免挤压 `AGENT-MCP` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-25297:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-25337:start -->
`SF-2026-ARXIV-2607-25337` 的 exact-v1 Deep Review 已保留。其机制为：Against LeWM and the concurrent RC-aux baseline under locked evaluation, Temporal-Distance-JEPA matches or exceeds both methods on every environment. 为避免挤压 `MULTIMODAL-WORLD-MODELS` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-25337:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-25364:start -->
`SF-2026-ARXIV-2607-25364` 的 exact-v1 Deep Review 已保留。其机制为：We present Explanation-Bound Tool Execution (EBTE), a claim-carrying mediation layer that converts decision-relevant rationale content into typed action claims and checks them against server-held intent, policy, payload, tool, risk, provenance, and freshness facts. 为避免挤压 `AGENT-TOOL-CALLING` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-25364:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-25379:start -->
`SF-2026-ARXIV-2607-25379` 的 exact-v1 Deep Review 已保留。其机制为：A comparative evidence protocol distinguishes record-specific factual claims from the shared systems lesson: the evaluation environment is itself part of the security boundary. 为避免挤压 `PLATFORM-SECURITY` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-25379:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-25398:start -->
`SF-2026-ARXIV-2607-25398` 的 exact-v1 Deep Review 已保留。其机制为：We present HANDBOOK_md, a benchmark of 65 agentic tasks modeled on how employees follow company handbooks. 为避免挤压 `AGENT-CONTEXT` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-25398:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-25400:start -->
`SF-2026-ARXIV-2607-25400` 的 exact-v1 Deep Review 已保留。其机制为：In this work, we propose COVENANT, a compiler-and-interpreter architecture for workflow-aligned agent execution. 为避免挤压 `AGENT-WORKFLOW` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-25400:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-25408:start -->
`SF-2026-ARXIV-2607-25408` 的 exact-v1 Deep Review 已保留。其机制为：A growing body of 2026 work applies control theory to LLM agents: Lyapunov-certified stability for tool-mediated controllers (Prinos et al., "Stable Agentic Control", 2026), sample-complexity bounds for sparse policies over massive discrete tool universes (Majumdar, "Sparse Agentic Control", 2026), and regulatory-control decompositions of multi-agent systems into auditable feedback loops (Nogueira and Skogestad, 2026). 为避免挤压 `AGENT-CONTEXT` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-25408:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-25415:start -->
`SF-2026-ARXIV-2607-25415` 的 exact-v1 Deep Review 已保留。其机制为：We release the harness-control-system code, the cross-domain verifiable task suite, the full trajectory/reward-decomposition logs from training, and a provider-agnostic deployment recipe for applying this to a new organization's domain and verification setup. 为避免挤压 `AGENT-MEMORY` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-25415:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-25431:start -->
`SF-2026-ARXIV-2607-25431` 的 exact-v1 Deep Review 已保留。其机制为：CodeNib builds reusable lexical, dense, and structural views per repository commit, maps outputs to repository-relative source ranges, maintains selected views across edits, and serves ranked search, symbol navigation, and bounded context through one runtime. 为避免挤压 `AGENT-CONTEXT` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-25431:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-25487:start -->
`SF-2026-ARXIV-2607-25487` 的 exact-v1 Deep Review 已保留。其机制为：We present CoTinyVLA, a 0.9B-parameter action model on a Qwen3.5-0.8B backbone that obtains that robustness by structuring supervision instead of enlarging the model. 为避免挤压 `MULTIMODAL-EMBODIED-VLA` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-25487:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-25504:start -->
`SF-2026-ARXIV-2607-25504` 的 exact-v1 Deep Review 已保留。其机制为：We present Ventaglio, a runtime-configurable sparse execution unit coupled with RVV ISA extensions that drives sparse tensor contractions toward their roofline through indexed gather-accumulate-scatter support. 为避免挤压 `INFER-TENSORRT-LLM` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-25504:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-25566:start -->
`SF-2026-ARXIV-2607-25566` 的 exact-v1 Deep Review 已保留。其机制为：We introduce ARCHER (Agentic Rule and Compliance Harness for Executable Regulations), a test-driven, deterministically orchestrated multi-agent program-synthesis harness that generates auditable verification code from regulatory Codes of Practice, enabling transparent, adaptable, and scalable compliance checking. 为避免挤压 `AGENT-WORKFLOW` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-25566:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-25600:start -->
`SF-2026-ARXIV-2607-25600` 的 exact-v1 Deep Review 已保留。其机制为：Our method, BeyondUncertainty, first elicits a structured provisional answer and confidence estimate, then applies a model-specific threshold selected on held-out validation data and frozen before test evaluation. 为避免挤压 `AGENT-RAG` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-25600:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-25619:start -->
`SF-2026-ARXIV-2607-25619` 的 exact-v1 Deep Review 已保留。其机制为：No systematic toolchain defense exists for this attack surface. 为避免挤压 `AGENT-SKILL` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-25619:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-25650:start -->
`SF-2026-ARXIV-2607-25650` 的 exact-v1 Deep Review 已保留。其机制为：To address these inefficiencies, we present PowerScale, a hierarchical aggregation system that exploits the latency hierarchy of wide-area networks. 为避免挤压 `TRAIN-DISTRIBUTED-TRAINING` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-25650:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-25659:start -->
`SF-2026-ARXIV-2607-25659` 的 exact-v1 Deep Review 已保留。其机制为：We propose CoRT, a token-level credit weighting method for rubric-conditioned GRPO. 为避免挤压 `TRAIN-GRPO` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-25659:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-25816:start -->
`SF-2026-ARXIV-2607-25816` 的 exact-v1 Deep Review 已保留。其机制为：To enable this dual-mode agent without degrading performance, we propose a joint agent-speculator reinforcement learning method, which derives speculation targets from the agent's own rollouts and alternates agent and speculator updates. 为避免挤压 `INFER-SPECULATIVE-DECODING` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-25816:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-25852:start -->
`SF-2026-ARXIV-2607-25852` 的 exact-v1 Deep Review 已保留。其机制为：We present AngelSpec, a unified training framework for MTP and block-parallel speculative decoding that addresses this heterogeneity at three levels. 为避免挤压 `INFER-SPECULATIVE-DECODING` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-25852:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-25884:start -->
`SF-2026-ARXIV-2607-25884` 的 exact-v1 Deep Review 已保留。其机制为：We present CONQuER, a unified compiler-integrated infrastructure for hardware-aware MPQ. 为避免挤压 `INFER-TENSORRT-LLM` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-25884:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-25886:start -->
`SF-2026-ARXIV-2607-25886` 的 exact-v1 Deep Review 已保留。其机制为：We introduce RSIBench-Data, a controlled benchmark of LLM agents as data-centric researchers with a fixed post-training stack. 为避免挤压 `PLATFORM-EVALUATION-SYSTEM` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-25886:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-25904:start -->
`SF-2026-ARXIV-2607-25904` 的 exact-v1 Deep Review 已保留。其机制为：In this paper, we propose an interactive reward agent (IRA) based on a propose-then-verify framework to acquire and verify evidence from the post-execution environment. 为避免挤压 `PLATFORM-EVALUATION-SYSTEM` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-25904:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-25970:start -->
`SF-2026-ARXIV-2607-25970` 的 exact-v1 Deep Review 已保留。其机制为：Extending this to code optimization seems straightforward: just add execution time to the reward. 为避免挤压 `TRAIN-GRPO` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-25970:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-25992:start -->
`SF-2026-ARXIV-2607-25992` 的 exact-v1 Deep Review 已保留。其机制为：To address this challenge, we present MemLens, a value-aware memory management system that takes memory records as first-class data objects. 为避免挤压 `AGENT-MEMORY` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-25992:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-26037:start -->
`SF-2026-ARXIV-2607-26037` 的 exact-v1 Deep Review 已保留。其机制为：Achieving this capability requires a system-level co-design of control method, memory mechanism, and training strategy. 为避免挤压 `MULTIMODAL-WORLD-MODELS` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-26037:end -->

### Selected Analysis Narratives

<!-- analysis:DA-20260729-01:start -->
### Conformal Cascade: Distribution-Free Accuracy Guarantees for Multi-Tier LLM Inference

**约束变化与机制。** We introduce \textbf{Conformal Cascade} (CC), a multi-tier inference framework that uses conformal prediction set size as the deferral rule: accept when the calibrated set collapses to a single answer, defer otherwise.

**证明与未证明。** Large language model (LLM) cascades reduce inference cost by routing easy queries to a small model and deferring hard queries to a larger one. 但 The Phi tier-1 saturation itself is a property of the Phi-3.5-mini-instruct checkpoint at : on benchmarks where the mini model is uniformly uncertain, the frequency-based score produces broad sets that never meet the singleton acceptance criterion, and the cascade cannot exit at tier 1. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：The Phi tier-1 saturation itself is a property of the Phi-3.5-mini-instruct checkpoint at : on benchmarks where the mini model is uniformly uncertain, the frequency-based score produces broad sets that never meet the singleton acceptance criterion, and the cascade cannot exit at tier 1. 旧方案在不承受该约束时仍成立。

关联：`review:SF-2026-ARXIV-2607-25018`。
<!-- analysis:DA-20260729-01:end -->

<!-- analysis:DA-20260729-02:start -->
### SafeFlow: Semantic Information-Flow Control for Blocking Malicious Propagation in Multi-Agent Systems

**约束变化与机制。** To address this, we propose SafeFlow, a defense framework for multi-agent systems that formalizes malicious cross-agent propagation as a semantic information-flow problem.

**证明与未证明。** SafeFlow keeps this risk visible throughout the workflow, before it results in harm. 但 Exact v1 does not disclose a dedicated generalization or deployment guarantee beyond its stated evaluation scope. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Trade-off 与共存边界。** 新的安全控制点降低特定失败，但会引入误拒绝、旁路、观测不足或模型/任务迁移问题。 论文自身的边界信号是：Exact v1 does not disclose a dedicated generalization or deployment guarantee beyond its stated evaluation scope. 旧方案在不承受该约束时仍成立。

关联：`review:SF-2026-ARXIV-2607-25255`。
<!-- analysis:DA-20260729-02:end -->

<!-- analysis:DA-20260729-03:start -->
### Beyond Prefill-Decode Disaggregation: Dissecting LLM Inference for Heterogeneous Platforms via Dynamic Operator Scheduling

**约束变化与机制。** We present DOPS (dynamic operator scheduling), a hardware-aware, closed-loop framework that jointly optimizes operator scheduling and blockwise weight layouts.

**证明与未证明。** The source code is available at https://github.com/YIAI-02/TriForm, and the visualization tool is demonstrated at https://youtu.be/Ya_oMCyYno0. 但 On these edge-oriented systems, the results show the value of moving beyond coarse prefill – decode disaggregation and static roofline rules and support future hardware–software co-design. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Trade-off 与共存边界。** 更激进的缓存、迁移、并行或专用执行会换取吞吐/时延，同时增加配置依赖、资源压力与回退路径。 论文自身的边界信号是：On these edge-oriented systems, the results show the value of moving beyond coarse prefill – decode disaggregation and static roofline rules and support future hardware–software co-design. 旧方案在不承受该约束时仍成立。

关联：`review:SF-2026-ARXIV-2607-25498`。
<!-- analysis:DA-20260729-03:end -->

## 6. Books Comparison

<!-- validator:books-comparison-v1 -->
| Source Family ID | Stable Node ID | Target Chapter Ref | Adjacent Chapter Refs | Existing Proposition | New Evidence Delta | Evolution Relation | Decision | Books Review Ref |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |

None。建议路由已冻结到 date-local queue；最终 disposition 等待 root 按日期串行对读 Books。

## 7. Semantic Audit

<!-- validator:semantic-audit-v1 -->
| Audit ID | Auditor | Scope | Reviewed Refs | Findings | Resolution | Status |
| --- | --- | --- | --- | --- | --- | --- |
| SA-20260729-COVERAGE-INDEPENDENT | fresh-context:pending-root-auditor | coverage | coverage:SRC-ARXIV:20260729 | GAP-20260729-COVERAGE-INDEPENDENT：全量筛选尚未被独立反向审计 | Pending — 逐项核验 false positive / false negative | open |
| SA-20260729-EVIDENCE-INDEPENDENT | fresh-context:pending-root-auditor | evidence | validator:review-completion-v1 | GAP-20260729-EVIDENCE-INDEPENDENT：RP 尚需独立对照 exact v1 | Pending — finding 绑定具体 family | open |
| SA-20260729-SELECTION-INDEPENDENT | fresh-context:pending-root-auditor | deep_analysis_selection | validator:deep-analysis-selection-v1 | GAP-20260729-SELECTION-INDEPENDENT：三项选择尚需 adversarial comparison | Pending — 比较 impact、反证与 owner 独立性 | open |
| SA-20260729-BOOKS-ROOT | fresh-context:pending-root-books-owner | books | validator:books-comparison-v1 | GAP-20260729-BOOKS-ROOT：尚未逐项对读 Books | Pending — root 消费 frozen queue | open |

## 8. Ignored Noise

429 项均有 family-specific pre-denominator closure：

- `embodied_task_local_method`：26
- `incremental_method_without_durable_system_delta`：322
- `local_benchmark_without_release_delta`：12
- `theory_without_ai_system_contract`：9
- `vertical_application_without_system_delta`：60

## 9. Recommended Action

1. 独立审计 Coverage、Evidence 与 Selection；finding 只重开具体 family。
2. root 逐项比较 Books。建议起点：Integrate 43、No Change 98、Structural 0；不是最终决定。

## 10. Repository Changes

- 重建 `papers/2026/07/29/README.md` 及 date-local frozen queue。
- 未修改 Books、ROADMAP、docs、Learning State、Weekly。

## 11. Open Questions

- 独立审计是否恢复 closure 中的漏项？
- proposed Integrate 是否已被现有 Books 命题覆盖？

## 12. Sources

- [Do Models Fake Alignment Without Clear Consequences?](https://arxiv.org/html/2607.24758v1) — first-public（Asia/Shanghai）：2026-07-29；exact evidence：v1；accessed：2026-09-04
- [Beyond Memory: A Templated Substrate for Heterogeneous Collaborative Knowledge Work with LLM Agents](https://arxiv.org/html/2607.24759v1) — first-public（Asia/Shanghai）：2026-07-29；exact evidence：v1；accessed：2026-09-04
- [Kernel Forge: An Agent Harness for LLM-based Generation and Optimization of CUDA Kernels](https://arxiv.org/html/2607.24762v1) — first-public（Asia/Shanghai）：2026-07-29；exact evidence：v1；accessed：2026-09-04
- [CaRE Compute-aware Remasking Evaluation Protocol for Masked Diffusion Language Models](https://arxiv.org/html/2607.24763v1) — first-public（Asia/Shanghai）：2026-07-29；exact evidence：v1；accessed：2026-09-04
- [Measuring and Improving Behavioral Consistency in Large Language Models through Fact-Heuristic-Emotion State Enforcement](https://arxiv.org/html/2607.24765v1) — first-public（Asia/Shanghai）：2026-07-29；exact evidence：v1；accessed：2026-09-04
- [LLM Scheming Inversely Scales with Pretraining Language Coverage](https://arxiv.org/html/2607.24769v1) — first-public（Asia/Shanghai）：2026-07-29；exact evidence：v1；accessed：2026-09-04
- [RoCo-ACE: Rollout-Conditioned Online Distillation for Retention-Aware Knowledge Injection](https://arxiv.org/html/2607.24771v1) — first-public（Asia/Shanghai）：2026-07-29；exact evidence：v1；accessed：2026-09-04
- [JKO-RAG: Distributional Retrieval as Wasserstein Free-Energy Gradient Flow](https://arxiv.org/html/2607.24776v1) — first-public（Asia/Shanghai）：2026-07-29；exact evidence：v1；accessed：2026-09-04
- [LivingArena: Do LLMs Know What Other LLMs Don't? Peer-Probing as Scalable Evaluation](https://arxiv.org/html/2607.24780v1) — first-public（Asia/Shanghai）：2026-07-29；exact evidence：v1；accessed：2026-09-04
- [Three Sides of Retrieval: Factorial Evidence for Document-Side, Query-Side, and Answer-Side Complementarity in RAG](https://arxiv.org/pdf/2607.24781v1) — first-public（Asia/Shanghai）：2026-07-29；exact evidence：v1；accessed：2026-09-04
- [SpecPrefetch: Parameter-Efficient Expert Prefetching for Sparse MoE Foundation Models](https://arxiv.org/html/2607.24787v1) — first-public（Asia/Shanghai）：2026-07-29；exact evidence：v1；accessed：2026-09-04
- [GLIDE: Guided Layerwise Hybrid Attention for Efficient LLM Inference](https://arxiv.org/html/2607.24788v1) — first-public（Asia/Shanghai）：2026-07-29；exact evidence：v1；accessed：2026-09-04
- [Reasoning with Memory: A Temporal Granularity-Adaptive Framework for Training-Free Long Video Understanding](https://arxiv.org/html/2607.24794v1) — first-public（Asia/Shanghai）：2026-07-29；exact evidence：v1；accessed：2026-09-04
- [Prediction Is Not Memory: Dual-Timescale Gated Profile Writing for Persistent User Modeling](https://arxiv.org/html/2607.24798v1) — first-public（Asia/Shanghai）：2026-07-29；exact evidence：v1；accessed：2026-09-04
- [When Thinking Before Retrieval Hurts: TraceBound Diagnostics for Adaptive Knowledge-Graph Retrieval](https://arxiv.org/html/2607.24800v1) — first-public（Asia/Shanghai）：2026-07-29；exact evidence：v1；accessed：2026-09-04
- [Forgetting Is Not a Fix: Path Dependence in Sequential Engram Editing](https://arxiv.org/html/2607.24805v1) — first-public（Asia/Shanghai）：2026-07-29；exact evidence：v1；accessed：2026-09-04
- [AVE-Compass: Towards Holistic Evaluation for Audio-Video Editing Abilities](https://arxiv.org/html/2607.24821v1) — first-public（Asia/Shanghai）：2026-07-29；exact evidence：v1；accessed：2026-09-04
- [Neuromorphic Diffusion Language Models: Addressing Compute and Memory Bottlenecks via Sparsity and Block Denoising](https://arxiv.org/html/2607.24841v1) — first-public（Asia/Shanghai）：2026-07-29；exact evidence：v1；accessed：2026-09-04
- [SearchArt: Training Long-Horizon Search Agent with Scalable Synthetic and Verified Task](https://arxiv.org/html/2607.24850v1) — first-public（Asia/Shanghai）：2026-07-29；exact evidence：v1；accessed：2026-09-04
- [The Mirage of LLM Guardrails: A Case Study in AI-Assisted Medical Note Manipulation](https://arxiv.org/html/2607.24859v1) — first-public（Asia/Shanghai）：2026-07-29；exact evidence：v1；accessed：2026-09-04
- [The Missing Layer: Specification Infrastructure for AI Oversight](https://arxiv.org/html/2607.24866v1) — first-public（Asia/Shanghai）：2026-07-29；exact evidence：v1；accessed：2026-09-04
- [FinAbstain: Uncertainty-Calibrated Multimodal RAG for Selective Financial Forecasting](https://arxiv.org/html/2607.24875v1) — first-public（Asia/Shanghai）：2026-07-29；exact evidence：v1；accessed：2026-09-04
- [Agent Retrieval Bench: Evaluating Repository Context Retrieval for Coding Agents](https://arxiv.org/html/2607.24882v1) — first-public（Asia/Shanghai）：2026-07-29；exact evidence：v1；accessed：2026-09-04
- [Beyond "What to Retrieve": Uncertainty in Retrieval-Augmented Code Generation](https://arxiv.org/html/2607.24884v1) — first-public（Asia/Shanghai）：2026-07-29；exact evidence：v1；accessed：2026-09-04
- [Mechanisms of Width Scaling in Normalized Residual Networks: The Effective Alignment Dimension](https://arxiv.org/html/2607.24887v1) — first-public（Asia/Shanghai）：2026-07-29；exact evidence：v1；accessed：2026-09-04
- [GAUGE: Grading Agent-Built Financial Models Without a Golden Answer](https://arxiv.org/html/2607.24889v1) — first-public（Asia/Shanghai）：2026-07-29；exact evidence：v1；accessed：2026-09-04
- [Early Detection of Distributed Backdoors in Multi-Agent LLM Systems: A Characterization Study](https://arxiv.org/html/2607.24893v1) — first-public（Asia/Shanghai）：2026-07-29；exact evidence：v1；accessed：2026-09-04
- [TYPO: Instruction-Dense Visual Jailbreaks against Commercial Closed-Source Image-Generation Models](https://arxiv.org/html/2607.24897v1) — first-public（Asia/Shanghai）：2026-07-29；exact evidence：v1；accessed：2026-09-04
- [Inverse RL Helps Align AI by Imitating Humans](https://arxiv.org/html/2607.24900v1) — first-public（Asia/Shanghai）：2026-07-29；exact evidence：v1；accessed：2026-09-04
- [Mage-VL: An Efficient Codec-Native Streaming Multimodal Foundation Model](https://arxiv.org/html/2607.24904v1) — first-public（Asia/Shanghai）：2026-07-29；exact evidence：v1；accessed：2026-09-04
- [Stable FP4 Training via Transposition-Invariant Block Quantization](https://arxiv.org/html/2607.24953v1) — first-public（Asia/Shanghai）：2026-07-29；exact evidence：v1；accessed：2026-09-04
- [PerceptionBench: Evaluating Atomic Visual Perception in Multimodal Large Language Models](https://arxiv.org/html/2607.24957v1) — first-public（Asia/Shanghai）：2026-07-29；exact evidence：v1；accessed：2026-09-04
- [ALIBI: Adaptive Agentic Attacks on LLM-Based Vulnerability Detectors via Adversarial Code Comments](https://arxiv.org/html/2607.24964v1) — first-public（Asia/Shanghai）：2026-07-29；exact evidence：v1；accessed：2026-09-04
- [Enabling Fully Integer-Only Inference for Lightweight Detection Transformers](https://arxiv.org/html/2607.24981v1) — first-public（Asia/Shanghai）：2026-07-29；exact evidence：v1；accessed：2026-09-04
- [Calibrated Partial Resets: Preventing Policy Collapse in Continual Reinforcement Learning](https://arxiv.org/html/2607.24996v1) — first-public（Asia/Shanghai）：2026-07-29；exact evidence：v1；accessed：2026-09-04
- [Conformal Cascade: Distribution-Free Accuracy Guarantees for Multi-Tier LLM Inference](https://arxiv.org/html/2607.25018v1) — first-public（Asia/Shanghai）：2026-07-29；exact evidence：v1；accessed：2026-09-04
- [Interactive Alignment](https://arxiv.org/html/2607.25019v1) — first-public（Asia/Shanghai）：2026-07-29；exact evidence：v1；accessed：2026-09-04
- [Authoring Agent Skills: A Software-Engineering Approach](https://arxiv.org/html/2607.25032v1) — first-public（Asia/Shanghai）：2026-07-29；exact evidence：v1；accessed：2026-09-04
- [Similar Models Learn Differently: Final-Window Pretraining Shapes Post-Training Beyond SFT](https://arxiv.org/html/2607.25063v1) — first-public（Asia/Shanghai）：2026-07-29；exact evidence：v1；accessed：2026-09-04
- [Addressable Recall Compaction for Long Context-Window Control in AI Agents](https://arxiv.org/html/2607.25066v1) — first-public（Asia/Shanghai）：2026-07-29；exact evidence：v1；accessed：2026-09-04
- [Towards an Agent Operating System - Lessons from Classical and Cloud OS](https://arxiv.org/html/2607.25076v1) — first-public（Asia/Shanghai）：2026-07-29；exact evidence：v1；accessed：2026-09-04
- [PLATO: Pointer Learner for Agent and Task Openness](https://arxiv.org/html/2607.25082v1) — first-public（Asia/Shanghai）：2026-07-29；exact evidence：v1；accessed：2026-09-04
- [Matryoshka Agent: Unfolding Sub-Agents for Long-Horizon Machine Learning Engineering](https://arxiv.org/html/2607.25090v1) — first-public（Asia/Shanghai）：2026-07-29；exact evidence：v1；accessed：2026-09-04
- [Towards Robust Reinforcement Learning for Small-Scale Language Model Agents](https://arxiv.org/html/2607.25091v1) — first-public（Asia/Shanghai）：2026-07-29；exact evidence：v1；accessed：2026-09-04
- [ScalableRAG: High-Quality RAG at Zero Ingestion Cost](https://arxiv.org/html/2607.25135v1) — first-public（Asia/Shanghai）：2026-07-29；exact evidence：v1；accessed：2026-09-04
- [Less Data, Better Alignment: Data-Centric Multi-Evaluator Agreement for Preference Optimization](https://arxiv.org/html/2607.25136v1) — first-public（Asia/Shanghai）：2026-07-29；exact evidence：v1；accessed：2026-09-04
- [HiEviDR-Bench: A Benchmark for Hierarchical Evidence Aggregation in Deep Research](https://arxiv.org/html/2607.25151v1) — first-public（Asia/Shanghai）：2026-07-29；exact evidence：v1；accessed：2026-09-04
- [When Do Agent Loops Mistake Stagnation for Progress? Self-Evaluation Bias and Externally Grounded Verification in Long-Running Autonomous LLM Agent Loops](https://arxiv.org/pdf/2607.25152v1) — first-public（Asia/Shanghai）：2026-07-29；exact evidence：v1；accessed：2026-09-04
- [PreDiff-LM: Pretrained Discrete Masked Diffusion Language Modeling with Hybrid Attention](https://arxiv.org/html/2607.25157v1) — first-public（Asia/Shanghai）：2026-07-29；exact evidence：v1；accessed：2026-09-04
- [Rethinking CD: A Reproducibility Study and Extension on the Ineffectiveness of Contrastive Decoding at Mitigating Object Hallucinations in MLLMs](https://arxiv.org/html/2607.25196v1) — first-public（Asia/Shanghai）：2026-07-29；exact evidence：v1；accessed：2026-09-04
- [SecDrift: Measuring Sector-Conditioned Security Drift in AI-Generated Code](https://arxiv.org/html/2607.25225v1) — first-public（Asia/Shanghai）：2026-07-29；exact evidence：v1；accessed：2026-09-04
- [Decision-Level Hijacking: Injecting Cognitive Bias into Large Language Models via Bit-Flip Attacks](https://arxiv.org/html/2607.25227v1) — first-public（Asia/Shanghai）：2026-07-29；exact evidence：v1；accessed：2026-09-04
- [VisualPatchWorld: Code World Models as Latent Structured Representations for Planning](https://arxiv.org/html/2607.25236v1) — first-public（Asia/Shanghai）：2026-07-29；exact evidence：v1；accessed：2026-09-04
- [SafeFlow: Semantic Information-Flow Control for Blocking Malicious Propagation in Multi-Agent Systems](https://arxiv.org/html/2607.25255v1) — first-public（Asia/Shanghai）：2026-07-29；exact evidence：v1；accessed：2026-09-04
- [Laplace-PSN-IRT: Uncertainty Quantification for Neural Item Response Theory Models of LLM Benchmarks](https://arxiv.org/html/2607.25257v1) — first-public（Asia/Shanghai）：2026-07-29；exact evidence：v1；accessed：2026-09-04
- [Bridging Compute- and Data-Optimal Pretraining](https://arxiv.org/html/2607.25271v1) — first-public（Asia/Shanghai）：2026-07-29；exact evidence：v1；accessed：2026-09-04
- [CoSA: Accelerating Long-Context Inference via Proxy-Kernel Co-Designed Sparse Attention](https://arxiv.org/html/2607.25291v1) — first-public（Asia/Shanghai）：2026-07-29；exact evidence：v1；accessed：2026-09-04
- [Instruction-Tuned Language Models Cannot Sample from Distributions They Can Describe](https://arxiv.org/html/2607.25292v1) — first-public（Asia/Shanghai）：2026-07-29；exact evidence：v1；accessed：2026-09-04
- [CLBench-V: Evaluating Multimodal Context Learning from Grounding to Knowledge Acquisition](https://arxiv.org/html/2607.25294v1) — first-public（Asia/Shanghai）：2026-07-29；exact evidence：v1；accessed：2026-09-04
- [Hybrid Analysis for Secure MCP Tool Use in LLM Agents](https://arxiv.org/html/2607.25297v1) — first-public（Asia/Shanghai）：2026-07-29；exact evidence：v1；accessed：2026-09-04
- [Specula: Scaling formal specifications for autonomous model checking of system code](https://arxiv.org/html/2607.25333v1) — first-public（Asia/Shanghai）：2026-07-29；exact evidence：v1；accessed：2026-09-04
- [Every Time I Hire a Linguist, Inference Costs Go Down: On Linguistic Rules as Effective Prompt Compressors](https://arxiv.org/html/2607.25335v1) — first-public（Asia/Shanghai）：2026-07-29；exact evidence：v1；accessed：2026-09-04
- [Temporal-Distance JEPA: Plan-Aware Representation Learning for Latent World Model Predictive Control](https://arxiv.org/html/2607.25337v1) — first-public（Asia/Shanghai）：2026-07-29；exact evidence：v1；accessed：2026-09-04
- [The Case Against Generation for Retrieval: Discriminative Language Models as Effective Retrievers](https://arxiv.org/html/2607.25346v1) — first-public（Asia/Shanghai）：2026-07-29；exact evidence：v1；accessed：2026-09-04
- [Data Quality Profiling at Scale with Progressive Sampling: A Benchmark for Data-Centric AI Pipelines](https://arxiv.org/html/2607.25356v1) — first-public（Asia/Shanghai）：2026-07-29；exact evidence：v1；accessed：2026-09-04
- [Raven: High-Recall Sequence Modeling with Sparse Memory Routing](https://arxiv.org/html/2607.25357v1) — first-public（Asia/Shanghai）：2026-07-29；exact evidence：v1；accessed：2026-09-04
- [Explanation-Bound Tool Execution for AI Agents: Server-Verified Action Claims Without Trusting Model Rationales](https://arxiv.org/html/2607.25364v1) — first-public（Asia/Shanghai）：2026-07-29；exact evidence：v1；accessed：2026-09-04
- [ODYSSE: Episode-wise Policy Optimization for Personalized Agentic Reasoning](https://arxiv.org/html/2607.25369v1) — first-public（Asia/Shanghai）：2026-07-29；exact evidence：v1；accessed：2026-09-04
- [Cyber-Capable AI Agents: Vulnerabilities, Evaluation Containment, and Defensive Response](https://arxiv.org/html/2607.25379v1) — first-public（Asia/Shanghai）：2026-07-29；exact evidence：v1；accessed：2026-09-04
- [Memory for Large Language Models](https://arxiv.org/html/2607.25380v1) — first-public（Asia/Shanghai）：2026-07-29；exact evidence：v1；accessed：2026-09-04
- [HANDBOOK.md: A Benchmark for Long-Context Agentic Instruction Following](https://arxiv.org/html/2607.25398v1) — first-public（Asia/Shanghai）：2026-07-29；exact evidence：v1；accessed：2026-09-04
- [COVENANT: Natural-Language Workflow Compilation for Aligned Agent Execution](https://arxiv.org/html/2607.25400v1) — first-public（Asia/Shanghai）：2026-07-29；exact evidence：v1；accessed：2026-09-04
- [Context Assembly as the Controlled Variable: A Control-Theoretic View of Harness Policies for Frozen LLM Agents](https://arxiv.org/html/2607.25408v1) — first-public（Asia/Shanghai）：2026-07-29；exact evidence：v1；accessed：2026-09-04
- [A Control System, a Dataset, and a Recipe for Making Frozen LLM Agents Learn a Domain](https://arxiv.org/html/2607.25415v1) — first-public（Asia/Shanghai）：2026-07-29；exact evidence：v1；accessed：2026-09-04
- [CodeNib: A Multi-View Data System for Serving Repository Context to Coding Agents](https://arxiv.org/html/2607.25431v1) — first-public（Asia/Shanghai）：2026-07-29；exact evidence：v1；accessed：2026-09-04
- [Toward an Organizational Science of Multi-Agent LLM Systems: Decoupling Who, How, and Which Algorithm](https://arxiv.org/html/2607.25446v1) — first-public（Asia/Shanghai）：2026-07-29；exact evidence：v1；accessed：2026-09-04
- [Bits and Memories: Measuring Verbatim Extraction Across LLM Quantization](https://arxiv.org/html/2607.25451v1) — first-public（Asia/Shanghai）：2026-07-29；exact evidence：v1；accessed：2026-09-04
- [Seen, Said, or Forgotten? A Causal Audit of Visual KV Memory Across Dialog Turns](https://arxiv.org/html/2607.25467v1) — first-public（Asia/Shanghai）：2026-07-29；exact evidence：v1；accessed：2026-09-04
- [Architectural Backdoors in Vision-Language Model Supply Chains via Representation Steering](https://arxiv.org/html/2607.25479v1) — first-public（Asia/Shanghai）：2026-07-29；exact evidence：v1；accessed：2026-09-04
- [CoTinyVLA: Chain-of-Thought Distillation for a Sub-Billion-Parameter Vision-Language-Action Model](https://arxiv.org/html/2607.25487v1) — first-public（Asia/Shanghai）：2026-07-29；exact evidence：v1；accessed：2026-09-04
- [Automated Numerical Stability Analysis of Deep Learning Operators](https://arxiv.org/html/2607.25494v1) — first-public（Asia/Shanghai）：2026-07-29；exact evidence：v1；accessed：2026-09-04
- [Beyond Prefill-Decode Disaggregation: Dissecting LLM Inference for Heterogeneous Platforms via Dynamic Operator Scheduling](https://arxiv.org/html/2607.25498v1) — first-public（Asia/Shanghai）：2026-07-29；exact evidence：v1；accessed：2026-09-04
- [At-the-Roofline Sparse Tensor Contractions on Vector Processors for Transformer Inference](https://arxiv.org/html/2607.25504v1) — first-public（Asia/Shanghai）：2026-07-29；exact evidence：v1；accessed：2026-09-04
- [Phase Structure in Rotary Attention: A Spectral Framework for Semantic Continuity and Execution-Boundary Governance](https://arxiv.org/html/2607.25507v1) — first-public（Asia/Shanghai）：2026-07-29；exact evidence：v1；accessed：2026-09-04
- [A Causality-aware Infer-diagnose-refine Framework for Test-time Modality Adaptation in VLA Models](https://arxiv.org/html/2607.25516v1) — first-public（Asia/Shanghai）：2026-07-29；exact evidence：v1；accessed：2026-09-04
- [Distilling Temporal Search and Reasoning: Evolving LLMs for Future Prediction via Harness-Assisted Efficient Data Synthesis](https://arxiv.org/html/2607.25554v1) — first-public（Asia/Shanghai）：2026-07-29；exact evidence：v1；accessed：2026-09-04
- [Agent Skills Matter: Inferring Proprietary Skills from Execution Trajectories](https://arxiv.org/html/2607.25560v1) — first-public（Asia/Shanghai）：2026-07-29；exact evidence：v1；accessed：2026-09-04
- [ARCHER: Agentic Rule and Compliance Harness for Executable Regulations](https://arxiv.org/html/2607.25566v1) — first-public（Asia/Shanghai）：2026-07-29；exact evidence：v1；accessed：2026-09-04
- [How Small Can You Go? A Controlled Study of LoRA Rank, Target Modules, and Quantization Trade-offs for Text-to-SQL on a 60M-Parameter Model](https://arxiv.org/html/2607.25583v1) — first-public（Asia/Shanghai）：2026-07-29；exact evidence：v1；accessed：2026-09-04
- [Forensic Reproducibility Audit of a Radiology Vision-Language Model Benchmark: From Intended Protocol to Released Artifact](https://arxiv.org/html/2607.25589v1) — first-public（Asia/Shanghai）：2026-07-29；exact evidence：v1；accessed：2026-09-04
- [Beyond Self-Knowledge: Propagating Uncertainty Across Reasoning and Retrieval in LLMs](https://arxiv.org/html/2607.25600v1) — first-public（Asia/Shanghai）：2026-07-29；exact evidence：v1；accessed：2026-09-04
- [MemSFT: Mitigating Alignment Tax with an External Parametric Memory](https://arxiv.org/html/2607.25614v1) — first-public（Asia/Shanghai）：2026-07-29；exact evidence：v1；accessed：2026-09-04
- [SkillGate: Cost Efficient Runtime Malicious Skill File Detection in Coding Agents](https://arxiv.org/html/2607.25619v1) — first-public（Asia/Shanghai）：2026-07-29；exact evidence：v1；accessed：2026-09-04
- [An Empirical Study of Model Context Protocol Applications](https://arxiv.org/html/2607.25635v1) — first-public（Asia/Shanghai）：2026-07-29；exact evidence：v1；accessed：2026-09-04
- [F(AI)2R: Who Did What, and Who Checked? Verifiable AI Provenance as an Executable Skill](https://arxiv.org/html/2607.25637v1) — first-public（Asia/Shanghai）：2026-07-29；exact evidence：v1；accessed：2026-09-04
- [PowerScale: Energy-Efficient Geo-Distributed Model Training with Federated Datacenter Power](https://arxiv.org/html/2607.25650v1) — first-public（Asia/Shanghai）：2026-07-29；exact evidence：v1；accessed：2026-09-04
- [Demystifying Deep Learning Compiler Frontend Bugs: An LLM-Aided Empirical Study](https://arxiv.org/html/2607.25651v1) — first-public（Asia/Shanghai）：2026-07-29；exact evidence：v1；accessed：2026-09-04
- [OrchBench: Evaluating Multi-Agent Orchestration Plans in Isolation via Deterministic Simulation](https://arxiv.org/html/2607.25656v1) — first-public（Asia/Shanghai）：2026-07-29；exact evidence：v1；accessed：2026-09-04
- [CoRT: Counterfactual Replay for Token-Level Rubric-Guided Policy Optimization](https://arxiv.org/html/2607.25659v1) — first-public（Asia/Shanghai）：2026-07-29；exact evidence：v1；accessed：2026-09-04
- [Localized Adaptation Reveals Distinct Learning Signatures in Transformers](https://arxiv.org/html/2607.25663v1) — first-public（Asia/Shanghai）：2026-07-29；exact evidence：v1；accessed：2026-09-04
- [OmniDelta: Skill-Driven Budget Allocation for Token Compression in OmniLLMs](https://arxiv.org/html/2607.25669v1) — first-public（Asia/Shanghai）：2026-07-29；exact evidence：v1；accessed：2026-09-04
- [Tools Are Not Islands: Set-Level Tool Retrieval for LLM Agents via Query-Conditioned Hyperedge Prediction](https://arxiv.org/html/2607.25718v1) — first-public（Asia/Shanghai）：2026-07-29；exact evidence：v1；accessed：2026-09-04
- [Detecting CSAM Text-to-Image LoRAs From Weights](https://arxiv.org/html/2607.25750v1) — first-public（Asia/Shanghai）：2026-07-29；exact evidence：v1；accessed：2026-09-04
- [WorkSurface-Bench: Benchmarking Enterprise Agents on Multi-Surface Knowledge Routing](https://arxiv.org/html/2607.25765v1) — first-public（Asia/Shanghai）：2026-07-29；exact evidence：v1；accessed：2026-09-04
- [Transformer Transformer: A Unified Model for Motion-Conditioned Robot Co-design](https://arxiv.org/html/2607.25798v1) — first-public（Asia/Shanghai）：2026-07-29；exact evidence：v1；accessed：2026-09-04
- [Speculate While You Reason: Teaching Agents to Predict Their Next Tool Call via Joint Agent-Speculator RL](https://arxiv.org/html/2607.25816v1) — first-public（Asia/Shanghai）：2026-07-29；exact evidence：v1；accessed：2026-09-04
- [SepPrune:A Separator-based Pruning Framework for Efficient Multimodal Large Language Models](https://arxiv.org/html/2607.25818v1) — first-public（Asia/Shanghai）：2026-07-29；exact evidence：v1；accessed：2026-09-04
- [CHILL-Harness: Counterfactual Harness Learning for Efficient Reasoning in Long-Horizon Agents](https://arxiv.org/html/2607.25825v1) — first-public（Asia/Shanghai）：2026-07-29；exact evidence：v1；accessed：2026-09-04
- [WarmTuner: Program-Specific Warm Starts for Compiler Autotuning via Offline-to-Online Reinforcement Learning](https://arxiv.org/html/2607.25831v1) — first-public（Asia/Shanghai）：2026-07-29；exact evidence：v1；accessed：2026-09-04
- [AngelSpec: Towards Real-World High Performance Inference with Speculative Decoding](https://arxiv.org/html/2607.25852v1) — first-public（Asia/Shanghai）：2026-07-29；exact evidence：v1；accessed：2026-09-04
- [HiSkill: Empowering LLM Agents with Hierarchical Skill Graphs](https://arxiv.org/html/2607.25853v1) — first-public（Asia/Shanghai）：2026-07-29；exact evidence：v1；accessed：2026-09-04
- [Shieldstral](https://arxiv.org/html/2607.25857v1) — first-public（Asia/Shanghai）：2026-07-29；exact evidence：v1；accessed：2026-09-04
- [Runtime Uncertainty Monitoring for LLM-Based Multi-Agent Systems Using Bayesian Networks](https://arxiv.org/html/2607.25877v1) — first-public（Asia/Shanghai）：2026-07-29；exact evidence：v1；accessed：2026-09-04
- [Stemma: Induced Decision Regions Reveal LLM Provenance](https://arxiv.org/html/2607.25880v1) — first-public（Asia/Shanghai）：2026-07-29；exact evidence：v1；accessed：2026-09-04
- [Towards a Systems Foundation for Agentic Cloud Management](https://arxiv.org/html/2607.25883v1) — first-public（Asia/Shanghai）：2026-07-29；exact evidence：v1；accessed：2026-09-04
- [CONQuER: Hardware-Aware Mixed-Precision Quantisation with Online-Calibrated Surrogates](https://arxiv.org/html/2607.25884v1) — first-public（Asia/Shanghai）：2026-07-29；exact evidence：v1；accessed：2026-09-04
- [RSIBench-Data: Benchmarking Data-Centric Research for Recursive Self-Improvement](https://arxiv.org/html/2607.25886v1) — first-public（Asia/Shanghai）：2026-07-29；exact evidence：v1；accessed：2026-09-04
- [Distributing Security Controls Through Harness Engineering](https://arxiv.org/html/2607.25890v1) — first-public（Asia/Shanghai）：2026-07-29；exact evidence：v1；accessed：2026-09-04
- [Messier: A High-Resolution Corpus for Cross-Benchmark Agent Evaluation](https://arxiv.org/html/2607.25891v1) — first-public（Asia/Shanghai）：2026-07-29；exact evidence：v1；accessed：2026-09-04
- [Interactive Reward Agent: GUI Task Evaluation via Environment-State Verification](https://arxiv.org/html/2607.25904v1) — first-public（Asia/Shanghai）：2026-07-29；exact evidence：v1；accessed：2026-09-04
- [Minimizing Targeted Activations: Input-Only Suppression of Evaluation-Awareness Latents in Large Language Models](https://arxiv.org/html/2607.25907v1) — first-public（Asia/Shanghai）：2026-07-29；exact evidence：v1；accessed：2026-09-04
- [SAM3D-Guided Object-Centric Representation Alignment for Vision-Language-Action Models](https://arxiv.org/html/2607.25912v1) — first-public（Asia/Shanghai）：2026-07-29；exact evidence：v1；accessed：2026-09-04
- [Toward Standardized Cross-Vendor Agent Tool Trust Management in Autonomous Networks](https://arxiv.org/html/2607.25914v1) — first-public（Asia/Shanghai）：2026-07-29；exact evidence：v1；accessed：2026-09-04
- [Penelope: Localized Latent Recurrence for Efficient Structured Reasoning](https://arxiv.org/html/2607.25915v1) — first-public（Asia/Shanghai）：2026-07-29；exact evidence：v1；accessed：2026-09-04
- [DC-WAM: Dynamic-Centric Visual Supervision and Reasoning for World-Action Models](https://arxiv.org/html/2607.25918v1) — first-public（Asia/Shanghai）：2026-07-29；exact evidence：v1；accessed：2026-09-04
- [From Role Prompt to Infinite Thinking: Exploiting Persona Conditioning for Inference Cost Attacks in LLMs](https://arxiv.org/html/2607.25936v1) — first-public（Asia/Shanghai）：2026-07-29；exact evidence：v1；accessed：2026-09-04
- [MODUS: Decoder-Only Any-to-Any Modeling of Diverse Modalities](https://arxiv.org/html/2607.25948v1) — first-public（Asia/Shanghai）：2026-07-29；exact evidence：v1；accessed：2026-09-04
- [Reinforcement Learning for Code Optimization](https://arxiv.org/html/2607.25970v1) — first-public（Asia/Shanghai）：2026-07-29；exact evidence：v1；accessed：2026-09-04
- [IH-Benchmark: A Conflict-Centered Benchmark for Instruction-Hierarchy Robustness in LLM Applications](https://arxiv.org/html/2607.25987v1) — first-public（Asia/Shanghai）：2026-07-29；exact evidence：v1；accessed：2026-09-04
- [MemLens: A Value-Aware Memory Management System with Interactive Analytics for LLM-based Agents](https://arxiv.org/html/2607.25992v1) — first-public（Asia/Shanghai）：2026-07-29；exact evidence：v1；accessed：2026-09-04
- [Does Runtime Topology Context Improve LLM-Generated Kubernetes Security Patches?](https://arxiv.org/html/2607.25995v1) — first-public（Asia/Shanghai）：2026-07-29；exact evidence：v1；accessed：2026-09-04
- [RepoReasoner: Evaluating Repository-Level Code Reasoning Ability of Long-Context Language Models](https://arxiv.org/html/2607.25996v1) — first-public（Asia/Shanghai）：2026-07-29；exact evidence：v1；accessed：2026-09-04
- [Parallel Decoding Distillation for Fast Image and Video Generation](https://arxiv.org/html/2607.26004v1) — first-public（Asia/Shanghai）：2026-07-29；exact evidence：v1；accessed：2026-09-04
- [MDTransformer: A Hardware-Software Co-Design of Mode-Division Photonic Transformer Accelerator with Inverse-Designed Coherent Crossbar](https://arxiv.org/html/2607.26016v1) — first-public（Asia/Shanghai）：2026-07-29；exact evidence：v1；accessed：2026-09-04
- [UniMem: Complementary Episodic-to-Parametric Memory for Boundary-Agnostic Task Streams](https://arxiv.org/html/2607.26017v1) — first-public（Asia/Shanghai）：2026-07-29；exact evidence：v1；accessed：2026-09-04
- [Wonder: Video World Model Done Better](https://arxiv.org/html/2607.26037v1) — first-public（Asia/Shanghai）：2026-07-29；exact evidence：v1；accessed：2026-09-04
- [Reinformed Dreamer: An Asymmetric World Model Efficiently Trained through Latent Guidance](https://arxiv.org/pdf/2607.26040v1) — first-public（Asia/Shanghai）：2026-07-29；exact evidence：v1；accessed：2026-09-04
- [Desktop-Delta Bench: Do Computer-Use Models Understand Desktop GUI Transitions?](https://arxiv.org/pdf/2607.26041v1) — first-public（Asia/Shanghai）：2026-07-29；exact evidence：v1；accessed：2026-09-04
- [Spend Experts Where You Are Unsure: Confidence-Adaptive Routing for Mixture-of-Experts LoRA](https://arxiv.org/html/2607.26052v1) — first-public（Asia/Shanghai）：2026-07-29；exact evidence：v1；accessed：2026-09-04
- [$π\mathbf{R}^2$: Reactive Real-time Flow Policies](https://arxiv.org/html/2607.26055v1) — first-public（Asia/Shanghai）：2026-07-29；exact evidence：v1；accessed：2026-09-04
- [INTACT: Isomorphic Intent-to-Action Learning for Search-Free World Models](https://arxiv.org/html/2607.26056v1) — first-public（Asia/Shanghai）：2026-07-29；exact evidence：v1；accessed：2026-09-04

## 13. Final Status

Author-side screening、denominator、exact-v1 access、141/141 Review 与 Deep Selection receipt 已构建；Books 写回冻结，四项独立审计未完成。

State Truth: Completion=In Progress；Coverage=Open；Evidence=Open；Books=Open；Unresolved Findings=4。
