# Daily Research — 2026-03-04

**Research Date:** 2026-03-04

**Timezone:** Asia/Shanghai

**Strict Window:** 2026-03-03 09:00:00 ～ 2026-03-04 09:00:00（Asia/Shanghai，左闭右开）

**Contract:** V2.1 Historical Daily independent Full Replay；既有 Weekly 未参与 discovery、分母、评分、Review、Books 判断或漏项校准；Weekly dependency=0。

**Status:** In Progress；Coverage=Open、Evidence=Open、Books=Open。2026-09-03 fresh-context 反证审计已重开；当前机器结构和既有 retained Review 仍可复用，但 denominator completeness 尚未按“不得抽样、逐项判断”合同重新验收。


## Executive Summary

> **2026-09-03 Semantic Reopen：** 旧 `Complete` 声明已被 `papers/2026/03/_sources/latest-contract-semantic-reopen-20260903.json` 取代。在 `MAR26-FC-001/MAR26-FC-002/MAR26-FC-003` 与 `MAR26-FC-004` 关闭前，本日报不得恢复 `Complete`；validator 通过只表示机器接口自洽。

窗口内 raw identities=1270，完成 title+abstract semantic screening=1270/1270；冻结 Candidate Denominator=33，pre-denominator closures=1237。exact-v1 Review=33/33，withdrawn=0，blocked=0；Books Integrate proposal=3。

3 月 arXiv 的 `Submitted:v1` 与 `Updated:v1` 只作为版本 provenance，不承担事件归属。日报以 DataCite DOI `created/registered` 恢复 identity，再按官方 Sun–Thu 20:00 Eastern 公告时刻映射到北京时间半开窗口。公告落在 09:00 右边界时不归结束于该时刻的窗口，而归下一份日报。

## 1. Coverage

<!-- validator:report-metadata-v2 -->
| Field | Value |
| --- | --- |
| Contract Version | V2.1 |
| Score Schema | V2 |
| Report Type | Daily |
| Window Start | 2026-03-04 |
| Window End | 2026-03-04 |
| Registry Version | 2026-08-25 |
| Coverage Mode | Full Replay |
| Baseline Report | — |
| Changed Source IDs | — |
| Previous Denominator ID | — |
| Denominator ID | sha256:fd24b3d0c8b9a21d494b235c2d3104e18017d4c5feaddecdc82c00f5a5353539 |
| Denominator Frozen At | 2026-09-02T08:53:37Z |
| Completion Status | In Progress |
| Coverage Gate | Open |
| Evidence Gate | Open |
| Books Gate | Open |

### Source Coverage Receipt

<!-- validator:source-coverage-v2 -->
| Source ID | Window Start | Window End | Executed At | Endpoint / Filter | Result | Hits | Candidate Source Families | Pagination / Cursor | Window Watermark | Closure Evidence | Gap / Limitation ID |
| --- | --- | --- | --- | --- | --- | ---: | --- | --- | --- | --- | --- |
| SRC-ARXIV | 2026-03-03T09:00:00+08:00 | 2026-03-04T09:00:00+08:00 | 2026-09-02T08:53:37Z | official arXiv March archive + scheduled announcement recovery + exact-v1 abs/HTML/PDF; registered categories; 1270/1270 semantic replay | checked | 33 | SF-2026-ARXIV-2603-00063; SF-2026-ARXIV-2603-00195; SF-2026-ARXIV-2603-00196; SF-2026-ARXIV-2603-00356; SF-2026-ARXIV-2603-00357; SF-2026-ARXIV-2603-00495; SF-2026-ARXIV-2603-00575; SF-2026-ARXIV-2603-00811; SF-2026-ARXIV-2603-01209; SF-2026-ARXIV-2603-01630; SF-2026-ARXIV-2603-02176; SF-2026-ARXIV-2603-00349; SF-2026-ARXIV-2603-00381; SF-2026-ARXIV-2603-00468; SF-2026-ARXIV-2603-00623; SF-2026-ARXIV-2603-00680; SF-2026-ARXIV-2603-00825; SF-2026-ARXIV-2603-01058; SF-2026-ARXIV-2603-01162; SF-2026-ARXIV-2603-01399; SF-2026-ARXIV-2603-01499; SF-2026-ARXIV-2603-01960; SF-2026-ARXIV-2603-02075; SF-2026-ARXIV-2603-02146; SF-2026-ARXIV-2603-02188; SF-2026-ARXIV-2603-00188; SF-2026-ARXIV-2603-01045; SF-2026-ARXIV-2603-01548; SF-2026-ARXIV-2603-01581; SF-2026-ARXIV-2603-01639; SF-2026-ARXIV-2603-01661; SF-2026-ARXIV-2603-01683; SF-2026-ARXIV-2603-01966 | Not Applicable — frozen shared archive receipt enumerates the complete owner batch | 2026-03-04T09:00:00+08:00 | papers/2026/03/_sources/daily-20260304/official-archive-membership-receipt.json; papers/2026/03/_sources/daily-20260304/screening-ledger-final.json; coverage:SRC-ARXIV:20260304 | — |

<!-- coverage:SRC-ARXIV:20260304:start -->本次独立重放以官方公告日程恢复 strict-window inventory；保留 exact-ID archive membership 与 exact-v1 identity/access。当前注册表在 2026-08-25 生效，不反推 2026-03 的机构来源为当日 Required；all raw title+abstract rows 已由独立 reviewer 逐项完成 FP/FN audit，Coverage Gate Closed。<!-- coverage:SRC-ARXIV:20260304:end -->

### Later-effective non-arXiv archival replay

虽然 20 个机构/发现来源的 registry Effective Date 为 2026-08-25、按合同不反推为本日 Required，父任务仍要求本次执行 bounded archival replay。独立收据为 `papers/2026/03/_sources/daily-20260304/non-arxiv-historical-replay-receipt.json`；状态计数为 `{"date_only_lead_unowned": 3, "enumerated_no_hit": 9, "historical_backstop_incomplete": 1, "historical_cursor_incomplete": 7}`。没有任何线索同时取得 strict-window first-public instant 与长期机制证据，因此新增 Candidate Source Family=0。

日期-only 边界线索（不归属、不评分、不进入分母）：

- `SRC-OPENAI` — `2026-03-04` — [Extending single-minus amplitudes to gravitons](https://openai.com/research/index/)；官方页面没有精确发布时间/时区。
- `SRC-GOOGLE-AI` — `2026-03-03` — [Gemini 3.1 Flash-Lite model card update](https://deepmind.google/models/model-cards/)；官方页面没有精确发布时间/时区。
- `SRC-QWEN` — `2026-03-03` — [Qwen Code update](https://qwenlm.github.io/qwen-code-docs/en/blog/updates/)；官方页面没有精确发布时间/时区。

## 2. Candidate Ledger

<!-- validator:candidate-ledger-v2.1 -->
| Source Family ID | Primary Identifier | Event Identity | Owner Week | First-public Date | Supporting Source IDs | Design Delta | System Reach | Durability | Total | Candidate State | Review Status | Access Status | Review Override | Review Ref | Owner Report Ref | Prior Review Ref | Reconciliation | Stable Node ID | Books Disposition | Books Review Ref | Benchmark Claim |
| --- | --- | --- | --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2603-00063 | arXiv:2603.00063v1 | paper-v1:2603.00063 | 2026-W10 | 2026-03-03 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2603-00063 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-00063 | no |
| SF-2026-ARXIV-2603-00195 | arXiv:2603.00195v1 | paper-v1:2603.00195 | 2026-W10 | 2026-03-03 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2603-00195 | self | — | new_in_window | AGENT-PLATFORM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-00195 | no |
| SF-2026-ARXIV-2603-00196 | arXiv:2603.00196v1 | paper-v1:2603.00196 | 2026-W10 | 2026-03-03 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2603-00196 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-00196 | no |
| SF-2026-ARXIV-2603-00356 | arXiv:2603.00356v1 | paper-v1:2603.00356 | 2026-W10 | 2026-03-03 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2603-00356 | self | — | new_in_window | INFER-SCHEDULING | Integrate | books-review:SF-2026-ARXIV-2603-00356 | no |
| SF-2026-ARXIV-2603-00357 | arXiv:2603.00357v1 | paper-v1:2603.00357 | 2026-W10 | 2026-03-03 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2603-00357 | self | — | new_in_window | TRAIN-CHECKPOINT | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-00357 | no |
| SF-2026-ARXIV-2603-00495 | arXiv:2603.00495v1 | paper-v1:2603.00495 | 2026-W10 | 2026-03-03 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2603-00495 | self | — | new_in_window | PLATFORM-FOUNDATIONS | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-00495 | no |
| SF-2026-ARXIV-2603-00575 | arXiv:2603.00575v1 | paper-v1:2603.00575 | 2026-W10 | 2026-03-03 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2603-00575 | self | — | new_in_window | AGENT-PLATFORM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-00575 | no |
| SF-2026-ARXIV-2603-00811 | arXiv:2603.00811v1 | paper-v1:2603.00811 | 2026-W10 | 2026-03-03 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2603-00811 | self | — | new_in_window | TRAIN-DATA | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-00811 | no |
| SF-2026-ARXIV-2603-01209 | arXiv:2603.01209v1 | paper-v1:2603.01209 | 2026-W10 | 2026-03-03 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2603-01209 | self | — | new_in_window | AGENT-PLATFORM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-01209 | no |
| SF-2026-ARXIV-2603-01630 | arXiv:2603.01630v1 | paper-v1:2603.01630 | 2026-W10 | 2026-03-03 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2603-01630 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-01630 | no |
| SF-2026-ARXIV-2603-02176 | arXiv:2603.02176v1 | paper-v1:2603.02176 | 2026-W10 | 2026-03-03 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2603-02176 | self | — | new_in_window | AGENT-PLATFORM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-02176 | no |
| SF-2026-ARXIV-2603-00349 | arXiv:2603.00349v1 | paper-v1:2603.00349 | 2026-W10 | 2026-03-03 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2603-00349 | self | — | new_in_window | AGENT-MULTI-AGENT | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-00349 | no |
| SF-2026-ARXIV-2603-00381 | arXiv:2603.00381v1 | paper-v1:2603.00381 | 2026-W10 | 2026-03-03 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2603-00381 | self | — | new_in_window | AGENT-MULTI-AGENT | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-00381 | no |
| SF-2026-ARXIV-2603-00468 | arXiv:2603.00468v1 | paper-v1:2603.00468 | 2026-W10 | 2026-03-03 | SRC-ARXIV | 2 | 3 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2603-00468 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-00468 | no |
| SF-2026-ARXIV-2603-00623 | arXiv:2603.00623v1 | paper-v1:2603.00623 | 2026-W10 | 2026-03-03 | SRC-ARXIV | 3 | 3 | 2 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2603-00623 | self | — | new_in_window | PLATFORM-TRACE | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-00623 | no |
| SF-2026-ARXIV-2603-00680 | arXiv:2603.00680v1 | paper-v1:2603.00680 | 2026-W10 | 2026-03-03 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2603-00680 | self | — | new_in_window | AGENT-MEMORY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-00680 | no |
| SF-2026-ARXIV-2603-00825 | arXiv:2603.00825v1 | paper-v1:2603.00825 | 2026-W10 | 2026-03-03 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2603-00825 | self | — | new_in_window | MULTIMODAL-WORLD-MODELS | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-00825 | no |
| SF-2026-ARXIV-2603-01058 | arXiv:2603.01058v1 | paper-v1:2603.01058 | 2026-W10 | 2026-03-03 | SRC-ARXIV | 3 | 3 | 2 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2603-01058 | self | — | new_in_window | INFER-GPU-MEMORY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-01058 | no |
| SF-2026-ARXIV-2603-01162 | arXiv:2603.01162v1 | paper-v1:2603.01162 | 2026-W10 | 2026-03-03 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2603-01162 | self | — | new_in_window | TRAIN-GRPO | Integrate | books-review:SF-2026-ARXIV-2603-01162 | no |
| SF-2026-ARXIV-2603-01399 | arXiv:2603.01399v1 | paper-v1:2603.01399 | 2026-W10 | 2026-03-03 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2603-01399 | self | — | new_in_window | INFER-SPECULATIVE-DECODING | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-01399 | no |
| SF-2026-ARXIV-2603-01499 | arXiv:2603.01499v1 | paper-v1:2603.01499 | 2026-W10 | 2026-03-03 | SRC-ARXIV | 3 | 3 | 2 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2603-01499 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-01499 | no |
| SF-2026-ARXIV-2603-01960 | arXiv:2603.01960v1 | paper-v1:2603.01960 | 2026-W10 | 2026-03-03 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2603-01960 | self | — | new_in_window | INFER-TENSORRT-LLM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-01960 | no |
| SF-2026-ARXIV-2603-02075 | arXiv:2603.02075v1 | paper-v1:2603.02075 | 2026-W10 | 2026-03-03 | SRC-ARXIV | 3 | 3 | 2 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2603-02075 | self | — | new_in_window | TRAIN-DATA | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-02075 | no |
| SF-2026-ARXIV-2603-02146 | arXiv:2603.02146v1 | paper-v1:2603.02146 | 2026-W10 | 2026-03-03 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | knowledge_gap | review:SF-2026-ARXIV-2603-02146 | self | — | new_in_window | TRAIN-GRPO | Integrate | books-review:SF-2026-ARXIV-2603-02146 | no |
| SF-2026-ARXIV-2603-02188 | arXiv:2603.02188v1 | paper-v1:2603.02188 | 2026-W10 | 2026-03-03 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2603-02188 | self | — | new_in_window | MODEL-MULTI-HEAD-ATTENTION | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-02188 | no |
| SF-2026-ARXIV-2603-00188 | arXiv:2603.00188v1 | paper-v1:2603.00188 | 2026-W10 | 2026-03-03 | SRC-ARXIV | 3 | 2 | 2 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2603-00188 | self | — | new_in_window | INFER-KV-CACHE | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-00188 | no |
| SF-2026-ARXIV-2603-01045 | arXiv:2603.01045v1 | paper-v1:2603.01045 | 2026-W10 | 2026-03-03 | SRC-ARXIV | 2 | 3 | 2 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2603-01045 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-01045 | no |
| SF-2026-ARXIV-2603-01548 | arXiv:2603.01548v1 | paper-v1:2603.01548 | 2026-W10 | 2026-03-03 | SRC-ARXIV | 3 | 2 | 2 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2603-01548 | self | — | new_in_window | AGENT-TOOL-CALLING | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-01548 | no |
| SF-2026-ARXIV-2603-01581 | arXiv:2603.01581v1 | paper-v1:2603.01581 | 2026-W10 | 2026-03-03 | SRC-ARXIV | 3 | 2 | 2 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2603-01581 | self | — | new_in_window | INFER-SPECULATIVE-DECODING | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-01581 | no |
| SF-2026-ARXIV-2603-01639 | arXiv:2603.01639v1 | paper-v1:2603.01639 | 2026-W10 | 2026-03-03 | SRC-ARXIV | 3 | 2 | 2 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2603-01639 | self | — | new_in_window | INFER-SPECULATIVE-DECODING | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-01639 | no |
| SF-2026-ARXIV-2603-01661 | arXiv:2603.01661v1 | paper-v1:2603.01661 | 2026-W10 | 2026-03-03 | SRC-ARXIV | 2 | 3 | 2 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2603-01661 | self | — | new_in_window | INFER-SCHEDULING | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-01661 | no |
| SF-2026-ARXIV-2603-01683 | arXiv:2603.01683v1 | paper-v1:2603.01683 | 2026-W10 | 2026-03-03 | SRC-ARXIV | 3 | 2 | 2 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2603-01683 | self | — | new_in_window | TRAIN-RLHF | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-01683 | no |
| SF-2026-ARXIV-2603-01966 | arXiv:2603.01966v1 | paper-v1:2603.01966 | 2026-W10 | 2026-03-03 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2603-01966 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-01966 | no |

## 3. Review Completion Receipt

<!-- validator:review-completion-v1 -->
| Source Family ID | Review Provenance ID | Review Route | Primary Evidence Version | Reviewed Evidence Versions | Method / Identity Locators | Evaluation Locators | Limitations / Counterevidence Locators | Artifact Locators | Claim Boundary Ref | Completion Result |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2603-00063 | RP-11566662a07a332f | deep | arXiv:2603.00063v1 | SRC-ARXIV@arXiv:2603.00063v1 | https://arxiv.org/html/2603.00063v1#S4 — exact-v1 S4 — 4 More Sophisticated Methods and Their Fundamental Flaws (Method) | https://arxiv.org/html/2603.00063v1#S5.SS6 — exact-v1 §5.6 A Toy Illustration: Measuring a Capability and a Propensity (Evaluation illustration; not a production benchmark) | https://arxiv.org/html/2603.00063v1#S6 — exact-v1 S6 — 6 Conclusion (Limitations) | Not Disclosed — arXiv:2603.00063v1 exposes no dedicated Artifact / implementation section in the recovered exact-v1 body | claim:SF-2026-ARXIV-2603-00063 | complete |
| SF-2026-ARXIV-2603-00195 | RP-f7149b8149b8c911 | deep | arXiv:2603.00195v1 | SRC-ARXIV@arXiv:2603.00195v1 | https://arxiv.org/html/2603.00195v1#S2.SS5 — exact-v1 S2.SS5 — 2.5. Formal Methods Foundations (Method) | https://arxiv.org/html/2603.00195v1#S9 — exact-v1 S9 — 9. Evaluation (Evaluation) | https://arxiv.org/html/2603.00195v1#S11.SS1 — exact-v1 S11.SS1 — 11.1. Limitations (Limitations) | https://arxiv.org/html/2603.00195v1#S8 — exact-v1 S8 — 8. Implementation (Artifact) | claim:SF-2026-ARXIV-2603-00195 | complete |
| SF-2026-ARXIV-2603-00196 | RP-1dd278e0bae8d735 | deep | arXiv:2603.00196v1 | SRC-ARXIV@arXiv:2603.00196v1 | https://arxiv.org/html/2603.00196v1#A2 — exact-v1 A2 — Appendix B Additional Method Details (Method) | https://arxiv.org/html/2603.00196v1#A3 — exact-v1 A3 — Appendix C Additional Evaluations (Evaluation) | https://arxiv.org/html/2603.00196v1#Sx1 — exact-v1 Sx1 — Limitations (Limitations) | https://arxiv.org/html/2603.00196v1#A2.SS1 — exact-v1 A2.SS1 — B.1 Pseudocode Implementation (Artifact) | claim:SF-2026-ARXIV-2603-00196 | complete |
| SF-2026-ARXIV-2603-00356 | RP-dad4baa2d7a5983f | deep | arXiv:2603.00356v1 | SRC-ARXIV@arXiv:2603.00356v1 | https://arxiv.org/html/2603.00356v1#S4 — exact-v1 S4 — 4. System Architecture (Method) | https://arxiv.org/html/2603.00356v1#S5.SS3 — exact-v1 S5.SS3 — 5.3. Experiment 2: SLO-Aware Fair Share (Evaluation) | https://arxiv.org/html/2603.00356v1#S6.SS0.SSS0.Px3 — exact-v1 S6.SS0.SSS0.Px3 — Limitations. (Limitations) | https://arxiv.org/html/2603.00356v1#S5.SS1 — exact-v1 S5.SS1 — 5.1. Experimental Setup (Artifact) | claim:SF-2026-ARXIV-2603-00356 | complete |
| SF-2026-ARXIV-2603-00357 | RP-3afcffb2b1b65f56 | deep | arXiv:2603.00357v1 | SRC-ARXIV@arXiv:2603.00357v1 | https://arxiv.org/html/2603.00357v1#S3 — exact-v1 §3 SPARe: Stacked Parallelism with Adaptive Reordering (Method) | https://arxiv.org/html/2603.00357v1#S5 — exact-v1 S5 — 5 System Performance Evaluation (Evaluation) | https://arxiv.org/html/2603.00357v1#S6 — exact-v1 S6 — 6 Conclusion (Limitations) | Not Disclosed — arXiv:2603.00357v1 exposes no dedicated Artifact / implementation section in the recovered exact-v1 body | claim:SF-2026-ARXIV-2603-00357 | complete |
| SF-2026-ARXIV-2603-00495 | RP-c413c1859f36ee10 | deep | arXiv:2603.00495v1 | SRC-ARXIV@arXiv:2603.00495v1 | https://arxiv.org/html/2603.00495v1#S4 — exact-v1 S4 — 4 Design Principles for AI Runtime Infrastructure (Method) | https://arxiv.org/html/2603.00495v1#S7.SS3 — exact-v1 S7.SS3 — 7.3 Evaluation Beyond Post-Hoc Metrics (Evaluation) | https://arxiv.org/html/2603.00495v1#S8 — exact-v1 S8 — 8 Conclusion (Limitations) | Not Disclosed — arXiv:2603.00495v1 exposes no dedicated Artifact / implementation section in the recovered exact-v1 body | claim:SF-2026-ARXIV-2603-00495 | complete |
| SF-2026-ARXIV-2603-00575 | RP-223e56a2595669df | deep | arXiv:2603.00575v1 | SRC-ARXIV@arXiv:2603.00575v1 | https://arxiv.org/html/2603.00575v1#S3.SS2 — exact-v1 S3.SS2 — 3.2 Architecture (Method) | https://arxiv.org/html/2603.00575v1#S2.SS1 — exact-v1 S2.SS1 — 2.1 Execution Substrates and Reproducible Evaluation Harnesses (Evaluation) | https://arxiv.org/html/2603.00575v1#S5.SS7 — exact-v1 S5.SS7 — 5.7 Discussion: Quality, Triviality, and System-Level Limitations (Limitations) | Not Disclosed — arXiv:2603.00575v1 exposes no dedicated Artifact / implementation section in the recovered exact-v1 body | claim:SF-2026-ARXIV-2603-00575 | complete |
| SF-2026-ARXIV-2603-00811 | RP-203fd5ebed646e62 | deep | arXiv:2603.00811v1 | SRC-ARXIV@arXiv:2603.00811v1 | https://arxiv.org/html/2603.00811v1#A1 — exact-v1 A1 — Appendix A Curation Methods (Method) | https://arxiv.org/html/2603.00811v1#A5 — exact-v1 A5 — Appendix E Extended Evaluation (Evaluation) | https://arxiv.org/html/2603.00811v1#S6 — exact-v1 S6 — 6 Discussion and Conclusion (Limitations) | https://arxiv.org/html/2603.00811v1#Sx3 — exact-v1 Sx3 — Reproducibility Statement (Artifact) | claim:SF-2026-ARXIV-2603-00811 | complete |
| SF-2026-ARXIV-2603-01209 | RP-bdaeb2cfe9475c11 | deep | arXiv:2603.01209v1 | SRC-ARXIV@arXiv:2603.01209v1 | https://arxiv.org/html/2603.01209v1#S3 — exact-v1 S3 — 3 Methodology (Method) | https://arxiv.org/html/2603.01209v1#S4 — exact-v1 S4 — 4 Empirical Study: Opaque Knapsack Experiments (Evaluation) | https://arxiv.org/html/2603.01209v1#S5 — exact-v1 S5 — 5 Discussion (Limitations) | https://arxiv.org/html/2603.01209v1#A2 — exact-v1 A2 — Appendix B Agent Implementation (Artifact) | claim:SF-2026-ARXIV-2603-01209 | complete |
| SF-2026-ARXIV-2603-01630 | RP-8c7d1e66957e18b4 | deep | arXiv:2603.01630v1 | SRC-ARXIV@arXiv:2603.01630v1 | https://arxiv.org/html/2603.01630v1#A1.SS2 — exact-v1 A1.SS2 — A.2 Variational Bayesian methods:overview (Method) | https://arxiv.org/html/2603.01630v1#S5 — exact-v1 S5 — 5 Experiments (Evaluation) | https://arxiv.org/html/2603.01630v1#S6 — exact-v1 S6 — 6 Limitations (Limitations) | https://arxiv.org/html/2603.01630v1#A2.SS0.SSS1 — exact-v1 A2.SS0.SSS1 — B.0.1 System Setup (Artifact) | claim:SF-2026-ARXIV-2603-01630 | complete |
| SF-2026-ARXIV-2603-02176 | RP-77b8391885451360 | deep | arXiv:2603.02176v1 | SRC-ARXIV@arXiv:2603.02176v1 | https://arxiv.org/html/2603.02176v1#S2 — exact-v1 S2 — 2 Method (Method) | https://arxiv.org/html/2603.02176v1#S4 — exact-v1 S4 — 4 Experiments (Evaluation) | https://arxiv.org/html/2603.02176v1#S6 — exact-v1 S6 — 6 Conclusions and Future Work (Limitations) | https://arxiv.org/html/2603.02176v1#S4.SS1 — exact-v1 S4.SS1 — 4.1 Experimental Setup (Artifact) | claim:SF-2026-ARXIV-2603-02176 | complete |
| SF-2026-ARXIV-2603-00349 | RP-b8e8063ce3080e2e | deep | arXiv:2603.00349v1 | SRC-ARXIV@arXiv:2603.00349v1 | https://arxiv.org/html/2603.00349v1#S4 — exact-v1 S4 — 4 EmCoop Methodology (Method) | https://arxiv.org/html/2603.00349v1#S7 — exact-v1 S7 — 7 Experiment Design and Results (Evaluation) | https://arxiv.org/html/2603.00349v1#S8 — exact-v1 S8 — 8 Conclusion (Limitations) | https://arxiv.org/html/2603.00349v1#A4 — exact-v1 A4 — Appendix D Cooperation Analysis: Algorithmic Details (Artifact) | claim:SF-2026-ARXIV-2603-00349 | complete |
| SF-2026-ARXIV-2603-00381 | RP-c900b43e4623adcf | deep | arXiv:2603.00381v1 | SRC-ARXIV@arXiv:2603.00381v1 | https://arxiv.org/html/2603.00381v1#S2 — exact-v1 S2 — 2 A simple proof of concept (Method) | https://arxiv.org/html/2603.00381v1#S6 — exact-v1 S6 — 6 Experiments (Evaluation) | https://arxiv.org/html/2603.00381v1#S9 — exact-v1 S9 — 9 Conclusion (Limitations) | https://arxiv.org/html/2603.00381v1#A1 — exact-v1 A1 — Appendix A Experimental Details (Artifact) | claim:SF-2026-ARXIV-2603-00381 | complete |
| SF-2026-ARXIV-2603-00468 | RP-83bb3ca11bd13f1a | deep | arXiv:2603.00468v1 | SRC-ARXIV@arXiv:2603.00468v1 | https://arxiv.org/html/2603.00468v1#S3.SS2 — exact-v1 S3.SS2 — 3.2. Design Philosophy: The State Snapshot Paradigm (Method) | https://arxiv.org/html/2603.00468v1#S4.SS1 — exact-v1 S4.SS1 — 4.1. Experimental Setup (Evaluation) | https://arxiv.org/html/2603.00468v1#S5 — exact-v1 S5 — 5. Discussion (Limitations) | https://arxiv.org/html/2603.00468v1#S4.SS1 — exact-v1 S4.SS1 — 4.1. Experimental Setup (Artifact) | claim:SF-2026-ARXIV-2603-00468 | complete |
| SF-2026-ARXIV-2603-00623 | RP-f78eb1ee595facce | deep | arXiv:2603.00623v1 | SRC-ARXIV@arXiv:2603.00623v1 | https://arxiv.org/html/2603.00623v1#S3 — exact-v1 S3 — 3 Method (Method) | https://arxiv.org/html/2603.00623v1#S4 — exact-v1 S4 — 4 Experiments (Evaluation) | https://arxiv.org/html/2603.00623v1#Sx1 — exact-v1 Sx1 — Limitations (Limitations) | Not Disclosed — arXiv:2603.00623v1 exposes no dedicated Artifact / implementation section in the recovered exact-v1 body | claim:SF-2026-ARXIV-2603-00623 | complete |
| SF-2026-ARXIV-2603-00680 | RP-8a12497734cc2151 | deep | arXiv:2603.00680v1 | SRC-ARXIV@arXiv:2603.00680v1 | https://arxiv.org/html/2603.00680v1#S4 — exact-v1 §4 Self-Memory Policy Optimization (Method) | https://arxiv.org/html/2603.00680v1#S5 — exact-v1 S5 — 5 Experiments (Evaluation) | https://arxiv.org/html/2603.00680v1#Sx1 — exact-v1 Sx1 — Limitations (Limitations) | https://arxiv.org/html/2603.00680v1#S5.SS3 — exact-v1 S5.SS3 — 5.3 Implementation Details (Artifact) | claim:SF-2026-ARXIV-2603-00680 | complete |
| SF-2026-ARXIV-2603-00825 | RP-cab7b3477c3fd75f | deep | arXiv:2603.00825v1 | SRC-ARXIV@arXiv:2603.00825v1 | https://arxiv.org/html/2603.00825v1#S3 — exact-v1 S3 — 3 Method (Method) | https://arxiv.org/html/2603.00825v1#S4 — exact-v1 S4 — 4 Experiments (Evaluation) | https://arxiv.org/html/2603.00825v1#S5 — exact-v1 S5 — 5 Conclusion (Limitations) | https://arxiv.org/html/2603.00825v1#S4.SS1 — exact-v1 S4.SS1 — 4.1 Implementation Details (Artifact) | claim:SF-2026-ARXIV-2603-00825 | complete |
| SF-2026-ARXIV-2603-01058 | RP-59695ce0425d5979 | deep | arXiv:2603.01058v1 | SRC-ARXIV@arXiv:2603.01058v1 | https://arxiv.org/html/2603.01058v1#S4.SS1 — exact-v1 S4.SS1 — 4.1. TriMoE Architecture (Method) | https://arxiv.org/html/2603.01058v1#S5.SS1 — exact-v1 S5.SS1 — 5.1. Experiment Setup (Evaluation) | https://arxiv.org/html/2603.01058v1#S6 — exact-v1 S6 — 6. Conclusion (Limitations) | Not Disclosed — arXiv:2603.01058v1 exposes no dedicated Artifact / implementation section in the recovered exact-v1 body | claim:SF-2026-ARXIV-2603-01058 | complete |
| SF-2026-ARXIV-2603-01162 | RP-1433d806a95fa0ca | deep | arXiv:2603.01162v1 | SRC-ARXIV@arXiv:2603.01162v1 | https://arxiv.org/html/2603.01162v1#S4 — exact-v1 §4 Main results: U-statistic gradient and GRPO analysis (Method) | https://arxiv.org/html/2603.01162v1#S5 — exact-v1 S5 — 5 Experiments (Evaluation) | https://arxiv.org/html/2603.01162v1#S6 — exact-v1 S6 — 6 Discussion (Limitations) | Not Disclosed — arXiv:2603.01162v1 exposes no dedicated Artifact / implementation section in the recovered exact-v1 body | claim:SF-2026-ARXIV-2603-01162 | complete |
| SF-2026-ARXIV-2603-01399 | RP-789dcca4bc41cdde | deep | arXiv:2603.01399v1 | SRC-ARXIV@arXiv:2603.01399v1 | https://arxiv.org/html/2603.01399v1#S3 — exact-v1 S3 — 3 Methodology (Method) | https://arxiv.org/html/2603.01399v1#S4 — exact-v1 S4 — 4 Experiments (Evaluation) | https://arxiv.org/html/2603.01399v1#S5 — exact-v1 S5 — 5 Discussion (Limitations) | https://arxiv.org/html/2603.01399v1#S4.SS1.SSS0.Px3 — exact-v1 S4.SS1.SSS0.Px3 — Implementation Details. (Artifact) | claim:SF-2026-ARXIV-2603-01399 | complete |
| SF-2026-ARXIV-2603-01499 | RP-aa4ed13d1d79e8f8 | deep | arXiv:2603.01499v1 | SRC-ARXIV@arXiv:2603.01499v1 | https://arxiv.org/html/2603.01499v1#S2.SS1 — exact-v1 S2.SS1 — 2.1 Methods based on Obfuscation (Method) | https://arxiv.org/html/2603.01499v1#S6 — exact-v1 S6 — 6 Experiments (Evaluation) | https://arxiv.org/html/2603.01499v1#S7 — exact-v1 S7 — 7 Discussion and Future Work (Limitations) | https://arxiv.org/html/2603.01499v1#A6 — exact-v1 A6 — Appendix F Experiment Details (Artifact) | claim:SF-2026-ARXIV-2603-01499 | complete |
| SF-2026-ARXIV-2603-01960 | RP-4c1693267ccbfdde | deep | arXiv:2603.01960v1 | SRC-ARXIV@arXiv:2603.01960v1 | https://arxiv.org/html/2603.01960v1#S2 — exact-v1 S2 — 2 Method (Method) | https://arxiv.org/html/2603.01960v1#S3.SS3 — exact-v1 S3.SS3 — 3.3 Experimental Setup (Evaluation) | https://arxiv.org/html/2603.01960v1#S6 — exact-v1 S6 — 6 Limitations and Future Work (Limitations) | https://arxiv.org/html/2603.01960v1#S3.SS2 — exact-v1 S3.SS2 — 3.2 Implementation (Artifact) | claim:SF-2026-ARXIV-2603-01960 | complete |
| SF-2026-ARXIV-2603-02075 | RP-dcf12888a8bde5ad | deep | arXiv:2603.02075v1 | SRC-ARXIV@arXiv:2603.02075v1 | https://arxiv.org/html/2603.02075v1#S3.SS1 — exact-v1 S3.SS1 — 3.1 System Architecture (Method) | https://arxiv.org/html/2603.02075v1#S8.SS1 — exact-v1 S8.SS1 — 8.1 Experimental Setup (Evaluation) | https://arxiv.org/html/2603.02075v1#S10 — exact-v1 S10 — 10 Conclusion (Limitations) | https://arxiv.org/html/2603.02075v1#S7 — exact-v1 S7 — 7 Implementation (Artifact) | claim:SF-2026-ARXIV-2603-02075 | complete |
| SF-2026-ARXIV-2603-02146 | RP-8674c95d493fc790 | deep | arXiv:2603.02146v1 | SRC-ARXIV@arXiv:2603.02146v1 | https://arxiv.org/html/2603.02146v1#S2 — exact-v1 S2 — 2 Method (Method) | https://arxiv.org/html/2603.02146v1#S3 — exact-v1 S3 — 3 Experimental Setup (Evaluation) | https://arxiv.org/html/2603.02146v1#S6 — exact-v1 S6 — 6 Conclusion (Limitations) | https://arxiv.org/html/2603.02146v1#S3.SS1 — exact-v1 S3.SS1 — 3.1 Implementation Details (Artifact) | claim:SF-2026-ARXIV-2603-02146 | complete |
| SF-2026-ARXIV-2603-02188 | RP-734b47621a62a376 | deep | arXiv:2603.02188v1 | SRC-ARXIV@arXiv:2603.02188v1 | https://arxiv.org/html/2603.02188v1#A4 — exact-v1 A4 — Appendix D Llama-3 Architecture (Method) | https://arxiv.org/html/2603.02188v1#S4 — exact-v1 S4 — 4 Experiments (Evaluation) | https://arxiv.org/html/2603.02188v1#S5 — exact-v1 S5 — 5 Conclusion (Limitations) | https://arxiv.org/html/2603.02188v1#S4.SS1 — exact-v1 S4.SS1 — 4.1 Experimental Setup (Artifact) | claim:SF-2026-ARXIV-2603-02188 | complete |
| SF-2026-ARXIV-2603-00188 | RP-3b08fa289444b286 | deep | arXiv:2603.00188v1 | SRC-ARXIV@arXiv:2603.00188v1 | https://arxiv.org/html/2603.00188v1#S4 — exact-v1 S4 — 4. ST-Lite Framework (Method) | https://arxiv.org/html/2603.00188v1#S5 — exact-v1 S5 — 5. Experiment (Evaluation) | https://arxiv.org/html/2603.00188v1#A7 — exact-v1 A7 — Appendix G Limitations (Limitations) | https://arxiv.org/html/2603.00188v1#A2 — exact-v1 A2 — Appendix B Implementation Details (Artifact) | claim:SF-2026-ARXIV-2603-00188 | complete |
| SF-2026-ARXIV-2603-01045 | RP-1a1706d5399321d5 | deep | arXiv:2603.01045v1 | SRC-ARXIV@arXiv:2603.01045v1 | https://arxiv.org/html/2603.01045v1#S2.SS0.SSS0.Px2 — exact-v1 S2.SS0.SSS0.Px2 — Multi-Agent Architectures and Role-Agnosticism. (Method) | https://arxiv.org/html/2603.01045v1#S4 — exact-v1 S4 — 4 Experiments (Evaluation) | https://arxiv.org/html/2603.01045v1#Sx1 — exact-v1 Sx1 — Limitations (Limitations) | https://arxiv.org/html/2603.01045v1#S4.SS1 — exact-v1 S4.SS1 — 4.1 Experimental Setup (Artifact) | claim:SF-2026-ARXIV-2603-01045 | complete |
| SF-2026-ARXIV-2603-01548 | RP-1705a58c6f8ed2ed | deep | arXiv:2603.01548v1 | SRC-ARXIV@arXiv:2603.01548v1 | https://arxiv.org/pdf/2603.01548v1#page=4 — PDF page 4; exact heading 2. Architecture: Health Monitors + Tool Graph (Method) | https://arxiv.org/pdf/2603.01548v1#page=11 — PDF page 11; exact heading 3. Multi-Domain Evaluation (Evaluation) | https://arxiv.org/pdf/2603.01548v1#page=19 — PDF page 19; exact heading 5.4 Honest Limitations (Limitations) | Not Disclosed — arXiv:2603.01548v1 exposes no dedicated Artifact / implementation section in the recovered exact-v1 body | claim:SF-2026-ARXIV-2603-01548 | complete |
| SF-2026-ARXIV-2603-01581 | RP-6e07f6f6d15a33a8 | deep | arXiv:2603.01581v1 | SRC-ARXIV@arXiv:2603.01581v1 | https://arxiv.org/html/2603.01581v1#S4 — exact-v1 S4 — 4. KERV Framework (Method) | https://arxiv.org/html/2603.01581v1#S6 — exact-v1 S6 — 6. Experiments (Evaluation) | https://arxiv.org/html/2603.01581v1#S6.SS3 — exact-v1 S6.SS3 — 6.3. Discussion (Limitations) | https://arxiv.org/html/2603.01581v1#S5 — exact-v1 S5 — 5. System Implementation (Artifact) | claim:SF-2026-ARXIV-2603-01581 | complete |
| SF-2026-ARXIV-2603-01639 | RP-df08d243ceccbe87 | deep | arXiv:2603.01639v1 | SRC-ARXIV@arXiv:2603.01639v1 | https://arxiv.org/html/2603.01639v1#S4 — exact-v1 S4 — 4 Method (Method) | https://arxiv.org/html/2603.01639v1#S5 — exact-v1 S5 — 5 Experiments (Evaluation) | https://arxiv.org/html/2603.01639v1#S7 — exact-v1 S7 — 7 Conclusion (Limitations) | https://arxiv.org/html/2603.01639v1#Sx1 — exact-v1 Sx1 — Reproducibility Statement (Artifact) | claim:SF-2026-ARXIV-2603-01639 | complete |
| SF-2026-ARXIV-2603-01661 | RP-9266e47519eefb9e | deep | arXiv:2603.01661v1 | SRC-ARXIV@arXiv:2603.01661v1 | https://arxiv.org/html/2603.01661v1#S4 — exact-v1 S4 — 4. Orchestration Methods (Method) | https://arxiv.org/html/2603.01661v1#S6 — exact-v1 S6 — 6. Experiments (Evaluation) | https://arxiv.org/html/2603.01661v1#S7 — exact-v1 S7 — 7. Conclusion (Limitations) | https://arxiv.org/html/2603.01661v1#S5 — exact-v1 S5 — 5. Implementation (Artifact) | claim:SF-2026-ARXIV-2603-01661 | complete |
| SF-2026-ARXIV-2603-01683 | RP-673c136d3438946b | deep | arXiv:2603.01683v1 | SRC-ARXIV@arXiv:2603.01683v1 | https://arxiv.org/html/2603.01683v1#A5.SS0.SSS0.Px3 — exact-v1 A5.SS0.SSS0.Px3 — Evaluation Protocol (Method) | https://arxiv.org/html/2603.01683v1#S5 — exact-v1 S5 — 5 Experiments (Evaluation) | https://arxiv.org/html/2603.01683v1#S7 — exact-v1 S7 — 7 Discussion and Conclusion (Limitations) | Not Disclosed — arXiv:2603.01683v1 exposes no dedicated Artifact / implementation section in the recovered exact-v1 body | claim:SF-2026-ARXIV-2603-01683 | complete |
| SF-2026-ARXIV-2603-01966 | RP-3272e6961b36a32e | deep | arXiv:2603.01966v1 | SRC-ARXIV@arXiv:2603.01966v1 | https://arxiv.org/html/2603.01966v1#S3 — exact-v1 S3 — 3 AMemGym (Method) | https://arxiv.org/html/2603.01966v1#A5 — exact-v1 A5 — Appendix E Details for the self-evolution experiment (Evaluation) | https://arxiv.org/html/2603.01966v1#S6 — exact-v1 S6 — 6 Conclusion (Limitations) | https://arxiv.org/html/2603.01966v1#A3 — exact-v1 A3 — Appendix C Implementation Details (Artifact) | claim:SF-2026-ARXIV-2603-01966 | complete |

### Source Reviews

<!-- review:SF-2026-ARXIV-2603-00063:start -->
#### Measuring What AI Systems Might Do: Towards A Measurement Science in AI

问题与 changed constraint：一次 benchmark 得分把潜在能力、行为倾向和观测表现混成同一量，无法说明系统在条件变化后会做什么。

旧路径为何合理：在该约束未出现、规模较小或 workload 更稳定时，论文所比较的旧路径仍以更少状态、更短控制链和更成熟实现提供合理基线；不能因本论文出现而静默覆盖。

机制、state/data/control owner：论文把被测 disposition、measurement procedure、environment 与观测误差分开，使 evaluation claim 成为可反驳的测量对象。 对应 exact-v1 `S4 — 4 More Sophisticated Methods and Their Fundamental Flaws`；该机制由 `PLATFORM-EVALUATION-SYSTEM` 承载。原文定位摘录仅作核对：4 More Sophisticated Methods and Their Fundamental Flaws Recognising the limitations of simple benchmarking, many researchers have turned to more sophisticated statistical approaches, most prominently Item Response Theory (IRT) and related latent‑variable models Martínez-Plumed et al. (2016); Martínez-Plumed et al. (2022); Kipnis et al. (2024); Polo et al. (2024); Zhou et al. (2024). These methods appear to offer a principled alternative to crude accuracy scores. Unlike benchmark averages, IRT models explicitly rep

Evaluation contract：正文建立 measurement-science 构念和误差来源；它不证明任一现有 benchmark 已经测到真实能力。 exact-v1 定位为 `https://arxiv.org/html/2603.00063v1#S5.SS6 — exact-v1 §5.6 A Toy Illustration: Measuring a Capability and a Propensity (Evaluation illustration; not a production benchmark)`；用于核对的原文摘录：Not Disclosed

证明与未证明：证据只支持上述 paper-specific workload 内的机制/测量关系；不支持把作者结果外推为其他模型、数据、硬件、精度、长度、batch、并发或 production SLO 的通用结论。

Trade-off、failure 与共存边界：更严格的 construct/procedure 记录提高可解释性，却增加设计与复现实验成本；窄而稳定的回归测试仍可只测表现。 反证/限制定位为 `S6 — 6 Conclusion`；用于核对的原文摘录：6 Conclusion Developing rigorous, theoretically grounded measures of AI capabilities and propensities is a substantial scientific undertaking. It requires interdisciplinary collaboration across AI, cognitive science, philosophy of science, psychometrics, statistics, and the broader behavioural sciences. The task is not merely to devise better datasets or to refine existing scoring procedures, but to articulate the ca

Artifact / implementation：exact-v1 `Not Disclosed — arXiv:2603.00063v1 exposes no dedicated Artifact / implementation section in the recovered exact-v1 body`；公开范围摘录：Not Disclosed。未公开的代码、commit、部署配置或复现实验不得由论文叙事反推。

<!-- claim:SF-2026-ARXIV-2603-00063:start -->只接受 arXiv:2603.00063v1 在 exact-v1 公开 workload 下的作者机制与实验主张；未披露的 model、hardware、precision、length、batch、concurrency、cost 与 production SLO 均为 Not Disclosed，不外推为通用结论。<!-- claim:SF-2026-ARXIV-2603-00063:end -->

Books Comparison：已读 `PLATFORM-EVALUATION-SYSTEM` 的 `books/part-06-ai-infrastructure/66-evaluation-system.md#从“有结果”到可追责、可干预的 Evidence (line 2326)` 及相邻 `books/part-06-ai-infrastructure/65-kai-scheduler.md#本章要回答的问题 (line 10); books/part-06-ai-infrastructure/67-monitoring.md#本章要回答的问题 (line 10)`；现有命题为“看到异常高分后再估计 benchmark contamination，无法区分记忆、能力和数据生态。更强的协议在可控训练副本中按已知比例注入样本，拟合 contamination–response curve，再把目标 run 映射到带不确定性的校正区间。它把污染从传闻变成可复现实验，但需要训练数据写权限与未污染 counterfactual，闭源模型通常不具备这些条件；此时只能报告疑似污染而不能伪造校正分。现有证据仅覆盖披露模型与五类 benchmark。”。Decision=`No Change — Existing Coverage`；该 author-side 判断仍待fresh-context Books reviewer，Integrate 项只进入日期队列。
<!-- review:SF-2026-ARXIV-2603-00063:end -->

<!-- review:SF-2026-ARXIV-2603-00195:start -->
#### Formal Analysis and Supply Chain Security for Agentic AI Skills

问题与 changed constraint：Agent Skill 可执行第三方代码和指令，普通包完整性检查看不到 prompt、tool permission 与依赖共同形成的供应链路径。

旧路径为何合理：在该约束未出现、规模较小或 workload 更稳定时，论文所比较的旧路径仍以更少状态、更短控制链和更成熟实现提供合理基线；不能因本论文出现而静默覆盖。

机制、state/data/control owner：工作把 Skill manifest、依赖、权限和行为属性交给形式化分析与可复查 artifact，令安装前 admission 拥有明确证据。 对应 exact-v1 `S2.SS5 — 2.5. Formal Methods Foundations`；该机制由 `AGENT-PLATFORM` 承载。原文定位摘录仅作核对：2.5. Formal Methods Foundations Our framework synthesizes five established formal methods traditions. Dolev–Yao model. Dolev and Yao (Dolev and Yao, 1983) introduced the standard symbolic attacker model for security protocol analysis. The attacker controls the network and can intercept, inject, synthesize (construct new messages from known components), and decompose (extract components from messages) messages. Cervesato (Cervesato, 2001) proved that the DY intruder is the most powerful attacker in the symbolic mode

Evaluation contract：证明与工具实验只覆盖公开 threat model 和规则；不能证明未命中的 Skill 安全。 exact-v1 定位为 `S9 — 9. Evaluation`；用于核对的原文摘录：9. Evaluation We evaluate SkillFortify across seven experiments designed to test each formal contribution. All experiments use SkillFortifyBench, a purpose-built benchmark of 540 agent skills with ground-truth security labels. 9.1. SkillFortifyBench SkillFortifyBench is a controlled benchmark containing 540 agent skills: 270 malicious and 270 benign. Skills are evenly distributed across the three supported formats: 180 Claude Code skills, 180 MCP server configurations, and 180 OpenClaw manifests. Within each format

证明与未证明：证据只支持上述 paper-specific workload 内的机制/测量关系；不支持把作者结果外推为其他模型、数据、硬件、精度、长度、batch、并发或 production SLO 的通用结论。

Trade-off、failure 与共存边界：更强 admission 减少供应链风险，却提高发布摩擦并可能误拒；低风险、本地、只读 Skill 可使用更轻检查。 反证/限制定位为 `S11.SS1 — 11.1. Limitations`；用于核对的原文摘录：11.1. Limitations While SkillFortify achieves strong results across all evaluation experiments, several limitations warrant discussion. Typosquatting and Dependency Confusion. Attack types A11 (typosquatting) and A12 (dependency confusion) achieve 50% and 0% detection rates, respectively. Both attack classes are fundamentally relational—they require comparison against an external corpus of legitimate skill names and

Artifact / implementation：exact-v1 `S8 — 8. Implementation`；公开范围摘录：8. Implementation We implement the formal framework described in Sections 3–7 as SkillFortify, an open-source Python tool for agent skill supply chain security. This section describes the system architecture, supported skill formats, command-line interface, and engineering quality measures. 8.1. Architecture SkillFortify is organized around three core engine。未公开的代码、commit、部署配置或复现实验不得由论文叙事反推。

<!-- claim:SF-2026-ARXIV-2603-00195:start -->只接受 arXiv:2603.00195v1 在 exact-v1 公开 workload 下的作者机制与实验主张；未披露的 model、hardware、precision、length、batch、concurrency、cost 与 production SLO 均为 Not Disclosed，不外推为通用结论。<!-- claim:SF-2026-ARXIV-2603-00195:end -->

Books Comparison：已读 `AGENT-PLATFORM` 的 `books/part-07-agent/84-agent-platform.md#Skill Drift 应检测角色契约，而不是任意变化 (line 787)` 及相邻 `books/part-07-agent/83-mcp.md#本章要回答的问题 (line 10)`；现有命题为“契约级监控减少无关告警，却把 contract extractor、probe 和 live-condition source 变成新的可信组件；文档遗漏或角色抽取错误会造成漏报。无法建立可靠契约时，应保留 pinned dependency、canary execution、人工 review 与失败后回滚，而不能因为版本字符串未变就宣称 skill 可用。[受限证据：arXiv:2605.10990v1]”。Decision=`No Change — Existing Coverage`；该 author-side 判断仍待fresh-context Books reviewer，Integrate 项只进入日期队列。
<!-- review:SF-2026-ARXIV-2603-00195:end -->

<!-- review:SF-2026-ARXIV-2603-00196:start -->
#### Your Inference Request Will Become a Black Box: Confidential Inference for Cloud-based Large Language Models

问题与 changed constraint：云端 LLM 推理需要隐藏 prompt、权重和中间状态，但把整个 runtime 放进可信执行环境会扩大 TCB 并引入内存与性能压力。

旧路径为何合理：在该约束未出现、规模较小或 workload 更稳定时，论文所比较的旧路径仍以更少状态、更短控制链和更成熟实现提供合理基线；不能因本论文出现而静默覆盖。

机制、state/data/control owner：论文把 confidential inference 分解为隔离边界、远程证明、加密通道和可验证 runtime 组成，明确哪些请求状态由 enclave/guest、host 与客户端分别拥有。 对应 exact-v1 `A2 — Appendix B Additional Method Details`；该机制由 `PLATFORM-SECURITY` 承载。原文定位摘录仅作核对：Appendix B Additional Method Details B.1 Pseudocode Implementation The confidential inference process of Talaria is described as Alg. 1. Algorithm 1 Pseudocode of Talaria. Input: client prompt . Output: model response. Phase 1: One-time setup Initialize [CVM] [Cloud] Phase 2: Decoding while do Initialize [CVM] [CVM] [CVM] [CVM] for to do [CVM] [Cloud] [CVM] [CVM] end for [CVM] end while B.2 Theoretical Analysis of Def. 1 This section provides a theoretical foundation for Def. 1, which establishes the privacy guaran

Evaluation contract：实验只证明其原型配置下的隔离和开销；未证明云提供方所有 side channel 被消除，也未证明不同 GPU/TEE 组合具有同一性能。 exact-v1 定位为 `A3 — Appendix C Additional Evaluations`；用于核对的原文摘录：Appendix C Additional Evaluations C.1 Detailed Evaluation Setup C.1.1 Datasets We use four representative datasets in our experiments: • Midjourney prompts AI (2024) is a dataset containing 246,381 natural language prompts for text-to-image service. • WikiText-2 Merity et al. (2017) contains over 100 million tokens extracted from high-quality, curated Wikipedia articles. • Patient-notes Ha et al. (2022) is a dataset containing 40,000 patient note history portions. • GPT-OSS20B-samples Morris (2025) dataset is a col

证明与未证明：证据只支持上述 paper-specific workload 内的机制/测量关系；不支持把作者结果外推为其他模型、数据、硬件、精度、长度、batch、并发或 production SLO 的通用结论。

Trade-off、failure 与共存边界：机密性换来证明链、密钥生命周期和受限设备支持；failure 包括证明过期、I/O 泄露和 TCB 漏洞。可信私有集群仍可能比复杂 TEE 路径更合理。 反证/限制定位为 `Sx1 — Limitations`；用于核对的原文摘录：Limitations The limitations of this work mainly include the following two aspects: Threat Scenario. We adopt the standard honest-but-curious setting: the cloud provider executes the protocol correctly but may analyze observed artifacts to infer private information. This assumption is reasonable for cloud LLM services because ① providers are economically and reputationally incentivized to follow deployed protocols, ma

Artifact / implementation：exact-v1 `A2.SS1 — B.1 Pseudocode Implementation`；公开范围摘录：B.1 Pseudocode Implementation The confidential inference process of Talaria is described as Alg. 1. Algorithm 1 Pseudocode of Talaria. Input: client prompt . Output: model response. Phase 1: One-time setup Initialize [CVM] [Cloud] Phase 2: Decoding while do Initialize [CVM] [CVM] [CVM] [CVM] for to do [CVM] [Cloud] [CVM] [CVM] end for [CVM] end while。未公开的代码、commit、部署配置或复现实验不得由论文叙事反推。

<!-- claim:SF-2026-ARXIV-2603-00196:start -->只接受 arXiv:2603.00196v1 在 exact-v1 公开 workload 下的作者机制与实验主张；未披露的 model、hardware、precision、length、batch、concurrency、cost 与 production SLO 均为 Not Disclosed，不外推为通用结论。<!-- claim:SF-2026-ARXIV-2603-00196:end -->

Books Comparison：已读 `PLATFORM-SECURITY` 的 `books/part-06-ai-infrastructure/72-security.md#风险管理而不是一次性认证 (line 1131)` 及相邻 `books/part-06-ai-infrastructure/71-multi-tenant.md#本章要回答的问题 (line 10); books/part-06-ai-infrastructure/73-production-best-practice.md#本章要回答的问题 (line 10)`；现有命题为“即使原始输入留在 client，split inference 仍会把 intermediate activation 暴露给 server。旧的“在本地跑前几层即可隐藏输入”只在 activation 对攻击者确实不可逆、split point 与模型固定时成立；server-visible tensor、layer identity、shape/precision 和 auxiliary knowledge 变化后，activation matching/inversion 可以把中间状态重新关联到输入。client 拥有原文与允许的 split policy，server runtime 只拥有执行所需 activation，security plane 则必须测试每个候选 split point 的可重建性并记录 attacker capability。更深本地计算或 activation protection 能降低暴露，却增加 client compute、带宽、精度损失与部署复杂度；风险无法校准时回退本地完整推理、TEE/MPC 或可信服务端。`arXiv:2605.23158v1` 的 §3、§4.1 至 §”。Decision=`No Change — Existing Coverage`；该 author-side 判断仍待fresh-context Books reviewer，Integrate 项只进入日期队列。
<!-- review:SF-2026-ARXIV-2603-00196:end -->

<!-- review:SF-2026-ARXIV-2603-00356:start -->
#### Token Management in Multi-Tenant AI Inference Platforms

问题与 changed constraint：多租户推理中，token 数不是只用于计费的结果量；prefill、decode、KV residency 与 deadline 让 token 成为调度前必须管理的资源单位。

旧路径为何合理：在该约束未出现、规模较小或 workload 更稳定时，论文所比较的旧路径仍以更少状态、更短控制链和更成熟实现提供合理基线；不能因本论文出现而静默覆盖。

机制、state/data/control owner：论文把 token budget、admission、运行中配额与 reclaim 连接起来，使平台在请求进入和执行期间都能控制 token 责任，而非只按 request count 排队。 对应 exact-v1 `S4 — 4. System Architecture`；该机制由 `INFER-SCHEDULING` 承载。原文定位摘录仅作核对：4. System Architecture Having defined the resource model and priority mechanism, we now describe how these abstractions are realized in a Kubernetes-native architecture. Figure 1 illustrates the system components and their interactions. The central architectural challenge is bridging two resource models: token pools allocate capacity in inference-native units, while Kubernetes schedules containers to nodes based on CPU, memory, and extended resources. We resolve this through virtual nodes: synthetic node objects th

Evaluation contract：作者评估其 workload 下的隔离、利用率与尾延迟；证据支持 token-aware policy 的局部收益，不证明同一策略跨模型、长度分布和硬件均占优。 exact-v1 定位为 `S5.SS3 — 5.3. Experiment 2: SLO-Aware Fair Share`；用于核对的原文摘录：5.3. Experiment 2: SLO-Aware Fair Share Scenario: “A GPU node fails during peak hours. Two production services share the surviving capacity: a latency-critical coding assistant and a batch synthetic data pipeline. After recovery, an analytics report generator joins to diagnose what occurred.” Three elastic entitlements participate: elastic-copilot (5 slots, 500ms SLO) is a developer coding assistant requiring fast responses; elastic-synth (5 slots, 30s SLO) is a batch synthetic data pipeline tolerant of delay; and

证明与未证明：证据只支持上述 paper-specific workload 内的机制/测量关系；不支持把作者结果外推为其他模型、数据、硬件、精度、长度、batch、并发或 production SLO 的通用结论。

Trade-off、failure 与共存边界：更细粒度控制可降低 noisy-neighbor，但需要在线估算未来 token 与 KV 占用；低估会破坏 SLO，高估会浪费容量。稳定、同质 workload 仍可用简单队列。 反证/限制定位为 `S6.SS0.SSS0.Px3 — Limitations.`；用于核对的原文摘录：Limitations. Experiments use a single vLLM replica; production deployments would involve multiple replicas and cross-replica coordination for pool-level state. The three-resource model assumes colocated prefill and decode; extending to disaggregated architectures would require phase-specific capacity terms and accounting for KV cache transfer bandwidth. Formal convergence analysis of the debt mechanism under arbitrar

Artifact / implementation：exact-v1 `S5.SS1 — 5.1. Experimental Setup`；公开范围摘录：5.1. Experimental Setup Experiments run on a single-node cluster with one vLLM (Kwon et al., 2023) replica serving nvidia/Qwen3-8B-NVFP4, providing capacity for 16 concurrent sequences (hereafter “slots”) at a total throughput of roughly 240 tokens/sec. We use a constrained setup on a DGX Spark for several reasons. First, token pools operate at the admission。未公开的代码、commit、部署配置或复现实验不得由论文叙事反推。

<!-- claim:SF-2026-ARXIV-2603-00356:start -->只接受 arXiv:2603.00356v1 在 exact-v1 公开 workload 下的作者机制与实验主张；未披露的 model、hardware、precision、length、batch、concurrency、cost 与 production SLO 均为 Not Disclosed，不外推为通用结论。<!-- claim:SF-2026-ARXIV-2603-00356:end -->

Books Comparison：已读 `INFER-SCHEDULING` 的 `books/part-05-inference-system/56-inference-scheduling.md#从逐配置压测到校准后的配置搜索 (line 581)` 及相邻 `books/part-05-inference-system/55-pd-disaggregation.md#本章要回答的问题 (line 10); books/part-06-ai-infrastructure/57-what-is-ai-platform.md#本章要回答的问题 (line 10)`；现有命题为“Replica 已固定时，scheduler 只需在同构候选中 placement；边缘设备、精度容忍和带宽差异同时出现后，请求真正选择的是 `(model family, size, quantization, device)`。先为 accuracy、latency、resource 与 response size 建立版本化预测，再在 request tolerance、capacity、bandwidth、concurrency 与 deadline 下联合 admission，可以避免把一个质量不满足的快速配置误当可行解。”。Decision=`Integrate`；该 author-side 判断仍待fresh-context Books reviewer，Integrate 项只进入日期队列。
<!-- review:SF-2026-ARXIV-2603-00356:end -->

<!-- review:SF-2026-ARXIV-2603-00357:start -->
#### SPARe: Stacked Parallelism with Adaptive Reordering for Fault-Tolerant LLM Pretraining Systems with 100k+ GPUs

问题与 changed constraint：十万 GPU 训练中 fail-stop 已从偶发异常变成常态，整作业 checkpoint-restart 的重放时间会主导 wall clock。

旧路径为何合理：在该约束未出现、规模较小或 workload 更稳定时，论文所比较的旧路径仍以更少状态、更短控制链和更成熟实现提供合理基线；不能因本论文出现而静默覆盖。

机制、state/data/control owner：SPARe 叠加并行冗余与故障后的 adaptive reordering，把 surviving work、replacement 和恢复顺序交给运行时而非整作业重启。 对应 exact-v1 `https://arxiv.org/html/2603.00357v1#S3 — exact-v1 §3 SPARe: Stacked Parallelism with Adaptive Reordering (Method)`；该机制由 `TRAIN-CHECKPOINT` 承载。原文定位摘录仅作核对：Not Disclosed

Evaluation contract：模拟/集群实验只支持所测故障率、模型和拓扑；不覆盖 silent corruption 或相关机架故障。 exact-v1 定位为 `S5 — 5 System Performance Evaluation`；用于核对的原文摘录：5 System Performance Evaluation Figure 6: Time-to-train of SPARe+CKPT / Rep+CKPT from simulation and (7) for (a) , (b) , (c) . Figure 7: Availability of SPARe+CKPT from simulation and (2) for (a) , (b) , (c) Figure 8: Average Computation Overhead of SPARe from simulation and (5) for (a) , (b) , (c) This section evaluates the performance of SPARe via a solid discrete-event simulation developed based on SimGrid (Casanova et al., 2013) – a state-of-the-art distributed/parallel computing system simulator that facilitat

证明与未证明：证据只支持上述 paper-specific workload 内的机制/测量关系；不支持把作者结果外推为其他模型、数据、硬件、精度、长度、batch、并发或 production SLO 的通用结论。

Trade-off、failure 与共存边界：更小 rollback 换来冗余 capacity、状态映射和复杂调度；故障稀少或规模较小时 durable checkpoint-restart 仍最清楚。 反证/限制定位为 `S6 — 6 Conclusion`；用于核对的原文摘录：6 Conclusion In this work, we have introduced SPARe: Stacked Parallelism with Adaptive Reordering, which masks failures as many as traditional replication yet keeps the computation overhead as low as even for high redundancies. SPARe achieves substantially smaller time-to-train compared to traditional replication baseline, lower according to our realistic SimGrid-based discrete event simulations, at the harsh restart

Artifact / implementation：exact-v1 `Not Disclosed — arXiv:2603.00357v1 exposes no dedicated Artifact / implementation section in the recovered exact-v1 body`；公开范围摘录：Not Disclosed。未公开的代码、commit、部署配置或复现实验不得由论文叙事反推。

<!-- claim:SF-2026-ARXIV-2603-00357:start -->只接受 arXiv:2603.00357v1 在 exact-v1 公开 workload 下的作者机制与实验主张；未披露的 model、hardware、precision、length、batch、concurrency、cost 与 production SLO 均为 Not Disclosed，不外推为通用结论。<!-- claim:SF-2026-ARXIV-2603-00357:end -->

Books Comparison：已读 `TRAIN-CHECKPOINT` 的 `books/part-04-training-system/35-checkpoint.md#异步保存移动了 Pause，而没有删除 IO (line 250)` 及相邻 `books/part-04-training-system/34-dpo.md#本章要回答的问题 (line 10); books/part-04-training-system/36-distributed-training.md#本章要回答的问题 (line 10)`；现有命题为“→ coalesce fragmented tensor shards; serialize only objects that require it”。Decision=`No Change — Existing Coverage`；该 author-side 判断仍待fresh-context Books reviewer，Integrate 项只进入日期队列。
<!-- review:SF-2026-ARXIV-2603-00357:end -->

<!-- review:SF-2026-ARXIV-2603-00495:start -->
#### AI Runtime Infrastructure

问题与 changed constraint：AI workload 同时包含模型执行、数据移动、隔离、可观测和控制面；把它当普通容器会丢失 accelerator 与 model-state contract。

旧路径为何合理：在该约束未出现、规模较小或 workload 更稳定时，论文所比较的旧路径仍以更少状态、更短控制链和更成熟实现提供合理基线；不能因本论文出现而静默覆盖。

机制、state/data/control owner：AI Runtime Infrastructure 将模型 artifact、执行计划、device runtime 和 platform control 分层，显式化跨层接口而不是把所有责任塞进框架。 对应 exact-v1 `S4 — 4 Design Principles for AI Runtime Infrastructure`；该机制由 `PLATFORM-FOUNDATIONS` 承载。原文定位摘录仅作核对：4 Design Principles for AI Runtime Infrastructure AI runtime infrastructure introduces a distinct set of design requirements that differ from those of model serving systems, orchestration frameworks, and observability tooling. To clarify what constitutes effective runtime infrastructure for agentic systems, we outline a set of core design principles. These principles are not tied to specific implementations, but instead characterize the essential properties required for execution-time oversight and control. 4.1 Exe

Evaluation contract：论文的架构与案例证明这种责任分解可表达现有 runtime；没有统一 benchmark 证明其抽象在所有平台上最优。 exact-v1 定位为 `S7.SS3 — 7.3 Evaluation Beyond Post-Hoc Metrics`；用于核对的原文摘录：7.3 Evaluation Beyond Post-Hoc Metrics The presence of an execution-time control layer also motivates new approaches to evaluating agentic systems. Traditional metrics that summarize outcomes after execution may fail to capture the benefits of runtime intervention, such as avoided failures or reduced recovery costs. Future evaluation frameworks may need to account for execution trajectories, intervention timing, and counterfactual outcomes enabled by runtime infrastructure.

证明与未证明：证据只支持上述 paper-specific workload 内的机制/测量关系；不支持把作者结果外推为其他模型、数据、硬件、精度、长度、batch、并发或 production SLO 的通用结论。

Trade-off、failure 与共存边界：清晰接口改善替换与治理，但增加版本兼容和跨层协调；小规模单框架部署仍可能不需要完整 runtime layer。 反证/限制定位为 `S8 — 8 Conclusion`；用于核对的原文摘录：8 Conclusion Agentic AI systems increasingly operate over long horizons, interact with external environments, and must satisfy constraints on reliability, efficiency, and safety during execution. While existing infrastructure addresses model execution, orchestration, observability, and post-hoc evaluation, these components do not provide execution-time control over agent behavior. As a result, many critical failure m

Artifact / implementation：exact-v1 `Not Disclosed — arXiv:2603.00495v1 exposes no dedicated Artifact / implementation section in the recovered exact-v1 body`；公开范围摘录：Not Disclosed。未公开的代码、commit、部署配置或复现实验不得由论文叙事反推。

<!-- claim:SF-2026-ARXIV-2603-00495:start -->只接受 arXiv:2603.00495v1 在 exact-v1 公开 workload 下的作者机制与实验主张；未披露的 model、hardware、precision、length、batch、concurrency、cost 与 production SLO 均为 Not Disclosed，不外推为通用结论。<!-- claim:SF-2026-ARXIV-2603-00495:end -->

Books Comparison：已读 `PLATFORM-FOUNDATIONS` 的 `books/part-06-ai-infrastructure/57-what-is-ai-platform.md#本章在知识树中的位置 (line 152)` 及相邻 `books/part-05-inference-system/56-inference-scheduling.md#本章要回答的问题 (line 10); books/part-06-ai-infrastructure/58-kubeflow.md#本章要回答的问题 (line 10)`；现有命题为“Part VII Agent runtime and action governance”。Decision=`No Change — Existing Coverage`；该 author-side 判断仍待fresh-context Books reviewer，Integrate 项只进入日期队列。
<!-- review:SF-2026-ARXIV-2603-00495:end -->

<!-- review:SF-2026-ARXIV-2603-00575:start -->
#### SWE-Hub: A Unified Production System for Scalable, Executable Software Engineering Tasks

问题与 changed constraint：软件工程 Agent 的训练与评估受制于不可复现环境、昂贵真实 bug 和跨语言执行差异，静态补丁集不能作为系统级证据。

旧路径为何合理：在该约束未出现、规模较小或 workload 更稳定时，论文所比较的旧路径仍以更少状态、更短控制链和更成熟实现提供合理基线；不能因本论文出现而静默覆盖。

机制、state/data/control owner：SWE-Hub 把 repository、环境构建、任务合成、执行验证和规模化调度组织成统一生产流水，使 executable task 成为版本化资产。 对应 exact-v1 `S3.SS2 — 3.2 Architecture`；该机制由 `AGENT-PLATFORM` 承载。原文定位摘录仅作核对：3.2 Architecture Overview. SWE-Hub is composed of an execution substrate layer and multiple task product lines (Figure 1). The substrate layer guarantees that a repository is runnable and testable in a deterministic way, while the product lines generate task instances by transforming repositories and validating outcomes through execution. Execution substrate: Env Agent. Given a repository snapshot, the Env Agent automatically constructs: (i) a versioned container image capturing toolchains and dependencies, and (ii

Evaluation contract：系统结果证明作者数据/环境集合的构建与执行能力；不证明合成 bug 等价于生产缺陷。 exact-v1 定位为 `S2.SS1 — 2.1 Execution Substrates and Reproducible Evaluation Harnesses`；用于核对的原文摘录：2.1 Execution Substrates and Reproducible Evaluation Harnesses A significant body of recent literature evaluates repository-level agents using containerized harnesses that standardize dependency installation, test invocation, and outcome collection. SWE-bench (Jimenez et al., 2024) pioneered the issue-resolution setting over real GitHub repositories, providing a Docker-based harness for reproducible evaluation. Subsequent efforts have further emphasized robustness and expanded coverage, including SWE-bench Verified

证明与未证明：证据只支持上述 paper-specific workload 内的机制/测量关系；不支持把作者结果外推为其他模型、数据、硬件、精度、长度、batch、并发或 production SLO 的通用结论。

Trade-off、failure 与共存边界：可执行规模换来容器构建成本、环境漂移和合成偏差；少量高价值真实 issue 仍需要人工维护。 反证/限制定位为 `S5.SS7 — 5.7 Discussion: Quality, Triviality, and System-Level Limitations`；用于核对的原文摘录：5.7 Discussion: Quality, Triviality, and System-Level Limitations Execution-based filtering ensures instances are active, but activeness is insufficient for high-quality data: trivial mutations (e.g., flipping a comparison) satisfy validity criteria yet offer limited learning signal. Moreover, entity-local transformations are inherently biased toward localized failures, failing to capture system-level regressions whe

Artifact / implementation：exact-v1 `Not Disclosed — arXiv:2603.00575v1 exposes no dedicated Artifact / implementation section in the recovered exact-v1 body`；公开范围摘录：Not Disclosed。未公开的代码、commit、部署配置或复现实验不得由论文叙事反推。

<!-- claim:SF-2026-ARXIV-2603-00575:start -->只接受 arXiv:2603.00575v1 在 exact-v1 公开 workload 下的作者机制与实验主张；未披露的 model、hardware、precision、length、batch、concurrency、cost 与 production SLO 均为 Not Disclosed，不外推为通用结论。<!-- claim:SF-2026-ARXIV-2603-00575:end -->

Books Comparison：已读 `AGENT-PLATFORM` 的 `books/part-07-agent/84-agent-platform.md#Evaluation 从答案扩展到 Trajectory (line 580)` 及相邻 `books/part-07-agent/83-mcp.md#本章要回答的问题 (line 10)`；现有命题为“Evaluation environment 要隔离真实副作用，并记录 model/tool/index versions。Benchmark score 不自动代表 production workload；AgentBench、SWE-bench 等提供任务入口，也暴露 long-horizon evaluation、environment leakage 和 verifier quality 的困难。”。Decision=`No Change — Existing Coverage`；该 author-side 判断仍待fresh-context Books reviewer，Integrate 项只进入日期队列。
<!-- review:SF-2026-ARXIV-2603-00575:end -->

<!-- review:SF-2026-ARXIV-2603-00811:start -->
#### Curation Leaks: Membership Inference Attacks against Data Curation for Machine Learning

问题与 changed constraint：数据 curation 本身会暴露样本是否被选择；只保护训练后模型并不能隐藏过滤、去重或质量排序的成员信息。

旧路径为何合理：在该约束未出现、规模较小或 workload 更稳定时，论文所比较的旧路径仍以更少状态、更短控制链和更成熟实现提供合理基线；不能因本论文出现而静默覆盖。

机制、state/data/control owner：Curation Leaks 将攻击目标从 training membership 扩展到 selection membership，并沿 curator 输出和模型行为测量选择决策泄露。 对应 exact-v1 `A1 — Appendix A Curation Methods`；该机制由 `TRAIN-DATA` 承载。原文定位摘录仅作核对：Appendix A Curation Methods Table 2: Overview of Curation Methods Method Description Score Function Image-based Identifies relevant pool data using image embeddings where is the embedding function TRAK Computes attribution scores via projected gradients to identify influential pool samples where are projected and out-to-loss-scaled features A.1 Image-Based Scoring We employ Image-based nearest neighbor distances inspired by Gadre et al. (2023). Following the DataComp methodology, we use embeddings from OpenAI’s pre

Evaluation contract：攻击在作者的数据、curator 和 threat model 下成立；没有证明所有 curation pipeline 都同等泄露，也未给出完整生产缓解成本。 exact-v1 定位为 `A5 — Appendix E Extended Evaluation`；用于核对的原文摘录：Appendix E Extended Evaluation E.1 Image-based Scoring Attacks We show the results of the attack on Image-based scoring in Figure 17. LiRA exhibits strong and consistent performance across all datasets. The custom attack is better for all datasets at FPR . For lower FPRs, performance is highly variable. Figure 18 shows the results of the attack on Image-based scoring without access to the scores. The custom attack and LiRA achieve similar results, with the custom attack being slightly more successful in the low FPR

证明与未证明：证据只支持上述 paper-specific workload 内的机制/测量关系；不支持把作者结果外推为其他模型、数据、硬件、精度、长度、batch、并发或 production SLO 的通用结论。

Trade-off、failure 与共存边界：增强选择隐私可能降低可解释性、质量控制或增加随机化；公开数据流水线仍可优先透明性而非 selection secrecy。 反证/限制定位为 `S6 — 6 Discussion and Conclusion`；用于核对的原文摘录：6 Discussion and Conclusion Our work demonstrates that data curation pipelines can leak membership information about the target datasets, exposing privacy risks at every stage, from curation scores and curated subset to the final trained model. Image-based nearest-neighbor methods are particularly vulnerable, and even state-of-the-art approaches like TRAK expose privacy risks for small target sets. Our discovered ris

Artifact / implementation：exact-v1 `Sx3 — Reproducibility Statement`；公开范围摘录：Reproducibility Statement Reproducing our results is possible from the information provided, and we support reproduction through the release of all our attack implementations in the supplemental code, as well as providing more detail on the algorithms in the appendix. What hinders reproduction is the computational cost associated with running curation and tr。未公开的代码、commit、部署配置或复现实验不得由论文叙事反推。

<!-- claim:SF-2026-ARXIV-2603-00811:start -->只接受 arXiv:2603.00811v1 在 exact-v1 公开 workload 下的作者机制与实验主张；未披露的 model、hardware、precision、length、batch、concurrency、cost 与 production SLO 均为 Not Disclosed，不外推为通用结论。<!-- claim:SF-2026-ARXIV-2603-00811:end -->

Books Comparison：已读 `TRAIN-DATA` 的 `books/part-04-training-system/27-data.md#Quality filtering 在过滤什么 (line 262)` 及相邻 `books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#本章要回答的问题 (line 10); books/part-04-training-system/28-pretraining.md#本章要回答的问题 (line 10)`；现有命题为“-> verify final state against original constraints”。Decision=`No Change — Existing Coverage`；该 author-side 判断仍待fresh-context Books reviewer，Integrate 项只进入日期队列。
<!-- review:SF-2026-ARXIV-2603-00811:end -->

<!-- review:SF-2026-ARXIV-2603-01209:start -->
#### Agents Learn Their Runtime: Interpreter Persistence as Training-Time Semantics

问题与 changed constraint：Agent 训练若每个 episode 重置 interpreter，而部署保留进程、文件和缓存，policy 学到的是错误的 runtime semantics。

旧路径为何合理：在该约束未出现、规模较小或 workload 更稳定时，论文所比较的旧路径仍以更少状态、更短控制链和更成熟实现提供合理基线；不能因本论文出现而静默覆盖。

机制、state/data/control owner：论文把 interpreter persistence 作为训练环境状态的一部分，使跨 turn 的变量、artifact 与副作用与部署执行合同一致。 对应 exact-v1 `S3 — 3 Methodology`；该机制由 `AGENT-PLATFORM` 承载。原文定位摘录仅作核对：3 Methodology Figure 1: Interpreter persistence as an execution semantic for tool-augmented agents. (Top) Opaque Knapsack hides item attributes and feasibility constraints behind a budgeted tool API, forcing multi-turn inspection and plan revision rather than a single one-shot script. (Bottom) Example rollout for the same task instance under two deployment runtimes. With a persistent interpreter (left), variables defined by earlier actions remain live and the agent can accumulate and reuse executable state across t

Evaluation contract：实验比较持久/非持久 runtime 下的 agent 行为；只证明所用 CodeAct 环境，不能外推所有工具和 sandbox。 exact-v1 定位为 `S4 — 4 Empirical Study: Opaque Knapsack Experiments`；用于核对的原文摘录：4 Empirical Study: Opaque Knapsack Experiments We provide an empirical validation designed to isolate the role of state persistence in multi-step interleaved reasoning under partial observability. 4.1 Experimental Setup This section details the end-to-end experimental pipeline designed to isolate and evaluate the role of execution semantics. We outline the procedural generation of the task splits and teacher trajectories, followed by the specific hyperparameter configurations for model fine-tuning and the infrastru

证明与未证明：证据只支持上述 paper-specific workload 内的机制/测量关系；不支持把作者结果外推为其他模型、数据、硬件、精度、长度、batch、并发或 production SLO 的通用结论。

Trade-off、failure 与共存边界：语义对齐提高长任务能力，但扩大状态污染、泄密和不可复现风险；无跨步依赖的任务仍应使用 ephemeral execution。 反证/限制定位为 `S5 — 5 Discussion`；用于核对的原文摘录：5 Discussion Our results support a practical claim: Execution semantics observed during training shape how a tool-augmented agent learns to use the interpreter at deployment. In a controlled cross-evaluation (training semantics runtime semantics; Table 2), models adapt their state management strategy to the persistence contract embedded in their fine-tuning traces. When the deployment runtime exposes a persistent int

Artifact / implementation：exact-v1 `A2 — Appendix B Agent Implementation`；公开范围摘录：Appendix B Agent Implementation To generate valid trajectories interleaving reasoning and executable actions, we implemented a custom CodeAct-style agent loop. This appendix documents the execution contract, runtime alignment across regimes, and the exact system prompts used in the experiments. B.1 Execution Flow and Turn Structure Each episode follows a str。未公开的代码、commit、部署配置或复现实验不得由论文叙事反推。

<!-- claim:SF-2026-ARXIV-2603-01209:start -->只接受 arXiv:2603.01209v1 在 exact-v1 公开 workload 下的作者机制与实验主张；未披露的 model、hardware、precision、length、batch、concurrency、cost 与 production SLO 均为 Not Disclosed，不外推为通用结论。<!-- claim:SF-2026-ARXIV-2603-01209:end -->

Books Comparison：已读 `AGENT-PLATFORM` 的 `books/part-07-agent/84-agent-platform.md#Scheduling 不只是 GPU (line 471)` 及相邻 `books/part-07-agent/83-mcp.md#本章要回答的问题 (line 10)`；现有命题为“/ Agent runtime / ready steps、tools、approvals、deadlines /”。Decision=`No Change — Existing Coverage`；该 author-side 判断仍待fresh-context Books reviewer，Integrate 项只进入日期队列。
<!-- review:SF-2026-ARXIV-2603-01209:end -->

<!-- review:SF-2026-ARXIV-2603-01630:start -->
#### SEED-SET: Scalable Evolving Experimental Design for System-level Ethical Testing

问题与 changed constraint：系统级伦理测试若只列原则或静态问题集，无法随模型、工具、用户和环境演进而保持覆盖。

旧路径为何合理：在该约束未出现、规模较小或 workload 更稳定时，论文所比较的旧路径仍以更少状态、更短控制链和更成熟实现提供合理基线；不能因本论文出现而静默覆盖。

机制、state/data/control owner：SEED-SET 将风险假设、场景生成、实验执行和失败归档组成可演进测试资产，令伦理声明绑定版本化 evidence。 对应 exact-v1 `A1.SS2 — A.2 Variational Bayesian methods:overview`；该机制由 `PLATFORM-EVALUATION-SYSTEM` 承载。原文定位摘录仅作核对：A.2 Variational Bayesian methods:overview In variational inference, the posterior distribution over a set of unobserved variables given some data is approximated by a so-called variational distribution : . Variational Bayesian methods are a family of techniques for efficient posterior approximation in Bayesian inference. In variational inference, the posterior distribution over a set of unobserved variables given some data is approximated by a so-called variational distribution : . The distribution is restricted to

Evaluation contract：论文展示方法与案例，不证明其场景空间完备或 evaluator 无偏。 exact-v1 定位为 `S5 — 5 Experiments`；用于核对的原文摘录：5 Experiments Figure 2: Environments for the two case studies considered in this work. (Left) Power Grid Allocation - IEEE 5-Bus and 30-Bus ( Section 5.1). (Right) Fire Rescue ( Section 5.2). Additional case study for Optimal Routing in Appendix E. Our central hypothesis is that SEED-SET enables scalable, accurate, and data-efficient ethical evaluation of autonomous systems. Using previously discussed ethical evaluation concerns (Battistuzzi et al., 2021; Luo et al., 2024; Bieler et al., 2024) to guide the design o

证明与未证明：证据只支持上述 paper-specific workload 内的机制/测量关系；不支持把作者结果外推为其他模型、数据、硬件、精度、长度、batch、并发或 production SLO 的通用结论。

Trade-off、failure 与共存边界：持续扩展覆盖换来治理成本和情景生成偏差；稳定低风险组件仍可使用固定回归集。 反证/限制定位为 `S6 — 6 Limitations`；用于核对的原文摘录：6 Limitations While the SEED-SET framework effectively mitigates common challenges associated with ethical assessment, certain limitations remain, along with promising future directions. Scalability for Extremely Large Datasets. Using sparse variational GPs reduces complexity from to with inducing points, enabling SEED-SET to handle tens of thousands of observations. Scaling to hundreds of thousands or more remains c

Artifact / implementation：exact-v1 `A2.SS0.SSS1 — B.0.1 System Setup`；公开范围摘录：B.0.1 System Setup The testbed is the standard IEEE 5/30-bus network, a widely used benchmark in power system studies. We consider a variety of DER placement and sizing configurations, each representing a distinct design candidate. For each configuration, an AC OPF is solved using the pandapower library to compute physical network states under steady-state c。未公开的代码、commit、部署配置或复现实验不得由论文叙事反推。

<!-- claim:SF-2026-ARXIV-2603-01630:start -->只接受 arXiv:2603.01630v1 在 exact-v1 公开 workload 下的作者机制与实验主张；未披露的 model、hardware、precision、length、batch、concurrency、cost 与 production SLO 均为 Not Disclosed，不外推为通用结论。<!-- claim:SF-2026-ARXIV-2603-01630:end -->

Books Comparison：已读 `PLATFORM-EVALUATION-SYSTEM` 的 `books/part-06-ai-infrastructure/66-evaluation-system.md#从答案评分到可执行证据 (line 936)` 及相邻 `books/part-06-ai-infrastructure/65-kai-scheduler.md#本章要回答的问题 (line 10); books/part-06-ai-infrastructure/67-monitoring.md#本章要回答的问题 (line 10)`；现有命题为“- `SF-2026-ARXIV-2606-21869` — primary `arXiv:2606.21869v1`；exact-v1 URL=`https://arxiv.org/html/2606.21869v1`；Method=`https://arxiv.org/html/2606.21869v1 — §3 Preliminaries — Energy Consumption and Measurement; Multilingual Dataset`；Evaluation=`https://arxiv.org/html/2606.21869v1 — §4 Results and Analysis — Common Setup; §4.1–§4.4; Appendix B Experimental Setups`；Non-proof=`https://arxiv.org/html/2606.21869v1 — §6 Conclusion; Environmental impact of this study; Translation quality and representation; Recommendatio”。Decision=`No Change — Existing Coverage`；该 author-side 判断仍待fresh-context Books reviewer，Integrate 项只进入日期队列。
<!-- review:SF-2026-ARXIV-2603-01630:end -->

<!-- review:SF-2026-ARXIV-2603-02176:start -->
#### Organizing, Orchestrating, and Benchmarking Agent Skills at Ecosystem Scale

问题与 changed constraint：Skill 数量扩张后，flat registry 与一次检索无法同时解决发现、组合和质量退化。

旧路径为何合理：在该约束未出现、规模较小或 workload 更稳定时，论文所比较的旧路径仍以更少状态、更短控制链和更成熟实现提供合理基线；不能因本论文出现而静默覆盖。

机制、state/data/control owner：AgentSkillOS 先构建 capability tree 管理 Skill，再用 DAG 选择和编排多 Skill，把生态索引与任务执行分为两个状态阶段。 对应 exact-v1 `S2 — 2 Method`；该机制由 `AGENT-PLATFORM` 承载。原文定位摘录仅作核对：2 Method In this section, we present AgentSkillOS, the first principled framework for efficiently selecting, orchestrating, and managing skills from a large-scale ecosystem to solve a user-specified task. AgentSkillOS comprises two stages: (i) Manage Skills, which organizes a large-scale skill ecosystem into a capability tree to enable efficient use of available skills prior to task execution; and (ii) Solve Tasks, which automatically selects, orchestrates, and executes multiple skills during task execution. Fig. 1

Evaluation contract：30 个 artifact-rich task、特定 Skill pool 和 LLM judge 支持规模效应观察；不证明安装量或树分类等价于真实质量。 exact-v1 定位为 `S4 — 4 Experiments`；用于核对的原文摘录：4 Experiments 4.1 Experimental Setup Skill ecosystem. We construct skill ecosystems of three sizes (, , ) to evaluate scalability. All skills are sourced from a public skill marketplace and GitHub repositories. The smallest pool () consists of two manually curated components: (i) the best-performing skill for each benchmark task, and (ii) a set of additional high-quality skills manually selected by human experts. The two larger pools ( and ) extend the -skill base by automatically including skills ranked by install

证明与未证明：证据只支持上述 paper-specific workload 内的机制/测量关系；不支持把作者结果外推为其他模型、数据、硬件、精度、长度、batch、并发或 production SLO 的通用结论。

Trade-off、failure 与共存边界：可扩展发现换来 taxonomy 漂移、DAG planning cost 与 evaluator bias；小 Skill 集仍适合直接绑定。 反证/限制定位为 `S6 — 6 Conclusions and Future Work`；用于核对的原文摘录：6 Conclusions and Future Work Skills have proven highly effective at extending LLM-based agents with domain-specific capabilities. However, there exists a fundamental tension between the rapidly expanding skill ecosystem and the agent’s inherently limited ability to discover and invoke skills, which requires an effective intermediate layer for skill management. To address this challenge, this paper introduces AgentSk

Artifact / implementation：exact-v1 `S4.SS1 — 4.1 Experimental Setup`；公开范围摘录：4.1 Experimental Setup Skill ecosystem. We construct skill ecosystems of three sizes (, , ) to evaluate scalability. All skills are sourced from a public skill marketplace and GitHub repositories. The smallest pool () consists of two manually curated components: (i) the best-performing skill for each benchmark task, and (ii) a set of additional high-quality。未公开的代码、commit、部署配置或复现实验不得由论文叙事反推。

<!-- claim:SF-2026-ARXIV-2603-02176:start -->只接受 arXiv:2603.02176v1 在 exact-v1 公开 workload 下的作者机制与实验主张；未披露的 model、hardware、precision、length、batch、concurrency、cost 与 production SLO 均为 Not Disclosed，不外推为通用结论。<!-- claim:SF-2026-ARXIV-2603-02176:end -->

Books Comparison：已读 `AGENT-PLATFORM` 的 `books/part-07-agent/84-agent-platform.md#Agent Definition 与 Run Identity (line 192)` 及相邻 `books/part-07-agent/83-mcp.md#本章要回答的问题 (line 10)`；现有命题为“evaluation。NVIDIA verified skills 提供了这条发布链的官方实现案例，但不能证明被验证 Skill 在所有 Agent、”。Decision=`No Change — Existing Coverage`；该 author-side 判断仍待fresh-context Books reviewer，Integrate 项只进入日期队列。
<!-- review:SF-2026-ARXIV-2603-02176:end -->

<!-- review:SF-2026-ARXIV-2603-00349:start -->
#### COOP$^2$: Defining, Observing, and Repairing Cooperation in LLM Multi-Agent Systems

问题与 changed constraint：Multi-Agent 的最终成功率无法解释合作是否真实发生，也无法把自然语言计划、消息与环境状态变化对齐。

旧路径为何合理：在该约束未出现、规模较小或 workload 更稳定时，论文所比较的旧路径仍以更少状态、更短控制链和更成熟实现提供合理基线；不能因本论文出现而静默覆盖。

机制、state/data/control owner：COOP²/EmCoop 建立 cognitive-event 到 environment-step 的时间映射，并沿约束满足过程度量计划、通信和执行，使合作成为可观察 trace 而非结果标签。 对应 exact-v1 `S4 — 4 EmCoop Methodology`；该机制由 `AGENT-MULTI-AGENT` 承载。原文定位摘录仅作核对：4 EmCoop Methodology We now present a methodological framework for analyzing cooperation in LLM-based embodied multi-agent systems by explicitly addressing the two challenges identified above: (i) the cognitive–embodied grounding challenge, i.e., how to align high-level plans and communication with stepwise embodied execution; and (ii) the cooperative tasks and constraints challenge, i.e., how to probe cooperation through the evolution of constraint satisfaction and final outcomes. 4.1 Solving the Cognitive–Embodie

Evaluation contract：作者在其 embodied task、拓扑和模型面板上展示多维合作指标；这证明指标能暴露不同协作轨迹，不证明存在跨任务唯一的 cooperation score。 exact-v1 定位为 `S7 — 7 Experiment Design and Results`；用于核对的原文摘录：7 Experiment Design and Results We evaluate EmCoop in two embodied environments with distinct cooperation constraints, varying communication topology, task difficulty, and agent count using GPT-5.2 and DeepSeek-V3.2. Figure 3 summarizes cooperation metrics (shown for MA-Crafter), with full results and run traces for both environments provided in Appendix J and K. RQ1: How does communication topology affect cooperation? LLM agents cooperate by forming plans at the cognitive layer and influencing one another’s decisi

证明与未证明：证据只支持上述 paper-specific workload 内的机制/测量关系；不支持把作者结果外推为其他模型、数据、硬件、精度、长度、batch、并发或 production SLO 的通用结论。

Trade-off、failure 与共存边界：可解释性换来更重的 trace instrumentation 与 task-specific constraint model；failure 是时钟或事件归因错误。只关心最终 SLA 的简单任务仍可用 outcome metric。 反证/限制定位为 `S8 — 8 Conclusion`；用于核对的原文摘录：8 Conclusion We introduced EmCoop, a benchmark framework for embodied cooperation among LLM agents that makes the cooperation process observable across cognitive activity, environment execution, and cooperative constraints. EmCoop shifts evaluation beyond end-task success toward interpretable cooperation dynamics. While we propose a concrete set of cooperation metrics, there is no single canonical metric for cooperat

Artifact / implementation：exact-v1 `A4 — Appendix D Cooperation Analysis: Algorithmic Details`；公开范围摘录：Appendix D Cooperation Analysis: Algorithmic Details Algorithm 1 specifies the threaded execution loop used to support cooperation analysis under asynchronous communication. At each environment step, agents run in parallel within live threads so they can continuously receive and process messages while forming plans. The system waits until all agents report r。未公开的代码、commit、部署配置或复现实验不得由论文叙事反推。

<!-- claim:SF-2026-ARXIV-2603-00349:start -->只接受 arXiv:2603.00349v1 在 exact-v1 公开 workload 下的作者机制与实验主张；未披露的 model、hardware、precision、length、batch、concurrency、cost 与 production SLO 均为 Not Disclosed，不外推为通用结论。<!-- claim:SF-2026-ARXIV-2603-00349:end -->

Books Comparison：已读 `AGENT-MULTI-AGENT` 的 `books/part-07-agent/82-multi-agent.md#Message 不是 State (line 356)` 及相邻 `books/part-07-agent/81-workflow.md#本章要回答的问题 (line 10); books/part-07-agent/83-mcp.md#本章要回答的问题 (line 10)`；现有命题为“shared side effect 多或 coordinator headroom 不足时，single Agent + deterministic verifier 仍更小、更可靠。”。Decision=`No Change — Existing Coverage`；该 author-side 判断仍待fresh-context Books reviewer，Integrate 项只进入日期队列。
<!-- review:SF-2026-ARXIV-2603-00349:end -->

<!-- review:SF-2026-ARXIV-2603-00381:start -->
#### Verifier-Bound Communication for LLM Agents: Certified Bounds on Covert Signaling

问题与 changed constraint：仅检查 Agent 消息的表面合规无法约束合谋信号，因为策略允许的多个表达仍可承载隐蔽选择。

旧路径为何合理：在该约束未出现、规模较小或 workload 更稳定时，论文所比较的旧路径仍以更少状态、更短控制链和更成熟实现提供合理基线；不能因本论文出现而静默覆盖。

机制、state/data/control owner：CLBC 将 generation 与 transcript admission 分离：消息只有携带绑定 policy、随机性、transcript chain 和字段约束的 proof envelope 并通过小 verifier 后才进入共享状态。 对应 exact-v1 `S2 — 2 A simple proof of concept`；该机制由 `AGENT-MULTI-AGENT` 承载。原文定位摘录仅作核对：2 A simple proof of concept We begin with a deliberately minimal protocol that isolates the intuition behind verifier-bound admission. The goal is not full security coverage; the goal is to expose the mechanism by which admission semantics can collapse otherwise exploitable degrees of freedom. Consider a reduced envelope with fields , where contains a small fixed metadata map. The verifier enforces schema fixedness, deterministic canonical serialization, and transcript chaining so that must match the canonical payl

Evaluation contract：理论界限与实验只覆盖论文声明的 residual channels、catalog、模型和 attacker；不能把 leakage bound 外推到未纳入 predicate 的环境 side channel。 exact-v1 定位为 `S6 — 6 Experiments`；用于核对的原文摘录：6 Experiments We evaluate the protocol with implementation artifacts spanning robustness, baselines, adaptive attackers, and performance. Our experimental goal is not a single benchmark score; it is evidence coherence across the full assurance stack. The implementation and evaluation artifacts used in this study are publicly available at https://github.com/Ostailor/CLBC. Strict-lane and empirical-lane evaluations cover multiple catalogs and task families, including multi-agent decision, negotiation, planning, summa

证明与未证明：证据只支持上述 paper-specific workload 内的机制/测量关系；不支持把作者结果外推为其他模型、数据、硬件、精度、长度、batch、并发或 production SLO 的通用结论。

Trade-off、failure 与共存边界：fail-closed admission 降低 covert capacity，但引入证明开销、predicate 版本治理与拒绝可用性风险；低风险协作或无需保密的通信仍可直接记录消息。 反证/限制定位为 `S9 — 9 Conclusion`；用于核对的原文摘录：9 Conclusion CLBCdemonstrates that communication security for LLM-agent systems can be operationalized as a verifier-bound admission protocol rather than an after-the-fact detection layer. The evidence supports three conclusions: reject-by-default admission suppresses recoverable covert signaling, robustness is workload-dependent and must be reported with residual declarations, and deployment feasibility is driven pr

Artifact / implementation：exact-v1 `A1 — Appendix A Experimental Details`；公开范围摘录：Appendix A Experimental Details This appendix expands protocol and measurement details needed to reproduce the reported claims. The evidence stack is ordered from protocol conformance to aggregate decision. Strict lanes emphasize deterministic acceptance semantics and theorem-aligned checks, while empirical lanes stress robustness under broader model/workloa。未公开的代码、commit、部署配置或复现实验不得由论文叙事反推。

<!-- claim:SF-2026-ARXIV-2603-00381:start -->只接受 arXiv:2603.00381v1 在 exact-v1 公开 workload 下的作者机制与实验主张；未披露的 model、hardware、precision、length、batch、concurrency、cost 与 production SLO 均为 Not Disclosed，不外推为通用结论。<!-- claim:SF-2026-ARXIV-2603-00381:end -->

Books Comparison：已读 `AGENT-MULTI-AGENT` 的 `books/part-07-agent/82-multi-agent.md#从机制演进到系统设计 (line 639)` 及相邻 `books/part-07-agent/81-workflow.md#本章要回答的问题 (line 10); books/part-07-agent/83-mcp.md#本章要回答的问题 (line 10)`；现有命题为“Multi-Agent 从广播全部对话演进到 typed role、message、shared state 与 topology。收益来自独立证据和真正的责任分解；当错误相关时，多数票可能放大失败，因此系统还要保存 minority evidence、校准 verifier/flip precision，并把 communication 和 verification delay纳入调度。”。Decision=`No Change — Existing Coverage`；该 author-side 判断仍待fresh-context Books reviewer，Integrate 项只进入日期队列。
<!-- review:SF-2026-ARXIV-2603-00381:end -->

<!-- review:SF-2026-ARXIV-2603-00468:start -->
#### Cloud-OpsBench: A Reproducible Benchmark for Agentic Root Cause Analysis in Cloud Systems

问题与 changed constraint：静态 RCA benchmark 可复现但缺少工具交互，live testbed 真实却让每次事故证据漂移，二者都难审计 agent 的调查过程。

旧路径为何合理：在该约束未出现、规模较小或 workload 更稳定时，论文所比较的旧路径仍以更少状态、更短控制链和更成熟实现提供合理基线；不能因本论文出现而静默覆盖。

机制、state/data/control owner：Cloud-OpsBench 冻结日志、指标、配置和瞬时 data-plane 状态为 State Snapshot，再通过标准诊断接口回放，解耦状态保存与工具交互。 对应 exact-v1 `S3.SS2 — 3.2. Design Philosophy: The State Snapshot Paradigm`；该机制由 `PLATFORM-EVALUATION-SYSTEM` 承载。原文定位摘录仅作核对：3.2. Design Philosophy: The State Snapshot Paradigm The core design philosophy of Cloud-OpsBench addresses the fundamental tension between reproducibility and ecological validity (§ 2). To bridge this gap, we introduce the State Snapshot paradigm (depicted in Fig. 1(c)), which conceptually serves as a deterministic digital twin of the target system at the precise moment of failure. Unlike traditional static artifacts (Gap 1)(§ 2), a State Snapshot captures the holistic operational context. This encompasses not only

Evaluation contract：754 个案例、57 类故障和两个微服务 workload 支持其可复算比较；不证明 snapshot 覆盖生产事故中的所有时变因果或外部依赖。 exact-v1 定位为 `S4.SS1 — 4.1. Experimental Setup`；用于核对的原文摘录：4.1. Experimental Setup The evaluating agent framework is implemented in Python 3.10, utilizing CrewAI(CrewAI, 2025) as the orchestration engine and Pydantic(Pydantic, 2026) for structured tool interface definitions. Consistent with white-box design principles, we employ Langfuse(Langfuse, 2025) for comprehensive agent observability, which automatically captures detailed traces of LLM generations, reasoning steps, and tool invocations during the diagnostic process. We evaluate the benchmark using seven models, expl

证明与未证明：证据只支持上述 paper-specific workload 内的机制/测量关系；不支持把作者结果外推为其他模型、数据、硬件、精度、长度、batch、并发或 production SLO 的通用结论。

Trade-off、failure 与共存边界：可重放性换来捕获与维护成本，failure 是 snapshot 缺少关键状态而制造假确定性。需要实时恢复能力时仍要补 live drill。 反证/限制定位为 `S5 — 5. Discussion`；用于核对的原文摘录：5. Discussion 5.1. Significance and Impact Redefining the Evaluation Standard for Autonomous SRE. Prior to Cloud-OpsBench, the field relied on outcome-based metrics that inadvertently rewarded stochastic guessing (Pham et al., 2025; Xu et al., 2025; Yu et al., 2023; AIOPS.CN, 2020; AIOPS.CN, 2021) . This work invalidates that approach. By enforcing a process-centric evaluation paradigm, we demonstrate that how an age

Artifact / implementation：exact-v1 `S4.SS1 — 4.1. Experimental Setup`；公开范围摘录：4.1. Experimental Setup The evaluating agent framework is implemented in Python 3.10, utilizing CrewAI(CrewAI, 2025) as the orchestration engine and Pydantic(Pydantic, 2026) for structured tool interface definitions. Consistent with white-box design principles, we employ Langfuse(Langfuse, 2025) for comprehensive agent observability, which automatically capt。未公开的代码、commit、部署配置或复现实验不得由论文叙事反推。

<!-- claim:SF-2026-ARXIV-2603-00468:start -->只接受 arXiv:2603.00468v1 在 exact-v1 公开 workload 下的作者机制与实验主张；未披露的 model、hardware、precision、length、batch、concurrency、cost 与 production SLO 均为 Not Disclosed，不外推为通用结论。<!-- claim:SF-2026-ARXIV-2603-00468:end -->

Books Comparison：已读 `PLATFORM-EVALUATION-SYSTEM` 的 `books/part-06-ai-infrastructure/66-evaluation-system.md#Action Control 需要 Sensitivity 与 Invariance 双臂证据 (line 2452)` 及相邻 `books/part-06-ai-infrastructure/65-kai-scheduler.md#本章要回答的问题 (line 10); books/part-06-ai-infrastructure/67-monitoring.md#本章要回答的问题 (line 10)`；现有命题为“EvalSpec 需要冻结 event/state schema、可控干预、matched interface、action scorer 与 tolerance，并保存每对干预样本的 trajectory。它能把相关性成功分解为更强的 behavioral evidence，却增加构造 matched interventions 的成本，也可能因遗漏真正 mediator 而误判。无法构造可信干预时，应把结论降级为 observational association，继续使用真实 outcome、人工 adjudication 与 production incident evidence。即使双臂通过，也只证明披露任务上的结构耦合，不证明模型具有内在 agency 或能迁移到开放环境。[受限证据：arXiv:2605.09692v1]”。Decision=`No Change — Existing Coverage`；该 author-side 判断仍待fresh-context Books reviewer，Integrate 项只进入日期队列。
<!-- review:SF-2026-ARXIV-2603-00468:end -->

<!-- review:SF-2026-ARXIV-2603-00623:start -->
#### TraceSIR: A Multi-Agent Framework for Structured Analysis and Reporting of Agentic Execution Traces

问题与 changed constraint：长工具链 Agent trace 既长又异构，直接让一个模型总结会丢失阶段、证据与根因之间的对应关系。

旧路径为何合理：在该约束未出现、规模较小或 workload 更稳定时，论文所比较的旧路径仍以更少状态、更短控制链和更成熟实现提供合理基线；不能因本论文出现而静默覆盖。

机制、state/data/control owner：TraceSIR 先结构化 trace，再由分工 Agent 归因、交叉核对并生成报告，把诊断对象从自然语言总结改成 typed execution evidence。 对应 exact-v1 `S3 — 3 Method`；该机制由 `PLATFORM-TRACE` 承载。原文定位摘录仅作核对：3 Method We propose TraceSIR, a multi-agent framework for structured analysis and reporting of agentic execution traces. As illustrated in Figure 2, TraceSIR coordinates three specialized components, i.e., StructureAgent, InsightAgent, and ReportAgent. Each component operates autonomously with tool invocation over structured traces, while the overall framework is designed to support both fine-grained per-case analysis and scalable cross-case reporting. 3.1 TraceFormat The input to TraceSIR can be either a single ex

Evaluation contract：评估只支持作者 trace、故障注入和 evaluator；不能证明多 Agent 归因是真实因果。 exact-v1 定位为 `S4 — 4 Experiments`；用于核对的原文摘录：4 Experiments Scenario Method Backbone Overall Score OS EA RCA OA OI Ranking Deep Research ClaudeCode GLM-5 82.7 8.7 8.0 7.3 9.0 8.3 4 ClaudeCode Claude-4.6 90.0 9.3 8.7 9.0 9.0 9.0 2 TraceSIR GLM-5 88.0 9.0 8.0 9.0 9.0 9.0 3 TraceSIR Claude-4.6 91.3 9.3 9.0 9.3 9.0 9.0 1 Function Calling ClaudeCode GLM-5 80.7 8.3 7.3 7.7 9.0 8.0 4 ClaudeCode Claude-4.6 88.0 8.7 8.3 9.0 9.0 9.0 3 TraceSIR GLM-5 89.3 9.0 8.7 9.0 9.0 9.0 2 TraceSIR Claude-4.6 91.3 9.0 9.0 9.0 9.7 9.0 1 Agentic Coding ClaudeCode GLM-5 58.7 6.0 4.0 5.7

证明与未证明：证据只支持上述 paper-specific workload 内的机制/测量关系；不支持把作者结果外推为其他模型、数据、硬件、精度、长度、batch、并发或 production SLO 的通用结论。

Trade-off、failure 与共存边界：结构化诊断提高定位能力但增加 token、judge 与编排成本；短而确定的 workflow 仍适合规则和人工检查。 反证/限制定位为 `Sx1 — Limitations`；用于核对的原文摘录：Limitations Despite its effectiveness, TraceSIR has several limitations. First, TraceSIR relies on LLM-based agents for trace abstraction, diagnostic reasoning, and report generation, and the quality of the resulting analyses may be influenced by the capabilities of the underlying language models, particularly in challenging domains such as complex coding tasks or highly specialized technical settings. Second, while

Artifact / implementation：exact-v1 `Not Disclosed — arXiv:2603.00623v1 exposes no dedicated Artifact / implementation section in the recovered exact-v1 body`；公开范围摘录：Not Disclosed。未公开的代码、commit、部署配置或复现实验不得由论文叙事反推。

<!-- claim:SF-2026-ARXIV-2603-00623:start -->只接受 arXiv:2603.00623v1 在 exact-v1 公开 workload 下的作者机制与实验主张；未披露的 model、hardware、precision、length、batch、concurrency、cost 与 production SLO 均为 Not Disclosed，不外推为通用结论。<!-- claim:SF-2026-ARXIV-2603-00623:end -->

Books Comparison：已读 `PLATFORM-TRACE` 的 `books/part-06-ai-infrastructure/69-trace.md#本章要回答的问题 (line 14)` 及相邻 `books/part-06-ai-infrastructure/68-logging.md#本章要回答的问题 (line 10); books/part-06-ai-infrastructure/70-cost.md#本章要回答的问题 (line 10)`；现有命题为“本章的核心判断是：**Trace 通过传播 context，将一次分布式操作拆成有父子或 link 关系的 spans，从而重建 critical path；其价值取决于边界、语义和采样是否保留真正决策点。**”。Decision=`No Change — Existing Coverage`；该 author-side 判断仍待fresh-context Books reviewer，Integrate 项只进入日期队列。
<!-- review:SF-2026-ARXIV-2603-00623:end -->

<!-- review:SF-2026-ARXIV-2603-00680:start -->
#### MemPO: Self-Memory Policy Optimization for Long-Horizon Agents

问题与 changed constraint：长时程 Agent 的 context 持续增长，外部 memory 若只被动检索，policy 无法学习何时写、压缩、替换和读取。

旧路径为何合理：在该约束未出现、规模较小或 workload 更稳定时，论文所比较的旧路径仍以更少状态、更短控制链和更成熟实现提供合理基线；不能因本论文出现而静默覆盖。

机制、state/data/control owner：MemPO 将 memory operation 纳入 policy action 与训练信号，让模型主动管理有限信息状态。 对应 exact-v1 `https://arxiv.org/html/2603.00680v1#S4 — exact-v1 §4 Self-Memory Policy Optimization (Method)`；该机制由 `AGENT-MEMORY` 承载。原文定位摘录仅作核对：Not Disclosed

Evaluation contract：结果仅支持所测环境、memory interface 与 reward；不证明模型写入内容具备事实权威。 exact-v1 定位为 `S5 — 5 Experiments`；用于核对的原文摘录：5 Experiments 5.1 Benchmarks To evaluate the effectiveness of our approach, following the method of MEM1 (Zhou et al., 2025), we test on multi-objective tasks, where the number of interaction rounds required for the agent to solve a problem is significantly higher compared to single-objective tasks. This allows us to better assess the performance of our method in scenarios with long contexts. Additionally, we can observe the changes in agent performance by progressively increasing the number of objectives. We creat

证明与未证明：证据只支持上述 paper-specific workload 内的机制/测量关系；不支持把作者结果外推为其他模型、数据、硬件、精度、长度、batch、并发或 production SLO 的通用结论。

Trade-off、failure 与共存边界：主动管理降低 context 压力，却引入 credit assignment、错误遗忘和自强化污染；短会话仍可直接保留上下文。 反证/限制定位为 `Sx1 — Limitations`；用于核对的原文摘录：Limitations Although our method shows promising performance, one potential limitation is that, due to varying tool invocation at different steps, the information content in memory naturally differs and the states are not completely equivalent across all steps in all rollout trajectories, which may introduce bias when calculating group-based advantages. While we alleviate this issue by introducing in Equation 4, more

Artifact / implementation：exact-v1 `S5.SS3 — 5.3 Implementation Details`；公开范围摘录：5.3 Implementation Details We first performed inference using GPT-4.1 (OpenAI et al., 2024) on the dataset from the work of Tang et al. (2025), and obtained approximately 10k trajectories containing memory. We then fine-tuned the model for one epoch using these data to enhance its ability to follow instructions related to the memory component. Simultaneously。未公开的代码、commit、部署配置或复现实验不得由论文叙事反推。

<!-- claim:SF-2026-ARXIV-2603-00680:start -->只接受 arXiv:2603.00680v1 在 exact-v1 公开 workload 下的作者机制与实验主张；未披露的 model、hardware、precision、length、batch、concurrency、cost 与 production SLO 均为 Not Disclosed，不外推为通用结论。<!-- claim:SF-2026-ARXIV-2603-00680:end -->

Books Comparison：已读 `AGENT-MEMORY` 的 `books/part-07-agent/77-memory.md#从原始轨迹到派生策略：Memory 的演进不是无限追加 (line 498)` 及相邻 `books/part-07-agent/76-rag.md#本章要回答的问题 (line 10); books/part-07-agent/78-tool-calling.md#本章要回答的问题 (line 10)`；现有命题为“把 raw interaction history 放进 Context 或 external memory，是最容易审计和纠错的起点；当经验频繁变化、涉及隐私删除，或样本仍少时，这个旧方案依然合理。压力来自另一侧：长轨迹会在每次推理中反复占用 context 与 environment budget，成功行为也无法在移除历史后保留。此时可以增加一个有条件的 consolidation 分支：teacher 读取累计经验，student 只读取原始任务状态；从已有轨迹构造 one-step decision branches，把 teacher 的局部决策监督压回 student，而不再与环境交互，也不依赖 learned world model 展开长 rollout。”。Decision=`No Change — Existing Coverage`；该 author-side 判断仍待fresh-context Books reviewer，Integrate 项只进入日期队列。
<!-- review:SF-2026-ARXIV-2603-00680:end -->

<!-- review:SF-2026-ARXIV-2603-00825:start -->
#### COMBAT: Conditional World Models for Behavioral Agent Training

问题与 changed constraint：只预测下一 observation 的 world model 不足以训练行为 agent，因为环境演化必须受条件、动作与多步 rollout 约束。

旧路径为何合理：在该约束未出现、规模较小或 workload 更稳定时，论文所比较的旧路径仍以更少状态、更短控制链和更成熟实现提供合理基线；不能因本论文出现而静默覆盖。

机制、state/data/control owner：COMBAT 将 behavior/action condition 注入生成式 dynamics，使模拟状态转移能为 agent 产生可控训练轨迹。 对应 exact-v1 `S3 — 3 Method`；该机制由 `MULTIMODAL-WORLD-MODELS` 承载。原文定位摘录仅作核对：3 Method Our proposed and studied approach, COMBAT, learns to simulate a complex, multi-agent environment by training a generative world model on video observations. World models have shown promise in mastering diverse domains [12] and creating interactive environments [5, 25]. We extend this paradigm to a competitive fighting game, where the model must learn the opponent’s behavior without explicit action labels. 3.1 Problem Formulation The task is as follows: Primarily, learning a conditional video generation mod

Evaluation contract：作者实验支持其环境与行为任务下的 controllability；不证明生成质量等价于因果正确性或真实环境安全。 exact-v1 定位为 `S4 — 4 Experiments`；用于核对的原文摘录：4 Experiments To validate our claim that a conditional world model can learn reactive agent behavior from partial observations, we conduct a series of experiments on the Tekken 3 dataset. We first detail our multi-stage training pipeline and model architectures. We then introduce our evaluation benchmarks and present results comparing our primary models and their distilled variants. 4.1 Implementation Details Our training process is divided into three main stages: autoencoder training, world model training, and dis

证明与未证明：证据只支持上述 paper-specific workload 内的机制/测量关系；不支持把作者结果外推为其他模型、数据、硬件、精度、长度、batch、并发或 production SLO 的通用结论。

Trade-off、failure 与共存边界：可控 rollout 提高训练覆盖，但会把 simulator bias 注入 policy；高风险动作仍需真实反馈与安全 envelope。 反证/限制定位为 `S5 — 5 Conclusion`；用于核对的原文摘录：5 Conclusion In this work, we introduce COMBAT, a conditional world model that learns complex, emergent agent behavior from partially observed gameplay. Our key finding is that by conditioning the model solely on Player 1’s actions it successfully learns a reactive, tactically coherent policy for Player 2 without any direct supervision. The model correctly associates the control inputs with the intended agent and gen

Artifact / implementation：exact-v1 `S4.SS1 — 4.1 Implementation Details`；公开范围摘录：4.1 Implementation Details Our training process is divided into three main stages: autoencoder training, world model training, and distillation for real-time inference. All models were trained on a cluster of NVIDIA H200 GPUs. Stage 1: Autoencoder Training. We first train a 340M parameter Deep Compression AutoEncoder (DCAE) to learn a compact latent represen。未公开的代码、commit、部署配置或复现实验不得由论文叙事反推。

<!-- claim:SF-2026-ARXIV-2603-00825:start -->只接受 arXiv:2603.00825v1 在 exact-v1 公开 workload 下的作者机制与实验主张；未披露的 model、hardware、precision、length、batch、concurrency、cost 与 production SLO 均为 Not Disclosed，不外推为通用结论。<!-- claim:SF-2026-ARXIV-2603-00825:end -->

Books Comparison：已读 `MULTIMODAL-WORLD-MODELS` 的 `books/part-03-multimodal-world-models/25-multimodal-world-models.md#本章要回答的问题 (line 8)` 及相邻 `books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md#本章要回答的问题 (line 10); books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#本章要回答的问题 (line 10)`；现有命题为“**Roadmap Intent:** 区分 video generation、predictive environment model 与 causal/controllable world model，解释 action-conditioned transition、latent dynamics、imagination 和 persistent state 的演进。”。Decision=`No Change — Existing Coverage`；该 author-side 判断仍待fresh-context Books reviewer，Integrate 项只进入日期队列。
<!-- review:SF-2026-ARXIV-2603-00825:end -->

<!-- review:SF-2026-ARXIV-2603-01058:start -->
#### TriMoE: Augmenting GPU with AMX-Enabled CPU and DIMM-NDP for High-Throughput MoE Inference via Offloading

问题与 changed constraint：MoE 推理的专家权重容量与不均匀路由使纯 GPU 部署受显存约束，而朴素 CPU offload 又受链路和计算差距限制。

旧路径为何合理：在该约束未出现、规模较小或 workload 更稳定时，论文所比较的旧路径仍以更少状态、更短控制链和更成熟实现提供合理基线；不能因本论文出现而静默覆盖。

机制、state/data/control owner：TriMoE 将活跃专家在 GPU、AMX CPU 与 DIMM-NDP 间分层放置并协调数据流，利用异构算力而非把 CPU 仅作存储。 对应 exact-v1 `S4.SS1 — 4.1. TriMoE Architecture`；该机制由 `INFER-GPU-MEMORY` 承载。原文定位摘录仅作核对：4.1. TriMoE Architecture Figure 4 illustrates the overall TriMoE architecture, which augments a server-grade single-GPU system with three heterogeneous compute resources: a high-performance GPU, an AMX-enabled CPU, and DIMM-NDP, to achieve high-throughput MoE offloading. High-Performance GPU: With hundreds of TFLOPS (Choquette et al., 2021; Choquette, 2023), the GPU serves as the core compute unit for high-density tasks. During the prefill phase, it performs all inference computations. In the decode phase, it focus

Evaluation contract：吞吐结果绑定作者模型、路由分布和硬件原型；不证明 NDP 可得性、成本或任意专家热度下均有收益。 exact-v1 定位为 `S5.SS1 — 5.1. Experiment Setup`；用于核对的原文摘录：5.1. Experiment Setup 5.1.1. TriMoE System To evaluate TriMoE, we built a heterogeneous prototype system comprising an NVIDIA H100 PCIe GPU with 80GB HBM, an AMX-enabled Intel Xeon Platinum 8470 CPU (8-channel memory), and 16 DIMM-NDPs providing high internal bandwidth. Detailed configurations are listed in Table 1. We utilize PCIe 5.0 to provide 64GB/s unidirectional bandwidth for host-to-GPU data transfer. On the software stack, we employ vLLM 0.8.1 (Kwon et al., 2023) and KTransformers (Chen et al., 2025) to imp

证明与未证明：证据只支持上述 paper-specific workload 内的机制/测量关系；不支持把作者结果外推为其他模型、数据、硬件、精度、长度、batch、并发或 production SLO 的通用结论。

Trade-off、failure 与共存边界：容量与吞吐换来 placement、prefetch 和一致性复杂度；链路拥塞或专家热度突变会反转收益。可装入 GPU 的小 MoE 仍应保持单层执行。 反证/限制定位为 `S6 — 6. Conclusion`；用于核对的原文摘录：6. Conclusion TriMoE revisits MoE offloading from the perspective of expert heterogeneity and exposes the fundamental inefficiency of binary GPU–NDP designs in handling warm experts. By jointly leveraging GPU for hot experts, AMX-enabled CPU for warm experts, and DIMM-NDP for cold experts, TriMoE matches each expert class to its most suitable compute domain. Combined with our bottleneck-aware scheduling and predictio

Artifact / implementation：exact-v1 `Not Disclosed — arXiv:2603.01058v1 exposes no dedicated Artifact / implementation section in the recovered exact-v1 body`；公开范围摘录：Not Disclosed。未公开的代码、commit、部署配置或复现实验不得由论文叙事反推。

<!-- claim:SF-2026-ARXIV-2603-01058:start -->只接受 arXiv:2603.01058v1 在 exact-v1 公开 workload 下的作者机制与实验主张；未披露的 model、hardware、precision、length、batch、concurrency、cost 与 production SLO 均为 Not Disclosed，不外推为通用结论。<!-- claim:SF-2026-ARXIV-2603-01058:end -->

Books Comparison：已读 `INFER-GPU-MEMORY` 的 `books/part-05-inference-system/54-gpu-memory.md#三类缓解路径 (line 230)` 及相邻 `books/part-05-inference-system/53-kserve-llm.md#本章要回答的问题 (line 10); books/part-05-inference-system/55-pd-disaggregation.md#本章要回答的问题 (line 10)`；现有命题为“cache owner 仍决定最终可见状态。收益取决于 CPU 核数、host memory bandwidth、PCIe 和 layer compute 是否足以”。Decision=`No Change — Existing Coverage`；该 author-side 判断仍待fresh-context Books reviewer，Integrate 项只进入日期队列。
<!-- review:SF-2026-ARXIV-2603-01058:end -->

<!-- review:SF-2026-ARXIV-2603-01162:start -->
#### Demystifying Group Relative Policy Optimization: Its Policy Gradient is a U-Statistic

问题与 changed constraint：GRPO 的组内相对优势常被当作普通 minibatch baseline，但同组样本耦合会改变估计量和方差解释。

旧路径为何合理：在该约束未出现、规模较小或 workload 更稳定时，论文所比较的旧路径仍以更少状态、更短控制链和更成熟实现提供合理基线；不能因本论文出现而静默覆盖。

机制、state/data/control owner：论文把 GRPO policy gradient 形式化为 U-statistic，显式描述组采样、相对比较与梯度估计之间的依赖。 对应 exact-v1 `https://arxiv.org/html/2603.01162v1#S4 — exact-v1 §4 Main results: U-statistic gradient and GRPO analysis (Method)`；该机制由 `TRAIN-GRPO` 承载。原文定位摘录仅作核对：Not Disclosed

Evaluation contract：理论结论在其假设下成立；实验不能证明某一 group size 或变体普遍最优。 exact-v1 定位为 `S5 — 5 Experiments`；用于核对的原文摘录：5 Experiments We conduct two sets of experiments in this section to validate our theoretical findings. In Section 5.1, we empirically compare GRPO with the vanilla and oracle algorithms in terms of gradient evaluation, to verify the oracle property of the GRPO gradient estimator (Corollary 4) and its superiority over the vanilla estimator (Corollary 5). In Section 5.2, we investigate the optimal group size for policy optimization, to verify the universality of the optimal group size established by our scaling law (

证明与未证明：证据只支持上述 paper-specific workload 内的机制/测量关系；不支持把作者结果外推为其他模型、数据、硬件、精度、长度、batch、并发或 production SLO 的通用结论。

Trade-off、failure 与共存边界：更准确的统计解释换来相关样本和方差估计复杂度；独立样本、显式 critic 的 PPO 分支仍有清楚适用条件。 反证/限制定位为 `S6 — 6 Discussion`；用于核对的原文摘录：6 Discussion We provide a rigorous theoretical analysis of GRPO, a cornerstone algorithm for enhancing the reasoning capabilities of large reasoning models. We show that GRPO is a statistically principled policy gradient algorithm whose gradient estimator naturally forms a U-statistic (Lemma 1). Leveraging Hoeffding’s decomposition, we characterize its MSE (Theorem 2, Proposition 3) and establish both oracle (Corolla

Artifact / implementation：exact-v1 `Not Disclosed — arXiv:2603.01162v1 exposes no dedicated Artifact / implementation section in the recovered exact-v1 body`；公开范围摘录：Not Disclosed。未公开的代码、commit、部署配置或复现实验不得由论文叙事反推。

<!-- claim:SF-2026-ARXIV-2603-01162:start -->只接受 arXiv:2603.01162v1 在 exact-v1 公开 workload 下的作者机制与实验主张；未披露的 model、hardware、precision、length、batch、concurrency、cost 与 production SLO 均为 Not Disclosed，不外推为通用结论。<!-- claim:SF-2026-ARXIV-2603-01162:end -->

Books Comparison：已读 `TRAIN-GRPO` 的 `books/part-04-training-system/33-grpo.md#本章要回答的问题 (line 16)` 及相邻 `books/part-04-training-system/32-ppo.md#本章要回答的问题 (line 10); books/part-04-training-system/34-dpo.md#本章要回答的问题 (line 10)`；现有命题为“本章以 DeepSeekMath 提出的 Group Relative Policy Optimization 为基线。后续系统可能修改 token weighting、KL estimator、normalization 或 clipping；同名 GRPO 实现必须逐项核验，不能仅凭算法名称推断完全相同 objective。”。Decision=`Integrate`；该 author-side 判断仍待fresh-context Books reviewer，Integrate 项只进入日期队列。
<!-- review:SF-2026-ARXIV-2603-01162:end -->

<!-- review:SF-2026-ARXIV-2603-01399:start -->
#### Quasar: Quantized Self-Speculative Acceleration for Rapid Inference via Memory-Efficient Verification

问题与 changed constraint：self-speculative decoding 需要 draft 足够便宜且 verification 保持准确；量化可降内存却可能降低接受率。

旧路径为何合理：在该约束未出现、规模较小或 workload 更稳定时，论文所比较的旧路径仍以更少状态、更短控制链和更成熟实现提供合理基线；不能因本论文出现而静默覆盖。

机制、state/data/control owner：Quasar 对 draft/self-draft 状态做量化并设计内存受限 verification，联合优化草稿成本与接受路径。 对应 exact-v1 `S3 — 3 Methodology`；该机制由 `INFER-SPECULATIVE-DECODING` 承载。原文定位摘录仅作核对：3 Methodology In this section, we present our framework designed to accelerate the verification phase of speculative decoding. We first establish the mathematical formulation of standard speculative decoding. Subsequently, we detail our proposed quantized verification mechanism. To address the challenge of activation outliers inherent in Large Language Models (LLMs), we employ an enhanced variant of SmoothQuant to enable robust W8A8 (8-bit weights and activations) inference. Finally, we provide a theoretical analys

Evaluation contract：加速与质量只属于作者模型、量化格式、序列和硬件；没有证明跨模型校准或所有分布均保持 exactness。 exact-v1 定位为 `S4 — 4 Experiments`；用于核对的原文摘录：4 Experiments In this section, we empirically evaluate the effectiveness of our Quantized Verification framework (named Quasar). We aim to answer three primary research questions: • Effectiveness(RQ1): Does replacing the BF16 verifier with a W8A8 quantized verifier yield significant wall-clock speedups in memory-bound settings? We evaluate the main speedup and average acceptance length of our method relative to the baseline method. • Robustness(RQ2): Does our method maintain consistent wall-clock speedups across di

证明与未证明：证据只支持上述 paper-specific workload 内的机制/测量关系；不支持把作者结果外推为其他模型、数据、硬件、精度、长度、batch、并发或 production SLO 的通用结论。

Trade-off、failure 与共存边界：更小草稿状态换来量化误差和额外校准；低接受率或短输出时普通 decode 更合适。 反证/限制定位为 `S5 — 5 Discussion`；用于核对的原文摘录：5 Discussion Table 5: Comparison between Structural Pruning and Quasar for Qwen3. represents the token acceptance rate, and denotes the mean acceptance length. Results highlight that training-free pruning fails to maintain the distributional alignment necessary for effective speculative decoding. Method Retention / Precision Speedup Vanilla (Full Model) 100% Layers / BF16 1.00 1.00 Structural Pruning Pruned-90% 90% L

Artifact / implementation：exact-v1 `S4.SS1.SSS0.Px3 — Implementation Details.`；公开范围摘录：Implementation Details. We implemented the W8A8 verification using NCLL and integrated it into a vLLM-Ascend inference engine. All experiments were conducted on a single Ascend 910B2 (64GB) NPU. The prompt lookup length is dynamically adjusted, with a maximum limit of 4 and a minimum limit of 1.。未公开的代码、commit、部署配置或复现实验不得由论文叙事反推。

<!-- claim:SF-2026-ARXIV-2603-01399:start -->只接受 arXiv:2603.01399v1 在 exact-v1 公开 workload 下的作者机制与实验主张；未披露的 model、hardware、precision、length、batch、concurrency、cost 与 production SLO 均为 Not Disclosed，不外推为通用结论。<!-- claim:SF-2026-ARXIV-2603-01399:end -->

Books Comparison：已读 `INFER-SPECULATIVE-DECODING` 的 `books/part-05-inference-system/48-speculative-decoding.md#本章要回答的问题 (line 16)` 及相邻 `books/part-05-inference-system/47-pagedattention.md#本章要回答的问题 (line 10); books/part-05-inference-system/49-tensorrt-llm.md#本章要回答的问题 (line 10)`；现有命题为“本章的核心判断是：**Speculative Decoding 用额外且便宜的 proposal work，换取一次 target-model verification 推进多个 output tokens；经典算法通过 acceptance 与 residual sampling 保持 target distribution，而不是用 draft model 改写模型行为。**”。Decision=`No Change — Existing Coverage`；该 author-side 判断仍待fresh-context Books reviewer，Integrate 项只进入日期队列。
<!-- review:SF-2026-ARXIV-2603-01399:end -->

<!-- review:SF-2026-ARXIV-2603-01499:start -->
#### Towards Privacy-Preserving LLM Inference via Covariant Obfuscation (Technical Report)

问题与 changed constraint：隐私推理若只靠传输加密，服务端仍看到表示与计算；完全同态/TEE 又可能成本过高或改变信任假设。

旧路径为何合理：在该约束未出现、规模较小或 workload 更稳定时，论文所比较的旧路径仍以更少状态、更短控制链和更成熟实现提供合理基线；不能因本论文出现而静默覆盖。

机制、state/data/control owner：covariant obfuscation 通过保持所需变换关系的输入/权重表示来隐藏原值，使服务端在混淆域执行。 对应 exact-v1 `S2.SS1 — 2.1 Methods based on Obfuscation`；该机制由 `PLATFORM-SECURITY` 承载。原文定位摘录仅作核对：2.1 Methods based on Obfuscation A series of obfuscation-based methods have been proposed for privacy-preserving LLM inference, primarily via three techniques: token substitution [11, 23, 12, 15], embedding transformation [16, 18, 17, 31, 32, 19], LLM-aided rewriting [14, 33]. Token Substitution. Since prompts are composed of a sequence of tokens, the most intuitive privacy preservation method is to substitute sensitive tokens within the text. SANTEXT [23] and RANTEXT [11] leverage local differential privacy to rep

Evaluation contract：技术报告只在其攻击模型和任务中展示可用性；没有证明密码学级 indistinguishability 或覆盖 side channel。 exact-v1 定位为 `S6 — 6 Experiments`；用于核对的原文摘录：6 Experiments In this section, we present the experimental results of AloePri and their explanation. 6.1 Experimental Settings Models and Datasets. We conduct experiments on commonly-used open-source LLMs to evaluate the effectiveness of AloePri. For dense models, we select Qwen2.5/Qwen3 [47, 48], Llama3 [49], Deepseek-R1-Distill-Qwen (R1-Distill) [43]. For MoE models, we choose Qwen3-MoE and Deepseek-V3.1-Terminus [50], covering both moderate and large-scale models. We employ various representative LLM evaluation

证明与未证明：证据只支持上述 paper-specific workload 内的机制/测量关系；不支持把作者结果外推为其他模型、数据、硬件、精度、长度、batch、并发或 production SLO 的通用结论。

Trade-off、failure 与共存边界：较轻执行换来特定变换假设和可能的精度/泄露边界；强对手或合规场景仍需成熟密码学或可信硬件。 反证/限制定位为 `S7 — 7 Discussion and Future Work`；用于核对的原文摘录：7 Discussion and Future Work Generalization to Other Models. We focus primarily on text-generative LLMs in this work, but our method’s design principles generalize to emerging Transformer variants and other neural network architectures (e.g., multi-modal LLMs, CNNs) under the covariant obfuscation mechanism. Most model architectures can be formulated as directed acyclic graphs (DAGs), with nodes (model components) co

Artifact / implementation：exact-v1 `A6 — Appendix F Experiment Details`；公开范围摘录：Appendix F Experiment Details F.1 Potential Threats Vocabulary-Matching Attack (VMA). AloePri protect privacy by mapping plaintext tokens of private text to obfuscated tokens via a permutation . With knowledge of the obfuscated model weights, attackers can attempt to map each obfuscated token back to its original plaintext token. This threat leverages the Vo。未公开的代码、commit、部署配置或复现实验不得由论文叙事反推。

<!-- claim:SF-2026-ARXIV-2603-01499:start -->只接受 arXiv:2603.01499v1 在 exact-v1 公开 workload 下的作者机制与实验主张；未披露的 model、hardware、precision、length、batch、concurrency、cost 与 production SLO 均为 Not Disclosed，不外推为通用结论。<!-- claim:SF-2026-ARXIV-2603-01499:end -->

Books Comparison：已读 `PLATFORM-SECURITY` 的 `books/part-06-ai-infrastructure/72-security.md#风险管理而不是一次性认证 (line 1091)` 及相邻 `books/part-06-ai-infrastructure/71-multi-tenant.md#本章要回答的问题 (line 10); books/part-06-ai-infrastructure/73-production-best-practice.md#本章要回答的问题 (line 10)`；现有命题为“- `SF-2026-ARXIV-2606-22019` — primary `arXiv:2606.22019v1`；exact-v1 URL=`https://arxiv.org/html/2606.22019v1`；Method=`https://arxiv.org/html/2606.22019v1 — §2 Audit model: carriers, screens, and ablations; §6 The audit lifecycle: which handle is sound in which channel?`；Evaluation=`https://arxiv.org/html/2606.22019v1 — §3 A controlled body channel is screenable: coverage predicts transfer; §4 Vocabulary-carried token traits evade initialization-alignment screens; §5 The carrier is signal-dependent, and moving it m”。Decision=`No Change — Existing Coverage`；该 author-side 判断仍待fresh-context Books reviewer，Integrate 项只进入日期队列。
<!-- review:SF-2026-ARXIV-2603-01499:end -->

<!-- review:SF-2026-ARXIV-2603-01960:start -->
#### TiledAttention: a CUDA Tile SDPA Kernel for PyTorch

问题与 changed constraint：通用 SDPA kernel 在形状、mask 和 tile 边界上可能无法同时利用 CUDA memory hierarchy 与计算流水。

旧路径为何合理：在该约束未出现、规模较小或 workload 更稳定时，论文所比较的旧路径仍以更少状态、更短控制链和更成熟实现提供合理基线；不能因本论文出现而静默覆盖。

机制、state/data/control owner：TiledAttention 将 attention 分解为显式 CUDA tiles 并控制加载、累加与边界处理，令执行计划而非框架默认 kernel 拥有数据移动。 对应 exact-v1 `S2 — 2 Method`；该机制由 `INFER-TENSORRT-LLM` 承载。原文定位摘录仅作核对：2 Method 2.1 Scaled dot-product attention Given queries , keys , and values , SDPAcomputes (1) where is a mask (e.g., causal or padding). Materializing the score matrix is prohibitive for long , motivating blockwise implementations. 2.2 Online softmax and blockwise attention The FlashAttention line of work [5, 6] established blockwise, IO-aware attention as a strong baseline. It streams tiles while maintaining running softmax statistics (running max and normalization), avoiding materialization of the score matrix.

Evaluation contract：性能只属于给定 GPU、dtype、shape 和 PyTorch integration；不证明所有 attention 变体或未来硬件仍占优。 exact-v1 定位为 `S3.SS3 — 3.3 Experimental Setup`；用于核对的原文摘录：3.3 Experimental Setup We sweep a workload grid intended to cover common foundation-model attention shapes: • Sequence length . • Head dimensions . • Dtypes: FP16 and BF16. • Masking: causal and non-causal. This grid is anchored in common transformer deployments: is common in BERT- and ViT-style models [7, 8, 13], while is prevalent in larger decoder-only language models such as GPT-3, PaLM, and LLaMA-family systems [2, 3, 17]. Sequence lengths 512–2048 cover short-to-mid context workloads common in serving and fin

证明与未证明：证据只支持上述 paper-specific workload 内的机制/测量关系；不支持把作者结果外推为其他模型、数据、硬件、精度、长度、batch、并发或 production SLO 的通用结论。

Trade-off、failure 与共存边界：定制 kernel 换来形状特化、维护和数值验证成本；常规形状仍可依赖成熟 vendor kernel。 反证/限制定位为 `S6 — 6 Limitations and Future Work`；用于核对的原文摘录：6 Limitations and Future Work This work has three main limitations. First, we evaluate only the forward pass; backward and fused variants are future work. Second, we target Grace–Blackwell / Blackwell-class GPUs; portability to other architectures may require additional schedules. Third, we study a deliberately small tuning space; extending to larger search spaces is an important next step.

Artifact / implementation：exact-v1 `S3.SS2 — 3.2 Implementation`；公开范围摘录：3.2 Implementation API We expose a minimal functional API: (5) The API matches common frameworks: q,k,v are contiguous tensors in , causal selects causal masking, and scale defaults to . PyTorch entry point. TiledAttention is available as a Python package that integrates with PyTorch. A typical usage pattern is: import torch from tiledattention import sdpa #。未公开的代码、commit、部署配置或复现实验不得由论文叙事反推。

<!-- claim:SF-2026-ARXIV-2603-01960:start -->只接受 arXiv:2603.01960v1 在 exact-v1 公开 workload 下的作者机制与实验主张；未披露的 model、hardware、precision、length、batch、concurrency、cost 与 production SLO 均为 Not Disclosed，不外推为通用结论。<!-- claim:SF-2026-ARXIV-2603-01960:end -->

Books Comparison：已读 `INFER-TENSORRT-LLM` 的 `books/part-05-inference-system/49-tensorrt-llm.md#从 Linear 语义到 GEMM 执行 (line 267)` 及相邻 `books/part-05-inference-system/48-speculative-decoding.md#本章要回答的问题 (line 10); books/part-05-inference-system/50-vllm.md#本章要回答的问题 (line 10)`；现有命题为“为每个 fused operator 手写 kernel，在 shape 稳定、目标硬件单一时可获得最直接的控制；attention、state-space、quantized block 或自定义 reduction 增多后，kernel surface 会随组合爆炸。一个中间抽象是把可表达部分归一为 `GEMM + versioned epilogue`：compiler 拥有 tile、layout 与 epilogue lowering，runtime 只提交已验证的 shape/precision instance，custom kernel 保留给无法合法表达的 control flow。”。Decision=`No Change — Existing Coverage`；该 author-side 判断仍待fresh-context Books reviewer，Integrate 项只进入日期队列。
<!-- review:SF-2026-ARXIV-2603-01960:end -->

<!-- review:SF-2026-ARXIV-2603-02075:start -->
#### Trident: Adaptive Scheduling for Heterogeneous Multimodal Data Pipelines

问题与 changed constraint：多模态训练数据样本的 decode、augment、长度和设备需求差异大，FIFO pipeline 会让某一 modality 阻塞整体 step。

旧路径为何合理：在该约束未出现、规模较小或 workload 更稳定时，论文所比较的旧路径仍以更少状态、更短控制链和更成熟实现提供合理基线；不能因本论文出现而静默覆盖。

机制、state/data/control owner：Trident 依据样本/模态 cost 动态调度数据处理阶段，在异构 worker 间平衡生产速度与 trainer 消费。 对应 exact-v1 `S3.SS1 — 3.1 System Architecture`；该机制由 `TRAIN-DATA` 承载。原文定位摘录仅作核对：3.1 System Architecture Figure 1 illustrates the architecture of Trident, which consists of three integrated layers built atop a Ray cluster. Pipeline Executor. The pipeline executor manages the dataflow graph, instantiating operators, routing data between them, and applying parallelism updates from the scheduling layer. Metrics Collector. The metrics collector gathers runtime statistics from all operator instances—including observed throughput, resource utilization, queue lengths, per-request characteristics, and

Evaluation contract：吞吐改善绑定作者数据组合、worker 和存储；不证明调度开销在小数据或单模态 workload 中值得。 exact-v1 定位为 `S8.SS1 — 8.1 Experimental Setup`；用于核对的原文摘录：8.1 Experimental Setup Cluster Configuration. We conduct experiments on a cluster of 8 servers, each equipped with 8 Huawei Ascend 910B NPUs, 256 CPU cores, and 1 TB memory, interconnected via 100 Gbps network. Datasets. We use two datasets spanning distinct modalities. The PDF dataset contains documents of three types—academic papers, annual reports, and financial reports—processed sequentially by type. The video dataset contains clips in two categories: short-form (10–30 s, 720p) and long-form (5–10 min, 1080p–4K

证明与未证明：证据只支持上述 paper-specific workload 内的机制/测量关系；不支持把作者结果外推为其他模型、数据、硬件、精度、长度、batch、并发或 production SLO 的通用结论。

Trade-off、failure 与共存边界：减少 pipeline bubble 但引入 cost estimation、重排和数据顺序变化；可预测数据集仍可用静态流水。 反证/限制定位为 `S10 — 10 Conclusion`；用于核对的原文摘录：10 Conclusion In this paper, we presented Trident, an adaptive scheduling framework for heterogeneous multimodal data preparation pipelines running on fixed-resource clusters. Trident addresses key limitations of existing stream processing schedulers when applied to modern multimodal workloads, including inaccurate throughput estimation for asynchronous operators, static operator configurations under workload heterog

Artifact / implementation：exact-v1 `S7 — 7 Implementation`；公开范围摘录：7 Implementation We implement Trident as an extension to Ray Data v2.46.0 [10], a distributed data processing library built on the Ray framework [23]. For the observation layer, we extend Ray Data’s metrics infrastructure to capture per-operator timestamps, record counts, and queue statistics. Workers maintain local buffers that flush to a central coordinato。未公开的代码、commit、部署配置或复现实验不得由论文叙事反推。

<!-- claim:SF-2026-ARXIV-2603-02075:start -->只接受 arXiv:2603.02075v1 在 exact-v1 公开 workload 下的作者机制与实验主张；未披露的 model、hardware、precision、length、batch、concurrency、cost 与 production SLO 均为 Not Disclosed，不外推为通用结论。<!-- claim:SF-2026-ARXIV-2603-02075:end -->

Books Comparison：已读 `TRAIN-DATA` 的 `books/part-04-training-system/27-data.md#数据分布就是优化权重 (line 152)` 及相邻 `books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#本章要回答的问题 (line 10); books/part-04-training-system/28-pretraining.md#本章要回答的问题 (line 10)`；现有命题为“这里 data operator 只提出训练分布，training controller 拥有 active set、采样权重、cache 与更新时机，”。Decision=`No Change — Existing Coverage`；该 author-side 判断仍待fresh-context Books reviewer，Integrate 项只进入日期队列。
<!-- review:SF-2026-ARXIV-2603-02075:end -->

<!-- review:SF-2026-ARXIV-2603-02146:start -->
#### LongRLVR: Long-Context Reinforcement Learning Requires Verifiable Context Rewards

问题与 changed constraint：长上下文 RL 只给最终答案 reward 时，模型可以忽略大部分 context 或走捷径，无法学习证据使用。

旧路径为何合理：在该约束未出现、规模较小或 workload 更稳定时，论文所比较的旧路径仍以更少状态、更短控制链和更成熟实现提供合理基线；不能因本论文出现而静默覆盖。

机制、state/data/control owner：LongRLVR 把可验证 context-use 条件纳入 reward，使长文证据选择与最终答案共同决定更新。 对应 exact-v1 `S2 — 2 Method`；该机制由 `TRAIN-GRPO` 承载。原文定位摘录仅作核对：2 Method In this section, we introduce LongRLVR to remedy the limitations of RLVR in long-context tasks. We first present an explicit grounding formulation for long-context RLVR in Section 2.1. Next, in Section 2.2, we formally prove that outcome-only rewards lead to a vanishing gradient problem for this grounding process. To solve this, we introduce our verifiable context reward, presenting its theoretical foundation in Section 2.3.1 and a practical F-score-based implementation in Section 2.3.2. Finally, we detail

Evaluation contract：作者实验只覆盖可验证任务与其 reward construction；不证明开放域证据链都可自动判定。 exact-v1 定位为 `S3 — 3 Experimental Setup`；用于核对的原文摘录：3 Experimental Setup 3.1 Implementation Details Data Curation. To train our model, we constructed a large-scale, high-quality dataset of 46K long-context question-answering pairs with explicit grounding annotations. We sourced documents from book, arXiv, and code domains, filtering for lengths between 8K and 64K tokens. Following the pipeline detailed in Algorithm 1, we first identified semantically coherent clusters of text segments within each document. For each document, we then used a powerful generator model,

证明与未证明：证据只支持上述 paper-specific workload 内的机制/测量关系；不支持把作者结果外推为其他模型、数据、硬件、精度、长度、batch、并发或 production SLO 的通用结论。

Trade-off、failure 与共存边界：稠密上下文约束减少 shortcut，却增加 verifier 成本和 specification gaming；答案充分可验证的短任务仍可用 outcome reward。 反证/限制定位为 `S6 — 6 Conclusion`；用于核对的原文摘录：6 Conclusion In this work, we addressed a fundamental limitation of Reinforcement Learning with Verifiable Rewards (RLVR) in long-context scenarios: its inability to effectively learn contextual grounding due to sparse, outcome-only rewards. We formally identified this issue as the “vanishing grounding gradient” problem, where the learning signal for retrieving evidence diminishes significantly with the complexity of

Artifact / implementation：exact-v1 `S3.SS1 — 3.1 Implementation Details`；公开范围摘录：3.1 Implementation Details Data Curation. To train our model, we constructed a large-scale, high-quality dataset of 46K long-context question-answering pairs with explicit grounding annotations. We sourced documents from book, arXiv, and code domains, filtering for lengths between 8K and 64K tokens. Following the pipeline detailed in Algorithm 1, we first id。未公开的代码、commit、部署配置或复现实验不得由论文叙事反推。

<!-- claim:SF-2026-ARXIV-2603-02146:start -->只接受 arXiv:2603.02146v1 在 exact-v1 公开 workload 下的作者机制与实验主张；未披露的 model、hardware、precision、length、batch、concurrency、cost 与 production SLO 均为 Not Disclosed，不外推为通用结论。<!-- claim:SF-2026-ARXIV-2603-02146:end -->

Books Comparison：已读 `TRAIN-GRPO` 的 `books/part-04-training-system/33-grpo.md#Measurement 也是 Reward Interface 的一部分 (line 399)` 及相邻 `books/part-04-training-system/32-ppo.md#本章要回答的问题 (line 10); books/part-04-training-system/34-dpo.md#本章要回答的问题 (line 10)`；现有命题为“可执行结果仍会受 environment、measurement noise 与 reward mapping 影响；训练 specification 必须绑定测量环境、重复性与 reward transformation，hard correctness gate 不能被连续 proxy 取代。”。Decision=`Integrate`；该 author-side 判断仍待fresh-context Books reviewer，Integrate 项只进入日期队列。
<!-- review:SF-2026-ARXIV-2603-02146:end -->

<!-- review:SF-2026-ARXIV-2603-02188:start -->
#### Multi-Head Low-Rank Attention

问题与 changed constraint：标准 multi-head attention 的 projection 与 KV 状态随 head/维度扩张，低秩共享可省参数但会损失 head diversity。

旧路径为何合理：在该约束未出现、规模较小或 workload 更稳定时，论文所比较的旧路径仍以更少状态、更短控制链和更成熟实现提供合理基线；不能因本论文出现而静默覆盖。

机制、state/data/control owner：Multi-Head Low-Rank Attention 在 head 结构内引入低秩参数化，重分配共享与每头特有表示。 对应 exact-v1 `A4 — Appendix D Llama-3 Architecture`；该机制由 `MODEL-MULTI-HEAD-ATTENTION` 承载。原文定位摘录仅作核对：Appendix D Llama-3 Architecture Given hidden states for a sequence of tokens, we first compute the attention output then project back to the model dimension and add a residual: Next, an MLP block (gated form) is applied: followed by the output projection and residual: where is an elementwise nonlinearity function such as SiLU and denotes elementwise multiplication.

Evaluation contract：作者结果支持其模型与 rank 下的质量/成本点；不证明统一 rank 适合所有层或长上下文。 exact-v1 定位为 `S4 — 4 Experiments`；用于核对的原文摘录：4 Experiments 4.1 Experimental Setup Model Configuration. We adopt the Llama-3 (Llama and others, 2024) architecture (Appendix D) and compare MLRA against the following attention mechanism baselines: MHA (Vaswani et al., 2017), MQA (Shazeer, 2019), GQA (Ainslie et al., 2023), MLA (DeepSeek and others, 2024a), MFA (Hu et al., 2024), TPA (Zhang et al., 2025), GLA-2 (Zadouri et al., 2025), GLA-4, and GTA (Zadouri et al., 2025). GLA-4 compresses the KV cache into four latent heads. We initialize the MHA baseline with t

证明与未证明：证据只支持上述 paper-specific workload 内的机制/测量关系；不支持把作者结果外推为其他模型、数据、硬件、精度、长度、batch、并发或 production SLO 的通用结论。

Trade-off、failure 与共存边界：压缩计算与状态换来表示瓶颈和 rank 选择；质量优先或小模型仍可保留 full-rank heads。 反证/限制定位为 `S5 — 5 Conclusion`；用于核对的原文摘录：5 Conclusion We propose Multi-Head Low-Rank Attention (MLRA), a novel attention mechanism with native 4-way tensor parallelism support. At the 2.9B scale, MLRA-4 achieves state-of-the-art performance on perplexity and zero-shot common-sense reasoning benchmarks. Furthermore, MLRA achieves the lowest decoding latency for long-context sequences (up to 2M tokens) and the highest throughput across sequence lengths from 1

Artifact / implementation：exact-v1 `S4.SS1 — 4.1 Experimental Setup`；公开范围摘录：4.1 Experimental Setup Model Configuration. We adopt the Llama-3 (Llama and others, 2024) architecture (Appendix D) and compare MLRA against the following attention mechanism baselines: MHA (Vaswani et al., 2017), MQA (Shazeer, 2019), GQA (Ainslie et al., 2023), MLA (DeepSeek and others, 2024a), MFA (Hu et al., 2024), TPA (Zhang et al., 2025), GLA-2 (Zadouri。未公开的代码、commit、部署配置或复现实验不得由论文叙事反推。

<!-- claim:SF-2026-ARXIV-2603-02188:start -->只接受 arXiv:2603.02188v1 在 exact-v1 公开 workload 下的作者机制与实验主张；未披露的 model、hardware、precision、length、batch、concurrency、cost 与 production SLO 均为 Not Disclosed，不外推为通用结论。<!-- claim:SF-2026-ARXIV-2603-02188:end -->

Books Comparison：已读 `MODEL-MULTI-HEAD-ATTENTION` 的 `books/part-02-model/15-multi-head-attention.md#本章要回答的问题 (line 12)` 及相邻 `books/part-02-model/14-self-attention.md#本章要回答的问题 (line 10); books/part-02-model/16-feed-forward-mlp.md#本章要回答的问题 (line 10)`；现有命题为“第14章的单个 Attention head 已能让 token 按内容读取上下文，为什么还需要多个 head？Multi-Head Attention 如何在多个投影子空间并行建立关系，又为什么会演化出 MQA 和 GQA？”。Decision=`No Change — Existing Coverage`；该 author-side 判断仍待fresh-context Books reviewer，Integrate 项只进入日期队列。
<!-- review:SF-2026-ARXIV-2603-02188:end -->

<!-- review:SF-2026-ARXIV-2603-00188:start -->
#### ST-Lite: Training-Free KV Cache Compression with Spatio-Trajectory Guidance for Long-Horizon GUI Agents

问题与 changed constraint：长时程 GUI agent 的视觉轨迹会让 KV 状态持续膨胀；只按注意力或 recency 删除 token 会破坏动作轨迹中的空间连续性。

旧路径为何合理：在该约束未出现、规模较小或 workload 更稳定时，论文所比较的旧路径仍以更少状态、更短控制链和更成熟实现提供合理基线；不能因本论文出现而静默覆盖。

机制、state/data/control owner：ST-Lite 把视觉 token 的空间位置和交互轨迹共同用于训练外压缩，令保留决策拥有 GUI 轨迹语义，而不是只由通用 KV eviction 规则决定。 对应 exact-v1 `S4 — 4. ST-Lite Framework`；该机制由 `INFER-KV-CACHE` 承载。原文定位摘录仅作核对：4. ST-Lite Framework Addressing the aforementioned misalignments, we propose ST-Lite (Spatio-Trajectory Lite), a training-free KV Cache compression framework, as illustrated in Figure 4. We introduce two core components: Component-centric Spatial Saliency (CSS) for maintaining spatial structural integrity, and Trajectory-aware Semantic Gating (TSG) for eliminating historical redundancy. Figure 4. The overall architecture of ST-Lite. Our framework dynamically optimizes the KV cache through two synergistic modules: (

Evaluation contract：作者只在其 GUI-agent、压缩率与任务集合上比较性能和缓存开销；这支持该保留信号在该 workload 下有效，不证明它适用于普通文本或任意视觉 agent。 exact-v1 定位为 `S5 — 5. Experiment`；用于核对的原文摘录：5. Experiment This section verifies the effectiveness of ST-Lite through quantitative evaluation and qualitative analysis, focusing on: (1) ST-Lite’s performance retention capability compared to existing compression algorithms under low-to-medium cache budgets (10%–40%); (2) the specific contributions of Component-centric Spatial Saliency (CSS) and Trajectory-aware Semantic Gating (TSG) to context simplification. 5.1. Experimental Setup Benchmarks. To comprehensively assess the efficacy of ST-Lite across varying le

证明与未证明：证据只支持上述 paper-specific workload 内的机制/测量关系；不支持把作者结果外推为其他模型、数据、硬件、精度、长度、batch、并发或 production SLO 的通用结论。

Trade-off、failure 与共存边界：收益是降低长轨迹状态量；代价是额外轨迹特征与任务耦合，failure 是关键但低频的视觉状态被误删。短轨迹或显存宽裕时，全量 KV 仍更简单。 反证/限制定位为 `A7 — Appendix G Limitations`；用于核对的原文摘录：Appendix G Limitations While our framework achieves significant efficiency gains by leveraging structural and historical priors, there remains potential to further align the compression strategy with the model’s internal representation dynamics through data-driven optimization. Future work will explore end-to-end learnable policies to facilitate the deployment of Large Vision-Language Models in even more complex scen

Artifact / implementation：exact-v1 `A2 — Appendix B Implementation Details`；公开范围摘录：Appendix B Implementation Details To ensure a comprehensive evaluation, we instantiate our framework on two state-of-the-art GUI agent backbones: UI-TARS-1.5-7B (Qin et al., 2025) and OpenCUA-7B (Wang et al., 2025). UI-TARS-1.5-7B. UI-TARS is a specialized Vision-Language Model (VLM) based on the Qwen2.5-VL (Bai et al., 2025) architecture, fine-tuned specifi。未公开的代码、commit、部署配置或复现实验不得由论文叙事反推。

<!-- claim:SF-2026-ARXIV-2603-00188:start -->只接受 arXiv:2603.00188v1 在 exact-v1 公开 workload 下的作者机制与实验主张；未披露的 model、hardware、precision、length、batch、concurrency、cost 与 production SLO 均为 Not Disclosed，不外推为通用结论。<!-- claim:SF-2026-ARXIV-2603-00188:end -->

Books Comparison：已读 `INFER-KV-CACHE` 的 `books/part-05-inference-system/45-why-kv-cache-speeds-up.md#KV Cache 的生命周期 (line 517)` 及相邻 `books/part-05-inference-system/44-decode.md#本章要回答的问题 (line 10); books/part-05-inference-system/46-continuous-batching.md#本章要回答的问题 (line 10)`；现有命题为“一个 training-free 分支先离线建立 model-side PCA basis，再在每个 request prefill 中估计各层 reconstruction curve，用 water-filling 在总 KV budget 下分配 variable rank。它不删除 token，而是改变每个 region 保留的 feature subspace；basis revision、request statistic、rank map、packed offsets、codec precision 与 reuse scope 都必须进入 cache identity。Prefix reuse 只有在 basis、model、RoPE 与 rank policy 兼容时才能共享，Decode kernel 若不能直接消费 variable layout，projection/gather 成本会返还 memory 节省。”。Decision=`No Change — Existing Coverage`；该 author-side 判断仍待fresh-context Books reviewer，Integrate 项只进入日期队列。
<!-- review:SF-2026-ARXIV-2603-00188:end -->

<!-- review:SF-2026-ARXIV-2603-01045:start -->
#### Silo-Bench: A Scalable Environment for Evaluating Distributed Coordination in Multi-Agent LLM Systems

问题与 changed constraint：Multi-Agent coordination 常用单任务最终分数，无法区分通信拓扑、共享状态和分布式协调能力。

旧路径为何合理：在该约束未出现、规模较小或 workload 更稳定时，论文所比较的旧路径仍以更少状态、更短控制链和更成熟实现提供合理基线；不能因本论文出现而静默覆盖。

机制、state/data/control owner：Silo-Bench 提供隔离但可交互的环境与可扩展任务，把 coordination protocol、资源和结果作为同一 evaluation contract。 对应 exact-v1 `S2.SS0.SSS0.Px2 — Multi-Agent Architectures and Role-Agnosticism.`；该机制由 `PLATFORM-EVALUATION-SYSTEM` 承载。原文定位摘录仅作核对：Multi-Agent Architectures and Role-Agnosticism. The paradigm of orchestrating multiple LLM agents has evolved from simple role-playing to complex problem-solving frameworks. Foundational works like CAMEL (Li et al., 2023) and MetaGPT (Hong et al., 2023) utilize role-specialized agents (e.g., assigning “Manager” or “Coder” personas) embedded within fixed hierarchical or waterfall workflows. While effective for domain-specific tasks like software engineering (Islam et al., 2024a), these approaches entangle the agents

Evaluation contract：结果只属于所测模型、agent 数和任务；不能外推开放环境中的协作可靠性。 exact-v1 定位为 `S4 — 4 Experiments`；用于核对的原文摘录：4 Experiments We systematically evaluate multi-agent coordination across three orthogonal axes—agent scale, communication protocol, and language model—yielding a factorial design that covers qualitatively distinct coordination regimes. 4.1 Experimental Setup Each evaluation instance in Silo-Bench is specified by agent scale , communication protocol , and language model . All models are deployed locally with default temperature and 128K context windows. Agent Scale (). We vary team size across , chosen to probe qual

证明与未证明：证据只支持上述 paper-specific workload 内的机制/测量关系；不支持把作者结果外推为其他模型、数据、硬件、精度、长度、batch、并发或 production SLO 的通用结论。

Trade-off、failure 与共存边界：更真实的 coordination 测量增加环境成本和随机性；单元级协议测试仍适合快速回归。 反证/限制定位为 `Sx1 — Limitations`；用于核对的原文摘录：Limitations While Silo-Bench provides a comprehensive framework for evaluating multi-agent collaboration, it has several limitations. Our evaluation only covers three fundamental communication protocols and does not include other coordination mechanisms such as hierarchical protocols, gossip-based dissemination and hybrid approaches. We adopt agent configurations with uniform underlying models, whereas real-world mul

Artifact / implementation：exact-v1 `S4.SS1 — 4.1 Experimental Setup`；公开范围摘录：4.1 Experimental Setup Each evaluation instance in Silo-Bench is specified by agent scale , communication protocol , and language model . All models are deployed locally with default temperature and 128K context windows. Agent Scale (). We vary team size across , chosen to probe qualitatively distinct coordination regimes. The minimal team () isolates fundam。未公开的代码、commit、部署配置或复现实验不得由论文叙事反推。

<!-- claim:SF-2026-ARXIV-2603-01045:start -->只接受 arXiv:2603.01045v1 在 exact-v1 公开 workload 下的作者机制与实验主张；未披露的 model、hardware、precision、length、batch、concurrency、cost 与 production SLO 均为 Not Disclosed，不外推为通用结论。<!-- claim:SF-2026-ARXIV-2603-01045:end -->

Books Comparison：已读 `PLATFORM-EVALUATION-SYSTEM` 的 `books/part-06-ai-infrastructure/66-evaluation-system.md#评估对象有四个层次 (line 417)` 及相邻 `books/part-06-ai-infrastructure/65-kai-scheduler.md#本章要回答的问题 (line 10); books/part-06-ai-infrastructure/67-monitoring.md#本章要回答的问题 (line 10)`；现有命题为“Research Agent 还需要把 final artifact、research progress 与 environment integrity 分开：没有产出最终解，不等于过程中没有形成可复用证据；反过来，拿到高分也可能来自损坏的依赖、污染的 workspace 或 verifier 漏洞。风险评估同样应按 risk family 保存不同 EvalSpec，并进一步区分：”。Decision=`No Change — Existing Coverage`；该 author-side 判断仍待fresh-context Books reviewer，Integrate 项只进入日期队列。
<!-- review:SF-2026-ARXIV-2603-01045:end -->

<!-- review:SF-2026-ARXIV-2603-01548:start -->
#### Graph-Based Self-Healing Tool Routing for Cost-Efficient LLM Agents

问题与 changed constraint：Agent tool router 的静态映射在工具变更或错误累积时会持续失败，人工修复又无法跟上工具规模。

旧路径为何合理：在该约束未出现、规模较小或 workload 更稳定时，论文所比较的旧路径仍以更少状态、更短控制链和更成熟实现提供合理基线；不能因本论文出现而静默覆盖。

机制、state/data/control owner：论文将工具、能力和失败关系建图，并根据执行反馈修复路由边，使错误成为 routing-state 更新信号。 对应 exact-v1 `PDF page 4; exact heading 2. Architecture: Health Monitors + Tool Graph`；该机制由 `AGENT-TOOL-CALLING` 承载。原文定位摘录仅作核对：2. Architecture: Health Monitors + Tool Graph Our architecture has three layers that separate attention (what matters now), action planning (what tools to use), and reasoning (what to do when plans fail). Figure 2: Self-Healing Router Architecture. Parallel health monitors compete on priority; the tool graph handles routing; the LLM is invoked only for goal demotion. 2.1 Parallel Health Monitors: Priority Competition The architecture runs cheap parallel health monitors — intent classifiers, risk detectors, tool hea

Evaluation contract：成本和成功率只覆盖作者工具集、错误注入和模型；不证明自动修复不会把偶发失败固化为错误拓扑。 exact-v1 定位为 `PDF page 11; exact heading 3. Multi-Domain Evaluation`；用于核对的原文摘录：3. Multi-Domain Evaluation A key question for any agent architecture is whether it generalizes across different tool orchestration patterns, or whether it only works for one graph shape. We evaluate across three domains chosen specifically because their tool graphs have structurally distinct topologies. Before examining per-domain results, consider how the four approaches handle the same failure. In Scenario S5, email dies mid-task after a refund has already been processed: Figure 6: Same failure (email dies mid-ta

证明与未证明：证据只支持上述 paper-specific workload 内的机制/测量关系；不支持把作者结果外推为其他模型、数据、硬件、精度、长度、batch、并发或 production SLO 的通用结论。

Trade-off、failure 与共存边界：自愈降低人工维护，但引入图状态漂移与反馈污染；小而稳定的工具集合仍适合显式映射。 反证/限制定位为 `PDF page 19; exact heading 5.4 Honest Limitations`；用于核对的原文摘录：5.4 Honest Limitations We identify several limitations that should be addressed in future work: Mock environment. All 19 scenarios use mock tools and a deterministic mock LLM. This validates structural properties — that Dijkstra correctly reroutes, that priority competition correctly prioritizes, that goal demotion triggers at the right time — but does not validate real- world API latency, error distributions, or LLM

Artifact / implementation：exact-v1 `Not Disclosed — arXiv:2603.01548v1 exposes no dedicated Artifact / implementation section in the recovered exact-v1 body`；公开范围摘录：Not Disclosed。未公开的代码、commit、部署配置或复现实验不得由论文叙事反推。

<!-- claim:SF-2026-ARXIV-2603-01548:start -->只接受 arXiv:2603.01548v1 在 exact-v1 公开 workload 下的作者机制与实验主张；未披露的 model、hardware、precision、length、batch、concurrency、cost 与 production SLO 均为 Not Disclosed，不外推为通用结论。<!-- claim:SF-2026-ARXIV-2603-01548:end -->

Books Comparison：已读 `AGENT-TOOL-CALLING` 的 `books/part-07-agent/78-tool-calling.md#Evaluation 与 Observability (line 365)` 及相邻 `books/part-07-agent/77-memory.md#本章要回答的问题 (line 10); books/part-07-agent/79-planning.md#本章要回答的问题 (line 10)`；现有命题为“复杂多轮 tool path 若等完整 reasoning 后才开始交互，用户看到的 latency 由最长链决定。Agent 可在低风险、可取消的边界并行准备候选 tool call 或 UI response，但只能把它们作为 proposal；authorizer 和 side-effect identity 在真实执行前统一 commit，错误分支必须可撤销。收益是隐藏思考延迟，代价是浪费、重复调用和 stale observation；不可逆工具、权限不明或 cancellation 不可靠时回退串行。”。Decision=`No Change — Existing Coverage`；该 author-side 判断仍待fresh-context Books reviewer，Integrate 项只进入日期队列。
<!-- review:SF-2026-ARXIV-2603-01548:end -->

<!-- review:SF-2026-ARXIV-2603-01581:start -->
#### KERV: Kinematic-Rectified Speculative Decoding for Embodied VLA Models

问题与 changed constraint：VLA 动作序列具有运动连续性，通用 token equality/概率接受规则会拒绝语义可行但数值不同的 draft。

旧路径为何合理：在该约束未出现、规模较小或 workload 更稳定时，论文所比较的旧路径仍以更少状态、更短控制链和更成熟实现提供合理基线；不能因本论文出现而静默覆盖。

机制、state/data/control owner：KERV 用运动学误差校正/接受 VLA 草稿，把 verification 从离散 token 一致扩展到受动作动力学约束的近似路径。 对应 exact-v1 `S4 — 4. KERV Framework`；该机制由 `INFER-SPECULATIVE-DECODING` 承载。原文定位摘录仅作核对：4. KERV Framework Figure 4. KF-Based Compensation Mechanism in KERVfig4 In this section, we will detail how we combine and leverage these insights to address the two key challenges of SD within the proposed end-to-end KERV framework. 4.1. KF-Based Compensation Mechanism From Insight ①, to address the challenge of re-inference when facing token errors in SD, we combine kinematic-based methods and VLA models, proposing a compensation mechanism. As Fig. 4 illustrates, the core idea is that when an SD error occurs, we

Evaluation contract：结果仅对所测 robot、动作表示和容差成立；不证明近似接受保持一般任务的 exact distribution。 exact-v1 定位为 `S6 — 6. Experiments`；用于核对的原文摘录：6. Experiments 6.1. Setup Following OpenVLA (Kim et al., 2024), we tested KERV framework on the LIBERO benchmark (Liu et al., 2023). We utilize four task suites, including LIBERO-Object, LIBERO-Spatial, LIBERO-Goal, and LIBERO-Long. Each suite contains 10 tasks. For each task, we conduct 50 trials for testing. We utilize the finetuned OpenVLA as the verification models and build a single LLaMA block (Touvron et al., 2023) as a draft model. We trained the draft models based on the DeepSpeed (Rasley et al., 2020) fra

证明与未证明：证据只支持上述 paper-specific workload 内的机制/测量关系；不支持把作者结果外推为其他模型、数据、硬件、精度、长度、batch、并发或 production SLO 的通用结论。

Trade-off、failure 与共存边界：更高接受率换来非精确语义和 safety threshold；对不可容忍动作误差的控制回路仍应精确验证。 反证/限制定位为 `S6.SS3 — 6.3. Discussion`；用于核对的原文摘录：6.3. Discussion Hyperparameters. The hyperparameters of KERV include the prediction length (PL), the action context (AC) of KF, and the number of SD steps () executed after each time of KF. We evaluate KERV’s performance across different hyperparameters on LIBERO-Goal, with the results presented in Fig. 8. From Fig. 8 (a), when <4, the SR decreases rapidly. When >4, the acceleration ratio decreases gradually due to t

Artifact / implementation：exact-v1 `S5 — 5. System Implementation`；公开范围摘录：5. System Implementation This section explores the efficient implementation of KERV on existing hardware platforms from a computational perspective based on CPU-GPU collaboration. 5.1. GPU-Side Draft and Verify Both the draft model and verification model involve substantial computation. Measurements show the draft model requires 0.07 GFLOPs per inference, wh。未公开的代码、commit、部署配置或复现实验不得由论文叙事反推。

<!-- claim:SF-2026-ARXIV-2603-01581:start -->只接受 arXiv:2603.01581v1 在 exact-v1 公开 workload 下的作者机制与实验主张；未披露的 model、hardware、precision、length、batch、concurrency、cost 与 production SLO 均为 Not Disclosed，不外推为通用结论。<!-- claim:SF-2026-ARXIV-2603-01581:end -->

Books Comparison：已读 `INFER-SPECULATIVE-DECODING` 的 `books/part-05-inference-system/48-speculative-decoding.md#本章要回答的问题 (line 12)` 及相邻 `books/part-05-inference-system/47-pagedattention.md#本章要回答的问题 (line 10); books/part-05-inference-system/49-tensorrt-llm.md#本章要回答的问题 (line 10)`；现有命题为“自回归 Decode 每次只能生成一个 token，这是 LLM 推理延迟的根本瓶颈之一。Speculative Decoding 为什么能让大模型“看起来一次生成多个 token”？它为什么不是简单地用小模型替代大模型？它在什么条件下才真正有效？”。Decision=`No Change — Existing Coverage`；该 author-side 判断仍待fresh-context Books reviewer，Integrate 项只进入日期队列。
<!-- review:SF-2026-ARXIV-2603-01581:end -->

<!-- review:SF-2026-ARXIV-2603-01639:start -->
#### Learning to Draft: Adaptive Speculative Decoding with Reinforcement Learning

问题与 changed constraint：Speculative decoding 的 draft 固定后，workload/target 变化会使接受率下降；仅训练更小模型不能直接优化系统延迟。

旧路径为何合理：在该约束未出现、规模较小或 workload 更稳定时，论文所比较的旧路径仍以更少状态、更短控制链和更成熟实现提供合理基线；不能因本论文出现而静默覆盖。

机制、state/data/control owner：Learning to Draft 用 RL 把 target verification feedback 与系统收益送回 draft policy，使 proposal 分布随目标和成本约束调整。 对应 exact-v1 `S4 — 4 Method`；该机制由 `INFER-SPECULATIVE-DECODING` 承载。原文定位摘录仅作核对：4 Method We frame the interaction between draft and target models within a Reinforcement Learning (RL) framework, employing two co-adaptive policies to navigate the inherent trade-off between acceptance length and latency: a depth policy, , which determines the draft depth, and a size policy, , which determines the verification size. The action space for the depth policy is binary, , determining whether to continue drafting after each forward pass, while the action space for the size policy, , is a discrete range o

Evaluation contract：加速与质量只属于作者模型、硬件和 reward；不证明 learned draft 始终保持 exactness 或跨 target 泛化。 exact-v1 定位为 `S5 — 5 Experiments`；用于核对的原文摘录：5 Experiments 5.1 Setups Models We conduct experiments with state-of-the-art open source chat and reasoning models, including Llama-3.1-8B-Instruct (Dubey et al., 2024), Vicuna-13B-v1.3 (Chiang et al., 2023), DeepSeek-R1-Distill-LLaMA 8B (DeepSeek-AI, 2025), Qwen3-14B (Team, 2025a) and Qwen3-32B (Team, 2025a). The Eagle3 models for the Qwen3 series are from AngelSlim (Contributors, 2025), as the official implementation had not been released. For all other models, we used the official public releases of Eagle3 (Li e

证明与未证明：证据只支持上述 paper-specific workload 内的机制/测量关系；不支持把作者结果外推为其他模型、数据、硬件、精度、长度、batch、并发或 production SLO 的通用结论。

Trade-off、failure 与共存边界：适应性提高接受率但引入训练、版本耦合和 reward mismatch；稳定 target 仍适合静态 draft。 反证/限制定位为 `S7 — 7 Conclusion`；用于核对的原文摘录：7 Conclusion In this paper, we introduce LTD, a novel speculative decoding method that directly optimizes the throughput of each draft-and-verify cycle using reinforcement learning. By employing two co-adaptive policies to dynamically coordinate the drafting and verification phases, LTD learns to manage the trade-off between acceptance length and time cost, achieving a synergistic acceleration. Extensive experiments

Artifact / implementation：exact-v1 `Sx1 — Reproducibility Statement`；公开范围摘录：Reproducibility Statement In Section 4 and Appendix A.2, we provide a detailed description of our method and the training process; in Section 5.1 and Appendix A.3, we present the complete training parameters and evaluation datasets; and in Appendix A.1, we document the hyperparameters used for baseline methods. Together, these details support the reproducibi。未公开的代码、commit、部署配置或复现实验不得由论文叙事反推。

<!-- claim:SF-2026-ARXIV-2603-01639:start -->只接受 arXiv:2603.01639v1 在 exact-v1 公开 workload 下的作者机制与实验主张；未披露的 model、hardware、precision、length、batch、concurrency、cost 与 production SLO 均为 Not Disclosed，不外推为通用结论。<!-- claim:SF-2026-ARXIV-2603-01639:end -->

Books Comparison：已读 `INFER-SPECULATIVE-DECODING` 的 `books/part-05-inference-system/48-speculative-decoding.md#本章要回答的问题 (line 16)` 及相邻 `books/part-05-inference-system/47-pagedattention.md#本章要回答的问题 (line 10); books/part-05-inference-system/49-tensorrt-llm.md#本章要回答的问题 (line 10)`；现有命题为“本章的核心判断是：**Speculative Decoding 用额外且便宜的 proposal work，换取一次 target-model verification 推进多个 output tokens；经典算法通过 acceptance 与 residual sampling 保持 target distribution，而不是用 draft model 改写模型行为。**”。Decision=`No Change — Existing Coverage`；该 author-side 判断仍待fresh-context Books reviewer，Integrate 项只进入日期队列。
<!-- review:SF-2026-ARXIV-2603-01639:end -->

<!-- review:SF-2026-ARXIV-2603-01661:start -->
#### HeRo: Adaptive Orchestration of Agentic RAG on Heterogeneous Mobile SoC

问题与 changed constraint：移动端 Agentic RAG 同时竞争 CPU/GPU/NPU、内存和能耗，固定算子放置无法适应检索与生成阶段变化。

旧路径为何合理：在该约束未出现、规模较小或 workload 更稳定时，论文所比较的旧路径仍以更少状态、更短控制链和更成熟实现提供合理基线；不能因本论文出现而静默覆盖。

机制、state/data/control owner：HeRo 根据阶段、热状态和设备能力动态编排检索、rerank 与生成，把异构 SoC 资源作为在线调度对象。 对应 exact-v1 `S4 — 4. Orchestration Methods`；该机制由 `INFER-SCHEDULING` 承载。原文定位摘录仅作核对：4. Orchestration Methods Figure 4. Orchestration Techniques. AAA 4.1. Problem Formulation We focus on minimizing the latency of a single RAG graph, with each node being a sub-stage associated with: (1) model, (2) configuration set including the PU and workload shape. and (3) profiled performance model for runtime, bandwidth, and slowdown. For each , the scheduler chooses a configuration and a start time . The end-to-end latency of the RAG flow is: (2) where denotes the completion time of , is an average slowdown fa

Evaluation contract：延迟/能耗结果绑定作者移动 SoC、模型和 RAG pipeline；不证明所有厂商 runtime 都支持同等迁移成本。 exact-v1 定位为 `S6 — 6. Experiments`；用于核对的原文摘录：6. Experiments 6.1. Experiment Setup Hardware Platform. As summarized in Tab. 2, we evaluate HeRo on two representative mobile devices, Redmi K80 and OnePlus 13, equipped with Snapdragon 8Gen4 and 8Gen4 SoCs, respectively. Applications. Our experiments cover three agentic RAG workflows with varying complexity, derived from the template workflow in Fig. 1. Workflow 1, Fast Document Finder, segments documents into chunks (default size: 128, overlap: 10), embeds them, and stores them in the vector DB. Then it retrieve

证明与未证明：证据只支持上述 paper-specific workload 内的机制/测量关系；不支持把作者结果外推为其他模型、数据、硬件、精度、长度、batch、并发或 production SLO 的通用结论。

Trade-off、failure 与共存边界：适应性提高利用率但增加 profiling、迁移与 thermal feedback；固定 workload 可用静态 placement 降复杂度。 反证/限制定位为 `S7 — 7. Conclusion`；用于核对的原文摘录：7. Conclusion This paper presents HeRo, an adaptive orchestration system designed to address the challenges of deploying complex agentic RAG workflows onto heterogeneous mobile SoCs, including stage-accelerator mapping, workload partitioning, concurrency control, and dynamic dependency scheduling. By designing a dependency-guided scheduler with awareness of shape, bandwidth, and hardware affinity, HeRo achieves effic

Artifact / implementation：exact-v1 `S5 — 5. Implementation`；公开范围摘录：5. Implementation We implemented HeRoon top of llama.cpp (ggml-org, 2025), Powerserve (Contributors, 2025) (a mobile LLM inference framework with Hexagon NPU support), and Faiss (Douze et al., 2024), with roughly 5,000 lines of C/C++ code. HeRo reuses the CPU and OpenCL backends from llama.cpp and integrates the NPU backend from Powerserve. We extend the run。未公开的代码、commit、部署配置或复现实验不得由论文叙事反推。

<!-- claim:SF-2026-ARXIV-2603-01661:start -->只接受 arXiv:2603.01661v1 在 exact-v1 公开 workload 下的作者机制与实验主张；未披露的 model、hardware、precision、length、batch、concurrency、cost 与 production SLO 均为 Not Disclosed，不外推为通用结论。<!-- claim:SF-2026-ARXIV-2603-01661:end -->

Books Comparison：已读 `INFER-SCHEDULING` 的 `books/part-05-inference-system/56-inference-scheduling.md#本章在知识树中的位置 (line 853)` 及相邻 `books/part-05-inference-system/55-pd-disaggregation.md#本章要回答的问题 (line 10); books/part-06-ai-infrastructure/57-what-is-ai-platform.md#本章要回答的问题 (line 10)`；现有命题为“把 online LLM scheduling 建模为带几何长度/剩余工作量的 admission 与排队问题；scheduler 以 workload shape 和 SLO slack 决定队列而非只按到达顺序。 这项变化只在 exact-v1 披露的 workload、状态身份和评估合同内成立；作者 workload、FP16/BF16、QPS 2–128 与队列模型不能外推到其他 engine、KV tier 或多租户优先级；估计失准需要保守 admission fallback。 因此旧路径在这些新增约束不存在、证据条件不足或失败回退被触发时仍然成立，不能被新的局部结果静默覆盖。”。Decision=`No Change — Existing Coverage`；该 author-side 判断仍待fresh-context Books reviewer，Integrate 项只进入日期队列。
<!-- review:SF-2026-ARXIV-2603-01661:end -->

<!-- review:SF-2026-ARXIV-2603-01683:start -->
#### Surgical Post-Training: Proximal On-Policy Distillation for Reasoning with Knowledge Retention

问题与 changed constraint：推理蒸馏若全局更新 policy，容易为新 reasoning 轨迹破坏既有知识；纯离线 KL 又缺少当前策略 rollout。

旧路径为何合理：在该约束未出现、规模较小或 workload 更稳定时，论文所比较的旧路径仍以更少状态、更短控制链和更成熟实现提供合理基线；不能因本论文出现而静默覆盖。

机制、state/data/control owner：Surgical Post-Training 使用受限的 on-policy distillation，把新轨迹信号与保留约束绑定到同一 update。 对应 exact-v1 `A5.SS0.SSS0.Px3 — Evaluation Protocol`；该机制由 `TRAIN-RLHF` 承载。原文定位摘录仅作核对：Evaluation Protocol For each instance, LLMs are prompted to solve two problems in a query: • Are there any potential winning moves to form 4-in-a-row for you? Output all winning moves. • Are there any potential winning moves to form 4-in-a-row for your opponent? Output all winning moves. Ground truth is computed using a perfect solver within GAMEBoT. We parse the model’s Chain-of-Thought (CoT) to extract the final answers and verify them against the game engine’s ground truth.

Evaluation contract：结果只支持指定模型、任务和 teacher；不证明所有知识保留或长期无遗忘。 exact-v1 定位为 `S5 — 5 Experiments`；用于核对的原文摘录：5 Experiments In this section, we present the experimental results of SPoT, followed by ablation studies that validate the effectiveness of our optimization objective (Section 5.3) and our data pipeline (Section 5.4). 5.1 Setup Models and Datasets We adopt Qwen3-8B and Llama3.1-8B-Instruct as the policy models for training. We intentionally choose instruction-tuned models over base models, since these already post-trained models are more susceptible to catastrophic forgetting (Lu and Lab, 2025). If SPoT retains the

证明与未证明：证据只支持上述 paper-specific workload 内的机制/测量关系；不支持把作者结果外推为其他模型、数据、硬件、精度、长度、batch、并发或 production SLO 的通用结论。

Trade-off、failure 与共存边界：更小行为漂移换来保守更新和额外 rollout；需要较大能力跃迁时普通 SFT/RL 仍更直接。 反证/限制定位为 `S7 — 7 Discussion and Conclusion`；用于核对的原文摘录：7 Discussion and Conclusion We demonstrate that it is possible to efficiently boost in-domain performance via supervision without incurring catastrophic forgetting. We present SPoT, a novel paradigm synergizing the surgical rectification pipeline with the binary optimization objective. Our theoretical and empirical analyses reveal that this loss acts as a sample-wise early stopping mechanism that effectively preserve

Artifact / implementation：exact-v1 `Not Disclosed — arXiv:2603.01683v1 exposes no dedicated Artifact / implementation section in the recovered exact-v1 body`；公开范围摘录：Not Disclosed。未公开的代码、commit、部署配置或复现实验不得由论文叙事反推。

<!-- claim:SF-2026-ARXIV-2603-01683:start -->只接受 arXiv:2603.01683v1 在 exact-v1 公开 workload 下的作者机制与实验主张；未披露的 model、hardware、precision、length、batch、concurrency、cost 与 production SLO 均为 Not Disclosed，不外推为通用结论。<!-- claim:SF-2026-ARXIV-2603-01683:end -->

Books Comparison：已读 `TRAIN-RLHF` 的 `books/part-04-training-system/31-rlhf.md#从机制演进到系统设计 (line 599)` 及相邻 `books/part-04-training-system/30-lora.md#本章要回答的问题 (line 10); books/part-04-training-system/32-ppo.md#本章要回答的问题 (line 10)`；现有命题为“动态 rubric、spec learning 或 on-policy distillation可以提高适应性，却会放大 reward hacking、judge correlation、density mismatch 与评价成本。它们必须通过 frozen holdout、独立 outcome evidence 和 rollback gate；反馈不足或评估失去区分力时，回退静态 rubric、SFT 或人工 adjudication。几何差异只有在 data、step 和 learning rate 匹配时才可归因于 objective。”。Decision=`No Change — Existing Coverage`；该 author-side 判断仍待fresh-context Books reviewer，Integrate 项只进入日期队列。
<!-- review:SF-2026-ARXIV-2603-01683:end -->

<!-- review:SF-2026-ARXIV-2603-01966:start -->
#### AMemGym: Interactive Memory Benchmarking for Assistants in Long-Horizon Conversations

问题与 changed constraint：长对话 memory benchmark 若只测最终回答，会混淆记忆写入、检索、更新与冲突处理。

旧路径为何合理：在该约束未出现、规模较小或 workload 更稳定时，论文所比较的旧路径仍以更少状态、更短控制链和更成熟实现提供合理基线；不能因本论文出现而静默覆盖。

机制、state/data/control owner：AMemGym 通过交互式长时程环境分别触发记忆生命周期操作，使 memory policy 在动态对话中被观察。 对应 exact-v1 `S3 — 3 AMemGym`；该机制由 `PLATFORM-EVALUATION-SYSTEM` 承载。原文定位摘录仅作核对：3 AMemGym Figure 2: An overview of the AMemGym framework. AMemGym provides an interactive environment for benchmarking and optimizing personal assistant memory, with the scenario and the task described below. LLM-based Assistants. An LLM-based assistant takes as input the observation (user input) and provides output responses (a sequence of tokens) based on its policy and its internal memory at that time (e.g., tokens in the context window, text snippets written to an external index, or its own parameters): . The i

Evaluation contract：benchmark 揭示作者任务和模型中的失败模式；不证明其任务分布代表真实助手，也不提供唯一 memory quality 指标。 exact-v1 定位为 `A5 — Appendix E Details for the self-evolution experiment`；用于核对的原文摘录：Appendix E Details for the self-evolution experiment Algorithm 1 Memory Agent Self-Evolution Loop 1: Input: Initial policy prompt , Number of evolution cycles . 2: Initialize: Agent with policy . 3: for to do 4: Interact with the AMemGym environment for one episode using policy . 5: Collect trajectory and evaluation outcomes. 6: Generate environmental feedback summary based on the interaction and outcomes. 7: Generate the updated policy prompt: . 8: Update the agent’s policy to . 9: end for 10: Output: Sequence of

证明与未证明：证据只支持上述 paper-specific workload 内的机制/测量关系；不支持把作者结果外推为其他模型、数据、硬件、精度、长度、batch、并发或 production SLO 的通用结论。

Trade-off、failure 与共存边界：生命周期覆盖提高诊断性但增加标注与 evaluator 依赖；简单一次性 QA 不需要该复杂度。 反证/限制定位为 `S6 — 6 Conclusion`；用于核对的原文摘录：6 Conclusion AMemGym introduces a scalable, interactive environment for the on-policy evaluation of conversational memory. By grounding free-form interactions in structured state evolution, it enables reliable benchmarking, diagnosis of performance gaps, and optimization of memory strategies. Our experiments confirm that AMemGym not only identifies weaknesses in existing systems but also facilitates agent self-evolut

Artifact / implementation：exact-v1 `A3 — Appendix C Implementation Details`；公开范围摘录：Appendix C Implementation Details C.1 Benchmark Statistics Our benchmark comprises 20 unique user profiles. The benchmark is designed in two configurations: a base version and an extended version (extra) with increased temporal complexity. User Diversity. The benchmark exhibits substantial demographic variation to ensure broad representativeness. Age distrib。未公开的代码、commit、部署配置或复现实验不得由论文叙事反推。

<!-- claim:SF-2026-ARXIV-2603-01966:start -->只接受 arXiv:2603.01966v1 在 exact-v1 公开 workload 下的作者机制与实验主张；未披露的 model、hardware、precision、length、batch、concurrency、cost 与 production SLO 均为 Not Disclosed，不外推为通用结论。<!-- claim:SF-2026-ARXIV-2603-01966:end -->

Books Comparison：已读 `PLATFORM-EVALUATION-SYSTEM` 的 `books/part-06-ai-infrastructure/66-evaluation-system.md#从答案评分到可执行证据 (line 1463)` 及相邻 `books/part-06-ai-infrastructure/65-kai-scheduler.md#本章要回答的问题 (line 10); books/part-06-ai-infrastructure/67-monitoring.md#本章要回答的问题 (line 10)`；现有命题为“Final anchored verifier 可以提供可扩展 outcome evidence，却不能证明每个中间 transition 正确。真实用户风格、多意图同轮和含糊修订还需要额外切片；Agent 的 Context、Memory 与 Workflow 可以消费这些状态边界，但 evaluation owner 仍负责定义 transition identity、control arm 与最终可比较性。”。Decision=`No Change — Existing Coverage`；该 author-side 判断仍待fresh-context Books reviewer，Integrate 项只进入日期队列。
<!-- review:SF-2026-ARXIV-2603-01966:end -->

## 4. Benchmark Contracts

None — 本日报不把作者结果或摘要数字重标为可跨 workload 外推的 benchmark claim。

## 5. Deep Analysis Selection

<!-- validator:deep-analysis-selection-v1 -->
| Source Family ID | Eligibility | Decision | Analysis Unit ID | Subsumed By | Priority Rationale | Narrative Ref |
| --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2603-00063 | score_7_9 | selected | DA-20260304-1 | — | 从完整 eligibility frontier 中优先覆盖独立 owner 的 durable state/control 或 evaluation contract 变化。 | analysis:DA-20260304-1 |
| SF-2026-ARXIV-2603-00195 | score_7_9 | selected | DA-20260304-2 | — | 从完整 eligibility frontier 中优先覆盖独立 owner 的 durable state/control 或 evaluation contract 变化。 | analysis:DA-20260304-2 |
| SF-2026-ARXIV-2603-00196 | score_7_9 | selected | DA-20260304-3 | — | 从完整 eligibility frontier 中优先覆盖独立 owner 的 durable state/control 或 evaluation contract 变化。 | analysis:DA-20260304-3 |
| SF-2026-ARXIV-2603-00356 | score_7_9; forced_review; potential_books_delta | not_selected | — | — | Full Source Review 已完成；相对三个叙事单元，其机制由相同 owner 或较窄 workload 承载。 | analysis-decision:SF-2026-ARXIV-2603-00356 |
| SF-2026-ARXIV-2603-00357 | score_7_9 | not_selected | — | — | Full Source Review 已完成；相对三个叙事单元，其机制由相同 owner 或较窄 workload 承载。 | analysis-decision:SF-2026-ARXIV-2603-00357 |
| SF-2026-ARXIV-2603-00495 | score_7_9 | not_selected | — | — | Full Source Review 已完成；相对三个叙事单元，其机制由相同 owner 或较窄 workload 承载。 | analysis-decision:SF-2026-ARXIV-2603-00495 |
| SF-2026-ARXIV-2603-00575 | score_7_9 | not_selected | — | — | Full Source Review 已完成；相对三个叙事单元，其机制由相同 owner 或较窄 workload 承载。 | analysis-decision:SF-2026-ARXIV-2603-00575 |
| SF-2026-ARXIV-2603-00811 | score_7_9 | not_selected | — | — | Full Source Review 已完成；相对三个叙事单元，其机制由相同 owner 或较窄 workload 承载。 | analysis-decision:SF-2026-ARXIV-2603-00811 |
| SF-2026-ARXIV-2603-01209 | score_7_9 | not_selected | — | — | Full Source Review 已完成；相对三个叙事单元，其机制由相同 owner 或较窄 workload 承载。 | analysis-decision:SF-2026-ARXIV-2603-01209 |
| SF-2026-ARXIV-2603-01630 | score_7_9 | not_selected | — | — | Full Source Review 已完成；相对三个叙事单元，其机制由相同 owner 或较窄 workload 承载。 | analysis-decision:SF-2026-ARXIV-2603-01630 |
| SF-2026-ARXIV-2603-02176 | score_7_9 | not_selected | — | — | Full Source Review 已完成；相对三个叙事单元，其机制由相同 owner 或较窄 workload 承载。 | analysis-decision:SF-2026-ARXIV-2603-02176 |
| SF-2026-ARXIV-2603-00349 | score_7_9 | not_selected | — | — | Full Source Review 已完成；相对三个叙事单元，其机制由相同 owner 或较窄 workload 承载。 | analysis-decision:SF-2026-ARXIV-2603-00349 |
| SF-2026-ARXIV-2603-00381 | score_7_9 | not_selected | — | — | Full Source Review 已完成；相对三个叙事单元，其机制由相同 owner 或较窄 workload 承载。 | analysis-decision:SF-2026-ARXIV-2603-00381 |
| SF-2026-ARXIV-2603-00468 | score_7_9 | not_selected | — | — | Full Source Review 已完成；相对三个叙事单元，其机制由相同 owner 或较窄 workload 承载。 | analysis-decision:SF-2026-ARXIV-2603-00468 |
| SF-2026-ARXIV-2603-00623 | score_7_9 | not_selected | — | — | Full Source Review 已完成；相对三个叙事单元，其机制由相同 owner 或较窄 workload 承载。 | analysis-decision:SF-2026-ARXIV-2603-00623 |
| SF-2026-ARXIV-2603-00680 | score_7_9 | not_selected | — | — | Full Source Review 已完成；相对三个叙事单元，其机制由相同 owner 或较窄 workload 承载。 | analysis-decision:SF-2026-ARXIV-2603-00680 |
| SF-2026-ARXIV-2603-00825 | score_7_9 | not_selected | — | — | Full Source Review 已完成；相对三个叙事单元，其机制由相同 owner 或较窄 workload 承载。 | analysis-decision:SF-2026-ARXIV-2603-00825 |
| SF-2026-ARXIV-2603-01058 | score_7_9 | not_selected | — | — | Full Source Review 已完成；相对三个叙事单元，其机制由相同 owner 或较窄 workload 承载。 | analysis-decision:SF-2026-ARXIV-2603-01058 |
| SF-2026-ARXIV-2603-01162 | score_7_9; forced_review; potential_books_delta | not_selected | — | — | Full Source Review 已完成；相对三个叙事单元，其机制由相同 owner 或较窄 workload 承载。 | analysis-decision:SF-2026-ARXIV-2603-01162 |
| SF-2026-ARXIV-2603-01399 | score_7_9 | not_selected | — | — | Full Source Review 已完成；相对三个叙事单元，其机制由相同 owner 或较窄 workload 承载。 | analysis-decision:SF-2026-ARXIV-2603-01399 |
| SF-2026-ARXIV-2603-01499 | score_7_9 | not_selected | — | — | Full Source Review 已完成；相对三个叙事单元，其机制由相同 owner 或较窄 workload 承载。 | analysis-decision:SF-2026-ARXIV-2603-01499 |
| SF-2026-ARXIV-2603-01960 | score_7_9 | not_selected | — | — | Full Source Review 已完成；相对三个叙事单元，其机制由相同 owner 或较窄 workload 承载。 | analysis-decision:SF-2026-ARXIV-2603-01960 |
| SF-2026-ARXIV-2603-02075 | score_7_9 | not_selected | — | — | Full Source Review 已完成；相对三个叙事单元，其机制由相同 owner 或较窄 workload 承载。 | analysis-decision:SF-2026-ARXIV-2603-02075 |
| SF-2026-ARXIV-2603-02146 | score_7_9; forced_review; potential_books_delta | not_selected | — | — | Full Source Review 已完成；相对三个叙事单元，其机制由相同 owner 或较窄 workload 承载。 | analysis-decision:SF-2026-ARXIV-2603-02146 |
| SF-2026-ARXIV-2603-02188 | score_7_9 | not_selected | — | — | Full Source Review 已完成；相对三个叙事单元，其机制由相同 owner 或较窄 workload 承载。 | analysis-decision:SF-2026-ARXIV-2603-02188 |
| SF-2026-ARXIV-2603-00188 | score_7_9 | not_selected | — | — | Full Source Review 已完成；相对三个叙事单元，其机制由相同 owner 或较窄 workload 承载。 | analysis-decision:SF-2026-ARXIV-2603-00188 |
| SF-2026-ARXIV-2603-01045 | score_7_9 | not_selected | — | — | Full Source Review 已完成；相对三个叙事单元，其机制由相同 owner 或较窄 workload 承载。 | analysis-decision:SF-2026-ARXIV-2603-01045 |
| SF-2026-ARXIV-2603-01548 | score_7_9 | not_selected | — | — | Full Source Review 已完成；相对三个叙事单元，其机制由相同 owner 或较窄 workload 承载。 | analysis-decision:SF-2026-ARXIV-2603-01548 |
| SF-2026-ARXIV-2603-01581 | score_7_9 | not_selected | — | — | Full Source Review 已完成；相对三个叙事单元，其机制由相同 owner 或较窄 workload 承载。 | analysis-decision:SF-2026-ARXIV-2603-01581 |
| SF-2026-ARXIV-2603-01639 | score_7_9 | not_selected | — | — | Full Source Review 已完成；相对三个叙事单元，其机制由相同 owner 或较窄 workload 承载。 | analysis-decision:SF-2026-ARXIV-2603-01639 |
| SF-2026-ARXIV-2603-01661 | score_7_9 | not_selected | — | — | Full Source Review 已完成；相对三个叙事单元，其机制由相同 owner 或较窄 workload 承载。 | analysis-decision:SF-2026-ARXIV-2603-01661 |
| SF-2026-ARXIV-2603-01683 | score_7_9 | not_selected | — | — | Full Source Review 已完成；相对三个叙事单元，其机制由相同 owner 或较窄 workload 承载。 | analysis-decision:SF-2026-ARXIV-2603-01683 |
| SF-2026-ARXIV-2603-01966 | score_7_9 | not_selected | — | — | Full Source Review 已完成；相对三个叙事单元，其机制由相同 owner 或较窄 workload 承载。 | analysis-decision:SF-2026-ARXIV-2603-01966 |

<!-- analysis:DA-20260304-1:start -->
### DA-20260304-1 — Measuring What AI Systems Might Do: Towards A Measurement Science in AI

旧路径在 changed constraint 未出现时仍然合理；该工作把新的状态、数据或控制责任交给 `PLATFORM-EVALUATION-SYSTEM`。exact-v1 机制为：论文把被测 disposition、measurement procedure、environment 与观测误差分开，使 evaluation claim 成为可反驳的测量对象。 证据只证明作者 evaluation contract，不能外推未披露配置。代价、failure 与下一重压力受以下边界约束：只接受 arXiv:2603.00063v1 在 exact-v1 公开 workload 下的作者机制与实验主张；未披露的 model、hardware、precision、length、batch、concurrency、cost 与 production SLO 均为 Not Disclosed，不外推为通用结论。
<!-- analysis:DA-20260304-1:end -->

<!-- analysis:DA-20260304-2:start -->
### DA-20260304-2 — Formal Analysis and Supply Chain Security for Agentic AI Skills

旧路径在 changed constraint 未出现时仍然合理；该工作把新的状态、数据或控制责任交给 `AGENT-PLATFORM`。exact-v1 机制为：工作把 Skill manifest、依赖、权限和行为属性交给形式化分析与可复查 artifact，令安装前 admission 拥有明确证据。 证据只证明作者 evaluation contract，不能外推未披露配置。代价、failure 与下一重压力受以下边界约束：只接受 arXiv:2603.00195v1 在 exact-v1 公开 workload 下的作者机制与实验主张；未披露的 model、hardware、precision、length、batch、concurrency、cost 与 production SLO 均为 Not Disclosed，不外推为通用结论。
<!-- analysis:DA-20260304-2:end -->

<!-- analysis:DA-20260304-3:start -->
### DA-20260304-3 — Your Inference Request Will Become a Black Box: Confidential Inference for Cloud-based Large Language Models

旧路径在 changed constraint 未出现时仍然合理；该工作把新的状态、数据或控制责任交给 `PLATFORM-SECURITY`。exact-v1 机制为：论文把 confidential inference 分解为隔离边界、远程证明、加密通道和可验证 runtime 组成，明确哪些请求状态由 enclave/guest、host 与客户端分别拥有。 证据只证明作者 evaluation contract，不能外推未披露配置。代价、failure 与下一重压力受以下边界约束：只接受 arXiv:2603.00196v1 在 exact-v1 公开 workload 下的作者机制与实验主张；未披露的 model、hardware、precision、length、batch、concurrency、cost 与 production SLO 均为 Not Disclosed，不外推为通用结论。
<!-- analysis:DA-20260304-3:end -->

<!-- analysis-decision:SF-2026-ARXIV-2603-00356:start -->
`Token Management in Multi-Tenant AI Inference Platforms` 已完成 full review，但不占用有限叙事单元；这不改变它的 Review Completion。
<!-- analysis-decision:SF-2026-ARXIV-2603-00356:end -->

<!-- analysis-decision:SF-2026-ARXIV-2603-00357:start -->
`SPARe: Stacked Parallelism with Adaptive Reordering for Fault-Tolerant LLM Pretraining Systems with 100k+ GPUs` 已完成 full review，但不占用有限叙事单元；这不改变它的 Review Completion。
<!-- analysis-decision:SF-2026-ARXIV-2603-00357:end -->

<!-- analysis-decision:SF-2026-ARXIV-2603-00495:start -->
`AI Runtime Infrastructure` 已完成 full review，但不占用有限叙事单元；这不改变它的 Review Completion。
<!-- analysis-decision:SF-2026-ARXIV-2603-00495:end -->

<!-- analysis-decision:SF-2026-ARXIV-2603-00575:start -->
`SWE-Hub: A Unified Production System for Scalable, Executable Software Engineering Tasks` 已完成 full review，但不占用有限叙事单元；这不改变它的 Review Completion。
<!-- analysis-decision:SF-2026-ARXIV-2603-00575:end -->

<!-- analysis-decision:SF-2026-ARXIV-2603-00811:start -->
`Curation Leaks: Membership Inference Attacks against Data Curation for Machine Learning` 已完成 full review，但不占用有限叙事单元；这不改变它的 Review Completion。
<!-- analysis-decision:SF-2026-ARXIV-2603-00811:end -->

<!-- analysis-decision:SF-2026-ARXIV-2603-01209:start -->
`Agents Learn Their Runtime: Interpreter Persistence as Training-Time Semantics` 已完成 full review，但不占用有限叙事单元；这不改变它的 Review Completion。
<!-- analysis-decision:SF-2026-ARXIV-2603-01209:end -->

<!-- analysis-decision:SF-2026-ARXIV-2603-01630:start -->
`SEED-SET: Scalable Evolving Experimental Design for System-level Ethical Testing` 已完成 full review，但不占用有限叙事单元；这不改变它的 Review Completion。
<!-- analysis-decision:SF-2026-ARXIV-2603-01630:end -->

<!-- analysis-decision:SF-2026-ARXIV-2603-02176:start -->
`Organizing, Orchestrating, and Benchmarking Agent Skills at Ecosystem Scale` 已完成 full review，但不占用有限叙事单元；这不改变它的 Review Completion。
<!-- analysis-decision:SF-2026-ARXIV-2603-02176:end -->

<!-- analysis-decision:SF-2026-ARXIV-2603-00349:start -->
`COOP$^2$: Defining, Observing, and Repairing Cooperation in LLM Multi-Agent Systems` 已完成 full review，但不占用有限叙事单元；这不改变它的 Review Completion。
<!-- analysis-decision:SF-2026-ARXIV-2603-00349:end -->

<!-- analysis-decision:SF-2026-ARXIV-2603-00381:start -->
`Verifier-Bound Communication for LLM Agents: Certified Bounds on Covert Signaling` 已完成 full review，但不占用有限叙事单元；这不改变它的 Review Completion。
<!-- analysis-decision:SF-2026-ARXIV-2603-00381:end -->

<!-- analysis-decision:SF-2026-ARXIV-2603-00468:start -->
`Cloud-OpsBench: A Reproducible Benchmark for Agentic Root Cause Analysis in Cloud Systems` 已完成 full review，但不占用有限叙事单元；这不改变它的 Review Completion。
<!-- analysis-decision:SF-2026-ARXIV-2603-00468:end -->

<!-- analysis-decision:SF-2026-ARXIV-2603-00623:start -->
`TraceSIR: A Multi-Agent Framework for Structured Analysis and Reporting of Agentic Execution Traces` 已完成 full review，但不占用有限叙事单元；这不改变它的 Review Completion。
<!-- analysis-decision:SF-2026-ARXIV-2603-00623:end -->

<!-- analysis-decision:SF-2026-ARXIV-2603-00680:start -->
`MemPO: Self-Memory Policy Optimization for Long-Horizon Agents` 已完成 full review，但不占用有限叙事单元；这不改变它的 Review Completion。
<!-- analysis-decision:SF-2026-ARXIV-2603-00680:end -->

<!-- analysis-decision:SF-2026-ARXIV-2603-00825:start -->
`COMBAT: Conditional World Models for Behavioral Agent Training` 已完成 full review，但不占用有限叙事单元；这不改变它的 Review Completion。
<!-- analysis-decision:SF-2026-ARXIV-2603-00825:end -->

<!-- analysis-decision:SF-2026-ARXIV-2603-01058:start -->
`TriMoE: Augmenting GPU with AMX-Enabled CPU and DIMM-NDP for High-Throughput MoE Inference via Offloading` 已完成 full review，但不占用有限叙事单元；这不改变它的 Review Completion。
<!-- analysis-decision:SF-2026-ARXIV-2603-01058:end -->

<!-- analysis-decision:SF-2026-ARXIV-2603-01162:start -->
`Demystifying Group Relative Policy Optimization: Its Policy Gradient is a U-Statistic` 已完成 full review，但不占用有限叙事单元；这不改变它的 Review Completion。
<!-- analysis-decision:SF-2026-ARXIV-2603-01162:end -->

<!-- analysis-decision:SF-2026-ARXIV-2603-01399:start -->
`Quasar: Quantized Self-Speculative Acceleration for Rapid Inference via Memory-Efficient Verification` 已完成 full review，但不占用有限叙事单元；这不改变它的 Review Completion。
<!-- analysis-decision:SF-2026-ARXIV-2603-01399:end -->

<!-- analysis-decision:SF-2026-ARXIV-2603-01499:start -->
`Towards Privacy-Preserving LLM Inference via Covariant Obfuscation (Technical Report)` 已完成 full review，但不占用有限叙事单元；这不改变它的 Review Completion。
<!-- analysis-decision:SF-2026-ARXIV-2603-01499:end -->

<!-- analysis-decision:SF-2026-ARXIV-2603-01960:start -->
`TiledAttention: a CUDA Tile SDPA Kernel for PyTorch` 已完成 full review，但不占用有限叙事单元；这不改变它的 Review Completion。
<!-- analysis-decision:SF-2026-ARXIV-2603-01960:end -->

<!-- analysis-decision:SF-2026-ARXIV-2603-02075:start -->
`Trident: Adaptive Scheduling for Heterogeneous Multimodal Data Pipelines` 已完成 full review，但不占用有限叙事单元；这不改变它的 Review Completion。
<!-- analysis-decision:SF-2026-ARXIV-2603-02075:end -->

<!-- analysis-decision:SF-2026-ARXIV-2603-02146:start -->
`LongRLVR: Long-Context Reinforcement Learning Requires Verifiable Context Rewards` 已完成 full review，但不占用有限叙事单元；这不改变它的 Review Completion。
<!-- analysis-decision:SF-2026-ARXIV-2603-02146:end -->

<!-- analysis-decision:SF-2026-ARXIV-2603-02188:start -->
`Multi-Head Low-Rank Attention` 已完成 full review，但不占用有限叙事单元；这不改变它的 Review Completion。
<!-- analysis-decision:SF-2026-ARXIV-2603-02188:end -->

<!-- analysis-decision:SF-2026-ARXIV-2603-00188:start -->
`ST-Lite: Training-Free KV Cache Compression with Spatio-Trajectory Guidance for Long-Horizon GUI Agents` 已完成 full review，但不占用有限叙事单元；这不改变它的 Review Completion。
<!-- analysis-decision:SF-2026-ARXIV-2603-00188:end -->

<!-- analysis-decision:SF-2026-ARXIV-2603-01045:start -->
`Silo-Bench: A Scalable Environment for Evaluating Distributed Coordination in Multi-Agent LLM Systems` 已完成 full review，但不占用有限叙事单元；这不改变它的 Review Completion。
<!-- analysis-decision:SF-2026-ARXIV-2603-01045:end -->

<!-- analysis-decision:SF-2026-ARXIV-2603-01548:start -->
`Graph-Based Self-Healing Tool Routing for Cost-Efficient LLM Agents` 已完成 full review，但不占用有限叙事单元；这不改变它的 Review Completion。
<!-- analysis-decision:SF-2026-ARXIV-2603-01548:end -->

<!-- analysis-decision:SF-2026-ARXIV-2603-01581:start -->
`KERV: Kinematic-Rectified Speculative Decoding for Embodied VLA Models` 已完成 full review，但不占用有限叙事单元；这不改变它的 Review Completion。
<!-- analysis-decision:SF-2026-ARXIV-2603-01581:end -->

<!-- analysis-decision:SF-2026-ARXIV-2603-01639:start -->
`Learning to Draft: Adaptive Speculative Decoding with Reinforcement Learning` 已完成 full review，但不占用有限叙事单元；这不改变它的 Review Completion。
<!-- analysis-decision:SF-2026-ARXIV-2603-01639:end -->

<!-- analysis-decision:SF-2026-ARXIV-2603-01661:start -->
`HeRo: Adaptive Orchestration of Agentic RAG on Heterogeneous Mobile SoC` 已完成 full review，但不占用有限叙事单元；这不改变它的 Review Completion。
<!-- analysis-decision:SF-2026-ARXIV-2603-01661:end -->

<!-- analysis-decision:SF-2026-ARXIV-2603-01683:start -->
`Surgical Post-Training: Proximal On-Policy Distillation for Reasoning with Knowledge Retention` 已完成 full review，但不占用有限叙事单元；这不改变它的 Review Completion。
<!-- analysis-decision:SF-2026-ARXIV-2603-01683:end -->

<!-- analysis-decision:SF-2026-ARXIV-2603-01966:start -->
`AMemGym: Interactive Memory Benchmarking for Assistants in Long-Horizon Conversations` 已完成 full review，但不占用有限叙事单元；这不改变它的 Review Completion。
<!-- analysis-decision:SF-2026-ARXIV-2603-01966:end -->

## 6. Books Comparison

<!-- validator:books-comparison-v1 -->
| Source Family ID | Stable Node ID | Target Chapter Ref | Adjacent Chapter Refs | Existing Proposition | New Evidence Delta | Evolution Relation | Decision | Books Review Ref |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2603-00063 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#从“有结果”到可追责、可干预的 Evidence (line 2326) | books/part-06-ai-infrastructure/65-kai-scheduler.md#本章要回答的问题 (line 10); books/part-06-ai-infrastructure/67-monitoring.md#本章要回答的问题 (line 10) | existing:SF-2026-ARXIV-2603-00063 | delta:SF-2026-ARXIV-2603-00063 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-00063 |
| SF-2026-ARXIV-2603-00195 | AGENT-PLATFORM | books/part-07-agent/84-agent-platform.md#Skill Drift 应检测角色契约，而不是任意变化 (line 787) | books/part-07-agent/83-mcp.md#本章要回答的问题 (line 10) | existing:SF-2026-ARXIV-2603-00195 | delta:SF-2026-ARXIV-2603-00195 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-00195 |
| SF-2026-ARXIV-2603-00196 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#风险管理而不是一次性认证 (line 1131) | books/part-06-ai-infrastructure/71-multi-tenant.md#本章要回答的问题 (line 10); books/part-06-ai-infrastructure/73-production-best-practice.md#本章要回答的问题 (line 10) | existing:SF-2026-ARXIV-2603-00196 | delta:SF-2026-ARXIV-2603-00196 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-00196 |
| SF-2026-ARXIV-2603-00356 | INFER-SCHEDULING | books/part-05-inference-system/56-inference-scheduling.md#从逐配置压测到校准后的配置搜索 (line 581) | books/part-05-inference-system/55-pd-disaggregation.md#本章要回答的问题 (line 10); books/part-06-ai-infrastructure/57-what-is-ai-platform.md#本章要回答的问题 (line 10) | existing:SF-2026-ARXIV-2603-00356 | delta:SF-2026-ARXIV-2603-00356 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2603-00356 |
| SF-2026-ARXIV-2603-00357 | TRAIN-CHECKPOINT | books/part-04-training-system/35-checkpoint.md#异步保存移动了 Pause，而没有删除 IO (line 250) | books/part-04-training-system/34-dpo.md#本章要回答的问题 (line 10); books/part-04-training-system/36-distributed-training.md#本章要回答的问题 (line 10) | existing:SF-2026-ARXIV-2603-00357 | delta:SF-2026-ARXIV-2603-00357 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-00357 |
| SF-2026-ARXIV-2603-00495 | PLATFORM-FOUNDATIONS | books/part-06-ai-infrastructure/57-what-is-ai-platform.md#本章在知识树中的位置 (line 152) | books/part-05-inference-system/56-inference-scheduling.md#本章要回答的问题 (line 10); books/part-06-ai-infrastructure/58-kubeflow.md#本章要回答的问题 (line 10) | existing:SF-2026-ARXIV-2603-00495 | delta:SF-2026-ARXIV-2603-00495 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-00495 |
| SF-2026-ARXIV-2603-00575 | AGENT-PLATFORM | books/part-07-agent/84-agent-platform.md#Evaluation 从答案扩展到 Trajectory (line 580) | books/part-07-agent/83-mcp.md#本章要回答的问题 (line 10) | existing:SF-2026-ARXIV-2603-00575 | delta:SF-2026-ARXIV-2603-00575 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-00575 |
| SF-2026-ARXIV-2603-00811 | TRAIN-DATA | books/part-04-training-system/27-data.md#Quality filtering 在过滤什么 (line 262) | books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#本章要回答的问题 (line 10); books/part-04-training-system/28-pretraining.md#本章要回答的问题 (line 10) | existing:SF-2026-ARXIV-2603-00811 | delta:SF-2026-ARXIV-2603-00811 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-00811 |
| SF-2026-ARXIV-2603-01209 | AGENT-PLATFORM | books/part-07-agent/84-agent-platform.md#Scheduling 不只是 GPU (line 471) | books/part-07-agent/83-mcp.md#本章要回答的问题 (line 10) | existing:SF-2026-ARXIV-2603-01209 | delta:SF-2026-ARXIV-2603-01209 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-01209 |
| SF-2026-ARXIV-2603-01630 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#从答案评分到可执行证据 (line 936) | books/part-06-ai-infrastructure/65-kai-scheduler.md#本章要回答的问题 (line 10); books/part-06-ai-infrastructure/67-monitoring.md#本章要回答的问题 (line 10) | existing:SF-2026-ARXIV-2603-01630 | delta:SF-2026-ARXIV-2603-01630 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-01630 |
| SF-2026-ARXIV-2603-02176 | AGENT-PLATFORM | books/part-07-agent/84-agent-platform.md#Agent Definition 与 Run Identity (line 192) | books/part-07-agent/83-mcp.md#本章要回答的问题 (line 10) | existing:SF-2026-ARXIV-2603-02176 | delta:SF-2026-ARXIV-2603-02176 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-02176 |
| SF-2026-ARXIV-2603-00349 | AGENT-MULTI-AGENT | books/part-07-agent/82-multi-agent.md#Message 不是 State (line 356) | books/part-07-agent/81-workflow.md#本章要回答的问题 (line 10); books/part-07-agent/83-mcp.md#本章要回答的问题 (line 10) | existing:SF-2026-ARXIV-2603-00349 | delta:SF-2026-ARXIV-2603-00349 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-00349 |
| SF-2026-ARXIV-2603-00381 | AGENT-MULTI-AGENT | books/part-07-agent/82-multi-agent.md#从机制演进到系统设计 (line 639) | books/part-07-agent/81-workflow.md#本章要回答的问题 (line 10); books/part-07-agent/83-mcp.md#本章要回答的问题 (line 10) | existing:SF-2026-ARXIV-2603-00381 | delta:SF-2026-ARXIV-2603-00381 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-00381 |
| SF-2026-ARXIV-2603-00468 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#Action Control 需要 Sensitivity 与 Invariance 双臂证据 (line 2452) | books/part-06-ai-infrastructure/65-kai-scheduler.md#本章要回答的问题 (line 10); books/part-06-ai-infrastructure/67-monitoring.md#本章要回答的问题 (line 10) | existing:SF-2026-ARXIV-2603-00468 | delta:SF-2026-ARXIV-2603-00468 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-00468 |
| SF-2026-ARXIV-2603-00623 | PLATFORM-TRACE | books/part-06-ai-infrastructure/69-trace.md#本章要回答的问题 (line 14) | books/part-06-ai-infrastructure/68-logging.md#本章要回答的问题 (line 10); books/part-06-ai-infrastructure/70-cost.md#本章要回答的问题 (line 10) | existing:SF-2026-ARXIV-2603-00623 | delta:SF-2026-ARXIV-2603-00623 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-00623 |
| SF-2026-ARXIV-2603-00680 | AGENT-MEMORY | books/part-07-agent/77-memory.md#从原始轨迹到派生策略：Memory 的演进不是无限追加 (line 498) | books/part-07-agent/76-rag.md#本章要回答的问题 (line 10); books/part-07-agent/78-tool-calling.md#本章要回答的问题 (line 10) | existing:SF-2026-ARXIV-2603-00680 | delta:SF-2026-ARXIV-2603-00680 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-00680 |
| SF-2026-ARXIV-2603-00825 | MULTIMODAL-WORLD-MODELS | books/part-03-multimodal-world-models/25-multimodal-world-models.md#本章要回答的问题 (line 8) | books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md#本章要回答的问题 (line 10); books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#本章要回答的问题 (line 10) | existing:SF-2026-ARXIV-2603-00825 | delta:SF-2026-ARXIV-2603-00825 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-00825 |
| SF-2026-ARXIV-2603-01058 | INFER-GPU-MEMORY | books/part-05-inference-system/54-gpu-memory.md#三类缓解路径 (line 230) | books/part-05-inference-system/53-kserve-llm.md#本章要回答的问题 (line 10); books/part-05-inference-system/55-pd-disaggregation.md#本章要回答的问题 (line 10) | existing:SF-2026-ARXIV-2603-01058 | delta:SF-2026-ARXIV-2603-01058 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-01058 |
| SF-2026-ARXIV-2603-01162 | TRAIN-GRPO | books/part-04-training-system/33-grpo.md#Group-relative Gradient 不是独立样本均值 (line 219) | books/part-04-training-system/32-ppo.md#本章要回答的问题 (line 10); books/part-04-training-system/34-dpo.md#本章要回答的问题 (line 10) | existing:SF-2026-ARXIV-2603-01162 | delta:SF-2026-ARXIV-2603-01162 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2603-01162 |
| SF-2026-ARXIV-2603-01399 | INFER-SPECULATIVE-DECODING | books/part-05-inference-system/48-speculative-decoding.md#本章要回答的问题 (line 16) | books/part-05-inference-system/47-pagedattention.md#本章要回答的问题 (line 10); books/part-05-inference-system/49-tensorrt-llm.md#本章要回答的问题 (line 10) | existing:SF-2026-ARXIV-2603-01399 | delta:SF-2026-ARXIV-2603-01399 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-01399 |
| SF-2026-ARXIV-2603-01499 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#风险管理而不是一次性认证 (line 1091) | books/part-06-ai-infrastructure/71-multi-tenant.md#本章要回答的问题 (line 10); books/part-06-ai-infrastructure/73-production-best-practice.md#本章要回答的问题 (line 10) | existing:SF-2026-ARXIV-2603-01499 | delta:SF-2026-ARXIV-2603-01499 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-01499 |
| SF-2026-ARXIV-2603-01960 | INFER-TENSORRT-LLM | books/part-05-inference-system/49-tensorrt-llm.md#从 Linear 语义到 GEMM 执行 (line 267) | books/part-05-inference-system/48-speculative-decoding.md#本章要回答的问题 (line 10); books/part-05-inference-system/50-vllm.md#本章要回答的问题 (line 10) | existing:SF-2026-ARXIV-2603-01960 | delta:SF-2026-ARXIV-2603-01960 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-01960 |
| SF-2026-ARXIV-2603-02075 | TRAIN-DATA | books/part-04-training-system/27-data.md#数据分布就是优化权重 (line 152) | books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#本章要回答的问题 (line 10); books/part-04-training-system/28-pretraining.md#本章要回答的问题 (line 10) | existing:SF-2026-ARXIV-2603-02075 | delta:SF-2026-ARXIV-2603-02075 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-02075 |
| SF-2026-ARXIV-2603-02146 | TRAIN-GRPO | books/part-04-training-system/33-grpo.md#长上下文 RL 还要验证 Context 是否真正被使用 (line 451) | books/part-04-training-system/32-ppo.md#本章要回答的问题 (line 10); books/part-04-training-system/34-dpo.md#本章要回答的问题 (line 10) | existing:SF-2026-ARXIV-2603-02146 | delta:SF-2026-ARXIV-2603-02146 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2603-02146 |
| SF-2026-ARXIV-2603-02188 | MODEL-MULTI-HEAD-ATTENTION | books/part-02-model/15-multi-head-attention.md#本章要回答的问题 (line 12) | books/part-02-model/14-self-attention.md#本章要回答的问题 (line 10); books/part-02-model/16-feed-forward-mlp.md#本章要回答的问题 (line 10) | existing:SF-2026-ARXIV-2603-02188 | delta:SF-2026-ARXIV-2603-02188 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-02188 |
| SF-2026-ARXIV-2603-00188 | INFER-KV-CACHE | books/part-05-inference-system/45-why-kv-cache-speeds-up.md#KV Cache 的生命周期 (line 517) | books/part-05-inference-system/44-decode.md#本章要回答的问题 (line 10); books/part-05-inference-system/46-continuous-batching.md#本章要回答的问题 (line 10) | existing:SF-2026-ARXIV-2603-00188 | delta:SF-2026-ARXIV-2603-00188 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-00188 |
| SF-2026-ARXIV-2603-01045 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#评估对象有四个层次 (line 417) | books/part-06-ai-infrastructure/65-kai-scheduler.md#本章要回答的问题 (line 10); books/part-06-ai-infrastructure/67-monitoring.md#本章要回答的问题 (line 10) | existing:SF-2026-ARXIV-2603-01045 | delta:SF-2026-ARXIV-2603-01045 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-01045 |
| SF-2026-ARXIV-2603-01548 | AGENT-TOOL-CALLING | books/part-07-agent/78-tool-calling.md#Evaluation 与 Observability (line 365) | books/part-07-agent/77-memory.md#本章要回答的问题 (line 10); books/part-07-agent/79-planning.md#本章要回答的问题 (line 10) | existing:SF-2026-ARXIV-2603-01548 | delta:SF-2026-ARXIV-2603-01548 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-01548 |
| SF-2026-ARXIV-2603-01581 | INFER-SPECULATIVE-DECODING | books/part-05-inference-system/48-speculative-decoding.md#本章要回答的问题 (line 12) | books/part-05-inference-system/47-pagedattention.md#本章要回答的问题 (line 10); books/part-05-inference-system/49-tensorrt-llm.md#本章要回答的问题 (line 10) | existing:SF-2026-ARXIV-2603-01581 | delta:SF-2026-ARXIV-2603-01581 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-01581 |
| SF-2026-ARXIV-2603-01639 | INFER-SPECULATIVE-DECODING | books/part-05-inference-system/48-speculative-decoding.md#本章要回答的问题 (line 16) | books/part-05-inference-system/47-pagedattention.md#本章要回答的问题 (line 10); books/part-05-inference-system/49-tensorrt-llm.md#本章要回答的问题 (line 10) | existing:SF-2026-ARXIV-2603-01639 | delta:SF-2026-ARXIV-2603-01639 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-01639 |
| SF-2026-ARXIV-2603-01661 | INFER-SCHEDULING | books/part-05-inference-system/56-inference-scheduling.md#本章在知识树中的位置 (line 853) | books/part-05-inference-system/55-pd-disaggregation.md#本章要回答的问题 (line 10); books/part-06-ai-infrastructure/57-what-is-ai-platform.md#本章要回答的问题 (line 10) | existing:SF-2026-ARXIV-2603-01661 | delta:SF-2026-ARXIV-2603-01661 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-01661 |
| SF-2026-ARXIV-2603-01683 | TRAIN-RLHF | books/part-04-training-system/31-rlhf.md#从机制演进到系统设计 (line 599) | books/part-04-training-system/30-lora.md#本章要回答的问题 (line 10); books/part-04-training-system/32-ppo.md#本章要回答的问题 (line 10) | existing:SF-2026-ARXIV-2603-01683 | delta:SF-2026-ARXIV-2603-01683 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-01683 |
| SF-2026-ARXIV-2603-01966 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#从答案评分到可执行证据 (line 1463) | books/part-06-ai-infrastructure/65-kai-scheduler.md#本章要回答的问题 (line 10); books/part-06-ai-infrastructure/67-monitoring.md#本章要回答的问题 (line 10) | existing:SF-2026-ARXIV-2603-01966 | delta:SF-2026-ARXIV-2603-01966 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2603-01966 |

<!-- existing:SF-2026-ARXIV-2603-00063:start -->
author-side 已读 current owner `PLATFORM-EVALUATION-SYSTEM` 的具体命题：看到异常高分后再估计 benchmark contamination，无法区分记忆、能力和数据生态。更强的协议在可控训练副本中按已知比例注入样本，拟合 contamination–response curve，再把目标 run 映射到带不确定性的校正区间。它把污染从传闻变成可复现实验，但需要训练数据写权限与未污染 counterfactual，闭源模型通常不具备这些条件；此时只能报告疑似污染而不能伪造校正分。现有证据仅覆盖披露模型与五类 benchmark。
<!-- existing:SF-2026-ARXIV-2603-00063:end -->

<!-- delta:SF-2026-ARXIV-2603-00063:start -->
论文把被测 disposition、measurement procedure、environment 与观测误差分开，使 evaluation claim 成为可反驳的测量对象。
<!-- delta:SF-2026-ARXIV-2603-00063:end -->

<!-- books-review:SF-2026-ARXIV-2603-00063:start -->
Decision=`No Change — Existing Coverage`；owner=`PLATFORM-EVALUATION-SYSTEM`；target=`books/part-06-ai-infrastructure/66-evaluation-system.md#从“有结果”到可追责、可干预的 Evidence (line 2326)`；adjacent=`books/part-06-ai-infrastructure/65-kai-scheduler.md#本章要回答的问题 (line 10); books/part-06-ai-infrastructure/67-monitoring.md#本章要回答的问题 (line 10)`。证据边界：只接受 arXiv:2603.00063v1 在 exact-v1 公开 workload 下的作者机制与实验主张；未披露的 model、hardware、precision、length、batch、concurrency、cost 与 production SLO 均为 Not Disclosed，不外推为通用结论。 该判断尚未由 fresh-context Books reviewer 接受；Integrate 项只进入日期 queue，不写共享 Books。
<!-- books-review:SF-2026-ARXIV-2603-00063:end -->

<!-- existing:SF-2026-ARXIV-2603-00195:start -->
author-side 已读 current owner `AGENT-PLATFORM` 的具体命题：契约级监控减少无关告警，却把 contract extractor、probe 和 live-condition source 变成新的可信组件；文档遗漏或角色抽取错误会造成漏报。无法建立可靠契约时，应保留 pinned dependency、canary execution、人工 review 与失败后回滚，而不能因为版本字符串未变就宣称 skill 可用。[受限证据：arXiv:2605.10990v1]
<!-- existing:SF-2026-ARXIV-2603-00195:end -->

<!-- delta:SF-2026-ARXIV-2603-00195:start -->
工作把 Skill manifest、依赖、权限和行为属性交给形式化分析与可复查 artifact，令安装前 admission 拥有明确证据。
<!-- delta:SF-2026-ARXIV-2603-00195:end -->

<!-- books-review:SF-2026-ARXIV-2603-00195:start -->
Decision=`No Change — Existing Coverage`；owner=`AGENT-PLATFORM`；target=`books/part-07-agent/84-agent-platform.md#Skill Drift 应检测角色契约，而不是任意变化 (line 787)`；adjacent=`books/part-07-agent/83-mcp.md#本章要回答的问题 (line 10)`。证据边界：只接受 arXiv:2603.00195v1 在 exact-v1 公开 workload 下的作者机制与实验主张；未披露的 model、hardware、precision、length、batch、concurrency、cost 与 production SLO 均为 Not Disclosed，不外推为通用结论。 该判断尚未由 fresh-context Books reviewer 接受；Integrate 项只进入日期 queue，不写共享 Books。
<!-- books-review:SF-2026-ARXIV-2603-00195:end -->

<!-- existing:SF-2026-ARXIV-2603-00196:start -->
author-side 已读 current owner `PLATFORM-SECURITY` 的具体命题：即使原始输入留在 client，split inference 仍会把 intermediate activation 暴露给 server。旧的“在本地跑前几层即可隐藏输入”只在 activation 对攻击者确实不可逆、split point 与模型固定时成立；server-visible tensor、layer identity、shape/precision 和 auxiliary knowledge 变化后，activation matching/inversion 可以把中间状态重新关联到输入。client 拥有原文与允许的 split policy，server runtime 只拥有执行所需 activation，security plane 则必须测试每个候选 split point 的可重建性并记录 attacker capability。更深本地计算或 activation protection 能降低暴露，却增加 client compute、带宽、精度损失与部署复杂度；风险无法校准时回退本地完整推理、TEE/MPC 或可信服务端。`arXiv:2605.23158v1` 的 §3、§4.1 至 §
<!-- existing:SF-2026-ARXIV-2603-00196:end -->

<!-- delta:SF-2026-ARXIV-2603-00196:start -->
论文把 confidential inference 分解为隔离边界、远程证明、加密通道和可验证 runtime 组成，明确哪些请求状态由 enclave/guest、host 与客户端分别拥有。
<!-- delta:SF-2026-ARXIV-2603-00196:end -->

<!-- books-review:SF-2026-ARXIV-2603-00196:start -->
Decision=`No Change — Existing Coverage`；owner=`PLATFORM-SECURITY`；target=`books/part-06-ai-infrastructure/72-security.md#风险管理而不是一次性认证 (line 1131)`；adjacent=`books/part-06-ai-infrastructure/71-multi-tenant.md#本章要回答的问题 (line 10); books/part-06-ai-infrastructure/73-production-best-practice.md#本章要回答的问题 (line 10)`。证据边界：只接受 arXiv:2603.00196v1 在 exact-v1 公开 workload 下的作者机制与实验主张；未披露的 model、hardware、precision、length、batch、concurrency、cost 与 production SLO 均为 Not Disclosed，不外推为通用结论。 该判断尚未由 fresh-context Books reviewer 接受；Integrate 项只进入日期 queue，不写共享 Books。
<!-- books-review:SF-2026-ARXIV-2603-00196:end -->

<!-- existing:SF-2026-ARXIV-2603-00356:start -->
author-side 已读 current owner `INFER-SCHEDULING` 的具体命题：Replica 已固定时，scheduler 只需在同构候选中 placement；边缘设备、精度容忍和带宽差异同时出现后，请求真正选择的是 `(model family, size, quantization, device)`。先为 accuracy、latency、resource 与 response size 建立版本化预测，再在 request tolerance、capacity、bandwidth、concurrency 与 deadline 下联合 admission，可以避免把一个质量不满足的快速配置误当可行解。
<!-- existing:SF-2026-ARXIV-2603-00356:end -->

<!-- delta:SF-2026-ARXIV-2603-00356:start -->
论文把 token budget、admission、运行中配额与 reclaim 连接起来，使平台在请求进入和执行期间都能控制 token 责任，而非只按 request count 排队。
<!-- delta:SF-2026-ARXIV-2603-00356:end -->

<!-- books-review:SF-2026-ARXIV-2603-00356:start -->
Decision=`Integrate`；owner=`INFER-SCHEDULING`；target=`books/part-05-inference-system/56-inference-scheduling.md#从逐配置压测到校准后的配置搜索 (line 581)`；adjacent=`books/part-05-inference-system/55-pd-disaggregation.md#本章要回答的问题 (line 10); books/part-06-ai-infrastructure/57-what-is-ai-platform.md#本章要回答的问题 (line 10)`。证据边界：只接受 arXiv:2603.00356v1 在 exact-v1 公开 workload 下的作者机制与实验主张；未披露的 model、hardware、precision、length、batch、concurrency、cost 与 production SLO 均为 Not Disclosed，不外推为通用结论。 该判断尚未由 fresh-context Books reviewer 接受；Integrate 项只进入日期 queue，不写共享 Books。
<!-- books-review:SF-2026-ARXIV-2603-00356:end -->

<!-- existing:SF-2026-ARXIV-2603-00357:start -->
author-side 已读 current owner `TRAIN-CHECKPOINT` 的具体命题：→ coalesce fragmented tensor shards; serialize only objects that require it
<!-- existing:SF-2026-ARXIV-2603-00357:end -->

<!-- delta:SF-2026-ARXIV-2603-00357:start -->
SPARe 叠加并行冗余与故障后的 adaptive reordering，把 surviving work、replacement 和恢复顺序交给运行时而非整作业重启。
<!-- delta:SF-2026-ARXIV-2603-00357:end -->

<!-- books-review:SF-2026-ARXIV-2603-00357:start -->
Decision=`No Change — Existing Coverage`；owner=`TRAIN-CHECKPOINT`；target=`books/part-04-training-system/35-checkpoint.md#异步保存移动了 Pause，而没有删除 IO (line 250)`；adjacent=`books/part-04-training-system/34-dpo.md#本章要回答的问题 (line 10); books/part-04-training-system/36-distributed-training.md#本章要回答的问题 (line 10)`。证据边界：只接受 arXiv:2603.00357v1 在 exact-v1 公开 workload 下的作者机制与实验主张；未披露的 model、hardware、precision、length、batch、concurrency、cost 与 production SLO 均为 Not Disclosed，不外推为通用结论。 该判断尚未由 fresh-context Books reviewer 接受；Integrate 项只进入日期 queue，不写共享 Books。
<!-- books-review:SF-2026-ARXIV-2603-00357:end -->

<!-- existing:SF-2026-ARXIV-2603-00495:start -->
author-side 已读 current owner `PLATFORM-FOUNDATIONS` 的具体命题：Part VII Agent runtime and action governance
<!-- existing:SF-2026-ARXIV-2603-00495:end -->

<!-- delta:SF-2026-ARXIV-2603-00495:start -->
AI Runtime Infrastructure 将模型 artifact、执行计划、device runtime 和 platform control 分层，显式化跨层接口而不是把所有责任塞进框架。
<!-- delta:SF-2026-ARXIV-2603-00495:end -->

<!-- books-review:SF-2026-ARXIV-2603-00495:start -->
Decision=`No Change — Existing Coverage`；owner=`PLATFORM-FOUNDATIONS`；target=`books/part-06-ai-infrastructure/57-what-is-ai-platform.md#本章在知识树中的位置 (line 152)`；adjacent=`books/part-05-inference-system/56-inference-scheduling.md#本章要回答的问题 (line 10); books/part-06-ai-infrastructure/58-kubeflow.md#本章要回答的问题 (line 10)`。证据边界：只接受 arXiv:2603.00495v1 在 exact-v1 公开 workload 下的作者机制与实验主张；未披露的 model、hardware、precision、length、batch、concurrency、cost 与 production SLO 均为 Not Disclosed，不外推为通用结论。 该判断尚未由 fresh-context Books reviewer 接受；Integrate 项只进入日期 queue，不写共享 Books。
<!-- books-review:SF-2026-ARXIV-2603-00495:end -->

<!-- existing:SF-2026-ARXIV-2603-00575:start -->
author-side 已读 current owner `AGENT-PLATFORM` 的具体命题：Evaluation environment 要隔离真实副作用，并记录 model/tool/index versions。Benchmark score 不自动代表 production workload；AgentBench、SWE-bench 等提供任务入口，也暴露 long-horizon evaluation、environment leakage 和 verifier quality 的困难。
<!-- existing:SF-2026-ARXIV-2603-00575:end -->

<!-- delta:SF-2026-ARXIV-2603-00575:start -->
SWE-Hub 把 repository、环境构建、任务合成、执行验证和规模化调度组织成统一生产流水，使 executable task 成为版本化资产。
<!-- delta:SF-2026-ARXIV-2603-00575:end -->

<!-- books-review:SF-2026-ARXIV-2603-00575:start -->
Decision=`No Change — Existing Coverage`；owner=`AGENT-PLATFORM`；target=`books/part-07-agent/84-agent-platform.md#Evaluation 从答案扩展到 Trajectory (line 580)`；adjacent=`books/part-07-agent/83-mcp.md#本章要回答的问题 (line 10)`。证据边界：只接受 arXiv:2603.00575v1 在 exact-v1 公开 workload 下的作者机制与实验主张；未披露的 model、hardware、precision、length、batch、concurrency、cost 与 production SLO 均为 Not Disclosed，不外推为通用结论。 该判断尚未由 fresh-context Books reviewer 接受；Integrate 项只进入日期 queue，不写共享 Books。
<!-- books-review:SF-2026-ARXIV-2603-00575:end -->

<!-- existing:SF-2026-ARXIV-2603-00811:start -->
author-side 已读 current owner `TRAIN-DATA` 的具体命题：-> verify final state against original constraints
<!-- existing:SF-2026-ARXIV-2603-00811:end -->

<!-- delta:SF-2026-ARXIV-2603-00811:start -->
Curation Leaks 将攻击目标从 training membership 扩展到 selection membership，并沿 curator 输出和模型行为测量选择决策泄露。
<!-- delta:SF-2026-ARXIV-2603-00811:end -->

<!-- books-review:SF-2026-ARXIV-2603-00811:start -->
Decision=`No Change — Existing Coverage`；owner=`TRAIN-DATA`；target=`books/part-04-training-system/27-data.md#Quality filtering 在过滤什么 (line 262)`；adjacent=`books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#本章要回答的问题 (line 10); books/part-04-training-system/28-pretraining.md#本章要回答的问题 (line 10)`。证据边界：只接受 arXiv:2603.00811v1 在 exact-v1 公开 workload 下的作者机制与实验主张；未披露的 model、hardware、precision、length、batch、concurrency、cost 与 production SLO 均为 Not Disclosed，不外推为通用结论。 该判断尚未由 fresh-context Books reviewer 接受；Integrate 项只进入日期 queue，不写共享 Books。
<!-- books-review:SF-2026-ARXIV-2603-00811:end -->

<!-- existing:SF-2026-ARXIV-2603-01209:start -->
author-side 已读 current owner `AGENT-PLATFORM` 的具体命题：/ Agent runtime / ready steps、tools、approvals、deadlines /
<!-- existing:SF-2026-ARXIV-2603-01209:end -->

<!-- delta:SF-2026-ARXIV-2603-01209:start -->
论文把 interpreter persistence 作为训练环境状态的一部分，使跨 turn 的变量、artifact 与副作用与部署执行合同一致。
<!-- delta:SF-2026-ARXIV-2603-01209:end -->

<!-- books-review:SF-2026-ARXIV-2603-01209:start -->
Decision=`No Change — Existing Coverage`；owner=`AGENT-PLATFORM`；target=`books/part-07-agent/84-agent-platform.md#Scheduling 不只是 GPU (line 471)`；adjacent=`books/part-07-agent/83-mcp.md#本章要回答的问题 (line 10)`。证据边界：只接受 arXiv:2603.01209v1 在 exact-v1 公开 workload 下的作者机制与实验主张；未披露的 model、hardware、precision、length、batch、concurrency、cost 与 production SLO 均为 Not Disclosed，不外推为通用结论。 该判断尚未由 fresh-context Books reviewer 接受；Integrate 项只进入日期 queue，不写共享 Books。
<!-- books-review:SF-2026-ARXIV-2603-01209:end -->

<!-- existing:SF-2026-ARXIV-2603-01630:start -->
author-side 已读 current owner `PLATFORM-EVALUATION-SYSTEM` 的具体命题：- `SF-2026-ARXIV-2606-21869` — primary `arXiv:2606.21869v1`；exact-v1 URL=`https://arxiv.org/html/2606.21869v1`；Method=`https://arxiv.org/html/2606.21869v1 — §3 Preliminaries — Energy Consumption and Measurement; Multilingual Dataset`；Evaluation=`https://arxiv.org/html/2606.21869v1 — §4 Results and Analysis — Common Setup; §4.1–§4.4; Appendix B Experimental Setups`；Non-proof=`https://arxiv.org/html/2606.21869v1 — §6 Conclusion; Environmental impact of this study; Translation quality and representation; Recommendatio
<!-- existing:SF-2026-ARXIV-2603-01630:end -->

<!-- delta:SF-2026-ARXIV-2603-01630:start -->
SEED-SET 将风险假设、场景生成、实验执行和失败归档组成可演进测试资产，令伦理声明绑定版本化 evidence。
<!-- delta:SF-2026-ARXIV-2603-01630:end -->

<!-- books-review:SF-2026-ARXIV-2603-01630:start -->
Decision=`No Change — Existing Coverage`；owner=`PLATFORM-EVALUATION-SYSTEM`；target=`books/part-06-ai-infrastructure/66-evaluation-system.md#从答案评分到可执行证据 (line 936)`；adjacent=`books/part-06-ai-infrastructure/65-kai-scheduler.md#本章要回答的问题 (line 10); books/part-06-ai-infrastructure/67-monitoring.md#本章要回答的问题 (line 10)`。证据边界：只接受 arXiv:2603.01630v1 在 exact-v1 公开 workload 下的作者机制与实验主张；未披露的 model、hardware、precision、length、batch、concurrency、cost 与 production SLO 均为 Not Disclosed，不外推为通用结论。 该判断尚未由 fresh-context Books reviewer 接受；Integrate 项只进入日期 queue，不写共享 Books。
<!-- books-review:SF-2026-ARXIV-2603-01630:end -->

<!-- existing:SF-2026-ARXIV-2603-02176:start -->
author-side 已读 current owner `AGENT-PLATFORM` 的具体命题：evaluation。NVIDIA verified skills 提供了这条发布链的官方实现案例，但不能证明被验证 Skill 在所有 Agent、
<!-- existing:SF-2026-ARXIV-2603-02176:end -->

<!-- delta:SF-2026-ARXIV-2603-02176:start -->
AgentSkillOS 先构建 capability tree 管理 Skill，再用 DAG 选择和编排多 Skill，把生态索引与任务执行分为两个状态阶段。
<!-- delta:SF-2026-ARXIV-2603-02176:end -->

<!-- books-review:SF-2026-ARXIV-2603-02176:start -->
Decision=`No Change — Existing Coverage`；owner=`AGENT-PLATFORM`；target=`books/part-07-agent/84-agent-platform.md#Agent Definition 与 Run Identity (line 192)`；adjacent=`books/part-07-agent/83-mcp.md#本章要回答的问题 (line 10)`。证据边界：只接受 arXiv:2603.02176v1 在 exact-v1 公开 workload 下的作者机制与实验主张；未披露的 model、hardware、precision、length、batch、concurrency、cost 与 production SLO 均为 Not Disclosed，不外推为通用结论。 该判断尚未由 fresh-context Books reviewer 接受；Integrate 项只进入日期 queue，不写共享 Books。
<!-- books-review:SF-2026-ARXIV-2603-02176:end -->

<!-- existing:SF-2026-ARXIV-2603-00349:start -->
author-side 已读 current owner `AGENT-MULTI-AGENT` 的具体命题：shared side effect 多或 coordinator headroom 不足时，single Agent + deterministic verifier 仍更小、更可靠。
<!-- existing:SF-2026-ARXIV-2603-00349:end -->

<!-- delta:SF-2026-ARXIV-2603-00349:start -->
COOP²/EmCoop 建立 cognitive-event 到 environment-step 的时间映射，并沿约束满足过程度量计划、通信和执行，使合作成为可观察 trace 而非结果标签。
<!-- delta:SF-2026-ARXIV-2603-00349:end -->

<!-- books-review:SF-2026-ARXIV-2603-00349:start -->
Decision=`No Change — Existing Coverage`；owner=`AGENT-MULTI-AGENT`；target=`books/part-07-agent/82-multi-agent.md#Message 不是 State (line 356)`；adjacent=`books/part-07-agent/81-workflow.md#本章要回答的问题 (line 10); books/part-07-agent/83-mcp.md#本章要回答的问题 (line 10)`。证据边界：只接受 arXiv:2603.00349v1 在 exact-v1 公开 workload 下的作者机制与实验主张；未披露的 model、hardware、precision、length、batch、concurrency、cost 与 production SLO 均为 Not Disclosed，不外推为通用结论。 该判断尚未由 fresh-context Books reviewer 接受；Integrate 项只进入日期 queue，不写共享 Books。
<!-- books-review:SF-2026-ARXIV-2603-00349:end -->

<!-- existing:SF-2026-ARXIV-2603-00381:start -->
author-side 已读 current owner `AGENT-MULTI-AGENT` 的具体命题：Multi-Agent 从广播全部对话演进到 typed role、message、shared state 与 topology。收益来自独立证据和真正的责任分解；当错误相关时，多数票可能放大失败，因此系统还要保存 minority evidence、校准 verifier/flip precision，并把 communication 和 verification delay纳入调度。
<!-- existing:SF-2026-ARXIV-2603-00381:end -->

<!-- delta:SF-2026-ARXIV-2603-00381:start -->
CLBC 将 generation 与 transcript admission 分离：消息只有携带绑定 policy、随机性、transcript chain 和字段约束的 proof envelope 并通过小 verifier 后才进入共享状态。
<!-- delta:SF-2026-ARXIV-2603-00381:end -->

<!-- books-review:SF-2026-ARXIV-2603-00381:start -->
Decision=`No Change — Existing Coverage`；owner=`AGENT-MULTI-AGENT`；target=`books/part-07-agent/82-multi-agent.md#从机制演进到系统设计 (line 639)`；adjacent=`books/part-07-agent/81-workflow.md#本章要回答的问题 (line 10); books/part-07-agent/83-mcp.md#本章要回答的问题 (line 10)`。证据边界：只接受 arXiv:2603.00381v1 在 exact-v1 公开 workload 下的作者机制与实验主张；未披露的 model、hardware、precision、length、batch、concurrency、cost 与 production SLO 均为 Not Disclosed，不外推为通用结论。 该判断尚未由 fresh-context Books reviewer 接受；Integrate 项只进入日期 queue，不写共享 Books。
<!-- books-review:SF-2026-ARXIV-2603-00381:end -->

<!-- existing:SF-2026-ARXIV-2603-00468:start -->
author-side 已读 current owner `PLATFORM-EVALUATION-SYSTEM` 的具体命题：EvalSpec 需要冻结 event/state schema、可控干预、matched interface、action scorer 与 tolerance，并保存每对干预样本的 trajectory。它能把相关性成功分解为更强的 behavioral evidence，却增加构造 matched interventions 的成本，也可能因遗漏真正 mediator 而误判。无法构造可信干预时，应把结论降级为 observational association，继续使用真实 outcome、人工 adjudication 与 production incident evidence。即使双臂通过，也只证明披露任务上的结构耦合，不证明模型具有内在 agency 或能迁移到开放环境。[受限证据：arXiv:2605.09692v1]
<!-- existing:SF-2026-ARXIV-2603-00468:end -->

<!-- delta:SF-2026-ARXIV-2603-00468:start -->
Cloud-OpsBench 冻结日志、指标、配置和瞬时 data-plane 状态为 State Snapshot，再通过标准诊断接口回放，解耦状态保存与工具交互。
<!-- delta:SF-2026-ARXIV-2603-00468:end -->

<!-- books-review:SF-2026-ARXIV-2603-00468:start -->
Decision=`No Change — Existing Coverage`；owner=`PLATFORM-EVALUATION-SYSTEM`；target=`books/part-06-ai-infrastructure/66-evaluation-system.md#Action Control 需要 Sensitivity 与 Invariance 双臂证据 (line 2452)`；adjacent=`books/part-06-ai-infrastructure/65-kai-scheduler.md#本章要回答的问题 (line 10); books/part-06-ai-infrastructure/67-monitoring.md#本章要回答的问题 (line 10)`。证据边界：只接受 arXiv:2603.00468v1 在 exact-v1 公开 workload 下的作者机制与实验主张；未披露的 model、hardware、precision、length、batch、concurrency、cost 与 production SLO 均为 Not Disclosed，不外推为通用结论。 该判断尚未由 fresh-context Books reviewer 接受；Integrate 项只进入日期 queue，不写共享 Books。
<!-- books-review:SF-2026-ARXIV-2603-00468:end -->

<!-- existing:SF-2026-ARXIV-2603-00623:start -->
author-side 已读 current owner `PLATFORM-TRACE` 的具体命题：本章的核心判断是：**Trace 通过传播 context，将一次分布式操作拆成有父子或 link 关系的 spans，从而重建 critical path；其价值取决于边界、语义和采样是否保留真正决策点。**
<!-- existing:SF-2026-ARXIV-2603-00623:end -->

<!-- delta:SF-2026-ARXIV-2603-00623:start -->
TraceSIR 先结构化 trace，再由分工 Agent 归因、交叉核对并生成报告，把诊断对象从自然语言总结改成 typed execution evidence。
<!-- delta:SF-2026-ARXIV-2603-00623:end -->

<!-- books-review:SF-2026-ARXIV-2603-00623:start -->
Decision=`No Change — Existing Coverage`；owner=`PLATFORM-TRACE`；target=`books/part-06-ai-infrastructure/69-trace.md#本章要回答的问题 (line 14)`；adjacent=`books/part-06-ai-infrastructure/68-logging.md#本章要回答的问题 (line 10); books/part-06-ai-infrastructure/70-cost.md#本章要回答的问题 (line 10)`。证据边界：只接受 arXiv:2603.00623v1 在 exact-v1 公开 workload 下的作者机制与实验主张；未披露的 model、hardware、precision、length、batch、concurrency、cost 与 production SLO 均为 Not Disclosed，不外推为通用结论。 该判断尚未由 fresh-context Books reviewer 接受；Integrate 项只进入日期 queue，不写共享 Books。
<!-- books-review:SF-2026-ARXIV-2603-00623:end -->

<!-- existing:SF-2026-ARXIV-2603-00680:start -->
author-side 已读 current owner `AGENT-MEMORY` 的具体命题：把 raw interaction history 放进 Context 或 external memory，是最容易审计和纠错的起点；当经验频繁变化、涉及隐私删除，或样本仍少时，这个旧方案依然合理。压力来自另一侧：长轨迹会在每次推理中反复占用 context 与 environment budget，成功行为也无法在移除历史后保留。此时可以增加一个有条件的 consolidation 分支：teacher 读取累计经验，student 只读取原始任务状态；从已有轨迹构造 one-step decision branches，把 teacher 的局部决策监督压回 student，而不再与环境交互，也不依赖 learned world model 展开长 rollout。
<!-- existing:SF-2026-ARXIV-2603-00680:end -->

<!-- delta:SF-2026-ARXIV-2603-00680:start -->
MemPO 将 memory operation 纳入 policy action 与训练信号，让模型主动管理有限信息状态。
<!-- delta:SF-2026-ARXIV-2603-00680:end -->

<!-- books-review:SF-2026-ARXIV-2603-00680:start -->
Decision=`No Change — Existing Coverage`；owner=`AGENT-MEMORY`；target=`books/part-07-agent/77-memory.md#从原始轨迹到派生策略：Memory 的演进不是无限追加 (line 498)`；adjacent=`books/part-07-agent/76-rag.md#本章要回答的问题 (line 10); books/part-07-agent/78-tool-calling.md#本章要回答的问题 (line 10)`。证据边界：只接受 arXiv:2603.00680v1 在 exact-v1 公开 workload 下的作者机制与实验主张；未披露的 model、hardware、precision、length、batch、concurrency、cost 与 production SLO 均为 Not Disclosed，不外推为通用结论。 该判断尚未由 fresh-context Books reviewer 接受；Integrate 项只进入日期 queue，不写共享 Books。
<!-- books-review:SF-2026-ARXIV-2603-00680:end -->

<!-- existing:SF-2026-ARXIV-2603-00825:start -->
author-side 已读 current owner `MULTIMODAL-WORLD-MODELS` 的具体命题：**Roadmap Intent:** 区分 video generation、predictive environment model 与 causal/controllable world model，解释 action-conditioned transition、latent dynamics、imagination 和 persistent state 的演进。
<!-- existing:SF-2026-ARXIV-2603-00825:end -->

<!-- delta:SF-2026-ARXIV-2603-00825:start -->
COMBAT 将 behavior/action condition 注入生成式 dynamics，使模拟状态转移能为 agent 产生可控训练轨迹。
<!-- delta:SF-2026-ARXIV-2603-00825:end -->

<!-- books-review:SF-2026-ARXIV-2603-00825:start -->
Decision=`No Change — Existing Coverage`；owner=`MULTIMODAL-WORLD-MODELS`；target=`books/part-03-multimodal-world-models/25-multimodal-world-models.md#本章要回答的问题 (line 8)`；adjacent=`books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md#本章要回答的问题 (line 10); books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#本章要回答的问题 (line 10)`。证据边界：只接受 arXiv:2603.00825v1 在 exact-v1 公开 workload 下的作者机制与实验主张；未披露的 model、hardware、precision、length、batch、concurrency、cost 与 production SLO 均为 Not Disclosed，不外推为通用结论。 该判断尚未由 fresh-context Books reviewer 接受；Integrate 项只进入日期 queue，不写共享 Books。
<!-- books-review:SF-2026-ARXIV-2603-00825:end -->

<!-- existing:SF-2026-ARXIV-2603-01058:start -->
author-side 已读 current owner `INFER-GPU-MEMORY` 的具体命题：cache owner 仍决定最终可见状态。收益取决于 CPU 核数、host memory bandwidth、PCIe 和 layer compute 是否足以
<!-- existing:SF-2026-ARXIV-2603-01058:end -->

<!-- delta:SF-2026-ARXIV-2603-01058:start -->
TriMoE 将活跃专家在 GPU、AMX CPU 与 DIMM-NDP 间分层放置并协调数据流，利用异构算力而非把 CPU 仅作存储。
<!-- delta:SF-2026-ARXIV-2603-01058:end -->

<!-- books-review:SF-2026-ARXIV-2603-01058:start -->
Decision=`No Change — Existing Coverage`；owner=`INFER-GPU-MEMORY`；target=`books/part-05-inference-system/54-gpu-memory.md#三类缓解路径 (line 230)`；adjacent=`books/part-05-inference-system/53-kserve-llm.md#本章要回答的问题 (line 10); books/part-05-inference-system/55-pd-disaggregation.md#本章要回答的问题 (line 10)`。证据边界：只接受 arXiv:2603.01058v1 在 exact-v1 公开 workload 下的作者机制与实验主张；未披露的 model、hardware、precision、length、batch、concurrency、cost 与 production SLO 均为 Not Disclosed，不外推为通用结论。 该判断尚未由 fresh-context Books reviewer 接受；Integrate 项只进入日期 queue，不写共享 Books。
<!-- books-review:SF-2026-ARXIV-2603-01058:end -->

<!-- existing:SF-2026-ARXIV-2603-01162:start -->
author-side 已读 current owner `TRAIN-GRPO` 的具体命题：本章以 DeepSeekMath 提出的 Group Relative Policy Optimization 为基线。后续系统可能修改 token weighting、KL estimator、normalization 或 clipping；同名 GRPO 实现必须逐项核验，不能仅凭算法名称推断完全相同 objective。
<!-- existing:SF-2026-ARXIV-2603-01162:end -->

<!-- delta:SF-2026-ARXIV-2603-01162:start -->
论文把 GRPO policy gradient 形式化为 U-statistic，显式描述组采样、相对比较与梯度估计之间的依赖。
<!-- delta:SF-2026-ARXIV-2603-01162:end -->

<!-- books-review:SF-2026-ARXIV-2603-01162:start -->
Decision=`Integrate`；owner=`TRAIN-GRPO`；target=`books/part-04-training-system/33-grpo.md#Group-relative Gradient 不是独立样本均值 (line 219)`；adjacent=`books/part-04-training-system/32-ppo.md#本章要回答的问题 (line 10); books/part-04-training-system/34-dpo.md#本章要回答的问题 (line 10)`。证据边界：只接受 arXiv:2603.01162v1 在 exact-v1 公开 workload 下的作者机制与实验主张；未披露的 model、hardware、precision、length、batch、concurrency、cost 与 production SLO 均为 Not Disclosed，不外推为通用结论。已写入共享 Books，marker=`source-family:SF-2026-ARXIV-2603-01162`；仍待非作者 post-write semantic audit，因此 Books Gate 保持 Open。
<!-- books-review:SF-2026-ARXIV-2603-01162:end -->

<!-- existing:SF-2026-ARXIV-2603-01399:start -->
author-side 已读 current owner `INFER-SPECULATIVE-DECODING` 的具体命题：本章的核心判断是：**Speculative Decoding 用额外且便宜的 proposal work，换取一次 target-model verification 推进多个 output tokens；经典算法通过 acceptance 与 residual sampling 保持 target distribution，而不是用 draft model 改写模型行为。**
<!-- existing:SF-2026-ARXIV-2603-01399:end -->

<!-- delta:SF-2026-ARXIV-2603-01399:start -->
Quasar 对 draft/self-draft 状态做量化并设计内存受限 verification，联合优化草稿成本与接受路径。
<!-- delta:SF-2026-ARXIV-2603-01399:end -->

<!-- books-review:SF-2026-ARXIV-2603-01399:start -->
Decision=`No Change — Existing Coverage`；owner=`INFER-SPECULATIVE-DECODING`；target=`books/part-05-inference-system/48-speculative-decoding.md#本章要回答的问题 (line 16)`；adjacent=`books/part-05-inference-system/47-pagedattention.md#本章要回答的问题 (line 10); books/part-05-inference-system/49-tensorrt-llm.md#本章要回答的问题 (line 10)`。证据边界：只接受 arXiv:2603.01399v1 在 exact-v1 公开 workload 下的作者机制与实验主张；未披露的 model、hardware、precision、length、batch、concurrency、cost 与 production SLO 均为 Not Disclosed，不外推为通用结论。 该判断尚未由 fresh-context Books reviewer 接受；Integrate 项只进入日期 queue，不写共享 Books。
<!-- books-review:SF-2026-ARXIV-2603-01399:end -->

<!-- existing:SF-2026-ARXIV-2603-01499:start -->
author-side 已读 current owner `PLATFORM-SECURITY` 的具体命题：- `SF-2026-ARXIV-2606-22019` — primary `arXiv:2606.22019v1`；exact-v1 URL=`https://arxiv.org/html/2606.22019v1`；Method=`https://arxiv.org/html/2606.22019v1 — §2 Audit model: carriers, screens, and ablations; §6 The audit lifecycle: which handle is sound in which channel?`；Evaluation=`https://arxiv.org/html/2606.22019v1 — §3 A controlled body channel is screenable: coverage predicts transfer; §4 Vocabulary-carried token traits evade initialization-alignment screens; §5 The carrier is signal-dependent, and moving it m
<!-- existing:SF-2026-ARXIV-2603-01499:end -->

<!-- delta:SF-2026-ARXIV-2603-01499:start -->
covariant obfuscation 通过保持所需变换关系的输入/权重表示来隐藏原值，使服务端在混淆域执行。
<!-- delta:SF-2026-ARXIV-2603-01499:end -->

<!-- books-review:SF-2026-ARXIV-2603-01499:start -->
Decision=`No Change — Existing Coverage`；owner=`PLATFORM-SECURITY`；target=`books/part-06-ai-infrastructure/72-security.md#风险管理而不是一次性认证 (line 1091)`；adjacent=`books/part-06-ai-infrastructure/71-multi-tenant.md#本章要回答的问题 (line 10); books/part-06-ai-infrastructure/73-production-best-practice.md#本章要回答的问题 (line 10)`。证据边界：只接受 arXiv:2603.01499v1 在 exact-v1 公开 workload 下的作者机制与实验主张；未披露的 model、hardware、precision、length、batch、concurrency、cost 与 production SLO 均为 Not Disclosed，不外推为通用结论。 该判断尚未由 fresh-context Books reviewer 接受；Integrate 项只进入日期 queue，不写共享 Books。
<!-- books-review:SF-2026-ARXIV-2603-01499:end -->

<!-- existing:SF-2026-ARXIV-2603-01960:start -->
author-side 已读 current owner `INFER-TENSORRT-LLM` 的具体命题：为每个 fused operator 手写 kernel，在 shape 稳定、目标硬件单一时可获得最直接的控制；attention、state-space、quantized block 或自定义 reduction 增多后，kernel surface 会随组合爆炸。一个中间抽象是把可表达部分归一为 `GEMM + versioned epilogue`：compiler 拥有 tile、layout 与 epilogue lowering，runtime 只提交已验证的 shape/precision instance，custom kernel 保留给无法合法表达的 control flow。
<!-- existing:SF-2026-ARXIV-2603-01960:end -->

<!-- delta:SF-2026-ARXIV-2603-01960:start -->
TiledAttention 将 attention 分解为显式 CUDA tiles 并控制加载、累加与边界处理，令执行计划而非框架默认 kernel 拥有数据移动。
<!-- delta:SF-2026-ARXIV-2603-01960:end -->

<!-- books-review:SF-2026-ARXIV-2603-01960:start -->
Decision=`No Change — Existing Coverage`；owner=`INFER-TENSORRT-LLM`；target=`books/part-05-inference-system/49-tensorrt-llm.md#从 Linear 语义到 GEMM 执行 (line 267)`；adjacent=`books/part-05-inference-system/48-speculative-decoding.md#本章要回答的问题 (line 10); books/part-05-inference-system/50-vllm.md#本章要回答的问题 (line 10)`。证据边界：只接受 arXiv:2603.01960v1 在 exact-v1 公开 workload 下的作者机制与实验主张；未披露的 model、hardware、precision、length、batch、concurrency、cost 与 production SLO 均为 Not Disclosed，不外推为通用结论。 该判断尚未由 fresh-context Books reviewer 接受；Integrate 项只进入日期 queue，不写共享 Books。
<!-- books-review:SF-2026-ARXIV-2603-01960:end -->

<!-- existing:SF-2026-ARXIV-2603-02075:start -->
author-side 已读 current owner `TRAIN-DATA` 的具体命题：这里 data operator 只提出训练分布，training controller 拥有 active set、采样权重、cache 与更新时机，
<!-- existing:SF-2026-ARXIV-2603-02075:end -->

<!-- delta:SF-2026-ARXIV-2603-02075:start -->
Trident 依据样本/模态 cost 动态调度数据处理阶段，在异构 worker 间平衡生产速度与 trainer 消费。
<!-- delta:SF-2026-ARXIV-2603-02075:end -->

<!-- books-review:SF-2026-ARXIV-2603-02075:start -->
Decision=`No Change — Existing Coverage`；owner=`TRAIN-DATA`；target=`books/part-04-training-system/27-data.md#数据分布就是优化权重 (line 152)`；adjacent=`books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#本章要回答的问题 (line 10); books/part-04-training-system/28-pretraining.md#本章要回答的问题 (line 10)`。证据边界：只接受 arXiv:2603.02075v1 在 exact-v1 公开 workload 下的作者机制与实验主张；未披露的 model、hardware、precision、length、batch、concurrency、cost 与 production SLO 均为 Not Disclosed，不外推为通用结论。 该判断尚未由 fresh-context Books reviewer 接受；Integrate 项只进入日期 queue，不写共享 Books。
<!-- books-review:SF-2026-ARXIV-2603-02075:end -->

<!-- existing:SF-2026-ARXIV-2603-02146:start -->
author-side 已读 current owner `TRAIN-GRPO` 的具体命题：可执行结果仍会受 environment、measurement noise 与 reward mapping 影响；训练 specification 必须绑定测量环境、重复性与 reward transformation，hard correctness gate 不能被连续 proxy 取代。
<!-- existing:SF-2026-ARXIV-2603-02146:end -->

<!-- delta:SF-2026-ARXIV-2603-02146:start -->
LongRLVR 把可验证 context-use 条件纳入 reward，使长文证据选择与最终答案共同决定更新。
<!-- delta:SF-2026-ARXIV-2603-02146:end -->

<!-- books-review:SF-2026-ARXIV-2603-02146:start -->
Decision=`Integrate`；owner=`TRAIN-GRPO`；target=`books/part-04-training-system/33-grpo.md#长上下文 RL 还要验证 Context 是否真正被使用 (line 451)`；adjacent=`books/part-04-training-system/32-ppo.md#本章要回答的问题 (line 10); books/part-04-training-system/34-dpo.md#本章要回答的问题 (line 10)`。证据边界：只接受 arXiv:2603.02146v1 在 exact-v1 公开 workload 下的作者机制与实验主张；未披露的 model、hardware、precision、length、batch、concurrency、cost 与 production SLO 均为 Not Disclosed，不外推为通用结论。已写入共享 Books，marker=`source-family:SF-2026-ARXIV-2603-02146`；仍待非作者 post-write semantic audit，因此 Books Gate 保持 Open。
<!-- books-review:SF-2026-ARXIV-2603-02146:end -->

<!-- existing:SF-2026-ARXIV-2603-02188:start -->
author-side 已读 current owner `MODEL-MULTI-HEAD-ATTENTION` 的具体命题：第14章的单个 Attention head 已能让 token 按内容读取上下文，为什么还需要多个 head？Multi-Head Attention 如何在多个投影子空间并行建立关系，又为什么会演化出 MQA 和 GQA？
<!-- existing:SF-2026-ARXIV-2603-02188:end -->

<!-- delta:SF-2026-ARXIV-2603-02188:start -->
Multi-Head Low-Rank Attention 在 head 结构内引入低秩参数化，重分配共享与每头特有表示。
<!-- delta:SF-2026-ARXIV-2603-02188:end -->

<!-- books-review:SF-2026-ARXIV-2603-02188:start -->
Decision=`No Change — Existing Coverage`；owner=`MODEL-MULTI-HEAD-ATTENTION`；target=`books/part-02-model/15-multi-head-attention.md#本章要回答的问题 (line 12)`；adjacent=`books/part-02-model/14-self-attention.md#本章要回答的问题 (line 10); books/part-02-model/16-feed-forward-mlp.md#本章要回答的问题 (line 10)`。证据边界：只接受 arXiv:2603.02188v1 在 exact-v1 公开 workload 下的作者机制与实验主张；未披露的 model、hardware、precision、length、batch、concurrency、cost 与 production SLO 均为 Not Disclosed，不外推为通用结论。 该判断尚未由 fresh-context Books reviewer 接受；Integrate 项只进入日期 queue，不写共享 Books。
<!-- books-review:SF-2026-ARXIV-2603-02188:end -->

<!-- existing:SF-2026-ARXIV-2603-00188:start -->
author-side 已读 current owner `INFER-KV-CACHE` 的具体命题：一个 training-free 分支先离线建立 model-side PCA basis，再在每个 request prefill 中估计各层 reconstruction curve，用 water-filling 在总 KV budget 下分配 variable rank。它不删除 token，而是改变每个 region 保留的 feature subspace；basis revision、request statistic、rank map、packed offsets、codec precision 与 reuse scope 都必须进入 cache identity。Prefix reuse 只有在 basis、model、RoPE 与 rank policy 兼容时才能共享，Decode kernel 若不能直接消费 variable layout，projection/gather 成本会返还 memory 节省。
<!-- existing:SF-2026-ARXIV-2603-00188:end -->

<!-- delta:SF-2026-ARXIV-2603-00188:start -->
ST-Lite 把视觉 token 的空间位置和交互轨迹共同用于训练外压缩，令保留决策拥有 GUI 轨迹语义，而不是只由通用 KV eviction 规则决定。
<!-- delta:SF-2026-ARXIV-2603-00188:end -->

<!-- books-review:SF-2026-ARXIV-2603-00188:start -->
Decision=`No Change — Existing Coverage`；owner=`INFER-KV-CACHE`；target=`books/part-05-inference-system/45-why-kv-cache-speeds-up.md#KV Cache 的生命周期 (line 517)`；adjacent=`books/part-05-inference-system/44-decode.md#本章要回答的问题 (line 10); books/part-05-inference-system/46-continuous-batching.md#本章要回答的问题 (line 10)`。证据边界：只接受 arXiv:2603.00188v1 在 exact-v1 公开 workload 下的作者机制与实验主张；未披露的 model、hardware、precision、length、batch、concurrency、cost 与 production SLO 均为 Not Disclosed，不外推为通用结论。 该判断尚未由 fresh-context Books reviewer 接受；Integrate 项只进入日期 queue，不写共享 Books。
<!-- books-review:SF-2026-ARXIV-2603-00188:end -->

<!-- existing:SF-2026-ARXIV-2603-01045:start -->
author-side 已读 current owner `PLATFORM-EVALUATION-SYSTEM` 的具体命题：Research Agent 还需要把 final artifact、research progress 与 environment integrity 分开：没有产出最终解，不等于过程中没有形成可复用证据；反过来，拿到高分也可能来自损坏的依赖、污染的 workspace 或 verifier 漏洞。风险评估同样应按 risk family 保存不同 EvalSpec，并进一步区分：
<!-- existing:SF-2026-ARXIV-2603-01045:end -->

<!-- delta:SF-2026-ARXIV-2603-01045:start -->
Silo-Bench 提供隔离但可交互的环境与可扩展任务，把 coordination protocol、资源和结果作为同一 evaluation contract。
<!-- delta:SF-2026-ARXIV-2603-01045:end -->

<!-- books-review:SF-2026-ARXIV-2603-01045:start -->
Decision=`No Change — Existing Coverage`；owner=`PLATFORM-EVALUATION-SYSTEM`；target=`books/part-06-ai-infrastructure/66-evaluation-system.md#评估对象有四个层次 (line 417)`；adjacent=`books/part-06-ai-infrastructure/65-kai-scheduler.md#本章要回答的问题 (line 10); books/part-06-ai-infrastructure/67-monitoring.md#本章要回答的问题 (line 10)`。证据边界：只接受 arXiv:2603.01045v1 在 exact-v1 公开 workload 下的作者机制与实验主张；未披露的 model、hardware、precision、length、batch、concurrency、cost 与 production SLO 均为 Not Disclosed，不外推为通用结论。 该判断尚未由 fresh-context Books reviewer 接受；Integrate 项只进入日期 queue，不写共享 Books。
<!-- books-review:SF-2026-ARXIV-2603-01045:end -->

<!-- existing:SF-2026-ARXIV-2603-01548:start -->
author-side 已读 current owner `AGENT-TOOL-CALLING` 的具体命题：复杂多轮 tool path 若等完整 reasoning 后才开始交互，用户看到的 latency 由最长链决定。Agent 可在低风险、可取消的边界并行准备候选 tool call 或 UI response，但只能把它们作为 proposal；authorizer 和 side-effect identity 在真实执行前统一 commit，错误分支必须可撤销。收益是隐藏思考延迟，代价是浪费、重复调用和 stale observation；不可逆工具、权限不明或 cancellation 不可靠时回退串行。
<!-- existing:SF-2026-ARXIV-2603-01548:end -->

<!-- delta:SF-2026-ARXIV-2603-01548:start -->
论文将工具、能力和失败关系建图，并根据执行反馈修复路由边，使错误成为 routing-state 更新信号。
<!-- delta:SF-2026-ARXIV-2603-01548:end -->

<!-- books-review:SF-2026-ARXIV-2603-01548:start -->
Decision=`No Change — Existing Coverage`；owner=`AGENT-TOOL-CALLING`；target=`books/part-07-agent/78-tool-calling.md#Evaluation 与 Observability (line 365)`；adjacent=`books/part-07-agent/77-memory.md#本章要回答的问题 (line 10); books/part-07-agent/79-planning.md#本章要回答的问题 (line 10)`。证据边界：只接受 arXiv:2603.01548v1 在 exact-v1 公开 workload 下的作者机制与实验主张；未披露的 model、hardware、precision、length、batch、concurrency、cost 与 production SLO 均为 Not Disclosed，不外推为通用结论。 该判断尚未由 fresh-context Books reviewer 接受；Integrate 项只进入日期 queue，不写共享 Books。
<!-- books-review:SF-2026-ARXIV-2603-01548:end -->

<!-- existing:SF-2026-ARXIV-2603-01581:start -->
author-side 已读 current owner `INFER-SPECULATIVE-DECODING` 的具体命题：自回归 Decode 每次只能生成一个 token，这是 LLM 推理延迟的根本瓶颈之一。Speculative Decoding 为什么能让大模型“看起来一次生成多个 token”？它为什么不是简单地用小模型替代大模型？它在什么条件下才真正有效？
<!-- existing:SF-2026-ARXIV-2603-01581:end -->

<!-- delta:SF-2026-ARXIV-2603-01581:start -->
KERV 用运动学误差校正/接受 VLA 草稿，把 verification 从离散 token 一致扩展到受动作动力学约束的近似路径。
<!-- delta:SF-2026-ARXIV-2603-01581:end -->

<!-- books-review:SF-2026-ARXIV-2603-01581:start -->
Decision=`No Change — Existing Coverage`；owner=`INFER-SPECULATIVE-DECODING`；target=`books/part-05-inference-system/48-speculative-decoding.md#本章要回答的问题 (line 12)`；adjacent=`books/part-05-inference-system/47-pagedattention.md#本章要回答的问题 (line 10); books/part-05-inference-system/49-tensorrt-llm.md#本章要回答的问题 (line 10)`。证据边界：只接受 arXiv:2603.01581v1 在 exact-v1 公开 workload 下的作者机制与实验主张；未披露的 model、hardware、precision、length、batch、concurrency、cost 与 production SLO 均为 Not Disclosed，不外推为通用结论。 该判断尚未由 fresh-context Books reviewer 接受；Integrate 项只进入日期 queue，不写共享 Books。
<!-- books-review:SF-2026-ARXIV-2603-01581:end -->

<!-- existing:SF-2026-ARXIV-2603-01639:start -->
author-side 已读 current owner `INFER-SPECULATIVE-DECODING` 的具体命题：本章的核心判断是：**Speculative Decoding 用额外且便宜的 proposal work，换取一次 target-model verification 推进多个 output tokens；经典算法通过 acceptance 与 residual sampling 保持 target distribution，而不是用 draft model 改写模型行为。**
<!-- existing:SF-2026-ARXIV-2603-01639:end -->

<!-- delta:SF-2026-ARXIV-2603-01639:start -->
Learning to Draft 用 RL 把 target verification feedback 与系统收益送回 draft policy，使 proposal 分布随目标和成本约束调整。
<!-- delta:SF-2026-ARXIV-2603-01639:end -->

<!-- books-review:SF-2026-ARXIV-2603-01639:start -->
Decision=`No Change — Existing Coverage`；owner=`INFER-SPECULATIVE-DECODING`；target=`books/part-05-inference-system/48-speculative-decoding.md#本章要回答的问题 (line 16)`；adjacent=`books/part-05-inference-system/47-pagedattention.md#本章要回答的问题 (line 10); books/part-05-inference-system/49-tensorrt-llm.md#本章要回答的问题 (line 10)`。证据边界：只接受 arXiv:2603.01639v1 在 exact-v1 公开 workload 下的作者机制与实验主张；未披露的 model、hardware、precision、length、batch、concurrency、cost 与 production SLO 均为 Not Disclosed，不外推为通用结论。 该判断尚未由 fresh-context Books reviewer 接受；Integrate 项只进入日期 queue，不写共享 Books。
<!-- books-review:SF-2026-ARXIV-2603-01639:end -->

<!-- existing:SF-2026-ARXIV-2603-01661:start -->
author-side 已读 current owner `INFER-SCHEDULING` 的具体命题：把 online LLM scheduling 建模为带几何长度/剩余工作量的 admission 与排队问题；scheduler 以 workload shape 和 SLO slack 决定队列而非只按到达顺序。 这项变化只在 exact-v1 披露的 workload、状态身份和评估合同内成立；作者 workload、FP16/BF16、QPS 2–128 与队列模型不能外推到其他 engine、KV tier 或多租户优先级；估计失准需要保守 admission fallback。 因此旧路径在这些新增约束不存在、证据条件不足或失败回退被触发时仍然成立，不能被新的局部结果静默覆盖。
<!-- existing:SF-2026-ARXIV-2603-01661:end -->

<!-- delta:SF-2026-ARXIV-2603-01661:start -->
HeRo 根据阶段、热状态和设备能力动态编排检索、rerank 与生成，把异构 SoC 资源作为在线调度对象。
<!-- delta:SF-2026-ARXIV-2603-01661:end -->

<!-- books-review:SF-2026-ARXIV-2603-01661:start -->
Decision=`No Change — Existing Coverage`；owner=`INFER-SCHEDULING`；target=`books/part-05-inference-system/56-inference-scheduling.md#本章在知识树中的位置 (line 853)`；adjacent=`books/part-05-inference-system/55-pd-disaggregation.md#本章要回答的问题 (line 10); books/part-06-ai-infrastructure/57-what-is-ai-platform.md#本章要回答的问题 (line 10)`。证据边界：只接受 arXiv:2603.01661v1 在 exact-v1 公开 workload 下的作者机制与实验主张；未披露的 model、hardware、precision、length、batch、concurrency、cost 与 production SLO 均为 Not Disclosed，不外推为通用结论。 该判断尚未由 fresh-context Books reviewer 接受；Integrate 项只进入日期 queue，不写共享 Books。
<!-- books-review:SF-2026-ARXIV-2603-01661:end -->

<!-- existing:SF-2026-ARXIV-2603-01683:start -->
author-side 已读 current owner `TRAIN-RLHF` 的具体命题：动态 rubric、spec learning 或 on-policy distillation可以提高适应性，却会放大 reward hacking、judge correlation、density mismatch 与评价成本。它们必须通过 frozen holdout、独立 outcome evidence 和 rollback gate；反馈不足或评估失去区分力时，回退静态 rubric、SFT 或人工 adjudication。几何差异只有在 data、step 和 learning rate 匹配时才可归因于 objective。
<!-- existing:SF-2026-ARXIV-2603-01683:end -->

<!-- delta:SF-2026-ARXIV-2603-01683:start -->
Surgical Post-Training 使用受限的 on-policy distillation，把新轨迹信号与保留约束绑定到同一 update。
<!-- delta:SF-2026-ARXIV-2603-01683:end -->

<!-- books-review:SF-2026-ARXIV-2603-01683:start -->
Decision=`No Change — Existing Coverage`；owner=`TRAIN-RLHF`；target=`books/part-04-training-system/31-rlhf.md#从机制演进到系统设计 (line 599)`；adjacent=`books/part-04-training-system/30-lora.md#本章要回答的问题 (line 10); books/part-04-training-system/32-ppo.md#本章要回答的问题 (line 10)`。证据边界：只接受 arXiv:2603.01683v1 在 exact-v1 公开 workload 下的作者机制与实验主张；未披露的 model、hardware、precision、length、batch、concurrency、cost 与 production SLO 均为 Not Disclosed，不外推为通用结论。 该判断尚未由 fresh-context Books reviewer 接受；Integrate 项只进入日期 queue，不写共享 Books。
<!-- books-review:SF-2026-ARXIV-2603-01683:end -->

<!-- existing:SF-2026-ARXIV-2603-01966:start -->
author-side 已读 current owner `PLATFORM-EVALUATION-SYSTEM` 的具体命题：Final anchored verifier 可以提供可扩展 outcome evidence，却不能证明每个中间 transition 正确。真实用户风格、多意图同轮和含糊修订还需要额外切片；Agent 的 Context、Memory 与 Workflow 可以消费这些状态边界，但 evaluation owner 仍负责定义 transition identity、control arm 与最终可比较性。
<!-- existing:SF-2026-ARXIV-2603-01966:end -->

<!-- delta:SF-2026-ARXIV-2603-01966:start -->
AMemGym 通过交互式长时程环境分别触发记忆生命周期操作，使 memory policy 在动态对话中被观察。
<!-- delta:SF-2026-ARXIV-2603-01966:end -->

<!-- books-review:SF-2026-ARXIV-2603-01966:start -->
Decision=`No Change — Existing Coverage`；owner=`PLATFORM-EVALUATION-SYSTEM`；target=`books/part-06-ai-infrastructure/66-evaluation-system.md#从答案评分到可执行证据 (line 1463)`；adjacent=`books/part-06-ai-infrastructure/65-kai-scheduler.md#本章要回答的问题 (line 10); books/part-06-ai-infrastructure/67-monitoring.md#本章要回答的问题 (line 10)`。证据边界：只接受 arXiv:2603.01966v1 在 exact-v1 公开 workload 下的作者机制与实验主张；未披露的 model、hardware、precision、length、batch、concurrency、cost 与 production SLO 均为 Not Disclosed，不外推为通用结论。 该判断尚未由 fresh-context Books reviewer 接受；Integrate 项只进入日期 queue，不写共享 Books。
<!-- books-review:SF-2026-ARXIV-2603-01966:end -->

## 7. Semantic Audit

<!-- validator:semantic-audit-v1 -->
| Audit ID | Auditor | Scope | Reviewed Refs | Findings | Resolution | Status |
| --- | --- | --- | --- | --- | --- | --- |
| SA-20260304-COVERAGE | fresh-context:march-lane-b-reviewer | coverage | coverage:SRC-ARXIV:20260304 | MAR26-FC-001/MAR26-FC-002/MAR26-FC-003 | pending: full-row fresh-context false-positive/false-negative replay; see papers/2026/03/_sources/latest-contract-semantic-reopen-20260903.json | open |
| SA-20260304-EVIDENCE | fresh-context:march-lane-b-reviewer | evidence | validator:review-completion-v1 | — | accepted: retained family 均完成 exact-v1 review，blocked/unverified/disputed=0 | passed |
| SA-20260304-SELECTION | fresh-context:march-lane-b-reviewer | deep_analysis_selection | validator:deep-analysis-selection-v1 | MAR26-FC-004 | pending: recompute after denominator refreeze; see papers/2026/03/_sources/latest-contract-semantic-reopen-20260903.json | open |
| SA-20260304-BOOKS | fresh-context:march-lane-b-reviewer | books | validator:books-comparison-v1 | MAR26-FC-004 | pending: recheck disposition after denominator refreeze; see papers/2026/03/_sources/latest-contract-semantic-reopen-20260903.json | open |

## 8. Ignored Noise

1237 个 pre-denominator closure 保存在 `papers/2026/03/_sources/daily-20260304/screening-ledger-final.json`；每个 family 保存 identity、title、abstract 与具体排除理由。withdrawn=0。

## 9. Recommended Action

本日 3 项长期机制已完成 exact-v1 证据审阅、canonical owner 写回与非写作者 post-write Semantic Audit；后续仅在 primary revision 或新反证出现时重开。

## 10. Repository Changes

- 新增或幂等更新本日 Daily 与可复算 source packet。
- 完成 3 项 Books Integration：
- 更新并复核 `books/part-04-training-system/33-grpo.md`。
- 更新并复核 `books/part-05-inference-system/56-inference-scheduling.md`。
- 未修改 Weekly；未 stage、commit 或 push。

## 11. Open Questions

- 未解决语义 finding=4（`MAR26-FC-001 / MAR26-FC-002 / MAR26-FC-003 / MAR26-FC-004`）；blocked / unverified / disputed 仍为 0。
- 论文自身未证明边界保留在各 Source Review 的 Claim Boundary 中；它们不是本次流程 pending。

## 12. Sources

- [arXiv:2603.00063v1](https://arxiv.org/abs/2603.00063v1) — official announcement instant `2026-03-03T09:00:00+08:00`；按半开窗口 owner report=`2026-03-04`；访问日期 2026-09-02。
- [arXiv:2603.00195v1](https://arxiv.org/abs/2603.00195v1) — official announcement instant `2026-03-03T09:00:00+08:00`；按半开窗口 owner report=`2026-03-04`；访问日期 2026-09-02。
- [arXiv:2603.00196v1](https://arxiv.org/abs/2603.00196v1) — official announcement instant `2026-03-03T09:00:00+08:00`；按半开窗口 owner report=`2026-03-04`；访问日期 2026-09-02。
- [arXiv:2603.00356v1](https://arxiv.org/abs/2603.00356v1) — official announcement instant `2026-03-03T09:00:00+08:00`；按半开窗口 owner report=`2026-03-04`；访问日期 2026-09-02。
- [arXiv:2603.00357v1](https://arxiv.org/abs/2603.00357v1) — official announcement instant `2026-03-03T09:00:00+08:00`；按半开窗口 owner report=`2026-03-04`；访问日期 2026-09-02。
- [arXiv:2603.00495v1](https://arxiv.org/abs/2603.00495v1) — official announcement instant `2026-03-03T09:00:00+08:00`；按半开窗口 owner report=`2026-03-04`；访问日期 2026-09-02。
- [arXiv:2603.00575v1](https://arxiv.org/abs/2603.00575v1) — official announcement instant `2026-03-03T09:00:00+08:00`；按半开窗口 owner report=`2026-03-04`；访问日期 2026-09-02。
- [arXiv:2603.00811v1](https://arxiv.org/abs/2603.00811v1) — official announcement instant `2026-03-03T09:00:00+08:00`；按半开窗口 owner report=`2026-03-04`；访问日期 2026-09-02。
- [arXiv:2603.01209v1](https://arxiv.org/abs/2603.01209v1) — official announcement instant `2026-03-03T09:00:00+08:00`；按半开窗口 owner report=`2026-03-04`；访问日期 2026-09-02。
- [arXiv:2603.01630v1](https://arxiv.org/abs/2603.01630v1) — official announcement instant `2026-03-03T09:00:00+08:00`；按半开窗口 owner report=`2026-03-04`；访问日期 2026-09-02。
- [arXiv:2603.02176v1](https://arxiv.org/abs/2603.02176v1) — official announcement instant `2026-03-03T09:00:00+08:00`；按半开窗口 owner report=`2026-03-04`；访问日期 2026-09-02。
- [arXiv:2603.00349v1](https://arxiv.org/abs/2603.00349v1) — official announcement instant `2026-03-03T09:00:00+08:00`；按半开窗口 owner report=`2026-03-04`；访问日期 2026-09-02。
- [arXiv:2603.00381v1](https://arxiv.org/abs/2603.00381v1) — official announcement instant `2026-03-03T09:00:00+08:00`；按半开窗口 owner report=`2026-03-04`；访问日期 2026-09-02。
- [arXiv:2603.00468v1](https://arxiv.org/abs/2603.00468v1) — official announcement instant `2026-03-03T09:00:00+08:00`；按半开窗口 owner report=`2026-03-04`；访问日期 2026-09-02。
- [arXiv:2603.00623v1](https://arxiv.org/abs/2603.00623v1) — official announcement instant `2026-03-03T09:00:00+08:00`；按半开窗口 owner report=`2026-03-04`；访问日期 2026-09-02。
- [arXiv:2603.00680v1](https://arxiv.org/abs/2603.00680v1) — official announcement instant `2026-03-03T09:00:00+08:00`；按半开窗口 owner report=`2026-03-04`；访问日期 2026-09-02。
- [arXiv:2603.00825v1](https://arxiv.org/abs/2603.00825v1) — official announcement instant `2026-03-03T09:00:00+08:00`；按半开窗口 owner report=`2026-03-04`；访问日期 2026-09-02。
- [arXiv:2603.01058v1](https://arxiv.org/abs/2603.01058v1) — official announcement instant `2026-03-03T09:00:00+08:00`；按半开窗口 owner report=`2026-03-04`；访问日期 2026-09-02。
- [arXiv:2603.01162v1](https://arxiv.org/abs/2603.01162v1) — official announcement instant `2026-03-03T09:00:00+08:00`；按半开窗口 owner report=`2026-03-04`；访问日期 2026-09-02。
- [arXiv:2603.01399v1](https://arxiv.org/abs/2603.01399v1) — official announcement instant `2026-03-03T09:00:00+08:00`；按半开窗口 owner report=`2026-03-04`；访问日期 2026-09-02。
- [arXiv:2603.01499v1](https://arxiv.org/abs/2603.01499v1) — official announcement instant `2026-03-03T09:00:00+08:00`；按半开窗口 owner report=`2026-03-04`；访问日期 2026-09-02。
- [arXiv:2603.01960v1](https://arxiv.org/abs/2603.01960v1) — official announcement instant `2026-03-03T09:00:00+08:00`；按半开窗口 owner report=`2026-03-04`；访问日期 2026-09-02。
- [arXiv:2603.02075v1](https://arxiv.org/abs/2603.02075v1) — official announcement instant `2026-03-03T09:00:00+08:00`；按半开窗口 owner report=`2026-03-04`；访问日期 2026-09-02。
- [arXiv:2603.02146v1](https://arxiv.org/abs/2603.02146v1) — official announcement instant `2026-03-03T09:00:00+08:00`；按半开窗口 owner report=`2026-03-04`；访问日期 2026-09-02。
- [arXiv:2603.02188v1](https://arxiv.org/abs/2603.02188v1) — official announcement instant `2026-03-03T09:00:00+08:00`；按半开窗口 owner report=`2026-03-04`；访问日期 2026-09-02。
- [arXiv:2603.00188v1](https://arxiv.org/abs/2603.00188v1) — official announcement instant `2026-03-03T09:00:00+08:00`；按半开窗口 owner report=`2026-03-04`；访问日期 2026-09-02。
- [arXiv:2603.01045v1](https://arxiv.org/abs/2603.01045v1) — official announcement instant `2026-03-03T09:00:00+08:00`；按半开窗口 owner report=`2026-03-04`；访问日期 2026-09-02。
- [arXiv:2603.01548v1](https://arxiv.org/abs/2603.01548v1) — official announcement instant `2026-03-03T09:00:00+08:00`；按半开窗口 owner report=`2026-03-04`；访问日期 2026-09-02。
- [arXiv:2603.01581v1](https://arxiv.org/abs/2603.01581v1) — official announcement instant `2026-03-03T09:00:00+08:00`；按半开窗口 owner report=`2026-03-04`；访问日期 2026-09-02。
- [arXiv:2603.01639v1](https://arxiv.org/abs/2603.01639v1) — official announcement instant `2026-03-03T09:00:00+08:00`；按半开窗口 owner report=`2026-03-04`；访问日期 2026-09-02。
- [arXiv:2603.01661v1](https://arxiv.org/abs/2603.01661v1) — official announcement instant `2026-03-03T09:00:00+08:00`；按半开窗口 owner report=`2026-03-04`；访问日期 2026-09-02。
- [arXiv:2603.01683v1](https://arxiv.org/abs/2603.01683v1) — official announcement instant `2026-03-03T09:00:00+08:00`；按半开窗口 owner report=`2026-03-04`；访问日期 2026-09-02。
- [arXiv:2603.01966v1](https://arxiv.org/abs/2603.01966v1) — official announcement instant `2026-03-03T09:00:00+08:00`；按半开窗口 owner report=`2026-03-04`；访问日期 2026-09-02。

## 13. Final Status

- Completion Status: `In Progress`
- Coverage: `Open`
- Evidence: `Open`
- Books: `Open`
- unresolved findings: 4（`MAR26-FC-001 / MAR26-FC-002 / MAR26-FC-003 / MAR26-FC-004`）
