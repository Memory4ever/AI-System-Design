# 2026-05-08 Root Books Writeback

## 写回结果

以下 7 个 Source Family 已按唯一 Stable Knowledge Node 写入机制正文，而不是只追加来源标签：

| Source Family | Owner | 写回命题 |
| --- | --- | --- |
| `SF-2026-ARXIV-2605-05594` | `AGENT-RAG` | 多模态 evidence admission 必须检查模态覆盖、冲突与支配；attention 只作诊断，不能充当 truth score。 |
| `SF-2026-ARXIV-2605-05657` | `AGENT-MULTI-AGENT` | 确定成本下以 resource algebra 作为拓扑准入证书；随机成本回退 runtime accounting。 |
| `SF-2026-ARXIV-2605-05818` | `PLATFORM-SECURITY` | RAG 泄露按跨轮 extraction state 与模块组合累计；faithfulness 不等于 confidentiality。 |
| `SF-2026-ARXIV-2605-05838` | `MODEL-LONG-CONTEXT` | 二阶 momentum recurrence 必须保持 chunk-parallel training 与 recurrent decode 的代数一致。 |
| `SF-2026-ARXIV-2605-06014` | `INFER-TENSORRT-LLM` | transform count 必须与 scalar/block quantizer 的分布假设和 moment check 共同进入 Numeric Plan。 |
| `SF-2026-ARXIV-2605-06326` | `TRAIN-SFT` | tool-use SFT 由 task suitability、teacher trajectory learnability、mixture 与 checkpoint 联合准入，再交 RLVR。 |
| `SF-2026-ARXIV-2605-06631` | `PLATFORM-EVALUATION-SYSTEM` | compression release 要比较 paired excess answer error 与 worst-family confidence bound。 |

## Root 首轮检查

- 每项均写入既有 owner 的论证主线，并保留旧方案适用条件、代价、failure mode、fallback 与证据边界。
- 7 个 `semantic-body-binding` 唯一；没有把论文名称堆成独立方法列表。
- Daily 中对应状态已从 `Queued` 同步为 `Applied`。
- 此记录不是独立 Gate；需要未参与作者修复与本次写回的新 reviewer 完成 post-write semantic audit。

## 第二轮写回结果

以下 5 个 Source Family 已继续按唯一 owner 写入机制正文：

| Source Family | Owner | 写回命题 |
| --- | --- | --- |
| `SF-2026-ARXIV-2605-05715` | `PLATFORM-EVALUATION-SYSTEM` | 将 failure signal 的可解码性、干预有效性与决策权限拆开；固定 steering 失败时只允许校准后的 abstention/escalation。 |
| `SF-2026-ARXIV-2605-05750` | `TRAIN-RLHF` | 多目标 reward 的 bottleneck 聚合是风险敏感分支，不可冒充 hard constraint。 |
| `SF-2026-ARXIV-2605-06036` | `TRAIN-RLHF` | preference admission 可拒绝 noisy mass，但必须保留选择 mask、版本与 dispute path，并承认 systematic noise 与二次成本。 |
| `SF-2026-ARXIV-2605-06078` | `TRAIN-GRPO` | milestone 是 terminal reward 与逐 action causal credit 之间的中间粒度，不拥有因果归因。 |
| `SF-2026-ARXIV-2605-06200` | `TRAIN-GRPO` | turn index 只能作为受限 comparison key，不能替代真实 state equivalence。 |

## Root 第二轮检查

- 5 个 `semantic-body-binding` 均唯一，正文位于 Review notes 之前。
- 每项均写明旧基线、约束变化、状态或控制权、代价、failure mode、fallback 与论文未证明的范围。
- `git diff --check` 对三个目标 Books 文件通过。
- Daily 与 V3 活动账本已同步为 `Integrate — Applied`；该同步仍不代替 fresh-context 独立终审。
