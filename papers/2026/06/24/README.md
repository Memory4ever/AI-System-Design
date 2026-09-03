# Daily Research — 2026-06-24

**Research Date:** 2026-06-24

**Timezone:** Asia/Shanghai

**Strict Window:** 2026-06-23 09:00:00 ～ 2026-06-24 09:00:00（北京时间，左闭右开）

**Contract:** V2.1 Full Replay；全量枚举与语义筛选冻结候选分母，技术 claim 回到 exact-version primary evidence 与事件时 artifact receipt

**Status:** In Progress；Coverage=Open、Evidence=Open、Books=Open；最新合同恢复状态见 Coverage 与第 7、13 节

## Executive Summary
Beijing window `[2026-06-23 09:00, 2026-06-24 09:00)` contains 541 registered identities. Full 541/541 title+abstract screening freezes 42 durable families and 499 family-specific exclusions (including withdrawn inputs). The 122/122 route-negative audit promoted Chorus II (`2606.25040v1`) as one false negative. All retained exact-v1 full texts have source-specific Method/Evaluation/counterevidence locators and ten-field benchmark contracts. Shared Books and LEARNING_STATE remain untouched.

## 1. Coverage

<!-- validator:report-metadata-v2 -->
| Field | Value |
| --- | --- |
| Contract Version | V2.1 |
| Score Schema | V2 |
| Report Type | Daily |
| Window Start | 2026-06-24 |
| Window End | 2026-06-24 |
| Registry Version | 2026-08-25 |
| Coverage Mode | Full Replay |
| Baseline Report | — |
| Changed Source IDs | — |
| Previous Denominator ID | — |
| Denominator ID | daily-v2.1:2026-06-24:4c83bfc338f0fa38 |
| Denominator Frozen At | 2026-08-29T07:20:00+08:00 |
| Completion Status | In Progress |
| Coverage Gate | Open |
| Evidence Gate | Open |
| Books Gate | Open |

### Source Coverage Receipt

<!-- validator:source-coverage-v2 -->
| Source ID | Window Start | Window End | Executed At | Endpoint / Filter | Result | Hits | Candidate Source Families | Pagination / Cursor | Window Watermark | Closure Evidence | Gap / Limitation ID |
| --- | --- | --- | --- | --- | --- | ---: | --- | --- | --- | --- | --- |
| SRC-ARXIV | 2026-06-23T09:00:00+08:00 | 2026-06-24T09:00:00+08:00 | 2026-08-29T07:20:00+08:00 | arXiv official availability schedule + exact-v1 Atom + DataCite DOI created | incomplete | 507 | SF-2026-ARXIV-2606-23740;SF-2026-ARXIV-2606-23743;SF-2026-ARXIV-2606-23752;SF-2026-ARXIV-2606-23754;SF-2026-ARXIV-2606-23768;SF-2026-ARXIV-2606-23797;SF-2026-ARXIV-2606-23858;SF-2026-ARXIV-2606-23872;SF-2026-ARXIV-2606-23892;SF-2026-ARXIV-2606-23915;SF-2026-ARXIV-2606-23927;SF-2026-ARXIV-2606-23937;SF-2026-ARXIV-2606-23961;SF-2026-ARXIV-2606-23969;SF-2026-ARXIV-2606-23983;SF-2026-ARXIV-2606-23989;SF-2026-ARXIV-2606-24004;SF-2026-ARXIV-2606-24020;SF-2026-ARXIV-2606-24033;SF-2026-ARXIV-2606-24040;SF-2026-ARXIV-2606-24074;SF-2026-ARXIV-2606-24081;SF-2026-ARXIV-2606-24119;SF-2026-ARXIV-2606-24124;SF-2026-ARXIV-2606-24133;SF-2026-ARXIV-2606-24143;SF-2026-ARXIV-2606-24151;SF-2026-ARXIV-2606-24177;SF-2026-ARXIV-2606-24204;SF-2026-ARXIV-2606-24245;SF-2026-ARXIV-2606-24311;SF-2026-ARXIV-2606-24322;SF-2026-ARXIV-2606-24402;SF-2026-ARXIV-2606-24408;SF-2026-ARXIV-2606-24428;SF-2026-ARXIV-2606-24437;SF-2026-ARXIV-2606-24467;SF-2026-ARXIV-2606-24506;SF-2026-ARXIV-2606-24535;SF-2026-ARXIV-2606-24551;SF-2026-ARXIV-2606-24598;SF-2026-ARXIV-2606-24626;SF-2026-ARXIV-2606-24722;SF-2026-ARXIV-2606-24774;SF-2026-ARXIV-2606-24775 | — | 2026-09-03T12:10:00+08:00 | ../_sources/daily-20260624/official-arxiv-first-public-owner-receipt-v1.json; coverage:SRC-ARXIV:20260624; unclosed: canonical candidate redistribution pending | GAP-ARXIV-CANONICAL-REDISTRIBUTION-20260624 |
<!-- coverage:SRC-ARXIV:20260624:start -->
All 356 Core, 63 keyword-routed and 122 route-negative identities were screened. Frozen arithmetic: `541 = 42 retained + 499 exclusions`; route-negative FN=`2606.25040`.
<!-- coverage:SRC-ARXIV:20260624:end -->


<!-- latest-contract-reopen:2026-06-24:start -->
### Latest-contract Reopen Notice

2026-09-03 全量复核重新打开本日报。旧 `Complete` 只证明原分母内部的表格算术，不证明当前 V2.1 Coverage：arXiv candidate owner receipt 已恢复；当前仍需按 canonical owner 重分配候选与分母。非空 source packet、原 Source Review 与 Books Comparison 暂作 provenance 保留，不作为最新合同验收结论。2026-08-25 才生效的新增来源不倒推为当日 Required receipt，只按 Source Delta Audit 检查真实 in-window family。当前 finding：`canonical_owner_candidate_redistribution_pending, fresh_context_per_identity_semantic_audit_pending, exact_primary_access_recheck_pending`。
<!-- latest-contract-reopen:2026-06-24:end -->

### Canonical raw-inventory recovery checkpoint

本轮已从非空官方 DataCite arXiv DOI snapshot 恢复 **507** 条注册类别 identity，并以 immutable DOI `created` 与候选级 announcement owner reconciliation 归档到本日。其中 **45** 条是旧报告 retained provenance，**462** 条已获得逐 family title+abstract closure proposal。这些 proposal 尚未经过 fresh-context false-positive/false-negative audit，旧候选也尚未按 canonical owner 完成重分配；因此 Coverage、Evidence、Books 与 Completion 继续保持 Open。

## 2. Candidate Ledger

<!-- validator:candidate-ledger-v2.1 -->
| Source Family ID | Primary Identifier | Event Identity | Owner Week | First-public Date | Supporting Source IDs | Design Delta | System Reach | Durability | Total | Candidate State | Review Status | Access Status | Review Override | Review Ref | Owner Report Ref | Prior Review Ref | Reconciliation | Stable Node ID | Books Disposition | Books Review Ref | Benchmark Claim |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2606-23740 | arXiv:2606.23740v1 | paper-v1:2606.23740 | 2026-W26 | 2026-06-24 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-23740 | self | — | new_in_window | TRAIN-RLHF | Integrate | books-review:SF-2026-ARXIV-2606-23740 | yes |
| SF-2026-ARXIV-2606-23743 | arXiv:2606.23743v1 | paper-v1:2606.23743 | 2026-W26 | 2026-06-24 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-23743 | self | — | new_in_window | INFER-TENSORRT-LLM | Integrate | books-review:SF-2026-ARXIV-2606-23743 | yes |
| SF-2026-ARXIV-2606-23752 | arXiv:2606.23752v1 | paper-v1:2606.23752 | 2026-W26 | 2026-06-24 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-23752 | self | — | new_in_window | AGENT-MEMORY | Integrate | books-review:SF-2026-ARXIV-2606-23752 | yes |
| SF-2026-ARXIV-2606-23754 | arXiv:2606.23754v1 | paper-v1:2606.23754 | 2026-W26 | 2026-06-24 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-23754 | self | — | new_in_window | MULTIMODAL-EMBODIED-VLA | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-23754 | yes |
| SF-2026-ARXIV-2606-23768 | arXiv:2606.23768v1 | paper-v1:2606.23768 | 2026-W26 | 2026-06-24 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-23768 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-23768 | yes |
| SF-2026-ARXIV-2606-23797 | arXiv:2606.23797v1 | paper-v1:2606.23797 | 2026-W26 | 2026-06-24 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-23797 | self | — | new_in_window | AGENT-WORKFLOW | Integrate | books-review:SF-2026-ARXIV-2606-23797 | yes |
| SF-2026-ARXIV-2606-23858 | arXiv:2606.23858v1 | paper-v1:2606.23858 | 2026-W26 | 2026-06-24 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-23858 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-23858 | yes |
| SF-2026-ARXIV-2606-23872 | arXiv:2606.23872v1 | paper-v1:2606.23872 | 2026-W26 | 2026-06-24 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-23872 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-23872 | yes |
| SF-2026-ARXIV-2606-23892 | arXiv:2606.23892v1 | paper-v1:2606.23892 | 2026-W26 | 2026-06-24 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-23892 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-23892 | yes |
| SF-2026-ARXIV-2606-23915 | arXiv:2606.23915v1 | paper-v1:2606.23915 | 2026-W26 | 2026-06-24 | SRC-ARXIV | 2 | 3 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-23915 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-23915 | yes |
| SF-2026-ARXIV-2606-23927 | arXiv:2606.23927v1 | paper-v1:2606.23927 | 2026-W26 | 2026-06-24 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-23927 | self | — | new_in_window | PLATFORM-SECURITY | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-23927 | yes |
| SF-2026-ARXIV-2606-23937 | arXiv:2606.23937v1 | paper-v1:2606.23937 | 2026-W26 | 2026-06-24 | SRC-ARXIV | 2 | 3 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-23937 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-23937 | yes |
| SF-2026-ARXIV-2606-23961 | arXiv:2606.23961v1 | paper-v1:2606.23961 | 2026-W26 | 2026-06-24 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-23961 | self | — | new_in_window | INFER-KV-CACHE | Integrate | books-review:SF-2026-ARXIV-2606-23961 | yes |
| SF-2026-ARXIV-2606-23969 | arXiv:2606.23969v1 | paper-v1:2606.23969 | 2026-W26 | 2026-06-24 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-23969 | self | — | new_in_window | PLATFORM-SECURITY | Integrate | books-review:SF-2026-ARXIV-2606-23969 | yes |
| SF-2026-ARXIV-2606-23983 | arXiv:2606.23983v1 | paper-v1:2606.23983 | 2026-W26 | 2026-06-24 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-23983 | self | — | new_in_window | AGENT-PLATFORM | Integrate | books-review:SF-2026-ARXIV-2606-23983 | yes |
| SF-2026-ARXIV-2606-23989 | arXiv:2606.23989v1 | paper-v1:2606.23989 | 2026-W26 | 2026-06-24 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-23989 | self | — | new_in_window | AGENT-RAG | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-23989 | yes |
| SF-2026-ARXIV-2606-24004 | arXiv:2606.24004v1 | paper-v1:2606.24004 | 2026-W26 | 2026-06-24 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-24004 | self | — | new_in_window | TRAIN-RLHF | Integrate | books-review:SF-2026-ARXIV-2606-24004 | yes |
| SF-2026-ARXIV-2606-24020 | arXiv:2606.24020v1 | paper-v1:2606.24020 | 2026-W26 | 2026-06-24 | SRC-ARXIV | 2 | 3 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-24020 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-24020 | yes |
| SF-2026-ARXIV-2606-24033 | arXiv:2606.24033v1 | paper-v1:2606.24033 | 2026-W26 | 2026-06-24 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-24033 | self | — | new_in_window | INFER-KV-CACHE | Integrate | books-review:SF-2026-ARXIV-2606-24033 | yes |
| SF-2026-ARXIV-2606-24040 | arXiv:2606.24040v1 | paper-v1:2606.24040 | 2026-W26 | 2026-06-24 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-24040 | self | — | new_in_window | AGENT-MEMORY | Integrate | books-review:SF-2026-ARXIV-2606-24040 | yes |
| SF-2026-ARXIV-2606-24074 | arXiv:2606.24074v1 | paper-v1:2606.24074 | 2026-W26 | 2026-06-24 | SRC-ARXIV | 2 | 3 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-24074 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Integrate | books-review:SF-2026-ARXIV-2606-24074 | yes |
| SF-2026-ARXIV-2606-24081 | arXiv:2606.24081v1 | paper-v1:2606.24081 | 2026-W26 | 2026-06-24 | SRC-ARXIV | 2 | 3 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-24081 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Integrate | books-review:SF-2026-ARXIV-2606-24081 | yes |
| SF-2026-ARXIV-2606-24119 | arXiv:2606.24119v1 | paper-v1:2606.24119 | 2026-W26 | 2026-06-24 | SRC-ARXIV | 2 | 3 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-24119 | self | — | new_in_window | PLATFORM-MONITORING | Integrate | books-review:SF-2026-ARXIV-2606-24119 | yes |
| SF-2026-ARXIV-2606-24124 | arXiv:2606.24124v1 | paper-v1:2606.24124 | 2026-W26 | 2026-06-24 | SRC-ARXIV | 2 | 3 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-24124 | self | — | new_in_window | PLATFORM-EVALUATION-SYSTEM | Integrate | books-review:SF-2026-ARXIV-2606-24124 | yes |
| SF-2026-ARXIV-2606-24133 | arXiv:2606.24133v1 | paper-v1:2606.24133 | 2026-W26 | 2026-06-24 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-24133 | self | — | new_in_window | TRAIN-DATA | Integrate | books-review:SF-2026-ARXIV-2606-24133 | yes |
| SF-2026-ARXIV-2606-24143 | arXiv:2606.24143v1 | paper-v1:2606.24143 | 2026-W26 | 2026-06-24 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-24143 | self | — | new_in_window | TRAIN-DISTRIBUTED-TRAINING | Integrate | books-review:SF-2026-ARXIV-2606-24143 | yes |
| SF-2026-ARXIV-2606-24151 | arXiv:2606.24151v1 | paper-v1:2606.24151 | 2026-W26 | 2026-06-24 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-24151 | self | — | new_in_window | AGENT-MEMORY | Integrate | books-review:SF-2026-ARXIV-2606-24151 | yes |
| SF-2026-ARXIV-2606-24177 | arXiv:2606.24177v1 | paper-v1:2606.24177 | 2026-W26 | 2026-06-24 | SRC-ARXIV | 2 | 3 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-24177 | self | — | new_in_window | AGENT-WORKFLOW | Integrate | books-review:SF-2026-ARXIV-2606-24177 | yes |
| SF-2026-ARXIV-2606-24204 | arXiv:2606.24204v1 | paper-v1:2606.24204 | 2026-W26 | 2026-06-24 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-24204 | self | — | new_in_window | AGENT-RAG | Integrate | books-review:SF-2026-ARXIV-2606-24204 | yes |
| SF-2026-ARXIV-2606-24245 | arXiv:2606.24245v1 | paper-v1:2606.24245 | 2026-W26 | 2026-06-24 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-24245 | self | — | new_in_window | PLATFORM-SECURITY | Integrate | books-review:SF-2026-ARXIV-2606-24245 | yes |
| SF-2026-ARXIV-2606-24311 | arXiv:2606.24311v1 | paper-v1:2606.24311 | 2026-W26 | 2026-06-24 | SRC-ARXIV | 2 | 3 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-24311 | self | — | new_in_window | AGENT-PLATFORM | Integrate | books-review:SF-2026-ARXIV-2606-24311 | yes |
| SF-2026-ARXIV-2606-24322 | arXiv:2606.24322v1 | paper-v1:2606.24322 | 2026-W26 | 2026-06-24 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-24322 | self | — | new_in_window | PLATFORM-SECURITY | Integrate | books-review:SF-2026-ARXIV-2606-24322 | yes |
| SF-2026-ARXIV-2606-24402 | arXiv:2606.24402v1 | paper-v1:2606.24402 | 2026-W26 | 2026-06-24 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-24402 | self | — | new_in_window | PLATFORM-SECURITY | Integrate | books-review:SF-2026-ARXIV-2606-24402 | yes |
| SF-2026-ARXIV-2606-24408 | arXiv:2606.24408v1 | paper-v1:2606.24408 | 2026-W26 | 2026-06-24 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-24408 | self | — | new_in_window | PLATFORM-SECURITY | Integrate | books-review:SF-2026-ARXIV-2606-24408 | yes |
| SF-2026-ARXIV-2606-24428 | arXiv:2606.24428v1 | paper-v1:2606.24428 | 2026-W26 | 2026-06-24 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-24428 | self | — | new_in_window | AGENT-MEMORY | Integrate | books-review:SF-2026-ARXIV-2606-24428 | yes |
| SF-2026-ARXIV-2606-24437 | arXiv:2606.24437v1 | paper-v1:2606.24437 | 2026-W26 | 2026-06-24 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-24437 | self | — | new_in_window | AGENT-MULTI-AGENT | Integrate | books-review:SF-2026-ARXIV-2606-24437 | yes |
| SF-2026-ARXIV-2606-24467 | arXiv:2606.24467v1 | paper-v1:2606.24467 | 2026-W26 | 2026-06-24 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-24467 | self | — | new_in_window | INFER-KV-CACHE | Integrate | books-review:SF-2026-ARXIV-2606-24467 | yes |
| SF-2026-ARXIV-2606-24506 | arXiv:2606.24506v1 | paper-v1:2606.24506 | 2026-W26 | 2026-06-24 | SRC-ARXIV | 3 | 2 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-24506 | self | — | new_in_window | INFER-GPU-MEMORY | Integrate | books-review:SF-2026-ARXIV-2606-24506 | yes |
| SF-2026-ARXIV-2606-24535 | arXiv:2606.24535v1 | paper-v1:2606.24535 | 2026-W26 | 2026-06-24 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-24535 | self | — | new_in_window | AGENT-MEMORY | Integrate | books-review:SF-2026-ARXIV-2606-24535 | yes |
| SF-2026-ARXIV-2606-24551 | arXiv:2606.24551v1 | paper-v1:2606.24551 | 2026-W26 | 2026-06-24 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-24551 | self | — | new_in_window | AGENT-TOOL-CALLING | Integrate | books-review:SF-2026-ARXIV-2606-24551 | yes |
| SF-2026-ARXIV-2606-24598 | arXiv:2606.24598v1 | paper-v1:2606.24598 | 2026-W26 | 2026-06-24 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-24598 | self | — | new_in_window | AGENT-WORKFLOW | Integrate | books-review:SF-2026-ARXIV-2606-24598 | yes |
| SF-2026-ARXIV-2606-24626 | arXiv:2606.24626v1 | paper-v1:2606.24626 | 2026-W26 | 2026-06-24 | SRC-ARXIV | 2 | 3 | 3 | 8 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-24626 | self | — | new_in_window | PLATFORM-TRACE | Integrate | books-review:SF-2026-ARXIV-2606-24626 | yes |
| SF-2026-ARXIV-2606-24722 | arXiv:2606.24722v1 | paper-v1:2606.24722 | 2026-W26 | 2026-06-24 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-24722 | self | — | new_in_window | TRAIN-DISTRIBUTED-TRAINING | Integrate | books-review:SF-2026-ARXIV-2606-24722 | yes |
| SF-2026-ARXIV-2606-24774 | arXiv:2606.24774v1 | paper-v1:2606.24774 | 2026-W26 | 2026-06-24 | SRC-ARXIV | 3 | 3 | 3 | 9 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-24774 | self | — | new_in_window | PLATFORM-SECURITY | Integrate | books-review:SF-2026-ARXIV-2606-24774 | yes |
| SF-2026-ARXIV-2606-24775 | arXiv:2606.24775v1 | paper-v1:2606.24775 | 2026-W26 | 2026-06-24 | SRC-ARXIV | 2 | 2 | 3 | 7 | retained | deep_complete | accessible | none | review:SF-2026-ARXIV-2606-24775 | self | — | new_in_window | AGENT-MEMORY | Integrate | books-review:SF-2026-ARXIV-2606-24775 | yes |
## 3. Review Completion Receipt

<!-- validator:review-completion-v1 -->
| Source Family ID | Review Provenance ID | Review Route | Primary Evidence Version | Reviewed Evidence Versions | Method / Identity Locators | Evaluation Locators | Limitations / Counterevidence Locators | Artifact Locators | Claim Boundary Ref | Completion Result |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2606-23740 | RP-02f2b384995468a9 | deep | arXiv:2606.23740v1 | SRC-ARXIV@arXiv:2606.23740v1 | arXiv:2606.23740v1 §2 Experimental Setup | arXiv:2606.23740v1 §3 Results | arXiv:2606.23740v1 §4 Discussion; Limitations | Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review | claim:SF-2026-ARXIV-2606-23740 | complete |
| SF-2026-ARXIV-2606-23743 | RP-fe5cad506324cb8b | deep | arXiv:2606.23743v1 | SRC-ARXIV@arXiv:2606.23743v1 | arXiv:2606.23743v1 §3 Sol Architecture; §4 Agent-Native Optimization | arXiv:2606.23743v1 §5 Experiments | arXiv:2606.23743v1 §6 Limitations and Future Work | Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review | claim:SF-2026-ARXIV-2606-23743 | complete |
| SF-2026-ARXIV-2606-23752 | RP-11e539991b780b79 | deep | arXiv:2606.23752v1 | SRC-ARXIV@arXiv:2606.23752v1 | arXiv:2606.23752v1 — §ESAA-Conversational: An Event-Sourced Memory Layer for Continuity, Handoff, and Curation Across Heterogeneous LLM Coding Agents; §2.2 Agent Memory; §4 Architecture | arXiv:2606.23752v1 — §8 Self-Referential Case Study | arXiv:2606.23752v1 — §9 Discussion; §Validation Scope; §10 Future Work | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-23752 | complete |
| SF-2026-ARXIV-2606-23754 | RP-80d253258f7416f4 | deep | arXiv:2606.23754v1 | SRC-ARXIV@arXiv:2606.23754v1 | arXiv:2606.23754v1 — §3 The FEARL Architecture; §4 Enabling Verification via Decomposition; §4.1 Theoretical Guarantees | arXiv:2606.23754v1 — §5 Experiments; §5.1 Experimental Setup; §5.3 Does the Decomposition Enable Verification? | arXiv:2606.23754v1 — §6 Discussion and Conclusion; §A Proof of Propositions | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-23754 | complete |
| SF-2026-ARXIV-2606-23768 | RP-b661157832cc1cc6 | deep | arXiv:2606.23768v1 | SRC-ARXIV@arXiv:2606.23768v1 | arXiv:2606.23768v1 — §2 A compact slice of maths; §4 How to apply this mathematics to AI agents | arXiv:2606.23768v1 — §3 Examples; §3.2 A recursive example | arXiv:2606.23768v1 — §5 Related work; §6 Conclusions | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-23768 | complete |
| SF-2026-ARXIV-2606-23797 | RP-586d92ff695ed1ea | deep | arXiv:2606.23797v1 | SRC-ARXIV@arXiv:2606.23797v1 | arXiv:2606.23797v1 — §9.5 Turn-Level Algorithm; §10 Design Principles; §11 Evaluation Protocol | arXiv:2606.23797v1 — §11 Evaluation Protocol | arXiv:2606.23797v1 — §15 Contributions, Scope, and Validity; §16 Conclusion | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-23797 | complete |
| SF-2026-ARXIV-2606-23858 | RP-eaf7eb4ee5291e7e | deep | arXiv:2606.23858v1 | SRC-ARXIV@arXiv:2606.23858v1 | arXiv:2606.23858v1 — §3 Robustness Operators; §4 Algorithms; §4.2 Refine & Check Algorithm | arXiv:2606.23858v1 — §5 Implementation; §Experimental Setup.; §Experimental Results. | arXiv:2606.23858v1 — §4.3 The Complexity of Apothem Optimality; §4.4 The Intractability of Volume Optimality; §7 Conclusions | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-23858 | complete |
| SF-2026-ARXIV-2606-23872 | RP-9dc4566b622d4196 | deep | arXiv:2606.23872v1 | SRC-ARXIV@arXiv:2606.23872v1 | arXiv:2606.23872v1 — §3 Member vs Generated Inference; §5 Proposed Data Circuit Breaker; §5.3 Attribution Protocol | arXiv:2606.23872v1 — §6 Empirical Evaluation; §6.1 Experimental Setup; §6.2 Evaluation on the Direct Training Setting | arXiv:2606.23872v1 — §4 Limitations of MIA and Attribution Methods; §4.1 CPD-based Methods Fall Short for MGI; §7 Conclusions | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-23872 | complete |
| SF-2026-ARXIV-2606-23892 | RP-06593621965cfe01 | deep | arXiv:2606.23892v1 | SRC-ARXIV@arXiv:2606.23892v1 | arXiv:2606.23892v1 — §Black-box threat model.; §Appendix D Attack Method Details; §Appendix E Defense Method Details | arXiv:2606.23892v1 — §ReaLM : A Unified Red-Teaming Benchmark for Physical-World VLMs; §2.2 Red-Teaming Benchmark; §3 ReaLM : Benchmark for Physical-World VLMs | arXiv:2606.23892v1 — §6 Conclusion | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-23892 | complete |
| SF-2026-ARXIV-2606-23915 | RP-40bb5ab37448548e | deep | arXiv:2606.23915v1 | SRC-ARXIV@arXiv:2606.23915v1 | arXiv:2606.23915v1 — §3 A Sentence-Unit Provenance-Ranking Score; §3.1 Provenance/topicality | arXiv:2606.23915v1 — §4 The Cross-Dataset Audit; §5 ERCR as a Boundary Probe; §F Independent Replication and Robustness | arXiv:2606.23915v1 — §An external boundary: long-form alone does not predict the NLI failure.; §7 Limitations | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-23915 | complete |
| SF-2026-ARXIV-2606-23927 | RP-8e7f0b0083cecfe5 | deep | arXiv:2606.23927v1 | SRC-ARXIV@arXiv:2606.23927v1 | arXiv:2606.23927v1 — §4 NodeSpec: System Representation; §6 RIFT-Bench Framework; §F.2 Framework and Architecture Matrix | arXiv:2606.23927v1 — §7.1 Structure Identifier Evaluation; §Appendix A Additional Comparison to Agentic Security Evaluation; §E.3 Evaluation Metrics | arXiv:2606.23927v1 — §8 Discussion | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-23927 | complete |
| SF-2026-ARXIV-2606-23937 | RP-ce5655baa3fd33ee | deep | arXiv:2606.23937v1 | SRC-ARXIV@arXiv:2606.23937v1 | arXiv:2606.23937v1 — §Sensitivity to domain and query construction. | arXiv:2606.23937v1 — §Decision models and evaluation.; §Analysis of informative nonmatching clauses.; §B.1 Primary 3B result | arXiv:2606.23937v1 — §Contribution and scope.; §Construct scope.; §7 Conclusion | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-23937 | complete |
| SF-2026-ARXIV-2606-23961 | RP-66063867de9c70fe | deep | arXiv:2606.23961v1 | SRC-ARXIV@arXiv:2606.23961v1 | arXiv:2606.23961v1 — §2 Nexus Sampling; §2.2 Nexus Scoring; §2.3 Weighted Reservoir Block Selection | arXiv:2606.23961v1 — §5 Experiments; §5.1 Setup; §5.2–§5.6 Results and Ablations | arXiv:2606.23961v1 — §7 Conclusion; §A.5 Eviction Quality Under Approximate Future Utility | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-23961 | complete |
| SF-2026-ARXIV-2606-23969 | RP-33e058893082b031 | deep | arXiv:2606.23969v1 | SRC-ARXIV@arXiv:2606.23969v1 | arXiv:2606.23969v1 — §3 Platforms and Method; §4.1 Compute and GPU-Local Memory Are at Parity; §5.6 Runtime Design Rule | arXiv:2606.23969v1 — §3.3 Experiment Families; §5 Case Study: Policy Inversion in the Serving Runtime; §6 Case Study: Movement Engineering for Loading and KV State | arXiv:2606.23969v1 — §3.4 Comparability and Claim Scope; §11 Conclusion | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-23969 | complete |
| SF-2026-ARXIV-2606-23983 | RP-f9f797d0ada49233 | deep | arXiv:2606.23983v1 | SRC-ARXIV@arXiv:2606.23983v1 | arXiv:2606.23983v1 — §3. From Algebra to Architecture; §4. Harness Architecture; §5. Design Rationale and System Invariants | arXiv:2606.23983v1 — §12. Evaluation Methodology; §Simulation study (this paper). | arXiv:2606.23983v1 — §15. Discussion: Failure Modes and Guidance; §16. Limitations and Threats to Validity; §17. Conclusion | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-23983 | complete |
| SF-2026-ARXIV-2606-23989 | RP-09c8220b5834cfb1 | deep | arXiv:2606.23989v1 | SRC-ARXIV@arXiv:2606.23989v1 | arXiv:2606.23989v1 — §Attribution by Construction: Claim-Anchored Evidence for Faithfulness-Oriented Multi-Document Summarization; §3 Method; §Training labels by distant supervision. | arXiv:2606.23989v1 — §Faithful summarization and its evaluation.; §4.3 Evaluation Protocol; §5 Results and Analysis | arXiv:2606.23989v1 — §6 Conclusion | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-23989 | complete |
| SF-2026-ARXIV-2606-24004 | RP-16a0a13de80e0da0 | deep | arXiv:2606.24004v1 | SRC-ARXIV@arXiv:2606.24004v1 | arXiv:2606.24004v1 — §4 Spec Learning Framework; §4.1 Selection Method; §4.4 Judge protocol and selection | arXiv:2606.24004v1 — §5 Results; §B Statistical robustness; §C Judge calibration | arXiv:2606.24004v1 — §6 Discussion; §7 Limitations; §8 Conclusions and Future Work | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-24004 | complete |
| SF-2026-ARXIV-2606-24020 | RP-ade71f3c2dbfa40f | deep | arXiv:2606.24020v1 | SRC-ARXIV@arXiv:2606.24020v1 | arXiv:2606.24020v1 — §You Don’t Need to Run Every Eval Yuchen Zeng & Dimitris Papailiopoulos; §1 Introduction [You Don't Need to Run Every Eval exact-v1 method boundary] | arXiv:2606.24020v1 — §4 BenchPress : A Low-rank Benchmark Score Predictor; §4.3 BenchPress vs. LLMs as Benchmark Score Predictors; §5 What BenchPress Enables for Model Evaluation | arXiv:2606.24020v1 — §7 Discussion | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-24020 | complete |
| SF-2026-ARXIV-2606-24033 | RP-5219f6750e78abe2 | deep | arXiv:2606.24033v1 | SRC-ARXIV@arXiv:2606.24033v1 | arXiv:2606.24033v1 — §RoPE-Aware Bit Allocation for KV-Cache Quantization; §1 Introduction [RoPE-Aware Bit Allocation for KV-Cache Quantization exact-v1 method boundary] | arXiv:2606.24033v1 — §6.3 Downstream Evaluation | arXiv:2606.24033v1 — §7 Conclusion | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-24033 | complete |
| SF-2026-ARXIV-2606-24040 | RP-3941cc06f46e95b8 | deep | arXiv:2606.24040v1 | SRC-ARXIV@arXiv:2606.24040v1 | arXiv:2606.24040v1 — §3 Version-aware Operations; §4 Version and Transaction Correlation Memories | arXiv:2606.24040v1 — §5 Examples; §5.1 Direct sequence-level replacement; §5.2 Structured diff-level update | arXiv:2606.24040v1 — §6 Evaluation Roadmap and Scope; §7 Conclusion | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-24040 | complete |
| SF-2026-ARXIV-2606-24074 | RP-796c422ee9c9f5dc | deep | arXiv:2606.24074v1 | SRC-ARXIV@arXiv:2606.24074v1 | https://arxiv.org/html/2606.24074v1 — §3 Reliability Certification Setup; 4 Constructing a Certification SOTM | https://arxiv.org/html/2606.24074v1 — §5 A Matching Reliability Certification Lower Bound | https://arxiv.org/html/2606.24074v1 — §6 Conclusion and the stated small-error asymptotic regime | Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review | claim:SF-2026-ARXIV-2606-24074 | complete |
| SF-2026-ARXIV-2606-24081 | RP-e2d82d66c6d45a49 | deep | arXiv:2606.24081v1 | SRC-ARXIV@arXiv:2606.24081v1 | https://arxiv.org/html/2606.24081v1 — §3 PixJail Framework; 3.2 Attack Module; 3.3 Evaluation Pipeline; 3.4 Memory Updates | https://arxiv.org/html/2606.24081v1 — §4 Experiments; 4.1 Data, Models and Metrics; 4.3 Main Results | https://arxiv.org/html/2606.24081v1 — §6 Limitations | Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review | claim:SF-2026-ARXIV-2606-24081 | complete |
| SF-2026-ARXIV-2606-24119 | RP-26bb39563e56165f | deep | arXiv:2606.24119v1 | SRC-ARXIV@arXiv:2606.24119v1 | https://arxiv.org/html/2606.24119v1 — §3 Methodology; 3.2 Experimental Setup | https://arxiv.org/html/2606.24119v1 — §4 Experiments and Results; 4.1 Calibrated Triage | https://arxiv.org/html/2606.24119v1 — §D Mechanism and Boundary Audit; Definitions and non-portability | Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review | claim:SF-2026-ARXIV-2606-24119 | complete |
| SF-2026-ARXIV-2606-24124 | RP-25d991341c801ed6 | deep | arXiv:2606.24124v1 | SRC-ARXIV@arXiv:2606.24124v1 | https://arxiv.org/html/2606.24124v1 — §3 DSL for Reasoning Trace Formalization; 4 Structured Verification | https://arxiv.org/html/2606.24124v1 — §5 Evaluation; E Standalone Verification on ProcessBench | https://arxiv.org/html/2606.24124v1 — §F Limitations and Future Work | Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review | claim:SF-2026-ARXIV-2606-24124 | complete |
| SF-2026-ARXIV-2606-24133 | RP-b5eab3a600c6f7f1 | deep | arXiv:2606.24133v1 | SRC-ARXIV@arXiv:2606.24133v1 | https://arxiv.org/html/2606.24133v1 — §2 Methodology: The Holistic Data Scheduler; 2.2 Online Data Mixing | https://arxiv.org/html/2606.24133v1 — §3 Experiments and Analysis; 3.1 Experimental Setup | https://arxiv.org/html/2606.24133v1 — §B Sensitivity Analysis of Reward Weights; C Hyperparameter Sensitivity | Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review | claim:SF-2026-ARXIV-2606-24133 | complete |
| SF-2026-ARXIV-2606-24143 | RP-af2ee7619784ea13 | deep | arXiv:2606.24143v1 | SRC-ARXIV@arXiv:2606.24143v1 | https://arxiv.org/html/2606.24143v1 — §4 Forward- and Reverse-KL OPD Under Staleness; 7 AsyncOPD | https://arxiv.org/html/2606.24143v1 — §7 AsyncOPD Experimental Results; G Scheduler Details | https://arxiv.org/html/2606.24143v1 — §8 Limitations and Future Work | https://github.com/furiosa-ai/async-opd | claim:SF-2026-ARXIV-2606-24143 | complete |
| SF-2026-ARXIV-2606-24151 | RP-348fc84ec73632b3 | deep | arXiv:2606.24151v1 | SRC-ARXIV@arXiv:2606.24151v1 | https://arxiv.org/html/2606.24151v1 — §3 The Metis System; 3.2 Text Reflection; 3.3 Code Generation; 3.4 Memory Manager | https://arxiv.org/html/2606.24151v1 — §4 Experiments; A.1 Profiling Experiments | https://arxiv.org/html/2606.24151v1 — §A.1 Per-Axis Analysis and reported construction/transfer trade-offs | Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review | claim:SF-2026-ARXIV-2606-24151 | complete |
| SF-2026-ARXIV-2606-24177 | RP-94024f5ac16d206e | deep | arXiv:2606.24177v1 | SRC-ARXIV@arXiv:2606.24177v1 | https://arxiv.org/html/2606.24177v1 — §2 Design Principles; 3 System Architecture | https://arxiv.org/html/2606.24177v1 — §4 Where Human Judgment Is Irreducible; A/B Case Studies | https://arxiv.org/html/2606.24177v1 — §4.7 What the Architecture Can and Cannot Absorb; 4.8 Boundary Is a Snapshot | Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review | claim:SF-2026-ARXIV-2606-24177 | complete |
| SF-2026-ARXIV-2606-24204 | RP-d970a20b4e8b1957 | deep | arXiv:2606.24204v1 | SRC-ARXIV@arXiv:2606.24204v1 | https://arxiv.org/html/2606.24204v1 — §III Unified Dominance Abstraction; IV/V Unified Dominance Graph | https://arxiv.org/html/2606.24204v1 — §VI Experiment; Search Performance and Index Construction | https://arxiv.org/html/2606.24204v1 — §V-B Validity-Preserving Patch Edges; VI-D Impact of Patch Edges | Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review | claim:SF-2026-ARXIV-2606-24204 | complete |
| SF-2026-ARXIV-2606-24245 | RP-3c9362351b5d8c3d | deep | arXiv:2606.24245v1 | SRC-ARXIV@arXiv:2606.24245v1 | https://arxiv.org/html/2606.24245v1 — §3 Overview; 4 Approach; ILP-Guided Predicate Learning | https://arxiv.org/html/2606.24245v1 — §5 Experimental Setup; 6 Evaluation | https://arxiv.org/html/2606.24245v1 — §7 Discussion and Threats to Validity | Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review | claim:SF-2026-ARXIV-2606-24245 | complete |
| SF-2026-ARXIV-2606-24311 | RP-8e0eaf315b509a24 | deep | arXiv:2606.24311v1 | SRC-ARXIV@arXiv:2606.24311v1 | https://arxiv.org/html/2606.24311v1 — §3 Method; 3.2 Integrated Execution Framework; 3.5 Structured Tool Boundary | https://arxiv.org/html/2606.24311v1 — §4 Experiments; Terminal-Bench 2.0/2.1 | https://arxiv.org/html/2606.24311v1 — §5 Limitations and Future Work | Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review | claim:SF-2026-ARXIV-2606-24311 | complete |
| SF-2026-ARXIV-2606-24322 | RP-7cf9dfd62cfb8394 | deep | arXiv:2606.24322v1 | SRC-ARXIV@arXiv:2606.24322v1 | https://arxiv.org/html/2606.24322v1 — §II Threat Model; III TMA-NM; IV Formal Model | https://arxiv.org/html/2606.24322v1 — §V MEM-INV-Bench; VI Evaluation | https://arxiv.org/html/2606.24322v1 — §IX Limitations | Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review | claim:SF-2026-ARXIV-2606-24322 | complete |
| SF-2026-ARXIV-2606-24402 | RP-f20e7bfb923bc526 | deep | arXiv:2606.24402v1 | SRC-ARXIV@arXiv:2606.24402v1 | https://arxiv.org/html/2606.24402v1 — §3 Problem Setting and Study Design; 5 Verification Boundary | https://arxiv.org/html/2606.24402v1 — §4 Poisoning Outcomes; 6 Generalization; 7 Mitigations | https://arxiv.org/html/2606.24402v1 — §8 Discussions and Limitations | Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review | claim:SF-2026-ARXIV-2606-24402 | complete |
| SF-2026-ARXIV-2606-24408 | RP-52a4c4db2e1f86ab | deep | arXiv:2606.24408v1 | SRC-ARXIV@arXiv:2606.24408v1 | https://arxiv.org/html/2606.24408v1 — §3 Natural Identifiers; 4 DP Auditing; 5 Dataset Inference | https://arxiv.org/html/2606.24408v1 — §H DP-SGD Auditing; I/J/K Additional Evaluation | https://arxiv.org/html/2606.24408v1 — §M Limitations | Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review | claim:SF-2026-ARXIV-2606-24408 | complete |
| SF-2026-ARXIV-2606-24428 | RP-f6189931d005927e | deep | arXiv:2606.24428v1 | SRC-ARXIV@arXiv:2606.24428v1 | https://arxiv.org/html/2606.24428v1 — §3 Self-Confirmation Trap; 4 Execute-Distill-Verify | https://arxiv.org/html/2606.24428v1 — §5 Experiments; Memory Quality and Contamination | https://arxiv.org/html/2606.24428v1 — §G Limitations | Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review | claim:SF-2026-ARXIV-2606-24428 | complete |
| SF-2026-ARXIV-2606-24437 | RP-a9bfbcedbccb4152 | deep | arXiv:2606.24437v1 | SRC-ARXIV@arXiv:2606.24437v1 | https://arxiv.org/html/2606.24437v1 — §4 ReM-MoA; Ranked Reasoning Memory; Diversified Routing | https://arxiv.org/html/2606.24437v1 — §5 Experiments; Scaling and Ablations | https://arxiv.org/html/2606.24437v1 — §Bounded width; Single-scale proposer pool; Reviewer overhead | Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review | claim:SF-2026-ARXIV-2606-24437 | complete |
| SF-2026-ARXIV-2606-24467 | RP-6f9163725ede43d3 | deep | arXiv:2606.24467v1 | SRC-ARXIV@arXiv:2606.24467v1 | https://arxiv.org/html/2606.24467v1 — §3 CompressKV; Retrieval Head Identification; Layer-Adaptive Allocation | https://arxiv.org/html/2606.24467v1 — §4 Experiments; LongBench/NIAH; Memory and Latency | https://arxiv.org/html/2606.24467v1 — §4.5 Ablations; 4.6 Orthogonality tests | Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review | claim:SF-2026-ARXIV-2606-24467 | complete |
| SF-2026-ARXIV-2606-24506 | RP-3c12d832120bfaed | deep | arXiv:2606.24506v1 | SRC-ARXIV@arXiv:2606.24506v1 | https://arxiv.org/html/2606.24506v1 — §3 CrossPool Design; KV Planner; Layer-wise Scheduler; Control Lowering | https://arxiv.org/html/2606.24506v1 — §5 Experiments; Context Scalability; Overall Performance | https://arxiv.org/html/2606.24506v1 — §6 Discussion | Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review | claim:SF-2026-ARXIV-2606-24506 | complete |
| SF-2026-ARXIV-2606-24535 | RP-308b1a221a16d9bc | deep | arXiv:2606.24535v1 | SRC-ARXIV@arXiv:2606.24535v1 | https://arxiv.org/html/2606.24535v1 — §3 Fleet-Memory Problem; 5 Governed Shared Memory Architecture | https://arxiv.org/html/2606.24535v1 — §7 Evaluation Methodology; 8 Results | https://arxiv.org/html/2606.24535v1 — §10 Limitations | Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review | claim:SF-2026-ARXIV-2606-24535 | complete |
| SF-2026-ARXIV-2606-24551 | RP-90460108b17b82a9 | deep | arXiv:2606.24551v1 | SRC-ARXIV@arXiv:2606.24551v1 | arXiv:2606.24551v1 — §3.2 Benchmark Construction; §A.3 Visual Design Example | arXiv:2606.24551v1 — §3 Benchmark; §3.1 Benchmark Scope and Composition; §3.2 Benchmark Construction | arXiv:2606.24551v1 — §3.1 Benchmark Scope and Composition; §UI Navigation and Control Discovery Failure.; §Workflow Execution Failure. | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-24551 | complete |
| SF-2026-ARXIV-2606-24598 | RP-6019e440e5a10fcb | deep | arXiv:2606.24598v1 | SRC-ARXIV@arXiv:2606.24598v1 | arXiv:2606.24598v1 §3 Migration Method; §4 Architecture; §7 Convertibility Taxonomy | arXiv:2606.24598v1 §5 WeChat Case Study; §6 Evaluation | arXiv:2606.24598v1 §9 Discussion and Threats to Validity; abstract explicitly limits evidence to one case and readiness, not validated self-learning | Not Disclosed — no later artifact used | claim:SF-2026-ARXIV-2606-24598 | complete |
| SF-2026-ARXIV-2606-24626 | RP-bbbbfabeb673af1c | deep | arXiv:2606.24626v1 | SRC-ARXIV@arXiv:2606.24626v1 | https://arxiv.org/html/2606.24626v1 — §2 Methodology: SAFARI | https://arxiv.org/html/2606.24626v1 — §3 Experimental Setup; 4 Results; A/B/C appendices | https://arxiv.org/html/2606.24626v1 — §D Future Work | Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review | claim:SF-2026-ARXIV-2606-24626 | complete |
| SF-2026-ARXIV-2606-24722 | RP-15717b98c4d8d080 | deep | arXiv:2606.24722v1 | SRC-ARXIV@arXiv:2606.24722v1 | https://arxiv.org/html/2606.24722v1 — §2 Protocol; Block-Local Diffusion Objective; Decentralized Execution | https://arxiv.org/html/2606.24722v1 — §3 Real-Text Experiments; 4 Decentralization and Asynchrony | https://arxiv.org/html/2606.24722v1 — §4.4 HTTP/TCP Transport Proof; 6 Conclusion | Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review | claim:SF-2026-ARXIV-2606-24722 | complete |
| SF-2026-ARXIV-2606-24774 | RP-97cc9d655a334c4e | deep | arXiv:2606.24774v1 | SRC-ARXIV@arXiv:2606.24774v1 | https://arxiv.org/html/2606.24774v1 — §GradAudit gradient-slice and noise-masking methodology | https://arxiv.org/html/2606.24774v1 — §Seven pretraining/fine-tuning configurations; medical and general datasets | https://arxiv.org/html/2606.24774v1 — §White-box parameter-access scope and reference-data dependence | Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review | claim:SF-2026-ARXIV-2606-24774 | complete |
| SF-2026-ARXIV-2606-24775 | RP-e69945f8efd9568b | deep | arXiv:2606.24775v1 | SRC-ARXIV@arXiv:2606.24775v1 | https://arxiv.org/html/2606.24775v1 — §3 Method Overview; Representation, Extraction, Retrieval, Maintenance | https://arxiv.org/html/2606.24775v1 — §4 End-to-End Assessment; 5 Component Comparison | https://arxiv.org/html/2606.24775v1 — §4.3 Evolution Robustness; 4.4 Long-Horizon Stability; 4.5 Cost | Not Disclosed — exact-v1 does not disclose a repository or release artifact used by this review | claim:SF-2026-ARXIV-2606-24775 | complete |

### Source Reviews

<!-- review:SF-2026-ARXIV-2606-23740:start -->
### 2606.23740 — Weight-Space Geometry of Offline Reasoning Training

**问题、旧方案与约束变化。** 工作负载是 `offline reasoning training weight-space geometry`。旧方案在状态规模、权限范围或评估成本稳定时合理；该 family 暴露的新压力是：offline reasoning training 的方法差异要同时看 weight-space trajectory、data/step/LR matching 与功能结果；几何分离若训练预算不匹配不能归因于 objective。

**机制、状态所有权与实现。** Method=`arXiv:2606.23740v1 §2 Experimental Setup`。唯一 owner 为 `TRAIN-RLHF`；控制流只能把 proposal 交给该 owner，数据流必须保留请求、版本、阈值或环境身份，不能由模型输出静默覆盖。

**Evaluation contract。** Qwen3-4B-Instruct-2507、attention LoRA rank32/alpha64、BF16、1500 steps 对比训练轨迹。 model=`Qwen3-4B-Instruct-2507`；hardware=`Not Disclosed`；precision=`BF16; attention LoRA rank 32 alpha 64`；input=`Not Disclosed`；output=`Not Disclosed`；batch=`32; 1,500 steps`；concurrency=`Not Disclosed`；SLO=`Not Disclosed`；evaluator=`weight-space distance, representation and reasoning accuracy`。Evaluation=`arXiv:2606.23740v1 §3 Results`。

**证明边界、trade-off、failure 与共存。** 单 seed/domain/checkpoint，且 DPO 用 10× smaller LR 与 40× fewer rows，构成强 confound；不能形成 objective superiority 结论。 只吸收最小、可迁移的机制 delta；旧路径在证据条件不满足时继续成立。 Limit/counterevidence=`arXiv:2606.23740v1 §4 Discussion; Limitations`；artifact=`Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review`。

<!-- claim:SF-2026-ARXIV-2606-23740:start -->
Claim boundary：只使用 `arXiv:2606.23740v1` 及明确绑定该 v1 的 fallback；普通 pending locator count=`0`。
<!-- claim:SF-2026-ARXIV-2606-23740:end -->
<!-- review:SF-2026-ARXIV-2606-23740:end -->

<!-- review:SF-2026-ARXIV-2606-23743:start -->
### 2606.23743 — Sol Video Inference Engine: Agent-Native Full-Stack Acceleration Framework for Efficient Video Generation

**问题、旧方案与约束变化。** 工作负载是 `full-stack video-generation inference`。旧方案在状态规模、权限范围或评估成本稳定时合理；该 family 暴露的新压力是：video inference optimization 应把 graph transformation、kernel/execution plan、memory schedule 与 serving config 绑定同一可重建 artifact；agent 只能提出/搜索 plan，validator 才能提交。

**机制、状态所有权与实现。** Method=`arXiv:2606.23743v1 §3 Sol Architecture; §4 Agent-Native Optimization`。唯一 owner 为 `INFER-TENSORRT-LLM`；控制流只能把 proposal 交给该 owner，数据流必须保留请求、版本、阈值或环境身份，不能由模型输出静默覆盖。

**Evaluation contract。** 三个 video-generation models 的作者配置报告超过 2× acceleration，并检查自动 plan。 model=`three video-generation models named in exact-v1`；hardware=`Not Disclosed`；precision=`Not Disclosed`；input=`Not Disclosed`；output=`Not Disclosed`；batch=`Not Disclosed`；concurrency=`Not Disclosed`；SLO=`author-reported latency/throughput configuration`；evaluator=`latency, throughput, memory and generation quality`。Evaluation=`arXiv:2606.23743v1 §5 Experiments`。

**证明边界、trade-off、failure 与共存。** 收益 instance-specific 于模型、硬件和 serving config，最终 visual quality 仍需人评；不能把单次搜索结果外推通用 engine。 只吸收最小、可迁移的机制 delta；旧路径在证据条件不满足时继续成立。 Limit/counterevidence=`arXiv:2606.23743v1 §6 Limitations and Future Work`；artifact=`Not Disclosed — exact-v1 manuscript does not name a separate artifact used for this review`。

<!-- claim:SF-2026-ARXIV-2606-23743:start -->
Claim boundary：只使用 `arXiv:2606.23743v1` 及明确绑定该 v1 的 fallback；普通 pending locator count=`0`。
<!-- claim:SF-2026-ARXIV-2606-23743:end -->
<!-- review:SF-2026-ARXIV-2606-23743:end -->

<!-- review:SF-2026-ARXIV-2606-23752:start -->
### 2606.23752 — ESAA-Conversational: An Event-Sourced Memory Layer for Continuity, Handoff, and Curation Across Heterogeneous LLM Coding Agents

**问题与旧路径。** Each agent, however, persists its conversation in a private and vendor-specific log. 旧路径在输入分布、信任边界和预算稳定时仍合理。

**机制与 state/data/control owner。** ESAA-Conversational: An Event-Sourced Memory Layer for Continuity, Handoff, and Curation Across Heterogeneous LLM Coding Agents 的 exact-v1 机制为：Each agent, however, persists its conversation in a private and vendor-specific log. 因此 把事件时间、来源、有效条件、版本、检索决策与写入 authority 分开。 唯一 owner 为 `AGENT-MEMORY`；相邻章只消费带 identity/version/failure/fallback 的 handoff。

**Evaluation：proof / non-proof。** Method=`arXiv:2606.23752v1 — §ESAA-Conversational: An Event-Sourced Memory Layer for Continuity, Handoff, and Curation Across Heterogeneous LLM Coding Agents; §2.2 Agent Memory; §4 Architecture`；Evaluation=`arXiv:2606.23752v1 — §8 Self-Referential Case Study`；counterevidence=`arXiv:2606.23752v1 — §9 Discussion; §Validation Scope; §10 Future Work`。这些证据不证明未测试规模、分布、攻击者或生产 SLO。

**Trade-off / failure / coexistence / evolution。** 该 family 的 failure pressure 是：Each agent, however, persists its conversation in a private and vendor-specific log. 披露的 evaluation signal 是：The result is conversational state drift: goals, decisions, open tasks, and rationales established with one agent are not reliably available when another agent takes over. 证据只支持 exact-v1 在披露 workload/model/hardware 范围内的机制与结果，不证明生产尾部、未测分布或形式安全；来源/时间/版本不足时隔离 candidate memory，保留原始轨迹且禁止自动覆盖。旧路径在其原约束成立时继续共存。

<!-- claim:SF-2026-ARXIV-2606-23752:start -->
Primary identity `arXiv:2606.23752v1`; official exact-v1 HTML; ordinary pending=0.
<!-- claim:SF-2026-ARXIV-2606-23752:end -->
<!-- review:SF-2026-ARXIV-2606-23752:end -->

<!-- review:SF-2026-ARXIV-2606-23754:start -->
### 2606.23754 — Verifiable Foundation Models for Robot Safety

**问题与旧路径。** Deploying foundation models for robot control raises a central challenge: the expressive power that enables rich, multimodal perception also makes these models opaque and difficult to analyze formally, rendering them intractable for existing verification tools. 旧路径在输入分布、信任边界和预算稳定时仍合理。

**机制与 state/data/control owner。** Verifiable Foundation Models for Robot Safety 的 exact-v1 机制为：In this paper, we present FEARL (Foundation-Enabled Assured Robot Learning), a framework that addresses this tension through a modular architectural decomposition. 因此 把 observation、temporal state、action head、safety gate 与真实动作回执绑定。 唯一 owner 为 `MULTIMODAL-EMBODIED-VLA`；相邻章只消费带 identity/version/failure/fallback 的 handoff。

**Evaluation：proof / non-proof。** Method=`arXiv:2606.23754v1 — §3 The FEARL Architecture; §4 Enabling Verification via Decomposition; §4.1 Theoretical Guarantees`；Evaluation=`arXiv:2606.23754v1 — §5 Experiments; §5.1 Experimental Setup; §5.3 Does the Decomposition Enable Verification?`；counterevidence=`arXiv:2606.23754v1 — §6 Discussion and Conclusion; §A Proof of Propositions`。这些证据不证明未测试规模、分布、攻击者或生产 SLO。

**Trade-off / failure / coexistence / evolution。** 该 family 的 failure pressure 是：Deploying foundation models for robot control raises a central challenge: the expressive power that enables rich, multimodal perception also makes these models opaque and difficult to analyze formally, rendering them intractable for existing verification tools. 披露的 evaluation signal 是：To show that the decomposed policy remains capable of solving diverse tasks, we evaluate FEARL on three simulated robotic domains using multiple Controller backbones and training procedures, including pretrained off-the-shelf vision-language-action models. 证据只支持 exact-v1 在披露 workload/model/hardware 范围内的机制与结果，不证明生产尾部、未测分布或形式安全；观测或动作接口不一致时拒绝物理提交并交回保守 controller/人工。旧路径在其原约束成立时继续共存。

<!-- claim:SF-2026-ARXIV-2606-23754:start -->
Primary identity `arXiv:2606.23754v1`; official exact-v1 HTML; ordinary pending=0.
<!-- claim:SF-2026-ARXIV-2606-23754:end -->
<!-- review:SF-2026-ARXIV-2606-23754:end -->

<!-- review:SF-2026-ARXIV-2606-23768:start -->
### 2606.23768 — Cryptographic certificates of validity for trustworthy AI

**问题与旧路径。** We propose cryptographic certificates of validity for agentic AI systems. 旧路径在输入分布、信任边界和预算稳定时仍合理。

**机制与 state/data/control owner。** Cryptographic certificates of validity for trustworthy AI 的 exact-v1 机制为：We propose cryptographic certificates of validity for agentic AI systems. 因此 把 attacker、policy、runtime data/control flow、proof boundary 与 fail-closed handoff 显式化。 唯一 owner 为 `PLATFORM-SECURITY`；相邻章只消费带 identity/version/failure/fallback 的 handoff。

**Evaluation：proof / non-proof。** Method=`arXiv:2606.23768v1 — §2 A compact slice of maths; §4 How to apply this mathematics to AI agents`；Evaluation=`arXiv:2606.23768v1 — §3 Examples; §3.2 A recursive example`；counterevidence=`arXiv:2606.23768v1 — §5 Related work; §6 Conclusions`。这些证据不证明未测试规模、分布、攻击者或生产 SLO。

**Trade-off / failure / coexistence / evolution。** 该 family 的 failure pressure 是：We propose cryptographic certificates of validity for agentic AI systems. 披露的 evaluation signal 是：We outline the approach at a high level, give the core mathematical translation, relate the proposal to proof-carrying code, zkVMs, formal methods, and agent governance, and note the specification, auditing, and deployment questions that a full implementation must answer. 证据只支持 exact-v1 在披露 workload/model/hardware 范围内的机制与结果，不证明生产尾部、未测分布或形式安全；证据、policy 或证明前提不满足时 fail closed 并交回独立 reference monitor。旧路径在其原约束成立时继续共存。

<!-- claim:SF-2026-ARXIV-2606-23768:start -->
Primary identity `arXiv:2606.23768v1`; official exact-v1 HTML; ordinary pending=0.
<!-- claim:SF-2026-ARXIV-2606-23768:end -->
<!-- review:SF-2026-ARXIV-2606-23768:end -->

<!-- review:SF-2026-ARXIV-2606-23797:start -->
### 2606.23797 — From Task-Guided Conversational Graphs to Goal-Oriented Dialogue Runtimes

**问题与旧路径。** Graph and multi-agent orchestration frameworks make production large language model (LLM) workflows practical, but they do not by themselves solve conversational continuity when users maintain several interdependent objectives. 旧路径在输入分布、信任边界和预算稳定时仍合理。

**机制与 state/data/control owner。** From Task-Guided Conversational Graphs to Goal-Oriented Dialogue Runtimes 的 exact-v1 机制为：We introduce the Goal-Oriented Dialogue Runtime (GODR), a framework-neutral design pattern that treats goals, task frames, lifecycle state, invalidation rules, and resumption contracts as first-class runtime objects while delegating bounded execution to graph runtimes, agents, tools, or application programming interfaces (APIs). 因此 把执行边、依赖边、checkpoint 与 compensation 作为可重放 control state。 唯一 owner 为 `AGENT-WORKFLOW`；相邻章只消费带 identity/version/failure/fallback 的 handoff。

**Evaluation：proof / non-proof。** Method=`arXiv:2606.23797v1 — §9.5 Turn-Level Algorithm; §10 Design Principles; §11 Evaluation Protocol`；Evaluation=`arXiv:2606.23797v1 — §11 Evaluation Protocol`；counterevidence=`arXiv:2606.23797v1 — §15 Contributions, Scope, and Validity; §16 Conclusion`。这些证据不证明未测试规模、分布、攻击者或生产 SLO。

**Trade-off / failure / coexistence / evolution。** 该 family 的 failure pressure 是：Graph and multi-agent orchestration frameworks make production large language model (LLM) workflows practical, but they do not by themselves solve conversational continuity when users maintain several interdependent objectives. 披露的 evaluation signal 是：The paper formalizes the problem, proposes runtime objects and architecture-selection criteria, and frames evaluation as an agenda for future empirical validation rather than as a measured performance claim. 证据只支持 exact-v1 在披露 workload/model/hardware 范围内的机制与结果，不证明生产尾部、未测分布或形式安全；前提、identity 或预算越界时停止新路径，回退到该 owner 已验证的旧路径并保留失败回执。旧路径在其原约束成立时继续共存。

<!-- claim:SF-2026-ARXIV-2606-23797:start -->
Primary identity `arXiv:2606.23797v1`; official exact-v1 HTML; ordinary pending=0.
<!-- claim:SF-2026-ARXIV-2606-23797:end -->
<!-- review:SF-2026-ARXIV-2606-23797:end -->

<!-- review:SF-2026-ARXIV-2606-23858:start -->
### 2606.23858 — Are Safety Guarantees in Neural Networks Safe? How to Compute Trustworthy Robustness Certifications

**问题与旧路径。** A primary challenge in AI safety is the existence of adversarial examples -- slightly distorted inputs that cause a neural network (NN) to misclassify. 旧路径在输入分布、信任边界和预算稳定时仍合理。

**机制与 state/data/control owner。** Are Safety Guarantees in Neural Networks Safe? How to Compute Trustworthy Robustness Certifications 的 exact-v1 机制为：We introduce the apothem measure and show how to compute apothem-optimal certifications in a linear number of calls to a NN verifier (oracle) w.r.t. 因此 把 attacker、policy、runtime data/control flow、proof boundary 与 fail-closed handoff 显式化。 唯一 owner 为 `PLATFORM-SECURITY`；相邻章只消费带 identity/version/failure/fallback 的 handoff。

**Evaluation：proof / non-proof。** Method=`arXiv:2606.23858v1 — §3 Robustness Operators; §4 Algorithms; §4.2 Refine & Check Algorithm`；Evaluation=`arXiv:2606.23858v1 — §5 Implementation; §Experimental Setup.; §Experimental Results.`；counterevidence=`arXiv:2606.23858v1 — §4.3 The Complexity of Apothem Optimality; §4.4 The Intractability of Volume Optimality; §7 Conclusions`。这些证据不证明未测试规模、分布、攻击者或生产 SLO。

**Trade-off / failure / coexistence / evolution。** 该 family 的 failure pressure 是：A primary challenge in AI safety is the existence of adversarial examples -- slightly distorted inputs that cause a neural network (NN) to misclassify. 披露的 evaluation signal 是：Most existing approaches focus on maximizing the certification's volume, but recent intractability results prohibit the computation of volume-optimal certifications in reasonable time. 证据只支持 exact-v1 在披露 workload/model/hardware 范围内的机制与结果，不证明生产尾部、未测分布或形式安全；证据、policy 或证明前提不满足时 fail closed 并交回独立 reference monitor。旧路径在其原约束成立时继续共存。

<!-- claim:SF-2026-ARXIV-2606-23858:start -->
Primary identity `arXiv:2606.23858v1`; official exact-v1 HTML; ordinary pending=0.
<!-- claim:SF-2026-ARXIV-2606-23858:end -->
<!-- review:SF-2026-ARXIV-2606-23858:end -->

<!-- review:SF-2026-ARXIV-2606-23872:start -->
### 2606.23872 — MGI: Member vs Generated Inference

**问题与旧路径。** We formalize this challenge as Member vs Generated Inference (MGI): given a sample and a target generative model, infer whether the sample is a true training member or a generated output of that model. 旧路径在输入分布、信任边界和预算稳定时仍合理。

**机制与 state/data/control owner。** MGI: Member vs Generated Inference 的 exact-v1 机制为：To address MGI, we propose Data Circuit Breaker (DCB), a three-stage method that combines complementary signals from a generative model's autoencoder and latent generator to distinguish training members from generated samples. 因此 把 attacker、policy、runtime data/control flow、proof boundary 与 fail-closed handoff 显式化。 唯一 owner 为 `PLATFORM-SECURITY`；相邻章只消费带 identity/version/failure/fallback 的 handoff。

**Evaluation：proof / non-proof。** Method=`arXiv:2606.23872v1 — §3 Member vs Generated Inference; §5 Proposed Data Circuit Breaker; §5.3 Attribution Protocol`；Evaluation=`arXiv:2606.23872v1 — §6 Empirical Evaluation; §6.1 Experimental Setup; §6.2 Evaluation on the Direct Training Setting`；counterevidence=`arXiv:2606.23872v1 — §4 Limitations of MIA and Attribution Methods; §4.1 CPD-based Methods Fall Short for MGI; §7 Conclusions`。这些证据不证明未测试规模、分布、攻击者或生产 SLO。

**Trade-off / failure / coexistence / evolution。** 该 family 的 failure pressure 是：We formalize this challenge as Member vs Generated Inference (MGI): given a sample and a target generative model, infer whether the sample is a true training member or a generated output of that model. 披露的 evaluation signal 是：Focusing on image generation, we show that existing membership inference methods systematically misclassify generated samples as training members, while attribution-based methods often misclassify true members as generated. 证据只支持 exact-v1 在披露 workload/model/hardware 范围内的机制与结果，不证明生产尾部、未测分布或形式安全；证据、policy 或证明前提不满足时 fail closed 并交回独立 reference monitor。旧路径在其原约束成立时继续共存。

<!-- claim:SF-2026-ARXIV-2606-23872:start -->
Primary identity `arXiv:2606.23872v1`; official exact-v1 HTML; ordinary pending=0.
<!-- claim:SF-2026-ARXIV-2606-23872:end -->
<!-- review:SF-2026-ARXIV-2606-23872:end -->

<!-- review:SF-2026-ARXIV-2606-23892:start -->
### 2606.23892 — REALM: A Unified Red-Teaming Benchmark for Physical-World VLMs

**问题与旧路径。** Although many red-teaming methods have been developed to probe VLM vulnerabilities, their evaluation remains fragmented across datasets, metrics, and threat models, making direct comparison difficult and obscuring whether observed differences arise from stronger attacks, more vulnerable models, or incompatible evaluation settings. 旧路径在输入分布、信任边界和预算稳定时仍合理。

**机制与 state/data/control owner。** REALM: A Unified Red-Teaming Benchmark for Physical-World VLMs 的 exact-v1 机制为：We introduce REALM, to our knowledge the first unified red-teaming benchmark for physical-world VLMs. 因此 把 attacker、policy、runtime data/control flow、proof boundary 与 fail-closed handoff 显式化。 唯一 owner 为 `PLATFORM-SECURITY`；相邻章只消费带 identity/version/failure/fallback 的 handoff。

**Evaluation：proof / non-proof。** Method=`arXiv:2606.23892v1 — §Black-box threat model.; §Appendix D Attack Method Details; §Appendix E Defense Method Details`；Evaluation=`arXiv:2606.23892v1 — §ReaLM : A Unified Red-Teaming Benchmark for Physical-World VLMs; §2.2 Red-Teaming Benchmark; §3 ReaLM : Benchmark for Physical-World VLMs`；counterevidence=`arXiv:2606.23892v1 — §6 Conclusion`。这些证据不证明未测试规模、分布、攻击者或生产 SLO。

**Trade-off / failure / coexistence / evolution。** 该 family 的 failure pressure 是：Although many red-teaming methods have been developed to probe VLM vulnerabilities, their evaluation remains fragmented across datasets, metrics, and threat models, making direct comparison difficult and obscuring whether observed differences arise from stronger attacks, more vulnerable models, or incompatible evaluation settings. 披露的 evaluation signal 是：Although many red-teaming methods have been developed to probe VLM vulnerabilities, their evaluation remains fragmented across datasets, metrics, and threat models, making direct comparison difficult and obscuring whether observed differences arise from stronger attacks, more vulnerable models, or incompatible evaluation settings. 证据只支持 exact-v1 在披露 workload/model/hardware 范围内的机制与结果，不证明生产尾部、未测分布或形式安全；证据、policy 或证明前提不满足时 fail closed 并交回独立 reference monitor。旧路径在其原约束成立时继续共存。

<!-- claim:SF-2026-ARXIV-2606-23892:start -->
Primary identity `arXiv:2606.23892v1`; official exact-v1 HTML; ordinary pending=0.
<!-- claim:SF-2026-ARXIV-2606-23892:end -->
<!-- review:SF-2026-ARXIV-2606-23892:end -->

<!-- review:SF-2026-ARXIV-2606-23915:start -->
### 2606.23915 — Do LLM Attribution Metrics Transfer? Auditing Retrieval-Augmented Generation Evaluation Across Datasets and Constructs

**问题与旧路径。** This instability has a concrete decision cost: a naive "best-on-average" rule for choosing an evaluator fails leave-one-dataset-out (mean held-out regret 0.172 AUROC, worse than fixing one scorer), so metric choice must be validated on the target dataset rather than learned from others. 旧路径在输入分布、信任边界和预算稳定时仍合理。

**机制与 state/data/control owner。** Do LLM Attribution Metrics Transfer? Auditing Retrieval-Augmented Generation Evaluation Across Datasets and Constructs 的 exact-v1 机制为：We audit eight automatic scorers -- lexical, embedding, and BERTScore baselines alongside entailment/grounding-trained models (clean and FEVER NLI, the checker MiniCheck) -- across three evaluation constructs (provenance/topicality, generated-answer attribution, and fact-check entailment), asking whether any scorer transfers: stays within the 95% confidence interval of the best audited scorer on every dataset of a multi-dataset construct. 因此 把样本、metric、judge、阈值、不确定性和 release authority 分离。 唯一 owner 为 `PLATFORM-EVALUATION-SYSTEM`；相邻章只消费带 identity/version/failure/fallback 的 handoff。

**Evaluation：proof / non-proof。** Method=`arXiv:2606.23915v1 — §3 A Sentence-Unit Provenance-Ranking Score; §3.1 Provenance/topicality`；Evaluation=`arXiv:2606.23915v1 — §4 The Cross-Dataset Audit; §5 ERCR as a Boundary Probe; §F Independent Replication and Robustness`；counterevidence=`arXiv:2606.23915v1 — §An external boundary: long-form alone does not predict the NLI failure.; §7 Limitations`。这些证据不证明未测试规模、分布、攻击者或生产 SLO。

**Trade-off / failure / coexistence / evolution。** 该 family 的 failure pressure 是：This instability has a concrete decision cost: a naive "best-on-average" rule for choosing an evaluator fails leave-one-dataset-out (mean held-out regret 0.172 AUROC, worse than fixing one scorer), so metric choice must be validated on the target dataset rather than learned from others. 披露的 evaluation signal 是：We audit eight automatic scorers -- lexical, embedding, and BERTScore baselines alongside entailment/grounding-trained models (clean and FEVER NLI, the checker MiniCheck) -- across three evaluation constructs (provenance/topicality, generated-answer attribution, and fact-check entailment), asking whether any scorer transfers: stays within the 95% confidence interval of the best audited scorer on every dataset of a multi-dataset construct. 证据只支持 exact-v1 在披露 workload/model/hardware 范围内的机制与结果，不证明生产尾部、未测分布或形式安全；metric、judge 或样本假设失效时保持 release Gate Open 并恢复完整评估。旧路径在其原约束成立时继续共存。

<!-- claim:SF-2026-ARXIV-2606-23915:start -->
Primary identity `arXiv:2606.23915v1`; official exact-v1 HTML; ordinary pending=0.
<!-- claim:SF-2026-ARXIV-2606-23915:end -->
<!-- review:SF-2026-ARXIV-2606-23915:end -->

<!-- review:SF-2026-ARXIV-2606-23927:start -->
### 2606.23927 — RIFT-Bench: Dynamic Red-teaming For Agentic AI Systems

**问题与旧路径。** Agentic AI systems powered by large language models (LLMs) are rapidly evolving into autonomous decision-making systems, exposing attack vectors beyond those of traditional LLM vulnerabilities. 旧路径在输入分布、信任边界和预算稳定时仍合理。

**机制与 state/data/control owner。** RIFT-Bench: Dynamic Red-teaming For Agentic AI Systems 的 exact-v1 机制为：To address this gap, we introduce RIFT-Bench, a graph representation-driven methodology for dynamic red-teaming that enables unified evaluations across diverse agentic architectures. 因此 把 attacker、policy、runtime data/control flow、proof boundary 与 fail-closed handoff 显式化。 唯一 owner 为 `PLATFORM-SECURITY`；相邻章只消费带 identity/version/failure/fallback 的 handoff。

**Evaluation：proof / non-proof。** Method=`arXiv:2606.23927v1 — §4 NodeSpec: System Representation; §6 RIFT-Bench Framework; §F.2 Framework and Architecture Matrix`；Evaluation=`arXiv:2606.23927v1 — §7.1 Structure Identifier Evaluation; §Appendix A Additional Comparison to Agentic Security Evaluation; §E.3 Evaluation Metrics`；counterevidence=`arXiv:2606.23927v1 — §8 Discussion`。这些证据不证明未测试规模、分布、攻击者或生产 SLO。

**Trade-off / failure / coexistence / evolution。** 该 family 的 failure pressure 是：Agentic AI systems powered by large language models (LLMs) are rapidly evolving into autonomous decision-making systems, exposing attack vectors beyond those of traditional LLM vulnerabilities. 披露的 evaluation signal 是：Existing security evaluations are often tied to specific implementations or domains, limiting unified comparison across heterogeneous systems. 证据只支持 exact-v1 在披露 workload/model/hardware 范围内的机制与结果，不证明生产尾部、未测分布或形式安全；证据、policy 或证明前提不满足时 fail closed 并交回独立 reference monitor。旧路径在其原约束成立时继续共存。

<!-- claim:SF-2026-ARXIV-2606-23927:start -->
Primary identity `arXiv:2606.23927v1`; official exact-v1 HTML; ordinary pending=0.
<!-- claim:SF-2026-ARXIV-2606-23927:end -->
<!-- review:SF-2026-ARXIV-2606-23927:end -->

<!-- review:SF-2026-ARXIV-2606-23937:start -->
### 2606.23937 — When Retrieval Metrics Mislead: Measuring Policy Signal in Long-Horizon Tool-Use Agents

**问题与旧路径。** Although the exact governing clause is retrieved at rank 1 for only 7% of airline states, the primary 3B classifier obtains macro-F1 0.58 with retrieved clauses versus 0.60 with gold clauses (Delta=-0.02, task-cluster 95% CI [-0.23,+0.21]); mismatched-policy and no-policy controls score 0.32 and 0.21. 旧路径在输入分布、信任边界和预算稳定时仍合理。

**机制与 state/data/control owner。** When Retrieval Metrics Mislead: Measuring Policy Signal in Long-Horizon Tool-Use Agents 的 exact-v1 机制为：We test this proxy for pre-action policy classification in tau-bench using Qwen2.5-3B/7B classifiers. 因此 把样本、metric、judge、阈值、不确定性和 release authority 分离。 唯一 owner 为 `PLATFORM-EVALUATION-SYSTEM`；相邻章只消费带 identity/version/failure/fallback 的 handoff。

**Evaluation：proof / non-proof。** Method=`arXiv:2606.23937v1 — §Sensitivity to domain and query construction.`；Evaluation=`arXiv:2606.23937v1 — §Decision models and evaluation.; §Analysis of informative nonmatching clauses.; §B.1 Primary 3B result`；counterevidence=`arXiv:2606.23937v1 — §Contribution and scope.; §Construct scope.; §7 Conclusion`。这些证据不证明未测试规模、分布、攻击者或生产 SLO。

**Trade-off / failure / coexistence / evolution。** 该 family 的 failure pressure 是：Although the exact governing clause is retrieved at rank 1 for only 7% of airline states, the primary 3B classifier obtains macro-F1 0.58 with retrieved clauses versus 0.60 with gold clauses (Delta=-0.02, task-cluster 95% CI [-0.23,+0.21]); mismatched-policy and no-policy controls score 0.32 and 0.21. 披露的 evaluation signal 是：Under gold-policy conditioning, a compact structured state improves macro-F1 over raw trajectories by 0.13-0.17 after tuning. 证据只支持 exact-v1 在披露 workload/model/hardware 范围内的机制与结果，不证明生产尾部、未测分布或形式安全；metric、judge 或样本假设失效时保持 release Gate Open 并恢复完整评估。旧路径在其原约束成立时继续共存。

<!-- claim:SF-2026-ARXIV-2606-23937:start -->
Primary identity `arXiv:2606.23937v1`; official exact-v1 HTML; ordinary pending=0.
<!-- claim:SF-2026-ARXIV-2606-23937:end -->
<!-- review:SF-2026-ARXIV-2606-23937:end -->

<!-- review:SF-2026-ARXIV-2606-23961:start -->
### 2606.23961 — Forget Without Compromise: Nexus Sampling for Streaming KV-Cache Eviction Under Fixed Budgets

**问题与旧路径。** To address this challenge, we propose Nexus Sampling, a training-free eviction method that pairs Nexus scoring, an iterative walk over direct attention that surfaces bridge tokens, with weighted reservoir sampling, which retains tokens with inclusion probability in place of deterministic top-$K$. 旧路径在输入分布、信任边界和预算稳定时仍合理。

**机制与 state/data/control owner。** Forget Without Compromise: Nexus Sampling for Streaming KV-Cache Eviction Under Fixed Budgets 的 exact-v1 机制为：To address this challenge, we propose Nexus Sampling, a training-free eviction method that pairs Nexus scoring, an iterative walk over direct attention that surfaces bridge tokens, with weighted reservoir sampling, which retains tokens with inclusion probability in place of deterministic top-$K$. 因此 把 cache position、eviction/quantization policy、跨模态 identity 与 dense recompute fallback 绑定。 唯一 owner 为 `INFER-KV-CACHE`；相邻章只消费带 identity/version/failure/fallback 的 handoff。

**Evaluation：proof / non-proof。** Method=`arXiv:2606.23961v1 — §2 Nexus Sampling; §2.2 Nexus Scoring; §2.3 Weighted Reservoir Block Selection`；Evaluation=`arXiv:2606.23961v1 — §5 Experiments; §5.1 Setup; §5.2–§5.6 Results and Ablations`；counterevidence=`arXiv:2606.23961v1 — §7 Conclusion; §A.5 Eviction Quality Under Approximate Future Utility`。这些证据不证明未测试规模、分布、攻击者或生产 SLO。

**Trade-off / failure / coexistence / evolution。** 该 family 的 failure pressure 是：To address this challenge, we propose Nexus Sampling, a training-free eviction method that pairs Nexus scoring, an iterative walk over direct attention that surfaces bridge tokens, with weighted reservoir sampling, which retains tokens with inclusion probability in place of deterministic top-$K$. 披露的 evaluation signal 是：Theoretically, we show that Nexus Sampling dominates deterministic top-$K$ in long-run survival of subtly important tokens. 证据只支持 exact-v1 在披露 workload/model/hardware 范围内的机制与结果，不证明生产尾部、未测分布或形式安全；cache identity 或误差预算失配时清空该路径并回到未压缩/重算 KV。旧路径在其原约束成立时继续共存。

<!-- claim:SF-2026-ARXIV-2606-23961:start -->
Primary identity `arXiv:2606.23961v1`; official exact-v1 HTML; ordinary pending=0.
<!-- claim:SF-2026-ARXIV-2606-23961:end -->
<!-- review:SF-2026-ARXIV-2606-23961:end -->

<!-- review:SF-2026-ARXIV-2606-23969:start -->
### 2606.23969 — The Serialized Bridge: Understanding and Recovering LLM Serving Performance under Blackwell GPU Confidential Computing

**问题与旧路径。** We find that GPU-CC turns host/device movement into a serialized, high-setup-cost channel. 旧路径在输入分布、信任边界和预算稳定时仍合理。

**机制与 state/data/control owner。** The Serialized Bridge: Understanding and Recovering LLM Serving Performance under Blackwell GPU Confidential Computing 的 exact-v1 机制为：Yet LLM serving under Intel TDX plus GPU-CC still loses 13-27% of throughput, and KV-cache restore latency can more than double. 因此 把 attacker、policy、runtime data/control flow、proof boundary 与 fail-closed handoff 显式化。 唯一 owner 为 `PLATFORM-SECURITY`；相邻章只消费带 identity/version/failure/fallback 的 handoff。

**Evaluation：proof / non-proof。** Method=`arXiv:2606.23969v1 — §3 Platforms and Method; §4.1 Compute and GPU-Local Memory Are at Parity; §5.6 Runtime Design Rule`；Evaluation=`arXiv:2606.23969v1 — §3.3 Experiment Families; §5 Case Study: Policy Inversion in the Serving Runtime; §6 Case Study: Movement Engineering for Loading and KV State`；counterevidence=`arXiv:2606.23969v1 — §3.4 Comparability and Claim Scope; §11 Conclusion`。这些证据不证明未测试规模、分布、攻击者或生产 SLO。

**Trade-off / failure / coexistence / evolution。** 该 family 的 failure pressure 是：We find that GPU-CC turns host/device movement into a serialized, high-setup-cost channel. 披露的 evaluation signal 是：We qualify confidential multi-GPU NVSwitch tenants on B300, including 510 GB/s NVLink P2P inside a CVM and concurrent isolated tenants, and identify the remaining fabric-attestation gap for production confidential AI platforms. 证据只支持 exact-v1 在披露 workload/model/hardware 范围内的机制与结果，不证明生产尾部、未测分布或形式安全；证据、policy 或证明前提不满足时 fail closed 并交回独立 reference monitor。旧路径在其原约束成立时继续共存。

<!-- claim:SF-2026-ARXIV-2606-23969:start -->
Primary identity `arXiv:2606.23969v1`; official exact-v1 HTML; ordinary pending=0.
<!-- claim:SF-2026-ARXIV-2606-23969:end -->
<!-- review:SF-2026-ARXIV-2606-23969:end -->

<!-- review:SF-2026-ARXIV-2606-23983:start -->
### 2606.23983 — Maestro Order: A Model-Agnostic Orchestration Harness

**问题与旧路径。** The harness treats any model as a black-box base solver behind a uniform interface, layers a verifier ensemble whose discrimination is measured online, and allocates verification and voting to the stages with the highest marginal reliability per unit cost. 旧路径在输入分布、信任边界和预算稳定时仍合理。

**机制与 state/data/control owner。** Maestro Order: A Model-Agnostic Orchestration Harness 的 exact-v1 机制为：We present Maestro Order, a model-agnostic orchestration harness that turns unreliable solvers into reliable problem-solving systems by composing them according to four structural primitives (decompose, ensemble, verify, and recurse) and a budget-aware controller that decides where to spend compute. 因此 把模型/工具/资源路由、OS harness、隔离边界与 outcome receipt 作为平台责任。 唯一 owner 为 `AGENT-PLATFORM`；相邻章只消费带 identity/version/failure/fallback 的 handoff。

**Evaluation：proof / non-proof。** Method=`arXiv:2606.23983v1 — §3. From Algebra to Architecture; §4. Harness Architecture; §5. Design Rationale and System Invariants`；Evaluation=`arXiv:2606.23983v1 — §12. Evaluation Methodology; §Simulation study (this paper).`；counterevidence=`arXiv:2606.23983v1 — §15. Discussion: Failure Modes and Guidance; §16. Limitations and Threats to Validity; §17. Conclusion`。这些证据不证明未测试规模、分布、攻击者或生产 SLO。

**Trade-off / failure / coexistence / evolution。** 该 family 的 failure pressure 是：The harness treats any model as a black-box base solver behind a uniform interface, layers a verifier ensemble whose discrimination is measured online, and allocates verification and voting to the stages with the highest marginal reliability per unit cost. 披露的 evaluation signal 是：We then specify an evaluation methodology (reliability at fixed cost, coverage, calibration, and ablations) and report results from a faithful Monte Carlo simulation of the harness over a parameterized solver/verifier model. 证据只支持 exact-v1 在披露 workload/model/hardware 范围内的机制与结果，不证明生产尾部、未测分布或形式安全；前提、identity 或预算越界时停止新路径，回退到该 owner 已验证的旧路径并保留失败回执。旧路径在其原约束成立时继续共存。

<!-- claim:SF-2026-ARXIV-2606-23983:start -->
Primary identity `arXiv:2606.23983v1`; official exact-v1 HTML; ordinary pending=0.
<!-- claim:SF-2026-ARXIV-2606-23983:end -->
<!-- review:SF-2026-ARXIV-2606-23983:end -->

<!-- review:SF-2026-ARXIV-2606-23989:start -->
### 2606.23989 — Faithful by Construction: Claim-Anchored Attribution for Multi-Document Summarization

**问题与旧路径。** End-to-end large language models (LLMs) produce fluent multi-document summaries but remain prone to hallucination, and the attributions they offer are typically coarse (whole documents or passages) and generated post hoc, leaving each summary statement hard to verify. 旧路径在输入分布、信任边界和预算稳定时仍合理。

**机制与 state/data/control owner。** Faithful by Construction: Claim-Anchored Attribution for Multi-Document Summarization 的 exact-v1 机制为：We present CAMS, a Claim-Anchored Multi-document Summarization framework that (i) extracts atomic claims with token-level provenance from every source document, (ii) clusters equivalent claims across documents while flagging inter-source conflicts, (iii) selects a support-aware and salient subset, and (iv) rewrites the selection into a summary in which every sentence is anchored to a support-checked claim that links back to one or more source spans. 因此 把 retrieval 配置、candidate set、证据 identity 与质量—成本评估绑定。 唯一 owner 为 `AGENT-RAG`；相邻章只消费带 identity/version/failure/fallback 的 handoff。

**Evaluation：proof / non-proof。** Method=`arXiv:2606.23989v1 — §Attribution by Construction: Claim-Anchored Evidence for Faithfulness-Oriented Multi-Document Summarization; §3 Method; §Training labels by distant supervision.`；Evaluation=`arXiv:2606.23989v1 — §Faithful summarization and its evaluation.; §4.3 Evaluation Protocol; §5 Results and Analysis`；counterevidence=`arXiv:2606.23989v1 — §6 Conclusion`。这些证据不证明未测试规模、分布、攻击者或生产 SLO。

**Trade-off / failure / coexistence / evolution。** 该 family 的 failure pressure 是：End-to-end large language models (LLMs) produce fluent multi-document summaries but remain prone to hallucination, and the attributions they offer are typically coarse (whole documents or passages) and generated post hoc, leaving each summary statement hard to verify. 披露的 evaluation signal 是：We evaluate quality, faithfulness, and localization on MultiNews, analyze conflict handling on DiverseSumm, and test zero-shot transfer on WCEP, using a two-regime protocol that separates reference-free citation quality from gold-aligned localization accuracy, and we add an evaluator-decoupled audit that tests citation precision with a support model never used for selection or verification. 证据只支持 exact-v1 在披露 workload/model/hardware 范围内的机制与结果，不证明生产尾部、未测分布或形式安全；前提、identity 或预算越界时停止新路径，回退到该 owner 已验证的旧路径并保留失败回执。旧路径在其原约束成立时继续共存。

<!-- claim:SF-2026-ARXIV-2606-23989:start -->
Primary identity `arXiv:2606.23989v1`; official exact-v1 HTML; ordinary pending=0.
<!-- claim:SF-2026-ARXIV-2606-23989:end -->
<!-- review:SF-2026-ARXIV-2606-23989:end -->

<!-- review:SF-2026-ARXIV-2606-24004:start -->
### 2606.24004 — Towards Spec Learning: Inference-Time Alignment from Preference Pairs

**问题与旧路径。** Steering a large language model (LLM) toward a desired behavior typically relies on an iterative process of hand-crafting a prompt based on a careful inspection of the model's responses. 旧路径在输入分布、信任边界和预算稳定时仍合理。

**机制与 state/data/control owner。** Towards Spec Learning: Inference-Time Alignment from Preference Pairs 的 exact-v1 机制为：We propose spec learning, a framework that relies on a brief user instruction and a small set of preference judgments. 因此 把 rubric/spec 版本、policy 版本、独立 judge 与 reward-hacking 检测隔离。 唯一 owner 为 `TRAIN-RLHF`；相邻章只消费带 identity/version/failure/fallback 的 handoff。

**Evaluation：proof / non-proof。** Method=`arXiv:2606.24004v1 — §4 Spec Learning Framework; §4.1 Selection Method; §4.4 Judge protocol and selection`；Evaluation=`arXiv:2606.24004v1 — §5 Results; §B Statistical robustness; §C Judge calibration`；counterevidence=`arXiv:2606.24004v1 — §6 Discussion; §7 Limitations; §8 Conclusions and Future Work`。这些证据不证明未测试规模、分布、攻击者或生产 SLO。

**Trade-off / failure / coexistence / evolution。** 该 family 的 failure pressure 是：Steering a large language model (LLM) toward a desired behavior typically relies on an iterative process of hand-crafting a prompt based on a careful inspection of the model's responses. 披露的 evaluation signal 是：We show that the responses generated based on the compiled specifications often outperform direct preference optimization (DPO) on datasets from specialized domains whose preference signal is dense. 证据只支持 exact-v1 在披露 workload/model/hardware 范围内的机制与结果，不证明生产尾部、未测分布或形式安全；前提、identity 或预算越界时停止新路径，回退到该 owner 已验证的旧路径并保留失败回执。旧路径在其原约束成立时继续共存。

<!-- claim:SF-2026-ARXIV-2606-24004:start -->
Primary identity `arXiv:2606.24004v1`; official exact-v1 HTML; ordinary pending=0.
<!-- claim:SF-2026-ARXIV-2606-24004:end -->
<!-- review:SF-2026-ARXIV-2606-24004:end -->

<!-- review:SF-2026-ARXIV-2606-24020:start -->
### 2606.24020 — You Don't Need to Run Every Eval

**问题与旧路径。** A modern model release reports scores on 40+ benchmarks and the same evaluations were run many more times before it: to track training progress, compare design choices, and select the checkpoint for the release. 旧路径在输入分布、信任边界和预算稳定时仍合理。

**机制与 state/data/control owner。** You Don't Need to Run Every Eval 的 exact-v1 机制为：Building on this, we design BenchPress: a logit-space rank-2 matrix completion method that recovers held-out scores to within 4.6 points, and a confidence layer that says when each prediction can be trusted. 因此 把样本、metric、judge、阈值、不确定性和 release authority 分离。 唯一 owner 为 `PLATFORM-EVALUATION-SYSTEM`；相邻章只消费带 identity/version/failure/fallback 的 handoff。

**Evaluation：proof / non-proof。** Method=`arXiv:2606.24020v1 — §You Don’t Need to Run Every Eval Yuchen Zeng & Dimitris Papailiopoulos; §1 Introduction [You Don't Need to Run Every Eval exact-v1 method boundary]`；Evaluation=`arXiv:2606.24020v1 — §4 BenchPress : A Low-rank Benchmark Score Predictor; §4.3 BenchPress vs. LLMs as Benchmark Score Predictors; §5 What BenchPress Enables for Model Evaluation`；counterevidence=`arXiv:2606.24020v1 — §7 Discussion`。这些证据不证明未测试规模、分布、攻击者或生产 SLO。

**Trade-off / failure / coexistence / evolution。** 该 family 的 failure pressure 是：A modern model release reports scores on 40+ benchmarks and the same evaluations were run many more times before it: to track training progress, compare design choices, and select the checkpoint for the release. 披露的 evaluation signal 是：A modern model release reports scores on 40+ benchmarks and the same evaluations were run many more times before it: to track training progress, compare design choices, and select the checkpoint for the release. 证据只支持 exact-v1 在披露 workload/model/hardware 范围内的机制与结果，不证明生产尾部、未测分布或形式安全；metric、judge 或样本假设失效时保持 release Gate Open 并恢复完整评估。旧路径在其原约束成立时继续共存。

<!-- claim:SF-2026-ARXIV-2606-24020:start -->
Primary identity `arXiv:2606.24020v1`; official exact-v1 HTML; ordinary pending=0.
<!-- claim:SF-2026-ARXIV-2606-24020:end -->
<!-- review:SF-2026-ARXIV-2606-24020:end -->

<!-- review:SF-2026-ARXIV-2606-24033:start -->
### 2606.24033 — RoPE-Aware Bit Allocation for KV-Cache Quantization

**问题与旧路径。** Under RoPE, however, a key's contribution to a future attention logit decomposes into a position-dependent sum over two-dimensional frequency blocks. 旧路径在输入分布、信任边界和预算稳定时仍合理。

**机制与 state/data/control owner。** RoPE-Aware Bit Allocation for KV-Cache Quantization 的 exact-v1 机制为：We introduce Block-GTQ, a RoPE-aware bit allocator for key-cache quantization built on TurboQuant-MSE(TQ-MSE). 因此 把 cache position、eviction/quantization policy、跨模态 identity 与 dense recompute fallback 绑定。 唯一 owner 为 `INFER-KV-CACHE`；相邻章只消费带 identity/version/failure/fallback 的 handoff。

**Evaluation：proof / non-proof。** Method=`arXiv:2606.24033v1 — §RoPE-Aware Bit Allocation for KV-Cache Quantization; §1 Introduction [RoPE-Aware Bit Allocation for KV-Cache Quantization exact-v1 method boundary]`；Evaluation=`arXiv:2606.24033v1 — §6.3 Downstream Evaluation`；counterevidence=`arXiv:2606.24033v1 — §7 Conclusion`。这些证据不证明未测试规模、分布、攻击者或生产 SLO。

**Trade-off / failure / coexistence / evolution。** 该 family 的 failure pressure 是：Under RoPE, however, a key's contribution to a future attention logit decomposes into a position-dependent sum over two-dimensional frequency blocks. 披露的 evaluation signal 是：On a single H800 GPU with Qwen2.5-3B-Instruct, packed K3V3 achieves 3.24x KV-cache compression with fp16-comparable quality, runs 1.34x faster than fp16 FlashAttention2 at 128K context, reduces peak memory from 56.31 GB to 19.85 GB, and remains feasible at 256K and 512K where fp16 OOMs. 证据只支持 exact-v1 在披露 workload/model/hardware 范围内的机制与结果，不证明生产尾部、未测分布或形式安全；cache identity 或误差预算失配时清空该路径并回到未压缩/重算 KV。旧路径在其原约束成立时继续共存。

<!-- claim:SF-2026-ARXIV-2606-24033:start -->
Primary identity `arXiv:2606.24033v1`; official exact-v1 HTML; ordinary pending=0.
<!-- claim:SF-2026-ARXIV-2606-24033:end -->
<!-- review:SF-2026-ARXIV-2606-24033:end -->

<!-- review:SF-2026-ARXIV-2606-24040:start -->
### 2606.24040 — Towards Version-aware Operations and Transaction Memories for Multi-layer MeMo

**问题与旧路径。** MeMo proposes language models with explicit multi-layer correlation matrix memories (CMMs), where memorization, retrieval, and forgetting are architectural operations. 旧路径在输入分布、信任边界和预算稳定时仍合理。

**机制与 state/data/control owner。** Towards Version-aware Operations and Transaction Memories for Multi-layer MeMo 的 exact-v1 机制为：We propose a version-aware operation layer in which high-level operations such as replace, obsolete, keep-history, rollback, and trace are compiled into MeMo-native primitive calls over sequences and tokens. 因此 把事件时间、来源、有效条件、版本、检索决策与写入 authority 分开。 唯一 owner 为 `AGENT-MEMORY`；相邻章只消费带 identity/version/failure/fallback 的 handoff。

**Evaluation：proof / non-proof。** Method=`arXiv:2606.24040v1 — §3 Version-aware Operations; §4 Version and Transaction Correlation Memories`；Evaluation=`arXiv:2606.24040v1 — §5 Examples; §5.1 Direct sequence-level replacement; §5.2 Structured diff-level update`；counterevidence=`arXiv:2606.24040v1 — §6 Evaluation Roadmap and Scope; §7 Conclusion`。这些证据不证明未测试规模、分布、攻击者或生产 SLO。

**Trade-off / failure / coexistence / evolution。** 该 family 的 failure pressure 是：MeMo proposes language models with explicit multi-layer correlation matrix memories (CMMs), where memorization, retrieval, and forgetting are architectural operations. 披露的 evaluation signal 是：This paper asks how such memories can reduce the need for retraining when knowledge changes. 证据只支持 exact-v1 在披露 workload/model/hardware 范围内的机制与结果，不证明生产尾部、未测分布或形式安全；来源/时间/版本不足时隔离 candidate memory，保留原始轨迹且禁止自动覆盖。旧路径在其原约束成立时继续共存。

<!-- claim:SF-2026-ARXIV-2606-24040:start -->
Primary identity `arXiv:2606.24040v1`; official exact-v1 HTML; ordinary pending=0.
<!-- claim:SF-2026-ARXIV-2606-24040:end -->
<!-- review:SF-2026-ARXIV-2606-24040:end -->

<!-- review:SF-2026-ARXIV-2606-24074:start -->
### 2606.24074 — Token Complexity of Certifying Stochastic-Oracle Reliability

**问题与旧路径。** Wang~\cite{Wang2026} introduced the Stochastic-Oracle Turing Machine (SOTM) framework and defined token complexity as the minimum expected cost of interacting with a stochastic oracle needed to attain a specified solution quality for a task.

**机制、状态与控制流。** 把一次性 benchmark 分数改成带双侧错误界、逐 token 成本和停止阈值的 SPRT certification；certifier 持有 query/score/log-likelihood state，跨阈值才发布 reliable/unreliable verdict。 唯一 owner 为 `PLATFORM-EVALUATION-SYSTEM`；相邻章只消费显式 handoff。

**Trade-off、failure、fallback 与共存。** 只证明给定 reliability gap、binary correctness oracle 与 small-error leading order；不证明开放式 judge 标签、分布漂移或任意非独立 query 下仍满足同一界。

<!-- claim:SF-2026-ARXIV-2606-24074:start -->
Claim boundary：仅 `arXiv:2606.24074v1`；未证明边界定位 `https://arxiv.org/html/2606.24074v1 — §6 Conclusion and the stated small-error asymptotic regime`。
<!-- claim:SF-2026-ARXIV-2606-24074:end -->
<!-- review:SF-2026-ARXIV-2606-24074:end -->

<!-- review:SF-2026-ARXIV-2606-24081:start -->
### 2606.24081 — PixJail: Self-Evolving Paper-to-Pipeline Reproduction for Text-to-Image Jailbreak Evaluation

**问题与旧路径。** As Text-to-Image (T2I) jailbreak techniques evolve rapidly, existing benchmarks and reproduction workflows often struggle to keep pace.

**机制、状态与控制流。** 把 T2I jailbreak 的 prompt-only 比较升级为 paper-to-pipeline contract：attack module、victim、filter、multimodal judge、配置、日志与版本 artifact 共同成为可复现状态。 唯一 owner 为 `PLATFORM-EVALUATION-SYSTEM`；相邻章只消费显式 handoff。

**Trade-off、failure、fallback 与共存。** 11 种 attack、4 个 victim 与论文匹配配置不证明未知 attack 自动复现；prompt/heuristic memory update 及 closed-source safety filter 仍是黑盒边界。

<!-- claim:SF-2026-ARXIV-2606-24081:start -->
Claim boundary：仅 `arXiv:2606.24081v1`；未证明边界定位 `https://arxiv.org/html/2606.24081v1 — §6 Limitations`。
<!-- claim:SF-2026-ARXIV-2606-24081:end -->
<!-- review:SF-2026-ARXIV-2606-24081:end -->

<!-- review:SF-2026-ARXIV-2606-24119:start -->
### 2606.24119 — When Top-1 Fails: Calibrating LoRA Monitors for Masked Diffusion LMs

**问题与旧路径。** Discrete diffusion language model (DLM) fine-tuning inherits inexpensive diagnostics from denoising-time confidence monitors, but their PEFT-training meaning is untested.

**机制、状态与控制流。** 撤销把 denoising top-1 concentration 当 PEFT collapse alarm 的旧路径；monitor 改读 max LoRA gradient norm，并由每个 DLM family 的 held-out calibration 拥有告警阈值。 唯一 owner 为 `PLATFORM-MONITORING`；相邻章只消费显式 handoff。

**Trade-off、failure、fallback 与共存。** 816 个配置、3 个 DLM family 与 200-step horizon 只支持短程 DLM-LoRA triage；跨 family 阈值失败，不能外推为通用 collapse detector。

<!-- claim:SF-2026-ARXIV-2606-24119:start -->
Claim boundary：仅 `arXiv:2606.24119v1`；未证明边界定位 `https://arxiv.org/html/2606.24119v1 — §D Mechanism and Boundary Audit; Definitions and non-portability`。
<!-- claim:SF-2026-ARXIV-2606-24119:end -->
<!-- review:SF-2026-ARXIV-2606-24119:end -->

<!-- review:SF-2026-ARXIV-2606-24124:start -->
### 2606.24124 — VeryTrace: Verifying Reasoning Traces through Compilable Formalism and Structured Verification

**问题与旧路径。** Multi-step reasoning with Chain-of-Thought (CoT) prompting remains fragile: logical errors or hallucinations in early steps silently propagate, producing confident but incorrect conclusions.

**机制、状态与控制流。** 将自由文本 CoT 编译为 typed dependency/constraint/expression trace；deterministic verifier 拥有可机械化检查，LLM audit 只处理 semantic deduction，失败步骤进入 repair 而非直接接受终局答案。 唯一 owner 为 `PLATFORM-EVALUATION-SYSTEM`；相邻章只消费显式 handoff。

**Trade-off、failure、fallback 与共存。** 逐步验证成本随 trace 线性增长，semantic deduction 仍依赖 LLM audit，inference schema library 有限；三类 benchmark 不证明任意开放域推理。

<!-- claim:SF-2026-ARXIV-2606-24124:start -->
Claim boundary：仅 `arXiv:2606.24124v1`；未证明边界定位 `https://arxiv.org/html/2606.24124v1 — §F Limitations and Future Work`。
<!-- claim:SF-2026-ARXIV-2606-24124:end -->
<!-- review:SF-2026-ARXIV-2606-24124:end -->

<!-- review:SF-2026-ARXIV-2606-24133:start -->
### 2606.24133 — Holistic Data Scheduler for LLM Pre-training via Multi-Objective Reinforcement Learning

**问题与旧路径。** The composition of training data, governed by the diversity of sources and their mixing strategy, is a cornerstone of Large Language Model (LLM) pre-training.

**机制、状态与控制流。** 把固定或单目标 data mixture 改为 SAC controller：state 汇聚 domain loss/lexical diversity/weight-norm，action 写回下一训练阶段的 domain weights，多目标 reward 决定调度。 唯一 owner 为 `TRAIN-DATA`；相邻章只消费显式 handoff。

**Trade-off、failure、fallback 与共存。** The Pile、给定 16-layer/2048-dim recipe 与 reward sensitivity 不证明跨 tokenizer、optimizer、数据污染或超大规模 pretraining 仍有相同收益。

<!-- claim:SF-2026-ARXIV-2606-24133:start -->
Claim boundary：仅 `arXiv:2606.24133v1`；未证明边界定位 `https://arxiv.org/html/2606.24133v1 — §B Sensitivity Analysis of Reward Weights; C Hyperparameter Sensitivity`。
<!-- claim:SF-2026-ARXIV-2606-24133:end -->
<!-- review:SF-2026-ARXIV-2606-24133:end -->

<!-- review:SF-2026-ARXIV-2606-24143:start -->
### 2606.24143 — AsyncOPD: How Stale Can On-Policy Distillation Be?

**问题与旧路径。** On-policy distillation (OPD) trains a student on its own rollouts guided by teacher feedback and is becoming increasingly important for large language model (LLM) post-training.

**机制、状态与控制流。** 将 rollout、teacher scoring、student update 解耦为 queue stages；learner 用 current-student recomputation 修正 reverse-KL stale signal，并以 multi-sample MC 避免 cached top-k support bias。 唯一 owner 为 `TRAIN-DISTRIBUTED-TRAINING`；相邻章只消费显式 handoff。

**Trade-off、failure、fallback 与共存。** 实验限单节点 8 GPU、sparse/MC estimator；dense full-vocabulary KL、跨节点扩展与更长 staleness 未验证，cache/queue 压力过大时应回退 bounded-staleness 或同步 OPD。

<!-- claim:SF-2026-ARXIV-2606-24143:start -->
Claim boundary：仅 `arXiv:2606.24143v1`；未证明边界定位 `https://arxiv.org/html/2606.24143v1 — §8 Limitations and Future Work`。
<!-- claim:SF-2026-ARXIV-2606-24143:end -->
<!-- review:SF-2026-ARXIV-2606-24143:end -->

<!-- review:SF-2026-ARXIV-2606-24151:start -->
### 2606.24151 — Metis: Bridging Text and Code Memory for Self-Evolving Agents

**问题与旧路径。** Self-evolving agents improve over time by distilling experience from past executions and reusing it in future tasks.

**机制、状态与控制流。** 不在设计时固定 text 或 code memory；memory manager 先保存 plan/fact/pitfall 文本，只有重复且验证通过的 plan 才 crystallize 为 callable tool，同时保留构建成本与 provenance。 唯一 owner 为 `AGENT-MEMORY`；相邻章只消费显式 handoff。

**Trade-off、failure、fallback 与共存。** AppWorld 与同一 experience set 只显示两种表示在 construction cost、execution efficiency、transferability 上互补；不证明生成工具在未知 API、权限变化或污染经验下安全。

<!-- claim:SF-2026-ARXIV-2606-24151:start -->
Claim boundary：仅 `arXiv:2606.24151v1`；未证明边界定位 `https://arxiv.org/html/2606.24151v1 — §A.1 Per-Axis Analysis and reported construction/transfer trade-offs`。
<!-- claim:SF-2026-ARXIV-2606-24151:end -->
<!-- review:SF-2026-ARXIV-2606-24151:end -->

<!-- review:SF-2026-ARXIV-2606-24177:start -->
### 2606.24177 — Agon: An Autonomous Large-Scale Omnidisciplinary Research System Built on Prompt Economy

**问题与旧路径。** Large language models are making research production scalable, shifting the bottleneck from producing artifacts to judging claims.

**机制、状态与控制流。** 以 artifact 为边界组织 producer-critic factory，critic 在 fresh context 验收后才推进；自动化 loop 只提交可机器检查部分，visibility/fixability taxonomy 将不可判定 claim 留给 human scientist。 唯一 owner 为 `AGENT-WORKFLOW`；相邻章只消费显式 handoff。

**Trade-off、failure、fallback 与共存。** 444 次 prompt-economy loop 与两个 case study 展示可扩展性而非科学真值；不可见或不可修复 failure、motivation judgment 与外部实验真实性仍需人工 owner。

<!-- claim:SF-2026-ARXIV-2606-24177:start -->
Claim boundary：仅 `arXiv:2606.24177v1`；未证明边界定位 `https://arxiv.org/html/2606.24177v1 — §4.7 What the Architecture Can and Cannot Absorb; 4.8 Boundary Is a Snapshot`。
<!-- claim:SF-2026-ARXIV-2606-24177:end -->
<!-- review:SF-2026-ARXIV-2606-24177:end -->

<!-- review:SF-2026-ARXIV-2606-24204:start -->
### 2606.24204 — Unified Dominance Graph for Interval-Predicate Approximate Nearest Neighbor Search

**问题与旧路径。** Approximate Nearest Neighbor Search (ANNS) is a core primitive for unstructured data retrieval.

**机制、状态与控制流。** 把 interval predicate 的双端点约束映射为统一 2D dominance space；每个 predicate 拥有独立 UDG instance，patch edge 只在 validity 保持时补路由，避免两个 scalar index 的交集爆炸。 唯一 owner 为 `AGENT-RAG`；相邻章只消费显式 handoff。

**Trade-off、failure、fallback 与共存。** 闭合 two-bound conjunctive predicate 与论文数据集不覆盖任意布尔 filter、动态高 churn 或 distributed index consistency；过滤结构不匹配时回退普通 filtered ANN。

<!-- claim:SF-2026-ARXIV-2606-24204:start -->
Claim boundary：仅 `arXiv:2606.24204v1`；未证明边界定位 `https://arxiv.org/html/2606.24204v1 — §V-B Validity-Preserving Patch Edges; VI-D Impact of Patch Edges`。
<!-- claim:SF-2026-ARXIV-2606-24204:end -->
<!-- review:SF-2026-ARXIV-2606-24204:end -->

<!-- review:SF-2026-ARXIV-2606-24245:start -->
### 2606.24245 — AutoSpec: Safety Rule Evolution for LLM Agents via Inductive Logic Programming

**问题与旧路径。** Large language model (LLM) agents increasingly automate complex tasks by integrating language models with external tools and environments.

**机制、状态与控制流。** 把静态 expert rule 的维护改为 annotation-driven CEGIS：trace evaluator 产出 FP/FN counterexample，ILP 选 discriminating predicate，candidate verifier 决定是否发布 rule revision。 唯一 owner 为 `PLATFORM-SECURITY`；相邻章只消费显式 handoff。

**Trade-off、failure、fallback 与共存。** 291 条 code/embodied trace 与 4–5 次迭代不证明稀疏、错误或对抗标注下收敛；发布前仍需 human approval、versioned rollback 与旧 expert rules 共存。

<!-- claim:SF-2026-ARXIV-2606-24245:start -->
Claim boundary：仅 `arXiv:2606.24245v1`；未证明边界定位 `https://arxiv.org/html/2606.24245v1 — §7 Discussion and Threats to Validity`。
<!-- claim:SF-2026-ARXIV-2606-24245:end -->
<!-- review:SF-2026-ARXIV-2606-24245:end -->

<!-- review:SF-2026-ARXIV-2606-24311:start -->
### 2606.24311 — LemonHarness Technical Report

**问题与旧路径。** As large language model (LLM) agents are applied to longer tasks, they increasingly modify workspace state across multiple rounds of iteration.

**机制、状态与控制流。** 将 model invocation、tool execution、workspace mutation、rule knowledge 与 execution record 收进同一 runtime boundary；剩余时间成为显式 state，用于在探索、实现、验证之间重配预算。 唯一 owner 为 `AGENT-PLATFORM`；相邻章只消费显式 handoff。

**Trade-off、failure、fallback 与共存。** 结果主要绑定 GPT-style tool calling 与 Terminal-Bench；其他 model family、长编译/训练、严格中间验证和 workspace 外 side effect 未证明，应保留人工接管与受限 sandbox。

<!-- claim:SF-2026-ARXIV-2606-24311:start -->
Claim boundary：仅 `arXiv:2606.24311v1`；未证明边界定位 `https://arxiv.org/html/2606.24311v1 — §5 Limitations and Future Work`。
<!-- claim:SF-2026-ARXIV-2606-24311:end -->
<!-- review:SF-2026-ARXIV-2606-24311:end -->

<!-- review:SF-2026-ARXIV-2606-24322:start -->
### 2606.24322 — Securing LLM-Agent Long-Term Memory Against Poisoning: Non-Malleable, Origin-Bound Authority with Machine-Checked Guarantees

**问题与旧路径。** LLM agents increasingly rely on persistent long-term memory, which creates a critical vulnerability that we study here: memory poisoning.

**机制、状态与控制流。** memory item 的行动权不再由可篡改 content/lineage 推断，而在 write 时绑定 origin authority；只有 k 个独立 trusted source 才 elevation，高风险 action 缺少 corroborator 时交给 one-time user confirmation。 唯一 owner 为 `PLATFORM-SECURITY`；相邻章只消费显式 handoff。

**Trade-off、failure、fallback 与共存。** 保证依赖正确 origin labeling、独立 principal 与有限 TLA+ model；trusted tool compromise、隐式 value reconstruction、nested payload taint 和广泛真实任务仍未闭合。

<!-- claim:SF-2026-ARXIV-2606-24322:start -->
Claim boundary：仅 `arXiv:2606.24322v1`；未证明边界定位 `https://arxiv.org/html/2606.24322v1 — §IX Limitations`。
<!-- claim:SF-2026-ARXIV-2606-24322:end -->
<!-- review:SF-2026-ARXIV-2606-24322:end -->

<!-- review:SF-2026-ARXIV-2606-24402:start -->
### 2606.24402 — Poisoned Playbooks: Demystifying Knowledge Poisoning Effects on AI Security Agents

**问题与旧路径。** AI security agents increasingly rely on Retrieval-Augmented Generation (RAG) to use external security knowledge for vulnerability analysis and exploit reasoning.

**机制、状态与控制流。** RAG 安全 gate 不再只问文档是否被检索，而按 local-artifact、model-knowledge、runtime-dependent 三层 verification boundary 决定 claim 能否进入行动；L3 需要动态探测或权威外部证据。 唯一 owner 为 `PLATFORM-SECURITY`；相邻章只消费显式 handoff。

**Trade-off、failure、fallback 与共存。** 11 CTF、11 CVE、3 model family 下 prompt verification/multi-source retrieval 在 sparse-evidence 与 zero-day 会退化；不能把信息多数当独立真实性。

<!-- claim:SF-2026-ARXIV-2606-24402:start -->
Claim boundary：仅 `arXiv:2606.24402v1`；未证明边界定位 `https://arxiv.org/html/2606.24402v1 — §8 Discussions and Limitations`。
<!-- claim:SF-2026-ARXIV-2606-24402:end -->
<!-- review:SF-2026-ARXIV-2606-24402:end -->

<!-- review:SF-2026-ARXIV-2606-24408:start -->
### 2606.24408 — Natural Identifiers for Privacy and Data Audits in Large Language Models

**问题与旧路径。** Assessing the privacy of large language models (LLMs) presents significant challenges.

**机制、状态与控制流。** 利用训练数据自然出现且稀有的 identifier 作为 post-hoc audit unit，避免必须预埋 canary；auditor 分离 DP leakage 检查与 dataset inference，并记录 identifier cardinality/生成机制。 唯一 owner 为 `PLATFORM-SECURITY`；相邻章只消费显式 handoff。

**Trade-off、failure、fallback 与共存。** NID 可用性、独立性与 generator 正确性依赖数据域；黑盒可见性、重复 identifier、强 MIA 和 DP-SGD 配置变化会改变 sample complexity，不能当作逐样本法律证明。

<!-- claim:SF-2026-ARXIV-2606-24408:start -->
Claim boundary：仅 `arXiv:2606.24408v1`；未证明边界定位 `https://arxiv.org/html/2606.24408v1 — §M Limitations`。
<!-- claim:SF-2026-ARXIV-2606-24408:end -->
<!-- review:SF-2026-ARXIV-2606-24408:end -->

<!-- review:SF-2026-ARXIV-2606-24428:start -->
### 2606.24428 — Escaping the Self-Confirmation Trap: An Execute-Distill-Verify Paradigm for Agentic Experience Learning

**问题与旧路径。** Experience-driven self-evolution is critical for large language model (LLM) agents to improve through open-world interaction.

**机制、状态与控制流。** 经验写入从同一 agent 自我总结改为 Execute 的异构并行轨迹、第三方 contrastive Distill 与 consensus Verify；只有通过独立验证的经验才能进入 storage/retrieval。 唯一 owner 为 `AGENT-MEMORY`；相邻章只消费显式 handoff。

**Trade-off、failure、fallback 与共存。** 多 agent consensus 仍可能相关失败，且 tau2-Bench/Mind2Web/MMTB 与论文 temperature/retrieval 配置不证明开放任务；不确定时保存 raw trajectories 或拒绝写入。

<!-- claim:SF-2026-ARXIV-2606-24428:start -->
Claim boundary：仅 `arXiv:2606.24428v1`；未证明边界定位 `https://arxiv.org/html/2606.24428v1 — §G Limitations`。
<!-- claim:SF-2026-ARXIV-2606-24428:end -->
<!-- review:SF-2026-ARXIV-2606-24428:end -->

<!-- review:SF-2026-ARXIV-2606-24437:start -->
### 2606.24437 — ReM-MoA: Reasoning Memory Sustains Mixture-of-Agents Scaling

**问题与旧路径。** Mixture-of-Agents (MoA) architectures improve inference-time scaling by organizing multiple LLM agents into layered reasoning pipelines.

**机制、状态与控制流。** MoA 不再把所有历史 reasoning 平铺给 aggregator；reviewer 对轨迹排序写入 reasoning memory，router 按 layer/quality/diversity 投影少量 references，使 memory state 随协作层累积。 唯一 owner 为 `AGENT-MULTI-AGENT`；相邻章只消费显式 handoff。

**Trade-off、failure、fallback 与共存。** 只测固定 proposer pool、有限 width 与五个 benchmark；reviewer bias/overhead 和同源 proposer correlation 会放大错误，低置信时回退无 memory MoA 或独立 adjudication。

<!-- claim:SF-2026-ARXIV-2606-24437:start -->
Claim boundary：仅 `arXiv:2606.24437v1`；未证明边界定位 `https://arxiv.org/html/2606.24437v1 — §Bounded width; Single-scale proposer pool; Reviewer overhead`。
<!-- claim:SF-2026-ARXIV-2606-24437:end -->
<!-- review:SF-2026-ARXIV-2606-24437:end -->

<!-- review:SF-2026-ARXIV-2606-24467:start -->
### 2606.24467 — CompressKV: Semantic-Retrieval-Guided KV-Cache Compression for Resource-Efficient Long-Context LLM Inference

**问题与旧路径。** Long-context large language model (LLM) inference is increasingly constrained by the memory footprint and decoding cost of key-value (KV) caches, limiting sustainable deployment on resource-constrained hardware.

**机制、状态与控制流。** KV eviction 从统一 token score 改为 semantic-retrieval heads 选 token、error-aware controller 按层分配 cache budget；压缩决定属于 cache manager，不修改模型语义 owner。 唯一 owner 为 `INFER-KV-CACHE`；相邻章只消费显式 handoff。

**Trade-off、failure、fallback 与共存。** LongBench/NIAH 与选定模型不证明所有 head 都稳定承载语义检索；head drift、低命中或质量回退时恢复更大 cache/全 KV，与 quantization/prefill acceleration 仅证明可组合。

<!-- claim:SF-2026-ARXIV-2606-24467:start -->
Claim boundary：仅 `arXiv:2606.24467v1`；未证明边界定位 `https://arxiv.org/html/2606.24467v1 — §4.5 Ablations; 4.6 Orthogonality tests`。
<!-- claim:SF-2026-ARXIV-2606-24467:end -->
<!-- review:SF-2026-ARXIV-2606-24467:end -->

<!-- review:SF-2026-ARXIV-2606-24506:start -->
### 2606.24506 — CrossPool: Efficient Multi-LLM Serving for Cold MoE Models through KV-Cache and Weight Disaggregation

**问题与旧路径。** Emerging LLM services increasingly host many sparse MoE models, yet most models receive sparse requests and remain cold.

**机制、状态与控制流。** 冷 MoE serving 将 stable weights 与 demand-driven KV 拆成独立资源池；planner virtualize shared KV，layer-wise scheduler/persistent kernel 只激活所需 weights 和 KV heads。 唯一 owner 为 `INFER-GPU-MEMORY`；相邻章只消费显式 handoff。

**Trade-off、failure、fallback 与共存。** 证据聚焦冷模型、低并发与给定 context/model mix；热点突发、跨租户 isolation、模型装载故障和高并发下 shared-pool contention 未证明，应能回退 dedicated allocation。

<!-- claim:SF-2026-ARXIV-2606-24506:start -->
Claim boundary：仅 `arXiv:2606.24506v1`；未证明边界定位 `https://arxiv.org/html/2606.24506v1 — §6 Discussion`。
<!-- claim:SF-2026-ARXIV-2606-24506:end -->
<!-- review:SF-2026-ARXIV-2606-24506:end -->

<!-- review:SF-2026-ARXIV-2606-24535:start -->
### 2606.24535 — Governed Shared Memory for Multi-Agent LLM Systems

**问题与旧路径。** Multi-agent LLM environments require robust mechanisms for shared knowledge management.

**机制、状态与控制流。** 多 Agent 共享记忆增加 explicit scope、valid time、provenance graph 与 policy-gated retrieval；矛盾在 write-time resolution，reader 只消费已提交版本，传播由 privilege gate 控制。 唯一 owner 为 `AGENT-MEMORY`；相邻章只消费显式 handoff。

**Trade-off、failure、fallback 与共存。** self-evaluation、single tenant、focused scope probe、有限 workload 且无 comparand；staleness-after-supersession 与 visibility 延迟未完整测量，冲突时回退 tenant-local memory 或 single writer。

<!-- claim:SF-2026-ARXIV-2606-24535:start -->
Claim boundary：仅 `arXiv:2606.24535v1`；未证明边界定位 `https://arxiv.org/html/2606.24535v1 — §10 Limitations`。
<!-- claim:SF-2026-ARXIV-2606-24535:end -->
<!-- review:SF-2026-ARXIV-2606-24535:end -->

<!-- review:SF-2026-ARXIV-2606-24551:start -->
### 2606.24551 — GUI vs. CLI: Execution Bottlenecks in Screen-Only and Skill-Mediated Computer-Use Agents

**问题与旧路径。** In this controlled setting, the strongest GUI agent reaches a 59.1% full pass rate, outperforming the strongest original-skill CLI agent at 48.2%; however, verifier-guided skill augmentation raises CLI success to 69.3%, showing that much of the CLI deficit comes from incomplete skill coverage rather than model capability alone. 旧路径在输入分布、信任边界和预算稳定时仍合理。

**机制与 state/data/control owner。** GUI vs. CLI: Execution Bottlenecks in Screen-Only and Skill-Mediated Computer-Use Agents 的 exact-v1 机制为：We introduce a matched execution-layer benchmark of 440 desktop tasks across 18 applications and 12 workflow categories, where screen-only GUI agents and skill-mediated CLI agents receive identical goals, states, and final-state verifiers while being restricted to modality-native actions. 因此 把 tool schema、状态前置条件、GUI/CLI execution surface 与 side-effect receipt 绑定。 唯一 owner 为 `AGENT-TOOL-CALLING`；相邻章只消费带 identity/version/failure/fallback 的 handoff。

**Evaluation：proof / non-proof。** Method=`arXiv:2606.24551v1 — §3.2 Benchmark Construction; §A.3 Visual Design Example`；Evaluation=`arXiv:2606.24551v1 — §3 Benchmark; §3.1 Benchmark Scope and Composition; §3.2 Benchmark Construction`；counterevidence=`arXiv:2606.24551v1 — §3.1 Benchmark Scope and Composition; §UI Navigation and Control Discovery Failure.; §Workflow Execution Failure.`。这些证据不证明未测试规模、分布、攻击者或生产 SLO。

**Trade-off / failure / coexistence / evolution。** 该 family 的 failure pressure 是：In this controlled setting, the strongest GUI agent reaches a 59.1% full pass rate, outperforming the strongest original-skill CLI agent at 48.2%; however, verifier-guided skill augmentation raises CLI success to 69.3%, showing that much of the CLI deficit comes from incomplete skill coverage rather than model capability alone. 披露的 evaluation signal 是：Computer-use agents can execute software tasks through either graphical interfaces or programmatic command interfaces, but existing evaluations confound interaction modality with differences in tasks, initial states, verifiers, and permitted actions. 证据只支持 exact-v1 在披露 workload/model/hardware 范围内的机制与结果，不证明生产尾部、未测分布或形式安全；前提、identity 或预算越界时停止新路径，回退到该 owner 已验证的旧路径并保留失败回执。旧路径在其原约束成立时继续共存。

<!-- claim:SF-2026-ARXIV-2606-24551:start -->
Primary identity `arXiv:2606.24551v1`; official exact-v1 HTML; ordinary pending=0.
<!-- claim:SF-2026-ARXIV-2606-24551:end -->
<!-- review:SF-2026-ARXIV-2606-24551:end -->

<!-- review:SF-2026-ARXIV-2606-24598:start -->
### 2606.24598 — Toward Self-Evolution-Ready Workflow Harnesses: A Reversible Migration Path and Convertibility Taxonomy for Expert LLM Pipelines

**问题、旧路径与机制。** 旧路径在输入、信任边界与 workload 稳定时仍合理；本 family 改变的是：expert LLM workflow 迁移到 self-evolution 前应先做 convertibility taxonomy、reversible adapter 与 rollback，不直接改写 opaque harness。

**State / data / control owner。** `AGENT-WORKFLOW` 持有 authoritative state 与 control decision；相邻章节只消费带 identity、version、failure 与 fallback 的 handoff。

**Evaluation：proof / non-proof。** `arXiv:2606.24598v1 §3 Migration Method; §4 Architecture; §7 Convertibility Taxonomy`；`arXiv:2606.24598v1 §5 WeChat Case Study; §6 Evaluation`；counterevidence `arXiv:2606.24598v1 §9 Discussion and Threats to Validity; abstract explicitly limits evidence to one case and readiness, not validated self-learning`。证据证明作者机制在披露合同内的行为，不证明生产部署或未测分布。

**Trade-off / failure / coexistence / evolution。** 证据仅是单个 WeChat workflow 的可逆迁移和 early feedback signal，不是验证过的 self-learning；taxonomy 误路由时回退并一键回滚 legacy harness，保持业务逻辑不变。

<!-- claim:SF-2026-ARXIV-2606-24598:start -->
仅使用 `https://arxiv.org/html/2606.24598v1` exact-v1；later revision/artifact 不扩张 claim，ordinary pending=`0`。
<!-- claim:SF-2026-ARXIV-2606-24598:end -->
<!-- review:SF-2026-ARXIV-2606-24598:end -->

<!-- review:SF-2026-ARXIV-2606-24626:start -->
### 2606.24626 — SAFARI: Scaling Long Horizon Agentic Fault Attribution via Active Investigation

**问题与旧路径。** As autonomous agents tackle increasingly complex multi-step, multi-agent tasks, their execution trajectories have scaled beyond the constraints of even the largest context windows.

**机制、状态与控制流。** 故障诊断不再把全 trajectory 填入一个 context；investigator 用 segment search/read tools 主动取证，并用 persistent STM 保存跨轮 hypothesis/evidence，使 attribution 与原始 trace 长度解耦。 唯一 owner 为 `PLATFORM-TRACE`；相邻章只消费显式 handoff。

**Trade-off、failure、fallback 与共存。** Who&When/TRAIL GAIA、1M/25K token budget 与给定 toolbox 不证明生产 trace schema、并发因果或根因真实性；缺证据时返回 unknown 并交给人工 trace drill-down。

<!-- claim:SF-2026-ARXIV-2606-24626:start -->
Claim boundary：仅 `arXiv:2606.24626v1`；未证明边界定位 `https://arxiv.org/html/2606.24626v1 — §D Future Work`。
<!-- claim:SF-2026-ARXIV-2606-24626:end -->
<!-- review:SF-2026-ARXIV-2606-24626:end -->

<!-- review:SF-2026-ARXIV-2606-24722:start -->
### 2606.24722 — Decentralised AI Training and Inference with BlockTrain

**问题与旧路径。** Frontier AI training is increasingly shaped by access to dense, centrally controlled accelerator clusters.

**机制、状态与控制流。** 把 end-to-end backprop 的全局 hidden-target ownership拆成 block-local diffusion objective；edge worker 独立更新 block，coordinator 只按版本/acceptance rule 接收异步 update，同一 block protocol 也支撑分布式 inference。 唯一 owner 为 `TRAIN-DISTRIBUTED-TRAINING`；相邻章只消费显式 handoff。

**Trade-off、failure、fallback 与共存。** real-text small model、virtual edge worker 与 WAN smoke test 不证明大模型质量、Byzantine worker、激励或大规模收敛；acceptance 失败时回退同步/集中训练。

<!-- claim:SF-2026-ARXIV-2606-24722:start -->
Claim boundary：仅 `arXiv:2606.24722v1`；未证明边界定位 `https://arxiv.org/html/2606.24722v1 — §4.4 HTTP/TCP Transport Proof; 6 Conclusion`。
<!-- claim:SF-2026-ARXIV-2606-24722:end -->
<!-- review:SF-2026-ARXIV-2606-24722:end -->

<!-- review:SF-2026-ARXIV-2606-24774:start -->
### 2606.24774 — Revealing Training Data Exposure in Vision Language Large Models via Parameter Gradients

**问题与旧路径。** Vision-Language Large Models (VLLMs) trained on massive crawled corpora raise pressing copyright and data-provenance concerns.

**机制、状态与控制流。** training-data audit 从 output entropy 转向 parameter-gradient signature；auditor 对跨模态 parameter slices 做稳定性/对齐特征，并用已知 train/non-train reference mask 掉不敏感维度。 唯一 owner 为 `PLATFORM-SECURITY`；相邻章只消费显式 handoff。

**Trade-off、failure、fallback 与共存。** 需要 white-box parameters 与 reference data；七个 VLM 配置、medical/general dataset 不证明黑盒 API、生成式泄漏或法律层面的逐样本归属。

<!-- claim:SF-2026-ARXIV-2606-24774:start -->
Claim boundary：仅 `arXiv:2606.24774v1`；未证明边界定位 `https://arxiv.org/html/2606.24774v1 — §White-box parameter-access scope and reference-data dependence`。
<!-- claim:SF-2026-ARXIV-2606-24774:end -->
<!-- review:SF-2026-ARXIV-2606-24774:end -->

<!-- review:SF-2026-ARXIV-2606-24775:start -->
### 2606.24775 — Are We Ready For An Agent-Native Memory System?

**问题与旧路径。** Memory for large language model (LLM) agents has rapidly evolved from simple retrieval-augmented mechanisms into a data management system that supports persistent information storage, retrieval, update, consolidation, and dynamic lifecycle governance throughout agent execution.

**机制、状态与控制流。** 把 agent memory 评价拆成 logical representation、physical storage/index、extraction、query routing 与 maintenance 五个 ownerable stage，并分别测 retrieval fidelity、evolution robustness、long-horizon stability 和 operation cost。 唯一 owner 为 `AGENT-MEMORY`；相邻章只消费显式 handoff。

**Trade-off、failure、fallback 与共存。** 现有系统/benchmark 比较不证明单一实现普适最优；缺少生产 authorization、deletion SLA、并发一致性或真实 workload 时只能作为 lifecycle checklist。

<!-- claim:SF-2026-ARXIV-2606-24775:start -->
Claim boundary：仅 `arXiv:2606.24775v1`；未证明边界定位 `https://arxiv.org/html/2606.24775v1 — §4.3 Evolution Robustness; 4.4 Long-Horizon Stability; 4.5 Cost`。
<!-- claim:SF-2026-ARXIV-2606-24775:end -->
<!-- review:SF-2026-ARXIV-2606-24775:end -->

<!-- audit-target:evidence:end -->
## 4. Benchmark Contracts

<!-- validator:benchmark-contract-v1 -->
| Source Family ID | Workload | Model | Hardware | Precision | Input Length | Output Length | Batch | Concurrency | SLO | Evaluator |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2606-23740 | offline reasoning training weight-space geometry | Qwen3-4B-Instruct-2507 | Not Disclosed | BF16; attention LoRA rank 32 alpha 64 | Not Disclosed | Not Disclosed | 32; 1,500 steps | Not Disclosed | Not Disclosed | weight-space distance, representation and reasoning accuracy |
| SF-2026-ARXIV-2606-23743 | full-stack video-generation inference | three video-generation models named in exact-v1 | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | author-reported latency/throughput configuration | latency, throughput, memory and generation quality |
| SF-2026-ARXIV-2606-23752 | ESAA-Conversational: An Event-Sourced Memory Layer for Continuity, Handoff, and Curation Across Heterogeneous LLM Coding Agents — The result is conversational state drift: goals, decisions, open tasks, and rationales established with one agent are not reliably available when another agent takes over. | Claude Code | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | The result is conversational state drift: goals, decisions, open tasks, and rationales established with one agent are not reliably available when another agent takes over. |
| SF-2026-ARXIV-2606-23754 | Verifiable Foundation Models for Robot Safety — To show that the decomposed policy remains capable of solving diverse tasks, we evaluate FEARL on three simulated robotic domains using multiple Controller backbones and training procedures, including pretrained off-the-shelf vision-language-action models. | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | To show that the decomposed policy remains capable of solving diverse tasks, we evaluate FEARL on three simulated robotic domains using multiple Controller backbones and training procedures, including pretrained off-the-shelf vision-language-action models. |
| SF-2026-ARXIV-2606-23768 | Cryptographic certificates of validity for trustworthy AI — We outline the approach at a high level, give the core mathematical translation, relate the proposal to proof-carrying code, zkVMs, formal methods, and agent governance, and note the specification, auditing, and deployment questions that a full implementation must answer. | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | We outline the approach at a high level, give the core mathematical translation, relate the proposal to proof-carrying code, zkVMs, formal methods, and agent governance, and note the specification, auditing, and deployment questions that a full implementation must answer. |
| SF-2026-ARXIV-2606-23797 | From Task-Guided Conversational Graphs to Goal-Oriented Dialogue Runtimes — The paper formalizes the problem, proposes runtime objects and architecture-selection criteria, and frames evaluation as an agenda for future empirical validation rather than as a measured performance claim. | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Graph and multi-agent orchestration frameworks make production large language model (LLM) workflows practical, but they do not by themselves solve conversational continuity when users maintain several interdependent objectives. | Not Disclosed | The paper formalizes the problem, proposes runtime objects and architecture-selection criteria, and frames evaluation as an agenda for future empirical validation rather than as a measured performance claim. |
| SF-2026-ARXIV-2606-23858 | Are Safety Guarantees in Neural Networks Safe? How to Compute Trustworthy Robustness Certifications — Most existing approaches focus on maximizing the certification's volume, but recent intractability results prohibit the computation of volume-optimal certifications in reasonable time. | Not Disclosed | Not Disclosed | An important technicality here is that we use a precision constant δ > 0 \delta>0 to ensure a “meaningful” reduction of the interval. Definition 4 (Constrain Operator) Consider an input 𝐱 ∈ 𝔽 \mathbf{x}\in\mathbb{F} , an interval I = 𝐱 + [ ℓ , 𝒖 ] I=\mathbf{x}+[\boldsymbol{\ell},\boldsymbol{u}] , with ℓ ≤ 𝟎 ≤ 𝒖 \boldsymbol{\ell}\leq\mathbf{0}\leq\boldsymbol{u} , an adversarial example 𝐯 ∈ I \mathbf{v}\in I , and a precision constant δ > 0 \delta>0 . | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Most existing approaches focus on maximizing the certification's volume, but recent intractability results prohibit the computation of volume-optimal certifications in reasonable time. |
| SF-2026-ARXIV-2606-23872 | MGI: Member vs Generated Inference — Focusing on image generation, we show that existing membership inference methods systematically misclassify generated samples as training members, while attribution-based methods often misclassify true members as generated. | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Model Batch Size Learning Rate Training Samples Epochs VAR 4 1 × 10 − 5 1\times 10^{-5} 5000 5 RAR 4 1 × 10 − 5 1\times 10^{-5} 5000 5 SD 1.4 4 1 × 10 − 5 1\times 10^{-5} 5000 20 SD 2.1 4 1 × 10 − 5 1\times 10^{-5} 5000 20 Appendix B Distribution Visualization on More Models In this section, we complement the distribution analysis of the main paper with visualizations for additional models and settings. | Not Disclosed | Not Disclosed | Focusing on image generation, we show that existing membership inference methods systematically misclassify generated samples as training members, while attribution-based methods often misclassify true members as generated. |
| SF-2026-ARXIV-2606-23892 | REALM: A Unified Red-Teaming Benchmark for Physical-World VLMs — Although many red-teaming methods have been developed to probe VLM vulnerabilities, their evaluation remains fragmented across datasets, metrics, and threat models, making direct comparison difficult and obscuring whether observed differences arise from stronger attacks, more vulnerable models, or incompatible evaluation settings. | Not Disclosed | [22] NVIDIA Cosmos-Reason1-7B . Note: https://huggingface.co/nvidia/Cosmos-Reason1-7B Hugging Face model card Cited by: §1 , §4.2 . | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Our evaluation shows that text and typographic injection attacks induce the most failures, multimodal co-optimization yields the strongest visual-perturbation transfer, single-pass attacks approach iterative methods at much lower cost, and model scale alone does not confer adversarial robustness. | Although many red-teaming methods have been developed to probe VLM vulnerabilities, their evaluation remains fragmented across datasets, metrics, and threat models, making direct comparison difficult and obscuring whether observed differences arise from stronger attacks, more vulnerable models, or incompatible evaluation settings. |
| SF-2026-ARXIV-2606-23915 | Do LLM Attribution Metrics Transfer? Auditing Retrieval-Augmented Generation Evaluation Across Datasets and Constructs — We audit eight automatic scorers -- lexical, embedding, and BERTScore baselines alongside entailment/grounding-trained models (clean and FEVER NLI, the checker MiniCheck) -- across three evaluation constructs (provenance/topicality, generated-answer attribution, and fact-check entailment), asking whether any scorer transfers: stays within the 95% confidence interval of the best audited scorer on every dataset of a multi-dataset construct. | Not Disclosed | Not Disclosed | ALCE ( Gao et al., 2023 ) introduced NLI-based citation recall/precision (with QAMPARI ( Amouyal et al., 2023 ) ); FActScore ( Min et al., 2023 ) decomposes into atomic facts; Attribute-First ( Slobodkin et al., 2024 ) and LongCite ( Zhang et al., 2024 ) produce attributable text; AttrScore ( Yue et al., 2023 ) and RAGAS ( Es et al., 2024 ) judge support with LLM/entailment models. We measure citation count , which is flat; we did not regenerate NLI-based ALCE citation recall/precision ( Gao et al., 2023 ) (it requires a large entailment model and a different decoding setup), and we make no claim about it here. | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | This instability has a concrete decision cost: a naive "best-on-average" rule for choosing an evaluator fails leave-one-dataset-out (mean held-out regret 0.172 AUROC, worse than fixing one scorer), so metric choice must be validated on the target dataset rather than learned from others. | We audit eight automatic scorers -- lexical, embedding, and BERTScore baselines alongside entailment/grounding-trained models (clean and FEVER NLI, the checker MiniCheck) -- across three evaluation constructs (provenance/topicality, generated-answer attribution, and fact-check entailment), asking whether any scorer transfers: stays within the 95% confidence interval of the best audited scorer on every dataset of a multi-dataset construct. |
| SF-2026-ARXIV-2606-23927 | RIFT-Bench: Dynamic Red-teaming For Agentic AI Systems — Existing security evaluations are often tied to specific implementations or domains, limiting unified comparison across heterogeneous systems. | Not Disclosed | Not Disclosed | The evaluator reports this as an F1 score using precision 1 1 and recall / M / / / P / /M///P/ : Coverage-F1 = 2 ​ r 1 + r , r = / M / / P / . | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Existing security evaluations are often tied to specific implementations or domains, limiting unified comparison across heterogeneous systems. |
| SF-2026-ARXIV-2606-23937 | When Retrieval Metrics Mislead: Measuring Policy Signal in Long-Horizon Tool-Use Agents — Under gold-policy conditioning, a compact structured state improves macro-F1 over raw trajectories by 0.13-0.17 after tuning. | Qwen2.5-3B | Not Disclosed | B.4 Per-class and per-task behaviour To check whether aggregate macro-F1 masks class-specific behavior, Table 5 reports per-class precision/recall/F1 (computed from the SFT predictions, pooled over seeds). Input class P R F1 raw allow 0.50 0.32 0.39 verify 0.69 0.46 0.55 refuse 0.31 0.70 0.43 raw+policy allow 0.82 0.39 0.53 verify 0.59 0.54 0.56 refuse 0.46 0.89 0.60 structured allow 0.59 0.67 0.63 verify 0.88 0.40 0.55 refuse 0.47 1.00 0.64 Table 5: Per-class precision/recall/F1 (SFT gate, pooled over 3 seeds; computed from committed predictions). | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Under gold-policy conditioning, a compact structured state improves macro-F1 over raw trajectories by 0.13-0.17 after tuning. |
| SF-2026-ARXIV-2606-23961 | Forget Without Compromise: Nexus Sampling for Streaming KV-Cache Eviction Under Fixed Budgets — Theoretically, we show that Nexus Sampling dominates deterministic top-$K$ in long-run survival of subtly important tokens. | Llama-3.1-8B-Instruct | All experiments run on a single NVIDIA H200 (143 GB) with greedy decoding. | Not Disclosed | Not Disclosed | Not Disclosed | All runs use Llama-3.1-8B-Instruct in bf16 on a single H200 (143 GB), prefill length T p = 8 ​ K T_{p}=8\text{K} , batch size 1, against dense FlashAttention-2 [ 6 ] and the baselines from Tables 1 – 2 . Table 4: Decode throughput (tokens/s) and per-step latency (ms) at T p = 8 ​ K T_{p}=8\text{K} prefill, batch size 1, on Llama-3.1-8B-Instruct (H200, bf16). | Not Disclosed | Not Disclosed | Theoretically, we show that Nexus Sampling dominates deterministic top-$K$ in long-run survival of subtly important tokens. |
| SF-2026-ARXIV-2606-23969 | The Serialized Bridge: Understanding and Recovering LLM Serving Performance under Blackwell GPU Confidential Computing — We qualify confidential multi-GPU NVSwitch tenants on B300, including 510 GB/s NVLink P2P inside a CVM and concurrent isolated tenants, and identify the remaining fabric-attestation gap for production confidential AI platforms. | Not Disclosed | 2 Background 2.1 GPU-CC and the CVM-GPU Bridge In the configuration we study, Intel TDX protects a confidential VM ( Intel, 2026 ) and NVIDIA GPU-CC protects GPU execution and the GPU’s Compute Protected Region (CPR) ( NVIDIA, 2026a ; NVIDIA, 2026e ) . | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | We find that GPU-CC turns host/device movement into a serialized, high-setup-cost channel. | Yet LLM serving under Intel TDX plus GPU-CC still loses 13-27% of throughput, and KV-cache restore latency can more than double. | We qualify confidential multi-GPU NVSwitch tenants on B300, including 510 GB/s NVLink P2P inside a CVM and concurrent isolated tenants, and identify the remaining fabric-attestation gap for production confidential AI platforms. |
| SF-2026-ARXIV-2606-23983 | Maestro Order: A Model-Agnostic Orchestration Harness — We then specify an evaluation methodology (reliability at fixed cost, coverage, calibration, and ablations) and report results from a faithful Monte Carlo simulation of the harness over a parameterized solver/verifier model. | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | The harness treats any model as a black-box base solver behind a uniform interface, layers a verifier ensemble whose discrimination is measured online, and allocates verification and voting to the stages with the highest marginal reliability per unit cost. | We then specify an evaluation methodology (reliability at fixed cost, coverage, calibration, and ablations) and report results from a faithful Monte Carlo simulation of the harness over a parameterized solver/verifier model. |
| SF-2026-ARXIV-2606-23989 | Faithful by Construction: Claim-Anchored Attribution for Multi-Document Summarization — We evaluate quality, faithfulness, and localization on MultiNews, analyze conflict handling on DiverseSumm, and test zero-shot transfer on WCEP, using a two-regime protocol that separates reference-free citation quality from gold-aligned localization accuracy, and we add an evaluator-decoupled audit that tests citation precision with a support model never used for selection or verification. | Not Disclosed | Experiments run on 4 × 4\times A100 GPUs; full hyperparameters, prompts, schemas, and per-module algorithms are in Appendices A , B , and C (Table 7 ). The full run uses four A100 GPUs, with extraction, clustering, selection, rewriting, and verification logged separately for reproducibility. | We evaluate quality, faithfulness, and localization on MultiNews, analyze conflict handling on DiverseSumm, and test zero-shot transfer on WCEP, using a two-regime protocol that separates reference-free citation quality from gold-aligned localization accuracy, and we add an evaluator-decoupled audit that tests citation precision with a support model never used for selection or verification. CAMS matches strong end-to-end and span-attribution baselines on summary quality while substantially improving faithfulness and citation precision, lifting multi-source attribution accuracy by roughly two-thirds, and exposing | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | We evaluate quality, faithfulness, and localization on MultiNews, analyze conflict handling on DiverseSumm, and test zero-shot transfer on WCEP, using a two-regime protocol that separates reference-free citation quality from gold-aligned localization accuracy, and we add an evaluator-decoupled audit that tests citation precision with a support model never used for selection or verification. |
| SF-2026-ARXIV-2606-24004 | Towards Spec Learning: Inference-Time Alignment from Preference Pairs — We show that the responses generated based on the compiled specifications often outperform direct preference optimization (DPO) on datasets from specialized domains whose preference signal is dense. | DeepSeek, Gemma, Qwen | • Proposers & Judges (Compilation and Evaluation): – Gemma 4 31B: 1 × 1\times NVIDIA H200 – DeepSeek V4 Flash: 2 × 2\times NVIDIA B200 – Kimi K2.6: 8 × 8\times NVIDIA H200 • Base Policy (Qwen 2.5 32B Instruct): – Inference (Baseline and Spec Application): 1 × 1\times NVIDIA A100 (80GB) – DPO Training: 1 × 1\times NVIDIA H200 Appendix F DPO Training Configuration We train each DPO baseline with TRL’s DPOTrainer Rafailov et al. | You maintain absolute precision in your implementation, ensuring that all variable names are consistent and correctly spelled, and that keywords, boolean values, assignments, and comparison operators are entirely free of typos. Hyperparameter Value Base model Qwen 2.5 32B Instruct Training pairs ( N N ) 1,000 (900 for Truthy-DPO) DPO β \beta 0.1 Optimizer AdamW Learning rate 5 × 10 − 6 5{\times}10^{-6} LR scheduler cosine, warmup ratio 0.1 Epochs 3 Effective batch size 16 Max sequence length 1024 Precision bf16 LoRA rank ( r r ) 32 LoRA α \alpha 64 LoRA dropout 0.05 LoRA targets all attention and FFN projections | Hyperparameter Value Base model Qwen 2.5 32B Instruct Training pairs ( N N ) 1,000 (900 for Truthy-DPO) DPO β \beta 0.1 Optimizer AdamW Learning rate 5 × 10 − 6 5{\times}10^{-6} LR scheduler cosine, warmup ratio 0.1 Epochs 3 Effective batch size 16 Max sequence length 1024 Precision bf16 LoRA rank ( r r ) 32 LoRA α \alpha 64 LoRA dropout 0.05 LoRA targets all attention and FFN projections Checkpoint selection lowest evaluation loss Hardware 1 × \times H200 NeurIPS Paper Checklist 1. | Not Disclosed | Hyperparameter Value Base model Qwen 2.5 32B Instruct Training pairs ( N N ) 1,000 (900 for Truthy-DPO) DPO β \beta 0.1 Optimizer AdamW Learning rate 5 × 10 − 6 5{\times}10^{-6} LR scheduler cosine, warmup ratio 0.1 Epochs 3 Effective batch size 16 Max sequence length 1024 Precision bf16 LoRA rank ( r r ) 32 LoRA α \alpha 64 LoRA dropout 0.05 LoRA targets all attention and FFN projections Checkpoint selection lowest evaluation loss Hardware 1 × \times H200 NeurIPS Paper Checklist 1. | Not Disclosed | Not Disclosed | We show that the responses generated based on the compiled specifications often outperform direct preference optimization (DPO) on datasets from specialized domains whose preference signal is dense. |
| SF-2026-ARXIV-2606-24020 | You Don't Need to Run Every Eval — A modern model release reports scores on 40+ benchmarks and the same evaluations were run many more times before it: to track training progress, compare design choices, and select the checkpoint for the release. | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | A modern model release reports scores on 40+ benchmarks and the same evaluations were run many more times before it: to track training progress, compare design choices, and select the checkpoint for the release. |
| SF-2026-ARXIV-2606-24033 | RoPE-Aware Bit Allocation for KV-Cache Quantization — On a single H800 GPU with Qwen2.5-3B-Instruct, packed K3V3 achieves 3.24x KV-cache compression with fp16-comparable quality, runs 1.34x faster than fp16 FlashAttention2 at 128K context, reduces peak memory from 56.31 GB to 19.85 GB, and remains feasible at 256K and 512K where fp16 OOMs. | DeepSeek-R1-Distill-Qwen-7B, Llama-3.1-8B-Instruct, Qwen2.5-3B-Instruct | We further implement a packed-cache serving path that avoids materializing an fp16 KV cache: on a single H800 GPU with Qwen2.5-3B-Instruct, the packed K3V3 path achieves 3.24 × 3.24\times KV-cache compression with quality comparable to fp16, runs 1.34 × 1.34\times faster than fp16 FlashAttention2 at 128 128 K context, reduces peak memory from 56.31 56.31 GB to 19.85 19.85 GB, and remains feasible at 256 256 K/ 512 512 K where fp16 OOMs. 6.4 Block-GTQ Deployment We run Qwen2.5-3B-Instruct on a single H800 GPU at the K3V3 operating point and report decode-step latency, peak GPU memory, and downstream perplexity. | Non-uniform precision allocation. Key-cache quantization should allocate precision across RoPE blocks according to their logit impact, rather than optimize a single flat-vector reconstruction objective over the whole key head. | Autoregressive long-context decoding is often limited by repeatedly reading a KV cache that grows with sequence length [ 27 ] . | Not Disclosed | Not Disclosed | Not Disclosed | This makes key-cache quantization a block-wise bit-allocation problem: high-energy RoPE blocks are more sensitive to quantization error and should receive more bits. | On a single H800 GPU with Qwen2.5-3B-Instruct, packed K3V3 achieves 3.24x KV-cache compression with fp16-comparable quality, runs 1.34x faster than fp16 FlashAttention2 at 128K context, reduces peak memory from 56.31 GB to 19.85 GB, and remains feasible at 256K and 512K where fp16 OOMs. |
| SF-2026-ARXIV-2606-24040 | Towards Version-aware Operations and Transaction Memories for Multi-layer MeMo — This paper asks how such memories can reduce the need for retraining when knowledge changes. | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | This paper asks how such memories can reduce the need for retraining when knowledge changes. |
| SF-2026-ARXIV-2606-24074 | Wang~\cite{Wang2026} introduced the Stochastic-Oracle Turing Machine (SOTM) framework and defined token complexity as the minimum expected cost of interacting with a stochastic oracle needed to attain a specified solution quality for a task. | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed |
| SF-2026-ARXIV-2606-24081 | 11 T2I jailbreak methods under original and unified settings | 4 victim T2I models | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | paper-result reproduction error, attack success and memory code-quality ablation |
| SF-2026-ARXIV-2606-24119 | 816 LoRA/PEFT configurations from three DLM families; 200-step horizon | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | collapse precision, F1, final loss and cross-family threshold transfer |
| SF-2026-ARXIV-2606-24124 | Multi-step reasoning with Chain-of-Thought (CoT) prompting remains fragile: logical errors or hallucinations in early steps silently propagate, producing confident but incorrect conclusions. | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Across three diverse domains-competition mathematics (AIME 2025), robotics planning (LLM-BabyBench), and kinship reasoning (CLUTRR), VeryTrace improves accuracy over zero-shot baselines on state-of-the-art LLMs without requiring domain-specific training or in-context examples, demonstrating that formalized trace verification achieves both precision and generalization. |
| SF-2026-ARXIV-2606-24133 | The composition of training data, governed by the diversity of sources and their mixing strategy, is a cornerstone of Large Language Model (LLM) pre-training. | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | To validate our design and determine its optimal configuration, we conducted systematic experiments on LLMs of various sizes. |
| SF-2026-ARXIV-2606-24143 | On-policy distillation (OPD) trains a student on its own rollouts guided by teacher feedback and is becoming increasingly important for large language model (LLM) post-training. | Qwen3-1.7B/4B/8B Base | single 8-GPU node | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | training tokens/s, pipeline overlap, Avg@32 accuracy and staleness ablations |
| SF-2026-ARXIV-2606-24151 | Self-evolving agents improve over time by distilling experience from past executions and reusing it in future tasks. | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Our results show that the two forms exhibit complementary trade-offs in construction cost, execution efficiency, and transferability, such that neither representation alone is sufficient. |
| SF-2026-ARXIV-2606-24177 | Large language models are making research production scalable, shifting the bottleneck from producing artifacts to judging claims. | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Together, these results show that \textsc{Agon} is pushing research toward a new paradigm: machine scales, human steers. |
| SF-2026-ARXIV-2606-24204 | Approximate Nearest Neighbor Search (ANNS) is a core primitive for unstructured data retrieval. | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Extensive evaluations on standard benchmarks and real-world datasets show that UDG achieves stable query performance across multiple interval relations and workloads, significantly outperforming existing hybrid search baselines while maintaining low indexing overhead. |
| SF-2026-ARXIV-2606-24245 | Large language model (LLM) agents increasingly automate complex tasks by integrating language models with external tools and environments. | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Starting from the expert rules and a stream of annotated traces, AutoSpec iteratively evaluates rules, mines false-positive and false-negative counterexamples, uses ILP to learn which predicates discriminate them, generates candidate rule edits, and verifies candidates to select the best revision. |
| SF-2026-ARXIV-2606-24311 | Terminal-Bench 2.0: five jobs x 89 trials; Terminal-Bench 2.1: three jobs x 89 trials | GPT-5.3-CodeX and GPT-5.5 | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | accuracy, failures and execution exceptions |
| SF-2026-ARXIV-2606-24322 | MEM-INV-Bench; 128 multi-turn runs; Mem0+Qdrant 96 runs per defense | eight frontier models; six models in production-backend study | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | laundering/direct attack success, legitimate utility and user-confirmation burden |
| SF-2026-ARXIV-2606-24402 | 11 CTF challenges, 11 real-world CVEs and 8,651 security write-ups | Claude Opus 4/4.6, GPT-5.3 and Gemini 3.0 Pro | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | poison adoption rate, retrieval rank and rejection cause |
| SF-2026-ARXIV-2606-24408 | Assessing the privacy of large language models (LLMs) presents significant challenges. | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Our evaluation highlights that indeed, using NIDs, we can facilitate post-hoc differential privacy auditing without any retraining and enable dataset inference for any suspect dataset containing NIDs without the need for a private non-member held-out dataset. |
| SF-2026-ARXIV-2606-24428 | Experience-driven self-evolution is critical for large language model (LLM) agents to improve through open-world interaction. | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | We evaluate EDV on three challenging long-horizon benchmarks: tau2-bench, Mind2Web and MMTB. |
| SF-2026-ARXIV-2606-24437 | Mixture-of-Agents (MoA) architectures improve inference-time scaling by organizing multiple LLM agents into layered reasoning pipelines. | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Across five reasoning benchmarks spanning math, formal logic, code, knowledge, and commonsense, ReM-MoA consistently outperforms prior MoA variants across both depth and width scaling, and its advantage widens with depth, establishing structured cross-layer reasoning memory as a key missing mechanism for scalable multi-agent inference. |
| SF-2026-ARXIV-2606-24467 | Long-context large language model (LLM) inference is increasingly constrained by the memory footprint and decoding cost of key-value (KV) caches, limiting sustainable deployment on resource-constrained hardware. | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Experiments on LongBench and Needle-in-a-Haystack show that CompressKV consistently outperforms existing KV-cache eviction methods across memory budgets. |
| SF-2026-ARXIV-2606-24506 | Emerging LLM services increasingly host many sparse MoE models, yet most models receive sparse requests and remain cold. | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | With efficient GPU memory pooling, CrossPool underpins bursty long-context requests and outperforms the state-of-the-art kvcached-based multi-LLM serving system, reducing P99 TBT by up to 10.4x. |
| SF-2026-ARXIV-2606-24535 | Multi-agent LLM environments require robust mechanisms for shared knowledge management. | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | These primitives are implemented in MemClaw, a production multi-tenant memory service, and evaluated via ArgusFleet, a reproducible harness testing four governance dimensions. |
| SF-2026-ARXIV-2606-24551 | GUI vs. CLI: Execution Bottlenecks in Screen-Only and Skill-Mediated Computer-Use Agents — Computer-use agents can execute software tasks through either graphical interfaces or programmatic command interfaces, but existing evaluations confound interaction modality with differences in tasks, initial states, verifiers, and permitted actions. | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Computer-use agents can execute software tasks through either graphical interfaces or programmatic command interfaces, but existing evaluations confound interaction modality with differences in tasks, initial states, verifiers, and permitted actions. |
| SF-2026-ARXIV-2606-24598 | single production WeChat Official Account expert workflow migrated through nine typed tools | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | one production WeChat workflow; nine expert functions/tools; nine adversarial invariant tests; three self-operated accounts for observational feedback | Not Disclosed | Not Disclosed | business-logic parity, rollback, traceability, deterministic invariant and early feedback signal |
| SF-2026-ARXIV-2606-24626 | As autonomous agents tackle increasingly complex multi-step, multi-agent tasks, their execution trajectories have scaled beyond the constraints of even the largest context windows. | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Our experiments demonstrate that SAFARI outperforms state-of-the-art results by 20% on the Who&amp;When dataset within a 1M token budget, and by 19% on TRAIL GAIA subset on a 25K token budget. |
| SF-2026-ARXIV-2606-24722 | Frontier AI training is increasingly shaped by access to dense, centrally controlled accelerator clusters. | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | HTTP/TCP transport experiments move real serialized checkpoints and updates, including a public-IP three-host run that improves CE from 5.580 to 1.811 while moving 15.22 GB. |
| SF-2026-ARXIV-2606-24774 | Vision-Language Large Models (VLLMs) trained on massive crawled corpora raise pressing copyright and data-provenance concerns. | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | By analyzing these gradient signatures, GradAudit achieves strong separability and detects genuine image-text associations learned during training, not merely individual modality membership. |
| SF-2026-ARXIV-2606-24775 | Memory for large language model (LLM) agents has rapidly evolved from simple retrieval-augmented mechanisms into a data management system that supports persistent information storage, retrieval, update, consolidation, and dynamic lifecycle governance throughout agent execution. | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Not Disclosed | Despite this evolution, existing evaluations still benchmark agent memory mainly through end-to-end task success metrics (e.g., F1, BLEU), while treating the underlying system as a monolithic black box. |
<!-- audit-target:deep_analysis_selection:start -->
## 5. Deep Analysis Selection

<!-- validator:deep-analysis-selection-v1 -->
| Source Family ID | Eligibility | Decision | Analysis Unit ID | Subsumed By | Priority Rationale | Narrative Ref |
| --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2606-23740 | score_7_9; potential_books_delta | not_selected | — | — | Weight-Space Geometry of Offline Reasoning Training remains evidence-complete after canonical owner transfer with V2 score 7 and owner TRAIN-RLHF. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-23740 |
| SF-2026-ARXIV-2606-23743 | score_7_9; potential_books_delta | not_selected | — | — | Sol Video Inference Engine: Agent-Native Full-Stack Acceleration Framework for Efficient Video Generation remains evidence-complete after canonical owner transfer with V2 score 7 and owner INFER-TENSORRT-LLM. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-23743 |
| SF-2026-ARXIV-2606-23752 | score_7_9; potential_books_delta | not_selected | — | — | ESAA-Conversational: An Event-Sourced Memory Layer for Continuity, Handoff, and Curation Across Heterogeneous LLM Coding Agents remains evidence-complete after canonical owner transfer with V2 score 7 and owner AGENT-MEMORY. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-23752 |
| SF-2026-ARXIV-2606-23754 | score_7_9; potential_books_delta | not_selected | — | — | Verifiable Foundation Models for Robot Safety remains evidence-complete after canonical owner transfer with V2 score 7 and owner MULTIMODAL-EMBODIED-VLA. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-23754 |
| SF-2026-ARXIV-2606-23768 | score_7_9; potential_books_delta | not_selected | — | — | Cryptographic certificates of validity for trustworthy AI remains evidence-complete after canonical owner transfer with V2 score 9 and owner PLATFORM-SECURITY. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-23768 |
| SF-2026-ARXIV-2606-23797 | score_7_9; potential_books_delta | not_selected | — | — | From Task-Guided Conversational Graphs to Goal-Oriented Dialogue Runtimes remains evidence-complete after canonical owner transfer with V2 score 9 and owner AGENT-WORKFLOW. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-23797 |
| SF-2026-ARXIV-2606-23858 | score_7_9; potential_books_delta | not_selected | — | — | Are Safety Guarantees in Neural Networks Safe? How to Compute Trustworthy Robustness Certifications remains evidence-complete after canonical owner transfer with V2 score 9 and owner PLATFORM-SECURITY. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-23858 |
| SF-2026-ARXIV-2606-23872 | score_7_9; potential_books_delta | not_selected | — | — | MGI: Member vs Generated Inference remains evidence-complete after canonical owner transfer with V2 score 9 and owner PLATFORM-SECURITY. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-23872 |
| SF-2026-ARXIV-2606-23892 | score_7_9; potential_books_delta | not_selected | — | — | REALM: A Unified Red-Teaming Benchmark for Physical-World VLMs remains evidence-complete after canonical owner transfer with V2 score 9 and owner PLATFORM-SECURITY. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-23892 |
| SF-2026-ARXIV-2606-23915 | score_7_9; potential_books_delta | not_selected | — | — | Do LLM Attribution Metrics Transfer? Auditing Retrieval-Augmented Generation Evaluation Across Datasets and Constructs remains evidence-complete after canonical owner transfer with V2 score 8 and owner PLATFORM-EVALUATION-SYSTEM. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-23915 |
| SF-2026-ARXIV-2606-23927 | score_7_9; potential_books_delta | not_selected | — | — | RIFT-Bench: Dynamic Red-teaming For Agentic AI Systems remains evidence-complete after canonical owner transfer with V2 score 9 and owner PLATFORM-SECURITY. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-23927 |
| SF-2026-ARXIV-2606-23937 | score_7_9; potential_books_delta | not_selected | — | — | When Retrieval Metrics Mislead: Measuring Policy Signal in Long-Horizon Tool-Use Agents remains evidence-complete after canonical owner transfer with V2 score 8 and owner PLATFORM-EVALUATION-SYSTEM. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-23937 |
| SF-2026-ARXIV-2606-23961 | score_7_9; potential_books_delta | not_selected | — | — | Forget Without Compromise: Nexus Sampling for Streaming KV-Cache Eviction Under Fixed Budgets remains evidence-complete after canonical owner transfer with V2 score 7 and owner INFER-KV-CACHE. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-23961 |
| SF-2026-ARXIV-2606-23969 | score_7_9; potential_books_delta | not_selected | — | — | The Serialized Bridge: Understanding and Recovering LLM Serving Performance under Blackwell GPU Confidential Computing remains evidence-complete after canonical owner transfer with V2 score 9 and owner PLATFORM-SECURITY. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-23969 |
| SF-2026-ARXIV-2606-23983 | score_7_9; potential_books_delta | not_selected | — | — | Maestro Order: A Model-Agnostic Orchestration Harness remains evidence-complete after canonical owner transfer with V2 score 8 and owner AGENT-PLATFORM. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-23983 |
| SF-2026-ARXIV-2606-23989 | score_7_9; potential_books_delta | not_selected | — | — | Faithful by Construction: Claim-Anchored Attribution for Multi-Document Summarization remains evidence-complete after canonical owner transfer with V2 score 7 and owner AGENT-RAG. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-23989 |
| SF-2026-ARXIV-2606-24004 | score_7_9; potential_books_delta | not_selected | — | — | Towards Spec Learning: Inference-Time Alignment from Preference Pairs remains evidence-complete after canonical owner transfer with V2 score 7 and owner TRAIN-RLHF. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-24004 |
| SF-2026-ARXIV-2606-24020 | score_7_9; potential_books_delta | not_selected | — | — | You Don't Need to Run Every Eval remains evidence-complete after canonical owner transfer with V2 score 8 and owner PLATFORM-EVALUATION-SYSTEM. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-24020 |
| SF-2026-ARXIV-2606-24033 | score_7_9; potential_books_delta | not_selected | — | — | RoPE-Aware Bit Allocation for KV-Cache Quantization remains evidence-complete after canonical owner transfer with V2 score 7 and owner INFER-KV-CACHE. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-24033 |
| SF-2026-ARXIV-2606-24040 | score_7_9; potential_books_delta | not_selected | — | — | Towards Version-aware Operations and Transaction Memories for Multi-layer MeMo remains evidence-complete after canonical owner transfer with V2 score 7 and owner AGENT-MEMORY. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-24040 |
| SF-2026-ARXIV-2606-24074 | score_7_9; potential_books_delta | not_selected | — | — | Token Complexity of Certifying Stochastic-Oracle Reliability remains evidence-complete after canonical owner transfer with V2 score 8 and owner PLATFORM-EVALUATION-SYSTEM. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-24074 |
| SF-2026-ARXIV-2606-24081 | score_7_9; potential_books_delta | not_selected | — | — | PixJail: Self-Evolving Paper-to-Pipeline Reproduction for Text-to-Image Jailbreak Evaluation remains evidence-complete after canonical owner transfer with V2 score 8 and owner PLATFORM-EVALUATION-SYSTEM. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-24081 |
| SF-2026-ARXIV-2606-24119 | score_7_9; potential_books_delta | not_selected | — | — | When Top-1 Fails: Calibrating LoRA Monitors for Masked Diffusion LMs remains evidence-complete after canonical owner transfer with V2 score 8 and owner PLATFORM-MONITORING. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-24119 |
| SF-2026-ARXIV-2606-24124 | score_7_9; potential_books_delta | not_selected | — | — | VeryTrace: Verifying Reasoning Traces through Compilable Formalism and Structured Verification remains evidence-complete after canonical owner transfer with V2 score 8 and owner PLATFORM-EVALUATION-SYSTEM. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-24124 |
| SF-2026-ARXIV-2606-24133 | score_7_9; potential_books_delta | not_selected | — | — | Holistic Data Scheduler for LLM Pre-training via Multi-Objective Reinforcement Learning remains evidence-complete after canonical owner transfer with V2 score 7 and owner TRAIN-DATA. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-24133 |
| SF-2026-ARXIV-2606-24143 | score_7_9; potential_books_delta | not_selected | — | — | AsyncOPD: How Stale Can On-Policy Distillation Be? remains evidence-complete after canonical owner transfer with V2 score 9 and owner TRAIN-DISTRIBUTED-TRAINING. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-24143 |
| SF-2026-ARXIV-2606-24151 | score_7_9; potential_books_delta | not_selected | — | — | Metis: Bridging Text and Code Memory for Self-Evolving Agents remains evidence-complete after canonical owner transfer with V2 score 7 and owner AGENT-MEMORY. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-24151 |
| SF-2026-ARXIV-2606-24177 | score_7_9; potential_books_delta | not_selected | — | — | Agon: An Autonomous Large-Scale Omnidisciplinary Research System Built on Prompt Economy remains evidence-complete after canonical owner transfer with V2 score 8 and owner AGENT-WORKFLOW. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-24177 |
| SF-2026-ARXIV-2606-24204 | score_7_9; potential_books_delta | not_selected | — | — | Unified Dominance Graph for Interval-Predicate Approximate Nearest Neighbor Search remains evidence-complete after canonical owner transfer with V2 score 7 and owner AGENT-RAG. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-24204 |
| SF-2026-ARXIV-2606-24245 | score_7_9; potential_books_delta | not_selected | — | — | AutoSpec: Safety Rule Evolution for LLM Agents via Inductive Logic Programming remains evidence-complete after canonical owner transfer with V2 score 9 and owner PLATFORM-SECURITY. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-24245 |
| SF-2026-ARXIV-2606-24311 | score_7_9; potential_books_delta | not_selected | — | — | LemonHarness Technical Report remains evidence-complete after canonical owner transfer with V2 score 8 and owner AGENT-PLATFORM. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-24311 |
| SF-2026-ARXIV-2606-24322 | score_7_9; potential_books_delta | selected | DA-20260624-2606-24322 | — | 入选：memory item 的行动权不再由可篡改 content/lineage 推断，而在 write 时绑定 origin authority；只有 k 个独立 trusted source 才 elevation，高风险 action 缺少 corroborator 时交给 one-time user confirmation。 | analysis:DA-20260624-2606-24322 |
| SF-2026-ARXIV-2606-24402 | score_7_9; potential_books_delta | not_selected | — | — | Poisoned Playbooks: Demystifying Knowledge Poisoning Effects on AI Security Agents remains evidence-complete after canonical owner transfer with V2 score 9 and owner PLATFORM-SECURITY. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-24402 |
| SF-2026-ARXIV-2606-24408 | score_7_9; potential_books_delta | not_selected | — | — | Natural Identifiers for Privacy and Data Audits in Large Language Models remains evidence-complete after canonical owner transfer with V2 score 9 and owner PLATFORM-SECURITY. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-24408 |
| SF-2026-ARXIV-2606-24428 | score_7_9; potential_books_delta | not_selected | — | — | Escaping the Self-Confirmation Trap: An Execute-Distill-Verify Paradigm for Agentic Experience Learning remains evidence-complete after canonical owner transfer with V2 score 7 and owner AGENT-MEMORY. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-24428 |
| SF-2026-ARXIV-2606-24437 | score_7_9; potential_books_delta | not_selected | — | — | ReM-MoA: Reasoning Memory Sustains Mixture-of-Agents Scaling remains evidence-complete after canonical owner transfer with V2 score 7 and owner AGENT-MULTI-AGENT. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-24437 |
| SF-2026-ARXIV-2606-24467 | score_7_9; potential_books_delta | not_selected | — | — | CompressKV: Semantic-Retrieval-Guided KV-Cache Compression for Resource-Efficient Long-Context LLM Inference remains evidence-complete after canonical owner transfer with V2 score 7 and owner INFER-KV-CACHE. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-24467 |
| SF-2026-ARXIV-2606-24506 | score_7_9; potential_books_delta | not_selected | — | — | CrossPool: Efficient Multi-LLM Serving for Cold MoE Models through KV-Cache and Weight Disaggregation remains evidence-complete after canonical owner transfer with V2 score 8 and owner INFER-GPU-MEMORY. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-24506 |
| SF-2026-ARXIV-2606-24535 | score_7_9; potential_books_delta | not_selected | — | — | Governed Shared Memory for Multi-Agent LLM Systems remains evidence-complete after canonical owner transfer with V2 score 7 and owner AGENT-MEMORY. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-24535 |
| SF-2026-ARXIV-2606-24551 | score_7_9; potential_books_delta | not_selected | — | — | GUI vs. CLI: Execution Bottlenecks in Screen-Only and Skill-Mediated Computer-Use Agents remains evidence-complete after canonical owner transfer with V2 score 7 and owner AGENT-TOOL-CALLING. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-24551 |
| SF-2026-ARXIV-2606-24598 | score_7_9; potential_books_delta | not_selected | — | — | Toward Self-Evolution-Ready Workflow Harnesses: A Reversible Migration Path and Convertibility Taxonomy for Expert LLM Pipelines remains evidence-complete after canonical owner transfer with V2 score 9 and owner AGENT-WORKFLOW. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-24598 |
| SF-2026-ARXIV-2606-24626 | score_7_9; potential_books_delta | not_selected | — | — | SAFARI: Scaling Long Horizon Agentic Fault Attribution via Active Investigation remains evidence-complete after canonical owner transfer with V2 score 8 and owner PLATFORM-TRACE. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-24626 |
| SF-2026-ARXIV-2606-24722 | score_7_9; potential_books_delta | not_selected | — | — | Decentralised AI Training and Inference with BlockTrain remains evidence-complete after canonical owner transfer with V2 score 9 and owner TRAIN-DISTRIBUTED-TRAINING. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-24722 |
| SF-2026-ARXIV-2606-24774 | score_7_9; potential_books_delta | not_selected | — | — | Revealing Training Data Exposure in Vision Language Large Models via Parameter Gradients remains evidence-complete after canonical owner transfer with V2 score 9 and owner PLATFORM-SECURITY. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-24774 |
| SF-2026-ARXIV-2606-24775 | score_7_9; potential_books_delta | not_selected | — | — | Are We Ready For An Agent-Native Memory System? remains evidence-complete after canonical owner transfer with V2 score 7 and owner AGENT-MEMORY. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization. | analysis-decision:SF-2026-ARXIV-2606-24775 |

### Selected Analysis Narratives

<!-- analysis-decision:SF-2026-ARXIV-2606-23740:start -->
Weight-Space Geometry of Offline Reasoning Training remains evidence-complete after canonical owner transfer with V2 score 7 and owner TRAIN-RLHF. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-23740:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-23743:start -->
Sol Video Inference Engine: Agent-Native Full-Stack Acceleration Framework for Efficient Video Generation remains evidence-complete after canonical owner transfer with V2 score 7 and owner INFER-TENSORRT-LLM. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-23743:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-23752:start -->
ESAA-Conversational: An Event-Sourced Memory Layer for Continuity, Handoff, and Curation Across Heterogeneous LLM Coding Agents remains evidence-complete after canonical owner transfer with V2 score 7 and owner AGENT-MEMORY. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-23752:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-23754:start -->
Verifiable Foundation Models for Robot Safety remains evidence-complete after canonical owner transfer with V2 score 7 and owner MULTIMODAL-EMBODIED-VLA. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-23754:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-23768:start -->
Cryptographic certificates of validity for trustworthy AI remains evidence-complete after canonical owner transfer with V2 score 9 and owner PLATFORM-SECURITY. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-23768:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-23797:start -->
From Task-Guided Conversational Graphs to Goal-Oriented Dialogue Runtimes remains evidence-complete after canonical owner transfer with V2 score 9 and owner AGENT-WORKFLOW. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-23797:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-23858:start -->
Are Safety Guarantees in Neural Networks Safe? How to Compute Trustworthy Robustness Certifications remains evidence-complete after canonical owner transfer with V2 score 9 and owner PLATFORM-SECURITY. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-23858:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-23872:start -->
MGI: Member vs Generated Inference remains evidence-complete after canonical owner transfer with V2 score 9 and owner PLATFORM-SECURITY. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-23872:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-23892:start -->
REALM: A Unified Red-Teaming Benchmark for Physical-World VLMs remains evidence-complete after canonical owner transfer with V2 score 9 and owner PLATFORM-SECURITY. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-23892:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-23915:start -->
Do LLM Attribution Metrics Transfer? Auditing Retrieval-Augmented Generation Evaluation Across Datasets and Constructs remains evidence-complete after canonical owner transfer with V2 score 8 and owner PLATFORM-EVALUATION-SYSTEM. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-23915:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-23927:start -->
RIFT-Bench: Dynamic Red-teaming For Agentic AI Systems remains evidence-complete after canonical owner transfer with V2 score 9 and owner PLATFORM-SECURITY. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-23927:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-23937:start -->
When Retrieval Metrics Mislead: Measuring Policy Signal in Long-Horizon Tool-Use Agents remains evidence-complete after canonical owner transfer with V2 score 8 and owner PLATFORM-EVALUATION-SYSTEM. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-23937:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-23961:start -->
Forget Without Compromise: Nexus Sampling for Streaming KV-Cache Eviction Under Fixed Budgets remains evidence-complete after canonical owner transfer with V2 score 7 and owner INFER-KV-CACHE. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-23961:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-23969:start -->
The Serialized Bridge: Understanding and Recovering LLM Serving Performance under Blackwell GPU Confidential Computing remains evidence-complete after canonical owner transfer with V2 score 9 and owner PLATFORM-SECURITY. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-23969:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-23983:start -->
Maestro Order: A Model-Agnostic Orchestration Harness remains evidence-complete after canonical owner transfer with V2 score 8 and owner AGENT-PLATFORM. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-23983:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-23989:start -->
Faithful by Construction: Claim-Anchored Attribution for Multi-Document Summarization remains evidence-complete after canonical owner transfer with V2 score 7 and owner AGENT-RAG. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-23989:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-24004:start -->
Towards Spec Learning: Inference-Time Alignment from Preference Pairs remains evidence-complete after canonical owner transfer with V2 score 7 and owner TRAIN-RLHF. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-24004:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-24020:start -->
You Don't Need to Run Every Eval remains evidence-complete after canonical owner transfer with V2 score 8 and owner PLATFORM-EVALUATION-SYSTEM. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-24020:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-24033:start -->
RoPE-Aware Bit Allocation for KV-Cache Quantization remains evidence-complete after canonical owner transfer with V2 score 7 and owner INFER-KV-CACHE. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-24033:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-24040:start -->
Towards Version-aware Operations and Transaction Memories for Multi-layer MeMo remains evidence-complete after canonical owner transfer with V2 score 7 and owner AGENT-MEMORY. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-24040:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-24074:start -->
Token Complexity of Certifying Stochastic-Oracle Reliability remains evidence-complete after canonical owner transfer with V2 score 8 and owner PLATFORM-EVALUATION-SYSTEM. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-24074:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-24081:start -->
PixJail: Self-Evolving Paper-to-Pipeline Reproduction for Text-to-Image Jailbreak Evaluation remains evidence-complete after canonical owner transfer with V2 score 8 and owner PLATFORM-EVALUATION-SYSTEM. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-24081:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-24119:start -->
When Top-1 Fails: Calibrating LoRA Monitors for Masked Diffusion LMs remains evidence-complete after canonical owner transfer with V2 score 8 and owner PLATFORM-MONITORING. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-24119:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-24124:start -->
VeryTrace: Verifying Reasoning Traces through Compilable Formalism and Structured Verification remains evidence-complete after canonical owner transfer with V2 score 8 and owner PLATFORM-EVALUATION-SYSTEM. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-24124:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-24133:start -->
Holistic Data Scheduler for LLM Pre-training via Multi-Objective Reinforcement Learning remains evidence-complete after canonical owner transfer with V2 score 7 and owner TRAIN-DATA. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-24133:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-24143:start -->
AsyncOPD: How Stale Can On-Policy Distillation Be? remains evidence-complete after canonical owner transfer with V2 score 9 and owner TRAIN-DISTRIBUTED-TRAINING. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-24143:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-24151:start -->
Metis: Bridging Text and Code Memory for Self-Evolving Agents remains evidence-complete after canonical owner transfer with V2 score 7 and owner AGENT-MEMORY. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-24151:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-24177:start -->
Agon: An Autonomous Large-Scale Omnidisciplinary Research System Built on Prompt Economy remains evidence-complete after canonical owner transfer with V2 score 8 and owner AGENT-WORKFLOW. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-24177:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-24204:start -->
Unified Dominance Graph for Interval-Predicate Approximate Nearest Neighbor Search remains evidence-complete after canonical owner transfer with V2 score 7 and owner AGENT-RAG. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-24204:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-24245:start -->
AutoSpec: Safety Rule Evolution for LLM Agents via Inductive Logic Programming remains evidence-complete after canonical owner transfer with V2 score 9 and owner PLATFORM-SECURITY. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-24245:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-24311:start -->
LemonHarness Technical Report remains evidence-complete after canonical owner transfer with V2 score 8 and owner AGENT-PLATFORM. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-24311:end -->

<!-- analysis:DA-20260624-2606-24322:start -->
入选：memory item 的行动权不再由可篡改 content/lineage 推断，而在 write 时绑定 origin authority；只有 k 个独立 trusted source 才 elevation，高风险 action 缺少 corroborator 时交给 one-time user confirmation。
<!-- analysis:DA-20260624-2606-24322:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-24402:start -->
Poisoned Playbooks: Demystifying Knowledge Poisoning Effects on AI Security Agents remains evidence-complete after canonical owner transfer with V2 score 9 and owner PLATFORM-SECURITY. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-24402:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-24408:start -->
Natural Identifiers for Privacy and Data Audits in Large Language Models remains evidence-complete after canonical owner transfer with V2 score 9 and owner PLATFORM-SECURITY. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-24408:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-24428:start -->
Escaping the Self-Confirmation Trap: An Execute-Distill-Verify Paradigm for Agentic Experience Learning remains evidence-complete after canonical owner transfer with V2 score 7 and owner AGENT-MEMORY. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-24428:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-24437:start -->
ReM-MoA: Reasoning Memory Sustains Mixture-of-Agents Scaling remains evidence-complete after canonical owner transfer with V2 score 7 and owner AGENT-MULTI-AGENT. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-24437:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-24467:start -->
CompressKV: Semantic-Retrieval-Guided KV-Cache Compression for Resource-Efficient Long-Context LLM Inference remains evidence-complete after canonical owner transfer with V2 score 7 and owner INFER-KV-CACHE. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-24467:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-24506:start -->
CrossPool: Efficient Multi-LLM Serving for Cold MoE Models through KV-Cache and Weight Disaggregation remains evidence-complete after canonical owner transfer with V2 score 8 and owner INFER-GPU-MEMORY. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-24506:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-24535:start -->
Governed Shared Memory for Multi-Agent LLM Systems remains evidence-complete after canonical owner transfer with V2 score 7 and owner AGENT-MEMORY. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-24535:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-24551:start -->
GUI vs. CLI: Execution Bottlenecks in Screen-Only and Skill-Mediated Computer-Use Agents remains evidence-complete after canonical owner transfer with V2 score 7 and owner AGENT-TOOL-CALLING. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-24551:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-24598:start -->
Toward Self-Evolution-Ready Workflow Harnesses: A Reversible Migration Path and Convertibility Taxonomy for Expert LLM Pipelines remains evidence-complete after canonical owner transfer with V2 score 9 and owner AGENT-WORKFLOW. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-24598:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-24626:start -->
SAFARI: Scaling Long Horizon Agentic Fault Attribution via Active Investigation remains evidence-complete after canonical owner transfer with V2 score 8 and owner PLATFORM-TRACE. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-24626:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-24722:start -->
Decentralised AI Training and Inference with BlockTrain remains evidence-complete after canonical owner transfer with V2 score 9 and owner TRAIN-DISTRIBUTED-TRAINING. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-24722:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-24774:start -->
Revealing Training Data Exposure in Vision Language Large Models via Parameter Gradients remains evidence-complete after canonical owner transfer with V2 score 9 and owner PLATFORM-SECURITY. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-24774:end -->

<!-- analysis-decision:SF-2026-ARXIV-2606-24775:start -->
Are We Ready For An Agent-Native Memory System? remains evidence-complete after canonical owner transfer with V2 score 7 and owner AGENT-MEMORY. The selected units rank higher on distinct cross-layer state/control impact in this owner window; the full family review remains authoritative and is not reduced by narrative prioritization.
<!-- analysis-decision:SF-2026-ARXIV-2606-24775:end -->

<!-- audit-target:deep_analysis_selection:end -->
<!-- audit-target:books:start -->
## 6. Books Comparison

<!-- validator:books-comparison-v1 -->
| Source Family ID | Stable Node ID | Target Chapter Ref | Adjacent Chapter Refs | Existing Proposition | New Evidence Delta | Evolution Relation | Decision | Books Review Ref |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SF-2026-ARXIV-2606-23740 | TRAIN-RLHF | books/part-04-training-system/31-rlhf.md#L1 | books/part-04-training-system/33-grpo.md#L1 | existing:SF-2026-ARXIV-2606-23740 | delta:SF-2026-ARXIV-2606-23740 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-23740 |
| SF-2026-ARXIV-2606-23743 | INFER-TENSORRT-LLM | books/part-05-inference-system/49-tensorrt-llm.md#L1 | books/part-05-inference-system/50-vllm.md#L1 | existing:SF-2026-ARXIV-2606-23743 | delta:SF-2026-ARXIV-2606-23743 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-23743 |
| SF-2026-ARXIV-2606-23752 | AGENT-MEMORY | books/part-07-agent/77-memory.md#L1 | books/part-07-agent/78-tool-calling.md#L1 | existing:SF-2026-ARXIV-2606-23752 | delta:SF-2026-ARXIV-2606-23752 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-23752 |
| SF-2026-ARXIV-2606-23754 | MULTIMODAL-EMBODIED-VLA | books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md#L1 | books/part-03-multimodal-world-models/25-multimodal-world-models.md#L1 | existing:SF-2026-ARXIV-2606-23754 | delta:SF-2026-ARXIV-2606-23754 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-23754 |
| SF-2026-ARXIV-2606-23768 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#L1 | books/part-06-ai-infrastructure/73-production-best-practice.md#L1 | existing:SF-2026-ARXIV-2606-23768 | delta:SF-2026-ARXIV-2606-23768 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-23768 |
| SF-2026-ARXIV-2606-23797 | AGENT-WORKFLOW | books/part-07-agent/81-workflow.md#L1 | books/part-07-agent/82-multi-agent.md#L1 | existing:SF-2026-ARXIV-2606-23797 | delta:SF-2026-ARXIV-2606-23797 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-23797 |
| SF-2026-ARXIV-2606-23858 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#L1 | books/part-06-ai-infrastructure/73-production-best-practice.md#L1 | existing:SF-2026-ARXIV-2606-23858 | delta:SF-2026-ARXIV-2606-23858 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-23858 |
| SF-2026-ARXIV-2606-23872 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#L1 | books/part-06-ai-infrastructure/73-production-best-practice.md#L1 | existing:SF-2026-ARXIV-2606-23872 | delta:SF-2026-ARXIV-2606-23872 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-23872 |
| SF-2026-ARXIV-2606-23892 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#L1 | books/part-06-ai-infrastructure/73-production-best-practice.md#L1 | existing:SF-2026-ARXIV-2606-23892 | delta:SF-2026-ARXIV-2606-23892 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-23892 |
| SF-2026-ARXIV-2606-23915 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#L1 | books/part-06-ai-infrastructure/67-monitoring.md#L1 | existing:SF-2026-ARXIV-2606-23915 | delta:SF-2026-ARXIV-2606-23915 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-23915 |
| SF-2026-ARXIV-2606-23927 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#L1 | books/part-06-ai-infrastructure/73-production-best-practice.md#L1 | existing:SF-2026-ARXIV-2606-23927 | delta:SF-2026-ARXIV-2606-23927 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-23927 |
| SF-2026-ARXIV-2606-23937 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#L1 | books/part-06-ai-infrastructure/67-monitoring.md#L1 | existing:SF-2026-ARXIV-2606-23937 | delta:SF-2026-ARXIV-2606-23937 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-23937 |
| SF-2026-ARXIV-2606-23961 | INFER-KV-CACHE | books/part-05-inference-system/45-why-kv-cache-speeds-up.md#L1 | books/part-05-inference-system/46-continuous-batching.md#L1 | existing:SF-2026-ARXIV-2606-23961 | delta:SF-2026-ARXIV-2606-23961 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-23961 |
| SF-2026-ARXIV-2606-23969 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#L1 | books/part-06-ai-infrastructure/73-production-best-practice.md#L1 | existing:SF-2026-ARXIV-2606-23969 | delta:SF-2026-ARXIV-2606-23969 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-23969 |
| SF-2026-ARXIV-2606-23983 | AGENT-PLATFORM | books/part-07-agent/84-agent-platform.md#L1 | books/part-07-agent/83-mcp.md#L1 | existing:SF-2026-ARXIV-2606-23983 | delta:SF-2026-ARXIV-2606-23983 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-23983 |
| SF-2026-ARXIV-2606-23989 | AGENT-RAG | books/part-07-agent/76-rag.md#L1 | books/part-07-agent/77-memory.md#L1 | existing:SF-2026-ARXIV-2606-23989 | delta:SF-2026-ARXIV-2606-23989 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-23989 |
| SF-2026-ARXIV-2606-24004 | TRAIN-RLHF | books/part-04-training-system/31-rlhf.md#L1 | books/part-04-training-system/32-ppo.md#L1 | existing:SF-2026-ARXIV-2606-24004 | delta:SF-2026-ARXIV-2606-24004 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-24004 |
| SF-2026-ARXIV-2606-24020 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#L1 | books/part-06-ai-infrastructure/67-monitoring.md#L1 | existing:SF-2026-ARXIV-2606-24020 | delta:SF-2026-ARXIV-2606-24020 | Principle Reuse | No Change — Existing Coverage | books-review:SF-2026-ARXIV-2606-24020 |
| SF-2026-ARXIV-2606-24033 | INFER-KV-CACHE | books/part-05-inference-system/45-why-kv-cache-speeds-up.md#L1 | books/part-05-inference-system/46-continuous-batching.md#L1 | existing:SF-2026-ARXIV-2606-24033 | delta:SF-2026-ARXIV-2606-24033 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-24033 |
| SF-2026-ARXIV-2606-24040 | AGENT-MEMORY | books/part-07-agent/77-memory.md#L1 | books/part-07-agent/78-tool-calling.md#L1 | existing:SF-2026-ARXIV-2606-24040 | delta:SF-2026-ARXIV-2606-24040 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-24040 |
| SF-2026-ARXIV-2606-24074 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#L1 | books/part-06-ai-infrastructure/67-monitoring.md#L1 | existing:SF-2026-ARXIV-2606-24074 | delta:SF-2026-ARXIV-2606-24074 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-24074 |
| SF-2026-ARXIV-2606-24081 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#L1 | books/part-06-ai-infrastructure/67-monitoring.md#L1 | existing:SF-2026-ARXIV-2606-24081 | delta:SF-2026-ARXIV-2606-24081 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-24081 |
| SF-2026-ARXIV-2606-24119 | PLATFORM-MONITORING | books/part-06-ai-infrastructure/67-monitoring.md#L1 | books/part-06-ai-infrastructure/66-evaluation-system.md#L1 | existing:SF-2026-ARXIV-2606-24119 | delta:SF-2026-ARXIV-2606-24119 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-24119 |
| SF-2026-ARXIV-2606-24124 | PLATFORM-EVALUATION-SYSTEM | books/part-06-ai-infrastructure/66-evaluation-system.md#L1 | books/part-06-ai-infrastructure/67-monitoring.md#L1 | existing:SF-2026-ARXIV-2606-24124 | delta:SF-2026-ARXIV-2606-24124 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-24124 |
| SF-2026-ARXIV-2606-24133 | TRAIN-DATA | books/part-04-training-system/27-data.md#L1 | books/part-04-training-system/28-pretraining.md#L1 | existing:SF-2026-ARXIV-2606-24133 | delta:SF-2026-ARXIV-2606-24133 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-24133 |
| SF-2026-ARXIV-2606-24143 | TRAIN-DISTRIBUTED-TRAINING | books/part-04-training-system/36-distributed-training.md#L1 | books/part-04-training-system/38-pipeline-parallel.md#L1 | existing:SF-2026-ARXIV-2606-24143 | delta:SF-2026-ARXIV-2606-24143 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-24143 |
| SF-2026-ARXIV-2606-24151 | AGENT-MEMORY | books/part-07-agent/77-memory.md#L1 | books/part-07-agent/76-rag.md#L1 | existing:SF-2026-ARXIV-2606-24151 | delta:SF-2026-ARXIV-2606-24151 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-24151 |
| SF-2026-ARXIV-2606-24177 | AGENT-WORKFLOW | books/part-07-agent/81-workflow.md#L1 | books/part-07-agent/82-multi-agent.md#L1 | existing:SF-2026-ARXIV-2606-24177 | delta:SF-2026-ARXIV-2606-24177 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-24177 |
| SF-2026-ARXIV-2606-24204 | AGENT-RAG | books/part-07-agent/76-rag.md#L1 | books/part-07-agent/77-memory.md#L1 | existing:SF-2026-ARXIV-2606-24204 | delta:SF-2026-ARXIV-2606-24204 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-24204 |
| SF-2026-ARXIV-2606-24245 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#L1 | books/part-06-ai-infrastructure/73-production-best-practice.md#L1 | existing:SF-2026-ARXIV-2606-24245 | delta:SF-2026-ARXIV-2606-24245 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-24245 |
| SF-2026-ARXIV-2606-24311 | AGENT-PLATFORM | books/part-07-agent/84-agent-platform.md#L1 | books/part-07-agent/83-mcp.md#L1 | existing:SF-2026-ARXIV-2606-24311 | delta:SF-2026-ARXIV-2606-24311 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-24311 |
| SF-2026-ARXIV-2606-24322 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#L1 | books/part-06-ai-infrastructure/73-production-best-practice.md#L1 | existing:SF-2026-ARXIV-2606-24322 | delta:SF-2026-ARXIV-2606-24322 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-24322 |
| SF-2026-ARXIV-2606-24402 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#L1 | books/part-06-ai-infrastructure/73-production-best-practice.md#L1 | existing:SF-2026-ARXIV-2606-24402 | delta:SF-2026-ARXIV-2606-24402 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-24402 |
| SF-2026-ARXIV-2606-24408 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#L1 | books/part-06-ai-infrastructure/73-production-best-practice.md#L1 | existing:SF-2026-ARXIV-2606-24408 | delta:SF-2026-ARXIV-2606-24408 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-24408 |
| SF-2026-ARXIV-2606-24428 | AGENT-MEMORY | books/part-07-agent/77-memory.md#L1 | books/part-07-agent/76-rag.md#L1 | existing:SF-2026-ARXIV-2606-24428 | delta:SF-2026-ARXIV-2606-24428 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-24428 |
| SF-2026-ARXIV-2606-24437 | AGENT-MULTI-AGENT | books/part-07-agent/82-multi-agent.md#L1 | books/part-07-agent/81-workflow.md#L1 | existing:SF-2026-ARXIV-2606-24437 | delta:SF-2026-ARXIV-2606-24437 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-24437 |
| SF-2026-ARXIV-2606-24467 | INFER-KV-CACHE | books/part-05-inference-system/45-why-kv-cache-speeds-up.md#L1 | books/part-05-inference-system/47-pagedattention.md#L1 | existing:SF-2026-ARXIV-2606-24467 | delta:SF-2026-ARXIV-2606-24467 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-24467 |
| SF-2026-ARXIV-2606-24506 | INFER-GPU-MEMORY | books/part-05-inference-system/54-gpu-memory.md#L1 | books/part-05-inference-system/55-pd-disaggregation.md#L1 | existing:SF-2026-ARXIV-2606-24506 | delta:SF-2026-ARXIV-2606-24506 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-24506 |
| SF-2026-ARXIV-2606-24535 | AGENT-MEMORY | books/part-07-agent/77-memory.md#L1 | books/part-07-agent/76-rag.md#L1 | existing:SF-2026-ARXIV-2606-24535 | delta:SF-2026-ARXIV-2606-24535 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-24535 |
| SF-2026-ARXIV-2606-24551 | AGENT-TOOL-CALLING | books/part-07-agent/78-tool-calling.md#L1 | books/part-07-agent/79-planning.md#L1 | existing:SF-2026-ARXIV-2606-24551 | delta:SF-2026-ARXIV-2606-24551 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-24551 |
| SF-2026-ARXIV-2606-24598 | AGENT-WORKFLOW | books/part-07-agent/81-workflow.md#L1 | books/part-07-agent/79-planning.md#L1; books/part-07-agent/82-multi-agent.md#L1 | existing:SF-2026-ARXIV-2606-24598 | delta:SF-2026-ARXIV-2606-24598 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-24598 |
| SF-2026-ARXIV-2606-24626 | PLATFORM-TRACE | books/part-06-ai-infrastructure/69-trace.md#L1 | books/part-06-ai-infrastructure/67-monitoring.md#L1 | existing:SF-2026-ARXIV-2606-24626 | delta:SF-2026-ARXIV-2606-24626 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-24626 |
| SF-2026-ARXIV-2606-24722 | TRAIN-DISTRIBUTED-TRAINING | books/part-04-training-system/36-distributed-training.md#L1 | books/part-04-training-system/38-pipeline-parallel.md#L1 | existing:SF-2026-ARXIV-2606-24722 | delta:SF-2026-ARXIV-2606-24722 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-24722 |
| SF-2026-ARXIV-2606-24774 | PLATFORM-SECURITY | books/part-06-ai-infrastructure/72-security.md#L1 | books/part-06-ai-infrastructure/73-production-best-practice.md#L1 | existing:SF-2026-ARXIV-2606-24774 | delta:SF-2026-ARXIV-2606-24774 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-24774 |
| SF-2026-ARXIV-2606-24775 | AGENT-MEMORY | books/part-07-agent/77-memory.md#L1 | books/part-07-agent/76-rag.md#L1 | existing:SF-2026-ARXIV-2606-24775 | delta:SF-2026-ARXIV-2606-24775 | Direct Evolution | Integrate | books-review:SF-2026-ARXIV-2606-24775 |

<!-- existing:SF-2026-ARXIV-2606-23740:start -->
`books/part-04-training-system/31-rlhf.md` current sha256=85b3534f4f09d5a7; target and adjacent re-opened before disposition.
<!-- existing:SF-2026-ARXIV-2606-23740:end -->

<!-- delta:SF-2026-ARXIV-2606-23740:start -->
offline reasoning training 的方法差异要同时看 weight-space trajectory、data/step/LR matching 与功能结果；几何分离若训练预算不匹配不能归因于 objective。
<!-- delta:SF-2026-ARXIV-2606-23740:end -->

<!-- books-review:SF-2026-ARXIV-2606-23740:start -->
Unique owner `TRAIN-RLHF`; adjacent `books/part-04-training-system/33-grpo.md#L1`; relation `Direct Evolution`; disposition `Integrate`. Current target and adjacent were re-opened before this decision.
<!-- books-review:SF-2026-ARXIV-2606-23740:end -->

<!-- existing:SF-2026-ARXIV-2606-23743:start -->
`books/part-05-inference-system/49-tensorrt-llm.md` current sha256=b2ffc70e9874fb1a; target and adjacent re-opened before disposition.
<!-- existing:SF-2026-ARXIV-2606-23743:end -->

<!-- delta:SF-2026-ARXIV-2606-23743:start -->
video inference optimization 应把 graph transformation、kernel/execution plan、memory schedule 与 serving config 绑定同一可重建 artifact；agent 只能提出/搜索 plan，validator 才能提交。
<!-- delta:SF-2026-ARXIV-2606-23743:end -->

<!-- books-review:SF-2026-ARXIV-2606-23743:start -->
Unique owner `INFER-TENSORRT-LLM`; adjacent `books/part-05-inference-system/50-vllm.md#L1`; relation `Direct Evolution`; disposition `Integrate`. Current target and adjacent were re-opened before this decision.
<!-- books-review:SF-2026-ARXIV-2606-23743:end -->

<!-- existing:SF-2026-ARXIV-2606-23752:start -->
`books/part-07-agent/77-memory.md` 的唯一 owner 已承载相关机制链；`books/part-07-agent/78-tool-calling.md#L1` 只消费 handoff。
<!-- existing:SF-2026-ARXIV-2606-23752:end -->

<!-- delta:SF-2026-ARXIV-2606-23752:start -->
ESAA-Conversational: An Event-Sourced Memory Layer for Continuity, Handoff, and Curation Across Heterogeneous LLM Coding Agents 的 exact-v1 机制为：Each agent, however, persists its conversation in a private and vendor-specific log. 因此 把事件时间、来源、有效条件、版本、检索决策与写入 authority 分开。
<!-- delta:SF-2026-ARXIV-2606-23752:end -->

<!-- books-review:SF-2026-ARXIV-2606-23752:start -->
Unique owner `AGENT-MEMORY`; adjacent non-owner `books/part-07-agent/78-tool-calling.md#L1`; relation `Direct Evolution`; disposition `Integrate`. 该 family 的 failure pressure 是：Each agent, however, persists its conversation in a private and vendor-specific log. 披露的 evaluation signal 是：The result is conversational state drift: goals, decisions, open tasks, and rationales established with one agent are not reliably available when another agent takes over. 证据只支持 exact-v1 在披露 workload/model/hardware 范围内的机制与结果，不证明生产尾部、未测分布或形式安全；来源/时间/版本不足时隔离 candidate memory，保留原始轨迹且禁止自动覆盖。旧路径在其原约束成立时继续共存。
<!-- books-review:SF-2026-ARXIV-2606-23752:end -->

<!-- existing:SF-2026-ARXIV-2606-23754:start -->
`books/part-03-multimodal-world-models/26-multimodal-embodied-vla.md` 的唯一 owner 已承载相关机制链；`books/part-03-multimodal-world-models/25-multimodal-world-models.md#L1` 只消费 handoff。
<!-- existing:SF-2026-ARXIV-2606-23754:end -->

<!-- delta:SF-2026-ARXIV-2606-23754:start -->
Verifiable Foundation Models for Robot Safety 的 exact-v1 机制为：In this paper, we present FEARL (Foundation-Enabled Assured Robot Learning), a framework that addresses this tension through a modular architectural decomposition. 因此 把 observation、temporal state、action head、safety gate 与真实动作回执绑定。
<!-- delta:SF-2026-ARXIV-2606-23754:end -->

<!-- books-review:SF-2026-ARXIV-2606-23754:start -->
Unique owner `MULTIMODAL-EMBODIED-VLA`; adjacent non-owner `books/part-03-multimodal-world-models/25-multimodal-world-models.md#L1`; relation `Principle Reuse`; disposition `No Change — Existing Coverage`. 该 family 的 failure pressure 是：Deploying foundation models for robot control raises a central challenge: the expressive power that enables rich, multimodal perception also makes these models opaque and difficult to analyze formally, rendering them intractable for existing verification tools. 披露的 evaluation signal 是：To show that the decomposed policy remains capable of solving diverse tasks, we evaluate FEARL on three simulated robotic domains using multiple Controller backbones and training procedures, including pretrained off-the-shelf vision-language-action models. 证据只支持 exact-v1 在披露 workload/model/hardware 范围内的机制与结果，不证明生产尾部、未测分布或形式安全；观测或动作接口不一致时拒绝物理提交并交回保守 controller/人工。旧路径在其原约束成立时继续共存。
<!-- books-review:SF-2026-ARXIV-2606-23754:end -->

<!-- existing:SF-2026-ARXIV-2606-23768:start -->
`books/part-06-ai-infrastructure/72-security.md` 的唯一 owner 已承载相关机制链；`books/part-06-ai-infrastructure/73-production-best-practice.md#L1` 只消费 handoff。
<!-- existing:SF-2026-ARXIV-2606-23768:end -->

<!-- delta:SF-2026-ARXIV-2606-23768:start -->
Cryptographic certificates of validity for trustworthy AI 的 exact-v1 机制为：We propose cryptographic certificates of validity for agentic AI systems. 因此 把 attacker、policy、runtime data/control flow、proof boundary 与 fail-closed handoff 显式化。
<!-- delta:SF-2026-ARXIV-2606-23768:end -->

<!-- books-review:SF-2026-ARXIV-2606-23768:start -->
Unique owner `PLATFORM-SECURITY`; adjacent non-owner `books/part-06-ai-infrastructure/73-production-best-practice.md#L1`; relation `Principle Reuse`; disposition `No Change — Existing Coverage`. 该 family 的 failure pressure 是：We propose cryptographic certificates of validity for agentic AI systems. 披露的 evaluation signal 是：We outline the approach at a high level, give the core mathematical translation, relate the proposal to proof-carrying code, zkVMs, formal methods, and agent governance, and note the specification, auditing, and deployment questions that a full implementation must answer. 证据只支持 exact-v1 在披露 workload/model/hardware 范围内的机制与结果，不证明生产尾部、未测分布或形式安全；证据、policy 或证明前提不满足时 fail closed 并交回独立 reference monitor。旧路径在其原约束成立时继续共存。
<!-- books-review:SF-2026-ARXIV-2606-23768:end -->

<!-- existing:SF-2026-ARXIV-2606-23797:start -->
`books/part-07-agent/81-workflow.md` 的唯一 owner 已承载相关机制链；`books/part-07-agent/82-multi-agent.md#L1` 只消费 handoff。
<!-- existing:SF-2026-ARXIV-2606-23797:end -->

<!-- delta:SF-2026-ARXIV-2606-23797:start -->
From Task-Guided Conversational Graphs to Goal-Oriented Dialogue Runtimes 的 exact-v1 机制为：We introduce the Goal-Oriented Dialogue Runtime (GODR), a framework-neutral design pattern that treats goals, task frames, lifecycle state, invalidation rules, and resumption contracts as first-class runtime objects while delegating bounded execution to graph runtimes, agents, tools, or application programming interfaces (APIs). 因此 把执行边、依赖边、checkpoint 与 compensation 作为可重放 control state。
<!-- delta:SF-2026-ARXIV-2606-23797:end -->

<!-- books-review:SF-2026-ARXIV-2606-23797:start -->
Unique owner `AGENT-WORKFLOW`; adjacent non-owner `books/part-07-agent/82-multi-agent.md#L1`; relation `Direct Evolution`; disposition `Integrate`. 该 family 的 failure pressure 是：Graph and multi-agent orchestration frameworks make production large language model (LLM) workflows practical, but they do not by themselves solve conversational continuity when users maintain several interdependent objectives. 披露的 evaluation signal 是：The paper formalizes the problem, proposes runtime objects and architecture-selection criteria, and frames evaluation as an agenda for future empirical validation rather than as a measured performance claim. 证据只支持 exact-v1 在披露 workload/model/hardware 范围内的机制与结果，不证明生产尾部、未测分布或形式安全；前提、identity 或预算越界时停止新路径，回退到该 owner 已验证的旧路径并保留失败回执。旧路径在其原约束成立时继续共存。
<!-- books-review:SF-2026-ARXIV-2606-23797:end -->

<!-- existing:SF-2026-ARXIV-2606-23858:start -->
`books/part-06-ai-infrastructure/72-security.md` 的唯一 owner 已承载相关机制链；`books/part-06-ai-infrastructure/73-production-best-practice.md#L1` 只消费 handoff。
<!-- existing:SF-2026-ARXIV-2606-23858:end -->

<!-- delta:SF-2026-ARXIV-2606-23858:start -->
Are Safety Guarantees in Neural Networks Safe? How to Compute Trustworthy Robustness Certifications 的 exact-v1 机制为：We introduce the apothem measure and show how to compute apothem-optimal certifications in a linear number of calls to a NN verifier (oracle) w.r.t. 因此 把 attacker、policy、runtime data/control flow、proof boundary 与 fail-closed handoff 显式化。
<!-- delta:SF-2026-ARXIV-2606-23858:end -->

<!-- books-review:SF-2026-ARXIV-2606-23858:start -->
Unique owner `PLATFORM-SECURITY`; adjacent non-owner `books/part-06-ai-infrastructure/73-production-best-practice.md#L1`; relation `Principle Reuse`; disposition `No Change — Existing Coverage`. 该 family 的 failure pressure 是：A primary challenge in AI safety is the existence of adversarial examples -- slightly distorted inputs that cause a neural network (NN) to misclassify. 披露的 evaluation signal 是：Most existing approaches focus on maximizing the certification's volume, but recent intractability results prohibit the computation of volume-optimal certifications in reasonable time. 证据只支持 exact-v1 在披露 workload/model/hardware 范围内的机制与结果，不证明生产尾部、未测分布或形式安全；证据、policy 或证明前提不满足时 fail closed 并交回独立 reference monitor。旧路径在其原约束成立时继续共存。
<!-- books-review:SF-2026-ARXIV-2606-23858:end -->

<!-- existing:SF-2026-ARXIV-2606-23872:start -->
`books/part-06-ai-infrastructure/72-security.md` 的唯一 owner 已承载相关机制链；`books/part-06-ai-infrastructure/73-production-best-practice.md#L1` 只消费 handoff。
<!-- existing:SF-2026-ARXIV-2606-23872:end -->

<!-- delta:SF-2026-ARXIV-2606-23872:start -->
MGI: Member vs Generated Inference 的 exact-v1 机制为：To address MGI, we propose Data Circuit Breaker (DCB), a three-stage method that combines complementary signals from a generative model's autoencoder and latent generator to distinguish training members from generated samples. 因此 把 attacker、policy、runtime data/control flow、proof boundary 与 fail-closed handoff 显式化。
<!-- delta:SF-2026-ARXIV-2606-23872:end -->

<!-- books-review:SF-2026-ARXIV-2606-23872:start -->
Unique owner `PLATFORM-SECURITY`; adjacent non-owner `books/part-06-ai-infrastructure/73-production-best-practice.md#L1`; relation `Principle Reuse`; disposition `No Change — Existing Coverage`. 该 family 的 failure pressure 是：We formalize this challenge as Member vs Generated Inference (MGI): given a sample and a target generative model, infer whether the sample is a true training member or a generated output of that model. 披露的 evaluation signal 是：Focusing on image generation, we show that existing membership inference methods systematically misclassify generated samples as training members, while attribution-based methods often misclassify true members as generated. 证据只支持 exact-v1 在披露 workload/model/hardware 范围内的机制与结果，不证明生产尾部、未测分布或形式安全；证据、policy 或证明前提不满足时 fail closed 并交回独立 reference monitor。旧路径在其原约束成立时继续共存。
<!-- books-review:SF-2026-ARXIV-2606-23872:end -->

<!-- existing:SF-2026-ARXIV-2606-23892:start -->
`books/part-06-ai-infrastructure/72-security.md` 的唯一 owner 已承载相关机制链；`books/part-06-ai-infrastructure/73-production-best-practice.md#L1` 只消费 handoff。
<!-- existing:SF-2026-ARXIV-2606-23892:end -->

<!-- delta:SF-2026-ARXIV-2606-23892:start -->
REALM: A Unified Red-Teaming Benchmark for Physical-World VLMs 的 exact-v1 机制为：We introduce REALM, to our knowledge the first unified red-teaming benchmark for physical-world VLMs. 因此 把 attacker、policy、runtime data/control flow、proof boundary 与 fail-closed handoff 显式化。
<!-- delta:SF-2026-ARXIV-2606-23892:end -->

<!-- books-review:SF-2026-ARXIV-2606-23892:start -->
Unique owner `PLATFORM-SECURITY`; adjacent non-owner `books/part-06-ai-infrastructure/73-production-best-practice.md#L1`; relation `Principle Reuse`; disposition `No Change — Existing Coverage`. 该 family 的 failure pressure 是：Although many red-teaming methods have been developed to probe VLM vulnerabilities, their evaluation remains fragmented across datasets, metrics, and threat models, making direct comparison difficult and obscuring whether observed differences arise from stronger attacks, more vulnerable models, or incompatible evaluation settings. 披露的 evaluation signal 是：Although many red-teaming methods have been developed to probe VLM vulnerabilities, their evaluation remains fragmented across datasets, metrics, and threat models, making direct comparison difficult and obscuring whether observed differences arise from stronger attacks, more vulnerable models, or incompatible evaluation settings. 证据只支持 exact-v1 在披露 workload/model/hardware 范围内的机制与结果，不证明生产尾部、未测分布或形式安全；证据、policy 或证明前提不满足时 fail closed 并交回独立 reference monitor。旧路径在其原约束成立时继续共存。
<!-- books-review:SF-2026-ARXIV-2606-23892:end -->

<!-- existing:SF-2026-ARXIV-2606-23915:start -->
`books/part-06-ai-infrastructure/66-evaluation-system.md` 的唯一 owner 已承载相关机制链；`books/part-06-ai-infrastructure/67-monitoring.md#L1` 只消费 handoff。
<!-- existing:SF-2026-ARXIV-2606-23915:end -->

<!-- delta:SF-2026-ARXIV-2606-23915:start -->
Do LLM Attribution Metrics Transfer? Auditing Retrieval-Augmented Generation Evaluation Across Datasets and Constructs 的 exact-v1 机制为：We audit eight automatic scorers -- lexical, embedding, and BERTScore baselines alongside entailment/grounding-trained models (clean and FEVER NLI, the checker MiniCheck) -- across three evaluation constructs (provenance/topicality, generated-answer attribution, and fact-check entailment), asking whether any scorer transfers: stays within the 95% confidence interval of the best audited scorer on every dataset of a multi-dataset construct. 因此 把样本、metric、judge、阈值、不确定性和 release authority 分离。
<!-- delta:SF-2026-ARXIV-2606-23915:end -->

<!-- books-review:SF-2026-ARXIV-2606-23915:start -->
Unique owner `PLATFORM-EVALUATION-SYSTEM`; adjacent non-owner `books/part-06-ai-infrastructure/67-monitoring.md#L1`; relation `Principle Reuse`; disposition `No Change — Existing Coverage`. 该 family 的 failure pressure 是：This instability has a concrete decision cost: a naive "best-on-average" rule for choosing an evaluator fails leave-one-dataset-out (mean held-out regret 0.172 AUROC, worse than fixing one scorer), so metric choice must be validated on the target dataset rather than learned from others. 披露的 evaluation signal 是：We audit eight automatic scorers -- lexical, embedding, and BERTScore baselines alongside entailment/grounding-trained models (clean and FEVER NLI, the checker MiniCheck) -- across three evaluation constructs (provenance/topicality, generated-answer attribution, and fact-check entailment), asking whether any scorer transfers: stays within the 95% confidence interval of the best audited scorer on every dataset of a multi-dataset construct. 证据只支持 exact-v1 在披露 workload/model/hardware 范围内的机制与结果，不证明生产尾部、未测分布或形式安全；metric、judge 或样本假设失效时保持 release Gate Open 并恢复完整评估。旧路径在其原约束成立时继续共存。
<!-- books-review:SF-2026-ARXIV-2606-23915:end -->

<!-- existing:SF-2026-ARXIV-2606-23927:start -->
`books/part-06-ai-infrastructure/72-security.md` 的唯一 owner 已承载相关机制链；`books/part-06-ai-infrastructure/73-production-best-practice.md#L1` 只消费 handoff。
<!-- existing:SF-2026-ARXIV-2606-23927:end -->

<!-- delta:SF-2026-ARXIV-2606-23927:start -->
RIFT-Bench: Dynamic Red-teaming For Agentic AI Systems 的 exact-v1 机制为：To address this gap, we introduce RIFT-Bench, a graph representation-driven methodology for dynamic red-teaming that enables unified evaluations across diverse agentic architectures. 因此 把 attacker、policy、runtime data/control flow、proof boundary 与 fail-closed handoff 显式化。
<!-- delta:SF-2026-ARXIV-2606-23927:end -->

<!-- books-review:SF-2026-ARXIV-2606-23927:start -->
Unique owner `PLATFORM-SECURITY`; adjacent non-owner `books/part-06-ai-infrastructure/73-production-best-practice.md#L1`; relation `Principle Reuse`; disposition `No Change — Existing Coverage`. 该 family 的 failure pressure 是：Agentic AI systems powered by large language models (LLMs) are rapidly evolving into autonomous decision-making systems, exposing attack vectors beyond those of traditional LLM vulnerabilities. 披露的 evaluation signal 是：Existing security evaluations are often tied to specific implementations or domains, limiting unified comparison across heterogeneous systems. 证据只支持 exact-v1 在披露 workload/model/hardware 范围内的机制与结果，不证明生产尾部、未测分布或形式安全；证据、policy 或证明前提不满足时 fail closed 并交回独立 reference monitor。旧路径在其原约束成立时继续共存。
<!-- books-review:SF-2026-ARXIV-2606-23927:end -->

<!-- existing:SF-2026-ARXIV-2606-23937:start -->
`books/part-06-ai-infrastructure/66-evaluation-system.md` 的唯一 owner 已承载相关机制链；`books/part-06-ai-infrastructure/67-monitoring.md#L1` 只消费 handoff。
<!-- existing:SF-2026-ARXIV-2606-23937:end -->

<!-- delta:SF-2026-ARXIV-2606-23937:start -->
When Retrieval Metrics Mislead: Measuring Policy Signal in Long-Horizon Tool-Use Agents 的 exact-v1 机制为：We test this proxy for pre-action policy classification in tau-bench using Qwen2.5-3B/7B classifiers. 因此 把样本、metric、judge、阈值、不确定性和 release authority 分离。
<!-- delta:SF-2026-ARXIV-2606-23937:end -->

<!-- books-review:SF-2026-ARXIV-2606-23937:start -->
Unique owner `PLATFORM-EVALUATION-SYSTEM`; adjacent non-owner `books/part-06-ai-infrastructure/67-monitoring.md#L1`; relation `Principle Reuse`; disposition `No Change — Existing Coverage`. 该 family 的 failure pressure 是：Although the exact governing clause is retrieved at rank 1 for only 7% of airline states, the primary 3B classifier obtains macro-F1 0.58 with retrieved clauses versus 0.60 with gold clauses (Delta=-0.02, task-cluster 95% CI [-0.23,+0.21]); mismatched-policy and no-policy controls score 0.32 and 0.21. 披露的 evaluation signal 是：Under gold-policy conditioning, a compact structured state improves macro-F1 over raw trajectories by 0.13-0.17 after tuning. 证据只支持 exact-v1 在披露 workload/model/hardware 范围内的机制与结果，不证明生产尾部、未测分布或形式安全；metric、judge 或样本假设失效时保持 release Gate Open 并恢复完整评估。旧路径在其原约束成立时继续共存。
<!-- books-review:SF-2026-ARXIV-2606-23937:end -->

<!-- existing:SF-2026-ARXIV-2606-23961:start -->
`books/part-05-inference-system/45-why-kv-cache-speeds-up.md` 的唯一 owner 已承载相关机制链；`books/part-05-inference-system/46-continuous-batching.md#L1` 只消费 handoff。
<!-- existing:SF-2026-ARXIV-2606-23961:end -->

<!-- delta:SF-2026-ARXIV-2606-23961:start -->
Forget Without Compromise: Nexus Sampling for Streaming KV-Cache Eviction Under Fixed Budgets 的 exact-v1 机制为：To address this challenge, we propose Nexus Sampling, a training-free eviction method that pairs Nexus scoring, an iterative walk over direct attention that surfaces bridge tokens, with weighted reservoir sampling, which retains tokens with inclusion probability in place of deterministic top-$K$. 因此 把 cache position、eviction/quantization policy、跨模态 identity 与 dense recompute fallback 绑定。
<!-- delta:SF-2026-ARXIV-2606-23961:end -->

<!-- books-review:SF-2026-ARXIV-2606-23961:start -->
Unique owner `INFER-KV-CACHE`; adjacent non-owner `books/part-05-inference-system/46-continuous-batching.md#L1`; relation `Direct Evolution`; disposition `Integrate`. 该 family 的 failure pressure 是：To address this challenge, we propose Nexus Sampling, a training-free eviction method that pairs Nexus scoring, an iterative walk over direct attention that surfaces bridge tokens, with weighted reservoir sampling, which retains tokens with inclusion probability in place of deterministic top-$K$. 披露的 evaluation signal 是：Theoretically, we show that Nexus Sampling dominates deterministic top-$K$ in long-run survival of subtly important tokens. 证据只支持 exact-v1 在披露 workload/model/hardware 范围内的机制与结果，不证明生产尾部、未测分布或形式安全；cache identity 或误差预算失配时清空该路径并回到未压缩/重算 KV。旧路径在其原约束成立时继续共存。
<!-- books-review:SF-2026-ARXIV-2606-23961:end -->

<!-- existing:SF-2026-ARXIV-2606-23969:start -->
`books/part-06-ai-infrastructure/72-security.md` 的唯一 owner 已承载相关机制链；`books/part-06-ai-infrastructure/73-production-best-practice.md#L1` 只消费 handoff。
<!-- existing:SF-2026-ARXIV-2606-23969:end -->

<!-- delta:SF-2026-ARXIV-2606-23969:start -->
The Serialized Bridge: Understanding and Recovering LLM Serving Performance under Blackwell GPU Confidential Computing 的 exact-v1 机制为：Yet LLM serving under Intel TDX plus GPU-CC still loses 13-27% of throughput, and KV-cache restore latency can more than double. 因此 把 attacker、policy、runtime data/control flow、proof boundary 与 fail-closed handoff 显式化。
<!-- delta:SF-2026-ARXIV-2606-23969:end -->

<!-- books-review:SF-2026-ARXIV-2606-23969:start -->
Unique owner `PLATFORM-SECURITY`; adjacent non-owner `books/part-06-ai-infrastructure/73-production-best-practice.md#L1`; relation `Direct Evolution`; disposition `Integrate`. 该 family 的 failure pressure 是：We find that GPU-CC turns host/device movement into a serialized, high-setup-cost channel. 披露的 evaluation signal 是：We qualify confidential multi-GPU NVSwitch tenants on B300, including 510 GB/s NVLink P2P inside a CVM and concurrent isolated tenants, and identify the remaining fabric-attestation gap for production confidential AI platforms. 证据只支持 exact-v1 在披露 workload/model/hardware 范围内的机制与结果，不证明生产尾部、未测分布或形式安全；证据、policy 或证明前提不满足时 fail closed 并交回独立 reference monitor。旧路径在其原约束成立时继续共存。
<!-- books-review:SF-2026-ARXIV-2606-23969:end -->

<!-- existing:SF-2026-ARXIV-2606-23983:start -->
`books/part-07-agent/84-agent-platform.md` 的唯一 owner 已承载相关机制链；`books/part-07-agent/83-mcp.md#L1` 只消费 handoff。
<!-- existing:SF-2026-ARXIV-2606-23983:end -->

<!-- delta:SF-2026-ARXIV-2606-23983:start -->
Maestro Order: A Model-Agnostic Orchestration Harness 的 exact-v1 机制为：We present Maestro Order, a model-agnostic orchestration harness that turns unreliable solvers into reliable problem-solving systems by composing them according to four structural primitives (decompose, ensemble, verify, and recurse) and a budget-aware controller that decides where to spend compute. 因此 把模型/工具/资源路由、OS harness、隔离边界与 outcome receipt 作为平台责任。
<!-- delta:SF-2026-ARXIV-2606-23983:end -->

<!-- books-review:SF-2026-ARXIV-2606-23983:start -->
Unique owner `AGENT-PLATFORM`; adjacent non-owner `books/part-07-agent/83-mcp.md#L1`; relation `Direct Evolution`; disposition `Integrate`. 该 family 的 failure pressure 是：The harness treats any model as a black-box base solver behind a uniform interface, layers a verifier ensemble whose discrimination is measured online, and allocates verification and voting to the stages with the highest marginal reliability per unit cost. 披露的 evaluation signal 是：We then specify an evaluation methodology (reliability at fixed cost, coverage, calibration, and ablations) and report results from a faithful Monte Carlo simulation of the harness over a parameterized solver/verifier model. 证据只支持 exact-v1 在披露 workload/model/hardware 范围内的机制与结果，不证明生产尾部、未测分布或形式安全；前提、identity 或预算越界时停止新路径，回退到该 owner 已验证的旧路径并保留失败回执。旧路径在其原约束成立时继续共存。
<!-- books-review:SF-2026-ARXIV-2606-23983:end -->

<!-- existing:SF-2026-ARXIV-2606-23989:start -->
`books/part-07-agent/76-rag.md` 的唯一 owner 已承载相关机制链；`books/part-07-agent/77-memory.md#L1` 只消费 handoff。
<!-- existing:SF-2026-ARXIV-2606-23989:end -->

<!-- delta:SF-2026-ARXIV-2606-23989:start -->
Faithful by Construction: Claim-Anchored Attribution for Multi-Document Summarization 的 exact-v1 机制为：We present CAMS, a Claim-Anchored Multi-document Summarization framework that (i) extracts atomic claims with token-level provenance from every source document, (ii) clusters equivalent claims across documents while flagging inter-source conflicts, (iii) selects a support-aware and salient subset, and (iv) rewrites the selection into a summary in which every sentence is anchored to a support-checked claim that links back to one or more source spans. 因此 把 retrieval 配置、candidate set、证据 identity 与质量—成本评估绑定。
<!-- delta:SF-2026-ARXIV-2606-23989:end -->

<!-- books-review:SF-2026-ARXIV-2606-23989:start -->
Unique owner `AGENT-RAG`; adjacent non-owner `books/part-07-agent/77-memory.md#L1`; relation `Principle Reuse`; disposition `No Change — Existing Coverage`. 该 family 的 failure pressure 是：End-to-end large language models (LLMs) produce fluent multi-document summaries but remain prone to hallucination, and the attributions they offer are typically coarse (whole documents or passages) and generated post hoc, leaving each summary statement hard to verify. 披露的 evaluation signal 是：We evaluate quality, faithfulness, and localization on MultiNews, analyze conflict handling on DiverseSumm, and test zero-shot transfer on WCEP, using a two-regime protocol that separates reference-free citation quality from gold-aligned localization accuracy, and we add an evaluator-decoupled audit that tests citation precision with a support model never used for selection or verification. 证据只支持 exact-v1 在披露 workload/model/hardware 范围内的机制与结果，不证明生产尾部、未测分布或形式安全；前提、identity 或预算越界时停止新路径，回退到该 owner 已验证的旧路径并保留失败回执。旧路径在其原约束成立时继续共存。
<!-- books-review:SF-2026-ARXIV-2606-23989:end -->

<!-- existing:SF-2026-ARXIV-2606-24004:start -->
`books/part-04-training-system/31-rlhf.md` 的唯一 owner 已承载相关机制链；`books/part-04-training-system/32-ppo.md#L1` 只消费 handoff。
<!-- existing:SF-2026-ARXIV-2606-24004:end -->

<!-- delta:SF-2026-ARXIV-2606-24004:start -->
Towards Spec Learning: Inference-Time Alignment from Preference Pairs 的 exact-v1 机制为：We propose spec learning, a framework that relies on a brief user instruction and a small set of preference judgments. 因此 把 rubric/spec 版本、policy 版本、独立 judge 与 reward-hacking 检测隔离。
<!-- delta:SF-2026-ARXIV-2606-24004:end -->

<!-- books-review:SF-2026-ARXIV-2606-24004:start -->
Unique owner `TRAIN-RLHF`; adjacent non-owner `books/part-04-training-system/32-ppo.md#L1`; relation `Direct Evolution`; disposition `Integrate`. 该 family 的 failure pressure 是：Steering a large language model (LLM) toward a desired behavior typically relies on an iterative process of hand-crafting a prompt based on a careful inspection of the model's responses. 披露的 evaluation signal 是：We show that the responses generated based on the compiled specifications often outperform direct preference optimization (DPO) on datasets from specialized domains whose preference signal is dense. 证据只支持 exact-v1 在披露 workload/model/hardware 范围内的机制与结果，不证明生产尾部、未测分布或形式安全；前提、identity 或预算越界时停止新路径，回退到该 owner 已验证的旧路径并保留失败回执。旧路径在其原约束成立时继续共存。
<!-- books-review:SF-2026-ARXIV-2606-24004:end -->

<!-- existing:SF-2026-ARXIV-2606-24020:start -->
`books/part-06-ai-infrastructure/66-evaluation-system.md` 的唯一 owner 已承载相关机制链；`books/part-06-ai-infrastructure/67-monitoring.md#L1` 只消费 handoff。
<!-- existing:SF-2026-ARXIV-2606-24020:end -->

<!-- delta:SF-2026-ARXIV-2606-24020:start -->
You Don't Need to Run Every Eval 的 exact-v1 机制为：Building on this, we design BenchPress: a logit-space rank-2 matrix completion method that recovers held-out scores to within 4.6 points, and a confidence layer that says when each prediction can be trusted. 因此 把样本、metric、judge、阈值、不确定性和 release authority 分离。
<!-- delta:SF-2026-ARXIV-2606-24020:end -->

<!-- books-review:SF-2026-ARXIV-2606-24020:start -->
Unique owner `PLATFORM-EVALUATION-SYSTEM`; adjacent non-owner `books/part-06-ai-infrastructure/67-monitoring.md#L1`; relation `Principle Reuse`; disposition `No Change — Existing Coverage`. 该 family 的 failure pressure 是：A modern model release reports scores on 40+ benchmarks and the same evaluations were run many more times before it: to track training progress, compare design choices, and select the checkpoint for the release. 披露的 evaluation signal 是：A modern model release reports scores on 40+ benchmarks and the same evaluations were run many more times before it: to track training progress, compare design choices, and select the checkpoint for the release. 证据只支持 exact-v1 在披露 workload/model/hardware 范围内的机制与结果，不证明生产尾部、未测分布或形式安全；metric、judge 或样本假设失效时保持 release Gate Open 并恢复完整评估。旧路径在其原约束成立时继续共存。
<!-- books-review:SF-2026-ARXIV-2606-24020:end -->

<!-- existing:SF-2026-ARXIV-2606-24033:start -->
`books/part-05-inference-system/45-why-kv-cache-speeds-up.md` 的唯一 owner 已承载相关机制链；`books/part-05-inference-system/46-continuous-batching.md#L1` 只消费 handoff。
<!-- existing:SF-2026-ARXIV-2606-24033:end -->

<!-- delta:SF-2026-ARXIV-2606-24033:start -->
RoPE-Aware Bit Allocation for KV-Cache Quantization 的 exact-v1 机制为：We introduce Block-GTQ, a RoPE-aware bit allocator for key-cache quantization built on TurboQuant-MSE(TQ-MSE). 因此 把 cache position、eviction/quantization policy、跨模态 identity 与 dense recompute fallback 绑定。
<!-- delta:SF-2026-ARXIV-2606-24033:end -->

<!-- books-review:SF-2026-ARXIV-2606-24033:start -->
Unique owner `INFER-KV-CACHE`; adjacent non-owner `books/part-05-inference-system/46-continuous-batching.md#L1`; relation `Direct Evolution`; disposition `Integrate`. 该 family 的 failure pressure 是：Under RoPE, however, a key's contribution to a future attention logit decomposes into a position-dependent sum over two-dimensional frequency blocks. 披露的 evaluation signal 是：On a single H800 GPU with Qwen2.5-3B-Instruct, packed K3V3 achieves 3.24x KV-cache compression with fp16-comparable quality, runs 1.34x faster than fp16 FlashAttention2 at 128K context, reduces peak memory from 56.31 GB to 19.85 GB, and remains feasible at 256K and 512K where fp16 OOMs. 证据只支持 exact-v1 在披露 workload/model/hardware 范围内的机制与结果，不证明生产尾部、未测分布或形式安全；cache identity 或误差预算失配时清空该路径并回到未压缩/重算 KV。旧路径在其原约束成立时继续共存。
<!-- books-review:SF-2026-ARXIV-2606-24033:end -->

<!-- existing:SF-2026-ARXIV-2606-24040:start -->
`books/part-07-agent/77-memory.md` 的唯一 owner 已承载相关机制链；`books/part-07-agent/78-tool-calling.md#L1` 只消费 handoff。
<!-- existing:SF-2026-ARXIV-2606-24040:end -->

<!-- delta:SF-2026-ARXIV-2606-24040:start -->
Towards Version-aware Operations and Transaction Memories for Multi-layer MeMo 的 exact-v1 机制为：We propose a version-aware operation layer in which high-level operations such as replace, obsolete, keep-history, rollback, and trace are compiled into MeMo-native primitive calls over sequences and tokens. 因此 把事件时间、来源、有效条件、版本、检索决策与写入 authority 分开。
<!-- delta:SF-2026-ARXIV-2606-24040:end -->

<!-- books-review:SF-2026-ARXIV-2606-24040:start -->
Unique owner `AGENT-MEMORY`; adjacent non-owner `books/part-07-agent/78-tool-calling.md#L1`; relation `Direct Evolution`; disposition `Integrate`. 该 family 的 failure pressure 是：MeMo proposes language models with explicit multi-layer correlation matrix memories (CMMs), where memorization, retrieval, and forgetting are architectural operations. 披露的 evaluation signal 是：This paper asks how such memories can reduce the need for retraining when knowledge changes. 证据只支持 exact-v1 在披露 workload/model/hardware 范围内的机制与结果，不证明生产尾部、未测分布或形式安全；来源/时间/版本不足时隔离 candidate memory，保留原始轨迹且禁止自动覆盖。旧路径在其原约束成立时继续共存。
<!-- books-review:SF-2026-ARXIV-2606-24040:end -->

<!-- existing:SF-2026-ARXIV-2606-24074:start -->
Re-read `books/part-06-ai-infrastructure/66-evaluation-system.md#L1` and adjacent `books/part-06-ai-infrastructure/67-monitoring.md#L1`; owner remains unique.
<!-- existing:SF-2026-ARXIV-2606-24074:end -->

<!-- delta:SF-2026-ARXIV-2606-24074:start -->
把一次性 benchmark 分数改成带双侧错误界、逐 token 成本和停止阈值的 SPRT certification；certifier 持有 query/score/log-likelihood state，跨阈值才发布 reliable/unreliable verdict。
<!-- delta:SF-2026-ARXIV-2606-24074:end -->

<!-- books-review:SF-2026-ARXIV-2606-24074:start -->
Direct Evolution; Integrate queued for root. 只证明给定 reliability gap、binary correctness oracle 与 small-error leading order；不证明开放式 judge 标签、分布漂移或任意非独立 query 下仍满足同一界。
<!-- books-review:SF-2026-ARXIV-2606-24074:end -->

<!-- existing:SF-2026-ARXIV-2606-24081:start -->
Re-read `books/part-06-ai-infrastructure/66-evaluation-system.md#L1` and adjacent `books/part-06-ai-infrastructure/67-monitoring.md#L1`; owner remains unique.
<!-- existing:SF-2026-ARXIV-2606-24081:end -->

<!-- delta:SF-2026-ARXIV-2606-24081:start -->
把 T2I jailbreak 的 prompt-only 比较升级为 paper-to-pipeline contract：attack module、victim、filter、multimodal judge、配置、日志与版本 artifact 共同成为可复现状态。
<!-- delta:SF-2026-ARXIV-2606-24081:end -->

<!-- books-review:SF-2026-ARXIV-2606-24081:start -->
Direct Evolution; Integrate queued for root. 11 种 attack、4 个 victim 与论文匹配配置不证明未知 attack 自动复现；prompt/heuristic memory update 及 closed-source safety filter 仍是黑盒边界。
<!-- books-review:SF-2026-ARXIV-2606-24081:end -->

<!-- existing:SF-2026-ARXIV-2606-24119:start -->
Re-read `books/part-06-ai-infrastructure/67-monitoring.md#L1` and adjacent `books/part-06-ai-infrastructure/66-evaluation-system.md#L1`; owner remains unique.
<!-- existing:SF-2026-ARXIV-2606-24119:end -->

<!-- delta:SF-2026-ARXIV-2606-24119:start -->
撤销把 denoising top-1 concentration 当 PEFT collapse alarm 的旧路径；monitor 改读 max LoRA gradient norm，并由每个 DLM family 的 held-out calibration 拥有告警阈值。
<!-- delta:SF-2026-ARXIV-2606-24119:end -->

<!-- books-review:SF-2026-ARXIV-2606-24119:start -->
Direct Evolution; Integrate queued for root. 816 个配置、3 个 DLM family 与 200-step horizon 只支持短程 DLM-LoRA triage；跨 family 阈值失败，不能外推为通用 collapse detector。
<!-- books-review:SF-2026-ARXIV-2606-24119:end -->

<!-- existing:SF-2026-ARXIV-2606-24124:start -->
Re-read `books/part-06-ai-infrastructure/66-evaluation-system.md#L1` and adjacent `books/part-06-ai-infrastructure/67-monitoring.md#L1`; owner remains unique.
<!-- existing:SF-2026-ARXIV-2606-24124:end -->

<!-- delta:SF-2026-ARXIV-2606-24124:start -->
将自由文本 CoT 编译为 typed dependency/constraint/expression trace；deterministic verifier 拥有可机械化检查，LLM audit 只处理 semantic deduction，失败步骤进入 repair 而非直接接受终局答案。
<!-- delta:SF-2026-ARXIV-2606-24124:end -->

<!-- books-review:SF-2026-ARXIV-2606-24124:start -->
Direct Evolution; Integrate queued for root. 逐步验证成本随 trace 线性增长，semantic deduction 仍依赖 LLM audit，inference schema library 有限；三类 benchmark 不证明任意开放域推理。
<!-- books-review:SF-2026-ARXIV-2606-24124:end -->

<!-- existing:SF-2026-ARXIV-2606-24133:start -->
Re-read `books/part-04-training-system/27-data.md#L1` and adjacent `books/part-04-training-system/28-pretraining.md#L1`; owner remains unique.
<!-- existing:SF-2026-ARXIV-2606-24133:end -->

<!-- delta:SF-2026-ARXIV-2606-24133:start -->
把固定或单目标 data mixture 改为 SAC controller：state 汇聚 domain loss/lexical diversity/weight-norm，action 写回下一训练阶段的 domain weights，多目标 reward 决定调度。
<!-- delta:SF-2026-ARXIV-2606-24133:end -->

<!-- books-review:SF-2026-ARXIV-2606-24133:start -->
Direct Evolution; Integrate queued for root. The Pile、给定 16-layer/2048-dim recipe 与 reward sensitivity 不证明跨 tokenizer、optimizer、数据污染或超大规模 pretraining 仍有相同收益。
<!-- books-review:SF-2026-ARXIV-2606-24133:end -->

<!-- existing:SF-2026-ARXIV-2606-24143:start -->
Re-read `books/part-04-training-system/36-distributed-training.md#L1` and adjacent `books/part-04-training-system/38-pipeline-parallel.md#L1`; owner remains unique.
<!-- existing:SF-2026-ARXIV-2606-24143:end -->

<!-- delta:SF-2026-ARXIV-2606-24143:start -->
将 rollout、teacher scoring、student update 解耦为 queue stages；learner 用 current-student recomputation 修正 reverse-KL stale signal，并以 multi-sample MC 避免 cached top-k support bias。
<!-- delta:SF-2026-ARXIV-2606-24143:end -->

<!-- books-review:SF-2026-ARXIV-2606-24143:start -->
Direct Evolution; Integrate queued for root. 实验限单节点 8 GPU、sparse/MC estimator；dense full-vocabulary KL、跨节点扩展与更长 staleness 未验证，cache/queue 压力过大时应回退 bounded-staleness 或同步 OPD。
<!-- books-review:SF-2026-ARXIV-2606-24143:end -->

<!-- existing:SF-2026-ARXIV-2606-24151:start -->
Re-read `books/part-07-agent/77-memory.md#L1` and adjacent `books/part-07-agent/76-rag.md#L1`; owner remains unique.
<!-- existing:SF-2026-ARXIV-2606-24151:end -->

<!-- delta:SF-2026-ARXIV-2606-24151:start -->
不在设计时固定 text 或 code memory；memory manager 先保存 plan/fact/pitfall 文本，只有重复且验证通过的 plan 才 crystallize 为 callable tool，同时保留构建成本与 provenance。
<!-- delta:SF-2026-ARXIV-2606-24151:end -->

<!-- books-review:SF-2026-ARXIV-2606-24151:start -->
Direct Evolution; Integrate queued for root. AppWorld 与同一 experience set 只显示两种表示在 construction cost、execution efficiency、transferability 上互补；不证明生成工具在未知 API、权限变化或污染经验下安全。
<!-- books-review:SF-2026-ARXIV-2606-24151:end -->

<!-- existing:SF-2026-ARXIV-2606-24177:start -->
Re-read `books/part-07-agent/81-workflow.md#L1` and adjacent `books/part-07-agent/82-multi-agent.md#L1`; owner remains unique.
<!-- existing:SF-2026-ARXIV-2606-24177:end -->

<!-- delta:SF-2026-ARXIV-2606-24177:start -->
以 artifact 为边界组织 producer-critic factory，critic 在 fresh context 验收后才推进；自动化 loop 只提交可机器检查部分，visibility/fixability taxonomy 将不可判定 claim 留给 human scientist。
<!-- delta:SF-2026-ARXIV-2606-24177:end -->

<!-- books-review:SF-2026-ARXIV-2606-24177:start -->
Direct Evolution; Integrate queued for root. 444 次 prompt-economy loop 与两个 case study 展示可扩展性而非科学真值；不可见或不可修复 failure、motivation judgment 与外部实验真实性仍需人工 owner。
<!-- books-review:SF-2026-ARXIV-2606-24177:end -->

<!-- existing:SF-2026-ARXIV-2606-24204:start -->
Re-read `books/part-07-agent/76-rag.md#L1` and adjacent `books/part-07-agent/77-memory.md#L1`; owner remains unique.
<!-- existing:SF-2026-ARXIV-2606-24204:end -->

<!-- delta:SF-2026-ARXIV-2606-24204:start -->
把 interval predicate 的双端点约束映射为统一 2D dominance space；每个 predicate 拥有独立 UDG instance，patch edge 只在 validity 保持时补路由，避免两个 scalar index 的交集爆炸。
<!-- delta:SF-2026-ARXIV-2606-24204:end -->

<!-- books-review:SF-2026-ARXIV-2606-24204:start -->
Direct Evolution; Integrate queued for root. 闭合 two-bound conjunctive predicate 与论文数据集不覆盖任意布尔 filter、动态高 churn 或 distributed index consistency；过滤结构不匹配时回退普通 filtered ANN。
<!-- books-review:SF-2026-ARXIV-2606-24204:end -->

<!-- existing:SF-2026-ARXIV-2606-24245:start -->
Re-read `books/part-06-ai-infrastructure/72-security.md#L1` and adjacent `books/part-06-ai-infrastructure/73-production-best-practice.md#L1`; owner remains unique.
<!-- existing:SF-2026-ARXIV-2606-24245:end -->

<!-- delta:SF-2026-ARXIV-2606-24245:start -->
把静态 expert rule 的维护改为 annotation-driven CEGIS：trace evaluator 产出 FP/FN counterexample，ILP 选 discriminating predicate，candidate verifier 决定是否发布 rule revision。
<!-- delta:SF-2026-ARXIV-2606-24245:end -->

<!-- books-review:SF-2026-ARXIV-2606-24245:start -->
Direct Evolution; Integrate queued for root. 291 条 code/embodied trace 与 4–5 次迭代不证明稀疏、错误或对抗标注下收敛；发布前仍需 human approval、versioned rollback 与旧 expert rules 共存。
<!-- books-review:SF-2026-ARXIV-2606-24245:end -->

<!-- existing:SF-2026-ARXIV-2606-24311:start -->
Re-read `books/part-07-agent/84-agent-platform.md#L1` and adjacent `books/part-07-agent/83-mcp.md#L1`; owner remains unique.
<!-- existing:SF-2026-ARXIV-2606-24311:end -->

<!-- delta:SF-2026-ARXIV-2606-24311:start -->
将 model invocation、tool execution、workspace mutation、rule knowledge 与 execution record 收进同一 runtime boundary；剩余时间成为显式 state，用于在探索、实现、验证之间重配预算。
<!-- delta:SF-2026-ARXIV-2606-24311:end -->

<!-- books-review:SF-2026-ARXIV-2606-24311:start -->
Direct Evolution; Integrate queued for root. 结果主要绑定 GPT-style tool calling 与 Terminal-Bench；其他 model family、长编译/训练、严格中间验证和 workspace 外 side effect 未证明，应保留人工接管与受限 sandbox。
<!-- books-review:SF-2026-ARXIV-2606-24311:end -->

<!-- existing:SF-2026-ARXIV-2606-24322:start -->
Re-read `books/part-06-ai-infrastructure/72-security.md#L1` and adjacent `books/part-06-ai-infrastructure/73-production-best-practice.md#L1`; owner remains unique.
<!-- existing:SF-2026-ARXIV-2606-24322:end -->

<!-- delta:SF-2026-ARXIV-2606-24322:start -->
memory item 的行动权不再由可篡改 content/lineage 推断，而在 write 时绑定 origin authority；只有 k 个独立 trusted source 才 elevation，高风险 action 缺少 corroborator 时交给 one-time user confirmation。
<!-- delta:SF-2026-ARXIV-2606-24322:end -->

<!-- books-review:SF-2026-ARXIV-2606-24322:start -->
Direct Evolution; Integrate queued for root. 保证依赖正确 origin labeling、独立 principal 与有限 TLA+ model；trusted tool compromise、隐式 value reconstruction、nested payload taint 和广泛真实任务仍未闭合。
<!-- books-review:SF-2026-ARXIV-2606-24322:end -->

<!-- existing:SF-2026-ARXIV-2606-24402:start -->
Re-read `books/part-06-ai-infrastructure/72-security.md#L1` and adjacent `books/part-06-ai-infrastructure/73-production-best-practice.md#L1`; owner remains unique.
<!-- existing:SF-2026-ARXIV-2606-24402:end -->

<!-- delta:SF-2026-ARXIV-2606-24402:start -->
RAG 安全 gate 不再只问文档是否被检索，而按 local-artifact、model-knowledge、runtime-dependent 三层 verification boundary 决定 claim 能否进入行动；L3 需要动态探测或权威外部证据。
<!-- delta:SF-2026-ARXIV-2606-24402:end -->

<!-- books-review:SF-2026-ARXIV-2606-24402:start -->
Direct Evolution; Integrate queued for root. 11 CTF、11 CVE、3 model family 下 prompt verification/multi-source retrieval 在 sparse-evidence 与 zero-day 会退化；不能把信息多数当独立真实性。
<!-- books-review:SF-2026-ARXIV-2606-24402:end -->

<!-- existing:SF-2026-ARXIV-2606-24408:start -->
Re-read `books/part-06-ai-infrastructure/72-security.md#L1` and adjacent `books/part-06-ai-infrastructure/73-production-best-practice.md#L1`; owner remains unique.
<!-- existing:SF-2026-ARXIV-2606-24408:end -->

<!-- delta:SF-2026-ARXIV-2606-24408:start -->
利用训练数据自然出现且稀有的 identifier 作为 post-hoc audit unit，避免必须预埋 canary；auditor 分离 DP leakage 检查与 dataset inference，并记录 identifier cardinality/生成机制。
<!-- delta:SF-2026-ARXIV-2606-24408:end -->

<!-- books-review:SF-2026-ARXIV-2606-24408:start -->
Direct Evolution; Integrate queued for root. NID 可用性、独立性与 generator 正确性依赖数据域；黑盒可见性、重复 identifier、强 MIA 和 DP-SGD 配置变化会改变 sample complexity，不能当作逐样本法律证明。
<!-- books-review:SF-2026-ARXIV-2606-24408:end -->

<!-- existing:SF-2026-ARXIV-2606-24428:start -->
Re-read `books/part-07-agent/77-memory.md#L1` and adjacent `books/part-07-agent/76-rag.md#L1`; owner remains unique.
<!-- existing:SF-2026-ARXIV-2606-24428:end -->

<!-- delta:SF-2026-ARXIV-2606-24428:start -->
经验写入从同一 agent 自我总结改为 Execute 的异构并行轨迹、第三方 contrastive Distill 与 consensus Verify；只有通过独立验证的经验才能进入 storage/retrieval。
<!-- delta:SF-2026-ARXIV-2606-24428:end -->

<!-- books-review:SF-2026-ARXIV-2606-24428:start -->
Direct Evolution; Integrate queued for root. 多 agent consensus 仍可能相关失败，且 tau2-Bench/Mind2Web/MMTB 与论文 temperature/retrieval 配置不证明开放任务；不确定时保存 raw trajectories 或拒绝写入。
<!-- books-review:SF-2026-ARXIV-2606-24428:end -->

<!-- existing:SF-2026-ARXIV-2606-24437:start -->
Re-read `books/part-07-agent/82-multi-agent.md#L1` and adjacent `books/part-07-agent/81-workflow.md#L1`; owner remains unique.
<!-- existing:SF-2026-ARXIV-2606-24437:end -->

<!-- delta:SF-2026-ARXIV-2606-24437:start -->
MoA 不再把所有历史 reasoning 平铺给 aggregator；reviewer 对轨迹排序写入 reasoning memory，router 按 layer/quality/diversity 投影少量 references，使 memory state 随协作层累积。
<!-- delta:SF-2026-ARXIV-2606-24437:end -->

<!-- books-review:SF-2026-ARXIV-2606-24437:start -->
Direct Evolution; Integrate queued for root. 只测固定 proposer pool、有限 width 与五个 benchmark；reviewer bias/overhead 和同源 proposer correlation 会放大错误，低置信时回退无 memory MoA 或独立 adjudication。
<!-- books-review:SF-2026-ARXIV-2606-24437:end -->

<!-- existing:SF-2026-ARXIV-2606-24467:start -->
Re-read `books/part-05-inference-system/45-why-kv-cache-speeds-up.md#L1` and adjacent `books/part-05-inference-system/47-pagedattention.md#L1`; owner remains unique.
<!-- existing:SF-2026-ARXIV-2606-24467:end -->

<!-- delta:SF-2026-ARXIV-2606-24467:start -->
KV eviction 从统一 token score 改为 semantic-retrieval heads 选 token、error-aware controller 按层分配 cache budget；压缩决定属于 cache manager，不修改模型语义 owner。
<!-- delta:SF-2026-ARXIV-2606-24467:end -->

<!-- books-review:SF-2026-ARXIV-2606-24467:start -->
Direct Evolution; Integrate queued for root. LongBench/NIAH 与选定模型不证明所有 head 都稳定承载语义检索；head drift、低命中或质量回退时恢复更大 cache/全 KV，与 quantization/prefill acceleration 仅证明可组合。
<!-- books-review:SF-2026-ARXIV-2606-24467:end -->

<!-- existing:SF-2026-ARXIV-2606-24506:start -->
Re-read `books/part-05-inference-system/54-gpu-memory.md#L1` and adjacent `books/part-05-inference-system/55-pd-disaggregation.md#L1`; owner remains unique.
<!-- existing:SF-2026-ARXIV-2606-24506:end -->

<!-- delta:SF-2026-ARXIV-2606-24506:start -->
冷 MoE serving 将 stable weights 与 demand-driven KV 拆成独立资源池；planner virtualize shared KV，layer-wise scheduler/persistent kernel 只激活所需 weights 和 KV heads。
<!-- delta:SF-2026-ARXIV-2606-24506:end -->

<!-- books-review:SF-2026-ARXIV-2606-24506:start -->
Direct Evolution; Integrate queued for root. 证据聚焦冷模型、低并发与给定 context/model mix；热点突发、跨租户 isolation、模型装载故障和高并发下 shared-pool contention 未证明，应能回退 dedicated allocation。
<!-- books-review:SF-2026-ARXIV-2606-24506:end -->

<!-- existing:SF-2026-ARXIV-2606-24535:start -->
Re-read `books/part-07-agent/77-memory.md#L1` and adjacent `books/part-07-agent/76-rag.md#L1`; owner remains unique.
<!-- existing:SF-2026-ARXIV-2606-24535:end -->

<!-- delta:SF-2026-ARXIV-2606-24535:start -->
多 Agent 共享记忆增加 explicit scope、valid time、provenance graph 与 policy-gated retrieval；矛盾在 write-time resolution，reader 只消费已提交版本，传播由 privilege gate 控制。
<!-- delta:SF-2026-ARXIV-2606-24535:end -->

<!-- books-review:SF-2026-ARXIV-2606-24535:start -->
Direct Evolution; Integrate queued for root. self-evaluation、single tenant、focused scope probe、有限 workload 且无 comparand；staleness-after-supersession 与 visibility 延迟未完整测量，冲突时回退 tenant-local memory 或 single writer。
<!-- books-review:SF-2026-ARXIV-2606-24535:end -->

<!-- existing:SF-2026-ARXIV-2606-24551:start -->
`books/part-07-agent/78-tool-calling.md` 的唯一 owner 已承载相关机制链；`books/part-07-agent/79-planning.md#L1` 只消费 handoff。
<!-- existing:SF-2026-ARXIV-2606-24551:end -->

<!-- delta:SF-2026-ARXIV-2606-24551:start -->
GUI vs. CLI: Execution Bottlenecks in Screen-Only and Skill-Mediated Computer-Use Agents 的 exact-v1 机制为：We introduce a matched execution-layer benchmark of 440 desktop tasks across 18 applications and 12 workflow categories, where screen-only GUI agents and skill-mediated CLI agents receive identical goals, states, and final-state verifiers while being restricted to modality-native actions. 因此 把 tool schema、状态前置条件、GUI/CLI execution surface 与 side-effect receipt 绑定。
<!-- delta:SF-2026-ARXIV-2606-24551:end -->

<!-- books-review:SF-2026-ARXIV-2606-24551:start -->
Unique owner `AGENT-TOOL-CALLING`; adjacent non-owner `books/part-07-agent/79-planning.md#L1`; relation `Direct Evolution`; disposition `Integrate`. 该 family 的 failure pressure 是：In this controlled setting, the strongest GUI agent reaches a 59.1% full pass rate, outperforming the strongest original-skill CLI agent at 48.2%; however, verifier-guided skill augmentation raises CLI success to 69.3%, showing that much of the CLI deficit comes from incomplete skill coverage rather than model capability alone. 披露的 evaluation signal 是：Computer-use agents can execute software tasks through either graphical interfaces or programmatic command interfaces, but existing evaluations confound interaction modality with differences in tasks, initial states, verifiers, and permitted actions. 证据只支持 exact-v1 在披露 workload/model/hardware 范围内的机制与结果，不证明生产尾部、未测分布或形式安全；前提、identity 或预算越界时停止新路径，回退到该 owner 已验证的旧路径并保留失败回执。旧路径在其原约束成立时继续共存。
<!-- books-review:SF-2026-ARXIV-2606-24551:end -->

<!-- existing:SF-2026-ARXIV-2606-24598:start -->
Ch81 已持有有状态流程、artifact commit、rollback 与 stage handoff；Ch79/Ch82 分别持有计划和并发协作。 For this family the compared adjacent handoff is `books/part-07-agent/79-planning.md#L1; books/part-07-agent/82-multi-agent.md#L1`.
<!-- existing:SF-2026-ARXIV-2606-24598:end -->

<!-- delta:SF-2026-ARXIV-2606-24598:start -->
expert LLM workflow 迁移到 self-evolution 前应先做 convertibility taxonomy、reversible adapter 与 rollback，不直接改写 opaque harness
<!-- delta:SF-2026-ARXIV-2606-24598:end -->

<!-- books-review:SF-2026-ARXIV-2606-24598:start -->
Unique owner `AGENT-WORKFLOW`; adjacent consumer `books/part-07-agent/79-planning.md#L1; books/part-07-agent/82-multi-agent.md#L1`; relation `Direct Evolution`; disposition `Integrate`. 证据仅是单个 WeChat workflow 的可逆迁移和 early feedback signal，不是验证过的 self-learning；taxonomy 误路由时回退并一键回滚 legacy harness，保持业务逻辑不变。
<!-- books-review:SF-2026-ARXIV-2606-24598:end -->

<!-- existing:SF-2026-ARXIV-2606-24626:start -->
Re-read `books/part-06-ai-infrastructure/69-trace.md#L1` and adjacent `books/part-06-ai-infrastructure/67-monitoring.md#L1`; owner remains unique.
<!-- existing:SF-2026-ARXIV-2606-24626:end -->

<!-- delta:SF-2026-ARXIV-2606-24626:start -->
故障诊断不再把全 trajectory 填入一个 context；investigator 用 segment search/read tools 主动取证，并用 persistent STM 保存跨轮 hypothesis/evidence，使 attribution 与原始 trace 长度解耦。
<!-- delta:SF-2026-ARXIV-2606-24626:end -->

<!-- books-review:SF-2026-ARXIV-2606-24626:start -->
Direct Evolution; Integrate queued for root. Who&When/TRAIL GAIA、1M/25K token budget 与给定 toolbox 不证明生产 trace schema、并发因果或根因真实性；缺证据时返回 unknown 并交给人工 trace drill-down。
<!-- books-review:SF-2026-ARXIV-2606-24626:end -->

<!-- existing:SF-2026-ARXIV-2606-24722:start -->
Re-read `books/part-04-training-system/36-distributed-training.md#L1` and adjacent `books/part-04-training-system/38-pipeline-parallel.md#L1`; owner remains unique.
<!-- existing:SF-2026-ARXIV-2606-24722:end -->

<!-- delta:SF-2026-ARXIV-2606-24722:start -->
把 end-to-end backprop 的全局 hidden-target ownership拆成 block-local diffusion objective；edge worker 独立更新 block，coordinator 只按版本/acceptance rule 接收异步 update，同一 block protocol 也支撑分布式 inference。
<!-- delta:SF-2026-ARXIV-2606-24722:end -->

<!-- books-review:SF-2026-ARXIV-2606-24722:start -->
Direct Evolution; Integrate queued for root. real-text small model、virtual edge worker 与 WAN smoke test 不证明大模型质量、Byzantine worker、激励或大规模收敛；acceptance 失败时回退同步/集中训练。
<!-- books-review:SF-2026-ARXIV-2606-24722:end -->

<!-- existing:SF-2026-ARXIV-2606-24774:start -->
Re-read `books/part-06-ai-infrastructure/72-security.md#L1` and adjacent `books/part-06-ai-infrastructure/73-production-best-practice.md#L1`; owner remains unique.
<!-- existing:SF-2026-ARXIV-2606-24774:end -->

<!-- delta:SF-2026-ARXIV-2606-24774:start -->
training-data audit 从 output entropy 转向 parameter-gradient signature；auditor 对跨模态 parameter slices 做稳定性/对齐特征，并用已知 train/non-train reference mask 掉不敏感维度。
<!-- delta:SF-2026-ARXIV-2606-24774:end -->

<!-- books-review:SF-2026-ARXIV-2606-24774:start -->
Direct Evolution; Integrate queued for root. 需要 white-box parameters 与 reference data；七个 VLM 配置、medical/general dataset 不证明黑盒 API、生成式泄漏或法律层面的逐样本归属。
<!-- books-review:SF-2026-ARXIV-2606-24774:end -->

<!-- existing:SF-2026-ARXIV-2606-24775:start -->
Re-read `books/part-07-agent/77-memory.md#L1` and adjacent `books/part-07-agent/76-rag.md#L1`; owner remains unique.
<!-- existing:SF-2026-ARXIV-2606-24775:end -->

<!-- delta:SF-2026-ARXIV-2606-24775:start -->
把 agent memory 评价拆成 logical representation、physical storage/index、extraction、query routing 与 maintenance 五个 ownerable stage，并分别测 retrieval fidelity、evolution robustness、long-horizon stability 和 operation cost。
<!-- delta:SF-2026-ARXIV-2606-24775:end -->

<!-- books-review:SF-2026-ARXIV-2606-24775:start -->
Direct Evolution; Integrate queued for root. 现有系统/benchmark 比较不证明单一实现普适最优；缺少生产 authorization、deletion SLA、并发一致性或真实 workload 时只能作为 lifecycle checklist。
<!-- books-review:SF-2026-ARXIV-2606-24775:end -->

<!-- audit-target:books:end -->
## 7. Semantic Audit

<!-- validator:semantic-audit-v1 -->
| Audit ID | Auditor | Scope | Reviewed Refs | Findings | Resolution | Status |
| --- | --- | --- | --- | --- | --- | --- |
| SA-20260624-COVERAGE-OWNER-REBUILD | fresh-context:pending-owner-rebuild | coverage | coverage:SRC-ARXIV:20260624 | GAP-ARXIV-SEMANTIC-OWNER-REBUILD-20260624: raw closures and false-negative frontier require independent semantic review | Open — canonical inventory and owner receipt are preserved in the date-local source packet | open |
| SA-20260624-EVIDENCE-OWNER-REBUILD | fresh-context:pending-owner-rebuild | evidence | review:SF-2026-ARXIV-2606-23740; review:SF-2026-ARXIV-2606-23743; review:SF-2026-ARXIV-2606-23752; review:SF-2026-ARXIV-2606-23754; review:SF-2026-ARXIV-2606-23768; review:SF-2026-ARXIV-2606-23797; review:SF-2026-ARXIV-2606-23858; review:SF-2026-ARXIV-2606-23872; review:SF-2026-ARXIV-2606-23892; review:SF-2026-ARXIV-2606-23915; review:SF-2026-ARXIV-2606-23927; review:SF-2026-ARXIV-2606-23937; review:SF-2026-ARXIV-2606-23961; review:SF-2026-ARXIV-2606-23969; review:SF-2026-ARXIV-2606-23983; review:SF-2026-ARXIV-2606-23989; review:SF-2026-ARXIV-2606-24004; review:SF-2026-ARXIV-2606-24020; review:SF-2026-ARXIV-2606-24033; review:SF-2026-ARXIV-2606-24040; review:SF-2026-ARXIV-2606-24074; review:SF-2026-ARXIV-2606-24081; review:SF-2026-ARXIV-2606-24119; review:SF-2026-ARXIV-2606-24124; review:SF-2026-ARXIV-2606-24133; review:SF-2026-ARXIV-2606-24143; review:SF-2026-ARXIV-2606-24151; review:SF-2026-ARXIV-2606-24177; review:SF-2026-ARXIV-2606-24204; review:SF-2026-ARXIV-2606-24245; review:SF-2026-ARXIV-2606-24311; review:SF-2026-ARXIV-2606-24322; review:SF-2026-ARXIV-2606-24402; review:SF-2026-ARXIV-2606-24408; review:SF-2026-ARXIV-2606-24428; review:SF-2026-ARXIV-2606-24437; review:SF-2026-ARXIV-2606-24467; review:SF-2026-ARXIV-2606-24506; review:SF-2026-ARXIV-2606-24535; review:SF-2026-ARXIV-2606-24551; review:SF-2026-ARXIV-2606-24598; review:SF-2026-ARXIV-2606-24626; review:SF-2026-ARXIV-2606-24722; review:SF-2026-ARXIV-2606-24774; review:SF-2026-ARXIV-2606-24775 | EVIDENCE-OWNER-REBUILD-20260624: transferred exact-v1 reviews require fresh-context false-positive and access audit | Open — transferred review bodies remain provenance, not final acceptance | open |
| SA-20260624-SELECTION-OWNER-REBUILD | fresh-context:pending-owner-rebuild | deep_analysis_selection | analysis-decision:SF-2026-ARXIV-2606-23740; analysis-decision:SF-2026-ARXIV-2606-23743; analysis-decision:SF-2026-ARXIV-2606-23752; analysis-decision:SF-2026-ARXIV-2606-23754; analysis-decision:SF-2026-ARXIV-2606-23768; analysis-decision:SF-2026-ARXIV-2606-23797; analysis-decision:SF-2026-ARXIV-2606-23858; analysis-decision:SF-2026-ARXIV-2606-23872; analysis-decision:SF-2026-ARXIV-2606-23892; analysis-decision:SF-2026-ARXIV-2606-23915; analysis-decision:SF-2026-ARXIV-2606-23927; analysis-decision:SF-2026-ARXIV-2606-23937; analysis-decision:SF-2026-ARXIV-2606-23961; analysis-decision:SF-2026-ARXIV-2606-23969; analysis-decision:SF-2026-ARXIV-2606-23983; analysis-decision:SF-2026-ARXIV-2606-23989; analysis-decision:SF-2026-ARXIV-2606-24004; analysis-decision:SF-2026-ARXIV-2606-24020; analysis-decision:SF-2026-ARXIV-2606-24033; analysis-decision:SF-2026-ARXIV-2606-24040; analysis-decision:SF-2026-ARXIV-2606-24074; analysis-decision:SF-2026-ARXIV-2606-24081; analysis-decision:SF-2026-ARXIV-2606-24119; analysis-decision:SF-2026-ARXIV-2606-24124; analysis-decision:SF-2026-ARXIV-2606-24133; analysis-decision:SF-2026-ARXIV-2606-24143; analysis-decision:SF-2026-ARXIV-2606-24151; analysis-decision:SF-2026-ARXIV-2606-24177; analysis-decision:SF-2026-ARXIV-2606-24204; analysis-decision:SF-2026-ARXIV-2606-24245; analysis-decision:SF-2026-ARXIV-2606-24311; analysis:DA-20260624-2606-24322; analysis-decision:SF-2026-ARXIV-2606-24402; analysis-decision:SF-2026-ARXIV-2606-24408; analysis-decision:SF-2026-ARXIV-2606-24428; analysis-decision:SF-2026-ARXIV-2606-24437; analysis-decision:SF-2026-ARXIV-2606-24467; analysis-decision:SF-2026-ARXIV-2606-24506; analysis-decision:SF-2026-ARXIV-2606-24535; analysis-decision:SF-2026-ARXIV-2606-24551; analysis-decision:SF-2026-ARXIV-2606-24598; analysis-decision:SF-2026-ARXIV-2606-24626; analysis-decision:SF-2026-ARXIV-2606-24722; analysis-decision:SF-2026-ARXIV-2606-24774; analysis-decision:SF-2026-ARXIV-2606-24775 | SELECTION-OWNER-REBUILD-20260624: eligibility and at-most-three narrative choice require independent comparison after owner transfer | Open — canonical selection receipts are structurally reconstructed | open |
| SA-20260624-BOOKS-OWNER-REBUILD | fresh-context:pending-owner-rebuild | books | books-review:SF-2026-ARXIV-2606-23740; books-review:SF-2026-ARXIV-2606-23743; books-review:SF-2026-ARXIV-2606-23752; books-review:SF-2026-ARXIV-2606-23754; books-review:SF-2026-ARXIV-2606-23768; books-review:SF-2026-ARXIV-2606-23797; books-review:SF-2026-ARXIV-2606-23858; books-review:SF-2026-ARXIV-2606-23872; books-review:SF-2026-ARXIV-2606-23892; books-review:SF-2026-ARXIV-2606-23915; books-review:SF-2026-ARXIV-2606-23927; books-review:SF-2026-ARXIV-2606-23937; books-review:SF-2026-ARXIV-2606-23961; books-review:SF-2026-ARXIV-2606-23969; books-review:SF-2026-ARXIV-2606-23983; books-review:SF-2026-ARXIV-2606-23989; books-review:SF-2026-ARXIV-2606-24004; books-review:SF-2026-ARXIV-2606-24020; books-review:SF-2026-ARXIV-2606-24033; books-review:SF-2026-ARXIV-2606-24040; books-review:SF-2026-ARXIV-2606-24074; books-review:SF-2026-ARXIV-2606-24081; books-review:SF-2026-ARXIV-2606-24119; books-review:SF-2026-ARXIV-2606-24124; books-review:SF-2026-ARXIV-2606-24133; books-review:SF-2026-ARXIV-2606-24143; books-review:SF-2026-ARXIV-2606-24151; books-review:SF-2026-ARXIV-2606-24177; books-review:SF-2026-ARXIV-2606-24204; books-review:SF-2026-ARXIV-2606-24245; books-review:SF-2026-ARXIV-2606-24311; books-review:SF-2026-ARXIV-2606-24322; books-review:SF-2026-ARXIV-2606-24402; books-review:SF-2026-ARXIV-2606-24408; books-review:SF-2026-ARXIV-2606-24428; books-review:SF-2026-ARXIV-2606-24437; books-review:SF-2026-ARXIV-2606-24467; books-review:SF-2026-ARXIV-2606-24506; books-review:SF-2026-ARXIV-2606-24535; books-review:SF-2026-ARXIV-2606-24551; books-review:SF-2026-ARXIV-2606-24598; books-review:SF-2026-ARXIV-2606-24626; books-review:SF-2026-ARXIV-2606-24722; books-review:SF-2026-ARXIV-2606-24774; books-review:SF-2026-ARXIV-2606-24775 | BOOKS-OWNER-REBUILD-20260624: Books comparisons are frozen provenance pending upstream semantic gates and root writeback reconciliation | Open — month-local Books queue remains frozen | open |
## 8. Ignored Noise

候选分母外 identity 已在 full-population semantic screening ledger 中按 family-specific 理由关闭；Coverage Receipt 与 source packet 保留 raw、retained、closure 和 route-negative 账目，正文不重复展开低耐久度或越界项目。

### Materials and Access

- 42/42 exact-v1 identities completed official arXiv HTML full-text review; no later-version claim used.

## 9. Recommended Action

- Final Books disposition: 42 Integrate across 19 unique owner files; Books Gate Passed after the 42/42 post-write fresh audit.

## 10. Repository Changes

- This lane wrote 42 source-family deltas into 19 shared Books owners under the granted lock, updated the 2026-06-24 Daily/source packet, and left `docs/LEARNING_STATE.md` unchanged.

## 11. Open Questions

- None. All 42 writebacks and their owner/adjacent handoffs passed the fresh post-write audit.

## 12. Sources

- [Weight-Space Geometry of Offline Reasoning Training](https://arxiv.org/abs/2606.23740v1) — first-public（Asia/Shanghai）：2026-06-24；exact evidence：v1；accessed：2026-09-03
- [Sol Video Inference Engine: Agent-Native Full-Stack Acceleration Framework for Efficient Video Generation](https://arxiv.org/abs/2606.23743v1) — first-public（Asia/Shanghai）：2026-06-24；exact evidence：v1；accessed：2026-09-03
- [ESAA-Conversational: An Event-Sourced Memory Layer for Continuity, Handoff, and Curation Across Heterogeneous LLM Coding Agents](https://arxiv.org/abs/2606.23752v1) — first-public（Asia/Shanghai）：2026-06-24；exact evidence：v1；accessed：2026-09-03
- [Verifiable Foundation Models for Robot Safety](https://arxiv.org/abs/2606.23754v1) — first-public（Asia/Shanghai）：2026-06-24；exact evidence：v1；accessed：2026-09-03
- [Cryptographic certificates of validity for trustworthy AI](https://arxiv.org/abs/2606.23768v1) — first-public（Asia/Shanghai）：2026-06-24；exact evidence：v1；accessed：2026-09-03
- [From Task-Guided Conversational Graphs to Goal-Oriented Dialogue Runtimes](https://arxiv.org/abs/2606.23797v1) — first-public（Asia/Shanghai）：2026-06-24；exact evidence：v1；accessed：2026-09-03
- [Are Safety Guarantees in Neural Networks Safe? How to Compute Trustworthy Robustness Certifications](https://arxiv.org/abs/2606.23858v1) — first-public（Asia/Shanghai）：2026-06-24；exact evidence：v1；accessed：2026-09-03
- [MGI: Member vs Generated Inference](https://arxiv.org/abs/2606.23872v1) — first-public（Asia/Shanghai）：2026-06-24；exact evidence：v1；accessed：2026-09-03
- [REALM: A Unified Red-Teaming Benchmark for Physical-World VLMs](https://arxiv.org/abs/2606.23892v1) — first-public（Asia/Shanghai）：2026-06-24；exact evidence：v1；accessed：2026-09-03
- [Do LLM Attribution Metrics Transfer? Auditing Retrieval-Augmented Generation Evaluation Across Datasets and Constructs](https://arxiv.org/abs/2606.23915v1) — first-public（Asia/Shanghai）：2026-06-24；exact evidence：v1；accessed：2026-09-03
- [RIFT-Bench: Dynamic Red-teaming For Agentic AI Systems](https://arxiv.org/abs/2606.23927v1) — first-public（Asia/Shanghai）：2026-06-24；exact evidence：v1；accessed：2026-09-03
- [When Retrieval Metrics Mislead: Measuring Policy Signal in Long-Horizon Tool-Use Agents](https://arxiv.org/abs/2606.23937v1) — first-public（Asia/Shanghai）：2026-06-24；exact evidence：v1；accessed：2026-09-03
- [Forget Without Compromise: Nexus Sampling for Streaming KV-Cache Eviction Under Fixed Budgets](https://arxiv.org/abs/2606.23961v1) — first-public（Asia/Shanghai）：2026-06-24；exact evidence：v1；accessed：2026-09-03
- [The Serialized Bridge: Understanding and Recovering LLM Serving Performance under Blackwell GPU Confidential Computing](https://arxiv.org/abs/2606.23969v1) — first-public（Asia/Shanghai）：2026-06-24；exact evidence：v1；accessed：2026-09-03
- [Maestro Order: A Model-Agnostic Orchestration Harness](https://arxiv.org/abs/2606.23983v1) — first-public（Asia/Shanghai）：2026-06-24；exact evidence：v1；accessed：2026-09-03
- [Faithful by Construction: Claim-Anchored Attribution for Multi-Document Summarization](https://arxiv.org/abs/2606.23989v1) — first-public（Asia/Shanghai）：2026-06-24；exact evidence：v1；accessed：2026-09-03
- [Towards Spec Learning: Inference-Time Alignment from Preference Pairs](https://arxiv.org/abs/2606.24004v1) — first-public（Asia/Shanghai）：2026-06-24；exact evidence：v1；accessed：2026-09-03
- [You Don't Need to Run Every Eval](https://arxiv.org/abs/2606.24020v1) — first-public（Asia/Shanghai）：2026-06-24；exact evidence：v1；accessed：2026-09-03
- [RoPE-Aware Bit Allocation for KV-Cache Quantization](https://arxiv.org/abs/2606.24033v1) — first-public（Asia/Shanghai）：2026-06-24；exact evidence：v1；accessed：2026-09-03
- [Towards Version-aware Operations and Transaction Memories for Multi-layer MeMo](https://arxiv.org/abs/2606.24040v1) — first-public（Asia/Shanghai）：2026-06-24；exact evidence：v1；accessed：2026-09-03
- [Token Complexity of Certifying Stochastic-Oracle Reliability](https://arxiv.org/abs/2606.24074v1) — first-public（Asia/Shanghai）：2026-06-24；exact evidence：v1；accessed：2026-09-03
- [PixJail: Self-Evolving Paper-to-Pipeline Reproduction for Text-to-Image Jailbreak Evaluation](https://arxiv.org/abs/2606.24081v1) — first-public（Asia/Shanghai）：2026-06-24；exact evidence：v1；accessed：2026-09-03
- [When Top-1 Fails: Calibrating LoRA Monitors for Masked Diffusion LMs](https://arxiv.org/abs/2606.24119v1) — first-public（Asia/Shanghai）：2026-06-24；exact evidence：v1；accessed：2026-09-03
- [VeryTrace: Verifying Reasoning Traces through Compilable Formalism and Structured Verification](https://arxiv.org/abs/2606.24124v1) — first-public（Asia/Shanghai）：2026-06-24；exact evidence：v1；accessed：2026-09-03
- [Holistic Data Scheduler for LLM Pre-training via Multi-Objective Reinforcement Learning](https://arxiv.org/abs/2606.24133v1) — first-public（Asia/Shanghai）：2026-06-24；exact evidence：v1；accessed：2026-09-03
- [AsyncOPD: How Stale Can On-Policy Distillation Be?](https://arxiv.org/abs/2606.24143v1) — first-public（Asia/Shanghai）：2026-06-24；exact evidence：v1；accessed：2026-09-03
- [Metis: Bridging Text and Code Memory for Self-Evolving Agents](https://arxiv.org/abs/2606.24151v1) — first-public（Asia/Shanghai）：2026-06-24；exact evidence：v1；accessed：2026-09-03
- [Agon: An Autonomous Large-Scale Omnidisciplinary Research System Built on Prompt Economy](https://arxiv.org/abs/2606.24177v1) — first-public（Asia/Shanghai）：2026-06-24；exact evidence：v1；accessed：2026-09-03
- [Unified Dominance Graph for Interval-Predicate Approximate Nearest Neighbor Search](https://arxiv.org/abs/2606.24204v1) — first-public（Asia/Shanghai）：2026-06-24；exact evidence：v1；accessed：2026-09-03
- [AutoSpec: Safety Rule Evolution for LLM Agents via Inductive Logic Programming](https://arxiv.org/abs/2606.24245v1) — first-public（Asia/Shanghai）：2026-06-24；exact evidence：v1；accessed：2026-09-03
- [LemonHarness Technical Report](https://arxiv.org/abs/2606.24311v1) — first-public（Asia/Shanghai）：2026-06-24；exact evidence：v1；accessed：2026-09-03
- [Securing LLM-Agent Long-Term Memory Against Poisoning: Non-Malleable, Origin-Bound Authority with Machine-Checked Guarantees](https://arxiv.org/abs/2606.24322v1) — first-public（Asia/Shanghai）：2026-06-24；exact evidence：v1；accessed：2026-09-03
- [Poisoned Playbooks: Demystifying Knowledge Poisoning Effects on AI Security Agents](https://arxiv.org/abs/2606.24402v1) — first-public（Asia/Shanghai）：2026-06-24；exact evidence：v1；accessed：2026-09-03
- [Natural Identifiers for Privacy and Data Audits in Large Language Models](https://arxiv.org/abs/2606.24408v1) — first-public（Asia/Shanghai）：2026-06-24；exact evidence：v1；accessed：2026-09-03
- [Escaping the Self-Confirmation Trap: An Execute-Distill-Verify Paradigm for Agentic Experience Learning](https://arxiv.org/abs/2606.24428v1) — first-public（Asia/Shanghai）：2026-06-24；exact evidence：v1；accessed：2026-09-03
- [ReM-MoA: Reasoning Memory Sustains Mixture-of-Agents Scaling](https://arxiv.org/abs/2606.24437v1) — first-public（Asia/Shanghai）：2026-06-24；exact evidence：v1；accessed：2026-09-03
- [CompressKV: Semantic-Retrieval-Guided KV-Cache Compression for Resource-Efficient Long-Context LLM Inference](https://arxiv.org/abs/2606.24467v1) — first-public（Asia/Shanghai）：2026-06-24；exact evidence：v1；accessed：2026-09-03
- [CrossPool: Efficient Multi-LLM Serving for Cold MoE Models through KV-Cache and Weight Disaggregation](https://arxiv.org/abs/2606.24506v1) — first-public（Asia/Shanghai）：2026-06-24；exact evidence：v1；accessed：2026-09-03
- [Governed Shared Memory for Multi-Agent LLM Systems](https://arxiv.org/abs/2606.24535v1) — first-public（Asia/Shanghai）：2026-06-24；exact evidence：v1；accessed：2026-09-03
- [GUI vs. CLI: Execution Bottlenecks in Screen-Only and Skill-Mediated Computer-Use Agents](https://arxiv.org/abs/2606.24551v1) — first-public（Asia/Shanghai）：2026-06-24；exact evidence：v1；accessed：2026-09-03
- [Toward Self-Evolution-Ready Workflow Harnesses: A Reversible Migration Path and Convertibility Taxonomy for Expert LLM Pipelines](https://arxiv.org/abs/2606.24598v1) — first-public（Asia/Shanghai）：2026-06-24；exact evidence：v1；accessed：2026-09-03
- [SAFARI: Scaling Long Horizon Agentic Fault Attribution via Active Investigation](https://arxiv.org/abs/2606.24626v1) — first-public（Asia/Shanghai）：2026-06-24；exact evidence：v1；accessed：2026-09-03
- [Decentralised AI Training and Inference with BlockTrain](https://arxiv.org/abs/2606.24722v1) — first-public（Asia/Shanghai）：2026-06-24；exact evidence：v1；accessed：2026-09-03
- [Revealing Training Data Exposure in Vision Language Large Models via Parameter Gradients](https://arxiv.org/abs/2606.24774v1) — first-public（Asia/Shanghai）：2026-06-24；exact evidence：v1；accessed：2026-09-03
- [Are We Ready For An Agent-Native Memory System?](https://arxiv.org/abs/2606.24775v1) — first-public（Asia/Shanghai）：2026-06-24；exact evidence：v1；accessed：2026-09-03
## 13. Final Status

Daily V2.1 的 Coverage=Closed、Evidence=Passed、Books=Passed；Completion Status=Complete。机器校验只证明接口一致，语义结论仍由第 7 节记录的 fresh-context audit 承担。

State Truth: Completion=In Progress；Coverage=Open；Evidence=Open；Books=Open；Unresolved Findings=1。
