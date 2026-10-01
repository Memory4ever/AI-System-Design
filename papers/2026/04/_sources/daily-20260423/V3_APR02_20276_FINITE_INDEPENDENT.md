# 2604.20276v1 有界非作者 source→owner 复核

范围：仅核 [官方 exact-v1](https://arxiv.org/html/2604.20276v1) §2、§3.1–3.3、§4.1–4.5、§5.1–5.2、Appendix A/B 中决定采用的定理、实验与例外，对读 `ROADMAP.md` 的 `MODEL-EMBEDDING` owner 及 [Ch12](../../../../../books/part-02-model/12-embedding.md) 的内在维度段（约 89–109 行）。这是单项非作者审阅，不核 04/23 首次公开归属、14 来源、分母或日 Gate；未修改 Books。

## 贡献准入与当前 owner

准入通过，建议 2+2+2=6、深入审阅，而非因“又一种 ID 指标”进入。Ch12 目前已说明 TwoNN/最近邻距离比可受短范数 hub 影响，裁剪后读数不是“真实维度”；但尚未明确区分**估计器的层间曲线**、**pointwise/Hausdorff 所定义的数学维度**与**任务能力/表示容量**。exact-v1 §3.3 在 WikiText 10k prompts、Llama-3.1-8B/Mistral-7B/Pythia-6.9B 的最后 token 上观察 Gride 早层上升；§4.1 中邻居距离比趋近 1 提供一个受测几何解释，不是“真实维度增长”的证据。§4.5 的 von Neumann entropy 相似曲线与 variance spread 只是候选解释，§5.2 尚无确立的理论等价或发布收益。

**可独立核实的窄数学合同。** §3.1 Lemma 1/Theorem 1 对固定确定性、逐层在相关输入测度上 Lipschitz 的映射，给出 pushforward 测度的上下 pointwise dimension 逐层不增；要说单一层级标量不增，还要各层 exact-dimensional。Appendix A 承认标准 dot-product attention 在无界域并非全局 Lipschitz；紧致/有界相关域可限定应用，hard quantization、argmax、top-k 的不连续分支不可套用。§3.3.2 对有限词表、有限 token 序列的离散支持得经典 pointwise/Hausdorff 维度为零；这揭示数学对象对 LLM“容量”的解释力有限，不能写成模型表示无增长、也不能搬到连续视觉输入。

**必须隔离的一处更强定理。** Appendix B Theorem 2 的证明在第 573 行直接用 `f(supp μ)=supp(f#μ)`；一般连续/Lipschitz 映射下右侧应是像的闭包，若原支持集不紧，闭包可增 Hausdorff 维。构造：令 μ 在正整数集每点均赋正质量，故 `supp μ=N` 且 `dim_H=0`；在各整数上令 `f(n)` 依次枚举 `[0,1]` 的有理数，因值域直径 ≤1、任意两整数距离 ≥1，此离散定义是 1-Lipschitz，并可作 1-Lipschitz 延拓。`f#μ` 的原子点集稠密，`supp(f#μ)=[0,1]` 且 `dim_H=1`。因此论文“任意 Lipschitz 层的**支持集** Hausdorff 维单调”按显示条件不成立；若输入支持紧致、像闭合，才可从标准像集不增结论取得该支持集版本。这是对显示证明的数学反例，不是作者确认勘误，也不反驳 §3.1 的测度 pointwise 引理或有限离散 token 的零维特例。

**Books 建议。** `MODEL-EMBEDDING` Ch12 内在维度段之后可提出极窄一段：报告最近邻估计曲线时同时列测度/支持、距离度量、采样与 estimator，不能把受测早层 Gride/TwoNN 上升当真实 pointwise 维度、表示自由度或任务收益；在相关 Lipschitz/测度条件下用 pointwise 不增提供反证，保留有限 token 的零维悖论作为“数学维度不等容量”的界限。不得引用论文未经补充条件的 Hausdorff 支持集定理为通用保证，不写“所有 Transformer 均不增长维度”。这个窄命题比 Ch12 现有 hub 案例增加**定义对象与估计对象的责任边界**，但需 root 复核上述反例/修正并协调共享 Ch12 锁，实际落笔+写后审阅前不得记 Integrate。若不愿在争议定理未澄清前写书稿，可先作为 6 分深入、窄 Disputed 暂缓；本审阅不替作者作最终 Books Decision。
