# 第七批完整精确题摘与准入校准

仅本日已有主题发现的具体线索，不自动全文队列。当前版本有变化者已恢复精确v1摘要，以下尚待root准入校准与各自日期边界核验。

## 2602.15396v1 — Efficient Generative Modeling beyond Memoryless Diffusion via Adjoint Schrödinger Bridge Matching

[精确v1](https://arxiv.org/html/2602.15396v1)

Diffusion models often yield highly curved trajectories and noisy score targets due to an uninformative, memoryless forward process that induces independent data-noise coupling. We propose Adjoint Schrödinger Bridge Matching (ASBM) , a generative modeling framework that recovers optimal trajectories in high dimensions via two stages. First, we view the Schrödinger Bridge (SB) forward dynamic as a coupling construction problem and learn it through a data-to-energy sampling perspective that transports data to an energy-defined prior. Then, we learn the backward generative dynamic with a simple matching loss supervised by the induced optimal coupling. By operating in a non-memoryless regime, ASBM produces significantly straighter and more efficient sampling paths. Compared to prior works, ASBM scales to high-dimensional data with notably improved stability and efficiency. Extensive experiments on image generation show that ASBM improves fidelity with fewer sampling steps. We further showcase the effectiveness of our optimal trajectory via distillation to a one-step generator.

准入理由：独立data-noise coupling使memoryless路径弯曲→先学习data-to-energy SB forward coupling再matching backward→生成路径质量/步数与forward过程选择需重新比较，不借optimal名授全局保证。

## 2602.15438v1 — Logit Distance Bounds Representational Similarity

[精确v1](https://arxiv.org/html/2602.15438v1)

For a broad family of discriminative models that includes autoregressive language models, identifiability results imply that if two models induce the same conditional distributions, then their internal representations agree up to an invertible linear transformation. We ask whether an analogous conclusion holds approximately when the distributions are close instead of equal. Building on the observation of Nielsen et al. (2025) that closeness in KL divergence need not imply high linear representational similarity, we study a distributional distance based on logit differences and show that closeness in this distance does yield linear similarity guarantees. Specifically, we define a representational dissimilarity measure based on the models’ identifiability class and prove that it is bounded by the logit distance. We further show that, when model probabilities are bounded away from zero, KL divergence upper-bounds logit distance; yet the resulting bound fails to provide nontrivial control in practice. As a consequence, KL-based distillation can match a teacher’s predictions while failing to preserve linear representational properties, such as linear-probe recoverability of human-interpretable concepts. In distillation experiments on synthetic and image datasets, logit-distance distillation yields students with higher linear representational similarity and better preservation of the teacher’s linearly recoverable concepts.

准入理由：teacher/student output KL接近不必保留线性可读concept→identifiability类下logit-distance控制表示差与positive-prob条件→distillation fidelity须区分预测与representation保持。

## 2602.15460v1 — On the Out-of-Distribution Generalization of Reasoning in Multimodal LLMs for Simple Visual Planning Tasks

[精确v1](https://arxiv.org/html/2602.15460v1)

Integrating reasoning in large language models and large vision-language models has recently led to significant improvement of their capabilities. However, the generalization of reasoning models is still vaguely defined and poorly understood. In this work, we present an evaluation framework to rigorously examine how well chain-of-thought (CoT) approaches generalize on a simple planning task. Specifically, we consider a grid-based navigation task in which a model is provided with a map and must output a sequence of moves that guides a player from a start position to a goal while avoiding obstacles. The versatility of the task and its data allows us to fine-tune model variants using different input representations (visual and textual) and CoT reasoning strategies, and systematically evaluate them under both in-distribution (ID) and out-of-distribution (OOD) test conditions. Our experiments show that, while CoT reasoning improves in-distribution generalization across all representations, out-of-distribution generalization (e.g., to larger maps) remains very limited in most cases when controlling for trivial matches with the ID data. Surprisingly, we find that reasoning traces which combine multiple text formats yield the best (and non-trivial) OOD generalization. Finally, purely text-based models consistently outperform those utilizing image-based inputs, including a recently proposed approach relying on latent space reasoning.

准入理由：CoT/visual reasoning在ID改善被误当结构外推→固定grid planning表示/trace策略并控制trivial overlap的OOD反侧→text/image与混合trace的外推边界需独立验收。

## 2602.15481v1 — LLM-as-Judge on a Budget

[精确v1](https://arxiv.org/html/2602.15481v1)

LLM-as-a-judge has emerged as a cornerstone technique for evaluating large language models by leveraging LLM reasoning to score prompt-response pairs. Since LLM judgments are stochastic, practitioners commonly query each pair multiple times to estimate mean scores accurately. This raises a critical challenge: given a fixed computational budget B, how to optimally allocate queries across K prompt-response pairs to minimize estimation error? We present a principled variance-adaptive approach leveraging multi-armed bandit theory and concentration inequalities. Our method dynamically allocates queries based on estimated score variances, concentrating resources where uncertainty is highest. Further, our algorithm is shown to achieve a worst-case score-estimation error of \tilde{O}\left(\sqrt{\frac{\sum_{i=1}^{K}\sigma_{i}^{2}}{B}}\right), \sigma_{i}^{2} being the unknown score variance for pair i\in[K] with near-optimal budget allocation. Experiments on Summarize-From-Feedback and HelpSteer2 demonstrate our method significantly outperforms uniform allocation, reducing worst-case estimation error while maintaining identical budgets. Our work establishes a theoretical foundation for efficient LLM evaluation with practical implications for AI safety, model alignment, and automated assessment at scale.

准入理由：同预算每pair均匀重复judge忽略variance→bandit variance-adaptive allocation及worst-case error界→query预算在估计均值precision而非human truth之间分账。

## 2602.15503v1 — Approximation Theory for Lipschitz Continuous Transformers

[精确v1](https://arxiv.org/html/2602.15503v1)

Stability and robustness are critical for deploying Transformers in safety-sensitive settings. A principled way to enforce such behavior is to constrain the model’s Lipschitz constant. However, approximation-theoretic guarantees for architectures that explicitly preserve Lipschitz continuity have yet to be established. In this work, we bridge this gap by introducing a class of gradient-descent-type in-context Transformers that are Lipschitz-continuous by construction. We realize both MLP and attention blocks as explicit Euler steps of negative gradient flows, ensuring inherent stability without sacrificing expressivity. We prove a universal approximation theorem for this class within a Lipschitz-constrained function space. Crucially, our analysis adopts a measure-theoretic formalism, interpreting Transformers as operators on probability measures, to yield approximation guarantees independent of token count. These results provide a rigorous theoretical foundation for the design of robust, Lipschitz continuous Transformer architectures.

准入理由：限制Lipschitz可能被视为必牺牲表达→attention/MLP negative-gradient-flow Euler构造及概率测度上的受限universalapprox→稳定性/表达保证须回到特定架构与函数类，不授生产安全。
