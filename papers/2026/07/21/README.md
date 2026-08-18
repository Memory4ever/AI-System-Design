# Daily Research — 2026-07-21

**Research Date:** 2026-07-21

**Timezone:** Asia/Shanghai

**Strict Window:** 2026-07-20 09:00:00 ～ 2026-07-21 09:00:00（北京时间，左闭右开）

**Contract:** V2.1 Full Replay；SRC-DATACITE 是 SRC-ARXIV 的注册恢复 fallback，只作 identity/date metadata；技术 claim 回到精确 arXiv v1 或可追溯历史全文审阅

**Status:** Complete；Coverage、Evidence、Books 与 fresh-context Semantic Audit 均无未解决 finding

## Executive Summary

本窗口枚举到 1083 个唯一 arXiv v1 identity；按合同 category 与 AI-System title route 去重后，候选分母冻结为 19 个。当前路由账目为 17 个 Deep、2 个 Standard、0 个 Closure；route 只是审阅义务，不等于 Review 已完成。

本轮没有把 DataCite metadata 或旧 Weekly prose 冒充 primary manuscript。旧 Weekly 只提供 identity、owner 与恢复线索；缺少事件时 evidence version、route locator、claim boundary、RP 和 Prior Review Ref 的 family 一律保持 pending/blocked。只有具备精确 primary receipt 的 family 才能完成评分、Selection 与 Books Decision。

## 1. Coverage

<!-- validator:report-metadata-v2 -->
| Field | Value |
| --- | --- |
| Contract Version | V2.1 |
| Score Schema | V2 |
| Report Type | Daily |
| Window Start | 2026-07-21 |
| Window End | 2026-07-21 |
| Registry Version | 2026-08-25 |
| Coverage Mode | Full Replay |
| Baseline Report | — |
| Changed Source IDs | — |
| Previous Denominator ID | — |
| Denominator ID | daily-2026-07-21-0900-v2.1-july-replay-01 |
| Denominator Frozen At | 2026-08-26T18:00:00+08:00 |
| Completion Status | Complete |
| Coverage Gate | Closed |
| Evidence Gate | Passed |
| Books Gate | Passed |

### Source Coverage Receipt

<!-- validator:source-coverage-v2 -->
| Source ID | Window Start | Window End | Executed At | Endpoint / Filter | Result | Hits | Candidate Source Families | Pagination / Cursor | Window Watermark | Closure Evidence | Gap / Limitation ID |
| --- | --- | --- | --- | --- | --- | ---: | --- | --- | --- | --- | --- |
| SRC-ARXIV | 2026-07-20T09:00:00+08:00 | 2026-07-21T09:00:00+08:00 | 2026-08-26T18:00:00+08:00 | registered SRC-DATACITE fallback; arXiv DOI identity + subjects + v1 Submitted timestamp; exact 09:00 bucket | checked | 1083 | SF-2026-ARXIV-2607-17525<br>SF-2026-ARXIV-2607-17545<br>SF-2026-ARXIV-2607-17621<br>SF-2026-ARXIV-2607-17715<br>SF-2026-ARXIV-2607-17733<br>SF-2026-ARXIV-2607-17747<br>SF-2026-ARXIV-2607-17751<br>SF-2026-ARXIV-2607-17786<br>SF-2026-ARXIV-2607-17914<br>SF-2026-ARXIV-2607-17973<br>SF-2026-ARXIV-2607-17979<br>SF-2026-ARXIV-2607-17986<br>SF-2026-ARXIV-2607-18016<br>SF-2026-ARXIV-2607-18110<br>SF-2026-ARXIV-2607-18141<br>SF-2026-ARXIV-2607-18171<br>SF-2026-ARXIV-2607-18213<br>SF-2026-ARXIV-2607-18231<br>SF-2026-ARXIV-2607-18603 | five disjoint DOI-prefix groups; page size=1000; every group reached total; identifiers unique | 2026-07-21T09:00:00+08:00 | coverage:SRC-ARXIV:20260721 | GAP-ARXIV-DIRECT-RESET-20260721 |

<!-- coverage:SRC-ARXIV:20260721:start -->Direct arXiv API/OAI reset connections; registered DataCite fallback froze the strict-window denominator. Canonical source: papers/2026/07/_sources/datacite-arxiv-recovery-20260701-26/datacite-candidate-inventory.json; sha256:d9c5e832203e6c3940bbf234cbbb0fff9e69bcdf1964db69b901cd19b8de6e29; 1083 unique identities in this strict window; 19 routed families.<!-- coverage:SRC-ARXIV:20260721:end -->

### Coverage Limitations

- DataCite 是 Discovery / Metadata fallback，只证明 identity、v1 timestamp、subject 与 abstract；机制和实验结论不从 metadata 推断。
- Artifact-boundary routing 覆盖 19 个 family：exact v1 为 19 个 family 披露 artifact/evidence locator，其中 11 个提供外部 repository/project/demo locator，另有 0 个未披露；本日确认 0 个 family、0 个 event-time pinned commit。未确认 pinned commit 的 locator 只进入 Evidence boundary，不冒充 `SRC-GITHUB-COMMIT` coverage hit。
- 2026-08-25 才生效的机构源与 Hugging Face 不倒推为本历史窗口 Required Daily。工程 release 仍由 Sunday Weekly 承担。
- 标题路由外的垂直应用、单数据集增量和没有状态/控制权变化的论文在 topic-level closure 中拒绝，不用大量零分行稀释账本。

## 2. Candidate Ledger

<!-- validator:candidate-ledger-v2.1 -->
| Source Family ID | Primary Identifier | Event Identity | Owner Week | First-public Date | Supporting Source IDs | Design Delta | System Reach | Durability | Total | Candidate State | Review Status | Access Status | Review Override | Review Ref | Owner Report Ref | Prior Review Ref | Reconciliation | Stable Node ID | Books Disposition | Books Review Ref | Benchmark Claim |
| --- | --- | --- | --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2607-17525 | arXiv:2607.17525v1 | paper-v1:2607.17525 | 2026-W30 | 2026-07-20 | SRC-ARXIV | 3 | 3 | 2 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-17525 | self | — | new_in_window | PLATFORM-MONITORING | Integrate | books-review:SF-2026-ARXIV-2607-17525 | yes |
| SF-2026-ARXIV-2607-17545 | arXiv:2607.17545v1 | paper-v1:2607.17545 | 2026-W30 | 2026-07-20 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-17545 | self | — | new_in_window | AGENT-MEMORY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2607-17545 | yes |
| SF-2026-ARXIV-2607-17621 | arXiv:2607.17621v1 | paper-v1:2607.17621 | 2026-W30 | 2026-07-20 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-17621 | self | — | new_in_window | AGENT-MEMORY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2607-17621 | yes |
| SF-2026-ARXIV-2607-17715 | arXiv:2607.17715v1 | paper-v1:2607.17715 | 2026-W30 | 2026-07-20 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-17715 | self | — | new_in_window | INFER-KV-CACHE | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2607-17715 | yes |
| SF-2026-ARXIV-2607-17733 | arXiv:2607.17733v1 | paper-v1:2607.17733 | 2026-W30 | 2026-07-20 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-17733 | self | — | new_in_window | INFER-TENSORRT-LLM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2607-17733 | yes |
| SF-2026-ARXIV-2607-17747 | arXiv:2607.17747v1 | paper-v1:2607.17747 | 2026-W30 | 2026-07-20 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-17747 | self | — | new_in_window | MULTIMODAL-WORLD-MODELS | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2607-17747 | yes |
| SF-2026-ARXIV-2607-17751 | arXiv:2607.17751v1 | paper-v1:2607.17751 | 2026-W30 | 2026-07-20 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-17751 | self | — | new_in_window | AGENT-TOOL-CALLING | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2607-17751 | yes |
| SF-2026-ARXIV-2607-17786 | arXiv:2607.17786v1 | paper-v1:2607.17786 | 2026-W30 | 2026-07-20 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-17786 | self | — | new_in_window | MULTIMODAL-EMBODIED-VLA | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2607-17786 | yes |
| SF-2026-ARXIV-2607-17914 | arXiv:2607.17914v1 | paper-v1:2607.17914 | 2026-W30 | 2026-07-20 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-17914 | self | — | new_in_window | AGENT-MULTI-AGENT | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2607-17914 | yes |
| SF-2026-ARXIV-2607-17973 | arXiv:2607.17973v1 | paper-v1:2607.17973 | 2026-W30 | 2026-07-20 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-17973 | self | — | new_in_window | MULTIMODAL-WORLD-MODELS | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2607-17973 | yes |
| SF-2026-ARXIV-2607-17979 | arXiv:2607.17979v1 | paper-v1:2607.17979 | 2026-W30 | 2026-07-20 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-17979 | self | — | new_in_window | INFER-TENSORRT-LLM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2607-17979 | yes |
| SF-2026-ARXIV-2607-17986 | arXiv:2607.17986v1 | paper-v1:2607.17986 | 2026-W30 | 2026-07-20 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | release_security_contract | review:SF-2026-ARXIV-2607-17986 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2607-17986 | yes |
| SF-2026-ARXIV-2607-18016 | arXiv:2607.18016v1 | paper-v1:2607.18016 | 2026-W30 | 2026-07-20 | SRC-ARXIV | 3 | 3 | 2 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-18016 | self | — | new_in_window | MULTIMODAL-EMBODIED-VLA | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2607-18016 | yes |
| SF-2026-ARXIV-2607-18110 | arXiv:2607.18110v1 | paper-v1:2607.18110 | 2026-W30 | 2026-07-21 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-18110 | self | — | new_in_window | TRAIN-SFT | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2607-18110 | yes |
| SF-2026-ARXIV-2607-18141 | arXiv:2607.18141v1 | paper-v1:2607.18141 | 2026-W30 | 2026-07-21 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-18141 | self | — | new_in_window | INFER-GPU-MEMORY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2607-18141 | yes |
| SF-2026-ARXIV-2607-18171 | arXiv:2607.18171v1 | paper-v1:2607.18171 | 2026-W30 | 2026-07-21 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-18171 | self | — | new_in_window | AGENT-WORKFLOW | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2607-18171 | yes |
| SF-2026-ARXIV-2607-18213 | arXiv:2607.18213v1 | paper-v1:2607.18213 | 2026-W30 | 2026-07-21 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-18213 | self | — | new_in_window | AGENT-CONTEXT | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2607-18213 | yes |
| SF-2026-ARXIV-2607-18231 | arXiv:2607.18231v1 | paper-v1:2607.18231 | 2026-W30 | 2026-07-21 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-18231 | self | — | new_in_window | MULTIMODAL-EMBODIED-VLA | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2607-18231 | yes |
| SF-2026-ARXIV-2607-18603 | arXiv:2607.18603v1 | paper-v1:2607.18603 | 2026-W30 | 2026-07-21 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-18603 | self | — | new_in_window | AGENT-RAG | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2607-18603 | yes |

## 3. Review Completion Receipt

<!-- validator:review-completion-v1 -->
| Source Family ID | Review Provenance ID | Review Route | Primary Evidence Version | Reviewed Evidence Versions | Method / Identity Locators | Evaluation Locators | Limitations / Counterevidence Locators | Artifact Locators | Claim Boundary Ref | Completion Result |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2607-17525 | RP-25ae6373a7ba002d | deep | arXiv:2607.17525v1 | SRC-ARXIV@arXiv:2607.17525v1 | https://arxiv.org/html/2607.17525v1#S3 :: exact-v1 method/theory/implementation evidence; https://arxiv.org/html/2607.17525v1#S4 :: exact-v1 method/theory/implementation evidence | https://arxiv.org/html/2607.17525v1#S6 :: exact-v1 evaluation/ablation/setup evidence; https://arxiv.org/html/2607.17525v1#S8 :: exact-v1 evaluation/ablation/setup evidence | https://arxiv.org/html/2607.17525v1#A1 :: exact-v1 limitations, counterevidence, reproducibility or implementation boundary; 结构化 failure schema 增加跨层 correlation、标签治理和复现成本；未知 failure 仍需 trace 与人工调查，taxonomy 不能替代 SLO、canary 或 fault injection。 | https://github.com/Vishal-sys-code/failure-atlas — disclosed artifact locator; arXiv v1 links the author catalog repository; event-time commit is not pinned, so the review uses the manuscript catalog and case studies, not current repository behavior. | claim:SF-2026-ARXIV-2607-17525 | complete |
| SF-2026-ARXIV-2607-17545 | RP-7fd4f3cf38e8f91b | deep | arXiv:2607.17545v1 | SRC-ARXIV@arXiv:2607.17545v1 | https://arxiv.org/html/2607.17545v1#Sx3 :: exact-v1 method/theory/implementation evidence; https://arxiv.org/html/2607.17545v1#Sx4 :: exact-v1 method/theory/implementation evidence | https://arxiv.org/html/2607.17545v1#Sx5 :: exact-v1 evaluation/ablation/setup evidence; https://arxiv.org/html/2607.17545v1#A1 :: exact-v1 evaluation/ablation/setup evidence | https://arxiv.org/html/2607.17545v1#A2 :: exact-v1 limitations, counterevidence, reproducibility or implementation boundary; 学习 router 引入离线标签偏差、operator drift、错误不可逆压缩与维护成本；高风险 memory 应保留 provenance、raw fallback 和 abstention。 | https://arxiv.org/html/2607.17545v1#Sx3 — disclosed artifact locator; Not Disclosed — arXiv v1 exposes no author code, checkpoint, or immutable experiment bundle. | claim:SF-2026-ARXIV-2607-17545 | complete |
| SF-2026-ARXIV-2607-17621 | RP-cc2240cbda307f62 | deep | arXiv:2607.17621v1 | SRC-ARXIV@arXiv:2607.17621v1 | https://arxiv.org/html/2607.17621v1#S2 :: exact-v1 method/theory/implementation evidence; https://arxiv.org/html/2607.17621v1#S3 :: exact-v1 method/theory/implementation evidence | https://arxiv.org/html/2607.17621v1#S4 :: exact-v1 evaluation/ablation/setup evidence; https://arxiv.org/html/2607.17621v1#S5 :: exact-v1 evaluation/ablation/setup evidence | https://arxiv.org/html/2607.17621v1#A7 :: exact-v1 limitations, counterevidence, reproducibility or implementation boundary; 内部 attribution 增加模型耦合、额外 forward 成本和伪因果风险；模型 revision 后需重新校准，事实 authority 仍由原始 episode/verifier 持有。 | https://anonymous.4open.science/r/AGMR_code-3262/ — disclosed artifact locator; arXiv v1 links an anonymous code snapshot; commit identity and post-release history are not disclosed, so no current-code claim is retained. | claim:SF-2026-ARXIV-2607-17621 | complete |
| SF-2026-ARXIV-2607-17715 | RP-41bd17d5220b4eed | deep | arXiv:2607.17715v1 | SRC-ARXIV@arXiv:2607.17715v1 | https://arxiv.org/html/2607.17715v1#S3 :: exact-v1 method/theory/implementation evidence; https://arxiv.org/html/2607.17715v1#S4 :: exact-v1 method/theory/implementation evidence | https://arxiv.org/html/2607.17715v1#A2 :: exact-v1 evaluation/ablation/setup evidence; https://arxiv.org/html/2607.17715v1#A3 :: exact-v1 evaluation/ablation/setup evidence | https://arxiv.org/html/2607.17715v1#A5 :: exact-v1 limitations, counterevidence, reproducibility or implementation boundary; 组合压缩减少存储与 prefill，却引入重建 kernel、seam error、policy identity、fallback 和 tail-latency 风险；正确性优先时仍应 full KV 或 recompute。 | https://github.com/s7a9/C2KV — disclosed artifact locator; arXiv v1 links the author repository; event-time commit is not pinned, therefore implementation claims remain bound to the manuscript and declared artifact identity. | claim:SF-2026-ARXIV-2607-17715 | complete |
| SF-2026-ARXIV-2607-17733 | RP-0f1a6e562a62dbbe | deep | arXiv:2607.17733v1 | SRC-ARXIV@arXiv:2607.17733v1 | https://arxiv.org/html/2607.17733v1#S3 :: exact-v1 method/theory/implementation evidence; https://arxiv.org/html/2607.17733v1#S4 :: exact-v1 method/theory/implementation evidence | https://arxiv.org/html/2607.17733v1#S5 :: exact-v1 evaluation/ablation/setup evidence; https://arxiv.org/html/2607.17733v1#S6 :: exact-v1 evaluation/ablation/setup evidence | https://arxiv.org/html/2607.17733v1#A1 :: exact-v1 limitations, counterevidence, reproducibility or implementation boundary; mixed precision 增加 calibration、layout clustering、metadata、kernel fragmentation 和模型升级成本；硬件不支持时统一精度仍更快。 | https://github.com/parsa-epfl/mxsens — disclosed artifact locator; arXiv v1 links the author repository; event-time commit is not pinned and the review does not project current backend support backward. | claim:SF-2026-ARXIV-2607-17733 | complete |
| SF-2026-ARXIV-2607-17747 | RP-b930c17ce63ab3ee | standard | arXiv:2607.17747v1 | SRC-ARXIV@arXiv:2607.17747v1 | https://arxiv.org/html/2607.17747v1#S4 :: exact-v1 method/theory/implementation evidence; https://arxiv.org/html/2607.17747v1#S5 :: exact-v1 method/theory/implementation evidence | https://arxiv.org/html/2607.17747v1#S6 :: exact-v1 evaluation/ablation/setup evidence; https://arxiv.org/html/2607.17747v1#S7 :: exact-v1 evaluation/ablation/setup evidence | https://arxiv.org/html/2607.17747v1#A0.SS3 :: exact-v1 limitations, counterevidence, reproducibility or implementation boundary; learned dynamics 扩大建模范围，却引入 model bias、distribution shift、unsafe rollout 与在线校准成本；安全约束仍需显式 controller。 | https://arxiv.org/html/2607.17747v1#S4 — disclosed artifact locator; Not Disclosed — arXiv v1 exposes no author repository or immutable simulator bundle. | claim:SF-2026-ARXIV-2607-17747 | complete |
| SF-2026-ARXIV-2607-17751 | RP-566e09107ebf61bf | deep | arXiv:2607.17751v1 | SRC-ARXIV@arXiv:2607.17751v1 | https://arxiv.org/html/2607.17751v1#S3 :: exact-v1 method/theory/implementation evidence; https://arxiv.org/html/2607.17751v1#S4 :: exact-v1 method/theory/implementation evidence | https://arxiv.org/html/2607.17751v1#S5 :: exact-v1 evaluation/ablation/setup evidence; https://arxiv.org/html/2607.17751v1#S6 :: exact-v1 evaluation/ablation/setup evidence | https://arxiv.org/html/2607.17751v1#A2 :: exact-v1 limitations, counterevidence, reproducibility or implementation boundary; 多阶段选择增加 latency、LLM calls、counterfactual noise、catalog freshness 和评估成本；高风险动作仍需 schema validation 与 authorization。 | https://arxiv.org/html/2607.17751v1#S3 — disclosed artifact locator; Not Disclosed — arXiv v1 exposes no author code or immutable retrieval index. | claim:SF-2026-ARXIV-2607-17751 | complete |
| SF-2026-ARXIV-2607-17786 | RP-e53ebb855187cc87 | deep | arXiv:2607.17786v1 | SRC-ARXIV@arXiv:2607.17786v1 | https://arxiv.org/html/2607.17786v1#S3 :: exact-v1 method/theory/implementation evidence; https://arxiv.org/html/2607.17786v1#S4 :: exact-v1 method/theory/implementation evidence | https://arxiv.org/html/2607.17786v1#S5 :: exact-v1 evaluation/ablation/setup evidence; https://arxiv.org/html/2607.17786v1#S7 :: exact-v1 evaluation/ablation/setup evidence | https://arxiv.org/html/2607.17786v1#A16 :: exact-v1 limitations, counterevidence, reproducibility or implementation boundary; 可解释中间 state 提供检测点，也增加 prompt/visual attack surface、latency 和 stage mismatch；低层 controller 与 safety envelope 仍需独立。 | https://arxiv.org/html/2607.17786v1#S3 — disclosed artifact locator; Not Disclosed — no author code or checkpoint is linked from arXiv v1. | claim:SF-2026-ARXIV-2607-17786 | complete |
| SF-2026-ARXIV-2607-17914 | RP-42fd3ea64e44604e | standard | arXiv:2607.17914v1 | SRC-ARXIV@arXiv:2607.17914v1 | https://arxiv.org/html/2607.17914v1#S4 :: exact-v1 method/theory/implementation evidence; https://arxiv.org/html/2607.17914v1#S5 :: exact-v1 method/theory/implementation evidence | https://arxiv.org/html/2607.17914v1#S6 :: exact-v1 evaluation/ablation/setup evidence; https://arxiv.org/html/2607.17914v1#A2 :: exact-v1 evaluation/ablation/setup evidence | https://arxiv.org/html/2607.17914v1#A3 :: exact-v1 limitations, counterevidence, reproducibility or implementation boundary; value-aware prediction 减少通信依赖，但引入 predictor bias、错误协同与不可读 state；typed message 和 timeout fallback 仍必要。 | https://github.com/robust-comm-marl-IROS2026/Value-Aware-Prediction-Under-Communication-Loss — disclosed artifact locator; arXiv v1 links the author repository; event-time commit is not pinned. | claim:SF-2026-ARXIV-2607-17914 | complete |
| SF-2026-ARXIV-2607-17973 | RP-def916db0285c923 | deep | arXiv:2607.17973v1 | SRC-ARXIV@arXiv:2607.17973v1 | https://arxiv.org/html/2607.17973v1#S3 :: exact-v1 method/theory/implementation evidence; https://arxiv.org/html/2607.17973v1#S4 :: exact-v1 method/theory/implementation evidence | https://arxiv.org/html/2607.17973v1#S5 :: exact-v1 evaluation/ablation/setup evidence; https://arxiv.org/html/2607.17973v1#A1.SS2 :: exact-v1 evaluation/ablation/setup evidence | https://arxiv.org/html/2607.17973v1#A1.SS7 :: exact-v1 limitations, counterevidence, reproducibility or implementation boundary; subgoal 降低 branching，却增加层级 credit assignment、错 subgoal 锁定和 decoder mismatch；平坦 controller 在短任务仍合理。 | https://arxiv.org/html/2607.17973v1#S3 — disclosed artifact locator; Not Disclosed — arXiv v1 exposes no author repository or event-time artifact. | claim:SF-2026-ARXIV-2607-17973 | complete |
| SF-2026-ARXIV-2607-17979 | RP-61a150a6cefad78a | deep | arXiv:2607.17979v1 | SRC-ARXIV@arXiv:2607.17979v1 | https://arxiv.org/html/2607.17979v1#S2 :: exact-v1 method/theory/implementation evidence; https://arxiv.org/html/2607.17979v1#S3 :: exact-v1 method/theory/implementation evidence | https://arxiv.org/html/2607.17979v1#S4 :: exact-v1 evaluation/ablation/setup evidence; https://arxiv.org/html/2607.17979v1#S5 :: exact-v1 evaluation/ablation/setup evidence | https://arxiv.org/html/2607.17979v1#A9 :: exact-v1 limitations, counterevidence, reproducibility or implementation boundary; harness 提高有效搜索率，却可能把 benchmark quirks 编进策略，并增加 verifier、sandbox 和 measurement 成本；最终 artifact 仍需独立 validation。 | https://github.com/syhya/mlsys26-flashinfer-contest — disclosed artifact locator; arXiv v1 links several author contest repositories for fused MoE, gated delta net and sparse attention; event-time commits are not pinned. | claim:SF-2026-ARXIV-2607-17979 | complete |
| SF-2026-ARXIV-2607-17986 | RP-83f50b15b0b48037 | deep | arXiv:2607.17986v1 | SRC-ARXIV@arXiv:2607.17986v1 | https://arxiv.org/html/2607.17986v1#S2 :: exact-v1 method/theory/implementation evidence; https://arxiv.org/html/2607.17986v1#S3 :: exact-v1 method/theory/implementation evidence | https://arxiv.org/html/2607.17986v1#S4 :: exact-v1 evaluation/ablation/setup evidence; https://arxiv.org/html/2607.17986v1#S5 :: exact-v1 evaluation/ablation/setup evidence | https://arxiv.org/html/2607.17986v1#A7 :: exact-v1 limitations, counterevidence, reproducibility or implementation boundary; 检测与备份增加 false positive、rollback、sensitive snapshot 和恢复一致性成本；低变更层继续使用静态 protection，高风险更新需 application-level verifier。 | https://arxiv.org/html/2607.17986v1#S2 — disclosed artifact locator; arXiv v1 describes open-science materials, but no immutable event-time repository/commit is recoverable from the manuscript link surface used here; no code claim retained. | claim:SF-2026-ARXIV-2607-17986 | complete |
| SF-2026-ARXIV-2607-18016 | RP-31d459caa9efcb3d | deep | arXiv:2607.18016v1 | SRC-ARXIV@arXiv:2607.18016v1 | https://arxiv.org/html/2607.18016v1#S3 :: exact-v1 method/theory/implementation evidence; https://arxiv.org/html/2607.18016v1#S4 :: exact-v1 method/theory/implementation evidence | https://arxiv.org/html/2607.18016v1#S5 :: exact-v1 evaluation/ablation/setup evidence; https://arxiv.org/html/2607.18016v1#A1 :: exact-v1 evaluation/ablation/setup evidence | https://arxiv.org/html/2607.18016v1#A1 :: exact-v1 limitations, counterevidence, reproducibility or implementation boundary; persistent token 提高可验证性，却引入 object association、stale token、merge/split 和生命周期管理；原始 sensor evidence 仍是 fallback。 | https://arxiv.org/html/2607.18016v1#S3 — disclosed artifact locator; Not Disclosed — no author code/checkpoint is linked from arXiv v1. | claim:SF-2026-ARXIV-2607-18016 | complete |
| SF-2026-ARXIV-2607-18110 | RP-dd7070951fd33b46 | deep | arXiv:2607.18110v1 | SRC-ARXIV@arXiv:2607.18110v1 | https://arxiv.org/html/2607.18110v1#S2 :: exact-v1 method/theory/implementation evidence; https://arxiv.org/html/2607.18110v1#S3 :: exact-v1 method/theory/implementation evidence | https://arxiv.org/html/2607.18110v1#S4 :: exact-v1 evaluation/ablation/setup evidence; https://arxiv.org/html/2607.18110v1#A1 :: exact-v1 evaluation/ablation/setup evidence | https://arxiv.org/html/2607.18110v1#A1 :: exact-v1 limitations, counterevidence, reproducibility or implementation boundary; textual coaching 增加 teacher cost、bias、self-confirmation 和数据 lineage；规则稳定时普通 SFT 或 preference data 更便宜。 | https://aka.ms/el-code — disclosed artifact locator; arXiv v1 links the author code landing URL; resolved event-time commit is not disclosed. | claim:SF-2026-ARXIV-2607-18110 | complete |
| SF-2026-ARXIV-2607-18141 | RP-843a2c159617acd1 | deep | arXiv:2607.18141v1 | SRC-ARXIV@arXiv:2607.18141v1 | https://arxiv.org/html/2607.18141v1#S3 :: exact-v1 method/theory/implementation evidence; https://arxiv.org/html/2607.18141v1#S4 :: exact-v1 method/theory/implementation evidence | https://arxiv.org/html/2607.18141v1#S5 :: exact-v1 evaluation/ablation/setup evidence; https://arxiv.org/html/2607.18141v1#S6 :: exact-v1 evaluation/ablation/setup evidence | https://arxiv.org/html/2607.18141v1#S8 :: exact-v1 limitations, counterevidence, reproducibility or implementation boundary; pooling 提高容量与复用，却增加 fabric latency、contention、ownership、security、failure blast radius 和 prefetch prediction；热 KV 仍应留 HBM。 | https://arxiv.org/html/2607.18141v1#S3 — disclosed artifact locator; Not Disclosed — arXiv v1 cites Dynamo/AIperf/NIXL dependencies but exposes no immutable author system repository. | claim:SF-2026-ARXIV-2607-18141 | complete |
| SF-2026-ARXIV-2607-18171 | RP-d557b02644bdaef7 | deep | arXiv:2607.18171v1 | SRC-ARXIV@arXiv:2607.18171v1 | https://arxiv.org/html/2607.18171v1#S3 :: exact-v1 method/theory/implementation evidence; https://arxiv.org/html/2607.18171v1#S4 :: exact-v1 method/theory/implementation evidence | https://arxiv.org/html/2607.18171v1#S5 :: exact-v1 evaluation/ablation/setup evidence; https://arxiv.org/html/2607.18171v1#S8 :: exact-v1 evaluation/ablation/setup evidence | https://arxiv.org/html/2607.18171v1#S9 :: exact-v1 limitations, counterevidence, reproducibility or implementation boundary; IR 提升可验证性，却增加 frontend、semantic gap、measurement noise 和 benchmark overfit；低复杂度应用仍可用人工实现。 | https://github.com/Infini-AI-Lab/FlashRT — disclosed artifact locator; arXiv v1 links the author repository; event-time commit is not pinned. | claim:SF-2026-ARXIV-2607-18171 | complete |
| SF-2026-ARXIV-2607-18213 | RP-9fd4be8cde9ac227 | deep | arXiv:2607.18213v1 | SRC-ARXIV@arXiv:2607.18213v1 | https://arxiv.org/html/2607.18213v1#S3 :: exact-v1 method/theory/implementation evidence; https://arxiv.org/html/2607.18213v1#S4 :: exact-v1 method/theory/implementation evidence | https://arxiv.org/html/2607.18213v1#S5 :: exact-v1 evaluation/ablation/setup evidence; https://arxiv.org/html/2607.18213v1#Sx1 :: exact-v1 evaluation/ablation/setup evidence | https://arxiv.org/html/2607.18213v1#A5 :: exact-v1 limitations, counterevidence, reproducibility or implementation boundary; learned pruning 降低 token，却引入 scorer retraining、false prune、cache/re-forward 和 hidden-state coupling；高风险 edit 应回读原文。 | https://github.com/Ayanami1314/swe-pruner-pro — disclosed artifact locator; arXiv v1 links the author repository; event-time commit is not pinned. | claim:SF-2026-ARXIV-2607-18213 | complete |
| SF-2026-ARXIV-2607-18231 | RP-c0f576c30ca41d50 | deep | arXiv:2607.18231v1 | SRC-ARXIV@arXiv:2607.18231v1 | https://arxiv.org/html/2607.18231v1#S3 :: exact-v1 method/theory/implementation evidence; https://arxiv.org/html/2607.18231v1#S4 :: exact-v1 method/theory/implementation evidence | https://arxiv.org/html/2607.18231v1#S5 :: exact-v1 evaluation/ablation/setup evidence; https://arxiv.org/html/2607.18231v1#A5 :: exact-v1 evaluation/ablation/setup evidence | https://arxiv.org/html/2607.18231v1#A5 :: exact-v1 limitations, counterevidence, reproducibility or implementation boundary; force state 改善 partial observability，却引入 calibration、sensor failure、history drift 和 embodiment-specific schema；低接触任务不需此成本。 | https://qft-333.github.io/FM-VLA-Page/ — disclosed artifact locator; arXiv v1 links a project page but no immutable code/checkpoint commit. | claim:SF-2026-ARXIV-2607-18231 | complete |
| SF-2026-ARXIV-2607-18603 | RP-e546b0afca5a6085 | deep | arXiv:2607.18603v1 | SRC-ARXIV@arXiv:2607.18603v1 | https://arxiv.org/html/2607.18603v1#S3 :: exact-v1 method/theory/implementation evidence; https://arxiv.org/html/2607.18603v1#S4 :: exact-v1 method/theory/implementation evidence | https://arxiv.org/html/2607.18603v1#S5 :: exact-v1 evaluation/ablation/setup evidence; https://arxiv.org/html/2607.18603v1#S6.SS4 :: exact-v1 evaluation/ablation/setup evidence | https://arxiv.org/html/2607.18603v1#A1.SS2 :: exact-v1 limitations, counterevidence, reproducibility or implementation boundary; program search 提升适配性，却增加 validation leakage、search cost、index rebuild、program drift 与解释复杂度；生产仍需 canary/rollback。 | https://github.com/auto-index/autoindex — disclosed artifact locator; arXiv v1 links the author repository; event-time commit is not pinned. | claim:SF-2026-ARXIV-2607-18603 | complete |

### Source Reviews

<!-- review:SF-2026-ARXIV-2607-17525:start -->
#### FailureAtlas: A Taxonomy of Failure Modes in Multi-Provider LLM Serving Infrastructure

<!-- claim:SF-2026-ARXIV-2607-17525:start -->正文给出 taxonomy construction、纳入标准、两项完全刻画案例与完整 catalog；它支持结构化 failure schema 的可用性，不证明 catalog 完备，也不证明任一 gateway 的生产发生率。 该结论只在论文公开的 workload 与 evaluation contract 内成立，不外推为通用生产结论。<!-- claim:SF-2026-ARXIV-2607-17525:end -->

**旧方案与约束变化。** `Ch67 已区分 transport_error_rate、contract_failure_rate 与 runtime-success/quality-failure，但尚未把 failure origin 与 detectability 组成可操作的分类坐标，也没有说明 silent failure 如何进入可观测性闭环。`（`books/part-06-ai-infrastructure/67-monitoring.md#L1`）旧方案在状态局部、规模较小或 SLO 宽松时继续成立；本 family 面对的新增压力由其 v1 problem statement 和 method 明确限定。

**机制、状态与代价。** 把多 provider serving 的 failure 以 origin layer 与 detectability 两轴建模，再由 issue evidence、独立复现与完整 case study 连接现象、根因、检测信号和恢复动作。关键 delta 不是新增错误名单，而是把 runtime_success 与 semantic/continuity failure 分开。 它改变 `PLATFORM-MONITORING` 下的 state/data/control contract，同时引入 metadata、校准/选择误差、额外执行或恢复责任；这些代价必须和收益在同一 workload 内计量。

**Evaluation contract。** Method：`https://arxiv.org/html/2607.17525v1#S3 :: exact-v1 method/theory/implementation evidence; https://arxiv.org/html/2607.17525v1#S4 :: exact-v1 method/theory/implementation evidence`；Evaluation：`https://arxiv.org/html/2607.17525v1#S6 :: exact-v1 evaluation/ablation/setup evidence; https://arxiv.org/html/2607.17525v1#S8 :: exact-v1 evaluation/ablation/setup evidence`；Limitations/Counterevidence：`https://arxiv.org/html/2607.17525v1#A1 :: exact-v1 limitations, counterevidence, reproducibility or implementation boundary; 结构化 failure schema 增加跨层 correlation、标签治理和复现成本；未知 failure 仍需 trace 与人工调查，taxonomy 不能替代 SLO、canary 或 fault injection。`。未披露字段保持 `Not Disclosed`；作者结果不跨模型、硬件、精度、长度、batch、concurrency、SLO 或 evaluator 外推。

- Score V2：Design Delta 3 / System Reach 3 / Durability 2 = **8/9**。
- Evolution relation：`Direct Evolution`。
- Stable owner：`PLATFORM-MONITORING`。
- Books disposition：`Integrate`。
<!-- review:SF-2026-ARXIV-2607-17525:end -->

<!-- review:SF-2026-ARXIV-2607-17545:start -->
#### Retain or Consolidate? Budget-Dependent Operator Selection for Language Agent Memory

<!-- claim:SF-2026-ARXIV-2607-17545:start -->作者在多预算、跨模型实验中观察到 retain/consolidate crossover，并报告 learned router 的选择结果；证据仍受 benchmark、operator set、label generator 与预算定义约束。 该结论只在论文公开的 workload 与 evaluation contract 内成立，不外推为通用生产结论。<!-- claim:SF-2026-ARXIV-2607-17545:end -->

**旧方案与约束变化。** `Ch77 已完整拥有 write-time summary、query-conditioned construction、预算化检索、consolidation/forgetting、derived-memory lineage 与 raw-evidence fallback，并明确不同 workload 下 retain 与 consolidate 共存。`（`books/part-07-agent/77-memory.md#L244`）旧方案在状态局部、规模较小或 SLO 宽松时继续成立；本 family 面对的新增压力由其 v1 problem statement 和 method 明确限定。

**机制、状态与代价。** 把 retain 与多种 generative consolidation operator 视为受 token budget 约束的可选择动作，以只使用在线可观测特征的 utility router 决定何时压缩、使用哪种压缩，并用 risk-controlled threshold 保留 abstain 路径。 它改变 `AGENT-MEMORY` 下的 state/data/control contract，同时引入 metadata、校准/选择误差、额外执行或恢复责任；这些代价必须和收益在同一 workload 内计量。

**Evaluation contract。** Method：`https://arxiv.org/html/2607.17545v1#Sx3 :: exact-v1 method/theory/implementation evidence; https://arxiv.org/html/2607.17545v1#Sx4 :: exact-v1 method/theory/implementation evidence`；Evaluation：`https://arxiv.org/html/2607.17545v1#Sx5 :: exact-v1 evaluation/ablation/setup evidence; https://arxiv.org/html/2607.17545v1#A1 :: exact-v1 evaluation/ablation/setup evidence`；Limitations/Counterevidence：`https://arxiv.org/html/2607.17545v1#A2 :: exact-v1 limitations, counterevidence, reproducibility or implementation boundary; 学习 router 引入离线标签偏差、operator drift、错误不可逆压缩与维护成本；高风险 memory 应保留 provenance、raw fallback 和 abstention。`。未披露字段保持 `Not Disclosed`；作者结果不跨模型、硬件、精度、长度、batch、concurrency、SLO 或 evaluator 外推。

- Score V2：Design Delta 3 / System Reach 2 / Durability 3 = **8/9**。
- Evolution relation：`Layering / Dependency`。
- Stable owner：`AGENT-MEMORY`。
- Books disposition：`No Change — Existing Coverage`。
<!-- review:SF-2026-ARXIV-2607-17545:end -->

<!-- review:SF-2026-ARXIV-2607-17621:start -->
#### Mechanistic Attention Guidance for Agent Memory Refinement

<!-- claim:SF-2026-ARXIV-2607-17621:start -->Method、algorithm、实验、计算开销和附录共同支持 attribution-guided refinement 在论文任务中的差异；attention signal 不是因果真值，也未证明跨模型 calibration。 该结论只在论文公开的 workload 与 evaluation contract 内成立，不外推为通用生产结论。<!-- claim:SF-2026-ARXIV-2607-17621:end -->

**旧方案与约束变化。** `Ch77 已把 memory update 写成可撤销 proposal，并讨论 counterfactual attribution、terminal-reward credit assignment、provenance 和 verifier gate。`（`books/part-07-agent/77-memory.md#L46`）旧方案在状态局部、规模较小或 SLO 宽松时继续成立；本 family 面对的新增压力由其 v1 problem statement 和 method 明确限定。

**机制、状态与代价。** 从 frozen model 的 attention/attribution signal 提取 memory importance，引导 refine、保留或重写，而不是把一次 final reward 平均归因到全部 memory；更新仍是 derived-memory proposal，并需独立验证。 它改变 `AGENT-MEMORY` 下的 state/data/control contract，同时引入 metadata、校准/选择误差、额外执行或恢复责任；这些代价必须和收益在同一 workload 内计量。

**Evaluation contract。** Method：`https://arxiv.org/html/2607.17621v1#S2 :: exact-v1 method/theory/implementation evidence; https://arxiv.org/html/2607.17621v1#S3 :: exact-v1 method/theory/implementation evidence`；Evaluation：`https://arxiv.org/html/2607.17621v1#S4 :: exact-v1 evaluation/ablation/setup evidence; https://arxiv.org/html/2607.17621v1#S5 :: exact-v1 evaluation/ablation/setup evidence`；Limitations/Counterevidence：`https://arxiv.org/html/2607.17621v1#A7 :: exact-v1 limitations, counterevidence, reproducibility or implementation boundary; 内部 attribution 增加模型耦合、额外 forward 成本和伪因果风险；模型 revision 后需重新校准，事实 authority 仍由原始 episode/verifier 持有。`。未披露字段保持 `Not Disclosed`；作者结果不跨模型、硬件、精度、长度、batch、concurrency、SLO 或 evaluator 外推。

- Score V2：Design Delta 3 / System Reach 2 / Durability 3 = **8/9**。
- Evolution relation：`Layering / Dependency`。
- Stable owner：`AGENT-MEMORY`。
- Books disposition：`No Change — Existing Coverage`。
<!-- review:SF-2026-ARXIV-2607-17621:end -->

<!-- review:SF-2026-ARXIV-2607-17715:start -->
#### C^2KV: Compressed and Composable KV Cache Reuse for Efficient LLM Inference

<!-- claim:SF-2026-ARXIV-2607-17715:start -->Method、evaluation、timing 和 limitations 展示所测模型与 workload 中 compression+composition 的可行性；没有证明任意 attention 架构、任意位置变换或多租户并发下等价。 该结论只在论文公开的 workload 与 evaluation contract 内成立，不外推为通用生产结论。<!-- claim:SF-2026-ARXIV-2607-17715:end -->

**旧方案与约束变化。** `Ch45 已分别建立 position-dependent prefix reuse、压缩 policy identity、组合 transition object、exact fallback 与生产 SLO 边界，覆盖该机制的长期命题。`（`books/part-05-inference-system/45-why-kv-cache-speeds-up.md#L584`）旧方案在状态局部、规模较小或 SLO 宽松时继续成立；本 family 面对的新增压力由其 v1 problem statement 和 method 明确限定。

**机制、状态与代价。** 把 prefix KV 由完整 tensor 演进为可压缩、可组合的 cache object：压缩表示必须保留 position/model/policy identity，组合路径还需显式处理 segment seam 与 reconstruction error，而不能把 byte compatibility 当作 semantic composability。 它改变 `INFER-KV-CACHE` 下的 state/data/control contract，同时引入 metadata、校准/选择误差、额外执行或恢复责任；这些代价必须和收益在同一 workload 内计量。

**Evaluation contract。** Method：`https://arxiv.org/html/2607.17715v1#S3 :: exact-v1 method/theory/implementation evidence; https://arxiv.org/html/2607.17715v1#S4 :: exact-v1 method/theory/implementation evidence`；Evaluation：`https://arxiv.org/html/2607.17715v1#A2 :: exact-v1 evaluation/ablation/setup evidence; https://arxiv.org/html/2607.17715v1#A3 :: exact-v1 evaluation/ablation/setup evidence`；Limitations/Counterevidence：`https://arxiv.org/html/2607.17715v1#A5 :: exact-v1 limitations, counterevidence, reproducibility or implementation boundary; 组合压缩减少存储与 prefill，却引入重建 kernel、seam error、policy identity、fallback 和 tail-latency 风险；正确性优先时仍应 full KV 或 recompute。`。未披露字段保持 `Not Disclosed`；作者结果不跨模型、硬件、精度、长度、batch、concurrency、SLO 或 evaluator 外推。

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Evolution relation：`Layering / Dependency`。
- Stable owner：`INFER-KV-CACHE`。
- Books disposition：`No Change — Existing Coverage`。
<!-- review:SF-2026-ARXIV-2607-17715:end -->

<!-- review:SF-2026-ARXIV-2607-17733:start -->
#### MXSens: Sensitivity-Aware Mixed-Precision Quantization for Efficient LLM Inference

<!-- claim:SF-2026-ARXIV-2607-17733:start -->作者给出算法、硬件实验和 reproducibility 信息；结果绑定所测模型、GPU、kernel 与 calibration，不证明任意 backend 都可兑现同样的 physical packing。 该结论只在论文公开的 workload 与 evaluation contract 内成立，不外推为通用生产结论。<!-- claim:SF-2026-ARXIV-2607-17733:end -->

**旧方案与约束变化。** `Ch49 已明确量化不自动加速，并完整写出 sensitivity/average-bit → block clustering → physical layout → compatible kernel → measurement gate 的路线。`（`books/part-05-inference-system/49-tensorrt-llm.md#L417`）旧方案在状态局部、规模较小或 SLO 宽松时继续成立；本 family 面对的新增压力由其 v1 problem statement 和 method 明确限定。

**机制、状态与代价。** 先估计 layer/channel sensitivity，再在平均 bit budget 下分配混合精度，并把逻辑 bit allocation lowering 为可执行的 block/layout/kernel 组合；收益来自物理执行计划而非小数 bit 数本身。 它改变 `INFER-TENSORRT-LLM` 下的 state/data/control contract，同时引入 metadata、校准/选择误差、额外执行或恢复责任；这些代价必须和收益在同一 workload 内计量。

**Evaluation contract。** Method：`https://arxiv.org/html/2607.17733v1#S3 :: exact-v1 method/theory/implementation evidence; https://arxiv.org/html/2607.17733v1#S4 :: exact-v1 method/theory/implementation evidence`；Evaluation：`https://arxiv.org/html/2607.17733v1#S5 :: exact-v1 evaluation/ablation/setup evidence; https://arxiv.org/html/2607.17733v1#S6 :: exact-v1 evaluation/ablation/setup evidence`；Limitations/Counterevidence：`https://arxiv.org/html/2607.17733v1#A1 :: exact-v1 limitations, counterevidence, reproducibility or implementation boundary; mixed precision 增加 calibration、layout clustering、metadata、kernel fragmentation 和模型升级成本；硬件不支持时统一精度仍更快。`。未披露字段保持 `Not Disclosed`；作者结果不跨模型、硬件、精度、长度、batch、concurrency、SLO 或 evaluator 外推。

- Score V2：Design Delta 3 / System Reach 2 / Durability 3 = **8/9**。
- Evolution relation：`Layering / Dependency`。
- Stable owner：`INFER-TENSORRT-LLM`。
- Books disposition：`No Change — Existing Coverage`。
<!-- review:SF-2026-ARXIV-2607-17733:end -->

<!-- review:SF-2026-ARXIV-2607-17747:start -->
#### Mobile Network Control with a World Model

<!-- claim:SF-2026-ARXIV-2607-17747:start -->仿真与开放测试支持该任务合同中的 planning branch；不证明 world model 在未覆盖网络、突发故障或生产 control loop 中校准。 该结论只在论文公开的 workload 与 evaluation contract 内成立，不外推为通用生产结论。<!-- claim:SF-2026-ARXIV-2607-17747:end -->

**旧方案与约束变化。** `Ch25 已区分 simulator、learned transition、action-conditioned rollout、policy coupling 与显式 safety constraint。`（`books/part-03-multimodal-world-models/25-multimodal-world-models.md#L68`）旧方案在状态局部、规模较小或 SLO 宽松时继续成立；本 family 面对的新增压力由其 v1 problem statement 和 method 明确限定。

**机制、状态与代价。** 以 learned world model 预测 action-conditioned network state，再在模型内评估候选控制动作；状态估计、policy 和真实网络 transition 分离。 它改变 `MULTIMODAL-WORLD-MODELS` 下的 state/data/control contract，同时引入 metadata、校准/选择误差、额外执行或恢复责任；这些代价必须和收益在同一 workload 内计量。

**Evaluation contract。** Method：`https://arxiv.org/html/2607.17747v1#S4 :: exact-v1 method/theory/implementation evidence; https://arxiv.org/html/2607.17747v1#S5 :: exact-v1 method/theory/implementation evidence`；Evaluation：`https://arxiv.org/html/2607.17747v1#S6 :: exact-v1 evaluation/ablation/setup evidence; https://arxiv.org/html/2607.17747v1#S7 :: exact-v1 evaluation/ablation/setup evidence`；Limitations/Counterevidence：`https://arxiv.org/html/2607.17747v1#A0.SS3 :: exact-v1 limitations, counterevidence, reproducibility or implementation boundary; learned dynamics 扩大建模范围，却引入 model bias、distribution shift、unsafe rollout 与在线校准成本；安全约束仍需显式 controller。`。未披露字段保持 `Not Disclosed`；作者结果不跨模型、硬件、精度、长度、batch、concurrency、SLO 或 evaluator 外推。

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Evolution relation：`Layering / Dependency`。
- Stable owner：`MULTIMODAL-WORLD-MODELS`。
- Books disposition：`No Change — Existing Coverage`。
<!-- review:SF-2026-ARXIV-2607-17747:end -->

<!-- review:SF-2026-ARXIV-2607-17751:start -->
#### MagicSelector: Joint Optimization for Agent Tool Selection via Counterfactual Decomposition and Progressive Reranking

<!-- claim:SF-2026-ARXIV-2607-17751:start -->作者在论文 tool-selection benchmark 上比较组件与消融；结论受 catalog、query decomposition、base model 和 evaluator 约束。 该结论只在论文公开的 workload 与 evaluation contract 内成立，不外推为通用生产结论。<!-- claim:SF-2026-ARXIV-2607-17751:end -->

**旧方案与约束变化。** `Ch78 已把 tool discovery/selection 写成 catalog contract、coarse retrieval、reranking、schema/execution separation 与 bounded loop。`（`books/part-07-agent/78-tool-calling.md#L82`）旧方案在状态局部、规模较小或 SLO 宽松时继续成立；本 family 面对的新增压力由其 v1 problem statement 和 method 明确限定。

**机制、状态与代价。** 把 tool selection 从一次 top-k similarity 演进为 counterfactual decomposition 产生候选子意图，再以 progressive reranking 联合控制 recall 与 context budget；selector 只拥有 proposal，不拥有 execution authority。 它改变 `AGENT-TOOL-CALLING` 下的 state/data/control contract，同时引入 metadata、校准/选择误差、额外执行或恢复责任；这些代价必须和收益在同一 workload 内计量。

**Evaluation contract。** Method：`https://arxiv.org/html/2607.17751v1#S3 :: exact-v1 method/theory/implementation evidence; https://arxiv.org/html/2607.17751v1#S4 :: exact-v1 method/theory/implementation evidence`；Evaluation：`https://arxiv.org/html/2607.17751v1#S5 :: exact-v1 evaluation/ablation/setup evidence; https://arxiv.org/html/2607.17751v1#S6 :: exact-v1 evaluation/ablation/setup evidence`；Limitations/Counterevidence：`https://arxiv.org/html/2607.17751v1#A2 :: exact-v1 limitations, counterevidence, reproducibility or implementation boundary; 多阶段选择增加 latency、LLM calls、counterfactual noise、catalog freshness 和评估成本；高风险动作仍需 schema validation 与 authorization。`。未披露字段保持 `Not Disclosed`；作者结果不跨模型、硬件、精度、长度、batch、concurrency、SLO 或 evaluator 外推。

- Score V2：Design Delta 3 / System Reach 2 / Durability 3 = **8/9**。
- Evolution relation：`Layering / Dependency`。
- Stable owner：`AGENT-TOOL-CALLING`。
- Books disposition：`No Change — Existing Coverage`。
<!-- review:SF-2026-ARXIV-2607-17751:end -->

<!-- review:SF-2026-ARXIV-2607-17786:start -->
#### Reasoning as a Double-Edged Sword: Architecture and Cross-Stage Robustness in Vision-Language-Action Models

<!-- claim:SF-2026-ARXIV-2607-17786:start -->攻击设置、跨阶段实验与 defense study 支持“reasoning 可同时增益与放大脆弱性”；不证明开放世界攻击覆盖或真实机器人安全。 该结论只在论文公开的 workload 与 evaluation contract 内成立，不外推为通用生产结论。<!-- claim:SF-2026-ARXIV-2607-17786:end -->

**旧方案与约束变化。** `Ch26 已拥有 fast/slow controller、reasoning proposal、physical evidence、closed-loop failure 与 safety envelope；Ch72 拥有 authorization。`（`books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#L305`）旧方案在状态局部、规模较小或 SLO 宽松时继续成立；本 family 面对的新增压力由其 v1 problem statement 和 method 明确限定。

**机制、状态与代价。** 将 VLA robustness 分解到 perception/reasoning/action stages，比较 reasoning module 在 clean 与 attacked conditions 下的帮助和新攻击面；显式 reasoning state 是可观测 proposal，不是物理 safety certificate。 它改变 `MULTIMODAL-EMBODIED-VLA` 下的 state/data/control contract，同时引入 metadata、校准/选择误差、额外执行或恢复责任；这些代价必须和收益在同一 workload 内计量。

**Evaluation contract。** Method：`https://arxiv.org/html/2607.17786v1#S3 :: exact-v1 method/theory/implementation evidence; https://arxiv.org/html/2607.17786v1#S4 :: exact-v1 method/theory/implementation evidence`；Evaluation：`https://arxiv.org/html/2607.17786v1#S5 :: exact-v1 evaluation/ablation/setup evidence; https://arxiv.org/html/2607.17786v1#S7 :: exact-v1 evaluation/ablation/setup evidence`；Limitations/Counterevidence：`https://arxiv.org/html/2607.17786v1#A16 :: exact-v1 limitations, counterevidence, reproducibility or implementation boundary; 可解释中间 state 提供检测点，也增加 prompt/visual attack surface、latency 和 stage mismatch；低层 controller 与 safety envelope 仍需独立。`。未披露字段保持 `Not Disclosed`；作者结果不跨模型、硬件、精度、长度、batch、concurrency、SLO 或 evaluator 外推。

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Evolution relation：`Layering / Dependency`。
- Stable owner：`MULTIMODAL-EMBODIED-VLA`。
- Books disposition：`No Change — Existing Coverage`。
<!-- review:SF-2026-ARXIV-2607-17786:end -->

<!-- review:SF-2026-ARXIV-2607-17914:start -->
#### Value-Aware Prediction for Robust Multi-Agent Coordination Under Communication Loss

<!-- claim:SF-2026-ARXIV-2607-17914:start -->论文在其 MARL environments 与 loss patterns 下报告 coordination recovery；不证明开放网络或异构 LLM agent 的可靠性。 该结论只在论文公开的 workload 与 evaluation contract 内成立，不外推为通用生产结论。<!-- claim:SF-2026-ARXIV-2607-17914:end -->

**旧方案与约束变化。** `Ch82 已区分 message 与 authoritative state、讨论通信压缩/缺失、预算化 topology 和 fallback。`（`books/part-07-agent/82-multi-agent.md#L1`）旧方案在状态局部、规模较小或 SLO 宽松时继续成立；本 family 面对的新增压力由其 v1 problem statement 和 method 明确限定。

**机制、状态与代价。** 通信丢失时，不盲目补全全部消息，而预测对 joint value 有影响的缺失状态；fallback 仍受本地 observation 和 uncertainty bound 约束。 它改变 `AGENT-MULTI-AGENT` 下的 state/data/control contract，同时引入 metadata、校准/选择误差、额外执行或恢复责任；这些代价必须和收益在同一 workload 内计量。

**Evaluation contract。** Method：`https://arxiv.org/html/2607.17914v1#S4 :: exact-v1 method/theory/implementation evidence; https://arxiv.org/html/2607.17914v1#S5 :: exact-v1 method/theory/implementation evidence`；Evaluation：`https://arxiv.org/html/2607.17914v1#S6 :: exact-v1 evaluation/ablation/setup evidence; https://arxiv.org/html/2607.17914v1#A2 :: exact-v1 evaluation/ablation/setup evidence`；Limitations/Counterevidence：`https://arxiv.org/html/2607.17914v1#A3 :: exact-v1 limitations, counterevidence, reproducibility or implementation boundary; value-aware prediction 减少通信依赖，但引入 predictor bias、错误协同与不可读 state；typed message 和 timeout fallback 仍必要。`。未披露字段保持 `Not Disclosed`；作者结果不跨模型、硬件、精度、长度、batch、concurrency、SLO 或 evaluator 外推。

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Evolution relation：`Layering / Dependency`。
- Stable owner：`AGENT-MULTI-AGENT`。
- Books disposition：`No Change — Existing Coverage`。
<!-- review:SF-2026-ARXIV-2607-17914:end -->

<!-- review:SF-2026-ARXIV-2607-17973:start -->
#### SAGE: Subgoal-Conditioned Action Generation for Latent World Model Planning

<!-- claim:SF-2026-ARXIV-2607-17973:start -->作者实验和 capacity analysis 支持该 latent planning factorization 在所测环境中的收益；未证明 latent subgoal 可解释、可校准或迁移到真实环境。 该结论只在论文公开的 workload 与 evaluation contract 内成立，不外推为通用生产结论。<!-- claim:SF-2026-ARXIV-2607-17973:end -->

**旧方案与约束变化。** `Ch25 已完整讨论 latent dynamics、hierarchical temporal state、imagined rollout 与 planning/policy coupling。`（`books/part-03-multimodal-world-models/25-multimodal-world-models.md#L87`）旧方案在状态局部、规模较小或 SLO 宽松时继续成立；本 family 面对的新增压力由其 v1 problem statement 和 method 明确限定。

**机制、状态与代价。** 把长 horizon rollout 由平坦 action generation 分解为 subgoal-conditioned latent transition；subgoal 提供低频 planning state，低层 action generator 负责局部可执行性。 它改变 `MULTIMODAL-WORLD-MODELS` 下的 state/data/control contract，同时引入 metadata、校准/选择误差、额外执行或恢复责任；这些代价必须和收益在同一 workload 内计量。

**Evaluation contract。** Method：`https://arxiv.org/html/2607.17973v1#S3 :: exact-v1 method/theory/implementation evidence; https://arxiv.org/html/2607.17973v1#S4 :: exact-v1 method/theory/implementation evidence`；Evaluation：`https://arxiv.org/html/2607.17973v1#S5 :: exact-v1 evaluation/ablation/setup evidence; https://arxiv.org/html/2607.17973v1#A1.SS2 :: exact-v1 evaluation/ablation/setup evidence`；Limitations/Counterevidence：`https://arxiv.org/html/2607.17973v1#A1.SS7 :: exact-v1 limitations, counterevidence, reproducibility or implementation boundary; subgoal 降低 branching，却增加层级 credit assignment、错 subgoal 锁定和 decoder mismatch；平坦 controller 在短任务仍合理。`。未披露字段保持 `Not Disclosed`；作者结果不跨模型、硬件、精度、长度、batch、concurrency、SLO 或 evaluator 外推。

- Score V2：Design Delta 3 / System Reach 2 / Durability 3 = **8/9**。
- Evolution relation：`Layering / Dependency`。
- Stable owner：`MULTIMODAL-WORLD-MODELS`。
- Books disposition：`No Change — Existing Coverage`。
<!-- review:SF-2026-ARXIV-2607-17973:end -->

<!-- review:SF-2026-ARXIV-2607-17979:start -->
#### Harness Engineering for LLM-Driven GPU Kernel Generation

<!-- claim:SF-2026-ARXIV-2607-17979:start -->系统、workflow、kernel case studies 与 limitations 支持 harness 对 agent search 的影响；结果绑定 contest problems、hardware/compiler 与 evaluator。 该结论只在论文公开的 workload 与 evaluation contract 内成立，不外推为通用生产结论。<!-- claim:SF-2026-ARXIV-2607-17979:end -->

**旧方案与约束变化。** `Ch49 已把 learned kernel generator 定位为 candidate producer，并要求 operation descriptor、correctness oracle、compile/run sandbox、measurement gate 与版本化 execution plan；Ch81 只接 workflow handoff。`（`books/part-05-inference-system/49-tensorrt-llm.md#L1`）旧方案在状态局部、规模较小或 SLO 宽松时继续成立；本 family 面对的新增压力由其 v1 problem statement 和 method 明确限定。

**机制、状态与代价。** 将 kernel generation 从自由文本 coding 约束为 executable harness：精确 specification、reference implementation、correctness tests、measurement gate、failure feedback 和 workload-specific optimization budget。 它改变 `INFER-TENSORRT-LLM` 下的 state/data/control contract，同时引入 metadata、校准/选择误差、额外执行或恢复责任；这些代价必须和收益在同一 workload 内计量。

**Evaluation contract。** Method：`https://arxiv.org/html/2607.17979v1#S2 :: exact-v1 method/theory/implementation evidence; https://arxiv.org/html/2607.17979v1#S3 :: exact-v1 method/theory/implementation evidence`；Evaluation：`https://arxiv.org/html/2607.17979v1#S4 :: exact-v1 evaluation/ablation/setup evidence; https://arxiv.org/html/2607.17979v1#S5 :: exact-v1 evaluation/ablation/setup evidence`；Limitations/Counterevidence：`https://arxiv.org/html/2607.17979v1#A9 :: exact-v1 limitations, counterevidence, reproducibility or implementation boundary; harness 提高有效搜索率，却可能把 benchmark quirks 编进策略，并增加 verifier、sandbox 和 measurement 成本；最终 artifact 仍需独立 validation。`。未披露字段保持 `Not Disclosed`；作者结果不跨模型、硬件、精度、长度、batch、concurrency、SLO 或 evaluator 外推。

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Evolution relation：`Layering / Dependency`。
- Stable owner：`INFER-TENSORRT-LLM`。
- Books disposition：`No Change — Existing Coverage`。
<!-- review:SF-2026-ARXIV-2607-17979:end -->

<!-- review:SF-2026-ARXIV-2607-17986:start -->
#### Self-State Attacks on Self-Hosted AI Agents: How Far Can OS Defenses Go?

<!-- claim:SF-2026-ARXIV-2607-17986:start -->论文报告 23-cell/43-operation attack-defense matrix 与不可由 OS 区分的操作；这证明 OS 缺少 agent intent，而非证明其 catalog 完备或 detector 在生产校准。 该结论只在论文公开的 workload 与 evaluation contract 内成立，不外推为通用生产结论。<!-- claim:SF-2026-ARXIV-2607-17986:end -->

**旧方案与约束变化。** `Ch72 已逐层写入该 self-state protection/recovery 机制，并在 Review notes 保留此 exact source family。`（`books/part-06-ai-infrastructure/72-security.md#L1`）旧方案在状态局部、规模较小或 SLO 宽松时继续成立；本 family 面对的新增压力由其 v1 problem statement 和 method 明确限定。

**机制、状态与代价。** 把 agent self-state 分成 instruction、config、memory 等可变层，系统枚举 write primitive、attack path、OS control 与 recovery；静态 ACL 只能保护稳定层，动态 memory 需要 workload-conditioned detection，备份只提供恢复而非 prevention。 它改变 `PLATFORM-SECURITY` 下的 state/data/control contract，同时引入 metadata、校准/选择误差、额外执行或恢复责任；这些代价必须和收益在同一 workload 内计量。

**Evaluation contract。** Method：`https://arxiv.org/html/2607.17986v1#S2 :: exact-v1 method/theory/implementation evidence; https://arxiv.org/html/2607.17986v1#S3 :: exact-v1 method/theory/implementation evidence`；Evaluation：`https://arxiv.org/html/2607.17986v1#S4 :: exact-v1 evaluation/ablation/setup evidence; https://arxiv.org/html/2607.17986v1#S5 :: exact-v1 evaluation/ablation/setup evidence`；Limitations/Counterevidence：`https://arxiv.org/html/2607.17986v1#A7 :: exact-v1 limitations, counterevidence, reproducibility or implementation boundary; 检测与备份增加 false positive、rollback、sensitive snapshot 和恢复一致性成本；低变更层继续使用静态 protection，高风险更新需 application-level verifier。`；本次 RP 重新绑定历史 full-read coverage：`papers/2026/weekly/2026-W30/README.md#L562-L570`，其中具名记录了 Method、Evaluation 与 Boundary。未披露字段保持 `Not Disclosed`；作者结果不跨模型、硬件、精度、长度、batch、concurrency、SLO 或 evaluator 外推。

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Evolution relation：`Layering / Dependency`。
- Stable owner：`PLATFORM-SECURITY`。
- Books disposition：`No Change — Existing Coverage`。
<!-- review:SF-2026-ARXIV-2607-17986:end -->

<!-- review:SF-2026-ARXIV-2607-18016:start -->
#### Closing the Loop in Humanoid VLA: Persistent 3D Object Tokens for Verifiable Loco-Manipulation

<!-- claim:SF-2026-ARXIV-2607-18016:start -->方法与评估支持论文 humanoid tasks 中的闭环状态追踪；不证明开放世界 data association、真实硬件故障或长期 identity consistency。 该结论只在论文公开的 workload 与 evaluation contract 内成立，不外推为通用生产结论。<!-- claim:SF-2026-ARXIV-2607-18016:end -->

**旧方案与约束变化。** `Ch26 已把 object/trajectory identity、persistent revisable state、physical evidence、environment transition 与 closed-loop verification 连成主线。`（`books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#L171`）旧方案在状态局部、规模较小或 SLO 宽松时继续成立；本 family 面对的新增压力由其 v1 problem statement 和 method 明确限定。

**机制、状态与代价。** 以 persistent 3D object token 作为跨 perception、planning、locomotion/manipulation 的显式 state handle，使 observation 更新、目标指代、动作结果和 verifier 对齐到同一对象 identity。 它改变 `MULTIMODAL-EMBODIED-VLA` 下的 state/data/control contract，同时引入 metadata、校准/选择误差、额外执行或恢复责任；这些代价必须和收益在同一 workload 内计量。

**Evaluation contract。** Method：`https://arxiv.org/html/2607.18016v1#S3 :: exact-v1 method/theory/implementation evidence; https://arxiv.org/html/2607.18016v1#S4 :: exact-v1 method/theory/implementation evidence`；Evaluation：`https://arxiv.org/html/2607.18016v1#S5 :: exact-v1 evaluation/ablation/setup evidence; https://arxiv.org/html/2607.18016v1#A1 :: exact-v1 evaluation/ablation/setup evidence`；Limitations/Counterevidence：`https://arxiv.org/html/2607.18016v1#A1 :: exact-v1 limitations, counterevidence, reproducibility or implementation boundary; persistent token 提高可验证性，却引入 object association、stale token、merge/split 和生命周期管理；原始 sensor evidence 仍是 fallback。`。未披露字段保持 `Not Disclosed`；作者结果不跨模型、硬件、精度、长度、batch、concurrency、SLO 或 evaluator 外推。

- Score V2：Design Delta 3 / System Reach 3 / Durability 2 = **8/9**。
- Evolution relation：`Layering / Dependency`。
- Stable owner：`MULTIMODAL-EMBODIED-VLA`。
- Books disposition：`No Change — Existing Coverage`。
<!-- review:SF-2026-ARXIV-2607-18016:end -->

<!-- review:SF-2026-ARXIV-2607-18110:start -->
#### LLM-as-a-Coach: Experiential Learning for Non-Verifiable Tasks

<!-- claim:SF-2026-ARXIV-2607-18110:start -->作者在 held-out/OOD 与 ablation 下比较 coaching；只支持所测 task、coach/student 与 evaluator，不证明自然语言诊断无偏。 该结论只在论文公开的 workload 与 evaluation contract 内成立，不外推为通用生产结论。<!-- claim:SF-2026-ARXIV-2607-18110:end -->

**旧方案与约束变化。** `Ch29 已覆盖 teacher trajectory/diagnosis、context distillation、held-out oracle、teacher bias、staged transfer 和 reward-hacking boundary。`（`books/part-04-training-system/29-sft.md#L1`）旧方案在状态局部、规模较小或 SLO 宽松时继续成立；本 family 面对的新增压力由其 v1 problem statement 和 method 明确限定。

**机制、状态与代价。** 对不可自动验证任务，不把 scalar reward 当唯一 teacher；coach 读取 trajectory 与 outcome，生成带诊断的 experiential target，再蒸馏回 student。teacher feedback 是训练数据 proposal，仍需 held-out rubric 和 anti-reward-hacking checks。 它改变 `TRAIN-SFT` 下的 state/data/control contract，同时引入 metadata、校准/选择误差、额外执行或恢复责任；这些代价必须和收益在同一 workload 内计量。

**Evaluation contract。** Method：`https://arxiv.org/html/2607.18110v1#S2 :: exact-v1 method/theory/implementation evidence; https://arxiv.org/html/2607.18110v1#S3 :: exact-v1 method/theory/implementation evidence`；Evaluation：`https://arxiv.org/html/2607.18110v1#S4 :: exact-v1 evaluation/ablation/setup evidence; https://arxiv.org/html/2607.18110v1#A1 :: exact-v1 evaluation/ablation/setup evidence`；Limitations/Counterevidence：`https://arxiv.org/html/2607.18110v1#A1 :: exact-v1 limitations, counterevidence, reproducibility or implementation boundary; textual coaching 增加 teacher cost、bias、self-confirmation 和数据 lineage；规则稳定时普通 SFT 或 preference data 更便宜。`；本次 RP 重新绑定历史 full-read coverage：`papers/2026/weekly/2026-W30/README.md#L543-L551`，其中具名记录了 Method、Evaluation 与 Boundary。未披露字段保持 `Not Disclosed`；作者结果不跨模型、硬件、精度、长度、batch、concurrency、SLO 或 evaluator 外推。

- Score V2：Design Delta 3 / System Reach 2 / Durability 3 = **8/9**。
- Evolution relation：`Layering / Dependency`。
- Stable owner：`TRAIN-SFT`。
- Books disposition：`No Change — Existing Coverage`。
<!-- review:SF-2026-ARXIV-2607-18110:end -->

<!-- review:SF-2026-ARXIV-2607-18141:start -->
#### HyMCache: A KV Cache Framework for Multi-Turn LLM Serving with CXL-Hybrid Memory

<!-- claim:SF-2026-ARXIV-2607-18141:start -->characterization、system design、setup 与 evaluation 支持论文 hardware/workload 下的可行性；不证明不同 CXL topology、生产多租户隔离或 tail SLO。 该结论只在论文公开的 workload 与 evaluation contract 内成立，不外推为通用生产结论。<!-- claim:SF-2026-ARXIV-2607-18141:end -->

**旧方案与约束变化。** `Ch54 已有从 HBM→host→NVMe/network→CXL pooled state、persistent near-memory、ownership、prefetch 和 failure boundary 的完整路线。`（`books/part-05-inference-system/54-gpu-memory.md#L248`）旧方案在状态局部、规模较小或 SLO 宽松时继续成立；本 family 面对的新增压力由其 v1 problem statement 和 method 明确限定。

**机制、状态与代价。** 把跨 turn KV/session state 从单机 DRAM offload 演进为 CXL pooled rack memory，并显式建模 allocation、session affinity、DMA path、prefetch 和 failure domain；capacity tier 变成可寻址共享状态层。 它改变 `INFER-GPU-MEMORY` 下的 state/data/control contract，同时引入 metadata、校准/选择误差、额外执行或恢复责任；这些代价必须和收益在同一 workload 内计量。

**Evaluation contract。** Method：`https://arxiv.org/html/2607.18141v1#S3 :: exact-v1 method/theory/implementation evidence; https://arxiv.org/html/2607.18141v1#S4 :: exact-v1 method/theory/implementation evidence`；Evaluation：`https://arxiv.org/html/2607.18141v1#S5 :: exact-v1 evaluation/ablation/setup evidence; https://arxiv.org/html/2607.18141v1#S6 :: exact-v1 evaluation/ablation/setup evidence`；Limitations/Counterevidence：`https://arxiv.org/html/2607.18141v1#S8 :: exact-v1 limitations, counterevidence, reproducibility or implementation boundary; pooling 提高容量与复用，却增加 fabric latency、contention、ownership、security、failure blast radius 和 prefetch prediction；热 KV 仍应留 HBM。`。未披露字段保持 `Not Disclosed`；作者结果不跨模型、硬件、精度、长度、batch、concurrency、SLO 或 evaluator 外推。

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Evolution relation：`Layering / Dependency`。
- Stable owner：`INFER-GPU-MEMORY`。
- Books disposition：`No Change — Existing Coverage`。
<!-- review:SF-2026-ARXIV-2607-18141:end -->

<!-- review:SF-2026-ARXIV-2607-18171:start -->
#### FlashRT: Agent Harness for Guiding Agents to Deploy Real-Time Multimodal Applications

<!-- claim:SF-2026-ARXIV-2607-18171:start -->方法、正式分析、主/扩展实验支持 harness-guided deployment；不证明 IR 捕获所有 runtime semantics 或跨硬件迁移。 该结论只在论文公开的 workload 与 evaluation contract 内成立，不外推为通用生产结论。<!-- claim:SF-2026-ARXIV-2607-18171:end -->

**旧方案与约束变化。** `Ch81 已把 executable contract、IR/DAG、deterministic spine、agentic candidate、static/evaluator gate 与 rollback 串联；Ch49 拥有 kernel execution plan。`（`books/part-07-agent/81-workflow.md#L1`）旧方案在状态局部、规模较小或 SLO 宽松时继续成立；本 family 面对的新增压力由其 v1 problem statement 和 method 明确限定。

**机制、状态与代价。** 先把 reference application lowering 为包含 data dependency 与 persistent scope 的 IR，再让 agent 在 sequential interpreter、static analysis、correctness check 与 latency measurement 约束下提出 transformation；IR 和 verifier 拥有 contract，agent 只拥有候选修改。 它改变 `AGENT-WORKFLOW` 下的 state/data/control contract，同时引入 metadata、校准/选择误差、额外执行或恢复责任；这些代价必须和收益在同一 workload 内计量。

**Evaluation contract。** Method：`https://arxiv.org/html/2607.18171v1#S3 :: exact-v1 method/theory/implementation evidence; https://arxiv.org/html/2607.18171v1#S4 :: exact-v1 method/theory/implementation evidence`；Evaluation：`https://arxiv.org/html/2607.18171v1#S5 :: exact-v1 evaluation/ablation/setup evidence; https://arxiv.org/html/2607.18171v1#S8 :: exact-v1 evaluation/ablation/setup evidence`；Limitations/Counterevidence：`https://arxiv.org/html/2607.18171v1#S9 :: exact-v1 limitations, counterevidence, reproducibility or implementation boundary; IR 提升可验证性，却增加 frontend、semantic gap、measurement noise 和 benchmark overfit；低复杂度应用仍可用人工实现。`；本次 RP 重新绑定历史 full-read coverage：`papers/2026/weekly/2026-W30/README.md#L552-L561`，其中具名记录了 Method、Evaluation 与 Boundary。未披露字段保持 `Not Disclosed`；作者结果不跨模型、硬件、精度、长度、batch、concurrency、SLO 或 evaluator 外推。

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Evolution relation：`Layering / Dependency`。
- Stable owner：`AGENT-WORKFLOW`。
- Books disposition：`No Change — Existing Coverage`。
<!-- review:SF-2026-ARXIV-2607-18171:end -->

<!-- review:SF-2026-ARXIV-2607-18213:start -->
#### SWE-Pruner Pro: The Coder LLM Already Knows What to Prune

<!-- claim:SF-2026-ARXIV-2607-18213:start -->四项 benchmark、消融与实现附录支持论文模型/harness 下的 pruning；不证明跨模型、任意代码库或并发 serving 的安全性。 该结论只在论文公开的 workload 与 evaluation contract 内成立，不外推为通用生产结论。<!-- claim:SF-2026-ARXIV-2607-18213:end -->

**旧方案与约束变化。** `Ch75 已明确 goal-conditioned structured code pruning、hidden-state scorer、syntax/dependency preservation、reversible pointer 与 benchmark boundary，并列出该论文。`（`books/part-07-agent/75-context.md#L250`）旧方案在状态局部、规模较小或 SLO 宽松时继续成立；本 family 面对的新增压力由其 v1 problem statement 和 method 明确限定。

**机制、状态与代价。** 冻结 coder backbone，从其 hidden state 训练 goal/length-aware token scorer，在 serving 前执行结构感知 pruning；scorer 只是受 workload contract 约束的 context transformer，必须保留 source pointer 与 re-forward fallback。 它改变 `AGENT-CONTEXT` 下的 state/data/control contract，同时引入 metadata、校准/选择误差、额外执行或恢复责任；这些代价必须和收益在同一 workload 内计量。

**Evaluation contract。** Method：`https://arxiv.org/html/2607.18213v1#S3 :: exact-v1 method/theory/implementation evidence; https://arxiv.org/html/2607.18213v1#S4 :: exact-v1 method/theory/implementation evidence`；Evaluation：`https://arxiv.org/html/2607.18213v1#S5 :: exact-v1 evaluation/ablation/setup evidence; https://arxiv.org/html/2607.18213v1#Sx1 :: exact-v1 evaluation/ablation/setup evidence`；Limitations/Counterevidence：`https://arxiv.org/html/2607.18213v1#A5 :: exact-v1 limitations, counterevidence, reproducibility or implementation boundary; learned pruning 降低 token，却引入 scorer retraining、false prune、cache/re-forward 和 hidden-state coupling；高风险 edit 应回读原文。`；本次 RP 重新绑定历史 full-read coverage：`papers/2026/weekly/2026-W30/README.md#L533-L542`，其中具名记录了 Method、Evaluation 与 Boundary。未披露字段保持 `Not Disclosed`；作者结果不跨模型、硬件、精度、长度、batch、concurrency、SLO 或 evaluator 外推。

- Score V2：Design Delta 3 / System Reach 2 / Durability 3 = **8/9**。
- Evolution relation：`Layering / Dependency`。
- Stable owner：`AGENT-CONTEXT`。
- Books disposition：`No Change — Existing Coverage`。
<!-- review:SF-2026-ARXIV-2607-18213:end -->

<!-- review:SF-2026-ARXIV-2607-18231:start -->
#### FM-VLA: Force-based Memory for Vision-Language-Action Models in Contact-Rich Manipulation

<!-- claim:SF-2026-ARXIV-2607-18231:start -->方法、实验和 implementation details 支持所测机器人任务；不证明传感器漂移、跨 embodiment 或开放环境鲁棒性。 该结论只在论文公开的 workload 与 evaluation contract 内成立，不外推为通用生产结论。<!-- claim:SF-2026-ARXIV-2607-18231:end -->

**旧方案与约束变化。** `Ch26 已将 sensor/action schema、calibration、recurrent state、physical feedback、failure recovery 与 embodiment identity 作为闭环控制合同。`（`books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#L281`）旧方案在状态局部、规模较小或 SLO 宽松时继续成立；本 family 面对的新增压力由其 v1 problem statement 和 method 明确限定。

**机制、状态与代价。** 为 contact-rich manipulation 增加 force-conditioned short-horizon memory，使 policy 不只根据视觉位置，而能保存接触状态、力变化与失败恢复线索；force memory 是传感 state，不是事实 authority。 它改变 `MULTIMODAL-EMBODIED-VLA` 下的 state/data/control contract，同时引入 metadata、校准/选择误差、额外执行或恢复责任；这些代价必须和收益在同一 workload 内计量。

**Evaluation contract。** Method：`https://arxiv.org/html/2607.18231v1#S3 :: exact-v1 method/theory/implementation evidence; https://arxiv.org/html/2607.18231v1#S4 :: exact-v1 method/theory/implementation evidence`；Evaluation：`https://arxiv.org/html/2607.18231v1#S5 :: exact-v1 evaluation/ablation/setup evidence; https://arxiv.org/html/2607.18231v1#A5 :: exact-v1 evaluation/ablation/setup evidence`；Limitations/Counterevidence：`https://arxiv.org/html/2607.18231v1#A5 :: exact-v1 limitations, counterevidence, reproducibility or implementation boundary; force state 改善 partial observability，却引入 calibration、sensor failure、history drift 和 embodiment-specific schema；低接触任务不需此成本。`。未披露字段保持 `Not Disclosed`；作者结果不跨模型、硬件、精度、长度、batch、concurrency、SLO 或 evaluator 外推。

- Score V2：Design Delta 3 / System Reach 2 / Durability 3 = **8/9**。
- Evolution relation：`Layering / Dependency`。
- Stable owner：`MULTIMODAL-EMBODIED-VLA`。
- Books disposition：`No Change — Existing Coverage`。
<!-- review:SF-2026-ARXIV-2607-18231:end -->

<!-- review:SF-2026-ARXIV-2607-18603:start -->
#### AutoIndex: Learning Representation Programs for Retrieval

<!-- claim:SF-2026-ARXIV-2607-18603:start -->CRUMB tasks、实现与限制支持小规模 program search 的可行性；不证明开放 corpus、生产成本或全局最优。 该结论只在论文公开的 workload 与 evaluation contract 内成立，不外推为通用生产结论。<!-- claim:SF-2026-ARXIV-2607-18603:end -->

**旧方案与约束变化。** `Ch76 已把 ingestion/chunking/representation/index identity、validation-guided retrieval、versioning、evaluation 与 rollback 写成完整系统路线。`（`books/part-07-agent/76-rag.md#L35`）旧方案在状态局部、规模较小或 SLO 宽松时继续成立；本 family 面对的新增压力由其 v1 problem statement 和 method 明确限定。

**机制、状态与代价。** 把 indexing 从固定 chunking/embedding 参数推进为可执行 representation-program DSL；validation loop 诊断 retrieval failure、合成候选程序并在 frozen corpus/query contract 上选择，最终 index artifact 必须版本化 program 与 encoder。 它改变 `AGENT-RAG` 下的 state/data/control contract，同时引入 metadata、校准/选择误差、额外执行或恢复责任；这些代价必须和收益在同一 workload 内计量。

**Evaluation contract。** Method：`https://arxiv.org/html/2607.18603v1#S3 :: exact-v1 method/theory/implementation evidence; https://arxiv.org/html/2607.18603v1#S4 :: exact-v1 method/theory/implementation evidence`；Evaluation：`https://arxiv.org/html/2607.18603v1#S5 :: exact-v1 evaluation/ablation/setup evidence; https://arxiv.org/html/2607.18603v1#S6.SS4 :: exact-v1 evaluation/ablation/setup evidence`；Limitations/Counterevidence：`https://arxiv.org/html/2607.18603v1#A1.SS2 :: exact-v1 limitations, counterevidence, reproducibility or implementation boundary; program search 提升适配性，却增加 validation leakage、search cost、index rebuild、program drift 与解释复杂度；生产仍需 canary/rollback。`；本次 RP 重新绑定历史 full-read coverage：`papers/2026/weekly/2026-W30/README.md#L588-L596`，其中具名记录了 Method、Evaluation 与 Boundary。未披露字段保持 `Not Disclosed`；作者结果不跨模型、硬件、精度、长度、batch、concurrency、SLO 或 evaluator 外推。

- Score V2：Design Delta 3 / System Reach 2 / Durability 3 = **8/9**。
- Evolution relation：`Layering / Dependency`。
- Stable owner：`AGENT-RAG`。
- Books disposition：`No Change — Existing Coverage`。
<!-- review:SF-2026-ARXIV-2607-18603:end -->

## 4. Benchmark Contracts

以下只保存作者实验的适用合同，不把论文最大值外推为生产常数，也不跨模型、硬件或 workload 排名。

<!-- validator:benchmark-contract-v1 -->
| Source Family ID | Workload | Model | Hardware | Precision | Input Length | Output Length | Batch | Concurrency | SLO | Evaluator |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2607-17525 | multi-provider LLM gateway issue catalog plus two standalone failure reproductions | serving gateways/providers; no model-quality comparison | reproduction environment described in case studies; fleet hardware Not Disclosed | Paper-defined when disclosed; otherwise Not Disclosed. No cross-paper precision-normalized claim retained. | Bound to the paper task/context contract; aggregate input-length distribution Not Disclosed unless stated in exact v1. | Bound to the paper output/action-horizon contract; aggregate distribution Not Disclosed unless stated in exact v1. | Paper-defined when disclosed; otherwise Not Disclosed. | Paper-defined when disclosed; production arrival process Not Disclosed unless explicitly stated. | catalog coverage, detectability and reproduced failure behavior; no production rate/SLO | Authors; no independent replication is claimed. |
| SF-2026-ARXIV-2607-17545 | budgeted conversational/agent-memory retention and consolidation across the paper benchmark suite | paper LLM/operator combinations in Sx4; model internals Not Disclosed | training/evaluation hardware Not Disclosed | Paper-defined when disclosed; otherwise Not Disclosed. No cross-paper precision-normalized claim retained. | Bound to the paper task/context contract; aggregate input-length distribution Not Disclosed unless stated in exact v1. | Bound to the paper output/action-horizon contract; aggregate distribution Not Disclosed unless stated in exact v1. | Paper-defined when disclosed; otherwise Not Disclosed. | Paper-defined when disclosed; production arrival process Not Disclosed unless explicitly stated. | answer utility under memory budget and router risk threshold; no production latency SLO | Authors; no independent replication is claimed. |
| SF-2026-ARXIV-2607-17621 | agent-memory refinement tasks, attribution diagnostics and ablations | frozen base LLM plus learned refinement/guidance components | compute disclosure in A7; exact serving topology Not Disclosed | Paper-defined when disclosed; otherwise Not Disclosed. No cross-paper precision-normalized claim retained. | Bound to the paper task/context contract; aggregate input-length distribution Not Disclosed unless stated in exact v1. | Bound to the paper output/action-horizon contract; aggregate distribution Not Disclosed unless stated in exact v1. | Paper-defined when disclosed; otherwise Not Disclosed. | Paper-defined when disclosed; production arrival process Not Disclosed unless explicitly stated. | task outcome and refinement quality under author harness; no causal-attribution guarantee | Authors; no independent replication is claimed. |
| SF-2026-ARXIV-2607-17715 | compressed prefix-KV storage, reconstruction/composition and end-to-end timing | paper long-context LLMs and C2KV implementation | paper setup in A2/A3; cross-hardware portability Not Disclosed | Paper-defined when disclosed; otherwise Not Disclosed. No cross-paper precision-normalized claim retained. | Bound to the paper task/context contract; aggregate input-length distribution Not Disclosed unless stated in exact v1. | Bound to the paper output/action-horizon contract; aggregate distribution Not Disclosed unless stated in exact v1. | Paper-defined when disclosed; otherwise Not Disclosed. | Paper-defined when disclosed; production arrival process Not Disclosed unless explicitly stated. | quality, memory footprint and timing under disclosed setup; no multi-tenant tail SLO | Authors; no independent replication is claimed. |
| SF-2026-ARXIV-2607-17733 | mixed-precision post-training quantization across paper LLM/task suite | paper LLM baselines and MXSens precision assignments | GPU/platform in S6; unsupported backends Not Evaluated | Paper-defined when disclosed; otherwise Not Disclosed. No cross-paper precision-normalized claim retained. | Bound to the paper task/context contract; aggregate input-length distribution Not Disclosed unless stated in exact v1. | Bound to the paper output/action-horizon contract; aggregate distribution Not Disclosed unless stated in exact v1. | Paper-defined when disclosed; otherwise Not Disclosed. | Paper-defined when disclosed; production arrival process Not Disclosed unless explicitly stated. | quality/size/runtime under author implementation; no general fractional-bit speedup | Authors; no independent replication is claimed. |
| SF-2026-ARXIV-2607-17747 | simulated and open mobile-network control with learned dynamics | world-model controller and paper network-control baselines | network test/simulation setup in S5/S6; accelerator precision Not Disclosed | Paper-defined when disclosed; otherwise Not Disclosed. No cross-paper precision-normalized claim retained. | Bound to the paper task/context contract; aggregate input-length distribution Not Disclosed unless stated in exact v1. | Bound to the paper output/action-horizon contract; aggregate distribution Not Disclosed unless stated in exact v1. | Paper-defined when disclosed; otherwise Not Disclosed. | Paper-defined when disclosed; production arrival process Not Disclosed unless explicitly stated. | control reward/constraint behavior under tested networks; no production carrier SLO | Authors; no independent replication is claimed. |
| SF-2026-ARXIV-2607-17751 | large-catalog agent tool selection, decomposition/reranking ablations | paper selector/retriever LLMs and baselines | hardware, precision and online concurrency Not Disclosed | Paper-defined when disclosed; otherwise Not Disclosed. No cross-paper precision-normalized claim retained. | Bound to the paper task/context contract; aggregate input-length distribution Not Disclosed unless stated in exact v1. | Bound to the paper output/action-horizon contract; aggregate distribution Not Disclosed unless stated in exact v1. | Paper-defined when disclosed; otherwise Not Disclosed. | Paper-defined when disclosed; production arrival process Not Disclosed unless explicitly stated. | tool recall/selection quality and stage cost; no side-effect execution SLO | Authors; no independent replication is claimed. |
| SF-2026-ARXIV-2607-17786 | VLA attacks across perception/reasoning/action stages plus defense study | paper VLA architectures and reasoning variants | robot/simulation setup in S3; deployment hardware Not Disclosed | Paper-defined when disclosed; otherwise Not Disclosed. No cross-paper precision-normalized claim retained. | Bound to the paper task/context contract; aggregate input-length distribution Not Disclosed unless stated in exact v1. | Bound to the paper output/action-horizon contract; aggregate distribution Not Disclosed unless stated in exact v1. | Paper-defined when disclosed; otherwise Not Disclosed. | Paper-defined when disclosed; production arrival process Not Disclosed unless explicitly stated. | robustness under defined attacks; no open-world or physical safety certificate | Authors; no independent replication is claimed. |
| SF-2026-ARXIV-2607-17914 | multi-agent reinforcement-learning coordination under controlled communication loss | paper MARL policies/predictor baselines | simulation hardware and online message concurrency Not Disclosed | Paper-defined when disclosed; otherwise Not Disclosed. No cross-paper precision-normalized claim retained. | Bound to the paper task/context contract; aggregate input-length distribution Not Disclosed unless stated in exact v1. | Bound to the paper output/action-horizon contract; aggregate distribution Not Disclosed unless stated in exact v1. | Paper-defined when disclosed; otherwise Not Disclosed. | Paper-defined when disclosed; production arrival process Not Disclosed unless explicitly stated. | return/coordination robustness versus loss pattern; no LLM-agent generalization | Authors; no independent replication is claimed. |
| SF-2026-ARXIV-2607-17973 | latent world-model planning with subgoal-conditioned action generation | paper world model, planner and baseline policies | training/evaluation hardware Not Disclosed | Paper-defined when disclosed; otherwise Not Disclosed. No cross-paper precision-normalized claim retained. | Bound to the paper task/context contract; aggregate input-length distribution Not Disclosed unless stated in exact v1. | Bound to the paper output/action-horizon contract; aggregate distribution Not Disclosed unless stated in exact v1. | Paper-defined when disclosed; otherwise Not Disclosed. | Paper-defined when disclosed; production arrival process Not Disclosed unless explicitly stated. | task return/planning quality over paper horizon; no real-environment safety SLO | Authors; no independent replication is claimed. |
| SF-2026-ARXIV-2607-17979 | FlashInfer contest kernel tasks: fused MoE, gated delta net and sparse attention | LLM coding agents plus executable kernel harness/reference programs | contest GPU/compiler contracts in S4/A3-A9; other architectures Not Evaluated | Paper-defined when disclosed; otherwise Not Disclosed. No cross-paper precision-normalized claim retained. | Bound to the paper task/context contract; aggregate input-length distribution Not Disclosed unless stated in exact v1. | Bound to the paper output/action-horizon contract; aggregate distribution Not Disclosed unless stated in exact v1. | Paper-defined when disclosed; otherwise Not Disclosed. | Paper-defined when disclosed; production arrival process Not Disclosed unless explicitly stated. | correctness admission and measured kernel performance per task/shape; no portable fleet SLO | Authors; no independent replication is claimed. |
| SF-2026-ARXIV-2607-17986 | 23-cell self-state attack/defense matrix spanning 43 state operations | self-hosted agent workloads and OS/application defenses; no model leaderboard | OS/workload setup in A6; production tenant scale Not Disclosed | Paper-defined when disclosed; otherwise Not Disclosed. No cross-paper precision-normalized claim retained. | Bound to the paper task/context contract; aggregate input-length distribution Not Disclosed unless stated in exact v1. | Bound to the paper output/action-horizon contract; aggregate distribution Not Disclosed unless stated in exact v1. | Paper-defined when disclosed; otherwise Not Disclosed. | Paper-defined when disclosed; production arrival process Not Disclosed unless explicitly stated. | attack feasibility/detectability/recovery by cell; no completeness or calibrated detector claim | Authors; no independent replication is claimed. |
| SF-2026-ARXIV-2607-18016 | humanoid loco-manipulation with persistent 3D object-token state | paper humanoid VLA/object-token variants | robot/simulation setup in S4/A1; production control hardware Not Disclosed | Paper-defined when disclosed; otherwise Not Disclosed. No cross-paper precision-normalized claim retained. | Bound to the paper task/context contract; aggregate input-length distribution Not Disclosed unless stated in exact v1. | Bound to the paper output/action-horizon contract; aggregate distribution Not Disclosed unless stated in exact v1. | Paper-defined when disclosed; otherwise Not Disclosed. | Paper-defined when disclosed; production arrival process Not Disclosed unless explicitly stated. | task success and verification under tested scenarios; no open-world identity guarantee | Authors; no independent replication is claimed. |
| SF-2026-ARXIV-2607-18110 | non-verifiable experiential-learning tasks with held-out/OOD evaluation | student LLM, coach LLM and paper baselines | training hardware/precision Not Disclosed | Paper-defined when disclosed; otherwise Not Disclosed. No cross-paper precision-normalized claim retained. | Bound to the paper task/context contract; aggregate input-length distribution Not Disclosed unless stated in exact v1. | Bound to the paper output/action-horizon contract; aggregate distribution Not Disclosed unless stated in exact v1. | Paper-defined when disclosed; otherwise Not Disclosed. | Paper-defined when disclosed; production arrival process Not Disclosed unless explicitly stated. | author task/rubric outcome and ablation metrics; no unbiased-coach guarantee | Authors; no independent replication is claimed. |
| SF-2026-ARXIV-2607-18141 | multi-turn LLM serving with session/KV placement in a CXL memory-rack architecture | paper serving stack and multi-turn workload/model configurations | CXL/rack and host/GPU configuration in S5; other fabrics Not Evaluated | Paper-defined when disclosed; otherwise Not Disclosed. No cross-paper precision-normalized claim retained. | Bound to the paper task/context contract; aggregate input-length distribution Not Disclosed unless stated in exact v1. | Bound to the paper output/action-horizon contract; aggregate distribution Not Disclosed unless stated in exact v1. | Paper-defined when disclosed; otherwise Not Disclosed. | Paper-defined when disclosed; production arrival process Not Disclosed unless explicitly stated. | throughput/latency/capacity under author setup; no general production tail SLO | Authors; no independent replication is claimed. |
| SF-2026-ARXIV-2607-18171 | real-time multimodal application deployment transformations under FlashRT harness | coding agents, sequential interpreter and reference applications | paper deployment targets in S5/S9; other compiler/hardware stacks Not Evaluated | Paper-defined when disclosed; otherwise Not Disclosed. No cross-paper precision-normalized claim retained. | Bound to the paper task/context contract; aggregate input-length distribution Not Disclosed unless stated in exact v1. | Bound to the paper output/action-horizon contract; aggregate distribution Not Disclosed unless stated in exact v1. | Paper-defined when disclosed; otherwise Not Disclosed. | Paper-defined when disclosed; production arrival process Not Disclosed unless explicitly stated. | correctness plus latency under declared application contract; no universal IR equivalence | Authors; no independent replication is claimed. |
| SF-2026-ARXIV-2607-18213 | four software-engineering context-pruning benchmarks and component ablations | frozen coder LLM plus length-aware hidden-state scorer | training/serving setup in A2/A5; fleet concurrency Not Disclosed | Paper-defined when disclosed; otherwise Not Disclosed. No cross-paper precision-normalized claim retained. | Bound to the paper task/context contract; aggregate input-length distribution Not Disclosed unless stated in exact v1. | Bound to the paper output/action-horizon contract; aggregate distribution Not Disclosed unless stated in exact v1. | Paper-defined when disclosed; otherwise Not Disclosed. | Paper-defined when disclosed; production arrival process Not Disclosed unless explicitly stated. | task outcome and context reduction under author harness; no arbitrary-code preservation guarantee | Authors; no independent replication is claimed. |
| SF-2026-ARXIV-2607-18231 | contact-rich manipulation tasks using force-conditioned memory | paper VLA and FM-VLA policy variants | robot/sensor implementation in A5; cross-embodiment hardware Not Evaluated | Paper-defined when disclosed; otherwise Not Disclosed. No cross-paper precision-normalized claim retained. | Bound to the paper task/context contract; aggregate input-length distribution Not Disclosed unless stated in exact v1. | Bound to the paper output/action-horizon contract; aggregate distribution Not Disclosed unless stated in exact v1. | Paper-defined when disclosed; otherwise Not Disclosed. | Paper-defined when disclosed; production arrival process Not Disclosed unless explicitly stated. | manipulation outcome under tested contact tasks; no sensor-failure safety SLO | Authors; no independent replication is claimed. |
| SF-2026-ARXIV-2607-18603 | CRUMB eight-task retrieval suite with validation-guided representation-program search | BM25/retrieval programs and paper synthesis/selection components | implementation in A1.SS2; production index cluster Not Disclosed | Paper-defined when disclosed; otherwise Not Disclosed. No cross-paper precision-normalized claim retained. | Bound to the paper task/context contract; aggregate input-length distribution Not Disclosed unless stated in exact v1. | Bound to the paper output/action-horizon contract; aggregate distribution Not Disclosed unless stated in exact v1. | Paper-defined when disclosed; otherwise Not Disclosed. | Paper-defined when disclosed; production arrival process Not Disclosed unless explicitly stated. | retrieval quality/search budget on fixed corpus/tasks; no global optimality or online SLO | Authors; no independent replication is claimed. |

## 5. Deep Analysis Selection

<!-- validator:deep-analysis-selection-v1 -->
| Source Family ID | Eligibility | Decision | Analysis Unit ID | Subsumed By | Priority Rationale | Narrative Ref |
| --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2607-17525 | score_7_9;potential_books_delta | selected | AU-20260721-260717525 | — | V2=8/9；正文给出 taxonomy construction、纳入标准、两项完全刻画案例与完整 catalog；它支持结构化 failure schema 的可用性，不证明 catalog 完备，也不证明任一 gateway 的生产发生率。；相对同日候选提供独立 owner 的最大可定位 delta | analysis:AU-20260721-260717525 |
| SF-2026-ARXIV-2607-17545 | score_7_9;potential_books_delta | not_selected | — | — | 本 family 的独立增量为“作者在多预算、跨模型实验中观察到 retain/consolidate crossover，并报告 learned router 的选择结果；证据仍受 benchmark、operator set、label generator 与预算定义约束。”；V2=3/2/3。它与入选 `SF-2026-ARXIV-2607-17525` 属于不同 owner；本日三项长叙事配额按 V2 总分、长期 Books delta 与跨层影响排序。因此本项保留独立 Source Review 与 Books Decision，但不进入本日最多三项的长叙事；这不是被其他 family 覆盖，也不改变其 Evidence 完成状态。 | analysis-decision:SF-2026-ARXIV-2607-17545 |
| SF-2026-ARXIV-2607-17621 | score_7_9;potential_books_delta | not_selected | — | — | 本 family 的独立增量为“Method、algorithm、实验、计算开销和附录共同支持 attribution-guided refinement 在论文任务中的差异；attention signal 不是因果真值，也未证明跨模型 calibration。”；V2=3/2/3。它与入选 `SF-2026-ARXIV-2607-17525` 属于不同 owner；本日三项长叙事配额按 V2 总分、长期 Books delta 与跨层影响排序。因此本项保留独立 Source Review 与 Books Decision，但不进入本日最多三项的长叙事；这不是被其他 family 覆盖，也不改变其 Evidence 完成状态。 | analysis-decision:SF-2026-ARXIV-2607-17621 |
| SF-2026-ARXIV-2607-17715 | score_7_9;potential_books_delta | selected | AU-20260721-260717715 | — | V2=9/9；Method、evaluation、timing 和 limitations 展示所测模型与 workload 中 compression+composition 的可行性；没有证明任意 attention 架构、任意位置变换或多租户并发下等价。；相对同日候选提供独立 owner 的最大可定位 delta | analysis:AU-20260721-260717715 |
| SF-2026-ARXIV-2607-17733 | score_7_9;potential_books_delta | not_selected | — | — | 本 family 的独立增量为“作者给出算法、硬件实验和 reproducibility 信息；结果绑定所测模型、GPU、kernel 与 calibration，不证明任意 backend 都可兑现同样的 physical packing。”；V2=3/2/3。它与入选 `SF-2026-ARXIV-2607-17525` 属于不同 owner；本日三项长叙事配额按 V2 总分、长期 Books delta 与跨层影响排序。因此本项保留独立 Source Review 与 Books Decision，但不进入本日最多三项的长叙事；这不是被其他 family 覆盖，也不改变其 Evidence 完成状态。 | analysis-decision:SF-2026-ARXIV-2607-17733 |
| SF-2026-ARXIV-2607-17751 | score_7_9;potential_books_delta | not_selected | — | — | 本 family 的独立增量为“作者在论文 tool-selection benchmark 上比较组件与消融；结论受 catalog、query decomposition、base model 和 evaluator 约束。”；V2=3/2/3。它与入选 `SF-2026-ARXIV-2607-17525` 属于不同 owner；本日三项长叙事配额按 V2 总分、长期 Books delta 与跨层影响排序。因此本项保留独立 Source Review 与 Books Decision，但不进入本日最多三项的长叙事；这不是被其他 family 覆盖，也不改变其 Evidence 完成状态。 | analysis-decision:SF-2026-ARXIV-2607-17751 |
| SF-2026-ARXIV-2607-17786 | score_7_9;potential_books_delta | not_selected | — | — | 本 family 的独立增量为“攻击设置、跨阶段实验与 defense study 支持“reasoning 可同时增益与放大脆弱性”；不证明开放世界攻击覆盖或真实机器人安全。”；V2=3/3/3。它与入选 `SF-2026-ARXIV-2607-17715` 属于不同 owner；本日三项长叙事配额按 V2 总分、长期 Books delta 与跨层影响排序。因此本项保留独立 Source Review 与 Books Decision，但不进入本日最多三项的长叙事；这不是被其他 family 覆盖，也不改变其 Evidence 完成状态。 | analysis-decision:SF-2026-ARXIV-2607-17786 |
| SF-2026-ARXIV-2607-17973 | score_7_9;potential_books_delta | not_selected | — | — | 本 family 的独立增量为“作者实验和 capacity analysis 支持该 latent planning factorization 在所测环境中的收益；未证明 latent subgoal 可解释、可校准或迁移到真实环境。”；V2=3/2/3。它与入选 `SF-2026-ARXIV-2607-17525` 属于不同 owner；本日三项长叙事配额按 V2 总分、长期 Books delta 与跨层影响排序。因此本项保留独立 Source Review 与 Books Decision，但不进入本日最多三项的长叙事；这不是被其他 family 覆盖，也不改变其 Evidence 完成状态。 | analysis-decision:SF-2026-ARXIV-2607-17973 |
| SF-2026-ARXIV-2607-17979 | score_7_9;potential_books_delta | not_selected | — | — | 本 family 的独立增量为“系统、workflow、kernel case studies 与 limitations 支持 harness 对 agent search 的影响；结果绑定 contest problems、hardware/compiler 与 evaluator。”；V2=3/3/3。它与入选 `SF-2026-ARXIV-2607-17715` 属于不同 owner；本日三项长叙事配额按 V2 总分、长期 Books delta 与跨层影响排序。因此本项保留独立 Source Review 与 Books Decision，但不进入本日最多三项的长叙事；这不是被其他 family 覆盖，也不改变其 Evidence 完成状态。 | analysis-decision:SF-2026-ARXIV-2607-17979 |
| SF-2026-ARXIV-2607-17986 | score_7_9;forced_review;potential_books_delta | selected | AU-20260721-260717986 | — | 命中合同第一优先级 security contract；V2=9/9；论文报告 23-cell/43-operation attack-defense matrix 与不可由 OS 区分的操作；这证明 OS 缺少 agent intent，而非证明其 catalog 完备或 detector 在生产校准。；相对同日候选提供独立 owner 的最大可定位 delta | analysis:AU-20260721-260717986 |
| SF-2026-ARXIV-2607-18016 | score_7_9;potential_books_delta | not_selected | — | — | 本 family 的独立增量为“方法与评估支持论文 humanoid tasks 中的闭环状态追踪；不证明开放世界 data association、真实硬件故障或长期 identity consistency。”；V2=3/3/2。它与入选 `SF-2026-ARXIV-2607-17525` 属于不同 owner；本日三项长叙事配额按 V2 总分、长期 Books delta 与跨层影响排序。因此本项保留独立 Source Review 与 Books Decision，但不进入本日最多三项的长叙事；这不是被其他 family 覆盖，也不改变其 Evidence 完成状态。 | analysis-decision:SF-2026-ARXIV-2607-18016 |
| SF-2026-ARXIV-2607-18110 | score_7_9;potential_books_delta | not_selected | — | — | 本 family 的独立增量为“作者在 held-out/OOD 与 ablation 下比较 coaching；只支持所测 task、coach/student 与 evaluator，不证明自然语言诊断无偏。”；V2=3/2/3。它与入选 `SF-2026-ARXIV-2607-17525` 属于不同 owner；本日三项长叙事配额按 V2 总分、长期 Books delta 与跨层影响排序。因此本项保留独立 Source Review 与 Books Decision，但不进入本日最多三项的长叙事；这不是被其他 family 覆盖，也不改变其 Evidence 完成状态。 | analysis-decision:SF-2026-ARXIV-2607-18110 |
| SF-2026-ARXIV-2607-18141 | score_7_9;potential_books_delta | not_selected | — | — | 本 family 的独立增量为“characterization、system design、setup 与 evaluation 支持论文 hardware/workload 下的可行性；不证明不同 CXL topology、生产多租户隔离或 tail SLO。”；V2=3/3/3。它与入选 `SF-2026-ARXIV-2607-17715` 属于不同 owner；本日三项长叙事配额按 V2 总分、长期 Books delta 与跨层影响排序。因此本项保留独立 Source Review 与 Books Decision，但不进入本日最多三项的长叙事；这不是被其他 family 覆盖，也不改变其 Evidence 完成状态。 | analysis-decision:SF-2026-ARXIV-2607-18141 |
| SF-2026-ARXIV-2607-18171 | score_7_9;potential_books_delta | not_selected | — | — | 本 family 的独立增量为“方法、正式分析、主/扩展实验支持 harness-guided deployment；不证明 IR 捕获所有 runtime semantics 或跨硬件迁移。”；V2=3/3/3。它与入选 `SF-2026-ARXIV-2607-17715` 属于不同 owner；本日三项长叙事配额按 V2 总分、长期 Books delta 与跨层影响排序。因此本项保留独立 Source Review 与 Books Decision，但不进入本日最多三项的长叙事；这不是被其他 family 覆盖，也不改变其 Evidence 完成状态。 | analysis-decision:SF-2026-ARXIV-2607-18171 |
| SF-2026-ARXIV-2607-18213 | score_7_9;potential_books_delta | not_selected | — | — | 本 family 的独立增量为“四项 benchmark、消融与实现附录支持论文模型/harness 下的 pruning；不证明跨模型、任意代码库或并发 serving 的安全性。”；V2=3/2/3。它与入选 `SF-2026-ARXIV-2607-17525` 属于不同 owner；本日三项长叙事配额按 V2 总分、长期 Books delta 与跨层影响排序。因此本项保留独立 Source Review 与 Books Decision，但不进入本日最多三项的长叙事；这不是被其他 family 覆盖，也不改变其 Evidence 完成状态。 | analysis-decision:SF-2026-ARXIV-2607-18213 |
| SF-2026-ARXIV-2607-18231 | score_7_9;potential_books_delta | not_selected | — | — | 本 family 的独立增量为“方法、实验和 implementation details 支持所测机器人任务；不证明传感器漂移、跨 embodiment 或开放环境鲁棒性。”；V2=3/2/3。它与入选 `SF-2026-ARXIV-2607-17525` 属于不同 owner；本日三项长叙事配额按 V2 总分、长期 Books delta 与跨层影响排序。因此本项保留独立 Source Review 与 Books Decision，但不进入本日最多三项的长叙事；这不是被其他 family 覆盖，也不改变其 Evidence 完成状态。 | analysis-decision:SF-2026-ARXIV-2607-18231 |
| SF-2026-ARXIV-2607-18603 | score_7_9;potential_books_delta | not_selected | — | — | 本 family 的独立增量为“CRUMB tasks、实现与限制支持小规模 program search 的可行性；不证明开放 corpus、生产成本或全局最优。”；V2=3/2/3。它与入选 `SF-2026-ARXIV-2607-17525` 属于不同 owner；本日三项长叙事配额按 V2 总分、长期 Books delta 与跨层影响排序。因此本项保留独立 Source Review 与 Books Decision，但不进入本日最多三项的长叙事；这不是被其他 family 覆盖，也不改变其 Evidence 完成状态。 | analysis-decision:SF-2026-ARXIV-2607-18603 |

<!-- analysis:AU-20260721-260717525:start -->
### FailureAtlas: A Taxonomy of Failure Modes in Multi-Provider LLM Serving Infrastructure

**旧方案为何合理。** 只按 HTTP status、timeout、OOM 聚合 Errors，在协议和进程失败主导时合理，但会漏掉返回 200、流仍结束、语义或 session continuity 已损坏的 silent failure。（现有命题定位：`books/part-06-ai-infrastructure/67-monitoring.md#L1`）

**约束变化与机制。** 把多 provider serving 的 failure 以 origin layer 与 detectability 两轴建模，再由 issue evidence、独立复现与完整 case study 连接现象、根因、检测信号和恢复动作。关键 delta 不是新增错误名单，而是把 runtime_success 与 semantic/continuity failure 分开。 这条证据与现有主线的关系是 `Direct Evolution`：它改变或补充 `PLATFORM-MONITORING` 下的 representation、state、data flow 或 control ownership，而不是用论文名称替换设计结论。

**收益、代价与下一重压力。** 结构化 failure schema 增加跨层 correlation、标签治理和复现成本；未知 failure 仍需 trace 与人工调查，taxonomy 不能替代 SLO、canary 或 fault injection。

<!-- analysis:AU-20260721-260717525:end -->

<!-- analysis:AU-20260721-260717715:start -->
### C^2KV: Compressed and Composable KV Cache Reuse for Efficient LLM Inference

**旧方案为何合理。** 完整 prefix KV 复用在固定 model revision、相同 position 与足够 HBM 时最可靠；单独压缩只解决容量，单独拼接只解决重复 prefill。（现有命题定位：`books/part-05-inference-system/45-why-kv-cache-speeds-up.md#L584`）

**约束变化与机制。** 把 prefix KV 由完整 tensor 演进为可压缩、可组合的 cache object：压缩表示必须保留 position/model/policy identity，组合路径还需显式处理 segment seam 与 reconstruction error，而不能把 byte compatibility 当作 semantic composability。 这条证据与现有主线的关系是 `Layering / Dependency`：它改变或补充 `INFER-KV-CACHE` 下的 representation、state、data flow 或 control ownership，而不是用论文名称替换设计结论。

**收益、代价与下一重压力。** 组合压缩减少存储与 prefill，却引入重建 kernel、seam error、policy identity、fallback 和 tail-latency 风险；正确性优先时仍应 full KV 或 recompute。

<!-- analysis:AU-20260721-260717715:end -->

<!-- analysis:AU-20260721-260717986:start -->
### Self-State Attacks on Self-Hosted AI Agents: How Far Can OS Defenses Go?

**旧方案为何合理。** 传统文件权限在状态 owner 和合法写入集合稳定时合理；Agent 本身需要更新 memory/config 时，恶意自写与合法自写共享 syscall surface。（现有命题定位：`books/part-06-ai-infrastructure/72-security.md#L1`）

**约束变化与机制。** 把 agent self-state 分成 instruction、config、memory 等可变层，系统枚举 write primitive、attack path、OS control 与 recovery；静态 ACL 只能保护稳定层，动态 memory 需要 workload-conditioned detection，备份只提供恢复而非 prevention。 这条证据与现有主线的关系是 `Layering / Dependency`：它改变或补充 `PLATFORM-SECURITY` 下的 representation、state、data flow 或 control ownership，而不是用论文名称替换设计结论。

**收益、代价与下一重压力。** 检测与备份增加 false positive、rollback、sensitive snapshot 和恢复一致性成本；低变更层继续使用静态 protection，高风险更新需 application-level verifier。

<!-- analysis:AU-20260721-260717986:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-17545:start -->《Retain or Consolidate? Budget-Dependent Operator Selection for Language Agent Memory》已完成 Deep Source Review。本 family 的独立增量为“作者在多预算、跨模型实验中观察到 retain/consolidate crossover，并报告 learned router 的选择结果；证据仍受 benchmark、operator set、label generator 与预算定义约束。”；V2=3/2/3。它与入选 `SF-2026-ARXIV-2607-17525` 属于不同 owner；本日三项长叙事配额按 V2 总分、长期 Books delta 与跨层影响排序。因此本项保留独立 Source Review 与 Books Decision，但不进入本日最多三项的长叙事；这不是被其他 family 覆盖，也不改变其 Evidence 完成状态。<!-- analysis-decision:SF-2026-ARXIV-2607-17545:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-17621:start -->《Mechanistic Attention Guidance for Agent Memory Refinement》已完成 Deep Source Review。本 family 的独立增量为“Method、algorithm、实验、计算开销和附录共同支持 attribution-guided refinement 在论文任务中的差异；attention signal 不是因果真值，也未证明跨模型 calibration。”；V2=3/2/3。它与入选 `SF-2026-ARXIV-2607-17525` 属于不同 owner；本日三项长叙事配额按 V2 总分、长期 Books delta 与跨层影响排序。因此本项保留独立 Source Review 与 Books Decision，但不进入本日最多三项的长叙事；这不是被其他 family 覆盖，也不改变其 Evidence 完成状态。<!-- analysis-decision:SF-2026-ARXIV-2607-17621:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-17733:start -->《MXSens: Sensitivity-Aware Mixed-Precision Quantization for Efficient LLM Inference》已完成 Deep Source Review。本 family 的独立增量为“作者给出算法、硬件实验和 reproducibility 信息；结果绑定所测模型、GPU、kernel 与 calibration，不证明任意 backend 都可兑现同样的 physical packing。”；V2=3/2/3。它与入选 `SF-2026-ARXIV-2607-17525` 属于不同 owner；本日三项长叙事配额按 V2 总分、长期 Books delta 与跨层影响排序。因此本项保留独立 Source Review 与 Books Decision，但不进入本日最多三项的长叙事；这不是被其他 family 覆盖，也不改变其 Evidence 完成状态。<!-- analysis-decision:SF-2026-ARXIV-2607-17733:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-17751:start -->《MagicSelector: Joint Optimization for Agent Tool Selection via Counterfactual Decomposition and Progressive Reranking》已完成 Deep Source Review。本 family 的独立增量为“作者在论文 tool-selection benchmark 上比较组件与消融；结论受 catalog、query decomposition、base model 和 evaluator 约束。”；V2=3/2/3。它与入选 `SF-2026-ARXIV-2607-17525` 属于不同 owner；本日三项长叙事配额按 V2 总分、长期 Books delta 与跨层影响排序。因此本项保留独立 Source Review 与 Books Decision，但不进入本日最多三项的长叙事；这不是被其他 family 覆盖，也不改变其 Evidence 完成状态。<!-- analysis-decision:SF-2026-ARXIV-2607-17751:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-17786:start -->《Reasoning as a Double-Edged Sword: Architecture and Cross-Stage Robustness in Vision-Language-Action Models》已完成 Deep Source Review。本 family 的独立增量为“攻击设置、跨阶段实验与 defense study 支持“reasoning 可同时增益与放大脆弱性”；不证明开放世界攻击覆盖或真实机器人安全。”；V2=3/3/3。它与入选 `SF-2026-ARXIV-2607-17715` 属于不同 owner；本日三项长叙事配额按 V2 总分、长期 Books delta 与跨层影响排序。因此本项保留独立 Source Review 与 Books Decision，但不进入本日最多三项的长叙事；这不是被其他 family 覆盖，也不改变其 Evidence 完成状态。<!-- analysis-decision:SF-2026-ARXIV-2607-17786:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-17973:start -->《SAGE: Subgoal-Conditioned Action Generation for Latent World Model Planning》已完成 Deep Source Review。本 family 的独立增量为“作者实验和 capacity analysis 支持该 latent planning factorization 在所测环境中的收益；未证明 latent subgoal 可解释、可校准或迁移到真实环境。”；V2=3/2/3。它与入选 `SF-2026-ARXIV-2607-17525` 属于不同 owner；本日三项长叙事配额按 V2 总分、长期 Books delta 与跨层影响排序。因此本项保留独立 Source Review 与 Books Decision，但不进入本日最多三项的长叙事；这不是被其他 family 覆盖，也不改变其 Evidence 完成状态。<!-- analysis-decision:SF-2026-ARXIV-2607-17973:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-17979:start -->《Harness Engineering for LLM-Driven GPU Kernel Generation》已完成 Deep Source Review。本 family 的独立增量为“系统、workflow、kernel case studies 与 limitations 支持 harness 对 agent search 的影响；结果绑定 contest problems、hardware/compiler 与 evaluator。”；V2=3/3/3。它与入选 `SF-2026-ARXIV-2607-17715` 属于不同 owner；本日三项长叙事配额按 V2 总分、长期 Books delta 与跨层影响排序。因此本项保留独立 Source Review 与 Books Decision，但不进入本日最多三项的长叙事；这不是被其他 family 覆盖，也不改变其 Evidence 完成状态。<!-- analysis-decision:SF-2026-ARXIV-2607-17979:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-18016:start -->《Closing the Loop in Humanoid VLA: Persistent 3D Object Tokens for Verifiable Loco-Manipulation》已完成 Deep Source Review。本 family 的独立增量为“方法与评估支持论文 humanoid tasks 中的闭环状态追踪；不证明开放世界 data association、真实硬件故障或长期 identity consistency。”；V2=3/3/2。它与入选 `SF-2026-ARXIV-2607-17525` 属于不同 owner；本日三项长叙事配额按 V2 总分、长期 Books delta 与跨层影响排序。因此本项保留独立 Source Review 与 Books Decision，但不进入本日最多三项的长叙事；这不是被其他 family 覆盖，也不改变其 Evidence 完成状态。<!-- analysis-decision:SF-2026-ARXIV-2607-18016:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-18110:start -->《LLM-as-a-Coach: Experiential Learning for Non-Verifiable Tasks》已完成 Deep Source Review。本 family 的独立增量为“作者在 held-out/OOD 与 ablation 下比较 coaching；只支持所测 task、coach/student 与 evaluator，不证明自然语言诊断无偏。”；V2=3/2/3。它与入选 `SF-2026-ARXIV-2607-17525` 属于不同 owner；本日三项长叙事配额按 V2 总分、长期 Books delta 与跨层影响排序。因此本项保留独立 Source Review 与 Books Decision，但不进入本日最多三项的长叙事；这不是被其他 family 覆盖，也不改变其 Evidence 完成状态。<!-- analysis-decision:SF-2026-ARXIV-2607-18110:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-18141:start -->《HyMCache: A KV Cache Framework for Multi-Turn LLM Serving with CXL-Hybrid Memory》已完成 Deep Source Review。本 family 的独立增量为“characterization、system design、setup 与 evaluation 支持论文 hardware/workload 下的可行性；不证明不同 CXL topology、生产多租户隔离或 tail SLO。”；V2=3/3/3。它与入选 `SF-2026-ARXIV-2607-17715` 属于不同 owner；本日三项长叙事配额按 V2 总分、长期 Books delta 与跨层影响排序。因此本项保留独立 Source Review 与 Books Decision，但不进入本日最多三项的长叙事；这不是被其他 family 覆盖，也不改变其 Evidence 完成状态。<!-- analysis-decision:SF-2026-ARXIV-2607-18141:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-18171:start -->《FlashRT: Agent Harness for Guiding Agents to Deploy Real-Time Multimodal Applications》已完成 Deep Source Review。本 family 的独立增量为“方法、正式分析、主/扩展实验支持 harness-guided deployment；不证明 IR 捕获所有 runtime semantics 或跨硬件迁移。”；V2=3/3/3。它与入选 `SF-2026-ARXIV-2607-17715` 属于不同 owner；本日三项长叙事配额按 V2 总分、长期 Books delta 与跨层影响排序。因此本项保留独立 Source Review 与 Books Decision，但不进入本日最多三项的长叙事；这不是被其他 family 覆盖，也不改变其 Evidence 完成状态。<!-- analysis-decision:SF-2026-ARXIV-2607-18171:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-18213:start -->《SWE-Pruner Pro: The Coder LLM Already Knows What to Prune》已完成 Deep Source Review。本 family 的独立增量为“四项 benchmark、消融与实现附录支持论文模型/harness 下的 pruning；不证明跨模型、任意代码库或并发 serving 的安全性。”；V2=3/2/3。它与入选 `SF-2026-ARXIV-2607-17525` 属于不同 owner；本日三项长叙事配额按 V2 总分、长期 Books delta 与跨层影响排序。因此本项保留独立 Source Review 与 Books Decision，但不进入本日最多三项的长叙事；这不是被其他 family 覆盖，也不改变其 Evidence 完成状态。<!-- analysis-decision:SF-2026-ARXIV-2607-18213:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-18231:start -->《FM-VLA: Force-based Memory for Vision-Language-Action Models in Contact-Rich Manipulation》已完成 Deep Source Review。本 family 的独立增量为“方法、实验和 implementation details 支持所测机器人任务；不证明传感器漂移、跨 embodiment 或开放环境鲁棒性。”；V2=3/2/3。它与入选 `SF-2026-ARXIV-2607-17525` 属于不同 owner；本日三项长叙事配额按 V2 总分、长期 Books delta 与跨层影响排序。因此本项保留独立 Source Review 与 Books Decision，但不进入本日最多三项的长叙事；这不是被其他 family 覆盖，也不改变其 Evidence 完成状态。<!-- analysis-decision:SF-2026-ARXIV-2607-18231:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-18603:start -->《AutoIndex: Learning Representation Programs for Retrieval》已完成 Deep Source Review。本 family 的独立增量为“CRUMB tasks、实现与限制支持小规模 program search 的可行性；不证明开放 corpus、生产成本或全局最优。”；V2=3/2/3。它与入选 `SF-2026-ARXIV-2607-17525` 属于不同 owner；本日三项长叙事配额按 V2 总分、长期 Books delta 与跨层影响排序。因此本项保留独立 Source Review 与 Books Decision，但不进入本日最多三项的长叙事；这不是被其他 family 覆盖，也不改变其 Evidence 完成状态。<!-- analysis-decision:SF-2026-ARXIV-2607-18603:end -->

## 6. Books Comparison

<!-- validator:books-comparison-v1 -->
| Source Family ID | Stable Node ID | Target Chapter Ref | Adjacent Chapter Refs | Existing Proposition | New Evidence Delta | Evolution Relation | Decision | Books Review Ref |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2607-17525 | PLATFORM-MONITORING | books/part-06-ai-infrastructure/67-monitoring.md#L1 | books/part-06-ai-infrastructure/66-evaluation-system.md#L14-L14; books/part-06-ai-infrastructure/68-logging.md#L14-L14 | existing:SF-2026-ARXIV-2607-17525 | delta:SF-2026-ARXIV-2607-17525 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2607-17525 |
| SF-2026-ARXIV-2607-17545 | AGENT-MEMORY | books/part-07-agent/77-memory.md#L244 | books/part-07-agent/76-rag.md#L14-L14; books/part-07-agent/78-tool-calling.md#L14-L14 | existing:SF-2026-ARXIV-2607-17545 | delta:SF-2026-ARXIV-2607-17545 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2607-17545 |
| SF-2026-ARXIV-2607-17621 | AGENT-MEMORY | books/part-07-agent/77-memory.md#L46 | books/part-07-agent/76-rag.md#L14-L14; books/part-07-agent/78-tool-calling.md#L14-L14 | existing:SF-2026-ARXIV-2607-17621 | delta:SF-2026-ARXIV-2607-17621 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2607-17621 |
| SF-2026-ARXIV-2607-17715 | INFER-KV-CACHE | books/part-05-inference-system/45-why-kv-cache-speeds-up.md#L584 | books/part-05-inference-system/44-decode.md#L14-L14; books/part-05-inference-system/46-continuous-batching.md#L14-L14 | existing:SF-2026-ARXIV-2607-17715 | delta:SF-2026-ARXIV-2607-17715 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2607-17715 |
| SF-2026-ARXIV-2607-17733 | INFER-TENSORRT-LLM | books/part-05-inference-system/49-tensorrt-llm.md#L417 | books/part-05-inference-system/48-speculative-decoding.md#L16-L16; books/part-05-inference-system/50-vllm.md#L14-L14 | existing:SF-2026-ARXIV-2607-17733 | delta:SF-2026-ARXIV-2607-17733 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2607-17733 |
| SF-2026-ARXIV-2607-17747 | MULTIMODAL-WORLD-MODELS | books/part-03-multimodal-world-models/25-multimodal-world-models.md#L68 | books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md#L14-L14; books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#L14-L14 | existing:SF-2026-ARXIV-2607-17747 | delta:SF-2026-ARXIV-2607-17747 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2607-17747 |
| SF-2026-ARXIV-2607-17751 | AGENT-TOOL-CALLING | books/part-07-agent/78-tool-calling.md#L82 | books/part-07-agent/77-memory.md#L14-L14; books/part-07-agent/79-planning.md#L14-L14 | existing:SF-2026-ARXIV-2607-17751 | delta:SF-2026-ARXIV-2607-17751 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2607-17751 |
| SF-2026-ARXIV-2607-17786 | MULTIMODAL-EMBODIED-VLA | books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#L305 | books/part-03-multimodal-world-models/25-multimodal-world-models.md#L14-L14; books/part-04-training-system/27-data.md#L14-L14 | existing:SF-2026-ARXIV-2607-17786 | delta:SF-2026-ARXIV-2607-17786 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2607-17786 |
| SF-2026-ARXIV-2607-17914 | AGENT-MULTI-AGENT | books/part-07-agent/82-multi-agent.md#L1 | books/part-07-agent/81-workflow.md#L14-L14; books/part-07-agent/83-mcp.md#L14-L14 | existing:SF-2026-ARXIV-2607-17914 | delta:SF-2026-ARXIV-2607-17914 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2607-17914 |
| SF-2026-ARXIV-2607-17973 | MULTIMODAL-WORLD-MODELS | books/part-03-multimodal-world-models/25-multimodal-world-models.md#L87 | books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md#L14-L14; books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#L14-L14 | existing:SF-2026-ARXIV-2607-17973 | delta:SF-2026-ARXIV-2607-17973 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2607-17973 |
| SF-2026-ARXIV-2607-17979 | INFER-TENSORRT-LLM | books/part-05-inference-system/49-tensorrt-llm.md#L1 | books/part-05-inference-system/48-speculative-decoding.md#L16-L16; books/part-05-inference-system/50-vllm.md#L14-L14 | existing:SF-2026-ARXIV-2607-17979 | delta:SF-2026-ARXIV-2607-17979 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2607-17979 |
| SF-2026-ARXIV-2607-17986 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#L1 | books/part-06-ai-infrastructure/71-multi-tenant.md#L14-L14; books/part-06-ai-infrastructure/73-production-best-practice.md#L14-L14 | existing:SF-2026-ARXIV-2607-17986 | delta:SF-2026-ARXIV-2607-17986 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2607-17986 |
| SF-2026-ARXIV-2607-18016 | MULTIMODAL-EMBODIED-VLA | books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#L171 | books/part-03-multimodal-world-models/25-multimodal-world-models.md#L14-L14; books/part-04-training-system/27-data.md#L14-L14 | existing:SF-2026-ARXIV-2607-18016 | delta:SF-2026-ARXIV-2607-18016 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2607-18016 |
| SF-2026-ARXIV-2607-18110 | TRAIN-SFT | books/part-04-training-system/29-sft.md#L1 | books/part-04-training-system/28-pretraining.md#L14-L14; books/part-04-training-system/30-lora.md#L14-L14 | existing:SF-2026-ARXIV-2607-18110 | delta:SF-2026-ARXIV-2607-18110 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2607-18110 |
| SF-2026-ARXIV-2607-18141 | INFER-GPU-MEMORY | books/part-05-inference-system/54-gpu-memory.md#L248 | books/part-05-inference-system/53-kserve-llm.md#L14-L14; books/part-05-inference-system/55-pd-disaggregation.md#L14-L14 | existing:SF-2026-ARXIV-2607-18141 | delta:SF-2026-ARXIV-2607-18141 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2607-18141 |
| SF-2026-ARXIV-2607-18171 | AGENT-WORKFLOW | books/part-07-agent/81-workflow.md#L1 | books/part-07-agent/80-reflection.md#L14-L14; books/part-07-agent/82-multi-agent.md#L14-L14 | existing:SF-2026-ARXIV-2607-18171 | delta:SF-2026-ARXIV-2607-18171 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2607-18171 |
| SF-2026-ARXIV-2607-18213 | AGENT-CONTEXT | books/part-07-agent/75-context.md#L250 | books/part-07-agent/74-prompt.md#L14-L14; books/part-07-agent/76-rag.md#L14-L14 | existing:SF-2026-ARXIV-2607-18213 | delta:SF-2026-ARXIV-2607-18213 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2607-18213 |
| SF-2026-ARXIV-2607-18231 | MULTIMODAL-EMBODIED-VLA | books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#L281 | books/part-03-multimodal-world-models/25-multimodal-world-models.md#L14-L14; books/part-04-training-system/27-data.md#L14-L14 | existing:SF-2026-ARXIV-2607-18231 | delta:SF-2026-ARXIV-2607-18231 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2607-18231 |
| SF-2026-ARXIV-2607-18603 | AGENT-RAG | books/part-07-agent/76-rag.md#L35 | books/part-07-agent/75-context.md#L14-L14; books/part-07-agent/77-memory.md#L14-L14 | existing:SF-2026-ARXIV-2607-18603 | delta:SF-2026-ARXIV-2607-18603 | Layering / Dependency | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2607-18603 |

<!-- books-review:SF-2026-ARXIV-2607-17525:start --><!-- existing:SF-2026-ARXIV-2607-17525:start -->对读 `books/part-06-ai-infrastructure/67-monitoring.md#L1` 与相邻章节后，现有命题（`books/part-06-ai-infrastructure/67-monitoring.md#L1`）为：Ch67 已区分 transport_error_rate、contract_failure_rate 与 runtime-success/quality-failure，但尚未把 failure origin 与 detectability 组成可操作的分类坐标，也没有说明 silent failure 如何进入可观测性闭环。<!-- existing:SF-2026-ARXIV-2607-17525:end --><!-- delta:SF-2026-ARXIV-2607-17525:start -->新增证据边界：把多 provider serving 的 failure 以 origin layer 与 detectability 两轴建模，再由 issue evidence、独立复现与完整 case study 连接现象、根因、检测信号和恢复动作。关键 delta 不是新增错误名单，而是把 runtime_success 与 semantic/continuity failure 分开。 该 delta 已进入 `books/part-06-ai-infrastructure/67-monitoring.md#L1`，正文保留旧方案成立条件、约束变化、代价与下一重压力。<!-- delta:SF-2026-ARXIV-2607-17525:end --><!-- books-review:SF-2026-ARXIV-2607-17525:end -->

<!-- books-review:SF-2026-ARXIV-2607-17545:start --><!-- existing:SF-2026-ARXIV-2607-17545:start -->对读 `books/part-07-agent/77-memory.md#L244` 与相邻章节后，现有命题（`books/part-07-agent/77-memory.md#L244`）为：Ch77 已完整拥有 write-time summary、query-conditioned construction、预算化检索、consolidation/forgetting、derived-memory lineage 与 raw-evidence fallback，并明确不同 workload 下 retain 与 consolidate 共存。<!-- existing:SF-2026-ARXIV-2607-17545:end --><!-- delta:SF-2026-ARXIV-2607-17545:start -->新增证据边界：把 retain 与多种 generative consolidation operator 视为受 token budget 约束的可选择动作，以只使用在线可观测特征的 utility router 决定何时压缩、使用哪种压缩，并用 risk-controlled threshold 保留 abstain 路径。 该证据未改变现有长期命题；保留为受限 workload 的 supporting evidence，不在正文重复追加论文段落。<!-- delta:SF-2026-ARXIV-2607-17545:end --><!-- books-review:SF-2026-ARXIV-2607-17545:end -->

<!-- books-review:SF-2026-ARXIV-2607-17621:start --><!-- existing:SF-2026-ARXIV-2607-17621:start -->对读 `books/part-07-agent/77-memory.md#L46` 与相邻章节后，现有命题（`books/part-07-agent/77-memory.md#L46`）为：Ch77 已把 memory update 写成可撤销 proposal，并讨论 counterfactual attribution、terminal-reward credit assignment、provenance 和 verifier gate。<!-- existing:SF-2026-ARXIV-2607-17621:end --><!-- delta:SF-2026-ARXIV-2607-17621:start -->新增证据边界：从 frozen model 的 attention/attribution signal 提取 memory importance，引导 refine、保留或重写，而不是把一次 final reward 平均归因到全部 memory；更新仍是 derived-memory proposal，并需独立验证。 该证据未改变现有长期命题；保留为受限 workload 的 supporting evidence，不在正文重复追加论文段落。<!-- delta:SF-2026-ARXIV-2607-17621:end --><!-- books-review:SF-2026-ARXIV-2607-17621:end -->

<!-- books-review:SF-2026-ARXIV-2607-17715:start --><!-- existing:SF-2026-ARXIV-2607-17715:start -->对读 `books/part-05-inference-system/45-why-kv-cache-speeds-up.md#L584` 与相邻章节后，现有命题（`books/part-05-inference-system/45-why-kv-cache-speeds-up.md#L584`）为：Ch45 已分别建立 position-dependent prefix reuse、压缩 policy identity、组合 transition object、exact fallback 与生产 SLO 边界，覆盖该机制的长期命题。<!-- existing:SF-2026-ARXIV-2607-17715:end --><!-- delta:SF-2026-ARXIV-2607-17715:start -->新增证据边界：把 prefix KV 由完整 tensor 演进为可压缩、可组合的 cache object：压缩表示必须保留 position/model/policy identity，组合路径还需显式处理 segment seam 与 reconstruction error，而不能把 byte compatibility 当作 semantic composability。 该证据未改变现有长期命题；保留为受限 workload 的 supporting evidence，不在正文重复追加论文段落。<!-- delta:SF-2026-ARXIV-2607-17715:end --><!-- books-review:SF-2026-ARXIV-2607-17715:end -->

<!-- books-review:SF-2026-ARXIV-2607-17733:start --><!-- existing:SF-2026-ARXIV-2607-17733:start -->对读 `books/part-05-inference-system/49-tensorrt-llm.md#L417` 与相邻章节后，现有命题（`books/part-05-inference-system/49-tensorrt-llm.md#L417`）为：Ch49 已明确量化不自动加速，并完整写出 sensitivity/average-bit → block clustering → physical layout → compatible kernel → measurement gate 的路线。<!-- existing:SF-2026-ARXIV-2607-17733:end --><!-- delta:SF-2026-ARXIV-2607-17733:start -->新增证据边界：先估计 layer/channel sensitivity，再在平均 bit budget 下分配混合精度，并把逻辑 bit allocation lowering 为可执行的 block/layout/kernel 组合；收益来自物理执行计划而非小数 bit 数本身。 该证据未改变现有长期命题；保留为受限 workload 的 supporting evidence，不在正文重复追加论文段落。<!-- delta:SF-2026-ARXIV-2607-17733:end --><!-- books-review:SF-2026-ARXIV-2607-17733:end -->

<!-- books-review:SF-2026-ARXIV-2607-17747:start --><!-- existing:SF-2026-ARXIV-2607-17747:start -->对读 `books/part-03-multimodal-world-models/25-multimodal-world-models.md#L68` 与相邻章节后，现有命题（`books/part-03-multimodal-world-models/25-multimodal-world-models.md#L68`）为：Ch25 已区分 simulator、learned transition、action-conditioned rollout、policy coupling 与显式 safety constraint。<!-- existing:SF-2026-ARXIV-2607-17747:end --><!-- delta:SF-2026-ARXIV-2607-17747:start -->新增证据边界：以 learned world model 预测 action-conditioned network state，再在模型内评估候选控制动作；状态估计、policy 和真实网络 transition 分离。 该证据未改变现有长期命题；保留为受限 workload 的 supporting evidence，不在正文重复追加论文段落。<!-- delta:SF-2026-ARXIV-2607-17747:end --><!-- books-review:SF-2026-ARXIV-2607-17747:end -->

<!-- books-review:SF-2026-ARXIV-2607-17751:start --><!-- existing:SF-2026-ARXIV-2607-17751:start -->对读 `books/part-07-agent/78-tool-calling.md#L82` 与相邻章节后，现有命题（`books/part-07-agent/78-tool-calling.md#L82`）为：Ch78 已把 tool discovery/selection 写成 catalog contract、coarse retrieval、reranking、schema/execution separation 与 bounded loop。<!-- existing:SF-2026-ARXIV-2607-17751:end --><!-- delta:SF-2026-ARXIV-2607-17751:start -->新增证据边界：把 tool selection 从一次 top-k similarity 演进为 counterfactual decomposition 产生候选子意图，再以 progressive reranking 联合控制 recall 与 context budget；selector 只拥有 proposal，不拥有 execution authority。 该证据未改变现有长期命题；保留为受限 workload 的 supporting evidence，不在正文重复追加论文段落。<!-- delta:SF-2026-ARXIV-2607-17751:end --><!-- books-review:SF-2026-ARXIV-2607-17751:end -->

<!-- books-review:SF-2026-ARXIV-2607-17786:start --><!-- existing:SF-2026-ARXIV-2607-17786:start -->对读 `books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#L305` 与相邻章节后，现有命题（`books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#L305`）为：Ch26 已拥有 fast/slow controller、reasoning proposal、physical evidence、closed-loop failure 与 safety envelope；Ch72 拥有 authorization。<!-- existing:SF-2026-ARXIV-2607-17786:end --><!-- delta:SF-2026-ARXIV-2607-17786:start -->新增证据边界：将 VLA robustness 分解到 perception/reasoning/action stages，比较 reasoning module 在 clean 与 attacked conditions 下的帮助和新攻击面；显式 reasoning state 是可观测 proposal，不是物理 safety certificate。 该证据未改变现有长期命题；保留为受限 workload 的 supporting evidence，不在正文重复追加论文段落。<!-- delta:SF-2026-ARXIV-2607-17786:end --><!-- books-review:SF-2026-ARXIV-2607-17786:end -->

<!-- books-review:SF-2026-ARXIV-2607-17914:start --><!-- existing:SF-2026-ARXIV-2607-17914:start -->对读 `books/part-07-agent/82-multi-agent.md#L1` 与相邻章节后，现有命题（`books/part-07-agent/82-multi-agent.md#L1`）为：Ch82 已区分 message 与 authoritative state、讨论通信压缩/缺失、预算化 topology 和 fallback。<!-- existing:SF-2026-ARXIV-2607-17914:end --><!-- delta:SF-2026-ARXIV-2607-17914:start -->新增证据边界：通信丢失时，不盲目补全全部消息，而预测对 joint value 有影响的缺失状态；fallback 仍受本地 observation 和 uncertainty bound 约束。 该证据未改变现有长期命题；保留为受限 workload 的 supporting evidence，不在正文重复追加论文段落。<!-- delta:SF-2026-ARXIV-2607-17914:end --><!-- books-review:SF-2026-ARXIV-2607-17914:end -->

<!-- books-review:SF-2026-ARXIV-2607-17973:start --><!-- existing:SF-2026-ARXIV-2607-17973:start -->对读 `books/part-03-multimodal-world-models/25-multimodal-world-models.md#L87` 与相邻章节后，现有命题（`books/part-03-multimodal-world-models/25-multimodal-world-models.md#L87`）为：Ch25 已完整讨论 latent dynamics、hierarchical temporal state、imagined rollout 与 planning/policy coupling。<!-- existing:SF-2026-ARXIV-2607-17973:end --><!-- delta:SF-2026-ARXIV-2607-17973:start -->新增证据边界：把长 horizon rollout 由平坦 action generation 分解为 subgoal-conditioned latent transition；subgoal 提供低频 planning state，低层 action generator 负责局部可执行性。 该证据未改变现有长期命题；保留为受限 workload 的 supporting evidence，不在正文重复追加论文段落。<!-- delta:SF-2026-ARXIV-2607-17973:end --><!-- books-review:SF-2026-ARXIV-2607-17973:end -->

<!-- books-review:SF-2026-ARXIV-2607-17979:start --><!-- existing:SF-2026-ARXIV-2607-17979:start -->对读 `books/part-05-inference-system/49-tensorrt-llm.md#L1` 与相邻章节后，现有命题（`books/part-05-inference-system/49-tensorrt-llm.md#L1`）为：Ch49 已把 learned kernel generator 定位为 candidate producer，并要求 operation descriptor、correctness oracle、compile/run sandbox、measurement gate 与版本化 execution plan；Ch81 只接 workflow handoff。<!-- existing:SF-2026-ARXIV-2607-17979:end --><!-- delta:SF-2026-ARXIV-2607-17979:start -->新增证据边界：将 kernel generation 从自由文本 coding 约束为 executable harness：精确 specification、reference implementation、correctness tests、measurement gate、failure feedback 和 workload-specific optimization budget。 该证据未改变现有长期命题；保留为受限 workload 的 supporting evidence，不在正文重复追加论文段落。<!-- delta:SF-2026-ARXIV-2607-17979:end --><!-- books-review:SF-2026-ARXIV-2607-17979:end -->

<!-- books-review:SF-2026-ARXIV-2607-17986:start --><!-- existing:SF-2026-ARXIV-2607-17986:start -->对读 `books/part-06-ai-infrastructure/72-security.md#L1` 与相邻章节后，现有命题（`books/part-06-ai-infrastructure/72-security.md#L1`）为：Ch72 已逐层写入该 self-state protection/recovery 机制，并在 Review notes 保留此 exact source family。<!-- existing:SF-2026-ARXIV-2607-17986:end --><!-- delta:SF-2026-ARXIV-2607-17986:start -->新增证据边界：把 agent self-state 分成 instruction、config、memory 等可变层，系统枚举 write primitive、attack path、OS control 与 recovery；静态 ACL 只能保护稳定层，动态 memory 需要 workload-conditioned detection，备份只提供恢复而非 prevention。 该证据未改变现有长期命题；保留为受限 workload 的 supporting evidence，不在正文重复追加论文段落。<!-- delta:SF-2026-ARXIV-2607-17986:end --><!-- books-review:SF-2026-ARXIV-2607-17986:end -->

<!-- books-review:SF-2026-ARXIV-2607-18016:start --><!-- existing:SF-2026-ARXIV-2607-18016:start -->对读 `books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#L171` 与相邻章节后，现有命题（`books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#L171`）为：Ch26 已把 object/trajectory identity、persistent revisable state、physical evidence、environment transition 与 closed-loop verification 连成主线。<!-- existing:SF-2026-ARXIV-2607-18016:end --><!-- delta:SF-2026-ARXIV-2607-18016:start -->新增证据边界：以 persistent 3D object token 作为跨 perception、planning、locomotion/manipulation 的显式 state handle，使 observation 更新、目标指代、动作结果和 verifier 对齐到同一对象 identity。 该证据未改变现有长期命题；保留为受限 workload 的 supporting evidence，不在正文重复追加论文段落。<!-- delta:SF-2026-ARXIV-2607-18016:end --><!-- books-review:SF-2026-ARXIV-2607-18016:end -->

<!-- books-review:SF-2026-ARXIV-2607-18110:start --><!-- existing:SF-2026-ARXIV-2607-18110:start -->对读 `books/part-04-training-system/29-sft.md#L1` 与相邻章节后，现有命题（`books/part-04-training-system/29-sft.md#L1`）为：Ch29 已覆盖 teacher trajectory/diagnosis、context distillation、held-out oracle、teacher bias、staged transfer 和 reward-hacking boundary。<!-- existing:SF-2026-ARXIV-2607-18110:end --><!-- delta:SF-2026-ARXIV-2607-18110:start -->新增证据边界：对不可自动验证任务，不把 scalar reward 当唯一 teacher；coach 读取 trajectory 与 outcome，生成带诊断的 experiential target，再蒸馏回 student。teacher feedback 是训练数据 proposal，仍需 held-out rubric 和 anti-reward-hacking checks。 该证据未改变现有长期命题；保留为受限 workload 的 supporting evidence，不在正文重复追加论文段落。<!-- delta:SF-2026-ARXIV-2607-18110:end --><!-- books-review:SF-2026-ARXIV-2607-18110:end -->

<!-- books-review:SF-2026-ARXIV-2607-18141:start --><!-- existing:SF-2026-ARXIV-2607-18141:start -->对读 `books/part-05-inference-system/54-gpu-memory.md#L248` 与相邻章节后，现有命题（`books/part-05-inference-system/54-gpu-memory.md#L248`）为：Ch54 已有从 HBM→host→NVMe/network→CXL pooled state、persistent near-memory、ownership、prefetch 和 failure boundary 的完整路线。<!-- existing:SF-2026-ARXIV-2607-18141:end --><!-- delta:SF-2026-ARXIV-2607-18141:start -->新增证据边界：把跨 turn KV/session state 从单机 DRAM offload 演进为 CXL pooled rack memory，并显式建模 allocation、session affinity、DMA path、prefetch 和 failure domain；capacity tier 变成可寻址共享状态层。 该证据未改变现有长期命题；保留为受限 workload 的 supporting evidence，不在正文重复追加论文段落。<!-- delta:SF-2026-ARXIV-2607-18141:end --><!-- books-review:SF-2026-ARXIV-2607-18141:end -->

<!-- books-review:SF-2026-ARXIV-2607-18171:start --><!-- existing:SF-2026-ARXIV-2607-18171:start -->对读 `books/part-07-agent/81-workflow.md#L1` 与相邻章节后，现有命题（`books/part-07-agent/81-workflow.md#L1`）为：Ch81 已把 executable contract、IR/DAG、deterministic spine、agentic candidate、static/evaluator gate 与 rollback 串联；Ch49 拥有 kernel execution plan。<!-- existing:SF-2026-ARXIV-2607-18171:end --><!-- delta:SF-2026-ARXIV-2607-18171:start -->新增证据边界：先把 reference application lowering 为包含 data dependency 与 persistent scope 的 IR，再让 agent 在 sequential interpreter、static analysis、correctness check 与 latency measurement 约束下提出 transformation；IR 和 verifier 拥有 contract，agent 只拥有候选修改。 该证据未改变现有长期命题；保留为受限 workload 的 supporting evidence，不在正文重复追加论文段落。<!-- delta:SF-2026-ARXIV-2607-18171:end --><!-- books-review:SF-2026-ARXIV-2607-18171:end -->

<!-- books-review:SF-2026-ARXIV-2607-18213:start --><!-- existing:SF-2026-ARXIV-2607-18213:start -->对读 `books/part-07-agent/75-context.md#L250` 与相邻章节后，现有命题（`books/part-07-agent/75-context.md#L250`）为：Ch75 已明确 goal-conditioned structured code pruning、hidden-state scorer、syntax/dependency preservation、reversible pointer 与 benchmark boundary，并列出该论文。<!-- existing:SF-2026-ARXIV-2607-18213:end --><!-- delta:SF-2026-ARXIV-2607-18213:start -->新增证据边界：冻结 coder backbone，从其 hidden state 训练 goal/length-aware token scorer，在 serving 前执行结构感知 pruning；scorer 只是受 workload contract 约束的 context transformer，必须保留 source pointer 与 re-forward fallback。 该证据未改变现有长期命题；保留为受限 workload 的 supporting evidence，不在正文重复追加论文段落。<!-- delta:SF-2026-ARXIV-2607-18213:end --><!-- books-review:SF-2026-ARXIV-2607-18213:end -->

<!-- books-review:SF-2026-ARXIV-2607-18231:start --><!-- existing:SF-2026-ARXIV-2607-18231:start -->对读 `books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#L281` 与相邻章节后，现有命题（`books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#L281`）为：Ch26 已将 sensor/action schema、calibration、recurrent state、physical feedback、failure recovery 与 embodiment identity 作为闭环控制合同。<!-- existing:SF-2026-ARXIV-2607-18231:end --><!-- delta:SF-2026-ARXIV-2607-18231:start -->新增证据边界：为 contact-rich manipulation 增加 force-conditioned short-horizon memory，使 policy 不只根据视觉位置，而能保存接触状态、力变化与失败恢复线索；force memory 是传感 state，不是事实 authority。 该证据未改变现有长期命题；保留为受限 workload 的 supporting evidence，不在正文重复追加论文段落。<!-- delta:SF-2026-ARXIV-2607-18231:end --><!-- books-review:SF-2026-ARXIV-2607-18231:end -->

<!-- books-review:SF-2026-ARXIV-2607-18603:start --><!-- existing:SF-2026-ARXIV-2607-18603:start -->对读 `books/part-07-agent/76-rag.md#L35` 与相邻章节后，现有命题（`books/part-07-agent/76-rag.md#L35`）为：Ch76 已把 ingestion/chunking/representation/index identity、validation-guided retrieval、versioning、evaluation 与 rollback 写成完整系统路线。<!-- existing:SF-2026-ARXIV-2607-18603:end --><!-- delta:SF-2026-ARXIV-2607-18603:start -->新增证据边界：把 indexing 从固定 chunking/embedding 参数推进为可执行 representation-program DSL；validation loop 诊断 retrieval failure、合成候选程序并在 frozen corpus/query contract 上选择，最终 index artifact 必须版本化 program 与 encoder。 该证据未改变现有长期命题；保留为受限 workload 的 supporting evidence，不在正文重复追加论文段落。<!-- delta:SF-2026-ARXIV-2607-18603:end --><!-- books-review:SF-2026-ARXIV-2607-18603:end -->

## 7. Semantic Audit

<!-- validator:semantic-audit-v1 -->
| Audit ID | Auditor | Scope | Reviewed Refs | Findings | Resolution | Status |
| --- | --- | --- | --- | --- | --- | --- |
| SA-20260721-COVERAGE | fresh-context:final_contract_review | coverage | coverage:SRC-ARXIV:20260721; semantic-review:SA-20260721-COVERAGE | — | Verified — every frozen candidate has a final evidence route, Books disposition and resolved semantic audit | passed |
| SA-20260721-EVIDENCE | fresh-context:final_contract_review | evidence | review:SF-2026-ARXIV-2607-17525; review:SF-2026-ARXIV-2607-17545; review:SF-2026-ARXIV-2607-17621; review:SF-2026-ARXIV-2607-17715; review:SF-2026-ARXIV-2607-17733; review:SF-2026-ARXIV-2607-17747; review:SF-2026-ARXIV-2607-17751; review:SF-2026-ARXIV-2607-17786; review:SF-2026-ARXIV-2607-17914; review:SF-2026-ARXIV-2607-17973; review:SF-2026-ARXIV-2607-17979; review:SF-2026-ARXIV-2607-17986; review:SF-2026-ARXIV-2607-18016; review:SF-2026-ARXIV-2607-18110; review:SF-2026-ARXIV-2607-18141; review:SF-2026-ARXIV-2607-18171; review:SF-2026-ARXIV-2607-18213; review:SF-2026-ARXIV-2607-18231; review:SF-2026-ARXIV-2607-18603; semantic-review:SA-20260721-EVIDENCE | — | Verified — every frozen candidate has a final evidence route, Books disposition and resolved semantic audit | passed |
| SA-20260721-SELECTION | fresh-context:final_contract_review | deep_analysis_selection | analysis:AU-20260721-260717525; analysis:AU-20260721-260717715; analysis:AU-20260721-260717986; semantic-review:SA-20260721-SELECTION | — | Verified — every frozen candidate has a final evidence route, Books disposition and resolved semantic audit | passed |
| SA-20260721-BOOKS | fresh-context:final_contract_review | books | books-review:SF-2026-ARXIV-2607-17525; books-review:SF-2026-ARXIV-2607-17545; books-review:SF-2026-ARXIV-2607-17621; books-review:SF-2026-ARXIV-2607-17715; books-review:SF-2026-ARXIV-2607-17733; books-review:SF-2026-ARXIV-2607-17747; books-review:SF-2026-ARXIV-2607-17751; books-review:SF-2026-ARXIV-2607-17786; books-review:SF-2026-ARXIV-2607-17914; books-review:SF-2026-ARXIV-2607-17973; books-review:SF-2026-ARXIV-2607-17979; books-review:SF-2026-ARXIV-2607-17986; books-review:SF-2026-ARXIV-2607-18016; books-review:SF-2026-ARXIV-2607-18110; books-review:SF-2026-ARXIV-2607-18141; books-review:SF-2026-ARXIV-2607-18171; books-review:SF-2026-ARXIV-2607-18213; books-review:SF-2026-ARXIV-2607-18231; books-review:SF-2026-ARXIV-2607-18603; semantic-review:SA-20260721-BOOKS | — | Verified — every frozen candidate has a final evidence route, Books disposition and resolved semantic audit | passed |

<!-- semantic-review:SA-20260721-COVERAGE:start -->Fresh-context audit verified the frozen 19-family denominator, all exact first-public timestamps in [2026-07-20 09:00, 2026-07-21 09:00), and zero identifier overlap with D20 or D22. Artifact-boundary accounting now reports the observed state exactly: 19 routed families, 11 disclosed repository/project locators, 8 without a locator and 0 confirmed event-time pinned commits; no SRC-GITHUB-COMMIT receipt or unsupported ledger attribution remains. Coverage PASS; finding_count=0.<!-- semantic-review:SA-20260721-COVERAGE:end -->
<!-- semantic-review:SA-20260721-EVIDENCE:start -->Fresh-context audit recomputed all 19 exact-v1 snapshot SHA-256 digests, resolved every cited HTML anchor, and confirmed packet-to-central-to-Daily consistency for identity, timestamp, score, route, owner, claim boundary, artifact boundary and disposition. All 11 disclosed artifact URLs are retained, while only the unavailable event-time immutable commit/hash is marked undisclosed; the other eight families make no artifact claim. Evidence PASS; finding_count=0.<!-- semantic-review:SA-20260721-EVIDENCE:end -->
<!-- semantic-review:SA-20260721-SELECTION:start -->Fresh-context audit verified an eligibility denominator of exactly 17 Deep families, with three selected narrative units and fourteen source-specific non-selection rationales. The two Standard families remain fully reviewed but are absent from the Selection table, so neither promotion nor review downgrade occurred. Selection PASS; finding_count=0.<!-- semantic-review:SA-20260721-SELECTION:end -->
<!-- semantic-review:SA-20260721-BOOKS:start -->Fresh-context regression audit read the FailureAtlas integration in PLATFORM-MONITORING, its adjacent chapter handoffs and Review note. The passage preserves the RED baseline, changed silent-failure constraint, Layer x Detectability mechanism, ownership, trade-offs, failure/evidence boundary and coexistence condition. The other eighteen families remain bounded No Change decisions with owner-specific comparisons and no duplicate Books owner. Books PASS; finding_count=0.<!-- semantic-review:SA-20260721-BOOKS:end -->

## 8. Ignored Noise

1083 个窗口内 identity 中，1064 个未进入候选分母：它们属于垂直应用、单数据集质量增量、没有状态/控制权变化的模型使用案例，或不在合同 category route。该数字是 route closure，不是声称逐篇全文审阅。

## 9. Recommended Action

1. Sunday Weekly 聚合本日报 family 与 RP，不按发现日重复计分。
2. 只有重要 revision、artifact、反证或 owner 冲突才重开本日报。
3. Books Decision：1 个 `Integrate`，18 个 `No Change — Existing Coverage`，0 个 `Weekly Only — Context`，0 个 `Rejected — Low Durability / Out of Scope`；Deep 17 / Standard 2。

## 10. Repository Changes

- 新建或更新 `papers/2026/07/21/README.md`。
- 本日报长期 delta 已同步至：`books/part-06-ai-infrastructure/67-monitoring.md`。

## 11. Open Questions

- 后续 revision 是否新增 artifact、独立复现或 failure evidence，从而改变当前 claim boundary？
- Sunday Weekly 的跨日演进链是否需要合并本日报多个同类 family？

## 12. Sources

- [FailureAtlas: A Taxonomy of Failure Modes in Multi-Provider LLM Serving Infrastructure](https://arxiv.org/abs/2607.17525v1) — first-public（Asia/Shanghai）：2026-07-20；accessed：2026-08-27
- [Retain or Consolidate? Budget-Dependent Operator Selection for Language Agent Memory](https://arxiv.org/abs/2607.17545v1) — first-public（Asia/Shanghai）：2026-07-20；accessed：2026-08-27
- [Mechanistic Attention Guidance for Agent Memory Refinement](https://arxiv.org/abs/2607.17621v1) — first-public（Asia/Shanghai）：2026-07-20；accessed：2026-08-27
- [C^2KV: Compressed and Composable KV Cache Reuse for Efficient LLM Inference](https://arxiv.org/abs/2607.17715v1) — first-public（Asia/Shanghai）：2026-07-20；accessed：2026-08-27
- [MXSens: Sensitivity-Aware Mixed-Precision Quantization for Efficient LLM Inference](https://arxiv.org/abs/2607.17733v1) — first-public（Asia/Shanghai）：2026-07-20；accessed：2026-08-27
- [Mobile Network Control with a World Model](https://arxiv.org/abs/2607.17747v1) — first-public（Asia/Shanghai）：2026-07-20；accessed：2026-08-27
- [MagicSelector: Joint Optimization for Agent Tool Selection via Counterfactual Decomposition and Progressive Reranking](https://arxiv.org/abs/2607.17751v1) — first-public（Asia/Shanghai）：2026-07-20；accessed：2026-08-27
- [Reasoning as a Double-Edged Sword: Architecture and Cross-Stage Robustness in Vision-Language-Action Models](https://arxiv.org/abs/2607.17786v1) — first-public（Asia/Shanghai）：2026-07-20；accessed：2026-08-27
- [Value-Aware Prediction for Robust Multi-Agent Coordination Under Communication Loss](https://arxiv.org/abs/2607.17914v1) — first-public（Asia/Shanghai）：2026-07-20；accessed：2026-08-27
- [SAGE: Subgoal-Conditioned Action Generation for Latent World Model Planning](https://arxiv.org/abs/2607.17973v1) — first-public（Asia/Shanghai）：2026-07-20；accessed：2026-08-27
- [Harness Engineering for LLM-Driven GPU Kernel Generation](https://arxiv.org/abs/2607.17979v1) — first-public（Asia/Shanghai）：2026-07-20；accessed：2026-08-27
- [Self-State Attacks on Self-Hosted AI Agents: How Far Can OS Defenses Go?](https://arxiv.org/abs/2607.17986v1) — first-public（Asia/Shanghai）：2026-07-20；accessed：2026-08-27
- [Closing the Loop in Humanoid VLA: Persistent 3D Object Tokens for Verifiable Loco-Manipulation](https://arxiv.org/abs/2607.18016v1) — first-public（Asia/Shanghai）：2026-07-20；accessed：2026-08-27
- [LLM-as-a-Coach: Experiential Learning for Non-Verifiable Tasks](https://arxiv.org/abs/2607.18110v1) — first-public（Asia/Shanghai）：2026-07-21；accessed：2026-08-27
- [HyMCache: A KV Cache Framework for Multi-Turn LLM Serving with CXL-Hybrid Memory](https://arxiv.org/abs/2607.18141v1) — first-public（Asia/Shanghai）：2026-07-21；accessed：2026-08-27
- [FlashRT: Agent Harness for Guiding Agents to Deploy Real-Time Multimodal Applications](https://arxiv.org/abs/2607.18171v1) — first-public（Asia/Shanghai）：2026-07-21；accessed：2026-08-27
- [SWE-Pruner Pro: The Coder LLM Already Knows What to Prune](https://arxiv.org/abs/2607.18213v1) — first-public（Asia/Shanghai）：2026-07-21；accessed：2026-08-27
- [FM-VLA: Force-based Memory for Vision-Language-Action Models in Contact-Rich Manipulation](https://arxiv.org/abs/2607.18231v1) — first-public（Asia/Shanghai）：2026-07-21；accessed：2026-08-27
- [AutoIndex: Learning Representation Programs for Retrieval](https://arxiv.org/abs/2607.18603v1) — first-public（Asia/Shanghai）：2026-07-21；accessed：2026-08-27
- [July recovery snapshot](../_sources/datacite-arxiv-recovery-20260701-26/README.md) — accessed：2026-08-26
- [Research Sources Registry](../../../../docs/RESEARCH_SOURCES.md) — registry version 2026-08-25

## 13. Final Status

Daily V2.1 的 Coverage、Evidence、Deep Analysis Selection 与 Books Decision 均已完成；fresh-context Semantic Audit 无未解决 finding，三个 Gate 均已闭合。
