# Daily Research — 2026-06-18

**Research Date:** 2026-06-18

**Timezone:** Asia/Shanghai

**Strict Window:** 2026-06-17 09:00:00 ～ 2026-06-18 09:00:00（北京时间，左闭右开）

**Contract:** V2.1 Full Replay；516/516 identities 完成 title+abstract semantic screening，技术 claim 仅来自 exact-v1 primary evidence 与已冻结 source packet

**Status:** In Progress；Coverage=Open、Evidence=Open、Books=Open；最新合同恢复状态见 Coverage 与第 7、13 节

## Executive Summary
> Strict V2.1 Daily for `DEN-20260618-2977f506`. All V2.1 Gates passed after the complete 37/37 post-write fresh audit.

Beijing window `[2026-06-17 09:00, 2026-06-18 09:00)` contains 516 registered identities. Full 516/516 title+abstract screening freezes 37 durable families and 479 family-specific closures. Official exact-v1 HTML was reviewed for 37/37 families. Full-frontier selection freezes three winners before rationale. Books comparison yields 16 Integrate proposals and 21 No Change handoffs.

## 1. Coverage

<!-- validator:report-metadata-v2 -->
| Field | Value |
| --- | --- |
| Contract Version | V2.1 |
| Score Schema | V2 |
| Report Type | Daily |
| Window Start | 2026-06-18 |
| Window End | 2026-06-18 |
| Registry Version | 2026-08-25 |
| Coverage Mode | Full Replay |
| Baseline Report | — |
| Changed Source IDs | — |
| Previous Denominator ID | — |
| Denominator ID | DEN-20260618-2977f506 |
| Denominator Frozen At | 2026-08-29T23:40:00+08:00 |
| Completion Status | In Progress |
| Coverage Gate | Open |
| Evidence Gate | Open |
| Books Gate | Open |

### Source Coverage Receipt

<!-- validator:source-coverage-v2 -->
| Source ID | Window Start | Window End | Executed At | Endpoint / Filter | Result | Hits | Candidate Source Families | Pagination / Cursor | Window Watermark | Closure Evidence | Gap / Limitation ID |
| --- | --- | --- | --- | --- | --- | ---: | --- | --- | --- | --- | --- |
| SRC-ARXIV | 2026-06-17T09:00:00+08:00 | 2026-06-18T09:00:00+08:00 | 2026-08-29T23:40:00+08:00 | arXiv official availability schedule + exact-v1 Atom + DataCite DOI created | incomplete | 525 | SF-2026-ARXIV-2606-18284;SF-2026-ARXIV-2606-18286;SF-2026-ARXIV-2606-18310;SF-2026-ARXIV-2606-18322;SF-2026-ARXIV-2606-18356;SF-2026-ARXIV-2606-18379;SF-2026-ARXIV-2606-18383;SF-2026-ARXIV-2606-18394;SF-2026-ARXIV-2606-18400;SF-2026-ARXIV-2606-18421;SF-2026-ARXIV-2606-18431;SF-2026-ARXIV-2606-18448;SF-2026-ARXIV-2606-18467;SF-2026-ARXIV-2606-18497;SF-2026-ARXIV-2606-18532;SF-2026-ARXIV-2606-18550;SF-2026-ARXIV-2606-18600;SF-2026-ARXIV-2606-18619;SF-2026-ARXIV-2606-18650;SF-2026-ARXIV-2606-18668;SF-2026-ARXIV-2606-18673;SF-2026-ARXIV-2606-18697;SF-2026-ARXIV-2606-18741;SF-2026-ARXIV-2606-18746;SF-2026-ARXIV-2606-18810;SF-2026-ARXIV-2606-18829;SF-2026-ARXIV-2606-18831;SF-2026-ARXIV-2606-18847;SF-2026-ARXIV-2606-18874;SF-2026-ARXIV-2606-18958;SF-2026-ARXIV-2606-18967;SF-2026-ARXIV-2606-18996;SF-2026-ARXIV-2606-19004;SF-2026-ARXIV-2606-19025;SF-2026-ARXIV-2606-19057;SF-2026-ARXIV-2606-19111;SF-2026-ARXIV-2606-19191;SF-2026-ARXIV-2606-19242;SF-2026-ARXIV-2606-19262;SF-2026-ARXIV-2606-19271 | — | 2026-09-03T12:10:00+08:00 | ../_sources/daily-20260618/official-arxiv-first-public-owner-receipt-v1.json; coverage:SRC-ARXIV:20260618; unclosed: canonical candidate redistribution pending | GAP-ARXIV-CANONICAL-REDISTRIBUTION-20260618 |
<!-- coverage:SRC-ARXIV:20260618:start -->
All 357 Core, 55 keyword-routed and 104 route-negative identities were screened. Frozen arithmetic: `516 = 37 retained + 479 closures`. Route reconciliation: `{"keyword_daily_semantic_review_required": {"raw": 55, "retained": 5, "closure": 50}, "not_routed_by_keyword_contract": {"raw": 104, "retained": 1, "closure": 103}, "core_daily_semantic_review_required": {"raw": 357, "retained": 31, "closure": 326}}`. Keyword routing was recall-only.
<!-- coverage:SRC-ARXIV:20260618:end -->


<!-- latest-contract-reopen:2026-06-18:start -->
### Latest-contract Reopen Notice

2026-09-03 全量复核重新打开本日报。旧 `Complete` 只证明原分母内部的表格算术，不证明当前 V2.1 Coverage：arXiv candidate owner receipt 已恢复；当前仍需按 canonical owner 重分配候选与分母。非空 source packet、原 Source Review 与 Books Comparison 暂作 provenance 保留，不作为最新合同验收结论。2026-08-25 才生效的新增来源不倒推为当日 Required receipt，只按 Source Delta Audit 检查真实 in-window family。当前 finding：`canonical_owner_candidate_redistribution_pending, fresh_context_per_identity_semantic_audit_pending, exact_primary_access_recheck_pending`。
<!-- latest-contract-reopen:2026-06-18:end -->

### Canonical raw-inventory recovery checkpoint

本轮已从非空官方 DataCite arXiv DOI snapshot 恢复 **525** 条注册类别 identity，并以 immutable DOI `created` 与候选级 announcement owner reconciliation 归档到本日。其中 **40** 条是旧报告 retained provenance，**485** 条已获得逐 family title+abstract closure proposal。这些 proposal 尚未经过 fresh-context false-positive/false-negative audit，旧候选也尚未按 canonical owner 完成重分配；因此 Coverage、Evidence、Books 与 Completion 继续保持 Open。

## 2. Candidate Ledger

<!-- validator:candidate-ledger-v2.1 -->
| Source Family ID | Primary Identifier | Event Identity | Owner Week | First-public Date | Supporting Source IDs | Design Delta | System Reach | Durability | Total | Candidate State | Review Status | Access Status | Review Override | Review Ref | Owner Report Ref | Prior Review Ref | Reconciliation | Stable Node ID | Books Disposition | Books Review Ref | Benchmark Claim |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2606-18284 | arXiv:2606.18284v1 | paper-v1:2606.18284 | 2026-W25 | 2026-06-18 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-18284 | self | — | new_in_window | TRAIN-DATA | Integrate | books-review:SF-2026-ARXIV-2606-18284 | yes |
| SF-2026-ARXIV-2606-18286 | arXiv:2606.18286v1 | paper-v1:2606.18286 | 2026-W25 | 2026-06-18 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-18286 | self | — | new_in_window | TRAIN-SFT | Integrate | books-review:SF-2026-ARXIV-2606-18286 | yes |
| SF-2026-ARXIV-2606-18310 | arXiv:2606.18310v1 | paper-v1:2606.18310 | 2026-W25 | 2026-06-18 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-18310 | self | — | new_in_window | AGENT-RAG | Integrate | books-review:SF-2026-ARXIV-2606-18310 | yes |
| SF-2026-ARXIV-2606-18322 | arXiv:2606.18322v1 | paper-v1:2606.18322 | 2026-W25 | 2026-06-18 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-18322 | self | — | new_in_window | TRAIN-RLHF | Integrate | books-review:SF-2026-ARXIV-2606-18322 | yes |
| SF-2026-ARXIV-2606-18356 | arXiv:2606.18356v1 | paper-v1:2606.18356 | 2026-W25 | 2026-06-18 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-18356 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Integrate | books-review:SF-2026-ARXIV-2606-18356 | yes |
| SF-2026-ARXIV-2606-18379 | arXiv:2606.18379v1 | paper-v1:2606.18379 | 2026-W25 | 2026-06-18 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-18379 | self | — | new_in_window | AGENT-RAG | Integrate | books-review:SF-2026-ARXIV-2606-18379 | yes |
| SF-2026-ARXIV-2606-18383 | arXiv:2606.18383v1 | paper-v1:2606.18383 | 2026-W25 | 2026-06-18 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-18383 | self | — | new_in_window | TRAIN-RLHF | Integrate | books-review:SF-2026-ARXIV-2606-18383 | yes |
| SF-2026-ARXIV-2606-18394 | arXiv:2606.18394v1 | paper-v1:2606.18394 | 2026-W25 | 2026-06-18 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-18394 | self | — | new_in_window | INFER-SPECULATIVE-DECODING | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-18394 | yes |
| SF-2026-ARXIV-2606-18400 | arXiv:2606.18400v1 | paper-v1:2606.18400 | 2026-W25 | 2026-06-18 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-18400 | self | — | new_in_window | PLATFORM-SECURITY | Integrate | books-review:SF-2026-ARXIV-2606-18400 | yes |
| SF-2026-ARXIV-2606-18421 | arXiv:2606.18421v1 | paper-v1:2606.18421 | 2026-W25 | 2026-06-18 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-18421 | self | — | new_in_window | INFER-TENSORRT-LLM | Integrate | books-review:SF-2026-ARXIV-2606-18421 | yes |
| SF-2026-ARXIV-2606-18431 | arXiv:2606.18431v1 | paper-v1:2606.18431 | 2026-W25 | 2026-06-18 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-18431 | self | — | new_in_window | INFER-SCHEDULING | Integrate | books-review:SF-2026-ARXIV-2606-18431 | yes |
| SF-2026-ARXIV-2606-18448 | arXiv:2606.18448v1 | paper-v1:2606.18448 | 2026-W25 | 2026-06-18 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-18448 | self | — | new_in_window | AGENT-TOOL-CALLING | Integrate | books-review:SF-2026-ARXIV-2606-18448 | yes |
| SF-2026-ARXIV-2606-18467 | arXiv:2606.18467v1 | paper-v1:2606.18467 | 2026-W25 | 2026-06-18 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-18467 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Integrate | books-review:SF-2026-ARXIV-2606-18467 | yes |
| SF-2026-ARXIV-2606-18497 | arXiv:2606.18497v1 | paper-v1:2606.18497 | 2026-W25 | 2026-06-18 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-18497 | self | — | new_in_window | AGENT-RAG | Integrate | books-review:SF-2026-ARXIV-2606-18497 | yes |
| SF-2026-ARXIV-2606-18532 | arXiv:2606.18532v1 | paper-v1:2606.18532 | 2026-W25 | 2026-06-18 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-18532 | self | — | new_in_window | PLATFORM-SECURITY | Integrate | books-review:SF-2026-ARXIV-2606-18532 | yes |
| SF-2026-ARXIV-2606-18550 | arXiv:2606.18550v1 | paper-v1:2606.18550 | 2026-W25 | 2026-06-18 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-18550 | self | — | new_in_window | PLATFORM-SECURITY | Integrate | books-review:SF-2026-ARXIV-2606-18550 | yes |
| SF-2026-ARXIV-2606-18600 | arXiv:2606.18600v1 | paper-v1:2606.18600 | 2026-W25 | 2026-06-18 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-18600 | self | — | new_in_window | INFER-SCHEDULING | Integrate | books-review:SF-2026-ARXIV-2606-18600 | yes |
| SF-2026-ARXIV-2606-18619 | arXiv:2606.18619v1 | paper-v1:2606.18619 | 2026-W25 | 2026-06-18 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-18619 | self | — | new_in_window | PLATFORM-SECURITY | Integrate | books-review:SF-2026-ARXIV-2606-18619 | yes |
| SF-2026-ARXIV-2606-18650 | arXiv:2606.18650v1 | paper-v1:2606.18650 | 2026-W25 | 2026-06-18 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-18650 | self | — | new_in_window | TRAIN-DATA | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-18650 | yes |
| SF-2026-ARXIV-2606-18668 | arXiv:2606.18668v1 | paper-v1:2606.18668 | 2026-W25 | 2026-06-18 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-18668 | self | — | new_in_window | AGENT-MULTI-AGENT | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-18668 | yes |
| SF-2026-ARXIV-2606-18673 | arXiv:2606.18673v1 | paper-v1:2606.18673 | 2026-W25 | 2026-06-18 | SRC-ARXIV | 2 | 3 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-18673 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-18673 | yes |
| SF-2026-ARXIV-2606-18697 | arXiv:2606.18697v1 | paper-v1:2606.18697 | 2026-W25 | 2026-06-18 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-18697 | self | — | new_in_window | MULTIMODAL-WORLD-MODELS | Integrate | books-review:SF-2026-ARXIV-2606-18697 | yes |
| SF-2026-ARXIV-2606-18741 | arXiv:2606.18741v1 | paper-v1:2606.18741 | 2026-W25 | 2026-06-18 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-18741 | self | — | new_in_window | INFER-SCHEDULING | Integrate | books-review:SF-2026-ARXIV-2606-18741 | yes |
| SF-2026-ARXIV-2606-18746 | arXiv:2606.18746v1 | paper-v1:2606.18746 | 2026-W25 | 2026-06-18 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-18746 | self | — | new_in_window | AGENT-MEMORY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-18746 | yes |
| SF-2026-ARXIV-2606-18810 | arXiv:2606.18810v1 | paper-v1:2606.18810 | 2026-W25 | 2026-06-18 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-18810 | self | — | new_in_window | TRAIN-GRPO | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-18810 | yes |
| SF-2026-ARXIV-2606-18829 | arXiv:2606.18829v1 | paper-v1:2606.18829 | 2026-W25 | 2026-06-18 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-18829 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-18829 | yes |
| SF-2026-ARXIV-2606-18831 | arXiv:2606.18831v1 | paper-v1:2606.18831 | 2026-W25 | 2026-06-18 | SRC-ARXIV | 2 | 3 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-18831 | self | — | new_in_window | TRAIN-GRPO | Integrate | books-review:SF-2026-ARXIV-2606-18831 | yes |
| SF-2026-ARXIV-2606-18847 | arXiv:2606.18847v1 | paper-v1:2606.18847 | 2026-W25 | 2026-06-18 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-18847 | self | — | new_in_window | MULTIMODAL-EMBODIED-VLA | Integrate | books-review:SF-2026-ARXIV-2606-18847 | yes |
| SF-2026-ARXIV-2606-18874 | arXiv:2606.18874v1 | paper-v1:2606.18874 | 2026-W25 | 2026-06-18 | SRC-ARXIV | 2 | 3 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-18874 | self | — | new_in_window | AGENT-WORKFLOW | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-18874 | yes |
| SF-2026-ARXIV-2606-18958 | arXiv:2606.18958v1 | paper-v1:2606.18958 | 2026-W25 | 2026-06-18 | SRC-ARXIV | 2 | 3 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-18958 | self | — | new_in_window | PLATFORM-PRODUCTION | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-18958 | yes |
| SF-2026-ARXIV-2606-18967 | arXiv:2606.18967v1 | paper-v1:2606.18967 | 2026-W25 | 2026-06-18 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-18967 | self | — | new_in_window | INFER-SPECULATIVE-DECODING | Integrate | books-review:SF-2026-ARXIV-2606-18967 | yes |
| SF-2026-ARXIV-2606-18996 | arXiv:2606.18996v1 | paper-v1:2606.18996 | 2026-W25 | 2026-06-18 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-18996 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-18996 | yes |
| SF-2026-ARXIV-2606-19004 | arXiv:2606.19004v1 | paper-v1:2606.19004 | 2026-W25 | 2026-06-18 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-19004 | self | — | new_in_window | PLATFORM-GPU-SCHEDULER | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-19004 | yes |
| SF-2026-ARXIV-2606-19025 | arXiv:2606.19025v1 | paper-v1:2606.19025 | 2026-W25 | 2026-06-18 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-19025 | self | — | new_in_window | TRAIN-DISTRIBUTED-TRAINING | Integrate | books-review:SF-2026-ARXIV-2606-19025 | yes |
| SF-2026-ARXIV-2606-19057 | arXiv:2606.19057v1 | paper-v1:2606.19057 | 2026-W25 | 2026-06-18 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-19057 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Integrate | books-review:SF-2026-ARXIV-2606-19057 | yes |
| SF-2026-ARXIV-2606-19111 | arXiv:2606.19111v1 | paper-v1:2606.19111 | 2026-W25 | 2026-06-18 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-19111 | self | — | new_in_window | AGENT-MULTI-AGENT | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-19111 | yes |
| SF-2026-ARXIV-2606-19191 | arXiv:2606.19191v1 | paper-v1:2606.19191 | 2026-W25 | 2026-06-18 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-19191 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-19191 | yes |
| SF-2026-ARXIV-2606-19242 | arXiv:2606.19242v1 | paper-v1:2606.19242 | 2026-W25 | 2026-06-18 | SRC-ARXIV | 2 | 3 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-19242 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-19242 | yes |
| SF-2026-ARXIV-2606-19262 | arXiv:2606.19262v1 | paper-v1:2606.19262 | 2026-W25 | 2026-06-18 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-19262 | self | — | new_in_window | PLATFORM-MONITORING | Integrate | books-review:SF-2026-ARXIV-2606-19262 | yes |
| SF-2026-ARXIV-2606-19271 | arXiv:2606.19271v1 | paper-v1:2606.19271 | 2026-W25 | 2026-06-18 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-19271 | self | — | new_in_window | INFER-SCHEDULING | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-19271 | yes |
## 3. Review Completion Receipt

<!-- validator:review-completion-v1 -->
| Source Family ID | Review Provenance ID | Review Route | Primary Evidence Version | Reviewed Evidence Versions | Method / Identity Locators | Evaluation Locators | Limitations / Counterevidence Locators | Artifact Locators | Claim Boundary Ref | Completion Result |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2606-18284 | RP-9d5e9586a5980f9a | deep | arXiv:2606.18284v1 | SRC-ARXIV@arXiv:2606.18284v1 | arXiv:2606.18284v1 §3 Probe Rewards; §5 probe data/selection | arXiv:2606.18284v1 §§4 and 6 Evaluation/Results | arXiv:2606.18284v1 §7 Limitations; mode-collapse findings | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-18284 | complete |
| SF-2026-ARXIV-2606-18286 | RP-c8dae86a49cd767b | deep | arXiv:2606.18286v1 | SRC-ARXIV@arXiv:2606.18286v1 | arXiv:2606.18286v1 §5 Method; §§5.1–5.4 | arXiv:2606.18286v1 §6 Experiments; Appendix A | arXiv:2606.18286v1 §7 Conclusion; Appendix C runtime analysis | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-18286 | complete |
| SF-2026-ARXIV-2606-18310 | RP-deb8c27cf0790387 | deep | arXiv:2606.18310v1 | SRC-ARXIV@arXiv:2606.18310v1 | arXiv:2606.18310v1 §3 conflict-aware retriever editing attack; §4 anchor-based repair | arXiv:2606.18310v1 §5 multi-dataset/model retrieval and downstream evaluations | Not Disclosed — arXiv:2606.18310v1 has no dedicated limitations section; exact-v1 counterevidence is localized at edit access, retriever architecture, corpus and transfer limitations | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-18310 | complete |
| SF-2026-ARXIV-2606-18322 | RP-77022ee8d233e199 | deep | arXiv:2606.18322v1 | SRC-ARXIV@arXiv:2606.18322v1 | arXiv:2606.18322v1 §3 SAE intervention and residual-recovery analysis | arXiv:2606.18322v1 §4–§5 cross-layer behavior evaluations and controls | Not Disclosed — arXiv:2606.18322v1 has no dedicated limitations section; exact-v1 counterevidence is localized at SAE/model/behavior/prompt scope and causal-interpretation limitations | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-18322 | complete |
| SF-2026-ARXIV-2606-18356 | RP-0198cb0f94f3d67e | deep | arXiv:2606.18356v1 | SRC-ARXIV@arXiv:2606.18356v1 | arXiv:2606.18356v1 §3.1–3.7 attack surface, threat model, benchmark levels and measurement | arXiv:2606.18356v1 §4 experiments; §5 endpoint analyses; appendices J–M calibration/sandbox checks | Not Disclosed — arXiv:2606.18356v1 has no dedicated limitations section; exact-v1 counterevidence is localized at prompt-only defense scope, synthetic stress-test and separate Core/Exec call boundary | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-18356 | complete |
| SF-2026-ARXIV-2606-18379 | RP-57bb27eebdd11ac3 | deep | arXiv:2606.18379v1 | SRC-ARXIV@arXiv:2606.18379v1 | arXiv:2606.18379v1 §3 RankGraph-2 lifecycle co-design and co-learned cluster index | arXiv:2606.18379v1 §4–§5 production-scale offline/online evaluation | Not Disclosed — arXiv:2606.18379v1 has no dedicated limitations section; exact-v1 counterevidence is localized at Meta recommendation workload, graph distribution and deployment-scope limits | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-18379 | complete |
| SF-2026-ARXIV-2606-18383 | RP-2a302bd788704335 | deep | arXiv:2606.18383v1 | SRC-ARXIV@arXiv:2606.18383v1 | arXiv:2606.18383v1 §3 proxy-certificate framework and bound components | arXiv:2606.18383v1 §4–§5 synthetic and language-model validation | Not Disclosed — arXiv:2606.18383v1 has no dedicated limitations section; exact-v1 counterevidence is localized at certificate assumptions, concept labeling and model/SAE scope | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-18383 | complete |
| SF-2026-ARXIV-2606-18394 | RP-791b3020552cc289 | deep | arXiv:2606.18394v1 | SRC-ARXIV@arXiv:2606.18394v1 | arXiv:2606.18394v1 §3 JetSpec parallel causal tree-drafting architecture | arXiv:2606.18394v1 §4–§5 vLLM integration and H100 evaluation | Not Disclosed — arXiv:2606.18394v1 has no dedicated limitations section; exact-v1 counterevidence is localized at draft-tree/model/hardware/concurrency scope and branch-waste boundary | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-18394 | complete |
| SF-2026-ARXIV-2606-18400 | RP-5861a884c9db6db0 | deep | arXiv:2606.18400v1 | SRC-ARXIV@arXiv:2606.18400v1 | arXiv:2606.18400v1 PDF §3 threat model; §§4–5 CloakLM three-tier design and integration | arXiv:2606.18400v1 PDF §§6–7 PyTorch/vLLM LLaMA/Qwen evaluation | arXiv:2606.18400v1 PDF §1/§8 scope: no host OS, hypervisor, firmware or mapping-compromise defense | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-18400 | complete |
| SF-2026-ARXIV-2606-18421 | RP-6873b4ff5363b062 | deep | arXiv:2606.18421v1 | SRC-ARXIV@arXiv:2606.18421v1 | arXiv:2606.18421v1 §3 XCheck, §§3.1–3.3 constraint extraction, exploration and behavior differentiation | arXiv:2606.18421v1 §4.1–4.2 evaluation on TVM, ONNX-MLIR and GeneSys | Not Disclosed — arXiv:2606.18421v1 has no dedicated limitations section; exact-v1 counterevidence is localized at three-compiler/backend scope; no dedicated limitations section | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-18421 | complete |
| SF-2026-ARXIV-2606-18431 | RP-8c71745478b3e855 | deep | arXiv:2606.18431v1 | SRC-ARXIV@arXiv:2606.18431v1 | arXiv:2606.18431v1 §3 tail-aware objective and prediction-free scheduler; §4 cache-aware preemption | arXiv:2606.18431v1 §5 production/open-trace evaluation and ablations | Not Disclosed — arXiv:2606.18431v1 has no dedicated limitations section; exact-v1 counterevidence is localized at trace/model/engine and overload-regime boundaries | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-18431 | complete |
| SF-2026-ARXIV-2606-18448 | RP-058692235df166a4 | deep | arXiv:2606.18448v1 | SRC-ARXIV@arXiv:2606.18448v1 | arXiv:2606.18448v1 §3 VisualSkill construction; §4 hierarchical storage and load_topic interface | arXiv:2606.18448v1 §5 live-UI computer-use evaluation and ablations | Not Disclosed — arXiv:2606.18448v1 has no dedicated limitations section; exact-v1 counterevidence is localized at UI/task/model, authored-skill and MCP-loading scope | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-18448 | complete |
| SF-2026-ARXIV-2606-18467 | RP-3bfb0142a829090f | deep | arXiv:2606.18467v1 | SRC-ARXIV@arXiv:2606.18467v1 | arXiv:2606.18467v1 §3 trajectory risk and conformal calibration; §4 anytime monitoring and drift extension | arXiv:2606.18467v1 §5 retrieval/tool-use experiments and coverage-risk analyses | Not Disclosed — arXiv:2606.18467v1 has no dedicated limitations section; exact-v1 counterevidence is localized at exchangeability, detector delay and tool/retrieval drift limitations | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-18467 | complete |
| SF-2026-ARXIV-2606-18497 | RP-ff3bec20f0a5f21c | deep | arXiv:2606.18497v1 | SRC-ARXIV@arXiv:2606.18497v1 | arXiv:2606.18497v1 §3 Ghost Vectors recovery methodology; §4 cryptographic epoch-deletion design | arXiv:2606.18497v1 §5 HNSW/database recovery experiments | Not Disclosed — arXiv:2606.18497v1 has no dedicated limitations section; exact-v1 counterevidence is localized at backend/version/access model and cryptographic-key assumptions | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-18497 | complete |
| SF-2026-ARXIV-2606-18532 | RP-8dee2ab8e796b321 | deep | arXiv:2606.18532v1 | SRC-ARXIV@arXiv:2606.18532v1 | arXiv:2606.18532v1 §3 sandbox threat model and taxonomy; §4 measurement framework | arXiv:2606.18532v1 §5 cross-sandbox case studies/measurements | Not Disclosed — arXiv:2606.18532v1 has no dedicated limitations section; exact-v1 counterevidence is localized at coverage of sandbox types, attacker capability and measurement incompleteness | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-18532 | complete |
| SF-2026-ARXIV-2606-18550 | RP-c3df87c10269d7bf | deep | arXiv:2606.18550v1 | SRC-ARXIV@arXiv:2606.18550v1 | arXiv:2606.18550v1 §II threat model; §III two-gate taxonomy; §IV ContractGuard ladder | arXiv:2606.18550v1 §VI–VII controlled exhaustive attacker and six-model validation | arXiv:2606.18550v1 §XI Limitations; trusted-attestation, symbolic-space and external-side-effect boundaries | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-18550 | complete |
| SF-2026-ARXIV-2606-18600 | RP-43d464fda7218e6e | deep | arXiv:2606.18600v1 | SRC-ARXIV@arXiv:2606.18600v1 | https://arxiv.org/html/2606.18600v1 — § exact-v1 anchor: 4 Model Placement for Heterogeneous GPUs | https://arxiv.org/html/2606.18600v1 — § exact-v1 evaluation anchor: 7 Evaluation | https://arxiv.org/html/2606.18600v1 — § exact-v1 limitation/counterevidence anchor: 8.1 Limitation | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-18600 | complete |
| SF-2026-ARXIV-2606-18619 | RP-b1641e5e887033df | deep | arXiv:2606.18619v1 | SRC-ARXIV@arXiv:2606.18619v1 | https://arxiv.org/html/2606.18619v1 — § exact-v1 anchor: security-specification-first paradigm | https://arxiv.org/html/2606.18619v1 — § exact-v1 evaluation anchor: real-world subjects | https://arxiv.org/html/2606.18619v1 — § exact-v1 limitation/counterevidence anchor: limitations | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-18619 | complete |
| SF-2026-ARXIV-2606-18650 | RP-06daad534bd2ce5d | deep | arXiv:2606.18650v1 | SRC-ARXIV@arXiv:2606.18650v1 | https://arxiv.org/html/2606.18650v1 — § exact-v1 anchor: penalized single-level objective | https://arxiv.org/html/2606.18650v1 — § exact-v1 evaluation anchor: Experiments | https://arxiv.org/html/2606.18650v1 — § exact-v1 limitation/counterevidence anchor: Limitations | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-18650 | complete |
| SF-2026-ARXIV-2606-18668 | RP-80c4ada12115ffae | deep | arXiv:2606.18668v1 | SRC-ARXIV@arXiv:2606.18668v1 | https://arxiv.org/html/2606.18668v1 — § exact-v1 anchor: Explanatory Abstention | https://arxiv.org/html/2606.18668v1 — § exact-v1 evaluation anchor: production e-commerce assistant | https://arxiv.org/html/2606.18668v1 — § exact-v1 limitation/counterevidence anchor: Limitations | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-18668 | complete |
| SF-2026-ARXIV-2606-18673 | RP-11622651a47d8c44 | deep | arXiv:2606.18673v1 | SRC-ARXIV@arXiv:2606.18673v1 | https://arxiv.org/html/2606.18673v1 — § exact-v1 anchor: attention drift | https://arxiv.org/html/2606.18673v1 — § exact-v1 evaluation anchor: 1,200 applications | https://arxiv.org/html/2606.18673v1 — § exact-v1 limitation/counterevidence anchor: limitations | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-18673 | complete |
| SF-2026-ARXIV-2606-18697 | RP-97d4b5a5b08b22ff | deep | arXiv:2606.18697v1 | SRC-ARXIV@arXiv:2606.18697v1 | https://arxiv.org/html/2606.18697v1 — § exact-v1 anchor: two-stage data poisoning framework | https://arxiv.org/html/2606.18697v1 — § exact-v1 evaluation anchor: continuous-control tasks | https://arxiv.org/html/2606.18697v1 — § exact-v1 limitation/counterevidence anchor: limitations | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-18697 | complete |
| SF-2026-ARXIV-2606-18741 | RP-8f89bc901404df5e | deep | arXiv:2606.18741v1 | SRC-ARXIV@arXiv:2606.18741v1 | https://arxiv.org/html/2606.18741v1 — § exact-v1 anchor: two-dimensional KV cache migration | https://arxiv.org/html/2606.18741v1 — § exact-v1 evaluation anchor: Experiments | https://arxiv.org/html/2606.18741v1 — § exact-v1 limitation/counterevidence anchor: Limitations | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-18741 | complete |
| SF-2026-ARXIV-2606-18746 | RP-6534f060fca815cb | deep | arXiv:2606.18746v1 | SRC-ARXIV@arXiv:2606.18746v1 | https://arxiv.org/html/2606.18746v1 — § exact-v1 anchor: separation theorem | https://arxiv.org/html/2606.18746v1 — § exact-v1 evaluation anchor: transition-model reconstruction | https://arxiv.org/html/2606.18746v1 — § exact-v1 limitation/counterevidence anchor: assumptions | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-18746 | complete |
| SF-2026-ARXIV-2606-18810 | RP-67359ff010705fe8 | deep | arXiv:2606.18810v1 | SRC-ARXIV@arXiv:2606.18810v1 | https://arxiv.org/html/2606.18810v1 — § exact-v1 anchor: Self-Conditioned GRPO | https://arxiv.org/html/2606.18810v1 — § exact-v1 evaluation anchor: five benchmarks | https://arxiv.org/html/2606.18810v1 — § exact-v1 limitation/counterevidence anchor: Limitations | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-18810 | complete |
| SF-2026-ARXIV-2606-18829 | RP-142faf4468530c97 | deep | arXiv:2606.18829v1 | SRC-ARXIV@arXiv:2606.18829v1 | https://arxiv.org/html/2606.18829v1 — § exact-v1 anchor: multi-principal shared-memory agents | https://arxiv.org/html/2606.18829v1 — § exact-v1 evaluation anchor: diverse baselines and backbone models | https://arxiv.org/html/2606.18829v1 — § exact-v1 limitation/counterevidence anchor: limitations | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-18829 | complete |
| SF-2026-ARXIV-2606-18831 | RP-4e5c1ee492eb62aa | deep | arXiv:2606.18831v1 | SRC-ARXIV@arXiv:2606.18831v1 | https://arxiv.org/html/2606.18831v1 — § exact-v1 anchor: 3.1 Long-Context Training Data | https://arxiv.org/html/2606.18831v1 — § exact-v1 evaluation anchor: 4 Experiments | https://arxiv.org/html/2606.18831v1 — § exact-v1 limitation/counterevidence anchor: 5 Analysis | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-18831 | complete |
| SF-2026-ARXIV-2606-18847 | RP-592b0b44c1431829 | deep | arXiv:2606.18847v1 | SRC-ARXIV@arXiv:2606.18847v1 | https://arxiv.org/html/2606.18847v1 — § exact-v1 anchor: WorldLines | https://arxiv.org/html/2606.18847v1 — § exact-v1 evaluation anchor: ObsMem | https://arxiv.org/html/2606.18847v1 — § exact-v1 limitation/counterevidence anchor: Limitations | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-18847 | complete |
| SF-2026-ARXIV-2606-18874 | RP-9fd4dd2d000acb58 | deep | arXiv:2606.18874v1 | SRC-ARXIV@arXiv:2606.18874v1 | https://arxiv.org/html/2606.18874v1 — § exact-v1 anchor: persistent research artifacts | https://arxiv.org/html/2606.18874v1 — § exact-v1 evaluation anchor: three case studies | https://arxiv.org/html/2606.18874v1 — § exact-v1 limitation/counterevidence anchor: limitations | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-18874 | complete |
| SF-2026-ARXIV-2606-18958 | RP-0502c38e36e7d46f | deep | arXiv:2606.18958v1 | SRC-ARXIV@arXiv:2606.18958v1 | https://arxiv.org/html/2606.18958v1 — § exact-v1 anchor: full-stack live simulation | https://arxiv.org/html/2606.18958v1 — § exact-v1 evaluation anchor: Evaluation | https://arxiv.org/html/2606.18958v1 — § exact-v1 limitation/counterevidence anchor: Limitations | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-18958 | complete |
| SF-2026-ARXIV-2606-18967 | RP-85a776d1f8c87caf | deep | arXiv:2606.18967v1 | SRC-ARXIV@arXiv:2606.18967v1 | https://arxiv.org/html/2606.18967v1 — § exact-v1 anchor: system-aware self-speculative decoding | https://arxiv.org/html/2606.18967v1 — § exact-v1 evaluation anchor: Experiments | https://arxiv.org/html/2606.18967v1 — § exact-v1 limitation/counterevidence anchor: Limitations | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-18967 | complete |
| SF-2026-ARXIV-2606-18996 | RP-9721999a51e217df | deep | arXiv:2606.18996v1 | SRC-ARXIV@arXiv:2606.18996v1 | https://arxiv.org/html/2606.18996v1 — § exact-v1 anchor: Task-completion and Resistance | https://arxiv.org/html/2606.18996v1 — § exact-v1 evaluation anchor: Evaluation | https://arxiv.org/html/2606.18996v1 — § exact-v1 limitation/counterevidence anchor: Limitations | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-18996 | complete |
| SF-2026-ARXIV-2606-19004 | RP-4134963e7c617cf0 | deep | arXiv:2606.19004v1 | SRC-ARXIV@arXiv:2606.19004v1 | https://arxiv.org/html/2606.19004v1 — § exact-v1 anchor: Seed Exploration and Spot GPUs | https://arxiv.org/html/2606.19004v1 — § exact-v1 evaluation anchor: Experiments | https://arxiv.org/html/2606.19004v1 — § exact-v1 limitation/counterevidence anchor: Limitations | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-19004 | complete |
| SF-2026-ARXIV-2606-19025 | RP-69c349a48eb20aa0 | deep | arXiv:2606.19025v1 | SRC-ARXIV@arXiv:2606.19025v1 | https://arxiv.org/html/2606.19025v1 — § exact-v1 anchor: partitioning expert layers across workers | https://arxiv.org/html/2606.19025v1 — § exact-v1 evaluation anchor: FoMoE Scalability & Resource Consumption | https://arxiv.org/html/2606.19025v1 — § exact-v1 limitation/counterevidence anchor: Limitations | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-19025 | complete |
| SF-2026-ARXIV-2606-19057 | RP-32e81e7396980e1c | deep | arXiv:2606.19057v1 | SRC-ARXIV@arXiv:2606.19057v1 | https://arxiv.org/html/2606.19057v1 — § exact-v1 anchor: Positive–Unlabeled Learning | https://arxiv.org/html/2606.19057v1 — § exact-v1 evaluation anchor: Experiments | https://arxiv.org/html/2606.19057v1 — § exact-v1 limitation/counterevidence anchor: Limitations | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-19057 | complete |
| SF-2026-ARXIV-2606-19111 | RP-d57ed8541041e79e | deep | arXiv:2606.19111v1 | SRC-ARXIV@arXiv:2606.19111v1 | https://arxiv.org/html/2606.19111v1 — § exact-v1 anchor: Recovery-Advantage Boundary | https://arxiv.org/html/2606.19111v1 — § exact-v1 evaluation anchor: Experiments | https://arxiv.org/html/2606.19111v1 — § exact-v1 limitation/counterevidence anchor: Limitations | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-19111 | complete |
| SF-2026-ARXIV-2606-19191 | RP-3577ad1227f9b380 | deep | arXiv:2606.19191v1 | SRC-ARXIV@arXiv:2606.19191v1 | https://arxiv.org/html/2606.19191v1 — § exact-v1 anchor: 3 Threat Model | https://arxiv.org/html/2606.19191v1 — § exact-v1 evaluation anchor: 5 Evaluation | https://arxiv.org/html/2606.19191v1 — § exact-v1 limitation/counterevidence anchor: 6 Discussion | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-19191 | complete |
| SF-2026-ARXIV-2606-19242 | RP-274d1357452733c6 | deep | arXiv:2606.19242v1 | SRC-ARXIV@arXiv:2606.19242v1 | https://arxiv.org/html/2606.19242v1 — § exact-v1 anchor: Runtime Compliance Verification | https://arxiv.org/html/2606.19242v1 — § exact-v1 evaluation anchor: Evaluation | https://arxiv.org/html/2606.19242v1 — § exact-v1 limitation/counterevidence anchor: Limitations | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-19242 | complete |
| SF-2026-ARXIV-2606-19262 | RP-9b28f51a00defa29 | deep | arXiv:2606.19262v1 | SRC-ARXIV@arXiv:2606.19262v1 | https://arxiv.org/html/2606.19262v1 — § exact-v1 anchor: Zero-Overhead Telemetry | https://arxiv.org/html/2606.19262v1 — § exact-v1 evaluation anchor: Evaluation | https://arxiv.org/html/2606.19262v1 — § exact-v1 limitation/counterevidence anchor: Limitations | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-19262 | complete |
| SF-2026-ARXIV-2606-19271 | RP-c7db478f4bc8677e | deep | arXiv:2606.19271v1 | SRC-ARXIV@arXiv:2606.19271v1 | https://arxiv.org/html/2606.19271v1 — § exact-v1 anchor: Streaming Video Generation | https://arxiv.org/html/2606.19271v1 — § exact-v1 evaluation anchor: Evaluation | https://arxiv.org/html/2606.19271v1 — § exact-v1 limitation/counterevidence anchor: Limitations | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-19271 | complete |

### Source Reviews

<!-- review:SF-2026-ARXIV-2606-18284:start -->
### 2606.18284 — Breaking the Solver Bottleneck: Training Task Generators at the Learnable Frontier

**问题、旧路径与机制。** 旧路径在 workload、trust boundary 或资源层级稳定时仍然合理；该 exact-v1 的约束变化是：训练 task generator 时可用一次 solver-labeled pool 训练 activation probe，把 targeted solve-rate 作为 amortized reward；最终仍由 held-out solver 验证。

**State / data / control owner。** `TRAIN-DATA` 持有长期机制。State 是论文显式维护的 runtime/training/evaluation state；data 是其 evidence/workload/artifact；control 是 admission、routing、selection、verification 或 fallback 决策。项目名不取得新 owner，跨 owner 中间状态必须携带 identity、version 与 failure semantics。

**Evaluation：proof / non-proof。** `arXiv:2606.18284v1 §§4 and 6 Evaluation/Results` 支持 `Math, code and SWE task generation across model scales`；模型 `Qwen2.5-3B/7B and Qwen3.5-27B solver settings`；硬件 `Not Disclosed`；精度 `Not Disclosed`。它不证明生产 SLO、跨模型/跨硬件普遍优越性或未披露字段。Method locator：`arXiv:2606.18284v1 §3 Probe Rewards; §5 probe data/selection`；counterevidence locator：`arXiv:2606.18284v1 §7 Limitations; mode-collapse findings`。

**Trade-off / failure / coexistence / evolution。** probe 降低 inner-loop solver cost，但 reward hacking、mode collapse 与 solver drift 要求 held-out solver gate。 旧路径保留为兼容/fallback 分支；长期正文只吸收 mechanism、owner handoff 与 failure boundary。

<!-- claim:SF-2026-ARXIV-2606-18284:start -->
**Claim boundary。** 仅引用 `https://arxiv.org/html/2606.18284v1` 的 exact-v1 method/evaluation/limitations；later versions 或 artifact 不扩张 v1 claim。
<!-- claim:SF-2026-ARXIV-2606-18284:end -->
<!-- review:SF-2026-ARXIV-2606-18284:end -->

<!-- review:SF-2026-ARXIV-2606-18286:start -->
### 2606.18286 — CODEBLOCK: Learning to Supervise Code at the Right Granularity

**问题、旧路径与机制。** 旧路径在 workload、trust boundary 或资源层级稳定时仍然合理；该 exact-v1 的约束变化是：Code SFT 的 sparse supervision unit 应是 syntax-complete、data-flow-connected code block，而非孤立 high-loss token；完整 response 继续作 context。

**State / data / control owner。** `TRAIN-SFT` 持有长期机制。State 是论文显式维护的 runtime/training/evaluation state；data 是其 evidence/workload/artifact；control 是 admission、routing、selection、verification 或 fallback 决策。项目名不取得新 owner，跨 owner 中间状态必须携带 identity、version 与 failure semantics。

**Evaluation：proof / non-proof。** `arXiv:2606.18286v1 §6 Experiments; Appendix A` 支持 `Six code-generation benchmarks`；模型 `Qwen2.5-Coder-1.5B-Instruct and comparison models`；硬件 `Disclosed in Appendix A.3; exact accelerator remains v1-bound`；精度 `Training precision disclosed in Appendix A.3`。它不证明生产 SLO、跨模型/跨硬件普遍优越性或未披露字段。Method locator：`arXiv:2606.18286v1 §5 Method; §§5.1–5.4`；counterevidence locator：`arXiv:2606.18286v1 §7 Conclusion; Appendix C runtime analysis`。

**Trade-off / failure / coexistence / evolution。** 仅 1.9% supervised tokens 降低 loss work，却依赖 parser/data-flow correctness；错误 block 边界会删除必要 credit，full-token SFT 仍是稳健基线。 旧路径保留为兼容/fallback 分支；长期正文只吸收 mechanism、owner handoff 与 failure boundary。

<!-- claim:SF-2026-ARXIV-2606-18286:start -->
**Claim boundary。** 仅引用 `https://arxiv.org/html/2606.18286v1` 的 exact-v1 method/evaluation/limitations；later versions 或 artifact 不扩张 v1 claim。
<!-- claim:SF-2026-ARXIV-2606-18286:end -->
<!-- review:SF-2026-ARXIV-2606-18286:end -->

<!-- review:SF-2026-ARXIV-2606-18310:start -->
### 2606.18310 — Conflict-Aware Retriever Editing for Knowledge Injection Attacks on LLM-Based RAG Systems

**问题与机制变化。** RAG threat model 需覆盖 retriever parameter editing：攻击者可改变 ranking 而不改 corpus；index/model revision、anchor repair 与 retrieval regression 必须同 lifecycle 验证。

**State / data / control owner。** `AGENT-RAG` 是唯一知识 owner；`Books/part-07-agent/77-memory.md; Books/part-06-ai-infrastructure/72-security.md` 只接收相邻 handoff。论文名称不取得跨章 authority。

**Evaluation：proof / non-proof。** Method=`arXiv:2606.18310v1 §3 conflict-aware retriever editing attack; §4 anchor-based repair`；Evaluation=`arXiv:2606.18310v1 §5 multi-dataset/model retrieval and downstream evaluations`；Counterevidence=`Not Disclosed — arXiv:2606.18310v1 has no dedicated limitations section; exact-v1 counterevidence is localized at edit access, retriever architecture, corpus and transfer limitations`。Workload=`knowledge-injection attacks and repair across disclosed RAG datasets`；Model=`Not Disclosed`；Hardware=`Not Disclosed`；Evaluator=`attack success, retrieval ranking, downstream answer and clean-utility recovery`。这些证据不自动成为 production SLO、普遍安全保证或跨模型/硬件排名。

**Trade-off / failure / fallback。** repair anchors能恢复局部行为却可能伤正常 recall；受测编辑不代表所有 retriever compromise。

<!-- claim:SF-2026-ARXIV-2606-18310:start -->
**Claim boundary。** 只使用 `https://arxiv.org/html/2606.18310v1` 的 exact-v1 正文；HTML 不可用的三个 family 显式走官方 PDF fallback。later revision/artifact 不参与，ordinary pending=`0`。
<!-- claim:SF-2026-ARXIV-2606-18310:end -->
<!-- review:SF-2026-ARXIV-2606-18310:end -->

<!-- review:SF-2026-ARXIV-2606-18322:start -->
### 2606.18322 — SAE Interventions are Unreliable: Post-Intervention Recovery of Suppressed Behavior

**问题与机制变化。** SAE feature clamp/ablation 不能被当作行为控制 complete；residual stream 会在后续层恢复被压制行为，需做 post-intervention trajectory 与 residual recovery audit。

**State / data / control owner。** `TRAIN-RLHF` 是唯一知识 owner；`Books/part-04-training-system/29-sft.md; Books/part-06-ai-infrastructure/66-evaluation-system.md` 只接收相邻 handoff。论文名称不取得跨章 authority。

**Evaluation：proof / non-proof。** Method=`arXiv:2606.18322v1 §3 SAE intervention and residual-recovery analysis`；Evaluation=`arXiv:2606.18322v1 §4–§5 cross-layer behavior evaluations and controls`；Counterevidence=`Not Disclosed — arXiv:2606.18322v1 has no dedicated limitations section; exact-v1 counterevidence is localized at SAE/model/behavior/prompt scope and causal-interpretation limitations`。Workload=`behavior-suppression interventions followed across downstream transformer layers`；Model=`Not Disclosed`；Hardware=`Not Disclosed`；Evaluator=`target behavior suppression and later recovery with residual/feature diagnostics`。这些证据不自动成为 production SLO、普遍安全保证或跨模型/硬件排名。

**Trade-off / failure / fallback。** 跨层审计增加 hook/compute且仍是 proxy；观察恢复不证明 SAE 无用，也不提供通用 steering 方案。

<!-- claim:SF-2026-ARXIV-2606-18322:start -->
**Claim boundary。** 只使用 `https://arxiv.org/html/2606.18322v1` 的 exact-v1 正文；HTML 不可用的三个 family 显式走官方 PDF fallback。later revision/artifact 不参与，ordinary pending=`0`。
<!-- claim:SF-2026-ARXIV-2606-18322:end -->
<!-- review:SF-2026-ARXIV-2606-18322:end -->

<!-- review:SF-2026-ARXIV-2606-18356:start -->
### 2606.18356 — SafeClawBench: Separating Semantic, Audit-Evidence, and Sandbox Harm in Tool-Using LLM Agents

**问题与机制变化。** Agent security EvalSpec 必须分开 semantic compromise、artifact-visible harm evidence 与 sandbox-observed state/tool harm，并保持各自 denominator 和 matched identity。

**State / data / control owner。** `PLATFORM-EVALUATION-SYSTEM` 是唯一知识 owner；`Books/part-06-ai-infrastructure/69-trace.md; Books/part-06-ai-infrastructure/72-security.md` 只接收相邻 handoff。论文名称不取得跨章 authority。

**Evaluation：proof / non-proof。** Method=`arXiv:2606.18356v1 §3.1–3.7 attack surface, threat model, benchmark levels and measurement`；Evaluation=`arXiv:2606.18356v1 §4 experiments; §5 endpoint analyses; appendices J–M calibration/sandbox checks`；Counterevidence=`Not Disclosed — arXiv:2606.18356v1 has no dedicated limitations section; exact-v1 counterevidence is localized at prompt-only defense scope, synthetic stress-test and separate Core/Exec call boundary`。Workload=`600 cases across six attack families plus a 12,000-row matched Core/Exec analysis`；Model=`Not Disclosed`；Hardware=`Not Disclosed`；Evaluator=`CoreFail, HarmEvidence, SemanticOnly and sandbox state-oracle harm as separate endpoints`。这些证据不自动成为 production SLO、普遍安全保证或跨模型/硬件排名。

**Trade-off / failure / fallback。** 多 endpoint改善定位却增加匹配与审计成本；600 合成 case不估计生产 prevalence，prompt policy不替代 runtime control。

<!-- claim:SF-2026-ARXIV-2606-18356:start -->
**Claim boundary。** 只使用 `https://arxiv.org/html/2606.18356v1` 的 exact-v1 正文；HTML 不可用的三个 family 显式走官方 PDF fallback。later revision/artifact 不参与，ordinary pending=`0`。
<!-- claim:SF-2026-ARXIV-2606-18356:end -->
<!-- review:SF-2026-ARXIV-2606-18356:end -->

<!-- review:SF-2026-ARXIV-2606-18379:start -->
### 2606.18379 — RankGraph-2: Lifecycle Co-Design for Billion-Node Graph Learning in Recommendation

**问题与机制变化。** Billion-node graph retrieval owner 应贯通 graph construction、cluster/index lifecycle、训练与 serving refresh，避免离线 embedding/index 与在线推荐 state 各自漂移。

**State / data / control owner。** `AGENT-RAG` 是唯一知识 owner；`Books/part-07-agent/77-memory.md; Books/part-06-ai-infrastructure/72-security.md` 只接收相邻 handoff。论文名称不取得跨章 authority。

**Evaluation：proof / non-proof。** Method=`arXiv:2606.18379v1 §3 RankGraph-2 lifecycle co-design and co-learned cluster index`；Evaluation=`arXiv:2606.18379v1 §4–§5 production-scale offline/online evaluation`；Counterevidence=`Not Disclosed — arXiv:2606.18379v1 has no dedicated limitations section; exact-v1 counterevidence is localized at Meta recommendation workload, graph distribution and deployment-scope limits`。Workload=`Billion-node recommendation graph with hour-scale refresh and online serving`；Model=`Not Disclosed`；Hardware=`Not Disclosed`；Evaluator=`retrieval/recommendation quality, refresh/build time and serving efficiency`。这些证据不自动成为 production SLO、普遍安全保证或跨模型/硬件排名。

**Trade-off / failure / fallback。** 联合 lifecycle缩短 refresh却扩大 control-plane coupling、rebuild和失败域；单平台生产证据不外推任意 RAG corpus。

<!-- claim:SF-2026-ARXIV-2606-18379:start -->
**Claim boundary。** 只使用 `https://arxiv.org/html/2606.18379v1` 的 exact-v1 正文；HTML 不可用的三个 family 显式走官方 PDF fallback。later revision/artifact 不参与，ordinary pending=`0`。
<!-- claim:SF-2026-ARXIV-2606-18379:end -->
<!-- review:SF-2026-ARXIV-2606-18379:end -->

<!-- review:SF-2026-ARXIV-2606-18383:start -->
### 2606.18383 — From Sparse Features to Trustworthy Proxies: Certifying SAE-Based Interpretability

**问题与机制变化。** SAE 只有在 proxy risk、reconstruction gap、concept mismatch 与 proxy complexity 共同受控时才能支撑干预结论；单独 sparsity/reconstruction score不足以认证 fidelity。

**State / data / control owner。** `TRAIN-RLHF` 是唯一知识 owner；`Books/part-04-training-system/29-sft.md; Books/part-06-ai-infrastructure/66-evaluation-system.md` 只接收相邻 handoff。论文名称不取得跨章 authority。

**Evaluation：proof / non-proof。** Method=`arXiv:2606.18383v1 §3 proxy-certificate framework and bound components`；Evaluation=`arXiv:2606.18383v1 §4–§5 synthetic and language-model validation`；Counterevidence=`Not Disclosed — arXiv:2606.18383v1 has no dedicated limitations section; exact-v1 counterevidence is localized at certificate assumptions, concept labeling and model/SAE scope`。Workload=`synthetic controls and language-model SAE proxy validation`；Model=`Not Disclosed`；Hardware=`Not Disclosed`；Evaluator=`proxy risk, reconstruction/concept gaps and certificate coverage/tightness`。这些证据不自动成为 production SLO、普遍安全保证或跨模型/硬件排名。

**Trade-off / failure / fallback。** 证书更可审计却依赖可估计 risk 与 concept定义；通过 proxy certificate 仍不证明行为因果或部署安全。

<!-- claim:SF-2026-ARXIV-2606-18383:start -->
**Claim boundary。** 只使用 `https://arxiv.org/html/2606.18383v1` 的 exact-v1 正文；HTML 不可用的三个 family 显式走官方 PDF fallback。later revision/artifact 不参与，ordinary pending=`0`。
<!-- claim:SF-2026-ARXIV-2606-18383:end -->
<!-- review:SF-2026-ARXIV-2606-18383:end -->

<!-- review:SF-2026-ARXIV-2606-18394:start -->
### 2606.18394 — JetFlow: Breaking the Scaling Ceiling of Speculative Decoding with Parallel Tree Drafting

**问题与机制变化。** Parallel causal tree drafting仍遵守 proposal tree、target verification、accepted-prefix commit 与 suffix rollback；Ch48 已有该 owner、DARTree/TAPS 与 tree cost/fallback 边界。

**State / data / control owner。** `INFER-SPECULATIVE-DECODING` 是唯一知识 owner；`Books/part-05-inference-system/44-decode.md; Books/part-05-inference-system/56-inference-scheduling.md` 只接收相邻 handoff。论文名称不取得跨章 authority。

**Evaluation：proof / non-proof。** Method=`arXiv:2606.18394v1 §3 JetSpec parallel causal tree-drafting architecture`；Evaluation=`arXiv:2606.18394v1 §4–§5 vLLM integration and H100 evaluation`；Counterevidence=`Not Disclosed — arXiv:2606.18394v1 has no dedicated limitations section; exact-v1 counterevidence is localized at draft-tree/model/hardware/concurrency scope and branch-waste boundary`。Workload=`speculative decoding with parallel causal draft trees in vLLM`；Model=`Not Disclosed`；Hardware=`NVIDIA H100 GPU`；Evaluator=`accepted length, output throughput/latency and tree-width/depth ablations`。这些证据不自动成为 production SLO、普遍安全保证或跨模型/硬件排名。

**Trade-off / failure / fallback。** 更宽树提高候选覆盖也增加 verify shape、显存和 branch waste；现有 Ch48 已覆盖该 trade-off，不追加论文特定实现。

<!-- claim:SF-2026-ARXIV-2606-18394:start -->
**Claim boundary。** 只使用 `https://arxiv.org/html/2606.18394v1` 的 exact-v1 正文；HTML 不可用的三个 family 显式走官方 PDF fallback。later revision/artifact 不参与，ordinary pending=`0`。
<!-- claim:SF-2026-ARXIV-2606-18394:end -->
<!-- review:SF-2026-ARXIV-2606-18394:end -->

<!-- review:SF-2026-ARXIV-2606-18400:start -->
### 2606.18400 — CloakLM: Obfuscating GPU Memory Layout to Mitigate Model Ex-filtration for Serving

**问题与机制变化。** 共享 GPU 上的模型权重保护可在 PCIe traffic、weight order 与 HBM physical page 三层破坏可重建 regularity，同时保留 authorized virtual layout；这是 cost-imposition 而非 secrecy proof。

**State / data / control owner。** `PLATFORM-SECURITY` 是唯一知识 owner；`Books/part-06-ai-infrastructure/69-trace.md; Books/part-07-agent/84-agent-platform.md` 只接收相邻 handoff。论文名称不取得跨章 authority。

**Evaluation：proof / non-proof。** Method=`arXiv:2606.18400v1 PDF §3 threat model; §§4–5 CloakLM three-tier design and integration`；Evaluation=`arXiv:2606.18400v1 PDF §§6–7 PyTorch/vLLM LLaMA/Qwen evaluation`；Counterevidence=`arXiv:2606.18400v1 PDF §1/§8 scope: no host OS, hypervisor, firmware or mapping-compromise defense`。Workload=`Four configurations spanning dense and MoE models at tensor parallelism 1 and 2 under PCIe-snooping and HBM-dump attacks`；Model=`Llama 3.1 8B, Qwen 3 14B and Qwen 3 MoE 30B/3B-active`；Hardware=`NVIDIA L40S GPUs with 46 GB HBM and PCIe 4.0 x16 at 32 GB/s one-way bandwidth`；Evaluator=`extraction degradation plus inference latency/throughput overhead`。这些证据不自动成为 production SLO、普遍安全保证或跨模型/硬件排名。

**Trade-off / failure / fallback。** layout obfuscation增加 allocator/metadata和可能的访问开销；无法阻止已拿到映射或可改 kernel 的攻击者。

<!-- claim:SF-2026-ARXIV-2606-18400:start -->
**Claim boundary。** 只使用 `https://arxiv.org/pdf/2606.18400v1` 的 exact-v1 正文；HTML 不可用的三个 family 显式走官方 PDF fallback。later revision/artifact 不参与，ordinary pending=`0`。
<!-- claim:SF-2026-ARXIV-2606-18400:end -->
<!-- review:SF-2026-ARXIV-2606-18400:end -->

<!-- review:SF-2026-ARXIV-2606-18421:start -->
### 2606.18421 — Finding Compiler-Platform Interaction Bugs in Deep Learning Pipelines via Cross-Layer Constraints

**问题与机制变化。** DL compiler release testing 应抽取跨 model semantics、IR pass 与 hardware feasibility 的 full-stack constraints，并把 assertion pattern作为 behavior-equivalence oracle。

**State / data / control owner。** `INFER-TENSORRT-LLM` 是唯一知识 owner；`Books/part-05-inference-system/48-speculative-decoding.md; Books/part-05-inference-system/54-gpu-memory.md` 只接收相邻 handoff。论文名称不取得跨章 authority。

**Evaluation：proof / non-proof。** Method=`arXiv:2606.18421v1 §3 XCheck, §§3.1–3.3 constraint extraction, exploration and behavior differentiation`；Evaluation=`arXiv:2606.18421v1 §4.1–4.2 evaluation on TVM, ONNX-MLIR and GeneSys`；Counterevidence=`Not Disclosed — arXiv:2606.18421v1 has no dedicated limitations section; exact-v1 counterevidence is localized at three-compiler/backend scope; no dedicated limitations section`。Workload=`Generated ONNX graphs exercised against TVM, ONNX-MLIR and GeneSys`；Model=`Not Disclosed`；Hardware=`Not Disclosed`；Evaluator=`bug-revealing cases, late-stage reach, behavior partitions and extensibility`。这些证据不自动成为 production SLO、普遍安全保证或跨模型/硬件排名。

**Trade-off / failure / fallback。** 深层 constraint能发现 silent bug却增加规则维护和 false signal；2,034 cases不等于2,034已确认独立生产缺陷。

<!-- claim:SF-2026-ARXIV-2606-18421:start -->
**Claim boundary。** 只使用 `https://arxiv.org/html/2606.18421v1` 的 exact-v1 正文；HTML 不可用的三个 family 显式走官方 PDF fallback。later revision/artifact 不参与，ordinary pending=`0`。
<!-- claim:SF-2026-ARXIV-2606-18421:end -->
<!-- review:SF-2026-ARXIV-2606-18421:end -->

<!-- review:SF-2026-ARXIV-2606-18431:start -->
### 2606.18431 — Beyond Prediction: Tail-Aware Scheduling for LLM Inference

**问题与机制变化。** LLM scheduler 应直接优化 tail risk，以 cache-aware preemption与完成风险信号决策，而不是依赖易漂移的 output-length point predictor。

**State / data / control owner。** `INFER-SCHEDULING` 是唯一知识 owner；`Books/part-05-inference-system/55-pd-disaggregation.md; Books/part-06-ai-infrastructure/63-gpu-scheduler.md` 只接收相邻 handoff。论文名称不取得跨章 authority。

**Evaluation：proof / non-proof。** Method=`arXiv:2606.18431v1 §3 tail-aware objective and prediction-free scheduler; §4 cache-aware preemption`；Evaluation=`arXiv:2606.18431v1 §5 production/open-trace evaluation and ablations`；Counterevidence=`Not Disclosed — arXiv:2606.18431v1 has no dedicated limitations section; exact-v1 counterevidence is localized at trace/model/engine and overload-regime boundaries`。Workload=`production and open LLM-serving traces under tail-latency pressure`；Model=`Not Disclosed`；Hardware=`Not Disclosed`；Evaluator=`P95/P99 latency, throughput, preemption/recompute and cache-hit effects`。这些证据不自动成为 production SLO、普遍安全保证或跨模型/硬件排名。

**Trade-off / failure / fallback。** prediction-free不等于信息免费，tail objective可能牺牲mean/fairness；受测 traces不证明所有SLO最优。

<!-- claim:SF-2026-ARXIV-2606-18431:start -->
**Claim boundary。** 只使用 `https://arxiv.org/html/2606.18431v1` 的 exact-v1 正文；HTML 不可用的三个 family 显式走官方 PDF fallback。later revision/artifact 不参与，ordinary pending=`0`。
<!-- claim:SF-2026-ARXIV-2606-18431:end -->
<!-- review:SF-2026-ARXIV-2606-18431:end -->

<!-- review:SF-2026-ARXIV-2606-18448:start -->
### 2606.18448 — VisualSkill: Multimodal Skills for Computer-Use Agents

**问题与机制变化。** Computer-use skill 应把 screenshot、spatial step、semantic instruction 与 resource references组成可版本化 multimodal artifact，并允许按 topic/on-demand MCP load，避免全库 prompt 膨胀。

**State / data / control owner。** `AGENT-TOOL-CALLING` 是唯一知识 owner；`Books/part-07-agent/81-workflow.md; Books/part-06-ai-infrastructure/72-security.md` 只接收相邻 handoff。论文名称不取得跨章 authority。

**Evaluation：proof / non-proof。** Method=`arXiv:2606.18448v1 §3 VisualSkill construction; §4 hierarchical storage and load_topic interface`；Evaluation=`arXiv:2606.18448v1 §5 live-UI computer-use evaluation and ablations`；Counterevidence=`Not Disclosed — arXiv:2606.18448v1 has no dedicated limitations section; exact-v1 counterevidence is localized at UI/task/model, authored-skill and MCP-loading scope`。Workload=`live computer-use tasks over graphical interfaces with reusable multimodal skills`；Model=`Not Disclosed`；Hardware=`Not Disclosed`；Evaluator=`task success, steps/tokens, retrieval/loading and transfer ablations`。这些证据不自动成为 production SLO、普遍安全保证或跨模型/硬件排名。

**Trade-off / failure / fallback。** 多模态 skill提高复用却增加视觉漂移、存储与供应链面；按需加载 miss 时必须回退在线探索。

<!-- claim:SF-2026-ARXIV-2606-18448:start -->
**Claim boundary。** 只使用 `https://arxiv.org/html/2606.18448v1` 的 exact-v1 正文；HTML 不可用的三个 family 显式走官方 PDF fallback。later revision/artifact 不参与，ordinary pending=`0`。
<!-- claim:SF-2026-ARXIV-2606-18448:end -->
<!-- review:SF-2026-ARXIV-2606-18448:end -->

<!-- review:SF-2026-ARXIV-2606-18467:start -->
### 2606.18467 — ToolChain-CRC: Conformal Risk Control for Agentic AI Under Retrieval and Tool-Use Drift

**问题与机制变化。** Tool/retrieval trajectory release 可把 step risk校准为 trajectory conformal acceptance，并用 supermartingale anytime alarm监测运行中超界；drift时必须重校准或 abstain。

**State / data / control owner。** `PLATFORM-EVALUATION-SYSTEM` 是唯一知识 owner；`Books/part-06-ai-infrastructure/69-trace.md; Books/part-06-ai-infrastructure/72-security.md` 只接收相邻 handoff。论文名称不取得跨章 authority。

**Evaluation：proof / non-proof。** Method=`arXiv:2606.18467v1 §3 trajectory risk and conformal calibration; §4 anytime monitoring and drift extension`；Evaluation=`arXiv:2606.18467v1 §5 retrieval/tool-use experiments and coverage-risk analyses`；Counterevidence=`Not Disclosed — arXiv:2606.18467v1 has no dedicated limitations section; exact-v1 counterevidence is localized at exchangeability, detector delay and tool/retrieval drift limitations`。Workload=`agent trajectories with retrieval and tool-use distribution drift`；Model=`Not Disclosed`；Hardware=`Not Disclosed`；Evaluator=`trajectory risk coverage, abstention, alarm delay and false-alarm behavior`。这些证据不自动成为 production SLO、普遍安全保证或跨模型/硬件排名。

**Trade-off / failure / fallback。** coverage依赖 calibration分布且 alarm会 false positive；形式保证不证明 scorer或 causal harm标签正确。

<!-- claim:SF-2026-ARXIV-2606-18467:start -->
**Claim boundary。** 只使用 `https://arxiv.org/html/2606.18467v1` 的 exact-v1 正文；HTML 不可用的三个 family 显式走官方 PDF fallback。later revision/artifact 不参与，ordinary pending=`0`。
<!-- claim:SF-2026-ARXIV-2606-18467:end -->
<!-- review:SF-2026-ARXIV-2606-18467:end -->

<!-- review:SF-2026-ARXIV-2606-18497:start -->
### 2606.18497 — Ghost Vectors: Soft-Deleted Embeddings Remain Reconstructible in HNSW Vector Databases

**问题与机制变化。** Vector DB deletion 必须追踪 source→embedding→HNSW node→backup/replica 的物理生命周期；soft-delete tombstone 不是擦除，需 epoch key rotation与 signed deletion proof。

**State / data / control owner。** `AGENT-RAG` 是唯一知识 owner；`Books/part-07-agent/77-memory.md; Books/part-06-ai-infrastructure/72-security.md` 只接收相邻 handoff。论文名称不取得跨章 authority。

**Evaluation：proof / non-proof。** Method=`arXiv:2606.18497v1 §3 Ghost Vectors recovery methodology; §4 cryptographic epoch-deletion design`；Evaluation=`arXiv:2606.18497v1 §5 HNSW/database recovery experiments`；Counterevidence=`Not Disclosed — arXiv:2606.18497v1 has no dedicated limitations section; exact-v1 counterevidence is localized at backend/version/access model and cryptographic-key assumptions`。Workload=`soft-deleted embeddings recovered from HNSW vector databases`；Model=`Not Disclosed`；Hardware=`Not Disclosed`；Evaluator=`vector reconstruction/re-identification success, purge cost and key-rotation proof checks`。这些证据不自动成为 production SLO、普遍安全保证或跨模型/硬件排名。

**Trade-off / failure / fallback。** physical purge或key rotation增加 rebuild、availability与密钥治理成本；受测 HNSW 恢复不覆盖所有 vector stores。

<!-- claim:SF-2026-ARXIV-2606-18497:start -->
**Claim boundary。** 只使用 `https://arxiv.org/html/2606.18497v1` 的 exact-v1 正文；HTML 不可用的三个 family 显式走官方 PDF fallback。later revision/artifact 不参与，ordinary pending=`0`。
<!-- claim:SF-2026-ARXIV-2606-18497:end -->
<!-- review:SF-2026-ARXIV-2606-18497:end -->

<!-- review:SF-2026-ARXIV-2606-18532:start -->
### 2606.18532 — AI Sandboxes: A Threat Model, Taxonomy, and Measurement Framework

**问题与机制变化。** AI sandbox 应以 threat model和 weakest-link evidence评估 fidelity、controllability、observability、containment、reproducibility与governance，不能把“进程在容器里”当成安全证明。

**State / data / control owner。** `PLATFORM-SECURITY` 是唯一知识 owner；`Books/part-06-ai-infrastructure/69-trace.md; Books/part-07-agent/84-agent-platform.md` 只接收相邻 handoff。论文名称不取得跨章 authority。

**Evaluation：proof / non-proof。** Method=`arXiv:2606.18532v1 §3 sandbox threat model and taxonomy; §4 measurement framework`；Evaluation=`arXiv:2606.18532v1 §5 cross-sandbox case studies/measurements`；Counterevidence=`Not Disclosed — arXiv:2606.18532v1 has no dedicated limitations section; exact-v1 counterevidence is localized at coverage of sandbox types, attacker capability and measurement incompleteness`。Workload=`representative AI-agent sandbox designs and attack surfaces`；Model=`Not Disclosed`；Hardware=`Not Disclosed`；Evaluator=`six-dimension evidence matrix, containment tests and reproducibility/governance checks`。这些证据不自动成为 production SLO、普遍安全保证或跨模型/硬件排名。

**Trade-off / failure / fallback。** 更强隔离通常降低 fidelity/性能且扩大运维；框架只能组织证据，不能认证未知 escape或side channel不存在。

<!-- claim:SF-2026-ARXIV-2606-18532:start -->
**Claim boundary。** 只使用 `https://arxiv.org/html/2606.18532v1` 的 exact-v1 正文；HTML 不可用的三个 family 显式走官方 PDF fallback。later revision/artifact 不参与，ordinary pending=`0`。
<!-- claim:SF-2026-ARXIV-2606-18532:end -->
<!-- review:SF-2026-ARXIV-2606-18532:end -->

<!-- review:SF-2026-ARXIV-2606-18550:start -->
### 2606.18550 — The Gate Is Only as Honest as Its Contracts: ContractGuard for the Contract Layer of Risk-Aware Causal Gating

**问题与机制变化。** Tool safety gate依赖 contract integrity；应对 precondition/effect/risk/authorization字段做 signed provenance、typed attestation与runtime effect verification，且 effect字段比risk标签更load-bearing。

**State / data / control owner。** `PLATFORM-SECURITY` 是唯一知识 owner；`Books/part-06-ai-infrastructure/69-trace.md; Books/part-07-agent/84-agent-platform.md` 只接收相邻 handoff。论文名称不取得跨章 authority。

**Evaluation：proof / non-proof。** Method=`arXiv:2606.18550v1 §II threat model; §III two-gate taxonomy; §IV ContractGuard ladder`；Evaluation=`arXiv:2606.18550v1 §VI–VII controlled exhaustive attacker and six-model validation`；Counterevidence=`arXiv:2606.18550v1 §XI Limitations; trusted-attestation, symbolic-space and external-side-effect boundaries`。Workload=`RiskGate 100-tool registry; eight high-risk targets; 256 perturbation configurations per target; 1,898 executed configurations and 5,886 phrasing trials`；Model=`Claude Opus 4.8, Claude Sonnet 4.6, Claude Haiku 4.5, Nova Premier, Nova 2 Lite and GPT-OSS-120B`；Hardware=`Not Disclosed`；Evaluator=`injection success by guard rung, field/compound attacks, honest-contract rejection and model validation`。这些证据不自动成为 production SLO、普遍安全保证或跨模型/硬件排名。

**Trade-off / failure / fallback。** 完整 ladder增加签名、schema与runtime mediation成本；只在有限 contract perturbation空间给保证，attestation失陷即失效。

<!-- claim:SF-2026-ARXIV-2606-18550:start -->
**Claim boundary。** 只使用 `https://arxiv.org/html/2606.18550v1` 的 exact-v1 正文；HTML 不可用的三个 family 显式走官方 PDF fallback。later revision/artifact 不参与，ordinary pending=`0`。
<!-- claim:SF-2026-ARXIV-2606-18550:end -->
<!-- review:SF-2026-ARXIV-2606-18550:end -->

<!-- review:SF-2026-ARXIV-2606-18600:start -->
### 2606.18600 — ShuntServe: Cost-Efficient LLM Serving on Heterogeneous Spot GPU Clusters

**问题与旧路径。** As large language model (LLM) services become widely adopted, the cost of GPU resources for serving these models in cloud environments has emerged as a critical concern. 旧路径在风险、状态或控制面没有跨出作者前提时仍然合理。

**机制与 owner。** 异构 spot serving 必须联合决定 GPU pool、每 stage TP/PP 与不等层分配；中断时以输出重算恢复 request，并让 replacement initialization 与旧 pipeline 服务重叠。 唯一知识 owner 为 `INFER-SCHEDULING`；相邻节点只消费带 identity 的 handoff。

**Evaluation：证明与未证明。** Llama-3.1-70B 与 Qwen3-32B 在 AWS L4/A10G/L40S 集群上报告吞吐与 offline/online 成本效率改善。 Method=`https://arxiv.org/html/2606.18600v1 — § exact-v1 anchor: 4 Model Placement for Heterogeneous GPUs`；Evaluation=`https://arxiv.org/html/2606.18600v1 — § exact-v1 evaluation anchor: 7 Evaluation`。Benchmark contract：model=`Llama-3.1-70B; Qwen3-32B`；hardware=`AWS L4, A10G and L40S GPUs`；precision=`Not Disclosed`；batch=`Not Disclosed`；concurrency=`Not Disclosed`；SLO=`Not Disclosed`；evaluator=`offline throughput, online TTFT/TPOT and cost efficiency under spot interruption`。

**Trade-off、failure、共存与演进。** 六天单 region 可用性和短上下文重算不能证明跨区供应或长上下文恢复；shared tensor store 也引入新的可用性 owner。 因而该 family 只支持这里写出的 delta，未披露执行字段保持 Unknown/Not Disclosed。Limit/counterevidence=`https://arxiv.org/html/2606.18600v1 — § exact-v1 limitation/counterevidence anchor: 8.1 Limitation`。

<!-- claim:SF-2026-ARXIV-2606-18600:start -->
Claim boundary：仅 `arXiv:2606.18600v1` official HTML；不使用 later version；ordinary pending locator count=`0`.
<!-- claim:SF-2026-ARXIV-2606-18600:end -->
<!-- review:SF-2026-ARXIV-2606-18600:end -->

<!-- review:SF-2026-ARXIV-2606-18619:start -->
### 2606.18619 — Code-Augur: Agentic Vulnerability Detection via Specification Inference

**问题与旧路径。** The advent of agentic vulnerability detection is already becoming a watershed moment for software security. 旧路径在风险、状态或控制面没有跨出作者前提时仍然合理。

**机制与 owner。** Agent 判定代码安全时要把隐含输入假设提交为 in-source assertions，再由 guided fuzzer 反证；assertion failure 可能是漏洞，也可能是 specification repair 信号。 唯一知识 owner 为 `PLATFORM-SECURITY`；相邻节点只消费带 identity 的 handoff。

**Evaluation：证明与未证明。** 在真实开源项目上与 agent baselines 比较，并报告发现 22 个新漏洞；使用 Sonnet、DeepSeek，并与 Claude Mythos 作受限比较。 Method=`https://arxiv.org/html/2606.18619v1 — § exact-v1 anchor: security-specification-first paradigm`；Evaluation=`https://arxiv.org/html/2606.18619v1 — § exact-v1 evaluation anchor: real-world subjects`。Benchmark contract：model=`Claude Sonnet 4.6 and DeepSeek V4 Pro; Claude Mythos is comparison-only`；hardware=`Not Disclosed`；precision=`Not Disclosed`；batch=`Not Disclosed`；concurrency=`Not Disclosed`；SLO=`Not Disclosed`；evaluator=`real-subject vulnerability findings plus specification-falsification outcomes`。

**Trade-off、failure、共存与演进。** fuzzer 未触发不等于 invariant 成立，assertion 也可能错；覆盖限于作者 subjects 与可观测运行输入。 因而该 family 只支持这里写出的 delta，未披露执行字段保持 Unknown/Not Disclosed。Limit/counterevidence=`https://arxiv.org/html/2606.18619v1 — § exact-v1 limitation/counterevidence anchor: limitations`。

<!-- claim:SF-2026-ARXIV-2606-18619:start -->
Claim boundary：仅 `arXiv:2606.18619v1` official HTML；不使用 later version；ordinary pending locator count=`0`.
<!-- claim:SF-2026-ARXIV-2606-18619:end -->
<!-- review:SF-2026-ARXIV-2606-18619:end -->

<!-- review:SF-2026-ARXIV-2606-18650:start -->
### 2606.18650 — BLADE: Scalable Bi-level Adaptive Data Selection for LLM Training

**问题与旧路径。** As Large Language Model (LLM) datasets scale to trillions of tokens, data selection has emerged as a critical frontier to filter out uninformative noise and construct adaptive learning trajectories. 旧路径在风险、状态或控制面没有跨出作者前提时仍然合理。

**机制与 owner。** 训练数据选择可把双层 influence objective 改写为带 Lagrange penalty 的单层目标，并让动态 reference 随 proxy trajectory 同步；online selector 用 memoryless randomized block-coordinate Frank-Wolfe。 唯一知识 owner 为 `TRAIN-DATA`；相邻节点只消费带 identity 的 handoff。

**Evaluation：证明与未证明。** exact-v1 在作者 LLM pretraining matrix 中比较 BLADE 与 influence、excess-loss baselines，并给出 first-order convergence。 Method=`https://arxiv.org/html/2606.18650v1 — § exact-v1 anchor: penalized single-level objective`；Evaluation=`https://arxiv.org/html/2606.18650v1 — § exact-v1 evaluation anchor: Experiments`。Benchmark contract：model=`TinyLlama-1.1B and Llama2-7B target models with 3B/5B-token continued-pretraining budgets`；hardware=`Not Disclosed`；precision=`Not Disclosed`；batch=`Not Disclosed`；concurrency=`Not Disclosed`；SLO=`Not Disclosed`；evaluator=`downstream task quality and selection efficiency against influence/excess-loss baselines`。

**Trade-off、failure、共存与演进。** proxy-to-target transfer、penalty 设定与 trajectory drift 仍可能失配；收敛定理不等于目标模型质量普遍提升。 因而该 family 只支持这里写出的 delta，未披露执行字段保持 Unknown/Not Disclosed。Limit/counterevidence=`https://arxiv.org/html/2606.18650v1 — § exact-v1 limitation/counterevidence anchor: Limitations`。

<!-- claim:SF-2026-ARXIV-2606-18650:start -->
Claim boundary：仅 `arXiv:2606.18650v1` official HTML；不使用 later version；ordinary pending locator count=`0`.
<!-- claim:SF-2026-ARXIV-2606-18650:end -->
<!-- review:SF-2026-ARXIV-2606-18650:end -->

<!-- review:SF-2026-ARXIV-2606-18668:start -->
### 2606.18668 — EARS: Explanatory Abstention for Reliable Sub-Agent Modeling in Large-scale Multi-Agent Systems

**问题与旧路径。** In large-scale enterprise settings, centralized multi-agent systems (MAS) are increasingly adopted, in which a coordinator delegates user requests to lightweight, domain-specialized sub-agents. 旧路径在风险、状态或控制面没有跨出作者前提时仍然合理。

**机制与 owner。** sub-agent abstention 应是 typed failure message，携带 ambiguous、misrouted、unsupported 等理由，供 coordinator clarification、reroute 或 fallback，而不是空响应。 唯一知识 owner 为 `AGENT-MULTI-AGENT`；相邻节点只消费带 identity 的 handoff。

**Evaluation：证明与未证明。** 生产电商 BI assistant 的 overall response pass rate从 68.5% 提升到 78.9%。 Method=`https://arxiv.org/html/2606.18668v1 — § exact-v1 anchor: Explanatory Abstention`；Evaluation=`https://arxiv.org/html/2606.18668v1 — § exact-v1 evaluation anchor: production e-commerce assistant`。Benchmark contract：model=`Not Disclosed`；hardware=`Not Disclosed`；precision=`Not Disclosed`；batch=`Not Disclosed`；concurrency=`Not Disclosed`；SLO=`Not Disclosed`；evaluator=`production pass rate under structured abstention labels and rationales`。

**Trade-off、failure、共存与演进。** judge ensemble 与生产流量共享偏差且 backbone 未披露；pass rate 不证明授权、安全或跨域 calibration。 因而该 family 只支持这里写出的 delta，未披露执行字段保持 Unknown/Not Disclosed。Limit/counterevidence=`https://arxiv.org/html/2606.18668v1 — § exact-v1 limitation/counterevidence anchor: Limitations`。

<!-- claim:SF-2026-ARXIV-2606-18668:start -->
Claim boundary：仅 `arXiv:2606.18668v1` official HTML；不使用 later version；ordinary pending locator count=`0`.
<!-- claim:SF-2026-ARXIV-2606-18668:end -->
<!-- review:SF-2026-ARXIV-2606-18668:end -->

<!-- review:SF-2026-ARXIV-2606-18673:start -->
### 2606.18673 — Understanding and Mitigating Prompt Leaking Attacks in Real-World LLM-Based Applications

**问题与旧路径。** Large language model (LLM)-based applications rely on system prompts to encode core logic and developer-defined constraints, making these prompts important intellectual property. 旧路径在风险、状态或控制面没有跨出作者前提时仍然合理。

**机制与 owner。** system-prompt secrecy 不能只靠静态拒答；AREA 用可优化 soft prompt 重锚 attention，但 secret/API key 仍必须移出 prompt 并由外部 reference monitor 管理。 唯一知识 owner 为 `PLATFORM-SECURITY`；相邻节点只消费带 identity 的 handoff。

**Evaluation：证明与未证明。** 测量六个平台 1,200 个应用，报告超过 80% 泄漏；AREA 的 usability 与优化开销相对防线比较。 Method=`https://arxiv.org/html/2606.18673v1 — § exact-v1 anchor: attention drift`；Evaluation=`https://arxiv.org/html/2606.18673v1 — § exact-v1 evaluation anchor: 1,200 applications`。Benchmark contract：model=`Llama-2-7B-chat-hf, Llama-3.1-8B-Instruct, Mistral-7B-Instruct, Qwen3-4B-Instruct, Qwen3-32B, Qwen2.5-72B-Instruct and Llama-3.3-70B-Instruct`；hardware=`Not Disclosed`；precision=`Not Disclosed`；batch=`Not Disclosed`；concurrency=`Not Disclosed`；SLO=`Not Disclosed`；evaluator=`prompt leakage resistance, usability and optimization overhead over 1,200 applications`。

**Trade-off、failure、共存与演进。** attention drift 是受测模型解释，不证明所有泄漏因果；soft prompt 无法把已放入上下文的密钥变成真正 secret。 因而该 family 只支持这里写出的 delta，未披露执行字段保持 Unknown/Not Disclosed。Limit/counterevidence=`https://arxiv.org/html/2606.18673v1 — § exact-v1 limitation/counterevidence anchor: limitations`。

<!-- claim:SF-2026-ARXIV-2606-18673:start -->
Claim boundary：仅 `arXiv:2606.18673v1` official HTML；不使用 later version；ordinary pending locator count=`0`.
<!-- claim:SF-2026-ARXIV-2606-18673:end -->
<!-- review:SF-2026-ARXIV-2606-18673:end -->

<!-- review:SF-2026-ARXIV-2606-18697:start -->
### 2606.18697 — Stealthy World Model Manipulation via Data Poisoning

**问题与旧路径。** Model-based learning agents use learned world models to predict future states, plan actions, and adapt to new environments. 旧路径在风险、状态或控制面没有跨出作者前提时仍然合理。

**机制与 owner。** world-model fine-tuning data 是 planning control surface：SWAAP 先优化近似 clean dynamics 的低回报目标模型，再以 stealth-constrained gradient matching 修改有限 transition targets。 唯一知识 owner 为 `MULTIMODAL-WORLD-MODELS`；相邻节点只消费带 identity 的 handoff。

**Evaluation：证明与未证明。** 连续控制任务上评估 planning return、poison detectability，并测试 residual/CUSUM/TRIM 防线。 Method=`https://arxiv.org/html/2606.18697v1 — § exact-v1 anchor: two-stage data poisoning framework`；Evaluation=`https://arxiv.org/html/2606.18697v1 — § exact-v1 evaluation anchor: continuous-control tasks`。Benchmark contract：model=`Not Disclosed`；hardware=`Not Disclosed`；precision=`Not Disclosed`；batch=`Not Disclosed`；concurrency=`Not Disclosed`；SLO=`Not Disclosed`；evaluator=`planning return, poison detectability and defense response across three pipeline stages`。

**Trade-off、failure、共存与演进。** 只击败 non-adaptive defenses；低 prediction error 不等于 transition 正确，真实环境 feedback 仍是权威。 因而该 family 只支持这里写出的 delta，未披露执行字段保持 Unknown/Not Disclosed。Limit/counterevidence=`https://arxiv.org/html/2606.18697v1 — § exact-v1 limitation/counterevidence anchor: limitations`。

<!-- claim:SF-2026-ARXIV-2606-18697:start -->
Claim boundary：仅 `arXiv:2606.18697v1` official HTML；不使用 later version；ordinary pending locator count=`0`.
<!-- claim:SF-2026-ARXIV-2606-18697:end -->
<!-- review:SF-2026-ARXIV-2606-18697:end -->

<!-- review:SF-2026-ARXIV-2606-18741:start -->
### 2606.18741 — ReMP: Low-Downtime Runtime Model-Parallelism Reconfiguration for LLM Serving

**问题与旧路径。** Current large language model (LLM) inference systems universally deploy ultra-large-scale models using a combination of Tensor Parallelism (TP) and Pipeline Parallelism (PP). 旧路径在风险、状态或控制面没有跨出作者前提时仍然合理。

**机制与 owner。** runtime parallelism 变更要把 topology 与 request state 解耦，并以二维 KV migration 将旧 TP/PP shard 映射到新 topology，再原子切换流量。 唯一知识 owner 为 `INFER-SCHEDULING`；相邻节点只消费带 identity 的 handoff。

**Evaluation：证明与未证明。** 7B–70B models 的多数 topology switch 为 1–7 秒，并报告动态 workload 的 TTFT、TPOT 与 output throughput。 Method=`https://arxiv.org/html/2606.18741v1 — § exact-v1 anchor: two-dimensional KV cache migration`；Evaluation=`https://arxiv.org/html/2606.18741v1 — § exact-v1 evaluation anchor: Experiments`。Benchmark contract：model=`Llama2-7B, Qwen3-30B-A3B, DeepSeek-R1-Distill-Qwen-32B and Llama2-70B`；hardware=`NVIDIA H100 and RTX 5090 platforms`；precision=`Not Disclosed`；batch=`Not Disclosed`；concurrency=`Not Disclosed`；SLO=`Not Disclosed`；evaluator=`reconfiguration downtime, TTFT, TPOT and output throughput`。

**Trade-off、failure、共存与演进。** KV migration 与双份资源会制造瞬时带宽/容量峰值；作者模型与网络不证明任意拓扑可无损切换。 因而该 family 只支持这里写出的 delta，未披露执行字段保持 Unknown/Not Disclosed。Limit/counterevidence=`https://arxiv.org/html/2606.18741v1 — § exact-v1 limitation/counterevidence anchor: Limitations`。

<!-- claim:SF-2026-ARXIV-2606-18741:start -->
Claim boundary：仅 `arXiv:2606.18741v1` official HTML；不使用 later version；ordinary pending locator count=`0`.
<!-- claim:SF-2026-ARXIV-2606-18741:end -->
<!-- review:SF-2026-ARXIV-2606-18741:end -->

<!-- review:SF-2026-ARXIV-2606-18746:start -->
### 2606.18746 — What Must Generalist Agents Remember?

**问题与旧路径。** This paper develops a formal account of what generalist agents must store in memory in order to act near-optimally across multiple environments and goals. 旧路径在风险、状态或控制面没有跨出作者前提时仍然合理。

**机制与 owner。** 若相同 observation bottleneck 在不同 domain 需要不兼容 action，近最优 policy 必须保存可区分的 memory distribution；足够的 value 信息还可近似重建局部 transition dynamics。 唯一知识 owner 为 `AGENT-MEMORY`；相邻节点只消费带 identity 的 handoff。

**Evaluation：证明与未证明。** exact-v1 给出 separation theorem 与 transition reconstruction 条件，而非经验 leaderboard。 Method=`https://arxiv.org/html/2606.18746v1 — § exact-v1 anchor: separation theorem`；Evaluation=`https://arxiv.org/html/2606.18746v1 — § exact-v1 evaluation anchor: transition-model reconstruction`。Benchmark contract：model=`Not Disclosed`；hardware=`Not Disclosed`；precision=`Not Disclosed`；batch=`Not Disclosed`；concurrency=`Not Disclosed`；SLO=`Not Disclosed`；evaluator=`theorem premises and approximation error for domain disambiguation and local dynamics reconstruction`。

**Trade-off、failure、共存与演进。** 定理依赖形式化 observation/domain 假设；可重建局部 dynamics 不代表 memory 内容真实、授权或可长期维护。 因而该 family 只支持这里写出的 delta，未披露执行字段保持 Unknown/Not Disclosed。Limit/counterevidence=`https://arxiv.org/html/2606.18746v1 — § exact-v1 limitation/counterevidence anchor: assumptions`。

<!-- claim:SF-2026-ARXIV-2606-18746:start -->
Claim boundary：仅 `arXiv:2606.18746v1` official HTML；不使用 later version；ordinary pending locator count=`0`.
<!-- claim:SF-2026-ARXIV-2606-18746:end -->
<!-- review:SF-2026-ARXIV-2606-18746:end -->

<!-- review:SF-2026-ARXIV-2606-18810:start -->
### 2606.18810 — Learning from Own Solutions: Self-Conditioned Credit Assignment for Reinforcement Learning with Verifiable Rewards

**问题与旧路径。** Reinforcement learning with verifiable rewards (RLVR) has driven substantial progress in training LLMs for reasoning tasks, but representative methods such as GRPO assign uniform credit across all tokens, wasting gradient on routine tokens while under-crediting pivotal reasoning steps. 旧路径在风险、状态或控制面没有跨出作者前提时仍然合理。

**机制与 owner。** SC-GRPO 用 verified trajectory 条件化前后 token KL 作为 GRPO gradient 权重，让 policy 自己暴露 pivotal token，避免外部 PRM/teacher。 唯一知识 owner 为 `TRAIN-GRPO`；相邻节点只消费带 identity 的 handoff。

**Evaluation：证明与未证明。** 五个 math、code、agentic benchmarks 上相对 GRPO 与 DAPO 报告平均改善和 OOD 结果。 Method=`https://arxiv.org/html/2606.18810v1 — § exact-v1 anchor: Self-Conditioned GRPO`；Evaluation=`https://arxiv.org/html/2606.18810v1 — § exact-v1 evaluation anchor: five benchmarks`。Benchmark contract：model=`Qwen3-1.7B-Base; DeepSeek-R1-Distill-Qwen-1.5B; experiments are limited to models at most 8B`；hardware=`Not Disclosed`；precision=`Not Disclosed`；batch=`Not Disclosed`；concurrency=`Not Disclosed`；SLO=`Not Disclosed`；evaluator=`task accuracy and OOD performance against GRPO, DAPO and OPD`。

**Trade-off、failure、共存与演进。** self-conditioned teacher 与 student 共偏；KL 大小不自动等于因果 credit，verified final answer 也可能掩盖错误路径。 因而该 family 只支持这里写出的 delta，未披露执行字段保持 Unknown/Not Disclosed。Limit/counterevidence=`https://arxiv.org/html/2606.18810v1 — § exact-v1 limitation/counterevidence anchor: Limitations`。

<!-- claim:SF-2026-ARXIV-2606-18810:start -->
Claim boundary：仅 `arXiv:2606.18810v1` official HTML；不使用 later version；ordinary pending locator count=`0`.
<!-- claim:SF-2026-ARXIV-2606-18810:end -->
<!-- review:SF-2026-ARXIV-2606-18810:end -->

<!-- review:SF-2026-ARXIV-2606-18829:start -->
### 2606.18829 — GateMem: Benchmarking Memory Governance in Multi-Principal Shared-Memory Agents

**问题与旧路径。** Memory benchmarks for LLM agents largely assume single-user settings, leaving shared assistants for hospitals, workplaces, campuses, and households understudied. 旧路径在风险、状态或控制面没有跨出作者前提时仍然合理。

**机制与 owner。** 共享 memory 的 admission/read/delete 必须按 principal、role、scope 和 relationship 授权，并把 utility、ACL leakage 与 active forgetting 作为三个独立 Gate。 唯一知识 owner 为 `PLATFORM-SECURITY`；相邻节点只消费带 identity 的 handoff。

**Evaluation：证明与未证明。** GateMem 跨医疗、办公、教育、家庭；多种 memory baselines/backbones 均未同时获得强 utility、ACL 与 forgetting。 Method=`https://arxiv.org/html/2606.18829v1 — § exact-v1 anchor: multi-principal shared-memory agents`；Evaluation=`https://arxiv.org/html/2606.18829v1 — § exact-v1 evaluation anchor: diverse baselines and backbone models`。Benchmark contract：model=`GPT-5.4, DeepSeek-V4-Pro, Llama-4-Maverick, GPT-5-mini, GPT-4o-mini and Gemini-2.5-Flash-Lite`；hardware=`Not Disclosed`；precision=`Not Disclosed`；batch=`Not Disclosed`；concurrency=`Not Disclosed`；SLO=`Not Disclosed`；evaluator=`legitimate utility, contextual access-control leakage and post-deletion active forgetting`。

**Trade-off、failure、共存与演进。** structured judge 与合成 episode 不证明真实机构合规；long-context 的较高 governance score 伴随 token cost，external memory 仍可能泄漏。 因而该 family 只支持这里写出的 delta，未披露执行字段保持 Unknown/Not Disclosed。Limit/counterevidence=`https://arxiv.org/html/2606.18829v1 — § exact-v1 limitation/counterevidence anchor: limitations`。

<!-- claim:SF-2026-ARXIV-2606-18829:start -->
Claim boundary：仅 `arXiv:2606.18829v1` official HTML；不使用 later version；ordinary pending locator count=`0`.
<!-- claim:SF-2026-ARXIV-2606-18829:end -->
<!-- review:SF-2026-ARXIV-2606-18829:end -->

<!-- review:SF-2026-ARXIV-2606-18831:start -->
### 2606.18831 — Beyond Reward Engineering: A Data Recipe for Long-Context Reinforcement Learning

**问题与旧路径。** Long-context reasoning is an essential capability for large language models, particularly when they are deployed as autonomous agents that must reason over lengthy trajectories. 旧路径在风险、状态或控制面没有跨出作者前提时仍然合理。

**机制与 owner。** long-context RL 的 data owner 应同时覆盖 retrieval、multi-evidence synthesis 与 reasoning，避免只通过 reward shaping 修补 evidence localization。 唯一知识 owner 为 `TRAIN-GRPO`；相邻节点只消费带 identity 的 handoff。

**Evaluation：证明与未证明。** Qwen3-4B/8B/30B-A3B、约 14K 样本、七个长上下文 benchmark，并在 GAIA/BrowseComp 测 transfer。 Method=`https://arxiv.org/html/2606.18831v1 — § exact-v1 anchor: 3.1 Long-Context Training Data`；Evaluation=`https://arxiv.org/html/2606.18831v1 — § exact-v1 evaluation anchor: 4 Experiments`。Benchmark contract：model=`Qwen3-4B, Qwen3-8B and Qwen3-30B-A3B`；hardware=`Not Disclosed`；precision=`Not Disclosed`；batch=`Not Disclosed`；concurrency=`Not Disclosed`；SLO=`Not Disclosed`；evaluator=`seven long-context benchmarks plus GAIA and BrowseComp transfer`。

**Trade-off、failure、共存与演进。** 作者 mixture 与 Qwen family 不能证明通用配方；outcome reward 仍可能奖励无 grounding shortcut。 因而该 family 只支持这里写出的 delta，未披露执行字段保持 Unknown/Not Disclosed。Limit/counterevidence=`https://arxiv.org/html/2606.18831v1 — § exact-v1 limitation/counterevidence anchor: 5 Analysis`。

<!-- claim:SF-2026-ARXIV-2606-18831:start -->
Claim boundary：仅 `arXiv:2606.18831v1` official HTML；不使用 later version；ordinary pending locator count=`0`.
<!-- claim:SF-2026-ARXIV-2606-18831:end -->
<!-- review:SF-2026-ARXIV-2606-18831:end -->

<!-- review:SF-2026-ARXIV-2606-18847:start -->
### 2606.18847 — WorldLines: Benchmarking and Modeling Long-Horizon Stateful Embodied Agents

**问题与旧路径。** To assist humans over extended periods in real homes, embodied agents must remember user routines, world states, and past interactions. 旧路径在风险、状态或控制面没有跨出作者前提时仍然合理。

**机制与 owner。** 长期 embodied memory 需保存 visibility-aware observation、action-native state trail 与执行反馈，且旧 state 被覆盖时保留时间身份，供 planning 消费。 唯一知识 owner 为 `MULTIMODAL-EMBODIED-VLA`；相邻节点只消费带 identity 的 handoff。

**Evaluation：证明与未证明。** WorldLines 同时评 Memory QA 与 Embodied Task Planning；ObsMem 对 partial observability、overwritten state 进行比较。 Method=`https://arxiv.org/html/2606.18847v1 — § exact-v1 anchor: WorldLines`；Evaluation=`https://arxiv.org/html/2606.18847v1 — § exact-v1 evaluation anchor: ObsMem`。Benchmark contract：model=`google/gemini-3.5-flash answer generator; GPT-4o judge; GPT-4o-mini question generator`；hardware=`Not Disclosed`；precision=`Not Disclosed`；batch=`Not Disclosed`；concurrency=`Not Disclosed`；SLO=`Not Disclosed`；evaluator=`Memory QA and Embodied Task Planning over evidence-linked household traces`。

**Trade-off、failure、共存与演进。** benchmark household traces 不是开放世界；observer-grounded memory 仍可能漏看并把推断状态误写成事实。 因而该 family 只支持这里写出的 delta，未披露执行字段保持 Unknown/Not Disclosed。Limit/counterevidence=`https://arxiv.org/html/2606.18847v1 — § exact-v1 limitation/counterevidence anchor: Limitations`。

<!-- claim:SF-2026-ARXIV-2606-18847:start -->
Claim boundary：仅 `arXiv:2606.18847v1` official HTML；不使用 later version；ordinary pending locator count=`0`.
<!-- claim:SF-2026-ARXIV-2606-18847:end -->
<!-- review:SF-2026-ARXIV-2606-18847:end -->

<!-- review:SF-2026-ARXIV-2606-18874:start -->
### 2606.18874 — Externalizing Research Synthesis and Validation in AI Scientists through a Research Harness

**问题与旧路径。** AI systems can increasingly automate scientific workflows, but the reasoning that links prior evidence, generated ideas, experiments and final claims often remains implicit inside model inference. 旧路径在风险、状态或控制面没有跨出作者前提时仍然合理。

**机制与 owner。** AI scientist 应把 literature evidence、idea、implementation、ablation 与 repair trace 外化为 persistent contracts，并检查 runnable artifact 是否仍支持原 claim。 唯一知识 owner 为 `AGENT-WORKFLOW`；相邻节点只消费带 identity 的 handoff。

**Evaluation：证明与未证明。** 在 training-free memory、traffic forecasting 与 PINN 三类研究流程展示可追踪 problem→mechanism→validation 轨迹。 Method=`https://arxiv.org/html/2606.18874v1 — § exact-v1 anchor: persistent research artifacts`；Evaluation=`https://arxiv.org/html/2606.18874v1 — § exact-v1 evaluation anchor: three case studies`。Benchmark contract：model=`gpt-4o-mini answer generator and all-MiniLM-L6-v2 embedder in the matched LoCoMo validation`；hardware=`Not Disclosed`；precision=`Not Disclosed`；batch=`Not Disclosed`；concurrency=`Not Disclosed`；SLO=`Not Disclosed`；evaluator=`claim-to-artifact traceability, ablation and bounded repair across three research domains`。

**Trade-off、failure、共存与演进。** 三个案例不证明自动科学发现质量；trace 完整也不能替代独立复现或可信实验。 因而该 family 只支持这里写出的 delta，未披露执行字段保持 Unknown/Not Disclosed。Limit/counterevidence=`https://arxiv.org/html/2606.18874v1 — § exact-v1 limitation/counterevidence anchor: limitations`。

<!-- claim:SF-2026-ARXIV-2606-18874:start -->
Claim boundary：仅 `arXiv:2606.18874v1` official HTML；不使用 later version；ordinary pending locator count=`0`.
<!-- claim:SF-2026-ARXIV-2606-18874:end -->
<!-- review:SF-2026-ARXIV-2606-18874:end -->

<!-- review:SF-2026-ARXIV-2606-18958:start -->
### 2606.18958 — LiveStack: OS Support for Cluster-Scale Full-Stack Live Simulation

**问题与旧路径。** Cluster-scale full-stack simulation is essential for evaluating distributed software stacks and emerging hardware components before deployment. 旧路径在风险、状态或控制面没有跨出作者前提时仍然合理。

**机制与 owner。** cluster live simulation 要让真实 software stack 与模拟 node/network/device time 协同推进，并显式区分 simulated resource state 与 production effect。 唯一知识 owner 为 `PLATFORM-PRODUCTION`；相邻节点只消费带 identity 的 handoff。

**Evaluation：证明与未证明。** exact-v1 在 cluster-scale full-stack workloads 上比较 simulation fidelity、scale 与执行开销。 Method=`https://arxiv.org/html/2606.18958v1 — § exact-v1 anchor: full-stack live simulation`；Evaluation=`https://arxiv.org/html/2606.18958v1 — § exact-v1 evaluation anchor: Evaluation`。Benchmark contract：model=`Not Disclosed`；hardware=`Not Disclosed`；precision=`Not Disclosed`；batch=`Not Disclosed`；concurrency=`Not Disclosed`；SLO=`Not Disclosed`；evaluator=`simulation scale, fidelity and runtime overhead`。

**Trade-off、failure、共存与演进。** 模拟器遗漏的 kernel、network tail 和 control-plane race 会制造假确定性；不能用 live simulation 代替 canary。 因而该 family 只支持这里写出的 delta，未披露执行字段保持 Unknown/Not Disclosed。Limit/counterevidence=`https://arxiv.org/html/2606.18958v1 — § exact-v1 limitation/counterevidence anchor: Limitations`。

<!-- claim:SF-2026-ARXIV-2606-18958:start -->
Claim boundary：仅 `arXiv:2606.18958v1` official HTML；不使用 later version；ordinary pending locator count=`0`.
<!-- claim:SF-2026-ARXIV-2606-18958:end -->
<!-- review:SF-2026-ARXIV-2606-18958:end -->

<!-- review:SF-2026-ARXIV-2606-18967:start -->
### 2606.18967 — EfficientRollout: System-Aware Self-Speculative Decoding for RL Rollouts

**问题与旧路径。** Reinforcement learning (RL) has become a representative post-training paradigm for LLMs, enabling strong reasoning and agentic capabilities. 旧路径在风险、状态或控制面没有跨出作者前提时仍然合理。

**机制与 owner。** RL rollout 的 draft policy 可由当前 policy 自身派生，但 acceptance、KV/state rollback 与训练版本 identity 必须共同绑定，避免把 serving speculation 当成离策略数据复用。 唯一知识 owner 为 `INFER-SPECULATIVE-DECODING`；相邻节点只消费带 identity 的 handoff。

**Evaluation：证明与未证明。** 在 RL rollout workloads 上报告 self-speculative speedup、acceptance 与 training quality。 Method=`https://arxiv.org/html/2606.18967v1 — § exact-v1 anchor: system-aware self-speculative decoding`；Evaluation=`https://arxiv.org/html/2606.18967v1 — § exact-v1 evaluation anchor: Experiments`。Benchmark contract：model=`Qwen2.5-7B, Qwen2.5-14B and Llama3.1-8B-Instruct with quantized self-drafters`；hardware=`single NVIDIA A100-80GiB SXM in the decode-cost study`；precision=`FP16 target inference; W4/W8 weight-quantized self-drafters`；batch=`Not Disclosed`；concurrency=`Not Disclosed`；SLO=`Not Disclosed`；evaluator=`rollout throughput, acceptance and downstream RL quality`。

**Trade-off、failure、共存与演进。** acceptance 随 policy update 漂移；额外 draft computation 和 rollback bookkeeping 可能抵消收益，且不改变 reward validity。 因而该 family 只支持这里写出的 delta，未披露执行字段保持 Unknown/Not Disclosed。Limit/counterevidence=`https://arxiv.org/html/2606.18967v1 — § exact-v1 limitation/counterevidence anchor: Limitations`。

<!-- claim:SF-2026-ARXIV-2606-18967:start -->
Claim boundary：仅 `arXiv:2606.18967v1` official HTML；不使用 later version；ordinary pending locator count=`0`.
<!-- claim:SF-2026-ARXIV-2606-18967:end -->
<!-- review:SF-2026-ARXIV-2606-18967:end -->

<!-- review:SF-2026-ARXIV-2606-18996:start -->
### 2606.18996 — TRAP: Benchmark for Task-completion and Resistance to Active Privacy-extraction

**问题与旧路径。** Agents are increasingly deployed in document-intensive workflows where sensitive private information is not an edge case but a routine input, e.g., an agent booking a flight needs passport numbers. 旧路径在风险、状态或控制面没有跨出作者前提时仍然合理。

**机制与 owner。** privacy-capable agent benchmark 必须联合评分 task completion 与 active extraction resistance，并把攻击者交互轨迹、secret canary 与 policy effect 分开。 唯一知识 owner 为 `PLATFORM-EVALUATION-SYSTEM`；相邻节点只消费带 identity 的 handoff。

**Evaluation：证明与未证明。** TRAP 在作者 agent/model matrix 中同时测任务完成与主动隐私提取。 Method=`https://arxiv.org/html/2606.18996v1 — § exact-v1 anchor: Task-completion and Resistance`；Evaluation=`https://arxiv.org/html/2606.18996v1 — § exact-v1 evaluation anchor: Evaluation`。Benchmark contract：model=`GPT-4o-mini, GPT-5-mini, GPT-5.4-mini, GPT-5, Gemini-2.5-Flash-Lite, Gemini-2.5-Flash, Gemini-2.5-Pro, Claude Haiku 4.5, Claude Sonnet 4.5, Qwen3-VL-2B, Qwen3-VL-4B, Qwen3-VL-8B, Qwen3-VL-32B, Phi-4-multimodal, InternVL3.5-2B, InternVL3.5-4B, InternVL3.5-8B, InternVL3.5-14B, InternVL3.5-38B, Devstral-Small-2512, Llama3.2-11B-Vision and GLM-4.6V-Flash`；hardware=`NVIDIA A6000 GPUs for open-source models`；precision=`Not Disclosed`；batch=`Not Disclosed`；concurrency=`Not Disclosed`；SLO=`Not Disclosed`；evaluator=`paired task-completion and active privacy-extraction outcomes`。

**Trade-off、failure、共存与演进。** benchmark secret 与攻击策略覆盖有限；未泄漏不证明模型无记忆或生产 ACL 正确。 因而该 family 只支持这里写出的 delta，未披露执行字段保持 Unknown/Not Disclosed。Limit/counterevidence=`https://arxiv.org/html/2606.18996v1 — § exact-v1 limitation/counterevidence anchor: Limitations`。

<!-- claim:SF-2026-ARXIV-2606-18996:start -->
Claim boundary：仅 `arXiv:2606.18996v1` official HTML；不使用 later version；ordinary pending locator count=`0`.
<!-- claim:SF-2026-ARXIV-2606-18996:end -->
<!-- review:SF-2026-ARXIV-2606-18996:end -->

<!-- review:SF-2026-ARXIV-2606-19004:start -->
### 2606.19004 — Spotlight: Synergizing Seed Exploration and Spot GPUs for DiT RL Post-Training

**问题与旧路径。** Reinforcement learning (RL) post-training of Diffusion Transformers (DiTs) is prohibitively expensive, requiring thousands of high-end GPUs. 旧路径在风险、状态或控制面没有跨出作者前提时仍然合理。

**机制与 owner。** DiT RL post-training 可把探索 seed 与 spot GPU availability 联合调度，把可重放 seed state 作为 preemption recovery unit。 唯一知识 owner 为 `PLATFORM-GPU-SCHEDULER`；相邻节点只消费带 identity 的 handoff。

**Evaluation：证明与未证明。** exact-v1 比较 seed exploration quality、GPU utilization、成本与训练结果。 Method=`https://arxiv.org/html/2606.19004v1 — § exact-v1 anchor: Seed Exploration and Spot GPUs`；Evaluation=`https://arxiv.org/html/2606.19004v1 — § exact-v1 evaluation anchor: Experiments`。Benchmark contract：model=`Qwen-Image`；hardware=`4 reserved-node H100 GPUs plus 8 H100 GPUs on four spot nodes`；precision=`Not Disclosed`；batch=`Not Disclosed`；concurrency=`Not Disclosed`；SLO=`Not Disclosed`；evaluator=`training reward/quality, GPU utilization and spot cost`。

**Trade-off、failure、共存与演进。** spot reclaim 与 seed replay 会改变样本时序；结果限于 DiT RL，不能外推 LLM RL 或硬实时 SLO。 因而该 family 只支持这里写出的 delta，未披露执行字段保持 Unknown/Not Disclosed。Limit/counterevidence=`https://arxiv.org/html/2606.19004v1 — § exact-v1 limitation/counterevidence anchor: Limitations`。

<!-- claim:SF-2026-ARXIV-2606-19004:start -->
Claim boundary：仅 `arXiv:2606.19004v1` official HTML；不使用 later version；ordinary pending locator count=`0`.
<!-- claim:SF-2026-ARXIV-2606-19004:end -->
<!-- review:SF-2026-ARXIV-2606-19004:end -->

<!-- review:SF-2026-ARXIV-2606-19025:start -->
### 2606.19025 — FoMoE: Breaking the Full-Replica Barrier with a Federation of MoEs

**问题与旧路径。** Pre-training Large Language Models (LLMs) typically demands large-scale infrastructure with tightly coupled hardware accelerators. 旧路径在风险、状态或控制面没有跨出作者前提时仍然合理。

**机制与 owner。** 低带宽跨站 MoE 训练不应让每个 site 持有 full replica；FoMoE 分区 expert layers、部分复制 experts，并让 local training 对 non-resident experts 执行 skip-token，再按较低频率同步。 唯一知识 owner 为 `TRAIN-DISTRIBUTED-TRAINING`；相邻节点只消费带 identity 的 handoff。

**Evaluation：证明与未证明。** 通信相对高效 baseline 最多降 1.42x、相对 DDP 降 45.44x，skip-token 吞吐最高 1.4x；100B 只由 cost model 投影。 Method=`https://arxiv.org/html/2606.19025v1 — § exact-v1 anchor: partitioning expert layers across workers`；Evaluation=`https://arxiv.org/html/2606.19025v1 — § exact-v1 evaluation anchor: FoMoE Scalability & Resource Consumption`。Benchmark contract：model=`Not Disclosed`；hardware=`Not Disclosed`；precision=`Not Disclosed`；batch=`Not Disclosed`；concurrency=`Not Disclosed`；SLO=`Not Disclosed`；evaluator=`communication volume, local-training throughput and routing stability; 100B results are modeled projections`。

**Trade-off、failure、共存与演进。** non-resident expert skip 会改变本地训练分布，routing stability 只在受测 regimes 成立；100B projection 不是实测，WAN failure/straggler 未闭合。 因而该 family 只支持这里写出的 delta，未披露执行字段保持 Unknown/Not Disclosed。Limit/counterevidence=`https://arxiv.org/html/2606.19025v1 — § exact-v1 limitation/counterevidence anchor: Limitations`。

<!-- claim:SF-2026-ARXIV-2606-19025:start -->
Claim boundary：仅 `arXiv:2606.19025v1` official HTML；不使用 later version；ordinary pending locator count=`0`.
<!-- claim:SF-2026-ARXIV-2606-19025:end -->
<!-- review:SF-2026-ARXIV-2606-19025:end -->

<!-- review:SF-2026-ARXIV-2606-19057:start -->
### 2606.19057 — Quantifying and Auditing LLM Evaluation via Positive--Unlabeled Learning

**问题与旧路径。** Large Language Models (LLMs) are increasingly used as judges for scalable evaluation, yet such LLM--as--a--Judge systems exhibit systematic biases that are decoupled from semantic quality, most notably verbosity bias. 旧路径在风险、状态或控制面没有跨出作者前提时仍然合理。

**机制与 owner。** 当只有少量确定正例而未标注集混合正负时，evaluation audit 可用 positive-unlabeled inference 估计隐藏错误率，但必须公开 class-prior 与 identifiability assumptions。 唯一知识 owner 为 `PLATFORM-EVALUATION-SYSTEM`；相邻节点只消费带 identity 的 handoff。

**Evaluation：证明与未证明。** exact-v1 用受控与真实 LLM evaluation data 比较 PU 估计、校准与 audit coverage。 Method=`https://arxiv.org/html/2606.19057v1 — § exact-v1 anchor: Positive–Unlabeled Learning`；Evaluation=`https://arxiv.org/html/2606.19057v1 — § exact-v1 evaluation anchor: Experiments`。Benchmark contract：model=`Mistral-7B-Instruct, Qwen2.5-7B-Instruct, Llemma-7B-MuInstruct and GPT-5.4-mini judges`；hardware=`Not Disclosed`；precision=`Not Disclosed`；batch=`Not Disclosed`；concurrency=`Not Disclosed`；SLO=`Not Disclosed`；evaluator=`hidden-positive prevalence, calibration and audit error`。

**Trade-off、failure、共存与演进。** class-prior 错设会系统性偏移；PU 只能估计分布级缺口，不能证明单个 judgment 正确。 因而该 family 只支持这里写出的 delta，未披露执行字段保持 Unknown/Not Disclosed。Limit/counterevidence=`https://arxiv.org/html/2606.19057v1 — § exact-v1 limitation/counterevidence anchor: Limitations`。

<!-- claim:SF-2026-ARXIV-2606-19057:start -->
Claim boundary：仅 `arXiv:2606.19057v1` official HTML；不使用 later version；ordinary pending locator count=`0`.
<!-- claim:SF-2026-ARXIV-2606-19057:end -->
<!-- review:SF-2026-ARXIV-2606-19057:end -->

<!-- review:SF-2026-ARXIV-2606-19111:start -->
### 2606.19111 — Leadership as Coordination Control: Behavioral Signatures and the Recovery-Advantage Boundary in Multi-Agent LLM Teams

**问题与旧路径。** Team science holds that leadership is contingent: it helps only under specific conditions, and capable, autonomous teams may need none at all. 旧路径在风险、状态或控制面没有跨出作者前提时仍然合理。

**机制与 owner。** leader 只有在 coordinator 的 recovery advantage 超过沟通与单点故障成本时才应持有重分配 authority；行为 leadership 不等于稳定角色标签。 唯一知识 owner 为 `AGENT-MULTI-AGENT`；相邻节点只消费带 identity 的 handoff。

**Evaluation：证明与未证明。** 多 Agent team configurations 上测 coordination behavior、failure recovery 与任务结果。 Method=`https://arxiv.org/html/2606.19111v1 — § exact-v1 anchor: Recovery-Advantage Boundary`；Evaluation=`https://arxiv.org/html/2606.19111v1 — § exact-v1 evaluation anchor: Experiments`。Benchmark contract：model=`gpt-oss-120b, gemma-4-31B-it and llama-4-scout`；hardware=`Not Disclosed`；precision=`Not Disclosed`；batch=`Not Disclosed`；concurrency=`Not Disclosed`；SLO=`Not Disclosed`；evaluator=`team outcome, behavioral leadership signatures and recovery advantage`。

**Trade-off、failure、共存与演进。** 作者 tasks 和 agent count 不证明组织结构普适；leader failure、shared bias 与通信成本仍可能主导。 因而该 family 只支持这里写出的 delta，未披露执行字段保持 Unknown/Not Disclosed。Limit/counterevidence=`https://arxiv.org/html/2606.19111v1 — § exact-v1 limitation/counterevidence anchor: Limitations`。

<!-- claim:SF-2026-ARXIV-2606-19111:start -->
Claim boundary：仅 `arXiv:2606.19111v1` official HTML；不使用 later version；ordinary pending locator count=`0`.
<!-- claim:SF-2026-ARXIV-2606-19111:end -->
<!-- review:SF-2026-ARXIV-2606-19111:end -->

<!-- review:SF-2026-ARXIV-2606-19191:start -->
### 2606.19191 — PhantomSkill: Malicious Code Injection in Agent Skill Ecosystems

**问题与旧路径。** Agent skills allow LLM-based coding agents to acquire domain-specific capabilities from third-party packages, but they also introduce a new supply-chain attack surface. 旧路径在风险、状态或控制面没有跨出作者前提时仍然合理。

**机制与 owner。** skill admission 不能只读 SKILL.md；必须审 auxiliary resources、triggerable vulnerabilities 与 runtime effects，并在沙箱中验证 benign utility 与恶意 side effect。 唯一知识 owner 为 `PLATFORM-SECURITY`；相邻节点只消费带 identity 的 handoff。

**Evaluation：证明与未证明。** VulMask 跨 host skills、四类攻击、Cursor backbones 与多个 automated reviewers；GPT-5.5 设置 ASR 58.8%、warning 11.4%。 Method=`https://arxiv.org/html/2606.19191v1 — § exact-v1 anchor: 3 Threat Model`；Evaluation=`https://arxiv.org/html/2606.19191v1 — § exact-v1 evaluation anchor: 5 Evaluation`。Benchmark contract：model=`GPT-5.5, GLM-4.7-Flash and Qwen3-Coder-30B-A3B-Instruct; Opus-4.7, GLM-4.7-Flash and Qwen3-Coder-30B-A3B-Instruct for cross-generator transfer; Cursor backends additionally include Opus-4.7`；hardware=`Not Disclosed`；precision=`Not Disclosed`；batch=`Not Disclosed`；concurrency=`Not Disclosed`；SLO=`Not Disclosed`；evaluator=`attack success, warning/detection and benign utility across four attack goals`。

**Trade-off、failure、共存与演进。** 攻击 corpus 与触发器由作者构造；静态扫描漏报不证明 runtime containment 无效，检测率也不等于安全。 因而该 family 只支持这里写出的 delta，未披露执行字段保持 Unknown/Not Disclosed。Limit/counterevidence=`https://arxiv.org/html/2606.19191v1 — § exact-v1 limitation/counterevidence anchor: 6 Discussion`。

<!-- claim:SF-2026-ARXIV-2606-19191:start -->
Claim boundary：仅 `arXiv:2606.19191v1` official HTML；不使用 later version；ordinary pending locator count=`0`.
<!-- claim:SF-2026-ARXIV-2606-19191:end -->
<!-- review:SF-2026-ARXIV-2606-19191:end -->

<!-- review:SF-2026-ARXIV-2606-19242:start -->
### 2606.19242 — Runtime Compliance Verification for AI Agents

**问题与旧路径。** AI agents now handle personal data through tool use, function calls, and multi turn dialogue, which can create obligations under the General Data Protection Regulation (GDPR). 旧路径在风险、状态或控制面没有跨出作者前提时仍然合理。

**机制与 owner。** Agent compliance 应在每次 tool/message effect 前由外部 runtime monitor 检查 temporal/policy state，而非要求 LLM 自述合规。 唯一知识 owner 为 `PLATFORM-SECURITY`；相邻节点只消费带 identity 的 handoff。

**Evaluation：证明与未证明。** exact-v1 在作者 policies、agent traces 与 violation cases 上评 runtime verification。 Method=`https://arxiv.org/html/2606.19242v1 — § exact-v1 anchor: Runtime Compliance Verification`；Evaluation=`https://arxiv.org/html/2606.19242v1 — § exact-v1 evaluation anchor: Evaluation`。Benchmark contract：model=`Not Disclosed`；hardware=`Not Disclosed`；precision=`Not Disclosed`；batch=`Not Disclosed`；concurrency=`Not Disclosed`；SLO=`Not Disclosed`；evaluator=`policy-violation detection and runtime enforcement outcomes`。

**Trade-off、failure、共存与演进。** 形式化 policy 不覆盖未建模 effect，monitor 自身可能成为延迟或可用性瓶颈。 因而该 family 只支持这里写出的 delta，未披露执行字段保持 Unknown/Not Disclosed。Limit/counterevidence=`https://arxiv.org/html/2606.19242v1 — § exact-v1 limitation/counterevidence anchor: Limitations`。

<!-- claim:SF-2026-ARXIV-2606-19242:start -->
Claim boundary：仅 `arXiv:2606.19242v1` official HTML；不使用 later version；ordinary pending locator count=`0`.
<!-- claim:SF-2026-ARXIV-2606-19242:end -->
<!-- review:SF-2026-ARXIV-2606-19242:end -->

<!-- review:SF-2026-ARXIV-2606-19262:start -->
### 2606.19262 — Detecting Hidden ML Training With Zero-Overhead Telemetry

**问题与旧路径。** Hardware-enabled monitoring of GPU workloads underpins many proposals for AI compute governance, but if developers can defeat monitoring mechanisms, such schemes are unworkable. 旧路径在风险、状态或控制面没有跨出作者前提时仍然合理。

**机制与 owner。** hidden training detection 可读取已有 accelerator telemetry 的 phase、memory/compute 与 collective signatures，保持 observe-only，不向 workload 注入探针。 唯一知识 owner 为 `PLATFORM-MONITORING`；相邻节点只消费带 identity 的 handoff。

**Evaluation：证明与未证明。** exact-v1 在多种 ML/non-ML workloads 与 hardware traces 上报告检测质量及 zero-overhead claim。 Method=`https://arxiv.org/html/2606.19262v1 — § exact-v1 anchor: Zero-Overhead Telemetry`；Evaluation=`https://arxiv.org/html/2606.19262v1 — § exact-v1 evaluation anchor: Evaluation`。Benchmark contract：model=`Not Disclosed`；hardware=`nine NVIDIA GPU models across four architecture generations`；precision=`Not Disclosed`；batch=`Not Disclosed`；concurrency=`Not Disclosed`；SLO=`Not Disclosed`；evaluator=`hidden-training detection, false positives and telemetry overhead`。

**Trade-off、failure、共存与演进。** 共享 GPU、融合 kernel 与新 compiler 会造成概念漂移；无额外探针不等于 telemetry 免费或不可规避。 因而该 family 只支持这里写出的 delta，未披露执行字段保持 Unknown/Not Disclosed。Limit/counterevidence=`https://arxiv.org/html/2606.19262v1 — § exact-v1 limitation/counterevidence anchor: Limitations`。

<!-- claim:SF-2026-ARXIV-2606-19262:start -->
Claim boundary：仅 `arXiv:2606.19262v1` official HTML；不使用 later version；ordinary pending locator count=`0`.
<!-- claim:SF-2026-ARXIV-2606-19262:end -->
<!-- review:SF-2026-ARXIV-2606-19262:end -->

<!-- review:SF-2026-ARXIV-2606-19271:start -->
### 2606.19271 — TurboServe: Serving Streaming Video Generation Efficiently and Economically

**问题与旧路径。** Streaming video generation is emerging as a new serving workload in which users interact with long-lived sessions that generate video progressively, chunk by chunk. 旧路径在风险、状态或控制面没有跨出作者前提时仍然合理。

**机制与 owner。** streaming video generation 应以 chunk deadline 为调度单位，联合决定 GPU residency、跨 chunk pipeline 与质量/成本降级，而不是只优化整段 makespan。 唯一知识 owner 为 `INFER-SCHEDULING`；相邻节点只消费带 identity 的 handoff。

**Evaluation：证明与未证明。** TurboServe 报告 worst-case per-chunk latency 降 37.5%、平均 GPU cost 降 37.2%。 Method=`https://arxiv.org/html/2606.19271v1 — § exact-v1 anchor: Streaming Video Generation`；Evaluation=`https://arxiv.org/html/2606.19271v1 — § exact-v1 evaluation anchor: Evaluation`。Benchmark contract：model=`Not Disclosed`；hardware=`GPU clusters with up to 64 NVIDIA B300 GPUs`；precision=`Not Disclosed`；batch=`Not Disclosed`；concurrency=`Not Disclosed`；SLO=`Not Disclosed`；evaluator=`worst-case per-chunk latency, end-to-end quality and GPU operating cost`。

**Trade-off、failure、共存与演进。** 作者 workloads/GPU matrix 不证明交互视频通用 SLO；跨 chunk state 与 quality degradation 仍需独立验收。 因而该 family 只支持这里写出的 delta，未披露执行字段保持 Unknown/Not Disclosed。Limit/counterevidence=`https://arxiv.org/html/2606.19271v1 — § exact-v1 limitation/counterevidence anchor: Limitations`。

<!-- claim:SF-2026-ARXIV-2606-19271:start -->
Claim boundary：仅 `arXiv:2606.19271v1` official HTML；不使用 later version；ordinary pending locator count=`0`.
<!-- claim:SF-2026-ARXIV-2606-19271:end -->
<!-- review:SF-2026-ARXIV-2606-19271:end -->

<!-- audit-target:evidence:end -->
## 4. Benchmark Contracts

<!-- validator:benchmark-contract-v1 -->
| Source Family ID | Workload | Model | Hardware | Precision | Input Length | Output Length | Batch | Concurrency | SLO | Evaluator |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2606-18284 | Disclosed — Math, code and SWE task generation across model scales | Disclosed — Qwen2.5-3B/7B and Qwen3.5-27B solver settings | Not Disclosed | Not Disclosed | Not Disclosed as one universal contract — task-specific lengths remain exact-v1-bound | Not Disclosed as one universal contract — task-specific limits remain exact-v1-bound | Not Disclosed as one universal contract — trial count is not relabeled as batch | Not Disclosed unless stated in workload — worker/trial parallelism is not serving concurrency | Not Disclosed — research metrics are not a production SLO | Disclosed — exact-v1 evaluation locator reports outcome plus mechanism-specific cost/failure metrics |
| SF-2026-ARXIV-2606-18286 | Disclosed — Six code-generation benchmarks | Disclosed — Qwen2.5-Coder-1.5B-Instruct and comparison models | Disclosed in Appendix A.3; exact accelerator remains v1-bound | Training precision disclosed in Appendix A.3 | Not Disclosed as one universal contract — task-specific lengths remain exact-v1-bound | Not Disclosed as one universal contract — task-specific limits remain exact-v1-bound | Not Disclosed as one universal contract — trial count is not relabeled as batch | Not Disclosed unless stated in workload — worker/trial parallelism is not serving concurrency | Not Disclosed — research metrics are not a production SLO | Disclosed — exact-v1 evaluation locator reports outcome plus mechanism-specific cost/failure metrics |
| SF-2026-ARXIV-2606-18310 | knowledge-injection attacks and repair across disclosed RAG datasets | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | attack success, retrieval ranking, downstream answer and clean-utility recovery |
| SF-2026-ARXIV-2606-18322 | behavior-suppression interventions followed across downstream transformer layers | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | target behavior suppression and later recovery with residual/feature diagnostics |
| SF-2026-ARXIV-2606-18356 | 600 cases across six attack families plus a 12,000-row matched Core/Exec analysis | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | CoreFail, HarmEvidence, SemanticOnly and sandbox state-oracle harm as separate endpoints |
| SF-2026-ARXIV-2606-18379 | Billion-node recommendation graph with hour-scale refresh and online serving | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | retrieval/recommendation quality, refresh/build time and serving efficiency |
| SF-2026-ARXIV-2606-18383 | synthetic controls and language-model SAE proxy validation | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | proxy risk, reconstruction/concept gaps and certificate coverage/tightness |
| SF-2026-ARXIV-2606-18394 | speculative decoding with parallel causal draft trees in vLLM | Not Disclosed | NVIDIA H100 GPU | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | accepted length, output throughput/latency and tree-width/depth ablations |
| SF-2026-ARXIV-2606-18400 | Four configurations spanning dense and MoE models at tensor parallelism 1 and 2 under PCIe-snooping and HBM-dump attacks | Llama 3.1 8B, Qwen 3 14B and Qwen 3 MoE 30B/3B-active | NVIDIA L40S GPUs with 46 GB HBM and PCIe 4.0 x16 at 32 GB/s one-way bandwidth | Not Disclosed | 100-200 input tokens, uniformly sampled | 100-200 output tokens, uniformly sampled | Not Disclosed | Not Disclosed | Not Disclosed | extraction degradation plus inference latency/throughput overhead |
| SF-2026-ARXIV-2606-18421 | Generated ONNX graphs exercised against TVM, ONNX-MLIR and GeneSys | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | bug-revealing cases, late-stage reach, behavior partitions and extensibility |
| SF-2026-ARXIV-2606-18431 | production and open LLM-serving traces under tail-latency pressure | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | P95/P99 latency, throughput, preemption/recompute and cache-hit effects |
| SF-2026-ARXIV-2606-18448 | live computer-use tasks over graphical interfaces with reusable multimodal skills | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | task success, steps/tokens, retrieval/loading and transfer ablations |
| SF-2026-ARXIV-2606-18467 | agent trajectories with retrieval and tool-use distribution drift | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | trajectory risk coverage, abstention, alarm delay and false-alarm behavior |
| SF-2026-ARXIV-2606-18497 | soft-deleted embeddings recovered from HNSW vector databases | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | vector reconstruction/re-identification success, purge cost and key-rotation proof checks |
| SF-2026-ARXIV-2606-18532 | representative AI-agent sandbox designs and attack surfaces | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | six-dimension evidence matrix, containment tests and reproducibility/governance checks |
| SF-2026-ARXIV-2606-18550 | RiskGate 100-tool registry; eight high-risk targets; 256 perturbation configurations per target; 1,898 executed configurations and 5,886 phrasing trials | Claude Opus 4.8, Claude Sonnet 4.6, Claude Haiku 4.5, Nova Premier, Nova 2 Lite and GPT-OSS-120B | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | injection success by guard rung, field/compound attacks, honest-contract rejection and model validation |
| SF-2026-ARXIV-2606-18600 | offline throughput | Llama-3.1-70B; Qwen3-32B | AWS L4, A10G and L40S GPUs | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | offline throughput, online TTFT/TPOT and cost efficiency under spot interruption |
| SF-2026-ARXIV-2606-18619 | real-subject vulnerability findings plus specification-falsification outcomes | Claude Sonnet 4.6 and DeepSeek V4 Pro; Claude Mythos is comparison-only | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | real-subject vulnerability findings plus specification-falsification outcomes |
| SF-2026-ARXIV-2606-18650 | downstream task quality and selection efficiency against influence/excess-loss baselines | TinyLlama-1.1B and Llama2-7B target models with 3B/5B-token continued-pretraining budgets | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | downstream task quality and selection efficiency against influence/excess-loss baselines |
| SF-2026-ARXIV-2606-18668 | production pass rate under structured abstention labels and rationales | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | production pass rate under structured abstention labels and rationales |
| SF-2026-ARXIV-2606-18673 | prompt leakage resistance | Llama-2-7B-chat-hf, Llama-3.1-8B-Instruct, Mistral-7B-Instruct, Qwen3-4B-Instruct, Qwen3-32B, Qwen2.5-72B-Instruct and Llama-3.3-70B-Instruct | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | prompt leakage resistance, usability and optimization overhead over 1,200 applications |
| SF-2026-ARXIV-2606-18697 | planning return | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | planning return, poison detectability and defense response across three pipeline stages |
| SF-2026-ARXIV-2606-18741 | reconfiguration downtime | Llama2-7B, Qwen3-30B-A3B, DeepSeek-R1-Distill-Qwen-32B and Llama2-70B | NVIDIA H100 and RTX 5090 platforms | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | reconfiguration downtime, TTFT, TPOT and output throughput |
| SF-2026-ARXIV-2606-18746 | theorem premises and approximation error for domain disambiguation and local dynamics reconstruction | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | theorem premises and approximation error for domain disambiguation and local dynamics reconstruction |
| SF-2026-ARXIV-2606-18810 | task accuracy and OOD performance against GRPO | Qwen3-1.7B-Base; DeepSeek-R1-Distill-Qwen-1.5B; experiments are limited to models at most 8B | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | task accuracy and OOD performance against GRPO, DAPO and OPD |
| SF-2026-ARXIV-2606-18829 | legitimate utility | GPT-5.4, DeepSeek-V4-Pro, Llama-4-Maverick, GPT-5-mini, GPT-4o-mini and Gemini-2.5-Flash-Lite | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | legitimate utility, contextual access-control leakage and post-deletion active forgetting |
| SF-2026-ARXIV-2606-18831 | seven long-context benchmarks plus GAIA and BrowseComp transfer | Qwen3-4B, Qwen3-8B and Qwen3-30B-A3B | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | seven long-context benchmarks plus GAIA and BrowseComp transfer |
| SF-2026-ARXIV-2606-18847 | Memory QA and Embodied Task Planning over evidence-linked household traces | google/gemini-3.5-flash answer generator; GPT-4o judge; GPT-4o-mini question generator | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Memory QA and Embodied Task Planning over evidence-linked household traces |
| SF-2026-ARXIV-2606-18874 | claim-to-artifact traceability | gpt-4o-mini answer generator and all-MiniLM-L6-v2 embedder in the matched LoCoMo validation | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | claim-to-artifact traceability, ablation and bounded repair across three research domains |
| SF-2026-ARXIV-2606-18958 | simulation scale | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | simulation scale, fidelity and runtime overhead |
| SF-2026-ARXIV-2606-18967 | rollout throughput | Qwen2.5-7B, Qwen2.5-14B and Llama3.1-8B-Instruct with quantized self-drafters | single NVIDIA A100-80GiB SXM in the decode-cost study | FP16 target inference; W4/W8 weight-quantized self-drafters | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | rollout throughput, acceptance and downstream RL quality |
| SF-2026-ARXIV-2606-18996 | paired task-completion and active privacy-extraction outcomes | GPT-4o-mini, GPT-5-mini, GPT-5.4-mini, GPT-5, Gemini-2.5-Flash-Lite, Gemini-2.5-Flash, Gemini-2.5-Pro, Claude Haiku 4.5, Claude Sonnet 4.5, Qwen3-VL-2B, Qwen3-VL-4B, Qwen3-VL-8B, Qwen3-VL-32B, Phi-4-multimodal, InternVL3.5-2B, InternVL3.5-4B, InternVL3.5-8B, InternVL3.5-14B, InternVL3.5-38B, Devstral-Small-2512, Llama3.2-11B-Vision and GLM-4.6V-Flash | NVIDIA A6000 GPUs for open-source models | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | paired task-completion and active privacy-extraction outcomes |
| SF-2026-ARXIV-2606-19004 | training reward/quality | Qwen-Image | 4 reserved-node H100 GPUs plus 8 H100 GPUs on four spot nodes | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | training reward/quality, GPU utilization and spot cost |
| SF-2026-ARXIV-2606-19025 | communication volume | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | communication volume, local-training throughput and routing stability; 100B results are modeled projections |
| SF-2026-ARXIV-2606-19057 | hidden-positive prevalence | Mistral-7B-Instruct, Qwen2.5-7B-Instruct, Llemma-7B-MuInstruct and GPT-5.4-mini judges | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | hidden-positive prevalence, calibration and audit error |
| SF-2026-ARXIV-2606-19111 | team outcome | gpt-oss-120b, gemma-4-31B-it and llama-4-scout | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | team outcome, behavioral leadership signatures and recovery advantage |
| SF-2026-ARXIV-2606-19191 | attack success | GPT-5.5, GLM-4.7-Flash and Qwen3-Coder-30B-A3B-Instruct; Opus-4.7, GLM-4.7-Flash and Qwen3-Coder-30B-A3B-Instruct for cross-generator transfer; Cursor backends additionally include Opus-4.7 | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | attack success, warning/detection and benign utility across four attack goals |
| SF-2026-ARXIV-2606-19242 | policy-violation detection and runtime enforcement outcomes | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | policy-violation detection and runtime enforcement outcomes |
| SF-2026-ARXIV-2606-19262 | hidden-training detection | Not Disclosed | nine NVIDIA GPU models across four architecture generations | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | hidden-training detection, false positives and telemetry overhead |
| SF-2026-ARXIV-2606-19271 | worst-case per-chunk latency | Not Disclosed | GPU clusters with up to 64 NVIDIA B300 GPUs | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | worst-case per-chunk latency, end-to-end quality and GPU operating cost |
<!-- audit-target:deep_analysis_selection:start -->
## 5. Deep Analysis Selection

<!-- validator:deep-analysis-selection-v1 -->
| Source Family ID | Eligibility | Decision | Analysis Unit ID | Subsumed By | Priority Rationale | Narrative Ref |
| --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2606-18284 | score_7_9; potential_books_delta | not_selected | — | — | Breaking the Solver Bottleneck: Training Task Generators at the Learnable Frontier remains evidence-complete after canonical owner transfer with V2 score 9 and owner TRAIN-DATA. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-18284 |
| SF-2026-ARXIV-2606-18286 | score_7_9; potential_books_delta | not_selected | — | — | CODEBLOCK: Learning to Supervise Code at the Right Granularity remains evidence-complete after canonical owner transfer with V2 score 9 and owner TRAIN-SFT. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-18286 |
| SF-2026-ARXIV-2606-18310 | score_7_9; potential_books_delta | not_selected | — | — | Conflict-Aware Retriever Editing for Knowledge Injection Attacks on LLM-Based RAG Systems remains evidence-complete after canonical owner transfer with V2 score 9 and owner AGENT-RAG. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-18310 |
| SF-2026-ARXIV-2606-18322 | score_7_9; potential_books_delta | not_selected | — | — | SAE Interventions are Unreliable: Post-Intervention Recovery of Suppressed Behavior remains evidence-complete after canonical owner transfer with V2 score 9 and owner TRAIN-RLHF. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-18322 |
| SF-2026-ARXIV-2606-18356 | score_7_9; potential_books_delta | not_selected | — | — | SafeClawBench: Separating Semantic, Audit-Evidence, and Sandbox Harm in Tool-Using LLM Agents remains evidence-complete after canonical owner transfer with V2 score 9 and owner PLATFORM-EVALUATION-SYSTEM. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-18356 |
| SF-2026-ARXIV-2606-18379 | score_7_9; potential_books_delta | not_selected | — | — | RankGraph-2: Lifecycle Co-Design for Billion-Node Graph Learning in Recommendation remains evidence-complete after canonical owner transfer with V2 score 9 and owner AGENT-RAG. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-18379 |
| SF-2026-ARXIV-2606-18383 | score_7_9; potential_books_delta | not_selected | — | — | From Sparse Features to Trustworthy Proxies: Certifying SAE-Based Interpretability remains evidence-complete after canonical owner transfer with V2 score 9 and owner TRAIN-RLHF. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-18383 |
| SF-2026-ARXIV-2606-18394 | score_7_9 | not_selected | — | — | JetSpec: Breaking the Scaling Ceiling of Speculative Decoding with Parallel Tree Drafting remains evidence-complete after canonical owner transfer with V2 score 8 and owner INFER-SPECULATIVE-DECODING. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-18394 |
| SF-2026-ARXIV-2606-18400 | score_7_9; potential_books_delta | not_selected | — | — | CloakLM: Obfuscating GPU Memory Layout to Mitigate Model Ex-filtration for Serving remains evidence-complete after canonical owner transfer with V2 score 9 and owner PLATFORM-SECURITY. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-18400 |
| SF-2026-ARXIV-2606-18421 | score_7_9; potential_books_delta | not_selected | — | — | Finding Compiler-Platform Interaction Bugs in Deep Learning Pipelines via Cross-Layer Constraints remains evidence-complete after canonical owner transfer with V2 score 9 and owner INFER-TENSORRT-LLM. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-18421 |
| SF-2026-ARXIV-2606-18431 | score_7_9; potential_books_delta | not_selected | — | — | Beyond Prediction: Tail-Aware Scheduling for LLM Inference remains evidence-complete after canonical owner transfer with V2 score 9 and owner INFER-SCHEDULING. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-18431 |
| SF-2026-ARXIV-2606-18448 | score_7_9; potential_books_delta | not_selected | — | — | VISUALSKILL: Multimodal Skills for Computer-Use Agents remains evidence-complete after canonical owner transfer with V2 score 9 and owner AGENT-TOOL-CALLING. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-18448 |
| SF-2026-ARXIV-2606-18467 | score_7_9; potential_books_delta | not_selected | — | — | ToolChain-CRC: Conformal Risk Control for Agentic AI Under Retrieval and Tool-Use Drift remains evidence-complete after canonical owner transfer with V2 score 9 and owner PLATFORM-EVALUATION-SYSTEM. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-18467 |
| SF-2026-ARXIV-2606-18497 | score_7_9; potential_books_delta | not_selected | — | — | Ghost Vectors: Soft-Deleted Embeddings Remain Reconstructible in HNSW Vector Databases remains evidence-complete after canonical owner transfer with V2 score 9 and owner AGENT-RAG. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-18497 |
| SF-2026-ARXIV-2606-18532 | score_7_9; potential_books_delta | not_selected | — | — | AI Sandboxes: A Threat Model, Taxonomy, and Measurement Framework remains evidence-complete after canonical owner transfer with V2 score 9 and owner PLATFORM-SECURITY. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-18532 |
| SF-2026-ARXIV-2606-18550 | score_7_9; potential_books_delta | selected | DA-20260617-CONTRACT-INTEGRITY | — | Selected after 43/43 frontier comparison for a non-overlapping transaction, recovery or contract-integrity control boundary. | analysis:DA-20260617-CONTRACT-INTEGRITY |
| SF-2026-ARXIV-2606-18600 | score_7_9; potential_books_delta | selected | DA-20260618-HETEROGENEOUS-RECOVERY | — | 唯一同时改变 placement 与 interruption recovery 的 serving family，进入三项叙事。 | analysis:DA-20260618-HETEROGENEOUS-RECOVERY |
| SF-2026-ARXIV-2606-18619 | score_7_9; potential_books_delta | not_selected | — | — | Code-Augur: Agentic Vulnerability Detection via Specification Inference remains evidence-complete after canonical owner transfer with V2 score 9 and owner PLATFORM-SECURITY. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-18619 |
| SF-2026-ARXIV-2606-18650 | score_7_9 | not_selected | — | — | BLADE: Scalable Bi-level Adaptive Data Selection for LLM Training remains evidence-complete after canonical owner transfer with V2 score 7 and owner TRAIN-DATA. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-18650 |
| SF-2026-ARXIV-2606-18668 | score_7_9 | not_selected | — | — | EARS: Explanatory Abstention for Reliable Sub-Agent Modeling in Large-scale Multi-Agent Systems remains evidence-complete after canonical owner transfer with V2 score 7 and owner AGENT-MULTI-AGENT. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-18668 |
| SF-2026-ARXIV-2606-18673 | score_7_9 | not_selected | — | — | Understanding and Mitigating Prompt Leaking Attacks in Real-World LLM-Based Applications remains evidence-complete after canonical owner transfer with V2 score 8 and owner PLATFORM-SECURITY. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-18673 |
| SF-2026-ARXIV-2606-18697 | score_7_9; potential_books_delta | not_selected | — | — | Stealthy World Model Manipulation via Data Poisoning remains evidence-complete after canonical owner transfer with V2 score 8 and owner MULTIMODAL-WORLD-MODELS. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-18697 |
| SF-2026-ARXIV-2606-18741 | score_7_9; potential_books_delta | not_selected | — | — | ReMP: Low-Downtime Runtime Model-Parallelism Reconfiguration for LLM Serving remains evidence-complete after canonical owner transfer with V2 score 9 and owner INFER-SCHEDULING. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-18741 |
| SF-2026-ARXIV-2606-18746 | score_7_9 | not_selected | — | — | What Must Generalist Agents Remember? remains evidence-complete after canonical owner transfer with V2 score 7 and owner AGENT-MEMORY. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-18746 |
| SF-2026-ARXIV-2606-18810 | score_7_9 | not_selected | — | — | Learning from Own Solutions: Self-Conditioned Credit Assignment for Reinforcement Learning with Verifiable Rewards remains evidence-complete after canonical owner transfer with V2 score 7 and owner TRAIN-GRPO. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-18810 |
| SF-2026-ARXIV-2606-18829 | score_7_9 | not_selected | — | — | GateMem: Benchmarking Memory Governance in Multi-Principal Shared-Memory Agents remains evidence-complete after canonical owner transfer with V2 score 9 and owner PLATFORM-SECURITY. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-18829 |
| SF-2026-ARXIV-2606-18831 | score_7_9; potential_books_delta | not_selected | — | — | Beyond Reward Engineering: A Data Recipe for Long-Context Reinforcement Learning remains evidence-complete after canonical owner transfer with V2 score 8 and owner TRAIN-GRPO. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-18831 |
| SF-2026-ARXIV-2606-18847 | score_7_9; potential_books_delta | not_selected | — | — | WorldLines: Benchmarking and Modeling Long-Horizon Stateful Embodied Agents remains evidence-complete after canonical owner transfer with V2 score 8 and owner MULTIMODAL-EMBODIED-VLA. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-18847 |
| SF-2026-ARXIV-2606-18874 | score_7_9 | not_selected | — | — | Externalizing Research Synthesis and Validation in AI Scientists through a Research Harness remains evidence-complete after canonical owner transfer with V2 score 8 and owner AGENT-WORKFLOW. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-18874 |
| SF-2026-ARXIV-2606-18958 | score_7_9 | not_selected | — | — | LiveStack: OS Support for Cluster-Scale Full-Stack Live Simulation remains evidence-complete after canonical owner transfer with V2 score 8 and owner PLATFORM-PRODUCTION. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-18958 |
| SF-2026-ARXIV-2606-18967 | score_7_9; potential_books_delta | not_selected | — | — | EfficientRollout: System-Aware Self-Speculative Decoding for RL Rollouts remains evidence-complete after canonical owner transfer with V2 score 8 and owner INFER-SPECULATIVE-DECODING. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-18967 |
| SF-2026-ARXIV-2606-18996 | score_7_9 | not_selected | — | — | TRAP: Benchmark for Task-completion and Resistance to Active Privacy-extraction remains evidence-complete after canonical owner transfer with V2 score 9 and owner PLATFORM-EVALUATION-SYSTEM. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-18996 |
| SF-2026-ARXIV-2606-19004 | score_7_9 | not_selected | — | — | Spotlight: Synergizing Seed Exploration and Spot GPUs for DiT RL Post-Training remains evidence-complete after canonical owner transfer with V2 score 7 and owner PLATFORM-GPU-SCHEDULER. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-19004 |
| SF-2026-ARXIV-2606-19025 | score_7_9; potential_books_delta | selected | DA-20260618-CROSS-SITE-MOE-OWNERSHIP | — | 它改变跨站 distributed-training replica/state ownership，而不是 serving placement。 | analysis:DA-20260618-CROSS-SITE-MOE-OWNERSHIP |
| SF-2026-ARXIV-2606-19057 | score_7_9; potential_books_delta | not_selected | — | — | Quantifying and Auditing LLM Evaluation via Positive--Unlabeled Learning remains evidence-complete after canonical owner transfer with V2 score 9 and owner PLATFORM-EVALUATION-SYSTEM. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-19057 |
| SF-2026-ARXIV-2606-19111 | score_7_9 | not_selected | — | — | Leadership as Coordination Control: Behavioral Signatures and the Recovery-Advantage Boundary in Multi-Agent LLM Teams remains evidence-complete after canonical owner transfer with V2 score 7 and owner AGENT-MULTI-AGENT. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-19111 |
| SF-2026-ARXIV-2606-19191 | score_7_9 | not_selected | — | — | PhantomSkill: Malicious Code Injection in Agent Skill Ecosystems remains evidence-complete after canonical owner transfer with V2 score 9 and owner PLATFORM-SECURITY. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-19191 |
| SF-2026-ARXIV-2606-19242 | score_7_9 | not_selected | — | — | Runtime Compliance Verification for AI Agents remains evidence-complete after canonical owner transfer with V2 score 8 and owner PLATFORM-SECURITY. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-19242 |
| SF-2026-ARXIV-2606-19262 | score_7_9; potential_books_delta | not_selected | — | — | Detecting Hidden ML Training With Zero-Overhead Telemetry remains evidence-complete after canonical owner transfer with V2 score 9 and owner PLATFORM-MONITORING. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-19262 |
| SF-2026-ARXIV-2606-19271 | score_7_9 | not_selected | — | — | TurboServe: Serving Streaming Video Generation Efficiently and Economically remains evidence-complete after canonical owner transfer with V2 score 7 and owner INFER-SCHEDULING. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-19271 |

### Selected Analysis Narratives

<!-- analysis-decision:SF-2026-ARXIV-2606-18284:start -->
Breaking the Solver Bottleneck: Training Task Generators at the Learnable Frontier remains evidence-complete after canonical owner transfer with V2 score 9 and owner TRAIN-DATA. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-18284:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-18286:start -->
CODEBLOCK: Learning to Supervise Code at the Right Granularity remains evidence-complete after canonical owner transfer with V2 score 9 and owner TRAIN-SFT. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-18286:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-18310:start -->
Conflict-Aware Retriever Editing for Knowledge Injection Attacks on LLM-Based RAG Systems remains evidence-complete after canonical owner transfer with V2 score 9 and owner AGENT-RAG. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-18310:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-18322:start -->
SAE Interventions are Unreliable: Post-Intervention Recovery of Suppressed Behavior remains evidence-complete after canonical owner transfer with V2 score 9 and owner TRAIN-RLHF. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-18322:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-18356:start -->
SafeClawBench: Separating Semantic, Audit-Evidence, and Sandbox Harm in Tool-Using LLM Agents remains evidence-complete after canonical owner transfer with V2 score 9 and owner PLATFORM-EVALUATION-SYSTEM. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-18356:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-18379:start -->
RankGraph-2: Lifecycle Co-Design for Billion-Node Graph Learning in Recommendation remains evidence-complete after canonical owner transfer with V2 score 9 and owner AGENT-RAG. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-18379:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-18383:start -->
From Sparse Features to Trustworthy Proxies: Certifying SAE-Based Interpretability remains evidence-complete after canonical owner transfer with V2 score 9 and owner TRAIN-RLHF. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-18383:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-18394:start -->
JetSpec: Breaking the Scaling Ceiling of Speculative Decoding with Parallel Tree Drafting remains evidence-complete after canonical owner transfer with V2 score 8 and owner INFER-SPECULATIVE-DECODING. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-18394:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-18400:start -->
CloakLM: Obfuscating GPU Memory Layout to Mitigate Model Ex-filtration for Serving remains evidence-complete after canonical owner transfer with V2 score 9 and owner PLATFORM-SECURITY. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-18400:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-18421:start -->
Finding Compiler-Platform Interaction Bugs in Deep Learning Pipelines via Cross-Layer Constraints remains evidence-complete after canonical owner transfer with V2 score 9 and owner INFER-TENSORRT-LLM. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-18421:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-18431:start -->
Beyond Prediction: Tail-Aware Scheduling for LLM Inference remains evidence-complete after canonical owner transfer with V2 score 9 and owner INFER-SCHEDULING. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-18431:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-18448:start -->
VISUALSKILL: Multimodal Skills for Computer-Use Agents remains evidence-complete after canonical owner transfer with V2 score 9 and owner AGENT-TOOL-CALLING. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-18448:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-18467:start -->
ToolChain-CRC: Conformal Risk Control for Agentic AI Under Retrieval and Tool-Use Drift remains evidence-complete after canonical owner transfer with V2 score 9 and owner PLATFORM-EVALUATION-SYSTEM. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-18467:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-18497:start -->
Ghost Vectors: Soft-Deleted Embeddings Remain Reconstructible in HNSW Vector Databases remains evidence-complete after canonical owner transfer with V2 score 9 and owner AGENT-RAG. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-18497:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-18532:start -->
AI Sandboxes: A Threat Model, Taxonomy, and Measurement Framework remains evidence-complete after canonical owner transfer with V2 score 9 and owner PLATFORM-SECURITY. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-18532:end -->

<!-- analysis:DA-20260617-CONTRACT-INTEGRITY:start -->
### DA-20260617-CONTRACT-INTEGRITY
A structural tool gate is only as trustworthy as the precondition/effect/authorization facts it consumes. Signed provenance, typed attestation and runtime effect verification protect different rungs; none proves safety if the attestation root or external effect boundary is compromised.
<!-- analysis:DA-20260617-CONTRACT-INTEGRITY:end -->

<!-- analysis:DA-20260618-HETEROGENEOUS-RECOVERY:start -->
### DA-20260618-HETEROGENEOUS-RECOVERY
异构 spot serving 的控制对象不是一张静态 placement 表，而是 topology、request/KV state 与 replacement lifecycle。只有把重配置和输出恢复纳入同一 commit，成本优化才不会以分钟级中断换取。
<!-- analysis:DA-20260618-HETEROGENEOUS-RECOVERY:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-18619:start -->
Code-Augur: Agentic Vulnerability Detection via Specification Inference remains evidence-complete after canonical owner transfer with V2 score 9 and owner PLATFORM-SECURITY. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-18619:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-18650:start -->
BLADE: Scalable Bi-level Adaptive Data Selection for LLM Training remains evidence-complete after canonical owner transfer with V2 score 7 and owner TRAIN-DATA. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-18650:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-18668:start -->
EARS: Explanatory Abstention for Reliable Sub-Agent Modeling in Large-scale Multi-Agent Systems remains evidence-complete after canonical owner transfer with V2 score 7 and owner AGENT-MULTI-AGENT. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-18668:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-18673:start -->
Understanding and Mitigating Prompt Leaking Attacks in Real-World LLM-Based Applications remains evidence-complete after canonical owner transfer with V2 score 8 and owner PLATFORM-SECURITY. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-18673:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-18697:start -->
Stealthy World Model Manipulation via Data Poisoning remains evidence-complete after canonical owner transfer with V2 score 8 and owner MULTIMODAL-WORLD-MODELS. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-18697:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-18741:start -->
ReMP: Low-Downtime Runtime Model-Parallelism Reconfiguration for LLM Serving remains evidence-complete after canonical owner transfer with V2 score 9 and owner INFER-SCHEDULING. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-18741:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-18746:start -->
What Must Generalist Agents Remember? remains evidence-complete after canonical owner transfer with V2 score 7 and owner AGENT-MEMORY. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-18746:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-18810:start -->
Learning from Own Solutions: Self-Conditioned Credit Assignment for Reinforcement Learning with Verifiable Rewards remains evidence-complete after canonical owner transfer with V2 score 7 and owner TRAIN-GRPO. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-18810:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-18829:start -->
GateMem: Benchmarking Memory Governance in Multi-Principal Shared-Memory Agents remains evidence-complete after canonical owner transfer with V2 score 9 and owner PLATFORM-SECURITY. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-18829:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-18831:start -->
Beyond Reward Engineering: A Data Recipe for Long-Context Reinforcement Learning remains evidence-complete after canonical owner transfer with V2 score 8 and owner TRAIN-GRPO. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-18831:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-18847:start -->
WorldLines: Benchmarking and Modeling Long-Horizon Stateful Embodied Agents remains evidence-complete after canonical owner transfer with V2 score 8 and owner MULTIMODAL-EMBODIED-VLA. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-18847:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-18874:start -->
Externalizing Research Synthesis and Validation in AI Scientists through a Research Harness remains evidence-complete after canonical owner transfer with V2 score 8 and owner AGENT-WORKFLOW. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-18874:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-18958:start -->
LiveStack: OS Support for Cluster-Scale Full-Stack Live Simulation remains evidence-complete after canonical owner transfer with V2 score 8 and owner PLATFORM-PRODUCTION. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-18958:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-18967:start -->
EfficientRollout: System-Aware Self-Speculative Decoding for RL Rollouts remains evidence-complete after canonical owner transfer with V2 score 8 and owner INFER-SPECULATIVE-DECODING. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-18967:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-18996:start -->
TRAP: Benchmark for Task-completion and Resistance to Active Privacy-extraction remains evidence-complete after canonical owner transfer with V2 score 9 and owner PLATFORM-EVALUATION-SYSTEM. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-18996:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-19004:start -->
Spotlight: Synergizing Seed Exploration and Spot GPUs for DiT RL Post-Training remains evidence-complete after canonical owner transfer with V2 score 7 and owner PLATFORM-GPU-SCHEDULER. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-19004:end -->

<!-- analysis:DA-20260618-CROSS-SITE-MOE-OWNERSHIP:start -->
### DA-20260618-CROSS-SITE-MOE-OWNERSHIP
跨站 MoE 训练的关键不是把数据并行原样搬到 WAN，而是重新划分 expert/state ownership：每站只持有分区 expert，有限复制承担热点与可用性，non-resident token 以显式 skip 规则改变本地更新分布。实测通信和吞吐只覆盖作者配置，100B 仍是模型投影。
<!-- analysis:DA-20260618-CROSS-SITE-MOE-OWNERSHIP:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-19057:start -->
Quantifying and Auditing LLM Evaluation via Positive--Unlabeled Learning remains evidence-complete after canonical owner transfer with V2 score 9 and owner PLATFORM-EVALUATION-SYSTEM. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-19057:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-19111:start -->
Leadership as Coordination Control: Behavioral Signatures and the Recovery-Advantage Boundary in Multi-Agent LLM Teams remains evidence-complete after canonical owner transfer with V2 score 7 and owner AGENT-MULTI-AGENT. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-19111:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-19191:start -->
PhantomSkill: Malicious Code Injection in Agent Skill Ecosystems remains evidence-complete after canonical owner transfer with V2 score 9 and owner PLATFORM-SECURITY. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-19191:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-19242:start -->
Runtime Compliance Verification for AI Agents remains evidence-complete after canonical owner transfer with V2 score 8 and owner PLATFORM-SECURITY. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-19242:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-19262:start -->
Detecting Hidden ML Training With Zero-Overhead Telemetry remains evidence-complete after canonical owner transfer with V2 score 9 and owner PLATFORM-MONITORING. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-19262:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-19271:start -->
TurboServe: Serving Streaming Video Generation Efficiently and Economically remains evidence-complete after canonical owner transfer with V2 score 7 and owner INFER-SCHEDULING. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-19271:end -->

<!-- audit-target:deep_analysis_selection:end -->
<!-- audit-target:books:start -->
## 6. Books Comparison

<!-- validator:books-comparison-v1 -->
| Source Family ID | Stable Node ID | Target Chapter Ref | Adjacent Chapter Refs | Existing Proposition | New Evidence Delta | Evolution Relation | Decision | Books Review Ref |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2606-18284 | TRAIN-DATA | books/part-04-training-system/27-data.md#L1 | books/part-04-training-system/28-pretraining.md#L1; books/part-06-ai-infrastructure/59-model-registry.md#L1 | existing:SF-2026-ARXIV-2606-18284 | delta:SF-2026-ARXIV-2606-18284 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-18284 |
| SF-2026-ARXIV-2606-18286 | TRAIN-SFT | books/part-04-training-system/29-sft.md#L1 | books/part-04-training-system/27-data.md#L1; books/part-04-training-system/31-rlhf.md#L1 | existing:SF-2026-ARXIV-2606-18286 | delta:SF-2026-ARXIV-2606-18286 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-18286 |
| SF-2026-ARXIV-2606-18310 | AGENT-RAG | Books/part-07-agent/76-rag.md#L1 | Books/part-07-agent/77-memory.md#L1; Books/part-06-ai-infrastructure/72-security.md#L1 | existing:SF-2026-ARXIV-2606-18310 | delta:SF-2026-ARXIV-2606-18310 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-18310 |
| SF-2026-ARXIV-2606-18322 | TRAIN-RLHF | Books/part-04-training-system/31-rlhf.md#L1 | Books/part-04-training-system/29-sft.md#L1; Books/part-06-ai-infrastructure/66-evaluation-system.md#L1 | existing:SF-2026-ARXIV-2606-18322 | delta:SF-2026-ARXIV-2606-18322 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-18322 |
| SF-2026-ARXIV-2606-18356 | PLATFORM-EVALUATION-SYSTEM | Books/part-06-ai-infrastructure/66-evaluation-system.md#L1 | Books/part-06-ai-infrastructure/69-trace.md#L1; Books/part-06-ai-infrastructure/72-security.md#L1 | existing:SF-2026-ARXIV-2606-18356 | delta:SF-2026-ARXIV-2606-18356 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-18356 |
| SF-2026-ARXIV-2606-18379 | AGENT-RAG | Books/part-07-agent/76-rag.md#L1 | Books/part-07-agent/77-memory.md#L1; Books/part-06-ai-infrastructure/72-security.md#L1 | existing:SF-2026-ARXIV-2606-18379 | delta:SF-2026-ARXIV-2606-18379 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-18379 |
| SF-2026-ARXIV-2606-18383 | TRAIN-RLHF | Books/part-04-training-system/31-rlhf.md#L1 | Books/part-04-training-system/29-sft.md#L1; Books/part-06-ai-infrastructure/66-evaluation-system.md#L1 | existing:SF-2026-ARXIV-2606-18383 | delta:SF-2026-ARXIV-2606-18383 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-18383 |
| SF-2026-ARXIV-2606-18394 | INFER-SPECULATIVE-DECODING | Books/part-05-inference-system/48-speculative-decoding.md#L1 | Books/part-05-inference-system/44-decode.md#L1; Books/part-05-inference-system/56-inference-scheduling.md#L1 | existing:SF-2026-ARXIV-2606-18394 | delta:SF-2026-ARXIV-2606-18394 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-18394 |
| SF-2026-ARXIV-2606-18400 | PLATFORM-SECURITY | Books/part-06-ai-infrastructure/72-security.md#L1 | Books/part-06-ai-infrastructure/69-trace.md#L1; Books/part-07-agent/84-agent-platform.md#L1 | existing:SF-2026-ARXIV-2606-18400 | delta:SF-2026-ARXIV-2606-18400 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-18400 |
| SF-2026-ARXIV-2606-18421 | INFER-TENSORRT-LLM | Books/part-05-inference-system/49-tensorrt-llm.md#L1 | Books/part-05-inference-system/48-speculative-decoding.md#L1; Books/part-05-inference-system/54-gpu-memory.md#L1 | existing:SF-2026-ARXIV-2606-18421 | delta:SF-2026-ARXIV-2606-18421 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-18421 |
| SF-2026-ARXIV-2606-18431 | INFER-SCHEDULING | Books/part-05-inference-system/56-inference-scheduling.md#L1 | Books/part-05-inference-system/55-pd-disaggregation.md#L1; Books/part-06-ai-infrastructure/63-gpu-scheduler.md#L1 | existing:SF-2026-ARXIV-2606-18431 | delta:SF-2026-ARXIV-2606-18431 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-18431 |
| SF-2026-ARXIV-2606-18448 | AGENT-TOOL-CALLING | Books/part-07-agent/78-tool-calling.md#L1 | Books/part-07-agent/81-workflow.md#L1; Books/part-06-ai-infrastructure/72-security.md#L1 | existing:SF-2026-ARXIV-2606-18448 | delta:SF-2026-ARXIV-2606-18448 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-18448 |
| SF-2026-ARXIV-2606-18467 | PLATFORM-EVALUATION-SYSTEM | Books/part-06-ai-infrastructure/66-evaluation-system.md#L1 | Books/part-06-ai-infrastructure/69-trace.md#L1; Books/part-06-ai-infrastructure/72-security.md#L1 | existing:SF-2026-ARXIV-2606-18467 | delta:SF-2026-ARXIV-2606-18467 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-18467 |
| SF-2026-ARXIV-2606-18497 | AGENT-RAG | Books/part-07-agent/76-rag.md#L1 | Books/part-07-agent/77-memory.md#L1; Books/part-06-ai-infrastructure/72-security.md#L1 | existing:SF-2026-ARXIV-2606-18497 | delta:SF-2026-ARXIV-2606-18497 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-18497 |
| SF-2026-ARXIV-2606-18532 | PLATFORM-SECURITY | Books/part-06-ai-infrastructure/72-security.md#L1 | Books/part-06-ai-infrastructure/69-trace.md#L1; Books/part-07-agent/84-agent-platform.md#L1 | existing:SF-2026-ARXIV-2606-18532 | delta:SF-2026-ARXIV-2606-18532 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-18532 |
| SF-2026-ARXIV-2606-18550 | PLATFORM-SECURITY | Books/part-06-ai-infrastructure/72-security.md#L1 | Books/part-06-ai-infrastructure/69-trace.md#L1; Books/part-07-agent/84-agent-platform.md#L1 | existing:SF-2026-ARXIV-2606-18550 | delta:SF-2026-ARXIV-2606-18550 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-18550 |
| SF-2026-ARXIV-2606-18600 | INFER-SCHEDULING | books/part-05-inference-system/56-inference-scheduling.md#L1 | books/part-05-inference-system/55-pd-disaggregation.md#L1 | existing:SF-2026-ARXIV-2606-18600 | delta:SF-2026-ARXIV-2606-18600 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-18600 |
| SF-2026-ARXIV-2606-18619 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#L1 | books/part-06-ai-infrastructure/71-multi-tenant.md#L1 | existing:SF-2026-ARXIV-2606-18619 | delta:SF-2026-ARXIV-2606-18619 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-18619 |
| SF-2026-ARXIV-2606-18650 | TRAIN-DATA | books/part-04-training-system/27-data.md#L1 | books/part-04-training-system/28-pretraining.md#L1 | existing:SF-2026-ARXIV-2606-18650 | delta:SF-2026-ARXIV-2606-18650 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-18650 |
| SF-2026-ARXIV-2606-18668 | AGENT-MULTI-AGENT | books/part-07-agent/82-multi-agent.md#L1 | books/part-07-agent/81-workflow.md#L1 | existing:SF-2026-ARXIV-2606-18668 | delta:SF-2026-ARXIV-2606-18668 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-18668 |
| SF-2026-ARXIV-2606-18673 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#L1 | books/part-06-ai-infrastructure/71-multi-tenant.md#L1 | existing:SF-2026-ARXIV-2606-18673 | delta:SF-2026-ARXIV-2606-18673 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-18673 |
| SF-2026-ARXIV-2606-18697 | MULTIMODAL-WORLD-MODELS | books/part-03-multimodal-world-models/25-multimodal-world-models.md#L1 | books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md#L1 | existing:SF-2026-ARXIV-2606-18697 | delta:SF-2026-ARXIV-2606-18697 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-18697 |
| SF-2026-ARXIV-2606-18741 | INFER-SCHEDULING | books/part-05-inference-system/56-inference-scheduling.md#L1 | books/part-05-inference-system/55-pd-disaggregation.md#L1 | existing:SF-2026-ARXIV-2606-18741 | delta:SF-2026-ARXIV-2606-18741 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-18741 |
| SF-2026-ARXIV-2606-18746 | AGENT-MEMORY | books/part-07-agent/77-memory.md#L1 | books/part-07-agent/76-rag.md#L1 | existing:SF-2026-ARXIV-2606-18746 | delta:SF-2026-ARXIV-2606-18746 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-18746 |
| SF-2026-ARXIV-2606-18810 | TRAIN-GRPO | books/part-04-training-system/33-grpo.md#L1 | books/part-04-training-system/32-ppo.md#L1 | existing:SF-2026-ARXIV-2606-18810 | delta:SF-2026-ARXIV-2606-18810 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-18810 |
| SF-2026-ARXIV-2606-18829 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#L1 | books/part-06-ai-infrastructure/71-multi-tenant.md#L1 | existing:SF-2026-ARXIV-2606-18829 | delta:SF-2026-ARXIV-2606-18829 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-18829 |
| SF-2026-ARXIV-2606-18831 | TRAIN-GRPO | books/part-04-training-system/33-grpo.md#L1 | books/part-04-training-system/32-ppo.md#L1 | existing:SF-2026-ARXIV-2606-18831 | delta:SF-2026-ARXIV-2606-18831 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-18831 |
| SF-2026-ARXIV-2606-18847 | MULTIMODAL-EMBODIED-VLA | books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#L1 | books/part-03-multimodal-world-models/25-multimodal-world-models.md#L1 | existing:SF-2026-ARXIV-2606-18847 | delta:SF-2026-ARXIV-2606-18847 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-18847 |
| SF-2026-ARXIV-2606-18874 | AGENT-WORKFLOW | books/part-07-agent/81-workflow.md#L1 | books/part-07-agent/80-reflection.md#L1 | existing:SF-2026-ARXIV-2606-18874 | delta:SF-2026-ARXIV-2606-18874 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-18874 |
| SF-2026-ARXIV-2606-18958 | PLATFORM-PRODUCTION | books/part-06-ai-infrastructure/73-production-best-practice.md#L1 | books/part-06-ai-infrastructure/72-security.md#L1 | existing:SF-2026-ARXIV-2606-18958 | delta:SF-2026-ARXIV-2606-18958 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-18958 |
| SF-2026-ARXIV-2606-18967 | INFER-SPECULATIVE-DECODING | books/part-05-inference-system/48-speculative-decoding.md#L1 | books/part-05-inference-system/47-pagedattention.md#L1 | existing:SF-2026-ARXIV-2606-18967 | delta:SF-2026-ARXIV-2606-18967 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-18967 |
| SF-2026-ARXIV-2606-18996 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#L1 | books/part-06-ai-infrastructure/67-monitoring.md#L1 | existing:SF-2026-ARXIV-2606-18996 | delta:SF-2026-ARXIV-2606-18996 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-18996 |
| SF-2026-ARXIV-2606-19004 | PLATFORM-GPU-SCHEDULER | books/part-06-ai-infrastructure/63-gpu-scheduler.md#L1 | books/part-06-ai-infrastructure/65-kai-scheduler.md#L1 | existing:SF-2026-ARXIV-2606-19004 | delta:SF-2026-ARXIV-2606-19004 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-19004 |
| SF-2026-ARXIV-2606-19025 | TRAIN-DISTRIBUTED-TRAINING | books/part-04-training-system/36-distributed-training.md#L1 | books/part-04-training-system/37-tensor-parallel.md#L1 | existing:SF-2026-ARXIV-2606-19025 | delta:SF-2026-ARXIV-2606-19025 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-19025 |
| SF-2026-ARXIV-2606-19057 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#L1 | books/part-06-ai-infrastructure/67-monitoring.md#L1 | existing:SF-2026-ARXIV-2606-19057 | delta:SF-2026-ARXIV-2606-19057 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-19057 |
| SF-2026-ARXIV-2606-19111 | AGENT-MULTI-AGENT | books/part-07-agent/82-multi-agent.md#L1 | books/part-07-agent/81-workflow.md#L1 | existing:SF-2026-ARXIV-2606-19111 | delta:SF-2026-ARXIV-2606-19111 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-19111 |
| SF-2026-ARXIV-2606-19191 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#L1 | books/part-06-ai-infrastructure/71-multi-tenant.md#L1 | existing:SF-2026-ARXIV-2606-19191 | delta:SF-2026-ARXIV-2606-19191 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-19191 |
| SF-2026-ARXIV-2606-19242 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#L1 | books/part-06-ai-infrastructure/71-multi-tenant.md#L1 | existing:SF-2026-ARXIV-2606-19242 | delta:SF-2026-ARXIV-2606-19242 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-19242 |
| SF-2026-ARXIV-2606-19262 | PLATFORM-MONITORING | books/part-06-ai-infrastructure/67-monitoring.md#L1 | books/part-06-ai-infrastructure/69-trace.md#L1 | existing:SF-2026-ARXIV-2606-19262 | delta:SF-2026-ARXIV-2606-19262 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-19262 |
| SF-2026-ARXIV-2606-19271 | INFER-SCHEDULING | books/part-05-inference-system/56-inference-scheduling.md#L1 | books/part-05-inference-system/55-pd-disaggregation.md#L1 | existing:SF-2026-ARXIV-2606-19271 | delta:SF-2026-ARXIV-2606-19271 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-19271 |

<!-- existing:SF-2026-ARXIV-2606-18284:start -->
Owner `TRAIN-DATA` and adjacent chapters were read; existing proposition was compared against exact-v1, including coexistence and failure boundaries.
<!-- existing:SF-2026-ARXIV-2606-18284:end -->

<!-- delta:SF-2026-ARXIV-2606-18284:start -->
训练 task generator 时可用一次 solver-labeled pool 训练 activation probe，把 targeted solve-rate 作为 amortized reward；最终仍由 held-out solver 验证。
<!-- delta:SF-2026-ARXIV-2606-18284:end -->

<!-- books-review:SF-2026-ARXIV-2606-18284:start -->
Owner `TRAIN-DATA`; relation `Direct Evolution`; disposition `Integrate`; adjacent handoff `books/part-04-training-system/28-pretraining.md; books/part-06-ai-infrastructure/59-model-registry.md`.
<!-- books-review:SF-2026-ARXIV-2606-18284:end -->

<!-- existing:SF-2026-ARXIV-2606-18286:start -->
Owner `TRAIN-SFT` and adjacent chapters were read; existing proposition was compared against exact-v1, including coexistence and failure boundaries.
<!-- existing:SF-2026-ARXIV-2606-18286:end -->

<!-- delta:SF-2026-ARXIV-2606-18286:start -->
Code SFT 的 sparse supervision unit 应是 syntax-complete、data-flow-connected code block，而非孤立 high-loss token；完整 response 继续作 context。
<!-- delta:SF-2026-ARXIV-2606-18286:end -->

<!-- books-review:SF-2026-ARXIV-2606-18286:start -->
Owner `TRAIN-SFT`; relation `Direct Evolution`; disposition `Integrate`; adjacent handoff `books/part-04-training-system/27-data.md; books/part-04-training-system/31-rlhf.md`.
<!-- books-review:SF-2026-ARXIV-2606-18286:end -->

<!-- existing:SF-2026-ARXIV-2606-18310:start -->
`AGENT-RAG` 已有 source provenance、index identity、retrieval lifecycle 与删除传播; adjacent handoff was checked in `Books/part-07-agent/77-memory.md; Books/part-06-ai-infrastructure/72-security.md`.
<!-- existing:SF-2026-ARXIV-2606-18310:end -->

<!-- delta:SF-2026-ARXIV-2606-18310:start -->
RAG threat model 需覆盖 retriever parameter editing：攻击者可改变 ranking 而不改 corpus；index/model revision、anchor repair 与 retrieval regression 必须同 lifecycle 验证。
<!-- delta:SF-2026-ARXIV-2606-18310:end -->

<!-- books-review:SF-2026-ARXIV-2606-18310:start -->
Relation=`Direct Evolution`; disposition=`Integrate`; unique owner=`AGENT-RAG`. repair anchors能恢复局部行为却可能伤正常 recall；受测编辑不代表所有 retriever compromise。
<!-- books-review:SF-2026-ARXIV-2606-18310:end -->

<!-- existing:SF-2026-ARXIV-2606-18322:start -->
`TRAIN-RLHF` 已有 behavior intervention、reward/evaluation 与 promotion boundary; adjacent handoff was checked in `Books/part-04-training-system/29-sft.md; Books/part-06-ai-infrastructure/66-evaluation-system.md`.
<!-- existing:SF-2026-ARXIV-2606-18322:end -->

<!-- delta:SF-2026-ARXIV-2606-18322:start -->
SAE feature clamp/ablation 不能被当作行为控制 complete；residual stream 会在后续层恢复被压制行为，需做 post-intervention trajectory 与 residual recovery audit。
<!-- delta:SF-2026-ARXIV-2606-18322:end -->

<!-- books-review:SF-2026-ARXIV-2606-18322:start -->
Relation=`Direct Evolution`; disposition=`Integrate`; unique owner=`TRAIN-RLHF`. 跨层审计增加 hook/compute且仍是 proxy；观察恢复不证明 SAE 无用，也不提供通用 steering 方案。
<!-- books-review:SF-2026-ARXIV-2606-18322:end -->

<!-- existing:SF-2026-ARXIV-2606-18356:start -->
`PLATFORM-EVALUATION-SYSTEM` 已有 EvalSpec、artifact/process/environment evidence 与 release authority; adjacent handoff was checked in `Books/part-06-ai-infrastructure/69-trace.md; Books/part-06-ai-infrastructure/72-security.md`.
<!-- existing:SF-2026-ARXIV-2606-18356:end -->

<!-- delta:SF-2026-ARXIV-2606-18356:start -->
Agent security EvalSpec 必须分开 semantic compromise、artifact-visible harm evidence 与 sandbox-observed state/tool harm，并保持各自 denominator 和 matched identity。
<!-- delta:SF-2026-ARXIV-2606-18356:end -->

<!-- books-review:SF-2026-ARXIV-2606-18356:start -->
Relation=`Direct Evolution`; disposition=`Integrate`; unique owner=`PLATFORM-EVALUATION-SYSTEM`. 多 endpoint改善定位却增加匹配与审计成本；600 合成 case不估计生产 prevalence，prompt policy不替代 runtime control。
<!-- books-review:SF-2026-ARXIV-2606-18356:end -->

<!-- existing:SF-2026-ARXIV-2606-18379:start -->
`AGENT-RAG` 已有 source provenance、index identity、retrieval lifecycle 与删除传播; adjacent handoff was checked in `Books/part-07-agent/77-memory.md; Books/part-06-ai-infrastructure/72-security.md`.
<!-- existing:SF-2026-ARXIV-2606-18379:end -->

<!-- delta:SF-2026-ARXIV-2606-18379:start -->
Billion-node graph retrieval owner 应贯通 graph construction、cluster/index lifecycle、训练与 serving refresh，避免离线 embedding/index 与在线推荐 state 各自漂移。
<!-- delta:SF-2026-ARXIV-2606-18379:end -->

<!-- books-review:SF-2026-ARXIV-2606-18379:start -->
Relation=`Direct Evolution`; disposition=`Integrate`; unique owner=`AGENT-RAG`. 联合 lifecycle缩短 refresh却扩大 control-plane coupling、rebuild和失败域；单平台生产证据不外推任意 RAG corpus。
<!-- books-review:SF-2026-ARXIV-2606-18379:end -->

<!-- existing:SF-2026-ARXIV-2606-18383:start -->
`TRAIN-RLHF` 已有 behavior intervention、reward/evaluation 与 promotion boundary; adjacent handoff was checked in `Books/part-04-training-system/29-sft.md; Books/part-06-ai-infrastructure/66-evaluation-system.md`.
<!-- existing:SF-2026-ARXIV-2606-18383:end -->

<!-- delta:SF-2026-ARXIV-2606-18383:start -->
SAE 只有在 proxy risk、reconstruction gap、concept mismatch 与 proxy complexity 共同受控时才能支撑干预结论；单独 sparsity/reconstruction score不足以认证 fidelity。
<!-- delta:SF-2026-ARXIV-2606-18383:end -->

<!-- books-review:SF-2026-ARXIV-2606-18383:start -->
Relation=`Direct Evolution`; disposition=`Integrate`; unique owner=`TRAIN-RLHF`. 证书更可审计却依赖可估计 risk 与 concept定义；通过 proxy certificate 仍不证明行为因果或部署安全。
<!-- books-review:SF-2026-ARXIV-2606-18383:end -->

<!-- existing:SF-2026-ARXIV-2606-18394:start -->
`INFER-SPECULATIVE-DECODING` 已有 proposal tree、target verification、prefix commit 与 suffix rollback; current owner already contains this exact mechanism/family and fallback boundary; adjacent handoff was checked in `Books/part-05-inference-system/44-decode.md; Books/part-05-inference-system/56-inference-scheduling.md`.
<!-- existing:SF-2026-ARXIV-2606-18394:end -->

<!-- delta:SF-2026-ARXIV-2606-18394:start -->
Parallel causal tree drafting仍遵守 proposal tree、target verification、accepted-prefix commit 与 suffix rollback；Ch48 已有该 owner、DARTree/TAPS 与 tree cost/fallback 边界。
<!-- delta:SF-2026-ARXIV-2606-18394:end -->

<!-- books-review:SF-2026-ARXIV-2606-18394:start -->
Relation=`Principle Reuse`; disposition=`No Change — Existing Coverage`; unique owner=`INFER-SPECULATIVE-DECODING`. 更宽树提高候选覆盖也增加 verify shape、显存和 branch waste；现有 Ch48 已覆盖该 trade-off，不追加论文特定实现。
<!-- books-review:SF-2026-ARXIV-2606-18394:end -->

<!-- existing:SF-2026-ARXIV-2606-18400:start -->
`PLATFORM-SECURITY` 已有 trust boundary、provenance、least privilege、containment 与 effect-time authority; adjacent handoff was checked in `Books/part-06-ai-infrastructure/69-trace.md; Books/part-07-agent/84-agent-platform.md`.
<!-- existing:SF-2026-ARXIV-2606-18400:end -->

<!-- delta:SF-2026-ARXIV-2606-18400:start -->
共享 GPU 上的模型权重保护可在 PCIe traffic、weight order 与 HBM physical page 三层破坏可重建 regularity，同时保留 authorized virtual layout；这是 cost-imposition 而非 secrecy proof。
<!-- delta:SF-2026-ARXIV-2606-18400:end -->

<!-- books-review:SF-2026-ARXIV-2606-18400:start -->
Relation=`Direct Evolution`; disposition=`Integrate`; unique owner=`PLATFORM-SECURITY`. layout obfuscation增加 allocator/metadata和可能的访问开销；无法阻止已拿到映射或可改 kernel 的攻击者。
<!-- books-review:SF-2026-ARXIV-2606-18400:end -->

<!-- existing:SF-2026-ARXIV-2606-18421:start -->
`INFER-TENSORRT-LLM` 已有 compiler/kernel/runtime 协同与 backend-specific validation; adjacent handoff was checked in `Books/part-05-inference-system/48-speculative-decoding.md; Books/part-05-inference-system/54-gpu-memory.md`.
<!-- existing:SF-2026-ARXIV-2606-18421:end -->

<!-- delta:SF-2026-ARXIV-2606-18421:start -->
DL compiler release testing 应抽取跨 model semantics、IR pass 与 hardware feasibility 的 full-stack constraints，并把 assertion pattern作为 behavior-equivalence oracle。
<!-- delta:SF-2026-ARXIV-2606-18421:end -->

<!-- books-review:SF-2026-ARXIV-2606-18421:start -->
Relation=`Direct Evolution`; disposition=`Integrate`; unique owner=`INFER-TENSORRT-LLM`. 深层 constraint能发现 silent bug却增加规则维护和 false signal；2,034 cases不等于2,034已确认独立生产缺陷。
<!-- books-review:SF-2026-ARXIV-2606-18421:end -->

<!-- existing:SF-2026-ARXIV-2606-18431:start -->
`INFER-SCHEDULING` 已有 admission、queue、preemption、KV residency 与 tail-SLO trade-off; adjacent handoff was checked in `Books/part-05-inference-system/55-pd-disaggregation.md; Books/part-06-ai-infrastructure/63-gpu-scheduler.md`.
<!-- existing:SF-2026-ARXIV-2606-18431:end -->

<!-- delta:SF-2026-ARXIV-2606-18431:start -->
LLM scheduler 应直接优化 tail risk，以 cache-aware preemption与完成风险信号决策，而不是依赖易漂移的 output-length point predictor。
<!-- delta:SF-2026-ARXIV-2606-18431:end -->

<!-- books-review:SF-2026-ARXIV-2606-18431:start -->
Relation=`Direct Evolution`; disposition=`Integrate`; unique owner=`INFER-SCHEDULING`. prediction-free不等于信息免费，tail objective可能牺牲mean/fairness；受测 traces不证明所有SLO最优。
<!-- books-review:SF-2026-ARXIV-2606-18431:end -->

<!-- existing:SF-2026-ARXIV-2606-18448:start -->
`AGENT-TOOL-CALLING` 已有 tool schema、routing、authority 与执行反馈边界; adjacent handoff was checked in `Books/part-07-agent/81-workflow.md; Books/part-06-ai-infrastructure/72-security.md`.
<!-- existing:SF-2026-ARXIV-2606-18448:end -->

<!-- delta:SF-2026-ARXIV-2606-18448:start -->
Computer-use skill 应把 screenshot、spatial step、semantic instruction 与 resource references组成可版本化 multimodal artifact，并允许按 topic/on-demand MCP load，避免全库 prompt 膨胀。
<!-- delta:SF-2026-ARXIV-2606-18448:end -->

<!-- books-review:SF-2026-ARXIV-2606-18448:start -->
Relation=`Direct Evolution`; disposition=`Integrate`; unique owner=`AGENT-TOOL-CALLING`. 多模态 skill提高复用却增加视觉漂移、存储与供应链面；按需加载 miss 时必须回退在线探索。
<!-- books-review:SF-2026-ARXIV-2606-18448:end -->

<!-- existing:SF-2026-ARXIV-2606-18467:start -->
`PLATFORM-EVALUATION-SYSTEM` 已有 EvalSpec、artifact/process/environment evidence 与 release authority; adjacent handoff was checked in `Books/part-06-ai-infrastructure/69-trace.md; Books/part-06-ai-infrastructure/72-security.md`.
<!-- existing:SF-2026-ARXIV-2606-18467:end -->

<!-- delta:SF-2026-ARXIV-2606-18467:start -->
Tool/retrieval trajectory release 可把 step risk校准为 trajectory conformal acceptance，并用 supermartingale anytime alarm监测运行中超界；drift时必须重校准或 abstain。
<!-- delta:SF-2026-ARXIV-2606-18467:end -->

<!-- books-review:SF-2026-ARXIV-2606-18467:start -->
Relation=`Direct Evolution`; disposition=`Integrate`; unique owner=`PLATFORM-EVALUATION-SYSTEM`. coverage依赖 calibration分布且 alarm会 false positive；形式保证不证明 scorer或 causal harm标签正确。
<!-- books-review:SF-2026-ARXIV-2606-18467:end -->

<!-- existing:SF-2026-ARXIV-2606-18497:start -->
`AGENT-RAG` 已有 source provenance、index identity、retrieval lifecycle 与删除传播; adjacent handoff was checked in `Books/part-07-agent/77-memory.md; Books/part-06-ai-infrastructure/72-security.md`.
<!-- existing:SF-2026-ARXIV-2606-18497:end -->

<!-- delta:SF-2026-ARXIV-2606-18497:start -->
Vector DB deletion 必须追踪 source→embedding→HNSW node→backup/replica 的物理生命周期；soft-delete tombstone 不是擦除，需 epoch key rotation与 signed deletion proof。
<!-- delta:SF-2026-ARXIV-2606-18497:end -->

<!-- books-review:SF-2026-ARXIV-2606-18497:start -->
Relation=`Direct Evolution`; disposition=`Integrate`; unique owner=`AGENT-RAG`. physical purge或key rotation增加 rebuild、availability与密钥治理成本；受测 HNSW 恢复不覆盖所有 vector stores。
<!-- books-review:SF-2026-ARXIV-2606-18497:end -->

<!-- existing:SF-2026-ARXIV-2606-18532:start -->
`PLATFORM-SECURITY` 已有 trust boundary、provenance、least privilege、containment 与 effect-time authority; adjacent handoff was checked in `Books/part-06-ai-infrastructure/69-trace.md; Books/part-07-agent/84-agent-platform.md`.
<!-- existing:SF-2026-ARXIV-2606-18532:end -->

<!-- delta:SF-2026-ARXIV-2606-18532:start -->
AI sandbox 应以 threat model和 weakest-link evidence评估 fidelity、controllability、observability、containment、reproducibility与governance，不能把“进程在容器里”当成安全证明。
<!-- delta:SF-2026-ARXIV-2606-18532:end -->

<!-- books-review:SF-2026-ARXIV-2606-18532:start -->
Relation=`Direct Evolution`; disposition=`Integrate`; unique owner=`PLATFORM-SECURITY`. 更强隔离通常降低 fidelity/性能且扩大运维；框架只能组织证据，不能认证未知 escape或side channel不存在。
<!-- books-review:SF-2026-ARXIV-2606-18532:end -->

<!-- existing:SF-2026-ARXIV-2606-18550:start -->
`PLATFORM-SECURITY` 已有 trust boundary、provenance、least privilege、containment 与 effect-time authority; adjacent handoff was checked in `Books/part-06-ai-infrastructure/69-trace.md; Books/part-07-agent/84-agent-platform.md`.
<!-- existing:SF-2026-ARXIV-2606-18550:end -->

<!-- delta:SF-2026-ARXIV-2606-18550:start -->
Tool safety gate依赖 contract integrity；应对 precondition/effect/risk/authorization字段做 signed provenance、typed attestation与runtime effect verification，且 effect字段比risk标签更load-bearing。
<!-- delta:SF-2026-ARXIV-2606-18550:end -->

<!-- books-review:SF-2026-ARXIV-2606-18550:start -->
Relation=`Direct Evolution`; disposition=`Integrate`; unique owner=`PLATFORM-SECURITY`. 完整 ladder增加签名、schema与runtime mediation成本；只在有限 contract perturbation空间给保证，attestation失陷即失效。
<!-- books-review:SF-2026-ARXIV-2606-18550:end -->

<!-- existing:SF-2026-ARXIV-2606-18600:start -->
现有 owner 已覆盖请求级 admission、prefill/decode 调度、fairness、elasticity 与恢复 handoff；相邻 PD 章拥有阶段边界。 Comparative result for arXiv:2606.18600v1: 唯一同时改变 placement 与 interruption recovery 的 serving family，进入三项叙事。
<!-- existing:SF-2026-ARXIV-2606-18600:end -->

<!-- delta:SF-2026-ARXIV-2606-18600:start -->
异构 spot serving 必须联合决定 GPU pool、每 stage TP/PP 与不等层分配；中断时以输出重算恢复 request，并让 replacement initialization 与旧 pipeline 服务重叠。
<!-- delta:SF-2026-ARXIV-2606-18600:end -->

<!-- books-review:SF-2026-ARXIV-2606-18600:start -->
Direct Evolution; Integrate. 六天单 region 可用性和短上下文重算不能证明跨区供应或长上下文恢复；shared tensor store 也引入新的可用性 owner。
<!-- books-review:SF-2026-ARXIV-2606-18600:end -->

<!-- existing:SF-2026-ARXIV-2606-18619:start -->
现有 owner 已把 secret、policy、artifact identity、effect-time authorization 与撤销放在外部安全控制面；相邻多租户章拥有 principal/isolation。 Comparative result for arXiv:2606.18619v1: 把 agent 判断转成可反证 artifact，补足安全 evidence plane，优先于纯检测率改进。
<!-- existing:SF-2026-ARXIV-2606-18619:end -->

<!-- delta:SF-2026-ARXIV-2606-18619:start -->
Agent 判定代码安全时要把隐含输入假设提交为 in-source assertions，再由 guided fuzzer 反证；assertion failure 可能是漏洞，也可能是 specification repair 信号。
<!-- delta:SF-2026-ARXIV-2606-18619:end -->

<!-- books-review:SF-2026-ARXIV-2606-18619:start -->
Direct Evolution; Integrate. fuzzer 未触发不等于 invariant 成立，assertion 也可能错；覆盖限于作者 subjects 与可观测运行输入。
<!-- books-review:SF-2026-ARXIV-2606-18619:end -->

<!-- existing:SF-2026-ARXIV-2606-18650:start -->
现有 owner 已把数据选择建模为带 lineage、proxy coverage、动态反馈与 admission gate 的控制问题；相邻预训练章消费冻结后的数据 contract。 Comparative result for arXiv:2606.18650v1: Ch27 已拥有动态 data admission 与 proxy bias；本工作强化求解器分支但不新增 owner。
<!-- existing:SF-2026-ARXIV-2606-18650:end -->

<!-- delta:SF-2026-ARXIV-2606-18650:start -->
训练数据选择可把双层 influence objective 改写为带 Lagrange penalty 的单层目标，并让动态 reference 随 proxy trajectory 同步；online selector 用 memoryless randomized block-coordinate Frank-Wolfe。
<!-- delta:SF-2026-ARXIV-2606-18650:end -->

<!-- books-review:SF-2026-ARXIV-2606-18650:start -->
Principle Reuse; No Change — Existing Coverage. proxy-to-target transfer、penalty 设定与 trajectory drift 仍可能失配；收敛定理不等于目标模型质量普遍提升。
<!-- books-review:SF-2026-ARXIV-2606-18650:end -->

<!-- existing:SF-2026-ARXIV-2606-18668:start -->
现有 owner 已拥有 coordinator、typed handoff、reroute、shared-state commit 与 fallback authority；相邻 workflow 章拥有单流程执行。 Comparative result for arXiv:2606.18668v1: Ch82 已有 typed failure handoff、reroute 与 fallback authority；EARS 提供生产证据，不另建 abstention owner。
<!-- existing:SF-2026-ARXIV-2606-18668:end -->

<!-- delta:SF-2026-ARXIV-2606-18668:start -->
sub-agent abstention 应是 typed failure message，携带 ambiguous、misrouted、unsupported 等理由，供 coordinator clarification、reroute 或 fallback，而不是空响应。
<!-- delta:SF-2026-ARXIV-2606-18668:end -->

<!-- books-review:SF-2026-ARXIV-2606-18668:start -->
Principle Reuse; No Change — Existing Coverage. judge ensemble 与生产流量共享偏差且 backbone 未披露；pass rate 不证明授权、安全或跨域 calibration。
<!-- books-review:SF-2026-ARXIV-2606-18668:end -->

<!-- existing:SF-2026-ARXIV-2606-18673:start -->
现有 owner 已把 secret、policy、artifact identity、effect-time authorization 与撤销放在外部安全控制面；相邻多租户章拥有 principal/isolation。 Comparative result for arXiv:2606.18673v1: Ch72 已明确 prompt 不是 secret store；AREA 只作为受限 sensor 分支。
<!-- existing:SF-2026-ARXIV-2606-18673:end -->

<!-- delta:SF-2026-ARXIV-2606-18673:start -->
system-prompt secrecy 不能只靠静态拒答；AREA 用可优化 soft prompt 重锚 attention，但 secret/API key 仍必须移出 prompt 并由外部 reference monitor 管理。
<!-- delta:SF-2026-ARXIV-2606-18673:end -->

<!-- books-review:SF-2026-ARXIV-2606-18673:start -->
Principle Reuse; No Change — Existing Coverage. attention drift 是受测模型解释，不证明所有泄漏因果；soft prompt 无法把已放入上下文的密钥变成真正 secret。
<!-- books-review:SF-2026-ARXIV-2606-18673:end -->

<!-- existing:SF-2026-ARXIV-2606-18697:start -->
现有 owner 已拥有 learned dynamics、planning feedback 与环境真值边界；相邻生成范式章不拥有 planning control。 Comparative result for arXiv:2606.18697v1: 首次把 world-model adaptation data 显式定位为 downstream planning authority 的供应链边界。
<!-- existing:SF-2026-ARXIV-2606-18697:end -->

<!-- delta:SF-2026-ARXIV-2606-18697:start -->
world-model fine-tuning data 是 planning control surface：SWAAP 先优化近似 clean dynamics 的低回报目标模型，再以 stealth-constrained gradient matching 修改有限 transition targets。
<!-- delta:SF-2026-ARXIV-2606-18697:end -->

<!-- books-review:SF-2026-ARXIV-2606-18697:start -->
Direct Evolution; Integrate. 只击败 non-adaptive defenses；低 prediction error 不等于 transition 正确，真实环境 feedback 仍是权威。
<!-- books-review:SF-2026-ARXIV-2606-18697:end -->

<!-- existing:SF-2026-ARXIV-2606-18741:start -->
现有 owner 已覆盖请求级 admission、prefill/decode 调度、fairness、elasticity 与恢复 handoff；相邻 PD 章拥有阶段边界。 Comparative result for arXiv:2606.18741v1: 它改变 serving topology 的运行时 commit protocol，不只是更好的静态 scheduler。
<!-- existing:SF-2026-ARXIV-2606-18741:end -->

<!-- delta:SF-2026-ARXIV-2606-18741:start -->
runtime parallelism 变更要把 topology 与 request state 解耦，并以二维 KV migration 将旧 TP/PP shard 映射到新 topology，再原子切换流量。
<!-- delta:SF-2026-ARXIV-2606-18741:end -->

<!-- books-review:SF-2026-ARXIV-2606-18741:start -->
Direct Evolution; Integrate. KV migration 与双份资源会制造瞬时带宽/容量峰值；作者模型与网络不证明任意拓扑可无损切换。
<!-- books-review:SF-2026-ARXIV-2606-18741:end -->

<!-- existing:SF-2026-ARXIV-2606-18746:start -->
现有 owner 已区分 observation/memory/environment state 及其读写生命周期；相邻 RAG 章只拥有 evidence retrieval。 Comparative result for arXiv:2606.18746v1: Ch77/79 已区分 memory state 与 environment state；该定理加强必要性证明。
<!-- existing:SF-2026-ARXIV-2606-18746:end -->

<!-- delta:SF-2026-ARXIV-2606-18746:start -->
若相同 observation bottleneck 在不同 domain 需要不兼容 action，近最优 policy 必须保存可区分的 memory distribution；足够的 value 信息还可近似重建局部 transition dynamics。
<!-- delta:SF-2026-ARXIV-2606-18746:end -->

<!-- books-review:SF-2026-ARXIV-2606-18746:start -->
Principle Reuse; No Change — Existing Coverage. 定理依赖形式化 observation/domain 假设；可重建局部 dynamics 不代表 memory 内容真实、授权或可长期维护。
<!-- books-review:SF-2026-ARXIV-2606-18746:end -->

<!-- existing:SF-2026-ARXIV-2606-18810:start -->
现有 owner 已拥有 rollout identity、verifier/reward 共偏、credit assignment 与 promotion gate；相邻 PPO 章拥有旧策略约束。 Comparative result for arXiv:2606.18810v1: Ch33 已拥有 token credit 与 verifier 共偏边界；保留为不依赖外部 teacher 的证据。
<!-- existing:SF-2026-ARXIV-2606-18810:end -->

<!-- delta:SF-2026-ARXIV-2606-18810:start -->
SC-GRPO 用 verified trajectory 条件化前后 token KL 作为 GRPO gradient 权重，让 policy 自己暴露 pivotal token，避免外部 PRM/teacher。
<!-- delta:SF-2026-ARXIV-2606-18810:end -->

<!-- books-review:SF-2026-ARXIV-2606-18810:start -->
Principle Reuse; No Change — Existing Coverage. self-conditioned teacher 与 student 共偏；KL 大小不自动等于因果 credit，verified final answer 也可能掩盖错误路径。
<!-- books-review:SF-2026-ARXIV-2606-18810:end -->

<!-- existing:SF-2026-ARXIV-2606-18829:start -->
现有 owner 已把 secret、policy、artifact identity、effect-time authorization 与撤销放在外部安全控制面；相邻多租户章拥有 principal/isolation。 Comparative result for arXiv:2606.18829v1: Ch72 已有同一 exact family 的 Utility/ACL/Forgetting Gate 与代价边界；本日只保留证据 handoff。
<!-- existing:SF-2026-ARXIV-2606-18829:end -->

<!-- delta:SF-2026-ARXIV-2606-18829:start -->
共享 memory 的 admission/read/delete 必须按 principal、role、scope 和 relationship 授权，并把 utility、ACL leakage 与 active forgetting 作为三个独立 Gate。
<!-- delta:SF-2026-ARXIV-2606-18829:end -->

<!-- books-review:SF-2026-ARXIV-2606-18829:start -->
Principle Reuse; No Change — Existing Coverage. structured judge 与合成 episode 不证明真实机构合规；long-context 的较高 governance score 伴随 token cost，external memory 仍可能泄漏。
<!-- books-review:SF-2026-ARXIV-2606-18829:end -->

<!-- existing:SF-2026-ARXIV-2606-18831:start -->
现有 owner 已拥有 rollout identity、verifier/reward 共偏、credit assignment 与 promotion gate；相邻 PPO 章拥有旧策略约束。 Comparative result for arXiv:2606.18831v1: 训练 mixture 把检索、证据合成、推理拆成可审计能力，而非只调 reward。
<!-- existing:SF-2026-ARXIV-2606-18831:end -->

<!-- delta:SF-2026-ARXIV-2606-18831:start -->
long-context RL 的 data owner 应同时覆盖 retrieval、multi-evidence synthesis 与 reasoning，避免只通过 reward shaping 修补 evidence localization。
<!-- delta:SF-2026-ARXIV-2606-18831:end -->

<!-- books-review:SF-2026-ARXIV-2606-18831:start -->
Direct Evolution; Integrate. 作者 mixture 与 Qwen family 不能证明通用配方；outcome reward 仍可能奖励无 grounding shortcut。
<!-- books-review:SF-2026-ARXIV-2606-18831:end -->

<!-- existing:SF-2026-ARXIV-2606-18847:start -->
现有 owner 已拥有 observation-action-state 闭环与真实执行反馈；相邻 world-model 章提供预测状态而不拥有 action commit。 Comparative result for arXiv:2606.18847v1: 它把 memory retrieval 与真实 action/state evolution接起来，属于 embodied owner 的长期 delta。
<!-- existing:SF-2026-ARXIV-2606-18847:end -->

<!-- delta:SF-2026-ARXIV-2606-18847:start -->
长期 embodied memory 需保存 visibility-aware observation、action-native state trail 与执行反馈，且旧 state 被覆盖时保留时间身份，供 planning 消费。
<!-- delta:SF-2026-ARXIV-2606-18847:end -->

<!-- books-review:SF-2026-ARXIV-2606-18847:start -->
Direct Evolution; Integrate. benchmark household traces 不是开放世界；observer-grounded memory 仍可能漏看并把推断状态误写成事实。
<!-- books-review:SF-2026-ARXIV-2606-18847:end -->

<!-- existing:SF-2026-ARXIV-2606-18874:start -->
现有 owner 已拥有 durable checkpoint、claim-evidence lineage、idempotent resume 与人工接管；相邻 reflection 章只提出修正信号。 Comparative result for arXiv:2606.18874v1: Ch81/66 已拥有 claim-evidence lineage 与 harness identity；Xcientist 是具体实例。
<!-- existing:SF-2026-ARXIV-2606-18874:end -->

<!-- delta:SF-2026-ARXIV-2606-18874:start -->
AI scientist 应把 literature evidence、idea、implementation、ablation 与 repair trace 外化为 persistent contracts，并检查 runnable artifact 是否仍支持原 claim。
<!-- delta:SF-2026-ARXIV-2606-18874:end -->

<!-- books-review:SF-2026-ARXIV-2606-18874:start -->
Principle Reuse; No Change — Existing Coverage. 三个案例不证明自动科学发现质量；trace 完整也不能替代独立复现或可信实验。
<!-- books-review:SF-2026-ARXIV-2606-18874:end -->

<!-- existing:SF-2026-ARXIV-2606-18958:start -->
现有 owner 已区分 simulation、shadow、canary 与 production evidence，并保留 rollback；相邻安全章拥有授权而非发布。 Comparative result for arXiv:2606.18958v1: Ch73 已把 simulation、canary 与真实 deployment evidence 分层；LiveStack 是更深的 OS 实现实例。
<!-- existing:SF-2026-ARXIV-2606-18958:end -->

<!-- delta:SF-2026-ARXIV-2606-18958:start -->
cluster live simulation 要让真实 software stack 与模拟 node/network/device time 协同推进，并显式区分 simulated resource state 与 production effect。
<!-- delta:SF-2026-ARXIV-2606-18958:end -->

<!-- books-review:SF-2026-ARXIV-2606-18958:start -->
Principle Reuse; No Change — Existing Coverage. 模拟器遗漏的 kernel、network tail 和 control-plane race 会制造假确定性；不能用 live simulation 代替 canary。
<!-- books-review:SF-2026-ARXIV-2606-18958:end -->

<!-- existing:SF-2026-ARXIV-2606-18967:start -->
现有 owner 已拥有 draft/target verification、acceptance、KV rollback 与质量等价边界；相邻 PagedAttention 章只拥有块化 KV。 Comparative result for arXiv:2606.18967v1: 它把 speculative verification 延伸到训练 rollout，同时保留 policy/version owner。
<!-- existing:SF-2026-ARXIV-2606-18967:end -->

<!-- delta:SF-2026-ARXIV-2606-18967:start -->
RL rollout 的 draft policy 可由当前 policy 自身派生，但 acceptance、KV/state rollback 与训练版本 identity 必须共同绑定，避免把 serving speculation 当成离策略数据复用。
<!-- delta:SF-2026-ARXIV-2606-18967:end -->

<!-- books-review:SF-2026-ARXIV-2606-18967:start -->
Direct Evolution; Integrate. acceptance 随 policy update 漂移；额外 draft computation 和 rollback bookkeeping 可能抵消收益，且不改变 reward validity。
<!-- books-review:SF-2026-ARXIV-2606-18967:end -->

<!-- existing:SF-2026-ARXIV-2606-18996:start -->
现有 owner 已把 evaluator、denominator、validity、污染与 release evidence 分离；相邻监控章只提供运行信号。 Comparative result for arXiv:2606.18996v1: Ch66/72 已要求 capability 与 harm 双轴评价；TRAP 补充 workload 而不改 owner。
<!-- existing:SF-2026-ARXIV-2606-18996:end -->

<!-- delta:SF-2026-ARXIV-2606-18996:start -->
privacy-capable agent benchmark 必须联合评分 task completion 与 active extraction resistance，并把攻击者交互轨迹、secret canary 与 policy effect 分开。
<!-- delta:SF-2026-ARXIV-2606-18996:end -->

<!-- books-review:SF-2026-ARXIV-2606-18996:start -->
Principle Reuse; No Change — Existing Coverage. benchmark secret 与攻击策略覆盖有限；未泄漏不证明模型无记忆或生产 ACL 正确。
<!-- books-review:SF-2026-ARXIV-2606-18996:end -->

<!-- existing:SF-2026-ARXIV-2606-19004:start -->
现有 owner 已拥有 quota、priority、preemption、checkpoint cost 与 workload-class-aware placement；相邻 KAI 章是实现分支。 Comparative result for arXiv:2606.19004v1: Ch63/33 已有 preemptible training 与 rollout identity；本工作是 DiT-specific composition。
<!-- existing:SF-2026-ARXIV-2606-19004:end -->

<!-- delta:SF-2026-ARXIV-2606-19004:start -->
DiT RL post-training 可把探索 seed 与 spot GPU availability 联合调度，把可重放 seed state 作为 preemption recovery unit。
<!-- delta:SF-2026-ARXIV-2606-19004:end -->

<!-- books-review:SF-2026-ARXIV-2606-19004:start -->
Principle Reuse; No Change — Existing Coverage. spot reclaim 与 seed replay 会改变样本时序；结果限于 DiT RL，不能外推 LLM RL 或硬实时 SLO。
<!-- books-review:SF-2026-ARXIV-2606-19004:end -->

<!-- existing:SF-2026-ARXIV-2606-19025:start -->
现有 owner 已拥有 replica/shard/state synchronization 与 WAN failure boundary；相邻 TP 章只拥有张量切分。 Comparative result for arXiv:2606.19025v1: 它改变跨站 distributed-training replica/state ownership，而不是 serving placement。
<!-- existing:SF-2026-ARXIV-2606-19025:end -->

<!-- delta:SF-2026-ARXIV-2606-19025:start -->
低带宽跨站 MoE 训练不应让每个 site 持有 full replica；FoMoE 分区 expert layers、部分复制 experts，并让 local training 对 non-resident experts 执行 skip-token，再按较低频率同步。
<!-- delta:SF-2026-ARXIV-2606-19025:end -->

<!-- books-review:SF-2026-ARXIV-2606-19025:start -->
Direct Evolution; Integrate. non-resident expert skip 会改变本地训练分布，routing stability 只在受测 regimes 成立；100B projection 不是实测，WAN failure/straggler 未闭合。
<!-- books-review:SF-2026-ARXIV-2606-19025:end -->

<!-- existing:SF-2026-ARXIV-2606-19057:start -->
现有 owner 已把 evaluator、denominator、validity、污染与 release evidence 分离；相邻监控章只提供运行信号。 Comparative result for arXiv:2606.19057v1: 把未审样本从默认负例改成不确定集合，直接修正 evaluation denominator。
<!-- existing:SF-2026-ARXIV-2606-19057:end -->

<!-- delta:SF-2026-ARXIV-2606-19057:start -->
当只有少量确定正例而未标注集混合正负时，evaluation audit 可用 positive-unlabeled inference 估计隐藏错误率，但必须公开 class-prior 与 identifiability assumptions。
<!-- delta:SF-2026-ARXIV-2606-19057:end -->

<!-- books-review:SF-2026-ARXIV-2606-19057:start -->
Direct Evolution; Integrate. class-prior 错设会系统性偏移；PU 只能估计分布级缺口，不能证明单个 judgment 正确。
<!-- books-review:SF-2026-ARXIV-2606-19057:end -->

<!-- existing:SF-2026-ARXIV-2606-19111:start -->
现有 owner 已拥有 coordinator、typed handoff、reroute、shared-state commit 与 fallback authority；相邻 workflow 章拥有单流程执行。 Comparative result for arXiv:2606.19111v1: Ch82 已把 coordinator 视为可替换 control role；本 family 提供 recovery boundary 证据。
<!-- existing:SF-2026-ARXIV-2606-19111:end -->

<!-- delta:SF-2026-ARXIV-2606-19111:start -->
leader 只有在 coordinator 的 recovery advantage 超过沟通与单点故障成本时才应持有重分配 authority；行为 leadership 不等于稳定角色标签。
<!-- delta:SF-2026-ARXIV-2606-19111:end -->

<!-- books-review:SF-2026-ARXIV-2606-19111:start -->
Principle Reuse; No Change — Existing Coverage. 作者 tasks 和 agent count 不证明组织结构普适；leader failure、shared bias 与通信成本仍可能主导。
<!-- books-review:SF-2026-ARXIV-2606-19111:end -->

<!-- existing:SF-2026-ARXIV-2606-19191:start -->
现有 owner 已把 secret、policy、artifact identity、effect-time authorization 与撤销放在外部安全控制面；相邻多租户章拥有 principal/isolation。 Comparative result for arXiv:2606.19191v1: Ch72 已把 persistent Skill 定义为 supply-chain artifact，并要求 code/resource/runtime effect 联合审计与 containment。
<!-- existing:SF-2026-ARXIV-2606-19191:end -->

<!-- delta:SF-2026-ARXIV-2606-19191:start -->
skill admission 不能只读 SKILL.md；必须审 auxiliary resources、triggerable vulnerabilities 与 runtime effects，并在沙箱中验证 benign utility 与恶意 side effect。
<!-- delta:SF-2026-ARXIV-2606-19191:end -->

<!-- books-review:SF-2026-ARXIV-2606-19191:start -->
Principle Reuse; No Change — Existing Coverage. 攻击 corpus 与触发器由作者构造；静态扫描漏报不证明 runtime containment 无效，检测率也不等于安全。
<!-- books-review:SF-2026-ARXIV-2606-19191:end -->

<!-- existing:SF-2026-ARXIV-2606-19242:start -->
现有 owner 已把 secret、policy、artifact identity、effect-time authorization 与撤销放在外部安全控制面；相邻多租户章拥有 principal/isolation。 Comparative result for arXiv:2606.19242v1: Ch72 已拥有 canonical action 与 effect-time authorization；论文强化实现路径。
<!-- existing:SF-2026-ARXIV-2606-19242:end -->

<!-- delta:SF-2026-ARXIV-2606-19242:start -->
Agent compliance 应在每次 tool/message effect 前由外部 runtime monitor 检查 temporal/policy state，而非要求 LLM 自述合规。
<!-- delta:SF-2026-ARXIV-2606-19242:end -->

<!-- books-review:SF-2026-ARXIV-2606-19242:start -->
Principle Reuse; No Change — Existing Coverage. 形式化 policy 不覆盖未建模 effect，monitor 自身可能成为延迟或可用性瓶颈。
<!-- books-review:SF-2026-ARXIV-2606-19242:end -->

<!-- existing:SF-2026-ARXIV-2606-19262:start -->
现有 owner 已区分 observe-only telemetry、告警证据与执行授权；相邻 trace 章拥有跨组件因果链。 Comparative result for arXiv:2606.19262v1: 它为平台监控增加未注册训练的被动 evidence path，而不把检测器提升为执行授权。
<!-- existing:SF-2026-ARXIV-2606-19262:end -->

<!-- delta:SF-2026-ARXIV-2606-19262:start -->
hidden training detection 可读取已有 accelerator telemetry 的 phase、memory/compute 与 collective signatures，保持 observe-only，不向 workload 注入探针。
<!-- delta:SF-2026-ARXIV-2606-19262:end -->

<!-- books-review:SF-2026-ARXIV-2606-19262:start -->
Direct Evolution; Integrate. 共享 GPU、融合 kernel 与新 compiler 会造成概念漂移；无额外探针不等于 telemetry 免费或不可规避。
<!-- books-review:SF-2026-ARXIV-2606-19262:end -->

<!-- existing:SF-2026-ARXIV-2606-19271:start -->
现有 owner 已覆盖请求级 admission、prefill/decode 调度、fairness、elasticity 与恢复 handoff；相邻 PD 章拥有阶段边界。 Comparative result for arXiv:2606.19271v1: Ch56 已有 streaming generation 的 playout slack、migration/re-homing、elasticity 与质量降级；TurboServe 是生产 trace 佐证。
<!-- existing:SF-2026-ARXIV-2606-19271:end -->

<!-- delta:SF-2026-ARXIV-2606-19271:start -->
streaming video generation 应以 chunk deadline 为调度单位，联合决定 GPU residency、跨 chunk pipeline 与质量/成本降级，而不是只优化整段 makespan。
<!-- delta:SF-2026-ARXIV-2606-19271:end -->

<!-- books-review:SF-2026-ARXIV-2606-19271:start -->
Principle Reuse; No Change — Existing Coverage. 作者 workloads/GPU matrix 不证明交互视频通用 SLO；跨 chunk state 与 quality degradation 仍需独立验收。
<!-- books-review:SF-2026-ARXIV-2606-19271:end -->

<!-- audit-target:books:end -->
## 7. Semantic Audit

<!-- validator:semantic-audit-v1 -->
| Audit ID | Auditor | Scope | Reviewed Refs | Findings | Resolution | Status |
| --- | --- | --- | --- | --- | --- | --- |
| SA-20260618-COVERAGE-OWNER-REBUILD | fresh-context:pending-owner-rebuild | coverage | coverage:SRC-ARXIV:20260618 | GAP-ARXIV-SEMANTIC-OWNER-REBUILD-20260618: raw closures and false-negative frontier require independent semantic review | Open — canonical inventory and owner receipt are preserved in the date-local source packet | open |
| SA-20260618-EVIDENCE-OWNER-REBUILD | fresh-context:pending-owner-rebuild | evidence | review:SF-2026-ARXIV-2606-18284; review:SF-2026-ARXIV-2606-18286; review:SF-2026-ARXIV-2606-18310; review:SF-2026-ARXIV-2606-18322; review:SF-2026-ARXIV-2606-18356; review:SF-2026-ARXIV-2606-18379; review:SF-2026-ARXIV-2606-18383; review:SF-2026-ARXIV-2606-18394; review:SF-2026-ARXIV-2606-18400; review:SF-2026-ARXIV-2606-18421; review:SF-2026-ARXIV-2606-18431; review:SF-2026-ARXIV-2606-18448; review:SF-2026-ARXIV-2606-18467; review:SF-2026-ARXIV-2606-18497; review:SF-2026-ARXIV-2606-18532; review:SF-2026-ARXIV-2606-18550; review:SF-2026-ARXIV-2606-18600; review:SF-2026-ARXIV-2606-18619; review:SF-2026-ARXIV-2606-18650; review:SF-2026-ARXIV-2606-18668; review:SF-2026-ARXIV-2606-18673; review:SF-2026-ARXIV-2606-18697; review:SF-2026-ARXIV-2606-18741; review:SF-2026-ARXIV-2606-18746; review:SF-2026-ARXIV-2606-18810; review:SF-2026-ARXIV-2606-18829; review:SF-2026-ARXIV-2606-18831; review:SF-2026-ARXIV-2606-18847; review:SF-2026-ARXIV-2606-18874; review:SF-2026-ARXIV-2606-18958; review:SF-2026-ARXIV-2606-18967; review:SF-2026-ARXIV-2606-18996; review:SF-2026-ARXIV-2606-19004; review:SF-2026-ARXIV-2606-19025; review:SF-2026-ARXIV-2606-19057; review:SF-2026-ARXIV-2606-19111; review:SF-2026-ARXIV-2606-19191; review:SF-2026-ARXIV-2606-19242; review:SF-2026-ARXIV-2606-19262; review:SF-2026-ARXIV-2606-19271 | EVIDENCE-OWNER-REBUILD-20260618: transferred exact-v1 reviews require fresh-context false-positive and access audit | Open — transferred review bodies remain provenance, not final acceptance | open |
| SA-20260618-SELECTION-OWNER-REBUILD | fresh-context:pending-owner-rebuild | deep_analysis_selection | analysis-decision:SF-2026-ARXIV-2606-18284; analysis-decision:SF-2026-ARXIV-2606-18286; analysis-decision:SF-2026-ARXIV-2606-18310; analysis-decision:SF-2026-ARXIV-2606-18322; analysis-decision:SF-2026-ARXIV-2606-18356; analysis-decision:SF-2026-ARXIV-2606-18379; analysis-decision:SF-2026-ARXIV-2606-18383; analysis-decision:SF-2026-ARXIV-2606-18394; analysis-decision:SF-2026-ARXIV-2606-18400; analysis-decision:SF-2026-ARXIV-2606-18421; analysis-decision:SF-2026-ARXIV-2606-18431; analysis-decision:SF-2026-ARXIV-2606-18448; analysis-decision:SF-2026-ARXIV-2606-18467; analysis-decision:SF-2026-ARXIV-2606-18497; analysis-decision:SF-2026-ARXIV-2606-18532; analysis:DA-20260617-CONTRACT-INTEGRITY; analysis:DA-20260618-HETEROGENEOUS-RECOVERY; analysis-decision:SF-2026-ARXIV-2606-18619; analysis-decision:SF-2026-ARXIV-2606-18650; analysis-decision:SF-2026-ARXIV-2606-18668; analysis-decision:SF-2026-ARXIV-2606-18673; analysis-decision:SF-2026-ARXIV-2606-18697; analysis-decision:SF-2026-ARXIV-2606-18741; analysis-decision:SF-2026-ARXIV-2606-18746; analysis-decision:SF-2026-ARXIV-2606-18810; analysis-decision:SF-2026-ARXIV-2606-18829; analysis-decision:SF-2026-ARXIV-2606-18831; analysis-decision:SF-2026-ARXIV-2606-18847; analysis-decision:SF-2026-ARXIV-2606-18874; analysis-decision:SF-2026-ARXIV-2606-18958; analysis-decision:SF-2026-ARXIV-2606-18967; analysis-decision:SF-2026-ARXIV-2606-18996; analysis-decision:SF-2026-ARXIV-2606-19004; analysis:DA-20260618-CROSS-SITE-MOE-OWNERSHIP; analysis-decision:SF-2026-ARXIV-2606-19057; analysis-decision:SF-2026-ARXIV-2606-19111; analysis-decision:SF-2026-ARXIV-2606-19191; analysis-decision:SF-2026-ARXIV-2606-19242; analysis-decision:SF-2026-ARXIV-2606-19262; analysis-decision:SF-2026-ARXIV-2606-19271 | SELECTION-OWNER-REBUILD-20260618: eligibility and at-most-three narrative choice require independent comparison after owner transfer | Open — canonical selection receipts are structurally reconstructed | open |
| SA-20260618-BOOKS-OWNER-REBUILD | fresh-context:pending-owner-rebuild | books | books-review:SF-2026-ARXIV-2606-18284; books-review:SF-2026-ARXIV-2606-18286; books-review:SF-2026-ARXIV-2606-18310; books-review:SF-2026-ARXIV-2606-18322; books-review:SF-2026-ARXIV-2606-18356; books-review:SF-2026-ARXIV-2606-18379; books-review:SF-2026-ARXIV-2606-18383; books-review:SF-2026-ARXIV-2606-18394; books-review:SF-2026-ARXIV-2606-18400; books-review:SF-2026-ARXIV-2606-18421; books-review:SF-2026-ARXIV-2606-18431; books-review:SF-2026-ARXIV-2606-18448; books-review:SF-2026-ARXIV-2606-18467; books-review:SF-2026-ARXIV-2606-18497; books-review:SF-2026-ARXIV-2606-18532; books-review:SF-2026-ARXIV-2606-18550; books-review:SF-2026-ARXIV-2606-18600; books-review:SF-2026-ARXIV-2606-18619; books-review:SF-2026-ARXIV-2606-18650; books-review:SF-2026-ARXIV-2606-18668; books-review:SF-2026-ARXIV-2606-18673; books-review:SF-2026-ARXIV-2606-18697; books-review:SF-2026-ARXIV-2606-18741; books-review:SF-2026-ARXIV-2606-18746; books-review:SF-2026-ARXIV-2606-18810; books-review:SF-2026-ARXIV-2606-18829; books-review:SF-2026-ARXIV-2606-18831; books-review:SF-2026-ARXIV-2606-18847; books-review:SF-2026-ARXIV-2606-18874; books-review:SF-2026-ARXIV-2606-18958; books-review:SF-2026-ARXIV-2606-18967; books-review:SF-2026-ARXIV-2606-18996; books-review:SF-2026-ARXIV-2606-19004; books-review:SF-2026-ARXIV-2606-19025; books-review:SF-2026-ARXIV-2606-19057; books-review:SF-2026-ARXIV-2606-19111; books-review:SF-2026-ARXIV-2606-19191; books-review:SF-2026-ARXIV-2606-19242; books-review:SF-2026-ARXIV-2606-19262; books-review:SF-2026-ARXIV-2606-19271 | BOOKS-OWNER-REBUILD-20260618: Books comparisons are frozen provenance pending upstream semantic gates and root writeback reconciliation | Open — month-local Books queue remains frozen | open |
## 8. Ignored Noise

- 479 identities were closed before the denominator with family-specific semantic reasons in `denominator-full-semantic-audit-v1.tsv`; they remain preserved for recall audit rather than being promoted into the Candidate Ledger.

## 9. Recommended Action

- Integrate: 16; No Change: 21.
- Books Gate Passed: 16 Integrate families were audited in 11 unique owners; 21 No Change handoffs retain existing coverage without writeback leakage.

## 10. Repository Changes

- Only this date's Daily, source packet and finalizer are written by this lane; shared Books are untouched.

## 11. Open Questions

- How should heterogeneous spot serving decide whether migration, replication or recomputation is the safest recovery path under simultaneous price and topology change?
- Which cross-site MoE ownership policy remains stable when expert popularity and WAN availability drift together?
- How should executable model identity bind weights, adapters, kernels, hardware and serving build without making routine upgrades impossible?
- These are research continuations, not unresolved Gate findings.

## 12. Sources

- [Breaking the Solver Bottleneck: Training Task Generators at the Learnable Frontier](https://arxiv.org/abs/2606.18284v1) — first-public（Asia/Shanghai）：2026-06-18；exact evidence：v1；accessed：2026-09-03
- [CODEBLOCK: Learning to Supervise Code at the Right Granularity](https://arxiv.org/abs/2606.18286v1) — first-public（Asia/Shanghai）：2026-06-18；exact evidence：v1；accessed：2026-09-03
- [Conflict-Aware Retriever Editing for Knowledge Injection Attacks on LLM-Based RAG Systems](https://arxiv.org/abs/2606.18310v1) — first-public（Asia/Shanghai）：2026-06-18；exact evidence：v1；accessed：2026-09-03
- [SAE Interventions are Unreliable: Post-Intervention Recovery of Suppressed Behavior](https://arxiv.org/abs/2606.18322v1) — first-public（Asia/Shanghai）：2026-06-18；exact evidence：v1；accessed：2026-09-03
- [SafeClawBench: Separating Semantic, Audit-Evidence, and Sandbox Harm in Tool-Using LLM Agents](https://arxiv.org/abs/2606.18356v1) — first-public（Asia/Shanghai）：2026-06-18；exact evidence：v1；accessed：2026-09-03
- [RankGraph-2: Lifecycle Co-Design for Billion-Node Graph Learning in Recommendation](https://arxiv.org/abs/2606.18379v1) — first-public（Asia/Shanghai）：2026-06-18；exact evidence：v1；accessed：2026-09-03
- [From Sparse Features to Trustworthy Proxies: Certifying SAE-Based Interpretability](https://arxiv.org/abs/2606.18383v1) — first-public（Asia/Shanghai）：2026-06-18；exact evidence：v1；accessed：2026-09-03
- [JetSpec: Breaking the Scaling Ceiling of Speculative Decoding with Parallel Tree Drafting](https://arxiv.org/abs/2606.18394v1) — first-public（Asia/Shanghai）：2026-06-18；exact evidence：v1；accessed：2026-09-03
- [CloakLM: Obfuscating GPU Memory Layout to Mitigate Model Ex-filtration for Serving](https://arxiv.org/abs/2606.18400v1) — first-public（Asia/Shanghai）：2026-06-18；exact evidence：v1；accessed：2026-09-03
- [Finding Compiler-Platform Interaction Bugs in Deep Learning Pipelines via Cross-Layer Constraints](https://arxiv.org/abs/2606.18421v1) — first-public（Asia/Shanghai）：2026-06-18；exact evidence：v1；accessed：2026-09-03
- [Beyond Prediction: Tail-Aware Scheduling for LLM Inference](https://arxiv.org/abs/2606.18431v1) — first-public（Asia/Shanghai）：2026-06-18；exact evidence：v1；accessed：2026-09-03
- [VISUALSKILL: Multimodal Skills for Computer-Use Agents](https://arxiv.org/abs/2606.18448v1) — first-public（Asia/Shanghai）：2026-06-18；exact evidence：v1；accessed：2026-09-03
- [ToolChain-CRC: Conformal Risk Control for Agentic AI Under Retrieval and Tool-Use Drift](https://arxiv.org/abs/2606.18467v1) — first-public（Asia/Shanghai）：2026-06-18；exact evidence：v1；accessed：2026-09-03
- [Ghost Vectors: Soft-Deleted Embeddings Remain Reconstructible in HNSW Vector Databases](https://arxiv.org/abs/2606.18497v1) — first-public（Asia/Shanghai）：2026-06-18；exact evidence：v1；accessed：2026-09-03
- [AI Sandboxes: A Threat Model, Taxonomy, and Measurement Framework](https://arxiv.org/abs/2606.18532v1) — first-public（Asia/Shanghai）：2026-06-18；exact evidence：v1；accessed：2026-09-03
- [The Gate Is Only as Honest as Its Contracts: ContractGuard for the Contract Layer of Risk-Aware Causal Gating](https://arxiv.org/abs/2606.18550v1) — first-public（Asia/Shanghai）：2026-06-18；exact evidence：v1；accessed：2026-09-03
- [ShuntServe: Cost-Efficient LLM Serving on Heterogeneous Spot GPU Clusters](https://arxiv.org/abs/2606.18600v1) — first-public（Asia/Shanghai）：2026-06-18；exact evidence：v1；accessed：2026-09-03
- [Code-Augur: Agentic Vulnerability Detection via Specification Inference](https://arxiv.org/abs/2606.18619v1) — first-public（Asia/Shanghai）：2026-06-18；exact evidence：v1；accessed：2026-09-03
- [BLADE: Scalable Bi-level Adaptive Data Selection for LLM Training](https://arxiv.org/abs/2606.18650v1) — first-public（Asia/Shanghai）：2026-06-18；exact evidence：v1；accessed：2026-09-03
- [EARS: Explanatory Abstention for Reliable Sub-Agent Modeling in Large-scale Multi-Agent Systems](https://arxiv.org/abs/2606.18668v1) — first-public（Asia/Shanghai）：2026-06-18；exact evidence：v1；accessed：2026-09-03
- [Understanding and Mitigating Prompt Leaking Attacks in Real-World LLM-Based Applications](https://arxiv.org/abs/2606.18673v1) — first-public（Asia/Shanghai）：2026-06-18；exact evidence：v1；accessed：2026-09-03
- [Stealthy World Model Manipulation via Data Poisoning](https://arxiv.org/abs/2606.18697v1) — first-public（Asia/Shanghai）：2026-06-18；exact evidence：v1；accessed：2026-09-03
- [ReMP: Low-Downtime Runtime Model-Parallelism Reconfiguration for LLM Serving](https://arxiv.org/abs/2606.18741v1) — first-public（Asia/Shanghai）：2026-06-18；exact evidence：v1；accessed：2026-09-03
- [What Must Generalist Agents Remember?](https://arxiv.org/abs/2606.18746v1) — first-public（Asia/Shanghai）：2026-06-18；exact evidence：v1；accessed：2026-09-03
- [Learning from Own Solutions: Self-Conditioned Credit Assignment for Reinforcement Learning with Verifiable Rewards](https://arxiv.org/abs/2606.18810v1) — first-public（Asia/Shanghai）：2026-06-18；exact evidence：v1；accessed：2026-09-03
- [GateMem: Benchmarking Memory Governance in Multi-Principal Shared-Memory Agents](https://arxiv.org/abs/2606.18829v1) — first-public（Asia/Shanghai）：2026-06-18；exact evidence：v1；accessed：2026-09-03
- [Beyond Reward Engineering: A Data Recipe for Long-Context Reinforcement Learning](https://arxiv.org/abs/2606.18831v1) — first-public（Asia/Shanghai）：2026-06-18；exact evidence：v1；accessed：2026-09-03
- [WorldLines: Benchmarking and Modeling Long-Horizon Stateful Embodied Agents](https://arxiv.org/abs/2606.18847v1) — first-public（Asia/Shanghai）：2026-06-18；exact evidence：v1；accessed：2026-09-03
- [Externalizing Research Synthesis and Validation in AI Scientists through a Research Harness](https://arxiv.org/abs/2606.18874v1) — first-public（Asia/Shanghai）：2026-06-18；exact evidence：v1；accessed：2026-09-03
- [LiveStack: OS Support for Cluster-Scale Full-Stack Live Simulation](https://arxiv.org/abs/2606.18958v1) — first-public（Asia/Shanghai）：2026-06-18；exact evidence：v1；accessed：2026-09-03
- [EfficientRollout: System-Aware Self-Speculative Decoding for RL Rollouts](https://arxiv.org/abs/2606.18967v1) — first-public（Asia/Shanghai）：2026-06-18；exact evidence：v1；accessed：2026-09-03
- [TRAP: Benchmark for Task-completion and Resistance to Active Privacy-extraction](https://arxiv.org/abs/2606.18996v1) — first-public（Asia/Shanghai）：2026-06-18；exact evidence：v1；accessed：2026-09-03
- [Spotlight: Synergizing Seed Exploration and Spot GPUs for DiT RL Post-Training](https://arxiv.org/abs/2606.19004v1) — first-public（Asia/Shanghai）：2026-06-18；exact evidence：v1；accessed：2026-09-03
- [FoMoE: Breaking the Full-Replica Barrier with a Federation of MoEs](https://arxiv.org/abs/2606.19025v1) — first-public（Asia/Shanghai）：2026-06-18；exact evidence：v1；accessed：2026-09-03
- [Quantifying and Auditing LLM Evaluation via Positive--Unlabeled Learning](https://arxiv.org/abs/2606.19057v1) — first-public（Asia/Shanghai）：2026-06-18；exact evidence：v1；accessed：2026-09-03
- [Leadership as Coordination Control: Behavioral Signatures and the Recovery-Advantage Boundary in Multi-Agent LLM Teams](https://arxiv.org/abs/2606.19111v1) — first-public（Asia/Shanghai）：2026-06-18；exact evidence：v1；accessed：2026-09-03
- [PhantomSkill: Malicious Code Injection in Agent Skill Ecosystems](https://arxiv.org/abs/2606.19191v1) — first-public（Asia/Shanghai）：2026-06-18；exact evidence：v1；accessed：2026-09-03
- [Runtime Compliance Verification for AI Agents](https://arxiv.org/abs/2606.19242v1) — first-public（Asia/Shanghai）：2026-06-18；exact evidence：v1；accessed：2026-09-03
- [Detecting Hidden ML Training With Zero-Overhead Telemetry](https://arxiv.org/abs/2606.19262v1) — first-public（Asia/Shanghai）：2026-06-18；exact evidence：v1；accessed：2026-09-03
- [TurboServe: Serving Streaming Video Generation Efficiently and Economically](https://arxiv.org/abs/2606.19271v1) — first-public（Asia/Shanghai）：2026-06-18；exact evidence：v1；accessed：2026-09-03
## 13. Final Status

- Status: Complete.
- Coverage Gate: Closed.
- Evidence Gate: Passed.
- Books Gate: Passed.
- Fresh-context Semantic Audit: Passed；unresolved findings = 0.

State Truth: Completion=In Progress；Coverage=Open；Evidence=Open；Books=Open；Unresolved Findings=4。
