# 03/20 后批11项 exact-v1完整题摘原文

本日有限恢复保存，2026-10-02T03:36:54+08:00。以下只供准入抽核；均D4–14日期隔离，非确定本窗候选、非Evidence或性能保证。来源为官方export.arxiv.org exact-version Atom查询，id_list为下列11个v1、max_results=11；实际11返回。`published`是接口提交字段，不当首次公开时间。摘要原文保存，不采摘要数字。

## 2603.18373v1

Title: To See or To Please: Uncovering Visual Sycophancy and Split Beliefs in VLMs

Primary: https://arxiv.org/abs/2603.18373v1

API published: 2026-03-19T00:15:05Z

Abstract (complete verbatim):

When VLMs answer correctly, do they genuinely rely on visual information or exploit language shortcuts? We introduce the Tri-Layer Diagnostic Framework, which disentangles hallucination sources via three metrics: Latent Anomaly Detection (perceptual awareness), Visual Necessity Score (visual dependency, measured via KL divergence), and Competition Score (conflict between visual grounding and instruction following). Using counterfactual interventions (blind, noise, and conflict images) across 7 VLMs and 7,000 model-sample pairs, our taxonomy reveals that 69.6% of samples exhibit Visual Sycophancy--models detect visual anomalies but hallucinate to satisfy user expectations--while zero samples show Robust Refusal, indicating alignment training has systematically suppressed truthful uncertainty acknowledgment. A scaling analysis (Qwen2.5-VL 7B to 72B) shows larger models reduce Language Shortcuts but amplify Visual Sycophancy, demonstrating scale alone cannot resolve the grounding problem. Diagnostic scores further enable a post-hoc selective prediction strategy achieving up to +9.5pp accuracy at 50% coverage with no additional training cost.

## 2603.18815v1

Title: ProRL Agent: Rollout-as-a-Service for RL Training of Multi-Turn LLM Agents

Primary: https://arxiv.org/abs/2603.18815v1

API published: 2026-03-19T12:08:51Z

Abstract (complete verbatim):

Multi-turn LLM agents are increasingly important for solving complex, interactive tasks, and reinforcement learning (RL) is a key ingredient for improving their long-horizon behavior. However, RL training requires generating large numbers of sandboxed rollout trajectories, and existing infrastructures often couple rollout orchestration with the training loop, making systems hard to migrate and maintain. Under the rollout-as-a-service philosophy, we present ProRL Agent , a scalable infrastructure that serves the full agentic rollout lifecycle through an API service. ProRL Agent also provides standardized and extensible sandbox environments that support diverse agentic tasks in rootless HPC settings. We validate ProRL Agent through RL training on software engineering, math, STEM, and coding tasks. ProRL Agent is open-sourced and integrated as part of NVIDIA NeMo Gym.

## 2603.18567v1

Title: SpecForge: A Flexible and Efficient Open-Source Training Framework for Speculative Decoding

Primary: https://arxiv.org/abs/2603.18567v1

API published: 2026-03-19T07:28:56Z

Abstract (complete verbatim):

Large language models incur high inference latency due to sequential autoregressive decoding. Speculative decoding alleviates this bottleneck by using a lightweight draft model to propose multiple tokens for batched verification. However, its adoption has been limited by the lack of high-quality draft models and scalable training infrastructure. We introduce SpecForge, an open-source, production-oriented framework for training speculative decoding models with full support for EAGLE-3. SpecForge incorporates target-draft decoupling, hybrid parallelism, optimized training kernels, and integration with production-grade inference engines, enabling up to 9.9x faster EAGLE-3 training for Qwen3-235B-A22B. In addition, we release SpecBundle, a suite of production-grade EAGLE-3 draft models trained with SpecForge for mainstream open-source LLMs. Through a systematic study of speculative decoding training recipes, SpecBundle addresses the scarcity of high-quality drafts in the community, and our draft models achieve up to 4.48x end-to-end inference speedup on SGLang, establishing SpecForge as a practical foundation for real-world speculative decoding deployment.

## 2603.18636v1

Title: Training-Free Sparse Attention for Fast Video Generation via Offline Layer-Wise Sparsity Profiling and Online Bidirectional Co-Clustering

Primary: https://arxiv.org/abs/2603.18636v1

API published: 2026-03-19T09:00:08Z

Abstract (complete verbatim):

Diffusion Transformers (DiTs) achieve strong video generation quality but suffer from high inference cost due to dense 3D attention, leading to the development of sparse attention technologies to improve efficiency. However, existing training-free sparse attention methods in video generation still face two unresolved limitations: ignoring layer heterogeneity in attention pruning and ignoring query-key coupling in block partitioning, which hinder a better quality-speedup trade-off. In this work, we uncover a critical insight that the attention sparsity of each layer is its intrinsic property, with minor effects across different inputs. Motivated by this, we propose SVOO, a training-free Sparse attention framework for fast Video generation via Offline layer-wise sparsity profiling and Online bidirectional co-clustering. Specifically, SVOO adopts a two-stage paradigm: (i) offline layer-wise sensitivity profiling to derive intrinsic per-layer pruning levels, and (ii) online block-wise sparse attention via a novel bidirectional co-clustering algorithm. Extensive experiments on seven widely used video generation models demonstrate that SVOO achieves a superior quality-speedup trade-off over state-of-the-art methods, delivering up to $1.93\times$ speedup while maintaining a PSNR of up to 29 dB on Wan2.1.

## 2603.19335v1

Title: Do Post-Training Algorithms Actually Differ? A Controlled Study Across Model Scales Uncovers Scale-Dependent Ranking Inversions

Primary: https://arxiv.org/abs/2603.19335v1

API published: 2026-03-19T04:10:38Z

Abstract (complete verbatim):

Post-training alignment has produced dozens of competing algorithms -- DPO, SimPO, KTO, GRPO, and others -- yet practitioners lack controlled comparisons to guide algorithm selection. We present OXRL, a unified framework implementing 51 post-training algorithms with identical infrastructure, enabling the first large-scale apples-to-apples evaluation. Our study spans 8 algorithms across 4 model scales (0.5B--7B), 3 evaluation domains, and a 20-variant DPO taxonomy (100 runs at 1.5B, 5 seeds each), totaling $\sim$240 training runs on H100 GPUs. Three headline findings emerge. (1)~Algorithm rankings are unstable across scale: at 1.5B, online RL (SGRPO) tops all methods at 58.0\%~$\pm$0.57 on GSM8K; by 7B, the worst small-scale method (SimPO) becomes the best (85.8\%), a complete ranking inversion driven by model scale rather than LoRA regularization (confirmed via 2$\times$2 factorial). (2)~Loss function modifications yield negligible gains: none of 20 DPO variants significantly outperform vanilla DPO after Bonferroni correction; the sole significant outlier, SimPO, is worse ($-$11.5~pp, $p < 10^{-4}$). (3)~Algorithm leverage is task-specific: the 19.3~pp GSM8K spread collapses to 0.54~pp on MATH ($36\times$) and 0.47~pp on general-domain benchmarks ($41\times$), confirming that algorithm choice matters primarily within the training distribution. These findings yield a hierarchy of leverage for practitioners: model scale (${\sim}$50~pp) $\gg$ training paradigm (${\sim}$10~pp) $\gg$ online vs.\ offline (${\sim}$9~pp) $\gg$ loss function (${\sim}$1~pp). We release all code, configs, and evaluation data as a living community benchmark.

## 2603.19233v1

Title: Not All Features Are Created Equal: A Mechanistic Study of Vision-Language-Action Models

Primary: https://arxiv.org/abs/2603.19233v1

API published: 2026-03-19T17:59:55Z

Abstract (complete verbatim):

Vision-Language-Action (VLA) models combine perception, language, and motor control in a single architecture, yet how they translate multimodal inputs into actions remains poorly understood. We apply activation injection, sparse autoencoders (SAEs), and linear probes to six models spanning 80M--7B parameters across 394,000+ rollout episodes on four benchmarks. The visual pathway dominates action generation across all architectures: injecting baseline activations into null-prompt episodes recovers near-identical behavior, while cross-task injection steers robots toward source-task positions (99.8\% of X-VLA episodes align with the source trajectory), exposing spatially bound motor programs tied to scene coordinates rather than abstract task representations. Language sensitivity depends on task structure, not model design: when visual context uniquely specifies the task, language is ignored; when multiple goals share a scene, language becomes essential (X-VLA \texttt{libero\_goal}: 94\%$\to$10\% under wrong prompts vs.\ \texttt{libero\_object}: 60--100\% regardless). In all three multi-pathway architectures (\pizhalf{}, SmolVLA, GR00T), expert pathways encode motor programs while VLM pathways encode goal semantics ($2\times$ greater behavioral displacement from expert injection), and subspace injection confirms these occupy separable activation subspaces. Per-token SAE processing is essential for action fidelity on most architectures, though mean-pooling improves fidelity on X-VLA. Contrastive identification recovers 82+ manipulation concepts, and causal ablation reveals sensitivity spanning 28--92\% zero-effect rates independent of representation width. We release \textbf{Action Atlas} (https://action-atlas.com) for interactive exploration of VLA representations across all six models.

## 2603.19131v1

Title: From Inference Efficiency to Embodied Efficiency: Revisiting Efficiency Metrics for Vision-Language-Action Models

Primary: https://arxiv.org/abs/2603.19131v1

API published: 2026-03-19T16:49:28Z

Abstract (complete verbatim):

Vision-Language-Action (VLA) models have recently enabled embodied agents to perform increasingly complex tasks by jointly reasoning over visual, linguistic, and motor modalities. However, we find that the prevailing notion of ``efficiency'' in current VLA research, characterized by parameters, FLOPs, or token decoding throughput, does not reflect actual performance on robotic platforms. In real-world execution, efficiency is determined by system-level embodied behaviors such as task completion time, trajectory smoothness, cumulative joint rotation, and motion energy. Through controlled studies across model compression, token sparsification, and action sequence compression, we make several observations that challenge common assumptions. (1) Methods that reduce computation under conventional metrics often increase end-to-end execution cost or degrade motion quality, despite maintaining task success rates. (2) System-level embodied efficiency metrics reveal performance differences in the learned action policies that remain hidden under conventional evaluations. (3) Common adaptation methods such as in-context prompting or supervised fine-tuning show only mild and metric-specific improvements in embodied efficiency. While these methods can reduce targeted embodied-efficiency metrics such as jerk or action rate, the resulting gains may come with trade-offs in other metrics, such as longer completion time. Taken together, our results suggest that conventional inference efficiency metrics can overlook important aspects of embodied execution. Incorporating embodied efficiency provides a more complete view of policy behavior and practical performance, enabling fairer and more comprehensive comparisons of VLA models.

## 2603.18742v1

Title: 6Bit-Diffusion: Inference-Time Mixed-Precision Quantization for Video Diffusion Models

Primary: https://arxiv.org/abs/2603.18742v1

API published: 2026-03-19T10:45:11Z

Abstract (complete verbatim):

Diffusion transformers have demonstrated remarkable capabilities in generating videos. However, their practical deployment is severely constrained by high memory usage and computational cost. Post-Training Quantization provides a practical way to reduce memory usage and boost computation speed. Existing quantization methods typically apply a static bit-width allocation, overlooking the quantization difficulty of activations across diffusion timesteps, leading to a suboptimal trade-off between efficiency and quality. In this paper, we propose a inference time NVFP4/INT8 Mixed-Precision Quantization framework. We find a strong linear correlation between a block's input-output difference and the quantization sensitivity of its internal linear layers. Based on this insight, we design a lightweight predictor that dynamically allocates NVFP4 to temporally stable layers to maximize memory compression, while selectively preserving INT8 for volatile layers to ensure robustness. This adaptive precision strategy enables aggressive quantization without compromising generation quality. Beside this, we observe that the residual between the input and output of a Transformer block exhibits high temporal consistency across timesteps. Leveraging this temporal redundancy, we introduce Temporal Delta Cache (TDC) to skip computations for these invariant blocks, further reducing the computational cost. Extensive experiments demonstrate that our method achieves 1.92$\times$ end-to-end acceleration and 3.32$\times$ memory reduction, setting a new baseline for efficient inference in Video DiTs.

## 2603.19220v1

Title: Nemotron-Cascade 2: Post-Training LLMs with Cascade RL and Multi-Domain On-Policy Distillation

Primary: https://arxiv.org/abs/2603.19220v1

API published: 2026-03-19T17:58:52Z

Abstract (complete verbatim):

We introduce Nemotron-Cascade 2, an open 30B MoE model with 3B activated parameters that delivers best-in-class reasoning and strong agentic capabilities. Despite its compact size, its mathematical and coding reasoning performance approaches that of frontier open models. It is the second open-weight LLM, after DeepSeekV3.2-Speciale-671B-A37B, to achieve Gold Medal-level performance in the 2025 International Mathematical Olympiad (IMO), the International Olympiad in Informatics (IOI), and the ICPC World Finals, demonstrating remarkably high intelligence density with 20x fewer parameters. In contrast to Nemotron-Cascade 1, the key technical advancements are as follows. After SFT on a meticulously curated dataset, we substantially expand Cascade RL to cover a much broader spectrum of reasoning and agentic domains. Furthermore, we introduce multi-domain on-policy distillation from the strongest intermediate teacher models for each domain throughout the Cascade RL process, allowing us to efficiently recover benchmark regressions and sustain strong performance gains along the way. We release the collection of model checkpoint and training data.

## 2603.18718v1

Title: MemMA: Coordinating the Memory Cycle through Multi-Agent Reasoning and In-Situ Self-Evolution

Primary: https://arxiv.org/abs/2603.18718v1

API published: 2026-03-19T10:15:59Z

Abstract (complete verbatim):

Memory-augmented LLM agents maintain external memory banks to support long-horizon interaction, yet most existing systems treat construction, retrieval, and utilization as isolated subroutines. This creates two coupled challenges: strategic blindness on the forward path of the memory cycle, where construction and retrieval are driven by local heuristics rather than explicit strategic reasoning, and sparse, delayed supervision on the backward path, where downstream failures rarely translate into direct repairs of the memory bank. To address these challenges, we propose MemMA, a plug-and-play multi-agent framework that coordinates the memory cycle along both the forward and backward paths. On the forward path, a Meta-Thinker produces structured guidance that steers a Memory Manager during construction and directs a Query Reasoner during iterative retrieval. On the backward path, MemMA introduces in-situ self-evolving memory construction, which synthesizes probe QA pairs, verifies the current memory, and converts failures into repair actions before the memory is finalized. Extensive experiments on LoCoMo show that MemMA consistently outperforms existing baselines across multiple LLM backbones and improves three different storage backends in a plug-and-play manner. Our code is publicly available at https://github.com/ventr1c/memma.

## 2603.19092v1

Title: SAVeS: Steering Safety Judgments in Vision-Language Models via Semantic Cues

Primary: https://arxiv.org/abs/2603.19092v1

API published: 2026-03-19T16:18:00Z

Abstract (complete verbatim):

Vision-language models (VLMs) are increasingly deployed in real-world and embodied settings where safety decisions depend on visual context. However, it remains unclear which visual evidence drives these judgments. We study whether multimodal safety behavior in VLMs can be steered by simple semantic cues. We introduce a semantic steering framework that applies controlled textual, visual, and cognitive interventions without changing the underlying scene content. To evaluate these effects, we propose SAVeS, a benchmark for situational safety under semantic cues, together with an evaluation protocol that separates behavioral refusal, grounded safety reasoning, and false refusals. Experiments across multiple VLMs and an additional state-of-the-art benchmark show that safety decisions are highly sensitive to semantic cues, indicating reliance on learned visual-linguistic associations rather than grounded visual understanding. We further demonstrate that automated steering pipelines can exploit these mechanisms, highlighting a potential vulnerability in multimodal safety systems.
