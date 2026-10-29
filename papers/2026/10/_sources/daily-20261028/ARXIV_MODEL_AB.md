# 模型与推理题摘：原始读取，尚未完成准入

仅存本日导航定点恢复的完整题摘与版本原字段；列表出现日不自动等于首公开日。以下原始字段不代表审阅完成或Books采用。读取时间2026-10-28。

## 2610.35556

[2610.35556] LoopFold: Parallelizing Recurrent Depth in Looped Transformers

[原件](https://arxiv.org/abs/2610.35556)

Abstract: Looped Transformers increase computation per token by repeatedly applying a shared backbone, offering a way to improve language modeling and downstream task performance at a fixed backbone parameter count. However, each loop depends on the preceding loop, so increasing recurrent depth also increases decoding latency. Existing approaches include Parallel Loop Transformers, which reduce latency by overlapping loop computation across token positions, but yield rapidly diminishing marginal accuracy gains at larger depths. To address this challenge, we introduce LoopFold, which folds computation at multiple recurrent depths into parallel batches for the same token prefix. A lightweight predictor estimates inputs to later loops so they can start before earlier loops finish. A corrector then refines the outputs of these later loops using newly available results from earlier loops. All components are trained jointly using only the final next-token prediction loss. In experiments with 1.4B models, deeper LoopFold configurations achieve progressively higher average zero-shot accuracy across eight tasks, rising from 53.41% to 56.38%. Vanilla looped models and PLT show limited gains over the same depth range. Compared with a nine-loop vanilla model, LoopFold uses five sequential stages and additional parallel computation to reduce decoding latency by 46%.

Submission history From: Feichen Song [ view email ] [v1] Mon, 26 Oct 2026 14:58:11 UTC (1,239 KB) Full-text links: Access Paper: View a PDF of the paper titled LoopFold: Parallelizing Recurrent Depth in Looped Transformers, by Feichen Song and 9 other authors View PDF HTML (experimental) TeX Source view license Additional Features Audio Summary Current browse context: cs.CL <a class="abs-button prev-url" href="/prevnext?id=2610.35556&function=prev&context=cs.CL" accesskey="p" title="previ

## 2610.35544

[2610.35544] StateLoop: Persistent State for Looped Transformers

[原件](https://arxiv.org/abs/2610.35544)

Abstract: Looped Transformers offer a parameter-efficient approach to language modeling by repeatedly applying a shared backbone. Vanilla looped Transformers use each backbone output directly as the input to the next iteration. These outputs may contain information useful several iterations later, but retaining it across the loop depends entirely on the single hidden state. We introduce StateLoop, which maintains one additional persistent state per token to retain information across iterations. At each iteration, a learned gate controls how much of the previous state is retained and how much information from the backbone output is incorporated. The updated state is projected back and added to the backbone output for subsequent iterations and final prediction. This design reduces Pile perplexity and improves average accuracy across eight zero-shot tasks over Vanilla Looped. Its perplexity advantage over Vanilla Looped grows with trained loop depth, consistent with persistent state becoming increasingly useful as recurrent computation deepens.

Submission history From: Feichen Song [ view email ] [v1] Mon, 26 Oct 2026 14:53:49 UTC (1,254 KB) Full-text links: Access Paper: View a PDF of the paper titled StateLoop: Persistent State for Looped Transformers, by Feichen Song and 9 other authors View PDF HTML (experimental) TeX Source view license Additional Features Audio Summary Current browse context: cs.CL <a class="abs-button prev-url" href="/prevnext?id=2610.35544&function=prev&context=cs.CL" accesskey="p" title="previous in cs.C

## 2610.33517

[2610.33517] One Model, Two Paths: Balancing Single-Pass and Looped Performance in Language Models

[原件](https://arxiv.org/abs/2610.33517)

Abstract: Repeating Transformer layers can improve language-model performance without adding parameters. A pretrained model can be adapted to support both single-pass and looped inference by reusing middle-layer weights for additional computation. Because both paths share weights, training to improve looped predictions can degrade single-pass quality. We study joint training strategies using weighted losses on both outputs, with guidance from the frozen original model. Joint supervision substantially reduces single-pass degradation compared to looped-only training, while preserving looped gains over ordinary continued training. Most of this benefit comes from adjusting the single-pass loss weight, with guidance from the frozen original model further improving the looped output. With validation-selected weights, our method preserves single-pass quality within a predefined tolerance of ordinary continued training while improving looped predictions.

Submission history From: Jiarun Shen [ view email ] [v1] Sat, 24 Oct 2026 07:50:29 UTC (400 KB) Full-text links: Access Paper: View a PDF of the paper titled One Model, Two Paths: Balancing Single-Pass and Looped Performance in Language Models, by Jiarun Shen and 2 other authors View PDF HTML (experimental) TeX Source view license Additional Features Audio Summary Current browse context: cs.CL < prev |

## 2610.33360

[2610.33360] LSTM-Style Looped Transformers with Shared KV Caches

[原件](https://arxiv.org/abs/2610.33360)

Abstract: Recurrent transformers reuse weights to perform deep computation with fewer parameters. We study an LSTM-style transformer that also shares one key--value cache across its recurrent core. At width 1024, it uses 40.4% fewer parameters than an untied control at nearly matched forward FLOPs, and reduces persistent cache sets from fifteen to four. Parallel training supplies cache entries from a standard-attention pass, whereas continuation reads entries produced recursively using shared attention. We address this mismatch by aligning the two training passes' cache entries with a consistency loss during the final 10% of a fixed training-token budget. Across three model widths on FineWeb, this removes 81--89% of the continuation-loss penalty relative to full-cache evaluation. The improvement replicates on disjoint documents for two training seeds. Across four widths and 1.05--4.19B training tokens, the loss cost of weight tying is smallest at lower token budgets, suggesting an opportunity to use recurrent computation when data and model storage are limited.

Submission history From: Andreas Kirsch [ view email ] [v1] Fri, 23 Oct 2026 23:12:12 UTC (136 KB) Full-text links: Access Paper: View a PDF of the paper titled LSTM-Style Looped Transformers with Shared KV Caches, by Andreas Kirsch View PDF HTML (experimental) TeX Source view license Additional Features Audio Summary Current browse context: cs.LG < prev | <a class="abs-but

## 2610.34436

[2610.34436] Prefix Keys and Values Matter Late: RIPE Caching for Self-Speculative Decoding in Looped Language Models

[原件](https://arxiv.org/abs/2610.34436)

Abstract: A looped language model runs one block of layers $R$ times per token, so its key-value (KV) cache holds $R$ planes per recurrent layer, and self-speculative decoding (draft with a few loops, verify with all $R$) reads them all. We find that prefix keys and values matter late: at equal perturbation size, loops 25-32 are $e^{15.0}$ (Huginn-0125) and $e^{12.8}$ (Raven-Llama) times more sensitive than loops 2-9, and the planes approach the last one geometrically, at 0.88 and 0.81 per loop. Whether the deepest plane alone suffices then depends on how ripe the late planes are: on Raven, storing only it is indistinguishable from a bf16-to-fp32 change; on Huginn, 1% of positions carry 74% of its error. We turn this into RIPE, which stores the deepest plane everywhere except a window of recent positions kept at full depth. On Huginn, a 64-position window removes 89% of the tail positions at 11.9% of the full cache's memory (1024-token context), and any window at least as long as the draft block makes batched verification block-independent by construction. Nine pre-registered GPU batches back these results. Simple models of acceptance, decoding cost and memory, two of them checked on held-out measurements, account for the measured self-speculative speed-ups ($2.09\times$ with the full cache, $2.58\times$ with the deepest plane) and decompose the $2.24\times$ fixed-memory throughput gain of one shared plane.

Submission history From: Zixiang Ni [ view email ] [v1] Sun, 25 Oct 2026 16:44:33 UTC (403 KB) Full-text links: Access Paper: View a PDF of the paper titled Prefix Keys and Values Matter Late: RIPE Caching for Self-Speculative Decoding in Looped Language Models, by Dezhen Lu and 2 other authors View PDF HTML (experimental) TeX Source view license Additional Features Audio Summary Current browse context: cs.DC < prev

## 2610.34427

[2610.34427] ScaleRLT: Exact Log-Probabilities and Fast Deferred Rollouts for Reinforcement Learning on Looped Transformers

[原件](https://arxiv.org/abs/2610.34427)

Abstract: Looped language models such as Ouro reuse one block of layers several times per token. A rollout engine can batch the deeper loops of several response positions and run them only when a deep readout is due. This deferred schedule is fast, but the learner of an on-policy RL algorithm recomputes the sampled tokens' log-probabilities with a dense pass, and the two computations differ in floating point: in FP32 at 4096 tokens about 18% of the sampled tokens miss a $10^{-5}$ same-weight gate, and with bf16 weights nearly every token does. We use a hybrid learner log-probability, $\ell=\ell_{\mathrm{dense}}+\mathrm{sg}(\ell_{\mathrm{sched}}-\ell_{\mathrm{dense}})$, where $\mathrm{sg}$ denotes stop-gradient. Its value is a no-grad replay through the rollout's own schedule, and its gradient is the dense learner's. The replay reproduces the rollout bit for bit in all 167 FP32 and 28 bf16 real-weight cells we ran on three platforms, including rollouts whose batch shrinks at stop tokens, and the gradient has the same FP32 error as other dense implementations in all 102 pre-registered comparisons from 96 to 4096 tokens; the full GRPO loss of a training step matches a float64 reference to $3.1\times10^{-4}$. On one GPU, deferral raises rollout throughput by $1.47$ to $1.56\times$, and by $1.18$ to $1.54\times$ once every step runs from CUDA graphs, bit for bit. In a two-node GRPO loop, one-wave KV admission and CUDA graphs shorten an update by $2.71\times$ with the gate bitwise at every update, and four nodes keep the update time within 2% at the same per-GPU load. In 100-update runs held-out GSM8K accuracy rose from 23% to 82% with the mixed-depth readout that deferral relies on and from 34% to 90% with the native readout, which reached a higher accuracy in less time. For looped models beyond one node we analyse a ring mapping of layers to GPUs and measure its communication paths.

Submission history From: Zixiang Ni [ view email ] [v1] Sun, 25 Oct 2026 16:35:30 UTC (38 KB) Full-text links: Access Paper: View a PDF of the paper titled ScaleRLT: Exact Log-Probabilities and Fast Deferred Rollouts for Reinforcement Learning on Looped Transformers, by Dezhen Lu and 2 other authors View PDF HTML (experimental) TeX Source view license Additional Features Audio Summary Current browse context: cs.LG < prev &n

## 2610.35804

[2610.35804] Learning When to Commit: Schedule Distillation for Fast Diffusion Language Models

[原件](https://arxiv.org/abs/2610.35804)

Abstract: Diffusion large language models (dLLMs) can generate multiple tokens in parallel, but often require many decoding rounds to complete a response. Efficient generation depends not only on which tokens are easy to predict, but also on how committing to them helps predict the remaining positions. A highly predictable token may provide little useful context, while revealing a less predictable token can help several other positions become predictable sooner. We propose dSpark, a new schedule distillation-based framework for learning when to commit tokens for faster diffusion language generation. To achieve this, we construct unmasking schedules that prioritize tokens whose reveal makes other positions easier to predict, reducing uncertainty earlier in decoding. We then distill these schedules into the model to enable faster parallel sampling, with a KL-divergence regularizer to help preserve generation quality. We extensively evaluate our approach across mathematical reasoning and code generation tasks. On GSM8K, our method achieves remarkable 10.12$\times$ and 5.12$\times$ speedups over the various baselines on LLaDA-8B-Instruct and Dream-7B-Instruct, respectively, while maintaining superior task performance. Our code is available at this https URL .

Submission history From: Aidar Myrzakhan [ view email ] [v1] Mon, 26 Oct 2026 17:35:58 UTC (523 KB) Full-text links: Access Paper: View a PDF of the paper titled Learning When to Commit: Schedule Distillation for Fast Diffusion Language Models, by Aidar Myrzakhan and 1 other authors View PDF HTML (experimental) TeX Source view license Additional Features Audio Summary Current browse context: cs.CL <a class="abs-button prev-url" href="/prevnext?id=2610.35804&function=prev&context=cs.CL" acc

## 2610.34103

[2610.34103] T2D: Target-to-Draft Model Pruning & Adaptation for Efficient Speculative Decoding

[原件](https://arxiv.org/abs/2610.34103)

Abstract: Speculative decoding significantly accelerates autoregressive text generation in Large Language Models (LLMs), but its efficacy depends largely on two key factors: the distributional alignment between the draft and the target model, and the draft model's latency during inference. However, existing approaches typically utilize independently pretrained small draft models or seek to prune the target model to a manually chosen architecture, thereby failing to explicitly balance the trade-off between draft model alignment and token generation efficiency. To address this gap, we formulate draft model design as an optimization problem and propose T2D, a framework that constructs draft models directly from the target model using latency-aware structured pruning and knowledge distillation. In this manner, T2D obtains draft models that are jointly optimized for both measured inference latency and cross-entropy loss on the target model's responses, resulting in superlative speculative decoding performance. Through extensive experiments on multi-domain speculative decoding benchmarks and across several target model families of differing scale, we demonstrate how T2D prunes up to 92\% of the target model to obtain highly performant draft models compared to competitive baselines. Moreover, draft models obtained via T2D can also be utilized by other speculative decoding token-alignment and knowledge distillation methods in a plug-and-play fashion, leading to further gains. Our findings underscore the importance of jointly navigating the draft model architecture-alignment frontier to unlock the full potential of speculative decoding for LLMs.

Submission history From: Shahriar Kabir Nahin [ view email ] [v1] Sun, 25 Oct 2026 07:00:45 UTC (734 KB) Full-text links: Access Paper: View a PDF of the paper titled T2D: Target-to-Draft Model Pruning & Adaptation for Efficient Speculative Decoding, by Shahriar Kabir Nahin and 4 other authors View PDF HTML (experimental) TeX Source view license Additional Features Audio Summary Current browse context: cs.CL < prev &nbs

## 2610.33719

[2610.33719] ZipFusion: Fusing Lossless KV Decompression with Attention for Efficient LLM Decoding

[原件](https://arxiv.org/abs/2610.33719)

Abstract: The key-value (KV) cache places growing demands on GPU memory capacity and bandwidth as large language models serve longer contexts and more concurrent requests. Its footprint limits concurrency, while repeated KV reads during attention can make decoding memory-bandwidth bound. Prior lossless KV cache compression methods reduce transfers between devices but restore the uncompressed KV cache in GPU memory before attention. They therefore leave these repeated KV reads unchanged and require additional work and memory for decompression. We present ZipFusion, which enables attention to consume the losslessly compressed KV cache directly. ZipFusion co-designs the compression format and attention kernel to reduce the bytes read from GPU memory during attention. The kernel reconstructs the original values directly in registers using simple bit operations, avoiding a separate decompression pass and easing the memory-bandwidth bound. ZipFusion also reassigns memory freed by compression across layers to store additional KV cache. Its memory manager reserves space for ongoing generation and makes the remaining capacity available to new requests. We implement ZipFusion on top of FlashInfer and integrate it with SGLang. On an NVIDIA H100, ZipFusion achieves about 1.25x speedup over FlashInfer in decode attention. With 8K context, it improves model decode throughput by up to 26.3% over uncompressed SGLang under the same GPU memory budget. At each method's largest supported batch, it also delivers up to 2.76x the throughput of the best-performing lossless KV cache compression baseline.

Submission history From: Yuetao Chen [ view email ] [v1] Sat, 24 Oct 2026 15:07:10 UTC (237 KB) Full-text links: Access Paper: View a PDF of the paper titled ZipFusion: Fusing Lossless KV Decompression with Attention for Efficient LLM Decoding, by Yuetao Chen and 1 other authors View PDF HTML (experimental) TeX Source view license Additional Features Audio Summary Current browse context: cs.AR < prev |

## 2610.33625

[2610.33625] RAQ-MLA: Role-Aware Quantization for Multi-Head Latent Attention Caches

[原件](https://arxiv.org/abs/2610.33625)

Abstract: Multi-Head Latent Attention (MLA) has been adopted by recent frontier large language models. Instead of per-head keys and values, MLA caches a compressed KV latent that is up-projected into keys and values at decode time, together with a narrow positional key that carries position information into the attention score. Existing KV-cache quantization methods are designed around the keys and values of standard attention and do not account for what MLA actually caches, which costs accuracy at low bit widths. We analyze the MLA cache both in activation distribution and in how quantization error propagates to the attention output, and show that the two cached tensors play different roles: the latent mainly supplies the values, whereas the positional key dominates the attention score. We therefore propose RAQ-MLA (Role-Aware Quantization for Multi-Head Latent Attention Caches), which fits an invertible transform to each cached tensor against the error that tensor delivers to the attention output: attention-weighted value error for the latent and score perturbation for the positional key. Without training, RAQ-MLA quantizes the full MLA cache to about 2.5 bits per element, a 6.5x increase in theoretical KV-cache capacity, while remaining nearly lossless on reasoning and coding tasks across four MLA models.

Submission history From: Chen Tianqi [ view email ] [v1] Sat, 24 Oct 2026 11:54:55 UTC (7,327 KB) Full-text links: Access Paper: View a PDF of the paper titled RAQ-MLA: Role-Aware Quantization for Multi-Head Latent Attention Caches, by Tianqi Chen and 6 other authors View PDF HTML (experimental) TeX Source view license Additional Features Audio Summary Current browse context: cs.AI <a class="abs-button prev-url" href="/prevnext?id=2610.33625&function=prev&context=cs.AI" accessk

## 2610.33076

[2610.33076] Double KV Cache Optimization on Apple Silicon: Block-FP4, Radial Quantization, and Fused Metal Kernels

[原件](https://arxiv.org/abs/2610.33076)

Abstract: Key-value (KV) cache capacity and memory traffic are primary bottlenecks in long-context autoregressive inference. We evaluate five cache paths on an Apple Silicon M5 Max using MLX: a native bf16 baseline, block-scaled E2M1 FP4, a Python reference implementing radial quantization with a QJL-style residual, sequential FP4-to-Polar composition, and a fused Metal Polar kernel. On Apple Silicon M5 Max, fused Metal PolarQuant achieves 46.8 tok/s at 3,456 B/token - 3.64x compression versus the bf16 baseline and 1.84x faster than the Python Polar reference (25.4 tok/s), while slightly outperforming block-FP4 (41.5 tok/s at 3.62x compression). Sequential composition of FP4 and Polar (Double Optimization) yields no additive benefit: 4,241 B/token at 15.1 tok/s, worse than FP4 alone on both axes. The fused path establishes that radial coding can be competitive when packing, rotation, and reconstruction are placed in one device kernel, but this result does not extend to longer contexts. At 32K and above, all compressed variants collapse to 1.5-14 tok/s because the current attention path repeatedly reconstructs the full cache, retaining cumulative O(N^2) decode work. At 64K, the Metal variant runs out of memory when a 33.5 GB allocation exceeds MLX's 22.6 GB Metal buffer limit. Fused scaled dot-product attention operating directly on compressed KV, together with chunked pre-allocation, is required for long-context viability. These results separate representation-level compression from kernel and allocator effects and identify the conditions under which low-bit KV caching helps on unified memory hardware.

Submission history From: Ibrokhimsho Abduchaborov [ view email ] [v1] Wed, 21 Oct 2026 07:57:51 UTC (33 KB) Full-text links: Access Paper: View a PDF of the paper titled Double KV Cache Optimization on Apple Silicon: Block-FP4, Radial Quantization, and Fused Metal Kernels, by Ibrokhimsho Abduchaborov View PDF HTML (experimental) TeX Source view license Additional Features Audio Summary Current browse context: cs.AR <a class="abs-button prev-url" href="/prevnext?id=2610.33076&function=prev&context=c

## 2610.34721

[2610.34721] Prefetch-Steered Routing: Deterministic Cache-Aware Expert Selection for Offloaded Mixture-of-Experts Decoding

[原件](https://arxiv.org/abs/2610.34721)

Abstract: When a Mixture-of-Experts (MoE) model does not fit in GPU memory, batch-1 decoding is dominated by copying expert weights from host memory. Cache-aware routing reduces these copies by biasing the router toward resident experts, but combined with asynchronous prefetching it makes the model's outputs depend on transfer timing, so a harness that does not simulate that timing no longer evaluates the deployed model. We propose prefetch-steered routing (PSR): routing conditions on a deterministic logical cache, into which at most n experts predicted by the next layer's router are inserted per layer and token; physical copies affect only latency. On OLMoE-1B-7B with 50% and 25% of experts resident on an RTX 4090, PSR decodes 2.2-2.3x faster than exact routing with LRU and 25-30% faster than the Cache-Prior operating point, with mean benchmark differences of +0.1 and +0.5 points (95% lower bounds -0.8 and -0.3). In greedy generation its lead over Cache-Prior depends on the workload and reverses on HumanEval at 50% residency. On Moonlight-16B-A3B, PSR is 1.9x faster than exact routing with LRU at 37.5% residency and, at the latency of Cache-Prior, significantly better on three of eight benchmarks. On Qwen3.6-35B-A3B, where copies are cheap relative to computation, PSR keeps its advantage over Cache-Prior on the likelihood benchmarks but not its speed. Distillation-trained gates did not help. Speculative decoding with block-level expert selection was slower than PSR with a 1B autoregressive drafter on OLMoE, but with a block drafter on Qwen3.6 it was 2.1-2.9x faster than any autoregressive configuration with at most its GPU memory on the 64 prompts we timed.

Submission history From: Siming Huang [ view email ] [v1] Mon, 26 Oct 2026 02:19:12 UTC (355 KB) Full-text links: Access Paper: View a PDF of the paper titled Prefetch-Steered Routing: Deterministic Cache-Aware Expert Selection for Offloaded Mixture-of-Experts Decoding, by Siming Huang View PDF HTML (experimental) TeX Source view license Additional Features Audio Summary Current browse context: cs.AI < prev | <

