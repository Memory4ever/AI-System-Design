# 第七批有限主题准入（未冻结）

以下20条完整current题摘已实际读。只校准具体增量，不继承Updated归属/旧候选，待逐项exact-v1与first-public身份；含糊只一次core，不自动给分。

## 2602.14134 — DenseMLLM: Standard Multimodal LLMs for Dense Prediction

原始身份：https://arxiv.org/abs/2602.14134v1；Submitted raw：2026-02-15T13:12:28Z，尚非公开时间。

Multimodal Large Language Models (MLLMs) have demonstrated exceptional capabilities in high-level visual understanding. However, extending these models to fine-grained dense prediction tasks, such as semantic segmentation and depth estimation, typically necessitates the incorporation of complex, task-specific decoders and other customizations. This architectural fragmentation increases model complexity and deviates from the generalist design of MLLMs, ultimately limiting their practicality. In this work, we challenge this paradigm by accommodating standard MLLMs to perform dense predictions without requiring additional task-specific decoders. The proposed model is called DenseMLLM, grounded in the standard architecture with a novel vision token supervision strategy for multiple labels and tasks. Despite its minimalist design, our model achieves highly competitive performance across a wide range of dense prediction and vision-language benchmarks, demonstrating that a standard, general-purpose MLLM can effectively support dense perception without architectural specialization. This project is available at github.com/Eli-YiLi/DenseMLLM.

判断：拟入：dense perception另设decoder→标准MLLM vision tokens上多标签监督→可以改变表示输出接口，需核真正dense map与任务head是否隐性恢复，非因指标高。

## 2602.14147 — LaViDa-R1: Advancing Reasoning for Unified Multimodal Diffusion Language Models

原始身份：https://arxiv.org/abs/2602.14147v1；Submitted raw：2026-02-15T13:52:45Z，尚非公开时间。

Diffusion language models (dLLMs) recently emerged as a promising alternative to auto-regressive LLMs. The latest works further extended it to multimodal understanding and generation tasks. In this work, we propose LaViDa-R1, a multimodal, general-purpose reasoning dLLM. Unlike existing works that build reasoning dLLMs through task-specific reinforcement learning, LaViDa-R1 incorporates diverse multimodal understanding and generation tasks in a unified manner. In particular, LaViDa-R1 is built with a novel unified post-training framework that seamlessly integrates supervised finetuning (SFT) and multi-task reinforcement learning (RL). It employs several novel training techniques, including answer-forcing, tree search, and complementary likelihood estimation, to enhance effectiveness and scalability. Extensive experiments demonstrate LaViDa-R1's strong performance on a wide range of multimodal tasks, including visual math reasoning, reason-intensive grounding, and image editing.

判断：一次core：multi-task SFT/RL组合不够；核answer-forcing/tree/complementary likelihood是否改变dLLM likelihood估计/跨任务目标条件。

## 2602.14157 — When Test-Time Guidance Is Enough: Fast Image and Video Editing with Diffusion Guidance

原始身份：https://arxiv.org/abs/2602.14157v1；Submitted raw：2026-02-15T14:13:25Z，尚非公开时间。

Text-driven image and video editing can be naturally cast as inpainting problems, where masked regions are reconstructed to remain consistent with both the observed content and the editing prompt. Recent advances in test-time guidance for diffusion and flow models provide a principled framework for this task; however, existing methods rely on costly vector--Jacobian product (VJP) computations to approximate the intractable guidance term, limiting their practical applicability. Building upon the recent work of Moufad et al. (2025), we provide theoretical insights into their VJP-free approximation and substantially extend their empirical evaluation to large-scale image and video editing benchmarks. Our results demonstrate that test-time guidance alone can achieve performance comparable to, and in some cases surpass, training-based methods.

判断：拟入：editing guidance需昂贵VJP→现有VJP-free近似的新增理论条件与大规模编辑反侧→决定什么时候纯testtime近似替代再训，不能借旧机制冒新机制。

## 2602.14169 — Deep Dense Exploration for LLM Reinforcement Learning via Pivot-Driven Resampling

原始身份：https://arxiv.org/abs/2602.14169v1；Submitted raw：2026-02-15T14:44:15Z，尚非公开时间。

Effective exploration is a key challenge in reinforcement learning for large language models: discovering high-quality trajectories within a limited sampling budget from the vast natural language sequence space. Existing methods face notable limitations: GRPO samples exclusively from the root, saturating high-probability trajectories while leaving deep, error-prone states under-explored. Tree-based methods blindly disperse budgets across trivial or unrecoverable states, causing sampling dilution that fails to uncover rare correct suffixes and destabilizes local baselines. To address this, we propose Deep Dense Exploration (DDE), a strategy that focuses exploration on $\textit{pivots}$-deep, recoverable states within unsuccessful trajectories. We instantiate DDE with DEEP-GRPO, which introduces three key innovations: (1) a lightweight data-driven utility function that automatically balances recoverability and depth bias to identify pivot states; (2) local dense resampling at each pivot to increase the probability of discovering correct subsequent trajectories; and (3) a dual-stream optimization objective that decouples global policy learning from local corrective updates. Experiments on mathematical reasoning benchmarks demonstrate that our method consistently outperforms GRPO, tree-based methods, and other strong baselines. Code is available at https://github.com/AgentCombo/DEEP-GRPO

判断：拟入：root group采样/分散tree budget浪费深部可救状态→recoverability×depth utility选pivot局部密集重采+global/local目标分离→训练探索预算与local baseline人口。

## 2602.14286 — Online LLM watermark detection via e-processes

原始身份：https://arxiv.org/abs/2602.14286v1；Submitted raw：2026-02-15T19:37:06Z，尚非公开时间。

Watermarking for large language models (LLMs) has emerged as an effective tool for distinguishing AI-generated text from human-written content. Statistically, watermark schemes induce dependence between generated tokens and a pseudo-random sequence, reducing watermark detection to a hypothesis testing problem on independence. We develop a unified framework for LLM watermark detection based on e-processes, providing anytime-valid guarantees for online testing. We propose various methods to construct empirically adaptive e-processes that can enhance the detection power. The proposed methods are applicable to any sequential testing problem where independent pivotal statistics are available. In addition, theoretical results are established to characterize the power properties of the proposed procedures. Some experiments demonstrate that the proposed framework achieves competitive performance compared to existing watermark detection methods.

判断：拟入：固定样本watermark test不能任意时刻窥视→e-process anytime-valid在独立pivotal统计量下→在线识别风险界与停止协议。

## 2602.14296 — AutoWebWorld: Synthesizing Infinite Verifiable Web Environments via Finite State Machines

原始身份：https://arxiv.org/abs/2602.14296v1；Submitted raw：2026-02-15T20:03:19Z，尚非公开时间。

The performance of autonomous Web GUI agents heavily relies on the quality and quantity of their training data. However, a fundamental bottleneck persists: collecting interaction trajectories from real-world websites is expensive and difficult to verify. The underlying state transitions are hidden, leading to reliance on inconsistent and costly external verifiers to evaluate step-level correctness. To address this, we propose AutoWebWorld, a novel framework for synthesizing controllable and verifiable web environments by modeling them as Finite State Machines (FSMs) and use coding agents to translate FSMs into interactive websites. Unlike real websites, where state transitions are implicit, AutoWebWorld explicitly defines all states, actions, and transition rules. This enables programmatic verification: action correctness is checked against predefined rules, and task success is confirmed by reaching a goal state in the FSM graph. AutoWebWorld enables a fully automated search-and-verify pipeline, generating over 11,663 verified trajectories from 29 diverse web environments at only $0.04 per trajectory. Training on this synthetic data significantly boosts real-world performance. Our 7B Web GUI agent outperforms all baselines within 15 steps on WebVoyager. Furthermore, we observe a clear scaling law: as the synthetic data volume increases, performance on WebVoyager and Online-Mind2Web consistently improves.

判断：关闭：用显式FSM定义web goal/transition并coding合成网站、graph rule验证是已有synthetic environment/executable verifier配方；规模/单轨成本/跨网站提升未给新的语义真值或验证盲区，题摘不把FSM本身当新长期机制。

## 2602.14338 — Train Less, Learn More: Adaptive Efficient Rollout Optimization for Group-Based Reinforcement Learning

原始身份：https://arxiv.org/abs/2602.14338v1；Submitted raw：2026-02-15T23:14:05Z，尚非公开时间。

Reinforcement learning (RL) plays a central role in large language model (LLM) post-training. Among existing approaches, Group Relative Policy Optimization (GRPO) is widely used, especially for RL with verifiable rewards (RLVR) fine-tuning. In GRPO, each query prompts the LLM to generate a group of rollouts with a fixed group size $N$. When all rollouts in a group share the same outcome, either all correct or all incorrect, the group-normalized advantages become zero, yielding no gradient signal and wasting fine-tuning compute. We introduce Adaptive Efficient Rollout Optimization (AERO), an enhancement of GRPO. AERO uses an adaptive rollout strategy, applies selective rejection to strategically prune rollouts, and maintains a Bayesian posterior to prevent zero-advantage dead zones. Across three model configurations (Qwen2.5-Math-1.5B, Qwen2.5-7B, and Qwen2.5-7B-Instruct), AERO improves compute efficiency without sacrificing performance. Under the same total rollout budget, AERO reduces total training compute by about 48% while shortening wall-clock time per step by about 45% on average. Despite the substantial reduction in compute, AERO matches or improves Pass@8 and Avg@8 over GRPO, demonstrating a practical, scalable, and compute-efficient strategy for RL-based LLM alignment.

判断：拟入：GRPO同结果组zero advantage浪费→adaptive rollout/rejection加Bayesian posterior保持信息→改变dead-zone处理与预算口径，须核posterior引入的目标偏差。

## 2602.14351 — WIMLE: Uncertainty-Aware World Models with IMLE for Sample-Efficient Continuous Control

原始身份：https://arxiv.org/abs/2602.14351v1；Submitted raw：2026-02-15T23:53:16Z，尚非公开时间。

Model-based reinforcement learning promises strong sample efficiency but often underperforms in practice due to compounding model error, unimodal world models that average over multi-modal dynamics, and overconfident predictions that bias learning. We introduce WIMLE, a model-based method that extends Implicit Maximum Likelihood Estimation (IMLE) to the model-based RL framework to learn stochastic, multi-modal world models without iterative sampling and to estimate predictive uncertainty via ensembles and latent sampling. During training, WIMLE weights each synthetic transition by its predicted confidence, preserving useful model rollouts while attenuating bias from uncertain predictions and enabling stable learning. Across $40$ continuous-control tasks spanning DeepMind Control, MyoSuite, and HumanoidBench, WIMLE achieves superior sample efficiency and competitive or better asymptotic performance than strong model-free and model-based baselines. Notably, on the challenging Humanoid-run task, WIMLE improves sample efficiency by over $50$\% relative to the strongest competitor, and on HumanoidBench it solves $8$ of $14$ tasks (versus $4$ for BRO and $5$ for SimbaV2). These results highlight the value of IMLE-based multi-modality and uncertainty-aware weighting for stable model-based RL.

判断：拟入：worldmodel单峰平均多modal且overconfidence偏rollout→IMLE随机多modal免迭代sampling+uncertainty transition weighting→state rollout接纳机制，限定continuouscontrol而非通用foundation安全。

## 2602.14370 — Competition for attention predicts good-to-bad tipping in AI

原始身份：https://arxiv.org/abs/2602.14370v1；Submitted raw：2026-02-16T00:43:56Z，尚非公开时间。

More than half the global population now carries devices that can run ChatGPT-like language models with no Internet connection and minimal safety oversight -- and hence the potential to promote self-harm, financial losses and extremism among other dangers. Existing safety tools either require cloud connectivity or discover failures only after harm has occurred. Here we show that a large class of potentially dangerous tipping originates at the atomistic scale in such edge AI due to competition for the machinery's attention. This yields a mathematical formula for the dynamical tipping point n*, governed by dot-product competition for attention between the conversation's context and competing output basins, that reveals new control levers. Validated against multiple AI models, the mechanism can be instantiated for different definitions of 'good' and 'bad' and hence in principle applies across domains (e.g. health, law, finance, defense), changing legal landscapes (e.g. EU, UK, US and state level), languages, and cultural settings.

判断：一次core：attention dot-product basins→危险tipping n*是否有真实可验证边界，不把泛危险叙述/法规场景当贡献；仅看核心建模与validation。

## 2602.14381 — Adapting VACE for Real-Time Autoregressive Video Diffusion

原始身份：https://arxiv.org/abs/2602.14381v1；Submitted raw：2026-02-16T01:13:33Z，尚非公开时间。

We describe an adaptation of VACE (Video All-in-one Creation and Editing) for real-time autoregressive video generation. VACE provides unified video control (reference guidance, structural conditioning, inpainting, and temporal extension) but assumes bidirectional attention over full sequences, making it incompatible with streaming pipelines that require fixed chunk sizes and causal attention. The key modification moves reference frames from the diffusion latent space into a parallel conditioning pathway, preserving the fixed chunk sizes and KV caching that autoregressive models require. This adaptation reuses existing pretrained VACE weights without additional training. Across 1.3B and 14B model scales, VACE adds 20-30% latency overhead for structural control and inpainting, with negligible VRAM cost relative to the base model. Reference-to-video fidelity is severely degraded compared to batch VACE due to causal attention constraints. A reference implementation is available at https://github.com/daydreamlive/scope.

判断：拟入：VACE reference latent破坏causal固定chunk/cache→把reference移parallel conditioning路径复用权重→新streaming兼容分支及reference fidelity反退，不把免训当无损。

## 2602.14386 — Beyond Token-Level Policy Gradients for Complex Reasoning with Large Language Models

原始身份：https://arxiv.org/abs/2602.14386v1；Submitted raw：2026-02-16T01:28:38Z，尚非公开时间。

Existing policy-gradient methods for auto-regressive language models typically select subsequent tokens one at a time as actions in the policy. While effective for many generation tasks, such an approach may not fully capture the structure of complex reasoning tasks, where a single semantic decision is often realized across multiple tokens--for example, when defining variables or composing equations. This introduces a potential mismatch between token-level optimization and the inherently block-level nature of reasoning in these settings. To bridge this gap, we propose Multi-token Policy Gradient Optimization (MPO), a framework that treats sequences of K consecutive tokens as unified semantic actions. This block-level perspective enables our method to capture the compositional structure of reasoning trajectories and supports optimization over coherent, higher-level objectives. Experiments on mathematical reasoning and coding benchmarks show that MPO outperforms standard token-level policy gradient baselines, highlight the limitations of token-level policy gradients for complex reasoning, motivating future research to look beyond token-level granularity for reasoning-intensive language tasks.

判断：拟入：token PG与semantic多token决策不一致→连续K-token block action policy gradient→改变ratio/credit granularity条件，不能自动说块语义完整。

## 2602.14399 — Multi-Turn Adaptive Prompting Attack on Large Vision-Language Models

原始身份：https://arxiv.org/abs/2602.14399v1；Submitted raw：2026-02-16T02:15:58Z，尚非公开时间。

Multi-turn jailbreak attacks have proven effective against text-only large language models (LLMs), where malicious content is gradually introduced to bypass safety alignment. However, effectively extending such attacks to large vision-language models (LVLMs) remains underexplored. In this paper, we find that naively incorporating visual inputs can make multi-turn jailbreaks easier to defend against; for example, overly malicious visual content will easily trigger the defense mechanism in safety-aligned LVLMs, resulting in more conservative responses. Based on this finding, we propose multi-turn adaptive prompting attack (MAPA) that 1) at each turn, alternates text-vision attack actions to elicit the most malicious response; and 2) across turns, adjusts the attack trajectory through iterative back-and-forth refinement to gradually amplify response maliciousness. This two-level design enables MAPA to consistently outperform state-of-the-art methods, improving attack success rates by 15-30% on recent benchmarks against LLaVA-v1.6-Mistral-7B, Qwen2.5-VL-7B-Instruct, Llama-3.2-Vision-11B-Instruct and GPT-4o-mini. Our code is available at: https://github.com/thomaschoi143/MAPA.

判断：拟入安全反侧：直接恶意visual加入反让防御更强→turn内text/vision选择+turn间反馈轨迹→跨模态/多轮组合边界而非更多jailbreak prompt。

## 2602.14404 — Boule or Baguette? A Study on Task Topology, Length Generalization, and the Benefit of Reasoning Traces

原始身份：https://arxiv.org/abs/2602.14404v1；Submitted raw：2026-02-16T02:20:37Z，尚非公开时间。

Recent years have witnessed meteoric progress in reasoning models: neural networks that generate intermediate reasoning traces (RTs) before producing a final output. Despite the rapid advancement, our understanding of how RTs support reasoning, and the limits of this paradigm, remain incomplete. To promote greater clarity, we introduce PITA: a novel large-scale dataset of over 23 million statements in propositional logic and their corresponding proofs. As a benchmark for robust reasoning, we focus on length generalization: if a model is trained to determine truth or falsity on statements with proofs up to fixed length, how well does it generalize to statements requiring longer proofs? We propose notions of (1) task depth and (2) task breadth, which measure respectively (1) the number of steps required to solve an example from a task and (2) the number of unique examples across a task. We vary these quantities across subsets of PITA, and find that RT models generalize well on broad and shallow subsets, while deteriorating on narrow and deep subsets relative to non-RT baselines. To determine whether our results are idiosyncratic to PITA or indicative of general phenomena, we compare our results to a simple synthetic task based on syllogisms. Our resulting theory suggests fundamental scalings that limit how well RT models perform on deep tasks, and highlights their generalization strengths on broad tasks. Our findings overall identify fundamental benefits and limitations inherent in using reasoning traces.

判断：拟入：CoT普遍帮助lengthgen假设→受控proof task breadth/depth分离且深窄时劣于noRT→需要用task topology限定reasoning trace收益。

## 2602.14432 — S2D: Selective Spectral Decay for Quantization-Friendly Conditioning of Neural Activations

原始身份：https://arxiv.org/abs/2602.14432v1；Submitted raw：2026-02-16T03:41:06Z，尚非公开时间。

Activation outliers in large-scale transformer models pose a fundamental challenge to model quantization, creating excessively large ranges that cause severe accuracy drops during quantization. We empirically observe that outlier severity intensifies with pre-training scale (e.g., progressing from CLIP to the more extensively trained SigLIP and SigLIP2). Through theoretical analysis as well as empirical correlation studies, we establish the direct link between these activation outliers and dominant singular values of the weights. Building on this insight, we propose Selective Spectral Decay ($S^2D$), a geometrically-principled conditioning method that surgically regularizes only the weight components corresponding to the largest singular values during fine-tuning. Through extensive experiments, we demonstrate that $S^2D$ significantly reduces activation outliers and produces well-conditioned representations that are inherently quantization-friendly. Models trained with $S^2D$ achieve up to 7% improved PTQ accuracy on ImageNet under W4A4 quantization and 4% gains when combined with QAT. These improvements also generalize across downstream tasks and vision-language models, enabling the scaling of increasingly large and rigorously trained models without sacrificing deployment efficiency.

判断：拟入：outlier quantization仅activation尺度修补→dominant singular weight方向与outlier联系、选择性谱衰减→训练conditioning/量化接口，理论/视觉基础模型范围待核。

## 2602.14444 — Broken Chains: The Cost of Incomplete Reasoning in LLMs

原始身份：https://arxiv.org/abs/2602.14444v1；Submitted raw：2026-02-16T03:57:51Z，尚非公开时间。

Reasoning-specialized models like OpenAI's 5.1 and DeepSeek-V3.2 allocate substantial inference compute to extended chain-of-thought (CoT) traces, yet reasoning tokens incur significant costs. How do different reasoning modalities of code, natural language, hybrid, or none do perform under token constraints? We introduce a framework that constrains models to reason exclusively through code, comments, both, or neither, then systematically ablates token budgets to 10\%, 30\%, 50\%, and 70\% of optimal. We evaluate four frontier models (GPT-5.1, Gemini 3 Flash, DeepSeek-V3.2, Grok 4.1) across mathematical benchmarks (AIME, GSM8K, HMMT). Our findings reveal: (1) \textbf{truncated reasoning can hurt} as DeepSeek-V3.2 achieves 53\% with no reasoning but only 17\% with truncated CoT at 50\% budget; (2) \textbf{code degrades gracefully} as Gemini's comments collapse to 0\% while code maintains 43-47\%; (3) \textbf{hybrid reasoning underperforms} single modalities; (4) \textbf{robustness is model-dependent} as Grok maintains 80-90\% at 30\% budget where OpenAI and DeepSeek collapse to 7-27\%. These results suggest incomplete reasoning chains actively mislead models, with implications for deploying reasoning-specialized systems under resource constraints.

判断：拟入反侧：少预算CoT被当noCoT与fullCoT中间→按reasoning modality截断可低于noCoT且不同model耐受不同→停止/预算不能仅线性缩短trace，truncation协议待核。

## 2602.14452 — WiSparse: Boosting LLM Inference Efficiency with Weight-Aware Mixed Activation Sparsity

原始身份：https://arxiv.org/abs/2602.14452v1；Submitted raw：2026-02-16T04:18:36Z，尚非公开时间。

Large Language Models (LLMs) offer strong capabilities but incur high inference costs due to dense computation and memory access. Training-free activation sparsity is a promising approach for efficient LLM inference, yet existing methods often rely solely on activation information and uniform sparsity ratios. This overlooks the critical interplay with weights and inter-block sensitivity variation, leading to suboptimal performance. We identify two key phenomena in modern LLMs: 1) less significant activations may align with highly important weights, and 2) sparsity sensitivity varies non-monotonically across model blocks. We propose Weight-aware Mixed-Granularity Training-free Activation Sparsity (WiSparse), which leverages both activation and weight information for adaptive sparsity allocation. Specifically, we introduce a weight-aware mechanism integrating activation magnitudes with precomputed weight norms to accurately identify salient channels. This is combined with a mixed-granularity allocation scheme: a global budget is distributed across blocks via evolutionary search to protect sensitive regions, then refined within blocks to minimize reconstruction error. We improve sparse kernels and demonstrate effectiveness on three representative models. Notably, at 50% sparsity, WiSparse preserves 97% of Llama3.1's dense performance, surpassing the strongest baseline by 2.23 percentage points while achieving a 21.4% acceleration in end-to-end inference speed. Our research advances the limits of training-free approaches for efficient LLM inference, pushing the boundaries of achievable speedup without training.

判断：一次core：weight norm×activation saliency+跨block evolutionary budget是既有Wanda/allocator组合；核nonmonotonic敏感性或kernel机制是否改变实际选择，否则关闭。

## 2602.14468 — LACONIC: Length-Aware Constrained Reinforcement Learning for LLM

原始身份：https://arxiv.org/abs/2602.14468v1；Submitted raw：2026-02-16T05:09:40Z，尚非公开时间。

Reinforcement learning (RL) has enhanced the capabilities of large language models (LLMs) through reward-driven training. Nevertheless, this process can introduce excessively long responses, inflating inference latency and computational overhead. Prior length-control approaches typically rely on fixed heuristic reward shaping, which can misalign with the task objective and require brittle tuning. In this work, we propose LACONIC, a reinforcement learning method that enforces a target token budget during training. Specifically, we update policy models using an augmented objective that combines the task reward with a length-based cost. To balance brevity and task performance, the cost scale is adaptively adjusted throughout training. This yields robust length control while preserving task reward. We provide a theoretical guarantee that support the method. Across mathematical reasoning models and datasets, LACONIC preserves or improves pass@1 while reducing output length by over 50%. It maintains out-of-domain performance on general knowledge and multilingual benchmarks with 44% fewer tokens. Moreover, LACONIC integrates into standard RL-tuning with no inference changes and minimal deployment overhead.

判断：一次core：adaptive length cost/augmented Lagrangian是成熟CMDP原理；核新保证的有限训练接纳条件，而非token少百分比/名称。

## 2602.14506 — Covariance-Aware Transformers for Quadratic Programming and Decision Making

原始身份：https://arxiv.org/abs/2602.14506v1；Submitted raw：2026-02-16T06:39:24Z，尚非公开时间。

We explore the use of transformers for solving quadratic programs and how this capability benefits decision-making problems that involve covariance matrices. We first show that the linear attention mechanism can provably solve unconstrained QPs by tokenizing the matrix variables (e.g.~$A$ of the objective $\frac{1}{2}x^\top Ax+b^\top x$) row-by-row and emulating gradient descent iterations. Furthermore, by incorporating MLPs, a transformer block can solve (i) $\ell_1$-penalized QPs by emulating iterative soft-thresholding and (ii) $\ell_1$-constrained QPs when equipped with an additional feedback loop. Our theory motivates us to introduce Time2Decide: a generic method that enhances a time series foundation model (TSFM) by explicitly feeding the covariance matrix between the variates. We empirically find that Time2Decide uniformly outperforms the base TSFM model for the classical portfolio optimization problem that admits an $\ell_1$-constrained QP formulation. Remarkably, Time2Decide also outperforms the classical "Predict-then-Optimize (PtO)" procedure, where we first forecast the returns and then explicitly solve a constrained QP, in suitable settings. Our results demonstrate that transformers benefit from explicit use of second-order statistics, and this can enable them to effectively solve complex decision-making problems, like portfolio construction, in one forward pass.

判断：拟入理论切片：row-tokenized matrix的linearattention模拟GD、MLP/反馈约束prox→Transformer可计算QP的构造条件；金融TSFM应用不作额外范围入口或一般真实决策保证。

## 2602.14518 — Diagnosing Knowledge Conflict in Multimodal Long-Chain Reasoning

原始身份：https://arxiv.org/abs/2602.14518v1；Submitted raw：2026-02-16T07:10:44Z，尚非公开时间。

Multimodal large language models (MLLMs) in long chain-of-thought reasoning often fail when different knowledge sources provide conflicting signals. We formalize these failures under a unified notion of knowledge conflict, distinguishing input-level objective conflict from process-level effective conflict. Through probing internal representations, we reveal that: (I) Linear Separability: different conflict types are explicitly encoded as linearly separable features rather than entangled; (II) Depth Localization: conflict signals concentrate in mid-to-late layers, indicating a distinct processing stage for conflict encoding; (III) Hierarchical Consistency: aggregating noisy token-level signals along trajectories robustly recovers input-level conflict types; and (IV) Directional Asymmetry: reinforcing the model's implicit source preference under conflict is far easier than enforcing the opposite source. Our findings provide a mechanism-level view of multimodal reasoning under knowledge conflict and enable principled diagnosis and control of long-CoT failures.

判断：拟入：冲突结果不分input/process→内部线性可分/层定位/trajectory pooling与steering方向非对称→诊断与干预不能当对称纠错，真值/causalcontrol待核。

## 2602.14529 — Disentangling Deception and Hallucination Failures in LLMs

原始身份：https://arxiv.org/abs/2602.14529v1；Submitted raw：2026-02-16T07:36:49Z，尚非公开时间。

Failures in large language models (LLMs) are often analyzed from a behavioral perspective, where incorrect outputs in factual question answering are commonly associated with missing knowledge. In this work, focusing on entity-based factual queries, we suggest that such a view may conflate different failure mechanisms, and propose an internal, mechanism-oriented perspective that separates Knowledge Existence from Behavior Expression. Under this formulation, hallucination and deception correspond to two qualitatively different failure modes that may appear similar at the output level but differ in their underlying mechanisms. To study this distinction, we construct a controlled environment for entity-centric factual questions in which knowledge is preserved while behavioral expression is selectively altered, enabling systematic analysis of four behavioral cases. We analyze these failure modes through representation separability, sparse interpretability, and inference-time activation steering.

判断：拟入：错误输出一概缺知识→controlled knowledge preserved但expression被改变四行为人口→知识存在/行为表达的因果分离，不从probe可分推模型有意欺骗。

