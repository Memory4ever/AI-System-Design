# 2026-05-13 V3 Round 8 Fresh Non-author Post-write Review

- 复核者：`fresh-nonauthor:may13-round8-postwrite-20260915`
- 独立性：未参与 Round 8 作者返修及最初五项 root 写回。
- 范围：Round 8 六项、五项 Books binding、`2605.11059` No Change 对读、冻结算术、163 项结构化对账及 Round 7 去重边界。
- 结论：**未通过；Daily 保持 Ongoing。**

## 逐项结论

| arXiv | 结论 | 写后语义判断 |
| --- | --- | --- |
| `2605.10981` | 未通过；root 已在初审后修复，尚待另一位 reviewer | 原写回把 SimPO 的 `beta/gamma` 与 ξ-DPO 的 `xi` 写成同一分支的并列旋钮，并把减少联合调参误写为“更细的旋钮/放大 sweep”。exact-v1 的关键恰是 ratio reward 消去 `beta`、以单一有界 `xi` 取代 `gamma`。 |
| `2605.11181` | 通过 | 唯一 `TRAIN-PRETRAINING` binding 正确收窄“精确 LMO/全局几何”的因果解释，分离 spectrum suppression、alignment、descent potential 与 step-size matching；保留 GPT-2/random-feature 边界、Kaon 非推荐和 AdamW/Muon fallback。 |
| `2605.11235` | 通过 | 唯一 `TRAIN-GRPO` binding 将 same-policy ICL judgment、Top-B allocation 与 self-judgment reward 限定为 curriculum sensor，external verifier 保留 outcome authority；87.6% parse failure、作者 workload 数字和三类 fallback 均保留。 |
| `2605.11290` | 通过 | 唯一 `TRAIN-SFT` binding 在 fixed token budget 下承载 capability state、saturation、spillover 与动态 teacher allocation；probe/taxonomy/teacher/safety/privacy 边界及 static/uniform/staged fallback 均明确。 |
| `2605.11311` | 通过 | 唯一 `MULTIMODAL-GENERATIVE-PARADIGMS` binding 区分单样本 Gaussian marginal 与 batch joint contract，明确 coupling、sampler、gallery evaluator 的控制权；作者模型、2,000 prompts、三图 gallery 边界及 independent-seed fallback 均保留。 |
| `2605.11059` | No Change 通过 | `TRAIN-PRETRAINING` 已要求 depth/width 参数化同时稳定 forward 与 update scale，并明确数学 scaling limit 不能独自签发真实 schedule；exact-v1 的 attention-only、finite-time 条件不会改变现有长期命题。 |

五项 Books binding 在初审时均为唯一 owner、起止各一处并位于各章 `## Review notes` 前；四项通过正文均真实承载旧方案成立条件、约束变化、state/control owner、exact-v1 证明与未证明、trade-off、failure 和 fallback。`2605.10981` 的 marker/owner/位置通过，但命题内容未通过，不能用结构正确替代语义 Gate。

## 冻结对账与去重

- 分母：`163 retained + 484 pre-denominator closure + 191 isolation = 838`，其中 owner-day 为 `163 + 484 = 647`，withdrawn=`0`。
- `v3-active-ledger.json` 的候选 ID、`v3-active-evidence.json` 的 review 与 `v3-books-comparison.json` 的 comparison 均为 163 个唯一 Source Family，集合一致；163 项都有 Evidence 与 Books disposition。
- Round 7 scope 六项与 Round 8 scope 六项交集为空；Round 7 已通过的 83 项没有进入本轮新增队列或被重复追加。
- Round 8 的 5 项 Integrate 均已由 root 写入；本轮通过 4 项，1 项进入 `V3_ROUND8_ROOT_SEMANTIC_REPAIR_QUEUE_20260915.md`。

## 失败项与后续边界

root 已在本审计 finding 之后写入 `ROOT_ROUND8_BOOKS_REPAIR_2605_10981_20260915.md`。为保持 reviewer 独立性，本 reviewer 不对该后续修改签字，也不据 root repair record 推断语义已通过。

精确剩余 Gate 只有一项：另一位未参与 root 修复的 fresh non-author 仅复核 `2605.10981` 的修复后 binding，确认 `beta/gamma` 属于 SimPO 诊断、ξ-DPO 消去 `beta` 并以单一 `xi` 取代 `gamma`，同时保留 quantile 状态、LeakyReLU、Appendix A 边界与 DPO/SimPO fallback。通过前 05-13 必须保持 Ongoing；不得重开其他 162 个 retained candidate、484 closure、191 isolation 或 Round 7 的 83 项。

## 机械检查

- `scripts/validate_research.py`：通过；该结果只证明接口一致性，不替代上述语义失败。
- JSON 解析、`163/163/163` 集合对账与 `163 + 484 + 191 = 838`：通过。
- Round 7 / Round 8 scope 交集为空；五项 marker 各一组且位于 `## Review notes` 前：通过。
- scoped `git diff --check`：通过。
