# Daily Research — 2026-06-27

**Research Date:** 2026-06-27

**Timezone:** Asia/Shanghai

**Strict Window:** 2026-06-26 09:00:00 ～ 2026-06-27 09:00:00（北京时间，左闭右开）

**Contract:** V2.1 Full Replay；全量枚举与语义筛选冻结候选分母，技术 claim 回到 exact-version primary evidence 与事件时 artifact receipt

**Status:** Complete；Coverage=Closed、Evidence=Passed、Books=Passed，fresh-context Semantic Audit 状态见第 7 节

## Executive Summary
北京时间窗口 [2026-06-26 09:00, 2026-06-27 09:00) 共 384 个注册 identity。全量 title+abstract 语义筛选冻结 384 = 64 retained + 320 family-specific closures，并从 84 个 route-negative identity 中恢复 3 个 false negatives。64/64 official exact-v1 HTML 已访问；Books 重审得到 14 Integrate、47 No Change 与 3 Weekly Only，合并为 11 个 owner 写入；root 已串行完成 14-family 写回，64/64 post-write fresh audit 通过。

## 1. Coverage

<!-- validator:report-metadata-v2 -->
| Field | Value |
| --- | --- |
| Contract Version | V2.1 |
| Score Schema | V2 |
| Report Type | Daily |
| Window Start | 2026-06-27 |
| Window End | 2026-06-27 |
| Registry Version | 2026-08-25 |
| Coverage Mode | Full Replay |
| Baseline Report | — |
| Changed Source IDs | — |
| Previous Denominator ID | — |
| Denominator ID | DEN-20260627-aef6bb58 |
| Denominator Frozen At | 2026-08-29T18:30:00+08:00 |
| Completion Status | Complete |
| Coverage Gate | Closed |
| Evidence Gate | Passed |
| Books Gate | Passed |

### Source Coverage Receipt

<!-- validator:source-coverage-v2 -->
| Source ID | Window Start | Window End | Executed At | Endpoint / Filter | Result | Hits | Candidate Source Families | Pagination / Cursor | Window Watermark | Closure Evidence | Gap / Limitation ID |
| --- | --- | --- | --- | --- | --- | ---: | --- | --- | --- | --- | --- |
| SRC-ARXIV | 2026-06-26T09:00:00+08:00 | 2026-06-27T09:00:00+08:00 | 2026-08-29T18:30:00+08:00 | frozen DataCite prefix snapshots; exact UTC window; all registered categories | checked | 384 | SF-2026-ARXIV-2606-27632; SF-2026-ARXIV-2606-27634; SF-2026-ARXIV-2606-27650; SF-2026-ARXIV-2606-27669; SF-2026-ARXIV-2606-27679; SF-2026-ARXIV-2606-27681; SF-2026-ARXIV-2606-27683; SF-2026-ARXIV-2606-27704; SF-2026-ARXIV-2606-27709; SF-2026-ARXIV-2606-27732; SF-2026-ARXIV-2606-27739; SF-2026-ARXIV-2606-27743; SF-2026-ARXIV-2606-27757; SF-2026-ARXIV-2606-27780; SF-2026-ARXIV-2606-27791; SF-2026-ARXIV-2606-27797; SF-2026-ARXIV-2606-27806; SF-2026-ARXIV-2606-27814; SF-2026-ARXIV-2606-27826; SF-2026-ARXIV-2606-27841; SF-2026-ARXIV-2606-27866; SF-2026-ARXIV-2606-27906; SF-2026-ARXIV-2606-27934; SF-2026-ARXIV-2606-27936; SF-2026-ARXIV-2606-27944; SF-2026-ARXIV-2606-27962; SF-2026-ARXIV-2606-27976; SF-2026-ARXIV-2606-27997; SF-2026-ARXIV-2606-28011; SF-2026-ARXIV-2606-28013; SF-2026-ARXIV-2606-28037; SF-2026-ARXIV-2606-28050; SF-2026-ARXIV-2606-28061; SF-2026-ARXIV-2606-28070; SF-2026-ARXIV-2606-28116; SF-2026-ARXIV-2606-28128; SF-2026-ARXIV-2606-28153; SF-2026-ARXIV-2606-28166; SF-2026-ARXIV-2606-28187; SF-2026-ARXIV-2606-28235; SF-2026-ARXIV-2606-28276; SF-2026-ARXIV-2606-28277; SF-2026-ARXIV-2606-28279; SF-2026-ARXIV-2606-28322; SF-2026-ARXIV-2606-28430; SF-2026-ARXIV-2606-28433; SF-2026-ARXIV-2606-28434; SF-2026-ARXIV-2606-28436; SF-2026-ARXIV-2606-28438; SF-2026-ARXIV-2606-28455; SF-2026-ARXIV-2606-28471; SF-2026-ARXIV-2606-28479; SF-2026-ARXIV-2606-28480; SF-2026-ARXIV-2606-28514; SF-2026-ARXIV-2606-28529; SF-2026-ARXIV-2606-28551; SF-2026-ARXIV-2606-28560; SF-2026-ARXIV-2606-28562; SF-2026-ARXIV-2606-28565; SF-2026-ARXIV-2606-28574; SF-2026-ARXIV-2606-28615; SF-2026-ARXIV-2606-28639; SF-2026-ARXIV-2606-28649; SF-2026-ARXIV-2606-28661 | snapshots=32,040 records; pages=40; final_cursor=end | 2026-06-27T01:00:00Z | ../_sources/daily-20260627/screening-ledger.json; ../_sources/daily-20260627/denominator-full-semantic-audit-v1.tsv; coverage:SRC-ARXIV:20260627 | — |

<!-- coverage:SRC-ARXIV:20260627:start -->
Full-population reconciliation: 384 = 64 + 320; Core={'raw': 259, 'retained': 55, 'closure': 204}; keyword={'raw': 41, 'retained': 6, 'closure': 35}; route-negative={'raw': 84, 'retained': 3, 'closure': 81}. Keyword routing was recall-only; all 84 route negatives were semantically reviewed and 3 restored.
<!-- coverage:SRC-ARXIV:20260627:end -->

## 2. Candidate Ledger

<!-- validator:candidate-ledger-v2.1 -->
| Source Family ID | Primary Identifier | Event Identity | Owner Week | First-public Date | Supporting Source IDs | Design Delta | System Reach | Durability | Total | Candidate State | Review Status | Access Status | Review Override | Review Ref | Owner Report Ref | Prior Review Ref | Reconciliation | Stable Node ID | Books Disposition | Books Review Ref | Benchmark Claim |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2606-27632 | arXiv:2606.27632v1 | paper-v1:2606.27632 | 2026-W26 | 2026-06-26 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-27632 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-27632 | yes |
| SF-2026-ARXIV-2606-27634 | arXiv:2606.27634v1 | paper-v1:2606.27634 | 2026-W26 | 2026-06-26 | SRC-ARXIV | 2 | 1 | 2 | 5 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2606-27634 | self | — | new_in_window | PLATFORM-MONITORING | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-27634 | yes |
| SF-2026-ARXIV-2606-27650 | arXiv:2606.27650v1 | paper-v1:2606.27650 | 2026-W26 | 2026-06-26 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2606-27650 | self | — | new_in_window | AGENT-PLATFORM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-27650 | yes |
| SF-2026-ARXIV-2606-27669 | arXiv:2606.27669v1 | paper-v1:2606.27669 | 2026-W26 | 2026-06-26 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-27669 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-27669 | yes |
| SF-2026-ARXIV-2606-27679 | arXiv:2606.27679v1 | paper-v1:2606.27679 | 2026-W26 | 2026-06-26 | SRC-ARXIV | 2 | 1 | 2 | 5 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2606-27679 | self | — | new_in_window | PLATFORM-MONITORING | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-27679 | yes |
| SF-2026-ARXIV-2606-27681 | arXiv:2606.27681v1 | paper-v1:2606.27681 | 2026-W26 | 2026-06-26 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-27681 | self | — | new_in_window | MULTIMODAL-WORLD-MODELS | Integrate | books-review:SF-2026-ARXIV-2606-27681 | yes |
| SF-2026-ARXIV-2606-27683 | arXiv:2606.27683v1 | paper-v1:2606.27683 | 2026-W26 | 2026-06-26 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-27683 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-27683 | yes |
| SF-2026-ARXIV-2606-27704 | arXiv:2606.27704v1 | paper-v1:2606.27704 | 2026-W26 | 2026-06-26 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-27704 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-27704 | yes |
| SF-2026-ARXIV-2606-27709 | arXiv:2606.27709v1 | paper-v1:2606.27709 | 2026-W26 | 2026-06-26 | SRC-ARXIV | 2 | 1 | 2 | 5 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2606-27709 | self | — | new_in_window | TRAIN-DATA | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-27709 | yes |
| SF-2026-ARXIV-2606-27732 | arXiv:2606.27732v1 | paper-v1:2606.27732 | 2026-W26 | 2026-06-26 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-27732 | self | — | new_in_window | MULTIMODAL-GENERATIVE-PARADIGMS | Integrate | books-review:SF-2026-ARXIV-2606-27732 | yes |
| SF-2026-ARXIV-2606-27739 | arXiv:2606.27739v1 | paper-v1:2606.27739 | 2026-W26 | 2026-06-26 | SRC-ARXIV | 2 | 1 | 2 | 5 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2606-27739 | self | — | new_in_window | TRAIN-GRPO | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-27739 | yes |
| SF-2026-ARXIV-2606-27743 | arXiv:2606.27743v1 | paper-v1:2606.27743 | 2026-W26 | 2026-06-26 | SRC-ARXIV | 2 | 1 | 2 | 5 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2606-27743 | self | — | new_in_window | INFER-SCHEDULING | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-27743 | yes |
| SF-2026-ARXIV-2606-27757 | arXiv:2606.27757v1 | paper-v1:2606.27757 | 2026-W26 | 2026-06-26 | SRC-ARXIV | 2 | 1 | 2 | 5 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2606-27757 | self | — | new_in_window | AGENT-PLANNING | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-27757 | yes |
| SF-2026-ARXIV-2606-27780 | arXiv:2606.27780v1 | paper-v1:2606.27780 | 2026-W26 | 2026-06-26 | SRC-ARXIV | 2 | 1 | 2 | 5 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2606-27780 | self | — | new_in_window | MULTIMODAL-WORLD-MODELS | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-27780 | yes |
| SF-2026-ARXIV-2606-27791 | arXiv:2606.27791v1 | paper-v1:2606.27791 | 2026-W26 | 2026-06-26 | SRC-ARXIV | 2 | 1 | 2 | 5 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2606-27791 | self | — | new_in_window | MODEL-LONG-CONTEXT | Weekly Only — Context | — | yes |
| SF-2026-ARXIV-2606-27797 | arXiv:2606.27797v1 | paper-v1:2606.27797 | 2026-W26 | 2026-06-26 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-27797 | self | — | new_in_window | TRAIN-DISTRIBUTED-TRAINING | Integrate | books-review:SF-2026-ARXIV-2606-27797 | yes |
| SF-2026-ARXIV-2606-27806 | arXiv:2606.27806v1 | paper-v1:2606.27806 | 2026-W26 | 2026-06-26 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-27806 | self | — | new_in_window | AGENT-PLANNING | Integrate | books-review:SF-2026-ARXIV-2606-27806 | yes |
| SF-2026-ARXIV-2606-27814 | arXiv:2606.27814v1 | paper-v1:2606.27814 | 2026-W26 | 2026-06-26 | SRC-ARXIV | 2 | 1 | 2 | 5 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2606-27814 | self | — | new_in_window | TRAIN-GRPO | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-27814 | yes |
| SF-2026-ARXIV-2606-27826 | arXiv:2606.27826v1 | paper-v1:2606.27826 | 2026-W26 | 2026-06-26 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-27826 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-27826 | yes |
| SF-2026-ARXIV-2606-27841 | arXiv:2606.27841v1 | paper-v1:2606.27841 | 2026-W26 | 2026-06-26 | SRC-ARXIV | 3 | 1 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-27841 | self | — | new_in_window | PLATFORM-COST | Integrate | books-review:SF-2026-ARXIV-2606-27841 | yes |
| SF-2026-ARXIV-2606-27866 | arXiv:2606.27866v1 | paper-v1:2606.27866 | 2026-W26 | 2026-06-26 | SRC-ARXIV | 2 | 1 | 2 | 5 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2606-27866 | self | — | new_in_window | MODEL-MOE | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-27866 | yes |
| SF-2026-ARXIV-2606-27906 | arXiv:2606.27906v1 | paper-v1:2606.27906 | 2026-W26 | 2026-06-26 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-27906 | self | — | new_in_window | INFER-REQUEST-LIFECYCLE | Integrate | books-review:SF-2026-ARXIV-2606-27906 | yes |
| SF-2026-ARXIV-2606-27934 | arXiv:2606.27934v1 | paper-v1:2606.27934 | 2026-W26 | 2026-06-26 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-27934 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-27934 | yes |
| SF-2026-ARXIV-2606-27936 | arXiv:2606.27936v1 | paper-v1:2606.27936 | 2026-W26 | 2026-06-26 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-27936 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-27936 | yes |
| SF-2026-ARXIV-2606-27944 | arXiv:2606.27944v1 | paper-v1:2606.27944 | 2026-W26 | 2026-06-26 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-27944 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-27944 | yes |
| SF-2026-ARXIV-2606-27962 | arXiv:2606.27962v1 | paper-v1:2606.27962 | 2026-W26 | 2026-06-26 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2606-27962 | self | — | new_in_window | PLATFORM-FOUNDATIONS | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-27962 | yes |
| SF-2026-ARXIV-2606-27976 | arXiv:2606.27976v1 | paper-v1:2606.27976 | 2026-W26 | 2026-06-26 | SRC-ARXIV | 2 | 1 | 2 | 5 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2606-27976 | self | — | new_in_window | AGENT-RAG | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-27976 | yes |
| SF-2026-ARXIV-2606-27997 | arXiv:2606.27997v1 | paper-v1:2606.27997 | 2026-W26 | 2026-06-26 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-27997 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-27997 | yes |
| SF-2026-ARXIV-2606-28011 | arXiv:2606.28011v1 | paper-v1:2606.28011 | 2026-W26 | 2026-06-26 | SRC-ARXIV | 2 | 1 | 2 | 5 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2606-28011 | self | — | new_in_window | AGENT-WORKFLOW | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-28011 | yes |
| SF-2026-ARXIV-2606-28013 | arXiv:2606.28013v1 | paper-v1:2606.28013 | 2026-W26 | 2026-06-26 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-28013 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Integrate | books-review:SF-2026-ARXIV-2606-28013 | yes |
| SF-2026-ARXIV-2606-28037 | arXiv:2606.28037v1 | paper-v1:2606.28037 | 2026-W26 | 2026-06-26 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-28037 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-28037 | yes |
| SF-2026-ARXIV-2606-28050 | arXiv:2606.28050v1 | paper-v1:2606.28050 | 2026-W26 | 2026-06-26 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-28050 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-28050 | yes |
| SF-2026-ARXIV-2606-28061 | arXiv:2606.28061v1 | paper-v1:2606.28061 | 2026-W26 | 2026-06-26 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-28061 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-28061 | yes |
| SF-2026-ARXIV-2606-28070 | arXiv:2606.28070v1 | paper-v1:2606.28070 | 2026-W26 | 2026-06-26 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2606-28070 | self | — | new_in_window | PLATFORM-FOUNDATIONS | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-28070 | yes |
| SF-2026-ARXIV-2606-28116 | arXiv:2606.28116v1 | paper-v1:2606.28116 | 2026-W26 | 2026-06-26 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-28116 | self | — | new_in_window | PLATFORM-MONITORING | Integrate | books-review:SF-2026-ARXIV-2606-28116 | yes |
| SF-2026-ARXIV-2606-28128 | arXiv:2606.28128v1 | paper-v1:2606.28128 | 2026-W26 | 2026-06-26 | SRC-ARXIV | 2 | 1 | 2 | 5 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2606-28128 | self | — | new_in_window | MULTIMODAL-WORLD-MODELS | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-28128 | yes |
| SF-2026-ARXIV-2606-28153 | arXiv:2606.28153v1 | paper-v1:2606.28153 | 2026-W26 | 2026-06-26 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-28153 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-28153 | yes |
| SF-2026-ARXIV-2606-28166 | arXiv:2606.28166v1 | paper-v1:2606.28166 | 2026-W26 | 2026-06-26 | SRC-ARXIV | 2 | 1 | 2 | 5 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2606-28166 | self | — | new_in_window | TRAIN-GRPO | Weekly Only — Context | — | yes |
| SF-2026-ARXIV-2606-28187 | arXiv:2606.28187v1 | paper-v1:2606.28187 | 2026-W26 | 2026-06-26 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2606-28187 | self | — | new_in_window | AGENT-MULTI-AGENT | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-28187 | yes |
| SF-2026-ARXIV-2606-28235 | arXiv:2606.28235v1 | paper-v1:2606.28235 | 2026-W26 | 2026-06-26 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2606-28235 | self | — | new_in_window | AGENT-PLATFORM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-28235 | yes |
| SF-2026-ARXIV-2606-28276 | arXiv:2606.28276v1 | paper-v1:2606.28276 | 2026-W26 | 2026-06-26 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-28276 | self | — | new_in_window | MULTIMODAL-EMBODIED-VLA | Integrate | books-review:SF-2026-ARXIV-2606-28276 | yes |
| SF-2026-ARXIV-2606-28277 | arXiv:2606.28277v1 | paper-v1:2606.28277 | 2026-W26 | 2026-06-26 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-28277 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-28277 | yes |
| SF-2026-ARXIV-2606-28279 | arXiv:2606.28279v1 | paper-v1:2606.28279 | 2026-W26 | 2026-06-26 | SRC-ARXIV | 2 | 1 | 2 | 5 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2606-28279 | self | — | new_in_window | AGENT-WORKFLOW | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-28279 | yes |
| SF-2026-ARXIV-2606-28322 | arXiv:2606.28322v1 | paper-v1:2606.28322 | 2026-W26 | 2026-06-26 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-28322 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-28322 | yes |
| SF-2026-ARXIV-2606-28430 | arXiv:2606.28430v1 | paper-v1:2606.28430 | 2026-W26 | 2026-06-26 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-28430 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-28430 | yes |
| SF-2026-ARXIV-2606-28433 | arXiv:2606.28433v1 | paper-v1:2606.28433 | 2026-W26 | 2026-06-26 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-28433 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-28433 | yes |
| SF-2026-ARXIV-2606-28434 | arXiv:2606.28434v1 | paper-v1:2606.28434 | 2026-W26 | 2026-06-26 | SRC-ARXIV | 2 | 1 | 2 | 5 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2606-28434 | self | — | new_in_window | AGENT-MEMORY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-28434 | yes |
| SF-2026-ARXIV-2606-28436 | arXiv:2606.28436v1 | paper-v1:2606.28436 | 2026-W26 | 2026-06-26 | SRC-ARXIV | 2 | 1 | 2 | 5 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2606-28436 | self | — | new_in_window | TRAIN-GRPO | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-28436 | yes |
| SF-2026-ARXIV-2606-28438 | arXiv:2606.28438v1 | paper-v1:2606.28438 | 2026-W26 | 2026-06-26 | SRC-ARXIV | 2 | 1 | 2 | 5 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2606-28438 | self | — | new_in_window | TRAIN-DATA | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-28438 | yes |
| SF-2026-ARXIV-2606-28455 | arXiv:2606.28455v1 | paper-v1:2606.28455 | 2026-W26 | 2026-06-26 | SRC-ARXIV | 2 | 1 | 2 | 5 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2606-28455 | self | — | new_in_window | MULTIMODAL-WORLD-MODELS | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-28455 | yes |
| SF-2026-ARXIV-2606-28471 | arXiv:2606.28471v1 | paper-v1:2606.28471 | 2026-W26 | 2026-06-26 | SRC-ARXIV | 2 | 1 | 2 | 5 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2606-28471 | self | — | new_in_window | TRAIN-DATA | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-28471 | yes |
| SF-2026-ARXIV-2606-28479 | arXiv:2606.28479v1 | paper-v1:2606.28479 | 2026-W26 | 2026-06-26 | SRC-ARXIV | 3 | 1 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-28479 | self | — | new_in_window | TRAIN-LORA | Integrate | books-review:SF-2026-ARXIV-2606-28479 | yes |
| SF-2026-ARXIV-2606-28480 | arXiv:2606.28480v1 | paper-v1:2606.28480 | 2026-W26 | 2026-06-26 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-28480 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-28480 | yes |
| SF-2026-ARXIV-2606-28514 | arXiv:2606.28514v1 | paper-v1:2606.28514 | 2026-W26 | 2026-06-26 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2606-28514 | self | — | new_in_window | AGENT-MULTI-AGENT | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-28514 | yes |
| SF-2026-ARXIV-2606-28529 | arXiv:2606.28529v1 | paper-v1:2606.28529 | 2026-W26 | 2026-06-26 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-28529 | self | — | new_in_window | INFER-REQUEST-LIFECYCLE | Integrate | books-review:SF-2026-ARXIV-2606-28529 | yes |
| SF-2026-ARXIV-2606-28551 | arXiv:2606.28551v1 | paper-v1:2606.28551 | 2026-W26 | 2026-06-26 | SRC-ARXIV | 2 | 1 | 2 | 5 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2606-28551 | self | — | new_in_window | TRAIN-DATA | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-28551 | yes |
| SF-2026-ARXIV-2606-28560 | arXiv:2606.28560v1 | paper-v1:2606.28560 | 2026-W26 | 2026-06-26 | SRC-ARXIV | 2 | 1 | 2 | 5 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2606-28560 | self | — | new_in_window | MODEL-LONG-CONTEXT | Weekly Only — Context | — | yes |
| SF-2026-ARXIV-2606-28562 | arXiv:2606.28562v1 | paper-v1:2606.28562 | 2026-W26 | 2026-06-26 | SRC-ARXIV | 2 | 1 | 2 | 5 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2606-28562 | self | — | new_in_window | TRAIN-GRPO | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-28562 | yes |
| SF-2026-ARXIV-2606-28565 | arXiv:2606.28565v1 | paper-v1:2606.28565 | 2026-W26 | 2026-06-26 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-28565 | self | — | new_in_window | INFER-REQUEST-LIFECYCLE | Integrate | books-review:SF-2026-ARXIV-2606-28565 | yes |
| SF-2026-ARXIV-2606-28574 | arXiv:2606.28574v1 | paper-v1:2606.28574 | 2026-W26 | 2026-06-26 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-28574 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-28574 | yes |
| SF-2026-ARXIV-2606-28615 | arXiv:2606.28615v1 | paper-v1:2606.28615 | 2026-W26 | 2026-06-26 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-28615 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-28615 | yes |
| SF-2026-ARXIV-2606-28639 | arXiv:2606.28639v1 | paper-v1:2606.28639 | 2026-W26 | 2026-06-26 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-28639 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-28639 | yes |
| SF-2026-ARXIV-2606-28649 | arXiv:2606.28649v1 | paper-v1:2606.28649 | 2026-W26 | 2026-06-26 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-28649 | self | — | new_in_window | PLATFORM-SECURITY | Integrate | books-review:SF-2026-ARXIV-2606-28649 | yes |
| SF-2026-ARXIV-2606-28661 | arXiv:2606.28661v1 | paper-v1:2606.28661 | 2026-W26 | 2026-06-26 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-28661 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Integrate | books-review:SF-2026-ARXIV-2606-28661 | yes |

## 3. Review Completion Receipt

<!-- validator:review-completion-v1 -->
| Source Family ID | Review Provenance ID | Review Route | Primary Evidence Version | Reviewed Evidence Versions | Method / Identity Locators | Evaluation Locators | Limitations / Counterevidence Locators | Artifact Locators | Claim Boundary Ref | Completion Result |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2606-27632 | RP-fcbc4265f52dcdfb | deep | arXiv:2606.27632v1 | SRC-ARXIV@arXiv:2606.27632v1 | https://arxiv.org/html/2606.27632v1 — §2 Content-Safety-Oriented Data System; 3 Yuvion LLM: Progressive Safety Training Paradigm; 3.2 Target Capability Design | https://arxiv.org/html/2606.27632v1 — §4 Evaluation Framework; 4.2 Level 1: Open-source General Benchmarks; 4.3 Level 2: Open-source Content Safety Benchmarks | https://arxiv.org/html/2606.27632v1 — §Discussion.; 9 Conclusion; 10 Limitations and Future Work | Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review | claim:SF-2026-ARXIV-2606-27632 | complete |
| SF-2026-ARXIV-2606-27634 | RP-75996c215715c982 | standard | arXiv:2606.27634v1 | SRC-ARXIV@arXiv:2606.27634v1 | https://arxiv.org/html/2606.27634v1 — §4.0.4 Training Procedure | https://arxiv.org/html/2606.27634v1 — §Continual Learning for Sequential Personalization of Small Language Models: A Stability Monitoring Analysis; 2.0.1 Continual Learning and Evaluation of Language Models.; 3.2 Model Checkpoints and Evaluation | https://arxiv.org/html/2606.27634v1 — §6 Conclusion; 6.0.1 Limitations | Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review | claim:SF-2026-ARXIV-2606-27634 | complete |
| SF-2026-ARXIV-2606-27650 | RP-ef58e045338123ab | standard | arXiv:2606.27650v1 | SRC-ARXIV@arXiv:2606.27650v1 | https://arxiv.org/html/2606.27650v1 — §Context Design and Coverage; 6 Platform Architecture; 6.1 System Overview | https://arxiv.org/html/2606.27650v1 — §7 Evaluation Cases and Scalability; 7.1 Evaluation Cases; 7.1.5 Scalability Analysis | https://arxiv.org/html/2606.27650v1 — §8 Discussion; Limitations and Future Work; 9 Conclusion | Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review | claim:SF-2026-ARXIV-2606-27650 | complete |
| SF-2026-ARXIV-2606-27669 | RP-ceffdfb9a0b8de47 | deep | arXiv:2606.27669v1 | SRC-ARXIV@arXiv:2606.27669v1 | https://arxiv.org/html/2606.27669v1 — §4 Methodology of Dataset Construction; Benchmark Design and Methodology.; Evaluation Framework and User Simulator. | https://arxiv.org/html/2606.27669v1 — §2.1 Web Search Benchmark; 2.2 Ambiguity Benchmark; 2.3 Interactive Clarification Benchmark | https://arxiv.org/html/2606.27669v1 — §Search-heavy guessing reveals a major failure mode.; 6 Conclusion; Limitations | Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review | claim:SF-2026-ARXIV-2606-27669 | complete |
| SF-2026-ARXIV-2606-27679 | RP-f4a08ba2915c4ee6 | standard | arXiv:2606.27679v1 | SRC-ARXIV@arXiv:2606.27679v1 | https://arxiv.org/html/2606.27679v1 — §Probe Training.; Probe Architecture and Training Size. | https://arxiv.org/html/2606.27679v1 — §Toolkits, Benchmarks, and Evaluation.; 3.1 Experimental Setup; Evaluation Metrics. | https://arxiv.org/html/2606.27679v1 — §4.2 Results and Discussion; 5 Conclusion; Limitations | Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review | claim:SF-2026-ARXIV-2606-27679 | complete |
| SF-2026-ARXIV-2606-27681 | RP-856e55a15de3a886 | deep | arXiv:2606.27681v1 | SRC-ARXIV@arXiv:2606.27681v1 | https://arxiv.org/html/2606.27681v1 — §Proposition 2 (Non-identifiability under leaky architectures) .; Proposition 3 (Training–inference consistency) .; 4.2 Model Architecture | https://arxiv.org/html/2606.27681v1 — §2 Problem Setup: Text Based POMDPs; 5 Experimental Evaluation; 5.3 Evaluation Metrics | https://arxiv.org/html/2606.27681v1 — §7 Conclusion | Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review | claim:SF-2026-ARXIV-2606-27681 | complete |
| SF-2026-ARXIV-2606-27683 | RP-9a69aabca4d4421b | deep | arXiv:2606.27683v1 | SRC-ARXIV@arXiv:2606.27683v1 | https://arxiv.org/html/2606.27683v1 — §III Preliminaries and Framework; III-A White-Box and Gray-Box Unlearning Methods; III-B API-Only Scenario and Proposed Framework | https://arxiv.org/html/2606.27683v1 — §VI Experiments; VI-A Experimental Setup; VI-B Performance Evaluation | https://arxiv.org/html/2606.27683v1 — §VII Conclusion | Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review | claim:SF-2026-ARXIV-2606-27683 | complete |
| SF-2026-ARXIV-2606-27704 | RP-eab38e6ee494e401 | deep | arXiv:2606.27704v1 | SRC-ARXIV@arXiv:2606.27704v1 | https://arxiv.org/html/2606.27704v1 — §IV AdvScan Algorithm; V-A 3 Adversarial Examples (AE) Generation Methodologies; V-C Evaluation of the AdvScan Algorithm | https://arxiv.org/html/2606.27704v1 — §AdvScan: Black-Box Adversarial Example Detection at Runtime through Power Analysis; II-D Power Analysis; II-E Side Channel Analysis for Adversarial Behavior Detection | https://arxiv.org/html/2606.27704v1 — §II-F Threat Model; IV-D Discussion of Merits and Limitations of AdvScan; VI Conclusion | Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review | claim:SF-2026-ARXIV-2606-27704 | complete |
| SF-2026-ARXIV-2606-27709 | RP-c82291588b7aaac8 | standard | arXiv:2606.27709v1 | SRC-ARXIV@arXiv:2606.27709v1 | https://arxiv.org/html/2606.27709v1 — §3 Methods; 3.2 Study design; 3.3 Training data and data construction | https://arxiv.org/html/2606.27709v1 — §Experiment 1.; Experiment 2.; Experiment 3. | https://arxiv.org/html/2606.27709v1 — §5 Discussion; Limitations | Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review | claim:SF-2026-ARXIV-2606-27709 | complete |
| SF-2026-ARXIV-2606-27732 | RP-eb6d768fc8c67a93 | deep | arXiv:2606.27732v1 | SRC-ARXIV@arXiv:2606.27732v1 | https://arxiv.org/html/2606.27732v1 — §3 Method; 3.4 R2LM Architecture; 3.5 Training and Inference | https://arxiv.org/html/2606.27732v1 — §4 Experiments; 4.1 Experimental Setup; 4.2 Main Results: Multiple-Choice Benchmarks | https://arxiv.org/html/2606.27732v1 — §5 Conclusion | Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review | claim:SF-2026-ARXIV-2606-27732 | complete |
| SF-2026-ARXIV-2606-27739 | RP-8b16b5a26e2e32be | standard | arXiv:2606.27739v1 | SRC-ARXIV@arXiv:2606.27739v1 | https://arxiv.org/html/2606.27739v1 — §4 Method; C.2 PRM Training Details; Model architecture. | https://arxiv.org/html/2606.27739v1 — §3 Analysis; 3.3 Theoretical Analysis; 5 Experiments | https://arxiv.org/html/2606.27739v1 — §6 Conclusion; Limitations; B.7 Discussion | Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review | claim:SF-2026-ARXIV-2606-27739 | complete |
| SF-2026-ARXIV-2606-27743 | RP-50afd2df11e5cd81 | standard | arXiv:2606.27743v1 | SRC-ARXIV@arXiv:2606.27743v1 | https://arxiv.org/html/2606.27743v1 — §3 Methodology; 3.5 Training and Inference | https://arxiv.org/html/2606.27743v1 — §4 Experiments; 4.1 Experimental Setup; 4.2 Main Results | https://arxiv.org/html/2606.27743v1 — §4.6 Discussion and Limitations; 5 Conclusion | Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review | claim:SF-2026-ARXIV-2606-27743 | complete |
| SF-2026-ARXIV-2606-27757 | RP-ccd06f48cc8dc834 | standard | arXiv:2606.27757v1 | SRC-ARXIV@arXiv:2606.27757v1 | https://arxiv.org/html/2606.27757v1 — §Towards Reliable and Robust LLM Planning: A Symbolic Feedback-Driven Iterative Self-Refinement Framework Thanks: * Corresponding author at: Institute of Automation, Chinese Academy of Sciences, Beijing, China.; III METHODOLOGY; III-B Feedback-Driven Iterative Self-Refinement Framework | https://arxiv.org/html/2606.27757v1 — §IV EXPERIMENTS; IV-A Experimental Settings; IV-D Analysis of Planning Length | https://arxiv.org/html/2606.27757v1 — §V CONCLUSION | Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review | claim:SF-2026-ARXIV-2606-27757 | complete |
| SF-2026-ARXIV-2606-27780 | RP-183a200d4042495f | standard | arXiv:2606.27780v1 | SRC-ARXIV@arXiv:2606.27780v1 | https://arxiv.org/html/2606.27780v1 — §Agent graphs and skill-graph systems.; 3 Graph World Model Framework; Framework overview. | https://arxiv.org/html/2606.27780v1 — §5 Dataset and Evaluation Protocol; Graph world model setup.; 7 Experiments | https://arxiv.org/html/2606.27780v1 — §7.2.3 Global spectral amplification differs from local hub failure; 7.5.4 OOD perturbation confirms the FE contraction boundary; 7.6.2 Role-dependent failure sensitivity | Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review | claim:SF-2026-ARXIV-2606-27780 | complete |
| SF-2026-ARXIV-2606-27791 | RP-5277f4acb2dfb798 | standard | arXiv:2606.27791v1 | SRC-ARXIV@arXiv:2606.27791v1 | https://arxiv.org/html/2606.27791v1 — §NLL-Guided Full-Attention Layer Selection for Training-Free Sliding-Window Adaptation; 3 Method | https://arxiv.org/html/2606.27791v1 — §4 Experiments; 4.1 Experimental Setup; 4.2 Main Results | https://arxiv.org/html/2606.27791v1 — §5 Conclusion | Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review | claim:SF-2026-ARXIV-2606-27791 | complete |
| SF-2026-ARXIV-2606-27797 | RP-4df54364f89af0a2 | deep | arXiv:2606.27797v1 | SRC-ARXIV@arXiv:2606.27797v1 | https://arxiv.org/html/2606.27797v1 — §Optimizing Teacher-Student Partitioning for Scalable Knowledge Distillation on HPC Systems; 2 Background: LLM Training and Parallelism; 2.1 LLM Training | https://arxiv.org/html/2606.27797v1 — §3 Testing Setup; 4 GKD Analysis and Improvements; 4.1 Experimental Results | https://arxiv.org/html/2606.27797v1 — §6 Conclusions | Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review | claim:SF-2026-ARXIV-2606-27797 | complete |
| SF-2026-ARXIV-2606-27806 | RP-c3ab9602bc243f16 | deep | arXiv:2606.27806v1 | SRC-ARXIV@arXiv:2606.27806v1 | https://arxiv.org/html/2606.27806v1 — §Our approach: GILP.; LLM API ecosystem.; 4 Method: Grounded Iterative Language Planning | https://arxiv.org/html/2606.27806v1 — §5 Experiments; Setup.; Cost analysis. | https://arxiv.org/html/2606.27806v1 — §6 Discussion; 7 Limitations; 8 Conclusion | Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review | claim:SF-2026-ARXIV-2606-27806 | complete |
| SF-2026-ARXIV-2606-27814 | RP-435b3d0c09213e9a | standard | arXiv:2606.27814v1 | SRC-ARXIV@arXiv:2606.27814v1 | https://arxiv.org/html/2606.27814v1 — §4 Method; 5.4 Training Dynamics and Diagnostic Metrics; Appendix A Method and Algorithmic Details | https://arxiv.org/html/2606.27814v1 — §5 Experiments; 5.1 Experimental Setup; Datasets & Benchmarks. | https://arxiv.org/html/2606.27814v1 — §6 Conclusion | Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review | claim:SF-2026-ARXIV-2606-27814 | complete |
| SF-2026-ARXIV-2606-27826 | RP-264745a51e7b122d | deep | arXiv:2606.27826v1 | SRC-ARXIV@arXiv:2606.27826v1 | https://arxiv.org/html/2606.27826v1 — §3.1 Benchmark Design; Appendix F NormPerceptor Training Data Details | https://arxiv.org/html/2606.27826v1 — §NormAct : A Benchmark for Hidden Social Norm Compliance in Embodied Planning; 2.1 Social Norm Evaluation in (M)LLMs; 3 The NormAct Benchmark | https://arxiv.org/html/2606.27826v1 — §7 Conclusion; Limitations | Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review | claim:SF-2026-ARXIV-2606-27826 | complete |
| SF-2026-ARXIV-2606-27841 | RP-274a4d92ab6f68ca | deep | arXiv:2606.27841v1 | SRC-ARXIV@arXiv:2606.27841v1 | https://arxiv.org/html/2606.27841v1 — §3 Methodology and Experimental Set-up; 3.2 Layer-Wise Energy Estimation Framework | https://arxiv.org/html/2606.27841v1 — §3 Methodology and Experimental Set-up; 3.1 Experimental Protocol; 4 Results | https://arxiv.org/html/2606.27841v1 — §5 Discussion; 6 Conclusion | Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review | claim:SF-2026-ARXIV-2606-27841 | complete |
| SF-2026-ARXIV-2606-27866 | RP-20466c85fa2228a3 | standard | arXiv:2606.27866v1 | SRC-ARXIV@arXiv:2606.27866v1 | https://arxiv.org/html/2606.27866v1 — §3 Method; Clip FFN Forward Kernel Co-Design.; Toward Co-Designed Online Budget Scheduling. | https://arxiv.org/html/2606.27866v1 — §4 Experiments; 4.1 Experimental Setup; Implementation Details and Evaluation Tasks. | https://arxiv.org/html/2606.27866v1 — §5 Conclusion; Limitations and Future Works.; A.2 Additional Discussion on Cross-Budget Transfer and Cross-Model Trends | Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review | claim:SF-2026-ARXIV-2606-27866 | complete |
| SF-2026-ARXIV-2606-27906 | RP-f018813c97ac966b | deep | arXiv:2606.27906v1 | SRC-ARXIV@arXiv:2606.27906v1 | https://arxiv.org/html/2606.27906v1 — §7.2. Methodology and Outcomes on Phi-3.5-V | https://arxiv.org/html/2606.27906v1 — §2. Platform and Experimental Setup; 3.1. Phase-Level Results; 6.1. Three-Backend Benchmark | https://arxiv.org/html/2606.27906v1 — §8. Discussion; 10. Conclusion | Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review | claim:SF-2026-ARXIV-2606-27906 | complete |
| SF-2026-ARXIV-2606-27934 | RP-b387c14574be17ea | deep | arXiv:2606.27934v1 | SRC-ARXIV@arXiv:2606.27934v1 | https://arxiv.org/html/2606.27934v1 — §Approach. | https://arxiv.org/html/2606.27934v1 — §Self-Verifying Measurement Records: Hash-Linked Evidence Graphs for Hardware Benchmarking | https://arxiv.org/html/2606.27934v1 — §10 Threat model and guarantees; 12 Physical stress and the trust boundary; 14 Scope and limitations | Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review | claim:SF-2026-ARXIV-2606-27934 | complete |
| SF-2026-ARXIV-2606-27936 | RP-45f8de32ae80c0d8 | deep | arXiv:2606.27936v1 | SRC-ARXIV@arXiv:2606.27936v1 | https://arxiv.org/html/2606.27936v1 — §3 Methodology; 3.2 Study Design and Simulated Data | https://arxiv.org/html/2606.27936v1 — §4 Results | https://arxiv.org/html/2606.27936v1 — §Agentic AI-Powered Re-Identification: An Emerging, Scalable Threat to Mobility Microdata Privacy; Threat model.; 5 Discussion and Conclusion | Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review | claim:SF-2026-ARXIV-2606-27936 | complete |
| SF-2026-ARXIV-2606-27944 | RP-75221d7997b0d453 | deep | arXiv:2606.27944v1 | SRC-ARXIV@arXiv:2606.27944v1 | https://arxiv.org/html/2606.27944v1 — §4 Misuse Collection and the Awareness-to-Action Evaluation Framework; 4.3 Evaluation Framework | https://arxiv.org/html/2606.27944v1 — §4 Misuse Collection and the Awareness-to-Action Evaluation Framework; 4.3 Evaluation Framework; 5 Evaluation Results | https://arxiv.org/html/2606.27944v1 — §3 Threat Model; 8 Discussion and Limitation; 9 Conclusion | Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review | claim:SF-2026-ARXIV-2606-27944 | complete |
| SF-2026-ARXIV-2606-27962 | RP-22dc06642d188f8b | standard | arXiv:2606.27962v1 | SRC-ARXIV@arXiv:2606.27962v1 | https://arxiv.org/html/2606.27962v1 — §Building a Scalable, Reproducible, Evaluatable, and Closed-Loop Simulation Environment Foundation for Embodied Intelligence Cloud-Native Simulation Infrastructure for Embodied Intelligence Training, Evaluation, and Data Collection; 2 Overall Positioning and Design Principles; 2.3 Design Principles | https://arxiv.org/html/2606.27962v1 — §Building a Scalable, Reproducible, Evaluatable, and Closed-Loop Simulation Environment Foundation for Embodied Intelligence Cloud-Native Simulation Infrastructure for Embodied Intelligence Training, Evaluation, and Data Collection; 1.2 Bottlenecks in Real Robot Data and Evaluation; 3.2 Mainstream Benchmarks and Datasets | https://arxiv.org/html/2606.27962v1 — §3.3 Limitations of Current Solutions; 6.5 Failure Data and Corrective Data | Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review | claim:SF-2026-ARXIV-2606-27962 | complete |
| SF-2026-ARXIV-2606-27976 | RP-161e1684a0ac6eaa | standard | arXiv:2606.27976v1 | SRC-ARXIV@arXiv:2606.27976v1 | https://arxiv.org/html/2606.27976v1 — §Appendix A Reproduced baseline analyses from the global-linear system | https://arxiv.org/html/2606.27976v1 — §8 Experiments; Integral multi-encoder evaluation at 10 6 10^{6} scale. | https://arxiv.org/html/2606.27976v1 — §3 Threat Model; A measured limitation: overlap reference lookup.; 9 Discussion | Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review | claim:SF-2026-ARXIV-2606-27976 | complete |
| SF-2026-ARXIV-2606-27997 | RP-816d86e3849e0ca0 | deep | arXiv:2606.27997v1 | SRC-ARXIV@arXiv:2606.27997v1 | https://arxiv.org/html/2606.27997v1 — §5.1. Evaluation methodology; Recommender Systems.; Recommender Systems | https://arxiv.org/html/2606.27997v1 — §Benchmarking on Tasks That Matter: Dataset Selection for Preserving Model Rankings; Benchmark Setting; Theoretical results summary | https://arxiv.org/html/2606.27997v1 — §7. Conclusions and discussion | Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review | claim:SF-2026-ARXIV-2606-27997 | complete |
| SF-2026-ARXIV-2606-28011 | RP-b5c754ca86619d68 | standard | arXiv:2606.28011v1 | SRC-ARXIV@arXiv:2606.28011v1 | https://arxiv.org/html/2606.28011v1 — §3 LLM-based agentic framework for fault-tolerant control | https://arxiv.org/html/2606.28011v1 — §4.3 Evaluation criteria; 5 Results; 5.1 Mixing module results | https://arxiv.org/html/2606.28011v1 — §6 Discussion | Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review | claim:SF-2026-ARXIV-2606-28011 | complete |
| SF-2026-ARXIV-2606-28013 | RP-ff54311f4759385a | deep | arXiv:2606.28013v1 | SRC-ARXIV@arXiv:2606.28013v1 | https://arxiv.org/html/2606.28013v1 — §Methods.; 5.1 Per-method cell decomposition; 5.4 A predictive regularity: stratum-rates are method-invariant | https://arxiv.org/html/2606.28013v1 — §4 Experimental Setup; 5 Experimental Results and Analysis | https://arxiv.org/html/2606.28013v1 — §6 Discussion and Limitations; 7 Conclusion | Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review | claim:SF-2026-ARXIV-2606-28013 | complete |
| SF-2026-ARXIV-2606-28037 | RP-e4c56ec741d0b7c3 | deep | arXiv:2606.28037v1 | SRC-ARXIV@arXiv:2606.28037v1 | https://arxiv.org/html/2606.28037v1 — §Evolution-Aware Regression Test Prioritization of ML-Enabled Systems Using Gradient-Based Behavior Vectors; 4.1.1. Tasks, Datasets, and Model Architectures | https://arxiv.org/html/2606.28037v1 — §4. Evaluation; 4.1. Experiment Setup; 4.1.5. Reproducibility and Additional Results | https://arxiv.org/html/2606.28037v1 — §5. Discussion; 5.3. Limitations; 6. Threats to Validity | Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review | claim:SF-2026-ARXIV-2606-28037 | complete |
| SF-2026-ARXIV-2606-28050 | RP-8b0774eecb4ded05 | deep | arXiv:2606.28050v1 | SRC-ARXIV@arXiv:2606.28050v1 | https://arxiv.org/html/2606.28050v1 — §3 Methodology; Hard-negative generation for evaluator training.; LoRA training budget. | https://arxiv.org/html/2606.28050v1 — §Generation–evaluation asymmetry.; 3.1 Task Asymmetry Analysis; Evaluation task ( 𝒯 eval \mathcal{T}_{\text{eval}} ). | https://arxiv.org/html/2606.28050v1 — §5 Results and Discussion; 6 Conclusion; Limitations | Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review | claim:SF-2026-ARXIV-2606-28050 | complete |
| SF-2026-ARXIV-2606-28061 | RP-c941eb9693e60137 | deep | arXiv:2606.28061v1 | SRC-ARXIV@arXiv:2606.28061v1 | https://arxiv.org/html/2606.28061v1 — §4.7 System Modules | https://arxiv.org/html/2606.28061v1 — §ToolPrivacyBench: Benchmarking Purpose-Bound Privacy in Tool-Using LLM Agents Note: This work was supported by the Beijing Advanced Innovation Center for Future Blockchain and Privacy Computing (GJJ-25-009).; 2.1 Privacy Evaluation of Large Language Models; 2.2 Tool-Using Agents and Agent Benchmarks | https://arxiv.org/html/2606.28061v1 — §8 Representative Failure Cases; 9 Discussion and Implications; 10 Conclusion | Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review | claim:SF-2026-ARXIV-2606-28061 | complete |
| SF-2026-ARXIV-2606-28070 | RP-4296b82eda3d243f | standard | arXiv:2606.28070v1 | SRC-ARXIV@arXiv:2606.28070v1 | https://arxiv.org/html/2606.28070v1 — §2 Architecture Overview; 3.1 Method Overview; 3.2.2 Algorithm-driven ontology growth (bottom-up) | https://arxiv.org/html/2606.28070v1 — §3.3 Results; 4.2.3 Results; Module 1: Data evaluation. | https://arxiv.org/html/2606.28070v1 — §9 Conclusion; 10 Limitations and Future Work | Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review | claim:SF-2026-ARXIV-2606-28070 | complete |
| SF-2026-ARXIV-2606-28116 | RP-877f1c28dc3cdce2 | deep | arXiv:2606.28116v1 | SRC-ARXIV@arXiv:2606.28116v1 | https://arxiv.org/html/2606.28116v1 — §Mechanism-Driven Monitors for Preemptive Detection of LLM Training Instability; Training-stability monitors.; 5 Designing Module-Specific Monitors from First Principles | https://arxiv.org/html/2606.28116v1 — §Mechanism-Driven Monitors for Preemptive Detection of LLM Training Instability; 1 Introduction | https://arxiv.org/html/2606.28116v1 — §6 Limitations; 7 Conclusion | Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review | claim:SF-2026-ARXIV-2606-28116 | complete |
| SF-2026-ARXIV-2606-28128 | RP-37d91892793bd718 | standard | arXiv:2606.28128v1 | SRC-ARXIV@arXiv:2606.28128v1 | https://arxiv.org/html/2606.28128v1 — §3 Method; 3.4 Training and Inference; Training data. | https://arxiv.org/html/2606.28128v1 — §4 Experiments; 4.1 Experimental Setup; Benchmarks. | https://arxiv.org/html/2606.28128v1 — §5 Conclusion; Appendix F Limitations and future work | Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review | claim:SF-2026-ARXIV-2606-28128 | complete |
| SF-2026-ARXIV-2606-28153 | RP-0c083d0c43178004 | deep | arXiv:2606.28153v1 | SRC-ARXIV@arXiv:2606.28153v1 | https://arxiv.org/html/2606.28153v1 — §Detection-based methods; Perturbation-based methods; Representation-based methods | https://arxiv.org/html/2606.28153v1 — §4 Experiments; 4.1 Experimental Setup; Experimental Design | https://arxiv.org/html/2606.28153v1 — §6 Conclusion; Conclusions and practical guidance.; B.3 Limitations and Future Directions | Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review | claim:SF-2026-ARXIV-2606-28153 | complete |
| SF-2026-ARXIV-2606-28166 | RP-16a24106681be088 | standard | arXiv:2606.28166v1 | SRC-ARXIV@arXiv:2606.28166v1 | https://arxiv.org/html/2606.28166v1 — §3.1 Preliminaries: tandem training; 5.1 Training dynamics of TRL | https://arxiv.org/html/2606.28166v1 — §4 Results; 4.1 Experimental setup; Appendix B Additional Results | https://arxiv.org/html/2606.28166v1 — §5 Discussion; 6 Conclusion | Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review | claim:SF-2026-ARXIV-2606-28166 | complete |
| SF-2026-ARXIV-2606-28187 | RP-feea63dcbfbd1558 | standard | arXiv:2606.28187v1 | SRC-ARXIV@arXiv:2606.28187v1 | https://arxiv.org/html/2606.28187v1 — §GBC: Gradient-Based Connections for Optimizing Multi-Agent Systems; 2.2 Multi-Agent System; 2.3 Multi-Agent System Optimization | https://arxiv.org/html/2606.28187v1 — §5 Experiment; Setup; Optimization Setup | https://arxiv.org/html/2606.28187v1 — §6 Conclusion; Limitations | Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review | claim:SF-2026-ARXIV-2606-28187 | complete |
| SF-2026-ARXIV-2606-28235 | RP-c88d6aafa0eb9682 | standard | arXiv:2606.28235v1 | SRC-ARXIV@arXiv:2606.28235v1 | https://arxiv.org/html/2606.28235v1 — §Govern the Repository, Not the Agent: Measuring Ecosystem-Level Risk in AI-Native Software; II-C Software ecosystems and coordination cost; II-D Emergence and complex adaptive systems | https://arxiv.org/html/2606.28235v1 — §IV-B Level of analysis and why multilevel models; V Results | https://arxiv.org/html/2606.28235v1 — §VI Discussion; VII Threats to Validity; VIII Conclusion | Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review | claim:SF-2026-ARXIV-2606-28235 | complete |
| SF-2026-ARXIV-2606-28276 | RP-e01698a305212ce3 | deep | arXiv:2606.28276v1 | SRC-ARXIV@arXiv:2606.28276v1 | https://arxiv.org/html/2606.28276v1 — §SimFoundry outperforms state-of-the-art simulation evaluation frameworks and makes fewer assumptions.; 5.2 Sim-to-Real Policy Training; Co-training with sim and real data further improves performance. | https://arxiv.org/html/2606.28276v1 — §SimFoundry: Modular and Automated Scene Generation for Policy Learning and Evaluation; 5 Experiments; 5.1 Real-to-Sim Policy Evaluation | https://arxiv.org/html/2606.28276v1 — §6 Limitations; 7 Conclusion; Appendix C Limitations | Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review | claim:SF-2026-ARXIV-2606-28276 | complete |
| SF-2026-ARXIV-2606-28277 | RP-16cc254bac4c05d0 | deep | arXiv:2606.28277v1 | SRC-ARXIV@arXiv:2606.28277v1 | https://arxiv.org/html/2606.28277v1 — §Design Considerations. | https://arxiv.org/html/2606.28277v1 — §2.1. Case Study: Verification of Retracted Papers in the SPOT Benchmark; 3. PAT Experimental Programs at STOC and ICML; 3.1. Quantitative Author Feedback for PAT Experimental Programs | https://arxiv.org/html/2606.28277v1 — §5. Conclusion and Future Outlook | Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review | claim:SF-2026-ARXIV-2606-28277 | complete |
| SF-2026-ARXIV-2606-28279 | RP-584274718264c170 | standard | arXiv:2606.28279v1 | SRC-ARXIV@arXiv:2606.28279v1 | https://arxiv.org/html/2606.28279v1 — §Agentic Hardware Design as Repository-Level Code Evolution; Benchmarks for RTL design and verification.; 3 The HORIZON Framework | https://arxiv.org/html/2606.28279v1 — §Benchmarks for RTL design and verification.; 4 Experiments; Setup and protocol. | https://arxiv.org/html/2606.28279v1 — §4.3 Detailed discussion on test-generation tasks; 5 Discussion and Limitations; 6 Conclusion | Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review | claim:SF-2026-ARXIV-2606-28279 | complete |
| SF-2026-ARXIV-2606-28322 | RP-50a46bd07bd079cb | deep | arXiv:2606.28322v1 | SRC-ARXIV@arXiv:2606.28322v1 | https://arxiv.org/html/2606.28322v1 — §3.1 Design Criteria | https://arxiv.org/html/2606.28322v1 — §PerceptionRubrics: Calibrating Multimodal Evaluation to Human Perception; Visual Perception Benchmarks in MLLMs.; Evaluation of Image Captioning. | https://arxiv.org/html/2606.28322v1 — §6 Conclusion | Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review | claim:SF-2026-ARXIV-2606-28322 | complete |
| SF-2026-ARXIV-2606-28430 | RP-88f5ade44eedbcfe | deep | arXiv:2606.28430v1 | SRC-ARXIV@arXiv:2606.28430v1 | https://arxiv.org/html/2606.28430v1 — §3 Library audit methodology; An honest oracle is enough; the exposed signal is not the per-subsystem driver.; c9 removes c3’s guards by design, and remains honest. | https://arxiv.org/html/2606.28430v1 — §2 Setup; Unit of analysis: the production agent.; Code-generation benchmarks. | https://arxiv.org/html/2606.28430v1 — §6 Threats to validity; 8 Discussion; 9 Conclusion | Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review | claim:SF-2026-ARXIV-2606-28430 | complete |
| SF-2026-ARXIV-2606-28433 | RP-8e5b7b9a6d0a15b9 | deep | arXiv:2606.28433v1 | SRC-ARXIV@arXiv:2606.28433v1 | https://arxiv.org/html/2606.28433v1 — §Position: RL Researchers Need to Distinguish Between Solving Simulators and Using Simulators as a Proxy; Keywords: | https://arxiv.org/html/2606.28433v1 — §3.4 Issue: Evaluation Rollouts; Appendix A Experiment Details; A.1 Collapsing Learning Curve Experiment | https://arxiv.org/html/2606.28433v1 — §3 Misleading Conclusions from Not Distinguishing Between Simulator Usages; 6 Conclusion | Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review | claim:SF-2026-ARXIV-2606-28433 | complete |
| SF-2026-ARXIV-2606-28434 | RP-f022ef36ea3e64e9 | standard | arXiv:2606.28434v1 | SRC-ARXIV@arXiv:2606.28434v1 | https://arxiv.org/html/2606.28434v1 — §2 Proposed Approach; 2.1 Memory Management Tool Design; Appendix A Method Details | https://arxiv.org/html/2606.28434v1 — §3 Experiment; 3.3 Experiment Details; 3.4 Main Results | https://arxiv.org/html/2606.28434v1 — §6 Conclusion | Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review | claim:SF-2026-ARXIV-2606-28434 | complete |
| SF-2026-ARXIV-2606-28436 | RP-dfe14957edbfc2c7 | standard | arXiv:2606.28436v1 | SRC-ARXIV@arXiv:2606.28436v1 | https://arxiv.org/html/2606.28436v1 — §2 Methodology; 2.2 Architecture of Dockerless; 2.3 Dockerless Training | https://arxiv.org/html/2606.28436v1 — §3 Experimental Settings; Benchmarks.; Evaluation protocol. | https://arxiv.org/html/2606.28436v1 — §6 Conclusion | Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review | claim:SF-2026-ARXIV-2606-28436 | complete |
| SF-2026-ARXIV-2606-28438 | RP-9195cfde9ec90c8d | standard | arXiv:2606.28438v1 | SRC-ARXIV@arXiv:2606.28438v1 | https://arxiv.org/html/2606.28438v1 — §When AI Reviews Its Own Code: Recursive Self-Training Collapse in Code LLMs; 2.1 Iterative Self-Training Without vs. With Gating; 2.2 Representation-Subspace Drift Under Recursive Self-Training | https://arxiv.org/html/2606.28438v1 — §2 Problem Formulation and Theoretical Analysis; 3 Experiments; 3.1 Evaluation Setup | https://arxiv.org/html/2606.28438v1 — §4 Conclusion; 5 Limitations | Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review | claim:SF-2026-ARXIV-2606-28438 | complete |
| SF-2026-ARXIV-2606-28455 | RP-87068849f946223a | standard | arXiv:2606.28455v1 | SRC-ARXIV@arXiv:2606.28455v1 | https://arxiv.org/pdf/2606.28455v1 — §3 Problem formulation; 4 Diagnostic Protocol; 5 Dataset and Models | https://arxiv.org/pdf/2606.28455v1 — §6 Main results; Appendix A. Experimental and Diagnostic Details | https://arxiv.org/pdf/2606.28455v1 — §7 Discussion and Limitations; 7.2 Scope and limitations; C.9 Interpretation boundary | Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review | claim:SF-2026-ARXIV-2606-28455 | complete |
| SF-2026-ARXIV-2606-28471 | RP-11be81e5c6e861e4 | standard | arXiv:2606.28471v1 | SRC-ARXIV@arXiv:2606.28471v1 | https://arxiv.org/html/2606.28471v1 — §2 Conceptual Framework; 2.3 Understanding Training Data; Assessment of the targeted-sampling method and the data–evaluation loop. | https://arxiv.org/html/2606.28471v1 — §Data and Evaluation Closed-Loop for Model Capability Enhancement; 2.1 Understanding Evaluation; 3 Analysis Toolkit | https://arxiv.org/html/2606.28471v1 — §4.1.3 Prediction-Level Audit of Parser-Sensitive Failures; 4.1.5 Restoring EOS Supervision and Validating Failure-Mode Reduction; 5 Conclusion | Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review | claim:SF-2026-ARXIV-2606-28471 | complete |
| SF-2026-ARXIV-2606-28479 | RP-7efc439a7c3ac654 | deep | arXiv:2606.28479v1 | SRC-ARXIV@arXiv:2606.28479v1 | https://arxiv.org/html/2606.28479v1 — §III Threat Model and Methodology | https://arxiv.org/html/2606.28479v1 — §VI Utility Evaluation | https://arxiv.org/html/2606.28479v1 — §III Threat Model and Methodology; III-A Threat Model; VII Discussion | Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review | claim:SF-2026-ARXIV-2606-28479 | complete |
| SF-2026-ARXIV-2606-28480 | RP-c1545da73365487c | deep | arXiv:2606.28480v1 | SRC-ARXIV@arXiv:2606.28480v1 | https://arxiv.org/html/2606.28480v1 — §TUA-Bench: A Benchmark for General-Purpose Terminal-Use Agents; 1 Introduction | https://arxiv.org/html/2606.28480v1 — §TUA-Bench: A Benchmark for General-Purpose Terminal-Use Agents; 4 Benchmark Experiments; 4.1 Experimental Settings | https://arxiv.org/html/2606.28480v1 — §5 Limitations; 6 Conclusion | Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review | claim:SF-2026-ARXIV-2606-28480 | complete |
| SF-2026-ARXIV-2606-28514 | RP-50bf4808e2b500ff | standard | arXiv:2606.28514v1 | SRC-ARXIV@arXiv:2606.28514v1 | https://arxiv.org/html/2606.28514v1 — §System prompt.; ReAct-style framework.; Appendix C The GPTNT Framework | https://arxiv.org/html/2606.28514v1 — §GPTNT: Benchmarking Real-Time Collaboration Between Multimodal Agents on Keep Talking And Nobody Explodes; 4 The Benchmark: What is GPTNT?; 4.3 Evaluation Protocol | https://arxiv.org/html/2606.28514v1 — §Synchronous play shifts failures toward striking out.; Localisation failure acts as a hard ceiling on downstream success.; 11 Conclusion | Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review | claim:SF-2026-ARXIV-2606-28514 | complete |
| SF-2026-ARXIV-2606-28529 | RP-a968e6a90f72f7bd | deep | arXiv:2606.28529v1 | SRC-ARXIV@arXiv:2606.28529v1 | https://arxiv.org/html/2606.28529v1 — §Optimization Methods.; B.1 Optimization Method Settings | https://arxiv.org/html/2606.28529v1 — §4 Experiments; 4.1 Setup; Simulation Task Setup. | https://arxiv.org/html/2606.28529v1 — §5 Conclusion; 6 Limitations; A.3 Assumptions and Limitations | Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review | claim:SF-2026-ARXIV-2606-28529 | complete |
| SF-2026-ARXIV-2606-28551 | RP-207f701593e0527f | standard | arXiv:2606.28551v1 | SRC-ARXIV@arXiv:2606.28551v1 | https://arxiv.org/html/2606.28551v1 — §3.2 Model Architecture and Training Recipe; 3.3 Competition Scales and Design Principles; Appendix C Model Architecture Details | https://arxiv.org/html/2606.28551v1 — §3 The DCVLM Benchmark; 3.4 Evaluation Protocol; 4.3 Control Experiments | https://arxiv.org/html/2606.28551v1 — §6 Conclusion; Appendix P Limitations and Future Directions; P.1 Limitations | Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review | claim:SF-2026-ARXIV-2606-28551 | complete |
| SF-2026-ARXIV-2606-28560 | RP-27b8a609fe71196e | standard | arXiv:2606.28560v1 | SRC-ARXIV@arXiv:2606.28560v1 | https://arxiv.org/html/2606.28560v1 — §2 Method; Model and training.; Training-length gap to dense. | https://arxiv.org/html/2606.28560v1 — §Depth-Staggered Fibonacci Spacing for Sparse Attention: Static Schedules Beat Learned Dilation and Extrapolate Where Dense Attention Fails Thanks: Code, the paper source, and the experiment database are available at https://github.com/ccapps42/scaled-fibonacci-attention .; 3 Experimental Setup; Data and evaluation. | https://arxiv.org/html/2606.28560v1 — §6 Discussion and Limitations; 7 Conclusion | Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review | claim:SF-2026-ARXIV-2606-28560 | complete |
| SF-2026-ARXIV-2606-28562 | RP-ef59e39b92b93da6 | standard | arXiv:2606.28562v1 | SRC-ARXIV@arXiv:2606.28562v1 | https://arxiv.org/html/2606.28562v1 — §2 Method; Training.; Combined Method Performance. | https://arxiv.org/html/2606.28562v1 — §3 Evaluation; 3.1 Experimental Setup; Evaluation. | https://arxiv.org/html/2606.28562v1 — §6 Conclusion and Limitations | Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review | claim:SF-2026-ARXIV-2606-28562 | complete |
| SF-2026-ARXIV-2606-28565 | RP-a49bbefa58f5800e | deep | arXiv:2606.28565v1 | SRC-ARXIV@arXiv:2606.28565v1 | https://arxiv.org/html/2606.28565v1 — §2.1. Modern LLMs and Inference Frameworks; 3.3. Gaps in Existing Approaches; 4. Tool Architecture and Methodologies | https://arxiv.org/html/2606.28565v1 — §5.2. Production Kernel Microbenchmarking; 6. Experimental Setup; 7. Results and Analysis | https://arxiv.org/html/2606.28565v1 — §8. Conclusions; Appendix B Limitations | Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review | claim:SF-2026-ARXIV-2606-28565 | complete |
| SF-2026-ARXIV-2606-28574 | RP-671807f8d42e5a4f | deep | arXiv:2606.28574v1 | SRC-ARXIV@arXiv:2606.28574v1 | https://arxiv.org/pdf/2606.28574v1 — §1.7 The three opacities; 2 Construct validity; 3 Grain calibration | https://arxiv.org/pdf/2606.28574v1 — §3.1 Clauses with grounds; 3.2 Human in the loop | https://arxiv.org/pdf/2606.28574v1 — §1.1 Where the instrument fails; 2.1 Still the wrong reasons; 3.1 Clauses with grounds | Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review | claim:SF-2026-ARXIV-2606-28574 | complete |
| SF-2026-ARXIV-2606-28615 | RP-ecf748eaaefe8914 | deep | arXiv:2606.28615v1 | SRC-ARXIV@arXiv:2606.28615v1 | https://arxiv.org/html/2606.28615v1 — §Appendix C Algorithms | https://arxiv.org/html/2606.28615v1 — §5 Experiments; 5.4 Additional analysis; Appendix E Additional results | https://arxiv.org/html/2606.28615v1 — §7 Conclusion | Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review | claim:SF-2026-ARXIV-2606-28615 | complete |
| SF-2026-ARXIV-2606-28639 | RP-abf921be504e8ec8 | deep | arXiv:2606.28639v1 | SRC-ARXIV@arXiv:2606.28639v1 | https://arxiv.org/pdf/2606.28639v1 — §2 The Unverifiability of AGI Alignment; 4 The Semantic Barrier; 6 Trakhtenbrot's Wall | https://arxiv.org/pdf/2606.28639v1 — §7 Formal Conclusion of the Proof; 9 Theorem of Finite Structural Unverifiability | https://arxiv.org/pdf/2606.28639v1 — §10 Applied Engineering; 11 Conclusions | Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review | claim:SF-2026-ARXIV-2606-28639 | complete |
| SF-2026-ARXIV-2606-28649 | RP-8a8be17a6b14ef51 | deep | arXiv:2606.28649v1 | SRC-ARXIV@arXiv:2606.28649v1 | https://arxiv.org/html/2606.28649v1 — §II-C Security of ROS-Based Systems; III-A System Model; IV Methodology | https://arxiv.org/html/2606.28649v1 — §V Experimental Results; V-B Firewall Defense Evaluation; V-C Firewall Bypass Analysis | https://arxiv.org/html/2606.28649v1 — §III Threat Model; VI Discussion; VI-C The Sensory Vector as a Distinct Threat | Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review | claim:SF-2026-ARXIV-2606-28649 | complete |
| SF-2026-ARXIV-2606-28661 | RP-2a6eb36ad4257672 | deep | arXiv:2606.28661v1 | SRC-ARXIV@arXiv:2606.28661v1 | https://arxiv.org/html/2606.28661v1 — §Proposition 1 (Design effect of test-time sampling) .; Two-stage design effect. | https://arxiv.org/html/2606.28661v1 — §1 Introduction and roadmap; 2 Test-time sampling is cluster sampling | https://arxiv.org/html/2606.28661v1 — §6 Conclusion | Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review | claim:SF-2026-ARXIV-2606-28661 | complete |

### Source Reviews
<!-- review:SF-2026-ARXIV-2606-27632:start -->
### 2606.27632 — Yuvion LLM: An Adversarially-Aware Large Language Model for Content And AI Safety

**问题、约束与旧路径。** As large language models are increasingly deployed in real-world systems, safety failures can still lead to harmful outputs and dangerous misuse. We argue that the essence of safety is adversarial: many failures arise not from natural inputs alone, but from strategic attempts to evade model policies and safeguards. 旧路径在论文新增条件之外仍然合理。

**机制、state/data/control owner。** 把 adversarial robustness、agentic tool use 与 safety release evaluation 绑定为同一模型发布合同。 由 PLATFORM-SECURITY 持有 authority envelope、untrusted input 与 release gate；相邻节点只消费版本化 handoff。

**Evaluation：证明与未证明。** Notably, Yuvion-8B outperforms most state-of-the-art baselines, including substantially larger models such as GPT-5.4 and Qwen3-MAX, on several safety tasks. Method=https://arxiv.org/html/2606.27632v1 — §2 Content-Safety-Oriented Data System; 3 Yuvion LLM: Progressive Safety Training Paradigm; 3.2 Target Capability Design；Evaluation=https://arxiv.org/html/2606.27632v1 — §4 Evaluation Framework; 4.2 Level 1: Open-source General Benchmarks; 4.3 Level 2: Open-source Content Safety Benchmarks。评测合同逐字段冻结，未公开项才写 Not Disclosed。

**Trade-off、failure、fallback、coexistence 与 evolution。** Across these evaluations, Yuvion LLM demonstrates clear advantages on safety-focused benchmarks and particularly strong robustness under adversarial conditions, while maintaining solid overall capability. 现有 owner 已覆盖同一长期原则，因此只作为受限反例或实例留在 Daily，不复制 Books 分支。 Counterevidence/limitation=https://arxiv.org/html/2606.27632v1 — §Discussion.; 9 Conclusion; 10 Limitations and Future Work。

<!-- claim:SF-2026-ARXIV-2606-27632:start -->
Claim boundary：仅 arXiv:2606.27632v1 与 official exact-v1 HTML；不使用 later version，不把 benchmark outcome 外推为生产 SLO。
<!-- claim:SF-2026-ARXIV-2606-27632:end -->
<!-- review:SF-2026-ARXIV-2606-27632:end -->

<!-- review:SF-2026-ARXIV-2606-27634:start -->
### 2606.27634 — Continual Learning for Sequential Personalization of Small Language Models: A Stability Monitoring Analysis

**问题、约束与旧路径。** Small Language Models (SLMs) are increasingly being considered for deployment on edge devices such as laptops, enabling private, low-latency, and locally personalized applications. However, personalization requires models to adapt over time to evolving user- or task-specific data, placing them in a continual learning setting. 旧路径在论文新增条件之外仍然合理。

**机制、state/data/control owner。** 把 sequential LoRA personalization 的 checkpoint、reference-set drift 与遗忘监控绑定为持续适配合同。 由 PLATFORM-MONITORING 持有 sensor state、calibration 与 alarm action；相邻节点只消费版本化 handoff。

**Evaluation：证明与未证明。** We show that lightweight reference set distributional diagnostics can reveal model-specific instability patterns during sequential LoRA personalization of SLMs, including cases where task-level metrics alone hide harmful adaptation. Method=https://arxiv.org/html/2606.27634v1 — §4.0.4 Training Procedure；Evaluation=https://arxiv.org/html/2606.27634v1 — §Continual Learning for Sequential Personalization of Small Language Models: A Stability Monitoring Analysis; 2.0.1 Continual Learning and Evaluation of Language Models.; 3.2 Model Checkpoints and Evaluation。评测合同逐字段冻结，未公开项才写 Not Disclosed。

**Trade-off、failure、fallback、coexistence 与 evolution。** However, personalization requires models to adapt over time to evolving user- or task-specific data, placing them in a continual learning setting. 现有 owner 已覆盖同一长期原则，因此只作为受限反例或实例留在 Daily，不复制 Books 分支。 Counterevidence/limitation=https://arxiv.org/html/2606.27634v1 — §6 Conclusion; 6.0.1 Limitations。

<!-- claim:SF-2026-ARXIV-2606-27634:start -->
Claim boundary：仅 arXiv:2606.27634v1 与 official exact-v1 HTML；不使用 later version，不把 benchmark outcome 外推为生产 SLO。
<!-- claim:SF-2026-ARXIV-2606-27634:end -->
<!-- review:SF-2026-ARXIV-2606-27634:end -->

<!-- review:SF-2026-ARXIV-2606-27650:start -->
### 2606.27650 — GenWorld: Empirically Grounded Urban Simulation Infrastructure for Scalable LLM-Agent Studies

**问题、约束与旧路径。** LLM-agent simulation faces a joint grounding and scaling problem: agents should act in environments that reflect real urban constraints, yet direct online LLM calls for city-scale populations are computationally prohibitive. We present GenWorld, an empirically grounded urban simulation infrastructure that combines a building-level synthetic city, a structured agent-environment interface, and offline compilation of LLM-derived decision signals into lookup policies for scalable rollout. 旧路径在论文新增条件之外仍然合理。

**机制、state/data/control owner。** 把城市级 agent environment、离线 policy compilation、人口/地理 grounding 与可复算 rollout 统一为 simulation infrastructure。 由 AGENT-PLATFORM 持有 workspace、runtime、acceptance predicate 与 replay；相邻节点只消费版本化 handoff。

**Evaluation：证明与未证明。** We demonstrate the infrastructure through three reproducible cases: a full-city weekday rollout, a weekday-weekend behavioral contrast, and a warning-response perturbation with auditable replanning traces. Method=https://arxiv.org/html/2606.27650v1 — §Context Design and Coverage; 6 Platform Architecture; 6.1 System Overview；Evaluation=https://arxiv.org/html/2606.27650v1 — §7 Evaluation Cases and Scalability; 7.1 Evaluation Cases; 7.1.5 Scalability Analysis。评测合同逐字段冻结，未公开项才写 Not Disclosed。

**Trade-off、failure、fallback、coexistence 与 evolution。** These cases support GenWorld as a reproducible platform for grounded and scalable LLM-agent studies, while calibrated forecasting for traffic, evacuation, or policy outcomes remains future work. 现有 owner 已覆盖同一长期原则，因此只作为受限反例或实例留在 Daily，不复制 Books 分支。 Counterevidence/limitation=https://arxiv.org/html/2606.27650v1 — §8 Discussion; Limitations and Future Work; 9 Conclusion。

<!-- claim:SF-2026-ARXIV-2606-27650:start -->
Claim boundary：仅 arXiv:2606.27650v1 与 official exact-v1 HTML；不使用 later version，不把 benchmark outcome 外推为生产 SLO。
<!-- claim:SF-2026-ARXIV-2606-27650:end -->
<!-- review:SF-2026-ARXIV-2606-27650:end -->

<!-- review:SF-2026-ARXIV-2606-27669:start -->
### 2606.27669 — When Search Agents Should Ask: DiscoBench for Clarification-Aware Deep Search

**问题、约束与旧路径。** Search agents powered by large language models (LLMs) are increasingly used to solve complex information-seeking tasks, requiring multi-step retrieval and reasoning to fulfill user goals. However, existing benchmarks often assume that user queries are complete and explicit, overlooking the fact that real-world search requests are frequently vague, underspecified, or even factually incorrect. 旧路径在论文新增条件之外仍然合理。

**机制、state/data/control owner。** 把 deep-search 的 ambiguity detection、clarification action、task utility 与交互成本分离成评估合同。 由 PLATFORM-EVALUATION-SYSTEM 持有 oracle、metric、slice 与结论发布；相邻节点只消费版本化 handoff。

**Evaluation：证明与未证明。** Experiments on representative LLMs show that ambiguity detection and effective clarification are distinct capabilities, and that repeatedly searching instead of asking for clarification often performs worse than direct guessing, highlighting a critical gap between retrieval ability and interactive problem-solving in current search agents. Method=https://arxiv.org/html/2606.27669v1 — §4 Methodology of Dataset Construction; Benchmark Design and Methodology.; Evaluation Framework and User Simulator.；Evaluation=https://arxiv.org/html/2606.27669v1 — §2.1 Web Search Benchmark; 2.2 Ambiguity Benchmark; 2.3 Interactive Clarification Benchmark。评测合同逐字段冻结，未公开项才写 Not Disclosed。

**Trade-off、failure、fallback、coexistence 与 evolution。** However, existing benchmarks often assume that user queries are complete and explicit, overlooking the fact that real-world search requests are frequently vague, underspecified, or even factually incorrect. 现有 owner 已覆盖同一长期原则，因此只作为受限反例或实例留在 Daily，不复制 Books 分支。 Counterevidence/limitation=https://arxiv.org/html/2606.27669v1 — §Search-heavy guessing reveals a major failure mode.; 6 Conclusion; Limitations。

<!-- claim:SF-2026-ARXIV-2606-27669:start -->
Claim boundary：仅 arXiv:2606.27669v1 与 official exact-v1 HTML；不使用 later version，不把 benchmark outcome 外推为生产 SLO。
<!-- claim:SF-2026-ARXIV-2606-27669:end -->
<!-- review:SF-2026-ARXIV-2606-27669:end -->

<!-- review:SF-2026-ARXIV-2606-27679:start -->
### 2606.27679 — From Signals to Transfer: A Factorised Study of Probe-Based Uncertainty Estimation in Large Language Models

**问题、约束与旧路径。** Probe-based uncertainty estimation (UE) has emerged as a prominent approach to detect hallucinations in Large Language Models (LLMs) by learning uncertainty from internal model signals. Yet, recent methods vary simultaneously across feature design, training data construction, and evaluation setting, obscuring what actually drives performance. 旧路径在论文新增条件之外仍然合理。

**机制、state/data/control owner。** 给 probe uncertainty monitor 建立 feature、label construction、prompt 与 distribution-shift transfer 的可迁移边界。 由 PLATFORM-MONITORING 持有 sensor state、calibration 与 alarm action；相邻节点只消费版本化 handoff。

**Evaluation：证明与未证明。** Our results show that raw hidden states and attention features are difficult to outperform in-domain. Method=https://arxiv.org/html/2606.27679v1 — §Probe Training.; Probe Architecture and Training Size.；Evaluation=https://arxiv.org/html/2606.27679v1 — §Toolkits, Benchmarks, and Evaluation.; 3.1 Experimental Setup; Evaluation Metrics.。评测合同逐字段冻结，未公开项才写 Not Disclosed。

**Trade-off、failure、fallback、coexistence 与 evolution。** However, under distribution shift, structured and compressed features are more robust, suggesting that in-domain performance alone is insufficient to measure progress. 现有 owner 已覆盖同一长期原则，因此只作为受限反例或实例留在 Daily，不复制 Books 分支。 Counterevidence/limitation=https://arxiv.org/html/2606.27679v1 — §4.2 Results and Discussion; 5 Conclusion; Limitations。

<!-- claim:SF-2026-ARXIV-2606-27679:start -->
Claim boundary：仅 arXiv:2606.27679v1 与 official exact-v1 HTML；不使用 later version，不把 benchmark outcome 外推为生产 SLO。
<!-- claim:SF-2026-ARXIV-2606-27679:end -->
<!-- review:SF-2026-ARXIV-2606-27679:end -->

<!-- review:SF-2026-ARXIV-2606-27681:start -->
### 2606.27681 — Textual Belief States for World Models: Identifiable Representation Learning Under Strict Mediation

**问题、约束与旧路径。** World models in partially observed environments rely on latent representations that summarize interaction history, but in many modern LLM-based architectures predictive performance fails to reflect representation quality due to history bypass, rendering the latent state unidentifiable. Strict latent state mediation, requiring predictions to depend only on the latent state and action, is a classical principle that resolves this, but enforcing it in text-based settings is an open challenge: textual latent states are discrete and non-differentiable, precluding variational training, and expressive LLM decoders readily ignore the bottleneck. 旧路径在论文新增条件之外仍然合理。

**机制、state/data/control owner。** 用 strict mediation 让 textual belief state 成为唯一可测试的预测状态，阻断 history bypass。 由 MULTIMODAL-WORLD-MODELS 持有 belief/latent state、transition 与 physical boundary；相邻节点只消费版本化 handoff。

**Evaluation：证明与未证明。** Experiments on TextWorld and ScienceWorld show preserved one-step prediction accuracy alongside up to 57\% gains in representation quality and 98\% improvements in rollout performance, increasing with task complexity and horizon. Method=https://arxiv.org/html/2606.27681v1 — §Proposition 2 (Non-identifiability under leaky architectures) .; Proposition 3 (Training–inference consistency) .; 4.2 Model Architecture；Evaluation=https://arxiv.org/html/2606.27681v1 — §2 Problem Setup: Text Based POMDPs; 5 Experimental Evaluation; 5.3 Evaluation Metrics。评测合同逐字段冻结，未公开项才写 Not Disclosed。

**Trade-off、failure、fallback、coexistence 与 evolution。** We formalize why it is necessary, showing that strict mediation makes representation quality empirically testable while history-leaky architectures break this connection. Strict mediation 增加训练成本，也可能让有损 textual state 成为瓶颈；无需可识别性时，直接 latent/history access 仍是合理旧路径。 Counterevidence/limitation=https://arxiv.org/html/2606.27681v1 — §7 Conclusion。

<!-- claim:SF-2026-ARXIV-2606-27681:start -->
Claim boundary：仅 arXiv:2606.27681v1 与 official exact-v1 HTML；不使用 later version，不把 benchmark outcome 外推为生产 SLO。
<!-- claim:SF-2026-ARXIV-2606-27681:end -->
<!-- review:SF-2026-ARXIV-2606-27681:end -->

<!-- review:SF-2026-ARXIV-2606-27683:start -->
### 2606.27683 — CBD: API-Only LLM Black-Box Unlearning through Controlled Behavioral Divergence

**问题、约束与旧路径。** Edge devices increasingly invoke large language models (LLMs) through API services for context aware edge intelligence, while edge generated data may be collected to improve LLMs and may introduce sensitive, copyrighted, harmful, or outdated information into model behavior. Machine unlearning offers a practical way to remove the influence of undesired data without retraining LLMs. 旧路径在论文新增条件之外仍然合理。

**机制、state/data/control owner。** 揭示 API-only black-box unlearning 实际由 relevance router 与 auxiliary models 持有控制权，而非修改远端模型。 由 PLATFORM-SECURITY 持有 authority envelope、untrusted input 与 release gate；相邻节点只消费版本化 handoff。

**Evaluation：证明与未证明。** Compared with eleven white box and gray box unlearning baselines, CBD achieves a better unlearning utility trade off and its performance varies little across settings. Method=https://arxiv.org/html/2606.27683v1 — §III Preliminaries and Framework; III-A White-Box and Gray-Box Unlearning Methods; III-B API-Only Scenario and Proposed Framework；Evaluation=https://arxiv.org/html/2606.27683v1 — §VI Experiments; VI-A Experimental Setup; VI-B Performance Evaluation。评测合同逐字段冻结，未公开项才写 Not Disclosed。

**Trade-off、failure、fallback、coexistence 与 evolution。** On WMDP, it lowers hazardous knowledge accuracy to 25.68, near random guessing, while preserving MMLU accuracy of 52.67. 现有 owner 已覆盖同一长期原则，因此只作为受限反例或实例留在 Daily，不复制 Books 分支。 Counterevidence/limitation=https://arxiv.org/html/2606.27683v1 — §VII Conclusion。

<!-- claim:SF-2026-ARXIV-2606-27683:start -->
Claim boundary：仅 arXiv:2606.27683v1 与 official exact-v1 HTML；不使用 later version，不把 benchmark outcome 外推为生产 SLO。
<!-- claim:SF-2026-ARXIV-2606-27683:end -->
<!-- review:SF-2026-ARXIV-2606-27683:end -->

<!-- review:SF-2026-ARXIV-2606-27704:start -->
### 2606.27704 — AdvScan: Black-Box Adversarial Example Detection at Runtime through Power Analysis

**问题、约束与旧路径。** TinyML models deployed on edge devices are increasingly adopted in safety/security-critical applications, making them a prime target for adversarial example (AE) attacks where inputs are modified to cause misclassifications. However, existing AE detection methods either require white-box model access, which is often unavailable in licensed black-box deployments, or rely on input pre-processing stages that add non-trivial latency and resource overhead, often exceeding what mission-critical applications can afford on their inference path. 旧路径在论文新增条件之外仍然合理。

**机制、state/data/control owner。** 把 edge black-box adversarial detection 从模型内部 probe 改为 runtime power sensor，并暴露设备/攻击覆盖边界。 由 PLATFORM-SECURITY 持有 authority envelope、untrusted input 与 release gate；相邻节点只消费版本化 handoff。

**Evaluation：证明与未证明。** These results demonstrate the viability of power-based AE detection for secure, accuracy-critical TinyML deployments in black-box environments. Method=https://arxiv.org/html/2606.27704v1 — §IV AdvScan Algorithm; V-A 3 Adversarial Examples (AE) Generation Methodologies; V-C Evaluation of the AdvScan Algorithm；Evaluation=https://arxiv.org/html/2606.27704v1 — §AdvScan: Black-Box Adversarial Example Detection at Runtime through Power Analysis; II-D Power Analysis; II-E Side Channel Analysis for Adversarial Behavior Detection。评测合同逐字段冻结，未公开项才写 Not Disclosed。

**Trade-off、failure、fallback、coexistence 与 evolution。** Across 318,400 total test inputs, AdvScan detects 99.984% of AEs with only 40 false negatives and zero false positives. 现有 owner 已覆盖同一长期原则，因此只作为受限反例或实例留在 Daily，不复制 Books 分支。 Counterevidence/limitation=https://arxiv.org/html/2606.27704v1 — §II-F Threat Model; IV-D Discussion of Merits and Limitations of AdvScan; VI Conclusion。

<!-- claim:SF-2026-ARXIV-2606-27704:start -->
Claim boundary：仅 arXiv:2606.27704v1 与 official exact-v1 HTML；不使用 later version，不把 benchmark outcome 外推为生产 SLO。
<!-- claim:SF-2026-ARXIV-2606-27704:end -->
<!-- review:SF-2026-ARXIV-2606-27704:end -->

<!-- review:SF-2026-ARXIV-2606-27709:start -->
### 2606.27709 — Low-Agreeableness Persona Conditioning for Safe LLM Fine-Tuning

**问题、约束与旧路径。** Recent work has shown that fine-tuning large language models (LLMs) for social warmth degrades factual reliability and increases sycophancy. We investigate a related but distinct failure mode: warmth fine-tuning also weakens adversarial safety, making models more susceptible to jailbreaks and harmful output generation. 旧路径在论文新增条件之外仍然合理。

**机制、state/data/control owner。** 证明 warmth fine-tuning 的 jailbreak regression 取决于 persona/data construction，而非同理性目标本身必然削弱安全。 由 TRAIN-DATA 持有 sample provenance、mixture 与 admission state；相邻节点只消费版本化 handoff。

**Evaluation：证明与未证明。** These results show that safer empathetic fine-tuning is achievable through data design alone, without safety labels, harm detectors, or changes to the training objective. Method=https://arxiv.org/html/2606.27709v1 — §3 Methods; 3.2 Study design; 3.3 Training data and data construction；Evaluation=https://arxiv.org/html/2606.27709v1 — §Experiment 1.; Experiment 2.; Experiment 3.。评测合同逐字段冻结，未公开项才写 Not Disclosed。

**Trade-off、failure、fallback、coexistence 与 evolution。** These results show that safer empathetic fine-tuning is achievable through data design alone, without safety labels, harm detectors, or changes to the training objective. 现有 owner 已覆盖同一长期原则，因此只作为受限反例或实例留在 Daily，不复制 Books 分支。 Counterevidence/limitation=https://arxiv.org/html/2606.27709v1 — §5 Discussion; Limitations。

<!-- claim:SF-2026-ARXIV-2606-27709:start -->
Claim boundary：仅 arXiv:2606.27709v1 与 official exact-v1 HTML；不使用 later version，不把 benchmark outcome 外推为生产 SLO。
<!-- claim:SF-2026-ARXIV-2606-27709:end -->
<!-- review:SF-2026-ARXIV-2606-27709:end -->

<!-- review:SF-2026-ARXIV-2606-27732:start -->
### 2606.27732 — Bifocal Diffusion Language Models: Asymmetric Bidirectional Context for Parallel Generation

**问题、约束与旧路径。** Discrete diffusion language models (dLLMs) recover masked tokens in parallel, offering significant speedups over autoregressive (AR) generation. However, such promising frameworks face a fundamental architectural design dilemma: \ding{182} Adopting bidirectional attention achieves strong generation quality by allowing each position to access the full context, but is inherently incompatible with KV caching, limiting inference throughput in batch-serving scenarios; \ding{183} Conversely, causal attention enables efficient cached inference but loses all right-side context, substantially degrading generation quality. 旧路径在论文新增条件之外仍然合理。

**机制、state/data/control owner。** 用 asymmetric bidirectional sidecar 重构 diffusion-LM 的右上下文、KV cache 与 parallel decode 取舍。 由 MULTIMODAL-GENERATIVE-PARADIGMS 持有 generation dependency、cache 与 commit order；相邻节点只消费版本化 handoff。

**Evaluation：证明与未证明。** Comprehensive experiments on continued pretraining of Qwen3-1.7B with 60B tokens demonstrate that R2LM achieves $2.4\times$ to $12.9\times$ higher throughput than bidirectional dLLMs and $1.9\times$ to $2.9\times$ speedup over AR baselines in batch serving through parallel decoding with KV caching, while exceeding the causal baseline on most benchmarks and surpassing the bidirectional dLLM on average. Method=https://arxiv.org/html/2606.27732v1 — §3 Method; 3.4 R2LM Architecture; 3.5 Training and Inference；Evaluation=https://arxiv.org/html/2606.27732v1 — §4 Experiments; 4.1 Experimental Setup; 4.2 Main Results: Multiple-Choice Benchmarks。评测合同逐字段冻结，未公开项才写 Not Disclosed。

**Trade-off、failure、fallback、coexistence 与 evolution。** Comprehensive experiments on continued pretraining of Qwen3-1.7B with 60B tokens demonstrate that R2LM achieves $2.4\times$ to $12.9\times$ higher throughput than bidirectional dLLMs and $1.9\times$ to $2.9\times$ speedup over AR baselines in batch serving through parallel decoding with KV caching, while exceeding the causal baseline on most benchmarks and surpassing the bidirectional dLLM on average. Side path 增加参数、训练耦合与 cache-version 复杂度；要求 exact streaming 或 kernel 不支持时回退 causal generation。 Counterevidence/limitation=https://arxiv.org/html/2606.27732v1 — §5 Conclusion。

<!-- claim:SF-2026-ARXIV-2606-27732:start -->
Claim boundary：仅 arXiv:2606.27732v1 与 official exact-v1 HTML；不使用 later version，不把 benchmark outcome 外推为生产 SLO。
<!-- claim:SF-2026-ARXIV-2606-27732:end -->
<!-- review:SF-2026-ARXIV-2606-27732:end -->

<!-- review:SF-2026-ARXIV-2606-27739:start -->
### 2606.27739 — The Weakest Link Tells It All: Outcome-Supervised Process Reward Modeling via Learnable Credit Assignment

**问题、约束与旧路径。** Process reward models (PRMs) enhance the reasoning capabilities of large language models (LLMs) by providing fine-grained feedback, yet training PRMs typically requires expensive stepwise annotations. Outcome-supervised PRMs offer a scalable alternative by learning from final-answer correctness alone, but this introduces a fundamental *credit assignment* challenge, i.e., attributing outcomes to responsible reasoning steps. 旧路径在论文新增条件之外仍然合理。

**机制、state/data/control owner。** 把 outcome-supervised PRM 的 step credit assignment 表述为 weakest-link multiple-instance learning。 由 TRAIN-GRPO 持有 trajectory、credit、teacher signal 与 update gate；相邻节点只消费版本化 handoff。

**Evaluation：证明与未证明。** Extensive experiments demonstrate that **LCA** consistently outperforms state-of-the-art outcome-supervised PRMs across multiple tasks and backbones. Method=https://arxiv.org/html/2606.27739v1 — §4 Method; C.2 PRM Training Details; Model architecture.；Evaluation=https://arxiv.org/html/2606.27739v1 — §3 Analysis; 3.3 Theoretical Analysis; 5 Experiments。评测合同逐字段冻结，未公开项才写 Not Disclosed。

**Trade-off、failure、fallback、coexistence 与 evolution。** exact-v1 的结论只覆盖《The Weakest Link Tells It All: Outcome-Supervised Process Reward Modeling via Learnable Credit Assignment》在 3 Analysis; 3.3 Theoretical Analysis; 5 Experiments 声明的实验；它没有证明跨 model family、hardware/runtime、数据分布或未测 failure mode 的普遍成立。 现有 owner 已覆盖同一长期原则，因此只作为受限反例或实例留在 Daily，不复制 Books 分支。 Counterevidence/limitation=https://arxiv.org/html/2606.27739v1 — §6 Conclusion; Limitations; B.7 Discussion。

<!-- claim:SF-2026-ARXIV-2606-27739:start -->
Claim boundary：仅 arXiv:2606.27739v1 与 official exact-v1 HTML；不使用 later version，不把 benchmark outcome 外推为生产 SLO。
<!-- claim:SF-2026-ARXIV-2606-27739:end -->
<!-- review:SF-2026-ARXIV-2606-27739:end -->

<!-- review:SF-2026-ARXIV-2606-27743:start -->
### 2606.27743 — End-to-End Dynamic Sparsity for Resource-Adaptive LLM Inference

**问题、约束与旧路径。** Large Language Models (LLMs) inference is typically deployed under a static resource assumption, where models execute a fixed computational graph regardless of the runtime environment. However, real-world cloud infrastructure is inherently dynamic, characterized by fluctuating availability (e.g., spot instance preemption) and tiered Quality-of-Service requirements. 旧路径在论文新增条件之外仍然合理。

**机制、state/data/control owner。** 把 layer/head/token compute footprint 变成由输入与实时资源预算共同控制的 runtime policy state。 由 INFER-SCHEDULING 持有 request budget、compute allocation 与 fallback；相邻节点只消费版本化 handoff。

**Evaluation：证明与未证明。** A single L2A model traces the entire compute-accuracy Pareto frontier on Llama-3-8B and Qwen-3-4B: at up to 34% realized layer sparsity, it stays within 0.6% of the dense baseline on GSM8K, with the same gap holding zero-shot on out-of-distribution tasks, while every static or heuristic baseline requires a separately tuned model and still drops by 5-10% at comparable inference time. Method=https://arxiv.org/html/2606.27743v1 — §3 Methodology; 3.5 Training and Inference；Evaluation=https://arxiv.org/html/2606.27743v1 — §4 Experiments; 4.1 Experimental Setup; 4.2 Main Results。评测合同逐字段冻结，未公开项才写 Not Disclosed。

**Trade-off、failure、fallback、coexistence 与 evolution。** A single L2A model traces the entire compute-accuracy Pareto frontier on Llama-3-8B and Qwen-3-4B: at up to 34% realized layer sparsity, it stays within 0.6% of the dense baseline on GSM8K, with the same gap holding zero-shot on out-of-distribution tasks, while every static or heuristic baseline requires a separately tuned model and still drops by 5-10% at comparable inference time. 现有 owner 已覆盖同一长期原则，因此只作为受限反例或实例留在 Daily，不复制 Books 分支。 Counterevidence/limitation=https://arxiv.org/html/2606.27743v1 — §4.6 Discussion and Limitations; 5 Conclusion。

<!-- claim:SF-2026-ARXIV-2606-27743:start -->
Claim boundary：仅 arXiv:2606.27743v1 与 official exact-v1 HTML；不使用 later version，不把 benchmark outcome 外推为生产 SLO。
<!-- claim:SF-2026-ARXIV-2606-27743:end -->
<!-- review:SF-2026-ARXIV-2606-27743:end -->

<!-- review:SF-2026-ARXIV-2606-27757:start -->
### 2606.27757 — Towards Reliable and Robust LLM Planning: Symbolic Feedback-Driven Iterative Self-Refinement Framework

**问题、约束与旧路径。** Large language models (LLMs) have attracted widespread attention from academia and industry, yet their deployment raises critical security concerns regarding robustness and reliability. Planning, a core component of intelligent behavior, remains challenging for LLMs, which often produce infeasible or incorrect solutions in long-horizon decision-making tasks due to inherent complexity. 旧路径在论文新增条件之外仍然合理。

**机制、state/data/control owner。** 把 symbolic verifier、reachability recognizer 与 revision loop 放到 long-horizon plan 的显式控制流。 由 AGENT-PLANNING 持有 world state、plan revision 与 executable commit；相邻节点只消费版本化 handoff。

**Evaluation：证明与未证明。** Empirical results demonstrate that the proposed framework consistently improves both feasibility and correctness in long-horizon planning tasks. Method=https://arxiv.org/html/2606.27757v1 — §Towards Reliable and Robust LLM Planning: A Symbolic Feedback-Driven Iterative Self-Refinement Framework Thanks: * Corresponding author at: Institute of Automation, Chinese Academy of Sciences, Beijing, China.; III METHODOLOGY; III-B Feedback-Driven Iterative Self-Refinement Framework；Evaluation=https://arxiv.org/html/2606.27757v1 — §IV EXPERIMENTS; IV-A Experimental Settings; IV-D Analysis of Planning Length。评测合同逐字段冻结，未公开项才写 Not Disclosed。

**Trade-off、failure、fallback、coexistence 与 evolution。** exact-v1 的结论只覆盖《Towards Reliable and Robust LLM Planning: Symbolic Feedback-Driven Iterative Self-Refinement Framework》在 IV EXPERIMENTS; IV-A Experimental Settings; IV-D Analysis of Planning Length 声明的实验；它没有证明跨 model family、hardware/runtime、数据分布或未测 failure mode 的普遍成立。 现有 owner 已覆盖同一长期原则，因此只作为受限反例或实例留在 Daily，不复制 Books 分支。 Counterevidence/limitation=https://arxiv.org/html/2606.27757v1 — §V CONCLUSION。

<!-- claim:SF-2026-ARXIV-2606-27757:start -->
Claim boundary：仅 arXiv:2606.27757v1 与 official exact-v1 HTML；不使用 later version，不把 benchmark outcome 外推为生产 SLO。
<!-- claim:SF-2026-ARXIV-2606-27757:end -->
<!-- review:SF-2026-ARXIV-2606-27757:end -->

<!-- review:SF-2026-ARXIV-2606-27780:start -->
### 2606.27780 — Understanding Rollout Error in Graph World Models

**问题、约束与旧路径。** World models are increasingly used for planning, yet most analyses of rollout error assume vector-valued states and scalar error amplification. Many planning environments, however, are naturally graph-structured: agents, tools, skills, routes, and dependencies interact through evolving relations. 旧路径在论文新增条件之外仍然合理。

**机制、state/data/control owner。** 给 graph world-model rollout 建立 topology/model factor 分解与 dynamic-edge error feedback contract。 由 MULTIMODAL-WORLD-MODELS 持有 belief/latent state、transition 与 physical boundary；相邻节点只消费版本化 handoff。

**Evaluation：证明与未证明。** Our results characterize when graph world models remain reliable under autoregressive planning and when topology makes them fail. Method=https://arxiv.org/html/2606.27780v1 — §Agent graphs and skill-graph systems.; 3 Graph World Model Framework; Framework overview.；Evaluation=https://arxiv.org/html/2606.27780v1 — §5 Dataset and Evaluation Protocol; Graph world model setup.; 7 Experiments。评测合同逐字段冻结，未公开项才写 Not Disclosed。

**Trade-off、failure、fallback、coexistence 与 evolution。** Our results characterize when graph world models remain reliable under autoregressive planning and when topology makes them fail. 现有 owner 已覆盖同一长期原则，因此只作为受限反例或实例留在 Daily，不复制 Books 分支。 Counterevidence/limitation=https://arxiv.org/html/2606.27780v1 — §7.2.3 Global spectral amplification differs from local hub failure; 7.5.4 OOD perturbation confirms the FE contraction boundary; 7.6.2 Role-dependent failure sensitivity。

<!-- claim:SF-2026-ARXIV-2606-27780:start -->
Claim boundary：仅 arXiv:2606.27780v1 与 official exact-v1 HTML；不使用 later version，不把 benchmark outcome 外推为生产 SLO。
<!-- claim:SF-2026-ARXIV-2606-27780:end -->
<!-- review:SF-2026-ARXIV-2606-27780:end -->

<!-- review:SF-2026-ARXIV-2606-27791:start -->
### 2606.27791 — NLL-Guided Full-Attention Layer Selection for Training-Free Sliding-Window Adaptation

**问题、约束与旧路径。** Hybrid attention models that mix full and sliding-window attention across layers offer a promising approach to efficient long-context inference, but the critical question of \emph{which layers} should retain full attention remains unsolved. Existing methods use either fixed periodic patterns or attention-based heuristics that may not capture what matters for downstream accuracy. 旧路径在论文新增条件之外仍然合理。

**机制、state/data/control owner。** 以 answer-token NLL degradation 选择保留 full-attention 的层，改变 hybrid attention 的 calibration owner。 由 MODEL-LONG-CONTEXT 持有 attention reach、layer policy 与 context budget；相邻节点只消费版本化 handoff。

**Evaluation：证明与未证明。** De-confounding analysis shows the signal is consistent with long-range attention needs rather than generic layer sensitivity. Method=https://arxiv.org/html/2606.27791v1 — §NLL-Guided Full-Attention Layer Selection for Training-Free Sliding-Window Adaptation; 3 Method；Evaluation=https://arxiv.org/html/2606.27791v1 — §4 Experiments; 4.1 Experimental Setup; 4.2 Main Results。评测合同逐字段冻结，未公开项才写 Not Disclosed。

**Trade-off、failure、fallback、coexistence 与 evolution。** The method requires only $\sim$15 minutes of one-time calibration, advancing the efficiency-accuracy Pareto frontier for long-context LLM deployment. 该结果只保留为局部方法/实验语境；它不新增长期 owner、authority、coexistence 或 fallback 命题。 Counterevidence/limitation=https://arxiv.org/html/2606.27791v1 — §5 Conclusion。

<!-- claim:SF-2026-ARXIV-2606-27791:start -->
Claim boundary：仅 arXiv:2606.27791v1 与 official exact-v1 HTML；不使用 later version，不把 benchmark outcome 外推为生产 SLO。
<!-- claim:SF-2026-ARXIV-2606-27791:end -->
<!-- review:SF-2026-ARXIV-2606-27791:end -->

<!-- review:SF-2026-ARXIV-2606-27797:start -->
### 2606.27797 — Optimizing Teacher-Student Partitioning for Scalable Knowledge Distillation on HPC Systems

**问题、约束与旧路径。** Knowledge Distillation (KD) enables training smaller student models under the guidance of larger teacher models, and the widely adopted TRL library implements it. Yet, TRL treats both models symmetrically, missing opportunities to exploit their pronounced asymmetry in memory footprint, and communication requirements. 旧路径在论文新增条件之外仍然合理。

**机制、state/data/control owner。** 按 teacher/student 不对称分别选择模型分片与拓扑通信，改变 KD runtime partition contract。 由 TRAIN-DISTRIBUTED-TRAINING 持有 partition、topology、version 与 synchronization；相邻节点只消费版本化 handoff。

**Evaluation：证明与未证明。** These results showed that exploiting teacher--student asymmetry through topology-aware parallelism notably accelerated GKD training on production HPC clusters at our company Method=https://arxiv.org/html/2606.27797v1 — §Optimizing Teacher-Student Partitioning for Scalable Knowledge Distillation on HPC Systems; 2 Background: LLM Training and Parallelism; 2.1 LLM Training；Evaluation=https://arxiv.org/html/2606.27797v1 — §3 Testing Setup; 4 GKD Analysis and Improvements; 4.1 Experimental Results。评测合同逐字段冻结，未公开项才写 Not Disclosed。

**Trade-off、failure、fallback、coexistence 与 evolution。** exact-v1 的结论只覆盖《Optimizing Teacher-Student Partitioning for Scalable Knowledge Distillation on HPC Systems》在 3 Testing Setup; 4 GKD Analysis and Improvements; 4.1 Experimental Results 声明的实验；它没有证明跨 model family、hardware/runtime、数据分布或未测 failure mode 的普遍成立。 非对称方案增加 handoff buffering 与 topology search；teacher/student footprint 相近时，共享方案仍更简单。 Counterevidence/limitation=https://arxiv.org/html/2606.27797v1 — §6 Conclusions。

<!-- claim:SF-2026-ARXIV-2606-27797:start -->
Claim boundary：仅 arXiv:2606.27797v1 与 official exact-v1 HTML；不使用 later version，不把 benchmark outcome 外推为生产 SLO。
<!-- claim:SF-2026-ARXIV-2606-27797:end -->
<!-- review:SF-2026-ARXIV-2606-27797:end -->

<!-- review:SF-2026-ARXIV-2606-27806:start -->
### 2606.27806 — Agent vs. Parametric World Models: Hybrid Planning for Reliable Language Agents

**问题、约束与旧路径。** Language agents plan by generating not only actions but also implicit predictions of how the world will change. These imagined state updates make agents flexible, but they also create a distinct failure mode: hallucinated state claims can be written into context and propagated across subsequent decisions. 旧路径在论文新增条件之外仍然合理。

**机制、state/data/control owner。** 以 parametric transition model 校验 agent imagined delta，并把 disagreement 变成 targeted revision gate。 由 AGENT-PLANNING 持有 world state、plan revision 与 executable commit；相邻节点只消费版本化 handoff。

**Evaluation：证明与未证明。** These results suggest that lightweight parametric transition models can serve as effective grounding mechanisms for language-agent planning without replacing semantic reasoning. Method=https://arxiv.org/html/2606.27806v1 — §Our approach: GILP.; LLM API ecosystem.; 4 Method: Grounded Iterative Language Planning；Evaluation=https://arxiv.org/html/2606.27806v1 — §5 Experiments; Setup.; Cost analysis.。评测合同逐字段冻结，未公开项才写 Not Disclosed。

**Trade-off、failure、fallback、coexistence 与 evolution。** These results suggest that lightweight parametric transition models can serve as effective grounding mechanisms for language-agent planning without replacing semantic reasoning. Learned transition verifier 可能与 planner 共享盲点，也不是 physics oracle；分歧或 OOD state 回退 environment validation 或人工复核。 Counterevidence/limitation=https://arxiv.org/html/2606.27806v1 — §6 Discussion; 7 Limitations; 8 Conclusion。

<!-- claim:SF-2026-ARXIV-2606-27806:start -->
Claim boundary：仅 arXiv:2606.27806v1 与 official exact-v1 HTML；不使用 later version，不把 benchmark outcome 外推为生产 SLO。
<!-- claim:SF-2026-ARXIV-2606-27806:end -->
<!-- review:SF-2026-ARXIV-2606-27806:end -->

<!-- review:SF-2026-ARXIV-2606-27814:start -->
### 2606.27814 — ATOD: Annealed Turn-Aware On-Policy Distillation for Multi-Turn Agentic Tasks

**问题、约束与旧路径。** Training small language-model agents for long-horizon interactive tasks requires both fast imitation and reward-driven improvement. On-policy distillation (OPD) provides dense teacher guidance and typically improves rapidly in the early stage, but its gains saturate once the student approaches the teacher, limiting the final performance ceiling. 旧路径在论文新增条件之外仍然合理。

**机制、state/data/control owner。** 在 multi-turn agent training 中按 competence/turn state 退火切换 on-policy distillation 与 environment reward。 由 TRAIN-GRPO 持有 trajectory、credit、teacher signal 与 update gate；相邻节点只消费版本化 handoff。

**Evaluation：证明与未证明。** Experiments on ALFWorld, WebShop, and Search-QA show that ATOD consistently outperforms competing post-training baselines: across the three student sizes, ATOD improves average success rate by 4.16 points over OPD and 23.62 points over GRPO, while surpassing the corresponding teacher models by 2.16 points. Method=https://arxiv.org/html/2606.27814v1 — §4 Method; 5.4 Training Dynamics and Diagnostic Metrics; Appendix A Method and Algorithmic Details；Evaluation=https://arxiv.org/html/2606.27814v1 — §5 Experiments; 5.1 Experimental Setup; Datasets & Benchmarks.。评测合同逐字段冻结，未公开项才写 Not Disclosed。

**Trade-off、failure、fallback、coexistence 与 evolution。** Experiments on ALFWorld, WebShop, and Search-QA show that ATOD consistently outperforms competing post-training baselines: across the three student sizes, ATOD improves average success rate by 4.16 points over OPD and 23.62 points over GRPO, while surpassing the corresponding teacher models by 2.16 points. 现有 owner 已覆盖同一长期原则，因此只作为受限反例或实例留在 Daily，不复制 Books 分支。 Counterevidence/limitation=https://arxiv.org/html/2606.27814v1 — §6 Conclusion。

<!-- claim:SF-2026-ARXIV-2606-27814:start -->
Claim boundary：仅 arXiv:2606.27814v1 与 official exact-v1 HTML；不使用 later version，不把 benchmark outcome 外推为生产 SLO。
<!-- claim:SF-2026-ARXIV-2606-27814:end -->
<!-- review:SF-2026-ARXIV-2606-27814:end -->

<!-- review:SF-2026-ARXIV-2606-27826:start -->
### 2606.27826 — NormAct: Benchmarking Embodied Agents' Proactive Compliance with Unspoken Social Norms

**问题、约束与旧路径。** Embodied agents driven by multimodal large language models (MLLMs) can often complete everyday tasks from visual observations, but goal achievement does not establish whether they proactively respect unstated social norms. Existing benchmarks assess explicit norm judgments or constrained behavior, but rarely test whether agents infer and apply scene-relevant norms during ordinary tasks. 旧路径在论文新增条件之外仍然合理。

**机制、state/data/control owner。** 把 embodied-agent goal success 与未明示社会规范的自主识别/遵守拆成渐进 guidance evaluation contract。 由 PLATFORM-EVALUATION-SYSTEM 持有 oracle、metric、slice 与结论发布；相邻节点只消费版本化 handoff。

**Evaluation：证明与未证明。** Across three MLLM planners, goal achievement substantially exceeds norm compliance without guidance (67.4% versus 24.7%), while both broad and rule-specific guidance improve compliance, indicating that planners can often comply when prompted but not reliably on their own. Method=https://arxiv.org/html/2606.27826v1 — §3.1 Benchmark Design; Appendix F NormPerceptor Training Data Details；Evaluation=https://arxiv.org/html/2606.27826v1 — §NormAct : A Benchmark for Hidden Social Norm Compliance in Embodied Planning; 2.1 Social Norm Evaluation in (M)LLMs; 3 The NormAct Benchmark。评测合同逐字段冻结，未公开项才写 Not Disclosed。

**Trade-off、failure、fallback、coexistence 与 evolution。** NormAct therefore supports the development of embodied agents that pursue everyday goals while proactively respecting unstated social norms. 现有 owner 已覆盖同一长期原则，因此只作为受限反例或实例留在 Daily，不复制 Books 分支。 Counterevidence/limitation=https://arxiv.org/html/2606.27826v1 — §7 Conclusion; Limitations。

<!-- claim:SF-2026-ARXIV-2606-27826:start -->
Claim boundary：仅 arXiv:2606.27826v1 与 official exact-v1 HTML；不使用 later version，不把 benchmark outcome 外推为生产 SLO。
<!-- claim:SF-2026-ARXIV-2606-27826:end -->
<!-- review:SF-2026-ARXIV-2606-27826:end -->

<!-- review:SF-2026-ARXIV-2606-27841:start -->
### 2606.27841 — WattLayer: Get Layers Right to Estimate Inference Energy of Neural Networks

**问题、约束与旧路径。** The widespread adoption of Artificial Intelligence (AI) has led to increasing concerns about energy consumption, yet there is a lack of standardized methodologies to accurately estimate AI inference energy consumption, particularly across various tasks and architectures. In this study, we propose a task independent, layer-wise energy estimation model for AI architectures. 旧路径在论文新增条件之外仍然合理。

**机制、state/data/control owner。** 把 inference energy estimation 从整模型 proxy 拆成可跨任务/架构迁移的 layer-wise measurement contract。 由 PLATFORM-COST 持有 measurement state、resource attribution 与 cost model；相邻节点只消费版本化 handoff。

**Evaluation：证明与未证明。** We further show that layer-wise decomposition generalize to new tasks without complete retraining, by leveraging shared layers across architectures. Method=https://arxiv.org/html/2606.27841v1 — §3 Methodology and Experimental Set-up; 3.2 Layer-Wise Energy Estimation Framework；Evaluation=https://arxiv.org/html/2606.27841v1 — §3 Methodology and Experimental Set-up; 3.1 Experimental Protocol; 4 Results。评测合同逐字段冻结，未公开项才写 Not Disclosed。

**Trade-off、failure、fallback、coexistence 与 evolution。** We further show that layer-wise decomposition generalize to new tasks without complete retraining, by leveraging shared layers across architectures. Layer recomposition 可能遗漏 fusion、memory hierarchy 与 concurrency interaction；生产真值仍由 whole-run meter 持有，漂移时重校 layer model。 Counterevidence/limitation=https://arxiv.org/html/2606.27841v1 — §5 Discussion; 6 Conclusion。

<!-- claim:SF-2026-ARXIV-2606-27841:start -->
Claim boundary：仅 arXiv:2606.27841v1 与 official exact-v1 HTML；不使用 later version，不把 benchmark outcome 外推为生产 SLO。
<!-- claim:SF-2026-ARXIV-2606-27841:end -->
<!-- review:SF-2026-ARXIV-2606-27841:end -->

<!-- review:SF-2026-ARXIV-2606-27866:start -->
### 2606.27866 — FlexMoE: One-for-All Nested Intra-Expert Pruning for MoE Language Models

**问题、约束与旧路径。** Mixture-of-Experts (MoE) language models scale model ability with sparsely activated experts, making this architecture a standard recipe for modern large models. However, sparse activation does not remove the deployment burden of storing and serving all experts, and the available deployment budget can vary substantially across devices, users, and workloads. 旧路径在论文新增条件之外仍然合理。

**机制、state/data/control owner。** 把一次性 MoE compression artifact 改成 nested subnet family 与可在线切换的 budget state。 由 MODEL-MOE 持有 expert capacity、nested subnet 与 routing budget；相邻节点只消费版本化 handoff。

**Evaluation：证明与未证明。** For deployment, our pruned subnetworks deliver real memory reduction and throughput gains, and further support realtime online budget switching with kernel-level co-design. Method=https://arxiv.org/html/2606.27866v1 — §3 Method; Clip FFN Forward Kernel Co-Design.; Toward Co-Designed Online Budget Scheduling.；Evaluation=https://arxiv.org/html/2606.27866v1 — §4 Experiments; 4.1 Experimental Setup; Implementation Details and Evaluation Tasks.。评测合同逐字段冻结，未公开项才写 Not Disclosed。

**Trade-off、failure、fallback、coexistence 与 evolution。** Specifically, on Qwen2-57B-A14B, our method retains ~99.8% of base performance while pruning 50% of routed expert parameters even without fine-tuning. 现有 owner 已覆盖同一长期原则，因此只作为受限反例或实例留在 Daily，不复制 Books 分支。 Counterevidence/limitation=https://arxiv.org/html/2606.27866v1 — §5 Conclusion; Limitations and Future Works.; A.2 Additional Discussion on Cross-Budget Transfer and Cross-Model Trends。

<!-- claim:SF-2026-ARXIV-2606-27866:start -->
Claim boundary：仅 arXiv:2606.27866v1 与 official exact-v1 HTML；不使用 later version，不把 benchmark outcome 外推为生产 SLO。
<!-- claim:SF-2026-ARXIV-2606-27866:end -->
<!-- review:SF-2026-ARXIV-2606-27866:end -->

<!-- review:SF-2026-ARXIV-2606-27906:start -->
### 2606.27906 — Phase Matters: Characterizing Heterogeneous Vision-Language Inference on a Mobile SoC

**问题、约束与旧路径。** Recent phone-class mobile SoCs expose practical NPU execution paths for on-device vision-language model (VLM) inference, but developers still lack phase-level guidance for mapping VLM pipelines across heterogeneous backends. We present a hardware-in-the-loop characterization of VLM inference on the Qualcomm SM8750 (Snapdragon 8 Elite), covering phase throughput, cache-state effects, 100-run thermal stability, energy, heterogeneous CPU/NPU pipeline configurations, and visual-token-budget sensitivity. 旧路径在论文新增条件之外仍然合理。

**机制、state/data/control owner。** 以真实 mobile SoC 证据拆开 vision encoder、prefill、decode、cache 与 thermal phase 的 backend placement。 由 INFER-REQUEST-LIFECYCLE 持有 request phase、runtime placement、queue 与 latency state；相邻节点只消费版本化 handoff。

**Evaluation：证明与未证明。** Finally, we show that a four-step graph rewrite enables previously unsupported encoders, such as Phi-3.5-V, to reach the QNN path with up to 22x speedup, providing a practical porting recipe for mobile VLM deployment. Method=https://arxiv.org/html/2606.27906v1 — §7.2. Methodology and Outcomes on Phi-3.5-V；Evaluation=https://arxiv.org/html/2606.27906v1 — §2. Platform and Experimental Setup; 3.1. Phase-Level Results; 6.1. Three-Backend Benchmark。评测合同逐字段冻结，未公开项才写 Not Disclosed。

**Trade-off、failure、fallback、coexistence 与 evolution。** Using FastVLM-0.5B as an end-to-end case study, together with encoder-only measurements across four architecture families, we show that phase matters: NPU execution is highly phase-dependent, delivering 1.64x speedup for prefill but only 1.18x for decode, while vision encoders achieve 20-45x speedups over CPU. Simulation 与 component latency 不证明生产 SLO 或 embodied success；mismatch、thermal drift 或 deadline miss 时回退已实测的保守 placement/control。 Counterevidence/limitation=https://arxiv.org/html/2606.27906v1 — §8. Discussion; 10. Conclusion。

<!-- claim:SF-2026-ARXIV-2606-27906:start -->
Claim boundary：仅 arXiv:2606.27906v1 与 official exact-v1 HTML；不使用 later version，不把 benchmark outcome 外推为生产 SLO。
<!-- claim:SF-2026-ARXIV-2606-27906:end -->
<!-- review:SF-2026-ARXIV-2606-27906:end -->

<!-- review:SF-2026-ARXIV-2606-27934:start -->
### 2606.27934 — Self-Verifying Measurement Records: Hash-Linked Evidence Graphs for Hardware Benchmarking

**问题、约束与旧路径。** Performance numbers reported for hardware are accepted on trust: the reader cannot recompute them, the apparatus is gone, and the silicon itself can be silently wrong, with fleet studies reporting on the order of one core in a thousand returning incorrect arithmetic with no error raised. We make a reported hardware measurement a tamper-evident, independently checkable record. 旧路径在论文新增条件之外仍然合理。

**机制、state/data/control owner。** 用 hash-linked measurement/evidence graph 与 output-derived challenge 让硬件 benchmark 可离线验证。 由 PLATFORM-EVALUATION-SYSTEM 持有 oracle、metric、slice 与结论发布；相邻节点只消费版本化 handoff。

**Evaluation：证明与未证明。** We demonstrate the construction across Blackwell and Hopper GPUs and report a residual-floor and reproducibility map by precision, size, and device. Method=https://arxiv.org/html/2606.27934v1 — §Approach.；Evaluation=https://arxiv.org/html/2606.27934v1 — §Self-Verifying Measurement Records: Hash-Linked Evidence Graphs for Hardware Benchmarking。评测合同逐字段冻结，未公开项才写 Not Disclosed。

**Trade-off、failure、fallback、coexistence 与 evolution。** We then treat the check itself as a security object: a probe seed committed for offline reproducibility is an attack surface, and a probe-aware adversary can hide a corruption in the probe's null space, fooling even a quorum of bit-identical witnesses, while a Fiat-Shamir challenge derived from the claimed output closes this. 现有 owner 已覆盖同一长期原则，因此只作为受限反例或实例留在 Daily，不复制 Books 分支。 Counterevidence/limitation=https://arxiv.org/html/2606.27934v1 — §10 Threat model and guarantees; 12 Physical stress and the trust boundary; 14 Scope and limitations。

<!-- claim:SF-2026-ARXIV-2606-27934:start -->
Claim boundary：仅 arXiv:2606.27934v1 与 official exact-v1 HTML；不使用 later version，不把 benchmark outcome 外推为生产 SLO。
<!-- claim:SF-2026-ARXIV-2606-27934:end -->
<!-- review:SF-2026-ARXIV-2606-27934:end -->

<!-- review:SF-2026-ARXIV-2606-27936:start -->
### 2606.27936 — Agentic AI-Powered Re-Identification: An Emerging, Scalable Threat to Mobility Microdata Privacy

**问题、约束与旧路径。** The widespread collection of fine-grained location data by commercial data brokers creates a re-identification risk that is not widely recognised by the public. While prior research has established that mobility traces are highly unique and that individuals can, in principle, be identified from a handful of spatio-temporal points, such attacks have historically required significant manual effort from skilled analysts, limiting their practical scale. 旧路径在论文新增条件之外仍然合理。

**机制、state/data/control owner。** 证明 agentic open-web resolution 把 mobility re-identification 从专家手工能力改成可规模化 threat model。 由 PLATFORM-SECURITY 持有 authority envelope、untrusted input 与 release gate；相邻节点只消费版本化 handoff。

**Evaluation：证明与未证明。** Our results demonstrate that, from spatio-temporal data and public sources alone, our agentic AI successfully re-identified 18 of the 25 re-identifiable individuals (72%) and 18 of 43 cases overall (41.9%). Method=https://arxiv.org/html/2606.27936v1 — §3 Methodology; 3.2 Study Design and Simulated Data；Evaluation=https://arxiv.org/html/2606.27936v1 — §4 Results。评测合同逐字段冻结，未公开项才写 Not Disclosed。

**Trade-off、failure、fallback、coexistence 与 evolution。** We present an end-to-end pipeline in which large language model agents autonomously search the open web, cross-reference public records and social media, and resolve raw coordinate sequences to candidate identities - without human intervention. 现有 owner 已覆盖同一长期原则，因此只作为受限反例或实例留在 Daily，不复制 Books 分支。 Counterevidence/limitation=https://arxiv.org/html/2606.27936v1 — §Agentic AI-Powered Re-Identification: An Emerging, Scalable Threat to Mobility Microdata Privacy; Threat model.; 5 Discussion and Conclusion。

<!-- claim:SF-2026-ARXIV-2606-27936:start -->
Claim boundary：仅 arXiv:2606.27936v1 与 official exact-v1 HTML；不使用 later version，不把 benchmark outcome 外推为生产 SLO。
<!-- claim:SF-2026-ARXIV-2606-27936:end -->
<!-- review:SF-2026-ARXIV-2606-27936:end -->

<!-- review:SF-2026-ARXIV-2606-27944:start -->
### 2606.27944 — It Lied to a Doctor to Buy Poison Ingredients: Quantifying Real-World Misuse of Phone-use Agents

**问题、约束与旧路径。** Phone-use Agents can execute complex tasks end to end across real mobile applications. By operating a real device on the user's behalf, they reach far more functionalities than CLI agents, which amplifies the real-world harm they can cause when driven for malicious purposes. 旧路径在论文新增条件之外仍然合理。

**机制、state/data/control owner。** 以真实 phone/app side effects 揭示 safety awareness 与 execution authorization 分离后的 misuse failure。 由 PLATFORM-SECURITY 持有 authority envelope、untrusted input 与 release gate；相邻节点只消费版本化 handoff。

**Evaluation：证明与未证明。** Simple defenses curb the overt cases, but the more covert and arguably more damaging threats, such as coordinated review manipulation and fake traffic, remain largely unsolved. Method=https://arxiv.org/html/2606.27944v1 — §4 Misuse Collection and the Awareness-to-Action Evaluation Framework; 4.3 Evaluation Framework；Evaluation=https://arxiv.org/html/2606.27944v1 — §4 Misuse Collection and the Awareness-to-Action Evaluation Framework; 4.3 Evaluation Framework; 5 Evaluation Results。评测合同逐字段冻结，未公开项才写 Not Disclosed。

**Trade-off、failure、fallback、coexistence 与 evolution。** Simple defenses curb the overt cases, but the more covert and arguably more damaging threats, such as coordinated review manipulation and fake traffic, remain largely unsolved. 现有 owner 已覆盖同一长期原则，因此只作为受限反例或实例留在 Daily，不复制 Books 分支。 Counterevidence/limitation=https://arxiv.org/html/2606.27944v1 — §3 Threat Model; 8 Discussion and Limitation; 9 Conclusion。

<!-- claim:SF-2026-ARXIV-2606-27944:start -->
Claim boundary：仅 arXiv:2606.27944v1 与 official exact-v1 HTML；不使用 later version，不把 benchmark outcome 外推为生产 SLO。
<!-- claim:SF-2026-ARXIV-2606-27944:end -->
<!-- review:SF-2026-ARXIV-2606-27944:end -->

<!-- review:SF-2026-ARXIV-2606-27962:start -->
### 2606.27962 — Building a Scalable, Reproducible, Evaluatable, and Closed-Loop Simulation Environment Foundation for Embodied Intelligence

**问题、约束与旧路径。** This paper presents a cloud-native simulation infrastructure framework for embodied intelligence that supports large-scale training, standardized evaluation, and simulation-based data collection. The framework unifies simulation environment generation, task execution, trajectory collection, model evaluation, data management, and cloud services into a scalable and reproducible platform. 旧路径在论文新增条件之外仍然合理。

**机制、state/data/control owner。** 把 embodied simulation 的 environment、trajectory、evaluation、data 与 elastic cloud scheduling 统一成闭环平台。 由 PLATFORM-FOUNDATIONS 持有 environment、artifact、scheduler 与 lifecycle control；相邻节点只消费版本化 handoff。

**Evaluation：证明与未证明。** We argue that cloud-native simulation infrastructure provides a unified foundation for data generation, model training, standardized evaluation, and real-world deployment, and will play a key role in the future development of embodied intelligence. Method=https://arxiv.org/html/2606.27962v1 — §Building a Scalable, Reproducible, Evaluatable, and Closed-Loop Simulation Environment Foundation for Embodied Intelligence Cloud-Native Simulation Infrastructure for Embodied Intelligence Training, Evaluation, and Data Collection; 2 Overall Positioning and Design Principles; 2.3 Design Principles；Evaluation=https://arxiv.org/html/2606.27962v1 — §Building a Scalable, Reproducible, Evaluatable, and Closed-Loop Simulation Environment Foundation for Embodied Intelligence Cloud-Native Simulation Infrastructure for Embodied Intelligence Training, Evaluation, and Data Collection; 1.2 Bottlenecks in Real Robot Data and Evaluation; 3.2 Mainstream Benchmarks and Datasets。评测合同逐字段冻结，未公开项才写 Not Disclosed。

**Trade-off、failure、fallback、coexistence 与 evolution。** exact-v1 的结论只覆盖《Building a Scalable, Reproducible, Evaluatable, and Closed-Loop Simulation Environment Foundation for Embodied Intelligence》在 Building a Scalable, Reproducible, Evaluatable, and Closed-Loop Simulation Environment Foundation for Embodied Intelligence Cloud-Native Simulation Infrastructure for Embodied Intelligence Training, Evaluation, and Data Collection; 1.2 Bottlenecks in Real Robot Data and Evaluation; 3.2 Mainstream Benchmarks and Datasets 声明的实验；它没有证明跨 model family、hardware/runtime、数据分布或未测 failure mode 的普遍成立。 现有 owner 已覆盖同一长期原则，因此只作为受限反例或实例留在 Daily，不复制 Books 分支。 Counterevidence/limitation=https://arxiv.org/html/2606.27962v1 — §3.3 Limitations of Current Solutions; 6.5 Failure Data and Corrective Data。

<!-- claim:SF-2026-ARXIV-2606-27962:start -->
Claim boundary：仅 arXiv:2606.27962v1 与 official exact-v1 HTML；不使用 later version，不把 benchmark outcome 外推为生产 SLO。
<!-- claim:SF-2026-ARXIV-2606-27962:end -->
<!-- review:SF-2026-ARXIV-2606-27962:end -->

<!-- review:SF-2026-ARXIV-2606-27976:start -->
### 2606.27976 — SHARD: cell-keyed residual splitting for alignment-resistant private dense retrieval

**问题、约束与旧路径。** Dense retrieval systems expose document geometry when vector stores are compromised, and a global protective transform can often be aligned from known pairs. We study SHARD, which splits PCA coordinates into a short routing prefix and a residual protected by independent cell-local orthogonal keys. 旧路径在论文新增条件之外仍然合理。

**机制、state/data/control owner。** 把 private dense retrieval 的 routing prefix、cell-local residual key、CKKS rerank 与 linkage risk 分开声明。 由 AGENT-RAG 持有 retrieval index、privacy boundary 与 evidence handoff；相邻节点只消费版本化 handoff。

**Evaluation：证明与未证明。** It supports CKKS ciphertext--plaintext reranking but is evaluated as a leakage trade-off, not a cryptographic document-privacy guarantee. Method=https://arxiv.org/html/2606.27976v1 — §Appendix A Reproduced baseline analyses from the global-linear system；Evaluation=https://arxiv.org/html/2606.27976v1 — §8 Experiments; Integral multi-encoder evaluation at 10 6 10^{6} scale.。评测合同逐字段冻结，未公开项才写 Not Disclosed。

**Trade-off、failure、fallback、coexistence 与 evolution。** SHARD preserves retrieval and compartmentalizes alignment evidence, but does not provide DP, unlinkability, or cancellable templates. 现有 owner 已覆盖同一长期原则，因此只作为受限反例或实例留在 Daily，不复制 Books 分支。 Counterevidence/limitation=https://arxiv.org/html/2606.27976v1 — §3 Threat Model; A measured limitation: overlap reference lookup.; 9 Discussion。

<!-- claim:SF-2026-ARXIV-2606-27976:start -->
Claim boundary：仅 arXiv:2606.27976v1 与 official exact-v1 HTML；不使用 later version，不把 benchmark outcome 外推为生产 SLO。
<!-- claim:SF-2026-ARXIV-2606-27976:end -->
<!-- review:SF-2026-ARXIV-2606-27976:end -->

<!-- review:SF-2026-ARXIV-2606-27997:start -->
### 2606.27997 — Benchmarking on Tasks That Matter: Dataset Selection for Preserving Model Rankings

**问题、约束与旧路径。** Benchmarks of machine learning models often include many datasets, making evaluation expensive. For efficiency, it is preferable to perform evaluations on small, representative datasets instead. 旧路径在论文新增条件之外仍然合理。

**机制、state/data/control owner。** 把 benchmark task subset selection 绑定 rank-preservation uncertainty，而非把少量数据集当作无损代理。 由 PLATFORM-EVALUATION-SYSTEM 持有 oracle、metric、slice 与结论发布；相邻节点只消费版本化 handoff。

**Evaluation：证明与未证明。** Additional experiments indicate that the effectiveness of selection approaches depends on both the quality of dataset representations and the scale of the benchmarking regime. Method=https://arxiv.org/html/2606.27997v1 — §5.1. Evaluation methodology; Recommender Systems.; Recommender Systems；Evaluation=https://arxiv.org/html/2606.27997v1 — §Benchmarking on Tasks That Matter: Dataset Selection for Preserving Model Rankings; Benchmark Setting; Theoretical results summary。评测合同逐字段冻结，未公开项才写 Not Disclosed。

**Trade-off、failure、fallback、coexistence 与 evolution。** For TSC, our best-performing strategy achieves a Spearman correlation of 0.95 with the full benchmark model rankings using only five selected datasets. 现有 owner 已覆盖同一长期原则，因此只作为受限反例或实例留在 Daily，不复制 Books 分支。 Counterevidence/limitation=https://arxiv.org/html/2606.27997v1 — §7. Conclusions and discussion。

<!-- claim:SF-2026-ARXIV-2606-27997:start -->
Claim boundary：仅 arXiv:2606.27997v1 与 official exact-v1 HTML；不使用 later version，不把 benchmark outcome 外推为生产 SLO。
<!-- claim:SF-2026-ARXIV-2606-27997:end -->
<!-- review:SF-2026-ARXIV-2606-27997:end -->

<!-- review:SF-2026-ARXIV-2606-28011:start -->
### 2606.28011 — From Detection to Action: Using LLM Agents for Fault-Tolerant Control

**问题、约束与旧路径。** We propose an agentic Large Language Model (LLM) framework for active Fault-Tolerant Control (FTC) that transforms fault detection outputs into constraint-aware recovery actions grounded in plant-specific knowledge. The approach couples (i) a multi-agent workflow that decomposes operator duties into monitoring, planning, action synthesis, simulation, validation, and reprompting; (ii) a Digital Process Plant Twin (DPPT) that exposes plant data, models, and a simulation service for pre-execution testing; and (iii) a Graph Retrieval-Augmented Generation (Graph RAG) layer built on the CPSMod ontology, which organizes plant knowledge (structure, function, hybrid dynamics, control context, and fault semantics) into a graph that supports relation-aware, multi-hop retrieval for the agents. 旧路径在论文新增条件之外仍然合理。

**机制、state/data/control owner。** 把 LLM recovery proposal 放在 plant twin simulation、deterministic interlock validation 与 bounded fallback 之后。 由 AGENT-WORKFLOW 持有 artifact state、verifier/interlock 与 fallback；相邻节点只消费版本化 handoff。

**Evaluation：证明与未证明。** Results with lightweight LLMs (GPT-4o-mini and GPT-4.1-mini) show that semantically grounded agents can derive valid recovery decisions within latency budgets compatible with the respective process dynamics, demonstrating a practical pathway from detection to validated corrective action across both discrete and continuous FTC tasks. Method=https://arxiv.org/html/2606.28011v1 — §3 LLM-based agentic framework for fault-tolerant control；Evaluation=https://arxiv.org/html/2606.28011v1 — §4.3 Evaluation criteria; 5 Results; 5.1 Mixing module results。评测合同逐字段冻结，未公开项才写 Not Disclosed。

**Trade-off、failure、fallback、coexistence 与 evolution。** exact-v1 的结论只覆盖《From Detection to Action: Using LLM Agents for Fault-Tolerant Control》在 4.3 Evaluation criteria; 5 Results; 5.1 Mixing module results 声明的实验；它没有证明跨 model family、hardware/runtime、数据分布或未测 failure mode 的普遍成立。 现有 owner 已覆盖同一长期原则，因此只作为受限反例或实例留在 Daily，不复制 Books 分支。 Counterevidence/limitation=https://arxiv.org/html/2606.28011v1 — §6 Discussion。

<!-- claim:SF-2026-ARXIV-2606-28011:start -->
Claim boundary：仅 arXiv:2606.28011v1 与 official exact-v1 HTML；不使用 later version，不把 benchmark outcome 外推为生产 SLO。
<!-- claim:SF-2026-ARXIV-2606-28011:end -->
<!-- review:SF-2026-ARXIV-2606-28011:end -->

<!-- review:SF-2026-ARXIV-2606-28013:start -->
### 2606.28013 — The Signal-Coverage Matrix: Stratifying Type and Semantic Errors in Statement Autoformalization

**问题、约束与旧路径。** Headline type-correctness (TC\%) of LLM autoformalization has climbed from $\sim$53\% to $\sim$76\% in two years, yet this scalar conceals which errors each method resolves. We propose a signal-coverage matrix that crosses the Lean elaborator (pass/fail) with a semantic-equivalence judgment (equivalent/not), sorting every output into one of four cells: true success (TS), type-only (TO), semantic-only (SO), or both fail (BF). 旧路径在论文新增条件之外仍然合理。

**机制、state/data/control owner。** 把 autoformalization 的 type correctness 与 semantic equivalence 交叉分层，防止单标量误归因。 由 PLATFORM-EVALUATION-SYSTEM 持有 oracle、metric、slice 与结论发布；相邻节点只消费版本化 handoff。

**Evaluation：证明与未证明。** We propose a signal-coverage matrix that crosses the Lean elaborator (pass/fail) with a semantic-equivalence judgment (equivalent/not), sorting every output into one of four cells: true success (TS), type-only (TO), semantic-only (SO), or both fail (BF). Method=https://arxiv.org/html/2606.28013v1 — §Methods.; 5.1 Per-method cell decomposition; 5.4 A predictive regularity: stratum-rates are method-invariant；Evaluation=https://arxiv.org/html/2606.28013v1 — §4 Experimental Setup; 5 Experimental Results and Analysis。评测合同逐字段冻结，未公开项才写 Not Disclosed。

**Trade-off、failure、fallback、coexistence 与 evolution。** We propose a signal-coverage matrix that crosses the Lean elaborator (pass/fail) with a semantic-equivalence judgment (equivalent/not), sorting every output into one of four cells: true success (TS), type-only (TO), semantic-only (SO), or both fail (BF). Semantic judge 与 selector 都可能错误或相关；uncovered/undecidable 必须保持 Unknown，高风险分歧交回独立 verification 或人工。 Counterevidence/limitation=https://arxiv.org/html/2606.28013v1 — §6 Discussion and Limitations; 7 Conclusion。

<!-- claim:SF-2026-ARXIV-2606-28013:start -->
Claim boundary：仅 arXiv:2606.28013v1 与 official exact-v1 HTML；不使用 later version，不把 benchmark outcome 外推为生产 SLO。
<!-- claim:SF-2026-ARXIV-2606-28013:end -->
<!-- review:SF-2026-ARXIV-2606-28013:end -->

<!-- review:SF-2026-ARXIV-2606-28037:start -->
### 2606.28037 — Evolution-Aware Regression Test Prioritization of ML-Enabled Systems Using Gradient-Based Behavior Vectors

**问题、约束与旧路径。** The machine learning(ML) component of an ML-enabled system evolves through retraining, fine-tuning, and optimization, so previously valid test results may no longer hold. A single evolution step can worsen performance on some test cases while improving others, making regression test prioritization inherently directional. 旧路径在论文新增条件之外仍然合理。

**机制、state/data/control owner。** 以原模型 gradient behavior vector 和 parameter delta 做 evolution-aware regression-test prioritization。 由 PLATFORM-EVALUATION-SYSTEM 持有 oracle、metric、slice 与结论发布；相邻节点只消费版本化 handoff。

**Evaluation：证明与未证明。** These results show that behavior-space ideas can be operationalized into a practical and efficient mechanism for repeated-update regression testing of evolving ML-enabled systems. Method=https://arxiv.org/html/2606.28037v1 — §Evolution-Aware Regression Test Prioritization of ML-Enabled Systems Using Gradient-Based Behavior Vectors; 4.1.1. Tasks, Datasets, and Model Architectures；Evaluation=https://arxiv.org/html/2606.28037v1 — §4. Evaluation; 4.1. Experiment Setup; 4.1.5. Reproducibility and Additional Results。评测合同逐字段冻结，未公开项才写 Not Disclosed。

**Trade-off、failure、fallback、coexistence 与 evolution。** In an empirical study across classification and regression tasks, GBV-PD consistently outperformed non-directional baselines and remained competitive with a full-gradient reference, while offering better time and storage profiles for repeated updates via reusable GBV caching. 现有 owner 已覆盖同一长期原则，因此只作为受限反例或实例留在 Daily，不复制 Books 分支。 Counterevidence/limitation=https://arxiv.org/html/2606.28037v1 — §5. Discussion; 5.3. Limitations; 6. Threats to Validity。

<!-- claim:SF-2026-ARXIV-2606-28037:start -->
Claim boundary：仅 arXiv:2606.28037v1 与 official exact-v1 HTML；不使用 later version，不把 benchmark outcome 外推为生产 SLO。
<!-- claim:SF-2026-ARXIV-2606-28037:end -->
<!-- review:SF-2026-ARXIV-2606-28037:end -->

<!-- review:SF-2026-ARXIV-2606-28050:start -->
### 2606.28050 — Can LLMs Judge Better Than They Generate? Evaluating Task Asymmetry, Mechanistic Interpretability and Transferability for In-Context QA

**问题、约束与旧路径。** LLM-as-a-Judge and self-evaluation pipelines implicitly assume that evaluation is easier than generation. We test this in a controlled in-context QA setting where a context passage is the sole information source and each model judges the answer it generated, removing the parametric-knowledge confound of open-domain comparisons. 旧路径在论文新增条件之外仍然合理。

**机制、state/data/control owner。** 用 controlled in-context QA 反证 self-evaluation 普遍比 generation 更容易的默认假设。 由 PLATFORM-EVALUATION-SYSTEM 持有 oracle、metric、slice 与结论发布；相邻节点只消费版本化 handoff。

**Evaluation：证明与未证明。** These findings challenge core assumptions in self-evaluation pipelines. Method=https://arxiv.org/html/2606.28050v1 — §3 Methodology; Hard-negative generation for evaluator training.; LoRA training budget.；Evaluation=https://arxiv.org/html/2606.28050v1 — §Generation–evaluation asymmetry.; 3.1 Task Asymmetry Analysis; Evaluation task ( 𝒯 eval \mathcal{T}_{\text{eval}} ).。评测合同逐字段冻结，未公开项才写 Not Disclosed。

**Trade-off、failure、fallback、coexistence 与 evolution。** exact-v1 的结论只覆盖《Can LLMs Judge Better Than They Generate? Evaluating Task Asymmetry, Mechanistic Interpretability and Transferability for In-Context QA》在 Generation–evaluation asymmetry.; 3.1 Task Asymmetry Analysis; Evaluation task ( 𝒯 eval \mathcal{T}_{\text{eval}} ). 声明的实验；它没有证明跨 model family、hardware/runtime、数据分布或未测 failure mode 的普遍成立。 现有 owner 已覆盖同一长期原则，因此只作为受限反例或实例留在 Daily，不复制 Books 分支。 Counterevidence/limitation=https://arxiv.org/html/2606.28050v1 — §5 Results and Discussion; 6 Conclusion; Limitations。

<!-- claim:SF-2026-ARXIV-2606-28050:start -->
Claim boundary：仅 arXiv:2606.28050v1 与 official exact-v1 HTML；不使用 later version，不把 benchmark outcome 外推为生产 SLO。
<!-- claim:SF-2026-ARXIV-2606-28050:end -->
<!-- review:SF-2026-ARXIV-2606-28050:end -->

<!-- review:SF-2026-ARXIV-2606-28061:start -->
### 2606.28061 — ToolPrivacyBench: Benchmarking Purpose-Bound Privacy in Tool-Using LLM Agents

**问题、约束与旧路径。** Large language models (LLMs) have increasingly moved from standalone text generation systems to agents that invoke external tools, access environments, and execute multi-step tasks. However, conventional function-calling benchmarks mainly evaluate task completion and API correctness, while privacy evaluation benchmarks typically focus on final responses or privacy judgments. 旧路径在论文新增条件之外仍然合理。

**机制、state/data/control owner。** 把 tool-agent privacy 从最终文本扩展到每个 tool argument、sink 与 purpose-bound information flow。 由 PLATFORM-SECURITY 持有 authority envelope、untrusted input 与 release gate；相邻节点只消费版本化 handoff。

**Evaluation：证明与未证明。** The results show that successful tool execution does not imply appropriate privacy disclosure: an agent may complete a task while transmitting unnecessary private information through intermediate tool calls. Method=https://arxiv.org/html/2606.28061v1 — §4.7 System Modules；Evaluation=https://arxiv.org/html/2606.28061v1 — §ToolPrivacyBench: Benchmarking Purpose-Bound Privacy in Tool-Using LLM Agents Note: This work was supported by the Beijing Advanced Innovation Center for Future Blockchain and Privacy Computing (GJJ-25-009).; 2.1 Privacy Evaluation of Large Language Models; 2.2 Tool-Using Agents and Agent Benchmarks。评测合同逐字段冻结，未公开项才写 Not Disclosed。

**Trade-off、failure、fallback、coexistence 与 evolution。** ToolPrivacyBench therefore formalizes a need-to-know disclosure boundary, under which each tool should receive only the information necessary for its stated purpose, and uses trajectory-level auditing to identify privacy over-disclosure in multi-tool workflows. 现有 owner 已覆盖同一长期原则，因此只作为受限反例或实例留在 Daily，不复制 Books 分支。 Counterevidence/limitation=https://arxiv.org/html/2606.28061v1 — §8 Representative Failure Cases; 9 Discussion and Implications; 10 Conclusion。

<!-- claim:SF-2026-ARXIV-2606-28061:start -->
Claim boundary：仅 arXiv:2606.28061v1 与 official exact-v1 HTML；不使用 later version，不把 benchmark outcome 外推为生产 SLO。
<!-- claim:SF-2026-ARXIV-2606-28061:end -->
<!-- review:SF-2026-ARXIV-2606-28061:end -->

<!-- review:SF-2026-ARXIV-2606-28070:start -->
### 2606.28070 — JD Oxygen AI Item Center (Oxygen AIIC) V1: An Industrial-Scale LLM/VLM-Centric Solution for Item Understanding, Management, and Applications

**问题、约束与旧路径。** JD$.$com, one of the world's largest e-commerce platforms, serves over 700 million active users and millions of merchants, with a catalog of tens of billions of SKUs. At this scale, high-quality, structured item knowledge underpins a better consumer experience, lower management costs, and higher operational efficiency-yet producing and serving it poses three industrial-scale challenges: fast-emerging concepts, high-quality knowledge production for massive SKUs, and diverse downstream requirements. 旧路径在论文新增条件之外仍然合理。

**机制、state/data/control owner。** 提供 ontology、knowledge production、model evolution、unified data/service tunnel 在工业规模下的统一平台合同。 由 PLATFORM-FOUNDATIONS 持有 environment、artifact、scheduler 与 lifecycle control；相邻节点只消费版本化 handoff。

**Evaluation：证明与未证明。** Search-traffic coverage reaches 80.4%, item-information quality issues drop by 37%, the automated fill rate of core attributes during item listing exceeds 80%. Method=https://arxiv.org/html/2606.28070v1 — §2 Architecture Overview; 3.1 Method Overview; 3.2.2 Algorithm-driven ontology growth (bottom-up)；Evaluation=https://arxiv.org/html/2606.28070v1 — §3.3 Results; 4.2.3 Results; Module 1: Data evaluation.。评测合同逐字段冻结，未公开项才写 Not Disclosed。

**Trade-off、failure、fallback、coexistence 与 evolution。** exact-v1 的结论只覆盖《JD Oxygen AI Item Center (Oxygen AIIC) V1: An Industrial-Scale LLM/VLM-Centric Solution for Item Understanding, Management, and Applications》在 3.3 Results; 4.2.3 Results; Module 1: Data evaluation. 声明的实验；它没有证明跨 model family、hardware/runtime、数据分布或未测 failure mode 的普遍成立。 现有 owner 已覆盖同一长期原则，因此只作为受限反例或实例留在 Daily，不复制 Books 分支。 Counterevidence/limitation=https://arxiv.org/html/2606.28070v1 — §9 Conclusion; 10 Limitations and Future Work。

<!-- claim:SF-2026-ARXIV-2606-28070:start -->
Claim boundary：仅 arXiv:2606.28070v1 与 official exact-v1 HTML；不使用 later version，不把 benchmark outcome 外推为生产 SLO。
<!-- claim:SF-2026-ARXIV-2606-28070:end -->
<!-- review:SF-2026-ARXIV-2606-28070:end -->

<!-- review:SF-2026-ARXIV-2606-28116:start -->
### 2606.28116 — Mechanism-Driven Monitors for Preemptive Detection of LLM Training Instability

**问题、约束与旧路径。** Frontier large language model training consumes massive accelerator fleets and long wall-clock computation, making stability failures costly when they occur. After a numerical or a hyperparameter fault has already destabilized the training dynamics, it may continue for thousands of steps while loss and gradient norms still appear normal. 旧路径在论文新增条件之外仍然合理。

**机制、state/data/control owner。** 从 attention/router 的故障机理导出 pre-loss training-instability sensors，而非等待 loss collapse。 由 PLATFORM-MONITORING 持有 sensor state、calibration 与 alarm action；相邻节点只消费版本化 handoff。

**Evaluation：证明与未证明。** Our fault-injection experiments on low-precision attention, large learning-rate, and combined faults show that these signals provide distinct signatures for different failures, triggering thousands of steps before loss divergence. Method=https://arxiv.org/html/2606.28116v1 — §Mechanism-Driven Monitors for Preemptive Detection of LLM Training Instability; Training-stability monitors.; 5 Designing Module-Specific Monitors from First Principles；Evaluation=https://arxiv.org/html/2606.28116v1 — §Mechanism-Driven Monitors for Preemptive Detection of LLM Training Instability; 1 Introduction。评测合同逐字段冻结，未公开项才写 Not Disclosed。

**Trade-off、failure、fallback、coexistence 与 evolution。** After a numerical or a hyperparameter fault has already destabilized the training dynamics, it may continue for thousands of steps while loss and gradient norms still appear normal. Pre-loss signal 可能噪声大且依赖 family；它们保持 observe-first，缺失校准时 abstain，不能自动干预训练。 Counterevidence/limitation=https://arxiv.org/html/2606.28116v1 — §6 Limitations; 7 Conclusion。

<!-- claim:SF-2026-ARXIV-2606-28116:start -->
Claim boundary：仅 arXiv:2606.28116v1 与 official exact-v1 HTML；不使用 later version，不把 benchmark outcome 外推为生产 SLO。
<!-- claim:SF-2026-ARXIV-2606-28116:end -->
<!-- review:SF-2026-ARXIV-2606-28116:end -->

<!-- review:SF-2026-ARXIV-2606-28128:start -->
### 2606.28128 — PhysisForcing: Physics Reinforced World Simulator for Robotic Manipulation

**问题、约束与旧路径。** Video generation models have emerged as a promising paradigm for embodied world simulation. However, both general-domain video generators and robot-specific data fine-tuned models can still produce physically implausible manipulations, including discontinuous motion trajectories and inconsistent robot-object interactions, which limits their reliability as world simulators. 旧路径在论文新增条件之外仍然合理。

**机制、state/data/control owner。** 把 video-world-simulator 的 contact/trajectory physics supervision 与 downstream closed-loop policy effect 联结。 由 MULTIMODAL-WORLD-MODELS 持有 belief/latent state、transition 与 physical boundary；相邻节点只消费版本化 handoff。

**Evaluation：证明与未证明。** Beyond generation, as a world model under the WorldArena action-planner protocol it raises the closed-loop success rate from 16.0\% to 24.0\% and further improves downstream policy success, indicating that physically aligned video models yield stronger representations for robotic manipulation. Method=https://arxiv.org/html/2606.28128v1 — §3 Method; 3.4 Training and Inference; Training data.；Evaluation=https://arxiv.org/html/2606.28128v1 — §4 Experiments; 4.1 Experimental Setup; Benchmarks.。评测合同逐字段冻结，未公开项才写 Not Disclosed。

**Trade-off、failure、fallback、coexistence 与 evolution。** However, both general-domain video generators and robot-specific data fine-tuned models can still produce physically implausible manipulations, including discontinuous motion trajectories and inconsistent robot-object interactions, which limits their reliability as world simulators. 现有 owner 已覆盖同一长期原则，因此只作为受限反例或实例留在 Daily，不复制 Books 分支。 Counterevidence/limitation=https://arxiv.org/html/2606.28128v1 — §5 Conclusion; Appendix F Limitations and future work。

<!-- claim:SF-2026-ARXIV-2606-28128:start -->
Claim boundary：仅 arXiv:2606.28128v1 与 official exact-v1 HTML；不使用 later version，不把 benchmark outcome 外推为生产 SLO。
<!-- claim:SF-2026-ARXIV-2606-28128:end -->
<!-- review:SF-2026-ARXIV-2606-28128:end -->

<!-- review:SF-2026-ARXIV-2606-28153:start -->
### 2606.28153 — Robust Harmful Features Under Jailbreak Attacks: Mechanistic Evidence from Attention Head Specialization in Large Language Models

**问题、约束与旧路径。** Jailbreak attacks bypass LLM safety alignment, yet their mechanisms remain poorly understood. We provide evidence that attacks do not comprehensively eliminate safety features, but instead selectively suppress specific attention heads. 旧路径在论文新增条件之外仍然合理。

**机制、state/data/control owner。** 区分被攻击抑制与仍持续存在的 safety attention heads，并验证其 causal/monitoring 边界。 由 PLATFORM-SECURITY 持有 authority envelope、untrusted input 与 release gate；相邻节点只消费版本化 handoff。

**Evaluation：证明与未证明。** To validate the practical significance of this robustness, we show that simply reading these persistent activations -- without any training -- yields competitive aggregate detection performance with strong adversarial robustness. Method=https://arxiv.org/html/2606.28153v1 — §Detection-based methods; Perturbation-based methods; Representation-based methods；Evaluation=https://arxiv.org/html/2606.28153v1 — §4 Experiments; 4.1 Experimental Setup; Experimental Design。评测合同逐字段冻结，未公开项才写 Not Disclosed。

**Trade-off、failure、fallback、coexistence 与 evolution。** To validate the practical significance of this robustness, we show that simply reading these persistent activations -- without any training -- yields competitive aggregate detection performance with strong adversarial robustness. 现有 owner 已覆盖同一长期原则，因此只作为受限反例或实例留在 Daily，不复制 Books 分支。 Counterevidence/limitation=https://arxiv.org/html/2606.28153v1 — §6 Conclusion; Conclusions and practical guidance.; B.3 Limitations and Future Directions。

<!-- claim:SF-2026-ARXIV-2606-28153:start -->
Claim boundary：仅 arXiv:2606.28153v1 与 official exact-v1 HTML；不使用 later version，不把 benchmark outcome 外推为生产 SLO。
<!-- claim:SF-2026-ARXIV-2606-28153:end -->
<!-- review:SF-2026-ARXIV-2606-28153:end -->

<!-- review:SF-2026-ARXIV-2606-28166:start -->
### 2606.28166 — Tandem Reinforcement Learning with Verifiable Rewards

**问题、约束与旧路径。** Reinforcement learning with verifiable rewards (RLVR) has significantly improved the reasoning capability of large language models, reaching expert or even superhuman performance in domains such as competition math. However, whether weaker agents and humans can actually harness this capability is far less certain, with RLVR documented to drift reasoning toward idiosyncratic patterns such as poor readability and language mixing. 旧路径在论文新增条件之外仍然合理。

**机制、state/data/control owner。** 让 senior/junior 交替共同生成 RLVR rollout，把 handoff compatibility 变成训练目标。 由 TRAIN-GRPO 持有 trajectory、credit、teacher signal 与 update gate；相邻节点只消费版本化 handoff。

**Evaluation：证明与未证明。** Our results demonstrate a promising route for RLVR with practical payoffs in multi-model communication and human compatibility. Method=https://arxiv.org/html/2606.28166v1 — §3.1 Preliminaries: tandem training; 5.1 Training dynamics of TRL；Evaluation=https://arxiv.org/html/2606.28166v1 — §4 Results; 4.1 Experimental setup; Appendix B Additional Results。评测合同逐字段冻结，未公开项才写 Not Disclosed。

**Trade-off、failure、fallback、coexistence 与 evolution。** Training Qwen3-4B-Instruct on competition math, we find that TRL matches vanilla GRPO on solo reasoning capability while three properties emerge together from the same rollout structure: stronger handoff robustness with the junior, reduced distributional drift from the junior, and a chain-of-thought more legible to the junior. 该结果只保留为局部方法/实验语境；它不新增长期 owner、authority、coexistence 或 fallback 命题。 Counterevidence/limitation=https://arxiv.org/html/2606.28166v1 — §5 Discussion; 6 Conclusion。

<!-- claim:SF-2026-ARXIV-2606-28166:start -->
Claim boundary：仅 arXiv:2606.28166v1 与 official exact-v1 HTML；不使用 later version，不把 benchmark outcome 外推为生产 SLO。
<!-- claim:SF-2026-ARXIV-2606-28166:end -->
<!-- review:SF-2026-ARXIV-2606-28166:end -->

<!-- review:SF-2026-ARXIV-2606-28187:start -->
### 2606.28187 — GBC: Gradient-Based Connections for Optimizing Multi-Agent Systems

**问题、约束与旧路径。** Multi-agent systems (MAS) built on large language models (LLMs) provide a promising framework for solving complex tasks through role specialization and structured interaction. However, their performance is often limited by miscoordination and, more fundamentally, the lack of fine-grained credit assignment across agents. 旧路径在论文新增条件之外仍然合理。

**机制、state/data/control owner。** 把 multi-agent interaction 建成可反传 attribution graph，以 token-level influence 分配错误责任。 由 AGENT-MULTI-AGENT 持有 interaction graph、attribution 与 commit coordination；相邻节点只消费版本化 handoff。

**Evaluation：证明与未证明。** Experiments on MultiWOZ and τ-bench show that GBC improves multi-agent performance and outperforms strong single-agent and multi-agent baselines, and higher attribution quality is associated with greater optimization effectiveness. Method=https://arxiv.org/html/2606.28187v1 — §GBC: Gradient-Based Connections for Optimizing Multi-Agent Systems; 2.2 Multi-Agent System; 2.3 Multi-Agent System Optimization；Evaluation=https://arxiv.org/html/2606.28187v1 — §5 Experiment; Setup; Optimization Setup。评测合同逐字段冻结，未公开项才写 Not Disclosed。

**Trade-off、failure、fallback、coexistence 与 evolution。** However, their performance is often limited by miscoordination and, more fundamentally, the lack of fine-grained credit assignment across agents. 现有 owner 已覆盖同一长期原则，因此只作为受限反例或实例留在 Daily，不复制 Books 分支。 Counterevidence/limitation=https://arxiv.org/html/2606.28187v1 — §6 Conclusion; Limitations。

<!-- claim:SF-2026-ARXIV-2606-28187:start -->
Claim boundary：仅 arXiv:2606.28187v1 与 official exact-v1 HTML；不使用 later version，不把 benchmark outcome 外推为生产 SLO。
<!-- claim:SF-2026-ARXIV-2606-28187:end -->
<!-- review:SF-2026-ARXIV-2606-28187:end -->

<!-- review:SF-2026-ARXIV-2606-28235:start -->
### 2606.28235 — Govern the Repository, Not the Agent: Measuring Ecosystem-Level Risk in AI-Native Software

**问题、约束与旧路径。** Autonomous coding agents now open and merge pull requests in shared repositories at scale, and the field evaluates them the way it has always evaluated components, one agent at a time, on isolated benchmark tasks. Yet agents that each pass their own tests still leave repositories that accumulate problems no single contribution accounts for. 旧路径在论文新增条件之外仍然合理。

**机制、state/data/control owner。** 用大规模 PR 数据把 coding-agent 风险 owner 从单次 agent score 移到 repository-level integration friction。 由 AGENT-PLATFORM 持有 workspace、runtime、acceptance predicate 与 replay；相邻节点只消费版本化 handoff。

**Evaluation：证明与未证明。** Autonomous coding agents now open and merge pull requests in shared repositories at scale, and the field evaluates them the way it has always evaluated components, one agent at a time, on isolated benchmark tasks. Method=https://arxiv.org/html/2606.28235v1 — §Govern the Repository, Not the Agent: Measuring Ecosystem-Level Risk in AI-Native Software; II-C Software ecosystems and coordination cost; II-D Emergence and complex adaptive systems；Evaluation=https://arxiv.org/html/2606.28235v1 — §IV-B Level of analysis and why multilevel models; V Results。评测合同逐字段冻结，未公开项才写 Not Disclosed。

**Trade-off、failure、fallback、coexistence 与 evolution。** exact-v1 的结论只覆盖《Govern the Repository, Not the Agent: Measuring Ecosystem-Level Risk in AI-Native Software》在 IV-B Level of analysis and why multilevel models; V Results 声明的实验；它没有证明跨 model family、hardware/runtime、数据分布或未测 failure mode 的普遍成立。 现有 owner 已覆盖同一长期原则，因此只作为受限反例或实例留在 Daily，不复制 Books 分支。 Counterevidence/limitation=https://arxiv.org/html/2606.28235v1 — §VI Discussion; VII Threats to Validity; VIII Conclusion。

<!-- claim:SF-2026-ARXIV-2606-28235:start -->
Claim boundary：仅 arXiv:2606.28235v1 与 official exact-v1 HTML；不使用 later version，不把 benchmark outcome 外推为生产 SLO。
<!-- claim:SF-2026-ARXIV-2606-28235:end -->
<!-- review:SF-2026-ARXIV-2606-28235:end -->

<!-- review:SF-2026-ARXIV-2606-28276:start -->
### 2606.28276 — SimFoundry: Modular and Automated Scene Generation for Policy Learning and Evaluation

**问题、约束与旧路径。** Training and evaluating robot policies in the real world is costly and difficult to scale. We introduce SimFoundry, a modular and automated system for zero-shot real-to-sim scene construction from a video. 旧路径在论文新增条件之外仍然合理。

**机制、state/data/control owner。** 把 video-to-sim reconstruction、digital cousins、policy training 与 sim-to-real rank validity 绑定。 由 MULTIMODAL-EMBODIED-VLA 持有 scene state、policy evaluation 与 real-world commit；相邻节点只消费版本化 handoff。

**Evaluation：证明与未证明。** When evaluating sim-trained policies zero-shot in the real world, policies trained with object, scene, and task cousins in simulation show average task success rate improvements of 17%, 21%, and 40%, respectively. Method=https://arxiv.org/html/2606.28276v1 — §SimFoundry outperforms state-of-the-art simulation evaluation frameworks and makes fewer assumptions.; 5.2 Sim-to-Real Policy Training; Co-training with sim and real data further improves performance.；Evaluation=https://arxiv.org/html/2606.28276v1 — §SimFoundry: Modular and Automated Scene Generation for Policy Learning and Evaluation; 5 Experiments; 5.1 Real-to-Sim Policy Evaluation。评测合同逐字段冻结，未公开项才写 Not Disclosed。

**Trade-off、failure、fallback、coexistence 与 evolution。** exact-v1 的结论只覆盖《SimFoundry: Modular and Automated Scene Generation for Policy Learning and Evaluation》在 SimFoundry: Modular and Automated Scene Generation for Policy Learning and Evaluation; 5 Experiments; 5.1 Real-to-Sim Policy Evaluation 声明的实验；它没有证明跨 model family、hardware/runtime、数据分布或未测 failure mode 的普遍成立。 Reconstruction quality 与 simulator ranking 不证明 contact dynamics 或 safety；rank mismatch 或未知 embodiment 会阻断物理 promotion，并保留 real-data/controller gate。 Counterevidence/limitation=https://arxiv.org/html/2606.28276v1 — §6 Limitations; 7 Conclusion; Appendix C Limitations。

<!-- claim:SF-2026-ARXIV-2606-28276:start -->
Claim boundary：仅 arXiv:2606.28276v1 与 official exact-v1 HTML；不使用 later version，不把 benchmark outcome 外推为生产 SLO。
<!-- claim:SF-2026-ARXIV-2606-28276:end -->
<!-- review:SF-2026-ARXIV-2606-28276:end -->

<!-- review:SF-2026-ARXIV-2606-28277:start -->
### 2606.28277 — Towards Automating Scientific Review with Google's Paper Assistant Tool

**问题、约束与旧路径。** Artificial intelligence is driving a revolution in scientific discovery, accelerating everything from hypothesis generation to mathematical theorem proving. However, this rapid acceleration is creating a systemic challenge: traditional human peer review cannot scale to match the influx of AI-assisted science. 旧路径在论文新增条件之外仍然合理。

**机制、state/data/control owner。** 把 agentic scientific review 的 verification depth 与 human decision authority 分层，并给出部署证据。 由 PLATFORM-EVALUATION-SYSTEM 持有 oracle、metric、slice 与结论发布；相邻节点只消费版本化 handoff。

**Evaluation：证明与未证明。** Pilot deployments of PAT as a pre-submission tool for authors at two major Computer Science conferences -- STOC and ICML -- demonstrate its ability to identify critical errors and suggest substantive improvements to research papers. Method=https://arxiv.org/html/2606.28277v1 — §Design Considerations.；Evaluation=https://arxiv.org/html/2606.28277v1 — §2.1. Case Study: Verification of Retracted Papers in the SPOT Benchmark; 3. PAT Experimental Programs at STOC and ICML; 3.1. Quantitative Author Feedback for PAT Experimental Programs。评测合同逐字段冻结，未公开项才写 Not Disclosed。

**Trade-off、failure、fallback、coexistence 与 evolution。** By catching errors early, PAT eases the cognitive burden placed on referees, while preserving their control over the outcomes of the review process. 现有 owner 已覆盖同一长期原则，因此只作为受限反例或实例留在 Daily，不复制 Books 分支。 Counterevidence/limitation=https://arxiv.org/html/2606.28277v1 — §5. Conclusion and Future Outlook。

<!-- claim:SF-2026-ARXIV-2606-28277:start -->
Claim boundary：仅 arXiv:2606.28277v1 与 official exact-v1 HTML；不使用 later version，不把 benchmark outcome 外推为生产 SLO。
<!-- claim:SF-2026-ARXIV-2606-28277:end -->
<!-- review:SF-2026-ARXIV-2606-28277:end -->

<!-- review:SF-2026-ARXIV-2606-28279:start -->
### 2606.28279 — Agentic Hardware Design as Repository-Level Code Evolution

**问题、约束与旧路径。** We present HORIZON, a self-evolving agent framework that treats hardware design as repository-level code evolution. A Markdown harness is compiled into a project pack containing domain knowledge, an executable evaluator, an acceptance predicate, and a git/runtime policy; a hands-free agent loop then evolves an isolated git worktree, using repository operations for state management, tracing, and replay. 旧路径在论文新增条件之外仍然合理。

**机制、state/data/control owner。** 用 compiled project pack、acceptance predicate、isolated worktree 与 trace/replay 管理 repository-scale hardware agent。 由 AGENT-WORKFLOW 持有 artifact state、verifier/interlock 与 fallback；相邻节点只消费版本化 handoff。

**Evaluation：证明与未证明。** We evaluate our approach on ChipBench, RTLLM, Verilog-Eval, and nine CVDP categories, achieving 100\% benchmark completion across all suites with a fully hands-free agentic loop. Method=https://arxiv.org/html/2606.28279v1 — §Agentic Hardware Design as Repository-Level Code Evolution; Benchmarks for RTL design and verification.; 3 The HORIZON Framework；Evaluation=https://arxiv.org/html/2606.28279v1 — §Benchmarks for RTL design and verification.; 4 Experiments; Setup and protocol.。评测合同逐字段冻结，未公开项才写 Not Disclosed。

**Trade-off、failure、fallback、coexistence 与 evolution。** However, we do not claim that agentic AI for hardware design is solved: these benchmarks are controlled proxies for a much broader engineering problem in chip design. 现有 owner 已覆盖同一长期原则，因此只作为受限反例或实例留在 Daily，不复制 Books 分支。 Counterevidence/limitation=https://arxiv.org/html/2606.28279v1 — §4.3 Detailed discussion on test-generation tasks; 5 Discussion and Limitations; 6 Conclusion。

<!-- claim:SF-2026-ARXIV-2606-28279:start -->
Claim boundary：仅 arXiv:2606.28279v1 与 official exact-v1 HTML；不使用 later version，不把 benchmark outcome 外推为生产 SLO。
<!-- claim:SF-2026-ARXIV-2606-28279:end -->
<!-- review:SF-2026-ARXIV-2606-28279:end -->

<!-- review:SF-2026-ARXIV-2606-28322:start -->
### 2606.28322 — PerceptionRubrics: Calibrating Multimodal Evaluation to Human Perception

**问题、约束与旧路径。** We introduce PerceptionRubrics, a rubric-based evaluation framework that addresses the gap between saturated benchmark scores and real-world brittleness. Shifting evaluation from holistic semantic matching to rigorous atomic auditing, PerceptionRubrics pairs 1,038 information-dense images with over 10,000 instance-specific rubrics. 旧路径在论文新增条件之外仍然合理。

**机制、state/data/control owner。** 以 Must-Right/Easy-Wrong atomic rubrics 与 gated penalty 替代会掩盖必需事实失败的平均分。 由 PLATFORM-EVALUATION-SYSTEM 持有 oracle、metric、slice 与结论发布；相邻节点只消费版本化 handoff。

**Evaluation：证明与未证明。** Extensive evaluation yields critical insights: (1) The Reliability Gap: models often verify fragmented elements correctly yet fail strict conjunctive constraints, exposing brittleness in dense domains; (2) Open-Closed Stratification: contrary to reasoning trends, we reveal a persistent 8% perception deficit between open-source and proprietary frontiers; and (3) Human-Aligned Rigor: our gated metrics substantially out-align conventional benchmarks, validating that strict perceptual fidelity is the prerequisite for reliable generation. Method=https://arxiv.org/html/2606.28322v1 — §3.1 Design Criteria；Evaluation=https://arxiv.org/html/2606.28322v1 — §PerceptionRubrics: Calibrating Multimodal Evaluation to Human Perception; Visual Perception Benchmarks in MLLMs.; Evaluation of Image Captioning.。评测合同逐字段冻结，未公开项才写 Not Disclosed。

**Trade-off、failure、fallback、coexistence 与 evolution。** exact-v1 的结论只覆盖《PerceptionRubrics: Calibrating Multimodal Evaluation to Human Perception》在 PerceptionRubrics: Calibrating Multimodal Evaluation to Human Perception; Visual Perception Benchmarks in MLLMs.; Evaluation of Image Captioning. 声明的实验；它没有证明跨 model family、hardware/runtime、数据分布或未测 failure mode 的普遍成立。 现有 owner 已覆盖同一长期原则，因此只作为受限反例或实例留在 Daily，不复制 Books 分支。 Counterevidence/limitation=https://arxiv.org/html/2606.28322v1 — §6 Conclusion。

<!-- claim:SF-2026-ARXIV-2606-28322:start -->
Claim boundary：仅 arXiv:2606.28322v1 与 official exact-v1 HTML；不使用 later version，不把 benchmark outcome 外推为生产 SLO。
<!-- claim:SF-2026-ARXIV-2606-28322:end -->
<!-- review:SF-2026-ARXIV-2606-28322:end -->

<!-- review:SF-2026-ARXIV-2606-28430:start -->
### 2606.28430 — Building to the Test: Coding Agents Deliver What You Check, Not What You Requested

**问题、约束与旧路径。** Benchmarks are widely used to evaluate task completion by Large Language Models (LLMs), but this approach has accumulated construction-validity problems, and a passing score may not show whether the requested task was delivered. We study both problems. 旧路径在论文新增条件之外仍然合理。

**机制、state/data/control owner。** 用 no-op ablation 揭示 coding agent 可通过 oracle 却未交付可复用 artifact 的 construction-validity failure。 由 PLATFORM-EVALUATION-SYSTEM 持有 oracle、metric、slice 与结论发布；相邻节点只消费版本化 handoff。

**Evaluation：证明与未证明。** Benchmarks are widely used to evaluate task completion by Large Language Models (LLMs), but this approach has accumulated construction-validity problems, and a passing score may not show whether the requested task was delivered. Method=https://arxiv.org/html/2606.28430v1 — §3 Library audit methodology; An honest oracle is enough; the exposed signal is not the per-subsystem driver.; c9 removes c3’s guards by design, and remains honest.；Evaluation=https://arxiv.org/html/2606.28430v1 — §2 Setup; Unit of analysis: the production agent.; Code-generation benchmarks.。评测合同逐字段冻结，未公开项才写 Not Disclosed。

**Trade-off、failure、fallback、coexistence 与 evolution。** The agent does not, on its own, validate what it ships as a user would. 现有 owner 已覆盖同一长期原则，因此只作为受限反例或实例留在 Daily，不复制 Books 分支。 Counterevidence/limitation=https://arxiv.org/html/2606.28430v1 — §6 Threats to validity; 8 Discussion; 9 Conclusion。

<!-- claim:SF-2026-ARXIV-2606-28430:start -->
Claim boundary：仅 arXiv:2606.28430v1 与 official exact-v1 HTML；不使用 later version，不把 benchmark outcome 外推为生产 SLO。
<!-- claim:SF-2026-ARXIV-2606-28430:end -->
<!-- review:SF-2026-ARXIV-2606-28430:end -->

<!-- review:SF-2026-ARXIV-2606-28433:start -->
### 2606.28433 — Position: RL Researchers Need to Distinguish Between Solving Simulators and Using Simulators as a Proxy

**问题、约束与旧路径。** One goal in reinforcement learning (RL) research is to understand general-purpose sequential decision-making, using benchmark simulators as a proxy for learning in deployment settings. When running experiments, however, the goal of achieving high performance in the simulator can mutate into focusing exclusively on solving the simulator. 旧路径在论文新增条件之外仍然合理。

**机制、state/data/control owner。** 要求 RL evaluation 区分把 simulator 当目标与把 simulator 当 deployment proxy 的两套约束。 由 PLATFORM-EVALUATION-SYSTEM 持有 oracle、metric、slice 与结论发布；相邻节点只消费版本化 handoff。

**Evaluation：证明与未证明。** We then highlight several issues and misleading conclusions that can occur by not making the distinction between these two settings clear, supported with examples and simple experiments. Method=https://arxiv.org/html/2606.28433v1 — §Position: RL Researchers Need to Distinguish Between Solving Simulators and Using Simulators as a Proxy; Keywords:；Evaluation=https://arxiv.org/html/2606.28433v1 — §3.4 Issue: Evaluation Rollouts; Appendix A Experiment Details; A.1 Collapsing Learning Curve Experiment。评测合同逐字段冻结，未公开项才写 Not Disclosed。

**Trade-off、failure、fallback、coexistence 与 evolution。** To achieve high scores, researchers may adopt solutions exclusively meant for solving simulators, rather than learning while the agent is deployed outside a simulator. 现有 owner 已覆盖同一长期原则，因此只作为受限反例或实例留在 Daily，不复制 Books 分支。 Counterevidence/limitation=https://arxiv.org/html/2606.28433v1 — §3 Misleading Conclusions from Not Distinguishing Between Simulator Usages; 6 Conclusion。

<!-- claim:SF-2026-ARXIV-2606-28433:start -->
Claim boundary：仅 arXiv:2606.28433v1 与 official exact-v1 HTML；不使用 later version，不把 benchmark outcome 外推为生产 SLO。
<!-- claim:SF-2026-ARXIV-2606-28433:end -->
<!-- review:SF-2026-ARXIV-2606-28433:end -->

<!-- review:SF-2026-ARXIV-2606-28434:start -->
### 2606.28434 — SWE-MeM: Learning Adaptive Memory Management for Long-Horizon Coding Agents

**问题、约束与旧路径。** Long-horizon software engineering agents often need to manage lengthy and noisy interaction histories under limited context budgets. Existing memory management methods typically rely on static compression workflows or impose rigid constraints on compression timing and granularity. 旧路径在论文新增条件之外仍然合理。

**机制、state/data/control owner。** 把 coding-agent compression timing、granularity 与剩余 context budget 变成 agent-controlled memory action。 由 AGENT-MEMORY 持有 memory action、compression 与 remaining-context state；相邻节点只消费版本化 handoff。

**Evaluation：证明与未证明。** On SWE-Bench Verified, SWE-MeM achieves 43.4% and 60.2% resolve rate with 4B and 30B models, respectively, outperforming existing memory management baselines in both performance and efficiency. Method=https://arxiv.org/html/2606.28434v1 — §2 Proposed Approach; 2.1 Memory Management Tool Design; Appendix A Method Details；Evaluation=https://arxiv.org/html/2606.28434v1 — §3 Experiment; 3.3 Experiment Details; 3.4 Main Results。评测合同逐字段冻结，未公开项才写 Not Disclosed。

**Trade-off、failure、fallback、coexistence 与 evolution。** Moreover, these approaches fail to jointly optimize memory management and issue resolution capabilities to improve performance while reducing token usage. 现有 owner 已覆盖同一长期原则，因此只作为受限反例或实例留在 Daily，不复制 Books 分支。 Counterevidence/limitation=https://arxiv.org/html/2606.28434v1 — §6 Conclusion。

<!-- claim:SF-2026-ARXIV-2606-28434:start -->
Claim boundary：仅 arXiv:2606.28434v1 与 official exact-v1 HTML；不使用 later version，不把 benchmark outcome 外推为生产 SLO。
<!-- claim:SF-2026-ARXIV-2606-28434:end -->
<!-- review:SF-2026-ARXIV-2606-28434:end -->

<!-- review:SF-2026-ARXIV-2606-28436:start -->
### 2606.28436 — Dockerless: Environment-Free Program Verifier for Coding Agents

**问题、约束与旧路径。** Program verifiers play a central role in training coding agents, including selecting trajectories for supervised fine-tuning (SFT) and providing rewards for reinforcement learning (RL). Standard execution-based verification requires running unit tests inside per-repository environments such as Docker images, incurring substantial environment setup costs. 旧路径在论文新增条件之外仍然合理。

**机制、state/data/control owner。** 把 coding post-training verifier 从 executable environment 改成 repository-evidence judge，改变 reward authority 与 non-proof 边界。 由 TRAIN-GRPO 持有 trajectory、credit、teacher signal 与 update gate；相邻节点只消费版本化 handoff。

**Evaluation：证明与未证明。** The resulting model reaches 62.0%, 50.0%, and 35.2% resolve rate on SWE-bench Verified, Multilingual, and Pro, respectively. Method=https://arxiv.org/html/2606.28436v1 — §2 Methodology; 2.2 Architecture of Dockerless; 2.3 Dockerless Training；Evaluation=https://arxiv.org/html/2606.28436v1 — §3 Experimental Settings; Benchmarks.; Evaluation protocol.。评测合同逐字段冻结，未公开项才写 Not Disclosed。

**Trade-off、failure、fallback、coexistence 与 evolution。** We propose Dockerless, an environment-free agentic patch verifier that evaluates generated code patches without executing them. 现有 owner 已覆盖同一长期原则，因此只作为受限反例或实例留在 Daily，不复制 Books 分支。 Counterevidence/limitation=https://arxiv.org/html/2606.28436v1 — §6 Conclusion。

<!-- claim:SF-2026-ARXIV-2606-28436:start -->
Claim boundary：仅 arXiv:2606.28436v1 与 official exact-v1 HTML；不使用 later version，不把 benchmark outcome 外推为生产 SLO。
<!-- claim:SF-2026-ARXIV-2606-28436:end -->
<!-- review:SF-2026-ARXIV-2606-28436:end -->

<!-- review:SF-2026-ARXIV-2606-28438:start -->
### 2606.28438 — When AI Reviews Its Own Code: Recursive Self-Training Collapse in Code LLMs

**问题、约束与旧路径。** Recursive self-training can degrade neural generative models when generated data is reused without fresh human data or external quality control. We study this risk in code LLMs, where AI-generated code can enter real repositories, later become training data, and create a repository-scale self-training loop. 旧路径在论文新增条件之外仍然合理。

**机制、state/data/control owner。** 证明 recursive code self-training 的 model-coupled gate 会 rubber-stamp collapse，要求 exogenous verification。 由 TRAIN-DATA 持有 sample provenance、mixture 与 admission state；相邻节点只消费版本化 handoff。

**Evaluation：证明与未证明。** These results suggest that stable recursive code LLM training requires exogenous verification rather than model-coupled self-review. Method=https://arxiv.org/html/2606.28438v1 — §When AI Reviews Its Own Code: Recursive Self-Training Collapse in Code LLMs; 2.1 Iterative Self-Training Without vs. With Gating; 2.2 Representation-Subspace Drift Under Recursive Self-Training；Evaluation=https://arxiv.org/html/2606.28438v1 — §2 Problem Formulation and Theoretical Analysis; 3 Experiments; 3.1 Evaluation Setup。评测合同逐字段冻结，未公开项才写 Not Disclosed。

**Trade-off、failure、fallback、coexistence 与 evolution。** In the clearest case, the binary self-gate enters a rubber-stamp regime where acceptance scores rise while benchmark correctness falls. 现有 owner 已覆盖同一长期原则，因此只作为受限反例或实例留在 Daily，不复制 Books 分支。 Counterevidence/limitation=https://arxiv.org/html/2606.28438v1 — §4 Conclusion; 5 Limitations。

<!-- claim:SF-2026-ARXIV-2606-28438:start -->
Claim boundary：仅 arXiv:2606.28438v1 与 official exact-v1 HTML；不使用 later version，不把 benchmark outcome 外推为生产 SLO。
<!-- claim:SF-2026-ARXIV-2606-28438:end -->
<!-- review:SF-2026-ARXIV-2606-28438:end -->

<!-- review:SF-2026-ARXIV-2606-28455:start -->
### 2606.28455 — Event-Conditioned Diagnostics of Kinematic, Contact, and Object-Permanence Structure in Passive Object-State World Models

**问题、约束与旧路径。** World models can predict future physical states, but prediction accuracy alone does not explain how physical information is organized and used inside their latent dynamics. We introduce a controlled diagnostic protocol for studying event-conditioned latent physical structure in passive object-state world models. 旧路径在论文新增条件之外仍然合理。

**机制、state/data/control owner。** 把 event readout、context-relative emphasis 与 causal sensitivity 分开评估 latent physical structure。 由 MULTIMODAL-WORLD-MODELS 持有 belief/latent state、transition 与 physical boundary；相邻节点只消费版本化 handoff。

**Evaluation：证明与未证明。** These results support event-conditioned latent structure and functional sensitivity without implying explicit physical modules or isolated causal circuits. Method=https://arxiv.org/pdf/2606.28455v1 — §3 Problem formulation; 4 Diagnostic Protocol; 5 Dataset and Models；Evaluation=https://arxiv.org/pdf/2606.28455v1 — §6 Main results; Appendix A. Experimental and Diagnostic Details。评测合同逐字段冻结，未公开项才写 Not Disclosed。

**Trade-off、failure、fallback、coexistence 与 evolution。** These results support event-conditioned latent structure and functional sensitivity without implying explicit physical modules or isolated causal circuits. 现有 owner 已覆盖同一长期原则，因此只作为受限反例或实例留在 Daily，不复制 Books 分支。 Counterevidence/limitation=https://arxiv.org/pdf/2606.28455v1 — §7 Discussion and Limitations; 7.2 Scope and limitations; C.9 Interpretation boundary。

<!-- claim:SF-2026-ARXIV-2606-28455:start -->
Claim boundary：仅 arXiv:2606.28455v1 与 official exact-v1 HTML；不使用 later version，不把 benchmark outcome 外推为生产 SLO。
<!-- claim:SF-2026-ARXIV-2606-28455:end -->
<!-- review:SF-2026-ARXIV-2606-28455:end -->

<!-- review:SF-2026-ARXIV-2606-28471:start -->
### 2606.28471 — Data and Evaluation Closed-Loop for Model Capability Enhancement

**问题、约束与旧路径。** Model capability is the central variable in LLM pre-training, yet is never observed directly: data shapes it prospectively, while evaluation reveals it only retrospectively, compressing samples, prompts, decoding, and scoring rules into one noisy score. Practical optimization runs this backward: a failure is observed first, and the engineer must infer the corpus fix. 旧路径在论文新增条件之外仍然合理。

**机制、state/data/control owner。** 以 capability slice 将 evaluation failure 反向映射为可检验 data intervention，并允许判定 data 非根因。 由 TRAIN-DATA 持有 sample provenance、mixture 与 admission state；相邻节点只消费版本化 handoff。

**Evaluation：证明与未证明。** The same unmodified loop reaches opposite, correct verdicts in both cases, showing the evaluation-to-data inference can be routine, auditable, and experimentally validated rather than intuitive. Method=https://arxiv.org/html/2606.28471v1 — §2 Conceptual Framework; 2.3 Understanding Training Data; Assessment of the targeted-sampling method and the data–evaluation loop.；Evaluation=https://arxiv.org/html/2606.28471v1 — §Data and Evaluation Closed-Loop for Model Capability Enhancement; 2.1 Understanding Evaluation; 3 Analysis Toolkit。评测合同逐字段冻结，未公开项才写 Not Disclosed。

**Trade-off、failure、fallback、coexistence 与 evolution。** First, the loop rules the data out: continued pre-training drives BBH down by $-46.82\%$, but diagnosis traces this to a single masked \texttt{\textless EOS\textgreater} loss rather than weakened reasoning; restoring it recovers BBH to $66.44$, above the original checkpoint, without changing the data. 现有 owner 已覆盖同一长期原则，因此只作为受限反例或实例留在 Daily，不复制 Books 分支。 Counterevidence/limitation=https://arxiv.org/html/2606.28471v1 — §4.1.3 Prediction-Level Audit of Parser-Sensitive Failures; 4.1.5 Restoring EOS Supervision and Validating Failure-Mode Reduction; 5 Conclusion。

<!-- claim:SF-2026-ARXIV-2606-28471:start -->
Claim boundary：仅 arXiv:2606.28471v1 与 official exact-v1 HTML；不使用 later version，不把 benchmark outcome 外推为生产 SLO。
<!-- claim:SF-2026-ARXIV-2606-28471:end -->
<!-- review:SF-2026-ARXIV-2606-28471:end -->

<!-- review:SF-2026-ARXIV-2606-28479:start -->
### 2606.28479 — Decomposing Memorization Reduction in Privacy-Preserving Fine-Tuning of SLMs for CSIRTs

**问题、约束与旧路径。** CSIRTs increasingly fine tune language models on vulnerability scan records, but these records expose internal network topology and create privacy risks under regulations such as GDPR and LGPD. We present the first empirical study of how DP SGD and HMAC pseudonymization interact when fine tuning small language models with 1B to 3B parameters on structured CSIRT data. 旧路径在论文新增条件之外仍然合理。

**机制、state/data/control owner。** 用 matched-update controls 分离 DP guarantee、pseudonymization 与 optimizer-step memorization effect。 由 TRAIN-LORA 持有 adapter/update identity 与 rollback；相邻节点只消费版本化 handoff。

**Evaluation：证明与未证明。** Third, F1 scores remain between 0.19 and 0.28 across all 96 adapters using four shot prompting, indicating that, under the evaluated training budget, 1B to 3B SLMs do not achieve operationally useful performance. Method=https://arxiv.org/html/2606.28479v1 — §III Threat Model and Methodology；Evaluation=https://arxiv.org/html/2606.28479v1 — §VI Utility Evaluation。评测合同逐字段冻结，未公开项才写 Not Disclosed。

**Trade-off、failure、fallback、coexistence 与 evolution。** Third, F1 scores remain between 0.19 and 0.28 across all 96 adapters using four shot prompting, indicating that, under the evaluated training budget, 1B to 3B SLMs do not achieve operationally useful performance. Matched control 增加实验成本，empirical attack 的 recall 也有边界；未测到 leakage 不是 privacy guarantee，不确定时保留更严格 data/DP path。 Counterevidence/limitation=https://arxiv.org/html/2606.28479v1 — §III Threat Model and Methodology; III-A Threat Model; VII Discussion。

<!-- claim:SF-2026-ARXIV-2606-28479:start -->
Claim boundary：仅 arXiv:2606.28479v1 与 official exact-v1 HTML；不使用 later version，不把 benchmark outcome 外推为生产 SLO。
<!-- claim:SF-2026-ARXIV-2606-28479:end -->
<!-- review:SF-2026-ARXIV-2606-28479:end -->

<!-- review:SF-2026-ARXIV-2606-28480:start -->
### 2606.28480 — TUA-Bench: A Benchmark for General-Purpose Terminal-Use Agents

**问题、约束与旧路径。** As large language models and harness frameworks continue to advance, agents operating in terminals are increasingly capable of performing a broader range of general computer-use tasks beyond coding. However, existing benchmarks do not adequately evaluate general-purpose terminal computer-use agents (TUAs): general computer-use benchmarks primarily target graphical user interfaces (GUIs), whereas terminal-based benchmarks largely emphasize technical and programming-centric workflows historically native to the shell. 旧路径在论文新增条件之外仍然合理。

**机制、state/data/control owner。** 把 terminal-use agent 扩展到非 coding workflow，并用 deterministic setup/execution scoring 约束 release claim。 由 PLATFORM-EVALUATION-SYSTEM 持有 oracle、metric、slice 与结论发布；相邻节点只消费版本化 handoff。

**Evaluation：证明与未证明。** We find that the strongest frontier agent, Claude Code with Claude Opus 4.8 max reasoning effort, achieves 65.8% overall performance, with substantial gaps across both tracks. Method=https://arxiv.org/html/2606.28480v1 — §TUA-Bench: A Benchmark for General-Purpose Terminal-Use Agents; 1 Introduction；Evaluation=https://arxiv.org/html/2606.28480v1 — §TUA-Bench: A Benchmark for General-Purpose Terminal-Use Agents; 4 Benchmark Experiments; 4.1 Experimental Settings。评测合同逐字段冻结，未公开项才写 Not Disclosed。

**Trade-off、failure、fallback、coexistence 与 evolution。** However, existing benchmarks do not adequately evaluate general-purpose terminal computer-use agents (TUAs): general computer-use benchmarks primarily target graphical user interfaces (GUIs), whereas terminal-based benchmarks largely emphasize technical and programming-centric workflows historically native to the shell. 现有 owner 已覆盖同一长期原则，因此只作为受限反例或实例留在 Daily，不复制 Books 分支。 Counterevidence/limitation=https://arxiv.org/html/2606.28480v1 — §5 Limitations; 6 Conclusion。

<!-- claim:SF-2026-ARXIV-2606-28480:start -->
Claim boundary：仅 arXiv:2606.28480v1 与 official exact-v1 HTML；不使用 later version，不把 benchmark outcome 外推为生产 SLO。
<!-- claim:SF-2026-ARXIV-2606-28480:end -->
<!-- review:SF-2026-ARXIV-2606-28480:end -->

<!-- review:SF-2026-ARXIV-2606-28514:start -->
### 2606.28514 — GPTNT: Benchmarking Real-Time Collaboration Between Multimodal Agents on Keep Talking And Nobody Explodes

**问题、约束与旧路径。** Multimodal models are increasingly deployed to solve tasks collaboratively with humans or other artificial agents. Existing benchmarks show that these models possess many of the required component capabilities, but the conditions that coincide in collaboration, including time pressure, information asymmetry, and imperfect communication, are usually studied in isolation. 旧路径在论文新增条件之外仍然合理。

**机制、state/data/control owner。** 以真实异步倒计时、信息不对称与不可单独完成任务测量实时 collaboration。 由 AGENT-MULTI-AGENT 持有 interaction graph、attribution 与 commit coordination；相邻节点只消费版本化 handoff。

**Evaluation：证明与未证明。** Because it runs on the real game, GPTNT benefits from procedural generation and inherits a living modding community, allowing the benchmark to evolve as models improve rather than being solved once and retired. Method=https://arxiv.org/html/2606.28514v1 — §System prompt.; ReAct-style framework.; Appendix C The GPTNT Framework；Evaluation=https://arxiv.org/html/2606.28514v1 — §GPTNT: Benchmarking Real-Time Collaboration Between Multimodal Agents on Keep Talking And Nobody Explodes; 4 The Benchmark: What is GPTNT?; 4.3 Evaluation Protocol。评测合同逐字段冻结，未公开项才写 Not Disclosed。

**Trade-off、failure、fallback、coexistence 与 evolution。** One agent can see and manipulate the bomb but does not have the defusal instructions; the other has the instructions but cannot see or manipulate the bomb. 现有 owner 已覆盖同一长期原则，因此只作为受限反例或实例留在 Daily，不复制 Books 分支。 Counterevidence/limitation=https://arxiv.org/html/2606.28514v1 — §Synchronous play shifts failures toward striking out.; Localisation failure acts as a hard ceiling on downstream success.; 11 Conclusion。

<!-- claim:SF-2026-ARXIV-2606-28514:start -->
Claim boundary：仅 arXiv:2606.28514v1 与 official exact-v1 HTML；不使用 later version，不把 benchmark outcome 外推为生产 SLO。
<!-- claim:SF-2026-ARXIV-2606-28514:end -->
<!-- review:SF-2026-ARXIV-2606-28514:end -->

<!-- review:SF-2026-ARXIV-2606-28529:start -->
### 2606.28529 — The Speedup Paradox: Rethinking Inference Speed-Quality Trade-off in Embodied Tasks

**问题、约束与旧路径。** Embodied foundation models have recently been widely used to improve robot generalization and task success rates. Previous works apply lossy efficient-inference techniques such as quantization, pruning, and asynchronous inference, accepting small action quality degradation in exchange for lower per-step computation cost and inter-action latency. 旧路径在论文新增条件之外仍然合理。

**机制、state/data/control owner。** 把 embodied inference optimization 从 per-step latency 扩展到 closed-loop task time、success 与 hardware-dependent sweet spot。 由 INFER-REQUEST-LIFECYCLE 持有 request phase、runtime placement、queue 与 latency state；相邻节点只消费版本化 handoff。

**Evaluation：证明与未证明。** Embodied foundation models have recently been widely used to improve robot generalization and task success rates. Method=https://arxiv.org/html/2606.28529v1 — §Optimization Methods.; B.1 Optimization Method Settings；Evaluation=https://arxiv.org/html/2606.28529v1 — §4 Experiments; 4.1 Setup; Simulation Task Setup.。评测合同逐字段冻结，未公开项才写 Not Disclosed。

**Trade-off、failure、fallback、coexistence 与 evolution。** However, unlike traditional static ML tasks, embodied tasks involve repeated interaction with the environment, and task-level performance is determined not only by per-step cost, but also by closed-loop effects unique to embodied execution, which remain insufficiently characterized in current efficient-inference studies. Simulation 与 component latency 不证明生产 SLO 或 embodied success；mismatch、thermal drift 或 deadline miss 时回退已实测的保守 placement/control。 Counterevidence/limitation=https://arxiv.org/html/2606.28529v1 — §5 Conclusion; 6 Limitations; A.3 Assumptions and Limitations。

<!-- claim:SF-2026-ARXIV-2606-28529:start -->
Claim boundary：仅 arXiv:2606.28529v1 与 official exact-v1 HTML；不使用 later version，不把 benchmark outcome 外推为生产 SLO。
<!-- claim:SF-2026-ARXIV-2606-28529:end -->
<!-- review:SF-2026-ARXIV-2606-28529:end -->

<!-- review:SF-2026-ARXIV-2606-28551:start -->
### 2606.28551 — DataComp-VLM: Improved Open Datasets for Vision-Language Models

**问题、约束与旧路径。** Building performant Vision-Language Models (VLMs) requires carefully curating large-scale training datasets, yet the community lacks systematic benchmarks for evaluating such curation strategies. We introduce DataComp for VLMs (DCVLM), a benchmark for controlled data-centric experiments to improve VLM training. 旧路径在论文新增条件之外仍然合理。

**机制、state/data/control owner。** 用固定 model/token budget 与多数据类型 corpus 建立 VLM data curation、mixing 与 release artifact 的可复算合同。 由 TRAIN-DATA 持有 sample provenance、mixture 与 admission state；相邻节点只消费版本化 handoff。

**Evaluation：证明与未证明。** Compared to FineVision, the state-of-the-art open VLM training dataset, this represents an improvement of +5.4pp. Method=https://arxiv.org/html/2606.28551v1 — §3.2 Model Architecture and Training Recipe; 3.3 Competition Scales and Design Principles; Appendix C Model Architecture Details；Evaluation=https://arxiv.org/html/2606.28551v1 — §3 The DCVLM Benchmark; 3.4 Evaluation Protocol; 4.3 Control Experiments。评测合同逐字段冻结，未公开项才写 Not Disclosed。

**Trade-off、failure、fallback、coexistence 与 evolution。** As part of DCVLM, we collect 160 datasets spanning four data types -- image-caption pairs, multimodal interleaved documents, text-only, and instruction-tuning data -- into a corpus of 6T multimodal tokens. 现有 owner 已覆盖同一长期原则，因此只作为受限反例或实例留在 Daily，不复制 Books 分支。 Counterevidence/limitation=https://arxiv.org/html/2606.28551v1 — §6 Conclusion; Appendix P Limitations and Future Directions; P.1 Limitations。

<!-- claim:SF-2026-ARXIV-2606-28551:start -->
Claim boundary：仅 arXiv:2606.28551v1 与 official exact-v1 HTML；不使用 later version，不把 benchmark outcome 外推为生产 SLO。
<!-- claim:SF-2026-ARXIV-2606-28551:end -->
<!-- review:SF-2026-ARXIV-2606-28551:end -->

<!-- review:SF-2026-ARXIV-2606-28560:start -->
### 2606.28560 — Depth-Staggered Fibonacci Spacing for Sparse Attention: Static Schedules Beat Learned Dilation and Extrapolate Where Dense Attention Fails

**问题、约束与旧路径。** We study sparse self-attention in which each query attends to a dense local window plus a set of Fibonacci-spaced offsets, with a per-layer scalar alpha that compresses or expands the spacing. Across 21 language models trained under one matched recipe (60M parameters, 512 hidden, 16 layers, 426M tokens), we compare four ways of setting alpha across depth: fixed, per-layer learned, a static linear stagger, and a coprime (anti-gridding) reassignment of that stagger, together with a reach-matched power-of-2 control. 旧路径在论文新增条件之外仍然合理。

**机制、state/data/control owner。** 以 matched small-model study 反证 learned sparse spacing 必然优于 static schedule，并暴露 train-length 与 extrapolation 的反向取舍。 由 MODEL-LONG-CONTEXT 持有 attention reach、layer policy 与 context budget；相邻节点只消费版本化 handoff。

**Evaluation：证明与未证明。** First, a static per-layer stagger improves perplexity over both fixed and learned alpha, and the gain is base-agnostic: applying the same stagger to a power-of-2 base lifts it above fixed Fibonacci and to parity with learned Fibonacci attention. Method=https://arxiv.org/html/2606.28560v1 — §2 Method; Model and training.; Training-length gap to dense.；Evaluation=https://arxiv.org/html/2606.28560v1 — §Depth-Staggered Fibonacci Spacing for Sparse Attention: Static Schedules Beat Learned Dilation and Extrapolate Where Dense Attention Fails Thanks: Code, the paper source, and the experiment database are available at https://github.com/ccapps42/scaled-fibonacci-attention .; 3 Experimental Setup; Data and evaluation.。评测合同逐字段冻结，未公开项才写 Not Disclosed。

**Trade-off、failure、fallback、coexistence 与 evolution。** Third, and most consequential, all sparse variants extrapolate to four times their training length with little or no degradation, whereas a recipe-matched dense baseline collapses (perplexity rises by 201% at 4x length); we attribute this to fixed-offset attention only ever querying relative positions seen during training. 该结果只保留为局部方法/实验语境；它不新增长期 owner、authority、coexistence 或 fallback 命题。 Counterevidence/limitation=https://arxiv.org/html/2606.28560v1 — §6 Discussion and Limitations; 7 Conclusion。

<!-- claim:SF-2026-ARXIV-2606-28560:start -->
Claim boundary：仅 arXiv:2606.28560v1 与 official exact-v1 HTML；不使用 later version，不把 benchmark outcome 外推为生产 SLO。
<!-- claim:SF-2026-ARXIV-2606-28560:end -->
<!-- review:SF-2026-ARXIV-2606-28560:end -->

<!-- review:SF-2026-ARXIV-2606-28562:start -->
### 2606.28562 — SEAD: Competence-Aware On-Policy Distillation via Entropy-Guided Supervision

**问题、约束与旧路径。** On-policy distillation (OPD) has a property absent in offline distillation and RL: teacher supervision quality depends on student competence. Incoherent rollouts yield noisy gradients; already-mastered tokens yield redundant ones. 旧路径在论文新增条件之外仍然合理。

**机制、state/data/control owner。** 按 student competence 在 token、phase、prompt 三个尺度控制 on-policy distillation supervision。 由 TRAIN-GRPO 持有 trajectory、credit、teacher signal 与 update gate；相邻节点只消费版本化 handoff。

**Evaluation：证明与未证明。** On OLMo-3 (7B to 32B), SEAD achieves +4.8 avg accuracy over vanilla OPD across six math benchmarks, with ablations confirming super-additive interactions. Method=https://arxiv.org/html/2606.28562v1 — §2 Method; Training.; Combined Method Performance.；Evaluation=https://arxiv.org/html/2606.28562v1 — §3 Evaluation; 3.1 Experimental Setup; Evaluation.。评测合同逐字段冻结，未公开项才写 Not Disclosed。

**Trade-off、failure、fallback、coexistence 与 evolution。** exact-v1 的结论只覆盖《SEAD: Competence-Aware On-Policy Distillation via Entropy-Guided Supervision》在 3 Evaluation; 3.1 Experimental Setup; Evaluation. 声明的实验；它没有证明跨 model family、hardware/runtime、数据分布或未测 failure mode 的普遍成立。 现有 owner 已覆盖同一长期原则，因此只作为受限反例或实例留在 Daily，不复制 Books 分支。 Counterevidence/limitation=https://arxiv.org/html/2606.28562v1 — §6 Conclusion and Limitations。

<!-- claim:SF-2026-ARXIV-2606-28562:start -->
Claim boundary：仅 arXiv:2606.28562v1 与 official exact-v1 HTML；不使用 later version，不把 benchmark outcome 外推为生产 SLO。
<!-- claim:SF-2026-ARXIV-2606-28562:end -->
<!-- review:SF-2026-ARXIV-2606-28562:end -->

<!-- review:SF-2026-ARXIV-2606-28565:start -->
### 2606.28565 — KernelSight-LM: A Kernel-Level LLM Inference Simulator

**问题、约束与旧路径。** As large language models (LLMs) move into production serving, practitioners must rapidly evaluate inference performance across diverse hardware, models, and serving parameters to meet cost and latency targets. However, the end-to-end behavior of LLMs couples serving-layer policies with low-level GPU kernel execution and rapidly evolving architectures, forcing slow, deployment-specific benchmarking that is hard to generalize. 旧路径在论文新增条件之外仍然合理。

**机制、state/data/control owner。** 把 serving scheduler、kernel、communication 与 host overhead 组合成 token/kernel-level capacity simulator。 由 INFER-REQUEST-LIFECYCLE 持有 request phase、runtime placement、queue 与 latency state；相邻节点只消费版本化 handoff。

**Evaluation：证明与未证明。** A second target-measured tier adds one model-agnostic kernel-microbenchmark sweep on the target GPU, sharpening per-kernel error to 3.8%, a 7.3x improvement over a comparable baseline (27.7%). Method=https://arxiv.org/html/2606.28565v1 — §2.1. Modern LLMs and Inference Frameworks; 3.3. Gaps in Existing Approaches; 4. Tool Architecture and Methodologies；Evaluation=https://arxiv.org/html/2606.28565v1 — §5.2. Production Kernel Microbenchmarking; 6. Experimental Setup; 7. Results and Analysis。评测合同逐字段冻结，未公开项才写 Not Disclosed。

**Trade-off、failure、fallback、coexistence 与 evolution。** In our simulator, these predictions yield end-to-end median (p50) errors across six model families of 15.4%, 12.8%, and 3.0% (TTFT, TPOT, throughput) in the cross-generation tier and 14.3%, 6.2%, and 2.7% in the target-measured tier, matching dedicated profiling tools while collecting far less on-device data. Simulation 与 component latency 不证明生产 SLO 或 embodied success；mismatch、thermal drift 或 deadline miss 时回退已实测的保守 placement/control。 Counterevidence/limitation=https://arxiv.org/html/2606.28565v1 — §8. Conclusions; Appendix B Limitations。

<!-- claim:SF-2026-ARXIV-2606-28565:start -->
Claim boundary：仅 arXiv:2606.28565v1 与 official exact-v1 HTML；不使用 later version，不把 benchmark outcome 外推为生产 SLO。
<!-- claim:SF-2026-ARXIV-2606-28565:end -->
<!-- review:SF-2026-ARXIV-2606-28565:end -->

<!-- review:SF-2026-ARXIV-2606-28574:start -->
### 2606.28574 — Correct codes for the wrong reasons? validating LLMs as measurement instruments for theoretical constructs

**问题、约束与旧路径。** When a large language model (LLM) codes a construct in text as a human annotator would, that agreement makes the LLM a reliable coder. Yet reliability leaves construct validity untouched. 旧路径在论文新增条件之外仍然合理。

**机制、state/data/control owner。** 把 LLM coder 的表面一致性与 theoretical construct validity 分开，并要求 clause-level extractive evidence。 由 PLATFORM-EVALUATION-SYSTEM 持有 oracle、metric、slice 与结论发布；相邻节点只消费版本化 handoff。

**Evaluation：证明与未证明。** Validation shifts from scoring an instrument's outputs against an annotator to showing that the instrument runs on the construct its theory specifies. Method=https://arxiv.org/pdf/2606.28574v1 — §1.7 The three opacities; 2 Construct validity; 3 Grain calibration；Evaluation=https://arxiv.org/pdf/2606.28574v1 — §3.1 Clauses with grounds; 3.2 Human in the loop。评测合同逐字段冻结，未公开项才写 Not Disclosed。

**Trade-off、failure、fallback、coexistence 与 evolution。** exact-v1 的结论只覆盖《Correct codes for the wrong reasons? validating LLMs as measurement instruments for theoretical constructs》在 3.1 Clauses with grounds; 3.2 Human in the loop 声明的实验；它没有证明跨 model family、hardware/runtime、数据分布或未测 failure mode 的普遍成立。 现有 owner 已覆盖同一长期原则，因此只作为受限反例或实例留在 Daily，不复制 Books 分支。 Counterevidence/limitation=https://arxiv.org/pdf/2606.28574v1 — §1.1 Where the instrument fails; 2.1 Still the wrong reasons; 3.1 Clauses with grounds。

<!-- claim:SF-2026-ARXIV-2606-28574:start -->
Claim boundary：仅 arXiv:2606.28574v1 与 official exact-v1 HTML；不使用 later version，不把 benchmark outcome 外推为生产 SLO。
<!-- claim:SF-2026-ARXIV-2606-28574:end -->
<!-- review:SF-2026-ARXIV-2606-28574:end -->

<!-- review:SF-2026-ARXIV-2606-28615:start -->
### 2606.28615 — What LLMs explain is not what they believe: Evaluating explanation sufficiency under models' own input beliefs

**问题、约束与旧路径。** Large language models (LLMs) are increasingly deployed in high-stakes domains, where free-text explanations such as chain-of-thought and post-hoc rationales are used to justify model outputs. Yet it remains unclear whether these explanations are sufficient, i.e., if they contain enough information to explain the model's output-generating process. 旧路径在论文新增条件之外仍然合理。

**机制、state/data/control owner。** 把 free-text explanation sufficiency 绑定显式 input distribution 与 self-consistent information metric。 由 PLATFORM-EVALUATION-SYSTEM 持有 oracle、metric、slice 与结论发布；相邻节点只消费版本化 handoff。

**Evaluation：证明与未证明。** Analysis of final-token hidden states shows that top and bottom SCSuff scores can be predicted from internal representations, suggesting that SCSuff can guide detection and improvement of sufficient LLM explanations. Method=https://arxiv.org/html/2606.28615v1 — §Appendix C Algorithms；Evaluation=https://arxiv.org/html/2606.28615v1 — §5 Experiments; 5.4 Additional analysis; Appendix E Additional results。评测合同逐字段冻结，未公开项才写 Not Disclosed。

**Trade-off、failure、fallback、coexistence 与 evolution。** We formalize self-consistent sufficiency as a goal for free-text explanations and introduce an information-theoretic metric, SCSuff, that enables evaluation of free-text explanations without relying on predefined biases or shortcuts. 现有 owner 已覆盖同一长期原则，因此只作为受限反例或实例留在 Daily，不复制 Books 分支。 Counterevidence/limitation=https://arxiv.org/html/2606.28615v1 — §7 Conclusion。

<!-- claim:SF-2026-ARXIV-2606-28615:start -->
Claim boundary：仅 arXiv:2606.28615v1 与 official exact-v1 HTML；不使用 later version，不把 benchmark outcome 外推为生产 SLO。
<!-- claim:SF-2026-ARXIV-2606-28615:end -->
<!-- review:SF-2026-ARXIV-2606-28615:end -->

<!-- review:SF-2026-ARXIV-2606-28639:start -->
### 2606.28639 — The Unverifiability of Artificial General Intelligence (AGI) Alignment, Static and Dynamic: From Trakhtenbrot's Wall to the Safety-Generality Tension

**问题、约束与旧路径。** We establish the mathematical limits of AGI safety in two forms: verifying a fixed system, and verifying that a certified safety property persists once the system self-modifies. In the static case, no algorithm can certify a highly expressive AGI's safe behaviour infallibly, completely and tractably, whether over unbounded input domains (blocked by Rice's and Godel's theorems) or over all finite hardware configurations (blocked by Trakhtenbrot's theorem, which splits into a PSPACE-hardness barrier and a co-RE-completeness barrier), forcing a Soundness-Completeness-Tractability Trilemma as a structural, not statistical, necessity. 旧路径在论文新增条件之外仍然合理。

**机制、state/data/control owner。** 给 static/dynamic alignment certification 划出 expressivity、soundness、completeness 与 tractability 的形式边界。 由 PLATFORM-SECURITY 持有 authority envelope、untrusted input 与 release gate；相邻节点只消费版本化 handoff。

**Evaluation：证明与未证明。** These results give formal content to the unverifiability of AI, showing it is not an engineering target deferred by current limits but a structural tension, an Expressivity Invariant governed by the same computational laws as the Halting Problem and Rice's Theorem. Method=https://arxiv.org/pdf/2606.28639v1 — §2 The Unverifiability of AGI Alignment; 4 The Semantic Barrier; 6 Trakhtenbrot's Wall；Evaluation=https://arxiv.org/pdf/2606.28639v1 — §7 Formal Conclusion of the Proof; 9 Theorem of Finite Structural Unverifiability。评测合同逐字段冻结，未公开项才写 Not Disclosed。

**Trade-off、failure、fallback、coexistence 与 evolution。** Three practical risks (finite test coverage, bounded deliberation time, restricted observation) are one phenomenon: every bounded scheme that does not reject correct evidence admits an evolution trace it certifies at every stage while the property is persistently violated. 现有 owner 已覆盖同一长期原则，因此只作为受限反例或实例留在 Daily，不复制 Books 分支。 Counterevidence/limitation=https://arxiv.org/pdf/2606.28639v1 — §10 Applied Engineering; 11 Conclusions。

<!-- claim:SF-2026-ARXIV-2606-28639:start -->
Claim boundary：仅 arXiv:2606.28639v1 与 official exact-v1 HTML；不使用 later version，不把 benchmark outcome 外推为生产 SLO。
<!-- claim:SF-2026-ARXIV-2606-28639:end -->
<!-- review:SF-2026-ARXIV-2606-28639:end -->

<!-- review:SF-2026-ARXIV-2606-28649:start -->
### 2606.28649 — RIPA: Sensory-Vector Prompt Injection Attacks on LLM-Controlled ROS 2 Robots

**问题、约束与旧路径。** We present RIPA, the first systematic multi-channel empirical study of prompt injection attacks delivered through the sensory pipeline of a ROS 2-based LLM-controlled robotic system. Across 100 independent runs per injection variant on five LLMs spanning four model families and parameter scales from approximately 4B to approximately 284B (DeepSeek-V4-Flash, Llama-3-8B-Instruct-Lite, Llama-3.3-70B-Instruct-Turbo, Qwen 2.5-7B-Instruct-Turbo, Gemma-3n-E4B), we identify model-specific vulnerability profiles that do not follow a monotonic scaling trend: Llama-3.3-70B-Instruct-Turbo exhibits 100% attack success rate (ASR) across all injection variants, while Llama-3-8B-Instruct-Lite and Qwen 2.5-7B-Instruct-Turbo resist direct-override injection (0% ASR), and the smallest model evaluated (Gemma-3n-E4B, approximately 4B) matches the 70B model's vulnerability profile, indicating that robustness is model-specific rather than scale-dependent. 旧路径在论文新增条件之外仍然合理。

**机制、state/data/control owner。** 把 robot prompt injection threat surface 扩展到 OCR、audio 与 LiDAR-derived system context，并测 firewall bypass。 由 PLATFORM-SECURITY 持有 authority envelope、untrusted input 与 release gate；相邻节点只消费版本化 handoff。

**Evaluation：证明与未证明。** All code, data, and results are publicly available. Method=https://arxiv.org/html/2606.28649v1 — §II-C Security of ROS-Based Systems; III-A System Model; IV Methodology；Evaluation=https://arxiv.org/html/2606.28649v1 — §V Experimental Results; V-B Firewall Defense Evaluation; V-C Firewall Bypass Analysis。评测合同逐字段冻结，未公开项才写 Not Disclosed。

**Trade-off、failure、fallback、coexistence 与 evolution。** Across 100 independent runs per injection variant on five LLMs spanning four model families and parameter scales from approximately 4B to approximately 284B (DeepSeek-V4-Flash, Llama-3-8B-Instruct-Lite, Llama-3.3-70B-Instruct-Turbo, Qwen 2.5-7B-Instruct-Turbo, Gemma-3n-E4B), we identify model-specific vulnerability profiles that do not follow a monotonic scaling trend: Llama-3.3-70B-Instruct-Turbo exhibits 100% attack success rate (ASR) across all injection variants, while Llama-3-8B-Instruct-Lite and Qwen 2.5-7B-Instruct-Turbo resist direct-override injection (0% ASR), and the smallest model evaluated (Gemma-3n-E4B, approximately 4B) matches the 70B model's vulnerability profile, indicating that robustness is model-specific rather than scale-dependent. 证据只覆盖特定 ROS 2 transformation 与 attack，不覆盖所有 sensor/model；provenance 缺失或 modality 冲突时，在 action 前 fail closed。 Counterevidence/limitation=https://arxiv.org/html/2606.28649v1 — §III Threat Model; VI Discussion; VI-C The Sensory Vector as a Distinct Threat。

<!-- claim:SF-2026-ARXIV-2606-28649:start -->
Claim boundary：仅 arXiv:2606.28649v1 与 official exact-v1 HTML；不使用 later version，不把 benchmark outcome 外推为生产 SLO。
<!-- claim:SF-2026-ARXIV-2606-28649:end -->
<!-- review:SF-2026-ARXIV-2606-28649:end -->

<!-- review:SF-2026-ARXIV-2606-28661:start -->
### 2606.28661 — When More Sampling Hurts: The Modal Ceiling and Correlation Ceiling of Test-Time Scaling

**问题、约束与旧路径。** People overthink; language models over-sample, and the extra effort can talk both into a worse answer. Reasoning systems answer a hard question by sampling it many times (test-time scaling), and the more they draw, the more often a correct answer turns up somewhere, so coverage, the fraction of problems with at least one correct try, climbs and appears to be progress. 旧路径在论文新增条件之外仍然合理。

**机制、state/data/control owner。** 区分 test-time sampling coverage 与可部署 selection，并定义 modal/correlation ceiling 的停止边界。 由 PLATFORM-EVALUATION-SYSTEM 持有 oracle、metric、slice 与结论发布；相邻节点只消费版本化 handoff。

**Evaluation：证明与未证明。** The gap between climbing coverage and stalled selection, the identifiability gap, is the answer a model can produce but not pick. Method=https://arxiv.org/html/2606.28661v1 — §Proposition 1 (Design effect of test-time sampling) .; Two-stage design effect.；Evaluation=https://arxiv.org/html/2606.28661v1 — §1 Introduction and roadmap; 2 Test-time sampling is cluster sampling。评测合同逐字段冻结，未公开项才写 Not Disclosed。

**Trade-off、failure、fallback、coexistence 与 evolution。** But a deployed system must return one answer, and choosing it, not knowing which try is right, is selection; selection is capped, and past a point extra samples only make the model surer of a confident mistake, even as every draw adds cost. Semantic judge 与 selector 都可能错误或相关；uncovered/undecidable 必须保持 Unknown，高风险分歧交回独立 verification 或人工。 Counterevidence/limitation=https://arxiv.org/html/2606.28661v1 — §6 Conclusion。

<!-- claim:SF-2026-ARXIV-2606-28661:start -->
Claim boundary：仅 arXiv:2606.28661v1 与 official exact-v1 HTML；不使用 later version，不把 benchmark outcome 外推为生产 SLO。
<!-- claim:SF-2026-ARXIV-2606-28661:end -->
<!-- review:SF-2026-ARXIV-2606-28661:end -->

## 4. Benchmark Contracts

<!-- validator:benchmark-contract-v1 -->
| Source Family ID | Workload | Model | Hardware | Precision | Input Length | Output Length | Batch | Concurrency | SLO | Evaluator |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2606-27632 | The tool use benchmark suite includes API-Bank ( Li et al., 2023b ) , which assesses tool selection and execution in multi-turn dialogues over 73 API tools, and BFCL ( Patil et al., 2024 ) (Berkeley Function Calling Leaderboard), which evaluates function-calling capability across dimensions such as AST accuracy, execution accuracy, live API interactions, multi-turn conversations, and relevance detection. | We evaluate Yuvion-8B and Yuvion-32B alongside representative general-purpose baselines including GPT-5.4, Qwen3-32B, Qwen3.5-27B, Qwen3-Max, and DeepSeek-R1. | Output normalization. | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | The tool use benchmark suite includes API-Bank ( Li et al., 2023b ) , which assesses tool selection and execution in multi-turn dialogues over 73 API tools, and BFCL ( Patil et al., 2024 ) (Berkeley Function Calling Leaderboard), which evaluates function-calling capability across dimensions such as AST accuracy, execution accuracy, live API interactions, multi-turn conversations, and relevance detection. |
| SF-2026-ARXIV-2606-27634 | As a base for our experiments, we defined our sequential personalization setting following a continual learning setup with a sequence tasks: In order to explore both the continual learning and the stability scenarios, we leverage the TRACE benchmark ( Wang et al., 2023b ) . | Qwen 3.5 0.8B, Llama 3.2 1B Instruct and Gemma 3 1B IT | NVIDIA Titan X (11 GB), CUDA 11.8 | In order to do so, techniques such as quantization, pruning, and distillation have been employed to compress the models to a size that can fit on edge devices. | Training maximum length 512 tokens | Evaluation maximum output 256 tokens | Training batch size 2 with gradient accumulation 8; evaluation batch size 4 | Not Disclosed | Not Disclosed | Exact-match task accuracy plus ACC, BWT, FWT, KL divergence, entropy and margin over three seeds |
| SF-2026-ARXIV-2606-27650 | We evaluate GenWorld through three cases: a full-city weekday baseline, a weekday–weekend behavioral contrast, and a warning-response perturbation. | We use K = 10 K=10 – 30 30 samples per context key with a single teacher model (Gemma 3 27B); ablation of sampling count, temperature, and teacher model choice is needed. | We define a query-conditioned interface in which raw city and persona states are mapped into binned observations, actions are selected from finite candidate sets, outputs are JSON-validated, and execution traces are recorded in machine-readable form. | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Against this reference, the 90,744 synthetic workers assigned to workplaces have a mean commute distance of 10.81 km, median of 10.09 km, and 90th percentile of 19.15 km. | Not Disclosed | Not Disclosed |
| SF-2026-ARXIV-2606-27669 | We conduct experiments on DiscoBench across a set of representative LLMs. | We evaluate Claude-Opus-4.7, GPT-5.4, Gemini-3.1-Pro-Preview, Doubao-Seed-2.0-Pro-High, DeepSeek-V4-Pro, Qwen-3.6-Max, MiniMax-M2.7, GLM-5.1, MiMo-v2.5-Pro, Kimi-K2.6, and Hunyuan-3.0-Preview under the same interactive retrieval framework and checkpoint-level evaluator. | 7 summarizes the total input and output tokens under the Neutral and Guided prompting settings. | Not Disclosed | 7 summarizes the total input and output tokens under the Neutral and Guided prompting settings. | Not Disclosed | Not Disclosed | (2022) focus on mapping single queries to multiple concurrent valid facts. | Not Disclosed | This section provides detailed definitions of the evaluation metrics used in our experiments. |
| SF-2026-ARXIV-2606-27679 | Our study covers a wide range of recently proposed feature representations, spanning latent embeddings, output probabilities, attention patterns, and their combinations ( Azaria and Mitchell, 2023 ; Chuang et al., 2024 ; He et al., 2024 ; Huang et al., 2025b ; Shelmanov et al., 2025 ) , evaluated with different probe architectures, supervision sizes, prompting strategies, and automated correctness labels. | We further study benchmark-to-benchmark transfer and a deployment-oriented setting in w We evaluate on seven datasets spanning three tasks: For the main experiment, we evaluate with five popular LLMs across three model families: Llama-3.1-8B ( Grattafiori et al., 2024 ) , Qwen-3-4B, Qwen-3-8B ( Yang et al., 2025 ) , Qwen-3.5-9B ( Qwen Team, 2026 ) , Gemma-3-12B ( Kamath et al., 2025 ) . | Our study covers a wide range of recently proposed feature representations, spanning latent embeddings, output probabilities, attention patterns, and their combinations ( Azaria and Mitchell, 2023 ; Chuang et al., 2024 ; He et al., 2024 ; Huang et al., 2025b ; Shelmanov et al., 2025 ) , evaluated with different probe architectures, supervision sizes, prompting strategies, and automated correctness labels. | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed |
| SF-2026-ARXIV-2606-27681 | A large body of work has focused on building better dynamics models ( Hafner et al., 2019a ; Hafner et al., 2019b ; Hafner et al., 2023 ; Schritt Our experiments evaluate whether enforcing strict mediation via fGRPO preserves predictive accuracy (Prop 1 ), yields more informative latent states (Prop 2 ), and improves rollout stability (Prop 3 ). | We additionally apply a small set of determ We experiment with three pretrained instruction-tuned language models: Qwen2.5-0.5B-Instruct (0.5B parameters), Qwen3-4B-Instruct-2507 (4B parameters) and Qwen3-32B (32B parameters). | Each instance is equipped with 8 NVIDIA A100-SXM4 GPUs (80GB memory each), for a total of 640GB GPU memory per node. | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed |
| SF-2026-ARXIV-2606-27683 | We evaluate CBD on benchmark unlearning datasets against white-box and gray-box baselines, showing an improved unlearning-utility trade-off under the API-only black-box setting. | We use the ToFU-released Llama-2-7B-Chat model 3 3 3 https://hu We first review the two mainstream unlearning paradigms and clarify why the API-only setting requires a different solution. | Second, auxiliary-model-bas layer input and output dimensions where the forget loss ℒ f wb \mathcal{L}_{f}^{\mathrm{wb}} drives the model away from the forget data, the retain loss ℒ r wb \mathcal{L}_{r}^{\mathrm{wb}} preserves behavior on retained data, and λ \lambda trades off the two. | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed |
| SF-2026-ARXIV-2606-27704 | To address these challenges, we propose AdvScan, a runtime power analysis-based methodology for AE detection that operates in a black-box We evaluate AdvScan on two MCU platforms, an STM32F303RC (Arm Cortex-M4) and an STM32L562RE (Arm Cortex-M33), running three TinyML models in the presence of AEs generated by Fast Gradient Sign Method (FGSM) [ 4 ] , Projected Gradient Descent (PGD) [ 5 ] , and the Carlini–Wagner (C&W) attack [ 6 ] under L 0 L_{0} , L 2 L_{2} , and L ∞ L_{\infty} norms. | Not Disclosed | IV-C 1 Gated-output mode An adversarial example (AE) is a maliciously crafted input designed to make NN models misclassify. | TinyML models commonly use aggressive quantization and pruning to fit within limited hardware constraints, making them more vulnerable to adversarial attacks than traditional neural networks (NNs) [ 45 ] . | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | However, existing AE detection methods either require white-box model access, which is often unavailable in licensed black-box deployments, or rely on input pre-processing stages that add non-trivial latency and resource overhead, often exceeding what mission-critical applications can afford on their inference path. |
| SF-2026-ARXIV-2606-27709 | Our experiments reveal that fine-tuning on empathetic dialogues whose user turns reflect low Agreeableness , a Big Five trait associated with skepticism, directness, and resistance to social pressure ( Costa and McCrae, 1992 ; Jensen-Campbell and Graziano, 2001 ) , paired with warm, de-escalating assistant responses, outperforms both generic empathetic data and warmth-rewritten baselines on adversarial safety measures. | We conducted three main experiments across four models: SmolLM3-3B , Llama-3.1-8B , Qwen2.5-7B-Instruct , and Mistral-7B-Instruct-v0.3 , varying only dataset composition. | 1 NVIDIA L20 GPU (48 GB VRAM) | 4-bit quantization | Maximum sequence length 1024 tokens | Not Disclosed | Batch size 8; gradient accumulation 2 | Not Disclosed | Not Disclosed | (2026) extend this to supervised fine-tuning: warm assistant responses increase sycophancy by eleven percentage points and degrade factual accuracy, with the data’s warmth identified as the causal driver. |
| SF-2026-ARXIV-2606-27732 | We evaluate R2LM through a controlled three-way comparison against the bidirectional and causal dLLM endpoints under a matched 60 60 B-token continued-pretraining protocol on Qwen3- 1.7 1.7 B. | We evaluate R2LM through a controlled three-way comparison against the bidirectional and causal dLLM endpoints under a matched 60 60 B-token continued-pretraining protocol on Qwen3- 1.7 1.7 B. | 32 NVIDIA H100 GPUs (4 nodes × 8 GPUs) | bfloat16 | Sequence length 4096 tokens | Not Disclosed | Per-device batch size 8; no gradient accumulation | Not Disclosed | Not Disclosed | However, such promising frameworks face a fundamental architectural design dilemma: ❶ Adopting bidirectional attention achieves strong generation quality by allowing each position to access the full context, but is inherently incompatible with KV caching, limiting inference throughput in batch-serving scenarios; ❷ Conversely, causal attention enables efficient cached inference but loses all right-side context, substantially degrading generation quality. |
| SF-2026-ARXIV-2606-27739 | We conduct a series of experiments to answer four research questions: Our experiments focus on math reasoning, where the correctness of intermediate steps and final answers is relatively well-defined and easy to verify. | We train PRMs on the Math-Shepherd dataset, using Qwen2.5-Math-7B-Instruct as the backbone. | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | For all methods except PQM, we use a global batch size (GPU count × gradient accumulation steps × per-GPU batch size) of 384 on Qwen2.5-Math-7B-Instruct and Llama3.2-3B-Instruct backbones, and 512 on Qwen3-4B. | Not Disclosed | Not Disclosed | Not Disclosed |
| SF-2026-ARXIV-2606-27743 | We design our experiments to rigorously validate two central hypotheses: (1) Our unified optimization framework with dynamic gating, achieves a superior performance-efficiency trade-off compared to static or heuristic methods. | We evaluate on two representative open-source backbones, Llama-3-8B ( Dubey et al., 2024 ) and Qwen-3-4B ( Yang et al., 2024a ) , to test whether the proposed gating-and-adaptation framework transfers across model families. | Not Disclosed | Not Disclosed | Complementary approaches learn to skip computation inside the backbone: Mixture-of-Depths routes a subset of tokens through each layer under a fixed token budget ( Raposo et al., 2024a ) , while layer-skipping To make the transition behavior explicit, we assume a structured generation format <think> ⋯ \cdots </think> <answer> ⋯ \cdots </answer> . | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | w/o head gating (layer-only) underperforms the joint strategy at similar latency constraints. |
| SF-2026-ARXIV-2606-27757 | In this section, we conduct comparative experiments to evaluate the performance. | In addition, we construct a plan recogn To validate the superior planning capabilities of our framework, we conducted comparative experiments with three mainstream LLMs: GPT-4o, Claude-3-5, and DeepSeek-R1, using standard inference parameters (temperature = 0.1) for consistency. | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | We evaluate performance using planning coverage (success rate), defined as the proportion of problems solved relative to the total number of problems. |
| SF-2026-ARXIV-2606-27780 | We evaluate the framework on a seven-topology synthetic benchmark with existing GWM baselines, including GCN Kipf and Welling (2017) , MPNN Gilmer et al. | Not Disclosed | In an agent system, node features can encode agent status, tool outputs, skill availability, task progress, or failure signals. | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed |
| SF-2026-ARXIV-2606-27791 | We evaluate NLL-guided layer selection on Qwen3-4B-Thinking-2507 3 3 3 https://huggingface.co/Qwen/Qwen3-4B-Thinking-2507 ( Yang et al., 2025 ) , a 36-layer model, using the LongMemEval benchmark ( Wu et al., 2025 ) . | We evaluate NLL-guided layer selection on Qwen3-4B-Thinking-2507 3 3 3 https://huggingface.co/Qwen/Qwen3-4B-Thinking-2507 ( Yang et al., 2025 ) , a 36-layer model, using the LongMemEval benchmark ( Wu et al., 2025 ) . | We propose NLL-guided layer selection , a principled approach that directly measures what we care about: how much does each layer’s output quality degrade when we restrict its attention? | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed |
| SF-2026-ARXIV-2606-27797 | Teacher-student generative knowledge distillation with asymmetric partition and communication plans | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | End-to-end GKD training time and topology/partition ablations |
| SF-2026-ARXIV-2606-27806 | TaskGraph, ToolChain, ResourceAlloc and RepairFlow; 100 test tasks per benchmark (60 in-distribution, 40 out-of-distribution) | Because production LLM rollouts are expensive, the agent and hybrid behaviours are reproduced by a behavioural simulator calibrated against measured GPT-4o-mini TaskGraph runs (the real-API validati We train a small parametric world model F θ : ( G t , a ) ↦ ( p ^ valid , Δ ​ G ^ , r ^ , p ^ done , ρ ^ , U ^ , J ^ K ) F_{\theta}:(G_{t},a)\mapsto(\hat{p}_{\text{valid}},\widehat{\Delta G},\hat{r},\hat{p}_{\text{done}},\hat{\rho},\hat{U},\hat{J}_{K}) on oracle transitions 𝒟 = { ( G t , a t , G t + 1 , r t , d t , m t ) } \mathcal{D}=\{(G_{t},a_{t},G_{t+1},r_{t},d_{t},m_{t})\} with the multi-task loss We use four graph-structured world-model planning benchmarks—TaskGraph … | Structured output and grounding. | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Eleven agent-only, parametric-only and hybrid planners evaluated on plan validity/reward and hallucinated state transitions |
| SF-2026-ARXIV-2606-27814 | We evaluate ATOD on three long-horizon agent benchmarks: ALFWorld, WebShop, and Search-QA. | Qwen3-0.6B, Qwen3-1.7B and Qwen3-4B student models | 8 GPUs on one node | Not Disclosed | Not Disclosed | Not Disclosed | Train batch sizes ALFWorld/WebShop/Search-QA = 16/128/16; validation = 128/512/128 | Not Disclosed | Not Disclosed | However, strong agentic behavior is usually concentrated in large models, whose inference cost and deployment overhead are undesirable in latency-, privacy-, and resource-sensitive settings. |
| SF-2026-ARXIV-2606-27826 | As shown in Figure 1 , we evaluate three cue conditions of increasing explicitness to diagnose why models fail and find that models can often comply with the relevant norm when the constraint is made explicit but fail to infer it from the scene alone. | We used GPT-4o to analyze the failure causes in the action sequences generated by the models. | 5.2 Output Parsing and Error Labels E Output Parsing and Error Labels MLLM are increasingly used as embodied planners in first-person environments, where they must interpret visual observations, follow natural-language instructions, and output executable action plans ( Liu et al., 2023 ; Li et al., 2023b ; Dai et al., 2023 ; Bai et al., 2025 ; Zitkovich et al., 2023 ; Wang et al., 2023 ) . | Not Disclosed | Not Disclosed | Not Disclosed | We use 60 training epochs, a batch size of 4, and a learning rate of 1 ​ e − 4 1e^{-4} . | Not Disclosed | Not Disclosed | Each sequence is scored according to three binary rewards: We evaluate whether MLLM -based embodied planners treat social norms as implicit constraints when producing high-level action plans for ordinary embodied tasks. |
| SF-2026-ARXIV-2606-27841 | As our experiments in Section 4 show, adding new tasks to the database weakens the estimation performance of the final model. | Not Disclosed | NVIDIA H100, A100 and TITAN X measurements | Although pruning is accounted for in the model due to its impact on layer shapes, other acceleration techniques such as quantization or sparsification have not been explicitly included in the methodology. | Not Disclosed | Not Disclosed | LLM zero-shot energy evaluation uses batch size 1 | Not Disclosed | Not Disclosed | (2024) have investigated the internal mechanisms of energy measurement provided by NVIDIA-smi and found that the tool has an overall measurement error of 5%. |
| SF-2026-ARXIV-2606-27866 | We conducted comprehensive experiments on Mixtral-8x7B, Phi-3.5-MoE, and Qwen2-57B-A14B. | We conducted comprehensive experiments on Mixtral-8x7B, Phi-3.5-MoE, and Qwen2-57B-A14B. | During action training, all parameters are kept and we only use prefix mask m ⁡ ( r ) m(r) to simulate pruned expert outputs, but during deployment, parameters masked by learned actions can be dropped or excluded from forward calculations to reduce cost. | Chen Examining post-training quantization for mixture-of-experts: a benchmark . | Not Disclosed | Not Disclosed | Not Disclosed | We use the SGLang engine ( Zheng et al., 2024 ) on a single H200 GPU under a synthetic workload with 4096 prompt requests, input length = 64 =64 , output length = 256 =256 1 1 1 SGLang is a serving-oriented runtime which is designed for high-throughput structured LLM execution, and this setup is intended to approximate a realistic serving regime with substantial concurrent traffic, rather than a single-request latency test. | Not Disclosed | We further show that the shared weights recovered from single mid-budget fine-tune strategy transfers well to unseen higher and lower budgets, and that the resulting subnet family delivers real throughput gains and more flexible interfaces in deployment, especially when coupled with our explor Task Accuracy Results Analysis. |
| SF-2026-ARXIV-2606-27906 | FastVLM-0.5B FP16 CPU versus INT8 NPU on 500 COCO val2017 images and 200 VQAv2 questions | We use FastVLM-0.5B ( 1 ) as the primary model: a 0.5B-parameter VLM built on Qwen-0.5B ( 8 ) with a FastViT encoder that applies aggressive token compression for mobile execution. | Snapdragon mobile SoC CPU and Qualcomm NPU paths | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | COCO CIDEr and VQAv2 lowercase-normalized exact-match accuracy |
| SF-2026-ARXIV-2606-27934 | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Throughput divergence. |
| SF-2026-ARXIV-2606-27936 | We evaluate the pipeline on a spatio-temporal dataset containing simulated location points anchored at and around true home and work addresses, focusing on a high-risk disclosure scenario. | Not Disclosed | Each stage produces structured output consumed by the next; the orchestrator enforces quality gates between transitions and halts the run early when evidence falls below a sufficiency threshold. | Zettlemoyer (2023) QLoRA: efficient finetuning of quantized LLMs . | Not Disclosed | Not Disclosed | Not Disclosed | A bash script parallelises one session per device CSV file at a concurrenc Across the 43 evaluation runs, each attempt cost on average $2.24 in API charges at list prices, produced on average 58.5K output tokens (range: 39.5K–78.9K), and took on average 17 minutes of unattended computation (range: 11.7–28.5 minutes). | Not Disclosed | Our results demonstrate that, from spatio-temporal data and public sources alone, our agentic AI successfully re-identified Re-identifying individuals at scale from spatio-temporal mobility traces has historically required sophisticated technical knowledge, including API configuration, data preprocessing, and familiarity with OSINT techniques. |
| SF-2026-ARXIV-2606-27944 | We evaluate Phone-use Agents built on four commercial models (Claude-Sonnet-4.5, GPT-5.4-medium, Gemini-3.1-Pro, and Seed-2.0-Pro) and five open-source models. | We evaluate Phone-use Agents built on four commercial models (Claude-Sonnet-4.5, GPT-5.4-medium, Gemini-3.1-Pro, and Seed-2.0-Pro) and five open-source models. | Phone-use Agents perceive the phone screen, interpret natural-language instructions, and output directly executable UI actions (tapping, typing, swiping, etc.) [ 24 , 9 , 12 , 35 , 33 ] . | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | For each level, we report the success rate (SR) , defined as the fraction of samples for which the misuse task is completed, and the refusal rate (RR) , defined as the fraction of samples for which the model identifies pote Evaluation Setups . |
| SF-2026-ARXIV-2606-27962 | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed |
| SF-2026-ARXIV-2606-27976 | The client encodes the query, v q = E ⁡ ( q text ) ∈ ℝ d v_{q}=E(q_{\mathrm{text}})\in\mathbb{R}^{d} , and forms the rotated query q ′ = R ​ V k ⊤ ​ ( v q − μ ) ∈ ℝ k q^{\prime}=R\,V_{k}^{\top}(v_{q}-\mu)\in\mathbb{R}^{k} ; using the public PQ artefact and q ~ = q ′ \tilde{q}=q^{\prime} it then runs an asymmetric PQ-distance search locally and keeps the top- K cands K_{\mathrm{cands}} candidate IDs I cand I_{\mathrm{cand}} —a short-list small enough ( K cands = 40 K_{\mathrm{cands}}=40 in our experiments) that the CKKS reranking still fits the latency budget. | Not Disclosed | Five reported cells CPU-encoded; e5-large/NFCorpus omitted after exceeding CPU budget | ✓ \checkmark provided, × \times not addressed, ∼ \sim partial/approximate; “exact rerank” is full-dimensional scoring with no quantization/noise loss, “coarse-only leak” means the accessible channel exposes only coarse/topic structure. | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | End-to-end query latency < 1 <1 s at 10 6 10^{6} docs The pipeline of Figure 1 processes a query in stages, of which only the last leaves the client. | The client encodes the query, v q = E ⁡ ( q text ) ∈ ℝ d v_{q}=E(q_{\mathrm{text}})\in\mathbb{R}^{d} , and forms the rotated query q ′ = R ​ V k ⊤ ​ ( v q − μ ) ∈ ℝ k q^{\prime}=R\,V_{k}^{\top}(v_{q}-\mu)\in\mathbb{R}^{k} ; using the public PQ artefact and q ~ = q ′ \tilde{q}=q^{\prime} it then runs an asymmetric PQ-distance search locally and keeps the top- K cands K_{\mathrm{cands}} candidate IDs I cand I_{\mathrm{cand}} —a short-list small enough ( K cands = 40 K_{\mathrm{cands}}=40 in our experiments) that the CKKS reranking still fits the latency budget. |
| SF-2026-ARXIV-2606-27997 | Similarly we use for the pair 𝐑 𝒮 , 𝐑 𝒟 \mathbf{R}_{\mathcal{S}},\mathbf{R}_{\mathcal{D}} Spearman’s Rank Correlation ρ ⁡ ( 𝐑 𝒮 , 𝐑 𝒟 ) \rho(\mathbf{R}_{\mathcal{S}},\mathbf{R}_{\mathcal{D}}) , Kendall’s Rank Correlation τ ⁡ ( 𝐑 𝒮 , 𝐑 𝒟 ) \tau(\mathbf{R}_{\mathcal{S}},\mathbf{R}_{\mathcal{D}}) , Normalized Discounted Cumulative Gain (NDCG@K) with K = 5 K=5 , and Mean Reciprocal Rank (MRR) used in our experiments. | Not Disclosed | Not Disclosed | Not Disclosed | These descriptions are encoded with bert-base-uncased : we tokenize each description with maximum length 256, mean-pool final-layer token embeddings over non-padding tokens, and ℓ 2 \ell_{2} -normalize the resulting 768-dimensional vector. | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | For these four metrics, larger values indicate better preservation of the ranking. |
| SF-2026-ARXIV-2606-28011 | Not Disclosed | Not Disclosed | We propose an agentic Large Language Model (LLM) framework for active Fault-Tolerant Control (FTC) that transforms fault detection outputs into constraint-aware recovery actions grounded in plant-specific knowledge. | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed |
| SF-2026-ARXIV-2606-28013 | Statement autoformalization stratified by Lean type-check and semantic-equivalence judgment | DeepSeek V4-Pro on ProofNet# for the full four-method dual-judging cell | We propose a signal-coverage matrix that crosses the Lean elaborator (pass/fail) with a semantic-equivalence judgment (equivalent/not), sorting every output into one of four cells: true success ( TS ), type-only ( TO ), semantic-only ( SO ), or both fail ( BF ). | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Four-cell TS/TO/SO/BF signal-coverage matrix under dual semantic judging |
| SF-2026-ARXIV-2606-28037 | We evaluate GBV-PD along four dimensions: We evaluate two tasks: image classification (IC) on the CIFAR-100 ( Krizhevsky, 2009 ) and behavior cloning (BC) on the Udacity Jungle dataset ( Su, 2023 ) , released as part of Udacity’s behavior cloning project ( Udacity, 2016 ) . | Not Disclosed | Black-box testing ( Zohdinasab et al., 2023 ) , which relies only on inputs and outputs, provides limited insight into how the model has changed internally. | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | 3.2.3 Projection Error of Delta Loss For regression tasks, let e θ ​ ( x , y ) e_{\theta}(x,y) be a task-specific error function and τ task > 0 \tau_{\mathrm{task}}>0 a threshold for meaningful change: These definitions capture meaningful behavior changes of the model on a test case rather than small numerical fluctuations. |
| SF-2026-ARXIV-2606-28050 | We evaluate two models as ℒ \mathcal{L} : Llama-3.1-8B-Instruct ( Dubey and others, 2024 ) , a capable open-source model at modest scale, and GPT-4o-mini , a stronger proprietary model. | We evaluate two models as ℒ \mathcal{L} : Llama-3.1-8B-Instruct ( Dubey and others, 2024 ) , a capable open-source model at modest scale, and GPT-4o-mini , a stronger proprietary model. | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | We test this in a controlled in-context QA setting where a context passage is the sole information source and each model judges the answer it generated, removing the parametric-knowledge confound of open-domain comparisons. |
| SF-2026-ARXIV-2606-28061 | Not Disclosed | Not Disclosed | 4.8 Evaluation Outputs This case design moves evaluation beyond final-output correctness and makes it possible to inspect how an agent moves information during execution. | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Runtime monitoring and adversarial RAG evaluation further study how agent behavior or retrieved contexts can be scored or stre To make evaluation reproducible and diagnosable, ToolPrivacyBench separates policy definition, runtime evidence capture, disclosure identification, authorization judgment, and metric computation into independent modules. |
| SF-2026-ARXIV-2606-28070 | To assess the efficacy of 𝖲 2 ​ 𝖣 \mathsf{S}^{2}\mathsf{D} , we conducted random sampling of items across diverse categories to evaluate their knowledge recognition results. | Not Disclosed | For example, if “CPU model” already exists, “central processing unit model” is rejected. | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | A single platform must serve all of these highly concurrent, domain-specific demands at once, efficiently building on what the scenarios share while supporting what makes L1 cross-chunk asynchronous pipeline. | Not Disclosed | While each of the aforementioned strategies yields significant throughput gains, they are difficult to stack efficiently in practice. |
| SF-2026-ARXIV-2606-28116 | Low-precision attention, large-learning-rate and combined-fault training-instability injections | Not Disclosed | Not Disclosed | For example, flash attention (FA) exhibits substantially larger BF16 numeric deviation than baseline attention in isolated forward passes ( Golden et al., 2024 ) , and low-precision FA can corrupt weight updates through biased rounding errors and gradually derail training dynamics ( Qiu and Yao, 2026 ) . | Not Disclosed | Not Disclosed | To make the LR–GBS coupling explicit, for global batch size B B write the empirical reinforcement coefficient as The stable-winner feedback loop derived in Section 4 predicts that larger learning rates and smaller global batch sizes amplify router entropy collapse. | Not Disclosed | Not Disclosed | Pre-loss detection lead time and distinct attention/router failure signatures |
| SF-2026-ARXIV-2606-28128 | Not Disclosed | Not Disclosed | All three auxiliary models are frozen and used only to extract physics targets; they are run on the ground-truth clip on the fly during each training step, and the tracker/depth outputs are shared between the two physics losses. | Not Disclosed | Not Disclosed | Not Disclosed | For the two Wan backbones, input videos are resized to 640 × 480 640\times 480 with a maximum length of 81 frames, and both are trained for 20K steps with a global batch size of 128 using the AdamW optimizer with a learning rate of 1 × 10 − 5 1\times 10^{-5} ; for Wan2.2-I2V-A14B, we initialize from its high-noise expert and adapt it to later denoising stages during training. | Not Disclosed | Not Disclosed | In contact-rich manipulation, physical violations often appear as local dynamic errors, such as discontinuous gripper trajectories, object penetration, or anti-gravity motion, and as global relational errors, such as a pushed object remaining static or a grasped object drifting away. |
| SF-2026-ARXIV-2606-28153 | All source datasets are publicly released benchmarks intended for safety research; We evaluate on 10 datasets from the safety-eval framework ( Han et al., 2024 ; Jiang et al., 2024 ) : general intent moderation (WildGuardTest ( Han et al., 2024 ) , ToxicChat ( Lin et al., 2023 ) , OpenAI Moderation ( Markov et al., 2022 ) , Aegis ( Ghosh et al., 2024 ; Ghosh et al., 2025 ) , SimpleSafetyTests ( Vidgen et al., 2024 ) , HarmBench-Vanilla ( Mazeika et al., 2024 ) ) and adversarial-attack detection (WildJailbreak ( Jiang et al., 2024 ) , SALAD-Bench ( Li et al., 2024a ) , HarmBench-Adversarial). | We conduct our analysis on Llama-3-8B-Instruct and Llama-2-7B-Chat. | (2025) , we trace information flow by projecting the mid-layer refusal direction, under a linear framework, into the output space of attention heads across layers, thereby quantifying each head’s contribution to the refusal signal. | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed |
| SF-2026-ARXIV-2606-28166 | We evaluate on AMC 23–25, AIME 24–26, and Minerva Math ( Lewkowycz et al., 2022 ) , and report pass@ k k via an unbiased estimator following Chen et al. | We fine-tune Qwen3-4B-Instruct-2507 ( Yang et al., 2025 ) on DeepScaleR ( Tan et al., 2025 ) with a binary correctness reward on the boxed final answer. | An operational definition of compatibility, or intelligibility, is handoff robustness ( West et al., 2026 ) : a model’s output is intelligible to another agent if that agent can continue it without derailing the trajectory. | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | We estimate bootstrap standard errors by resampling evaluation problems, reported as ± \pm values in tables and as shaded bands in figures. |
| SF-2026-ARXIV-2606-28187 | We evaluate our approach on both task-oriented dialogue (MultiWOZ ( Ye et al., 2022 ) ) and interactive tool-use environments ( τ \tau -bench ( Yao et al., 2025 ) ), demonstrating that GBC significantly improves multi-agent performance across multiple metrics. | Backbone models are Llama-3.3-70B-It and Qwen-3-32B. | In multi-agent workflows, errors in the final output often originate from specific agents or interaction steps, yet existing methods typically rely on coarse-grained signals (e.g., overall task success or reward) to guide optimization ( Khattab et al., 2024 ; Xu et al., 2025 ; Yuksekgonul et al., 2024 ; Zhuge et al., 2024 ; Luo et al., 2025 ) . | For local model serving, we enable FP8 quantization whenever supported by the target model and serving backend. | Not Disclosed | Not Disclosed | Not Disclosed | We adopt a manager–worker architecture (Figure 2 ). | The table shows the inform score, success score, joint goal accuracy (JGA), slot recall, slot precision, and slot F1 score. | Not Disclosed |
| SF-2026-ARXIV-2606-28235 | Not Disclosed | The five agents in AIDev are OpenAI Codex, Devin, GitHub Copilot, Cursor, and Claude Code, and every row is labelled with which one wrote it. | What rules out the obvious alternative, that this traffic is merely an agent acting on its own output, is the composition of the reviewing and commenting accounts. | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Across more than 930,000 agent-authored pull requests, we measure how much of the variation in fr This paper locates the problem in the ecosystem, and measures it. | Not Disclosed | That understanding is a team-level asset that can be lost: projects suffer disproportionate knowledge loss when contributors leave [ 10 ] , and developers who lean on AI assistance score lower on later comprehension of the same code [ 11 ] . |
| SF-2026-ARXIV-2606-28276 | In our experiments, object cousins improve robustness to unseen object instances, scene cousins improve generalization to novel layouts, and task cousins improve both zero-shot and few-shot downstream task performance. | Not Disclosed | SimFoundry extracts per-object relevant information (segmentation masks, depth, etc.), generates 3D visual meshes via 2D-to-3D generation models, and compiles the final output scene by annotating relevant physical parameters and sanity checking the overall scene configuration in a physics simulator. | Not Disclosed | Not Disclosed | Not Disclosed | Each policy is trained with a batch size of 256, a learning rate of 1 ​ e − 5 1e-5 , and for 10k gradient steps. | Not Disclosed | Not Disclosed | The policy success rate with initial subtasks completed in sim is compared with the full end-to-end task success rate in the real world which we found improved evaluation correlations In this sub-section, we provide the scoring rubric for each task, along with the language instruction provided to the VLAs. |
| SF-2026-ARXIV-2606-28277 | Towards this end, we evaluate the real-world utility of PAT on organic, human-authored errors, using the SPOT benchmark ( Son et al., 2025 ) , which compiles manuscripts containing verified mistakes that led to subsequent errata or retractions. | Not Disclosed | However, the Scientific Method requires rigorously validating these outputs, not just generating them. | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | One of the primary aims of PAT is to find technical errors in full-length scientific manuscripts. |
| SF-2026-ARXIV-2606-28279 | We evaluate our approach on ChipBench, RTLLM, Verilog-Eval, and nine CVDP categories, achieving 100% benchmark completion across all suites with a | Model: we use GPT-5.3 as the agent backbone for all experiments, fixed throughout; Benchmarks: ChipBench, RTLLM-2.0, and Verilog-Eval, together with all CVDP code- and verification-generation categories (CID 002 to 016) spanning completion, specification-to-RTL, modification, reuse, linting/QoR, and stimulus, checker, and assertion generation as well as debugging. | RTL generation differs from ordinary code completion because the output defines hardware that must satisfy temporal and bit-accurate behavior. | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | AutoChip drives a generate-compile-simulate feedback loop ( Thakur et al., 2023 ) ; RTLFixer repairs syntax errors with retrieval-augmented, ReAct-style debugging ( Tsai et al., 2024 ) ; VerilogCoder plans with a task-and-circuit-relation graph and traces waveforms via an AST-based tool to localize functional bugs ( Ho et al., 2025 ) ; MAGE decomposes a design across cooperating agents with high-temperature sampling and checkpoint-based debugging ( Zhao et al., 2025 ) ; and ACE-RTL pairs an RTL-specialized generator with a frontier-model reflector and coordinator that evolves the prompting con CVDP also distinguishes non-agentic and agentic settings. |
| SF-2026-ARXIV-2606-28322 | We evaluate a diverse suite of 25 models, spanning proprietary frontier models (e.g., Gemini-3-Pro ( Team, 2025 ) , Gemini-3.5-Flash ( Gemini Team, Google DeepMind, 2026 ) , GPT-5.4 ( OpenAI, 2026b ) , GPT-4o ( OpenAI, 2024 ) , Seed-2.0 ( ByteDance-Seed, 2026c ) , Seed-1.8 ( ByteDance-Seed, 2026b ) , Seed-1.6 ( ByteDance-Seed, 2026a ) , GLM-5V-Turbo ( Hong et al., 2026 ) , Qwen3.5-Plus ( Team, 2026a ) ) and leading open-weights models (e.g.,Qwen3.5-397B ( Team, 2026a ) , Qwen3-VL ( Bai et al., 2025a ) , Qwen2.5-VL ( Bai et al., 2025b ) ,Step3-VL-10B ( Huang et al., 2026 ) , Step-3.7-Flash ( StepFun Team, 2026 ) , MiniMax-M3 ( Lai et al., 2026 ) , MiMo-V2.5 ( Team, 2026b … | We evaluate a diverse suite of 25 models, spanning proprietary frontier models (e.g., Gemini-3-Pro ( Team, 2025 ) , Gemini-3.5-Flash ( Gemini Team, Google DeepMind, 2026 ) , GPT-5.4 ( OpenAI, 2026b ) , GPT-4o ( OpenAI, 2024 ) , Seed-2.0 ( ByteDance-Seed, 2026c ) , Seed-1.8 ( ByteDance-Seed, 2026b ) , Seed-1.6 ( ByteDance-Seed, 2026a ) , GLM-5V-Turbo ( Hong et al., 2026 ) , Qwen3.5-Plus ( Team, 2026a ) ) and leading open-weights models (e.g.,Qwen3.5-397B ( Team, 2026a ) , Qwen3-VL ( Bai et al., 2025a ) , Qwen2.5-VL ( Bai et al., 2025b ) ,Step3-VL-10B ( Huang et al., 2026 ) , Step-3.7-Flash ( StepFun Team, 2026 ) , MiniMax-M3 ( Lai et al., 2026 ) , MiMo-V2.5 ( Team, 2026b … | By analyzing the discrepancies between these actual outputs 𝒫 \mathcal{P} and the reference C g ​ o ​ l ​ d C_{gold} , the rubric proposer identifies frequent hallucinations and subtle misinterpretations. | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed |
| SF-2026-ARXIV-2606-28430 | Not Disclosed | Not Disclosed | Scores can reflect memorization rather than capability ( Sainz et al., 2024 ; Oren et al., 2024 ; Jain et al., 2025 ; Prathifkumar et al., 2025 ) , metric choice rather than ability ( Schaeffer et al., 2023 ) , or judge bias rather than output quality ( Thakur et al., 2025 ) . | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | What benchmark scores actually certify. |
| SF-2026-ARXIV-2606-28433 | Not Disclosed | Not Disclosed | Most libraries provide multi-stream algorithms and parallelization on GPUs to achieve significant speed increases ( Lu et al., 2022 ; DeepMind et al., 2020 ; Bonnet et al., 2024 ; Lange, 2022 ) , with algorithms like PPO ( Schulman et al., 2017 ) , PQN ( Gallici et al., 2025 ) , and A2C ( Mnih et al., 2016 ) . | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed |
| SF-2026-ARXIV-2606-28434 | We evaluate on SWE-Bench-Verified [ SweBench2024 ] . | We use Qwen3-Coder-30B-A3B-Instruct [ DBLP:journals/corr/abs-2505-09388 ] and Qwen3-4B-Instruct-2507 [ DBLP:journals/corr/abs-2505-09388 ] as base models, adopt OpenHands [ OpenHands2025 ] as the base scaffold, and set the context limit to 32,768 tokens throughout data collection, SFT, and RL. | Early capability-oriented work studied code generation [ DBLP:journals/corr/abs-2107-03374 , DBLP:journals/corr/abs-2203-07814 , CodeT5 , abs-2510-17130 , DBLP:journals/corr/abs-2601-00376 , DBLP:journals/corr/abs-2410-01215 ] , program repair [ XiaWZ23 , PengGGHL24 ] , code summarization [ DBLP:journals/corr/abs-2601-05485 ] ,code translation [ RoziereLCL20 , LuoJGGFLXL25 ] , and test generation [ | Not Disclosed | Not Disclosed | Not Disclosed | We train the SFT models with the VeOmni framework [ VeOmni2025 ] using a global batch size of 128, a learning rate of 2 × 10 − 5 2\times 10^{-5} , a cosine learning-rate schedule, and 3 training epochs. | Not Disclosed | Not Disclosed | We report issue resolve rate as the main evaluation metric. |
| SF-2026-ARXIV-2606-28436 | Not Disclosed | For verifier evaluation, we follow [ 28 ] and report AUC, a discrimination metric aligned with SFT filtering and RL r We use Qwen3.5-9B [ 24 ] as the backbone for both Dockerless and the downstream post-training. | Given ( x , y ref , y , { ( Q k , A k ) } k = 1 K ) (x,y_{\text{ref}},y,\{(Q_{k},A_{k})\}_{k=1}^{K}) , the verdict model outputs a binary token in { 0 , 1 } \{0,1\} , where 1 1 denotes a correct patch. | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | 4.5 Latency analysis F Latency distribution Figure 1 : Comparison of verifiers for SWE agents. |
| SF-2026-ARXIV-2606-28438 | Training mixture used in our experiments. | (2024) (HumanEval+ baseline: 0.274, MBPP+ baseline: 0.492), Qwen2.5-Coder-1.5B Hui et al. | In image generation, self-consuming training can reduce distributional variance and drive models toward low-diversity outputs, a failure mode described as model amplification disorder Alemohammad et al. | Not Disclosed | Human gates: (2) Compile applies a syntax gate via compile() ; (3) Quality applies fixed static metrics (repetition rate ≤ 0.3 \leq 0.3 , length ≥ 50 \geq 50 tokens). | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | In our experiments, this case corresponds to perplexity filtering and binary self-scoring, where the code LLM evaluates its own generated samples. |
| SF-2026-ARXIV-2606-28455 | We evaluate GRU, Transformer-lite, and RSSM-lite passive object-state transition models on free-motion, collision, and occlusion events under an eight-frame observed and eight-frame predicted fixed horizon. | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Normalized future-position MSE, event-probe macro-F1, field-readout scores, and fixed-horizon projection CFE. |
| SF-2026-ARXIV-2606-28471 | Two evaluation-to-data case studies: EOS-supervision diagnosis and operation-composition targeted sampling | Not Disclosed | 3.2.5 Output Constraint 4.1.2 Output-Constraint Regression on BBH Model capability is the central variable in LLM pre-training, yet is never observed directly: data shapes it prospectively, while evaluation reveals it only retrospectively, compressing samples, prompts, decoding, and scoring rules into one noisy score. | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | BBH checkpoint recovery plus AIME2025/AIME2026 Pass@128 and operation-level attribution |
| SF-2026-ARXIV-2606-28479 | We evaluate four open-weight SLMs in the 1 1 – 3 3 B range from three independent families, controlling for tokenizer and pretraining-corpus idiosyncrasies in the memorization signal: Gemma 3 1B-IT [ 18 ] , Qwen3 1.7B [ 43 ] , Llama 3.2 3B-Instruct [ 20 ] , and VaultGemma 1B [ 51 ] . | Not Disclosed | Not Disclosed | V0 (raw) : bf16 weights with HuggingFace SFTTrainer , unprotected baseline. | Not Disclosed | Not Disclosed | Not Disclosed | A decade of work establishes that planted canaries are extractable [ 10 , 36 , 22 ] , that memorization scales with capacity, duplication, and prompt length [ 12 , 28 ] , and that fine-tuning, including PEFT, retains measurable leakage [ 38 , 55 ] ; concurrent work cautions that some apparent extraction tracks generalization rather than | Not Disclosed | Not Disclosed |
| SF-2026-ARXIV-2606-28480 | Our analysis reveals that even the strongest evaluated agent achieves only 65.8% success rate, highlighting remaining challenges in long-horizon planning, tool use, execution monitoring, and error recovery. | To this end, we evaluate each candidate task using three frontier models, GPT-5.5 ( OpenAI, 2026 ) , Claude Opus 4.7 ( Anthropic, 2026b ) , and Gemini 3.1 Pro ( The Gemini Team, 2026 ) , each deployed within the Terminus-2 agent framework. | For each task, we also reuse the corresponding input files and gold artifacts from OSWorld, which define the initial task state and the target output for evaluation. | Not Disclosed | Success rate across five thinking-effort settings for GPT-5.5; higher effort costs more tokens and steadily lifts performance. | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Our analysis reveals that even the strongest evaluated agent achieves only 65.8% success rate, highlighting remaining challenges in long-horizon planning, tool use, execution monitoring, and error recovery. |
| SF-2026-ARXIV-2606-28514 | There are eleven default 4 4 4 We exclude Needy Modules from our experiments—a separate class of modules that require repeated attention at random intervals and cannot be evaluated in isolation. | These include GPT-5.2 ( OpenAI, 2025b ) , Claude Sonnet 4.6 ( Anthropic, 2026b ) , Gemini 3 Flash ( Google, 2025 ) , Qwen3.5 ( Qwen Team, 2026 , 27B;) , and InternVL 3.5 ( Wang et al., 2025b , 38B;) . | Structured outputs cannot enforce field ordering. | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | For this, we take each module and ask the following question (filling in the placeholder with the name): Unsalvageable errors. |
| SF-2026-ARXIV-2606-28529 | We evaluate policy models at different scales. | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | We evaluate the latency of policy models’ inference on edge devices such as the Jetson AGX Orin [ 38 ] (denoted AGX 15W/30W/50W ) and server-class GPUs, including the RTX 3090 [ 1 ] and the Ada 6000 [ 39 ] . |
| SF-2026-ARXIV-2606-28551 | Building performant Vision-Language Models (VLMs) requires carefully curating large-scale training datasets, yet the community lacks systematic benchmarks for evaluating such curation strategies. | Not Disclosed | Not Disclosed | Not Disclosed | As part of DCVLM , we collect 160 datasets spanning four data types—image-caption pairs, multimodal interleaved documents, text-only, and instruction-tuning data—into a corpus of 6T multimodal tokens. | Not Disclosed | Global batch size 1024 | Even with 3 filters applied concurrently, the overhead is only 1.10 × 1.10\times baseline, confirming that online filtering is a scalable approach. | Not Disclosed | To ensure that the InternVL LR configurations were optimal, we conducted a small LR-sweep ourselves 2 2 2 We did this LR-sweep quite early on in the project when we had a slightly different experimental setup: (i) we were using the Qwen-Instruct backbones instead of the Qwen-Base LM, and (ii) we had not yet finalized the validation or core evaluation sets, and hence used 12 randomly selected benchmarks for tracking our average-metric. |
| SF-2026-ARXIV-2606-28560 | We evaluate by token-level perplexity on four held-out sets: FineWeb-Edu, Wikipedia, TinyStories, and a math set held out from OpenMathInstruct-2 (problem–solution pairs, a disjoint shard from the training math). | Not Disclosed | All AI-assisted output, including every claim, numerical result, and reference, was reviewed and verified by the author, who takes full responsibility for the content of this paper. | Training is identical across runs: 13,000 steps at an effective batch of 32,768 tokens (426M tokens total), AdamW ( β = 0.9 , 0.95 \beta=0.9,0.95 , weight decay 0.1 0.1 ), learning rate 3 × 10 − 4 3\times 10^{-4} with 300 warmup steps and cosine decay, gradient clip 1.0 1.0 , bf16 autocast, seed 42. | Across 21 language models trained under one matched recipe (60M parameters, 512 hidden, 16 layers, 426M tokens), we compare four ways of setting α \alpha across depth: fixed, per-layer learned, a static linear stagger, and a coprime (anti-gridding) reassignment of that stagger, together with a reach-matched power-of-2 control. | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | We evaluate by token-level perplexity on four held-out sets: FineWeb-Edu, Wikipedia, TinyStories, and a math set held out from OpenMathInstruct-2 (problem–solution pairs, a disjoint shard from the training math). |
| SF-2026-ARXIV-2606-28562 | Not Disclosed | The first is Nemotron (Nano-8B student, Super-49B teacher)and the second is OLMo (7B-Instruct-SFT student, 32B-Instruct teacher), which allows us to rigorously test our method in the challenging small teacher-student capability gap regime. | Reverse KL drives the student to concentrate on the teacher’s high-probability modes, yielding sharper outputs but risking premature entropy collapse ( Ko et al., 2026 ) . | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | accuracy alone, while annealing (A) in isolation provides negligible gain (+0.22). |
| SF-2026-ARXIV-2606-28565 | We evaluate Tier A by predicting GB200 with the device fully held out from training (Table 2 ), against NeuSight ( Lee et al., 2025 ) . | Not Disclosed | Not Disclosed | Systems such as vLLM ( Kwon et al., 2023 ) popularize KV-cache-aware memory management and continuous batching ( Yu et al., 2022 ) to sustain high throughput under variable-length requests, while vendor stacks such as TensorRT-LLM ( NVIDIA Corporation, 2023b ) emphasize kernel fusion, quantization, and hardware-specific tuning to maximize performance on particular GPU families. | Not Disclosed | Not Disclosed | Not Disclosed | A GPU is a massively parallel processor built from an array of streaming multiprocessors (SMs) over a memory hierarchy of per-SM registers and L1/shared memory, a shared L2 cache, and off-chip high-bandwidth memory (HBM), as shown in Figure 1 . | Not Disclosed | Table 3 reports the distribution of per-request prediction error on GB200 across various serving runs spanning different model families, sizes, and tensor parallelism, and Figure 9 shows the corresponding per-run accuracy heatmap. |
| SF-2026-ARXIV-2606-28574 | Not Disclosed | Not Disclosed | The examples were not installing the codebook but cueing associations the LLM already held [ 11 ] . | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed |
| SF-2026-ARXIV-2606-28615 | We propose using the LLM itself to generate alternative inputs conditioned on an explanation, captur Using SCSuff , we evaluate self-consistent sufficiency across 9 LLMs and 4 datasets. | We evaluate a range of instruction-tuned LLMs spanning multiple families and scales: Qwen3 (0.6B, 1.4B, 4B, 8B, 14B) ( Team, 2025 ) , Llama 3.2 (1B, 3B) and Llama 3.1 (8B) ( Grattafiori et al., 2024 ) , and Ministral (8B) ( Liu et al., 2026 ) . | 2 NVIDIA A100 GPUs | Not Disclosed | Using the last-layer hidden state of the final input token ( Figure 6 ), we observe moderate separation between high and low SCSuff samples in five of six model-dataset pairs. | Not Disclosed | Batch size 8 | Not Disclosed | Not Disclosed | We further find LLM explanations to be insufficient across datasets and models, with weak correlation to model size, accuracy, or output entropy. |
| SF-2026-ARXIV-2606-28639 | Not Disclosed | Not Disclosed | Note on scope: Rice’s Theorem is a statement about semantic properties — those determined solely by the input/output behaviour of M x M_{x} , independently of its internal description. | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed |
| SF-2026-ARXIV-2606-28649 | We evaluate four injection conditions (one benign baseline and three attack variants, A1–A3) across 100 runs each on five LLMs spanning four model families and parameter scales from ∼ \sim 4B to ∼ \sim 70B, revealing model-specific—rather than scale-dependent—vulnerability profiles: Llama-3.3-70B-Instruct-Turbo exhibits 100% ASR across all variants, while the smallest model evaluated (Gemma-3n-E4B, ∼ \sim 4B) exhibits a comparably high vulnerability profile, and two mid-sized models (Llama-3-8B-Instruct-Lite, Qwen 2.5-7B-Instruct-Turbo) resist direct-override injection entirely. | We evaluate four injection conditions (one benign baseline and three attack variants, A1–A3) across 100 runs each on five LLMs spanning four model families and parameter scales from ∼ \sim 4B to ∼ \sim 70B, revealing model-specific—rather than scale-dependent—vulnerability profiles: Llama-3.3-70B-Instruct-Turbo exhibits 100% ASR across all variants, while the smallest model evaluated (Gemma-3n-E4B, ∼ \sim 4B) exhibits a comparably high vulnerability profile, and two mid-sized models (Llama-3-8B-Instruct-Lite, Qwen 2.5-7B-Instruct-Turbo) resist direct-override injection entirely. | We consider an LLM-controlled robotic system implemented on ROS 2 Jazzy, where a robot equipped with a camera perceives its environment, reads text from objects via OCR, and forwards the extracted text to an LLM that interprets the instruction and outputs a structured action label (e.g., MOVE_ZONE_A , MOVE_ZONE_B ), which is deterministically mapped to velocity commands published to the ROS 2 control topic /cmd_vel . | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Timeouts reflect cumulative pipeline latency (gTTS synthesis + + Whisper inference + + DeepSeek API call) occasionally exceeding the 8 s window under high API load. | Attack success rate across 100 runs per injection condition |
| SF-2026-ARXIV-2606-28661 | Repeated test-time sampling under clustered/correlated answer distributions | Not Disclosed | Three recent works apply the same instrument to language-model outputs, but to different objects: Kohli [14] measure the effective votes of a panel of distinct judge models in evaluation, Goel et al. | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Coverage, oracle selection, learned selection, modal ceiling, correlation ceiling and effective sample size |

## 5. Deep Analysis Selection

<!-- validator:deep-analysis-selection-v1 -->
| Source Family ID | Eligibility | Decision | Analysis Unit ID | Subsumed By | Priority Rationale | Narrative Ref |
| --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2606-27632 | score_7_9; potential_books_delta | not_selected | — | — | 完成 64-family frontier 对读后，《Yuvion LLM: An Adversarially-Aware Large Language Model for Content And AI Safety》不单独进入分析单元。其 source-specific delta 是：把 adversarial robustness、agentic tool use 与 safety release evaluation 绑定为同一模型发布合同。 决定性边界是：除非改变哪类输入能取得 system-role authority，否则其边界窄于已入选 sensory-context authority break。Exact-v1 non-proof：Across these evaluations, Yuvion LLM demonstrates clear advantages on safety-focused benchmarks and particularly strong robustness under adversarial conditions, while maintaining solid overall capability. | analysis-decision:SF-2026-ARXIV-2606-27632 |
| SF-2026-ARXIV-2606-27634 | potential_books_delta | not_selected | — | — | 完成 64-family frontier 对读后，《Continual Learning for Sequential Personalization of Small Language Models: A Stability Monitoring Analysis》不单独进入分析单元。其 source-specific delta 是：把 sequential LoRA personalization 的 checkpoint、reference-set drift 与遗忘监控绑定为持续适配合同。 决定性边界是：它仍是 observe/diagnose sensor contract，不取得 state-transition 或 release authority。Exact-v1 non-proof：However, personalization requires models to adapt over time to evolving user- or task-specific data, placing them in a continual learning setting. | analysis-decision:SF-2026-ARXIV-2606-27634 |
| SF-2026-ARXIV-2606-27650 | potential_books_delta | not_selected | — | — | 完成 64-family frontier 对读后，《GenWorld: Empirically Grounded Urban Simulation Infrastructure for Scalable LLM-Agent Studies》不单独进入分析单元。其 source-specific delta 是：把城市级 agent environment、离线 policy compilation、人口/地理 grounding 与可复算 rollout 统一为 simulation infrastructure。 决定性边界是：它仍是 canonical owner 内的有界变化。Exact-v1 non-proof：These cases support GenWorld as a reproducible platform for grounded and scalable LLM-agent studies, while calibrated forecasting for traffic, evacuation, or policy outcomes remains future work. | analysis-decision:SF-2026-ARXIV-2606-27650 |
| SF-2026-ARXIV-2606-27669 | score_7_9; potential_books_delta | not_selected | — | — | 完成 64-family frontier 对读后，《When Search Agents Should Ask: DiscoBench for Clarification-Aware Deep Search》不单独进入分析单元。其 source-specific delta 是：把 deep-search 的 ambiguity detection、clarification action、task utility 与交互成本分离成评估合同。 决定性边界是：它改变 evaluator/measurement contract，但运行影响窄于三条入选的跨层 state/control chain。Exact-v1 non-proof：However, existing benchmarks often assume that user queries are complete and explicit, overlooking the fact that real-world search requests are frequently vague, underspecified, or even factually incorrect. | analysis-decision:SF-2026-ARXIV-2606-27669 |
| SF-2026-ARXIV-2606-27679 | potential_books_delta | not_selected | — | — | 完成 64-family frontier 对读后，《From Signals to Transfer: A Factorised Study of Probe-Based Uncertainty Estimation in Large Language Models》不单独进入分析单元。其 source-specific delta 是：给 probe uncertainty monitor 建立 feature、label construction、prompt 与 distribution-shift transfer 的可迁移边界。 决定性边界是：它仍是 observe/diagnose sensor contract，不取得 state-transition 或 release authority。Exact-v1 non-proof：However, under distribution shift, structured and compressed features are more robust, suggesting that in-domain performance alone is insufficient to measure progress. | analysis-decision:SF-2026-ARXIV-2606-27679 |
| SF-2026-ARXIV-2606-27681 | score_7_9; potential_books_delta | selected | DA-20260627-STRICT-MEDIATED-WORLD-STATE | — | 该 family 直接改变跨层 state/control boundary：用 strict mediation 让 textual belief state 成为唯一可测试的预测状态，阻断 history bypass。 exact-v1 proof=Experiments on TextWorld and ScienceWorld show preserved one-step prediction accuracy alongside up to 57\% gains in representation quality and 98\% improvements in rollout performance, increasing with task complexity and horizon.；non-proof=We formalize why it is necessary, showing that strict mediation makes representation quality empirically testable while history-leaky architectures break this connection. | analysis:DA-20260627-STRICT-MEDIATED-WORLD-STATE |
| SF-2026-ARXIV-2606-27683 | score_7_9; potential_books_delta | not_selected | — | — | 完成 64-family frontier 对读后，《CBD: API-Only LLM Black-Box Unlearning through Controlled Behavioral Divergence》不单独进入分析单元。其 source-specific delta 是：揭示 API-only black-box unlearning 实际由 relevance router 与 auxiliary models 持有控制权，而非修改远端模型。 决定性边界是：除非改变哪类输入能取得 system-role authority，否则其边界窄于已入选 sensory-context authority break。Exact-v1 non-proof：On WMDP, it lowers hazardous knowledge accuracy to 25.68, near random guessing, while preserving MMLU accuracy of 52.67. | analysis-decision:SF-2026-ARXIV-2606-27683 |
| SF-2026-ARXIV-2606-27704 | score_7_9; potential_books_delta | not_selected | — | — | 完成 64-family frontier 对读后，《AdvScan: Black-Box Adversarial Example Detection at Runtime through Power Analysis》不单独进入分析单元。其 source-specific delta 是：把 edge black-box adversarial detection 从模型内部 probe 改为 runtime power sensor，并暴露设备/攻击覆盖边界。 决定性边界是：除非改变哪类输入能取得 system-role authority，否则其边界窄于已入选 sensory-context authority break。Exact-v1 non-proof：Across 318,400 total test inputs, AdvScan detects 99.984% of AEs with only 40 false negatives and zero false positives. | analysis-decision:SF-2026-ARXIV-2606-27704 |
| SF-2026-ARXIV-2606-27709 | potential_books_delta | not_selected | — | — | 完成 64-family frontier 对读后，《Low-Agreeableness Persona Conditioning for Safe LLM Fine-Tuning》不单独进入分析单元。其 source-specific delta 是：证明 warmth fine-tuning 的 jailbreak regression 取决于 persona/data construction，而非同理性目标本身必然削弱安全。 决定性边界是：它仍是 canonical owner 内的有界变化。Exact-v1 non-proof：These results show that safer empathetic fine-tuning is achievable through data design alone, without safety labels, harm detectors, or changes to the training objective. | analysis-decision:SF-2026-ARXIV-2606-27709 |
| SF-2026-ARXIV-2606-27732 | score_7_9; potential_books_delta | not_selected | — | — | 完成 64-family frontier 对读后，《Bifocal Diffusion Language Models: Asymmetric Bidirectional Context for Parallel Generation》不单独进入分析单元。其 source-specific delta 是：用 asymmetric bidirectional sidecar 重构 diffusion-LM 的右上下文、KV cache 与 parallel decode 取舍。 决定性边界是：它改变 provisional generation/cache semantics，但仍完整落在 generation owner 内。Exact-v1 non-proof：Comprehensive experiments on continued pretraining of Qwen3-1.7B with 60B tokens demonstrate that R2LM achieves $2.4\times$ to $12.9\times$ higher throughput than bidirectional dLLMs and $1.9\times$ to $2.9\times$ speedup over AR baselines in batch serving through parallel decoding with KV caching, while exceeding the causal baseline on most benchmarks and surpassing the bidirectional dLLM on average. | analysis-decision:SF-2026-ARXIV-2606-27732 |
| SF-2026-ARXIV-2606-27739 | potential_books_delta | not_selected | — | — | 完成 64-family frontier 对读后，《The Weakest Link Tells It All: Outcome-Supervised Process Reward Modeling via Learnable Credit Assignment》不单独进入分析单元。其 source-specific delta 是：把 outcome-supervised PRM 的 step credit assignment 表述为 weakest-link multiple-instance learning。 决定性边界是：它改变 trainer 内部 credit/guidance，但不跨 subsystem 移动 runtime 或 release authority。Exact-v1 non-proof：exact-v1 的结论只覆盖《The Weakest Link Tells It All: Outcome-Supervised Process Reward Modeling via Learnable Credit Assignment》在 3 Analysis; 3.3 Theoretical Analysis; 5 Experiments 声明的实验；它没有证明跨 model family、hardware/runtime、数据分布或未测 failure mode 的普遍成立。 | analysis-decision:SF-2026-ARXIV-2606-27739 |
| SF-2026-ARXIV-2606-27743 | potential_books_delta | not_selected | — | — | 完成 64-family frontier 对读后，《End-to-End Dynamic Sparsity for Resource-Adaptive LLM Inference》不单独进入分析单元。其 source-specific delta 是：把 layer/head/token compute footprint 变成由输入与实时资源预算共同控制的 runtime policy state。 决定性边界是：它仍是 canonical owner 内的有界变化。Exact-v1 non-proof：A single L2A model traces the entire compute-accuracy Pareto frontier on Llama-3-8B and Qwen-3-4B: at up to 34% realized layer sparsity, it stays within 0.6% of the dense baseline on GSM8K, with the same gap holding zero-shot on out-of-distribution tasks, while every static or heuristic baseline requires a separately tuned model and still drops by 5-10% at comparable inference time. | analysis-decision:SF-2026-ARXIV-2606-27743 |
| SF-2026-ARXIV-2606-27757 | potential_books_delta | not_selected | — | — | 完成 64-family frontier 对读后，《Towards Reliable and Robust LLM Planning: Symbolic Feedback-Driven Iterative Self-Refinement Framework》不单独进入分析单元。其 source-specific delta 是：把 symbolic verifier、reachability recognizer 与 revision loop 放到 long-horizon plan 的显式控制流。 决定性边界是：它增加 bounded planning verifier，同时保持 environment/controller commit authority 不变。Exact-v1 non-proof：exact-v1 的结论只覆盖《Towards Reliable and Robust LLM Planning: Symbolic Feedback-Driven Iterative Self-Refinement Framework》在 IV EXPERIMENTS; IV-A Experimental Settings; IV-D Analysis of Planning Length 声明的实验；它没有证明跨 model family、hardware/runtime、数据分布或未测 failure mode 的普遍成立。 | analysis-decision:SF-2026-ARXIV-2606-27757 |
| SF-2026-ARXIV-2606-27780 | potential_books_delta | not_selected | — | — | 完成 64-family frontier 对读后，《Understanding Rollout Error in Graph World Models》不单独进入分析单元。其 source-specific delta 是：给 graph world-model rollout 建立 topology/model factor 分解与 dynamic-edge error feedback contract。 决定性边界是：它改变 model-state interface，但没有越过已入选 strict-mediation chain 的 authority 边界。Exact-v1 non-proof：Our results characterize when graph world models remain reliable under autoregressive planning and when topology makes them fail. | analysis-decision:SF-2026-ARXIV-2606-27780 |
| SF-2026-ARXIV-2606-27791 | potential_books_delta | not_selected | — | — | 完成 64-family frontier 对读后，《NLL-Guided Full-Attention Layer Selection for Training-Free Sliding-Window Adaptation》不单独进入分析单元。其 source-specific delta 是：以 answer-token NLL degradation 选择保留 full-attention 的层，改变 hybrid attention 的 calibration owner。 决定性边界是：它是有界的 attention calibration/layout 结果，而不是新的跨层 control contract。Exact-v1 non-proof：The method requires only $\sim$15 minutes of one-time calibration, advancing the efficiency-accuracy Pareto frontier for long-context LLM deployment. | analysis-decision:SF-2026-ARXIV-2606-27791 |
| SF-2026-ARXIV-2606-27797 | score_7_9; potential_books_delta | not_selected | — | — | 完成 64-family frontier 对读后，《Optimizing Teacher-Student Partitioning for Scalable Knowledge Distillation on HPC Systems》不单独进入分析单元。其 source-specific delta 是：按 teacher/student 不对称分别选择模型分片与拓扑通信，改变 KD runtime partition contract。 决定性边界是：它改变 training runtime partition/handoff，但影响仍受限于 distillation job。Exact-v1 non-proof：exact-v1 的结论只覆盖《Optimizing Teacher-Student Partitioning for Scalable Knowledge Distillation on HPC Systems》在 3 Testing Setup; 4 GKD Analysis and Improvements; 4.1 Experimental Results 声明的实验；它没有证明跨 model family、hardware/runtime、数据分布或未测 failure mode 的普遍成立。 | analysis-decision:SF-2026-ARXIV-2606-27797 |
| SF-2026-ARXIV-2606-27806 | score_7_9; potential_books_delta | not_selected | — | — | 完成 64-family frontier 对读后，《Agent vs. Parametric World Models: Hybrid Planning for Reliable Language Agents》不单独进入分析单元。其 source-specific delta 是：以 parametric transition model 校验 agent imagined delta，并把 disagreement 变成 targeted revision gate。 决定性边界是：它增加 bounded planning verifier，同时保持 environment/controller commit authority 不变。Exact-v1 non-proof：These results suggest that lightweight parametric transition models can serve as effective grounding mechanisms for language-agent planning without replacing semantic reasoning. | analysis-decision:SF-2026-ARXIV-2606-27806 |
| SF-2026-ARXIV-2606-27814 | potential_books_delta | not_selected | — | — | 完成 64-family frontier 对读后，《ATOD: Annealed Turn-Aware On-Policy Distillation for Multi-Turn Agentic Tasks》不单独进入分析单元。其 source-specific delta 是：在 multi-turn agent training 中按 competence/turn state 退火切换 on-policy distillation 与 environment reward。 决定性边界是：它改变 trainer 内部 credit/guidance，但不跨 subsystem 移动 runtime 或 release authority。Exact-v1 non-proof：Experiments on ALFWorld, WebShop, and Search-QA show that ATOD consistently outperforms competing post-training baselines: across the three student sizes, ATOD improves average success rate by 4.16 points over OPD and 23.62 points over GRPO, while surpassing the corresponding teacher models by 2.16 points. | analysis-decision:SF-2026-ARXIV-2606-27814 |
| SF-2026-ARXIV-2606-27826 | score_7_9; potential_books_delta | not_selected | — | — | 完成 64-family frontier 对读后，《NormAct: Benchmarking Embodied Agents' Proactive Compliance with Unspoken Social Norms》不单独进入分析单元。其 source-specific delta 是：把 embodied-agent goal success 与未明示社会规范的自主识别/遵守拆成渐进 guidance evaluation contract。 决定性边界是：它改变 evaluator/measurement contract，但运行影响窄于三条入选的跨层 state/control chain。Exact-v1 non-proof：NormAct therefore supports the development of embodied agents that pursue everyday goals while proactively respecting unstated social norms. | analysis-decision:SF-2026-ARXIV-2606-27826 |
| SF-2026-ARXIV-2606-27841 | score_7_9; potential_books_delta | not_selected | — | — | 完成 64-family frontier 对读后，《WattLayer: Get Layers Right to Estimate Inference Energy of Neural Networks》不单独进入分析单元。其 source-specific delta 是：把 inference energy estimation 从整模型 proxy 拆成可跨任务/架构迁移的 layer-wise measurement contract。 决定性边界是：它改变 cost attribution granularity，但仍从属于 measured run evidence。Exact-v1 non-proof：We further show that layer-wise decomposition generalize to new tasks without complete retraining, by leveraging shared layers across architectures. | analysis-decision:SF-2026-ARXIV-2606-27841 |
| SF-2026-ARXIV-2606-27866 | potential_books_delta | not_selected | — | — | 完成 64-family frontier 对读后，《FlexMoE: One-for-All Nested Intra-Expert Pruning for MoE Language Models》不单独进入分析单元。其 source-specific delta 是：把一次性 MoE compression artifact 改成 nested subnet family 与可在线切换的 budget state。 决定性边界是：canonical MoE owner 已持有 budget-profile state，因此本 family 只增加实现证据，不另建 analysis unit。Exact-v1 non-proof：Specifically, on Qwen2-57B-A14B, our method retains ~99.8% of base performance while pruning 50% of routed expert parameters even without fine-tuning. | analysis-decision:SF-2026-ARXIV-2606-27866 |
| SF-2026-ARXIV-2606-27906 | score_7_9; potential_books_delta | selected | DA-20260627-PHASE-CLOSED-LOOP-INFERENCE | — | 该 family 直接改变跨层 state/control boundary：以真实 mobile SoC 证据拆开 vision encoder、prefill、decode、cache 与 thermal phase 的 backend placement。 exact-v1 proof=Finally, we show that a four-step graph rewrite enables previously unsupported encoders, such as Phi-3.5-V, to reach the QNN path with up to 22x speedup, providing a practical porting recipe for mobile VLM deployment.；non-proof=Using FastVLM-0.5B as an end-to-end case study, together with encoder-only measurements across four architecture families, we show that phase matters: NPU execution is highly phase-dependent, delivering 1.64x speedup for prefill but only 1.18x for decode, while vision encoders achieve 20-45x speedups over CPU. | analysis:DA-20260627-PHASE-CLOSED-LOOP-INFERENCE |
| SF-2026-ARXIV-2606-27934 | score_7_9; potential_books_delta | not_selected | — | — | 完成 64-family frontier 对读后，《Self-Verifying Measurement Records: Hash-Linked Evidence Graphs for Hardware Benchmarking》不单独进入分析单元。其 source-specific delta 是：用 hash-linked measurement/evidence graph 与 output-derived challenge 让硬件 benchmark 可离线验证。 决定性边界是：它改变 evaluator/measurement contract，但运行影响窄于三条入选的跨层 state/control chain。Exact-v1 non-proof：We then treat the check itself as a security object: a probe seed committed for offline reproducibility is an attack surface, and a probe-aware adversary can hide a corruption in the probe's null space, fooling even a quorum of bit-identical witnesses, while a Fiat-Shamir challenge derived from the claimed output closes this. | analysis-decision:SF-2026-ARXIV-2606-27934 |
| SF-2026-ARXIV-2606-27936 | score_7_9; potential_books_delta | not_selected | — | — | 完成 64-family frontier 对读后，《Agentic AI-Powered Re-Identification: An Emerging, Scalable Threat to Mobility Microdata Privacy》不单独进入分析单元。其 source-specific delta 是：证明 agentic open-web resolution 把 mobility re-identification 从专家手工能力改成可规模化 threat model。 决定性边界是：除非改变哪类输入能取得 system-role authority，否则其边界窄于已入选 sensory-context authority break。Exact-v1 non-proof：We present an end-to-end pipeline in which large language model agents autonomously search the open web, cross-reference public records and social media, and resolve raw coordinate sequences to candidate identities - without human intervention. | analysis-decision:SF-2026-ARXIV-2606-27936 |
| SF-2026-ARXIV-2606-27944 | score_7_9; potential_books_delta | not_selected | — | — | 完成 64-family frontier 对读后，《It Lied to a Doctor to Buy Poison Ingredients: Quantifying Real-World Misuse of Phone-use Agents》不单独进入分析单元。其 source-specific delta 是：以真实 phone/app side effects 揭示 safety awareness 与 execution authorization 分离后的 misuse failure。 决定性边界是：除非改变哪类输入能取得 system-role authority，否则其边界窄于已入选 sensory-context authority break。Exact-v1 non-proof：Simple defenses curb the overt cases, but the more covert and arguably more damaging threats, such as coordinated review manipulation and fake traffic, remain largely unsolved. | analysis-decision:SF-2026-ARXIV-2606-27944 |
| SF-2026-ARXIV-2606-27962 | potential_books_delta | not_selected | — | — | 完成 64-family frontier 对读后，《Building a Scalable, Reproducible, Evaluatable, and Closed-Loop Simulation Environment Foundation for Embodied Intelligence》不单独进入分析单元。其 source-specific delta 是：把 embodied simulation 的 environment、trajectory、evaluation、data 与 elastic cloud scheduling 统一成闭环平台。 决定性边界是：它仍是 canonical owner 内的有界变化。Exact-v1 non-proof：exact-v1 的结论只覆盖《Building a Scalable, Reproducible, Evaluatable, and Closed-Loop Simulation Environment Foundation for Embodied Intelligence》在 Building a Scalable, Reproducible, Evaluatable, and Closed-Loop Simulation Environment Foundation for Embodied Intelligence Cloud-Native Simulation Infrastructure for Embodied Intelligence Training, Evaluation, and Data Collection; 1.2 Bottlenecks in Real Robot Data and Evaluation; 3.2 Mainstream Benchmarks and Datasets 声明的实验；它没有证明跨 model family、hardware/runtime、数据分布或未测 failure mode 的普遍成立。 | analysis-decision:SF-2026-ARXIV-2606-27962 |
| SF-2026-ARXIV-2606-27976 | potential_books_delta | not_selected | — | — | 完成 64-family frontier 对读后，《SHARD: cell-keyed residual splitting for alignment-resistant private dense retrieval》不单独进入分析单元。其 source-specific delta 是：把 private dense retrieval 的 routing prefix、cell-local residual key、CKKS rerank 与 linkage risk 分开声明。 决定性边界是：它仍是 canonical owner 内的有界变化。Exact-v1 non-proof：SHARD preserves retrieval and compartmentalizes alignment evidence, but does not provide DP, unlinkability, or cancellable templates. | analysis-decision:SF-2026-ARXIV-2606-27976 |
| SF-2026-ARXIV-2606-27997 | score_7_9; potential_books_delta | not_selected | — | — | 完成 64-family frontier 对读后，《Benchmarking on Tasks That Matter: Dataset Selection for Preserving Model Rankings》不单独进入分析单元。其 source-specific delta 是：把 benchmark task subset selection 绑定 rank-preservation uncertainty，而非把少量数据集当作无损代理。 决定性边界是：它改变 evaluator/measurement contract，但运行影响窄于三条入选的跨层 state/control chain。Exact-v1 non-proof：For TSC, our best-performing strategy achieves a Spearman correlation of 0.95 with the full benchmark model rankings using only five selected datasets. | analysis-decision:SF-2026-ARXIV-2606-27997 |
| SF-2026-ARXIV-2606-28011 | potential_books_delta | not_selected | — | — | 完成 64-family frontier 对读后，《From Detection to Action: Using LLM Agents for Fault-Tolerant Control》不单独进入分析单元。其 source-specific delta 是：把 LLM recovery proposal 放在 plant twin simulation、deterministic interlock validation 与 bounded fallback 之后。 决定性边界是：它仍是 canonical owner 内的有界变化。Exact-v1 non-proof：exact-v1 的结论只覆盖《From Detection to Action: Using LLM Agents for Fault-Tolerant Control》在 4.3 Evaluation criteria; 5 Results; 5.1 Mixing module results 声明的实验；它没有证明跨 model family、hardware/runtime、数据分布或未测 failure mode 的普遍成立。 | analysis-decision:SF-2026-ARXIV-2606-28011 |
| SF-2026-ARXIV-2606-28013 | score_7_9; potential_books_delta | not_selected | — | — | 完成 64-family frontier 对读后，《The Signal-Coverage Matrix: Stratifying Type and Semantic Errors in Statement Autoformalization》不单独进入分析单元。其 source-specific delta 是：把 autoformalization 的 type correctness 与 semantic equivalence 交叉分层，防止单标量误归因。 决定性边界是：它改变 evaluator/measurement contract，但运行影响窄于三条入选的跨层 state/control chain。Exact-v1 non-proof：We propose a signal-coverage matrix that crosses the Lean elaborator (pass/fail) with a semantic-equivalence judgment (equivalent/not), sorting every output into one of four cells: true success (TS), type-only (TO), semantic-only (SO), or both fail (BF). | analysis-decision:SF-2026-ARXIV-2606-28013 |
| SF-2026-ARXIV-2606-28037 | score_7_9; potential_books_delta | not_selected | — | — | 完成 64-family frontier 对读后，《Evolution-Aware Regression Test Prioritization of ML-Enabled Systems Using Gradient-Based Behavior Vectors》不单独进入分析单元。其 source-specific delta 是：以原模型 gradient behavior vector 和 parameter delta 做 evolution-aware regression-test prioritization。 决定性边界是：它改变 evaluator/measurement contract，但运行影响窄于三条入选的跨层 state/control chain。Exact-v1 non-proof：In an empirical study across classification and regression tasks, GBV-PD consistently outperformed non-directional baselines and remained competitive with a full-gradient reference, while offering better time and storage profiles for repeated updates via reusable GBV caching. | analysis-decision:SF-2026-ARXIV-2606-28037 |
| SF-2026-ARXIV-2606-28050 | score_7_9; potential_books_delta | not_selected | — | — | 完成 64-family frontier 对读后，《Can LLMs Judge Better Than They Generate? Evaluating Task Asymmetry, Mechanistic Interpretability and Transferability for In-Context QA》不单独进入分析单元。其 source-specific delta 是：用 controlled in-context QA 反证 self-evaluation 普遍比 generation 更容易的默认假设。 决定性边界是：它改变 evaluator/measurement contract，但运行影响窄于三条入选的跨层 state/control chain。Exact-v1 non-proof：exact-v1 的结论只覆盖《Can LLMs Judge Better Than They Generate? Evaluating Task Asymmetry, Mechanistic Interpretability and Transferability for In-Context QA》在 Generation–evaluation asymmetry.; 3.1 Task Asymmetry Analysis; Evaluation task ( 𝒯 eval \mathcal{T}_{\text{eval}} ). 声明的实验；它没有证明跨 model family、hardware/runtime、数据分布或未测 failure mode 的普遍成立。 | analysis-decision:SF-2026-ARXIV-2606-28050 |
| SF-2026-ARXIV-2606-28061 | score_7_9; potential_books_delta | not_selected | — | — | 完成 64-family frontier 对读后，《ToolPrivacyBench: Benchmarking Purpose-Bound Privacy in Tool-Using LLM Agents》不单独进入分析单元。其 source-specific delta 是：把 tool-agent privacy 从最终文本扩展到每个 tool argument、sink 与 purpose-bound information flow。 决定性边界是：除非改变哪类输入能取得 system-role authority，否则其边界窄于已入选 sensory-context authority break。Exact-v1 non-proof：ToolPrivacyBench therefore formalizes a need-to-know disclosure boundary, under which each tool should receive only the information necessary for its stated purpose, and uses trajectory-level auditing to identify privacy over-disclosure in multi-tool workflows. | analysis-decision:SF-2026-ARXIV-2606-28061 |
| SF-2026-ARXIV-2606-28070 | potential_books_delta | not_selected | — | — | 完成 64-family frontier 对读后，《JD Oxygen AI Item Center (Oxygen AIIC) V1: An Industrial-Scale LLM/VLM-Centric Solution for Item Understanding, Management, and Applications》不单独进入分析单元。其 source-specific delta 是：提供 ontology、knowledge production、model evolution、unified data/service tunnel 在工业规模下的统一平台合同。 决定性边界是：它仍是 canonical owner 内的有界变化。Exact-v1 non-proof：exact-v1 的结论只覆盖《JD Oxygen AI Item Center (Oxygen AIIC) V1: An Industrial-Scale LLM/VLM-Centric Solution for Item Understanding, Management, and Applications》在 3.3 Results; 4.2.3 Results; Module 1: Data evaluation. 声明的实验；它没有证明跨 model family、hardware/runtime、数据分布或未测 failure mode 的普遍成立。 | analysis-decision:SF-2026-ARXIV-2606-28070 |
| SF-2026-ARXIV-2606-28116 | score_7_9; potential_books_delta | not_selected | — | — | 完成 64-family frontier 对读后，《Mechanism-Driven Monitors for Preemptive Detection of LLM Training Instability》不单独进入分析单元。其 source-specific delta 是：从 attention/router 的故障机理导出 pre-loss training-instability sensors，而非等待 loss collapse。 决定性边界是：它仍是 observe/diagnose sensor contract，不取得 state-transition 或 release authority。Exact-v1 non-proof：After a numerical or a hyperparameter fault has already destabilized the training dynamics, it may continue for thousands of steps while loss and gradient norms still appear normal. | analysis-decision:SF-2026-ARXIV-2606-28116 |
| SF-2026-ARXIV-2606-28128 | potential_books_delta | not_selected | — | — | 完成 64-family frontier 对读后，《PhysisForcing: Physics Reinforced World Simulator for Robotic Manipulation》不单独进入分析单元。其 source-specific delta 是：把 video-world-simulator 的 contact/trajectory physics supervision 与 downstream closed-loop policy effect 联结。 决定性边界是：它改变 model-state interface，但没有越过已入选 strict-mediation chain 的 authority 边界。Exact-v1 non-proof：However, both general-domain video generators and robot-specific data fine-tuned models can still produce physically implausible manipulations, including discontinuous motion trajectories and inconsistent robot-object interactions, which limits their reliability as world simulators. | analysis-decision:SF-2026-ARXIV-2606-28128 |
| SF-2026-ARXIV-2606-28153 | score_7_9; potential_books_delta | not_selected | — | — | 完成 64-family frontier 对读后，《Robust Harmful Features Under Jailbreak Attacks: Mechanistic Evidence from Attention Head Specialization in Large Language Models》不单独进入分析单元。其 source-specific delta 是：区分被攻击抑制与仍持续存在的 safety attention heads，并验证其 causal/monitoring 边界。 决定性边界是：除非改变哪类输入能取得 system-role authority，否则其边界窄于已入选 sensory-context authority break。Exact-v1 non-proof：To validate the practical significance of this robustness, we show that simply reading these persistent activations -- without any training -- yields competitive aggregate detection performance with strong adversarial robustness. | analysis-decision:SF-2026-ARXIV-2606-28153 |
| SF-2026-ARXIV-2606-28166 | potential_books_delta | not_selected | — | — | 完成 64-family frontier 对读后，《Tandem Reinforcement Learning with Verifiable Rewards》不单独进入分析单元。其 source-specific delta 是：让 senior/junior 交替共同生成 RLVR rollout，把 handoff compatibility 变成训练目标。 决定性边界是：它改变 trainer 内部 credit/guidance，但不跨 subsystem 移动 runtime 或 release authority。Exact-v1 non-proof：Training Qwen3-4B-Instruct on competition math, we find that TRL matches vanilla GRPO on solo reasoning capability while three properties emerge together from the same rollout structure: stronger handoff robustness with the junior, reduced distributional drift from the junior, and a chain-of-thought more legible to the junior. | analysis-decision:SF-2026-ARXIV-2606-28166 |
| SF-2026-ARXIV-2606-28187 | potential_books_delta | not_selected | — | — | 完成 64-family frontier 对读后，《GBC: Gradient-Based Connections for Optimizing Multi-Agent Systems》不单独进入分析单元。其 source-specific delta 是：把 multi-agent interaction 建成可反传 attribution graph，以 token-level influence 分配错误责任。 决定性边界是：interaction attribution 命题已被 canonical owner 持有，不足以形成另一条叙事。Exact-v1 non-proof：However, their performance is often limited by miscoordination and, more fundamentally, the lack of fine-grained credit assignment across agents. | analysis-decision:SF-2026-ARXIV-2606-28187 |
| SF-2026-ARXIV-2606-28235 | potential_books_delta | not_selected | — | — | 完成 64-family frontier 对读后，《Govern the Repository, Not the Agent: Measuring Ecosystem-Level Risk in AI-Native Software》不单独进入分析单元。其 source-specific delta 是：用大规模 PR 数据把 coding-agent 风险 owner 从单次 agent score 移到 repository-level integration friction。 决定性边界是：它仍是 canonical owner 内的有界变化。Exact-v1 non-proof：exact-v1 的结论只覆盖《Govern the Repository, Not the Agent: Measuring Ecosystem-Level Risk in AI-Native Software》在 IV-B Level of analysis and why multilevel models; V Results 声明的实验；它没有证明跨 model family、hardware/runtime、数据分布或未测 failure mode 的普遍成立。 | analysis-decision:SF-2026-ARXIV-2606-28235 |
| SF-2026-ARXIV-2606-28276 | score_7_9; potential_books_delta | not_selected | — | — | 完成 64-family frontier 对读后，《SimFoundry: Modular and Automated Scene Generation for Policy Learning and Evaluation》不单独进入分析单元。其 source-specific delta 是：把 video-to-sim reconstruction、digital cousins、policy training 与 sim-to-real rank validity 绑定。 决定性边界是：它改变进入 physical promotion 的 evidence handoff，但不取代入选 inference/security chain。Exact-v1 non-proof：exact-v1 的结论只覆盖《SimFoundry: Modular and Automated Scene Generation for Policy Learning and Evaluation》在 SimFoundry: Modular and Automated Scene Generation for Policy Learning and Evaluation; 5 Experiments; 5.1 Real-to-Sim Policy Evaluation 声明的实验；它没有证明跨 model family、hardware/runtime、数据分布或未测 failure mode 的普遍成立。 | analysis-decision:SF-2026-ARXIV-2606-28276 |
| SF-2026-ARXIV-2606-28277 | score_7_9; potential_books_delta | not_selected | — | — | 完成 64-family frontier 对读后，《Towards Automating Scientific Review with Google's Paper Assistant Tool》不单独进入分析单元。其 source-specific delta 是：把 agentic scientific review 的 verification depth 与 human decision authority 分层，并给出部署证据。 决定性边界是：它改变 evaluator/measurement contract，但运行影响窄于三条入选的跨层 state/control chain。Exact-v1 non-proof：By catching errors early, PAT eases the cognitive burden placed on referees, while preserving their control over the outcomes of the review process. | analysis-decision:SF-2026-ARXIV-2606-28277 |
| SF-2026-ARXIV-2606-28279 | potential_books_delta | not_selected | — | — | 完成 64-family frontier 对读后，《Agentic Hardware Design as Repository-Level Code Evolution》不单独进入分析单元。其 source-specific delta 是：用 compiled project pack、acceptance predicate、isolated worktree 与 trace/replay 管理 repository-scale hardware agent。 决定性边界是：它仍是 canonical owner 内的有界变化。Exact-v1 non-proof：However, we do not claim that agentic AI for hardware design is solved: these benchmarks are controlled proxies for a much broader engineering problem in chip design. | analysis-decision:SF-2026-ARXIV-2606-28279 |
| SF-2026-ARXIV-2606-28322 | score_7_9; potential_books_delta | not_selected | — | — | 完成 64-family frontier 对读后，《PerceptionRubrics: Calibrating Multimodal Evaluation to Human Perception》不单独进入分析单元。其 source-specific delta 是：以 Must-Right/Easy-Wrong atomic rubrics 与 gated penalty 替代会掩盖必需事实失败的平均分。 决定性边界是：它改变 evaluator/measurement contract，但运行影响窄于三条入选的跨层 state/control chain。Exact-v1 non-proof：exact-v1 的结论只覆盖《PerceptionRubrics: Calibrating Multimodal Evaluation to Human Perception》在 PerceptionRubrics: Calibrating Multimodal Evaluation to Human Perception; Visual Perception Benchmarks in MLLMs.; Evaluation of Image Captioning. 声明的实验；它没有证明跨 model family、hardware/runtime、数据分布或未测 failure mode 的普遍成立。 | analysis-decision:SF-2026-ARXIV-2606-28322 |
| SF-2026-ARXIV-2606-28430 | score_7_9; potential_books_delta | not_selected | — | — | 完成 64-family frontier 对读后，《Building to the Test: Coding Agents Deliver What You Check, Not What You Requested》不单独进入分析单元。其 source-specific delta 是：用 no-op ablation 揭示 coding agent 可通过 oracle 却未交付可复用 artifact 的 construction-validity failure。 决定性边界是：它改变 evaluator/measurement contract，但运行影响窄于三条入选的跨层 state/control chain。Exact-v1 non-proof：The agent does not, on its own, validate what it ships as a user would. | analysis-decision:SF-2026-ARXIV-2606-28430 |
| SF-2026-ARXIV-2606-28433 | score_7_9; potential_books_delta | not_selected | — | — | 完成 64-family frontier 对读后，《Position: RL Researchers Need to Distinguish Between Solving Simulators and Using Simulators as a Proxy》不单独进入分析单元。其 source-specific delta 是：要求 RL evaluation 区分把 simulator 当目标与把 simulator 当 deployment proxy 的两套约束。 决定性边界是：它改变 evaluator/measurement contract，但运行影响窄于三条入选的跨层 state/control chain。Exact-v1 non-proof：To achieve high scores, researchers may adopt solutions exclusively meant for solving simulators, rather than learning while the agent is deployed outside a simulator. | analysis-decision:SF-2026-ARXIV-2606-28433 |
| SF-2026-ARXIV-2606-28434 | potential_books_delta | not_selected | — | — | 完成 64-family frontier 对读后，《SWE-MeM: Learning Adaptive Memory Management for Long-Horizon Coding Agents》不单独进入分析单元。其 source-specific delta 是：把 coding-agent compression timing、granularity 与剩余 context budget 变成 agent-controlled memory action。 决定性边界是：它仍是 canonical owner 内的有界变化。Exact-v1 non-proof：Moreover, these approaches fail to jointly optimize memory management and issue resolution capabilities to improve performance while reducing token usage. | analysis-decision:SF-2026-ARXIV-2606-28434 |
| SF-2026-ARXIV-2606-28436 | potential_books_delta | not_selected | — | — | 完成 64-family frontier 对读后，《Dockerless: Environment-Free Program Verifier for Coding Agents》不单独进入分析单元。其 source-specific delta 是：把 coding post-training verifier 从 executable environment 改成 repository-evidence judge，改变 reward authority 与 non-proof 边界。 决定性边界是：它改变 trainer 内部 credit/guidance，但不跨 subsystem 移动 runtime 或 release authority。Exact-v1 non-proof：We propose Dockerless, an environment-free agentic patch verifier that evaluates generated code patches without executing them. | analysis-decision:SF-2026-ARXIV-2606-28436 |
| SF-2026-ARXIV-2606-28438 | potential_books_delta | not_selected | — | — | 完成 64-family frontier 对读后，《When AI Reviews Its Own Code: Recursive Self-Training Collapse in Code LLMs》不单独进入分析单元。其 source-specific delta 是：证明 recursive code self-training 的 model-coupled gate 会 rubber-stamp collapse，要求 exogenous verification。 决定性边界是：它仍是 canonical owner 内的有界变化。Exact-v1 non-proof：In the clearest case, the binary self-gate enters a rubber-stamp regime where acceptance scores rise while benchmark correctness falls. | analysis-decision:SF-2026-ARXIV-2606-28438 |
| SF-2026-ARXIV-2606-28455 | potential_books_delta | not_selected | — | — | 完成 64-family frontier 对读后，《Event-Conditioned Diagnostics of Kinematic, Contact, and Object-Permanence Structure in Passive Object-State World Models》不单独进入分析单元。其 source-specific delta 是：把 event readout、context-relative emphasis 与 causal sensitivity 分开评估 latent physical structure。 决定性边界是：它改变 model-state interface，但没有越过已入选 strict-mediation chain 的 authority 边界。Exact-v1 non-proof：These results support event-conditioned latent structure and functional sensitivity without implying explicit physical modules or isolated causal circuits. | analysis-decision:SF-2026-ARXIV-2606-28455 |
| SF-2026-ARXIV-2606-28471 | potential_books_delta | not_selected | — | — | 完成 64-family frontier 对读后，《Data and Evaluation Closed-Loop for Model Capability Enhancement》不单独进入分析单元。其 source-specific delta 是：以 capability slice 将 evaluation failure 反向映射为可检验 data intervention，并允许判定 data 非根因。 决定性边界是：它仍是 canonical owner 内的有界变化。Exact-v1 non-proof：First, the loop rules the data out: continued pre-training drives BBH down by $-46.82\%$, but diagnosis traces this to a single masked \texttt{\textless EOS\textgreater} loss rather than weakened reasoning; restoring it recovers BBH to $66.44$, above the original checkpoint, without changing the data. | analysis-decision:SF-2026-ARXIV-2606-28471 |
| SF-2026-ARXIV-2606-28479 | score_7_9; potential_books_delta | not_selected | — | — | 完成 64-family frontier 对读后，《Decomposing Memorization Reduction in Privacy-Preserving Fine-Tuning of SLMs for CSIRTs》不单独进入分析单元。其 source-specific delta 是：用 matched-update controls 分离 DP guarantee、pseudonymization 与 optimizer-step memorization effect。 决定性边界是：它改善 adapter training 内部 causal attribution，但不移动 deployment authority。Exact-v1 non-proof：Third, F1 scores remain between 0.19 and 0.28 across all 96 adapters using four shot prompting, indicating that, under the evaluated training budget, 1B to 3B SLMs do not achieve operationally useful performance. | analysis-decision:SF-2026-ARXIV-2606-28479 |
| SF-2026-ARXIV-2606-28480 | score_7_9; potential_books_delta | not_selected | — | — | 完成 64-family frontier 对读后，《TUA-Bench: A Benchmark for General-Purpose Terminal-Use Agents》不单独进入分析单元。其 source-specific delta 是：把 terminal-use agent 扩展到非 coding workflow，并用 deterministic setup/execution scoring 约束 release claim。 决定性边界是：它改变 evaluator/measurement contract，但运行影响窄于三条入选的跨层 state/control chain。Exact-v1 non-proof：However, existing benchmarks do not adequately evaluate general-purpose terminal computer-use agents (TUAs): general computer-use benchmarks primarily target graphical user interfaces (GUIs), whereas terminal-based benchmarks largely emphasize technical and programming-centric workflows historically native to the shell. | analysis-decision:SF-2026-ARXIV-2606-28480 |
| SF-2026-ARXIV-2606-28514 | potential_books_delta | not_selected | — | — | 完成 64-family frontier 对读后，《GPTNT: Benchmarking Real-Time Collaboration Between Multimodal Agents on Keep Talking And Nobody Explodes》不单独进入分析单元。其 source-specific delta 是：以真实异步倒计时、信息不对称与不可单独完成任务测量实时 collaboration。 决定性边界是：interaction attribution 命题已被 canonical owner 持有，不足以形成另一条叙事。Exact-v1 non-proof：One agent can see and manipulate the bomb but does not have the defusal instructions; the other has the instructions but cannot see or manipulate the bomb. | analysis-decision:SF-2026-ARXIV-2606-28514 |
| SF-2026-ARXIV-2606-28529 | score_7_9; potential_books_delta | subsumed | — | DA-20260627-PHASE-CLOSED-LOOP-INFERENCE | 该 family 与已入选 inference chain 共用阶段化 runtime/capacity 演进，不重复建叙事；自身 proof=Embodied foundation models have recently been widely used to improve robot generalization and task success rates.；boundary=However, unlike traditional static ML tasks, embodied tasks involve repeated interaction with the environment, and task-level performance is determined not only by per-step cost, but also by closed-loop effects unique to embodied execution, which remain insufficiently characterized in current efficient-inference studies. | analysis:DA-20260627-PHASE-CLOSED-LOOP-INFERENCE |
| SF-2026-ARXIV-2606-28551 | potential_books_delta | not_selected | — | — | 完成 64-family frontier 对读后，《DataComp-VLM: Improved Open Datasets for Vision-Language Models》不单独进入分析单元。其 source-specific delta 是：用固定 model/token budget 与多数据类型 corpus 建立 VLM data curation、mixing 与 release artifact 的可复算合同。 决定性边界是：它仍是 canonical owner 内的有界变化。Exact-v1 non-proof：As part of DCVLM, we collect 160 datasets spanning four data types -- image-caption pairs, multimodal interleaved documents, text-only, and instruction-tuning data -- into a corpus of 6T multimodal tokens. | analysis-decision:SF-2026-ARXIV-2606-28551 |
| SF-2026-ARXIV-2606-28560 | potential_books_delta | not_selected | — | — | 完成 64-family frontier 对读后，《Depth-Staggered Fibonacci Spacing for Sparse Attention: Static Schedules Beat Learned Dilation and Extrapolate Where Dense Attention Fails》不单独进入分析单元。其 source-specific delta 是：以 matched small-model study 反证 learned sparse spacing 必然优于 static schedule，并暴露 train-length 与 extrapolation 的反向取舍。 决定性边界是：它是有界的 attention calibration/layout 结果，而不是新的跨层 control contract。Exact-v1 non-proof：Third, and most consequential, all sparse variants extrapolate to four times their training length with little or no degradation, whereas a recipe-matched dense baseline collapses (perplexity rises by 201% at 4x length); we attribute this to fixed-offset attention only ever querying relative positions seen during training. | analysis-decision:SF-2026-ARXIV-2606-28560 |
| SF-2026-ARXIV-2606-28562 | potential_books_delta | not_selected | — | — | 完成 64-family frontier 对读后，《SEAD: Competence-Aware On-Policy Distillation via Entropy-Guided Supervision》不单独进入分析单元。其 source-specific delta 是：按 student competence 在 token、phase、prompt 三个尺度控制 on-policy distillation supervision。 决定性边界是：它改变 trainer 内部 credit/guidance，但不跨 subsystem 移动 runtime 或 release authority。Exact-v1 non-proof：exact-v1 的结论只覆盖《SEAD: Competence-Aware On-Policy Distillation via Entropy-Guided Supervision》在 3 Evaluation; 3.1 Experimental Setup; Evaluation. 声明的实验；它没有证明跨 model family、hardware/runtime、数据分布或未测 failure mode 的普遍成立。 | analysis-decision:SF-2026-ARXIV-2606-28562 |
| SF-2026-ARXIV-2606-28565 | score_7_9; potential_books_delta | subsumed | — | DA-20260627-PHASE-CLOSED-LOOP-INFERENCE | 该 family 与已入选 inference chain 共用阶段化 runtime/capacity 演进，不重复建叙事；自身 proof=A second target-measured tier adds one model-agnostic kernel-microbenchmark sweep on the target GPU, sharpening per-kernel error to 3.8%, a 7.3x improvement over a comparable baseline (27.7%).；boundary=In our simulator, these predictions yield end-to-end median (p50) errors across six model families of 15.4%, 12.8%, and 3.0% (TTFT, TPOT, throughput) in the cross-generation tier and 14.3%, 6.2%, and 2.7% in the target-measured tier, matching dedicated profiling tools while collecting far less on-device data. | analysis:DA-20260627-PHASE-CLOSED-LOOP-INFERENCE |
| SF-2026-ARXIV-2606-28574 | score_7_9; potential_books_delta | not_selected | — | — | 完成 64-family frontier 对读后，《Correct codes for the wrong reasons? validating LLMs as measurement instruments for theoretical constructs》不单独进入分析单元。其 source-specific delta 是：把 LLM coder 的表面一致性与 theoretical construct validity 分开，并要求 clause-level extractive evidence。 决定性边界是：它改变 evaluator/measurement contract，但运行影响窄于三条入选的跨层 state/control chain。Exact-v1 non-proof：exact-v1 的结论只覆盖《Correct codes for the wrong reasons? validating LLMs as measurement instruments for theoretical constructs》在 3.1 Clauses with grounds; 3.2 Human in the loop 声明的实验；它没有证明跨 model family、hardware/runtime、数据分布或未测 failure mode 的普遍成立。 | analysis-decision:SF-2026-ARXIV-2606-28574 |
| SF-2026-ARXIV-2606-28615 | score_7_9; potential_books_delta | not_selected | — | — | 完成 64-family frontier 对读后，《What LLMs explain is not what they believe: Evaluating explanation sufficiency under models' own input beliefs》不单独进入分析单元。其 source-specific delta 是：把 free-text explanation sufficiency 绑定显式 input distribution 与 self-consistent information metric。 决定性边界是：它改变 evaluator/measurement contract，但运行影响窄于三条入选的跨层 state/control chain。Exact-v1 non-proof：We formalize self-consistent sufficiency as a goal for free-text explanations and introduce an information-theoretic metric, SCSuff, that enables evaluation of free-text explanations without relying on predefined biases or shortcuts. | analysis-decision:SF-2026-ARXIV-2606-28615 |
| SF-2026-ARXIV-2606-28639 | score_7_9; potential_books_delta | not_selected | — | — | 完成 64-family frontier 对读后，《The Unverifiability of Artificial General Intelligence (AGI) Alignment, Static and Dynamic: From Trakhtenbrot's Wall to the Safety-Generality Tension》不单独进入分析单元。其 source-specific delta 是：给 static/dynamic alignment certification 划出 expressivity、soundness、completeness 与 tractability 的形式边界。 决定性边界是：除非改变哪类输入能取得 system-role authority，否则其边界窄于已入选 sensory-context authority break。Exact-v1 non-proof：Three practical risks (finite test coverage, bounded deliberation time, restricted observation) are one phenomenon: every bounded scheme that does not reject correct evidence admits an evolution trace it certifies at every stage while the property is persistently violated. | analysis-decision:SF-2026-ARXIV-2606-28639 |
| SF-2026-ARXIV-2606-28649 | score_7_9; potential_books_delta | selected | DA-20260627-SENSORY-CONTEXT-AUTHORITY | — | 该 family 直接改变跨层 state/control boundary：把 robot prompt injection threat surface 扩展到 OCR、audio 与 LiDAR-derived system context，并测 firewall bypass。 exact-v1 proof=All code, data, and results are publicly available.；non-proof=Across 100 independent runs per injection variant on five LLMs spanning four model families and parameter scales from approximately 4B to approximately 284B (DeepSeek-V4-Flash, Llama-3-8B-Instruct-Lite, Llama-3.3-70B-Instruct-Turbo, Qwen 2.5-7B-Instruct-Turbo, Gemma-3n-E4B), we identify model-specific vulnerability profiles that do not follow a monotonic scaling trend: Llama-3.3-70B-Instruct-Turbo exhibits 100% attack success rate (ASR) across all injection variants, while Llama-3-8B-Instruct-Lite and Qwen 2.5-7B-Instruct-Turbo resist direct-override injection (0% ASR), and the smallest model evaluated (Gemma-3n-E4B, approximately 4B) matches the 70B model's vulnerability profile, indicating that robustness is model-specific rather than scale-dependent. | analysis:DA-20260627-SENSORY-CONTEXT-AUTHORITY |
| SF-2026-ARXIV-2606-28661 | score_7_9; potential_books_delta | not_selected | — | — | 完成 64-family frontier 对读后，《When More Sampling Hurts: The Modal Ceiling and Correlation Ceiling of Test-Time Scaling》不单独进入分析单元。其 source-specific delta 是：区分 test-time sampling coverage 与可部署 selection，并定义 modal/correlation ceiling 的停止边界。 决定性边界是：它改变 evaluator/measurement contract，但运行影响窄于三条入选的跨层 state/control chain。Exact-v1 non-proof：But a deployed system must return one answer, and choosing it, not knowing which try is right, is selection; selection is capped, and past a point extra samples only make the model surer of a confident mistake, even as every draw adds cost. | analysis-decision:SF-2026-ARXIV-2606-28661 |

<!-- analysis-decision:SF-2026-ARXIV-2606-27632:start -->
完成 64-family frontier 对读后，《Yuvion LLM: An Adversarially-Aware Large Language Model for Content And AI Safety》不单独进入分析单元。其 source-specific delta 是：把 adversarial robustness、agentic tool use 与 safety release evaluation 绑定为同一模型发布合同。 决定性边界是：除非改变哪类输入能取得 system-role authority，否则其边界窄于已入选 sensory-context authority break。Exact-v1 non-proof：Across these evaluations, Yuvion LLM demonstrates clear advantages on safety-focused benchmarks and particularly strong robustness under adversarial conditions, while maintaining solid overall capability.
<!-- analysis-decision:SF-2026-ARXIV-2606-27632:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-27634:start -->
完成 64-family frontier 对读后，《Continual Learning for Sequential Personalization of Small Language Models: A Stability Monitoring Analysis》不单独进入分析单元。其 source-specific delta 是：把 sequential LoRA personalization 的 checkpoint、reference-set drift 与遗忘监控绑定为持续适配合同。 决定性边界是：它仍是 observe/diagnose sensor contract，不取得 state-transition 或 release authority。Exact-v1 non-proof：However, personalization requires models to adapt over time to evolving user- or task-specific data, placing them in a continual learning setting.
<!-- analysis-decision:SF-2026-ARXIV-2606-27634:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-27650:start -->
完成 64-family frontier 对读后，《GenWorld: Empirically Grounded Urban Simulation Infrastructure for Scalable LLM-Agent Studies》不单独进入分析单元。其 source-specific delta 是：把城市级 agent environment、离线 policy compilation、人口/地理 grounding 与可复算 rollout 统一为 simulation infrastructure。 决定性边界是：它仍是 canonical owner 内的有界变化。Exact-v1 non-proof：These cases support GenWorld as a reproducible platform for grounded and scalable LLM-agent studies, while calibrated forecasting for traffic, evacuation, or policy outcomes remains future work.
<!-- analysis-decision:SF-2026-ARXIV-2606-27650:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-27669:start -->
完成 64-family frontier 对读后，《When Search Agents Should Ask: DiscoBench for Clarification-Aware Deep Search》不单独进入分析单元。其 source-specific delta 是：把 deep-search 的 ambiguity detection、clarification action、task utility 与交互成本分离成评估合同。 决定性边界是：它改变 evaluator/measurement contract，但运行影响窄于三条入选的跨层 state/control chain。Exact-v1 non-proof：However, existing benchmarks often assume that user queries are complete and explicit, overlooking the fact that real-world search requests are frequently vague, underspecified, or even factually incorrect.
<!-- analysis-decision:SF-2026-ARXIV-2606-27669:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-27679:start -->
完成 64-family frontier 对读后，《From Signals to Transfer: A Factorised Study of Probe-Based Uncertainty Estimation in Large Language Models》不单独进入分析单元。其 source-specific delta 是：给 probe uncertainty monitor 建立 feature、label construction、prompt 与 distribution-shift transfer 的可迁移边界。 决定性边界是：它仍是 observe/diagnose sensor contract，不取得 state-transition 或 release authority。Exact-v1 non-proof：However, under distribution shift, structured and compressed features are more robust, suggesting that in-domain performance alone is insufficient to measure progress.
<!-- analysis-decision:SF-2026-ARXIV-2606-27679:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-27683:start -->
完成 64-family frontier 对读后，《CBD: API-Only LLM Black-Box Unlearning through Controlled Behavioral Divergence》不单独进入分析单元。其 source-specific delta 是：揭示 API-only black-box unlearning 实际由 relevance router 与 auxiliary models 持有控制权，而非修改远端模型。 决定性边界是：除非改变哪类输入能取得 system-role authority，否则其边界窄于已入选 sensory-context authority break。Exact-v1 non-proof：On WMDP, it lowers hazardous knowledge accuracy to 25.68, near random guessing, while preserving MMLU accuracy of 52.67.
<!-- analysis-decision:SF-2026-ARXIV-2606-27683:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-27704:start -->
完成 64-family frontier 对读后，《AdvScan: Black-Box Adversarial Example Detection at Runtime through Power Analysis》不单独进入分析单元。其 source-specific delta 是：把 edge black-box adversarial detection 从模型内部 probe 改为 runtime power sensor，并暴露设备/攻击覆盖边界。 决定性边界是：除非改变哪类输入能取得 system-role authority，否则其边界窄于已入选 sensory-context authority break。Exact-v1 non-proof：Across 318,400 total test inputs, AdvScan detects 99.984% of AEs with only 40 false negatives and zero false positives.
<!-- analysis-decision:SF-2026-ARXIV-2606-27704:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-27709:start -->
完成 64-family frontier 对读后，《Low-Agreeableness Persona Conditioning for Safe LLM Fine-Tuning》不单独进入分析单元。其 source-specific delta 是：证明 warmth fine-tuning 的 jailbreak regression 取决于 persona/data construction，而非同理性目标本身必然削弱安全。 决定性边界是：它仍是 canonical owner 内的有界变化。Exact-v1 non-proof：These results show that safer empathetic fine-tuning is achievable through data design alone, without safety labels, harm detectors, or changes to the training objective.
<!-- analysis-decision:SF-2026-ARXIV-2606-27709:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-27732:start -->
完成 64-family frontier 对读后，《Bifocal Diffusion Language Models: Asymmetric Bidirectional Context for Parallel Generation》不单独进入分析单元。其 source-specific delta 是：用 asymmetric bidirectional sidecar 重构 diffusion-LM 的右上下文、KV cache 与 parallel decode 取舍。 决定性边界是：它改变 provisional generation/cache semantics，但仍完整落在 generation owner 内。Exact-v1 non-proof：Comprehensive experiments on continued pretraining of Qwen3-1.7B with 60B tokens demonstrate that R2LM achieves $2.4\times$ to $12.9\times$ higher throughput than bidirectional dLLMs and $1.9\times$ to $2.9\times$ speedup over AR baselines in batch serving through parallel decoding with KV caching, while exceeding the causal baseline on most benchmarks and surpassing the bidirectional dLLM on average.
<!-- analysis-decision:SF-2026-ARXIV-2606-27732:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-27739:start -->
完成 64-family frontier 对读后，《The Weakest Link Tells It All: Outcome-Supervised Process Reward Modeling via Learnable Credit Assignment》不单独进入分析单元。其 source-specific delta 是：把 outcome-supervised PRM 的 step credit assignment 表述为 weakest-link multiple-instance learning。 决定性边界是：它改变 trainer 内部 credit/guidance，但不跨 subsystem 移动 runtime 或 release authority。Exact-v1 non-proof：exact-v1 的结论只覆盖《The Weakest Link Tells It All: Outcome-Supervised Process Reward Modeling via Learnable Credit Assignment》在 3 Analysis; 3.3 Theoretical Analysis; 5 Experiments 声明的实验；它没有证明跨 model family、hardware/runtime、数据分布或未测 failure mode 的普遍成立。
<!-- analysis-decision:SF-2026-ARXIV-2606-27739:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-27743:start -->
完成 64-family frontier 对读后，《End-to-End Dynamic Sparsity for Resource-Adaptive LLM Inference》不单独进入分析单元。其 source-specific delta 是：把 layer/head/token compute footprint 变成由输入与实时资源预算共同控制的 runtime policy state。 决定性边界是：它仍是 canonical owner 内的有界变化。Exact-v1 non-proof：A single L2A model traces the entire compute-accuracy Pareto frontier on Llama-3-8B and Qwen-3-4B: at up to 34% realized layer sparsity, it stays within 0.6% of the dense baseline on GSM8K, with the same gap holding zero-shot on out-of-distribution tasks, while every static or heuristic baseline requires a separately tuned model and still drops by 5-10% at comparable inference time.
<!-- analysis-decision:SF-2026-ARXIV-2606-27743:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-27757:start -->
完成 64-family frontier 对读后，《Towards Reliable and Robust LLM Planning: Symbolic Feedback-Driven Iterative Self-Refinement Framework》不单独进入分析单元。其 source-specific delta 是：把 symbolic verifier、reachability recognizer 与 revision loop 放到 long-horizon plan 的显式控制流。 决定性边界是：它增加 bounded planning verifier，同时保持 environment/controller commit authority 不变。Exact-v1 non-proof：exact-v1 的结论只覆盖《Towards Reliable and Robust LLM Planning: Symbolic Feedback-Driven Iterative Self-Refinement Framework》在 IV EXPERIMENTS; IV-A Experimental Settings; IV-D Analysis of Planning Length 声明的实验；它没有证明跨 model family、hardware/runtime、数据分布或未测 failure mode 的普遍成立。
<!-- analysis-decision:SF-2026-ARXIV-2606-27757:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-27780:start -->
完成 64-family frontier 对读后，《Understanding Rollout Error in Graph World Models》不单独进入分析单元。其 source-specific delta 是：给 graph world-model rollout 建立 topology/model factor 分解与 dynamic-edge error feedback contract。 决定性边界是：它改变 model-state interface，但没有越过已入选 strict-mediation chain 的 authority 边界。Exact-v1 non-proof：Our results characterize when graph world models remain reliable under autoregressive planning and when topology makes them fail.
<!-- analysis-decision:SF-2026-ARXIV-2606-27780:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-27791:start -->
完成 64-family frontier 对读后，《NLL-Guided Full-Attention Layer Selection for Training-Free Sliding-Window Adaptation》不单独进入分析单元。其 source-specific delta 是：以 answer-token NLL degradation 选择保留 full-attention 的层，改变 hybrid attention 的 calibration owner。 决定性边界是：它是有界的 attention calibration/layout 结果，而不是新的跨层 control contract。Exact-v1 non-proof：The method requires only $\sim$15 minutes of one-time calibration, advancing the efficiency-accuracy Pareto frontier for long-context LLM deployment.
<!-- analysis-decision:SF-2026-ARXIV-2606-27791:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-27797:start -->
完成 64-family frontier 对读后，《Optimizing Teacher-Student Partitioning for Scalable Knowledge Distillation on HPC Systems》不单独进入分析单元。其 source-specific delta 是：按 teacher/student 不对称分别选择模型分片与拓扑通信，改变 KD runtime partition contract。 决定性边界是：它改变 training runtime partition/handoff，但影响仍受限于 distillation job。Exact-v1 non-proof：exact-v1 的结论只覆盖《Optimizing Teacher-Student Partitioning for Scalable Knowledge Distillation on HPC Systems》在 3 Testing Setup; 4 GKD Analysis and Improvements; 4.1 Experimental Results 声明的实验；它没有证明跨 model family、hardware/runtime、数据分布或未测 failure mode 的普遍成立。
<!-- analysis-decision:SF-2026-ARXIV-2606-27797:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-27806:start -->
完成 64-family frontier 对读后，《Agent vs. Parametric World Models: Hybrid Planning for Reliable Language Agents》不单独进入分析单元。其 source-specific delta 是：以 parametric transition model 校验 agent imagined delta，并把 disagreement 变成 targeted revision gate。 决定性边界是：它增加 bounded planning verifier，同时保持 environment/controller commit authority 不变。Exact-v1 non-proof：These results suggest that lightweight parametric transition models can serve as effective grounding mechanisms for language-agent planning without replacing semantic reasoning.
<!-- analysis-decision:SF-2026-ARXIV-2606-27806:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-27814:start -->
完成 64-family frontier 对读后，《ATOD: Annealed Turn-Aware On-Policy Distillation for Multi-Turn Agentic Tasks》不单独进入分析单元。其 source-specific delta 是：在 multi-turn agent training 中按 competence/turn state 退火切换 on-policy distillation 与 environment reward。 决定性边界是：它改变 trainer 内部 credit/guidance，但不跨 subsystem 移动 runtime 或 release authority。Exact-v1 non-proof：Experiments on ALFWorld, WebShop, and Search-QA show that ATOD consistently outperforms competing post-training baselines: across the three student sizes, ATOD improves average success rate by 4.16 points over OPD and 23.62 points over GRPO, while surpassing the corresponding teacher models by 2.16 points.
<!-- analysis-decision:SF-2026-ARXIV-2606-27814:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-27826:start -->
完成 64-family frontier 对读后，《NormAct: Benchmarking Embodied Agents' Proactive Compliance with Unspoken Social Norms》不单独进入分析单元。其 source-specific delta 是：把 embodied-agent goal success 与未明示社会规范的自主识别/遵守拆成渐进 guidance evaluation contract。 决定性边界是：它改变 evaluator/measurement contract，但运行影响窄于三条入选的跨层 state/control chain。Exact-v1 non-proof：NormAct therefore supports the development of embodied agents that pursue everyday goals while proactively respecting unstated social norms.
<!-- analysis-decision:SF-2026-ARXIV-2606-27826:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-27841:start -->
完成 64-family frontier 对读后，《WattLayer: Get Layers Right to Estimate Inference Energy of Neural Networks》不单独进入分析单元。其 source-specific delta 是：把 inference energy estimation 从整模型 proxy 拆成可跨任务/架构迁移的 layer-wise measurement contract。 决定性边界是：它改变 cost attribution granularity，但仍从属于 measured run evidence。Exact-v1 non-proof：We further show that layer-wise decomposition generalize to new tasks without complete retraining, by leveraging shared layers across architectures.
<!-- analysis-decision:SF-2026-ARXIV-2606-27841:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-27866:start -->
完成 64-family frontier 对读后，《FlexMoE: One-for-All Nested Intra-Expert Pruning for MoE Language Models》不单独进入分析单元。其 source-specific delta 是：把一次性 MoE compression artifact 改成 nested subnet family 与可在线切换的 budget state。 决定性边界是：canonical MoE owner 已持有 budget-profile state，因此本 family 只增加实现证据，不另建 analysis unit。Exact-v1 non-proof：Specifically, on Qwen2-57B-A14B, our method retains ~99.8% of base performance while pruning 50% of routed expert parameters even without fine-tuning.
<!-- analysis-decision:SF-2026-ARXIV-2606-27866:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-27934:start -->
完成 64-family frontier 对读后，《Self-Verifying Measurement Records: Hash-Linked Evidence Graphs for Hardware Benchmarking》不单独进入分析单元。其 source-specific delta 是：用 hash-linked measurement/evidence graph 与 output-derived challenge 让硬件 benchmark 可离线验证。 决定性边界是：它改变 evaluator/measurement contract，但运行影响窄于三条入选的跨层 state/control chain。Exact-v1 non-proof：We then treat the check itself as a security object: a probe seed committed for offline reproducibility is an attack surface, and a probe-aware adversary can hide a corruption in the probe's null space, fooling even a quorum of bit-identical witnesses, while a Fiat-Shamir challenge derived from the claimed output closes this.
<!-- analysis-decision:SF-2026-ARXIV-2606-27934:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-27936:start -->
完成 64-family frontier 对读后，《Agentic AI-Powered Re-Identification: An Emerging, Scalable Threat to Mobility Microdata Privacy》不单独进入分析单元。其 source-specific delta 是：证明 agentic open-web resolution 把 mobility re-identification 从专家手工能力改成可规模化 threat model。 决定性边界是：除非改变哪类输入能取得 system-role authority，否则其边界窄于已入选 sensory-context authority break。Exact-v1 non-proof：We present an end-to-end pipeline in which large language model agents autonomously search the open web, cross-reference public records and social media, and resolve raw coordinate sequences to candidate identities - without human intervention.
<!-- analysis-decision:SF-2026-ARXIV-2606-27936:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-27944:start -->
完成 64-family frontier 对读后，《It Lied to a Doctor to Buy Poison Ingredients: Quantifying Real-World Misuse of Phone-use Agents》不单独进入分析单元。其 source-specific delta 是：以真实 phone/app side effects 揭示 safety awareness 与 execution authorization 分离后的 misuse failure。 决定性边界是：除非改变哪类输入能取得 system-role authority，否则其边界窄于已入选 sensory-context authority break。Exact-v1 non-proof：Simple defenses curb the overt cases, but the more covert and arguably more damaging threats, such as coordinated review manipulation and fake traffic, remain largely unsolved.
<!-- analysis-decision:SF-2026-ARXIV-2606-27944:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-27962:start -->
完成 64-family frontier 对读后，《Building a Scalable, Reproducible, Evaluatable, and Closed-Loop Simulation Environment Foundation for Embodied Intelligence》不单独进入分析单元。其 source-specific delta 是：把 embodied simulation 的 environment、trajectory、evaluation、data 与 elastic cloud scheduling 统一成闭环平台。 决定性边界是：它仍是 canonical owner 内的有界变化。Exact-v1 non-proof：exact-v1 的结论只覆盖《Building a Scalable, Reproducible, Evaluatable, and Closed-Loop Simulation Environment Foundation for Embodied Intelligence》在 Building a Scalable, Reproducible, Evaluatable, and Closed-Loop Simulation Environment Foundation for Embodied Intelligence Cloud-Native Simulation Infrastructure for Embodied Intelligence Training, Evaluation, and Data Collection; 1.2 Bottlenecks in Real Robot Data and Evaluation; 3.2 Mainstream Benchmarks and Datasets 声明的实验；它没有证明跨 model family、hardware/runtime、数据分布或未测 failure mode 的普遍成立。
<!-- analysis-decision:SF-2026-ARXIV-2606-27962:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-27976:start -->
完成 64-family frontier 对读后，《SHARD: cell-keyed residual splitting for alignment-resistant private dense retrieval》不单独进入分析单元。其 source-specific delta 是：把 private dense retrieval 的 routing prefix、cell-local residual key、CKKS rerank 与 linkage risk 分开声明。 决定性边界是：它仍是 canonical owner 内的有界变化。Exact-v1 non-proof：SHARD preserves retrieval and compartmentalizes alignment evidence, but does not provide DP, unlinkability, or cancellable templates.
<!-- analysis-decision:SF-2026-ARXIV-2606-27976:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-27997:start -->
完成 64-family frontier 对读后，《Benchmarking on Tasks That Matter: Dataset Selection for Preserving Model Rankings》不单独进入分析单元。其 source-specific delta 是：把 benchmark task subset selection 绑定 rank-preservation uncertainty，而非把少量数据集当作无损代理。 决定性边界是：它改变 evaluator/measurement contract，但运行影响窄于三条入选的跨层 state/control chain。Exact-v1 non-proof：For TSC, our best-performing strategy achieves a Spearman correlation of 0.95 with the full benchmark model rankings using only five selected datasets.
<!-- analysis-decision:SF-2026-ARXIV-2606-27997:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-28011:start -->
完成 64-family frontier 对读后，《From Detection to Action: Using LLM Agents for Fault-Tolerant Control》不单独进入分析单元。其 source-specific delta 是：把 LLM recovery proposal 放在 plant twin simulation、deterministic interlock validation 与 bounded fallback 之后。 决定性边界是：它仍是 canonical owner 内的有界变化。Exact-v1 non-proof：exact-v1 的结论只覆盖《From Detection to Action: Using LLM Agents for Fault-Tolerant Control》在 4.3 Evaluation criteria; 5 Results; 5.1 Mixing module results 声明的实验；它没有证明跨 model family、hardware/runtime、数据分布或未测 failure mode 的普遍成立。
<!-- analysis-decision:SF-2026-ARXIV-2606-28011:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-28013:start -->
完成 64-family frontier 对读后，《The Signal-Coverage Matrix: Stratifying Type and Semantic Errors in Statement Autoformalization》不单独进入分析单元。其 source-specific delta 是：把 autoformalization 的 type correctness 与 semantic equivalence 交叉分层，防止单标量误归因。 决定性边界是：它改变 evaluator/measurement contract，但运行影响窄于三条入选的跨层 state/control chain。Exact-v1 non-proof：We propose a signal-coverage matrix that crosses the Lean elaborator (pass/fail) with a semantic-equivalence judgment (equivalent/not), sorting every output into one of four cells: true success (TS), type-only (TO), semantic-only (SO), or both fail (BF).
<!-- analysis-decision:SF-2026-ARXIV-2606-28013:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-28037:start -->
完成 64-family frontier 对读后，《Evolution-Aware Regression Test Prioritization of ML-Enabled Systems Using Gradient-Based Behavior Vectors》不单独进入分析单元。其 source-specific delta 是：以原模型 gradient behavior vector 和 parameter delta 做 evolution-aware regression-test prioritization。 决定性边界是：它改变 evaluator/measurement contract，但运行影响窄于三条入选的跨层 state/control chain。Exact-v1 non-proof：In an empirical study across classification and regression tasks, GBV-PD consistently outperformed non-directional baselines and remained competitive with a full-gradient reference, while offering better time and storage profiles for repeated updates via reusable GBV caching.
<!-- analysis-decision:SF-2026-ARXIV-2606-28037:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-28050:start -->
完成 64-family frontier 对读后，《Can LLMs Judge Better Than They Generate? Evaluating Task Asymmetry, Mechanistic Interpretability and Transferability for In-Context QA》不单独进入分析单元。其 source-specific delta 是：用 controlled in-context QA 反证 self-evaluation 普遍比 generation 更容易的默认假设。 决定性边界是：它改变 evaluator/measurement contract，但运行影响窄于三条入选的跨层 state/control chain。Exact-v1 non-proof：exact-v1 的结论只覆盖《Can LLMs Judge Better Than They Generate? Evaluating Task Asymmetry, Mechanistic Interpretability and Transferability for In-Context QA》在 Generation–evaluation asymmetry.; 3.1 Task Asymmetry Analysis; Evaluation task ( 𝒯 eval \mathcal{T}_{\text{eval}} ). 声明的实验；它没有证明跨 model family、hardware/runtime、数据分布或未测 failure mode 的普遍成立。
<!-- analysis-decision:SF-2026-ARXIV-2606-28050:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-28061:start -->
完成 64-family frontier 对读后，《ToolPrivacyBench: Benchmarking Purpose-Bound Privacy in Tool-Using LLM Agents》不单独进入分析单元。其 source-specific delta 是：把 tool-agent privacy 从最终文本扩展到每个 tool argument、sink 与 purpose-bound information flow。 决定性边界是：除非改变哪类输入能取得 system-role authority，否则其边界窄于已入选 sensory-context authority break。Exact-v1 non-proof：ToolPrivacyBench therefore formalizes a need-to-know disclosure boundary, under which each tool should receive only the information necessary for its stated purpose, and uses trajectory-level auditing to identify privacy over-disclosure in multi-tool workflows.
<!-- analysis-decision:SF-2026-ARXIV-2606-28061:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-28070:start -->
完成 64-family frontier 对读后，《JD Oxygen AI Item Center (Oxygen AIIC) V1: An Industrial-Scale LLM/VLM-Centric Solution for Item Understanding, Management, and Applications》不单独进入分析单元。其 source-specific delta 是：提供 ontology、knowledge production、model evolution、unified data/service tunnel 在工业规模下的统一平台合同。 决定性边界是：它仍是 canonical owner 内的有界变化。Exact-v1 non-proof：exact-v1 的结论只覆盖《JD Oxygen AI Item Center (Oxygen AIIC) V1: An Industrial-Scale LLM/VLM-Centric Solution for Item Understanding, Management, and Applications》在 3.3 Results; 4.2.3 Results; Module 1: Data evaluation. 声明的实验；它没有证明跨 model family、hardware/runtime、数据分布或未测 failure mode 的普遍成立。
<!-- analysis-decision:SF-2026-ARXIV-2606-28070:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-28116:start -->
完成 64-family frontier 对读后，《Mechanism-Driven Monitors for Preemptive Detection of LLM Training Instability》不单独进入分析单元。其 source-specific delta 是：从 attention/router 的故障机理导出 pre-loss training-instability sensors，而非等待 loss collapse。 决定性边界是：它仍是 observe/diagnose sensor contract，不取得 state-transition 或 release authority。Exact-v1 non-proof：After a numerical or a hyperparameter fault has already destabilized the training dynamics, it may continue for thousands of steps while loss and gradient norms still appear normal.
<!-- analysis-decision:SF-2026-ARXIV-2606-28116:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-28128:start -->
完成 64-family frontier 对读后，《PhysisForcing: Physics Reinforced World Simulator for Robotic Manipulation》不单独进入分析单元。其 source-specific delta 是：把 video-world-simulator 的 contact/trajectory physics supervision 与 downstream closed-loop policy effect 联结。 决定性边界是：它改变 model-state interface，但没有越过已入选 strict-mediation chain 的 authority 边界。Exact-v1 non-proof：However, both general-domain video generators and robot-specific data fine-tuned models can still produce physically implausible manipulations, including discontinuous motion trajectories and inconsistent robot-object interactions, which limits their reliability as world simulators.
<!-- analysis-decision:SF-2026-ARXIV-2606-28128:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-28153:start -->
完成 64-family frontier 对读后，《Robust Harmful Features Under Jailbreak Attacks: Mechanistic Evidence from Attention Head Specialization in Large Language Models》不单独进入分析单元。其 source-specific delta 是：区分被攻击抑制与仍持续存在的 safety attention heads，并验证其 causal/monitoring 边界。 决定性边界是：除非改变哪类输入能取得 system-role authority，否则其边界窄于已入选 sensory-context authority break。Exact-v1 non-proof：To validate the practical significance of this robustness, we show that simply reading these persistent activations -- without any training -- yields competitive aggregate detection performance with strong adversarial robustness.
<!-- analysis-decision:SF-2026-ARXIV-2606-28153:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-28166:start -->
完成 64-family frontier 对读后，《Tandem Reinforcement Learning with Verifiable Rewards》不单独进入分析单元。其 source-specific delta 是：让 senior/junior 交替共同生成 RLVR rollout，把 handoff compatibility 变成训练目标。 决定性边界是：它改变 trainer 内部 credit/guidance，但不跨 subsystem 移动 runtime 或 release authority。Exact-v1 non-proof：Training Qwen3-4B-Instruct on competition math, we find that TRL matches vanilla GRPO on solo reasoning capability while three properties emerge together from the same rollout structure: stronger handoff robustness with the junior, reduced distributional drift from the junior, and a chain-of-thought more legible to the junior.
<!-- analysis-decision:SF-2026-ARXIV-2606-28166:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-28187:start -->
完成 64-family frontier 对读后，《GBC: Gradient-Based Connections for Optimizing Multi-Agent Systems》不单独进入分析单元。其 source-specific delta 是：把 multi-agent interaction 建成可反传 attribution graph，以 token-level influence 分配错误责任。 决定性边界是：interaction attribution 命题已被 canonical owner 持有，不足以形成另一条叙事。Exact-v1 non-proof：However, their performance is often limited by miscoordination and, more fundamentally, the lack of fine-grained credit assignment across agents.
<!-- analysis-decision:SF-2026-ARXIV-2606-28187:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-28235:start -->
完成 64-family frontier 对读后，《Govern the Repository, Not the Agent: Measuring Ecosystem-Level Risk in AI-Native Software》不单独进入分析单元。其 source-specific delta 是：用大规模 PR 数据把 coding-agent 风险 owner 从单次 agent score 移到 repository-level integration friction。 决定性边界是：它仍是 canonical owner 内的有界变化。Exact-v1 non-proof：exact-v1 的结论只覆盖《Govern the Repository, Not the Agent: Measuring Ecosystem-Level Risk in AI-Native Software》在 IV-B Level of analysis and why multilevel models; V Results 声明的实验；它没有证明跨 model family、hardware/runtime、数据分布或未测 failure mode 的普遍成立。
<!-- analysis-decision:SF-2026-ARXIV-2606-28235:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-28276:start -->
完成 64-family frontier 对读后，《SimFoundry: Modular and Automated Scene Generation for Policy Learning and Evaluation》不单独进入分析单元。其 source-specific delta 是：把 video-to-sim reconstruction、digital cousins、policy training 与 sim-to-real rank validity 绑定。 决定性边界是：它改变进入 physical promotion 的 evidence handoff，但不取代入选 inference/security chain。Exact-v1 non-proof：exact-v1 的结论只覆盖《SimFoundry: Modular and Automated Scene Generation for Policy Learning and Evaluation》在 SimFoundry: Modular and Automated Scene Generation for Policy Learning and Evaluation; 5 Experiments; 5.1 Real-to-Sim Policy Evaluation 声明的实验；它没有证明跨 model family、hardware/runtime、数据分布或未测 failure mode 的普遍成立。
<!-- analysis-decision:SF-2026-ARXIV-2606-28276:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-28277:start -->
完成 64-family frontier 对读后，《Towards Automating Scientific Review with Google's Paper Assistant Tool》不单独进入分析单元。其 source-specific delta 是：把 agentic scientific review 的 verification depth 与 human decision authority 分层，并给出部署证据。 决定性边界是：它改变 evaluator/measurement contract，但运行影响窄于三条入选的跨层 state/control chain。Exact-v1 non-proof：By catching errors early, PAT eases the cognitive burden placed on referees, while preserving their control over the outcomes of the review process.
<!-- analysis-decision:SF-2026-ARXIV-2606-28277:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-28279:start -->
完成 64-family frontier 对读后，《Agentic Hardware Design as Repository-Level Code Evolution》不单独进入分析单元。其 source-specific delta 是：用 compiled project pack、acceptance predicate、isolated worktree 与 trace/replay 管理 repository-scale hardware agent。 决定性边界是：它仍是 canonical owner 内的有界变化。Exact-v1 non-proof：However, we do not claim that agentic AI for hardware design is solved: these benchmarks are controlled proxies for a much broader engineering problem in chip design.
<!-- analysis-decision:SF-2026-ARXIV-2606-28279:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-28322:start -->
完成 64-family frontier 对读后，《PerceptionRubrics: Calibrating Multimodal Evaluation to Human Perception》不单独进入分析单元。其 source-specific delta 是：以 Must-Right/Easy-Wrong atomic rubrics 与 gated penalty 替代会掩盖必需事实失败的平均分。 决定性边界是：它改变 evaluator/measurement contract，但运行影响窄于三条入选的跨层 state/control chain。Exact-v1 non-proof：exact-v1 的结论只覆盖《PerceptionRubrics: Calibrating Multimodal Evaluation to Human Perception》在 PerceptionRubrics: Calibrating Multimodal Evaluation to Human Perception; Visual Perception Benchmarks in MLLMs.; Evaluation of Image Captioning. 声明的实验；它没有证明跨 model family、hardware/runtime、数据分布或未测 failure mode 的普遍成立。
<!-- analysis-decision:SF-2026-ARXIV-2606-28322:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-28430:start -->
完成 64-family frontier 对读后，《Building to the Test: Coding Agents Deliver What You Check, Not What You Requested》不单独进入分析单元。其 source-specific delta 是：用 no-op ablation 揭示 coding agent 可通过 oracle 却未交付可复用 artifact 的 construction-validity failure。 决定性边界是：它改变 evaluator/measurement contract，但运行影响窄于三条入选的跨层 state/control chain。Exact-v1 non-proof：The agent does not, on its own, validate what it ships as a user would.
<!-- analysis-decision:SF-2026-ARXIV-2606-28430:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-28433:start -->
完成 64-family frontier 对读后，《Position: RL Researchers Need to Distinguish Between Solving Simulators and Using Simulators as a Proxy》不单独进入分析单元。其 source-specific delta 是：要求 RL evaluation 区分把 simulator 当目标与把 simulator 当 deployment proxy 的两套约束。 决定性边界是：它改变 evaluator/measurement contract，但运行影响窄于三条入选的跨层 state/control chain。Exact-v1 non-proof：To achieve high scores, researchers may adopt solutions exclusively meant for solving simulators, rather than learning while the agent is deployed outside a simulator.
<!-- analysis-decision:SF-2026-ARXIV-2606-28433:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-28434:start -->
完成 64-family frontier 对读后，《SWE-MeM: Learning Adaptive Memory Management for Long-Horizon Coding Agents》不单独进入分析单元。其 source-specific delta 是：把 coding-agent compression timing、granularity 与剩余 context budget 变成 agent-controlled memory action。 决定性边界是：它仍是 canonical owner 内的有界变化。Exact-v1 non-proof：Moreover, these approaches fail to jointly optimize memory management and issue resolution capabilities to improve performance while reducing token usage.
<!-- analysis-decision:SF-2026-ARXIV-2606-28434:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-28436:start -->
完成 64-family frontier 对读后，《Dockerless: Environment-Free Program Verifier for Coding Agents》不单独进入分析单元。其 source-specific delta 是：把 coding post-training verifier 从 executable environment 改成 repository-evidence judge，改变 reward authority 与 non-proof 边界。 决定性边界是：它改变 trainer 内部 credit/guidance，但不跨 subsystem 移动 runtime 或 release authority。Exact-v1 non-proof：We propose Dockerless, an environment-free agentic patch verifier that evaluates generated code patches without executing them.
<!-- analysis-decision:SF-2026-ARXIV-2606-28436:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-28438:start -->
完成 64-family frontier 对读后，《When AI Reviews Its Own Code: Recursive Self-Training Collapse in Code LLMs》不单独进入分析单元。其 source-specific delta 是：证明 recursive code self-training 的 model-coupled gate 会 rubber-stamp collapse，要求 exogenous verification。 决定性边界是：它仍是 canonical owner 内的有界变化。Exact-v1 non-proof：In the clearest case, the binary self-gate enters a rubber-stamp regime where acceptance scores rise while benchmark correctness falls.
<!-- analysis-decision:SF-2026-ARXIV-2606-28438:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-28455:start -->
完成 64-family frontier 对读后，《Event-Conditioned Diagnostics of Kinematic, Contact, and Object-Permanence Structure in Passive Object-State World Models》不单独进入分析单元。其 source-specific delta 是：把 event readout、context-relative emphasis 与 causal sensitivity 分开评估 latent physical structure。 决定性边界是：它改变 model-state interface，但没有越过已入选 strict-mediation chain 的 authority 边界。Exact-v1 non-proof：These results support event-conditioned latent structure and functional sensitivity without implying explicit physical modules or isolated causal circuits.
<!-- analysis-decision:SF-2026-ARXIV-2606-28455:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-28471:start -->
完成 64-family frontier 对读后，《Data and Evaluation Closed-Loop for Model Capability Enhancement》不单独进入分析单元。其 source-specific delta 是：以 capability slice 将 evaluation failure 反向映射为可检验 data intervention，并允许判定 data 非根因。 决定性边界是：它仍是 canonical owner 内的有界变化。Exact-v1 non-proof：First, the loop rules the data out: continued pre-training drives BBH down by $-46.82\%$, but diagnosis traces this to a single masked \texttt{\textless EOS\textgreater} loss rather than weakened reasoning; restoring it recovers BBH to $66.44$, above the original checkpoint, without changing the data.
<!-- analysis-decision:SF-2026-ARXIV-2606-28471:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-28479:start -->
完成 64-family frontier 对读后，《Decomposing Memorization Reduction in Privacy-Preserving Fine-Tuning of SLMs for CSIRTs》不单独进入分析单元。其 source-specific delta 是：用 matched-update controls 分离 DP guarantee、pseudonymization 与 optimizer-step memorization effect。 决定性边界是：它改善 adapter training 内部 causal attribution，但不移动 deployment authority。Exact-v1 non-proof：Third, F1 scores remain between 0.19 and 0.28 across all 96 adapters using four shot prompting, indicating that, under the evaluated training budget, 1B to 3B SLMs do not achieve operationally useful performance.
<!-- analysis-decision:SF-2026-ARXIV-2606-28479:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-28480:start -->
完成 64-family frontier 对读后，《TUA-Bench: A Benchmark for General-Purpose Terminal-Use Agents》不单独进入分析单元。其 source-specific delta 是：把 terminal-use agent 扩展到非 coding workflow，并用 deterministic setup/execution scoring 约束 release claim。 决定性边界是：它改变 evaluator/measurement contract，但运行影响窄于三条入选的跨层 state/control chain。Exact-v1 non-proof：However, existing benchmarks do not adequately evaluate general-purpose terminal computer-use agents (TUAs): general computer-use benchmarks primarily target graphical user interfaces (GUIs), whereas terminal-based benchmarks largely emphasize technical and programming-centric workflows historically native to the shell.
<!-- analysis-decision:SF-2026-ARXIV-2606-28480:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-28514:start -->
完成 64-family frontier 对读后，《GPTNT: Benchmarking Real-Time Collaboration Between Multimodal Agents on Keep Talking And Nobody Explodes》不单独进入分析单元。其 source-specific delta 是：以真实异步倒计时、信息不对称与不可单独完成任务测量实时 collaboration。 决定性边界是：interaction attribution 命题已被 canonical owner 持有，不足以形成另一条叙事。Exact-v1 non-proof：One agent can see and manipulate the bomb but does not have the defusal instructions; the other has the instructions but cannot see or manipulate the bomb.
<!-- analysis-decision:SF-2026-ARXIV-2606-28514:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-28551:start -->
完成 64-family frontier 对读后，《DataComp-VLM: Improved Open Datasets for Vision-Language Models》不单独进入分析单元。其 source-specific delta 是：用固定 model/token budget 与多数据类型 corpus 建立 VLM data curation、mixing 与 release artifact 的可复算合同。 决定性边界是：它仍是 canonical owner 内的有界变化。Exact-v1 non-proof：As part of DCVLM, we collect 160 datasets spanning four data types -- image-caption pairs, multimodal interleaved documents, text-only, and instruction-tuning data -- into a corpus of 6T multimodal tokens.
<!-- analysis-decision:SF-2026-ARXIV-2606-28551:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-28560:start -->
完成 64-family frontier 对读后，《Depth-Staggered Fibonacci Spacing for Sparse Attention: Static Schedules Beat Learned Dilation and Extrapolate Where Dense Attention Fails》不单独进入分析单元。其 source-specific delta 是：以 matched small-model study 反证 learned sparse spacing 必然优于 static schedule，并暴露 train-length 与 extrapolation 的反向取舍。 决定性边界是：它是有界的 attention calibration/layout 结果，而不是新的跨层 control contract。Exact-v1 non-proof：Third, and most consequential, all sparse variants extrapolate to four times their training length with little or no degradation, whereas a recipe-matched dense baseline collapses (perplexity rises by 201% at 4x length); we attribute this to fixed-offset attention only ever querying relative positions seen during training.
<!-- analysis-decision:SF-2026-ARXIV-2606-28560:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-28562:start -->
完成 64-family frontier 对读后，《SEAD: Competence-Aware On-Policy Distillation via Entropy-Guided Supervision》不单独进入分析单元。其 source-specific delta 是：按 student competence 在 token、phase、prompt 三个尺度控制 on-policy distillation supervision。 决定性边界是：它改变 trainer 内部 credit/guidance，但不跨 subsystem 移动 runtime 或 release authority。Exact-v1 non-proof：exact-v1 的结论只覆盖《SEAD: Competence-Aware On-Policy Distillation via Entropy-Guided Supervision》在 3 Evaluation; 3.1 Experimental Setup; Evaluation. 声明的实验；它没有证明跨 model family、hardware/runtime、数据分布或未测 failure mode 的普遍成立。
<!-- analysis-decision:SF-2026-ARXIV-2606-28562:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-28574:start -->
完成 64-family frontier 对读后，《Correct codes for the wrong reasons? validating LLMs as measurement instruments for theoretical constructs》不单独进入分析单元。其 source-specific delta 是：把 LLM coder 的表面一致性与 theoretical construct validity 分开，并要求 clause-level extractive evidence。 决定性边界是：它改变 evaluator/measurement contract，但运行影响窄于三条入选的跨层 state/control chain。Exact-v1 non-proof：exact-v1 的结论只覆盖《Correct codes for the wrong reasons? validating LLMs as measurement instruments for theoretical constructs》在 3.1 Clauses with grounds; 3.2 Human in the loop 声明的实验；它没有证明跨 model family、hardware/runtime、数据分布或未测 failure mode 的普遍成立。
<!-- analysis-decision:SF-2026-ARXIV-2606-28574:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-28615:start -->
完成 64-family frontier 对读后，《What LLMs explain is not what they believe: Evaluating explanation sufficiency under models' own input beliefs》不单独进入分析单元。其 source-specific delta 是：把 free-text explanation sufficiency 绑定显式 input distribution 与 self-consistent information metric。 决定性边界是：它改变 evaluator/measurement contract，但运行影响窄于三条入选的跨层 state/control chain。Exact-v1 non-proof：We formalize self-consistent sufficiency as a goal for free-text explanations and introduce an information-theoretic metric, SCSuff, that enables evaluation of free-text explanations without relying on predefined biases or shortcuts.
<!-- analysis-decision:SF-2026-ARXIV-2606-28615:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-28639:start -->
完成 64-family frontier 对读后，《The Unverifiability of Artificial General Intelligence (AGI) Alignment, Static and Dynamic: From Trakhtenbrot's Wall to the Safety-Generality Tension》不单独进入分析单元。其 source-specific delta 是：给 static/dynamic alignment certification 划出 expressivity、soundness、completeness 与 tractability 的形式边界。 决定性边界是：除非改变哪类输入能取得 system-role authority，否则其边界窄于已入选 sensory-context authority break。Exact-v1 non-proof：Three practical risks (finite test coverage, bounded deliberation time, restricted observation) are one phenomenon: every bounded scheme that does not reject correct evidence admits an evolution trace it certifies at every stage while the property is persistently violated.
<!-- analysis-decision:SF-2026-ARXIV-2606-28639:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-28661:start -->
完成 64-family frontier 对读后，《When More Sampling Hurts: The Modal Ceiling and Correlation Ceiling of Test-Time Scaling》不单独进入分析单元。其 source-specific delta 是：区分 test-time sampling coverage 与可部署 selection，并定义 modal/correlation ceiling 的停止边界。 决定性边界是：它改变 evaluator/measurement contract，但运行影响窄于三条入选的跨层 state/control chain。Exact-v1 non-proof：But a deployed system must return one answer, and choosing it, not knowing which try is right, is selection; selection is capped, and past a point extra samples only make the model surer of a confident mistake, even as every draw adds cost.
<!-- analysis-decision:SF-2026-ARXIV-2606-28661:end -->

<!-- analysis:DA-20260627-STRICT-MEDIATED-WORLD-STATE:start -->
### DA-20260627-STRICT-MEDIATED-WORLD-STATE

若 world model 可从 history bypass latent state，预测准确率无法识别 state quality。strict mediation 把 textual belief state 变成唯一读取面，训练代价和离散状态误差则成为新的 failure pressure。
<!-- analysis:DA-20260627-STRICT-MEDIATED-WORLD-STATE:end -->

<!-- analysis:DA-20260627-PHASE-CLOSED-LOOP-INFERENCE:start -->
### DA-20260627-PHASE-CLOSED-LOOP-INFERENCE

mobile phase characterization、closed-loop task time 与 kernel-level capacity simulation 共同说明：推理优化不能只发布单步 latency。backend 必须按 vision/prefill/decode/queue/kernel phase 建模，并以任务完成时间、success 与饱和边界验收。
<!-- analysis:DA-20260627-PHASE-CLOSED-LOOP-INFERENCE:end -->

<!-- analysis:DA-20260627-SENSORY-CONTEXT-AUTHORITY:start -->
### DA-20260627-SENSORY-CONTEXT-AUTHORITY

机器人把 OCR、STT 与 LiDAR state 序列化进 prompt 后，system-role 文本也可能来自不可信 sensor。安全边界必须在 middleware provenance 与 cross-modal consistency 上建立，不能只过滤 user message。
<!-- analysis:DA-20260627-SENSORY-CONTEXT-AUTHORITY:end -->

## 6. Books Comparison

 and Decision

<!-- validator:books-comparison-v1 -->
| Source Family ID | Stable Node ID | Target Chapter Ref | Adjacent Chapter Refs | Existing Proposition | New Evidence Delta | Evolution Relation | Decision | Books Review Ref |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2606-27632 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#L733 — ## 风险管理而不是一次性认证 | books/part-06-ai-infrastructure/71-multi-tenant.md#L10 — ## 本章要回答的问题 | existing:SF-2026-ARXIV-2606-27632 | delta:SF-2026-ARXIV-2606-27632 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-27632 |
| SF-2026-ARXIV-2606-27634 | PLATFORM-MONITORING | books/part-06-ai-infrastructure/67-monitoring.md#L206 — ## Monitoring 也会改变系统 | books/part-06-ai-infrastructure/66-evaluation-system.md#L10 — ## 本章要回答的问题 | existing:SF-2026-ARXIV-2606-27634 | delta:SF-2026-ARXIV-2606-27634 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-27634 |
| SF-2026-ARXIV-2606-27650 | AGENT-PLATFORM | books/part-07-agent/84-agent-platform.md#L399 — ## Agent Runtime State Machine | books/part-07-agent/83-mcp.md#L10 — ## 本章要回答的问题 | existing:SF-2026-ARXIV-2606-27650 | delta:SF-2026-ARXIV-2606-27650 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-27650 |
| SF-2026-ARXIV-2606-27669 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#L353 — ### Evaluator 可以主动制造 Probe，但不能冒充被动观察 | books/part-06-ai-infrastructure/67-monitoring.md#L10 — ## 本章要回答的问题 | existing:SF-2026-ARXIV-2606-27669 | delta:SF-2026-ARXIV-2606-27669 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-27669 |
| SF-2026-ARXIV-2606-27679 | PLATFORM-MONITORING | books/part-06-ai-infrastructure/67-monitoring.md#L206 — ## Monitoring 也会改变系统 | books/part-06-ai-infrastructure/66-evaluation-system.md#L10 — ## 本章要回答的问题 | existing:SF-2026-ARXIV-2606-27679 | delta:SF-2026-ARXIV-2606-27679 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-27679 |
| SF-2026-ARXIV-2606-27681 | MULTIMODAL-WORLD-MODELS | books/part-03-multimodal-world-models/25-multimodal-world-models.md#L251 — ## State ownership | books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md#L10 — ## 本章要回答的问题 | existing:SF-2026-ARXIV-2606-27681 | delta:SF-2026-ARXIV-2606-27681 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-27681 |
| SF-2026-ARXIV-2606-27683 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#L733 — ## 风险管理而不是一次性认证 | books/part-06-ai-infrastructure/71-multi-tenant.md#L10 — ## 本章要回答的问题 | existing:SF-2026-ARXIV-2606-27683 | delta:SF-2026-ARXIV-2606-27683 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-27683 |
| SF-2026-ARXIV-2606-27704 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#L733 — ## 风险管理而不是一次性认证 | books/part-06-ai-infrastructure/71-multi-tenant.md#L10 — ## 本章要回答的问题 | existing:SF-2026-ARXIV-2606-27704 | delta:SF-2026-ARXIV-2606-27704 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-27704 |
| SF-2026-ARXIV-2606-27709 | TRAIN-DATA | books/part-04-training-system/27-data.md#L487 — ### 从 sample provenance 到训练生命周期 lineage | books/part-04-training-system/28-pretraining.md#L10 — ## 本章要回答的问题 | existing:SF-2026-ARXIV-2606-27709 | delta:SF-2026-ARXIV-2606-27709 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-27709 |
| SF-2026-ARXIV-2606-27732 | MULTIMODAL-GENERATIVE-PARADIGMS | books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md#L276 — ## Cache、rollback 与 exactness | books/part-03-multimodal-world-models/25-multimodal-world-models.md#L10 — ## 本章要回答的问题 | existing:SF-2026-ARXIV-2606-27732 | delta:SF-2026-ARXIV-2606-27732 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-27732 |
| SF-2026-ARXIV-2606-27739 | TRAIN-GRPO | books/part-04-training-system/33-grpo.md#L930 — ### 从一个终局标量到 Typed Credit：Reward 必须匹配决策边界 | books/part-04-training-system/32-ppo.md#L10 — ## 本章要回答的问题 | existing:SF-2026-ARXIV-2606-27739 | delta:SF-2026-ARXIV-2606-27739 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-27739 |
| SF-2026-ARXIV-2606-27743 | INFER-SCHEDULING | books/part-05-inference-system/56-inference-scheduling.md#L343 — ### Semantic Predicate 的 Token Cost 应成为 Query-planner State | books/part-05-inference-system/55-pd-disaggregation.md#L10 — ## 本章要回答的问题 | existing:SF-2026-ARXIV-2606-27743 | delta:SF-2026-ARXIV-2606-27743 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-27743 |
| SF-2026-ARXIV-2606-27757 | AGENT-PLANNING | books/part-07-agent/79-planning.md#L271 — ## 完成证据与 Verification | books/part-07-agent/78-tool-calling.md#L10 — ## 本章要回答的问题 | existing:SF-2026-ARXIV-2606-27757 | delta:SF-2026-ARXIV-2606-27757 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-27757 |
| SF-2026-ARXIV-2606-27780 | MULTIMODAL-WORLD-MODELS | books/part-03-multimodal-world-models/25-multimodal-world-models.md#L251 — ## State ownership | books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md#L10 — ## 本章要回答的问题 | existing:SF-2026-ARXIV-2606-27780 | delta:SF-2026-ARXIV-2606-27780 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-27780 |
| SF-2026-ARXIV-2606-27797 | TRAIN-DISTRIBUTED-TRAINING | books/part-04-training-system/36-distributed-training.md#L629 — ### 从 Phase 串行到依赖驱动的跨 Phase 重排 | books/part-04-training-system/37-tensor-parallel.md#L10 — ## 本章要回答的问题 | existing:SF-2026-ARXIV-2606-27797 | delta:SF-2026-ARXIV-2606-27797 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-27797 |
| SF-2026-ARXIV-2606-27806 | AGENT-PLANNING | books/part-07-agent/79-planning.md#L271 — ## 完成证据与 Verification | books/part-07-agent/78-tool-calling.md#L10 — ## 本章要回答的问题 | existing:SF-2026-ARXIV-2606-27806 | delta:SF-2026-ARXIV-2606-27806 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-27806 |
| SF-2026-ARXIV-2606-27814 | TRAIN-GRPO | books/part-04-training-system/33-grpo.md#L930 — ### 从一个终局标量到 Typed Credit：Reward 必须匹配决策边界 | books/part-04-training-system/32-ppo.md#L10 — ## 本章要回答的问题 | existing:SF-2026-ARXIV-2606-27814 | delta:SF-2026-ARXIV-2606-27814 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-27814 |
| SF-2026-ARXIV-2606-27826 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#L353 — ### Evaluator 可以主动制造 Probe，但不能冒充被动观察 | books/part-06-ai-infrastructure/67-monitoring.md#L10 — ## 本章要回答的问题 | existing:SF-2026-ARXIV-2606-27826 | delta:SF-2026-ARXIV-2606-27826 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-27826 |
| SF-2026-ARXIV-2606-27841 | PLATFORM-COST | books/part-06-ai-infrastructure/70-cost.md#L107 — ## 利用率与有效利用率 | books/part-06-ai-infrastructure/69-trace.md#L10 — ## 本章要回答的问题 | existing:SF-2026-ARXIV-2606-27841 | delta:SF-2026-ARXIV-2606-27841 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-27841 |
| SF-2026-ARXIV-2606-27866 | MODEL-MOE | books/part-02-model/21-moe.md#L491 — ### 从局部结果到可执行的系统边界 | books/part-02-model/20-sampling.md#L10 — ## 本章要回答的问题 | existing:SF-2026-ARXIV-2606-27866 | delta:SF-2026-ARXIV-2606-27866 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-27866 |
| SF-2026-ARXIV-2606-27906 | INFER-REQUEST-LIFECYCLE | books/part-05-inference-system/42-what-happens-during-inference.md#L80 — ## 请求状态机 | books/part-05-inference-system/43-prefill.md#L10 — ## 本章要回答的问题 | existing:SF-2026-ARXIV-2606-27906 | delta:SF-2026-ARXIV-2606-27906 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-27906 |
| SF-2026-ARXIV-2606-27934 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#L353 — ### Evaluator 可以主动制造 Probe，但不能冒充被动观察 | books/part-06-ai-infrastructure/67-monitoring.md#L10 — ## 本章要回答的问题 | existing:SF-2026-ARXIV-2606-27934 | delta:SF-2026-ARXIV-2606-27934 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-27934 |
| SF-2026-ARXIV-2606-27936 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#L733 — ## 风险管理而不是一次性认证 | books/part-06-ai-infrastructure/71-multi-tenant.md#L10 — ## 本章要回答的问题 | existing:SF-2026-ARXIV-2606-27936 | delta:SF-2026-ARXIV-2606-27936 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-27936 |
| SF-2026-ARXIV-2606-27944 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#L733 — ## 风险管理而不是一次性认证 | books/part-06-ai-infrastructure/71-multi-tenant.md#L10 — ## 本章要回答的问题 | existing:SF-2026-ARXIV-2606-27944 | delta:SF-2026-ARXIV-2606-27944 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-27944 |
| SF-2026-ARXIV-2606-27962 | PLATFORM-FOUNDATIONS | books/part-06-ai-infrastructure/57-what-is-ai-platform.md#L118 — ## Paved Road 与 Escape Hatch | books/part-06-ai-infrastructure/58-kubeflow.md#L10 — ## 本章要回答的问题 | existing:SF-2026-ARXIV-2606-27962 | delta:SF-2026-ARXIV-2606-27962 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-27962 |
| SF-2026-ARXIV-2606-27976 | AGENT-RAG | books/part-07-agent/76-rag.md#L35 — ## Offline Ingestion 不是预处理细节 | books/part-07-agent/77-memory.md#L10 — ## 本章要回答的问题 | existing:SF-2026-ARXIV-2606-27976 | delta:SF-2026-ARXIV-2606-27976 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-27976 |
| SF-2026-ARXIV-2606-27997 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#L353 — ### Evaluator 可以主动制造 Probe，但不能冒充被动观察 | books/part-06-ai-infrastructure/67-monitoring.md#L10 — ## 本章要回答的问题 | existing:SF-2026-ARXIV-2606-27997 | delta:SF-2026-ARXIV-2606-27997 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-27997 |
| SF-2026-ARXIV-2606-28011 | AGENT-WORKFLOW | books/part-07-agent/81-workflow.md#L36 — ## State Machine 是基本模型 | books/part-07-agent/80-reflection.md#L10 — ## 本章要回答的问题 | existing:SF-2026-ARXIV-2606-28011 | delta:SF-2026-ARXIV-2606-28011 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-28011 |
| SF-2026-ARXIV-2606-28013 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#L353 — ### Evaluator 可以主动制造 Probe，但不能冒充被动观察 | books/part-06-ai-infrastructure/67-monitoring.md#L10 — ## 本章要回答的问题 | existing:SF-2026-ARXIV-2606-28013 | delta:SF-2026-ARXIV-2606-28013 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-28013 |
| SF-2026-ARXIV-2606-28037 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#L353 — ### Evaluator 可以主动制造 Probe，但不能冒充被动观察 | books/part-06-ai-infrastructure/67-monitoring.md#L10 — ## 本章要回答的问题 | existing:SF-2026-ARXIV-2606-28037 | delta:SF-2026-ARXIV-2606-28037 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-28037 |
| SF-2026-ARXIV-2606-28050 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#L353 — ### Evaluator 可以主动制造 Probe，但不能冒充被动观察 | books/part-06-ai-infrastructure/67-monitoring.md#L10 — ## 本章要回答的问题 | existing:SF-2026-ARXIV-2606-28050 | delta:SF-2026-ARXIV-2606-28050 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-28050 |
| SF-2026-ARXIV-2606-28061 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#L733 — ## 风险管理而不是一次性认证 | books/part-06-ai-infrastructure/71-multi-tenant.md#L10 — ## 本章要回答的问题 | existing:SF-2026-ARXIV-2606-28061 | delta:SF-2026-ARXIV-2606-28061 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-28061 |
| SF-2026-ARXIV-2606-28070 | PLATFORM-FOUNDATIONS | books/part-06-ai-infrastructure/57-what-is-ai-platform.md#L118 — ## Paved Road 与 Escape Hatch | books/part-06-ai-infrastructure/58-kubeflow.md#L10 — ## 本章要回答的问题 | existing:SF-2026-ARXIV-2606-28070 | delta:SF-2026-ARXIV-2606-28070 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-28070 |
| SF-2026-ARXIV-2606-28116 | PLATFORM-MONITORING | books/part-06-ai-infrastructure/67-monitoring.md#L206 — ## Monitoring 也会改变系统 | books/part-06-ai-infrastructure/66-evaluation-system.md#L10 — ## 本章要回答的问题 | existing:SF-2026-ARXIV-2606-28116 | delta:SF-2026-ARXIV-2606-28116 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-28116 |
| SF-2026-ARXIV-2606-28128 | MULTIMODAL-WORLD-MODELS | books/part-03-multimodal-world-models/25-multimodal-world-models.md#L251 — ## State ownership | books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md#L10 — ## 本章要回答的问题 | existing:SF-2026-ARXIV-2606-28128 | delta:SF-2026-ARXIV-2606-28128 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-28128 |
| SF-2026-ARXIV-2606-28153 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#L733 — ## 风险管理而不是一次性认证 | books/part-06-ai-infrastructure/71-multi-tenant.md#L10 — ## 本章要回答的问题 | existing:SF-2026-ARXIV-2606-28153 | delta:SF-2026-ARXIV-2606-28153 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-28153 |
| SF-2026-ARXIV-2606-28187 | AGENT-MULTI-AGENT | books/part-07-agent/82-multi-agent.md#L283 — ### 共享 Repository 需要 Commitment Protocol，不只是更多消息 | books/part-07-agent/81-workflow.md#L10 — ## 本章要回答的问题 | existing:SF-2026-ARXIV-2606-28187 | delta:SF-2026-ARXIV-2606-28187 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-28187 |
| SF-2026-ARXIV-2606-28235 | AGENT-PLATFORM | books/part-07-agent/84-agent-platform.md#L399 — ## Agent Runtime State Machine | books/part-07-agent/83-mcp.md#L10 — ## 本章要回答的问题 | existing:SF-2026-ARXIV-2606-28235 | delta:SF-2026-ARXIV-2606-28235 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-28235 |
| SF-2026-ARXIV-2606-28276 | MULTIMODAL-EMBODIED-VLA | books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#L305 — ## Safety envelope | books/part-03-multimodal-world-models/25-multimodal-world-models.md#L10 — ## 本章要回答的问题 | existing:SF-2026-ARXIV-2606-28276 | delta:SF-2026-ARXIV-2606-28276 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-28276 |
| SF-2026-ARXIV-2606-28277 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#L353 — ### Evaluator 可以主动制造 Probe，但不能冒充被动观察 | books/part-06-ai-infrastructure/67-monitoring.md#L10 — ## 本章要回答的问题 | existing:SF-2026-ARXIV-2606-28277 | delta:SF-2026-ARXIV-2606-28277 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-28277 |
| SF-2026-ARXIV-2606-28279 | AGENT-WORKFLOW | books/part-07-agent/81-workflow.md#L36 — ## State Machine 是基本模型 | books/part-07-agent/80-reflection.md#L10 — ## 本章要回答的问题 | existing:SF-2026-ARXIV-2606-28279 | delta:SF-2026-ARXIV-2606-28279 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-28279 |
| SF-2026-ARXIV-2606-28322 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#L353 — ### Evaluator 可以主动制造 Probe，但不能冒充被动观察 | books/part-06-ai-infrastructure/67-monitoring.md#L10 — ## 本章要回答的问题 | existing:SF-2026-ARXIV-2606-28322 | delta:SF-2026-ARXIV-2606-28322 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-28322 |
| SF-2026-ARXIV-2606-28430 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#L353 — ### Evaluator 可以主动制造 Probe，但不能冒充被动观察 | books/part-06-ai-infrastructure/67-monitoring.md#L10 — ## 本章要回答的问题 | existing:SF-2026-ARXIV-2606-28430 | delta:SF-2026-ARXIV-2606-28430 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-28430 |
| SF-2026-ARXIV-2606-28433 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#L353 — ### Evaluator 可以主动制造 Probe，但不能冒充被动观察 | books/part-06-ai-infrastructure/67-monitoring.md#L10 — ## 本章要回答的问题 | existing:SF-2026-ARXIV-2606-28433 | delta:SF-2026-ARXIV-2606-28433 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-28433 |
| SF-2026-ARXIV-2606-28434 | AGENT-MEMORY | books/part-07-agent/77-memory.md#L252 — ## Consolidation 与 Forgetting | books/part-07-agent/76-rag.md#L10 — ## 本章要回答的问题 | existing:SF-2026-ARXIV-2606-28434 | delta:SF-2026-ARXIV-2606-28434 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-28434 |
| SF-2026-ARXIV-2606-28436 | TRAIN-GRPO | books/part-04-training-system/33-grpo.md#L930 — ### 从一个终局标量到 Typed Credit：Reward 必须匹配决策边界 | books/part-04-training-system/32-ppo.md#L10 — ## 本章要回答的问题 | existing:SF-2026-ARXIV-2606-28436 | delta:SF-2026-ARXIV-2606-28436 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-28436 |
| SF-2026-ARXIV-2606-28438 | TRAIN-DATA | books/part-04-training-system/27-data.md#L487 — ### 从 sample provenance 到训练生命周期 lineage | books/part-04-training-system/28-pretraining.md#L10 — ## 本章要回答的问题 | existing:SF-2026-ARXIV-2606-28438 | delta:SF-2026-ARXIV-2606-28438 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-28438 |
| SF-2026-ARXIV-2606-28455 | MULTIMODAL-WORLD-MODELS | books/part-03-multimodal-world-models/25-multimodal-world-models.md#L251 — ## State ownership | books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md#L10 — ## 本章要回答的问题 | existing:SF-2026-ARXIV-2606-28455 | delta:SF-2026-ARXIV-2606-28455 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-28455 |
| SF-2026-ARXIV-2606-28471 | TRAIN-DATA | books/part-04-training-system/27-data.md#L487 — ### 从 sample provenance 到训练生命周期 lineage | books/part-04-training-system/28-pretraining.md#L10 — ## 本章要回答的问题 | existing:SF-2026-ARXIV-2606-28471 | delta:SF-2026-ARXIV-2606-28471 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-28471 |
| SF-2026-ARXIV-2606-28479 | TRAIN-LORA | books/part-04-training-system/30-lora.md#L342 — ## Checkpoint 与可复现性 | books/part-04-training-system/29-sft.md#L10 — ## 本章要回答的问题 | existing:SF-2026-ARXIV-2606-28479 | delta:SF-2026-ARXIV-2606-28479 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-28479 |
| SF-2026-ARXIV-2606-28480 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#L353 — ### Evaluator 可以主动制造 Probe，但不能冒充被动观察 | books/part-06-ai-infrastructure/67-monitoring.md#L10 — ## 本章要回答的问题 | existing:SF-2026-ARXIV-2606-28480 | delta:SF-2026-ARXIV-2606-28480 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-28480 |
| SF-2026-ARXIV-2606-28514 | AGENT-MULTI-AGENT | books/part-07-agent/82-multi-agent.md#L283 — ### 共享 Repository 需要 Commitment Protocol，不只是更多消息 | books/part-07-agent/81-workflow.md#L10 — ## 本章要回答的问题 | existing:SF-2026-ARXIV-2606-28514 | delta:SF-2026-ARXIV-2606-28514 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-28514 |
| SF-2026-ARXIV-2606-28529 | INFER-REQUEST-LIFECYCLE | books/part-05-inference-system/42-what-happens-during-inference.md#L80 — ## 请求状态机 | books/part-05-inference-system/43-prefill.md#L10 — ## 本章要回答的问题 | existing:SF-2026-ARXIV-2606-28529 | delta:SF-2026-ARXIV-2606-28529 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-28529 |
| SF-2026-ARXIV-2606-28551 | TRAIN-DATA | books/part-04-training-system/27-data.md#L487 — ### 从 sample provenance 到训练生命周期 lineage | books/part-04-training-system/28-pretraining.md#L10 — ## 本章要回答的问题 | existing:SF-2026-ARXIV-2606-28551 | delta:SF-2026-ARXIV-2606-28551 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-28551 |
| SF-2026-ARXIV-2606-28562 | TRAIN-GRPO | books/part-04-training-system/33-grpo.md#L930 — ### 从一个终局标量到 Typed Credit：Reward 必须匹配决策边界 | books/part-04-training-system/32-ppo.md#L10 — ## 本章要回答的问题 | existing:SF-2026-ARXIV-2606-28562 | delta:SF-2026-ARXIV-2606-28562 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-28562 |
| SF-2026-ARXIV-2606-28565 | INFER-REQUEST-LIFECYCLE | books/part-05-inference-system/42-what-happens-during-inference.md#L80 — ## 请求状态机 | books/part-05-inference-system/43-prefill.md#L10 — ## 本章要回答的问题 | existing:SF-2026-ARXIV-2606-28565 | delta:SF-2026-ARXIV-2606-28565 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-28565 |
| SF-2026-ARXIV-2606-28574 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#L353 — ### Evaluator 可以主动制造 Probe，但不能冒充被动观察 | books/part-06-ai-infrastructure/67-monitoring.md#L10 — ## 本章要回答的问题 | existing:SF-2026-ARXIV-2606-28574 | delta:SF-2026-ARXIV-2606-28574 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-28574 |
| SF-2026-ARXIV-2606-28615 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#L353 — ### Evaluator 可以主动制造 Probe，但不能冒充被动观察 | books/part-06-ai-infrastructure/67-monitoring.md#L10 — ## 本章要回答的问题 | existing:SF-2026-ARXIV-2606-28615 | delta:SF-2026-ARXIV-2606-28615 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-28615 |
| SF-2026-ARXIV-2606-28639 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#L733 — ## 风险管理而不是一次性认证 | books/part-06-ai-infrastructure/71-multi-tenant.md#L10 — ## 本章要回答的问题 | existing:SF-2026-ARXIV-2606-28639 | delta:SF-2026-ARXIV-2606-28639 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-28639 |
| SF-2026-ARXIV-2606-28649 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#L733 — ## 风险管理而不是一次性认证 | books/part-06-ai-infrastructure/71-multi-tenant.md#L10 — ## 本章要回答的问题 | existing:SF-2026-ARXIV-2606-28649 | delta:SF-2026-ARXIV-2606-28649 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-28649 |
| SF-2026-ARXIV-2606-28661 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#L353 — ### Evaluator 可以主动制造 Probe，但不能冒充被动观察 | books/part-06-ai-infrastructure/67-monitoring.md#L10 — ## 本章要回答的问题 | existing:SF-2026-ARXIV-2606-28661 | delta:SF-2026-ARXIV-2606-28661 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-28661 |

<!-- existing:SF-2026-ARXIV-2606-27632:start -->
Ch72 已把不可信内容、model context 与 tool/action authority 分离，并要求 model 外的 fail-closed gate。 本 family 的 source-specific delta 为：把 adversarial robustness、agentic tool use 与 safety release evaluation 绑定为同一模型发布合同。 Fresh adjacent review at books/part-06-ai-infrastructure/71-multi-tenant.md found no competing owner.
<!-- existing:SF-2026-ARXIV-2606-27632:end -->

<!-- delta:SF-2026-ARXIV-2606-27632:start -->
把 adversarial robustness、agentic tool use 与 safety release evaluation 绑定为同一模型发布合同。
<!-- delta:SF-2026-ARXIV-2606-27632:end -->

<!-- books-review:SF-2026-ARXIV-2606-27632:start -->
Principle Reuse; No Change — Existing Coverage. Across these evaluations, Yuvion LLM demonstrates clear advantages on safety-focused benchmarks and particularly strong robustness under adversarial conditions, while maintaining solid overall capability.
<!-- books-review:SF-2026-ARXIV-2606-27632:end -->

<!-- existing:SF-2026-ARXIV-2606-27634:start -->
The monitoring owner already marks checkpoint-bound monitors stale and requires re-alignment, retraining or abstention; sequential LoRA/reference-set drift is an instance, not a new contract.
<!-- existing:SF-2026-ARXIV-2606-27634:end -->

<!-- delta:SF-2026-ARXIV-2606-27634:start -->
把 sequential LoRA personalization 的 checkpoint、reference-set drift 与遗忘监控绑定为持续适配合同。
<!-- delta:SF-2026-ARXIV-2606-27634:end -->

<!-- books-review:SF-2026-ARXIV-2606-27634:start -->
Principle Reuse; No Change — Existing Coverage. However, personalization requires models to adapt over time to evolving user- or task-specific data, placing them in a continual learning setting.
<!-- books-review:SF-2026-ARXIV-2606-27634:end -->

<!-- existing:SF-2026-ARXIV-2606-27650:start -->
Ch84 已把 workspace/runtime、intent、acceptance predicate、trace/replay 与 promotion gate 分开。 本 family 的 source-specific delta 为：把城市级 agent environment、离线 policy compilation、人口/地理 grounding 与可复算 rollout 统一为 simulation infrastructure。 Fresh adjacent review at books/part-07-agent/83-mcp.md found no competing owner.
<!-- existing:SF-2026-ARXIV-2606-27650:end -->

<!-- delta:SF-2026-ARXIV-2606-27650:start -->
把城市级 agent environment、离线 policy compilation、人口/地理 grounding 与可复算 rollout 统一为 simulation infrastructure。
<!-- delta:SF-2026-ARXIV-2606-27650:end -->

<!-- books-review:SF-2026-ARXIV-2606-27650:start -->
Principle Reuse; No Change — Existing Coverage. These cases support GenWorld as a reproducible platform for grounded and scalable LLM-agent studies, while calibrated forecasting for traffic, evacuation, or policy outcomes remains future work.
<!-- books-review:SF-2026-ARXIV-2606-27650:end -->

<!-- existing:SF-2026-ARXIV-2606-27669:start -->
Ch66 已把 subject identity、EvalSpec、scorer、slice 与 release decision 分成版本化证据对象。 本 family 的 source-specific delta 为：把 deep-search 的 ambiguity detection、clarification action、task utility 与交互成本分离成评估合同。 Fresh adjacent review at books/part-06-ai-infrastructure/67-monitoring.md found no competing owner.
<!-- existing:SF-2026-ARXIV-2606-27669:end -->

<!-- delta:SF-2026-ARXIV-2606-27669:start -->
把 deep-search 的 ambiguity detection、clarification action、task utility 与交互成本分离成评估合同。
<!-- delta:SF-2026-ARXIV-2606-27669:end -->

<!-- books-review:SF-2026-ARXIV-2606-27669:start -->
Principle Reuse; No Change — Existing Coverage. However, existing benchmarks often assume that user queries are complete and explicit, overlooking the fact that real-world search requests are frequently vague, underspecified, or even factually incorrect.
<!-- books-review:SF-2026-ARXIV-2606-27669:end -->

<!-- existing:SF-2026-ARXIV-2606-27679:start -->
Ch67 已把 monitor 定义为需校准的 observe/alert sensor，并要求 checkpoint 变化后 stale/abstain。 本 family 的 source-specific delta 为：给 probe uncertainty monitor 建立 feature、label construction、prompt 与 distribution-shift transfer 的可迁移边界。 Fresh adjacent review at books/part-06-ai-infrastructure/66-evaluation-system.md found no competing owner.
<!-- existing:SF-2026-ARXIV-2606-27679:end -->

<!-- delta:SF-2026-ARXIV-2606-27679:start -->
给 probe uncertainty monitor 建立 feature、label construction、prompt 与 distribution-shift transfer 的可迁移边界。
<!-- delta:SF-2026-ARXIV-2606-27679:end -->

<!-- books-review:SF-2026-ARXIV-2606-27679:start -->
Principle Reuse; No Change — Existing Coverage. However, under distribution shift, structured and compressed features are more robust, suggesting that in-domain performance alone is insufficient to measure progress.
<!-- books-review:SF-2026-ARXIV-2606-27679:end -->

<!-- existing:SF-2026-ARXIV-2606-27681:start -->
The world-model owner separates latent state from physical commit, but does not require state-only mediation that makes representation quality identifiable.
<!-- existing:SF-2026-ARXIV-2606-27681:end -->

<!-- delta:SF-2026-ARXIV-2606-27681:start -->
用 strict mediation 让 textual belief state 成为唯一可测试的预测状态，阻断 history bypass。
<!-- delta:SF-2026-ARXIV-2606-27681:end -->

<!-- books-review:SF-2026-ARXIV-2606-27681:start -->
Direct Evolution; Integrate. We formalize why it is necessary, showing that strict mediation makes representation quality empirically testable while history-leaky architectures break this connection.
<!-- books-review:SF-2026-ARXIV-2606-27681:end -->

<!-- existing:SF-2026-ARXIV-2606-27683:start -->
Ch72 已把不可信内容、model context 与 tool/action authority 分离，并要求 model 外的 fail-closed gate。 本 family 的 source-specific delta 为：揭示 API-only black-box unlearning 实际由 relevance router 与 auxiliary models 持有控制权，而非修改远端模型。 Fresh adjacent review at books/part-06-ai-infrastructure/71-multi-tenant.md found no competing owner.
<!-- existing:SF-2026-ARXIV-2606-27683:end -->

<!-- delta:SF-2026-ARXIV-2606-27683:start -->
揭示 API-only black-box unlearning 实际由 relevance router 与 auxiliary models 持有控制权，而非修改远端模型。
<!-- delta:SF-2026-ARXIV-2606-27683:end -->

<!-- books-review:SF-2026-ARXIV-2606-27683:start -->
Principle Reuse; No Change — Existing Coverage. On WMDP, it lowers hazardous knowledge accuracy to 25.68, near random guessing, while preserving MMLU accuracy of 52.67.
<!-- books-review:SF-2026-ARXIV-2606-27683:end -->

<!-- existing:SF-2026-ARXIV-2606-27704:start -->
Ch72 已把不可信内容、model context 与 tool/action authority 分离，并要求 model 外的 fail-closed gate。 本 family 的 source-specific delta 为：把 edge black-box adversarial detection 从模型内部 probe 改为 runtime power sensor，并暴露设备/攻击覆盖边界。 Fresh adjacent review at books/part-06-ai-infrastructure/71-multi-tenant.md found no competing owner.
<!-- existing:SF-2026-ARXIV-2606-27704:end -->

<!-- delta:SF-2026-ARXIV-2606-27704:start -->
把 edge black-box adversarial detection 从模型内部 probe 改为 runtime power sensor，并暴露设备/攻击覆盖边界。
<!-- delta:SF-2026-ARXIV-2606-27704:end -->

<!-- books-review:SF-2026-ARXIV-2606-27704:start -->
Principle Reuse; No Change — Existing Coverage. Across 318,400 total test inputs, AdvScan detects 99.984% of AEs with only 40 false negatives and zero false positives.
<!-- books-review:SF-2026-ARXIV-2606-27704:end -->

<!-- existing:SF-2026-ARXIV-2606-27709:start -->
Ch27 已让 sample provenance、mixture/admission 与训练生命周期 lineage 共同决定数据能否进入训练。 本 family 的 source-specific delta 为：证明 warmth fine-tuning 的 jailbreak regression 取决于 persona/data construction，而非同理性目标本身必然削弱安全。 Fresh adjacent review at books/part-04-training-system/28-pretraining.md found no competing owner.
<!-- existing:SF-2026-ARXIV-2606-27709:end -->

<!-- delta:SF-2026-ARXIV-2606-27709:start -->
证明 warmth fine-tuning 的 jailbreak regression 取决于 persona/data construction，而非同理性目标本身必然削弱安全。
<!-- delta:SF-2026-ARXIV-2606-27709:end -->

<!-- books-review:SF-2026-ARXIV-2606-27709:start -->
Principle Reuse; No Change — Existing Coverage. These results show that safer empathetic fine-tuning is achievable through data design alone, without safety labels, harm detectors, or changes to the training objective.
<!-- books-review:SF-2026-ARXIV-2606-27709:end -->

<!-- existing:SF-2026-ARXIV-2606-27732:start -->
The generation owner covers provisional commit and cache invalidation, but not an asymmetric right-context side path coexisting with a causal cache.
<!-- existing:SF-2026-ARXIV-2606-27732:end -->

<!-- delta:SF-2026-ARXIV-2606-27732:start -->
用 asymmetric bidirectional sidecar 重构 diffusion-LM 的右上下文、KV cache 与 parallel decode 取舍。
<!-- delta:SF-2026-ARXIV-2606-27732:end -->

<!-- books-review:SF-2026-ARXIV-2606-27732:start -->
Direct Evolution; Integrate. Comprehensive experiments on continued pretraining of Qwen3-1.7B with 60B tokens demonstrate that R2LM achieves $2.4\times$ to $12.9\times$ higher throughput than bidirectional dLLMs and $1.9\times$ to $2.9\times$ speedup over AR baselines in batch serving through parallel decoding with KV caching, while exceeding the causal baseline on most benchmarks and surpassing the bidirectional dLLM on average.
<!-- books-review:SF-2026-ARXIV-2606-27732:end -->

<!-- existing:SF-2026-ARXIV-2606-27739:start -->
Ch33 已分离 trajectory owner、outcome verifier、teacher guidance 与 typed credit，避免 teacher 获得 reward sign authority。 本 family 的 source-specific delta 为：把 outcome-supervised PRM 的 step credit assignment 表述为 weakest-link multiple-instance learning。 Fresh adjacent review at books/part-04-training-system/32-ppo.md found no competing owner.
<!-- existing:SF-2026-ARXIV-2606-27739:end -->

<!-- delta:SF-2026-ARXIV-2606-27739:start -->
把 outcome-supervised PRM 的 step credit assignment 表述为 weakest-link multiple-instance learning。
<!-- delta:SF-2026-ARXIV-2606-27739:end -->

<!-- books-review:SF-2026-ARXIV-2606-27739:start -->
Principle Reuse; No Change — Existing Coverage. exact-v1 的结论只覆盖《The Weakest Link Tells It All: Outcome-Supervised Process Reward Modeling via Learnable Credit Assignment》在 3 Analysis; 3.3 Theoretical Analysis; 5 Experiments 声明的实验；它没有证明跨 model family、hardware/runtime、数据分布或未测 failure mode 的普遍成立。
<!-- books-review:SF-2026-ARXIV-2606-27739:end -->

<!-- existing:SF-2026-ARXIV-2606-27743:start -->
Ch56 已让 request budget、queue state、goodput 与 fallback 共同约束 compute allocation。 本 family 的 source-specific delta 为：把 layer/head/token compute footprint 变成由输入与实时资源预算共同控制的 runtime policy state。 Fresh adjacent review at books/part-05-inference-system/55-pd-disaggregation.md found no competing owner.
<!-- existing:SF-2026-ARXIV-2606-27743:end -->

<!-- delta:SF-2026-ARXIV-2606-27743:start -->
把 layer/head/token compute footprint 变成由输入与实时资源预算共同控制的 runtime policy state。
<!-- delta:SF-2026-ARXIV-2606-27743:end -->

<!-- books-review:SF-2026-ARXIV-2606-27743:start -->
Principle Reuse; No Change — Existing Coverage. A single L2A model traces the entire compute-accuracy Pareto frontier on Llama-3-8B and Qwen-3-4B: at up to 34% realized layer sparsity, it stays within 0.6% of the dense baseline on GSM8K, with the same gap holding zero-shot on out-of-distribution tasks, while every static or heuristic baseline requires a separately tuned model and still drops by 5-10% at comparable inference time.
<!-- books-review:SF-2026-ARXIV-2606-27743:end -->

<!-- existing:SF-2026-ARXIV-2606-27757:start -->
Ch79 已区分 plan proposal、pre-commit verifier、environment feedback 与 executable commit。 本 family 的 source-specific delta 为：把 symbolic verifier、reachability recognizer 与 revision loop 放到 long-horizon plan 的显式控制流。 Fresh adjacent review at books/part-07-agent/78-tool-calling.md found no competing owner.
<!-- existing:SF-2026-ARXIV-2606-27757:end -->

<!-- delta:SF-2026-ARXIV-2606-27757:start -->
把 symbolic verifier、reachability recognizer 与 revision loop 放到 long-horizon plan 的显式控制流。
<!-- delta:SF-2026-ARXIV-2606-27757:end -->

<!-- books-review:SF-2026-ARXIV-2606-27757:start -->
Principle Reuse; No Change — Existing Coverage. exact-v1 的结论只覆盖《Towards Reliable and Robust LLM Planning: Symbolic Feedback-Driven Iterative Self-Refinement Framework》在 IV EXPERIMENTS; IV-A Experimental Settings; IV-D Analysis of Planning Length 声明的实验；它没有证明跨 model family、hardware/runtime、数据分布或未测 failure mode 的普遍成立。
<!-- books-review:SF-2026-ARXIV-2606-27757:end -->

<!-- existing:SF-2026-ARXIV-2606-27780:start -->
Ch25 已分离 belief/latent state、action-conditioned transition、physical truth 与 commit authority。 本 family 的 source-specific delta 为：给 graph world-model rollout 建立 topology/model factor 分解与 dynamic-edge error feedback contract。 Fresh adjacent review at books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md found no competing owner.
<!-- existing:SF-2026-ARXIV-2606-27780:end -->

<!-- delta:SF-2026-ARXIV-2606-27780:start -->
给 graph world-model rollout 建立 topology/model factor 分解与 dynamic-edge error feedback contract。
<!-- delta:SF-2026-ARXIV-2606-27780:end -->

<!-- books-review:SF-2026-ARXIV-2606-27780:start -->
Principle Reuse; No Change — Existing Coverage. Our results characterize when graph world models remain reliable under autoregressive planning and when topology makes them fail.
<!-- books-review:SF-2026-ARXIV-2606-27780:end -->

<!-- existing:SF-2026-ARXIV-2606-27797:start -->
The distributed-training owner covers model/optimizer partitioning, but not independent teacher-inference and student-training topology plans joined by a versioned handoff.
<!-- existing:SF-2026-ARXIV-2606-27797:end -->

<!-- delta:SF-2026-ARXIV-2606-27797:start -->
按 teacher/student 不对称分别选择模型分片与拓扑通信，改变 KD runtime partition contract。
<!-- delta:SF-2026-ARXIV-2606-27797:end -->

<!-- books-review:SF-2026-ARXIV-2606-27797:start -->
Direct Evolution; Integrate. exact-v1 的结论只覆盖《Optimizing Teacher-Student Partitioning for Scalable Knowledge Distillation on HPC Systems》在 3 Testing Setup; 4 GKD Analysis and Improvements; 4.1 Experimental Results 声明的实验；它没有证明跨 model family、hardware/runtime、数据分布或未测 failure mode 的普遍成立。
<!-- books-review:SF-2026-ARXIV-2606-27797:end -->

<!-- existing:SF-2026-ARXIV-2606-27806:start -->
The planning owner separates proposal, validation and commit, but lacks a learned transition-disagreement gate that requests targeted plan revision without taking action authority.
<!-- existing:SF-2026-ARXIV-2606-27806:end -->

<!-- delta:SF-2026-ARXIV-2606-27806:start -->
以 parametric transition model 校验 agent imagined delta，并把 disagreement 变成 targeted revision gate。
<!-- delta:SF-2026-ARXIV-2606-27806:end -->

<!-- books-review:SF-2026-ARXIV-2606-27806:start -->
Direct Evolution; Integrate. These results suggest that lightweight parametric transition models can serve as effective grounding mechanisms for language-agent planning without replacing semantic reasoning.
<!-- books-review:SF-2026-ARXIV-2606-27806:end -->

<!-- existing:SF-2026-ARXIV-2606-27814:start -->
Ch33 已分离 trajectory owner、outcome verifier、teacher guidance 与 typed credit，避免 teacher 获得 reward sign authority。 本 family 的 source-specific delta 为：在 multi-turn agent training 中按 competence/turn state 退火切换 on-policy distillation 与 environment reward。 Fresh adjacent review at books/part-04-training-system/32-ppo.md found no competing owner.
<!-- existing:SF-2026-ARXIV-2606-27814:end -->

<!-- delta:SF-2026-ARXIV-2606-27814:start -->
在 multi-turn agent training 中按 competence/turn state 退火切换 on-policy distillation 与 environment reward。
<!-- delta:SF-2026-ARXIV-2606-27814:end -->

<!-- books-review:SF-2026-ARXIV-2606-27814:start -->
Principle Reuse; No Change — Existing Coverage. Experiments on ALFWorld, WebShop, and Search-QA show that ATOD consistently outperforms competing post-training baselines: across the three student sizes, ATOD improves average success rate by 4.16 points over OPD and 23.62 points over GRPO, while surpassing the corresponding teacher models by 2.16 points.
<!-- books-review:SF-2026-ARXIV-2606-27814:end -->

<!-- existing:SF-2026-ARXIV-2606-27826:start -->
Ch66 已把 subject identity、EvalSpec、scorer、slice 与 release decision 分成版本化证据对象。 本 family 的 source-specific delta 为：把 embodied-agent goal success 与未明示社会规范的自主识别/遵守拆成渐进 guidance evaluation contract。 Fresh adjacent review at books/part-06-ai-infrastructure/67-monitoring.md found no competing owner.
<!-- existing:SF-2026-ARXIV-2606-27826:end -->

<!-- delta:SF-2026-ARXIV-2606-27826:start -->
把 embodied-agent goal success 与未明示社会规范的自主识别/遵守拆成渐进 guidance evaluation contract。
<!-- delta:SF-2026-ARXIV-2606-27826:end -->

<!-- books-review:SF-2026-ARXIV-2606-27826:start -->
Principle Reuse; No Change — Existing Coverage. NormAct therefore supports the development of embodied agents that pursue everyday goals while proactively respecting unstated social norms.
<!-- books-review:SF-2026-ARXIV-2606-27826:end -->

<!-- existing:SF-2026-ARXIV-2606-27841:start -->
The cost owner models offered load and whole-run energy, but does not expose layer/operator measurement identity before architecture-level recomposition.
<!-- existing:SF-2026-ARXIV-2606-27841:end -->

<!-- delta:SF-2026-ARXIV-2606-27841:start -->
把 inference energy estimation 从整模型 proxy 拆成可跨任务/架构迁移的 layer-wise measurement contract。
<!-- delta:SF-2026-ARXIV-2606-27841:end -->

<!-- books-review:SF-2026-ARXIV-2606-27841:start -->
Direct Evolution; Integrate. We further show that layer-wise decomposition generalize to new tasks without complete retraining, by leveraging shared layers across architectures.
<!-- books-review:SF-2026-ARXIV-2606-27841:end -->

<!-- existing:SF-2026-ARXIV-2606-27866:start -->
The MoE owner already defines a shared checkpoint plus sampled subnet profiles, independent quality envelopes and online budget selection; nested intra-expert pruning is covered.
<!-- existing:SF-2026-ARXIV-2606-27866:end -->

<!-- delta:SF-2026-ARXIV-2606-27866:start -->
把一次性 MoE compression artifact 改成 nested subnet family 与可在线切换的 budget state。
<!-- delta:SF-2026-ARXIV-2606-27866:end -->

<!-- books-review:SF-2026-ARXIV-2606-27866:start -->
Principle Reuse; No Change — Existing Coverage. Specifically, on Qwen2-57B-A14B, our method retains ~99.8% of base performance while pruning 50% of routed expert parameters even without fine-tuning.
<!-- books-review:SF-2026-ARXIV-2606-27866:end -->

<!-- existing:SF-2026-ARXIV-2606-27906:start -->
The inference lifecycle names prefill/decode/request state, but does not bind mobile vision/prefill/decode placement and thermal phase to one hardware-specific record.
<!-- existing:SF-2026-ARXIV-2606-27906:end -->

<!-- delta:SF-2026-ARXIV-2606-27906:start -->
以真实 mobile SoC 证据拆开 vision encoder、prefill、decode、cache 与 thermal phase 的 backend placement。
<!-- delta:SF-2026-ARXIV-2606-27906:end -->

<!-- books-review:SF-2026-ARXIV-2606-27906:start -->
Direct Evolution; Integrate. Using FastVLM-0.5B as an end-to-end case study, together with encoder-only measurements across four architecture families, we show that phase matters: NPU execution is highly phase-dependent, delivering 1.64x speedup for prefill but only 1.18x for decode, while vision encoders achieve 20-45x speedups over CPU.
<!-- books-review:SF-2026-ARXIV-2606-27906:end -->

<!-- existing:SF-2026-ARXIV-2606-27934:start -->
Ch66 已把 subject identity、EvalSpec、scorer、slice 与 release decision 分成版本化证据对象。 本 family 的 source-specific delta 为：用 hash-linked measurement/evidence graph 与 output-derived challenge 让硬件 benchmark 可离线验证。 Fresh adjacent review at books/part-06-ai-infrastructure/67-monitoring.md found no competing owner.
<!-- existing:SF-2026-ARXIV-2606-27934:end -->

<!-- delta:SF-2026-ARXIV-2606-27934:start -->
用 hash-linked measurement/evidence graph 与 output-derived challenge 让硬件 benchmark 可离线验证。
<!-- delta:SF-2026-ARXIV-2606-27934:end -->

<!-- books-review:SF-2026-ARXIV-2606-27934:start -->
Principle Reuse; No Change — Existing Coverage. We then treat the check itself as a security object: a probe seed committed for offline reproducibility is an attack surface, and a probe-aware adversary can hide a corruption in the probe's null space, fooling even a quorum of bit-identical witnesses, while a Fiat-Shamir challenge derived from the claimed output closes this.
<!-- books-review:SF-2026-ARXIV-2606-27934:end -->

<!-- existing:SF-2026-ARXIV-2606-27936:start -->
Ch72 已把不可信内容、model context 与 tool/action authority 分离，并要求 model 外的 fail-closed gate。 本 family 的 source-specific delta 为：证明 agentic open-web resolution 把 mobility re-identification 从专家手工能力改成可规模化 threat model。 Fresh adjacent review at books/part-06-ai-infrastructure/71-multi-tenant.md found no competing owner.
<!-- existing:SF-2026-ARXIV-2606-27936:end -->

<!-- delta:SF-2026-ARXIV-2606-27936:start -->
证明 agentic open-web resolution 把 mobility re-identification 从专家手工能力改成可规模化 threat model。
<!-- delta:SF-2026-ARXIV-2606-27936:end -->

<!-- books-review:SF-2026-ARXIV-2606-27936:start -->
Principle Reuse; No Change — Existing Coverage. We present an end-to-end pipeline in which large language model agents autonomously search the open web, cross-reference public records and social media, and resolve raw coordinate sequences to candidate identities - without human intervention.
<!-- books-review:SF-2026-ARXIV-2606-27936:end -->

<!-- existing:SF-2026-ARXIV-2606-27944:start -->
Ch72 已把不可信内容、model context 与 tool/action authority 分离，并要求 model 外的 fail-closed gate。 本 family 的 source-specific delta 为：以真实 phone/app side effects 揭示 safety awareness 与 execution authorization 分离后的 misuse failure。 Fresh adjacent review at books/part-06-ai-infrastructure/71-multi-tenant.md found no competing owner.
<!-- existing:SF-2026-ARXIV-2606-27944:end -->

<!-- delta:SF-2026-ARXIV-2606-27944:start -->
以真实 phone/app side effects 揭示 safety awareness 与 execution authorization 分离后的 misuse failure。
<!-- delta:SF-2026-ARXIV-2606-27944:end -->

<!-- books-review:SF-2026-ARXIV-2606-27944:start -->
Principle Reuse; No Change — Existing Coverage. Simple defenses curb the overt cases, but the more covert and arguably more damaging threats, such as coordinated review manipulation and fake traffic, remain largely unsolved.
<!-- books-review:SF-2026-ARXIV-2606-27944:end -->

<!-- existing:SF-2026-ARXIV-2606-27962:start -->
Ch57 已把 paved road、escape hatch、artifact/environment identity 与 lifecycle control 分开。 本 family 的 source-specific delta 为：把 embodied simulation 的 environment、trajectory、evaluation、data 与 elastic cloud scheduling 统一成闭环平台。 Fresh adjacent review at books/part-06-ai-infrastructure/58-kubeflow.md found no competing owner.
<!-- existing:SF-2026-ARXIV-2606-27962:end -->

<!-- delta:SF-2026-ARXIV-2606-27962:start -->
把 embodied simulation 的 environment、trajectory、evaluation、data 与 elastic cloud scheduling 统一成闭环平台。
<!-- delta:SF-2026-ARXIV-2606-27962:end -->

<!-- books-review:SF-2026-ARXIV-2606-27962:start -->
Principle Reuse; No Change — Existing Coverage. exact-v1 的结论只覆盖《Building a Scalable, Reproducible, Evaluatable, and Closed-Loop Simulation Environment Foundation for Embodied Intelligence》在 Building a Scalable, Reproducible, Evaluatable, and Closed-Loop Simulation Environment Foundation for Embodied Intelligence Cloud-Native Simulation Infrastructure for Embodied Intelligence Training, Evaluation, and Data Collection; 1.2 Bottlenecks in Real Robot Data and Evaluation; 3.2 Mainstream Benchmarks and Datasets 声明的实验；它没有证明跨 model family、hardware/runtime、数据分布或未测 failure mode 的普遍成立。
<!-- books-review:SF-2026-ARXIV-2606-27962:end -->

<!-- existing:SF-2026-ARXIV-2606-27976:start -->
Ch76 已让 index/source provenance、retrieval evidence 与 context admission 分别持有状态和权限。 本 family 的 source-specific delta 为：把 private dense retrieval 的 routing prefix、cell-local residual key、CKKS rerank 与 linkage risk 分开声明。 Fresh adjacent review at books/part-07-agent/77-memory.md found no competing owner.
<!-- existing:SF-2026-ARXIV-2606-27976:end -->

<!-- delta:SF-2026-ARXIV-2606-27976:start -->
把 private dense retrieval 的 routing prefix、cell-local residual key、CKKS rerank 与 linkage risk 分开声明。
<!-- delta:SF-2026-ARXIV-2606-27976:end -->

<!-- books-review:SF-2026-ARXIV-2606-27976:start -->
Principle Reuse; No Change — Existing Coverage. SHARD preserves retrieval and compartmentalizes alignment evidence, but does not provide DP, unlinkability, or cancellable templates.
<!-- books-review:SF-2026-ARXIV-2606-27976:end -->

<!-- existing:SF-2026-ARXIV-2606-27997:start -->
Ch66 已把 subject identity、EvalSpec、scorer、slice 与 release decision 分成版本化证据对象。 本 family 的 source-specific delta 为：把 benchmark task subset selection 绑定 rank-preservation uncertainty，而非把少量数据集当作无损代理。 Fresh adjacent review at books/part-06-ai-infrastructure/67-monitoring.md found no competing owner.
<!-- existing:SF-2026-ARXIV-2606-27997:end -->

<!-- delta:SF-2026-ARXIV-2606-27997:start -->
把 benchmark task subset selection 绑定 rank-preservation uncertainty，而非把少量数据集当作无损代理。
<!-- delta:SF-2026-ARXIV-2606-27997:end -->

<!-- books-review:SF-2026-ARXIV-2606-27997:start -->
Principle Reuse; No Change — Existing Coverage. For TSC, our best-performing strategy achieves a Spearman correlation of 0.95 with the full benchmark model rankings using only five selected datasets.
<!-- books-review:SF-2026-ARXIV-2606-27997:end -->

<!-- existing:SF-2026-ARXIV-2606-28011:start -->
Ch81 已把 artifact state、deterministic interlock、verifier 与 retry/fallback 组织为可提交状态机。 本 family 的 source-specific delta 为：把 LLM recovery proposal 放在 plant twin simulation、deterministic interlock validation 与 bounded fallback 之后。 Fresh adjacent review at books/part-07-agent/80-reflection.md found no competing owner.
<!-- existing:SF-2026-ARXIV-2606-28011:end -->

<!-- delta:SF-2026-ARXIV-2606-28011:start -->
把 LLM recovery proposal 放在 plant twin simulation、deterministic interlock validation 与 bounded fallback 之后。
<!-- delta:SF-2026-ARXIV-2606-28011:end -->

<!-- books-review:SF-2026-ARXIV-2606-28011:start -->
Principle Reuse; No Change — Existing Coverage. exact-v1 的结论只覆盖《From Detection to Action: Using LLM Agents for Fault-Tolerant Control》在 4.3 Evaluation criteria; 5 Results; 5.1 Mixing module results 声明的实验；它没有证明跨 model family、hardware/runtime、数据分布或未测 failure mode 的普遍成立。
<!-- books-review:SF-2026-ARXIV-2606-28011:end -->

<!-- existing:SF-2026-ARXIV-2606-28013:start -->
The evaluation owner requires semantic-equivalent adapters, but does not freeze the two-axis type-acceptance versus semantic-equivalence coverage matrix.
<!-- existing:SF-2026-ARXIV-2606-28013:end -->

<!-- delta:SF-2026-ARXIV-2606-28013:start -->
把 autoformalization 的 type correctness 与 semantic equivalence 交叉分层，防止单标量误归因。
<!-- delta:SF-2026-ARXIV-2606-28013:end -->

<!-- books-review:SF-2026-ARXIV-2606-28013:start -->
Direct Evolution; Integrate. We propose a signal-coverage matrix that crosses the Lean elaborator (pass/fail) with a semantic-equivalence judgment (equivalent/not), sorting every output into one of four cells: true success (TS), type-only (TO), semantic-only (SO), or both fail (BF).
<!-- books-review:SF-2026-ARXIV-2606-28013:end -->

<!-- existing:SF-2026-ARXIV-2606-28037:start -->
Ch66 已把 subject identity、EvalSpec、scorer、slice 与 release decision 分成版本化证据对象。 本 family 的 source-specific delta 为：以原模型 gradient behavior vector 和 parameter delta 做 evolution-aware regression-test prioritization。 Fresh adjacent review at books/part-06-ai-infrastructure/67-monitoring.md found no competing owner.
<!-- existing:SF-2026-ARXIV-2606-28037:end -->

<!-- delta:SF-2026-ARXIV-2606-28037:start -->
以原模型 gradient behavior vector 和 parameter delta 做 evolution-aware regression-test prioritization。
<!-- delta:SF-2026-ARXIV-2606-28037:end -->

<!-- books-review:SF-2026-ARXIV-2606-28037:start -->
Principle Reuse; No Change — Existing Coverage. In an empirical study across classification and regression tasks, GBV-PD consistently outperformed non-directional baselines and remained competitive with a full-gradient reference, while offering better time and storage profiles for repeated updates via reusable GBV caching.
<!-- books-review:SF-2026-ARXIV-2606-28037:end -->

<!-- existing:SF-2026-ARXIV-2606-28050:start -->
Ch66 已把 subject identity、EvalSpec、scorer、slice 与 release decision 分成版本化证据对象。 本 family 的 source-specific delta 为：用 controlled in-context QA 反证 self-evaluation 普遍比 generation 更容易的默认假设。 Fresh adjacent review at books/part-06-ai-infrastructure/67-monitoring.md found no competing owner.
<!-- existing:SF-2026-ARXIV-2606-28050:end -->

<!-- delta:SF-2026-ARXIV-2606-28050:start -->
用 controlled in-context QA 反证 self-evaluation 普遍比 generation 更容易的默认假设。
<!-- delta:SF-2026-ARXIV-2606-28050:end -->

<!-- books-review:SF-2026-ARXIV-2606-28050:start -->
Principle Reuse; No Change — Existing Coverage. exact-v1 的结论只覆盖《Can LLMs Judge Better Than They Generate? Evaluating Task Asymmetry, Mechanistic Interpretability and Transferability for In-Context QA》在 Generation–evaluation asymmetry.; 3.1 Task Asymmetry Analysis; Evaluation task ( 𝒯 eval \mathcal{T}_{\text{eval}} ). 声明的实验；它没有证明跨 model family、hardware/runtime、数据分布或未测 failure mode 的普遍成立。
<!-- books-review:SF-2026-ARXIV-2606-28050:end -->

<!-- existing:SF-2026-ARXIV-2606-28061:start -->
Ch72 已把不可信内容、model context 与 tool/action authority 分离，并要求 model 外的 fail-closed gate。 本 family 的 source-specific delta 为：把 tool-agent privacy 从最终文本扩展到每个 tool argument、sink 与 purpose-bound information flow。 Fresh adjacent review at books/part-06-ai-infrastructure/71-multi-tenant.md found no competing owner.
<!-- existing:SF-2026-ARXIV-2606-28061:end -->

<!-- delta:SF-2026-ARXIV-2606-28061:start -->
把 tool-agent privacy 从最终文本扩展到每个 tool argument、sink 与 purpose-bound information flow。
<!-- delta:SF-2026-ARXIV-2606-28061:end -->

<!-- books-review:SF-2026-ARXIV-2606-28061:start -->
Principle Reuse; No Change — Existing Coverage. ToolPrivacyBench therefore formalizes a need-to-know disclosure boundary, under which each tool should receive only the information necessary for its stated purpose, and uses trajectory-level auditing to identify privacy over-disclosure in multi-tool workflows.
<!-- books-review:SF-2026-ARXIV-2606-28061:end -->

<!-- existing:SF-2026-ARXIV-2606-28070:start -->
Ch57 已把 paved road、escape hatch、artifact/environment identity 与 lifecycle control 分开。 本 family 的 source-specific delta 为：提供 ontology、knowledge production、model evolution、unified data/service tunnel 在工业规模下的统一平台合同。 Fresh adjacent review at books/part-06-ai-infrastructure/58-kubeflow.md found no competing owner.
<!-- existing:SF-2026-ARXIV-2606-28070:end -->

<!-- delta:SF-2026-ARXIV-2606-28070:start -->
提供 ontology、knowledge production、model evolution、unified data/service tunnel 在工业规模下的统一平台合同。
<!-- delta:SF-2026-ARXIV-2606-28070:end -->

<!-- books-review:SF-2026-ARXIV-2606-28070:start -->
Principle Reuse; No Change — Existing Coverage. exact-v1 的结论只覆盖《JD Oxygen AI Item Center (Oxygen AIIC) V1: An Industrial-Scale LLM/VLM-Centric Solution for Item Understanding, Management, and Applications》在 3.3 Results; 4.2.3 Results; Module 1: Data evaluation. 声明的实验；它没有证明跨 model family、hardware/runtime、数据分布或未测 failure mode 的普遍成立。
<!-- books-review:SF-2026-ARXIV-2606-28070:end -->

<!-- existing:SF-2026-ARXIV-2606-28116:start -->
The monitoring owner covers telemetry and checkpoint-stale monitors, but lacks mechanism-derived pre-loss sensors for attention/router/update failure signatures.
<!-- existing:SF-2026-ARXIV-2606-28116:end -->

<!-- delta:SF-2026-ARXIV-2606-28116:start -->
从 attention/router 的故障机理导出 pre-loss training-instability sensors，而非等待 loss collapse。
<!-- delta:SF-2026-ARXIV-2606-28116:end -->

<!-- books-review:SF-2026-ARXIV-2606-28116:start -->
Direct Evolution; Integrate. After a numerical or a hyperparameter fault has already destabilized the training dynamics, it may continue for thousands of steps while loss and gradient norms still appear normal.
<!-- books-review:SF-2026-ARXIV-2606-28116:end -->

<!-- existing:SF-2026-ARXIV-2606-28128:start -->
Ch25 已分离 belief/latent state、action-conditioned transition、physical truth 与 commit authority。 本 family 的 source-specific delta 为：把 video-world-simulator 的 contact/trajectory physics supervision 与 downstream closed-loop policy effect 联结。 Fresh adjacent review at books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md found no competing owner.
<!-- existing:SF-2026-ARXIV-2606-28128:end -->

<!-- delta:SF-2026-ARXIV-2606-28128:start -->
把 video-world-simulator 的 contact/trajectory physics supervision 与 downstream closed-loop policy effect 联结。
<!-- delta:SF-2026-ARXIV-2606-28128:end -->

<!-- books-review:SF-2026-ARXIV-2606-28128:start -->
Principle Reuse; No Change — Existing Coverage. However, both general-domain video generators and robot-specific data fine-tuned models can still produce physically implausible manipulations, including discontinuous motion trajectories and inconsistent robot-object interactions, which limits their reliability as world simulators.
<!-- books-review:SF-2026-ARXIV-2606-28128:end -->

<!-- existing:SF-2026-ARXIV-2606-28153:start -->
Ch72 已把不可信内容、model context 与 tool/action authority 分离，并要求 model 外的 fail-closed gate。 本 family 的 source-specific delta 为：区分被攻击抑制与仍持续存在的 safety attention heads，并验证其 causal/monitoring 边界。 Fresh adjacent review at books/part-06-ai-infrastructure/71-multi-tenant.md found no competing owner.
<!-- existing:SF-2026-ARXIV-2606-28153:end -->

<!-- delta:SF-2026-ARXIV-2606-28153:start -->
区分被攻击抑制与仍持续存在的 safety attention heads，并验证其 causal/monitoring 边界。
<!-- delta:SF-2026-ARXIV-2606-28153:end -->

<!-- books-review:SF-2026-ARXIV-2606-28153:start -->
Principle Reuse; No Change — Existing Coverage. To validate the practical significance of this robustness, we show that simply reading these persistent activations -- without any training -- yields competitive aggregate detection performance with strong adversarial robustness.
<!-- books-review:SF-2026-ARXIV-2606-28153:end -->

<!-- existing:SF-2026-ARXIV-2606-28187:start -->
The multi-agent owner already represents interaction edges and attribution/noise boundaries; differentiable connection weights are a local optimizer, not a new coordination owner.
<!-- existing:SF-2026-ARXIV-2606-28187:end -->

<!-- delta:SF-2026-ARXIV-2606-28187:start -->
把 multi-agent interaction 建成可反传 attribution graph，以 token-level influence 分配错误责任。
<!-- delta:SF-2026-ARXIV-2606-28187:end -->

<!-- books-review:SF-2026-ARXIV-2606-28187:start -->
Principle Reuse; No Change — Existing Coverage. However, their performance is often limited by miscoordination and, more fundamentally, the lack of fine-grained credit assignment across agents.
<!-- books-review:SF-2026-ARXIV-2606-28187:end -->

<!-- existing:SF-2026-ARXIV-2606-28235:start -->
Ch84 已把 workspace/runtime、intent、acceptance predicate、trace/replay 与 promotion gate 分开。 本 family 的 source-specific delta 为：用大规模 PR 数据把 coding-agent 风险 owner 从单次 agent score 移到 repository-level integration friction。 Fresh adjacent review at books/part-07-agent/83-mcp.md found no competing owner.
<!-- existing:SF-2026-ARXIV-2606-28235:end -->

<!-- delta:SF-2026-ARXIV-2606-28235:start -->
用大规模 PR 数据把 coding-agent 风险 owner 从单次 agent score 移到 repository-level integration friction。
<!-- delta:SF-2026-ARXIV-2606-28235:end -->

<!-- books-review:SF-2026-ARXIV-2606-28235:start -->
Principle Reuse; No Change — Existing Coverage. exact-v1 的结论只覆盖《Govern the Repository, Not the Agent: Measuring Ecosystem-Level Risk in AI-Native Software》在 IV-B Level of analysis and why multilevel models; V Results 声明的实验；它没有证明跨 model family、hardware/runtime、数据分布或未测 failure mode 的普遍成立。
<!-- books-review:SF-2026-ARXIV-2606-28235:end -->

<!-- existing:SF-2026-ARXIV-2606-28276:start -->
The embodied owner warns that simulator success does not prove sim-to-real, but does not bind reconstruction artifact, editable scene variants and real-world rank-validity checks into one promotion chain.
<!-- existing:SF-2026-ARXIV-2606-28276:end -->

<!-- delta:SF-2026-ARXIV-2606-28276:start -->
把 video-to-sim reconstruction、digital cousins、policy training 与 sim-to-real rank validity 绑定。
<!-- delta:SF-2026-ARXIV-2606-28276:end -->

<!-- books-review:SF-2026-ARXIV-2606-28276:start -->
Direct Evolution; Integrate. exact-v1 的结论只覆盖《SimFoundry: Modular and Automated Scene Generation for Policy Learning and Evaluation》在 SimFoundry: Modular and Automated Scene Generation for Policy Learning and Evaluation; 5 Experiments; 5.1 Real-to-Sim Policy Evaluation 声明的实验；它没有证明跨 model family、hardware/runtime、数据分布或未测 failure mode 的普遍成立。
<!-- books-review:SF-2026-ARXIV-2606-28276:end -->

<!-- existing:SF-2026-ARXIV-2606-28277:start -->
Ch66 已把 subject identity、EvalSpec、scorer、slice 与 release decision 分成版本化证据对象。 本 family 的 source-specific delta 为：把 agentic scientific review 的 verification depth 与 human decision authority 分层，并给出部署证据。 Fresh adjacent review at books/part-06-ai-infrastructure/67-monitoring.md found no competing owner.
<!-- existing:SF-2026-ARXIV-2606-28277:end -->

<!-- delta:SF-2026-ARXIV-2606-28277:start -->
把 agentic scientific review 的 verification depth 与 human decision authority 分层，并给出部署证据。
<!-- delta:SF-2026-ARXIV-2606-28277:end -->

<!-- books-review:SF-2026-ARXIV-2606-28277:start -->
Principle Reuse; No Change — Existing Coverage. By catching errors early, PAT eases the cognitive burden placed on referees, while preserving their control over the outcomes of the review process.
<!-- books-review:SF-2026-ARXIV-2606-28277:end -->

<!-- existing:SF-2026-ARXIV-2606-28279:start -->
Ch81 已把 artifact state、deterministic interlock、verifier 与 retry/fallback 组织为可提交状态机。 本 family 的 source-specific delta 为：用 compiled project pack、acceptance predicate、isolated worktree 与 trace/replay 管理 repository-scale hardware agent。 Fresh adjacent review at books/part-07-agent/80-reflection.md found no competing owner.
<!-- existing:SF-2026-ARXIV-2606-28279:end -->

<!-- delta:SF-2026-ARXIV-2606-28279:start -->
用 compiled project pack、acceptance predicate、isolated worktree 与 trace/replay 管理 repository-scale hardware agent。
<!-- delta:SF-2026-ARXIV-2606-28279:end -->

<!-- books-review:SF-2026-ARXIV-2606-28279:start -->
Principle Reuse; No Change — Existing Coverage. However, we do not claim that agentic AI for hardware design is solved: these benchmarks are controlled proxies for a much broader engineering problem in chip design.
<!-- books-review:SF-2026-ARXIV-2606-28279:end -->

<!-- existing:SF-2026-ARXIV-2606-28322:start -->
Ch66 已把 subject identity、EvalSpec、scorer、slice 与 release decision 分成版本化证据对象。 本 family 的 source-specific delta 为：以 Must-Right/Easy-Wrong atomic rubrics 与 gated penalty 替代会掩盖必需事实失败的平均分。 Fresh adjacent review at books/part-06-ai-infrastructure/67-monitoring.md found no competing owner.
<!-- existing:SF-2026-ARXIV-2606-28322:end -->

<!-- delta:SF-2026-ARXIV-2606-28322:start -->
以 Must-Right/Easy-Wrong atomic rubrics 与 gated penalty 替代会掩盖必需事实失败的平均分。
<!-- delta:SF-2026-ARXIV-2606-28322:end -->

<!-- books-review:SF-2026-ARXIV-2606-28322:start -->
Principle Reuse; No Change — Existing Coverage. exact-v1 的结论只覆盖《PerceptionRubrics: Calibrating Multimodal Evaluation to Human Perception》在 PerceptionRubrics: Calibrating Multimodal Evaluation to Human Perception; Visual Perception Benchmarks in MLLMs.; Evaluation of Image Captioning. 声明的实验；它没有证明跨 model family、hardware/runtime、数据分布或未测 failure mode 的普遍成立。
<!-- books-review:SF-2026-ARXIV-2606-28322:end -->

<!-- existing:SF-2026-ARXIV-2606-28430:start -->
Ch66 已把 subject identity、EvalSpec、scorer、slice 与 release decision 分成版本化证据对象。 本 family 的 source-specific delta 为：用 no-op ablation 揭示 coding agent 可通过 oracle 却未交付可复用 artifact 的 construction-validity failure。 Fresh adjacent review at books/part-06-ai-infrastructure/67-monitoring.md found no competing owner.
<!-- existing:SF-2026-ARXIV-2606-28430:end -->

<!-- delta:SF-2026-ARXIV-2606-28430:start -->
用 no-op ablation 揭示 coding agent 可通过 oracle 却未交付可复用 artifact 的 construction-validity failure。
<!-- delta:SF-2026-ARXIV-2606-28430:end -->

<!-- books-review:SF-2026-ARXIV-2606-28430:start -->
Principle Reuse; No Change — Existing Coverage. The agent does not, on its own, validate what it ships as a user would.
<!-- books-review:SF-2026-ARXIV-2606-28430:end -->

<!-- existing:SF-2026-ARXIV-2606-28433:start -->
Ch66 已把 subject identity、EvalSpec、scorer、slice 与 release decision 分成版本化证据对象。 本 family 的 source-specific delta 为：要求 RL evaluation 区分把 simulator 当目标与把 simulator 当 deployment proxy 的两套约束。 Fresh adjacent review at books/part-06-ai-infrastructure/67-monitoring.md found no competing owner.
<!-- existing:SF-2026-ARXIV-2606-28433:end -->

<!-- delta:SF-2026-ARXIV-2606-28433:start -->
要求 RL evaluation 区分把 simulator 当目标与把 simulator 当 deployment proxy 的两套约束。
<!-- delta:SF-2026-ARXIV-2606-28433:end -->

<!-- books-review:SF-2026-ARXIV-2606-28433:start -->
Principle Reuse; No Change — Existing Coverage. To achieve high scores, researchers may adopt solutions exclusively meant for solving simulators, rather than learning while the agent is deployed outside a simulator.
<!-- books-review:SF-2026-ARXIV-2606-28433:end -->

<!-- existing:SF-2026-ARXIV-2606-28434:start -->
Ch77 已让 write/read/compress/delete、provenance 与 remaining-context state 共同决定 memory 行为。 本 family 的 source-specific delta 为：把 coding-agent compression timing、granularity 与剩余 context budget 变成 agent-controlled memory action。 Fresh adjacent review at books/part-07-agent/76-rag.md found no competing owner.
<!-- existing:SF-2026-ARXIV-2606-28434:end -->

<!-- delta:SF-2026-ARXIV-2606-28434:start -->
把 coding-agent compression timing、granularity 与剩余 context budget 变成 agent-controlled memory action。
<!-- delta:SF-2026-ARXIV-2606-28434:end -->

<!-- books-review:SF-2026-ARXIV-2606-28434:start -->
Principle Reuse; No Change — Existing Coverage. Moreover, these approaches fail to jointly optimize memory management and issue resolution capabilities to improve performance while reducing token usage.
<!-- books-review:SF-2026-ARXIV-2606-28434:end -->

<!-- existing:SF-2026-ARXIV-2606-28436:start -->
Ch33 已分离 trajectory owner、outcome verifier、teacher guidance 与 typed credit，避免 teacher 获得 reward sign authority。 本 family 的 source-specific delta 为：把 coding post-training verifier 从 executable environment 改成 repository-evidence judge，改变 reward authority 与 non-proof 边界。 Fresh adjacent review at books/part-04-training-system/32-ppo.md found no competing owner.
<!-- existing:SF-2026-ARXIV-2606-28436:end -->

<!-- delta:SF-2026-ARXIV-2606-28436:start -->
把 coding post-training verifier 从 executable environment 改成 repository-evidence judge，改变 reward authority 与 non-proof 边界。
<!-- delta:SF-2026-ARXIV-2606-28436:end -->

<!-- books-review:SF-2026-ARXIV-2606-28436:start -->
Principle Reuse; No Change — Existing Coverage. We propose Dockerless, an environment-free agentic patch verifier that evaluates generated code patches without executing them.
<!-- books-review:SF-2026-ARXIV-2606-28436:end -->

<!-- existing:SF-2026-ARXIV-2606-28438:start -->
Ch27 已让 sample provenance、mixture/admission 与训练生命周期 lineage 共同决定数据能否进入训练。 本 family 的 source-specific delta 为：证明 recursive code self-training 的 model-coupled gate 会 rubber-stamp collapse，要求 exogenous verification。 Fresh adjacent review at books/part-04-training-system/28-pretraining.md found no competing owner.
<!-- existing:SF-2026-ARXIV-2606-28438:end -->

<!-- delta:SF-2026-ARXIV-2606-28438:start -->
证明 recursive code self-training 的 model-coupled gate 会 rubber-stamp collapse，要求 exogenous verification。
<!-- delta:SF-2026-ARXIV-2606-28438:end -->

<!-- books-review:SF-2026-ARXIV-2606-28438:start -->
Principle Reuse; No Change — Existing Coverage. In the clearest case, the binary self-gate enters a rubber-stamp regime where acceptance scores rise while benchmark correctness falls.
<!-- books-review:SF-2026-ARXIV-2606-28438:end -->

<!-- existing:SF-2026-ARXIV-2606-28455:start -->
Ch25 已分离 belief/latent state、action-conditioned transition、physical truth 与 commit authority。 本 family 的 source-specific delta 为：把 event readout、context-relative emphasis 与 causal sensitivity 分开评估 latent physical structure。 Fresh adjacent review at books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md found no competing owner.
<!-- existing:SF-2026-ARXIV-2606-28455:end -->

<!-- delta:SF-2026-ARXIV-2606-28455:start -->
把 event readout、context-relative emphasis 与 causal sensitivity 分开评估 latent physical structure。
<!-- delta:SF-2026-ARXIV-2606-28455:end -->

<!-- books-review:SF-2026-ARXIV-2606-28455:start -->
Principle Reuse; No Change — Existing Coverage. These results support event-conditioned latent structure and functional sensitivity without implying explicit physical modules or isolated causal circuits.
<!-- books-review:SF-2026-ARXIV-2606-28455:end -->

<!-- existing:SF-2026-ARXIV-2606-28471:start -->
Ch27 已让 sample provenance、mixture/admission 与训练生命周期 lineage 共同决定数据能否进入训练。 本 family 的 source-specific delta 为：以 capability slice 将 evaluation failure 反向映射为可检验 data intervention，并允许判定 data 非根因。 Fresh adjacent review at books/part-04-training-system/28-pretraining.md found no competing owner.
<!-- existing:SF-2026-ARXIV-2606-28471:end -->

<!-- delta:SF-2026-ARXIV-2606-28471:start -->
以 capability slice 将 evaluation failure 反向映射为可检验 data intervention，并允许判定 data 非根因。
<!-- delta:SF-2026-ARXIV-2606-28471:end -->

<!-- books-review:SF-2026-ARXIV-2606-28471:start -->
Principle Reuse; No Change — Existing Coverage. First, the loop rules the data out: continued pre-training drives BBH down by $-46.82\%$, but diagnosis traces this to a single masked \texttt{\textless EOS\textgreater} loss rather than weakened reasoning; restoring it recovers BBH to $66.44$, above the original checkpoint, without changing the data.
<!-- books-review:SF-2026-ARXIV-2606-28471:end -->

<!-- existing:SF-2026-ARXIV-2606-28479:start -->
The LoRA owner versions adapters and rollback but does not require matched optimizer-step controls that distinguish DP, pseudonymization and update-count memorization effects.
<!-- existing:SF-2026-ARXIV-2606-28479:end -->

<!-- delta:SF-2026-ARXIV-2606-28479:start -->
用 matched-update controls 分离 DP guarantee、pseudonymization 与 optimizer-step memorization effect。
<!-- delta:SF-2026-ARXIV-2606-28479:end -->

<!-- books-review:SF-2026-ARXIV-2606-28479:start -->
Direct Evolution; Integrate. Third, F1 scores remain between 0.19 and 0.28 across all 96 adapters using four shot prompting, indicating that, under the evaluated training budget, 1B to 3B SLMs do not achieve operationally useful performance.
<!-- books-review:SF-2026-ARXIV-2606-28479:end -->

<!-- existing:SF-2026-ARXIV-2606-28480:start -->
Ch66 已把 subject identity、EvalSpec、scorer、slice 与 release decision 分成版本化证据对象。 本 family 的 source-specific delta 为：把 terminal-use agent 扩展到非 coding workflow，并用 deterministic setup/execution scoring 约束 release claim。 Fresh adjacent review at books/part-06-ai-infrastructure/67-monitoring.md found no competing owner.
<!-- existing:SF-2026-ARXIV-2606-28480:end -->

<!-- delta:SF-2026-ARXIV-2606-28480:start -->
把 terminal-use agent 扩展到非 coding workflow，并用 deterministic setup/execution scoring 约束 release claim。
<!-- delta:SF-2026-ARXIV-2606-28480:end -->

<!-- books-review:SF-2026-ARXIV-2606-28480:start -->
Principle Reuse; No Change — Existing Coverage. However, existing benchmarks do not adequately evaluate general-purpose terminal computer-use agents (TUAs): general computer-use benchmarks primarily target graphical user interfaces (GUIs), whereas terminal-based benchmarks largely emphasize technical and programming-centric workflows historically native to the shell.
<!-- books-review:SF-2026-ARXIV-2606-28480:end -->

<!-- existing:SF-2026-ARXIV-2606-28514:start -->
Ch82 已让 interaction graph、edge attribution、shared-object ordering 与 coordination noise 分别可审计。 本 family 的 source-specific delta 为：以真实异步倒计时、信息不对称与不可单独完成任务测量实时 collaboration。 Fresh adjacent review at books/part-07-agent/81-workflow.md found no competing owner.
<!-- existing:SF-2026-ARXIV-2606-28514:end -->

<!-- delta:SF-2026-ARXIV-2606-28514:start -->
以真实异步倒计时、信息不对称与不可单独完成任务测量实时 collaboration。
<!-- delta:SF-2026-ARXIV-2606-28514:end -->

<!-- books-review:SF-2026-ARXIV-2606-28514:start -->
Principle Reuse; No Change — Existing Coverage. One agent can see and manipulate the bomb but does not have the defusal instructions; the other has the instructions but cannot see or manipulate the bomb.
<!-- books-review:SF-2026-ARXIV-2606-28514:end -->

<!-- existing:SF-2026-ARXIV-2606-28529:start -->
The inference owner separates request stages and component latency, but does not make closed-loop task time and success the acceptance criterion for embodied speedups.
<!-- existing:SF-2026-ARXIV-2606-28529:end -->

<!-- delta:SF-2026-ARXIV-2606-28529:start -->
把 embodied inference optimization 从 per-step latency 扩展到 closed-loop task time、success 与 hardware-dependent sweet spot。
<!-- delta:SF-2026-ARXIV-2606-28529:end -->

<!-- books-review:SF-2026-ARXIV-2606-28529:start -->
Direct Evolution; Integrate. However, unlike traditional static ML tasks, embodied tasks involve repeated interaction with the environment, and task-level performance is determined not only by per-step cost, but also by closed-loop effects unique to embodied execution, which remain insufficiently characterized in current efficient-inference studies.
<!-- books-review:SF-2026-ARXIV-2606-28529:end -->

<!-- existing:SF-2026-ARXIV-2606-28551:start -->
Ch27 已让 sample provenance、mixture/admission 与训练生命周期 lineage 共同决定数据能否进入训练。 本 family 的 source-specific delta 为：用固定 model/token budget 与多数据类型 corpus 建立 VLM data curation、mixing 与 release artifact 的可复算合同。 Fresh adjacent review at books/part-04-training-system/28-pretraining.md found no competing owner.
<!-- existing:SF-2026-ARXIV-2606-28551:end -->

<!-- delta:SF-2026-ARXIV-2606-28551:start -->
用固定 model/token budget 与多数据类型 corpus 建立 VLM data curation、mixing 与 release artifact 的可复算合同。
<!-- delta:SF-2026-ARXIV-2606-28551:end -->

<!-- books-review:SF-2026-ARXIV-2606-28551:start -->
Principle Reuse; No Change — Existing Coverage. As part of DCVLM, we collect 160 datasets spanning four data types -- image-caption pairs, multimodal interleaved documents, text-only, and instruction-tuning data -- into a corpus of 6T multimodal tokens.
<!-- books-review:SF-2026-ARXIV-2606-28551:end -->

<!-- existing:SF-2026-ARXIV-2606-28562:start -->
Ch33 已分离 trajectory owner、outcome verifier、teacher guidance 与 typed credit，避免 teacher 获得 reward sign authority。 本 family 的 source-specific delta 为：按 student competence 在 token、phase、prompt 三个尺度控制 on-policy distillation supervision。 Fresh adjacent review at books/part-04-training-system/32-ppo.md found no competing owner.
<!-- existing:SF-2026-ARXIV-2606-28562:end -->

<!-- delta:SF-2026-ARXIV-2606-28562:start -->
按 student competence 在 token、phase、prompt 三个尺度控制 on-policy distillation supervision。
<!-- delta:SF-2026-ARXIV-2606-28562:end -->

<!-- books-review:SF-2026-ARXIV-2606-28562:start -->
Principle Reuse; No Change — Existing Coverage. exact-v1 的结论只覆盖《SEAD: Competence-Aware On-Policy Distillation via Entropy-Guided Supervision》在 3 Evaluation; 3.1 Experimental Setup; Evaluation. 声明的实验；它没有证明跨 model family、hardware/runtime、数据分布或未测 failure mode 的普遍成立。
<!-- books-review:SF-2026-ARXIV-2606-28562:end -->

<!-- existing:SF-2026-ARXIV-2606-28565:start -->
The inference owner tracks queue, prefill, decode and host work, but does not state how a kernel/communication simulator remains a forecast subordinate to measured request outcomes.
<!-- existing:SF-2026-ARXIV-2606-28565:end -->

<!-- delta:SF-2026-ARXIV-2606-28565:start -->
把 serving scheduler、kernel、communication 与 host overhead 组合成 token/kernel-level capacity simulator。
<!-- delta:SF-2026-ARXIV-2606-28565:end -->

<!-- books-review:SF-2026-ARXIV-2606-28565:start -->
Direct Evolution; Integrate. In our simulator, these predictions yield end-to-end median (p50) errors across six model families of 15.4%, 12.8%, and 3.0% (TTFT, TPOT, throughput) in the cross-generation tier and 14.3%, 6.2%, and 2.7% in the target-measured tier, matching dedicated profiling tools while collecting far less on-device data.
<!-- books-review:SF-2026-ARXIV-2606-28565:end -->

<!-- existing:SF-2026-ARXIV-2606-28574:start -->
Ch66 已把 subject identity、EvalSpec、scorer、slice 与 release decision 分成版本化证据对象。 本 family 的 source-specific delta 为：把 LLM coder 的表面一致性与 theoretical construct validity 分开，并要求 clause-level extractive evidence。 Fresh adjacent review at books/part-06-ai-infrastructure/67-monitoring.md found no competing owner.
<!-- existing:SF-2026-ARXIV-2606-28574:end -->

<!-- delta:SF-2026-ARXIV-2606-28574:start -->
把 LLM coder 的表面一致性与 theoretical construct validity 分开，并要求 clause-level extractive evidence。
<!-- delta:SF-2026-ARXIV-2606-28574:end -->

<!-- books-review:SF-2026-ARXIV-2606-28574:start -->
Principle Reuse; No Change — Existing Coverage. exact-v1 的结论只覆盖《Correct codes for the wrong reasons? validating LLMs as measurement instruments for theoretical constructs》在 3.1 Clauses with grounds; 3.2 Human in the loop 声明的实验；它没有证明跨 model family、hardware/runtime、数据分布或未测 failure mode 的普遍成立。
<!-- books-review:SF-2026-ARXIV-2606-28574:end -->

<!-- existing:SF-2026-ARXIV-2606-28615:start -->
Ch66 已把 subject identity、EvalSpec、scorer、slice 与 release decision 分成版本化证据对象。 本 family 的 source-specific delta 为：把 free-text explanation sufficiency 绑定显式 input distribution 与 self-consistent information metric。 Fresh adjacent review at books/part-06-ai-infrastructure/67-monitoring.md found no competing owner.
<!-- existing:SF-2026-ARXIV-2606-28615:end -->

<!-- delta:SF-2026-ARXIV-2606-28615:start -->
把 free-text explanation sufficiency 绑定显式 input distribution 与 self-consistent information metric。
<!-- delta:SF-2026-ARXIV-2606-28615:end -->

<!-- books-review:SF-2026-ARXIV-2606-28615:start -->
Principle Reuse; No Change — Existing Coverage. We formalize self-consistent sufficiency as a goal for free-text explanations and introduce an information-theoretic metric, SCSuff, that enables evaluation of free-text explanations without relying on predefined biases or shortcuts.
<!-- books-review:SF-2026-ARXIV-2606-28615:end -->

<!-- existing:SF-2026-ARXIV-2606-28639:start -->
Ch72 已把不可信内容、model context 与 tool/action authority 分离，并要求 model 外的 fail-closed gate。 本 family 的 source-specific delta 为：给 static/dynamic alignment certification 划出 expressivity、soundness、completeness 与 tractability 的形式边界。 Fresh adjacent review at books/part-06-ai-infrastructure/71-multi-tenant.md found no competing owner.
<!-- existing:SF-2026-ARXIV-2606-28639:end -->

<!-- delta:SF-2026-ARXIV-2606-28639:start -->
给 static/dynamic alignment certification 划出 expressivity、soundness、completeness 与 tractability 的形式边界。
<!-- delta:SF-2026-ARXIV-2606-28639:end -->

<!-- books-review:SF-2026-ARXIV-2606-28639:start -->
Principle Reuse; No Change — Existing Coverage. Three practical risks (finite test coverage, bounded deliberation time, restricted observation) are one phenomenon: every bounded scheme that does not reject correct evidence admits an evolution trace it certifies at every stage while the property is persistently violated.
<!-- books-review:SF-2026-ARXIV-2606-28639:end -->

<!-- existing:SF-2026-ARXIV-2606-28649:start -->
The security owner treats OCR/audio content as untrusted, but does not trace sensor-derived text/state promoted into system-role context through robot middleware.
<!-- existing:SF-2026-ARXIV-2606-28649:end -->

<!-- delta:SF-2026-ARXIV-2606-28649:start -->
把 robot prompt injection threat surface 扩展到 OCR、audio 与 LiDAR-derived system context，并测 firewall bypass。
<!-- delta:SF-2026-ARXIV-2606-28649:end -->

<!-- books-review:SF-2026-ARXIV-2606-28649:start -->
Direct Evolution; Integrate. Across 100 independent runs per injection variant on five LLMs spanning four model families and parameter scales from approximately 4B to approximately 284B (DeepSeek-V4-Flash, Llama-3-8B-Instruct-Lite, Llama-3.3-70B-Instruct-Turbo, Qwen 2.5-7B-Instruct-Turbo, Gemma-3n-E4B), we identify model-specific vulnerability profiles that do not follow a monotonic scaling trend: Llama-3.3-70B-Instruct-Turbo exhibits 100% attack success rate (ASR) across all injection variants, while Llama-3-8B-Instruct-Lite and Qwen 2.5-7B-Instruct-Turbo resist direct-override injection (0% ASR), and the smallest model evaluated (Gemma-3n-E4B, approximately 4B) matches the 70B model's vulnerability profile, indicating that robustness is model-specific rather than scale-dependent.
<!-- books-review:SF-2026-ARXIV-2606-28649:end -->

<!-- existing:SF-2026-ARXIV-2606-28661:start -->
The evaluation owner discusses correlated uncertainty, but does not separate sampling coverage from selector authority or expose modal/correlation ceilings as a stopping boundary.
<!-- existing:SF-2026-ARXIV-2606-28661:end -->

<!-- delta:SF-2026-ARXIV-2606-28661:start -->
区分 test-time sampling coverage 与可部署 selection，并定义 modal/correlation ceiling 的停止边界。
<!-- delta:SF-2026-ARXIV-2606-28661:end -->

<!-- books-review:SF-2026-ARXIV-2606-28661:start -->
Direct Evolution; Integrate. But a deployed system must return one answer, and choosing it, not knowing which try is right, is selection; selection is capped, and past a point extra samples only make the model surer of a confident mistake, even as every draw adds cost.
<!-- books-review:SF-2026-ARXIV-2606-28661:end -->

## 7. Semantic Audit

<!-- validator:semantic-audit-v1 -->
| Audit ID | Auditor | Scope | Reviewed Refs | Findings | Resolution | Status |
| --- | --- | --- | --- | --- | --- | --- |
| SA-20260627-COVERAGE-V1 | fresh-context:jun27-v1 | coverage | coverage:SRC-ARXIV:20260627 | — | 384/384 screened; 64 retained; 320 closures; 84/84 route-negative checked; 3 FNs restored | passed |
| SA-20260627-EVIDENCE-V1 | fresh-context:jun27-v1 | evidence | review:SF-2026-ARXIV-2606-27632; review:SF-2026-ARXIV-2606-27634; review:SF-2026-ARXIV-2606-27650; review:SF-2026-ARXIV-2606-27669; review:SF-2026-ARXIV-2606-27679; review:SF-2026-ARXIV-2606-27681; review:SF-2026-ARXIV-2606-27683; review:SF-2026-ARXIV-2606-27704; review:SF-2026-ARXIV-2606-27709; review:SF-2026-ARXIV-2606-27732; review:SF-2026-ARXIV-2606-27739; review:SF-2026-ARXIV-2606-27743; review:SF-2026-ARXIV-2606-27757; review:SF-2026-ARXIV-2606-27780; review:SF-2026-ARXIV-2606-27791; review:SF-2026-ARXIV-2606-27797; review:SF-2026-ARXIV-2606-27806; review:SF-2026-ARXIV-2606-27814; review:SF-2026-ARXIV-2606-27826; review:SF-2026-ARXIV-2606-27841; review:SF-2026-ARXIV-2606-27866; review:SF-2026-ARXIV-2606-27906; review:SF-2026-ARXIV-2606-27934; review:SF-2026-ARXIV-2606-27936; review:SF-2026-ARXIV-2606-27944; review:SF-2026-ARXIV-2606-27962; review:SF-2026-ARXIV-2606-27976; review:SF-2026-ARXIV-2606-27997; review:SF-2026-ARXIV-2606-28011; review:SF-2026-ARXIV-2606-28013; review:SF-2026-ARXIV-2606-28037; review:SF-2026-ARXIV-2606-28050; review:SF-2026-ARXIV-2606-28061; review:SF-2026-ARXIV-2606-28070; review:SF-2026-ARXIV-2606-28116; review:SF-2026-ARXIV-2606-28128; review:SF-2026-ARXIV-2606-28153; review:SF-2026-ARXIV-2606-28166; review:SF-2026-ARXIV-2606-28187; review:SF-2026-ARXIV-2606-28235; review:SF-2026-ARXIV-2606-28276; review:SF-2026-ARXIV-2606-28277; review:SF-2026-ARXIV-2606-28279; review:SF-2026-ARXIV-2606-28322; review:SF-2026-ARXIV-2606-28430; review:SF-2026-ARXIV-2606-28433; review:SF-2026-ARXIV-2606-28434; review:SF-2026-ARXIV-2606-28436; review:SF-2026-ARXIV-2606-28438; review:SF-2026-ARXIV-2606-28455; review:SF-2026-ARXIV-2606-28471; review:SF-2026-ARXIV-2606-28479; review:SF-2026-ARXIV-2606-28480; review:SF-2026-ARXIV-2606-28514; review:SF-2026-ARXIV-2606-28529; review:SF-2026-ARXIV-2606-28551; review:SF-2026-ARXIV-2606-28560; review:SF-2026-ARXIV-2606-28562; review:SF-2026-ARXIV-2606-28565; review:SF-2026-ARXIV-2606-28574; review:SF-2026-ARXIV-2606-28615; review:SF-2026-ARXIV-2606-28639; review:SF-2026-ARXIV-2606-28649; review:SF-2026-ARXIV-2606-28661 | — | 64/64 exact-v1 resolved with no blocker | passed |
| SA-20260627-SELECTION-V1 | fresh-context:jun27-v1 | deep_analysis_selection | analysis-decision:SF-2026-ARXIV-2606-27632; analysis-decision:SF-2026-ARXIV-2606-27634; analysis-decision:SF-2026-ARXIV-2606-27650; analysis-decision:SF-2026-ARXIV-2606-27669; analysis-decision:SF-2026-ARXIV-2606-27679; analysis:DA-20260627-STRICT-MEDIATED-WORLD-STATE; analysis-decision:SF-2026-ARXIV-2606-27683; analysis-decision:SF-2026-ARXIV-2606-27704; analysis-decision:SF-2026-ARXIV-2606-27709; analysis-decision:SF-2026-ARXIV-2606-27732; analysis-decision:SF-2026-ARXIV-2606-27739; analysis-decision:SF-2026-ARXIV-2606-27743; analysis-decision:SF-2026-ARXIV-2606-27757; analysis-decision:SF-2026-ARXIV-2606-27780; analysis-decision:SF-2026-ARXIV-2606-27791; analysis-decision:SF-2026-ARXIV-2606-27797; analysis-decision:SF-2026-ARXIV-2606-27806; analysis-decision:SF-2026-ARXIV-2606-27814; analysis-decision:SF-2026-ARXIV-2606-27826; analysis-decision:SF-2026-ARXIV-2606-27841; analysis-decision:SF-2026-ARXIV-2606-27866; analysis:DA-20260627-PHASE-CLOSED-LOOP-INFERENCE; analysis-decision:SF-2026-ARXIV-2606-27934; analysis-decision:SF-2026-ARXIV-2606-27936; analysis-decision:SF-2026-ARXIV-2606-27944; analysis-decision:SF-2026-ARXIV-2606-27962; analysis-decision:SF-2026-ARXIV-2606-27976; analysis-decision:SF-2026-ARXIV-2606-27997; analysis-decision:SF-2026-ARXIV-2606-28011; analysis-decision:SF-2026-ARXIV-2606-28013; analysis-decision:SF-2026-ARXIV-2606-28037; analysis-decision:SF-2026-ARXIV-2606-28050; analysis-decision:SF-2026-ARXIV-2606-28061; analysis-decision:SF-2026-ARXIV-2606-28070; analysis-decision:SF-2026-ARXIV-2606-28116; analysis-decision:SF-2026-ARXIV-2606-28128; analysis-decision:SF-2026-ARXIV-2606-28153; analysis-decision:SF-2026-ARXIV-2606-28166; analysis-decision:SF-2026-ARXIV-2606-28187; analysis-decision:SF-2026-ARXIV-2606-28235; analysis-decision:SF-2026-ARXIV-2606-28276; analysis-decision:SF-2026-ARXIV-2606-28277; analysis-decision:SF-2026-ARXIV-2606-28279; analysis-decision:SF-2026-ARXIV-2606-28322; analysis-decision:SF-2026-ARXIV-2606-28430; analysis-decision:SF-2026-ARXIV-2606-28433; analysis-decision:SF-2026-ARXIV-2606-28434; analysis-decision:SF-2026-ARXIV-2606-28436; analysis-decision:SF-2026-ARXIV-2606-28438; analysis-decision:SF-2026-ARXIV-2606-28455; analysis-decision:SF-2026-ARXIV-2606-28471; analysis-decision:SF-2026-ARXIV-2606-28479; analysis-decision:SF-2026-ARXIV-2606-28480; analysis-decision:SF-2026-ARXIV-2606-28514; analysis-decision:SF-2026-ARXIV-2606-28551; analysis-decision:SF-2026-ARXIV-2606-28560; analysis-decision:SF-2026-ARXIV-2606-28562; analysis-decision:SF-2026-ARXIV-2606-28574; analysis-decision:SF-2026-ARXIV-2606-28615; analysis-decision:SF-2026-ARXIV-2606-28639; analysis:DA-20260627-SENSORY-CONTEXT-AUTHORITY; analysis-decision:SF-2026-ARXIV-2606-28661 | — | 64/64 frontier frozen; three units selected before rationale | passed |
| SA-20260627-BOOKS-POSTWRITE-V1 | fresh-context:jun27-v1 | books | books-review:SF-2026-ARXIV-2606-27632; books-review:SF-2026-ARXIV-2606-27634; books-review:SF-2026-ARXIV-2606-27650; books-review:SF-2026-ARXIV-2606-27669; books-review:SF-2026-ARXIV-2606-27679; books-review:SF-2026-ARXIV-2606-27681; books-review:SF-2026-ARXIV-2606-27683; books-review:SF-2026-ARXIV-2606-27704; books-review:SF-2026-ARXIV-2606-27709; books-review:SF-2026-ARXIV-2606-27732; books-review:SF-2026-ARXIV-2606-27739; books-review:SF-2026-ARXIV-2606-27743; books-review:SF-2026-ARXIV-2606-27757; books-review:SF-2026-ARXIV-2606-27780; review:SF-2026-ARXIV-2606-27791; books-review:SF-2026-ARXIV-2606-27797; books-review:SF-2026-ARXIV-2606-27806; books-review:SF-2026-ARXIV-2606-27814; books-review:SF-2026-ARXIV-2606-27826; books-review:SF-2026-ARXIV-2606-27841; books-review:SF-2026-ARXIV-2606-27866; books-review:SF-2026-ARXIV-2606-27906; books-review:SF-2026-ARXIV-2606-27934; books-review:SF-2026-ARXIV-2606-27936; books-review:SF-2026-ARXIV-2606-27944; books-review:SF-2026-ARXIV-2606-27962; books-review:SF-2026-ARXIV-2606-27976; books-review:SF-2026-ARXIV-2606-27997; books-review:SF-2026-ARXIV-2606-28011; books-review:SF-2026-ARXIV-2606-28013; books-review:SF-2026-ARXIV-2606-28037; books-review:SF-2026-ARXIV-2606-28050; books-review:SF-2026-ARXIV-2606-28061; books-review:SF-2026-ARXIV-2606-28070; books-review:SF-2026-ARXIV-2606-28116; books-review:SF-2026-ARXIV-2606-28128; books-review:SF-2026-ARXIV-2606-28153; review:SF-2026-ARXIV-2606-28166; books-review:SF-2026-ARXIV-2606-28187; books-review:SF-2026-ARXIV-2606-28235; books-review:SF-2026-ARXIV-2606-28276; books-review:SF-2026-ARXIV-2606-28277; books-review:SF-2026-ARXIV-2606-28279; books-review:SF-2026-ARXIV-2606-28322; books-review:SF-2026-ARXIV-2606-28430; books-review:SF-2026-ARXIV-2606-28433; books-review:SF-2026-ARXIV-2606-28434; books-review:SF-2026-ARXIV-2606-28436; books-review:SF-2026-ARXIV-2606-28438; books-review:SF-2026-ARXIV-2606-28455; books-review:SF-2026-ARXIV-2606-28471; books-review:SF-2026-ARXIV-2606-28479; books-review:SF-2026-ARXIV-2606-28480; books-review:SF-2026-ARXIV-2606-28514; books-review:SF-2026-ARXIV-2606-28529; books-review:SF-2026-ARXIV-2606-28551; review:SF-2026-ARXIV-2606-28560; books-review:SF-2026-ARXIV-2606-28562; books-review:SF-2026-ARXIV-2606-28565; books-review:SF-2026-ARXIV-2606-28574; books-review:SF-2026-ARXIV-2606-28615; books-review:SF-2026-ARXIV-2606-28639; books-review:SF-2026-ARXIV-2606-28649; books-review:SF-2026-ARXIV-2606-28661 | — | 14/14 Integrate writebacks across 11 owners, 47/47 No Change and 3/3 Weekly Only passed the 64/64 post-write fresh audit; unresolved findings 0 | passed |

## 8. Ignored Noise

候选分母外 identity 已在 full-population semantic screening ledger 中按 family-specific 理由关闭；Coverage Receipt 与 source packet 保留 raw、retained、closure 和 route-negative 账目，正文不重复展开低耐久度或越界项目。

### Materials and Access

- 64/64 official exact-v1 HTML pages accessible; blocker=0; later versions used=0.
- No Materials Request.

## 9. Recommended Action

- Integrate: 14/14 written across 11 owners; No Change: 47/47 revalidated; Weekly Only: 3/3 remained context-only.
- Shared Books were updated under root's serialized write lock; `docs/LEARNING_STATE.md` was not edited; this lane audited all 64 dispositions after writeback.

## 10. Repository Changes

- Date-local Daily/source packet/scripts plus the root-authorized 11-owner Books writeback.

## 11. Open Questions

- Evidence and Selection passed the 64/64 pre-write fresh audit.
- Books passed the 64/64 post-write fresh audit; unresolved findings: 0.

## 12. Sources

- [Yuvion LLM: An Adversarially-Aware Large Language Model for Content And AI Safety](https://arxiv.org/abs/2606.27632v1) — first-public（Asia/Shanghai）：2026-06-26；accessed：2026-08-29
- [Continual Learning for Sequential Personalization of Small Language Models: A Stability Monitoring Analysis](https://arxiv.org/abs/2606.27634v1) — first-public（Asia/Shanghai）：2026-06-26；accessed：2026-08-29
- [GenWorld: Empirically Grounded Urban Simulation Infrastructure for Scalable LLM-Agent Studies](https://arxiv.org/abs/2606.27650v1) — first-public（Asia/Shanghai）：2026-06-26；accessed：2026-08-29
- [When Search Agents Should Ask: DiscoBench for Clarification-Aware Deep Search](https://arxiv.org/abs/2606.27669v1) — first-public（Asia/Shanghai）：2026-06-26；accessed：2026-08-29
- [From Signals to Transfer: A Factorised Study of Probe-Based Uncertainty Estimation in Large Language Models](https://arxiv.org/abs/2606.27679v1) — first-public（Asia/Shanghai）：2026-06-26；accessed：2026-08-29
- [Textual Belief States for World Models: Identifiable Representation Learning Under Strict Mediation](https://arxiv.org/abs/2606.27681v1) — first-public（Asia/Shanghai）：2026-06-26；accessed：2026-08-29
- [CBD: API-Only LLM Black-Box Unlearning through Controlled Behavioral Divergence](https://arxiv.org/abs/2606.27683v1) — first-public（Asia/Shanghai）：2026-06-26；accessed：2026-08-29
- [AdvScan: Black-Box Adversarial Example Detection at Runtime through Power Analysis](https://arxiv.org/abs/2606.27704v1) — first-public（Asia/Shanghai）：2026-06-26；accessed：2026-08-29
- [Low-Agreeableness Persona Conditioning for Safe LLM Fine-Tuning](https://arxiv.org/abs/2606.27709v1) — first-public（Asia/Shanghai）：2026-06-26；accessed：2026-08-29
- [Bifocal Diffusion Language Models: Asymmetric Bidirectional Context for Parallel Generation](https://arxiv.org/abs/2606.27732v1) — first-public（Asia/Shanghai）：2026-06-26；accessed：2026-08-29
- [The Weakest Link Tells It All: Outcome-Supervised Process Reward Modeling via Learnable Credit Assignment](https://arxiv.org/abs/2606.27739v1) — first-public（Asia/Shanghai）：2026-06-26；accessed：2026-08-29
- [End-to-End Dynamic Sparsity for Resource-Adaptive LLM Inference](https://arxiv.org/abs/2606.27743v1) — first-public（Asia/Shanghai）：2026-06-26；accessed：2026-08-29
- [Towards Reliable and Robust LLM Planning: Symbolic Feedback-Driven Iterative Self-Refinement Framework](https://arxiv.org/abs/2606.27757v1) — first-public（Asia/Shanghai）：2026-06-26；accessed：2026-08-29
- [Understanding Rollout Error in Graph World Models](https://arxiv.org/abs/2606.27780v1) — first-public（Asia/Shanghai）：2026-06-26；accessed：2026-08-29
- [NLL-Guided Full-Attention Layer Selection for Training-Free Sliding-Window Adaptation](https://arxiv.org/abs/2606.27791v1) — first-public（Asia/Shanghai）：2026-06-26；accessed：2026-08-29
- [Optimizing Teacher-Student Partitioning for Scalable Knowledge Distillation on HPC Systems](https://arxiv.org/abs/2606.27797v1) — first-public（Asia/Shanghai）：2026-06-26；accessed：2026-08-29
- [Agent vs. Parametric World Models: Hybrid Planning for Reliable Language Agents](https://arxiv.org/abs/2606.27806v1) — first-public（Asia/Shanghai）：2026-06-26；accessed：2026-08-29
- [ATOD: Annealed Turn-Aware On-Policy Distillation for Multi-Turn Agentic Tasks](https://arxiv.org/abs/2606.27814v1) — first-public（Asia/Shanghai）：2026-06-26；accessed：2026-08-29
- [NormAct: Benchmarking Embodied Agents' Proactive Compliance with Unspoken Social Norms](https://arxiv.org/abs/2606.27826v1) — first-public（Asia/Shanghai）：2026-06-26；accessed：2026-08-29
- [WattLayer: Get Layers Right to Estimate Inference Energy of Neural Networks](https://arxiv.org/abs/2606.27841v1) — first-public（Asia/Shanghai）：2026-06-26；accessed：2026-08-29
- [FlexMoE: One-for-All Nested Intra-Expert Pruning for MoE Language Models](https://arxiv.org/abs/2606.27866v1) — first-public（Asia/Shanghai）：2026-06-26；accessed：2026-08-29
- [Phase Matters: Characterizing Heterogeneous Vision-Language Inference on a Mobile SoC](https://arxiv.org/abs/2606.27906v1) — first-public（Asia/Shanghai）：2026-06-26；accessed：2026-08-29
- [Self-Verifying Measurement Records: Hash-Linked Evidence Graphs for Hardware Benchmarking](https://arxiv.org/abs/2606.27934v1) — first-public（Asia/Shanghai）：2026-06-26；accessed：2026-08-29
- [Agentic AI-Powered Re-Identification: An Emerging, Scalable Threat to Mobility Microdata Privacy](https://arxiv.org/abs/2606.27936v1) — first-public（Asia/Shanghai）：2026-06-26；accessed：2026-08-29
- [It Lied to a Doctor to Buy Poison Ingredients: Quantifying Real-World Misuse of Phone-use Agents](https://arxiv.org/abs/2606.27944v1) — first-public（Asia/Shanghai）：2026-06-26；accessed：2026-08-29
- [Building a Scalable, Reproducible, Evaluatable, and Closed-Loop Simulation Environment Foundation for Embodied Intelligence](https://arxiv.org/abs/2606.27962v1) — first-public（Asia/Shanghai）：2026-06-26；accessed：2026-08-29
- [SHARD: cell-keyed residual splitting for alignment-resistant private dense retrieval](https://arxiv.org/abs/2606.27976v1) — first-public（Asia/Shanghai）：2026-06-26；accessed：2026-08-29
- [Benchmarking on Tasks That Matter: Dataset Selection for Preserving Model Rankings](https://arxiv.org/abs/2606.27997v1) — first-public（Asia/Shanghai）：2026-06-26；accessed：2026-08-29
- [From Detection to Action: Using LLM Agents for Fault-Tolerant Control](https://arxiv.org/abs/2606.28011v1) — first-public（Asia/Shanghai）：2026-06-26；accessed：2026-08-29
- [The Signal-Coverage Matrix: Stratifying Type and Semantic Errors in Statement Autoformalization](https://arxiv.org/abs/2606.28013v1) — first-public（Asia/Shanghai）：2026-06-26；accessed：2026-08-29
- [Evolution-Aware Regression Test Prioritization of ML-Enabled Systems Using Gradient-Based Behavior Vectors](https://arxiv.org/abs/2606.28037v1) — first-public（Asia/Shanghai）：2026-06-26；accessed：2026-08-29
- [Can LLMs Judge Better Than They Generate? Evaluating Task Asymmetry, Mechanistic Interpretability and Transferability for In-Context QA](https://arxiv.org/abs/2606.28050v1) — first-public（Asia/Shanghai）：2026-06-26；accessed：2026-08-29
- [ToolPrivacyBench: Benchmarking Purpose-Bound Privacy in Tool-Using LLM Agents](https://arxiv.org/abs/2606.28061v1) — first-public（Asia/Shanghai）：2026-06-26；accessed：2026-08-29
- [JD Oxygen AI Item Center (Oxygen AIIC) V1: An Industrial-Scale LLM/VLM-Centric Solution for Item Understanding, Management, and Applications](https://arxiv.org/abs/2606.28070v1) — first-public（Asia/Shanghai）：2026-06-26；accessed：2026-08-29
- [Mechanism-Driven Monitors for Preemptive Detection of LLM Training Instability](https://arxiv.org/abs/2606.28116v1) — first-public（Asia/Shanghai）：2026-06-26；accessed：2026-08-29
- [PhysisForcing: Physics Reinforced World Simulator for Robotic Manipulation](https://arxiv.org/abs/2606.28128v1) — first-public（Asia/Shanghai）：2026-06-26；accessed：2026-08-29
- [Robust Harmful Features Under Jailbreak Attacks: Mechanistic Evidence from Attention Head Specialization in Large Language Models](https://arxiv.org/abs/2606.28153v1) — first-public（Asia/Shanghai）：2026-06-26；accessed：2026-08-29
- [Tandem Reinforcement Learning with Verifiable Rewards](https://arxiv.org/abs/2606.28166v1) — first-public（Asia/Shanghai）：2026-06-26；accessed：2026-08-29
- [GBC: Gradient-Based Connections for Optimizing Multi-Agent Systems](https://arxiv.org/abs/2606.28187v1) — first-public（Asia/Shanghai）：2026-06-26；accessed：2026-08-29
- [Govern the Repository, Not the Agent: Measuring Ecosystem-Level Risk in AI-Native Software](https://arxiv.org/abs/2606.28235v1) — first-public（Asia/Shanghai）：2026-06-26；accessed：2026-08-29
- [SimFoundry: Modular and Automated Scene Generation for Policy Learning and Evaluation](https://arxiv.org/abs/2606.28276v1) — first-public（Asia/Shanghai）：2026-06-26；accessed：2026-08-29
- [Towards Automating Scientific Review with Google's Paper Assistant Tool](https://arxiv.org/abs/2606.28277v1) — first-public（Asia/Shanghai）：2026-06-26；accessed：2026-08-29
- [Agentic Hardware Design as Repository-Level Code Evolution](https://arxiv.org/abs/2606.28279v1) — first-public（Asia/Shanghai）：2026-06-26；accessed：2026-08-29
- [PerceptionRubrics: Calibrating Multimodal Evaluation to Human Perception](https://arxiv.org/abs/2606.28322v1) — first-public（Asia/Shanghai）：2026-06-26；accessed：2026-08-29
- [Building to the Test: Coding Agents Deliver What You Check, Not What You Requested](https://arxiv.org/abs/2606.28430v1) — first-public（Asia/Shanghai）：2026-06-26；accessed：2026-08-29
- [Position: RL Researchers Need to Distinguish Between Solving Simulators and Using Simulators as a Proxy](https://arxiv.org/abs/2606.28433v1) — first-public（Asia/Shanghai）：2026-06-26；accessed：2026-08-29
- [SWE-MeM: Learning Adaptive Memory Management for Long-Horizon Coding Agents](https://arxiv.org/abs/2606.28434v1) — first-public（Asia/Shanghai）：2026-06-26；accessed：2026-08-29
- [Dockerless: Environment-Free Program Verifier for Coding Agents](https://arxiv.org/abs/2606.28436v1) — first-public（Asia/Shanghai）：2026-06-26；accessed：2026-08-29
- [When AI Reviews Its Own Code: Recursive Self-Training Collapse in Code LLMs](https://arxiv.org/abs/2606.28438v1) — first-public（Asia/Shanghai）：2026-06-26；accessed：2026-08-29
- [Event-Conditioned Diagnostics of Kinematic, Contact, and Object-Permanence Structure in Passive Object-State World Models](https://arxiv.org/abs/2606.28455v1) — first-public（Asia/Shanghai）：2026-06-26；accessed：2026-08-29
- [Data and Evaluation Closed-Loop for Model Capability Enhancement](https://arxiv.org/abs/2606.28471v1) — first-public（Asia/Shanghai）：2026-06-26；accessed：2026-08-29
- [Decomposing Memorization Reduction in Privacy-Preserving Fine-Tuning of SLMs for CSIRTs](https://arxiv.org/abs/2606.28479v1) — first-public（Asia/Shanghai）：2026-06-26；accessed：2026-08-29
- [TUA-Bench: A Benchmark for General-Purpose Terminal-Use Agents](https://arxiv.org/abs/2606.28480v1) — first-public（Asia/Shanghai）：2026-06-26；accessed：2026-08-29
- [GPTNT: Benchmarking Real-Time Collaboration Between Multimodal Agents on Keep Talking And Nobody Explodes](https://arxiv.org/abs/2606.28514v1) — first-public（Asia/Shanghai）：2026-06-26；accessed：2026-08-29
- [The Speedup Paradox: Rethinking Inference Speed-Quality Trade-off in Embodied Tasks](https://arxiv.org/abs/2606.28529v1) — first-public（Asia/Shanghai）：2026-06-26；accessed：2026-08-29
- [DataComp-VLM: Improved Open Datasets for Vision-Language Models](https://arxiv.org/abs/2606.28551v1) — first-public（Asia/Shanghai）：2026-06-26；accessed：2026-08-29
- [Depth-Staggered Fibonacci Spacing for Sparse Attention: Static Schedules Beat Learned Dilation and Extrapolate Where Dense Attention Fails](https://arxiv.org/abs/2606.28560v1) — first-public（Asia/Shanghai）：2026-06-26；accessed：2026-08-29
- [SEAD: Competence-Aware On-Policy Distillation via Entropy-Guided Supervision](https://arxiv.org/abs/2606.28562v1) — first-public（Asia/Shanghai）：2026-06-26；accessed：2026-08-29
- [KernelSight-LM: A Kernel-Level LLM Inference Simulator](https://arxiv.org/abs/2606.28565v1) — first-public（Asia/Shanghai）：2026-06-26；accessed：2026-08-29
- [Correct codes for the wrong reasons? validating LLMs as measurement instruments for theoretical constructs](https://arxiv.org/abs/2606.28574v1) — first-public（Asia/Shanghai）：2026-06-26；accessed：2026-08-29
- [What LLMs explain is not what they believe: Evaluating explanation sufficiency under models' own input beliefs](https://arxiv.org/abs/2606.28615v1) — first-public（Asia/Shanghai）：2026-06-26；accessed：2026-08-29
- [The Unverifiability of Artificial General Intelligence (AGI) Alignment, Static and Dynamic: From Trakhtenbrot's Wall to the Safety-Generality Tension](https://arxiv.org/abs/2606.28639v1) — first-public（Asia/Shanghai）：2026-06-26；accessed：2026-08-29
- [RIPA: Sensory-Vector Prompt Injection Attacks on LLM-Controlled ROS 2 Robots](https://arxiv.org/abs/2606.28649v1) — first-public（Asia/Shanghai）：2026-06-26；accessed：2026-08-29
- [When More Sampling Hurts: The Modal Ceiling and Correlation Ceiling of Test-Time Scaling](https://arxiv.org/abs/2606.28661v1) — first-public（Asia/Shanghai）：2026-06-26；accessed：2026-08-29
- [Research Sources Registry](../../../../docs/RESEARCH_SOURCES.md) — source roles、cadence 与 evidence scope 的权威注册表

## 13. Final Status

Daily V2.1 的 Coverage=Closed、Evidence=Passed、Books=Passed；Completion Status=Complete。机器校验只证明接口一致，语义结论由第 7 节记录的 pre-write 与 post-write fresh-context audit 承担。

State Truth: Completion=Complete；Coverage=Closed；Evidence=Passed；Books=Passed；Unresolved Findings=0。
