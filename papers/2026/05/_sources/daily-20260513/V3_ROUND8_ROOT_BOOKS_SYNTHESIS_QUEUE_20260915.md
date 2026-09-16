# 2026-05-13 V3 Round 8 Root Books 串行队列

## 不变量

- 本队列只含 5 项新写回；`2605.11059` 为 No Change，不写 Books。
- Round 7 及之前已经应用并通过独立写后复核的 83 项不得重复追加。
- 按日期与 owner 文件串行写入；每项写入现有论证主干，不在章末堆论文摘要。
- 每项正文必须包含旧基线、约束变化、机制与 state/control owner、exact-v1 证明与未证明、trade-off/failure、fallback/coexistence。
- root 写后更新 JSON queue 与 README，但不能代替另一位 fresh non-author 终审。

## 1. 2605.10981 → TRAIN-DPO

- 文件：`books/part-04-training-system/34-dpo.md`
- Anchor：`Preference Scale 与 Optimization Scale 不应共用一个旋钮`
- 增量：补充 `beta` 的 sigmoid-saturation sample filtering、`gamma` 的 dataset-gap dependence，以及 bounded ratio margin `xi`。
- 边界：四个 preference datasets 与所测 7B/8B 模型；late-stage target likelihood collapse 未解释；代码未绑定 immutable commit。
- Fallback：vanilla DPO/SimPO、显式 sweep、raw gap/KL/likelihood/行为联合监控。

## 2. 2605.11181 → TRAIN-PRETRAINING

- 文件：`books/part-04-training-system/28-pretraining.md`
- Anchor：`Whitening 的收益取决于 Gradient Spectrum 所在 Regime`
- 类型：纠错型写回。
- 增量：不要再让“matrix-aware 保留二维几何”暗示精确 LMO/全局几何是性能原因；写成 spectrum suppression、alignment、descent potential 与 step-size matching 的可验证分解。
- 边界：单一 GPT-2 architecture，理论/诊断主要限 random-feature model；不能推广为 Kaon deployment recommendation。
- Fallback：matched-budget AdamW/Muon baseline，按 update norm、loss trajectory 与 noise regime 比较。

## 3. 2605.11235 → TRAIN-GRPO

- 文件：`books/part-04-training-system/33-grpo.md`
- Anchor：`Group Size 改变什么` 中 reward-variance curriculum 段落之后。
- 增量：same-policy ICL judgment + Top-B allocation + self-judgment reward 是 curriculum sensor 的条件分支；external verifier 仍拥有 outcome truth。
- 边界：作者 workload 的最高 67% wall-clock reduction 与约 3.9% overhead 不外推；移除 ICL evidence 的 87.6% parse failure 必须保留。
- Fallback：random coverage slice、static curriculum、external selector。

## 4. 2605.11290 → TRAIN-SFT

- 文件：`books/part-04-training-system/29-sft.md`
- Anchor：`从平均拟合转向覆盖尚未学会的序列`
- 增量：fixed token budget 下按 capability state、saturation 与 cross-capability spillover 动态分配 targeted teacher supervision。
- 边界：作者 teacher/student、20M/150M token budgets、八类 capability 与 evaluator；probe/taxonomy/safety/privacy 均受限。
- Fallback：static mixture、均匀探索、staged distillation。

## 5. 2605.11311 → MULTIMODAL-GENERATIVE-PARADIGMS

- 文件：`books/part-03-multimodal-world-models/24-multimodal-generative-paradigms.md`
- Anchor：`Continuous 与 Discrete Flow 的等价是有条件的`之后，作为 source/coupling identity 的 batch-level 分支。
- 增量：保持单样本 `N(0,I)` marginal 不变，通过 joint noise coupling 控制 gallery diversity；independent seeds 只是 joint contract 的一个选择。
- 边界：SD1.5/SDXL/SD3、2,000 COCO prompts、三图 gallery 与作者 metrics；未证明所有 sampler、gallery size 或 production SLO。
- Fallback：单图、强复现、failure isolation 或 coupling 未校准时使用 independent seeds。

## 完成条件

5 项均写入唯一 owner 的机制正文，binding 唯一且位于 `## Review notes` 前；queue 更新为 88 applied / 0 pending 后，交由未参与本轮作者返修与 root 写入的 fresh non-author reviewer 做逐命题写后审计。在此之前 2026-05-13 必须保持 `Ongoing`。

