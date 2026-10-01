# 04/24 三项 Books 实际写后非作者复核（2026-09-28）

复核者 root。只核三项 exact-v1 已在前置独立 source→owner 审阅通过的候选，其当前实际正文、相邻段与证据边界；不代替 04/24 整日 Gate，未复现实验。三个目标文件 scoped `git diff --check` 均通过。

| 来源及 owner | 写后裁决 | 相邻衔接、实际机制与边界 |
| --- | --- | --- |
| [`2604.21160v1`](https://arxiv.org/html/2604.21160v1)，`TRAIN-GRPO` Ch33 约 195–197 行 | PASS | outcome broadcast 后自然进入字段化 credit 的条件分支：解析 JSON 字符区间→映射 token span→字段组内 advantage，并与背景/全组分母分开。字段 oracle、malformed/重叠/零方差均有工程回退，不把预测 2D–3D 一致性冒充外部几何真值；GRCA-only IoU3D 略低于广播的反例在正文。 |
| [`2604.21511v1`](https://arxiv.org/html/2604.21511v1)，`AGENT-RAG` Ch76 约 966–968 行 | PASS | 单向量及 lexical/SPLADE 路线后接 learned sparse latent 词表与倒排 posting，再转向多向量物理搬运，逻辑顺接。冻结编码器字典预训→联合检索适配分责清楚；token Top-K 不保证 pooled document sparsity，解释性命名不是真值。版本化重建标为工程推论，受限对照和真实延迟未证均在。 |
| [`2604.21221v1`](https://arxiv.org/html/2604.21221v1)，`MULTIMODAL-GENERATIVE-PARADIGMS` Ch24 约 284–286 行 | PASS | Salt 的有误差历史训练后，按历史写入质量→实际读取集合切入内生 sparse persistent/local KV；coarse pool 只有提名权，训练 mask 与推理读取合同一致。移除 persistent 的速度—质量反向、有限时长与 kernel/serving handoff 可见；不宣称无限长稳定或完整 SLO，dense/full-history 旧路保留。 |

此 PASS 仅允许三项对应 Books 实际写后状态进入 04/24 Daily；该日尚需完成所有候选、日期和分母复核，不能据此宣称整日闭环。
