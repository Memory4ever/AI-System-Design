# Daily Research — 2026-07-07

**Research Date:** 2026-07-07

**Timezone:** Asia/Shanghai

**Strict Window:** 2026-07-06 09:00:00 ～ 2026-07-07 09:00:00（北京时间，左闭右开）

**Contract:** V2.1 Full Replay；SRC-DATACITE 是 SRC-ARXIV 的注册恢复 fallback，只作 identity/date metadata；技术 claim 回到精确 arXiv v1 或可追溯历史全文审阅

**Status:** In Progress；Coverage=Open、Evidence=Open、Books=Open；最新合同恢复状态见 Coverage 与第 7、13 节

## Executive Summary
本窗口枚举到 1122 个唯一 arXiv v1 identity；按合同 category 与 AI-System title route 去重后，候选分母冻结为 21 个。当前路由账目为 11 个 Deep、0 个 Standard、10 个 Closure；route 只是审阅义务，不等于 Review 已完成。

本轮没有把 DataCite metadata 或旧 Weekly prose 冒充 primary manuscript。旧 Weekly 只提供 identity、owner 与恢复线索；缺少事件时 evidence version、route locator、claim boundary、RP 和 Prior Review Ref 的 family 一律保持 pending/blocked。只有具备精确 primary receipt 的 family 才能完成评分、Selection 与 Books Decision。

## 1. Coverage

<!-- validator:report-metadata-v2 -->
| Field | Value |
| --- | --- |
| Contract Version | V2.1 |
| Score Schema | V2 |
| Report Type | Daily |
| Window Start | 2026-07-07 |
| Window End | 2026-07-07 |
| Registry Version | 2026-08-25 |
| Coverage Mode | Full Replay |
| Baseline Report | — |
| Changed Source IDs | — |
| Previous Denominator ID | — |
| Denominator ID | daily-2026-07-07-0900-v2.1-july-replay-01 |
| Denominator Frozen At | 2026-08-26T18:00:00+08:00 |
| Completion Status | In Progress |
| Coverage Gate | Open |
| Evidence Gate | Open |
| Books Gate | Open |

### Source Coverage Receipt

<!-- validator:source-coverage-v2 -->
| Source ID | Window Start | Window End | Executed At | Endpoint / Filter | Result | Hits | Candidate Source Families | Pagination / Cursor | Window Watermark | Closure Evidence | Gap / Limitation ID |
| --- | --- | --- | --- | --- | --- | ---: | --- | --- | --- | --- | --- |
| SRC-ARXIV | 2026-07-06T09:00:00+08:00 | 2026-07-07T09:00:00+08:00 | 2026-08-26T18:00:00+08:00 | arXiv official availability schedule + exact-v1 Atom + DataCite DOI created | incomplete | 1295 | SF-2026-ARXIV-2607-02574;SF-2026-ARXIV-2607-02577;SF-2026-ARXIV-2607-02604;SF-2026-ARXIV-2607-02686;SF-2026-ARXIV-2607-02840;SF-2026-ARXIV-2607-02865;SF-2026-ARXIV-2607-02882;SF-2026-ARXIV-2607-02980;SF-2026-ARXIV-2607-03146;SF-2026-ARXIV-2607-03182;SF-2026-ARXIV-2607-03333;SF-2026-ARXIV-2607-03449;SF-2026-ARXIV-2607-03461;SF-2026-ARXIV-2607-03473;SF-2026-ARXIV-2607-03693;SF-2026-ARXIV-2607-03751;SF-2026-ARXIV-2607-03870;SF-2026-ARXIV-2607-03876;SF-2026-ARXIV-2607-03948;SF-2026-ARXIV-2607-03964;SF-2026-ARXIV-2607-04171;SF-2026-ARXIV-2607-04181;SF-2026-ARXIV-2607-04292;SF-2026-ARXIV-2607-04302;SF-2026-ARXIV-2607-04391;SF-2026-ARXIV-2607-04395;SF-2026-ARXIV-2607-04517;SF-2026-ARXIV-2607-04591;SF-2026-ARXIV-2607-04609;SF-2026-ARXIV-2607-04637;SF-2026-ARXIV-2607-04668;SF-2026-ARXIV-2607-04681;SF-2026-ARXIV-2607-04763;SF-2026-ARXIV-2607-04816;SF-2026-ARXIV-2607-04969;SF-2026-ARXIV-2607-05029;SF-2026-ARXIV-2607-05061;SF-2026-ARXIV-2607-05122;SF-2026-ARXIV-2607-05147;SF-2026-ARXIV-2607-05391;SF-2026-ARXIV-2607-05394;SF-2026-ARXIV-2607-05396 | — | 2026-09-03T12:10:00+08:00 | ../_sources/daily-20260707/official-arxiv-first-public-owner-receipt-v1.json; coverage:SRC-ARXIV:20260707; unclosed: canonical candidate redistribution pending | GAP-ARXIV-CANONICAL-REDISTRIBUTION-20260707 |
| SRC-GITHUB-COMMIT | 2026-07-07T00:00:00+08:00 | 2026-07-07T23:59:59+08:00 | 2026-09-03T12:45:00+08:00 | canonical-owner transferred exact artifact provenance from retained Source Review | checked | 2 | SF-2026-ARXIV-2607-03333;SF-2026-ARXIV-2607-03948 | Not Applicable — bounded exact artifact set has no pagination | 2026-09-03T12:45:00+08:00 | coverage:SRC-GITHUB-COMMIT:20260707-owner-transfer | — |

<!-- coverage:SRC-GITHUB-COMMIT:20260707-owner-transfer:start -->
SRC-GITHUB-COMMIT is retained only as exact supporting-artifact provenance for SF-2026-ARXIV-2607-03333; SF-2026-ARXIV-2607-03948 after canonical owner transfer. This receipt does not assert a full historical discovery scan of the source.
<!-- coverage:SRC-GITHUB-COMMIT:20260707-owner-transfer:end -->








<!-- coverage:SRC-ARXIV:20260707:start -->Direct arXiv API/OAI reset connections; registered DataCite fallback froze the strict-window denominator. Canonical source: papers/2026/07/_sources/datacite-arxiv-recovery-20260701-26/datacite-candidate-inventory.json; sha256:d9c5e832203e6c3940bbf234cbbb0fff9e69bcdf1964db69b901cd19b8de6e29; 1122 unique identities in this strict window; 21 routed families.<!-- coverage:SRC-ARXIV:20260707:end -->

### Coverage Limitations

- DataCite 是 Discovery / Metadata fallback，只证明 identity、v1 timestamp、subject 与 abstract；机制和实验结论不从 metadata 推断。
- Artifact-boundary routing 覆盖 21 个 family：exact v1 为 9 个 family 披露 artifact/evidence locator，其中 5 个提供外部 repository/project/demo locator，另有 12 个未披露；本日确认 0 个 family、0 个 event-time pinned commit。未确认 pinned commit 的 locator 只进入 Evidence boundary，不冒充 `SRC-GITHUB-COMMIT` coverage hit。
- 2026-08-25 才生效的机构源与 Hugging Face 不倒推为本历史窗口 Required Daily。工程 release 仍由 Sunday Weekly 承担。
- 标题路由外的垂直应用、单数据集增量和没有状态/控制权变化的论文在 topic-level closure 中拒绝，不用大量零分行稀释账本。


<!-- latest-contract-reopen:2026-07-07:start -->
### Latest-contract Reopen Notice

2026-09-03 全量复核重新打开本日报。旧 `Complete` 只证明原分母内部的表格算术，不证明当前 V2.1 Coverage：arXiv candidate owner receipt 已恢复；当前仍需按 canonical owner 重分配候选与分母。非空 source packet、原 Source Review 与 Books Comparison 暂作 provenance 保留，不作为最新合同验收结论。2026-08-25 才生效的新增来源不倒推为当日 Required receipt，只按 Source Delta Audit 检查真实 in-window family。当前 finding：`canonical_owner_candidate_redistribution_pending, fresh_context_per_identity_semantic_audit_pending, exact_primary_access_recheck_pending`。
<!-- latest-contract-reopen:2026-07-07:end -->

### Canonical raw-inventory recovery checkpoint

本轮已从非空官方 DataCite arXiv DOI snapshot 恢复 **1295** 条注册类别 identity，并以 immutable DOI `created` 与候选级 announcement owner reconciliation 归档到本日。其中 **42** 条是旧报告 retained provenance，**1253** 条已获得逐 family title+abstract closure proposal。这些 proposal 尚未经过 fresh-context false-positive/false-negative audit，旧候选也尚未按 canonical owner 完成重分配；因此 Coverage、Evidence、Books 与 Completion 继续保持 Open。

## 2. Candidate Ledger

<!-- validator:candidate-ledger-v2.1 -->
| Source Family ID | Primary Identifier | Event Identity | Owner Week | First-public Date | Supporting Source IDs | Design Delta | System Reach | Durability | Total | Candidate State | Review Status | Access Status | Review Override | Review Ref | Owner Report Ref | Prior Review Ref | Reconciliation | Stable Node ID | Books Disposition | Books Review Ref | Benchmark Claim |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2607-02574 | arXiv:2607.02574v1 | paper-v1:2607.02574 | 2026-W28 | 2026-07-07 | SRC-ARXIV | 1 | 2 | 1 | 4 | closure_only | closure_complete | accessible | none | review:SF-2026-ARXIV-2607-02574 | self | — | new_in_window | INFER-KV-CACHE | Rejected — Low Durability / Out of Scope | — | no |
| SF-2026-ARXIV-2607-02577 | arXiv:2607.02577v1 | paper-v1:2607.02577 | 2026-W28 | 2026-07-07 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-02577 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Integrate | books-review:SF-2026-ARXIV-2607-02577 | no |
| SF-2026-ARXIV-2607-02604 | arXiv:2607.02604v1 | paper-v1:2607.02604 | 2026-W28 | 2026-07-07 | SRC-ARXIV | 1 | 2 | 1 | 4 | closure_only | closure_complete | accessible | none | review:SF-2026-ARXIV-2607-02604 | self | — | new_in_window | MULTIMODAL-EMBODIED-VLA | Rejected — Low Durability / Out of Scope | — | no |
| SF-2026-ARXIV-2607-02686 | arXiv:2607.02686v1 | paper-v1:2607.02686 | 2026-W28 | 2026-07-07 | SRC-ARXIV | 1 | 2 | 0 | 3 | closure_only | closure_complete | accessible | none | review:SF-2026-ARXIV-2607-02686 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Rejected — Low Durability / Out of Scope | — | no |
| SF-2026-ARXIV-2607-02840 | arXiv:2607.02840v1 | paper-v1:2607.02840 | 2026-W28 | 2026-07-07 | SRC-ARXIV | 1 | 2 | 0 | 3 | closure_only | closure_complete | accessible | none | review:SF-2026-ARXIV-2607-02840 | self | — | new_in_window | MULTIMODAL-WORLD-MODELS | Rejected — Low Durability / Out of Scope | — | no |
| SF-2026-ARXIV-2607-02865 | arXiv:2607.02865v1 | paper-v1:2607.02865 | 2026-W28 | 2026-07-07 | SRC-ARXIV | 1 | 1 | 1 | 3 | closure_only | closure_complete | accessible | none | review:SF-2026-ARXIV-2607-02865 | self | — | new_in_window | MULTIMODAL-WORLD-MODELS | Rejected — Low Durability / Out of Scope | — | no |
| SF-2026-ARXIV-2607-02882 | arXiv:2607.02882v1 | paper-v1:2607.02882 | 2026-W28 | 2026-07-07 | SRC-ARXIV | 1 | 2 | 0 | 3 | closure_only | closure_complete | accessible | none | review:SF-2026-ARXIV-2607-02882 | self | — | new_in_window | AGENT-WORKFLOW | Rejected — Low Durability / Out of Scope | — | no |
| SF-2026-ARXIV-2607-02980 | arXiv:2607.02980v1 | paper-v1:2607.02980 | 2026-W28 | 2026-07-07 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-02980 | self | — | new_in_window | MODEL-LONG-CONTEXT | Integrate | books-review:SF-2026-ARXIV-2607-02980 | yes |
| SF-2026-ARXIV-2607-03146 | arXiv:2607.03146v1 | paper-v1:2607.03146 | 2026-W28 | 2026-07-07 | SRC-ARXIV | 1 | 2 | 0 | 3 | closure_only | closure_complete | accessible | none | review:SF-2026-ARXIV-2607-03146 | self | — | new_in_window | MULTIMODAL-EMBODIED-VLA | Rejected — Low Durability / Out of Scope | — | no |
| SF-2026-ARXIV-2607-03182 | arXiv:2607.03182v1 | paper-v1:2607.03182 | 2026-W28 | 2026-07-07 | SRC-ARXIV | 1 | 1 | 1 | 3 | closure_only | closure_complete | accessible | none | review:SF-2026-ARXIV-2607-03182 | self | — | new_in_window | MULTIMODAL-EMBODIED-VLA | Rejected — Low Durability / Out of Scope | — | no |
| SF-2026-ARXIV-2607-03333 | arXiv:2607.03333v1 | paper-v1:2607.03333 | 2026-W28 | 2026-07-07 | SRC-ARXIV; SRC-GITHUB-COMMIT | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-03333 | self | — | new_in_window | INFER-SPECULATIVE-DECODING | Integrate | books-review:SF-2026-ARXIV-2607-03333 | yes |
| SF-2026-ARXIV-2607-03449 | arXiv:2607.03449v1 | paper-v1:2607.03449 | 2026-W28 | 2026-07-07 | SRC-ARXIV | 1 | 2 | 1 | 4 | closure_only | closure_complete | accessible | none | review:SF-2026-ARXIV-2607-03449 | self | — | new_in_window | MULTIMODAL-EMBODIED-VLA | Rejected — Low Durability / Out of Scope | — | no |
| SF-2026-ARXIV-2607-03461 | arXiv:2607.03461v1 | paper-v1:2607.03461 | 2026-W28 | 2026-07-07 | SRC-ARXIV | 1 | 2 | 0 | 3 | closure_only | closure_complete | accessible | none | review:SF-2026-ARXIV-2607-03461 | self | — | new_in_window | MULTIMODAL-WORLD-MODELS | Rejected — Low Durability / Out of Scope | — | no |
| SF-2026-ARXIV-2607-03473 | arXiv:2607.03473v1 | paper-v1:2607.03473 | 2026-W28 | 2026-07-07 | SRC-ARXIV | 1 | 2 | 1 | 4 | closure_only | closure_complete | accessible | none | review:SF-2026-ARXIV-2607-03473 | self | — | new_in_window | INFER-SCHEDULING | Rejected — Low Durability / Out of Scope | — | no |
| SF-2026-ARXIV-2607-03693 | arXiv:2607.03693v1 | paper-v1:2607.03693 | 2026-W28 | 2026-07-07 | SRC-ARXIV | 1 | 2 | 1 | 4 | closure_only | closure_complete | accessible | none | review:SF-2026-ARXIV-2607-03693 | self | — | new_in_window | MULTIMODAL-EMBODIED-VLA | Rejected — Low Durability / Out of Scope | — | no |
| SF-2026-ARXIV-2607-03751 | arXiv:2607.03751v1 | paper-v1:2607.03751 | 2026-W28 | 2026-07-07 | SRC-ARXIV | 1 | 2 | 1 | 4 | closure_only | closure_complete | accessible | none | review:SF-2026-ARXIV-2607-03751 | self | — | new_in_window | MULTIMODAL-EMBODIED-VLA | Rejected — Low Durability / Out of Scope | — | no |
| SF-2026-ARXIV-2607-03870 | arXiv:2607.03870v1 | paper-v1:2607.03870 | 2026-W28 | 2026-07-07 | SRC-ARXIV | 1 | 2 | 1 | 4 | closure_only | closure_complete | accessible | none | review:SF-2026-ARXIV-2607-03870 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Rejected — Low Durability / Out of Scope | — | no |
| SF-2026-ARXIV-2607-03876 | arXiv:2607.03876v1 | paper-v1:2607.03876 | 2026-W28 | 2026-07-07 | SRC-ARXIV | 1 | 2 | 1 | 4 | closure_only | closure_complete | accessible | none | review:SF-2026-ARXIV-2607-03876 | self | — | new_in_window | INFER-SPECULATIVE-DECODING | Rejected — Low Durability / Out of Scope | — | no |
| SF-2026-ARXIV-2607-03948 | arXiv:2607.03948v1 | paper-v1:2607.03948 | 2026-W28 | 2026-07-07 | SRC-ARXIV; SRC-GITHUB-COMMIT | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-03948 | self | — | new_in_window | INFER-SCHEDULING | Integrate | books-review:SF-2026-ARXIV-2607-03948 | yes |
| SF-2026-ARXIV-2607-03964 | arXiv:2607.03964v1 | paper-v1:2607.03964 | 2026-W28 | 2026-07-07 | SRC-ARXIV | 1 | 2 | 0 | 3 | closure_only | closure_complete | accessible | none | review:SF-2026-ARXIV-2607-03964 | self | — | new_in_window | MULTIMODAL-WORLD-MODELS | Rejected — Low Durability / Out of Scope | — | no |
| SF-2026-ARXIV-2607-04171 | arXiv:2607.04171v1 | paper-v1:2607.04171 | 2026-W28 | 2026-07-07 | SRC-ARXIV | 1 | 2 | 0 | 3 | closure_only | closure_complete | accessible | none | review:SF-2026-ARXIV-2607-04171 | self | — | new_in_window | MULTIMODAL-EMBODIED-VLA | Rejected — Low Durability / Out of Scope | — | no |
| SF-2026-ARXIV-2607-04181 | arXiv:2607.04181v1 | paper-v1:2607.04181 | 2026-W28 | 2026-07-07 | SRC-ARXIV | 3 | 3 | 2 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-04181 | self | — | new_in_window | INFER-SCHEDULING | Integrate | books-review:SF-2026-ARXIV-2607-04181 | yes |
| SF-2026-ARXIV-2607-04292 | arXiv:2607.04292v1 | paper-v1:2607.04292 | 2026-W28 | 2026-07-07 | SRC-ARXIV | 1 | 2 | 1 | 4 | closure_only | closure_complete | accessible | none | review:SF-2026-ARXIV-2607-04292 | self | — | new_in_window | AGENT-MULTI-AGENT | Rejected — Low Durability / Out of Scope | — | no |
| SF-2026-ARXIV-2607-04302 | arXiv:2607.04302v1 | paper-v1:2607.04302 | 2026-W28 | 2026-07-07 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-04302 | self | — | new_in_window | INFER-TENSORRT-LLM | Integrate | books-review:SF-2026-ARXIV-2607-04302 | yes |
| SF-2026-ARXIV-2607-04391 | arXiv:2607.04391v1 | paper-v1:2607.04391 | 2026-W28 | 2026-07-07 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-04391 | self | — | new_in_window | AGENT-MEMORY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2607-04391 | no |
| SF-2026-ARXIV-2607-04395 | arXiv:2607.04395v1 | paper-v1:2607.04395 | 2026-W28 | 2026-07-07 | SRC-ARXIV | 2 | 2 | 2 | 6 | retained | standard_complete | accessible | none | review:SF-2026-ARXIV-2607-04395 | self | — | new_in_window | INFER-TENSORRT-LLM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2607-04395 | yes |
| SF-2026-ARXIV-2607-04517 | arXiv:2607.04517v1 | paper-v1:2607.04517 | 2026-W28 | 2026-07-07 | SRC-ARXIV | 1 | 1 | 0 | 2 | closure_only | closure_complete | accessible | none | review:SF-2026-ARXIV-2607-04517 | self | — | new_in_window | MULTIMODAL-EMBODIED-VLA | Rejected — Low Durability / Out of Scope | — | no |
| SF-2026-ARXIV-2607-04591 | arXiv:2607.04591v1 | paper-v1:2607.04591 | 2026-W28 | 2026-07-07 | SRC-ARXIV | 1 | 2 | 1 | 4 | closure_only | closure_complete | accessible | none | review:SF-2026-ARXIV-2607-04591 | self | — | new_in_window | MULTIMODAL-EMBODIED-VLA | Rejected — Low Durability / Out of Scope | — | no |
| SF-2026-ARXIV-2607-04609 | arXiv:2607.04609v1 | paper-v1:2607.04609 | 2026-W28 | 2026-07-07 | SRC-ARXIV | 1 | 2 | 1 | 4 | closure_only | closure_complete | accessible | none | review:SF-2026-ARXIV-2607-04609 | self | — | new_in_window | MULTIMODAL-EMBODIED-VLA | Rejected — Low Durability / Out of Scope | — | no |
| SF-2026-ARXIV-2607-04637 | arXiv:2607.04637v1 | paper-v1:2607.04637 | 2026-W28 | 2026-07-07 | SRC-ARXIV | 1 | 2 | 0 | 3 | closure_only | closure_complete | accessible | none | review:SF-2026-ARXIV-2607-04637 | self | — | new_in_window | MULTIMODAL-EMBODIED-VLA | Rejected — Low Durability / Out of Scope | — | no |
| SF-2026-ARXIV-2607-04668 | arXiv:2607.04668v1 | paper-v1:2607.04668 | 2026-W28 | 2026-07-07 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-04668 | self | — | new_in_window | INFER-SCHEDULING | Integrate | books-review:SF-2026-ARXIV-2607-04668 | yes |
| SF-2026-ARXIV-2607-04681 | arXiv:2607.04681v1 | paper-v1:2607.04681 | 2026-W28 | 2026-07-07 | SRC-ARXIV | 0 | 2 | 1 | 3 | closure_only | closure_complete | accessible | none | review:SF-2026-ARXIV-2607-04681 | self | — | new_in_window | MULTIMODAL-EMBODIED-VLA | Rejected — Low Durability / Out of Scope | — | no |
| SF-2026-ARXIV-2607-04763 | arXiv:2607.04763v1 | paper-v1:2607.04763 | 2026-W28 | 2026-07-07 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-04763 | self | — | new_in_window | TRAIN-SFT | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2607-04763 | yes |
| SF-2026-ARXIV-2607-04816 | arXiv:2607.04816v1 | paper-v1:2607.04816 | 2026-W28 | 2026-07-07 | SRC-ARXIV | 1 | 1 | 0 | 2 | closure_only | closure_complete | accessible | none | review:SF-2026-ARXIV-2607-04816 | self | — | new_in_window | MULTIMODAL-EMBODIED-VLA | Rejected — Low Durability / Out of Scope | — | no |
| SF-2026-ARXIV-2607-04969 | arXiv:2607.04969v1 | paper-v1:2607.04969 | 2026-W28 | 2026-07-07 | SRC-ARXIV | 1 | 2 | 1 | 4 | closure_only | closure_complete | accessible | none | review:SF-2026-ARXIV-2607-04969 | self | — | new_in_window | TRAIN-PRETRAINING | Rejected — Low Durability / Out of Scope | — | no |
| SF-2026-ARXIV-2607-05029 | arXiv:2607.05029v1 | paper-v1:2607.05029 | 2026-W28 | 2026-07-07 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-05029 | self | — | new_in_window | PLATFORM-SECURITY | Integrate | books-review:SF-2026-ARXIV-2607-05029 | yes |
| SF-2026-ARXIV-2607-05061 | arXiv:2607.05061v1 | paper-v1:2607.05061 | 2026-W28 | 2026-07-07 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-05061 | self | — | new_in_window | INFER-KV-CACHE | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2607-05061 | yes |
| SF-2026-ARXIV-2607-05122 | arXiv:2607.05122v1 | paper-v1:2607.05122 | 2026-W28 | 2026-07-07 | SRC-ARXIV | 1 | 2 | 1 | 4 | closure_only | closure_complete | accessible | none | review:SF-2026-ARXIV-2607-05122 | self | — | new_in_window | MULTIMODAL-EMBODIED-VLA | Rejected — Low Durability / Out of Scope | — | no |
| SF-2026-ARXIV-2607-05147 | arXiv:2607.05147v1 | paper-v1:2607.05147 | 2026-W28 | 2026-07-07 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-05147 | self | — | new_in_window | INFER-SPECULATIVE-DECODING | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2607-05147 | yes |
| SF-2026-ARXIV-2607-05391 | arXiv:2607.05391v1 | paper-v1:2607.05391 | 2026-W28 | 2026-07-07 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-05391 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2607-05391 | yes |
| SF-2026-ARXIV-2607-05394 | arXiv:2607.05394v1 | paper-v1:2607.05394 | 2026-W28 | 2026-07-07 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2607-05394 | self | — | new_in_window | TRAIN-SFT | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2607-05394 | yes |
| SF-2026-ARXIV-2607-05396 | arXiv:2607.05396v1 | paper-v1:2607.05396 | 2026-W28 | 2026-07-07 | SRC-ARXIV | 0 | 2 | 1 | 3 | closure_only | closure_complete | accessible | none | review:SF-2026-ARXIV-2607-05396 | self | — | new_in_window | MULTIMODAL-EMBODIED-VLA | Rejected — Low Durability / Out of Scope | — | no |
## 3. Review Completion Receipt

<!-- validator:review-completion-v1 -->
| Source Family ID | Review Provenance ID | Review Route | Primary Evidence Version | Reviewed Evidence Versions | Method / Identity Locators | Evaluation Locators | Limitations / Counterevidence Locators | Artifact Locators | Claim Boundary Ref | Completion Result |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2607-02574 | RP-257ead4190539142 | closure | doi:10.48550/arxiv.2607.02574@v1 | SRC-DATACITE@doi:10.48550/arxiv.2607.02574@v1 | doi:10.48550/arxiv.2607.02574#identity; DataCite Submitted:v1 timestamp | Not Required — closure route makes no mechanism or benchmark claim | Not Required — DataCite abstract is Discovery / Metadata and no technical claim is retained | Not Required — closure route; no artifact claim retained | claim:SF-2026-ARXIV-2607-02574 | complete |
| SF-2026-ARXIV-2607-02577 | RP-a36e36382f707535 | deep | arXiv:2607.02577v1 | SRC-ARXIV@arXiv:2607.02577v1 | https://arxiv.org/html/2607.02577v1#S3 :: trace-level disagreement taxonomy, reproducibility analysis, corrected evaluator and deterministic-first protocol with restricted judge fallback | https://arxiv.org/html/2607.02577v1#S4 :: author audit covers four tool-calling benchmark families, complete traces, expert adjudication and repeated judge runs; it does not establish a new model ranking | https://arxiv.org/html/2607.02577v1#S5 :: evidence diagnoses selected benchmark/evaluator configurations; artifact release was still pending and evaluator agreement does not prove task representativeness | https://arxiv.org/html/2607.02577v1#S6 :: corrected artifacts and Harness Lab were announced but versioned public identifiers were not yet disclosed | claim:SF-2026-ARXIV-2607-02577 | complete |
| SF-2026-ARXIV-2607-02604 | RP-54af7759241e1226 | closure | doi:10.48550/arxiv.2607.02604@v1 | SRC-DATACITE@doi:10.48550/arxiv.2607.02604@v1 | doi:10.48550/arxiv.2607.02604#identity; DataCite Submitted:v1 timestamp | Not Required — closure route makes no mechanism or benchmark claim | Not Required — DataCite abstract is Discovery / Metadata and no technical claim is retained | Not Required — closure route; no artifact claim retained | claim:SF-2026-ARXIV-2607-02604 | complete |
| SF-2026-ARXIV-2607-02686 | RP-b9ad29aa69d0ba1c | closure | doi:10.48550/arxiv.2607.02686@v1 | SRC-DATACITE@doi:10.48550/arxiv.2607.02686@v1 | doi:10.48550/arxiv.2607.02686#identity; DataCite Submitted:v1 timestamp | Not Required — closure route makes no mechanism or benchmark claim | Not Required — DataCite abstract is Discovery / Metadata and no technical claim is retained | Not Required — closure route; no artifact claim retained | claim:SF-2026-ARXIV-2607-02686 | complete |
| SF-2026-ARXIV-2607-02840 | RP-1073abf41e79e65a | closure | doi:10.48550/arxiv.2607.02840@v1 | SRC-DATACITE@doi:10.48550/arxiv.2607.02840@v1 | doi:10.48550/arxiv.2607.02840#identity; DataCite Submitted:v1 timestamp | Not Required — closure route makes no mechanism or benchmark claim | Not Required — DataCite abstract is Discovery / Metadata and no technical claim is retained | Not Required — closure route; no artifact claim retained | claim:SF-2026-ARXIV-2607-02840 | complete |
| SF-2026-ARXIV-2607-02865 | RP-a2879a38b4543394 | closure | doi:10.48550/arxiv.2607.02865@v1 | SRC-DATACITE@doi:10.48550/arxiv.2607.02865@v1 | doi:10.48550/arxiv.2607.02865#identity; DataCite Submitted:v1 timestamp | Not Required — closure route makes no mechanism or benchmark claim | Not Required — DataCite abstract is Discovery / Metadata and no technical claim is retained | Not Required — closure route; no artifact claim retained | claim:SF-2026-ARXIV-2607-02865 | complete |
| SF-2026-ARXIV-2607-02882 | RP-ccedea45a6f10870 | closure | doi:10.48550/arxiv.2607.02882@v1 | SRC-DATACITE@doi:10.48550/arxiv.2607.02882@v1 | doi:10.48550/arxiv.2607.02882#identity; DataCite Submitted:v1 timestamp | Not Required — closure route makes no mechanism or benchmark claim | Not Required — DataCite abstract is Discovery / Metadata and no technical claim is retained | Not Required — closure route; no artifact claim retained | claim:SF-2026-ARXIV-2607-02882 | complete |
| SF-2026-ARXIV-2607-02980 | RP-c099d1a1d6a7ec22 | deep | arXiv:2607.02980v1 | SRC-ARXIV@arXiv:2607.02980v1 | https://arxiv.org/html/2607.02980v1#S2.SS2 :: mean/max pooled chunk summaries cannot uniformly approximate query-dependent LogSumExp chunk mass; https://arxiv.org/html/2607.02980v1#S3 :: affine first-order chunk-mass surrogate and hierarchical inter-/intra-chunk normalization place retrieval scores in the forward path; https://arxiv.org/html/2607.02980v1#S4.SS1 through #S4.SS3 :: landmark/query calibration, HoPE/GQA variants, adjacent-query packing and checkpoint migration; https://arxiv.org/html/2607.02980v1#A1 and #A2 :: derivation and proof details | https://arxiv.org/html/2607.02980v1#S5.SS1 through #S5.SS3 :: 345M 8K/256K training, dense/sparse baselines, PPL, modified RULER/NIAH and ablations; https://arxiv.org/html/2607.02980v1#S6.SS1 and #S6.SS2 :: 1.4B from-scratch and OLMo3-7B conversion studies; https://arxiv.org/html/2607.02980v1#S7.SS1 and #S7.SS2 :: single-H800 SGLang/Triton inference and adjacent-query overlap; https://arxiv.org/html/2607.02980v1#A4 through #A8 :: recipes and evaluator details | https://arxiv.org/html/2607.02980v1#S4.SS1 and #S5.SS3 :: position encoding, query calibration and landmark choices materially affect extrapolation, and the calibration mechanism is not fully understood; https://arxiv.org/html/2607.02980v1#S6.SS2 :: 7B migration cost and short/general-task trade-offs remain recipe-bound; https://arxiv.org/html/2607.02980v1#S7.SS1 :: latency uses one H800, batch 1 and matched Triton kernels, with full attention faster below the reported crossover; Not Disclosed — no production concurrency/arrival/SLO study or independent replication | https://github.com/Tencent-Hunyuan/HiLS-Attention :: repository linked by v1; bounded event-time query found no commit at or before 2026-07-03T05:39:00Z. The first visible commit 562167440a4ae460c32e4e8136e0a2ee45e0b71d is five minutes after v1 and is not event-time implementation evidence. | claim:SF-2026-ARXIV-2607-02980 | complete |
| SF-2026-ARXIV-2607-03146 | RP-c50219892b185cab | closure | doi:10.48550/arxiv.2607.03146@v1 | SRC-DATACITE@doi:10.48550/arxiv.2607.03146@v1 | doi:10.48550/arxiv.2607.03146#identity; DataCite Submitted:v1 timestamp | Not Required — closure route makes no mechanism or benchmark claim | Not Required — DataCite abstract is Discovery / Metadata and no technical claim is retained | Not Required — closure route; no artifact claim retained | claim:SF-2026-ARXIV-2607-03146 | complete |
| SF-2026-ARXIV-2607-03182 | RP-1586613855615e84 | closure | doi:10.48550/arxiv.2607.03182@v1 | SRC-DATACITE@doi:10.48550/arxiv.2607.03182@v1 | doi:10.48550/arxiv.2607.03182#identity; DataCite Submitted:v1 timestamp | Not Required — closure route makes no mechanism or benchmark claim | Not Required — DataCite abstract is Discovery / Metadata and no technical claim is retained | Not Required — closure route; no artifact claim retained | claim:SF-2026-ARXIV-2607-03182 | complete |
| SF-2026-ARXIV-2607-03333 | RP-2a7770e7cef5c105 | deep | arXiv:2607.03333v1 | SRC-ARXIV@arXiv:2607.03333v1; SRC-GITHUB-COMMIT@commit:a027e4287758affd1fd4ecd0e1e79991faad1804 | https://arxiv.org/html/2607.03333v1#S2.SS2 :: overlap cost model and break-even condition; https://arxiv.org/html/2607.03333v1#S3 through #S5 :: forced-prefix self-probe, D1 prefix-KV fork, D2 confidence gate, D3 verified-prefix reuse, strict action-match commit and read-only manifest boundary; https://arxiv.org/html/2607.03333v1#A1, #A2 and #A8 :: derivation, partial-token acceptance and late-probe supersession | https://arxiv.org/html/2607.03333v1#S6.SS1 through #S6.SS6 :: Qwen3-4B/32B and Qwen3.5-35B-A3B on H20-3e, bf16, vLLM, greedy think-mode, GAIA/HotpotQA/tau2 latency and quality, component ablations, drafter comparison and break-even sweep; https://arxiv.org/html/2607.03333v1#A3 through #A7 :: BrowseComp, serving configuration and format-divergence details | https://arxiv.org/html/2607.03333v1#S6.SS3 and #S6.SS6 :: real-network nondeterminism, fast tools, short/no-think decode, format divergence, probe overhead and batching can shrink or reverse benefit; https://arxiv.org/html/2607.03333v1#S8 :: only read-only tools and open serving interfaces are in scope; https://arxiv.org/html/2607.03333v1#A6 through #A8 :: format collapse, small-model boundary and cancellation/supersession; exact action match does not undo quota, privacy or external side effects | https://github.com/baihuajun24/spork/tree/a027e4287758affd1fd4ecd0e1e79991faad1804 :: latest commit at or before v1, timestamp 2026-07-03T13:05:25Z; tree contains controller, gates, executor, vLLM integration, tau2 backend and evaluation entrypoints | claim:SF-2026-ARXIV-2607-03333 | complete |
| SF-2026-ARXIV-2607-03449 | RP-72a7e56ed853d105 | closure | doi:10.48550/arxiv.2607.03449@v1 | SRC-DATACITE@doi:10.48550/arxiv.2607.03449@v1 | doi:10.48550/arxiv.2607.03449#identity; DataCite Submitted:v1 timestamp | Not Required — closure route makes no mechanism or benchmark claim | Not Required — DataCite abstract is Discovery / Metadata and no technical claim is retained | Not Required — closure route; no artifact claim retained | claim:SF-2026-ARXIV-2607-03449 | complete |
| SF-2026-ARXIV-2607-03461 | RP-a5c0cf72f08b22e7 | closure | doi:10.48550/arxiv.2607.03461@v1 | SRC-DATACITE@doi:10.48550/arxiv.2607.03461@v1 | doi:10.48550/arxiv.2607.03461#identity; DataCite Submitted:v1 timestamp | Not Required — closure route makes no mechanism or benchmark claim | Not Required — DataCite abstract is Discovery / Metadata and no technical claim is retained | Not Required — closure route; no artifact claim retained | claim:SF-2026-ARXIV-2607-03461 | complete |
| SF-2026-ARXIV-2607-03473 | RP-d9d2d051fd597799 | closure | doi:10.48550/arxiv.2607.03473@v1 | SRC-DATACITE@doi:10.48550/arxiv.2607.03473@v1 | doi:10.48550/arxiv.2607.03473#identity; DataCite Submitted:v1 timestamp | Not Required — closure route makes no mechanism or benchmark claim | Not Required — DataCite abstract is Discovery / Metadata and no technical claim is retained | Not Required — closure route; no artifact claim retained | claim:SF-2026-ARXIV-2607-03473 | complete |
| SF-2026-ARXIV-2607-03693 | RP-b317ec66f39dc724 | closure | doi:10.48550/arxiv.2607.03693@v1 | SRC-DATACITE@doi:10.48550/arxiv.2607.03693@v1 | doi:10.48550/arxiv.2607.03693#identity; DataCite Submitted:v1 timestamp | Not Required — closure route makes no mechanism or benchmark claim | Not Required — DataCite abstract is Discovery / Metadata and no technical claim is retained | Not Required — closure route; no artifact claim retained | claim:SF-2026-ARXIV-2607-03693 | complete |
| SF-2026-ARXIV-2607-03751 | RP-a27cdea39aa4a2c0 | closure | doi:10.48550/arxiv.2607.03751@v1 | SRC-DATACITE@doi:10.48550/arxiv.2607.03751@v1 | doi:10.48550/arxiv.2607.03751#identity; DataCite Submitted:v1 timestamp | Not Required — closure route makes no mechanism or benchmark claim | Not Required — DataCite abstract is Discovery / Metadata and no technical claim is retained | Not Required — closure route; no artifact claim retained | claim:SF-2026-ARXIV-2607-03751 | complete |
| SF-2026-ARXIV-2607-03870 | RP-419291148783521f | closure | doi:10.48550/arxiv.2607.03870@v1 | SRC-DATACITE@doi:10.48550/arxiv.2607.03870@v1 | doi:10.48550/arxiv.2607.03870#identity; DataCite Submitted:v1 timestamp | Not Required — closure route makes no mechanism or benchmark claim | Not Required — DataCite abstract is Discovery / Metadata and no technical claim is retained | Not Required — closure route; no artifact claim retained | claim:SF-2026-ARXIV-2607-03870 | complete |
| SF-2026-ARXIV-2607-03876 | RP-5509f92293072965 | closure | doi:10.48550/arxiv.2607.03876@v1 | SRC-DATACITE@doi:10.48550/arxiv.2607.03876@v1 | doi:10.48550/arxiv.2607.03876#identity; DataCite Submitted:v1 timestamp | Not Required — closure route makes no mechanism or benchmark claim | Not Required — DataCite abstract is Discovery / Metadata and no technical claim is retained | Not Required — closure route; no artifact claim retained | claim:SF-2026-ARXIV-2607-03876 | complete |
| SF-2026-ARXIV-2607-03948 | RP-905250919facbb59 | deep | arXiv:2607.03948v1 | SRC-ARXIV@arXiv:2607.03948v1; SRC-GITHUB-COMMIT@commit:c14eea013db3d60ad1aba0780a3d65688bfb9c19 | https://arxiv.org/html/2607.03948v1#S2.SS0.SSS0.Px2, #S2.SS0.SSS0.Px5 and #S2.SS0.SSS0.Px6 :: central buffering, release-when-startable admission and time-coupled batch/KV occupancy; https://arxiv.org/html/2607.03948v1#S3.SS1 through #S3.SS3 :: SLO-weighted action reward, online LP constraints, dual shadow prices, SAA history and projected subgradient updates; https://arxiv.org/html/2607.03948v1#A2.SS1 and #A2.SS3 :: pseudocode | https://arxiv.org/html/2607.03948v1#S4.SS1 :: Vidur-only simulation on four A100 GPUs with LMSYS-Chat-1M and synthetic P/D-ratio workloads; model, precision, batch/concurrency and exact serving SLO Not Disclosed; https://arxiv.org/html/2607.03948v1#S4.SS2 and #S4.SS3 :: RR/LOR/Random/Power-of-2 baselines, noisy length estimates, objective sweeps and an arrival-rate shift; https://arxiv.org/html/2607.03948v1#A3 :: broader sweeps and tail-weight sensitivity | https://arxiv.org/html/2607.03948v1#S6 :: simulation-only, without serving-engine integration, preemption, KV swapping, distributed coordination, heterogeneous priorities or fairness validation; https://arxiv.org/html/2607.03948v1#A1.SS0.SSS0.Px9 :: PD-mixing duration is input-dependent; no LLM-specific theorem/regret/convergence or component ablation. Event-time artifact only partially corresponds to the manuscript noisy-length/tail-objective interface. | https://github.com/qqwetidx/Online-Linear-Programming-for-Vidur/tree/c14eea013db3d60ad1aba0780a3d65688bfb9c19 :: only repository commit, authored 2026-01-18 before v1; implements time-indexed batch/KV occupancy, projected dual-price updates and margin-ranked feasible admission, but only partially reproduces the full manuscript objective/prediction contract | claim:SF-2026-ARXIV-2607-03948 | complete |
| SF-2026-ARXIV-2607-03964 | RP-809d4d70726e28aa | closure | doi:10.48550/arxiv.2607.03964@v1 | SRC-DATACITE@doi:10.48550/arxiv.2607.03964@v1 | doi:10.48550/arxiv.2607.03964#identity; DataCite Submitted:v1 timestamp | Not Required — closure route makes no mechanism or benchmark claim | Not Required — DataCite abstract is Discovery / Metadata and no technical claim is retained | Not Required — closure route; no artifact claim retained | claim:SF-2026-ARXIV-2607-03964 | complete |
| SF-2026-ARXIV-2607-04171 | RP-66f278ba4a8cb9be | closure | doi:10.48550/arxiv.2607.04171@v1 | SRC-DATACITE@doi:10.48550/arxiv.2607.04171@v1 | doi:10.48550/arxiv.2607.04171#identity; DataCite Submitted:v1 timestamp | Not Required — closure route makes no mechanism or benchmark claim | Not Required — DataCite abstract is Discovery / Metadata and no technical claim is retained | Not Required — closure route; no artifact claim retained | claim:SF-2026-ARXIV-2607-04171 | complete |
| SF-2026-ARXIV-2607-04181 | RP-4526ccb507bc4310 | deep | arXiv:2607.04181v1 | SRC-ARXIV@arXiv:2607.04181v1 | https://arxiv.org/html/2607.04181v1#S3.SS1 through #S3.SS1.p4.1 :: feasible layer-replication configuration, request scatter/gather across consecutive layer segments and partitioned KV redistribution during configuration transition; https://arxiv.org/html/2607.04181v1#S3.SS2.p1.1 through #S3.SS2.p3.1 :: bidirectional chunked ring multicast for weights and fine-grained KV transfer overlapped with inter-token intervals; https://arxiv.org/html/2607.04181v1#S4.E1 through #S4.E10 and #S4.SS4 :: configuration search and migration cost model | https://arxiv.org/html/2607.04181v1#S4.SS1 and #S6.SS1 through #S6.SS3 :: Nano-vLLM-based prototype on four NVLink-connected H20 GPUs, Qwen3 8B/14B/32B, Alibaba/Azure trace replays and LongBench prompts; compares static vLLM and a threshold autoscaler using average/P99 latency and SLO attainment | https://arxiv.org/html/2607.04181v1#S4.SS2 and #S6.SS3 :: analytical ranking assumes homogeneous devices and divisible layer placements; no PCIe/Ethernet fabric, heterogeneous failure recovery, arbitrary graph, public artifact or production-fleet validation | Not Disclosed — v1 identifies a Nano-vLLM-based prototype but provides no CoCoScale repository, commit, tag or release | claim:SF-2026-ARXIV-2607-04181 | complete |
| SF-2026-ARXIV-2607-04292 | RP-5761dd695db0dcd7 | closure | doi:10.48550/arxiv.2607.04292@v1 | SRC-DATACITE@doi:10.48550/arxiv.2607.04292@v1 | doi:10.48550/arxiv.2607.04292#identity; DataCite Submitted:v1 timestamp | Not Required — closure route makes no mechanism or benchmark claim | Not Required — DataCite abstract is Discovery / Metadata and no technical claim is retained | Not Required — closure route; no artifact claim retained | claim:SF-2026-ARXIV-2607-04292 | complete |
| SF-2026-ARXIV-2607-04302 | RP-fe3ac22acabb985a | deep | arXiv:2607.04302v1 | SRC-ARXIV@arXiv:2607.04302v1 | https://arxiv.org/html/2607.04302v1#S4.SS1 through #S4.SS4 and #S4.E1 through #S4.E3 :: diagnose parameter-induced K-channel outliers after QK-RMSNorm, apply diagonal post-RoPE Q scaling with inverse K scaling, and gate static calibration; https://arxiv.org/html/2607.04302v1#S4.SS5 and #Thmtheorem1 :: reorder quantized P so numerator and denominator share the same tensor, fuse normalization into PV, and delimit the coherent-error result to fixed V | https://arxiv.org/html/2607.04302v1#S5, #S5.SS4 and #S6.T7 :: zero-shot option-likelihood and attention-error diagnostics across Qwen3-8B, Gemma2-9B, Llama3.1-8B, Mistral-7B and Phi-4B plus one Qwen3 long-context retrieval case; https://arxiv.org/html/2607.04302v1#A2.SS0.SSS0.Px1 through #A2.SS0.SSS0.Px7 :: scoring, prompt, dtype, calibration, hook, software/hardware and determinism settings | https://arxiv.org/html/2607.04302v1#S7.SS0.SSS0.Px3 and #Thmtheorem1 :: all latency numbers are theoretical instruction-scheduling estimates, target hardware was not available for direct validation, and the theorem holds V fixed; applicability also depends on the calibrated outlier regime, while gate thresholds are tested on five models only and the promised implementation artifact is absent | Not Disclosed — v1 promises the exact library, framework/toolkit and code in a future release; no public repository, commit or tag is identified | claim:SF-2026-ARXIV-2607-04302 | complete |
| SF-2026-ARXIV-2607-04391 | RP-25c2eb35c31cb479 | standard | arXiv:2607.04391v1 | SRC-ARXIV@arXiv:2607.04391v1 | https://arxiv.org/html/2607.04391v1#S3.SS1 through #S3.SS6 :: preserve immutable source evidence, build revisable relational metadata and semantic overlays, profile queries before deterministic SQL retrieval, and log retrieval/reformulation lifecycle | https://arxiv.org/html/2607.04391v1#S4 and #S4.SS4 :: experience report for one long-running single-user corpus; deployment statistics establish feasibility but no controlled retrieval comparison | https://arxiv.org/html/2607.04391v1#S4.SS4, #S5.SS5 and #S6 :: no multi-tenant isolation, poisoning test, multimodal completeness, comparative retrieval quality, reproducible benchmark or public artifact | Not Disclosed — v1 provides architecture and deployment statistics but no public repository, commit, release or reproducible benchmark artifact | claim:SF-2026-ARXIV-2607-04391 | complete |
| SF-2026-ARXIV-2607-04395 | RP-c50c7628c6b16c66 | standard | arXiv:2607.04395v1 | SRC-ARXIV@arXiv:2607.04395v1 | https://arxiv.org/html/2607.04395v1#S3.SS1 through #S3.SS4 :: model proposes NKI kernels, compiles with bounded timeout, executes random-input comparisons against a PyTorch reference and iterates for up to ten tool turns; SFT traces are compiler/execution filtered | https://arxiv.org/html/2607.04395v1#S4 and #S5.SS1 through #S5.SS2 :: NKIGen-Bench main/ablation evaluation on AWS Trainium; SFT and GRPO compared with named proprietary models; single runs without error bars and no kernel-runtime speed benchmark | https://arxiv.org/html/2607.04395v1#S6 and #S5.SS1 through #S5.SS2 :: SDK-specific, sparse binary reward can collapse group ranking signal, no public dataset/training trace/artifact, inference precision and runtime performance Not Disclosed | Not Disclosed — v1 cites official NKI samples but provides no public NKI-Agent repository, NKIGen-Bench snapshot, training trace, commit or release | claim:SF-2026-ARXIV-2607-04395 | complete |
| SF-2026-ARXIV-2607-04517 | RP-0b0710824ed07659 | closure | doi:10.48550/arxiv.2607.04517@v1 | SRC-DATACITE@doi:10.48550/arxiv.2607.04517@v1 | doi:10.48550/arxiv.2607.04517#identity; DataCite Submitted:v1 timestamp | Not Required — closure route makes no mechanism or benchmark claim | Not Required — DataCite abstract is Discovery / Metadata and no technical claim is retained | Not Required — closure route; no artifact claim retained | claim:SF-2026-ARXIV-2607-04517 | complete |
| SF-2026-ARXIV-2607-04591 | RP-40d813250b9df09d | closure | doi:10.48550/arxiv.2607.04591@v1 | SRC-DATACITE@doi:10.48550/arxiv.2607.04591@v1 | doi:10.48550/arxiv.2607.04591#identity; DataCite Submitted:v1 timestamp | Not Required — closure route makes no mechanism or benchmark claim | Not Required — DataCite abstract is Discovery / Metadata and no technical claim is retained | Not Required — closure route; no artifact claim retained | claim:SF-2026-ARXIV-2607-04591 | complete |
| SF-2026-ARXIV-2607-04609 | RP-39c736fc50a91dc4 | closure | doi:10.48550/arxiv.2607.04609@v1 | SRC-DATACITE@doi:10.48550/arxiv.2607.04609@v1 | doi:10.48550/arxiv.2607.04609#identity; DataCite Submitted:v1 timestamp | Not Required — closure route makes no mechanism or benchmark claim | Not Required — DataCite abstract is Discovery / Metadata and no technical claim is retained | Not Required — closure route; no artifact claim retained | claim:SF-2026-ARXIV-2607-04609 | complete |
| SF-2026-ARXIV-2607-04637 | RP-2e83f8b28268230f | closure | doi:10.48550/arxiv.2607.04637@v1 | SRC-DATACITE@doi:10.48550/arxiv.2607.04637@v1 | doi:10.48550/arxiv.2607.04637#identity; DataCite Submitted:v1 timestamp | Not Required — closure route makes no mechanism or benchmark claim | Not Required — DataCite abstract is Discovery / Metadata and no technical claim is retained | Not Required — closure route; no artifact claim retained | claim:SF-2026-ARXIV-2607-04637 | complete |
| SF-2026-ARXIV-2607-04668 | RP-37cc3d8df06ef4c3 | deep | arXiv:2607.04668v1 | SRC-ARXIV@arXiv:2607.04668v1 | https://arxiv.org/html/2607.04668v1#S3.SS1; https://arxiv.org/html/2607.04668v1#S3.SS2; https://arxiv.org/html/2607.04668v1#S3.SS3; https://arxiv.org/html/2607.04668v1#S3.SS4; https://arxiv.org/html/2607.04668v1#S3.SS5; https://arxiv.org/html/2607.04668v1#S3.SS6 — gang state, ACK-latched epoch, generation-tagged participant latch, lend/migrate/return, ownership and invariants; https://arxiv.org/html/2607.04668v1#S4.SS1; https://arxiv.org/html/2607.04668v1#S4.SS2; https://arxiv.org/html/2607.04668v1#S4.SS3 — kernel integration, row partition/work stealing and syscall/control path | https://arxiv.org/html/2607.04668v1#S5.SS1; https://arxiv.org/html/2607.04668v1#S5.SS2; https://arxiv.org/html/2607.04668v1#S5.SS3; https://arxiv.org/html/2607.04668v1#S5.SS4; https://arxiv.org/html/2607.04668v1#S5.SS5; https://arxiv.org/html/2607.04668v1#S5.SS6; https://arxiv.org/html/2607.04668v1#S5.SS7; https://arxiv.org/html/2607.04668v1#S5.SS8 — hardware/model contract, static-policy ablation, saturation knee, bit-exact churn, latency/migration and governance sweeps | https://arxiv.org/html/2607.04668v1#S7 — one Zen 5 host, SMT confound, directional Linux comparison, pinned-process worst case and limited governance scope | https://arxiv.org/html/2607.04668v1#S8 and https://github.com/coconut-os/coconutOS — manuscript identifies boot-log/parsing artifacts and the author OS repository, but an event-time commit containing every paper scenario is Not Disclosed; artifact is not used to validate headline numbers | claim:SF-2026-ARXIV-2607-04668 | complete |
| SF-2026-ARXIV-2607-04681 | RP-31fa09b3abbfff53 | closure | doi:10.48550/arxiv.2607.04681@v1 | SRC-DATACITE@doi:10.48550/arxiv.2607.04681@v1 | doi:10.48550/arxiv.2607.04681#identity; DataCite Submitted:v1 timestamp | Not Required — closure route makes no mechanism or benchmark claim | Not Required — DataCite abstract is Discovery / Metadata and no technical claim is retained | Not Required — closure route; no artifact claim retained | claim:SF-2026-ARXIV-2607-04681 | complete |
| SF-2026-ARXIV-2607-04763 | RP-409b1db5a4929d36 | deep | arXiv:2607.04763v1 | SRC-ARXIV@arXiv:2607.04763v1 | https://arxiv.org/html/2607.04763v1#S3 — two-sided distribution shift and prefix trap; https://arxiv.org/html/2607.04763v1#S4 — replayed teacher prefixes, student action at selected step, teacher token-distribution target and step-decaying sampling | https://arxiv.org/html/2607.04763v1#S5 and subsections — math/search environments, model pairs, training parity, schedule ablations and multi-environment pool | https://arxiv.org/html/2607.04763v1#S6 — pool coverage, teacher reliability and future mixed-environment/generalization limits | https://aka.ms/GeneralAI, https://baohaoliao.github.io/ReOPD/ and https://github.com/BaohaoLiao/ReOPD — official project/repository identities are corroborated by the historical W28 review; exact event-time commit is Not Disclosed in v1, so repository contents do not enlarge the manuscript claim boundary | claim:SF-2026-ARXIV-2607-04763 | complete |
| SF-2026-ARXIV-2607-04816 | RP-606bc913eb78bdbc | closure | doi:10.48550/arxiv.2607.04816@v1 | SRC-DATACITE@doi:10.48550/arxiv.2607.04816@v1 | doi:10.48550/arxiv.2607.04816#identity; DataCite Submitted:v1 timestamp | Not Required — closure route makes no mechanism or benchmark claim | Not Required — DataCite abstract is Discovery / Metadata and no technical claim is retained | Not Required — closure route; no artifact claim retained | claim:SF-2026-ARXIV-2607-04816 | complete |
| SF-2026-ARXIV-2607-04969 | RP-33142b9cc8e13ae7 | closure | doi:10.48550/arxiv.2607.04969@v1 | SRC-DATACITE@doi:10.48550/arxiv.2607.04969@v1 | doi:10.48550/arxiv.2607.04969#identity; DataCite Submitted:v1 timestamp | Not Required — closure route makes no mechanism or benchmark claim | Not Required — DataCite abstract is Discovery / Metadata and no technical claim is retained | Not Required — closure route; no artifact claim retained | claim:SF-2026-ARXIV-2607-04969 | complete |
| SF-2026-ARXIV-2607-05029 | RP-d9738e511793d354 | deep | arXiv:2607.05029v1 | SRC-ARXIV@arXiv:2607.05029v1 | https://arxiv.org/html/2607.05029v1#S2 — agent/memory threat model; https://arxiv.org/html/2607.05029v1#S3.SS1; https://arxiv.org/html/2607.05029v1#S3.SS2; https://arxiv.org/html/2607.05029v1#S3.SS3 — forged reasoning injection and amplification; https://arxiv.org/html/2607.05029v1#S4.SS1; https://arxiv.org/html/2607.05029v1#S4.SS2; https://arxiv.org/html/2607.05029v1#S4.SS3; https://arxiv.org/html/2607.05029v1#S4.SS4; https://arxiv.org/html/2607.05029v1#S4.SS5; https://arxiv.org/html/2607.05029v1#S4.SS6 — layered SENTINEL design and weighted Reasoning Guard | https://arxiv.org/html/2607.05029v1#S5.SS1; https://arxiv.org/html/2607.05029v1#S5.SS2; https://arxiv.org/html/2607.05029v1#S5.SS3; https://arxiv.org/html/2607.05029v1#S5.SS4; https://arxiv.org/html/2607.05029v1#S5.SS5 — EHRAgent/ReAct-QA/RAP, three model families, 50 trials per cell, amplification and defense ablation | https://arxiv.org/html/2607.05029v1#S6 — adaptive paraphrase bypass, single-agent/single-store scope, simulated environments and absent real EHR/production validation | Not Disclosed — v1 provides no public FARMA/SENTINEL repository, commit, prompts, poisoned memory corpus or reproduction package | claim:SF-2026-ARXIV-2607-05029 | complete |
| SF-2026-ARXIV-2607-05061 | RP-7777b3352c08020a | deep | arXiv:2607.05061v1 | SRC-ARXIV@arXiv:2607.05061v1 | https://arxiv.org/html/2607.05061v1#S3.SS1; https://arxiv.org/html/2607.05061v1#S3.SS2; https://arxiv.org/html/2607.05061v1#S3.SS3 — future-attention supervision, sparse target construction, stateless/stateful scorers and delayed scoring; https://arxiv.org/html/2607.05061v1#A1; https://arxiv.org/html/2607.05061v1#A2; https://arxiv.org/html/2607.05061v1#A3; https://arxiv.org/html/2607.05061v1#A3.SS1; https://arxiv.org/html/2607.05061v1#A3.SS2; https://arxiv.org/html/2607.05061v1#A3.SS3 — boundary loss, running top-k, scorer implementations and pseudocode | https://arxiv.org/html/2607.05061v1#S4.SS1; https://arxiv.org/html/2607.05061v1#S4.SS2; https://arxiv.org/html/2607.05061v1#S4.SS3 — Qwen3 setup, quality results, delayed-scoring and eviction analyses; https://arxiv.org/html/2607.05061v1#A4; https://arxiv.org/html/2607.05061v1#A5 — extended experimental details and sensitivity | https://arxiv.org/html/2607.05061v1#S5 — dense-attention retrofit scope, limited scorer families, homogeneous per-head budget and future hybrid directions | Not Disclosed — v1 contains algorithms/pseudocode and points to an NVIDIA-hosted comparison model, but provides no public KVpop implementation repository, commit or release | claim:SF-2026-ARXIV-2607-05061 | complete |
| SF-2026-ARXIV-2607-05122 | RP-8ee0915a3438c847 | closure | doi:10.48550/arxiv.2607.05122@v1 | SRC-DATACITE@doi:10.48550/arxiv.2607.05122@v1 | doi:10.48550/arxiv.2607.05122#identity; DataCite Submitted:v1 timestamp | Not Required — closure route makes no mechanism or benchmark claim | Not Required — DataCite abstract is Discovery / Metadata and no technical claim is retained | Not Required — closure route; no artifact claim retained | claim:SF-2026-ARXIV-2607-05122 | complete |
| SF-2026-ARXIV-2607-05147 | RP-a8cec12ec5d7ee15 | deep | arXiv:2607.05147v1 | SRC-ARXIV@arXiv:2607.05147v1 | https://arxiv.org/html/2607.05147v1#S3.SS1; https://arxiv.org/html/2607.05147v1#S3.SS2; https://arxiv.org/html/2607.05147v1#S3.SS3 — semi-autoregressive drafter, confidence head, hardware-aware verify-length scheduler and training | https://arxiv.org/html/2607.05147v1#S4.SS1; https://arxiv.org/html/2607.05147v1#S4.SS2; https://arxiv.org/html/2607.05147v1#S4.SS3; https://arxiv.org/html/2607.05147v1#S5.SS1; https://arxiv.org/html/2607.05147v1#S5.SS2; https://arxiv.org/html/2607.05147v1#S5.SS3; https://arxiv.org/html/2607.05147v1#S5.SS4 — setup, quality/speed studies, component analysis and deployment observations | https://arxiv.org/html/2607.05147v1#S5; https://arxiv.org/html/2607.05147v1#S6; https://arxiv.org/html/2607.05147v1#S7 — model/hardware/traffic dependence, calibration drift and deployment-specific evidence | https://arxiv.org/html/2607.05147v1#S3.SS1; https://arxiv.org/html/2607.05147v1#S3.SS3 — the v1 manuscript supplies architecture/training details but no uniquely bound public DSpark commit. Later SGLang integration is a separate revision/event and must not be used to validate event-time production claims. | claim:SF-2026-ARXIV-2607-05147 | complete |
| SF-2026-ARXIV-2607-05391 | RP-c0c9ddac48322d4b | deep | arXiv:2607.05391v1 | SRC-ARXIV@arXiv:2607.05391v1 | https://arxiv.org/html/2607.05391v1#S3.SS1; https://arxiv.org/html/2607.05391v1#S3.SS2 — ordered score-token expectation, preference objective and probabilistic pivot selection; https://arxiv.org/html/2607.05391v1#S4.SS1; https://arxiv.org/html/2607.05391v1#S4.SS2; https://arxiv.org/html/2607.05391v1#S4.SS3 — granularity, repetition and criteria scaling | https://arxiv.org/html/2607.05391v1#S5.SS1; https://arxiv.org/html/2607.05391v1#S5.SS2; https://arxiv.org/html/2607.05391v1#S5.SS3; https://arxiv.org/html/2607.05391v1#S5.SS4 — Terminal-Bench, SWE-Bench, RoboRewardBench and MedAgentBench; https://arxiv.org/html/2607.05391v1#S6; https://arxiv.org/html/2607.05391v1#S7 — progress proxy and dense-reward RL experiments | https://arxiv.org/html/2607.05391v1#A1; https://arxiv.org/html/2607.05391v1#A2; https://arxiv.org/html/2607.05391v1#S8 — correlated verifier bias, rubric/logprob dependency, budget, reward hacking and domain/calibration limits | https://arxiv.org/html/2607.05391v1#S8 — Historical W28 review records an official code release, but v1 HTML does not expose a stable repository/commit locator. Exact event-time artifact binding is therefore Not Disclosed and the manuscript remains the claim source. | claim:SF-2026-ARXIV-2607-05391 | complete |
| SF-2026-ARXIV-2607-05394 | RP-f291a7169262dc8b | deep | arXiv:2607.05394v1 | SRC-ARXIV@arXiv:2607.05394v1 | https://arxiv.org/html/2607.05394v1#S2.SS1; https://arxiv.org/html/2607.05394v1#S2.SS2; https://arxiv.org/html/2607.05394v1#S2.SS3; https://arxiv.org/html/2607.05394v1#S2.SS4 — OPD preliminaries, teacher policy shift as implicit reward, Direct-OPD objective and adaptive KL | https://arxiv.org/html/2607.05394v1#S3.SS1; https://arxiv.org/html/2607.05394v1#S3.SS2; https://arxiv.org/html/2607.05394v1#S3.SS3 — model/task/training contract and matched baselines; https://arxiv.org/html/2607.05394v1#S4.SS1; https://arxiv.org/html/2607.05394v1#S4.SS2; https://arxiv.org/html/2607.05394v1#S4.SS3 — cross-token transfer, short-horizon effect and KL diagnostics; https://arxiv.org/html/2607.05394v1#A1; https://arxiv.org/html/2607.05394v1#A2; https://arxiv.org/html/2607.05394v1#A3 — experimental details and additional results | https://arxiv.org/html/2607.05394v1#S6 — dependence on meaningful teacher/reference improvement, student-visited support, response length and KL strength | https://bytedtsinghua-sia.github.io/Direct-OPD/ — official project page is identified by v1; a reproducible event-time code commit is Not Disclosed | claim:SF-2026-ARXIV-2607-05394 | complete |
| SF-2026-ARXIV-2607-05396 | RP-aa940a30d4bc2f2c | closure | doi:10.48550/arxiv.2607.05396@v1 | SRC-DATACITE@doi:10.48550/arxiv.2607.05396@v1 | doi:10.48550/arxiv.2607.05396#identity; DataCite Submitted:v1 timestamp | Not Required — closure route makes no mechanism or benchmark claim | Not Required — DataCite abstract is Discovery / Metadata and no technical claim is retained | Not Required — closure route; no artifact claim retained | claim:SF-2026-ARXIV-2607-05396 | complete |

### Source Reviews

<!-- review:SF-2026-ARXIV-2607-02574:start -->
#### From Tensor Buffer to Distributed Memory Hierarchy: A Survey of KV Cache Management for LLM Serving

<!-- claim:SF-2026-ARXIV-2607-02574:start -->本次只确认唯一 arXiv identity、v1 Submitted timestamp、owner Daily 与主题拒绝；DataCite abstract 不用于建立机制或 benchmark 结论。<!-- claim:SF-2026-ARXIV-2607-02574:end -->

- Identity：`arXiv:2607.02574v1`；first-public（Asia/Shanghai）：`2026-07-07`。
- Reconciliation：当前严格窗口内首次出现，无同层级 duplicate 或 revision。
- Closure rationale：标题与摘要触发系统主题路由，但当前证据只支持局部案例、调查或实现线索；在没有形成可验证的跨组件设计变化前，Design Delta / System Reach / Durability 为 `1/2/1`。
- Disposition：`Rejected — Low Durability / Out of Scope`；若未来 revision、artifact 或独立复现改变证据边界，重开真实 owner Daily。
<!-- review:SF-2026-ARXIV-2607-02574:end -->

<!-- review:SF-2026-ARXIV-2607-02577:start -->
#### Benchmarking the Benchmarks: A Validity Audit of Tool-Calling Evaluation

<!-- claim:SF-2026-ARXIV-2607-02577:start -->Tool-calling evaluation must separate typed tool/action checks, outcome state and qualitative judgment. Deterministic gates should own verifiable invariants; a restricted judge may handle residual semantic ambiguity, but only with full trace preservation, repeated-run variance, human adjudication and versioned evaluator artifacts. Neither branch is ground truth by default. 该结论只在论文公开的 workload 与 evaluation contract 内成立，不外推为通用生产结论。<!-- claim:SF-2026-ARXIV-2607-02577:end -->

**旧方案与约束变化。** `本章的核心判断是：**Evaluation System 是把目标转化为可重复证据和受控决策的系统。它必须同时版本化被评估对象、输入分布、执行环境与 scorer，并显式表达不确定性、切片和风险；工具可以保存证据，但不能替组织定义什么算成功。**`（`books/part-06-ai-infrastructure/66-evaluation-system.md#L14-L14`）旧方案在状态局部、规模较小或 SLO 宽松时继续成立；本 family 面对的新增压力由其 v1 problem statement 和 method 明确限定。

**机制、状态与代价。** Tool-calling evaluation must separate typed tool/action checks, outcome state and qualitative judgment. Deterministic gates should own verifiable invariants; a restricted judge may handle residual semantic ambiguity, but only with full trace preservation, repeated-run variance, human adjudication and versioned evaluator artifacts. Neither branch is ground truth by default. 它改变 `PLATFORM-EVALUATION-SYSTEM` 下的 state/data/control contract，同时引入 metadata、校准/选择误差、额外执行或恢复责任；这些代价必须和收益在同一 workload 内计量。

**Evaluation contract。** Method：`https://arxiv.org/html/2607.02577v1#S3 :: trace-level disagreement taxonomy, reproducibility analysis, corrected evaluator and deterministic-first protocol with restricted judge fallback`；Evaluation：`https://arxiv.org/html/2607.02577v1#S4 :: author audit covers four tool-calling benchmark families, complete traces, expert adjudication and repeated judge runs; it does not establish a new model ranking`；Limitations/Counterevidence：`https://arxiv.org/html/2607.02577v1#S5 :: evidence diagnoses selected benchmark/evaluator configurations; artifact release was still pending and evaluator agreement does not prove task representativeness`。未披露字段保持 `Not Disclosed`；作者结果不跨模型、硬件、精度、长度、batch、concurrency、SLO 或 evaluator 外推。

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Evolution relation：`Direct Evolution`。
- Stable owner：`PLATFORM-EVALUATION-SYSTEM`。
- Books disposition：`Integrate`。
<!-- review:SF-2026-ARXIV-2607-02577:end -->

<!-- review:SF-2026-ARXIV-2607-02604:start -->
#### DynaWM: A Base-VLA-Guided World Foundation Model for Moving-Object Manipulation

<!-- claim:SF-2026-ARXIV-2607-02604:start -->本次只确认唯一 arXiv identity、v1 Submitted timestamp、owner Daily 与主题拒绝；DataCite abstract 不用于建立机制或 benchmark 结论。<!-- claim:SF-2026-ARXIV-2607-02604:end -->

- Identity：`arXiv:2607.02604v1`；first-public（Asia/Shanghai）：`2026-07-07`。
- Reconciliation：当前严格窗口内首次出现，无同层级 duplicate 或 revision。
- Closure rationale：标题与摘要触发系统主题路由，但当前证据只支持局部案例、调查或实现线索；在没有形成可验证的跨组件设计变化前，Design Delta / System Reach / Durability 为 `1/2/1`。
- Disposition：`Rejected — Low Durability / Out of Scope`；若未来 revision、artifact 或独立复现改变证据边界，重开真实 owner Daily。
<!-- review:SF-2026-ARXIV-2607-02604:end -->

<!-- review:SF-2026-ARXIV-2607-02686:start -->
#### ASK in the Dark: Uncertainty-Gated LLM Assistance under Partial Observability

<!-- claim:SF-2026-ARXIV-2607-02686:start -->本次只确认唯一 arXiv identity、v1 Submitted timestamp、owner Daily 与主题拒绝；DataCite abstract 不用于建立机制或 benchmark 结论。<!-- claim:SF-2026-ARXIV-2607-02686:end -->

- Identity：`arXiv:2607.02686v1`；first-public（Asia/Shanghai）：`2026-07-07`。
- Reconciliation：当前严格窗口内首次出现，无同层级 duplicate 或 revision。
- Closure rationale：标题与摘要触发系统主题路由，但当前证据只支持局部案例、调查或实现线索；在没有形成可验证的跨组件设计变化前，Design Delta / System Reach / Durability 为 `1/2/0`。
- Disposition：`Rejected — Low Durability / Out of Scope`；若未来 revision、artifact 或独立复现改变证据边界，重开真实 owner Daily。
<!-- review:SF-2026-ARXIV-2607-02686:end -->

<!-- review:SF-2026-ARXIV-2607-02840:start -->
#### TACO: TActile World Model as a Self-COrrector forScalable VLA Post-Training

<!-- claim:SF-2026-ARXIV-2607-02840:start -->本次只确认唯一 arXiv identity、v1 Submitted timestamp、owner Daily 与主题拒绝；DataCite abstract 不用于建立机制或 benchmark 结论。<!-- claim:SF-2026-ARXIV-2607-02840:end -->

- Identity：`arXiv:2607.02840v1`；first-public（Asia/Shanghai）：`2026-07-07`。
- Reconciliation：当前严格窗口内首次出现，无同层级 duplicate 或 revision。
- Closure rationale：标题与摘要触发系统主题路由，但当前证据只支持局部案例、调查或实现线索；在没有形成可验证的跨组件设计变化前，Design Delta / System Reach / Durability 为 `1/2/0`。
- Disposition：`Rejected — Low Durability / Out of Scope`；若未来 revision、artifact 或独立复现改变证据边界，重开真实 owner Daily。
<!-- review:SF-2026-ARXIV-2607-02840:end -->

<!-- review:SF-2026-ARXIV-2607-02865:start -->
#### DREAMSTEER: Latent World Models Can Steer VLA Policies During Deployment Without Any Finetuning

<!-- claim:SF-2026-ARXIV-2607-02865:start -->本次只确认唯一 arXiv identity、v1 Submitted timestamp、owner Daily 与主题拒绝；DataCite abstract 不用于建立机制或 benchmark 结论。<!-- claim:SF-2026-ARXIV-2607-02865:end -->

- Identity：`arXiv:2607.02865v1`；first-public（Asia/Shanghai）：`2026-07-07`。
- Reconciliation：当前严格窗口内首次出现，无同层级 duplicate 或 revision。
- Closure rationale：标题与摘要触发系统主题路由，但当前证据只支持局部案例、调查或实现线索；在没有形成可验证的跨组件设计变化前，Design Delta / System Reach / Durability 为 `1/1/1`。
- Disposition：`Rejected — Low Durability / Out of Scope`；若未来 revision、artifact 或独立复现改变证据边界，重开真实 owner Daily。
<!-- review:SF-2026-ARXIV-2607-02865:end -->

<!-- review:SF-2026-ARXIV-2607-02882:start -->
#### Diagnosis-Driven Automatic Repair for Agentic Workflow via Symbolic Inference

<!-- claim:SF-2026-ARXIV-2607-02882:start -->本次只确认唯一 arXiv identity、v1 Submitted timestamp、owner Daily 与主题拒绝；DataCite abstract 不用于建立机制或 benchmark 结论。<!-- claim:SF-2026-ARXIV-2607-02882:end -->

- Identity：`arXiv:2607.02882v1`；first-public（Asia/Shanghai）：`2026-07-07`。
- Reconciliation：当前严格窗口内首次出现，无同层级 duplicate 或 revision。
- Closure rationale：标题与摘要触发系统主题路由，但当前证据只支持局部案例、调查或实现线索；在没有形成可验证的跨组件设计变化前，Design Delta / System Reach / Durability 为 `1/2/0`。
- Disposition：`Rejected — Low Durability / Out of Scope`；若未来 revision、artifact 或独立复现改变证据边界，重开真实 owner Daily。
<!-- review:SF-2026-ARXIV-2607-02882:end -->

<!-- review:SF-2026-ARXIV-2607-02980:start -->
#### Hierarchical Sparse Attention Done Right: Toward Infinite Context Modeling

<!-- claim:SF-2026-ARXIV-2607-02980:start -->Teacher-distilled selection keeps dense attention as semantic owner; a coexisting branch can put an approximate chunk-mass selector directly into hierarchical forward attention so next-token loss trains selection. This improves ownership alignment but adds landmark/query calibration, position-rule coupling, selector misses, union overfetch, continued-training cost and specialized sparse kernels; it remains an approximation rather than exact full attention. 该结论只在论文公开的 workload 与 evaluation contract 内成立，不外推为通用生产结论。<!-- claim:SF-2026-ARXIV-2607-02980:end -->

**旧方案与约束变化。** `Native sparse attention already couples selector training, block/GQA granularity and kernels, while teacher-owned stop-gradient warm-up provides an auditable migration path from dense checkpoints.`（`books/part-02-model/22-long-context.md#L194-L228`）旧方案在状态局部、规模较小或 SLO 宽松时继续成立；本 family 面对的新增压力由其 v1 problem statement 和 method 明确限定。

**机制、状态与代价。** Teacher-distilled selection keeps dense attention as semantic owner; a coexisting branch can put an approximate chunk-mass selector directly into hierarchical forward attention so next-token loss trains selection. This improves ownership alignment but adds landmark/query calibration, position-rule coupling, selector misses, union overfetch, continued-training cost and specialized sparse kernels; it remains an approximation rather than exact full attention. 它改变 `MODEL-LONG-CONTEXT` 下的 state/data/control contract，同时引入 metadata、校准/选择误差、额外执行或恢复责任；这些代价必须和收益在同一 workload 内计量。

**Evaluation contract。** Method：`https://arxiv.org/html/2607.02980v1#S2.SS2 :: mean/max pooled chunk summaries cannot uniformly approximate query-dependent LogSumExp chunk mass; https://arxiv.org/html/2607.02980v1#S3 :: affine first-order chunk-mass surrogate and hierarchical inter-/intra-chunk normalization place retrieval scores in the forward path; https://arxiv.org/html/2607.02980v1#S4.SS1 through #S4.SS3 :: landmark/query calibration, HoPE/GQA variants, adjacent-query packing and checkpoint migration; https://arxiv.org/html/2607.02980v1#A1 and #A2 :: derivation and proof details`；Evaluation：`https://arxiv.org/html/2607.02980v1#S5.SS1 through #S5.SS3 :: 345M 8K/256K training, dense/sparse baselines, PPL, modified RULER/NIAH and ablations; https://arxiv.org/html/2607.02980v1#S6.SS1 and #S6.SS2 :: 1.4B from-scratch and OLMo3-7B conversion studies; https://arxiv.org/html/2607.02980v1#S7.SS1 and #S7.SS2 :: single-H800 SGLang/Triton inference and adjacent-query overlap; https://arxiv.org/html/2607.02980v1#A4 through #A8 :: recipes and evaluator details`；Limitations/Counterevidence：`https://arxiv.org/html/2607.02980v1#S4.SS1 and #S5.SS3 :: position encoding, query calibration and landmark choices materially affect extrapolation, and the calibration mechanism is not fully understood; https://arxiv.org/html/2607.02980v1#S6.SS2 :: 7B migration cost and short/general-task trade-offs remain recipe-bound; https://arxiv.org/html/2607.02980v1#S7.SS1 :: latency uses one H800, batch 1 and matched Triton kernels, with full attention faster below the reported crossover; Not Disclosed — no production concurrency/arrival/SLO study or independent replication`；本次 RP 重新绑定历史 full-read coverage：`papers/2026/weekly/2026-W27/README.md#L540-L549`，其中具名记录了 Method、Evaluation 与 Boundary。未披露字段保持 `Not Disclosed`；作者结果不跨模型、硬件、精度、长度、batch、concurrency、SLO 或 evaluator 外推。

- Score V2：Design Delta 3 / System Reach 2 / Durability 3 = **8/9**。
- Evolution relation：`Alternative Branch`。
- Stable owner：`MODEL-LONG-CONTEXT`。
- Books disposition：`Integrate`。
<!-- review:SF-2026-ARXIV-2607-02980:end -->

<!-- review:SF-2026-ARXIV-2607-03146:start -->
#### Exp2VLA: Enabling Vision-Language-Action for Drone Navigation from Expert Demonstrations

<!-- claim:SF-2026-ARXIV-2607-03146:start -->本次只确认唯一 arXiv identity、v1 Submitted timestamp、owner Daily 与主题拒绝；DataCite abstract 不用于建立机制或 benchmark 结论。<!-- claim:SF-2026-ARXIV-2607-03146:end -->

- Identity：`arXiv:2607.03146v1`；first-public（Asia/Shanghai）：`2026-07-07`。
- Reconciliation：当前严格窗口内首次出现，无同层级 duplicate 或 revision。
- Closure rationale：标题与摘要触发系统主题路由，但当前证据只支持局部案例、调查或实现线索；在没有形成可验证的跨组件设计变化前，Design Delta / System Reach / Durability 为 `1/2/0`。
- Disposition：`Rejected — Low Durability / Out of Scope`；若未来 revision、artifact 或独立复现改变证据边界，重开真实 owner Daily。
<!-- review:SF-2026-ARXIV-2607-03146:end -->

<!-- review:SF-2026-ARXIV-2607-03182:start -->
#### AnchorVLA: Bridging Discrete Decisions and Continuous Trajectories for Vision-Language-Action Planning

<!-- claim:SF-2026-ARXIV-2607-03182:start -->本次只确认唯一 arXiv identity、v1 Submitted timestamp、owner Daily 与主题拒绝；DataCite abstract 不用于建立机制或 benchmark 结论。<!-- claim:SF-2026-ARXIV-2607-03182:end -->

- Identity：`arXiv:2607.03182v1`；first-public（Asia/Shanghai）：`2026-07-07`。
- Reconciliation：当前严格窗口内首次出现，无同层级 duplicate 或 revision。
- Closure rationale：标题与摘要触发系统主题路由，但当前证据只支持局部案例、调查或实现线索；在没有形成可验证的跨组件设计变化前，Design Delta / System Reach / Durability 为 `1/1/1`。
- Disposition：`Rejected — Low Durability / Out of Scope`；若未来 revision、artifact 或独立复现改变证据边界，重开真实 owner Daily。
<!-- review:SF-2026-ARXIV-2607-03182:end -->

<!-- review:SF-2026-ARXIV-2607-03333:start -->
#### SPORK: Self-Speculative Forking to Accelerate Agentic LLM Inference

<!-- claim:SF-2026-ARXIV-2607-03333:start -->Token speculation can be layered with read-only action speculation: fork the main model from shared prefix KV, confidence-gate an early tool probe, execute only read-only calls, and admit the observation only after exact final action match. The main action retains commit authority; mismatches use serial fallback, while verified rejected-prefix tokens may be reused as ordinary draft. This spends probe compute and read traffic and adds calibration, cancellation and side-effect boundaries. 该结论只在论文公开的 workload 与 evaluation contract 内成立，不外推为通用生产结论。<!-- claim:SF-2026-ARXIV-2607-03333:end -->

**旧方案与约束变化。** `Speculation is provisional work whose target/verifier owns commit; Agent phase hints may change proposal budgets but cannot change target authority, while tool authorization and side-effect classes remain outside the model.`（`books/part-05-inference-system/48-speculative-decoding.md#L489-L503`）旧方案在状态局部、规模较小或 SLO 宽松时继续成立；本 family 面对的新增压力由其 v1 problem statement 和 method 明确限定。

**机制、状态与代价。** Token speculation can be layered with read-only action speculation: fork the main model from shared prefix KV, confidence-gate an early tool probe, execute only read-only calls, and admit the observation only after exact final action match. The main action retains commit authority; mismatches use serial fallback, while verified rejected-prefix tokens may be reused as ordinary draft. This spends probe compute and read traffic and adds calibration, cancellation and side-effect boundaries. 它改变 `INFER-SPECULATIVE-DECODING` 下的 state/data/control contract，同时引入 metadata、校准/选择误差、额外执行或恢复责任；这些代价必须和收益在同一 workload 内计量。

**Evaluation contract。** Method：`https://arxiv.org/html/2607.03333v1#S2.SS2 :: overlap cost model and break-even condition; https://arxiv.org/html/2607.03333v1#S3 through #S5 :: forced-prefix self-probe, D1 prefix-KV fork, D2 confidence gate, D3 verified-prefix reuse, strict action-match commit and read-only manifest boundary; https://arxiv.org/html/2607.03333v1#A1, #A2 and #A8 :: derivation, partial-token acceptance and late-probe supersession`；Evaluation：`https://arxiv.org/html/2607.03333v1#S6.SS1 through #S6.SS6 :: Qwen3-4B/32B and Qwen3.5-35B-A3B on H20-3e, bf16, vLLM, greedy think-mode, GAIA/HotpotQA/tau2 latency and quality, component ablations, drafter comparison and break-even sweep; https://arxiv.org/html/2607.03333v1#A3 through #A7 :: BrowseComp, serving configuration and format-divergence details`；Limitations/Counterevidence：`https://arxiv.org/html/2607.03333v1#S6.SS3 and #S6.SS6 :: real-network nondeterminism, fast tools, short/no-think decode, format divergence, probe overhead and batching can shrink or reverse benefit; https://arxiv.org/html/2607.03333v1#S8 :: only read-only tools and open serving interfaces are in scope; https://arxiv.org/html/2607.03333v1#A6 through #A8 :: format collapse, small-model boundary and cancellation/supersession; exact action match does not undo quota, privacy or external side effects`。未披露字段保持 `Not Disclosed`；作者结果不跨模型、硬件、精度、长度、batch、concurrency、SLO 或 evaluator 外推。

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Evolution relation：`Layering / Dependency`。
- Stable owner：`INFER-SPECULATIVE-DECODING`。
- Books disposition：`Integrate`。
<!-- review:SF-2026-ARXIV-2607-03333:end -->

<!-- review:SF-2026-ARXIV-2607-03449:start -->
#### HiMe: Hierarchical Embodied Memory for Long-Horizon Vision-Language-Action Control

<!-- claim:SF-2026-ARXIV-2607-03449:start -->本次只确认唯一 arXiv identity、v1 Submitted timestamp、owner Daily 与主题拒绝；DataCite abstract 不用于建立机制或 benchmark 结论。<!-- claim:SF-2026-ARXIV-2607-03449:end -->

- Identity：`arXiv:2607.03449v1`；first-public（Asia/Shanghai）：`2026-07-07`。
- Reconciliation：当前严格窗口内首次出现，无同层级 duplicate 或 revision。
- Closure rationale：标题与摘要触发系统主题路由，但当前证据只支持局部案例、调查或实现线索；在没有形成可验证的跨组件设计变化前，Design Delta / System Reach / Durability 为 `1/2/1`。
- Disposition：`Rejected — Low Durability / Out of Scope`；若未来 revision、artifact 或独立复现改变证据边界，重开真实 owner Daily。
<!-- review:SF-2026-ARXIV-2607-03449:end -->

<!-- review:SF-2026-ARXIV-2607-03461:start -->
#### WorldBagel: Uncovering the Power of Unified Multimodal Models for Vision-Language-Action-World Modeling

<!-- claim:SF-2026-ARXIV-2607-03461:start -->本次只确认唯一 arXiv identity、v1 Submitted timestamp、owner Daily 与主题拒绝；DataCite abstract 不用于建立机制或 benchmark 结论。<!-- claim:SF-2026-ARXIV-2607-03461:end -->

- Identity：`arXiv:2607.03461v1`；first-public（Asia/Shanghai）：`2026-07-07`。
- Reconciliation：当前严格窗口内首次出现，无同层级 duplicate 或 revision。
- Closure rationale：标题与摘要触发系统主题路由，但当前证据只支持局部案例、调查或实现线索；在没有形成可验证的跨组件设计变化前，Design Delta / System Reach / Durability 为 `1/2/0`。
- Disposition：`Rejected — Low Durability / Out of Scope`；若未来 revision、artifact 或独立复现改变证据边界，重开真实 owner Daily。
<!-- review:SF-2026-ARXIV-2607-03461:end -->

<!-- review:SF-2026-ARXIV-2607-03473:start -->
#### MUTE: Return-Preserving Communication Unlearning for Efficient Multi-Agent Coordination

<!-- claim:SF-2026-ARXIV-2607-03473:start -->本次只确认唯一 arXiv identity、v1 Submitted timestamp、owner Daily 与主题拒绝；DataCite abstract 不用于建立机制或 benchmark 结论。<!-- claim:SF-2026-ARXIV-2607-03473:end -->

- Identity：`arXiv:2607.03473v1`；first-public（Asia/Shanghai）：`2026-07-07`。
- Reconciliation：当前严格窗口内首次出现，无同层级 duplicate 或 revision。
- Closure rationale：标题与摘要触发系统主题路由，但当前证据只支持局部案例、调查或实现线索；在没有形成可验证的跨组件设计变化前，Design Delta / System Reach / Durability 为 `1/2/1`。
- Disposition：`Rejected — Low Durability / Out of Scope`；若未来 revision、artifact 或独立复现改变证据边界，重开真实 owner Daily。
<!-- review:SF-2026-ARXIV-2607-03473:end -->

<!-- review:SF-2026-ARXIV-2607-03693:start -->
#### CoRE-VLA: Towards Scalable and Robust Vision-Language-Action Modeling via Conditional Routing of Experts

<!-- claim:SF-2026-ARXIV-2607-03693:start -->本次只确认唯一 arXiv identity、v1 Submitted timestamp、owner Daily 与主题拒绝；DataCite abstract 不用于建立机制或 benchmark 结论。<!-- claim:SF-2026-ARXIV-2607-03693:end -->

- Identity：`arXiv:2607.03693v1`；first-public（Asia/Shanghai）：`2026-07-07`。
- Reconciliation：当前严格窗口内首次出现，无同层级 duplicate 或 revision。
- Closure rationale：标题与摘要触发系统主题路由，但当前证据只支持局部案例、调查或实现线索；在没有形成可验证的跨组件设计变化前，Design Delta / System Reach / Durability 为 `1/2/1`。
- Disposition：`Rejected — Low Durability / Out of Scope`；若未来 revision、artifact 或独立复现改变证据边界，重开真实 owner Daily。
<!-- review:SF-2026-ARXIV-2607-03693:end -->

<!-- review:SF-2026-ARXIV-2607-03751:start -->
#### Look Before You Leap: Distilling Tree Search into Action Evaluation for Frozen VLA Models

<!-- claim:SF-2026-ARXIV-2607-03751:start -->本次只确认唯一 arXiv identity、v1 Submitted timestamp、owner Daily 与主题拒绝；DataCite abstract 不用于建立机制或 benchmark 结论。<!-- claim:SF-2026-ARXIV-2607-03751:end -->

- Identity：`arXiv:2607.03751v1`；first-public（Asia/Shanghai）：`2026-07-07`。
- Reconciliation：当前严格窗口内首次出现，无同层级 duplicate 或 revision。
- Closure rationale：标题与摘要触发系统主题路由，但当前证据只支持局部案例、调查或实现线索；在没有形成可验证的跨组件设计变化前，Design Delta / System Reach / Durability 为 `1/2/1`。
- Disposition：`Rejected — Low Durability / Out of Scope`；若未来 revision、artifact 或独立复现改变证据边界，重开真实 owner Daily。
<!-- review:SF-2026-ARXIV-2607-03751:end -->

<!-- review:SF-2026-ARXIV-2607-03870:start -->
#### Evaluating LLM Uncertainty in Long-Form Generation Using Deterministic Ground Truth

<!-- claim:SF-2026-ARXIV-2607-03870:start -->本次只确认唯一 arXiv identity、v1 Submitted timestamp、owner Daily 与主题拒绝；DataCite abstract 不用于建立机制或 benchmark 结论。<!-- claim:SF-2026-ARXIV-2607-03870:end -->

- Identity：`arXiv:2607.03870v1`；first-public（Asia/Shanghai）：`2026-07-07`。
- Reconciliation：当前严格窗口内首次出现，无同层级 duplicate 或 revision。
- Closure rationale：标题与摘要触发系统主题路由，但当前证据只支持局部案例、调查或实现线索；在没有形成可验证的跨组件设计变化前，Design Delta / System Reach / Durability 为 `1/2/1`。
- Disposition：`Rejected — Low Durability / Out of Scope`；若未来 revision、artifact 或独立复现改变证据边界，重开真实 owner Daily。
<!-- review:SF-2026-ARXIV-2607-03870:end -->

<!-- review:SF-2026-ARXIV-2607-03876:start -->
#### AdaptiveSD A Stability-Aware, Runtime-Adaptive Speculative Decoding Framework with Multi-Policy Orchestration for CPU-Constrained LLM Inference

<!-- claim:SF-2026-ARXIV-2607-03876:start -->本次只确认唯一 arXiv identity、v1 Submitted timestamp、owner Daily 与主题拒绝；DataCite abstract 不用于建立机制或 benchmark 结论。<!-- claim:SF-2026-ARXIV-2607-03876:end -->

- Identity：`arXiv:2607.03876v1`；first-public（Asia/Shanghai）：`2026-07-07`。
- Reconciliation：当前严格窗口内首次出现，无同层级 duplicate 或 revision。
- Closure rationale：标题与摘要触发系统主题路由，但当前证据只支持局部案例、调查或实现线索；在没有形成可验证的跨组件设计变化前，Design Delta / System Reach / Durability 为 `1/2/1`。
- Disposition：`Rejected — Low Durability / Out of Scope`；若未来 revision、artifact 或独立复现改变证据边界，重开真实 owner Daily。
<!-- review:SF-2026-ARXIV-2607-03876:end -->

<!-- review:SF-2026-ARXIV-2607-03948:start -->
#### Online Linear Programming for Multi-Objective Routing in LLM Serving

<!-- claim:SF-2026-ARXIV-2607-03948:start -->When output length is heterogeneous and KV grows over time, a queue snapshot cannot express the opportunity cost of admitting a request across future batch and memory capacity. An online controller can compare SLO-weighted benefit with time-indexed batch/KV shadow prices and update those prices from residual capacity plus historical predicted action columns. This makes cross-time commitment explicit but adds a separate production responsibility: output-length calibration must compare predicted with realized service without being misrepresented as the paper's price-update mechanism. 该结论只在论文公开的 workload 与 evaluation contract 内成立，不外推为通用生产结论。<!-- claim:SF-2026-ARXIV-2607-03948:end -->

**旧方案与约束变化。** `Ch56 already separates admission, iteration scheduling, routing/placement and autoscaling and requires future-KV feasibility, goodput, calibration and fairness, but did not yet make future batch/KV scarcity an explicit per-request opportunity cost.`（`books/part-05-inference-system/56-inference-scheduling.md#L43-L90`）旧方案在状态局部、规模较小或 SLO 宽松时继续成立；本 family 面对的新增压力由其 v1 problem statement 和 method 明确限定。

**机制、状态与代价。** When output length is heterogeneous and KV grows over time, a queue snapshot cannot express the opportunity cost of admitting a request across future batch and memory capacity. An online controller can compare SLO-weighted benefit with time-indexed batch/KV shadow prices and update those prices from residual capacity plus historical predicted action columns. This makes cross-time commitment explicit but adds a separate production responsibility: output-length calibration must compare predicted with realized service without being misrepresented as the paper's price-update mechanism. 它改变 `INFER-SCHEDULING` 下的 state/data/control contract，同时引入 metadata、校准/选择误差、额外执行或恢复责任；这些代价必须和收益在同一 workload 内计量。

**Evaluation contract。** Method：`https://arxiv.org/html/2607.03948v1#S2.SS0.SSS0.Px2, #S2.SS0.SSS0.Px5 and #S2.SS0.SSS0.Px6 :: central buffering, release-when-startable admission and time-coupled batch/KV occupancy; https://arxiv.org/html/2607.03948v1#S3.SS1 through #S3.SS3 :: SLO-weighted action reward, online LP constraints, dual shadow prices, SAA history and projected subgradient updates; https://arxiv.org/html/2607.03948v1#A2.SS1 and #A2.SS3 :: pseudocode`；Evaluation：`https://arxiv.org/html/2607.03948v1#S4.SS1 :: Vidur-only simulation on four A100 GPUs with LMSYS-Chat-1M and synthetic P/D-ratio workloads; model, precision, batch/concurrency and exact serving SLO Not Disclosed; https://arxiv.org/html/2607.03948v1#S4.SS2 and #S4.SS3 :: RR/LOR/Random/Power-of-2 baselines, noisy length estimates, objective sweeps and an arrival-rate shift; https://arxiv.org/html/2607.03948v1#A3 :: broader sweeps and tail-weight sensitivity`；Limitations/Counterevidence：`https://arxiv.org/html/2607.03948v1#S6 :: simulation-only, without serving-engine integration, preemption, KV swapping, distributed coordination, heterogeneous priorities or fairness validation; https://arxiv.org/html/2607.03948v1#A1.SS0.SSS0.Px9 :: PD-mixing duration is input-dependent; no LLM-specific theorem/regret/convergence or component ablation. Event-time artifact only partially corresponds to the manuscript noisy-length/tail-objective interface.`。未披露字段保持 `Not Disclosed`；作者结果不跨模型、硬件、精度、长度、batch、concurrency、SLO 或 evaluator 外推。

- Score V2：Design Delta 2 / System Reach 2 / Durability 3 = **7/9**。
- Evolution relation：`Direct Evolution`。
- Stable owner：`INFER-SCHEDULING`。
- Books disposition：`Integrate`。
<!-- review:SF-2026-ARXIV-2607-03948:end -->

<!-- review:SF-2026-ARXIV-2607-03964:start -->
#### Worldscape-MoE: A Unified Mixture-of-Experts World Model for Scalable Heterogeneous Action Control

<!-- claim:SF-2026-ARXIV-2607-03964:start -->本次只确认唯一 arXiv identity、v1 Submitted timestamp、owner Daily 与主题拒绝；DataCite abstract 不用于建立机制或 benchmark 结论。<!-- claim:SF-2026-ARXIV-2607-03964:end -->

- Identity：`arXiv:2607.03964v1`；first-public（Asia/Shanghai）：`2026-07-07`。
- Reconciliation：当前严格窗口内首次出现，无同层级 duplicate 或 revision。
- Closure rationale：标题与摘要触发系统主题路由，但当前证据只支持局部案例、调查或实现线索；在没有形成可验证的跨组件设计变化前，Design Delta / System Reach / Durability 为 `1/2/0`。
- Disposition：`Rejected — Low Durability / Out of Scope`；若未来 revision、artifact 或独立复现改变证据边界，重开真实 owner Daily。
<!-- review:SF-2026-ARXIV-2607-03964:end -->

<!-- review:SF-2026-ARXIV-2607-04171:start -->
#### Teaching Tiny VLA Models Where to Look and How to Move

<!-- claim:SF-2026-ARXIV-2607-04171:start -->本次只确认唯一 arXiv identity、v1 Submitted timestamp、owner Daily 与主题拒绝；DataCite abstract 不用于建立机制或 benchmark 结论。<!-- claim:SF-2026-ARXIV-2607-04171:end -->

- Identity：`arXiv:2607.04171v1`；first-public（Asia/Shanghai）：`2026-07-07`。
- Reconciliation：当前严格窗口内首次出现，无同层级 duplicate 或 revision。
- Closure rationale：标题与摘要触发系统主题路由，但当前证据只支持局部案例、调查或实现线索；在没有形成可验证的跨组件设计变化前，Design Delta / System Reach / Durability 为 `1/2/0`。
- Disposition：`Rejected — Low Durability / Out of Scope`；若未来 revision、artifact 或独立复现改变证据边界，重开真实 owner Daily。
<!-- review:SF-2026-ARXIV-2607-04171:end -->

<!-- review:SF-2026-ARXIV-2607-04181:start -->
#### CoCoScale: Leveraging Layer-wise Scaling to Unlock the Potential of Online LLM Serving

<!-- claim:SF-2026-ARXIV-2607-04181:start -->A full model replica is not the only elastic unit. A controller can choose replication counts for consecutive Transformer layer segments; the scheduler scatters sub-batches across those replicas, gathers boundary activations and redistributes affected KV partitions during a configuration transition. This reduces whole-instance startup pressure on the evaluated topology but turns activation boundaries, KV ownership and transition coordination into correctness-critical scheduling state. The v1 manuscript does not define atomic configuration publication, route-version semantics or a state-transfer-plus-SLO commit protocol. 该结论只在论文公开的 workload 与 evaluation contract 内成立，不外推为通用生产结论。<!-- claim:SF-2026-ARXIV-2607-04181:end -->

**旧方案与约束变化。** `Ch56 already evolves replica-level scaling toward stage and operator-DAG elasticity and requires profile, topology, state and failure-aware scheduling.`（`books/part-05-inference-system/56-inference-scheduling.md#L229`）旧方案在状态局部、规模较小或 SLO 宽松时继续成立；本 family 面对的新增压力由其 v1 problem statement 和 method 明确限定。

**机制、状态与代价。** A full model replica is not the only elastic unit. A controller can choose replication counts for consecutive Transformer layer segments; the scheduler scatters sub-batches across those replicas, gathers boundary activations and redistributes affected KV partitions during a configuration transition. This reduces whole-instance startup pressure on the evaluated topology but turns activation boundaries, KV ownership and transition coordination into correctness-critical scheduling state. The v1 manuscript does not define atomic configuration publication, route-version semantics or a state-transfer-plus-SLO commit protocol. 它改变 `INFER-SCHEDULING` 下的 state/data/control contract，同时引入 metadata、校准/选择误差、额外执行或恢复责任；这些代价必须和收益在同一 workload 内计量。

**Evaluation contract。** Method：`https://arxiv.org/html/2607.04181v1#S3.SS1 through #S3.SS1.p4.1 :: feasible layer-replication configuration, request scatter/gather across consecutive layer segments and partitioned KV redistribution during configuration transition; https://arxiv.org/html/2607.04181v1#S3.SS2.p1.1 through #S3.SS2.p3.1 :: bidirectional chunked ring multicast for weights and fine-grained KV transfer overlapped with inter-token intervals; https://arxiv.org/html/2607.04181v1#S4.E1 through #S4.E10 and #S4.SS4 :: configuration search and migration cost model`；Evaluation：`https://arxiv.org/html/2607.04181v1#S4.SS1 and #S6.SS1 through #S6.SS3 :: Nano-vLLM-based prototype on four NVLink-connected H20 GPUs, Qwen3 8B/14B/32B, Alibaba/Azure trace replays and LongBench prompts; compares static vLLM and a threshold autoscaler using average/P99 latency and SLO attainment`；Limitations/Counterevidence：`https://arxiv.org/html/2607.04181v1#S4.SS2 and #S6.SS3 :: analytical ranking assumes homogeneous devices and divisible layer placements; no PCIe/Ethernet fabric, heterogeneous failure recovery, arbitrary graph, public artifact or production-fleet validation`。未披露字段保持 `Not Disclosed`；作者结果不跨模型、硬件、精度、长度、batch、concurrency、SLO 或 evaluator 外推。

- Score V2：Design Delta 3 / System Reach 3 / Durability 2 = **8/9**。
- Evolution relation：`Direct Evolution`。
- Stable owner：`INFER-SCHEDULING`。
- Books disposition：`Integrate`。
<!-- review:SF-2026-ARXIV-2607-04181:end -->

<!-- review:SF-2026-ARXIV-2607-04292:start -->
#### Agentic SABRE: An Uncertainty-Aware Neuro-Symbolic Multi-Agent Framework for Adaptive Ransomware Detection

<!-- claim:SF-2026-ARXIV-2607-04292:start -->本次只确认唯一 arXiv identity、v1 Submitted timestamp、owner Daily 与主题拒绝；DataCite abstract 不用于建立机制或 benchmark 结论。<!-- claim:SF-2026-ARXIV-2607-04292:end -->

- Identity：`arXiv:2607.04292v1`；first-public（Asia/Shanghai）：`2026-07-07`。
- Reconciliation：当前严格窗口内首次出现，无同层级 duplicate 或 revision。
- Closure rationale：标题与摘要触发系统主题路由，但当前证据只支持局部案例、调查或实现线索；在没有形成可验证的跨组件设计变化前，Design Delta / System Reach / Durability 为 `1/2/1`。
- Disposition：`Rejected — Low Durability / Out of Scope`；若未来 revision、artifact 或独立复现改变证据边界，重开真实 owner Daily。
<!-- review:SF-2026-ARXIV-2607-04292:end -->

<!-- review:SF-2026-ARXIV-2607-04302:start -->
#### HiFA4: Training-Free 4-bit FlashAttention on Ascend HIF4 NPUs for LLM Inference

<!-- claim:SF-2026-ARXIV-2607-04302:start -->Attention quantization should first diagnose asymmetric Q/K structure. When calibration confirms the K-outlier regime, a paired diagonal transform can scale Q and inversely scale K while preserving the unquantized attention score; a quantized-P reordering can then make the softmax numerator and denominator consume the same quantized tensor. The equality does not preserve the final quantized output, and the reordering removes one coherent error component rather than proving all Q/K/V error harmless. 该结论只在论文公开的 workload 与 evaluation contract 内成立，不外推为通用生产结论。<!-- claim:SF-2026-ARXIV-2607-04302:end -->

**旧方案与约束变化。** `Ch49 already explains that lower bit width does not automatically accelerate attention and that distribution handling, calibration, fusion and runtime execution must be co-designed.`（`books/part-05-inference-system/49-tensorrt-llm.md#L263`）旧方案在状态局部、规模较小或 SLO 宽松时继续成立；本 family 面对的新增压力由其 v1 problem statement 和 method 明确限定。

**机制、状态与代价。** Attention quantization should first diagnose asymmetric Q/K structure. When calibration confirms the K-outlier regime, a paired diagonal transform can scale Q and inversely scale K while preserving the unquantized attention score; a quantized-P reordering can then make the softmax numerator and denominator consume the same quantized tensor. The equality does not preserve the final quantized output, and the reordering removes one coherent error component rather than proving all Q/K/V error harmless. 它改变 `INFER-TENSORRT-LLM` 下的 state/data/control contract，同时引入 metadata、校准/选择误差、额外执行或恢复责任；这些代价必须和收益在同一 workload 内计量。

**Evaluation contract。** Method：`https://arxiv.org/html/2607.04302v1#S4.SS1 through #S4.SS4 and #S4.E1 through #S4.E3 :: diagnose parameter-induced K-channel outliers after QK-RMSNorm, apply diagonal post-RoPE Q scaling with inverse K scaling, and gate static calibration; https://arxiv.org/html/2607.04302v1#S4.SS5 and #Thmtheorem1 :: reorder quantized P so numerator and denominator share the same tensor, fuse normalization into PV, and delimit the coherent-error result to fixed V`；Evaluation：`https://arxiv.org/html/2607.04302v1#S5, #S5.SS4 and #S6.T7 :: zero-shot option-likelihood and attention-error diagnostics across Qwen3-8B, Gemma2-9B, Llama3.1-8B, Mistral-7B and Phi-4B plus one Qwen3 long-context retrieval case; https://arxiv.org/html/2607.04302v1#A2.SS0.SSS0.Px1 through #A2.SS0.SSS0.Px7 :: scoring, prompt, dtype, calibration, hook, software/hardware and determinism settings`；Limitations/Counterevidence：`https://arxiv.org/html/2607.04302v1#S7.SS0.SSS0.Px3 and #Thmtheorem1 :: all latency numbers are theoretical instruction-scheduling estimates, target hardware was not available for direct validation, and the theorem holds V fixed; applicability also depends on the calibrated outlier regime, while gate thresholds are tested on five models only and the promised implementation artifact is absent`。未披露字段保持 `Not Disclosed`；作者结果不跨模型、硬件、精度、长度、batch、concurrency、SLO 或 evaluator 外推。

- Score V2：Design Delta 3 / System Reach 2 / Durability 3 = **8/9**。
- Evolution relation：`Direct Evolution`。
- Stable owner：`INFER-TENSORRT-LLM`。
- Books disposition：`Integrate`。
<!-- review:SF-2026-ARXIV-2607-04302:end -->

<!-- review:SF-2026-ARXIV-2607-04391:start -->
#### Memory-Orchestrated Semantic System (MOSS): An Auditable Agentic Memory Architecture

<!-- claim:SF-2026-ARXIV-2607-04391:start -->The immutable source corpus remains evidence truth while relational metadata, semantic overlays and query profiles are revisable derived views. This is a concrete operational instance of the existing archive-versus-derived-memory contract, not a new canonical mechanism. 该结论只在论文公开的 workload 与 evaluation contract 内成立，不外推为通用生产结论。<!-- claim:SF-2026-ARXIV-2607-04391:end -->

**旧方案与约束变化。** `Ch77 already separates compact control state from exact evidence archive and requires provenance, authorization, correction and auditability; Ch76 owns retrieval and Ch78 owns tool execution.`（`books/part-07-agent/77-memory.md#L1`）旧方案在状态局部、规模较小或 SLO 宽松时继续成立；本 family 面对的新增压力由其 v1 problem statement 和 method 明确限定。

**机制、状态与代价。** The immutable source corpus remains evidence truth while relational metadata, semantic overlays and query profiles are revisable derived views. This is a concrete operational instance of the existing archive-versus-derived-memory contract, not a new canonical mechanism. 它改变 `AGENT-MEMORY` 下的 state/data/control contract，同时引入 metadata、校准/选择误差、额外执行或恢复责任；这些代价必须和收益在同一 workload 内计量。

**Evaluation contract。** Method：`https://arxiv.org/html/2607.04391v1#S3.SS1 through #S3.SS6 :: preserve immutable source evidence, build revisable relational metadata and semantic overlays, profile queries before deterministic SQL retrieval, and log retrieval/reformulation lifecycle`；Evaluation：`https://arxiv.org/html/2607.04391v1#S4 and #S4.SS4 :: experience report for one long-running single-user corpus; deployment statistics establish feasibility but no controlled retrieval comparison`；Limitations/Counterevidence：`https://arxiv.org/html/2607.04391v1#S4.SS4, #S5.SS5 and #S6 :: no multi-tenant isolation, poisoning test, multimodal completeness, comparative retrieval quality, reproducible benchmark or public artifact`。未披露字段保持 `Not Disclosed`；作者结果不跨模型、硬件、精度、长度、batch、concurrency、SLO 或 evaluator 外推。

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Evolution relation：`Principle Reuse`。
- Stable owner：`AGENT-MEMORY`。
- Books disposition：`No Change — Existing Coverage`。
<!-- review:SF-2026-ARXIV-2607-04391:end -->

<!-- review:SF-2026-ARXIV-2607-04395:start -->
#### NKI-Agent: Domain-Specific Fine-Tuning and Agentic Tool Use for Neuron Kernel Generation

<!-- claim:SF-2026-ARXIV-2607-04395:start -->An executable compiler and numerical reference can own kernel admission even when the model proposes candidates, but that binary verifier can be a weak group-relative learning signal when every candidate in a group fails together. This bounded accelerator case connects existing execution, RL and tool-authority principles without changing their canonical owners. 该结论只在论文公开的 workload 与 evaluation contract 内成立，不外推为通用生产结论。<!-- claim:SF-2026-ARXIV-2607-04395:end -->

**旧方案与约束变化。** `Ch49 already treats learned kernel generation as candidate production while compiler/correctness checks own admission; Ch33 owns sparse group-relative reward failure and Ch78 owns typed execution authority.`（`books/part-05-inference-system/49-tensorrt-llm.md#L437-L458`）旧方案在状态局部、规模较小或 SLO 宽松时继续成立；本 family 面对的新增压力由其 v1 problem statement 和 method 明确限定。

**机制、状态与代价。** An executable compiler and numerical reference can own kernel admission even when the model proposes candidates, but that binary verifier can be a weak group-relative learning signal when every candidate in a group fails together. This bounded accelerator case connects existing execution, RL and tool-authority principles without changing their canonical owners. 它改变 `INFER-TENSORRT-LLM` 下的 state/data/control contract，同时引入 metadata、校准/选择误差、额外执行或恢复责任；这些代价必须和收益在同一 workload 内计量。

**Evaluation contract。** Method：`https://arxiv.org/html/2607.04395v1#S3.SS1 through #S3.SS4 :: model proposes NKI kernels, compiles with bounded timeout, executes random-input comparisons against a PyTorch reference and iterates for up to ten tool turns; SFT traces are compiler/execution filtered`；Evaluation：`https://arxiv.org/html/2607.04395v1#S4 and #S5.SS1 through #S5.SS2 :: NKIGen-Bench main/ablation evaluation on AWS Trainium; SFT and GRPO compared with named proprietary models; single runs without error bars and no kernel-runtime speed benchmark`；Limitations/Counterevidence：`https://arxiv.org/html/2607.04395v1#S6 and #S5.SS1 through #S5.SS2 :: SDK-specific, sparse binary reward can collapse group ranking signal, no public dataset/training trace/artifact, inference precision and runtime performance Not Disclosed`。未披露字段保持 `Not Disclosed`；作者结果不跨模型、硬件、精度、长度、batch、concurrency、SLO 或 evaluator 外推。

- Score V2：Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- Evolution relation：`Principle Reuse`。
- Stable owner：`INFER-TENSORRT-LLM`。
- Books disposition：`No Change — Existing Coverage`。
<!-- review:SF-2026-ARXIV-2607-04395:end -->

<!-- review:SF-2026-ARXIV-2607-04517:start -->
#### VLA Grounder: Language-Conditioning Space Optimization for Black-Box VLA Models

<!-- claim:SF-2026-ARXIV-2607-04517:start -->本次只确认唯一 arXiv identity、v1 Submitted timestamp、owner Daily 与主题拒绝；DataCite abstract 不用于建立机制或 benchmark 结论。<!-- claim:SF-2026-ARXIV-2607-04517:end -->

- Identity：`arXiv:2607.04517v1`；first-public（Asia/Shanghai）：`2026-07-07`。
- Reconciliation：当前严格窗口内首次出现，无同层级 duplicate 或 revision。
- Closure rationale：标题与摘要触发系统主题路由，但当前证据只支持局部案例、调查或实现线索；在没有形成可验证的跨组件设计变化前，Design Delta / System Reach / Durability 为 `1/1/0`。
- Disposition：`Rejected — Low Durability / Out of Scope`；若未来 revision、artifact 或独立复现改变证据边界，重开真实 owner Daily。
<!-- review:SF-2026-ARXIV-2607-04517:end -->

<!-- review:SF-2026-ARXIV-2607-04591:start -->
#### Simple-to-Complex Structured Demonstrations for Vision-Language-Action Learning

<!-- claim:SF-2026-ARXIV-2607-04591:start -->本次只确认唯一 arXiv identity、v1 Submitted timestamp、owner Daily 与主题拒绝；DataCite abstract 不用于建立机制或 benchmark 结论。<!-- claim:SF-2026-ARXIV-2607-04591:end -->

- Identity：`arXiv:2607.04591v1`；first-public（Asia/Shanghai）：`2026-07-07`。
- Reconciliation：当前严格窗口内首次出现，无同层级 duplicate 或 revision。
- Closure rationale：标题与摘要触发系统主题路由，但当前证据只支持局部案例、调查或实现线索；在没有形成可验证的跨组件设计变化前，Design Delta / System Reach / Durability 为 `1/2/1`。
- Disposition：`Rejected — Low Durability / Out of Scope`；若未来 revision、artifact 或独立复现改变证据边界，重开真实 owner Daily。
<!-- review:SF-2026-ARXIV-2607-04591:end -->

<!-- review:SF-2026-ARXIV-2607-04609:start -->
#### SEAM: Smooth Execution of Action-Chunked Motion for Vision-Language-Action Policies

<!-- claim:SF-2026-ARXIV-2607-04609:start -->本次只确认唯一 arXiv identity、v1 Submitted timestamp、owner Daily 与主题拒绝；DataCite abstract 不用于建立机制或 benchmark 结论。<!-- claim:SF-2026-ARXIV-2607-04609:end -->

- Identity：`arXiv:2607.04609v1`；first-public（Asia/Shanghai）：`2026-07-07`。
- Reconciliation：当前严格窗口内首次出现，无同层级 duplicate 或 revision。
- Closure rationale：标题与摘要触发系统主题路由，但当前证据只支持局部案例、调查或实现线索；在没有形成可验证的跨组件设计变化前，Design Delta / System Reach / Durability 为 `1/2/1`。
- Disposition：`Rejected — Low Durability / Out of Scope`；若未来 revision、artifact 或独立复现改变证据边界，重开真实 owner Daily。
<!-- review:SF-2026-ARXIV-2607-04609:end -->

<!-- review:SF-2026-ARXIV-2607-04637:start -->
#### PixelPilot: Scalable Vision-Language-Action Models for End-to-End Autonomous Driving

<!-- claim:SF-2026-ARXIV-2607-04637:start -->本次只确认唯一 arXiv identity、v1 Submitted timestamp、owner Daily 与主题拒绝；DataCite abstract 不用于建立机制或 benchmark 结论。<!-- claim:SF-2026-ARXIV-2607-04637:end -->

- Identity：`arXiv:2607.04637v1`；first-public（Asia/Shanghai）：`2026-07-07`。
- Reconciliation：当前严格窗口内首次出现，无同层级 duplicate 或 revision。
- Closure rationale：标题与摘要触发系统主题路由，但当前证据只支持局部案例、调查或实现线索；在没有形成可验证的跨组件设计变化前，Design Delta / System Reach / Durability 为 `1/2/0`。
- Disposition：`Rejected — Low Durability / Out of Scope`；若未来 revision、artifact 或独立复现改变证据边界，重开真实 owner Daily。
<!-- review:SF-2026-ARXIV-2607-04637:end -->

<!-- review:SF-2026-ARXIV-2607-04668:start -->
#### Elastic Gang: Per-Token Membership Change for a Hard-Barriered LLM Inference Gang Co-Scheduled with OS Processes

<!-- claim:SF-2026-ARXIV-2607-04668:start -->A generation increments a global epoch; a core joins only after parking its tenant and ACKing that epoch. Each token snapshots requested intersect current-ACKed cores into one generation-tagged participant latch, and barriers wait on the latched count rather than named cores. A core that misses the latch is outside the token, while row work stealing absorbs the missing share. Owner CAS plus idempotent teardown keeps failure paths from leaving a live gang. Scheduler owns requested membership and tenant migration; each core owns its epoch ACK; the generation latch owns the immutable per-token participant set; the inference engine owns row assignment and token commit. Control changes occur only at generation/token boundaries, while model rows and partial sums remain on the token data path. 该结论只在论文公开的 workload 与 evaluation contract 内成立，不外推为通用生产结论。<!-- claim:SF-2026-ARXIV-2607-04668:end -->

**旧方案与约束变化。** `Ch56 already owns barrier-synchronized worker sets, scheduling-state transitions and work-conserving resource control, but does not yet distinguish requested membership from acknowledged token membership.`（`books/part-05-inference-system/56-inference-scheduling.md#L305-L335`）旧方案在状态局部、规模较小或 SLO 宽松时继续成立；本 family 面对的新增压力由其 v1 problem statement 和 method 明确限定。

**机制、状态与代价。** A generation increments a global epoch; a core joins only after parking its tenant and ACKing that epoch. Each token snapshots requested intersect current-ACKed cores into one generation-tagged participant latch, and barriers wait on the latched count rather than named cores. A core that misses the latch is outside the token, while row work stealing absorbs the missing share. Owner CAS plus idempotent teardown keeps failure paths from leaving a live gang. Scheduler owns requested membership and tenant migration; each core owns its epoch ACK; the generation latch owns the immutable per-token participant set; the inference engine owns row assignment and token commit. Control changes occur only at generation/token boundaries, while model rows and partial sums remain on the token data path. 它改变 `INFER-SCHEDULING` 下的 state/data/control contract，同时引入 metadata、校准/选择误差、额外执行或恢复责任；这些代价必须和收益在同一 workload 内计量。

**Evaluation contract。** Method：`https://arxiv.org/html/2607.04668v1#S3.SS1; https://arxiv.org/html/2607.04668v1#S3.SS2; https://arxiv.org/html/2607.04668v1#S3.SS3; https://arxiv.org/html/2607.04668v1#S3.SS4; https://arxiv.org/html/2607.04668v1#S3.SS5; https://arxiv.org/html/2607.04668v1#S3.SS6 — gang state, ACK-latched epoch, generation-tagged participant latch, lend/migrate/return, ownership and invariants; https://arxiv.org/html/2607.04668v1#S4.SS1; https://arxiv.org/html/2607.04668v1#S4.SS2; https://arxiv.org/html/2607.04668v1#S4.SS3 — kernel integration, row partition/work stealing and syscall/control path`；Evaluation：`https://arxiv.org/html/2607.04668v1#S5.SS1; https://arxiv.org/html/2607.04668v1#S5.SS2; https://arxiv.org/html/2607.04668v1#S5.SS3; https://arxiv.org/html/2607.04668v1#S5.SS4; https://arxiv.org/html/2607.04668v1#S5.SS5; https://arxiv.org/html/2607.04668v1#S5.SS6; https://arxiv.org/html/2607.04668v1#S5.SS7; https://arxiv.org/html/2607.04668v1#S5.SS8 — hardware/model contract, static-policy ablation, saturation knee, bit-exact churn, latency/migration and governance sweeps`；Limitations/Counterevidence：`https://arxiv.org/html/2607.04668v1#S7 — one Zen 5 host, SMT confound, directional Linux comparison, pinned-process worst case and limited governance scope`。未披露字段保持 `Not Disclosed`；作者结果不跨模型、硬件、精度、长度、batch、concurrency、SLO 或 evaluator 外推。

- Score V2：Design Delta 3 / System Reach 2 / Durability 3 = **8/9**。
- Evolution relation：`Direct Evolution`。
- Stable owner：`INFER-SCHEDULING`。
- Books disposition：`Integrate`。
<!-- review:SF-2026-ARXIV-2607-04668:end -->

<!-- review:SF-2026-ARXIV-2607-04681:start -->
#### Do Vision-Language-Action Models Mean What They Say? On the Role of Faithfulness in Embodied Reasoning

<!-- claim:SF-2026-ARXIV-2607-04681:start -->本次只确认唯一 arXiv identity、v1 Submitted timestamp、owner Daily 与主题拒绝；DataCite abstract 不用于建立机制或 benchmark 结论。<!-- claim:SF-2026-ARXIV-2607-04681:end -->

- Identity：`arXiv:2607.04681v1`；first-public（Asia/Shanghai）：`2026-07-07`。
- Reconciliation：当前严格窗口内首次出现，无同层级 duplicate 或 revision。
- Closure rationale：标题与摘要触发系统主题路由，但当前证据只支持局部案例、调查或实现线索；在没有形成可验证的跨组件设计变化前，Design Delta / System Reach / Durability 为 `0/2/1`。
- Disposition：`Rejected — Low Durability / Out of Scope`；若未来 revision、artifact 或独立复现改变证据边界，重开真实 owner Daily。
<!-- review:SF-2026-ARXIV-2607-04681:end -->

<!-- review:SF-2026-ARXIV-2607-04763:start -->
#### Multi-Turn On-Policy Distillation with Prefix Replay

<!-- claim:SF-2026-ARXIV-2607-04763:start -->The teacher's recorded multi-turn history and observations are replayed as a prefix; the student generates the action only at the supervised step, and the teacher supplies dense conditional token targets at that student action. A step-decaying prefix sampler reduces exposure to late histories where teacher-forced state and student occupancy diverge. This trades live environment interaction for a reliability-aware replay distribution. The trajectory store owns immutable teacher prefix/observation provenance; the sampler owns which step becomes supervision; the student owns the current action distribution; the teacher owns the conditional target; no environment side effect is executed during student training. Replay freshness and environment version remain external debts. 该结论只在论文公开的 workload 与 evaluation contract 内成立，不外推为通用生产结论。<!-- claim:SF-2026-ARXIV-2607-04763:end -->

**旧方案与约束变化。** `Ch29 already contains the full prefix-replay evolution chain, the two-sided distribution-shift debt, the teacher/environment provenance boundary and the conditions under which live OPD or ordinary offline SFT remains preferable.`（`books/part-04-training-system/29-sft.md#L255-L281`）旧方案在状态局部、规模较小或 SLO 宽松时继续成立；本 family 面对的新增压力由其 v1 problem statement 和 method 明确限定。

**机制、状态与代价。** The teacher's recorded multi-turn history and observations are replayed as a prefix; the student generates the action only at the supervised step, and the teacher supplies dense conditional token targets at that student action. A step-decaying prefix sampler reduces exposure to late histories where teacher-forced state and student occupancy diverge. This trades live environment interaction for a reliability-aware replay distribution. The trajectory store owns immutable teacher prefix/observation provenance; the sampler owns which step becomes supervision; the student owns the current action distribution; the teacher owns the conditional target; no environment side effect is executed during student training. Replay freshness and environment version remain external debts. 它改变 `TRAIN-SFT` 下的 state/data/control contract，同时引入 metadata、校准/选择误差、额外执行或恢复责任；这些代价必须和收益在同一 workload 内计量。

**Evaluation contract。** Method：`https://arxiv.org/html/2607.04763v1#S3 — two-sided distribution shift and prefix trap; https://arxiv.org/html/2607.04763v1#S4 — replayed teacher prefixes, student action at selected step, teacher token-distribution target and step-decaying sampling`；Evaluation：`https://arxiv.org/html/2607.04763v1#S5 and subsections — math/search environments, model pairs, training parity, schedule ablations and multi-environment pool`；Limitations/Counterevidence：`https://arxiv.org/html/2607.04763v1#S6 — pool coverage, teacher reliability and future mixed-environment/generalization limits`；本次 RP 重新绑定历史 full-read coverage：`papers/2026/weekly/2026-W28/README.md#L506-L544`，其中具名记录了 Method、Evaluation 与 Boundary。未披露字段保持 `Not Disclosed`；作者结果不跨模型、硬件、精度、长度、batch、concurrency、SLO 或 evaluator 外推。

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Evolution relation：`Alternative Branch`。
- Stable owner：`TRAIN-SFT`。
- Books disposition：`No Change — Existing Coverage`。
<!-- review:SF-2026-ARXIV-2607-04763:end -->

<!-- review:SF-2026-ARXIV-2607-04816:start -->
#### CAC-VLA: Context-Gated Action Conditioning for Vision-Language-Action Models

<!-- claim:SF-2026-ARXIV-2607-04816:start -->本次只确认唯一 arXiv identity、v1 Submitted timestamp、owner Daily 与主题拒绝；DataCite abstract 不用于建立机制或 benchmark 结论。<!-- claim:SF-2026-ARXIV-2607-04816:end -->

- Identity：`arXiv:2607.04816v1`；first-public（Asia/Shanghai）：`2026-07-07`。
- Reconciliation：当前严格窗口内首次出现，无同层级 duplicate 或 revision。
- Closure rationale：标题与摘要触发系统主题路由，但当前证据只支持局部案例、调查或实现线索；在没有形成可验证的跨组件设计变化前，Design Delta / System Reach / Durability 为 `1/1/0`。
- Disposition：`Rejected — Low Durability / Out of Scope`；若未来 revision、artifact 或独立复现改变证据边界，重开真实 owner Daily。
<!-- review:SF-2026-ARXIV-2607-04816:end -->

<!-- review:SF-2026-ARXIV-2607-04969:start -->
#### Train Smarter, Not Longer: Memorization-Guided Data Reuse for Efficient LLM Training

<!-- claim:SF-2026-ARXIV-2607-04969:start -->本次只确认唯一 arXiv identity、v1 Submitted timestamp、owner Daily 与主题拒绝；DataCite abstract 不用于建立机制或 benchmark 结论。<!-- claim:SF-2026-ARXIV-2607-04969:end -->

- Identity：`arXiv:2607.04969v1`；first-public（Asia/Shanghai）：`2026-07-07`。
- Reconciliation：当前严格窗口内首次出现，无同层级 duplicate 或 revision。
- Closure rationale：标题与摘要触发系统主题路由，但当前证据只支持局部案例、调查或实现线索；在没有形成可验证的跨组件设计变化前，Design Delta / System Reach / Durability 为 `1/2/1`。
- Disposition：`Rejected — Low Durability / Out of Scope`；若未来 revision、artifact 或独立复现改变证据边界，重开真实 owner Daily。
<!-- review:SF-2026-ARXIV-2607-04969:end -->

<!-- review:SF-2026-ARXIV-2607-05029:start -->
#### Your Agent's Memories Are Not Its Own: Forged Reasoning Attacks on LLM Agent Memory and Defenses

<!-- claim:SF-2026-ARXIV-2607-05029:start -->The v1 demonstrates forged-reasoning entries that persist through agent memory, amplify through repeated retrieval/consensus, and can evade or defeat tested defenses; SENTINEL reduces attacks in the author experiments but remains vulnerable to adaptive paraphrase and is not a complete memory-security proof. 该结论只在论文公开的 workload 与 evaluation contract 内成立，不外推为通用生产结论。<!-- claim:SF-2026-ARXIV-2607-05029:end -->

**旧方案与约束变化。** `Ch72 already protects Agent instruction/config/memory and Ch77 already rejects provenance-correlated majority as independent evidence; neither explicitly freezes remembered completion claims below authoritative effect receipts.`（`books/part-06-ai-infrastructure/72-security.md#L416-L435`）旧方案在状态局部、规模较小或 SLO 宽松时继续成立；本 family 面对的新增压力由其 v1 problem statement 和 method 明确限定。

**机制、状态与代价。** An attacker writes persistent memory entries that imitate a trusted reasoning trace and claim a safety check or prerequisite was already completed. Repetition creates correlated descendants, so majority/consensus logic may count one forged origin as apparently repeated support. SENTINEL layers lexical, provenance/taint, risk-pattern and reasoning checks, but its own ablation makes the Reasoning Guard load-bearing and the limitations show adaptive paraphrase can evade it. Project inference for the durable system contract: the memory store owns untrusted persisted claims and provenance; a security policy owns taint/risk routing; only the authoritative tool/environment/effect receipt can own whether an action actually completed. Read-time voting should collapse descendants sharing one provenance family before counting evidence. 它改变 `PLATFORM-SECURITY` 下的 state/data/control contract，同时引入 metadata、校准/选择误差、额外执行或恢复责任；这些代价必须和收益在同一 workload 内计量。

**Evaluation contract。** Method：`https://arxiv.org/html/2607.05029v1#S2 — agent/memory threat model; https://arxiv.org/html/2607.05029v1#S3.SS1; https://arxiv.org/html/2607.05029v1#S3.SS2; https://arxiv.org/html/2607.05029v1#S3.SS3 — forged reasoning injection and amplification; https://arxiv.org/html/2607.05029v1#S4.SS1; https://arxiv.org/html/2607.05029v1#S4.SS2; https://arxiv.org/html/2607.05029v1#S4.SS3; https://arxiv.org/html/2607.05029v1#S4.SS4; https://arxiv.org/html/2607.05029v1#S4.SS5; https://arxiv.org/html/2607.05029v1#S4.SS6 — layered SENTINEL design and weighted Reasoning Guard`；Evaluation：`https://arxiv.org/html/2607.05029v1#S5.SS1; https://arxiv.org/html/2607.05029v1#S5.SS2; https://arxiv.org/html/2607.05029v1#S5.SS3; https://arxiv.org/html/2607.05029v1#S5.SS4; https://arxiv.org/html/2607.05029v1#S5.SS5 — EHRAgent/ReAct-QA/RAP, three model families, 50 trials per cell, amplification and defense ablation`；Limitations/Counterevidence：`https://arxiv.org/html/2607.05029v1#S6 — adaptive paraphrase bypass, single-agent/single-store scope, simulated environments and absent real EHR/production validation`。未披露字段保持 `Not Disclosed`；作者结果不跨模型、硬件、精度、长度、batch、concurrency、SLO 或 evaluator 外推。

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Evolution relation：`Direct Evolution`。
- Stable owner：`PLATFORM-SECURITY`。
- Books disposition：`Integrate`。
<!-- review:SF-2026-ARXIV-2607-05029:end -->

<!-- review:SF-2026-ARXIV-2607-05061:start -->
#### KVpop -- Key-Value Cache Compression with Predictive Online Pruning

<!-- claim:SF-2026-ARXIV-2607-05061:start -->Future attention mass after a protected window becomes the retention target. A boundary-focused loss trains a lightweight stateless or recurrent scorer; scoring may be delayed until the eviction boundary to expose near-future context. Runtime retains a fixed top-k budget per head, separating learned importance prediction from regular memory allocation. The target-construction path uses future attention only during training; the online scorer owns a per-token priority estimate; the cache manager owns the hard capacity and top-k commit; the model's true future attention is unavailable at eviction time. Delayed scoring trades memory residency for a better observation window. 该结论只在论文公开的 workload 与 evaluation contract 内成立，不外推为通用生产结论。<!-- claim:SF-2026-ARXIV-2607-05061:end -->

**旧方案与约束变化。** `Ch45 already contains the oracle-to-learned-eviction evolution, future-access target, stateful/stateless scorer, delayed-scoring trade-off, fixed-budget runtime boundary and KVpop evidence limits.`（`books/part-05-inference-system/45-why-kv-cache-speeds-up.md#L306-L359`）旧方案在状态局部、规模较小或 SLO 宽松时继续成立；本 family 面对的新增压力由其 v1 problem statement 和 method 明确限定。

**机制、状态与代价。** Future attention mass after a protected window becomes the retention target. A boundary-focused loss trains a lightweight stateless or recurrent scorer; scoring may be delayed until the eviction boundary to expose near-future context. Runtime retains a fixed top-k budget per head, separating learned importance prediction from regular memory allocation. The target-construction path uses future attention only during training; the online scorer owns a per-token priority estimate; the cache manager owns the hard capacity and top-k commit; the model's true future attention is unavailable at eviction time. Delayed scoring trades memory residency for a better observation window. 它改变 `INFER-KV-CACHE` 下的 state/data/control contract，同时引入 metadata、校准/选择误差、额外执行或恢复责任；这些代价必须和收益在同一 workload 内计量。

**Evaluation contract。** Method：`https://arxiv.org/html/2607.05061v1#S3.SS1; https://arxiv.org/html/2607.05061v1#S3.SS2; https://arxiv.org/html/2607.05061v1#S3.SS3 — future-attention supervision, sparse target construction, stateless/stateful scorers and delayed scoring; https://arxiv.org/html/2607.05061v1#A1; https://arxiv.org/html/2607.05061v1#A2; https://arxiv.org/html/2607.05061v1#A3; https://arxiv.org/html/2607.05061v1#A3.SS1; https://arxiv.org/html/2607.05061v1#A3.SS2; https://arxiv.org/html/2607.05061v1#A3.SS3 — boundary loss, running top-k, scorer implementations and pseudocode`；Evaluation：`https://arxiv.org/html/2607.05061v1#S4.SS1; https://arxiv.org/html/2607.05061v1#S4.SS2; https://arxiv.org/html/2607.05061v1#S4.SS3 — Qwen3 setup, quality results, delayed-scoring and eviction analyses; https://arxiv.org/html/2607.05061v1#A4; https://arxiv.org/html/2607.05061v1#A5 — extended experimental details and sensitivity`；Limitations/Counterevidence：`https://arxiv.org/html/2607.05061v1#S5 — dense-attention retrofit scope, limited scorer families, homogeneous per-head budget and future hybrid directions`；本次 RP 重新绑定历史 full-read coverage：`papers/2026/weekly/2026-W28/README.md#L593-L607`，其中具名记录了 Method、Evaluation 与 Boundary。未披露字段保持 `Not Disclosed`；作者结果不跨模型、硬件、精度、长度、batch、concurrency、SLO 或 evaluator 外推。

- Score V2：Design Delta 3 / System Reach 2 / Durability 3 = **8/9**。
- Evolution relation：`Direct Evolution`。
- Stable owner：`INFER-KV-CACHE`。
- Books disposition：`No Change — Existing Coverage`。
<!-- review:SF-2026-ARXIV-2607-05061:end -->

<!-- review:SF-2026-ARXIV-2607-05122:start -->
#### Green for Go, Red for No: Visual Grounding via Semantic Segmentation for VLA Navigation Policies

<!-- claim:SF-2026-ARXIV-2607-05122:start -->本次只确认唯一 arXiv identity、v1 Submitted timestamp、owner Daily 与主题拒绝；DataCite abstract 不用于建立机制或 benchmark 结论。<!-- claim:SF-2026-ARXIV-2607-05122:end -->

- Identity：`arXiv:2607.05122v1`；first-public（Asia/Shanghai）：`2026-07-07`。
- Reconciliation：当前严格窗口内首次出现，无同层级 duplicate 或 revision。
- Closure rationale：标题与摘要触发系统主题路由，但当前证据只支持局部案例、调查或实现线索；在没有形成可验证的跨组件设计变化前，Design Delta / System Reach / Durability 为 `1/2/1`。
- Disposition：`Rejected — Low Durability / Out of Scope`；若未来 revision、artifact 或独立复现改变证据边界，重开真实 owner Daily。
<!-- review:SF-2026-ARXIV-2607-05122:end -->

<!-- review:SF-2026-ARXIV-2607-05147:start -->
#### DSpark: Confidence-Scheduled Speculative Decoding with Semi-Autoregressive Generation

<!-- claim:SF-2026-ARXIV-2607-05147:start -->A semi-autoregressive drafter proposes multiple tokens with lightweight sequential dependency, while a confidence head predicts how far verification should extend. A hardware-aware scheduler maps confidence and target-device behavior into a variable verify window; the target model remains authoritative and rejected suffixes roll back. The drafter owns provisional tokens and confidence; scheduler owns proposal/verify length; target owns acceptance; runtime owns provisional KV, rollback and batch capacity. Confidence is an estimate, not the commit authority. 该结论只在论文公开的 workload 与 evaluation contract 内成立，不外推为通用生产结论。<!-- claim:SF-2026-ARXIV-2607-05147:end -->

**旧方案与约束变化。** `Ch48 already treats verify depth as a capacity-aware policy, separates confidence from target commit authority and preserves rollback/KV/SLO boundaries using DSpark as Experimental evidence.`（`books/part-05-inference-system/48-speculative-decoding.md#L190-L230`）旧方案在状态局部、规模较小或 SLO 宽松时继续成立；本 family 面对的新增压力由其 v1 problem statement 和 method 明确限定。

**机制、状态与代价。** A semi-autoregressive drafter proposes multiple tokens with lightweight sequential dependency, while a confidence head predicts how far verification should extend. A hardware-aware scheduler maps confidence and target-device behavior into a variable verify window; the target model remains authoritative and rejected suffixes roll back. The drafter owns provisional tokens and confidence; scheduler owns proposal/verify length; target owns acceptance; runtime owns provisional KV, rollback and batch capacity. Confidence is an estimate, not the commit authority. 它改变 `INFER-SPECULATIVE-DECODING` 下的 state/data/control contract，同时引入 metadata、校准/选择误差、额外执行或恢复责任；这些代价必须和收益在同一 workload 内计量。

**Evaluation contract。** Method：`https://arxiv.org/html/2607.05147v1#S3.SS1; https://arxiv.org/html/2607.05147v1#S3.SS2; https://arxiv.org/html/2607.05147v1#S3.SS3 — semi-autoregressive drafter, confidence head, hardware-aware verify-length scheduler and training`；Evaluation：`https://arxiv.org/html/2607.05147v1#S4.SS1; https://arxiv.org/html/2607.05147v1#S4.SS2; https://arxiv.org/html/2607.05147v1#S4.SS3; https://arxiv.org/html/2607.05147v1#S5.SS1; https://arxiv.org/html/2607.05147v1#S5.SS2; https://arxiv.org/html/2607.05147v1#S5.SS3; https://arxiv.org/html/2607.05147v1#S5.SS4 — setup, quality/speed studies, component analysis and deployment observations`；Limitations/Counterevidence：`https://arxiv.org/html/2607.05147v1#S5; https://arxiv.org/html/2607.05147v1#S6; https://arxiv.org/html/2607.05147v1#S7 — model/hardware/traffic dependence, calibration drift and deployment-specific evidence`；本次 RP 重新绑定历史 full-read coverage：`papers/2026/weekly/2026-W28/README.md#L430-L444`，其中具名记录了 Method、Evaluation 与 Boundary。未披露字段保持 `Not Disclosed`；作者结果不跨模型、硬件、精度、长度、batch、concurrency、SLO 或 evaluator 外推。

- Score V2：Design Delta 3 / System Reach 2 / Durability 3 = **8/9**。
- Evolution relation：`Direct Evolution`。
- Stable owner：`INFER-SPECULATIVE-DECODING`。
- Books disposition：`No Change — Existing Coverage`。
<!-- review:SF-2026-ARXIV-2607-05147:end -->

<!-- review:SF-2026-ARXIV-2607-05391:start -->
#### LLM-as-a-Verifier: A General-Purpose Verification Framework

<!-- claim:SF-2026-ARXIV-2607-05391:start -->A verifier converts the probability distribution over ordered score tokens into a continuous expected score, can aggregate repeated criteria/runs, and can learn pairwise preferences. Candidate selection can be reduced by probabilistic pivot tournaments, but every layer remains a fallible judgment channel whose calibration and correlation must be measured. The environment/test harness owns executable outcome; the verifier owns a probabilistic score or preference; an aggregator owns criterion/repetition combination; a selection policy owns budgeted ranking. Verifier confidence cannot overwrite environment truth. 该结论只在论文公开的 workload 与 evaluation contract 内成立，不外推为通用生产结论。<!-- claim:SF-2026-ARXIV-2607-05391:end -->

**旧方案与约束变化。** `Ch66 already separates scorer/verifier from outcome authority, covers criteria/repetition/ranking, calibration, claim graphs and trajectory evidence, including the exact correlated-confidence boundary.`（`books/part-06-ai-infrastructure/66-evaluation-system.md#L1`）旧方案在状态局部、规模较小或 SLO 宽松时继续成立；本 family 面对的新增压力由其 v1 problem statement 和 method 明确限定。

**机制、状态与代价。** A verifier converts the probability distribution over ordered score tokens into a continuous expected score, can aggregate repeated criteria/runs, and can learn pairwise preferences. Candidate selection can be reduced by probabilistic pivot tournaments, but every layer remains a fallible judgment channel whose calibration and correlation must be measured. The environment/test harness owns executable outcome; the verifier owns a probabilistic score or preference; an aggregator owns criterion/repetition combination; a selection policy owns budgeted ranking. Verifier confidence cannot overwrite environment truth. 它改变 `PLATFORM-EVALUATION-SYSTEM` 下的 state/data/control contract，同时引入 metadata、校准/选择误差、额外执行或恢复责任；这些代价必须和收益在同一 workload 内计量。

**Evaluation contract。** Method：`https://arxiv.org/html/2607.05391v1#S3.SS1; https://arxiv.org/html/2607.05391v1#S3.SS2 — ordered score-token expectation, preference objective and probabilistic pivot selection; https://arxiv.org/html/2607.05391v1#S4.SS1; https://arxiv.org/html/2607.05391v1#S4.SS2; https://arxiv.org/html/2607.05391v1#S4.SS3 — granularity, repetition and criteria scaling`；Evaluation：`https://arxiv.org/html/2607.05391v1#S5.SS1; https://arxiv.org/html/2607.05391v1#S5.SS2; https://arxiv.org/html/2607.05391v1#S5.SS3; https://arxiv.org/html/2607.05391v1#S5.SS4 — Terminal-Bench, SWE-Bench, RoboRewardBench and MedAgentBench; https://arxiv.org/html/2607.05391v1#S6; https://arxiv.org/html/2607.05391v1#S7 — progress proxy and dense-reward RL experiments`；Limitations/Counterevidence：`https://arxiv.org/html/2607.05391v1#A1; https://arxiv.org/html/2607.05391v1#A2; https://arxiv.org/html/2607.05391v1#S8 — correlated verifier bias, rubric/logprob dependency, budget, reward hacking and domain/calibration limits`；本次 RP 重新绑定历史 full-read coverage：`papers/2026/weekly/2026-W28/README.md#L474-L505`，其中具名记录了 Method、Evaluation 与 Boundary。未披露字段保持 `Not Disclosed`；作者结果不跨模型、硬件、精度、长度、batch、concurrency、SLO 或 evaluator 外推。

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Evolution relation：`Direct Evolution`。
- Stable owner：`PLATFORM-EVALUATION-SYSTEM`。
- Books disposition：`No Change — Existing Coverage`。
<!-- review:SF-2026-ARXIV-2607-05391:end -->

<!-- review:SF-2026-ARXIV-2607-05394:start -->
#### Weak-to-Strong Generalization via Direct On-Policy Distillation

<!-- claim:SF-2026-ARXIV-2607-05394:start -->Instead of imitating a weaker post-RL teacher's final policy, Direct-OPD contrasts that teacher with its own pre-RL reference. The log policy ratio becomes a dense directional reward evaluated on the stronger student's on-policy prefixes, transferring the change induced by RL rather than the weaker model's capability ceiling. Teacher/reference checkpoint identity jointly owns the policy-shift signal; the student owns sampled prefixes; token log-ratios provide dense supervision; adaptive KL owns proximity control. The method cannot create useful direction where the teacher/reference delta is irrelevant or unsupported on student states. 该结论只在论文公开的 workload 与 evaluation contract 内成立，不外推为通用生产结论。<!-- claim:SF-2026-ARXIV-2607-05394:end -->

**旧方案与约束变化。** `Ch29 already distinguishes policy-shift transfer from final-policy imitation, preserves student-on-policy prefixes, checkpoint-pair identity, support/KL/length limits and the branch's coexistence with SFT/RL.`（`books/part-04-training-system/29-sft.md#L277-L281`）旧方案在状态局部、规模较小或 SLO 宽松时继续成立；本 family 面对的新增压力由其 v1 problem statement 和 method 明确限定。

**机制、状态与代价。** Instead of imitating a weaker post-RL teacher's final policy, Direct-OPD contrasts that teacher with its own pre-RL reference. The log policy ratio becomes a dense directional reward evaluated on the stronger student's on-policy prefixes, transferring the change induced by RL rather than the weaker model's capability ceiling. Teacher/reference checkpoint identity jointly owns the policy-shift signal; the student owns sampled prefixes; token log-ratios provide dense supervision; adaptive KL owns proximity control. The method cannot create useful direction where the teacher/reference delta is irrelevant or unsupported on student states. 它改变 `TRAIN-SFT` 下的 state/data/control contract，同时引入 metadata、校准/选择误差、额外执行或恢复责任；这些代价必须和收益在同一 workload 内计量。

**Evaluation contract。** Method：`https://arxiv.org/html/2607.05394v1#S2.SS1; https://arxiv.org/html/2607.05394v1#S2.SS2; https://arxiv.org/html/2607.05394v1#S2.SS3; https://arxiv.org/html/2607.05394v1#S2.SS4 — OPD preliminaries, teacher policy shift as implicit reward, Direct-OPD objective and adaptive KL`；Evaluation：`https://arxiv.org/html/2607.05394v1#S3.SS1; https://arxiv.org/html/2607.05394v1#S3.SS2; https://arxiv.org/html/2607.05394v1#S3.SS3 — model/task/training contract and matched baselines; https://arxiv.org/html/2607.05394v1#S4.SS1; https://arxiv.org/html/2607.05394v1#S4.SS2; https://arxiv.org/html/2607.05394v1#S4.SS3 — cross-token transfer, short-horizon effect and KL diagnostics; https://arxiv.org/html/2607.05394v1#A1; https://arxiv.org/html/2607.05394v1#A2; https://arxiv.org/html/2607.05394v1#A3 — experimental details and additional results`；Limitations/Counterevidence：`https://arxiv.org/html/2607.05394v1#S6 — dependence on meaningful teacher/reference improvement, student-visited support, response length and KL strength`；本次 RP 重新绑定历史 full-read coverage：`papers/2026/weekly/2026-W28/README.md#L778-L789`，其中具名记录了 Method、Evaluation 与 Boundary。未披露字段保持 `Not Disclosed`；作者结果不跨模型、硬件、精度、长度、batch、concurrency、SLO 或 evaluator 外推。

- Score V2：Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- Evolution relation：`Alternative Branch`。
- Stable owner：`TRAIN-SFT`。
- Books disposition：`No Change — Existing Coverage`。
<!-- review:SF-2026-ARXIV-2607-05394:end -->

<!-- review:SF-2026-ARXIV-2607-05396:start -->
#### From Fixed to Free Cameras: Calibration-Free View-Robust Vision-Language-Action Model

<!-- claim:SF-2026-ARXIV-2607-05396:start -->本次只确认唯一 arXiv identity、v1 Submitted timestamp、owner Daily 与主题拒绝；DataCite abstract 不用于建立机制或 benchmark 结论。<!-- claim:SF-2026-ARXIV-2607-05396:end -->

- Identity：`arXiv:2607.05396v1`；first-public（Asia/Shanghai）：`2026-07-07`。
- Reconciliation：当前严格窗口内首次出现，无同层级 duplicate 或 revision。
- Closure rationale：标题与摘要触发系统主题路由，但当前证据只支持局部案例、调查或实现线索；在没有形成可验证的跨组件设计变化前，Design Delta / System Reach / Durability 为 `0/2/1`。
- Disposition：`Rejected — Low Durability / Out of Scope`；若未来 revision、artifact 或独立复现改变证据边界，重开真实 owner Daily。
<!-- review:SF-2026-ARXIV-2607-05396:end -->

<!-- audit-target:evidence:end -->
## 4. Benchmark Contracts

<!-- validator:benchmark-contract-v1 -->
| Source Family ID | Workload | Model | Hardware | Precision | Input Length | Output Length | Batch | Concurrency | SLO | Evaluator |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2607-02980 | 345M 8K from-scratch and 256K continued training; 1.4B/300B-token from-scratch; OLMo3-7B conversion; single-stream inference | 345M GPT-2-Medium-like; 1.4B; OLMo3-1025-7B | single NVIDIA H800 for disclosed inference; complete training topology Not Disclosed | bf16 for inference; complete training precision contract Not Disclosed | 8K/256K training; evaluation spans disclosed 512 through 4M contexts depending on study | Not Disclosed; not applicable to the prefill/PPL/retrieval runs, and generation length is not uniformly reported | batch 1 for inference; training/evaluation batch varies by recipe | single-stream inference; production concurrency Not Disclosed | No production SLO; paper reports PPL, retrieval/downstream quality, warm prefill and median per-token decode latency | paper-defined PPL, modified RULER/NIAH, downstream suites, LongBench-v1 and SGLang/Triton harness |
| SF-2026-ARXIV-2607-03333 | agentic read-only tool loops on GAIA, HotpotQA and tau2-bench; additional BrowseComp decomposition | Qwen3-4B, Qwen3-32B, Qwen3.5-35B-A3B | NVIDIA H20-3e 143 GiB; main TP=1, BrowseComp TP=4 on four GPUs | bf16 | benchmark-dependent; BrowseComp max_model_len=40960; exact per-query lengths otherwise Not Disclosed | thinking-mode decode; exact output-token distribution Not Disclosed | Not Disclosed uniformly across configurations | main and probe concurrent; BrowseComp workers=4; production arrival process Not Disclosed | No production SLO; paper reports end-to-end wall time, P50/P95/mean latency, EM/F1 and tool-latency break-even metrics | paper harness with real GAIA/HotpotQA APIs, tau2 tools and vLLM 0.19.1/0.18.1 |
| SF-2026-ARXIV-2607-03948 | Vidur simulation with LMSYS-Chat-1M and synthetic P/D-ratio workloads | Not Disclosed | 4 x NVIDIA A100 | Not Disclosed | Trace/synthetic workload dependent; exact distribution Not Disclosed | Predicted and actual decode lengths are simulated; exact distribution Not Disclosed | Simulator-managed dynamic batching; exact sizes Not Disclosed | Not Disclosed; the workload uses Poisson arrival rates lambda in {0.4, 0.5}, which are not concurrency counts | No production SLO; reports EEL, TTFT, token throughput, QPS, tail indicator and SLO-violation metrics. Appendix C.1 uses TTFT threshold t2'=49 only in the corresponding sensitivity experiment | Vidur simulator with RR, LOR, Random and Power-of-2 baselines; exact Vidur version and experiment/config commit Not Disclosed |
| SF-2026-ARXIV-2607-04181 | Four concurrent model instances replaying 60-minute Alibaba and 130-minute Azure traces with LongBench prompts; separate Alpaca ablation | Qwen3-8B, Qwen3-14B, Qwen3-32B | 4 x NVIDIA H20 connected by NVLink | Not Disclosed | Trace-run distribution Not Disclosed; separate ablation uses 1,000 input tokens | Trace-run distribution Not Disclosed; separate ablation uses 64 output tokens | Dynamic sub-batches; exact sizes Not Disclosed | Four model instances; request concurrency Not Disclosed, and reported arrival rates are not concurrency counts | 30 s for the Alibaba replay and 27 s for the Azure replay | Nano-vLLM-based prototype compared with static vLLM and a threshold autoscaler; exact prototype commit Not Disclosed |
| SF-2026-ARXIV-2607-04302 | Zero-shot option-likelihood evaluation, attention-error diagnostics and one saturated long-context retrieval test | Qwen3-8B, Gemma2-9B, Llama3.1-8B, Mistral-7B, Phi-4B | Ascend HIF4 NPU is the target; public on-hardware timing is absent | HIF4 for QK^T/PV attention paths, BF16 elsewhere, FP16 online-softmax state | Benchmark-dependent; exact serving distribution Not Disclosed | Benchmark-dependent; exact serving distribution Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed; latency statements are theoretical instruction-scheduling estimates, not measured serving SLO | Official HIF4 QDQ reference comparing BF16, direct HIF4 and HiFA4; exact evaluator commit Not Disclosed |
| SF-2026-ARXIV-2607-04395 | NKIGen-Bench: 150 balanced held-out tasks for main evaluation and 60 for ablation | Qwen3-Coder-30B-A3B base/SFT/GRPO; Claude Sonnet 4 and Opus 4.8 comparisons | AWS Trainium Trn1 for kernel execution; SFT training uses 8 x A100 40GB | SFT BF16; evaluation inference precision Not Disclosed | Not Disclosed | Not Disclosed; up to 10 agent/tool turns | Evaluation per task; training batch 4 | Not Disclosed | Compiler timeout 120 s; no runtime-latency SLO and no kernel-speed benchmark | neuronx-cc compilation plus numerical allclose against a PyTorch reference at atol=rtol=1e-3; exact SDK/evaluator commit Not Disclosed |
| SF-2026-ARXIV-2607-04668 | 24 synthetic general tenants plus 32-token inference bursts and duty-cycle sweeps; churn and microbenchmark scenarios | SmolLM2-135M Q4_0 and Qwen2.5-7B-Instruct Q4_0 | AMD Ryzen 7 9800X3D, 8 cores/16 threads, DDR5-6000 | Q4_0 | Prompt length Not Disclosed | 32 generated tokens per burst | single inference gang; batch size Not Disclosed | 24 synthetic tenant processes plus gang members | No production SLO; reports inference/general throughput, bit-exactness, acquisition/return latency and fairness-oriented sweeps | same shipped kernel binary under elastic versus fair static partition policies; Author measurements establish safety and a policy frontier only on this CPU/kernel/model contract. Scheduling quanta and throughput ratios must not be generalized to other CPUs, kernels or GPU serving. |
| SF-2026-ARXIV-2607-04763 | Python-assisted math and retrieval/search agent tasks | Qwen3 teacher/student families including 4B student and 8B teacher in the headline setup | Not Disclosed for all reported comparisons | Not Disclosed | Multi-turn trajectories; exact per-task context/output distributions Not Disclosed | Not separately disclosed; bounded by the workload/length contract | Matched between OPD and ReOPD; exact batch cardinality Not Disclosed in the retained contract | Not Disclosed | Training cost, accuracy and tool-call count; not an online-serving SLO | six math and seven QA/search benchmarks with environment-specific correctness; The paper supports a training branch under its prefix pool and teacher/environment versions, not a guarantee that replay matches arbitrary student occupancy or that late prefixes remain reliable. |
| SF-2026-ARXIV-2607-05029 | poisoned-memory agent tasks in EHRAgent, ReAct-QA and RAP | GPT-4o-mini, GPT-4o and Llama 3.3 70B | Not Disclosed | Not Disclosed | Prompt/memory lengths Not Disclosed | Not separately disclosed; bounded by the workload/length contract | 50 trials per cell | single-agent, single-store | attack success and defense effectiveness; no latency or production SLO | task-specific safety/correctness plus benign-trace false-positive study; The layered defense is not a complete security proof; adaptive attackers and production stores remain unvalidated. |
| SF-2026-ARXIV-2607-05061 | math, science/reasoning and code benchmarks under compressed KV cache | Qwen3-4B and Qwen3-8B | Not Disclosed for the complete benchmark set | Model/cache precision Not Disclosed beyond compression configuration | task and compression-ratio dependent; exact distributions Not Disclosed | Not separately disclosed; bounded by the workload/length contract | Not Disclosed | single-model evaluation; serving concurrency Not Disclosed | quality under KV budget; no TTFT/TPOT/goodput SLO | AIME/HMMT, GPQA and LiveCodeBench-style correctness plus eviction diagnostics; No vLLM/SGLang paged-cache integration, multi-tenant scheduler or production latency result is demonstrated. |
| SF-2026-ARXIV-2607-05147 | math/code/general generation plus an author-reported serving deployment | Offline: Qwen3-4B/8B/14B and Gemma4-12B cohorts; online preview: DeepSeek-V4-Flash/Pro with DSpark-5 and MTP-1 cohorts | varies by experiment; full production fleet contract Not Disclosed | Not Disclosed for all results | task dependent; live traffic distributions Not Disclosed | Not separately disclosed; bounded by the workload/length contract | dynamic; exact composition Not Disclosed | production and offline contexts differ; exact live concurrency Not Disclosed | acceptance/speed and author serving throughput; tail SLO contract Not Disclosed | task correctness and author deployment metrics; Confidence calibration and optimal verify length are device, target, batch-composition and traffic dependent. |
| SF-2026-ARXIV-2607-05391 | software engineering, terminal, robotics-reward and medical-agent verification plus RL reward use | paper-specific frontier/open verifier and policy models | Not Disclosed for all comparisons | Not Disclosed | task dependent; exact distributions Not Disclosed | Not separately disclosed; bounded by the workload/length contract | Not Disclosed | Not Disclosed | verification quality/budget and downstream RL performance; no serving SLO | four benchmark-specific outcome contracts plus learned-verifier judgments; Criterion averaging and repeated samples do not create independent evidence when errors are correlated; logprob and rubric behavior are model/domain dependent. |
| SF-2026-ARXIV-2607-05394 | mathematical reasoning with verifiable answers | weak teacher/reference pairs and Qwen3/R1-distilled stronger students described in v1 | headline includes 8 A100 GPUs; full hardware for every run Not Disclosed | Not Disclosed | response-length sensitivity studied; full distributions Not Disclosed | Not separately disclosed; bounded by the workload/length contract | Not Disclosed | training rollouts; serving concurrency not applicable | accuracy and training compute/time; no serving SLO | verifiable math benchmark answers; Transfer is conditional on teacher/reference improvement having support and meaning on student prefixes; math results do not establish general agent/task transfer. |
<!-- audit-target:deep_analysis_selection:start -->
## 5. Deep Analysis Selection

<!-- validator:deep-analysis-selection-v1 -->
| Source Family ID | Eligibility | Decision | Analysis Unit ID | Subsumed By | Priority Rationale | Narrative Ref |
| --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2607-02577 | score_7_9;potential_books_delta | selected | DA-20260701-2607-02577 | — | V2=9/9；Tool-calling evaluation must separate typed tool/action checks, outcome state and qualitative judgment. Deterministic gates should own verifiable invariants; a restricted judge may handle residual semantic ambiguity, but only with full trace preservation, repeated-run variance, human adjudication and versioned evaluator artifacts. Neither branch is ground truth by default.；相对同日候选提供独立 owner 的最大可定位 delta | analysis:DA-20260701-2607-02577 |
| SF-2026-ARXIV-2607-02980 | score_7_9;potential_books_delta | not_selected | — | — | Hierarchical Sparse Attention Done Right: Toward Infinite Context Modeling remains evidence-complete after canonical owner transfer with V2 score 8 and owner MODEL-LONG-CONTEXT. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2607-02980 |
| SF-2026-ARXIV-2607-03333 | score_7_9;potential_books_delta | selected | DA-20260704-2607-03333 | — | V2=9/9；Token speculation can be layered with read-only action speculation: fork the main model from shared prefix KV, confidence-gate an early tool probe, execute only read-only calls, and admit the observation only after exact final action match. The main action retains commit authority; mismatches use serial fallback, while verified rejected-prefix tokens may be reused as ordinary draft. This spends probe compute and read traffic and adds calibration, cancellation and side-effect boundaries.；相对同日候选提供独立 owner 的最大可定位 delta | analysis:DA-20260704-2607-03333 |
| SF-2026-ARXIV-2607-03948 | score_7_9;potential_books_delta | not_selected | — | — | Online Linear Programming for Multi-Objective Routing in LLM Serving remains evidence-complete after canonical owner transfer with V2 score 7 and owner INFER-SCHEDULING. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2607-03948 |
| SF-2026-ARXIV-2607-04181 | score_7_9;potential_books_delta | not_selected | — | — | CoCoScale: Leveraging Layer-wise Scaling to Unlock the Potential of Online LLM Serving remains evidence-complete after canonical owner transfer with V2 score 8 and owner INFER-SCHEDULING. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2607-04181 |
| SF-2026-ARXIV-2607-04302 | score_7_9;potential_books_delta | not_selected | — | — | HiFA4: Training-Free 4-bit FlashAttention on Ascend HIF4 NPUs for LLM Inference remains evidence-complete after canonical owner transfer with V2 score 8 and owner INFER-TENSORRT-LLM. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2607-04302 |
| SF-2026-ARXIV-2607-04668 | score_7_9;potential_books_delta | not_selected | — | — | Elastic Gang: Per-Token Membership Change for a Hard-Barriered LLM Inference Gang Co-Scheduled with OS Processes remains evidence-complete after canonical owner transfer with V2 score 8 and owner INFER-SCHEDULING. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2607-04668 |
| SF-2026-ARXIV-2607-04763 | score_7_9;potential_books_delta | not_selected | — | — | Multi-Turn On-Policy Distillation with Prefix Replay remains evidence-complete after canonical owner transfer with V2 score 9 and owner TRAIN-SFT. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2607-04763 |
| SF-2026-ARXIV-2607-05029 | score_7_9;potential_books_delta | selected | DA-20260707-2607-05029 | — | 命中合同第一优先级 security contract；V2=9/9；The v1 demonstrates forged-reasoning entries that persist through agent memory, amplify through repeated retrieval/consensus, and can evade or defeat tested defenses; SENTINEL reduces attacks in the author experiments but remains vulnerable to adaptive paraphrase and is not a complete memory-security proof.；相对同日候选提供独立 owner 的最大可定位 delta | analysis:DA-20260707-2607-05029 |
| SF-2026-ARXIV-2607-05061 | score_7_9;potential_books_delta | not_selected | — | — | KVpop -- Key-Value Cache Compression with Predictive Online Pruning remains evidence-complete after canonical owner transfer with V2 score 8 and owner INFER-KV-CACHE. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2607-05061 |
| SF-2026-ARXIV-2607-05147 | score_7_9;potential_books_delta | not_selected | — | — | DSpark: Confidence-Scheduled Speculative Decoding with Semi-Autoregressive Generation remains evidence-complete after canonical owner transfer with V2 score 8 and owner INFER-SPECULATIVE-DECODING. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2607-05147 |
| SF-2026-ARXIV-2607-05391 | score_7_9;potential_books_delta | not_selected | — | — | LLM-as-a-Verifier: A General-Purpose Verification Framework remains evidence-complete after canonical owner transfer with V2 score 9 and owner PLATFORM-EVALUATION-SYSTEM. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2607-05391 |
| SF-2026-ARXIV-2607-05394 | score_7_9;potential_books_delta | not_selected | — | — | Weak-to-Strong Generalization via Direct On-Policy Distillation remains evidence-complete after canonical owner transfer with V2 score 9 and owner TRAIN-SFT. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2607-05394 |

### Selected Analysis Narratives

<!-- analysis:DA-20260701-2607-02577:start -->
### Benchmarking the Benchmarks: A Validity Audit of Tool-Calling Evaluation

**旧方案为何合理。** 本章的核心判断是：**Evaluation System 是把目标转化为可重复证据和受控决策的系统。它必须同时版本化被评估对象、输入分布、执行环境与 scorer，并显式表达不确定性、切片和风险；工具可以保存证据，但不能替组织定义什么算成功。** 当状态局部、规模较小、workload 稳定或 SLO 宽松时，这一基线仍然成立。（现有命题定位：`books/part-06-ai-infrastructure/66-evaluation-system.md#L14-L14`）

**约束变化与机制。** Tool-calling evaluation must separate typed tool/action checks, outcome state and qualitative judgment. Deterministic gates should own verifiable invariants; a restricted judge may handle residual semantic ambiguity, but only with full trace preservation, repeated-run variance, human adjudication and versioned evaluator artifacts. Neither branch is ground truth by default. 这条证据与现有主线的关系是 `Direct Evolution`：它改变或补充 `PLATFORM-EVALUATION-SYSTEM` 下的 representation、state、data flow 或 control ownership，而不是用论文名称替换设计结论。

**收益、代价与下一重压力。** 新机制以额外 metadata、选择/压缩误差、计算或恢复责任换取作者 workload 内的收益；未披露的 model、hardware、precision、length、batch、concurrency、SLO 与 evaluator 不做补推。旧方案仍在新增成本高于收益时成立，下一步需要跨 workload、故障与长期状态的独立验证。

<!-- analysis:DA-20260701-2607-02577:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-02980:start -->
Hierarchical Sparse Attention Done Right: Toward Infinite Context Modeling remains evidence-complete after canonical owner transfer with V2 score 8 and owner MODEL-LONG-CONTEXT. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2607-02980:end -->

<!-- analysis:DA-20260704-2607-03333:start -->
### SPORK: Self-Speculative Forking to Accelerate Agentic LLM Inference

**旧方案为何合理。** Serial tool dispatch remains the safest branch for writes, non-idempotent actions, fast tools, short/no-think generations, closed APIs and runtimes without shared prefix KV or token logprobs.（现有命题定位：`books/part-05-inference-system/48-speculative-decoding.md#L489-L503`）

**约束变化与机制。** Token speculation can be layered with read-only action speculation: fork the main model from shared prefix KV, confidence-gate an early tool probe, execute only read-only calls, and admit the observation only after exact final action match. The main action retains commit authority; mismatches use serial fallback, while verified rejected-prefix tokens may be reused as ordinary draft. This spends probe compute and read traffic and adds calibration, cancellation and side-effect boundaries. 这条证据与现有主线的关系是 `Layering / Dependency`：它改变或补充 `INFER-SPECULATIVE-DECODING` 下的 representation、state、data flow 或 control ownership，而不是用论文名称替换设计结论。

**收益、代价与下一重压力。** SPORK overlaps only slow read-only tools with remaining reasoning and needs spare serving capacity, stable tool formatting, confidence calibration and open backend interfaces. Exact action match controls conversation commit but cannot undo quota, privacy exposure or remote reads; format divergence, heavy batching and short decode can erase the benefit. The next pressure is transactional authority for writes and multi-tenant tail-SLO accounting, neither of which v1 establishes.

<!-- analysis:DA-20260704-2607-03333:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-03948:start -->
Online Linear Programming for Multi-Objective Routing in LLM Serving remains evidence-complete after canonical owner transfer with V2 score 7 and owner INFER-SCHEDULING. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2607-03948:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-04181:start -->
CoCoScale: Leveraging Layer-wise Scaling to Unlock the Potential of Online LLM Serving remains evidence-complete after canonical owner transfer with V2 score 8 and owner INFER-SCHEDULING. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2607-04181:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-04302:start -->
HiFA4: Training-Free 4-bit FlashAttention on Ascend HIF4 NPUs for LLM Inference remains evidence-complete after canonical owner transfer with V2 score 8 and owner INFER-TENSORRT-LLM. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2607-04302:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-04668:start -->
Elastic Gang: Per-Token Membership Change for a Hard-Barriered LLM Inference Gang Co-Scheduled with OS Processes remains evidence-complete after canonical owner transfer with V2 score 8 and owner INFER-SCHEDULING. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2607-04668:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-04763:start -->
Multi-Turn On-Policy Distillation with Prefix Replay remains evidence-complete after canonical owner transfer with V2 score 9 and owner TRAIN-SFT. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2607-04763:end -->

<!-- analysis:DA-20260707-2607-05029:start -->
### Your Agent's Memories Are Not Its Own: Forged Reasoning Attacks on LLM Agent Memory and Defenses

**旧方案为何合理。** Model-written memory remains useful as advisory context, but it never becomes authoritative proof that an external effect completed.（现有命题定位：`books/part-06-ai-infrastructure/72-security.md#L416-L435`）

**约束变化与机制。** An attacker writes persistent memory entries that imitate a trusted reasoning trace and claim a safety check or prerequisite was already completed. Repetition creates correlated descendants, so majority/consensus logic may count one forged origin as apparently repeated support. SENTINEL layers lexical, provenance/taint, risk-pattern and reasoning checks, but its own ablation makes the Reasoning Guard load-bearing and the limitations show adaptive paraphrase can evade it. Project inference for the durable system contract: the memory store owns untrusted persisted claims and provenance; a security policy owns taint/risk routing; only the authoritative tool/environment/effect receipt can own whether an action actually completed. Read-time voting should collapse descendants sharing one provenance family before counting evidence. 这条证据与现有主线的关系是 `Direct Evolution`：它改变或补充 `PLATFORM-SECURITY` 下的 representation、state、data flow 或 control ownership，而不是用论文名称替换设计结论。

**收益、代价与下一重压力。** Adds lineage tracking, effect-receipt retention and read-time verification. Heuristic reasoning guards remain bypassable and are not a security proof.

<!-- analysis:DA-20260707-2607-05029:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-05061:start -->
KVpop -- Key-Value Cache Compression with Predictive Online Pruning remains evidence-complete after canonical owner transfer with V2 score 8 and owner INFER-KV-CACHE. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2607-05061:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-05147:start -->
DSpark: Confidence-Scheduled Speculative Decoding with Semi-Autoregressive Generation remains evidence-complete after canonical owner transfer with V2 score 8 and owner INFER-SPECULATIVE-DECODING. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2607-05147:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-05391:start -->
LLM-as-a-Verifier: A General-Purpose Verification Framework remains evidence-complete after canonical owner transfer with V2 score 9 and owner PLATFORM-EVALUATION-SYSTEM. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2607-05391:end -->

<!-- analysis-decision:SF-2026-ARXIV-2607-05394:start -->
Weak-to-Strong Generalization via Direct On-Policy Distillation remains evidence-complete after canonical owner transfer with V2 score 9 and owner TRAIN-SFT. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2607-05394:end -->

<!-- audit-target:deep_analysis_selection:end -->
<!-- audit-target:books:start -->
## 6. Books Comparison

<!-- validator:books-comparison-v1 -->
| Source Family ID | Stable Node ID | Target Chapter Ref | Adjacent Chapter Refs | Existing Proposition | New Evidence Delta | Evolution Relation | Decision | Books Review Ref |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2607-02577 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#L844 | books/part-06-ai-infrastructure/65-kai-scheduler.md#L14-L14; books/part-06-ai-infrastructure/67-monitoring.md#L14-L14 | existing:SF-2026-ARXIV-2607-02577 | delta:SF-2026-ARXIV-2607-02577 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2607-02577 |
| SF-2026-ARXIV-2607-02980 | MODEL-LONG-CONTEXT | books/part-02-model/22-long-context.md#L247 | books/part-02-model/21-moe.md#L1 | existing:SF-2026-ARXIV-2607-02980 | delta:SF-2026-ARXIV-2607-02980 | Alternative Branch | Integrate | books-review:SF-2026-ARXIV-2607-02980 |
| SF-2026-ARXIV-2607-03333 | INFER-SPECULATIVE-DECODING | books/part-05-inference-system/48-speculative-decoding.md#L510 | books/part-05-inference-system/47-pagedattention.md#L1 | existing:SF-2026-ARXIV-2607-03333 | delta:SF-2026-ARXIV-2607-03333 | Layering / Dependency | Integrate | books-review:SF-2026-ARXIV-2607-03333 |
| SF-2026-ARXIV-2607-03948 | INFER-SCHEDULING | books/part-05-inference-system/56-inference-scheduling.md#L97 | books/part-05-inference-system/55-pd-disaggregation.md#L1 | existing:SF-2026-ARXIV-2607-03948 | delta:SF-2026-ARXIV-2607-03948 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2607-03948 |
| SF-2026-ARXIV-2607-04181 | INFER-SCHEDULING | books/part-05-inference-system/56-inference-scheduling.md#L255 | books/part-05-inference-system/55-pd-disaggregation.md#L1 | existing:SF-2026-ARXIV-2607-04181 | delta:SF-2026-ARXIV-2607-04181 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2607-04181 |
| SF-2026-ARXIV-2607-04302 | INFER-TENSORRT-LLM | books/part-05-inference-system/49-tensorrt-llm.md#L441 | books/part-05-inference-system/48-speculative-decoding.md#L1 | existing:SF-2026-ARXIV-2607-04302 | delta:SF-2026-ARXIV-2607-04302 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2607-04302 |
| SF-2026-ARXIV-2607-04391 | AGENT-MEMORY | books/part-07-agent/77-memory.md#L1 | books/part-07-agent/76-rag.md#L1 | existing:SF-2026-ARXIV-2607-04391 | delta:SF-2026-ARXIV-2607-04391 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2607-04391 |
| SF-2026-ARXIV-2607-04395 | INFER-TENSORRT-LLM | books/part-05-inference-system/49-tensorrt-llm.md#L437-L458 | books/part-04-training-system/33-grpo.md#L1 | existing:SF-2026-ARXIV-2607-04395 | delta:SF-2026-ARXIV-2607-04395 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2607-04395 |
| SF-2026-ARXIV-2607-04668 | INFER-SCHEDULING | books/part-05-inference-system/56-inference-scheduling.md#L358 | books/part-05-inference-system/55-pd-disaggregation.md#L1 | existing:SF-2026-ARXIV-2607-04668 | delta:SF-2026-ARXIV-2607-04668 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2607-04668 |
| SF-2026-ARXIV-2607-04763 | TRAIN-SFT | books/part-04-training-system/29-sft.md#L255-L281 | books/part-04-training-system/28-pretraining.md#L1 | existing:SF-2026-ARXIV-2607-04763 | delta:SF-2026-ARXIV-2607-04763 | Alternative Branch | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2607-04763 |
| SF-2026-ARXIV-2607-05029 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#L451 | books/part-06-ai-infrastructure/71-multi-tenant.md#L1 | existing:SF-2026-ARXIV-2607-05029 | delta:SF-2026-ARXIV-2607-05029 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2607-05029 |
| SF-2026-ARXIV-2607-05061 | INFER-KV-CACHE | books/part-05-inference-system/45-why-kv-cache-speeds-up.md#L306-L359 | books/part-05-inference-system/44-decode.md#L1 | existing:SF-2026-ARXIV-2607-05061 | delta:SF-2026-ARXIV-2607-05061 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2607-05061 |
| SF-2026-ARXIV-2607-05147 | INFER-SPECULATIVE-DECODING | books/part-05-inference-system/48-speculative-decoding.md#L190-L230 | books/part-05-inference-system/47-pagedattention.md#L1 | existing:SF-2026-ARXIV-2607-05147 | delta:SF-2026-ARXIV-2607-05147 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2607-05147 |
| SF-2026-ARXIV-2607-05391 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#L1 | books/part-06-ai-infrastructure/65-kai-scheduler.md#L1 | existing:SF-2026-ARXIV-2607-05391 | delta:SF-2026-ARXIV-2607-05391 | Direct Evolution | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2607-05391 |
| SF-2026-ARXIV-2607-05394 | TRAIN-SFT | books/part-04-training-system/29-sft.md#L277-L281 | books/part-04-training-system/28-pretraining.md#L1 | existing:SF-2026-ARXIV-2607-05394 | delta:SF-2026-ARXIV-2607-05394 | Alternative Branch | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2607-05394 |

<!-- books-review:SF-2026-ARXIV-2607-02577:start --><!-- existing:SF-2026-ARXIV-2607-02577:start -->对读 `books/part-06-ai-infrastructure/66-evaluation-system.md#L844` 与相邻章节后，现有命题（`books/part-06-ai-infrastructure/66-evaluation-system.md#L14-L14`）为：本章的核心判断是：**Evaluation System 是把目标转化为可重复证据和受控决策的系统。它必须同时版本化被评估对象、输入分布、执行环境与 scorer，并显式表达不确定性、切片和风险；工具可以保存证据，但不能替组织定义什么算成功。**<!-- existing:SF-2026-ARXIV-2607-02577:end --><!-- delta:SF-2026-ARXIV-2607-02577:start -->新增证据边界：Tool-calling evaluation must separate typed tool/action checks, outcome state and qualitative judgment. Deterministic gates should own verifiable invariants; a restricted judge may handle residual semantic ambiguity, but only with full trace preservation, repeated-run variance, human adjudication and versioned evaluator artifacts. Neither branch is ground truth by default. 该 delta 已进入 `books/part-06-ai-infrastructure/66-evaluation-system.md#L844`，正文保留旧方案成立条件、约束变化、代价与下一重压力。<!-- delta:SF-2026-ARXIV-2607-02577:end --><!-- books-review:SF-2026-ARXIV-2607-02577:end -->

<!-- books-review:SF-2026-ARXIV-2607-02980:start --><!-- existing:SF-2026-ARXIV-2607-02980:start -->对读 `books/part-02-model/22-long-context.md#L247` 与相邻章节后，现有命题（`books/part-02-model/22-long-context.md#L194-L228`）为：Native sparse attention already couples selector training, block/GQA granularity and kernels, while teacher-owned stop-gradient warm-up provides an auditable migration path from dense checkpoints.<!-- existing:SF-2026-ARXIV-2607-02980:end --><!-- delta:SF-2026-ARXIV-2607-02980:start -->新增证据边界：Teacher-distilled selection keeps dense attention as semantic owner; a coexisting branch can put an approximate chunk-mass selector directly into hierarchical forward attention so next-token loss trains selection. This improves ownership alignment but adds landmark/query calibration, position-rule coupling, selector misses, union overfetch, continued-training cost and specialized sparse kernels; it remains an approximation rather than exact full attention. 该 delta 已进入 `books/part-02-model/22-long-context.md#L247`，正文保留旧方案成立条件、约束变化、代价与下一重压力。<!-- delta:SF-2026-ARXIV-2607-02980:end --><!-- books-review:SF-2026-ARXIV-2607-02980:end -->

<!-- books-review:SF-2026-ARXIV-2607-03333:start --><!-- existing:SF-2026-ARXIV-2607-03333:start -->对读 `books/part-05-inference-system/48-speculative-decoding.md#L510` 与相邻章节后，现有命题（`books/part-05-inference-system/48-speculative-decoding.md#L489-L503`）为：Speculation is provisional work whose target/verifier owns commit; Agent phase hints may change proposal budgets but cannot change target authority, while tool authorization and side-effect classes remain outside the model.<!-- existing:SF-2026-ARXIV-2607-03333:end --><!-- delta:SF-2026-ARXIV-2607-03333:start -->新增证据边界：Token speculation can be layered with read-only action speculation: fork the main model from shared prefix KV, confidence-gate an early tool probe, execute only read-only calls, and admit the observation only after exact final action match. The main action retains commit authority; mismatches use serial fallback, while verified rejected-prefix tokens may be reused as ordinary draft. This spends probe compute and read traffic and adds calibration, cancellation and side-effect boundaries. 该 delta 已进入 `books/part-05-inference-system/48-speculative-decoding.md#L510`，正文保留旧方案成立条件、约束变化、代价与下一重压力。<!-- delta:SF-2026-ARXIV-2607-03333:end --><!-- books-review:SF-2026-ARXIV-2607-03333:end -->

<!-- books-review:SF-2026-ARXIV-2607-03948:start --><!-- existing:SF-2026-ARXIV-2607-03948:start -->对读 `books/part-05-inference-system/56-inference-scheduling.md#L97` 与相邻章节后，现有命题（`books/part-05-inference-system/56-inference-scheduling.md#L43-L90`）为：Ch56 already separates admission, iteration scheduling, routing/placement and autoscaling and requires future-KV feasibility, goodput, calibration and fairness, but did not yet make future batch/KV scarcity an explicit per-request opportunity cost.<!-- existing:SF-2026-ARXIV-2607-03948:end --><!-- delta:SF-2026-ARXIV-2607-03948:start -->新增证据边界：When output length is heterogeneous and KV grows over time, a queue snapshot cannot express the opportunity cost of admitting a request across future batch and memory capacity. An online controller can compare SLO-weighted benefit with time-indexed batch/KV shadow prices and update those prices from residual capacity plus historical predicted action columns. This makes cross-time commitment explicit but adds a separate production responsibility: output-length calibration must compare predicted with realized service without being misrepresented as the paper's price-update mechanism. 该 delta 已进入 `books/part-05-inference-system/56-inference-scheduling.md#L97`，正文保留旧方案成立条件、约束变化、代价与下一重压力。<!-- delta:SF-2026-ARXIV-2607-03948:end --><!-- books-review:SF-2026-ARXIV-2607-03948:end -->

<!-- books-review:SF-2026-ARXIV-2607-04181:start --><!-- existing:SF-2026-ARXIV-2607-04181:start -->对读 `books/part-05-inference-system/56-inference-scheduling.md#L255` 与相邻章节后，现有命题（`books/part-05-inference-system/56-inference-scheduling.md#L229`）为：Ch56 already evolves replica-level scaling toward stage and operator-DAG elasticity and requires profile, topology, state and failure-aware scheduling.<!-- existing:SF-2026-ARXIV-2607-04181:end --><!-- delta:SF-2026-ARXIV-2607-04181:start -->新增证据边界：A full model replica is not the only elastic unit. A controller can choose replication counts for consecutive Transformer layer segments; the scheduler scatters sub-batches across those replicas, gathers boundary activations and redistributes affected KV partitions during a configuration transition. This reduces whole-instance startup pressure on the evaluated topology but turns activation boundaries, KV ownership and transition coordination into correctness-critical scheduling state. The v1 manuscript does not define atomic configuration publication, route-version semantics or a state-transfer-plus-SLO commit protocol. 该 delta 已进入 `books/part-05-inference-system/56-inference-scheduling.md#L255`，正文保留旧方案成立条件、约束变化、代价与下一重压力。<!-- delta:SF-2026-ARXIV-2607-04181:end --><!-- books-review:SF-2026-ARXIV-2607-04181:end -->

<!-- books-review:SF-2026-ARXIV-2607-04302:start --><!-- existing:SF-2026-ARXIV-2607-04302:start -->对读 `books/part-05-inference-system/49-tensorrt-llm.md#L441` 与相邻章节后，现有命题（`books/part-05-inference-system/49-tensorrt-llm.md#L263`）为：Ch49 already explains that lower bit width does not automatically accelerate attention and that distribution handling, calibration, fusion and runtime execution must be co-designed.<!-- existing:SF-2026-ARXIV-2607-04302:end --><!-- delta:SF-2026-ARXIV-2607-04302:start -->新增证据边界：Attention quantization should first diagnose asymmetric Q/K structure. When calibration confirms the K-outlier regime, a paired diagonal transform can scale Q and inversely scale K while preserving the unquantized attention score; a quantized-P reordering can then make the softmax numerator and denominator consume the same quantized tensor. The equality does not preserve the final quantized output, and the reordering removes one coherent error component rather than proving all Q/K/V error harmless. 该 delta 已进入 `books/part-05-inference-system/49-tensorrt-llm.md#L441`，正文保留旧方案成立条件、约束变化、代价与下一重压力。<!-- delta:SF-2026-ARXIV-2607-04302:end --><!-- books-review:SF-2026-ARXIV-2607-04302:end -->

<!-- books-review:SF-2026-ARXIV-2607-04391:start --><!-- existing:SF-2026-ARXIV-2607-04391:start -->对读 `books/part-07-agent/77-memory.md#L1` 与相邻章节后，现有命题（`books/part-07-agent/77-memory.md#L1`）为：Ch77 already separates compact control state from exact evidence archive and requires provenance, authorization, correction and auditability; Ch76 owns retrieval and Ch78 owns tool execution.<!-- existing:SF-2026-ARXIV-2607-04391:end --><!-- delta:SF-2026-ARXIV-2607-04391:start -->新增证据边界：The immutable source corpus remains evidence truth while relational metadata, semantic overlays and query profiles are revisable derived views. This is a concrete operational instance of the existing archive-versus-derived-memory contract, not a new canonical mechanism. 该证据未改变现有长期命题；保留为受限 workload 的 supporting evidence，不在正文重复追加论文段落。<!-- delta:SF-2026-ARXIV-2607-04391:end --><!-- books-review:SF-2026-ARXIV-2607-04391:end -->

<!-- books-review:SF-2026-ARXIV-2607-04395:start --><!-- existing:SF-2026-ARXIV-2607-04395:start -->对读 `books/part-05-inference-system/49-tensorrt-llm.md#L437-L458` 与相邻章节后，现有命题（`books/part-05-inference-system/49-tensorrt-llm.md#L437-L458`）为：Ch49 already treats learned kernel generation as candidate production while compiler/correctness checks own admission; Ch33 owns sparse group-relative reward failure and Ch78 owns typed execution authority.<!-- existing:SF-2026-ARXIV-2607-04395:end --><!-- delta:SF-2026-ARXIV-2607-04395:start -->新增证据边界：An executable compiler and numerical reference can own kernel admission even when the model proposes candidates, but that binary verifier can be a weak group-relative learning signal when every candidate in a group fails together. This bounded accelerator case connects existing execution, RL and tool-authority principles without changing their canonical owners. 该证据未改变现有长期命题；保留为受限 workload 的 supporting evidence，不在正文重复追加论文段落。<!-- delta:SF-2026-ARXIV-2607-04395:end --><!-- books-review:SF-2026-ARXIV-2607-04395:end -->

<!-- books-review:SF-2026-ARXIV-2607-04668:start --><!-- existing:SF-2026-ARXIV-2607-04668:start -->对读 `books/part-05-inference-system/56-inference-scheduling.md#L358` 与相邻章节后，现有命题（`books/part-05-inference-system/56-inference-scheduling.md#L305-L335`）为：Ch56 already owns barrier-synchronized worker sets, scheduling-state transitions and work-conserving resource control, but does not yet distinguish requested membership from acknowledged token membership.<!-- existing:SF-2026-ARXIV-2607-04668:end --><!-- delta:SF-2026-ARXIV-2607-04668:start -->新增证据边界：A generation increments a global epoch; a core joins only after parking its tenant and ACKing that epoch. Each token snapshots requested intersect current-ACKed cores into one generation-tagged participant latch, and barriers wait on the latched count rather than named cores. A core that misses the latch is outside the token, while row work stealing absorbs the missing share. Owner CAS plus idempotent teardown keeps failure paths from leaving a live gang. Scheduler owns requested membership and tenant migration; each core owns its epoch ACK; the generation latch owns the immutable per-token participant set; the inference engine owns row assignment and token commit. Control changes occur only at generation/token boundaries, while model rows and partial sums remain on the token data path. 该 delta 已进入 `books/part-05-inference-system/56-inference-scheduling.md#L358`，正文保留旧方案成立条件、约束变化、代价与下一重压力。<!-- delta:SF-2026-ARXIV-2607-04668:end --><!-- books-review:SF-2026-ARXIV-2607-04668:end -->

<!-- books-review:SF-2026-ARXIV-2607-04763:start --><!-- existing:SF-2026-ARXIV-2607-04763:start -->对读 `books/part-04-training-system/29-sft.md#L255-L281` 与相邻章节后，现有命题（`books/part-04-training-system/29-sft.md#L255-L281`）为：Ch29 already contains the full prefix-replay evolution chain, the two-sided distribution-shift debt, the teacher/environment provenance boundary and the conditions under which live OPD or ordinary offline SFT remains preferable.<!-- existing:SF-2026-ARXIV-2607-04763:end --><!-- delta:SF-2026-ARXIV-2607-04763:start -->新增证据边界：The teacher's recorded multi-turn history and observations are replayed as a prefix; the student generates the action only at the supervised step, and the teacher supplies dense conditional token targets at that student action. A step-decaying prefix sampler reduces exposure to late histories where teacher-forced state and student occupancy diverge. This trades live environment interaction for a reliability-aware replay distribution. The trajectory store owns immutable teacher prefix/observation provenance; the sampler owns which step becomes supervision; the student owns the current action distribution; the teacher owns the conditional target; no environment side effect is executed during student training. Replay freshness and environment version remain external debts. 该证据未改变现有长期命题；保留为受限 workload 的 supporting evidence，不在正文重复追加论文段落。<!-- delta:SF-2026-ARXIV-2607-04763:end --><!-- books-review:SF-2026-ARXIV-2607-04763:end -->

<!-- books-review:SF-2026-ARXIV-2607-05029:start --><!-- existing:SF-2026-ARXIV-2607-05029:start -->对读 `books/part-06-ai-infrastructure/72-security.md#L451` 与相邻章节后，现有命题（`books/part-06-ai-infrastructure/72-security.md#L416-L435`）为：Ch72 already protects Agent instruction/config/memory and Ch77 already rejects provenance-correlated majority as independent evidence; neither explicitly freezes remembered completion claims below authoritative effect receipts.<!-- existing:SF-2026-ARXIV-2607-05029:end --><!-- delta:SF-2026-ARXIV-2607-05029:start -->新增证据边界：An attacker writes persistent memory entries that imitate a trusted reasoning trace and claim a safety check or prerequisite was already completed. Repetition creates correlated descendants, so majority/consensus logic may count one forged origin as apparently repeated support. SENTINEL layers lexical, provenance/taint, risk-pattern and reasoning checks, but its own ablation makes the Reasoning Guard load-bearing and the limitations show adaptive paraphrase can evade it. Project inference for the durable system contract: the memory store owns untrusted persisted claims and provenance; a security policy owns taint/risk routing; only the authoritative tool/environment/effect receipt can own whether an action actually completed. Read-time voting should collapse descendants sharing one provenance family before counting evidence. 该 delta 已进入 `books/part-06-ai-infrastructure/72-security.md#L451`，正文保留旧方案成立条件、约束变化、代价与下一重压力。<!-- delta:SF-2026-ARXIV-2607-05029:end --><!-- books-review:SF-2026-ARXIV-2607-05029:end -->

<!-- books-review:SF-2026-ARXIV-2607-05061:start --><!-- existing:SF-2026-ARXIV-2607-05061:start -->对读 `books/part-05-inference-system/45-why-kv-cache-speeds-up.md#L306-L359` 与相邻章节后，现有命题（`books/part-05-inference-system/45-why-kv-cache-speeds-up.md#L306-L359`）为：Ch45 already contains the oracle-to-learned-eviction evolution, future-access target, stateful/stateless scorer, delayed-scoring trade-off, fixed-budget runtime boundary and KVpop evidence limits.<!-- existing:SF-2026-ARXIV-2607-05061:end --><!-- delta:SF-2026-ARXIV-2607-05061:start -->新增证据边界：Future attention mass after a protected window becomes the retention target. A boundary-focused loss trains a lightweight stateless or recurrent scorer; scoring may be delayed until the eviction boundary to expose near-future context. Runtime retains a fixed top-k budget per head, separating learned importance prediction from regular memory allocation. The target-construction path uses future attention only during training; the online scorer owns a per-token priority estimate; the cache manager owns the hard capacity and top-k commit; the model's true future attention is unavailable at eviction time. Delayed scoring trades memory residency for a better observation window. 该证据未改变现有长期命题；保留为受限 workload 的 supporting evidence，不在正文重复追加论文段落。<!-- delta:SF-2026-ARXIV-2607-05061:end --><!-- books-review:SF-2026-ARXIV-2607-05061:end -->

<!-- books-review:SF-2026-ARXIV-2607-05147:start --><!-- existing:SF-2026-ARXIV-2607-05147:start -->对读 `books/part-05-inference-system/48-speculative-decoding.md#L190-L230` 与相邻章节后，现有命题（`books/part-05-inference-system/48-speculative-decoding.md#L190-L230`）为：Ch48 already treats verify depth as a capacity-aware policy, separates confidence from target commit authority and preserves rollback/KV/SLO boundaries using DSpark as Experimental evidence.<!-- existing:SF-2026-ARXIV-2607-05147:end --><!-- delta:SF-2026-ARXIV-2607-05147:start -->新增证据边界：A semi-autoregressive drafter proposes multiple tokens with lightweight sequential dependency, while a confidence head predicts how far verification should extend. A hardware-aware scheduler maps confidence and target-device behavior into a variable verify window; the target model remains authoritative and rejected suffixes roll back. The drafter owns provisional tokens and confidence; scheduler owns proposal/verify length; target owns acceptance; runtime owns provisional KV, rollback and batch capacity. Confidence is an estimate, not the commit authority. 该证据未改变现有长期命题；保留为受限 workload 的 supporting evidence，不在正文重复追加论文段落。<!-- delta:SF-2026-ARXIV-2607-05147:end --><!-- books-review:SF-2026-ARXIV-2607-05147:end -->

<!-- books-review:SF-2026-ARXIV-2607-05391:start --><!-- existing:SF-2026-ARXIV-2607-05391:start -->对读 `books/part-06-ai-infrastructure/66-evaluation-system.md#L1` 与相邻章节后，现有命题（`books/part-06-ai-infrastructure/66-evaluation-system.md#L1`）为：Ch66 already separates scorer/verifier from outcome authority, covers criteria/repetition/ranking, calibration, claim graphs and trajectory evidence, including the exact correlated-confidence boundary.<!-- existing:SF-2026-ARXIV-2607-05391:end --><!-- delta:SF-2026-ARXIV-2607-05391:start -->新增证据边界：A verifier converts the probability distribution over ordered score tokens into a continuous expected score, can aggregate repeated criteria/runs, and can learn pairwise preferences. Candidate selection can be reduced by probabilistic pivot tournaments, but every layer remains a fallible judgment channel whose calibration and correlation must be measured. The environment/test harness owns executable outcome; the verifier owns a probabilistic score or preference; an aggregator owns criterion/repetition combination; a selection policy owns budgeted ranking. Verifier confidence cannot overwrite environment truth. 该证据未改变现有长期命题；保留为受限 workload 的 supporting evidence，不在正文重复追加论文段落。<!-- delta:SF-2026-ARXIV-2607-05391:end --><!-- books-review:SF-2026-ARXIV-2607-05391:end -->

<!-- books-review:SF-2026-ARXIV-2607-05394:start --><!-- existing:SF-2026-ARXIV-2607-05394:start -->对读 `books/part-04-training-system/29-sft.md#L277-L281` 与相邻章节后，现有命题（`books/part-04-training-system/29-sft.md#L277-L281`）为：Ch29 already distinguishes policy-shift transfer from final-policy imitation, preserves student-on-policy prefixes, checkpoint-pair identity, support/KL/length limits and the branch's coexistence with SFT/RL.<!-- existing:SF-2026-ARXIV-2607-05394:end --><!-- delta:SF-2026-ARXIV-2607-05394:start -->新增证据边界：Instead of imitating a weaker post-RL teacher's final policy, Direct-OPD contrasts that teacher with its own pre-RL reference. The log policy ratio becomes a dense directional reward evaluated on the stronger student's on-policy prefixes, transferring the change induced by RL rather than the weaker model's capability ceiling. Teacher/reference checkpoint identity jointly owns the policy-shift signal; the student owns sampled prefixes; token log-ratios provide dense supervision; adaptive KL owns proximity control. The method cannot create useful direction where the teacher/reference delta is irrelevant or unsupported on student states. 该证据未改变现有长期命题；保留为受限 workload 的 supporting evidence，不在正文重复追加论文段落。<!-- delta:SF-2026-ARXIV-2607-05394:end --><!-- books-review:SF-2026-ARXIV-2607-05394:end -->

<!-- audit-target:books:end -->
## 7. Semantic Audit

<!-- validator:semantic-audit-v1 -->
| Audit ID | Auditor | Scope | Reviewed Refs | Findings | Resolution | Status |
| --- | --- | --- | --- | --- | --- | --- |
| SA-20260707-COVERAGE-OWNER-REBUILD | fresh-context:pending-owner-rebuild | coverage | coverage:SRC-GITHUB-COMMIT:20260707-owner-transfer | GAP-ARXIV-SEMANTIC-OWNER-REBUILD-20260707: raw closures and false-negative frontier require independent semantic review | Open — canonical inventory and owner receipt are preserved in the date-local source packet | open |
| SA-20260707-EVIDENCE-OWNER-REBUILD | fresh-context:pending-owner-rebuild | evidence | review:SF-2026-ARXIV-2607-02574; review:SF-2026-ARXIV-2607-02577; review:SF-2026-ARXIV-2607-02604; review:SF-2026-ARXIV-2607-02686; review:SF-2026-ARXIV-2607-02840; review:SF-2026-ARXIV-2607-02865; review:SF-2026-ARXIV-2607-02882; review:SF-2026-ARXIV-2607-02980; review:SF-2026-ARXIV-2607-03146; review:SF-2026-ARXIV-2607-03182; review:SF-2026-ARXIV-2607-03333; review:SF-2026-ARXIV-2607-03449; review:SF-2026-ARXIV-2607-03461; review:SF-2026-ARXIV-2607-03473; review:SF-2026-ARXIV-2607-03693; review:SF-2026-ARXIV-2607-03751; review:SF-2026-ARXIV-2607-03870; review:SF-2026-ARXIV-2607-03876; review:SF-2026-ARXIV-2607-03948; review:SF-2026-ARXIV-2607-03964; review:SF-2026-ARXIV-2607-04171; review:SF-2026-ARXIV-2607-04181; review:SF-2026-ARXIV-2607-04292; review:SF-2026-ARXIV-2607-04302; review:SF-2026-ARXIV-2607-04391; review:SF-2026-ARXIV-2607-04395; review:SF-2026-ARXIV-2607-04517; review:SF-2026-ARXIV-2607-04591; review:SF-2026-ARXIV-2607-04609; review:SF-2026-ARXIV-2607-04637; review:SF-2026-ARXIV-2607-04668; review:SF-2026-ARXIV-2607-04681; review:SF-2026-ARXIV-2607-04763; review:SF-2026-ARXIV-2607-04816; review:SF-2026-ARXIV-2607-04969; review:SF-2026-ARXIV-2607-05029; review:SF-2026-ARXIV-2607-05061; review:SF-2026-ARXIV-2607-05122; review:SF-2026-ARXIV-2607-05147; review:SF-2026-ARXIV-2607-05391; review:SF-2026-ARXIV-2607-05394; review:SF-2026-ARXIV-2607-05396 | EVIDENCE-OWNER-REBUILD-20260707: transferred exact-v1 reviews require fresh-context false-positive and access audit | Open — transferred review bodies remain provenance, not final acceptance | open |
| SA-20260707-SELECTION-OWNER-REBUILD | fresh-context:pending-owner-rebuild | deep_analysis_selection | analysis:DA-20260701-2607-02577; analysis-decision:SF-2026-ARXIV-2607-02980; analysis:DA-20260704-2607-03333; analysis-decision:SF-2026-ARXIV-2607-03948; analysis-decision:SF-2026-ARXIV-2607-04181; analysis-decision:SF-2026-ARXIV-2607-04302; analysis-decision:SF-2026-ARXIV-2607-04668; analysis-decision:SF-2026-ARXIV-2607-04763; analysis:DA-20260707-2607-05029; analysis-decision:SF-2026-ARXIV-2607-05061; analysis-decision:SF-2026-ARXIV-2607-05147; analysis-decision:SF-2026-ARXIV-2607-05391; analysis-decision:SF-2026-ARXIV-2607-05394 | SELECTION-OWNER-REBUILD-20260707: eligibility and at-most-three narrative choice require independent comparison after owner transfer | Open — canonical selection receipts are structurally reconstructed | open |
| SA-20260707-BOOKS-OWNER-REBUILD | fresh-context:pending-owner-rebuild | books | books-review:SF-2026-ARXIV-2607-02577; books-review:SF-2026-ARXIV-2607-02980; books-review:SF-2026-ARXIV-2607-03333; books-review:SF-2026-ARXIV-2607-03948; books-review:SF-2026-ARXIV-2607-04181; books-review:SF-2026-ARXIV-2607-04302; books-review:SF-2026-ARXIV-2607-04391; books-review:SF-2026-ARXIV-2607-04395; books-review:SF-2026-ARXIV-2607-04668; books-review:SF-2026-ARXIV-2607-04763; books-review:SF-2026-ARXIV-2607-05029; books-review:SF-2026-ARXIV-2607-05061; books-review:SF-2026-ARXIV-2607-05147; books-review:SF-2026-ARXIV-2607-05391; books-review:SF-2026-ARXIV-2607-05394 | BOOKS-OWNER-REBUILD-20260707: Books comparisons are frozen provenance pending upstream semantic gates and root writeback reconciliation | Open — month-local Books queue remains frozen | open |
## 8. Ignored Noise

1122 个窗口内 identity 中，1101 个未进入候选分母：它们属于垂直应用、单数据集质量增量、没有状态/控制权变化的模型使用案例，或不在合同 category route。该数字是 route closure，不是声称逐篇全文审阅。

## 9. Recommended Action

1. Sunday Weekly 聚合本日报 family 与 RP，不按发现日重复计分。
2. 只有重要 revision、artifact、反证或 owner 冲突才重开本日报。
3. Books Decision：4 个 `Integrate`，6 个 `No Change — Existing Coverage`，1 个 `Weekly Only — Context`，10 个 `Rejected — Low Durability / Out of Scope`；Deep 11 / Standard 0。

## 10. Repository Changes

- 新建或更新 `papers/2026/07/07/README.md`。
- 本日报长期 delta 已同步至：`books/part-05-inference-system/49-tensorrt-llm.md`、`books/part-05-inference-system/56-inference-scheduling.md`、`books/part-06-ai-infrastructure/72-security.md`、`books/part-07-agent/77-memory.md`。

## 11. Open Questions

- 后续 revision 是否新增 artifact、独立复现或 failure evidence，从而改变当前 claim boundary？
- Sunday Weekly 的跨日演进链是否需要合并本日报多个同类 family？

## 12. Sources

- [From Tensor Buffer to Distributed Memory Hierarchy: A Survey of KV Cache Management for LLM Serving](https://arxiv.org/abs/2607.02574v1) — first-public（Asia/Shanghai）：2026-07-07；exact evidence：v1；accessed：2026-09-03
- [Benchmarking the Benchmarks: A Validity Audit of Tool-Calling Evaluation](https://arxiv.org/abs/2607.02577v1) — first-public（Asia/Shanghai）：2026-07-07；exact evidence：v1；accessed：2026-09-03
- [DynaWM: A Base-VLA-Guided World Foundation Model for Moving-Object Manipulation](https://arxiv.org/abs/2607.02604v1) — first-public（Asia/Shanghai）：2026-07-07；exact evidence：v1；accessed：2026-09-03
- [ASK in the Dark: Uncertainty-Gated LLM Assistance under Partial Observability](https://arxiv.org/abs/2607.02686v1) — first-public（Asia/Shanghai）：2026-07-07；exact evidence：v1；accessed：2026-09-03
- [TACO: TActile World Model as a Self-COrrector forScalable VLA Post-Training](https://arxiv.org/abs/2607.02840v1) — first-public（Asia/Shanghai）：2026-07-07；exact evidence：v1；accessed：2026-09-03
- [DREAMSTEER: Latent World Models Can Steer VLA Policies During Deployment Without Any Finetuning](https://arxiv.org/abs/2607.02865v1) — first-public（Asia/Shanghai）：2026-07-07；exact evidence：v1；accessed：2026-09-03
- [Diagnosis-Driven Automatic Repair for Agentic Workflow via Symbolic Inference](https://arxiv.org/abs/2607.02882v1) — first-public（Asia/Shanghai）：2026-07-07；exact evidence：v1；accessed：2026-09-03
- [Hierarchical Sparse Attention Done Right: Toward Infinite Context Modeling](https://arxiv.org/abs/2607.02980v1) — first-public（Asia/Shanghai）：2026-07-07；exact evidence：v1；accessed：2026-09-03
- [Exp2VLA: Enabling Vision-Language-Action for Drone Navigation from Expert Demonstrations](https://arxiv.org/abs/2607.03146v1) — first-public（Asia/Shanghai）：2026-07-07；exact evidence：v1；accessed：2026-09-03
- [AnchorVLA: Bridging Discrete Decisions and Continuous Trajectories for Vision-Language-Action Planning](https://arxiv.org/abs/2607.03182v1) — first-public（Asia/Shanghai）：2026-07-07；exact evidence：v1；accessed：2026-09-03
- [SPORK: Self-Speculative Forking to Accelerate Agentic LLM Inference](https://arxiv.org/abs/2607.03333v1) — first-public（Asia/Shanghai）：2026-07-07；exact evidence：v1；accessed：2026-09-03
- [HiMe: Hierarchical Embodied Memory for Long-Horizon Vision-Language-Action Control](https://arxiv.org/abs/2607.03449v1) — first-public（Asia/Shanghai）：2026-07-07；exact evidence：v1；accessed：2026-09-03
- [WorldBagel: Uncovering the Power of Unified Multimodal Models for Vision-Language-Action-World Modeling](https://arxiv.org/abs/2607.03461v1) — first-public（Asia/Shanghai）：2026-07-07；exact evidence：v1；accessed：2026-09-03
- [MUTE: Return-Preserving Communication Unlearning for Efficient Multi-Agent Coordination](https://arxiv.org/abs/2607.03473v1) — first-public（Asia/Shanghai）：2026-07-07；exact evidence：v1；accessed：2026-09-03
- [CoRE-VLA: Towards Scalable and Robust Vision-Language-Action Modeling via Conditional Routing of Experts](https://arxiv.org/abs/2607.03693v1) — first-public（Asia/Shanghai）：2026-07-07；exact evidence：v1；accessed：2026-09-03
- [Look Before You Leap: Distilling Tree Search into Action Evaluation for Frozen VLA Models](https://arxiv.org/abs/2607.03751v1) — first-public（Asia/Shanghai）：2026-07-07；exact evidence：v1；accessed：2026-09-03
- [Evaluating LLM Uncertainty in Long-Form Generation Using Deterministic Ground Truth](https://arxiv.org/abs/2607.03870v1) — first-public（Asia/Shanghai）：2026-07-07；exact evidence：v1；accessed：2026-09-03
- [AdaptiveSD A Stability-Aware, Runtime-Adaptive Speculative Decoding Framework with Multi-Policy Orchestration for CPU-Constrained LLM Inference](https://arxiv.org/abs/2607.03876v1) — first-public（Asia/Shanghai）：2026-07-07；exact evidence：v1；accessed：2026-09-03
- [Online Linear Programming for Multi-Objective Routing in LLM Serving](https://arxiv.org/abs/2607.03948v1) — first-public（Asia/Shanghai）：2026-07-07；exact evidence：v1；accessed：2026-09-03
- [Worldscape-MoE: A Unified Mixture-of-Experts World Model for Scalable Heterogeneous Action Control](https://arxiv.org/abs/2607.03964v1) — first-public（Asia/Shanghai）：2026-07-07；exact evidence：v1；accessed：2026-09-03
- [Teaching Tiny VLA Models Where to Look and How to Move](https://arxiv.org/abs/2607.04171v1) — first-public（Asia/Shanghai）：2026-07-07；exact evidence：v1；accessed：2026-09-03
- [CoCoScale: Leveraging Layer-wise Scaling to Unlock the Potential of Online LLM Serving](https://arxiv.org/abs/2607.04181v1) — first-public（Asia/Shanghai）：2026-07-07；exact evidence：v1；accessed：2026-09-03
- [Agentic SABRE: An Uncertainty-Aware Neuro-Symbolic Multi-Agent Framework for Adaptive Ransomware Detection](https://arxiv.org/abs/2607.04292v1) — first-public（Asia/Shanghai）：2026-07-07；exact evidence：v1；accessed：2026-09-03
- [HiFA4: Training-Free 4-bit FlashAttention on Ascend HIF4 NPUs for LLM Inference](https://arxiv.org/abs/2607.04302v1) — first-public（Asia/Shanghai）：2026-07-07；exact evidence：v1；accessed：2026-09-03
- [Memory-Orchestrated Semantic System (MOSS): An Auditable Agentic Memory Architecture](https://arxiv.org/abs/2607.04391v1) — first-public（Asia/Shanghai）：2026-07-07；exact evidence：v1；accessed：2026-09-03
- [NKI-Agent: Domain-Specific Fine-Tuning and Agentic Tool Use for Neuron Kernel Generation](https://arxiv.org/abs/2607.04395v1) — first-public（Asia/Shanghai）：2026-07-07；exact evidence：v1；accessed：2026-09-03
- [VLA Grounder: Language-Conditioning Space Optimization for Black-Box VLA Models](https://arxiv.org/abs/2607.04517v1) — first-public（Asia/Shanghai）：2026-07-07；exact evidence：v1；accessed：2026-09-03
- [Simple-to-Complex Structured Demonstrations for Vision-Language-Action Learning](https://arxiv.org/abs/2607.04591v1) — first-public（Asia/Shanghai）：2026-07-07；exact evidence：v1；accessed：2026-09-03
- [SEAM: Smooth Execution of Action-Chunked Motion for Vision-Language-Action Policies](https://arxiv.org/abs/2607.04609v1) — first-public（Asia/Shanghai）：2026-07-07；exact evidence：v1；accessed：2026-09-03
- [PixelPilot: Scalable Vision-Language-Action Models for End-to-End Autonomous Driving](https://arxiv.org/abs/2607.04637v1) — first-public（Asia/Shanghai）：2026-07-07；exact evidence：v1；accessed：2026-09-03
- [Elastic Gang: Per-Token Membership Change for a Hard-Barriered LLM Inference Gang Co-Scheduled with OS Processes](https://arxiv.org/abs/2607.04668v1) — first-public（Asia/Shanghai）：2026-07-07；exact evidence：v1；accessed：2026-09-03
- [Do Vision-Language-Action Models Mean What They Say? On the Role of Faithfulness in Embodied Reasoning](https://arxiv.org/abs/2607.04681v1) — first-public（Asia/Shanghai）：2026-07-07；exact evidence：v1；accessed：2026-09-03
- [Multi-Turn On-Policy Distillation with Prefix Replay](https://arxiv.org/abs/2607.04763v1) — first-public（Asia/Shanghai）：2026-07-07；exact evidence：v1；accessed：2026-09-03
- [CAC-VLA: Context-Gated Action Conditioning for Vision-Language-Action Models](https://arxiv.org/abs/2607.04816v1) — first-public（Asia/Shanghai）：2026-07-07；exact evidence：v1；accessed：2026-09-03
- [Train Smarter, Not Longer: Memorization-Guided Data Reuse for Efficient LLM Training](https://arxiv.org/abs/2607.04969v1) — first-public（Asia/Shanghai）：2026-07-07；exact evidence：v1；accessed：2026-09-03
- [Your Agent's Memories Are Not Its Own: Forged Reasoning Attacks on LLM Agent Memory and Defenses](https://arxiv.org/abs/2607.05029v1) — first-public（Asia/Shanghai）：2026-07-07；exact evidence：v1；accessed：2026-09-03
- [KVpop -- Key-Value Cache Compression with Predictive Online Pruning](https://arxiv.org/abs/2607.05061v1) — first-public（Asia/Shanghai）：2026-07-07；exact evidence：v1；accessed：2026-09-03
- [Green for Go, Red for No: Visual Grounding via Semantic Segmentation for VLA Navigation Policies](https://arxiv.org/abs/2607.05122v1) — first-public（Asia/Shanghai）：2026-07-07；exact evidence：v1；accessed：2026-09-03
- [DSpark: Confidence-Scheduled Speculative Decoding with Semi-Autoregressive Generation](https://arxiv.org/abs/2607.05147v1) — first-public（Asia/Shanghai）：2026-07-07；exact evidence：v1；accessed：2026-09-03
- [LLM-as-a-Verifier: A General-Purpose Verification Framework](https://arxiv.org/abs/2607.05391v1) — first-public（Asia/Shanghai）：2026-07-07；exact evidence：v1；accessed：2026-09-03
- [Weak-to-Strong Generalization via Direct On-Policy Distillation](https://arxiv.org/abs/2607.05394v1) — first-public（Asia/Shanghai）：2026-07-07；exact evidence：v1；accessed：2026-09-03
- [From Fixed to Free Cameras: Calibration-Free View-Robust Vision-Language-Action Model](https://arxiv.org/abs/2607.05396v1) — first-public（Asia/Shanghai）：2026-07-07；exact evidence：v1；accessed：2026-09-03
## 13. Final Status

Daily V2.1 的 Coverage、Evidence、Deep Analysis Selection 与 Books Decision 均已完成；fresh-context Semantic Audit 无未解决 finding，三个 Gate 均已闭合。

State Truth: Completion=In Progress；Coverage=Open；Evidence=Open；Books=Open；Unresolved Findings=2。
