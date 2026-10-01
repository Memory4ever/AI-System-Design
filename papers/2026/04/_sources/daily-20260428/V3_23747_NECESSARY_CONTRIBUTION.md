# 2604.23747v1：训练比较的失真分母（作者侧必要审阅）

此记录只为 04/28 的贡献准入与必要证据定位；不是首次公开证明、正式评分、Books 写前许可或日级 Gate。[官方 exact-v1](https://arxiv.org/html/2604.23747v1) §2.1–2.2、§3、§4/Table 1–3 和 §6 为唯一采用版本；HTML 页头 `26 Apr` 不当公开时刻。后续仍须官方公告槽、连续身份和 OAI 组合核日期。

## 可采用的窄机制与现有 owner 差异

§2.1 的特定 DeepSpeed ZeRO-1/2 + CPU-offloaded Adam 路径在梯度累积中只把首个 micro-batch 的梯度送到 CPU optimizer；其余 micro-batch 虽在 GPU 累积却未复制给实际更新 owner。§2.2 的另一错误把不等有效 response-token 数的 mini-batch/rank 均值再次平均，使每个 mini-batch/rank 等权，而非按全部有效 token 的 loss sum/count 归一。两者不是同一 bug，也不应以最终分数单指标验收：前者改实际 update，后者改 objective 权重。

[Ch36 Data Parallel](../../../../../books/part-04-training-system/36-distributed-training.md) 约 415–439 已要求固定 micro-batch/DP 身份并检查有效 token/loss normalization；[Ch33](../../../../../books/part-04-training-system/33-grpo.md) 约 730–750 已把 SFT→RL 作为多阶段合理基线，未称 mixed-policy 必胜。本文进一步给出**训练比较有效性**的具体联立反证：候选 mixed-policy 在 verl 路径、对照 SFT 在另一框架的有 bug offload 路径时，同名训练预算不代表同一有效样本梯度或 objective；应先核累计梯度/有效 token 分母/跨框架 loss 与 gradient norm，再比较算法。主 owner 宜 Ch36 的 step/optimizer identity，Ch33 仅训练比较 handoff；是否需新增正文仍待非作者 source→actual owner 裁决，不能因两章已提一般原则便自动 Existing，也不因 framework 名称新便自动 Integrate。

## 必须保留的反证与范围

- §4/Table 2 同一 Qwen2.5-Math-7B 设置下，OpenRLHF 原基线均分 48.3；仅修 token 聚合 49.1，仅修 optimizer 53.4，均修 54.0，与独立 verl 53.8 接近。三 seed、单节点复现支持这两处错误的有限分项作用；不是任何 DeepSpeed/TRL/OpenRLHF 当前版本皆受影响。
- §4/Table 1 的 Qwen 六个 ID 数学任务中，修正 SFT→RL 平均 57.0，高于所列 mixed-policy；但 OOD 平均 59.9 低于 SRFT 62.5，不能写“全部任务/领域都胜”。只有 LUFFY/ReLIFT 由作者完全重实现为单 seed；SRFT/Prefix-RFT/HPT 采用文献报告配置与分数，不是全部方法同一代码、同一随机性与 wall-clock 的对照。
- 文中的 500-step 与 50-step/FLOPs 比较不等于总数据生成、框架实现、调参或服务成本全匹配；Llama-3.1-8B 的跨模型结果也只在披露数学任务、模板和训练预算成立。§6 不授权把 SFT→RL 设为所有混合训练问题的普遍胜者。

作者侧处置：保留为**受限、确有训练比较合同增量的候选线索**；待非作者必要源与 Ch36/33 实际论证核后再决定评分、Books 和正式入选。不得把旧 70 开放工作池直接当候选分母。
