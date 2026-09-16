# 2026-05-13 V3 Round 8 Fresh Non-author Review After 2605.10981 Repair

- 复核者：`fresh-nonauthor:may13-round8-10981-postrepair-20260915`
- 独立性：未参与 Round 8 作者返修、初始 root 写回或 `2605.10981` root 修复。
- 范围：只复核 `SF-2026-ARXIV-2605-10981` 的 official exact-v1 与 Ch34 当前唯一 binding；未扩日期、来源、候选分母、其他 Round 8 项或 Round 7 已通过项。
- exact-v1：<https://arxiv.org/html/2605.10981v1>
- 结论：**未通过；Daily 保持 Ongoing。**

## 逐命题复核

| 合同 | 结果 | exact-v1 与当前正文对读 |
| --- | --- | --- |
| SimPO `beta` 的 sample filtering | 通过 | exact-v1 §3.1 与 Appendix E 把 `beta` 对 sigmoid saturation/gradient 的作用解释为隐式过滤；Ch34 明确写出该关系。 |
| SimPO `gamma` 的 dataset-gap dependence | 通过 | exact-v1 §3.2 把 `gamma` 与数据内在 reward-gap 结构绑定；Ch34 没有把它写成跨数据集不变常数。 |
| ratio transformation 消去 `beta` 对 margin 定义的影响 | 通过 | exact-v1 §4.1 的 chosen/rejected ratio normalization 取消公共 `beta` 并把 margin 定义到有界 ratio space；Ch34 已明确表达这一点。 |
| 单一 bounded `xi` 取代 `beta/gamma` 的耦合 margin 调节 | 通过 | exact-v1 §4.1–§4.2 只保留一个可调 `xi`，由初始 gap quantile 提议；Ch34 明确说明 `xi` 不是第三个并列旋钮。 |
| state / trade-off / failure / fallback | 通过 | Ch34 保留 initial-gap quantile、可能的 `xi` schedule、ratio normalization、distribution drift、Appendix A late-stage target-likelihood collapse，以及 DPO/SimPO fallback 与 raw gap/KL/likelihood/behavior 观测。 |
| evidence boundary | **未通过** | Ch34 写“作者四个数据集和所测 7B/8B 模型”，但 exact-v1 §5.1 明确使用 Mistral-7B-Instruct、Llama3-8B-Instruct 与 **Gemma2-9B-Instruct**。当前措辞把所测模型集合错误收窄，不能签署 exact-v1 evidence boundary。 |

## Doubt cycle

- CLAIM：当前 binding 已满足全部方法与证据边界，可以关闭 05-13 Gate。
- EXTRACT：只抽取 Ch34 该 binding 与 exact-v1 §3.1、§3.2、§4.1、§4.2、§5.1、Appendix A/E/F。
- DOUBT：逐项尝试证伪 sample filtering、dataset dependence、`beta` cancellation、单参数 bounded margin、failure/fallback 与实验范围。Cross-model skipped: non-interactive reviewer lane。
- RECONCILE：五项机制/运行边界未发现违约；模型集合遗漏 Gemma2-9B 是 valid + actionable，不是表述偏好。
- STOP：发现一项精确可修复违约，转入单项 root queue；在修复前不继续循环、不扩审其他材料。

## 精确后续动作

只处理 [`V3_ROUND8_ROOT_EVIDENCE_BOUNDARY_REPAIR_QUEUE_20260915.md`](./V3_ROUND8_ROOT_EVIDENCE_BOUNDARY_REPAIR_QUEUE_20260915.md) 中的一处 Books 证据边界。不得改写已经通过的机制、trade-off、failure 或 fallback，也不得追加第二份 binding。root 修复后仍需另一位未参与该修复的 fresh non-author 对这一句和唯一 marker 复核；通过前 2026-05-13 保持 Ongoing。

