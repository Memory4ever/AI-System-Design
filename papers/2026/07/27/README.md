# Daily Research — 2026-07-27

**Research Date:** 2026-07-27

**Timezone:** Asia/Shanghai

**Strict Window:** 2026-07-26 09:00:00 ～ 2026-07-27 09:00:00（北京时间，左闭右开）

**Contract:** V2.1 Full Replay；Historical Daily 独立重建，不使用 Weekly 作为 discovery、评分或 Review 来源

**Status:** In Progress；Coverage=Open、Evidence=Open、Books=Open；author-side evidence 已闭合，等待独立 Semantic Audit 与 root Books 比较

## Executive Summary

官方 owner inventory 共 **383** 个 identity；全量 title + abstract 筛选后冻结 **100** 个候选与 **283** 个 family-specific closure，retain rate **26.11%**。exact-v1 Review 为 100/100：Deep 33、Standard 67、blocked 0。

当前只是 author-side evidence 闭合：Books disposition 仍为 `Not Assessed`，四项 fresh-context 独立审计保持 Open。

## 1. Coverage

<!-- validator:report-metadata-v2 -->
| Field | Value |
| --- | --- |
| Contract Version | V2.1 |
| Score Schema | V2 |
| Report Type | Daily |
| Window Start | 2026-07-27 |
| Window End | 2026-07-27 |
| Registry Version | 2026-08-25 |
| Coverage Mode | Full Replay |
| Baseline Report | — |
| Changed Source IDs | — |
| Previous Denominator ID | — |
| Denominator ID | daily-2026-07-27-0900-v2.1-sha256:58a0920341e090f827435419c4b2380954f8795d81208ddc9a5d8b334b135eec |
| Denominator Frozen At | 2026-09-04T20:00:00+08:00 |
| Completion Status | In Progress |
| Coverage Gate | Open |
| Evidence Gate | Open |
| Books Gate | Open |

### Source Coverage Receipt

<!-- coverage:SRC-ARXIV:20260727:start -->
<!-- validator:source-coverage-v2 -->
| Source ID | Window Start | Window End | Executed At | Endpoint / Filter | Result | Hits | Candidate Source Families | Pagination / Cursor | Window Watermark | Closure Evidence | Gap / Limitation ID |
| --- | --- | --- | --- | --- | --- | ---: | --- | --- | --- | --- | --- |
| SRC-ARXIV | 2026-07-26T09:00:00+08:00 | 2026-07-27T09:00:00+08:00 | 2026-09-04T20:00:00+08:00 | official listings + v1 history + availability schedule; DataCite created only for cycle reconciliation | checked | 383 | SF-2026-ARXIV-2607-21596;SF-2026-ARXIV-2607-21599;SF-2026-ARXIV-2607-21600;SF-2026-ARXIV-2607-21602;SF-2026-ARXIV-2607-21604;SF-2026-ARXIV-2607-21606;SF-2026-ARXIV-2607-21609;SF-2026-ARXIV-2607-21610;SF-2026-ARXIV-2607-21612;SF-2026-ARXIV-2607-21613;SF-2026-ARXIV-2607-21616;SF-2026-ARXIV-2607-21617;SF-2026-ARXIV-2607-21619;SF-2026-ARXIV-2607-21623;SF-2026-ARXIV-2607-21624;SF-2026-ARXIV-2607-21625;SF-2026-ARXIV-2607-21627;SF-2026-ARXIV-2607-21632;SF-2026-ARXIV-2607-21635;SF-2026-ARXIV-2607-21641;SF-2026-ARXIV-2607-21642;SF-2026-ARXIV-2607-21646;SF-2026-ARXIV-2607-21653;SF-2026-ARXIV-2607-21656;SF-2026-ARXIV-2607-21661;SF-2026-ARXIV-2607-21670;SF-2026-ARXIV-2607-21672;SF-2026-ARXIV-2607-21674;SF-2026-ARXIV-2607-21686;SF-2026-ARXIV-2607-21722;SF-2026-ARXIV-2607-21725;SF-2026-ARXIV-2607-21731;SF-2026-ARXIV-2607-21735;SF-2026-ARXIV-2607-21738;SF-2026-ARXIV-2607-21746;SF-2026-ARXIV-2607-21752;SF-2026-ARXIV-2607-21756;SF-2026-ARXIV-2607-21763;SF-2026-ARXIV-2607-21799;SF-2026-ARXIV-2607-21804;SF-2026-ARXIV-2607-21824;SF-2026-ARXIV-2607-21835;SF-2026-ARXIV-2607-21857;SF-2026-ARXIV-2607-21861;SF-2026-ARXIV-2607-21909;SF-2026-ARXIV-2607-21910;SF-2026-ARXIV-2607-21912;SF-2026-ARXIV-2607-21918;SF-2026-ARXIV-2607-21927;SF-2026-ARXIV-2607-21946;SF-2026-ARXIV-2607-21951;SF-2026-ARXIV-2607-21958;SF-2026-ARXIV-2607-21962;SF-2026-ARXIV-2607-21971;SF-2026-ARXIV-2607-21978;SF-2026-ARXIV-2607-21985;SF-2026-ARXIV-2607-22000;SF-2026-ARXIV-2607-22002;SF-2026-ARXIV-2607-22013;SF-2026-ARXIV-2607-22014;SF-2026-ARXIV-2607-22022;SF-2026-ARXIV-2607-22024;SF-2026-ARXIV-2607-22034;SF-2026-ARXIV-2607-22038;SF-2026-ARXIV-2607-22039;SF-2026-ARXIV-2607-22043;SF-2026-ARXIV-2607-22083;SF-2026-ARXIV-2607-22091;SF-2026-ARXIV-2607-22098;SF-2026-ARXIV-2607-22119;SF-2026-ARXIV-2607-22157;SF-2026-ARXIV-2607-22165;SF-2026-ARXIV-2607-22182;SF-2026-ARXIV-2607-22186;SF-2026-ARXIV-2607-22188;SF-2026-ARXIV-2607-22199;SF-2026-ARXIV-2607-22225;SF-2026-ARXIV-2607-22242;SF-2026-ARXIV-2607-22251;SF-2026-ARXIV-2607-22305;SF-2026-ARXIV-2607-22319;SF-2026-ARXIV-2607-22334;SF-2026-ARXIV-2607-22367;SF-2026-ARXIV-2607-22368;SF-2026-ARXIV-2607-22385;SF-2026-ARXIV-2607-22389;SF-2026-ARXIV-2607-22392;SF-2026-ARXIV-2607-22393;SF-2026-ARXIV-2607-22400;SF-2026-ARXIV-2607-22430;SF-2026-ARXIV-2607-22432;SF-2026-ARXIV-2607-22445;SF-2026-ARXIV-2607-22448;SF-2026-ARXIV-2607-22465;SF-2026-ARXIV-2607-22489;SF-2026-ARXIV-2607-22511;SF-2026-ARXIV-2607-22520;SF-2026-ARXIV-2607-22529;SF-2026-ARXIV-2607-22530;SF-2026-ARXIV-2607-22535 | all registered category pages; cross-category dedup complete | 2026-07-27T09:00:00+08:00 | sha256:58a0920341e090f827435419c4b2380954f8795d81208ddc9a5d8b334b135eec | — |
<!-- coverage:SRC-ARXIV:20260727:end -->

### Coverage Limitations

- DataCite 只辅助 owner reconciliation；技术结论全部回到 official exact arXiv v1。
- author-side receipt 已闭合，独立 false-positive / false-negative audit 尚未签收。

## 2. Candidate Ledger

<!-- validator:candidate-ledger-v2.1 -->
| Source Family ID | Primary Identifier | Event Identity | Owner Week | First-public Date | Supporting Source IDs | Design Delta | System Reach | Durability | Total | Candidate State | Review Status | Access Status | Review Override | Review Ref | Owner Report Ref | Prior Review Ref | Reconciliation | Stable Node ID | Books Disposition | Books Review Ref | Benchmark Claim |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2607-21596 | arXiv:2607.21596v1 | paper-v1:2607.21596 | 2026-W31 | 2026-07-27 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-21596 | self | — | new_in_window | AGENT-WORKFLOW | Not Assessed | — | no |
| SF-2026-ARXIV-2607-21599 | arXiv:2607.21599v1 | paper-v1:2607.21599 | 2026-W31 | 2026-07-27 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-21599 | self | — | new_in_window | INFER-KV-CACHE | Not Assessed | — | no |
| SF-2026-ARXIV-2607-21600 | arXiv:2607.21600v1 | paper-v1:2607.21600 | 2026-W31 | 2026-07-27 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-21600 | self | — | new_in_window | PLATFORM-SECURITY | Not Assessed | — | no |
| SF-2026-ARXIV-2607-21602 | arXiv:2607.21602v1 | paper-v1:2607.21602 | 2026-W31 | 2026-07-27 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-21602 | self | — | new_in_window | INFER-SCHEDULING | Not Assessed | — | no |
| SF-2026-ARXIV-2607-21604 | arXiv:2607.21604v1 | paper-v1:2607.21604 | 2026-W31 | 2026-07-27 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-21604 | self | — | new_in_window | AGENT-MEMORY | Not Assessed | — | no |
| SF-2026-ARXIV-2607-21606 | arXiv:2607.21606v1 | paper-v1:2607.21606 | 2026-W31 | 2026-07-27 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-21606 | self | — | new_in_window | MULTIMODAL-GENERATIVE-PARADIGMS | Not Assessed | — | no |
| SF-2026-ARXIV-2607-21609 | arXiv:2607.21609v1 | paper-v1:2607.21609 | 2026-W31 | 2026-07-27 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-21609 | self | — | new_in_window | AGENT-WORKFLOW | Not Assessed | — | no |
| SF-2026-ARXIV-2607-21610 | arXiv:2607.21610v1 | paper-v1:2607.21610 | 2026-W31 | 2026-07-27 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-21610 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-21612 | arXiv:2607.21612v1 | paper-v1:2607.21612 | 2026-W31 | 2026-07-27 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-21612 | self | — | new_in_window | TRAIN-LORA | Not Assessed | — | no |
| SF-2026-ARXIV-2607-21613 | arXiv:2607.21613v1 | paper-v1:2607.21613 | 2026-W31 | 2026-07-27 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-21613 | self | — | new_in_window | WORLDVIEW-LLM-INTELLIGENCE | Not Assessed | — | no |
| SF-2026-ARXIV-2607-21616 | arXiv:2607.21616v1 | paper-v1:2607.21616 | 2026-W31 | 2026-07-27 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-21616 | self | — | new_in_window | AGENT-CONTEXT | Not Assessed | — | no |
| SF-2026-ARXIV-2607-21617 | arXiv:2607.21617v1 | paper-v1:2607.21617 | 2026-W31 | 2026-07-27 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-21617 | self | — | new_in_window | MULTIMODAL-REPRESENTATION | Not Assessed | — | no |
| SF-2026-ARXIV-2607-21619 | arXiv:2607.21619v1 | paper-v1:2607.21619 | 2026-W31 | 2026-07-27 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-21619 | self | — | new_in_window | PLATFORM-SECURITY | Not Assessed | — | no |
| SF-2026-ARXIV-2607-21623 | arXiv:2607.21623v1 | paper-v1:2607.21623 | 2026-W31 | 2026-07-27 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-21623 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-21624 | arXiv:2607.21624v1 | paper-v1:2607.21624 | 2026-W31 | 2026-07-27 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-21624 | self | — | new_in_window | TRAIN-LORA | Not Assessed | — | no |
| SF-2026-ARXIV-2607-21625 | arXiv:2607.21625v1 | paper-v1:2607.21625 | 2026-W31 | 2026-07-27 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-21625 | self | — | new_in_window | AGENT-RAG | Not Assessed | — | no |
| SF-2026-ARXIV-2607-21627 | arXiv:2607.21627v1 | paper-v1:2607.21627 | 2026-W31 | 2026-07-27 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-21627 | self | — | new_in_window | AGENT-PLATFORM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-21632 | arXiv:2607.21632v1 | paper-v1:2607.21632 | 2026-W31 | 2026-07-27 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-21632 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-21635 | arXiv:2607.21635v1 | paper-v1:2607.21635 | 2026-W31 | 2026-07-27 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-21635 | self | — | new_in_window | AGENT-PLATFORM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-21641 | arXiv:2607.21641v1 | paper-v1:2607.21641 | 2026-W31 | 2026-07-27 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-21641 | self | — | new_in_window | AGENT-TOOL-CALLING | Not Assessed | — | no |
| SF-2026-ARXIV-2607-21642 | arXiv:2607.21642v1 | paper-v1:2607.21642 | 2026-W31 | 2026-07-27 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-21642 | self | — | new_in_window | AGENT-TOOL-CALLING | Not Assessed | — | no |
| SF-2026-ARXIV-2607-21646 | arXiv:2607.21646v1 | paper-v1:2607.21646 | 2026-W31 | 2026-07-27 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-21646 | self | — | new_in_window | TRAIN-GRPO | Not Assessed | — | no |
| SF-2026-ARXIV-2607-21653 | arXiv:2607.21653v1 | paper-v1:2607.21653 | 2026-W31 | 2026-07-27 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-21653 | self | — | new_in_window | TRAIN-GRPO | Not Assessed | — | no |
| SF-2026-ARXIV-2607-21656 | arXiv:2607.21656v1 | paper-v1:2607.21656 | 2026-W31 | 2026-07-27 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-21656 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-21661 | arXiv:2607.21661v1 | paper-v1:2607.21661 | 2026-W31 | 2026-07-27 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-21661 | self | — | new_in_window | MULTIMODAL-EMBODIED-VLA | Not Assessed | — | no |
| SF-2026-ARXIV-2607-21670 | arXiv:2607.21670v1 | paper-v1:2607.21670 | 2026-W31 | 2026-07-27 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-21670 | self | — | new_in_window | MULTIMODAL-EMBODIED-VLA | Not Assessed | — | no |
| SF-2026-ARXIV-2607-21672 | arXiv:2607.21672v1 | paper-v1:2607.21672 | 2026-W31 | 2026-07-27 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-21672 | self | — | new_in_window | PLATFORM-COST | Not Assessed | — | no |
| SF-2026-ARXIV-2607-21674 | arXiv:2607.21674v1 | paper-v1:2607.21674 | 2026-W31 | 2026-07-27 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-21674 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-21686 | arXiv:2607.21686v1 | paper-v1:2607.21686 | 2026-W31 | 2026-07-27 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-21686 | self | — | new_in_window | MULTIMODAL-WORLD-MODELS | Not Assessed | — | no |
| SF-2026-ARXIV-2607-21722 | arXiv:2607.21722v1 | paper-v1:2607.21722 | 2026-W31 | 2026-07-27 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-21722 | self | — | new_in_window | MULTIMODAL-REPRESENTATION | Not Assessed | — | no |
| SF-2026-ARXIV-2607-21725 | arXiv:2607.21725v1 | paper-v1:2607.21725 | 2026-W31 | 2026-07-27 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-21725 | self | — | new_in_window | MULTIMODAL-EMBODIED-VLA | Not Assessed | — | no |
| SF-2026-ARXIV-2607-21731 | arXiv:2607.21731v1 | paper-v1:2607.21731 | 2026-W31 | 2026-07-27 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-21731 | self | — | new_in_window | INFER-TENSORRT-LLM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-21735 | arXiv:2607.21735v1 | paper-v1:2607.21735 | 2026-W31 | 2026-07-27 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-21735 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-21738 | arXiv:2607.21738v1 | paper-v1:2607.21738 | 2026-W31 | 2026-07-27 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-21738 | self | — | new_in_window | PLATFORM-MODEL-REGISTRY | Not Assessed | — | no |
| SF-2026-ARXIV-2607-21746 | arXiv:2607.21746v1 | paper-v1:2607.21746 | 2026-W31 | 2026-07-27 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-21746 | self | — | new_in_window | PLATFORM-FOUNDATIONS | Not Assessed | — | no |
| SF-2026-ARXIV-2607-21752 | arXiv:2607.21752v1 | paper-v1:2607.21752 | 2026-W31 | 2026-07-27 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-21752 | self | — | new_in_window | MODEL-LONG-CONTEXT | Not Assessed | — | no |
| SF-2026-ARXIV-2607-21756 | arXiv:2607.21756v1 | paper-v1:2607.21756 | 2026-W31 | 2026-07-27 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-21756 | self | — | new_in_window | AGENT-PROMPT | Not Assessed | — | no |
| SF-2026-ARXIV-2607-21763 | arXiv:2607.21763v1 | paper-v1:2607.21763 | 2026-W31 | 2026-07-27 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-21763 | self | — | new_in_window | PLATFORM-SECURITY | Not Assessed | — | no |
| SF-2026-ARXIV-2607-21799 | arXiv:2607.21799v1 | paper-v1:2607.21799 | 2026-W31 | 2026-07-27 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-21799 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-21804 | arXiv:2607.21804v1 | paper-v1:2607.21804 | 2026-W31 | 2026-07-27 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-21804 | self | — | new_in_window | INFER-SPECULATIVE-DECODING | Not Assessed | — | no |
| SF-2026-ARXIV-2607-21824 | arXiv:2607.21824v1 | paper-v1:2607.21824 | 2026-W31 | 2026-07-27 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-21824 | self | — | new_in_window | AGENT-PLATFORM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-21835 | arXiv:2607.21835v1 | paper-v1:2607.21835 | 2026-W31 | 2026-07-27 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-21835 | self | — | new_in_window | AGENT-TOOL-CALLING | Not Assessed | — | no |
| SF-2026-ARXIV-2607-21857 | arXiv:2607.21857v1 | paper-v1:2607.21857 | 2026-W31 | 2026-07-27 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-21857 | self | — | new_in_window | MULTIMODAL-REPRESENTATION | Not Assessed | — | no |
| SF-2026-ARXIV-2607-21861 | arXiv:2607.21861v1 | paper-v1:2607.21861 | 2026-W31 | 2026-07-27 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-21861 | self | — | new_in_window | TRAIN-LORA | Not Assessed | — | no |
| SF-2026-ARXIV-2607-21909 | arXiv:2607.21909v1 | paper-v1:2607.21909 | 2026-W31 | 2026-07-27 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-21909 | self | — | new_in_window | AGENT-WORKFLOW | Not Assessed | — | no |
| SF-2026-ARXIV-2607-21910 | arXiv:2607.21910v1 | paper-v1:2607.21910 | 2026-W31 | 2026-07-27 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-21910 | self | — | new_in_window | MULTIMODAL-WORLD-MODELS | Not Assessed | — | no |
| SF-2026-ARXIV-2607-21912 | arXiv:2607.21912v1 | paper-v1:2607.21912 | 2026-W31 | 2026-07-27 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-21912 | self | — | new_in_window | AGENT-MULTI-AGENT | Not Assessed | — | no |
| SF-2026-ARXIV-2607-21918 | arXiv:2607.21918v1 | paper-v1:2607.21918 | 2026-W31 | 2026-07-27 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-21918 | self | — | new_in_window | MULTIMODAL-WORLD-MODELS | Not Assessed | — | no |
| SF-2026-ARXIV-2607-21927 | arXiv:2607.21927v1 | paper-v1:2607.21927 | 2026-W31 | 2026-07-27 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-21927 | self | — | new_in_window | MODEL-LONG-CONTEXT | Not Assessed | — | no |
| SF-2026-ARXIV-2607-21946 | arXiv:2607.21946v1 | paper-v1:2607.21946 | 2026-W31 | 2026-07-27 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-21946 | self | — | new_in_window | AGENT-MULTI-AGENT | Not Assessed | — | no |
| SF-2026-ARXIV-2607-21951 | arXiv:2607.21951v1 | paper-v1:2607.21951 | 2026-W31 | 2026-07-27 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-21951 | self | — | new_in_window | AGENT-RAG | Not Assessed | — | no |
| SF-2026-ARXIV-2607-21958 | arXiv:2607.21958v1 | paper-v1:2607.21958 | 2026-W31 | 2026-07-27 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-21958 | self | — | new_in_window | PLATFORM-SECURITY | Not Assessed | — | no |
| SF-2026-ARXIV-2607-21962 | arXiv:2607.21962v1 | paper-v1:2607.21962 | 2026-W31 | 2026-07-27 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-21962 | self | — | new_in_window | AGENT-MEMORY | Not Assessed | — | no |
| SF-2026-ARXIV-2607-21971 | arXiv:2607.21971v1 | paper-v1:2607.21971 | 2026-W31 | 2026-07-27 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-21971 | self | — | new_in_window | AGENT-REFLECTION | Not Assessed | — | no |
| SF-2026-ARXIV-2607-21978 | arXiv:2607.21978v1 | paper-v1:2607.21978 | 2026-W31 | 2026-07-27 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-21978 | self | — | new_in_window | TRAIN-LORA | Not Assessed | — | no |
| SF-2026-ARXIV-2607-21985 | arXiv:2607.21985v1 | paper-v1:2607.21985 | 2026-W31 | 2026-07-27 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-21985 | self | — | new_in_window | INFER-DECODE | Not Assessed | — | no |
| SF-2026-ARXIV-2607-22000 | arXiv:2607.22000v1 | paper-v1:2607.22000 | 2026-W31 | 2026-07-27 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-22000 | self | — | new_in_window | MULTIMODAL-WORLD-MODELS | Not Assessed | — | no |
| SF-2026-ARXIV-2607-22002 | arXiv:2607.22002v1 | paper-v1:2607.22002 | 2026-W31 | 2026-07-27 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-22002 | self | — | new_in_window | TRAIN-GRPO | Not Assessed | — | no |
| SF-2026-ARXIV-2607-22013 | arXiv:2607.22013v1 | paper-v1:2607.22013 | 2026-W31 | 2026-07-27 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-22013 | self | — | new_in_window | MULTIMODAL-REPRESENTATION | Not Assessed | — | no |
| SF-2026-ARXIV-2607-22014 | arXiv:2607.22014v1 | paper-v1:2607.22014 | 2026-W31 | 2026-07-27 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-22014 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-22022 | arXiv:2607.22022v1 | paper-v1:2607.22022 | 2026-W31 | 2026-07-27 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-22022 | self | — | new_in_window | INFER-TENSORRT-LLM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-22024 | arXiv:2607.22024v1 | paper-v1:2607.22024 | 2026-W31 | 2026-07-27 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-22024 | self | — | new_in_window | AGENT-PLATFORM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-22034 | arXiv:2607.22034v1 | paper-v1:2607.22034 | 2026-W31 | 2026-07-27 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-22034 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-22038 | arXiv:2607.22038v1 | paper-v1:2607.22038 | 2026-W31 | 2026-07-27 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-22038 | self | — | new_in_window | INFER-TENSORRT-LLM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-22039 | arXiv:2607.22039v1 | paper-v1:2607.22039 | 2026-W31 | 2026-07-27 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-22039 | self | — | new_in_window | TRAIN-GRPO | Not Assessed | — | no |
| SF-2026-ARXIV-2607-22043 | arXiv:2607.22043v1 | paper-v1:2607.22043 | 2026-W31 | 2026-07-27 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-22043 | self | — | new_in_window | MULTIMODAL-REPRESENTATION | Not Assessed | — | no |
| SF-2026-ARXIV-2607-22083 | arXiv:2607.22083v1 | paper-v1:2607.22083 | 2026-W31 | 2026-07-27 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-22083 | self | — | new_in_window | AGENT-PLATFORM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-22091 | arXiv:2607.22091v1 | paper-v1:2607.22091 | 2026-W31 | 2026-07-27 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-22091 | self | — | new_in_window | MULTIMODAL-GENERATIVE-PARADIGMS | Not Assessed | — | no |
| SF-2026-ARXIV-2607-22098 | arXiv:2607.22098v1 | paper-v1:2607.22098 | 2026-W31 | 2026-07-27 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-22098 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-22119 | arXiv:2607.22119v1 | paper-v1:2607.22119 | 2026-W31 | 2026-07-27 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-22119 | self | — | new_in_window | AGENT-MULTI-AGENT | Not Assessed | — | no |
| SF-2026-ARXIV-2607-22157 | arXiv:2607.22157v1 | paper-v1:2607.22157 | 2026-W31 | 2026-07-27 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-22157 | self | — | new_in_window | AGENT-MEMORY | Not Assessed | — | no |
| SF-2026-ARXIV-2607-22165 | arXiv:2607.22165v1 | paper-v1:2607.22165 | 2026-W31 | 2026-07-27 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-22165 | self | — | new_in_window | AGENT-TOOL-CALLING | Not Assessed | — | no |
| SF-2026-ARXIV-2607-22182 | arXiv:2607.22182v1 | paper-v1:2607.22182 | 2026-W31 | 2026-07-27 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-22182 | self | — | new_in_window | WORLDVIEW-KNOWLEDGE-TREE | Not Assessed | — | no |
| SF-2026-ARXIV-2607-22186 | arXiv:2607.22186v1 | paper-v1:2607.22186 | 2026-W31 | 2026-07-27 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-22186 | self | — | new_in_window | TRAIN-GRPO | Not Assessed | — | no |
| SF-2026-ARXIV-2607-22188 | arXiv:2607.22188v1 | paper-v1:2607.22188 | 2026-W31 | 2026-07-27 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-22188 | self | — | new_in_window | AGENT-MULTI-AGENT | Not Assessed | — | no |
| SF-2026-ARXIV-2607-22199 | arXiv:2607.22199v1 | paper-v1:2607.22199 | 2026-W31 | 2026-07-27 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-22199 | self | — | new_in_window | MULTIMODAL-GENERATIVE-PARADIGMS | Not Assessed | — | no |
| SF-2026-ARXIV-2607-22225 | arXiv:2607.22225v1 | paper-v1:2607.22225 | 2026-W31 | 2026-07-27 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-22225 | self | — | new_in_window | MULTIMODAL-WORLD-MODELS | Not Assessed | — | no |
| SF-2026-ARXIV-2607-22242 | arXiv:2607.22242v1 | paper-v1:2607.22242 | 2026-W31 | 2026-07-27 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-22242 | self | — | new_in_window | PLATFORM-GPU-SCHEDULER | Not Assessed | — | no |
| SF-2026-ARXIV-2607-22251 | arXiv:2607.22251v1 | paper-v1:2607.22251 | 2026-W31 | 2026-07-27 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-22251 | self | — | new_in_window | TRAIN-LORA | Not Assessed | — | no |
| SF-2026-ARXIV-2607-22305 | arXiv:2607.22305v1 | paper-v1:2607.22305 | 2026-W31 | 2026-07-27 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-22305 | self | — | new_in_window | TRAIN-RLHF | Not Assessed | — | no |
| SF-2026-ARXIV-2607-22319 | arXiv:2607.22319v1 | paper-v1:2607.22319 | 2026-W31 | 2026-07-27 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-22319 | self | — | new_in_window | AGENT-RAG | Not Assessed | — | no |
| SF-2026-ARXIV-2607-22334 | arXiv:2607.22334v1 | paper-v1:2607.22334 | 2026-W31 | 2026-07-27 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-22334 | self | — | new_in_window | TRAIN-SFT | Not Assessed | — | no |
| SF-2026-ARXIV-2607-22367 | arXiv:2607.22367v1 | paper-v1:2607.22367 | 2026-W31 | 2026-07-27 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-22367 | self | — | new_in_window | MODEL-TRANSFORMER-LAYER | Not Assessed | — | no |
| SF-2026-ARXIV-2607-22368 | arXiv:2607.22368v1 | paper-v1:2607.22368 | 2026-W31 | 2026-07-27 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-22368 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-22385 | arXiv:2607.22385v1 | paper-v1:2607.22385 | 2026-W31 | 2026-07-27 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-22385 | self | — | new_in_window | AGENT-REFLECTION | Not Assessed | — | no |
| SF-2026-ARXIV-2607-22389 | arXiv:2607.22389v1 | paper-v1:2607.22389 | 2026-W31 | 2026-07-27 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-22389 | self | — | new_in_window | INFER-KV-CACHE | Not Assessed | — | no |
| SF-2026-ARXIV-2607-22392 | arXiv:2607.22392v1 | paper-v1:2607.22392 | 2026-W31 | 2026-07-27 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-22392 | self | — | new_in_window | AGENT-CONTEXT | Not Assessed | — | no |
| SF-2026-ARXIV-2607-22393 | arXiv:2607.22393v1 | paper-v1:2607.22393 | 2026-W31 | 2026-07-27 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-22393 | self | — | new_in_window | MULTIMODAL-EMBODIED-VLA | Not Assessed | — | no |
| SF-2026-ARXIV-2607-22400 | arXiv:2607.22400v1 | paper-v1:2607.22400 | 2026-W31 | 2026-07-27 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-22400 | self | — | new_in_window | PLATFORM-GPU-SCHEDULER | Not Assessed | — | no |
| SF-2026-ARXIV-2607-22430 | arXiv:2607.22430v1 | paper-v1:2607.22430 | 2026-W31 | 2026-07-27 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-22430 | self | — | new_in_window | MULTIMODAL-WORLD-MODELS | Not Assessed | — | no |
| SF-2026-ARXIV-2607-22432 | arXiv:2607.22432v1 | paper-v1:2607.22432 | 2026-W31 | 2026-07-27 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-22432 | self | — | new_in_window | INFER-TENSORRT-LLM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-22445 | arXiv:2607.22445v1 | paper-v1:2607.22445 | 2026-W31 | 2026-07-27 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-22445 | self | — | new_in_window | AGENT-PLATFORM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-22448 | arXiv:2607.22448v1 | paper-v1:2607.22448 | 2026-W31 | 2026-07-27 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-22448 | self | — | new_in_window | AGENT-MULTI-AGENT | Not Assessed | — | no |
| SF-2026-ARXIV-2607-22465 | arXiv:2607.22465v1 | paper-v1:2607.22465 | 2026-W31 | 2026-07-27 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-22465 | self | — | new_in_window | INFER-SCHEDULING | Not Assessed | — | no |
| SF-2026-ARXIV-2607-22489 | arXiv:2607.22489v1 | paper-v1:2607.22489 | 2026-W31 | 2026-07-27 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-22489 | self | — | new_in_window | TRAIN-LORA | Not Assessed | — | no |
| SF-2026-ARXIV-2607-22511 | arXiv:2607.22511v1 | paper-v1:2607.22511 | 2026-W31 | 2026-07-27 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-22511 | self | — | new_in_window | AGENT-REFLECTION | Not Assessed | — | no |
| SF-2026-ARXIV-2607-22520 | arXiv:2607.22520v1 | paper-v1:2607.22520 | 2026-W31 | 2026-07-27 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-22520 | self | — | new_in_window | AGENT-PLATFORM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-22529 | arXiv:2607.22529v1 | paper-v1:2607.22529 | 2026-W31 | 2026-07-27 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-22529 | self | — | new_in_window | AGENT-REFLECTION | Not Assessed | — | no |
| SF-2026-ARXIV-2607-22530 | arXiv:2607.22530v1 | paper-v1:2607.22530 | 2026-W31 | 2026-07-27 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-22530 | self | — | new_in_window | MULTIMODAL-WORLD-MODELS | Not Assessed | — | no |
| SF-2026-ARXIV-2607-22535 | arXiv:2607.22535v1 | paper-v1:2607.22535 | 2026-W31 | 2026-07-27 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-22535 | self | — | new_in_window | MULTIMODAL-WORLD-MODELS | Not Assessed | — | no |

## 3. Review Completion Receipt

<!-- validator:review-completion-v1 -->
| Source Family ID | Review Provenance ID | Review Route | Primary Evidence Version | Reviewed Evidence Versions | Method / Identity Locators | Evaluation Locators | Limitations / Counterevidence Locators | Artifact Locators | Claim Boundary Ref | Completion Result |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2607-21596 | RP-834e9e93f0c0747f | deep | arXiv:2607.21596v1 | SRC-ARXIV@arXiv:2607.21596v1 | https://arxiv.org/html/2607.21596v1#A2 — Appendix B Framework Thresholds and Configuration Constants; https://arxiv.org/html/2607.21596v1#S3 — 3 Method | https://arxiv.org/html/2607.21596v1#S4 — 4 Experiments; https://arxiv.org/html/2607.21596v1#S4.SS1 — 4.1 Experimental setup | https://arxiv.org/html/2607.21596v1#S5 — 5 Discussion; https://arxiv.org/html/2607.21596v1#S6 — 6 Conclusion | Exact v1 links https://github.com/DEFENSE-SEU/FlowEvo, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-21596 | complete |
| SF-2026-ARXIV-2607-21599 | RP-80701e6d1705cc38 | deep | arXiv:2607.21599v1 | SRC-ARXIV@arXiv:2607.21599v1 | https://arxiv.org/html/2607.21599v1#S2 — 2. Methods: Decoupled Attention Fusion | https://arxiv.org/html/2607.21599v1#S3 — 3. Preliminary Results | https://arxiv.org/html/2607.21599v1#S1 — 1. Introduction; https://arxiv.org/html/2607.21599v1#S2 — 2. Methods: Decoupled Attention Fusion | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-21599 | complete |
| SF-2026-ARXIV-2607-21600 | RP-96e7f2cbd733f851 | deep | arXiv:2607.21600v1 | SRC-ARXIV@arXiv:2607.21600v1 | https://arxiv.org/html/2607.21600v1#S3 — 3 Methodology; https://arxiv.org/html/2607.21600v1#A1.SS2 — A.2 Baseline Implementation Details | https://arxiv.org/html/2607.21600v1#S4.SS3 — 4.3 Evaluation Benchmarks; https://arxiv.org/html/2607.21600v1#A1.SS1 — A.1 Detailed Experimental Configuration | https://arxiv.org/html/2607.21600v1#S6 — 6 Conclusion and Future Work; https://arxiv.org/html/2607.21600v1#S4.SS4 — 4.4 Threat Configuration | Exact v1 links https://github.com/Jeybird248/FlowGuard, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-21600 | complete |
| SF-2026-ARXIV-2607-21602 | RP-27ac446ec30a0ea9 | deep | arXiv:2607.21602v1 | SRC-ARXIV@arXiv:2607.21602v1 | https://arxiv.org/html/2607.21602v1#S3 — 3. System Design; https://arxiv.org/html/2607.21602v1#S4 — 4. Experimental Design | https://arxiv.org/html/2607.21602v1#S5 — 5. Results and Analysis; https://arxiv.org/html/2607.21602v1#S4 — 4. Experimental Design | https://arxiv.org/html/2607.21602v1#S2.SS3 — 2.3. Limitations of Static Latency Predictors; https://arxiv.org/html/2607.21602v1#S5.SS7 — 5.7. Discussion | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-21602 | complete |
| SF-2026-ARXIV-2607-21604 | RP-88f21881f3ed711c | deep | arXiv:2607.21604v1 | SRC-ARXIV@arXiv:2607.21604v1 | https://arxiv.org/html/2607.21604v1#S3 — 3 Proposed Approach; https://arxiv.org/html/2607.21604v1#A3 — Appendix C Empirical Validation of the Modeling Assumptions | https://arxiv.org/html/2607.21604v1#A1 — Appendix A Extended Experimental Results; https://arxiv.org/html/2607.21604v1#A1.SS1 — A.1 Extended Experimental Set-Up and Reproducibility | https://arxiv.org/html/2607.21604v1#A5 — Appendix E Limitations and Future Work; https://arxiv.org/html/2607.21604v1#A1.SS2 — A.2 Extended AMA-Bench Discussion | Exact v1 links https://huggingface.co/mistralai/Mistral-7B-Instruct-v0.3, https://github.com/agiresearch/a-mem, https://github.com/EverM0re/LiCoMemory; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-21604 | complete |
| SF-2026-ARXIV-2607-21606 | RP-0ba6dd7a5d6e5d63 | deep | arXiv:2607.21606v1 | SRC-ARXIV@arXiv:2607.21606v1 | https://arxiv.org/html/2607.21606v1#S3 — 3 Method; https://arxiv.org/html/2607.21606v1#A5 — Appendix E More Implementation Details | https://arxiv.org/html/2607.21606v1#A6 — Appendix F More Qualitative Results; https://arxiv.org/html/2607.21606v1#S4 — 4 Experiments | https://arxiv.org/html/2607.21606v1#S6 — 6 Conclusion | Exact v1 links https://aclanthology.org/2020.acl-demos.14/, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-21606 | complete |
| SF-2026-ARXIV-2607-21609 | RP-dfbb2e196dc827d7 | deep | arXiv:2607.21609v1 | SRC-ARXIV@arXiv:2607.21609v1 | https://arxiv.org/html/2607.21609v1#S2 — 2 Methodology; https://arxiv.org/html/2607.21609v1#A3 — Appendix C Algorithmic Details of HierFlow | https://arxiv.org/html/2607.21609v1#A4.SS3 — D.3 Detailed Ablation Analysis; https://arxiv.org/html/2607.21609v1#A4 — Appendix D Additional Experimental Details | https://arxiv.org/html/2607.21609v1#A2 — Appendix B Proofs and Additional Theoretical Discussions; https://arxiv.org/html/2607.21609v1#S4 — 4 Conclusion | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-21609 | complete |
| SF-2026-ARXIV-2607-21610 | RP-dc0fc8a283493cae | standard | arXiv:2607.21610v1 | SRC-ARXIV@arXiv:2607.21610v1 | https://arxiv.org/html/2607.21610v1#S4 — 4 SCION Method; https://arxiv.org/html/2607.21610v1#A6.SS6 — F.6 SCION-RL: Replacing the Schema Engineer with a Trained Compact Model | https://arxiv.org/html/2607.21610v1#S5.SS7 — 5.7 Results and Analysis; https://arxiv.org/html/2607.21610v1#A3 — Appendix C Additional Details of the SCOPE Benchmark | https://arxiv.org/html/2607.21610v1#A7.SS4 — G.4 Failure Case: Polysemy and Conservative Rejection; https://arxiv.org/html/2607.21610v1#S6 — 6 Conclusion | Exact v1 links https://github.com/wandugu/paper_scion, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-21610 | complete |
| SF-2026-ARXIV-2607-21612 | RP-07d5340d9b425dcc | deep | arXiv:2607.21612v1 | SRC-ARXIV@arXiv:2607.21612v1 | https://arxiv.org/html/2607.21612v1#S2 — 2 Method | https://arxiv.org/html/2607.21612v1#S2.SS4 — 2.4 Evaluation Conditions; https://arxiv.org/html/2607.21612v1#S2.SS5 — 2.5 Evaluation Protocol | https://arxiv.org/html/2607.21612v1#S3.SS1 — 3.1 Behavioral Failure Across Ranks; https://arxiv.org/html/2607.21612v1#S4 — 4 Discussion | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-21612 | complete |
| SF-2026-ARXIV-2607-21613 | RP-f0d4cedfb874ac6a | standard | arXiv:2607.21613v1 | SRC-ARXIV@arXiv:2607.21613v1 | https://arxiv.org/html/2607.21613v1#S3 — 3 Methodology; https://arxiv.org/html/2607.21613v1#A1 — Appendix A Prompt, Models and Datasets | https://arxiv.org/html/2607.21613v1#A3 — Appendix C Supplementary Results for Finding 1; https://arxiv.org/html/2607.21613v1#A4 — Appendix D Supplementary Results for Finding 2 | https://arxiv.org/html/2607.21613v1#S5 — 5 Discussion; https://arxiv.org/html/2607.21613v1#S6 — 6 Limitations | Exact v1 links https://github.com/Mystic-Slice/hard-decision-layer, https://huggingface.co/ibm-granite/granite-3.3-2b-instruct, https://huggingface.co/mistralai/Mistral-7B-Instruct-v0.3; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-21613 | complete |
| SF-2026-ARXIV-2607-21616 | RP-58cc003e4b7db33d | standard | arXiv:2607.21616v1 | SRC-ARXIV@arXiv:2607.21616v1 | https://arxiv.org/html/2607.21616v1#A4.SS1 — D.1 Motivation and Task Design; https://arxiv.org/html/2607.21616v1#S3 — 3 Method | https://arxiv.org/html/2607.21616v1#A6 — Appendix F Sensitivity Analysis of the Context Anxiety Detector; https://arxiv.org/html/2607.21616v1#S4 — 4 Results | https://arxiv.org/html/2607.21616v1#S5 — 5 Conclusion | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-21616 | complete |
| SF-2026-ARXIV-2607-21617 | RP-48c2007b77987cc0 | standard | arXiv:2607.21617v1 | SRC-ARXIV@arXiv:2607.21617v1 | https://arxiv.org/html/2607.21617v1#A2 — Appendix B Models; https://arxiv.org/html/2607.21617v1#A6.SS1 — F.1 Effect of model size. | https://arxiv.org/html/2607.21617v1#S4 — 4 Experimental Results; https://arxiv.org/html/2607.21617v1#A6 — Appendix F Ablation Studies | https://arxiv.org/html/2607.21617v1#A3 — Appendix C Failure Detection and Exclusion; https://arxiv.org/html/2607.21617v1#S5 — 5 Conclusion | Exact v1 links https://github.com/mindee/doctr, https://huggingface.co/blog/lightonai/lightonocr, https://github.com/arXiv/html_feedback/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-21617 | complete |
| SF-2026-ARXIV-2607-21619 | RP-b529876f9c9bea60 | standard | arXiv:2607.21619v1 | SRC-ARXIV@arXiv:2607.21619v1 | https://arxiv.org/html/2607.21619v1#S2.SS1 — 2.1 Multimodal Large Language Models (MLLMs) | https://arxiv.org/html/2607.21619v1#S5 — 5 Experiments; https://arxiv.org/html/2607.21619v1#S5.SS1 — 5.1 Experimental Setup | https://arxiv.org/html/2607.21619v1#S6 — 6 Conclusion | Exact v1 links https://github.com/bingjunluo/ASO, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-21619 | complete |
| SF-2026-ARXIV-2607-21623 | RP-72cde4773da719cd | deep | arXiv:2607.21623v1 | SRC-ARXIV@arXiv:2607.21623v1 | https://arxiv.org/html/2607.21623v1#S3 — 3 Methodology; https://arxiv.org/html/2607.21623v1#S3.SS1 — 3.1 Architecture | https://arxiv.org/html/2607.21623v1#S3.SS2 — 3.2 Evaluation Services; https://arxiv.org/html/2607.21623v1#S3.SS4 — 3.4 Experimental Design | https://arxiv.org/html/2607.21623v1#S5 — 5 Discussion; https://arxiv.org/html/2607.21623v1#S6 — 6 Conclusion | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-21623 | complete |
| SF-2026-ARXIV-2607-21624 | RP-b38dcabbe3a3c864 | deep | arXiv:2607.21624v1 | SRC-ARXIV@arXiv:2607.21624v1 | https://arxiv.org/html/2607.21624v1#S4 — 4. Design of FBLayout; https://arxiv.org/html/2607.21624v1#S5.SS5 — 5.5. System Overhead Analysis | https://arxiv.org/html/2607.21624v1#S3 — 3. Problem Formulation and Analysis; https://arxiv.org/html/2607.21624v1#S5 — 5. Evaluation | https://arxiv.org/html/2607.21624v1#S2.SS3 — 2.3. Limitations of Existing Solutions.; https://arxiv.org/html/2607.21624v1#S7 — 7. Discussion | Exact v1 links https://github.com/alibaba/MNN/blob/2.3.0/source/core/BufferAllocator.cpp, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-21624 | complete |
| SF-2026-ARXIV-2607-21625 | RP-cc5e43ef15ab505e | standard | arXiv:2607.21625v1 | SRC-ARXIV@arXiv:2607.21625v1 | https://arxiv.org/html/2607.21625v1#S4 — 4 Method; https://arxiv.org/html/2607.21625v1#S4.SS2 — 4.2 Stage 2: Latent Growth Curve Modeling | https://arxiv.org/html/2607.21625v1#S5 — 5 Experiments | https://arxiv.org/html/2607.21625v1#S6 — 6 Discussion | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-21625 | complete |
| SF-2026-ARXIV-2607-21627 | RP-96b3699100e3e480 | standard | arXiv:2607.21627v1 | SRC-ARXIV@arXiv:2607.21627v1 | https://arxiv.org/html/2607.21627v1#S1 — 1 Introduction; https://arxiv.org/html/2607.21627v1#S2 — 2 Related Work | https://arxiv.org/html/2607.21627v1#S4 — 4 Experiments; https://arxiv.org/html/2607.21627v1#S4.SS1 — 4.1 Experimental Setup | https://arxiv.org/html/2607.21627v1#S6 — 6 Limitations and Future Work; https://arxiv.org/html/2607.21627v1#S4.SS5 — 4.5 Discussion: Why Prevent Role Drift? | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-21627 | complete |
| SF-2026-ARXIV-2607-21632 | RP-aee76ff5a7c85e22 | standard | arXiv:2607.21632v1 | SRC-ARXIV@arXiv:2607.21632v1 | https://arxiv.org/html/2607.21632v1#S2.SS1 — 2.1 LLM-as-a-Judge Frameworks; https://arxiv.org/html/2607.21632v1#S2.SS2 — 2.2 Consensus-Based and Independent Aggregation Approaches. | https://arxiv.org/html/2607.21632v1#S2.SS3 — 2.3 Multi-Agent and Consensus-Based Evaluation; https://arxiv.org/html/2607.21632v1#S2.SS4 — 2.4 Reliability, Calibration, and Meta-Evaluation of Judges. | https://arxiv.org/html/2607.21632v1#S5 — 5 Conclusion | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-21632 | complete |
| SF-2026-ARXIV-2607-21635 | RP-3b042297daf19284 | standard | arXiv:2607.21635v1 | SRC-ARXIV@arXiv:2607.21635v1 | https://arxiv.org/html/2607.21635v1#S5 — 5. Metrics and Minimal Benchmark Design | https://arxiv.org/html/2607.21635v1#S4 — 4. Gap Analysis; https://arxiv.org/html/2607.21635v1#S5 — 5. Metrics and Minimal Benchmark Design | https://arxiv.org/html/2607.21635v1#S6 — 6. Open Challenges and Conclusion | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-21635 | complete |
| SF-2026-ARXIV-2607-21641 | RP-a8d2756f047946e4 | standard | arXiv:2607.21641v1 | SRC-ARXIV@arXiv:2607.21641v1 | https://arxiv.org/html/2607.21641v1#S3 — 3 Approach | https://arxiv.org/html/2607.21641v1#S4 — 4 Experiment Results; https://arxiv.org/html/2607.21641v1#S3.SS2 — 3.2 Compilation and Static Analysis | https://arxiv.org/html/2607.21641v1#S5 — 5 Future Work; https://arxiv.org/html/2607.21641v1#S6 — 6 Conclusion | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-21641 | complete |
| SF-2026-ARXIV-2607-21642 | RP-896809077e706d01 | deep | arXiv:2607.21642v1 | SRC-ARXIV@arXiv:2607.21642v1 | https://arxiv.org/html/2607.21642v1#S3 — III Methodology; https://arxiv.org/html/2607.21642v1#S2 — II Threat Model | https://arxiv.org/html/2607.21642v1#S4 — IV Experimental Setup; https://arxiv.org/html/2607.21642v1#S5 — V Results | https://arxiv.org/html/2607.21642v1#S2 — II Threat Model; https://arxiv.org/html/2607.21642v1#S6 — VI Discussion | Exact v1 links https://github.com/prisma-research/CARE, https://www.anthropic.com/product/claude-code, https://openai.com/index/introducing-codex/; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-21642 | complete |
| SF-2026-ARXIV-2607-21646 | RP-a34c06f07242d064 | standard | arXiv:2607.21646v1 | SRC-ARXIV@arXiv:2607.21646v1 | https://arxiv.org/html/2607.21646v1#S4 — 4 Method; https://arxiv.org/html/2607.21646v1#A2 — Appendix B Implementation Details | https://arxiv.org/html/2607.21646v1#A3 — Appendix C Additional Experimental and Calibration Details; https://arxiv.org/html/2607.21646v1#S5 — 5 Experiments | https://arxiv.org/html/2607.21646v1#S6 — 6 Conclusion | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-21646 | complete |
| SF-2026-ARXIV-2607-21653 | RP-fc637524eebfe367 | deep | arXiv:2607.21653v1 | SRC-ARXIV@arXiv:2607.21653v1 | https://arxiv.org/html/2607.21653v1#S2 — 2 Design Principles; https://arxiv.org/html/2607.21653v1#S3 — 3 The System: Four Concepts, One Loop | https://arxiv.org/html/2607.21653v1#S4 — 4 Evaluation: Does Leanness Cost Throughput? | https://arxiv.org/html/2607.21653v1#S6 — 6 Future Work; https://arxiv.org/html/2607.21653v1#S7 — 7 Conclusion | Exact v1 links https://github.com/NVIDIA-NeMo/labs-molt, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-21653 | complete |
| SF-2026-ARXIV-2607-21656 | RP-599006df3b619199 | standard | arXiv:2607.21656v1 | SRC-ARXIV@arXiv:2607.21656v1 | https://arxiv.org/html/2607.21656v1#S3 — 3. Methodology | https://arxiv.org/html/2607.21656v1#S2.SS1 — 2.1. Code generation benchmarks; https://arxiv.org/html/2607.21656v1#S4 — 4. Results | https://arxiv.org/html/2607.21656v1#S5 — 5. Discussion; https://arxiv.org/html/2607.21656v1#S5.SS5 — 5.5. Scope, Limitations, and Reproducibility | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-21656 | complete |
| SF-2026-ARXIV-2607-21661 | RP-e7a28eac812237af | standard | arXiv:2607.21661v1 | SRC-ARXIV@arXiv:2607.21661v1 | https://arxiv.org/html/2607.21661v1#S3 — III PROPOSED METHOD; https://arxiv.org/html/2607.21661v1#S2.SS1 — II-A Diffusion Models for Trajectory Generation | https://arxiv.org/html/2607.21661v1#S4 — IV EXPERIMENTS; https://arxiv.org/html/2607.21661v1#S4.SS1 — IV-A Experimental Setup | https://arxiv.org/html/2607.21661v1#S5 — V CONCLUSION | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-21661 | complete |
| SF-2026-ARXIV-2607-21670 | RP-957cc0461dacccc1 | standard | arXiv:2607.21670v1 | SRC-ARXIV@arXiv:2607.21670v1 | https://arxiv.org/html/2607.21670v1#A3 — Appendix C Experimental Protocol and Implementation; https://arxiv.org/html/2607.21670v1#A3.SS3 — C.3 Policy Implementations | https://arxiv.org/html/2607.21670v1#S6.SS4 — 6.4 Ablation and Analysis; https://arxiv.org/html/2607.21670v1#A3 — Appendix C Experimental Protocol and Implementation | https://arxiv.org/html/2607.21670v1#S8 — 8 Conclusion and Limitations | Exact v1 links https://github.com/Chaoqi-LIU/oat, https://github.com/Chaoqi-LIU/praxis-vla, https://github.com/arXiv/html_feedback/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-21670 | complete |
| SF-2026-ARXIV-2607-21672 | RP-66243d8ae6d5a75d | standard | arXiv:2607.21672v1 | SRC-ARXIV@arXiv:2607.21672v1 | https://arxiv.org/html/2607.21672v1#S3 — 3. Study Design | https://arxiv.org/html/2607.21672v1#S4 — 4. Results; https://arxiv.org/html/2607.21672v1#S5.SS3 — 5.3. Next experiment | https://arxiv.org/html/2607.21672v1#S5 — 5. Discussion; https://arxiv.org/html/2607.21672v1#S6 — 6. Threats to Validity | Exact v1 links https://github.com/ron-42/code-image-token-accounting, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-21672 | complete |
| SF-2026-ARXIV-2607-21674 | RP-16c4edc2638be874 | standard | arXiv:2607.21674v1 | SRC-ARXIV@arXiv:2607.21674v1 | https://arxiv.org/html/2607.21674v1#A1.SS1 — A.1 System Instruction (Fixed); https://arxiv.org/html/2607.21674v1#S2.SS1 — 2.1 Coding Agent Architectures and Benchmarks | https://arxiv.org/html/2607.21674v1#A1.SS5 — A.5 Experiment Runner Configuration; https://arxiv.org/html/2607.21674v1#A2 — Appendix B Task Type Moderation (Supplementary Analysis) | https://arxiv.org/html/2607.21674v1#A3 — Appendix C Supplementary Limitations; https://arxiv.org/html/2607.21674v1#S2.SS3 — 2.3 Agent Evaluation and Failure Diagnosis | Exact v1 links https://github.com/NousResearch/hermes-agent/issues/66127, https://github.com/NousResearch/hermes-agent/issues/64103, https://github.com/arXiv/html_feedback/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-21674 | complete |
| SF-2026-ARXIV-2607-21686 | RP-d6db21e33b724526 | deep | arXiv:2607.21686v1 | SRC-ARXIV@arXiv:2607.21686v1 | https://arxiv.org/html/2607.21686v1#S8 — 8 Implementation | https://arxiv.org/html/2607.21686v1#S7 — 7 Evaluation | https://arxiv.org/html/2607.21686v1#S10 — 10 Discussion, limitations, and conclusion; https://arxiv.org/html/2607.21686v1#S7.SS11 — 7.11 Threats to validity | Exact v1 links https://github.com/NVIDIA/TensorRT-LLM, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-21686 | complete |
| SF-2026-ARXIV-2607-21722 | RP-7347caf289bb0404 | standard | arXiv:2607.21722v1 | SRC-ARXIV@arXiv:2607.21722v1 | https://arxiv.org/html/2607.21722v1#A14 — Appendix N Comparison with Prior Consistency-Based Reasoning Methods; https://arxiv.org/html/2607.21722v1#S3 — 3 Method | https://arxiv.org/html/2607.21722v1#A13 — Appendix M Benchmark Characteristics Analysis; https://arxiv.org/html/2607.21722v1#A1 — Appendix A Benchmark Comparison | https://arxiv.org/html/2607.21722v1#S6 — 6 Conclusion; https://arxiv.org/html/2607.21722v1#Sx1 — Limitations | Exact v1 links https://github.com/LiqiangJing/ConVLM, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-21722 | complete |
| SF-2026-ARXIV-2607-21725 | RP-c65b03e4d7d5d583 | standard | arXiv:2607.21725v1 | SRC-ARXIV@arXiv:2607.21725v1 | https://arxiv.org/html/2607.21725v1#S1 — 1 Introduction; https://arxiv.org/html/2607.21725v1#S2 — 2 Related Work | https://arxiv.org/html/2607.21725v1#S12 — 12 Additional Results; https://arxiv.org/html/2607.21725v1#S12.SS1 — 12.1 Per-task real-robot results | https://arxiv.org/html/2607.21725v1#S10 — 10 Observation Channel and Failure Annotations; https://arxiv.org/html/2607.21725v1#S12.SS3 — 12.3 First-failure mode distribution | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-21725 | complete |
| SF-2026-ARXIV-2607-21731 | RP-e52e49783a5ff785 | deep | arXiv:2607.21731v1 | SRC-ARXIV@arXiv:2607.21731v1 | https://arxiv.org/html/2607.21731v1#S3.SS3 — III-C Architecture Design in RED-PIM; https://arxiv.org/html/2607.21731v1#S2.SS2 — II-B Processing In/Near Memory Architectures | https://arxiv.org/html/2607.21731v1#S4 — IV Evaluation Methodology and Results; https://arxiv.org/html/2607.21731v1#S4.SS2 — IV-B Experimental Setup | https://arxiv.org/html/2607.21731v1#S6 — VI Conclusion | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-21731 | complete |
| SF-2026-ARXIV-2607-21735 | RP-16c9075c2ebb1d7a | standard | arXiv:2607.21735v1 | SRC-ARXIV@arXiv:2607.21735v1 | https://arxiv.org/html/2607.21735v1#Sx1 — Methods | https://arxiv.org/html/2607.21735v1#S4.SS1 — 4.1 The benchmark null result, made precise; https://arxiv.org/html/2607.21735v1#S3 — 3 What an evaluation must establish | https://arxiv.org/html/2607.21735v1#S7 — 7 Limitations; https://arxiv.org/html/2607.21735v1#S8 — 8 Discussion | Exact v1 links https://github.com/hackwither/ai-redteam-evidential-limits, https://github.com/llm-attacks/llm-attacks, https://github.com/centerforaisafety/HarmBench; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-21735 | complete |
| SF-2026-ARXIV-2607-21738 | RP-24edafab91d68461 | standard | arXiv:2607.21738v1 | SRC-ARXIV@arXiv:2607.21738v1 | https://arxiv.org/html/2607.21738v1#S3 — 3 Methodology; https://arxiv.org/html/2607.21738v1#S3.SS1 — 3.1 Survey Design and Pilot | https://arxiv.org/html/2607.21738v1#S3.SS4 — 3.4 Data Analysis; https://arxiv.org/html/2607.21738v1#S4 — 4 Results | https://arxiv.org/html/2607.21738v1#S4.SS3 — 4.3 : What practical strategies do producers and consumers use to understand and trace model lineage across the AI supply chain, and what limitations or challenges do these strategies exhibit?; https://arxiv.org/html/2607.21738v1#S5 — 5 Discussion and Implications | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-21738 | complete |
| SF-2026-ARXIV-2607-21746 | RP-e3ff56e039a5b31b | standard | arXiv:2607.21746v1 | SRC-ARXIV@arXiv:2607.21746v1 | https://arxiv.org/html/2607.21746v1#S3.SS2 — 3.2 Framework Architecture; https://arxiv.org/html/2607.21746v1#S2 — 2 Storage Systems for AI Research Workflows | https://arxiv.org/html/2607.21746v1#S3 — 3 PRISM: A Benchmark Framework for AI research clusters; https://arxiv.org/html/2607.21746v1#S3.SS1 — 3.1 Benchmark Taxonomy | https://arxiv.org/html/2607.21746v1#S6 — 6 Conclusion | Exact v1 links https://github.com/axboe/fio, https://github.com/webdataset/webdataset, https://github.com/breuner/elbencho; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-21746 | complete |
| SF-2026-ARXIV-2607-21752 | RP-860532ac8dfa4cf8 | deep | arXiv:2607.21752v1 | SRC-ARXIV@arXiv:2607.21752v1 | https://arxiv.org/html/2607.21752v1#A1.SS1 — A.1 Model Architecture; https://arxiv.org/html/2607.21752v1#A9 — Appendix I Detailed Comparison to Learned Mask Methods | https://arxiv.org/html/2607.21752v1#S4 — 4 Experiments and Results; https://arxiv.org/html/2607.21752v1#S4.SS3 — 4.3 Experiment 2: Component ablation | https://arxiv.org/html/2607.21752v1#A11 — Appendix K Extended Discussion; https://arxiv.org/html/2607.21752v1#A12 — Appendix L Detailed Limitations | Exact v1 links https://github.com/sc782/SBM-Transformer, https://github.com/sc782/SBM-Transformer/tree/main/code, https://github.com/arXiv/html_feedback/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-21752 | complete |
| SF-2026-ARXIV-2607-21756 | RP-b22edbd3f668a85e | standard | arXiv:2607.21756v1 | SRC-ARXIV@arXiv:2607.21756v1 | https://arxiv.org/html/2607.21756v1#S3 — 3. System Implementation; https://arxiv.org/html/2607.21756v1#S2 — 2. Formal Model | https://arxiv.org/html/2607.21756v1#S4 — 4. Experiments and Results; https://arxiv.org/html/2607.21756v1#S4.SS2 — 4.2. Rule Ablation | https://arxiv.org/html/2607.21756v1#S4.SS4 — 4.4. Discussion; https://arxiv.org/html/2607.21756v1#S6 — 6. Conclusion | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-21756 | complete |
| SF-2026-ARXIV-2607-21763 | RP-357d081ddb673987 | standard | arXiv:2607.21763v1 | SRC-ARXIV@arXiv:2607.21763v1 | https://arxiv.org/html/2607.21763v1#S2 — 2 Methodology | https://arxiv.org/html/2607.21763v1#S3 — 3 Results; https://arxiv.org/html/2607.21763v1#S3.SS2 — 3.2 Prompt Ablation | https://arxiv.org/html/2607.21763v1#S4 — 4 Discussion; https://arxiv.org/html/2607.21763v1#S6 — 6 Conclusion | Exact v1 links https://github.com/mkultraWasHere, https://github.com/GangGreenTemperTatum, https://github.com/rdheekonda; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-21763 | complete |
| SF-2026-ARXIV-2607-21799 | RP-539ab4f17353e28a | standard | arXiv:2607.21799v1 | SRC-ARXIV@arXiv:2607.21799v1 | https://arxiv.org/html/2607.21799v1#A3.SS2 — C.2 Task Interface and Methodology; https://arxiv.org/html/2607.21799v1#S3.SS3 — 3.3 Legal Framework: U.S. Copyright Law | https://arxiv.org/html/2607.21799v1#S2.SS1 — 2.1 Agent Benchmarks and Agent Evaluation; https://arxiv.org/html/2607.21799v1#A4 — Appendix D Full Results Table | https://arxiv.org/html/2607.21799v1#A1 — Appendix A Limitations and Future Work; https://arxiv.org/html/2607.21799v1#S3.SS4 — 3.4 Scope and Limitations | Exact v1 links https://github.com/zackhuiiiii/Copyright-Bench, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-21799 | complete |
| SF-2026-ARXIV-2607-21804 | RP-83f39f2535aacfb6 | deep | arXiv:2607.21804v1 | SRC-ARXIV@arXiv:2607.21804v1 | https://arxiv.org/html/2607.21804v1#S3.SS2 — 3.2 Systemic Impact; https://arxiv.org/html/2607.21804v1#S4 — 4 Attack Method | https://arxiv.org/html/2607.21804v1#A1 — Appendix A Additional Evaluation Settings; https://arxiv.org/html/2607.21804v1#A2 — Appendix B Additional Attack Analysis | https://arxiv.org/html/2607.21804v1#A2.SS1 — B.1 Case Study: Standalone Draft Failure vs. Speculative Recovery; https://arxiv.org/html/2607.21804v1#S3 — 3 Threat Model and Impact | Exact v1 links https://aws.amazon.com/blogs/machine-learning/accelerating-decode-heavy-llm-inference-with-speculative-decoding-on-aws-trainium-and-vllm/, https://huggingface.co/docs/text-generation-inference/en/index, https://huggingface.co/blog/continuous_batching; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-21804 | complete |
| SF-2026-ARXIV-2607-21824 | RP-e0f49c0fbe95ba51 | deep | arXiv:2607.21824v1 | SRC-ARXIV@arXiv:2607.21824v1 | https://arxiv.org/html/2607.21824v1#S8.SS1 — 8.1 Architecture and Design Principles; https://arxiv.org/html/2607.21824v1#S3.SS1 — 3.1 System Actors and Trust Boundaries | https://arxiv.org/html/2607.21824v1#A2 — Appendix B Experimental Environment; https://arxiv.org/html/2607.21824v1#A5.SSx1 — A-AP2-4: Empty trusted_roots (Python Falsy Evaluation) | https://arxiv.org/html/2607.21824v1#S10 — 10 Discussion; https://arxiv.org/html/2607.21824v1#S10.SS2 — 10.2 Limitations | Exact v1 links https://github.com/yedidel/aip-bench-public, https://huggingface.co/datasets/anonymos-2321135/aip-bench, https://github.com/Coral-Protocol/coral-server; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-21824 | complete |
| SF-2026-ARXIV-2607-21835 | RP-af48a5320b473e42 | deep | arXiv:2607.21835v1 | SRC-ARXIV@arXiv:2607.21835v1 | https://arxiv.org/html/2607.21835v1#S6 — VI Policy Framework; https://arxiv.org/html/2607.21835v1#S3 — III Threat Model | https://arxiv.org/html/2607.21835v1#S8 — VIII Evaluation Results; https://arxiv.org/html/2607.21835v1#A1 — Appendix A Tool benchmarks | https://arxiv.org/html/2607.21835v1#S10 — X Limitations and Future Work; https://arxiv.org/html/2607.21835v1#S11 — XI Conclusion | Exact v1 links https://github.com/cisco-ai-defense/mcp-scanner, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-21835 | complete |
| SF-2026-ARXIV-2607-21857 | RP-6ddac2cc035537df | standard | arXiv:2607.21857v1 | SRC-ARXIV@arXiv:2607.21857v1 | https://arxiv.org/html/2607.21857v1#S3 — III Agentic Soundscape Construction Framework | https://arxiv.org/html/2607.21857v1#S4 — IV Experiments and Results; https://arxiv.org/html/2607.21857v1#S4.SS1 — IV-A Track A: Agent Evaluation | https://arxiv.org/html/2607.21857v1#S5 — V Discussion and Conclusion | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-21857 | complete |
| SF-2026-ARXIV-2607-21861 | RP-596300ef9c1bb2f8 | standard | arXiv:2607.21861v1 | SRC-ARXIV@arXiv:2607.21861v1 | https://arxiv.org/html/2607.21861v1#S1 — 1 Introduction; https://arxiv.org/html/2607.21861v1#S2 — 2 Task, Metric, and Recipe | https://arxiv.org/html/2607.21861v1#A2 — Appendix B Metric-Bias Analysis; https://arxiv.org/html/2607.21861v1#S3 — 3 Results | https://arxiv.org/html/2607.21861v1#S4 — 4 Discussion and Threats to Validity; https://arxiv.org/html/2607.21861v1#S5 — 5 Conclusion | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-21861 | complete |
| SF-2026-ARXIV-2607-21909 | RP-1fc6634ddc9c2684 | deep | arXiv:2607.21909v1 | SRC-ARXIV@arXiv:2607.21909v1 | https://arxiv.org/pdf/2607.21909v1#page=3 — Claim Plane Architecture and ChangeIntent; https://arxiv.org/pdf/2607.21909v1#page=4 — Admission and dependency invalidation | https://arxiv.org/pdf/2607.21909v1#page=7 — Comparative evaluation arms and setup | https://arxiv.org/pdf/2607.21909v1#page=9 — Confidence escalation boundary; https://arxiv.org/pdf/2607.21909v1#page=10 — Evidence and disclosure boundary | Not Disclosed — exact v1 exposes no uniquely versioned artifact locator used to enlarge the manuscript claim boundary. | claim:SF-2026-ARXIV-2607-21909 | complete |
| SF-2026-ARXIV-2607-21910 | RP-8baa82fe0321a6be | standard | arXiv:2607.21910v1 | SRC-ARXIV@arXiv:2607.21910v1 | https://arxiv.org/html/2607.21910v1#S5 — 5 The Flood-SAR System; https://arxiv.org/html/2607.21910v1#S5.SS1 — 5.1 Architecture | https://arxiv.org/html/2607.21910v1#S7 — 7 Evaluation; https://arxiv.org/html/2607.21910v1#A6 — Appendix F RQ2 Mechanism Study | https://arxiv.org/html/2607.21910v1#S8 — 8 Discussion and Limitations; https://arxiv.org/html/2607.21910v1#S9 — 9 Conclusion | Exact v1 links https://github.com/eyuchang/trace-worldmodel-flood-sar, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-21910 | complete |
| SF-2026-ARXIV-2607-21912 | RP-fd751b55ecb28727 | standard | arXiv:2607.21912v1 | SRC-ARXIV@arXiv:2607.21912v1 | https://arxiv.org/html/2607.21912v1#S6.SS1 — 6.1 Design; https://arxiv.org/html/2607.21912v1#S7.SS1 — 7.1 Design | https://arxiv.org/html/2607.21912v1#S3 — 3 Clean reliability benchmark; https://arxiv.org/html/2607.21912v1#S6.SS2 — 6.2 Results | https://arxiv.org/html/2607.21912v1#S8 — 8 Discussion; https://arxiv.org/html/2607.21912v1#S9 — 9 Conclusion | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-21912 | complete |
| SF-2026-ARXIV-2607-21918 | RP-69f9c0554388a6e0 | standard | arXiv:2607.21918v1 | SRC-ARXIV@arXiv:2607.21918v1 | https://arxiv.org/html/2607.21918v1#S2 — II Methodology; https://arxiv.org/html/2607.21918v1#S2.SS2 — II-B Action-conditioned latent diffusion ultrasound world model | https://arxiv.org/html/2607.21918v1#S3 — III Experiment; https://arxiv.org/html/2607.21918v1#S3.SS1 — III-A Experimental setup | https://arxiv.org/html/2607.21918v1#S4 — IV Discussion & Future work; https://arxiv.org/html/2607.21918v1#S5 — V Conclusion | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-21918 | complete |
| SF-2026-ARXIV-2607-21927 | RP-244c7db8ff20b510 | deep | arXiv:2607.21927v1 | SRC-ARXIV@arXiv:2607.21927v1 | https://arxiv.org/html/2607.21927v1#S4 — 4 Methods: The RIS Implementation | https://arxiv.org/html/2607.21927v1#S2 — 2 Results; https://arxiv.org/html/2607.21927v1#S2.SS2 — 2.2 Empirical Evaluation | https://arxiv.org/html/2607.21927v1#S3 — 3 Discussion | Exact v1 links https://github.com/santosardr/riskernel, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-21927 | complete |
| SF-2026-ARXIV-2607-21946 | RP-c0dffb1bf1a1a874 | standard | arXiv:2607.21946v1 | SRC-ARXIV@arXiv:2607.21946v1 | https://arxiv.org/html/2607.21946v1#S3 — 3 Methodology | https://arxiv.org/html/2607.21946v1#S4 — 4 Experiments; https://arxiv.org/html/2607.21946v1#S4.SS1 — 4.1 Experimental Settings | https://arxiv.org/html/2607.21946v1#A2.SS1 — B.1 A Reasoning Failure on Text-Only Level 1; https://arxiv.org/html/2607.21946v1#A2.SS2 — B.2 A Perception Failure on Level 3 and Its Recovery | Exact v1 links https://github.com/OpenDCAI/SciReasoner/tree/main/seephys_pro_codabench, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-21946 | complete |
| SF-2026-ARXIV-2607-21951 | RP-8bd8d9a5a71d5630 | standard | arXiv:2607.21951v1 | SRC-ARXIV@arXiv:2607.21951v1 | https://arxiv.org/html/2607.21951v1#S5 — 5. The SIREN Method; https://arxiv.org/html/2607.21951v1#A1 — Appendix A Results by Query–Model Context | https://arxiv.org/html/2607.21951v1#A1 — Appendix A Results by Query–Model Context; https://arxiv.org/html/2607.21951v1#A2 — Appendix B Per-Technique Full-Sweep Results | https://arxiv.org/html/2607.21951v1#S10 — 10. Discussion; https://arxiv.org/html/2607.21951v1#S11 — 11. Conclusion | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-21951 | complete |
| SF-2026-ARXIV-2607-21958 | RP-6ba611458a36a2fb | standard | arXiv:2607.21958v1 | SRC-ARXIV@arXiv:2607.21958v1 | https://arxiv.org/html/2607.21958v1#S3.SS1 — 3.1 The proposed token-level pivot framework | https://arxiv.org/html/2607.21958v1#S5 — 5 Experiments; https://arxiv.org/html/2607.21958v1#S5.SS1 — 5.1 Synthetic experiments | https://arxiv.org/html/2607.21958v1#S1 — 1 Introduction; https://arxiv.org/html/2607.21958v1#S2 — 2 Preliminaries | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-21958 | complete |
| SF-2026-ARXIV-2607-21962 | RP-3d633c3ba9495368 | deep | arXiv:2607.21962v1 | SRC-ARXIV@arXiv:2607.21962v1 | https://arxiv.org/html/2607.21962v1#S5.SS3 — 5.3 The layered architecture leads the memory systems at the short horizon; https://arxiv.org/html/2607.21962v1#S2.SS1 — 2.1 Agent memory architectures | https://arxiv.org/html/2607.21962v1#S2.SS2 — 2.2 Benchmarks, and the case for ground-truth-first generation; https://arxiv.org/html/2607.21962v1#S2.SS6 — 2.6 Confabulation, abstention, and judged evaluation | https://arxiv.org/html/2607.21962v1#S8 — 8 Conclusion and future work; https://arxiv.org/html/2607.21962v1#S7 — 7 Threats to validity | Exact v1 links https://github.com/veracium-ai/Veracium, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-21962 | complete |
| SF-2026-ARXIV-2607-21971 | RP-68d3ecffdf672ea2 | standard | arXiv:2607.21971v1 | SRC-ARXIV@arXiv:2607.21971v1 | https://arxiv.org/html/2607.21971v1#A1 — Appendix A GRPO Training Algorithm | https://arxiv.org/html/2607.21971v1#S3.SS2 — 3.2 Experiment Results; https://arxiv.org/html/2607.21971v1#A2 — Appendix B Evolution Ablations | https://arxiv.org/html/2607.21971v1#S6 — 6 Conclusion | Exact v1 links https://codeforces.com/, https://github.com/algorithmicsuperintelligence/openevolve, https://github.com/arXiv/html_feedback/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-21971 | complete |
| SF-2026-ARXIV-2607-21978 | RP-8b9f3b45ec6b39d4 | standard | arXiv:2607.21978v1 | SRC-ARXIV@arXiv:2607.21978v1 | https://arxiv.org/html/2607.21978v1#S3 — 3 Method; https://arxiv.org/html/2607.21978v1#S2.SS2 — 2.2 PEFT for MoE models. | https://arxiv.org/html/2607.21978v1#S4.SS2 — 4.2 Main Experimental Results; https://arxiv.org/html/2607.21978v1#A1.SS1 — A.1 Evaluation Protocol | https://arxiv.org/html/2607.21978v1#S5 — 5 Analysis and Discussion; https://arxiv.org/html/2607.21978v1#S6 — 6 Conclusion | Exact v1 links https://huggingface.co/datasets/xai-org/RealworldQA, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-21978 | complete |
| SF-2026-ARXIV-2607-21985 | RP-c09f73ebccd920a4 | deep | arXiv:2607.21985v1 | SRC-ARXIV@arXiv:2607.21985v1 | https://arxiv.org/html/2607.21985v1#S4 — 4. Design of SPDP: Unifying Static and Dynamic Sparsity; https://arxiv.org/html/2607.21985v1#S4.SS2 — 4.2. Decode Phase (spMspV) Kernel Design | https://arxiv.org/html/2607.21985v1#S3.SS1 — 3.1. Efficacy of Pruning: Roofline Analysis; https://arxiv.org/html/2607.21985v1#S5 — 5. Evaluation | https://arxiv.org/html/2607.21985v1#S6 — 6. Discussion and Future Work; https://arxiv.org/html/2607.21985v1#S7 — 7. Conclusion | Exact v1 links https://github.com/AIDASLab/SPDP, https://huggingface.co/docs/transformers/index, https://github.com/tatsu-lab/stanford_alpaca; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-21985 | complete |
| SF-2026-ARXIV-2607-22000 | RP-1d3dcc7eb5ecc319 | standard | arXiv:2607.22000v1 | SRC-ARXIV@arXiv:2607.22000v1 | https://arxiv.org/html/2607.22000v1#S3 — 3 Method; https://arxiv.org/html/2607.22000v1#S3.SS2 — 3.2 Model Architecture | https://arxiv.org/html/2607.22000v1#S4 — 4 Experiments; https://arxiv.org/html/2607.22000v1#S4.SS3 — 4.3 Evaluation of Latent Dynamics | https://arxiv.org/html/2607.22000v1#S5 — 5 Conclusion and Future Work | Exact v1 links https://zzwaang.github.io/music-jepa-demo/, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-22000 | complete |
| SF-2026-ARXIV-2607-22002 | RP-e655ee5ea74cced3 | deep | arXiv:2607.22002v1 | SRC-ARXIV@arXiv:2607.22002v1 | https://arxiv.org/html/2607.22002v1#S4 — 4 Method | https://arxiv.org/html/2607.22002v1#A1 — Appendix A Detailed Benchmark Results; https://arxiv.org/html/2607.22002v1#S5.SS3 — 5.3 Analysis and Ablation Study | https://arxiv.org/html/2607.22002v1#S6 — 6 Conclusion | Exact v1 links https://github.com/huggingface/Math-Verify, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-22002 | complete |
| SF-2026-ARXIV-2607-22013 | RP-3effb8ded3c505d4 | standard | arXiv:2607.22013v1 | SRC-ARXIV@arXiv:2607.22013v1 | https://arxiv.org/html/2607.22013v1#S1 — 1 Introduction; https://arxiv.org/html/2607.22013v1#S2 — 2 Visual Saliency Steering Distillation | https://arxiv.org/html/2607.22013v1#S3 — 3 Experiment; https://arxiv.org/html/2607.22013v1#S3.SS1 — 3.1 Experiments Settings | https://arxiv.org/html/2607.22013v1#S4 — 4 Conclusion | Exact v1 links https://github.com/BGWH123/VSSD, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-22013 | complete |
| SF-2026-ARXIV-2607-22014 | RP-b874643bd25ca452 | standard | arXiv:2607.22014v1 | SRC-ARXIV@arXiv:2607.22014v1 | https://arxiv.org/html/2607.22014v1#A4 — Appendix D Model Details | https://arxiv.org/html/2607.22014v1#A2 — Appendix B Extended Results; https://arxiv.org/html/2607.22014v1#A3 — Appendix C Additional Benchmark Details | https://arxiv.org/html/2607.22014v1#A1 — Appendix A Further Discussion; https://arxiv.org/html/2607.22014v1#S5 — 5 Conclusion | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-22014 | complete |
| SF-2026-ARXIV-2607-22022 | RP-529ca67dbee0257c | deep | arXiv:2607.22022v1 | SRC-ARXIV@arXiv:2607.22022v1 | https://arxiv.org/html/2607.22022v1#S5 — 5. Hardware Design Details; https://arxiv.org/html/2607.22022v1#S5.SS2 — 5.2. Overall Architecture | https://arxiv.org/html/2607.22022v1#S6 — 6. Evaluation; https://arxiv.org/html/2607.22022v1#S6.SS1 — 6.1. Experiment Setup | https://arxiv.org/html/2607.22022v1#S7 — 7. Conclusion | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-22022 | complete |
| SF-2026-ARXIV-2607-22024 | RP-fc6c83dbfa1e0397 | standard | arXiv:2607.22024v1 | SRC-ARXIV@arXiv:2607.22024v1 | https://arxiv.org/html/2607.22024v1#S6.SS2 — 6.2 Security Research Should Focus on Model Robustness | https://arxiv.org/html/2607.22024v1#A1 — Appendix A Full Benchmark Analysis; https://arxiv.org/html/2607.22024v1#S3.SS2 — 3.2 Continuous Evaluation Across Time | https://arxiv.org/html/2607.22024v1#S8 — 8 Conclusion | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-22024 | complete |
| SF-2026-ARXIV-2607-22034 | RP-90476d6205d6ba3e | standard | arXiv:2607.22034v1 | SRC-ARXIV@arXiv:2607.22034v1 | https://arxiv.org/html/2607.22034v1#S3 — 3 Method; https://arxiv.org/html/2607.22034v1#S2.SS1 — 2.1 Verbalized uncertainty in language and vision-language models | https://arxiv.org/html/2607.22034v1#A1 — Appendix A Full results tables; https://arxiv.org/html/2607.22034v1#S4 — 4 Results | https://arxiv.org/html/2607.22034v1#S5 — 5 Discussion; https://arxiv.org/html/2607.22034v1#S5.SS4 — 5.4 Limitations | Exact v1 links https://github.com/Asif-Ferdous/vlm-reliability, https://huggingface.co/HuggingFaceTB/SmolVLM-Instruct, https://github.com/arXiv/html_feedback/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-22034 | complete |
| SF-2026-ARXIV-2607-22038 | RP-b4f136f52e2c339c | deep | arXiv:2607.22038v1 | SRC-ARXIV@arXiv:2607.22038v1 | https://arxiv.org/html/2607.22038v1#S3 — 3. System Design; https://arxiv.org/html/2607.22038v1#A1.SS8 — A.8. Methodology | https://arxiv.org/html/2607.22038v1#A1.SS6 — A.6. Evaluation and expected results; https://arxiv.org/html/2607.22038v1#A1.SS5 — A.5. Experiment workflow | https://arxiv.org/html/2607.22038v1#S6 — 6. Conclusion | Exact v1 links https://github.com/afzalxo/sparse-by-command, https://github.com/carla-simulator/carla/issues/4004, https://github.com/arXiv/html_feedback/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-22038 | complete |
| SF-2026-ARXIV-2607-22039 | RP-84035652766c3c87 | standard | arXiv:2607.22039v1 | SRC-ARXIV@arXiv:2607.22039v1 | https://arxiv.org/html/2607.22039v1#A1 — Appendix A The Use of Large Language Models; https://arxiv.org/html/2607.22039v1#A5.SS1 — E.1 The Number of Merging Model | https://arxiv.org/html/2607.22039v1#A3 — Appendix C Detailed Experiments Results; https://arxiv.org/html/2607.22039v1#A6.SS1 — F.1 Experiment Setup Details | https://arxiv.org/html/2607.22039v1#S6 — 6 Conclusion | Exact v1 links https://huggingface.co/models, https://github.com/OpenRLHF/OpenRLHF, https://github.com/volcengine/verl; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-22039 | complete |
| SF-2026-ARXIV-2607-22043 | RP-2d46f0570ace93d5 | deep | arXiv:2607.22043v1 | SRC-ARXIV@arXiv:2607.22043v1 | https://arxiv.org/html/2607.22043v1#A1 — Appendix A Implementation Details; https://arxiv.org/html/2607.22043v1#S4.SS1 — 4.1 Evaluation of Base Models | https://arxiv.org/html/2607.22043v1#A2 — Appendix B Experiment Results; https://arxiv.org/html/2607.22043v1#S2.SS3 — 2.3 Experimental Setup | https://arxiv.org/html/2607.22043v1#S6 — 6 Conclusion | Exact v1 links https://huggingface.co/datasets/xai-org/RealworldQA, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-22043 | complete |
| SF-2026-ARXIV-2607-22083 | RP-10c0be91856c3107 | standard | arXiv:2607.22083v1 | SRC-ARXIV@arXiv:2607.22083v1 | https://arxiv.org/html/2607.22083v1#S2.SS1 — 2.1 Architecture | https://arxiv.org/html/2607.22083v1#A2 — Appendix B Evaluation settings; https://arxiv.org/html/2607.22083v1#A2.SS2 — B.2 Code Agent Evaluation | https://arxiv.org/html/2607.22083v1#S4 — 4 Conclusion | Exact v1 links https://huggingface.co/Nanbeige/Nanbeige4.2-3B, https://github.com/openclaw/openclaw, https://github.com/arXiv/html_feedback/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-22083 | complete |
| SF-2026-ARXIV-2607-22091 | RP-b397c9e0ebd1465c | standard | arXiv:2607.22091v1 | SRC-ARXIV@arXiv:2607.22091v1 | https://arxiv.org/html/2607.22091v1#Pt0.A4 — Appendix 0.D Implementation Details of the Baseline Methods; https://arxiv.org/html/2607.22091v1#S2.SS3 — 2.3 Motivation for the Proposed Method | https://arxiv.org/html/2607.22091v1#Pt0.A3 — Appendix 0.C Analysis of the Hyperparameters; https://arxiv.org/html/2607.22091v1#Pt0.A3.SS1 — 0.C.1 Analysis on the guidance strength | https://arxiv.org/html/2607.22091v1#S6 — 6 Conclusion | Exact v1 links https://github.com/SonyResearch/SPA, https://huggingface.co/black-forest-labs/FLUX.1-dev, https://huggingface.co/nyanko7/flux-dev-de-distill; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-22091 | complete |
| SF-2026-ARXIV-2607-22098 | RP-5f6c4318eca99479 | standard | arXiv:2607.22098v1 | SRC-ARXIV@arXiv:2607.22098v1 | https://arxiv.org/html/2607.22098v1#A3.SS5 — C.5 Effect of truthfulness labeling methods; https://arxiv.org/html/2607.22098v1#S4 — 4 Method | https://arxiv.org/html/2607.22098v1#A1 — Appendix A Additional experimental details; https://arxiv.org/html/2607.22098v1#A2 — Appendix B Additional ablation studies | https://arxiv.org/html/2607.22098v1#A4 — Appendix D Broader impact and limitations; https://arxiv.org/html/2607.22098v1#S7 — 7 Conclusion | Exact v1 links https://huggingface.co/datasets/HuggingFaceH4/aime_2024, https://huggingface.co/datasets/opencompass/AIME2025, https://huggingface.co/MoritzLaurer/DeBERTa-v3-large-mnli-fever-anli-ling-wanli; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-22098 | complete |
| SF-2026-ARXIV-2607-22119 | RP-452f7764a5e70d6a | standard | arXiv:2607.22119v1 | SRC-ARXIV@arXiv:2607.22119v1 | https://arxiv.org/html/2607.22119v1#S3 — III Technical Approach | https://arxiv.org/html/2607.22119v1#S5 — V Experimental Evaluation; https://arxiv.org/html/2607.22119v1#S4 — IV DynaBench: A Dynamic Environment Manipulation Benchmark | https://arxiv.org/html/2607.22119v1#S6 — VI Conclusion | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-22119 | complete |
| SF-2026-ARXIV-2607-22157 | RP-381ace3921396498 | standard | arXiv:2607.22157v1 | SRC-ARXIV@arXiv:2607.22157v1 | https://arxiv.org/html/2607.22157v1#A1.SS1 — A.1 Memory advertisement in the system prompt; https://arxiv.org/html/2607.22157v1#A5 — Appendix E Statistical methodology | https://arxiv.org/html/2607.22157v1#A2 — Appendix B Transfer experiment details; https://arxiv.org/html/2607.22157v1#S3 — 3 Experimental Setup | https://arxiv.org/html/2607.22157v1#S5 — 5 Discussion; https://arxiv.org/html/2607.22157v1#S6 — 6 Conclusion | Exact v1 links https://github.com/memcoai/spark-continual-learning-paper-data, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-22157 | complete |
| SF-2026-ARXIV-2607-22165 | RP-2f19d21565861f50 | standard | arXiv:2607.22165v1 | SRC-ARXIV@arXiv:2607.22165v1 | https://arxiv.org/html/2607.22165v1#S6.SS5 — 6.5. Fixed-backbone Agent-System Comparison; https://arxiv.org/html/2607.22165v1#S7.SS1 — 7.1. Implications for Database-Agent Design | https://arxiv.org/html/2607.22165v1#S3.SS4 — 3.4. Evaluation Interface: Post-fix State, Report, and Trace; https://arxiv.org/html/2607.22165v1#S5 — 5. Evaluation Protocol | https://arxiv.org/html/2607.22165v1#S7 — 7. Discussion; https://arxiv.org/html/2607.22165v1#S8 — 8. Conclusion | Exact v1 links https://github.com/TanJI-C/DBA-Bench, https://github.com/TsinghuaDatabaseGroup/DB-GPT, https://github.com/arXiv/html_feedback/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-22165 | complete |
| SF-2026-ARXIV-2607-22182 | RP-4ae749d4c09c36a1 | standard | arXiv:2607.22182v1 | SRC-ARXIV@arXiv:2607.22182v1 | https://arxiv.org/html/2607.22182v1#S2 — 2 Taxonomy Design Principles and Construction; https://arxiv.org/html/2607.22182v1#S2.SS1 — 2.1 Scope and Design Objective | https://arxiv.org/html/2607.22182v1#S4.SS2 — 4.2 Results; https://arxiv.org/html/2607.22182v1#S5.SS2 — 5.2 Implications for Evaluation Design and Capability Diagnosis | https://arxiv.org/html/2607.22182v1#S5 — 5 Discussion and Conclusion; https://arxiv.org/html/2607.22182v1#S5.SS4 — 5.4 Limitations and Boundary Conditions | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-22182 | complete |
| SF-2026-ARXIV-2607-22186 | RP-6a8a925ecce592d8 | deep | arXiv:2607.22186v1 | SRC-ARXIV@arXiv:2607.22186v1 | https://arxiv.org/html/2607.22186v1#S3.SS3 — 3.3 An Entropy-Scaled Design Principle; https://arxiv.org/html/2607.22186v1#S4 — 4 Method | https://arxiv.org/html/2607.22186v1#S5 — 5 Experiment | https://arxiv.org/html/2607.22186v1#S6 — 6 Conclusion | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-22186 | complete |
| SF-2026-ARXIV-2607-22188 | RP-b08c81ed6dfd7a31 | standard | arXiv:2607.22188v1 | SRC-ARXIV@arXiv:2607.22188v1 | https://arxiv.org/html/2607.22188v1#S3 — 3 Experimental Design; https://arxiv.org/html/2607.22188v1#S3.SS1 — 3.1 Design logic | https://arxiv.org/html/2607.22188v1#Ax4 — Appendix D. Benchmark checks, request specifications, and exact tests; https://arxiv.org/html/2607.22188v1#S2.SS2 — 2.2 Strategic LLMs and public-resource evaluation | https://arxiv.org/html/2607.22188v1#S2.SS1 — 2.1 From single-agent to multi-agent alignment failures; https://arxiv.org/html/2607.22188v1#S5 — 5 Discussion | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-22188 | complete |
| SF-2026-ARXIV-2607-22199 | RP-4a4ebabb76e8e357 | standard | arXiv:2607.22199v1 | SRC-ARXIV@arXiv:2607.22199v1 | https://arxiv.org/html/2607.22199v1#S8.SS3 — 8.3 General Diffusion Models; https://arxiv.org/html/2607.22199v1#S8.SS5 — 8.5 Learning Theory for Diffusion Models | https://arxiv.org/html/2607.22199v1#S1 — 1 Introduction; https://arxiv.org/html/2607.22199v1#S2 — 2 Related Work | https://arxiv.org/html/2607.22199v1#S8 — 8 Extensions and Future Directions | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-22199 | complete |
| SF-2026-ARXIV-2607-22225 | RP-31825064ed8cd881 | standard | arXiv:2607.22225v1 | SRC-ARXIV@arXiv:2607.22225v1 | https://arxiv.org/html/2607.22225v1#S2.SS1 — II-A Safe Control of Ego–World Robotic Systems; https://arxiv.org/html/2607.22225v1#S4.SS2 — IV-B Ego–World Vehicle Models for MPC Design | https://arxiv.org/html/2607.22225v1#S4 — IV Virtual Experiments; https://arxiv.org/html/2607.22225v1#S4.SS3 — IV-C Virtual Experiment on ETHZ Mobil Track | https://arxiv.org/html/2607.22225v1#S6 — VI Conclusions | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-22225 | complete |
| SF-2026-ARXIV-2607-22242 | RP-e94a9a34f3effad0 | deep | arXiv:2607.22242v1 | SRC-ARXIV@arXiv:2607.22242v1 | https://arxiv.org/html/2607.22242v1#S3 — 3. Proposed Agentic Scheduler Design | https://arxiv.org/html/2607.22242v1#A1 — Appendix A S13 Ablation Study; https://arxiv.org/html/2607.22242v1#S4 — 4. Evaluation | https://arxiv.org/html/2607.22242v1#S5 — 5. Discussion; https://arxiv.org/html/2607.22242v1#S7 — 7. Conclusion | Exact v1 links https://github.com/crewAIInc/crewAI, https://github.com/langchain-ai/langgraph, https://github.com/arXiv/html_feedback/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-22242 | complete |
| SF-2026-ARXIV-2607-22251 | RP-37e22415216621d0 | standard | arXiv:2607.22251v1 | SRC-ARXIV@arXiv:2607.22251v1 | https://arxiv.org/html/2607.22251v1#A1.SS2 — A.2 Method-Specific Configurations; https://arxiv.org/html/2607.22251v1#S3 — 3 Method | https://arxiv.org/html/2607.22251v1#A1 — Appendix A Experimental Details; https://arxiv.org/html/2607.22251v1#A1.SS1 — A.1 Common Training and Evaluation Setup | https://arxiv.org/html/2607.22251v1#S6 — 6 Conclusion and Future Work; https://arxiv.org/html/2607.22251v1#S5 — 5 Discussion | Exact v1 links https://neurips.cc/public/guides/CodeSubmissionPolicy, https://paperswithcode.com/datasets, https://github.com/arXiv/html_feedback/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-22251 | complete |
| SF-2026-ARXIV-2607-22305 | RP-80a60ea81331006e | standard | arXiv:2607.22305v1 | SRC-ARXIV@arXiv:2607.22305v1 | https://arxiv.org/html/2607.22305v1#A1.SS2 — A.2 Model Evaluations: System Cards, Technical Reports; https://arxiv.org/html/2607.22305v1#S5.SS3 — 5.3 Evaluations and Methods That Model Developers Could Adopt | https://arxiv.org/html/2607.22305v1#A1.SS2 — A.2 Model Evaluations: System Cards, Technical Reports; https://arxiv.org/html/2607.22305v1#S5.SS3 — 5.3 Evaluations and Methods That Model Developers Could Adopt | https://arxiv.org/html/2607.22305v1#S5 — 5 Call to Action: Future Directions; https://arxiv.org/html/2607.22305v1#S6 — 6 Conclusion | Exact v1 links https://github.com/elinorp-d/scholar-trend-tracker, https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=ELEC&sectionNum=9084, https://github.com/xai-org/grok-prompts; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-22305 | complete |
| SF-2026-ARXIV-2607-22319 | RP-788f8600623b68d5 | standard | arXiv:2607.22319v1 | SRC-ARXIV@arXiv:2607.22319v1 | https://arxiv.org/html/2607.22319v1#S4.SS4 — 4.4 System Architecture | https://arxiv.org/html/2607.22319v1#S1 — 1 Introduction; https://arxiv.org/html/2607.22319v1#S2 — 2 Bridging the Knowledge Gap for LLM-based Data Integration | https://arxiv.org/html/2607.22319v1#S6 — 6 Conclusion | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-22319 | complete |
| SF-2026-ARXIV-2607-22334 | RP-98031252fa853afd | standard | arXiv:2607.22334v1 | SRC-ARXIV@arXiv:2607.22334v1 | https://arxiv.org/html/2607.22334v1#A8.SS2 — H.2 Method-Agnostic Distributional Closeness; https://arxiv.org/html/2607.22334v1#S3 — 3 Method | https://arxiv.org/html/2607.22334v1#A8 — Appendix H Extended Results; https://arxiv.org/html/2607.22334v1#A8.SS1 — H.1 Per-Benchmark Scores for the Divergence Comparison | https://arxiv.org/html/2607.22334v1#S5 — 5 Conclusion | Exact v1 links https://huggingface.co/spaces/HuggingFaceH4/on-policy-distillation, https://huggingface.co/Qwen/Qwen3.5-2B, https://huggingface.co/zai-org/GLM-Z1-9B-0414; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-22334 | complete |
| SF-2026-ARXIV-2607-22367 | RP-c731018f1559d76e | standard | arXiv:2607.22367v1 | SRC-ARXIV@arXiv:2607.22367v1 | https://arxiv.org/html/2607.22367v1#S3.SS3 — 3.3. Interpretability methods; https://arxiv.org/html/2607.22367v1#S3.SS2 — 3.2. Model and training setup | https://arxiv.org/html/2607.22367v1#S4 — 4. Experimental results; https://arxiv.org/html/2607.22367v1#S4.SS1 — 4.1. Experimental results on Dataset 1 | https://arxiv.org/html/2607.22367v1#S4.SS3 — 4.3. Limitations of the empirical analysis; https://arxiv.org/html/2607.22367v1#S5 — 5. Conclusions and perspectives | Exact v1 links https://github.com/umbertoBiccari/Attn_interpretability, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-22367 | complete |
| SF-2026-ARXIV-2607-22368 | RP-bc6be2a4f63817e1 | standard | arXiv:2607.22368v1 | SRC-ARXIV@arXiv:2607.22368v1 | https://arxiv.org/html/2607.22368v1#A8 — Appendix H Why Exposures Recur: Design Considerations; https://arxiv.org/html/2607.22368v1#S5.SS4 — 5.4 Independent Cases Support the Attribution Framework | https://arxiv.org/html/2607.22368v1#S5 — 5 Experimental Results; https://arxiv.org/html/2607.22368v1#A3.SS1 — C.1 Case 1 — Benchmark overexposure (SWE-bench Pro, OpenLibrary) | https://arxiv.org/html/2607.22368v1#A9 — Appendix I Protocol-Specific Verification and Future Directions; https://arxiv.org/html/2607.22368v1#A9.SS1 — I.1 Future Work | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-22368 | complete |
| SF-2026-ARXIV-2607-22385 | RP-010f360d092c6a97 | standard | arXiv:2607.22385v1 | SRC-ARXIV@arXiv:2607.22385v1 | https://arxiv.org/html/2607.22385v1#S2.SS1 — 2.1 Benchmark systems and evaluation protocol; https://arxiv.org/html/2607.22385v1#S2.SS6 — 2.6 AgentRCA extends to large multivariate industrial systems | https://arxiv.org/html/2607.22385v1#S2.SS1 — 2.1 Benchmark systems and evaluation protocol; https://arxiv.org/html/2607.22385v1#S2 — 2 Results | https://arxiv.org/html/2607.22385v1#S3 — 3 Discussion | Exact v1 links https://huggingface.co/Qwen/Qwen3-30B-A3B-Thinking-2507, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-22385 | complete |
| SF-2026-ARXIV-2607-22389 | RP-8670b9b681b9d563 | deep | arXiv:2607.22389v1 | SRC-ARXIV@arXiv:2607.22389v1 | https://arxiv.org/html/2607.22389v1#S4.SS1 — IV-A System Architecture Overview; https://arxiv.org/html/2607.22389v1#S4 — IV HiKV Accelerator Architecture | https://arxiv.org/html/2607.22389v1#S5 — V Experimental Results; https://arxiv.org/html/2607.22389v1#S3.SS1 — III-A Importance Analysis of KV Cache | https://arxiv.org/html/2607.22389v1#S6 — VI Conclusion | Exact v1 links https://github.com/meta-llama/llama3/blob/main/MODEL_CARD.md, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-22389 | complete |
| SF-2026-ARXIV-2607-22392 | RP-2a0da3d31158cf44 | standard | arXiv:2607.22392v1 | SRC-ARXIV@arXiv:2607.22392v1 | https://arxiv.org/html/2607.22392v1#S7.SS2 — 7.2 Implications for evaluation design; https://arxiv.org/html/2607.22392v1#S2.SS2 — 2.2 History use by language models | https://arxiv.org/html/2607.22392v1#S6 — 6 Results; https://arxiv.org/html/2607.22392v1#S7.SS2 — 7.2 Implications for evaluation design | https://arxiv.org/html/2607.22392v1#S10 — 10 Conclusion; https://arxiv.org/html/2607.22392v1#S8 — 8 Limitations | Exact v1 links https://dx.doi.org/10.18653/v1/2025.acl-demo.17, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-22392 | complete |
| SF-2026-ARXIV-2607-22393 | RP-3815fc077abe078e | standard | arXiv:2607.22393v1 | SRC-ARXIV@arXiv:2607.22393v1 | https://arxiv.org/html/2607.22393v1#S1 — 1 Introduction; https://arxiv.org/html/2607.22393v1#S2 — 2 Related Work | https://arxiv.org/html/2607.22393v1#A1 — Appendix A Benchmark Details; https://arxiv.org/html/2607.22393v1#A2 — Appendix B Evaluation Protocol | https://arxiv.org/html/2607.22393v1#S5 — 5 Limitations; https://arxiv.org/html/2607.22393v1#S6 — 6 Conclusion | Exact v1 links https://github.com/Feinaldo2/SceneActBench, https://feinaldo2.github.io/sceneactbench-project-page/, https://huggingface.co/datasets/FEInaldo/SceneActBench/tree/main; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-22393 | complete |
| SF-2026-ARXIV-2607-22400 | RP-1afef97ba5158d7e | deep | arXiv:2607.22400v1 | SRC-ARXIV@arXiv:2607.22400v1 | https://arxiv.org/html/2607.22400v1#S2.SS4 — II-D Edge Resource Orchestration and Multi-Agent Systems; https://arxiv.org/html/2607.22400v1#S3 — III Architecture | https://arxiv.org/html/2607.22400v1#S6 — VI Evaluation; https://arxiv.org/html/2607.22400v1#S6.SS1 — VI-A Experimental Setup | https://arxiv.org/html/2607.22400v1#S6.SS6 — VI-F Discussion; https://arxiv.org/html/2607.22400v1#S7 — VII Conclusion | Exact v1 links https://github.com/MarlaGru/Edge_Device_AI_Hardware_monitore_Dataset, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-22400 | complete |
| SF-2026-ARXIV-2607-22430 | RP-2408ab698569e55a | standard | arXiv:2607.22430v1 | SRC-ARXIV@arXiv:2607.22430v1 | https://arxiv.org/html/2607.22430v1#S3 — 3 Method; https://arxiv.org/html/2607.22430v1#S3.SS2 — 3.2 Identifiability of Controlled World Models | https://arxiv.org/html/2607.22430v1#A4 — Appendix D Experimental Details; https://arxiv.org/html/2607.22430v1#S4 — 4 Experiments | https://arxiv.org/html/2607.22430v1#S5 — 5 Conclusion | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-22430 | complete |
| SF-2026-ARXIV-2607-22432 | RP-f179b8ab1720f270 | deep | arXiv:2607.22432v1 | SRC-ARXIV@arXiv:2607.22432v1 | https://arxiv.org/html/2607.22432v1#S2.SS1 — 2.1. GPU Performance Modeling; https://arxiv.org/html/2607.22432v1#S2.SS2 — 2.2. Modeling Gap for Tile-Centric Programs | https://arxiv.org/html/2607.22432v1#S5 — 5. Evaluation; https://arxiv.org/html/2607.22432v1#S5.SS1 — 5.1. Experimental Setup | https://arxiv.org/html/2607.22432v1#S7 — 7. Limitations and Future Work; https://arxiv.org/html/2607.22432v1#S8 — 8. Conclusion | Exact v1 links https://rocm.docs.amd.com/projects/omniperf/en/docs-6.2.1/what-is-omniperf.html, https://github.com/tile-ai/tilelang, https://github.com/NVIDIA/cutlass; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-22432 | complete |
| SF-2026-ARXIV-2607-22445 | RP-940efaf19699c21e | standard | arXiv:2607.22445v1 | SRC-ARXIV@arXiv:2607.22445v1 | https://arxiv.org/html/2607.22445v1#S3 — 3 Three-Source Architecture; https://arxiv.org/html/2607.22445v1#S3.SS4 — 3.4 Combined Application of the Three-Source Architecture | https://arxiv.org/html/2607.22445v1#S5 — 5 Validation Results | https://arxiv.org/html/2607.22445v1#S6 — 6 Discussion and Limitations; https://arxiv.org/html/2607.22445v1#S7 — 7 Conclusion | Exact v1 links https://github.com/0xballistics/mostargate, https://dx.doi.org/10.18653/v1/2023.emnlp-demo.40, https://aclanthology.org/2023.emnlp-demo.40; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-22445 | complete |
| SF-2026-ARXIV-2607-22448 | RP-8ff145ad7d1dac0b | standard | arXiv:2607.22448v1 | SRC-ARXIV@arXiv:2607.22448v1 | https://arxiv.org/html/2607.22448v1#Sx4 — Attribution Methodology; https://arxiv.org/html/2607.22448v1#Sx5.SS0.SSS0.Px2 — Engines, profiles, and frameworks. | https://arxiv.org/html/2607.22448v1#Sx4.SS0.SSS0.Px7 — Analysis.; https://arxiv.org/html/2607.22448v1#Sx5 — Experimental Setup | https://arxiv.org/html/2607.22448v1#Sx6.SS0.SSS0.Px4 — Failure ledger (Table 8 ).; https://arxiv.org/html/2607.22448v1#Sx7 — Future Work | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-22448 | complete |
| SF-2026-ARXIV-2607-22465 | RP-a718c8181dd0ed99 | deep | arXiv:2607.22465v1 | SRC-ARXIV@arXiv:2607.22465v1 | https://arxiv.org/html/2607.22465v1#S3 — 3 Methodology; https://arxiv.org/html/2607.22465v1#S3.SS2 — 3.2 Context-Conditioned Model Selection | https://arxiv.org/html/2607.22465v1#S4 — 4 Evaluation | https://arxiv.org/html/2607.22465v1#S1 — 1 Introduction; https://arxiv.org/html/2607.22465v1#S2 — 2 Related Work | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-22465 | complete |
| SF-2026-ARXIV-2607-22489 | RP-eba5e9332299a156 | standard | arXiv:2607.22489v1 | SRC-ARXIV@arXiv:2607.22489v1 | https://arxiv.org/html/2607.22489v1#S3 — 3 Methodology; https://arxiv.org/html/2607.22489v1#S3.SS2 — 3.2 Method | https://arxiv.org/html/2607.22489v1#A3 — Appendix C Additional experiments; https://arxiv.org/html/2607.22489v1#S4 — 4 Experiments | https://arxiv.org/html/2607.22489v1#S5 — 5 Discussion | Exact v1 links https://github.com/tatsu-lab/stanford_alpaca, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-22489 | complete |
| SF-2026-ARXIV-2607-22511 | RP-38982500bf39a5bd | standard | arXiv:2607.22511v1 | SRC-ARXIV@arXiv:2607.22511v1 | https://arxiv.org/html/2607.22511v1#S4.SS1 — 4.1 Design and scope; https://arxiv.org/html/2607.22511v1#S6.SS2 — 6.2 Which self-proposed questions the system converts | https://arxiv.org/html/2607.22511v1#S4.SS3 — 4.3 Flagship results; https://arxiv.org/html/2607.22511v1#S6 — 6 Results | https://arxiv.org/html/2607.22511v1#S7 — 7 Discussion and Limitations; https://arxiv.org/html/2607.22511v1#S8 — 8 Conclusion | Exact v1 links https://github.com/Jiyuan-Tan/CausalForge, https://github.com/optsuite/optlib, https://github.com/auto-res/lean-rademacher; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-22511 | complete |
| SF-2026-ARXIV-2607-22520 | RP-26805c1aa53ab14e | standard | arXiv:2607.22520v1 | SRC-ARXIV@arXiv:2607.22520v1 | https://arxiv.org/html/2607.22520v1#A2 — Appendix B Worked Cases: Correct Method, Wrong Grounding or Verification; https://arxiv.org/html/2607.22520v1#S6.SS1 — 6.1. Designing and Measuring Skill Libraries | https://arxiv.org/html/2607.22520v1#S3 — 3. Experimental Setup; https://arxiv.org/html/2607.22520v1#S3.SS1 — 3.1. Benchmarks and Tasks | https://arxiv.org/html/2607.22520v1#S5.SS4 — 5.4. Residual Failures; https://arxiv.org/html/2607.22520v1#S6 — 6. Discussion | Exact v1 links https://github.com/sentient-agi/meta-skill-creator, https://github.com/anthropics/skills/tree/main/skills/skill-creator, https://github.com/openai/skills/tree/main/skills/.system/skill-creator; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-22520 | complete |
| SF-2026-ARXIV-2607-22529 | RP-317d40ed3e0ce1b3 | standard | arXiv:2607.22529v1 | SRC-ARXIV@arXiv:2607.22529v1 | https://arxiv.org/html/2607.22529v1#S3 — 3 Methodology; https://arxiv.org/html/2607.22529v1#A3 — Appendix C Training and Implementation Details | https://arxiv.org/html/2607.22529v1#A7 — Appendix G Analysis of Evaluation Benchmark; https://arxiv.org/html/2607.22529v1#A1 — Appendix A Iteration-wise Evaluation Trajectories | https://arxiv.org/html/2607.22529v1#A8 — Appendix H Limitations and Future Work; https://arxiv.org/html/2607.22529v1#S5 — 5 Conclusion | Exact v1 links https://github.com/Qwen-Applications/skill-self-play, https://huggingface.co/blog/ibm-granite/granit-4-1, https://github.com/arXiv/html_feedback/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-22529 | complete |
| SF-2026-ARXIV-2607-22530 | RP-69c5569d38d06c4d | deep | arXiv:2607.22530v1 | SRC-ARXIV@arXiv:2607.22530v1 | https://arxiv.org/html/2607.22530v1#A3 — Appendix C Implementation, Data, and Training Details; https://arxiv.org/html/2607.22530v1#A3.SS2 — C.2 World Model and Policy Training Details | https://arxiv.org/html/2607.22530v1#A1 — Appendix A Additional Evaluation and Improvement Results; https://arxiv.org/html/2607.22530v1#S3.SS4 — 3.4 Visuo-Tactile Policy Improvement and Evaluation | https://arxiv.org/html/2607.22530v1#S5 — 5 Conclusion; https://arxiv.org/html/2607.22530v1#S6 — 6 Limitations | Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-22530 | complete |
| SF-2026-ARXIV-2607-22535 | RP-763275b260593164 | standard | arXiv:2607.22535v1 | SRC-ARXIV@arXiv:2607.22535v1 | https://arxiv.org/html/2607.22535v1#S3 — 3 Method; https://arxiv.org/html/2607.22535v1#A2 — Appendix B Model, Baseline, and Evaluation Details | https://arxiv.org/html/2607.22535v1#A2 — Appendix B Model, Baseline, and Evaluation Details; https://arxiv.org/html/2607.22535v1#A5 — Appendix E Additional Qualitative Results | https://arxiv.org/html/2607.22535v1#S5 — 5 Conclusion and Limitations | Exact v1 links https://github.com/aigc-apps/VideoX-Fun, https://github.com/ModelTC/lightx2v, https://github.com/robocasa/robocasa-gr1-tabletop-tasks; no event-time commit was independently pinned, so the manuscript remains the claim authority. | claim:SF-2026-ARXIV-2607-22535 | complete |

### Source Reviews

<!-- review:SF-2026-ARXIV-2607-21596:start -->
### FlowEvo: Self-Evolving Agents through the Co-Evolution of Workflows and Executable Skills

<!-- claim:SF-2026-ARXIV-2607-21596:start -->Large language model agents can adapt to complex tasks by constructing workflows at inference time, but procedures discovered in one episode are usually discarded after execution. Existing skill libraries provide reusable executable routines, but are typically assembled offline and do not grow from the agent's own workflows. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-21596:end -->

**为什么进入候选分母。** 摘要首要问题为“Large language model agents can adapt to complex tasks by constructing workflows at inference time, but procedures discovered in one episode are usually discarded after execution.”；它把 context、memory、能力或进度变成持久且可验证的 agent state。

**机制与状态边界。** We introduce FlowEvo, a training-free framework in which workflows and skills co-evolve at inference time.

**证据证明什么。** Across 10 base models spanning 7B to 671B parameters, FlowEvo outperforms ExpeL in 49 of 50 model-dataset comparisons.

**证据没有证明什么。** In that sense, continual use may depend not only on how new skills are acquired, but also on how the skill bank is maintained over time ( Yue et al., 2026b ) . 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.21596v1#A2 — Appendix B Framework Thresholds and Configuration Constants; https://arxiv.org/html/2607.21596v1#S3 — 3 Method。Evaluation：https://arxiv.org/html/2607.21596v1#S4 — 4 Experiments; https://arxiv.org/html/2607.21596v1#S4.SS1 — 4.1 Experimental setup。Limitations / counterevidence：https://arxiv.org/html/2607.21596v1#S5 — 5 Discussion; https://arxiv.org/html/2607.21596v1#S6 — 6 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/DEFENSE-SEU/FlowEvo, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 显式 agent state 改善恢复与控制，但增加状态陈旧、错误提交、跨轮污染和一致性责任。 论文自身的边界信号是：In that sense, continual use may depend not only on how new skills are acquired, but also on how the skill bank is maintained over time ( Yue et al., 2026b ) .

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`AGENT-WORKFLOW`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-21596:end -->

<!-- review:SF-2026-ARXIV-2607-21599:start -->
### Decoupled Attention Fusion: Accelerating RAG with Efficient KV Cache Reuse

<!-- claim:SF-2026-ARXIV-2607-21599:start -->Retrieval-Augmented Generation (RAG) effectively mitigates hallucinations in Large Language Models (LLMs) but suffers from prohibitive Time-To-First-Token (TTFT) latency in long-context scenarios. Reusing pre-computed document KV caches addresses this but introduces a distribution mismatch, where offline caches lack the inter-document attention patterns required for coherent reasoning. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-21599:end -->

**为什么进入候选分母。** 摘要首要问题为“Retrieval-Augmented Generation (RAG) effectively mitigates hallucinations in Large Language Models (LLMs) but suffers from prohibitive Time-To-First-Token (TTFT) latency in long-context scenarios.”；它改变推理期状态放置、数据移动、执行控制或实时 SLO。

**机制与状态边界。** To address these challenges, we propose Decoupled Attention Fusion (DAF), a framework that maintains high accuracy while significantly reducing recomputation overhead.

**证据证明什么。** CacheBlend reduces recomputation via selective attention, but suffers severe accuracy degradation at longer contexts.

**证据没有证明什么。** However, as the context length increases, its accumulated approximation errors lead to noticeable degradation in retrieval and generation quality, limiting its scalability in truly long-context RAG scenarios. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.21599v1#S2 — 2. Methods: Decoupled Attention Fusion。Evaluation：https://arxiv.org/html/2607.21599v1#S3 — 3. Preliminary Results。Limitations / counterevidence：https://arxiv.org/html/2607.21599v1#S1 — 1. Introduction; https://arxiv.org/html/2607.21599v1#S2 — 2. Methods: Decoupled Attention Fusion。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更激进的缓存、迁移、并行或专用执行会换取吞吐/时延，同时增加配置依赖、资源压力与回退路径。 论文自身的边界信号是：However, as the context length increases, its accumulated approximation errors lead to noticeable degradation in retrieval and generation quality, limiting its scalability in truly long-context RAG scenarios.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`INFER-KV-CACHE`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-21599:end -->

<!-- review:SF-2026-ARXIV-2607-21600:start -->
### Securing Multimodal AI through Internal Information Decomposition

<!-- claim:SF-2026-ARXIV-2607-21600:start -->Multimodal large language models introduce attack surfaces absent in unimodal systems: adversaries can distribute malicious intent across modalities to evade unimodal safeguards. This motivates using cross-modal consistency as a detection signal rather than inspecting each modality in isolation. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-21600:end -->

**为什么进入候选分母。** 摘要首要问题为“Multimodal large language models introduce attack surfaces absent in unimodal systems: adversaries can distribute malicious intent across modalities to evade unimodal safeguards.”；它改变执行安全的 trust boundary、guard 或 failure detection。

**机制与状态边界。** We propose FlowGuard, a lightweight inference-time framework that detects harmful inputs by monitoring internal multimodal consistency.

**证据证明什么。** Our results demonstrate that monitoring cross-modal consistency offers an efficient and effective defense for multimodal reasoning.

**证据没有证明什么。** 4.4 Threat Configuration We evaluate FlowGuard under unsafe inputs that include both explicit harmful queries and multimodal jailbreak attacks. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.21600v1#S3 — 3 Methodology; https://arxiv.org/html/2607.21600v1#A1.SS2 — A.2 Baseline Implementation Details。Evaluation：https://arxiv.org/html/2607.21600v1#S4.SS3 — 4.3 Evaluation Benchmarks; https://arxiv.org/html/2607.21600v1#A1.SS1 — A.1 Detailed Experimental Configuration。Limitations / counterevidence：https://arxiv.org/html/2607.21600v1#S6 — 6 Conclusion and Future Work; https://arxiv.org/html/2607.21600v1#S4.SS4 — 4.4 Threat Configuration。

**Artifact boundary。** Exact v1 links https://github.com/Jeybird248/FlowGuard, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 新的安全控制点降低特定失败，但会引入误拒绝、旁路、观测不足或模型/任务迁移问题。 论文自身的边界信号是：4.4 Threat Configuration We evaluate FlowGuard under unsafe inputs that include both explicit harmful queries and multimodal jailbreak attacks.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`PLATFORM-SECURITY`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-21600:end -->

<!-- review:SF-2026-ARXIV-2607-21602:start -->
### Transferable Latency Prediction for Fast LLM Screening on Heterogeneous Edge Devices

<!-- claim:SF-2026-ARXIV-2607-21602:start -->Accurate latency prediction is critical for deploying large language models (LLMs) on heterogeneous edge devices, where inference latency is affected by model architecture, prompt behavior, runtime backend, hardware utilization, dynamic voltage and frequency scaling (DVFS), and thermal variation. This paper presents a runtime-aware latency prediction framework for deployment-oriented LLM selection. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-21602:end -->

**为什么进入候选分母。** 摘要首要问题为“Accurate latency prediction is critical for deploying large language models (LLMs) on heterogeneous edge devices, where inference latency is affected by model architecture, prompt behavior, runtime backend, hardware utilization, dynamic voltage and frequency scaling (DVFS), and thermal variation.”；它改变 observable、对照组、判定粒度或外推边界，可能修正既有评测结论。

**机制与状态边界。** This paper presents a runtime-aware latency prediction framework for deployment-oriented LLM selection.

**证据证明什么。** These results demonstrate that runtime-aware prediction with lightweight calibration can reduce profiling cost and support latency-aware LLM deployment across heterogeneous edge platforms.

**证据没有证明什么。** First, LLM latency depends not only on model structure but also on workload configuration, such as prompt length and output length. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.21602v1#S3 — 3. System Design; https://arxiv.org/html/2607.21602v1#S4 — 4. Experimental Design。Evaluation：https://arxiv.org/html/2607.21602v1#S5 — 5. Results and Analysis; https://arxiv.org/html/2607.21602v1#S4 — 4. Experimental Design。Limitations / counterevidence：https://arxiv.org/html/2607.21602v1#S2.SS3 — 2.3. Limitations of Static Latency Predictors; https://arxiv.org/html/2607.21602v1#S5.SS7 — 5.7. Discussion。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：First, LLM latency depends not only on model structure but also on workload configuration, such as prompt length and output length.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`INFER-SCHEDULING`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-21602:end -->

<!-- review:SF-2026-ARXIV-2607-21604:start -->
### AgentKVShift: Efficient KV Cache Reuse for Agentic Memory Systems

<!-- claim:SF-2026-ARXIV-2607-21604:start -->Memory-augmented LLM agents maintain context across hundreds of interactions through agentic memory systems that actively curate retrieved content with LLM-generated metadata such as summaries, keywords, and tags. From an inference cost standpoint, every retrieval triggers a full re-encoding of these structured memory units into Key-Value (KV) states, which dominates prefill latency. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-21604:end -->

**为什么进入候选分母。** 摘要首要问题为“Memory-augmented LLM agents maintain context across hundreds of interactions through agentic memory systems that actively curate retrieved content with LLM-generated metadata such as summaries, keywords, and tags.”；它改变推理期状态放置、数据移动、执行控制或实时 SLO。

**机制与状态边界。** We present AgentKVShift, a training-free, probe-guided KV residual correction method that operates per retrieved memory unit.

**证据证明什么。** Across four open-source LLMs spanning 3B to 32B parameters and two long-horizon agentic memory benchmarks (long-term dialogue and agentic applications), AgentKVShift achieves near full recompute performance while refreshing only 10-30% of the cache, outperforming baselines at the same recompute ratio.

**证据没有证明什么。** Values in parentheses denote the retention ratio relative to Full Rec. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.21604v1#S3 — 3 Proposed Approach; https://arxiv.org/html/2607.21604v1#A3 — Appendix C Empirical Validation of the Modeling Assumptions。Evaluation：https://arxiv.org/html/2607.21604v1#A1 — Appendix A Extended Experimental Results; https://arxiv.org/html/2607.21604v1#A1.SS1 — A.1 Extended Experimental Set-Up and Reproducibility。Limitations / counterevidence：https://arxiv.org/html/2607.21604v1#A5 — Appendix E Limitations and Future Work; https://arxiv.org/html/2607.21604v1#A1.SS2 — A.2 Extended AMA-Bench Discussion。

**Artifact boundary。** Exact v1 links https://huggingface.co/mistralai/Mistral-7B-Instruct-v0.3, https://github.com/agiresearch/a-mem, https://github.com/EverM0re/LiCoMemory; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更激进的缓存、迁移、并行或专用执行会换取吞吐/时延，同时增加配置依赖、资源压力与回退路径。 论文自身的边界信号是：Values in parentheses denote the retention ratio relative to Full Rec.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`AGENT-MEMORY`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-21604:end -->

<!-- review:SF-2026-ARXIV-2607-21606:start -->
### TILT: Improving Compositional Generation in Diffusion Models with a Model-Intrinsic Reward

<!-- claim:SF-2026-ARXIV-2607-21606:start -->Recent advances in powerful text-to-image generation models have made it increasingly important to develop test-time methods that modify the sampling trajectory to produce images more faithful to complex compositional prompts. We present TILT, a training-free framework for compositional text-to-image generation via test-time reward alignment. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-21606:end -->

**为什么进入候选分母。** 摘要首要问题为“Recent advances in powerful text-to-image generation models have made it increasingly important to develop test-time methods that modify the sampling trajectory to produce images more faithful to complex compositional prompts.”；它改变训练信号、capacity 或 update ownership，而非只报告任务精度。

**机制与状态边界。** We present TILT, a training-free framework for compositional text-to-image generation via test-time reward alignment.

**证据证明什么。** Experiments on prompts from T2ICompBench show that our method improves compositional alignment while preserving image quality compared to previous baselines.

**证据没有证明什么。** For future work, our formulation is modality-agnostic and depends only on conditional score estimation and factorizable conditioning variables. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.21606v1#S3 — 3 Method; https://arxiv.org/html/2607.21606v1#A5 — Appendix E More Implementation Details。Evaluation：https://arxiv.org/html/2607.21606v1#A6 — Appendix F More Qualitative Results; https://arxiv.org/html/2607.21606v1#S4 — 4 Experiments。Limitations / counterevidence：https://arxiv.org/html/2607.21606v1#S6 — 6 Conclusion。

**Artifact boundary。** Exact v1 links https://aclanthology.org/2020.acl-demos.14/, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更密集或更定向的训练信号改善样本效率，但会增加 verifier 偏差、分布迁移和优化耦合。 论文自身的边界信号是：For future work, our formulation is modality-agnostic and depends only on conditional score estimation and factorizable conditioning variables.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`MULTIMODAL-GENERATIVE-PARADIGMS`；evidence-stage relation：`alternative_branch`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-21606:end -->

<!-- review:SF-2026-ARXIV-2607-21609:start -->
### Coupled Hierarchical Search over Topology and Execution for Agentic Workflow Synthesis

<!-- claim:SF-2026-ARXIV-2607-21609:start -->Although structured workflows empower Large Language Models (LLMs) to tackle complex problems, automating their creation is severely hindered by a vast combinatorial search space, frequently resulting in inflexible and resource-heavy offline training dependencies. To address this, we conceptualize workflow generation as an intertwined topology-and-execution search paradigm, where the broader topological layer dictates subtask boundaries and lower-level execution outcomes actively reshape the topology itself. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-21609:end -->

**为什么进入候选分母。** 摘要首要问题为“Although structured workflows empower Large Language Models (LLMs) to tackle complex problems, automating their creation is severely hindered by a vast combinatorial search space, frequently resulting in inflexible and resource-heavy offline training dependencies.”；它把 context、memory、能力或进度变成持久且可验证的 agent state。

**机制与状态边界。** Building on this foundation, we introduce HierFlow, a training-free, test-time hierarchical search architecture that automates agentic workflow design by merging feedback-guided topology adjustments with a fast, MCTS-inspired tree search for sub-workflow optimization.

**证据证明什么。** Comprehensive testing across question answering, mathematical reasoning, and code generation benchmarks confirms that HierFlow consistently outperforms strong baselines, delivering an optimal balance of high-quality results and computational efficiency without any additional training overhead.

**证据没有证明什么。** The goal is not to prove an unconditional asymptotic speedup under idealized independence assumptions, but to characterize when hierarchical decomposition and proxy-based gating are expected to be useful. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.21609v1#S2 — 2 Methodology; https://arxiv.org/html/2607.21609v1#A3 — Appendix C Algorithmic Details of HierFlow。Evaluation：https://arxiv.org/html/2607.21609v1#A4.SS3 — D.3 Detailed Ablation Analysis; https://arxiv.org/html/2607.21609v1#A4 — Appendix D Additional Experimental Details。Limitations / counterevidence：https://arxiv.org/html/2607.21609v1#A2 — Appendix B Proofs and Additional Theoretical Discussions; https://arxiv.org/html/2607.21609v1#S4 — 4 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 显式 agent state 改善恢复与控制，但增加状态陈旧、错误提交、跨轮污染和一致性责任。 论文自身的边界信号是：The goal is not to prove an unconditional asymptotic speedup under idealized independence assumptions, but to characterize when hierarchical decomposition and proxy-based gating are expected to be useful.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`AGENT-WORKFLOW`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-21609:end -->

<!-- review:SF-2026-ARXIV-2607-21610:start -->
### SCOPE and SCION: A Benchmark and an Auditable Reference Pipeline for Schema Induction and Fusion from Text

<!-- claim:SF-2026-ARXIV-2607-21610:start -->Schema graphs are an upstream bottleneck of schema-grounded information extraction and knowledge graph construction, yet most extraction systems assume the schema is already available. We introduce SCOPE (Schema Construction and Ontology-induction Pipeline Evaluation), a train-text-only benchmark for corpus-to-schema induction and optional schema fusion from raw text, built from 24 public information extraction sources (15 RE and 9 EE) normalized into evaluation-only gold schema graphs; its core event-extraction target covers event types and within-event argument roles, with inter-event links reported separately. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-21610:end -->

**为什么进入候选分母。** 摘要首要问题为“Schema graphs are an upstream bottleneck of schema-grounded information extraction and knowledge graph construction, yet most extraction systems assume the schema is already available.”；它把 evidence identity、lineage、conflict 或 commit 变成显式系统状态。

**机制与状态边界。** Schema graphs are an upstream bottleneck of schema-grounded information extraction and knowledge graph construction, yet most extraction systems assume the schema is already available.

**证据证明什么。** These results are reported against normalized typed-edge targets rather than as claims that induced schemas surpass human ontology design; the release includes evidence-linked outputs, parse/fallback logs, candidate retention/merging logs, run manifests, code, and benchmark packages at https://github.com/wandugu/paper_scion.

**证据没有证明什么。** Future work will expand SCOPE beyond the current 24-source core suite, add inter-event temporal/causal links to the core EE benchmark, strengthen the fusion track with larger human-audited mapping sets, and study how induced/fused schemas affect downstream schema-grounded extraction quality and long-term schema maintenance under domain drift. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.21610v1#S4 — 4 SCION Method; https://arxiv.org/html/2607.21610v1#A6.SS6 — F.6 SCION-RL: Replacing the Schema Engineer with a Trained Compact Model。Evaluation：https://arxiv.org/html/2607.21610v1#S5.SS7 — 5.7 Results and Analysis; https://arxiv.org/html/2607.21610v1#A3 — Appendix C Additional Details of the SCOPE Benchmark。Limitations / counterevidence：https://arxiv.org/html/2607.21610v1#A7.SS4 — G.4 Failure Case: Polysemy and Conservative Rejection; https://arxiv.org/html/2607.21610v1#S6 — 6 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/wandugu/paper_scion, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 显式 evidence state 提高可追溯性，但新增 lineage、冲突、commit 与恢复语义，状态本身也必须被验证。 论文自身的边界信号是：Future work will expand SCOPE beyond the current 24-source core suite, add inter-event temporal/causal links to the core EE benchmark, strengthen the fusion track with larger human-audited mapping sets, and study how induced/fused schemas affect downstream schema-grounded extraction quality and long-term schema maintenance under domain drift.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`PLATFORM-EVALUATION-SYSTEM`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-21610:end -->

<!-- review:SF-2026-ARXIV-2607-21612:start -->
### Procedural Knowledge Is Not Low-Rank: Why LoRA Fails to Internalize Multi-Step Procedures

<!-- claim:SF-2026-ARXIV-2607-21612:start -->Parameter-efficient fine-tuning methods like LoRA have become the default for adapting large language models, succeeding across instruction following, style transfer, and factual adaptation. We show that for procedural knowledge--the ability to follow multi-step procedures with conditional branching through to terminal states--LoRA fails to match full fine-tuning at the ranks where it retains its efficiency advantage. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-21612:end -->

**为什么进入候选分母。** 摘要首要问题为“Parameter-efficient fine-tuning methods like LoRA have become the default for adapting large language models, succeeding across instruction following, style transfer, and factual adaptation.”；它改变训练信号、capacity 或 update ownership，而非只报告任务精度。

**机制与状态边界。** In a systematic ablation (r = 16--128) on a procedural travel booking task (14 nodes), all LoRA configurations fail uniformly (task success &lt;= 2.54 vs.

**证据证明什么。** Quadrupling rank from 32 to 128 provides marginal improvement but does not close the gap.

**证据没有证明什么。** The LoRA rank ablation (§ 3.1 ) shows that low-rank parameter updates cannot capture procedural knowledge on travel, and the cross-domain replication confirms this on Zoom and insurance at 8B—with the largest gap on the most complex procedure. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.21612v1#S2 — 2 Method。Evaluation：https://arxiv.org/html/2607.21612v1#S2.SS4 — 2.4 Evaluation Conditions; https://arxiv.org/html/2607.21612v1#S2.SS5 — 2.5 Evaluation Protocol。Limitations / counterevidence：https://arxiv.org/html/2607.21612v1#S3.SS1 — 3.1 Behavioral Failure Across Ranks; https://arxiv.org/html/2607.21612v1#S4 — 4 Discussion。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更密集或更定向的训练信号改善样本效率，但会增加 verifier 偏差、分布迁移和优化耦合。 论文自身的边界信号是：The LoRA rank ablation (§ 3.1 ) shows that low-rank parameter updates cannot capture procedural knowledge on travel, and the cross-domain replication confirms this on Zoom and insurance at 8B—with the largest gap on the most complex procedure.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`TRAIN-LORA`；evidence-stage relation：`corrective_evidence`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-21612:end -->

<!-- review:SF-2026-ARXIV-2607-21613:start -->
### The Hard Decision Layer: Evidence for Committed Inference in Transformers

<!-- claim:SF-2026-ARXIV-2607-21613:start -->We investigate where and how transformer-based language models commit to predictions in multiple-choice question answering. We identify the _Hard Decision Layer_ (HDL), a natural architectural property where answer option rankings stabilize abruptly during inference. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-21613:end -->

**为什么进入候选分母。** 摘要首要问题为“We investigate where and how transformer-based language models commit to predictions in multiple-choice question answering.”；它提出可跨 workload 讨论的表示、状态或计算机制，并暴露旧方案边界。

**机制与状态边界。** Systematic ablations on label formats and problem complexity confirm the phenomenon is fundamental to model architecture.

**证据证明什么。** Our results reveal striking accuracy improvements at the HDL: up to +0.61 (Qwen on CommonsenseQA), after which performance stabilizes.

**证据没有证明什么。** Additionally, our analysis focuses only on the canonical answer labels (A/B/C/D), but intermediate layers may activate alternative surface forms that correspond to the same option (e.g., “b”, “second”, “B)” and other variants), which are not accounted for in the current analysis. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.21613v1#S3 — 3 Methodology; https://arxiv.org/html/2607.21613v1#A1 — Appendix A Prompt, Models and Datasets。Evaluation：https://arxiv.org/html/2607.21613v1#A3 — Appendix C Supplementary Results for Finding 1; https://arxiv.org/html/2607.21613v1#A4 — Appendix D Supplementary Results for Finding 2。Limitations / counterevidence：https://arxiv.org/html/2607.21613v1#S5 — 5 Discussion; https://arxiv.org/html/2607.21613v1#S6 — 6 Limitations。

**Artifact boundary。** Exact v1 links https://github.com/Mystic-Slice/hard-decision-layer, https://huggingface.co/ibm-granite/granite-3.3-2b-instruct, https://huggingface.co/mistralai/Mistral-7B-Instruct-v0.3; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 新表示或状态机制扩大能力边界，但带来额外训练、状态管理、稳定性或泛化假设。 论文自身的边界信号是：Additionally, our analysis focuses only on the canonical answer labels (A/B/C/D), but intermediate layers may activate alternative surface forms that correspond to the same option (e.g., “b”, “second”, “B)” and other variants), which are not accounted for in the current analysis.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`WORLDVIEW-LLM-INTELLIGENCE`；evidence-stage relation：`alternative_branch`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-21613:end -->

<!-- review:SF-2026-ARXIV-2607-21616:start -->
### Lost in Context: Addressing Context Anxiety in Large Language Models

<!-- claim:SF-2026-ARXIV-2607-21616:start -->Conventional wisdom suggests that reasoning models fail when problems exceed their capabilities. However, we find that frontier reasoning models sometimes possess the necessary capabilities to solve problems but fail due to premature self-doubt -- a phenomenon informally known as context anxiety. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-21616:end -->

**为什么进入候选分母。** 摘要首要问题为“Conventional wisdom suggests that reasoning models fail when problems exceed their capabilities.”；它改变 observable、对照组、判定粒度或外推边界，可能修正既有评测结论。

**机制与状态边界。** We provide the first systematic study of context anxiety, demonstrating that it arises, in part, from a model's inability to accurately estimate the tokens required to complete a task.

**证据证明什么。** Building on this analysis, we further show that models can learn alternative strategies for solving long-horizon problems without exhibiting context anxiety, suggesting that performance improvements may be achievable not through scaling model capabilities, but by improving models' ability to accurately assess and adapt to their own limitations.

**证据没有证明什么。** Future work should evaluate whether similar behavioral patterns arise across broader task classes and develop detection methods that do not depend on explicit self-reports. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.21616v1#A4.SS1 — D.1 Motivation and Task Design; https://arxiv.org/html/2607.21616v1#S3 — 3 Method。Evaluation：https://arxiv.org/html/2607.21616v1#A6 — Appendix F Sensitivity Analysis of the Context Anxiety Detector; https://arxiv.org/html/2607.21616v1#S4 — 4 Results。Limitations / counterevidence：https://arxiv.org/html/2607.21616v1#S5 — 5 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：Future work should evaluate whether similar behavioral patterns arise across broader task classes and develop detection methods that do not depend on explicit self-reports.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`AGENT-CONTEXT`；evidence-stage relation：`corrective_evidence`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-21616:end -->

<!-- review:SF-2026-ARXIV-2607-21617:start -->
### Do VLMs Read or Rewrite? On Transcription Faithfulness in Vision-Language Models

<!-- claim:SF-2026-ARXIV-2607-21617:start -->Vision Language Models (VLMs) are increasingly used in place of traditional OCR pipelines for document understanding. In this paper, we show they do not always act as faithful transcribers: when text is imperfect, they often tend to rewrite it into a more plausible form - a behavior that clean-text OCR benchmarks cannot detect. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-21617:end -->

**为什么进入候选分母。** 摘要首要问题为“Vision Language Models (VLMs) are increasingly used in place of traditional OCR pipelines for document understanding.”；它改变 observable、对照组、判定粒度或外推边界，可能修正既有评测结论。

**机制与状态边界。** We use the benchmark to evaluate 15 systems spanning general-purpose VLMs, OCR-specialized VLMs, and traditional OCR pipelines.

**证据证明什么。** In this paper, we show they do not always act as faithful transcribers: when text is imperfect, they often tend to rewrite it into a more plausible form - a behavior that clean-text OCR benchmarks cannot detect.

**证据没有证明什么。** Probing Qwen3-VL-4B layer by layer shows that rewriting depends on how far the perturbation shifts the model’s internal representation, not on how much attention the model allocates to the perturbed word. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.21617v1#A2 — Appendix B Models; https://arxiv.org/html/2607.21617v1#A6.SS1 — F.1 Effect of model size.。Evaluation：https://arxiv.org/html/2607.21617v1#S4 — 4 Experimental Results; https://arxiv.org/html/2607.21617v1#A6 — Appendix F Ablation Studies。Limitations / counterevidence：https://arxiv.org/html/2607.21617v1#A3 — Appendix C Failure Detection and Exclusion; https://arxiv.org/html/2607.21617v1#S5 — 5 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/mindee/doctr, https://huggingface.co/blog/lightonai/lightonocr, https://github.com/arXiv/html_feedback/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：Probing Qwen3-VL-4B layer by layer shows that rewriting depends on how far the perturbation shifts the model’s internal representation, not on how much attention the model allocates to the perturbed word.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`MULTIMODAL-REPRESENTATION`；evidence-stage relation：`corrective_evidence`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-21617:end -->

<!-- review:SF-2026-ARXIV-2607-21619:start -->
### Adversarial Style Optimization: Enhancing VLM Jailbreaks by GRPO-based Stylistic Triggers Optimization

<!-- claim:SF-2026-ARXIV-2607-21619:start -->Multimodal Large Language Models (MLLMs) have achieved impressive performance, but their safety alignment remains vulnerable to jailbreak attacks. Existing content-based jailbreaks are often inconsistent and show unsatisfying performance against the rapidly evolving MLLMs, failing to exploit non-content-based vulnerabilities. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-21619:end -->

**为什么进入候选分母。** 摘要首要问题为“Multimodal Large Language Models (MLLMs) have achieved impressive performance, but their safety alignment remains vulnerable to jailbreak attacks.”；它改变执行安全的 trust boundary、guard 或 failure detection。

**机制与状态边界。** Based on this finding, we propose Adversarial Style Optimization (ASO), a plug-and-play enhancement module to amplify existing visual jailbreaks.

**证据证明什么。** Multimodal Large Language Models (MLLMs) have achieved impressive performance, but their safety alignment remains vulnerable to jailbreak attacks.

**证据没有证明什么。** Our findings prove VLM safety is a function of how (style) not just what (content), revealing a larger attack surface and the need for defenses beyond content-centric filters. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.21619v1#S2.SS1 — 2.1 Multimodal Large Language Models (MLLMs)。Evaluation：https://arxiv.org/html/2607.21619v1#S5 — 5 Experiments; https://arxiv.org/html/2607.21619v1#S5.SS1 — 5.1 Experimental Setup。Limitations / counterevidence：https://arxiv.org/html/2607.21619v1#S6 — 6 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/bingjunluo/ASO, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 新的安全控制点降低特定失败，但会引入误拒绝、旁路、观测不足或模型/任务迁移问题。 论文自身的边界信号是：Our findings prove VLM safety is a function of how (style) not just what (content), revealing a larger attack surface and the need for defenses beyond content-centric filters.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`PLATFORM-SECURITY`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-21619:end -->

<!-- review:SF-2026-ARXIV-2607-21623:start -->
### Cloud-Native Evaluation-as-a-Service: A Microservices Architecture for Scalable AI Monitoring with Conformal Guarantees

<!-- claim:SF-2026-ARXIV-2607-21623:start -->We present EaaS, a cloud-native reference architecture that operationalizes AI evaluation methods as six stateless Kubernetes microservices: conformal prediction with finite-sample-corrected Adaptive Prediction Sets, calibration assessment, drift detection via RFF-approximated Maximum Mean Discrepancy, fairness monitoring with bootstrap confidence intervals, a DAG-based pipeline orchestrator, and a result storage API. We validate four key methodological concerns. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-21623:end -->

**为什么进入候选分母。** 摘要首要问题为“We present EaaS, a cloud-native reference architecture that operationalizes AI evaluation methods as six stateless Kubernetes microservices: conformal prediction with finite-sample-corrected Adaptive Prediction Sets, calibration assessment, drift detection via RFF-approximated Maximum Mean Discrepancy, fairness monitoring with bootstrap confidence intervals, a DAG-based pipeline orchestrator, and a result storage API”；它把 evidence identity、lineage、conflict 或 commit 变成显式系统状态。

**机制与状态边界。** We present EaaS, a cloud-native reference architecture that operationalizes AI evaluation methods as six stateless Kubernetes microservices: conformal prediction with finite-sample-corrected Adaptive Prediction Sets, calibration assessment, drift detection via RFF-approximated Maximum Mean Discrepancy, fairness monitoring with bootstrap confidence intervals, a DAG-based pipeline orchestrator, and a result storage API.

**证据证明什么。** Third, RFF-MMD achieves 100% detection power for mild and severe drift at the median heuristic bandwidth, with Type I error between 5-8.5%.

**证据没有证明什么。** The KS test with BH correction correctly identifies all 5 drifted features at magnitude with zero false positives, while MMD detects multivariate distributional shifts that per-feature tests cannot capture. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.21623v1#S3 — 3 Methodology; https://arxiv.org/html/2607.21623v1#S3.SS1 — 3.1 Architecture。Evaluation：https://arxiv.org/html/2607.21623v1#S3.SS2 — 3.2 Evaluation Services; https://arxiv.org/html/2607.21623v1#S3.SS4 — 3.4 Experimental Design。Limitations / counterevidence：https://arxiv.org/html/2607.21623v1#S5 — 5 Discussion; https://arxiv.org/html/2607.21623v1#S6 — 6 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 显式 evidence state 提高可追溯性，但新增 lineage、冲突、commit 与恢复语义，状态本身也必须被验证。 论文自身的边界信号是：The KS test with BH correction correctly identifies all 5 drifted features at magnitude with zero false positives, while MMD detects multivariate distributional shifts that per-feature tests cannot capture.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`PLATFORM-EVALUATION-SYSTEM`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-21623:end -->

<!-- review:SF-2026-ARXIV-2607-21624:start -->
### FBLayout: Optimizing Memory Layout for Efficient LLM Finetuning on Mobile GPUs

<!-- claim:SF-2026-ARXIV-2607-21624:start -->Transformer-based models have enabled unprecedented capabilities across language, vision, and multimodal tasks. On-device fine-tuning of transformer models offers a privacy-preserving path to personalized AI, yet remains inefficient on mobile GPUs due to severe memory constraints and frequent layout transformations in attention mechanism during training. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-21624:end -->

**为什么进入候选分母。** 摘要首要问题为“Transformer-based models have enabled unprecedented capabilities across language, vision, and multimodal tasks.”；它改变资源计量、分配、路由或迁移的控制权与约束。

**机制与状态边界。** To overcome this, we propose FBLayout, a layout-aware framework that co-designs tensor organization with mobile GPU platforms.

**证据证明什么。** Evaluations on seven transformer models across different mobile phones (including ARM Mali and Qualcomm Adreno GPUs) show that FBLayout achieves 2.2-5.7x speedup over MNN, TFLite, and TVM, while significantly improving cache efficiency and reducing memory footprint, enabling practical on-device large model fine-tuning.

**证据没有证明什么。** It is worth noting that while mobile NPUs offer significantly higher computing capability, they lack backpropagation support, operate at limited precision (typically int8) ( Xu et al., 2022 ) , and provide only fixed-architecture inference acceleration ( Mahurin, 2023 ) . 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.21624v1#S4 — 4. Design of FBLayout; https://arxiv.org/html/2607.21624v1#S5.SS5 — 5.5. System Overhead Analysis。Evaluation：https://arxiv.org/html/2607.21624v1#S3 — 3. Problem Formulation and Analysis; https://arxiv.org/html/2607.21624v1#S5 — 5. Evaluation。Limitations / counterevidence：https://arxiv.org/html/2607.21624v1#S2.SS3 — 2.3. Limitations of Existing Solutions.; https://arxiv.org/html/2607.21624v1#S7 — 7. Discussion。

**Artifact boundary。** Exact v1 links https://github.com/alibaba/MNN/blob/2.3.0/source/core/BufferAllocator.cpp, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 动态资源控制提高利用率，但增加测量误差、迁移开销、租户公平和控制稳定性问题。 论文自身的边界信号是：It is worth noting that while mobile NPUs offer significantly higher computing capability, they lack backpropagation support, operate at limited precision (typically int8) ( Xu et al., 2022 ) , and provide only fixed-architecture inference acceleration ( Mahurin, 2023 ) .

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`TRAIN-LORA`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-21624:end -->

<!-- review:SF-2026-ARXIV-2607-21625:start -->
### Trajectory-Aware Retrieval Agents for Temporal Decision- Making

<!-- claim:SF-2026-ARXIV-2607-21625:start -->We study the problem of decision-making from long-form, temporally structured text using large language model (LLM) agents. Standard retrievalaugmented generation (RAG) pipelines fragment chronological context into isolated snippets, discarding the temporal structure that is often critical for correct downstream decisions. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-21625:end -->

**为什么进入候选分母。** 摘要首要问题为“We study the problem of decision-making from long-form, temporally structured text using large language model (LLM) agents.”；它把 context、memory、能力或进度变成持久且可验证的 agent state。

**机制与状态边界。** We introduce TLM (Trajectory Language Model), a closed-loop agentic framework that iteratively refines the evidence set using SHAP-guided feedback.

**证据证明什么。** TLM substantially outperforms both zero-shot LLM baselines and standard retrieval-augmented approaches on the medical task, and yields consistent, economically meaningful gains on the two financial tasks.

**证据没有证明什么。** Exact v1 does not disclose a dedicated generalization or deployment guarantee beyond its stated evaluation scope. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.21625v1#S4 — 4 Method; https://arxiv.org/html/2607.21625v1#S4.SS2 — 4.2 Stage 2: Latent Growth Curve Modeling。Evaluation：https://arxiv.org/html/2607.21625v1#S5 — 5 Experiments。Limitations / counterevidence：https://arxiv.org/html/2607.21625v1#S6 — 6 Discussion。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 显式 agent state 改善恢复与控制，但增加状态陈旧、错误提交、跨轮污染和一致性责任。 论文自身的边界信号是：Exact v1 does not disclose a dedicated generalization or deployment guarantee beyond its stated evaluation scope.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`AGENT-RAG`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-21625:end -->

<!-- review:SF-2026-ARXIV-2607-21627:start -->
### Do Modules Stay in Their Lane? Role Drift in Compound LLM Systems

<!-- claim:SF-2026-ARXIV-2607-21627:start -->End-to-end reinforcement learning can improve the accuracy of compound LLM systems, but it does not constrain how modules divide labor internally. We identify Role Drift, a failure mode in which modules preserve or improve end-task performance while deviating from their assigned roles through role-violating shortcuts that remain invisible to system-level evaluation. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-21627:end -->

**为什么进入候选分母。** 摘要首要问题为“End-to-end reinforcement learning can improve the accuracy of compound LLM systems, but it does not constrain how modules divide labor internally.”；它改变 observable、对照组、判定粒度或外推边界，可能修正既有评测结论。

**机制与状态边界。** End-to-end reinforcement learning can improve the accuracy of compound LLM systems, but it does not constrain how modules divide labor internally.

**证据证明什么。** End-to-end reinforcement learning can improve the accuracy of compound LLM systems, but it does not constrain how modules divide labor internally.

**证据没有证明什么。** The underlying ideas, however, are not specific to LLMs. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.21627v1#S1 — 1 Introduction; https://arxiv.org/html/2607.21627v1#S2 — 2 Related Work。Evaluation：https://arxiv.org/html/2607.21627v1#S4 — 4 Experiments; https://arxiv.org/html/2607.21627v1#S4.SS1 — 4.1 Experimental Setup。Limitations / counterevidence：https://arxiv.org/html/2607.21627v1#S6 — 6 Limitations and Future Work; https://arxiv.org/html/2607.21627v1#S4.SS5 — 4.5 Discussion: Why Prevent Role Drift?。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：The underlying ideas, however, are not specific to LLMs.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`AGENT-PLATFORM`；evidence-stage relation：`corrective_evidence`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-21627:end -->

<!-- review:SF-2026-ARXIV-2607-21632:start -->
### A Consensus-Based Framework for Relative Preference Evaluation of Large Language Models

<!-- claim:SF-2026-ARXIV-2607-21632:start -->Traditional benchmarks for LLMs primarily rely on static datasets and objective scoring metrics, which often fail to capture differences in response quality when multiple answers are acceptable. In such settings, correctness alone is insufficient to distinguish between responses that vary in clarity, completeness, and usefulness. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-21632:end -->

**为什么进入候选分母。** 摘要首要问题为“Traditional benchmarks for LLMs primarily rely on static datasets and objective scoring metrics, which often fail to capture differences in response quality when multiple answers are acceptable.”；它改变 observable、对照组、判定粒度或外推边界，可能修正既有评测结论。

**机制与状态边界。** This framework provides a scalable, model-driven method for comparative evaluation, offering an alternative perspective on response quality in scenarios where multiple valid answers exist.

**证据证明什么。** However, we emphasize that these results reflect inter-model preference alignment rather than objective correctness or human judgment.

**证据没有证明什么。** Importantly, this framework does not claim to measure objective intelligence or alignment with human judgment. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.21632v1#S2.SS1 — 2.1 LLM-as-a-Judge Frameworks; https://arxiv.org/html/2607.21632v1#S2.SS2 — 2.2 Consensus-Based and Independent Aggregation Approaches.。Evaluation：https://arxiv.org/html/2607.21632v1#S2.SS3 — 2.3 Multi-Agent and Consensus-Based Evaluation; https://arxiv.org/html/2607.21632v1#S2.SS4 — 2.4 Reliability, Calibration, and Meta-Evaluation of Judges.。Limitations / counterevidence：https://arxiv.org/html/2607.21632v1#S5 — 5 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：Importantly, this framework does not claim to measure objective intelligence or alignment with human judgment.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`PLATFORM-EVALUATION-SYSTEM`；evidence-stage relation：`principle_reuse`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-21632:end -->

<!-- review:SF-2026-ARXIV-2607-21635:start -->
### Toward User-Conditioned Evaluation of Personal LLM Agents under Temporal Interventions

<!-- claim:SF-2026-ARXIV-2607-21635:start -->Personal agents maintain memories, learned skills, tool configurations, and policy state that evolve with each user. Existing agent benchmarks often evaluate these capabilities in isolation: tool benchmarks test invocation under fixed APIs, memory benchmarks test recall or forgetting, and safety benchmarks test static policy compliance. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-21635:end -->

**为什么进入候选分母。** 摘要首要问题为“Personal agents maintain memories, learned skills, tool configurations, and policy state that evolve with each user.”；它改变 observable、对照组、判定粒度或外推边界，可能修正既有评测结论。

**机制与状态边界。** Existing agent benchmarks often evaluate these capabilities in isolation: tool benchmarks test invocation under fixed APIs, memory benchmarks test recall or forgetting, and safety benchmarks test static policy compliance.

**证据证明什么。** The result is a concrete design requirement for future personal-agent evaluation, with metrics used as reporting tools for that requirement.

**证据没有证明什么。** A useful next benchmark should provide profile states, event scripts, dependency annotations, oracle checks, and per-user regression suites, so that other groups can test whether the same update creates different failures for different users. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.21635v1#S5 — 5. Metrics and Minimal Benchmark Design。Evaluation：https://arxiv.org/html/2607.21635v1#S4 — 4. Gap Analysis; https://arxiv.org/html/2607.21635v1#S5 — 5. Metrics and Minimal Benchmark Design。Limitations / counterevidence：https://arxiv.org/html/2607.21635v1#S6 — 6. Open Challenges and Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：A useful next benchmark should provide profile states, event scripts, dependency annotations, oracle checks, and per-user regression suites, so that other groups can test whether the same update creates different failures for different users.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`AGENT-PLATFORM`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-21635:end -->

<!-- review:SF-2026-ARXIV-2607-21641:start -->
### Tool-Guided Retrieval-Augmented Repair for Securing LLM-Generated C Code

<!-- claim:SF-2026-ARXIV-2607-21641:start -->Large language models can generate C code from natural-language descriptions, but resulting programs often contain security vulnerabilities and compilation errors, posing risks for embedded and resource-constrained systems. This work investigates how feedback and retrieval improve reliability of LLM-generated C code. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-21641:end -->

**为什么进入候选分母。** 摘要首要问题为“Large language models can generate C code from natural-language descriptions, but resulting programs often contain security vulnerabilities and compilation errors, posing risks for embedded and resource-constrained systems.”；它改变执行安全的 trust boundary、guard 或 failure detection。

**机制与状态边界。** We present an analysis-and-repair workflow that combines compilation diagnostics, CodeQL static analysis, and KLEE symbolic execution with retrieval of prior repair patterns for iterative refinement.

**证据证明什么。** These results show that integrating lightweight analysis tools can improve the safety of LLM-generated code for embedded development.

**证据没有证明什么。** These findings show that incorporating lightweight analysis tools into the generation loop improves build success and security, with embedded evaluation and component ablations left for future work. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.21641v1#S3 — 3 Approach。Evaluation：https://arxiv.org/html/2607.21641v1#S4 — 4 Experiment Results; https://arxiv.org/html/2607.21641v1#S3.SS2 — 3.2 Compilation and Static Analysis。Limitations / counterevidence：https://arxiv.org/html/2607.21641v1#S5 — 5 Future Work; https://arxiv.org/html/2607.21641v1#S6 — 6 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 新的安全控制点降低特定失败，但会引入误拒绝、旁路、观测不足或模型/任务迁移问题。 论文自身的边界信号是：These findings show that incorporating lightweight analysis tools into the generation loop improves build success and security, with embedded evaluation and component ablations left for future work.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`AGENT-TOOL-CALLING`；evidence-stage relation：`principle_reuse`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-21641:end -->

<!-- review:SF-2026-ARXIV-2607-21642:start -->
### CARE: Pre-Execution Command Verification for Shell-Executing LLM Agents

<!-- claim:SF-2026-ARXIV-2607-21642:start -->Large Language Model (LLM) agents are increasingly used for coding and terminal automation, making shell-command dispatch a high-stakes runtime control point. We study command-level pre-execution mediation for individual shell commands produced by LLM agents under bounded path context. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-21642:end -->

**为什么进入候选分母。** 摘要首要问题为“Large Language Model (LLM) agents are increasingly used for coding and terminal automation, making shell-command dispatch a high-stakes runtime control point.”；它改变执行安全的 trust boundary、guard 或 failure detection。

**机制与状态边界。** We present CARE (Canonicalization, Attribution, and Resolution Engine), a shell-specific, static-first verifier for individual shell commands before execution.

**证据证明什么。** Overall, command-level shell mediation can reduce dispatch-boundary risk for LLM agents while preserving most benign workflows.

**证据没有证明什么。** The key contribution is therefore not only higher headline detection, but a practical operating spectrum: a fully static mode for maximal conservatism and a selective-resolution mode that recovers benign utility at modest latency cost. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.21642v1#S3 — III Methodology; https://arxiv.org/html/2607.21642v1#S2 — II Threat Model。Evaluation：https://arxiv.org/html/2607.21642v1#S4 — IV Experimental Setup; https://arxiv.org/html/2607.21642v1#S5 — V Results。Limitations / counterevidence：https://arxiv.org/html/2607.21642v1#S2 — II Threat Model; https://arxiv.org/html/2607.21642v1#S6 — VI Discussion。

**Artifact boundary。** Exact v1 links https://github.com/prisma-research/CARE, https://www.anthropic.com/product/claude-code, https://openai.com/index/introducing-codex/; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 新的安全控制点降低特定失败，但会引入误拒绝、旁路、观测不足或模型/任务迁移问题。 论文自身的边界信号是：The key contribution is therefore not only higher headline detection, but a practical operating spectrum: a fully static mode for maximal conservatism and a selective-resolution mode that recovers benign utility at modest latency cost.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`AGENT-TOOL-CALLING`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-21642:end -->

<!-- review:SF-2026-ARXIV-2607-21646:start -->
### Adjustment Speed as a Safety Constraint for Nonstationary Reinforcement Learning

<!-- claim:SF-2026-ARXIV-2607-21646:start -->Ensuring safety in reinforcement learning under nonstationarity requires determining whether a learning system can safely adapt to forecasted environmental change within the required recovery horizon. Existing safe reinforcement learning methods typically assume stationary environments and do not explicitly consider adaptation speed as a safety concern. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-21646:end -->

**为什么进入候选分母。** 摘要首要问题为“Ensuring safety in reinforcement learning under nonstationarity requires determining whether a learning system can safely adapt to forecasted environmental change within the required recovery horizon.”；它改变执行安全的 trust boundary、guard 或 failure detection。

**机制与状态边界。** Existing safe reinforcement learning methods typically assume stationary environments and do not explicitly consider adaptation speed as a safety concern.

**证据证明什么。** These results support adaptation feasibility as a practical safety principle for reinforcement learning under nonstationarity and demonstrate that proactive intervention can improve safety during periods of environmental change.

**证据没有证明什么。** Future states or regions may become unsafe when ordinary adaptation cannot keep pace with the required adaptation demand. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.21646v1#S4 — 4 Method; https://arxiv.org/html/2607.21646v1#A2 — Appendix B Implementation Details。Evaluation：https://arxiv.org/html/2607.21646v1#A3 — Appendix C Additional Experimental and Calibration Details; https://arxiv.org/html/2607.21646v1#S5 — 5 Experiments。Limitations / counterevidence：https://arxiv.org/html/2607.21646v1#S6 — 6 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 新的安全控制点降低特定失败，但会引入误拒绝、旁路、观测不足或模型/任务迁移问题。 论文自身的边界信号是：Future states or regions may become unsafe when ordinary adaptation cannot keep pace with the required adaptation demand.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`TRAIN-GRPO`；evidence-stage relation：`corrective_evidence`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-21646:end -->

<!-- review:SF-2026-ARXIV-2607-21653:start -->
### Molt: A Scalable PyTorch-Native Training Framework for Agentic Reinforcement Learning

<!-- claim:SF-2026-ARXIV-2607-21653:start -->Agentic reinforcement learning research is constant algorithm modification, new estimators, new pipeline stages, new rollout schemes, and in mainstream frameworks each change threads through layers of trainer, distributed backend, and rollout glue: the cost lands on the researcher at every iteration. Molt is a PyTorch-native training framework built to keep that cost small: a codebase compact and clean enough for a researcher to hold in their head, and for an AI coding assistant to read and reason about in its entirety, so the algorithm flow can be traced and changed end to end. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-21653:end -->

**为什么进入候选分母。** 摘要首要问题为“Agentic reinforcement learning research is constant algorithm modification, new estimators, new pipeline stages, new rollout schemes, and in mainstream frameworks each change threads through layers of trainer, distributed backend, and rollout glue: the cost lands on the researcher at every iteration.”；它改变训练信号、capacity 或 update ownership，而非只报告任务精度。

**机制与状态边界。** Molt is a PyTorch-native training framework built to keep that cost small: a codebase compact and clean enough for a researcher to hold in their head, and for an AI coding assistant to read and reason about in its entirety, so the algorithm flow can be traced and changed end to end.

**证据证明什么。** Molt is open source and provides recipes and containers at https://github.com/NVIDIA-NeMo/labs-molt.

**证据没有证明什么。** 6 Future Work Molt already runs the full asynchronous loop, rollout, weight refit, and optimizer step, end to end on a 700B MoE at expert parallelism 256, on the same lean loop it runs at 4B. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.21653v1#S2 — 2 Design Principles; https://arxiv.org/html/2607.21653v1#S3 — 3 The System: Four Concepts, One Loop。Evaluation：https://arxiv.org/html/2607.21653v1#S4 — 4 Evaluation: Does Leanness Cost Throughput?。Limitations / counterevidence：https://arxiv.org/html/2607.21653v1#S6 — 6 Future Work; https://arxiv.org/html/2607.21653v1#S7 — 7 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/NVIDIA-NeMo/labs-molt, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更密集或更定向的训练信号改善样本效率，但会增加 verifier 偏差、分布迁移和优化耦合。 论文自身的边界信号是：6 Future Work Molt already runs the full asynchronous loop, rollout, weight refit, and optimizer step, end to end on a 700B MoE at expert parallelism 256, on the same lean loop it runs at 4B.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`TRAIN-GRPO`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-21653:end -->

<!-- review:SF-2026-ARXIV-2607-21656:start -->
### Cross-Model LLM Code Review: Should you use Claude to review Codex or vice versa?

<!-- claim:SF-2026-ARXIV-2607-21656:start -->Developers increasingly use two coding agents together: one writes a draft, and the other reviews it. However, it is not clear whether the pairing is worth its cost and time, or whether the order of the pairing matters. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-21656:end -->

**为什么进入候选分母。** 摘要首要问题为“Developers increasingly use two coding agents together: one writes a draft, and the other reviews it.”；它改变 observable、对照组、判定粒度或外推边界，可能修正既有评测结论。

**机制与状态边界。** However, it is not clear whether the pairing is worth its cost and time, or whether the order of the pairing matters.

**证据证明什么。** Our evaluation indicates that the useful pairing is asymmetric: use Claude to review Codex, not the other way around.

**证据没有证明什么。** The static reviewer cannot execute tests, which keeps the setting close to pre-CI code review but likely understates what a tool-using agent with a sandbox could achieve. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.21656v1#S3 — 3. Methodology。Evaluation：https://arxiv.org/html/2607.21656v1#S2.SS1 — 2.1. Code generation benchmarks; https://arxiv.org/html/2607.21656v1#S4 — 4. Results。Limitations / counterevidence：https://arxiv.org/html/2607.21656v1#S5 — 5. Discussion; https://arxiv.org/html/2607.21656v1#S5.SS5 — 5.5. Scope, Limitations, and Reproducibility。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：The static reviewer cannot execute tests, which keeps the setting close to pre-CI code review but likely understates what a tool-using agent with a sandbox could achieve.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`PLATFORM-EVALUATION-SYSTEM`；evidence-stage relation：`corrective_evidence`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-21656:end -->

<!-- review:SF-2026-ARXIV-2607-21661:start -->
### GRACE: Gradient-Free Robot Action Generation via Combined Diffusion-MPPI Posterior Mean Estimation

<!-- claim:SF-2026-ARXIV-2607-21661:start -->Diffusion policies generate multimodal robot action sequences from demonstrations, but steering them toward deployment-time constraints typically relies on differentiable guidance costs. This excludes many practical safety constraints, such as binary collision checks, joint limits, and black-box rollout costs that are nondifferentiable. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-21661:end -->

**为什么进入候选分母。** 摘要首要问题为“Diffusion policies generate multimodal robot action sequences from demonstrations, but steering them toward deployment-time constraints typically relies on differentiable guidance costs.”；它提出可跨 workload 讨论的表示、状态或计算机制，并暴露旧方案边界。

**机制与状态边界。** We propose Gradient-free Robot Action generation via Combined diffusion-MPPI posterior mean Estimation (GRACE), which guides a pretrained diffusion policy with Model Predictive Path Integral (MPPI) control using only forward cost evaluations.

**证据证明什么。** Code and experiment videos are available at https://anonymous.4open.science/w/grace-70BB/.

**证据没有证明什么。** Future work will extend GRACE to a broader range of robotic tasks and investigate a single diffusion prior that captures multiple task behaviors, developing guidance that steers the shared prior toward a desired task at inference time without training separate models. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.21661v1#S3 — III PROPOSED METHOD; https://arxiv.org/html/2607.21661v1#S2.SS1 — II-A Diffusion Models for Trajectory Generation。Evaluation：https://arxiv.org/html/2607.21661v1#S4 — IV EXPERIMENTS; https://arxiv.org/html/2607.21661v1#S4.SS1 — IV-A Experimental Setup。Limitations / counterevidence：https://arxiv.org/html/2607.21661v1#S5 — V CONCLUSION。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 新表示或状态机制扩大能力边界，但带来额外训练、状态管理、稳定性或泛化假设。 论文自身的边界信号是：Future work will extend GRACE to a broader range of robotic tasks and investigate a single diffusion prior that captures multiple task behaviors, developing guidance that steers the shared prior toward a desired task at inference time without training separate models.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`MULTIMODAL-EMBODIED-VLA`；evidence-stage relation：`alternative_branch`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-21661:end -->

<!-- review:SF-2026-ARXIV-2607-21670:start -->
### Ordered Action Tokens for Visuomotor Policy Learning

<!-- claim:SF-2026-ARXIV-2607-21670:start -->Action tokenization maps continuous robot action chunks to discrete tokens and has become an important interface for modern visuomotor policies. Existing approaches either rely on analytical discretization methods that produce prohibitively long token sequences or learned latent tokenizers that lack structure, limiting their compatibility with downstream policies. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-21670:end -->

**为什么进入候选分母。** 摘要首要问题为“Action tokenization maps continuous robot action chunks to discrete tokens and has become an important interface for modern visuomotor policies.”；它提出可跨 workload 讨论的表示、状态或计算机制，并暴露旧方案边界。

**机制与状态边界。** Existing approaches either rely on analytical discretization methods that produce prohibitively long token sequences or learned latent tokenizers that lack structure, limiting their compatibility with downstream policies.

**证据证明什么。** Across three policy backbones and more than 60 tasks spanning five simulation benchmarks and real-world settings, OAT consistently delivers strong policy performance while offering significantly greater flexibility at inference time.

**证据没有证明什么。** Future policies could decide online whether another token or block warrants an additional policy call, using token entropy, reconstruction uncertainty, or downstream value estimates. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.21670v1#A3 — Appendix C Experimental Protocol and Implementation; https://arxiv.org/html/2607.21670v1#A3.SS3 — C.3 Policy Implementations。Evaluation：https://arxiv.org/html/2607.21670v1#S6.SS4 — 6.4 Ablation and Analysis; https://arxiv.org/html/2607.21670v1#A3 — Appendix C Experimental Protocol and Implementation。Limitations / counterevidence：https://arxiv.org/html/2607.21670v1#S8 — 8 Conclusion and Limitations。

**Artifact boundary。** Exact v1 links https://github.com/Chaoqi-LIU/oat, https://github.com/Chaoqi-LIU/praxis-vla, https://github.com/arXiv/html_feedback/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 新表示或状态机制扩大能力边界，但带来额外训练、状态管理、稳定性或泛化假设。 论文自身的边界信号是：Future policies could decide online whether another token or block warrants an additional policy call, using token entropy, reconstruction uncertainty, or downstream value estimates.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`MULTIMODAL-EMBODIED-VLA`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-21670:end -->

<!-- review:SF-2026-ARXIV-2607-21672:start -->
### Pixels for Programs? A Cross-Provider Case Study of Input-Token Accounting for Source Code as Text and Images

<!-- claim:SF-2026-ARXIV-2607-21672:start -->Long source-code contexts consume many text tokens, motivating the proposal to render code as images for vision-language models. Recent work asks whether models can still solve code tasks after this transformation. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-21672:end -->

**为什么进入候选分母。** 摘要首要问题为“Long source-code contexts consume many text tokens, motivating the proposal to render code as images for vision-language models.”；它改变 observable、对照组、判定粒度或外推边界，可能修正既有评测结论。

**机制与状态边界。** We examine a different systems question: how commercial APIs count the resulting requests.

**证据证明什么。** We release the scripts, revision-pinned corpus specification, raw usage records, validators, and deterministic analysis needed to reproduce and extend the study.

**证据没有证明什么。** Threats to Validity Empirical software-engineering guidance emphasizes construct validity, measurement fairness, repetitions, and reproducibility ( Ralph et al., 2020 ) . 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.21672v1#S3 — 3. Study Design。Evaluation：https://arxiv.org/html/2607.21672v1#S4 — 4. Results; https://arxiv.org/html/2607.21672v1#S5.SS3 — 5.3. Next experiment。Limitations / counterevidence：https://arxiv.org/html/2607.21672v1#S5 — 5. Discussion; https://arxiv.org/html/2607.21672v1#S6 — 6. Threats to Validity。

**Artifact boundary。** Exact v1 links https://github.com/ron-42/code-image-token-accounting, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：Threats to Validity Empirical software-engineering guidance emphasizes construct validity, measurement fairness, repetitions, and reproducibility ( Ralph et al., 2020 ) .

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`PLATFORM-COST`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-21672:end -->

<!-- review:SF-2026-ARXIV-2607-21674:start -->
### Output Format x Model Identity: Interaction Effects in Single-Round Coding Agent Performance

<!-- claim:SF-2026-ARXIV-2607-21674:start -->Output format is not a neutral implementation detail -- it can reorder model rankings, amplify or suppress individual model differences, and determine whether a coding agent succeeds or fails. We conducted a controlled single-round experiment with 3 models (DeepSeek V4, Doubao 2.0 Pro, Qwen 3.7 Max) x 3 output formats (full file, JSON Patch, unified diff) x 6 tasks x 20 repetitions, totaling 4,013 runs across 4 open-source projects. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-21674:end -->

**为什么进入候选分母。** 摘要首要问题为“Output format is not a neutral implementation detail -- it can reorder model rankings, amplify or suppress individual model differences, and determine whether a coding agent succeeds or fails.”；它改变 observable、对照组、判定粒度或外推边界，可能修正既有评测结论。

**机制与状态边界。** We propose a model-specific output strategy, a tool-design principle that constrains format semantics to the agent's own localization step, and release all data and templates for reproducibility.

**证据证明什么。** Doubao achieves 94% success with JSON Patch (Cohen's h = 1.57, p &lt; 0.001), DeepSeek excels at unified diff (66%, h = 0.63), and Qwen shows a small but significant full-file preference (50%, h = 0.29, p &lt; 0.05).

**证据没有证明什么。** Baseline tests on unmodified project clones were not performed in the original v1 preprint. v2 includes baseline validation (see §3.1): dotenv (220 passed), requests (402 passed), confirming that zero-success rates reflect genuine agent limitations rather than broken test suites. jsoup could not be validated (JDK 21 incompatibility with the project’s JDK 8 target). • Verification heterogeneity. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.21674v1#A1.SS1 — A.1 System Instruction (Fixed); https://arxiv.org/html/2607.21674v1#S2.SS1 — 2.1 Coding Agent Architectures and Benchmarks。Evaluation：https://arxiv.org/html/2607.21674v1#A1.SS5 — A.5 Experiment Runner Configuration; https://arxiv.org/html/2607.21674v1#A2 — Appendix B Task Type Moderation (Supplementary Analysis)。Limitations / counterevidence：https://arxiv.org/html/2607.21674v1#A3 — Appendix C Supplementary Limitations; https://arxiv.org/html/2607.21674v1#S2.SS3 — 2.3 Agent Evaluation and Failure Diagnosis。

**Artifact boundary。** Exact v1 links https://github.com/NousResearch/hermes-agent/issues/66127, https://github.com/NousResearch/hermes-agent/issues/64103, https://github.com/arXiv/html_feedback/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：Baseline tests on unmodified project clones were not performed in the original v1 preprint. v2 includes baseline validation (see §3.1): dotenv (220 passed), requests (402 passed), confirming that zero-success rates reflect genuine agent limitations rather than broken test suites. jsoup could not be validated (JDK 21 incompatibility with the project’s JDK 8 target). • Verification heterogeneity.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`PLATFORM-EVALUATION-SYSTEM`；evidence-stage relation：`corrective_evidence`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-21674:end -->

<!-- review:SF-2026-ARXIV-2607-21686:start -->
### Persistent Computational State: A Session-Centric Runtime for Generative World Models

<!-- claim:SF-2026-ARXIV-2607-21686:start -->Generative world models are increasingly driven as simulators: a planner forks a state, rolls out futures, backtracks, and returns to a visited viewpoint. Recent benchmarks establish that current video world models fail this usage, and attribute it to the model, prescribing new architectures and training objectives. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-21686:end -->

**为什么进入候选分母。** 摘要首要问题为“Generative world models are increasingly driven as simulators: a planner forks a state, rolls out futures, backtracks, and returns to a visited viewpoint.”；它把 context、memory、能力或进度变成持久且可验证的 agent state。

**机制与状态边界。** Recent benchmarks establish that current video world models fail this usage, and attribute it to the model, prescribing new architectures and training objectives.

**证据证明什么。** We show this attribution is incomplete, and for an important class of models simply wrong.

**证据没有证明什么。** The addressability the substrate exposes is read-only, not write-repositionable without rewriting the cache manager. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.21686v1#S8 — 8 Implementation。Evaluation：https://arxiv.org/html/2607.21686v1#S7 — 7 Evaluation。Limitations / counterevidence：https://arxiv.org/html/2607.21686v1#S10 — 10 Discussion, limitations, and conclusion; https://arxiv.org/html/2607.21686v1#S7.SS11 — 7.11 Threats to validity。

**Artifact boundary。** Exact v1 links https://github.com/NVIDIA/TensorRT-LLM, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 显式 agent state 改善恢复与控制，但增加状态陈旧、错误提交、跨轮污染和一致性责任。 论文自身的边界信号是：The addressability the substrate exposes is read-only, not write-repositionable without rewriting the cache manager.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`MULTIMODAL-WORLD-MODELS`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-21686:end -->

<!-- review:SF-2026-ARXIV-2607-21722:start -->
### Be Consistent! Enhancing Robust Visual Reasoning in LVLMs with Consistency Constraints

<!-- claim:SF-2026-ARXIV-2607-21722:start -->While Large Vision-Language Models (LVLMs) exhibit strong perceptual capabilities, they remain vulnerable in visual reasoning tasks. Existing benchmarks largely focus on symbolic mathematical or scientific problems and simple vision-centric tasks, offering limited assessment of complex visual reasoning and logical consistency, a critical requirement for reliable reasoning systems. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-21722:end -->

**为什么进入候选分母。** 摘要首要问题为“While Large Vision-Language Models (LVLMs) exhibit strong perceptual capabilities, they remain vulnerable in visual reasoning tasks.”；它改变 observable、对照组、判定粒度或外推边界，可能修正既有评测结论。

**机制与状态边界。** The framework functions effectively with or without strict answer supervision.

**证据证明什么。** We further present ConVLM, which improves LVLM reasoning through Group Relative Policy Optimization (GRPO)-based reinforcement learning with a novel consistency reward.

**证据没有证明什么。** Limitations This work makes the initial step to explore consistency reward and robustness in visual reasoning tasks, leaving many promising directions to future work. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.21722v1#A14 — Appendix N Comparison with Prior Consistency-Based Reasoning Methods; https://arxiv.org/html/2607.21722v1#S3 — 3 Method。Evaluation：https://arxiv.org/html/2607.21722v1#A13 — Appendix M Benchmark Characteristics Analysis; https://arxiv.org/html/2607.21722v1#A1 — Appendix A Benchmark Comparison。Limitations / counterevidence：https://arxiv.org/html/2607.21722v1#S6 — 6 Conclusion; https://arxiv.org/html/2607.21722v1#Sx1 — Limitations。

**Artifact boundary。** Exact v1 links https://github.com/LiqiangJing/ConVLM, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：Limitations This work makes the initial step to explore consistency reward and robustness in visual reasoning tasks, leaving many promising directions to future work.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`MULTIMODAL-REPRESENTATION`；evidence-stage relation：`corrective_evidence`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-21722:end -->

<!-- review:SF-2026-ARXIV-2607-21725:start -->
### Addressing the Orchestration Gap in Generalist Robots via Physical Agency

<!-- claim:SF-2026-ARXIV-2607-21725:start -->General-purpose robots need to reason about their actions, combining perception, world knowledge, planning, success detection, recovery, and low-level control. Today's state-of-the-art models attempt to combine all these capabilities into the learned policy via large-scale pre-training. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-21725:end -->

**为什么进入候选分母。** 摘要首要问题为“General-purpose robots need to reason about their actions, combining perception, world knowledge, planning, success detection, recovery, and low-level control.”；它把 context、memory、能力或进度变成持久且可验证的 agent state。

**机制与状态边界。** Today's state-of-the-art models attempt to combine all these capabilities into the learned policy via large-scale pre-training.

**证据证明什么。** We evaluate Pigey extensively across simulation benchmarks and challenging real-world robotic manipulation tasks, and demonstrate significant performance improvements over existing generalist policies.

**证据没有证明什么。** First-failure mode TiPToP Pigey (ours) Grounding (wrong / random target) 86 5 0 Reasoning / planning 38 65 0 Grasp (execution) 1 7 2 Verifier false-success 0 0 2 Total failures 125 77 4 Table 14 : Distribution of first-failure modes (counts, out of 150 trials each). fails predominantly at grounding —selecting the wrong object; TiPToP grounds correctly but fails at reasoning / planning on the multi-step, obstacle, recovery, and memory tasks; while Pigey fails only four times, split between grasp execution and verifier false-success , a mode unique to its closed-loop verifier (declaring success when the target was not actually achieved). 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.21725v1#S1 — 1 Introduction; https://arxiv.org/html/2607.21725v1#S2 — 2 Related Work。Evaluation：https://arxiv.org/html/2607.21725v1#S12 — 12 Additional Results; https://arxiv.org/html/2607.21725v1#S12.SS1 — 12.1 Per-task real-robot results。Limitations / counterevidence：https://arxiv.org/html/2607.21725v1#S10 — 10 Observation Channel and Failure Annotations; https://arxiv.org/html/2607.21725v1#S12.SS3 — 12.3 First-failure mode distribution。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 显式 agent state 改善恢复与控制，但增加状态陈旧、错误提交、跨轮污染和一致性责任。 论文自身的边界信号是：First-failure mode TiPToP Pigey (ours) Grounding (wrong / random target) 86 5 0 Reasoning / planning 38 65 0 Grasp (execution) 1 7 2 Verifier false-success 0 0 2 Total failures 125 77 4 Table 14 : Distribution of first-failure modes (counts, out of 150 trials each). fails predominantly at grounding —selecting the wrong object; TiPToP grounds correctly but fails at reasoning / planning on the multi-step, obstacle, recovery, and memory tasks; while Pigey fails only four times, split between grasp execution and verifier false-success , a mode unique to its closed-loop verifier (declaring success when the target was not actually achieved).

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`MULTIMODAL-EMBODIED-VLA`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-21725:end -->

<!-- review:SF-2026-ARXIV-2607-21731:start -->
### RED-PIM: Reducing Data Movement for Transformers using Processing-in-Memory

<!-- claim:SF-2026-ARXIV-2607-21731:start -->Transformers are widely used across many domains, including natural language processing, computer vision, web search, and DNA sequence analysis. Given their broad applicability, improving the performance of transformer models is critical. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-21731:end -->

**为什么进入候选分母。** 摘要首要问题为“Transformers are widely used across many domains, including natural language processing, computer vision, web search, and DNA sequence analysis.”；它改变资源计量、分配、路由或迁移的控制权与约束。

**机制与状态边界。** In this work, we propose RED-PIM, an algorithm-architecture co-design that reduces attention latency by minimizing inter-bank data movement from O(N^2) to O(N) and shrinking intermediate attention matrices from N x N to d x d.

**证据证明什么。** These results demonstrate RED-PIM's effectiveness for scalable and efficient transformer inference.

**证据没有证明什么。** Along with these improvements, some limitations remain to be explored in future work: • Reduced Usable Bank Capacity: The use of FIMDRAM involves allocating portions of each memory bank for PCUs, which reduces the available storage. • Simulation-Based Evaluation: Due to the lack of available commercial or open-source hardware support, our PIM architecture is evaluated through simulation, which models data movement and in-memory computation. • Focus on Inference: Our work focuses on inference. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.21731v1#S3.SS3 — III-C Architecture Design in RED-PIM; https://arxiv.org/html/2607.21731v1#S2.SS2 — II-B Processing In/Near Memory Architectures。Evaluation：https://arxiv.org/html/2607.21731v1#S4 — IV Evaluation Methodology and Results; https://arxiv.org/html/2607.21731v1#S4.SS2 — IV-B Experimental Setup。Limitations / counterevidence：https://arxiv.org/html/2607.21731v1#S6 — VI Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 动态资源控制提高利用率，但增加测量误差、迁移开销、租户公平和控制稳定性问题。 论文自身的边界信号是：Along with these improvements, some limitations remain to be explored in future work: • Reduced Usable Bank Capacity: The use of FIMDRAM involves allocating portions of each memory bank for PCUs, which reduces the available storage. • Simulation-Based Evaluation: Due to the lack of available commercial or open-source hardware support, our PIM architecture is evaluated through simulation, which models data movement and in-memory computation. • Focus on Inference: Our work focuses on inference.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`INFER-TENSORRT-LLM`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-21731:end -->

<!-- review:SF-2026-ARXIV-2607-21735:start -->
### What AI Red-Team Evaluations Can and Cannot Prove

<!-- claim:SF-2026-ARXIV-2607-21735:start -->Red-team evaluations of AI models support some claims and not others, and the boundary between the two is calculable rather than merely a matter of judgment. We define the evidential ceiling of an evaluation as the largest factor by which one result can move belief under a fixed testing budget, derive it in closed form for the benchmark null result, and use it to locate that boundary exactly. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-21735:end -->

**为什么进入候选分母。** 摘要首要问题为“Red-team evaluations of AI models support some claims and not others, and the boundary between the two is calculable rather than merely a matter of judgment.”；它改变 observable、对照组、判定粒度或外推边界，可能修正既有评测结论。

**机制与状态边界。** We define the evidential ceiling of an evaluation as the largest factor by which one result can move belief under a fixed testing budget, derive it in closed form for the benchmark null result, and use it to locate that boundary exactly.

**证据证明什么。** Auditing eight evaluation suites against the boundary, we find that current benchmarks are adequate for high-frequency harm categories and several orders of magnitude short for rare, catastrophic ones.

**证据没有证明什么。** 8 Discussion We defined the ceiling abstractly and instantiated it only for the passive benchmark null result. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.21735v1#Sx1 — Methods。Evaluation：https://arxiv.org/html/2607.21735v1#S4.SS1 — 4.1 The benchmark null result, made precise; https://arxiv.org/html/2607.21735v1#S3 — 3 What an evaluation must establish。Limitations / counterevidence：https://arxiv.org/html/2607.21735v1#S7 — 7 Limitations; https://arxiv.org/html/2607.21735v1#S8 — 8 Discussion。

**Artifact boundary。** Exact v1 links https://github.com/hackwither/ai-redteam-evidential-limits, https://github.com/llm-attacks/llm-attacks, https://github.com/centerforaisafety/HarmBench; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：8 Discussion We defined the ceiling abstractly and instantiated it only for the passive benchmark null result.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`PLATFORM-EVALUATION-SYSTEM`；evidence-stage relation：`corrective_evidence`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-21735:end -->

<!-- review:SF-2026-ARXIV-2607-21738:start -->
### When Model Release Meets Model Reuse: Producer-Consumer Misalignment in Hugging Face

<!-- claim:SF-2026-ARXIV-2607-21738:start -->Pre-trained Language Models (PTLMs) are increasingly reused as dependencies in modern software systems, even though prior work has documented persistent structural problems in PTLM supply chains, such as inconsistent release practices, incomplete metadata, and divergence between Hugging Face and GitHub repositories. One previously unexplored angle on these problems is that misalignment between PTLM producers' release practices and consumers' model reuse needs may explain several of these challenges, yet the human expectations, processes and interactions underneath this misalignment have never been studied. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-21738:end -->

**为什么进入候选分母。** 摘要首要问题为“Pre-trained Language Models (PTLMs) are increasingly reused as dependencies in modern software systems, even though prior work has documented persistent structural problems in PTLM supply chains, such as inconsistent release practices, incomplete metadata, and divergence between Hugging Face and GitHub repositories.”；它把 evidence identity、lineage、conflict 或 commit 变成显式系统状态。

**机制与状态边界。** Pre-trained Language Models (PTLMs) are increasingly reused as dependencies in modern software systems, even though prior work has documented persistent structural problems in PTLM supply chains, such as inconsistent release practices, incomplete metadata, and divergence between Hugging Face and GitHub repositories.

**证据证明什么。** These findings highlight opportunities to improve model documentation conventions, lineage visibility, and governance support in PTLM supply chains.

**证据没有证明什么。** This low rate does not reflect lack of interest, but stems from difficulties due to the documentation gaps identified in RQ2: without complete and structured metadata, producers and consumers cannot reconstruct a model’s provenance even when they want to. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.21738v1#S3 — 3 Methodology; https://arxiv.org/html/2607.21738v1#S3.SS1 — 3.1 Survey Design and Pilot。Evaluation：https://arxiv.org/html/2607.21738v1#S3.SS4 — 3.4 Data Analysis; https://arxiv.org/html/2607.21738v1#S4 — 4 Results。Limitations / counterevidence：https://arxiv.org/html/2607.21738v1#S4.SS3 — 4.3 : What practical strategies do producers and consumers use to understand and trace model lineage across the AI supply chain, and what limitations or challenges do these strategies exhibit?; https://arxiv.org/html/2607.21738v1#S5 — 5 Discussion and Implications。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 显式 evidence state 提高可追溯性，但新增 lineage、冲突、commit 与恢复语义，状态本身也必须被验证。 论文自身的边界信号是：This low rate does not reflect lack of interest, but stems from difficulties due to the documentation gaps identified in RQ2: without complete and structured metadata, producers and consumers cannot reconstruct a model’s provenance even when they want to.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`PLATFORM-MODEL-REGISTRY`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-21738:end -->

<!-- review:SF-2026-ARXIV-2607-21746:start -->
### PRISM: Evaluating POSIX Storage Systems for AI Research Workflows

<!-- claim:SF-2026-ARXIV-2607-21746:start -->The rapid advancement of AI research is driven by massive investments in GPU clusters, yet the critical role of storage systems in enabling efficient research workflows is often overlooked. Unlike traditional HPC workloads, AI research prioritizes researcher productivity and ease of iteration. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-21746:end -->

**为什么进入候选分母。** 摘要首要问题为“The rapid advancement of AI research is driven by massive investments in GPU clusters, yet the critical role of storage systems in enabling efficient research workflows is often overlooked.”；它改变 observable、对照组、判定粒度或外推边界，可能修正既有评测结论。

**机制与状态边界。** We introduce PRISM, an evaluation framework that reproduces representative AI research workloads - spanning data ingestion, checkpoint IO, and developer workflows to assess and qualify POSIX storage systems along both usability and performance dimensions on GPU clusters.

**证据证明什么。** As a specific case study in our environment we observed that a flash backed NFS solution outperformed the flash backed Lustre solution by up to 3x for the distributed checkpoint load usecase which helped us make an informed cluster design

**证据没有证明什么。** By capturing these complex, real-world behaviors, PRISM provides actionable insights that synthetic benchmarks cannot. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.21746v1#S3.SS2 — 3.2 Framework Architecture; https://arxiv.org/html/2607.21746v1#S2 — 2 Storage Systems for AI Research Workflows。Evaluation：https://arxiv.org/html/2607.21746v1#S3 — 3 PRISM: A Benchmark Framework for AI research clusters; https://arxiv.org/html/2607.21746v1#S3.SS1 — 3.1 Benchmark Taxonomy。Limitations / counterevidence：https://arxiv.org/html/2607.21746v1#S6 — 6 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/axboe/fio, https://github.com/webdataset/webdataset, https://github.com/breuner/elbencho; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：By capturing these complex, real-world behaviors, PRISM provides actionable insights that synthetic benchmarks cannot.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`PLATFORM-FOUNDATIONS`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-21746:end -->

<!-- review:SF-2026-ARXIV-2607-21752:start -->
### Parameter-free Adaptive Sparse Attention via Compression-Based Content Selection

<!-- claim:SF-2026-ARXIV-2607-21752:start -->Data-adaptive sparse attention masks substantially outperform fixed patterns (e.g., BigBird and Longformer) and can even exceed dense attention on long sequences. Existing adaptive approaches---including SBM-Transformer, Dynamic Mask Attention, and NSA---typically require additional learnable parameters, custom gradient estimators, or specialized CUDA kernels. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-21752:end -->

**为什么进入候选分母。** 摘要首要问题为“Data-adaptive sparse attention masks substantially outperform fixed patterns (e.g., BigBird and Longformer) and can even exceed dense attention on long sequences.”；它提出可跨 workload 讨论的表示、状态或计算机制，并暴露旧方案边界。

**机制与状态边界。** On PG-19 byte-level language modeling at 92M parameters with 8K context, our method achieves 1.71 bits-per-byte (BPB), outperforming dense attention (2.89), BigBird (2.34), Longformer (3.21), and a reimplemented SBM-Transformer (3.38)---the only learned-mask baseline---by up to 1.67 BPB while adding no parameters.

**证据证明什么。** On PG-19 byte-level language modeling at 92M parameters with 8K context, our method achieves 1.71 bits-per-byte (BPB), outperforming dense attention (2.89), BigBird (2.34), Longformer (3.21), and a reimplemented SBM-Transformer (3.38)---the only learned-mask baseline---by up to 1.67 BPB while adding no parameters.

**证据没有证明什么。** Exact v1 does not disclose a dedicated generalization or deployment guarantee beyond its stated evaluation scope. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.21752v1#A1.SS1 — A.1 Model Architecture; https://arxiv.org/html/2607.21752v1#A9 — Appendix I Detailed Comparison to Learned Mask Methods。Evaluation：https://arxiv.org/html/2607.21752v1#S4 — 4 Experiments and Results; https://arxiv.org/html/2607.21752v1#S4.SS3 — 4.3 Experiment 2: Component ablation。Limitations / counterevidence：https://arxiv.org/html/2607.21752v1#A11 — Appendix K Extended Discussion; https://arxiv.org/html/2607.21752v1#A12 — Appendix L Detailed Limitations。

**Artifact boundary。** Exact v1 links https://github.com/sc782/SBM-Transformer, https://github.com/sc782/SBM-Transformer/tree/main/code, https://github.com/arXiv/html_feedback/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 新表示或状态机制扩大能力边界，但带来额外训练、状态管理、稳定性或泛化假设。 论文自身的边界信号是：Exact v1 does not disclose a dedicated generalization or deployment guarantee beyond its stated evaluation scope.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`MODEL-LONG-CONTEXT`；evidence-stage relation：`alternative_branch`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-21752:end -->

<!-- review:SF-2026-ARXIV-2607-21756:start -->
### Prompt as a Data Type: In-Database LLM Prompt Management and Rewriting

<!-- claim:SF-2026-ARXIV-2607-21756:start -->Large Language Models (LLMs) are increasingly used in database-backed applications to classify tuples, filter records using semantic predicates, extract structured attributes, and enrich query results. Yet the prompt that start these computations are typically stored outside the DBMS in unstructured formats, making them invisible to query execution, metadata management, and optimization. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-21756:end -->

**为什么进入候选分母。** 摘要首要问题为“Large Language Models (LLMs) are increasingly used in database-backed applications to classify tuples, filter records using semantic predicates, extract structured attributes, and enrich query results.”；它把 evidence identity、lineage、conflict 或 commit 变成显式系统状态。

**机制与状态边界。** Users query prompt-valued attributes through generated evaluation views, while the system internally renders, rewrites, optimizes, and executes prompts through an EVAL operator.

**证据证明什么。** The results show how database-guided rewriting improves output validity and yields favorable cost-quality trade-offs compared with static, manually written prompts.

**证据没有证明什么。** These results motivate future work on task-aware, calibrated, or learned models. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.21756v1#S3 — 3. System Implementation; https://arxiv.org/html/2607.21756v1#S2 — 2. Formal Model。Evaluation：https://arxiv.org/html/2607.21756v1#S4 — 4. Experiments and Results; https://arxiv.org/html/2607.21756v1#S4.SS2 — 4.2. Rule Ablation。Limitations / counterevidence：https://arxiv.org/html/2607.21756v1#S4.SS4 — 4.4. Discussion; https://arxiv.org/html/2607.21756v1#S6 — 6. Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 显式 evidence state 提高可追溯性，但新增 lineage、冲突、commit 与恢复语义，状态本身也必须被验证。 论文自身的边界信号是：These results motivate future work on task-aware, calibrated, or learned models.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`AGENT-PROMPT`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-21756:end -->

<!-- review:SF-2026-ARXIV-2607-21763:start -->
### Every Model Cheats: Prompt-Level Mitigation of Cheating on Offensive Cyber Tasks

<!-- claim:SF-2026-ARXIV-2607-21763:start -->Large language model (LLM) agents routinely cheat on cybersecurity benchmarks, inflating reported pass rates far beyond genuine capability. Prior audits of Cybench found cheating in 0.3-3.4% of traces, implicating only a handful of models. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-21763:end -->

**为什么进入候选分母。** 摘要首要问题为“Large language model (LLM) agents routinely cheat on cybersecurity benchmarks, inflating reported pass rates far beyond genuine capability.”；它改变执行安全的 trust boundary、guard 或 failure detection。

**机制与状态边界。** We present a controlled prompt-ablation study across 22 frontier models from 7 providers on 23 Cybench capture-the-flag (CTF) challenges under three prompt conditions (no anti-cheat, standard, severe).

**证据证明什么。** Anti-cheat prompts reduce cheat propensity from 33.0% (baseline) to 17.8% (standard) to 8.5% (severe) without degrading, and sometimes improving, solve rates.

**证据没有证明什么。** Second, prompt-level mitigation should be adopted as a default first layer of defense, but environmental controls remain necessary to close the gap that prompts cannot. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.21763v1#S2 — 2 Methodology。Evaluation：https://arxiv.org/html/2607.21763v1#S3 — 3 Results; https://arxiv.org/html/2607.21763v1#S3.SS2 — 3.2 Prompt Ablation。Limitations / counterevidence：https://arxiv.org/html/2607.21763v1#S4 — 4 Discussion; https://arxiv.org/html/2607.21763v1#S6 — 6 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/mkultraWasHere, https://github.com/GangGreenTemperTatum, https://github.com/rdheekonda; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 新的安全控制点降低特定失败，但会引入误拒绝、旁路、观测不足或模型/任务迁移问题。 论文自身的边界信号是：Second, prompt-level mitigation should be adopted as a default first layer of defense, but environmental controls remain necessary to close the gap that prompts cannot.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`PLATFORM-SECURITY`；evidence-stage relation：`corrective_evidence`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-21763:end -->

<!-- review:SF-2026-ARXIV-2607-21799:start -->
### Agentic Evaluation of Copyright Law Compliance

<!-- claim:SF-2026-ARXIV-2607-21799:start -->Large language model (LLM) agents increasingly perform commercial tasks that involve retrieving external content, such as images, and, where appropriate, reproducing that content. LLM agents should comply with the law, including copyright law. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-21799:end -->

**为什么进入候选分母。** 摘要首要问题为“Large language model (LLM) agents increasingly perform commercial tasks that involve retrieving external content, such as images, and, where appropriate, reproducing that content.”；它改变 observable、对照组、判定粒度或外推边界，可能修正既有评测结论。

**机制与状态边界。** Presently, however, we lack adequate frameworks to assess whether they do so in practice.

**证据证明什么。** Comparing state-of-the-art LLM agents against a human baseline, we find that: (1) agents select copyrighted works despite the availability of public-domain alternatives; and (2) for open-weight models, violation rates increase in response to certain user preferences and simulated time pressure.

**证据没有证明什么。** Exact v1 does not disclose a dedicated generalization or deployment guarantee beyond its stated evaluation scope. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.21799v1#A3.SS2 — C.2 Task Interface and Methodology; https://arxiv.org/html/2607.21799v1#S3.SS3 — 3.3 Legal Framework: U.S. Copyright Law。Evaluation：https://arxiv.org/html/2607.21799v1#S2.SS1 — 2.1 Agent Benchmarks and Agent Evaluation; https://arxiv.org/html/2607.21799v1#A4 — Appendix D Full Results Table。Limitations / counterevidence：https://arxiv.org/html/2607.21799v1#A1 — Appendix A Limitations and Future Work; https://arxiv.org/html/2607.21799v1#S3.SS4 — 3.4 Scope and Limitations。

**Artifact boundary。** Exact v1 links https://github.com/zackhuiiiii/Copyright-Bench, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：Exact v1 does not disclose a dedicated generalization or deployment guarantee beyond its stated evaluation scope.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`PLATFORM-EVALUATION-SYSTEM`；evidence-stage relation：`principle_reuse`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-21799:end -->

<!-- review:SF-2026-ARXIV-2607-21804:start -->
### Adversarial Prompts for Acceptance Collapse in Speculative Decoding

<!-- claim:SF-2026-ARXIV-2607-21804:start -->Lossless acceleration schemes, such as speculative decoding, promise significant inference speedups by relying on dynamic token-level alignment between a draft and a target model. However, this guarantee of semantic equivalence masks a severe operational vulnerability: draft-target alignment can be systematically attacked. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-21804:end -->

**为什么进入候选分母。** 摘要首要问题为“Lossless acceleration schemes, such as speculative decoding, promise significant inference speedups by relying on dynamic token-level alignment between a draft and a target model.”；它改变执行安全的 trust boundary、guard 或 failure detection。

**机制与状态边界。** However, this guarantee of semantic equivalence masks a severe operational vulnerability: draft-target alignment can be systematically attacked.

**证据证明什么。** We further show that this vulnerability exists across different domains, speculative decoding strategies, and model architectures.

**证据没有证明什么。** The only difference is whether we run (i) the standalone draft model alone or (ii) the full speculative decoding system with a larger target verifier. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.21804v1#S3.SS2 — 3.2 Systemic Impact; https://arxiv.org/html/2607.21804v1#S4 — 4 Attack Method。Evaluation：https://arxiv.org/html/2607.21804v1#A1 — Appendix A Additional Evaluation Settings; https://arxiv.org/html/2607.21804v1#A2 — Appendix B Additional Attack Analysis。Limitations / counterevidence：https://arxiv.org/html/2607.21804v1#A2.SS1 — B.1 Case Study: Standalone Draft Failure vs. Speculative Recovery; https://arxiv.org/html/2607.21804v1#S3 — 3 Threat Model and Impact。

**Artifact boundary。** Exact v1 links https://aws.amazon.com/blogs/machine-learning/accelerating-decode-heavy-llm-inference-with-speculative-decoding-on-aws-trainium-and-vllm/, https://huggingface.co/docs/text-generation-inference/en/index, https://huggingface.co/blog/continuous_batching; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 新的安全控制点降低特定失败，但会引入误拒绝、旁路、观测不足或模型/任务迁移问题。 论文自身的边界信号是：The only difference is whether we run (i) the standalone draft model alone or (ii) the full speculative decoding system with a larger target verifier.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`INFER-SPECULATIVE-DECODING`；evidence-stage relation：`corrective_evidence`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-21804:end -->

<!-- review:SF-2026-ARXIV-2607-21824:start -->
### Protocol-Level Attacks on Agentic Commerce Platforms: A Cross-Platform Taxonomy, AIP-Bench, and Unified Defense

<!-- claim:SF-2026-ARXIV-2607-21824:start -->Agentic commerce platforms let AI agents autonomously discover services, move payments, and wield user credentials on their users' behalf, and they already handle real money. Their security has so far been studied almost entirely at the level of the AI model, through prompt injection and misalignment. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-21824:end -->

**为什么进入候选分母。** 摘要首要问题为“Agentic commerce platforms let AI agents autonomously discover services, move payments, and wield user credentials on their users' behalf, and they already handle real money.”；它改变执行安全的 trust boundary、guard 或 failure detection。

**机制与状态边界。** The same failure modes recur across independently built codebases, a systemic pattern rather than isolated bugs.

**证据证明什么。** We show that the more consequential risks lie one layer down, in the protocol between agents and commerce services.

**证据没有证明什么。** The live V9 proof (Section 4.5 ) stops at the protocol level rather than an on-chain transfer: we generated real Solana Devnet keypairs for both parties but could not settle on-chain due to faucet rate limiting. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.21824v1#S8.SS1 — 8.1 Architecture and Design Principles; https://arxiv.org/html/2607.21824v1#S3.SS1 — 3.1 System Actors and Trust Boundaries。Evaluation：https://arxiv.org/html/2607.21824v1#A2 — Appendix B Experimental Environment; https://arxiv.org/html/2607.21824v1#A5.SSx1 — A-AP2-4: Empty trusted_roots (Python Falsy Evaluation)。Limitations / counterevidence：https://arxiv.org/html/2607.21824v1#S10 — 10 Discussion; https://arxiv.org/html/2607.21824v1#S10.SS2 — 10.2 Limitations。

**Artifact boundary。** Exact v1 links https://github.com/yedidel/aip-bench-public, https://huggingface.co/datasets/anonymos-2321135/aip-bench, https://github.com/Coral-Protocol/coral-server; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 新的安全控制点降低特定失败，但会引入误拒绝、旁路、观测不足或模型/任务迁移问题。 论文自身的边界信号是：The live V9 proof (Section 4.5 ) stops at the protocol level rather than an on-chain transfer: we generated real Solana Devnet keypairs for both parties but could not settle on-chain due to faucet rate limiting.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`AGENT-PLATFORM`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-21824:end -->

<!-- review:SF-2026-ARXIV-2607-21835:start -->
### ToolGuardian: Declarative Security for AI Agent-Tool Interactions

<!-- claim:SF-2026-ARXIV-2607-21835:start -->LLM agents increasingly rely on external tools, expanding capability while creating a new security boundary: third-party tools may appear benign at the interface level while embedding unsafe behavior in implementation. Existing defenses rely on weak metadata, collapse characterization and policy judgment into a single decision, or use heuristic/LLM enforcement that lacks deterministic, auditable reasoning over task context and multi-tool composition. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-21835:end -->

**为什么进入候选分母。** 摘要首要问题为“LLM agents increasingly rely on external tools, expanding capability while creating a new security boundary: third-party tools may appear benign at the interface level while embedding unsafe behavior in implementation.”；它改变执行安全的 trust boundary、guard 或 failure detection。

**机制与状态边界。** This paper presents ToolGuardian, a policy-driven framework for securing agent-tool interactions through pre-admission vetting and task-aware runtime authorization.

**证据证明什么。** For runtime authorization, fully specified realizations classify all scenarios correctly, while ablations show that removing compositional and conformance rules substantially degrades performance.

**证据没有证明什么。** Exact v1 does not disclose a dedicated generalization or deployment guarantee beyond its stated evaluation scope. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.21835v1#S6 — VI Policy Framework; https://arxiv.org/html/2607.21835v1#S3 — III Threat Model。Evaluation：https://arxiv.org/html/2607.21835v1#S8 — VIII Evaluation Results; https://arxiv.org/html/2607.21835v1#A1 — Appendix A Tool benchmarks。Limitations / counterevidence：https://arxiv.org/html/2607.21835v1#S10 — X Limitations and Future Work; https://arxiv.org/html/2607.21835v1#S11 — XI Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/cisco-ai-defense/mcp-scanner, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 新的安全控制点降低特定失败，但会引入误拒绝、旁路、观测不足或模型/任务迁移问题。 论文自身的边界信号是：Exact v1 does not disclose a dedicated generalization or deployment guarantee beyond its stated evaluation scope.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`AGENT-TOOL-CALLING`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-21835:end -->

<!-- review:SF-2026-ARXIV-2607-21857:start -->
### SoundscapeAgent: Agentic Soundscape Construction for Controllable Synthesis and Scalable Audio-Language Supervision

<!-- claim:SF-2026-ARXIV-2607-21857:start -->We present an agentic soundscape construction framework for controllable compositional audio generation that makes explicit the scene planning, source selection, temporal layout, and rendering steps typically handled implicitly by single-shot text-to-audio models. An LLM-based agent converts user intent into an executable scene plan, acquires assets through retrieval and on-demand generation, renders controllable multi-event mixtures, and exports aligned scene metadata. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-21857:end -->

**为什么进入候选分母。** 摘要首要问题为“We present an agentic soundscape construction framework for controllable compositional audio generation that makes explicit the scene planning, source selection, temporal layout, and rendering steps typically handled implicitly by single-shot text-to-audio models.”；它改变训练信号、capacity 或 update ownership，而非只报告任务精度。

**机制与状态边界。** We present an agentic soundscape construction framework for controllable compositional audio generation that makes explicit the scene planning, source selection, temporal layout, and rendering steps typically handled implicitly by single-shot text-to-audio models.

**证据证明什么。** Listener studies and objective metrics demonstrate competitive generation performance against text-to-audio baselines, while models trained with agent-generated data consistently outperform real-only baselines in downstream audio reasoning.

**证据没有证明什么。** In particular, some of the fine-grained information captured by our data is not explicitly evaluated by MMAU, so the current results may reflect only part of the value of the generated supervision. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.21857v1#S3 — III Agentic Soundscape Construction Framework。Evaluation：https://arxiv.org/html/2607.21857v1#S4 — IV Experiments and Results; https://arxiv.org/html/2607.21857v1#S4.SS1 — IV-A Track A: Agent Evaluation。Limitations / counterevidence：https://arxiv.org/html/2607.21857v1#S5 — V Discussion and Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更密集或更定向的训练信号改善样本效率，但会增加 verifier 偏差、分布迁移和优化耦合。 论文自身的边界信号是：In particular, some of the fine-grained information captured by our data is not explicitly evaluated by MMAU, so the current results may reflect only part of the value of the generated supervision.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`MULTIMODAL-REPRESENTATION`；evidence-stage relation：`principle_reuse`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-21857:end -->

<!-- review:SF-2026-ARXIV-2607-21861:start -->
### Data Quality over Capacity: Internalizing Documents into LoRA Adapters for Closed-Book QA

<!-- claim:SF-2026-ARXIV-2607-21861:start -->We study baking documents directly into the weights of a 4-bit Gemma-4-e4b model via LoRA, so a system can answer questions about a corpus closed-book: no retrieval and no context-window budget. Across roughly 100 training runs from single documents to a 99-document corpus, we find that once adapter capacity is adequate, training-data quality is the dominant lever on closed-book accuracy, outweighing LoRA rank, learning rate, and two alternative architectures combined; capacity itself is a hard gate below which no data intervention helps. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-21861:end -->

**为什么进入候选分母。** 摘要首要问题为“We study baking documents directly into the weights of a 4-bit Gemma-4-e4b model via LoRA, so a system can answer questions about a corpus closed-book: no retrieval and no context-window budget.”；它改变训练信号、capacity 或 update ownership，而非只报告任务精度。

**机制与状态边界。** We study baking documents directly into the weights of a 4-bit Gemma-4-e4b model via LoRA, so a system can answer questions about a corpus closed-book: no retrieval and no context-window budget.

**证据证明什么。** Across roughly 100 training runs from single documents to a 99-document corpus, we find that once adapter capacity is adequate, training-data quality is the dominant lever on closed-book accuracy, outweighing LoRA rank, learning rate, and two alternative architectures combined; capacity itself is a hard gate below which no data intervention helps.

**证据没有证明什么。** Scale : 99 documents is far below a tens-of-thousands-document target, so the negative architecture results and the exact rank/LR constants may not extrapolate; larger-scale cartridge training in particular reports gains our small-scale runs cannot ( Eyuboglu et al., 2025 ; Hardalov et al., 2026 ) . 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.21861v1#S1 — 1 Introduction; https://arxiv.org/html/2607.21861v1#S2 — 2 Task, Metric, and Recipe。Evaluation：https://arxiv.org/html/2607.21861v1#A2 — Appendix B Metric-Bias Analysis; https://arxiv.org/html/2607.21861v1#S3 — 3 Results。Limitations / counterevidence：https://arxiv.org/html/2607.21861v1#S4 — 4 Discussion and Threats to Validity; https://arxiv.org/html/2607.21861v1#S5 — 5 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更密集或更定向的训练信号改善样本效率，但会增加 verifier 偏差、分布迁移和优化耦合。 论文自身的边界信号是：Scale : 99 documents is far below a tens-of-thousands-document target, so the negative architecture results and the exact rank/LR constants may not extrapolate; larger-scale cartridge training in particular reports gains our small-scale runs cannot ( Eyuboglu et al., 2025 ; Hardalov et al., 2026 ) .

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`TRAIN-LORA`；evidence-stage relation：`corrective_evidence`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-21861:end -->

<!-- review:SF-2026-ARXIV-2607-21909:start -->
### Claim Plane: Enforceable Change Intents and Dynamic Scope for Parallel Coding Agents

<!-- claim:SF-2026-ARXIV-2607-21909:start -->Parallel coding agents can independently produce locally valid changes while still interfering at integration time, expanding beyond planned scope, or relying on premises invalidated by concurrent work. Existing responses emphasize communication, isolated workspaces, late merge-time repair, continuous supervision, or post-hoc runtime recovery. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-21909:end -->

**为什么进入候选分母。** 摘要首要问题为“Parallel coding agents can independently produce locally valid changes while still interfering at integration time, expanding beyond planned scope, or relying on premises invalidated by concurrent work.”；它把 context、memory、能力或进度变成持久且可验证的 agent state。

**机制与状态边界。** Existing responses emphasize communication, isolated workspaces, late merge-time repair, continuous supervision, or post-hoc runtime recovery.

**证据证明什么。** A preliminary six-pair CooperBench mechanism check is reported only as feasibility evidence: static Claim Plane achieved 6/6 pair passes with full serialization, while dynamic scope retained parallel admission on half of the pairs, performed seven successful scope promotions, and failed closed on two undeclared mutations.

**证据没有证明什么。** We argue that separating probabilistic planning from deterministic authority provides a foundation for a future learned semantic-dependency model and frontier-model escalation only on unresolved cases. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/pdf/2607.21909v1#page=3 — Claim Plane Architecture and ChangeIntent; https://arxiv.org/pdf/2607.21909v1#page=4 — Admission and dependency invalidation。Evaluation：https://arxiv.org/pdf/2607.21909v1#page=7 — Comparative evaluation arms and setup。Limitations / counterevidence：https://arxiv.org/pdf/2607.21909v1#page=9 — Confidence escalation boundary; https://arxiv.org/pdf/2607.21909v1#page=10 — Evidence and disclosure boundary。

**Artifact boundary。** Not Disclosed — exact v1 exposes no uniquely versioned artifact locator used to enlarge the manuscript claim boundary.

**Trade-off 与共存边界。** 显式 agent state 改善恢复与控制，但增加状态陈旧、错误提交、跨轮污染和一致性责任。 论文自身的边界信号是：We argue that separating probabilistic planning from deterministic authority provides a foundation for a future learned semantic-dependency model and frontier-model escalation only on unresolved cases.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`AGENT-WORKFLOW`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-21909:end -->

<!-- review:SF-2026-ARXIV-2607-21910:start -->
### TRW: TRACE-RealWorld---An Auditable Consistency Contract for World Models as Materialized Views

<!-- claim:SF-2026-ARXIV-2607-21910:start -->World models let agents plan against predicted physical state, but that state drifts; re-observation is costly and delayed, and repair can fail. We present TRACE-RealWorld (TRW), to our knowledge the first commitment-level consistency contract for world models. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-21910:end -->

**为什么进入候选分母。** 摘要首要问题为“World models let agents plan against predicted physical state, but that state drifts; re-observation is costly and delayed, and repair can fail.”；它把 evidence identity、lineage、conflict 或 commit 变成显式系统状态。

**机制与状态边界。** We present TRACE-RealWorld (TRW), to our knowledge the first commitment-level consistency contract for world models.

**证据证明什么。** Adaptive refresh reduces stale execution but does not dominate fixed refresh on cost, coverage, or rescue outcomes.

**证据没有证明什么。** 8 Discussion and Limitations Adaptive refresh cannot detect a change absent from its process model or visible evidence; support, OOD, and normative gates bound where the predictor may authorize action, but thresholds remain declared, versioned institutional choices. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.21910v1#S5 — 5 The Flood-SAR System; https://arxiv.org/html/2607.21910v1#S5.SS1 — 5.1 Architecture。Evaluation：https://arxiv.org/html/2607.21910v1#S7 — 7 Evaluation; https://arxiv.org/html/2607.21910v1#A6 — Appendix F RQ2 Mechanism Study。Limitations / counterevidence：https://arxiv.org/html/2607.21910v1#S8 — 8 Discussion and Limitations; https://arxiv.org/html/2607.21910v1#S9 — 9 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/eyuchang/trace-worldmodel-flood-sar, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 显式 evidence state 提高可追溯性，但新增 lineage、冲突、commit 与恢复语义，状态本身也必须被验证。 论文自身的边界信号是：8 Discussion and Limitations Adaptive refresh cannot detect a change absent from its process model or visible evidence; support, OOD, and normative gates bound where the predictor may authorize action, but thresholds remain declared, versioned institutional choices.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`MULTIMODAL-WORLD-MODELS`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-21910:end -->

<!-- review:SF-2026-ARXIV-2607-21912:start -->
### Reliability-Contagion Feasibility in LLM Multi-Agent Networks

<!-- claim:SF-2026-ARXIV-2607-21912:start -->Communication allows large language model agents to pool evidence, but it also creates paths along which an erroneous claim can spread. We formulate a correction-aware network model that tracks susceptible, exposed, infectious, and corrected agents and derive its early-invasion condition for heterogeneous communication networks. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-21912:end -->

**为什么进入候选分母。** 摘要首要问题为“Communication allows large language model agents to pool evidence, but it also creates paths along which an erroneous claim can spread.”；它改变执行安全的 trust boundary、guard 或 failure detection。

**机制与状态边界。** We formulate a correction-aware network model that tracks susceptible, exposed, infectious, and corrected agents and derive its early-invasion condition for heterogeneous communication networks.

**证据证明什么。** Together, these results provide a tractable basis for selecting connectivity under explicit reliability and propagation constraints.

**证据没有证明什么。** Its location depends on signal accuracy, verification, correction, and lifetime exposure. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.21912v1#S6.SS1 — 6.1 Design; https://arxiv.org/html/2607.21912v1#S7.SS1 — 7.1 Design。Evaluation：https://arxiv.org/html/2607.21912v1#S3 — 3 Clean reliability benchmark; https://arxiv.org/html/2607.21912v1#S6.SS2 — 6.2 Results。Limitations / counterevidence：https://arxiv.org/html/2607.21912v1#S8 — 8 Discussion; https://arxiv.org/html/2607.21912v1#S9 — 9 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 新的安全控制点降低特定失败，但会引入误拒绝、旁路、观测不足或模型/任务迁移问题。 论文自身的边界信号是：Its location depends on signal accuracy, verification, correction, and lifetime exposure.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`AGENT-MULTI-AGENT`；evidence-stage relation：`corrective_evidence`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-21912:end -->

<!-- review:SF-2026-ARXIV-2607-21918:start -->
### Action-Conditioned World Model for Goal Plane Probe Guidance in Robotic Ultrasound

<!-- claim:SF-2026-ARXIV-2607-21918:start -->We present an action-conditioned world model framework for goal plane probe guidance in robotic ultrasound, with a focus on neck ultrasound scanning. Autonomous ultrasound tasks often require large numbers of probe-motion trajectories for training, but collecting high-quality demonstrations is labor-intensive and explicit simulators are difficult to build because ultrasound appearance depends on contact, tissue deformation, and view-dependent acoustic artifacts. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-21918:end -->

**为什么进入候选分母。** 摘要首要问题为“We present an action-conditioned world model framework for goal plane probe guidance in robotic ultrasound, with a focus on neck ultrasound scanning.”；它提出可跨 workload 讨论的表示、状态或计算机制，并暴露旧方案边界。

**机制与状态边界。** We present an action-conditioned world model framework for goal plane probe guidance in robotic ultrasound, with a focus on neck ultrasound scanning.

**证据证明什么。** These results demonstrate the potential of learned ultrasound dynamics for training goal-directed robotic probe navigation.

**证据没有证明什么。** Another limitation is that force control is used only at the robot control level and is not used as an input modality for either the world model or the action predictor. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.21918v1#S2 — II Methodology; https://arxiv.org/html/2607.21918v1#S2.SS2 — II-B Action-conditioned latent diffusion ultrasound world model。Evaluation：https://arxiv.org/html/2607.21918v1#S3 — III Experiment; https://arxiv.org/html/2607.21918v1#S3.SS1 — III-A Experimental setup。Limitations / counterevidence：https://arxiv.org/html/2607.21918v1#S4 — IV Discussion & Future work; https://arxiv.org/html/2607.21918v1#S5 — V Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 新表示或状态机制扩大能力边界，但带来额外训练、状态管理、稳定性或泛化假设。 论文自身的边界信号是：Another limitation is that force control is used only at the robot control level and is not used as an input modality for either the world model or the action predictor.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`MULTIMODAL-WORLD-MODELS`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-21918:end -->

<!-- review:SF-2026-ARXIV-2607-21927:start -->
### RIS-Kernel: A Model-Agnostic Architecture for Long-Context LLM Inference via Sparse Attention

<!-- claim:SF-2026-ARXIV-2607-21927:start -->Full self-attention in large language models scales as O(N^2), which limits long-context document analysis to 65,536 tokens and requires costly GPU clusters. The Reduced Interaction Sampling (RIS) inference engine addresses this constraint as a model-agnostic architecture. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-21927:end -->

**为什么进入候选分母。** 摘要首要问题为“Full self-attention in large language models scales as O(N^2), which limits long-context document analysis to 65,536 tokens and requires costly GPU clusters.”；它改变推理期状态放置、数据移动、执行控制或实时 SLO。

**机制与状态边界。** The Reduced Interaction Sampling (RIS) inference engine addresses this constraint as a model-agnostic architecture.

**证据证明什么。** In controlled evaluations at 32,768 tokens (where native dense attention serves as the upper bound), RIS-Stochastic at 1% density and 70 ensemble seeds achieves 75.00% accuracy, outperforming the native dense baseline (71.88%), while RIS-Stochastic at 5% density and 10 seeds matches it (71.88%).

**证据没有证明什么。** Exact v1 does not disclose a dedicated generalization or deployment guarantee beyond its stated evaluation scope. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.21927v1#S4 — 4 Methods: The RIS Implementation。Evaluation：https://arxiv.org/html/2607.21927v1#S2 — 2 Results; https://arxiv.org/html/2607.21927v1#S2.SS2 — 2.2 Empirical Evaluation。Limitations / counterevidence：https://arxiv.org/html/2607.21927v1#S3 — 3 Discussion。

**Artifact boundary。** Exact v1 links https://github.com/santosardr/riskernel, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更激进的缓存、迁移、并行或专用执行会换取吞吐/时延，同时增加配置依赖、资源压力与回退路径。 论文自身的边界信号是：Exact v1 does not disclose a dedicated generalization or deployment guarantee beyond its stated evaluation scope.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`MODEL-LONG-CONTEXT`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-21927:end -->

<!-- review:SF-2026-ARXIV-2607-21946:start -->
### Multi-Agent Debate and Visual Information Extraction for SeePhys Pro: A 1st-Place Technical Report from ICML 2026 AI4Math Track 3 Challenge

<!-- claim:SF-2026-ARXIV-2607-21946:start -->This technical report presents our approach to Challenge Track~3: SeePhys Pro at the 3rd AI for Math Workshop, where the task is to answer college-level physics questions whose statement and figure may be given partly or entirely as an image. Visual physics problems become substantially harder for large language models when the decisive information resides in a figure rather than in the text, and this modality gap widens as more of the problem migrates into the image. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-21946:end -->

**为什么进入候选分母。** 摘要首要问题为“This technical report presents our approach to Challenge Track~3: SeePhys Pro at the 3rd AI for Math Workshop, where the task is to answer college-level physics questions whose statement and figure may be given partly or entirely as an image.”；它改变 observable、对照组、判定粒度或外推边界，可能修正既有评测结论。

**机制与状态边界。** We address the task with a two-stage framework: a visual information extraction stage that re-expresses figure content as solver-readable text to close the modality gap, and a reasoning stage that orchestrates three heterogeneous solvers through multi-agent debate.

**证据证明什么。** The resulting pipeline improves overall accuracy over a single-agent baseline from 0.643 to 0.802 on the public split, and won 1st place on both the public and the private leaderboard (private overall 0.743).

**证据没有证明什么。** B.1 A Reasoning Failure on Text-Only Level 1 On level1_testmini_000087 (text-only: a block leaves a rough incline, , , and passes through a slot in a platform at height rotating at angular velocity ), GPT-5.5 at xhigh , solving alone, derives the correct answer and then argues itself out of it: The answer existed in the candidate pool; the failure was in settling on it, which is exactly what the value-aware selection of Section 4.2 repairs. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.21946v1#S3 — 3 Methodology。Evaluation：https://arxiv.org/html/2607.21946v1#S4 — 4 Experiments; https://arxiv.org/html/2607.21946v1#S4.SS1 — 4.1 Experimental Settings。Limitations / counterevidence：https://arxiv.org/html/2607.21946v1#A2.SS1 — B.1 A Reasoning Failure on Text-Only Level 1; https://arxiv.org/html/2607.21946v1#A2.SS2 — B.2 A Perception Failure on Level 3 and Its Recovery。

**Artifact boundary。** Exact v1 links https://github.com/OpenDCAI/SciReasoner/tree/main/seephys_pro_codabench, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：B.1 A Reasoning Failure on Text-Only Level 1 On level1_testmini_000087 (text-only: a block leaves a rough incline, , , and passes through a slot in a platform at height rotating at angular velocity ), GPT-5.5 at xhigh , solving alone, derives the correct answer and then argues itself out of it: The answer existed in the candidate pool; the failure was in settling on it, which is exactly what the value-aware selection of Section 4.2 repairs.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`AGENT-MULTI-AGENT`；evidence-stage relation：`principle_reuse`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-21946:end -->

<!-- review:SF-2026-ARXIV-2607-21951:start -->
### SIREN (Luring LLMs onto the Rocks): PAIR-Driven Preference Manipulation in Web-RAG Recommenders

<!-- claim:SF-2026-ARXIV-2607-21951:start -->This paper investigates the adversarial manipulation of the ranked recommendations produced by web-augmented large language models (LLMs). When an LLM answers a recommendation query by retrieving and reading live webpages, it acts as a recommender, and each retrieved page becomes a potential attack surface. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-21951:end -->

**为什么进入候选分母。** 摘要首要问题为“This paper investigates the adversarial manipulation of the ranked recommendations produced by web-augmented large language models (LLMs).”；它改变执行安全的 trust boundary、guard 或 failure detection。

**机制与状态边界。** To address this gap, we propose SIREN, an automated attacker--judge method that adapts the PAIR jailbreaking loop to competitive rank manipulation, with the goal of moving a chosen entity to rank~1 in an LLM-generated recommendation.

**证据证明什么。** To the best of our knowledge, this is among the first controlled studies of competitive rank manipulation in production LLMs where the supplied source context is kept fixed.

**证据没有证明什么。** These findings do not support a uniform ordering between the target models. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.21951v1#S5 — 5. The SIREN Method; https://arxiv.org/html/2607.21951v1#A1 — Appendix A Results by Query–Model Context。Evaluation：https://arxiv.org/html/2607.21951v1#A1 — Appendix A Results by Query–Model Context; https://arxiv.org/html/2607.21951v1#A2 — Appendix B Per-Technique Full-Sweep Results。Limitations / counterevidence：https://arxiv.org/html/2607.21951v1#S10 — 10. Discussion; https://arxiv.org/html/2607.21951v1#S11 — 11. Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 新的安全控制点降低特定失败，但会引入误拒绝、旁路、观测不足或模型/任务迁移问题。 论文自身的边界信号是：These findings do not support a uniform ordering between the target models.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`AGENT-RAG`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-21951:end -->

<!-- review:SF-2026-ARXIV-2607-21958:start -->
### Efficient Online LLM Watermark Detection via Rao-Blackwellized E-Processes

<!-- claim:SF-2026-ARXIV-2607-21958:start -->As large language models (LLMs) are increasingly deployed, reliable and efficient mechanisms for distinguishing AI-generated text from human-written content have become essential. Statistical watermarking has emerged as a promising solution, yet most existing methods are typically fixed-horizon procedures, precluding valid early stopping in streaming generation. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-21958:end -->

**为什么进入候选分母。** 摘要首要问题为“As large language models (LLMs) are increasingly deployed, reliable and efficient mechanisms for distinguishing AI-generated text from human-written content have become essential.”；它把 evidence identity、lineage、conflict 或 commit 变成显式系统状态。

**机制与状态边界。** Statistical watermarking has emerged as a promising solution, yet most existing methods are typically fixed-horizon procedures, precluding valid early stopping in streaming generation.

**证据证明什么。** Simulations and experiments on real LLM-generated text demonstrate efficient online detection with rigorous anytime-valid guarantees.

**证据没有证明什么。** Despite these advances, existing approaches do not yet simultaneously provide a fully online and anytime-valid watermark detection procedure that avoids full-history dependence and does not rely on a carefully chosen anchor distribution. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.21958v1#S3.SS1 — 3.1 The proposed token-level pivot framework。Evaluation：https://arxiv.org/html/2607.21958v1#S5 — 5 Experiments; https://arxiv.org/html/2607.21958v1#S5.SS1 — 5.1 Synthetic experiments。Limitations / counterevidence：https://arxiv.org/html/2607.21958v1#S1 — 1 Introduction; https://arxiv.org/html/2607.21958v1#S2 — 2 Preliminaries。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 显式 evidence state 提高可追溯性，但新增 lineage、冲突、commit 与恢复语义，状态本身也必须被验证。 论文自身的边界信号是：Despite these advances, existing approaches do not yet simultaneously provide a fully online and anytime-valid watermark detection procedure that avoids full-history dependence and does not rely on a carefully chosen anchor distribution.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`PLATFORM-SECURITY`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-21958:end -->

<!-- review:SF-2026-ARXIV-2607-21962:start -->
### Ground Truth First: A Longitudinal Evaluation Instrument for Agent Memory, and the Tenure Crossover in Memory-Architecture Rankings

<!-- claim:SF-2026-ARXIV-2607-21962:start -->Benchmarks for LLM-agent memory typically generate conversations first and extract answer keys afterwards -- with documented label-error and contamination problems -- and they overwhelmingly measure short interaction histories. We invert the pipeline: a seeded life-script sampler emits facts with validity intervals, volatility classes, and source channels before any text exists; an LLM renderer writes chat and email from per-event fact manifests; a fidelity verifier confirms every planted fact; and questions are instantiated mechanically from the script, so gold answers are script-valid by construction and separately validated for answerability. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-21962:end -->

**为什么进入候选分母。** 摘要首要问题为“Benchmarks for LLM-agent memory typically generate conversations first and extract answer keys afterwards -- with documented label-error and contamination problems -- and they overwhelmingly measure short interaction histories.”；它改变 observable、对照组、判定粒度或外推边界，可能修正既有评测结论。

**机制与状态边界。** A full-rendered-history baseline ties or exceeds the best memory system at the short horizon but shows no judge-independent advantage at nine weeks, at about twice the read cost.

**证据证明什么。** A full-rendered-history baseline ties or exceeds the best memory system at the short horizon but shows no judge-independent advantage at nine weeks, at about twice the read cost.

**证据没有证明什么。** The instrument’s features (validity intervals, trust-typed channels, benign injection probes, as-of-date sets) surfaced phenomena the standard pipeline cannot see: a replicated ranking inversion with history length, an association between write-stage errors and downstream misses aligned fact-for-fact, injection resistance that tracked whether provenance boundaries survive representation, and a mismatch between overall accuracy and conditional abstention behavior. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.21962v1#S5.SS3 — 5.3 The layered architecture leads the memory systems at the short horizon; https://arxiv.org/html/2607.21962v1#S2.SS1 — 2.1 Agent memory architectures。Evaluation：https://arxiv.org/html/2607.21962v1#S2.SS2 — 2.2 Benchmarks, and the case for ground-truth-first generation; https://arxiv.org/html/2607.21962v1#S2.SS6 — 2.6 Confabulation, abstention, and judged evaluation。Limitations / counterevidence：https://arxiv.org/html/2607.21962v1#S8 — 8 Conclusion and future work; https://arxiv.org/html/2607.21962v1#S7 — 7 Threats to validity。

**Artifact boundary。** Exact v1 links https://github.com/veracium-ai/Veracium, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：The instrument’s features (validity intervals, trust-typed channels, benign injection probes, as-of-date sets) surfaced phenomena the standard pipeline cannot see: a replicated ranking inversion with history length, an association between write-stage errors and downstream misses aligned fact-for-fact, injection resistance that tracked whether provenance boundaries survive representation, and a mismatch between overall accuracy and conditional abstention behavior.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`AGENT-MEMORY`；evidence-stage relation：`corrective_evidence`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-21962:end -->

<!-- review:SF-2026-ARXIV-2607-21971:start -->
### Teaching LLMs to Self-Evolve: Cultivating Core Meta-Skills with Reinforcement Learning

<!-- claim:SF-2026-ARXIV-2607-21971:start -->Test-time scaling through iterative self-evolution with environment feedback, as demonstrated by AlphaEvolve, shows remarkable performance gains. We hypothesize that the success of such evolution frameworks hinges on meta-skills, such as self-reflection with environment feedback, that enable effective multi-round refinement, yet are largely neglected by traditional post-training. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-21971:end -->

**为什么进入候选分母。** 摘要首要问题为“Test-time scaling through iterative self-evolution with environment feedback, as demonstrated by AlphaEvolve, shows remarkable performance gains.”；它改变训练信号、capacity 或 update ownership，而非只报告任务精度。

**机制与状态边界。** To bridge this gap, we present MetaEvolve, a framework designed to develop these meta-skills via a data synthesis pipeline, evolution-aware reinforcement learning (RL), and inference-time evolutionary search.

**证据证明什么。** On open-ended algorithm optimization problems entirely outside the training domain, it further achieves a 46.9% relative improvement.

**证据没有证明什么。** Exact v1 does not disclose a dedicated generalization or deployment guarantee beyond its stated evaluation scope. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.21971v1#A1 — Appendix A GRPO Training Algorithm。Evaluation：https://arxiv.org/html/2607.21971v1#S3.SS2 — 3.2 Experiment Results; https://arxiv.org/html/2607.21971v1#A2 — Appendix B Evolution Ablations。Limitations / counterevidence：https://arxiv.org/html/2607.21971v1#S6 — 6 Conclusion。

**Artifact boundary。** Exact v1 links https://codeforces.com/, https://github.com/algorithmicsuperintelligence/openevolve, https://github.com/arXiv/html_feedback/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更密集或更定向的训练信号改善样本效率，但会增加 verifier 偏差、分布迁移和优化耦合。 论文自身的边界信号是：Exact v1 does not disclose a dedicated generalization or deployment guarantee beyond its stated evaluation scope.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`AGENT-REFLECTION`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-21971:end -->

<!-- review:SF-2026-ARXIV-2607-21978:start -->
### MoE$^2$-LoRA: When MoE Models Meet MoE-style Low-Rank Adaptation

<!-- claim:SF-2026-ARXIV-2607-21978:start -->Mixture-of-Experts (MoE) architectures have been widely adopted in large language models, yet parameter-efficient fine-tuning (PEFT) for MoE models remains underexplored. Existing PEFT methods for MoE either ignore router priors with uniform adapters, reducing efficiency and risking forgetting, or rely on static expert selection, limiting per-token capacity and cross-expert feature learning. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-21978:end -->

**为什么进入候选分母。** 摘要首要问题为“Mixture-of-Experts (MoE) architectures have been widely adopted in large language models, yet parameter-efficient fine-tuning (PEFT) for MoE models remains underexplored.”；它提出可跨 workload 讨论的表示、状态或计算机制，并暴露旧方案边界。

**机制与状态边界。** Existing PEFT methods for MoE either ignore router priors with uniform adapters, reducing efficiency and risking forgetting, or rely on static expert selection, limiting per-token capacity and cross-expert feature learning.

**证据证明什么。** Evaluated on multiple MoE backbones with varying scales and expert granularities, MoE$^2$-LoRA consistently achieves state-of-the-art downstream accuracy while retaining stronger general capabilities.

**证据没有证明什么。** Exact v1 does not disclose a dedicated generalization or deployment guarantee beyond its stated evaluation scope. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.21978v1#S3 — 3 Method; https://arxiv.org/html/2607.21978v1#S2.SS2 — 2.2 PEFT for MoE models.。Evaluation：https://arxiv.org/html/2607.21978v1#S4.SS2 — 4.2 Main Experimental Results; https://arxiv.org/html/2607.21978v1#A1.SS1 — A.1 Evaluation Protocol。Limitations / counterevidence：https://arxiv.org/html/2607.21978v1#S5 — 5 Analysis and Discussion; https://arxiv.org/html/2607.21978v1#S6 — 6 Conclusion。

**Artifact boundary。** Exact v1 links https://huggingface.co/datasets/xai-org/RealworldQA, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 新表示或状态机制扩大能力边界，但带来额外训练、状态管理、稳定性或泛化假设。 论文自身的边界信号是：Exact v1 does not disclose a dedicated generalization or deployment guarantee beyond its stated evaluation scope.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`TRAIN-LORA`；evidence-stage relation：`alternative_branch`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-21978:end -->

<!-- review:SF-2026-ARXIV-2607-21985:start -->
### Unified Static-Dynamic Pruning for Efficient LLM Inference

<!-- claim:SF-2026-ARXIV-2607-21985:start -->The increasing deployment of large language models (LLMs) has magnified the computational and memory bottlenecks of autoregressive decoding, where low compute intensity and bandwidth-bound kernels dominate inference cost. Weight pruning offers a promising remedy, but existing methods remain confined to either static pruning (SP), which permanently removes redundant weights but lacks adaptivity, or dynamic pruning (DP), which adapts to input sparsity but introduces runtime irregularity. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-21985:end -->

**为什么进入候选分母。** 摘要首要问题为“The increasing deployment of large language models (LLMs) has magnified the computational and memory bottlenecks of autoregressive decoding, where low compute intensity and bandwidth-bound kernels dominate inference cost.”；它改变资源计量、分配、路由或迁移的控制权与约束。

**机制与状态边界。** This paper presents SPDP, a unified sparse-inference framework that integrates unstructured SP with input-adaptive DP for efficient LLM inference on GPUs.

**证据证明什么。** SPDP advances the inference efficiency-quality Pareto frontier, showing that unified static-dynamic pruning can deliver substantial throughput and performance-per-watt improvements in large-scale LLM serving.

**证据没有证明什么。** However, quantization and unstructured sparsity do not provide multiplicative compression in practice: low-bit precision reduces only Values , while Bitmap , ColInfo , TileOffset , and padding remain. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.21985v1#S4 — 4. Design of SPDP: Unifying Static and Dynamic Sparsity; https://arxiv.org/html/2607.21985v1#S4.SS2 — 4.2. Decode Phase (spMspV) Kernel Design。Evaluation：https://arxiv.org/html/2607.21985v1#S3.SS1 — 3.1. Efficacy of Pruning: Roofline Analysis; https://arxiv.org/html/2607.21985v1#S5 — 5. Evaluation。Limitations / counterevidence：https://arxiv.org/html/2607.21985v1#S6 — 6. Discussion and Future Work; https://arxiv.org/html/2607.21985v1#S7 — 7. Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/AIDASLab/SPDP, https://huggingface.co/docs/transformers/index, https://github.com/tatsu-lab/stanford_alpaca; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 动态资源控制提高利用率，但增加测量误差、迁移开销、租户公平和控制稳定性问题。 论文自身的边界信号是：However, quantization and unstructured sparsity do not provide multiplicative compression in practice: low-bit precision reduces only Values , while Bitmap , ColInfo , TileOffset , and padding remain.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`INFER-DECODE`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-21985:end -->

<!-- review:SF-2026-ARXIV-2607-22000:start -->
### Music-JEPA: Learning a World Model of Sound from Action

<!-- claim:SF-2026-ARXIV-2607-22000:start -->Joint Embedding Predictive Architectures (JEPA) have recently emerged as a paradigm for learning world models by predicting latent representations, offering a promising direction for self-supervised learning. While initial attempts have applied JEPA to the music domain, it remains unclear how such frameworks can naturally support the formation of a world model for music. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-22000:end -->

**为什么进入候选分母。** 摘要首要问题为“Joint Embedding Predictive Architectures (JEPA) have recently emerged as a paradigm for learning world models by predicting latent representations, offering a promising direction for self-supervised learning.”；它提出可跨 workload 讨论的表示、状态或计算机制，并暴露旧方案边界。

**机制与状态边界。** In this work, we propose to learn a world model of piano sound using JEPA by framing music as an action-conditioned system: the audio is treated as the state, and the pianoroll as the instrument action.

**证据证明什么。** Experiments show that the learned model captures the relationships between musical actions and their resulting sound.

**证据没有证明什么。** We hope this work provides a foundation for future exploration. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.22000v1#S3 — 3 Method; https://arxiv.org/html/2607.22000v1#S3.SS2 — 3.2 Model Architecture。Evaluation：https://arxiv.org/html/2607.22000v1#S4 — 4 Experiments; https://arxiv.org/html/2607.22000v1#S4.SS3 — 4.3 Evaluation of Latent Dynamics。Limitations / counterevidence：https://arxiv.org/html/2607.22000v1#S5 — 5 Conclusion and Future Work。

**Artifact boundary。** Exact v1 links https://zzwaang.github.io/music-jepa-demo/, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 新表示或状态机制扩大能力边界，但带来额外训练、状态管理、稳定性或泛化假设。 论文自身的边界信号是：We hope this work provides a foundation for future exploration.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`MULTIMODAL-WORLD-MODELS`；evidence-stage relation：`alternative_branch`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-22000:end -->

<!-- review:SF-2026-ARXIV-2607-22002:start -->
### Learning as Reasoning Unfolds: Progressive Rollout Allocation for Efficient Reinforcement Learning

<!-- claim:SF-2026-ARXIV-2607-22002:start -->Reinforcement learning with verifiable rewards (RLVR) has emerged as a highly effective framework for improving LLM reasoning, with methods such as GRPO among its most successful instantiations. However, GRPO relies on repeated generation of long chain-of-thought rollouts. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-22002:end -->

**为什么进入候选分母。** 摘要首要问题为“Reinforcement learning with verifiable rewards (RLVR) has emerged as a highly effective framework for improving LLM reasoning, with methods such as GRPO among its most successful instantiations.”；它改变训练信号、capacity 或 update ownership，而非只报告任务精度。

**机制与状态边界。** Reinforcement learning with verifiable rewards (RLVR) has emerged as a highly effective framework for improving LLM reasoning, with methods such as GRPO among its most successful instantiations.

**证据证明什么。** Experiments on mathematical reasoning and coding tasks show that VIGOR reaches target accuracy with up to 2.3$\times$ fewer rollouts on math, reaches GRPO's final coding full pass rate with 1.49$\times$ fewer rollouts, and improves the coding average test pass rate by 3.4 points.

**证据没有证明什么。** By progressively allocating more rollout budget only to examples with larger within-group reward variance, VIGOR improves computational efficiency while preserving the original GRPO training paradigm. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.22002v1#S4 — 4 Method。Evaluation：https://arxiv.org/html/2607.22002v1#A1 — Appendix A Detailed Benchmark Results; https://arxiv.org/html/2607.22002v1#S5.SS3 — 5.3 Analysis and Ablation Study。Limitations / counterevidence：https://arxiv.org/html/2607.22002v1#S6 — 6 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/huggingface/Math-Verify, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更密集或更定向的训练信号改善样本效率，但会增加 verifier 偏差、分布迁移和优化耦合。 论文自身的边界信号是：By progressively allocating more rollout budget only to examples with larger within-group reward variance, VIGOR improves computational efficiency while preserving the original GRPO training paradigm.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`TRAIN-GRPO`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-22002:end -->

<!-- review:SF-2026-ARXIV-2607-22013:start -->
### Visual Saliency Steering Distillation for Multimodal Chain-of-Thought Reasoning

<!-- claim:SF-2026-ARXIV-2607-22013:start -->Multimodal chain-of-thought (CoT) reasoning integrates visual and textual cues through step-by-step inference. In small models with limited token budgets, modality-interaction fusion often suppresses tiny cross-modal differences. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-22013:end -->

**为什么进入候选分母。** 摘要首要问题为“Multimodal chain-of-thought (CoT) reasoning integrates visual and textual cues through step-by-step inference.”；它改变训练信号、capacity 或 update ownership，而非只报告任务精度。

**机制与状态边界。** In small models with limited token budgets, modality-interaction fusion often suppresses tiny cross-modal differences.

**证据证明什么。** Experiments on ScienceQA and M$^3$CoT demonstrate that VSSD improves rationale generation and answer inference.

**证据没有证明什么。** Future work will extend VSSD to broader multimodal reasoning tasks and explore more adaptive steering vector extraction. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.22013v1#S1 — 1 Introduction; https://arxiv.org/html/2607.22013v1#S2 — 2 Visual Saliency Steering Distillation。Evaluation：https://arxiv.org/html/2607.22013v1#S3 — 3 Experiment; https://arxiv.org/html/2607.22013v1#S3.SS1 — 3.1 Experiments Settings。Limitations / counterevidence：https://arxiv.org/html/2607.22013v1#S4 — 4 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/BGWH123/VSSD, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更密集或更定向的训练信号改善样本效率，但会增加 verifier 偏差、分布迁移和优化耦合。 论文自身的边界信号是：Future work will extend VSSD to broader multimodal reasoning tasks and explore more adaptive steering vector extraction.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`MULTIMODAL-REPRESENTATION`；evidence-stage relation：`alternative_branch`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-22013:end -->

<!-- review:SF-2026-ARXIV-2607-22014:start -->
### Zero-Shot Mission-Level Evaluation for Aerial MLLM Agents

<!-- claim:SF-2026-ARXIV-2607-22014:start -->Multimodal Large Language Models (MLLMs) are emerging as core reasoning modules for embodied agents, yet it remains unclear how well general-purpose models can solve long-horizon embodied tasks from a single high-level instruction. We introduce MissionBench, a benchmark for mission-level evaluation of MLLMs in aerial 3D environments. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-22014:end -->

**为什么进入候选分母。** 摘要首要问题为“Multimodal Large Language Models (MLLMs) are emerging as core reasoning modules for embodied agents, yet it remains unclear how well general-purpose models can solve long-horizon embodied tasks from a single high-level instruction.”；它改变 observable、对照组、判定粒度或外推边界，可能修正既有评测结论。

**机制与状态边界。** We introduce MissionBench, a benchmark for mission-level evaluation of MLLMs in aerial 3D environments.

**证据证明什么。** This motivates closed-loop evaluation and highlights both the promise and risk of scaling-driven improvements for embodied AI.

**证据没有证明什么。** Exact v1 does not disclose a dedicated generalization or deployment guarantee beyond its stated evaluation scope. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.22014v1#A4 — Appendix D Model Details。Evaluation：https://arxiv.org/html/2607.22014v1#A2 — Appendix B Extended Results; https://arxiv.org/html/2607.22014v1#A3 — Appendix C Additional Benchmark Details。Limitations / counterevidence：https://arxiv.org/html/2607.22014v1#A1 — Appendix A Further Discussion; https://arxiv.org/html/2607.22014v1#S5 — 5 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：Exact v1 does not disclose a dedicated generalization or deployment guarantee beyond its stated evaluation scope.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`PLATFORM-EVALUATION-SYSTEM`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-22014:end -->

<!-- review:SF-2026-ARXIV-2607-22022:start -->
### HEMERA: A Heterogeneous Memory-Centric Accelerator with Recursive Dataflow for Edge-Constrained State-Space-Duality Models Inference

<!-- claim:SF-2026-ARXIV-2607-22022:start -->Structured State Space Models (SSMs), such as Mamba, enable efficient long-sequence modeling with linear time complexity. Recent implementations realize this capability through Structured State Space Duality (SSD), which transforms recursive state evolution into matrix-form computations. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-22022:end -->

**为什么进入候选分母。** 摘要首要问题为“Structured State Space Models (SSMs), such as Mamba, enable efficient long-sequence modeling with linear time complexity.”；它改变资源计量、分配、路由或迁移的控制权与约束。

**机制与状态边界。** However, SSD introduces substantial system-level overheads, including quadratic intermediate materialization, irregular data movement, and prefix-dependent execution, leading to excessive memory traffic and bandwidth demand on conventional architectures.

**证据证明什么。** Across Mamba-2 models ranging from 130M to 2.8B, HEMERA achieves average latency speedups of 1.4x-3.6x and energy-efficiency improvements of 12.2x-27.0x over the official optimized fused Mamba-2 kernel on NVIDIA A100.

**证据没有证明什么。** Future work will explore extending this recursion-centric design framework to broader state-space and non-attention architectures under edge constraints. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.22022v1#S5 — 5. Hardware Design Details; https://arxiv.org/html/2607.22022v1#S5.SS2 — 5.2. Overall Architecture。Evaluation：https://arxiv.org/html/2607.22022v1#S6 — 6. Evaluation; https://arxiv.org/html/2607.22022v1#S6.SS1 — 6.1. Experiment Setup。Limitations / counterevidence：https://arxiv.org/html/2607.22022v1#S7 — 7. Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 动态资源控制提高利用率，但增加测量误差、迁移开销、租户公平和控制稳定性问题。 论文自身的边界信号是：Future work will explore extending this recursion-centric design framework to broader state-space and non-attention architectures under edge constraints.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`INFER-TENSORRT-LLM`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-22022:end -->

<!-- review:SF-2026-ARXIV-2607-22024:start -->
### Agent Security Needs Redefinition through a Holistic Framework

<!-- claim:SF-2026-ARXIV-2607-22024:start -->Agent security is widely treated as a question about action content. Defenses ask whether an instruction looks malicious. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-22024:end -->

**为什么进入候选分母。** 摘要首要问题为“Agent security is widely treated as a question about action content.”；它改变执行安全的 trust boundary、guard 或 failure detection。

**机制与状态边界。** Benchmarks ask whether an agent performs a harmful sounding action. \textbf{We argue that agent security is fundamentally a contextual problem, and that the current content based framing systematically misdefines it.} A command to ``delete user data'' might be a routine administrative request or a prompt injection attacking production systems, and the content alone cannot distinguish the two.

**证据证明什么。** The contextual reframing changes which defenses are coherent, which evaluations measure something useful, and which attack patterns evaluation can see at all.

**证据没有证明什么。** The same action is legitimate or a violation depending on who issued the command, what task the agent is pursuing, what each action serves, and how information flows across boundaries. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.22024v1#S6.SS2 — 6.2 Security Research Should Focus on Model Robustness。Evaluation：https://arxiv.org/html/2607.22024v1#A1 — Appendix A Full Benchmark Analysis; https://arxiv.org/html/2607.22024v1#S3.SS2 — 3.2 Continuous Evaluation Across Time。Limitations / counterevidence：https://arxiv.org/html/2607.22024v1#S8 — 8 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 新的安全控制点降低特定失败，但会引入误拒绝、旁路、观测不足或模型/任务迁移问题。 论文自身的边界信号是：The same action is legitimate or a violation depending on who issued the command, what task the agent is pursuing, what each action serves, and how information flows across boundaries.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`AGENT-PLATFORM`；evidence-stage relation：`structural_candidate`。
- Books 候选路由（尚非最终决定）：`Structural Candidate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-22024:end -->

<!-- review:SF-2026-ARXIV-2607-22034:start -->
### Small Vision-Language Models Know When They Are Wrong But Cannot Say So: A Two-Model Study of Stated versus Internal Confidence Under Realistic Image Degradation

<!-- claim:SF-2026-ARXIV-2607-22034:start -->Vision-language models (VLMs) are increasingly deployed on consumer hardware where input images are degraded by compression, camera shake, and poor lighting. In such settings, a reliable uncertainty signal matters more than raw accuracy, because it determines when a system should defer rather than answer. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-22034:end -->

**为什么进入候选分母。** 摘要首要问题为“Vision-language models (VLMs) are increasingly deployed on consumer hardware where input images are degraded by compression, camera shake, and poor lighting.”；它改变 observable、对照组、判定粒度或外推边界，可能修正既有评测结论。

**机制与状态边界。** In such settings, a reliable uncertainty signal matters more than raw accuracy, because it determines when a system should defer rather than answer.

**证据证明什么。** Across 3,800 predictions, we find a large and consistent gap.

**证据没有证明什么。** Whether small open-weight models refuse under degradation, and whether refusal correlates with low internal confidence, is an open question our design cannot address. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.22034v1#S3 — 3 Method; https://arxiv.org/html/2607.22034v1#S2.SS1 — 2.1 Verbalized uncertainty in language and vision-language models。Evaluation：https://arxiv.org/html/2607.22034v1#A1 — Appendix A Full results tables; https://arxiv.org/html/2607.22034v1#S4 — 4 Results。Limitations / counterevidence：https://arxiv.org/html/2607.22034v1#S5 — 5 Discussion; https://arxiv.org/html/2607.22034v1#S5.SS4 — 5.4 Limitations。

**Artifact boundary。** Exact v1 links https://github.com/Asif-Ferdous/vlm-reliability, https://huggingface.co/HuggingFaceTB/SmolVLM-Instruct, https://github.com/arXiv/html_feedback/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：Whether small open-weight models refuse under degradation, and whether refusal correlates with low internal confidence, is an open question our design cannot address.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`PLATFORM-EVALUATION-SYSTEM`；evidence-stage relation：`corrective_evidence`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-22034:end -->

<!-- review:SF-2026-ARXIV-2607-22038:start -->
### Sparse by Command: Task-Conditional Compute Skipping for Multi-Task Inference Accelerators

<!-- claim:SF-2026-ARXIV-2607-22038:start -->Multi-task inference models share a single backbone across diverse tasks, yet execute identical computation regardless of which task is active - wasting energy and cycles on task-irrelevant operations. We observe that the task command, typically available before inference begins, provides a free signal that can be exploited to skip unnecessary computation at the hardware level. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-22038:end -->

**为什么进入候选分母。** 摘要首要问题为“Multi-task inference models share a single backbone across diverse tasks, yet execute identical computation regardless of which task is active - wasting energy and cycles on task-irrelevant operations.”；它改变资源计量、分配、路由或迁移的控制权与约束。

**机制与状态边界。** We present a HW/SW co-designed approach in which a lightweight gating network, trained jointly with the backbone, predicts per-tile binary execution masks conditioned on the task input.

**证据证明什么。** Task-conditional sparsity reduces FLOPs by 66-76% while maintaining driving quality.

**证据没有证明什么。** Future work includes extending the gating mechanism to support input-conditional sparsity ( Verelst and Tuytelaars, 2020 ) (where the mask depends on both the task and the input image), exploring hierarchical masking at multiple granularities (block, layer, tile, channel), and scaling the accelerator to larger models and higher parallelism configurations on multi-SLR FPGA platforms. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.22038v1#S3 — 3. System Design; https://arxiv.org/html/2607.22038v1#A1.SS8 — A.8. Methodology。Evaluation：https://arxiv.org/html/2607.22038v1#A1.SS6 — A.6. Evaluation and expected results; https://arxiv.org/html/2607.22038v1#A1.SS5 — A.5. Experiment workflow。Limitations / counterevidence：https://arxiv.org/html/2607.22038v1#S6 — 6. Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/afzalxo/sparse-by-command, https://github.com/carla-simulator/carla/issues/4004, https://github.com/arXiv/html_feedback/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 动态资源控制提高利用率，但增加测量误差、迁移开销、租户公平和控制稳定性问题。 论文自身的边界信号是：Future work includes extending the gating mechanism to support input-conditional sparsity ( Verelst and Tuytelaars, 2020 ) (where the mask depends on both the task and the input image), exploring hierarchical masking at multiple granularities (block, layer, tile, channel), and scaling the accelerator to larger models and higher parallelism configurations on multi-SLR FPGA platforms.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`INFER-TENSORRT-LLM`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-22038:end -->

<!-- review:SF-2026-ARXIV-2607-22039:start -->
### Enough is as good as a feast: A Comprehensive Analysis of How Reinforcement Learning Mitigates Task Conflicts in LLMs

<!-- claim:SF-2026-ARXIV-2607-22039:start -->Model merging plays a crucial role in consolidating multiple specialized models into a single, unified model, especially in the era of large language models (LLMs). Recent research has primarily focused on developing strategies to enhance merging performance with the trained models, while the impact of training paradigms, such as supervised fine-tuning (SFT) and reinforcement learning (RL), on the effectiveness of model merging remains underexplored. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-22039:end -->

**为什么进入候选分母。** 摘要首要问题为“Model merging plays a crucial role in consolidating multiple specialized models into a single, unified model, especially in the era of large language models (LLMs).”；它改变训练信号、capacity 或 update ownership，而非只报告任务精度。

**机制与状态边界。** In this study, we systematically explore the merging behavior of RL-trained LLMs compared to those trained with traditional SFT.

**证据证明什么。** Through comprehensive evaluations across five representative tasks, we find that RL significantly reduces task conflicts and results in less performance degradation after merging, making RL-trained models particularly well-suited for this process.

**证据没有证明什么。** Taken together, our findings indicate that RL is not merely an alternative to SFT but constitutes a fundamentally more suitable paradigm for multi-task post-training in foundation models. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.22039v1#A1 — Appendix A The Use of Large Language Models; https://arxiv.org/html/2607.22039v1#A5.SS1 — E.1 The Number of Merging Model。Evaluation：https://arxiv.org/html/2607.22039v1#A3 — Appendix C Detailed Experiments Results; https://arxiv.org/html/2607.22039v1#A6.SS1 — F.1 Experiment Setup Details。Limitations / counterevidence：https://arxiv.org/html/2607.22039v1#S6 — 6 Conclusion。

**Artifact boundary。** Exact v1 links https://huggingface.co/models, https://github.com/OpenRLHF/OpenRLHF, https://github.com/volcengine/verl; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更密集或更定向的训练信号改善样本效率，但会增加 verifier 偏差、分布迁移和优化耦合。 论文自身的边界信号是：Taken together, our findings indicate that RL is not merely an alternative to SFT but constitutes a fundamentally more suitable paradigm for multi-task post-training in foundation models.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`TRAIN-GRPO`；evidence-stage relation：`corrective_evidence`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-22039:end -->

<!-- review:SF-2026-ARXIV-2607-22043:start -->
### Scaling Native Multimodal Pre-Training From Scratch

<!-- claim:SF-2026-ARXIV-2607-22043:start -->Although large language models (LLMs) exhibit remarkable reasoning capabilities, their reliance on text-only pre-training restricts the perception of the multimodal physical world. Native multimodal pre-training avoids this limitation by training models from scratch on multimodal inputs, thereby achieving deep cross-modal integration and mitigating optimization asymmetries inherent to traditional late-fusion architectures. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-22043:end -->

**为什么进入候选分母。** 摘要首要问题为“Although large language models (LLMs) exhibit remarkable reasoning capabilities, their reliance on text-only pre-training restricts the perception of the multimodal physical world.”；它改变训练信号、capacity 或 update ownership，而非只报告任务精度。

**机制与状态边界。** Despite these advantages, the scaling properties of this paradigm remain systematically uncharacterized.

**证据证明什么。** We demonstrate that minimal objective loss adheres to a predictable compute law, whereas compute-optimal model sizes and token counts scale as power laws.

**证据没有证明什么。** Specifically, language scaling remains largely insensitive to data composition, whereas multimodal scaling depends heavily on the multimodal data ratio. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.22043v1#A1 — Appendix A Implementation Details; https://arxiv.org/html/2607.22043v1#S4.SS1 — 4.1 Evaluation of Base Models。Evaluation：https://arxiv.org/html/2607.22043v1#A2 — Appendix B Experiment Results; https://arxiv.org/html/2607.22043v1#S2.SS3 — 2.3 Experimental Setup。Limitations / counterevidence：https://arxiv.org/html/2607.22043v1#S6 — 6 Conclusion。

**Artifact boundary。** Exact v1 links https://huggingface.co/datasets/xai-org/RealworldQA, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更密集或更定向的训练信号改善样本效率，但会增加 verifier 偏差、分布迁移和优化耦合。 论文自身的边界信号是：Specifically, language scaling remains largely insensitive to data composition, whereas multimodal scaling depends heavily on the multimodal data ratio.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`MULTIMODAL-REPRESENTATION`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-22043:end -->

<!-- review:SF-2026-ARXIV-2607-22083:start -->
### Nanbeige4.2-3B: Unlocking Agentic Capabilities in a Compact Model

<!-- claim:SF-2026-ARXIV-2607-22083:start -->We present Nanbeige4.2-3B, a compact general agentic model with 3B non-embedding parameters. It delivers strong performance across code-agent, office-agent, and complex tool-use tasks while maintaining highly competitive reasoning capabilities in mathematics, coding, and science. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-22083:end -->

**为什么进入候选分母。** 摘要首要问题为“We present Nanbeige4.2-3B, a compact general agentic model with 3B non-embedding parameters.”；它提出可跨 workload 讨论的表示、状态或计算机制，并暴露旧方案边界。

**机制与状态边界。** We present Nanbeige4.2-3B, a compact general agentic model with 3B non-embedding parameters.

**证据证明什么。** Extensive evaluations show that Nanbeige4.2-3B outperforms larger models, including Qwen3.5-9B and Gemma4-12B, across diverse agentic benchmarks while remaining competitive on reasoning and alignment tasks.

**证据没有证明什么。** Exact v1 does not disclose a dedicated generalization or deployment guarantee beyond its stated evaluation scope. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.22083v1#S2.SS1 — 2.1 Architecture。Evaluation：https://arxiv.org/html/2607.22083v1#A2 — Appendix B Evaluation settings; https://arxiv.org/html/2607.22083v1#A2.SS2 — B.2 Code Agent Evaluation。Limitations / counterevidence：https://arxiv.org/html/2607.22083v1#S4 — 4 Conclusion。

**Artifact boundary。** Exact v1 links https://huggingface.co/Nanbeige/Nanbeige4.2-3B, https://github.com/openclaw/openclaw, https://github.com/arXiv/html_feedback/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 新表示或状态机制扩大能力边界，但带来额外训练、状态管理、稳定性或泛化假设。 论文自身的边界信号是：Exact v1 does not disclose a dedicated generalization or deployment guarantee beyond its stated evaluation scope.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`AGENT-PLATFORM`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-22083:end -->

<!-- review:SF-2026-ARXIV-2607-22091:start -->
### Spectral Prior for Reducing Exposure Bias in Diffusion Models

<!-- claim:SF-2026-ARXIV-2607-22091:start -->Diffusion models typically suffer from error accumulation during iterative sampling, commonly referred to as exposure bias. We reveal systematic frequency-dependent discrepancies between training and inference, which can be interpreted as frequency-dependent SNR error. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-22091:end -->

**为什么进入候选分母。** 摘要首要问题为“Diffusion models typically suffer from error accumulation during iterative sampling, commonly referred to as exposure bias.”；它改变训练信号、capacity 或 update ownership，而非只报告任务精度。

**机制与状态边界。** We propose Spectral Alignment (SPA), a lightweight, guidance-based method that calibrates the power spectrum of intermediate predictions to a pre-computed prior.

**证据证明什么。** We demonstrate consistent improvements across diverse architectures, from pixel-space models (DDPM, ADM) to latent diffusion models (SD2.0, SDXL) and flow-matching models (SD3.5, FLUX).

**证据没有证明什么。** Exact v1 does not disclose a dedicated generalization or deployment guarantee beyond its stated evaluation scope. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.22091v1#Pt0.A4 — Appendix 0.D Implementation Details of the Baseline Methods; https://arxiv.org/html/2607.22091v1#S2.SS3 — 2.3 Motivation for the Proposed Method。Evaluation：https://arxiv.org/html/2607.22091v1#Pt0.A3 — Appendix 0.C Analysis of the Hyperparameters; https://arxiv.org/html/2607.22091v1#Pt0.A3.SS1 — 0.C.1 Analysis on the guidance strength。Limitations / counterevidence：https://arxiv.org/html/2607.22091v1#S6 — 6 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/SonyResearch/SPA, https://huggingface.co/black-forest-labs/FLUX.1-dev, https://huggingface.co/nyanko7/flux-dev-de-distill; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更密集或更定向的训练信号改善样本效率，但会增加 verifier 偏差、分布迁移和优化耦合。 论文自身的边界信号是：Exact v1 does not disclose a dedicated generalization or deployment guarantee beyond its stated evaluation scope.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`MULTIMODAL-GENERATIVE-PARADIGMS`；evidence-stage relation：`corrective_evidence`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-22091:end -->

<!-- review:SF-2026-ARXIV-2607-22098:start -->
### Reasoning Denoiser: Denoising Reasoning Traces for Hallucination Detection in Large Reasoning Models

<!-- claim:SF-2026-ARXIV-2607-22098:start -->Large reasoning models (LRMs) generate long reasoning traces before producing final answers. While these traces may contain useful signals for hallucination detection, harnessing them is non-trivial because long trajectories often include noisy steps that obscure the cues relevant to truthfulness assessment. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-22098:end -->

**为什么进入候选分母。** 摘要首要问题为“Large reasoning models (LRMs) generate long reasoning traces before producing final answers.”；它改变 observable、对照组、判定粒度或外推边界，可能修正既有评测结论。

**机制与状态边界。** To address this challenge, we propose REDE, a novel learning framework for denoising reasoning traces for hallucination detection.

**证据证明什么。** Extensive experiments on multiple reasoning benchmarks show that REDE consistently improves detection performance over competitive baselines.

**证据没有证明什么。** At the same time, ReDe is not a guarantee of truthfulness. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.22098v1#A3.SS5 — C.5 Effect of truthfulness labeling methods; https://arxiv.org/html/2607.22098v1#S4 — 4 Method。Evaluation：https://arxiv.org/html/2607.22098v1#A1 — Appendix A Additional experimental details; https://arxiv.org/html/2607.22098v1#A2 — Appendix B Additional ablation studies。Limitations / counterevidence：https://arxiv.org/html/2607.22098v1#A4 — Appendix D Broader impact and limitations; https://arxiv.org/html/2607.22098v1#S7 — 7 Conclusion。

**Artifact boundary。** Exact v1 links https://huggingface.co/datasets/HuggingFaceH4/aime_2024, https://huggingface.co/datasets/opencompass/AIME2025, https://huggingface.co/MoritzLaurer/DeBERTa-v3-large-mnli-fever-anli-ling-wanli; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：At the same time, ReDe is not a guarantee of truthfulness.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`PLATFORM-EVALUATION-SYSTEM`；evidence-stage relation：`corrective_evidence`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-22098:end -->

<!-- review:SF-2026-ARXIV-2607-22119:start -->
### One Hand Watches The Other: Dynamic Multi-Agent Cooperation for Sample-Efficient Bimanual Manipulation in Dynamic Environments

<!-- claim:SF-2026-ARXIV-2607-22119:start -->Multi-stream robot manipulation policies achieve unparalleled sample efficiency and generalization by modeling actions relative to environmental reference frames. However, existing approaches typically assume these frames to be strictly exogenous. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-22119:end -->

**为什么进入候选分母。** 摘要首要问题为“Multi-stream robot manipulation policies achieve unparalleled sample efficiency and generalization by modeling actions relative to environmental reference frames.”；它把 context、memory、能力或进度变成持久且可验证的 agent state。

**机制与状态边界。** We propose DynaMAC, a lightweight, policy-agnostic framework that resolves this causal limitation while preserving the sample efficiency, computational speed, and flexibility of multi-stream policies, DynaMAC treats the opposite arm as a dynamic task parameter, thereby providing a unified formulation for dynamic manipulation and bimanual coordination without requiring an explicit leader-follower relationship.

**证据证明什么。** Multi-stream robot manipulation policies achieve unparalleled sample efficiency and generalization by modeling actions relative to environmental reference frames.

**证据没有证明什么。** Limitations and Future Work: By building on multi-stream learning, DynaMAC inherits some of its structural limitations, namely the requirement that individual skills can be segmented from long-horizon tasks [ 2 ] , and the reliance on an external vision encoder module. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.22119v1#S3 — III Technical Approach。Evaluation：https://arxiv.org/html/2607.22119v1#S5 — V Experimental Evaluation; https://arxiv.org/html/2607.22119v1#S4 — IV DynaBench: A Dynamic Environment Manipulation Benchmark。Limitations / counterevidence：https://arxiv.org/html/2607.22119v1#S6 — VI Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 显式 agent state 改善恢复与控制，但增加状态陈旧、错误提交、跨轮污染和一致性责任。 论文自身的边界信号是：Limitations and Future Work: By building on multi-stream learning, DynaMAC inherits some of its structural limitations, namely the requirement that individual skills can be segmented from long-horizon tasks [ 2 ] , and the reliance on an external vision encoder module.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`AGENT-MULTI-AGENT`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-22119:end -->

<!-- review:SF-2026-ARXIV-2607-22157:start -->
### Learning on the Job: Continual Learning from Deployment Feedback for Frozen-Weights Agents

<!-- claim:SF-2026-ARXIV-2607-22157:start -->AI agents encounter learning opportunities in every episode they run, and discard nearly all of them: the underlying models are frozen at deployment, so an agent that resolves a difficult request today starts from zero when it recurs tomorrow. Yet ordinary operation already produces feedback, in the form of outcome verdicts and after-the-fact corrections. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-22157:end -->

**为什么进入候选分母。** 摘要首要问题为“AI agents encounter learning opportunities in every episode they run, and discard nearly all of them: the underlying models are frozen at deployment, so an agent that resolves a difficult request today starts from zero when it recurs tomorrow.”；它把 context、memory、能力或进度变成持久且可验证的 agent state。

**机制与状态边界。** Yet ordinary operation already produces feedback, in the form of outcome verdicts and after-the-fact corrections.

**证据证明什么。** We show that this feedback is a sufficient signal for continual learning when the frozen model is paired with an external memory that distils each episode into retrievable natural-language rules.

**证据没有证明什么。** At pass^4 the metric cannot distinguish that task from one never solved, so a learning agent’s advantage should shrink as grows and vanish at . 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.22157v1#A1.SS1 — A.1 Memory advertisement in the system prompt; https://arxiv.org/html/2607.22157v1#A5 — Appendix E Statistical methodology。Evaluation：https://arxiv.org/html/2607.22157v1#A2 — Appendix B Transfer experiment details; https://arxiv.org/html/2607.22157v1#S3 — 3 Experimental Setup。Limitations / counterevidence：https://arxiv.org/html/2607.22157v1#S5 — 5 Discussion; https://arxiv.org/html/2607.22157v1#S6 — 6 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/memcoai/spark-continual-learning-paper-data, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 显式 agent state 改善恢复与控制，但增加状态陈旧、错误提交、跨轮污染和一致性责任。 论文自身的边界信号是：At pass^4 the metric cannot distinguish that task from one never solved, so a learning agent’s advantage should shrink as grows and vanish at .

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`AGENT-MEMORY`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-22157:end -->

<!-- review:SF-2026-ARXIV-2607-22165:start -->
### DBA-Bench: A Production-Fidelity Benchmark for LLM-Based Database Operations Agents

<!-- claim:SF-2026-ARXIV-2607-22165:start -->LLM-based database agents show promise, but differing task scopes, testbeds, and metrics hinder comparison. We identify four gaps between evaluation and production operations: live-environment fidelity (multi-turn read-write interaction with a running database); observation-space scale and complexity (causal diagnosis across thousands of time series, business logs, and concurrent activity); solution-space openness (multiple remediations with different operational trade-offs); and scenario complexity and coverage (faults cascading across internal mechanisms and operational domains). 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-22165:end -->

**为什么进入候选分母。** 摘要首要问题为“LLM-based database agents show promise, but differing task scopes, testbeds, and metrics hinder comparison.”；它改变 observable、对照组、判定粒度或外推边界，可能修正既有评测结论。

**机制与状态边界。** We evaluate nine baseline groups, including six foundation-model systems, two GPT-5.5-backed database agents, and a Human DBA reference.

**证据证明什么。** LLM-based database agents show promise, but differing task scopes, testbeds, and metrics hinder comparison.

**证据没有证明什么。** Conclusion Evaluations based on curated observations, recommendation-only answers, or non-reproducible testbeds can overestimate whether an LLM agent can diagnose and safely remediate a live database incident. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.22165v1#S6.SS5 — 6.5. Fixed-backbone Agent-System Comparison; https://arxiv.org/html/2607.22165v1#S7.SS1 — 7.1. Implications for Database-Agent Design。Evaluation：https://arxiv.org/html/2607.22165v1#S3.SS4 — 3.4. Evaluation Interface: Post-fix State, Report, and Trace; https://arxiv.org/html/2607.22165v1#S5 — 5. Evaluation Protocol。Limitations / counterevidence：https://arxiv.org/html/2607.22165v1#S7 — 7. Discussion; https://arxiv.org/html/2607.22165v1#S8 — 8. Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/TanJI-C/DBA-Bench, https://github.com/TsinghuaDatabaseGroup/DB-GPT, https://github.com/arXiv/html_feedback/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：Conclusion Evaluations based on curated observations, recommendation-only answers, or non-reproducible testbeds can overestimate whether an LLM agent can diagnose and safely remediate a live database incident.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`AGENT-TOOL-CALLING`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-22165:end -->

<!-- review:SF-2026-ARXIV-2607-22182:start -->
### From Isolated Tasks to Structured Capabilities: A Multilayer Taxonomy for Large Language Models

<!-- claim:SF-2026-ARXIV-2607-22182:start -->Large language model (LLM) evaluation spans diverse tasks and benchmarks, yet evidence remains organized around tasks rather than the capabilities they probe. This fragmentation limits cross-study comparison, obscures capabilities tasks recruit, and makes coverage gaps difficult to identify. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-22182:end -->

**为什么进入候选分母。** 摘要首要问题为“Large language model (LLM) evaluation spans diverse tasks and benchmarks, yet evidence remains organized around tasks rather than the capabilities they probe.”；它改变 observable、对照组、判定粒度或外推边界，可能修正既有评测结论。

**机制与状态边界。** We introduce a multi-layer taxonomy of 14 capability domains and 91 subskills across Primitive, Constructed, and Integrative layers.

**证据证明什么。** To demonstrate operational utility, we screened 31,505 papers from ACL, AAAI, ICML, and NeurIPS between 2023 and 2025 and mapped 15,934 LLM-focused papers through multi-model annotation, consensus, and arbitration.

**证据没有证明什么。** First, the taxonomy is not a blueprint for LLM architecture. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.22182v1#S2 — 2 Taxonomy Design Principles and Construction; https://arxiv.org/html/2607.22182v1#S2.SS1 — 2.1 Scope and Design Objective。Evaluation：https://arxiv.org/html/2607.22182v1#S4.SS2 — 4.2 Results; https://arxiv.org/html/2607.22182v1#S5.SS2 — 5.2 Implications for Evaluation Design and Capability Diagnosis。Limitations / counterevidence：https://arxiv.org/html/2607.22182v1#S5 — 5 Discussion and Conclusion; https://arxiv.org/html/2607.22182v1#S5.SS4 — 5.4 Limitations and Boundary Conditions。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：First, the taxonomy is not a blueprint for LLM architecture.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`WORLDVIEW-KNOWLEDGE-TREE`；evidence-stage relation：`principle_reuse`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-22182:end -->

<!-- review:SF-2026-ARXIV-2607-22186:start -->
### Deconstructing Off-Policy Ratios: Entropy-Scaled Trust Regions for Asynchronous Reinforcement Learning

<!-- claim:SF-2026-ARXIV-2607-22186:start -->Asynchronous reinforcement learning (RL) accelerates large language model (LLM) post-training by overlapping rollout generation with policy optimization, but the resulting stale, off-policy data can destabilize optimization and ultimately cause policy collapse. Existing methods typically retain or discard tokens based solely on the magnitude of their importance ratios, applying the same threshold uniformly across token positions. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-22186:end -->

**为什么进入候选分母。** 摘要首要问题为“Asynchronous reinforcement learning (RL) accelerates large language model (LLM) post-training by overlapping rollout generation with policy optimization, but the resulting stale, off-policy data can destabilize optimization and ultimately cause policy collapse.”；它改变训练信号、capacity 或 update ownership，而非只报告任务精度。

**机制与状态边界。** In this work, we reveal that the natural scale of the importance ratio varies systematically with token entropy.

**证据证明什么。** Across long-horizon agentic tasks and mathematical reasoning benchmarks, ESTR consistently outperforms existing asynchronous methods and achieves the best train-inference consistency.

**证据没有证明什么。** Future work will explore extending this framework to tackle problem-solving in even longer-horizon agentic tasks under extreme asynchronous regimes. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.22186v1#S3.SS3 — 3.3 An Entropy-Scaled Design Principle; https://arxiv.org/html/2607.22186v1#S4 — 4 Method。Evaluation：https://arxiv.org/html/2607.22186v1#S5 — 5 Experiment。Limitations / counterevidence：https://arxiv.org/html/2607.22186v1#S6 — 6 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更密集或更定向的训练信号改善样本效率，但会增加 verifier 偏差、分布迁移和优化耦合。 论文自身的边界信号是：Future work will explore extending this framework to tackle problem-solving in even longer-horizon agentic tasks under extreme asynchronous regimes.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`TRAIN-GRPO`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-22186:end -->

<!-- review:SF-2026-ARXIV-2607-22188:start -->
### Draining the Energy Commons: Self-Defeating Over-Appropriation as a Coordination Failure in Agentic LLM Collectives

<!-- claim:SF-2026-ARXIV-2607-22188:start -->LLMs are increasingly deployed as agents that plan, use tools, and act over time. When they share persistent resources, such as compute pools or energy reserves, decisions by one agent affect the conditions faced by later agents. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-22188:end -->

**为什么进入候选分母。** 摘要首要问题为“LLMs are increasingly deployed as agents that plan, use tools, and act over time.”；它改变执行安全的 trust boundary、guard 或 failure detection。

**机制与状态边界。** This system-level alignment failure would be missed by isolated-response evaluation.

**证据证明什么。** This system-level alignment failure would be missed by isolated-response evaluation.

**证据没有证明什么。** Such failures may result from conflict, collusion, or miscoordination, and they cannot always be identified by evaluating each agent in isolation ( Hammond et al., 2025 ; Bisconti et al., 2025 ) . 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.22188v1#S3 — 3 Experimental Design; https://arxiv.org/html/2607.22188v1#S3.SS1 — 3.1 Design logic。Evaluation：https://arxiv.org/html/2607.22188v1#Ax4 — Appendix D. Benchmark checks, request specifications, and exact tests; https://arxiv.org/html/2607.22188v1#S2.SS2 — 2.2 Strategic LLMs and public-resource evaluation。Limitations / counterevidence：https://arxiv.org/html/2607.22188v1#S2.SS1 — 2.1 From single-agent to multi-agent alignment failures; https://arxiv.org/html/2607.22188v1#S5 — 5 Discussion。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 新的安全控制点降低特定失败，但会引入误拒绝、旁路、观测不足或模型/任务迁移问题。 论文自身的边界信号是：Such failures may result from conflict, collusion, or miscoordination, and they cannot always be identified by evaluating each agent in isolation ( Hammond et al., 2025 ; Bisconti et al., 2025 ) .

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`AGENT-MULTI-AGENT`；evidence-stage relation：`corrective_evidence`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-22188:end -->

<!-- review:SF-2026-ARXIV-2607-22199:start -->
### From Score Approximation to Distribution Approximation in Score-Based Diffusion Models

<!-- claim:SF-2026-ARXIV-2607-22199:start -->Score-based diffusion models have achieved remarkable empirical success in generative modeling, yet their approximation-theoretic foundations remain incomplete. In particular, although classical universal approximation theorems guarantee that neural networks can approximate score functions, it remains unclear whether such approximation guarantees translate into approximation of the probability distributions generated by reverse diffusion processes. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-22199:end -->

**为什么进入候选分母。** 摘要首要问题为“Score-based diffusion models have achieved remarkable empirical success in generative modeling, yet their approximation-theoretic foundations remain incomplete.”；它提出可跨 workload 讨论的表示、状态或计算机制，并暴露旧方案边界。

**机制与状态边界。** In particular, although classical universal approximation theorems guarantee that neural networks can approximate score functions, it remains unclear whether such approximation guarantees translate into approximation of the probability distributions generated by reverse diffusion processes.

**证据证明什么。** Score-based diffusion models have achieved remarkable empirical success in generative modeling, yet their approximation-theoretic foundations remain incomplete.

**证据没有证明什么。** 8 Extensions and Future Directions The present work establishes a direct connection between approximation of the score function and approximation of the generated probability distribution in Kullback–Leibler divergence. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.22199v1#S8.SS3 — 8.3 General Diffusion Models; https://arxiv.org/html/2607.22199v1#S8.SS5 — 8.5 Learning Theory for Diffusion Models。Evaluation：https://arxiv.org/html/2607.22199v1#S1 — 1 Introduction; https://arxiv.org/html/2607.22199v1#S2 — 2 Related Work。Limitations / counterevidence：https://arxiv.org/html/2607.22199v1#S8 — 8 Extensions and Future Directions。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 新表示或状态机制扩大能力边界，但带来额外训练、状态管理、稳定性或泛化假设。 论文自身的边界信号是：8 Extensions and Future Directions The present work establishes a direct connection between approximation of the score function and approximation of the generated probability distribution in Kullback–Leibler divergence.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`MULTIMODAL-GENERATIVE-PARADIGMS`；evidence-stage relation：`corrective_evidence`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-22199:end -->

<!-- review:SF-2026-ARXIV-2607-22225:start -->
### Safe Learning Predictive Control for Ego-World Robotic Systems

<!-- claim:SF-2026-ARXIV-2607-22225:start -->Safe autonomous navigation in shared environments requires the ability to anticipate and react to the latent behaviors of surrounding robots. In this paper, we propose SOWL-MPC, a safe learning-based predictive control strategy for a novel scenario, which we name ego-world robotic framework. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-22225:end -->

**为什么进入候选分母。** 摘要首要问题为“Safe autonomous navigation in shared environments requires the ability to anticipate and react to the latent behaviors of surrounding robots.”；它改变执行安全的 trust boundary、guard 或 failure detection。

**机制与状态边界。** In this paper, we propose SOWL-MPC, a safe learning-based predictive control strategy for a novel scenario, which we name ego-world robotic framework.

**证据证明什么。** The real-time feasibility and safety guarantees of SOWL-MPC are demonstrated through extensive Monte Carlo virtual experiments in ROS 2, and validated on real-world robotic hardware in an indoor arena.

**证据没有证明什么。** Exact v1 does not disclose a dedicated generalization or deployment guarantee beyond its stated evaluation scope. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.22225v1#S2.SS1 — II-A Safe Control of Ego–World Robotic Systems; https://arxiv.org/html/2607.22225v1#S4.SS2 — IV-B Ego–World Vehicle Models for MPC Design。Evaluation：https://arxiv.org/html/2607.22225v1#S4 — IV Virtual Experiments; https://arxiv.org/html/2607.22225v1#S4.SS3 — IV-C Virtual Experiment on ETHZ Mobil Track。Limitations / counterevidence：https://arxiv.org/html/2607.22225v1#S6 — VI Conclusions。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 新的安全控制点降低特定失败，但会引入误拒绝、旁路、观测不足或模型/任务迁移问题。 论文自身的边界信号是：Exact v1 does not disclose a dedicated generalization or deployment guarantee beyond its stated evaluation scope.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`MULTIMODAL-WORLD-MODELS`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-22225:end -->

<!-- review:SF-2026-ARXIV-2607-22242:start -->
### Agentic CPU-GPU Scheduling for Heterogeneous AI Workloads

<!-- claim:SF-2026-ARXIV-2607-22242:start -->Agentic AI systems compose heterogeneous tool workloads on shared GPU/CPU infrastructure, yet existing frameworks assign all GPU-capable tools to the GPU by default. We profile 19 AI tools across GPU and CPU and find that 11 are GPU-preferred, 4 are ambiguous, 1 is CPU-preferred due to PCIe transfer dominance, and 3 are device-neutral, establishing that blanket GPU-first scheduling is suboptimal. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-22242:end -->

**为什么进入候选分母。** 摘要首要问题为“Agentic AI systems compose heterogeneous tool workloads on shared GPU/CPU infrastructure, yet existing frameworks assign all GPU-capable tools to the GPU by default.”；它改变资源计量、分配、路由或迁移的控制权与约束。

**机制与状态边界。** Agentic AI systems compose heterogeneous tool workloads on shared GPU/CPU infrastructure, yet existing frameworks assign all GPU-capable tools to the GPU by default.

**证据证明什么。** Across 13 scenarios spanning serial execution, parallel contention, and memory-constrained execution, the agentic scheduler reaches the brute-force optimal mapping in all 13 scenarios, matching the best classical baseline on mapping accuracy while avoiding bandit-style exploration over complete mappings, and outperforming HEFT, StarPU, and the all-GPU policy while requiring zero offline training.

**证据没有证明什么。** A future data-driven policy could trigger exploration only when runtime measurements reveal unexplored feasible placements. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.22242v1#S3 — 3. Proposed Agentic Scheduler Design。Evaluation：https://arxiv.org/html/2607.22242v1#A1 — Appendix A S13 Ablation Study; https://arxiv.org/html/2607.22242v1#S4 — 4. Evaluation。Limitations / counterevidence：https://arxiv.org/html/2607.22242v1#S5 — 5. Discussion; https://arxiv.org/html/2607.22242v1#S7 — 7. Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/crewAIInc/crewAI, https://github.com/langchain-ai/langgraph, https://github.com/arXiv/html_feedback/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 动态资源控制提高利用率，但增加测量误差、迁移开销、租户公平和控制稳定性问题。 论文自身的边界信号是：A future data-driven policy could trigger exploration only when runtime measurements reveal unexplored feasible placements.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`PLATFORM-GPU-SCHEDULER`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-22242:end -->

<!-- review:SF-2026-ARXIV-2607-22251:start -->
### IFCLoRA: Topology-Aware Rank Allocation for Parameter-Efficient Fine-Tuning

<!-- claim:SF-2026-ARXIV-2607-22251:start -->Low-Rank Adaptation (LoRA) is a widely used approach to parameter-efficient fine-tuning (PEFT) of LLMs whose effectiveness depends on rank allocation. Existing adaptive LoRA methods derive ranks from local gradient, activation, or matrix statistics collected before or during fine-tuning; training-time variants add overhead, and local signals reveal little about each module's structural role in information propagation, giving weak global grounding for scarce-capacity allocation. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-22251:end -->

**为什么进入候选分母。** 摘要首要问题为“Low-Rank Adaptation (LoRA) is a widely used approach to parameter-efficient fine-tuning (PEFT) of LLMs whose effectiveness depends on rank allocation.”；它改变训练信号、capacity 或 update ownership，而非只报告任务精度。

**机制与状态边界。** We propose IFCLoRA, a topology-aware method for pre-fine-tuning rank allocation and adapter initialization.

**证据证明什么。** Across all settings, IFCLoRA achieves higher mean scores than standard LoRA with comparable fine-tuning time and peak memory; it requires a one-time offline calibration stage.

**证据没有证明什么。** This reframes low-budget adaptation as routing limited capacity along task-relevant information-flow paths. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.22251v1#A1.SS2 — A.2 Method-Specific Configurations; https://arxiv.org/html/2607.22251v1#S3 — 3 Method。Evaluation：https://arxiv.org/html/2607.22251v1#A1 — Appendix A Experimental Details; https://arxiv.org/html/2607.22251v1#A1.SS1 — A.1 Common Training and Evaluation Setup。Limitations / counterevidence：https://arxiv.org/html/2607.22251v1#S6 — 6 Conclusion and Future Work; https://arxiv.org/html/2607.22251v1#S5 — 5 Discussion。

**Artifact boundary。** Exact v1 links https://neurips.cc/public/guides/CodeSubmissionPolicy, https://paperswithcode.com/datasets, https://github.com/arXiv/html_feedback/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更密集或更定向的训练信号改善样本效率，但会增加 verifier 偏差、分布迁移和优化耦合。 论文自身的边界信号是：This reframes low-budget adaptation as routing limited capacity along task-relevant information-flow paths.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`TRAIN-LORA`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-22251:end -->

<!-- review:SF-2026-ARXIV-2607-22305:start -->
### A Roadmap to Impactful Pluralistic Alignment Research

<!-- claim:SF-2026-ARXIV-2607-22305:start -->Pluralistic value alignment---the goal of building AI systems that represent and serve diverse human values and perspectives---has emerged as an active research agenda. Yet, there's no public evidence that it has shaped the training or evaluation of the AI systems people actually use. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-22305:end -->

**为什么进入候选分母。** 摘要首要问题为“Pluralistic value alignment---the goal of building AI systems that represent and serve diverse human values and perspectives---has emerged as an active research agenda.”；它改变 observable、对照组、判定粒度或外推边界，可能修正既有评测结论。

**机制与状态边界。** Current methods trade off against other desiderata of LLMs in ways that are largely unmeasured, and existing metrics are not "hill-climbable." We need trade-off-aware evaluations and methods that meet the requirements of production systems.

**证据证明什么。** We need studies showing empirically how pluralistic AI benefits users or society.

**证据没有证明什么。** At this point, however, further research-scale progress alone cannot achieve the field’s goals, which are tied to the behavior of deployed frontier models (§ 1 ), and the cost of waiting grows as more users come to rely on models that fall well short of pluralistic ideals (§ 4.3 ). 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.22305v1#A1.SS2 — A.2 Model Evaluations: System Cards, Technical Reports; https://arxiv.org/html/2607.22305v1#S5.SS3 — 5.3 Evaluations and Methods That Model Developers Could Adopt。Evaluation：https://arxiv.org/html/2607.22305v1#A1.SS2 — A.2 Model Evaluations: System Cards, Technical Reports; https://arxiv.org/html/2607.22305v1#S5.SS3 — 5.3 Evaluations and Methods That Model Developers Could Adopt。Limitations / counterevidence：https://arxiv.org/html/2607.22305v1#S5 — 5 Call to Action: Future Directions; https://arxiv.org/html/2607.22305v1#S6 — 6 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/elinorp-d/scholar-trend-tracker, https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=ELEC&sectionNum=9084, https://github.com/xai-org/grok-prompts; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：At this point, however, further research-scale progress alone cannot achieve the field’s goals, which are tied to the behavior of deployed frontier models (§ 1 ), and the cost of waiting grows as more users come to rely on models that fall well short of pluralistic ideals (§ 4.3 ).

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`TRAIN-RLHF`；evidence-stage relation：`principle_reuse`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-22305:end -->

<!-- review:SF-2026-ARXIV-2607-22319:start -->
### Towards Trustworthy and Cost-Efficient Data Integration: From Naïve RAG to Agentic RAG

<!-- claim:SF-2026-ARXIV-2607-22319:start -->Large language models (LLMs) and AI agents have demonstrated strong potential for data integration in zero-shot and few-shot settings. However, they continue to face significant accuracy and cost challenges in enterprise environments due to a persistent knowledge gap. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-22319:end -->

**为什么进入候选分母。** 摘要首要问题为“Large language models (LLMs) and AI agents have demonstrated strong potential for data integration in zero-shot and few-shot settings.”；它把 context、memory、能力或进度变成持久且可验证的 agent state。

**机制与状态边界。** Finally, we outline open challenges and future directions toward building reliable, explainable, and scalable knowledge-grounded integration systems.

**证据证明什么。** Large language models (LLMs) and AI agents have demonstrated strong potential for data integration in zero-shot and few-shot settings.

**证据没有证明什么。** Exact v1 does not disclose a dedicated generalization or deployment guarantee beyond its stated evaluation scope. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.22319v1#S4.SS4 — 4.4 System Architecture。Evaluation：https://arxiv.org/html/2607.22319v1#S1 — 1 Introduction; https://arxiv.org/html/2607.22319v1#S2 — 2 Bridging the Knowledge Gap for LLM-based Data Integration。Limitations / counterevidence：https://arxiv.org/html/2607.22319v1#S6 — 6 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 显式 agent state 改善恢复与控制，但增加状态陈旧、错误提交、跨轮污染和一致性责任。 论文自身的边界信号是：Exact v1 does not disclose a dedicated generalization or deployment guarantee beyond its stated evaluation scope.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`AGENT-RAG`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-22319:end -->

<!-- review:SF-2026-ARXIV-2607-22334:start -->
### Cross-Tokenizer On-Policy Distillation via Byte-Prefix Marginalization

<!-- claim:SF-2026-ARXIV-2607-22334:start -->Open-weight language models from different families exhibit complementary capabilities, motivating their consolidation into a compact student through on-policy distillation (OPD). However, full-vocabulary OPD typically assumes a shared tokenizer, while existing cross-tokenizer methods may discard teacher probability mass or assign it to student tokens with unrelated content. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-22334:end -->

**为什么进入候选分母。** 摘要首要问题为“Open-weight language models from different families exhibit complementary capabilities, motivating their consolidation into a compact student through on-policy distillation (OPD).”；它改变训练信号、capacity 或 update ownership，而非只报告任务精度。

**机制与状态边界。** We introduce Byte-Prefix Marginalization (BPM), which re-expresses the teacher's next-token distribution over the student vocabulary in a shared byte space.

**证据证明什么。** Across Qwen3-32B, GLM-Z1-9B-0414, and MiniMax-M2.7 as teachers, BPM consistently outperforms current cross-tokenizer methods on six mathematics and programming benchmarks, improving six-benchmark avg@8 by 3.7-6.6 points over the strongest baselines.

**证据没有证明什么。** At whitespace-only code positions the target encodes only segmentation noise, and training on that noise collapses executable code. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.22334v1#A8.SS2 — H.2 Method-Agnostic Distributional Closeness; https://arxiv.org/html/2607.22334v1#S3 — 3 Method。Evaluation：https://arxiv.org/html/2607.22334v1#A8 — Appendix H Extended Results; https://arxiv.org/html/2607.22334v1#A8.SS1 — H.1 Per-Benchmark Scores for the Divergence Comparison。Limitations / counterevidence：https://arxiv.org/html/2607.22334v1#S5 — 5 Conclusion。

**Artifact boundary。** Exact v1 links https://huggingface.co/spaces/HuggingFaceH4/on-policy-distillation, https://huggingface.co/Qwen/Qwen3.5-2B, https://huggingface.co/zai-org/GLM-Z1-9B-0414; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更密集或更定向的训练信号改善样本效率，但会增加 verifier 偏差、分布迁移和优化耦合。 论文自身的边界信号是：At whitespace-only code positions the target encodes only segmentation noise, and training on that noise collapses executable code.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`TRAIN-SFT`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-22334:end -->

<!-- review:SF-2026-ARXIV-2607-22367:start -->
### Interior interpretability with attention rollout: contraction and propagation profiles in Transformers

<!-- claim:SF-2026-ARXIV-2607-22367:start -->Feature-attribution methods assign scores relating input variables to a model's output, but do not by themselves characterize how explicitly defined interaction operators compose across its intermediate layers. We introduce \emph{interior interpretability}, a propagation-based perspective on internal model organization, and instantiate it for tabular Transformers using attention rollout. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-22367:end -->

**为什么进入候选分母。** 摘要首要问题为“Feature-attribution methods assign scores relating input variables to a model's output, but do not by themselves characterize how explicitly defined interaction operators compose across its intermediate layers.”；它把 evidence identity、lineage、conflict 或 commit 变成显式系统状态。

**机制与状态边界。** We introduce \emph{interior interpretability}, a propagation-based perspective on internal model organization, and instantiate it for tabular Transformers using attention rollout.

**证据证明什么。** By applying classical Doeblin--Dobrushin contraction theory, we show that a rollout operator with a small Dobrushin coefficient is quantitatively close to a rank-one stochastic matrix whose common row is determined by its normalized column sums.

**证据没有证明什么。** Second, the product analysis provides a layerwise upper bound on rollout contraction but does not by itself prove decay with depth; moreover, the experiments report trained contraction only, while the trained–random-initialization comparison concerns propagation profiles rather than contraction coefficients. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.22367v1#S3.SS3 — 3.3. Interpretability methods; https://arxiv.org/html/2607.22367v1#S3.SS2 — 3.2. Model and training setup。Evaluation：https://arxiv.org/html/2607.22367v1#S4 — 4. Experimental results; https://arxiv.org/html/2607.22367v1#S4.SS1 — 4.1. Experimental results on Dataset 1。Limitations / counterevidence：https://arxiv.org/html/2607.22367v1#S4.SS3 — 4.3. Limitations of the empirical analysis; https://arxiv.org/html/2607.22367v1#S5 — 5. Conclusions and perspectives。

**Artifact boundary。** Exact v1 links https://github.com/umbertoBiccari/Attn_interpretability, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 显式 evidence state 提高可追溯性，但新增 lineage、冲突、commit 与恢复语义，状态本身也必须被验证。 论文自身的边界信号是：Second, the product analysis provides a layerwise upper bound on rollout contraction but does not by itself prove decay with depth; moreover, the experiments report trained contraction only, while the trained–random-initialization comparison concerns propagation profiles rather than contraction coefficients.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`MODEL-TRANSFORMER-LAYER`；evidence-stage relation：`corrective_evidence`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-22367:end -->

<!-- review:SF-2026-ARXIV-2607-22368:start -->
### Do Agent Benchmarks Measure Capability? Protocol Validity in the Age of Agentic AI

<!-- claim:SF-2026-ARXIV-2607-22368:start -->Agent benchmarks increasingly evaluate repository editing, web research, terminal use, and long-horizon interaction. Their scores support capability claims only when the evaluation protocol keeps the intended capability necessary for success. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-22368:end -->

**为什么进入候选分母。** 摘要首要问题为“Agent benchmarks increasingly evaluate repository editing, web research, terminal use, and long-horizon interaction.”；它改变 observable、对照组、判定粒度或外推边界，可能修正既有评测结论。

**机制与状态边界。** Recent reward-hacking benchmarks and system reports show that agents can instead recover public solutions, read evaluation artifacts, infer generator structure, manipulate feedback, or benefit from invalid scoring paths; existing responses do not provide a common procedure for attributing these shortcuts and quantifying their effect across benchmarks.

**证据证明什么。** Across paired comparisons, we measure score inflation of 0.45-1.00, showing that benchmark reports should provide evidence that scores reflect the intended capability.

**证据没有证明什么。** I.1 Future Work Two research directions could move benchmark verification from case-specific audit findings toward durable validity claims: • Formal protocol verification. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.22368v1#A8 — Appendix H Why Exposures Recur: Design Considerations; https://arxiv.org/html/2607.22368v1#S5.SS4 — 5.4 Independent Cases Support the Attribution Framework。Evaluation：https://arxiv.org/html/2607.22368v1#S5 — 5 Experimental Results; https://arxiv.org/html/2607.22368v1#A3.SS1 — C.1 Case 1 — Benchmark overexposure (SWE-bench Pro, OpenLibrary)。Limitations / counterevidence：https://arxiv.org/html/2607.22368v1#A9 — Appendix I Protocol-Specific Verification and Future Directions; https://arxiv.org/html/2607.22368v1#A9.SS1 — I.1 Future Work。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：I.1 Future Work Two research directions could move benchmark verification from case-specific audit findings toward durable validity claims: • Formal protocol verification.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`PLATFORM-EVALUATION-SYSTEM`；evidence-stage relation：`corrective_evidence`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-22368:end -->

<!-- review:SF-2026-ARXIV-2607-22385:start -->
### Agentic Root Cause Analysis through Evidence-Grounded Reasoning

<!-- claim:SF-2026-ARXIV-2607-22385:start -->Diagnosing the root cause of anomalies is essential for safe industrial operation. Despite extensive sensor instrumentation, formulating hypotheses and gathering evidence remains a manual process, creating a major operational bottleneck. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-22385:end -->

**为什么进入候选分母。** 摘要首要问题为“Diagnosing the root cause of anomalies is essential for safe industrial operation.”；它把 evidence identity、lineage、conflict 或 commit 变成显式系统状态。

**机制与状态边界。** To address this gap, we introduce AgentRCA, a zero-shot agentic framework for evidence-grounded root cause analysis.

**证据证明什么。** These results establish autonomous hypothesis-driven reasoning as a practical foundation for scalable industrial root cause analysis.

**证据没有证明什么。** These limitations define a clear trajectory for future research. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.22385v1#S2.SS1 — 2.1 Benchmark systems and evaluation protocol; https://arxiv.org/html/2607.22385v1#S2.SS6 — 2.6 AgentRCA extends to large multivariate industrial systems。Evaluation：https://arxiv.org/html/2607.22385v1#S2.SS1 — 2.1 Benchmark systems and evaluation protocol; https://arxiv.org/html/2607.22385v1#S2 — 2 Results。Limitations / counterevidence：https://arxiv.org/html/2607.22385v1#S3 — 3 Discussion。

**Artifact boundary。** Exact v1 links https://huggingface.co/Qwen/Qwen3-30B-A3B-Thinking-2507, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 显式 evidence state 提高可追溯性，但新增 lineage、冲突、commit 与恢复语义，状态本身也必须被验证。 论文自身的边界信号是：These limitations define a clear trajectory for future research.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`AGENT-REFLECTION`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-22385:end -->

<!-- review:SF-2026-ARXIV-2607-22389:start -->
### HiKV: Hierarchical Importance-Aware KV Cache with Hardware Acceleration for LLM Decoding

<!-- claim:SF-2026-ARXIV-2607-22389:start -->With the rapid adoption of long-context large language models (LLMs), the continuously growing KV cache during decoding has become the critical memory bottleneck. To tackle this challenge, we propose HiKV, a novel algorithm-hardware co-design that exploits KV cache redundancy through hierarchical importance awareness. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-22389:end -->

**为什么进入候选分母。** 摘要首要问题为“With the rapid adoption of long-context large language models (LLMs), the continuously growing KV cache during decoding has become the critical memory bottleneck.”；它改变资源计量、分配、路由或迁移的控制权与约束。

**机制与状态边界。** These benefits are enabled by specialized hardware components that add only 8% to the system area.

**证据证明什么。** Under iso-accuracy constraints, HiKV outperforms state-of-the-art importance-based methods by achieving an additional 1.82~4.87x reduction in external memory accesses.

**证据没有证明什么。** Built on the insight that KV cache redundancy exists at both token and element granularities, HiKV employs two orthogonally complementary compression stages, supported by the reconfigurable importance sorter as the core hardware innovation that accommodates the semantically distinct sorting requirements of both stages within a unified circuit, incurring only 8% area and power overhead in total. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.22389v1#S4.SS1 — IV-A System Architecture Overview; https://arxiv.org/html/2607.22389v1#S4 — IV HiKV Accelerator Architecture。Evaluation：https://arxiv.org/html/2607.22389v1#S5 — V Experimental Results; https://arxiv.org/html/2607.22389v1#S3.SS1 — III-A Importance Analysis of KV Cache。Limitations / counterevidence：https://arxiv.org/html/2607.22389v1#S6 — VI Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/meta-llama/llama3/blob/main/MODEL_CARD.md, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 动态资源控制提高利用率，但增加测量误差、迁移开销、租户公平和控制稳定性问题。 论文自身的边界信号是：Built on the insight that KV cache redundancy exists at both token and element granularities, HiKV employs two orthogonally complementary compression stages, supported by the reconfigurable importance sorter as the core hardware innovation that accommodates the semantically distinct sorting requirements of both stages within a unified circuit, incurring only 8% area and power overhead in total.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`INFER-KV-CACHE`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-22389:end -->

<!-- review:SF-2026-ARXIV-2607-22392:start -->
### The Prompt Is Not the Query: How Request State Evolves Across Multi-Turn AI Conversations

<!-- claim:SF-2026-ARXIV-2607-22392:start -->AI-search evaluation commonly treats a prompt as a stable query that can be counted, classified, and replayed in isolation. A conversation makes that unit of analysis questionable: each user turn can add a constraint, revise an assumption, request evidence, or refer to alternatives established earlier. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-22392:end -->

**为什么进入候选分母。** 摘要首要问题为“AI-search evaluation commonly treats a prompt as a stable query that can be counted, classified, and replayed in isolation.”；它把 context、memory、能力或进度变成持久且可验证的 agent state。

**机制与状态边界。** A conversation makes that unit of analysis questionable: each user turn can add a constraint, revise an assumption, request evidence, or refer to alternatives established earlier.

**证据证明什么。** Length-matched nulls show that low lexical coverage is largely a consequence of turn length, so vocabulary results are interpreted as information availability, not semantic drift.

**证据没有证明什么。** It is frequently another delta in an evolving request state. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.22392v1#S7.SS2 — 7.2 Implications for evaluation design; https://arxiv.org/html/2607.22392v1#S2.SS2 — 2.2 History use by language models。Evaluation：https://arxiv.org/html/2607.22392v1#S6 — 6 Results; https://arxiv.org/html/2607.22392v1#S7.SS2 — 7.2 Implications for evaluation design。Limitations / counterevidence：https://arxiv.org/html/2607.22392v1#S10 — 10 Conclusion; https://arxiv.org/html/2607.22392v1#S8 — 8 Limitations。

**Artifact boundary。** Exact v1 links https://dx.doi.org/10.18653/v1/2025.acl-demo.17, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 显式 agent state 改善恢复与控制，但增加状态陈旧、错误提交、跨轮污染和一致性责任。 论文自身的边界信号是：It is frequently another delta in an evolving request state.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`AGENT-CONTEXT`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-22392:end -->

<!-- review:SF-2026-ARXIV-2607-22393:start -->
### SceneActBench: Can Agents Act on the 3D Scenes They See?

<!-- claim:SF-2026-ARXIV-2607-22393:start -->Vision-language model (VLM) agents increasingly use tools to act on 3D scenes rather than only describe them. Existing 3D benchmarks score textual responses or single-object operations, leaving agent action on complete multi-object 3D scenes under evaluated. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-22393:end -->

**为什么进入候选分母。** 摘要首要问题为“Vision-language model (VLM) agents increasingly use tools to act on 3D scenes rather than only describe them.”；它改变 observable、对照组、判定粒度或外推边界，可能修正既有评测结论。

**机制与状态边界。** We present SceneActBench, a benchmark for visually conditioned action across five 3D tasks under a unified agent-environment loop.

**证据证明什么。** We further analyse where and how failures manifest.

**证据没有证明什么。** Comparisons with task-specialist 3D pipelines remain an important direction for future work. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.22393v1#S1 — 1 Introduction; https://arxiv.org/html/2607.22393v1#S2 — 2 Related Work。Evaluation：https://arxiv.org/html/2607.22393v1#A1 — Appendix A Benchmark Details; https://arxiv.org/html/2607.22393v1#A2 — Appendix B Evaluation Protocol。Limitations / counterevidence：https://arxiv.org/html/2607.22393v1#S5 — 5 Limitations; https://arxiv.org/html/2607.22393v1#S6 — 6 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/Feinaldo2/SceneActBench, https://feinaldo2.github.io/sceneactbench-project-page/, https://huggingface.co/datasets/FEInaldo/SceneActBench/tree/main; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：Comparisons with task-specialist 3D pipelines remain an important direction for future work.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`MULTIMODAL-EMBODIED-VLA`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-22393:end -->

<!-- review:SF-2026-ARXIV-2607-22400:start -->
### A Self-Calibrating Agentic AI Framework for Autonomous Edge Resource Allocation

<!-- claim:SF-2026-ARXIV-2607-22400:start -->Large Language Models (LLMs) are increasingly deployed as autonomous agents, transitioning from static conversational interfaces to dynamic systems capable of complex reasoning, tool execution, and decision-making. However, the operational reliability of these agentic AI systems is fundamentally challenged by the absence of reliable ground truth in open-ended environments and the risk of increasing operational drift over time. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-22400:end -->

**为什么进入候选分母。** 摘要首要问题为“Large Language Models (LLMs) are increasingly deployed as autonomous agents, transitioning from static conversational interfaces to dynamic systems capable of complex reasoning, tool execution, and decision-making.”；它改变资源计量、分配、路由或迁移的控制权与约束。

**机制与状态边界。** To address this challenge, we propose and experimentally evaluate an agentic AI framework, designed to enforce autonomous integrity within LLM-driven systems.

**证据证明什么。** Experimental results show that the proposed self-calibrating agentic framework successfully profiles the zero-knowledge workloads, achieving a higher accuracy than baseline LLM agents by 91.7% for resource usage prediction and improving the prediction speed by 71.7% compared to pure profiling, establishing a robust foundation for deploying autonomous AI in decentralized infrastructures.

**证据没有证明什么。** Another limitation we observed in the experiments is that the system was susceptible to ”cold start” scenarios. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.22400v1#S2.SS4 — II-D Edge Resource Orchestration and Multi-Agent Systems; https://arxiv.org/html/2607.22400v1#S3 — III Architecture。Evaluation：https://arxiv.org/html/2607.22400v1#S6 — VI Evaluation; https://arxiv.org/html/2607.22400v1#S6.SS1 — VI-A Experimental Setup。Limitations / counterevidence：https://arxiv.org/html/2607.22400v1#S6.SS6 — VI-F Discussion; https://arxiv.org/html/2607.22400v1#S7 — VII Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/MarlaGru/Edge_Device_AI_Hardware_monitore_Dataset, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 动态资源控制提高利用率，但增加测量误差、迁移开销、租户公平和控制稳定性问题。 论文自身的边界信号是：Another limitation we observed in the experiments is that the system was susceptible to ”cold start” scenarios.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`PLATFORM-GPU-SCHEDULER`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-22400:end -->

<!-- review:SF-2026-ARXIV-2607-22430:start -->
### On the Identifiability of Controlled World Models

<!-- claim:SF-2026-ARXIV-2607-22430:start -->World model serves as a promising tool to infer environment dynamics under high-dimensional observations and candidate actions. Recently, LeCun's JEPA provides a compelling framework for learning such models in representation space. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-22430:end -->

**为什么进入候选分母。** 摘要首要问题为“World model serves as a promising tool to infer environment dynamics under high-dimensional observations and candidate actions.”；它改变 observable、对照组、判定粒度或外推边界，可能修正既有评测结论。

**机制与状态边界。** Recently, LeCun's JEPA provides a compelling framework for learning such models in representation space.

**证据证明什么。** The theoretical predictions are empirically supported across four nonlinear observation settings.

**证据没有证明什么。** State-only prediction generally represents the behavior-policy-averaged future and therefore does not identify how alternative actions change the next state, even when its representation is identifiable. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.22430v1#S3 — 3 Method; https://arxiv.org/html/2607.22430v1#S3.SS2 — 3.2 Identifiability of Controlled World Models。Evaluation：https://arxiv.org/html/2607.22430v1#A4 — Appendix D Experimental Details; https://arxiv.org/html/2607.22430v1#S4 — 4 Experiments。Limitations / counterevidence：https://arxiv.org/html/2607.22430v1#S5 — 5 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：State-only prediction generally represents the behavior-policy-averaged future and therefore does not identify how alternative actions change the next state, even when its representation is identifiable.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`MULTIMODAL-WORLD-MODELS`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-22430:end -->

<!-- review:SF-2026-ARXIV-2607-22432:start -->
### TileSight: A First-Principles Tile-Centric Analytical GPU Performance Model from Cores to Clusters

<!-- claim:SF-2026-ARXIV-2607-22432:start -->Recent GPU programming frameworks such as Triton, TileLang, and CUDA Tile adopt tiles as first-class primitives, making tile-centric programming the prevailing approach for high-performance GPU kernels. Performance-analysis tooling has not followed: programmers still rely on coarse roofline bounds, opaque ML predictors, or post-hoc profilers to understand kernel execution. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-22432:end -->

**为什么进入候选分母。** 摘要首要问题为“Recent GPU programming frameworks such as Triton, TileLang, and CUDA Tile adopt tiles as first-class primitives, making tile-centric programming the prevailing approach for high-performance GPU kernels.”；它改变 observable、对照组、判定粒度或外推边界，可能修正既有评测结论。

**机制与状态边界。** We present TileSight, a tile-centric performance-modeling tool that elevates the tile from a programming primitive to an analysis primitive.

**证据证明什么。** At up to 32 GPUs, TileSight achieves 16.18% weighted MAPE (wMAPE) on fused distributed kernels and 13.52% wMAPE on end-to-end vLLM serving.

**证据没有证明什么。** Limitations and Future Work TileSight targets regular, tile-structured programs whose runtime is dominated by resource utilization. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.22432v1#S2.SS1 — 2.1. GPU Performance Modeling; https://arxiv.org/html/2607.22432v1#S2.SS2 — 2.2. Modeling Gap for Tile-Centric Programs。Evaluation：https://arxiv.org/html/2607.22432v1#S5 — 5. Evaluation; https://arxiv.org/html/2607.22432v1#S5.SS1 — 5.1. Experimental Setup。Limitations / counterevidence：https://arxiv.org/html/2607.22432v1#S7 — 7. Limitations and Future Work; https://arxiv.org/html/2607.22432v1#S8 — 8. Conclusion。

**Artifact boundary。** Exact v1 links https://rocm.docs.amd.com/projects/omniperf/en/docs-6.2.1/what-is-omniperf.html, https://github.com/tile-ai/tilelang, https://github.com/NVIDIA/cutlass; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：Limitations and Future Work TileSight targets regular, tile-structured programs whose runtime is dominated by resource utilization.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`INFER-TENSORRT-LLM`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-22432:end -->

<!-- review:SF-2026-ARXIV-2607-22445:start -->
### Dynamic Capability Scoping for Enterprise AI Agents: A Synthetic Dataset and Three-Source Permission Architecture

<!-- claim:SF-2026-ARXIV-2607-22445:start -->Enterprise AI agents are typically granted static credential sets at configuration time, holding every tool the role might need for every task they perform. This persistent over-privilege expands the attack surface. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-22445:end -->

**为什么进入候选分母。** 摘要首要问题为“Enterprise AI agents are typically granted static credential sets at configuration time, holding every tool the role might need for every task they perform.”；它改变执行安全的 trust boundary、guard 或 failure detection。

**机制与状态边界。** This persistent over-privilege expands the attack surface.

**证据证明什么。** Iterating between dataset and policy reduced ceiling violations from 46 to 3, a 93% reduction.

**证据没有证明什么。** Because Source 2 currently evaluates only the upfront request, it cannot anticipate downstream requirements discovered during the agent’s reasoning loop. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.22445v1#S3 — 3 Three-Source Architecture; https://arxiv.org/html/2607.22445v1#S3.SS4 — 3.4 Combined Application of the Three-Source Architecture。Evaluation：https://arxiv.org/html/2607.22445v1#S5 — 5 Validation Results。Limitations / counterevidence：https://arxiv.org/html/2607.22445v1#S6 — 6 Discussion and Limitations; https://arxiv.org/html/2607.22445v1#S7 — 7 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/0xballistics/mostargate, https://dx.doi.org/10.18653/v1/2023.emnlp-demo.40, https://aclanthology.org/2023.emnlp-demo.40; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 新的安全控制点降低特定失败，但会引入误拒绝、旁路、观测不足或模型/任务迁移问题。 论文自身的边界信号是：Because Source 2 currently evaluates only the upfront request, it cannot anticipate downstream requirements discovered during the agent’s reasoning loop.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`AGENT-PLATFORM`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-22445:end -->

<!-- review:SF-2026-ARXIV-2607-22448:start -->
### Where Facts Go Missing: A Layerwise Taxonomy and Per-Layer Attribution of Information Omission in Air-Gapped LLMAgent Pipelines

<!-- claim:SF-2026-ARXIV-2607-22448:start -->Air-gapped and on-premises language-model agents can silently omit decision-critical facts at any boundary between source ingestion and final answer generation. We present a nine-layer taxonomy (L0-L8), an instrumented attribution harness, and a conditional omission waterfall that distinguishes deterministic software loss from behavioral non-retrieval. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-22448:end -->

**为什么进入候选分母。** 摘要首要问题为“Air-gapped and on-premises language-model agents can silently omit decision-critical facts at any boundary between source ingestion and final answer generation.”；它把 evidence identity、lineage、conflict 或 commit 变成显式系统状态。

**机制与状态边界。** We present a nine-layer taxonomy (L0-L8), an instrumented attribution harness, and a conditional omission waterfall that distinguishes deterministic software loss from behavioral non-retrieval.

**证据证明什么。** These results establish pipeline-level attribution in a controlled stress test, but benchmark allocations, confounded model comparisons, and heuristic behavioral labels do not measure production prevalence or causal architectural effects.

**证据没有证明什么。** Future Work The completed sweep establishes the taxonomy and the deterministic-layer attribution, but several axes remain open for investigation. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.22448v1#Sx4 — Attribution Methodology; https://arxiv.org/html/2607.22448v1#Sx5.SS0.SSS0.Px2 — Engines, profiles, and frameworks.。Evaluation：https://arxiv.org/html/2607.22448v1#Sx4.SS0.SSS0.Px7 — Analysis.; https://arxiv.org/html/2607.22448v1#Sx5 — Experimental Setup。Limitations / counterevidence：https://arxiv.org/html/2607.22448v1#Sx6.SS0.SSS0.Px4 — Failure ledger (Table 8 ).; https://arxiv.org/html/2607.22448v1#Sx7 — Future Work。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 显式 evidence state 提高可追溯性，但新增 lineage、冲突、commit 与恢复语义，状态本身也必须被验证。 论文自身的边界信号是：Future Work The completed sweep establishes the taxonomy and the deterministic-layer attribution, but several axes remain open for investigation.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`AGENT-MULTI-AGENT`；evidence-stage relation：`corrective_evidence`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-22448:end -->

<!-- review:SF-2026-ARXIV-2607-22465:start -->
### TRACE-ROUTER: Task-Consistent and Adaptive Online Routing for Agentic AI

<!-- claim:SF-2026-ARXIV-2607-22465:start -->Routing to select large language models (LLMs) with different cost-quality trade-offs has become a fundamental deployment feature of enterprise AI. Existing routers, primarily make independent routing decisions for each LLM call. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-22465:end -->

**为什么进入候选分母。** 摘要首要问题为“Routing to select large language models (LLMs) with different cost-quality trade-offs has become a fundamental deployment feature of enterprise AI.”；它改变资源计量、分配、路由或迁移的控制权与约束。

**机制与状态边界。** Towards mitigating this, we present TRACE-Router, a task-level routing framework that aligns routing with the unit of supervision.

**证据证明什么。** On tau2-Bench, it outperforms latency-matched interpolation between individual models by 7-8 accuracy points, while on Terminal-Bench it achieves 7.1 higher accuracy points than the strongest single model baseline with 36% lower latency.

**证据没有证明什么。** Without a principled mechanism for credit assignment, the router cannot effectively learn from task-level feedback. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.22465v1#S3 — 3 Methodology; https://arxiv.org/html/2607.22465v1#S3.SS2 — 3.2 Context-Conditioned Model Selection。Evaluation：https://arxiv.org/html/2607.22465v1#S4 — 4 Evaluation。Limitations / counterevidence：https://arxiv.org/html/2607.22465v1#S1 — 1 Introduction; https://arxiv.org/html/2607.22465v1#S2 — 2 Related Work。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 动态资源控制提高利用率，但增加测量误差、迁移开销、租户公平和控制稳定性问题。 论文自身的边界信号是：Without a principled mechanism for credit assignment, the router cannot effectively learn from task-level feedback.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`INFER-SCHEDULING`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-22465:end -->

<!-- review:SF-2026-ARXIV-2607-22489:start -->
### \k{appa}-LoRA: Condition Numbers Reveal Which LoRA Matrices Worth Updating

<!-- claim:SF-2026-ARXIV-2607-22489:start -->Low-Rank Adaptation (LoRA) has become a widely adopted technique for efficient neural network fine-tuning, decomposing model updates into low-rank matrices. However, LoRA remains computationally costly because it updates all matrices uniformly, regardless of their actual contribution to adaptation. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-22489:end -->

**为什么进入候选分母。** 摘要首要问题为“Low-Rank Adaptation (LoRA) has become a widely adopted technique for efficient neural network fine-tuning, decomposing model updates into low-rank matrices.”；它改变训练信号、capacity 或 update ownership，而非只报告任务精度。

**机制与状态边界。** Building on this insight, we propose \k{appa}-LoRA, a method that optimizes LoRA by focusing updates on the matrices with the largest condition numbers, which capture the most informative directions of change.

**证据证明什么。** Extensive experiments across multiple benchmarks show that this design cuts fine-tuning time by 16.2% on average while matching the accuracy of standard LoRA and reducing memory cost by 4.5%.

**证据没有证明什么。** Limitations Our study has several limitations that open directions for future work. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.22489v1#S3 — 3 Methodology; https://arxiv.org/html/2607.22489v1#S3.SS2 — 3.2 Method。Evaluation：https://arxiv.org/html/2607.22489v1#A3 — Appendix C Additional experiments; https://arxiv.org/html/2607.22489v1#S4 — 4 Experiments。Limitations / counterevidence：https://arxiv.org/html/2607.22489v1#S5 — 5 Discussion。

**Artifact boundary。** Exact v1 links https://github.com/tatsu-lab/stanford_alpaca, https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更密集或更定向的训练信号改善样本效率，但会增加 verifier 偏差、分布迁移和优化耦合。 论文自身的边界信号是：Limitations Our study has several limitations that open directions for future work.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`TRAIN-LORA`；evidence-stage relation：`corrective_evidence`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-22489:end -->

<!-- review:SF-2026-ARXIV-2607-22511:start -->
### CausalSmith: A Formally Grounded, Self-Improving Agentic Framework for Automated Research in Causal Inference

<!-- claim:SF-2026-ARXIV-2607-22511:start -->Automating theoretical research is constrained not only by the generation of candidate results, but also by their reliable evaluation. A common approach is to close the research loop with a large language model (LLM) reviewer. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-22511:end -->

**为什么进入候选分母。** 摘要首要问题为“Automating theoretical research is constrained not only by the generation of candidate results, but also by their reliable evaluation.”；它把 context、memory、能力或进度变成持久且可验证的 agent state。

**机制与状态边界。** We present CausalSmith, a framework for automated theoretical research in causal inference grounded in the Lean proof assistant.

**证据证明什么。** Automating theoretical research is constrained not only by the generation of candidate results, but also by their reliable evaluation.

**证据没有证明什么。** We regard constructing such a benchmark, and convening an independent panel, as future work. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.22511v1#S4.SS1 — 4.1 Design and scope; https://arxiv.org/html/2607.22511v1#S6.SS2 — 6.2 Which self-proposed questions the system converts。Evaluation：https://arxiv.org/html/2607.22511v1#S4.SS3 — 4.3 Flagship results; https://arxiv.org/html/2607.22511v1#S6 — 6 Results。Limitations / counterevidence：https://arxiv.org/html/2607.22511v1#S7 — 7 Discussion and Limitations; https://arxiv.org/html/2607.22511v1#S8 — 8 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/Jiyuan-Tan/CausalForge, https://github.com/optsuite/optlib, https://github.com/auto-res/lean-rademacher; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 显式 agent state 改善恢复与控制，但增加状态陈旧、错误提交、跨轮污染和一致性责任。 论文自身的边界信号是：We regard constructing such a benchmark, and convening an independent panel, as future work.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`AGENT-REFLECTION`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-22511:end -->

<!-- review:SF-2026-ARXIV-2607-22520:start -->
### The Regression Tax: Decomposing Why Skills Help and Hurt LLM Agents

<!-- claim:SF-2026-ARXIV-2607-22520:start -->Adding procedural skills to an LLM agent is typically evaluated by average improvement in task success. However, this metric hides an important cost: skills can also make agents worse. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-22520:end -->

**为什么进入候选分母。** 摘要首要问题为“Adding procedural skills to an LLM agent is typically evaluated by average improvement in task success.”；它改变 observable、对照组、判定粒度或外推边界，可能修正既有评测结论。

**机制与状态边界。** However, this metric hides an important cost: skills can also make agents worse.

**证据证明什么。** We find that regressions are substantial enough that the best performing skills outperform others primarily by regressing less, not by gaining more.

**证据没有证明什么。** There the missing content is a check, not a procedure. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.22520v1#A2 — Appendix B Worked Cases: Correct Method, Wrong Grounding or Verification; https://arxiv.org/html/2607.22520v1#S6.SS1 — 6.1. Designing and Measuring Skill Libraries。Evaluation：https://arxiv.org/html/2607.22520v1#S3 — 3. Experimental Setup; https://arxiv.org/html/2607.22520v1#S3.SS1 — 3.1. Benchmarks and Tasks。Limitations / counterevidence：https://arxiv.org/html/2607.22520v1#S5.SS4 — 5.4. Residual Failures; https://arxiv.org/html/2607.22520v1#S6 — 6. Discussion。

**Artifact boundary。** Exact v1 links https://github.com/sentient-agi/meta-skill-creator, https://github.com/anthropics/skills/tree/main/skills/skill-creator, https://github.com/openai/skills/tree/main/skills/.system/skill-creator; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更强的评测可解释性需要额外对照、重复试验、ground-truth 或 evaluator 校准，成本不能由单一准确率隐藏。 论文自身的边界信号是：There the missing content is a check, not a procedure.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`AGENT-PLATFORM`；evidence-stage relation：`corrective_evidence`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-22520:end -->

<!-- review:SF-2026-ARXIV-2607-22529:start -->
### Skill Self-Play: Pushing the Frontier of LLM Capability with Co-Evolving Skills

<!-- claim:SF-2026-ARXIV-2607-22529:start -->LLM training is shifting from manual design and annotation to interaction-driven self-evolution. However, existing self-evolutionary methods face a fundamental dilemma between task diversity and verification reliability: environment-bound methods obtain precise feedback but confine learning to narrow domains, while open-ended self-generation broadens the task space but lacks reliable verification, allowing misleading rewards to pollute the training loop. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-22529:end -->

**为什么进入候选分母。** 摘要首要问题为“LLM training is shifting from manual design and annotation to interaction-driven self-evolution.”；它改变训练信号、capacity 或 update ownership，而非只报告任务精度。

**机制与状态边界。** Leveraging this insight, we introduce Skill Self-Play (Skill-SP), a co-evolutionary framework comprising a proposer, a solver, and a dynamic skill controller.

**证据证明什么。** Empirical evaluations on tool-use and reasoning benchmarks demonstrate that Skill-SP, serving as a robust evolution engine, consistently pushes the performance ceiling of competent backbones while catalyzing striking turnarounds for initially misaligned models.

**证据没有证明什么。** Building on these observations, future work will explore several promising directions. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.22529v1#S3 — 3 Methodology; https://arxiv.org/html/2607.22529v1#A3 — Appendix C Training and Implementation Details。Evaluation：https://arxiv.org/html/2607.22529v1#A7 — Appendix G Analysis of Evaluation Benchmark; https://arxiv.org/html/2607.22529v1#A1 — Appendix A Iteration-wise Evaluation Trajectories。Limitations / counterevidence：https://arxiv.org/html/2607.22529v1#A8 — Appendix H Limitations and Future Work; https://arxiv.org/html/2607.22529v1#S5 — 5 Conclusion。

**Artifact boundary。** Exact v1 links https://github.com/Qwen-Applications/skill-self-play, https://huggingface.co/blog/ibm-granite/granit-4-1, https://github.com/arXiv/html_feedback/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 更密集或更定向的训练信号改善样本效率，但会增加 verifier 偏差、分布迁移和优化耦合。 论文自身的边界信号是：Building on these observations, future work will explore several promising directions.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`AGENT-REFLECTION`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-22529:end -->

<!-- review:SF-2026-ARXIV-2607-22530:start -->
### ViTacWorld: Scaling Visuo-Tactile World Models for Contact-Rich Robot Manipulation

<!-- claim:SF-2026-ARXIV-2607-22530:start -->Contact-rich robot manipulation requires physical interaction cues that are often invisible to cameras, making tactile sensing essential for robust control. However, scaling visuo-tactile robot learning remains difficult because real tactile interaction data are expensive to collect, hardware-dependent, and limited in task and scene diversity. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-22530:end -->

**为什么进入候选分母。** 摘要首要问题为“Contact-rich robot manipulation requires physical interaction cues that are often invisible to cameras, making tactile sensing essential for robust control.”；它提出可跨 workload 讨论的表示、状态或计算机制，并暴露旧方案边界。

**机制与状态边界。** We present ViTacWorld, an action-conditioned visuo-tactile world model for scalable contact-rich robot manipulation.

**证据证明什么。** Experiments on contact-rich manipulation tasks show that ViTacWorld generates physically meaningful rollouts, improves policy performance through scalable data augmentation, and enables action-conditioned policy evaluation.

**证据没有证明什么。** Future work will explore automated filtering with vision-language models or multimodal evaluators to further improve the scalability of generated data curation. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.22530v1#A3 — Appendix C Implementation, Data, and Training Details; https://arxiv.org/html/2607.22530v1#A3.SS2 — C.2 World Model and Policy Training Details。Evaluation：https://arxiv.org/html/2607.22530v1#A1 — Appendix A Additional Evaluation and Improvement Results; https://arxiv.org/html/2607.22530v1#S3.SS4 — 3.4 Visuo-Tactile Policy Improvement and Evaluation。Limitations / counterevidence：https://arxiv.org/html/2607.22530v1#S5 — 5 Conclusion; https://arxiv.org/html/2607.22530v1#S6 — 6 Limitations。

**Artifact boundary。** Exact v1 links https://github.com/arXiv/html_feedback/issues, https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML, https://github.com/brucemiller/LaTeXML/issues; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 新表示或状态机制扩大能力边界，但带来额外训练、状态管理、稳定性或泛化假设。 论文自身的边界信号是：Future work will explore automated filtering with vision-language models or multimodal evaluators to further improve the scalability of generated data curation.

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Stable owner 候选：`MULTIMODAL-WORLD-MODELS`；evidence-stage relation：`direct_evolution`。
- Books 候选路由（尚非最终决定）：`Integrate`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-22530:end -->

<!-- review:SF-2026-ARXIV-2607-22535:start -->
### Robot-Factored World Models via Robot Rendering

<!-- claim:SF-2026-ARXIV-2607-22535:start -->Action-conditioned video world models predict future observations from an initial observation and an action signal. In robotics, actions influence future observations through two distinct processes: they are first realized into robot motion by the robot body and controller, and the scene then responds through contact and object motion. 本报告只把这一结论绑定到 arXiv v1 已公开的方法、实验与限制；不把作者结果外推为跨 workload、模型、硬件或生产 SLO 的通用事实。<!-- claim:SF-2026-ARXIV-2607-22535:end -->

**为什么进入候选分母。** 摘要首要问题为“Action-conditioned video world models predict future observations from an initial observation and an action signal.”；它提出可跨 workload 讨论的表示、状态或计算机制，并暴露旧方案边界。

**机制与状态边界。** We propose robot-factored world models, which move two robot-specific factors outside the world model.

**证据证明什么。** Our experiments show that the rendered interface outperforms vector-conditioned baselines and generalizes to unseen robot embodiments at inference.

**证据没有证明什么。** While our rendering-based action interface improves action following and generalization, several limitations remain. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Evaluation contract。** Method / identity：https://arxiv.org/html/2607.22535v1#S3 — 3 Method; https://arxiv.org/html/2607.22535v1#A2 — Appendix B Model, Baseline, and Evaluation Details。Evaluation：https://arxiv.org/html/2607.22535v1#A2 — Appendix B Model, Baseline, and Evaluation Details; https://arxiv.org/html/2607.22535v1#A5 — Appendix E Additional Qualitative Results。Limitations / counterevidence：https://arxiv.org/html/2607.22535v1#S5 — 5 Conclusion and Limitations。

**Artifact boundary。** Exact v1 links https://github.com/aigc-apps/VideoX-Fun, https://github.com/ModelTC/lightx2v, https://github.com/robocasa/robocasa-gr1-tabletop-tasks; no event-time commit was independently pinned, so the manuscript remains the claim authority.

**Trade-off 与共存边界。** 新表示或状态机制扩大能力边界，但带来额外训练、状态管理、稳定性或泛化假设。 论文自身的边界信号是：While our rendering-based action interface improves action following and generalization, several limitations remain.

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Stable owner 候选：`MULTIMODAL-WORLD-MODELS`；evidence-stage relation：`alternative_branch`。
- Books 候选路由（尚非最终决定）：`No Change — Existing Coverage`；等待 root 按日期串行完成目标章、相邻章与现有命题比较。
<!-- review:SF-2026-ARXIV-2607-22535:end -->

## 4. Benchmark Contracts

None。数值只在各 Source Review 的 exact-v1 evaluation contract 内使用，不形成跨配置 benchmark claim。

## 5. Deep Analysis Selection

<!-- validator:deep-analysis-selection-v1 -->
| Source Family ID | Eligibility | Decision | Analysis Unit ID | Subsumed By | Priority Rationale | Narrative Ref |
| --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2607-21596 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-21596 |
| SF-2026-ARXIV-2607-21599 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-21599 |
| SF-2026-ARXIV-2607-21600 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-21600 |
| SF-2026-ARXIV-2607-21602 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-21602 |
| SF-2026-ARXIV-2607-21604 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-21604 |
| SF-2026-ARXIV-2607-21606 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-21606 |
| SF-2026-ARXIV-2607-21609 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-21609 |
| SF-2026-ARXIV-2607-21612 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-21612 |
| SF-2026-ARXIV-2607-21623 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-21623 |
| SF-2026-ARXIV-2607-21624 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-21624 |
| SF-2026-ARXIV-2607-21642 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-21642 |
| SF-2026-ARXIV-2607-21653 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-21653 |
| SF-2026-ARXIV-2607-21686 | score_7_9 | selected | DA-20260727-02 | — | V2=9/9；相对其他 eligible family 提供更直接、可迁移且不重复的 state/control/evaluation 机制。 | analysis:DA-20260727-02 |
| SF-2026-ARXIV-2607-21731 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-21731 |
| SF-2026-ARXIV-2607-21752 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-21752 |
| SF-2026-ARXIV-2607-21804 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-21804 |
| SF-2026-ARXIV-2607-21824 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-21824 |
| SF-2026-ARXIV-2607-21835 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-21835 |
| SF-2026-ARXIV-2607-21909 | score_7_9 | selected | DA-20260727-01 | — | V2=9/9；相对其他 eligible family 提供更直接、可迁移且不重复的 state/control/evaluation 机制。 | analysis:DA-20260727-01 |
| SF-2026-ARXIV-2607-21927 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-21927 |
| SF-2026-ARXIV-2607-21962 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-21962 |
| SF-2026-ARXIV-2607-21985 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-21985 |
| SF-2026-ARXIV-2607-22002 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-22002 |
| SF-2026-ARXIV-2607-22022 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-22022 |
| SF-2026-ARXIV-2607-22038 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-22038 |
| SF-2026-ARXIV-2607-22043 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-22043 |
| SF-2026-ARXIV-2607-22186 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-22186 |
| SF-2026-ARXIV-2607-22242 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-22242 |
| SF-2026-ARXIV-2607-22389 | score_7_9 | selected | DA-20260727-03 | — | V2=9/9；相对其他 eligible family 提供更直接、可迁移且不重复的 state/control/evaluation 机制。 | analysis:DA-20260727-03 |
| SF-2026-ARXIV-2607-22400 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-22400 |
| SF-2026-ARXIV-2607-22432 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-22432 |
| SF-2026-ARXIV-2607-22465 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-22465 |
| SF-2026-ARXIV-2607-22530 | score_7_9 | not_selected | — | — | V2=9/9；完整 Review 保留，但系统影响更局部或主要承担反证边界。 | analysis-decision:SF-2026-ARXIV-2607-22530 |

### Selection Decisions

<!-- analysis-decision:SF-2026-ARXIV-2607-21596:start -->
`SF-2026-ARXIV-2607-21596` 的 exact-v1 Deep Review 已保留。其机制为：We introduce FlowEvo, a training-free framework in which workflows and skills co-evolve at inference time. 为避免挤压 `AGENT-WORKFLOW` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-21596:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-21599:start -->
`SF-2026-ARXIV-2607-21599` 的 exact-v1 Deep Review 已保留。其机制为：To address these challenges, we propose Decoupled Attention Fusion (DAF), a framework that maintains high accuracy while significantly reducing recomputation overhead. 为避免挤压 `INFER-KV-CACHE` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-21599:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-21600:start -->
`SF-2026-ARXIV-2607-21600` 的 exact-v1 Deep Review 已保留。其机制为：We propose FlowGuard, a lightweight inference-time framework that detects harmful inputs by monitoring internal multimodal consistency. 为避免挤压 `PLATFORM-SECURITY` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-21600:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-21602:start -->
`SF-2026-ARXIV-2607-21602` 的 exact-v1 Deep Review 已保留。其机制为：This paper presents a runtime-aware latency prediction framework for deployment-oriented LLM selection. 为避免挤压 `INFER-SCHEDULING` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-21602:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-21604:start -->
`SF-2026-ARXIV-2607-21604` 的 exact-v1 Deep Review 已保留。其机制为：We present AgentKVShift, a training-free, probe-guided KV residual correction method that operates per retrieved memory unit. 为避免挤压 `AGENT-MEMORY` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-21604:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-21606:start -->
`SF-2026-ARXIV-2607-21606` 的 exact-v1 Deep Review 已保留。其机制为：We present TILT, a training-free framework for compositional text-to-image generation via test-time reward alignment. 为避免挤压 `MULTIMODAL-GENERATIVE-PARADIGMS` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-21606:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-21609:start -->
`SF-2026-ARXIV-2607-21609` 的 exact-v1 Deep Review 已保留。其机制为：Building on this foundation, we introduce HierFlow, a training-free, test-time hierarchical search architecture that automates agentic workflow design by merging feedback-guided topology adjustments with a fast, MCTS-inspired tree search for sub-workflow optimization. 为避免挤压 `AGENT-WORKFLOW` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-21609:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-21612:start -->
`SF-2026-ARXIV-2607-21612` 的 exact-v1 Deep Review 已保留。其机制为：In a systematic ablation (r = 16--128) on a procedural travel booking task (14 nodes), all LoRA configurations fail uniformly (task success &lt;= 2.54 vs. 为避免挤压 `TRAIN-LORA` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-21612:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-21623:start -->
`SF-2026-ARXIV-2607-21623` 的 exact-v1 Deep Review 已保留。其机制为：We present EaaS, a cloud-native reference architecture that operationalizes AI evaluation methods as six stateless Kubernetes microservices: conformal prediction with finite-sample-corrected Adaptive Prediction Sets, calibration assessment, drift detection via RFF-approximated Maximum Mean Discrepancy, fairness monitoring with bootstrap confidence intervals, a DAG-based pipeline orchestrator, and a result storage API. 为避免挤压 `PLATFORM-EVALUATION-SYSTEM` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-21623:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-21624:start -->
`SF-2026-ARXIV-2607-21624` 的 exact-v1 Deep Review 已保留。其机制为：To overcome this, we propose FBLayout, a layout-aware framework that co-designs tensor organization with mobile GPU platforms. 为避免挤压 `TRAIN-LORA` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-21624:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-21642:start -->
`SF-2026-ARXIV-2607-21642` 的 exact-v1 Deep Review 已保留。其机制为：We present CARE (Canonicalization, Attribution, and Resolution Engine), a shell-specific, static-first verifier for individual shell commands before execution. 为避免挤压 `AGENT-TOOL-CALLING` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-21642:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-21653:start -->
`SF-2026-ARXIV-2607-21653` 的 exact-v1 Deep Review 已保留。其机制为：Molt is a PyTorch-native training framework built to keep that cost small: a codebase compact and clean enough for a researcher to hold in their head, and for an AI coding assistant to read and reason about in its entirety, so the algorithm flow can be traced and changed end to end. 为避免挤压 `TRAIN-GRPO` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-21653:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-21731:start -->
`SF-2026-ARXIV-2607-21731` 的 exact-v1 Deep Review 已保留。其机制为：In this work, we propose RED-PIM, an algorithm-architecture co-design that reduces attention latency by minimizing inter-bank data movement from O(N^2) to O(N) and shrinking intermediate attention matrices from N x N to d x d. 为避免挤压 `INFER-TENSORRT-LLM` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-21731:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-21752:start -->
`SF-2026-ARXIV-2607-21752` 的 exact-v1 Deep Review 已保留。其机制为：On PG-19 byte-level language modeling at 92M parameters with 8K context, our method achieves 1.71 bits-per-byte (BPB), outperforming dense attention (2.89), BigBird (2.34), Longformer (3.21), and a reimplemented SBM-Transformer (3.38)---the only learned-mask baseline---by up to 1.67 BPB while adding no parameters. 为避免挤压 `MODEL-LONG-CONTEXT` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-21752:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-21804:start -->
`SF-2026-ARXIV-2607-21804` 的 exact-v1 Deep Review 已保留。其机制为：However, this guarantee of semantic equivalence masks a severe operational vulnerability: draft-target alignment can be systematically attacked. 为避免挤压 `INFER-SPECULATIVE-DECODING` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-21804:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-21824:start -->
`SF-2026-ARXIV-2607-21824` 的 exact-v1 Deep Review 已保留。其机制为：The same failure modes recur across independently built codebases, a systemic pattern rather than isolated bugs. 为避免挤压 `AGENT-PLATFORM` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-21824:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-21835:start -->
`SF-2026-ARXIV-2607-21835` 的 exact-v1 Deep Review 已保留。其机制为：This paper presents ToolGuardian, a policy-driven framework for securing agent-tool interactions through pre-admission vetting and task-aware runtime authorization. 为避免挤压 `AGENT-TOOL-CALLING` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-21835:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-21927:start -->
`SF-2026-ARXIV-2607-21927` 的 exact-v1 Deep Review 已保留。其机制为：The Reduced Interaction Sampling (RIS) inference engine addresses this constraint as a model-agnostic architecture. 为避免挤压 `MODEL-LONG-CONTEXT` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-21927:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-21962:start -->
`SF-2026-ARXIV-2607-21962` 的 exact-v1 Deep Review 已保留。其机制为：A full-rendered-history baseline ties or exceeds the best memory system at the short horizon but shows no judge-independent advantage at nine weeks, at about twice the read cost. 为避免挤压 `AGENT-MEMORY` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-21962:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-21985:start -->
`SF-2026-ARXIV-2607-21985` 的 exact-v1 Deep Review 已保留。其机制为：This paper presents SPDP, a unified sparse-inference framework that integrates unstructured SP with input-adaptive DP for efficient LLM inference on GPUs. 为避免挤压 `INFER-DECODE` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-21985:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-22002:start -->
`SF-2026-ARXIV-2607-22002` 的 exact-v1 Deep Review 已保留。其机制为：Reinforcement learning with verifiable rewards (RLVR) has emerged as a highly effective framework for improving LLM reasoning, with methods such as GRPO among its most successful instantiations. 为避免挤压 `TRAIN-GRPO` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-22002:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-22022:start -->
`SF-2026-ARXIV-2607-22022` 的 exact-v1 Deep Review 已保留。其机制为：However, SSD introduces substantial system-level overheads, including quadratic intermediate materialization, irregular data movement, and prefix-dependent execution, leading to excessive memory traffic and bandwidth demand on conventional architectures. 为避免挤压 `INFER-TENSORRT-LLM` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-22022:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-22038:start -->
`SF-2026-ARXIV-2607-22038` 的 exact-v1 Deep Review 已保留。其机制为：We present a HW/SW co-designed approach in which a lightweight gating network, trained jointly with the backbone, predicts per-tile binary execution masks conditioned on the task input. 为避免挤压 `INFER-TENSORRT-LLM` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-22038:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-22043:start -->
`SF-2026-ARXIV-2607-22043` 的 exact-v1 Deep Review 已保留。其机制为：Despite these advantages, the scaling properties of this paradigm remain systematically uncharacterized. 为避免挤压 `MULTIMODAL-REPRESENTATION` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-22043:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-22186:start -->
`SF-2026-ARXIV-2607-22186` 的 exact-v1 Deep Review 已保留。其机制为：In this work, we reveal that the natural scale of the importance ratio varies systematically with token entropy. 为避免挤压 `TRAIN-GRPO` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-22186:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-22242:start -->
`SF-2026-ARXIV-2607-22242` 的 exact-v1 Deep Review 已保留。其机制为：Agentic AI systems compose heterogeneous tool workloads on shared GPU/CPU infrastructure, yet existing frameworks assign all GPU-capable tools to the GPU by default. 为避免挤压 `PLATFORM-GPU-SCHEDULER` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-22242:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-22400:start -->
`SF-2026-ARXIV-2607-22400` 的 exact-v1 Deep Review 已保留。其机制为：To address this challenge, we propose and experimentally evaluate an agentic AI framework, designed to enforce autonomous integrity within LLM-driven systems. 为避免挤压 `PLATFORM-GPU-SCHEDULER` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-22400:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-22432:start -->
`SF-2026-ARXIV-2607-22432` 的 exact-v1 Deep Review 已保留。其机制为：We present TileSight, a tile-centric performance-modeling tool that elevates the tile from a programming primitive to an analysis primitive. 为避免挤压 `INFER-TENSORRT-LLM` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-22432:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-22465:start -->
`SF-2026-ARXIV-2607-22465` 的 exact-v1 Deep Review 已保留。其机制为：Towards mitigating this, we present TRACE-Router, a task-level routing framework that aligns routing with the unit of supervision. 为避免挤压 `INFER-SCHEDULING` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-22465:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-22530:start -->
`SF-2026-ARXIV-2607-22530` 的 exact-v1 Deep Review 已保留。其机制为：We present ViTacWorld, an action-conditioned visuo-tactile world model for scalable contact-rich robot manipulation. 为避免挤压 `MULTIMODAL-WORLD-MODELS` owner，本日报不将它合并进三条主叙事。
<!-- analysis-decision:SF-2026-ARXIV-2607-22530:end -->

### Selected Analysis Narratives

<!-- analysis:DA-20260727-01:start -->
### Claim Plane: Enforceable Change Intents and Dynamic Scope for Parallel Coding Agents

**约束变化与机制。** Existing responses emphasize communication, isolated workspaces, late merge-time repair, continuous supervision, or post-hoc runtime recovery.

**证明与未证明。** A preliminary six-pair CooperBench mechanism check is reported only as feasibility evidence: static Claim Plane achieved 6/6 pair passes with full serialization, while dynamic scope retained parallel admission on half of the pairs, performed seven successful scope promotions, and failed closed on two undeclared mutations. 但 We argue that separating probabilistic planning from deterministic authority provides a foundation for a future learned semantic-dependency model and frontier-model escalation only on unresolved cases. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Trade-off 与共存边界。** 显式 agent state 改善恢复与控制，但增加状态陈旧、错误提交、跨轮污染和一致性责任。 论文自身的边界信号是：We argue that separating probabilistic planning from deterministic authority provides a foundation for a future learned semantic-dependency model and frontier-model escalation only on unresolved cases. 旧方案在不承受该约束时仍成立。

关联：`review:SF-2026-ARXIV-2607-21909`。
<!-- analysis:DA-20260727-01:end -->

<!-- analysis:DA-20260727-02:start -->
### Persistent Computational State: A Session-Centric Runtime for Generative World Models

**约束变化与机制。** Recent benchmarks establish that current video world models fail this usage, and attribute it to the model, prescribing new architectures and training objectives.

**证明与未证明。** We show this attribution is incomplete, and for an important class of models simply wrong. 但 The addressability the substrate exposes is read-only, not write-repositionable without rewriting the cache manager. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Trade-off 与共存边界。** 显式 agent state 改善恢复与控制，但增加状态陈旧、错误提交、跨轮污染和一致性责任。 论文自身的边界信号是：The addressability the substrate exposes is read-only, not write-repositionable without rewriting the cache manager. 旧方案在不承受该约束时仍成立。

关联：`review:SF-2026-ARXIV-2607-21686`。
<!-- analysis:DA-20260727-02:end -->

<!-- analysis:DA-20260727-03:start -->
### HiKV: Hierarchical Importance-Aware KV Cache with Hardware Acceleration for LLM Decoding

**约束变化与机制。** These benefits are enabled by specialized hardware components that add only 8% to the system area.

**证明与未证明。** Under iso-accuracy constraints, HiKV outperforms state-of-the-art importance-based methods by achieving an additional 1.82~4.87x reduction in external memory accesses. 但 Built on the insight that KV cache redundancy exists at both token and element granularities, HiKV employs two orthogonally complementary compression stages, supported by the reconfigurable importance sorter as the core hardware innovation that accommodates the semantically distinct sorting requirements of both stages within a unified circuit, incurring only 8% area and power overhead in total. 因此本审阅只接受 exact v1 在其测试模型、数据、硬件、长度、并发与 evaluator 披露范围内的结论；未披露条件记为 Not Disclosed，不能外推为通用生产结论。

**Trade-off 与共存边界。** 动态资源控制提高利用率，但增加测量误差、迁移开销、租户公平和控制稳定性问题。 论文自身的边界信号是：Built on the insight that KV cache redundancy exists at both token and element granularities, HiKV employs two orthogonally complementary compression stages, supported by the reconfigurable importance sorter as the core hardware innovation that accommodates the semantically distinct sorting requirements of both stages within a unified circuit, incurring only 8% area and power overhead in total. 旧方案在不承受该约束时仍成立。

关联：`review:SF-2026-ARXIV-2607-22389`。
<!-- analysis:DA-20260727-03:end -->

## 6. Books Comparison

<!-- validator:books-comparison-v1 -->
| Source Family ID | Stable Node ID | Target Chapter Ref | Adjacent Chapter Refs | Existing Proposition | New Evidence Delta | Evolution Relation | Decision | Books Review Ref |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |

None。建议路由已冻结到 date-local queue；最终 disposition 等待 root 按日期串行对读 Books。

## 7. Semantic Audit

<!-- validator:semantic-audit-v1 -->
| Audit ID | Auditor | Scope | Reviewed Refs | Findings | Resolution | Status |
| --- | --- | --- | --- | --- | --- | --- |
| SA-20260727-COVERAGE-INDEPENDENT | fresh-context:pending-root-auditor | coverage | coverage:SRC-ARXIV:20260727 | GAP-20260727-COVERAGE-INDEPENDENT：全量筛选尚未被独立反向审计 | Pending — 逐项核验 false positive / false negative | open |
| SA-20260727-EVIDENCE-INDEPENDENT | fresh-context:pending-root-auditor | evidence | validator:review-completion-v1 | GAP-20260727-EVIDENCE-INDEPENDENT：RP 尚需独立对照 exact v1 | Pending — finding 绑定具体 family | open |
| SA-20260727-SELECTION-INDEPENDENT | fresh-context:pending-root-auditor | deep_analysis_selection | validator:deep-analysis-selection-v1 | GAP-20260727-SELECTION-INDEPENDENT：三项选择尚需 adversarial comparison | Pending — 比较 impact、反证与 owner 独立性 | open |
| SA-20260727-BOOKS-ROOT | fresh-context:pending-root-books-owner | books | validator:books-comparison-v1 | GAP-20260727-BOOKS-ROOT：尚未逐项对读 Books | Pending — root 消费 frozen queue | open |

## 8. Ignored Noise

283 项均有 family-specific pre-denominator closure：

- `embodied_task_local_method`：22
- `incremental_method_without_durable_system_delta`：200
- `local_benchmark_without_release_delta`：13
- `prior_retained_candidate`：1
- `theory_without_ai_system_contract`：6
- `vertical_application_without_system_delta`：41

## 9. Recommended Action

1. 独立审计 Coverage、Evidence 与 Selection；finding 只重开具体 family。
2. root 逐项比较 Books。建议起点：Integrate 31、No Change 68、Structural 1；不是最终决定。

## 10. Repository Changes

- 重建 `papers/2026/07/27/README.md` 及 date-local frozen queue。
- 未修改 Books、ROADMAP、docs、Learning State、Weekly。

## 11. Open Questions

- 独立审计是否恢复 closure 中的漏项？
- proposed Integrate 是否已被现有 Books 命题覆盖？

## 12. Sources

- [FlowEvo: Self-Evolving Agents through the Co-Evolution of Workflows and Executable Skills](https://arxiv.org/html/2607.21596v1) — first-public（Asia/Shanghai）：2026-07-27；exact evidence：v1；accessed：2026-09-04
- [Decoupled Attention Fusion: Accelerating RAG with Efficient KV Cache Reuse](https://arxiv.org/html/2607.21599v1) — first-public（Asia/Shanghai）：2026-07-27；exact evidence：v1；accessed：2026-09-04
- [Securing Multimodal AI through Internal Information Decomposition](https://arxiv.org/html/2607.21600v1) — first-public（Asia/Shanghai）：2026-07-27；exact evidence：v1；accessed：2026-09-04
- [Transferable Latency Prediction for Fast LLM Screening on Heterogeneous Edge Devices](https://arxiv.org/html/2607.21602v1) — first-public（Asia/Shanghai）：2026-07-27；exact evidence：v1；accessed：2026-09-04
- [AgentKVShift: Efficient KV Cache Reuse for Agentic Memory Systems](https://arxiv.org/html/2607.21604v1) — first-public（Asia/Shanghai）：2026-07-27；exact evidence：v1；accessed：2026-09-04
- [TILT: Improving Compositional Generation in Diffusion Models with a Model-Intrinsic Reward](https://arxiv.org/html/2607.21606v1) — first-public（Asia/Shanghai）：2026-07-27；exact evidence：v1；accessed：2026-09-04
- [Coupled Hierarchical Search over Topology and Execution for Agentic Workflow Synthesis](https://arxiv.org/html/2607.21609v1) — first-public（Asia/Shanghai）：2026-07-27；exact evidence：v1；accessed：2026-09-04
- [SCOPE and SCION: A Benchmark and an Auditable Reference Pipeline for Schema Induction and Fusion from Text](https://arxiv.org/html/2607.21610v1) — first-public（Asia/Shanghai）：2026-07-27；exact evidence：v1；accessed：2026-09-04
- [Procedural Knowledge Is Not Low-Rank: Why LoRA Fails to Internalize Multi-Step Procedures](https://arxiv.org/html/2607.21612v1) — first-public（Asia/Shanghai）：2026-07-27；exact evidence：v1；accessed：2026-09-04
- [The Hard Decision Layer: Evidence for Committed Inference in Transformers](https://arxiv.org/html/2607.21613v1) — first-public（Asia/Shanghai）：2026-07-27；exact evidence：v1；accessed：2026-09-04
- [Lost in Context: Addressing Context Anxiety in Large Language Models](https://arxiv.org/html/2607.21616v1) — first-public（Asia/Shanghai）：2026-07-27；exact evidence：v1；accessed：2026-09-04
- [Do VLMs Read or Rewrite? On Transcription Faithfulness in Vision-Language Models](https://arxiv.org/html/2607.21617v1) — first-public（Asia/Shanghai）：2026-07-27；exact evidence：v1；accessed：2026-09-04
- [Adversarial Style Optimization: Enhancing VLM Jailbreaks by GRPO-based Stylistic Triggers Optimization](https://arxiv.org/html/2607.21619v1) — first-public（Asia/Shanghai）：2026-07-27；exact evidence：v1；accessed：2026-09-04
- [Cloud-Native Evaluation-as-a-Service: A Microservices Architecture for Scalable AI Monitoring with Conformal Guarantees](https://arxiv.org/html/2607.21623v1) — first-public（Asia/Shanghai）：2026-07-27；exact evidence：v1；accessed：2026-09-04
- [FBLayout: Optimizing Memory Layout for Efficient LLM Finetuning on Mobile GPUs](https://arxiv.org/html/2607.21624v1) — first-public（Asia/Shanghai）：2026-07-27；exact evidence：v1；accessed：2026-09-04
- [Trajectory-Aware Retrieval Agents for Temporal Decision- Making](https://arxiv.org/html/2607.21625v1) — first-public（Asia/Shanghai）：2026-07-27；exact evidence：v1；accessed：2026-09-04
- [Do Modules Stay in Their Lane? Role Drift in Compound LLM Systems](https://arxiv.org/html/2607.21627v1) — first-public（Asia/Shanghai）：2026-07-27；exact evidence：v1；accessed：2026-09-04
- [A Consensus-Based Framework for Relative Preference Evaluation of Large Language Models](https://arxiv.org/html/2607.21632v1) — first-public（Asia/Shanghai）：2026-07-27；exact evidence：v1；accessed：2026-09-04
- [Toward User-Conditioned Evaluation of Personal LLM Agents under Temporal Interventions](https://arxiv.org/html/2607.21635v1) — first-public（Asia/Shanghai）：2026-07-27；exact evidence：v1；accessed：2026-09-04
- [Tool-Guided Retrieval-Augmented Repair for Securing LLM-Generated C Code](https://arxiv.org/html/2607.21641v1) — first-public（Asia/Shanghai）：2026-07-27；exact evidence：v1；accessed：2026-09-04
- [CARE: Pre-Execution Command Verification for Shell-Executing LLM Agents](https://arxiv.org/html/2607.21642v1) — first-public（Asia/Shanghai）：2026-07-27；exact evidence：v1；accessed：2026-09-04
- [Adjustment Speed as a Safety Constraint for Nonstationary Reinforcement Learning](https://arxiv.org/html/2607.21646v1) — first-public（Asia/Shanghai）：2026-07-27；exact evidence：v1；accessed：2026-09-04
- [Molt: A Scalable PyTorch-Native Training Framework for Agentic Reinforcement Learning](https://arxiv.org/html/2607.21653v1) — first-public（Asia/Shanghai）：2026-07-27；exact evidence：v1；accessed：2026-09-04
- [Cross-Model LLM Code Review: Should you use Claude to review Codex or vice versa?](https://arxiv.org/html/2607.21656v1) — first-public（Asia/Shanghai）：2026-07-27；exact evidence：v1；accessed：2026-09-04
- [GRACE: Gradient-Free Robot Action Generation via Combined Diffusion-MPPI Posterior Mean Estimation](https://arxiv.org/html/2607.21661v1) — first-public（Asia/Shanghai）：2026-07-27；exact evidence：v1；accessed：2026-09-04
- [Ordered Action Tokens for Visuomotor Policy Learning](https://arxiv.org/html/2607.21670v1) — first-public（Asia/Shanghai）：2026-07-27；exact evidence：v1；accessed：2026-09-04
- [Pixels for Programs? A Cross-Provider Case Study of Input-Token Accounting for Source Code as Text and Images](https://arxiv.org/html/2607.21672v1) — first-public（Asia/Shanghai）：2026-07-27；exact evidence：v1；accessed：2026-09-04
- [Output Format x Model Identity: Interaction Effects in Single-Round Coding Agent Performance](https://arxiv.org/html/2607.21674v1) — first-public（Asia/Shanghai）：2026-07-27；exact evidence：v1；accessed：2026-09-04
- [Persistent Computational State: A Session-Centric Runtime for Generative World Models](https://arxiv.org/html/2607.21686v1) — first-public（Asia/Shanghai）：2026-07-27；exact evidence：v1；accessed：2026-09-04
- [Be Consistent! Enhancing Robust Visual Reasoning in LVLMs with Consistency Constraints](https://arxiv.org/html/2607.21722v1) — first-public（Asia/Shanghai）：2026-07-27；exact evidence：v1；accessed：2026-09-04
- [Addressing the Orchestration Gap in Generalist Robots via Physical Agency](https://arxiv.org/html/2607.21725v1) — first-public（Asia/Shanghai）：2026-07-27；exact evidence：v1；accessed：2026-09-04
- [RED-PIM: Reducing Data Movement for Transformers using Processing-in-Memory](https://arxiv.org/html/2607.21731v1) — first-public（Asia/Shanghai）：2026-07-27；exact evidence：v1；accessed：2026-09-04
- [What AI Red-Team Evaluations Can and Cannot Prove](https://arxiv.org/html/2607.21735v1) — first-public（Asia/Shanghai）：2026-07-27；exact evidence：v1；accessed：2026-09-04
- [When Model Release Meets Model Reuse: Producer-Consumer Misalignment in Hugging Face](https://arxiv.org/html/2607.21738v1) — first-public（Asia/Shanghai）：2026-07-27；exact evidence：v1；accessed：2026-09-04
- [PRISM: Evaluating POSIX Storage Systems for AI Research Workflows](https://arxiv.org/html/2607.21746v1) — first-public（Asia/Shanghai）：2026-07-27；exact evidence：v1；accessed：2026-09-04
- [Parameter-free Adaptive Sparse Attention via Compression-Based Content Selection](https://arxiv.org/html/2607.21752v1) — first-public（Asia/Shanghai）：2026-07-27；exact evidence：v1；accessed：2026-09-04
- [Prompt as a Data Type: In-Database LLM Prompt Management and Rewriting](https://arxiv.org/html/2607.21756v1) — first-public（Asia/Shanghai）：2026-07-27；exact evidence：v1；accessed：2026-09-04
- [Every Model Cheats: Prompt-Level Mitigation of Cheating on Offensive Cyber Tasks](https://arxiv.org/html/2607.21763v1) — first-public（Asia/Shanghai）：2026-07-27；exact evidence：v1；accessed：2026-09-04
- [Agentic Evaluation of Copyright Law Compliance](https://arxiv.org/html/2607.21799v1) — first-public（Asia/Shanghai）：2026-07-27；exact evidence：v1；accessed：2026-09-04
- [Adversarial Prompts for Acceptance Collapse in Speculative Decoding](https://arxiv.org/html/2607.21804v1) — first-public（Asia/Shanghai）：2026-07-27；exact evidence：v1；accessed：2026-09-04
- [Protocol-Level Attacks on Agentic Commerce Platforms: A Cross-Platform Taxonomy, AIP-Bench, and Unified Defense](https://arxiv.org/html/2607.21824v1) — first-public（Asia/Shanghai）：2026-07-27；exact evidence：v1；accessed：2026-09-04
- [ToolGuardian: Declarative Security for AI Agent-Tool Interactions](https://arxiv.org/html/2607.21835v1) — first-public（Asia/Shanghai）：2026-07-27；exact evidence：v1；accessed：2026-09-04
- [SoundscapeAgent: Agentic Soundscape Construction for Controllable Synthesis and Scalable Audio-Language Supervision](https://arxiv.org/html/2607.21857v1) — first-public（Asia/Shanghai）：2026-07-27；exact evidence：v1；accessed：2026-09-04
- [Data Quality over Capacity: Internalizing Documents into LoRA Adapters for Closed-Book QA](https://arxiv.org/html/2607.21861v1) — first-public（Asia/Shanghai）：2026-07-27；exact evidence：v1；accessed：2026-09-04
- [Claim Plane: Enforceable Change Intents and Dynamic Scope for Parallel Coding Agents](https://arxiv.org/pdf/2607.21909v1) — first-public（Asia/Shanghai）：2026-07-27；exact evidence：v1；accessed：2026-09-04
- [TRW: TRACE-RealWorld---An Auditable Consistency Contract for World Models as Materialized Views](https://arxiv.org/html/2607.21910v1) — first-public（Asia/Shanghai）：2026-07-27；exact evidence：v1；accessed：2026-09-04
- [Reliability-Contagion Feasibility in LLM Multi-Agent Networks](https://arxiv.org/html/2607.21912v1) — first-public（Asia/Shanghai）：2026-07-27；exact evidence：v1；accessed：2026-09-04
- [Action-Conditioned World Model for Goal Plane Probe Guidance in Robotic Ultrasound](https://arxiv.org/html/2607.21918v1) — first-public（Asia/Shanghai）：2026-07-27；exact evidence：v1；accessed：2026-09-04
- [RIS-Kernel: A Model-Agnostic Architecture for Long-Context LLM Inference via Sparse Attention](https://arxiv.org/html/2607.21927v1) — first-public（Asia/Shanghai）：2026-07-27；exact evidence：v1；accessed：2026-09-04
- [Multi-Agent Debate and Visual Information Extraction for SeePhys Pro: A 1st-Place Technical Report from ICML 2026 AI4Math Track 3 Challenge](https://arxiv.org/html/2607.21946v1) — first-public（Asia/Shanghai）：2026-07-27；exact evidence：v1；accessed：2026-09-04
- [SIREN (Luring LLMs onto the Rocks): PAIR-Driven Preference Manipulation in Web-RAG Recommenders](https://arxiv.org/html/2607.21951v1) — first-public（Asia/Shanghai）：2026-07-27；exact evidence：v1；accessed：2026-09-04
- [Efficient Online LLM Watermark Detection via Rao-Blackwellized E-Processes](https://arxiv.org/html/2607.21958v1) — first-public（Asia/Shanghai）：2026-07-27；exact evidence：v1；accessed：2026-09-04
- [Ground Truth First: A Longitudinal Evaluation Instrument for Agent Memory, and the Tenure Crossover in Memory-Architecture Rankings](https://arxiv.org/html/2607.21962v1) — first-public（Asia/Shanghai）：2026-07-27；exact evidence：v1；accessed：2026-09-04
- [Teaching LLMs to Self-Evolve: Cultivating Core Meta-Skills with Reinforcement Learning](https://arxiv.org/html/2607.21971v1) — first-public（Asia/Shanghai）：2026-07-27；exact evidence：v1；accessed：2026-09-04
- [MoE$^2$-LoRA: When MoE Models Meet MoE-style Low-Rank Adaptation](https://arxiv.org/html/2607.21978v1) — first-public（Asia/Shanghai）：2026-07-27；exact evidence：v1；accessed：2026-09-04
- [Unified Static-Dynamic Pruning for Efficient LLM Inference](https://arxiv.org/html/2607.21985v1) — first-public（Asia/Shanghai）：2026-07-27；exact evidence：v1；accessed：2026-09-04
- [Music-JEPA: Learning a World Model of Sound from Action](https://arxiv.org/html/2607.22000v1) — first-public（Asia/Shanghai）：2026-07-27；exact evidence：v1；accessed：2026-09-04
- [Learning as Reasoning Unfolds: Progressive Rollout Allocation for Efficient Reinforcement Learning](https://arxiv.org/html/2607.22002v1) — first-public（Asia/Shanghai）：2026-07-27；exact evidence：v1；accessed：2026-09-04
- [Visual Saliency Steering Distillation for Multimodal Chain-of-Thought Reasoning](https://arxiv.org/html/2607.22013v1) — first-public（Asia/Shanghai）：2026-07-27；exact evidence：v1；accessed：2026-09-04
- [Zero-Shot Mission-Level Evaluation for Aerial MLLM Agents](https://arxiv.org/html/2607.22014v1) — first-public（Asia/Shanghai）：2026-07-27；exact evidence：v1；accessed：2026-09-04
- [HEMERA: A Heterogeneous Memory-Centric Accelerator with Recursive Dataflow for Edge-Constrained State-Space-Duality Models Inference](https://arxiv.org/html/2607.22022v1) — first-public（Asia/Shanghai）：2026-07-27；exact evidence：v1；accessed：2026-09-04
- [Agent Security Needs Redefinition through a Holistic Framework](https://arxiv.org/html/2607.22024v1) — first-public（Asia/Shanghai）：2026-07-27；exact evidence：v1；accessed：2026-09-04
- [Small Vision-Language Models Know When They Are Wrong But Cannot Say So: A Two-Model Study of Stated versus Internal Confidence Under Realistic Image Degradation](https://arxiv.org/html/2607.22034v1) — first-public（Asia/Shanghai）：2026-07-27；exact evidence：v1；accessed：2026-09-04
- [Sparse by Command: Task-Conditional Compute Skipping for Multi-Task Inference Accelerators](https://arxiv.org/html/2607.22038v1) — first-public（Asia/Shanghai）：2026-07-27；exact evidence：v1；accessed：2026-09-04
- [Enough is as good as a feast: A Comprehensive Analysis of How Reinforcement Learning Mitigates Task Conflicts in LLMs](https://arxiv.org/html/2607.22039v1) — first-public（Asia/Shanghai）：2026-07-27；exact evidence：v1；accessed：2026-09-04
- [Scaling Native Multimodal Pre-Training From Scratch](https://arxiv.org/html/2607.22043v1) — first-public（Asia/Shanghai）：2026-07-27；exact evidence：v1；accessed：2026-09-04
- [Nanbeige4.2-3B: Unlocking Agentic Capabilities in a Compact Model](https://arxiv.org/html/2607.22083v1) — first-public（Asia/Shanghai）：2026-07-27；exact evidence：v1；accessed：2026-09-04
- [Spectral Prior for Reducing Exposure Bias in Diffusion Models](https://arxiv.org/html/2607.22091v1) — first-public（Asia/Shanghai）：2026-07-27；exact evidence：v1；accessed：2026-09-04
- [Reasoning Denoiser: Denoising Reasoning Traces for Hallucination Detection in Large Reasoning Models](https://arxiv.org/html/2607.22098v1) — first-public（Asia/Shanghai）：2026-07-27；exact evidence：v1；accessed：2026-09-04
- [One Hand Watches The Other: Dynamic Multi-Agent Cooperation for Sample-Efficient Bimanual Manipulation in Dynamic Environments](https://arxiv.org/html/2607.22119v1) — first-public（Asia/Shanghai）：2026-07-27；exact evidence：v1；accessed：2026-09-04
- [Learning on the Job: Continual Learning from Deployment Feedback for Frozen-Weights Agents](https://arxiv.org/html/2607.22157v1) — first-public（Asia/Shanghai）：2026-07-27；exact evidence：v1；accessed：2026-09-04
- [DBA-Bench: A Production-Fidelity Benchmark for LLM-Based Database Operations Agents](https://arxiv.org/html/2607.22165v1) — first-public（Asia/Shanghai）：2026-07-27；exact evidence：v1；accessed：2026-09-04
- [From Isolated Tasks to Structured Capabilities: A Multilayer Taxonomy for Large Language Models](https://arxiv.org/html/2607.22182v1) — first-public（Asia/Shanghai）：2026-07-27；exact evidence：v1；accessed：2026-09-04
- [Deconstructing Off-Policy Ratios: Entropy-Scaled Trust Regions for Asynchronous Reinforcement Learning](https://arxiv.org/html/2607.22186v1) — first-public（Asia/Shanghai）：2026-07-27；exact evidence：v1；accessed：2026-09-04
- [Draining the Energy Commons: Self-Defeating Over-Appropriation as a Coordination Failure in Agentic LLM Collectives](https://arxiv.org/html/2607.22188v1) — first-public（Asia/Shanghai）：2026-07-27；exact evidence：v1；accessed：2026-09-04
- [From Score Approximation to Distribution Approximation in Score-Based Diffusion Models](https://arxiv.org/html/2607.22199v1) — first-public（Asia/Shanghai）：2026-07-27；exact evidence：v1；accessed：2026-09-04
- [Safe Learning Predictive Control for Ego-World Robotic Systems](https://arxiv.org/html/2607.22225v1) — first-public（Asia/Shanghai）：2026-07-27；exact evidence：v1；accessed：2026-09-04
- [Agentic CPU-GPU Scheduling for Heterogeneous AI Workloads](https://arxiv.org/html/2607.22242v1) — first-public（Asia/Shanghai）：2026-07-27；exact evidence：v1；accessed：2026-09-04
- [IFCLoRA: Topology-Aware Rank Allocation for Parameter-Efficient Fine-Tuning](https://arxiv.org/html/2607.22251v1) — first-public（Asia/Shanghai）：2026-07-27；exact evidence：v1；accessed：2026-09-04
- [A Roadmap to Impactful Pluralistic Alignment Research](https://arxiv.org/html/2607.22305v1) — first-public（Asia/Shanghai）：2026-07-27；exact evidence：v1；accessed：2026-09-04
- [Towards Trustworthy and Cost-Efficient Data Integration: From Naïve RAG to Agentic RAG](https://arxiv.org/html/2607.22319v1) — first-public（Asia/Shanghai）：2026-07-27；exact evidence：v1；accessed：2026-09-04
- [Cross-Tokenizer On-Policy Distillation via Byte-Prefix Marginalization](https://arxiv.org/html/2607.22334v1) — first-public（Asia/Shanghai）：2026-07-27；exact evidence：v1；accessed：2026-09-04
- [Interior interpretability with attention rollout: contraction and propagation profiles in Transformers](https://arxiv.org/html/2607.22367v1) — first-public（Asia/Shanghai）：2026-07-27；exact evidence：v1；accessed：2026-09-04
- [Do Agent Benchmarks Measure Capability? Protocol Validity in the Age of Agentic AI](https://arxiv.org/html/2607.22368v1) — first-public（Asia/Shanghai）：2026-07-27；exact evidence：v1；accessed：2026-09-04
- [Agentic Root Cause Analysis through Evidence-Grounded Reasoning](https://arxiv.org/html/2607.22385v1) — first-public（Asia/Shanghai）：2026-07-27；exact evidence：v1；accessed：2026-09-04
- [HiKV: Hierarchical Importance-Aware KV Cache with Hardware Acceleration for LLM Decoding](https://arxiv.org/html/2607.22389v1) — first-public（Asia/Shanghai）：2026-07-27；exact evidence：v1；accessed：2026-09-04
- [The Prompt Is Not the Query: How Request State Evolves Across Multi-Turn AI Conversations](https://arxiv.org/html/2607.22392v1) — first-public（Asia/Shanghai）：2026-07-27；exact evidence：v1；accessed：2026-09-04
- [SceneActBench: Can Agents Act on the 3D Scenes They See?](https://arxiv.org/html/2607.22393v1) — first-public（Asia/Shanghai）：2026-07-27；exact evidence：v1；accessed：2026-09-04
- [A Self-Calibrating Agentic AI Framework for Autonomous Edge Resource Allocation](https://arxiv.org/html/2607.22400v1) — first-public（Asia/Shanghai）：2026-07-27；exact evidence：v1；accessed：2026-09-04
- [On the Identifiability of Controlled World Models](https://arxiv.org/html/2607.22430v1) — first-public（Asia/Shanghai）：2026-07-27；exact evidence：v1；accessed：2026-09-04
- [TileSight: A First-Principles Tile-Centric Analytical GPU Performance Model from Cores to Clusters](https://arxiv.org/html/2607.22432v1) — first-public（Asia/Shanghai）：2026-07-27；exact evidence：v1；accessed：2026-09-04
- [Dynamic Capability Scoping for Enterprise AI Agents: A Synthetic Dataset and Three-Source Permission Architecture](https://arxiv.org/html/2607.22445v1) — first-public（Asia/Shanghai）：2026-07-27；exact evidence：v1；accessed：2026-09-04
- [Where Facts Go Missing: A Layerwise Taxonomy and Per-Layer Attribution of Information Omission in Air-Gapped LLMAgent Pipelines](https://arxiv.org/html/2607.22448v1) — first-public（Asia/Shanghai）：2026-07-27；exact evidence：v1；accessed：2026-09-04
- [TRACE-ROUTER: Task-Consistent and Adaptive Online Routing for Agentic AI](https://arxiv.org/html/2607.22465v1) — first-public（Asia/Shanghai）：2026-07-27；exact evidence：v1；accessed：2026-09-04
- [\k{appa}-LoRA: Condition Numbers Reveal Which LoRA Matrices Worth Updating](https://arxiv.org/html/2607.22489v1) — first-public（Asia/Shanghai）：2026-07-27；exact evidence：v1；accessed：2026-09-04
- [CausalSmith: A Formally Grounded, Self-Improving Agentic Framework for Automated Research in Causal Inference](https://arxiv.org/html/2607.22511v1) — first-public（Asia/Shanghai）：2026-07-27；exact evidence：v1；accessed：2026-09-04
- [The Regression Tax: Decomposing Why Skills Help and Hurt LLM Agents](https://arxiv.org/html/2607.22520v1) — first-public（Asia/Shanghai）：2026-07-27；exact evidence：v1；accessed：2026-09-04
- [Skill Self-Play: Pushing the Frontier of LLM Capability with Co-Evolving Skills](https://arxiv.org/html/2607.22529v1) — first-public（Asia/Shanghai）：2026-07-27；exact evidence：v1；accessed：2026-09-04
- [ViTacWorld: Scaling Visuo-Tactile World Models for Contact-Rich Robot Manipulation](https://arxiv.org/html/2607.22530v1) — first-public（Asia/Shanghai）：2026-07-27；exact evidence：v1；accessed：2026-09-04
- [Robot-Factored World Models via Robot Rendering](https://arxiv.org/html/2607.22535v1) — first-public（Asia/Shanghai）：2026-07-27；exact evidence：v1；accessed：2026-09-04

## 13. Final Status

Author-side screening、denominator、exact-v1 access、100/100 Review 与 Deep Selection receipt 已构建；Books 写回冻结，四项独立审计未完成。

State Truth: Completion=In Progress；Coverage=Open；Evidence=Open；Books=Open；Unresolved Findings=4。
