# 2026-05-13 V3 有界六项作者返修

## 范围

本轮只处理 fresh non-author 终审指定的六项，不重新枚举来源、不扩日期窗口、不触碰 191 项 revision/non-owner-route isolation，也不修改共享 Books。

## 结论

| arXiv | 修复前 | 修复后 | V3 | Owner |
| --- | --- | --- | --- | --- |
| 2605.11905 | pre-denominator closure | Integrate — Root write required | 2+2+2=6 | TRAIN-DATA |
| 2605.11931 | pre-denominator closure | Integrate — Root write required | 2+2+2=6 | TRAIN-SFT |
| 2605.12201 | pre-denominator closure | Integrate — Root write required | 3+2+3=8 | PLATFORM-EVALUATION-SYSTEM |
| 2605.10974 | No Change — Existing Coverage | Integrate — Root write required | 2+2+3=7 | PLATFORM-EVALUATION-SYSTEM |
| 2605.11317 | No Change — Existing Coverage | Integrate — Root write required | 3+2+3=8 | INFER-REQUEST-LIFECYCLE |
| 2605.12446 | No Change — Existing Coverage | Integrate — Root write required | 3+2+3=8 | PLATFORM-EVALUATION-SYSTEM |

三项重开论文的 exact-v1 HTML 均可访问，标题与身份一致，检查时未见官方 withdrawal banner。Method、evaluation、limitations 与 artifact boundary 已写入 v3-active-evidence.json。

## Books 对读

- 2605.11905：Ch27 有轨迹与数据治理背景，但没有 step、segment、whole-proof 的 supervision-unit 演进，也没有训练边界与 goal-aware rollout 的复用。
- 2605.11931：Ch29 有困难样本和 SFT 数据质量，但没有 partial-correct prefix resampling、视觉注意传感器及 SFT/DPO/GRPO 分支间的 handoff。
- 2605.12201：Ch66 有通用 prediction-set 讨论，但没有多有效输出、partial-program set、multiple hypothesis testing 和 selective-execution 风险交换。
- 2605.10974：Ch66 的通用 evidence contract 不能替代 interval-only softmax bound 的最优性证明，也没有说明继续收紧必须增加 correlation/coupling 信息。
- 2605.11317：Ch42 的普通请求状态机没有 session local manifold、小 surrogate 适配、switch 与 rollback。
- 2605.12446：Ch66 的通用 confidence/calibration 没有 decoupled confidence generation、order-aware reward 和 finite-sample/reference-drift/DPO 边界。

因此六项都不能继续使用 No Change 或 denominator closure。

## 状态同步

- 838 个 identity 保持不变。
- official-owner route 从 148 retained / 499 closure 修正为 151 retained / 496 closure。
- 151 项 Evidence 与 Books comparison 已齐备。
- 旧 root queue 的 71 项已按当前工作树同步为 applied。
- 唯一 root queue 为 v3-root-writeback-queue.json：77 项中 71 applied、6 pending。
- Round 5 独立 queue 的 26 项已同步为 root applied；本轮六项不在多个 queue 重复维护。

## Gate

作者返修结束，但不能自签 Complete。Daily 继续 Ongoing，等待 root 串行写入六项 Books 正文，以及新的 fresh non-author post-write review。

