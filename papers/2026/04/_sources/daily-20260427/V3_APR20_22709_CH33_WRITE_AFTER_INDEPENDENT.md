# 2604.22709v1 → Ch33：非书稿作者实际写后有限核

审阅人：apr20_resume；书稿写入人：root。本核只对照[官方 exact-v1](https://arxiv.org/html/2604.22709v1) §3.1–3.3、§4.1–4.2/Table 1、[作者窄提案](V3_PENDING_TWO_BOOKS_LITERAL.md)及 [Ch33](../../../../../books/part-04-training-system/33-grpo.md) 新正文约 704–710 行和两侧的自然语言 reward-prior→Pure RL/multi-stage 交接。不复核 04/27 日期、全部候选或 Books 其它段。

## 结论：一处表述需修正，其余窄机制与交接通过

新段准确区分了在自然语言 trace 上调长度惩罚与改变为保留离散码的中间动作空间；官方 §3.2 的带 verbal CoT bottleneck SFT、prompt-only 自蒸馏 warm-up，及 §3.3 对抽象码和答案联合做受约束 GRPO，均已在正文出现。Table 1 的 Qwen3-8B MATH-500 90.8/144 对 verbal SFT+RL 92.6/1671 支持“更短但该切片准确率仍低”；主表的 Qwen3 4B/8B、Granite 3B 是正文所称受限实验（附录另有 32B，不将主表措辞读作作者仅测三模型）。冷启动 RL-only 弱于 warm-up、有更多训练准备成本、不可把短输出自动换算总 compute/时延/faithfulness，均保留。位置承接前一段 prior 成本，再转入 Pure RL 与多阶段路线，不静默替代旧方案。

**唯一需改的词组：**新正文称“码表、最大长度、约束解码器与 reference policy 都进入训练和推理身份”。官方 §3.3 Eq(5) 的 `π_ref` 是 warm-started model，用于 GRPO 训练时对抽象码与答案分布的 KL；§3.1/§3.2 的推理只需 prompt、已训练 policy、保留词表/起止标记、长度与约束解码，不需要再执行 `π_ref`。当前并列句可能误导读者把训练 reference policy 当作推理侧依赖。建议改成“码表、最大长度与约束解码器进入训练和推理身份，reference policy 则进入训练身份”；仅修此词组，保留其它两段。修后可判实际写后 PASS；修前不记无保留 PASS。

未改共享 Books、04/27 正式日报或 checkpoint。本项不是 04/27 日级 Gate；04/20 本职闭环仍单独进行。

## 定点修正后复核

root 将该句实际改为“码表、最大长度与约束解码器进入训练和推理身份，reference policy 则作为训练时 KL 约束的版本化状态”。我只重读 Ch33 新段该句与紧邻上下文；现在准确对应官方 §3.3 Eq(5) 后对 `π_ref` 的训练定义，不再暗示部署推理必须执行 reference policy。上述唯一需修处已消除；本项**实际写后 PASS**，仍非 04/27 日级 Gate。
