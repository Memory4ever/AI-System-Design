# 2026-05-13 V3 Round 8 Root Semantic Repair Queue

- 生成者：`fresh-nonauthor:may13-round8-postwrite-20260915`
- 范围：仅 `SF-2026-ARXIV-2605-10981`；不得扩窗、扩源、重审 838 identity、触碰 191 isolation 或重复 Round 7 的 83 项。
- 初审状态：Books 写后语义未通过。
- 当前状态：root 已在本次审计之后记录修复；本 reviewer 未复核修复结果，仍须另一位 fresh non-author 终审。

## 唯一修复项

- Source Family：`SF-2026-ARXIV-2605-10981`
- exact-v1：`https://arxiv.org/html/2605.10981v1`
- Stable Node：`TRAIN-DPO`
- Owner：`books/part-04-training-system/34-dpo.md`
- Anchor：`Preference Scale 与 Optimization Scale 不应共用一个旋钮`
- Binding：`semantic-body-binding:SF-2026-ARXIV-2605-10981`
- 初审缺陷：原写回把 SimPO 的 `beta` sample filtering、`gamma` dataset-gap dependence 与 ξ-DPO 的 `xi` 写成同一 ratio-margin 分支的并列旋钮，并以“更细的旋钮/放大 sweep”描述 trade-off。这会让读者误以为 ξ-DPO 同时使用 `beta`、`gamma`、`xi`。

## 修复合同

1. 先保留旧基线：SimPO 的 `beta` 通过 sigmoid saturation 隐式过滤样本，`gamma` 的含义依赖数据集 reward-gap 结构，因此跨数据集需要联合调参。
2. 再写约束变化：ξ-DPO 通过 logit transformation 移除 sigmoid 梯度饱和的影响，并用 chosen/rejected ratio reward 消去 `beta`；`xi` 是取代 SimPO `gamma` 的唯一可调、有界 ratio margin，不是第三个并列旋钮。
3. 写清状态与控制权：`xi` 由初始 reward-gap distribution 的 quantile 提议；LeakyReLU 避免已超过 margin 的样本被强行拉回；trainer 仍拥有 update commit。
4. 写清代价与失败：减少的是 `beta/gamma` 联合 sweep，新增的是 initial-gap quantile、数据漂移和可能的动态 `xi` 状态；Appendix A 的 late-stage target-policy log probability collapse 原因仍未知。
5. 保留证据边界与 fallback：只覆盖作者四个 preference datasets 和所测 7B/8B 模型；代码未绑定 immutable commit；校准失配、ratio instability 或 likelihood collapse 时回退 vanilla DPO/SimPO、显式 sweep，并联合监控 raw gap、KL、chosen/rejected likelihood 与行为结果。

## 写后 Gate

- 只允许替换上述唯一 binding 内的正文，不新建 owner、不追加第二份 binding、不修改其他四项或 Round 7 内容。
- binding 起止各一处，仍位于 `## Review notes` 前。
- root 修复记录：`ROOT_ROUND8_BOOKS_REPAIR_2605_10981_20260915.md`。
- 完成 root 修复不等于通过；另一位未参与该修复的 fresh non-author 必须逐命题核验后，才能把 05-13 从 Ongoing 改为 Complete。
