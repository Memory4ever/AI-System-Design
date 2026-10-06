# 03/13 首8完整v1题摘实际读取

精确identity/v1由官方API返回；Submitted/Updated不当首公开。root实际题摘校准12201/11535通过potential准入，日期待窄核，不评分/Books。

```json
[
  {
    "id": "http://arxiv.org/abs/2603.12118v1",
    "title": "Cornserve: A Distributed Serving System for Any-to-Any Multimodal Models",
    "submitted": "2026-03-12T16:20:35Z",
    "updated": "2026-03-12T16:20:35Z",
    "abstract": "Any-to-Any models are an emerging class of multimodal models that accept combinations of multimodal data (e.g., text, image, video, audio) as input and generate them as output. Serving these models are challenging; different requests with different input and output modalities traverse different paths through the model computation graph, and each component of the model have different scaling characteristics.\n  We present Cornserve, a distributed serving system for generic Any-to-Any models. Cornserve provides a flexible task abstraction for expressing Any-to-Any model computation graphs, enabling component disaggregation and independent scaling. The distributed runtime dispatches compute to the data plane via an efficient record-and-replay execution model that keeps track of data dependencies, and forwards tensor data between components directly from the producer to the consumer. Built on Kubernetes with approximately 23K new lines of Python, Cornserve supports diverse Any-to-Any models and delivers up to 3.81$\\times$ higher throughput and 5.79$\\times$ lower tail latency. Cornserve is open-source, and the demo video is available on YouTube."
  },
  {
    "id": "http://arxiv.org/abs/2603.11564v1",
    "title": "Where Matters More Than What: Decoding-aligned KV Cache Compression via Position-aware Pseudo Queries",
    "submitted": "2026-03-12T05:36:32Z",
    "updated": "2026-03-12T05:36:32Z",
    "abstract": "The Key-Value (KV) cache is crucial for efficient Large Language Models (LLMs) inference, but excessively long contexts drastically increase KV cache memory footprint. Existing KV cache compression methods typically rely on input-side attention patterns within a prompt observation window to estimate token importance during the prefill stage. They fail to preserve critical tokens for future generation since these assessments are not derived from the decoding process. Intuitively, an effective observation window should mirror the decoding-stage queries to accurately reflect which tokens the generation process will attend to. However, ground-truth decoding queries are inherently unavailable during inference. For constructing pseudo queries to approximate them, we find that positional information plays a more critical role than semantic content. Motivated by this insight, we propose decoding-aligned KV cache compression via position-aware pseudo queries (DapQ), a novel and lightweight eviction framework that leverages position-aware pseudo queries to simulate the output tokens, thereby establishing an effective observation window for importance assessment. It aligns closely with the actual generation context and enables precise token eviction. Extensive evaluations across multiple benchmarks and LLMs demonstrate that DapQ achieves superior performance, particularly under strict memory constraints (e.g., up to nearly lossless performance 99.5% on NIAH with 3% KV cache budgets)."
  },
  {
    "id": "http://arxiv.org/abs/2603.11535v1",
    "title": "Expert Threshold Routing for Autoregressive Language Modeling with Dynamic Computation Allocation and Load Balancing",
    "submitted": "2026-03-12T04:45:48Z",
    "updated": "2026-03-12T04:45:48Z",
    "abstract": "Token-choice Mixture-of-Experts (TC-MoE) routes each token to a fixed number of experts, limiting dynamic computation allocation and requiring auxiliary losses to maintain load balance. We propose Expert Threshold (ET) routing, where each expert maintains an exponential moving average (EMA) threshold estimated from the global token distribution. At both training and inference, each token is independently routed to an expert if its score exceeds the expert's threshold, enabling dynamic computation allocation while achieving load balance without auxiliary losses. This fully causal mechanism eliminates dependence on other tokens in the batch, making it well-suited for autoregressive language modeling. In pretraining experiments scaling to 2.4B parameters on FineWeb-Edu, ET achieves 0.067 lower cross-entropy loss than TC-MoE, equivalent to reaching the same performance with 1.6$\\times$ fewer tokens."
  },
  {
    "id": "http://arxiv.org/abs/2603.11487v1",
    "title": "Attention Sinks Are Provably Necessary in Softmax Transformers: Evidence from Trigger-Conditional Tasks",
    "submitted": "2026-03-12T03:13:28Z",
    "updated": "2026-03-12T03:13:28Z",
    "abstract": "Transformers often display an attention sink: probability mass concentrates on a fixed, content-agnostic position. We prove that computing a simple trigger-conditional behavior necessarily induces a sink in softmax self-attention models. Our results formalize a familiar intuition: normalization over a probability simplex must force attention to collapse onto a stable anchor to realize a default state (e.g., when the model needs to ignore the input). We instantiate this with a concrete task: when a designated trigger token appears, the model must return the average of all preceding token representations, and otherwise output zero, a task which mirrors the functionality of attention heads in the wild (Barbero et al., 2025; Guo et al., 2024). We also prove that non-normalized ReLU attention can solve the same task without any sink, confirming that the normalization constraint is the fundamental driver of sink behavior. Experiments validate our predictions and demonstrate they extend beyond the theoretically analyzed setting: softmax models develop strong sinks while ReLU attention eliminates them in both single-head and multi-head variants."
  },
  {
    "id": "http://arxiv.org/abs/2603.12201v1",
    "title": "IndexCache: Accelerating Sparse Attention via Cross-Layer Index Reuse",
    "submitted": "2026-03-12T17:27:21Z",
    "updated": "2026-03-12T17:27:21Z",
    "abstract": "Long-context agentic workflows have emerged as a defining use case for large language models, making attention efficiency critical for both inference speed and serving cost. Sparse attention addresses this challenge effectively, and DeepSeek Sparse Attention (DSA) is a representative production-grade solution: a lightweight lightning indexer selects the top-k most relevant tokens per query, reducing core attention from $O(L^2)$ to $O(Lk)$. However, the indexer itself retains $O(L^2)$ complexity and must run independently at every layer, despite the fact that the resulting top-k selections are highly similar across consecutive layers. We present IndexCache, which exploits this cross-layer redundancy by partitioning layers into a small set of Full layers that run their own indexers and a majority of Shared layers that simply reuse the nearest Full layer's top-k indices. We propose two complementary approaches to determine and optimize this configuration. Training-free IndexCache applies a greedy search algorithm that selects which layers to retain indexers by directly minimizing language modeling loss on a calibration set, requiring no weight updates. Training-aware IndexCache introduces a multi-layer distillation loss that trains each retained indexer against the averaged attention distributions of all layers it serves, enabling even simple interleaved patterns to match full-indexer accuracy. Experimental results on a 30B DSA model show that IndexCache can remove 75% of indexer computations with negligible quality degradation, achieving up to 1.82$\\times$ prefill speedup and 1.48$\\times$ decode speedup compared to standard DSA. These positive results are further confirmed by our preliminary experiments on the production-scale GLM-5 model (Figure 1)."
  },
  {
    "id": "http://arxiv.org/abs/2603.11873v1",
    "title": "AdaFuse: Accelerating Dynamic Adapter Inference via Token-Level Pre-Gating and Fused Kernel Optimization",
    "submitted": "2026-03-12T12:46:42Z",
    "updated": "2026-03-12T12:46:42Z",
    "abstract": "The integration of dynamic, sparse structures like Mixture-of-Experts (MoE) with parameter-efficient adapters (e.g., LoRA) is a powerful technique for enhancing Large Language Models (LLMs). However, this architectural enhancement comes at a steep cost: despite minimal increases in computational load, the inference latency often skyrockets, leading to decoding speeds slowing by over 2.5 times. Through a fine-grained performance analysis, we pinpoint the primary bottleneck not in the computation itself, but in the severe overhead from fragmented, sequential CUDA kernel launches required for conventional dynamic routing. To address this challenge, we introduce AdaFuse, a framework built on a tight co-design between the algorithm and the underlying hardware system to enable efficient dynamic adapter execution. Departing from conventional layer-wise or block-wise routing, AdaFuse employs a token-level pre-gating strategy, which makes a single, global routing decision for all adapter layers before a token is processed. This \"decide-once, apply-everywhere\" approach effectively staticizes the execution path for each token, creating an opportunity for holistic optimization. We capitalize on this by developing a custom CUDA kernel that performs a fused switching operation, merging the parameters of all selected LoRA adapters into the backbone model in a single, efficient pass. Experimental results on popular open-source LLMs show that AdaFuse achieves accuracy on par with state-of-the-art dynamic adapters while drastically cutting decoding latency by a factor of over 2.4x, thereby bridging the gap between model capability and inference efficiency."
  },
  {
    "id": "http://arxiv.org/abs/2603.12038v1",
    "title": "Slow-Fast Inference: Training-Free Inference Acceleration via Within-Sentence Support Stability",
    "submitted": "2026-03-12T15:14:48Z",
    "updated": "2026-03-12T15:14:48Z",
    "abstract": "Long-context autoregressive decoding remains expensive because each decoding step must repeatedly process a growing history. We observe a consistent pattern during decoding: within a sentence, and more generally within a short semantically coherent span, the dominant attention support often remains largely stable. Motivated by this observation, we propose Slow-Fast Inference (SFI), a training-free decoding framework that decouples generation into frequent low-cost fast steps and occasional dense-attention slow steps. Fast steps reuse a compact sparse memory for efficient decoding. Slow steps are triggered near semantic boundaries. At slow steps, the model revisits the broader context and uses the Selector to refresh the selected memory for subsequent fast steps. Across the evaluated context lengths, SFI delivers approximately $1.6\\times$--$14.4\\times$ higher decoding throughput while generally maintaining quality on par with the full-KV baseline across long-context and long-CoT settings. Because SFI is training-free and applies directly to existing checkpoints, it offers a practical path to reducing inference cost for contemporary autoregressive reasoning models in long-context, long-horizon, and agentic workloads."
  },
  {
    "id": "http://arxiv.org/abs/2603.12248v1",
    "title": "Matching Features, Not Tokens: Energy-Based Fine-Tuning of Language Models",
    "submitted": "2026-03-12T17:57:50Z",
    "updated": "2026-03-12T17:57:50Z",
    "abstract": "Cross-entropy (CE) training provides dense and scalable supervision for language models, but it optimizes next-token prediction under teacher forcing rather than sequence-level behavior under model rollouts. We introduce a feature-matching objective for language-model fine-tuning that targets sequence-level statistics of the completion distribution, providing dense semantic feedback without requiring a task-specific verifier or preference model. To optimize this objective efficiently, we propose energy-based fine-tuning (EBFT), which uses strided block-parallel sampling to generate multiple rollouts from nested prefixes concurrently, batches feature extraction over these rollouts, and uses the resulting embeddings to perform an on-policy policy-gradient update. We present a theoretical perspective connecting EBFT to KL-regularized feature-matching and energy-based modeling. Empirically, across Q&A coding, unstructured coding, and translation, EBFT matches RLVR and outperforms SFT on downstream accuracy while achieving a lower validation cross-entropy than both methods."
  }
]

```

