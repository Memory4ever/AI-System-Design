# 2026-05-20 Fresh Non-author Final Review

**复核者：** `/root/may12_fresh_postwrite`（未参与本日作者 recertification 或 root Books 写回）

**结论：** PASS；Coverage=Closed、Evidence=Passed、Books=Passed、unresolved findings=0。

## 1. Owner、窗口与算术

- 严格窗口为 `[2026-05-19T09:00:00+08:00, 2026-05-20T09:00:00+08:00)`。arXiv 官方 cadence 的 2026-05-19 20:00 ET announcement 换算为 2026-05-20 08:00+08，位于窗口内；owner 不是 DataCite `created/updated`。
- 本地官方 owner receipt 中 `official_arxiv_oai_direct` 为 575 个唯一 identity，ID 范围 `2605.18755`–`2605.20182`；另 152 个 revision/other-owner identity 只作佐证。
- Fresh challenge 推翻作者保留的四个二次 closure：`2605.18810`、`2605.18999`、`2605.19260`、`2605.19619`。它们都满足当前 V3 的机制/显式 trade-off 准入条件；“没有改变 cross-runtime owner”或“Books 已覆盖”均不能作为 denominator exclusion。
- 最终 arXiv 算术：`575 = 70 retained + 505 pre-denominator closure + 0 withdrawn`。作者 14 项 FN override 与本轮 4 项恢复共 18 项，均唯一且属于这 575 个 official owner identity。
- 两个 Google AI date-only 原始事件均为 ROADMAP 明确排除的 AI-for-Science 应用，作为机构来源 pre-denominator closure；因此全日算术为 `577 = 70 retained + 507 closure + 0 withdrawn`。

## 2. 四项恢复的 exact-v1 Evidence 与 Books Decision

### 2605.18810 — D-PACE

- Score：`3+2+3=8`；owner=`INFER-SPECULATIVE-DECODING`。
- Adopted claim：parallel block drafter 的 acceptance bottleneck 会随训练迁移；expected accepted-length surrogate 可把 prefix-survival 与 continuation contribution 分配为动态 per-position CE credit，target verifier 仍独占 accept/commit。
- Evidence：§2 DFlash baseline；§3.1–3.3 method；§4、§5.1–5.6 与 Appendix C–D evaluation/ablation；§7、Appendix A 与 disclosed model/benchmark/hardware 是 non-proof boundary。
- Books：Integrate → `books/part-05-inference-system/48-speculative-decoding.md`。写回保留 fixed decayed CE/Forward-KL 基线、surrogate/temperature/target coupling、数值失稳与重新标定 fallback。

### 2605.18999 — Distance-Aware Muon

- Score：`3+2+3=8`；owner=`TRAIN-PRETRAINING`。
- Adopted claim：normalized direction 与 step scale 是两个 optimizer control；DA/SC/DF-Muon 分别以 explored trajectory、local descent certificate 或 majorized scalar search 选择 step radius，certificate/state 必须进入 optimizer/checkpoint identity。
- Evidence：§2 assumption map；§3–§5 method；§6.1–6.2 与 Appendix D evaluation；bounded trajectory、star-convex/bounded sublevel set、majorized search 和 tested budgets 是 non-proof boundary。
- Books：Integrate → `books/part-04-training-system/28-pretraining.md`。写回保留 tuned fixed-scale Muon/AdamW 基线、certificate failure、trajectory explosion、search cost 与 fallback。

### 2605.19260 — AQuaUI

- Score：`3+2+3=8`；owner=`MULTIMODAL-REPRESENTATION`。
- Adopted claim：GUI screenshot 可按空间信息密度构造 adaptive quadtree、保留代表 token 的 position identity；多步交互可复用前帧 tree，但变化检测失败时必须回退独立或 full-token path。
- Evidence：§3.2–3.3 与 Appendix A method；§4–§5、Appendix B evaluation；model/serving-stack-specific path、Qwen2/Qwen3 差异及小模型 overhead 是 non-proof boundary。
- Books：No Change。Ch23 `### 固定预算要先分配信息责任，再选择具体 Token` 已承载空间/时间 budget、position identity、selector drift 与 dense/full-token fallback；quadtree 是受限实现，不新增长期命题。

### 2605.19619 — MiMuon

- Score：`3+2+3=8`；owner=`TRAIN-PRETRAINING`。
- Adopted claim：singular-gap test 可作为条件正交化 sensor，在 gap 足够时选择 orthogonalized direction，否则切到 momentum-SGD；threshold、branch decision、momentum 与 checkpoint identity 属于 optimizer contract。
- Evidence：§2.1–2.3、§3/Algorithm 2 method；§6.1–6.2 evaluation；§4–§5 假设与两个小型 workload 是 non-proof boundary。Introduction contribution 句把 Muon/MiMuon bound 顺序写反，与 abstract、Table 1、定理及 §7 冲突，未被采作证据。
- Books：Integrate → `books/part-04-training-system/28-pretraining.md`。写回保留 pure Muon/SGDM/AdamW、gap noise、threshold thrashing、SVD/Newton-Schulz cost 与 matched-budget fallback。

最终 Evidence：70/70 exact-v1 deep complete；评分分布 `8 score7 + 51 score8 + 11 score9 = 70`；blocked=0，materials request=0。

## 3. Books Post-write Semantic Review

最终 Books 对账：`70 = 27 prior Applied + 9 root Applied + 34 No Change + 0 Structural Candidate`，即 `36 Applied + 34 No Change`。

| arXiv | Owner file | Marker lines | First `## Review notes` | Semantic result |
| --- | --- | ---: | ---: | --- |
| 2605.18813 | Ch25 | 456–460 | 1034 | PASS |
| 2605.18841 | Ch72 | 1303–1307 | 2494 | PASS |
| 2605.18882 | Ch78 | 602–606 | 664 | PASS |
| 2605.19095 | Ch28 | 1100–1104 | 1269 | PASS |
| 2605.19250 | Ch23 | 453–457 | 648 | PASS |
| 2605.19577 | Ch33 | 1594–1598 | 1985 | PASS |
| 2605.18810 | Ch48 | 148–161 | 901 | PASS |
| 2605.18999 | Ch28 | 278–290 | 1269 | PASS |
| 2605.19619 | Ch28 | 330–340 | 1269 | PASS |

九项 marker 均全局单文件唯一、start/end 成对且位于首个主 `## Review notes` 前。逐项顺读相邻段后，正文均真实承载 old path/why、changed constraint、state/control ownership、benefit/cost、failure、fallback/coexistence 与 exact-v1 non-proof boundary；没有只靠 marker 或 Review notes 充当语义整合。2605.18810 从单-token overlap 自然过渡到 block-position credit；2605.18999 位于 optimizer direction/state 讨论后并回到 role-aware state allocation；2605.19619 紧接固定 Muon/sign schedule，形成 conditional branch，再回到 sign-step geometry，衔接成立。

## 4. Gate Evidence

- `screening-outcomes-v3.json`、`official-owner-batch-evidence-v3.json`、`evidence-review-v3.json`、`books-comparison-v3.json` 与 `root-books-writeback-queue-v3.json` 均通过 JSON parse 和集合/算术断言。
- `scripts/validate_research.py --report papers/2026/05/20/README.md`：PASS。
- 九项 Books marker uniqueness/pair/placement：PASS。
- Scoped `git diff --check`：PASS。
- Cross-model review：本项为非交互式 delegated fresh-review lane，未另启 cross-model reviewer；作者与 root writer 均未参与本次最终语义签字。
