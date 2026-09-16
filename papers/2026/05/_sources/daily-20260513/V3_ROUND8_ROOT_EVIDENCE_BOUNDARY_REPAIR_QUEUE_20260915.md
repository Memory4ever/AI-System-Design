# 2026-05-13 V3 Round 8 Root Evidence-boundary Repair Queue

- 状态：`Closed — root repair applied and fresh non-author review passed`
- 唯一 Source Family：`SF-2026-ARXIV-2605-10981`
- Stable Node：`TRAIN-DPO`
- Owner：`books/part-04-training-system/34-dpo.md`
- Binding：`semantic-body-binding:SF-2026-ARXIV-2605-10981`
- exact-v1：<https://arxiv.org/html/2605.10981v1>
- 触发审计：[`V3_ROUND8_FRESH_NONAUTHOR_REVIEW_AFTER_10981_REPAIR_20260915.md`](./V3_ROUND8_FRESH_NONAUTHOR_REVIEW_AFTER_10981_REPAIR_20260915.md)

## 唯一修复

当前 binding 第二段末句写：

> exact-v1 只支持作者四个数据集和所测 7B/8B 模型，不证明免调参或跨数据集普适。

该模型范围不完整。exact-v1 §5.1 明确包含 Mistral-7B-Instruct、Llama3-8B-Instruct 和 Gemma2-9B-Instruct。root 只需在现有 binding 内把证据边界改为等价于：

> exact-v1 只支持作者四个 preference datasets、所测 Mistral-7B-Instruct、Llama3-8B-Instruct 与 Gemma2-9B-Instruct，以及论文披露的 evaluator；不证明免调参、跨数据集普适或 production guarantee。

## 不得改变

- 不改已经通过的 `beta` sample-filtering、`gamma` dataset-gap dependence、ratio normalization 取消 `beta`、单一 bounded `xi` 取代耦合 margin 调节。
- 不删除 initial-gap quantile、LeakyReLU、ratio normalization、distribution drift、late-stage likelihood collapse、DPO/SimPO fallback 或联合观测项。
- 不新增 owner、不追加第二份 binding、不触碰其他 162 个 retained candidate、484 closure、191 isolation、其他 Round 8 项或 Round 7 的 83 项。
- root 修复后，由另一位未参与修复的 fresh non-author 只复核该证据边界与 marker 唯一性；此前 Daily 保持 Ongoing。

## 关闭记录

root 已在唯一 binding 内补齐 Mistral-7B-Instruct、Llama3-8B-Instruct 与 Gemma2-9B-Instruct；新的 fresh non-author reviewer 对读 official exact-v1 §5.1 后通过。关闭审计见 [`V3_ROUND8_FRESH_NONAUTHOR_FINAL_REVIEW_AFTER_10981_EVIDENCE_REPAIR_20260915.md`](./V3_ROUND8_FRESH_NONAUTHOR_FINAL_REVIEW_AFTER_10981_EVIDENCE_REPAIR_20260915.md)。本 queue 不再包含待执行项。
