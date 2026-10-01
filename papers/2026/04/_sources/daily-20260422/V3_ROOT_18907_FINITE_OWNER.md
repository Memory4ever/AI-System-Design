# 2604.18907v1 — 有限独立 Books 判定

2026-09-28；复核者 root。本记录仅判断这一 source family 的必要原文、真实 owner 与采用边界，不替代 04/22 日级 Gate。

- Primary source：[arXiv exact-v1 HTML](https://arxiv.org/html/2604.18907v1)，实际核 §3.1–3.4、§4.1–4.5；与当前 `books/part-01-worldview/05-what-neural-networks-learn.md` 的“好的表示 / compositional usefulness”及相邻上下文交接比较。
- 旧方案与约束：单个连续 latent 编码整条程序，在训练内插能拟合，但不同长度或新组合的测试并不自然复用步骤；人工 DSL 能组合，却需要领域语言与离散搜索。
- 可采用的窄增量：在 programming-by-example、固定长度自定义序列任务中，论文通过可复用离散 codebook、共享循环执行器和测试时对 latent 程序的梯度搜索，把“表示是否可组合”具体化为 **primitive 身份、执行规则复用和搜索预算三项联立条件**。输入输出例子归纳程序；部署时改的是 latent 程序，不是 executor 权重。原文 Table 1 的 base / prior-search / gradient-search 对照及 §4.2 消融支持此受限解释。
- 边界：这不是现代 LLM 通用组合泛化结论。论文自建 20 长度序列任务、三 seed；DeepCoder 训练数据重生成 11.6M，不能与有 gold-program 监督的基线混作同一合同。soft program 表示也不等价于可验证的硬符号程序。搜索增加延迟/算力，局部梯度可能陷入次优；人工 DSL 在明确语法、可验证性要求高时仍成立。
- Decision：**有限 Integrate → `WORLDVIEW-REPRESENTATION` / Ch5**。在“compositional usefulness”之后插入一段机制性受限分支，解释可组合表示不仅需要可读 feature，还需要可复用的变换与在新任务中找到组合的办法。不得把模型名称、具体准确率、或程序合成局部结果改写成所有大模型的性质。相邻第6章不承接具体 program-search 算法。
- 尚未验收：书稿实际写后、Daily 同步、候选分母、日期与全日独立复核。
