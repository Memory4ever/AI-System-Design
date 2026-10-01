# 04/28 第二批开放线索的有限贡献反向剪枝

本页仅从已读的旧库存**完整标题与摘要**、当前 Books 的具体正文及其交接中，检验原“继续核贡献”是否真会改变长期知识；没有为这三项无差别展开全文。结论是作者侧具名**前分母关闭提案**，待非作者核后才改变 70/41 工作漏斗；不对论文领域价值作否定，也不处理首次公开日期。

| Family | 题摘中的真实方法和边界 | 已有命题与为何不再送必要全文 |
| --- | --- | --- |
| `2604.23272` MoSS | Tactile/torque 分流进入 action-stream cross-modal attention；先冻结预训练 VLA 再联合训练，另预测未来物理信号。真实机器人实验支持该受限组合，但摘要未给同成本、同 sensor 校准下能把分流、冻结与预测各自归因的对照。 | Ch23 `Token Hierarchy` 已把高频 tactile event 的独立 rate/timestamp/calibration/稀疏预测目标与共享语义消费分开；Ch25 约944–949已分当前 tactile 条件与未来 contact latent，Ch26保留 action/torque control deadline。MoSS 的具体 tactile+torque/两段冻结 recipe 不改变这组数据身份、预测与控制责任。不是因它是机器人论文而排除；如受控消融可证明 **heterogeneous modality interaction** 在当前三章尚未表达的必需分支，定点重开。 |
| `2604.23366` GSAR | 把 claim 分为 grounded/ungrounded/contradicted/complementary，按 evidence-type 权重评分，再映射 proceed/regenerate/replan；主实验是 FEVER gold Wikipedia evidence 与四个 LLM judges，不是实际多 Agent 执行或 action/effect 正确性。 | Ch66 约1827已把 claim support/contradict/insufficient、independent source、校准后的 answer/retrieve/ask/abstain/escalate 分账；Ch76 约609已有 source certainty、contradiction 与 answer gate。`complementary` 标签及三档循环是该静态代理上的局部实现，未改变谁可发布结论或谁授权行动。不能按摘要“first”自动入选，也不称其结构性质证明无效；若正文有不同于静态 FEVER 的执行前 authority 反例，定点重开。 |
| `2604.23553` ClusterFusion++ | 把既有 cluster-level QKV/attention 融合扩至 GPT-NeoX/Pythia 整个 decoder block，配 CUDA Graph compatible persistent TMA descriptor；单 RTX5090、两组 Pythia 的约1.34×及 FP16 atomics 轻微非确定性，只覆盖该形状/设备。 | Ch49 约57–85已串 kernel fusion、HBM/launch、graph capture/persistent runtime/shape 回退；约532–540明确 thread-block cluster 的 DSMEM、同步、scratch lifetime 和同 shape 非 cluster 基线；约495–516明确 TMA 只管搬运。该稿是现有联立成本合同中的更大 fusion scope 点，不给新 correctness/可移植性不变量或其他模型/硬件反证。若真实 full-block resource/lifetime 约束推翻当前形状选择，定点重开；不因 CUDA 术语新就纳 Books。 |

三个提案仍须独立复核完整题摘和上述实际正文，不能静默从工作上限扣除。`.23210/.23238/.23577/.23584/.23626` 等本批其他开放项未在此被关闭；不按固定比例剪枝。
