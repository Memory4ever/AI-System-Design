# 04/27 两项 Ch72 实际写后非作者核

复核者：apr20_resume；书稿写入者：root。只对 `2604.22438v1`、`2604.22550v1` 两处实际正文、前后交接及章末 Review note 作写后核；复用此前已读且未变的 [SSG source→owner 独立核](V3_APR20_SSG_INDEPENDENT.md)与 [ArmSSL source→owner 独立核](V3_APR20_ARMSSL_INDEPENDENT.md)，本轮再对照两篇官方 exact-v1 的决定性方法/反证。未改共享 [Ch72](../../../../../books/part-06-ai-infrastructure/72-security.md) 或 04/27 正式报告；不签来源、first-public、分母或整日 Gate，也未复现实验。

## 2604.22438v1 SSG → Ch72：实际写后 PASS

[官方 §4.1–4.4/§5.1/5.4–5.5](https://arxiv.org/html/2604.22438v1)支持“随机等词数 green/red 不等于分配相同 next-token 概率质量；低熵高概率候选同侧时注入弱”，并支持 Algorithm 1 在 top-k 当前 logits 邻近配对、其余词表随机分边的有限替代。[实际 Ch72 约827–854行](../../../../../books/part-06-ai-infrastructure/72-security.md)在多 bit CDF 消息容量段后新设单 bit 注入侧条件，明确 key、模型/tokenizer/context/候选集合与检测重放共版；下段保留全词表配对排序成本、top-k 不能继承全词表 Eq(7)–(10) 下界、`p1→1` 退化、code/math 质量反向和无原 prompt/改写检测不稳。前后仍接 metadata/签名及 entropy-source provenance 信任根，没有把统计检出当来源或授权真值。章末 Review note 也把理论与实现范围分开。保留旧随机分组和签名回退，不静默取代已有方案。故对**实际新增命题及衔接**通过；不采作者摘要中更宽的任意低熵严格改善或所有任务不损质量宣传。

## 2604.22550v1 ArmSSL → Ch72：实际写后 PASS

[官方 §III–VI](https://arxiv.org/html/2604.22550v1)分别处理 encoder embedding 可见与下游分类 confidence vector 黑盒可见的验证接口；其 clean/trigger 配对、shadow 样本、阈值/统计检验和 OOD 密簇可被反向检测构成受限机制。[实际 Ch72 约2460–2480行](../../../../../books/part-06-ai-infrastructure/72-security.md)位于跨身份 extraction budget/人工调查之后、adaptive student 与训练输出保护之前，只补“encoder→下游适配→可观察 API”身份和“可检出≠不可被对手定位”边界；并明确统计信号不等法律权属、置信/探针不可得时 inconclusive。第二段保留冻结 encoder 主对照不能外推任意 full fine-tune、有限负样本零误报不等总体零误报、适应性移除与效用取舍及访问控制回退。没有把 output-content watermark 与 model-ownership watermark 混同。章末 Review note 同样保留黑盒验证既有先例和有限攻击范围。故对**实际窄机制、反证与前后衔接**通过，不采 Proposition 1 的法律/全威胁 `iff` 保证。

以上两项仅为独立写后 PASS；04/27 报告作者仍须各自完成日期、来源和整日语义 Gate。
