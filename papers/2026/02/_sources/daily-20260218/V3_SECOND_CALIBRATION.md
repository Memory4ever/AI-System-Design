# 2026-02-18 第二批增量校准

仅本日raw identity完整题摘线索，未冻结候选。日期字段不直接等于first-public；以下拟项按逐v1 Submitted下界与原始DataCite上界交集继续核，尚未核绑定的项不计确定落窗。

## 2602.13407

Title: On-Policy Supervised Fine-Tuning for Efficient Reasoning

Abstract: Large reasoning models (LRMs) are commonly trained with reinforcement learning (RL) to explore long chain-of-thought reasoning, achieving strong performance at high computational cost. Recent methods add multi-reward objectives to jointly optimize correctness and brevity, but these complex extensions often destabilize training and yield suboptimal trade-offs. We revisit this objective and challenge the necessity of such complexity. Through principled analysis, we identify fundamental misalignments in this paradigm: KL regularization loses its intended role when correctness and length are directly verifiable, and group-wise normalization becomes ambiguous under multiple reward signals. By removing these two items and simplifying the reward to a truncation-based length penalty, we show that the optimization problem reduces to supervised fine-tuning on self-generated data filtered for both correctness and conciseness. We term this simplified training strategy on-policy SFT. Despite its simplicity, on-policy SFT consistently defines the accuracy-efficiency Pareto frontier. It reduces CoT length by up to 80 while maintaining original accuracy, surpassing more complex RL-based methods across five benchmarks. Furthermore, it significantly enhances training efficiency, reducing GPU memory usage by 50% and accelerating convergence by 70%. Our code is available at https://github.com/EIT-NLP/On-Policy-SFT.

可核增量：可验证correctness/length约束下，KL与多信号group normalization存在具体错位，删除后等价到filtered on-policy SFT；若成立，改变长CoT效率训练必须多reward RL的选择。拟5=2+1+2，不采用80%普遍数字。

原字段：{"submitted_v1_utc":"2026-02-13T19:16:39Z","registry_updated_v1_utc":"2026-02-17T01:06:07Z","doi_created_utc":"2026-02-17T03:50:43Z"}

## 2602.13595

Title: The Quantization Trap: Breaking Linear Scaling Laws in Multi-Hop Reasoning

Abstract: Neural scaling laws provide a predictable recipe for AI advancement: reducing numerical precision should linearly improve computational efficiency and energy profile ($E \propto \mathrm{bits}$). In this paper, we demonstrate that this scaling law breaks in the context of multi-hop reasoning. We reveal a 'quantization trap' where reducing precision from 16-bit to 8/4-bit paradoxically increases net energy consumption while degrading reasoning accuracy. We provide a rigorous theoretical decomposition that attributes this failure to hardware casting overhead, the hidden latency cost of dequantization kernels, which becomes a dominant bottleneck in sequential reasoning chains, as well as to a sequential energy amortization failure. As a result, scaling law breaking is unavoidable in practice. We formalize a Critical Model Scale $N^*$ that predicts when the trap dissolves or deepens as a function of model size, batch size, and hardware configuration, validated across a 120$\times$ range (0.6B--72B) on six GPU architectures. Our findings suggest that the industry's "smaller-is-better" heuristic is mathematically counterproductive for complex reasoning tasks.

可核增量：bit数不能直接预测顺序reasoning端到端energy，casting/dequantization占比与batch/hardware/model scale共同决定break-even；拟6=2+2+2。必须控制precision和实现替代解释，不采用unavoidable普遍句。

原字段：{"submitted_v1_utc":"2026-02-14T04:25:27Z","registry_updated_v1_utc":"2026-02-17T01:21:21Z","doi_created_utc":"2026-02-17T03:55:26Z"}

## 2602.14111

Title: Sanity Checks for Sparse Autoencoders: Do SAEs Beat Random Baselines?

Abstract: Sparse Autoencoders (SAEs) have emerged as a promising tool for interpreting neural networks by decomposing their activations into sparse sets of human-interpretable features. Recent work has introduced multiple SAE variants and successfully scaled them to frontier models. Despite much excitement, a growing number of negative results in downstream tasks casts doubt on whether SAEs recover meaningful features. To directly investigate this, we perform two complementary evaluations. On a synthetic setup with known ground-truth features, we demonstrate that SAEs recover only $9\%$ of true features despite achieving $71\%$ explained variance, showing that they fail at their core task even when reconstruction is strong. To evaluate SAEs on real activations, we introduce three baselines that constrain SAE feature directions or their activation patterns to random values. Through extensive experiments across multiple SAE architectures, we show that our baselines match fully-trained SAEs in interpretability (0.87 vs 0.90), sparse probing (0.69 vs 0.72), and causal editing (0.73 vs 0.72). Together, these results suggest that SAEs in their current state do not reliably decompose models' internal mechanisms.

可核增量：reconstruction和可解释性指标可在random feature baseline下仍高；ground-truth与causalediting对照挑战SAE feature recovery解释。拟6=3+1+2，只采实际tested setups，不作所有SAE不可解释普遍论。

原字段：{"submitted_v1_utc":"2026-02-15T11:53:55Z","registry_updated_v1_utc":"2026-02-17T01:54:07Z","doi_created_utc":"2026-02-17T04:07:58Z"}

## 2602.15014

Title: Scaling Beyond Masked Diffusion Language Models

Abstract: Diffusion language models are a promising alternative to autoregressive models due to their potential for faster generation. Among discrete diffusion approaches, Masked diffusion currently dominates, largely driven by strong perplexity on language modeling benchmarks. In this work, we present the first scaling law study of uniform-state and interpolating discrete diffusion methods. We also show that Masked diffusion models can be made approximately 12% more FLOPs-efficient when trained with a simple cross-entropy objective. We find that perplexity is informative within a diffusion family but can be misleading across families, where models with worse likelihood scaling may be preferable due to faster and more practical sampling, as reflected by the speed-quality Pareto frontier. These results challenge the view that Masked diffusion is categorically the future of diffusion language modeling and that perplexity alone suffices for cross-algorithm comparison. Scaling all methods to 1.7B parameters, we show that uniform-state diffusion remains competitive on likelihood-based benchmarks and outperforms autoregressive and Masked diffusion models on GSM8K, despite worse validation perplexity. We provide the code, model checkpoints, and video tutorials on the project page: http://s-sahoo.github.io/scaling-dllms

可核增量：同family perplexity有用而跨离散diffusion family可能逆序speed-quality Pareto；uniform/interpolating状态空间与sampler需要同时评价。拟6=2+2+2，不用模型架构名字代替评价边界。

原字段：{"submitted_v1_utc":"2026-02-16T18:54:47Z","registry_updated_v1_utc":"2026-02-17T02:51:34Z","doi_created_utc":"2026-02-17T04:31:10Z"}

