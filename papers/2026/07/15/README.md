# Daily Research — 2026-07-15

**Research Date:** 2026-07-15

**Timezone:** Asia/Shanghai

**Strict Window:** 2026-07-14 09:00:00 ～ 2026-07-15 09:00:00（北京时间，左闭右开）

**Contract:** V2.1 Full Replay；SRC-DATACITE 是 SRC-ARXIV 的注册恢复 fallback，只作 identity/date metadata；技术 claim 回到精确 arXiv v1 或可追溯历史全文审阅

**Status:** Complete；Coverage、Evidence、Books 与 fresh-context Semantic Audit 均无未解决 finding

## Executive Summary

本窗口枚举到 1111 个唯一 arXiv v1 identity；按合同 category 与 AI-System title route 去重后，候选分母冻结为 21 个。当前路由账目为 7 个 Deep、6 个 Standard、8 个 Closure；route 只是审阅义务，不等于 Review 已完成。

本轮没有把 DataCite metadata 或旧 Weekly prose 冒充 primary manuscript。旧 Weekly 只提供 identity、owner 与恢复线索；缺少事件时 evidence version、route locator、claim boundary、RP 和 Prior Review Ref 的 family 一律保持 pending/blocked。只有具备精确 primary receipt 的 family 才能完成评分、Selection 与 Books Decision。

## 1. Coverage

<!-- validator:report-metadata-v2 -->
| Field | Value |
| --- | --- |
| Contract Version | V2.1 |
| Score Schema | V2 |
| Report Type | Daily |
| Window Start | 2026-07-15 |
| Window End | 2026-07-15 |
| Registry Version | 2026-08-25 |
| Coverage Mode | Full Replay |
| Baseline Report | — |
| Changed Source IDs | — |
| Previous Denominator ID | — |
| Denominator ID | daily-2026-07-15-0900-v2.1-july-replay-01 |
| Denominator Frozen At | 2026-08-26T18:00:00+08:00 |
| Completion Status | Complete |
| Coverage Gate | Closed |
| Evidence Gate | Passed |
| Books Gate | Passed |

### Source Coverage Receipt

<!-- validator:source-coverage-v2 -->
| Source ID | Window Start | Window End | Executed At | Endpoint / Filter | Result | Hits | Candidate Source Families | Pagination / Cursor | Window Watermark | Closure Evidence | Gap / Limitation ID |
| --- | --- | --- | --- | --- | --- | ---: | --- | --- | --- | --- | --- |
| SRC-ARXIV | 2026-07-14T09:00:00+08:00 | 2026-07-15T09:00:00+08:00 | 2026-08-26T18:00:00+08:00 | registered SRC-DATACITE fallback; arXiv DOI identity + subjects + v1 Submitted timestamp; exact 09:00 bucket | checked | 1111 | SF-2026-ARXIV-2607-12273<br>SF-2026-ARXIV-2607-12287<br>SF-2026-ARXIV-2607-12356<br>SF-2026-ARXIV-2607-14145<br>SF-2026-ARXIV-2607-12395<br>SF-2026-ARXIV-2607-12463<br>SF-2026-ARXIV-2607-12550<br>SF-2026-ARXIV-2607-12571<br>SF-2026-ARXIV-2607-12625<br>SF-2026-ARXIV-2607-12650<br>SF-2026-ARXIV-2607-12747<br>SF-2026-ARXIV-2607-12839<br>SF-2026-ARXIV-2607-12875<br>SF-2026-ARXIV-2607-12886<br>SF-2026-ARXIV-2607-12931<br>SF-2026-ARXIV-2607-13124<br>SF-2026-ARXIV-2607-13027<br>SF-2026-ARXIV-2607-13157<br>SF-2026-ARXIV-2607-13179<br>SF-2026-ARXIV-2607-13205<br>SF-2026-ARXIV-2607-13285 | five disjoint DOI-prefix groups; page size=1000; every group reached total; identifiers unique | 2026-07-15T09:00:00+08:00 | coverage:SRC-ARXIV:20260715 | GAP-ARXIV-DIRECT-RESET-20260715 |

<!-- coverage:SRC-ARXIV:20260715:start -->Direct arXiv API/OAI reset connections; registered DataCite fallback froze the strict-window denominator. Canonical source: papers/2026/07/_sources/datacite-arxiv-recovery-20260701-26/datacite-candidate-inventory.json; sha256:d9c5e832203e6c3940bbf234cbbb0fff9e69bcdf1964db69b901cd19b8de6e29; 1111 unique identities in this strict window; 21 routed families.<!-- coverage:SRC-ARXIV:20260715:end -->

### Coverage Limitations

- DataCite 是 Discovery / Metadata fallback，只证明 identity、v1 timestamp、subject 与 abstract；机制和实验结论不从 metadata 推断。
- Artifact-boundary routing 覆盖 21 个 family：exact v1 为 9 个 family 披露 artifact/evidence locator，其中 9 个提供外部 repository/project/demo locator，另有 12 个未披露；本日确认 0 个 family、0 个 event-time pinned commit。未确认 pinned commit 的 locator 只进入 Evidence boundary，不冒充 `SRC-GITHUB-COMMIT` coverage hit。
- 2026-08-25 才生效的机构源与 Hugging Face 不倒推为本历史窗口 Required Daily。工程 release 仍由 Sunday Weekly 承担。
- 标题路由外的垂直应用、单数据集增量和没有状态/控制权变化的论文在 topic-level closure 中拒绝，不用大量零分行稀释账本。

## 2. Candidate Ledger

<!-- validator:candidate-ledger-v2.1 -->
| Source Family ID | Primary Identifier | Event Identity | Owner Week | First-public Date | Supporting Source IDs | Design Delta | System Reach | Durability | Total | Candidate State | Review Status | Access Status | Review Override | Review Ref | Owner Report Ref | Prior Review Ref | Reconciliation | Stable Node ID | Books Disposition | Books Review Ref | Benchmark Claim |
| --- | --- | --- | --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2607-12273 | arXiv:2607.12273v1 | paper-v1:2607.12273 | 2026-W29 | 2026-07-14 | SRC-ARXIV | 1 | 2 | 0 | 3 | closure_only | closure_complete | accessible | none | review:SF-2026-ARXIV-2607-12273 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Rejected — Low Durability / Out of Scope | — | no |
| SF-2026-ARXIV-2607-12287 | arXiv:2607.12287v1 | paper-v1:2607.12287 | 2026-W29 | 2026-07-14 | SRC-ARXIV | 1 | 2 | 1 | 4 | closure_only | closure_complete | accessible | none | review:SF-2026-ARXIV-2607-12287 | self | — | new_in_window | MULTIMODAL-EMBODIED-VLA | Rejected — Low Durability / Out of Scope | — | no |
| SF-2026-ARXIV-2607-12356 | arXiv:2607.12356v1 | paper-v1:2607.12356 | 2026-W29 | 2026-07-14 | SRC-ARXIV | 1 | 2 | 1 | 4 | closure_only | closure_complete | accessible | none | review:SF-2026-ARXIV-2607-12356 | self | — | new_in_window | MULTIMODAL-EMBODIED-VLA | Rejected — Low Durability / Out of Scope | — | no |
| SF-2026-ARXIV-2607-14145 | arXiv:2607.14145v1 | paper-v1:2607.14145 | 2026-W29 | 2026-07-14 | SRC-ARXIV | 1 | 2 | 1 | 4 | closure_only | closure_complete | accessible | none | review:SF-2026-ARXIV-2607-14145 | self | — | new_in_window | AGENT-TOOL-CALLING | Rejected — Low Durability / Out of Scope | — | no |
| SF-2026-ARXIV-2607-12395 | arXiv:2607.12395v1 | paper-v1:2607.12395 | 2026-W29 | 2026-07-14 | SRC-ARXIV | 3 | 3 | 2 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-12395 | self | — | new_in_window | TRAIN-RLHF | Integrate | books-review:SF-2026-ARXIV-2607-12395 | yes |
| SF-2026-ARXIV-2607-12463 | arXiv:2607.12463v1 | paper-v1:2607.12463 | 2026-W29 | 2026-07-14 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2607-12463 | self | — | new_in_window | TRAIN-PRETRAINING | Integrate | books-review:SF-2026-ARXIV-2607-12463 | yes |
| SF-2026-ARXIV-2607-12550 | arXiv:2607.12550v1 | paper-v1:2607.12550 | 2026-W29 | 2026-07-14 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-12550 | self | — | new_in_window | INFER-KV-CACHE | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2607-12550 | yes |
| SF-2026-ARXIV-2607-12571 | arXiv:2607.12571v1 | paper-v1:2607.12571 | 2026-W29 | 2026-07-14 | SRC-ARXIV | 1 | 2 | 1 | 4 | closure_only | closure_complete | accessible | none | review:SF-2026-ARXIV-2607-12571 | self | — | new_in_window | MULTIMODAL-EMBODIED-VLA | Rejected — Low Durability / Out of Scope | — | no |
| SF-2026-ARXIV-2607-12625 | arXiv:2607.12625v1 | paper-v1:2607.12625 | 2026-W29 | 2026-07-14 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-12625 | self | — | new_in_window | AGENT-MEMORY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2607-12625 | yes |
| SF-2026-ARXIV-2607-12650 | arXiv:2607.12650v1 | paper-v1:2607.12650 | 2026-W29 | 2026-07-14 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-12650 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2607-12650 | yes |
| SF-2026-ARXIV-2607-12747 | arXiv:2607.12747v1 | paper-v1:2607.12747 | 2026-W29 | 2026-07-14 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2607-12747 | self | — | new_in_window | PLATFORM-TRACE | Integrate | books-review:SF-2026-ARXIV-2607-12747 | yes |
| SF-2026-ARXIV-2607-12839 | arXiv:2607.12839v1 | paper-v1:2607.12839 | 2026-W29 | 2026-07-14 | SRC-ARXIV | 2 | 3 | 2 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-12839 | self | — | new_in_window | INFER-TENSORRT-LLM | Integrate | books-review:SF-2026-ARXIV-2607-12839 | yes |
| SF-2026-ARXIV-2607-12875 | arXiv:2607.12875v1 | paper-v1:2607.12875 | 2026-W29 | 2026-07-14 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-12875 | self | — | new_in_window | INFER-TENSORRT-LLM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2607-12875 | yes |
| SF-2026-ARXIV-2607-12886 | arXiv:2607.12886v1 | paper-v1:2607.12886 | 2026-W29 | 2026-07-14 | SRC-ARXIV | 1 | 2 | 0 | 3 | closure_only | closure_complete | accessible | none | review:SF-2026-ARXIV-2607-12886 | self | — | new_in_window | AGENT-MULTI-AGENT | Rejected — Low Durability / Out of Scope | — | no |
| SF-2026-ARXIV-2607-12931 | arXiv:2607.12931v1 | paper-v1:2607.12931 | 2026-W29 | 2026-07-15 | SRC-ARXIV | 1 | 2 | 0 | 3 | closure_only | closure_complete | accessible | none | review:SF-2026-ARXIV-2607-12931 | self | — | new_in_window | MULTIMODAL-EMBODIED-VLA | Rejected — Low Durability / Out of Scope | — | no |
| SF-2026-ARXIV-2607-13124 | arXiv:2607.13124v1 | paper-v1:2607.13124 | 2026-W29 | 2026-07-15 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2607-13124 | self | — | new_in_window | TRAIN-GRPO | Integrate | books-review:SF-2026-ARXIV-2607-13124 | yes |
| SF-2026-ARXIV-2607-13027 | arXiv:2607.13027v1 | paper-v1:2607.13027 | 2026-W29 | 2026-07-15 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-13027 | self | — | new_in_window | AGENT-PLATFORM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2607-13027 | yes |
| SF-2026-ARXIV-2607-13157 | arXiv:2607.13157v1 | paper-v1:2607.13157 | 2026-W29 | 2026-07-15 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-13157 | self | — | new_in_window | AGENT-MEMORY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2607-13157 | yes |
| SF-2026-ARXIV-2607-13179 | arXiv:2607.13179v1 | paper-v1:2607.13179 | 2026-W29 | 2026-07-15 | SRC-ARXIV | 1 | 2 | 1 | 4 | closure_only | closure_complete | accessible | none | review:SF-2026-ARXIV-2607-13179 | self | — | new_in_window | AGENT-MULTI-AGENT | Rejected — Low Durability / Out of Scope | — | no |
| SF-2026-ARXIV-2607-13205 | arXiv:2607.13205v1 | paper-v1:2607.13205 | 2026-W29 | 2026-07-15 | SRC-ARXIV | 3 | 3 | 2 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-13205 | self | — | new_in_window | INFER-KV-CACHE | Integrate | books-review:SF-2026-ARXIV-2607-13205 | yes |
| SF-2026-ARXIV-2607-13285 | arXiv:2607.13285v1 | paper-v1:2607.13285 | 2026-W29 | 2026-07-15 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-13285 | self | — | new_in_window | AGENT-WORKFLOW | Integrate | books-review:SF-2026-ARXIV-2607-13285 | yes |

## 3. Review Completion Receipt

<!-- validator:review-completion-v1 -->
| Source Family ID | Review Provenance ID | Review Route | Primary Evidence Version | Reviewed Evidence Versions | Method / Identity Locators | Evaluation Locators | Limitations / Counterevidence Locators | Artifact Locators | Claim Boundary Ref | Completion Result |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2607-12273 | RP-0abff2bbaa14680c | closure | doi:10.48550/arxiv.2607.12273@v1 | SRC-DATACITE@doi:10.48550/arxiv.2607.12273@v1 | doi:10.48550/arxiv.2607.12273#identity; DataCite Submitted:v1 timestamp | Not Required — closure route makes no mechanism or benchmark claim | Not Required — DataCite abstract is Discovery / Metadata and no technical claim is retained | Not Required — closure route; no artifact claim retained | claim:SF-2026-ARXIV-2607-12273 | complete |
| SF-2026-ARXIV-2607-12287 | RP-5ffdda8f34b9ff67 | closure | doi:10.48550/arxiv.2607.12287@v1 | SRC-DATACITE@doi:10.48550/arxiv.2607.12287@v1 | doi:10.48550/arxiv.2607.12287#identity; DataCite Submitted:v1 timestamp | Not Required — closure route makes no mechanism or benchmark claim | Not Required — DataCite abstract is Discovery / Metadata and no technical claim is retained | Not Required — closure route; no artifact claim retained | claim:SF-2026-ARXIV-2607-12287 | complete |
| SF-2026-ARXIV-2607-12356 | RP-bfbf308966446143 | closure | doi:10.48550/arxiv.2607.12356@v1 | SRC-DATACITE@doi:10.48550/arxiv.2607.12356@v1 | doi:10.48550/arxiv.2607.12356#identity; DataCite Submitted:v1 timestamp | Not Required — closure route makes no mechanism or benchmark claim | Not Required — DataCite abstract is Discovery / Metadata and no technical claim is retained | Not Required — closure route; no artifact claim retained | claim:SF-2026-ARXIV-2607-12356 | complete |
| SF-2026-ARXIV-2607-14145 | RP-60ffb25bc0b4ca32 | closure | doi:10.48550/arxiv.2607.14145@v1 | SRC-DATACITE@doi:10.48550/arxiv.2607.14145@v1 | doi:10.48550/arxiv.2607.14145#identity; DataCite Submitted:v1 timestamp | Not Required — closure route makes no mechanism or benchmark claim | Not Required — DataCite abstract is Discovery / Metadata and no technical claim is retained | Not Required — closure route; no artifact claim retained | claim:SF-2026-ARXIV-2607-14145 | complete |
| SF-2026-ARXIV-2607-12395 | RP-ff08a3c5534b817a | deep | arXiv:2607.12395v1 | SRC-ARXIV@arXiv:2607.12395v1 | https://arxiv.org/html/2607.12395v1#S3 | https://arxiv.org/html/2607.12395v1#S4 | https://arxiv.org/html/2607.12395v1#S5 | https://github.com/THUDM/slime (paper-linked dependency; no immutable Ring-Zero release established) | claim:SF-2026-ARXIV-2607-12395 | complete |
| SF-2026-ARXIV-2607-12463 | RP-8cde43cd1adf6258 | deep | arXiv:2607.12463v1 | SRC-ARXIV@arXiv:2607.12463v1 | https://arxiv.org/html/2607.12463v1#S3 | https://arxiv.org/html/2607.12463v1#S4 | https://arxiv.org/html/2607.12463v1#S6 | https://github.com/TIGER-AI-Lab/FIM-Midtraining | claim:SF-2026-ARXIV-2607-12463 | complete |
| SF-2026-ARXIV-2607-12550 | RP-3f2522220543a4f4 | standard | arXiv:2607.12550v1 | SRC-ARXIV@arXiv:2607.12550v1 | https://arxiv.org/html/2607.12550v1#S3 | https://arxiv.org/html/2607.12550v1#S4 | https://arxiv.org/html/2607.12550v1#S5 | Not Disclosed — exact v1 provides no source locator for artifact; No author implementation linked in v1 | claim:SF-2026-ARXIV-2607-12550 | complete |
| SF-2026-ARXIV-2607-12571 | RP-2c006cb9b06f0009 | closure | doi:10.48550/arxiv.2607.12571@v1 | SRC-DATACITE@doi:10.48550/arxiv.2607.12571@v1 | doi:10.48550/arxiv.2607.12571#identity; DataCite Submitted:v1 timestamp | Not Required — closure route makes no mechanism or benchmark claim | Not Required — DataCite abstract is Discovery / Metadata and no technical claim is retained | Not Required — closure route; no artifact claim retained | claim:SF-2026-ARXIV-2607-12571 | complete |
| SF-2026-ARXIV-2607-12625 | RP-b7c171683a083f56 | standard | arXiv:2607.12625v1 | SRC-ARXIV@arXiv:2607.12625v1 | https://arxiv.org/html/2607.12625v1#S3 | https://arxiv.org/html/2607.12625v1#S4 | https://arxiv.org/html/2607.12625v1#S5 | https://github.com/HITsz-TMG/KnowAct/releases/tag/Result | claim:SF-2026-ARXIV-2607-12625 | complete |
| SF-2026-ARXIV-2607-12650 | RP-77137eb583a52196 | standard | arXiv:2607.12650v1 | SRC-ARXIV@arXiv:2607.12650v1 | https://arxiv.org/html/2607.12650v1#S3 | https://arxiv.org/html/2607.12650v1#S4 | https://arxiv.org/html/2607.12650v1#S5 | https://github.com/7pocheR/eg-var/commit/88160519ce03dbd824f62799c1d3e1a02794a6e8 (paper-disclosed pinned commit; event-time artifact not independently fetched and not used as reviewed evidence) | claim:SF-2026-ARXIV-2607-12650 | complete |
| SF-2026-ARXIV-2607-12747 | RP-ddf839265a53cdcf | deep | arXiv:2607.12747v1 | SRC-ARXIV@arXiv:2607.12747v1 | https://arxiv.org/html/2607.12747v1#S3 | https://arxiv.org/html/2607.12747v1#S4 | https://arxiv.org/html/2607.12747v1#S5 | Not Disclosed — exact v1 provides no source locator for artifact; No author implementation linked in v1 | claim:SF-2026-ARXIV-2607-12747 | complete |
| SF-2026-ARXIV-2607-12839 | RP-c98b50f551d57b0a | deep | arXiv:2607.12839v1 | SRC-ARXIV@arXiv:2607.12839v1 | https://arxiv.org/html/2607.12839v1#S4 | https://arxiv.org/html/2607.12839v1#S5 | https://arxiv.org/html/2607.12839v1#S6 | https://github.com/FastFlowLM/FastFlowLM (referenced runtime; paper-specific commit not established) | claim:SF-2026-ARXIV-2607-12839 | complete |
| SF-2026-ARXIV-2607-12875 | RP-0771c294e8557d30 | standard | arXiv:2607.12875v1 | SRC-ARXIV@arXiv:2607.12875v1 | https://arxiv.org/html/2607.12875v1#S3 | https://arxiv.org/html/2607.12875v1#S4 | https://arxiv.org/html/2607.12875v1#S5 | https://github.com/MetaInfer/MetaInfer | claim:SF-2026-ARXIV-2607-12875 | complete |
| SF-2026-ARXIV-2607-12886 | RP-c1ec940590b398b7 | closure | doi:10.48550/arxiv.2607.12886@v1 | SRC-DATACITE@doi:10.48550/arxiv.2607.12886@v1 | doi:10.48550/arxiv.2607.12886#identity; DataCite Submitted:v1 timestamp | Not Required — closure route makes no mechanism or benchmark claim | Not Required — DataCite abstract is Discovery / Metadata and no technical claim is retained | Not Required — closure route; no artifact claim retained | claim:SF-2026-ARXIV-2607-12886 | complete |
| SF-2026-ARXIV-2607-12931 | RP-4ea823b12d21e007 | closure | doi:10.48550/arxiv.2607.12931@v1 | SRC-DATACITE@doi:10.48550/arxiv.2607.12931@v1 | doi:10.48550/arxiv.2607.12931#identity; DataCite Submitted:v1 timestamp | Not Required — closure route makes no mechanism or benchmark claim | Not Required — DataCite abstract is Discovery / Metadata and no technical claim is retained | Not Required — closure route; no artifact claim retained | claim:SF-2026-ARXIV-2607-12931 | complete |
| SF-2026-ARXIV-2607-13124 | RP-2ea6aa9883672b92 | deep | arXiv:2607.13124v1 | SRC-ARXIV@arXiv:2607.13124v1 | https://arxiv.org/html/2607.13124v1#S3 | https://arxiv.org/html/2607.13124v1#S4 | https://arxiv.org/html/2607.13124v1#S6 | https://github.com/icip-cas/ShortX | claim:SF-2026-ARXIV-2607-13124 | complete |
| SF-2026-ARXIV-2607-13027 | RP-8134850c92e423b3 | standard | arXiv:2607.13027v1 | SRC-ARXIV@arXiv:2607.13027v1 | https://arxiv.org/html/2607.13027v1#S3 | https://arxiv.org/html/2607.13027v1#S4 | https://arxiv.org/html/2607.13027v1#S5 | https://github.com/ModalityDance/PalmClaw/releases/latest (mutable latest pointer; event-time immutable release not established) | claim:SF-2026-ARXIV-2607-13027 | complete |
| SF-2026-ARXIV-2607-13157 | RP-5676fec12518bf05 | standard | arXiv:2607.13157v1 | SRC-ARXIV@arXiv:2607.13157v1 | https://arxiv.org/html/2607.13157v1#S4 | https://arxiv.org/html/2607.13157v1#S7 | https://arxiv.org/html/2607.13157v1#S9 | Not Disclosed — exact v1 provides no source locator for artifact; No paper-specific immutable repository linked | claim:SF-2026-ARXIV-2607-13157 | complete |
| SF-2026-ARXIV-2607-13179 | RP-5e2877dad5932500 | closure | doi:10.48550/arxiv.2607.13179@v1 | SRC-DATACITE@doi:10.48550/arxiv.2607.13179@v1 | doi:10.48550/arxiv.2607.13179#identity; DataCite Submitted:v1 timestamp | Not Required — closure route makes no mechanism or benchmark claim | Not Required — DataCite abstract is Discovery / Metadata and no technical claim is retained | Not Required — closure route; no artifact claim retained | claim:SF-2026-ARXIV-2607-13179 | complete |
| SF-2026-ARXIV-2607-13205 | RP-70ad05c95e8ffcb8 | deep | arXiv:2607.13205v1 | SRC-ARXIV@arXiv:2607.13205v1 | https://arxiv.org/html/2607.13205v1#S3 | https://arxiv.org/html/2607.13205v1#S4 | https://arxiv.org/html/2607.13205v1#S5 | Not Disclosed — exact v1 provides no source locator for artifact; No author implementation linked in v1 | claim:SF-2026-ARXIV-2607-13205 | complete |
| SF-2026-ARXIV-2607-13285 | RP-7f08608c5a000f49 | deep | arXiv:2607.13285v1 | SRC-ARXIV@arXiv:2607.13285v1 | https://arxiv.org/html/2607.13285v1#S3 | https://arxiv.org/html/2607.13285v1#S4 | https://arxiv.org/html/2607.13285v1#S5 | https://ruhan-wang.github.io/Harness-Handbook/ | claim:SF-2026-ARXIV-2607-13285 | complete |

### Source Reviews

<!-- review:SF-2026-ARXIV-2607-12273:start -->
#### Code-MUE: Measuring Code LLMs' Uncertainty through Execution-based Semantic Interaction Graphs

<!-- claim:SF-2026-ARXIV-2607-12273:start -->本次只确认唯一 arXiv identity、v1 Submitted timestamp、owner Daily 与主题拒绝；DataCite abstract 不用于建立机制或 benchmark 结论。<!-- claim:SF-2026-ARXIV-2607-12273:end -->

- Identity：`arXiv:2607.12273v1`；first-public（Asia/Shanghai）：`2026-07-14`。
- Reconciliation：当前严格窗口内首次出现，无同层级 duplicate 或 revision。
- Closure rationale：标题与摘要触发系统主题路由，但当前证据只支持局部案例、调查或实现线索；在没有形成可验证的跨组件设计变化前，Design Delta / System Reach / Durability 为 `1/2/0`。
- Disposition：`Rejected — Low Durability / Out of Scope`；若未来 revision、artifact 或独立复现改变证据边界，重开真实 owner Daily。
<!-- review:SF-2026-ARXIV-2607-12273:end -->

<!-- review:SF-2026-ARXIV-2607-12287:start -->
#### Reducing Temporal Redundancy for Efficient Vision-Language-Action Inference

<!-- claim:SF-2026-ARXIV-2607-12287:start -->本次只确认唯一 arXiv identity、v1 Submitted timestamp、owner Daily 与主题拒绝；DataCite abstract 不用于建立机制或 benchmark 结论。<!-- claim:SF-2026-ARXIV-2607-12287:end -->

- Identity：`arXiv:2607.12287v1`；first-public（Asia/Shanghai）：`2026-07-14`。
- Reconciliation：当前严格窗口内首次出现，无同层级 duplicate 或 revision。
- Closure rationale：标题与摘要触发系统主题路由，但当前证据只支持局部案例、调查或实现线索；在没有形成可验证的跨组件设计变化前，Design Delta / System Reach / Durability 为 `1/2/1`。
- Disposition：`Rejected — Low Durability / Out of Scope`；若未来 revision、artifact 或独立复现改变证据边界，重开真实 owner Daily。
<!-- review:SF-2026-ARXIV-2607-12287:end -->

<!-- review:SF-2026-ARXIV-2607-12356:start -->
#### VistaVLA: Geometry- and Semantic-Aware 3D Gaussian-Grounded VLA for Robotic Manipulation

<!-- claim:SF-2026-ARXIV-2607-12356:start -->本次只确认唯一 arXiv identity、v1 Submitted timestamp、owner Daily 与主题拒绝；DataCite abstract 不用于建立机制或 benchmark 结论。<!-- claim:SF-2026-ARXIV-2607-12356:end -->

- Identity：`arXiv:2607.12356v1`；first-public（Asia/Shanghai）：`2026-07-14`。
- Reconciliation：当前严格窗口内首次出现，无同层级 duplicate 或 revision。
- Closure rationale：标题与摘要触发系统主题路由，但当前证据只支持局部案例、调查或实现线索；在没有形成可验证的跨组件设计变化前，Design Delta / System Reach / Durability 为 `1/2/1`。
- Disposition：`Rejected — Low Durability / Out of Scope`；若未来 revision、artifact 或独立复现改变证据边界，重开真实 owner Daily。
<!-- review:SF-2026-ARXIV-2607-12356:end -->

<!-- review:SF-2026-ARXIV-2607-14145:start -->
#### ToolAnchor: Anchoring Counterfactual Context to Boost Agentic Tool-use Capability

<!-- claim:SF-2026-ARXIV-2607-14145:start -->本次只确认唯一 arXiv identity、v1 Submitted timestamp、owner Daily 与主题拒绝；DataCite abstract 不用于建立机制或 benchmark 结论。<!-- claim:SF-2026-ARXIV-2607-14145:end -->

- Identity：`arXiv:2607.14145v1`；first-public（Asia/Shanghai）：`2026-07-14`。
- Reconciliation：当前严格窗口内首次出现，无同层级 duplicate 或 revision。
- Closure rationale：标题与摘要触发系统主题路由，但当前证据只支持局部案例、调查或实现线索；在没有形成可验证的跨组件设计变化前，Design Delta / System Reach / Durability 为 `1/2/1`。
- Disposition：`Rejected — Low Durability / Out of Scope`；若未来 revision、artifact 或独立复现改变证据边界，重开真实 owner Daily。
<!-- review:SF-2026-ARXIV-2607-14145:end -->

<!-- review:SF-2026-ARXIV-2607-12395:start -->
#### Ring-Zero: Scaling Zero RL to a Trillion Parameters for Emergent Reasoning

<!-- claim:SF-2026-ARXIV-2607-12395:start -->The pipeline combines clipped importance sampling, training-engine numerator correction, KL control, mixed-precision safeguards and context-parallel communication optimization; staged self-distillation/RL and length-conditioned modes separate discovery, sharpening and adaptive inference depth. 该结论只在论文公开的 workload 与 evaluation contract 内成立，不外推为通用生产结论。<!-- claim:SF-2026-ARXIV-2607-12395:end -->

**旧方案与约束变化。** `本章的核心判断是：**RLHF 将人类对候选输出的相对判断拟合成 reward signal，再在不偏离参考策略过远的约束下提高期望 reward。**它把难以形式化的行为目标转成可优化代理，也把标注偏差、reward hacking 和在线 rollout 成本带进训练系统。`（`books/part-04-training-system/31-rlhf.md#L14-L14`）旧方案在状态局部、规模较小或 SLO 宽松时继续成立；本 family 面对的新增压力由其 v1 problem statement 和 method 明确限定。

**机制、状态与代价。** The pipeline combines clipped importance sampling, training-engine numerator correction, KL control, mixed-precision safeguards and context-parallel communication optimization; staged self-distillation/RL and length-conditioned modes separate discovery, sharpening and adaptive inference depth. 它改变 `TRAIN-RLHF` 下的 state/data/control contract，同时引入 metadata、校准/选择误差、额外执行或恢复责任；这些代价必须和收益在同一 workload 内计量。

**Evaluation contract。** Method：`https://arxiv.org/html/2607.12395v1#S3`；Evaluation：`https://arxiv.org/html/2607.12395v1#S4`；Limitations/Counterevidence：`https://arxiv.org/html/2607.12395v1#S5`；本次 RP 重新绑定历史 full-read coverage：`papers/2026/weekly/2026-W29/README.md#L447-L455`，其中具名记录了 Method、Evaluation 与 Boundary。未披露字段保持 `Not Disclosed`；作者结果不跨模型、硬件、精度、长度、batch、concurrency、SLO 或 evaluator 外推。

- Score V2：Design Delta 3 / System Reach 3 / Durability 2 = **8/9**。
- Evolution relation：`Direct Evolution`。
- Stable owner：`TRAIN-RLHF`。
- Books disposition：`Integrate`。
<!-- review:SF-2026-ARXIV-2607-12395:end -->

<!-- review:SF-2026-ARXIV-2607-12463:start -->
#### Function-Aware Fill-in-the-Middle as Mid-Training for Coding Agent Foundation Models

<!-- claim:SF-2026-ARXIV-2607-12463:start -->Program-dependency analysis selects function targets under complexity/inferability criteria; the model reconstructs the missing function with generated rationale before existing agentic post-training. 该结论只在论文公开的 workload 与 evaluation contract 内成立，不外推为通用生产结论。<!-- claim:SF-2026-ARXIV-2607-12463:end -->

**旧方案与约束变化。** `本章的核心判断是：**Pretraining 是在大规模数据分布上反复最小化 next-token negative log-likelihood，使参数逐步形成可复用表示与条件生成能力。**它提供通用能力底座，但 loss 下降不自动保证事实可靠、指令遵循或部署分布上的任务成功。`（`books/part-04-training-system/28-pretraining.md#L14-L14`）旧方案在状态局部、规模较小或 SLO 宽松时继续成立；本 family 面对的新增压力由其 v1 problem statement 和 method 明确限定。

**机制、状态与代价。** Program-dependency analysis selects function targets under complexity/inferability criteria; the model reconstructs the missing function with generated rationale before existing agentic post-training. 它改变 `TRAIN-PRETRAINING` 下的 state/data/control contract，同时引入 metadata、校准/选择误差、额外执行或恢复责任；这些代价必须和收益在同一 workload 内计量。

**Evaluation contract。** Method：`https://arxiv.org/html/2607.12463v1#S3`；Evaluation：`https://arxiv.org/html/2607.12463v1#S4`；Limitations/Counterevidence：`https://arxiv.org/html/2607.12463v1#S6`；本次 RP 重新绑定历史 full-read coverage：`papers/2026/weekly/2026-W29/README.md#L956-L965`，其中具名记录了 Method、Evaluation 与 Boundary。未披露字段保持 `Not Disclosed`；作者结果不跨模型、硬件、精度、长度、batch、concurrency、SLO 或 evaluator 外推。

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Evolution relation：`Direct Evolution`。
- Stable owner：`TRAIN-PRETRAINING`。
- Books disposition：`Integrate`。
<!-- review:SF-2026-ARXIV-2607-12463:end -->

<!-- review:SF-2026-ARXIV-2607-12550:start -->
#### A JoLT for the KV cache: Near-lossless KV cache compression via joint Lagrangian allocation of Tucker ranks and a rotated residual for LLMs

<!-- claim:SF-2026-ARXIV-2607-12550:start -->Partial Tucker compression preserves head/layer axes, compresses token/feature axes and encodes truncation residual through a JL rotation plus low bits; one Lagrangian dual jointly allocates ranks and residual widths under a byte cap. 该结论只在论文公开的 workload 与 evaluation contract 内成立，不外推为通用生产结论。<!-- claim:SF-2026-ARXIV-2607-12550:end -->

**旧方案与约束变化。** `本章的核心判断是：**KV Cache 利用 causal decoding 中历史 K/V 不再变化的性质，以随序列增长的 memory state 换取历史 layer computation 不重算；它加速 Decode，也把请求从无状态输入变成必须管理生命周期和 ownership 的系统对象。**`（`books/part-05-inference-system/45-why-kv-cache-speeds-up.md#L14-L14`）旧方案在状态局部、规模较小或 SLO 宽松时继续成立；本 family 面对的新增压力由其 v1 problem statement 和 method 明确限定。

**机制、状态与代价。** Partial Tucker compression preserves head/layer axes, compresses token/feature axes and encodes truncation residual through a JL rotation plus low bits; one Lagrangian dual jointly allocates ranks and residual widths under a byte cap. 它改变 `INFER-KV-CACHE` 下的 state/data/control contract，同时引入 metadata、校准/选择误差、额外执行或恢复责任；这些代价必须和收益在同一 workload 内计量。

**Evaluation contract。** Method：`https://arxiv.org/html/2607.12550v1#S3`；Evaluation：`https://arxiv.org/html/2607.12550v1#S4`；Limitations/Counterevidence：`https://arxiv.org/html/2607.12550v1#S5`。未披露字段保持 `Not Disclosed`；作者结果不跨模型、硬件、精度、长度、batch、concurrency、SLO 或 evaluator 外推。

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Evolution relation：`Layering / Dependency`。
- Stable owner：`INFER-KV-CACHE`。
- Books disposition：`No Change — Existing Coverage`。
<!-- review:SF-2026-ARXIV-2607-12550:end -->

<!-- review:SF-2026-ARXIV-2607-12571:start -->
#### TrustVLA: Mechanism-Guided Inference-Time Defense Against Vision-Language-Action Backdoors

<!-- claim:SF-2026-ARXIV-2607-12571:start -->本次只确认唯一 arXiv identity、v1 Submitted timestamp、owner Daily 与主题拒绝；DataCite abstract 不用于建立机制或 benchmark 结论。<!-- claim:SF-2026-ARXIV-2607-12571:end -->

- Identity：`arXiv:2607.12571v1`；first-public（Asia/Shanghai）：`2026-07-14`。
- Reconciliation：当前严格窗口内首次出现，无同层级 duplicate 或 revision。
- Closure rationale：标题与摘要触发系统主题路由，但当前证据只支持局部案例、调查或实现线索；在没有形成可验证的跨组件设计变化前，Design Delta / System Reach / Durability 为 `1/2/1`。
- Disposition：`Rejected — Low Durability / Out of Scope`；若未来 revision、artifact 或独立复现改变证据边界，重开真实 owner Daily。
<!-- review:SF-2026-ARXIV-2607-12571:end -->

<!-- review:SF-2026-ARXIV-2607-12625:start -->
#### KnowAct-GUIClaw: Know Deeply, Act Perfectly, Personal GUI Assistant with Self-Evolving Memory and Skill

<!-- claim:SF-2026-ARXIV-2607-12625:start -->Know–Route–Act–Reflect separates host orchestration from GUI execution, maintains attribution-aware memory and state-validated skills, and transfers typed blackboard data between applications. 该结论只在论文公开的 workload 与 evaluation contract 内成立，不外推为通用生产结论。<!-- claim:SF-2026-ARXIV-2607-12625:end -->

**旧方案与约束变化。** `本章的核心判断是：**Memory 是跨模型调用保存并重新选择状态的机制，由 storage、write policy、retrieval policy、consolidation、forgetting 和 authorization 共同构成；它不是模型意识，也不是无限 Context。**`（`books/part-07-agent/77-memory.md#L14-L14`）旧方案在状态局部、规模较小或 SLO 宽松时继续成立；本 family 面对的新增压力由其 v1 problem statement 和 method 明确限定。

**机制、状态与代价。** Know–Route–Act–Reflect separates host orchestration from GUI execution, maintains attribution-aware memory and state-validated skills, and transfers typed blackboard data between applications. 它改变 `AGENT-MEMORY` 下的 state/data/control contract，同时引入 metadata、校准/选择误差、额外执行或恢复责任；这些代价必须和收益在同一 workload 内计量。

**Evaluation contract。** Method：`https://arxiv.org/html/2607.12625v1#S3`；Evaluation：`https://arxiv.org/html/2607.12625v1#S4`；Limitations/Counterevidence：`https://arxiv.org/html/2607.12625v1#S5`；本次 RP 重新绑定历史 full-read coverage：`papers/2026/weekly/2026-W29/README.md#L976-L984`，其中具名记录了 Method、Evaluation 与 Boundary。未披露字段保持 `Not Disclosed`；作者结果不跨模型、硬件、精度、长度、batch、concurrency、SLO 或 evaluator 外推。

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Evolution relation：`Layering / Dependency`。
- Stable owner：`AGENT-MEMORY`。
- Books disposition：`No Change — Existing Coverage`。
<!-- review:SF-2026-ARXIV-2607-12625:end -->

<!-- review:SF-2026-ARXIV-2607-12650:start -->
#### Evidence-Grounded Verified Agentic Reasoning: A Path Toward Eliminating LLM Hallucination in Empirical Inference via Tool-Attested Kernel Proofs

<!-- claim:SF-2026-ARXIV-2607-12650:start -->Typed tool-attested leaves and curator-owned source lifts/axioms feed a proof object; only mkVerified constructs Verified, the Lean kernel checks the derivation, and failure yields Abstain plus a replay artifact. 该结论只在论文公开的 workload 与 evaluation contract 内成立，不外推为通用生产结论。<!-- claim:SF-2026-ARXIV-2607-12650:end -->

**旧方案与约束变化。** `本章的核心判断是：**Evaluation System 是把目标转化为可重复证据和受控决策的系统。它必须同时版本化被评估对象、输入分布、执行环境与 scorer，并显式表达不确定性、切片和风险；工具可以保存证据，但不能替组织定义什么算成功。**`（`books/part-06-ai-infrastructure/66-evaluation-system.md#L14-L14`）旧方案在状态局部、规模较小或 SLO 宽松时继续成立；本 family 面对的新增压力由其 v1 problem statement 和 method 明确限定。

**机制、状态与代价。** Typed tool-attested leaves and curator-owned source lifts/axioms feed a proof object; only mkVerified constructs Verified, the Lean kernel checks the derivation, and failure yields Abstain plus a replay artifact. 它改变 `PLATFORM-EVALUATION-SYSTEM` 下的 state/data/control contract，同时引入 metadata、校准/选择误差、额外执行或恢复责任；这些代价必须和收益在同一 workload 内计量。

**Evaluation contract。** Method：`https://arxiv.org/html/2607.12650v1#S3`；Evaluation：`https://arxiv.org/html/2607.12650v1#S4`；Limitations/Counterevidence：`https://arxiv.org/html/2607.12650v1#S5`。未披露字段保持 `Not Disclosed`；作者结果不跨模型、硬件、精度、长度、batch、concurrency、SLO 或 evaluator 外推。

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Evolution relation：`Layering / Dependency`。
- Stable owner：`PLATFORM-EVALUATION-SYSTEM`。
- Books disposition：`No Change — Existing Coverage`。
<!-- review:SF-2026-ARXIV-2607-12650:end -->

<!-- review:SF-2026-ARXIV-2607-12747:start -->
#### Tracing Agentic Failure from the Flow of Success

<!-- claim:SF-2026-ARXIV-2607-12747:start -->A latent continuous-time trajectory model learns normal flow from successful traces; deviations on failed traces yield step attribution, with conformal detection controlling thresholds. 该结论只在论文公开的 workload 与 evaluation contract 内成立，不外推为通用生产结论。<!-- claim:SF-2026-ARXIV-2607-12747:end -->

**旧方案与约束变化。** `本章的核心判断是：**Trace 通过传播 context，将一次分布式操作拆成有父子或 link 关系的 spans，从而重建 critical path；其价值取决于边界、语义和采样是否保留真正决策点。**`（`books/part-06-ai-infrastructure/69-trace.md#L14-L14`）旧方案在状态局部、规模较小或 SLO 宽松时继续成立；本 family 面对的新增压力由其 v1 problem statement 和 method 明确限定。

**机制、状态与代价。** A latent continuous-time trajectory model learns normal flow from successful traces; deviations on failed traces yield step attribution, with conformal detection controlling thresholds. 它改变 `PLATFORM-TRACE` 下的 state/data/control contract，同时引入 metadata、校准/选择误差、额外执行或恢复责任；这些代价必须和收益在同一 workload 内计量。

**Evaluation contract。** Method：`https://arxiv.org/html/2607.12747v1#S3`；Evaluation：`https://arxiv.org/html/2607.12747v1#S4`；Limitations/Counterevidence：`https://arxiv.org/html/2607.12747v1#S5`；本次 RP 重新绑定历史 full-read coverage：`papers/2026/weekly/2026-W29/README.md#L985-L995`，其中具名记录了 Method、Evaluation 与 Boundary。未披露字段保持 `Not Disclosed`；作者结果不跨模型、硬件、精度、长度、batch、concurrency、SLO 或 evaluator 外推。

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Evolution relation：`Direct Evolution`。
- Stable owner：`PLATFORM-TRACE`。
- Books disposition：`Integrate`。
<!-- review:SF-2026-ARXIV-2607-12747:end -->

<!-- review:SF-2026-ARXIV-2607-12839:start -->
#### HeteroMosaic: Exposing and Exploiting Heterogeneous Execution Opportunities for Energy-Efficient Edge LLM Inference

<!-- claim:SF-2026-ARXIV-2607-12839:start -->A heterogeneous roofline predicts opportunity; dependency-preserving microbatches expose overlap; trace-guided latency shaping jointly tunes assignment and schedule, with NPU-aware queues and custom GPU kernels. 该结论只在论文公开的 workload 与 evaluation contract 内成立，不外推为通用生产结论。<!-- claim:SF-2026-ARXIV-2607-12839:end -->

**旧方案与约束变化。** `本章的核心判断是：**TensorRT-LLM 的核心不是改变模型语义，而是把经过验证的模型资产转换为面向 NVIDIA GPU 的执行计划，并用专用 kernels、quantization、KV management 与 runtime scheduling 交付它。**`（`books/part-05-inference-system/49-tensorrt-llm.md#L14-L14`）旧方案在状态局部、规模较小或 SLO 宽松时继续成立；本 family 面对的新增压力由其 v1 problem statement 和 method 明确限定。

**机制、状态与代价。** A heterogeneous roofline predicts opportunity; dependency-preserving microbatches expose overlap; trace-guided latency shaping jointly tunes assignment and schedule, with NPU-aware queues and custom GPU kernels. 它改变 `INFER-TENSORRT-LLM` 下的 state/data/control contract，同时引入 metadata、校准/选择误差、额外执行或恢复责任；这些代价必须和收益在同一 workload 内计量。

**Evaluation contract。** Method：`https://arxiv.org/html/2607.12839v1#S4`；Evaluation：`https://arxiv.org/html/2607.12839v1#S5`；Limitations/Counterevidence：`https://arxiv.org/html/2607.12839v1#S6`。未披露字段保持 `Not Disclosed`；作者结果不跨模型、硬件、精度、长度、batch、concurrency、SLO 或 evaluator 外推。

- Score V2：Design Delta 2 / System Reach 3 / Durability 2 = **7/9**。
- Evolution relation：`Direct Evolution`。
- Stable owner：`INFER-TENSORRT-LLM`。
- Books disposition：`Integrate`。
<!-- review:SF-2026-ARXIV-2607-12839:end -->

<!-- review:SF-2026-ARXIV-2607-12875:start -->
#### MetaInfer: A Knowledge Only LLM Inference Engine Generator SKILL Toolbox

<!-- claim:SF-2026-ARXIV-2607-12875:start -->A contract knowledge base describes interfaces, shapes, state transitions and platform constraints; isolated implementation/review/verification agents synthesize and test a single-path engine, while controlled exploration consolidates successful new knowledge. 该结论只在论文公开的 workload 与 evaluation contract 内成立，不外推为通用生产结论。<!-- claim:SF-2026-ARXIV-2607-12875:end -->

**旧方案与约束变化。** `本章的核心判断是：**TensorRT-LLM 的核心不是改变模型语义，而是把经过验证的模型资产转换为面向 NVIDIA GPU 的执行计划，并用专用 kernels、quantization、KV management 与 runtime scheduling 交付它。**`（`books/part-05-inference-system/49-tensorrt-llm.md#L14-L14`）旧方案在状态局部、规模较小或 SLO 宽松时继续成立；本 family 面对的新增压力由其 v1 problem statement 和 method 明确限定。

**机制、状态与代价。** A contract knowledge base describes interfaces, shapes, state transitions and platform constraints; isolated implementation/review/verification agents synthesize and test a single-path engine, while controlled exploration consolidates successful new knowledge. 它改变 `INFER-TENSORRT-LLM` 下的 state/data/control contract，同时引入 metadata、校准/选择误差、额外执行或恢复责任；这些代价必须和收益在同一 workload 内计量。

**Evaluation contract。** Method：`https://arxiv.org/html/2607.12875v1#S3`；Evaluation：`https://arxiv.org/html/2607.12875v1#S4`；Limitations/Counterevidence：`https://arxiv.org/html/2607.12875v1#S5`。未披露字段保持 `Not Disclosed`；作者结果不跨模型、硬件、精度、长度、batch、concurrency、SLO 或 evaluator 外推。

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Evolution relation：`Layering / Dependency`。
- Stable owner：`INFER-TENSORRT-LLM`。
- Books disposition：`No Change — Existing Coverage`。
<!-- review:SF-2026-ARXIV-2607-12875:end -->

<!-- review:SF-2026-ARXIV-2607-12886:start -->
#### A Multi-Agent System for Autonomous, Fine-Tuning-Free Clinical Symptom Detection: Development and Validation Study

<!-- claim:SF-2026-ARXIV-2607-12886:start -->本次只确认唯一 arXiv identity、v1 Submitted timestamp、owner Daily 与主题拒绝；DataCite abstract 不用于建立机制或 benchmark 结论。<!-- claim:SF-2026-ARXIV-2607-12886:end -->

- Identity：`arXiv:2607.12886v1`；first-public（Asia/Shanghai）：`2026-07-14`。
- Reconciliation：当前严格窗口内首次出现，无同层级 duplicate 或 revision。
- Closure rationale：标题与摘要触发系统主题路由，但当前证据只支持局部案例、调查或实现线索；在没有形成可验证的跨组件设计变化前，Design Delta / System Reach / Durability 为 `1/2/0`。
- Disposition：`Rejected — Low Durability / Out of Scope`；若未来 revision、artifact 或独立复现改变证据边界，重开真实 owner Daily。
<!-- review:SF-2026-ARXIV-2607-12886:end -->

<!-- review:SF-2026-ARXIV-2607-12931:start -->
#### ExToken: Structured Exploration for Efficient Vision-Language-Action Reinforcement Fine-tuning

<!-- claim:SF-2026-ARXIV-2607-12931:start -->本次只确认唯一 arXiv identity、v1 Submitted timestamp、owner Daily 与主题拒绝；DataCite abstract 不用于建立机制或 benchmark 结论。<!-- claim:SF-2026-ARXIV-2607-12931:end -->

- Identity：`arXiv:2607.12931v1`；first-public（Asia/Shanghai）：`2026-07-15`。
- Reconciliation：当前严格窗口内首次出现，无同层级 duplicate 或 revision。
- Closure rationale：标题与摘要触发系统主题路由，但当前证据只支持局部案例、调查或实现线索；在没有形成可验证的跨组件设计变化前，Design Delta / System Reach / Durability 为 `1/2/0`。
- Disposition：`Rejected — Low Durability / Out of Scope`；若未来 revision、artifact 或独立复现改变证据边界，重开真实 owner Daily。
<!-- review:SF-2026-ARXIV-2607-12931:end -->

<!-- review:SF-2026-ARXIV-2607-13124:start -->
#### ShortOPD: Recovering Pruned LLMs with Short-to-Long On-Policy Distillation

<!-- claim:SF-2026-ARXIV-2607-13124:start -->On-policy distillation evaluates a frozen pre-pruning teacher on student samples; repetition/truncation feedback and two EMAs shrink early horizons then restore long generation as recovery improves. 该结论只在论文公开的 workload 与 evaluation contract 内成立，不外推为通用生产结论。<!-- claim:SF-2026-ARXIV-2607-13124:end -->

**旧方案与约束变化。** `本章的核心判断是：**GRPO 用同一 prompt 下多个 sampled responses 的组内 reward 统计构造相对 advantage，移除独立 learned critic，同时保留 policy ratio、clipping 与 reference regularization 的受限更新主线。**它减少 value-model 状态，不消除 rollout 成本、reward design 或 policy optimization 风险。`（`books/part-04-training-system/33-grpo.md#L14-L14`）旧方案在状态局部、规模较小或 SLO 宽松时继续成立；本 family 面对的新增压力由其 v1 problem statement 和 method 明确限定。

**机制、状态与代价。** On-policy distillation evaluates a frozen pre-pruning teacher on student samples; repetition/truncation feedback and two EMAs shrink early horizons then restore long generation as recovery improves. 它改变 `TRAIN-GRPO` 下的 state/data/control contract，同时引入 metadata、校准/选择误差、额外执行或恢复责任；这些代价必须和收益在同一 workload 内计量。

**Evaluation contract。** Method：`https://arxiv.org/html/2607.13124v1#S3`；Evaluation：`https://arxiv.org/html/2607.13124v1#S4`；Limitations/Counterevidence：`https://arxiv.org/html/2607.13124v1#S6`；本次 RP 重新绑定历史 full-read coverage：`papers/2026/weekly/2026-W29/README.md#L996-L1005`，其中具名记录了 Method、Evaluation 与 Boundary。未披露字段保持 `Not Disclosed`；作者结果不跨模型、硬件、精度、长度、batch、concurrency、SLO 或 evaluator 外推。

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Evolution relation：`Direct Evolution`。
- Stable owner：`TRAIN-GRPO`。
- Books disposition：`Integrate`。
<!-- review:SF-2026-ARXIV-2607-13124:end -->

<!-- review:SF-2026-ARXIV-2607-13027:start -->
#### PalmClaw: A Native On-Device Agent Framework for Mobile Phones

<!-- claim:SF-2026-ARXIV-2607-13027:start -->An on-device framework owns session loop, tools with typed arguments/results, shared/per-session memory and explicit execution boundaries; GUI remains a fallback branch. 该结论只在论文公开的 workload 与 evaluation contract 内成立，不外推为通用生产结论。<!-- claim:SF-2026-ARXIV-2607-13027:end -->

**旧方案与约束变化。** `本章的核心判断是：**Agent Platform 是 AI Platform 对有状态行动循环的扩展。它统一 Agent definition、run、context、memory、tools、workflow、evaluation 与 policy，但复用 Part VI 的 identity、resource、evidence、cost、tenancy、security 和 recovery substrate。**`（`books/part-07-agent/84-agent-platform.md#L14-L14`）旧方案在状态局部、规模较小或 SLO 宽松时继续成立；本 family 面对的新增压力由其 v1 problem statement 和 method 明确限定。

**机制、状态与代价。** An on-device framework owns session loop, tools with typed arguments/results, shared/per-session memory and explicit execution boundaries; GUI remains a fallback branch. 它改变 `AGENT-PLATFORM` 下的 state/data/control contract，同时引入 metadata、校准/选择误差、额外执行或恢复责任；这些代价必须和收益在同一 workload 内计量。

**Evaluation contract。** Method：`https://arxiv.org/html/2607.13027v1#S3`；Evaluation：`https://arxiv.org/html/2607.13027v1#S4`；Limitations/Counterevidence：`https://arxiv.org/html/2607.13027v1#S5`；本次 RP 重新绑定历史 full-read coverage：`papers/2026/weekly/2026-W29/README.md#L1006-L1015`，其中具名记录了 Method、Evaluation 与 Boundary。未披露字段保持 `Not Disclosed`；作者结果不跨模型、硬件、精度、长度、batch、concurrency、SLO 或 evaluator 外推。

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Evolution relation：`Layering / Dependency`。
- Stable owner：`AGENT-PLATFORM`。
- Books disposition：`No Change — Existing Coverage`。
<!-- review:SF-2026-ARXIV-2607-13027:end -->

<!-- review:SF-2026-ARXIV-2607-13157:start -->
#### Oracle Agent Memory as an Enterprise Memory Substrate for Long-Horizon AI Agents

<!-- claim:SF-2026-ARXIV-2607-13157:start -->A database-native lifecycle separates active context construction from passive scoped storage; it measures evidence retrieval, evidence use, task outcome and operational efficiency, with stable prefix/volatile suffix placement for cache compatibility. 该结论只在论文公开的 workload 与 evaluation contract 内成立，不外推为通用生产结论。<!-- claim:SF-2026-ARXIV-2607-13157:end -->

**旧方案与约束变化。** `本章的核心判断是：**Memory 是跨模型调用保存并重新选择状态的机制，由 storage、write policy、retrieval policy、consolidation、forgetting 和 authorization 共同构成；它不是模型意识，也不是无限 Context。**`（`books/part-07-agent/77-memory.md#L14-L14`）旧方案在状态局部、规模较小或 SLO 宽松时继续成立；本 family 面对的新增压力由其 v1 problem statement 和 method 明确限定。

**机制、状态与代价。** A database-native lifecycle separates active context construction from passive scoped storage; it measures evidence retrieval, evidence use, task outcome and operational efficiency, with stable prefix/volatile suffix placement for cache compatibility. 它改变 `AGENT-MEMORY` 下的 state/data/control contract，同时引入 metadata、校准/选择误差、额外执行或恢复责任；这些代价必须和收益在同一 workload 内计量。

**Evaluation contract。** Method：`https://arxiv.org/html/2607.13157v1#S4`；Evaluation：`https://arxiv.org/html/2607.13157v1#S7`；Limitations/Counterevidence：`https://arxiv.org/html/2607.13157v1#S9`。未披露字段保持 `Not Disclosed`；作者结果不跨模型、硬件、精度、长度、batch、concurrency、SLO 或 evaluator 外推。

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Evolution relation：`Layering / Dependency`。
- Stable owner：`AGENT-MEMORY`。
- Books disposition：`No Change — Existing Coverage`。
<!-- review:SF-2026-ARXIV-2607-13157:end -->

<!-- review:SF-2026-ARXIV-2607-13179:start -->
#### SoftBoard: A Multi-Agent Tool for the Creation and Evaluation of Low-Fidelity Prototypes

<!-- claim:SF-2026-ARXIV-2607-13179:start -->本次只确认唯一 arXiv identity、v1 Submitted timestamp、owner Daily 与主题拒绝；DataCite abstract 不用于建立机制或 benchmark 结论。<!-- claim:SF-2026-ARXIV-2607-13179:end -->

- Identity：`arXiv:2607.13179v1`；first-public（Asia/Shanghai）：`2026-07-15`。
- Reconciliation：当前严格窗口内首次出现，无同层级 duplicate 或 revision。
- Closure rationale：标题与摘要触发系统主题路由，但当前证据只支持局部案例、调查或实现线索；在没有形成可验证的跨组件设计变化前，Design Delta / System Reach / Durability 为 `1/2/1`。
- Disposition：`Rejected — Low Durability / Out of Scope`；若未来 revision、artifact 或独立复现改变证据边界，重开真实 owner Daily。
<!-- review:SF-2026-ARXIV-2607-13179:end -->

<!-- review:SF-2026-ARXIV-2607-13205:start -->
#### Adaptive Filtering of the KV Cache: Diagnosing and Correcting Structural-Role Bias in LLM Inference

<!-- claim:SF-2026-ARXIV-2607-13205:start -->The method labels structural roles, diagnoses attention allocation by role and applies adaptive role-aware correction before selection, retaining semantic leaves rather than structural scaffolding under tight budgets. 该结论只在论文公开的 workload 与 evaluation contract 内成立，不外推为通用生产结论。<!-- claim:SF-2026-ARXIV-2607-13205:end -->

**旧方案与约束变化。** `本章的核心判断是：**KV Cache 利用 causal decoding 中历史 K/V 不再变化的性质，以随序列增长的 memory state 换取历史 layer computation 不重算；它加速 Decode，也把请求从无状态输入变成必须管理生命周期和 ownership 的系统对象。**`（`books/part-05-inference-system/45-why-kv-cache-speeds-up.md#L14-L14`）旧方案在状态局部、规模较小或 SLO 宽松时继续成立；本 family 面对的新增压力由其 v1 problem statement 和 method 明确限定。

**机制、状态与代价。** The method labels structural roles, diagnoses attention allocation by role and applies adaptive role-aware correction before selection, retaining semantic leaves rather than structural scaffolding under tight budgets. 它改变 `INFER-KV-CACHE` 下的 state/data/control contract，同时引入 metadata、校准/选择误差、额外执行或恢复责任；这些代价必须和收益在同一 workload 内计量。

**Evaluation contract。** Method：`https://arxiv.org/html/2607.13205v1#S3`；Evaluation：`https://arxiv.org/html/2607.13205v1#S4`；Limitations/Counterevidence：`https://arxiv.org/html/2607.13205v1#S5`。未披露字段保持 `Not Disclosed`；作者结果不跨模型、硬件、精度、长度、batch、concurrency、SLO 或 evaluator 外推。

- Score V2：Design Delta 3 / System Reach 3 / Durability 2 = **8/9**。
- Evolution relation：`Direct Evolution`。
- Stable owner：`INFER-KV-CACHE`。
- Books disposition：`Integrate`。
<!-- review:SF-2026-ARXIV-2607-13205:end -->

<!-- review:SF-2026-ARXIV-2607-13285:start -->
#### Harness Handbook: Making Evolving Agent Harnesses Readable, Navigable, and Editable

<!-- claim:SF-2026-ARXIV-2607-13285:start -->The pipeline derives behavior-oriented handbooks from current code, connects high-level capability descriptions to candidate implementation locations and validates those locations against the repository before planning edits. 该结论只在论文公开的 workload 与 evaluation contract 内成立，不外推为通用生产结论。<!-- claim:SF-2026-ARXIV-2607-13285:end -->

**旧方案与约束变化。** `本章的核心判断是：**Workflow 是 Agent 的 durable control plane。它持久化状态和事件，强制 policy、budget、retry、approval 与 compensation；模型在被授权的节点内提出内容或分支，不拥有整个流程的事实状态。**`（`books/part-07-agent/81-workflow.md#L14-L14`）旧方案在状态局部、规模较小或 SLO 宽松时继续成立；本 family 面对的新增压力由其 v1 problem statement 和 method 明确限定。

**机制、状态与代价。** The pipeline derives behavior-oriented handbooks from current code, connects high-level capability descriptions to candidate implementation locations and validates those locations against the repository before planning edits. 它改变 `AGENT-WORKFLOW` 下的 state/data/control contract，同时引入 metadata、校准/选择误差、额外执行或恢复责任；这些代价必须和收益在同一 workload 内计量。

**Evaluation contract。** Method：`https://arxiv.org/html/2607.13285v1#S3`；Evaluation：`https://arxiv.org/html/2607.13285v1#S4`；Limitations/Counterevidence：`https://arxiv.org/html/2607.13285v1#S5`；本次 RP 重新绑定历史 full-read coverage：`papers/2026/weekly/2026-W29/README.md#L434-L446`，其中具名记录了 Method、Evaluation 与 Boundary。未披露字段保持 `Not Disclosed`；作者结果不跨模型、硬件、精度、长度、batch、concurrency、SLO 或 evaluator 外推。

- Score V2：Design Delta 3 / System Reach 2 / Durability 3 = **8/9**。
- Evolution relation：`Direct Evolution`。
- Stable owner：`AGENT-WORKFLOW`。
- Books disposition：`Integrate`。
<!-- review:SF-2026-ARXIV-2607-13285:end -->

## 4. Benchmark Contracts

以下只保存作者实验的适用合同，不把论文最大值外推为生产常数，也不跨模型、硬件或 workload 排名。

<!-- validator:benchmark-contract-v1 -->
| Source Family ID | Workload | Model | Hardware | Precision | Input Length | Output Length | Batch | Concurrency | SLO | Evaluator |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2607-12395 | Paper-defined evaluation contract: https://arxiv.org/html/2607.12395v1#S4 | Ring-2.5-1T-Zero and 104B Ring-2.5-flash-Zero; distillation into Qwen2.5-32B and Llama-3.3-70B-Instruct | 320 x NVIDIA H200 GPUs for all disclosed paper experiments; this does not establish other training topologies or serving behavior | mixed precision with explicit control; exact per-table precision must remain table-scoped | training truncation modes 4K/16K/64K | inference reasoning length reported per mode/benchmark | distributed training; serving concurrency not evaluated | distributed training; serving concurrency not evaluated | No production SLO | Does not establish general-domain RL scaling, causal emergence from parameter count alone, production serving efficiency or transfer beyond the disclosed models and math tasks |
| SF-2026-ARXIV-2607-12463 | Paper-defined evaluation contract: https://arxiv.org/html/2607.12463v1#S4 | Qwen2.5-Coder-Instruct 7B/14B and Qwen3-8B | NVIDIA H100 80GB; full reproduction GPU-hours reported in appendix | Not consistently disclosed across every evaluation table | 2.6B-token decontaminated corpus from 968 repositories | Task-dependent; not a serving latency study | Three independent seeds for main coding-agent results | Three independent seeds for main coding-agent results | None | Python-heavy, teacher-dependent evidence; no universal coding-agent improvement claim |
| SF-2026-ARXIV-2607-12550 | Paper-defined evaluation contract: https://arxiv.org/html/2607.12550v1#S4 | Mistral-7B-v0.3 and LLaMA-2-13B | NVIDIA A100 40GB for both disclosed model executions; a larger device is used only for the LLaMA RULER case that did not fit | Model execution in bfloat16 and decomposition in float32; fp16 is only the idealized serialization/byte-accounting convention | Long-context tests capped at 8192 tokens | Task-dependent | Single-GPU study; no production concurrency | Single-GPU study; no production concurrency | None | No fused deployable kernel, broader model/domain sweep, multi-needle regime or production latency proof |
| SF-2026-ARXIV-2607-12625 | Paper-defined evaluation contract: https://arxiv.org/html/2607.12625v1#S4 | Kimi-2.6, Qwen3.5-35B-A3B and 397B-A17B configurations | Host/device hardware not completely disclosed | Not disclosed | 117 MobileWorld GUI-only tasks from 201-task set; 50-step cap | Action traces; tokens separately reported where available | Sequential tasks; no concurrency | Sequential tasks; no concurrency | No production SLO | Benchmark/device/model-specific; not proof of open-world GUI reliability or safe self-modification |
| SF-2026-ARXIV-2607-12650 | Paper-defined evaluation contract: https://arxiv.org/html/2607.12650v1#S4 | claude-sonnet-4-6, claude-haiku-4-5-20251001, and claude-opus-4-7 at temperature 0 | Not Disclosed and not material to the offline proof-chain evaluation | Not Disclosed for hosted-model inference and Lean kernel checking | Tier 1 TableBench n=120; each counterfactual panel constructs 5 domains x 2 pair injections x 3 shapes = 30 claims, while the Table 4 headline reports n=20 binary/direction cells per panel; Tier 2 n=120 | Verified proof object or Abstain plus replay artifact; normalized token length Not Disclosed | Offline evaluation; one counterfactual repetition; no production concurrency | Offline evaluation; one counterfactual repetition; no production concurrency | No production latency or availability SLO | Proof is relative to the whitelist, axioms, source lifts, attestations, and formalization; Tier 1/1.5 bypass natural-language-to-Lean via a frozen goal; no proof of source truth, open-domain hallucination elimination, performance, latency, or production concurrency |
| SF-2026-ARXIV-2607-12747 | Paper-defined evaluation contract: https://arxiv.org/html/2607.12747v1#S4 | Qwen3.5-27B MCP-Atlas trajectories and GPT-4o Who&When trajectories | Not sufficiently disclosed for universal latency claims | Not disclosed | 203 public MCP-Atlas tasks; 88 behavior-caused failures after filtering | Step traces; prompt baselines report generated tokens | Offline evaluation | Offline evaluation | No production SLO | Localization benchmark evidence, not causal diagnosis or production incident-resolution proof |
| SF-2026-ARXIV-2607-12839 | Paper-defined evaluation contract: https://arxiv.org/html/2607.12839v1#S5 | Phi-3.5-3.8B, Llama-3-8B, Qwen2.5-14B, and Llama-3-70B | AMD Ryzen AI 7 350, Ryzen AI 9 HX 370, and Ryzen AI Max+ 395 | Primary path uses AWQ W4A16; the cross-framework HeteroMosaic comparison uses BF16 and is not apples-to-apples | Prompt/generation lengths vary by experiment | Decode throughput and TTFT measured | Dependency-preserving microbatches, not multi-tenant serving | Dependency-preserving microbatches, not multi-tenant serving | Interactive latency/energy objectives; no external production SLO | Vendor/platform/model-specific; maxima are not fleet-wide guarantees |
| SF-2026-ARXIV-2607-12875 | Paper-defined evaluation contract: https://arxiv.org/html/2607.12875v1#S4 | K100 main path Qwen3-8B, TP=4, greedy; Z200 Qwen3.6-27B, TP=4; A800 reference Qwen3-8B TP=4; Apple M5 Pro reference Qwen3-8B TP=1 | K100: 4 x K500SM_AI, 65,520 MiB per card; Z200: 4 x 16GB; A800 and Apple M5 Pro are reference cases, not main zero-reference evidence | BF16 on disclosed K100, Z200, A800, and Apple M5 Pro paths | K100 main 3x3 prompt lengths 11, 256, 1,021; supplement chunked prompt 1,021 and multi-batch prompt 256 | K100 main generation lengths 256, 1,024, 2,048; chunked and multi-batch supplement generation 256 | K100 matched CUDA Graph state versus vLLM, means plus/minus SD over 3 runs; Z200 batch 8 OOM; no production multi-tenant concurrency | K100 matched CUDA Graph state versus vLLM, means plus/minus SD over 3 runs; Z200 batch 8 OOM; no production multi-tenant concurrency | No production SLO | Zero-reference evidence is device/model/runtime specific and does not generalize to other accelerators, serving topologies, concurrency, or SLOs |
| SF-2026-ARXIV-2607-13124 | Paper-defined evaluation contract: https://arxiv.org/html/2607.13124v1#S4 | Qwen3-4B-Instruct-2507 with about 25% of parameters removed by pruning the lowest-BI layers | Single node with 8 NVIDIA H20 GPUs | Not uniform across all tables | 45,447 training prompts; maximum prompt length 4,096 tokens | Maximum response length 4,096 tokens with short-to-long rollout scheduling | Training batch 64 with rollout group 8; no serving concurrency evaluation | Training batch 64 with rollout group 8; no serving concurrency evaluation | None | Does not prove recovery for arbitrary sparsity, absent domains or production kernels |
| SF-2026-ARXIV-2607-13027 | Paper-defined evaluation contract: https://arxiv.org/html/2607.13027v1#S4 | DeepSeek-V4-Flash is the LLM backbone for all systems; MobileClaw additionally uses qwen3.7-plus for visual grounding | Xiaomi Redmi 2312DRAABC running Android 13 / SDK 33 for all disclosed mobile experiments; single-device evidence does not generalize across phones | Not applicable/not disclosed for hosted models | MobileTask 70 tasks and AssistantBench development subset 19 tasks | PalmClaw capped at 30 rounds; screen-based baselines capped at 100 rounds; token totals are reported separately | Single task; no concurrency | Single task; no concurrency | No production SLO | Relative results are task/device/tool-coverage specific, not general mobile-agent performance |
| SF-2026-ARXIV-2607-13157 | Paper-defined evaluation contract: https://arxiv.org/html/2607.13157v1#S7 | LongMemEval uses gpt-5.5 xhigh with nomic-embed-v1.5 and HNSW top-K=200; flat-history pairwise judge is gpt-5.4 | Database and hardware sizing Not Disclosed | Not Disclosed for hosted models; embedding precision Not Disclosed | LongMemEval 500 questions; pairwise run uses one 80-turn ChromAtlas-ND conversation; BEAM uses 100 conversations at 128K, 500K, 1M, and 10M tokens with 2,000 human-validated questions | Task-dependent answer length; Not Disclosed as a normalized token budget | Offline benchmark execution; production concurrency Not Evaluated | Offline benchmark execution; production concurrency Not Evaluated | No production latency or availability SLO | Prompt/model snapshots and run metadata are not fully enumerated; results do not establish production memory behavior or generalize beyond disclosed benchmarks |
| SF-2026-ARXIV-2607-13205 | Paper-defined evaluation contract: https://arxiv.org/html/2607.13205v1#S4 | Primary Llama-3.1-8B-Instruct; cross-model Mistral-7B-Instruct-v0.3, Phi-3-mini, and Qwen2.5-7B-Instruct; Llama-3.1-8B base diagnostic | Single NVIDIA A100 80GB for the disclosed experiments; mask harness does not materialize physical cache compaction | fp16 | Synthetic JSON, XML, markdown table and wiki-table corpora; cap policy tested at paper lengths | Exact-match leaf QA | No serving concurrency | No serving concurrency | None | No real tensor compaction, latency/memory saving, 4-bit KV, production RAG/log workload or per-step Quest equivalence |
| SF-2026-ARXIV-2607-13285 | Paper-defined evaluation contract: https://arxiv.org/html/2607.13285v1#S4 | Read-only planner DeepSeek-V4-Pro; judges GPT-5.5, Claude Opus 4.8, and DeepSeek-V4-Pro | Not disclosed/central to localization claims | Not applicable | Terminus-2 and Codex repositories with 30 curated modification requests each | Edit plans; planner token use measured | Offline planning | Offline planning | No production SLO | Does not prove patch correctness, arbitrary repository transfer or safe autonomous harness evolution |

## 5. Deep Analysis Selection

<!-- validator:deep-analysis-selection-v1 -->
| Source Family ID | Eligibility | Decision | Analysis Unit ID | Subsumed By | Priority Rationale | Narrative Ref |
| --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2607-12395 | score_7_9;potential_books_delta | selected | DA-20260715-01 | — | V2=8/9；The pipeline combines clipped importance sampling, training-engine numerator correction, KL control, mixed-precision safeguards and context-parallel communication optimization; staged self-distillation/RL and length-conditioned modes separate discovery, sharpening and adaptive inference depth.；相对同日候选提供独立 owner 的最大可定位 delta | analysis:DA-20260715-01 |
| SF-2026-ARXIV-2607-12463 | forced_review;potential_books_delta | not_selected | — | — | Deep Review is forced by a confirmed pretraining knowledge gap, but its Python-heavy function-reconstruction branch is narrower than the selected cross-system units. | analysis-decision:SF-2026-ARXIV-2607-12463 |
| SF-2026-ARXIV-2607-12747 | forced_review;potential_books_delta | not_selected | — | — | Deep Review is forced by a confirmed trace-diagnosis knowledge gap; long-form narrative remains with the selected workflow/state units because deviation localization does not establish causal root cause. | analysis-decision:SF-2026-ARXIV-2607-12747 |
| SF-2026-ARXIV-2607-12839 | score_7_9;potential_books_delta | not_selected | — | — | Full deep review remains required and complete, but its heterogeneity-first critical-path placement mechanism is narrower than the three selected cross-cutting deltas; selection affects narrative space only, not evidence depth or Books eligibility. | analysis-decision:SF-2026-ARXIV-2607-12839 |
| SF-2026-ARXIV-2607-13124 | forced_review;potential_books_delta | not_selected | — | — | Deep Review is forced by a confirmed post-pruning recovery gap, but the mechanism remains a bounded recovery curriculum rather than a broader objective/runtime change. | analysis-decision:SF-2026-ARXIV-2607-13124 |
| SF-2026-ARXIV-2607-13205 | score_7_9;potential_books_delta | selected | DA-20260715-02 | — | V2=8/9；The method labels structural roles, diagnoses attention allocation by role and applies adaptive role-aware correction before selection, retaining semantic leaves rather than structural scaffolding under tight budgets.；相对同日候选提供独立 owner 的最大可定位 delta | analysis:DA-20260715-02 |
| SF-2026-ARXIV-2607-13285 | score_7_9;potential_books_delta | selected | DA-20260715-03 | — | V2=8/9；The pipeline derives behavior-oriented handbooks from current code, connects high-level capability descriptions to candidate implementation locations and validates those locations against the repository before planning edits.；相对同日候选提供独立 owner 的最大可定位 delta | analysis:DA-20260715-03 |

<!-- analysis:DA-20260715-01:start -->
### Ring-Zero: Scaling Zero RL to a Trillion Parameters for Emergent Reasoning

**旧方案为何合理。** Small-model RLVR with fixed context and ordinary importance ratios is reasonable when engine mismatch and communication depth are small. At trillion-parameter scale, low-probability amplification magnifies floating-point disagreement and context parallelism becomes a critical-path bottleneck.（现有命题定位：`books/part-04-training-system/31-rlhf.md#L14-L14`）

**约束变化与机制。** The pipeline combines clipped importance sampling, training-engine numerator correction, KL control, mixed-precision safeguards and context-parallel communication optimization; staged self-distillation/RL and length-conditioned modes separate discovery, sharpening and adaptive inference depth. 这条证据与现有主线的关系是 `Direct Evolution`：它改变或补充 `TRAIN-RLHF` 下的 representation、state、data flow 或 control ownership，而不是用论文名称替换设计结论。

**收益、代价与下一重压力。** The design improves stability and sample efficiency but depends on costly large-scale infrastructure, math-verifiable rewards and proprietary 1T-model evidence. Joint length training produced negative transfer at the high mode, ultra-long high-quality data remained limiting, and 64K training context bounded the claim.

<!-- analysis:DA-20260715-01:end -->

<!-- analysis:DA-20260715-02:start -->
### Adaptive Filtering of the KV Cache: Diagnosing and Correcting Structural-Role Bias in LLM Inference

**旧方案为何合理。** H2O-style heavy hitters are reasonable on prose-like corpora where attention mass tracks future utility. Structured prompts concentrate attention by syntactic role and break that proxy.（现有命题定位：`books/part-05-inference-system/45-why-kv-cache-speeds-up.md#L14-L14`）

**约束变化与机制。** The method labels structural roles, diagnoses attention allocation by role and applies adaptive role-aware correction before selection, retaining semantic leaves rather than structural scaffolding under tight budgets. 这条证据与现有主线的关系是 `Direct Evolution`：它改变或补充 `INFER-KV-CACHE` 下的 representation、state、data flow 或 control ownership，而不是用论文名称替换设计结论。

**收益、代价与下一重压力。** Role-aware correction improves schema-dense leaf QA but has a role-density floor, seed-sensitive margins and format-specific labeling artifacts. The masking harness does not compact tensors, so it proves accuracy of keep patterns, not memory or latency gains.

<!-- analysis:DA-20260715-02:end -->

<!-- analysis:DA-20260715-03:start -->
### Harness Handbook: Making Evolving Agent Harnesses Readable, Navigable, and Editable

**旧方案为何合理。** Repository search and architecture docs suffice for stable modular systems. Fast-changing harnesses make documentation stale and behavioral ownership cross-module.（现有命题定位：`books/part-07-agent/81-workflow.md#L14-L14`）

**约束变化与机制。** The pipeline derives behavior-oriented handbooks from current code, connects high-level capability descriptions to candidate implementation locations and validates those locations against the repository before planning edits. 这条证据与现有主线的关系是 `Direct Evolution`：它改变或补充 `AGENT-WORKFLOW` 下的 representation、state、data flow 或 control ownership，而不是用论文名称替换设计结论。

**收益、代价与下一重压力。** Handbooks reduce planner tokens and improve localization but cost regeneration, can omit dynamic/runtime behavior and may become stale. Evidence spans only two production-style harnesses and selected modification requests.

<!-- analysis:DA-20260715-03:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-12463:start -->《Function-Aware Fill-in-the-Middle as Mid-Training for Coding Agent Foundation Models》已完成 Deep Source Review。Deep Review is forced by a confirmed pretraining knowledge gap, but its Python-heavy function-reconstruction branch is narrower than the selected cross-system units.<!-- analysis-decision:SF-2026-ARXIV-2607-12463:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-12747:start -->《Tracing Agentic Failure from the Flow of Success》已完成 Deep Source Review。Deep Review is forced by a confirmed trace-diagnosis knowledge gap; long-form narrative remains with the selected workflow/state units because deviation localization does not establish causal root cause.<!-- analysis-decision:SF-2026-ARXIV-2607-12747:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-12839:start -->《HeteroMosaic: Exposing and Exploiting Heterogeneous Execution Opportunities for Energy-Efficient Edge LLM Inference》已完成 Deep Source Review。Full deep review remains required and complete, but its heterogeneity-first critical-path placement mechanism is narrower than the three selected cross-cutting deltas; selection affects narrative space only, not evidence depth or Books eligibility.<!-- analysis-decision:SF-2026-ARXIV-2607-12839:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-13124:start -->《ShortOPD: Recovering Pruned LLMs with Short-to-Long On-Policy Distillation》已完成 Deep Source Review。Deep Review is forced by a confirmed post-pruning recovery gap, but the mechanism remains a bounded recovery curriculum rather than a broader objective/runtime change.<!-- analysis-decision:SF-2026-ARXIV-2607-13124:end -->

## 6. Books Comparison

<!-- validator:books-comparison-v1 -->
| Source Family ID | Stable Node ID | Target Chapter Ref | Adjacent Chapter Refs | Existing Proposition | New Evidence Delta | Evolution Relation | Decision | Books Review Ref |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2607-12395 | TRAIN-RLHF | books/part-04-training-system/31-rlhf.md#L1 | books/part-04-training-system/30-lora.md#L14-L14; books/part-04-training-system/32-ppo.md#L14-L14 | existing:SF-2026-ARXIV-2607-12395 | delta:SF-2026-ARXIV-2607-12395 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2607-12395 |
| SF-2026-ARXIV-2607-12463 | TRAIN-PRETRAINING | books/part-04-training-system/28-pretraining.md#L1 | books/part-04-training-system/27-data.md#L14-L14; books/part-04-training-system/29-sft.md#L14-L14 | existing:SF-2026-ARXIV-2607-12463 | delta:SF-2026-ARXIV-2607-12463 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2607-12463 |
| SF-2026-ARXIV-2607-12550 | INFER-KV-CACHE | books/part-05-inference-system/45-why-kv-cache-speeds-up.md#L14-L14 | books/part-05-inference-system/44-decode.md#L14-L14; books/part-05-inference-system/46-continuous-batching.md#L14-L14 | existing:SF-2026-ARXIV-2607-12550 | delta:SF-2026-ARXIV-2607-12550 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2607-12550 |
| SF-2026-ARXIV-2607-12625 | AGENT-MEMORY | books/part-07-agent/77-memory.md#L14-L14 | books/part-07-agent/76-rag.md#L14-L14; books/part-07-agent/78-tool-calling.md#L14-L14 | existing:SF-2026-ARXIV-2607-12625 | delta:SF-2026-ARXIV-2607-12625 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2607-12625 |
| SF-2026-ARXIV-2607-12650 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#L14-L14 | books/part-06-ai-infrastructure/65-kai-scheduler.md#L14-L14; books/part-06-ai-infrastructure/67-monitoring.md#L14-L14 | existing:SF-2026-ARXIV-2607-12650 | delta:SF-2026-ARXIV-2607-12650 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2607-12650 |
| SF-2026-ARXIV-2607-12747 | PLATFORM-TRACE | books/part-06-ai-infrastructure/69-trace.md#L1 | books/part-06-ai-infrastructure/68-logging.md#L14-L14; books/part-06-ai-infrastructure/70-cost.md#L14-L14 | existing:SF-2026-ARXIV-2607-12747 | delta:SF-2026-ARXIV-2607-12747 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2607-12747 |
| SF-2026-ARXIV-2607-12839 | INFER-TENSORRT-LLM | books/part-05-inference-system/49-tensorrt-llm.md#L1 | books/part-05-inference-system/48-speculative-decoding.md#L16-L16; books/part-05-inference-system/50-vllm.md#L14-L14 | existing:SF-2026-ARXIV-2607-12839 | delta:SF-2026-ARXIV-2607-12839 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2607-12839 |
| SF-2026-ARXIV-2607-12875 | INFER-TENSORRT-LLM | books/part-05-inference-system/49-tensorrt-llm.md#L14-L14 | books/part-05-inference-system/48-speculative-decoding.md#L16-L16; books/part-05-inference-system/50-vllm.md#L14-L14 | existing:SF-2026-ARXIV-2607-12875 | delta:SF-2026-ARXIV-2607-12875 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2607-12875 |
| SF-2026-ARXIV-2607-13124 | TRAIN-GRPO | books/part-04-training-system/33-grpo.md#L1 | books/part-04-training-system/32-ppo.md#L14-L14; books/part-04-training-system/34-dpo.md#L14-L14 | existing:SF-2026-ARXIV-2607-13124 | delta:SF-2026-ARXIV-2607-13124 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2607-13124 |
| SF-2026-ARXIV-2607-13027 | AGENT-PLATFORM | books/part-07-agent/84-agent-platform.md#L14-L14 | books/part-07-agent/83-mcp.md#L14-L14 | existing:SF-2026-ARXIV-2607-13027 | delta:SF-2026-ARXIV-2607-13027 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2607-13027 |
| SF-2026-ARXIV-2607-13157 | AGENT-MEMORY | books/part-07-agent/77-memory.md#L14-L14 | books/part-07-agent/76-rag.md#L14-L14; books/part-07-agent/78-tool-calling.md#L14-L14 | existing:SF-2026-ARXIV-2607-13157 | delta:SF-2026-ARXIV-2607-13157 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2607-13157 |
| SF-2026-ARXIV-2607-13205 | INFER-KV-CACHE | books/part-05-inference-system/45-why-kv-cache-speeds-up.md#L1 | books/part-05-inference-system/44-decode.md#L14-L14; books/part-05-inference-system/46-continuous-batching.md#L14-L14 | existing:SF-2026-ARXIV-2607-13205 | delta:SF-2026-ARXIV-2607-13205 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2607-13205 |
| SF-2026-ARXIV-2607-13285 | AGENT-WORKFLOW | books/part-07-agent/81-workflow.md#L1 | books/part-07-agent/80-reflection.md#L14-L14; books/part-07-agent/82-multi-agent.md#L14-L14 | existing:SF-2026-ARXIV-2607-13285 | delta:SF-2026-ARXIV-2607-13285 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2607-13285 |

<!-- books-review:SF-2026-ARXIV-2607-12395:start --><!-- existing:SF-2026-ARXIV-2607-12395:start -->对读 `books/part-04-training-system/31-rlhf.md#L1` 与相邻章节后，现有命题（`books/part-04-training-system/31-rlhf.md#L14-L14`）为：本章的核心判断是：**RLHF 将人类对候选输出的相对判断拟合成 reward signal，再在不偏离参考策略过远的约束下提高期望 reward。**它把难以形式化的行为目标转成可优化代理，也把标注偏差、reward hacking 和在线 rollout 成本带进训练系统。<!-- existing:SF-2026-ARXIV-2607-12395:end --><!-- delta:SF-2026-ARXIV-2607-12395:start -->新增证据边界：The pipeline combines clipped importance sampling, training-engine numerator correction, KL control, mixed-precision safeguards and context-parallel communication optimization; staged self-distillation/RL and length-conditioned modes separate discovery, sharpening and adaptive inference depth. 该 delta 已进入 `books/part-04-training-system/31-rlhf.md#L1`，正文保留旧方案成立条件、约束变化、代价与下一重压力。<!-- delta:SF-2026-ARXIV-2607-12395:end --><!-- books-review:SF-2026-ARXIV-2607-12395:end -->

<!-- books-review:SF-2026-ARXIV-2607-12463:start --><!-- existing:SF-2026-ARXIV-2607-12463:start -->对读 `books/part-04-training-system/28-pretraining.md#L1` 与相邻章节后，现有命题（`books/part-04-training-system/28-pretraining.md#L14-L14`）为：本章的核心判断是：**Pretraining 是在大规模数据分布上反复最小化 next-token negative log-likelihood，使参数逐步形成可复用表示与条件生成能力。**它提供通用能力底座，但 loss 下降不自动保证事实可靠、指令遵循或部署分布上的任务成功。<!-- existing:SF-2026-ARXIV-2607-12463:end --><!-- delta:SF-2026-ARXIV-2607-12463:start -->新增证据边界：Program-dependency analysis selects function targets under complexity/inferability criteria; the model reconstructs the missing function with generated rationale before existing agentic post-training. 该 delta 已进入 `books/part-04-training-system/28-pretraining.md#L1`，正文保留旧方案成立条件、约束变化、代价与下一重压力。<!-- delta:SF-2026-ARXIV-2607-12463:end --><!-- books-review:SF-2026-ARXIV-2607-12463:end -->

<!-- books-review:SF-2026-ARXIV-2607-12550:start --><!-- existing:SF-2026-ARXIV-2607-12550:start -->对读 `books/part-05-inference-system/45-why-kv-cache-speeds-up.md#L14-L14` 与相邻章节后，现有命题（`books/part-05-inference-system/45-why-kv-cache-speeds-up.md#L14-L14`）为：本章的核心判断是：**KV Cache 利用 causal decoding 中历史 K/V 不再变化的性质，以随序列增长的 memory state 换取历史 layer computation 不重算；它加速 Decode，也把请求从无状态输入变成必须管理生命周期和 ownership 的系统对象。**<!-- existing:SF-2026-ARXIV-2607-12550:end --><!-- delta:SF-2026-ARXIV-2607-12550:start -->新增证据边界：Partial Tucker compression preserves head/layer axes, compresses token/feature axes and encodes truncation residual through a JL rotation plus low bits; one Lagrangian dual jointly allocates ranks and residual widths under a byte cap. 该证据未改变现有长期命题；保留为受限 workload 的 supporting evidence，不在正文重复追加论文段落。<!-- delta:SF-2026-ARXIV-2607-12550:end --><!-- books-review:SF-2026-ARXIV-2607-12550:end -->

<!-- books-review:SF-2026-ARXIV-2607-12625:start --><!-- existing:SF-2026-ARXIV-2607-12625:start -->对读 `books/part-07-agent/77-memory.md#L14-L14` 与相邻章节后，现有命题（`books/part-07-agent/77-memory.md#L14-L14`）为：本章的核心判断是：**Memory 是跨模型调用保存并重新选择状态的机制，由 storage、write policy、retrieval policy、consolidation、forgetting 和 authorization 共同构成；它不是模型意识，也不是无限 Context。**<!-- existing:SF-2026-ARXIV-2607-12625:end --><!-- delta:SF-2026-ARXIV-2607-12625:start -->新增证据边界：Know–Route–Act–Reflect separates host orchestration from GUI execution, maintains attribution-aware memory and state-validated skills, and transfers typed blackboard data between applications. 该证据未改变现有长期命题；保留为受限 workload 的 supporting evidence，不在正文重复追加论文段落。<!-- delta:SF-2026-ARXIV-2607-12625:end --><!-- books-review:SF-2026-ARXIV-2607-12625:end -->

<!-- books-review:SF-2026-ARXIV-2607-12650:start --><!-- existing:SF-2026-ARXIV-2607-12650:start -->对读 `books/part-06-ai-infrastructure/66-evaluation-system.md#L14-L14` 与相邻章节后，现有命题（`books/part-06-ai-infrastructure/66-evaluation-system.md#L14-L14`）为：本章的核心判断是：**Evaluation System 是把目标转化为可重复证据和受控决策的系统。它必须同时版本化被评估对象、输入分布、执行环境与 scorer，并显式表达不确定性、切片和风险；工具可以保存证据，但不能替组织定义什么算成功。**<!-- existing:SF-2026-ARXIV-2607-12650:end --><!-- delta:SF-2026-ARXIV-2607-12650:start -->新增证据边界：Typed tool-attested leaves and curator-owned source lifts/axioms feed a proof object; only mkVerified constructs Verified, the Lean kernel checks the derivation, and failure yields Abstain plus a replay artifact. 该证据未改变现有长期命题；保留为受限 workload 的 supporting evidence，不在正文重复追加论文段落。<!-- delta:SF-2026-ARXIV-2607-12650:end --><!-- books-review:SF-2026-ARXIV-2607-12650:end -->

<!-- books-review:SF-2026-ARXIV-2607-12747:start --><!-- existing:SF-2026-ARXIV-2607-12747:start -->对读 `books/part-06-ai-infrastructure/69-trace.md#L1` 与相邻章节后，现有命题（`books/part-06-ai-infrastructure/69-trace.md#L14-L14`）为：本章的核心判断是：**Trace 通过传播 context，将一次分布式操作拆成有父子或 link 关系的 spans，从而重建 critical path；其价值取决于边界、语义和采样是否保留真正决策点。**<!-- existing:SF-2026-ARXIV-2607-12747:end --><!-- delta:SF-2026-ARXIV-2607-12747:start -->新增证据边界：A latent continuous-time trajectory model learns normal flow from successful traces; deviations on failed traces yield step attribution, with conformal detection controlling thresholds. 该 delta 已进入 `books/part-06-ai-infrastructure/69-trace.md#L1`，正文保留旧方案成立条件、约束变化、代价与下一重压力。<!-- delta:SF-2026-ARXIV-2607-12747:end --><!-- books-review:SF-2026-ARXIV-2607-12747:end -->

<!-- books-review:SF-2026-ARXIV-2607-12839:start --><!-- existing:SF-2026-ARXIV-2607-12839:start -->对读 `books/part-05-inference-system/49-tensorrt-llm.md#L1` 与相邻章节后，现有命题（`books/part-05-inference-system/49-tensorrt-llm.md#L14-L14`）为：本章的核心判断是：**TensorRT-LLM 的核心不是改变模型语义，而是把经过验证的模型资产转换为面向 NVIDIA GPU 的执行计划，并用专用 kernels、quantization、KV management 与 runtime scheduling 交付它。**<!-- existing:SF-2026-ARXIV-2607-12839:end --><!-- delta:SF-2026-ARXIV-2607-12839:start -->新增证据边界：A heterogeneous roofline predicts opportunity; dependency-preserving microbatches expose overlap; trace-guided latency shaping jointly tunes assignment and schedule, with NPU-aware queues and custom GPU kernels. 该 delta 已进入 `books/part-05-inference-system/49-tensorrt-llm.md#L1`，正文保留旧方案成立条件、约束变化、代价与下一重压力。<!-- delta:SF-2026-ARXIV-2607-12839:end --><!-- books-review:SF-2026-ARXIV-2607-12839:end -->

<!-- books-review:SF-2026-ARXIV-2607-12875:start --><!-- existing:SF-2026-ARXIV-2607-12875:start -->对读 `books/part-05-inference-system/49-tensorrt-llm.md#L14-L14` 与相邻章节后，现有命题（`books/part-05-inference-system/49-tensorrt-llm.md#L14-L14`）为：本章的核心判断是：**TensorRT-LLM 的核心不是改变模型语义，而是把经过验证的模型资产转换为面向 NVIDIA GPU 的执行计划，并用专用 kernels、quantization、KV management 与 runtime scheduling 交付它。**<!-- existing:SF-2026-ARXIV-2607-12875:end --><!-- delta:SF-2026-ARXIV-2607-12875:start -->新增证据边界：A contract knowledge base describes interfaces, shapes, state transitions and platform constraints; isolated implementation/review/verification agents synthesize and test a single-path engine, while controlled exploration consolidates successful new knowledge. 该证据未改变现有长期命题；保留为受限 workload 的 supporting evidence，不在正文重复追加论文段落。<!-- delta:SF-2026-ARXIV-2607-12875:end --><!-- books-review:SF-2026-ARXIV-2607-12875:end -->

<!-- books-review:SF-2026-ARXIV-2607-13124:start --><!-- existing:SF-2026-ARXIV-2607-13124:start -->对读 `books/part-04-training-system/33-grpo.md#L1` 与相邻章节后，现有命题（`books/part-04-training-system/33-grpo.md#L14-L14`）为：本章的核心判断是：**GRPO 用同一 prompt 下多个 sampled responses 的组内 reward 统计构造相对 advantage，移除独立 learned critic，同时保留 policy ratio、clipping 与 reference regularization 的受限更新主线。**它减少 value-model 状态，不消除 rollout 成本、reward design 或 policy optimization 风险。<!-- existing:SF-2026-ARXIV-2607-13124:end --><!-- delta:SF-2026-ARXIV-2607-13124:start -->新增证据边界：On-policy distillation evaluates a frozen pre-pruning teacher on student samples; repetition/truncation feedback and two EMAs shrink early horizons then restore long generation as recovery improves. 该 delta 已进入 `books/part-04-training-system/33-grpo.md#L1`，正文保留旧方案成立条件、约束变化、代价与下一重压力。<!-- delta:SF-2026-ARXIV-2607-13124:end --><!-- books-review:SF-2026-ARXIV-2607-13124:end -->

<!-- books-review:SF-2026-ARXIV-2607-13027:start --><!-- existing:SF-2026-ARXIV-2607-13027:start -->对读 `books/part-07-agent/84-agent-platform.md#L14-L14` 与相邻章节后，现有命题（`books/part-07-agent/84-agent-platform.md#L14-L14`）为：本章的核心判断是：**Agent Platform 是 AI Platform 对有状态行动循环的扩展。它统一 Agent definition、run、context、memory、tools、workflow、evaluation 与 policy，但复用 Part VI 的 identity、resource、evidence、cost、tenancy、security 和 recovery substrate。**<!-- existing:SF-2026-ARXIV-2607-13027:end --><!-- delta:SF-2026-ARXIV-2607-13027:start -->新增证据边界：An on-device framework owns session loop, tools with typed arguments/results, shared/per-session memory and explicit execution boundaries; GUI remains a fallback branch. 该证据未改变现有长期命题；保留为受限 workload 的 supporting evidence，不在正文重复追加论文段落。<!-- delta:SF-2026-ARXIV-2607-13027:end --><!-- books-review:SF-2026-ARXIV-2607-13027:end -->

<!-- books-review:SF-2026-ARXIV-2607-13157:start --><!-- existing:SF-2026-ARXIV-2607-13157:start -->对读 `books/part-07-agent/77-memory.md#L14-L14` 与相邻章节后，现有命题（`books/part-07-agent/77-memory.md#L14-L14`）为：本章的核心判断是：**Memory 是跨模型调用保存并重新选择状态的机制，由 storage、write policy、retrieval policy、consolidation、forgetting 和 authorization 共同构成；它不是模型意识，也不是无限 Context。**<!-- existing:SF-2026-ARXIV-2607-13157:end --><!-- delta:SF-2026-ARXIV-2607-13157:start -->新增证据边界：A database-native lifecycle separates active context construction from passive scoped storage; it measures evidence retrieval, evidence use, task outcome and operational efficiency, with stable prefix/volatile suffix placement for cache compatibility. 该证据未改变现有长期命题；保留为受限 workload 的 supporting evidence，不在正文重复追加论文段落。<!-- delta:SF-2026-ARXIV-2607-13157:end --><!-- books-review:SF-2026-ARXIV-2607-13157:end -->

<!-- books-review:SF-2026-ARXIV-2607-13205:start --><!-- existing:SF-2026-ARXIV-2607-13205:start -->对读 `books/part-05-inference-system/45-why-kv-cache-speeds-up.md#L1` 与相邻章节后，现有命题（`books/part-05-inference-system/45-why-kv-cache-speeds-up.md#L14-L14`）为：本章的核心判断是：**KV Cache 利用 causal decoding 中历史 K/V 不再变化的性质，以随序列增长的 memory state 换取历史 layer computation 不重算；它加速 Decode，也把请求从无状态输入变成必须管理生命周期和 ownership 的系统对象。**<!-- existing:SF-2026-ARXIV-2607-13205:end --><!-- delta:SF-2026-ARXIV-2607-13205:start -->新增证据边界：The method labels structural roles, diagnoses attention allocation by role and applies adaptive role-aware correction before selection, retaining semantic leaves rather than structural scaffolding under tight budgets. 该 delta 已进入 `books/part-05-inference-system/45-why-kv-cache-speeds-up.md#L1`，正文保留旧方案成立条件、约束变化、代价与下一重压力。<!-- delta:SF-2026-ARXIV-2607-13205:end --><!-- books-review:SF-2026-ARXIV-2607-13205:end -->

<!-- books-review:SF-2026-ARXIV-2607-13285:start --><!-- existing:SF-2026-ARXIV-2607-13285:start -->对读 `books/part-07-agent/81-workflow.md#L1` 与相邻章节后，现有命题（`books/part-07-agent/81-workflow.md#L14-L14`）为：本章的核心判断是：**Workflow 是 Agent 的 durable control plane。它持久化状态和事件，强制 policy、budget、retry、approval 与 compensation；模型在被授权的节点内提出内容或分支，不拥有整个流程的事实状态。**<!-- existing:SF-2026-ARXIV-2607-13285:end --><!-- delta:SF-2026-ARXIV-2607-13285:start -->新增证据边界：The pipeline derives behavior-oriented handbooks from current code, connects high-level capability descriptions to candidate implementation locations and validates those locations against the repository before planning edits. 该 delta 已进入 `books/part-07-agent/81-workflow.md#L1`，正文保留旧方案成立条件、约束变化、代价与下一重压力。<!-- delta:SF-2026-ARXIV-2607-13285:end --><!-- books-review:SF-2026-ARXIV-2607-13285:end -->

## 7. Semantic Audit

<!-- validator:semantic-audit-v1 -->
| Audit ID | Auditor | Scope | Reviewed Refs | Findings | Resolution | Status |
| --- | --- | --- | --- | --- | --- | --- |
| SA-20260715-COVERAGE | fresh-context:final_contract_review | coverage | coverage:SRC-ARXIV:20260715; semantic-review:SA-20260715-COVERAGE | — | Verified — every frozen candidate has a final evidence route, Books disposition and resolved semantic audit | passed |
| SA-20260715-EVIDENCE | fresh-context:final_contract_review | evidence | review:SF-2026-ARXIV-2607-12273; review:SF-2026-ARXIV-2607-12287; review:SF-2026-ARXIV-2607-12356; review:SF-2026-ARXIV-2607-14145; review:SF-2026-ARXIV-2607-12395; review:SF-2026-ARXIV-2607-12463; review:SF-2026-ARXIV-2607-12550; review:SF-2026-ARXIV-2607-12571; review:SF-2026-ARXIV-2607-12625; review:SF-2026-ARXIV-2607-12650; review:SF-2026-ARXIV-2607-12747; review:SF-2026-ARXIV-2607-12839; review:SF-2026-ARXIV-2607-12875; review:SF-2026-ARXIV-2607-12886; review:SF-2026-ARXIV-2607-12931; review:SF-2026-ARXIV-2607-13124; review:SF-2026-ARXIV-2607-13027; review:SF-2026-ARXIV-2607-13157; review:SF-2026-ARXIV-2607-13179; review:SF-2026-ARXIV-2607-13205; review:SF-2026-ARXIV-2607-13285; semantic-review:SA-20260715-EVIDENCE | — | Verified — every frozen candidate has a final evidence route, Books disposition and resolved semantic audit | passed |
| SA-20260715-SELECTION | fresh-context:final_contract_review | deep_analysis_selection | analysis:DA-20260715-01; analysis:DA-20260715-02; analysis:DA-20260715-03; semantic-review:SA-20260715-SELECTION | — | Verified — every frozen candidate has a final evidence route, Books disposition and resolved semantic audit | passed |
| SA-20260715-BOOKS | fresh-context:final_contract_review | books | books-review:SF-2026-ARXIV-2607-12395; books-review:SF-2026-ARXIV-2607-12463; books-review:SF-2026-ARXIV-2607-12550; books-review:SF-2026-ARXIV-2607-12625; books-review:SF-2026-ARXIV-2607-12650; books-review:SF-2026-ARXIV-2607-12747; books-review:SF-2026-ARXIV-2607-12839; books-review:SF-2026-ARXIV-2607-12875; books-review:SF-2026-ARXIV-2607-13124; books-review:SF-2026-ARXIV-2607-13027; books-review:SF-2026-ARXIV-2607-13157; books-review:SF-2026-ARXIV-2607-13205; books-review:SF-2026-ARXIV-2607-13285; semantic-review:SA-20260715-BOOKS | — | Verified — every frozen candidate has a final evidence route, Books disposition and resolved semantic audit | passed |

<!-- semantic-review:SA-20260715-COVERAGE:start -->Fresh-context review reconciled the exact window, partition totals, date bucket and denominator.<!-- semantic-review:SA-20260715-COVERAGE:end -->
<!-- semantic-review:SA-20260715-EVIDENCE:start -->Fresh-context review reconciled all 21 frozen families: 7 Deep, 6 Standard and 8 Closure; 0 pending and 0 blocked rows remain explicitly outside mechanism claims.<!-- semantic-review:SA-20260715-EVIDENCE:end -->
<!-- semantic-review:SA-20260715-SELECTION:start -->Fresh-context review reconciled 7 eligible Deep families: 3 selected and 4 not selected; the narrative limit does not downgrade any completed Source Review.<!-- semantic-review:SA-20260715-SELECTION:end -->
<!-- semantic-review:SA-20260715-BOOKS:start -->Fresh-context review checked current owner and adjacent chapter handoffs; 7 个 family 已定位到实际 Books 段落，6 个 family 的 No Change 结论可定位，0 个 Weekly Only disposition 已由逐 family Source Review 确认为不进入 Books。<!-- semantic-review:SA-20260715-BOOKS:end -->

## 8. Ignored Noise

1111 个窗口内 identity 中，1090 个未进入候选分母：它们属于垂直应用、单数据集质量增量、没有状态/控制权变化的模型使用案例，或不在合同 category route。该数字是 route closure，不是声称逐篇全文审阅。

## 9. Recommended Action

1. Sunday Weekly 聚合本日报 family 与 RP，不按发现日重复计分。
2. 只有重要 revision、artifact、反证或 owner 冲突才重开本日报。
3. Books Decision：7 个 `Integrate`，6 个 `No Change — Existing Coverage`，0 个 `Weekly Only — Context`，8 个 `Rejected — Low Durability / Out of Scope`；Deep 7 / Standard 6。

## 10. Repository Changes

- 新建或更新 `papers/2026/07/15/README.md`。
- 本日报长期 delta 已同步至：`books/part-04-training-system/28-pretraining.md`、`books/part-04-training-system/31-rlhf.md`、`books/part-04-training-system/33-grpo.md`、`books/part-05-inference-system/45-why-kv-cache-speeds-up.md`、`books/part-05-inference-system/49-tensorrt-llm.md`、`books/part-06-ai-infrastructure/69-trace.md`、`books/part-07-agent/81-workflow.md`。

## 11. Open Questions

- 后续 revision 是否新增 artifact、独立复现或 failure evidence，从而改变当前 claim boundary？
- Sunday Weekly 的跨日演进链是否需要合并本日报多个同类 family？

## 12. Sources

- [Code-MUE: Measuring Code LLMs' Uncertainty through Execution-based Semantic Interaction Graphs](https://arxiv.org/abs/2607.12273v1) — first-public（Asia/Shanghai）：2026-07-14；accessed：2026-08-26
- [Reducing Temporal Redundancy for Efficient Vision-Language-Action Inference](https://arxiv.org/abs/2607.12287v1) — first-public（Asia/Shanghai）：2026-07-14；accessed：2026-08-26
- [VistaVLA: Geometry- and Semantic-Aware 3D Gaussian-Grounded VLA for Robotic Manipulation](https://arxiv.org/abs/2607.12356v1) — first-public（Asia/Shanghai）：2026-07-14；accessed：2026-08-26
- [ToolAnchor: Anchoring Counterfactual Context to Boost Agentic Tool-use Capability](https://arxiv.org/abs/2607.14145v1) — first-public（Asia/Shanghai）：2026-07-14；accessed：2026-08-26
- [Ring-Zero: Scaling Zero RL to a Trillion Parameters for Emergent Reasoning](https://arxiv.org/abs/2607.12395v1) — first-public（Asia/Shanghai）：2026-07-14；accessed：2026-08-27
- [Function-Aware Fill-in-the-Middle as Mid-Training for Coding Agent Foundation Models](https://arxiv.org/abs/2607.12463v1) — first-public（Asia/Shanghai）：2026-07-14；accessed：2026-08-27
- [A JoLT for the KV cache: Near-lossless KV cache compression via joint Lagrangian allocation of Tucker ranks and a rotated residual for LLMs](https://arxiv.org/abs/2607.12550v1) — first-public（Asia/Shanghai）：2026-07-14；accessed：2026-08-27
- [TrustVLA: Mechanism-Guided Inference-Time Defense Against Vision-Language-Action Backdoors](https://arxiv.org/abs/2607.12571v1) — first-public（Asia/Shanghai）：2026-07-14；accessed：2026-08-26
- [KnowAct-GUIClaw: Know Deeply, Act Perfectly, Personal GUI Assistant with Self-Evolving Memory and Skill](https://arxiv.org/abs/2607.12625v1) — first-public（Asia/Shanghai）：2026-07-14；accessed：2026-08-27
- [Evidence-Grounded Verified Agentic Reasoning: A Path Toward Eliminating LLM Hallucination in Empirical Inference via Tool-Attested Kernel Proofs](https://arxiv.org/abs/2607.12650v1) — first-public（Asia/Shanghai）：2026-07-14；accessed：2026-08-27
- [Tracing Agentic Failure from the Flow of Success](https://arxiv.org/abs/2607.12747v1) — first-public（Asia/Shanghai）：2026-07-14；accessed：2026-08-27
- [HeteroMosaic: Exposing and Exploiting Heterogeneous Execution Opportunities for Energy-Efficient Edge LLM Inference](https://arxiv.org/abs/2607.12839v1) — first-public（Asia/Shanghai）：2026-07-14；accessed：2026-08-27
- [MetaInfer: A Knowledge Only LLM Inference Engine Generator SKILL Toolbox](https://arxiv.org/abs/2607.12875v1) — first-public（Asia/Shanghai）：2026-07-14；accessed：2026-08-27
- [A Multi-Agent System for Autonomous, Fine-Tuning-Free Clinical Symptom Detection: Development and Validation Study](https://arxiv.org/abs/2607.12886v1) — first-public（Asia/Shanghai）：2026-07-14；accessed：2026-08-26
- [ExToken: Structured Exploration for Efficient Vision-Language-Action Reinforcement Fine-tuning](https://arxiv.org/abs/2607.12931v1) — first-public（Asia/Shanghai）：2026-07-15；accessed：2026-08-26
- [ShortOPD: Recovering Pruned LLMs with Short-to-Long On-Policy Distillation](https://arxiv.org/abs/2607.13124v1) — first-public（Asia/Shanghai）：2026-07-15；accessed：2026-08-27
- [PalmClaw: A Native On-Device Agent Framework for Mobile Phones](https://arxiv.org/abs/2607.13027v1) — first-public（Asia/Shanghai）：2026-07-15；accessed：2026-08-27
- [Oracle Agent Memory as an Enterprise Memory Substrate for Long-Horizon AI Agents](https://arxiv.org/abs/2607.13157v1) — first-public（Asia/Shanghai）：2026-07-15；accessed：2026-08-27
- [SoftBoard: A Multi-Agent Tool for the Creation and Evaluation of Low-Fidelity Prototypes](https://arxiv.org/abs/2607.13179v1) — first-public（Asia/Shanghai）：2026-07-15；accessed：2026-08-26
- [Adaptive Filtering of the KV Cache: Diagnosing and Correcting Structural-Role Bias in LLM Inference](https://arxiv.org/abs/2607.13205v1) — first-public（Asia/Shanghai）：2026-07-15；accessed：2026-08-27
- [Harness Handbook: Making Evolving Agent Harnesses Readable, Navigable, and Editable](https://arxiv.org/abs/2607.13285v1) — first-public（Asia/Shanghai）：2026-07-15；accessed：2026-08-27
- [July recovery snapshot](../_sources/datacite-arxiv-recovery-20260701-26/README.md) — accessed：2026-08-26
- [Research Sources Registry](../../../../docs/RESEARCH_SOURCES.md) — registry version 2026-08-25

## 13. Final Status

Daily V2.1 的 Coverage、Evidence、Deep Analysis Selection 与 Books Decision 均已完成；fresh-context Semantic Audit 无未解决 finding，三个 Gate 均已闭合。
