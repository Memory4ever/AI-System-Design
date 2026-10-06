# 本日现有178题名有限18具体信号完整v1题摘

全部以下摘要实际完整读；题名相关仍非全文队列。每个潜在项只待日期与必要命题证明，不授摘要claim成立。

```json
{
  "queries": [
    {
      "url": "https://export.arxiv.org/api/query?id_list=2603.17063v1,2603.17104v1,2603.17170v1,2603.17174v1,2603.17484v1,2603.17771v1,2603.17884v1,2603.17917v1,2603.17946v1&max_results=9",
      "rows": [
        {
          "id": "http://arxiv.org/abs/2603.17063v1",
          "title": "Transformers are Bayesian Networks",
          "abstract": "Transformers are the dominant architecture in AI, yet why they work remains poorly understood. This paper offers a precise answer: a transformer is a Bayesian network. We establish this in five ways. First, we prove that every sigmoid transformer with any weights implements weighted loopy belief propagation on its implicit factor graph. One layer is one round of BP. This holds for any weights -- trained, random, or constructed. Formally verified against standard mathematical axioms. Second, we give a constructive proof that a transformer can implement exact belief propagation on any declared knowledge base. On knowledge bases without circular dependencies this yields provably correct probability estimates at every node. Formally verified against standard mathematical axioms. Third, we prove uniqueness: a sigmoid transformer that produces exact posteriors necessarily has BP weights. There is no other path through the sigmoid architecture to exact posteriors. Formally verified against standard mathematical axioms. Fourth, we delineate the AND/OR boolean structure of the transformer layer: attention is AND, the FFN is OR, and their strict alternation is Pearl's gather/update algorithm exactly. Fifth, we confirm all formal results experimentally, corroborating the Bayesian network characterization in practice. We also establish the practical viability of loopy belief propagation despite the current lack of a theoretical convergence guarantee. We further prove that verifiable inference requires a finite concept space. Any finite verification procedure can distinguish at most finitely many concepts. Without grounding, correctness is not defined. Hallucination is not a bug that scaling can fix. It is the structural consequence of operating without concepts. Formally verified against standard mathematical axioms.",
          "submitted": "2026-03-17T18:50:13Z",
          "updated": "2026-03-17T18:50:13Z",
          "comment": ""
        },
        {
          "id": "http://arxiv.org/abs/2603.17170v1",
          "title": "PAuth - Precise Task-Scoped Authorization For Agents",
          "abstract": "The emerging agentic web envisions AI agents that reliably fulfill users' natural-language (NL)-based tasks by interacting with existing web services. However, existing authorization models are misaligned with this vision. In particular, today's operator-scoped authorization, exemplified by OAuth, grants broad permissions tied to operators (e.g., the transfer operator) rather than to the specific operations (e.g., transfer $100 to Bob) implied by a user's task. This will inevitably result in overprivileged agents. We introduce Precise Task-Scoped Implicit Authorization (PAuth), a fundamentally different model in which submitting an NL task implicitly authorizes only the concrete operations required for its faithful execution. To make this enforceable at servers, we propose NL slices: symbolic specifications of the calls each service expects, derived from the task and upstream results. Complementing this, we also propose envelopes: special data structure to bind each operand's concrete value to its symbolic provenance, enabling servers to verify that all operands arise from legitimate computations. PAuth is prototyped in the agent-security evaluation framework AgentDojo. We evaluate it in both benign settings and attack scenarios where a spurious operation is injected into an otherwise normal task. In all benign tests, PAuth executes the tasks successfully without requiring any additional permissions. In all attack tests, PAuth correctly raises warnings about missing permissions. These results demonstrate that PAuth's reasoning about permissions is indeed precise. We further analyze the characteristics of these tasks and measure the associated token costs.",
          "submitted": "2026-03-17T22:05:03Z",
          "updated": "2026-03-17T22:05:03Z",
          "comment": ""
        },
        {
          "id": "http://arxiv.org/abs/2603.17884v1",
          "title": "DebugLM: Learning Traceable Training Data Provenance for LLMs",
          "abstract": "Large language models (LLMs) are trained through multi-stage pipelines over heterogeneous data sources, yet developers lack a principled way to pinpoint the specific data responsible for an observed behavior. This lack of observability reduces debugging to reactive patching and makes failures prone to recur under distribution shift or subsequent model updates. To address this limitation, we propose DebugLM, a framework that equips LLMs with built-in data provenance, enabling them to explicitly trace the origins of their behaviors to specific training data sources. Specifically, the model learns to associate its responses with unique provenance tags that indicate the responsible dataset, empowering developers to precisely identify where undesirable behaviors are learned. Building on this capability, DebugLM further supports targeted test-time remediation, enabling developers to selectively trigger targeted refusal for specified data sources without retraining or modifying model parameters. Experiments demonstrate that DebugLM provides accurate behavior tracing in multi-stage training pipelines and effective test-time remediation while preserving the general utility of the model.",
          "submitted": "2026-03-18T16:06:21Z",
          "updated": "2026-03-18T16:06:21Z",
          "comment": ""
        },
        {
          "id": "http://arxiv.org/abs/2603.17917v1",
          "title": "Only relative ranks matter in weight-clustered large language models",
          "abstract": "Large language models (LLMs) contain billions of parameters, yet many exact values are not essential. We show that what matters most is the relative rank of weights-whether one connection is stronger or weaker than another-rather than precise magnitudes. To reduce the number of unique weight values, we apply weight clustering to pretrained models, replacing every weight matrix with K shared values from K-means. For Llama 3.1-8B-Instruct and SmolLM2-135M, reducing each matrix to only 16-64 distinct values preserves strong accuracy without retraining, providing a simple, training-free method to compress LLMs on disk. Optionally fine-tuning only the cluster means (centroids) recovers 30-40 percent of the remaining accuracy gap at minimal cost. We then systematically randomize cluster means while keeping assignments fixed. Scrambling the relative ranks of the clusters degrades quality sharply-perplexity can increase by orders of magnitude-even when global statistics such as mean and variance are preserved. In contrast, rank-preserving randomizations cause almost no loss at mid and late layers. On the other hand, when many layers are perturbed simultaneously, progressive layer-by-layer replacement reveals that scale drift-not rank distortion-is the dominant collapse mechanism; however, an affine correction w' = aw + b with a > 0 (which preserves both rank order and overall weight distribution) can substantially delay this drift. This rank-based perspective offers a new lens on model compression and robustness.",
          "submitted": "2026-03-18T16:55:13Z",
          "updated": "2026-03-18T16:55:13Z",
          "comment": "10 pages, 3 figures, 9 tables"
        },
        {
          "id": "http://arxiv.org/abs/2603.17946v1",
          "title": "CARE: Covariance-Aware and Rank-Enhanced Decomposition for Enabling Multi-Head Latent Attention",
          "abstract": "Converting pretrained attention modules such as grouped-query attention (GQA) into multi-head latent attention (MLA) can improve expressivity without increasing KV-cache cost, making it attractive for efficient inference. However, many practical conversion baselines rely on weight-only low-rank approximations (e.g., SVD-style initializations) and uniform rank allocation. They focus on minimizing the difference between weight matrices rather than on how those weights affect input activations, ignore the covariance structure of activations, and enforce uniform rank across layers, causing activation drift and degraded attention fidelity. To address these issues, we propose CARE, a Covariance-Aware, Rank-Enhanced MLA conversion pipeline under a fixed KV width. CARE introduces three key steps: (i) activation-preserving factorization, which aligns the approximation with the actual input activations rather than just the weights; (ii) adjusted-rank allocation, which spreads a fixed KV budget across layers by giving more capacity to layers that need it most; and (iii) KV-parity mapping, which reparameterizes the converted K and V to fit the MLA format while keeping the KV-cache size unchanged. Our method outperforms a uniform-rank SVD baseline on Qwen3-4B/30B-A3B-Instruct-2507 and Llama-3.1-8B/70B-Instruct, reducing one-shot perplexity by up to 215x and improving mean accuracy by up to 1.70x at matched KV budgets. With a brief post-SVD healing fine-tune, we fully recover the original model's accuracy.",
          "submitted": "2026-03-18T17:18:35Z",
          "updated": "2026-03-18T17:18:35Z",
          "comment": "Accepted at ICLR 2026. Conference paper. 10 pages main text; 34 pages total including references and appendix. 11 figures and 20 tables in total"
        },
        {
          "id": "http://arxiv.org/abs/2603.17104v1",
          "title": "When the Specification Emerges: Benchmarking Faithfulness Loss in Long-Horizon Coding Agents",
          "abstract": "Current coding-agent benchmarks usually pro- vide the full task specification upfront. Real research coding often does not: the intended system is progressively disclosed through in- teraction, requiring the agent to track durable design commitments across a long session. We introduce a benchmark for this setting and study faithfulne Ss Loss U nder eM ergent s Pecification (SLUMP), defined as the reduc- tion in final implementation faithfulness un- der emergent specification relative to a single- shot specification control. The benchmark con- tains 20 recent ML papers (10 ICML 2025, 10 NeurIPS 2025), 371 atomic verifiable compo- nents, and interaction scripts of approximately 60 coding requests that progressively disclose the target design without revealing the paper itself. Final repositories are scored with a five-level component-faithfulness rubric and accompanied by an exposure audit to verify that scored components are recoverable from the visible interaction. Evaluated on Claude Code and Codex, the single-shot specification control achieves higher overall implementation fidelity on 16/20 and 14/20 papers, respectively. Structural integration degrades under emergent specification on both platforms, while seman- tic faithfulness loss is substantial on Claude Code and small on Codex. As a mitigation case study, we introduce ProjectGuard, an exter- nal project-state layer for specification tracking. On Claude Code, ProjectGuard recovers 90% of the faithfulness gap, increases fully faith- ful components from 118 to 181, and reduces severe failures from 72 to 49. These results identify specification tracking as a distinct eval- uation target for long-horizon coding agents.",
          "submitted": "2026-03-17T19:53:35Z",
          "updated": "2026-03-17T19:53:35Z",
          "comment": ""
        },
        {
          "id": "http://arxiv.org/abs/2603.17174v1",
          "title": "Detecting Data Poisoning in Code Generation LLMs via Black-Box, Vulnerability-Oriented Scanning",
          "abstract": "Code generation large language models (LLMs) are increasingly integrated into modern software development workflows. Recent work has shown that these models are vulnerable to backdoor and poisoning attacks that induce the generation of insecure code, yet effective defenses remain limited. Existing scanning approaches rely on token-level generation consistency to invert attack targets, which is ineffective for source code where identical semantics can appear in diverse syntactic forms. We present CodeScan, which, to the best of our knowledge, is the first poisoning-scanning framework tailored to code generation models. CodeScan identifies attack targets by analyzing structural similarities across multiple generations conditioned on different clean prompts. It combines iterative divergence analysis with abstract syntax tree (AST)-based normalization to abstract away surface-level variation and unify semantically equivalent code, isolating structures that recur consistently across generations. CodeScan then applies LLM-based vulnerability analysis to determine whether the extracted structures contain security vulnerabilities and flags the model as compromised when such a structure is found. We evaluate CodeScan against four representative attacks under both backdoor and poisoning settings across three real-world vulnerability classes. Experiments on 108 models spanning three architectures and multiple model sizes demonstrate 97%+ detection accuracy with substantially lower false positives than prior methods.",
          "submitted": "2026-03-17T22:08:45Z",
          "updated": "2026-03-17T22:08:45Z",
          "comment": "Preprint"
        },
        {
          "id": "http://arxiv.org/abs/2603.17484v1",
          "title": "Learning When to Attend: Conditional Memory Access for Long-Context LLMs",
          "abstract": "Language models struggle to generalize beyond pretraining context lengths, limiting long-horizon reasoning and retrieval. Continued pretraining on long-context data can help but is expensive due to the quadratic scaling of Attention. We observe that most tokens do not require (Global) Attention over the entire sequence and can rely on local context. Based on this, we propose L2A (Learning To Attend), a layer that enables conditional (token-wise) long-range memory access by deciding when to invoke global attention. We evaluate L2A on Qwen 2.5 and Qwen 3 models, extending their effective context length from 32K to 128K tokens. L2A matches the performance of standard long-context training to within 3% while skipping Global Attention for $\\sim$80% of tokens, outperforming prior baselines. We also design custom Triton kernels to efficiently implement this token-wise conditional Attention on GPUs, achieving up to $\\sim$2x improvements in training throughput and time-to-first-token over FlashAttention. Moreover, L2A enables post-training pruning of highly sparse Global Attention layers, reducing KV cache memory by up to 50% with negligible performance loss.",
          "submitted": "2026-03-18T08:48:18Z",
          "updated": "2026-03-18T08:48:18Z",
          "comment": "26 pages, 6 Tables, 18 Figures"
        },
        {
          "id": "http://arxiv.org/abs/2603.17771v1",
          "title": "Attention Sinks Induce Gradient Sinks",
          "abstract": "Attention sinks and massive activations are recurring and closely related phenomena in Transformer models. Existing studies have largely focused on the forward pass, making it unclear whether their connection is direct or mediated by a training-time mechanism. We study this question from the perspective of backpropagation. Empirically and theoretically, we show that under causal mask, attention sinks can induce pronounced gradient concentration, which we term gradient sinks. Furthermore, in pre-norm architectures with RMSNorm, massive activations can be understood as an adaptive response to this localized gradient pressure during training. To test this hypothesis, we introduce V-scale, a modification that adjusts value-path backpropagated gradients. In pretrained V-scale models, attention sinks are preserved whereas massive activations are suppressed. These results support the interpretation that gradient sink is a key training-time mediator linking attention sinks and massive activations.",
          "submitted": "2026-03-18T14:31:21Z",
          "updated": "2026-03-18T14:31:21Z",
          "comment": "10 pages, 5 figures"
        }
      ]
    },
    {
      "url": "https://export.arxiv.org/api/query?id_list=2603.17117v1,2603.17044v1,2603.17476v1,2603.17541v1,2603.17828v1,2603.17639v1,2603.17677v1,2603.17775v1,2603.17902v1&max_results=9",
      "rows": [
        {
          "id": "http://arxiv.org/abs/2603.17044v1",
          "title": "Do Understanding and Generation Fight? A Diagnostic Study of DPO for Unified Multimodal Models",
          "abstract": "Unified multimodal models share a language model backbone for both understanding and generating images. Can DPO align both capabilities simultaneously? We present the first systematic study of this question, applying DPO to Janus-Pro at 1B and 7B parameters under seven training strategies and two post-hoc methods. The central finding is negative: generation quality resists DPO alignment across all tested conditions on this architecture. No method improves generation CLIPScore at 7B (|Delta| < 0.2, p > 0.5 at n=200 per seed, 3 seeds); at 1B, all methods degrade generation, and the result holds across preference data types (real-vs-generated and model-vs-model) and the data volumes tested (150-288 pairs). Gradient analysis reveals why: understanding and generation gradients are near-orthogonal (cos ~ 0) with ~11-14x magnitude imbalance driven by VQ token count asymmetry (576 generation tokens vs. ~30-100 text tokens). This imbalance is the dominant interference mechanism in multi-task DPO; magnitude-balancing yields directionally positive understanding deltas (+0.01-0.04 VQA, though individually not significant), but the generation gap persists regardless. We identify discrete VQ tokenization as a likely structural bottleneck -- supported by the generation DPO loss converging to ln(2) -- and provide practical guidance for practitioners working with VQ-based unified models.",
          "submitted": "2026-03-17T18:26:29Z",
          "updated": "2026-03-17T18:26:29Z",
          "comment": "8 pages, CVPR MMF5M Workshop 2026"
        },
        {
          "id": "http://arxiv.org/abs/2603.17677v1",
          "title": "Adaptive Guidance for Retrieval-Augmented Masked Diffusion Models",
          "abstract": "Retrieval-Augmented Generation (RAG) improves factual grounding by incorporating external knowledge into language model generation. However, when retrieved context is noisy, unreliable, or inconsistent with the model's parametric knowledge, it introduces retrieval-prior conflicts that can degrade generation quality. While this problem has been studied in autoregressive language models, it remains largely unexplored in diffusion-based language models, where the iterative denoising process introduces unique challenges for integrating retrieved context. In this work, we propose Adaptive Retrieval-Augmented Masked Diffusion (ARAM), a training-free adaptive guidance framework for Masked Diffusion Models (MDMs) in RAG settings. ARAM dynamically calibrates the guidance scale during denoising according to the Signal-to-Noise Ratio (SNR) of the distributional shift induced by retrieved context. Intuitively, the model strengthens guidance when the retrieved context provides reliable corrective evidence and suppresses it when the contextual signal is noisy or non-supportive. Extensive experiments on multiple knowledge-intensive QA benchmarks show that ARAM improves overall QA performance over competitive RAG baselines.",
          "submitted": "2026-03-18T12:54:50Z",
          "updated": "2026-03-18T12:54:50Z",
          "comment": ""
        },
        {
          "id": "http://arxiv.org/abs/2603.17902v1",
          "title": "Differential Privacy in Generative AI Agents: Analysis and Optimal Tradeoffs",
          "abstract": "Large language models (LLMs) and AI agents are increasingly integrated into enterprise systems to access internal databases and generate context-aware responses. While such integration improves productivity and decision support, the model outputs may inadvertently reveal sensitive information. Although many prior efforts focus on protecting the privacy of user prompts, relatively few studies consider privacy risks from the enterprise data perspective. Hence, this paper develops a probabilistic framework for analyzing privacy leakage in AI agents based on differential privacy. We model response generation as a stochastic mechanism that maps prompts and datasets to distributions over token sequences. Within this framework, we introduce token-level and message-level differential privacy and derive privacy bounds that relate privacy leakage to generation parameters such as temperature and message length. We further formulate a privacy-utility design problem that characterizes optimal temperature selection.",
          "submitted": "2026-03-18T16:35:12Z",
          "updated": "2026-03-18T16:35:12Z",
          "comment": ""
        },
        {
          "id": "http://arxiv.org/abs/2603.17775v1",
          "title": "CoVerRL: Breaking the Consensus Trap in Label-Free Reasoning via Generator-Verifier Co-Evolution",
          "abstract": "Label-free reinforcement learning enables large language models to improve reasoning capabilities without ground-truth supervision, typically by treating majority-voted answers as pseudo-labels. However, we identify a critical failure mode: as training maximizes self-consistency, output diversity collapses, causing the model to confidently reinforce systematic errors that evade detection. We term this the consensus trap. To escape it, we propose CoVerRL, a framework where a single model alternates between generator and verifier roles, with each capability bootstrapping the other. Majority voting provides noisy but informative supervision for training the verifier, while the improving verifier progressively filters self-consistent errors from pseudo-labels. This co-evolution creates a virtuous cycle that maintains high reward accuracy throughout training. Experiments across Qwen and Llama model families demonstrate that CoVerRL outperforms label-free baselines by 4.7-5.9\\% on mathematical reasoning benchmarks. Moreover, self-verification accuracy improves from around 55\\% to over 85\\%, confirming that both capabilities genuinely co-evolve.",
          "submitted": "2026-03-18T14:38:55Z",
          "updated": "2026-03-18T14:38:55Z",
          "comment": "Project Page: https://zju-real.github.io/CoVerRL Code: https://github.com/ZJU-REAL/CoVerRL"
        },
        {
          "id": "http://arxiv.org/abs/2603.17828v1",
          "title": "TINA: Text-Free Inversion Attack for Unlearned Text-to-Image Diffusion Models",
          "abstract": "Although text-to-image diffusion models exhibit remarkable generative power, concept erasure techniques are essential for their safe deployment to prevent the creation of harmful content. This has fostered a dynamic interplay between the development of erasure defenses and the adversarial probes designed to bypass them, and this co-evolution has progressively enhanced the efficacy of erasure methods. However, this adversarial co-evolution has converged on a narrow, text-centric paradigm that equates erasure with severing the text-to-image mapping, ignoring that the underlying visual knowledge related to undesired concepts still persist. To substantiate this claim, we investigate from a visual perspective, leveraging DDIM inversion to probe whether a generative pathway for the erased concept can still be found. However, identifying such a visual generative pathway is challenging because standard text-guided DDIM inversion is actively resisted by text-centric defenses within the erased model. To address this, we introduce TINA, a novel Text-free INversion Attack, which enforces this visual-only probe by operating under a null-text condition, thereby avoiding existing text-centric defenses. Moreover, TINA integrates an optimization procedure to overcome the accumulating approximation errors that arise when standard inversion operates without its usual textual guidance. Our experiments demonstrate that TINA regenerates erased concepts from models treated with state-of-the-art unlearning. The success of TINA proves that current methods merely obscure concepts, highlighting an urgent need for paradigms that operate directly on internal visual knowledge.",
          "submitted": "2026-03-18T15:25:03Z",
          "updated": "2026-03-18T15:25:03Z",
          "comment": "16 pages, accepted by CVPR 2026"
        },
        {
          "id": "http://arxiv.org/abs/2603.17117v1",
          "title": "MosaicMem: Hybrid Spatial Memory for Controllable Video World Models",
          "abstract": "Video diffusion models are moving beyond short, plausible clips toward world simulators that must remain consistent under camera motion, revisits, and intervention. Yet spatial memory remains a key bottleneck: explicit 3D structures can improve reprojection-based consistency but struggle to depict moving objects, while implicit memory often produces inaccurate camera motion even with correct poses. We propose Mosaic Memory (MosaicMem), a hybrid spatial memory that lifts patches into 3D for reliable localization and targeted retrieval, while exploiting the model's native conditioning to preserve prompt-following generation. MosaicMem composes spatially aligned patches in the queried view via a patch-and-compose interface, preserving what should persist while allowing the model to inpaint what should evolve. With PRoPE camera conditioning and two new memory alignment methods, experiments show improved pose adherence compared to implicit memory and stronger dynamic modeling than explicit baselines. MosaicMem further enables minute-level navigation, memory-based scene editing, and autoregressive rollout.",
          "submitted": "2026-03-17T20:19:44Z",
          "updated": "2026-03-17T20:19:44Z",
          "comment": "Project Page: https://mosaicmem.github.io/mosaicmem/"
        },
        {
          "id": "http://arxiv.org/abs/2603.17476v1",
          "title": "UniSAFE: A Comprehensive Benchmark for Safety Evaluation of Unified Multimodal Models",
          "abstract": "Unified Multimodal Models (UMMs) offer powerful cross-modality capabilities but introduce new safety risks not observed in single-task models. Despite their emergence, existing safety benchmarks remain fragmented across tasks and modalities, limiting the comprehensive evaluation of complex system-level vulnerabilities. To address this gap, we introduce UniSAFE, the first comprehensive benchmark for system-level safety evaluation of UMMs across 7 I/O modality combinations, spanning conventional tasks and novel multimodal-context image generation settings. UniSAFE is built with a shared-target design that projects common risk scenarios across task-specific I/O configurations, enabling controlled cross-task comparisons of safety failures. Comprising 6,802 curated instances, we use UniSAFE to evaluate 15 state-of-the-art UMMs, both proprietary and open-source. Our results reveal critical vulnerabilities across current UMMs, including elevated safety violations in multi-image composition and multi-turn settings, with image-output tasks consistently more vulnerable than text-output tasks. These findings highlight the need for stronger system-level safety alignment for UMMs. Our code and data are publicly available at https://github.com/segyulee/UniSAFE",
          "submitted": "2026-03-18T08:30:31Z",
          "updated": "2026-03-18T08:30:31Z",
          "comment": "Equal contribution by first three authors, 55 pages"
        },
        {
          "id": "http://arxiv.org/abs/2603.17639v1",
          "title": "VeriGrey: Greybox Agent Validation",
          "abstract": "Agentic AI has been a topic of great interest recently. A Large Language Model (LLM) agent involves one or more LLMs in the back-end. In the front end, it conducts autonomous decision-making by combining the LLM outputs with results obtained by invoking several external tools. The autonomous interactions with the external environment introduce critical security risks. In this paper, we present a grey-box approach to explore diverse behaviors and uncover security risks in LLM agents. Our approach VeriGrey uses the sequence of tools invoked as a feedback function to drive the testing process. This helps uncover infrequent but dangerous tool invocations that cause unexpected agent behavior. As mutation operators in the testing process, we mutate prompts to design pernicious injection prompts. This is carefully accomplished by linking the task of the agent to an injection task, so that the injection task becomes a necessary step of completing the agent functionality. Comparing our approach with a black-box baseline on the well-known AgentDojo benchmark, VeriGrey achieves 33% additional efficacy in finding indirect prompt injection vulnerabilities with a GPT-4.1 back-end. We also conduct real-world case studies with the widely used coding agent Gemini CLI, and the well-known OpenClaw personal assistant. VeriGrey finds prompts inducing several attack scenarios that could not be identified by black-box approaches. In OpenClaw, by constructing a conversation agent which employs mutational fuzz testing as needed, VeriGrey is able to discover malicious skill variants from 10 malicious skills (with 10/10= 100% success rate on the Kimi-K2.5 LLM backend, and 9/10= 90% success rate on Opus 4.6 LLM backend). This demonstrates the value of a dynamic approach like VeriGrey to test agents, and to eventually lead to an agent assurance framework.",
          "submitted": "2026-03-18T12:00:54Z",
          "updated": "2026-03-18T12:00:54Z",
          "comment": ""
        },
        {
          "id": "http://arxiv.org/abs/2603.17541v1",
          "title": "Temporal Gains, Spatial Costs: Revisiting Video Fine-Tuning in Multimodal Large Language Models",
          "abstract": "Multimodal large language models (MLLMs) are typically trained in multiple stages, with video-based supervised fine-tuning (Video-SFT) serving as a key step for improving visual understanding. Yet its effect on the fine-grained evolution of visual capabilities, particularly the balance between spatial and temporal understanding, remains poorly understood. In this paper, we systematically study how Video-SFT reshapes visual capabilities in MLLMs. Across architectures, parameter scales, and frame sampling settings, we observe a consistent pattern: Video-SFT reliably improves video performance, but often yields limited gains or even degradation on static image benchmarks. We further show that this trade-off is closely tied to temporal budget: increasing the number of sampled frames generally improves video performance, but does not reliably improve static image performance. Motivated by this finding, we study an instruction-aware Hybrid-Frame strategy that adaptively allocates frame counts and partially mitigates the image-video trade-off. Our results indicate that Video-SFT is not a free lunch for MLLMs, and preserving spatial understanding remains a central challenge in joint image-video training.",
          "submitted": "2026-03-18T09:46:44Z",
          "updated": "2026-03-18T09:46:44Z",
          "comment": ""
        }
      ]
    }
  ]
}
```

