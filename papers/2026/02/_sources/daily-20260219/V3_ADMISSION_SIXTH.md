# 本日第六批准入校准

完整精确v1题摘，只本日材料，原库存不是默认逐项关闭队列。以下具体主张潜在准入，待root校准；分数在准入后仅定位最低投入。

## 2602.15329v1 — EventMemAgent: Hierarchical Event-Centric Memory for Online Video Understanding with Adaptive Tool Use

[精确v1](https://arxiv.org/html/2602.15329v1)

Online video understanding requires models to perform continuous perception and long-range reasoning within potentially infinite visual streams. Its fundamental challenge lies in the conflict between the unbounded nature of streaming media input and the limited context window of Multimodal Large Language Models (MLLMs). Current methods primarily rely on passive processing, which often face a trade-off between maintaining long-range context and capturing the fine-grained details necessary for complex tasks. To address this, we introduce EventMemAgent , an active online video agent framework based on a hierarchical memory module . Our framework employs a dual-layer strategy for online videos: short-term memory detects event boundaries and utilizes event-granular reservoir sampling to process streaming video frames within a fixed-length buffer dynamically; long-term memory structuredly archives past observations on an event-by-event basis. Furthermore, we integrate a multi-granular perception toolkit for active, iterative evidence capture and employ Agentic Reinforcement Learning (Agentic RL) to end-to-end internalize reasoning and tool-use strategies into the agent’s intrinsic capabilities. Experiments show that EventMemAgent achieves competitive results on online video benchmarks. The code will be released here: https://github.com/lingcco/EventMemAgent.

准入理由：固定buffer逐frame被动采样会丢事件/细节→event boundary内reservoir+event longterm archive与主动取证→分开保留population和按需细粒度读取。潜在2+2+2=6。

## 2602.15338v1 — Discovering Implicit Large Language Model Alignment Objectives

[精确v1](https://arxiv.org/html/2602.15338v1)

Large language model (LLM) alignment relies on complex reward signals that often obscure the specific behaviors being incentivized, creating critical risks of misalignment and reward hacking. Existing interpretation methods typically rely on pre-defined rubrics, risking the omission of "unknown unknowns", or fail to identify objectives that comprehensively cover and are causal to the model behavior. To address these limitations, we introduce Obj-Disco, a framework that automatically decomposes an alignment reward signal into a sparse, weighted combination of human-interpretable natural language objectives. Our approach utilizes an iterative greedy algorithm to analyze behavioral changes across training checkpoints, identifying and validating candidate objectives that best explain the residual reward signal. Extensive evaluations across diverse tasks, model sizes, and alignment algorithms demonstrate the framework’s robustness. Experiments with popular open-source reward models show that the framework consistently captures &gt; 90% of reward behavior, a finding further corroborated by human evaluation. Additionally, a case study on alignment with an open-source reward model reveals that Obj-Disco can successfully identify latent misaligned incentives that emerge alongside intended behaviors. Our work provides a crucial tool for uncovering the implicit objectives in LLM alignment, paving the way for more transparent and safer AI development.

准入理由：既有bias/rubric预设会漏未知reward incentives→checkpoint行为差额的residual reward贪心稀疏objective分解与验证→解释coverage/causal validation分责。潜在2+1+2=5。

## 2602.15344v1 — ER-MIA: Black-Box Adversarial Memory Injection Attacks on Long-Term Memory-Augmented Large Language Models

[精确v1](https://arxiv.org/html/2602.15344v1)

Large language models (LLMs) are increasingly augmented with long-term memory systems to overcome finite context windows and enable persistent reasoning across interactions. However, recent research finds that LLMs become more vulnerable because memory provides extra attack surfaces. In this paper, we present the first systematic study of black-box adversarial memory injection attacks that target the similarity-based retrieval mechanism in long-term memory–augmented LLMs. We introduce ER-MIA , a unified framework that exposes this vulnerability and formalizes two realistic attack settings: content-based attacks and question-targeted attacks. In these settings, ER-MIA includes an arsenal of composable attack primitives and ensemble attacks that achieve high success rates under minimal attacker assumptions. Extensive experiments across multiple LLMs and long-term memory systems demonstrate that similarity-based retrieval constitutes a fundamental and system-level vulnerability, revealing security risks that persist across memory designs and application scenarios. 1 1 1 Codes will be made publicly available.

准入理由：memory更新trusted且相似检索被当证据→content与question-targeted黑盒memory injection组合→write/retrieval/read权限与跨轮persistent影响要分责。潜在2+2+2=6，安全必要核心深入。

## 2602.15364v1 — MarkSweep: A No-box Removal Attack on AI-Generated Image Watermarking via Noise Intensification and Frequency-aware Denoising

[精确v1](https://arxiv.org/html/2602.15364v1)

AI watermarking embeds invisible signals within images to provide provenance information and identify content as AI-generated. In this paper, we introduce MarkSweep , a novel watermark removal attack that effectively erases the embedded watermarks from AI-generated images without degrading visual quality. MarkSweep first amplifies watermark noise in high-frequency regions via edge-aware Gaussian perturbations and injects it into clean images for training a denoising network. This network then integrates two modules, the learnable frequency decomposition module and the frequency-aware fusion module, to suppress amplified noise and eliminate watermark traces. Theoretical analysis and extensive experiments demonstrate that invisible watermarks are highly vulnerable to MarkSweep , which effectively removes embedded watermarks, reducing the bit accuracy of HiDDeN and Stable Signature watermarking schemes to below 67%, while preserving perceptual quality of AI-generated images.

准入理由：检测水印持久性不等任意内容保持变换鲁棒→edge-aware噪声放大训练frequency denoiser擦除→watermark安全归因须重验这类编辑和quality取舍。潜在2+2+2=6，安全必要核心深入。

## 2602.15379v1 — FlashMem: Supporting Modern DNN Workloads on Mobile with GPU Memory Hierarchy Optimizations

[精确v1](https://arxiv.org/html/2602.15379v1)

The increasing size and complexity of modern deep neural networks (DNNs) pose significant challenges for on-device inference on mobile GPUs, with limited memory and computational resources. Existing DNN acceleration frameworks primarily deploy a weight preloading strategy, where all model parameters are loaded into memory before execution on mobile GPUs. We posit that this approach is not adequate for modern DNN workloads that comprise very large model(s) and possibly execution of several distinct models in succession. In this work, we introduce FlashMem, a memory streaming framework designed to efficiently execute large-scale modern DNNs and multi-DNN workloads while minimizing memory consumption and reducing inference latency. Instead of fully preloading weights, FlashMem statically determines model loading schedules and dynamically streams them on demand, leveraging 2.5D texture memory to minimize data transformations and improve execution efficiency. Experimental results on 11 models demonstrate that FlashMem achieves 2.0\times to 8.4\times memory reduction and 1.7\times to 75.0\times speedup compared to existing frameworks, enabling efficient execution of large-scale models and multi-DNN support on resource-constrained mobile GPUs.

准入理由：mobile GPU预载大模型/多模型参数使容量受限→static schedule/demand stream与2.5D texture layout减少转换→GPU memory hierarchy与stream preload共存条件。潜在2+1+2=5；定点scope/core确认非仅数字应用。

## 2602.15382v1 — The Vision Wormhole: Latent-Space Communication in Heterogeneous Multi-Agent Systems

[精确v1](https://arxiv.org/html/2602.15382v1)

Multi-Agent Systems (MAS) powered by Large Language Models have unlocked advanced collaborative reasoning, yet they remain shackled by the inefficiency of discrete text communication, which imposes significant runtime overhead and information quantization loss. While latent state transfer offers a high-bandwidth alternative, existing approaches either assume homogeneous sender–receiver architectures or rely on pair-specific learned translators, limiting scalability and modularity across diverse model families with disjoint manifolds. In this work, we propose the Vision Wormhole , a novel framework that repurposes the visual interface of Vision-Language Models (VLMs) to enable model-agnostic, text-free communication. By introducing a Universal Visual Codec, we map heterogeneous reasoning traces into a shared continuous latent space and inject them directly into the receiver’s visual pathway, effectively treating the vision encoder as a universal port for inter-agent telepathy. Our framework adopts a hub-and-spoke topology to reduce pairwise alignment complexity from O(N^{2}) to O(N) and leverages a label-free, teacher-student distillation objective to align the high-speed visual channel with the robust reasoning patterns of the text pathway. Extensive experiments across heterogeneous model families (e.g., Qwen-VL, Gemma) demonstrate that the Vision Wormhole reduces end-to-end wall-clock time in controlled comparisons while maintaining reasoning fidelity comparable to standard text-based MAS. Code is available at https://github.com/xz-liu/heterogeneous-latent-mas

准入理由：异构latent communication pair translators N²→sharedvisual codec/hub-and-spoke及text-path distillation→每receiver visualport适配/前置训练与online通信成本分离。潜在2+2+2=6。


