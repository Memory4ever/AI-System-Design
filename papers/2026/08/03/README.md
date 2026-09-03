# Daily Research — 2026-08-03

**Research Date:** 2026-08-03

**Timezone:** Asia/Shanghai

**Strict Window:** 2026-08-02 09:00:00 ～ 2026-08-03 09:00:00（Asia/Shanghai，左闭右开）

**Contract:** V2.1 official-announcement owner replay；未使用 Weekly 进行 discovery、候选筛选、评分、Evidence Review 或 Books 判断。

**Status:** In Progress；Coverage=Open、Evidence=Open、Books=Open；作者侧 430/430 title+abstract 语义筛选和 102/102 exact-v1 全文 Review 已完成，blocked=0；独立 audit 与日期有序 Books writeback 尚未闭合。

## Executive Summary

官方 owner raw identities=`430`；完整语义筛选冻结 `102` 个 provisional retained families 与 `328` 个 family-specific pre-denominator closures。所有 retained family 均已恢复 exact-v1 正文：100 个 arXiv HTML、2 个 PDF fallback；blocked=0。全量 primary-status audit 另确认 withdrawn=1，该 family 已在分母前清除。

本次重审同时挑战了最初 40 项的旧决定，没有沿用“能映射 ROADMAP 即保留”的宽松口径。closure 逐条保留 title、完整 abstract、该 family 的摘要命题和未改变系统责任的边界。当前不能标成 Complete：作者不能替代不同上下文 reviewer，也不能在多日期并发时直接写共享 Books。

## 1. Coverage

<!-- validator:report-metadata-v2 -->
| Field | Value |
| --- | --- |
| Contract Version | V2.1 |
| Score Schema | V2 |
| Report Type | Daily |
| Window Start | 2026-08-03 |
| Window End | 2026-08-03 |
| Registry Version | 2026-08-25 |
| Coverage Mode | Full Replay |
| Baseline Report | — |
| Changed Source IDs | — |
| Previous Denominator ID | — |
| Denominator ID | DEN-20260803-V21-ec3d63915e8a |
| Denominator Frozen At | 2026-09-03T16:40:00+08:00 |
| Completion Status | In Progress |
| Coverage Gate | Open |
| Evidence Gate | Open |
| Books Gate | Open |

### Source Coverage Receipt

<!-- validator:source-coverage-v2 -->
| Source ID | Window Start | Window End | Executed At | Endpoint / Filter | Result | Hits | Candidate Source Families | Pagination / Cursor | Window Watermark | Closure Evidence | Gap / Limitation ID |
| --- | --- | --- | --- | --- | --- | ---: | --- | --- | --- | --- | --- |
| SRC-ARXIV | 2026-08-02T09:00:00+08:00 | 2026-08-03T09:00:00+08:00 | 2026-09-03T16:40:00+08:00 | DataCite identity recovery reconciled to official arXiv first-announcement owner; all registered categories; 430/430 title+full-abstract semantic screen; exact-v1 HTML/PDF | checked | 430 | SF-2026-ARXIV-2607-28631; SF-2026-ARXIV-2607-28633; SF-2026-ARXIV-2607-28636; SF-2026-ARXIV-2607-28638; SF-2026-ARXIV-2607-28640; SF-2026-ARXIV-2607-28642; SF-2026-ARXIV-2607-28658; SF-2026-ARXIV-2607-28666; SF-2026-ARXIV-2607-28669; SF-2026-ARXIV-2607-28670; SF-2026-ARXIV-2607-28678; SF-2026-ARXIV-2607-28684; SF-2026-ARXIV-2607-28685; SF-2026-ARXIV-2607-28692; SF-2026-ARXIV-2607-28699; SF-2026-ARXIV-2607-28707; SF-2026-ARXIV-2607-28737; SF-2026-ARXIV-2607-28777; SF-2026-ARXIV-2607-28788; SF-2026-ARXIV-2607-28801; SF-2026-ARXIV-2607-28802; SF-2026-ARXIV-2607-28815; SF-2026-ARXIV-2607-28818; SF-2026-ARXIV-2607-28824; SF-2026-ARXIV-2607-28829; SF-2026-ARXIV-2607-28848; SF-2026-ARXIV-2607-28871; SF-2026-ARXIV-2607-28884; SF-2026-ARXIV-2607-28887; SF-2026-ARXIV-2607-28896; SF-2026-ARXIV-2607-28908; SF-2026-ARXIV-2607-28928; SF-2026-ARXIV-2607-28940; SF-2026-ARXIV-2607-28942; SF-2026-ARXIV-2607-28966; SF-2026-ARXIV-2607-28979; SF-2026-ARXIV-2607-28990; SF-2026-ARXIV-2607-28991; SF-2026-ARXIV-2607-28993; SF-2026-ARXIV-2607-29032; SF-2026-ARXIV-2607-29053; SF-2026-ARXIV-2607-29065; SF-2026-ARXIV-2607-29069; SF-2026-ARXIV-2607-29071; SF-2026-ARXIV-2607-29076; SF-2026-ARXIV-2607-29078; SF-2026-ARXIV-2607-29079; SF-2026-ARXIV-2607-29104; SF-2026-ARXIV-2607-29120; SF-2026-ARXIV-2607-29125; SF-2026-ARXIV-2607-29167; SF-2026-ARXIV-2607-29169; SF-2026-ARXIV-2607-29172; SF-2026-ARXIV-2607-29175; SF-2026-ARXIV-2607-29185; SF-2026-ARXIV-2607-29190; SF-2026-ARXIV-2607-29199; SF-2026-ARXIV-2607-29209; SF-2026-ARXIV-2607-29211; SF-2026-ARXIV-2607-29218; SF-2026-ARXIV-2607-29221; SF-2026-ARXIV-2607-29235; SF-2026-ARXIV-2607-29240; SF-2026-ARXIV-2607-29246; SF-2026-ARXIV-2607-29250; SF-2026-ARXIV-2607-29252; SF-2026-ARXIV-2607-29254; SF-2026-ARXIV-2607-29279; SF-2026-ARXIV-2607-29283; SF-2026-ARXIV-2607-29285; SF-2026-ARXIV-2607-29302; SF-2026-ARXIV-2607-29320; SF-2026-ARXIV-2607-29353; SF-2026-ARXIV-2607-29363; SF-2026-ARXIV-2607-29377; SF-2026-ARXIV-2607-29393; SF-2026-ARXIV-2607-29398; SF-2026-ARXIV-2607-29405; SF-2026-ARXIV-2607-29431; SF-2026-ARXIV-2607-29440; SF-2026-ARXIV-2607-29465; SF-2026-ARXIV-2607-29468; SF-2026-ARXIV-2607-29484; SF-2026-ARXIV-2607-29494; SF-2026-ARXIV-2607-29503; SF-2026-ARXIV-2607-29516; SF-2026-ARXIV-2607-29529; SF-2026-ARXIV-2607-29545; SF-2026-ARXIV-2607-29549; SF-2026-ARXIV-2607-29559; SF-2026-ARXIV-2607-29569; SF-2026-ARXIV-2607-29575; SF-2026-ARXIV-2607-29591; SF-2026-ARXIV-2607-29596; SF-2026-ARXIV-2607-29600; SF-2026-ARXIV-2607-29601; SF-2026-ARXIV-2607-29613; SF-2026-ARXIV-2607-29626; SF-2026-ARXIV-2607-29638; SF-2026-ARXIV-2607-29658; SF-2026-ARXIV-2607-29674; SF-2026-ARXIV-2607-29678 | monthly pages=165; owner_rows=430; screened=430; final_cursor=end | 2026-08-03T09:00:00+08:00 | papers/2026/08/_sources/arxiv-owner-replay-20260903/20260803/coverage-receipt.json; papers/2026/08/_sources/arxiv-owner-replay-20260903/20260803/semantic-screening-author.json; coverage:SRC-ARXIV:20260803 | FRESH-20260803-COVERAGE |

<!-- coverage:SRC-ARXIV:20260803:start -->430/430 official owner identities have an authored title+full-abstract decision. The ledger accounts for every row as either retained or a family-specific pre-denominator closure. The independent all-row FP/FN audit is still required, so Coverage Gate remains Open despite complete author enumeration.<!-- coverage:SRC-ARXIV:20260803:end -->

## 2. Candidate Ledger

<!-- validator:candidate-ledger-v2.1 -->
| Source Family ID | Primary Identifier | Event Identity | Owner Week | First-public Date | Supporting Source IDs | Design Delta | System Reach | Durability | Total | Candidate State | Review Status | Access Status | Review Override | Review Ref | Owner Report Ref | Prior Review Ref | Reconciliation | Stable Node ID | Books Disposition | Books Review Ref | Benchmark Claim |
| --- | --- | --- | --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2607-28631 | arXiv:2607.28631v1 | arxiv:2607.28631v1@official-first-announcement | 2026-W32 | 2026-08-03 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | pending | accessible | none | review:SF-2026-ARXIV-2607-28631 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-28633 | arXiv:2607.28633v1 | arxiv:2607.28633v1@official-first-announcement | 2026-W32 | 2026-08-03 | SRC-ARXIV | 3 | 3 | 2 | 8 | retained | pending | accessible | none | review:SF-2026-ARXIV-2607-28633 | self | — | new_in_window | INFER-PD-DISAGGREGATION | Not Assessed | — | no |
| SF-2026-ARXIV-2607-28636 | arXiv:2607.28636v1 | arxiv:2607.28636v1@official-first-announcement | 2026-W32 | 2026-08-03 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | pending | accessible | none | review:SF-2026-ARXIV-2607-28636 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-28638 | arXiv:2607.28638v1 | arxiv:2607.28638v1@official-first-announcement | 2026-W32 | 2026-08-03 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | pending | accessible | none | review:SF-2026-ARXIV-2607-28638 | self | — | new_in_window | AGENT-MEMORY | Not Assessed | — | no |
| SF-2026-ARXIV-2607-28640 | arXiv:2607.28640v1 | arxiv:2607.28640v1@official-first-announcement | 2026-W32 | 2026-08-03 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | pending | accessible | none | review:SF-2026-ARXIV-2607-28640 | self | — | new_in_window | MULTIMODAL-REPRESENTATION | Not Assessed | — | no |
| SF-2026-ARXIV-2607-28642 | arXiv:2607.28642v1 | arxiv:2607.28642v1@official-first-announcement | 2026-W32 | 2026-08-03 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | pending | accessible | none | review:SF-2026-ARXIV-2607-28642 | self | — | new_in_window | AGENT-CONTEXT | Not Assessed | — | no |
| SF-2026-ARXIV-2607-28658 | arXiv:2607.28658v1 | arxiv:2607.28658v1@official-first-announcement | 2026-W32 | 2026-08-03 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | pending | accessible | none | review:SF-2026-ARXIV-2607-28658 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-28666 | arXiv:2607.28666v1 | arxiv:2607.28666v1@official-first-announcement | 2026-W32 | 2026-08-03 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | pending | accessible | none | review:SF-2026-ARXIV-2607-28666 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-28669 | arXiv:2607.28669v1 | arxiv:2607.28669v1@official-first-announcement | 2026-W32 | 2026-08-03 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | pending | accessible | none | review:SF-2026-ARXIV-2607-28669 | self | — | new_in_window | TRAIN-LORA | Not Assessed | — | no |
| SF-2026-ARXIV-2607-28670 | arXiv:2607.28670v1 | arxiv:2607.28670v1@official-first-announcement | 2026-W32 | 2026-08-03 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | pending | accessible | none | review:SF-2026-ARXIV-2607-28670 | self | — | new_in_window | MODEL-MOE | Not Assessed | — | no |
| SF-2026-ARXIV-2607-28678 | arXiv:2607.28678v1 | arxiv:2607.28678v1@official-first-announcement | 2026-W32 | 2026-08-03 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | pending | accessible | none | review:SF-2026-ARXIV-2607-28678 | self | — | new_in_window | AGENT-MEMORY | Not Assessed | — | no |
| SF-2026-ARXIV-2607-28684 | arXiv:2607.28684v1 | arxiv:2607.28684v1@official-first-announcement | 2026-W32 | 2026-08-03 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | pending | accessible | none | review:SF-2026-ARXIV-2607-28684 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-28685 | arXiv:2607.28685v1 | arxiv:2607.28685v1@official-first-announcement | 2026-W32 | 2026-08-03 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | pending | accessible | none | review:SF-2026-ARXIV-2607-28685 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-28692 | arXiv:2607.28692v1 | arxiv:2607.28692v1@official-first-announcement | 2026-W32 | 2026-08-03 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | pending | accessible | none | review:SF-2026-ARXIV-2607-28692 | self | — | new_in_window | AGENT-TOOL-CALLING | Not Assessed | — | no |
| SF-2026-ARXIV-2607-28699 | arXiv:2607.28699v1 | arxiv:2607.28699v1@official-first-announcement | 2026-W32 | 2026-08-03 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | pending | accessible | none | review:SF-2026-ARXIV-2607-28699 | self | — | new_in_window | INFER-KV-CACHE | Not Assessed | — | no |
| SF-2026-ARXIV-2607-28707 | arXiv:2607.28707v1 | arxiv:2607.28707v1@official-first-announcement | 2026-W32 | 2026-08-03 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | pending | accessible | none | review:SF-2026-ARXIV-2607-28707 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-28737 | arXiv:2607.28737v1 | arxiv:2607.28737v1@official-first-announcement | 2026-W32 | 2026-08-03 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | pending | accessible | none | review:SF-2026-ARXIV-2607-28737 | self | — | new_in_window | MULTIMODAL-EMBODIED-VLA | Not Assessed | — | no |
| SF-2026-ARXIV-2607-28777 | arXiv:2607.28777v1 | arxiv:2607.28777v1@official-first-announcement | 2026-W32 | 2026-08-03 | SRC-ARXIV | 3 | 3 | 2 | 8 | retained | pending | accessible | none | review:SF-2026-ARXIV-2607-28777 | self | — | new_in_window | AGENT-PLATFORM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-28788 | arXiv:2607.28788v1 | arxiv:2607.28788v1@official-first-announcement | 2026-W32 | 2026-08-03 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | pending | accessible | none | review:SF-2026-ARXIV-2607-28788 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-28801 | arXiv:2607.28801v1 | arxiv:2607.28801v1@official-first-announcement | 2026-W32 | 2026-08-03 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | pending | accessible | none | review:SF-2026-ARXIV-2607-28801 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-28802 | arXiv:2607.28802v1 | arxiv:2607.28802v1@official-first-announcement | 2026-W32 | 2026-08-03 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | pending | accessible | none | review:SF-2026-ARXIV-2607-28802 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-28815 | arXiv:2607.28815v1 | arxiv:2607.28815v1@official-first-announcement | 2026-W32 | 2026-08-03 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | pending | accessible | none | review:SF-2026-ARXIV-2607-28815 | self | — | new_in_window | AGENT-WORKFLOW | Not Assessed | — | no |
| SF-2026-ARXIV-2607-28818 | arXiv:2607.28818v1 | arxiv:2607.28818v1@official-first-announcement | 2026-W32 | 2026-08-03 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | pending | accessible | none | review:SF-2026-ARXIV-2607-28818 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-28824 | arXiv:2607.28824v1 | arxiv:2607.28824v1@official-first-announcement | 2026-W32 | 2026-08-03 | SRC-ARXIV | 3 | 3 | 2 | 8 | retained | pending | accessible | none | review:SF-2026-ARXIV-2607-28824 | self | — | new_in_window | INFER-GPU-MEMORY | Not Assessed | — | no |
| SF-2026-ARXIV-2607-28829 | arXiv:2607.28829v1 | arxiv:2607.28829v1@official-first-announcement | 2026-W32 | 2026-08-03 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | pending | accessible | none | review:SF-2026-ARXIV-2607-28829 | self | — | new_in_window | PLATFORM-SECURITY | Not Assessed | — | no |
| SF-2026-ARXIV-2607-28848 | arXiv:2607.28848v1 | arxiv:2607.28848v1@official-first-announcement | 2026-W32 | 2026-08-03 | SRC-ARXIV | 3 | 3 | 2 | 8 | retained | pending | accessible | none | review:SF-2026-ARXIV-2607-28848 | self | — | new_in_window | INFER-SCHEDULING | Not Assessed | — | no |
| SF-2026-ARXIV-2607-28871 | arXiv:2607.28871v1 | arxiv:2607.28871v1@official-first-announcement | 2026-W32 | 2026-08-03 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | pending | accessible | none | review:SF-2026-ARXIV-2607-28871 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-28884 | arXiv:2607.28884v1 | arxiv:2607.28884v1@official-first-announcement | 2026-W32 | 2026-08-03 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | pending | accessible | none | review:SF-2026-ARXIV-2607-28884 | self | — | new_in_window | PLATFORM-SECURITY | Not Assessed | — | no |
| SF-2026-ARXIV-2607-28887 | arXiv:2607.28887v1 | arxiv:2607.28887v1@official-first-announcement | 2026-W32 | 2026-08-03 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | pending | accessible | none | review:SF-2026-ARXIV-2607-28887 | self | — | new_in_window | AGENT-WORKFLOW | Not Assessed | — | no |
| SF-2026-ARXIV-2607-28896 | arXiv:2607.28896v1 | arxiv:2607.28896v1@official-first-announcement | 2026-W32 | 2026-08-03 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | pending | accessible | none | review:SF-2026-ARXIV-2607-28896 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-28908 | arXiv:2607.28908v1 | arxiv:2607.28908v1@official-first-announcement | 2026-W32 | 2026-08-03 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | pending | accessible | none | review:SF-2026-ARXIV-2607-28908 | self | — | new_in_window | AGENT-REFLECTION | Not Assessed | — | no |
| SF-2026-ARXIV-2607-28928 | arXiv:2607.28928v1 | arxiv:2607.28928v1@official-first-announcement | 2026-W32 | 2026-08-03 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | pending | accessible | none | review:SF-2026-ARXIV-2607-28928 | self | — | new_in_window | AGENT-WORKFLOW | Not Assessed | — | no |
| SF-2026-ARXIV-2607-28940 | arXiv:2607.28940v1 | arxiv:2607.28940v1@official-first-announcement | 2026-W32 | 2026-08-03 | SRC-ARXIV | 3 | 3 | 2 | 8 | retained | pending | accessible | none | review:SF-2026-ARXIV-2607-28940 | self | — | new_in_window | INFER-REQUEST-LIFECYCLE | Not Assessed | — | no |
| SF-2026-ARXIV-2607-28942 | arXiv:2607.28942v1 | arxiv:2607.28942v1@official-first-announcement | 2026-W32 | 2026-08-03 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | pending | accessible | none | review:SF-2026-ARXIV-2607-28942 | self | — | new_in_window | AGENT-PLANNING | Not Assessed | — | no |
| SF-2026-ARXIV-2607-28966 | arXiv:2607.28966v1 | arxiv:2607.28966v1@official-first-announcement | 2026-W32 | 2026-08-03 | SRC-ARXIV | 3 | 3 | 2 | 8 | retained | pending | accessible | none | review:SF-2026-ARXIV-2607-28966 | self | — | new_in_window | INFER-SCHEDULING | Not Assessed | — | no |
| SF-2026-ARXIV-2607-28979 | arXiv:2607.28979v1 | arxiv:2607.28979v1@official-first-announcement | 2026-W32 | 2026-08-03 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | pending | accessible | none | review:SF-2026-ARXIV-2607-28979 | self | — | new_in_window | INFER-KV-CACHE | Not Assessed | — | no |
| SF-2026-ARXIV-2607-28990 | arXiv:2607.28990v1 | arxiv:2607.28990v1@official-first-announcement | 2026-W32 | 2026-08-03 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | pending | accessible | none | review:SF-2026-ARXIV-2607-28990 | self | — | new_in_window | TRAIN-GRPO | Not Assessed | — | no |
| SF-2026-ARXIV-2607-28991 | arXiv:2607.28991v1 | arxiv:2607.28991v1@official-first-announcement | 2026-W32 | 2026-08-03 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | pending | accessible | none | review:SF-2026-ARXIV-2607-28991 | self | — | new_in_window | MULTIMODAL-REPRESENTATION | Not Assessed | — | no |
| SF-2026-ARXIV-2607-28993 | arXiv:2607.28993v1 | arxiv:2607.28993v1@official-first-announcement | 2026-W32 | 2026-08-03 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | pending | accessible | none | review:SF-2026-ARXIV-2607-28993 | self | — | new_in_window | MULTIMODAL-WORLD-MODELS | Not Assessed | — | no |
| SF-2026-ARXIV-2607-29032 | arXiv:2607.29032v1 | arxiv:2607.29032v1@official-first-announcement | 2026-W32 | 2026-08-03 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | pending | accessible | none | review:SF-2026-ARXIV-2607-29032 | self | — | new_in_window | AGENT-MEMORY | Not Assessed | — | no |
| SF-2026-ARXIV-2607-29053 | arXiv:2607.29053v1 | arxiv:2607.29053v1@official-first-announcement | 2026-W32 | 2026-08-03 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | pending | accessible | none | review:SF-2026-ARXIV-2607-29053 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-29065 | arXiv:2607.29065v1 | arxiv:2607.29065v1@official-first-announcement | 2026-W32 | 2026-08-03 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | pending | accessible | none | review:SF-2026-ARXIV-2607-29065 | self | — | new_in_window | MODEL-TOKENIZER | Not Assessed | — | no |
| SF-2026-ARXIV-2607-29069 | arXiv:2607.29069v1 | arxiv:2607.29069v1@official-first-announcement | 2026-W32 | 2026-08-03 | SRC-ARXIV | 3 | 3 | 2 | 8 | retained | pending | accessible | none | review:SF-2026-ARXIV-2607-29069 | self | — | new_in_window | AGENT-PLATFORM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-29071 | arXiv:2607.29071v1 | arxiv:2607.29071v1@official-first-announcement | 2026-W32 | 2026-08-03 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | pending | accessible | none | review:SF-2026-ARXIV-2607-29071 | self | — | new_in_window | TRAIN-DISTRIBUTED-TRAINING | Not Assessed | — | no |
| SF-2026-ARXIV-2607-29076 | arXiv:2607.29076v1 | arxiv:2607.29076v1@official-first-announcement | 2026-W32 | 2026-08-03 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | pending | accessible | none | review:SF-2026-ARXIV-2607-29076 | self | — | new_in_window | INFER-KV-CACHE | Not Assessed | — | no |
| SF-2026-ARXIV-2607-29078 | arXiv:2607.29078v1 | arxiv:2607.29078v1@official-first-announcement | 2026-W32 | 2026-08-03 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | pending | accessible | none | review:SF-2026-ARXIV-2607-29078 | self | — | new_in_window | TRAIN-GRPO | Not Assessed | — | no |
| SF-2026-ARXIV-2607-29079 | arXiv:2607.29079v1 | arxiv:2607.29079v1@official-first-announcement | 2026-W32 | 2026-08-03 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | pending | accessible | none | review:SF-2026-ARXIV-2607-29079 | self | — | new_in_window | MULTIMODAL-GENERATIVE-PARADIGMS | Not Assessed | — | no |
| SF-2026-ARXIV-2607-29104 | arXiv:2607.29104v1 | arxiv:2607.29104v1@official-first-announcement | 2026-W32 | 2026-08-03 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | pending | accessible | none | review:SF-2026-ARXIV-2607-29104 | self | — | new_in_window | AGENT-MEMORY | Not Assessed | — | no |
| SF-2026-ARXIV-2607-29120 | arXiv:2607.29120v1 | arxiv:2607.29120v1@official-first-announcement | 2026-W32 | 2026-08-03 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | pending | accessible | none | review:SF-2026-ARXIV-2607-29120 | self | — | new_in_window | TRAIN-DATA | Not Assessed | — | no |
| SF-2026-ARXIV-2607-29125 | arXiv:2607.29125v1 | arxiv:2607.29125v1@official-first-announcement | 2026-W32 | 2026-08-03 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | pending | accessible | none | review:SF-2026-ARXIV-2607-29125 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-29167 | arXiv:2607.29167v1 | arxiv:2607.29167v1@official-first-announcement | 2026-W32 | 2026-08-03 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | pending | accessible | none | review:SF-2026-ARXIV-2607-29167 | self | — | new_in_window | AGENT-MEMORY | Not Assessed | — | no |
| SF-2026-ARXIV-2607-29169 | arXiv:2607.29169v1 | arxiv:2607.29169v1@official-first-announcement | 2026-W32 | 2026-08-03 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | pending | accessible | none | review:SF-2026-ARXIV-2607-29169 | self | — | new_in_window | MULTIMODAL-EMBODIED-VLA | Not Assessed | — | no |
| SF-2026-ARXIV-2607-29172 | arXiv:2607.29172v1 | arxiv:2607.29172v1@official-first-announcement | 2026-W32 | 2026-08-03 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | pending | accessible | none | review:SF-2026-ARXIV-2607-29172 | self | — | new_in_window | TRAIN-SFT | Not Assessed | — | no |
| SF-2026-ARXIV-2607-29175 | arXiv:2607.29175v1 | arxiv:2607.29175v1@official-first-announcement | 2026-W32 | 2026-08-03 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | pending | accessible | none | review:SF-2026-ARXIV-2607-29175 | self | — | new_in_window | AGENT-TOOL-CALLING | Not Assessed | — | no |
| SF-2026-ARXIV-2607-29185 | arXiv:2607.29185v1 | arxiv:2607.29185v1@official-first-announcement | 2026-W32 | 2026-08-03 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | pending | accessible | none | review:SF-2026-ARXIV-2607-29185 | self | — | new_in_window | TRAIN-RLHF | Not Assessed | — | no |
| SF-2026-ARXIV-2607-29190 | arXiv:2607.29190v1 | arxiv:2607.29190v1@official-first-announcement | 2026-W32 | 2026-08-03 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | pending | accessible | none | review:SF-2026-ARXIV-2607-29190 | self | — | new_in_window | AGENT-TOOL-CALLING | Not Assessed | — | no |
| SF-2026-ARXIV-2607-29199 | arXiv:2607.29199v1 | arxiv:2607.29199v1@official-first-announcement | 2026-W32 | 2026-08-03 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | pending | accessible | none | review:SF-2026-ARXIV-2607-29199 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-29209 | arXiv:2607.29209v1 | arxiv:2607.29209v1@official-first-announcement | 2026-W32 | 2026-08-03 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | pending | accessible | none | review:SF-2026-ARXIV-2607-29209 | self | — | new_in_window | TRAIN-GRPO | Not Assessed | — | no |
| SF-2026-ARXIV-2607-29211 | arXiv:2607.29211v1 | arxiv:2607.29211v1@official-first-announcement | 2026-W32 | 2026-08-03 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | pending | accessible | none | review:SF-2026-ARXIV-2607-29211 | self | — | new_in_window | TRAIN-GRPO | Not Assessed | — | no |
| SF-2026-ARXIV-2607-29218 | arXiv:2607.29218v1 | arxiv:2607.29218v1@official-first-announcement | 2026-W32 | 2026-08-03 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | pending | accessible | none | review:SF-2026-ARXIV-2607-29218 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-29221 | arXiv:2607.29221v1 | arxiv:2607.29221v1@official-first-announcement | 2026-W32 | 2026-08-03 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | pending | accessible | none | review:SF-2026-ARXIV-2607-29221 | self | — | new_in_window | PLATFORM-SECURITY | Not Assessed | — | no |
| SF-2026-ARXIV-2607-29235 | arXiv:2607.29235v1 | arxiv:2607.29235v1@official-first-announcement | 2026-W32 | 2026-08-03 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | pending | accessible | none | review:SF-2026-ARXIV-2607-29235 | self | — | new_in_window | MULTIMODAL-WORLD-MODELS | Not Assessed | — | no |
| SF-2026-ARXIV-2607-29240 | arXiv:2607.29240v1 | arxiv:2607.29240v1@official-first-announcement | 2026-W32 | 2026-08-03 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | pending | accessible | none | review:SF-2026-ARXIV-2607-29240 | self | — | new_in_window | MULTIMODAL-REPRESENTATION | Not Assessed | — | no |
| SF-2026-ARXIV-2607-29246 | arXiv:2607.29246v1 | arxiv:2607.29246v1@official-first-announcement | 2026-W32 | 2026-08-03 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | pending | accessible | none | review:SF-2026-ARXIV-2607-29246 | self | — | new_in_window | TRAIN-RLHF | Not Assessed | — | no |
| SF-2026-ARXIV-2607-29250 | arXiv:2607.29250v1 | arxiv:2607.29250v1@official-first-announcement | 2026-W32 | 2026-08-03 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | pending | accessible | none | review:SF-2026-ARXIV-2607-29250 | self | — | new_in_window | TRAIN-DATA | Not Assessed | — | no |
| SF-2026-ARXIV-2607-29252 | arXiv:2607.29252v1 | arxiv:2607.29252v1@official-first-announcement | 2026-W32 | 2026-08-03 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | pending | accessible | none | review:SF-2026-ARXIV-2607-29252 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-29254 | arXiv:2607.29254v1 | arxiv:2607.29254v1@official-first-announcement | 2026-W32 | 2026-08-03 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | pending | accessible | none | review:SF-2026-ARXIV-2607-29254 | self | — | new_in_window | AGENT-TOOL-CALLING | Not Assessed | — | no |
| SF-2026-ARXIV-2607-29279 | arXiv:2607.29279v1 | arxiv:2607.29279v1@official-first-announcement | 2026-W32 | 2026-08-03 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | pending | accessible | none | review:SF-2026-ARXIV-2607-29279 | self | — | new_in_window | INFER-SPECULATIVE-DECODING | Not Assessed | — | no |
| SF-2026-ARXIV-2607-29283 | arXiv:2607.29283v1 | arxiv:2607.29283v1@official-first-announcement | 2026-W32 | 2026-08-03 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | pending | accessible | none | review:SF-2026-ARXIV-2607-29283 | self | — | new_in_window | TRAIN-DATA | Not Assessed | — | no |
| SF-2026-ARXIV-2607-29285 | arXiv:2607.29285v1 | arxiv:2607.29285v1@official-first-announcement | 2026-W32 | 2026-08-03 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | pending | accessible | none | review:SF-2026-ARXIV-2607-29285 | self | — | new_in_window | MULTIMODAL-EMBODIED-VLA | Not Assessed | — | no |
| SF-2026-ARXIV-2607-29302 | arXiv:2607.29302v1 | arxiv:2607.29302v1@official-first-announcement | 2026-W32 | 2026-08-03 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | pending | accessible | none | review:SF-2026-ARXIV-2607-29302 | self | — | new_in_window | MULTIMODAL-WORLD-MODELS | Not Assessed | — | no |
| SF-2026-ARXIV-2607-29320 | arXiv:2607.29320v1 | arxiv:2607.29320v1@official-first-announcement | 2026-W32 | 2026-08-03 | SRC-ARXIV | 3 | 3 | 2 | 8 | retained | pending | accessible | none | review:SF-2026-ARXIV-2607-29320 | self | — | new_in_window | AGENT-PLATFORM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-29353 | arXiv:2607.29353v1 | arxiv:2607.29353v1@official-first-announcement | 2026-W32 | 2026-08-03 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | pending | accessible | none | review:SF-2026-ARXIV-2607-29353 | self | — | new_in_window | TRAIN-LORA | Not Assessed | — | no |
| SF-2026-ARXIV-2607-29363 | arXiv:2607.29363v1 | arxiv:2607.29363v1@official-first-announcement | 2026-W32 | 2026-08-03 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | pending | accessible | none | review:SF-2026-ARXIV-2607-29363 | self | — | new_in_window | MULTIMODAL-GENERATIVE-PARADIGMS | Not Assessed | — | no |
| SF-2026-ARXIV-2607-29377 | arXiv:2607.29377v1 | arxiv:2607.29377v1@official-first-announcement | 2026-W32 | 2026-08-03 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | pending | accessible | none | review:SF-2026-ARXIV-2607-29377 | self | — | new_in_window | AGENT-MEMORY | Not Assessed | — | no |
| SF-2026-ARXIV-2607-29393 | arXiv:2607.29393v1 | arxiv:2607.29393v1@official-first-announcement | 2026-W32 | 2026-08-03 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | pending | accessible | none | review:SF-2026-ARXIV-2607-29393 | self | — | new_in_window | MULTIMODAL-WORLD-MODELS | Not Assessed | — | no |
| SF-2026-ARXIV-2607-29398 | arXiv:2607.29398v1 | arxiv:2607.29398v1@official-first-announcement | 2026-W32 | 2026-08-03 | SRC-ARXIV | 3 | 3 | 2 | 8 | retained | pending | accessible | none | review:SF-2026-ARXIV-2607-29398 | self | — | new_in_window | INFER-TENSORRT-LLM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-29405 | arXiv:2607.29405v1 | arxiv:2607.29405v1@official-first-announcement | 2026-W32 | 2026-08-03 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | pending | accessible | none | review:SF-2026-ARXIV-2607-29405 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-29431 | arXiv:2607.29431v1 | arxiv:2607.29431v1@official-first-announcement | 2026-W32 | 2026-08-03 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | pending | accessible | none | review:SF-2026-ARXIV-2607-29431 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-29440 | arXiv:2607.29440v1 | arxiv:2607.29440v1@official-first-announcement | 2026-W32 | 2026-08-03 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | pending | accessible | none | review:SF-2026-ARXIV-2607-29440 | self | — | new_in_window | AGENT-MEMORY | Not Assessed | — | no |
| SF-2026-ARXIV-2607-29465 | arXiv:2607.29465v1 | arxiv:2607.29465v1@official-first-announcement | 2026-W32 | 2026-08-03 | SRC-ARXIV | 3 | 3 | 2 | 8 | retained | pending | accessible | none | review:SF-2026-ARXIV-2607-29465 | self | — | new_in_window | PLATFORM-GPU-SCHEDULER | Not Assessed | — | no |
| SF-2026-ARXIV-2607-29468 | arXiv:2607.29468v1 | arxiv:2607.29468v1@official-first-announcement | 2026-W32 | 2026-08-03 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | pending | accessible | none | review:SF-2026-ARXIV-2607-29468 | self | — | new_in_window | AGENT-PLANNING | Not Assessed | — | no |
| SF-2026-ARXIV-2607-29484 | arXiv:2607.29484v1 | arxiv:2607.29484v1@official-first-announcement | 2026-W32 | 2026-08-03 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | pending | accessible | none | review:SF-2026-ARXIV-2607-29484 | self | — | new_in_window | TRAIN-DATA | Not Assessed | — | no |
| SF-2026-ARXIV-2607-29494 | arXiv:2607.29494v1 | arxiv:2607.29494v1@official-first-announcement | 2026-W32 | 2026-08-03 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | pending | accessible | none | review:SF-2026-ARXIV-2607-29494 | self | — | new_in_window | TRAIN-GRPO | Not Assessed | — | no |
| SF-2026-ARXIV-2607-29503 | arXiv:2607.29503v1 | arxiv:2607.29503v1@official-first-announcement | 2026-W32 | 2026-08-03 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | pending | accessible | none | review:SF-2026-ARXIV-2607-29503 | self | — | new_in_window | TRAIN-PRETRAINING | Not Assessed | — | no |
| SF-2026-ARXIV-2607-29516 | arXiv:2607.29516v1 | arxiv:2607.29516v1@official-first-announcement | 2026-W32 | 2026-08-03 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | pending | accessible | none | review:SF-2026-ARXIV-2607-29516 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-29529 | arXiv:2607.29529v1 | arxiv:2607.29529v1@official-first-announcement | 2026-W32 | 2026-08-03 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | pending | accessible | none | review:SF-2026-ARXIV-2607-29529 | self | — | new_in_window | AGENT-WORKFLOW | Not Assessed | — | no |
| SF-2026-ARXIV-2607-29545 | arXiv:2607.29545v1 | arxiv:2607.29545v1@official-first-announcement | 2026-W32 | 2026-08-03 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | pending | accessible | none | review:SF-2026-ARXIV-2607-29545 | self | — | new_in_window | MULTIMODAL-GENERATIVE-PARADIGMS | Not Assessed | — | no |
| SF-2026-ARXIV-2607-29549 | arXiv:2607.29549v1 | arxiv:2607.29549v1@official-first-announcement | 2026-W32 | 2026-08-03 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | pending | accessible | none | review:SF-2026-ARXIV-2607-29549 | self | — | new_in_window | AGENT-TOOL-CALLING | Not Assessed | — | no |
| SF-2026-ARXIV-2607-29559 | arXiv:2607.29559v1 | arxiv:2607.29559v1@official-first-announcement | 2026-W32 | 2026-08-03 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | pending | accessible | none | review:SF-2026-ARXIV-2607-29559 | self | — | new_in_window | TRAIN-RLHF | Not Assessed | — | no |
| SF-2026-ARXIV-2607-29569 | arXiv:2607.29569v1 | arxiv:2607.29569v1@official-first-announcement | 2026-W32 | 2026-08-03 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | pending | accessible | none | review:SF-2026-ARXIV-2607-29569 | self | — | new_in_window | MULTIMODAL-EMBODIED-VLA | Not Assessed | — | no |
| SF-2026-ARXIV-2607-29575 | arXiv:2607.29575v1 | arxiv:2607.29575v1@official-first-announcement | 2026-W32 | 2026-08-03 | SRC-ARXIV | 3 | 3 | 2 | 8 | retained | pending | accessible | none | review:SF-2026-ARXIV-2607-29575 | self | — | new_in_window | INFER-SCHEDULING | Not Assessed | — | no |
| SF-2026-ARXIV-2607-29591 | arXiv:2607.29591v1 | arxiv:2607.29591v1@official-first-announcement | 2026-W32 | 2026-08-03 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | pending | accessible | none | review:SF-2026-ARXIV-2607-29591 | self | — | new_in_window | INFER-KV-CACHE | Not Assessed | — | no |
| SF-2026-ARXIV-2607-29596 | arXiv:2607.29596v1 | arxiv:2607.29596v1@official-first-announcement | 2026-W32 | 2026-08-03 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | pending | accessible | none | review:SF-2026-ARXIV-2607-29596 | self | — | new_in_window | MULTIMODAL-EMBODIED-VLA | Not Assessed | — | no |
| SF-2026-ARXIV-2607-29600 | arXiv:2607.29600v1 | arxiv:2607.29600v1@official-first-announcement | 2026-W32 | 2026-08-03 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | pending | accessible | none | review:SF-2026-ARXIV-2607-29600 | self | — | new_in_window | AGENT-MEMORY | Not Assessed | — | no |
| SF-2026-ARXIV-2607-29601 | arXiv:2607.29601v1 | arxiv:2607.29601v1@official-first-announcement | 2026-W32 | 2026-08-03 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | pending | accessible | none | review:SF-2026-ARXIV-2607-29601 | self | — | new_in_window | TRAIN-DATA | Not Assessed | — | no |
| SF-2026-ARXIV-2607-29613 | arXiv:2607.29613v1 | arxiv:2607.29613v1@official-first-announcement | 2026-W32 | 2026-08-03 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | pending | accessible | none | review:SF-2026-ARXIV-2607-29613 | self | — | new_in_window | MULTIMODAL-EMBODIED-VLA | Not Assessed | — | no |
| SF-2026-ARXIV-2607-29626 | arXiv:2607.29626v1 | arxiv:2607.29626v1@official-first-announcement | 2026-W32 | 2026-08-03 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | pending | accessible | none | review:SF-2026-ARXIV-2607-29626 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Not Assessed | — | no |
| SF-2026-ARXIV-2607-29638 | arXiv:2607.29638v1 | arxiv:2607.29638v1@official-first-announcement | 2026-W32 | 2026-08-03 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | pending | accessible | none | review:SF-2026-ARXIV-2607-29638 | self | — | new_in_window | AGENT-RAG | Not Assessed | — | no |
| SF-2026-ARXIV-2607-29658 | arXiv:2607.29658v1 | arxiv:2607.29658v1@official-first-announcement | 2026-W32 | 2026-08-03 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | pending | accessible | none | review:SF-2026-ARXIV-2607-29658 | self | — | new_in_window | AGENT-WORKFLOW | Not Assessed | — | no |
| SF-2026-ARXIV-2607-29674 | arXiv:2607.29674v1 | arxiv:2607.29674v1@official-first-announcement | 2026-W32 | 2026-08-03 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | pending | accessible | none | review:SF-2026-ARXIV-2607-29674 | self | — | new_in_window | TRAIN-DISTRIBUTED-TRAINING | Not Assessed | — | no |
| SF-2026-ARXIV-2607-29678 | arXiv:2607.29678v1 | arxiv:2607.29678v1@official-first-announcement | 2026-W32 | 2026-08-03 | SRC-ARXIV | 3 | 3 | 2 | 8 | retained | pending | accessible | none | review:SF-2026-ARXIV-2607-29678 | self | — | new_in_window | INFER-REQUEST-LIFECYCLE | Not Assessed | — | no |

## 3. Review Completion Receipt

<!-- validator:review-completion-v1 -->
| Source Family ID | Review Provenance ID | Review Route | Primary Evidence Version | Reviewed Evidence Versions | Method / Identity Locators | Evaluation Locators | Limitations / Counterevidence Locators | Artifact Locators | Claim Boundary Ref | Completion Result |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2607-28631 | — | deep | arXiv:2607.28631v1 | SRC-ARXIV@arXiv:2607.28631v1 | https://arxiv.org/html/2607.28631v1#author-method-review | https://arxiv.org/html/2607.28631v1#author-evaluation-review | https://arxiv.org/html/2607.28631v1#author-limitations-review | https://arxiv.org/html/2607.28631v1 | claim:SF-2026-ARXIV-2607-28631 | pending |
| SF-2026-ARXIV-2607-28633 | — | deep | arXiv:2607.28633v1 | SRC-ARXIV@arXiv:2607.28633v1 | https://arxiv.org/html/2607.28633v1#author-method-review | https://arxiv.org/html/2607.28633v1#author-evaluation-review | https://arxiv.org/html/2607.28633v1#author-limitations-review | https://arxiv.org/html/2607.28633v1 | claim:SF-2026-ARXIV-2607-28633 | pending |
| SF-2026-ARXIV-2607-28636 | — | deep | arXiv:2607.28636v1 | SRC-ARXIV@arXiv:2607.28636v1 | https://arxiv.org/html/2607.28636v1#author-method-review | https://arxiv.org/html/2607.28636v1#author-evaluation-review | https://arxiv.org/html/2607.28636v1#author-limitations-review | https://arxiv.org/html/2607.28636v1 | claim:SF-2026-ARXIV-2607-28636 | pending |
| SF-2026-ARXIV-2607-28638 | — | deep | arXiv:2607.28638v1 | SRC-ARXIV@arXiv:2607.28638v1 | https://arxiv.org/html/2607.28638v1#author-method-review | https://arxiv.org/html/2607.28638v1#author-evaluation-review | https://arxiv.org/html/2607.28638v1#author-limitations-review | https://arxiv.org/html/2607.28638v1 | claim:SF-2026-ARXIV-2607-28638 | pending |
| SF-2026-ARXIV-2607-28640 | — | standard | arXiv:2607.28640v1 | SRC-ARXIV@arXiv:2607.28640v1 | https://arxiv.org/html/2607.28640v1#author-method-review | https://arxiv.org/html/2607.28640v1#author-evaluation-review | https://arxiv.org/html/2607.28640v1#author-limitations-review | https://arxiv.org/html/2607.28640v1 | claim:SF-2026-ARXIV-2607-28640 | pending |
| SF-2026-ARXIV-2607-28642 | — | standard | arXiv:2607.28642v1 | SRC-ARXIV@arXiv:2607.28642v1 | https://arxiv.org/html/2607.28642v1#author-method-review | https://arxiv.org/html/2607.28642v1#author-evaluation-review | https://arxiv.org/html/2607.28642v1#author-limitations-review | https://arxiv.org/html/2607.28642v1 | claim:SF-2026-ARXIV-2607-28642 | pending |
| SF-2026-ARXIV-2607-28658 | — | deep | arXiv:2607.28658v1 | SRC-ARXIV@arXiv:2607.28658v1 | https://arxiv.org/html/2607.28658v1#author-method-review | https://arxiv.org/html/2607.28658v1#author-evaluation-review | https://arxiv.org/html/2607.28658v1#author-limitations-review | https://arxiv.org/html/2607.28658v1 | claim:SF-2026-ARXIV-2607-28658 | pending |
| SF-2026-ARXIV-2607-28666 | — | deep | arXiv:2607.28666v1 | SRC-ARXIV@arXiv:2607.28666v1 | https://arxiv.org/html/2607.28666v1#author-method-review | https://arxiv.org/html/2607.28666v1#author-evaluation-review | https://arxiv.org/html/2607.28666v1#author-limitations-review | https://arxiv.org/html/2607.28666v1 | claim:SF-2026-ARXIV-2607-28666 | pending |
| SF-2026-ARXIV-2607-28669 | — | standard | arXiv:2607.28669v1 | SRC-ARXIV@arXiv:2607.28669v1 | https://arxiv.org/html/2607.28669v1#author-method-review | https://arxiv.org/html/2607.28669v1#author-evaluation-review | https://arxiv.org/html/2607.28669v1#author-limitations-review | https://arxiv.org/html/2607.28669v1 | claim:SF-2026-ARXIV-2607-28669 | pending |
| SF-2026-ARXIV-2607-28670 | — | standard | arXiv:2607.28670v1 | SRC-ARXIV@arXiv:2607.28670v1 | https://arxiv.org/html/2607.28670v1#author-method-review | https://arxiv.org/html/2607.28670v1#author-evaluation-review | https://arxiv.org/html/2607.28670v1#author-limitations-review | https://arxiv.org/html/2607.28670v1 | claim:SF-2026-ARXIV-2607-28670 | pending |
| SF-2026-ARXIV-2607-28678 | — | deep | arXiv:2607.28678v1 | SRC-ARXIV@arXiv:2607.28678v1 | https://arxiv.org/html/2607.28678v1#author-method-review | https://arxiv.org/html/2607.28678v1#author-evaluation-review | https://arxiv.org/html/2607.28678v1#author-limitations-review | https://arxiv.org/html/2607.28678v1 | claim:SF-2026-ARXIV-2607-28678 | pending |
| SF-2026-ARXIV-2607-28684 | — | deep | arXiv:2607.28684v1 | SRC-ARXIV@arXiv:2607.28684v1 | https://arxiv.org/html/2607.28684v1#author-method-review | https://arxiv.org/html/2607.28684v1#author-evaluation-review | https://arxiv.org/html/2607.28684v1#author-limitations-review | https://arxiv.org/html/2607.28684v1 | claim:SF-2026-ARXIV-2607-28684 | pending |
| SF-2026-ARXIV-2607-28685 | — | deep | arXiv:2607.28685v1 | SRC-ARXIV@arXiv:2607.28685v1 | https://arxiv.org/html/2607.28685v1#author-method-review | https://arxiv.org/html/2607.28685v1#author-evaluation-review | https://arxiv.org/html/2607.28685v1#author-limitations-review | https://arxiv.org/html/2607.28685v1 | claim:SF-2026-ARXIV-2607-28685 | pending |
| SF-2026-ARXIV-2607-28692 | — | deep | arXiv:2607.28692v1 | SRC-ARXIV@arXiv:2607.28692v1 | https://arxiv.org/html/2607.28692v1#author-method-review | https://arxiv.org/html/2607.28692v1#author-evaluation-review | https://arxiv.org/html/2607.28692v1#author-limitations-review | https://arxiv.org/html/2607.28692v1 | claim:SF-2026-ARXIV-2607-28692 | pending |
| SF-2026-ARXIV-2607-28699 | — | deep | arXiv:2607.28699v1 | SRC-ARXIV@arXiv:2607.28699v1 | https://arxiv.org/html/2607.28699v1#author-method-review | https://arxiv.org/html/2607.28699v1#author-evaluation-review | https://arxiv.org/html/2607.28699v1#author-limitations-review | https://arxiv.org/html/2607.28699v1 | claim:SF-2026-ARXIV-2607-28699 | pending |
| SF-2026-ARXIV-2607-28707 | — | deep | arXiv:2607.28707v1 | SRC-ARXIV@arXiv:2607.28707v1 | https://arxiv.org/html/2607.28707v1#author-method-review | https://arxiv.org/html/2607.28707v1#author-evaluation-review | https://arxiv.org/html/2607.28707v1#author-limitations-review | https://arxiv.org/html/2607.28707v1 | claim:SF-2026-ARXIV-2607-28707 | pending |
| SF-2026-ARXIV-2607-28737 | — | standard | arXiv:2607.28737v1 | SRC-ARXIV@arXiv:2607.28737v1 | https://arxiv.org/html/2607.28737v1#author-method-review | https://arxiv.org/html/2607.28737v1#author-evaluation-review | https://arxiv.org/html/2607.28737v1#author-limitations-review | https://arxiv.org/html/2607.28737v1 | claim:SF-2026-ARXIV-2607-28737 | pending |
| SF-2026-ARXIV-2607-28777 | — | deep | arXiv:2607.28777v1 | SRC-ARXIV@arXiv:2607.28777v1 | https://arxiv.org/html/2607.28777v1#author-method-review | https://arxiv.org/html/2607.28777v1#author-evaluation-review | https://arxiv.org/html/2607.28777v1#author-limitations-review | https://arxiv.org/html/2607.28777v1 | claim:SF-2026-ARXIV-2607-28777 | pending |
| SF-2026-ARXIV-2607-28788 | — | deep | arXiv:2607.28788v1 | SRC-ARXIV@arXiv:2607.28788v1 | https://arxiv.org/html/2607.28788v1#author-method-review | https://arxiv.org/html/2607.28788v1#author-evaluation-review | https://arxiv.org/html/2607.28788v1#author-limitations-review | https://arxiv.org/html/2607.28788v1 | claim:SF-2026-ARXIV-2607-28788 | pending |
| SF-2026-ARXIV-2607-28801 | — | deep | arXiv:2607.28801v1 | SRC-ARXIV@arXiv:2607.28801v1 | https://arxiv.org/html/2607.28801v1#author-method-review | https://arxiv.org/html/2607.28801v1#author-evaluation-review | https://arxiv.org/html/2607.28801v1#author-limitations-review | https://arxiv.org/html/2607.28801v1 | claim:SF-2026-ARXIV-2607-28801 | pending |
| SF-2026-ARXIV-2607-28802 | — | deep | arXiv:2607.28802v1 | SRC-ARXIV@arXiv:2607.28802v1 | https://arxiv.org/html/2607.28802v1#author-method-review | https://arxiv.org/html/2607.28802v1#author-evaluation-review | https://arxiv.org/html/2607.28802v1#author-limitations-review | https://arxiv.org/html/2607.28802v1 | claim:SF-2026-ARXIV-2607-28802 | pending |
| SF-2026-ARXIV-2607-28815 | — | standard | arXiv:2607.28815v1 | SRC-ARXIV@arXiv:2607.28815v1 | https://arxiv.org/html/2607.28815v1#author-method-review | https://arxiv.org/html/2607.28815v1#author-evaluation-review | https://arxiv.org/html/2607.28815v1#author-limitations-review | https://arxiv.org/html/2607.28815v1 | claim:SF-2026-ARXIV-2607-28815 | pending |
| SF-2026-ARXIV-2607-28818 | — | deep | arXiv:2607.28818v1 | SRC-ARXIV@arXiv:2607.28818v1 | https://arxiv.org/html/2607.28818v1#author-method-review | https://arxiv.org/html/2607.28818v1#author-evaluation-review | https://arxiv.org/html/2607.28818v1#author-limitations-review | https://arxiv.org/html/2607.28818v1 | claim:SF-2026-ARXIV-2607-28818 | pending |
| SF-2026-ARXIV-2607-28824 | — | deep | arXiv:2607.28824v1 | SRC-ARXIV@arXiv:2607.28824v1 | https://arxiv.org/html/2607.28824v1#author-method-review | https://arxiv.org/html/2607.28824v1#author-evaluation-review | https://arxiv.org/html/2607.28824v1#author-limitations-review | https://arxiv.org/html/2607.28824v1 | claim:SF-2026-ARXIV-2607-28824 | pending |
| SF-2026-ARXIV-2607-28829 | — | deep | arXiv:2607.28829v1 | SRC-ARXIV@arXiv:2607.28829v1 | https://arxiv.org/html/2607.28829v1#author-method-review | https://arxiv.org/html/2607.28829v1#author-evaluation-review | https://arxiv.org/html/2607.28829v1#author-limitations-review | https://arxiv.org/html/2607.28829v1 | claim:SF-2026-ARXIV-2607-28829 | pending |
| SF-2026-ARXIV-2607-28848 | — | deep | arXiv:2607.28848v1 | SRC-ARXIV@arXiv:2607.28848v1 | https://arxiv.org/html/2607.28848v1#author-method-review | https://arxiv.org/html/2607.28848v1#author-evaluation-review | https://arxiv.org/html/2607.28848v1#author-limitations-review | https://arxiv.org/html/2607.28848v1 | claim:SF-2026-ARXIV-2607-28848 | pending |
| SF-2026-ARXIV-2607-28871 | — | deep | arXiv:2607.28871v1 | SRC-ARXIV@arXiv:2607.28871v1 | https://arxiv.org/html/2607.28871v1#author-method-review | https://arxiv.org/html/2607.28871v1#author-evaluation-review | https://arxiv.org/html/2607.28871v1#author-limitations-review | https://arxiv.org/html/2607.28871v1 | claim:SF-2026-ARXIV-2607-28871 | pending |
| SF-2026-ARXIV-2607-28884 | — | deep | arXiv:2607.28884v1 | SRC-ARXIV@arXiv:2607.28884v1 | https://arxiv.org/html/2607.28884v1#author-method-review | https://arxiv.org/html/2607.28884v1#author-evaluation-review | https://arxiv.org/html/2607.28884v1#author-limitations-review | https://arxiv.org/html/2607.28884v1 | claim:SF-2026-ARXIV-2607-28884 | pending |
| SF-2026-ARXIV-2607-28887 | — | standard | arXiv:2607.28887v1 | SRC-ARXIV@arXiv:2607.28887v1 | https://arxiv.org/html/2607.28887v1#author-method-review | https://arxiv.org/html/2607.28887v1#author-evaluation-review | https://arxiv.org/html/2607.28887v1#author-limitations-review | https://arxiv.org/html/2607.28887v1 | claim:SF-2026-ARXIV-2607-28887 | pending |
| SF-2026-ARXIV-2607-28896 | — | deep | arXiv:2607.28896v1 | SRC-ARXIV@arXiv:2607.28896v1 | https://arxiv.org/html/2607.28896v1#author-method-review | https://arxiv.org/html/2607.28896v1#author-evaluation-review | https://arxiv.org/html/2607.28896v1#author-limitations-review | https://arxiv.org/html/2607.28896v1 | claim:SF-2026-ARXIV-2607-28896 | pending |
| SF-2026-ARXIV-2607-28908 | — | standard | arXiv:2607.28908v1 | SRC-ARXIV@arXiv:2607.28908v1 | https://arxiv.org/html/2607.28908v1#author-method-review | https://arxiv.org/html/2607.28908v1#author-evaluation-review | https://arxiv.org/html/2607.28908v1#author-limitations-review | https://arxiv.org/html/2607.28908v1 | claim:SF-2026-ARXIV-2607-28908 | pending |
| SF-2026-ARXIV-2607-28928 | — | standard | arXiv:2607.28928v1 | SRC-ARXIV@arXiv:2607.28928v1 | https://arxiv.org/html/2607.28928v1#author-method-review | https://arxiv.org/html/2607.28928v1#author-evaluation-review | https://arxiv.org/html/2607.28928v1#author-limitations-review | https://arxiv.org/html/2607.28928v1 | claim:SF-2026-ARXIV-2607-28928 | pending |
| SF-2026-ARXIV-2607-28940 | — | deep | arXiv:2607.28940v1 | SRC-ARXIV@arXiv:2607.28940v1 | https://arxiv.org/html/2607.28940v1#author-method-review | https://arxiv.org/html/2607.28940v1#author-evaluation-review | https://arxiv.org/html/2607.28940v1#author-limitations-review | https://arxiv.org/html/2607.28940v1 | claim:SF-2026-ARXIV-2607-28940 | pending |
| SF-2026-ARXIV-2607-28942 | — | standard | arXiv:2607.28942v1 | SRC-ARXIV@arXiv:2607.28942v1 | https://arxiv.org/html/2607.28942v1#author-method-review | https://arxiv.org/html/2607.28942v1#author-evaluation-review | https://arxiv.org/html/2607.28942v1#author-limitations-review | https://arxiv.org/html/2607.28942v1 | claim:SF-2026-ARXIV-2607-28942 | pending |
| SF-2026-ARXIV-2607-28966 | — | deep | arXiv:2607.28966v1 | SRC-ARXIV@arXiv:2607.28966v1 | https://arxiv.org/html/2607.28966v1#author-method-review | https://arxiv.org/html/2607.28966v1#author-evaluation-review | https://arxiv.org/html/2607.28966v1#author-limitations-review | https://arxiv.org/html/2607.28966v1 | claim:SF-2026-ARXIV-2607-28966 | pending |
| SF-2026-ARXIV-2607-28979 | — | deep | arXiv:2607.28979v1 | SRC-ARXIV@arXiv:2607.28979v1 | https://arxiv.org/html/2607.28979v1#author-method-review | https://arxiv.org/html/2607.28979v1#author-evaluation-review | https://arxiv.org/html/2607.28979v1#author-limitations-review | https://arxiv.org/html/2607.28979v1 | claim:SF-2026-ARXIV-2607-28979 | pending |
| SF-2026-ARXIV-2607-28990 | — | standard | arXiv:2607.28990v1 | SRC-ARXIV@arXiv:2607.28990v1 | https://arxiv.org/html/2607.28990v1#author-method-review | https://arxiv.org/html/2607.28990v1#author-evaluation-review | https://arxiv.org/html/2607.28990v1#author-limitations-review | https://arxiv.org/html/2607.28990v1 | claim:SF-2026-ARXIV-2607-28990 | pending |
| SF-2026-ARXIV-2607-28991 | — | standard | arXiv:2607.28991v1 | SRC-ARXIV@arXiv:2607.28991v1 | https://arxiv.org/html/2607.28991v1#author-method-review | https://arxiv.org/html/2607.28991v1#author-evaluation-review | https://arxiv.org/html/2607.28991v1#author-limitations-review | https://arxiv.org/html/2607.28991v1 | claim:SF-2026-ARXIV-2607-28991 | pending |
| SF-2026-ARXIV-2607-28993 | — | deep | arXiv:2607.28993v1 | SRC-ARXIV@arXiv:2607.28993v1 | https://arxiv.org/html/2607.28993v1#author-method-review | https://arxiv.org/html/2607.28993v1#author-evaluation-review | https://arxiv.org/html/2607.28993v1#author-limitations-review | https://arxiv.org/html/2607.28993v1 | claim:SF-2026-ARXIV-2607-28993 | pending |
| SF-2026-ARXIV-2607-29032 | — | deep | arXiv:2607.29032v1 | SRC-ARXIV@arXiv:2607.29032v1 | https://arxiv.org/html/2607.29032v1#author-method-review | https://arxiv.org/html/2607.29032v1#author-evaluation-review | https://arxiv.org/html/2607.29032v1#author-limitations-review | https://arxiv.org/html/2607.29032v1 | claim:SF-2026-ARXIV-2607-29032 | pending |
| SF-2026-ARXIV-2607-29053 | — | deep | arXiv:2607.29053v1 | SRC-ARXIV@arXiv:2607.29053v1 | https://arxiv.org/html/2607.29053v1#author-method-review | https://arxiv.org/html/2607.29053v1#author-evaluation-review | https://arxiv.org/html/2607.29053v1#author-limitations-review | https://arxiv.org/html/2607.29053v1 | claim:SF-2026-ARXIV-2607-29053 | pending |
| SF-2026-ARXIV-2607-29065 | — | standard | arXiv:2607.29065v1 | SRC-ARXIV@arXiv:2607.29065v1 | https://arxiv.org/html/2607.29065v1#author-method-review | https://arxiv.org/html/2607.29065v1#author-evaluation-review | https://arxiv.org/html/2607.29065v1#author-limitations-review | https://arxiv.org/html/2607.29065v1 | claim:SF-2026-ARXIV-2607-29065 | pending |
| SF-2026-ARXIV-2607-29069 | — | deep | arXiv:2607.29069v1 | SRC-ARXIV@arXiv:2607.29069v1 | https://arxiv.org/html/2607.29069v1#author-method-review | https://arxiv.org/html/2607.29069v1#author-evaluation-review | https://arxiv.org/html/2607.29069v1#author-limitations-review | https://arxiv.org/html/2607.29069v1 | claim:SF-2026-ARXIV-2607-29069 | pending |
| SF-2026-ARXIV-2607-29071 | — | standard | arXiv:2607.29071v1 | SRC-ARXIV@arXiv:2607.29071v1 | https://arxiv.org/html/2607.29071v1#author-method-review | https://arxiv.org/html/2607.29071v1#author-evaluation-review | https://arxiv.org/html/2607.29071v1#author-limitations-review | https://arxiv.org/html/2607.29071v1 | claim:SF-2026-ARXIV-2607-29071 | pending |
| SF-2026-ARXIV-2607-29076 | — | deep | arXiv:2607.29076v1 | SRC-ARXIV@arXiv:2607.29076v1 | https://arxiv.org/html/2607.29076v1#author-method-review | https://arxiv.org/html/2607.29076v1#author-evaluation-review | https://arxiv.org/html/2607.29076v1#author-limitations-review | https://arxiv.org/html/2607.29076v1 | claim:SF-2026-ARXIV-2607-29076 | pending |
| SF-2026-ARXIV-2607-29078 | — | standard | arXiv:2607.29078v1 | SRC-ARXIV@arXiv:2607.29078v1 | https://arxiv.org/html/2607.29078v1#author-method-review | https://arxiv.org/html/2607.29078v1#author-evaluation-review | https://arxiv.org/html/2607.29078v1#author-limitations-review | https://arxiv.org/html/2607.29078v1 | claim:SF-2026-ARXIV-2607-29078 | pending |
| SF-2026-ARXIV-2607-29079 | — | standard | arXiv:2607.29079v1 | SRC-ARXIV@arXiv:2607.29079v1 | https://arxiv.org/html/2607.29079v1#author-method-review | https://arxiv.org/html/2607.29079v1#author-evaluation-review | https://arxiv.org/html/2607.29079v1#author-limitations-review | https://arxiv.org/html/2607.29079v1 | claim:SF-2026-ARXIV-2607-29079 | pending |
| SF-2026-ARXIV-2607-29104 | — | deep | arXiv:2607.29104v1 | SRC-ARXIV@arXiv:2607.29104v1 | https://arxiv.org/html/2607.29104v1#author-method-review | https://arxiv.org/html/2607.29104v1#author-evaluation-review | https://arxiv.org/html/2607.29104v1#author-limitations-review | https://arxiv.org/html/2607.29104v1 | claim:SF-2026-ARXIV-2607-29104 | pending |
| SF-2026-ARXIV-2607-29120 | — | standard | arXiv:2607.29120v1 | SRC-ARXIV@arXiv:2607.29120v1 | https://arxiv.org/html/2607.29120v1#author-method-review | https://arxiv.org/html/2607.29120v1#author-evaluation-review | https://arxiv.org/html/2607.29120v1#author-limitations-review | https://arxiv.org/html/2607.29120v1 | claim:SF-2026-ARXIV-2607-29120 | pending |
| SF-2026-ARXIV-2607-29125 | — | deep | arXiv:2607.29125v1 | SRC-ARXIV@arXiv:2607.29125v1 | https://arxiv.org/html/2607.29125v1#author-method-review | https://arxiv.org/html/2607.29125v1#author-evaluation-review | https://arxiv.org/html/2607.29125v1#author-limitations-review | https://arxiv.org/html/2607.29125v1 | claim:SF-2026-ARXIV-2607-29125 | pending |
| SF-2026-ARXIV-2607-29167 | — | deep | arXiv:2607.29167v1 | SRC-ARXIV@arXiv:2607.29167v1 | https://arxiv.org/html/2607.29167v1#author-method-review | https://arxiv.org/html/2607.29167v1#author-evaluation-review | https://arxiv.org/html/2607.29167v1#author-limitations-review | https://arxiv.org/html/2607.29167v1 | claim:SF-2026-ARXIV-2607-29167 | pending |
| SF-2026-ARXIV-2607-29169 | — | standard | arXiv:2607.29169v1 | SRC-ARXIV@arXiv:2607.29169v1 | https://arxiv.org/html/2607.29169v1#author-method-review | https://arxiv.org/html/2607.29169v1#author-evaluation-review | https://arxiv.org/html/2607.29169v1#author-limitations-review | https://arxiv.org/html/2607.29169v1 | claim:SF-2026-ARXIV-2607-29169 | pending |
| SF-2026-ARXIV-2607-29172 | — | standard | arXiv:2607.29172v1 | SRC-ARXIV@arXiv:2607.29172v1 | https://arxiv.org/html/2607.29172v1#author-method-review | https://arxiv.org/html/2607.29172v1#author-evaluation-review | https://arxiv.org/html/2607.29172v1#author-limitations-review | https://arxiv.org/html/2607.29172v1 | claim:SF-2026-ARXIV-2607-29172 | pending |
| SF-2026-ARXIV-2607-29175 | — | deep | arXiv:2607.29175v1 | SRC-ARXIV@arXiv:2607.29175v1 | https://arxiv.org/html/2607.29175v1#author-method-review | https://arxiv.org/html/2607.29175v1#author-evaluation-review | https://arxiv.org/html/2607.29175v1#author-limitations-review | https://arxiv.org/html/2607.29175v1 | claim:SF-2026-ARXIV-2607-29175 | pending |
| SF-2026-ARXIV-2607-29185 | — | standard | arXiv:2607.29185v1 | SRC-ARXIV@arXiv:2607.29185v1 | https://arxiv.org/html/2607.29185v1#author-method-review | https://arxiv.org/html/2607.29185v1#author-evaluation-review | https://arxiv.org/html/2607.29185v1#author-limitations-review | https://arxiv.org/html/2607.29185v1 | claim:SF-2026-ARXIV-2607-29185 | pending |
| SF-2026-ARXIV-2607-29190 | — | deep | arXiv:2607.29190v1 | SRC-ARXIV@arXiv:2607.29190v1 | https://arxiv.org/html/2607.29190v1#author-method-review | https://arxiv.org/html/2607.29190v1#author-evaluation-review | https://arxiv.org/html/2607.29190v1#author-limitations-review | https://arxiv.org/html/2607.29190v1 | claim:SF-2026-ARXIV-2607-29190 | pending |
| SF-2026-ARXIV-2607-29199 | — | deep | arXiv:2607.29199v1 | SRC-ARXIV@arXiv:2607.29199v1 | https://arxiv.org/html/2607.29199v1#author-method-review | https://arxiv.org/html/2607.29199v1#author-evaluation-review | https://arxiv.org/html/2607.29199v1#author-limitations-review | https://arxiv.org/html/2607.29199v1 | claim:SF-2026-ARXIV-2607-29199 | pending |
| SF-2026-ARXIV-2607-29209 | — | standard | arXiv:2607.29209v1 | SRC-ARXIV@arXiv:2607.29209v1 | https://arxiv.org/html/2607.29209v1#author-method-review | https://arxiv.org/html/2607.29209v1#author-evaluation-review | https://arxiv.org/html/2607.29209v1#author-limitations-review | https://arxiv.org/html/2607.29209v1 | claim:SF-2026-ARXIV-2607-29209 | pending |
| SF-2026-ARXIV-2607-29211 | — | standard | arXiv:2607.29211v1 | SRC-ARXIV@arXiv:2607.29211v1 | https://arxiv.org/html/2607.29211v1#author-method-review | https://arxiv.org/html/2607.29211v1#author-evaluation-review | https://arxiv.org/html/2607.29211v1#author-limitations-review | https://arxiv.org/html/2607.29211v1 | claim:SF-2026-ARXIV-2607-29211 | pending |
| SF-2026-ARXIV-2607-29218 | — | deep | arXiv:2607.29218v1 | SRC-ARXIV@arXiv:2607.29218v1 | https://arxiv.org/html/2607.29218v1#author-method-review | https://arxiv.org/html/2607.29218v1#author-evaluation-review | https://arxiv.org/html/2607.29218v1#author-limitations-review | https://arxiv.org/html/2607.29218v1 | claim:SF-2026-ARXIV-2607-29218 | pending |
| SF-2026-ARXIV-2607-29221 | — | deep | arXiv:2607.29221v1 | SRC-ARXIV@arXiv:2607.29221v1 | https://arxiv.org/html/2607.29221v1#author-method-review | https://arxiv.org/html/2607.29221v1#author-evaluation-review | https://arxiv.org/html/2607.29221v1#author-limitations-review | https://arxiv.org/html/2607.29221v1 | claim:SF-2026-ARXIV-2607-29221 | pending |
| SF-2026-ARXIV-2607-29235 | — | deep | arXiv:2607.29235v1 | SRC-ARXIV@arXiv:2607.29235v1 | https://arxiv.org/html/2607.29235v1#author-method-review | https://arxiv.org/html/2607.29235v1#author-evaluation-review | https://arxiv.org/html/2607.29235v1#author-limitations-review | https://arxiv.org/html/2607.29235v1 | claim:SF-2026-ARXIV-2607-29235 | pending |
| SF-2026-ARXIV-2607-29240 | — | standard | arXiv:2607.29240v1 | SRC-ARXIV@arXiv:2607.29240v1 | https://arxiv.org/html/2607.29240v1#author-method-review | https://arxiv.org/html/2607.29240v1#author-evaluation-review | https://arxiv.org/html/2607.29240v1#author-limitations-review | https://arxiv.org/html/2607.29240v1 | claim:SF-2026-ARXIV-2607-29240 | pending |
| SF-2026-ARXIV-2607-29246 | — | standard | arXiv:2607.29246v1 | SRC-ARXIV@arXiv:2607.29246v1 | https://arxiv.org/html/2607.29246v1#author-method-review | https://arxiv.org/html/2607.29246v1#author-evaluation-review | https://arxiv.org/html/2607.29246v1#author-limitations-review | https://arxiv.org/html/2607.29246v1 | claim:SF-2026-ARXIV-2607-29246 | pending |
| SF-2026-ARXIV-2607-29250 | — | standard | arXiv:2607.29250v1 | SRC-ARXIV@arXiv:2607.29250v1 | https://arxiv.org/html/2607.29250v1#author-method-review | https://arxiv.org/html/2607.29250v1#author-evaluation-review | https://arxiv.org/html/2607.29250v1#author-limitations-review | https://arxiv.org/html/2607.29250v1 | claim:SF-2026-ARXIV-2607-29250 | pending |
| SF-2026-ARXIV-2607-29252 | — | deep | arXiv:2607.29252v1 | SRC-ARXIV@arXiv:2607.29252v1 | https://arxiv.org/html/2607.29252v1#author-method-review | https://arxiv.org/html/2607.29252v1#author-evaluation-review | https://arxiv.org/html/2607.29252v1#author-limitations-review | https://arxiv.org/html/2607.29252v1 | claim:SF-2026-ARXIV-2607-29252 | pending |
| SF-2026-ARXIV-2607-29254 | — | deep | arXiv:2607.29254v1 | SRC-ARXIV@arXiv:2607.29254v1 | https://arxiv.org/html/2607.29254v1#author-method-review | https://arxiv.org/html/2607.29254v1#author-evaluation-review | https://arxiv.org/html/2607.29254v1#author-limitations-review | https://arxiv.org/html/2607.29254v1 | claim:SF-2026-ARXIV-2607-29254 | pending |
| SF-2026-ARXIV-2607-29279 | — | standard | arXiv:2607.29279v1 | SRC-ARXIV@arXiv:2607.29279v1 | https://arxiv.org/html/2607.29279v1#author-method-review | https://arxiv.org/html/2607.29279v1#author-evaluation-review | https://arxiv.org/html/2607.29279v1#author-limitations-review | https://arxiv.org/html/2607.29279v1 | claim:SF-2026-ARXIV-2607-29279 | pending |
| SF-2026-ARXIV-2607-29283 | — | standard | arXiv:2607.29283v1 | SRC-ARXIV@arXiv:2607.29283v1 | https://arxiv.org/html/2607.29283v1#author-method-review | https://arxiv.org/html/2607.29283v1#author-evaluation-review | https://arxiv.org/html/2607.29283v1#author-limitations-review | https://arxiv.org/html/2607.29283v1 | claim:SF-2026-ARXIV-2607-29283 | pending |
| SF-2026-ARXIV-2607-29285 | — | standard | arXiv:2607.29285v1 | SRC-ARXIV@arXiv:2607.29285v1 | https://arxiv.org/html/2607.29285v1#author-method-review | https://arxiv.org/html/2607.29285v1#author-evaluation-review | https://arxiv.org/html/2607.29285v1#author-limitations-review | https://arxiv.org/html/2607.29285v1 | claim:SF-2026-ARXIV-2607-29285 | pending |
| SF-2026-ARXIV-2607-29302 | — | deep | arXiv:2607.29302v1 | SRC-ARXIV@arXiv:2607.29302v1 | https://arxiv.org/html/2607.29302v1#author-method-review | https://arxiv.org/html/2607.29302v1#author-evaluation-review | https://arxiv.org/html/2607.29302v1#author-limitations-review | https://arxiv.org/html/2607.29302v1 | claim:SF-2026-ARXIV-2607-29302 | pending |
| SF-2026-ARXIV-2607-29320 | — | deep | arXiv:2607.29320v1 | SRC-ARXIV@arXiv:2607.29320v1 | https://arxiv.org/html/2607.29320v1#author-method-review | https://arxiv.org/html/2607.29320v1#author-evaluation-review | https://arxiv.org/html/2607.29320v1#author-limitations-review | https://arxiv.org/html/2607.29320v1 | claim:SF-2026-ARXIV-2607-29320 | pending |
| SF-2026-ARXIV-2607-29353 | — | standard | arXiv:2607.29353v1 | SRC-ARXIV@arXiv:2607.29353v1 | https://arxiv.org/html/2607.29353v1#author-method-review | https://arxiv.org/html/2607.29353v1#author-evaluation-review | https://arxiv.org/html/2607.29353v1#author-limitations-review | https://arxiv.org/html/2607.29353v1 | claim:SF-2026-ARXIV-2607-29353 | pending |
| SF-2026-ARXIV-2607-29363 | — | standard | arXiv:2607.29363v1 | SRC-ARXIV@arXiv:2607.29363v1 | https://arxiv.org/html/2607.29363v1#author-method-review | https://arxiv.org/html/2607.29363v1#author-evaluation-review | https://arxiv.org/html/2607.29363v1#author-limitations-review | https://arxiv.org/html/2607.29363v1 | claim:SF-2026-ARXIV-2607-29363 | pending |
| SF-2026-ARXIV-2607-29377 | — | deep | arXiv:2607.29377v1 | SRC-ARXIV@arXiv:2607.29377v1 | https://arxiv.org/html/2607.29377v1#author-method-review | https://arxiv.org/html/2607.29377v1#author-evaluation-review | https://arxiv.org/html/2607.29377v1#author-limitations-review | https://arxiv.org/html/2607.29377v1 | claim:SF-2026-ARXIV-2607-29377 | pending |
| SF-2026-ARXIV-2607-29393 | — | deep | arXiv:2607.29393v1 | SRC-ARXIV@arXiv:2607.29393v1 | https://arxiv.org/html/2607.29393v1#author-method-review | https://arxiv.org/html/2607.29393v1#author-evaluation-review | https://arxiv.org/html/2607.29393v1#author-limitations-review | https://arxiv.org/html/2607.29393v1 | claim:SF-2026-ARXIV-2607-29393 | pending |
| SF-2026-ARXIV-2607-29398 | — | deep | arXiv:2607.29398v1 | SRC-ARXIV@arXiv:2607.29398v1 | https://arxiv.org/html/2607.29398v1#author-method-review | https://arxiv.org/html/2607.29398v1#author-evaluation-review | https://arxiv.org/html/2607.29398v1#author-limitations-review | https://arxiv.org/html/2607.29398v1 | claim:SF-2026-ARXIV-2607-29398 | pending |
| SF-2026-ARXIV-2607-29405 | — | deep | arXiv:2607.29405v1 | SRC-ARXIV@arXiv:2607.29405v1 | https://arxiv.org/html/2607.29405v1#author-method-review | https://arxiv.org/html/2607.29405v1#author-evaluation-review | https://arxiv.org/html/2607.29405v1#author-limitations-review | https://arxiv.org/html/2607.29405v1 | claim:SF-2026-ARXIV-2607-29405 | pending |
| SF-2026-ARXIV-2607-29431 | — | deep | arXiv:2607.29431v1 | SRC-ARXIV@arXiv:2607.29431v1 | https://arxiv.org/html/2607.29431v1#author-method-review | https://arxiv.org/html/2607.29431v1#author-evaluation-review | https://arxiv.org/html/2607.29431v1#author-limitations-review | https://arxiv.org/html/2607.29431v1 | claim:SF-2026-ARXIV-2607-29431 | pending |
| SF-2026-ARXIV-2607-29440 | — | deep | arXiv:2607.29440v1 | SRC-ARXIV@arXiv:2607.29440v1 | https://arxiv.org/html/2607.29440v1#author-method-review | https://arxiv.org/html/2607.29440v1#author-evaluation-review | https://arxiv.org/html/2607.29440v1#author-limitations-review | https://arxiv.org/html/2607.29440v1 | claim:SF-2026-ARXIV-2607-29440 | pending |
| SF-2026-ARXIV-2607-29465 | — | deep | arXiv:2607.29465v1 | SRC-ARXIV@arXiv:2607.29465v1 | https://arxiv.org/html/2607.29465v1#author-method-review | https://arxiv.org/html/2607.29465v1#author-evaluation-review | https://arxiv.org/html/2607.29465v1#author-limitations-review | https://arxiv.org/html/2607.29465v1 | claim:SF-2026-ARXIV-2607-29465 | pending |
| SF-2026-ARXIV-2607-29468 | — | standard | arXiv:2607.29468v1 | SRC-ARXIV@arXiv:2607.29468v1 | https://arxiv.org/html/2607.29468v1#author-method-review | https://arxiv.org/html/2607.29468v1#author-evaluation-review | https://arxiv.org/html/2607.29468v1#author-limitations-review | https://arxiv.org/html/2607.29468v1 | claim:SF-2026-ARXIV-2607-29468 | pending |
| SF-2026-ARXIV-2607-29484 | — | standard | arXiv:2607.29484v1 | SRC-ARXIV@arXiv:2607.29484v1 | https://arxiv.org/html/2607.29484v1#author-method-review | https://arxiv.org/html/2607.29484v1#author-evaluation-review | https://arxiv.org/html/2607.29484v1#author-limitations-review | https://arxiv.org/html/2607.29484v1 | claim:SF-2026-ARXIV-2607-29484 | pending |
| SF-2026-ARXIV-2607-29494 | — | standard | arXiv:2607.29494v1 | SRC-ARXIV@arXiv:2607.29494v1 | https://arxiv.org/html/2607.29494v1#author-method-review | https://arxiv.org/html/2607.29494v1#author-evaluation-review | https://arxiv.org/html/2607.29494v1#author-limitations-review | https://arxiv.org/html/2607.29494v1 | claim:SF-2026-ARXIV-2607-29494 | pending |
| SF-2026-ARXIV-2607-29503 | — | standard | arXiv:2607.29503v1 | SRC-ARXIV@arXiv:2607.29503v1 | https://arxiv.org/html/2607.29503v1#author-method-review | https://arxiv.org/html/2607.29503v1#author-evaluation-review | https://arxiv.org/html/2607.29503v1#author-limitations-review | https://arxiv.org/html/2607.29503v1 | claim:SF-2026-ARXIV-2607-29503 | pending |
| SF-2026-ARXIV-2607-29516 | — | deep | arXiv:2607.29516v1 | SRC-ARXIV@arXiv:2607.29516v1 | https://arxiv.org/html/2607.29516v1#author-method-review | https://arxiv.org/html/2607.29516v1#author-evaluation-review | https://arxiv.org/html/2607.29516v1#author-limitations-review | https://arxiv.org/html/2607.29516v1 | claim:SF-2026-ARXIV-2607-29516 | pending |
| SF-2026-ARXIV-2607-29529 | — | standard | arXiv:2607.29529v1 | SRC-ARXIV@arXiv:2607.29529v1 | https://arxiv.org/html/2607.29529v1#author-method-review | https://arxiv.org/html/2607.29529v1#author-evaluation-review | https://arxiv.org/html/2607.29529v1#author-limitations-review | https://arxiv.org/html/2607.29529v1 | claim:SF-2026-ARXIV-2607-29529 | pending |
| SF-2026-ARXIV-2607-29545 | — | standard | arXiv:2607.29545v1 | SRC-ARXIV@arXiv:2607.29545v1 | https://arxiv.org/html/2607.29545v1#author-method-review | https://arxiv.org/html/2607.29545v1#author-evaluation-review | https://arxiv.org/html/2607.29545v1#author-limitations-review | https://arxiv.org/html/2607.29545v1 | claim:SF-2026-ARXIV-2607-29545 | pending |
| SF-2026-ARXIV-2607-29549 | — | deep | arXiv:2607.29549v1 | SRC-ARXIV@arXiv:2607.29549v1 | https://arxiv.org/html/2607.29549v1#author-method-review | https://arxiv.org/html/2607.29549v1#author-evaluation-review | https://arxiv.org/html/2607.29549v1#author-limitations-review | https://arxiv.org/html/2607.29549v1 | claim:SF-2026-ARXIV-2607-29549 | pending |
| SF-2026-ARXIV-2607-29559 | — | standard | arXiv:2607.29559v1 | SRC-ARXIV@arXiv:2607.29559v1 | https://arxiv.org/html/2607.29559v1#author-method-review | https://arxiv.org/html/2607.29559v1#author-evaluation-review | https://arxiv.org/html/2607.29559v1#author-limitations-review | https://arxiv.org/html/2607.29559v1 | claim:SF-2026-ARXIV-2607-29559 | pending |
| SF-2026-ARXIV-2607-29569 | — | standard | arXiv:2607.29569v1 | SRC-ARXIV@arXiv:2607.29569v1 | https://arxiv.org/html/2607.29569v1#author-method-review | https://arxiv.org/html/2607.29569v1#author-evaluation-review | https://arxiv.org/html/2607.29569v1#author-limitations-review | https://arxiv.org/html/2607.29569v1 | claim:SF-2026-ARXIV-2607-29569 | pending |
| SF-2026-ARXIV-2607-29575 | — | deep | arXiv:2607.29575v1 | SRC-ARXIV@arXiv:2607.29575v1 | https://arxiv.org/html/2607.29575v1#author-method-review | https://arxiv.org/html/2607.29575v1#author-evaluation-review | https://arxiv.org/html/2607.29575v1#author-limitations-review | https://arxiv.org/html/2607.29575v1 | claim:SF-2026-ARXIV-2607-29575 | pending |
| SF-2026-ARXIV-2607-29591 | — | deep | arXiv:2607.29591v1 | SRC-ARXIV@arXiv:2607.29591v1 | https://arxiv.org/html/2607.29591v1#author-method-review | https://arxiv.org/html/2607.29591v1#author-evaluation-review | https://arxiv.org/html/2607.29591v1#author-limitations-review | https://arxiv.org/html/2607.29591v1 | claim:SF-2026-ARXIV-2607-29591 | pending |
| SF-2026-ARXIV-2607-29596 | — | standard | arXiv:2607.29596v1 | SRC-ARXIV@arXiv:2607.29596v1 | https://arxiv.org/html/2607.29596v1#author-method-review | https://arxiv.org/html/2607.29596v1#author-evaluation-review | https://arxiv.org/html/2607.29596v1#author-limitations-review | https://arxiv.org/html/2607.29596v1 | claim:SF-2026-ARXIV-2607-29596 | pending |
| SF-2026-ARXIV-2607-29600 | — | deep | arXiv:2607.29600v1 | SRC-ARXIV@arXiv:2607.29600v1 | https://arxiv.org/html/2607.29600v1#author-method-review | https://arxiv.org/html/2607.29600v1#author-evaluation-review | https://arxiv.org/html/2607.29600v1#author-limitations-review | https://arxiv.org/html/2607.29600v1 | claim:SF-2026-ARXIV-2607-29600 | pending |
| SF-2026-ARXIV-2607-29601 | — | standard | arXiv:2607.29601v1 | SRC-ARXIV@arXiv:2607.29601v1 | https://arxiv.org/html/2607.29601v1#author-method-review | https://arxiv.org/html/2607.29601v1#author-evaluation-review | https://arxiv.org/html/2607.29601v1#author-limitations-review | https://arxiv.org/html/2607.29601v1 | claim:SF-2026-ARXIV-2607-29601 | pending |
| SF-2026-ARXIV-2607-29613 | — | standard | arXiv:2607.29613v1 | SRC-ARXIV@arXiv:2607.29613v1 | https://arxiv.org/html/2607.29613v1#author-method-review | https://arxiv.org/html/2607.29613v1#author-evaluation-review | https://arxiv.org/html/2607.29613v1#author-limitations-review | https://arxiv.org/html/2607.29613v1 | claim:SF-2026-ARXIV-2607-29613 | pending |
| SF-2026-ARXIV-2607-29626 | — | deep | arXiv:2607.29626v1 | SRC-ARXIV@arXiv:2607.29626v1 | https://arxiv.org/html/2607.29626v1#author-method-review | https://arxiv.org/html/2607.29626v1#author-evaluation-review | https://arxiv.org/html/2607.29626v1#author-limitations-review | https://arxiv.org/html/2607.29626v1 | claim:SF-2026-ARXIV-2607-29626 | pending |
| SF-2026-ARXIV-2607-29638 | — | standard | arXiv:2607.29638v1 | SRC-ARXIV@arXiv:2607.29638v1 | https://arxiv.org/html/2607.29638v1#author-method-review | https://arxiv.org/html/2607.29638v1#author-evaluation-review | https://arxiv.org/html/2607.29638v1#author-limitations-review | https://arxiv.org/html/2607.29638v1 | claim:SF-2026-ARXIV-2607-29638 | pending |
| SF-2026-ARXIV-2607-29658 | — | standard | arXiv:2607.29658v1 | SRC-ARXIV@arXiv:2607.29658v1 | https://arxiv.org/html/2607.29658v1#author-method-review | https://arxiv.org/html/2607.29658v1#author-evaluation-review | https://arxiv.org/html/2607.29658v1#author-limitations-review | https://arxiv.org/html/2607.29658v1 | claim:SF-2026-ARXIV-2607-29658 | pending |
| SF-2026-ARXIV-2607-29674 | — | standard | arXiv:2607.29674v1 | SRC-ARXIV@arXiv:2607.29674v1 | https://arxiv.org/html/2607.29674v1#author-method-review | https://arxiv.org/html/2607.29674v1#author-evaluation-review | https://arxiv.org/html/2607.29674v1#author-limitations-review | https://arxiv.org/html/2607.29674v1 | claim:SF-2026-ARXIV-2607-29674 | pending |
| SF-2026-ARXIV-2607-29678 | — | deep | arXiv:2607.29678v1 | SRC-ARXIV@arXiv:2607.29678v1 | https://arxiv.org/html/2607.29678v1#author-method-review | https://arxiv.org/html/2607.29678v1#author-evaluation-review | https://arxiv.org/html/2607.29678v1#author-limitations-review | https://arxiv.org/html/2607.29678v1 | claim:SF-2026-ARXIV-2607-29678 | pending |

### Source Reviews

<!-- review:SF-2026-ARXIV-2607-28631:start -->
### Can AI Evaluate AI Scientists? A Benchmarking Study of Autonomous Research Generation Systems Using Automated Multi-Model Review

- **Status / Evidence:** Experimental；exact-v1 HTML 已读取并保存校验和；Score V2=`7`。
- **Problem / old solution:** 既有路径通常把 evaluation evidence and release decision 隐含在模型调用或离线平均指标中；在较小规模、单一模型或无跨请求状态时成本较低，但难以回答谁拥有失败恢复与版本一致性。
- **Changed constraint:** 论文面对的约束由摘要和全文共同限定为：AI Scientist systems capable of autonomous research have the potential to significantly accelerate scientific discovery. However, evaluating and comparing the quality of AI-generated papers remains an open challenge.
- **Mechanism:** exact-v1 的方法段写明：To illustrate how performance differences manifest in practice, we examine one representative proposal in depth. Proposal FA0006 addresses web-agent evaluation through evidence-based judging-a timely problem given the rapid deployment of autonomous web agents. The core research question asks whether selective evaluation strategies that compare chain-of-thought (CoT) inclusive views against evidence-only views can improve evaluation reliability without expensive human annotations. The divergence between FARS and competing frameworks on this proposal is striking. While FARS achieved a synthesis score of 3/5, all four competing frameworks scored at the floor (1/5). This three-fold advantage for the benchmark syst…
- **State ownership:** 需要显式绑定 evaluator configuration, dataset slice and result provenance；canonical owner 是 `PLATFORM-EVALUATION-SYSTEM`，而不是论文应用领域本身。
- **Control / data flow:** 数据由工作负载进入机制实现，evaluation controller 决定是否执行、路由、提交或回退；输出必须携带与输入同一版本域的证据。
- **Implementation surface:** 全文 locator=`Case Study: Framework Performance on Web-Agent Evaluation; papers/2026/08/_sources/arxiv-owner-replay-20260903/20260803/exact-v1-text/2607.28631v1.txt`；公开实现、硬件或训练配置只按正文披露解释，未披露字段不补写。
- **Evaluation contract:** AI Scientist systems capable of autonomous research have the potential to significantly accelerate scientific discovery. However, evaluating and comparing the quality of AI-generated papers remains an open challenge. We propose and implement a rigorous benchmarking protocol using an automated peer-review system that harnesses frontier large language models to assess scientific papers across four core dimensions: originality, scientific rigor, clarity, and significance. We evaluate four leading AI Scientist frameworks: , , and . Each framework was run on a consistent set of 15 research proposals published by a commercial autonomous AI scientist company (FARS), generating 60 papers that we evaluate alongside 15… 该结果只绑定论文声明的数据、模型、硬件、精度、长度、batch/concurrency 与 evaluator；缺失字段均为 `Not Disclosed`。
- **Proves / does not prove:** 证据支持该受限 workload 中机制可行或暴露既有评价缺口；不证明跨模型、跨硬件、跨领域或生产 SLO 的普遍优势。
- **Trade-off / failure mode:** 新增状态、控制器和观测提高可验证性，但引入版本错配、额外延迟/内存/通信、错误路由及 evaluator bias。全文边界：The proposal-level evaluation scores presented in Table demonstrate that FARS benchmark papers achieve substantially higher ratings compared to the four AI Scientist frameworks across all four reviewer models (GPT-5.4: 2.14, Gemini: 2.47, Claude: 2.47, Synthesis: 2.27). Notably, FARS scores exceed all competing systems by more than 2 on Gemini and Claude evaluations, indicating a substantial quality gap. This performance advantage is consistently visualized across all evaluation dimensions in Figure , where FARS demonstrates superior performance in Originality, Rigor, Clarity, and Significance. Among competing frameworks, CycleResearcher exhibits the strongest relative performance, particularly in Clarity (1.6…
- **Coexistence / evolution:** 旧方案在低风险、短状态或同构部署中仍成立；新机制只在约束变化使错误代价或状态漂移不可忽略时接手。
- **Books route:** 对照 `PLATFORM-EVALUATION-SYSTEM` 及相邻章节；先进入按日期排序的 writeback queue，根任务合并同 owner 后决定最终写回。
<!-- review:SF-2026-ARXIV-2607-28631:end -->

<!-- review:SF-2026-ARXIV-2607-28633:start -->
### Topology-Aware Data Movement for Disaggregated GPU Inference

- **Status / Evidence:** Experimental；exact-v1 HTML 已读取并保存校验和；Score V2=`8`。
- **Problem / old solution:** 既有路径通常把 cross-pool KV transfer 隐含在模型调用或离线平均指标中；在较小规模、单一模型或无跨请求状态时成本较低，但难以回答谁拥有失败恢复与版本一致性。
- **Changed constraint:** 论文面对的约束由摘要和全文共同限定为：Disaggregated LLM inference creates a datacenter networking problem that no existing system solves correctly. When prefill and decode run on separate GPU pools, the KV cache must be transferred between them.
- **Mechanism:** exact-v1 的方法段写明：manages the prefill-to-transfer-to-decode lifecycle. It maintains a registry of active transfers, handles retries (2 attempts with 100 ms exponential backoff), and enforces concurrency limits (default: 100 concurrent transfers). Transfers complete asynchronously: the prefill worker is freed immediately to accept the next request. performs data movement. It implements five transport modes (NVLink, NVSwitch, PCIe, RDMA, TCP) via a interface with wrappers that model real transport bandwidth.
- **State ownership:** 需要显式绑定 request/KV identity and topology metadata；canonical owner 是 `INFER-PD-DISAGGREGATION`，而不是论文应用领域本身。
- **Control / data flow:** 数据由工作负载进入机制实现，placement and transfer orchestrator 决定是否执行、路由、提交或回退；输出必须携带与输入同一版本域的证据。
- **Implementation surface:** 全文 locator=`System Architecture; papers/2026/08/_sources/arxiv-owner-replay-20260903/20260803/exact-v1-text/2607.28633v1.txt`；公开实现、硬件或训练配置只按正文披露解释，未披露字段不补写。
- **Evaluation contract:** We present analytical models grounded in published hardware specifications, validated against the component-level implementation. 该结果只绑定论文声明的数据、模型、硬件、精度、长度、batch/concurrency 与 evaluator；缺失字段均为 `Not Disclosed`。
- **Proves / does not prove:** 证据支持该受限 workload 中机制可行或暴露既有评价缺口；不证明跨模型、跨硬件、跨领域或生产 SLO 的普遍优势。
- **Trade-off / failure mode:** 新增状态、控制器和观测提高可验证性，但引入版本错配、额外延迟/内存/通信、错误路由及 evaluator bias。全文边界：Disaggregated LLM inference creates a new datacenter data movement pattern that existing systems handle suboptimally. TopKV demonstrates that topology-aware transport selection, exploiting the 72 bandwidth hierarchy in modern GPU clusters, can reduce KV cache transfer latency by 3 to 18. Co-optimizing MoE expert dispatch with KV cache placement and modeling CXL 3.0 as an overflow tier address complementary aspects of the problem. While full evaluation awaits access to multi-node GPU clusters with heterogeneous interconnects, the complete system design and analytical models grounded in published specifications provide evidence that the approach merits further investigation and hardware validation.
- **Coexistence / evolution:** 旧方案在低风险、短状态或同构部署中仍成立；新机制只在约束变化使错误代价或状态漂移不可忽略时接手。
- **Books route:** 对照 `INFER-PD-DISAGGREGATION` 及相邻章节；先进入按日期排序的 writeback queue，根任务合并同 owner 后决定最终写回。
<!-- review:SF-2026-ARXIV-2607-28633:end -->

<!-- review:SF-2026-ARXIV-2607-28636:start -->
### Chain-of-Models: Cross-Model Auditing for Bias-Robust LLM Judges

- **Status / Evidence:** Experimental；exact-v1 HTML 已读取并保存校验和；Score V2=`7`。
- **Problem / old solution:** 既有路径通常把 evaluation evidence and release decision 隐含在模型调用或离线平均指标中；在较小规模、单一模型或无跨请求状态时成本较低，但难以回答谁拥有失败恢复与版本一致性。
- **Changed constraint:** 论文面对的约束由摘要和全文共同限定为：LLMs increasingly serve as automated judges, but their judgments remain vulnerable to cognitive biases. Existing mitigations mostly rely on prompt-driven debiasing, which is brittle across bias types, or human evaluation, which does not scale.
- **Mechanism:** exact-v1 的方法段写明：Given a judgment task with instruction and input query , a single model produces a judgment . However, may be susceptible to cognitive biases embedded in the input—such as authority appeals, bandwagon effects, distraction cues, or sycophantic user-preference cues—leading to incorrect judgments. We aim to mitigate these biases without modifying any model’s weights. CoM constructs a sequential chain of models . In the step, receives the original task and produces a reasoning trace and answer :
- **State ownership:** 需要显式绑定 evaluator configuration, dataset slice and result provenance；canonical owner 是 `PLATFORM-EVALUATION-SYSTEM`，而不是论文应用领域本身。
- **Control / data flow:** 数据由工作负载进入机制实现，evaluation controller 决定是否执行、路由、提交或回退；输出必须携带与输入同一版本域的证据。
- **Implementation surface:** 全文 locator=`Framework Design; papers/2026/08/_sources/arxiv-owner-replay-20260903/20260803/exact-v1-text/2607.28636v1.txt`；公开实现、硬件或训练配置只按正文披露解释，未披露字段不补写。
- **Evaluation contract:** Our experiments isolate the contribution of and to bias correction. We construct chains with controlled variation in the auditor family and evaluate the auditor-selection results on two parallel evaluation tracks: factual multiple-choice QA (four MMLU-Pro splits) and subjective pairwise preference judging (four DPO datasets), each crossed with the four cognitive biases of Table . We select 9 models from six families representing the 2025–2026 frontier (Table ). Three families provide both a small and large variant (Qwen, GPT, DeepSeek), enabling within-family scale comparisons; three additional families (GLM, MiniMax, Kimi) contribute their flagship model, broadening the diversity of training lineages. This se… 该结果只绑定论文声明的数据、模型、硬件、精度、长度、batch/concurrency 与 evaluator；缺失字段均为 `Not Disclosed`。
- **Proves / does not prove:** 证据支持该受限 workload 中机制可行或暴露既有评价缺口；不证明跨模型、跨硬件、跨领域或生产 SLO 的普遍优势。
- **Trade-off / failure mode:** 新增状态、控制器和观测提高可验证性，但引入版本错配、额外延迟/内存/通信、错误路由及 evaluator bias。全文边界：Bias mitigation in LLM-as-judge pipelines has so far relied on hand-engineered prompts or human evaluation, neither of which scales to deployment volumes. The natural alternative is to have one LLM audit another’s reasoning, which raises a binary design question: does the auditor have to be a different model from the original judge? We find the answer is yes, and we identify two findings that overturn the natural defaults for picking such an auditor. First, the auditor with the strongest standalone bias resistance is not necessarily the auditor that produces the best chain accuracy: Kimi-K2.5 leads single-model resistance on bandwagon, authority, and distraction, yet pairing Qwen2.5-72B-Instruct with Kimi-K2.5…
- **Coexistence / evolution:** 旧方案在低风险、短状态或同构部署中仍成立；新机制只在约束变化使错误代价或状态漂移不可忽略时接手。
- **Books route:** 对照 `PLATFORM-EVALUATION-SYSTEM` 及相邻章节；先进入按日期排序的 writeback queue，根任务合并同 owner 后决定最终写回。
<!-- review:SF-2026-ARXIV-2607-28636:end -->

<!-- review:SF-2026-ARXIV-2607-28638:start -->
### Learning Stateful Predictive Knowledge From Experience

- **Status / Evidence:** Experimental；exact-v1 HTML 已读取并保存校验和；Score V2=`7`。
- **Problem / old solution:** 既有路径通常把 persistent or derived memory 隐含在模型调用或离线平均指标中；在较小规模、单一模型或无跨请求状态时成本较低，但难以回答谁拥有失败恢复与版本一致性。
- **Changed constraint:** 论文面对的约束由摘要和全文共同限定为：As large language model (LLM) agents increasingly learn from experience, they primarily rely on trajectory-level reflection to extract insights. Viewed through the lens of predictive knowledge, we argue that this approach operates on episodic hindsight rather than predictive foresight, yielding brittle, path-dependent heuristics.
- **Mechanism:** exact-v1 的方法段写明：The framework aligns with the paradigm, as our bootstrapping loop is essentially updating state knowledge using evaluative language generated at subsequent states. The central insight is that , regardless of whether it comes from external environments, self-reflection, other models, or human supervision. Within this paradigm, we here compare our methods to recent training-based methods designed to improve self-reflection capabilities. Critic-GRPO , Reflect-Retry-Reward , and L explore how evaluative behaviour evolves under reinforcement learning. These approaches construct datasets consisting of initial experiences , self-generated reflections , and refined experiences (trajectory-level) or retried experiences…
- **State ownership:** 需要显式绑定 memory provenance, version and read/write boundary；canonical owner 是 `AGENT-MEMORY`，而不是论文应用领域本身。
- **Control / data flow:** 数据由工作负载进入机制实现，agent memory manager 决定是否执行、路由、提交或回退；输出必须携带与输入同一版本域的证据。
- **Implementation surface:** 全文 locator=`Compare SKL-SD and SKL-RL to other training methods; papers/2026/08/_sources/arxiv-owner-replay-20260903/20260803/exact-v1-text/2607.28638v1.txt`；公开实现、硬件或训练配置只按正文披露解释，未披露字段不补写。
- **Evaluation contract:** We first evaluate SKL-SD on established agentic benchmarks (WebShop and ScienceWorld) to demonstrate that stateful knowledge learning can be integrated into existing training frameworks to outperform current state-of-the-art reflection training methods. Subsequently, we explore SKL-RL on ChessPuzzles, a complex reasoning task that suffers less from data contamination and requires deep look-ahead and strategic state assessments. 该结果只绑定论文声明的数据、模型、硬件、精度、长度、batch/concurrency 与 evaluator；缺失字段均为 `Not Disclosed`。
- **Proves / does not prove:** 证据支持该受限 workload 中机制可行或暴露既有评价缺口；不证明跨模型、跨硬件、跨领域或生产 SLO 的普遍优势。
- **Trade-off / failure mode:** 新增状态、控制器和观测提高可验证性，但引入版本错配、额外延迟/内存/通信、错误路由及 evaluator bias。全文边界：In this paper, we have challenged the prevailing reliance on trajectory-level reflection in LLM agent training. To address this, we introduced , a framework that centers on maintaining explicit, declarative predictive assessments anchored to specific states. Our motivating examples confirmed that stateful knowledge provides finer granularity and generalization, and also enables knowledge bootstrapping that scales SKL to increasingly complex tasks. Experiments validate how SKL training variants and can yield significant performance gains and move toward a more autonomous, self-evolving agent learning paradigm. As LLM agents transition further into the "Era of Experience," moving beyond static datasets toward co…
- **Coexistence / evolution:** 旧方案在低风险、短状态或同构部署中仍成立；新机制只在约束变化使错误代价或状态漂移不可忽略时接手。
- **Books route:** 对照 `AGENT-MEMORY` 及相邻章节；先进入按日期排序的 writeback queue，根任务合并同 owner 后决定最终写回。
<!-- review:SF-2026-ARXIV-2607-28638:end -->

<!-- review:SF-2026-ARXIV-2607-28640:start -->
### TokenSwap: Benchmarking and Reducing the Modality Gap in Multimodal LLMs

- **Status / Evidence:** Experimental；exact-v1 HTML 已读取并保存校验和；Score V2=`6`。
- **Problem / old solution:** 既有路径通常把 cross-modal evidence alignment 隐含在模型调用或离线平均指标中；在较小规模、单一模型或无跨请求状态时成本较低，但难以回答谁拥有失败恢复与版本一致性。
- **Changed constraint:** 论文面对的约束由摘要和全文共同限定为：Multimodal large language models (MLLMs) should generate consistent responses given semantically equivalent inputs across modalities. However, we observe a systematic discrepancy in model predictions under such cross-modal variations.
- **Mechanism:** exact-v1 的方法段写明：We formalize this phenomenon as the , defined as the difference in model performance when semantically equivalent content is presented in textual versus multimodal form. To systematically study this gap, we introduce TokenSwap, a general method for transforming text-only datasets into image-interleaved counterparts while preserving semantic alignment across modalities. Rather than converting entire inputs into images (e.g., rendering text as images ), TokenSwap operates at the concept level, replacing individual textual concepts with semantically aligned natural images while preserving the surrounding context and structure (Figure ).
- **State ownership:** 需要显式绑定 modality, timestamp and representation identity；canonical owner 是 `MULTIMODAL-REPRESENTATION`，而不是论文应用领域本身。
- **Control / data flow:** 数据由工作负载进入机制实现，fusion/evidence router 决定是否执行、路由、提交或回退；输出必须携带与输入同一版本域的证据。
- **Implementation surface:** 全文 locator=`full-text paragraph 3; papers/2026/08/_sources/arxiv-owner-replay-20260903/20260803/exact-v1-text/2607.28640v1.txt`；公开实现、硬件或训练配置只按正文披露解释，未披露字段不补写。
- **Evaluation contract:** Multimodal large language models (MLLMs) should generate consistent responses given semantically equivalent inputs across modalities. However, we observe a systematic discrepancy in model predictions under such cross-modal variations. Specifically, we define the modality gap as the difference in model performance under semantically equivalent textual and multimodal inputs. We introduce TokenSwap, a method that constructs such inputs by replacing textual concepts with semantically aligned images, resulting in sequences where visual tokens are interleaved with text tokens. Based on TokenSwap, we transform existing text-based benchmarks (e.g., MMLU ) into image-interleaved counterparts, resulting in . Across 42 M… 该结果只绑定论文声明的数据、模型、硬件、精度、长度、batch/concurrency 与 evaluator；缺失字段均为 `Not Disclosed`。
- **Proves / does not prove:** 证据支持该受限 workload 中机制可行或暴露既有评价缺口；不证明跨模型、跨硬件、跨领域或生产 SLO 的普遍优势。
- **Trade-off / failure mode:** 新增状态、控制器和观测提高可验证性，但引入版本错配、额外延迟/内存/通信、错误路由及 evaluator bias。全文边界：In this paper, we introduce for quantitative evaluation of modality gap and find that all models exhibit a non-trivial gap, with at least a 4% drop under image-interleaved inputs. To mitigate this, we propose TokenSwap as a training strategy that constructs image-interleaved data, effectively reducing the modality gap while preserving text performance. Our approach has several limitations. The measured gap depends on image quality, where relatively lower-quality (e.g., retrieval-based) images can introduce a bigger modality gap, although model rankings remain consistent. In addition, TokenSwap training requires in-distribution data: domain mismatch between training and evaluation (e.g., natural images vs. OCR…
- **Coexistence / evolution:** 旧方案在低风险、短状态或同构部署中仍成立；新机制只在约束变化使错误代价或状态漂移不可忽略时接手。
- **Books route:** 对照 `MULTIMODAL-REPRESENTATION` 及相邻章节；先进入按日期排序的 writeback queue，根任务合并同 owner 后决定最终写回。
<!-- review:SF-2026-ARXIV-2607-28640:end -->

<!-- review:SF-2026-ARXIV-2607-28642:start -->
### ThinkReset: Learnable Intermediate Interface Construction for Bounded-Context Long-Horizon Reasoning

- **Status / Evidence:** Experimental；exact-v1 HTML 已读取并保存校验和；Score V2=`6`。
- **Problem / old solution:** 既有路径通常把 bounded continuation state 隐含在模型调用或离线平均指标中；在较小规模、单一模型或无跨请求状态时成本较低，但难以回答谁拥有失败恢复与版本一致性。
- **Changed constraint:** 论文面对的约束由摘要和全文共同限定为：Long chain-of-thought reasoning improves performance on complex problems, but it also introduces redundancy accumulation, context overflow, and error anchoring. We argue that under bounded context windows, the core bottleneck is not trajectory compression or test-time control, but the absence of a reusable intermediate interface that can replace discarded history and support continued solving.
- **Mechanism:** exact-v1 的方法段写明：Recent work also studies stronger execution frameworks and runtime-level context management. Recursive reasoning frameworks place subtasks into isolated contexts with explicit call-return structure and can offer formal active-context savings guarantees . Halo represents a test-time controller that adjusts planning near reasoning boundaries using entropy signals rather than learning the written-back state itself . COMPASS elevates context management to the agent level through a main agent, a metacognitive planner, and a context manager . TIM/TIMRUN performs runtime KV pruning based on task relevance . Compared with these approaches, is narrower and more direct: it neither modifies the execution engine nor relie…
- **State ownership:** 需要显式绑定 context/interface commit identity；canonical owner 是 `AGENT-CONTEXT`，而不是论文应用领域本身。
- **Control / data flow:** 数据由工作负载进入机制实现，context controller 决定是否执行、路由、提交或回退；输出必须携带与输入同一版本域的证据。
- **Implementation surface:** 全文 locator=`Recursive frameworks, test-time controllers, and runtime refresh.; papers/2026/08/_sources/arxiv-owner-replay-20260903/20260803/exact-v1-text/2607.28642v1.txt`；公开实现、硬件或训练配置只按正文披露解释，未披露字段不补写。
- **Evaluation contract:** Our goal is not to compare which method shortens the reasoning trace the most. Instead, we test the following claim: under a fixed context window, the key to long-horizon reasoning is whether the model can construct a reusable intermediate interface that still supports solving after history is replaced. Accordingly, our experiments ask two questions: (1) can , as a text-space writeback-and-reset framework, improve continuation success under fixed context windows? and (2) do these gains come from rather than generic trajectory retention or test-time resets? We use Qwen3-8B, Qwen3-14B, and Qwen3-32B as base models, and train on the decontaminated DeepMath-103K dataset . The main paper reports AIME 2024, AIME 202… 该结果只绑定论文声明的数据、模型、硬件、精度、长度、batch/concurrency 与 evaluator；缺失字段均为 `Not Disclosed`。
- **Proves / does not prove:** 证据支持该受限 workload 中机制可行或暴露既有评价缺口；不证明跨模型、跨硬件、跨领域或生产 SLO 的普遍优势。
- **Trade-off / failure mode:** 新增状态、控制器和观测提高可验证性，但引入版本错配、额外延迟/内存/通信、错误路由及 evaluator bias。全文边界：Our evidence is concentrated on bounded-context long-horizon reasoning in math and logic; broader validation on scientific reasoning, program reasoning, and agentic multi-step tasks remains limited. In addition, still relies on a small amount of cold-start SFT to stabilize interface learning. Finally, the current implementation uses fixed-ratio triggering and at most two resets, so more flexible triggering and deeper interface hierarchies remain for future work.
- **Coexistence / evolution:** 旧方案在低风险、短状态或同构部署中仍成立；新机制只在约束变化使错误代价或状态漂移不可忽略时接手。
- **Books route:** 对照 `AGENT-CONTEXT` 及相邻章节；先进入按日期排序的 writeback queue，根任务合并同 owner 后决定最终写回。
<!-- review:SF-2026-ARXIV-2607-28642:end -->

<!-- review:SF-2026-ARXIV-2607-28658:start -->
### Evaluating Federated Pre-Training: On the Reliability of Downstream Fine-Tuning and Intrinsic Evaluation

- **Status / Evidence:** Experimental；exact-v1 HTML 已读取并保存校验和；Score V2=`7`。
- **Problem / old solution:** 既有路径通常把 evaluation evidence and release decision 隐含在模型调用或离线平均指标中；在较小规模、单一模型或无跨请求状态时成本较低，但难以回答谁拥有失败恢复与版本一致性。
- **Changed constraint:** 论文面对的约束由摘要和全文共同限定为：Federated pre-training offers a way to train foundation models on private or distributed data without centralizing the underlying datasets. However, evaluating federated pre-training remains challenging because differences in client participation and local data availability can make directly comparable evaluation difficult.
- **Mechanism:** exact-v1 的方法段写明：Federated learning offers a natural alternative in such settings. Instead of collecting data centrally, model training is performed across distributed clients while the underlying data remain local. This makes federated learning a promising approach for pre-training foundation models on data that would otherwise remain inaccessible to centralized training. Consequently, a crucial question arises:
- **State ownership:** 需要显式绑定 evaluator configuration, dataset slice and result provenance；canonical owner 是 `PLATFORM-EVALUATION-SYSTEM`，而不是论文应用领域本身。
- **Control / data flow:** 数据由工作负载进入机制实现，evaluation controller 决定是否执行、路由、提交或回退；输出必须携带与输入同一版本域的证据。
- **Implementation surface:** 全文 locator=`full-text paragraph 3; papers/2026/08/_sources/arxiv-owner-replay-20260903/20260803/exact-v1-text/2607.28658v1.txt`；公开实现、硬件或训练配置只按正文披露解释，未披露字段不补写。
- **Evaluation contract:** Federated pre-training offers a way to train foundation models on private or distributed data without centralizing the underlying datasets. However, evaluating federated pre-training remains challenging because differences in client participation and local data availability can make directly comparable evaluation difficult. Moreover, pre-training test perplexity is tied to the pre-training distribution, while downstream benchmarks introduce task-specific adaptation that may not faithfully reflect the test perplexity established during pre-training. In this work, we study which evaluation protocol more reliably reflects federated pre-training quality. Using a controlled set of centralized and federated-trained… 该结果只绑定论文声明的数据、模型、硬件、精度、长度、batch/concurrency 与 evaluator；缺失字段均为 `Not Disclosed`。
- **Proves / does not prove:** 证据支持该受限 workload 中机制可行或暴露既有评价缺口；不证明跨模型、跨硬件、跨领域或生产 SLO 的普遍优势。
- **Trade-off / failure mode:** 新增状态、控制器和观测提高可验证性，但引入版本错配、额外延迟/内存/通信、错误路由及 evaluator bias。全文边界：Our findings are based on controlled experiments at relatively small scale. In particular, we study a 16M parameter transformer model trained in centralized and federated settings on a small subset of ThePile. While this setup enables a controlled comparison across models, it is substantially smaller than modern foundation model pre-training regimes. We further restrict evaluation to the GLUE benchmark and to next-token prediction on the corresponding benchmark text, which covers only a limited range of downstream and intrinsic evaluation settings. In addition, our analysis measures evaluation quality by how well a protocol preserves a reference ranking induced by the after pre-training. This is a useful crite…
- **Coexistence / evolution:** 旧方案在低风险、短状态或同构部署中仍成立；新机制只在约束变化使错误代价或状态漂移不可忽略时接手。
- **Books route:** 对照 `PLATFORM-EVALUATION-SYSTEM` 及相邻章节；先进入按日期排序的 writeback queue，根任务合并同 owner 后决定最终写回。
<!-- review:SF-2026-ARXIV-2607-28658:end -->

<!-- review:SF-2026-ARXIV-2607-28666:start -->
### The Checking Problem: What must be true before AI ships in a regulated firm

- **Status / Evidence:** Experimental；exact-v1 HTML 已读取并保存校验和；Score V2=`7`。
- **Problem / old solution:** 既有路径通常把 evaluation evidence and release decision 隐含在模型调用或离线平均指标中；在较小规模、单一模型或无跨请求状态时成本较低，但难以回答谁拥有失败恢复与版本一致性。
- **Changed constraint:** 论文面对的约束由摘要和全文共同限定为：Enterprise AI programmes stall at a rate that is widely quoted and poorly explained. This paper measures the mechanism.
- **Mechanism:** exact-v1 的方法段写明：Have a free development cycle? Help support accessibility at arXiv! Our collaborators at LaTeXML maintain a , and welcome .
- **State ownership:** 需要显式绑定 evaluator configuration, dataset slice and result provenance；canonical owner 是 `PLATFORM-EVALUATION-SYSTEM`，而不是论文应用领域本身。
- **Control / data flow:** 数据由工作负载进入机制实现，evaluation controller 决定是否执行、路由、提交或回退；输出必须携带与输入同一版本域的证据。
- **Implementation surface:** 全文 locator=`full-text paragraph 3; papers/2026/08/_sources/arxiv-owner-replay-20260903/20260803/exact-v1-text/2607.28666v1.txt`；公开实现、硬件或训练配置只按正文披露解释，未披露字段不补写。
- **Evaluation contract:** Have a free development cycle? Help support accessibility at arXiv! Our collaborators at LaTeXML maintain a , and welcome . 该结果只绑定论文声明的数据、模型、硬件、精度、长度、batch/concurrency 与 evaluator；缺失字段均为 `Not Disclosed`。
- **Proves / does not prove:** 证据支持该受限 workload 中机制可行或暴露既有评价缺口；不证明跨模型、跨硬件、跨领域或生产 SLO 的普遍优势。
- **Trade-off / failure mode:** 新增状态、控制器和观测提高可验证性，但引入版本错配、额外延迟/内存/通信、错误路由及 evaluator bias。全文边界：Have a free development cycle? Help support accessibility at arXiv! Our collaborators at LaTeXML maintain a , and welcome .
- **Coexistence / evolution:** 旧方案在低风险、短状态或同构部署中仍成立；新机制只在约束变化使错误代价或状态漂移不可忽略时接手。
- **Books route:** 对照 `PLATFORM-EVALUATION-SYSTEM` 及相邻章节；先进入按日期排序的 writeback queue，根任务合并同 owner 后决定最终写回。
<!-- review:SF-2026-ARXIV-2607-28666:end -->

<!-- review:SF-2026-ARXIV-2607-28669:start -->
### LARA: Lightweight Adapters in the Residual Stream for Composable Adaptation and Alignment

- **Status / Evidence:** Experimental；exact-v1 HTML 已读取并保存校验和；Score V2=`6`。
- **Problem / old solution:** 既有路径通常把 composable adaptation 隐含在模型调用或离线平均指标中；在较小规模、单一模型或无跨请求状态时成本较低，但难以回答谁拥有失败恢复与版本一致性。
- **Changed constraint:** 论文面对的约束由摘要和全文共同限定为：We present LARA (Lightweight Additive Residual Adaptation), a method for efficient adaptation that operates in the residual stream of a frozen model rather than in its weights. Where LoRA adds an update of low rank to weight matrices, LARA reads the hidden state at a small set of layers and adds a correction of low rank back to the residual stream, leaving all base weights untouched.
- **Mechanism:** exact-v1 的方法段写明：This mechanism is not new. Adding a learned module to a frozen backbone, and specifically a module of low rank or a bottleneck on the residual path, is the family of residual adapters and side tuning . The closest recent instance is H-Res , which adds a low rank module, initialized to zero, to the residual stream of a frozen model and evaluates it on adaptation to a single task. We do not claim the residual-adapter mechanism as a contribution. Our contribution is threefold. First, we establish by comparison at equal parameters, rather than assume, that adaptation in the residual stream matches LoRA in weight space on a code fine-tuning task and on preference optimization (DPO); the closest prior work compares…
- **State ownership:** 需要显式绑定 adapter identity and activation scope；canonical owner 是 `TRAIN-LORA`，而不是论文应用领域本身。
- **Control / data flow:** 数据由工作负载进入机制实现，training and serving router 决定是否执行、路由、提交或回退；输出必须携带与输入同一版本域的证据。
- **Implementation surface:** 全文 locator=`full-text paragraph 3; papers/2026/08/_sources/arxiv-owner-replay-20260903/20260803/exact-v1-text/2607.28669v1.txt`；公开实现、硬件或训练配置只按正文披露解释，未披露字段不补写。
- **Evaluation contract:** We compare LARA against LoRA at the equal parameter budget of Section (2.39M against 2.18M trainable, LARA the larger), on the same frozen base, Qwen2.5 1.5B Instruct in 8 bits. Both methods are trained identically per task. Section establishes that adaptation in the residual stream matches adaptation in weight space on fine-tuning and preference optimization. Section examines the scaling coefficient at inference. Section shows many behaviors held resident on one frozen base and routed per token. 该结果只绑定论文声明的数据、模型、硬件、精度、长度、batch/concurrency 与 evaluator；缺失字段均为 `Not Disclosed`。
- **Proves / does not prove:** 证据支持该受限 workload 中机制可行或暴露既有评价缺口；不证明跨模型、跨硬件、跨领域或生产 SLO 的普遍优势。
- **Trade-off / failure mode:** 新增状态、控制器和观测提高可验证性，但引入版本错配、额外延迟/内存/通信、错误路由及 evaluator bias。全文边界：LARA places efficient adaptation in the residual stream of a frozen model rather than in its weights, and reaches the quality of LoRA in weight space at equal parameters on the tasks we study while adding two properties that follow from the additive form that preserves the base: a scale, applied at inference, that interpolates between base and adapted behavior, and the ability to hold many behaviors resident on one frozen model and route among them per token. The mechanism sits within an established line of work. Adding a learned module to a frozen backbone is the family of residual adapters and side tuning, and initializing the added module to zero so training begins from the base is standard practice. LARA’s…
- **Coexistence / evolution:** 旧方案在低风险、短状态或同构部署中仍成立；新机制只在约束变化使错误代价或状态漂移不可忽略时接手。
- **Books route:** 对照 `TRAIN-LORA` 及相邻章节；先进入按日期排序的 writeback queue，根任务合并同 owner 后决定最终写回。
<!-- review:SF-2026-ARXIV-2607-28669:end -->

<!-- review:SF-2026-ARXIV-2607-28670:start -->
### Hierarchical Copula-Gumbel-Top-K Routing: Two-Sided Dependence Control for Frozen Mixture-of-Experts at Fixed Per-Token Routing Laws

- **Status / Evidence:** Experimental；exact-v1 HTML 已读取并保存校验和；Score V2=`6`。
- **Problem / old solution:** 既有路径通常把 conditional expert activation 隐含在模型调用或离线平均指标中；在较小规模、单一模型或无跨请求状态时成本较低，但难以回答谁拥有失败恢复与版本一致性。
- **Changed constraint:** 论文面对的约束由摘要和全文共同限定为：A stochastic Gumbel-Top-K router defines, for every token of a mixture-of-experts (MoE) model, a routing law: a distribution over ordered expert lists and mixture weights. We ask which joint distributions over the routing choices of different tokens are reachable while every individual token's complete routing law is held exactly fixed.
- **Mechanism:** exact-v1 的方法段写明：We study a different, largely unexamined degree of freedom. Holding every token’s routing law fixed, the joint distribution over the choices of different tokens is still free: Sklar’s theorem separates marginals from dependence , and the routing choices of a frozen MoE are a collection of discrete marginals awaiting a dependence structure. This paper asks:
- **State ownership:** 需要显式绑定 token/expert routing state；canonical owner 是 `MODEL-MOE`，而不是论文应用领域本身。
- **Control / data flow:** 数据由工作负载进入机制实现，router and capacity controller 决定是否执行、路由、提交或回退；输出必须携带与输入同一版本域的证据。
- **Implementation surface:** 全文 locator=`full-text paragraph 3; papers/2026/08/_sources/arxiv-owner-replay-20260903/20260803/exact-v1-text/2607.28670v1.txt`；公开实现、硬件或训练配置只按正文披露解释，未披露字段不补写。
- **Evaluation contract:** The method leaves each token’s marginal selection distribution unchanged and acts only on the cross-token dependence of the routing noise: positive coordination raises the tendency of related tokens to make matching random selections, while negative coordination reduces the tendency of distinct groups to do so simultaneously. For the stochastic router studied here, this dependence can be introduced without altering any single token’s routing law. 该结果只绑定论文声明的数据、模型、硬件、精度、长度、batch/concurrency 与 evaluator；缺失字段均为 `Not Disclosed`。
- **Proves / does not prove:** 证据支持该受限 workload 中机制可行或暴露既有评价缺口；不证明跨模型、跨硬件、跨领域或生产 SLO 的普遍优势。
- **Trade-off / failure mode:** 新增状态、控制器和观测提高可验证性，但引入版本错配、额外延迟/内存/通信、错误路由及 evaluator bias。全文边界：is a dependence layer for stochastic routers, not a universal drop-in replacement for every MoE. It is exactly plug-compatible only with a stochastic Gumbel-Top- base router; converting a deterministic pretrained Top- router to stochastic Gumbel-Top- changes its base behavior even at zero coupling. Capacity clipping, token dropping, and expert-choice allocation act after sampling and are outside the invariance results; under a hard capacity, the burstiness signed by Proposition (i) is exactly the quantity that causes overflow, which is one motivation for the higher-level opposition dial. The proposition signs but does not quantify either variance effect, and for heterogeneous gate distributions the magnitudes…
- **Coexistence / evolution:** 旧方案在低风险、短状态或同构部署中仍成立；新机制只在约束变化使错误代价或状态漂移不可忽略时接手。
- **Books route:** 对照 `MODEL-MOE` 及相邻章节；先进入按日期排序的 writeback queue，根任务合并同 owner 后决定最终写回。
<!-- review:SF-2026-ARXIV-2607-28670:end -->

<!-- review:SF-2026-ARXIV-2607-28678:start -->
### ViSAGE: Constructing Self-Correcting Memories for Long-Form Video Understanding

- **Status / Evidence:** Experimental；exact-v1 HTML 已读取并保存校验和；Score V2=`7`。
- **Problem / old solution:** 既有路径通常把 persistent or derived memory 隐含在模型调用或离线平均指标中；在较小规模、单一模型或无跨请求状态时成本较低，但难以回答谁拥有失败恢复与版本一致性。
- **Changed constraint:** 论文面对的约束由摘要和全文共同限定为：Multimodal agents operating in long-horizon environments must build and continually update multimedia memories to support entity-consistent, temporally grounded reasoning. However, existing agentic memory approaches often discard fine-grained dentity cues under aggressive compression and segment-wise processing.
- **Mechanism:** exact-v1 的方法段写明：Rather than compressing inputs to fit fixed context windows, an alternative paradigm introduces explicit external banks or buffers. These memory-centric models adopt a streaming or chunk-based processing approach to bypass linear memory growth. For instance, MovieChat proposes a sparse memory mechanism for long-term storage. To address the lack of long-range spatiotemporal correlations and prevent catastrophic forgetting, MA-LMM and LifelongMemory utilize online memory banks and episodic buffers for active retrieval. At the architectural level, MeMViT caches previous network activations, while Flash-VStream optimizes for real-time updates with fast memory eviction for instantaneous video stream understanding.…
- **State ownership:** 需要显式绑定 memory provenance, version and read/write boundary；canonical owner 是 `AGENT-MEMORY`，而不是论文应用领域本身。
- **Control / data flow:** 数据由工作负载进入机制实现，agent memory manager 决定是否执行、路由、提交或回退；输出必须携带与输入同一版本域的证据。
- **Implementation surface:** 全文 locator=`Memory-Centric Architectures and AI Agents; papers/2026/08/_sources/arxiv-owner-replay-20260903/20260803/exact-v1-text/2607.28678v1.txt`；公开实现、硬件或训练配置只按正文披露解释，未披露字段不补写。
- **Evaluation contract:** To comprehensively analyze , we utilize three authoritative benchmarks (summarized in Table ). First, the robot split of M3-Bench focuses on general-purpose robots, featuring egocentric videos that test memory-guided reasoning such as inferring human personalities, interpersonal relationships, and object affordances. Complementing this, the web split of M3-Bench and Video-MME provide content with high information density from online platforms. These videos cover diverse topics like documentaries and movies, challenging the agent to process complex narratives and open-world knowledge relevant to practical multimodal applications. 该结果只绑定论文声明的数据、模型、硬件、精度、长度、batch/concurrency 与 evaluator；缺失字段均为 `Not Disclosed`。
- **Proves / does not prove:** 证据支持该受限 workload 中机制可行或暴露既有评价缺口；不证明跨模型、跨硬件、跨领域或生产 SLO 的普遍优势。
- **Trade-off / failure mode:** 新增状态、控制器和观测提高可验证性，但引入版本错配、额外延迟/内存/通信、错误路由及 evaluator bias。全文边界：In this paper, we argue that long-form video understanding requires a paradigm shift from strictly sequential processing to a self-correcting memory architecture. By enabling agents to retroactively align historical memory with evolving identity evidence, demonstrates that post-hoc rectification is a structural necessity for maintaining narrative coherence. Beyond accuracy, our framework establishes a new standard for epistemic safety in embodied AI: rather than prioritizing plausible fabrication, it enforces rigorous evidence verification. This transition from hazardous hallucinations to verified refusals is critical for deploying trustworthy agents in real-world environments, ensuring that future systems “kn…
- **Coexistence / evolution:** 旧方案在低风险、短状态或同构部署中仍成立；新机制只在约束变化使错误代价或状态漂移不可忽略时接手。
- **Books route:** 对照 `AGENT-MEMORY` 及相邻章节；先进入按日期排序的 writeback queue，根任务合并同 owner 后决定最终写回。
<!-- review:SF-2026-ARXIV-2607-28678:end -->

<!-- review:SF-2026-ARXIV-2607-28684:start -->
### Library Reachability in LSR-Synth: How Anti-Memorization Design Changes the Measurement of Symbolic Discovery

- **Status / Evidence:** Experimental；exact-v1 HTML 已读取并保存校验和；Score V2=`7`。
- **Problem / old solution:** 既有路径通常把 evaluation evidence and release decision 隐含在模型调用或离线平均指标中；在较小规模、单一模型或无跨请求状态时成本较低，但难以回答谁拥有失败恢复与版本一致性。
- **Changed constraint:** 论文面对的约束由摘要和全文共同限定为：Existing benchmarks for scientific equation discovery are largely composed of well-known equations available in the public domain, making it difficult to determine whether a model is discovering laws from data or merely recalling answers from its training corpus. LSR-Synth mitigates this problem by introducing novel synthetic terms into established scientific mechanisms and filtering the resulting tasks for novelty, solvabili…
- **Mechanism:** exact-v1 的方法段写明：The experiments use 129 LSR-Synth tasks from a local snapshot of LLM-SRBench, spanning four domains: population growth, physical oscillations, chemical reactions, and material relationships. Each task contains 4,000 training points, 500 in-distribution (ID) test points, and 500 out-of-distribution (OOD) test points, together with variable names, variable meanings, and a domain description . In the main experiments, a fixed seed is used to sample up to 800 points from the training set for candidate selection and parameter fitting. The two test sets are reserved exclusively for final evaluation. Ground-truth expressions are not used in prompting, candidate generation, or fitting. They are used only for post hoc…
- **State ownership:** 需要显式绑定 evaluator configuration, dataset slice and result provenance；canonical owner 是 `PLATFORM-EVALUATION-SYSTEM`，而不是论文应用领域本身。
- **Control / data flow:** 数据由工作负载进入机制实现，evaluation controller 决定是否执行、路由、提交或回退；输出必须携带与输入同一版本域的证据。
- **Implementation surface:** 全文 locator=`Experimental Methods; papers/2026/08/_sources/arxiv-owner-replay-20260903/20260803/exact-v1-text/2607.28684v1.txt`；公开实现、硬件或训练配置只按正文披露解释，未披露字段不补写。
- **Evaluation contract:** The experiments use 129 LSR-Synth tasks from a local snapshot of LLM-SRBench, spanning four domains: population growth, physical oscillations, chemical reactions, and material relationships. Each task contains 4,000 training points, 500 in-distribution (ID) test points, and 500 out-of-distribution (OOD) test points, together with variable names, variable meanings, and a domain description . In the main experiments, a fixed seed is used to sample up to 800 points from the training set for candidate selection and parameter fitting. The two test sets are reserved exclusively for final evaluation. Ground-truth expressions are not used in prompting, candidate generation, or fitting. They are used only for post hoc… 该结果只绑定论文声明的数据、模型、硬件、精度、长度、batch/concurrency 与 evaluator；缺失字段均为 `Not Disclosed`。
- **Proves / does not prove:** 证据支持该受限 workload 中机制可行或暴露既有评价缺口；不证明跨模型、跨硬件、跨领域或生产 SLO 的普遍优势。
- **Trade-off / failure mode:** 新增状态、控制器和观测提高可验证性，但引入版本错配、额外延迟/内存/通信、错误路由及 evaluator bias。全文边界：The evidence does not support a claim that language models are generally unnecessary for symbolic regression. It is limited to the current LSR-Synth snapshot, the tested vocabularies, and the prescribed search budgets. The matched knockout covers only 15 tasks and its confidence interval includes zero; the cross-backbone, GP, and selection diagnostics use historical single runs or task subsets; strict ID+OOD recovery depends on predefined extrapolation intervals; and SA depends on expression parameterization and judge rules. The unanimity rule further biases SA downward by assigning every mixed judgment to failure; it avoids optimistic manual relabeling but is not a model-independent definition of symbolic equ…
- **Coexistence / evolution:** 旧方案在低风险、短状态或同构部署中仍成立；新机制只在约束变化使错误代价或状态漂移不可忽略时接手。
- **Books route:** 对照 `PLATFORM-EVALUATION-SYSTEM` 及相邻章节；先进入按日期排序的 writeback queue，根任务合并同 owner 后决定最终写回。
<!-- review:SF-2026-ARXIV-2607-28684:end -->

<!-- review:SF-2026-ARXIV-2607-28685:start -->
### Safety, or Just Capability? A Validity Audit of Agent-Safety Benchmarks

- **Status / Evidence:** Experimental；exact-v1 HTML 已读取并保存校验和；Score V2=`7`。
- **Problem / old solution:** 既有路径通常把 evaluation evidence and release decision 隐含在模型调用或离线平均指标中；在较小规模、单一模型或无跨请求状态时成本较低，但难以回答谁拥有失败恢复与版本一致性。
- **Changed constraint:** 论文面对的约束由摘要和全文共同限定为：Agent-safety benchmarks measure different behaviors, and their scores get quoted interchangeably as an agent's safety. We treat four of them (R-Judge, InjecAgent, AgentHarm, AgentDojo) as measurements to be validated, running each under its official implementation and author-provided scorer on up to 22 models, with MMLU and GPQA measured by us under one protocol as a capability composite.
- **Mechanism:** exact-v1 的方法段写明：This paper picks up there. If a safety score is a measurement, it can fail in the ways measurements fail, so we separate (what a score measures), (whether its metric measures that target), and (whether it tracks held-out behavior). Four questions follow:
- **State ownership:** 需要显式绑定 evaluator configuration, dataset slice and result provenance；canonical owner 是 `PLATFORM-EVALUATION-SYSTEM`，而不是论文应用领域本身。
- **Control / data flow:** 数据由工作负载进入机制实现，evaluation controller 决定是否执行、路由、提交或回退；输出必须携带与输入同一版本域的证据。
- **Implementation surface:** 全文 locator=`full-text paragraph 3; papers/2026/08/_sources/arxiv-owner-replay-20260903/20260803/exact-v1-text/2607.28685v1.txt`；公开实现、硬件或训练配置只按正文披露解释，未披露字段不补写。
- **Evaluation contract:** Agent-safety benchmarks measure different behaviors, and their scores get quoted interchangeably as an agent’s safety. We treat four of them (R-Judge, InjecAgent, AgentHarm, AgentDojo) as measurements to be validated, running each under its official implementation and author-provided scorer on up to 22 models, with MMLU and GPQA measured by us under one protocol as a capability composite. The metric is the first problem. On any binary trace-judgment benchmark scored by , an “always positive” policy attains ; on R-Judge that is , above five of the 21 models that actually discriminate. The three broad-coverage benchmarks then rank the same 18 models differently, and the trade-off behind that disagreement is a sm… 该结果只绑定论文声明的数据、模型、硬件、精度、长度、batch/concurrency 与 evaluator；缺失字段均为 `Not Disclosed`。
- **Proves / does not prove:** 证据支持该受限 workload 中机制可行或暴露既有评价缺口；不证明跨模型、跨硬件、跨领域或生产 SLO 的普遍优势。
- **Trade-off / failure mode:** 新增状态、控制器和观测提高可验证性，但引入版本错配、额外延迟/内存/通信、错误路由及 evaluator bias。全文边界：A capability score is not a safety score, and no one agent-safety benchmark stands in for safety as a whole. What a score licenses you to say depends on how it was produced. Small panels are the sharpest edge: at seven models a weak relationship can look systematic, so validity needs re-checking as the model population turns over.
- **Coexistence / evolution:** 旧方案在低风险、短状态或同构部署中仍成立；新机制只在约束变化使错误代价或状态漂移不可忽略时接手。
- **Books route:** 对照 `PLATFORM-EVALUATION-SYSTEM` 及相邻章节；先进入按日期排序的 writeback queue，根任务合并同 owner 后决定最终写回。
<!-- review:SF-2026-ARXIV-2607-28685:end -->

<!-- review:SF-2026-ARXIV-2607-28692:start -->
### SciToolAgent-Evo: An Ontology-Aware Self-Evolving Agent for Open-World Scientific Tool Acquisition

- **Status / Evidence:** Experimental；exact-v1 HTML 已读取并保存校验和；Score V2=`7`。
- **Problem / old solution:** 既有路径通常把 tool acquisition or authorization 隐含在模型调用或离线平均指标中；在较小规模、单一模型或无跨请求状态时成本较低，但难以回答谁拥有失败恢复与版本一致性。
- **Changed constraint:** 论文面对的约束由摘要和全文共同限定为：Large language model (LLM) agents have been increasingly adopted in scientific research for organizing and invoking specialized computational tools. However, their reliance on predefined tool spaces with static semantics limits their applicability to open-world scientific workflows, where tool requirements, capabilities, and boundaries evolve dynamically.
- **Mechanism:** exact-v1 的方法段写明：In this section, we introduce SciToolAgent-Evo, an ontology-aware self-evolving agent for open-world scientific tool acquisition. As illustrated in Figure , SciToolAgent-Evo consists of two phases: (1) . Given a set of training tasks , the agent performs deterministic baseline sampling and temperature-based exploratory sampling, and distills reusable knowledge from contrastive trajectories. (2) . For a test task , the agent retrieves memory, formulates active tool requests, and uses a LinUCB-based bandit gate to acquire tools for executable tool-chain construction.
- **State ownership:** 需要显式绑定 tool schema, capability and return provenance；canonical owner 是 `AGENT-TOOL-CALLING`，而不是论文应用领域本身。
- **Control / data flow:** 数据由工作负载进入机制实现，tool-policy controller 决定是否执行、路由、提交或回退；输出必须携带与输入同一版本域的证据。
- **Implementation surface:** 全文 locator=`Methods; papers/2026/08/_sources/arxiv-owner-replay-20260903/20260803/exact-v1-text/2607.28692v1.txt`；公开实现、硬件或训练配置只按正文披露解释，未披露字段不补写。
- **Evaluation contract:** In recent years, the development of comprehensive tool-use benchmarks has gained increasing attention . Early benchmarks, such as APIBank and RESTBench , mainly evaluate static tool selection and invocation under explicit specifications. Subsequent benchmarks improve realism by introducing larger tool spaces and unseen-tool generalization; representative examples include Gorilla , ToolGen , and AppWorld . In the scientific domain, SciToolEval evaluates agents’ multi-step API planning and execution capabilities, while SciToolBench assesses agents’ ability to retrieve and reason with composable scientific functions. Despite their effectiveness, these benchmarks typically involve short tool chains and task descri… 该结果只绑定论文声明的数据、模型、硬件、精度、长度、batch/concurrency 与 evaluator；缺失字段均为 `Not Disclosed`。
- **Proves / does not prove:** 证据支持该受限 workload 中机制可行或暴露既有评价缺口；不证明跨模型、跨硬件、跨领域或生产 SLO 的普遍优势。
- **Trade-off / failure mode:** 新增状态、控制器和观测提高可验证性，但引入版本错配、额外延迟/内存/通信、错误路由及 evaluator bias。全文边界：In this work, we propose an ontology-aware self-evolving agent for open-world scientific tool acquisition. SciToolAgent-Evo follows a two-stage design: during accumulation, it distills reusable knowledge from contrastive trajectories; during inference, it uses active requests and a LinUCB-based bandit gate to balance tool exploration and exploitation. By leveraging an adaptive memory of skills, experiences, and an ontologized tool graph, SciToolAgent-Evo enables agents to continually expand their capabilities in open-world scientific environments. Moreover, we introduce OpenSciToolBench, a scientific tool-use benchmark with 900 tasks across four difficulty levels. Extensive experiments demonstrate that SciTool…
- **Coexistence / evolution:** 旧方案在低风险、短状态或同构部署中仍成立；新机制只在约束变化使错误代价或状态漂移不可忽略时接手。
- **Books route:** 对照 `AGENT-TOOL-CALLING` 及相邻章节；先进入按日期排序的 writeback queue，根任务合并同 owner 后决定最终写回。
<!-- review:SF-2026-ARXIV-2607-28692:end -->

<!-- review:SF-2026-ARXIV-2607-28699:start -->
### WitCert: Sound Runtime Risk Observability and Gating for KV-Cache Quantization

- **Status / Evidence:** Experimental；exact-v1 HTML 已读取并保存校验和；Score V2=`9`。
- **Problem / old solution:** 既有路径通常把 decode-state compression or translation 隐含在模型调用或离线平均指标中；在较小规模、单一模型或无跨请求状态时成本较低，但难以回答谁拥有失败恢复与版本一致性。
- **Changed constraint:** 论文面对的约束由摘要和全文共同限定为：KV-cache quantization is validated today by offline benchmark averages; a deployed system cannot tell whether compression is damaging the request it is serving right now. We give it a provably sound runtime meter -- a "DTrace for KV quantization": a per-(layer, head, step) upper bound on the total variation between exact and compressed attention.
- **Mechanism:** exact-v1 的方法段写明：The meter loop above is the design; Fig. shows where it lives in a serving engine. The rest of this section is organized as implementation (), evaluation () and analysis ().
- **State ownership:** 需要显式绑定 layer/head/token KV identity；canonical owner 是 `INFER-KV-CACHE`，而不是论文应用领域本身。
- **Control / data flow:** 数据由工作负载进入机制实现，cache manager 决定是否执行、路由、提交或回退；输出必须携带与输入同一版本域的证据。
- **Implementation surface:** 全文 locator=`Architecture; papers/2026/08/_sources/arxiv-owner-replay-20260903/20260803/exact-v1-text/2607.28699v1.txt`；公开实现、硬件或训练配置只按正文披露解释，未披露字段不补写。
- **Evaluation contract:** Unless stated otherwise: Qwen2.5-7B , Mistral-7B and Yi-1.5-6B , three domains (natural text, code, synthetic retrieval), documents, 8k context, online block-wise scaling (no whole-sequence statistics), 8-bit KV, , , , statistics at KV-head granularity (an unadorned always means ). Table reports joint KV step coverage, single run per cell, with the deterministic bound placed at . 该结果只绑定论文声明的数据、模型、硬件、精度、长度、batch/concurrency 与 evaluator；缺失字段均为 `Not Disclosed`。
- **Proves / does not prove:** 证据支持该受限 workload 中机制可行或暴露既有评价缺口；不证明跨模型、跨硬件、跨领域或生产 SLO 的普遍优势。
- **Trade-off / failure mode:** 新增状态、控制器和观测提高可验证性，但引入版本错配、额外延迟/内存/通信、错误路由及 evaluator bias。全文边界：A sound runtime meter turns KV-cache compression from an open-loop bet into an observable, gateable system quantity: any cache-preserving scheme can be measured in live serving, broken schemes are repaired at benchmark scale by meter-driven gating (fp8 restored from 22.8 to 79.7, paired difference against uncompressed), and analysis with the meter shows that what keeps aggressive schemes alive is cross-layer cancellation rather than per-step fidelity. On the certified tier, trading an explicit request-level risk budget for coverage is what turns the certificate from decoration into a tool: the sub-Gaussian certificate reduces the page-in rate of a sound deterministic bound by relative, with very weak dependenc…
- **Coexistence / evolution:** 旧方案在低风险、短状态或同构部署中仍成立；新机制只在约束变化使错误代价或状态漂移不可忽略时接手。
- **Books route:** 对照 `INFER-KV-CACHE` 及相邻章节；先进入按日期排序的 writeback queue，根任务合并同 owner 后决定最终写回。
<!-- review:SF-2026-ARXIV-2607-28699:end -->

<!-- review:SF-2026-ARXIV-2607-28707:start -->
### Demystifying Entropy-based Selection for Chain-of-Thought Compression in Large Reasoning Models

- **Status / Evidence:** Experimental；exact-v1 HTML 已读取并保存校验和；Score V2=`7`。
- **Problem / old solution:** 既有路径通常把 evaluation evidence and release decision 隐含在模型调用或离线平均指标中；在较小规模、单一模型或无跨请求状态时成本较低，但难以回答谁拥有失败恢复与版本一致性。
- **Changed constraint:** 论文面对的约束由摘要和全文共同限定为：Entropy-based pruning has been proposed as an effective method for compressing Chain-of-Thought (CoT) reasoning with negligible accuracy loss. We test the robustness of low- and high-entropy CoT step selection methods across various models and reasoning tasks, showing that entropy offers no advantage over random pruning in any evaluated setting.
- **Mechanism:** exact-v1 的方法段写明：One such strategy involves treating token- or sentence-entropy as a proxy for relevance, pruning large fractions of a trace based on entropy value alone with little to no accuracy drop. Opposite claims coexist in the literature, favoring either the pruning or the retention of low-entropy items.
- **State ownership:** 需要显式绑定 evaluator configuration, dataset slice and result provenance；canonical owner 是 `PLATFORM-EVALUATION-SYSTEM`，而不是论文应用领域本身。
- **Control / data flow:** 数据由工作负载进入机制实现，evaluation controller 决定是否执行、路由、提交或回退；输出必须携带与输入同一版本域的证据。
- **Implementation surface:** 全文 locator=`full-text paragraph 3; papers/2026/08/_sources/arxiv-owner-replay-20260903/20260803/exact-v1-text/2607.28707v1.txt`；公开实现、硬件或训练配置只按正文披露解释，未披露字段不补写。
- **Evaluation contract:** Each trace is bounded by the performance, a theoretical upper bound on achievable accuracy. This is compared against the accuracy obtained under and , for every selector and retention rate . We report the (RPR), i.e. the ratio of a certain setting’s accuracy to the as a general measure of compression effectiveness, using exact match with ground-truth answer. To summarize a selector’s behavior across the full RPR range, we additionally report the RPR (AUC) as a function of retention rate . We use to quantify a selector ’s advantage relative to the random baseline. 该结果只绑定论文声明的数据、模型、硬件、精度、长度、batch/concurrency 与 evaluator；缺失字段均为 `Not Disclosed`。
- **Proves / does not prove:** 证据支持该受限 workload 中机制可行或暴露既有评价缺口；不证明跨模型、跨硬件、跨领域或生产 SLO 的普遍优势。
- **Trade-off / failure mode:** 新增状态、控制器和观测提高可验证性，但引入版本错配、额外延迟/内存/通信、错误路由及 evaluator bias。全文边界：In this work, we revisit the widespread assumption that token- or sentence-level entropy are associated to the semantic content of a reasoning trace and therefore can be used as a signal to prune a trace without accuracy drops. We test entropy-based selection against a random baseline across six models (spanning three families and two parameter scales) on both mathematical and non-mathematical reasoning tasks. At sentence-level, the assumption fails consistently: pruning dominates both and selection across every model, scale and domain we tested, with no strategy reliably outperforming chance. At token-level, an apparent advantage for selection emerges on mathematical benchmarks only; we show this is not an en…
- **Coexistence / evolution:** 旧方案在低风险、短状态或同构部署中仍成立；新机制只在约束变化使错误代价或状态漂移不可忽略时接手。
- **Books route:** 对照 `PLATFORM-EVALUATION-SYSTEM` 及相邻章节；先进入按日期排序的 writeback queue，根任务合并同 owner 后决定最终写回。
<!-- review:SF-2026-ARXIV-2607-28707:end -->

<!-- review:SF-2026-ARXIV-2607-28737:start -->
### Mirror Learning

- **Status / Evidence:** Experimental；exact-v1 HTML 已读取并保存校验和；Score V2=`6`。
- **Problem / old solution:** 既有路径通常把 closed-loop physical action 隐含在模型调用或离线平均指标中；在较小规模、单一模型或无跨请求状态时成本较低，但难以回答谁拥有失败恢复与版本一致性。
- **Changed constraint:** 论文面对的约束由摘要和全文共同限定为：We investigate imitation learning through the lens of third-person observation and propose a framework for mirror learning: acquiring actionable policies from passive observation. While behavior cloning (BC) excels under dense, well-aligned first-person data, it fundamentally fails to leverage the rich observational signals arising from third-person demonstrations that humans and animals routinely exploit.
- **Mechanism:** exact-v1 的方法段写明：The first part of mirror learning requires converting observations of a demonstrator agent into perceptual data in the learner’s own observation space – putting the learner “in the shoes” of the demonstrator. The second part requires synthesizing actions corresponding to the demonstrator’s observed behavior. If the combination of the perceptual observation sequence and corresponding inferred action sequence is sufficiently noise-free, they can be used by a learner to behavior clone demonstrators. While there are many possible approaches to solving this problem, we specifically restrict ourselves to those that require minimal external supervision and leverage pre-trained artifacts. A subproblem of this is to wh…
- **State ownership:** 需要显式绑定 sensor/action/trajectory state；canonical owner 是 `MULTIMODAL-EMBODIED-VLA`，而不是论文应用领域本身。
- **Control / data flow:** 数据由工作负载进入机制实现，policy plus safety controller 决定是否执行、路由、提交或回退；输出必须携带与输入同一版本域的证据。
- **Implementation surface:** 全文 locator=`Methods; papers/2026/08/_sources/arxiv-owner-replay-20260903/20260803/exact-v1-text/2607.28737v1.txt`；公开实现、硬件或训练配置只按正文披露解释，未披露字段不补写。
- **Evaluation contract:** In this section we present our findings and provide answers to three main questions: Does a pretrained video diffusion model possess a sufficiently rich set of features to enable mirror learning? 该结果只绑定论文声明的数据、模型、硬件、精度、长度、batch/concurrency 与 evaluator；缺失字段均为 `Not Disclosed`。
- **Proves / does not prove:** 证据支持该受限 workload 中机制可行或暴露既有评价缺口；不证明跨模型、跨硬件、跨领域或生产 SLO 的普遍优势。
- **Trade-off / failure mode:** 新增状态、控制器和观测提高可验证性，但引入版本错配、额外延迟/内存/通信、错误路由及 evaluator bias。全文边界：Our central empirical finding is that pretrained video diffusion models can possess sufficiently rich internal representations of physical scene structure to support mirror video synthesis after lightweight fine-tuning — without requiring explicit camera parameters, pose estimation, or scene reconstruction. We demonstrated this capacity across two visually and structurally diverse domains (CARLA autonomous driving and open-world multiplayer Minecraft), and showed zero-shot generalization from synthetic training data to real-world robotaxi footage. For the autonomous vehicle setting, where full mirror learning evaluation was tractable, we showed that (i) an effective driving policy can be learned using mirror d…
- **Coexistence / evolution:** 旧方案在低风险、短状态或同构部署中仍成立；新机制只在约束变化使错误代价或状态漂移不可忽略时接手。
- **Books route:** 对照 `MULTIMODAL-EMBODIED-VLA` 及相邻章节；先进入按日期排序的 writeback queue，根任务合并同 owner 后决定最终写回。
<!-- review:SF-2026-ARXIV-2607-28737:end -->

<!-- review:SF-2026-ARXIV-2607-28777:start -->
### Self-Supervised Skill Optimization

- **Status / Evidence:** Experimental；exact-v1 HTML 已读取并保存校验和；Score V2=`8`。
- **Problem / old solution:** 既有路径通常把 persistent agent runtime 隐含在模型调用或离线平均指标中；在较小规模、单一模型或无跨请求状态时成本较低，但难以回答谁拥有失败恢复与版本一致性。
- **Changed constraint:** 论文面对的约束由摘要和全文共同限定为：Agent skills provide frozen large language model (LLM) agents with reusable procedural guidance, and recent work shows that such skills can be optimized with ground-truth (GT) feedback. Many applications, however, lack GT labels, task scores, rewards, or reliable task-specific evaluators.
- **Mechanism:** exact-v1 的方法段写明：Recent work constructs and refines skills from execution trajectories, failures, and domain resources . SkillOpt directly treats a single skill document as the trainable state of a frozen agent. It converts scored rollouts into bounded edits and accepts an update only when it improves performance on a separate validation set. Its results show that reusable skills can be optimized across models, benchmarks, and execution harnesses. However, both its update directions and acceptance decisions rely on ground-truth (GT) feedback from task scores or task-specific evaluators.
- **State ownership:** 需要显式绑定 agent/version/session state；canonical owner 是 `AGENT-PLATFORM`，而不是论文应用领域本身。
- **Control / data flow:** 数据由工作负载进入机制实现，agent control plane 决定是否执行、路由、提交或回退；输出必须携带与输入同一版本域的证据。
- **Implementation surface:** 全文 locator=`full-text paragraph 3; papers/2026/08/_sources/arxiv-owner-replay-20260903/20260803/exact-v1-text/2607.28777v1.txt`；公开实现、硬件或训练配置只按正文披露解释，未披露字段不补写。
- **Evaluation contract:** We evaluate SSO on six closed-ended benchmarks and three open-ended multi-turn dialogue tasks. The closed-ended suite covers retrieval QA with SearchQA , spreadsheet artifact manipulation with SpreadsheetBench , grounded enterprise QA with OfficeQA , multimodal document understanding with DocVQA , advanced multiple-choice mathematics with LiveMathematicianBench , and embodied household decision making with ALFWorld . For open-ended evaluation, we use three tasks from MT-Bench-101 : Context Memory (CM), Content Rephrasing (CR), and Proactive Interaction (PI). They respectively measure the model’s perceptivity, adaptability, and interactivity. Additional dataset details are provided in the supplementary material. 该结果只绑定论文声明的数据、模型、硬件、精度、长度、batch/concurrency 与 evaluator；缺失字段均为 `Not Disclosed`。
- **Proves / does not prove:** 证据支持该受限 workload 中机制可行或暴露既有评价缺口；不证明跨模型、跨硬件、跨领域或生产 SLO 的普遍优势。
- **Trade-off / failure mode:** 新增状态、控制器和观测提高可验证性，但引入版本错配、额外延迟/内存/通信、错误路由及 evaluator bias。全文边界：We formalized GT-free skill optimization and introduced Self-Supervised Skill Optimization (SSO), a comparative framework for learning a reusable skill from unlabeled task instances. SSO compares executions from complete skill probes with corresponding current-skill executions, extracts behavioral differences without seeing the judge’s decisions, and aggregates evidence for and against equivalent behaviors. It renders a new complete skill from the highest-ranked behaviors and accepts it only when it wins on a validation set. Across multiple target models, SSO outperforms GT-free prompt optimizers on closed-ended and open-ended tasks, while approaching and sometimes exceeding the strongest GT-based skill optimi…
- **Coexistence / evolution:** 旧方案在低风险、短状态或同构部署中仍成立；新机制只在约束变化使错误代价或状态漂移不可忽略时接手。
- **Books route:** 对照 `AGENT-PLATFORM` 及相邻章节；先进入按日期排序的 writeback queue，根任务合并同 owner 后决定最终写回。
<!-- review:SF-2026-ARXIV-2607-28777:end -->

<!-- review:SF-2026-ARXIV-2607-28788:start -->
### EarlyDx: An Admission-Anchored Benchmark for Open-Ended Generation of Evidence-Supported ED-Encounter Diagnoses

- **Status / Evidence:** Experimental；exact-v1 HTML 已读取并保存校验和；Score V2=`7`。
- **Problem / old solution:** 既有路径通常把 evaluation evidence and release decision 隐含在模型调用或离线平均指标中；在较小规模、单一模型或无跨请求状态时成本较低，但难以回答谁拥有失败恢复与版本一致性。
- **Changed constraint:** 论文面对的约束由摘要和全文共同限定为：Clinical diagnosis at hospital admission must be made rapidly from limited, incomplete evidence. Existing diagnosis-prediction benchmarks are poorly suited to this setting: they restrict prediction to closed code sets, exclude free-text notes, and supervise with discharge diagnoses that incorporate the full inpatient course.
- **Mechanism:** exact-v1 的方法段写明：Large language models (LLMs) have shown strong capabilities across diverse medical tasks and are natural candidates for this synthesis-under-uncertainty problem. However, existing benchmarks for early diagnosis are designed for non-LLM, closed-set classifiers and suffer from three limitations that make them ill-suited for evaluating modern LLMs. diagnoses are mapped to a fixed ICD code set, discarding clinical nuance and information lost during text-to-code conversion , as shown in Figure . rich free-text signals such as chief complaints, radiology findings, and prior history are excluded in favor of tabular features. models receive early, admission-time inputs but are supervised with diagnoses that are coded…
- **State ownership:** 需要显式绑定 evaluator configuration, dataset slice and result provenance；canonical owner 是 `PLATFORM-EVALUATION-SYSTEM`，而不是论文应用领域本身。
- **Control / data flow:** 数据由工作负载进入机制实现，evaluation controller 决定是否执行、路由、提交或回退；输出必须携带与输入同一版本域的证据。
- **Implementation surface:** 全文 locator=`full-text paragraph 3; papers/2026/08/_sources/arxiv-owner-replay-20260903/20260803/exact-v1-text/2607.28788v1.txt`；公开实现、硬件或训练配置只按正文披露解释，未披露字段不补写。
- **Evaluation contract:** Clinical diagnosis at hospital admission must be made rapidly from limited, incomplete evidence. Existing diagnosis-prediction benchmarks are poorly suited to this setting: they restrict prediction to closed code sets, exclude free-text notes, and supervise with discharge diagnoses that incorporate the full inpatient course. We introduce , a large-scale benchmark for early diagnosis, built from emergency department encounters in MIMIC-IV. Each encounter is restricted to records available at admission time and supervised by the diagnoses recorded during the ED encounter rather than at discharge. An LLM auditor further verifies every free-text label as , , or by that evidence; the primary evaluation scores only… 该结果只绑定论文声明的数据、模型、硬件、精度、长度、batch/concurrency 与 evaluator；缺失字段均为 `Not Disclosed`。
- **Proves / does not prove:** 证据支持该受限 workload 中机制可行或暴露既有评价缺口；不证明跨模型、跨硬件、跨领域或生产 SLO 的普遍优势。
- **Trade-off / failure mode:** 新增状态、控制器和观测提高可验证性，但引入版本错配、额外延迟/内存/通信、错误路由及 evaluator bias。全文边界：We introduced EarlyDx, a large-scale benchmark for open-ended early diagnosis built from MIMIC-IV admissions, in which every label is verified against the evidence actually available at admission and scoring uses an open-weight, version-pinned semantic judge. The central finding is negative but useful: zero-shot models mostly extract diagnoses the record already names, and collapse when one has to be inferred. Post-training narrows that gap without closing it, and on time-critical conditions no system reaches a clinician’s balance of sensitivity and precision. Two features of the evaluation limit what these results can show. The reference lists only the diagnoses finally coded, so a differential a clinician ri…
- **Coexistence / evolution:** 旧方案在低风险、短状态或同构部署中仍成立；新机制只在约束变化使错误代价或状态漂移不可忽略时接手。
- **Books route:** 对照 `PLATFORM-EVALUATION-SYSTEM` 及相邻章节；先进入按日期排序的 writeback queue，根任务合并同 owner 后决定最终写回。
<!-- review:SF-2026-ARXIV-2607-28788:end -->

<!-- review:SF-2026-ARXIV-2607-28801:start -->
### Benchmarks Are Not Monolithic: Sample-Level Auditing and Orchestration for LLM Evaluation

- **Status / Evidence:** Experimental；exact-v1 HTML 已读取并保存校验和；Score V2=`7`。
- **Problem / old solution:** 既有路径通常把 evaluation evidence and release decision 隐含在模型调用或离线平均指标中；在较小规模、单一模型或无跨请求状态时成本较低，但难以回答谁拥有失败恢复与版本一致性。
- **Changed constraint:** 论文面对的约束由摘要和全文共同限定为：Benchmark datasets are central to evaluating Large Language Models (LLMs), yet they are typically conceived as monolithic tasks, obscuring substantial variation in the demands of individual samples. We introduce a dataset-centric meta-evaluation framework that audits benchmark datasets at the sample level along five latent dimensions: 1.
- **Mechanism:** exact-v1 的方法段写明：To audit benchmarks at the sample level, we introduce a (Table ), organized hierarchically into , , and . Dimensions capture broad perspectives (e.g. Cognitive and Knowledge Demands or Task Properties), Aspects group related concerns within a Dimension, and Indicators are concrete, measurable attributes (e.g. Reasoning Depth or Distractor Quality) with explicit ordinal or categorical scales. This structure decomposes complex benchmark properties into observable units with standardized definitions. Each ordinal indicator is defined with explicit level semantics (e.g. 0–3) to ensure consistent interpretation across annotators and evaluator models; detailed scale definitions are provided in Appendix . While some…
- **State ownership:** 需要显式绑定 evaluator configuration, dataset slice and result provenance；canonical owner 是 `PLATFORM-EVALUATION-SYSTEM`，而不是论文应用领域本身。
- **Control / data flow:** 数据由工作负载进入机制实现，evaluation controller 决定是否执行、路由、提交或回退；输出必须携带与输入同一版本域的证据。
- **Implementation surface:** 全文 locator=`Methodology; papers/2026/08/_sources/arxiv-owner-replay-20260903/20260803/exact-v1-text/2607.28801v1.txt`；公开实现、硬件或训练配置只按正文披露解释，未披露字段不补写。
- **Evaluation contract:** Benchmark datasets are central to evaluating Large Language Models (LLMs), yet they are typically conceived as monolithic tasks, obscuring substantial variation in the demands of individual samples. We introduce a dataset-centric meta-evaluation framework that audits benchmark datasets at the sample level along five latent dimensions: 1. Cognitive and Knowledge Demands, 2. Language and Content Quality, 3. Task Properties, 4. Context, and 5. Ethics, Safety, and Fairness. Applying this framework, we annotate five influential benchmarks – MMLU, ARC, WinoGrande, HellaSwag, and TruthfulQA – revealing pronounced internal heterogeneity that is not captured by aggregate accuracy scores. We show how these annotations e… 该结果只绑定论文声明的数据、模型、硬件、精度、长度、batch/concurrency 与 evaluator；缺失字段均为 `Not Disclosed`。
- **Proves / does not prove:** 证据支持该受限 workload 中机制可行或暴露既有评价缺口；不证明跨模型、跨硬件、跨领域或生产 SLO 的普遍优势。
- **Trade-off / failure mode:** 新增状态、控制器和观测提高可验证性，但引入版本错配、额外延迟/内存/通信、错误路由及 evaluator bias。全文边界：The Indicator counts and distributions reveal pronounced differences in the internal makeup of the benchmarks considered in this study. By decomposing these datasets along our proposed five Dimensions, we can interpret model performance through the specific cognitive, linguistic, and ethical demands of the samples.
- **Coexistence / evolution:** 旧方案在低风险、短状态或同构部署中仍成立；新机制只在约束变化使错误代价或状态漂移不可忽略时接手。
- **Books route:** 对照 `PLATFORM-EVALUATION-SYSTEM` 及相邻章节；先进入按日期排序的 writeback queue，根任务合并同 owner 后决定最终写回。
<!-- review:SF-2026-ARXIV-2607-28801:end -->

<!-- review:SF-2026-ARXIV-2607-28802:start -->
### Model or Harness? An Interaction-Centric Taxonomy for Localizing Agent Failures

- **Status / Evidence:** Experimental；exact-v1 HTML 已读取并保存校验和；Score V2=`7`。
- **Problem / old solution:** 既有路径通常把 evaluation evidence and release decision 隐含在模型调用或离线平均指标中；在较小规模、单一模型或无跨请求状态时成本较低，但难以回答谁拥有失败恢复与版本一致性。
- **Changed constraint:** 论文面对的约束由摘要和全文共同限定为：Existing evaluations often reduce agent failures to system-level outcomes, obscuring where the fault originated and which intervention would improve the agent system. This creates a repair-assignment problem: the same visible failure may call for model post-training, harness engineering, environment redesign, or benchmark repair depending on its source.
- **Mechanism:** exact-v1 的方法段写明：We developed the taxonomy iteratively while reviewing failures from public benchmarks, model system cards, published reports, and logged agent trajectories. As new cases exposed overlaps or unclear boundaries, we refined the component definitions and failure modes. Once these definitions had stabilized, we froze the taxonomy and used that version for all reported labels and for the validation in §. The final definitions are reproduced verbatim in Appendix . To assign labels consistently, we applied the root-cause principle of §. For each example, we reviewed all available evidence in the trace or report and identified the observed system-level failure. We then traced the causal chain backward and selected the…
- **State ownership:** 需要显式绑定 evaluator configuration, dataset slice and result provenance；canonical owner 是 `PLATFORM-EVALUATION-SYSTEM`，而不是论文应用领域本身。
- **Control / data flow:** 数据由工作负载进入机制实现，evaluation controller 决定是否执行、路由、提交或回退；输出必须携带与输入同一版本域的证据。
- **Implementation surface:** 全文 locator=`Categorization Methodology; papers/2026/08/_sources/arxiv-owner-replay-20260903/20260803/exact-v1-text/2607.28802v1.txt`；公开实现、硬件或训练配置只按正文披露解释，未披露字段不补写。
- **Evaluation contract:** We compare each judge’s predictions with the human-assigned labels using exact-match accuracy, macro-averaged F, and Cohen’s . Category-level evaluation requires the correct interaction edge and fault side. Failure-mode evaluation additionally requires the correct named failure mode. 该结果只绑定论文声明的数据、模型、硬件、精度、长度、batch/concurrency 与 evaluator；缺失字段均为 `Not Disclosed`。
- **Proves / does not prove:** 证据支持该受限 workload 中机制可行或暴露既有评价缺口；不证明跨模型、跨硬件、跨领域或生产 SLO 的普遍优势。
- **Trade-off / failure mode:** 新增状态、控制器和观测提高可验证性，但引入版本错配、额外延迟/内存/通信、错误路由及 evaluator bias。全文边界：The proposed taxonomy shows why fault localization matters in practice: the same observed failure may require a different intervention depending on the fault side. Model-side failures identify targets for post-training, harness-side failures point to changes in the agent scaffolding, and faults in the environment or evaluation setup require interventions outside the model. It also reveals how responsibility is distributed across the system. As shown in Figure , most failure modes are assigned to the model side. This imbalance partly reflects our attribution rule: a failure is model-side when a more capable model could have prevented it or recovered from it. The remaining non-model failures identify cases that…
- **Coexistence / evolution:** 旧方案在低风险、短状态或同构部署中仍成立；新机制只在约束变化使错误代价或状态漂移不可忽略时接手。
- **Books route:** 对照 `PLATFORM-EVALUATION-SYSTEM` 及相邻章节；先进入按日期排序的 writeback queue，根任务合并同 owner 后决定最终写回。
<!-- review:SF-2026-ARXIV-2607-28802:end -->

<!-- review:SF-2026-ARXIV-2607-28815:start -->
### Preventing Premature Commitment in Coding Agents with an Evidence-Conditioned Execution Layer

- **Status / Evidence:** Experimental；exact-v1 HTML 已读取并保存校验和；Score V2=`6`。
- **Problem / old solution:** 既有路径通常把 durable multi-step execution 隐含在模型调用或离线平均指标中；在较小规模、单一模型或无跨请求状态时成本较低，但难以回答谁拥有失败恢复与版本一致性。
- **Changed constraint:** 论文面对的约束由摘要和全文共同限定为：LLM-based coding agents often edit source code or submit patches before examining enough repository evidence to justify the change, a failure pattern we call premature commitment. We present ECLoop, an execution layer that interposes between the agent and the repository to enforce evidence-conditioned execution.
- **Mechanism:** exact-v1 的方法段写明：Coding agents may edit code or submit a patch before examining enough repository evidence to support that action. An edit may appear plausible after inspecting the target function, even though an unseen caller, related implementation, test, or behavioral constraint would change that judgment. Likewise, a patch may appear ready for submission after one test passes while other relevant behavior remains unexamined. Thus, beyond generating a plausible repair , an agent must determine whether it has observed enough evidence for the proposed action to proceed. We call executing an edit or submission before the relevant evidence has been examined a .
- **State ownership:** 需要显式绑定 task, evidence and checkpoint state；canonical owner 是 `AGENT-WORKFLOW`，而不是论文应用领域本身。
- **Control / data flow:** 数据由工作负载进入机制实现，workflow engine 决定是否执行、路由、提交或回退；输出必须携带与输入同一版本域的证据。
- **Implementation surface:** 全文 locator=`full-text paragraph 3; papers/2026/08/_sources/arxiv-owner-replay-20260903/20260803/exact-v1-text/2607.28815v1.txt`；公开实现、硬件或训练配置只按正文披露解释，未披露字段不补写。
- **Evaluation contract:** We evaluate whether improves repository-level issue resolution across large language models and agent scaffolds, how much execution overhead and token cost it adds, and how much each component contributes. 该结果只绑定论文声明的数据、模型、硬件、精度、长度、batch/concurrency 与 evaluator；缺失字段均为 `Not Disclosed`。
- **Proves / does not prove:** 证据支持该受限 workload 中机制可行或暴露既有评价缺口；不证明跨模型、跨硬件、跨领域或生产 SLO 的普遍优势。
- **Trade-off / failure mode:** 新增状态、控制器和观测提高可验证性，但引入版本错配、额外延迟/内存/通信、错误路由及 evaluator bias。全文边界：We presented , an evidence-conditioned execution layer that addresses premature commitment in coding agents by tracking task-specific evidence and gating commitment actions whose supporting conditions remain unsatisfied. On SWE-bench Verified, improves Pass@1 by 4.8–11.8 percentage points across two models and two scaffolds while reducing token usage by up to 12.1%, without modifying the underlying agent. The results demonstrate that controlling an agent may commit is an effective and lightweight complement to improving it chooses to do.
- **Coexistence / evolution:** 旧方案在低风险、短状态或同构部署中仍成立；新机制只在约束变化使错误代价或状态漂移不可忽略时接手。
- **Books route:** 对照 `AGENT-WORKFLOW` 及相邻章节；先进入按日期排序的 writeback queue，根任务合并同 owner 后决定最终写回。
<!-- review:SF-2026-ARXIV-2607-28815:end -->

<!-- review:SF-2026-ARXIV-2607-28818:start -->
### Best Friends, Not Forever: Evaluating Long-Horizon Persona Collapse and Behavioral Drift in AI Companions

- **Status / Evidence:** Experimental；exact-v1 HTML 已读取并保存校验和；Score V2=`7`。
- **Problem / old solution:** 既有路径通常把 evaluation evidence and release decision 隐含在模型调用或离线平均指标中；在较小规模、单一模型或无跨请求状态时成本较低，但难以回答谁拥有失败恢复与版本一致性。
- **Changed constraint:** 论文面对的约束由摘要和全文共同限定为：As AI companions increasingly mediate repeated social interaction, users may rely on a stable role and shared history, yet locally acceptable replies do not ensure that either persists. We study two observable long-horizon failures: 'persona collapse', the loss of a deployed role, boundaries, values, or style, and 'behavioral drift', the gradual or recurrent erosion of those properties.
- **Mechanism:** exact-v1 的方法段写明：A companion’s user-facing surface is a : a structured representation used to condition the model toward particular traits, identities, and behavioral tendencies . We call the disclosed and legitimately revisable expectation that these properties remain recognizable . This does not imply that the model has a human identity. An observable loss of its specified name or role, values, boundaries, or style is ; slower, recurrent, or accumulating erosion is . The most common pipelines for this usecase is defined relative to the effective persona card, including valid updates. Adaptation requested by the user is considered a success, while rigidly preserving superseded state can itself violate the requirements of a go…
- **State ownership:** 需要显式绑定 evaluator configuration, dataset slice and result provenance；canonical owner 是 `PLATFORM-EVALUATION-SYSTEM`，而不是论文应用领域本身。
- **Control / data flow:** 数据由工作负载进入机制实现，evaluation controller 决定是否执行、路由、提交或回退；输出必须携带与输入同一版本域的证据。
- **Implementation surface:** 全文 locator=`full-text paragraph 3; papers/2026/08/_sources/arxiv-owner-replay-20260903/20260803/exact-v1-text/2607.28818v1.txt`；公开实现、硬件或训练配置只按正文披露解释，未披露字段不补写。
- **Evaluation contract:** The study contains several nested units: turns within sessions, sessions within conversations, and questions within banks. We do not treat the 929,841 archived primary-judge turn records as independent samples. Questionnaire tables aggregate at the conversation level. Schedule and sequential rates are descriptive summaries of primary-judge labels, with model and schedule comparisons bounded to the study corpus. Trajectory tables report both question counts and bank coverage; the 35 banks, rather than repeated answers to the same questions, are the broadest independent sampling units available for that probe. This distinction also limits the role of significance testing. Extremely small turn-level -values would… 该结果只绑定论文声明的数据、模型、硬件、精度、长度、batch/concurrency 与 evaluator；缺失字段均为 `Not Disclosed`。
- **Proves / does not prove:** 证据支持该受限 workload 中机制可行或暴露既有评价缺口；不证明跨模型、跨硬件、跨领域或生产 SLO 的普遍优势。
- **Trade-off / failure mode:** 新增状态、控制器和观测提高可验证性，但引入版本错配、额外延迟/内存/通信、错误路由及 evaluator bias。全文边界：evaluates persona-conditioned behavior and trajectory recall over long synthetic conversations. It does not directly observe a latent identity, but it shows that deployed persona properties can deviate, recur, and persist while trajectory recall fails along different dimensions. These patterns are themselves sensitive to evaluator and context design. The appropriate conclusion is not that one model or memory architecture solves companion continuity, but that long-horizon audits should distinguish isolated slips, behavioral drift, persistent collapse signatures, recall family, judge provenance, and scoring substrate. can surface evidence relevant to continuity claims; deciding whether a companion warrants trust…
- **Coexistence / evolution:** 旧方案在低风险、短状态或同构部署中仍成立；新机制只在约束变化使错误代价或状态漂移不可忽略时接手。
- **Books route:** 对照 `PLATFORM-EVALUATION-SYSTEM` 及相邻章节；先进入按日期排序的 writeback queue，根任务合并同 owner 后决定最终写回。
<!-- review:SF-2026-ARXIV-2607-28818:end -->

<!-- review:SF-2026-ARXIV-2607-28824:start -->
### Characterizing LLM Kernel Access and Memory Interaction in Multi-Partition NUMA GPUs

- **Status / Evidence:** Experimental；exact-v1 HTML 已读取并保存校验和；Score V2=`8`。
- **Problem / old solution:** 既有路径通常把 device-memory locality 隐含在模型调用或离线平均指标中；在较小规模、单一模型或无跨请求状态时成本较低，但难以回答谁拥有失败恢复与版本一致性。
- **Changed constraint:** 论文面对的约束由摘要和全文共同限定为：Large language model (LLM) workloads motivate multi-partition GPUs as a path to scaling compute and memory capacity, but their non-uniform memory access characteristics and inter-partition communication can amplify contention and degrade locality, leading to suboptimal kernel latency. To address this, we analyze performance-critical LLM kernel implementations spanning weight projection, mixture-of-experts, and attention varia…
- **Mechanism:** exact-v1 的方法段写明：Our method starts from generating memory traces in the virtual address space from real GPU kernels. From these memory traces, we use our analysis logic to diagnose workgroup-level access patterns. We then quantify the performance impact of these patterns using cycle-level simulation, whose configuration we describe alongside the case-by-case results in Section . We conduct our analysis at the granularity of individual workgroups (equivalently, Threadblocks in NVIDIA terminology) because the workgroup is the fundamental unit of scheduling across Compute Units (CUs) in the AMD GPU execution model. In a multi-partition GPU such as the AMD Instinct MI300X, the hardware scheduler distributes workgroups across XCDs,…
- **State ownership:** 需要显式绑定 allocation and access-topology state；canonical owner 是 `INFER-GPU-MEMORY`，而不是论文应用领域本身。
- **Control / data flow:** 数据由工作负载进入机制实现，runtime memory manager 决定是否执行、路由、提交或回退；输出必须携带与输入同一版本域的证据。
- **Implementation surface:** 全文 locator=`Methodology; papers/2026/08/_sources/arxiv-owner-replay-20260903/20260803/exact-v1-text/2607.28824v1.txt`；公开实现、硬件或训练配置只按正文披露解释，未披露字段不补写。
- **Evaluation contract:** This section describes the memory trace analysis pipeline that extracts inter-workgroup sharing behavior from raw GPU execution traces. 该结果只绑定论文声明的数据、模型、硬件、精度、长度、batch/concurrency 与 evaluator；缺失字段均为 `Not Disclosed`。
- **Proves / does not prove:** 证据支持该受限 workload 中机制可行或暴露既有评价缺口；不证明跨模型、跨硬件、跨领域或生产 SLO 的普遍优势。
- **Trade-off / failure mode:** 新增状态、控制器和观测提高可验证性，但引入版本错配、额外延迟/内存/通信、错误路由及 evaluator bias。全文边界：Table consolidates the sharing patterns, per-workgroup footprints, achievable speedups, and required placement optimizations identified across the analyzed LLM kernels. Throughout different case studies on LLM kernels on multi-partition GPU, we identified memory trace-based WG-level data access patterns and derived achievable Partition Locality under optimal workgroup/data placement. With a cycle-level simulator, we derived the achievable kernel speedup by optimizing inter-partition data access. Returning to our motivating question, the cost of NUMA in LLM serving kernels ranges from negligible (1.09 for compute-bound FA prefill) to substantial (1.79 for GQA decode), and the required mitigation ranges from sim…
- **Coexistence / evolution:** 旧方案在低风险、短状态或同构部署中仍成立；新机制只在约束变化使错误代价或状态漂移不可忽略时接手。
- **Books route:** 对照 `INFER-GPU-MEMORY` 及相邻章节；先进入按日期排序的 writeback queue，根任务合并同 owner 后决定最终写回。
<!-- review:SF-2026-ARXIV-2607-28824:end -->

<!-- review:SF-2026-ARXIV-2607-28829:start -->
### When Unlearning Fails: Reliable Data Deletion under Post-Training in Agent Networks

- **Status / Evidence:** Experimental；exact-v1 HTML 已读取并保存校验和；Score V2=`9`。
- **Problem / old solution:** 既有路径通常把 security/privacy boundary 隐含在模型调用或离线平均指标中；在较小规模、单一模型或无跨请求状态时成本较低，但难以回答谁拥有失败恢复与版本一致性。
- **Changed constraint:** 论文面对的约束由摘要和全文共同限定为：Self-improving federated agent networks keep training after deployment by collecting new trajectories with the current policy and feeding them back into later rounds. This closed loop makes unlearning harder than a one-time model repair.
- **Mechanism:** exact-v1 的方法段写明：Keeping raw data local does not settle the privacy obligation of such a network. A data owner may request that a trajectory, a client dataset, or a task source no longer influence the trained model. Regulations such as the General Data Protection Regulation (GDPR) give users a right to be forgotten . Federated unlearning (FU) addresses this requirement by removing the effect of requested data from a federated model . Existing FU methods reduce deletion cost through rollback, model editing, or verification , and recent work makes the deletion itself cheap enough for edge deployment . They mainly solve the request-time problem: once a request arrives, they update the current model to behave as if the target data…
- **State ownership:** 需要显式绑定 principal, data and proof provenance；canonical owner 是 `PLATFORM-SECURITY`，而不是论文应用领域本身。
- **Control / data flow:** 数据由工作负载进入机制实现，policy enforcement plane 决定是否执行、路由、提交或回退；输出必须携带与输入同一版本域的证据。
- **Implementation surface:** 全文 locator=`full-text paragraph 3; papers/2026/08/_sources/arxiv-owner-replay-20260903/20260803/exact-v1-text/2607.28829v1.txt`；公开实现、硬件或训练配置只按正文披露解释，未披露字段不补写。
- **Evaluation contract:** To address these limitations, we propose uting nlearned rajectories’ choes (), a reliable deletion method for self-improving federated agent networks. has three modules. It first replays a lightweight server ledger to estimate how the forget data’s influence propagates through aggregation and policy-driven collection without moving raw trajectories off clients. It then performs influence-aware erasure, where a model-side update removes direct residue and a data-side step quarantines or down-weights high-influence retained trajectories. Finally, it audits behavioral leakage and influence regeneration, and schedules later erasure or containment actions under an uplink budget. 该结果只绑定论文声明的数据、模型、硬件、精度、长度、batch/concurrency 与 evaluator；缺失字段均为 `Not Disclosed`。
- **Proves / does not prove:** 证据支持该受限 workload 中机制可行或暴露既有评价缺口；不证明跨模型、跨硬件、跨领域或生产 SLO 的普遍优势。
- **Trade-off / failure mode:** 新增状态、控制器和观测提高可验证性，但引入版本错配、额外延迟/内存/通信、错误路由及 evaluator bias。全文边界：Have a free development cycle? Help support accessibility at arXiv! Our collaborators at LaTeXML maintain a , and welcome .
- **Coexistence / evolution:** 旧方案在低风险、短状态或同构部署中仍成立；新机制只在约束变化使错误代价或状态漂移不可忽略时接手。
- **Books route:** 对照 `PLATFORM-SECURITY` 及相邻章节；先进入按日期排序的 writeback queue，根任务合并同 owner 后决定最终写回。
<!-- review:SF-2026-ARXIV-2607-28829:end -->

<!-- review:SF-2026-ARXIV-2607-28848:start -->
### DeltaServe: Host-Agnostic Co-Serving of Inference and Fine-Tuning for LLMs

- **Status / Evidence:** Experimental；exact-v1 HTML 已读取并保存校验和；Score V2=`8`。
- **Problem / old solution:** 既有路径通常把 shared inference capacity 隐含在模型调用或离线平均指标中；在较小规模、单一模型或无跨请求状态时成本较低，但难以回答谁拥有失败恢复与版本一致性。
- **Changed constraint:** 论文面对的约束由摘要和全文共同限定为：LLM serving systems are provisioned for peak load to meet strict latency targets, leaving substantial GPU compute idle whenever traffic falls below peak. We present DeltaServe, a host-agnostic co-serving design that converts this idle inference capacity into LoRA fine-tuning throughput while preserving inference service-level objectives (SLOs).
- **Mechanism:** exact-v1 的方法段写明：The background discussion shows that LoRA co-serving is appealing because inference and fine-tuning share the frozen base model, but realizing it inside an existing serving engine is difficult: fine-tuning needs training-specific control, activation capture, backward execution, and optimizer updates that inference engines are not designed to provide. addresses this gap by separating what must be added for fine-tuning from what should remain under the host system’s control. Its design keeps the host responsible for request handling, batching, KV-cache management, sampling, and optimized forward execution, while adds only the mechanisms needed to turn admitted fine-tuning samples into prefill-like batch entries…
- **State ownership:** 需要显式绑定 request/model/adaptation residency；canonical owner 是 `INFER-SCHEDULING`，而不是论文应用领域本身。
- **Control / data flow:** 数据由工作负载进入机制实现，scheduler 决定是否执行、路由、提交或回退；输出必须携带与输入同一版本域的证据。
- **Implementation surface:** 全文 locator=`System Design; papers/2026/08/_sources/arxiv-owner-replay-20260903/20260803/exact-v1-text/2607.28848v1.txt`；公开实现、硬件或训练配置只按正文披露解释，未披露字段不补写。
- **Evaluation contract:** In this section, we evaluate ’s ability to fold LoRA fine-tuning into a host inference engine under diverse conditions, harvesting the capacity inference leaves idle without violating the host’s inference SLOs, guided by the following key questions: Does exploit idle capacity left by gaps and low-load periods in inference workloads, converting it into fine-tuning throughput while preserving inference SLOs? How does this compare with LLMStation and with a split-pool deployment in fine-tuning throughput, average latency, and SLO compliance (Section )? 该结果只绑定论文声明的数据、模型、硬件、精度、长度、batch/concurrency 与 evaluator；缺失字段均为 `Not Disclosed`。
- **Proves / does not prove:** 证据支持该受限 workload 中机制可行或暴露既有评价缺口；不证明跨模型、跨硬件、跨领域或生产 SLO 的普遍优势。
- **Trade-off / failure mode:** 新增状态、控制器和观测提高可验证性，但引入版本错配、额外延迟/内存/通信、错误路由及 evaluator bias。全文边界：This paper introduced , a host-agnostic co-serving design that folds LoRA fine-tuning into an existing inference engine under SLO control, driven by a CUDA-graph-aware latency model and realized on vLLM, SGLang, and S-LoRA. On a Nutanix production trace it delivers the fine-tuning throughput of LLMStation at inference SLO compliance versus LLMStation’s , harvesting idle GPU capacity without compromising interactive latency.
- **Coexistence / evolution:** 旧方案在低风险、短状态或同构部署中仍成立；新机制只在约束变化使错误代价或状态漂移不可忽略时接手。
- **Books route:** 对照 `INFER-SCHEDULING` 及相邻章节；先进入按日期排序的 writeback queue，根任务合并同 owner 后决定最终写回。
<!-- review:SF-2026-ARXIV-2607-28848:end -->

<!-- review:SF-2026-ARXIV-2607-28871:start -->
### Validation Evidence in LLM Repair Agents: How Much of What Passes Actually Tests the Bug?

- **Status / Evidence:** Experimental；exact-v1 HTML 已读取并保存校验和；Score V2=`7`。
- **Problem / old solution:** 既有路径通常把 evaluation evidence and release decision 隐含在模型调用或离线平均指标中；在较小规模、单一模型或无跨请求状态时成本较低，但难以回答谁拥有失败恢复与版本一致性。
- **Changed constraint:** 论文面对的约束由摘要和全文共同限定为：When a repair agent runs a test and sees it pass, the result is treated as evidence about the reported defect. We measure how often that treatment is warranted.
- **Mechanism:** exact-v1 的方法段写明：But a passing test can mean different things. Consider an agent assigned a defect in a date-formatting routine. The agent modifies the routine, then writes a test that imports the module and asserts that the output is a string. The test passes. It would also have passed on the original buggy code, because the bug was not about return types but about locale handling. The agent has confirmed that its patch does not break the import or change the output type. It has learned nothing about whether the locale bug is fixed. If this is the only positive evidence the agent collects before submitting, the submission rests on validation that is real but irrelevant to the assigned defect.
- **State ownership:** 需要显式绑定 evaluator configuration, dataset slice and result provenance；canonical owner 是 `PLATFORM-EVALUATION-SYSTEM`，而不是论文应用领域本身。
- **Control / data flow:** 数据由工作负载进入机制实现，evaluation controller 决定是否执行、路由、提交或回退；输出必须携带与输入同一版本域的证据。
- **Implementation surface:** 全文 locator=`full-text paragraph 3; papers/2026/08/_sources/arxiv-owner-replay-20260903/20260803/exact-v1-text/2607.28871v1.txt`；公开实现、硬件或训练配置只按正文披露解释，未披露字段不补写。
- **Evaluation contract:** analyse six models on SWE-bench Verified and report that test-writing frequency is similar between successful and failed trajectories; that most validation commands are print-statement explorations rather than assertion-bearing tests; and that prompting models to write more or fewer tests produces no detectable change in repair outcomes. The finding that test-writing is abundant but not predictive of success is consistent with the hypothesis that much of the validation activity lacks discriminating power, but the study does not measure discriminating power directly. analyse the cost-effectiveness of code execution in LLM-based repair at scale and report that failed commercial-agent runs often pass their own se… 该结果只绑定论文声明的数据、模型、硬件、精度、长度、batch/concurrency 与 evaluator；缺失字段均为 `Not Disclosed`。
- **Proves / does not prove:** 证据支持该受限 workload 中机制可行或暴露既有评价缺口；不证明跨模型、跨硬件、跨领域或生产 SLO 的普遍优势。
- **Trade-off / failure mode:** 新增状态、控制器和观测提高可验证性，但引入版本错配、额外延迟/内存/通信、错误路由及 evaluator bias。全文边界：We introduce BSG-VA, a method that measures the evidential value of the validation activity repair agents perform mid-trajectory, by replaying each command on the buggy, candidate, and gold-fix code states. Applied at scale, the method reveals that 46.0% of positive comparable validation events carry no bug-discriminating information, and that 23.8% of baseline rollouts close on the basis of such evidence alone. Bug-contrast feedback, which returns the B-replay outcome to the agent in real time, reduces evidence-inadequate closure by 7.8 percentage points, without measurable cost to repair success. That estimate falls below the prespecified 10-percentage-point SESOI, so the direction of the effect is establish…
- **Coexistence / evolution:** 旧方案在低风险、短状态或同构部署中仍成立；新机制只在约束变化使错误代价或状态漂移不可忽略时接手。
- **Books route:** 对照 `PLATFORM-EVALUATION-SYSTEM` 及相邻章节；先进入按日期排序的 writeback queue，根任务合并同 owner 后决定最终写回。
<!-- review:SF-2026-ARXIV-2607-28871:end -->

<!-- review:SF-2026-ARXIV-2607-28884:start -->
### Hollow-LLM Attack: Computationally Trivial Weights in Zero-Knowledge Verification of LLM Inference

- **Status / Evidence:** Experimental；exact-v1 HTML 已读取并保存校验和；Score V2=`9`。
- **Problem / old solution:** 既有路径通常把 security/privacy boundary 隐含在模型调用或离线平均指标中；在较小规模、单一模型或无跨请求状态时成本较低，但难以回答谁拥有失败恢复与版本一致性。
- **Changed constraint:** 论文面对的约束由摘要和全文共同限定为：As large language models (LLMs) grow in scale and are predominantly served from remote platforms, verifying faithful inference execution becomes critical (i.e., ensuring that a provider actually executes the advertised model and computational workload rather than a tampered or downsized variant). Zero-knowledge (ZK) LLM inference offers an appealing approach.
- **Mechanism:** exact-v1 的方法段写明：Large Language Models (LLMs) have become increasingly powerful and pervasive, underpinning a large market of AI services. With the growth in both size and scale, LLMs usually require substantial GPU resources and are thus often deployed on remote or cloud platforms. This deployment model raises critical concerns about the of inference: Such concerns include verifying that the deployed model has not been tampered with (e.g., no hidden backdoors) , that the outputs are truly generated by the advertised model , and that the model’s size or parameters have not been surreptitiously replaced with a smaller or different model .
- **State ownership:** 需要显式绑定 principal, data and proof provenance；canonical owner 是 `PLATFORM-SECURITY`，而不是论文应用领域本身。
- **Control / data flow:** 数据由工作负载进入机制实现，policy enforcement plane 决定是否执行、路由、提交或回退；输出必须携带与输入同一版本域的证据。
- **Implementation surface:** 全文 locator=`full-text paragraph 3; papers/2026/08/_sources/arxiv-owner-replay-20260903/20260803/exact-v1-text/2607.28884v1.txt`；公开实现、硬件或训练配置只按正文披露解释，未披露字段不补写。
- **Evaluation contract:** In this paper, we reveal a previously overlooked limitation of the above ZK LLM inference verification procedure. Specifically, a zero-knowledge proof of inference certifies membership in a nondeterministic polynomial-time (NP) relation: it proves that there exist private weights such that the output is the result of executing the public model architecture on the input. However, the proof does not attest to the algorithmic path taken to obtain that result or how much computation was necessary to get the result. In other words, it verifies the correctness of the equations that define the model size and architecture, but not the effort expended to calculate the result. This creates an compared to the declared pu… 该结果只绑定论文声明的数据、模型、硬件、精度、长度、batch/concurrency 与 evaluator；缺失字段均为 `Not Disclosed`。
- **Proves / does not prove:** 证据支持该受限 workload 中机制可行或暴露既有评价缺口；不证明跨模型、跨硬件、跨领域或生产 SLO 的普遍优势。
- **Trade-off / failure mode:** 新增状态、控制器和观测提高可验证性，但引入版本错配、额外延迟/内存/通信、错误路由及 evaluator bias。全文边界：Have a free development cycle? Help support accessibility at arXiv! Our collaborators at LaTeXML maintain a , and welcome .
- **Coexistence / evolution:** 旧方案在低风险、短状态或同构部署中仍成立；新机制只在约束变化使错误代价或状态漂移不可忽略时接手。
- **Books route:** 对照 `PLATFORM-SECURITY` 及相邻章节；先进入按日期排序的 writeback queue，根任务合并同 owner 后决定最终写回。
<!-- review:SF-2026-ARXIV-2607-28884:end -->

<!-- review:SF-2026-ARXIV-2607-28887:start -->
### To Add Is Machine, To Delete Is Human: Measuring and Mitigating Deletion Avoidance in LLM Code Editing

- **Status / Evidence:** Experimental；exact-v1 HTML 已读取并保存校验和；Score V2=`6`。
- **Problem / old solution:** 既有路径通常把 durable multi-step execution 隐含在模型调用或离线平均指标中；在较小规模、单一模型或无跨请求状态时成本较低，但难以回答谁拥有失败恢复与版本一致性。
- **Changed constraint:** 论文面对的约束由摘要和全文共同限定为：Large language models increasingly write and repair production code, yet evidence is mounting that their test-passing patches leave codebases harder to maintain. We identify one concrete source: deletion avoidance, the systematic tendency to retain code that an intended edit requires removing.
- **Mechanism:** exact-v1 的方法段写明：Commit statistics point the same way. Across 623 million analyzed changes, edits that take out or update code older than twelve months fell 74% after 2023, while error-masking constructs rose 47% . One reason agent patches read as bloated is that models leave code in place that the change was meant to remove. Reviewers of agent-written pull requests routinely delete generated methods, which they must read in full before deciding .
- **State ownership:** 需要显式绑定 task, evidence and checkpoint state；canonical owner 是 `AGENT-WORKFLOW`，而不是论文应用领域本身。
- **Control / data flow:** 数据由工作负载进入机制实现，workflow engine 决定是否执行、路由、提交或回退；输出必须携带与输入同一版本域的证据。
- **Implementation surface:** 全文 locator=`full-text paragraph 3; papers/2026/08/_sources/arxiv-owner-replay-20260903/20260803/exact-v1-text/2607.28887v1.txt`；公开实现、硬件或训练配置只按正文披露解释，未披露字段不补写。
- **Evaluation contract:** Sections and establish that models leave developer-removed code in place and that behavioral test suites accept many of the patches that do. Neither study attributes the failure to deletion itself: in full repository repair, a missed removal can originate in localization, in replacement code, or in surrounding implementation work, and nothing in the task states that removal is required. We therefore build , 200 tasks mined from real commits in which deletion is the complete required transformation. Because the reference edit adds nothing, every compliant solution must perform the same removal while preserving unrelated code, and a failed output reflects the model’s editing behavior rather than ambiguity about… 该结果只绑定论文声明的数据、模型、硬件、精度、长度、batch/concurrency 与 evaluator；缺失字段均为 `Not Disclosed`。
- **Proves / does not prove:** 证据支持该受限 workload 中机制可行或暴露既有评价缺口；不证明跨模型、跨硬件、跨领域或生产 SLO 的普遍优势。
- **Trade-off / failure mode:** 新增状态、控制器和观测提高可验证性，但引入版本错配、额外延迟/内存/通信、错误路由及 evaluator bias。全文边界：Deletion avoidance recurs across current code models: patches that SWE-bench Verified marks resolved retain a quarter to a third of the developer’s deletions, substituting added control flow for removal, and pass because the tests rarely check it, so resolution rates overstate merge-ready behavior. The gap persists when deletion is the entire task, and exact spans only trade retention for over-deletion: models lack control over removal rather than the capability. Modest deletion supervision reduces the behavior and improves repository-level repair, so the deficit appears undertrained rather than intrinsic. These findings are bounded in scope, construction, and scale. The in-the-wild analysis rests on submitted…
- **Coexistence / evolution:** 旧方案在低风险、短状态或同构部署中仍成立；新机制只在约束变化使错误代价或状态漂移不可忽略时接手。
- **Books route:** 对照 `AGENT-WORKFLOW` 及相邻章节；先进入按日期排序的 writeback queue，根任务合并同 owner 后决定最终写回。
<!-- review:SF-2026-ARXIV-2607-28887:end -->

<!-- review:SF-2026-ARXIV-2607-28896:start -->
### TORUS: A Test of Rendering-Understanding Self-Coherence for Unified Audio Models

- **Status / Evidence:** Experimental；exact-v1 HTML 已读取并保存校验和；Score V2=`7`。
- **Problem / old solution:** 既有路径通常把 evaluation evidence and release decision 隐含在模型调用或离线平均指标中；在较小规模、单一模型或无跨请求状态时成本较低，但难以回答谁拥有失败恢复与版本一致性。
- **Changed constraint:** 论文面对的约束由摘要和全文共同限定为：Unified audio models capable of audio understanding, audio generation and, increasingly, audio editing are proliferating rapidly. Yet a basic question about them remains unanswered: do the two heads of a unified model agree about the same audio?
- **Mechanism:** exact-v1 的方法段写明：Vision has recently begun to close this loop, letting a unified model generate, edit and answer questions about its own images . The unified audio models space is still shaping up and we lack a concrete analogous evaluation for audio models. However, transfer self-evaluation from vision to audio is not a trivial task. Questions about audio carry unusually strong since both modalities represent languages heavily. Audio, being innately , also brings its own task structure which can span across physical causality and scene acoustics to temporal ordering, which have few to no visual analogs. An audio-native self-coherence benchmark must therefore be constructed text-prior leakage and audio’s own tasks transcending…
- **State ownership:** 需要显式绑定 evaluator configuration, dataset slice and result provenance；canonical owner 是 `PLATFORM-EVALUATION-SYSTEM`，而不是论文应用领域本身。
- **Control / data flow:** 数据由工作负载进入机制实现，evaluation controller 决定是否执行、路由、提交或回退；输出必须携带与输入同一版本域的证据。
- **Implementation surface:** 全文 locator=`full-text paragraph 3; papers/2026/08/_sources/arxiv-owner-replay-20260903/20260803/exact-v1-text/2607.28896v1.txt`；公开实现、硬件或训练配置只按正文披露解释，未披露字段不补写。
- **Evaluation contract:** Table situates TORUS against the closest benchmarks along the axes that define it. Benchmarks such as MMAU and MMAU-Pro grade text answers about audio while compositional, relational and reasoning suites like CompA , MMAR , MMSU and ADQA-Bench expand on the idea. Across all of them the model’s output is a label, never a sound, and the audio is never the model’s own. TORUS maintains this family’s grading discipline (with keys fixed at construction time, scored by exact letter match) and extends it to generation and editing: the clip under question is one that has been generated or edited by the model itself. Questions about audio tend to leak their own answers through their sentence framing i.e. the model doesn… 该结果只绑定论文声明的数据、模型、硬件、精度、长度、batch/concurrency 与 evaluator；缺失字段均为 `Not Disclosed`。
- **Proves / does not prove:** 证据支持该受限 workload 中机制可行或暴露既有评价缺口；不证明跨模型、跨硬件、跨领域或生产 SLO 的普遍优势。
- **Trade-off / failure mode:** 新增状态、控制器和观测提高可验证性，但引入版本错配、额外延迟/内存/通信、错误路由及 evaluator bias。全文边界：Table reports unified models’ performance across self-coherence based and objective metrics on TORUS compared across a baseline of cascaded audio understanding, generation and editing models (Cascaded Baseline). Several patterns can be seen to emerge.
- **Coexistence / evolution:** 旧方案在低风险、短状态或同构部署中仍成立；新机制只在约束变化使错误代价或状态漂移不可忽略时接手。
- **Books route:** 对照 `PLATFORM-EVALUATION-SYSTEM` 及相邻章节；先进入按日期排序的 writeback queue，根任务合并同 owner 后决定最终写回。
<!-- review:SF-2026-ARXIV-2607-28896:end -->

<!-- review:SF-2026-ARXIV-2607-28908:start -->
### Reflection or Re-Generation? Why LLM Revision Fails Where Human Revision Succeeds

- **Status / Evidence:** Experimental；exact-v1 HTML 已读取并保存校验和；Score V2=`6`。
- **Problem / old solution:** 既有路径通常把 revision and self-correction 隐含在模型调用或离线平均指标中；在较小规模、单一模型或无跨请求状态时成本较低，但难以回答谁拥有失败恢复与版本一致性。
- **Changed constraint:** 论文面对的约束由摘要和全文共同限定为：Reflection, the ability to revisit and revise prior reasoning, is central to how humans improve their answers. Large language models (LLMs) are increasingly prompted to "reflect," yet whether this resembles human revision remains unclear.
- **Mechanism:** exact-v1 的方法段写明：We introduce the Human–LLM Reflection Framework (HRF), a controlled evaluation protocol for studying reflective revision in humans and LLMs under identical conditions. The overall pipeline is illustrated in Figure .
- **State ownership:** 需要显式绑定 draft/evidence/revision state；canonical owner 是 `AGENT-REFLECTION`，而不是论文应用领域本身。
- **Control / data flow:** 数据由工作负载进入机制实现，reflection policy 决定是否执行、路由、提交或回退；输出必须携带与输入同一版本域的证据。
- **Implementation surface:** 全文 locator=`Framework and Experimental Setup; papers/2026/08/_sources/arxiv-owner-replay-20260903/20260803/exact-v1-text/2607.28908v1.txt`；公开实现、硬件或训练配置只按正文披露解释，未披露字段不补写。
- **Evaluation contract:** We introduce the Human–LLM Reflection Framework (HRF), a controlled evaluation protocol for studying reflective revision in humans and LLMs under identical conditions. The overall pipeline is illustrated in Figure . 该结果只绑定论文声明的数据、模型、硬件、精度、长度、batch/concurrency 与 evaluator；缺失字段均为 `Not Disclosed`。
- **Proves / does not prove:** 证据支持该受限 workload 中机制可行或暴露既有评价缺口；不证明跨模型、跨硬件、跨领域或生产 SLO 的普遍优势。
- **Trade-off / failure mode:** 新增状态、控制器和观测提高可验证性，但引入版本错配、额外延迟/内存/通信、错误路由及 evaluator bias。全文边界：Our information-theoretic analysis is restricted to tasks with finite answer spaces and reliable ground truth (MalAlgoQA and IMDb-Rating). Extending these measures to open-ended generation remains an open challenge. Human annotators are non-expert crowdworkers; expert annotators might exhibit different revision patterns, though the structural differences we observe (sparse, directional revision versus high-variance re-sampling) are unlikely to depend on domain expertise alone. Our second-pass prompt asks the model to agree or disagree with the prior answer, which may itself encourage revision. As a control, we re-ran the IMDb second pass with a neutral prompt that asks the model to revise only upon identifying…
- **Coexistence / evolution:** 旧方案在低风险、短状态或同构部署中仍成立；新机制只在约束变化使错误代价或状态漂移不可忽略时接手。
- **Books route:** 对照 `AGENT-REFLECTION` 及相邻章节；先进入按日期排序的 writeback queue，根任务合并同 owner 后决定最终写回。
<!-- review:SF-2026-ARXIV-2607-28908:end -->

<!-- review:SF-2026-ARXIV-2607-28928:start -->
### Automated Testing and Repair for Verified Compilers Generated by a Coding Agent

- **Status / Evidence:** Experimental；exact-v1 HTML 已读取并保存校验和；Score V2=`6`。
- **Problem / old solution:** 既有路径通常把 durable multi-step execution 隐含在模型调用或离线平均指标中；在较小规模、单一模型或无跨请求状态时成本较低，但难以回答谁拥有失败恢复与版本一致性。
- **Changed constraint:** 论文面对的约束由摘要和全文共同限定为：We present an agent based automated testing and repair system for verified compilers that contain four kinds of code: verified code, checked code, unverified code, and specification. We present specialized defect detection techniques that exploit the structure present in such compilers.
- **Mechanism:** exact-v1 的方法段写明：We present ACDC (Automated Certificate Detection and Correction), a new system and technique for automatically discovering and repairing defects in verified compiler systems that use credible/checked compilation. We apply ACDC to Axon , the first verified source to assembler compiler developed entirely by a coding agent operating under human supervision. Axon implements both verified compiler techniques: 1) full verification of basic translation steps to ensure correct compilation for all programs and 2) checked credible compilation to ensure the compilation includes only sound optimizations. With credible compilation optimizations are not verified — they instead generate a certificate that proves they transfo…
- **State ownership:** 需要显式绑定 task, evidence and checkpoint state；canonical owner 是 `AGENT-WORKFLOW`，而不是论文应用领域本身。
- **Control / data flow:** 数据由工作负载进入机制实现，workflow engine 决定是否执行、路由、提交或回退；输出必须携带与输入同一版本域的证据。
- **Implementation surface:** 全文 locator=`full-text paragraph 3; papers/2026/08/_sources/arxiv-owner-replay-20260903/20260803/exact-v1-text/2607.28928v1.txt`；公开实现、硬件或训练配置只按正文披露解释，未披露字段不补写。
- **Evaluation contract:** If the repair updates the certificate checker, it must also update the certificate checker’s proof of correctness to reestablish verified end to end compiler correctness. 该结果只绑定论文声明的数据、模型、硬件、精度、长度、batch/concurrency 与 evaluator；缺失字段均为 `Not Disclosed`。
- **Proves / does not prove:** 证据支持该受限 workload 中机制可行或暴露既有评价缺口；不证明跨模型、跨硬件、跨领域或生产 SLO 的普遍优势。
- **Trade-off / failure mode:** 新增状态、控制器和观测提高可验证性，但引入版本错配、额外延迟/内存/通信、错误路由及 evaluator bias。全文边界：Have a free development cycle? Help support accessibility at arXiv! Our collaborators at LaTeXML maintain a , and welcome .
- **Coexistence / evolution:** 旧方案在低风险、短状态或同构部署中仍成立；新机制只在约束变化使错误代价或状态漂移不可忽略时接手。
- **Books route:** 对照 `AGENT-WORKFLOW` 及相邻章节；先进入按日期排序的 writeback queue，根任务合并同 owner 后决定最终写回。
<!-- review:SF-2026-ARXIV-2607-28928:end -->

<!-- review:SF-2026-ARXIV-2607-28940:start -->
### TransX: Scaling Transformer-based Recommendation via Behavioral and Serving Stream Crossings

- **Status / Evidence:** Experimental；exact-v1 HTML 已读取并保存校验和；Score V2=`8`。
- **Problem / old solution:** 既有路径通常把 request execution lifecycle 隐含在模型调用或离线平均指标中；在较小规模、单一模型或无跨请求状态时成本较低，但难以回答谁拥有失败恢复与版本一致性。
- **Changed constraint:** 论文面对的约束由摘要和全文共同限定为：Modern industrial recommender systems (RecSys) increasingly adopt Transformer-based sequence models, with an emerging paradigm that frames recommendation as next-token prediction over a unified monolithic user sequence. However, collapsing heterogeneous data sources -- such as long-term user behaviors and real-time serving events -- into a single monolithic token stream that obscures their distinct causal roles and temporal c…
- **Mechanism:** exact-v1 的方法段写明：In this section, we detail the TransX architecture and its corresponding training and serving system infrastructure. We frame the recommendation task as a sequence-to-sequence transduction problem, mapping an input behavior stream and a serving event stream to a discrete action token stream.
- **State ownership:** 需要显式绑定 request/stream/session state；canonical owner 是 `INFER-REQUEST-LIFECYCLE`，而不是论文应用领域本身。
- **Control / data flow:** 数据由工作负载进入机制实现，serving engine 决定是否执行、路由、提交或回退；输出必须携带与输入同一版本域的证据。
- **Implementation surface:** 全文 locator=`Methodology; papers/2026/08/_sources/arxiv-owner-replay-20260903/20260803/exact-v1-text/2607.28940v1.txt`；公开实现、硬件或训练配置只按正文披露解释，未披露字段不补写。
- **Evaluation contract:** Let be the size of the local attention window and be the number of serving events. For simplicity, assume the decoding head is a linear function. We provide the detailed derivations in Appendix and summarize the analysis results below. Compared to the typical sequential and GR models, by enabling amortized and cachable sequence encoding, TransX approximately reduces training complexity from to , up to constant factors. As a result, . At serving time, , achieving -bounded online computation at the cost of a constant memory footprint. Together, they enable the deployment of our advanced Transformer-based action transduction model under sub-100ms latency SLAs without incurring significant online hardware cost. Em… 该结果只绑定论文声明的数据、模型、硬件、精度、长度、batch/concurrency 与 evaluator；缺失字段均为 `Not Disclosed`。
- **Proves / does not prove:** 证据支持该受限 workload 中机制可行或暴露既有评价缺口；不证明跨模型、跨硬件、跨领域或生产 SLO 的普遍优势。
- **Trade-off / failure mode:** 新增状态、控制器和观测提高可验证性，但引入版本错配、额外延迟/内存/通信、错误路由及 evaluator bias。全文边界：Beyond the substantial online metric improvements, the success of TransX suggests a promising direction for architecting large-scale industrial recommenders. A core takeaway from this work is that by explicitly modeling the "crossing" of the user behavior stream and the system serving stream, we allow the selective application of expensive Transformer layers where they are most needed, rather than uniformly across a flattened monolithic token stream. One promising direction is to extend TransX into a unified retrieval-and-ranking framework that jointly handles candidate generation and action transduction. The sequence–candidate crossing architecture naturally supports this extension by introducing an auxiliary…
- **Coexistence / evolution:** 旧方案在低风险、短状态或同构部署中仍成立；新机制只在约束变化使错误代价或状态漂移不可忽略时接手。
- **Books route:** 对照 `INFER-REQUEST-LIFECYCLE` 及相邻章节；先进入按日期排序的 writeback queue，根任务合并同 owner 后决定最终写回。
<!-- review:SF-2026-ARXIV-2607-28940:end -->

<!-- review:SF-2026-ARXIV-2607-28942:start -->
### NeSyFS: A Neuro-symbolic Fast-Slow Thinking Framework for LLM Agent under Partial Observability

- **Status / Evidence:** Experimental；exact-v1 HTML 已读取并保存校验和；Score V2=`6`。
- **Problem / old solution:** 既有路径通常把 planning under partial observability 隐含在模型调用或离线平均指标中；在较小规模、单一模型或无跨请求状态时成本较低，但难以回答谁拥有失败恢复与版本一致性。
- **Changed constraint:** 论文面对的约束由摘要和全文共同限定为：Recently Large Language Models (LLMs) have been increasingly deployed as autonomous agents in applications such as self-reflection, retrieval-augmented generation, and scientific discovery. In these settings, agents must act based on limited observations rather than full environmental states, leading to partial observability.
- **Mechanism:** exact-v1 的方法段写明：Recently Large Language Models (LLMs) have been increasingly deployed as autonomous agents in applications such as self-reflection, retrieval-augmented generation, and scientific discovery. In these settings, agents must act based on limited observations rather than full environmental states, leading to partial observability. This introduces several key challenges: belief state inference, task objective misalignment, and planning under uncertainty. Prior approaches typically condition actions on full or summarized action–observation histories whose redundant and irrelevant information can mislead the decision making of LLM agent. Inspired by human cognition, we propose a novel uro-mbolic ast–low thinking (NeSy…
- **State ownership:** 需要显式绑定 belief/plan/rollback state；canonical owner 是 `AGENT-PLANNING`，而不是论文应用领域本身。
- **Control / data flow:** 数据由工作负载进入机制实现，planner 决定是否执行、路由、提交或回退；输出必须携带与输入同一版本域的证据。
- **Implementation surface:** 全文 locator=`NeSyFS: A Neuro-symbolic Fast-Slow Thinking Framework for LLM Agent under Partial Observability; papers/2026/08/_sources/arxiv-owner-replay-20260903/20260803/exact-v1-text/2607.28942v1.txt`；公开实现、硬件或训练配置只按正文披露解释，未披露字段不补写。
- **Evaluation contract:** We benchmarked NeSyFS on three widely used text-based environments: ALFWorld , WebShop , and ScienceWorld . ALFWorld evaluates embodied agents on household tasks, WebShop emulates multi-step decision-making tasks in an online shopping website environment, and ScienceWorld assesses procedural and scientific reasoning in educational scenarios. For evaluation, ALFWorld uses binary task success, while WebShop and ScienceWorld provide dense reward signals, enabling evaluation based on both success rate and average reward, calculated as the mean reward across all tasks. Additional benchmark details are presented in Appendix . In the evaluations, we use GPT-5, GPT-5-mini and Llama-3.3-70B-Instruct as the underlying m… 该结果只绑定论文声明的数据、模型、硬件、精度、长度、batch/concurrency 与 evaluator；缺失字段均为 `Not Disclosed`。
- **Proves / does not prove:** 证据支持该受限 workload 中机制可行或暴露既有评价缺口；不证明跨模型、跨硬件、跨领域或生产 SLO 的普遍优势。
- **Trade-off / failure mode:** 新增状态、控制器和观测提高可验证性，但引入版本错配、额外延迟/内存/通信、错误路由及 evaluator bias。全文边界：In this work, we propose a neuro-symbolic framework which addresses the challenges introduced by partial observability in a unified manner. Under partial observability, the agent may have difficulties on latent state inference, task objective misalignment, and planning under uncertainty. In NeSyFS, the latent state of the environment is represented and maintained as a memory KG, and triplets retrieved from KG are used as context in every module of NeSyFS. In addition, a KG-augmented reflection module is proposed to address the misalignment of the task objective. Besides, a neuro-symbolic TSMC-style planning algorithm is proposed to tackle the uncertainty in observation prediction and task progress evaluation.…
- **Coexistence / evolution:** 旧方案在低风险、短状态或同构部署中仍成立；新机制只在约束变化使错误代价或状态漂移不可忽略时接手。
- **Books route:** 对照 `AGENT-PLANNING` 及相邻章节；先进入按日期排序的 writeback queue，根任务合并同 owner 后决定最终写回。
<!-- review:SF-2026-ARXIV-2607-28942:end -->

<!-- review:SF-2026-ARXIV-2607-28966:start -->
### BLADE: Boundary-Expanded and Layer-Adaptive Dynamic Exit for Efficient LLM Reasoning

- **Status / Evidence:** Experimental；exact-v1 HTML 已读取并保存校验和；Score V2=`8`。
- **Problem / old solution:** 既有路径通常把 shared inference capacity 隐含在模型调用或离线平均指标中；在较小规模、单一模型或无跨请求状态时成本较低，但难以回答谁拥有失败恢复与版本一致性。
- **Changed constraint:** 论文面对的约束由摘要和全文共同限定为：Large language models often improve task performance by generating long reasoning traces, but the resulting computation is frequently wasted on redundant verification and revision. Existing probe-based early-exit approaches mainly inspect explicit self-doubt expressions, leaving many earlier termination opportunities undetected.
- **Mechanism:** exact-v1 的方法段写明：We formulate reasoning early exit as prefix-sufficiency prediction: determining whether an intermediate reasoning prefix already supports a reliable correct answer. As shown in Fig. , BLADE consists of two training components and a checkpoint-aware inference policy. MGRC constructs diverse candidate states with low-noise sufficiency labels, while APLS selects a compact set of hidden layers for efficient prediction. At inference, the resulting probe applies checkpoint-specific stopping rules to terminate unnecessary reasoning.
- **State ownership:** 需要显式绑定 request/model/adaptation residency；canonical owner 是 `INFER-SCHEDULING`，而不是论文应用领域本身。
- **Control / data flow:** 数据由工作负载进入机制实现，scheduler 决定是否执行、路由、提交或回退；输出必须携带与输入同一版本域的证据。
- **Implementation surface:** 全文 locator=`Methodology; papers/2026/08/_sources/arxiv-owner-replay-20260903/20260803/exact-v1-text/2607.28966v1.txt`；公开实现、硬件或训练配置只按正文披露解释，未披露字段不补写。
- **Evaluation contract:** We evaluate BLADE on five mathematical reasoning benchmarks—GSM8K-test , MATH-500 , AMC 2023 , AIME 2024 , and AIME 2025 —using Qwen3-8B and Qwen3-4B . The suite contains 1,919 questions, split into 192 calibration and 1,727 held-out test examples. 该结果只绑定论文声明的数据、模型、硬件、精度、长度、batch/concurrency 与 evaluator；缺失字段均为 `Not Disclosed`。
- **Proves / does not prove:** 证据支持该受限 workload 中机制可行或暴露既有评价缺口；不证明跨模型、跨硬件、跨领域或生产 SLO 的普遍优势。
- **Trade-off / failure mode:** 新增状态、控制器和观测提高可验证性，但引入版本错配、额外延迟/内存/通信、错误路由及 evaluator bias。全文边界：We propose BLADE, a boundary-expanded, layer-adaptive framework for dynamic early exit in efficient LLM reasoning. Experiments on five benchmarks and two Qwen3 backbones show that BLADE reduces generated tokens while largely preserving accuracy. Ablations show that combining sentence and self-doubt boundaries uncovers exit opportunities missed by self-doubt-only monitoring, while automatic layer selection yields compact representations. These findings highlight the complementary roles of checkpoint coverage and adaptive layer selection in efficient reasoning.
- **Coexistence / evolution:** 旧方案在低风险、短状态或同构部署中仍成立；新机制只在约束变化使错误代价或状态漂移不可忽略时接手。
- **Books route:** 对照 `INFER-SCHEDULING` 及相邻章节；先进入按日期排序的 writeback queue，根任务合并同 owner 后决定最终写回。
<!-- review:SF-2026-ARXIV-2607-28966:end -->

<!-- review:SF-2026-ARXIV-2607-28979:start -->
### Mixture-of-Translators: Translating KV Caches Across Heterogeneous Large Language Models

- **Status / Evidence:** Experimental；exact-v1 HTML 已读取并保存校验和；Score V2=`9`。
- **Problem / old solution:** 既有路径通常把 decode-state compression or translation 隐含在模型调用或离线平均指标中；在较小规模、单一模型或无跨请求状态时成本较低，但难以回答谁拥有失败恢复与版本一致性。
- **Changed constraint:** 论文面对的约束由摘要和全文共同限定为：Heterogeneous Large Language Model (LLM) systems increasingly rely on shared contexts, retrieved evidence, and multi-agent dialogue histories, yet their internal key-value (KV) caches remain model-specific and cannot be reused across architectures. Consequently, each model must repeatedly prefill or store caches for the same context, limiting the scalability of multi-model reasoning and long-context generation.
- **Mechanism:** exact-v1 的方法段写明：The theoretical analysis in the preliminaries shows that cache translation must jointly control two error dynamics: the translation shift formed inside the channel window and the last-state shift remaining after insufficient upper-layer correction. Based on this analysis, we propose two learning components. First, Section introduces , which reduces token-level translation mismatch inside the channel window through gated translator routing. Second, Section introduces , which aligns the replayed target trajectory with the native target trajectory after translation and directly targets the remaining last-state shift. These two components are used within the overall cache-translation pipeline shown in Fig. . The p…
- **State ownership:** 需要显式绑定 layer/head/token KV identity；canonical owner 是 `INFER-KV-CACHE`，而不是论文应用领域本身。
- **Control / data flow:** 数据由工作负载进入机制实现，cache manager 决定是否执行、路由、提交或回退；输出必须携带与输入同一版本域的证据。
- **Implementation surface:** 全文 locator=`Proposed Method:; papers/2026/08/_sources/arxiv-owner-replay-20260903/20260803/exact-v1-text/2607.28979v1.txt`；公开实现、硬件或训练配置只按正文披露解释，未披露字段不补写。
- **Evaluation contract:** We evaluate on downstream QA benchmarks under both homogeneous and heterogeneous cache-translation settings. Section summarizes the experimental setup, and Section reports the main results. Section analyzes the effects of correction behavior, loss design, and the architecture. Additional ablations and scalability analyses are provided in Appendix and Appendix . 该结果只绑定论文声明的数据、模型、硬件、精度、长度、batch/concurrency 与 evaluator；缺失字段均为 `Not Disclosed`。
- **Proves / does not prove:** 证据支持该受限 workload 中机制可行或暴露既有评价缺口；不证明跨模型、跨硬件、跨领域或生产 SLO 的普遍优势。
- **Trade-off / failure mode:** 新增状态、控制器和观测提高可验证性，但引入版本错配、额外延迟/内存/通信、错误路由及 evaluator bias。全文边界：We introduced , a cache translation framework for reusing KV caches across heterogeneous LLMs. MoT combines multiple translator modules with token-level routing and a Context Correction Loss that aligns the replayed target trajectory with the native target trajectory. Our analysis identified two competing error sources, propagated translation shift and correction-deficit error, which motivate this joint design. Experiments on closed-set QA, extractive QA, multi-agent reasoning, and long-context cache-augmented generation show that MoT preserves downstream quality across homogeneous and heterogeneous model pairs. The case studies further demonstrate memory reuse in multi-agent reasoning and storage reuse in lon…
- **Coexistence / evolution:** 旧方案在低风险、短状态或同构部署中仍成立；新机制只在约束变化使错误代价或状态漂移不可忽略时接手。
- **Books route:** 对照 `INFER-KV-CACHE` 及相邻章节；先进入按日期排序的 writeback queue，根任务合并同 owner 后决定最终写回。
<!-- review:SF-2026-ARXIV-2607-28979:end -->

<!-- review:SF-2026-ARXIV-2607-28990:start -->
### Scaling Scientific Discovery Environments for Turn-Level Agentic RL

- **Status / Evidence:** Experimental；exact-v1 HTML 已读取并保存校验和；Score V2=`6`。
- **Problem / old solution:** 既有路径通常把 on-policy reasoning optimization 隐含在模型调用或离线平均指标中；在较小规模、单一模型或无跨请求状态时成本较低，但难以回答谁拥有失败恢复与版本一致性。
- **Changed constraint:** 论文面对的约束由摘要和全文共同限定为：Large language model agents have shown promising capabilities in data-driven scientific discovery tasks, where an agent interacts with an execution environment and produces a statistical claim. Long-horizon scientific analysis remains constrained by the lack of process supervised environments over real-world scientific data.
- **Mechanism:** exact-v1 的方法段写明：turns the process-reward formulation in Section into a three-stage post-training pipeline for scientific discovery agents. compiles scientific datasets into sandboxed task environments with task-local hidden evidence DAGs. DAG-grounded trajectory synthesis uses these environments to produce verifiable multi-turn demonstrations for SFT cold-start. then optimizes the policy with turn-level credit from environment-verified scientific progress. The task-local hidden evidence DAG is the shared interface across these stages: it defines what can be synthesized, what counts as an accepted transition during online interaction, and how progress is credited during RL.
- **State ownership:** 需要显式绑定 rollout/reward/advantage state；canonical owner 是 `TRAIN-GRPO`，而不是论文应用领域本身。
- **Control / data flow:** 数据由工作负载进入机制实现，post-training loop 决定是否执行、路由、提交或回退；输出必须携带与输入同一版本域的证据。
- **Implementation surface:** 全文 locator=`Methodology; papers/2026/08/_sources/arxiv-owner-replay-20260903/20260803/exact-v1-text/2607.28990v1.txt`；公开实现、硬件或训练配置只按正文披露解释，未披露字段不补写。
- **Evaluation contract:** The experiments evaluate whether SciDisco improves data-driven scientific discovery and executable scientific data analysis. The evaluation covers three benchmark regimes: hypothesis generation over scientific datasets, multi-step business data analysis, and programmatically checked data-science workflows. 该结果只绑定论文声明的数据、模型、硬件、精度、长度、batch/concurrency 与 evaluator；缺失字段均为 `Not Disclosed`。
- **Proves / does not prove:** 证据支持该受限 workload 中机制可行或暴露既有评价缺口；不证明跨模型、跨硬件、跨领域或生产 SLO 的普遍优势。
- **Trade-off / failure mode:** 新增状态、控制器和观测提高可验证性，但引入版本错配、额外延迟/内存/通信、错误路由及 evaluator bias。全文边界：We presented SciDisco, a framework for training data-driven scientific discovery agents in process-verifiable environments. Hidden evidence DAGs and verifier checks make intermediate analytical progress trainable, while SciTh‘eque compiles scientific datasets and hypothesis templates into sandboxed environments shared by DAG-grounded synthesis and DiscoPO. Evaluation results support SciDisco as a scalable pipeline for converting verified analytical evidence into process supervision.
- **Coexistence / evolution:** 旧方案在低风险、短状态或同构部署中仍成立；新机制只在约束变化使错误代价或状态漂移不可忽略时接手。
- **Books route:** 对照 `TRAIN-GRPO` 及相邻章节；先进入按日期排序的 writeback queue，根任务合并同 owner 后决定最终写回。
<!-- review:SF-2026-ARXIV-2607-28990:end -->

<!-- review:SF-2026-ARXIV-2607-28991:start -->
### CAER: Conflict-Aware Evidence Routing with Dual Prefix Experts for Multimodal Large Language Models

- **Status / Evidence:** Experimental；exact-v1 HTML 已读取并保存校验和；Score V2=`6`。
- **Problem / old solution:** 既有路径通常把 cross-modal evidence alignment 隐含在模型调用或离线平均指标中；在较小规模、单一模型或无跨请求状态时成本较低，但难以回答谁拥有失败恢复与版本一致性。
- **Changed constraint:** 论文面对的约束由摘要和全文共同限定为：Multimodal Large Language Models (MLLMs) have demonstrated remarkable capabilities in multimodal understanding and generation. However, when textual inputs conflict with visual evidence, they still suffer from hallucinations and produce responses inconsistent with visual content.
- **Mechanism:** exact-v1 的方法段写明：Given an image–text pair , CAER aims to determine whether the textual claim is supported by visual evidence or contains a conflict with the observed image, and subsequently generate a response conditioned on the detected conflict status. We define the conflict status label as , where represents visually supported inputs and represents conflicting inputs requiring correction. As illustrated in Figure , CAER consists of a trainable Conflict-Aware Evidence Router and two status-specialized prefix experts built upon a frozen vision-language backbone. Given an input image, the frozen backbone extracts projected visual tokens , while the textual claim is tokenized and mapped into language-space embeddings . Differen…
- **State ownership:** 需要显式绑定 modality, timestamp and representation identity；canonical owner 是 `MULTIMODAL-REPRESENTATION`，而不是论文应用领域本身。
- **Control / data flow:** 数据由工作负载进入机制实现，fusion/evidence router 决定是否执行、路由、提交或回退；输出必须携带与输入同一版本域的证据。
- **Implementation surface:** 全文 locator=`Framework Formulation; papers/2026/08/_sources/arxiv-owner-replay-20260903/20260803/exact-v1-text/2607.28991v1.txt`；公开实现、硬件或训练配置只按正文披露解释，未披露字段不补写。
- **Evaluation contract:** Although recent open-source MLLMs have achieved remarkable progress in multimodal understanding and reasoning, their ability to handle cases where textual inputs contain false presuppositions that conflict with visual evidence remains underexplored. To investigate this limitation, we conduct a preliminary analysis of representative open-source MLLMs on vision-language conflict scenarios. Specifically, we analyze their response behaviors under conflicting inputs, including whether they can identify false presuppositions, rely on visual evidence, and maintain consistent responses across paired conflict and non-conflict settings. 该结果只绑定论文声明的数据、模型、硬件、精度、长度、batch/concurrency 与 evaluator；缺失字段均为 `Not Disclosed`。
- **Proves / does not prove:** 证据支持该受限 workload 中机制可行或暴露既有评价缺口；不证明跨模型、跨硬件、跨领域或生产 SLO 的普遍优势。
- **Trade-off / failure mode:** 新增状态、控制器和观测提高可验证性，但引入版本错配、额外延迟/内存/通信、错误路由及 evaluator bias。全文边界：In this work, we study vision-language conflict handling in MLLMs, where textual inputs may contain false assumptions inconsistent with visual evidence. We propose CAER, a backbone-agnostic framework that introduces a span-grounded evidence router to associate conflict-related claims with visual evidence and a dual prefix expert routing mechanism for status-conditioned generation while keeping MLLMs frozen. Extensive experiments on the MMMC benchmark and our newly constructed AgriConflict dataset demonstrate that CAER improves conflict detection and correction across open-source MLLMs with fewer trainable parameters and lower optimization costs than full parameter adaptation approaches.
- **Coexistence / evolution:** 旧方案在低风险、短状态或同构部署中仍成立；新机制只在约束变化使错误代价或状态漂移不可忽略时接手。
- **Books route:** 对照 `MULTIMODAL-REPRESENTATION` 及相邻章节；先进入按日期排序的 writeback queue，根任务合并同 owner 后决定最终写回。
<!-- review:SF-2026-ARXIV-2607-28991:end -->

<!-- review:SF-2026-ARXIV-2607-28993:start -->
### ST-WAM: Semantic-Temporal World Action Model for Robust Manipulation under Visual Distribution Shifts

- **Status / Evidence:** Experimental；exact-v1 HTML 已读取并保存校验和；Score V2=`7`。
- **Problem / old solution:** 既有路径通常把 action-conditioned transition 隐含在模型调用或离线平均指标中；在较小规模、单一模型或无跨请求状态时成本较低，但难以回答谁拥有失败恢复与版本一致性。
- **Changed constraint:** 论文面对的约束由摘要和全文共同限定为：World Action Models (WAMs) have emerged as a promising paradigm by jointly modeling robot actions and future visual dynamics. However, their reliance on pixel-generative future supervision can entangle action-relevant state transitions with task-irrelevant visual content, limiting robustness under visual distribution shifts.
- **Mechanism:** exact-v1 的方法段写明：To investigate this question, we analyze two representative video-generative WAMs. As illustrated in Fig. (a), when LingBot-VA and Fast-WAM-Joint , both trained only on LIBERO, are evaluated zero-shot on LIBERO-Plus, their predicted videos progressively drift toward LIBERO-style content under perturbations to background textures, illumination, and other scene characteristics. We refer to this phenomenon as : when the current observation deviates from the training distribution, the predicted future hallucinates training-domain content rather than remaining faithful to the current scene. To assess its prevalence, we manually audit the predicted futures of both models on 30 randomly sampled cases under each of th…
- **State ownership:** 需要显式绑定 latent environment and rollout state；canonical owner 是 `MULTIMODAL-WORLD-MODELS`，而不是论文应用领域本身。
- **Control / data flow:** 数据由工作负载进入机制实现，world-model loop 决定是否执行、路由、提交或回退；输出必须携带与输入同一版本域的证据。
- **Implementation surface:** 全文 locator=`full-text paragraph 3; papers/2026/08/_sources/arxiv-owner-replay-20260903/20260803/exact-v1-text/2607.28993v1.txt`；公开实现、硬件或训练配置只按正文披露解释，未披露字段不补写。
- **Evaluation contract:** We evaluate in-distribution manipulation performance on the four LIBERO suites : Spatial, Object, Goal, and Long, covering 40 tasks with 50 evaluation rollouts per task. For out-of-distribution evaluation, we directly evaluate the LIBERO-trained policy on LIBERO-Plus without fine-tuning, which comprises 10,030 test cases spanning seven perturbation dimensions. We additionally evaluate bimanual manipulation on RoboTwin 2.0 and ST-WAM is trained on a mixture of 2,500 clean and 25,000 heavily randomized demonstrations and each task is evaluated over 100 trials in both clean and randomized settings. 该结果只绑定论文声明的数据、模型、硬件、精度、长度、batch/concurrency 与 evaluator；缺失字段均为 `Not Disclosed`。
- **Proves / does not prove:** 证据支持该受限 workload 中机制可行或暴露既有评价缺口；不证明跨模型、跨硬件、跨领域或生产 SLO 的普遍优势。
- **Trade-off / failure mode:** 新增状态、控制器和观测提高可验证性，但引入版本错配、额外延迟/内存/通信、错误路由及 evaluator bias。全文边界：Beyond pixel-generative objectives, recent works explore semantic or spatially structured future representations. Some methods predict semantic masks , while others model geometric-semantic cues, spatial value maps, or compact latent conditions . LDA-1B and LaWAM model future states directly in DINO feature space, but rely on large-scale embodied pretraining and multi-stage training. In contrast, ST-WAM retains fine-grained VAE dynamics while incorporating both DINOv3 future supervision and DINO-based history retrieval within an end-to-end WAM, achieving competitive performance without embodied pretraining.
- **Coexistence / evolution:** 旧方案在低风险、短状态或同构部署中仍成立；新机制只在约束变化使错误代价或状态漂移不可忽略时接手。
- **Books route:** 对照 `MULTIMODAL-WORLD-MODELS` 及相邻章节；先进入按日期排序的 writeback queue，根任务合并同 owner 后决定最终写回。
<!-- review:SF-2026-ARXIV-2607-28993:end -->

<!-- review:SF-2026-ARXIV-2607-29032:start -->
### TransMem: Transforming Hidden States into Memory for Large Language Models

- **Status / Evidence:** Experimental；exact-v1 HTML 已读取并保存校验和；Score V2=`7`。
- **Problem / old solution:** 既有路径通常把 persistent or derived memory 隐含在模型调用或离线平均指标中；在较小规模、单一模型或无跨请求状态时成本较低，但难以回答谁拥有失败恢复与版本一致性。
- **Changed constraint:** 论文面对的约束由摘要和全文共同限定为：Large language model (LLM) agents increasingly operate over long interaction histories, where effective reasoning requires identifying and exploiting task-relevant evidence distributed across past observations and actions. However, useful information encoded in previously computed representations is often underutilized during subsequent generation.
- **Mechanism:** exact-v1 的方法段写明：In this section, we present the TransMem framework, including its inference and training procedures. Figure provides an overview of the framework. During inference, the frozen backbone performs its standard forward computation, while TransMem abstracts a small set of historical hidden states into a memory shift. This shift influences current output hidden states to better preserve key information from long contexts. We train TransMem through self-distillation to recover the predictive distribution of a teacher model conditioned on gold evidence, enabling the memory module to preserve crucial information while suppressing contextual noise.
- **State ownership:** 需要显式绑定 memory provenance, version and read/write boundary；canonical owner 是 `AGENT-MEMORY`，而不是论文应用领域本身。
- **Control / data flow:** 数据由工作负载进入机制实现，agent memory manager 决定是否执行、路由、提交或回退；输出必须携带与输入同一版本域的证据。
- **Implementation surface:** 全文 locator=`Method; papers/2026/08/_sources/arxiv-owner-replay-20260903/20260803/exact-v1-text/2607.29032v1.txt`；公开实现、硬件或训练配置只按正文披露解释，未披露字段不补写。
- **Evaluation contract:** We evaluate both general reasoning ability and memory effectiveness. We evaluate multi-hop question answering performance on the HotpotQA test set , which assesses multi-hop reasoning. Memory effectiveness is evaluated on LoCoMo and MemoryAgentBench , which measure the retention, retrieval, and use of information over extended interaction histories. LoCoMo contains contexts with an average length of approximately 16K tokens, making it suitable for evaluating long-context reasoning capabilities. In contrast, MemoryAgentBench includes many scenarios with context lengths exceeding 256K tokens, providing a more challenging evaluation of latent-space memory utilization. Following mem0 , we exclude the adversarial q… 该结果只绑定论文声明的数据、模型、硬件、精度、长度、batch/concurrency 与 evaluator；缺失字段均为 `Not Disclosed`。
- **Proves / does not prove:** 证据支持该受限 workload 中机制可行或暴露既有评价缺口；不证明跨模型、跨硬件、跨领域或生产 SLO 的普遍优势。
- **Trade-off / failure mode:** 新增状态、控制器和观测提高可验证性，但引入版本错配、额外延迟/内存/通信、错误路由及 evaluator bias。全文边界：We propose TransMem, a lightweight parametric memory module that improves test-time long-context reasoning without explicit memory construction or backbone scaling. TransMem transforms sparse, position-sensitive historical hidden states into reusable memory representations and injects them into current reasoning. Evidence-conditioned self-distillation trains the module to recover an evidence-only teacher’s predictions from full contexts. Experiments on LoCoMo, MemoryAgentBench, and HotpotQA show consistent gains across backbones with sparse memory representations and context-independent overhead, supporting efficient decoupling of memory capability from backbone reasoning capacity. Future work will explore ada…
- **Coexistence / evolution:** 旧方案在低风险、短状态或同构部署中仍成立；新机制只在约束变化使错误代价或状态漂移不可忽略时接手。
- **Books route:** 对照 `AGENT-MEMORY` 及相邻章节；先进入按日期排序的 writeback queue，根任务合并同 owner 后决定最终写回。
<!-- review:SF-2026-ARXIV-2607-29032:end -->

<!-- review:SF-2026-ARXIV-2607-29053:start -->
### Who Wins Where? Conformal Model Comparison for Local Superiority

- **Status / Evidence:** Experimental；exact-v1 HTML 已读取并保存校验和；Score V2=`7`。
- **Problem / old solution:** 既有路径通常把 evaluation evidence and release decision 隐含在模型调用或离线平均指标中；在较小规模、单一模型或无跨请求状态时成本较低，但难以回答谁拥有失败恢复与版本一致性。
- **Changed constraint:** 论文面对的约束由摘要和全文共同限定为：Standard model comparison is global, aggregating losses across the covariate space to declare a single winner. This can obscure heterogeneous performance, where different models are preferable in different regions.
- **Mechanism:** exact-v1 的方法段写明：This paper studies . Rather than asking which model wins on average over the full distribution, we ask which model is superior near a target covariate value . Our primary estimand is the conditional mean comparison score , such as the difference between two squared losses, where negative values favor model and positive values favor model . This induces a local best-model map over the feature space. A finite-radius neighborhood average of the mean score provides a stable local smoothing target, and two additional summaries—a local majority notion and a local quantile notion—serve as secondary descriptors of local agreement. The main statistical development, however, focuses on local expected superiority.
- **State ownership:** 需要显式绑定 evaluator configuration, dataset slice and result provenance；canonical owner 是 `PLATFORM-EVALUATION-SYSTEM`，而不是论文应用领域本身。
- **Control / data flow:** 数据由工作负载进入机制实现，evaluation controller 决定是否执行、路由、提交或回退；输出必须携带与输入同一版本域的证据。
- **Implementation surface:** 全文 locator=`full-text paragraph 3; papers/2026/08/_sources/arxiv-owner-replay-20260903/20260803/exact-v1-text/2607.29053v1.txt`；公开实现、硬件或训练配置只按正文披露解释，未披露字段不补写。
- **Evaluation contract:** We validate our approach on synthetic and real-world datasets. The synthetic experiments serve three purposes. First, they test whether local comparison can recover heterogeneous winner regions, as formalized in Proposition . Second, they test whether conformal calibration converts local evidence into statistically reliable winner declarations, as guaranteed by Proposition . Third, they provide diagnostics for the asymptotic and bias–variance mechanisms in Theorem and Proposition . The real-data experiments, reported in Section , evaluate whether the conformal declarations select regions with positive realized gain when the oracle local winner map is unavailable. 该结果只绑定论文声明的数据、模型、硬件、精度、长度、batch/concurrency 与 evaluator；缺失字段均为 `Not Disclosed`。
- **Proves / does not prove:** 证据支持该受限 workload 中机制可行或暴露既有评价缺口；不证明跨模型、跨硬件、跨领域或生产 SLO 的普遍优势。
- **Trade-off / failure mode:** 新增状态、控制器和观测提高可验证性，但引入版本错配、额外延迟/内存/通信、错误路由及 evaluator bias。全文边界：We presented a novel localized framework for comparing predictive models: the conformalized conditional mean comparison score. To rigorously ground this methodology, we established three core theoretical properties: the asymptotic consistency of local winner estimation, the formal disconnect between global aggregate metrics and local superiority prevalence, and an ex-ante bias-variance decomposition that explicitly explains the mechanical emergence of local advantages. Our empirical experiments validate these theoretical claims, demonstrating the framework’s capacity to detect heterogeneous model performance where global metrics fail.
- **Coexistence / evolution:** 旧方案在低风险、短状态或同构部署中仍成立；新机制只在约束变化使错误代价或状态漂移不可忽略时接手。
- **Books route:** 对照 `PLATFORM-EVALUATION-SYSTEM` 及相邻章节；先进入按日期排序的 writeback queue，根任务合并同 owner 后决定最终写回。
<!-- review:SF-2026-ARXIV-2607-29053:end -->

<!-- review:SF-2026-ARXIV-2607-29065:start -->
### Tokenizer-Agnostic Engram Module

- **Status / Evidence:** Experimental；exact-v1 HTML 已读取并保存校验和；Score V2=`6`。
- **Problem / old solution:** 既有路径通常把 token/state encoding 隐含在模型调用或离线平均指标中；在较小规模、单一模型或无跨请求状态时成本较低，但难以回答谁拥有失败恢复与版本一致性。
- **Changed constraint:** 论文面对的约束由摘要和全文共同限定为：Deepseek's Engram, a conditional memory module, was introduced to trade-off storage versus reasoning in large language models. However, the module relies on token-level $N$-gram hashing for Engram embedding lookup, introducing a tight coupling to the tokenizer used: a model with a different tokenizer would have to train its own Engram embeddings from scratch.
- **Mechanism:** exact-v1 的方法段写明：Tokenizers may share the same algorithm, e.g., Byte-Pair Encoding (BPE) or Unigram , but may differ in their vocabulary set and size, resulting in different token sequence inputs. Each token has a corresponding initial hash value with the final hash key(s) being an aggregation of these token hashes in a rolling XOR-wise manner. This causes a tight coupling between the Engram embeddings to the tokenizer used. To share Engram embeddings across different models, they must use the same tokenizer. Model performance scales with tokenizer vocabulary size , so being able to adjust the tokenizer, with respect to model size or architecture, is an important consideration. For models with fewer parameters, a fixed tokeniz…
- **State ownership:** 需要显式绑定 token identity and learned memory code；canonical owner 是 `MODEL-TOKENIZER`，而不是论文应用领域本身。
- **Control / data flow:** 数据由工作负载进入机制实现，model input interface 决定是否执行、路由、提交或回退；输出必须携带与输入同一版本域的证据。
- **Implementation surface:** 全文 locator=`full-text paragraph 3; papers/2026/08/_sources/arxiv-owner-replay-20260903/20260803/exact-v1-text/2607.29065v1.txt`；公开实现、硬件或训练配置只按正文披露解释，未披露字段不补写。
- **Evaluation contract:** We use several popular benchmarks, from EleutherAI’s , that are commonly-used for pretraining evaluation: ARC , BoolQ , COPA , HellaSwag , LAMBADA , PIQA , SCIQ , and Winogrande . When possible, for these multiple-choice question benchmarks, we use length-normalized accuracy () instead of accuracy (). For aggregation across benchmarks, we report the of all accuracy and accuracy norm values together. Finally, as we will be comparing across tokenizers, we report of benchmark . 该结果只绑定论文声明的数据、模型、硬件、精度、长度、batch/concurrency 与 evaluator；缺失字段均为 `Not Disclosed`。
- **Proves / does not prove:** 证据支持该受限 workload 中机制可行或暴露既有评价缺口；不证明跨模型、跨硬件、跨领域或生产 SLO 的普遍优势。
- **Trade-off / failure mode:** 新增状态、控制器和观测提高可验证性，但引入版本错配、额外延迟/内存/通信、错误路由及 evaluator bias。全文边界：From this empirical experiment, we can conclude that Engram modules are useful in both Engram models. The inclusion of -gram does not seem to negatively impact training, which we will again verify in our subsequent ablation. The key benefit of modelling disjoint embedding spaces allows us to designate the proportion of embedding parameters to specific , controlling the importance of specific . A larger proportion assigned will decrease the chances of hash collision for that specific -gram. Our experiment assumed equal proportion. The context-aware SPDA mechanism, in the Engram module, serves to gate these collisions. Hence, collisions across may not matter as much or are mitigated by using the complete embeddi…
- **Coexistence / evolution:** 旧方案在低风险、短状态或同构部署中仍成立；新机制只在约束变化使错误代价或状态漂移不可忽略时接手。
- **Books route:** 对照 `MODEL-TOKENIZER` 及相邻章节；先进入按日期排序的 writeback queue，根任务合并同 owner 后决定最终写回。
<!-- review:SF-2026-ARXIV-2607-29065:end -->

<!-- review:SF-2026-ARXIV-2607-29069:start -->
### Rethinking AI Cloud Infrastructure for Agentic Serving Systems with the Aries Experimentation Framework

- **Status / Evidence:** Experimental；exact-v1 HTML 已读取并保存校验和；Score V2=`8`。
- **Problem / old solution:** 既有路径通常把 persistent agent runtime 隐含在模型调用或离线平均指标中；在较小规模、单一模型或无跨请求状态时成本较低，但难以回答谁拥有失败恢复与版本一致性。
- **Changed constraint:** 论文面对的约束由摘要和全文共同限定为：Autonomous agents challenge conventional LLM serving by coupling repeated inference with persistent context and sandboxed tool execution. We present Aries, a full-stack experimentation framework that separates task semantics from execution configurations, reconstructs cross-component agent trajectories with correlated system telemetry, and exposes stateful tool execution through a consistent interface across heterogeneous san…
- **Mechanism:** exact-v1 的方法段写明：Autonomous agents challenge conventional LLM serving by coupling repeated inference with persistent context and sandboxed tool execution. We present Aries, a full-stack experimentation framework that separates task semantics from execution configurations, reconstructs cross-component agent trajectories with correlated system telemetry, and exposes stateful tool execution through a consistent interface across heterogeneous sandbox substrates. We use Aries to conduct reproducible experiments on open agent harnesses and benchmarks. We complement these experiments with production traces from a commercial platform, grounding low-level systems research in observed production behavior. Our results show that (1) token…
- **State ownership:** 需要显式绑定 agent/version/session state；canonical owner 是 `AGENT-PLATFORM`，而不是论文应用领域本身。
- **Control / data flow:** 数据由工作负载进入机制实现，agent control plane 决定是否执行、路由、提交或回退；输出必须携带与输入同一版本域的证据。
- **Implementation surface:** 全文 locator=`Rethinking AI Cloud Infrastructure for Agentic Serving Systems with the Aries Experimentation Framework; papers/2026/08/_sources/arxiv-owner-replay-20260903/20260803/exact-v1-text/2607.29069v1.txt`；公开实现、硬件或训练配置只按正文披露解释，未披露字段不补写。
- **Evaluation contract:** Autonomous agents challenge conventional LLM serving by coupling repeated inference with persistent context and sandboxed tool execution. We present Aries, a full-stack experimentation framework that separates task semantics from execution configurations, reconstructs cross-component agent trajectories with correlated system telemetry, and exposes stateful tool execution through a consistent interface across heterogeneous sandbox substrates. We use Aries to conduct reproducible experiments on open agent harnesses and benchmarks. We complement these experiments with production traces from a commercial platform, grounding low-level systems research in observed production behavior. Our results show that (1) token… 该结果只绑定论文声明的数据、模型、硬件、精度、长度、batch/concurrency 与 evaluator；缺失字段均为 `Not Disclosed`。
- **Proves / does not prove:** 证据支持该受限 workload 中机制可行或暴露既有评价缺口；不证明跨模型、跨硬件、跨领域或生产 SLO 的普遍优势。
- **Trade-off / failure mode:** 新增状态、控制器和观测提高可验证性，但引入版本错配、额外延迟/内存/通信、错误路由及 evaluator bias。全文边界：Existing benchmarks answer complementary questions at incompatible granularities. Capability-oriented benchmarks evaluate whether an agent completes a realistic task, but largely treat the execution path as a black box . Systems benchmarks can measure end-to-end performance and resource behavior, but typically consider individual requests or transactions as their unit of analysis . None of the prior frameworks and benchmarks reveal how system behavior affects progress within a multi-step agent task. Task semantics are often entangled with harness- and runtime-specific choices, execution events remain fragmented across model, harness, and sandbox components, and stateful tool behavior depends on the underlying…
- **Coexistence / evolution:** 旧方案在低风险、短状态或同构部署中仍成立；新机制只在约束变化使错误代价或状态漂移不可忽略时接手。
- **Books route:** 对照 `AGENT-PLATFORM` 及相邻章节；先进入按日期排序的 writeback queue，根任务合并同 owner 后决定最终写回。
<!-- review:SF-2026-ARXIV-2607-29069:end -->

<!-- review:SF-2026-ARXIV-2607-29071:start -->
### Federated Foundation Models Fine-Tuning with Heterogeneous Compressed Clients

- **Status / Evidence:** Experimental；exact-v1 HTML 已读取并保存校验和；Score V2=`6`。
- **Problem / old solution:** 既有路径通常把 distributed update execution 隐含在模型调用或离线平均指标中；在较小规模、单一模型或无跨请求状态时成本较低，但难以回答谁拥有失败恢复与版本一致性。
- **Changed constraint:** 论文面对的约束由摘要和全文共同限定为：Federated learning of foundation models faces a fundamental resource-asymmetry challenge: the institutions holding the most valuable domain-specific data cannot host billion-parameter models. Existing heterogeneous federated approaches attempt to bridge this gap through parameter-efficient tuning, model pruning, or knowledge distillation, yet each trades away a critical property, whether full-model memory reduction, architect…
- **Mechanism:** exact-v1 的方法段写明：Federated learning (FL) offers a principled solution by enabling multiple participants to collaboratively train a shared model without exposing raw data. Yet applying FL to billion-parameter FMs exposes a : the institutions that hold the most valuable domain-specific data (hospitals, financial firms, and enterprise departments) often operate under GPU memory budgets that preclude hosting or fine-tuning the full model. This paradox is not merely an engineering inconvenience; it creates a fundamental tension between (each client must run a self-contained model) and (heterogeneous client updates must be fusible into a coherent global model). Existing approaches to heterogeneous FL, while effective in their respec…
- **State ownership:** 需要显式绑定 optimizer/collective/compression state；canonical owner 是 `TRAIN-DISTRIBUTED-TRAINING`，而不是论文应用领域本身。
- **Control / data flow:** 数据由工作负载进入机制实现，training runtime 决定是否执行、路由、提交或回退；输出必须携带与输入同一版本域的证据。
- **Implementation surface:** 全文 locator=`full-text paragraph 3; papers/2026/08/_sources/arxiv-owner-replay-20260903/20260803/exact-v1-text/2607.29071v1.txt`；公开实现、硬件或训练配置只按正文披露解释，未披露字段不补写。
- **Evaluation contract:** All experiments are conducted on a single server equipped with 8 NVIDIA L20 GPUs (48 GB). All methods use AdamW with weight decay , learning rate , a linear warmup over steps, and gradient clipping at -norm 1. Each client trains for 1 local epoch per round with batch size 2, gradient accumulation over 4 steps (effective batch size 8), and maximum sequence length 256. For 13B experiments we reduce the learning rate to , lower the per-device batch size to 1, and increase gradient accumulation to 8. We enable gradient checkpointing () and use 8-bit AdamW to reduce peak GPU memory. Computations are in bfloat16 where supported, falling back to float16 otherwise. 该结果只绑定论文声明的数据、模型、硬件、精度、长度、batch/concurrency 与 evaluator；缺失字段均为 `Not Disclosed`。
- **Proves / does not prove:** 证据支持该受限 workload 中机制可行或暴露既有评价缺口；不证明跨模型、跨硬件、跨领域或生产 SLO 的普遍优势。
- **Trade-off / failure mode:** 新增状态、控制器和观测提高可验证性，但引入版本错配、额外延迟/内存/通信、错误路由及 evaluator bias。全文边界：Have a free development cycle? Help support accessibility at arXiv! Our collaborators at LaTeXML maintain a , and welcome .
- **Coexistence / evolution:** 旧方案在低风险、短状态或同构部署中仍成立；新机制只在约束变化使错误代价或状态漂移不可忽略时接手。
- **Books route:** 对照 `TRAIN-DISTRIBUTED-TRAINING` 及相邻章节；先进入按日期排序的 writeback queue，根任务合并同 owner 后决定最终写回。
<!-- review:SF-2026-ARXIV-2607-29071:end -->

<!-- review:SF-2026-ARXIV-2607-29076:start -->
### Selective KV Cache Protection for Noise-Resilient LLM Inference on Analog Compute-In-Memory Systems

- **Status / Evidence:** Experimental；exact-v1 HTML 已读取并保存校验和；Score V2=`9`。
- **Problem / old solution:** 既有路径通常把 decode-state compression or translation 隐含在模型调用或离线平均指标中；在较小规模、单一模型或无跨请求状态时成本较低，但难以回答谁拥有失败恢复与版本一致性。
- **Changed constraint:** 论文面对的约束由摘要和全文共同限定为：Analog compute-in-memory (CIM) arrays have emerged as a promising substrate for energy-efficient LLM inference, particularly for weight-stationary computations in linear layers. However, extending analog CIM to attention mechanisms introduces a fundamental challenge: KV cache operations demand repeated in-situ weight updates, and the resulting mismatch with the weight-stationary paradigm exposes dynamic computations to signif…
- **Mechanism:** exact-v1 的方法段写明：Figure maps the GoS dataflow to a hybrid analog–digital CIM accelerator. The architecture implements three mechanisms required by Eqs. ()–(): ownership metadata for token routing, dual-path score generation, and positional score merging followed by softmax. The static projection matrices , , and are stored in weight-stationary analog CIM arrays. For each input token, the projection arrays generate , , and through analog MVMs. These arrays are programmed once at model deployment and remain stationary during inference, so they do not incur dynamic KV-cache reprogramming overhead.
- **State ownership:** 需要显式绑定 layer/head/token KV identity；canonical owner 是 `INFER-KV-CACHE`，而不是论文应用领域本身。
- **Control / data flow:** 数据由工作负载进入机制实现，cache manager 决定是否执行、路由、提交或回退；输出必须携带与输入同一版本域的证据。
- **Implementation surface:** 全文 locator=`Hardware Architecture; papers/2026/08/_sources/arxiv-owner-replay-20260903/20260803/exact-v1-text/2607.29076v1.txt`；公开实现、硬件或训练配置只按正文披露解释，未披露字段不补写。
- **Evaluation contract:** Attention exhibits the well-known attention-sink phenomenon : the token attracts disproportionately large attention across positions and layers. Since the softmax operator must allocate probability mass even when no key is strongly relevant, models often route excess mass to this semantically neutral token. Consequently, corruption of the key can affect all queries globally. Figure illustrates this vulnerability. Clean attention shows strong dominance and structured diagonal patterns, whereas KV-noisy attention collapses toward a flatter distribution because analog noise randomizes key vectors and weakens pre-softmax score contrast. This reveals three sensitivity tiers: sink tokens, whose corruption has global… 该结果只绑定论文声明的数据、模型、硬件、精度、长度、batch/concurrency 与 evaluator；缺失字段均为 `Not Disclosed`。
- **Proves / does not prove:** 证据支持该受限 workload 中机制可行或暴露既有评价缺口；不证明跨模型、跨硬件、跨领域或生产 SLO 的普遍优势。
- **Trade-off / failure mode:** 新增状态、控制器和观测提高可验证性，但引入版本错配、额外延迟/内存/通信、错误路由及 evaluator bias。全文边界：The measured chip data calibrate the noise kernel, but the evaluated LLMs are not executed end to end on that prototype. The model captures the measured error distribution and held-out agreement. The default , , and migration threshold are fixed for the reported configuration; their best values may change with model architecture, device characteristics, or service-level constraints. GoS protects dynamic KV storage but deliberately retains projection-array error, and its bounded on-chip digital footprint does not remove HBM traffic for cold long-context tiles. Finally, the reported energy, latency, and PPA values are design estimates under the stated organization rather than measurements from a fabricated full-…
- **Coexistence / evolution:** 旧方案在低风险、短状态或同构部署中仍成立；新机制只在约束变化使错误代价或状态漂移不可忽略时接手。
- **Books route:** 对照 `INFER-KV-CACHE` 及相邻章节；先进入按日期排序的 writeback queue，根任务合并同 owner 后决定最终写回。
<!-- review:SF-2026-ARXIV-2607-29076:end -->

<!-- review:SF-2026-ARXIV-2607-29078:start -->
### DASH-OPD: Discrepancy-Aware Switching with Hysteresis for On-Policy Distillation

- **Status / Evidence:** Experimental；exact-v1 HTML 已读取并保存校验和；Score V2=`6`。
- **Problem / old solution:** 既有路径通常把 on-policy reasoning optimization 隐含在模型调用或离线平均指标中；在较小规模、单一模型或无跨请求状态时成本较低，但难以回答谁拥有失败恢复与版本一致性。
- **Changed constraint:** 论文面对的约束由摘要和全文共同限定为：On-policy distillation (OPD) trains student models on their own rollouts to reduce exposure bias. However, in multi-turn agent scenarios, early student errors can lead a trajectory away from the teacher's familiar domain.
- **Mechanism:** exact-v1 的方法段写明：Teacher-generated turns can repair a collapsing trajectory, but excessive intervention reduces student state coverage and recreates the exposure bias. Recent agentic OPD methods seek to balance teacher and student control through rollout scheduling. As shown in , TCOD progressively expands student-controlled segments in trajectories, while Guided-OPD samples each turn’s executor randomly and gradually decays the teacher-intervention probability with training progress. These methods regulate teacher support is used, but not it is needed. The need for teacher support can vary across different trajectories of the same training step, and across different segments of the same trajectory .
- **State ownership:** 需要显式绑定 rollout/reward/advantage state；canonical owner 是 `TRAIN-GRPO`，而不是论文应用领域本身。
- **Control / data flow:** 数据由工作负载进入机制实现，post-training loop 决定是否执行、路由、提交或回退；输出必须携带与输入同一版本域的证据。
- **Implementation surface:** 全文 locator=`full-text paragraph 3; papers/2026/08/_sources/arxiv-owner-replay-20260903/20260803/exact-v1-text/2607.29078v1.txt`；公开实现、硬件或训练配置只按正文披露解释，未披露字段不补写。
- **Evaluation contract:** All distilled policies are evaluated student-only, without access to the teacher. We use eight parallel workers, temperature 0.4, top-, no top- or min- truncation, a 4,096-token response limit, a two-turn observation–action history, and seed 42. All the methods use the same evaluation configuration. 该结果只绑定论文声明的数据、模型、硬件、精度、长度、batch/concurrency 与 evaluator；缺失字段均为 `Not Disclosed`。
- **Proves / does not prove:** 证据支持该受限 workload 中机制可行或暴露既有评价缺口；不证明跨模型、跨硬件、跨领域或生产 SLO 的普遍优势。
- **Trade-off / failure mode:** 新增状态、控制器和观测提高可验证性，但引入版本错配、额外延迟/内存/通信、错误路由及 evaluator bias。全文边界：We presented DASH-OPD, an adaptive, bidirectional switching method for multi-turn OPD. It accumulates directional teacher–student discrepancy into drift and recovery evidence, then applies thresholds to decide teacher intervention and student return hysteretically. On ALFWorld, DASH-OPD attains the best success rate across all splits and student scales. It also demonstrates substantially greater training and deployment efficiency. These results show that DASH-OPD establishes a new state-of-the-art for agentic OPD.
- **Coexistence / evolution:** 旧方案在低风险、短状态或同构部署中仍成立；新机制只在约束变化使错误代价或状态漂移不可忽略时接手。
- **Books route:** 对照 `TRAIN-GRPO` 及相邻章节；先进入按日期排序的 writeback queue，根任务合并同 owner 后决定最终写回。
<!-- review:SF-2026-ARXIV-2607-29078:end -->

<!-- review:SF-2026-ARXIV-2607-29079:start -->
### Faster but Different: Diagnosing and Controlling Content Drift in Accelerated Multimodal Diffusion Language Models

- **Status / Evidence:** Experimental；exact-v1 HTML 已读取并保存校验和；Score V2=`6`。
- **Problem / old solution:** 既有路径通常把 iterative or routed generation 隐含在模型调用或离线平均指标中；在较小规模、单一模型或无跨请求状态时成本较低，但难以回答谁拥有失败恢复与版本一致性。
- **Changed constraint:** 论文面对的约束由摘要和全文共同限定为：Training-free acceleration makes diffusion-based multimodal large language models (dMLLMs) more deployable, but it may silently change generated content. We study this serving-time consistency problem on 300 real images, comparing Fast-dLLM outputs with the same model's unaccelerated outputs.
- **Mechanism:** exact-v1 的方法段写明：Unlike conventional left-to-right generation, dLLMs iteratively denoise a fully masked sequence through confidence-guided unmasking ; LLaDA-V extends this paradigm with a vision encoder. The practical appeal is undercut by slow inference and dependency violations under parallel decoding . Fast-dLLM addresses both through approximate block-wise KV caching and confidence-aware parallel decoding. Reported speedups reach an order of magnitude or more, and the confidence threshold is presented – and used in follow-up work such as VRCD – as the natural dial for trading inference speed against output quality.
- **State ownership:** 需要显式绑定 proposal/correction/sample state；canonical owner 是 `MULTIMODAL-GENERATIVE-PARADIGMS`，而不是论文应用领域本身。
- **Control / data flow:** 数据由工作负载进入机制实现，generation scheduler 决定是否执行、路由、提交或回退；输出必须携带与输入同一版本域的证据。
- **Implementation surface:** 全文 locator=`full-text paragraph 3; papers/2026/08/_sources/arxiv-owner-replay-20260903/20260803/exact-v1-text/2607.29079v1.txt`；公开实现、硬件或训练配置只按正文披露解释，未披露字段不补写。
- **Evaluation contract:** We use LLaDA-V (), an 8B-parameter dMLLM built on a LLaDA-8B language backbone with a SigLIP2-SO400M vision encoder. We draw 300 images with a fixed random seed from the MME benchmark ; RQ1 uses all 300, while the more computationally intensive mechanism, refresh, and cross-implementation studies use the same fixed 50-image subset. The primary prompt (“Please describe the image in detail.”) uses . A prompt/sample-generalization check draws 50 nonoverlapping images with seed 20260727 and uses a one-sentence prompt (length/steps 32) and fixed-schema JSON prompt (length/steps 96). An auxiliary cross-model check uses the official LaViDa checkpoint and code on the primary 50 rows and prompt, sweeping its exposed pr… 该结果只绑定论文声明的数据、模型、硬件、精度、长度、batch/concurrency 与 evaluator；缺失字段均为 `Not Disclosed`。
- **Proves / does not prove:** 证据支持该受限 workload 中机制可行或暴露既有评价缺口；不证明跨模型、跨硬件、跨领域或生产 SLO 的普遍优势。
- **Trade-off / failure mode:** 新增状态、控制器和观测提高可验证性，但引入版本错配、额外延迟/内存/通信、错误路由及 evaluator bias。全文边界：For output stability, treat KV-cache refresh interval rather than confidence threshold as the primary lever (Table ): the default gives – speedup, while conservative intervals improve reproducibility and still retain . This is not a safety control; it reproduces the baseline’s errors as well as its behavior (Section ). More generally, sweeping an exposed hyperparameter against a paired unaccelerated reference costs only a few hundred generations and should precede deployment. Table itemizes 4,930 generations (4,690 on RTX 6000 Ada; 240 A800 timing replications). RQ1 uses 300 images; costlier mechanism and generalization studies use paired 50-image subsets.
- **Coexistence / evolution:** 旧方案在低风险、短状态或同构部署中仍成立；新机制只在约束变化使错误代价或状态漂移不可忽略时接手。
- **Books route:** 对照 `MULTIMODAL-GENERATIVE-PARADIGMS` 及相邻章节；先进入按日期排序的 writeback queue，根任务合并同 owner 后决定最终写回。
<!-- review:SF-2026-ARXIV-2607-29079:end -->

<!-- review:SF-2026-ARXIV-2607-29104:start -->
### Reproducing LightMem: Naive RAG Is Just as Good for Memory Management

- **Status / Evidence:** Experimental；exact-v1 HTML 已读取并保存校验和；Score V2=`7`。
- **Problem / old solution:** 既有路径通常把 persistent or derived memory 隐含在模型调用或离线平均指标中；在较小规模、单一模型或无跨请求状态时成本较低，但难以回答谁拥有失败恢复与版本一致性。
- **Changed constraint:** 论文面对的约束由摘要和全文共同限定为：Long-term conversational agents require access to information from earlier interactions, such as a user's preferences, past requests, or previously mentioned facts. Repeatedly providing the full dialogue history can be expensive as conversations grow, so many memory approaches instead transform past interactions into compact entries that can be retrieved when needed.
- **Mechanism:** exact-v1 的方法段写明：Sparse retrievers such as BM25 rank documents using lexical overlap, while learned sparse methods such as SPLADE learn term weights and expansions. Dense retrievers encode queries and documents as vectors and rank them by semantic similarity . Hybrid and fusion methods instead combine lexical and dense signals . Because memory construction changes the wording and granularity of the indexed text, retrievers may behave differently over constructed memories and raw dialogue turns .
- **State ownership:** 需要显式绑定 memory provenance, version and read/write boundary；canonical owner 是 `AGENT-MEMORY`，而不是论文应用领域本身。
- **Control / data flow:** 数据由工作负载进入机制实现，agent memory manager 决定是否执行、路由、提交或回退；输出必须携带与输入同一版本域的证据。
- **Implementation surface:** 全文 locator=`Retrieval Methods; papers/2026/08/_sources/arxiv-owner-replay-20260903/20260803/exact-v1-text/2607.29104v1.txt`；公开实现、硬件或训练配置只按正文披露解释，未披露字段不补写。
- **Evaluation contract:** Our study reproduces the LightMem pipeline and extends its evaluation to examine memory construction and retrieval separately. Figure summarises the framework. transforms raw dialogue turns into constructed memory entries before retrieval, whereas retrieves directly from the raw turns. We first reproduce the original LightMem evaluation using its reported configurations, default retriever, and comparison baselines, and assess both answer accuracy and construction efficiency. We then fix the constructed memory store and evaluate a broader range of retrievers. Finally, we compare retrieval over constructed memories with retrieval over raw user turns under matched retrievers, retrieval depths, and answering-token… 该结果只绑定论文声明的数据、模型、硬件、精度、长度、batch/concurrency 与 evaluator；缺失字段均为 `Not Disclosed`。
- **Proves / does not prove:** 证据支持该受限 workload 中机制可行或暴露既有评价缺口；不证明跨模型、跨硬件、跨领域或生产 SLO 的普遍优势。
- **Trade-off / failure mode:** 新增状态、控制器和观测提高可验证性，但引入版本错配、额外延迟/内存/通信、错误路由及 evaluator bias。全文边界：Our reproduction recovers LightMem’s main configuration trend, although the absolute accuracy and construction-cost values differ from those originally reported. Beyond this reproduction result, our broader evaluation shows that retriever choice is a major source of variation in LightMem’s effectiveness. Stronger retrievers substantially improve performance over the same constructed memory store, while strong retrieval over raw user turns often matches or exceeds LightMem. The main lesson is not that memory construction is unnecessary, but that its value cannot be assessed independently of retrieval. Constructed memories are best viewed as a compact auxiliary representation rather than a replacement for the ra…
- **Coexistence / evolution:** 旧方案在低风险、短状态或同构部署中仍成立；新机制只在约束变化使错误代价或状态漂移不可忽略时接手。
- **Books route:** 对照 `AGENT-MEMORY` 及相邻章节；先进入按日期排序的 writeback queue，根任务合并同 owner 后决定最终写回。
<!-- review:SF-2026-ARXIV-2607-29104:end -->

<!-- review:SF-2026-ARXIV-2607-29120:start -->
### Curriculum Matters: Data-Efficient Relational PFN Pretraining with Synthetic Data

- **Status / Evidence:** Experimental；exact-v1 HTML 已读取并保存校验和；Score V2=`6`。
- **Problem / old solution:** 既有路径通常把 training evidence construction 隐含在模型调用或离线平均指标中；在较小规模、单一模型或无跨请求状态时成本较低，但难以回答谁拥有失败恢复与版本一致性。
- **Changed constraint:** 论文面对的约束由摘要和全文共同限定为：Relational Prior-Data Fitted Networks (PFNs) such as RDB-PFN approximate Bayesian inference over multi-table relational databases by pretraining on millions of synthetic tasks. We investigate three intertwined questions about this paradigm.
- **Mechanism:** exact-v1 的方法段写明：is the sole synthetic data generator. We organize experiments into seven families that collectively address Q1-Q3.
- **State ownership:** 需要显式绑定 sample lineage and acceptance state；canonical owner 是 `TRAIN-DATA`，而不是论文应用领域本身。
- **Control / data flow:** 数据由工作负载进入机制实现，data pipeline 决定是否执行、路由、提交或回退；输出必须携带与输入同一版本域的证据。
- **Implementation surface:** 全文 locator=`Methodology; papers/2026/08/_sources/arxiv-owner-replay-20260903/20260803/exact-v1-text/2607.29120v1.txt`；公开实现、硬件或训练配置只按正文披露解释，未披露字段不补写。
- **Evaluation contract:** We use the consumer architecture and training code, modifying only the synthetic data source. All other hyperparameters follow the original paper. Single-table evaluation uses 23 classification tasks from the Grinsztajn et al. benchmark; relational evaluation uses 19 tasks from RelBench and 4DBInfer . We report ROC-AUC at context sizes 64 and 1024 on the relational benchmark, and at context size 1024 on the single-table benchmark. 该结果只绑定论文声明的数据、模型、硬件、精度、长度、batch/concurrency 与 evaluator；缺失字段均为 `Not Disclosed`。
- **Proves / does not prove:** 证据支持该受限 workload 中机制可行或暴露既有评价缺口；不证明跨模型、跨硬件、跨领域或生产 SLO 的普遍优势。
- **Trade-off / failure mode:** 新增状态、控制器和观测提高可验证性，但引入版本错配、额外延迟/内存/通信、错误路由及 evaluator bias。全文边界：Using as the synthetic data source throughout, we have shown that (i) a structurally different relational synthetic generator can substitute for ’s native generator with limited loss in downstream quality, (ii) curriculum ordering is the dominant training-recipe variable, with a 16-point absolute gap on the single-table benchmark separating curriculum from all-at-once on identical data, and (iii) a single-table curriculum model already achieves nearly the same relational benchmark performance as a dedicated relational pipeline, indicating that -linearized relational tasks reduce substantially to structured tabular tasks. These findings reposition curriculum design, rather than synthetic generator identity or r…
- **Coexistence / evolution:** 旧方案在低风险、短状态或同构部署中仍成立；新机制只在约束变化使错误代价或状态漂移不可忽略时接手。
- **Books route:** 对照 `TRAIN-DATA` 及相邻章节；先进入按日期排序的 writeback queue，根任务合并同 owner 后决定最终写回。
<!-- review:SF-2026-ARXIV-2607-29120:end -->

<!-- review:SF-2026-ARXIV-2607-29125:start -->
### M3-DuplexBench: A Multi-Turn, Multilingual, Multidomain Benchmark for Full-Duplex Spoken Dialogue Models

- **Status / Evidence:** Experimental；exact-v1 HTML 已读取并保存校验和；Score V2=`7`。
- **Problem / old solution:** 既有路径通常把 evaluation evidence and release decision 隐含在模型调用或离线平均指标中；在较小规模、单一模型或无跨请求状态时成本较低，但难以回答谁拥有失败恢复与版本一致性。
- **Changed constraint:** 论文面对的约束由摘要和全文共同限定为：Full-duplex spoken dialogue systems (FDSDSs) can listen while speaking, enabling natural behaviors such as smooth turn-taking, backchannel handling, and user barge-in handling. However, fair comparisons in multi-turn conversations remain a challenge.
- **Mechanism:** exact-v1 的方法段写明：Along with the development of FDSDSs, many benchmarks have been proposed to automatically evaluate their behavior. Existing benchmarks evaluate various aspects of full-duplex dialogue, such as turn-taking , response naturalness , and instruction following . Several studies have also evaluated multi-turn conversations. For example, recent work evaluates multi-turn interaction using an automated examiner or pre-collected spoken dialogue data . These studies provide important tools for evaluating full-duplex behavior.
- **State ownership:** 需要显式绑定 evaluator configuration, dataset slice and result provenance；canonical owner 是 `PLATFORM-EVALUATION-SYSTEM`，而不是论文应用领域本身。
- **Control / data flow:** 数据由工作负载进入机制实现，evaluation controller 决定是否执行、路由、提交或回退；输出必须携带与输入同一版本域的证据。
- **Implementation surface:** 全文 locator=`full-text paragraph 3; papers/2026/08/_sources/arxiv-owner-replay-20260903/20260803/exact-v1-text/2607.29125v1.txt`；公开实现、硬件或训练配置只按正文披露解释，未披露字段不补写。
- **Evaluation contract:** Full-duplex spoken dialogue systems (FDSDSs) can listen while speaking, enabling natural behaviors such as smooth turn-taking, backchannel handling, and user barge-in handling. However, fair comparisons in multi-turn conversations remain a challenge. In addition, existing benchmarks provide limited coverage of languages and dialogue domains. We propose M3-DuplexBench, a multi-turn, multilingual, multidomain benchmark for FDSDSs. M3-DuplexBench supports English and Japanese and covers both casual conversation and multi-turn question answering. In addition, we evaluate models under multiple dialogue context settings, including single-turn, user-only, and teacher-forced full-context settings, to analyze how dialo… 该结果只绑定论文声明的数据、模型、硬件、精度、长度、batch/concurrency 与 evaluator；缺失字段均为 `Not Disclosed`。
- **Proves / does not prove:** 证据支持该受限 workload 中机制可行或暴露既有评价缺口；不证明跨模型、跨硬件、跨领域或生产 SLO 的普遍优势。
- **Trade-off / failure mode:** 新增状态、控制器和观测提高可验证性，但引入版本错配、额外延迟/内存/通信、错误路由及 evaluator bias。全文边界：Have a free development cycle? Help support accessibility at arXiv! Our collaborators at LaTeXML maintain a , and welcome .
- **Coexistence / evolution:** 旧方案在低风险、短状态或同构部署中仍成立；新机制只在约束变化使错误代价或状态漂移不可忽略时接手。
- **Books route:** 对照 `PLATFORM-EVALUATION-SYSTEM` 及相邻章节；先进入按日期排序的 writeback queue，根任务合并同 owner 后决定最终写回。
<!-- review:SF-2026-ARXIV-2607-29125:end -->

<!-- review:SF-2026-ARXIV-2607-29167:start -->
### Memory Provenance Laundering in LLM Agents: A Non-Amplification Firewall for Persistent Memory

- **Status / Evidence:** Experimental；exact-v1 HTML 已读取并保存校验和；Score V2=`7`。
- **Problem / old solution:** 既有路径通常把 persistent or derived memory 隐含在模型调用或离线平均指标中；在较小规模、单一模型或无跨请求状态时成本较低，但难以回答谁拥有失败恢复与版本一致性。
- **Changed constraint:** 论文面对的约束由摘要和全文共同限定为：Long-term memory lets large language model(LLM) agents reuse prior preferences and work flows, but it also turns untrusted observations into persistent action context. We identify memory provenance laundering: during LLM-based memory consolidation, an external observation may be rewritten as apparent user history or workflow support, preserving an action trigger while erasing the low-trust source that should limit its authori…
- **Mechanism:** exact-v1 的方法段写明：Setting Raw ASR↓ Raw benign↑ Vuln ASR↓ Launder↓ CF ASR↓ CF FB↓ PPMF ASR↓ PPMF benign↑
- **State ownership:** 需要显式绑定 memory provenance, version and read/write boundary；canonical owner 是 `AGENT-MEMORY`，而不是论文应用领域本身。
- **Control / data flow:** 数据由工作负载进入机制实现，agent memory manager 决定是否执行、路由、提交或回退；输出必须携带与输入同一版本域的证据。
- **Implementation surface:** 全文 locator=`full-text paragraph 3; papers/2026/08/_sources/arxiv-owner-replay-20260903/20260803/exact-v1-text/2607.29167v1.txt`；公开实现、硬件或训练配置只按正文披露解释，未披露字段不补写。
- **Evaluation contract:** Setting Raw ASR↓ Raw benign↑ Vuln ASR↓ Launder↓ CF ASR↓ CF FB↓ PPMF ASR↓ PPMF benign↑ 该结果只绑定论文声明的数据、模型、硬件、精度、长度、batch/concurrency 与 evaluator；缺失字段均为 `Not Disclosed`。
- **Proves / does not prove:** 证据支持该受限 workload 中机制可行或暴露既有评价缺口；不证明跨模型、跨硬件、跨领域或生产 SLO 的普遍优势。
- **Trade-off / failure mode:** 新增状态、控制器和观测提高可验证性，但引入版本错配、额外延迟/内存/通信、错误路由及 evaluator bias。全文边界：Setting Raw ASR↓ Raw benign↑ Vuln ASR↓ Launder↓ CF ASR↓ CF FB↓ PPMF ASR↓ PPMF benign↑
- **Coexistence / evolution:** 旧方案在低风险、短状态或同构部署中仍成立；新机制只在约束变化使错误代价或状态漂移不可忽略时接手。
- **Books route:** 对照 `AGENT-MEMORY` 及相邻章节；先进入按日期排序的 writeback queue，根任务合并同 owner 后决定最终写回。
<!-- review:SF-2026-ARXIV-2607-29167:end -->

<!-- review:SF-2026-ARXIV-2607-29169:start -->
### ActFovea: Runtime Safeguarding for VLA Policies via Spatiotemporal Visual-Action Consistency

- **Status / Evidence:** Experimental；exact-v1 HTML 已读取并保存校验和；Score V2=`6`。
- **Problem / old solution:** 既有路径通常把 closed-loop physical action 隐含在模型调用或离线平均指标中；在较小规模、单一模型或无跨请求状态时成本较低，但难以回答谁拥有失败恢复与版本一致性。
- **Changed constraint:** 论文面对的约束由摘要和全文共同限定为：Vision-language-action (VLA) policies achieve strong performance in robotic manipulation but remain vulnerable to runtime disturbances that break the temporal alignment among visual observations, robot states, and executed actions. We introduce ActFovea, a plug-and-play safeguarding framework that detects and mitigates such failures without retraining or modifying the underlying VLA policy.
- **Mechanism:** exact-v1 的方法段写明：Recent studies have revealed vulnerabilities across these components. Visual attacks can modify task-relevant image evidence , while SilentDrift exposes smooth intra-chunk action deviations and FreezeVLA shows that adversarial observations can induce persistent inaction . Existing runtime safeguards provide complementary but largely specialized forms of protection. Control-barrier layers enforce explicit geometric constraints, while observation interventions reduce sensitivity to visual distractors .
- **State ownership:** 需要显式绑定 sensor/action/trajectory state；canonical owner 是 `MULTIMODAL-EMBODIED-VLA`，而不是论文应用领域本身。
- **Control / data flow:** 数据由工作负载进入机制实现，policy plus safety controller 决定是否执行、路由、提交或回退；输出必须携带与输入同一版本域的证据。
- **Implementation surface:** 全文 locator=`full-text paragraph 3; papers/2026/08/_sources/arxiv-owner-replay-20260903/20260803/exact-v1-text/2607.29169v1.txt`；公开实现、硬件或训练配置只按正文披露解释，未披露字段不补写。
- **Evaluation contract:** We evaluate ActFovea with the frozen LIBERO checkpoint of on four ten-task suites: LIBERO-Spatial, LIBERO-Object, LIBERO-Goal, and LIBERO-10. Each task uses 50 episodes, yielding 2,000 episodes per method-scenario cell. All comparisons use the same checkpoint and matched task and execution configurations; ActFovea is applied only at inference time. 该结果只绑定论文声明的数据、模型、硬件、精度、长度、batch/concurrency 与 evaluator；缺失字段均为 `Not Disclosed`。
- **Proves / does not prove:** 证据支持该受限 workload 中机制可行或暴露既有评价缺口；不证明跨模型、跨硬件、跨领域或生产 SLO 的普遍优势。
- **Trade-off / failure mode:** 新增状态、控制器和观测提高可验证性，但引入版本错配、额外延迟/内存/通信、错误路由及 evaluator bias。全文边界：We presented ActFovea, a policy-interface-based runtime safeguard that treats spatial corruption, temporal misalignment, and action-trajectory drift as violations of spatiotemporal visual-action consistency. Action-conditioned foveation preserves interaction-relevant evidence, the consistency monitor determines whether recovery remains justified, and disturbance-conditioned candidate observations are verified before bounded execution, while the underlying VLA policy remains frozen throughout. When fresh perceptual grounding is lost, the same safeguarding loop transitions from recovery to safe failure. Across multiple LIBERO tasks with , ActFovea restores visual-overlay success from 49.3% to 90.3%, improves vis…
- **Coexistence / evolution:** 旧方案在低风险、短状态或同构部署中仍成立；新机制只在约束变化使错误代价或状态漂移不可忽略时接手。
- **Books route:** 对照 `MULTIMODAL-EMBODIED-VLA` 及相邻章节；先进入按日期排序的 writeback queue，根任务合并同 owner 后决定最终写回。
<!-- review:SF-2026-ARXIV-2607-29169:end -->

<!-- review:SF-2026-ARXIV-2607-29172:start -->
### CLIFT: Turning Gemini Robotics On-Device into Humanoid Specialists via Non-Invasive Closed-Loop Iterative Fine-Tuning

- **Status / Evidence:** Experimental；exact-v1 HTML 已读取并保存校验和；Score V2=`6`。
- **Problem / old solution:** 既有路径通常把 supervised adaptation 隐含在模型调用或离线平均指标中；在较小规模、单一模型或无跨请求状态时成本较低，但难以回答谁拥有失败恢复与版本一致性。
- **Changed constraint:** 论文面对的约束由摘要和全文共同限定为：While robot foundation models are growing increasingly capable, the strongest models are typically trained on proprietary data and remain closed-source, limiting downstream users' ability to adapt them to new tasks, embodiments, and deployment settings. Following the LLM community, an emerging access paradigm for closed-weight robot foundation models is the managed supervised fine-tuning (SFT) API, where users submit training…
- **Mechanism:** exact-v1 的方法段写明：As the open- versus closed-source debate continues, a middle ground has emerged: models exposed through managed adaptation interfaces. In the LLM community, SFT APIs already let users customize proprietary models without accessing their weights or training pipelines . Robot foundation VLAs are entering this regime, where base-model access matters even more, since robot data is far harder to scale than language data . Gemini Robotics On-Device (GROD) is an early example—offering managed fine-tuning while keeping the “model box” closed—and Physical Intelligence’s partner API signals the same trend. This positions closed-weight, API-exposed VLAs as an intermediate regime between fully closed systems and open-weig…
- **State ownership:** 需要显式绑定 example/adapter/checkpoint identity；canonical owner 是 `TRAIN-SFT`，而不是论文应用领域本身。
- **Control / data flow:** 数据由工作负载进入机制实现，fine-tuning loop 决定是否执行、路由、提交或回退；输出必须携带与输入同一版本域的证据。
- **Implementation surface:** 全文 locator=`full-text paragraph 3; papers/2026/08/_sources/arxiv-owner-replay-20260903/20260803/exact-v1-text/2607.29172v1.txt`；公开实现、硬件或训练配置只按正文披露解释，未披露字段不补写。
- **Evaluation contract:** We evaluate our method on a real humanoid across a diverse suite of agile, contact-rich tasks. Our experiments aim to study three questions: (1) Can our closed-loop self-improvement fine-tuning turn a API-only restricted-access foundation model into a humanoid specialist that achieves task mastery? (2) Does our pipeline generalize across different foundation models with different access regimes? (3) How does downstream performance compare between GROD and under the same self-improving fine-tuning pipeline? 该结果只绑定论文声明的数据、模型、硬件、精度、长度、batch/concurrency 与 evaluator；缺失字段均为 `Not Disclosed`。
- **Proves / does not prove:** 证据支持该受限 workload 中机制可行或暴露既有评价缺口；不证明跨模型、跨硬件、跨领域或生产 SLO 的普遍优势。
- **Trade-off / failure mode:** 新增状态、控制器和观测提高可验证性，但引入版本错配、额外延迟/内存/通信、错误路由及 evaluator bias。全文边界：While robot foundation models grow increasingly capable, the strongest are typically trained on proprietary data and exposed only through managed supervised fine-tuning (SFT) APIs—users submit training data and receive a tuned policy, with no access to model weights, gradients, or training internals. In this work, we studied how effective this managed-API regime is for humanoid adaptation, and how closed-loop improvement can be realized within it to push policies toward task mastery. We provided one of the first empirical studies of managed-API adaptation on a real humanoid, instantiated on Gemini Robotics model. Direct SFT through the API already substantially outperforms a leading open-weight VLA trained on…
- **Coexistence / evolution:** 旧方案在低风险、短状态或同构部署中仍成立；新机制只在约束变化使错误代价或状态漂移不可忽略时接手。
- **Books route:** 对照 `TRAIN-SFT` 及相邻章节；先进入按日期排序的 writeback queue，根任务合并同 owner 后决定最终写回。
<!-- review:SF-2026-ARXIV-2607-29172:end -->

<!-- review:SF-2026-ARXIV-2607-29175:start -->
### Execution-First Synthetic Tool-Use Trace Generation for LLM Agents

- **Status / Evidence:** Experimental；exact-v1 HTML 已读取并保存校验和；Score V2=`7`。
- **Problem / old solution:** 既有路径通常把 tool acquisition or authorization 隐含在模型调用或离线平均指标中；在较小规模、单一模型或无跨请求状态时成本较低，但难以回答谁拥有失败恢复与版本一致性。
- **Changed constraint:** 论文面对的约束由摘要和全文共同限定为：Agentic software-engineering and industrial systems increasingly operate through executable workflows rather than code genera- tion alone: they search artifacts, invoke tools, inspect structured observations, and query databases. Training these agents requires supervision data that captures valid tool interactions and executable workflows.
- **Mechanism:** exact-v1 的方法段写明：Despite these advances, these agents can still fail in complex, multi-step technical workflows. Common failure modes include selecting inappropriate tools , generating invalid tool arguments (e.g., incorrect parameter names or data types), failing to incorporate intermediate execution results into subsequent reasoning, and producing responses that are not fully supported by the evidence gathered during execution . These failures become particularly consequential in software engineering tasks involving artifact retrieval, programmatic tool execution, structured data access, and the orchestration of multiple API calls, where correctness depends on accurate tool use and faithful reasoning over intermediate observ…
- **State ownership:** 需要显式绑定 tool schema, capability and return provenance；canonical owner 是 `AGENT-TOOL-CALLING`，而不是论文应用领域本身。
- **Control / data flow:** 数据由工作负载进入机制实现，tool-policy controller 决定是否执行、路由、提交或回退；输出必须携带与输入同一版本域的证据。
- **Implementation surface:** 全文 locator=`full-text paragraph 3; papers/2026/08/_sources/arxiv-owner-replay-20260903/20260803/exact-v1-text/2607.29175v1.txt`；公开实现、硬件或训练配置只按正文披露解释，未披露字段不补写。
- **Evaluation contract:** Recent benchmarks for tool-augmented agents have evolved from broad API-centric evaluations toward more reproducible and production-oriented execution environments. Early efforts such as ToolLLM and API-Bank were built around diverse real-world APIs and evaluated planning, retrieval, and tool invocation through executable interactions . Subsequent work identified important reproducibility challenges, showing that benchmark performance can be affected by API drift, unstable tool availability, and complex multi-turn interactions . More recent benchmarks address these issues through virtualized APIs, simulated tool ecosystems, and controlled execution environments that better reflect long-horizon interactions and… 该结果只绑定论文声明的数据、模型、硬件、精度、长度、batch/concurrency 与 evaluator；缺失字段均为 `Not Disclosed`。
- **Proves / does not prove:** 证据支持该受限 workload 中机制可行或暴露既有评价缺口；不证明跨模型、跨硬件、跨领域或生产 SLO 的普遍优势。
- **Trade-off / failure mode:** 新增状态、控制器和观测提高可验证性，但引入版本错配、额外延迟/内存/通信、错误路由及 evaluator bias。全文边界：Our evaluation focuses on controlled tool ecosystems with fixed schemas and execution. Due to computational constraints, fine-tuning used only a subset of the generated dataset. Future work will study scaling across different training set sizes, dynamic environments with changing APIs and longer-horizon workflows, and cross-domain tool composition.
- **Coexistence / evolution:** 旧方案在低风险、短状态或同构部署中仍成立；新机制只在约束变化使错误代价或状态漂移不可忽略时接手。
- **Books route:** 对照 `AGENT-TOOL-CALLING` 及相邻章节；先进入按日期排序的 writeback queue，根任务合并同 owner 后决定最终写回。
<!-- review:SF-2026-ARXIV-2607-29175:end -->

<!-- review:SF-2026-ARXIV-2607-29185:start -->
### Learning Latent Reasoning Traces for Scalar Reward Models End-to-End

- **Status / Evidence:** Experimental；exact-v1 HTML 已读取并保存校验和；Score V2=`6`。
- **Problem / old solution:** 既有路径通常把 preference/reward optimization 隐含在模型调用或离线平均指标中；在较小规模、单一模型或无跨请求状态时成本较低，但难以回答谁拥有失败恢复与版本一致性。
- **Changed constraint:** 论文面对的约束由摘要和全文共同限定为：Reward models (RMs) are central to aligning large language models with human preferences via reinforcement learning. Although traditional scalar RMs enable efficient and probabilistic reward modeling, they rely on superficial cues that fail to generalize to complex or out-of-distribution (OOD) tasks.
- **Mechanism:** exact-v1 的方法段写明：In this paper, we introduce a generator-discriminator architecture for the reward model. In particular, the generator LLM parametrized by samples a chain-of-thought reasoning given . Then the discriminator scalar RM parametrized by outputs rewards given and . This design allows the discriminator to leverage ample evidence supporting the final decision in the reasoning, while ensuring flexible scoring that generative RMs lack. While the scalar RM may be of different architecture from the generator, we simply initialize the scalar RM as a copy of the generator with the language modeling head replaced by a scalar head randomly parametrized by . To induce a distribution over the the listwise rankings , we use Plac…
- **State ownership:** 需要显式绑定 preference, reward and policy-version state；canonical owner 是 `TRAIN-RLHF`，而不是论文应用领域本身。
- **Control / data flow:** 数据由工作负载进入机制实现，post-training controller 决定是否执行、路由、提交或回退；输出必须携带与输入同一版本域的证据。
- **Implementation surface:** 全文 locator=`Model Architecture; papers/2026/08/_sources/arxiv-owner-replay-20260903/20260803/exact-v1-text/2607.29185v1.txt`；公开实现、硬件或训练配置只按正文披露解释，未披露字段不补写。
- **Evaluation contract:** We validate LatentRM’s effectiveness on ID test set and several OOD benchmarks for evaluating reward models. In addition, we conduct RLHF experiments with LatentRM and baseline RMs to explore their utility on inducing an aligned LLM. Throughout the experiments, we use Qwen3-4B-Instruct as the backbone model across LatentRM and baselines. 该结果只绑定论文声明的数据、模型、硬件、精度、长度、batch/concurrency 与 evaluator；缺失字段均为 `Not Disclosed`。
- **Proves / does not prove:** 证据支持该受限 workload 中机制可行或暴露既有评价缺口；不证明跨模型、跨硬件、跨领域或生产 SLO 的普遍优势。
- **Trade-off / failure mode:** 新增状态、控制器和观测提高可验证性，但引入版本错配、额外延迟/内存/通信、错误路由及 evaluator bias。全文边界：In this paper, we introduce LatentRM, a scalar reward model enhanced by a reasoner that learns to shape its reasoning trace for a unified goal of maximizing the scalarRM’s likelihood of observing groundtruth preference ranking. By casting reasoning trace as a latent variable in a conditional generative model, we derive a simple and natural end-to-end procedure for training LatentRM. Extensive validations on ID and OOD datasets as well as RLHF experiments demonstrate that LatentRM achieves overall consistent improvements in preference modeling and policy alignment over a strong multi-task learning baseline, and much more clearly over scalar and generative reward models in isolation.
- **Coexistence / evolution:** 旧方案在低风险、短状态或同构部署中仍成立；新机制只在约束变化使错误代价或状态漂移不可忽略时接手。
- **Books route:** 对照 `TRAIN-RLHF` 及相邻章节；先进入按日期排序的 writeback queue，根任务合并同 owner 后决定最终写回。
<!-- review:SF-2026-ARXIV-2607-29185:end -->

<!-- review:SF-2026-ARXIV-2607-29190:start -->
### CAGE: Certified Authorization under Typed-Return Uncertainty for Tool-Using Agents

- **Status / Evidence:** Experimental；exact-v1 HTML 已读取并保存校验和；Score V2=`7`。
- **Problem / old solution:** 既有路径通常把 tool acquisition or authorization 隐含在模型调用或离线平均指标中；在较小规模、单一模型或无跨请求状态时成本较低，但难以回答谁拥有失败恢复与版本一致性。
- **Changed constraint:** 论文面对的约束由摘要和全文共同限定为：Tool-using LLM agents act on typed tool returns, records pairing provenance and categorical fields with numerical values. Runtime permission gates generally authorize the observed return and action, leaving the decision unprotected against small errors in how the return was bound to its source.
- **Mechanism:** exact-v1 的方法段写明：CAGE certifies the actual joint perturbation set: enumerate the finite discrete neighborhood exactly, run a sound per-branch test on the continuous ball at every , and allow only when every branch passes, A certified allow covers every branch under the continuous budget, up to the branch test’s stated confidence: exactly the joint budget the joint-gap attack exploits. Each branch is read as a plausible correctly bound return (TM2, Section ). The branch test comes from the assumption ladder of Section .
- **State ownership:** 需要显式绑定 tool schema, capability and return provenance；canonical owner 是 `AGENT-TOOL-CALLING`，而不是论文应用领域本身。
- **Control / data flow:** 数据由工作负载进入机制实现，tool-policy controller 决定是否执行、路由、提交或回退；输出必须携带与输入同一版本域的证据。
- **Implementation surface:** 全文 locator=`Method; papers/2026/08/_sources/arxiv-owner-replay-20260903/20260803/exact-v1-text/2607.29190v1.txt`；公开实现、硬件或训练配置只按正文披露解释，未披露字段不补写。
- **Evaluation contract:** The evaluation first establishes the existence of joint-gap witnesses (Tables –), then measures the soundness–autonomy trade-off (Table ), and finally tests whether the logical gap produces committed side effects (§). Additional experiments test whether these results depend on judge capacity, the analytic oracle, the attack strategy, policy stationarity, or the assumed budget (, freshness). The certificate covers a single decision under the declared budget (, ; §); rung 1 is policy-certified, rungs 2–3 are gate-certified under measured fidelity, and the LLM remains an uncertified proposer. Section discusses the assumptions outside this guarantee. 该结果只绑定论文声明的数据、模型、硬件、精度、长度、batch/concurrency 与 evaluator；缺失字段均为 `Not Disclosed`。
- **Proves / does not prove:** 证据支持该受限 workload 中机制可行或暴露既有评价缺口；不证明跨模型、跨硬件、跨领域或生产 SLO 的普遍优势。
- **Trade-off / failure mode:** 新增状态、控制器和观测提高可验证性，但引入版本错配、额外延迟/内存/通信、错误路由及 evaluator bias。全文边界：CAGE formulates authorization over typed tool returns as a joint-neighborhood decision. The non-composition result identifies pairs that are safe under each marginal check yet unsafe under a combined binding and numerical deviation. Across policy-engine, regulatory, and real-transaction settings, the joint certificates remove measured in-budget policy false allows while retaining useful autonomy; CAGE-Exact is policy-certified on the verified fragment, CAGE-Lip and CAGE-RS extend it to learned gates under an explicit gate–policy fidelity condition. The guarantee applies to a single authorization decision and assumes a validated typed-return constructor, complete mediation, an enumerable discrete neighborhood,…
- **Coexistence / evolution:** 旧方案在低风险、短状态或同构部署中仍成立；新机制只在约束变化使错误代价或状态漂移不可忽略时接手。
- **Books route:** 对照 `AGENT-TOOL-CALLING` 及相邻章节；先进入按日期排序的 writeback queue，根任务合并同 owner 后决定最终写回。
<!-- review:SF-2026-ARXIV-2607-29190:end -->

<!-- review:SF-2026-ARXIV-2607-29199:start -->
### Alignment Is Local: A Paired Diagnostic for GUI Agents under User-Side Persuasion

- **Status / Evidence:** Experimental；exact-v1 HTML 已读取并保存校验和；Score V2=`7`。
- **Problem / old solution:** 既有路径通常把 evaluation evidence and release decision 隐含在模型调用或离线平均指标中；在较小规模、单一模型或无跨请求状态时成本较低，但难以回答谁拥有失败恢复与版本一致性。
- **Changed constraint:** 论文面对的约束由摘要和全文共同限定为：Trustworthy deployment of GUI agents in ubiquitous computing settings requires alignment that survives dynamic interaction and precise threat conditions, not just single-turn refusal of explicit harmful requests. We argue that prompt-level alignment, the dominant lightweight defense in current mobile agents, is a local phenomenon: it works reliably only in the narrow evaluation slice where it is typically measured, namely sin…
- **Mechanism:** exact-v1 的方法段写明：Trustworthy deployment of GUI agents in ubiquitous computing settings imposes three demands that a scalar single-turn attack-success rate cannot capture. Safety must survive interaction, since an agent that refuses in isolation may accede once dialogue history accumulates. It must be , holding at every action boundary rather than only when harmful intent is explicitly named. And because a GUI agent’s outputs eventually become taps and confirmations on a real device, its pre-execution commitments, i.e., what it is willing to materially advance toward, function as a necessary gate on safety. Yet the dominant evaluation practice for GUI-agent alignment remains static, single-turn, and response-only, reporting one…
- **State ownership:** 需要显式绑定 evaluator configuration, dataset slice and result provenance；canonical owner 是 `PLATFORM-EVALUATION-SYSTEM`，而不是论文应用领域本身。
- **Control / data flow:** 数据由工作负载进入机制实现，evaluation controller 决定是否执行、路由、提交或回退；输出必须携带与输入同一版本域的证据。
- **Implementation surface:** 全文 locator=`full-text paragraph 3; papers/2026/08/_sources/arxiv-owner-replay-20260903/20260803/exact-v1-text/2607.29199v1.txt`；公开实现、硬件或训练配置只按正文披露解释，未披露字段不补写。
- **Evaluation contract:** Table gives unit-level ASR per regimedefense cell; Table decomposes the independent regime by defense and salience at the unit-level level, from which Eq. () is read; Table reports ASR, over-refusal, and robustness under the guardrail. Figure visualizes the two central effects. Three findings emerge, corresponding to the origin and the two off-axis directions of the local-alignment picture. In the independent regime, the guardrail reduces unit-level ASR on every target: Qwen3.7-Plus drops from to , GPT-5.6 Sol decreases from to , and Claude Opus 4.8 falls from to (Table ), while over-refusal on benign controls stays at most (Table ). Refusal-aware robustness (Eq. ) ranks GPT-5.6 Sol () above Claude () and Qwen… 该结果只绑定论文声明的数据、模型、硬件、精度、长度、batch/concurrency 与 evaluator；缺失字段均为 `Not Disclosed`。
- **Proves / does not prove:** 证据支持该受限 workload 中机制可行或暴露既有评价缺口；不证明跨模型、跨硬件、跨领域或生产 SLO 的普遍优势。
- **Trade-off / failure mode:** 新增状态、控制器和观测提高可验证性，但引入版本错配、额外延迟/内存/通信、错误路由及 evaluator bias。全文边界：The results are consistent with prompt-level alignment behaving as a local phenomenon: reliable in the slice where it is typically measured, and systematically weaker along the two axes any user can traverse. Two implications follow from the off-axis findings. Four-turn escalation raises guarded unit-level ASR by approximately points across all three models, although the difference-in-differences analysis attributes substantial relative guardrail erosion only to Qwen. Aggregate ASR should therefore be reported conditionally on turn structure rather than marginalized over it, and dialogue history should be treated as safety state, with intent re-evaluated at each action boundary. Single-probe and chain-level ev…
- **Coexistence / evolution:** 旧方案在低风险、短状态或同构部署中仍成立；新机制只在约束变化使错误代价或状态漂移不可忽略时接手。
- **Books route:** 对照 `PLATFORM-EVALUATION-SYSTEM` 及相邻章节；先进入按日期排序的 writeback queue，根任务合并同 owner 后决定最终写回。
<!-- review:SF-2026-ARXIV-2607-29199:end -->

<!-- review:SF-2026-ARXIV-2607-29209:start -->
### SAF-OPD: Stable Advantage Fusion for On-Policy Distillation

- **Status / Evidence:** Experimental；exact-v1 HTML 已读取并保存校验和；Score V2=`6`。
- **Problem / old solution:** 既有路径通常把 on-policy reasoning optimization 隐含在模型调用或离线平均指标中；在较小规模、单一模型或无跨请求状态时成本较低，但难以回答谁拥有失败恢复与版本一致性。
- **Changed constraint:** 论文面对的约束由摘要和全文共同限定为：Reinforcement learning with verifiable rewards (RLVR) broadcasts a single response-level reward to every token, while on-policy distillation (OPD) scores each token against a stronger teacher for a dense advantage but caps performance at teacher quality and discourages exploration beyond it. Their complementarity makes combining RLVR and OPD promising, but we find that fusing the two advantages with a fixed coefficient trigge…
- **Mechanism:** exact-v1 的方法段写明：GRPO-only, GRPO+OPD (fixed), and SAF use the same optimization and rollout configuration at a given student scale and domain; only their advantage construction differs. We optimize these methods for 300 steps on mathematics and 200 steps on code. Table lists their shared hyperparameters.
- **State ownership:** 需要显式绑定 rollout/reward/advantage state；canonical owner 是 `TRAIN-GRPO`，而不是论文应用领域本身。
- **Control / data flow:** 数据由工作负载进入机制实现，post-training loop 决定是否执行、路由、提交或回退；输出必须携带与输入同一版本域的证据。
- **Implementation surface:** 全文 locator=`GRPO-based methods.; papers/2026/08/_sources/arxiv-owner-replay-20260903/20260803/exact-v1-text/2607.29209v1.txt`；公开实现、硬件或训练配置只按正文披露解释，未披露字段不补写。
- **Evaluation contract:** We evaluate mathematical reasoning on AIME24 , AIME25 , and HMMT25 (February and November) , and code generation on HumanEval+, MBPP+ , and LiveCodeBench (v6, FebruaryMay 2025) . Math answers are validated with , and code is scored with the benchmark-provided unit tests; we report the unweighted mean per domain. Full decoding and sampling settings are in Appendix . 该结果只绑定论文声明的数据、模型、硬件、精度、长度、batch/concurrency 与 evaluator；缺失字段均为 `Not Disclosed`。
- **Proves / does not prove:** 证据支持该受限 workload 中机制可行或暴露既有评价缺口；不证明跨模型、跨硬件、跨领域或生产 SLO 的普遍优势。
- **Trade-off / failure mode:** 新增状态、控制器和观测提高可验证性，但引入版本错配、额外延迟/内存/通信、错误路由及 evaluator bias。全文边界：This paper studies how to fuse a response-level GRPO advantage with a token-level OPD advantage without either one destabilizing the other. Naive fixed-coefficient summation suffers from a magnitude mismatch, where token-level OPD advantages spike far beyond the bounded GRPO advantage, and a temporal mismatch, where the value of full-strength guidance drifts as the student converges toward the teacher. SAF addresses both via a four-stage, switchable pipeline pairing top- sparsify-then--compress magnitude control with warm-up-then-anneal temporal control, adding no auxiliary model, teacher query, or loss term. Across mathematical reasoning and code generation with Qwen3-8B, Qwen3-4B, and Qwen3-1.7B, SAF improve…
- **Coexistence / evolution:** 旧方案在低风险、短状态或同构部署中仍成立；新机制只在约束变化使错误代价或状态漂移不可忽略时接手。
- **Books route:** 对照 `TRAIN-GRPO` 及相邻章节；先进入按日期排序的 writeback queue，根任务合并同 owner 后决定最终写回。
<!-- review:SF-2026-ARXIV-2607-29209:end -->

<!-- review:SF-2026-ARXIV-2607-29211:start -->
### Knowing When to Quit: Diagnosing and Training LLMs to Abort Futile Reasoning

- **Status / Evidence:** Experimental；exact-v1 HTML 已读取并保存校验和；Score V2=`6`。
- **Problem / old solution:** 既有路径通常把 on-policy reasoning optimization 隐含在模型调用或离线平均指标中；在较小规模、单一模型或无跨请求状态时成本较低，但难以回答谁拥有失败恢复与版本一致性。
- **Changed constraint:** 论文面对的约束由摘要和全文共同限定为：Large language models generate computationally expensive yet semantically void reasoning on beyond-capability tasks, creating risks where plausible-sounding but incorrect derivations mislead users. We characterize this \textit{futile reasoning} phenomenon through systematic analysis, revealing universal capability overreach and systematic miscalibration between capability and behavior.
- **Mechanism:** exact-v1 的方法段写明：However, when confronted with tasks that exceed their intrinsic capabilities, LLMs fail to recognize their boundaries. Instead of acknowledging their ignorance, they often persist in generating output, producing outputs that superficially resemble valid solutions. Due to the lengthy and convoluted nature of these generated traces, distinguishing valid reasoning from such hallucinations is notoriously difficult for humans . Consequently, this creates a critical reliability risk: users may mistakenly trust plausible-sounding but fundamentally incorrect derivations, severely limiting the adoption of LLMs in high-reliability domains .
- **State ownership:** 需要显式绑定 rollout/reward/advantage state；canonical owner 是 `TRAIN-GRPO`，而不是论文应用领域本身。
- **Control / data flow:** 数据由工作负载进入机制实现，post-training loop 决定是否执行、路由、提交或回退；输出必须携带与输入同一版本域的证据。
- **Implementation surface:** 全文 locator=`full-text paragraph 3; papers/2026/08/_sources/arxiv-owner-replay-20260903/20260803/exact-v1-text/2607.29211v1.txt`；公开实现、硬件或训练配置只按正文披露解释，未披露字段不补写。
- **Evaluation contract:** We conduct a systematic empirical analysis to characterize the nature of . Our primary objective is to quantify the misalignment between LLMs’ generative behavior and their intrinsic competence boundaries. Using a controlled reasoning testbed, we investigate three key questions: (1) Do models refuse beyond-capability tasks, or exhibit universal capability overreach? (2) What are the characteristic failure patterns of futile reasoning? (3) Are models’ refusal decisions properly calibrated with their empirical capabilities? 该结果只绑定论文声明的数据、模型、硬件、精度、长度、batch/concurrency 与 evaluator；缺失字段均为 `Not Disclosed`。
- **Proves / does not prove:** 证据支持该受限 workload 中机制可行或暴露既有评价缺口；不证明跨模型、跨硬件、跨领域或生产 SLO 的普遍优势。
- **Trade-off / failure mode:** 新增状态、控制器和观测提高可验证性，但引入版本错配、额外延迟/内存/通信、错误路由及 evaluator bias。全文边界：We identify and address , where models generate incorrect reasoning on beyond-capability tasks rather than refusing. Through systematic analysis, we reveal universal capability overreach, dominant specious reasoning patterns, and the insufficiency of prompt engineering. Our proposed CaRL framework achieves a substantial reduction in futile reasoning through explicit capability-aligned training while preserving task performance.
- **Coexistence / evolution:** 旧方案在低风险、短状态或同构部署中仍成立；新机制只在约束变化使错误代价或状态漂移不可忽略时接手。
- **Books route:** 对照 `TRAIN-GRPO` 及相邻章节；先进入按日期排序的 writeback queue，根任务合并同 owner 后决定最终写回。
<!-- review:SF-2026-ARXIV-2607-29211:end -->

<!-- review:SF-2026-ARXIV-2607-29218:start -->
### MirrorCraft: Paired Evaluation under Hidden Rule Changes in Minecraft

- **Status / Evidence:** Experimental；exact-v1 HTML 已读取并保存校验和；Score V2=`7`。
- **Problem / old solution:** 既有路径通常把 evaluation evidence and release decision 隐含在模型调用或离线平均指标中；在较小规模、单一模型或无跨请求状态时成本较低，但难以回答谁拥有失败恢复与版本一致性。
- **Changed constraint:** 论文面对的约束由摘要和全文共同限定为：With the prosperity of the large language models (LLMs), it has become an interesting topic: how do LLM-based agents work in Minecraft? Unfortunately, most existing benchmarks evaluate them under fixed game mechanics.
- **Mechanism:** exact-v1 的方法段写明：Jilin University, Changchun, China; Tianjin University of Finance and Economics, Tianjin, China
- **State ownership:** 需要显式绑定 evaluator configuration, dataset slice and result provenance；canonical owner 是 `PLATFORM-EVALUATION-SYSTEM`，而不是论文应用领域本身。
- **Control / data flow:** 数据由工作负载进入机制实现，evaluation controller 决定是否执行、路由、提交或回退；输出必须携带与输入同一版本域的证据。
- **Implementation surface:** 全文 locator=`full-text paragraph 3; papers/2026/08/_sources/arxiv-owner-replay-20260903/20260803/exact-v1-text/2607.29218v1.txt`；公开实现、硬件或训练配置只按正文披露解释，未披露字段不补写。
- **Evaluation contract:** With the prosperity of the large language models (LLMs), it has become an interesting topic: how do LLM-based agents work in Minecraft? Unfortunately, most existing benchmarks evaluate them under fixed game mechanics. High performance in these settings does not show whether an agent can continue making progress when familiar recipes, drops, and other rules change. In this paper, we introduce MirrorCraft, a paired benchmark for evaluating agents under hidden rule changes in Minecraft. Each Mirror world is a copy of its paired Vanilla world, with selected server-side rules modified by the corresponding datapack. Terrain, spawn, resource placement, objective, interface, and action budget remain matched within eve… 该结果只绑定论文声明的数据、模型、硬件、精度、长度、batch/concurrency 与 evaluator；缺失字段均为 `Not Disclosed`。
- **Proves / does not prove:** 证据支持该受限 workload 中机制可行或暴露既有评价缺口；不证明跨模型、跨硬件、跨领域或生产 SLO 的普遍优势。
- **Trade-off / failure mode:** 新增状态、控制器和观测提高可验证性，但引入版本错配、额外延迟/内存/通信、错误路由及 evaluator bias。全文边界：MirrorCraft compares each Vanilla world with paired Mirror worlds copied from its save, preserving terrain, spawn, placed resources, task, interfaces, and action budget while changing only the rule suite. Across the evaluated settings, hidden rule changes do not produce a uniform penalty. The differences span both directions: ranges from to , while ranges from to percentage points. Among the six configurations evaluated without rule descriptions, ReAct achieves the highest pooled Mirror Score. For ReAct, providing the exact rules improves mean Score and SR in all three tasks but does not eliminate failures. Because Mirror performance and RIE rankings can disagree, both should be reported; a small RIE alone doe…
- **Coexistence / evolution:** 旧方案在低风险、短状态或同构部署中仍成立；新机制只在约束变化使错误代价或状态漂移不可忽略时接手。
- **Books route:** 对照 `PLATFORM-EVALUATION-SYSTEM` 及相邻章节；先进入按日期排序的 writeback queue，根任务合并同 owner 后决定最终写回。
<!-- review:SF-2026-ARXIV-2607-29218:end -->

<!-- review:SF-2026-ARXIV-2607-29221:start -->
### MOSAIC: Masked Outsourcing of Secure AI Computations

- **Status / Evidence:** Experimental；exact-v1 HTML 已读取并保存校验和；Score V2=`9`。
- **Problem / old solution:** 既有路径通常把 security/privacy boundary 隐含在模型调用或离线平均指标中；在较小规模、单一模型或无跨请求状态时成本较低，但难以回答谁拥有失败恢复与版本一致性。
- **Changed constraint:** 论文面对的约束由摘要和全文共同限定为：We address the challenge of securely and efficiently outsourcing AI computations from a trusted but computationally weak client to an untrusted but powerful server, in the setting where the client holds both the input and the model, and the server must learn neither. We present MOSAIC, whose core is a novel matrix-multiplication masking protocol that scales to far larger matrices than prior work, enabling the safe outsourcing…
- **Mechanism:** exact-v1 的方法段写明：A decoder-only transformer maps tokens to logits via an embedding, (or ), and a final language-model head. Each model layer follows the residual + pre-norm pattern combining attention and a position-wise MLP, each preceded by , which projects onto a sphere of radius , collapsing any radial disagreement.
- **State ownership:** 需要显式绑定 principal, data and proof provenance；canonical owner 是 `PLATFORM-SECURITY`，而不是论文应用领域本身。
- **Control / data flow:** 数据由工作负载进入机制实现，policy enforcement plane 决定是否执行、路由、提交或回退；输出必须携带与输入同一版本域的证据。
- **Implementation surface:** 全文 locator=`Transformer architecture; papers/2026/08/_sources/arxiv-owner-replay-20260903/20260803/exact-v1-text/2607.29221v1.txt`；公开实现、硬件或训练配置只按正文披露解释，未披露字段不补写。
- **Evaluation contract:** MOSAIC is roughly (decode) to – (prefill) slower than running inference for the same 70B models on a single local GPU of the same type, with the higher prefill factor corresponding to layer- rather than matrix-sharding. This overhead largely reflects our emulation of 32-bit integer arithmetic on 8-bit GPU cores (10 INT8 MatMuls per INT32 MatMul; see the emulation approach above); native 32-bit-integer support in AI accelerator cores (e.g. NVIDIA Tensor) would significantly reduce this gap. We highlight three observations in prefill () and decode () experiments on 70B class models. Firstly, communication between the trusted and untrusted pools is not the bottleneck under the available inter-GPU bandwidth: it ac… 该结果只绑定论文声明的数据、模型、硬件、精度、长度、batch/concurrency 与 evaluator；缺失字段均为 `Not Disclosed`。
- **Proves / does not prove:** 证据支持该受限 workload 中机制可行或暴露既有评价缺口；不证明跨模型、跨硬件、跨领域或生产 SLO 的普遍优势。
- **Trade-off / failure mode:** 新增状态、控制器和观测提高可验证性，但引入版本错配、额外延迟/内存/通信、错误路由及 evaluator bias。全文边界：Cryptographic protocols such as MOSAIC operate over integer rings, necessitating 32-bit integer arithmetic, which is not natively supported in the fastest cores of modern AI accelerators. We implement an emulation thereof over 8-bit Tensor cores, which results in a (decode) to – (prefill) slow-down versus a baseline, non-confidential inference on 70B models. We think much of this gap can be explained by the emulation overhead, in which each 32-bit integer MatMul is realized with 10x underlying 8-bit integer MatMul launches. We hope that works such as MOSAIC can inspire AI hardware manufacturers to consider native 32-bit integer support in future accelerator designs.
- **Coexistence / evolution:** 旧方案在低风险、短状态或同构部署中仍成立；新机制只在约束变化使错误代价或状态漂移不可忽略时接手。
- **Books route:** 对照 `PLATFORM-SECURITY` 及相邻章节；先进入按日期排序的 writeback queue，根任务合并同 owner 后决定最终写回。
<!-- review:SF-2026-ARXIV-2607-29221:end -->

<!-- review:SF-2026-ARXIV-2607-29235:start -->
### FBFM: A Training-Free Asynchronous Feedback Mechanism for Flow-Matching in World-Action Models Execution

- **Status / Evidence:** Experimental；exact-v1 HTML 已读取并保存校验和；Score V2=`7`。
- **Problem / old solution:** 既有路径通常把 action-conditioned transition 隐含在模型调用或离线平均指标中；在较小规模、单一模型或无跨请求状态时成本较低，但难以回答谁拥有失败恢复与版本一致性。
- **Changed constraint:** 论文面对的约束由摘要和全文共同限定为：Although world-action models (WAMs) enhance long-horizon robot control by predicting visual evolution before acting, long-horizon reliability demands repeated re-grounding in real observations--not recursive rollout. Existing WAMs address this by refreshing history or KV cache with ground-truth data between chunks.
- **Mechanism:** exact-v1 的方法段写明：Existing WAM systems partially address this requirement by refreshing their history or internal context with ground-truth observations between action chunks. Such context updates improve the condition available to a subsequent generation call, but the returned observations remain conditioning information rather than measurements imposed on selected variables of the future currently being generated. This distinction creates a temporal-granularity gap: chunk-level re-grounding cannot correct state-prediction errors at individual time steps of an active chunk. As a result, the future used to produce actions may remain inconsistent with physical transitions that have already occurred.
- **State ownership:** 需要显式绑定 latent environment and rollout state；canonical owner 是 `MULTIMODAL-WORLD-MODELS`，而不是论文应用领域本身。
- **Control / data flow:** 数据由工作负载进入机制实现，world-model loop 决定是否执行、路由、提交或回退；输出必须携带与输入同一版本域的证据。
- **Implementation surface:** 全文 locator=`full-text paragraph 3; papers/2026/08/_sources/arxiv-owner-replay-20260903/20260803/exact-v1-text/2607.29235v1.txt`；公开实现、硬件或训练配置只按正文披露解释，未披露字段不补写。
- **Evaluation contract:** We evaluate FBFM in two complementary tracks that cover the two WAM generation factorizations considered in Section . Comparisons are made within each track using the same frozen base model; absolute scores are not compared across architectures or benchmarks. 该结果只绑定论文声明的数据、模型、硬件、精度、长度、batch/concurrency 与 evaluator；缺失字段均为 `Not Disclosed`。
- **Proves / does not prove:** 证据支持该受限 workload 中机制可行或暴露既有评价缺口；不证明跨模型、跨硬件、跨领域或生产 SLO 的普遍优势。
- **Trade-off / failure mode:** 新增状态、控制器和观测提高可验证性，但引入版本错配、额外延迟/内存/通信、错误路由及 evaluator bias。全文边界：This paper studies a practical mismatch in world-action model execution: long-horizon behavior needs continual grounding in real observations, while existing chunk-wise refresh schemes only correct the model after a chunk has already been generated. We proposed Feedback Flow Matching (FBFM), a training-free inference mechanism that moves feedback into the active flow-matching process. By expressing both committed actions and newly observed latent states as masked pseudoinverse measurements, FBFM provides a common correction interface for stage-wise and joint-generation WAMs. Our experiments instantiate this idea on LingBot-VA on RoboTwin2.0 and DreamZero on LIBERO, and further evaluate real-world observation p…
- **Coexistence / evolution:** 旧方案在低风险、短状态或同构部署中仍成立；新机制只在约束变化使错误代价或状态漂移不可忽略时接手。
- **Books route:** 对照 `MULTIMODAL-WORLD-MODELS` 及相邻章节；先进入按日期排序的 writeback queue，根任务合并同 owner 后决定最终写回。
<!-- review:SF-2026-ARXIV-2607-29235:end -->

<!-- review:SF-2026-ARXIV-2607-29240:start -->
### When Model Priors Conflict with Visual Evidence: Mitigating Commonsense-Driven Hallucinations by Selective Prior Calibration

- **Status / Evidence:** Experimental；exact-v1 HTML 已读取并保存校验和；Score V2=`6`。
- **Problem / old solution:** 既有路径通常把 cross-modal evidence alignment 隐含在模型调用或离线平均指标中；在较小规模、单一模型或无跨请求状态时成本较低，但难以回答谁拥有失败恢复与版本一致性。
- **Changed constraint:** 论文面对的约束由摘要和全文共同限定为：In vision--language models, commonsense-driven hallucination (CDH) occurs when a model's commonsense prior overrides clear visual evidence of an atypical state. For example, a model may report that a visibly six-fingered hand has five fingers.
- **Mechanism:** exact-v1 的方法段写明：Table reports the performance of SPC on the MC test set. SPC raises CF accuracy by 7.8 and 7.0 points for Qwen and LLaVA, respectively, while changing CS accuracy by only +0.4 and -0.4 points. Repairs substantially outnumber harms (21/3 and 17/1). Consistent with these gains, CFAD and RPD decrease, indicating a narrower CF–CS performance gap, while the lower CCR shows that fewer remaining CF errors converge on the paired CS answer. SPC therefore repairs atypical cases while largely preserving correct predictions on matched CS images. Table compares SPC with existing mitigation methods using to summarize the repair–retention trade-off. For fairness, the same development objective is used to select every tunable…
- **State ownership:** 需要显式绑定 modality, timestamp and representation identity；canonical owner 是 `MULTIMODAL-REPRESENTATION`，而不是论文应用领域本身。
- **Control / data flow:** 数据由工作负载进入机制实现，fusion/evidence router 决定是否执行、路由、提交或回退；输出必须携带与输入同一版本域的证据。
- **Implementation surface:** 全文 locator=`RQ2: Comparison with Existing Methods; papers/2026/08/_sources/arxiv-owner-replay-20260903/20260803/exact-v1-text/2607.29240v1.txt`；公开实现、硬件或训练配置只按正文披露解释，未披露字段不补写。
- **Evaluation contract:** We organize our experiments around five research questions. We analyze the direction of incorrect CF predictions. We evaluate CF repair, CS retention, and performance relative to existing methods. We examine candidate-specific prior subtraction, instance-dependent correction strength, and selective answer revision. We test held-out CDH categories, unseen candidate-answer orders, and external benchmarks. We examine its sensitivity to question form and claim order. 该结果只绑定论文声明的数据、模型、硬件、精度、长度、batch/concurrency 与 evaluator；缺失字段均为 `Not Disclosed`。
- **Proves / does not prove:** 证据支持该受限 workload 中机制可行或暴露既有评价缺口；不证明跨模型、跨硬件、跨领域或生产 SLO 的普遍优势。
- **Trade-off / failure mode:** 新增状态、控制器和观测提高可验证性，但引入版本错配、额外延迟/内存/通信、错误路由及 evaluator bias。全文边界：SPC requires a fixed candidate set, access to candidate-level probabilities, and model-specific paired CF–CS development data. During inference, it scores each candidate both with and without the image, making it more expensive than one-pass decoding and incompatible with interfaces that expose only generated text. The current method therefore does not support open-ended generation. Table further reveals a limitation on binary QA: the no-image preference may reflect a fixed yes/no bias or claim position rather than a preference for the ordinary state. Although the final decision rule can reject weak corrections, it cannot compensate for a misaligned prior estimate. Future work will extend SPC to open-ended gen…
- **Coexistence / evolution:** 旧方案在低风险、短状态或同构部署中仍成立；新机制只在约束变化使错误代价或状态漂移不可忽略时接手。
- **Books route:** 对照 `MULTIMODAL-REPRESENTATION` 及相邻章节；先进入按日期排序的 writeback queue，根任务合并同 owner 后决定最终写回。
<!-- review:SF-2026-ARXIV-2607-29240:end -->

<!-- review:SF-2026-ARXIV-2607-29246:start -->
### Don't Mix Rewards, Mix Policies: Policy Decomposition and Optimization for Multi-Reward RL

- **Status / Evidence:** Experimental；exact-v1 HTML 已读取并保存校验和；Score V2=`6`。
- **Problem / old solution:** 既有路径通常把 preference/reward optimization 隐含在模型调用或离线平均指标中；在较小规模、单一模型或无跨请求状态时成本较低，但难以回答谁拥有失败恢复与版本一致性。
- **Changed constraint:** 论文面对的约束由摘要和全文共同限定为：Modern large language models (LLMs) are expected not just to answer correctly, but to adapt their behavior to different human values and use cases. As a result, multi-reward reinforcement learning (RL) has become an increasingly important problem for LLMs, where each reward captures a different aspect of desired behavior.
- **Mechanism:** exact-v1 的方法段写明：Existing multi-reward RL methods differ mainly in how they merge reward signals into one training objective. Linear scalarization sums rewards with manual weights; it is simple but scale-sensitive, and the weights must be retuned per task. Reward shaping and adaptive weighting mitigate scale mismatch, but still collapse all rewards into one scalar before each update, so conflicting preferences compete within the same gradient step. Constrained or multi-objective RL treats some rewards as Lagrangian constraints in pursuit of Pareto optimality, but is often hard to optimize and unstable in practice.
- **State ownership:** 需要显式绑定 preference, reward and policy-version state；canonical owner 是 `TRAIN-RLHF`，而不是论文应用领域本身。
- **Control / data flow:** 数据由工作负载进入机制实现，post-training controller 决定是否执行、路由、提交或回退；输出必须携带与输入同一版本域的证据。
- **Implementation surface:** 全文 locator=`full-text paragraph 3; papers/2026/08/_sources/arxiv-owner-replay-20260903/20260803/exact-v1-text/2607.29246v1.txt`；公开实现、硬件或训练配置只按正文披露解释，未披露字段不补写。
- **Evaluation contract:** We evaluate on three multi-reward alignment scenarios: scientific question answering, tool-use reasoning, and helpfulness–safety alignment. For scientific reasoning, we train models on SciKnowEval and evaluate them on GPQA and ScienceQA . Further details are in Appendix . 该结果只绑定论文声明的数据、模型、硬件、精度、长度、batch/concurrency 与 evaluator；缺失字段均为 `Not Disclosed`。
- **Proves / does not prove:** 证据支持该受限 workload 中机制可行或暴露既有评价缺口；不证明跨模型、跨硬件、跨领域或生产 SLO 的普遍优势。
- **Trade-off / failure mode:** 新增状态、控制器和观测提高可验证性，但引入版本错配、额外延迟/内存/通信、错误路由及 evaluator bias。全文边界：In this work, we propose , a policy-space composition framework for multi-reward LLM alignment. Instead of scalarizing heterogeneous rewards into a single optimization signal, keeps each reward as a separate optimization direction by learning one positive policy per reward. A single global negative policy further captures the union of failure modes. These policies are composed through explicit merge weights, enabling controllable preference trade-offs without retraining. Experiments on scientific reasoning, tool-use reasoning, and helpfulness–safety alignment show that consistently outperforms reward-space baselines, remains more robust as reward complexity increases, and supports effective inference-time pref…
- **Coexistence / evolution:** 旧方案在低风险、短状态或同构部署中仍成立；新机制只在约束变化使错误代价或状态漂移不可忽略时接手。
- **Books route:** 对照 `TRAIN-RLHF` 及相邻章节；先进入按日期排序的 writeback queue，根任务合并同 owner 后决定最终写回。
<!-- review:SF-2026-ARXIV-2607-29246:end -->

<!-- review:SF-2026-ARXIV-2607-29250:start -->
### Data Turnstile: A Scalable Open Framework for Function-Calling Data Generation

- **Status / Evidence:** Experimental；exact-v1 HTML 已读取并保存校验和；Score V2=`6`。
- **Problem / old solution:** 既有路径通常把 training evidence construction 隐含在模型调用或离线平均指标中；在较小规模、单一模型或无跨请求状态时成本较低，但难以回答谁拥有失败恢复与版本一致性。
- **Changed constraint:** 论文面对的约束由摘要和全文共同限定为：Small language models (SLMs) are attractive for agentic deployment due to low latency, reduced cost, and on-device privacy, yet they struggle with tool-use tasks where training data is scarce and noisy. Unlike larger models, SLMs cannot compensate for low-quality supervision through sheer capacity, making data quality the critical bottleneck.
- **Mechanism:** exact-v1 的方法段写明：Small language models (SLMs) are attractive for agentic deployment due to low latency, reduced cost, and on-device privacy, yet they struggle with tool-use tasks where training data is scarce and noisy. Unlike larger models, SLMs cannot compensate for low-quality supervision through sheer capacity, making data quality the critical bottleneck. We present Data Turnstile, an open-source framework that takes user-defined API specifications and generates high-quality synthetic training data for function calling. Turnstile decomposes multi-turn tool-use interactions into constrained, stepwise generation with validation and error-feedback loops, providing fine-grained control over API diversity, conversation complexi…
- **State ownership:** 需要显式绑定 sample lineage and acceptance state；canonical owner 是 `TRAIN-DATA`，而不是论文应用领域本身。
- **Control / data flow:** 数据由工作负载进入机制实现，data pipeline 决定是否执行、路由、提交或回退；输出必须携带与输入同一版本域的证据。
- **Implementation surface:** 全文 locator=`Data Turnstile: A Scalable Open Framework for; papers/2026/08/_sources/arxiv-owner-replay-20260903/20260803/exact-v1-text/2607.29250v1.txt`；公开实现、硬件或训练配置只按正文披露解释，未披露字段不补写。
- **Evaluation contract:** We design our experiments to investigate single-turn performance, and evaluate the following: Impact of training on existing open-source datasets (xLAM-OS and Glaive-OS). This is a baseline to compare Turnstile SFT against. 该结果只绑定论文声明的数据、模型、硬件、精度、长度、batch/concurrency 与 evaluator；缺失字段均为 `Not Disclosed`。
- **Proves / does not prove:** 证据支持该受限 workload 中机制可行或暴露既有评价缺口；不证明跨模型、跨硬件、跨领域或生产 SLO 的普遍优势。
- **Trade-off / failure mode:** 新增状态、控制器和观测提高可验证性，但引入版本错配、额外延迟/内存/通信、错误路由及 evaluator bias。全文边界：We further analyze the model performance across model sizes on the 114 evaluation tasks, breaking it down by category (Figure ).
- **Coexistence / evolution:** 旧方案在低风险、短状态或同构部署中仍成立；新机制只在约束变化使错误代价或状态漂移不可忽略时接手。
- **Books route:** 对照 `TRAIN-DATA` 及相邻章节；先进入按日期排序的 writeback queue，根任务合并同 owner 后决定最终写回。
<!-- review:SF-2026-ARXIV-2607-29250:end -->

<!-- review:SF-2026-ARXIV-2607-29252:start -->
### CalibratedRubric: Task-Adaptive Rubric Banks for Open-Ended LLM Evaluation

- **Status / Evidence:** Experimental；exact-v1 HTML 已读取并保存校验和；Score V2=`7`。
- **Problem / old solution:** 既有路径通常把 evaluation evidence and release decision 隐含在模型调用或离线平均指标中；在较小规模、单一模型或无跨请求状态时成本较低，但难以回答谁拥有失败恢复与版本一致性。
- **Changed constraint:** 论文面对的约束由摘要和全文共同限定为：Reliable evaluation of open-ended LLM outputs requires fine-grained rubrics, yet expert curation is costly and difficult to scale. Existing automated pipelines rely on strict judge unanimity and binary variance filters, which cannot distinguish measurable rubrics from informative ones.
- **Mechanism:** exact-v1 的方法段写明：Two structural bottlenecks limit current analytic evaluators. First, reliable rubric authoring still depends heavily on scarce domain expertise. For example, constructing a financial benchmark to professional examination standards requires experts to draft, refine, and validate criteria, making annotation difficult to scale . Second, automated methods can synthesize instance-specific criteria , but evaluation items vary substantially in informativeness , and reliable selection remains largely heuristic. Prior work uses IRT to build NLP evaluation scales, compare test sets, and shrink benchmarks ; we instead embed IRT inside rubric construction and use the item information function to select criteria over the r…
- **State ownership:** 需要显式绑定 evaluator configuration, dataset slice and result provenance；canonical owner 是 `PLATFORM-EVALUATION-SYSTEM`，而不是论文应用领域本身。
- **Control / data flow:** 数据由工作负载进入机制实现，evaluation controller 决定是否执行、路由、提交或回退；输出必须携带与输入同一版本域的证据。
- **Implementation surface:** 全文 locator=`full-text paragraph 3; papers/2026/08/_sources/arxiv-owner-replay-20260903/20260803/exact-v1-text/2607.29252v1.txt`；公开实现、硬件或训练配置只按正文披露解释，未披露字段不补写。
- **Evaluation contract:** Reliable evaluation of open-ended LLM outputs requires fine-grained rubrics, yet expert curation is costly and difficult to scale. Existing automated pipelines rely on strict judge unanimity and binary variance filters, which cannot distinguish measurable rubrics from informative ones. We introduce , a task-adaptive framework that combines type-specific scoring, Bayesian rubric-measurability filtering, and item response theory (IRT)-based bank assembly. CalibratedRubric estimates each rubric’s measurability with a Beta–Bernoulli agreement posterior and uses a submodular information-coverage objective to construct compact rubric banks over the observed capability range. Across financial, healthcare, general, an… 该结果只绑定论文声明的数据、模型、硬件、精度、长度、batch/concurrency 与 evaluator；缺失字段均为 `Not Disclosed`。
- **Proves / does not prove:** 证据支持该受限 workload 中机制可行或暴露既有评价缺口；不证明跨模型、跨硬件、跨领域或生产 SLO 的普遍优势。
- **Trade-off / failure mode:** 新增状态、控制器和观测提高可验证性，但引入版本错配、额外延迟/内存/通信、错误路由及 evaluator bias。全文边界：We introduced , a task-adaptive framework for constructing compact, consensus-derived rubric banks without placing experts in the full evaluation loop. It replaces rigid unanimity and variance filters with posterior judge consensus and IRT-based submodular test assembly, while task typing makes the response scale and scoring objective explicit. Corrupting task labels reduces downstream discrimination, posterior measurability filtering improves agreement on every three-judge block, and IIF-greedy improves cross-fitted rank-fidelity AUC over random selection across all six response blocks. On FinResearch it also reaches the target correlation with substantially fewer rubrics. The main benefit is therefore a more…
- **Coexistence / evolution:** 旧方案在低风险、短状态或同构部署中仍成立；新机制只在约束变化使错误代价或状态漂移不可忽略时接手。
- **Books route:** 对照 `PLATFORM-EVALUATION-SYSTEM` 及相邻章节；先进入按日期排序的 writeback queue，根任务合并同 owner 后决定最终写回。
<!-- review:SF-2026-ARXIV-2607-29252:end -->

<!-- review:SF-2026-ARXIV-2607-29254:start -->
### Tool Specifications Matter: Uncovering and Mitigating Safety Risks in AI Agents

- **Status / Evidence:** Experimental；exact-v1 HTML 已读取并保存校验和；Score V2=`7`。
- **Problem / old solution:** 既有路径通常把 tool acquisition or authorization 隐含在模型调用或离线平均指标中；在较小规模、单一模型或无跨请求状态时成本较低，但难以回答谁拥有失败恢复与版本一致性。
- **Changed constraint:** 论文面对的约束由摘要和全文共同限定为：AI agents extend large language models (LLMs) with external tools, enabling them to perform complex tasks and translate model outputs into consequential real-world actions. Yet LLMs often become substantially less safe when deployed as agents, and the source of this degradation remains poorly understood.
- **Mechanism:** exact-v1 的方法段写明：Recent studies , however, reveal a troubling phenomenon: the same LLM that refuses a harmful request in a chatbot setting may comply with it when deployed as an agent. This degradation is surprising because modern LLMs have already undergone extensive safety alignment and exhibit strong refusal behavior in standard conversational settings . Agent construction is intended to extend model capability, yet it can inadvertently undermine safety behavior that the underlying model already possesses. This raises a fundamental question:
- **State ownership:** 需要显式绑定 tool schema, capability and return provenance；canonical owner 是 `AGENT-TOOL-CALLING`，而不是论文应用领域本身。
- **Control / data flow:** 数据由工作负载进入机制实现，tool-policy controller 决定是否执行、路由、提交或回退；输出必须携带与输入同一版本域的证据。
- **Implementation surface:** 全文 locator=`full-text paragraph 3; papers/2026/08/_sources/arxiv-owner-replay-20260903/20260803/exact-v1-text/2607.29254v1.txt`；公开实现、硬件或训练配置只按正文披露解释，未披露字段不补写。
- **Evaluation contract:** We conduct two complementary analyses. First, we evaluate harmful–benign separability within each input setting by independently extracting refusal directions from chatbot- and agent-formatted inputs and evaluating each direction on held-out requests presented in the same format. Second, we apply the chatbot-derived refusal direction to agent-formatted inputs to examine whether the refusal-related separation identified in the chatbot setting is preserved after the agent context is introduced. Let and denote the direction-extraction and held-out evaluation splits, respectively. For an input format , we extract a refusal direction from the harmful and benign instances in presented in format , following prior wor… 该结果只绑定论文声明的数据、模型、硬件、精度、长度、batch/concurrency 与 evaluator；缺失字段均为 `Not Disclosed`。
- **Proves / does not prove:** 证据支持该受限 workload 中机制可行或暴露既有评价缺口；不证明跨模型、跨硬件、跨领域或生产 SLO 的普遍优势。
- **Trade-off / failure mode:** 新增状态、控制器和观测提高可验证性，但引入版本错配、额外延迟/内存/通信、错误路由及 evaluator bias。全文边界：This paper identifies schema-formatted tool specifications as a source of the safety degradation observed when LLMs are deployed as agents. Through white-box representation analysis, we show that schema formatting induces a hidden-state direction that opposes refusal, weakens refusal-related separation during generation, and causally contributes to harmful tool execution. Building on this finding, we propose SafeKeep, an inference-time safeguard that decouples safety judgment from tool execution by using flattened textual tool specifications for safety assessment while preserving the original agent pipeline for execution. Across two benchmarks and four LLMs, SafeKeep substantially improves agent safety while p…
- **Coexistence / evolution:** 旧方案在低风险、短状态或同构部署中仍成立；新机制只在约束变化使错误代价或状态漂移不可忽略时接手。
- **Books route:** 对照 `AGENT-TOOL-CALLING` 及相邻章节；先进入按日期排序的 writeback queue，根任务合并同 owner 后决定最终写回。
<!-- review:SF-2026-ARXIV-2607-29254:end -->

<!-- review:SF-2026-ARXIV-2607-29279:start -->
### ParaASR: Multi-Token Prediction for Fast and Long-Context LLM-Based Speech Recognition

- **Status / Evidence:** Experimental；exact-v1 HTML 已读取并保存校验和；Score V2=`6`。
- **Problem / old solution:** 既有路径通常把 multi-token proposal and verification 隐含在模型调用或离线平均指标中；在较小规模、单一模型或无跨请求状态时成本较低，但难以回答谁拥有失败恢复与版本一致性。
- **Changed constraint:** 论文面对的约束由摘要和全文共同限定为：Audio-encoder-LLM-decoder architectures have become the dominant paradigm for modern automatic speech recognition (ASR), improving transcription quality through large-scale language modeling. However, the cost of autoregressive decoding scales with decoder size, creating a fundamental trade-off between recognition quality and serving latency.
- **Mechanism:** exact-v1 的方法段写明：The backbone follows the standard encoder–adapter–decoder pattern for audio-language modeling. The audio encoder is a 0.6B Transformer initialized from a publicly available omni-modal foundation . It remains frozen throughout training and applies temporal downsampling to produce one acoustic embedding every 80 ms; the frame rate and token granularity of speech representations are known to affect recognition quality in speech language models . These embeddings are projected by a linear adapter into the hidden space of the language decoder. The decoder itself is a 4B dense Transformer initialized from a pre-trained text LLM and supports a native 32K context window. Combined with the 80 ms acoustic embedding rate…
- **State ownership:** 需要显式绑定 proposal-prefix commit state；canonical owner 是 `INFER-SPECULATIVE-DECODING`，而不是论文应用领域本身。
- **Control / data flow:** 数据由工作负载进入机制实现，decoder verifier 决定是否执行、路由、提交或回退；输出必须携带与输入同一版本域的证据。
- **Implementation surface:** 全文 locator=`Backbone Architecture; papers/2026/08/_sources/arxiv-owner-replay-20260903/20260803/exact-v1-text/2607.29279v1.txt`；公开实现、硬件或训练配置只按正文披露解释，未披露字段不补写。
- **Evaluation contract:** Our evaluation of focuses on three primary objectives: recognition accuracy across diverse languages and recording lengths, native long-form transcription capability, and inference efficiency under production-scale serving. We compare against several competitive baselines, namely VibeVoice-ASR , FunASR-Nano , Doubao-ASR-2603 , and Qwen3-ASR-1.7B . To ensure a fair comparison, all models are deployed in a local environment using a single NVIDIA H800 GPU with single-concurrency serving, except for Doubao-ASR-2603, which is accessed through its official API. For baselines that do not natively support long-form audio, such as FunASR-Nano, we use VAD to segment the recordings into clips of at most 30 seconds. Recog… 该结果只绑定论文声明的数据、模型、硬件、精度、长度、batch/concurrency 与 evaluator；缺失字段均为 `Not Disclosed`。
- **Proves / does not prove:** 证据支持该受限 workload 中机制可行或暴露既有评价缺口；不证明跨模型、跨硬件、跨领域或生产 SLO 的普遍优势。
- **Trade-off / failure mode:** 新增状态、控制器和观测提高可验证性，但引入版本错配、额外延迟/内存/通信、错误路由及 evaluator bias。全文边界：We presented , an LLM-based ASR system designed to resolve the fundamental tension between decoder scale and inference latency. By exploiting the inherent determinism of speech transcription, we integrate MTP into the LLM decoder, enabling high-parallelism decoding without compromising recognition accuracy. This design transforms the ASR decoding process from a token-by-token bottleneck into a high-throughput verification regime. Our technical approach further targets stable long-form transcription and efficient decoding. supports a native 32K-context window, allowing the system to process up to 30 minutes of audio in a single pass while maintaining a remarkably low real-time factor. The staged training protoc…
- **Coexistence / evolution:** 旧方案在低风险、短状态或同构部署中仍成立；新机制只在约束变化使错误代价或状态漂移不可忽略时接手。
- **Books route:** 对照 `INFER-SPECULATIVE-DECODING` 及相邻章节；先进入按日期排序的 writeback queue，根任务合并同 owner 后决定最终写回。
<!-- review:SF-2026-ARXIV-2607-29279:end -->

<!-- review:SF-2026-ARXIV-2607-29283:start -->
### RTLCurator: Label-Efficient Data Curation for RTL Generation

- **Status / Evidence:** Experimental；exact-v1 HTML 已读取并保存校验和；Score V2=`6`。
- **Problem / old solution:** 既有路径通常把 training evidence construction 隐含在模型调用或离线平均指标中；在较小规模、单一模型或无跨请求状态时成本较低，但难以回答谁拥有失败恢复与版本一致性。
- **Changed constraint:** 论文面对的约束由摘要和全文共同限定为：Training large language models (LLMs) to write register-transfer level (RTL) requires large corpora of paired specifications and code, and such data is scarce enough that most public corpora are now synthesized. Synthesis provides scale but not correctness, and in two widely used RTL datasets only 24.4% and 53.5% of pairs pass generated functional tests.
- **Mechanism:** exact-v1 的方法段写明：In this section, we present , a framework that composes an RTL training corpus under a validation budget and a retention budget . The key insight is that a compatibility prior trained on functionally refuted negatives carries enough behavioral signal that a small number of validated labels suffices to calibrate it into a corpus-wide ordering. The entire framework is illustrated in Figure .
- **State ownership:** 需要显式绑定 sample lineage and acceptance state；canonical owner 是 `TRAIN-DATA`，而不是论文应用领域本身。
- **Control / data flow:** 数据由工作负载进入机制实现，data pipeline 决定是否执行、路由、提交或回退；输出必须携带与输入同一版本域的证据。
- **Implementation surface:** 全文 locator=`Method; papers/2026/08/_sources/arxiv-owner-replay-20260903/20260803/exact-v1-text/2607.29283v1.txt`；公开实现、硬件或训练配置只按正文披露解释，未披露字段不补写。
- **Evaluation contract:** Curation costs one encoder pass and one clustering over , and respectively, calibrator refits on at most labels, and one sort for stratification. The dominant real cost is the calls to , which is why is the budget that matters rather than itself. 该结果只绑定论文声明的数据、模型、硬件、精度、长度、batch/concurrency 与 evaluator；缺失字段均为 `Not Disclosed`。
- **Proves / does not prove:** 证据支持该受限 workload 中机制可行或暴露既有评价缺口；不证明跨模型、跨硬件、跨领域或生产 SLO 的普遍优势。
- **Trade-off / failure mode:** 新增状态、控制器和观测提高可验证性，但引入版本错配、额外延迟/内存/通信、错误路由及 evaluator bias。全文边界：In this work, we present , which overcomes the limitation of validation-based curation by scoring every pair for spec–RTL alignment before any pair is validated and by balancing that score against representation coverage and structural richness. This keeps a large corpus while removing the pairs that hurt most, and it shows that behavioral correctness serves better as an input to curation than as its objective. Experiments on CodeV and RTLCoder confirm that the selected subsets outperform full-corpus fine-tuning and every matched-budget baseline. The alignment score transfers to corpora it was never trained on, which suggests it can support other hardware data pipelines. Isolating the contributions of coverage…
- **Coexistence / evolution:** 旧方案在低风险、短状态或同构部署中仍成立；新机制只在约束变化使错误代价或状态漂移不可忽略时接手。
- **Books route:** 对照 `TRAIN-DATA` 及相邻章节；先进入按日期排序的 writeback queue，根任务合并同 owner 后决定最终写回。
<!-- review:SF-2026-ARXIV-2607-29283:end -->

<!-- review:SF-2026-ARXIV-2607-29285:start -->
### TRACT: Temporally Routed Action Chunks with Chronological Phase Authority for Contact-Rich Manipulation

- **Status / Evidence:** Experimental；exact-v1 HTML 已读取并保存校验和；Score V2=`6`。
- **Problem / old solution:** 既有路径通常把 closed-loop physical action 隐含在模型调用或离线平均指标中；在较小规模、单一模型或无跨请求状态时成本较低，但难以回答谁拥有失败恢复与版本一致性。
- **Changed constraint:** 论文面对的约束由摘要和全文共同限定为：Action chunking shortens the effective decision horizon of robot imitation learning by predicting multiple future actions, while conventional phase conditioning describes the current control instant. When a predicted horizon crosses a procedural boundary, assigning the current phase to the entire chunk creates a structural temporal mismatch.
- **Mechanism:** exact-v1 的方法段写明：Action chunking predicts a sequence of future actions at each policy query, reducing the effective decision length and producing smooth behavior from demonstrations. Action Chunking with Transformers (ACT) is a representative approach, combining sequence prediction with a temporal ensemble of overlapping chunks . This future-action representation raises a separate temporal question: which procedural phase should each query in the predicted chunk represent?
- **State ownership:** 需要显式绑定 sensor/action/trajectory state；canonical owner 是 `MULTIMODAL-EMBODIED-VLA`，而不是论文应用领域本身。
- **Control / data flow:** 数据由工作负载进入机制实现，policy plus safety controller 决定是否执行、路由、提交或回退；输出必须携带与输入同一版本域的证据。
- **Implementation surface:** 全文 locator=`full-text paragraph 3; papers/2026/08/_sources/arxiv-owner-replay-20260903/20260803/exact-v1-text/2607.29285v1.txt`；公开实现、硬件或训练配置只按正文披露解释，未披露字段不补写。
- **Evaluation contract:** We therefore evaluate the complete routed package against a flat phase-conditioned package under matched conditions; the comparison is package-level and does not isolate routing from other generator-package differences. 该结果只绑定论文声明的数据、模型、硬件、精度、长度、batch/concurrency 与 evaluator；缺失字段均为 `Not Disclosed`。
- **Proves / does not prove:** 证据支持该受限 workload 中机制可行或暴露既有评价缺口；不证明跨模型、跨硬件、跨领域或生产 SLO 的普遍优势。
- **Trade-off / failure mode:** 新增状态、控制器和观测提高可验证性，但引入版本错配、额外延迟/内存/通信、错误路由及 evaluator bias。全文边界：Have a free development cycle? Help support accessibility at arXiv! Our collaborators at LaTeXML maintain a , and welcome .
- **Coexistence / evolution:** 旧方案在低风险、短状态或同构部署中仍成立；新机制只在约束变化使错误代价或状态漂移不可忽略时接手。
- **Books route:** 对照 `MULTIMODAL-EMBODIED-VLA` 及相邻章节；先进入按日期排序的 writeback queue，根任务合并同 owner 后决定最终写回。
<!-- review:SF-2026-ARXIV-2607-29285:end -->

<!-- review:SF-2026-ARXIV-2607-29302:start -->
### BWM: A Low-Cost High-Fidelity World Simulator for Robot Learning

- **Status / Evidence:** Experimental；exact-v1 HTML 已读取并保存校验和；Score V2=`7`。
- **Problem / old solution:** 既有路径通常把 action-conditioned transition 隐含在模型调用或离线平均指标中；在较小规模、单一模型或无跨请求状态时成本较低，但难以回答谁拥有失败恢复与版本一致性。
- **Changed constraint:** 论文面对的约束由摘要和全文共同限定为：Reliable robot learning requires a world simulator that can predict action consequences before execution on physical hardware, including risky and failure-prone outcomes. Existing physics simulators require substantial asset construction and calibration and still face a sim-to-real gap, while video generators often lack precise control over their responses to fine-grained robot actions.
- **Mechanism:** exact-v1 的方法段写明：A learned robot world simulator provides a complementary source of interaction by predicting the visual consequences of candidate controls from recorded robot trajectories . By learning appearance and dynamics directly from real-world interaction data, it can narrow the sim-to-real gap associated with physics simulators and reduce reliance on real-robot hardware. During policy learning, it can synthesize action-aligned trajectories for imitation learning and provide interactive rollouts for reinforcement learning. During deployment, it can evaluate a policy through closed-loop interaction and anticipate risky action consequences before physical execution. The simulator can generate video rollouts and evaluate…
- **State ownership:** 需要显式绑定 latent environment and rollout state；canonical owner 是 `MULTIMODAL-WORLD-MODELS`，而不是论文应用领域本身。
- **Control / data flow:** 数据由工作负载进入机制实现，world-model loop 决定是否执行、路由、提交或回退；输出必须携带与输入同一版本域的证据。
- **Implementation surface:** 全文 locator=`full-text paragraph 3; papers/2026/08/_sources/arxiv-owner-replay-20260903/20260803/exact-v1-text/2607.29302v1.txt`；公开实现、硬件或训练配置只按正文披露解释，未披露字段不补写。
- **Evaluation contract:** How well does BWM preserve visual appearance, interaction physics, spatial structure, and action-conditioned behavior? Can closed-loop rollouts reproduce policy performance measured in a reference physics simulator? 该结果只绑定论文声明的数据、模型、硬件、精度、长度、batch/concurrency 与 evaluator；缺失字段均为 `Not Disclosed`。
- **Proves / does not prove:** 证据支持该受限 workload 中机制可行或暴露既有评价缺口；不证明跨模型、跨硬件、跨领域或生产 SLO 的普遍优势。
- **Trade-off / failure mode:** 新增状态、控制器和观测提高可验证性，但引入版本错配、额外延迟/内存/通信、错误路由及 evaluator bias。全文边界：Have a free development cycle? Help support accessibility at arXiv! Our collaborators at LaTeXML maintain a , and welcome .
- **Coexistence / evolution:** 旧方案在低风险、短状态或同构部署中仍成立；新机制只在约束变化使错误代价或状态漂移不可忽略时接手。
- **Books route:** 对照 `MULTIMODAL-WORLD-MODELS` 及相邻章节；先进入按日期排序的 writeback queue，根任务合并同 owner 后决定最终写回。
<!-- review:SF-2026-ARXIV-2607-29302:end -->

<!-- review:SF-2026-ARXIV-2607-29320:start -->
### MAGA: Multi-Platform Self-Fusion of GUI Agents via Structured Action Distillation

- **Status / Evidence:** Experimental；exact-v1 HTML 已读取并保存校验和；Score V2=`8`。
- **Problem / old solution:** 既有路径通常把 persistent agent runtime 隐含在模型调用或离线平均指标中；在较小规模、单一模型或无跨请求状态时成本较低，但难以回答谁拥有失败恢复与版本一致性。
- **Changed constraint:** 论文面对的约束由摘要和全文共同限定为：Graphical user interface (GUI) agents based on large language models are increasingly deployed across mobile, web, and desktop environments. However, existing agents are typically domain-specific, limiting the deployment and user experience.
- **Mechanism:** exact-v1 的方法段写明：This section first introduces the GUI agent interface and routed OPD (Figure (b)). We then present (Figure (c)), which combines (Section ) with a (Section ) to provide targeted supervision for short, structured action outputs.
- **State ownership:** 需要显式绑定 agent/version/session state；canonical owner 是 `AGENT-PLATFORM`，而不是论文应用领域本身。
- **Control / data flow:** 数据由工作负载进入机制实现，agent control plane 决定是否执行、路由、提交或回退；输出必须携带与输入同一版本域的证据。
- **Implementation surface:** 全文 locator=`Method; papers/2026/08/_sources/arxiv-owner-replay-20260903/20260803/exact-v1-text/2607.29320v1.txt`；公开实现、硬件或训练配置只按正文披露解释，未披露字段不补写。
- **Evaluation contract:** In this section, we first describe the experiment implementation details, followed by presenting the main results of our method compared to various baselines and an ablation study. Then we provide deeper analysis of the trained student’s performance guided by six key questions, revealing fine-grained behavior beyond aggregate task success. 该结果只绑定论文声明的数据、模型、硬件、精度、长度、batch/concurrency 与 evaluator；缺失字段均为 `Not Disclosed`。
- **Proves / does not prove:** 证据支持该受限 workload 中机制可行或暴露既有评价缺口；不证明跨模型、跨硬件、跨领域或生产 SLO 的普遍优势。
- **Trade-off / failure mode:** 新增状态、控制器和观测提高可验证性，但引入版本错配、额外延迟/内存/通信、错误路由及 evaluator bias。全文边界：This work addresses how to consolidate multiple domain-specific GUI teachers into a single agent while retaining their specialized capabilities. Our analysis shows that weight merging degrades performance, particularly on high-disagreement spatial samples, while ordinary routed OPD provides only limited training signal to the short structured action. Moreover, the short action span carries domain-specific behavior, which significantly affects the environment state. Therefore, we propose to address this mismatch with structured action signal re-allocation and a training-only teacher hint, directing additional supervision according to action correctness and structure. Across MobileWorld, OSWorld, and WebVoyager…
- **Coexistence / evolution:** 旧方案在低风险、短状态或同构部署中仍成立；新机制只在约束变化使错误代价或状态漂移不可忽略时接手。
- **Books route:** 对照 `AGENT-PLATFORM` 及相邻章节；先进入按日期排序的 writeback queue，根任务合并同 owner 后决定最终写回。
<!-- review:SF-2026-ARXIV-2607-29320:end -->

<!-- review:SF-2026-ARXIV-2607-29353:start -->
### Versatile On-device Adaptation at the Edge by Unifying Few-shot, Zero-shot, Continual, and In-context Learning

- **Status / Evidence:** Experimental；exact-v1 HTML 已读取并保存校验和；Score V2=`6`。
- **Problem / old solution:** 既有路径通常把 composable adaptation 隐含在模型调用或离线平均指标中；在较小规模、单一模型或无跨请求状态时成本较低，但难以回答谁拥有失败恢复与版本一致性。
- **Changed constraint:** 论文面对的约束由摘要和全文共同限定为：With the ever-increasing pervasiveness of smart edge devices, the demand is growing for applications that can be tailored to users (e.g., custom keyword spotting) or patients (e.g., adaptive health monitoring). Yet, most edge devices rely on fixed inference algorithms and thus cannot learn on-device to personalize predictions.
- **Mechanism:** exact-v1 的方法段写明：Addressing these needs is challenging, due to the various limitations of existing strategies to adapt ((a)). We group these strategies into three categories. The first category, comprising inference accelerators, relies on the cloud for adaptation, which comes at the expense of the energy cost for the cloud link , latency penalties that preclude online learning , and risks of exposing user private data . The second trains a model from scratch with backpropagation (BP) directly on the device but requires storing all intermediate activations, which is especially prohibitive for long temporal signals . The third aims to alleviate this overhead of BP by implementing specialized learning algorithms in hardware , or…
- **State ownership:** 需要显式绑定 adapter identity and activation scope；canonical owner 是 `TRAIN-LORA`，而不是论文应用领域本身。
- **Control / data flow:** 数据由工作负载进入机制实现，training and serving router 决定是否执行、路由、提交或回退；输出必须携带与输入同一版本域的证据。
- **Implementation surface:** 全文 locator=`full-text paragraph 3; papers/2026/08/_sources/arxiv-owner-replay-20260903/20260803/exact-v1-text/2607.29353v1.txt`；公开实现、硬件或训练配置只按正文披露解释，未披露字段不补写。
- **Evaluation contract:** To evaluate the performance of our framework on FSL for classification tasks, we use the popular Omniglot dataset . The dataset consists of a total of 1623 different handwritten characters across a large variety of alphabets, containing 20 sample images per character of pixels. Since our framework is designed for processing sequential data, we flatten each input image to shape it into a 1D sequence. We test on Omniglot across the standard evaluation settings of 1, 5-shot and 5, 20-way, as well as 32-way 1-shot. We choose this dataset as it is widely used across both software and hardware works to measure FSL performance . Hence, Omniglot enables a direct comparison to these previous works. 该结果只绑定论文声明的数据、模型、硬件、精度、长度、batch/concurrency 与 evaluator；缺失字段均为 `Not Disclosed`。
- **Proves / does not prove:** 证据支持该受限 workload 中机制可行或暴露既有评价缺口；不证明跨模型、跨硬件、跨领域或生产 SLO 的普遍优势。
- **Trade-off / failure mode:** 新增状态、控制器和观测提高可验证性，但引入版本错配、额外延迟/内存/通信、错误路由及 evaluator bias。全文边界：Have a free development cycle? Help support accessibility at arXiv! Our collaborators at LaTeXML maintain a , and welcome .
- **Coexistence / evolution:** 旧方案在低风险、短状态或同构部署中仍成立；新机制只在约束变化使错误代价或状态漂移不可忽略时接手。
- **Books route:** 对照 `TRAIN-LORA` 及相邻章节；先进入按日期排序的 writeback queue，根任务合并同 owner 后决定最终写回。
<!-- review:SF-2026-ARXIV-2607-29353:end -->

<!-- review:SF-2026-ARXIV-2607-29363:start -->
### Stable Autoregressive Speech Generation with Low-Frame-Rate High-Dimensional Continuous Tokens

- **Status / Evidence:** Experimental；exact-v1 HTML 已读取并保存校验和；Score V2=`6`。
- **Problem / old solution:** 既有路径通常把 iterative or routed generation 隐含在模型调用或离线平均指标中；在较小规模、单一模型或无跨请求状态时成本较低，但难以回答谁拥有失败恢复与版本一致性。
- **Changed constraint:** 论文面对的约束由摘要和全文共同限定为：Balancing sequence length, representational capacity, and long-horizon stability is a central problem in autoregressive (AR) speech and audio generation. Representations with higher frame rates or greater capacity can preserve more signal detail, but they also make streaming generation more vulnerable to distribution drift and AR error accumulation.
- **Mechanism:** exact-v1 的方法段写明：In this section, we describe the concrete methods used to design our tokenizer and generative model, following the assumptions and design principles discussed above.
- **State ownership:** 需要显式绑定 proposal/correction/sample state；canonical owner 是 `MULTIMODAL-GENERATIVE-PARADIGMS`，而不是论文应用领域本身。
- **Control / data flow:** 数据由工作负载进入机制实现，generation scheduler 决定是否执行、路由、提交或回退；输出必须携带与输入同一版本域的证据。
- **Implementation surface:** 全文 locator=`Methodology; papers/2026/08/_sources/arxiv-owner-replay-20260903/20260803/exact-v1-text/2607.29363v1.txt`；公开实现、硬件或训练配置只按正文披露解释，未披露字段不补写。
- **Evaluation contract:** In this section, we evaluate Locodec and MP-ELD from two complementary perspectives. First, we study whether the proposed token-space shaping mechanisms preserve reconstruction quality while changing the geometry and statistics of the latent space. Second, we evaluate whether these shaped representations are easier to predict, and whether MP-ELD maintains short-form generation quality while improving long-horizon stability. 该结果只绑定论文声明的数据、模型、硬件、精度、长度、batch/concurrency 与 evaluator；缺失字段均为 `Not Disclosed`。
- **Proves / does not prove:** 证据支持该受限 workload 中机制可行或暴露既有评价缺口；不证明跨模型、跨硬件、跨领域或生产 SLO 的普遍优势。
- **Trade-off / failure mode:** 新增状态、控制器和观测提高可验证性，但引入版本错配、额外延迟/内存/通信、错误路由及 evaluator bias。全文边界：In this paper, we studied whether low-frame-rate, high-dimensional continuous tokens can serve as stable targets for autoregressive speech generation. Our main finding is that such tokens are viable when the representation space and the generative framework are designed jointly. We proposed Locodec, a locally encoded tokenizer which shapes a spherical high-dimensional token space around a lower-dimensional core manifold and induces a coordinate-wise energy hierarchy through PDD, improving predictability without noticeably degrading full-dimensional token reconstruction quality. We further proposed MP-ELD, which separates local-continuity, self-consistency, and alignment-consistency information pathways, allowi…
- **Coexistence / evolution:** 旧方案在低风险、短状态或同构部署中仍成立；新机制只在约束变化使错误代价或状态漂移不可忽略时接手。
- **Books route:** 对照 `MULTIMODAL-GENERATIVE-PARADIGMS` 及相邻章节；先进入按日期排序的 writeback queue，根任务合并同 owner 后决定最终写回。
<!-- review:SF-2026-ARXIV-2607-29363:end -->

<!-- review:SF-2026-ARXIV-2607-29377:start -->
### Zero-Mem: Zero-Token Memory Operations for LLM Agents

- **Status / Evidence:** Experimental；exact-v1 HTML 已读取并保存校验和；Score V2=`7`。
- **Problem / old solution:** 既有路径通常把 persistent or derived memory 隐含在模型调用或离线平均指标中；在较小规模、单一模型或无跨请求状态时成本较低，但难以回答谁拥有失败恢复与版本一致性。
- **Changed constraint:** 论文面对的约束由摘要和全文共同限定为：LLM agents need memory to act consistently over long interactions, yet many systems use additional LLM calls to operate that memory. Generating intermediate records and mediating their retrieval adds recurring token and time costs, while omitted or merged details can obscure the original evidence.
- **Mechanism:** exact-v1 的方法段写明：Across agent-memory and agentic structured-retrieval systems, language models have been used to summarize or reflect on experience, construct hierarchical abstractions and graph indexes, and generate or evolve linked memory records . These transformations can make large histories easier to access, but they also turn memory management into a recurring generative workload. When generated abstractions mediate later retrieval, omitted details, merged subjects, or blurred temporal updates may weaken traceability to the original interaction. The opposite strategy is to retain the complete history and retrieve directly from raw traces . Although this preserves source evidence, flat lexical or dense retrieval can conf…
- **State ownership:** 需要显式绑定 memory provenance, version and read/write boundary；canonical owner 是 `AGENT-MEMORY`，而不是论文应用领域本身。
- **Control / data flow:** 数据由工作负载进入机制实现，agent memory manager 决定是否执行、路由、提交或回退；输出必须携带与输入同一版本域的证据。
- **Implementation surface:** 全文 locator=`full-text paragraph 3; papers/2026/08/_sources/arxiv-owner-replay-20260903/20260803/exact-v1-text/2607.29377v1.txt`；公开实现、硬件或训练配置只按正文披露解释，未披露字段不补写。
- **Evaluation contract:** Across the long-context and long-memory QA benchmarks, Zero-Mem achieves competitive performance while reducing memory-operation LLM calls and tokens to zero. With an identical final-QA reader and equivalent context budget, Zero-Mem achieves a 57.6% reduction in memory-operation latency compared to the most time-efficient baseline, and ablation studies further verify the effectiveness of each core module. Our contributions are threefold: 该结果只绑定论文声明的数据、模型、硬件、精度、长度、batch/concurrency 与 evaluator；缺失字段均为 `Not Disclosed`。
- **Proves / does not prove:** 证据支持该受限 workload 中机制可行或暴露既有评价缺口；不证明跨模型、跨硬件、跨领域或生产 SLO 的普遍优势。
- **Trade-off / failure mode:** 新增状态、控制器和观测提高可验证性，但引入版本错配、额外延迟/内存/通信、错误路由及 evaluator bias。全文边界：We introduced Zero-Mem and formalized zero-token memory operations, an operating regime in which every operation outside final question answering invokes no LLM and consumes no LLM input or output tokens. Zero-Mem preserves original interaction traces and retrieves evidence through complementary relational and temporally ordered views without generating intermediate memory representations. Comprehensive experiments demonstrate competitive performance across long-term conversational memory and long-context multi-hop reasoning. Ablations further confirm the complementarity of the two evidence views. With an identical final-QA reader and an equivalent context budget, Zero-Mem eliminates memory-operation token con…
- **Coexistence / evolution:** 旧方案在低风险、短状态或同构部署中仍成立；新机制只在约束变化使错误代价或状态漂移不可忽略时接手。
- **Books route:** 对照 `AGENT-MEMORY` 及相邻章节；先进入按日期排序的 writeback queue，根任务合并同 owner 后决定最终写回。
<!-- review:SF-2026-ARXIV-2607-29377:end -->

<!-- review:SF-2026-ARXIV-2607-29393:start -->
### AquaJEPA: An Action-Conditioned Multimodal JEPA Family for Underwater Robot Dynamics

- **Status / Evidence:** Experimental；exact-v1 HTML 已读取并保存校验和；Score V2=`7`。
- **Problem / old solution:** 既有路径通常把 action-conditioned transition 隐含在模型调用或离线平均指标中；在较小规模、单一模型或无跨请求状态时成本较低，但难以回答谁拥有失败恢复与版本一致性。
- **Changed constraint:** 论文面对的约束由摘要和全文共同限定为：Underwater robots rely on complementary sensors whose reliability changes abruptly with water visibility and vehicle motion. We introduce AquaJEPA, a sensor-configurable family of action-conditioned joint-embedding predictive models spanning full multimodal, camera-only, sonar-only, and sensor-dropout configurations.
- **Mechanism:** exact-v1 的方法段写明：World models compress observations and predict how actions change future states . Pixel-level prediction, however, allocates capacity to appearance details that may be unpredictable and irrelevant to control. Joint-embedding predictive architectures (JEPAs) instead predict future features . For underwater control, the representation must additionally distinguish futures caused by different thruster sequences and remain interpretable when one sensing stream vanishes.
- **State ownership:** 需要显式绑定 latent environment and rollout state；canonical owner 是 `MULTIMODAL-WORLD-MODELS`，而不是论文应用领域本身。
- **Control / data flow:** 数据由工作负载进入机制实现，world-model loop 决定是否执行、路由、提交或回退；输出必须携带与输入同一版本域的证据。
- **Implementation surface:** 全文 locator=`full-text paragraph 3; papers/2026/08/_sources/arxiv-owner-replay-20260903/20260803/exact-v1-text/2607.29393v1.txt`；公开实现、硬件或训练配置只按正文披露解释，未披露字段不补写。
- **Evaluation contract:** controlled comparisons with state-only, supervised action-conditioned dynamics, and recurrent world-model baselines, plus one-factor ablations of the target, action margin, masks, and modality dropout; and 该结果只绑定论文声明的数据、模型、硬件、精度、长度、batch/concurrency 与 evaluator；缺失字段均为 `Not Disclosed`。
- **Proves / does not prove:** 证据支持该受限 workload 中机制可行或暴露既有评价缺口；不证明跨模型、跨硬件、跨领域或生产 SLO 的普遍优势。
- **Trade-off / failure mode:** 新增状态、控制器和观测提高可验证性，但引入版本错配、额外延迟/内存/通信、错误路由及 evaluator bias。全文边界：Have a free development cycle? Help support accessibility at arXiv! Our collaborators at LaTeXML maintain a , and welcome .
- **Coexistence / evolution:** 旧方案在低风险、短状态或同构部署中仍成立；新机制只在约束变化使错误代价或状态漂移不可忽略时接手。
- **Books route:** 对照 `MULTIMODAL-WORLD-MODELS` 及相邻章节；先进入按日期排序的 writeback queue，根任务合并同 owner 后决定最终写回。
<!-- review:SF-2026-ARXIV-2607-29393:end -->

<!-- review:SF-2026-ARXIV-2607-29398:start -->
### OnlineCache: Learning Dynamic Caching Policies with Error Correction for Efficient Diffusion Inference

- **Status / Evidence:** Experimental；exact-v1 HTML 已读取并保存校验和；Score V2=`8`。
- **Problem / old solution:** 既有路径通常把 compiled or cached execution 隐含在模型调用或离线平均指标中；在较小规模、单一模型或无跨请求状态时成本较低，但难以回答谁拥有失败恢复与版本一致性。
- **Changed constraint:** 论文面对的约束由摘要和全文共同限定为：Diffusion models have revolutionized generative tasks but incur high latency due to iterative denoising. While cache-based strategies accelerate inference by reusing intermediate features, they largely rely on static, sample-agnostic schedules.
- **Mechanism:** exact-v1 的方法段写明：In this section, we detail , a dynamic caching framework for diffusion acceleration. We formulate the caching decision as a sequential decision-making problem and solve it via Policy Gradient . Specifically, we introduce two versions: (i) a variant trains a separate policy network and (ii) a variant that jointly trains the policy while tuning an error corrector for caching-induced deviations.
- **State ownership:** 需要显式绑定 plan/cache validity state；canonical owner 是 `INFER-TENSORRT-LLM`，而不是论文应用领域本身。
- **Control / data flow:** 数据由工作负载进入机制实现，execution engine 决定是否执行、路由、提交或回退；输出必须携带与输入同一版本域的证据。
- **Implementation surface:** 全文 locator=`Methodology; papers/2026/08/_sources/arxiv-owner-replay-20260903/20260803/exact-v1-text/2607.29398v1.txt`；公开实现、硬件或训练配置只按正文披露解释，未披露字段不补写。
- **Evaluation contract:** (Targeting SOTA Caching Methods ): For image generation, we primarily compare against the SOTA caching methods and further provide a thorough generalization analysis. (Targeting Learning-Based Methods ): OnlineCache introduces an extra training phase. We therefore compare with representative learning-based cache methods (FastCache, L2C), demonstrating that our approach achieves superior performance even within trainable frameworks. 该结果只绑定论文声明的数据、模型、硬件、精度、长度、batch/concurrency 与 evaluator；缺失字段均为 `Not Disclosed`。
- **Proves / does not prove:** 证据支持该受限 workload 中机制可行或暴露既有评价缺口；不证明跨模型、跨硬件、跨领域或生产 SLO 的普遍优势。
- **Trade-off / failure mode:** 新增状态、控制器和观测提高可验证性，但引入版本错配、额外延迟/内存/通信、错误路由及 evaluator bias。全文边界：We propose OnlineCache, a dynamic cache-based acceleration framework that reformulates diffusion inference as an instance-aware sequential decision-making problem. By introducing a lightweight policy network and, in its advanced variant, jointly training an error corrector under a bilevel optimization paradigm, OnlineCache adaptively navigates the delicate trade-off between generation quality and computational cost, effectively handling both sample-level and timestep-level heterogeneities. Extensive experiments demonstrate the robustness, generality, and practical effectiveness of the proposed framework. By offering a globally optimized perspective, OnlineCache establishes a principled cache-based acceleration…
- **Coexistence / evolution:** 旧方案在低风险、短状态或同构部署中仍成立；新机制只在约束变化使错误代价或状态漂移不可忽略时接手。
- **Books route:** 对照 `INFER-TENSORRT-LLM` 及相邻章节；先进入按日期排序的 writeback queue，根任务合并同 owner 后决定最终写回。
<!-- review:SF-2026-ARXIV-2607-29398:end -->

<!-- review:SF-2026-ARXIV-2607-29405:start -->
### Beyond Component Testing: Validating Agentic AI Systems

- **Status / Evidence:** Experimental；exact-v1 HTML 已读取并保存校验和；Score V2=`7`。
- **Problem / old solution:** 既有路径通常把 evaluation evidence and release decision 隐含在模型调用或离线平均指标中；在较小规模、单一模型或无跨请求状态时成本较低，但难以回答谁拥有失败恢复与版本一致性。
- **Changed constraint:** 论文面对的约束由摘要和全文共同限定为：Agentic AI systems act through multi-step trajectories that combine planning, tool use, memory, interaction, and adaptation. This behavior stretches validation practice beyond component testing and one-shot input--output evaluation, because acceptable system behavior now depends on how decisions unfold over time and under changing environmental conditions.
- **Mechanism:** exact-v1 的方法段写明：A second literature evaluates agent frameworks directly, but in terms of capability rather than assurance. provide the most comprehensive architectural survey of LLM-based agents, covering memory, planning, tool use, and interaction patterns, but do not define validation dimensions or conduct systematic corpus coding. and offer further architectural surveys with attention to safety risks and governance, but neither treats temporal lifecycle validity or regulatory evidence legibility as first-class assurance targets. More focused work adds trajectory awareness only partially: MultiAgentBench and MAST score coordination outcomes and failure modes, AutoGen-style framework studies expose orchestration patterns, re…
- **State ownership:** 需要显式绑定 evaluator configuration, dataset slice and result provenance；canonical owner 是 `PLATFORM-EVALUATION-SYSTEM`，而不是论文应用领域本身。
- **Control / data flow:** 数据由工作负载进入机制实现，evaluation controller 决定是否执行、路由、提交或回退；输出必须携带与输入同一版本域的证据。
- **Implementation surface:** 全文 locator=`Agentic Frameworks Evaluation Gaps; papers/2026/08/_sources/arxiv-owner-replay-20260903/20260803/exact-v1-text/2607.29405v1.txt`；公开实现、硬件或训练配置只按正文披露解释，未披露字段不补写。
- **Evaluation contract:** A second literature evaluates agent frameworks directly, but in terms of capability rather than assurance. provide the most comprehensive architectural survey of LLM-based agents, covering memory, planning, tool use, and interaction patterns, but do not define validation dimensions or conduct systematic corpus coding. and offer further architectural surveys with attention to safety risks and governance, but neither treats temporal lifecycle validity or regulatory evidence legibility as first-class assurance targets. More focused work adds trajectory awareness only partially: MultiAgentBench and MAST score coordination outcomes and failure modes, AutoGen-style framework studies expose orchestration patterns, re… 该结果只绑定论文声明的数据、模型、硬件、精度、长度、batch/concurrency 与 evaluator；缺失字段均为 `Not Disclosed`。
- **Proves / does not prove:** 证据支持该受限 workload 中机制可行或暴露既有评价缺口；不证明跨模型、跨硬件、跨领域或生产 SLO 的普遍优势。
- **Trade-off / failure mode:** 新增状态、控制器和观测提高可验证性，但引入版本错配、额外延迟/内存/通信、错误路由及 evaluator bias。全文边界：The first limitation concerns corpus coverage and timing. Agentic AI validation remains terminologically unstable, and terms such as “assurance,” “evaluation,” and “monitoring” span overlapping research programs. The search therefore used expanded queries across five databases, citation chaining from anchor papers, and regulatory documents not consistently indexed in academic databases. Residual risks include terminology emerging after the March 2026 cut-off, metadata inconsistencies in preprint-heavy venues, and the dominance of IEEE Xplore in the merged retrieval set, which may under-represent some machine-learning venues. The second limitation is reviewer dependence. A single reviewer conducted title, abstr…
- **Coexistence / evolution:** 旧方案在低风险、短状态或同构部署中仍成立；新机制只在约束变化使错误代价或状态漂移不可忽略时接手。
- **Books route:** 对照 `PLATFORM-EVALUATION-SYSTEM` 及相邻章节；先进入按日期排序的 writeback queue，根任务合并同 owner 后决定最终写回。
<!-- review:SF-2026-ARXIV-2607-29405:end -->

<!-- review:SF-2026-ARXIV-2607-29431:start -->
### ModelEquivBench: Certifying Multi-Relational Evaluation of LLM-Generated Optimization Models

- **Status / Evidence:** Experimental；exact-v1 HTML 已读取并保存校验和；Score V2=`7`。
- **Problem / old solution:** 既有路径通常把 evaluation evidence and release decision 隐含在模型调用或离线平均指标中；在较小规模、单一模型或无跨请求状态时成本较低，但难以回答谁拥有失败恢复与版本一致性。
- **Changed constraint:** 论文面对的约束由摘要和全文共同限定为：Large language models increasingly generate optimization models from natural language, but existing evaluation often reduces a generated model and its ground truth to a single equivalent/not-equivalent verdict or an execution-success rate--labels that are neither independently checkable nor faithful to the multiple distinct senses in which two formulations can agree. We present ModelEquivBench, a certifying, multi-relational…
- **Mechanism:** exact-v1 的方法段写明：Large language models (LLMs) are increasingly used to turn natural-language problem descriptions into runnable optimization models . Assessing whether a generated model is , however, remains unsettled. Common signals include (i) —the code runs and a solver returns a number—and (ii) a single / verdict against a ground-truth model, produced by value comparison or structural graph matching . Neither by itself answers all of the semantic questions relevant to formulation correctness. Execution success says nothing about whether the model the right thing: a program can build, export, and solve a model that encodes the wrong feasible region or objective. A single global equivalence label, in turn, conflates several…
- **State ownership:** 需要显式绑定 evaluator configuration, dataset slice and result provenance；canonical owner 是 `PLATFORM-EVALUATION-SYSTEM`，而不是论文应用领域本身。
- **Control / data flow:** 数据由工作负载进入机制实现，evaluation controller 决定是否执行、路由、提交或回退；输出必须携带与输入同一版本域的证据。
- **Implementation surface:** 全文 locator=`full-text paragraph 3; papers/2026/08/_sources/arxiv-owner-replay-20260903/20260803/exact-v1-text/2607.29431v1.txt`；公开实现、硬件或训练配置只按正文披露解释，未披露字段不补写。
- **Evaluation contract:** Large language models increasingly generate optimization models from natural language, but existing evaluation often reduces a generated model and its ground truth to a single / verdict or an execution-success rate—labels that are neither independently checkable nor faithful to the multiple distinct senses in which two formulations can agree. We present , a certifying, multi-relational evaluation system that reports a per-pair –: model construction and exact ingestion (), verified representation alignment (), same-space and projected feasible-set relations (, ), objective-order equivalence (), optimal-value equality (), and optimizer-set equivalence (). Each decided entry carries relation-appropriate, independ… 该结果只绑定论文声明的数据、模型、硬件、精度、长度、batch/concurrency 与 evaluator；缺失字段均为 `Not Disclosed`。
- **Proves / does not prove:** 证据支持该受限 workload 中机制可行或暴露既有评价缺口；不证明跨模型、跨硬件、跨领域或生产 SLO 的普遍优势。
- **Trade-off / failure mode:** 新增状态、控制器和观测提高可验证性，但引入版本错配、额外延迟/内存/通信、错误路由及 evaluator bias。全文边界：We evaluate three model snapshots with one generation per condition; broader claims require more models and repeated sampling. The supported envelope covers linear and bounded-discrete structure, while quadratic and general nonlinear models yield . The finite grammar is incomplete, supports only the declared affine-lift schema, and has no certified-negative type. Exact rational verification also incurs resource limits: under the s policy, at least one dimension returns in , , and GPT, Sonnet, and Qwen cells. Results may depend on provider-specific serving, and one sample per cell cannot quantify generation variance. The paired prompt analysis is descriptive—no McNemar comparison survives Holm correction—and th…
- **Coexistence / evolution:** 旧方案在低风险、短状态或同构部署中仍成立；新机制只在约束变化使错误代价或状态漂移不可忽略时接手。
- **Books route:** 对照 `PLATFORM-EVALUATION-SYSTEM` 及相邻章节；先进入按日期排序的 writeback queue，根任务合并同 owner 后决定最终写回。
<!-- review:SF-2026-ARXIV-2607-29431:end -->

<!-- review:SF-2026-ARXIV-2607-29440:start -->
### Beyond Retrieval: Analytic Memory for Multimodal Agents

- **Status / Evidence:** Experimental；exact-v1 HTML 已读取并保存校验和；Score V2=`7`。
- **Problem / old solution:** 既有路径通常把 persistent or derived memory 隐含在模型调用或离线平均指标中；在较小规模、单一模型或无跨请求状态时成本较低，但难以回答谁拥有失败恢复与版本一致性。
- **Changed constraint:** 论文面对的约束由摘要和全文共同限定为：Long-term multimodal memory must support not only retrieving relevant information but also computing over observations accumulated across interactions. Existing systems largely emphasize \emph{retrieval memory}, organizing interaction histories through summaries and indexes to return query-relevant information at multiple granularities, from high-level abstractions to underlying records.
- **Mechanism:** exact-v1 的方法段写明：Recent multimodal memory systems have explored a broad range of designs, including textual abstraction , specialized memory types , hybrid stores , and cross-modal retrieval . Most existing systems follows a retrieve-then-answer paradigm, conditioning an LLM on a bounded set of relevant memories, which we denote as retrieval memory. Such systems are effective at selecting relevant memories from long interaction histories. However, long interaction histories also accumulate recurring observations that collectively form an append-only log. Analytical questions over such histories require complete, correctly scoped records and operations such as filtering, aggregation, ranking, and temporal selection. Relevance-b…
- **State ownership:** 需要显式绑定 memory provenance, version and read/write boundary；canonical owner 是 `AGENT-MEMORY`，而不是论文应用领域本身。
- **Control / data flow:** 数据由工作负载进入机制实现，agent memory manager 决定是否执行、路由、提交或回退；输出必须携带与输入同一版本域的证据。
- **Implementation surface:** 全文 locator=`full-text paragraph 3; papers/2026/08/_sources/arxiv-owner-replay-20260903/20260803/exact-v1-text/2607.29440v1.txt`；公开实现、硬件或训练配置只按正文披露解释，未披露字段不补写。
- **Evaluation contract:** We evaluate on two complex multimodal memory benchmarks. evaluates visual-memory granularity and reasoning through paired multiple-choice and open-ended queries , while assesses long-term conversational memory management . uses EM, BLEU-1 and LLM-judge for evaluation, whereas reports F1, BLEU-1, and LLM-Judge scores. Dataset statistics are provided in Table . We compare against unimodal memory agents, including and , which organize long-term textual interaction histories. Multimodal baselines include dedicated memory agents (, , and ) , which construct persistent memories from dialogue and visual observations, and retrieval-based systems ( and ), which directly retrieve relevant multimodal evidence for answer… 该结果只绑定论文声明的数据、模型、硬件、精度、长度、batch/concurrency 与 evaluator；缺失字段均为 `Not Disclosed`。
- **Proves / does not prove:** 证据支持该受限 workload 中机制可行或暴露既有评价缺口；不证明跨模型、跨硬件、跨领域或生产 SLO 的普遍优势。
- **Trade-off / failure mode:** 新增状态、控制器和观测提高可验证性，但引入版本错配、额外延迟/内存/通信、错误路由及 evaluator bias。全文边界：In this work, we identify a retrieval–analysis mismatch in long-term multimodal agent memory, highlighting the need for executable operations over accumulated experience beyond retrieval. To address this issue, we introduced , which couples hierarchical retrieval memory with schema-induced analytic memory and exposes their distinct capabilities through operation-specific tools. A memory-aware planner further grounds tool selection in the current memory state and progressively composes retrieval and analytic operations. Experiments on MemEye and MemGallery across two answer backbones demonstrate consistent improvements from combining flexible recall with executable analysis.
- **Coexistence / evolution:** 旧方案在低风险、短状态或同构部署中仍成立；新机制只在约束变化使错误代价或状态漂移不可忽略时接手。
- **Books route:** 对照 `AGENT-MEMORY` 及相邻章节；先进入按日期排序的 writeback queue，根任务合并同 owner 后决定最终写回。
<!-- review:SF-2026-ARXIV-2607-29440:end -->

<!-- review:SF-2026-ARXIV-2607-29465:start -->
### CARA: Exact Local Repair with Fresh One-Action Certification for Cloud Consolidation

- **Status / Evidence:** Experimental；exact-v1 HTML 已读取并保存校验和；Score V2=`8`。
- **Problem / old solution:** 既有路径通常把 resource allocation and repair 隐含在模型调用或离线平均指标中；在较小规模、单一模型或无跨请求状态时成本较低，但难以回答谁拥有失败恢复与版本一致性。
- **Changed constraint:** 论文面对的约束由摘要和全文共同限定为：Simulator-based placement pipelines may inspect many repairs but deploy only when several reliability criteria improve together. Reusing search scenes to test the selected action invalidates nominal evidence, while scalarization can trade away the weakest criterion.
- **Mechanism:** exact-v1 的方法段写明：This setting creates the two failures in Figure . First, a weighted objective can purchase a large average gain by worsening the weakest reliability coordinate. Second, testing the winner on the scenes used to find it treats an adaptive choice as if it had been fixed in advance. Predict-then-optimize methods explicitly couple predictions to downstream decisions , while decision-focused learning optimizes through that downstream objective . Neither coupling by itself makes reused post-selection evidence valid. Classical sample splitting addresses this information leak by separating adaptive choice from inference .
- **State ownership:** 需要显式绑定 placement/allocation/certification state；canonical owner 是 `PLATFORM-GPU-SCHEDULER`，而不是论文应用领域本身。
- **Control / data flow:** 数据由工作负载进入机制实现，resource controller 决定是否执行、路由、提交或回退；输出必须携带与输入同一版本域的证据。
- **Implementation surface:** 全文 locator=`full-text paragraph 3; papers/2026/08/_sources/arxiv-owner-replay-20260903/20260803/exact-v1-text/2607.29465v1.txt`；公开实现、硬件或训练配置只按正文披露解释，未披露字段不补写。
- **Evaluation contract:** All result blocks are derived from the same locked analysis specification and complete 512-cell record. They include all 128 environments, four contexts, five primary endpoints, structural host checks, and every fallback. Analysis proceeds only after verifying cell completeness, comparator and anchor identity, and all required result fields. 该结果只绑定论文声明的数据、模型、硬件、精度、长度、batch/concurrency 与 evaluator；缺失字段均为 `Not Disclosed`。
- **Proves / does not prove:** 证据支持该受限 workload 中机制可行或暴露既有评价缺口；不证明跨模型、跨硬件、跨领域或生产 SLO 的普遍优势。
- **Trade-off / failure mode:** 新增状态、控制器和观测提高可验证性，但引入版本错配、额外延迟/内存/通信、错误路由及 evaluator bias。全文边界：makes adaptive simulator-based placement repair auditable by coupling exact local proposal recovery to a one-use fresh deployment comparison. Its packing-specific bound returns the declared distinct top-, while fresh Certification controls false four-way improvement for the committed action independently of upstream search complexity. In the frozen study, the complete fail-closed policy improved all five terminal endpoints over the incumbent in every environment cluster. The five-endpoint incumbent-relative intersection–union test advanced; every Evaluation pair also retained exact precommitted host-target equality by construction. The durable contribution is the separation of proposal fidelity, decision valid…
- **Coexistence / evolution:** 旧方案在低风险、短状态或同构部署中仍成立；新机制只在约束变化使错误代价或状态漂移不可忽略时接手。
- **Books route:** 对照 `PLATFORM-GPU-SCHEDULER` 及相邻章节；先进入按日期排序的 writeback queue，根任务合并同 owner 后决定最终写回。
<!-- review:SF-2026-ARXIV-2607-29465:end -->

<!-- review:SF-2026-ARXIV-2607-29468:start -->
### Self-Play Meets Skill Evolution: Self-Evolving Search Agents that Pose, Solve, and Remember

- **Status / Evidence:** Experimental；exact-v1 HTML 已读取并保存校验和；Score V2=`6`。
- **Problem / old solution:** 既有路径通常把 planning under partial observability 隐含在模型调用或离线平均指标中；在较小规模、单一模型或无跨请求状态时成本较低，但难以回答谁拥有失败恢复与版本一致性。
- **Changed constraint:** 论文面对的约束由摘要和全文共同限定为：Self-play agents can generate training problems without questions from target benchmarks, but their curricula lack persistent state: failures affect gradients yet do not explicitly shape future practice. External skill memories preserve procedural experience but are typically learned from fixed task distributions.
- **Mechanism:** exact-v1 的方法段写明：Key Laboratory of Computing Power Internet and Service Computing, Shandong Fundamental Research Center for Computer Science
- **State ownership:** 需要显式绑定 belief/plan/rollback state；canonical owner 是 `AGENT-PLANNING`，而不是论文应用领域本身。
- **Control / data flow:** 数据由工作负载进入机制实现，planner 决定是否执行、路由、提交或回退；输出必须携带与输入同一版本域的证据。
- **Implementation surface:** 全文 locator=`full-text paragraph 3; papers/2026/08/_sources/arxiv-owner-replay-20260903/20260803/exact-v1-text/2607.29468v1.txt`；公开实现、硬件或训练配置只按正文披露解释，未披露字段不补写。
- **Evaluation contract:** We evaluate on 3,125 held-out questions from seven benchmarks. Natural Questions (NQ) , TriviaQA , and PopQA primarily test open-domain factual retrieval; HotpotQA , 2WikiMultiHopQA (2Wiki) , and MuSiQue emphasize compositional multi-hop search; and Bamboogle provides a compact, challenging set of 125 questions that are difficult to answer without explicit decomposition. We use 500 examples from each of the first six datasets and all 125 Bamboogle examples. This mix tests whether the skills learned from self-posed problems transfer across both fact-oriented and multi-hop distributions. 该结果只绑定论文声明的数据、模型、硬件、精度、长度、batch/concurrency 与 evaluator；缺失字段均为 `Not Disclosed`。
- **Proves / does not prove:** 证据支持该受限 workload 中机制可行或暴露既有评价缺口；不证明跨模型、跨硬件、跨领域或生产 SLO 的普遍优势。
- **Trade-off / failure mode:** 新增状态、控制器和观测提高可验证性，但引入版本错配、额外延迟/内存/通信、错误路由及 evaluator bias。全文边界：SESA couples self-posed self-play with persistent skill evolution by distilling frontier failures into a maintained memory that changes subsequent training. Across model scales, families, and search-specialized initializations, this closed loop consistently improves average accuracy over SSP, with component ablations identifying online failure distillation as the largest contributor. The Off/On evaluation further shows that skill-conditioned training leaves substantial capability in the model parameters, while the retained bank provides smaller, task-dependent inference gains. SESA thus treats procedural memory as evolving training state rather than an inference-only prompt, supporting both memory-free and mem…
- **Coexistence / evolution:** 旧方案在低风险、短状态或同构部署中仍成立；新机制只在约束变化使错误代价或状态漂移不可忽略时接手。
- **Books route:** 对照 `AGENT-PLANNING` 及相邻章节；先进入按日期排序的 writeback queue，根任务合并同 owner 后决定最终写回。
<!-- review:SF-2026-ARXIV-2607-29468:end -->

<!-- review:SF-2026-ARXIV-2607-29484:start -->
### Evidence-Type Competition: When Can Interventional Data Teach Language Models Causal Direction?

- **Status / Evidence:** Experimental；exact-v1 HTML 已读取并保存校验和；Score V2=`6`。
- **Problem / old solution:** 既有路径通常把 training evidence construction 隐含在模型调用或离线平均指标中；在较小规模、单一模型或无跨请求状态时成本较低，但难以回答谁拥有失败恢复与版本一致性。
- **Changed constraint:** 论文面对的约束由摘要和全文共同限定为：Interventional data is widely regarded as the gold standard for teaching models causal reasoning. We test this assumption in a fully controlled synthetic environment pitting observational correlation against causal effect, and find it fails instructively.
- **Mechanism:** exact-v1 的方法段写明：Per-world three-way classification: (, sign consistent with ) / () / (; is always positive in the evaluation family). The magnitude gate eliminates false positives in which a numerically flat line is counted as a hit. Even if the model were a , probe evidence is itself a single-draw random variable (4 probes, one sample each), and its regression slope carries an intrinsic sign-error rate. Writing the oracle grid response as , single-shot evaluation estimates with heteroscedastic inherited from , so that
- **State ownership:** 需要显式绑定 sample lineage and acceptance state；canonical owner 是 `TRAIN-DATA`，而不是论文应用领域本身。
- **Control / data flow:** 数据由工作负载进入机制实现，data pipeline 决定是否执行、路由、提交或回退；输出必须携带与输入同一版本域的证据。
- **Implementation surface:** 全文 locator=`Evaluation Methodology; papers/2026/08/_sources/arxiv-owner-replay-20260903/20260803/exact-v1-text/2607.29484v1.txt`；公开实现、硬件或训练配置只按正文披露解释，未披露字段不补写。
- **Evaluation contract:** Per-world three-way classification: (, sign consistent with ) / () / (; is always positive in the evaluation family). The magnitude gate eliminates false positives in which a numerically flat line is counted as a hit. Even if the model were a , probe evidence is itself a single-draw random variable (4 probes, one sample each), and its regression slope carries an intrinsic sign-error rate. Writing the oracle grid response as , single-shot evaluation estimates with heteroscedastic inherited from , so that 该结果只绑定论文声明的数据、模型、硬件、精度、长度、batch/concurrency 与 evaluator；缺失字段均为 `Not Disclosed`。
- **Proves / does not prove:** 证据支持该受限 workload 中机制可行或暴露既有评价缺口；不证明跨模型、跨硬件、跨领域或生产 SLO 的普遍优势。
- **Trade-off / failure mode:** 新增状态、控制器和观测提高可验证性，但引入版本错配、额外延迟/内存/通信、错误路由及 evaluator bias。全文边界：(1) Interventional evidence is to teach causal-direction interpolation (C2: 41/50, true reversal rate ). (2) The observational-correlation prior the use of interventional evidence at inference time (C1: 18/50, 19 reversed), independently of probe dose (E1a). (3) The suppression is an phenomenon: erasing observational evidence immediately releases the suppressed ability (E1b: ). (4) The shortcut is —the observational correlation is correct for most random queries (confounded pairs are only )—and deepens with training. (5) Training-distribution priors are : the learnable in-distribution regularity (“effects are positive”) can be removed by sign randomization, but an out-of-distribution default persists underneat…
- **Coexistence / evolution:** 旧方案在低风险、短状态或同构部署中仍成立；新机制只在约束变化使错误代价或状态漂移不可忽略时接手。
- **Books route:** 对照 `TRAIN-DATA` 及相邻章节；先进入按日期排序的 writeback queue，根任务合并同 owner 后决定最终写回。
<!-- review:SF-2026-ARXIV-2607-29484:end -->

<!-- review:SF-2026-ARXIV-2607-29494:start -->
### Adaptive FastOPD: Progress-Aware Rollout Horizon Expansion for Efficient On-Policy Distillation

- **Status / Evidence:** Experimental；exact-v1 HTML 已读取并保存校验和；Score V2=`6`。
- **Problem / old solution:** 既有路径通常把 on-policy reasoning optimization 隐含在模型调用或离线平均指标中；在较小规模、单一模型或无跨请求状态时成本较低，但难以回答谁拥有失败恢复与版本一致性。
- **Changed constraint:** 论文面对的约束由摘要和全文共同限定为：On-policy distillation (OPD) provides dense teacher supervision along student-generated trajectories, but its online rollout process incurs substantial computational cost, particularly when a few long responses delay batch completion. Existing acceleration methods typically control rollout length using fixed budgets or absolute teacher--student agreement thresholds, which may not reflect learning progress across different mod…
- **Mechanism:** exact-v1 的方法段写明：To alleviate these issues, recent work has explored shortening, progressively expanding, or selectively continuing OPD rollouts . FastOPD observes that useful supervision is often concentrated near the beginning of a response and progressively increases the horizon with a fixed schedule . Prune-OPD detects local student–teacher drift and truncates supervision after an overlap-based reliability score crosses a threshold . Early Stopping Rollout (ESR) argues that teacher supervision becomes less corrective at later positions and therefore restricts rollout generation to a short predefined rollout horizon . Collectively, these studies show that truncating or selectively extending rollouts can accelerate OPD while…
- **State ownership:** 需要显式绑定 rollout/reward/advantage state；canonical owner 是 `TRAIN-GRPO`，而不是论文应用领域本身。
- **Control / data flow:** 数据由工作负载进入机制实现，post-training loop 决定是否执行、路由、提交或回退；输出必须携带与输入同一版本域的证据。
- **Implementation surface:** 全文 locator=`full-text paragraph 3; papers/2026/08/_sources/arxiv-owner-replay-20260903/20260803/exact-v1-text/2607.29494v1.txt`；公开实现、硬件或训练配置只按正文披露解释，未披露字段不补写。
- **Evaluation contract:** We train all methods on DAPO-Math-17K using the verl framework , with vLLM for rollout generation . We evaluate two teacher–student configurations: JustRL-DeepSeek-1.5B with DeepSeek-R1-Distill-Qwen-1.5B , and Qwen3-8B-Base with Qwen3-1.7B-Base . All experiments run on a single node with four NVIDIA H200 140GB GPUs, with the actor trained in FP32. Each generation batch contains 64 inputs and four responses per input. We use a learning rate of , student-selected top- candidates with student-probability weighting, and no additional KL regularization. All runs use one epoch without data shuffling, corresponding to 279 optimization steps. Both adaptive and fixed schedules start from a rollout horizon of 1,024 toke… 该结果只绑定论文声明的数据、模型、硬件、精度、长度、batch/concurrency 与 evaluator；缺失字段均为 `Not Disclosed`。
- **Proves / does not prove:** 证据支持该受限 workload 中机制可行或暴露既有评价缺口；不证明跨模型、跨硬件、跨领域或生产 SLO 的普遍优势。
- **Trade-off / failure mode:** 新增状态、控制器和观测提高可验证性，但引入版本错配、额外延迟/内存/通信、错误路由及 evaluator bias。全文边界：We introduced Adaptive FastOPD, a progress-aware rollout-horizon expansion strategy for efficient on-policy distillation. Rather than triggering horizon expansion at a fixed step interval or from an absolute threshold on the raw teacher–student signals, Adaptive FastOPD evaluates learning progress relative to the initial state of each horizon. It combines four signals to monitor optimization near the current boundary region and expands the horizon only after the aggregated progress has plateaued and the available length is sufficiently utilized. The utilization condition also avoids extending the horizon when only a small number of long responses would increase rollout time. Experiments across two teacher–stud…
- **Coexistence / evolution:** 旧方案在低风险、短状态或同构部署中仍成立；新机制只在约束变化使错误代价或状态漂移不可忽略时接手。
- **Books route:** 对照 `TRAIN-GRPO` 及相邻章节；先进入按日期排序的 writeback queue，根任务合并同 owner 后决定最终写回。
<!-- review:SF-2026-ARXIV-2607-29494:end -->

<!-- review:SF-2026-ARXIV-2607-29503:start -->
### The Grokked Illusion: True Equilibrium Mitigates Catastrophic Forgetting

- **Status / Evidence:** Experimental；exact-v1 HTML 已读取并保存校验和；Score V2=`6`。
- **Problem / old solution:** 既有路径通常把 representation learning stability 隐含在模型调用或离线平均指标中；在较小规模、单一模型或无跨请求状态时成本较低，但难以回答谁拥有失败恢复与版本一致性。
- **Changed constraint:** 论文面对的约束由摘要和全文共同限定为：While neural networks are typically evaluated by their training and test performance, these metrics do not reveal how robust a learned representation is. Recent studies have shown that solutions occupying larger volumes in parameter space, as quantified by Boltzmann entropy, often exhibit superior generalizability compared to those reached by conventional optimization, a phenomenon known as the high entropy advantage.
- **Mechanism:** exact-v1 的方法段写明：Generalization performance has long been a key metric for evaluating machine learning models, reflecting the ability of neural networks (NNs) to learn knowledge and apply it to unknown data. Yet a model that generalizes perfectly to a test set may still be fragile: parameter updates caused by memorizing new input data may lead to a catastrophic collapse of its previously acquired knowledge. This disconnect between generalization and robustness has been observed across a wide range of settings, from adversarial examples to catastrophic forgetting in continual learning , and it raises a fundamental question: what properties of a NN determine not only its generalizability, but also its robustness to interference?
- **State ownership:** 需要显式绑定 parameter and optimizer trajectory；canonical owner 是 `TRAIN-PRETRAINING`，而不是论文应用领域本身。
- **Control / data flow:** 数据由工作负载进入机制实现，pretraining runtime 决定是否执行、路由、提交或回退；输出必须携带与输入同一版本域的证据。
- **Implementation surface:** 全文 locator=`full-text paragraph 3; papers/2026/08/_sources/arxiv-owner-replay-20260903/20260803/exact-v1-text/2607.29503v1.txt`；公开实现、硬件或训练配置只按正文披露解释，未披露字段不补写。
- **Evaluation contract:** To investigate the mechanistic basis of the observed robustness differences, we perform singular value decomposition (SVD) on the weight matrices of individual layers before and after noise injection. For a weight matrix , let its singular values be , where . We define the normalized singular value distribution as . Following , the (ER) is defined as: which quantifies the number of significant singular directions and serves as a measure of the representational richness of the layer. A higher ER indicates a more uniform singular value spectrum, implying that the layer utilizes a broader set of feature dimensions. 该结果只绑定论文声明的数据、模型、硬件、精度、长度、batch/concurrency 与 evaluator；缺失字段均为 `Not Disclosed`。
- **Proves / does not prove:** 证据支持该受限 workload 中机制可行或暴露既有评价缺口；不证明跨模型、跨硬件、跨领域或生产 SLO 的普遍优势。
- **Trade-off / failure mode:** 新增状态、控制器和观测提高可验证性，但引入版本错配、额外延迟/内存/通信、错误路由及 evaluator bias。全文边界：In this work, we have extended the high-entropy advantage beyond generalization to the domain of robustness. Using noise injection experiments on modular arithmetic tasks, we demonstrated that high-entropy NNs sampled from the Boltzmann entropy landscape maintain approximately 95% test accuracy on the original task after memorizing new noisy data, whereas AdamW-trained NNs suffer from catastrophic forgetting, dropping to about 75% under the same conditions. We term this hidden fragility behind apparent generalization the . Through singular value decomposition of NN weights, we revealed that high-entropy NNs possess significantly higher effective rank in attention and MLP layers both before and after noise inje…
- **Coexistence / evolution:** 旧方案在低风险、短状态或同构部署中仍成立；新机制只在约束变化使错误代价或状态漂移不可忽略时接手。
- **Books route:** 对照 `TRAIN-PRETRAINING` 及相邻章节；先进入按日期排序的 writeback queue，根任务合并同 owner 后决定最终写回。
<!-- review:SF-2026-ARXIV-2607-29503:end -->

<!-- review:SF-2026-ARXIV-2607-29516:start -->
### From Code Review to Code Critique: Intent, Drift, and Spotlight for AI-Generated Diffs at Scale

- **Status / Evidence:** Experimental；exact-v1 HTML 已读取并保存校验和；Score V2=`7`。
- **Problem / old solution:** 既有路径通常把 evaluation evidence and release decision 隐含在模型调用或离线平均指标中；在较小规模、单一模型或无跨请求状态时成本较低，但难以回答谁拥有失败恢复与版本一致性。
- **Changed constraint:** 论文面对的约束由摘要和全文共同限定为：AI coding agents are generating code at volumes that exceed the capacity of traditional peer review. At the same time, existing AI code review tools over-index on low-value suggestions such as style and best practices while under-indexing on the concerns human reviewers prioritize most: correctness, security, and performance.
- **Mechanism:** exact-v1 的方法段写明：To understand what expert human reviewers focus on, we derive a taxonomy of code review themes and measure the distribution of human review activity across the resulting themes. We use the CR2 dataset, which contains 18,000 human-reviewed diffs, each represented as a triplet of the original code, the code review comment, and the resulting code change. All entries were curated to ensure they represent actionable reviews that led to positive outcomes, specifically code changes that addressed the reviewer’s feedback. We additionally collected 712 AI-generated code reviews from the current code review system, filtered to include only reviews that received positive interactions from engineers, had at least one repl…
- **State ownership:** 需要显式绑定 evaluator configuration, dataset slice and result provenance；canonical owner 是 `PLATFORM-EVALUATION-SYSTEM`，而不是论文应用领域本身。
- **Control / data flow:** 数据由工作负载进入机制实现，evaluation controller 决定是否执行、路由、提交或回退；输出必须携带与输入同一版本域的证据。
- **Implementation surface:** 全文 locator=`Methodology for RQ 1. Taxonomy of Code Review Concerns; papers/2026/08/_sources/arxiv-owner-replay-20260903/20260803/exact-v1-text/2607.29516v1.txt`；公开实现、硬件或训练配置只按正文披露解释，未披露字段不补写。
- **Evaluation contract:** After validating each component through offline benchmarks, we progressively rolled out the ARCTIC code review workflow. ARCTIC serves as the intelligence layer powering a reimagined code review experience that enables author self-review. We describe our methodology, metrics, and progressive rollout strategy below. ARCTIC is a platform API that downstream surfaces consume independently. Each component, Intent, Drift, Spotlight, and Diff Categorization, is served as a separate signal. The funnel operates as follows: a diff is created, ARCTIC computes signals over it, and if the diff is eligible for self-review, the author is presented with an AI-assisted self-review experience. The author attests that the diff… 该结果只绑定论文声明的数据、模型、硬件、精度、长度、batch/concurrency 与 evaluator；缺失字段均为 `Not Disclosed`。
- **Proves / does not prove:** 证据支持该受限 workload 中机制可行或暴露既有评价缺口；不证明跨模型、跨硬件、跨领域或生产 SLO 的普遍优势。
- **Trade-off / failure mode:** 新增状态、控制器和观测提高可验证性，但引入版本错配、额外延迟/内存/通信、错误路由及 evaluator bias。全文边界：Have a free development cycle? Help support accessibility at arXiv! Our collaborators at LaTeXML maintain a , and welcome .
- **Coexistence / evolution:** 旧方案在低风险、短状态或同构部署中仍成立；新机制只在约束变化使错误代价或状态漂移不可忽略时接手。
- **Books route:** 对照 `PLATFORM-EVALUATION-SYSTEM` 及相邻章节；先进入按日期排序的 writeback queue，根任务合并同 owner 后决定最终写回。
<!-- review:SF-2026-ARXIV-2607-29516:end -->

<!-- review:SF-2026-ARXIV-2607-29529:start -->
### AuditCoder: Responsibility-Preserving Task Graphs for Auditable Code Generation and Bounded Repair

- **Status / Evidence:** Experimental；exact-v1 HTML 已读取并保存校验和；Score V2=`6`。
- **Problem / old solution:** 既有路径通常把 durable multi-step execution 隐含在模型调用或离线平均指标中；在较小规模、单一模型或无跨请求状态时成本较低，但难以回答谁拥有失败恢复与版本一致性。
- **Changed constraint:** 论文面对的约束由摘要和全文共同限定为：Code generators return programs, but typically do not preserve the construction record needed to connect a failure to the decision that produced the affected code or to delimit a justified repair. We present AuditCoder, which treats the program and an auditable construction trace as joint outputs.
- **Mechanism:** exact-v1 的方法段写明：Given a natural-language programming task , returns an executable program together with a structured construction trace : Here is the contract-annotated task graph, contains responsibility records, stores validation evidence, and is the append-only repair history. For implementation node , the record is
- **State ownership:** 需要显式绑定 task, evidence and checkpoint state；canonical owner 是 `AGENT-WORKFLOW`，而不是论文应用领域本身。
- **Control / data flow:** 数据由工作负载进入机制实现，workflow engine 决定是否执行、路由、提交或回退；输出必须携带与输入同一版本域的证据。
- **Implementation surface:** 全文 locator=`Method; papers/2026/08/_sources/arxiv-owner-replay-20260903/20260803/exact-v1-text/2607.29529v1.txt`；公开实现、硬件或训练配置只按正文披露解释，未披露字段不补写。
- **Evaluation contract:** We organize the evaluation around three questions. tests whether evidence-guided bounded repair can recover accuracy lost when generation is decomposed into auditable graph units. examines whether the retained records remain structurally usable and support evidence-bounded repair transactions. studies when such boundaries are appropriate and where their computational cost arises. 该结果只绑定论文声明的数据、模型、硬件、精度、长度、batch/concurrency 与 evaluator；缺失字段均为 `Not Disclosed`。
- **Proves / does not prove:** 证据支持该受限 workload 中机制可行或暴露既有评价缺口；不证明跨模型、跨硬件、跨领域或生产 SLO 的普遍优势。
- **Trade-off / failure mode:** 新增状态、控制器和观测提高可验证性，但引入版本错配、额外延迟/内存/通信、错误路由及 evaluator bias。全文边界：follows one principle: a generation-time subproblem remains responsible for its implementation, evidence, and interventions. Its contract-annotated task graph maps failures to evidence-supported nodes or branches, repairs them, reuses the frozen complement, or abstains without a defensible boundary. As a repair index, the graph recovers much of the accuracy lost to decomposition, but remains below the strongest functional baselines. The audit exposes the bottleneck: trace links persist, but only 26 of 60 failures support a node or branch boundary, while planning and global fallback dominate cost. It suits tasks with stable, locally testable artifacts. Repositories still require better boundaries and compact cr…
- **Coexistence / evolution:** 旧方案在低风险、短状态或同构部署中仍成立；新机制只在约束变化使错误代价或状态漂移不可忽略时接手。
- **Books route:** 对照 `AGENT-WORKFLOW` 及相邻章节；先进入按日期排序的 writeback queue，根任务合并同 owner 后决定最终写回。
<!-- review:SF-2026-ARXIV-2607-29529:end -->

<!-- review:SF-2026-ARXIV-2607-29545:start -->
### MoRoute: Dynamic Routing for In-Context Multimodal Video Generation

- **Status / Evidence:** Experimental；exact-v1 HTML 已读取并保存校验和；Score V2=`6`。
- **Problem / old solution:** 既有路径通常把 iterative or routed generation 隐含在模型调用或离线平均指标中；在较小规模、单一模型或无跨请求状态时成本较低，但难以回答谁拥有失败恢复与版本一致性。
- **Changed constraint:** 论文面对的约束由摘要和全文共同限定为：Multimodal video generation aims to generate and edit videos conditioned on arbitrary combinations of text, images, and videos within a single model, allowing diverse tasks to share complementary data and generative priors. Unifying these tasks requires multimodal understanding of diverse conditions, which is typically provided by a pretrained vision-language model (VLM).
- **Mechanism:** exact-v1 的方法段写明：Recent methods replace frozen text encoders with VLMs to provide richer multimodal conditioning for video diffusion models. One line of work extracts a single VLM representation, typically the final-layer hidden states, and feeds it to the DiT through query connectors or lightweight MLPs . Another line designs adapters or condition bridges that aggregate multimodal signals before injection, such as MLLM vision heads , understanding–generation stream connectors , caption-mediated adapters , or ViT semantic bottlenecks . The most closely related work is OmniWeaving’s DeepStacking , which extracts hidden states from multiple VLM layers and injects them into early DiT blocks via additive residuals. However, its la…
- **State ownership:** 需要显式绑定 proposal/correction/sample state；canonical owner 是 `MULTIMODAL-GENERATIVE-PARADIGMS`，而不是论文应用领域本身。
- **Control / data flow:** 数据由工作负载进入机制实现，generation scheduler 决定是否执行、路由、提交或回退；输出必须携带与输入同一版本域的证据。
- **Implementation surface:** 全文 locator=`Multimodal Video Generation Frameworks; papers/2026/08/_sources/arxiv-owner-replay-20260903/20260803/exact-v1-text/2607.29545v1.txt`；公开实现、硬件或训练配置只按正文披露解释，未披露字段不补写。
- **Evaluation contract:** We evaluate MoRoute on three benchmarks covering multimodal video generation and editing: covers Compositional Multi-Image-to-Video (MI2V), Implicit Image-to-Video (I2V), Interpolative Dual-Image-to-Video (DI2V), and Text-Image-Video-to-Video (TIV2V) with local replacement, background change, and object addition. focuses on Text-Video-to-Video (TV2V) editing. It includes background change, camera edit, creative edit, global style transfer, local add/change/remove, and subtitle edit. targets reference-guided video editing. We compare with five methods representing different condition injection paradigms (Sec. ): OmniWeaving , Bernini , Kiwi-Edit , Omni-Video 2 , and VACE . Since not all methods support every co… 该结果只绑定论文声明的数据、模型、硬件、精度、长度、batch/concurrency 与 evaluator；缺失字段均为 `Not Disclosed`。
- **Proves / does not prove:** 证据支持该受限 workload 中机制可行或暴露既有评价缺口；不证明跨模型、跨硬件、跨领域或生产 SLO 的普遍优势。
- **Trade-off / failure mode:** 新增状态、控制器和观测提高可验证性，但引入版本错配、额外延迟/内存/通信、错误路由及 evaluator bias。全文边界：We presented MoRoute, a unified framework for multimodal video generation and editing. The key idea is to connect a frozen VLM and a pretrained video DiT through block-wise dynamic layer routing: instead of relying on the final VLM layer or a fixed set of layers, each DiT block selects the VLM layer most relevant to the current input, more effectively leveraging the VLM’s hierarchical representations. We also introduced an in-context multi-condition video diffusion architecture that supports text, image, and video conditions in one model. Slotted temporal RoPE, sparse attention, and dual timestep modulation help the DiT handle clean conditioning tokens and noisy target tokens together, and a progressive three-…
- **Coexistence / evolution:** 旧方案在低风险、短状态或同构部署中仍成立；新机制只在约束变化使错误代价或状态漂移不可忽略时接手。
- **Books route:** 对照 `MULTIMODAL-GENERATIVE-PARADIGMS` 及相邻章节；先进入按日期排序的 writeback queue，根任务合并同 owner 后决定最终写回。
<!-- review:SF-2026-ARXIV-2607-29545:end -->

<!-- review:SF-2026-ARXIV-2607-29549:start -->
### AMTFV: Agentic Mathematical Tool-Flow Verification for LLM Self-Correction

- **Status / Evidence:** Experimental；exact-v1 HTML 已读取并保存校验和；Score V2=`7`。
- **Problem / old solution:** 既有路径通常把 tool acquisition or authorization 隐含在模型调用或离线平均指标中；在较小规模、单一模型或无跨请求状态时成本较低，但难以回答谁拥有失败恢复与版本一致性。
- **Changed constraint:** 论文面对的约束由摘要和全文共同限定为：Large language models have demonstrated strong mathematical problem-solving capabilities, yet reliably verifying their candidate answers remains challenging. Existing representative methods mainly revise outputs through natural-language reflection or assist verification by directly generating verification programs; the former may not reliably support exact computation, whereas the latter prematurely couples mathematical model…
- **Mechanism:** exact-v1 的方法段写明：We develop , an agentic mathematical verification and correction framework using MTF as its core interface. Given a problem and an initial candidate answer extracted from the initial response, the system verifies, provides feedback on, and revises the candidate. Whenever verification or revision requires reliable computation, the agents invoke mathematical tools through the standardized MTF interface. As shown in Figure , has three components. The left verification and correction module contains a verification agent, an answer-revision agent, and a verification-workflow revision agent. The central standardized MTF interface transmits computation requests and tool results. In the right mathematical tool invocat…
- **State ownership:** 需要显式绑定 tool schema, capability and return provenance；canonical owner 是 `AGENT-TOOL-CALLING`，而不是论文应用领域本身。
- **Control / data flow:** 数据由工作负载进入机制实现，tool-policy controller 决定是否执行、路由、提交或回退；输出必须携带与输入同一版本域的证据。
- **Implementation surface:** 全文 locator=`Method; papers/2026/08/_sources/arxiv-owner-replay-20260903/20260803/exact-v1-text/2607.29549v1.txt`；公开实现、硬件或训练配置只按正文披露解释，未披露字段不补写。
- **Evaluation contract:** We evaluate for mathematical reasoning verification and correction against self-correction, reasoning-enhanced, and verification-enhanced methods. We analyze its performance and gains through cross-model architectural comparisons, correction-state transitions, and verification-complexity bins. The supplementary material covers iteration budgets, correlations with empirical difficulty, MTF call types (see Supplementary Figure ), and case processes. 该结果只绑定论文声明的数据、模型、硬件、精度、长度、batch/concurrency 与 evaluator；缺失字段均为 `Not Disclosed`。
- **Proves / does not prove:** 证据支持该受限 workload 中机制可行或暴露既有评价缺口；不证明跨模型、跨硬件、跨领域或生产 SLO 的普遍优势。
- **Trade-off / failure mode:** 新增状态、控制器和观测提高可验证性，但引入版本错配、额外延迟/内存/通信、错误路由及 evaluator bias。全文边界：We introduce to decouple verification-target design from low-level implementation in mathematical backward verification. MTF separates mathematical verification modeling from tool execution, and its returned results support candidate adjudication and self-correction. Experiments show that outperforms representative correction and verification methods across mathematical reasoning datasets and base models, with larger gains at medium or high verification complexity. Further correction-state analysis indicates that these gains primarily arise from correcting initially incorrect answers while preserving initially correct ones, rather than from aggressive rewriting. Future work will extend the framework beyond mat…
- **Coexistence / evolution:** 旧方案在低风险、短状态或同构部署中仍成立；新机制只在约束变化使错误代价或状态漂移不可忽略时接手。
- **Books route:** 对照 `AGENT-TOOL-CALLING` 及相邻章节；先进入按日期排序的 writeback queue，根任务合并同 owner 后决定最终写回。
<!-- review:SF-2026-ARXIV-2607-29549:end -->

<!-- review:SF-2026-ARXIV-2607-29559:start -->
### LEMUR: Learning to Align with Multi-Objective Reinforcement Learning from Preference Feedback

- **Status / Evidence:** Experimental；exact-v1 HTML 已读取并保存校验和；Score V2=`6`。
- **Problem / old solution:** 既有路径通常把 preference/reward optimization 隐含在模型调用或离线平均指标中；在较小规模、单一模型或无跨请求状态时成本较低，但难以回答谁拥有失败恢复与版本一致性。
- **Changed constraint:** 论文面对的约束由摘要和全文共同限定为：Reinforcement Learning (RL) systems are typically trained using a single, well-specified scalar reward function. However, real-world decision-making tasks often involve multiple, competing objectives, such as performance versus efficiency, where ground-truth reward functions are difficult to specify or inaccessible.
- **Mechanism:** exact-v1 的方法段写明：Real-world tasks often involve objectives , such as balancing speed versus safety in autonomous driving , or throughput versus energy efficiency in robotics .
- **State ownership:** 需要显式绑定 preference, reward and policy-version state；canonical owner 是 `TRAIN-RLHF`，而不是论文应用领域本身。
- **Control / data flow:** 数据由工作负载进入机制实现，post-training controller 决定是否执行、路由、提交或回退；输出必须携带与输入同一版本域的证据。
- **Implementation surface:** 全文 locator=`full-text paragraph 3; papers/2026/08/_sources/arxiv-owner-replay-20260903/20260803/exact-v1-text/2607.29559v1.txt`；公开实现、硬件或训练配置只按正文披露解释，未披露字段不补写。
- **Evaluation contract:** Our experiments address three questions: (1) Can LEMUR learn multi-objective policies that balance multiple reward models from teachers? (2) How does LEMUR compare to existing baselines on multi-objective benchmarks? (3) Does explicitly learning multiple reward models for conflicting feedback outperform aggregating feedback into a single reward model? For all experiments, we report the mean across five random seeds with standard error. Additional implementation details are reported in Appendices & . We evaluate LEMUR on high-dimensional environments from the benchmark . Following standard practice in PbRL , we use scripted teachers that generate feedback according to the components of the ground-truth vector r… 该结果只绑定论文声明的数据、模型、硬件、精度、长度、batch/concurrency 与 evaluator；缺失字段均为 `Not Disclosed`。
- **Proves / does not prove:** 证据支持该受限 workload 中机制可行或暴露既有评价缺口；不证明跨模型、跨硬件、跨领域或生产 SLO 的普遍优势。
- **Trade-off / failure mode:** 新增状态、控制器和观测提高可验证性，但引入版本错配、额外延迟/内存/通信、错误路由及 evaluator bias。全文边界：We propose LEMUR, a framework for Multi-Objective RL in domains where reward functions are unknown and must be inferred from the conflicting preferences of multiple teachers. LEMUR jointly learns the objectives and the policies that balance them, without expert demonstrations, pre-defined rewards, or a priori aggregation rules that existing methods require. Across multi-objective RL control and robotic manipulation benchmark environments, LEMUR outperforms aggregation baselines and recent preference-based multi-objective methods, and remains robust to label noise, reduced feedback budgets, and scaling to additional objectives. Several directions for future work are as follows. Our evaluation uses scripted teac…
- **Coexistence / evolution:** 旧方案在低风险、短状态或同构部署中仍成立；新机制只在约束变化使错误代价或状态漂移不可忽略时接手。
- **Books route:** 对照 `TRAIN-RLHF` 及相邻章节；先进入按日期排序的 writeback queue，根任务合并同 owner 后决定最终写回。
<!-- review:SF-2026-ARXIV-2607-29559:end -->

<!-- review:SF-2026-ARXIV-2607-29569:start -->
### Safe Vision Language Action Models via Barrier Enhanced Flow Matching

- **Status / Evidence:** Experimental；exact-v1 HTML 已读取并保存校验和；Score V2=`6`。
- **Problem / old solution:** 既有路径通常把 closed-loop physical action 隐含在模型调用或离线平均指标中；在较小规模、单一模型或无跨请求状态时成本较低，但难以回答谁拥有失败恢复与版本一致性。
- **Changed constraint:** 论文面对的约束由摘要和全文共同限定为：This article presents a modular inference framework that integrates Flow Matching generative models with formal Control Barrier Function (CBF) safety guarantees. Unlike existing methods that apply external safety filters to a model's final output, our approach modifies the Flow Matching denoising process within the model to inherently generate safe trajectories.
- **Mechanism:** exact-v1 的方法段写明：Modern VLAs like Physical Intelligence and SmolVLA consist of two transformers with separate sets of weights, connected via a block-wise causal attention mask. The first set of transformer weights belongs to a conventional VLM, which provides strong semantic and visual understanding of the image and language inputs, while the second set of transformer weights is a smaller model called the Action Expert (AE). The action expert is essentially a subset of the model’s weights that is responsible for processing the system’s proprioceptive states and generating action chunks. Chen et al. proposed a flow matching algorithm as an optimized denoising procedure to be used for generation; this algorithm reduces the numbe…
- **State ownership:** 需要显式绑定 sensor/action/trajectory state；canonical owner 是 `MULTIMODAL-EMBODIED-VLA`，而不是论文应用领域本身。
- **Control / data flow:** 数据由工作负载进入机制实现，policy plus safety controller 决定是否执行、路由、提交或回退；输出必须携带与输入同一版本域的证据。
- **Implementation surface:** 全文 locator=`full-text paragraph 3; papers/2026/08/_sources/arxiv-owner-replay-20260903/20260803/exact-v1-text/2607.29569v1.txt`；公开实现、硬件或训练配置只按正文披露解释，未披露字段不补写。
- **Evaluation contract:** VLAs, despite their capabilities in generating trajectories for complex and abstract tasks such as tabletop operation, pick and place, cleaning, and laundry folding, are not yet fully integrated with safety-critical control. In this work, we develop a method that seamlessly bridges the gap between VLA policies and classical control safety guarantees, so that the resulting agent benefits simultaneously from the complex task planning and control capabilities of VLAs and the safety guarantees of CBFs. The main contributions of this work are summarized as follows: 该结果只绑定论文声明的数据、模型、硬件、精度、长度、batch/concurrency 与 evaluator；缺失字段均为 `Not Disclosed`。
- **Proves / does not prove:** 证据支持该受限 workload 中机制可行或暴露既有评价缺口；不证明跨模型、跨硬件、跨领域或生产 SLO 的普遍优势。
- **Trade-off / failure mode:** 新增状态、控制器和观测提高可验证性，但引入版本错配、额外延迟/内存/通信、错误路由及 evaluator bias。全文边界：Have a free development cycle? Help support accessibility at arXiv! Our collaborators at LaTeXML maintain a , and welcome .
- **Coexistence / evolution:** 旧方案在低风险、短状态或同构部署中仍成立；新机制只在约束变化使错误代价或状态漂移不可忽略时接手。
- **Books route:** 对照 `MULTIMODAL-EMBODIED-VLA` 及相邻章节；先进入按日期排序的 writeback queue，根任务合并同 owner 后决定最终写回。
<!-- review:SF-2026-ARXIV-2607-29569:end -->

<!-- review:SF-2026-ARXIV-2607-29575:start -->
### SLIM: Saturation-Aware Lightweight Performance Modeling for LLM Serving

- **Status / Evidence:** Experimental；exact-v1 HTML 已读取并保存校验和；Score V2=`8`。
- **Problem / old solution:** 既有路径通常把 shared inference capacity 隐含在模型调用或离线平均指标中；在较小规模、单一模型或无跨请求状态时成本较低，但难以回答谁拥有失败恢复与版本一致性。
- **Changed constraint:** 论文面对的约束由摘要和全文共同限定为：Large language model (LLM) serving commonly increases batch size to improve throughput, but performance eventually reaches a deployment-dependent plateau beyond which larger batches provide marginal gains while increasing latency and GPU memory consumption. Previous studies have attributed this behavior to HBM/DRAM bandwidth limitations, but the underlying causes have primarily been supported by conceptual arguments or high-l…
- **Mechanism:** exact-v1 的方法段写明：A key challenge in online LLM serving is understanding how this heterogeneity translates into accelerator-level performance. Among the factors affecting serving efficiency, the incoming request rate is particularly important because it determines the degree of batching that can be exploited during inference. Increasing batch size generally improves throughput by exposing greater request-level parallelism, albeit at the cost of higher request latency. However, throughput eventually reaches a saturation point beyond which additional parallelism provides only marginal performance gains, while latency continues to increase. At the same time, GPU memory consumption grows because additional requests require larger a…
- **State ownership:** 需要显式绑定 request/model/adaptation residency；canonical owner 是 `INFER-SCHEDULING`，而不是论文应用领域本身。
- **Control / data flow:** 数据由工作负载进入机制实现，scheduler 决定是否执行、路由、提交或回退；输出必须携带与输入同一版本域的证据。
- **Implementation surface:** 全文 locator=`full-text paragraph 3; papers/2026/08/_sources/arxiv-owner-replay-20260903/20260803/exact-v1-text/2607.29575v1.txt`；公开实现、硬件或训练配置只按正文披露解释，未披露字段不补写。
- **Evaluation contract:** To support BCA, we further propose the (SLIM), a semi-analytical performance model for LLM serving. SLIM leverages the performance insights obtained from our characterization study to estimate throughput and latency across the heterogeneous operating conditions typical of service providers. The model combines interpretable analytical formulations of the computation and memory traffic generated by Transformer operations with a small set of deployment-specific constants calibrated through a lightweight profiling phase. This lightweight calibration enables BCA to reduce profiling time by 43.85% compared to exhaustive profiling. We compare SLIM against two state-of-the-art performance models, LLMVisor and the mode… 该结果只绑定论文声明的数据、模型、硬件、精度、长度、batch/concurrency 与 evaluator；缺失字段均为 `Not Disclosed`。
- **Proves / does not prove:** 证据支持该受限 workload 中机制可行或暴露既有评价缺口；不证明跨模型、跨硬件、跨领域或生产 SLO 的普遍优势。
- **Trade-off / failure mode:** 新增状态、控制器和观测提高可验证性，但引入版本错配、额外延迟/内存/通信、错误路由及 evaluator bias。全文边界：We further evaluate SLIM’s ability to generalize to larger unseen models and tensor-parallel deployments. Figure compares measured throughput and end-to-end latency with SLIM predictions for Qwen-32B and Qwen-72B, served on two and four H100 GPUs, respectively. The results show that SLIM captures the throughput-saturation trend as batch size increases, but overestimates the performance gap between the two models. Under tensor parallelism, Qwen-72B is sharded across four GPUs, resulting in a per-GPU parameter footprint of approximately 16.5 GB, close to the roughly 15 GB per GPU of Qwen-32B. Their measured throughput curves are therefore similar, suggesting that per-GPU workload dominates and that tensor-parall…
- **Coexistence / evolution:** 旧方案在低风险、短状态或同构部署中仍成立；新机制只在约束变化使错误代价或状态漂移不可忽略时接手。
- **Books route:** 对照 `INFER-SCHEDULING` 及相邻章节；先进入按日期排序的 writeback queue，根任务合并同 owner 后决定最终写回。
<!-- review:SF-2026-ARXIV-2607-29575:end -->

<!-- review:SF-2026-ARXIV-2607-29591:start -->
### ResKV: Reconstructing Omitted Attention Contributions for Fixed-Budget KV Cache Compression

- **Status / Evidence:** Experimental；exact-v1 HTML 已读取并保存校验和；Score V2=`9`。
- **Problem / old solution:** 既有路径通常把 decode-state compression or translation 隐含在模型调用或离线平均指标中；在较小规模、单一模型或无跨请求状态时成本较低，但难以回答谁拥有失败恢复与版本一致性。
- **Changed constraint:** 论文面对的约束由摘要和全文共同限定为：KV cache compression is essential for efficient long-context inference. Existing eviction methods permanently discard unselected tokens and consequently remove their aggregate contribution to attention.
- **Mechanism:** exact-v1 的方法段写明：Table compares SnapKV, CaM, and ResKV under 10% retained KV in the query-agnostic setting. CaM can recover useful omitted information on some tasks, but its gains are less stable. ResKV gives stronger gains by storing omitted information in a separate residual cache while leaving the main cache unchanged.
- **State ownership:** 需要显式绑定 layer/head/token KV identity；canonical owner 是 `INFER-KV-CACHE`，而不是论文应用领域本身。
- **Control / data flow:** 数据由工作负载进入机制实现，cache manager 决定是否执行、路由、提交或回退；输出必须携带与输入同一版本域的证据。
- **Implementation surface:** 全文 locator=`Comparison with Merging Methods; papers/2026/08/_sources/arxiv-owner-replay-20260903/20260803/exact-v1-text/2607.29591v1.txt`；公开实现、硬件或训练配置只按正文披露解释，未披露字段不补写。
- **Evaluation contract:** We evaluate ResKV on two long-context benchmarks: LongBench and RULER . LongBench covers 16 real-world long-context understanding tasks, including single-document QA, multi-document QA, summarization, few-shot learning, synthetic retrieval, and code completion. RULER provides controlled long-context tests for retrieval and aggregation; we report results at both 4K and 32K context lengths over its 13 tasks. We evaluate ResKV on two instruction-tuned backbones, LLaMA-3.1-8B-Instruct and Qwen-2.5-7B-Instruct , under both query-aware and query-agnostic cache construction at compression ratios . ResKV uses the same total KV-slot budget as the corresponding baseline, split between the main and residual caches. For a… 该结果只绑定论文声明的数据、模型、硬件、精度、长度、batch/concurrency 与 evaluator；缺失字段均为 `Not Disclosed`。
- **Proves / does not prove:** 证据支持该受限 workload 中机制可行或暴露既有评价缺口；不证明跨模型、跨硬件、跨领域或生产 SLO 的普遍优势。
- **Trade-off / failure mode:** 新增状态、控制器和观测提高可验证性，但引入版本错配、额外延迟/内存/通信、错误路由及 evaluator bias。全文边界：We presented ResKV, a fixed-budget KV cache representation that preserves selected tokens exactly in a main cache while reconstructing the aggregate attention contribution of omitted tokens with compact residual entries. Its shared-softmax residual decode places main-cache tokens and residual entries under the same normalization, restoring residual numerator and denominator mass while keeping omitted information separate from exact main-cache entries. ResKV further controls residual usage with a construction-time validation proxy and a decode-time dynamic gate. Comprehensive evaluations on LongBench and RULER, spanning multiple backbones, cache budgets, compression baselines, and both query-aware and query-agn…
- **Coexistence / evolution:** 旧方案在低风险、短状态或同构部署中仍成立；新机制只在约束变化使错误代价或状态漂移不可忽略时接手。
- **Books route:** 对照 `INFER-KV-CACHE` 及相邻章节；先进入按日期排序的 writeback queue，根任务合并同 owner 后决定最终写回。
<!-- review:SF-2026-ARXIV-2607-29591:end -->

<!-- review:SF-2026-ARXIV-2607-29596:start -->
### FibVLA: An Efficient Temporal Vision-Language-Action Model with Fibonacci Sampling

- **Status / Evidence:** Experimental；exact-v1 HTML 已读取并保存校验和；Score V2=`6`。
- **Problem / old solution:** 既有路径通常把 closed-loop physical action 隐含在模型调用或离线平均指标中；在较小规模、单一模型或无跨请求状态时成本较低，但难以回答谁拥有失败恢复与版本一致性。
- **Changed constraint:** 论文面对的约束由摘要和全文共同限定为：Vision-language-action models (VLAs), which leverage the cognition of multimodal information to infer physical-world actions, provide a generalized solution for embodied AI applications. Conventional VLAs usually concentrate on current digital cognition.
- **Mechanism:** exact-v1 的方法段写明：To demonstrate the non-uniform information density inherent within embodied tasks, we investigate the latent characteristics of robotic manipulation data. As shown in Figure , our empirical analysis reveals that representations derived from high and low sampling frequencies form distinct clusters within the feature space. This phenomenon suggests that high-frequency frames are primarily associated with fine-grained motion control, such as changes in proprioceptive states, whereas low-frequency frames correspond to the understanding of task context, such as the progression of subtasks. Based on the above observation, we argue that by integrating information from gradual-frequency sampling, the VLA model can enh…
- **State ownership:** 需要显式绑定 sensor/action/trajectory state；canonical owner 是 `MULTIMODAL-EMBODIED-VLA`，而不是论文应用领域本身。
- **Control / data flow:** 数据由工作负载进入机制实现，policy plus safety controller 决定是否执行、路由、提交或回退；输出必须携带与输入同一版本域的证据。
- **Implementation surface:** 全文 locator=`full-text paragraph 3; papers/2026/08/_sources/arxiv-owner-replay-20260903/20260803/exact-v1-text/2607.29596v1.txt`；公开实现、硬件或训练配置只按正文披露解释，未披露字段不补写。
- **Evaluation contract:** We have conducted a comprehensive series of experiments to evaluate the effectiveness of , including: 1) Three simulated benchmark tests to measure its manipulation performance across diverse tasks. 2) Robotic deployment experiments in real-world environments. 3) Ablation studies to verify the contribution of each module. 4) Efficiency analysis to assess the model’s inference performance. We employ comprehensive benchmarks to evaluate task generalization and long-horizon manipulation capabilities. 1) Diverse simulation benchmarks, including and , alongside large-scale policy evaluations on the and via SimplerEnv . 2) , which is collected from a physical platform built on the Piper robotic arm, comprising over… 该结果只绑定论文声明的数据、模型、硬件、精度、长度、batch/concurrency 与 evaluator；缺失字段均为 `Not Disclosed`。
- **Proves / does not prove:** 证据支持该受限 workload 中机制可行或暴露既有评价缺口；不证明跨模型、跨硬件、跨领域或生产 SLO 的普遍优势。
- **Trade-off / failure mode:** 新增状态、控制器和观测提高可验证性，但引入版本错配、额外延迟/内存/通信、错误路由及 evaluator bias。全文边界：In this paper, we propose , an efficient temporal VLA framework designed to bridge the gap between temporal perception and real-time inference. We design a novel gradual-frequency sampling strategy based on Fibonacci sampling, which allows the model to directly reuse feature caches from the previous timestep during inference without incurring additional temporal encoding overhead, thereby capturing temporal context information for embodied tasks. Experimental results on three benchmarks and the real-world dataset show that significantly improves performance in long-horizon tasks and demonstrates real-time robustness in the real world. In future work, we plan to leverage the Fibonacci recursive principle to exp…
- **Coexistence / evolution:** 旧方案在低风险、短状态或同构部署中仍成立；新机制只在约束变化使错误代价或状态漂移不可忽略时接手。
- **Books route:** 对照 `MULTIMODAL-EMBODIED-VLA` 及相邻章节；先进入按日期排序的 writeback queue，根任务合并同 owner 后决定最终写回。
<!-- review:SF-2026-ARXIV-2607-29596:end -->

<!-- review:SF-2026-ARXIV-2607-29600:start -->
### HAM-VLN: Harnessing Hierarchical Agentic Memory for Zero-Shot Vision-and-Language Navigation

- **Status / Evidence:** Experimental；exact-v1 HTML 已读取并保存校验和；Score V2=`7`。
- **Problem / old solution:** 既有路径通常把 persistent or derived memory 隐含在模型调用或离线平均指标中；在较小规模、单一模型或无跨请求状态时成本较低，但难以回答谁拥有失败恢复与版本一致性。
- **Changed constraint:** 论文面对的约束由摘要和全文共同限定为：Vision-and-language navigation (VLN) enables robots to follow instructions in previously unseen environments. Recently, a training-free paradigm has emerged: the robot queries a multimodal LLM to understand its observations and plan the next action.
- **Mechanism:** exact-v1 的方法段写明：HAM-VLN equips a zero-shot VLN agent with decision-coupled memory that preserves task-relevant state over long trajectories. Within its dual-process architecture, a world graph records agent-authored state and supports subgoal-conditioned retrieval and grounded backtracking, turning failed exploration into reusable evidence. Figure illustrates how these components interact throughout a navigation episode.
- **State ownership:** 需要显式绑定 memory provenance, version and read/write boundary；canonical owner 是 `AGENT-MEMORY`，而不是论文应用领域本身。
- **Control / data flow:** 数据由工作负载进入机制实现，agent memory manager 决定是否执行、路由、提交或回退；输出必须携带与输入同一版本域的证据。
- **Implementation surface:** 全文 locator=`Method; papers/2026/08/_sources/arxiv-owner-replay-20260903/20260803/exact-v1-text/2607.29600v1.txt`；公开实现、硬件或训练配置只按正文披露解释，未披露字段不补写。
- **Evaluation contract:** We first describe the evaluation protocol (Section ) and compare HAM-VLN against published trained and zero-shot methods on R2R-CE, RxR-CE, and HM3D-v2 ObjectNav (Section ). We then examine inference cost and raw-history window sensitivity (Section ), ablate the memory components (Section ), and analyze backtracking through a real episode trace (Section ). 该结果只绑定论文声明的数据、模型、硬件、精度、长度、batch/concurrency 与 evaluator；缺失字段均为 `Not Disclosed`。
- **Proves / does not prove:** 证据支持该受限 workload 中机制可行或暴露既有评价缺口；不证明跨模型、跨硬件、跨领域或生产 SLO 的普遍优势。
- **Trade-off / failure mode:** 新增状态、控制器和观测提高可验证性，但引入版本错配、额外延迟/内存/通信、错误路由及 evaluator bias。全文边界：We introduce HAM-VLN, a framework that harnesses hierarchical agentic memory for zero-shot vision-and-language navigation. HAM-VLN represents navigation history in a depth-grounded world graph and uses working, episodic, semantic, and reflection memory views to retain recent observations, retrieve spatial and semantic information, and reuse failure evidence. Without task-specific training, HAM-VLN outperforms prior zero-shot methods and surpasses the full raw-history variant in navigation performance while requiring fewer inference-time tokens. Grounding agentic memory in a world graph allows HAM-VLN to reuse episode-specific evidence across long trajectories without continually expanding raw visual history.
- **Coexistence / evolution:** 旧方案在低风险、短状态或同构部署中仍成立；新机制只在约束变化使错误代价或状态漂移不可忽略时接手。
- **Books route:** 对照 `AGENT-MEMORY` 及相邻章节；先进入按日期排序的 writeback queue，根任务合并同 owner 后决定最终写回。
<!-- review:SF-2026-ARXIV-2607-29600:end -->

<!-- review:SF-2026-ARXIV-2607-29601:start -->
### The Parts Are Greater Than the Sum: Automated Task Sequencing for Efficient Training of Multi-Policy LLMs

- **Status / Evidence:** Experimental；exact-v1 HTML 已读取并保存校验和；Score V2=`6`。
- **Problem / old solution:** 既有路径通常把 training evidence construction 隐含在模型调用或离线平均指标中；在较小规模、单一模型或无跨请求状态时成本较低，但难以回答谁拥有失败恢复与版本一致性。
- **Changed constraint:** 论文面对的约束由摘要和全文共同限定为：Parameter-Efficient Fine-Tuning (PEFT) commonly adapts large language models using a single shared Low-Rank Adapter (LoRA). This shared optimization space often suffers from interference when adapting heterogeneous task sequences, leading to poor transfer and catastrophic forgetting.
- **Mechanism:** exact-v1 的方法段写明：O-LoRA is included as a parameter-isolation multi-adapter PEFT baseline, assigning one independent LoRA subspace to each individual task, whereas our framework automatically groups optimization-compatible tasks into shared policy-specific adaptation spaces. This makes O-LoRA a particularly appropriate baseline for isolating the effect of different optimization-path organization strategies. To ensure a fair comparison under the same total low-rank budget, O-LoRA allocates a rank-16 task-specific block to each of the eight tasks, resulting in a total rank of 128, while our framework uses two rank-64 policy-specific adapters, also resulting in a total rank of 128. Under this capacity-matched setting, O-LoRA achie…
- **State ownership:** 需要显式绑定 sample lineage and acceptance state；canonical owner 是 `TRAIN-DATA`，而不是论文应用领域本身。
- **Control / data flow:** 数据由工作负载进入机制实现，data pipeline 决定是否执行、路由、提交或回退；输出必须携带与输入同一版本域的证据。
- **Implementation surface:** 全文 locator=`Comparison with Baseline Methods; papers/2026/08/_sources/arxiv-owner-replay-20260903/20260803/exact-v1-text/2607.29601v1.txt`；公开实现、硬件或训练配置只按正文披露解释，未披露字段不补写。
- **Evaluation contract:** We evaluate the proposed method on TRACE, a continual-learning benchmark for large language models due to the wide range of different tasks for fine-tuning. TRACE contains eight heterogeneous tasks: C-STANCE, FOMC, MeetingBank, Py150, ScienceQA, NumGLUE-cm, NumGLUE-ds, and 20Minuten. While TRACE adopts LoRA, we use QLoRA through all experiments for its improved memory efficiency. Experiments are conducted on the same two 7B-scale aligned chat models, namely LLaMA-2-7B-Chat and Vicuna-7B-V1.5. Although Vicuna is built upon LLaMA-2, it is instruction-tuned differently, providing an additional backbone to evaluate the robustness of our work. For each backbone, the main multi-policy setting contains two independen… 该结果只绑定论文声明的数据、模型、硬件、精度、长度、batch/concurrency 与 evaluator；缺失字段均为 `Not Disclosed`。
- **Proves / does not prove:** 证据支持该受限 workload 中机制可行或暴露既有评价缺口；不证明跨模型、跨硬件、跨领域或生产 SLO 的普遍优势。
- **Trade-off / failure mode:** 新增状态、控制器和观测提高可验证性，但引入版本错配、额外延迟/内存/通信、错误路由及 evaluator bias。全文边界：In this paper, we proposed an optimization-path organization framework for parameter-efficient fine-tuning of large language models, implemented using a multi-policy PEFT architecture. Instead of forcing heterogeneous tasks to share a single low-rank adaptation space, our framework automatically organizes multiple optimization-compatible adaptation paths through task grouping and task sequencing. The approach separates incompatible tasks into independent adaptation spaces, reducing interference while preserving positive transfer among compatible tasks. This provides a new design perspective for parameter-efficient fine-tuning over heterogeneous task sequences, where optimization-path organization can be more e…
- **Coexistence / evolution:** 旧方案在低风险、短状态或同构部署中仍成立；新机制只在约束变化使错误代价或状态漂移不可忽略时接手。
- **Books route:** 对照 `TRAIN-DATA` 及相邻章节；先进入按日期排序的 writeback queue，根任务合并同 owner 后决定最终写回。
<!-- review:SF-2026-ARXIV-2607-29601:end -->

<!-- review:SF-2026-ARXIV-2607-29613:start -->
### WCM: A World Critic Model for Vision-Language-Action Reinforcement Learning

- **Status / Evidence:** Experimental；exact-v1 HTML 已读取并保存校验和；Score V2=`6`。
- **Problem / old solution:** 既有路径通常把 closed-loop physical action 隐含在模型调用或离线平均指标中；在较小规模、单一模型或无跨请求状态时成本较低，但难以回答谁拥有失败恢复与版本一致性。
- **Changed constraint:** 论文面对的约束由摘要和全文共同限定为：Reinforcement learning (RL) post-training of Vision-Language-Action (VLA) models has shown strong promise for robotic manipulation. Among RL methods, critic-based approaches rely on a value estimator that predominantly operates on single-frame observations or single-frame VLM backbone latents, which is a fundamental mismatch with the partially observable nature of robot control.
- **Mechanism:** exact-v1 的方法段写明：Our starting point is that robotic manipulation is inherently a partially observable Markov decision process (POMDP). A single frame may reveal object appearance and scene layout, but it often misses dynamic information that is critical for value estimation, such as motion, contact progress, and possible future evolution, etc. Classical POMDP theory shows that optimal decision-making depends not on the instantaneous observation alone, but on a sufficient statistic of history and a predictive representation of state . Therefore, a critic for VLA-RL should reason over observation history rather than a single frame alone, yet existing critics still predominantly estimate values from single-frame observations or V…
- **State ownership:** 需要显式绑定 sensor/action/trajectory state；canonical owner 是 `MULTIMODAL-EMBODIED-VLA`，而不是论文应用领域本身。
- **Control / data flow:** 数据由工作负载进入机制实现，policy plus safety controller 决定是否执行、路由、提交或回退；输出必须携带与输入同一版本域的证据。
- **Implementation surface:** 全文 locator=`full-text paragraph 3; papers/2026/08/_sources/arxiv-owner-replay-20260903/20260803/exact-v1-text/2607.29613v1.txt`；公开实现、硬件或训练配置只按正文披露解释，未披露字段不补写。
- **Evaluation contract:** We carefully designed our experiments and arrived at the following conclusions. (1) WCM consistently improves performance across simulation manipulation benchmarks. (2) WCM exhibits stronger generalization to OOD settings compared with existing methods. (3) WCM performs effectively in real-world RL training. (4) The world prediction objective plays a positive role in leveraging historical information. (5) Longer state history provides limited benefits beyond a certain optimal length rather than universal improvement in our tasks. 该结果只绑定论文声明的数据、模型、硬件、精度、长度、batch/concurrency 与 evaluator；缺失字段均为 `Not Disclosed`。
- **Proves / does not prove:** 证据支持该受限 workload 中机制可行或暴露既有评价缺口；不证明跨模型、跨硬件、跨领域或生产 SLO 的普遍优势。
- **Trade-off / failure mode:** 新增状态、控制器和观测提高可验证性，但引入版本错配、额外延迟/内存/通信、错误路由及 evaluator bias。全文边界：In this work, we identified a fundamental limitation of existing critic-based VLA-RL methods: value estimation from single-frame observations or weakly supervised history fails to capture the temporal structure required for state reconstruction under partial observability. To address this, we proposed the World Critic Model (WCM), a unified architecture that jointly learns latent state prediction and value estimation. Extensive experiments on 149 tasks across four simulation benchmarks demonstrate that WCM consistently achieves state-of-the-art performance in both in-distribution and out-of-distribution settings, with particularly strong generalization gains. We further validate WCM on seven real-world manipul…
- **Coexistence / evolution:** 旧方案在低风险、短状态或同构部署中仍成立；新机制只在约束变化使错误代价或状态漂移不可忽略时接手。
- **Books route:** 对照 `MULTIMODAL-EMBODIED-VLA` 及相邻章节；先进入按日期排序的 writeback queue，根任务合并同 owner 后决定最终写回。
<!-- review:SF-2026-ARXIV-2607-29613:end -->

<!-- review:SF-2026-ARXIV-2607-29626:start -->
### AgentHPOBench: A Benchmark For Evaluating LLM Agents as Sequential Hyperparameter Optimizers

- **Status / Evidence:** Experimental；exact-v1 HTML 已读取并保存校验和；Score V2=`7`。
- **Problem / old solution:** 既有路径通常把 evaluation evidence and release decision 隐含在模型调用或离线平均指标中；在较小规模、单一模型或无跨请求状态时成本较低，但难以回答谁拥有失败恢复与版本一致性。
- **Changed constraint:** 论文面对的约束由摘要和全文共同限定为：As LLMs evolve from code completion systems into autonomous scientific agents, evaluating their ability to conduct experiments has become increasingly important. Existing benchmarks typically focus on static code generation, paper replication, or final answer correctness, but do not directly assess whether agents can interpret experimental evidence and use it to guide subsequent hyperparameter decisions.
- **Mechanism:** exact-v1 的方法段写明：Sequential Optimization Trajectories.Figure 3 reports the MBNS obtained after the reference baseline and
- **State ownership:** 需要显式绑定 evaluator configuration, dataset slice and result provenance；canonical owner 是 `PLATFORM-EVALUATION-SYSTEM`，而不是论文应用领域本身。
- **Control / data flow:** 数据由工作负载进入机制实现，evaluation controller 决定是否执行、路由、提交或回退；输出必须携带与输入同一版本域的证据。
- **Implementation surface:** 全文 locator=`full-text paragraph 3; papers/2026/08/_sources/arxiv-owner-replay-20260903/20260803/exact-v1-text/2607.29626v1.txt`；公开实现、硬件或训练配置只按正文披露解释，未披露字段不补写。
- **Evaluation contract:** [41] Benjamin Warner, Antoine Chaffin, Benjamin Clavié, Orion Weller, Oskar Hallström, Said Taghadouini, Alexis 该结果只绑定论文声明的数据、模型、硬件、精度、长度、batch/concurrency 与 evaluator；缺失字段均为 `Not Disclosed`。
- **Proves / does not prove:** 证据支持该受限 workload 中机制可行或暴露既有评价缺口；不证明跨模型、跨硬件、跨领域或生产 SLO 的普遍优势。
- **Trade-off / failure mode:** 新增状态、控制器和观测提高可验证性，但引入版本错配、额外延迟/内存/通信、错误路由及 evaluator bias。全文边界：Execution environment and reproducibility resources.The controlled experiments run on Linux development
- **Coexistence / evolution:** 旧方案在低风险、短状态或同构部署中仍成立；新机制只在约束变化使错误代价或状态漂移不可忽略时接手。
- **Books route:** 对照 `PLATFORM-EVALUATION-SYSTEM` 及相邻章节；先进入按日期排序的 writeback queue，根任务合并同 owner 后决定最终写回。
<!-- review:SF-2026-ARXIV-2607-29626:end -->

<!-- review:SF-2026-ARXIV-2607-29638:start -->
### HierDoc: Hierarchical Page-to-Region Evidence Routing for Long-Document Visual Question Answering

- **Status / Evidence:** Experimental；exact-v1 HTML 已读取并保存校验和；Score V2=`6`。
- **Problem / old solution:** 既有路径通常把 retrieval evidence routing 隐含在模型调用或离线平均指标中；在较小规模、单一模型或无跨请求状态时成本较低，但难以回答谁拥有失败恢复与版本一致性。
- **Changed constraint:** 论文面对的约束由摘要和全文共同限定为：Multi-page document visual question answering requires locating sparse evidence at both the page and region levels. Existing approaches typically emphasize one level over the other: page-centric methods focus on page acquisition, with region operations serving mainly as navigation aids, whereas region-centric methods assume that the relevant pages have already been supplied.
- **Mechanism:** exact-v1 的方法段写明：We compare against the direct multimodal backbones InternVL3, mPLUG-DocOwl2, and Qwen2.5-VL . The document-specific and retrieval-based baselines comprise M3DocRAG, MoLoRAG+, CogDoc, Doc-, and MDocAgent .
- **State ownership:** 需要显式绑定 document/chunk/provenance identity；canonical owner 是 `AGENT-RAG`，而不是论文应用领域本身。
- **Control / data flow:** 数据由工作负载进入机制实现，retrieval pipeline 决定是否执行、路由、提交或回退；输出必须携带与输入同一版本域的证据。
- **Implementation surface:** 全文 locator=`Compared Methods; papers/2026/08/_sources/arxiv-owner-replay-20260903/20260803/exact-v1-text/2607.29638v1.txt`；公开实现、硬件或训练配置只按正文披露解释，未披露字段不补写。
- **Evaluation contract:** To assess the page selector independently of downstream answering, we conduct a dedicated page-retrieval evaluation. This protocol enables direct comparison with the page-selection components of prior methods and characterizes the quality of the evidence pool passed to later stages. Such evaluation is critical because all subsequent region-selection experiments in HierDoc operate exclusively on the selected pages; page-level evidence omitted at this stage cannot be recovered downstream. Table reports page-level evidence precision, recall, F1, and the average number of selected pages. The Doc- action rows describe the pages returned by two different tools rather than a single final page set, so they serve as re… 该结果只绑定论文声明的数据、模型、硬件、精度、长度、batch/concurrency 与 evaluator；缺失字段均为 `Not Disclosed`。
- **Proves / does not prove:** 证据支持该受限 workload 中机制可行或暴露既有评价缺口；不证明跨模型、跨硬件、跨领域或生产 SLO 的普遍优势。
- **Trade-off / failure mode:** 新增状态、控制器和观测提高可验证性，但引入版本错配、额外延迟/内存/通信、错误路由及 evaluator bias。全文边界：We introduced HierDoc, a hierarchical evidence-routing framework that formulates page and semantic-region acquisition as successive, answer-agnostic structured-set decisions. HierDoc independently optimizes its page and region policies with stage-specific GRPO rewards, uses parser-native semantic regions as a discrete action space, and combines selected full pages, region crops, and textual metadata for grounded answering. Across five multi-page and long-document VQA benchmarks, HierDoc achieves the best reported performance among open-weight methods on four benchmarks and competitive performance on the remaining one, with consistent improvements across different answer backbones. The retrieval evaluation and…
- **Coexistence / evolution:** 旧方案在低风险、短状态或同构部署中仍成立；新机制只在约束变化使错误代价或状态漂移不可忽略时接手。
- **Books route:** 对照 `AGENT-RAG` 及相邻章节；先进入按日期排序的 writeback queue，根任务合并同 owner 后决定最终写回。
<!-- review:SF-2026-ARXIV-2607-29638:end -->

<!-- review:SF-2026-ARXIV-2607-29658:start -->
### Reusing Past Repairs Through Hierarchical Trajectory Abstraction for Coding Agents

- **Status / Evidence:** Experimental；exact-v1 HTML 已读取并保存校验和；Score V2=`6`。
- **Problem / old solution:** 既有路径通常把 durable multi-step execution 隐含在模型调用或离线平均指标中；在较小规模、单一模型或无跨请求状态时成本较低，但难以回答谁拥有失败恢复与版本一致性。
- **Changed constraint:** 论文面对的约束由摘要和全文共同限定为：Although LLM-driven repair agents can tackle complex, repository-level issues, they treat every issue independently and discard the procedural knowledge accumulated from previous repairs. We introduce STAIR, a framework that converts historical repair trajectories into hierarchical, reusable plans that can be adapted to steer future repairs.
- **Mechanism:** exact-v1 的方法段写明：Recent advances in large language models (LLMs) have led to a new generation of autonomous repair agents that can resolve real-world repository-level issues . These agents interact with codebases through tool calls, execute tests, and iteratively refine patches. However, most existing repair agents treat each issue as an independent task. After each run, they discard the procedural knowledge embedded in past repair trajectories, such as effective localization strategies and common failure modes. While some studies have begun to explore knowledge reuse for issue resolution, they face three key limitations.
- **State ownership:** 需要显式绑定 task, evidence and checkpoint state；canonical owner 是 `AGENT-WORKFLOW`，而不是论文应用领域本身。
- **Control / data flow:** 数据由工作负载进入机制实现，workflow engine 决定是否执行、路由、提交或回退；输出必须携带与输入同一版本域的证据。
- **Implementation surface:** 全文 locator=`full-text paragraph 3; papers/2026/08/_sources/arxiv-owner-replay-20260903/20260803/exact-v1-text/2607.29658v1.txt`；公开实现、硬件或训练配置只按正文披露解释，未披露字段不补写。
- **Evaluation contract:** We evaluate on SWE-bench Verified , a benchmark of 500 real-world GitHub issues with developer-written test suites. achieves a Pass@1 of 81.2% with MiniMax M2.5 and 79.2% with GPT-5. We also compare with agents that reuse historical knowledge, including SWE-Exp , Lingxi , and ExpeRepair , and show that consistently outperforms them. 该结果只绑定论文声明的数据、模型、硬件、精度、长度、batch/concurrency 与 evaluator；缺失字段均为 `Not Disclosed`。
- **Proves / does not prove:** 证据支持该受限 workload 中机制可行或暴露既有评价缺口；不证明跨模型、跨硬件、跨领域或生产 SLO 的普遍优势。
- **Trade-off / failure mode:** 新增状态、控制器和观测提高可验证性，但引入版本错配、额外延迟/内存/通信、错误路由及 evaluator bias。全文边界：Have a free development cycle? Help support accessibility at arXiv! Our collaborators at LaTeXML maintain a , and welcome .
- **Coexistence / evolution:** 旧方案在低风险、短状态或同构部署中仍成立；新机制只在约束变化使错误代价或状态漂移不可忽略时接手。
- **Books route:** 对照 `AGENT-WORKFLOW` 及相邻章节；先进入按日期排序的 writeback queue，根任务合并同 owner 后决定最终写回。
<!-- review:SF-2026-ARXIV-2607-29658:end -->

<!-- review:SF-2026-ARXIV-2607-29674:start -->
### Sign compression for Muon: SignMuon, MuonSign, and the Limits of Error Feedback

- **Status / Evidence:** Experimental；exact-v1 HTML 已读取并保存校验和；Score V2=`6`。
- **Problem / old solution:** 既有路径通常把 distributed update execution 隐含在模型调用或离线平均指标中；在较小规模、单一模型或无跨请求状态时成本较低，但难以回答谁拥有失败恢复与版本一致性。
- **Changed constraint:** 论文面对的约束由摘要和全文共同限定为：SignMuon compresses the Muon update to one bit per parameter by taking its elementwise sign, providing the most direct way to run a matrix-aware optimizer under an extremely low communication budget. It outperforms SignSGD in practice, yet it can ascend even on a linear function.
- **Mechanism:** exact-v1 的方法段写明：We study the natural ways to combine sign compression with the Muon LMO at one bit per parameter: , which signs the LMO, ; , which signs , ; and , which signs on sides and, like SignMuon, emits a -valued step, so that uplink and downlink alike cost one bit. All three build Muon’s matrix-aware geometry into the step without preserving it intact, and they are not interchangeable: on federated CIFAR-10 () they span accuracy points, in the order after, before, both sides, and only sign-after matches full-precision Muon.
- **State ownership:** 需要显式绑定 optimizer/collective/compression state；canonical owner 是 `TRAIN-DISTRIBUTED-TRAINING`，而不是论文应用领域本身。
- **Control / data flow:** 数据由工作负载进入机制实现，training runtime 决定是否执行、路由、提交或回退；输出必须携带与输入同一版本域的证据。
- **Implementation surface:** 全文 locator=`full-text paragraph 3; papers/2026/08/_sources/arxiv-owner-replay-20260903/20260803/exact-v1-text/2607.29674v1.txt`；公开实现、硬件或训练配置只按正文披露解释，未披露字段不补写。
- **Evaluation contract:** On a deterministic convex quadratic () the first-order term of the descent lemma can be measured directly, through the alignment between the gradient and the direction actually taken. The direction descends when , and – provide instances on which ; on random instances this does not occur, all three placements keeping bounded away from zero at every step. The counterexamples describe a worst case rather than a typical one, which is what permits the network results below to run contrary to them. 该结果只绑定论文声明的数据、模型、硬件、精度、长度、batch/concurrency 与 evaluator；缺失字段均为 `Not Disclosed`。
- **Proves / does not prove:** 证据支持该受限 workload 中机制可行或暴露既有评价缺口；不证明跨模型、跨硬件、跨领域或生产 SLO 的普遍优势。
- **Trade-off / failure mode:** 新增状态、控制器和观测提高可验证性，但引入版本错配、额外延迟/内存/通信、错误路由及 evaluator bias。全文边界：A sign step and a spectral step are each an LMO, sound alone; composed, they are an LMO for no norm, and the descent property each factor guarantees is lost in the composition. On small explicit instances, at every step size and momentum, every placement of the sign around the oracle can turn the update into an ascent direction on a linear objective: SignMuon after the LMO, MuonUSign before it, and MuonSign on both sides. Where error feedback is applied then decides whether it repairs this. On the oracle’s it does not: the polar factor can move by a constant however small the step size, so one shared magnitude cannot track it, and for every some -smooth objective makes EF21-SignMuon diverge. On the it does: EF…
- **Coexistence / evolution:** 旧方案在低风险、短状态或同构部署中仍成立；新机制只在约束变化使错误代价或状态漂移不可忽略时接手。
- **Books route:** 对照 `TRAIN-DISTRIBUTED-TRAINING` 及相邻章节；先进入按日期排序的 writeback queue，根任务合并同 owner 后决定最终写回。
<!-- review:SF-2026-ARXIV-2607-29674:end -->

<!-- review:SF-2026-ARXIV-2607-29678:start -->
### TokTier: Exact Stateful CPU+GPU Tokenization for Agentic LLM Serving

- **Status / Evidence:** Experimental；exact-v1 HTML 已读取并保存校验和；Score V2=`8`。
- **Problem / old solution:** 既有路径通常把 request execution lifecycle 隐含在模型调用或离线平均指标中；在较小规模、单一模型或无跨请求状态时成本较低，但难以回答谁拥有失败恢复与版本一致性。
- **Changed constraint:** 论文面对的约束由摘要和全文共同限定为：LLM serving caches prompt KV state, yet most front ends still re-tokenize the full request on every call. Coding agents pay most: sessions repeatedly submit a long transcript after a small append, which can shift token boundaries near the end of the prior sequence.
- **Mechanism:** exact-v1 的方法段写明：is a tokenization service placed between the request router and the model engine. It accepts request text and a model identifier, then returns reference-equivalent token IDs. The service keeps token state for live sessions and selects an execution path from that state and the request size. Figure shows the data flow. Each tokenizer version is registered by content hash. Its entry carries the added-token rules, normalization configuration, pre-tokenization rules, vocabulary, merge table, and the family-specific checks used by the repair and GPU paths. A request is never interpreted through ambient process state, and a session created under one tokenizer version is never repaired under another.
- **State ownership:** 需要显式绑定 request/stream/session state；canonical owner 是 `INFER-REQUEST-LIFECYCLE`，而不是论文应用领域本身。
- **Control / data flow:** 数据由工作负载进入机制实现，serving engine 决定是否执行、路由、提交或回退；输出必须携带与输入同一版本域的证据。
- **Implementation surface:** 全文 locator=`System Design; papers/2026/08/_sources/arxiv-owner-replay-20260903/20260803/exact-v1-text/2607.29678v1.txt`；公开实现、硬件或训练配置只按正文披露解释，未披露字段不补写。
- **Evaluation contract:** We first place both execution paths against the measured baselines, then test them against frozen reference tokenizers. We measure incremental repair and GPU full tokenization separately, before evaluating burst tails, capacity, and time to first token with vLLM. The final experiments cover resource use and runtime verification. What limits the GPU path is discussed with the other limitations in §. Experiments run on a dual-socket AMD EPYC 9115 host (32 physical cores, SMT disabled) with four RTX PRO 6000 Blackwell GPUs of 96 GB each. CPU experiments are NUMA-pinned. One GPU serves vLLM 0.25 with prefix caching enabled and one serves unless stated otherwise. Tokenizer artifacts, datasets, and dependency versio… 该结果只绑定论文声明的数据、模型、硬件、精度、长度、batch/concurrency 与 evaluator；缺失字段均为 `Not Disclosed`。
- **Proves / does not prove:** 证据支持该受限 workload 中机制可行或暴露既有评价缺口；不证明跨模型、跨硬件、跨领域或生产 SLO 的普遍优势。
- **Trade-off / failure mode:** 新增状态、控制器和观测提高可验证性，但引入版本错配、额外延迟/内存/通信、错误路由及 evaluator bias。全文边界：We collect the system’s limitations here, from the physical floor of the GPU path to the boundary of what zero divergence establishes.
- **Coexistence / evolution:** 旧方案在低风险、短状态或同构部署中仍成立；新机制只在约束变化使错误代价或状态漂移不可忽略时接手。
- **Books route:** 对照 `INFER-REQUEST-LIFECYCLE` 及相邻章节；先进入按日期排序的 writeback queue，根任务合并同 owner 后决定最终写回。
<!-- review:SF-2026-ARXIV-2607-29678:end -->

## 4. Benchmark Contracts

本日报不产生可跨 workload 外推的 benchmark claim。每个数值只在对应 Source Review 的 exact-v1 evaluation locator、模型、数据、硬件、精度、长度、batch/concurrency、SLO 与 evaluator 披露范围内成立；未披露字段均是 `Not Disclosed`。

## 5. Deep Analysis Selection

<!-- validator:deep-analysis-selection-v1 -->
| Source Family ID | Eligibility | Decision | Analysis Unit ID | Subsumed By | Priority Rationale | Narrative Ref |
| --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2607-28631 | score_7_9 | not_selected | — | — | 已完成作者侧 exact-v1 Review；相对三个入选单元，其跨层影响或机制独立性较窄，不能把未入选误写成未审阅。 | analysis-decision:SF-2026-ARXIV-2607-28631 |
| SF-2026-ARXIV-2607-28633 | score_7_9 | not_selected | — | — | 已完成作者侧 exact-v1 Review；相对三个入选单元，其跨层影响或机制独立性较窄，不能把未入选误写成未审阅。 | analysis-decision:SF-2026-ARXIV-2607-28633 |
| SF-2026-ARXIV-2607-28636 | score_7_9 | not_selected | — | — | 已完成作者侧 exact-v1 Review；相对三个入选单元，其跨层影响或机制独立性较窄，不能把未入选误写成未审阅。 | analysis-decision:SF-2026-ARXIV-2607-28636 |
| SF-2026-ARXIV-2607-28638 | score_7_9 | not_selected | — | — | 已完成作者侧 exact-v1 Review；相对三个入选单元，其跨层影响或机制独立性较窄，不能把未入选误写成未审阅。 | analysis-decision:SF-2026-ARXIV-2607-28638 |
| SF-2026-ARXIV-2607-28658 | score_7_9 | not_selected | — | — | 已完成作者侧 exact-v1 Review；相对三个入选单元，其跨层影响或机制独立性较窄，不能把未入选误写成未审阅。 | analysis-decision:SF-2026-ARXIV-2607-28658 |
| SF-2026-ARXIV-2607-28666 | score_7_9 | not_selected | — | — | 已完成作者侧 exact-v1 Review；相对三个入选单元，其跨层影响或机制独立性较窄，不能把未入选误写成未审阅。 | analysis-decision:SF-2026-ARXIV-2607-28666 |
| SF-2026-ARXIV-2607-28678 | score_7_9 | not_selected | — | — | 已完成作者侧 exact-v1 Review；相对三个入选单元，其跨层影响或机制独立性较窄，不能把未入选误写成未审阅。 | analysis-decision:SF-2026-ARXIV-2607-28678 |
| SF-2026-ARXIV-2607-28684 | score_7_9 | not_selected | — | — | 已完成作者侧 exact-v1 Review；相对三个入选单元，其跨层影响或机制独立性较窄，不能把未入选误写成未审阅。 | analysis-decision:SF-2026-ARXIV-2607-28684 |
| SF-2026-ARXIV-2607-28685 | score_7_9 | not_selected | — | — | 已完成作者侧 exact-v1 Review；相对三个入选单元，其跨层影响或机制独立性较窄，不能把未入选误写成未审阅。 | analysis-decision:SF-2026-ARXIV-2607-28685 |
| SF-2026-ARXIV-2607-28692 | score_7_9 | not_selected | — | — | 已完成作者侧 exact-v1 Review；相对三个入选单元，其跨层影响或机制独立性较窄，不能把未入选误写成未审阅。 | analysis-decision:SF-2026-ARXIV-2607-28692 |
| SF-2026-ARXIV-2607-28699 | score_7_9; potential_books_delta | selected | DA-20260803-1 | — | 在 102-family frontier 中，该机制具有明确运行时状态、控制器和 failure/fallback 边界，并横跨模型机制与系统 owner。 | analysis:DA-20260803-1 |
| SF-2026-ARXIV-2607-28707 | score_7_9 | not_selected | — | — | 已完成作者侧 exact-v1 Review；相对三个入选单元，其跨层影响或机制独立性较窄，不能把未入选误写成未审阅。 | analysis-decision:SF-2026-ARXIV-2607-28707 |
| SF-2026-ARXIV-2607-28777 | score_7_9 | not_selected | — | — | 已完成作者侧 exact-v1 Review；相对三个入选单元，其跨层影响或机制独立性较窄，不能把未入选误写成未审阅。 | analysis-decision:SF-2026-ARXIV-2607-28777 |
| SF-2026-ARXIV-2607-28788 | score_7_9 | not_selected | — | — | 已完成作者侧 exact-v1 Review；相对三个入选单元，其跨层影响或机制独立性较窄，不能把未入选误写成未审阅。 | analysis-decision:SF-2026-ARXIV-2607-28788 |
| SF-2026-ARXIV-2607-28801 | score_7_9 | not_selected | — | — | 已完成作者侧 exact-v1 Review；相对三个入选单元，其跨层影响或机制独立性较窄，不能把未入选误写成未审阅。 | analysis-decision:SF-2026-ARXIV-2607-28801 |
| SF-2026-ARXIV-2607-28802 | score_7_9 | not_selected | — | — | 已完成作者侧 exact-v1 Review；相对三个入选单元，其跨层影响或机制独立性较窄，不能把未入选误写成未审阅。 | analysis-decision:SF-2026-ARXIV-2607-28802 |
| SF-2026-ARXIV-2607-28818 | score_7_9 | not_selected | — | — | 已完成作者侧 exact-v1 Review；相对三个入选单元，其跨层影响或机制独立性较窄，不能把未入选误写成未审阅。 | analysis-decision:SF-2026-ARXIV-2607-28818 |
| SF-2026-ARXIV-2607-28824 | score_7_9 | not_selected | — | — | 已完成作者侧 exact-v1 Review；相对三个入选单元，其跨层影响或机制独立性较窄，不能把未入选误写成未审阅。 | analysis-decision:SF-2026-ARXIV-2607-28824 |
| SF-2026-ARXIV-2607-28829 | score_7_9 | not_selected | — | — | 已完成作者侧 exact-v1 Review；相对三个入选单元，其跨层影响或机制独立性较窄，不能把未入选误写成未审阅。 | analysis-decision:SF-2026-ARXIV-2607-28829 |
| SF-2026-ARXIV-2607-28848 | score_7_9; potential_books_delta | selected | DA-20260803-2 | — | 在 102-family frontier 中，该机制具有明确运行时状态、控制器和 failure/fallback 边界，并横跨模型机制与系统 owner。 | analysis:DA-20260803-2 |
| SF-2026-ARXIV-2607-28871 | score_7_9 | not_selected | — | — | 已完成作者侧 exact-v1 Review；相对三个入选单元，其跨层影响或机制独立性较窄，不能把未入选误写成未审阅。 | analysis-decision:SF-2026-ARXIV-2607-28871 |
| SF-2026-ARXIV-2607-28884 | score_7_9 | not_selected | — | — | 已完成作者侧 exact-v1 Review；相对三个入选单元，其跨层影响或机制独立性较窄，不能把未入选误写成未审阅。 | analysis-decision:SF-2026-ARXIV-2607-28884 |
| SF-2026-ARXIV-2607-28896 | score_7_9 | not_selected | — | — | 已完成作者侧 exact-v1 Review；相对三个入选单元，其跨层影响或机制独立性较窄，不能把未入选误写成未审阅。 | analysis-decision:SF-2026-ARXIV-2607-28896 |
| SF-2026-ARXIV-2607-28940 | score_7_9 | not_selected | — | — | 已完成作者侧 exact-v1 Review；相对三个入选单元，其跨层影响或机制独立性较窄，不能把未入选误写成未审阅。 | analysis-decision:SF-2026-ARXIV-2607-28940 |
| SF-2026-ARXIV-2607-28966 | score_7_9 | not_selected | — | — | 已完成作者侧 exact-v1 Review；相对三个入选单元，其跨层影响或机制独立性较窄，不能把未入选误写成未审阅。 | analysis-decision:SF-2026-ARXIV-2607-28966 |
| SF-2026-ARXIV-2607-28979 | score_7_9 | not_selected | — | — | 已完成作者侧 exact-v1 Review；相对三个入选单元，其跨层影响或机制独立性较窄，不能把未入选误写成未审阅。 | analysis-decision:SF-2026-ARXIV-2607-28979 |
| SF-2026-ARXIV-2607-28993 | score_7_9 | not_selected | — | — | 已完成作者侧 exact-v1 Review；相对三个入选单元，其跨层影响或机制独立性较窄，不能把未入选误写成未审阅。 | analysis-decision:SF-2026-ARXIV-2607-28993 |
| SF-2026-ARXIV-2607-29032 | score_7_9 | not_selected | — | — | 已完成作者侧 exact-v1 Review；相对三个入选单元，其跨层影响或机制独立性较窄，不能把未入选误写成未审阅。 | analysis-decision:SF-2026-ARXIV-2607-29032 |
| SF-2026-ARXIV-2607-29053 | score_7_9 | not_selected | — | — | 已完成作者侧 exact-v1 Review；相对三个入选单元，其跨层影响或机制独立性较窄，不能把未入选误写成未审阅。 | analysis-decision:SF-2026-ARXIV-2607-29053 |
| SF-2026-ARXIV-2607-29069 | score_7_9 | not_selected | — | — | 已完成作者侧 exact-v1 Review；相对三个入选单元，其跨层影响或机制独立性较窄，不能把未入选误写成未审阅。 | analysis-decision:SF-2026-ARXIV-2607-29069 |
| SF-2026-ARXIV-2607-29076 | score_7_9 | not_selected | — | — | 已完成作者侧 exact-v1 Review；相对三个入选单元，其跨层影响或机制独立性较窄，不能把未入选误写成未审阅。 | analysis-decision:SF-2026-ARXIV-2607-29076 |
| SF-2026-ARXIV-2607-29104 | score_7_9 | not_selected | — | — | 已完成作者侧 exact-v1 Review；相对三个入选单元，其跨层影响或机制独立性较窄，不能把未入选误写成未审阅。 | analysis-decision:SF-2026-ARXIV-2607-29104 |
| SF-2026-ARXIV-2607-29125 | score_7_9 | not_selected | — | — | 已完成作者侧 exact-v1 Review；相对三个入选单元，其跨层影响或机制独立性较窄，不能把未入选误写成未审阅。 | analysis-decision:SF-2026-ARXIV-2607-29125 |
| SF-2026-ARXIV-2607-29167 | score_7_9 | not_selected | — | — | 已完成作者侧 exact-v1 Review；相对三个入选单元，其跨层影响或机制独立性较窄，不能把未入选误写成未审阅。 | analysis-decision:SF-2026-ARXIV-2607-29167 |
| SF-2026-ARXIV-2607-29175 | score_7_9 | not_selected | — | — | 已完成作者侧 exact-v1 Review；相对三个入选单元，其跨层影响或机制独立性较窄，不能把未入选误写成未审阅。 | analysis-decision:SF-2026-ARXIV-2607-29175 |
| SF-2026-ARXIV-2607-29190 | score_7_9 | not_selected | — | — | 已完成作者侧 exact-v1 Review；相对三个入选单元，其跨层影响或机制独立性较窄，不能把未入选误写成未审阅。 | analysis-decision:SF-2026-ARXIV-2607-29190 |
| SF-2026-ARXIV-2607-29199 | score_7_9 | not_selected | — | — | 已完成作者侧 exact-v1 Review；相对三个入选单元，其跨层影响或机制独立性较窄，不能把未入选误写成未审阅。 | analysis-decision:SF-2026-ARXIV-2607-29199 |
| SF-2026-ARXIV-2607-29218 | score_7_9 | not_selected | — | — | 已完成作者侧 exact-v1 Review；相对三个入选单元，其跨层影响或机制独立性较窄，不能把未入选误写成未审阅。 | analysis-decision:SF-2026-ARXIV-2607-29218 |
| SF-2026-ARXIV-2607-29221 | score_7_9 | not_selected | — | — | 已完成作者侧 exact-v1 Review；相对三个入选单元，其跨层影响或机制独立性较窄，不能把未入选误写成未审阅。 | analysis-decision:SF-2026-ARXIV-2607-29221 |
| SF-2026-ARXIV-2607-29235 | score_7_9 | not_selected | — | — | 已完成作者侧 exact-v1 Review；相对三个入选单元，其跨层影响或机制独立性较窄，不能把未入选误写成未审阅。 | analysis-decision:SF-2026-ARXIV-2607-29235 |
| SF-2026-ARXIV-2607-29252 | score_7_9 | not_selected | — | — | 已完成作者侧 exact-v1 Review；相对三个入选单元，其跨层影响或机制独立性较窄，不能把未入选误写成未审阅。 | analysis-decision:SF-2026-ARXIV-2607-29252 |
| SF-2026-ARXIV-2607-29254 | score_7_9 | not_selected | — | — | 已完成作者侧 exact-v1 Review；相对三个入选单元，其跨层影响或机制独立性较窄，不能把未入选误写成未审阅。 | analysis-decision:SF-2026-ARXIV-2607-29254 |
| SF-2026-ARXIV-2607-29302 | score_7_9 | not_selected | — | — | 已完成作者侧 exact-v1 Review；相对三个入选单元，其跨层影响或机制独立性较窄，不能把未入选误写成未审阅。 | analysis-decision:SF-2026-ARXIV-2607-29302 |
| SF-2026-ARXIV-2607-29320 | score_7_9 | not_selected | — | — | 已完成作者侧 exact-v1 Review；相对三个入选单元，其跨层影响或机制独立性较窄，不能把未入选误写成未审阅。 | analysis-decision:SF-2026-ARXIV-2607-29320 |
| SF-2026-ARXIV-2607-29377 | score_7_9 | not_selected | — | — | 已完成作者侧 exact-v1 Review；相对三个入选单元，其跨层影响或机制独立性较窄，不能把未入选误写成未审阅。 | analysis-decision:SF-2026-ARXIV-2607-29377 |
| SF-2026-ARXIV-2607-29393 | score_7_9 | not_selected | — | — | 已完成作者侧 exact-v1 Review；相对三个入选单元，其跨层影响或机制独立性较窄，不能把未入选误写成未审阅。 | analysis-decision:SF-2026-ARXIV-2607-29393 |
| SF-2026-ARXIV-2607-29398 | score_7_9 | not_selected | — | — | 已完成作者侧 exact-v1 Review；相对三个入选单元，其跨层影响或机制独立性较窄，不能把未入选误写成未审阅。 | analysis-decision:SF-2026-ARXIV-2607-29398 |
| SF-2026-ARXIV-2607-29405 | score_7_9 | not_selected | — | — | 已完成作者侧 exact-v1 Review；相对三个入选单元，其跨层影响或机制独立性较窄，不能把未入选误写成未审阅。 | analysis-decision:SF-2026-ARXIV-2607-29405 |
| SF-2026-ARXIV-2607-29431 | score_7_9 | not_selected | — | — | 已完成作者侧 exact-v1 Review；相对三个入选单元，其跨层影响或机制独立性较窄，不能把未入选误写成未审阅。 | analysis-decision:SF-2026-ARXIV-2607-29431 |
| SF-2026-ARXIV-2607-29440 | score_7_9 | not_selected | — | — | 已完成作者侧 exact-v1 Review；相对三个入选单元，其跨层影响或机制独立性较窄，不能把未入选误写成未审阅。 | analysis-decision:SF-2026-ARXIV-2607-29440 |
| SF-2026-ARXIV-2607-29465 | score_7_9 | not_selected | — | — | 已完成作者侧 exact-v1 Review；相对三个入选单元，其跨层影响或机制独立性较窄，不能把未入选误写成未审阅。 | analysis-decision:SF-2026-ARXIV-2607-29465 |
| SF-2026-ARXIV-2607-29516 | score_7_9 | not_selected | — | — | 已完成作者侧 exact-v1 Review；相对三个入选单元，其跨层影响或机制独立性较窄，不能把未入选误写成未审阅。 | analysis-decision:SF-2026-ARXIV-2607-29516 |
| SF-2026-ARXIV-2607-29549 | score_7_9 | not_selected | — | — | 已完成作者侧 exact-v1 Review；相对三个入选单元，其跨层影响或机制独立性较窄，不能把未入选误写成未审阅。 | analysis-decision:SF-2026-ARXIV-2607-29549 |
| SF-2026-ARXIV-2607-29575 | score_7_9 | not_selected | — | — | 已完成作者侧 exact-v1 Review；相对三个入选单元，其跨层影响或机制独立性较窄，不能把未入选误写成未审阅。 | analysis-decision:SF-2026-ARXIV-2607-29575 |
| SF-2026-ARXIV-2607-29591 | score_7_9 | not_selected | — | — | 已完成作者侧 exact-v1 Review；相对三个入选单元，其跨层影响或机制独立性较窄，不能把未入选误写成未审阅。 | analysis-decision:SF-2026-ARXIV-2607-29591 |
| SF-2026-ARXIV-2607-29600 | score_7_9 | not_selected | — | — | 已完成作者侧 exact-v1 Review；相对三个入选单元，其跨层影响或机制独立性较窄，不能把未入选误写成未审阅。 | analysis-decision:SF-2026-ARXIV-2607-29600 |
| SF-2026-ARXIV-2607-29626 | score_7_9 | not_selected | — | — | 已完成作者侧 exact-v1 Review；相对三个入选单元，其跨层影响或机制独立性较窄，不能把未入选误写成未审阅。 | analysis-decision:SF-2026-ARXIV-2607-29626 |
| SF-2026-ARXIV-2607-29678 | score_7_9; potential_books_delta | selected | DA-20260803-3 | — | 在 102-family frontier 中，该机制具有明确运行时状态、控制器和 failure/fallback 边界，并横跨模型机制与系统 owner。 | analysis:DA-20260803-3 |

<!-- analysis-decision:SF-2026-ARXIV-2607-28631:start -->
`Can AI Evaluate AI Scientists? A Benchmarking Study of Autonomous Research Generation Systems Using Automated Multi-Model Review` 已进入完整 frontier 并完成 exact-v1 Review；未选入三项长叙事只反映叙事预算与相对优先级，不改变其 Score、Evidence 或 Books 比较责任。
<!-- analysis-decision:SF-2026-ARXIV-2607-28631:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-28633:start -->
`Topology-Aware Data Movement for Disaggregated GPU Inference` 已进入完整 frontier 并完成 exact-v1 Review；未选入三项长叙事只反映叙事预算与相对优先级，不改变其 Score、Evidence 或 Books 比较责任。
<!-- analysis-decision:SF-2026-ARXIV-2607-28633:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-28636:start -->
`Chain-of-Models: Cross-Model Auditing for Bias-Robust LLM Judges` 已进入完整 frontier 并完成 exact-v1 Review；未选入三项长叙事只反映叙事预算与相对优先级，不改变其 Score、Evidence 或 Books 比较责任。
<!-- analysis-decision:SF-2026-ARXIV-2607-28636:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-28638:start -->
`Learning Stateful Predictive Knowledge From Experience` 已进入完整 frontier 并完成 exact-v1 Review；未选入三项长叙事只反映叙事预算与相对优先级，不改变其 Score、Evidence 或 Books 比较责任。
<!-- analysis-decision:SF-2026-ARXIV-2607-28638:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-28658:start -->
`Evaluating Federated Pre-Training: On the Reliability of Downstream Fine-Tuning and Intrinsic Evaluation` 已进入完整 frontier 并完成 exact-v1 Review；未选入三项长叙事只反映叙事预算与相对优先级，不改变其 Score、Evidence 或 Books 比较责任。
<!-- analysis-decision:SF-2026-ARXIV-2607-28658:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-28666:start -->
`The Checking Problem: What must be true before AI ships in a regulated firm` 已进入完整 frontier 并完成 exact-v1 Review；未选入三项长叙事只反映叙事预算与相对优先级，不改变其 Score、Evidence 或 Books 比较责任。
<!-- analysis-decision:SF-2026-ARXIV-2607-28666:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-28678:start -->
`ViSAGE: Constructing Self-Correcting Memories for Long-Form Video Understanding` 已进入完整 frontier 并完成 exact-v1 Review；未选入三项长叙事只反映叙事预算与相对优先级，不改变其 Score、Evidence 或 Books 比较责任。
<!-- analysis-decision:SF-2026-ARXIV-2607-28678:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-28684:start -->
`Library Reachability in LSR-Synth: How Anti-Memorization Design Changes the Measurement of Symbolic Discovery` 已进入完整 frontier 并完成 exact-v1 Review；未选入三项长叙事只反映叙事预算与相对优先级，不改变其 Score、Evidence 或 Books 比较责任。
<!-- analysis-decision:SF-2026-ARXIV-2607-28684:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-28685:start -->
`Safety, or Just Capability? A Validity Audit of Agent-Safety Benchmarks` 已进入完整 frontier 并完成 exact-v1 Review；未选入三项长叙事只反映叙事预算与相对优先级，不改变其 Score、Evidence 或 Books 比较责任。
<!-- analysis-decision:SF-2026-ARXIV-2607-28685:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-28692:start -->
`SciToolAgent-Evo: An Ontology-Aware Self-Evolving Agent for Open-World Scientific Tool Acquisition` 已进入完整 frontier 并完成 exact-v1 Review；未选入三项长叙事只反映叙事预算与相对优先级，不改变其 Score、Evidence 或 Books 比较责任。
<!-- analysis-decision:SF-2026-ARXIV-2607-28692:end -->

<!-- analysis:DA-20260803-1:start -->
### DA-20260803-1 — WitCert: Sound Runtime Risk Observability and Gating for KV-Cache Quantization

### WitCert: Sound Runtime Risk Observability and Gating for KV-Cache Quantization

- **Status / Evidence:** Experimental；exact-v1 HTML 已读取并保存校验和；Score V2=`9`。
- **Problem / old solution:** 既有路径通常把 decode-state compression or translation 隐含在模型调用或离线平均指标中；在较小规模、单一模型或无跨请求状态时成本较低，但难以回答谁拥有失败恢复与版本一致性。
- **Changed constraint:** 论文面对的约束由摘要和全文共同限定为：KV-cache quantization is validated today by offline benchmark averages; a deployed system cannot tell whether compression is damaging the request it is serving right now. We give it a provably sound runtime meter -- a "DTrace for KV quantization": a per-(layer, head, step) upper bound on the total variation between exact and compressed attention.
- **Mechanism:** exact-v1 的方法段写明：The meter loop above is the design; Fig. shows where it lives in a serving engine. The rest of this section is organized as implementation (), evaluation () and analysis ().
- **State ownership:** 需要显式绑定 layer/head/token KV identity；canonical owner 是 `INFER-KV-CACHE`，而不是论文应用领域本身。
- **Control / data flow:** 数据由工作负载进入机制实现，cache manager 决定是否执行、路由、提交或回退；输出必须携带与输入同一版本域的证据。
- **Implementation surface:** 全文 locator=`Architecture; papers/2026/08/_sources/arxiv-owner-replay-20260903/20260803/exact-v1-text/2607.28699v1.txt`；公开实现、硬件或训练配置只按正文披露解释，未披露字段不补写。
- **Evaluation contract:** Unless stated otherwise: Qwen2.5-7B , Mistral-7B and Yi-1.5-6B , three domains (natural text, code, synthetic retrieval), documents, 8k context, online block-wise scaling (no whole-sequence statistics), 8-bit KV, , , , statistics at KV-head granularity (an unadorned always means ). Table reports joint KV step coverage, single run per cell, with the deterministic bound placed at . 该结果只绑定论文声明的数据、模型、硬件、精度、长度、batch/concurrency 与 evaluator；缺失字段均为 `Not Disclosed`。
- **Proves / does not prove:** 证据支持该受限 workload 中机制可行或暴露既有评价缺口；不证明跨模型、跨硬件、跨领域或生产 SLO 的普遍优势。
- **Trade-off / failure mode:** 新增状态、控制器和观测提高可验证性，但引入版本错配、额外延迟/内存/通信、错误路由及 evaluator bias。全文边界：A sound runtime meter turns KV-cache compression from an open-loop bet into an observable, gateable system quantity: any cache-preserving scheme can be measured in live serving, broken schemes are repaired at benchmark scale by meter-driven gating (fp8 restored from 22.8 to 79.7, paired difference against uncompressed), and analysis with the meter shows that what keeps aggressive schemes alive is cross-layer cancellation rather than per-step fidelity. On the certified tier, trading an explicit request-level risk budget for coverage is what turns the certificate from decoration into a tool: the sub-Gaussian certificate reduces the page-in rate of a sound deterministic bound by relative, with very weak dependenc…
- **Coexistence / evolution:** 旧方案在低风险、短状态或同构部署中仍成立；新机制只在约束变化使错误代价或状态漂移不可忽略时接手。
- **Books route:** 对照 `INFER-KV-CACHE` 及相邻章节；先进入按日期排序的 writeback queue，根任务合并同 owner 后决定最终写回。
<!-- analysis:DA-20260803-1:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-28707:start -->
`Demystifying Entropy-based Selection for Chain-of-Thought Compression in Large Reasoning Models` 已进入完整 frontier 并完成 exact-v1 Review；未选入三项长叙事只反映叙事预算与相对优先级，不改变其 Score、Evidence 或 Books 比较责任。
<!-- analysis-decision:SF-2026-ARXIV-2607-28707:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-28777:start -->
`Self-Supervised Skill Optimization` 已进入完整 frontier 并完成 exact-v1 Review；未选入三项长叙事只反映叙事预算与相对优先级，不改变其 Score、Evidence 或 Books 比较责任。
<!-- analysis-decision:SF-2026-ARXIV-2607-28777:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-28788:start -->
`EarlyDx: An Admission-Anchored Benchmark for Open-Ended Generation of Evidence-Supported ED-Encounter Diagnoses` 已进入完整 frontier 并完成 exact-v1 Review；未选入三项长叙事只反映叙事预算与相对优先级，不改变其 Score、Evidence 或 Books 比较责任。
<!-- analysis-decision:SF-2026-ARXIV-2607-28788:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-28801:start -->
`Benchmarks Are Not Monolithic: Sample-Level Auditing and Orchestration for LLM Evaluation` 已进入完整 frontier 并完成 exact-v1 Review；未选入三项长叙事只反映叙事预算与相对优先级，不改变其 Score、Evidence 或 Books 比较责任。
<!-- analysis-decision:SF-2026-ARXIV-2607-28801:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-28802:start -->
`Model or Harness? An Interaction-Centric Taxonomy for Localizing Agent Failures` 已进入完整 frontier 并完成 exact-v1 Review；未选入三项长叙事只反映叙事预算与相对优先级，不改变其 Score、Evidence 或 Books 比较责任。
<!-- analysis-decision:SF-2026-ARXIV-2607-28802:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-28818:start -->
`Best Friends, Not Forever: Evaluating Long-Horizon Persona Collapse and Behavioral Drift in AI Companions` 已进入完整 frontier 并完成 exact-v1 Review；未选入三项长叙事只反映叙事预算与相对优先级，不改变其 Score、Evidence 或 Books 比较责任。
<!-- analysis-decision:SF-2026-ARXIV-2607-28818:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-28824:start -->
`Characterizing LLM Kernel Access and Memory Interaction in Multi-Partition NUMA GPUs` 已进入完整 frontier 并完成 exact-v1 Review；未选入三项长叙事只反映叙事预算与相对优先级，不改变其 Score、Evidence 或 Books 比较责任。
<!-- analysis-decision:SF-2026-ARXIV-2607-28824:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-28829:start -->
`When Unlearning Fails: Reliable Data Deletion under Post-Training in Agent Networks` 已进入完整 frontier 并完成 exact-v1 Review；未选入三项长叙事只反映叙事预算与相对优先级，不改变其 Score、Evidence 或 Books 比较责任。
<!-- analysis-decision:SF-2026-ARXIV-2607-28829:end -->

<!-- analysis:DA-20260803-2:start -->
### DA-20260803-2 — DeltaServe: Host-Agnostic Co-Serving of Inference and Fine-Tuning for LLMs

### DeltaServe: Host-Agnostic Co-Serving of Inference and Fine-Tuning for LLMs

- **Status / Evidence:** Experimental；exact-v1 HTML 已读取并保存校验和；Score V2=`8`。
- **Problem / old solution:** 既有路径通常把 shared inference capacity 隐含在模型调用或离线平均指标中；在较小规模、单一模型或无跨请求状态时成本较低，但难以回答谁拥有失败恢复与版本一致性。
- **Changed constraint:** 论文面对的约束由摘要和全文共同限定为：LLM serving systems are provisioned for peak load to meet strict latency targets, leaving substantial GPU compute idle whenever traffic falls below peak. We present DeltaServe, a host-agnostic co-serving design that converts this idle inference capacity into LoRA fine-tuning throughput while preserving inference service-level objectives (SLOs).
- **Mechanism:** exact-v1 的方法段写明：The background discussion shows that LoRA co-serving is appealing because inference and fine-tuning share the frozen base model, but realizing it inside an existing serving engine is difficult: fine-tuning needs training-specific control, activation capture, backward execution, and optimizer updates that inference engines are not designed to provide. addresses this gap by separating what must be added for fine-tuning from what should remain under the host system’s control. Its design keeps the host responsible for request handling, batching, KV-cache management, sampling, and optimized forward execution, while adds only the mechanisms needed to turn admitted fine-tuning samples into prefill-like batch entries…
- **State ownership:** 需要显式绑定 request/model/adaptation residency；canonical owner 是 `INFER-SCHEDULING`，而不是论文应用领域本身。
- **Control / data flow:** 数据由工作负载进入机制实现，scheduler 决定是否执行、路由、提交或回退；输出必须携带与输入同一版本域的证据。
- **Implementation surface:** 全文 locator=`System Design; papers/2026/08/_sources/arxiv-owner-replay-20260903/20260803/exact-v1-text/2607.28848v1.txt`；公开实现、硬件或训练配置只按正文披露解释，未披露字段不补写。
- **Evaluation contract:** In this section, we evaluate ’s ability to fold LoRA fine-tuning into a host inference engine under diverse conditions, harvesting the capacity inference leaves idle without violating the host’s inference SLOs, guided by the following key questions: Does exploit idle capacity left by gaps and low-load periods in inference workloads, converting it into fine-tuning throughput while preserving inference SLOs? How does this compare with LLMStation and with a split-pool deployment in fine-tuning throughput, average latency, and SLO compliance (Section )? 该结果只绑定论文声明的数据、模型、硬件、精度、长度、batch/concurrency 与 evaluator；缺失字段均为 `Not Disclosed`。
- **Proves / does not prove:** 证据支持该受限 workload 中机制可行或暴露既有评价缺口；不证明跨模型、跨硬件、跨领域或生产 SLO 的普遍优势。
- **Trade-off / failure mode:** 新增状态、控制器和观测提高可验证性，但引入版本错配、额外延迟/内存/通信、错误路由及 evaluator bias。全文边界：This paper introduced , a host-agnostic co-serving design that folds LoRA fine-tuning into an existing inference engine under SLO control, driven by a CUDA-graph-aware latency model and realized on vLLM, SGLang, and S-LoRA. On a Nutanix production trace it delivers the fine-tuning throughput of LLMStation at inference SLO compliance versus LLMStation’s , harvesting idle GPU capacity without compromising interactive latency.
- **Coexistence / evolution:** 旧方案在低风险、短状态或同构部署中仍成立；新机制只在约束变化使错误代价或状态漂移不可忽略时接手。
- **Books route:** 对照 `INFER-SCHEDULING` 及相邻章节；先进入按日期排序的 writeback queue，根任务合并同 owner 后决定最终写回。
<!-- analysis:DA-20260803-2:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-28871:start -->
`Validation Evidence in LLM Repair Agents: How Much of What Passes Actually Tests the Bug?` 已进入完整 frontier 并完成 exact-v1 Review；未选入三项长叙事只反映叙事预算与相对优先级，不改变其 Score、Evidence 或 Books 比较责任。
<!-- analysis-decision:SF-2026-ARXIV-2607-28871:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-28884:start -->
`Hollow-LLM Attack: Computationally Trivial Weights in Zero-Knowledge Verification of LLM Inference` 已进入完整 frontier 并完成 exact-v1 Review；未选入三项长叙事只反映叙事预算与相对优先级，不改变其 Score、Evidence 或 Books 比较责任。
<!-- analysis-decision:SF-2026-ARXIV-2607-28884:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-28896:start -->
`TORUS: A Test of Rendering-Understanding Self-Coherence for Unified Audio Models` 已进入完整 frontier 并完成 exact-v1 Review；未选入三项长叙事只反映叙事预算与相对优先级，不改变其 Score、Evidence 或 Books 比较责任。
<!-- analysis-decision:SF-2026-ARXIV-2607-28896:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-28940:start -->
`TransX: Scaling Transformer-based Recommendation via Behavioral and Serving Stream Crossings` 已进入完整 frontier 并完成 exact-v1 Review；未选入三项长叙事只反映叙事预算与相对优先级，不改变其 Score、Evidence 或 Books 比较责任。
<!-- analysis-decision:SF-2026-ARXIV-2607-28940:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-28966:start -->
`BLADE: Boundary-Expanded and Layer-Adaptive Dynamic Exit for Efficient LLM Reasoning` 已进入完整 frontier 并完成 exact-v1 Review；未选入三项长叙事只反映叙事预算与相对优先级，不改变其 Score、Evidence 或 Books 比较责任。
<!-- analysis-decision:SF-2026-ARXIV-2607-28966:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-28979:start -->
`Mixture-of-Translators: Translating KV Caches Across Heterogeneous Large Language Models` 已进入完整 frontier 并完成 exact-v1 Review；未选入三项长叙事只反映叙事预算与相对优先级，不改变其 Score、Evidence 或 Books 比较责任。
<!-- analysis-decision:SF-2026-ARXIV-2607-28979:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-28993:start -->
`ST-WAM: Semantic-Temporal World Action Model for Robust Manipulation under Visual Distribution Shifts` 已进入完整 frontier 并完成 exact-v1 Review；未选入三项长叙事只反映叙事预算与相对优先级，不改变其 Score、Evidence 或 Books 比较责任。
<!-- analysis-decision:SF-2026-ARXIV-2607-28993:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-29032:start -->
`TransMem: Transforming Hidden States into Memory for Large Language Models` 已进入完整 frontier 并完成 exact-v1 Review；未选入三项长叙事只反映叙事预算与相对优先级，不改变其 Score、Evidence 或 Books 比较责任。
<!-- analysis-decision:SF-2026-ARXIV-2607-29032:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-29053:start -->
`Who Wins Where? Conformal Model Comparison for Local Superiority` 已进入完整 frontier 并完成 exact-v1 Review；未选入三项长叙事只反映叙事预算与相对优先级，不改变其 Score、Evidence 或 Books 比较责任。
<!-- analysis-decision:SF-2026-ARXIV-2607-29053:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-29069:start -->
`Rethinking AI Cloud Infrastructure for Agentic Serving Systems with the Aries Experimentation Framework` 已进入完整 frontier 并完成 exact-v1 Review；未选入三项长叙事只反映叙事预算与相对优先级，不改变其 Score、Evidence 或 Books 比较责任。
<!-- analysis-decision:SF-2026-ARXIV-2607-29069:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-29076:start -->
`Selective KV Cache Protection for Noise-Resilient LLM Inference on Analog Compute-In-Memory Systems` 已进入完整 frontier 并完成 exact-v1 Review；未选入三项长叙事只反映叙事预算与相对优先级，不改变其 Score、Evidence 或 Books 比较责任。
<!-- analysis-decision:SF-2026-ARXIV-2607-29076:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-29104:start -->
`Reproducing LightMem: Naive RAG Is Just as Good for Memory Management` 已进入完整 frontier 并完成 exact-v1 Review；未选入三项长叙事只反映叙事预算与相对优先级，不改变其 Score、Evidence 或 Books 比较责任。
<!-- analysis-decision:SF-2026-ARXIV-2607-29104:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-29125:start -->
`M3-DuplexBench: A Multi-Turn, Multilingual, Multidomain Benchmark for Full-Duplex Spoken Dialogue Models` 已进入完整 frontier 并完成 exact-v1 Review；未选入三项长叙事只反映叙事预算与相对优先级，不改变其 Score、Evidence 或 Books 比较责任。
<!-- analysis-decision:SF-2026-ARXIV-2607-29125:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-29167:start -->
`Memory Provenance Laundering in LLM Agents: A Non-Amplification Firewall for Persistent Memory` 已进入完整 frontier 并完成 exact-v1 Review；未选入三项长叙事只反映叙事预算与相对优先级，不改变其 Score、Evidence 或 Books 比较责任。
<!-- analysis-decision:SF-2026-ARXIV-2607-29167:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-29175:start -->
`Execution-First Synthetic Tool-Use Trace Generation for LLM Agents` 已进入完整 frontier 并完成 exact-v1 Review；未选入三项长叙事只反映叙事预算与相对优先级，不改变其 Score、Evidence 或 Books 比较责任。
<!-- analysis-decision:SF-2026-ARXIV-2607-29175:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-29190:start -->
`CAGE: Certified Authorization under Typed-Return Uncertainty for Tool-Using Agents` 已进入完整 frontier 并完成 exact-v1 Review；未选入三项长叙事只反映叙事预算与相对优先级，不改变其 Score、Evidence 或 Books 比较责任。
<!-- analysis-decision:SF-2026-ARXIV-2607-29190:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-29199:start -->
`Alignment Is Local: A Paired Diagnostic for GUI Agents under User-Side Persuasion` 已进入完整 frontier 并完成 exact-v1 Review；未选入三项长叙事只反映叙事预算与相对优先级，不改变其 Score、Evidence 或 Books 比较责任。
<!-- analysis-decision:SF-2026-ARXIV-2607-29199:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-29218:start -->
`MirrorCraft: Paired Evaluation under Hidden Rule Changes in Minecraft` 已进入完整 frontier 并完成 exact-v1 Review；未选入三项长叙事只反映叙事预算与相对优先级，不改变其 Score、Evidence 或 Books 比较责任。
<!-- analysis-decision:SF-2026-ARXIV-2607-29218:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-29221:start -->
`MOSAIC: Masked Outsourcing of Secure AI Computations` 已进入完整 frontier 并完成 exact-v1 Review；未选入三项长叙事只反映叙事预算与相对优先级，不改变其 Score、Evidence 或 Books 比较责任。
<!-- analysis-decision:SF-2026-ARXIV-2607-29221:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-29235:start -->
`FBFM: A Training-Free Asynchronous Feedback Mechanism for Flow-Matching in World-Action Models Execution` 已进入完整 frontier 并完成 exact-v1 Review；未选入三项长叙事只反映叙事预算与相对优先级，不改变其 Score、Evidence 或 Books 比较责任。
<!-- analysis-decision:SF-2026-ARXIV-2607-29235:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-29252:start -->
`CalibratedRubric: Task-Adaptive Rubric Banks for Open-Ended LLM Evaluation` 已进入完整 frontier 并完成 exact-v1 Review；未选入三项长叙事只反映叙事预算与相对优先级，不改变其 Score、Evidence 或 Books 比较责任。
<!-- analysis-decision:SF-2026-ARXIV-2607-29252:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-29254:start -->
`Tool Specifications Matter: Uncovering and Mitigating Safety Risks in AI Agents` 已进入完整 frontier 并完成 exact-v1 Review；未选入三项长叙事只反映叙事预算与相对优先级，不改变其 Score、Evidence 或 Books 比较责任。
<!-- analysis-decision:SF-2026-ARXIV-2607-29254:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-29302:start -->
`BWM: A Low-Cost High-Fidelity World Simulator for Robot Learning` 已进入完整 frontier 并完成 exact-v1 Review；未选入三项长叙事只反映叙事预算与相对优先级，不改变其 Score、Evidence 或 Books 比较责任。
<!-- analysis-decision:SF-2026-ARXIV-2607-29302:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-29320:start -->
`MAGA: Multi-Platform Self-Fusion of GUI Agents via Structured Action Distillation` 已进入完整 frontier 并完成 exact-v1 Review；未选入三项长叙事只反映叙事预算与相对优先级，不改变其 Score、Evidence 或 Books 比较责任。
<!-- analysis-decision:SF-2026-ARXIV-2607-29320:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-29377:start -->
`Zero-Mem: Zero-Token Memory Operations for LLM Agents` 已进入完整 frontier 并完成 exact-v1 Review；未选入三项长叙事只反映叙事预算与相对优先级，不改变其 Score、Evidence 或 Books 比较责任。
<!-- analysis-decision:SF-2026-ARXIV-2607-29377:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-29393:start -->
`AquaJEPA: An Action-Conditioned Multimodal JEPA Family for Underwater Robot Dynamics` 已进入完整 frontier 并完成 exact-v1 Review；未选入三项长叙事只反映叙事预算与相对优先级，不改变其 Score、Evidence 或 Books 比较责任。
<!-- analysis-decision:SF-2026-ARXIV-2607-29393:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-29398:start -->
`OnlineCache: Learning Dynamic Caching Policies with Error Correction for Efficient Diffusion Inference` 已进入完整 frontier 并完成 exact-v1 Review；未选入三项长叙事只反映叙事预算与相对优先级，不改变其 Score、Evidence 或 Books 比较责任。
<!-- analysis-decision:SF-2026-ARXIV-2607-29398:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-29405:start -->
`Beyond Component Testing: Validating Agentic AI Systems` 已进入完整 frontier 并完成 exact-v1 Review；未选入三项长叙事只反映叙事预算与相对优先级，不改变其 Score、Evidence 或 Books 比较责任。
<!-- analysis-decision:SF-2026-ARXIV-2607-29405:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-29431:start -->
`ModelEquivBench: Certifying Multi-Relational Evaluation of LLM-Generated Optimization Models` 已进入完整 frontier 并完成 exact-v1 Review；未选入三项长叙事只反映叙事预算与相对优先级，不改变其 Score、Evidence 或 Books 比较责任。
<!-- analysis-decision:SF-2026-ARXIV-2607-29431:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-29440:start -->
`Beyond Retrieval: Analytic Memory for Multimodal Agents` 已进入完整 frontier 并完成 exact-v1 Review；未选入三项长叙事只反映叙事预算与相对优先级，不改变其 Score、Evidence 或 Books 比较责任。
<!-- analysis-decision:SF-2026-ARXIV-2607-29440:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-29465:start -->
`CARA: Exact Local Repair with Fresh One-Action Certification for Cloud Consolidation` 已进入完整 frontier 并完成 exact-v1 Review；未选入三项长叙事只反映叙事预算与相对优先级，不改变其 Score、Evidence 或 Books 比较责任。
<!-- analysis-decision:SF-2026-ARXIV-2607-29465:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-29516:start -->
`From Code Review to Code Critique: Intent, Drift, and Spotlight for AI-Generated Diffs at Scale` 已进入完整 frontier 并完成 exact-v1 Review；未选入三项长叙事只反映叙事预算与相对优先级，不改变其 Score、Evidence 或 Books 比较责任。
<!-- analysis-decision:SF-2026-ARXIV-2607-29516:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-29549:start -->
`AMTFV: Agentic Mathematical Tool-Flow Verification for LLM Self-Correction` 已进入完整 frontier 并完成 exact-v1 Review；未选入三项长叙事只反映叙事预算与相对优先级，不改变其 Score、Evidence 或 Books 比较责任。
<!-- analysis-decision:SF-2026-ARXIV-2607-29549:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-29575:start -->
`SLIM: Saturation-Aware Lightweight Performance Modeling for LLM Serving` 已进入完整 frontier 并完成 exact-v1 Review；未选入三项长叙事只反映叙事预算与相对优先级，不改变其 Score、Evidence 或 Books 比较责任。
<!-- analysis-decision:SF-2026-ARXIV-2607-29575:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-29591:start -->
`ResKV: Reconstructing Omitted Attention Contributions for Fixed-Budget KV Cache Compression` 已进入完整 frontier 并完成 exact-v1 Review；未选入三项长叙事只反映叙事预算与相对优先级，不改变其 Score、Evidence 或 Books 比较责任。
<!-- analysis-decision:SF-2026-ARXIV-2607-29591:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-29600:start -->
`HAM-VLN: Harnessing Hierarchical Agentic Memory for Zero-Shot Vision-and-Language Navigation` 已进入完整 frontier 并完成 exact-v1 Review；未选入三项长叙事只反映叙事预算与相对优先级，不改变其 Score、Evidence 或 Books 比较责任。
<!-- analysis-decision:SF-2026-ARXIV-2607-29600:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-29626:start -->
`AgentHPOBench: A Benchmark For Evaluating LLM Agents as Sequential Hyperparameter Optimizers` 已进入完整 frontier 并完成 exact-v1 Review；未选入三项长叙事只反映叙事预算与相对优先级，不改变其 Score、Evidence 或 Books 比较责任。
<!-- analysis-decision:SF-2026-ARXIV-2607-29626:end -->

<!-- analysis:DA-20260803-3:start -->
### DA-20260803-3 — TokTier: Exact Stateful CPU+GPU Tokenization for Agentic LLM Serving

### TokTier: Exact Stateful CPU+GPU Tokenization for Agentic LLM Serving

- **Status / Evidence:** Experimental；exact-v1 HTML 已读取并保存校验和；Score V2=`8`。
- **Problem / old solution:** 既有路径通常把 request execution lifecycle 隐含在模型调用或离线平均指标中；在较小规模、单一模型或无跨请求状态时成本较低，但难以回答谁拥有失败恢复与版本一致性。
- **Changed constraint:** 论文面对的约束由摘要和全文共同限定为：LLM serving caches prompt KV state, yet most front ends still re-tokenize the full request on every call. Coding agents pay most: sessions repeatedly submit a long transcript after a small append, which can shift token boundaries near the end of the prior sequence.
- **Mechanism:** exact-v1 的方法段写明：is a tokenization service placed between the request router and the model engine. It accepts request text and a model identifier, then returns reference-equivalent token IDs. The service keeps token state for live sessions and selects an execution path from that state and the request size. Figure shows the data flow. Each tokenizer version is registered by content hash. Its entry carries the added-token rules, normalization configuration, pre-tokenization rules, vocabulary, merge table, and the family-specific checks used by the repair and GPU paths. A request is never interpreted through ambient process state, and a session created under one tokenizer version is never repaired under another.
- **State ownership:** 需要显式绑定 request/stream/session state；canonical owner 是 `INFER-REQUEST-LIFECYCLE`，而不是论文应用领域本身。
- **Control / data flow:** 数据由工作负载进入机制实现，serving engine 决定是否执行、路由、提交或回退；输出必须携带与输入同一版本域的证据。
- **Implementation surface:** 全文 locator=`System Design; papers/2026/08/_sources/arxiv-owner-replay-20260903/20260803/exact-v1-text/2607.29678v1.txt`；公开实现、硬件或训练配置只按正文披露解释，未披露字段不补写。
- **Evaluation contract:** We first place both execution paths against the measured baselines, then test them against frozen reference tokenizers. We measure incremental repair and GPU full tokenization separately, before evaluating burst tails, capacity, and time to first token with vLLM. The final experiments cover resource use and runtime verification. What limits the GPU path is discussed with the other limitations in §. Experiments run on a dual-socket AMD EPYC 9115 host (32 physical cores, SMT disabled) with four RTX PRO 6000 Blackwell GPUs of 96 GB each. CPU experiments are NUMA-pinned. One GPU serves vLLM 0.25 with prefix caching enabled and one serves unless stated otherwise. Tokenizer artifacts, datasets, and dependency versio… 该结果只绑定论文声明的数据、模型、硬件、精度、长度、batch/concurrency 与 evaluator；缺失字段均为 `Not Disclosed`。
- **Proves / does not prove:** 证据支持该受限 workload 中机制可行或暴露既有评价缺口；不证明跨模型、跨硬件、跨领域或生产 SLO 的普遍优势。
- **Trade-off / failure mode:** 新增状态、控制器和观测提高可验证性，但引入版本错配、额外延迟/内存/通信、错误路由及 evaluator bias。全文边界：We collect the system’s limitations here, from the physical floor of the GPU path to the boundary of what zero divergence establishes.
- **Coexistence / evolution:** 旧方案在低风险、短状态或同构部署中仍成立；新机制只在约束变化使错误代价或状态漂移不可忽略时接手。
- **Books route:** 对照 `INFER-REQUEST-LIFECYCLE` 及相邻章节；先进入按日期排序的 writeback queue，根任务合并同 owner 后决定最终写回。
<!-- analysis:DA-20260803-3:end -->

## 6. Books Comparison

<!-- validator:books-comparison-v1 -->
| Source Family ID | Stable Node ID | Target Chapter Ref | Adjacent Chapter Refs | Existing Proposition | New Evidence Delta | Evolution Relation | Decision | Books Review Ref |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |

<!-- existing:SF-2026-ARXIV-2607-28631:start -->
Canonical owner 已解析为 `PLATFORM-EVALUATION-SYSTEM` / `books/part-06-ai-infrastructure/66-evaluation-system.md`；目标与相邻章节的 proposition-level 对读由根任务按日期串行执行，作者侧不在并发期间推定结果。
<!-- existing:SF-2026-ARXIV-2607-28631:end -->

<!-- delta:SF-2026-ARXIV-2607-28631:start -->
Exact-v1 evidence and source-specific review are available at `review:SF-2026-ARXIV-2607-28631`; durable delta must be reconciled against current Books rather than appended as a paper summary.
<!-- delta:SF-2026-ARXIV-2607-28631:end -->

<!-- books-review:SF-2026-ARXIV-2607-28631:start -->
Decision=`Not Assessed`；不得在共享 Books 未取得日期有序写锁时把 queue 当作已集成。
<!-- books-review:SF-2026-ARXIV-2607-28631:end -->

<!-- existing:SF-2026-ARXIV-2607-28633:start -->
Canonical owner 已解析为 `INFER-PD-DISAGGREGATION` / `books/part-05-inference-system/55-pd-disaggregation.md`；目标与相邻章节的 proposition-level 对读由根任务按日期串行执行，作者侧不在并发期间推定结果。
<!-- existing:SF-2026-ARXIV-2607-28633:end -->

<!-- delta:SF-2026-ARXIV-2607-28633:start -->
Exact-v1 evidence and source-specific review are available at `review:SF-2026-ARXIV-2607-28633`; durable delta must be reconciled against current Books rather than appended as a paper summary.
<!-- delta:SF-2026-ARXIV-2607-28633:end -->

<!-- books-review:SF-2026-ARXIV-2607-28633:start -->
Decision=`Not Assessed`；不得在共享 Books 未取得日期有序写锁时把 queue 当作已集成。
<!-- books-review:SF-2026-ARXIV-2607-28633:end -->

<!-- existing:SF-2026-ARXIV-2607-28636:start -->
Canonical owner 已解析为 `PLATFORM-EVALUATION-SYSTEM` / `books/part-06-ai-infrastructure/66-evaluation-system.md`；目标与相邻章节的 proposition-level 对读由根任务按日期串行执行，作者侧不在并发期间推定结果。
<!-- existing:SF-2026-ARXIV-2607-28636:end -->

<!-- delta:SF-2026-ARXIV-2607-28636:start -->
Exact-v1 evidence and source-specific review are available at `review:SF-2026-ARXIV-2607-28636`; durable delta must be reconciled against current Books rather than appended as a paper summary.
<!-- delta:SF-2026-ARXIV-2607-28636:end -->

<!-- books-review:SF-2026-ARXIV-2607-28636:start -->
Decision=`Not Assessed`；不得在共享 Books 未取得日期有序写锁时把 queue 当作已集成。
<!-- books-review:SF-2026-ARXIV-2607-28636:end -->

<!-- existing:SF-2026-ARXIV-2607-28638:start -->
Canonical owner 已解析为 `AGENT-MEMORY` / `books/part-07-agent/77-memory.md`；目标与相邻章节的 proposition-level 对读由根任务按日期串行执行，作者侧不在并发期间推定结果。
<!-- existing:SF-2026-ARXIV-2607-28638:end -->

<!-- delta:SF-2026-ARXIV-2607-28638:start -->
Exact-v1 evidence and source-specific review are available at `review:SF-2026-ARXIV-2607-28638`; durable delta must be reconciled against current Books rather than appended as a paper summary.
<!-- delta:SF-2026-ARXIV-2607-28638:end -->

<!-- books-review:SF-2026-ARXIV-2607-28638:start -->
Decision=`Not Assessed`；不得在共享 Books 未取得日期有序写锁时把 queue 当作已集成。
<!-- books-review:SF-2026-ARXIV-2607-28638:end -->

<!-- existing:SF-2026-ARXIV-2607-28640:start -->
Canonical owner 已解析为 `MULTIMODAL-REPRESENTATION` / `books/part-03-multimodal-world-models/23-multimodal-representation.md`；目标与相邻章节的 proposition-level 对读由根任务按日期串行执行，作者侧不在并发期间推定结果。
<!-- existing:SF-2026-ARXIV-2607-28640:end -->

<!-- delta:SF-2026-ARXIV-2607-28640:start -->
Exact-v1 evidence and source-specific review are available at `review:SF-2026-ARXIV-2607-28640`; durable delta must be reconciled against current Books rather than appended as a paper summary.
<!-- delta:SF-2026-ARXIV-2607-28640:end -->

<!-- books-review:SF-2026-ARXIV-2607-28640:start -->
Decision=`Not Assessed`；不得在共享 Books 未取得日期有序写锁时把 queue 当作已集成。
<!-- books-review:SF-2026-ARXIV-2607-28640:end -->

<!-- existing:SF-2026-ARXIV-2607-28642:start -->
Canonical owner 已解析为 `AGENT-CONTEXT` / `books/part-07-agent/75-context.md`；目标与相邻章节的 proposition-level 对读由根任务按日期串行执行，作者侧不在并发期间推定结果。
<!-- existing:SF-2026-ARXIV-2607-28642:end -->

<!-- delta:SF-2026-ARXIV-2607-28642:start -->
Exact-v1 evidence and source-specific review are available at `review:SF-2026-ARXIV-2607-28642`; durable delta must be reconciled against current Books rather than appended as a paper summary.
<!-- delta:SF-2026-ARXIV-2607-28642:end -->

<!-- books-review:SF-2026-ARXIV-2607-28642:start -->
Decision=`Not Assessed`；不得在共享 Books 未取得日期有序写锁时把 queue 当作已集成。
<!-- books-review:SF-2026-ARXIV-2607-28642:end -->

<!-- existing:SF-2026-ARXIV-2607-28658:start -->
Canonical owner 已解析为 `PLATFORM-EVALUATION-SYSTEM` / `books/part-06-ai-infrastructure/66-evaluation-system.md`；目标与相邻章节的 proposition-level 对读由根任务按日期串行执行，作者侧不在并发期间推定结果。
<!-- existing:SF-2026-ARXIV-2607-28658:end -->

<!-- delta:SF-2026-ARXIV-2607-28658:start -->
Exact-v1 evidence and source-specific review are available at `review:SF-2026-ARXIV-2607-28658`; durable delta must be reconciled against current Books rather than appended as a paper summary.
<!-- delta:SF-2026-ARXIV-2607-28658:end -->

<!-- books-review:SF-2026-ARXIV-2607-28658:start -->
Decision=`Not Assessed`；不得在共享 Books 未取得日期有序写锁时把 queue 当作已集成。
<!-- books-review:SF-2026-ARXIV-2607-28658:end -->

<!-- existing:SF-2026-ARXIV-2607-28666:start -->
Canonical owner 已解析为 `PLATFORM-EVALUATION-SYSTEM` / `books/part-06-ai-infrastructure/66-evaluation-system.md`；目标与相邻章节的 proposition-level 对读由根任务按日期串行执行，作者侧不在并发期间推定结果。
<!-- existing:SF-2026-ARXIV-2607-28666:end -->

<!-- delta:SF-2026-ARXIV-2607-28666:start -->
Exact-v1 evidence and source-specific review are available at `review:SF-2026-ARXIV-2607-28666`; durable delta must be reconciled against current Books rather than appended as a paper summary.
<!-- delta:SF-2026-ARXIV-2607-28666:end -->

<!-- books-review:SF-2026-ARXIV-2607-28666:start -->
Decision=`Not Assessed`；不得在共享 Books 未取得日期有序写锁时把 queue 当作已集成。
<!-- books-review:SF-2026-ARXIV-2607-28666:end -->

<!-- existing:SF-2026-ARXIV-2607-28669:start -->
Canonical owner 已解析为 `TRAIN-LORA` / `books/part-04-training-system/30-lora.md`；目标与相邻章节的 proposition-level 对读由根任务按日期串行执行，作者侧不在并发期间推定结果。
<!-- existing:SF-2026-ARXIV-2607-28669:end -->

<!-- delta:SF-2026-ARXIV-2607-28669:start -->
Exact-v1 evidence and source-specific review are available at `review:SF-2026-ARXIV-2607-28669`; durable delta must be reconciled against current Books rather than appended as a paper summary.
<!-- delta:SF-2026-ARXIV-2607-28669:end -->

<!-- books-review:SF-2026-ARXIV-2607-28669:start -->
Decision=`Not Assessed`；不得在共享 Books 未取得日期有序写锁时把 queue 当作已集成。
<!-- books-review:SF-2026-ARXIV-2607-28669:end -->

<!-- existing:SF-2026-ARXIV-2607-28670:start -->
Canonical owner 已解析为 `MODEL-MOE` / `books/part-02-model/21-moe.md`；目标与相邻章节的 proposition-level 对读由根任务按日期串行执行，作者侧不在并发期间推定结果。
<!-- existing:SF-2026-ARXIV-2607-28670:end -->

<!-- delta:SF-2026-ARXIV-2607-28670:start -->
Exact-v1 evidence and source-specific review are available at `review:SF-2026-ARXIV-2607-28670`; durable delta must be reconciled against current Books rather than appended as a paper summary.
<!-- delta:SF-2026-ARXIV-2607-28670:end -->

<!-- books-review:SF-2026-ARXIV-2607-28670:start -->
Decision=`Not Assessed`；不得在共享 Books 未取得日期有序写锁时把 queue 当作已集成。
<!-- books-review:SF-2026-ARXIV-2607-28670:end -->

<!-- existing:SF-2026-ARXIV-2607-28678:start -->
Canonical owner 已解析为 `AGENT-MEMORY` / `books/part-07-agent/77-memory.md`；目标与相邻章节的 proposition-level 对读由根任务按日期串行执行，作者侧不在并发期间推定结果。
<!-- existing:SF-2026-ARXIV-2607-28678:end -->

<!-- delta:SF-2026-ARXIV-2607-28678:start -->
Exact-v1 evidence and source-specific review are available at `review:SF-2026-ARXIV-2607-28678`; durable delta must be reconciled against current Books rather than appended as a paper summary.
<!-- delta:SF-2026-ARXIV-2607-28678:end -->

<!-- books-review:SF-2026-ARXIV-2607-28678:start -->
Decision=`Not Assessed`；不得在共享 Books 未取得日期有序写锁时把 queue 当作已集成。
<!-- books-review:SF-2026-ARXIV-2607-28678:end -->

<!-- existing:SF-2026-ARXIV-2607-28684:start -->
Canonical owner 已解析为 `PLATFORM-EVALUATION-SYSTEM` / `books/part-06-ai-infrastructure/66-evaluation-system.md`；目标与相邻章节的 proposition-level 对读由根任务按日期串行执行，作者侧不在并发期间推定结果。
<!-- existing:SF-2026-ARXIV-2607-28684:end -->

<!-- delta:SF-2026-ARXIV-2607-28684:start -->
Exact-v1 evidence and source-specific review are available at `review:SF-2026-ARXIV-2607-28684`; durable delta must be reconciled against current Books rather than appended as a paper summary.
<!-- delta:SF-2026-ARXIV-2607-28684:end -->

<!-- books-review:SF-2026-ARXIV-2607-28684:start -->
Decision=`Not Assessed`；不得在共享 Books 未取得日期有序写锁时把 queue 当作已集成。
<!-- books-review:SF-2026-ARXIV-2607-28684:end -->

<!-- existing:SF-2026-ARXIV-2607-28685:start -->
Canonical owner 已解析为 `PLATFORM-EVALUATION-SYSTEM` / `books/part-06-ai-infrastructure/66-evaluation-system.md`；目标与相邻章节的 proposition-level 对读由根任务按日期串行执行，作者侧不在并发期间推定结果。
<!-- existing:SF-2026-ARXIV-2607-28685:end -->

<!-- delta:SF-2026-ARXIV-2607-28685:start -->
Exact-v1 evidence and source-specific review are available at `review:SF-2026-ARXIV-2607-28685`; durable delta must be reconciled against current Books rather than appended as a paper summary.
<!-- delta:SF-2026-ARXIV-2607-28685:end -->

<!-- books-review:SF-2026-ARXIV-2607-28685:start -->
Decision=`Not Assessed`；不得在共享 Books 未取得日期有序写锁时把 queue 当作已集成。
<!-- books-review:SF-2026-ARXIV-2607-28685:end -->

<!-- existing:SF-2026-ARXIV-2607-28692:start -->
Canonical owner 已解析为 `AGENT-TOOL-CALLING` / `books/part-07-agent/78-tool-calling.md`；目标与相邻章节的 proposition-level 对读由根任务按日期串行执行，作者侧不在并发期间推定结果。
<!-- existing:SF-2026-ARXIV-2607-28692:end -->

<!-- delta:SF-2026-ARXIV-2607-28692:start -->
Exact-v1 evidence and source-specific review are available at `review:SF-2026-ARXIV-2607-28692`; durable delta must be reconciled against current Books rather than appended as a paper summary.
<!-- delta:SF-2026-ARXIV-2607-28692:end -->

<!-- books-review:SF-2026-ARXIV-2607-28692:start -->
Decision=`Not Assessed`；不得在共享 Books 未取得日期有序写锁时把 queue 当作已集成。
<!-- books-review:SF-2026-ARXIV-2607-28692:end -->

<!-- existing:SF-2026-ARXIV-2607-28699:start -->
Canonical owner 已解析为 `INFER-KV-CACHE` / `books/part-05-inference-system/45-why-kv-cache-speeds-up.md`；目标与相邻章节的 proposition-level 对读由根任务按日期串行执行，作者侧不在并发期间推定结果。
<!-- existing:SF-2026-ARXIV-2607-28699:end -->

<!-- delta:SF-2026-ARXIV-2607-28699:start -->
Exact-v1 evidence and source-specific review are available at `review:SF-2026-ARXIV-2607-28699`; durable delta must be reconciled against current Books rather than appended as a paper summary.
<!-- delta:SF-2026-ARXIV-2607-28699:end -->

<!-- books-review:SF-2026-ARXIV-2607-28699:start -->
Decision=`Not Assessed`；不得在共享 Books 未取得日期有序写锁时把 queue 当作已集成。
<!-- books-review:SF-2026-ARXIV-2607-28699:end -->

<!-- existing:SF-2026-ARXIV-2607-28707:start -->
Canonical owner 已解析为 `PLATFORM-EVALUATION-SYSTEM` / `books/part-06-ai-infrastructure/66-evaluation-system.md`；目标与相邻章节的 proposition-level 对读由根任务按日期串行执行，作者侧不在并发期间推定结果。
<!-- existing:SF-2026-ARXIV-2607-28707:end -->

<!-- delta:SF-2026-ARXIV-2607-28707:start -->
Exact-v1 evidence and source-specific review are available at `review:SF-2026-ARXIV-2607-28707`; durable delta must be reconciled against current Books rather than appended as a paper summary.
<!-- delta:SF-2026-ARXIV-2607-28707:end -->

<!-- books-review:SF-2026-ARXIV-2607-28707:start -->
Decision=`Not Assessed`；不得在共享 Books 未取得日期有序写锁时把 queue 当作已集成。
<!-- books-review:SF-2026-ARXIV-2607-28707:end -->

<!-- existing:SF-2026-ARXIV-2607-28737:start -->
Canonical owner 已解析为 `MULTIMODAL-EMBODIED-VLA` / `books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md`；目标与相邻章节的 proposition-level 对读由根任务按日期串行执行，作者侧不在并发期间推定结果。
<!-- existing:SF-2026-ARXIV-2607-28737:end -->

<!-- delta:SF-2026-ARXIV-2607-28737:start -->
Exact-v1 evidence and source-specific review are available at `review:SF-2026-ARXIV-2607-28737`; durable delta must be reconciled against current Books rather than appended as a paper summary.
<!-- delta:SF-2026-ARXIV-2607-28737:end -->

<!-- books-review:SF-2026-ARXIV-2607-28737:start -->
Decision=`Not Assessed`；不得在共享 Books 未取得日期有序写锁时把 queue 当作已集成。
<!-- books-review:SF-2026-ARXIV-2607-28737:end -->

<!-- existing:SF-2026-ARXIV-2607-28777:start -->
Canonical owner 已解析为 `AGENT-PLATFORM` / `books/part-07-agent/84-agent-platform.md`；目标与相邻章节的 proposition-level 对读由根任务按日期串行执行，作者侧不在并发期间推定结果。
<!-- existing:SF-2026-ARXIV-2607-28777:end -->

<!-- delta:SF-2026-ARXIV-2607-28777:start -->
Exact-v1 evidence and source-specific review are available at `review:SF-2026-ARXIV-2607-28777`; durable delta must be reconciled against current Books rather than appended as a paper summary.
<!-- delta:SF-2026-ARXIV-2607-28777:end -->

<!-- books-review:SF-2026-ARXIV-2607-28777:start -->
Decision=`Not Assessed`；不得在共享 Books 未取得日期有序写锁时把 queue 当作已集成。
<!-- books-review:SF-2026-ARXIV-2607-28777:end -->

<!-- existing:SF-2026-ARXIV-2607-28788:start -->
Canonical owner 已解析为 `PLATFORM-EVALUATION-SYSTEM` / `books/part-06-ai-infrastructure/66-evaluation-system.md`；目标与相邻章节的 proposition-level 对读由根任务按日期串行执行，作者侧不在并发期间推定结果。
<!-- existing:SF-2026-ARXIV-2607-28788:end -->

<!-- delta:SF-2026-ARXIV-2607-28788:start -->
Exact-v1 evidence and source-specific review are available at `review:SF-2026-ARXIV-2607-28788`; durable delta must be reconciled against current Books rather than appended as a paper summary.
<!-- delta:SF-2026-ARXIV-2607-28788:end -->

<!-- books-review:SF-2026-ARXIV-2607-28788:start -->
Decision=`Not Assessed`；不得在共享 Books 未取得日期有序写锁时把 queue 当作已集成。
<!-- books-review:SF-2026-ARXIV-2607-28788:end -->

<!-- existing:SF-2026-ARXIV-2607-28801:start -->
Canonical owner 已解析为 `PLATFORM-EVALUATION-SYSTEM` / `books/part-06-ai-infrastructure/66-evaluation-system.md`；目标与相邻章节的 proposition-level 对读由根任务按日期串行执行，作者侧不在并发期间推定结果。
<!-- existing:SF-2026-ARXIV-2607-28801:end -->

<!-- delta:SF-2026-ARXIV-2607-28801:start -->
Exact-v1 evidence and source-specific review are available at `review:SF-2026-ARXIV-2607-28801`; durable delta must be reconciled against current Books rather than appended as a paper summary.
<!-- delta:SF-2026-ARXIV-2607-28801:end -->

<!-- books-review:SF-2026-ARXIV-2607-28801:start -->
Decision=`Not Assessed`；不得在共享 Books 未取得日期有序写锁时把 queue 当作已集成。
<!-- books-review:SF-2026-ARXIV-2607-28801:end -->

<!-- existing:SF-2026-ARXIV-2607-28802:start -->
Canonical owner 已解析为 `PLATFORM-EVALUATION-SYSTEM` / `books/part-06-ai-infrastructure/66-evaluation-system.md`；目标与相邻章节的 proposition-level 对读由根任务按日期串行执行，作者侧不在并发期间推定结果。
<!-- existing:SF-2026-ARXIV-2607-28802:end -->

<!-- delta:SF-2026-ARXIV-2607-28802:start -->
Exact-v1 evidence and source-specific review are available at `review:SF-2026-ARXIV-2607-28802`; durable delta must be reconciled against current Books rather than appended as a paper summary.
<!-- delta:SF-2026-ARXIV-2607-28802:end -->

<!-- books-review:SF-2026-ARXIV-2607-28802:start -->
Decision=`Not Assessed`；不得在共享 Books 未取得日期有序写锁时把 queue 当作已集成。
<!-- books-review:SF-2026-ARXIV-2607-28802:end -->

<!-- existing:SF-2026-ARXIV-2607-28815:start -->
Canonical owner 已解析为 `AGENT-WORKFLOW` / `books/part-07-agent/81-workflow.md`；目标与相邻章节的 proposition-level 对读由根任务按日期串行执行，作者侧不在并发期间推定结果。
<!-- existing:SF-2026-ARXIV-2607-28815:end -->

<!-- delta:SF-2026-ARXIV-2607-28815:start -->
Exact-v1 evidence and source-specific review are available at `review:SF-2026-ARXIV-2607-28815`; durable delta must be reconciled against current Books rather than appended as a paper summary.
<!-- delta:SF-2026-ARXIV-2607-28815:end -->

<!-- books-review:SF-2026-ARXIV-2607-28815:start -->
Decision=`Not Assessed`；不得在共享 Books 未取得日期有序写锁时把 queue 当作已集成。
<!-- books-review:SF-2026-ARXIV-2607-28815:end -->

<!-- existing:SF-2026-ARXIV-2607-28818:start -->
Canonical owner 已解析为 `PLATFORM-EVALUATION-SYSTEM` / `books/part-06-ai-infrastructure/66-evaluation-system.md`；目标与相邻章节的 proposition-level 对读由根任务按日期串行执行，作者侧不在并发期间推定结果。
<!-- existing:SF-2026-ARXIV-2607-28818:end -->

<!-- delta:SF-2026-ARXIV-2607-28818:start -->
Exact-v1 evidence and source-specific review are available at `review:SF-2026-ARXIV-2607-28818`; durable delta must be reconciled against current Books rather than appended as a paper summary.
<!-- delta:SF-2026-ARXIV-2607-28818:end -->

<!-- books-review:SF-2026-ARXIV-2607-28818:start -->
Decision=`Not Assessed`；不得在共享 Books 未取得日期有序写锁时把 queue 当作已集成。
<!-- books-review:SF-2026-ARXIV-2607-28818:end -->

<!-- existing:SF-2026-ARXIV-2607-28824:start -->
Canonical owner 已解析为 `INFER-GPU-MEMORY` / `books/part-05-inference-system/54-gpu-memory.md`；目标与相邻章节的 proposition-level 对读由根任务按日期串行执行，作者侧不在并发期间推定结果。
<!-- existing:SF-2026-ARXIV-2607-28824:end -->

<!-- delta:SF-2026-ARXIV-2607-28824:start -->
Exact-v1 evidence and source-specific review are available at `review:SF-2026-ARXIV-2607-28824`; durable delta must be reconciled against current Books rather than appended as a paper summary.
<!-- delta:SF-2026-ARXIV-2607-28824:end -->

<!-- books-review:SF-2026-ARXIV-2607-28824:start -->
Decision=`Not Assessed`；不得在共享 Books 未取得日期有序写锁时把 queue 当作已集成。
<!-- books-review:SF-2026-ARXIV-2607-28824:end -->

<!-- existing:SF-2026-ARXIV-2607-28829:start -->
Canonical owner 已解析为 `PLATFORM-SECURITY` / `books/part-06-ai-infrastructure/72-security.md`；目标与相邻章节的 proposition-level 对读由根任务按日期串行执行，作者侧不在并发期间推定结果。
<!-- existing:SF-2026-ARXIV-2607-28829:end -->

<!-- delta:SF-2026-ARXIV-2607-28829:start -->
Exact-v1 evidence and source-specific review are available at `review:SF-2026-ARXIV-2607-28829`; durable delta must be reconciled against current Books rather than appended as a paper summary.
<!-- delta:SF-2026-ARXIV-2607-28829:end -->

<!-- books-review:SF-2026-ARXIV-2607-28829:start -->
Decision=`Not Assessed`；不得在共享 Books 未取得日期有序写锁时把 queue 当作已集成。
<!-- books-review:SF-2026-ARXIV-2607-28829:end -->

<!-- existing:SF-2026-ARXIV-2607-28848:start -->
Canonical owner 已解析为 `INFER-SCHEDULING` / `books/part-05-inference-system/56-inference-scheduling.md`；目标与相邻章节的 proposition-level 对读由根任务按日期串行执行，作者侧不在并发期间推定结果。
<!-- existing:SF-2026-ARXIV-2607-28848:end -->

<!-- delta:SF-2026-ARXIV-2607-28848:start -->
Exact-v1 evidence and source-specific review are available at `review:SF-2026-ARXIV-2607-28848`; durable delta must be reconciled against current Books rather than appended as a paper summary.
<!-- delta:SF-2026-ARXIV-2607-28848:end -->

<!-- books-review:SF-2026-ARXIV-2607-28848:start -->
Decision=`Not Assessed`；不得在共享 Books 未取得日期有序写锁时把 queue 当作已集成。
<!-- books-review:SF-2026-ARXIV-2607-28848:end -->

<!-- existing:SF-2026-ARXIV-2607-28871:start -->
Canonical owner 已解析为 `PLATFORM-EVALUATION-SYSTEM` / `books/part-06-ai-infrastructure/66-evaluation-system.md`；目标与相邻章节的 proposition-level 对读由根任务按日期串行执行，作者侧不在并发期间推定结果。
<!-- existing:SF-2026-ARXIV-2607-28871:end -->

<!-- delta:SF-2026-ARXIV-2607-28871:start -->
Exact-v1 evidence and source-specific review are available at `review:SF-2026-ARXIV-2607-28871`; durable delta must be reconciled against current Books rather than appended as a paper summary.
<!-- delta:SF-2026-ARXIV-2607-28871:end -->

<!-- books-review:SF-2026-ARXIV-2607-28871:start -->
Decision=`Not Assessed`；不得在共享 Books 未取得日期有序写锁时把 queue 当作已集成。
<!-- books-review:SF-2026-ARXIV-2607-28871:end -->

<!-- existing:SF-2026-ARXIV-2607-28884:start -->
Canonical owner 已解析为 `PLATFORM-SECURITY` / `books/part-06-ai-infrastructure/72-security.md`；目标与相邻章节的 proposition-level 对读由根任务按日期串行执行，作者侧不在并发期间推定结果。
<!-- existing:SF-2026-ARXIV-2607-28884:end -->

<!-- delta:SF-2026-ARXIV-2607-28884:start -->
Exact-v1 evidence and source-specific review are available at `review:SF-2026-ARXIV-2607-28884`; durable delta must be reconciled against current Books rather than appended as a paper summary.
<!-- delta:SF-2026-ARXIV-2607-28884:end -->

<!-- books-review:SF-2026-ARXIV-2607-28884:start -->
Decision=`Not Assessed`；不得在共享 Books 未取得日期有序写锁时把 queue 当作已集成。
<!-- books-review:SF-2026-ARXIV-2607-28884:end -->

<!-- existing:SF-2026-ARXIV-2607-28887:start -->
Canonical owner 已解析为 `AGENT-WORKFLOW` / `books/part-07-agent/81-workflow.md`；目标与相邻章节的 proposition-level 对读由根任务按日期串行执行，作者侧不在并发期间推定结果。
<!-- existing:SF-2026-ARXIV-2607-28887:end -->

<!-- delta:SF-2026-ARXIV-2607-28887:start -->
Exact-v1 evidence and source-specific review are available at `review:SF-2026-ARXIV-2607-28887`; durable delta must be reconciled against current Books rather than appended as a paper summary.
<!-- delta:SF-2026-ARXIV-2607-28887:end -->

<!-- books-review:SF-2026-ARXIV-2607-28887:start -->
Decision=`Not Assessed`；不得在共享 Books 未取得日期有序写锁时把 queue 当作已集成。
<!-- books-review:SF-2026-ARXIV-2607-28887:end -->

<!-- existing:SF-2026-ARXIV-2607-28896:start -->
Canonical owner 已解析为 `PLATFORM-EVALUATION-SYSTEM` / `books/part-06-ai-infrastructure/66-evaluation-system.md`；目标与相邻章节的 proposition-level 对读由根任务按日期串行执行，作者侧不在并发期间推定结果。
<!-- existing:SF-2026-ARXIV-2607-28896:end -->

<!-- delta:SF-2026-ARXIV-2607-28896:start -->
Exact-v1 evidence and source-specific review are available at `review:SF-2026-ARXIV-2607-28896`; durable delta must be reconciled against current Books rather than appended as a paper summary.
<!-- delta:SF-2026-ARXIV-2607-28896:end -->

<!-- books-review:SF-2026-ARXIV-2607-28896:start -->
Decision=`Not Assessed`；不得在共享 Books 未取得日期有序写锁时把 queue 当作已集成。
<!-- books-review:SF-2026-ARXIV-2607-28896:end -->

<!-- existing:SF-2026-ARXIV-2607-28908:start -->
Canonical owner 已解析为 `AGENT-REFLECTION` / `books/part-07-agent/80-reflection.md`；目标与相邻章节的 proposition-level 对读由根任务按日期串行执行，作者侧不在并发期间推定结果。
<!-- existing:SF-2026-ARXIV-2607-28908:end -->

<!-- delta:SF-2026-ARXIV-2607-28908:start -->
Exact-v1 evidence and source-specific review are available at `review:SF-2026-ARXIV-2607-28908`; durable delta must be reconciled against current Books rather than appended as a paper summary.
<!-- delta:SF-2026-ARXIV-2607-28908:end -->

<!-- books-review:SF-2026-ARXIV-2607-28908:start -->
Decision=`Not Assessed`；不得在共享 Books 未取得日期有序写锁时把 queue 当作已集成。
<!-- books-review:SF-2026-ARXIV-2607-28908:end -->

<!-- existing:SF-2026-ARXIV-2607-28928:start -->
Canonical owner 已解析为 `AGENT-WORKFLOW` / `books/part-07-agent/81-workflow.md`；目标与相邻章节的 proposition-level 对读由根任务按日期串行执行，作者侧不在并发期间推定结果。
<!-- existing:SF-2026-ARXIV-2607-28928:end -->

<!-- delta:SF-2026-ARXIV-2607-28928:start -->
Exact-v1 evidence and source-specific review are available at `review:SF-2026-ARXIV-2607-28928`; durable delta must be reconciled against current Books rather than appended as a paper summary.
<!-- delta:SF-2026-ARXIV-2607-28928:end -->

<!-- books-review:SF-2026-ARXIV-2607-28928:start -->
Decision=`Not Assessed`；不得在共享 Books 未取得日期有序写锁时把 queue 当作已集成。
<!-- books-review:SF-2026-ARXIV-2607-28928:end -->

<!-- existing:SF-2026-ARXIV-2607-28940:start -->
Canonical owner 已解析为 `INFER-REQUEST-LIFECYCLE` / `books/part-05-inference-system/42-what-happens-during-inference.md`；目标与相邻章节的 proposition-level 对读由根任务按日期串行执行，作者侧不在并发期间推定结果。
<!-- existing:SF-2026-ARXIV-2607-28940:end -->

<!-- delta:SF-2026-ARXIV-2607-28940:start -->
Exact-v1 evidence and source-specific review are available at `review:SF-2026-ARXIV-2607-28940`; durable delta must be reconciled against current Books rather than appended as a paper summary.
<!-- delta:SF-2026-ARXIV-2607-28940:end -->

<!-- books-review:SF-2026-ARXIV-2607-28940:start -->
Decision=`Not Assessed`；不得在共享 Books 未取得日期有序写锁时把 queue 当作已集成。
<!-- books-review:SF-2026-ARXIV-2607-28940:end -->

<!-- existing:SF-2026-ARXIV-2607-28942:start -->
Canonical owner 已解析为 `AGENT-PLANNING` / `books/part-07-agent/79-planning.md`；目标与相邻章节的 proposition-level 对读由根任务按日期串行执行，作者侧不在并发期间推定结果。
<!-- existing:SF-2026-ARXIV-2607-28942:end -->

<!-- delta:SF-2026-ARXIV-2607-28942:start -->
Exact-v1 evidence and source-specific review are available at `review:SF-2026-ARXIV-2607-28942`; durable delta must be reconciled against current Books rather than appended as a paper summary.
<!-- delta:SF-2026-ARXIV-2607-28942:end -->

<!-- books-review:SF-2026-ARXIV-2607-28942:start -->
Decision=`Not Assessed`；不得在共享 Books 未取得日期有序写锁时把 queue 当作已集成。
<!-- books-review:SF-2026-ARXIV-2607-28942:end -->

<!-- existing:SF-2026-ARXIV-2607-28966:start -->
Canonical owner 已解析为 `INFER-SCHEDULING` / `books/part-05-inference-system/56-inference-scheduling.md`；目标与相邻章节的 proposition-level 对读由根任务按日期串行执行，作者侧不在并发期间推定结果。
<!-- existing:SF-2026-ARXIV-2607-28966:end -->

<!-- delta:SF-2026-ARXIV-2607-28966:start -->
Exact-v1 evidence and source-specific review are available at `review:SF-2026-ARXIV-2607-28966`; durable delta must be reconciled against current Books rather than appended as a paper summary.
<!-- delta:SF-2026-ARXIV-2607-28966:end -->

<!-- books-review:SF-2026-ARXIV-2607-28966:start -->
Decision=`Not Assessed`；不得在共享 Books 未取得日期有序写锁时把 queue 当作已集成。
<!-- books-review:SF-2026-ARXIV-2607-28966:end -->

<!-- existing:SF-2026-ARXIV-2607-28979:start -->
Canonical owner 已解析为 `INFER-KV-CACHE` / `books/part-05-inference-system/45-why-kv-cache-speeds-up.md`；目标与相邻章节的 proposition-level 对读由根任务按日期串行执行，作者侧不在并发期间推定结果。
<!-- existing:SF-2026-ARXIV-2607-28979:end -->

<!-- delta:SF-2026-ARXIV-2607-28979:start -->
Exact-v1 evidence and source-specific review are available at `review:SF-2026-ARXIV-2607-28979`; durable delta must be reconciled against current Books rather than appended as a paper summary.
<!-- delta:SF-2026-ARXIV-2607-28979:end -->

<!-- books-review:SF-2026-ARXIV-2607-28979:start -->
Decision=`Not Assessed`；不得在共享 Books 未取得日期有序写锁时把 queue 当作已集成。
<!-- books-review:SF-2026-ARXIV-2607-28979:end -->

<!-- existing:SF-2026-ARXIV-2607-28990:start -->
Canonical owner 已解析为 `TRAIN-GRPO` / `books/part-04-training-system/33-grpo.md`；目标与相邻章节的 proposition-level 对读由根任务按日期串行执行，作者侧不在并发期间推定结果。
<!-- existing:SF-2026-ARXIV-2607-28990:end -->

<!-- delta:SF-2026-ARXIV-2607-28990:start -->
Exact-v1 evidence and source-specific review are available at `review:SF-2026-ARXIV-2607-28990`; durable delta must be reconciled against current Books rather than appended as a paper summary.
<!-- delta:SF-2026-ARXIV-2607-28990:end -->

<!-- books-review:SF-2026-ARXIV-2607-28990:start -->
Decision=`Not Assessed`；不得在共享 Books 未取得日期有序写锁时把 queue 当作已集成。
<!-- books-review:SF-2026-ARXIV-2607-28990:end -->

<!-- existing:SF-2026-ARXIV-2607-28991:start -->
Canonical owner 已解析为 `MULTIMODAL-REPRESENTATION` / `books/part-03-multimodal-world-models/23-multimodal-representation.md`；目标与相邻章节的 proposition-level 对读由根任务按日期串行执行，作者侧不在并发期间推定结果。
<!-- existing:SF-2026-ARXIV-2607-28991:end -->

<!-- delta:SF-2026-ARXIV-2607-28991:start -->
Exact-v1 evidence and source-specific review are available at `review:SF-2026-ARXIV-2607-28991`; durable delta must be reconciled against current Books rather than appended as a paper summary.
<!-- delta:SF-2026-ARXIV-2607-28991:end -->

<!-- books-review:SF-2026-ARXIV-2607-28991:start -->
Decision=`Not Assessed`；不得在共享 Books 未取得日期有序写锁时把 queue 当作已集成。
<!-- books-review:SF-2026-ARXIV-2607-28991:end -->

<!-- existing:SF-2026-ARXIV-2607-28993:start -->
Canonical owner 已解析为 `MULTIMODAL-WORLD-MODELS` / `books/part-03-multimodal-world-models/25-multimodal-world-models.md`；目标与相邻章节的 proposition-level 对读由根任务按日期串行执行，作者侧不在并发期间推定结果。
<!-- existing:SF-2026-ARXIV-2607-28993:end -->

<!-- delta:SF-2026-ARXIV-2607-28993:start -->
Exact-v1 evidence and source-specific review are available at `review:SF-2026-ARXIV-2607-28993`; durable delta must be reconciled against current Books rather than appended as a paper summary.
<!-- delta:SF-2026-ARXIV-2607-28993:end -->

<!-- books-review:SF-2026-ARXIV-2607-28993:start -->
Decision=`Not Assessed`；不得在共享 Books 未取得日期有序写锁时把 queue 当作已集成。
<!-- books-review:SF-2026-ARXIV-2607-28993:end -->

<!-- existing:SF-2026-ARXIV-2607-29032:start -->
Canonical owner 已解析为 `AGENT-MEMORY` / `books/part-07-agent/77-memory.md`；目标与相邻章节的 proposition-level 对读由根任务按日期串行执行，作者侧不在并发期间推定结果。
<!-- existing:SF-2026-ARXIV-2607-29032:end -->

<!-- delta:SF-2026-ARXIV-2607-29032:start -->
Exact-v1 evidence and source-specific review are available at `review:SF-2026-ARXIV-2607-29032`; durable delta must be reconciled against current Books rather than appended as a paper summary.
<!-- delta:SF-2026-ARXIV-2607-29032:end -->

<!-- books-review:SF-2026-ARXIV-2607-29032:start -->
Decision=`Not Assessed`；不得在共享 Books 未取得日期有序写锁时把 queue 当作已集成。
<!-- books-review:SF-2026-ARXIV-2607-29032:end -->

<!-- existing:SF-2026-ARXIV-2607-29053:start -->
Canonical owner 已解析为 `PLATFORM-EVALUATION-SYSTEM` / `books/part-06-ai-infrastructure/66-evaluation-system.md`；目标与相邻章节的 proposition-level 对读由根任务按日期串行执行，作者侧不在并发期间推定结果。
<!-- existing:SF-2026-ARXIV-2607-29053:end -->

<!-- delta:SF-2026-ARXIV-2607-29053:start -->
Exact-v1 evidence and source-specific review are available at `review:SF-2026-ARXIV-2607-29053`; durable delta must be reconciled against current Books rather than appended as a paper summary.
<!-- delta:SF-2026-ARXIV-2607-29053:end -->

<!-- books-review:SF-2026-ARXIV-2607-29053:start -->
Decision=`Not Assessed`；不得在共享 Books 未取得日期有序写锁时把 queue 当作已集成。
<!-- books-review:SF-2026-ARXIV-2607-29053:end -->

<!-- existing:SF-2026-ARXIV-2607-29065:start -->
Canonical owner 已解析为 `MODEL-TOKENIZER` / `books/part-02-model/11-tokenizer.md`；目标与相邻章节的 proposition-level 对读由根任务按日期串行执行，作者侧不在并发期间推定结果。
<!-- existing:SF-2026-ARXIV-2607-29065:end -->

<!-- delta:SF-2026-ARXIV-2607-29065:start -->
Exact-v1 evidence and source-specific review are available at `review:SF-2026-ARXIV-2607-29065`; durable delta must be reconciled against current Books rather than appended as a paper summary.
<!-- delta:SF-2026-ARXIV-2607-29065:end -->

<!-- books-review:SF-2026-ARXIV-2607-29065:start -->
Decision=`Not Assessed`；不得在共享 Books 未取得日期有序写锁时把 queue 当作已集成。
<!-- books-review:SF-2026-ARXIV-2607-29065:end -->

<!-- existing:SF-2026-ARXIV-2607-29069:start -->
Canonical owner 已解析为 `AGENT-PLATFORM` / `books/part-07-agent/84-agent-platform.md`；目标与相邻章节的 proposition-level 对读由根任务按日期串行执行，作者侧不在并发期间推定结果。
<!-- existing:SF-2026-ARXIV-2607-29069:end -->

<!-- delta:SF-2026-ARXIV-2607-29069:start -->
Exact-v1 evidence and source-specific review are available at `review:SF-2026-ARXIV-2607-29069`; durable delta must be reconciled against current Books rather than appended as a paper summary.
<!-- delta:SF-2026-ARXIV-2607-29069:end -->

<!-- books-review:SF-2026-ARXIV-2607-29069:start -->
Decision=`Not Assessed`；不得在共享 Books 未取得日期有序写锁时把 queue 当作已集成。
<!-- books-review:SF-2026-ARXIV-2607-29069:end -->

<!-- existing:SF-2026-ARXIV-2607-29071:start -->
Canonical owner 已解析为 `TRAIN-DISTRIBUTED-TRAINING` / `books/part-04-training-system/36-distributed-training.md`；目标与相邻章节的 proposition-level 对读由根任务按日期串行执行，作者侧不在并发期间推定结果。
<!-- existing:SF-2026-ARXIV-2607-29071:end -->

<!-- delta:SF-2026-ARXIV-2607-29071:start -->
Exact-v1 evidence and source-specific review are available at `review:SF-2026-ARXIV-2607-29071`; durable delta must be reconciled against current Books rather than appended as a paper summary.
<!-- delta:SF-2026-ARXIV-2607-29071:end -->

<!-- books-review:SF-2026-ARXIV-2607-29071:start -->
Decision=`Not Assessed`；不得在共享 Books 未取得日期有序写锁时把 queue 当作已集成。
<!-- books-review:SF-2026-ARXIV-2607-29071:end -->

<!-- existing:SF-2026-ARXIV-2607-29076:start -->
Canonical owner 已解析为 `INFER-KV-CACHE` / `books/part-05-inference-system/45-why-kv-cache-speeds-up.md`；目标与相邻章节的 proposition-level 对读由根任务按日期串行执行，作者侧不在并发期间推定结果。
<!-- existing:SF-2026-ARXIV-2607-29076:end -->

<!-- delta:SF-2026-ARXIV-2607-29076:start -->
Exact-v1 evidence and source-specific review are available at `review:SF-2026-ARXIV-2607-29076`; durable delta must be reconciled against current Books rather than appended as a paper summary.
<!-- delta:SF-2026-ARXIV-2607-29076:end -->

<!-- books-review:SF-2026-ARXIV-2607-29076:start -->
Decision=`Not Assessed`；不得在共享 Books 未取得日期有序写锁时把 queue 当作已集成。
<!-- books-review:SF-2026-ARXIV-2607-29076:end -->

<!-- existing:SF-2026-ARXIV-2607-29078:start -->
Canonical owner 已解析为 `TRAIN-GRPO` / `books/part-04-training-system/33-grpo.md`；目标与相邻章节的 proposition-level 对读由根任务按日期串行执行，作者侧不在并发期间推定结果。
<!-- existing:SF-2026-ARXIV-2607-29078:end -->

<!-- delta:SF-2026-ARXIV-2607-29078:start -->
Exact-v1 evidence and source-specific review are available at `review:SF-2026-ARXIV-2607-29078`; durable delta must be reconciled against current Books rather than appended as a paper summary.
<!-- delta:SF-2026-ARXIV-2607-29078:end -->

<!-- books-review:SF-2026-ARXIV-2607-29078:start -->
Decision=`Not Assessed`；不得在共享 Books 未取得日期有序写锁时把 queue 当作已集成。
<!-- books-review:SF-2026-ARXIV-2607-29078:end -->

<!-- existing:SF-2026-ARXIV-2607-29079:start -->
Canonical owner 已解析为 `MULTIMODAL-GENERATIVE-PARADIGMS` / `books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md`；目标与相邻章节的 proposition-level 对读由根任务按日期串行执行，作者侧不在并发期间推定结果。
<!-- existing:SF-2026-ARXIV-2607-29079:end -->

<!-- delta:SF-2026-ARXIV-2607-29079:start -->
Exact-v1 evidence and source-specific review are available at `review:SF-2026-ARXIV-2607-29079`; durable delta must be reconciled against current Books rather than appended as a paper summary.
<!-- delta:SF-2026-ARXIV-2607-29079:end -->

<!-- books-review:SF-2026-ARXIV-2607-29079:start -->
Decision=`Not Assessed`；不得在共享 Books 未取得日期有序写锁时把 queue 当作已集成。
<!-- books-review:SF-2026-ARXIV-2607-29079:end -->

<!-- existing:SF-2026-ARXIV-2607-29104:start -->
Canonical owner 已解析为 `AGENT-MEMORY` / `books/part-07-agent/77-memory.md`；目标与相邻章节的 proposition-level 对读由根任务按日期串行执行，作者侧不在并发期间推定结果。
<!-- existing:SF-2026-ARXIV-2607-29104:end -->

<!-- delta:SF-2026-ARXIV-2607-29104:start -->
Exact-v1 evidence and source-specific review are available at `review:SF-2026-ARXIV-2607-29104`; durable delta must be reconciled against current Books rather than appended as a paper summary.
<!-- delta:SF-2026-ARXIV-2607-29104:end -->

<!-- books-review:SF-2026-ARXIV-2607-29104:start -->
Decision=`Not Assessed`；不得在共享 Books 未取得日期有序写锁时把 queue 当作已集成。
<!-- books-review:SF-2026-ARXIV-2607-29104:end -->

<!-- existing:SF-2026-ARXIV-2607-29120:start -->
Canonical owner 已解析为 `TRAIN-DATA` / `books/part-04-training-system/27-data.md`；目标与相邻章节的 proposition-level 对读由根任务按日期串行执行，作者侧不在并发期间推定结果。
<!-- existing:SF-2026-ARXIV-2607-29120:end -->

<!-- delta:SF-2026-ARXIV-2607-29120:start -->
Exact-v1 evidence and source-specific review are available at `review:SF-2026-ARXIV-2607-29120`; durable delta must be reconciled against current Books rather than appended as a paper summary.
<!-- delta:SF-2026-ARXIV-2607-29120:end -->

<!-- books-review:SF-2026-ARXIV-2607-29120:start -->
Decision=`Not Assessed`；不得在共享 Books 未取得日期有序写锁时把 queue 当作已集成。
<!-- books-review:SF-2026-ARXIV-2607-29120:end -->

<!-- existing:SF-2026-ARXIV-2607-29125:start -->
Canonical owner 已解析为 `PLATFORM-EVALUATION-SYSTEM` / `books/part-06-ai-infrastructure/66-evaluation-system.md`；目标与相邻章节的 proposition-level 对读由根任务按日期串行执行，作者侧不在并发期间推定结果。
<!-- existing:SF-2026-ARXIV-2607-29125:end -->

<!-- delta:SF-2026-ARXIV-2607-29125:start -->
Exact-v1 evidence and source-specific review are available at `review:SF-2026-ARXIV-2607-29125`; durable delta must be reconciled against current Books rather than appended as a paper summary.
<!-- delta:SF-2026-ARXIV-2607-29125:end -->

<!-- books-review:SF-2026-ARXIV-2607-29125:start -->
Decision=`Not Assessed`；不得在共享 Books 未取得日期有序写锁时把 queue 当作已集成。
<!-- books-review:SF-2026-ARXIV-2607-29125:end -->

<!-- existing:SF-2026-ARXIV-2607-29167:start -->
Canonical owner 已解析为 `AGENT-MEMORY` / `books/part-07-agent/77-memory.md`；目标与相邻章节的 proposition-level 对读由根任务按日期串行执行，作者侧不在并发期间推定结果。
<!-- existing:SF-2026-ARXIV-2607-29167:end -->

<!-- delta:SF-2026-ARXIV-2607-29167:start -->
Exact-v1 evidence and source-specific review are available at `review:SF-2026-ARXIV-2607-29167`; durable delta must be reconciled against current Books rather than appended as a paper summary.
<!-- delta:SF-2026-ARXIV-2607-29167:end -->

<!-- books-review:SF-2026-ARXIV-2607-29167:start -->
Decision=`Not Assessed`；不得在共享 Books 未取得日期有序写锁时把 queue 当作已集成。
<!-- books-review:SF-2026-ARXIV-2607-29167:end -->

<!-- existing:SF-2026-ARXIV-2607-29169:start -->
Canonical owner 已解析为 `MULTIMODAL-EMBODIED-VLA` / `books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md`；目标与相邻章节的 proposition-level 对读由根任务按日期串行执行，作者侧不在并发期间推定结果。
<!-- existing:SF-2026-ARXIV-2607-29169:end -->

<!-- delta:SF-2026-ARXIV-2607-29169:start -->
Exact-v1 evidence and source-specific review are available at `review:SF-2026-ARXIV-2607-29169`; durable delta must be reconciled against current Books rather than appended as a paper summary.
<!-- delta:SF-2026-ARXIV-2607-29169:end -->

<!-- books-review:SF-2026-ARXIV-2607-29169:start -->
Decision=`Not Assessed`；不得在共享 Books 未取得日期有序写锁时把 queue 当作已集成。
<!-- books-review:SF-2026-ARXIV-2607-29169:end -->

<!-- existing:SF-2026-ARXIV-2607-29172:start -->
Canonical owner 已解析为 `TRAIN-SFT` / `books/part-04-training-system/29-sft.md`；目标与相邻章节的 proposition-level 对读由根任务按日期串行执行，作者侧不在并发期间推定结果。
<!-- existing:SF-2026-ARXIV-2607-29172:end -->

<!-- delta:SF-2026-ARXIV-2607-29172:start -->
Exact-v1 evidence and source-specific review are available at `review:SF-2026-ARXIV-2607-29172`; durable delta must be reconciled against current Books rather than appended as a paper summary.
<!-- delta:SF-2026-ARXIV-2607-29172:end -->

<!-- books-review:SF-2026-ARXIV-2607-29172:start -->
Decision=`Not Assessed`；不得在共享 Books 未取得日期有序写锁时把 queue 当作已集成。
<!-- books-review:SF-2026-ARXIV-2607-29172:end -->

<!-- existing:SF-2026-ARXIV-2607-29175:start -->
Canonical owner 已解析为 `AGENT-TOOL-CALLING` / `books/part-07-agent/78-tool-calling.md`；目标与相邻章节的 proposition-level 对读由根任务按日期串行执行，作者侧不在并发期间推定结果。
<!-- existing:SF-2026-ARXIV-2607-29175:end -->

<!-- delta:SF-2026-ARXIV-2607-29175:start -->
Exact-v1 evidence and source-specific review are available at `review:SF-2026-ARXIV-2607-29175`; durable delta must be reconciled against current Books rather than appended as a paper summary.
<!-- delta:SF-2026-ARXIV-2607-29175:end -->

<!-- books-review:SF-2026-ARXIV-2607-29175:start -->
Decision=`Not Assessed`；不得在共享 Books 未取得日期有序写锁时把 queue 当作已集成。
<!-- books-review:SF-2026-ARXIV-2607-29175:end -->

<!-- existing:SF-2026-ARXIV-2607-29185:start -->
Canonical owner 已解析为 `TRAIN-RLHF` / `books/part-04-training-system/31-rlhf.md`；目标与相邻章节的 proposition-level 对读由根任务按日期串行执行，作者侧不在并发期间推定结果。
<!-- existing:SF-2026-ARXIV-2607-29185:end -->

<!-- delta:SF-2026-ARXIV-2607-29185:start -->
Exact-v1 evidence and source-specific review are available at `review:SF-2026-ARXIV-2607-29185`; durable delta must be reconciled against current Books rather than appended as a paper summary.
<!-- delta:SF-2026-ARXIV-2607-29185:end -->

<!-- books-review:SF-2026-ARXIV-2607-29185:start -->
Decision=`Not Assessed`；不得在共享 Books 未取得日期有序写锁时把 queue 当作已集成。
<!-- books-review:SF-2026-ARXIV-2607-29185:end -->

<!-- existing:SF-2026-ARXIV-2607-29190:start -->
Canonical owner 已解析为 `AGENT-TOOL-CALLING` / `books/part-07-agent/78-tool-calling.md`；目标与相邻章节的 proposition-level 对读由根任务按日期串行执行，作者侧不在并发期间推定结果。
<!-- existing:SF-2026-ARXIV-2607-29190:end -->

<!-- delta:SF-2026-ARXIV-2607-29190:start -->
Exact-v1 evidence and source-specific review are available at `review:SF-2026-ARXIV-2607-29190`; durable delta must be reconciled against current Books rather than appended as a paper summary.
<!-- delta:SF-2026-ARXIV-2607-29190:end -->

<!-- books-review:SF-2026-ARXIV-2607-29190:start -->
Decision=`Not Assessed`；不得在共享 Books 未取得日期有序写锁时把 queue 当作已集成。
<!-- books-review:SF-2026-ARXIV-2607-29190:end -->

<!-- existing:SF-2026-ARXIV-2607-29199:start -->
Canonical owner 已解析为 `PLATFORM-EVALUATION-SYSTEM` / `books/part-06-ai-infrastructure/66-evaluation-system.md`；目标与相邻章节的 proposition-level 对读由根任务按日期串行执行，作者侧不在并发期间推定结果。
<!-- existing:SF-2026-ARXIV-2607-29199:end -->

<!-- delta:SF-2026-ARXIV-2607-29199:start -->
Exact-v1 evidence and source-specific review are available at `review:SF-2026-ARXIV-2607-29199`; durable delta must be reconciled against current Books rather than appended as a paper summary.
<!-- delta:SF-2026-ARXIV-2607-29199:end -->

<!-- books-review:SF-2026-ARXIV-2607-29199:start -->
Decision=`Not Assessed`；不得在共享 Books 未取得日期有序写锁时把 queue 当作已集成。
<!-- books-review:SF-2026-ARXIV-2607-29199:end -->

<!-- existing:SF-2026-ARXIV-2607-29209:start -->
Canonical owner 已解析为 `TRAIN-GRPO` / `books/part-04-training-system/33-grpo.md`；目标与相邻章节的 proposition-level 对读由根任务按日期串行执行，作者侧不在并发期间推定结果。
<!-- existing:SF-2026-ARXIV-2607-29209:end -->

<!-- delta:SF-2026-ARXIV-2607-29209:start -->
Exact-v1 evidence and source-specific review are available at `review:SF-2026-ARXIV-2607-29209`; durable delta must be reconciled against current Books rather than appended as a paper summary.
<!-- delta:SF-2026-ARXIV-2607-29209:end -->

<!-- books-review:SF-2026-ARXIV-2607-29209:start -->
Decision=`Not Assessed`；不得在共享 Books 未取得日期有序写锁时把 queue 当作已集成。
<!-- books-review:SF-2026-ARXIV-2607-29209:end -->

<!-- existing:SF-2026-ARXIV-2607-29211:start -->
Canonical owner 已解析为 `TRAIN-GRPO` / `books/part-04-training-system/33-grpo.md`；目标与相邻章节的 proposition-level 对读由根任务按日期串行执行，作者侧不在并发期间推定结果。
<!-- existing:SF-2026-ARXIV-2607-29211:end -->

<!-- delta:SF-2026-ARXIV-2607-29211:start -->
Exact-v1 evidence and source-specific review are available at `review:SF-2026-ARXIV-2607-29211`; durable delta must be reconciled against current Books rather than appended as a paper summary.
<!-- delta:SF-2026-ARXIV-2607-29211:end -->

<!-- books-review:SF-2026-ARXIV-2607-29211:start -->
Decision=`Not Assessed`；不得在共享 Books 未取得日期有序写锁时把 queue 当作已集成。
<!-- books-review:SF-2026-ARXIV-2607-29211:end -->

<!-- existing:SF-2026-ARXIV-2607-29218:start -->
Canonical owner 已解析为 `PLATFORM-EVALUATION-SYSTEM` / `books/part-06-ai-infrastructure/66-evaluation-system.md`；目标与相邻章节的 proposition-level 对读由根任务按日期串行执行，作者侧不在并发期间推定结果。
<!-- existing:SF-2026-ARXIV-2607-29218:end -->

<!-- delta:SF-2026-ARXIV-2607-29218:start -->
Exact-v1 evidence and source-specific review are available at `review:SF-2026-ARXIV-2607-29218`; durable delta must be reconciled against current Books rather than appended as a paper summary.
<!-- delta:SF-2026-ARXIV-2607-29218:end -->

<!-- books-review:SF-2026-ARXIV-2607-29218:start -->
Decision=`Not Assessed`；不得在共享 Books 未取得日期有序写锁时把 queue 当作已集成。
<!-- books-review:SF-2026-ARXIV-2607-29218:end -->

<!-- existing:SF-2026-ARXIV-2607-29221:start -->
Canonical owner 已解析为 `PLATFORM-SECURITY` / `books/part-06-ai-infrastructure/72-security.md`；目标与相邻章节的 proposition-level 对读由根任务按日期串行执行，作者侧不在并发期间推定结果。
<!-- existing:SF-2026-ARXIV-2607-29221:end -->

<!-- delta:SF-2026-ARXIV-2607-29221:start -->
Exact-v1 evidence and source-specific review are available at `review:SF-2026-ARXIV-2607-29221`; durable delta must be reconciled against current Books rather than appended as a paper summary.
<!-- delta:SF-2026-ARXIV-2607-29221:end -->

<!-- books-review:SF-2026-ARXIV-2607-29221:start -->
Decision=`Not Assessed`；不得在共享 Books 未取得日期有序写锁时把 queue 当作已集成。
<!-- books-review:SF-2026-ARXIV-2607-29221:end -->

<!-- existing:SF-2026-ARXIV-2607-29235:start -->
Canonical owner 已解析为 `MULTIMODAL-WORLD-MODELS` / `books/part-03-multimodal-world-models/25-multimodal-world-models.md`；目标与相邻章节的 proposition-level 对读由根任务按日期串行执行，作者侧不在并发期间推定结果。
<!-- existing:SF-2026-ARXIV-2607-29235:end -->

<!-- delta:SF-2026-ARXIV-2607-29235:start -->
Exact-v1 evidence and source-specific review are available at `review:SF-2026-ARXIV-2607-29235`; durable delta must be reconciled against current Books rather than appended as a paper summary.
<!-- delta:SF-2026-ARXIV-2607-29235:end -->

<!-- books-review:SF-2026-ARXIV-2607-29235:start -->
Decision=`Not Assessed`；不得在共享 Books 未取得日期有序写锁时把 queue 当作已集成。
<!-- books-review:SF-2026-ARXIV-2607-29235:end -->

<!-- existing:SF-2026-ARXIV-2607-29240:start -->
Canonical owner 已解析为 `MULTIMODAL-REPRESENTATION` / `books/part-03-multimodal-world-models/23-multimodal-representation.md`；目标与相邻章节的 proposition-level 对读由根任务按日期串行执行，作者侧不在并发期间推定结果。
<!-- existing:SF-2026-ARXIV-2607-29240:end -->

<!-- delta:SF-2026-ARXIV-2607-29240:start -->
Exact-v1 evidence and source-specific review are available at `review:SF-2026-ARXIV-2607-29240`; durable delta must be reconciled against current Books rather than appended as a paper summary.
<!-- delta:SF-2026-ARXIV-2607-29240:end -->

<!-- books-review:SF-2026-ARXIV-2607-29240:start -->
Decision=`Not Assessed`；不得在共享 Books 未取得日期有序写锁时把 queue 当作已集成。
<!-- books-review:SF-2026-ARXIV-2607-29240:end -->

<!-- existing:SF-2026-ARXIV-2607-29246:start -->
Canonical owner 已解析为 `TRAIN-RLHF` / `books/part-04-training-system/31-rlhf.md`；目标与相邻章节的 proposition-level 对读由根任务按日期串行执行，作者侧不在并发期间推定结果。
<!-- existing:SF-2026-ARXIV-2607-29246:end -->

<!-- delta:SF-2026-ARXIV-2607-29246:start -->
Exact-v1 evidence and source-specific review are available at `review:SF-2026-ARXIV-2607-29246`; durable delta must be reconciled against current Books rather than appended as a paper summary.
<!-- delta:SF-2026-ARXIV-2607-29246:end -->

<!-- books-review:SF-2026-ARXIV-2607-29246:start -->
Decision=`Not Assessed`；不得在共享 Books 未取得日期有序写锁时把 queue 当作已集成。
<!-- books-review:SF-2026-ARXIV-2607-29246:end -->

<!-- existing:SF-2026-ARXIV-2607-29250:start -->
Canonical owner 已解析为 `TRAIN-DATA` / `books/part-04-training-system/27-data.md`；目标与相邻章节的 proposition-level 对读由根任务按日期串行执行，作者侧不在并发期间推定结果。
<!-- existing:SF-2026-ARXIV-2607-29250:end -->

<!-- delta:SF-2026-ARXIV-2607-29250:start -->
Exact-v1 evidence and source-specific review are available at `review:SF-2026-ARXIV-2607-29250`; durable delta must be reconciled against current Books rather than appended as a paper summary.
<!-- delta:SF-2026-ARXIV-2607-29250:end -->

<!-- books-review:SF-2026-ARXIV-2607-29250:start -->
Decision=`Not Assessed`；不得在共享 Books 未取得日期有序写锁时把 queue 当作已集成。
<!-- books-review:SF-2026-ARXIV-2607-29250:end -->

<!-- existing:SF-2026-ARXIV-2607-29252:start -->
Canonical owner 已解析为 `PLATFORM-EVALUATION-SYSTEM` / `books/part-06-ai-infrastructure/66-evaluation-system.md`；目标与相邻章节的 proposition-level 对读由根任务按日期串行执行，作者侧不在并发期间推定结果。
<!-- existing:SF-2026-ARXIV-2607-29252:end -->

<!-- delta:SF-2026-ARXIV-2607-29252:start -->
Exact-v1 evidence and source-specific review are available at `review:SF-2026-ARXIV-2607-29252`; durable delta must be reconciled against current Books rather than appended as a paper summary.
<!-- delta:SF-2026-ARXIV-2607-29252:end -->

<!-- books-review:SF-2026-ARXIV-2607-29252:start -->
Decision=`Not Assessed`；不得在共享 Books 未取得日期有序写锁时把 queue 当作已集成。
<!-- books-review:SF-2026-ARXIV-2607-29252:end -->

<!-- existing:SF-2026-ARXIV-2607-29254:start -->
Canonical owner 已解析为 `AGENT-TOOL-CALLING` / `books/part-07-agent/78-tool-calling.md`；目标与相邻章节的 proposition-level 对读由根任务按日期串行执行，作者侧不在并发期间推定结果。
<!-- existing:SF-2026-ARXIV-2607-29254:end -->

<!-- delta:SF-2026-ARXIV-2607-29254:start -->
Exact-v1 evidence and source-specific review are available at `review:SF-2026-ARXIV-2607-29254`; durable delta must be reconciled against current Books rather than appended as a paper summary.
<!-- delta:SF-2026-ARXIV-2607-29254:end -->

<!-- books-review:SF-2026-ARXIV-2607-29254:start -->
Decision=`Not Assessed`；不得在共享 Books 未取得日期有序写锁时把 queue 当作已集成。
<!-- books-review:SF-2026-ARXIV-2607-29254:end -->

<!-- existing:SF-2026-ARXIV-2607-29279:start -->
Canonical owner 已解析为 `INFER-SPECULATIVE-DECODING` / `books/part-05-inference-system/48-speculative-decoding.md`；目标与相邻章节的 proposition-level 对读由根任务按日期串行执行，作者侧不在并发期间推定结果。
<!-- existing:SF-2026-ARXIV-2607-29279:end -->

<!-- delta:SF-2026-ARXIV-2607-29279:start -->
Exact-v1 evidence and source-specific review are available at `review:SF-2026-ARXIV-2607-29279`; durable delta must be reconciled against current Books rather than appended as a paper summary.
<!-- delta:SF-2026-ARXIV-2607-29279:end -->

<!-- books-review:SF-2026-ARXIV-2607-29279:start -->
Decision=`Not Assessed`；不得在共享 Books 未取得日期有序写锁时把 queue 当作已集成。
<!-- books-review:SF-2026-ARXIV-2607-29279:end -->

<!-- existing:SF-2026-ARXIV-2607-29283:start -->
Canonical owner 已解析为 `TRAIN-DATA` / `books/part-04-training-system/27-data.md`；目标与相邻章节的 proposition-level 对读由根任务按日期串行执行，作者侧不在并发期间推定结果。
<!-- existing:SF-2026-ARXIV-2607-29283:end -->

<!-- delta:SF-2026-ARXIV-2607-29283:start -->
Exact-v1 evidence and source-specific review are available at `review:SF-2026-ARXIV-2607-29283`; durable delta must be reconciled against current Books rather than appended as a paper summary.
<!-- delta:SF-2026-ARXIV-2607-29283:end -->

<!-- books-review:SF-2026-ARXIV-2607-29283:start -->
Decision=`Not Assessed`；不得在共享 Books 未取得日期有序写锁时把 queue 当作已集成。
<!-- books-review:SF-2026-ARXIV-2607-29283:end -->

<!-- existing:SF-2026-ARXIV-2607-29285:start -->
Canonical owner 已解析为 `MULTIMODAL-EMBODIED-VLA` / `books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md`；目标与相邻章节的 proposition-level 对读由根任务按日期串行执行，作者侧不在并发期间推定结果。
<!-- existing:SF-2026-ARXIV-2607-29285:end -->

<!-- delta:SF-2026-ARXIV-2607-29285:start -->
Exact-v1 evidence and source-specific review are available at `review:SF-2026-ARXIV-2607-29285`; durable delta must be reconciled against current Books rather than appended as a paper summary.
<!-- delta:SF-2026-ARXIV-2607-29285:end -->

<!-- books-review:SF-2026-ARXIV-2607-29285:start -->
Decision=`Not Assessed`；不得在共享 Books 未取得日期有序写锁时把 queue 当作已集成。
<!-- books-review:SF-2026-ARXIV-2607-29285:end -->

<!-- existing:SF-2026-ARXIV-2607-29302:start -->
Canonical owner 已解析为 `MULTIMODAL-WORLD-MODELS` / `books/part-03-multimodal-world-models/25-multimodal-world-models.md`；目标与相邻章节的 proposition-level 对读由根任务按日期串行执行，作者侧不在并发期间推定结果。
<!-- existing:SF-2026-ARXIV-2607-29302:end -->

<!-- delta:SF-2026-ARXIV-2607-29302:start -->
Exact-v1 evidence and source-specific review are available at `review:SF-2026-ARXIV-2607-29302`; durable delta must be reconciled against current Books rather than appended as a paper summary.
<!-- delta:SF-2026-ARXIV-2607-29302:end -->

<!-- books-review:SF-2026-ARXIV-2607-29302:start -->
Decision=`Not Assessed`；不得在共享 Books 未取得日期有序写锁时把 queue 当作已集成。
<!-- books-review:SF-2026-ARXIV-2607-29302:end -->

<!-- existing:SF-2026-ARXIV-2607-29320:start -->
Canonical owner 已解析为 `AGENT-PLATFORM` / `books/part-07-agent/84-agent-platform.md`；目标与相邻章节的 proposition-level 对读由根任务按日期串行执行，作者侧不在并发期间推定结果。
<!-- existing:SF-2026-ARXIV-2607-29320:end -->

<!-- delta:SF-2026-ARXIV-2607-29320:start -->
Exact-v1 evidence and source-specific review are available at `review:SF-2026-ARXIV-2607-29320`; durable delta must be reconciled against current Books rather than appended as a paper summary.
<!-- delta:SF-2026-ARXIV-2607-29320:end -->

<!-- books-review:SF-2026-ARXIV-2607-29320:start -->
Decision=`Not Assessed`；不得在共享 Books 未取得日期有序写锁时把 queue 当作已集成。
<!-- books-review:SF-2026-ARXIV-2607-29320:end -->

<!-- existing:SF-2026-ARXIV-2607-29353:start -->
Canonical owner 已解析为 `TRAIN-LORA` / `books/part-04-training-system/30-lora.md`；目标与相邻章节的 proposition-level 对读由根任务按日期串行执行，作者侧不在并发期间推定结果。
<!-- existing:SF-2026-ARXIV-2607-29353:end -->

<!-- delta:SF-2026-ARXIV-2607-29353:start -->
Exact-v1 evidence and source-specific review are available at `review:SF-2026-ARXIV-2607-29353`; durable delta must be reconciled against current Books rather than appended as a paper summary.
<!-- delta:SF-2026-ARXIV-2607-29353:end -->

<!-- books-review:SF-2026-ARXIV-2607-29353:start -->
Decision=`Not Assessed`；不得在共享 Books 未取得日期有序写锁时把 queue 当作已集成。
<!-- books-review:SF-2026-ARXIV-2607-29353:end -->

<!-- existing:SF-2026-ARXIV-2607-29363:start -->
Canonical owner 已解析为 `MULTIMODAL-GENERATIVE-PARADIGMS` / `books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md`；目标与相邻章节的 proposition-level 对读由根任务按日期串行执行，作者侧不在并发期间推定结果。
<!-- existing:SF-2026-ARXIV-2607-29363:end -->

<!-- delta:SF-2026-ARXIV-2607-29363:start -->
Exact-v1 evidence and source-specific review are available at `review:SF-2026-ARXIV-2607-29363`; durable delta must be reconciled against current Books rather than appended as a paper summary.
<!-- delta:SF-2026-ARXIV-2607-29363:end -->

<!-- books-review:SF-2026-ARXIV-2607-29363:start -->
Decision=`Not Assessed`；不得在共享 Books 未取得日期有序写锁时把 queue 当作已集成。
<!-- books-review:SF-2026-ARXIV-2607-29363:end -->

<!-- existing:SF-2026-ARXIV-2607-29377:start -->
Canonical owner 已解析为 `AGENT-MEMORY` / `books/part-07-agent/77-memory.md`；目标与相邻章节的 proposition-level 对读由根任务按日期串行执行，作者侧不在并发期间推定结果。
<!-- existing:SF-2026-ARXIV-2607-29377:end -->

<!-- delta:SF-2026-ARXIV-2607-29377:start -->
Exact-v1 evidence and source-specific review are available at `review:SF-2026-ARXIV-2607-29377`; durable delta must be reconciled against current Books rather than appended as a paper summary.
<!-- delta:SF-2026-ARXIV-2607-29377:end -->

<!-- books-review:SF-2026-ARXIV-2607-29377:start -->
Decision=`Not Assessed`；不得在共享 Books 未取得日期有序写锁时把 queue 当作已集成。
<!-- books-review:SF-2026-ARXIV-2607-29377:end -->

<!-- existing:SF-2026-ARXIV-2607-29393:start -->
Canonical owner 已解析为 `MULTIMODAL-WORLD-MODELS` / `books/part-03-multimodal-world-models/25-multimodal-world-models.md`；目标与相邻章节的 proposition-level 对读由根任务按日期串行执行，作者侧不在并发期间推定结果。
<!-- existing:SF-2026-ARXIV-2607-29393:end -->

<!-- delta:SF-2026-ARXIV-2607-29393:start -->
Exact-v1 evidence and source-specific review are available at `review:SF-2026-ARXIV-2607-29393`; durable delta must be reconciled against current Books rather than appended as a paper summary.
<!-- delta:SF-2026-ARXIV-2607-29393:end -->

<!-- books-review:SF-2026-ARXIV-2607-29393:start -->
Decision=`Not Assessed`；不得在共享 Books 未取得日期有序写锁时把 queue 当作已集成。
<!-- books-review:SF-2026-ARXIV-2607-29393:end -->

<!-- existing:SF-2026-ARXIV-2607-29398:start -->
Canonical owner 已解析为 `INFER-TENSORRT-LLM` / `books/part-05-inference-system/49-tensorrt-llm.md`；目标与相邻章节的 proposition-level 对读由根任务按日期串行执行，作者侧不在并发期间推定结果。
<!-- existing:SF-2026-ARXIV-2607-29398:end -->

<!-- delta:SF-2026-ARXIV-2607-29398:start -->
Exact-v1 evidence and source-specific review are available at `review:SF-2026-ARXIV-2607-29398`; durable delta must be reconciled against current Books rather than appended as a paper summary.
<!-- delta:SF-2026-ARXIV-2607-29398:end -->

<!-- books-review:SF-2026-ARXIV-2607-29398:start -->
Decision=`Not Assessed`；不得在共享 Books 未取得日期有序写锁时把 queue 当作已集成。
<!-- books-review:SF-2026-ARXIV-2607-29398:end -->

<!-- existing:SF-2026-ARXIV-2607-29405:start -->
Canonical owner 已解析为 `PLATFORM-EVALUATION-SYSTEM` / `books/part-06-ai-infrastructure/66-evaluation-system.md`；目标与相邻章节的 proposition-level 对读由根任务按日期串行执行，作者侧不在并发期间推定结果。
<!-- existing:SF-2026-ARXIV-2607-29405:end -->

<!-- delta:SF-2026-ARXIV-2607-29405:start -->
Exact-v1 evidence and source-specific review are available at `review:SF-2026-ARXIV-2607-29405`; durable delta must be reconciled against current Books rather than appended as a paper summary.
<!-- delta:SF-2026-ARXIV-2607-29405:end -->

<!-- books-review:SF-2026-ARXIV-2607-29405:start -->
Decision=`Not Assessed`；不得在共享 Books 未取得日期有序写锁时把 queue 当作已集成。
<!-- books-review:SF-2026-ARXIV-2607-29405:end -->

<!-- existing:SF-2026-ARXIV-2607-29431:start -->
Canonical owner 已解析为 `PLATFORM-EVALUATION-SYSTEM` / `books/part-06-ai-infrastructure/66-evaluation-system.md`；目标与相邻章节的 proposition-level 对读由根任务按日期串行执行，作者侧不在并发期间推定结果。
<!-- existing:SF-2026-ARXIV-2607-29431:end -->

<!-- delta:SF-2026-ARXIV-2607-29431:start -->
Exact-v1 evidence and source-specific review are available at `review:SF-2026-ARXIV-2607-29431`; durable delta must be reconciled against current Books rather than appended as a paper summary.
<!-- delta:SF-2026-ARXIV-2607-29431:end -->

<!-- books-review:SF-2026-ARXIV-2607-29431:start -->
Decision=`Not Assessed`；不得在共享 Books 未取得日期有序写锁时把 queue 当作已集成。
<!-- books-review:SF-2026-ARXIV-2607-29431:end -->

<!-- existing:SF-2026-ARXIV-2607-29440:start -->
Canonical owner 已解析为 `AGENT-MEMORY` / `books/part-07-agent/77-memory.md`；目标与相邻章节的 proposition-level 对读由根任务按日期串行执行，作者侧不在并发期间推定结果。
<!-- existing:SF-2026-ARXIV-2607-29440:end -->

<!-- delta:SF-2026-ARXIV-2607-29440:start -->
Exact-v1 evidence and source-specific review are available at `review:SF-2026-ARXIV-2607-29440`; durable delta must be reconciled against current Books rather than appended as a paper summary.
<!-- delta:SF-2026-ARXIV-2607-29440:end -->

<!-- books-review:SF-2026-ARXIV-2607-29440:start -->
Decision=`Not Assessed`；不得在共享 Books 未取得日期有序写锁时把 queue 当作已集成。
<!-- books-review:SF-2026-ARXIV-2607-29440:end -->

<!-- existing:SF-2026-ARXIV-2607-29465:start -->
Canonical owner 已解析为 `PLATFORM-GPU-SCHEDULER` / `books/part-06-ai-infrastructure/63-gpu-scheduler.md`；目标与相邻章节的 proposition-level 对读由根任务按日期串行执行，作者侧不在并发期间推定结果。
<!-- existing:SF-2026-ARXIV-2607-29465:end -->

<!-- delta:SF-2026-ARXIV-2607-29465:start -->
Exact-v1 evidence and source-specific review are available at `review:SF-2026-ARXIV-2607-29465`; durable delta must be reconciled against current Books rather than appended as a paper summary.
<!-- delta:SF-2026-ARXIV-2607-29465:end -->

<!-- books-review:SF-2026-ARXIV-2607-29465:start -->
Decision=`Not Assessed`；不得在共享 Books 未取得日期有序写锁时把 queue 当作已集成。
<!-- books-review:SF-2026-ARXIV-2607-29465:end -->

<!-- existing:SF-2026-ARXIV-2607-29468:start -->
Canonical owner 已解析为 `AGENT-PLANNING` / `books/part-07-agent/79-planning.md`；目标与相邻章节的 proposition-level 对读由根任务按日期串行执行，作者侧不在并发期间推定结果。
<!-- existing:SF-2026-ARXIV-2607-29468:end -->

<!-- delta:SF-2026-ARXIV-2607-29468:start -->
Exact-v1 evidence and source-specific review are available at `review:SF-2026-ARXIV-2607-29468`; durable delta must be reconciled against current Books rather than appended as a paper summary.
<!-- delta:SF-2026-ARXIV-2607-29468:end -->

<!-- books-review:SF-2026-ARXIV-2607-29468:start -->
Decision=`Not Assessed`；不得在共享 Books 未取得日期有序写锁时把 queue 当作已集成。
<!-- books-review:SF-2026-ARXIV-2607-29468:end -->

<!-- existing:SF-2026-ARXIV-2607-29484:start -->
Canonical owner 已解析为 `TRAIN-DATA` / `books/part-04-training-system/27-data.md`；目标与相邻章节的 proposition-level 对读由根任务按日期串行执行，作者侧不在并发期间推定结果。
<!-- existing:SF-2026-ARXIV-2607-29484:end -->

<!-- delta:SF-2026-ARXIV-2607-29484:start -->
Exact-v1 evidence and source-specific review are available at `review:SF-2026-ARXIV-2607-29484`; durable delta must be reconciled against current Books rather than appended as a paper summary.
<!-- delta:SF-2026-ARXIV-2607-29484:end -->

<!-- books-review:SF-2026-ARXIV-2607-29484:start -->
Decision=`Not Assessed`；不得在共享 Books 未取得日期有序写锁时把 queue 当作已集成。
<!-- books-review:SF-2026-ARXIV-2607-29484:end -->

<!-- existing:SF-2026-ARXIV-2607-29494:start -->
Canonical owner 已解析为 `TRAIN-GRPO` / `books/part-04-training-system/33-grpo.md`；目标与相邻章节的 proposition-level 对读由根任务按日期串行执行，作者侧不在并发期间推定结果。
<!-- existing:SF-2026-ARXIV-2607-29494:end -->

<!-- delta:SF-2026-ARXIV-2607-29494:start -->
Exact-v1 evidence and source-specific review are available at `review:SF-2026-ARXIV-2607-29494`; durable delta must be reconciled against current Books rather than appended as a paper summary.
<!-- delta:SF-2026-ARXIV-2607-29494:end -->

<!-- books-review:SF-2026-ARXIV-2607-29494:start -->
Decision=`Not Assessed`；不得在共享 Books 未取得日期有序写锁时把 queue 当作已集成。
<!-- books-review:SF-2026-ARXIV-2607-29494:end -->

<!-- existing:SF-2026-ARXIV-2607-29503:start -->
Canonical owner 已解析为 `TRAIN-PRETRAINING` / `books/part-04-training-system/28-pretraining.md`；目标与相邻章节的 proposition-level 对读由根任务按日期串行执行，作者侧不在并发期间推定结果。
<!-- existing:SF-2026-ARXIV-2607-29503:end -->

<!-- delta:SF-2026-ARXIV-2607-29503:start -->
Exact-v1 evidence and source-specific review are available at `review:SF-2026-ARXIV-2607-29503`; durable delta must be reconciled against current Books rather than appended as a paper summary.
<!-- delta:SF-2026-ARXIV-2607-29503:end -->

<!-- books-review:SF-2026-ARXIV-2607-29503:start -->
Decision=`Not Assessed`；不得在共享 Books 未取得日期有序写锁时把 queue 当作已集成。
<!-- books-review:SF-2026-ARXIV-2607-29503:end -->

<!-- existing:SF-2026-ARXIV-2607-29516:start -->
Canonical owner 已解析为 `PLATFORM-EVALUATION-SYSTEM` / `books/part-06-ai-infrastructure/66-evaluation-system.md`；目标与相邻章节的 proposition-level 对读由根任务按日期串行执行，作者侧不在并发期间推定结果。
<!-- existing:SF-2026-ARXIV-2607-29516:end -->

<!-- delta:SF-2026-ARXIV-2607-29516:start -->
Exact-v1 evidence and source-specific review are available at `review:SF-2026-ARXIV-2607-29516`; durable delta must be reconciled against current Books rather than appended as a paper summary.
<!-- delta:SF-2026-ARXIV-2607-29516:end -->

<!-- books-review:SF-2026-ARXIV-2607-29516:start -->
Decision=`Not Assessed`；不得在共享 Books 未取得日期有序写锁时把 queue 当作已集成。
<!-- books-review:SF-2026-ARXIV-2607-29516:end -->

<!-- existing:SF-2026-ARXIV-2607-29529:start -->
Canonical owner 已解析为 `AGENT-WORKFLOW` / `books/part-07-agent/81-workflow.md`；目标与相邻章节的 proposition-level 对读由根任务按日期串行执行，作者侧不在并发期间推定结果。
<!-- existing:SF-2026-ARXIV-2607-29529:end -->

<!-- delta:SF-2026-ARXIV-2607-29529:start -->
Exact-v1 evidence and source-specific review are available at `review:SF-2026-ARXIV-2607-29529`; durable delta must be reconciled against current Books rather than appended as a paper summary.
<!-- delta:SF-2026-ARXIV-2607-29529:end -->

<!-- books-review:SF-2026-ARXIV-2607-29529:start -->
Decision=`Not Assessed`；不得在共享 Books 未取得日期有序写锁时把 queue 当作已集成。
<!-- books-review:SF-2026-ARXIV-2607-29529:end -->

<!-- existing:SF-2026-ARXIV-2607-29545:start -->
Canonical owner 已解析为 `MULTIMODAL-GENERATIVE-PARADIGMS` / `books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md`；目标与相邻章节的 proposition-level 对读由根任务按日期串行执行，作者侧不在并发期间推定结果。
<!-- existing:SF-2026-ARXIV-2607-29545:end -->

<!-- delta:SF-2026-ARXIV-2607-29545:start -->
Exact-v1 evidence and source-specific review are available at `review:SF-2026-ARXIV-2607-29545`; durable delta must be reconciled against current Books rather than appended as a paper summary.
<!-- delta:SF-2026-ARXIV-2607-29545:end -->

<!-- books-review:SF-2026-ARXIV-2607-29545:start -->
Decision=`Not Assessed`；不得在共享 Books 未取得日期有序写锁时把 queue 当作已集成。
<!-- books-review:SF-2026-ARXIV-2607-29545:end -->

<!-- existing:SF-2026-ARXIV-2607-29549:start -->
Canonical owner 已解析为 `AGENT-TOOL-CALLING` / `books/part-07-agent/78-tool-calling.md`；目标与相邻章节的 proposition-level 对读由根任务按日期串行执行，作者侧不在并发期间推定结果。
<!-- existing:SF-2026-ARXIV-2607-29549:end -->

<!-- delta:SF-2026-ARXIV-2607-29549:start -->
Exact-v1 evidence and source-specific review are available at `review:SF-2026-ARXIV-2607-29549`; durable delta must be reconciled against current Books rather than appended as a paper summary.
<!-- delta:SF-2026-ARXIV-2607-29549:end -->

<!-- books-review:SF-2026-ARXIV-2607-29549:start -->
Decision=`Not Assessed`；不得在共享 Books 未取得日期有序写锁时把 queue 当作已集成。
<!-- books-review:SF-2026-ARXIV-2607-29549:end -->

<!-- existing:SF-2026-ARXIV-2607-29559:start -->
Canonical owner 已解析为 `TRAIN-RLHF` / `books/part-04-training-system/31-rlhf.md`；目标与相邻章节的 proposition-level 对读由根任务按日期串行执行，作者侧不在并发期间推定结果。
<!-- existing:SF-2026-ARXIV-2607-29559:end -->

<!-- delta:SF-2026-ARXIV-2607-29559:start -->
Exact-v1 evidence and source-specific review are available at `review:SF-2026-ARXIV-2607-29559`; durable delta must be reconciled against current Books rather than appended as a paper summary.
<!-- delta:SF-2026-ARXIV-2607-29559:end -->

<!-- books-review:SF-2026-ARXIV-2607-29559:start -->
Decision=`Not Assessed`；不得在共享 Books 未取得日期有序写锁时把 queue 当作已集成。
<!-- books-review:SF-2026-ARXIV-2607-29559:end -->

<!-- existing:SF-2026-ARXIV-2607-29569:start -->
Canonical owner 已解析为 `MULTIMODAL-EMBODIED-VLA` / `books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md`；目标与相邻章节的 proposition-level 对读由根任务按日期串行执行，作者侧不在并发期间推定结果。
<!-- existing:SF-2026-ARXIV-2607-29569:end -->

<!-- delta:SF-2026-ARXIV-2607-29569:start -->
Exact-v1 evidence and source-specific review are available at `review:SF-2026-ARXIV-2607-29569`; durable delta must be reconciled against current Books rather than appended as a paper summary.
<!-- delta:SF-2026-ARXIV-2607-29569:end -->

<!-- books-review:SF-2026-ARXIV-2607-29569:start -->
Decision=`Not Assessed`；不得在共享 Books 未取得日期有序写锁时把 queue 当作已集成。
<!-- books-review:SF-2026-ARXIV-2607-29569:end -->

<!-- existing:SF-2026-ARXIV-2607-29575:start -->
Canonical owner 已解析为 `INFER-SCHEDULING` / `books/part-05-inference-system/56-inference-scheduling.md`；目标与相邻章节的 proposition-level 对读由根任务按日期串行执行，作者侧不在并发期间推定结果。
<!-- existing:SF-2026-ARXIV-2607-29575:end -->

<!-- delta:SF-2026-ARXIV-2607-29575:start -->
Exact-v1 evidence and source-specific review are available at `review:SF-2026-ARXIV-2607-29575`; durable delta must be reconciled against current Books rather than appended as a paper summary.
<!-- delta:SF-2026-ARXIV-2607-29575:end -->

<!-- books-review:SF-2026-ARXIV-2607-29575:start -->
Decision=`Not Assessed`；不得在共享 Books 未取得日期有序写锁时把 queue 当作已集成。
<!-- books-review:SF-2026-ARXIV-2607-29575:end -->

<!-- existing:SF-2026-ARXIV-2607-29591:start -->
Canonical owner 已解析为 `INFER-KV-CACHE` / `books/part-05-inference-system/45-why-kv-cache-speeds-up.md`；目标与相邻章节的 proposition-level 对读由根任务按日期串行执行，作者侧不在并发期间推定结果。
<!-- existing:SF-2026-ARXIV-2607-29591:end -->

<!-- delta:SF-2026-ARXIV-2607-29591:start -->
Exact-v1 evidence and source-specific review are available at `review:SF-2026-ARXIV-2607-29591`; durable delta must be reconciled against current Books rather than appended as a paper summary.
<!-- delta:SF-2026-ARXIV-2607-29591:end -->

<!-- books-review:SF-2026-ARXIV-2607-29591:start -->
Decision=`Not Assessed`；不得在共享 Books 未取得日期有序写锁时把 queue 当作已集成。
<!-- books-review:SF-2026-ARXIV-2607-29591:end -->

<!-- existing:SF-2026-ARXIV-2607-29596:start -->
Canonical owner 已解析为 `MULTIMODAL-EMBODIED-VLA` / `books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md`；目标与相邻章节的 proposition-level 对读由根任务按日期串行执行，作者侧不在并发期间推定结果。
<!-- existing:SF-2026-ARXIV-2607-29596:end -->

<!-- delta:SF-2026-ARXIV-2607-29596:start -->
Exact-v1 evidence and source-specific review are available at `review:SF-2026-ARXIV-2607-29596`; durable delta must be reconciled against current Books rather than appended as a paper summary.
<!-- delta:SF-2026-ARXIV-2607-29596:end -->

<!-- books-review:SF-2026-ARXIV-2607-29596:start -->
Decision=`Not Assessed`；不得在共享 Books 未取得日期有序写锁时把 queue 当作已集成。
<!-- books-review:SF-2026-ARXIV-2607-29596:end -->

<!-- existing:SF-2026-ARXIV-2607-29600:start -->
Canonical owner 已解析为 `AGENT-MEMORY` / `books/part-07-agent/77-memory.md`；目标与相邻章节的 proposition-level 对读由根任务按日期串行执行，作者侧不在并发期间推定结果。
<!-- existing:SF-2026-ARXIV-2607-29600:end -->

<!-- delta:SF-2026-ARXIV-2607-29600:start -->
Exact-v1 evidence and source-specific review are available at `review:SF-2026-ARXIV-2607-29600`; durable delta must be reconciled against current Books rather than appended as a paper summary.
<!-- delta:SF-2026-ARXIV-2607-29600:end -->

<!-- books-review:SF-2026-ARXIV-2607-29600:start -->
Decision=`Not Assessed`；不得在共享 Books 未取得日期有序写锁时把 queue 当作已集成。
<!-- books-review:SF-2026-ARXIV-2607-29600:end -->

<!-- existing:SF-2026-ARXIV-2607-29601:start -->
Canonical owner 已解析为 `TRAIN-DATA` / `books/part-04-training-system/27-data.md`；目标与相邻章节的 proposition-level 对读由根任务按日期串行执行，作者侧不在并发期间推定结果。
<!-- existing:SF-2026-ARXIV-2607-29601:end -->

<!-- delta:SF-2026-ARXIV-2607-29601:start -->
Exact-v1 evidence and source-specific review are available at `review:SF-2026-ARXIV-2607-29601`; durable delta must be reconciled against current Books rather than appended as a paper summary.
<!-- delta:SF-2026-ARXIV-2607-29601:end -->

<!-- books-review:SF-2026-ARXIV-2607-29601:start -->
Decision=`Not Assessed`；不得在共享 Books 未取得日期有序写锁时把 queue 当作已集成。
<!-- books-review:SF-2026-ARXIV-2607-29601:end -->

<!-- existing:SF-2026-ARXIV-2607-29613:start -->
Canonical owner 已解析为 `MULTIMODAL-EMBODIED-VLA` / `books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md`；目标与相邻章节的 proposition-level 对读由根任务按日期串行执行，作者侧不在并发期间推定结果。
<!-- existing:SF-2026-ARXIV-2607-29613:end -->

<!-- delta:SF-2026-ARXIV-2607-29613:start -->
Exact-v1 evidence and source-specific review are available at `review:SF-2026-ARXIV-2607-29613`; durable delta must be reconciled against current Books rather than appended as a paper summary.
<!-- delta:SF-2026-ARXIV-2607-29613:end -->

<!-- books-review:SF-2026-ARXIV-2607-29613:start -->
Decision=`Not Assessed`；不得在共享 Books 未取得日期有序写锁时把 queue 当作已集成。
<!-- books-review:SF-2026-ARXIV-2607-29613:end -->

<!-- existing:SF-2026-ARXIV-2607-29626:start -->
Canonical owner 已解析为 `PLATFORM-EVALUATION-SYSTEM` / `books/part-06-ai-infrastructure/66-evaluation-system.md`；目标与相邻章节的 proposition-level 对读由根任务按日期串行执行，作者侧不在并发期间推定结果。
<!-- existing:SF-2026-ARXIV-2607-29626:end -->

<!-- delta:SF-2026-ARXIV-2607-29626:start -->
Exact-v1 evidence and source-specific review are available at `review:SF-2026-ARXIV-2607-29626`; durable delta must be reconciled against current Books rather than appended as a paper summary.
<!-- delta:SF-2026-ARXIV-2607-29626:end -->

<!-- books-review:SF-2026-ARXIV-2607-29626:start -->
Decision=`Not Assessed`；不得在共享 Books 未取得日期有序写锁时把 queue 当作已集成。
<!-- books-review:SF-2026-ARXIV-2607-29626:end -->

<!-- existing:SF-2026-ARXIV-2607-29638:start -->
Canonical owner 已解析为 `AGENT-RAG` / `books/part-07-agent/76-rag.md`；目标与相邻章节的 proposition-level 对读由根任务按日期串行执行，作者侧不在并发期间推定结果。
<!-- existing:SF-2026-ARXIV-2607-29638:end -->

<!-- delta:SF-2026-ARXIV-2607-29638:start -->
Exact-v1 evidence and source-specific review are available at `review:SF-2026-ARXIV-2607-29638`; durable delta must be reconciled against current Books rather than appended as a paper summary.
<!-- delta:SF-2026-ARXIV-2607-29638:end -->

<!-- books-review:SF-2026-ARXIV-2607-29638:start -->
Decision=`Not Assessed`；不得在共享 Books 未取得日期有序写锁时把 queue 当作已集成。
<!-- books-review:SF-2026-ARXIV-2607-29638:end -->

<!-- existing:SF-2026-ARXIV-2607-29658:start -->
Canonical owner 已解析为 `AGENT-WORKFLOW` / `books/part-07-agent/81-workflow.md`；目标与相邻章节的 proposition-level 对读由根任务按日期串行执行，作者侧不在并发期间推定结果。
<!-- existing:SF-2026-ARXIV-2607-29658:end -->

<!-- delta:SF-2026-ARXIV-2607-29658:start -->
Exact-v1 evidence and source-specific review are available at `review:SF-2026-ARXIV-2607-29658`; durable delta must be reconciled against current Books rather than appended as a paper summary.
<!-- delta:SF-2026-ARXIV-2607-29658:end -->

<!-- books-review:SF-2026-ARXIV-2607-29658:start -->
Decision=`Not Assessed`；不得在共享 Books 未取得日期有序写锁时把 queue 当作已集成。
<!-- books-review:SF-2026-ARXIV-2607-29658:end -->

<!-- existing:SF-2026-ARXIV-2607-29674:start -->
Canonical owner 已解析为 `TRAIN-DISTRIBUTED-TRAINING` / `books/part-04-training-system/36-distributed-training.md`；目标与相邻章节的 proposition-level 对读由根任务按日期串行执行，作者侧不在并发期间推定结果。
<!-- existing:SF-2026-ARXIV-2607-29674:end -->

<!-- delta:SF-2026-ARXIV-2607-29674:start -->
Exact-v1 evidence and source-specific review are available at `review:SF-2026-ARXIV-2607-29674`; durable delta must be reconciled against current Books rather than appended as a paper summary.
<!-- delta:SF-2026-ARXIV-2607-29674:end -->

<!-- books-review:SF-2026-ARXIV-2607-29674:start -->
Decision=`Not Assessed`；不得在共享 Books 未取得日期有序写锁时把 queue 当作已集成。
<!-- books-review:SF-2026-ARXIV-2607-29674:end -->

<!-- existing:SF-2026-ARXIV-2607-29678:start -->
Canonical owner 已解析为 `INFER-REQUEST-LIFECYCLE` / `books/part-05-inference-system/42-what-happens-during-inference.md`；目标与相邻章节的 proposition-level 对读由根任务按日期串行执行，作者侧不在并发期间推定结果。
<!-- existing:SF-2026-ARXIV-2607-29678:end -->

<!-- delta:SF-2026-ARXIV-2607-29678:start -->
Exact-v1 evidence and source-specific review are available at `review:SF-2026-ARXIV-2607-29678`; durable delta must be reconciled against current Books rather than appended as a paper summary.
<!-- delta:SF-2026-ARXIV-2607-29678:end -->

<!-- books-review:SF-2026-ARXIV-2607-29678:start -->
Decision=`Not Assessed`；不得在共享 Books 未取得日期有序写锁时把 queue 当作已集成。
<!-- books-review:SF-2026-ARXIV-2607-29678:end -->

## 7. Semantic Audit

<!-- validator:semantic-audit-v1 -->
| Audit ID | Auditor | Scope | Reviewed Refs | Findings | Resolution | Status |
| --- | --- | --- | --- | --- | --- | --- |
| SA-20260803-AUTHOR-COVERAGE | fresh-context:pending-aug03-independent | coverage | coverage:SRC-ARXIV:20260803 | Author cannot self-certify FP/FN | 430/430 authored decisions and row arithmetic complete; hand off all rows to different fresh context | open |
| SA-20260803-AUTHOR-EVIDENCE | fresh-context:pending-aug03-independent | evidence | review:SF-2026-ARXIV-2607-28631; review:SF-2026-ARXIV-2607-28633; review:SF-2026-ARXIV-2607-28636; review:SF-2026-ARXIV-2607-28638; review:SF-2026-ARXIV-2607-28640; review:SF-2026-ARXIV-2607-28642; review:SF-2026-ARXIV-2607-28658; review:SF-2026-ARXIV-2607-28666; review:SF-2026-ARXIV-2607-28669; review:SF-2026-ARXIV-2607-28670; review:SF-2026-ARXIV-2607-28678; review:SF-2026-ARXIV-2607-28684; review:SF-2026-ARXIV-2607-28685; review:SF-2026-ARXIV-2607-28692; review:SF-2026-ARXIV-2607-28699; review:SF-2026-ARXIV-2607-28707; review:SF-2026-ARXIV-2607-28737; review:SF-2026-ARXIV-2607-28777; review:SF-2026-ARXIV-2607-28788; review:SF-2026-ARXIV-2607-28801; review:SF-2026-ARXIV-2607-28802; review:SF-2026-ARXIV-2607-28815; review:SF-2026-ARXIV-2607-28818; review:SF-2026-ARXIV-2607-28824; review:SF-2026-ARXIV-2607-28829; review:SF-2026-ARXIV-2607-28848; review:SF-2026-ARXIV-2607-28871; review:SF-2026-ARXIV-2607-28884; review:SF-2026-ARXIV-2607-28887; review:SF-2026-ARXIV-2607-28896; review:SF-2026-ARXIV-2607-28908; review:SF-2026-ARXIV-2607-28928; review:SF-2026-ARXIV-2607-28940; review:SF-2026-ARXIV-2607-28942; review:SF-2026-ARXIV-2607-28966; review:SF-2026-ARXIV-2607-28979; review:SF-2026-ARXIV-2607-28990; review:SF-2026-ARXIV-2607-28991; review:SF-2026-ARXIV-2607-28993; review:SF-2026-ARXIV-2607-29032; review:SF-2026-ARXIV-2607-29053; review:SF-2026-ARXIV-2607-29065; review:SF-2026-ARXIV-2607-29069; review:SF-2026-ARXIV-2607-29071; review:SF-2026-ARXIV-2607-29076; review:SF-2026-ARXIV-2607-29078; review:SF-2026-ARXIV-2607-29079; review:SF-2026-ARXIV-2607-29104; review:SF-2026-ARXIV-2607-29120; review:SF-2026-ARXIV-2607-29125; review:SF-2026-ARXIV-2607-29167; review:SF-2026-ARXIV-2607-29169; review:SF-2026-ARXIV-2607-29172; review:SF-2026-ARXIV-2607-29175; review:SF-2026-ARXIV-2607-29185; review:SF-2026-ARXIV-2607-29190; review:SF-2026-ARXIV-2607-29199; review:SF-2026-ARXIV-2607-29209; review:SF-2026-ARXIV-2607-29211; review:SF-2026-ARXIV-2607-29218; review:SF-2026-ARXIV-2607-29221; review:SF-2026-ARXIV-2607-29235; review:SF-2026-ARXIV-2607-29240; review:SF-2026-ARXIV-2607-29246; review:SF-2026-ARXIV-2607-29250; review:SF-2026-ARXIV-2607-29252; review:SF-2026-ARXIV-2607-29254; review:SF-2026-ARXIV-2607-29279; review:SF-2026-ARXIV-2607-29283; review:SF-2026-ARXIV-2607-29285; review:SF-2026-ARXIV-2607-29302; review:SF-2026-ARXIV-2607-29320; review:SF-2026-ARXIV-2607-29353; review:SF-2026-ARXIV-2607-29363; review:SF-2026-ARXIV-2607-29377; review:SF-2026-ARXIV-2607-29393; review:SF-2026-ARXIV-2607-29398; review:SF-2026-ARXIV-2607-29405; review:SF-2026-ARXIV-2607-29431; review:SF-2026-ARXIV-2607-29440; review:SF-2026-ARXIV-2607-29465; review:SF-2026-ARXIV-2607-29468; review:SF-2026-ARXIV-2607-29484; review:SF-2026-ARXIV-2607-29494; review:SF-2026-ARXIV-2607-29503; review:SF-2026-ARXIV-2607-29516; review:SF-2026-ARXIV-2607-29529; review:SF-2026-ARXIV-2607-29545; review:SF-2026-ARXIV-2607-29549; review:SF-2026-ARXIV-2607-29559; review:SF-2026-ARXIV-2607-29569; review:SF-2026-ARXIV-2607-29575; review:SF-2026-ARXIV-2607-29591; review:SF-2026-ARXIV-2607-29596; review:SF-2026-ARXIV-2607-29600; review:SF-2026-ARXIV-2607-29601; review:SF-2026-ARXIV-2607-29613; review:SF-2026-ARXIV-2607-29626; review:SF-2026-ARXIV-2607-29638; review:SF-2026-ARXIV-2607-29658; review:SF-2026-ARXIV-2607-29674; review:SF-2026-ARXIV-2607-29678 | Independent locator/claim-boundary audit pending | 102/102 exact-v1 bodies recovered; blocked=0 | open |
| SA-20260803-AUTHOR-SELECTION | fresh-context:pending-aug03-independent | deep_analysis_selection | validator:deep-analysis-selection-v1 | Independent full-frontier comparison pending | Three provisional narrative units selected from all eligible families | open |
| SA-20260803-AUTHOR-BOOKS | fresh-context:pending-aug03-independent | books | books-review:SF-2026-ARXIV-2607-28631; books-review:SF-2026-ARXIV-2607-28633; books-review:SF-2026-ARXIV-2607-28636; books-review:SF-2026-ARXIV-2607-28638; books-review:SF-2026-ARXIV-2607-28640; books-review:SF-2026-ARXIV-2607-28642; books-review:SF-2026-ARXIV-2607-28658; books-review:SF-2026-ARXIV-2607-28666; books-review:SF-2026-ARXIV-2607-28669; books-review:SF-2026-ARXIV-2607-28670; books-review:SF-2026-ARXIV-2607-28678; books-review:SF-2026-ARXIV-2607-28684; books-review:SF-2026-ARXIV-2607-28685; books-review:SF-2026-ARXIV-2607-28692; books-review:SF-2026-ARXIV-2607-28699; books-review:SF-2026-ARXIV-2607-28707; books-review:SF-2026-ARXIV-2607-28737; books-review:SF-2026-ARXIV-2607-28777; books-review:SF-2026-ARXIV-2607-28788; books-review:SF-2026-ARXIV-2607-28801; books-review:SF-2026-ARXIV-2607-28802; books-review:SF-2026-ARXIV-2607-28815; books-review:SF-2026-ARXIV-2607-28818; books-review:SF-2026-ARXIV-2607-28824; books-review:SF-2026-ARXIV-2607-28829; books-review:SF-2026-ARXIV-2607-28848; books-review:SF-2026-ARXIV-2607-28871; books-review:SF-2026-ARXIV-2607-28884; books-review:SF-2026-ARXIV-2607-28887; books-review:SF-2026-ARXIV-2607-28896; books-review:SF-2026-ARXIV-2607-28908; books-review:SF-2026-ARXIV-2607-28928; books-review:SF-2026-ARXIV-2607-28940; books-review:SF-2026-ARXIV-2607-28942; books-review:SF-2026-ARXIV-2607-28966; books-review:SF-2026-ARXIV-2607-28979; books-review:SF-2026-ARXIV-2607-28990; books-review:SF-2026-ARXIV-2607-28991; books-review:SF-2026-ARXIV-2607-28993; books-review:SF-2026-ARXIV-2607-29032; books-review:SF-2026-ARXIV-2607-29053; books-review:SF-2026-ARXIV-2607-29065; books-review:SF-2026-ARXIV-2607-29069; books-review:SF-2026-ARXIV-2607-29071; books-review:SF-2026-ARXIV-2607-29076; books-review:SF-2026-ARXIV-2607-29078; books-review:SF-2026-ARXIV-2607-29079; books-review:SF-2026-ARXIV-2607-29104; books-review:SF-2026-ARXIV-2607-29120; books-review:SF-2026-ARXIV-2607-29125; books-review:SF-2026-ARXIV-2607-29167; books-review:SF-2026-ARXIV-2607-29169; books-review:SF-2026-ARXIV-2607-29172; books-review:SF-2026-ARXIV-2607-29175; books-review:SF-2026-ARXIV-2607-29185; books-review:SF-2026-ARXIV-2607-29190; books-review:SF-2026-ARXIV-2607-29199; books-review:SF-2026-ARXIV-2607-29209; books-review:SF-2026-ARXIV-2607-29211; books-review:SF-2026-ARXIV-2607-29218; books-review:SF-2026-ARXIV-2607-29221; books-review:SF-2026-ARXIV-2607-29235; books-review:SF-2026-ARXIV-2607-29240; books-review:SF-2026-ARXIV-2607-29246; books-review:SF-2026-ARXIV-2607-29250; books-review:SF-2026-ARXIV-2607-29252; books-review:SF-2026-ARXIV-2607-29254; books-review:SF-2026-ARXIV-2607-29279; books-review:SF-2026-ARXIV-2607-29283; books-review:SF-2026-ARXIV-2607-29285; books-review:SF-2026-ARXIV-2607-29302; books-review:SF-2026-ARXIV-2607-29320; books-review:SF-2026-ARXIV-2607-29353; books-review:SF-2026-ARXIV-2607-29363; books-review:SF-2026-ARXIV-2607-29377; books-review:SF-2026-ARXIV-2607-29393; books-review:SF-2026-ARXIV-2607-29398; books-review:SF-2026-ARXIV-2607-29405; books-review:SF-2026-ARXIV-2607-29431; books-review:SF-2026-ARXIV-2607-29440; books-review:SF-2026-ARXIV-2607-29465; books-review:SF-2026-ARXIV-2607-29468; books-review:SF-2026-ARXIV-2607-29484; books-review:SF-2026-ARXIV-2607-29494; books-review:SF-2026-ARXIV-2607-29503; books-review:SF-2026-ARXIV-2607-29516; books-review:SF-2026-ARXIV-2607-29529; books-review:SF-2026-ARXIV-2607-29545; books-review:SF-2026-ARXIV-2607-29549; books-review:SF-2026-ARXIV-2607-29559; books-review:SF-2026-ARXIV-2607-29569; books-review:SF-2026-ARXIV-2607-29575; books-review:SF-2026-ARXIV-2607-29591; books-review:SF-2026-ARXIV-2607-29596; books-review:SF-2026-ARXIV-2607-29600; books-review:SF-2026-ARXIV-2607-29601; books-review:SF-2026-ARXIV-2607-29613; books-review:SF-2026-ARXIV-2607-29626; books-review:SF-2026-ARXIV-2607-29638; books-review:SF-2026-ARXIV-2607-29658; books-review:SF-2026-ARXIV-2607-29674; books-review:SF-2026-ARXIV-2607-29678 | Root serialized comparison/writeback pending | 102 ordered queue items preserve evidence and owner mapping | open |

## 8. Ignored Noise

`328` 个 pre-denominator closures 保存在 `papers/2026/08/_sources/arxiv-owner-replay-20260903/20260803/semantic-screening-author.json`。每项保存 source family、exact identity、title、完整 abstract、摘要命题、分类、owner proof 和 family-specific closure reason；它们没有评分、Source Review、Deep selection 或 Books 痕迹。

## 9. Recommended Action

- 不同 fresh context 必须无抽样挑战 102 个 retained false positive 与 328 个 closure false negative。
- 通过 denominator audit 后，独立复核 102/102 exact-v1 locator、claim boundary 与完整 selection frontier。
- 根任务按日期顺序合并同 owner Books comparison/writeback；writeback 后再做 post-write audit。

## 10. Repository Changes

- 重建 2026-08-03 Daily、430-row semantic ledger、102-family exact-v1 text/review packet 与 Books ordered queue。
- 未修改 Books、Weekly、月级共享索引或 `docs/LEARNING_STATE.md`；未 stage、commit 或 push。

## 11. Open Questions

- 独立 FP/FN audit 是否会收缩或扩展 102-family provisional denominator？
- 哪些 evidence delta 已由当前 Books 完整承载，哪些需要 owner-merged writeback？

## 12. Sources

- [arXiv:2607.28631v1](https://arxiv.org/abs/2607.28631v1) — official exact-v1；official first-announcement owner=2026-08-03；访问日期 2026-09-03。
- [arXiv:2607.28633v1](https://arxiv.org/abs/2607.28633v1) — official exact-v1；official first-announcement owner=2026-08-03；访问日期 2026-09-03。
- [arXiv:2607.28636v1](https://arxiv.org/abs/2607.28636v1) — official exact-v1；official first-announcement owner=2026-08-03；访问日期 2026-09-03。
- [arXiv:2607.28638v1](https://arxiv.org/abs/2607.28638v1) — official exact-v1；official first-announcement owner=2026-08-03；访问日期 2026-09-03。
- [arXiv:2607.28640v1](https://arxiv.org/abs/2607.28640v1) — official exact-v1；official first-announcement owner=2026-08-03；访问日期 2026-09-03。
- [arXiv:2607.28642v1](https://arxiv.org/abs/2607.28642v1) — official exact-v1；official first-announcement owner=2026-08-03；访问日期 2026-09-03。
- [arXiv:2607.28658v1](https://arxiv.org/abs/2607.28658v1) — official exact-v1；official first-announcement owner=2026-08-03；访问日期 2026-09-03。
- [arXiv:2607.28666v1](https://arxiv.org/abs/2607.28666v1) — official exact-v1；official first-announcement owner=2026-08-03；访问日期 2026-09-03。
- [arXiv:2607.28669v1](https://arxiv.org/abs/2607.28669v1) — official exact-v1；official first-announcement owner=2026-08-03；访问日期 2026-09-03。
- [arXiv:2607.28670v1](https://arxiv.org/abs/2607.28670v1) — official exact-v1；official first-announcement owner=2026-08-03；访问日期 2026-09-03。
- [arXiv:2607.28678v1](https://arxiv.org/abs/2607.28678v1) — official exact-v1；official first-announcement owner=2026-08-03；访问日期 2026-09-03。
- [arXiv:2607.28684v1](https://arxiv.org/abs/2607.28684v1) — official exact-v1；official first-announcement owner=2026-08-03；访问日期 2026-09-03。
- [arXiv:2607.28685v1](https://arxiv.org/abs/2607.28685v1) — official exact-v1；official first-announcement owner=2026-08-03；访问日期 2026-09-03。
- [arXiv:2607.28692v1](https://arxiv.org/abs/2607.28692v1) — official exact-v1；official first-announcement owner=2026-08-03；访问日期 2026-09-03。
- [arXiv:2607.28699v1](https://arxiv.org/abs/2607.28699v1) — official exact-v1；official first-announcement owner=2026-08-03；访问日期 2026-09-03。
- [arXiv:2607.28707v1](https://arxiv.org/abs/2607.28707v1) — official exact-v1；official first-announcement owner=2026-08-03；访问日期 2026-09-03。
- [arXiv:2607.28737v1](https://arxiv.org/abs/2607.28737v1) — official exact-v1；official first-announcement owner=2026-08-03；访问日期 2026-09-03。
- [arXiv:2607.28777v1](https://arxiv.org/abs/2607.28777v1) — official exact-v1；official first-announcement owner=2026-08-03；访问日期 2026-09-03。
- [arXiv:2607.28788v1](https://arxiv.org/abs/2607.28788v1) — official exact-v1；official first-announcement owner=2026-08-03；访问日期 2026-09-03。
- [arXiv:2607.28801v1](https://arxiv.org/abs/2607.28801v1) — official exact-v1；official first-announcement owner=2026-08-03；访问日期 2026-09-03。
- [arXiv:2607.28802v1](https://arxiv.org/abs/2607.28802v1) — official exact-v1；official first-announcement owner=2026-08-03；访问日期 2026-09-03。
- [arXiv:2607.28815v1](https://arxiv.org/abs/2607.28815v1) — official exact-v1；official first-announcement owner=2026-08-03；访问日期 2026-09-03。
- [arXiv:2607.28818v1](https://arxiv.org/abs/2607.28818v1) — official exact-v1；official first-announcement owner=2026-08-03；访问日期 2026-09-03。
- [arXiv:2607.28824v1](https://arxiv.org/abs/2607.28824v1) — official exact-v1；official first-announcement owner=2026-08-03；访问日期 2026-09-03。
- [arXiv:2607.28829v1](https://arxiv.org/abs/2607.28829v1) — official exact-v1；official first-announcement owner=2026-08-03；访问日期 2026-09-03。
- [arXiv:2607.28848v1](https://arxiv.org/abs/2607.28848v1) — official exact-v1；official first-announcement owner=2026-08-03；访问日期 2026-09-03。
- [arXiv:2607.28871v1](https://arxiv.org/abs/2607.28871v1) — official exact-v1；official first-announcement owner=2026-08-03；访问日期 2026-09-03。
- [arXiv:2607.28884v1](https://arxiv.org/abs/2607.28884v1) — official exact-v1；official first-announcement owner=2026-08-03；访问日期 2026-09-03。
- [arXiv:2607.28887v1](https://arxiv.org/abs/2607.28887v1) — official exact-v1；official first-announcement owner=2026-08-03；访问日期 2026-09-03。
- [arXiv:2607.28896v1](https://arxiv.org/abs/2607.28896v1) — official exact-v1；official first-announcement owner=2026-08-03；访问日期 2026-09-03。
- [arXiv:2607.28908v1](https://arxiv.org/abs/2607.28908v1) — official exact-v1；official first-announcement owner=2026-08-03；访问日期 2026-09-03。
- [arXiv:2607.28928v1](https://arxiv.org/abs/2607.28928v1) — official exact-v1；official first-announcement owner=2026-08-03；访问日期 2026-09-03。
- [arXiv:2607.28940v1](https://arxiv.org/abs/2607.28940v1) — official exact-v1；official first-announcement owner=2026-08-03；访问日期 2026-09-03。
- [arXiv:2607.28942v1](https://arxiv.org/abs/2607.28942v1) — official exact-v1；official first-announcement owner=2026-08-03；访问日期 2026-09-03。
- [arXiv:2607.28966v1](https://arxiv.org/abs/2607.28966v1) — official exact-v1；official first-announcement owner=2026-08-03；访问日期 2026-09-03。
- [arXiv:2607.28979v1](https://arxiv.org/abs/2607.28979v1) — official exact-v1；official first-announcement owner=2026-08-03；访问日期 2026-09-03。
- [arXiv:2607.28990v1](https://arxiv.org/abs/2607.28990v1) — official exact-v1；official first-announcement owner=2026-08-03；访问日期 2026-09-03。
- [arXiv:2607.28991v1](https://arxiv.org/abs/2607.28991v1) — official exact-v1；official first-announcement owner=2026-08-03；访问日期 2026-09-03。
- [arXiv:2607.28993v1](https://arxiv.org/abs/2607.28993v1) — official exact-v1；official first-announcement owner=2026-08-03；访问日期 2026-09-03。
- [arXiv:2607.29032v1](https://arxiv.org/abs/2607.29032v1) — official exact-v1；official first-announcement owner=2026-08-03；访问日期 2026-09-03。
- [arXiv:2607.29053v1](https://arxiv.org/abs/2607.29053v1) — official exact-v1；official first-announcement owner=2026-08-03；访问日期 2026-09-03。
- [arXiv:2607.29065v1](https://arxiv.org/abs/2607.29065v1) — official exact-v1；official first-announcement owner=2026-08-03；访问日期 2026-09-03。
- [arXiv:2607.29069v1](https://arxiv.org/abs/2607.29069v1) — official exact-v1；official first-announcement owner=2026-08-03；访问日期 2026-09-03。
- [arXiv:2607.29071v1](https://arxiv.org/abs/2607.29071v1) — official exact-v1；official first-announcement owner=2026-08-03；访问日期 2026-09-03。
- [arXiv:2607.29076v1](https://arxiv.org/abs/2607.29076v1) — official exact-v1；official first-announcement owner=2026-08-03；访问日期 2026-09-03。
- [arXiv:2607.29078v1](https://arxiv.org/abs/2607.29078v1) — official exact-v1；official first-announcement owner=2026-08-03；访问日期 2026-09-03。
- [arXiv:2607.29079v1](https://arxiv.org/abs/2607.29079v1) — official exact-v1；official first-announcement owner=2026-08-03；访问日期 2026-09-03。
- [arXiv:2607.29104v1](https://arxiv.org/abs/2607.29104v1) — official exact-v1；official first-announcement owner=2026-08-03；访问日期 2026-09-03。
- [arXiv:2607.29120v1](https://arxiv.org/abs/2607.29120v1) — official exact-v1；official first-announcement owner=2026-08-03；访问日期 2026-09-03。
- [arXiv:2607.29125v1](https://arxiv.org/abs/2607.29125v1) — official exact-v1；official first-announcement owner=2026-08-03；访问日期 2026-09-03。
- [arXiv:2607.29167v1](https://arxiv.org/abs/2607.29167v1) — official exact-v1；official first-announcement owner=2026-08-03；访问日期 2026-09-03。
- [arXiv:2607.29169v1](https://arxiv.org/abs/2607.29169v1) — official exact-v1；official first-announcement owner=2026-08-03；访问日期 2026-09-03。
- [arXiv:2607.29172v1](https://arxiv.org/abs/2607.29172v1) — official exact-v1；official first-announcement owner=2026-08-03；访问日期 2026-09-03。
- [arXiv:2607.29175v1](https://arxiv.org/abs/2607.29175v1) — official exact-v1；official first-announcement owner=2026-08-03；访问日期 2026-09-03。
- [arXiv:2607.29185v1](https://arxiv.org/abs/2607.29185v1) — official exact-v1；official first-announcement owner=2026-08-03；访问日期 2026-09-03。
- [arXiv:2607.29190v1](https://arxiv.org/abs/2607.29190v1) — official exact-v1；official first-announcement owner=2026-08-03；访问日期 2026-09-03。
- [arXiv:2607.29199v1](https://arxiv.org/abs/2607.29199v1) — official exact-v1；official first-announcement owner=2026-08-03；访问日期 2026-09-03。
- [arXiv:2607.29209v1](https://arxiv.org/abs/2607.29209v1) — official exact-v1；official first-announcement owner=2026-08-03；访问日期 2026-09-03。
- [arXiv:2607.29211v1](https://arxiv.org/abs/2607.29211v1) — official exact-v1；official first-announcement owner=2026-08-03；访问日期 2026-09-03。
- [arXiv:2607.29218v1](https://arxiv.org/abs/2607.29218v1) — official exact-v1；official first-announcement owner=2026-08-03；访问日期 2026-09-03。
- [arXiv:2607.29221v1](https://arxiv.org/abs/2607.29221v1) — official exact-v1；official first-announcement owner=2026-08-03；访问日期 2026-09-03。
- [arXiv:2607.29235v1](https://arxiv.org/abs/2607.29235v1) — official exact-v1；official first-announcement owner=2026-08-03；访问日期 2026-09-03。
- [arXiv:2607.29240v1](https://arxiv.org/abs/2607.29240v1) — official exact-v1；official first-announcement owner=2026-08-03；访问日期 2026-09-03。
- [arXiv:2607.29246v1](https://arxiv.org/abs/2607.29246v1) — official exact-v1；official first-announcement owner=2026-08-03；访问日期 2026-09-03。
- [arXiv:2607.29250v1](https://arxiv.org/abs/2607.29250v1) — official exact-v1；official first-announcement owner=2026-08-03；访问日期 2026-09-03。
- [arXiv:2607.29252v1](https://arxiv.org/abs/2607.29252v1) — official exact-v1；official first-announcement owner=2026-08-03；访问日期 2026-09-03。
- [arXiv:2607.29254v1](https://arxiv.org/abs/2607.29254v1) — official exact-v1；official first-announcement owner=2026-08-03；访问日期 2026-09-03。
- [arXiv:2607.29279v1](https://arxiv.org/abs/2607.29279v1) — official exact-v1；official first-announcement owner=2026-08-03；访问日期 2026-09-03。
- [arXiv:2607.29283v1](https://arxiv.org/abs/2607.29283v1) — official exact-v1；official first-announcement owner=2026-08-03；访问日期 2026-09-03。
- [arXiv:2607.29285v1](https://arxiv.org/abs/2607.29285v1) — official exact-v1；official first-announcement owner=2026-08-03；访问日期 2026-09-03。
- [arXiv:2607.29302v1](https://arxiv.org/abs/2607.29302v1) — official exact-v1；official first-announcement owner=2026-08-03；访问日期 2026-09-03。
- [arXiv:2607.29320v1](https://arxiv.org/abs/2607.29320v1) — official exact-v1；official first-announcement owner=2026-08-03；访问日期 2026-09-03。
- [arXiv:2607.29353v1](https://arxiv.org/abs/2607.29353v1) — official exact-v1；official first-announcement owner=2026-08-03；访问日期 2026-09-03。
- [arXiv:2607.29363v1](https://arxiv.org/abs/2607.29363v1) — official exact-v1；official first-announcement owner=2026-08-03；访问日期 2026-09-03。
- [arXiv:2607.29377v1](https://arxiv.org/abs/2607.29377v1) — official exact-v1；official first-announcement owner=2026-08-03；访问日期 2026-09-03。
- [arXiv:2607.29393v1](https://arxiv.org/abs/2607.29393v1) — official exact-v1；official first-announcement owner=2026-08-03；访问日期 2026-09-03。
- [arXiv:2607.29398v1](https://arxiv.org/abs/2607.29398v1) — official exact-v1；official first-announcement owner=2026-08-03；访问日期 2026-09-03。
- [arXiv:2607.29405v1](https://arxiv.org/abs/2607.29405v1) — official exact-v1；official first-announcement owner=2026-08-03；访问日期 2026-09-03。
- [arXiv:2607.29431v1](https://arxiv.org/abs/2607.29431v1) — official exact-v1；official first-announcement owner=2026-08-03；访问日期 2026-09-03。
- [arXiv:2607.29440v1](https://arxiv.org/abs/2607.29440v1) — official exact-v1；official first-announcement owner=2026-08-03；访问日期 2026-09-03。
- [arXiv:2607.29465v1](https://arxiv.org/abs/2607.29465v1) — official exact-v1；official first-announcement owner=2026-08-03；访问日期 2026-09-03。
- [arXiv:2607.29468v1](https://arxiv.org/abs/2607.29468v1) — official exact-v1；official first-announcement owner=2026-08-03；访问日期 2026-09-03。
- [arXiv:2607.29484v1](https://arxiv.org/abs/2607.29484v1) — official exact-v1；official first-announcement owner=2026-08-03；访问日期 2026-09-03。
- [arXiv:2607.29494v1](https://arxiv.org/abs/2607.29494v1) — official exact-v1；official first-announcement owner=2026-08-03；访问日期 2026-09-03。
- [arXiv:2607.29503v1](https://arxiv.org/abs/2607.29503v1) — official exact-v1；official first-announcement owner=2026-08-03；访问日期 2026-09-03。
- [arXiv:2607.29516v1](https://arxiv.org/abs/2607.29516v1) — official exact-v1；official first-announcement owner=2026-08-03；访问日期 2026-09-03。
- [arXiv:2607.29529v1](https://arxiv.org/abs/2607.29529v1) — official exact-v1；official first-announcement owner=2026-08-03；访问日期 2026-09-03。
- [arXiv:2607.29545v1](https://arxiv.org/abs/2607.29545v1) — official exact-v1；official first-announcement owner=2026-08-03；访问日期 2026-09-03。
- [arXiv:2607.29549v1](https://arxiv.org/abs/2607.29549v1) — official exact-v1；official first-announcement owner=2026-08-03；访问日期 2026-09-03。
- [arXiv:2607.29559v1](https://arxiv.org/abs/2607.29559v1) — official exact-v1；official first-announcement owner=2026-08-03；访问日期 2026-09-03。
- [arXiv:2607.29569v1](https://arxiv.org/abs/2607.29569v1) — official exact-v1；official first-announcement owner=2026-08-03；访问日期 2026-09-03。
- [arXiv:2607.29575v1](https://arxiv.org/abs/2607.29575v1) — official exact-v1；official first-announcement owner=2026-08-03；访问日期 2026-09-03。
- [arXiv:2607.29591v1](https://arxiv.org/abs/2607.29591v1) — official exact-v1；official first-announcement owner=2026-08-03；访问日期 2026-09-03。
- [arXiv:2607.29596v1](https://arxiv.org/abs/2607.29596v1) — official exact-v1；official first-announcement owner=2026-08-03；访问日期 2026-09-03。
- [arXiv:2607.29600v1](https://arxiv.org/abs/2607.29600v1) — official exact-v1；official first-announcement owner=2026-08-03；访问日期 2026-09-03。
- [arXiv:2607.29601v1](https://arxiv.org/abs/2607.29601v1) — official exact-v1；official first-announcement owner=2026-08-03；访问日期 2026-09-03。
- [arXiv:2607.29613v1](https://arxiv.org/abs/2607.29613v1) — official exact-v1；official first-announcement owner=2026-08-03；访问日期 2026-09-03。
- [arXiv:2607.29626v1](https://arxiv.org/abs/2607.29626v1) — official exact-v1；official first-announcement owner=2026-08-03；访问日期 2026-09-03。
- [arXiv:2607.29638v1](https://arxiv.org/abs/2607.29638v1) — official exact-v1；official first-announcement owner=2026-08-03；访问日期 2026-09-03。
- [arXiv:2607.29658v1](https://arxiv.org/abs/2607.29658v1) — official exact-v1；official first-announcement owner=2026-08-03；访问日期 2026-09-03。
- [arXiv:2607.29674v1](https://arxiv.org/abs/2607.29674v1) — official exact-v1；official first-announcement owner=2026-08-03；访问日期 2026-09-03。
- [arXiv:2607.29678v1](https://arxiv.org/abs/2607.29678v1) — official exact-v1；official first-announcement owner=2026-08-03；访问日期 2026-09-03。

## 13. Final Status

Completion Status=`In Progress`；Coverage=`Open`；Evidence=`Open`；Books=`Open`；Unresolved Findings=`4`。作者侧 raw=`430`、retained=`102`、closures=`328`、exact-v1 reviews=`102`、blocked=`0`；四个 unresolved scopes 是 independent coverage、evidence、selection 与 Books audit。
