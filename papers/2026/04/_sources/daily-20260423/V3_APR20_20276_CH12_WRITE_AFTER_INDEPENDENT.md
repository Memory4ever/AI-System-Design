# 04/23 2604.20276v1 → Ch12 实际写后有限复核

复核者 `apr20_resume`，非该次 Ch12 正文作者。只核这一条已写入的机制边界和相邻交接，不核 04/23 的来源、日期、候选分母或整日 Gate；不修改共享 Books。

我实际重新打开[官方 exact-v1](https://arxiv.org/html/2604.20276v1) §2–3.3、§4–5 和 Appendix A/B 的必要位置，并复用[apr02 已完成的 source→Ch12 有界核](./V3_APR02_20276_FINITE_INDEPENDENT.md)。§3.1 Lemma 1/Theorem 1 针对相关输入测度上 Lipschitz 的固定映射，给的是上下 pointwise dimension 的逐点约束；整层单一数值还需 exact-dimensional 条件。§3.3 的 WikiText/受测模型 Gride 层曲线是有限样本估计读数，不是任务容量证明；有限 token 序列支持零维的数学特例也不能倒推语言能力为零。Appendix B Theorem 2 第573行将 `f(supp μ)` 直接等同于 `supp(f#μ)`，非紧支持时缺闭包条件；apr02 的稠密原子反例只隔离该印刷支持集 Hausdorff 普遍保证，不推翻 pointwise 引理或紧致情形。

实际顺读 [Ch12](../../../../../books/part-02-model/12-embedding.md) 新段约105行与前后：前段讲初始 embedding 的邻居距离、短范数 hub 与裁剪读数，新增段进一步分离“有限样本估计器读数／测度或支持集的数学维度／下游任务可用能力”，明确只在相应 Lipschitz 条件下谈测度 pointwise 约束，没有写任意支持集 Hausdorff 单调定理，也没有从层曲线推断表示自由度或裁剪/发布收益。后段转到初始表示不等上下文表示；与 Ch11 的 token 身份和 Ch13 的位置信息交接一致，未把位置编码或 Attention 全部视为满足前述条件。章末 Review note 亦明确隔离 Appendix B 印刷强保证及“LLM 几何观测→通用发布收益”外推。

**结论：真实写后 PASS。** 只认可 Ch12 这一最窄的诊断对象分账与条件化数学边界；不认可论文 Appendix B 的无条件支持集结论、不把 Gride 曲线变成任务能力、不签 04/23 整日 Gate。root 可将共享 Review note 的“写后独立核待完成”改为本具名 PASS。
