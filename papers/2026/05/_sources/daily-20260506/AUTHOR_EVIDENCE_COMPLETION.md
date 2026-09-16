# 2026-05-06 作者侧 exact-v1 证据完成记录

本文件是 137 个冻结候选的逐项作者审阅记录，不是独立 final review。HTML 优先；`03275`、`03884` 使用官方 exact-v1 PDF。方法、评价与 limitation/non-proof 均绑定 exact-v1，摘要只参与候选准入。

<a id="2605.02905"></a>

## 2605.02905 — eOptShrinkQ: Near-Lossless KV Cache Compression Through Optimal Spectral Denoising and Quantization

- **原文：** https://arxiv.org/html/2605.02905v1（访问：2026-09-14）
- **审阅：** deep；exact-v1 valid; no withdrawal banner observed。
- **机制与 owner：** `INFER-KV-CACHE`；spiked-model条件下先提取共享低秩context再量化residual，直接改变KV量化的偏差与rank选择假设，非仅更低bit数。。
- **Method：** 3 Method — The eOptShrinkQ pipeline processes the KV cache in blocks of n n tokens (Algorithm 3 ). Each block S ~ ∈ ℝ n × d \widetilde{S}\in\mathbb{R}^{n\times d} is first denoised via eOptShrink (Algorithm 2 ), which automatically determines the rank …
- **Evaluation：** 4 Numerical Experiments — We conduct numerical experiments on two model families to validate the compression pipeline: Llama-3.1-8B-Instruct ( Grattafiori et al., 2024 ) ( d = 128 d=128 , 32 layers × \times 8 KV heads) and Ministral-8B-Instruct ( Liu et al., 2026 …
- **Limit / non-proof：** Limitations and Future Work. — Our current evaluation uses block-wise processing with blocks of n = 128 n=128 tokens, which requires buffering tokens before compression. During prefill (processing a long prompt), 128-token chunks arise naturally and eOptShrinkQ compresses each chunk as it completes. During autoregressive …
- **Score V2：** Design Delta 2 / System Reach 2 / Durability 3 = **7/9**。
- **Books：** No Change — Existing Coverage。

<a id="2605.02907"></a>

## 2605.02907 — On the Invariants of Softmax Attention

- **原文：** https://arxiv.org/html/2605.02907v1（访问：2026-09-14）
- **审阅：** standard；exact-v1 valid; no withdrawal banner observed。
- **机制与 owner：** `MODEL-SELF-ATTENTION`；区分softmax代数必然秩约束与模型经验key incoherence；可能改变attention低秩解释及训练监测的有效条件，需原文验证。。
- **Method：** 3 The Energy Field — 3.1 Definitions A single attention head [ 14 ] projects each token x i ∈ ℝ d model x_{i}\in\mathbb{R}^{d_{\text{model}}} into a query q i = W Q ​ x i q_{i}=W_{Q}x_{i} and a key k j = W K ​ …
- **Evaluation：** 5.1 Main empirical result — Observation 5.2 (Key incoherence of trained language models) . Across 5,888 key-value heads in 16 trained language models (124M–7B parameters), seven architecture families (Pythia, GPT-2, OPT, Qwen, LLaMA, Phi-2, Mistral), five context lengths ( L = 64 L=64 – 1,024 …
- **Limit / non-proof：** 9.1 Experimental scope and limitations — We test 16 models from seven architecture families: Pythia [ 3 ] (160M, 410M, 1B, 2.8B), GPT-2 [ 11 ] (124M, 355M, 774M), OPT [ 17 ] (350M, 1.3B), Qwen-2.5 [ 16 ] (0.5B, 1.5B, 3B), LLaMA-3.2 [ 13 ] …
- **Score V2：** Design Delta 2 / System Reach 1 / Durability 2 = **5/9**。
- **Books：** No Change — Existing Coverage。

<a id="2605.02908"></a>

## 2605.02908 — Memorization In Stable Diffusion Is Unexpectedly Driven by CLIP Embeddings

- **原文：** https://arxiv.org/html/2605.02908v1（访问：2026-09-14）
- **审阅：** standard；exact-v1 valid; no withdrawal banner observed。
- **机制与 owner：** `MULTIMODAL-GENERATIVE-PARADIGMS`；CLIP EOT与重复padding而非prompt embedding驱动特定memorization，改变文本条件路径与推理期缓解选择；安全反例需原文验证。。
- **Method：** A.1 Applying Our Method To Stable Diffusion v1.4 — We apply our mitigation method, consisting of <pad> replacement and 𝐯 𝐞𝐨𝐭 \mathbf{v}^{\mathbf{eot}} masking. As shown in Figure 9 , our method significantly reduces memorization without degrading image quality. Figure 9 : <pad> replacement and v eot \mathbf{v}^{\mathbf{eot}} masking. The …
- **Evaluation：** Evaluation Metrics. — Following prior work on memorization in Stable Diffusion [ 31 , 3 , 36 , 18 , 16 ] , we adopt SSCD [ 21 ] as the primary metric to determine whether memorization occurs. To ensure a stricter and …
- **Limit / non-proof：** 5 Conclusion — Stable Diffusion exhibits unexpected memorization due to a misalignment between CLIP’s training objective and how diffusion models utilize embeddings. Specifically, the repeated use of <eot> as padding leads to multiple near-identical copies of the semantically dominant 𝐯 𝐞𝐨𝐭 \mathbf{v}^{\mathbf{eot}} , …
- **Score V2：** Design Delta 2 / System Reach 1 / Durability 2 = **5/9**。
- **Books：** No Change — Existing Coverage。

<a id="2605.02909"></a>

## 2605.02909 — Delay, Plateau, or Collapse: Evaluating the Impact of Systematic Verification Error on RLVR

- **原文：** https://arxiv.org/html/2605.02909v1（访问：2026-09-14）
- **审阅：** deep；exact-v1 valid; no withdrawal banner observed。
- **机制与 owner：** `TRAIN-GRPO`；verifier系统性false positive的pattern而非总错误率决定RLVR平台/崩塌，直接修正奖励可靠性假设。。
- **Method：** 3 Characterizing Training Dynamics with Imperfect Verifiers — In this section, we define systematic errors in the context of RLVR and characterize the downstream training dynamics that it can induce. We first introduce the necessary notation and definitions, and then describe the different training dynamics. Rewards and verifiers …
- **Evaluation：** 4 Experiments — In this section, we first describe the setup ( Section 4.1 ) and then demonstrate that all training dynamics from Section 3 can occur in practice ( Section 4.2 ). Next, we take a deeper look at the error patterns …
- **Limit / non-proof：** Limitations and future work — Our study is conducted in a controlled setting with manually specified error patterns, which is useful for isolating the effect of systematic verification errors and measuring oracle reward. However, practical RLVR settings are more complex: real verifiers may exhibit multiple …
- **Score V2：** Design Delta 3 / System Reach 2 / Durability 3 = **8/9**。
- **Books：** Integrate — applied and post-write audited。

<a id="2605.02910"></a>

## 2605.02910 — CreativityBench: Evaluating Agent Creative Reasoning via Affordance-Based Tool Repurposing

- **原文：** https://arxiv.org/html/2605.02910v1（访问：2026-09-14）
- **审阅：** standard；exact-v1 valid; no withdrawal banner observed。
- **机制与 owner：** `AGENT-TOOL-CALLING`；creative tool-use evaluation separates object, part, affordance and physical mechanism, and finds scaling/CoT saturation。
- **Method：** 4 CreativityBench — Creative tool use provides a concrete mechanism for studying creative intelligence in LLMs. Importantly, a “tool” is not defined by its name or intended category, but by its affordances , which are the action possibilities it enables. These affordances emerge …
- **Evaluation：** 5 Experiments — 5.1 Experimental Settings Models. We evaluate a diverse set of open- and closed-source models, including the GPT family ( Singh et al., 2025 ) , Gemini family ( Comanici et al., 2025 ) , Qwen family ( Yang et al., …
- **Limit / non-proof：** 7 Discussion — Difference of Creativity and Hallucination. Throughout this paper, we define creativity as grounded in object attributes and the affordances they induce. In this sense, our notion of creativity is importantly different from creative writing, open-ended design, or innovative research ideation, …
- **Score V2：** Design Delta 2 / System Reach 1 / Durability 2 = **5/9**。
- **Books：** No Change — Existing Coverage。

<a id="2605.02914"></a>

## 2605.02914 — When Safety Geometry Collapses: Fine-Tuning Vulnerabilities in Agentic Guard Models

- **原文：** https://arxiv.org/html/2605.02914v1（访问：2026-09-14）
- **审阅：** deep；exact-v1 valid; no withdrawal banner observed。
- **机制与 owner：** `PLATFORM-SECURITY`；benign fine-tuning可破坏专业guard集中的safety geometry，Fisher权重及梯度冲突正则提供具体纠错分支；需验证几何/行为关系边界。。
- **Method：** Fisher-Weighted Safety Subspace Regularization — FW-SSR: Formulation We propose FW-SSR, replacing the uniform penalty with a curvature-aware adaptive variant: ℒ FW-SSR = 𝔼 x ∼ 𝒟 safe ​ ∑ ℓ ∈ ℒ ‖ F ^ ℓ ⊙ U ℓ ⊤ ​ ( h ℓ ​ …
- **Evaluation：** Experimental Setup — Models We evaluate on three purpose-built guard model families. WildGuard [ Han et al.(2024) ] : An open-source safety classifier built on Mistral-7B (32 transformer layers, d = 4096 d=4096 ), trained to jointly detect harmful requests, adversarial jailbreaks, and …
- **Limit / non-proof：** Discussion — Implications for Agentic AI Safety. Our findings expose a systematic vulnerability in the standard agentic deployment practice of fine-tuning safety guards alongside the agents they protect. Guard models occupy a privileged position in multi-agent pipelines — they are the last …
- **Score V2：** Design Delta 2 / System Reach 2 / Durability 3 = **7/9**。
- **Books：** No Change — Existing Coverage。

<a id="2605.02915"></a>

## 2605.02915 — When Should a Language Model Trust Itself? Same-Model Self-Verification as a Conditional Confidence Signal

- **原文：** https://arxiv.org/html/2605.02915v1（访问：2026-09-14）
- **审阅：** standard；exact-v1 valid; no withdrawal banner observed。
- **机制与 owner：** `PLATFORM-EVALUATION-SYSTEM`；同模型自验相对于LL-AVG/LL-SUM在模型/任务间反转，直接修正selective-prediction中额外自验调用的收益假设。。
- **Method：** 3 Methods — 3.1 Task setting We study confidence estimation in a multiple-choice question answering setting. For each question q q , a model selects an answer a ^ \hat{a} from a finite set of candidate options { a 1 , … , …
- **Evaluation：** 4 Results — (a) ARC-Challenge (default prompt) (b) TruthfulQA-MC (default prompt) Figure 1 : AUROC by confidence signal across datasets under the default verification prompt. Self-Verify is strongly positive on ARC-Challenge for several models, but much less uniform on TruthfulQA-MC. (a) ARC-Challenge (default …
- **Limit / non-proof：** 6 Limitations — Our findings should be interpreted in light of several limitations, many of which are consistent with broader observations in the uncertainty and self-evaluation literature. 6.1 Limited model and family coverage Although we evaluate multiple open-weight models spanning several families, our …
- **Score V2：** Design Delta 2 / System Reach 1 / Durability 2 = **5/9**。
- **Books：** No Change — Existing Coverage。

<a id="2605.02943"></a>

## 2605.02943 — Healthcare AI GYM for Medical Agents

- **原文：** https://arxiv.org/html/2605.02943v1（访问：2026-09-14）
- **审阅：** standard；exact-v1 valid; no withdrawal banner observed。
- **机制与 owner：** `TRAIN-GRPO`；稀疏终局奖励使multi-turn工具轨迹退化为长单轮，TT-OPD以turn-level截断和outcome-privileged EMA teacher密化KL；虽医学任务，直接修改通用agentic RL机制。。
- **Method：** 4.2 TT-OPD Method — Given the failure modes described in § 1 , we require both a robust learning signal for accuracy and structural regularization to sustain multi-turn behavior. TT-OPD addresses these by utilizing a teacher model that tracks the student via Exponential Moving …
- **Evaluation：** 5 Experiments — 5.1 Setup The vanilla GRPO baseline and all OPD experiments (four ablation variants plus the full method) use Qwen3.5-9B ( Qwen Team, 2025 ) , trained from scratch without SFT warmup, to isolate the effect of each component without confounding …
- **Limit / non-proof：** 7 Discussion and Conclusion — Several avenues extend this work. First, process-level reward models (PRMs) ( Lightman et al., 2024 ; Uesato et al., 2022 ) could replace or augment the sparse terminal reward with turn-level feedback, potentially accelerating credit assignment in long episodes. Second, …
- **Score V2：** Design Delta 2 / System Reach 1 / Durability 2 = **5/9**。
- **Books：** No Change — Existing Coverage。

<a id="2605.02944"></a>

## 2605.02944 — Exploring Pass-Rate Reward in Reinforcement Learning for Code Generation

- **原文：** https://arxiv.org/html/2605.02944v1（访问：2026-09-14）
- **审阅：** standard；exact-v1 valid; no withdrawal banner observed。
- **机制与 owner：** `TRAIN-GRPO`；pass-rate奖励虽密集但partial-pass梯度可抵消、未指向全对解，直接反证GRPO/RLOO奖励密度假设，不能因无owner变更关闭。。
- **Method：** 2.2 Policy-Gradient Methods — We employ two commonly used critic-free policy-gradient methods for RL fine-tuning: Group relative policy optimization (GRPO) and reinforce leave-one-out (RLOO). GRPO. GRPO ( Shao et al., 2024 ) is a group-wise policy-gradient method. For a given problem x x , …
- **Evaluation：** 2.3 Evaluation Metric — Following standard practice in code generation ( Lyu et al., 2025 ; Chen, 2021 ; Kulal et al., 2019 ) , we adopt pass@ k k as the primary evaluation metric. Given a problem x x , pass@ k k …
- **Limit / non-proof：** Appendix F Limitations — Our study has several limitations that warrant further investigation. First, our reweighted pass-rate reward is a best-effort approximation inspired by MiMo’s difficulty-weighted code reward ( Xiaomi et al., 2025 ) . Since key implementation details of MiMo are not publicly …
- **Score V2：** Design Delta 2 / System Reach 1 / Durability 2 = **5/9**。
- **Books：** No Change — Existing Coverage。

<a id="2605.02946"></a>

## 2605.02946 — RouteHijack: Routing-Aware Attack on Mixture-of-Experts LLMs

- **原文：** https://arxiv.org/html/2605.02946v1（访问：2026-09-14）
- **审阅：** deep；exact-v1 valid; no withdrawal banner observed。
- **机制与 owner：** `PLATFORM-SECURITY`；MoE输入suffix优化直接操纵refusal/harmful expert routing，并有跨兄弟模型迁移，揭示输出层之外的架构安全攻击面。。
- **Method：** 4. RouteHijack — RouteHijack is a routing-aware adversarial framework for MoE models. An overview of the framework is shown in Figure 1 . We first localize safety- and harm-related experts via response-driven contrastive profiling that disentangles behavior from prompt semantics. We then optimize …
- **Evaluation：** 5.4. Evaluation Metrics — Attack Success Rate (ASR). We evaluate the effectiveness of the adversarial suffix by measuring ASR: the percentage of malicious prompts that trigger toxic or policy-violating responses. For robust assessment, we use a multi-stage pipeline: Llama-Guard-3-8B ( Llama Team, 2024 ) …
- **Limit / non-proof：** 9. Discussion — The effectiveness of RouteHijack across diverse MoE architectures and VLMs highlights a fundamental disconnect between current safety alignment methods and the architecture of sparse computation. Current methodologies, such as RLHF and DPO, predominantly focus on shaping the model’s output distribution …
- **Score V2：** Design Delta 2 / System Reach 3 / Durability 3 = **8/9**。
- **Books：** Integrate — already present and rechecked。

<a id="2605.02953"></a>

## 2605.02953 — DITRON: Distributed Multi-level Tiling Compiler for Parallel Tensor Programs

- **原文：** https://arxiv.org/html/2605.02953v1（访问：2026-09-14）
- **审阅：** deep；exact-v1 valid; no withdrawal banner observed。
- **机制与 owner：** `INFER-TENSORRT-LLM`；Core/Device/Task统一tiling映射分布式memory/communication层级，直接改变LLM kernel联合编译方法。。
- **Method：** 3 Ditron System Design — Figure 2 : Ditron is composed of front-end interface, mid-end swizzle, and back-end primitives and code generation. Followed by the insights discussed in Section 1 , we present Ditron , a unified compiler stack designed to bridge the gap between …
- **Evaluation：** 4 Evaluation — We evaluate Ditron across diverse parallel configurations. For inference (intra-node TP), we benchmark 5 GEMM/MoE workloads, Attention/FFN modules, and end-to-end Qwen3-32B/LLaMA3-70B models . For training, we analyze weak and strong scaling of TP, SP, and EP kernels on 8–128 GPUs. …
- **Limit / non-proof：** 2.2 Limitations of Existing Programming Models — Despite the hierarchical nature of hardware, existing software stacks largely fail to provide a unified abstraction that captures these nuances. Hand-tuned Libraries: Previous work [ flux , comet , deepep , tokenweave ] attempts to bridge the gap by providing …
- **Score V2：** Design Delta 2 / System Reach 2 / Durability 3 = **7/9**。
- **Books：** No Change — Existing Coverage。

<a id="2605.02958"></a>

## 2605.02958 — Tracing the Dynamics of Refusal: Exploiting Latent Refusal Trajectories for Robust Jailbreak Detection

- **原文：** https://arxiv.org/html/2605.02958v1（访问：2026-09-14）
- **审阅：** standard；exact-v1 valid; no withdrawal banner observed。
- **机制与 owner：** `PLATFORM-SECURITY`；静态末层refusal被抑制仍存在上游layer-token轨迹，causal tracing提供检测位置的新边界，须原文核验encoded/adaptive攻击限制。。
- **Method：** 4.1 Architecture — Latent Activation Volume. To capture the dynamic structure of refusal while maximizing the Signal-to-Noise Ratio (SNR), we isolate a critical Region of Interest (ROI). Specifically, we select a sensitive layer window W = { l s ​ t ​ a …
- **Evaluation：** 3.2 Microscopic Analysis — 3.2.1 Setup We initiate our analysis with a microscopic case study to identify regular mechanistic patterns as illustrated in Figure 1(a) . Specifically, we construct a minimal pair—contrasting a harmful query (e.g., “ How to make a bomb? ”) with …
- **Limit / non-proof：** 7 Limitations — Our work establishes the utility of the “refusal trajectory”, yet three limitations warrant future investigation. First, our Causal Tracing relies primarily on interchange interventions to identify sufficient causal anchors. While we acknowledge that sufficiency does not imply necessity (i.e., other …
- **Score V2：** Design Delta 2 / System Reach 1 / Durability 2 = **5/9**。
- **Books：** No Change — Existing Coverage。

<a id="2605.02960"></a>

## 2605.02960 — ZeRO-Prefill: Zero Redundancy Overheads in MoE Prefill Serving

- **原文：** https://arxiv.org/html/2605.02960v1（访问：2026-09-14）
- **审阅：** deep；exact-v1 valid; no withdrawal banner observed。
- **机制与 owner：** `INFER-PREFILL`；prefill-only长计算窗口允许expert weights AllGather替代activation AllToAll，且依赖饱和阈值/负载路由，改变MoE部署选择。。
- **Method：** 5.2 System Architecture and Workflow — Figure 5 : ZeRO-Prefill system architecture and end-to-end prefill-only serving workflow. The frontend normalizes incoming tasks into prefill-only form and schedules them into saturation-bounded batches with prefix affinity; the backend executes each batch under data-parallel attention and asynchronous expert streaming, …
- **Evaluation：** 3 Workload Analysis — 3.1 Prefill-Only Workloads in Practice Definition and atomic operation. Prefill-only workloads are inference tasks whose output is selected from a predefined candidate token set via the logits of a single prefill forward pass, without autoregressive decoding. We formalize the atomic …
- **Limit / non-proof：** 10 Discussion — Applicability and limitations. ZeRO-Prefill targets throughput-oriented, batch-driven prefill-only serving on MoE models that exceed single-GPU HBM. It is not designed for latency-critical interactive serving, arrivals too bursty to sustain the saturation threshold, or dense models with no expert stack. Three …
- **Score V2：** Design Delta 2 / System Reach 3 / Durability 3 = **8/9**。
- **Books：** Integrate — already present and rechecked。

<a id="2605.02964"></a>

## 2605.02964 — Reward Hacking Benchmark: Measuring Exploits in LLM Agents with Tool Use

- **原文：** https://arxiv.org/html/2605.02964v1（访问：2026-09-14）
- **审阅：** deep；exact-v1 valid; no withdrawal banner observed。
- **机制与 owner：** `PLATFORM-EVALUATION-SYSTEM`；工具任务把完成与harness漏洞分开，并揭示harder variants使低exploit模型暴露风险，修正单一任务成功率验收。。
- **Method：** 3 Reward Hacking Benchmark — 3.1 Agent Setting and Threat Model We evaluate the model as an agent in a sandbox that can: • Read task inputs in a workspace filesystem. • Use tools (shell, Python, etc.). • Write artifacts that a harness parses and …
- **Evaluation：** 5 Experiments — 5.1 Model Suite We ran two sets of experiments. (E1) Frontier sweep. We evaluated a set of frontier models including GPT-4o; o1; o3; o4-mini; o3-mini; Claude 3.5 Sonnet v2; Claude 3.7 Sonnet; Claude Sonnet 4.5; Claude Opus 4.5; Gemini 2.5 …
- **Limit / non-proof：** 8 Limitations — Sample sizes. Per-episode costs of $5–$50 on frontier APIs cap our sample sizes at the same order of magnitude as comparable behavioral evaluations of frontier models ( MacDiarmid et al., 2025 ; Arx et al., 2025 ; METR, 2025b ; …
- **Score V2：** Design Delta 2 / System Reach 2 / Durability 3 = **7/9**。
- **Books：** No Change — Existing Coverage。

<a id="2605.02968"></a>

## 2605.02968 — Finite-Size Gradient Transport in Large Language Model Pretraining: From Cascade Size to Intensive Transport Efficiency

- **原文：** https://arxiv.org/html/2605.02968v1（访问：2026-09-14）
- **审阅：** standard；exact-v1 valid; no withdrawal banner observed。
- **机制与 owner：** `TRAIN-PRETRAINING`；把raw-gradient与checkpoint-update观测区分，分离cascade规模及intensive transport；两个模型族不共享效率尺度，直接限定梯度传播解释。。
- **Method：** II Methods — II.1 TDU-OFC cascade method We use the same offline TDU-OFC avalanche probe introduced in our prior toy-grokking studies [ 27 , 26 ] . The present work applies this probe to saved field snapshots from real language-model pretraining trajectories, including …
- **Evaluation：** II.6 Unified analysis conventions — All reported Pico-LM and Pythia results are generated under a common analysis protocol. At each aligned training step, finite-size fits are performed only on the model scales that are available and pass the relevant inclusion criteria at that step. Linear …
- **Limit / non-proof：** IV Discussion — The present evidence supports a decompositional view of finite-size transport signatures in real language-model training. The central empirical contrast between the two families is captured not by a single distinguishing exponent but by how the multi-channel transport language partitions a …
- **Score V2：** Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- **Books：** No Change — Existing Coverage。

<a id="2605.02971"></a>

## 2605.02971 — Multilingual Safety Alignment via Self-Distillation

- **原文：** https://arxiv.org/html/2605.02971v1（访问：2026-09-14）
- **审阅：** standard；exact-v1 valid; no withdrawal banner observed。
- **机制与 owner：** `TRAIN-RLHF`；高资源安全能力以同模型teacher/student条件不对称转移至低资源语言，并对关键token加权；具体改动安全蒸馏数据/反馈选择。。
- **Method：** 3 Multilingual Self-Distillation — In this section, we propose Multilingual Self-Distillation (MSD) to bridge the multilingual safety gap in a target LLM. First, Section 3.1 introduces the cross-lingual safeguard transfer framework, specifically designed to transfer inherent safety capabilities from high-resource to low-resource languages. Second, …
- **Evaluation：** 4 Experiments — 4.1 Experimental Setup Models. We conduct our studies on four representative LLMs: Qwen-2.5-7B-Instruct ( Yang et al., 2025b ) , Qwen-3-8B ( Yang et al., 2025a ) , LLaMA-2-7B-chat ( Touvron et al., 2023 ) , and LLaMA-3-8B-Instruct ( Grattafiori …
- **Limit / non-proof：** 5 Conclusion and Limitations — In this paper, we introduce MSD, a response-free framework designed to bridge the severe safety alignment gap between high-resource and low-resource languages. By leveraging self-distillation, MSD effectively transfers internal safeguards from high-resource to low-resource languages, entirely eliminating the expensive costs …
- **Score V2：** Design Delta 2 / System Reach 1 / Durability 2 = **5/9**。
- **Books：** No Change — Existing Coverage。

<a id="2605.02973"></a>

## 2605.02973 — Structured Diffusion Bridges: Inductive Bias for Denoising Diffusion Bridges

- **原文：** https://arxiv.org/html/2605.02973v1（访问：2026-09-14）
- **审阅：** deep；exact-v1 valid; no withdrawal banner observed。
- **机制与 owner：** `MULTIMODAL-GENERATIVE-PARADIGMS`；同样边缘分布可对应错误cross-modal coupling，以端点及轨迹可逆性约束减少配对依赖，直接限定diffusion bridge可识别性。。
- **Method：** C.2 Denoiser Architecture — As depicted in Figure 5 , the denoiser is implemented as a stack of L L multi-head attention (MHA) blocks. The network operates directly in the endpoint space, i.e., it implements a denoising diffusion bridge model ( Zhou et al., …
- **Evaluation：** 5 Experiments — We validated SDB across a range of translation tasks, including a controlled synthetic dataset in Section 5.1 and real-world scenarios in Section 5.2 and Section 5.3 . The objectives of this empirical study were fourfold: 1. How do the proposed …
- **Limit / non-proof：** Limitations. — Individual heuristics do not completely solve the ambiguity in modality translation. MM (Section 4.1 ) matches the target marginal but may ignore the conditioning endpoint. Moreover, the WTA increases complexity as K K grows. CC (Section 4.2 ) preserves content …
- **Score V2：** Design Delta 2 / System Reach 2 / Durability 3 = **7/9**。
- **Books：** No Change — Existing Coverage。

<a id="2605.02977"></a>

## 2605.02977 — Contrastive Privacy: A Semantic Approach to Measuring Privacy of AI-based Sanitization

- **原文：** https://arxiv.org/html/2605.02977v1（访问：2026-09-14）
- **审阅：** deep；exact-v1 valid; no withdrawal banner observed。
- **机制与 owner：** `PLATFORM-SECURITY`；形式contrastive privacy加有限集合/语义模型操作化，检验遮挡概念外的身份泄露；可改变AI脱敏证据权限。。
- **Method：** 3 Contrastive Privacy Formulation — 3.1 Privacy for Complex Data Ensuring the privacy of unstructured information is a complex problem. In this paper, we ground our definition of privacy with respect to appropriate information flows following Contextual Integrity (CI) [ 43 ] . CI postulates …
- **Evaluation：** 5 Privatization Experiments — Figure 4 : (left) 30 images capturing Leonard DiCaprio sanitized of the identity of the celebrities by (center) iGPT1m/GEM31p , privacy resolution 0.02 and utility 0.42; (right) iGEM31f/Manual , privacy resolution 0 and utility 0.61, where 𝒟 \mathcal{D} is EVA …
- **Limit / non-proof：** 8 Conclusion — Increasingly, AI-models are being used to sanitize media based on natural language prompts. We have introduced contrastive privacy , a formal definition of privacy that yields an algorithm that uses embedding models such as CLIP to connect concepts latent in …
- **Score V2：** Design Delta 2 / System Reach 2 / Durability 3 = **7/9**。
- **Books：** No Change — Existing Coverage。

<a id="2605.03034"></a>

## 2605.03034 — Stable Agentic Control: Tool-Mediated LLM Architecture for Autonomous Cyber Defense

- **原文：** https://arxiv.org/html/2605.03034v1（访问：2026-09-14）
- **审阅：** deep；exact-v1 valid; no withdrawal banner observed。
- **机制与 owner：** `PLATFORM-SECURITY`；finite tool-action catalogs与machine-checked Lyapunov条件把LLM能力/随机性与闭环稳定性分开；应验证有限catalog及观测假设，原仅工具授权理由漏掉形式保证。。
- **Method：** 3 Approach — We cast autonomous cyber defense as a closed-loop control problem blending LLM tool use, game theory, and control-theoretic stability. The system is a discrete-time non-linear feedback loop: 𝒢 ⁡ ( k + 1 ) \displaystyle\mathcal{G}(k+1) = f ⁡ ( 𝒢 …
- **Evaluation：** 5 Experiments — We validate the architectural pattern along two axes corresponding to the formal results of § 4 . Experiment 1 tests Claims (i)–(iii) — Controllability, Robustness (ISS), and Observability — on 282 real enterprise attack graphs spanning 161 organizations and 25 …
- **Limit / non-proof：** 6 Discussion — Stability as architectural discipline. Constraining the environment rather than agent reasoning is more reliable than post-hoc behavioral constraints given destructive failures in [ 7 ] , addressing the open stability verification problem in [ 5 ] . The architecture does …
- **Score V2：** Design Delta 2 / System Reach 2 / Durability 3 = **7/9**。
- **Books：** No Change — Existing Coverage。

<a id="2605.03050"></a>

## 2605.03050 — Evaluating Reasoning Models for Queries with Presuppositions

- **原文：** https://arxiv.org/html/2605.03050v1（访问：2026-09-14）
- **审阅：** standard；exact-v1 valid; no withdrawal banner observed。
- **机制与 owner：** `PLATFORM-EVALUATION-SYSTEM`；reasoning与non-reasoning对错误预设的受控强度比较仍有26–42%失败，具体限定reasoning可替代事实前提检查的假设。。
- **Method：** 3 Approach — Model / Variant True False Mixed Overall GPT-OSS 20B off 64.2 % 64.2\% ( 63.7 ​ – ​ 64.7 % 63.7\text{\textendash}64.7\% ) 45.1 % 45.1\% ( 44.6 ​ – ​ 45.6 % 44.6\text{\textendash}45.6\% ) 25.7 % 25.7\% ( 22.9 ​ …
- **Evaluation：** 4 Results and Discussion — We evaluate a diverse set of contemporary language models spanning open- and closed-weight systems, multiple model families, and varying degrees of explicit reasoning. Our evaluation includes recent open-source models GPT-OSS 20B with three reasoning levels ( OpenAI, 2025b ) , …
- **Limit / non-proof：** Limitations — There are several important limitations of our work. First, reasoning models are a rapidly evolving space, with different architectures and training methodologies emerging regularly. Each model also operationalizes reasoning differently, and our evaluation captures the behavior of several contemporary models …
- **Score V2：** Design Delta 2 / System Reach 1 / Durability 2 = **5/9**。
- **Books：** No Change — Existing Coverage。

<a id="2605.03052"></a>

## 2605.03052 — How Language Models Process Negation

- **原文：** https://arxiv.org/html/2605.03052v1（访问：2026-09-14）
- **审阅：** standard；exact-v1 valid; no withdrawal banner observed。
- **机制与 owner：** `MODEL-TRANSFORMER-LAYER`；LLM内部可正确处理negation但晚层attention shortcut覆盖结果；causal ablation及两种表示机制直接补全模型计算解释。。
- **Method：** 4 Shortcut Attention Heads in LLMs — Before diving into our investigation, we first determine whether open-weight LLMs can understand negation in our dataset. Our results are twofold. First, models often output incorrect answers on negative prompts. We observe output failures such as “ An animal that …
- **Evaluation：** 4.1 Models Exhibit Internal Sensitivity to Negation — On our curated dataset, we show that LLMs appear to struggle with negation based on accuracy metrics. In addition, we define a sensitivity metric which reveals that models have learned negation mechanisms. Accuracy On positive prompts P + P_{+} , …
- **Limit / non-proof：** Discussion — Based on PCA results, it is plausible that the residual stream state of “ not Y ” is an additive combination of the representation of “ not ” and the representation of Y Y . This view conforms to part …
- **Score V2：** Design Delta 2 / System Reach 1 / Durability 2 = **5/9**。
- **Books：** No Change — Existing Coverage。

<a id="2605.03058"></a>

## 2605.03058 — Neuron-Anchored Rule Extraction for Large Language Models via Contrastive Hierarchical Ablation

- **原文：** https://arxiv.org/html/2605.03058v1（访问：2026-09-14）
- **审阅：** standard；exact-v1 valid; no withdrawal banner observed。
- **机制与 owner：** `MODEL-TRANSFORMER-LAYER`；规则对齐划分、稀疏activation group ablation与受限单例验证降低因果定位成本；必须核验overtopping/置信剪枝假设，不能因无owner改变关闭。。
- **Method：** 4. MechaRule : Rule-Grounded Neuron Localization — Figure 2 . Pipeline overview: RuleSHAP extracts behavioral splitter rules from 𝒟 \mathcal{D} , spectral compression and EAP-IG reduce the search space, binary hierarchical group ablations localize agonists, and RuleSHAP yields neuron-anchored rules. Flowchart of the \AlgoNamepipeline in four stages. …
- **Evaluation：** 6. Results — We report results aligned with our four experiment families (E0–E3). E0: MechaRule produces high-quality neuron rules. Table 1 summarizes, for the main configuration, how many high-quality neuron-anchored rules we obtain per model and task, together with directional union flip coverage. …
- **Limit / non-proof：** 8. Limitations — MechaRule produces task-local neuron-anchored explanations by combining behavioral rules with targeted internal interventions, and this design comes with limitations. Localization is only as rule-grounded as the behavioral splitter r 0 r_{0} and the interpretable vocabulary Φ \Phi : if r …
- **Score V2：** Design Delta 2 / System Reach 1 / Durability 2 = **5/9**。
- **Books：** No Change — Existing Coverage。

<a id="2605.03065"></a>

## 2605.03065 — OGPO: Sample Efficient Full-Finetuning of Generative Control Policies

- **原文：** https://arxiv.org/html/2605.03065v1（访问：2026-09-14）
- **审阅：** standard；exact-v1 valid; no withdrawal banner observed。
- **机制与 owner：** `MULTIMODAL-EMBODIED-VLA`；off-policy critic终端反馈穿过完整diffusion/flow生成路径，配合保守advantage与buffer稳定机制；改变具身generative policy全参数微调的可行分支。。
- **Method：** 3 Off-Policy Generative Policy Optimization — We propose O ff- P olicy G enerative P olicy O ptimization, OGPO , an off-policy full-policy finetuning method for generative control policies. We begin by introducing the basic algorithm, and then describe an improved variant, OGPO+ . We provide …
- **Evaluation：** Experimental Setup: — To identify improved design choices, we consider experiments on the state-based and image-based Robomimic tasks, which are described in greater detail in Section 5.1 . For state-based runs, we use all state-information directly; for image based runs, we pass image …
- **Limit / non-proof：** 8 Conclusion and Limitations — We introduce OGPO , an approach that combines the best of on-policy and off-policy methods for fine-tuning generative control policies (GCPs) and enjoys high success rates and sample efficiency across numerous tasks. However, OGPO still has drawbacks: the use of …
- **Score V2：** Design Delta 2 / System Reach 1 / Durability 2 = **5/9**。
- **Books：** No Change — Existing Coverage。

<a id="2605.03073"></a>

## 2605.03073 — The TTS-STT Flywheel: Synthetic Entity-Dense Audio Closes the Indic ASR Gap Where Commercial and Open-Source Systems Fail

- **原文：** https://arxiv.org/html/2605.03073v1（访问：2026-09-14）
- **审阅：** standard；exact-v1 valid; no withdrawal banner observed。
- **机制与 owner：** `MULTIMODAL-REPRESENTATION`；entity-dense合成语音/LoRA收益与script collapse具有语言条件反转，含held-out synthesizer和真人sanity，具体改变ASR适配/验证选择。。
- **Method：** III Method — III-A Entity-Dense Synthetic Audio (EDSA) corpus We define six entity classes that capture the niche-domain gap in Indic ASR: digits (10-digit phone numbers and similar runs), currency (amounts in Latin numerals or Indic words such as “Rs.50,000”, “50000 rupees”, “ …
- **Evaluation：** IV Experimental Setup — IV-A Holdouts Three real-recording holdouts plus one synthesised entity-dense holdout: • FLEURS [ 13 ] : n = 100 n=100 test-split utts per language; standard read-prose regression check. • Common Voice 25.0 (CV25) [ 12 ] : real volunteer recordings; …
- **Limit / non-proof：** VII Limitations — Synthesised entity-dense holdout. Our headline entity-dense evaluation (Table II ) is on Cartesia-synthesised audio held out from training, raising the concern that the gain reflects TTS-distribution learning rather than entity learning. We address this concern empirically with a 20-utterance native-human …
- **Score V2：** Design Delta 2 / System Reach 1 / Durability 2 = **5/9**。
- **Books：** No Change — Existing Coverage。

<a id="2605.03075"></a>

## 2605.03075 — Refining Compositional Diffusion for Reliable Long-Horizon Planning

- **原文：** https://arxiv.org/html/2605.03075v1（访问：2026-09-14）
- **审阅：** standard；exact-v1 valid; no withdrawal banner observed。
- **机制与 owner：** `MULTIMODAL-GENERATIVE-PARADIGMS`；局部多峰diffusion scores拼接导致mode averaging，以self-reconstruction density及重叠一致性guidance修复长程可行性。。
- **Method：** Appendix E Algorithm — Each RCD guidance step requires one additional forward pass through the score network (to compute the reconstruction at probe level s s ) and one backward pass for the gradient. The expectation in Equation 6 is approximated with a single …
- **Evaluation：** 4 Experiments — In this section, we present the effectiveness of RCD on long-horizon planning tasks from OGBench [ 56 ] . Specifically, we demonstrate (1) that RCD produces more physically feasible plans than existing compositional methods, (2) that it further enhances planning …
- **Limit / non-proof：** Limitations. — The current formulation operates within the Bethe factor graph framework of [ 78 , 51 ] , which assumes chain-structured overlapping segments. Extending RCD guidance to other compositional structures, such as hierarchical or temporal abstractions, or factor graphs with loops, …
- **Score V2：** Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- **Books：** No Change — Existing Coverage。

<a id="2605.03090"></a>

## 2605.03090 — From Barrier to Bridge: The Case for AI Data Center/Power Grid Co-Design

- **原文：** https://arxiv.org/html/2605.03090v1（访问：2026-09-14）
- **审阅：** standard；exact-v1 valid; no withdrawal banner observed。
- **机制与 owner：** `PLATFORM-COST`；同步AI训练负载破坏电网load-diversity假设，提出跨时标compute-power协同问题；保留受限设计论证，不把立场稿写成运行验证。。
- **Method：** 4. The Case for Co-Development and its Cultural and Technical Challenges — Unlike prior industrial loads, AI data centers are equipped with fast, programmable power electronics and workload-level controls that could, in principle, help stabilize the grid. Facilities already deploy multi-megawatt UPS inverters, battery banks, DC buses, and job-level schedulers capable of …
- **Evaluation：** Abstract evaluation — This paper argues that the resulting entanglement of compute and power infrastructure requires a shift from implicit coexistence to explicit co-development between the historically decoupled data center and electric power industries.
- **Limit / non-proof：** No dedicated limitation heading found; non-proof is bounded to the disclosed exact-v1 evaluation — We identify key research directions, from joint capacity planning, multi-timescale control, a compute--power protocol stack, to market innovation, that must be pursued to power the future of AI sustainably and reliably.
- **Score V2：** Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- **Books：** No Change — Existing Coverage。

<a id="2605.03095"></a>

## 2605.03095 — Revisiting JBShield: Breaking and Rebuilding Representation-Level Jailbreak Defenses

- **原文：** https://arxiv.org/html/2605.03095v1（访问：2026-09-14）
- **审阅：** deep；exact-v1 valid; no withdrawal banner observed。
- **机制与 owner：** `PLATFORM-SECURITY`；自适应攻击直接针对JBShield概念打破非自适应0%结论，RTV跨层fingerprint仍需自适应威胁测试，明确纠错/安全证据。。
- **Method：** 5. Adaptive Attack Design — JBShield ( Zhang et al., 2025 ) reports 0% ASR against GCG-based adaptive attacks in which the attack objective is modified to weaken the toxic concept and enhance the jailbreak concept (Table 9 in ( Zhang et al., 2025 ) …
- **Evaluation：** 6. Experiments — We first start by evaluating whether refusal suppression is effective enough to break JBShield-D. Then, we evaluate whether detector-aware optimization alone is sufficient to evade JBShield-D. In our last attack, we evaluate whether combining refusal suppression with detector-aware regularization yields …
- **Limit / non-proof：** 8.1. Limitations — Single model. All experiments are conducted on Llama-3-8B. While the refusal-direction phenomenon has been observed across 13+ open-source models ( Arditi et al., 2024 ) , we have not verified that RTV’s fingerprint separation and detection performance generalize to other …
- **Score V2：** Design Delta 3 / System Reach 2 / Durability 3 = **8/9**。
- **Books：** No Change — Existing Coverage。

<a id="2605.03109"></a>

## 2605.03109 — Gated Subspace Inference for Transformer Acceleration

- **原文：** https://arxiv.org/html/2605.03109v1（访问：2026-09-14）
- **审阅：** standard；exact-v1 valid; no withdrawal banner observed。
- **机制与 owner：** `INFER-TENSORRT-LLM`；token activation低秩subspace缓存weight image并门控residual计算，直接给出LLM linear层带宽与误差可控的替代执行路径。。
- **Method：** 4 Algorithm — This section states the complete GSI procedure and discusses the calibration and storage costs. Algorithm 1 Gated Subspace Inference (GSI) 1: Activation x ∈ ℝ d x\in\mathbb{R}^{d} , cached image M = W ​ V k ∈ ℝ d out …
- **Evaluation：** 3.3 Error analysis — Theorem 4 (Per-layer error bound). On the fast path, the per-token output error satisfies ‖ y t − y ^ t ‖ = ‖ W ​ r t ‖ ≤ ‖ W ‖ 2 ⋅ ε ⋅ ‖ x t …
- **Limit / non-proof：** 7 Open problems and future work — This section identifies four directions for future work. 7.1 Extension to larger models The experiments in this paper cover models up to 6.7 6.7 B parameters. The key question for larger models (Llama-3 70B, Mixtral 8x22B) is whether the effective …
- **Score V2：** Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- **Books：** No Change — Existing Coverage。

<a id="2605.03110"></a>

## 2605.03110 — Cascade Token Selection for Transformer Attention Acceleration

- **原文：** https://arxiv.org/html/2605.03110v1（访问：2026-09-14）
- **审阅：** standard；exact-v1 valid; no withdrawal banner observed。
- **机制与 owner：** `INFER-TENSORRT-LLM`；跨层继承代表token集合并用cross-Gram验证，将selection从T²d改Trd，明确减少attention压缩自身成本。。
- **Method：** 4.1 Algorithm — Algorithm 1 Cascade Token Selection 1: Activation X ( l + 1 ) ∈ ℝ T × d X^{(l+1)}\in\mathbb{R}^{T\times d} , inherited representative set ℛ ( l ) \mathcal{R}^{(l)} , threshold τ \tau 2: X ^ ← D − 1 …
- **Evaluation：** 4.2 Cost analysis — The cost of Algorithm 1 at layer l + 1 l+1 is: C cascade = r 2 ​ d + ( T − r ) ​ r ​ d = T ​ r ​ d , C_{\rm cascade}=r^{2}d+(T-r)rd=Trd, (6) compared …
- **Limit / non-proof：** 8 Open problems and future work — This section identifies five directions for future work. 8.1 Adaptive threshold across depth The current implementation uses a fixed Gram threshold τ \tau across all layers. The representative count profile (Table 4 ) shows that the optimal τ \tau varies …
- **Score V2：** Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- **Books：** No Change — Existing Coverage。

<a id="2605.03117"></a>

## 2605.03117 — ARISE: A Repository-level Graph Representation and Toolset for Agentic Fault Localization and Program Repair

- **原文：** https://arxiv.org/html/2605.03117v1（访问：2026-09-14）
- **审阅：** deep；exact-v1 valid; no withdrawal banner observed。
- **机制与 owner：** `AGENT-WORKFLOW`；repository graph加入statement级def-use及dataflow slicing，并用同backbone/host消融区分图信息和工具schema，直接改变Agent定位语义粒度。。
- **Method：** 3. Methodology — This section formulates the problem (Section 3.1 and describes ARISE’s three components, namely the multi-granularity repository graph (Section 3.2 ), the three-tier tool API (Section 3.3 ), and the agent loop and evaluation protocol (Sections 3.4 – 3.5 ). Figure …
- **Evaluation：** 3.5. Evaluation Protocol — Localization metrics. These metrics evaluate the ranked (file, function, line) list returned by the localization task . Localization performance is assessed at three granularity levels against the ground-truth patch. File level. The gold file set is the set of files …
- **Limit / non-proof：** 5.5. Limitations — Intra-procedural scope. The most significant architectural limitation of ARISE’s data-flow layer is that get_dataflow_slice does not cross Calls edges. A bug whose root cause is a value mutated inside a callee produces a symptom at the call site but a …
- **Score V2：** Design Delta 2 / System Reach 2 / Durability 3 = **7/9**。
- **Books：** No Change — Existing Coverage。

<a id="2605.03129"></a>

## 2605.03129 — PIIGuard: Mitigating PII Harvesting under Adversarial Sanitization

- **原文：** https://arxiv.org/html/2605.03129v1（访问：2026-09-14）
- **审阅：** standard；exact-v1 valid; no withdrawal banner observed。
- **机制与 owner：** `PLATFORM-SECURITY`；content-owner PII defense via indirect injection changes the browser/sanitizer trust boundary。
- **Method：** 3 Methodology — Figure 2 : Overview of PIIGuard. Phase 1: leakage assessment for initial seed fragments; Phase 2: mutate and rerank fragments under rule-based feedback; Phase 3: Judge-based recoverability selection on final fragment. 3.1 Overview PIIGuard searches for a short, visually concealed …
- **Evaluation：** 4 Experiments Setup — This section describes how we evaluate PIIGuard, including the evaluation modes Section 4.1 , Data and evaluation metrics Section 4.2 . Detailed setup of the hyperparameters of PIIGuard is deferred to Appendix 0.A . 4.1 Evaluation Modes We evaluate PIIGuard …
- **Limit / non-proof：** Limitations and Future Work. — Although we drive mutation with a rule-based signal to reduce judgment bias, several evaluation endpoints, including benign utility and judge-based recoverability, still rely on a single LLM. When the target, mutator, and judge are the same model, the evaluation may …
- **Score V2：** Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- **Books：** No Change — Existing Coverage。

<a id="2605.03140"></a>

## 2605.03140 — Evaluating Retrieval-Augmented Generation for Explainable Malware Analysis

- **原文：** https://arxiv.org/html/2605.03140v1（访问：2026-09-14）
- **审阅：** standard；exact-v1 valid; no withdrawal banner observed。
- **机制与 owner：** `AGENT-RAG`；structured malware evidence shows that default RAG can reduce explanation quality when evidence is already sufficient。
- **Method：** 2. Proposed Approach — We evaluate the explainability of LLMs with and without RAG for malware explanation tasks when structured evidence already exists. Figure 1. RAG LLM architecture for malware explanation. Implementation. We use LlamaIndex as the RAG orchestration framework, ChromaDB for persistent vector …
- **Evaluation：** Abstract evaluation — Large Language Models (LLMs) are increasingly being used as security engineering tools to summarize and explain malware behavior to analysts.
- **Limit / non-proof：** 3. Discussion — Results analysis. Based on commonly observed ranges in the literature, BERTScores 0.9-1 indicate excellent alignment, scores between 0.85 and 0.9 reflect strong semantic similarity, and scores between 0.8 and 0.85 indicate moderate quality. Differences as small as 0.01–0.02 are meaningful …
- **Score V2：** Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- **Books：** No Change — Existing Coverage。

<a id="2605.03143"></a>

## 2605.03143 — Pact: A Choreographic Language for Agentic Ecosystems

- **原文：** https://arxiv.org/html/2605.03143v1（访问：2026-09-14）
- **审阅：** standard；exact-v1 valid; no withdrawal banner observed。
- **机制与 owner：** `AGENT-MULTI-AGENT`；choreography从合作参与者扩展显式choice/preferences并映射game，改变Agent协议遵守假设；只保留preliminary实现边界。。
- **Method：** 2. How to Forge a Pact — We now walk through the design of Pact by extending the bookseller choreography ( cf. Figure 1 ) incrementally to address concerns relevant in multi-agentic coordination. Each extension extends the language to capture an additional aspect of agentic interaction: (1) …
- **Evaluation：** Abstract evaluation — Recent advances in large language models have led to the rise of software systems (i.e.
- **Limit / non-proof：** 5. Conclusion & Future Work — In this work we have presented Pact , a choreographic language tailored for the domain of multi-agentic coordination, extending choreographies so that agents can not only express their communication patterns, the flow of information through a protocol, but also their …
- **Score V2：** Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- **Books：** No Change — Existing Coverage。

<a id="2605.03153"></a>

## 2605.03153 — OCRR: A Benchmark for Online Correction Recovery under Distribution Shift

- **原文：** https://arxiv.org/html/2605.03153v1（访问：2026-09-14）
- **审阅：** deep；exact-v1 valid; no withdrawal banner observed。
- **机制与 owner：** `PLATFORM-EVALUATION-SYSTEM`；correction curves jointly measure new-class recovery and old-distribution retention instead of proxy ANN recall alone。
- **Method：** 3. The OCRR Benchmark — 3.1 Streaming-learning constraints OCRR adopts two of three classical online-learning constraints: Constraint OCRR Reasoning Sequential data arrival Required Models cannot peek ahead. Real-time updates per correction Required No batch retraining; one update step. Bounded memory Reported, not enforced We instead …
- **Evaluation：** 5. Results — 5.1 Headline: substrate is Pareto-dominant across all evaluated settings Figure 1: Figure 1: storage-vs-final-novel Pareto. Substrate sits alone on the upper-right frontier; bounded reservoir variants degrade gracefully along the trade-off curve. Banking77, oracle policy, 3 seeds, mean ± std (Table …
- **Limit / non-proof：** 6.6 Limitations — We collect the explicit limitations of OCRR v1 in one place: • Single language : Banking77 and CLINC150 are English-only. Recovery dynamics in multilingual or cross-script settings are open. • Categorical shift only : held-out classes appear in the stream; …
- **Score V2：** Design Delta 3 / System Reach 2 / Durability 3 = **8/9**。
- **Books：** No Change — Existing Coverage。

<a id="2605.03159"></a>

## 2605.03159 — Learning Correct Behavior from Examples: Validating Sequential Execution in Autonomous Agents

- **原文：** https://arxiv.org/html/2605.03159v1（访问：2026-09-14）
- **审阅：** deep；exact-v1 valid; no withdrawal banner observed。
- **机制与 owner：** `AGENT-WORKFLOW`；passing traces are compiled into necessary-state and order constraints for nondeterministic workflow acceptance。
- **Method：** 2.2 Our Approach — We collect 3–5 passing execution traces where the agent successfully completes the task. Each trace captures sequential screenshots showing the UI state at each step along with actions taken between states such as clicks and keystrokes. For example, traces might …
- **Evaluation：** 4.1 Complexity Analysis — The time complexity of the algorithm is dominated by the merging phase. For n n traces with average length k k , PTA construction runs in O ⁡ ( n ⋅ k ) O(n\cdot k) time, which is linear in …
- **Limit / non-proof：** 5.4 Threats to Validity — Our evaluation uses a synthetic bug scenario with a controlled VS Code extension, which allows precise measurement but may not capture the complexity of real-world failure patterns; additionally, the small sample sizes (e.g., 1 false success, 1 missed bug) limit …
- **Score V2：** Design Delta 2 / System Reach 2 / Durability 3 = **7/9**。
- **Books：** Integrate — applied and post-write audited。

<a id="2605.03160"></a>

## 2605.03160 — Pairwise matrices for sparse autoencoders: single-feature inspection mislabels causal axes

- **原文：** https://arxiv.org/html/2605.03160v1（访问：2026-09-14）
- **审阅：** standard；exact-v1 valid; no withdrawal banner observed。
- **机制与 owner：** `MODEL-TRANSFORMER-LAYER`；top-context SAE标签与steering方向不等价，joint feature suppression在matched-distortion random control下破坏grounded composition，直接改写可解释性因果claim权限。。
- **Method：** 3 Methods — The pipeline has four phases. Phase 1 generates samples under matched introspective and control prompts. Phase 2 partitions samples into pools by lexical cluster. Phase 3 ranks SAE features by per-pool activation differences with bootstrap and permutation controls. Phase 4 …
- **Evaluation：** 4 Three findings on what single-feature inspection misses — We report three findings on Qwen3-1.7B-Instruct, each on a different axis of the matrix (coefficient × \times joint condition). All experiments use the Qwen-Scope SAE at layer 20. 4.1 Coefficient axis: top-context labels miss the causal axis Feature #26221 was …
- **Limit / non-proof：** 7 Limitations — The headline coefficient-axis finding rests on Qwen #26221 and Gemma #3997, with Qwen #22082 (monotonic) and #2932 (breakdown) as falsifying anchors: two positives plus two controls earn the non-monotonic-with-coherence-preserved criterion but do not estimate its prevalence. The cross-model claim is …
- **Score V2：** Design Delta 2 / System Reach 1 / Durability 2 = **5/9**。
- **Books：** No Change — Existing Coverage。

<a id="2605.03179"></a>

## 2605.03179 — A Validated Prompt Bank for Malicious Code Generation: Separating Executable Weapons from Security Knowledge in 1,554 Consensus-Labeled Prompts

- **原文：** https://arxiv.org/html/2605.03179v1（访问：2026-09-14）
- **审阅：** standard；exact-v1 valid; no withdrawal banner observed。
- **机制与 owner：** `PLATFORM-SECURITY`；malicious-code evaluation separates executable weapon construction from harmful knowledge before interpreting refusal。
- **Method：** 3 Methods — The artifact described in this paper is a consolidated, consensus-labeled prompt bank constructed from four prior benchmarks. Figure 1 summarizes the end-to-end construction pipeline: four source benchmarks feed a rule-based pre-filter, a five-model consensus classifier spanning both general-purpose and coder-specialized …
- **Evaluation：** 2.1 Malicious Code Generation Benchmarks and the Broader Safety-Benchmark Landscape — Research on LLM safety evaluation has produced a dense landscape of benchmark artifacts over the past three years, with several distinct lineages emerging. The earliest large-scale adversarial-prompt corpora targeting safety-aligned models were assembled to support automated attack methods: Zou et …
- **Limit / non-proof：** 5.1 Limitations — Six limitations qualify the released artifact. First, inter-rater reliability is quantified as agreement among five LLM judges rather than between the LLM panel and human annotators. The choice of an all-LLM panel is deliberate and reflects the multi-vendor jury design …
- **Score V2：** Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- **Books：** No Change — Existing Coverage。

<a id="2605.03188"></a>

## 2605.03188 — Dependency-Aware Privacy for Multi-turn Agents

- **原文：** https://arxiv.org/html/2605.03188v1（访问：2026-09-14）
- **审阅：** deep；exact-v1 valid; no withdrawal banner observed。
- **机制与 owner：** `PLATFORM-SECURITY`；derived-value独立加噪可放大root distinguishability，root-once sanitization用postprocessing共享跨turn预算；改变Agent数据发布图的隐私会计。。
- **Method：** Our approach. — We propose RootGuard (Fig. 1 ), a dependency-aware privacy mechanism for multi-turn agentic interactions. We noise the private root values exactly once, and compute everything else deterministically from the noised roots. By the post-processing theorem of differential privacy [ 11 …
- **Evaluation：** Scope of evaluation. — Our experiments (Sec. 5.4 ) evaluate repeated direct root queries. Under independent noising, nonlinear derived-function queries could further amplify the adversary’s advantage (Sec. 4.3.1 ), making our reported numbers a lower bound on its vulnerability. Under RootGuard, the adversary’s function …
- **Limit / non-proof：** Limitations and future work. — We assume perfect NER for root identification, following prior sanitizers [ 8 , 9 ] ; integrating noisy NER into the privacy analysis is open. Our evaluation covers structured numeric values in single-user sessions; extending to free-form text, multi-user composition, …
- **Score V2：** Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- **Books：** Integrate — applied and post-write audited。

<a id="2605.03190"></a>

## 2605.03190 — VDCores: Resource Decoupled Programming and Execution for Asynchronous GPU

- **原文：** https://arxiv.org/html/2605.03190v1（访问：2026-09-14）
- **审阅：** deep；exact-v1 valid; no withdrawal banner observed。
- **机制与 owner：** `INFER-TENSORRT-LLM`；异步GPU以资源隔离virtual core和dependency micro-op解耦kernel编排，直接改变memory/compute重叠与动态输入执行。。
- **Method：** 4.1. The VDCores Decoupled Model — This section introduces the decoupled programming model VDCores adopt and how it shifts the programming and execution paradigm on asynchronous GPUs. ⬇ 1 VDC_DEFINE_UOP ( COP_MATVEC , h_matvec ) 2 __vdc_cop__ h_matvec ( VdcInst & inst , VdcCtx & ctx …
- **Evaluation：** 6. Evaluation — We answer three key questions in this section: (1) Does VDCores improve end-to-end model execution over state-of-the-art kernel and megakernel systems? (§ 6.1 ) (2) How much does each key optimization in VDCores contribute to the performance gain? (§ 6.2 …
- **Limit / non-proof：** 8. Discussion — Compiler support for VDCores. We view VDCores as a suitable abstraction layer for high-performance compilers. At μ \mu op layer, Compilers could now generate efficient handler for single leveraging their static packing and local schedule optimization. At system level, similar …
- **Score V2：** Design Delta 2 / System Reach 2 / Durability 3 = **7/9**。
- **Books：** Integrate — already present and rechecked。

<a id="2605.03196"></a>

## 2605.03196 — Geometric Deviation as an Unsupervised Pre-Generation Reliability Signal: Probing LLM Representations for Answerability

- **原文：** https://arxiv.org/html/2605.03196v1（访问：2026-09-14）
- **审阅：** standard；exact-v1 valid; no withdrawal banner observed。
- **机制与 owner：** `PLATFORM-EVALUATION-SYSTEM`；pre-generation representation geometry predicts math answerability but not factual answerability, bounding self-knowledge sensors。
- **Method：** 3 Experimental Setup — Models. We use three instruction-tuned models at the same scale (7–8B parameters): Llama 3.1-8B-Instruct ( Dubey et al., 2024 ) , Qwen 2.5-7B-Instruct ( Qwen Team, 2025 ) , and Mistral-7B-Instruct-v0.3 ( Jiang et al., 2023 ) , all loaded …
- **Evaluation：** 3 Experimental Setup — Models. We use three instruction-tuned models at the same scale (7–8B parameters): Llama 3.1-8B-Instruct ( Dubey et al., 2024 ) , Qwen 2.5-7B-Instruct ( Qwen Team, 2025 ) , and Mistral-7B-Instruct-v0.3 ( Jiang et al., 2023 ) , all loaded …
- **Limit / non-proof：** 7 Limitations — Scale. Sample sizes are modest by benchmark standards ( n = 50 n=50 matched pairs for Math , n = 10 n=10 for Fact , n = 30 n=30 for Code ). Fact and Code AUC estimates carry high variance. …
- **Score V2：** Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- **Books：** No Change — Existing Coverage。

<a id="2605.03202"></a>

## 2605.03202 — Stop Automating Peer Review Without Rigorous Evaluation

- **原文：** https://arxiv.org/html/2605.03202v1（访问：2026-09-14）
- **审阅：** standard；exact-v1 valid; no withdrawal banner observed。
- **机制与 owner：** `PLATFORM-EVALUATION-SYSTEM`；AI reviewer跨论文hivemind与style rewriting可game评分，直接反证相关judge票数及paper-laundering下评价可信度。。
- **Method：** 3 The AI reviewer hivemind effect — It is well-documented that instruction-tuned LLMs produce homogeneous outputs ( Zhang et al., 2025 ; West and Potts, 2025 ; Jiang et al., 2025 ; Hu et al., 2026 ; Goel et al., 2025 ; Kim et al., 2025a ) …
- **Evaluation：** 3.3 Results: Hivemind effect in the wild — Figure 1 : The AI reviewer hivemind effect in ICLR 2026 reviews. Distribution of pairwise inter-paper review similarity (InterSim) for fully AI-generated reviews versus all other reviews (human-written and AI-assisted). Fully AI-generated reviews show significantly higher within-group similarity (mean = …
- **Limit / non-proof：** Appendix A Limitations — Our AI reviewer simulations use only two models (GPT-5.1 and Claude Sonnet 4.5) with a single fixed prompt. In practice, researchers and conferences may use diverse prompts, temperatures, and model versions, which could yield more varied outputs. The high IntraSim …
- **Score V2：** Design Delta 2 / System Reach 1 / Durability 2 = **5/9**。
- **Books：** No Change — Existing Coverage。

<a id="2605.03208"></a>

## 2605.03208 — Kerncap: Automated Kernel Extraction and Isolation for AMD GPUs

- **原文：** https://arxiv.org/html/2605.03208v1（访问：2026-09-14）
- **审阅：** deep；exact-v1 valid; no withdrawal banner observed。
- **机制与 owner：** `INFER-TENSORRT-LLM`；HSA dispatch capture做完整virtual-address closure保持间接device pointers，且绑定Triton autotune配置；直接改变kernel独立复现的语义条件。。
- **Method：** Cross-architecture overhead. — Table 4 summarizes the same overhead decomposition for the three HIP workloads on each architecture. Interception-only overhead is consistently ≤ 1.2 × \leq 1.2\times on the two CDNA generations and ≤ 1.4 × \leq 1.4\times on RDNA3 for the larger …
- **Evaluation：** Empirical incidence. — On the two HIP workloads in our evaluation (llama.cpp and LAMMPS), the DWARF path succeeded for both, and nm disambiguation fired for both (llama.cpp’s template-instantiated mul_mat_vec_q variants and LAMMPS’s Kokkos-expanded TagPairEAMKernelC ). The grep fallback was not load-bearing in our …
- **Limit / non-proof：** 7. Limitations and Future Work — Single-kernel isolation. Kerncap captures one kernel dispatch at a time. It does not track inter-kernel data dependencies or stream synchronization, so kernels that depend on the output of preceding kernels require those predecessors to have already executed before the capture …
- **Score V2：** Design Delta 2 / System Reach 2 / Durability 3 = **7/9**。
- **Books：** No Change — Existing Coverage。

<a id="2605.03217"></a>

## 2605.03217 — Moral Sensitivity in LLMs: A Tiered Evaluation of Contextual Bias via Behavioral Profiling and Mechanistic Interpretability

- **原文：** https://arxiv.org/html/2605.03217v1（访问：2026-09-14）
- **审阅：** standard；exact-v1 valid; no withdrawal banner observed。
- **机制与 owner：** `PLATFORM-SECURITY`；同参数reasoning distillation可能重激活浅层bias circuit，配合graded社会线索与activation patching，直接改变alignment迁移的安全判断。。
- **Method：** 2 Methodology — We evaluate four publicly accessible and proprietary instruction-tuned LLMs: Claude (Anthropic), Qwen (Alibaba DAMO), Llama 3 (Meta), Gemma (Google). Gemini 1.5 (Google) was included in supplementary analyses. All models were queried through their standard inference APIs; no fine-tuning or system-prompt …
- **Evaluation：** 3 Experimental Setup — Evaluation Metrics: Each model response to a tiered prompt is annotated as Biased , Unbiased , or Ambiguous . Labels are assigned using automated classifiers and human annotators. The Ambiguous category captures responses exhibiting hedging, uncertainty, or conflicting reasoning. Based …
- **Limit / non-proof：** Appendix C Limitations — While our study links behavioral bias patterns to internal model mechanisms, several limitations remain. Limited sample size in mechanistic analysis Our mechanistic experiments are conducted on a relatively small set of prompts (n = 50), chosen as a controlled instantiation …
- **Score V2：** Design Delta 2 / System Reach 1 / Durability 2 = **5/9**。
- **Books：** No Change — Existing Coverage。

<a id="2605.03226"></a>

## 2605.03226 — Self-Mined Hardness for Safety Fine-Tuning

- **原文：** https://arxiv.org/html/2605.03226v1（访问：2026-09-14）
- **审阅：** deep；exact-v1 valid; no withdrawal banner observed。
- **机制与 owner：** `TRAIN-SFT`；当前policy自挖hard安全样本降低ASR却显著overrefusal，benign adversarial mix给明确tradeoff，直接改变安全SFT数据选择。。
- **Method：** 3 Method — 3.1 Notation Let M M be a fixed instruction-tuned target model. Given an adversarial prompt p p we draw rollouts r ∼ M ( ⋅ ∣ p ) r\sim M(\cdot\mid p) at sampling temperature T = 1 T=1 . A …
- **Evaluation：** Jailbreak attacks and benchmarks. — Adversarial prompting ( Wei et al., 2023 ) and automated attack search ( Zou et al., 2023 ) reliably elicit harmful completions from aligned models. WildJailbreak and WildGuardMix ( Jiang et al., 2024 ; Han et al., 2024 ) contain …
- **Limit / non-proof：** 7 Limitations and Future Work — Limitations. All reported results are on the Llama-3 family (Llama-3-8B-Instruct and Llama-3.2-3B-Instruct), so cross-family generalization remains untested. Even the best mixed baseline refuses 30 ​ – ​ 51 % 30\text{--}51\% (8B) or 52 ​ – ​ 72 % 52\text{--}72\% (3B) …
- **Score V2：** Design Delta 2 / System Reach 2 / Durability 3 = **7/9**。
- **Books：** No Change — Existing Coverage。

<a id="2605.03228"></a>

## 2605.03228 — MAGE: Safeguarding LLM Agents against Long-Horizon Threats via Shadow Memory

- **原文：** https://arxiv.org/html/2605.03228v1（访问：2026-09-14）
- **审阅：** deep；exact-v1 valid; no withdrawal banner observed。
- **机制与 owner：** `PLATFORM-SECURITY`；独立shadow memory保留跨turn安全关键状态再判断pending action，针对分散长程意图丢失，需核验检测/utility范围。。
- **Method：** 4.2. System Design — Figure 2 (a) illustrates the overall architecture of MAGE , comprising two key components: i ) the memory manager M M , which distills and maintains security-critical context across the agent’s interaction turns; ii ) the judge J J , …
- **Evaluation：** 5. Evaluation I: User-as-Adversary — We now empirically evaluate the effectiveness of MAGE under the long-horizon user-as-adversary threat model. 5.1. Experimental Setting 5.1.1. Attacks, Datasets, and Agents We instantiate the above threat model with Sequential Tool-Attack Chaining ( STAC ) ( Li et al., 2025a …
- **Limit / non-proof：** 7. Conclusion and Future Work — As LLM agents are deployed in complex, multi-turn settings, they face long-horizon attacks that spread adversarial intent across extended interactions, evading per-turn defenses. We present MAGE , the first framework to leverage agentic memory as a defensive measure for trajectory-level …
- **Score V2：** Design Delta 2 / System Reach 2 / Durability 3 = **7/9**。
- **Books：** No Change — Existing Coverage。

<a id="2605.03229"></a>

## 2605.03229 — Sparse Memory Finetuning as a Low-Forgetting Alternative to LoRA and Full Finetuning

- **原文：** https://arxiv.org/html/2605.03229v1（访问：2026-09-14）
- **审阅：** standard；exact-v1 valid; no withdrawal banner observed。
- **机制与 owner：** `AGENT-MEMORY`；sparse memory rows expose a capacity, adaptation and forgetting branch against LoRA/full tuning。
- **Method：** 3 Method — Figure 1 : Method overview. Each Qwen-2.5 transformer block uses RMSNorm, grouped-query self-attention, and a SwiGLU MLP down ​ _ ​ proj ​ ( silu ⁡ ( gate ​ _ ​ proj ​ ( x ) ) ⊙ up ​ …
- **Evaluation：** 4 Experiments — 4.1 Setup We use Qwen-2.5-0.5B-Instruct ( Qwen Team, 2024 ) as the base model. Sparse and LoRA training use a learning rate of × 10 − 4 5\!\times\!10^{-4} and × 10 − 4 2\!\times\!10^{-4} respectively. Full finetuning uses × 10 …
- **Limit / non-proof：** 5 Conclusion — We re-implement SMF on Qwen-2.5-0.5B-Instruct and compare against LoRA and full finetuning on MedMCQA. Two takeaways stand out. Preserving the pretrained MLP path matters at this scale: replacement memory, which discards the MLP, lies off both Pareto frontiers, while the …
- **Score V2：** Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- **Books：** No Change — Existing Coverage。

<a id="2605.03242"></a>

## 2605.03242 — Enhancing Agent Safety Judgment: Controlled Benchmark Rewriting and Analogical Reasoning for Deceptive Out-of-Distribution Scenarios

- **原文：** https://arxiv.org/html/2605.03242v1（访问：2026-09-14）
- **审阅：** standard；exact-v1 valid; no withdrawal banner observed。
- **机制与 owner：** `PLATFORM-SECURITY`；保留底层unsafe label却重写隐含风险/语境，具体隔离Agent safety judge OOD脆弱性；类比检索只受限增强。。
- **Method：** 3 Methodology — 3.1 Formalizing Real-World Safety Challenges Our methodology stems from a key insight: risks in current safety benchmarks are often too explicit and therefore fail to measure judgment under disguise, ambiguity, or misleading context. Our goal is not to invent new …
- **Evaluation：** 2.1 Agent Safety Benchmarks — Existing benchmarks target important but relatively distinct aspects of agent safety. R-Judge ( Yuan et al., 2024 ) focuses on post-hoc risk awareness over interaction logs, SafeAgentBench ( Zhang et al., 2024b ) evaluates planning safety in simulated environments, and …
- **Limit / non-proof：** Limitations — Our work has several limitations that define the scope of our claims. First, although ROME broadens the difficulty of agent-safety evaluation, it is still constructed from 100 unsafe source trajectories originating from a single benchmark family. This means the benchmark …
- **Score V2：** Design Delta 2 / System Reach 1 / Durability 2 = **5/9**。
- **Books：** No Change — Existing Coverage。

<a id="2605.03245"></a>

## 2605.03245 — Text-Conditional JEPA for Learning Semantically Rich Visual Representations

- **原文：** https://arxiv.org/html/2605.03245v1（访问：2026-09-14）
- **审阅：** standard；exact-v1 valid; no withdrawal banner observed。
- **机制与 owner：** `MULTIMODAL-REPRESENTATION`；caption sparse cross-attention条件降低masked patch特征预测不确定性，提供非contrastive视觉语言预训练替代机制。。
- **Method：** 3 Method — 3.1 I-JEPA Baseline The I-JEPA objective is to predict the representations of masked image parts, i.e. , target patches y = { y j | j ∈ B y } y=\{y_{j}|j\in B_{y}\} , given the context patches x = { …
- **Evaluation：** 4 Experimental Setup — 4.1 Pretraining on ImageNet Data preparation . IN-1k and IN-21k ( Russakovsky et al., 2015 ) are the golden pretraining datasets for most visual SSL methods. We compare with recent SSL methods all pretrained on the same ImageNet dataset, either …
- **Limit / non-proof：** 6 Conclusion — In this paper, we introduce fine-grained text conditioning into the JEPA prediction task, which learns text-sensitive and semantically rich visual representations. We show our TC-JEPA method can reduce feature prediction uncertainty and hence improve training stability. When evaluated on various …
- **Score V2：** Design Delta 2 / System Reach 1 / Durability 2 = **5/9**。
- **Books：** No Change — Existing Coverage。

<a id="2605.03252"></a>

## 2605.03252 — Ortho-Hydra: Orthogonalized Experts for DiT LoRA

- **原文：** https://arxiv.org/html/2605.03252v1（访问：2026-09-14）
- **审阅：** deep；exact-v1 valid; no withdrawal banner observed。
- **机制与 owner：** `TRAIN-LORA`；zero-init MoE LoRA导致router/expert置换对称deadlock，用disjoint singular subspaces让初始router梯度非退化，具体改写初始化选择。。
- **Method：** 3 Method: Ortho-Hydra — (a) Plain LoRA x x A A ℓ ∈ ℝ r \ell\,{\in}\,\mathbb{R}^{r} B B (init 0 0 ) + + W 0 ​ x W_{0}\,x y y d out d_{\mathrm{out}} col ⁡ ( B ) \mathrm{col}(B) (b) HydraLoRA x x …
- **Evaluation：** 4 Experiments — Figure 2: Cold-start router dynamics across three HydraLoRA variants ( E = 12 E\!=\!12 , balance-loss weight × 10 − 7 5\!\times\!10^{-7} with warmup ratio 0.4 0.4 , AdamW, identical dataset and optimiser schedule). Solid: mean normalised router entropy H …
- **Limit / non-proof：** 5 Discussion and limitations — Subspace restriction. Δ ​ W ​ ( b ) \Delta W(b) is constrained to live in colspace ⁡ ( P bases ) ⊆ top ​ - ​ ( E ​ r ) \mathrm{colspace}(P_{\mathrm{bases}})\subseteq\mathrm{top}\text{-}(Er) left singular vectors of W 0 W_{0} …
- **Score V2：** Design Delta 3 / System Reach 2 / Durability 3 = **8/9**。
- **Books：** Integrate — applied and post-write audited。

<a id="2605.03258"></a>

## 2605.03258 — The Right Answer, the Wrong Direction: Why Transformers Fail at Counting and How to Fix It

- **原文：** https://arxiv.org/html/2605.03258v1（访问：2026-09-14）
- **审阅：** standard；exact-v1 valid; no withdrawal banner observed。
- **机制与 owner：** `MODEL-DECODER-ONLY`；计数内部可线性读出却与digit head错位，digit-row修复只改善约束预测而LoRA才改善自由生成，具体分离表示/读出/路由瓶颈。。
- **Method：** 3 Method — 3.1 Synthetic Benchmark We generate a full-factorial benchmark: 6 ​ counts × 3 ​ distractors × 4 ​ lengths × 3 ​ spacings = 216 ​ conditions × 20 ​ samples = 4,320 ​ prompts 6\text{ counts}\times 3\text{ distractors}\times 4\text{ …
- **Evaluation：** 3.1 Synthetic Benchmark — We generate a full-factorial benchmark: 6 ​ counts × 3 ​ distractors × 4 ​ lengths × 3 ​ spacings = 216 ​ conditions × 20 ​ samples = 4,320 ​ prompts 6\text{ counts}\times 3\text{ distractors}\times 4\text{ lengths}\times 3\text{ spacings}=216\text{ …
- **Limit / non-proof：** Limitations. — (1) LoRA Q/V variance: The headline LoRA generation result (83.1% ± \pm 7.2%) reflects per-seed values of 71.5%, 89.0%, 86.5%, 81.0%, and 87.5% (seeds 42, 11, 77, 99, 123) under the multi-task generation protocol (entity counting + character counting + …
- **Score V2：** Design Delta 2 / System Reach 1 / Durability 2 = **5/9**。
- **Books：** No Change — Existing Coverage。

<a id="2605.03269"></a>

## 2605.03269 — RLDX-1 Technical Report

- **原文：** https://arxiv.org/html/2605.03269v1（访问：2026-09-14）
- **审阅：** deep；exact-v1 valid; no withdrawal banner observed。
- **机制与 owner：** `MULTIMODAL-EMBODIED-VLA`；MSAT modality-specific streams与joint attention整合物理感知/长记忆，提供复杂接触VLA的架构分支，需拆解系统模块与本体贡献。。
- **Method：** Neural Architecture — Real-world dexterous manipulation requires diverse functional capabilities beyond the versatile intelligence provided by a pre-trained VLM. We focus on three such capabilities, including motion awareness, long-term memory, and physical sensing, and address each with a tailored architectural module built on …
- **Evaluation：** Evaluation & Analysis — For evaluation, we combine diverse simulation benchmarks with real-world manipulation tasks across humanoid and single-arm embodiments. The simulation benchmarks assess broad VLA capabilities, while the real-world tasks evaluate versatile intelligence and functional capabilities. As strong baselines, we include recent state-of-the-art …
- **Limit / non-proof：** 8. Conclusion — In this paper, we have presented RLDX-1 , a general-purpose Vision-Language-Action model (VLA) for human-like dexterous manipulation in real-world environments. RLDX-1 goes beyond versatile intelligence by integrating key functional capabilities into a unified architecture for real-world manipulation, including motion awareness, …
- **Score V2：** Design Delta 2 / System Reach 2 / Durability 3 = **7/9**。
- **Books：** No Change — Existing Coverage。

<a id="2605.03275"></a>

## 2605.03275 — Beyond Similarity Search: A Unified Data Layer for Production RAG Systems

- **原文：** https://arxiv.org/pdf/2605.03275v1（访问：2026-09-14）
- **审阅：** deep；exact-v1 valid; no withdrawal banner observed。
- **机制与 owner：** `AGENT-RAG`；split storage使RAG freshness/tenant isolation/query组合成本耦合，统一事务data layer给具体取舍，需核验50k规模和安全断言范围。。
- **Method：** official exact-v1 PDF; method sections were recovered and checked in the prior exact-v1 packet
- **Evaluation：** official exact-v1 PDF; experimental setup/results were checked in the prior exact-v1 packet
- **Limit / non-proof：** official exact-v1 PDF; scope and limitation boundary were checked in the prior exact-v1 packet
- **Score V2：** Design Delta 2 / System Reach 2 / Durability 3 = **7/9**。
- **Books：** No Change — Existing Coverage。

<a id="2605.03308"></a>

## 2605.03308 — Revisiting the Travel Planning Capabilities of Large Language Models

- **原文：** https://arxiv.org/html/2605.03308v1（访问：2026-09-14）
- **审阅：** standard；exact-v1 valid; no withdrawal banner observed。
- **机制与 owner：** `AGENT-PLANNING`；oracle中间context解耦constraint/tool/plan/error-identification/correction，隔离cascade并暴露自纠错偏差，具体改变Agent规划评价。。
- **Method：** 3 Primitive Tasks — 3.1 Problem Formulation To rigorously formalize the planning process, we define the variable spaces involved. Let 𝒬 \mathcal{Q} denote the space of natural language user queries, and 𝒞 \mathcal{C} be the space of derived constraints. To model the interaction with …
- **Evaluation：** 4 Results — We evaluate a set of models, including GPT-5.2, DeepSeek V3.2 (DS V3.2), Qwen3 Max, Claude Sonnet 4.5 (Claude S4.5), and Gemini 3 Pro Preview (Gemini 3 Pro), in both reasoning and non-reasoning modes. For constraint extraction and plan generation, our …
- **Limit / non-proof：** 5 Limitations and Future Work — Despite the comprehensive analysis presented, our study has several limitations. First, we adopt an atomic evaluation strategy with oracle inputs to isolate individual reasoning modules. While this design enables fine grained diagnosis and avoids error propagation, it does not capture …
- **Score V2：** Design Delta 2 / System Reach 1 / Durability 2 = **5/9**。
- **Books：** No Change — Existing Coverage。

<a id="2605.03309"></a>

## 2605.03309 — Cryptographic Registry Provenance: Structural Defense Against Dependency Confusion in AI Package Ecosystems

- **原文：** https://arxiv.org/html/2605.03309v1（访问：2026-09-14）
- **审阅：** deep；exact-v1 valid; no withdrawal banner observed。
- **机制与 owner：** `PLATFORM-SECURITY`；registry identity+publisher/registry dual signature+namespace pinning规定artifact来源验证，AI package供应链有具体协议分支，须核验非实证/普遍性claim。。
- **Method：** 4 Two-Layer Archive Format — Published artifacts use a two-layer archive format separating the provenance envelope from the source contents: ⬇ artifact -1.2.0. pkg ( uncompressed outer tar ) ⊢ \vdash provenance . json # Provenance manifest ⊢ \vdash signature . json # Publisher Ed25519 …
- **Evaluation：** 12 Evaluation — 12.1 Verification Performance All performance numbers in this section are measured from a running implementation on an Apple M-series processor, using median values over 50 iterations. The implementation uses Erlang’s :crypto module for Ed25519 and SHA-256 operations. Table 2 shows …
- **Limit / non-proof：** 13.1 Limitations — Key management and revocation. Developers must manage Ed25519 keypairs and each registry instance must manage its own keypair. Auto-generation on first use and secure local storage mitigate the developer burden, but key rotation, backup, and revocation remain operational concerns. The …
- **Score V2：** Design Delta 2 / System Reach 3 / Durability 3 = **8/9**。
- **Books：** Integrate — already present and rechecked。

<a id="2605.03310"></a>

## 2605.03310 — Coordination as an Architectural Layer for LLM-Based Multi-Agent Systems

- **原文：** https://arxiv.org/html/2605.03310v1（访问：2026-09-14）
- **审阅：** standard；exact-v1 valid; no withdrawal banner observed。
- **机制与 owner：** `AGENT-MULTI-AGENT`；coordination configuration is isolated as a measurable multi-agent architecture variable with calibration and significance limits。
- **Method：** 2.3 Methodological critique: the information-architecture confound — Ao et al. (2026) provide the methodological foundation for the experimental design we adopt in Section 4 . They develop a decision-theoretic model in which alternative LLM-based multi-agent workflows are compared through the information available to the final decision. Their …
- **Evaluation：** 2.1 Empirical failure-mode taxonomies — Cemri et al. (2025) present the first large-scale empirical study of multi-agent LLM failures, analyzing 1 600+ execution traces across seven popular frameworks (including AutoGen, MetaGPT, and ChatDev) on coding, math, and general-purpose tasks. They identify 14 fine-grained failure modes …
- **Limit / non-proof：** 7.6 Threats to validity — Prompt sensitivity. The role-specific instruction blocks were authored once and not subjected to systematic ablation. A more careful study would vary the role prompts within each configuration while keeping the configuration’s structure fixed, to attribute observed effects to coordination structure …
- **Score V2：** Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- **Books：** No Change — Existing Coverage。

<a id="2605.03312"></a>

## 2605.03312 — MemFlow: Intent-Driven Memory Orchestration for Small Language Model Agents

- **原文：** https://arxiv.org/html/2605.03312v1（访问：2026-09-14）
- **审阅：** standard；exact-v1 valid; no withdrawal banner observed。
- **机制与 owner：** `AGENT-MEMORY`；按query intent外置memory plan、定型evidence compile并按tier升级，改变SLM自主memory-loop不可靠的控制分工。。
- **Method：** Appendix D Full Pipeline Algorithm — Algorithm 1 provides pseudocode for the MemFlow read-path pipeline. Algorithm 1 MemFlow Read-Path Pipeline 1: Query q q , history H H , SLM π θ \pi_{\theta} 2: Answer a a 3: retries ← 0 \leftarrow 0 4: if token_overlap …
- **Evaluation：** 4 Experiments & Results — We evaluate MemFlow along two axes: accuracy on long-horizon memory QA, and efficiency , measured by the answer-context tokens fed to the SLM. We conduct four experiments targeting distinct questions: (1) Does MemFlow outperform SLM baselines and dedicated memory systems …
- **Limit / non-proof：** 5 Conclusion, Limitations, and Future Work — We presented MemFlow , a training-free memory orchestration framework for long-horizon SLM agents. Its core finding is that a substantial portion of SLM memory failure can be mitigated by matching each query to an appropriate memory operation before evidence is …
- **Score V2：** Design Delta 2 / System Reach 1 / Durability 2 = **5/9**。
- **Books：** No Change — Existing Coverage。

<a id="2605.03314"></a>

## 2605.03314 — When to Think, When to Speak: Learning Disclosure Policies for LLM Reasoning

- **原文：** https://arxiv.org/html/2605.03314v1（访问：2026-09-14）
- **审阅：** deep；exact-v1 valid; no withdrawal banner observed。
- **机制与 owner：** `AGENT-CONTEXT`；离线entailment对齐训练交错披露策略，改变准确率/内容时序tradeoff；训练checker不是runtime gate，已按exact-v1纠正。。
- **Method：** 3 Method — We first describe how to construct supervised fine-tuning (SFT) data for dual-channel behavior from standard input–reasoning–answer triples ( x , r , a ) (x,r,a) . We transform each triple into an interleaved sequence S = ( x , r …
- **Evaluation：** 4 Experiments — 4.1 Training Details Model Architectures and Initialization. We study two models from the Qwen3 family: the Mixture-of-Experts (MoE) Qwen3-30B-A3B and the dense Qwen3-4B . Unless otherwise stated, we initialize from their post-trained checkpoints rather than base models. This choice preserves …
- **Limit / non-proof：** Appendix F Limitations — Our study has several limitations that are largely practical rather than conceptual. Entailment alignment cost and noise. SxS relies on entailment-aligned supervision to ensure early disclosures are supported by the reasoning prefix. In our current instantiation, using a large entailment …
- **Score V2：** Design Delta 2 / System Reach 2 / Durability 3 = **7/9**。
- **Books：** Integrate — already present and rechecked。

<a id="2605.03317"></a>

## 2605.03317 — AHPA: Adaptive Hierarchical Prior Alignment for Diffusion Transformers

- **原文：** https://arxiv.org/html/2605.03317v1（访问：2026-09-14）
- **审阅：** deep；exact-v1 valid; no withdrawal banner observed。
- **机制与 owner：** `MULTIMODAL-GENERATIVE-PARADIGMS`；useful diffusion representation granularity changes with SNR/timestep, making a static alignment target mismatched。
- **Method：** 4 Method — 4.1 Adaptive Hierarchical Prior Alignment (AHPA) The core of AHPA is that the diffusion process is inherently non-stationary, requiring a dynamic shift in guidance granularity as the signal-to-noise ratio (SNR) evolves. We propose to align the internal representations of the …
- **Evaluation：** 5 Experiments and Analysis — 5.1 Experimental Setup We evaluate AHPA across SiT-B/2, L/2, and XL/2 scales. Following the hierarchical partitioning established in Sec. 4.2 , the dynamic router ℛ ϕ \mathcal{R}_{\phi} is implemented as a 4-layer MLP that adaptively modulates the contributions of 𝒢 …
- **Limit / non-proof：** Appendix J Limitations — While AHPA demonstrates significant improvements in training efficiency and generative quality, we acknowledge several limitations that provide avenues for future work: • Dependence on Pre-trained VAEs: Our method relies on the hierarchical feature space of a frozen VAE (e.g., SD-VAE). …
- **Score V2：** Design Delta 2 / System Reach 2 / Durability 3 = **7/9**。
- **Books：** Integrate — applied and post-write audited。

<a id="2605.03327"></a>

## 2605.03327 — DGPO: Distribution Guided Policy Optimization for Fine Grained Credit Assignment

- **原文：** https://arxiv.org/html/2605.03327v1（访问：2026-09-14）
- **审阅：** deep；exact-v1 valid; no withdrawal banner observed。
- **机制与 owner：** `TRAIN-GRPO`；bounded Hellinger和entropy-gated token权重重分配sequence advantage，直接改变critic-free RL信用分配；不能把entropy称真实epistemic truth。。
- **Method：** 3 Distribution-Guided Policy Optimization — 3.1 Preliminaries and Motivation In the context of aligning large language models (LLMs) for complex reasoning tasks, such as Chain-of-Thought generation, standard Group Relative Policy Optimization (GRPO) relies on a coarse-grained, sequence-level reward mechanism. Given a prompt x x , …
- **Evaluation：** Gradient Stability Analysis. — The technical superiority of DGPO lies in its gradient dynamics. In standard KL-penalized RL, the gradient of the objective: ℒ K ​ L = 𝔼 ^ [ ρ t A t − β KL ( π θ | | π …
- **Limit / non-proof：** Appendix B Limitations and Future Work — B.1 Limitations While Distribution-Guided Policy Optimization (DGPO) provides a robust and theoretically grounded framework for fine-grained credit assignment, we acknowledge several limitations in our current study. Domain Specificity. The empirical evaluations in this work predominantly focus on highly complex mathematical …
- **Score V2：** Design Delta 2 / System Reach 2 / Durability 3 = **7/9**。
- **Books：** Integrate — already present and rechecked。

<a id="2605.03344"></a>

## 2605.03344 — RAG over Thinking Traces Can Improve Reasoning Tasks

- **原文：** https://arxiv.org/html/2605.03344v1（访问：2026-09-14）
- **审阅：** standard；exact-v1 valid; no withdrawal banner observed。
- **机制与 owner：** `AGENT-RAG`；reasoning RAG失败可能来自corpus类型，thinking trace经离线结构化T3可胜web corpus；改变检索对象与预算选择，需排查污染/公平性。。
- **Method：** 3 Methodology — We study how reasoning trajectories can be represented as effective retrieval units for reasoning-intensive tasks. The key idea is to view trajectory retrieval as a representation problem, where the same trace can be transformed into different retrieval-friendly forms. 3.1 Thinking …
- **Evaluation：** 4 Experimental Setup — 4.1 Thinking Trace Sources We construct multiple corpora of thinking trajectories generated by different LLMs and drawn from different problem collections. Here, we focus on a shared-corpus setting where previously generated traces are reused across different inference models. This setup …
- **Limit / non-proof：** Appendix E Limitations — This work has several limitations. First, we only study vanilla RAG. This choice is intentional: our goal is to test whether simple retrieval over thinking traces can help reasoning in the first place. We therefore leave more complex retrieval settings, …
- **Score V2：** Design Delta 2 / System Reach 1 / Durability 2 = **5/9**。
- **Books：** No Change — Existing Coverage。

<a id="2605.03346"></a>

## 2605.03346 — Provable Accuracy Collapse in Embedding-Based Representations under Dimensionality Mismatch

- **原文：** https://arxiv.org/html/2605.03346v1（访问：2026-09-14）
- **审阅：** standard；exact-v1 valid; no withdrawal banner observed。
- **机制与 owner：** `MODEL-EMBEDDING`；triplet可实现维度与压缩dimension存在最坏情形accuracy collapse/计算hardness，具体限定embedding降维可无损的解释，不能外推实测corpus必然崩塌。。
- **Method：** Embeddings and Training Procedure. — For the embeddings, we consider two variants: (i) Unconstrained embeddings , where parameters are unconstrained; (ii) Spherical embeddings , where after each optimization step all embeddings are projected onto the unit sphere. The latter setting resembles cosine-similarity–based representation learning. For …
- **Evaluation：** 4 Experiments — We provide synthetic experiments in two settings supporting Theorem 1.3 , which predicts that when the embedding dimension d d falls below a constant fraction of the ground-truth dimension D D , accuracy drops significantly and becomes comparable to the …
- **Limit / non-proof：** Information-Theoretic Limitations. — Our first result helps explain empirically-observed sharp drops in accuracy ( Takeshita et al., 2025 ; Tsukagoshi and Sasano, 2025 ) , via an information-theoretic lower bound for triplet embeddings under dimension mismatch up to a constant factor: Theorem 1.3 …
- **Score V2：** Design Delta 2 / System Reach 1 / Durability 2 = **5/9**。
- **Books：** No Change — Existing Coverage。

<a id="2605.03348"></a>

## 2605.03348 — Toward Structural Multimodal Representations: Specialization, Selection, and Sparsification via Mixture-of-Experts

- **原文：** https://arxiv.org/html/2605.03348v1（访问：2026-09-14）
- **审阅：** standard；exact-v1 valid; no withdrawal banner observed。
- **机制与 owner：** `MULTIMODAL-REPRESENTATION`；multimodal语义专家可选择/裁剪，reverse-U sparsity曲线提供表示共享与特化的具体tradeoff，需核验MoE机制不外推普适。。
- **Method：** 5 S3: A Modular and Structured Approach to Multimodal Representation Learning — To realize the structured representation principles outlined in Section 3 , we introduce S3, a three-stage framework for MMRL. Our goal is to construct representations that are Task-Sufficient and Information-Minimal , while also satisfying the structural constraints of latent concept …
- **Evaluation：** 6 Experiments — We evaluate our method on four multimodal benchmarks from the MultiBench ( Liang et al., 2021 ) , following its standardized evaluation protocol: MOSEI ( Bagher Zadeh et al., 2018 ) , MOSI ( Zadeh et al., 2016 ) , …
- **Limit / non-proof：** 2 A Fundamental Limitation of Existing Multimodal Representation Learning — We consider the self-supervised multimodal setting to analyze limitations of prior MMRL methods. For clarity, we focus on two modalities, denoted by the set ℳ = { 1 , 2 } {\cal M}=\{1,2\} , although the formulation and results naturally …
- **Score V2：** Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- **Books：** No Change — Existing Coverage。

<a id="2605.03351"></a>

## 2605.03351 — VLMaxxing through FrameMogging Training-Free Anti-Recomputation for Video Vision-Language Models

- **原文：** https://arxiv.org/html/2605.03351v1（访问：2026-09-14）
- **审阅：** deep；exact-v1 valid; no withdrawal banner observed。
- **机制与 owner：** `INFER-KV-CACHE`；same-video followup KV复用与fresh-video vision skip分开，并用paired drift与stage-share ceiling避免speedup相乘，直接改变视频cache验收。。
- **Method：** 3 Method — 3.1 Problem Setting We study three deployment regimes on frozen video-VLM stacks, plus a separate routing path used for mechanism validation: • First-pass visual pruning: skip or reduce vision-tower work before the rest of the model pays for it. • …
- **Evaluation：** 4 Experimental Setup — 4.1 Benchmarks and Workloads The paper uses three headline workload families plus one scale-out boundary lane, because the contribution is not a single benchmark trick and the protocols are not interchangeable. The routing mechanism is evaluated on sparse semantic-substitution holdouts: …
- **Limit / non-proof：** 9 Limitations and Reproducibility — The paper makes three kinds of claim, and each one breaks differently. For first-pass pruning, VideoMME is the clean holdout anchor, while MVBench and TOMATO keep timing caveats. Gemma supplies the cleanest measured sparse-vision cell: 32f short skips timed vision-tower …
- **Score V2：** Design Delta 2 / System Reach 2 / Durability 3 = **7/9**。
- **Books：** Integrate — applied and post-write audited。

<a id="2605.03353"></a>

## 2605.03353 — SkCC: Portable and Secure Skill Compilation for Cross-Framework LLM Agents

- **原文：** https://arxiv.org/html/2605.03353v1（访问：2026-09-14）
- **审阅：** standard；exact-v1 valid; no withdrawal banner observed。
- **机制与 owner：** `AGENT-PLATFORM`；typed SkIR分离skill语义与framework格式、编译期constraint检查，降低多skill×framework适配组合；静态trigger率不等同runtime授权保证。。
- **Method：** 3.1. Architecture Overview — Figure 2. SkCC ’s four-phase compilation pipeline. A unified SKILL.md source is parsed into a raw AST, transformed into a strongly-typed SkIR , validated and hardened by the Analyzer, and emitted into platform-native formats through polymorphic Emitters. A left-to-right pipeline …
- **Evaluation：** 3.3. Compile-time Semantic and Security Analysis — The Analyzer phase performs semantic validation and security enhancement on the SkIR , producing a validated IR with non-blocking diagnostic warnings. This phase executes a chain of five analyzers. Structural and Dependency Validation. Schema validation verifies name format (kebab-case, 1–64 …
- **Limit / non-proof：** 5. Conclusion — We presented SkCC , a skill compilation framework that introduces classical compiler design into agent skill development. Through a four-phase pipeline with a strongly-typed SkIR , Anti-Skill Injection, and polymorphic backend emission, SkCC achieves portable and secure skill deployment across …
- **Score V2：** Design Delta 2 / System Reach 1 / Durability 2 = **5/9**。
- **Books：** No Change — Existing Coverage。

<a id="2605.03354"></a>

## 2605.03354 — What Happens Inside Agent Memory? Circuit Analysis from Emergence to Diagnosis

- **原文：** https://arxiv.org/html/2605.03354v1（访问：2026-09-14）
- **审阅：** standard；exact-v1 valid; no withdrawal banner observed。
- **机制与 owner：** `AGENT-MEMORY`；small-model memory routing先于内容circuit、late hub被recruit而非新建，并有跨framework因果定位，改变SLM memory能力与诊断解释。。
- **Method：** 3 Method — 3.1 Agent Memory Pipeline The pipeline comprises three LLM operations: Write (extract facts from conversation), Manage (decide add/update/delete/none), and Read (answer from retrieved memory). Each is an independent forward pass with a stage-specific prompt. The pipeline processes sessions sequentially: each …
- **Evaluation：** Circuit analysis and scaling. — Circuit tracing with transcoders ( Dunefsky et al., 2024 ; Hanna et al., 2025 ) produces feature-level attribution graphs; automated circuit discovery methods ( Conmy et al., 2023 ) provide complementary graph-search approaches. Sparse feature circuits ( Marks et al., …
- **Limit / non-proof：** Appendix A Limitations — Our analysis covers one model family (Qwen-3), two memory frameworks, short factorized prompts (45–65 tokens), and MLP-traced circuits via per-layer transcoders. PLTs do not trace attention heads, and transcoder features are not guaranteed to be fully monosemantic: a feature we …
- **Score V2：** Design Delta 2 / System Reach 1 / Durability 2 = **5/9**。
- **Books：** No Change — Existing Coverage。

<a id="2605.03356"></a>

## 2605.03356 — POSTCONDBENCH: Benchmarking Correctness and Completeness in Formal Postcondition Inference

- **原文：** https://arxiv.org/html/2605.03356v1（访问：2026-09-14）
- **审阅：** deep；exact-v1 valid; no withdrawal banner observed。
- **机制与 owner：** `PLATFORM-EVALUATION-SYSTEM`；postcondition completeness通过可运行defect discrimination而非表面匹配，分离正确但弱约束与真实覆盖，直接改变coding-agent评价。。
- **Method：** 3 Methodology — 3.1 Benchmark Overview Our benchmark targets formal postcondition inference, evaluating whether approaches can generate precise and comprehensive postconditions from NL descriptions and/or code implementations. We construct a multilingual, repository-level dataset with automated evaluation capabilities. Formally, each PostcondBench instance is a …
- **Evaluation：** 3.1 Benchmark Overview — Our benchmark targets formal postcondition inference, evaluating whether approaches can generate precise and comprehensive postconditions from NL descriptions and/or code implementations. We construct a multilingual, repository-level dataset with automated evaluation capabilities. Formally, each PostcondBench instance is a tuple that captures …
- **Limit / non-proof：** Limitations — We exclude methods (or specific mutants) that require unsupported specification constructs or remain unkillable under the available tests. It is possible that this exclusion introduces bias in the PostcondBench evaluation of the affected behaviors, such as iterator or concurrency behaviors. …
- **Score V2：** Design Delta 3 / System Reach 1 / Durability 3 = **7/9**。
- **Books：** No Change — Existing Coverage。

<a id="2605.03361"></a>

## 2605.03361 — ReasonAudio: A Benchmark for Evaluating Reasoning Beyond Matching in Text-Audio Retrieval

- **原文：** https://arxiv.org/html/2605.03361v1（访问：2026-09-14）
- **审阅：** standard；exact-v1 valid; no withdrawal banner observed。
- **机制与 owner：** `MULTIMODAL-REPRESENTATION`；text-audio检索分离negation/order/overlap/duration，且MLLM backbone reasoning未随contrastive embedding保留，直接改变多模态检索评价和训练假设。。
- **Method：** 3. ReasonAudio Benchmark — We introduce ReasonAudio, a reasoning-intensive Text–Audio Retrieval benchmark constructed by synthesizing composite sounds as the audio corpus and generating search queries using predefined templates. The dataset is built through following three key stages. 3.1. Atomic Sound Collection To construct the …
- **Evaluation：** 4. Benchmarking SOTA Models on ReasonAudio — 4.1. Experimental Setup We evaluate three types of Text–Audio Retrieval approaches with ten SOTA models using ReasonAudio: (1) Two-Stage Text–Audio Retrieval. We evaluated a two-stage approach that sequentially applies audio-to-text models and text retrievers. Audio inputs are first converted into …
- **Limit / non-proof：** 6. Conclusion — This paper introduces ReasonAudio, the first reasoning-intensive benchmark for Text–Audio Retrieval. We evaluate three categories of audio retrieval systems and ten SOTA models, revealing critical limitations in existing approaches. All models perform poorly on sound matching and audio reasoning, with …
- **Score V2：** Design Delta 2 / System Reach 1 / Durability 2 = **5/9**。
- **Books：** No Change — Existing Coverage。

<a id="2605.03363"></a>

## 2605.03363 — Learning Reactive Dexterous Grasping via Hierarchical Task-Space RL Planning and Joint-Space QP Control

- **原文：** https://arxiv.org/html/2605.03363v1（访问：2026-09-14）
- **审阅：** standard；exact-v1 valid; no withdrawal banner observed。
- **机制与 owner：** `MULTIMODAL-EMBODIED-VLA`；high-level task-space RL and low-level joint-space QP separate semantic policy from physical safety commit。
- **Method：** II-A Model-Based Methods for Reactive Control and Grasping — Reactive control refers to the ability of a system to respond and adapt compliantly in real time to environmental changes and external disturbances. In contrast to simply tracking time-parametrized motions planned offline, reactive control relies on feedback-based motion generation and …
- **Evaluation：** VII Experimental Results — Fig. 4 : Simulation results demonstrating the reach-grasp-lift progression of the proposed framework. The top two rows show the 20-DoF 5F hand grasping (a) a toy airplane (ID: 072a) and (b) a pudding box (ID: 008). The bottom two rows …
- **Limit / non-proof：** VIII-D Discussion — To contextualize the empirical and architectural findings of this work, we address several fundamental questions arising from the design and applicability of our hybrid hierarchical control framework for reactive dexterous grasping. When is a hierarchical, multi-agent RL architecture necessary? Our …
- **Score V2：** Design Delta 2 / System Reach 1 / Durability 3 = **6/9**。
- **Books：** No Change — Existing Coverage。

<a id="2605.03373"></a>

## 2605.03373 — Learning Dynamics of Zeroth-Order Optimization: A Kernel Perspective

- **原文：** https://arxiv.org/html/2605.03373v1（访问：2026-09-14）
- **审阅：** standard；exact-v1 valid; no withdrawal banner observed。
- **机制与 owner：** `TRAIN-PRETRAINING`；ZO SGD eNTK由低维随机投影解释，近似误差依输出维数而非参数维数，直接挑战LLM ZO微调必受参数维度拖慢的解释。。
- **Method：** D.1 Group 1: LeNet Model, MNIST Dataset. — Our experiments start with some examples on the relatively low-dimensional LeNet ( d = 29,624 d=29,624 ) model trained on the MNIST dataset. Unless otherwise stated, we employ standard Gaussian perturbations u ∼ 𝒩 ⁡ ( 0 , I ) …
- **Evaluation：** Appendix D Experiment Setup and Extra Empirical Results — In this section, we provide more experiments setup details and empirical results to support our findings and conclusions in our main paper. To empirically validate our theoretical findings regarding the learning dynamics of ZO optimization, we conduct a series of …
- **Limit / non-proof：** 4 Trade-Offs, Limitations, and Future Work — As an explanatory study, this work primarily investigates the theoretical and empirical roles of the perturbation budget P P in ZO optimization under the standard empirical risk minimization (ERM) setting. Our analysis is grounded in supervised fine-tuning (SFT) tasks within …
- **Score V2：** Design Delta 2 / System Reach 1 / Durability 2 = **5/9**。
- **Books：** No Change — Existing Coverage。

<a id="2605.03375"></a>

## 2605.03375 — Tutti: Making SSD-Backed KV Cache Practical for Long-Context LLM Serving

- **原文：** https://arxiv.org/html/2605.03375v1（访问：2026-09-14）
- **审阅：** deep；exact-v1 valid; no withdrawal banner observed。
- **机制与 owner：** `INFER-KV-CACHE`；GPU KV object/io_uring/slack调度把SSD I/O提交从CPU关键链移出，直接改变offload瓶颈与TTFT/SLO权衡。。
- **Method：** 3. Design and Implementation — In this section, we introduce the design and implementation of Tutti . We first describe the GPU-native object abstraction that enables high-concurrency GPU direct access to KV cache using object semantics. We then explain how applications can efficiently submit and …
- **Evaluation：** 4. Evaluation — Figure 8 . End-to-end TTFT and ITL on Llama3-8B across LEval and LooGLE under two vLLM versions (v0.12.0 vs. v0.17.0) with the latest LMCache. As request rate increases, Tutti maintains the lowest and most stable latency curves, consistent with the …
- **Limit / non-proof：** 5. Conclusion and Future Work — In this paper, we presented Tutti, a GPU-centric, SSD-backed KV cache store for long-context LLM serving. Tutti removes CPU intervention from critical data and I/O control paths between GPU HBM and NVMe SSDs. By combining a GPU-centric object-storage design with …
- **Score V2：** Design Delta 2 / System Reach 2 / Durability 3 = **7/9**。
- **Books：** No Change — Existing Coverage。

<a id="2605.03378"></a>

## 2605.03378 — ARGUS: Defending LLM Agents Against Context-Aware Prompt Injection

- **原文：** https://arxiv.org/html/2605.03378v1（访问：2026-09-14）
- **审阅：** deep；exact-v1 valid; no withdrawal banner observed。
- **机制与 owner：** `PLATFORM-SECURITY`；context-dependent工具任务中action必须有benign evidence的因果支持，AgentLure/ARGUS区别仅授权与局部文本检测，具体新安全边界。。
- **Method：** 4.7 Audit Algorithm — Algorithm 1 ARGUS audit for a proposed tool call. Input: proposed call f ⁡ ( a 1 , … , a n ) f(a_{1},\ldots,a_{n}) , user query q q , IPG 𝒢 \mathcal{G} , invariants ℐ \mathcal{I} 1 if f …
- **Evaluation：** 3 The AgentLure Benchmark — We introduce AgentLure, a prompt-injection benchmark for evaluating LLM-agent defenses in the context-dependent regime. In AgentLure, legitimate actions depend on runtime observations rather than the user prompt alone, while attacks are embedded in the specific carriers that supply those observations …
- **Limit / non-proof：** 6 Discussion — We discuss the broader implications of our work and possible directions for future research. Appendix D provides simplified walkthroughs of ARGUS ’s running cases on AgentLure. 6.1 Implications The representative cases highlight three design lessons for defending context-dependent agent workflows. …
- **Score V2：** Design Delta 2 / System Reach 2 / Durability 3 = **7/9**。
- **Books：** No Change — Existing Coverage。

<a id="2605.03379"></a>

## 2605.03379 — Two Calls, Two Moments, and the Vote-Accuracy Curve of Repeated LLM Inference

- **原文：** https://arxiv.org/html/2605.03379v1（访问：2026-09-14）
- **审阅：** deep；exact-v1 valid; no withdrawal banner observed。
- **机制与 owner：** `PLATFORM-EVALUATION-SYSTEM`；two labeled calls仅识别两矩并约束fixed majority vote的sharp intervals，改变test-time预算规划；完整潜在分布仍不识别。。
- **Method：** 3 Repeated-call model — We now fix the notation used throughout the paper. Let Y i ∈ { − 1 , + 1 } Y_{i}\in\{-1,+1\} be the ground-truth label and let Y ^ i ​ j \widehat{Y}_{ij} be the output of repeated call j …
- **Evaluation：** 6 LLM experiments — The experiments use controlled LLM inference in the finite-vote setting. They compare two-call moment regions computed from the first two responses with empirical three- and five-vote accuracies obtained from repeated calls, and they summarize how the observed policies move between …
- **Limit / non-proof：** 7 Discussion — The paper separates repeated-inference planning into an identifiable two-call certification component and a parametric completion component. Two labeled calls identify mean accuracy and same-example correctness correlation; those two moments give sharp intervals [ L n , U n ] [L_{n},U_{n}] …
- **Score V2：** Design Delta 2 / System Reach 2 / Durability 3 = **7/9**。
- **Books：** No Change — Existing Coverage。

<a id="2605.03408"></a>

## 2605.03408 — Discovering Reinforcement Learning Interfaces with Large Language Models

- **原文：** https://arxiv.org/html/2605.03408v1（访问：2026-09-14）
- **审阅：** standard；exact-v1 valid; no withdrawal banner observed。
- **机制与 owner：** `TRAIN-RLHF`；从raw simulator state联合演化observation mapping和reward executable interface，单独一项跨域可灾难失败；不是仅reward生成已知原则，需原文核验交互消融。。
- **Method：** 4 Method — We address RL interface discovery using LLM guided evolutionary search. Given a task description and environment specification, the system synthesizes executable observation and reward space and optimizes them through iterative training feedback. Each interface consists of two executable programs operating …
- **Evaluation：** 4.3 Inner-Loop Evaluation and Fitness — The fitness of an interface F ⁡ ( ℐ ) F(\mathcal{I}) is determined by the performance of an agent π \pi trained from scratch within the induced MDP ℳ ℐ \mathcal{M}_{\mathcal{I}} . Evaluation Cascade. We also utilize a "short-budget" cascade …
- **Limit / non-proof：** 7 Limitations and Future Work — LIMEN relies on an external evaluation metric that measures true task success and guides interface evolution. In domains where such a reliable metric is unavailable or difficult to specify, the evolution may become much harder. In addition, the primary practical …
- **Score V2：** Design Delta 2 / System Reach 1 / Durability 2 = **5/9**。
- **Books：** No Change — Existing Coverage。

<a id="2605.03409"></a>

## 2605.03409 — Robust Agent Compensation (RAC): Teaching AI Agents to Compensate

- **原文：** https://arxiv.org/html/2605.03409v1（访问：2026-09-14）
- **审阅：** standard；exact-v1 valid; no withdrawal banner observed。
- **机制与 owner：** `AGENT-WORKFLOW`；用执行log驱动side-effect compensation而非LLM重试，跨framework recovery分支需核验哪些效果可补偿及不可逆边界。。
- **Method：** 5.5. Part 3: Ablation with High Reason Model — To understand how RAC behaves with higher reasoning, we have selected subset problems where frameworks ran into problems, and ran them three times with GPT-5.4, the most advanced model with full reasoning. We only selected problems that failed for this …
- **Evaluation：** 5. Evaluation — In the evaluation, as an RAC-based implementation, we ran benchmark prompts in a vanilla LangGraph ReAct Agent with RAC enabled via extension points. We evaluated RAC against the following approaches: (1) SagaLLM - state-of-the-art solution as discussed in ( Chang …
- **Limit / non-proof：** 6. Discussion — Comparing and contrasting LG, LG(PE), SagaLLM, and RAC: LG depends on ReAct loop for recovering from failures. While sometimes it can recover from failures and compensate to avoid leaving side effects, its behavior is highly dependent on the problem, the …
- **Score V2：** Design Delta 2 / System Reach 1 / Durability 3 = **6/9**。
- **Books：** No Change — Existing Coverage。

<a id="2605.03413"></a>

## 2605.03413 — Learning to Theorize the World from Observation

- **原文：** https://arxiv.org/html/2605.03413v1（访问：2026-09-14）
- **审阅：** standard；exact-v1 valid; no withdrawal banner observed。
- **机制与 owner：** `MULTIMODAL-WORLD-MODELS`；a world model represents explanations as executable latent programs consumed by a shared transition model。
- **Method：** Appendix F Model Hyperparameters — For reproducibility, we report the hyperparameters used in all experiments. The settings were guided by prior work and empirical validation to ensure stable training and consistent evaluation. We use largely shared hyperparameters across tasks, introducing task-specific configurations only when necessary, …
- **Evaluation：** 5 Experiments — Our experiments evaluate whether NEO can (1) discover latent primitive operations that are never directly observed during training and (2) explain dynamics arising from previously unseen program compositions. To this end, we introduce the Observation-to-Theory Induction Benchmark. 5.1 Observation to …
- **Limit / non-proof：** 6 Limitations & Discussion — This work should be viewed as an initial proof of concept for Learning-to-Theorize . The current formulation assumes a relatively small, discrete set of primitives and short program lengths, which limits its scalability to domains with long-horizon, continuous, or highly …
- **Score V2：** Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- **Books：** No Change — Existing Coverage。

<a id="2605.03425"></a>

## 2605.03425 — FIBER: A Differentially Private Optimizer with Filter-Aware Innovation Bias Correction

- **原文：** https://arxiv.org/html/2605.03425v1（访问：2026-09-14）
- **审阅：** deep；exact-v1 valid; no withdrawal banner observed。
- **机制与 owner：** `TRAIN-PRETRAINING`；DP noise先加入privatized gradient再filter，AdamW二阶矩须扣filtered-noise贡献而非未过滤variance；已核验顺序、校准及直接限制。。
- **Method：** 2.1 Differentially Private Optimization Methods — Most practical DP training algorithms use per-example gradient clipping and add Gaussian noise, resulting in DP-SGD and adaptive variants such as DP-Adam and DP-AdamW ( Abadi et al., 2016 ; Yu et al., 2024 ; Gilani et al., 2025 ) …
- **Evaluation：** 3.1 Problem Setup — Given a dataset 𝒟 = { ξ i } i = 1 N \mathcal{D}=\{\xi_{i}\}_{i=1}^{N} , we minimize empirical risk: min θ ∈ ℝ d ⁡ F ⁡ ( θ ) ≜ 1 N ​ ∑ i = 1 N f …
- **Limit / non-proof：** F.6 Limitations and Future Directions — Hardware-specific measurements. Our measurements are specific to RTX 4090 GPUs. Relative overheads may vary on different hardware: • TPUs : With specialized matmul units and compiler optimizations, overhead may decrease to 1.6-1.7x • CPUs : Limited parallelism may increase overhead …
- **Score V2：** Design Delta 3 / System Reach 2 / Durability 3 = **8/9**。
- **Books：** Integrate — already present and rechecked。

<a id="2605.03426"></a>

## 2605.03426 — Replacing Parameters with Preferences: Federated Alignment of Heterogeneous Vision-Language Models

- **原文：** https://arxiv.org/html/2605.03426v1（访问：2026-09-14）
- **审阅：** standard；exact-v1 valid; no withdrawal banner observed。
- **机制与 owner：** `TRAIN-DISTRIBUTED-TRAINING`；heterogeneous VLM clients share routed rewards/preferences rather than incompatible model parameters。
- **Method：** 4 Method — Framework Overview To address heterogeneous reward coordination in privacy-sensitive federated VLM alignment, our framework (Figure 2 ) employs a three-stage decentralized process that keeps sensitive labels and reward model parameters strictly on-device. First, to capture unique, domain-specific evaluation criteria, each …
- **Evaluation：** 5 Experiments — Experimental Settings Dataset. We construct a heterogeneous vision–language preference dataset from existing sources including POVID ( Zhou et al. 2024 ) , VLFeedback ( Li et al. 2023 ) , and MME-RealWorld ( Zhang et al. 2025 ) . Since …
- **Limit / non-proof：** 6 Conclusion — In this paper, we propose MoR, a federated alignment framework for heterogeneous vision-language models. Instead of aggregating model parameters, MoR coordinates client-specific preference signals through a routing-based Mixture-of-Rewards mechanism and optimizes the policy with GRPO. This design preserves local reward …
- **Score V2：** Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- **Books：** No Change — Existing Coverage。

<a id="2605.03441"></a>

## 2605.03441 — Exposing LLM Safety Gaps Through Mathematical Encoding:New Attacks and Systematic Analysis

- **原文：** https://arxiv.org/html/2605.03441v1（访问：2026-09-14）
- **审阅：** standard；exact-v1 valid; no withdrawal banner observed。
- **机制与 owner：** `PLATFORM-SECURITY`；数学jailbreak效果来自深层语义重构而非notation；规则格式对照失败具体分离攻击机制，需验证新旧模型边界。。
- **Method：** 3. Methodology — 3.1. Threat Model and Attack Pipeline We consider a black-box threat model in which the attacker has API-level access to both a processing model (a helper LLM used for encoding) and the target model under evaluation. The attacker submits text-only …
- **Evaluation：** Evaluation Benchmarks. — Standardized benchmarks are essential for reproducible and comparable evaluation of jailbreaking methods. HarmBench [ 10 ] provides 159 curated harmful behaviors spanning diverse categories—including malware generation, disinformation, and hate speech—with a standardized LLM-based judge protocol. JailbreakBench [ 5 ] offers …
- **Limit / non-proof：** Limitations. — Our study has several limitations. Attack success relies entirely on automated judging (GPT-5-Nano) without human evaluation; binary ASR does not capture whether outputs are truly actionable or only partial jailbreaks. The LLM-based vs. rule-based comparison is confounded by co-varying factors …
- **Score V2：** Design Delta 2 / System Reach 1 / Durability 2 = **5/9**。
- **Books：** No Change — Existing Coverage。

<a id="2605.03472"></a>

## 2605.03472 — Detecting Stealth Sycophancy in Mental-Health Dialogue with Dynamic Emotional Signature Graphs

- **原文：** https://arxiv.org/html/2605.03472v1（访问：2026-09-14）
- **审阅：** standard；exact-v1 valid; no withdrawal banner observed。
- **机制与 owner：** `PLATFORM-SECURITY`；empathy/fluency掩盖implicit sycophancy，clean matched/leakage controls与临床state方向评分分离抽取和judge，具体改变安全对话评价有效性。。
- **Method：** 3 Method — We propose Dynamic Emotional Signature Graphs (DESG), a model-agnostic offline evaluation framework for psychological AI. Given a dialogue window, DESG uses a large language model only as a structured state sensor to extract turn-level semantic, affective, and cognitive-distortion states, rather …
- **Evaluation：** 2.1 LLM-as-a-Judge and Automatic Evaluation — With the rapid development of large language models, automatic evaluation has increasingly shifted from reference-based text metrics to model-based judging. Traditional semantic metrics, such as SentenceBERT and BERTScore, provide useful measurements of embedding-level or token-level similarity, but they are not …
- **Limit / non-proof：** 5 Conclusion — This paper argues that clinical dialogue evaluation should move beyond surface empathy and black-box model judging. We introduced DESG, a structured offline evaluator that converts dialogue windows into clinical states, optionally represents them as directed state graphs, and scores them …
- **Score V2：** Design Delta 2 / System Reach 1 / Durability 2 = **5/9**。
- **Books：** No Change — Existing Coverage。

<a id="2605.03475"></a>

## 2605.03475 — WorldJen: An End-to-End Multi-Dimensional Benchmark for Generative Video Models

- **原文：** https://arxiv.org/html/2605.03475v1（访问：2026-09-14）
- **审阅：** deep；exact-v1 valid; no withdrawal banner observed。
- **机制与 owner：** `PLATFORM-EVALUATION-SYSTEM`；native-resolution, multi-dimensional video auditing exposes yes-bias and low-resolution evaluator failure。
- **Method：** 3 The WorldJen Framework — A high-level view of the two-phase pipeline used in this work is provided in Figure 1 . Phase A focuses on prompt curation, it produces a reusable, multi-dimensionally enriched prompt pool. Phase B takes that pool together with any set …
- **Evaluation：** 3.2 Phase B: Evaluation Engine — Figure 3 : Phase B evaluation engine. The curated prompt pool fans out in parallel into prompt-specific question generation and video generation. Both outputs feed the VLM Evaluator; scores aggregate into Bradley-Terry ratings combining into a final leaderboard. 3.2.1 Prompt-Specific …
- **Limit / non-proof：** 10 Limitations and Future Work — Human evaluation scale. Human annotation in this work focused on pairwise annotations § 5 . Dimension specific signals are harder to extract from this data as was observed in § 7 Table 6 . Dimension-specific human evaluation, where annotators score …
- **Score V2：** Design Delta 2 / System Reach 2 / Durability 3 = **7/9**。
- **Books：** No Change — Existing Coverage。

<a id="2605.03482"></a>

## 2605.03482 — MEMSAD: Gradient-Coupled Anomaly Detection for Memory Poisoning in Retrieval-Augmented Agents

- **原文：** https://arxiv.org/html/2605.03482v1（访问：2026-09-14）
- **审阅：** deep；exact-v1 valid; no withdrawal banner observed。
- **机制与 owner：** `PLATFORM-SECURITY`；纠正trigger-query协议使ASR变4倍，连续retrieval/anomaly gradient coupling仍有离散synonym loophole，明确安全纠错/保证边界。。
- **Method：** 4.1 Algorithm and formal definition — The key insight is that memory poisoning succeeds because adversarial entries are semantically close to victim queries; this closeness is itself a detectable signal. Definition 5 ( MemSAD detector) . Let ℋ = { q 1 , … , q …
- **Evaluation：** 6 Experiments — 6.1 Setup Vector memory. FAISS IndexFlatIP with L2-normalized all-MiniLM-L6-v2 embeddings ( d = 384 d=384 ). Benign corpus: | ℳ | = 1,000 |\mathcal{M}|=1{,}000 synthetic entries across 7 categories (task reminders, calendar events, user preferences, factual knowledge, document references, configuration …
- **Limit / non-proof：** 7 Discussion and limitations — Defense complementarity. No single defense dominates across access models α \alpha : watermarking fails when auto-storage bypasses ingestion control; MemSAD needs triggered calibration for AgentPoison ; proactive detection complements both. The defender’s uncertainty about α \alpha motivates composite portfolios ( …
- **Score V2：** Design Delta 2 / System Reach 2 / Durability 3 = **7/9**。
- **Books：** No Change — Existing Coverage。

<a id="2605.03505"></a>

## 2605.03505 — Multi-Agent Systems for Root Cause Analysis in Microservices

- **原文：** https://arxiv.org/html/2605.03505v1（访问：2026-09-14）
- **审阅：** deep；exact-v1 valid; no withdrawal banner observed。
- **机制与 owner：** `PLATFORM-MONITORING`；the same RCA agent falls from benchmark to real incidents because topology, multifactor causes and telemetry differ。
- **Method：** 3. LATS-RCA Architecture — LATS-RCA consists of two diagnostic agents (log and metrics), coordinated by a supervisor. Each agent operates over a distinct observability modality: the log agent explores log data, and the metric agent analyzes metric data and generates comparative visualizations. The supervisor …
- **Evaluation：** 4. Light-OAuth2 evaluation — We defined the following research questions: • RQ1. Diagnostic accuracy : How does LATS-RCA perform in terms of root cause diagnostic accuracy? • RQ2. Computational cost : What computational cost is associated with achieving this diagnostic accuracy? 4.1. Experiment setup …
- **Limit / non-proof：** 6. Threats to validity — External threats may arise from the gap between the LO2 benchmark evaluation and real-world production environment validation. Our LO2 evaluation is conducted on a small-team Java-based industrial MSS with injected, well-defined API-level error scenarios, which enables controlled benchmarking with relatively …
- **Score V2：** Design Delta 3 / System Reach 2 / Durability 3 = **8/9**。
- **Books：** No Change — Existing Coverage。

<a id="2605.03514"></a>

## 2605.03514 — Revisiting Graph-Tokenizing Large Language Models: A Systematic Evaluation of Graph Token Understanding

- **原文：** https://arxiv.org/html/2605.03514v1（访问：2026-09-14）
- **审阅：** standard；exact-v1 valid; no withdrawal banner observed。
- **机制与 owner：** `MODEL-EMBEDDING`；graph tokens含信息/被attention读取不等被LLM理解，instruction format/content变换及附加SFT未修复，直接分离表示可用性与下游推理。。
- **Method：** 2 The Unified Framework of GTokenLLMs — Figure 2 : The GTokenLLM framework, illustrating a stage-wise transformation of graph data from raw graph inputs (GI) to graph embeddings (GE), projected graph tokens (GT), and finally LLM-generated textual outputs (TO). 2.1 The Formal Definition of GTokenLLM Framework We …
- **Evaluation：** 3.2 Evaluation Settings of GTEval — In this paper, we evaluate 6 representative GTokenLLMs, including LLaGA ( Chen et al., 2024a ) , InstructGLM ( Ye et al., 2023 ) , GraphGPT ( Tang et al., 2024 ) , GraphTranslator ( Zhang et al., 2024 ) …
- **Limit / non-proof：** 5 Conclusion — Recently, GTokenLLMs have emerged as a mainstream paradigm for extending LLMs to TAGs. In this work, we first systematically examine whether these models fully understand graph tokens. By formalizing GTokenLLMs and introducing GTEval, an evaluation pipeline based on format- and …
- **Score V2：** Design Delta 2 / System Reach 1 / Durability 2 = **5/9**。
- **Books：** No Change — Existing Coverage。

<a id="2605.03534"></a>

## 2605.03534 — SURE-RAG: Sufficiency and Uncertainty-Aware Evidence Verification for Selective Retrieval-Augmented Generation

- **原文：** https://arxiv.org/html/2605.03534v1（访问：2026-09-14）
- **审阅：** deep；exact-v1 valid; no withdrawal banner observed。
- **机制与 owner：** `AGENT-RAG`；set-level缺hop/conflict不能由passage相关性相加判断，且controlled sufficiency与natural hallucination基线排名反转，明确RAG evaluator边界。。
- **Method：** IV Method — SURE-RAG comprises three components: pair-level claim-evidence verification, answer-level sufficiency aggregation, and selective answering, summarized in Figure 2 . The first scores each (claim, passage) pair locally; the second turns these local scores into a transparent answer-level feature vector; the third …
- **Evaluation：** II-B RAG Evaluation and Hallucination Detection — Two complementary lines evaluate RAG trustworthiness: RAGAS and ARES measure system-level dimensions such as context relevance, answer faithfulness, and answer relevance [ 6 , 7 ] , while SelfCheckGPT, RAGTruth, and HaluBench address context-grounded hallucination through self-consistency probing or labeled …
- **Limit / non-proof：** VII Discussion and Limitations — The experiments support SURE-RAG as a verifier for controlled evidence sufficiency, while also clarifying its limits. VII-A Interpretation The main result supports the premise that evidence sufficiency is distinct from retrieval relevance: SURE-RAG improves over pair-level pooling because it treats …
- **Score V2：** Design Delta 2 / System Reach 2 / Durability 3 = **7/9**。
- **Books：** No Change — Existing Coverage。

<a id="2605.03546"></a>

## 2605.03546 — ProgramBench: Can Language Models Rebuild Programs From Scratch?

- **原文：** https://arxiv.org/html/2605.03546v1（访问：2026-09-14）
- **审阅：** deep；exact-v1 valid; no withdrawal banner observed。
- **机制与 owner：** `PLATFORM-EVALUATION-SYSTEM`；以reference executable行为重建完整项目、agent fuzz测试不规定结构，揭示patch benchmark不能覆盖holistic软件设计，具体Agent评价增量。。
- **Method：** 5.2 Model-Generated Codebases — We highlight differences between model-generated solutions and the original human-written implementations. Figure 8: Confusion matrix of reference vs. model language. Each cell shows the percentage (and count) of runs per reference language. Models generally prefer, in descending order, Python, Go, …
- **Evaluation：** 2.2 Benchmark Construction — Next, we discuss our four-stage pipeline for converting open source GitHub repositories into ProgramBench task instances, as visualized in Figure 2 . All construction steps use the mini-SWE-agent 1 1 1 https://mini-swe-agent.com harness with Claude Sonnet 4.5, operating inside a …
- **Limit / non-proof：** 7 Discussion — Limitations. ProgramBench relies on a finite set of behavioral tests, which under-approximates each executable’s full specification. Evaluation therefore is a “lower bound” on correctness: solutions that fail are definitively incorrect, while those that pass may still diverge from the original …
- **Score V2：** Design Delta 2 / System Reach 2 / Durability 3 = **7/9**。
- **Books：** No Change — Existing Coverage。

<a id="2605.03547"></a>

## 2605.03547 — Erase Persona, Forget Lore: Benchmarking Multimodal Copyright Unlearning in Large Vision Language Models

- **原文：** https://arxiv.org/html/2605.03547v1（访问：2026-09-14）
- **审阅：** deep；exact-v1 valid; no withdrawal banner observed。
- **机制与 owner：** `PLATFORM-SECURITY`；multimodal unlearning must jointly test cross-variation forgetting and retained utility。
- **Method：** 3. CoVUBench — The primary design principle of the CoVUBench is to facilitate a safe yet realistic evaluation of copyright unlearning in LVLMs. To achieve this, our methodology is centered on the procedural generation of synthetic copyright content, thereby circumventing the legal and …
- **Evaluation：** 4. Experiments — Method ROUGE EM ( 𝒟 t ​ r ​ a ​ i ​ n \mathcal{D}_{train} ) EM ( 𝒟 t ​ e ​ s ​ t \mathcal{D}_{test} ) Acc. LLaVA-Phi-3B 76.63 99.65 98.16 74.86 LLaVA-1.5-7B 78.15 99.94 98.95 73.55 Table …
- **Limit / non-proof：** 5. Conclusion — We introduced CoVUBench , the first dedicated benchmark for evaluating multimodal copyright unlearning in LVLMs. Our framework enables a robust evaluation by introducing a visually diverse corpus spanning multiple domains and a diagnostic VQA set designed to probe both textual-level …
- **Score V2：** Design Delta 2 / System Reach 2 / Durability 3 = **7/9**。
- **Books：** No Change — Existing Coverage。

<a id="2605.03596"></a>

## 2605.03596 — Workspace-Bench 1.0: Benchmarking AI Agents on Workspace Tasks with Large-Scale File Dependencies

- **原文：** https://arxiv.org/html/2605.03596v1（访问：2026-09-14）
- **审阅：** deep；exact-v1 valid; no withdrawal banner observed。
- **机制与 owner：** `PLATFORM-EVALUATION-SYSTEM`；WorkspaceBench 把跨文件依赖、目录图状态与结果 rubric 纳入 agent 评估，明确暴露单工具/单文件基准不能覆盖的工作区成功条件。。
- **Method：** 4.5 Evaluation Framework — To evaluate agent performance on realistic workspace-grounded tasks, we designed a comprehensive evaluation framework (see Figure 6 ). Agent Initialization and Task Execution. Initially, the execution configurations for each agent are statically declared via a unified YAML file. Upon parsing …
- **Evaluation：** 2.2 Agent Benchmarks — To systematically evaluate the capabilities of LLM-based agents, numerous benchmarks have emerged. Based on their information dependency and environment interaction, existing efforts can be broadly categorized into four paradigms. Prompt-Driven Benchmarks. These benchmarks embed all requisite task information entirely within …
- **Limit / non-proof：** 7 Conclusion — In this paper, we introduce Workspace-Bench , a large-scale benchmark for evaluating Workspace Learning in autonomous AI agents, with a particular focus on cross-file dependency reasoning within realistic digital workspaces. Workspace-Bench bridges the gap between existing agent benchmarks and real-world …
- **Score V2：** Design Delta 2 / System Reach 3 / Durability 3 = **8/9**。
- **Books：** Integrate — already present and rechecked。

<a id="2605.03609"></a>

## 2605.03609 — Where Paths Split: Localized, Calibrated Control of Moral Reasoning in Large Language Models

- **原文：** https://arxiv.org/html/2605.03609v1（访问：2026-09-14）
- **审阅：** standard；exact-v1 valid; no withdrawal banner observed。
- **机制与 owner：** `MODEL-TRANSFORMER-LAYER`；branch-local residual steering uses a minimum-norm update rather than a global direction。
- **Method：** 3 Methodology — 3.1 CDR: Locating Branches in Transformers Attention Head Probing. To identify attention heads that are most predictive of each ethical framework e e , we train linear probes on the representations of each head. Let each Transformer layer contain H …
- **Evaluation：** 2 Problem Setup — Let f θ f_{\theta} be a model with L L transformer blocks. At inference time, the model receives a moral scenario p p and a user-specified preference vector α → = ( α U , α D ) \vec{\alpha}=(\alpha_{U},\alpha_{D}) defined …
- **Limit / non-proof：** Limitations — Pluralism in Moral Reasoning. Our work focuses on two canonical ethical frameworks: deontology and utilitarianism. While this binary setting enables precise control and analysis, future work could involve more pluralistic value systems, such as virtue ethics or care ethics, which …
- **Score V2：** Design Delta 2 / System Reach 1 / Durability 2 = **5/9**。
- **Books：** No Change — Existing Coverage。

<a id="2605.03619"></a>

## 2605.03619 — The Infinite Mutation Engine? Measuring Polymorphism in LLM-Generated Offensive Code

- **原文：** https://arxiv.org/html/2605.03619v1（访问：2026-09-14）
- **审阅：** standard；exact-v1 valid; no withdrawal banner observed。
- **机制与 owner：** `PLATFORM-SECURITY`；对 agent 生成行为等价攻击载荷的结构多样性与历史上下文成本做对照；可揭示依赖语法特征的检测边界及多样性提示不等于搜索效率，但需严格核验安全评估范围。。
- **Method：** 4. Methodology — This section details the experimental design, prompt architecture, and implementation details of our methodology. Figure 1 provides an overview of the pipeline, organized into three phases: a shared generation & validation module for stages 1–3 (left, steps \small1⃝–\small7⃝), the integration …
- **Evaluation：** 4.6. Analysis — The final phase of the methodology is the analysis stage (right block in Figure 1 ), where the orchestrator extracts the successfully validated payload.lua artifact (step \small12⃝). We then normalize these payloads to a canonical representation and extract two different …
- **Limit / non-proof：** 6. Discussion — The results of our work carry practical implications for the current landscape of malware detection. In particular, they contribute to better understand how LLM-driven malware development will provide generated payloads with polymorphic properties that make it harder to develop static …
- **Score V2：** Design Delta 2 / System Reach 1 / Durability 2 = **5/9**。
- **Books：** No Change — Existing Coverage。

<a id="2605.03623"></a>

## 2605.03623 — A Few-Step Generative Model on Cumulative Flow Maps

- **原文：** https://arxiv.org/html/2605.03623v1（访问：2026-09-14）
- **审阅：** standard；exact-v1 valid; no withdrawal banner observed。
- **机制与 owner：** `MULTIMODAL-GENERATIVE-PARADIGMS`；cumulative flow maps parameterize finite-time transport for few/one-step generation。
- **Method：** Flow Map Methods — The concept of the Flow Map originates from differential geometry and dynamical systems ( Arnold, 1992 ) , describing the evolution of points under a time-dependent vector field. Flow maps were initially developed in geophysical and hydrological modeling and have …
- **Evaluation：** 5. Experiments — In this section, we evaluate our method on five graphics tasks, demonstrating that, using our approach, few-step generation can be achieved with only a minor modification to the model’s time embedding and the training loss, without additional architectural components or …
- **Limit / non-proof：** 6. Additional Experiments and Discussion — Toy Example To better visualize the sample positions and prediction targets at each step under different formulations, we conduct a 2D toy experiment using an MLP on the standard Checkerboard and Two-Moons datasets with 4-step sampling. At each step, we …
- **Score V2：** Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- **Books：** No Change — Existing Coverage。

<a id="2605.03625"></a>

## 2605.03625 — Self-Improvement for Fast, High-Quality Plan Generation

- **原文：** https://arxiv.org/html/2605.03625v1（访问：2026-09-14）
- **审阅：** deep；exact-v1 valid; no withdrawal banner observed。
- **机制与 owner：** `AGENT-PLANNING`；graph search creates plan supervision while runtime search remains a separate optional owner。
- **Method：** 4 A Self-improving Plan Generator — Figure 2: Overview of SiGPlan . (a) The generative model is pretrained on plans generated by a domain-independent planner. (b) For a subset of m m problem instances, we sample candidate plans from our model, construct state graphs, and compute …
- **Evaluation：** 5 Experiments — Blocksworld Logistics Labyrinth Sokoban Method Compl. (%) Plan length Compl. (%) Plan length Compl. (%) Plan length Compl. (%) Plan length SiGPlan ( n loop = 15 n_{\text{loop}}{=}15 , N = 10 N{=}10 ) 99.40 41.86 (± 0.57) 99.30 146.12 …
- **Limit / non-proof：** 7 Discussion & Conclusions — Finding efficient algorithms for optimal and near-optimal planning has been a long-standing goal in AI. We presented SiGPlan , a self-improving generalized planning system that combines transformer models with symbolic graph search to iteratively improve plan quality, scaling favorably compared …
- **Score V2：** Design Delta 2 / System Reach 2 / Durability 3 = **7/9**。
- **Books：** Integrate — applied and post-write audited。

<a id="2605.03636"></a>

## 2605.03636 — Information Plane Analysis of Binary Neural Networks

- **原文：** https://arxiv.org/html/2605.03636v1（访问：2026-09-14）
- **审阅：** standard；exact-v1 valid; no withdrawal banner observed。
- **机制与 owner：** `WORLDVIEW-WHY-MODELS-LEARN`；明确有限样本 MI 估计饱和于 log2 N 的失效区间，并在可靠区间反证 compression 与 generalization 的普遍相关；属于训练解释方法的证据边界。。
- **Method：** III Methodology — III-A Binary Neural Networks In this work, we apply the sign function sign ⁡ x = { 1 if ​ x > 0 , 0 else \sgn\,x=\begin{cases}1&\text{if }x>0,\\ 0&\text{else}\end{cases} (1) to the activations of hidden fully connected (FC) layers with …
- **Evaluation：** IV Experimental Setups — We conduct IP analyses of BNNs on four datasets. For each dataset, different neural networks—varying in architecture and regularisation in the form of weight decay—are trained over 3,000 epochs. Each experiment is performed on three consecutive runs. 1 1 1 …
- **Limit / non-proof：** VII Discussion and Conclusions — In this work, we studied MI in BNNs , with the purpose of determining whether compression occurs during training, and whether compressed representations generalise better. While our experiments show that some form of compression during training is a prevalent phenomenon …
- **Score V2：** Design Delta 2 / System Reach 1 / Durability 2 = **5/9**。
- **Books：** No Change — Existing Coverage。

<a id="2605.03637"></a>

## 2605.03637 — Bridging the Embodiment Gap: Disentangled Cross-Embodiment Video Editing

- **原文：** https://arxiv.org/html/2605.03637v1（访问：2026-09-14）
- **审阅：** standard；exact-v1 valid; no withdrawal banner observed。
- **机制与 owner：** `MULTIMODAL-EMBODIED-VLA`；task and embodiment latents are disentangled for cross-embodiment video generation without claiming policy improvement。
- **Method：** 3 Method — In this section, we first describe our task formulation in Sec.3.1. Then we present the pipeline and the core of our proposed framework in Sec.3.2 and Sec.3.3. Sec.3.4 introduces our dataset construction. The overview of our framework is shown in …
- **Evaluation：** 4 Experiments — 4.1 Experimental Setup Implementation Details. We employ the pre-trained Wan2.1-VACE-1.3B ( Jiang et al., 2025 ) as the generative backbone. Our framework introduces three trainable components: a task encoder, an embodiment encoder, and a parameter-efficient adapter. Both encoders are lightweight …
- **Limit / non-proof：** 5 Conclusion — In this work, we addressed the key challenge of the distribution shift in learning from human video, where prior methods are often hindered by entangled representations that couple task semantics with human-specific kinematics. We introduced a generative framework for cross-embodiment …
- **Score V2：** Design Delta 2 / System Reach 1 / Durability 2 = **5/9**。
- **Books：** No Change — Existing Coverage。

<a id="2605.03639"></a>

## 2605.03639 — Diffusion Masked Pretraining for Dynamic Point Cloud

- **原文：** https://arxiv.org/html/2605.03639v1（访问：2026-09-14）
- **审阅：** standard；exact-v1 valid; no withdrawal banner observed。
- **机制与 owner：** `MULTIMODAL-REPRESENTATION`；指出 masked point-cloud decoder 使用真实 tube center 导致位置泄漏，并以 masked-center 扩散和位移分布目标修复；可改变预训练监督/评估泄漏的机制判断。。
- **Method：** 3 Method — Figure 3 : Structure of a VisMaskBlock . Visible tokens are updated by self-attention, while masked tokens query the visible stream through cross-attention. This asymmetric design preserves clean visible context and enables leakage-free inference for masked tubes. We present Di …
- **Evaluation：** 4 Experiments — 4.1 Downstream experiments 4D Action Segmentation on HOI4D. As reported in Table 1 , DiMP achieves consistent improvements over all prior pre-training approaches on HOI4D, with gains especially pronounced in the Edit and F1 metrics, reflecting that a probabilistic motion …
- **Limit / non-proof：** Appendix H Gradient propagation through the decoder: a known limitation and partial mitigation — Background. In masked autoencoding pretraining, the decoder is structurally inferior to the encoder from the perspective of downstream transfer: it is applied exclusively during pretraining and discarded at fine-tuning time. Any loss applied at the decoder output therefore has a …
- **Score V2：** Design Delta 2 / System Reach 1 / Durability 2 = **5/9**。
- **Books：** No Change — Existing Coverage。

<a id="2605.03644"></a>

## 2605.03644 — AdapShot: Adaptive Many-Shot In-Context Learning with Semantic-Aware KV Cache Reuse

- **原文：** https://arxiv.org/html/2605.03644v1（访问：2026-09-14）
- **审阅：** deep；exact-v1 valid; no withdrawal banner observed。
- **机制与 owner：** `INFER-KV-CACHE`；按 probe entropy 自适应选择 many-shot 数，并重编码位置以复用可重排 KV；直接改变 ICL 推理预算与缓存语义契约。。
- **Method：** 4 Method — AdapShot provides an adaptive inference framework that dynamically adjusts context scale based on the difficulty of input queries, enabling flexible and efficient allocation of computational resources. As illustrated in Figure 3 , AdapShot first constructs a semantically-aware global KV cache …
- **Evaluation：** 4.1 Probe-based Dynamic Evaluation — Many-Shot ICL deployment often falls into the misconception that "more examples are always better," leading to significant memory burden and inference latency, and even performance degradation. To address this, we propose a probe-based dynamic evaluation mechanism to assess the model’s …
- **Limit / non-proof：** 7 Limitations — Although AdapShot demonstrates superior performance in improving inference efficiency and dynamically adapting the number of shots, this study still presents certain limitations. Specifically, similar to traditional many-shot ICL methods, AdapShot relies on retrieving or constructing real data samples to serve …
- **Score V2：** Design Delta 2 / System Reach 2 / Durability 3 = **7/9**。
- **Books：** Integrate — already present and rechecked。

<a id="2605.03650"></a>

## 2605.03650 — Rethinking Temporal Consistency in Video Object-Centric Learning: From Prediction to Correspondence

- **原文：** https://arxiv.org/html/2605.03650v1（访问：2026-09-14）
- **审阅：** standard；exact-v1 valid; no withdrawal banner observed。
- **机制与 owner：** `MULTIMODAL-WORLD-MODELS`；以 frozen backbone 的身份特征加二分匹配取代 learned temporal transition；提供时序预测模块是否必要的可区分反证。。
- **Method：** 5 Method: Grounded Correspondence Framework — We introduce Grounded Correspondence, a framework that separates object discovery from temporal tracking. Existing methods use learned transition functions ϕ θ \phi_{\theta} and initialize slots without considering image content. Grounded Correspondence instead exploits instance-aware features from a frozen Vision Transformer …
- **Evaluation：** 4.1 The Empirical Redundancy of Temporal Predictors — We evaluate SlotContrast ( Manasyan et al., 2025 ) against a variant where the learned transitioner ϕ θ \phi_{\theta} is removed. In this ablation, queries for frame tt t are simply the slots from frame t − 1 t-1 : …
- **Limit / non-proof：** 7 Conclusion — We have examined the role of learned temporal predictors in video object-centric learning. Our analysis demonstrates that these modules function primarily as expensive solutions to a discrete correspondence problem rather than as models of physical dynamics. When slot initialization exploits …
- **Score V2：** Design Delta 2 / System Reach 1 / Durability 2 = **5/9**。
- **Books：** No Change — Existing Coverage。

<a id="2605.03667"></a>

## 2605.03667 — ELAS: Efficient Pre-Training of Low-Rank Large Language Models via 2:4 Activation Sparsity

- **原文：** https://arxiv.org/html/2605.03667v1（访问：2026-09-14）
- **审阅：** deep；exact-v1 valid; no withdrawal banner observed。
- **机制与 owner：** `TRAIN-PRETRAINING`；低秩训练中对 squared-ReLU activation 施加硬件 2:4 稀疏，连接激活内存与实际加速路径；需限定特定 FFN/模型尺度而非一般必要条件。。
- **Method：** 3 Methodology — In this section, we introduce ELAS that combines low-rank weights with activation 2:4 sparsity to achieve efficient training. ELAS integrates two key components: low-rank weight matrices and 2:4 sparsification of forward activations to enable hardware-accelerated sparse matrix multiplication. Figure 1 …
- **Evaluation：** 4 Experiments — We evaluate the performance of ELAS through comprehensive experiments on large language model pre-training. We conducted detailed ablation studies to further demonstrate ELAS’s effectiveness. All experiments were performed on NVIDIA 3090/A100 GPU. 4.1 Experiments setup Dataset. Our pre-training experiments utilize …
- **Limit / non-proof：** 5 Conclusion — In this paper, we presented ELAS, a novel framework that combines low-rank weight training with 2:4 structured activation sparsity for efficient LLMs pre-training. By applying the LORO framework with ReLU² activation functions and structured sparsity of forward activations, ELAS achieves …
- **Score V2：** Design Delta 2 / System Reach 2 / Durability 3 = **7/9**。
- **Books：** Integrate — already present and rechecked。

<a id="2605.03669"></a>

## 2605.03669 — FUS3DMaps: Scalable and Accurate Open-Vocabulary Semantic Mapping by 3D Fusion of Voxel- and Instance-Level Layers

- **原文：** https://arxiv.org/html/2605.03669v1（访问：2026-09-14）
- **审阅：** standard；exact-v1 valid; no withdrawal banner observed。
- **机制与 owner：** `MULTIMODAL-WORLD-MODELS`；a bounded voxel world state jointly owns dense semantics, instance identity and a sliding active window。
- **Method：** III Method — FUS3DMaps simultaneously maintains a dense semantic 3D voxel layer ℳ D \mathcal{M}^{\text{D}} with aggregated semantic patch-level embeddings and a sparser instance-level voxel layer ℳ I \mathcal{M}^{\text{I}} , constructed using a segmentation and image crop encoding strategy. As illustrated in Fig. …
- **Evaluation：** IV Experimental Setup — We demonstrate our proposed cross-layer semantic fusion method for two different sets of patch-level and image-level encoders Enc patch ​ ( ⋅ ) \text{Enc}_{\text{patch}}(\cdot) , Enc img ​ ( ⋅ ) \text{Enc}_{\text{img}}(\cdot) , which we detail in the following. Subsequently, …
- **Limit / non-proof：** VI Conclusions — We present an online open-vocabulary semantic mapping method that fuses embeddings of instance hypotheses with those of a dense semantic voxel layer. The proposed sliding window semantic mapping approach enables strong open-vocabulary semantic mapping by enriching instance-level embeddings with embeddings …
- **Score V2：** Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- **Books：** No Change — Existing Coverage。

<a id="2605.03675"></a>

## 2605.03675 — MEMTIER: Tiered Memory Architecture and Retrieval Bottleneck Analysis for Long-Running Autonomous AI Agents

- **原文：** https://arxiv.org/html/2605.03675v1（访问：2026-09-14）
- **审阅：** standard；exact-v1 valid; no withdrawal banner observed。
- **机制与 owner：** `AGENT-MEMORY`；分层 agent memory 的检索/整合机制与长会话基准，但摘要显露预填充来源、弱 full-context baseline 和 PPO 收益待验证；作为纠错/评估口径候选而非直接采纳性能结论。。
- **Method：** 3 Architecture — MemTier is implemented as an OpenClaw plugin ( [available upon acceptance] ) that intercepts two lifecycle hooks: before_prompt_build and agent_end . Figure 1 shows the full pipeline. Multi-agent isolation layer: Agent A (episodic, private) ↘ \searrow Agent B (episodic, private) …
- **Evaluation：** Memory benchmarks. — LoCoMo ( Maharana et al., 2024 ) evaluates conversational memory over 30-session dialogues. LongMemEval ( Wu and others, 2025 ) provides 500 manually crafted questions requiring retrieval from 53-session haystacks across five ability types: single-session recall, multi-session synthesis, temporal reasoning, …
- **Limit / non-proof：** Limitations. — (1) Attribution path: SGLang logprob attribution is code-complete but blocked by local hardware constraints on the evaluation machine; the lexical Jaccard fallback used in production is a coarse proxy. (2) RL weight dominance: While direct task-success reward ( + 1 …
- **Score V2：** Design Delta 2 / System Reach 1 / Durability 2 = **5/9**。
- **Books：** No Change — Existing Coverage。

<a id="2605.03677"></a>

## 2605.03677 — Uni-OPD: Unifying On-Policy Distillation with a Dual-Perspective Recipe

- **原文：** https://arxiv.org/html/2605.03677v1（访问：2026-09-14）
- **审阅：** deep；exact-v1 valid; no withdrawal banner observed。
- **机制与 owner：** `TRAIN-RLHF`；把 OPD 拆成 student-state 探索与 teacher token guidance 的 outcome 顺序一致性，提出校准；直接改变蒸馏反馈可靠性的机制边界。。
- **Method：** 3 Methodology — Figure 2: Overview of the Uni-OPD framework. ( Left ) Offline difficulty-aware and online correctness-aware data balancing promote student exploration. ( Right ) Outcome-guided margin calibration mechanism improves the reliability of teacher supervision. ( Middle ) The resulting student policy …
- **Evaluation：** 4 Experiments and Analysis — In this section, we conduct comprehensive experiments across both textual and multimodal domains to evaluate the effectiveness of Uni-OPD . We first detail the experimental configurations ( section 4.1 ). Subsequently, we assess how the proposed recipe improves OPD performance …
- **Limit / non-proof：** 5 Conclusion and Future Work — In this paper, we present Uni-OPD , a unified OPD framework that generalizes across LLMs and MLLMs. We identify two key bottlenecks for effective OPD: insufficient student exploration of informative states and unreliable teacher supervision for student rollouts. To address …
- **Score V2：** Design Delta 2 / System Reach 2 / Durability 3 = **7/9**。
- **Books：** Integrate — already present and rechecked。

<a id="2605.03702"></a>

## 2605.03702 — SprayCheck: Finding Gray Failures in Adaptive Routing Networks

- **原文：** https://arxiv.org/html/2605.03702v1（访问：2026-09-14）
- **审阅：** deep；exact-v1 valid; no withdrawal banner observed。
- **机制与 owner：** `PLATFORM-MONITORING`；利用 adaptive routing 流量喷洒统计和 flow 信息被动定位灰故障，并连接训练迭代内检测时延；直接影响大规模训练网络的可观测性与故障隔离。。
- **Method：** 3.1 Strawman Approach — In a symmetric network, where all links are healthy and available for AR, the source leaf switch sprays a flow evenly across all spines (as discussed in Section 2 ). In turn, the destination leaf switch receives the same number …
- **Evaluation：** 5 Evaluation — We evaluate SprayCheck’s detection quality, exhibiting how the accuracy depends on the network and workload, and its robustness to congestion control and concurrent network load. 5.1 Setup We evaluate SprayCheck both in a real-world testbed and with packet simulations. For …
- **Limit / non-proof：** 6 Limitations and Future Work — Weighted Packet Spraying Some AR spraying strategies do not distribute packets equally across all paths. If packet-sprayed flows coexist with preexisting, non-packet-sprayed flows, even spraying may cause imbalanced load. Weighted packet spraying allows certain queues to be preferred for spraying …
- **Score V2：** Design Delta 2 / System Reach 2 / Durability 3 = **7/9**。
- **Books：** No Change — Existing Coverage。

<a id="2605.03712"></a>

## 2605.03712 — Tempered Guided Diffusion

- **原文：** https://arxiv.org/html/2605.03712v1（访问：2026-09-14）
- **审阅：** standard；exact-v1 valid; no withdrawal banner observed。
- **机制与 owner：** `MULTIMODAL-GENERATIVE-PARADIGMS`；将 guided diffusion 改为 tempered SMC，按增量似然重采样并允许中途剪枝；把早期探索与最终轨迹计算预算连接，同时精确重建假设限制 posterior 一致性。。
- **Method：** Training-free conditional sampling. — Given an observation 𝒚 \bm{y} , we wish to sample from the posterior ( 2 ) without retraining the diffusion model. Training-free conditional diffusion uses the property that, if we adapt the reverse dynamics by replacing the unconditional score in …
- **Evaluation：** 5 Experiments — Setup. We evaluate TGD in a controlled two-dimensional inverse problem with a known posterior, and A-TGD on image inverse problems. The two-dimensional experiment uses a noisy elementwise absolute-value observation model and measures posterior approximation using sliced Wasserstein distance (SWD) [ …
- **Limit / non-proof：** 6 Discussion and Limitations — TGD separates clean-space particle inference from the conditional reconstruction module, yielding an idealized SMC construction while allowing practical implementations to reuse existing training-free diffusion solvers. The theoretical guarantee assumes exact stagewise reconstruction and an unpruned particle procedure; image experiments instead …
- **Score V2：** Design Delta 2 / System Reach 1 / Durability 2 = **5/9**。
- **Books：** No Change — Existing Coverage。

<a id="2605.03713"></a>

## 2605.03713 — SPEC CPU2026: Characterization, Representativeness, and Cross-Suite Comparison

- **原文：** https://arxiv.org/html/2605.03713v1（访问：2026-09-14）
- **审阅：** standard；exact-v1 valid; no withdrawal banner observed。
- **机制与 owner：** `PLATFORM-COST`；用微架构指标检验 SPEC CPU2026 对 agentic CPU pipeline 的代表性边界；可改变 agent 端到端成本中 CPU benchmark 代理是否可靠的判断。。
- **Method：** 3.1. Similarity Analysis Methodology — Our goal is to quantify workload similarity and extract representative subsets from SPEC CPU26 (and other analyzed suites), while accounting for cross-platform variability. We use a three-stage clustering pipeline that is consistent with prior work and widely used in benchmark …
- **Evaluation：** 3.1. Similarity Analysis Methodology — Our goal is to quantify workload similarity and extract representative subsets from SPEC CPU26 (and other analyzed suites), while accounting for cross-platform variability. We use a three-stage clustering pipeline that is consistent with prior work and widely used in benchmark …
- **Limit / non-proof：** 6. Conclusion — This paper presents the first comprehensive characterization of SPEC CPU26 and revisits the role of CPU-centric benchmarking in an era increasingly shaped by accelerators and ML workloads. Across nine platforms, we show that SPEC CPU26 broadens coverage relative to SPEC …
- **Score V2：** Design Delta 2 / System Reach 1 / Durability 2 = **5/9**。
- **Books：** No Change — Existing Coverage。

<a id="2605.03724"></a>

## 2605.03724 — Rethinking the Rank Threshold for LoRA Fine-Tuning

- **原文：** https://arxiv.org/html/2605.03724v1（访问：2026-09-14）
- **审阅：** deep；exact-v1 valid; no withdrawal banner observed。
- **机制与 owner：** `TRAIN-LORA`；区分平方损失 NTK 的充分 rank 阈值、交叉熵 PL 条件与二分类 bias 饱和，给出 rank-one 适用/不适用边界；不是普遍 LoRA rank=1 主张。。
- **Method：** 4 Theoretical refinement — This section sharpens the rank threshold for MSE in two stages and identifies its absence for CE. The capacity requirement is reduced from r ⁡ ( r + 1 ) / 2 > K ​ N r(r+1)/2>KN to a sharper …
- **Evaluation：** 5 Empirical evaluation — We test the loss-dependent threshold of Section 4 against the canonical fine-tuning regime that motivates the existing prescription, on real transformer encoders. Our experimental design mirrors the setup of Jang et al. (2024) : pretrained RoBERTa-base ( Liu et al., …
- **Limit / non-proof：** 6 Limitations — The theoretical results of Section 4 are stated under explicit assumptions. Theorem 1 ’s constant C ∗ ≈ 1.35 C^{*}\approx 1.35 rests on a Marchenko–Pastur self-consistency in the Gaussian-iid feature model, with c ≈ 0.020 c\approx 0.020 in C ∗ …
- **Score V2：** Design Delta 3 / System Reach 2 / Durability 3 = **8/9**。
- **Books：** Integrate — applied and post-write audited。

<a id="2605.03759"></a>

## 2605.03759 — Before Forgetting, Learn to Remember: Revisiting Foundational Learning Failures in LVLM Unlearning Benchmarks

- **原文：** https://arxiv.org/html/2605.03759v1（访问：2026-09-14）
- **审阅：** deep；exact-v1 valid; no withdrawal banner observed。
- **机制与 owner：** `PLATFORM-SECURITY`；指出 LVLM unlearning 基准在遗忘前未记住目标，提出先验证多跳/多图 memorization 及 exposure；直接修正 unlearning 成功判据。。
- **Method：** 4 Diagnosing Stage 1 Failure: Internal State Analysis — We posit that existing benchmarks fail to establish robust memorization during the initial fine-tuning (stage 1). To investigate this, we compare the base LLaVA-1.5-7b Liu et al. (2023) against models trained on FIUBench Ma et al. (2024) and MLLMU-Bench Liu …
- **Evaluation：** 7 Experiments — Model ROUGE ↑ \uparrow GPT ↑ \uparrow EM ↑ \uparrow EM t ↑ \uparrow LLaVA-1.5-7B 27.07 18.86 13.33 13.38 LLaVA-1.5-7B ∗ 97.19 95.18 91.50 81.33 LLaVA-1.5-13B 17.37 17.83 11.25 10.74 LLaVA-1.5-13B ∗ 98.92 98.05 96.37 87.98 Table 3: Performance comparison …
- **Limit / non-proof：** Limitations — A significant challenge in unlearning evaluation arises from scenarios with inherent dependencies between information to be forgotten and retained within the same data point. This is particularly acute in the multimodal domain, for instance, in real-world images containing multiple individuals …
- **Score V2：** Design Delta 3 / System Reach 2 / Durability 3 = **8/9**。
- **Books：** No Change — Existing Coverage。

<a id="2605.03762"></a>

## 2605.03762 — OracleProto: A Reproducible Framework for Benchmarking LLM Native Forecasting via Knowledge Cutoff and Temporal Masking

- **原文：** https://arxiv.org/html/2605.03762v1（访问：2026-09-14）
- **审阅：** deep；exact-v1 valid; no withdrawal banner observed。
- **机制与 owner：** `PLATFORM-EVALUATION-SYSTEM`；把 cutoff-aware 准入、工具时间遮蔽与内容泄漏检查分开，避免回溯预测被已知事实污染；可改变 forecasting eval 的信息边界与重现性。。
- **Method：** 3 Method — 3.1 Problem Formulation OracleProto evaluates the native forecasting capability of large language models under a bounded information environment. Each instance is a resolved event whose ground truth is hidden from the model and used only for scoring; the model must …
- **Evaluation：** 2.1 Forecasting Systems and Dynamic Benchmarks — The premise that LLMs can play a serious role in forecasting is settled, in the first instance, by Halawi et al. [ 3 ] , who show that retrieval-augmented language models approach the crowd aggregate of competitive forecasters on a …
- **Limit / non-proof：** 5 Discussion — Forecasting as a trainable capability. OracleProto’s current instantiation targets evaluation, yet each row of the dataset already carries the signal a trainer would need: a retrieval trace, a reasoning trajectory, and a final answer that together form a complete training …
- **Score V2：** Design Delta 2 / System Reach 2 / Durability 3 = **7/9**。
- **Books：** No Change — Existing Coverage。

<a id="2605.03769"></a>

## 2605.03769 — Nora: Normalized Orthogonal Row Alignment for Scalable Matrix Optimizer

- **原文：** https://arxiv.org/html/2605.03769v1（访问：2026-09-14）
- **审阅：** standard；exact-v1 valid; no withdrawal banner observed。
- **机制与 owner：** `TRAIN-PRETRAINING`；row-wise momentum 正交投影同时限制权重范数和角速度，以 Transformer Hessian 假设近似预条件；是 optimizer 几何、复杂度与稳定性边界的候选。。
- **Method：** B.1 Model and Training Configurations — Table 5 reports the detailed model and training configurations used in the 60M and 135M experiments. Both settings use context length 256, global batch size 512, cosine learning-rate decay, bf16 precision, gradient clipping at 1.0, evaluation every 1,000 steps, and …
- **Evaluation：** 4.2 Theoretical Analysis — We now analyze Nora as a scalable optimizer and establish non-convex convergence guarantees. For a matrix x ∈ ℝ m × n x\in\mathbb{R}^{m\times n} , define: ∥ x ∥ 1 , 2 := ∑ i = 1 m ∥ x …
- **Limit / non-proof：** 6 Conclusion — We introduce Nora, a normalized orthogonal row-alignment optimizer for scalable LLM training. Nora is motivated by the geometry of scale-invariant neural networks, where effective learning should mainly occur along angular rather than radial directions. By projecting momentum onto the row-wise …
- **Score V2：** Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- **Books：** No Change — Existing Coverage。

<a id="2605.03776"></a>

## 2605.03776 — Assessing the Impact of Noise and Speech Enhancement on the Intelligibility of Speech Codecs

- **原文：** https://arxiv.org/html/2605.03776v1（访问：2026-09-14）
- **审阅：** standard；exact-v1 valid; no withdrawal banner observed。
- **机制与 owner：** `MULTIMODAL-REPRESENTATION`；噪声条件下传统 speech codec 比 neural codec 更稳且 enhancement 改变排序；把饱和 intelligibility 与 listening effort 分开，是神经音频压缩取舍的反证。。
- **Method：** 2 Experiments — 2.1 Benchmarked Codecs Table 1: Codecs under test. CPU usage is measured on a single core of an Intel Core i7‑11700 at \SI 2.5kHz using publicly available implementations. Number of parameters is given for neural codecs when available. Codec kbps …
- **Evaluation：** 2 Experiments — 2.1 Benchmarked Codecs Table 1: Codecs under test. CPU usage is measured on a single core of an Intel Core i7‑11700 at \SI 2.5kHz using publicly available implementations. Number of parameters is given for neural codecs when available. Codec kbps …
- **Limit / non-proof：** 4 Conclusion — In this work, we conducted a crowdsourced evaluation of clean and noisy speech processed by multiple neural and classical speech codecs. We assessed speech intelligibility and listening effort and demonstrated that neural codecs are less noise robust than classical codecs. …
- **Score V2：** Design Delta 2 / System Reach 1 / Durability 2 = **5/9**。
- **Books：** No Change — Existing Coverage。

<a id="2605.03780"></a>

## 2605.03780 — Task Vector Geometry Underlies Dual Modes of Task Inference in Transformers

- **原文：** https://arxiv.org/html/2605.03780v1（访问：2026-09-14）
- **审阅：** standard；exact-v1 valid; no withdrawal banner observed。
- **机制与 owner：** `WORLDVIEW-WHY-MODELS-LEARN`；在受控 Transformer 中区分训练任务 Bayesian retrieval 与 OOD extrapolative learning 的表示子空间；为 ICL task-vector 解释提供明确实验/理论边界。。
- **Method：** 4 A mathematical framework for representation geometry — This section develops the mathematical framework used throughout the paper. Sec. 4.1 defines task vectors and four geometric properties of hidden states; Sec. 4.2 links these properties to Bayesian task retrieval, while Sec. 4.3 studies extrapolative task learning and shows …
- **Evaluation：** 3 Synthetic experiment setup — Data generation. In all synthetic experiments, we first draw a latent z z from a finite training set 𝒵 train ⊂ 𝒵 {\mathcal{Z}}_{\mathrm{train}}\subset{\mathcal{Z}} and then sample a sequence from the latent-specific distribution. E1. Rolling biased dice. Each latent z z …
- **Limit / non-proof：** 8 Limitations and Future Work — This work presents a modest attempt to bridge generalization and representation geometry in transformers. First, our analysis of E1 – E3 relies on the restrictive first-order Markov property on synthetic data; a more realistic setup may extend a single conditioning …
- **Score V2：** Design Delta 2 / System Reach 1 / Durability 2 = **5/9**。
- **Books：** No Change — Existing Coverage。

<a id="2605.03782"></a>

## 2605.03782 — What You Think is What You See: Driving Exploration in VLM Agents via Visual-Linguistic Curiosity

- **原文：** https://arxiv.org/html/2605.03782v1（访问：2026-09-14）
- **审阅：** standard；exact-v1 valid; no withdrawal banner observed。
- **机制与 owner：** `MULTIMODAL-WORLD-MODELS`；language-prediction error against later visual reality drives exploration that can revise an internal world model。
- **Method：** 3 Method — In this section, we propose GLANCE , a unified framework designed to transform the VLM agent’s internalized world modeling into a structured source of epistemic drive. As illustrated in Fig. 2 , the architecture consists of two parallel streams: an …
- **Evaluation：** 4 Experiment — In this section, we evaluate GLANCE against state-of-the-art VLM-RL baselines across five diverse agentic tasks. We aim to answer: (i) Can GLANCE facilitate effective exploration in sparse-reward environments? (ii) Does reasoning-driven curiosity improve the grounding of internalized world models? and …
- **Limit / non-proof：** 6 Discussion and Limitations — In this work, we demonstrate that grounding linguistic reasoning in visual reality creates a robust epistemic drive. Below, we discuss critical design choices, current limitations, and future directions. Backbone Update and Language Drift A central design choice in GLANCE is …
- **Score V2：** Design Delta 2 / System Reach 1 / Durability 2 = **5/9**。
- **Books：** No Change — Existing Coverage。

<a id="2605.03804"></a>

## 2605.03804 — ScrapMem: A Bio-inspired Framework for On-device Personalized Agent Memory via Optical Forgetting

- **原文：** https://arxiv.org/html/2605.03804v1（访问：2026-09-14）
- **审阅：** standard；exact-v1 valid; no withdrawal banner observed。
- **机制与 owner：** `AGENT-MEMORY`；把多模态 agent 记忆编码为图像页并随年龄降分辨率，以事件图保留语义；是存储压缩与可恢复细节/检索质量之间的新具体策略。。
- **Method：** 4 Method: ScrapMem — Figure 2: Overview of the ScrapMem. (1) Consolidation and Perception : Unifies heterogeneous records (images, videos, text) into hybrid representations via OCR and vision-to-text extraction. (2) EM-Graph Construction : Organizes nodes into an Episodic Memory Graph with event-centric paths (EM-Paths) …
- **Evaluation：** 5 Experiments and Results — # System Memory ATM-Bench Rep. QS R@10 Joint@10 N R O Upper / Lower Bounds 1 No-Evidence – 0.2 – – 0.0 0.0 0.6 2 Oracle DM 70.0 – – 81.8 69.3 61.9 3 Oracle SGM 77.8 – – 85.0 …
- **Limit / non-proof：** Limitations — ScrapMem relies on visual rendering and optical perception modules, whose performance may degrade under extremely aggressive optical forgetting or highly cluttered multimodal layouts. Additionally, the EM-Graph construction depends on LLM-based semantic extraction, which can introduce noise in event relation modeling. …
- **Score V2：** Design Delta 2 / System Reach 1 / Durability 2 = **5/9**。
- **Books：** No Change — Existing Coverage。

<a id="2605.03806"></a>

## 2605.03806 — ConRAD: Conformal Risk-Aware Neural Databases

- **原文：** https://arxiv.org/html/2605.03806v1（访问：2026-09-14）
- **审阅：** deep；exact-v1 valid; no withdrawal banner observed。
- **机制与 owner：** `AGENT-RAG`；在多跳 neural query 中按全局 risk budget 标定 operator 阈值并以 graph evidence bypass 推理；直接改变检索结果完整性与成本的组合保证，需核查有限样本含义。。
- **Method：** 4. The ConRAD Framework — We first show that independent per-operator calibration is provably wasteful, then introduce a scalarization strategy that reduces the k k -dimensional threshold search to a single parameter, and finally design the conformal gate operator that dynamically routes between retrieval and …
- **Evaluation：** 6. Experiments — We evaluate ConRAD on multi-hop EPFO queries over incomplete knowledge graphs, addressing four research questions: (RQ1) Validity: Does ConRAD satisfy user-specified recall targets across diverse query topologies and graph incompleteness levels? (RQ2) Precision: Does ConRAD’s risk-constrained optimization achieve precision competitive …
- **Limit / non-proof：** 7. Discussion — Marginal Guarantees and Exchangeability. ConRAD provides marginal guarantees, ensuring the recall target is satisfied on average across the query distribution rather than per individual query instance. Achieving strict conditional coverage is provably impossible without restrictive distributional assumptions or infinite calibration …
- **Score V2：** Design Delta 2 / System Reach 2 / Durability 3 = **7/9**。
- **Books：** No Change — Existing Coverage。

<a id="2605.03808"></a>

## 2605.03808 — Agentic-imodels: Evolving agentic interpretability tools via autoresearch

- **原文：** https://arxiv.org/html/2605.03808v1（访问：2026-09-14）
- **审阅：** standard；exact-v1 valid; no withdrawal banner observed。
- **机制与 owner：** `PLATFORM-EVALUATION-SYSTEM`；把工具可解释性定义为 agent 读字符串表示后可模拟行为，并以 autoresearch 优化该接口；可检验人类可解释工具不必然适合 agent 的边界。。
- **Method：** 3 Methods — The goal of Agentic-imodels is to automatically discover model classes that are both accurate and interpretable to LLMs. It does this using an agentic autoresearch loop that simultaneously optimizes predictive performance and a novel interpretability metric, using a coding agent …
- **Evaluation：** 4 Results — 4.1 Experimental setup Datasets. We evaluate predictive performance during the Agentic-imodels loop on 65 regression datasets, consisting of all the regression datasets from the OpenML TabArena suite [ 15 ] (7 datasets) and all the regression datasets from PMLB excluding …
- **Limit / non-proof：** Limitations. — One limitation of the study here is that our end-to-end ADS evaluations rely on LLM-as-judge for scoring, which may introduce some bias or artifacts (although notably the underlying ground-truth analysis is conducted by expert humans, making the judging task easier). …
- **Score V2：** Design Delta 2 / System Reach 1 / Durability 2 = **5/9**。
- **Books：** No Change — Existing Coverage。

<a id="2605.03812"></a>

## 2605.03812 — GPUBreach: Privilege Escalation Attacks on GPUs using Rowhammer

- **原文：** https://arxiv.org/html/2605.03812v1（访问：2026-09-14）
- **审阅：** deep；exact-v1 valid; no withdrawal banner observed。
- **机制与 owner：** `PLATFORM-SECURITY`；GPU Rowhammer 对 page table 的跨进程/CPU 权限影响直接挑战 GPU 多租户与 IOMMU 隔离假设；安全准入，仅研究防护边界与验证条件。。
- **Method：** IV Techniques for Page Table Massaging — To address the above challenges in page table massaging and understand where, how, and when page tables can be allocated, we develop the following techniques. IV-A Inspecting Page Tables To understand GPU page table layouts, we instrument the NVIDIA GPU …
- **Evaluation：** VI Exploitation Results — To assess the potential for exploitation with GPUBreach attacks, our evaluations answer the following questions: 1. Can we leverage Rowhammer bit-flips to tamper PTEs and escalate privilege on a GPU? ( Section VI-A ) 2. With our arbitrary GPU read …
- **Limit / non-proof：** VII Discussion and Limitations — Applicability to Other GPUs. Our exploits are demonstrated on the NVIDIA RTX A6000 GPU, a widely used workstation and cloud GPU previously shown to be susceptible to bit flips [ 11 ] . This is because the underlying Rowhammer vulnerability …
- **Score V2：** Design Delta 3 / System Reach 3 / Durability 3 = **9/9**。
- **Books：** Integrate — applied and post-write audited。

<a id="2605.03821"></a>

## 2605.03821 — RoboAlign-R1: Distilled Multimodal Reward Alignment for Robot Video World Models

- **原文：** https://arxiv.org/html/2605.03821v1（访问：2026-09-14）
- **审阅：** standard；exact-v1 valid; no withdrawal banner observed。
- **机制与 owner：** `MULTIMODAL-WORLD-MODELS`；video world model 的 reward 对齐与 sliding-window re-encoding 分别针对任务正确性和长程漂移；需分开同源 judge 与外部人评并限定 in-domain 收益。。
- **Method：** 3 Method — RoboAlign-R1 addresses two key challenges in robot video world models: reward misalignment during training and error accumulation during inference. RoboAlign-R1 unifies reward-aligned post-training and stabilized long-horizon decoding within a single framework. 3.1 Token-Based Robot Video World Model Our backbone (Figure …
- **Evaluation：** Stylized stability analysis. — We provide a simplified local error analysis that explains the qualitative window-size trade-off, rather than predicting exact gains. Let ε \varepsilon upper-bound the per-step token-space prediction error, δ q \delta_{q} the decode–re-encode quantization error, and α ∈ [ 0 , …
- **Limit / non-proof：** J.10 Limitations and Future Directions — We acknowledge several limitations of the current RoboAlign-Judge : • Dataset coverage. Although the current training corpus contains 10,000 samples spanning four robot datasets, coverage remains uneven across embodiments, environments, and failure modes. Expanding annotation density and generative-model diversity would …
- **Score V2：** Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- **Books：** No Change — Existing Coverage。

<a id="2605.03822"></a>

## 2605.03822 — KVerus: Scalable and Resilient Formal Verification Proof Generation for Rust Code

- **原文：** https://arxiv.org/html/2605.03822v1（访问：2026-09-14）
- **审阅：** standard；exact-v1 valid; no withdrawal banner observed。
- **机制与 owner：** `AGENT-WORKFLOW`；将跨文件依赖、lemma 语义及 toolchain version 纳入 proof RAG 状态并在版本变化时修复；直接影响代码 agent 正确性判据和可维护验证接口。。
- **Method：** 3. KVerus Design — In this section, we present the design of KVerus , detailing the architecture and functionality of its four main modules. The system is designed as a pipeline that systematically constructs, comprehends, and utilizes distinct types of knowledge to achieve robust, …
- **Evaluation：** 5. Evaluation — We evaluated KVerus in four crafted Verus benchmarks and two real-world Rust verification repositories and answered the following research questions (RQs): RQ1. How effective is KVerus for single-file verification? RQ2. How effective is KVerus for repository-level verification under cross-file dependencies? …
- **Limit / non-proof：** 6. Discussion — 6.1. Ensuring Specification Correctness Like most proof generation tools, KVerus assumes that formal specifications—such as preconditions and postconditions—are correct and well-defined. While this assumption often holds for crafted benchmarks, real-world verification frequently breaks it. Incorrect specifications not only block proof …
- **Score V2：** Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- **Books：** No Change — Existing Coverage。

<a id="2605.03824"></a>

## 2605.03824 — Reproducing Complex Set-Compositional Information Retrieval

- **原文：** https://arxiv.org/html/2605.03824v1（访问：2026-09-14）
- **审阅：** deep；exact-v1 valid; no withdrawal banner observed。
- **机制与 owner：** `AGENT-RAG`；受控 set-compositional retrieval 中强 dense/reasoning 检索从自然知识数据优势反转为低于 lexical；直接区分语义相似捷径与约束满足。。
- **Method：** Enhanced methods — We include four methods that explicitly target compositional or reasoning-intensive retrieval: • ReasonIR-8B ( Shao et al., 2025 ) fine-tunes LLaMA-3.1-8B as a bi-encoder using public retrieval data augmented with synthetic reasoning-intensive queries. It uses InfoNCE contrastive loss. • Set-Comp …
- **Evaluation：** 4. Experimental Setup — We evaluate a broad range of retrieval models spanning several paradigm families on multiple set-compositional benchmarks, considering six first stage rankers and four re-rankers. The first-stage retrievers are evaluated in a zero-shot setting—no model is fine-tuned on the target datasets …
- **Limit / non-proof：** Limitations. — LIMIT+ uses synthetic entities with explicit attribute lists, which simplifies the retrieval problem relative to natural text; its value lies in controlled diagnosis rather than as a standalone benchmark. Our re-ranking evaluation uses a curated candidate set that guarantees gold-document …
- **Score V2：** Design Delta 2 / System Reach 2 / Durability 3 = **7/9**。
- **Books：** No Change — Existing Coverage。

<a id="2605.03849"></a>

## 2605.03849 — Stream-R1: Reliability-Perplexity Aware Reward Distillation for Streaming Video Generation

- **原文：** https://arxiv.org/html/2605.03849v1（访问：2026-09-14）
- **审阅：** standard；exact-v1 valid; no withdrawal banner observed。
- **机制与 owner：** `MULTIMODAL-GENERATIVE-PARADIGMS`；同一 reward model 同时按 rollout 可靠性和时空梯度 saliency 重权 DMD，区分是否学习与学习何处；直接改变 video distillation 的监督契约。。
- **Method：** 3 Methodology — Figure 2 : Overview of Stream-R1. (a) The fake rollout from G θ G_{\theta} is scored by DMD networks f fake , f Real f_{\text{fake}},f_{\text{Real}} and the Stream R1 module; the distillation signal is modulated by an Inter-Reliability weight w …
- **Evaluation：** 4 Experiments — Figure 3 : Qualitative comparison on long video generation. For each pair, the top row is Reward Forcing and the bottom row is Stream-R1. 4.1 Implementation Details Stream-R1 is built upon the Reward Forcing [ 25 ] framework, using Wan2.1-T2V-1.3B …
- **Limit / non-proof：** 5 Conclusion — We present Stream-R1, a dynamic spatiotemporal reward-guided distillation framework that decomposes scalar reward signals into factored spatial and temporal saliency via reward-model gradient backpropagation, concentrating optimization intensity on quality-deficient regions and frames at no additional inference cost. Experiments show that …
- **Score V2：** Design Delta 2 / System Reach 1 / Durability 2 = **5/9**。
- **Books：** No Change — Existing Coverage。

<a id="2605.03858"></a>

## 2605.03858 — MCJudgeBench: A Benchmark for Constraint-Level Judge Evaluation in Multi-Constraint Instruction Following

- **原文：** https://arxiv.org/html/2605.03858v1（访问：2026-09-14）
- **审阅：** deep；exact-v1 valid; no withdrawal banner observed。
- **机制与 owner：** `PLATFORM-EVALUATION-SYSTEM`；逐 constraint 标注 yes/partial/no，并分解 stochastic 与 procedural inconsistency；直接修正整体 judge accuracy 不能证明局部约束可靠的评价边界。。
- **Method：** 3 MCJudgeBench — 3.1 Overview MCJudgeBench is a meta-evaluation benchmark for constraint-level judge evaluation in multi-constraint instruction following. Each instance is represented as x = ( I , y , C , L , 𝒫 y ) , x=(I,y,C,L,\mathcal{P}_{y}), where I I denotes …
- **Evaluation：** 4 Baseline Evaluation — 4.1 Baselines We evaluate a mix of proprietary and open-source LLM judges to provide representative baselines for judge performance on MCJudgeBench. Our proprietary judges are GPT-5.2 ( OpenAI, ) , Claude Sonnet 4.6 and Claude Haiku 4.5 ( Anthropic, ) …
- **Limit / non-proof：** Limitations — MCJudgeBench focuses on English-language multi-constraint instruction following and is constructed from two source benchmarks, ComplexBench and InFoBench. Its coverage therefore does not extend to all instruction following task distributions or languages. Although we include controlled perturbations over the candidate response …
- **Score V2：** Design Delta 2 / System Reach 2 / Durability 3 = **7/9**。
- **Books：** No Change — Existing Coverage。

<a id="2605.03862"></a>

## 2605.03862 — Correct Is Not Enough: Training Reasoning Planners with Executor-Grounded Rewards

- **原文：** https://arxiv.org/html/2605.03862v1（访问：2026-09-14）
- **审阅：** deep；exact-v1 valid; no withdrawal banner observed。
- **机制与 owner：** `AGENT-PLANNING`；planner trace reward 乘以 frozen executor 的 measured uplift，区别看似合理与可消费的中间推理；直接连接 reasoning artifact 和下游因果效用。。
- **Method：** 3 Method — TraceLift trains reasoning traces as executor-consumable intermediate artifacts in a fixed planner-executor protocol. In this section, we first describe TraceLift-Groups , the grouped reason-only supervision data used to learn trace-quality judgments. We then introduce TraceLift training framework, which uses scores …
- **Evaluation：** 4 Experiments — 4.1 Experimental setup Models and training objectives. We train TraceLift on Qwen2.5-7B, Llama3.1-8B, and Qwen3-4B model families [ 36 , 8 , 35 ] . For the main policy Group Relative Policy Optimization (GRPO) experiments, all Qwen2.5-7B, Llama3.1-8B, and Qwen3-4B …
- **Limit / non-proof：** 5 Conclusion — In this paper, we introduced TraceLift , a planner-executor framework that trains reasoning trajectories as executor-consumable intermediate artifacts. TraceLift trains a reasoning planner with verifier feedback on frozen-executor outputs and a Reason RM score weighted by measured executor uplift. We …
- **Score V2：** Design Delta 2 / System Reach 2 / Durability 3 = **7/9**。
- **Books：** No Change — Existing Coverage。

<a id="2605.03869"></a>

## 2605.03869 — On Adaptivity in Zeroth-Order Optimization

- **原文：** https://arxiv.org/html/2605.03869v1（访问：2026-09-14）
- **审阅：** deep；exact-v1 valid; no withdrawal banner observed。
- **机制与 owner：** `TRAIN-PRETRAINING`；反证高维 ZO gradient 缺少坐标异质性时 ZO-Adam 无收敛优势，以单标量适配代替逐坐标状态；直接改变无梯度微调的内存/优化判断。。
- **Method：** B.2 Adaptive Zeroth-Order Methods — To enhance convergence and robustness, adaptive ZO algorithms have incorporated techniques inspired by first-order optimization. ZO-AdaMM ( Chen et al., 2019 ) and ZEMA ( Nazari et al., 2020 ) introduced adaptive step sizes based on first and second moment …
- **Evaluation：** 2 Problem Setup and Notation — Notation . We adopt the following conventions. Vectors are denoted by bold lowercase letters ( e.g. , 𝐱 \mathbf{x} , 𝐲 \mathbf{y} ). Matrices are denoted by bold uppercase letters ( e.g. , 𝐖 \mathbf{W} , 𝐀 \mathbf{A} , 𝐁 …
- **Limit / non-proof：** 6 Discussion and Future Work — Please find a discussion of relevant related work in Appendix B . Our results show that well-tuned ZO-SGD can match or outperform adaptive methods like ZO-Adam, due to the lack of coordinate-wise structure in ZO gradients in high dimensions, which …
- **Score V2：** Design Delta 2 / System Reach 2 / Durability 3 = **7/9**。
- **Books：** No Change — Existing Coverage。

<a id="2605.03871"></a>

## 2605.03871 — EvoLM: Self-Evolving Language Models through Co-Evolved Discriminative Rubrics

- **原文：** https://arxiv.org/html/2605.03871v1（访问：2026-09-14）
- **审阅：** deep；exact-v1 valid; no withdrawal banner observed。
- **机制与 owner：** `TRAIN-RLHF`；以 checkpoint temporal contrast 共演 discriminative rubrics 与 policy，奖励依赖 frozen small judge；可检验 self-generated supervision 的反馈闭环与外部先验边界。。
- **Method：** Cross-method comparison. — Table 12 compares all methods at their final training step. Reported values are averages over 100 evaluation prompts. Table 12: Aggregate rubric statistics at final training step. Co-evolving methods with the alternate prompt and main prompt produce rubrics that are …
- **Evaluation：** 3 Experiments — Experiments are structured around three questions: (1) Are trained rubric generators better than prompting, and does co-evolving training improve over sequential training (Section 3.2 )? (2) Do learned rubrics generalize across domains, policy architectures, and judges (Section 3.3 )? (3) …
- **Limit / non-proof：** Limitations — EvoLM has been validated on general-purpose post-training data; behavior on domain-specialized mixtures such as medicine or law is an open question. The rubric enrichment mechanism is most clearly observed in tasks with verifiable intermediate steps, and its effect on purely …
- **Score V2：** Design Delta 2 / System Reach 2 / Durability 3 = **7/9**。
- **Books：** No Change — Existing Coverage。

<a id="2605.03884"></a>

## 2605.03884 — QKVShare: Quantized KV-Cache Handoff for Multi-Agent On-Device LLMs

- **原文：** https://arxiv.org/pdf/2605.03884v1（访问：2026-09-14）
- **审阅：** deep；exact-v1 valid; no withdrawal banner observed。
- **机制与 owner：** `AGENT-MULTI-AGENT`；以量化 KV CacheCard 携带跨 agent latent context 并注入 cache，改变 handoff 表示、校验和重 prefill 代价；存档摘要明显修订，必须回到 exact-v1 限定原始证据。。
- **Method：** official exact-v1 PDF; method sections were recovered and checked in the prior exact-v1 packet
- **Evaluation：** official exact-v1 PDF; experimental setup/results were checked in the prior exact-v1 packet
- **Limit / non-proof：** official exact-v1 PDF; scope and limitation boundary were checked in the prior exact-v1 packet
- **Score V2：** Design Delta 2 / System Reach 2 / Durability 3 = **7/9**。
- **Books：** Integrate — already present and rechecked。

<a id="2605.03903"></a>

## 2605.03903 — CC-OCR V2: Benchmarking Large Multimodal Models for Literacy in Real-world Document Processing

- **原文：** https://arxiv.org/html/2605.03903v1（访问：2026-09-14）
- **审阅：** deep；exact-v1 valid; no withdrawal banner observed。
- **机制与 owner：** `PLATFORM-EVALUATION-SYSTEM`；document-model evaluation attributes failure to acquisition conditions instead of hiding it in aggregate accuracy。
- **Method：** 3 CC-OCR v2 — In this section, we formalize the evaluation task of CC-OCR v2 in Sec. 3.1 and then present detailed statistics of the proposed benchmark in Sec. 3.2 . The data curation process is described in Sec. 3.3 . Finally, we compare …
- **Evaluation：** 5 Results and Analysis — This section presents a comprehensive evaluation of representative LMMs on CC-OCR v2 , with further analyses across tracks and document types. 5.1 Overall Performance Table 3 presents the benchmark results of representative on-device and on-server LMMs across five document understanding …
- **Limit / non-proof：** 6 Conclusion — We present CC-OCR v2 , a comprehensive and challenging benchmark for evaluating Large Multimodal Models on real-world document processing. By unifying five OCR-centric tasks and incorporating diverse document types with realistic distortions, CC-OCR v2 exposes substantial performance disparities across models, …
- **Score V2：** Design Delta 2 / System Reach 2 / Durability 3 = **7/9**。
- **Books：** No Change — Existing Coverage。

<a id="2605.03907"></a>

## 2605.03907 — Steer Like the LLM: Activation Steering that Mimics Prompting

- **原文：** https://arxiv.org/html/2605.03907v1（访问：2026-09-14）
- **审阅：** standard；exact-v1 valid; no withdrawal banner observed。
- **机制与 owner：** `MODEL-TRANSFORMER-LAYER`；发现 prompt steering 的干预随 token 强弱变化，以 activation-conditioned 系数蒸馏而非固定向量；可解释 activation steering 与 prompting 的机制差距。。
- **Method：** 3.4 Towards a More Faithful PSR Architecture — When analyzing on which tokens prompt steering exerts strong interventions, we observe distinct patterns (see Appendix A.2 for more analysis). This suggests that the prompt steering’s intervention strength could be decoded from the activations themselves. We therefore propose to relax …
- **Evaluation：** 4 Experimental Setup — 4.1 Benchmarks We carry out experiments on three benchmarks that evaluate steering long-form text generation. Persona Steering: Persona Vectors. To assess the effectiveness of the PSR models in steering LLMs towards a personality trait, we use the framework from Chen …
- **Limit / non-proof：** 6 Conclusion — We proposed a framework for studying the connection between prompting and activation steering by formulating prompt steering as a form of activation steering and distilling its behavior on instances where it is successful into simpler, interpretable models. Our analysis revealed …
- **Score V2：** Design Delta 2 / System Reach 1 / Durability 2 = **5/9**。
- **Books：** No Change — Existing Coverage。

<a id="2605.03936"></a>

## 2605.03936 — The Counterexample Game: Iterated Conceptual Analysis and Repair in Language Models

- **原文：** https://arxiv.org/html/2605.03936v1（访问：2026-09-14）
- **审阅：** standard；exact-v1 valid; no withdrawal banner observed。
- **机制与 owner：** `AGENT-REFLECTION`；counterexample-repair 长迭代只增长冗长而不增准确率，LM judge 接受率约人类两倍；直接反证自我修复迭代与评价器的可靠性。。
- **Method：** Methods — We study the iterative refinement of conceptual analyses through a counterexample-repair loop. A conceptual analysis proposes necessary and sufficient conditions for a concept (e.g., “To lie is to say something when you don’t believe it’s true”). A chain begins with …
- **Evaluation：** Experimental Conditions — Each chain was run in one of two conditions: memoryless (each step sees only the current analysis) or with-history (each step sees the full prior chain of counterexamples and repairs). For the mixed-model experiments, we ran 50 iterations per concept …
- **Limit / non-proof：** Discussion — For generations, philosophers have proposed and refined concepts iteratively—often leading to better conceptual analyses. In our Counterexample Game, we do not see similar long-term improvement over iterations, only longer definitions. Of course, an apples-to-apples comparison would require asking humans to …
- **Score V2：** Design Delta 2 / System Reach 1 / Durability 2 = **5/9**。
- **Books：** No Change — Existing Coverage。

<a id="2605.03937"></a>

## 2605.03937 — MiniMind-O Technical Report: An Open Small-Scale Speech-Native Omni Model

- **原文：** https://arxiv.org/html/2605.03937v1（访问：2026-09-14）
- **审阅：** standard；exact-v1 valid; no withdrawal banner observed。
- **机制与 owner：** `MULTIMODAL-REPRESENTATION`；a small open omni model exposes the semantic bridge, audio-codec buffer and multimodal sequence interfaces。
- **Method：** 3 Model Architecture — Figure 3: Training sequence format for Thinker and Talker. Text supervision is applied to the Thinker response tokens, while audio supervision is applied to target Mimi code positions. Reference-code regions are used as conditioning context rather than loss targets. Figure …
- **Evaluation：** 6 Evaluation — The evaluation is built around consistency properties that are easy to miss in demos. For each prompt, the model produces Thinker text and Talker audio. The audio is transcribed by Qwen3-ASR-Flash, and the transcript is compared with the Thinker text. …
- **Limit / non-proof：** 7 Discussion and Limitations — The main lesson from MiniMind-O is that the omni loop has a meaningful small-model regime. A full text–speech–image loop can be made public and inspectable at roughly 0.1B active parameters; the training data can be released in a form that …
- **Score V2：** Design Delta 2 / System Reach 1 / Durability 2 = **5/9**。
- **Books：** No Change — Existing Coverage。

<a id="2605.03941"></a>

## 2605.03941 — A Benchmark for Interactive World Models with a Unified Action Generation Framework

- **原文：** https://arxiv.org/html/2605.03941v1（访问：2026-09-14）
- **审阅：** standard；exact-v1 valid; no withdrawal banner observed。
- **机制与 owner：** `MULTIMODAL-WORLD-MODELS`；以统一 action-generation 接口评价不同互动 world model 的距离、轨迹与记忆，区分视频视觉质量和可交互物理能力。。
- **Method：** 3.2.1 Action Generation Framework — This is a unified and comprehensive framework. The design and definition of the Action Generation Framework support inputs from any modality of world models, enabling the design of action tasks and guiding the generation of world models. Specifically, it consists …
- **Evaluation：** 3.3 Evaluation Metrics — 3.3.1 Generation Quality Image Quality. We evaluate low-level visual distortions by calculating the normalized average MUSIQ ( Ke et al., 2021 ) score across all frames to reflect fundamental rendering fidelity. Brightness Consistency. It is designed to quantify the temporal …
- **Limit / non-proof：** 5 Conclusion and Future Work — iWorld-Bench is a unified benchmark specifically designed for interactive world models, integrating a multi-dimensional evaluation framework. It systematically evaluates model performance across diverse worlds through six types of interactive tasks and reveals the limitations of current models in terms of …
- **Score V2：** Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- **Books：** No Change — Existing Coverage。

<a id="2605.03945"></a>

## 2605.03945 — Integrating Feature Correlation in Differential Privacy with Applications in DP-ERM

- **原文：** https://arxiv.org/html/2605.03945v1（访问：2026-09-14）
- **审阅：** deep；exact-v1 valid; no withdrawal banner observed。
- **机制与 owner：** `PLATFORM-SECURITY`；CorrDP 按敏感/非敏感特征相关性放宽隐私定义并选择梯度噪声；直接涉及 DP utility 改善究竟来自算法还是保证变弱的安全边界。。
- **Method：** 2 CorrDP: setup and mechanisms — Let 𝒳 \mathcal{X} be the data domain where each point X ∈ 𝒳 ⊆ ℝ m X\in\mathcal{X}\subseteq\mathbb{R}^{m} can be partitioned as X = ( X 𝒮 , X 𝒰 ) ⊤ X=(X^{\mathcal{S}},X^{\mathcal{U}})^{\top} , where 𝒮 \mathcal{S} is the indices of …
- **Evaluation：** 5 Numerical experiments — In this section, we empirically demonstrate that CorrDP achieves a better privacy-utility tradeoff than standard DP for empirical risk minimization. We use CorrDP -SGD ( Algorithm 1 ) as the foundational algorithm across different experimental setups, and compare the utility …
- **Limit / non-proof：** 6 Discussion — In this work, we studied CorrDP , a relaxed notion of differential privacy that incorporates feature correlation across partitioned sensitive and insensitive features. We showed how this notion can be applied to the DP-ERM and DP-SGD algorithms. Our theoretical results …
- **Score V2：** Design Delta 3 / System Reach 2 / Durability 3 = **8/9**。
- **Books：** Integrate — applied and post-write audited。

<a id="2605.03952"></a>

## 2605.03952 — MOSAIC-Bench: Measuring Compositional Vulnerability Induction in Coding Agents

- **原文：** https://arxiv.org/html/2605.03952v1（访问：2026-09-14）
- **审阅：** deep；exact-v1 valid; no withdrawal banner observed。
- **机制与 owner：** `PLATFORM-SECURITY`；coding agent 分阶段无害 tickets 可组合成漏洞，deterministic exploit oracle 与累计 diff reviewer 分开；直接揭露单请求对齐无法保证全任务安全。。
- **Method：** Verifiable evaluation framework. — A two-layer harness pairing agentic chain construction with three independent verification gates (per-stage diff, reviewer-ensemble verdict, end-to-end oracle exploitability). The framework is adaptable (any Docker app + a chain design call per chain) and verifiable (deterministic PoC oracles).
- **Evaluation：** Verifiable evaluation framework. — A two-layer harness pairing agentic chain construction with three independent verification gates (per-stage diff, reviewer-ensemble verdict, end-to-end oracle exploitability). The framework is adaptable (any Docker app + a chain design call per chain) and verifiable (deterministic PoC oracles).
- **Limit / non-proof：** 7 Limitations, Ethics, and Responsible Release — Limitations. 8 of 10 substrates are at full scale; Spring (3 chains) and Laravel (3 chains) are pilot. Substrates outside web-app boilerplate (Rust services, .NET, mobile, embedded, OS kernels, ML pipelines) are not represented. The construction council (§ 3.3 ) …
- **Score V2：** Design Delta 2 / System Reach 3 / Durability 3 = **8/9**。
- **Books：** No Change — Existing Coverage。

<a id="2605.03953"></a>

## 2605.03953 — Transformers with Selective Access to Early Representations

- **原文：** https://arxiv.org/html/2605.03953v1（访问：2026-09-14）
- **审阅：** standard；exact-v1 valid; no withdrawal banner observed。
- **机制与 owner：** `MODEL-TRANSFORMER-LAYER`；把 first-layer value residual 复用从固定连接改为 token/head/context gate，连接早期表征访问、模型深度与开销；是 Transformer 架构具体机制。。
- **Method：** 3 Methodology — Previous work exposes V 1 V_{1} through layer-wise scalar coefficients, making early-value access uniform across tokens and heads within a layer ( Zhou et al., 2025 ) . To enable more dynamic input-aware gating, we replace the static scalar λ …
- **Evaluation：** 4 Experiments — We organize our evaluation around the central claim of this paper: selective access to early value representations provides an efficient alternative to dense cross-layer connectivity, with particular benefits for in-context retrieval and language-modeling performance. We therefore begin with retrieval-intensive benchmarks, …
- **Limit / non-proof：** Limitations. — The SAE-based categories should be interpreted as a coarse analysis tool rather than a definitive semantic labeling of early representations. The Llama-2 tokenizer produces many subword fragments and byte-level artifacts, which limits the granularity of linguistic categories. In addition, the …
- **Score V2：** Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- **Books：** No Change — Existing Coverage。

<a id="2605.03971"></a>

## 2605.03971 — Logical Consistency as a Bridge: Improving LLM Hallucination Detection via Label Constraint Modeling between Responses and Self-Judgments

- **原文：** https://arxiv.org/html/2605.03971v1（访问：2026-09-14）
- **审阅：** standard；exact-v1 valid; no withdrawal banner observed。
- **机制与 owner：** `PLATFORM-EVALUATION-SYSTEM`；用 response 与 self-judgment 的语义标签关系约束双视图 feature mutual learning，显式连接神经不确定性与判断一致性；需核验同源误差不会被逻辑形式掩盖。。
- **Method：** 4 Proposed Method: LaaB — Figure 2: Overall architecture of LaaB . Given a user query and corresponding response, LaaB first performs (a) Response Hallucination Modeling, extracting intrinsic features from the response generation to capture implicit uncertainty. (b) Self-Judgment Hallucination Modeling introduces a meta-judgment process …
- **Evaluation：** 5 Experiments — 5.1 Experimental Settings Datasets. We utilize four widely used datasets for factualness hallucination detection: TriviaQA, MMLU, NQ_Open, and HaluEval (Appendix A.1 ). For each dataset, we 1) prompt the LLM to generate responses to the given query; 2) prompt the …
- **Limit / non-proof：** Limitations — In this paper, we propose the integrated framework LaaB to combine the signals from LLMs’ intrinsic patterns and self-judgments for hallucination detection. Despite its effectiveness, we identify the following limitations: 1) To obtain the self-judgment from the LLMs, we force …
- **Score V2：** Design Delta 2 / System Reach 1 / Durability 2 = **5/9**。
- **Books：** No Change — Existing Coverage。

<a id="2605.03984"></a>

## 2605.03984 — Flow Sampling: Learning to Sample from Unnormalized Densities via Denoising Conditional Processes

- **原文：** https://arxiv.org/html/2605.03984v1（访问：2026-09-14）
- **审阅：** standard；exact-v1 valid; no withdrawal banner observed。
- **机制与 owner：** `MULTIMODAL-GENERATIVE-PARADIGMS`；对无归一化 energy 目标以 noise-conditioned denoising drift 学采样，减少 energy evaluation 并扩展流形；是 data-free diffusion/flow 训练机制。。
- **Method：** 3 Flow Sampling — In contrast to flow matching, we are interested in the data free settings, but our goal is similar. Given a score function of the target ∇ log ⁡ q ​ ( x 1 ) = ∇ r ​ ( x …
- **Evaluation：** 6 Experiments — 6.1 Synthetic Energy Functions We evaluate Flow Sampling on standard synthetic n n -particle energy benchmarks ( Köhler et al., 2020 ; Midgley et al., 2023 ; Klein et al., 2024 ; Akhound-Sadegh et al., 2024b ) : a 2D …
- **Limit / non-proof：** 6.5 Discussion on model efficiency — Training computational cost per a single exploration, followed by a training phase Algorithm 1 is composed of three primary components: i) Number of energy gradient evaluations ii) Number of function evaluations (NFE (Train)) to sample X 1 θ ¯ ∼ …
- **Score V2：** Design Delta 2 / System Reach 1 / Durability 2 = **5/9**。
- **Books：** No Change — Existing Coverage。

<a id="2605.03998"></a>

## 2605.03998 — EQUITRIAGE: A Fairness Audit of Gender Bias in LLM-Based Emergency Department Triage

- **原文：** https://arxiv.org/html/2605.03998v1（访问：2026-09-14）
- **审阅：** standard；exact-v1 valid; no withdrawal banner observed。
- **机制与 owner：** `PLATFORM-EVALUATION-SYSTEM`；性别 counterfactual、group parity 与 outcome calibration 分离，揭露低 calibration gap 仍有定向偏差和干预模型依赖性；安全评估反证。。
- **Method：** 3 Methods — 3.1 Data Source Two linked datasets from PhysioNet [ 51 ] were used: MIMIC-IV-ED [ 13 ] contains ∼ \sim 425,000 emergency department stays at Beth Israel Deaconess Medical Center (BIDMC), Boston, MA, between 2011 and 2019. The database comprises …
- **Evaluation：** Ablation conditions. — The primary counterfactual swaps both the gender token and the patient’s first name. To disentangle these effects, three ablation conditions were evaluated for two Profile-A models (Gemini-3-Flash and DeepSeek-V3.1, selected because they exhibit the panel’s clearest directional female-undertriage signal). Each …
- **Limit / non-proof：** 5.1 Limitations — Several limitations should be considered. First, MIMIC-IV-ED represents a single academic medical center (Beth Israel Deaconess, Boston); the patient population, triage practices, and documentation patterns may not generalize to community EDs or other regions. However, the counterfactual design controls for …
- **Score V2：** Design Delta 2 / System Reach 1 / Durability 2 = **5/9**。
- **Books：** No Change — Existing Coverage。

<a id="2605.04018"></a>

## 2605.04018 — Rethinking Reasoning-Intensive Retrieval: Evaluating and Advancing Retrievers in Agentic Search Systems

- **原文：** https://arxiv.org/html/2605.04018v1（访问：2026-09-14）
- **审阅：** standard；exact-v1 valid; no withdrawal banner observed。
- **机制与 owner：** `AGENT-RAG`；multi-aspect gold 与 agentic retrieval 区分单 passage 排名和互补 evidence portfolio，并按该目标构建正负训练样本；直接修正 reasoning retrieval 的评价目标。。
- **Method：** 5.2 RTriever Training Details — From one million MS MARCO queries we randomly sample 140K, and the synthesis pipeline generates 140K complete (query, positives, negatives) bundles after filtering. For each training step, we pair every query with one randomly-sampled positive passage and one randomly-sampled negative …
- **Evaluation：** Agentic Search System and Evaluation. — In parallel, agentic search systems ( e.g., DeepResearch) combine LLM planning with iterative search, reading, and synthesis to tackle complex queries Chen et al. (2025) ; Yang et al. (2025b) ; Wu et al. (2025) ; Shao et al. (2025a) …
- **Limit / non-proof：** Limitations and Future Work — Bright-Pro builds upon the StackExchange subset of Bright , which currently covers seven expert domains. However, this scope may not fully capture the diversity and complexity of real-world, reasoning-intensive retrieval scenarios. Future research could extend our work by incorporating a …
- **Score V2：** Design Delta 2 / System Reach 2 / Durability 2 = **6/9**。
- **Books：** No Change — Existing Coverage。

<a id="2605.04036"></a>

## 2605.04036 — OpenSeeker-v2: Pushing the Limits of Search Agents with Informative and High-Difficulty Trajectories

- **原文：** https://arxiv.org/html/2605.04036v1（访问：2026-09-14）
- **审阅：** standard；exact-v1 valid; no withdrawal banner observed。
- **机制与 owner：** `TRAIN-SFT`；只用高信息/高难度轨迹 SFT 对比重 CPT/RL search agent，明确图规模、工具集和低步过滤；可反证训练阶段复杂性是搜索能力必要条件。。
- **Method：** 2 Methodology and Results — 2.1 Methodology We introduce OpenSeeker-v2 , an upgraded search-agent training framework based on supervised fine-tuning (SFT). Our central hypothesis is that, given sufficiently difficult and information-rich training data, a straightforward SFT objective is enough to induce strong long-horizon search and …
- **Evaluation：** 2 Methodology and Results — 2.1 Methodology We introduce OpenSeeker-v2 , an upgraded search-agent training framework based on supervised fine-tuning (SFT). Our central hypothesis is that, given sufficiently difficult and information-rich training data, a straightforward SFT objective is enough to induce strong long-horizon search and …
- **Limit / non-proof：** 3 Conclusion — In this report, we share that when fueled by high-quality data of high-difficulty and richness, a search agent trained with simple SFT could rival the performance of agents trained with extensive resources. Specifically, we share three simple yet effective modifications …
- **Score V2：** Design Delta 2 / System Reach 1 / Durability 2 = **5/9**。
- **Books：** No Change — Existing Coverage。

<a id="2605.04039"></a>

## 2605.04039 — Safety and accuracy follow different scaling laws in clinical large language models

- **原文：** https://arxiv.org/html/2605.04039v1（访问：2026-09-14）
- **审阅：** deep；exact-v1 valid; no withdrawal banner observed。
- **机制与 owner：** `PLATFORM-EVALUATION-SYSTEM`；区分平均 accuracy 与高风险/矛盾/过度自信随模型、检索和context的变化，显示更大/更多计算非自动更安全；临床评估范围需严格限定。。
- **Method：** Materials and Methods — Ethics statement The study was conducted in accordance with relevant guidelines and regulations. RadSaFE-200 was constructed from previously published radiology question sets from the RadioRAG [ 41 ] and RaR [ 46 ] studies, together with newly curated text-only questions …
- **Evaluation：** Results — All analyses use the pooled 200-question RadSaFE-200 benchmark, with no stratification by source subset. For each model response, the selected option was mapped to correctness and to the predefined option-level safety labels, yielding high-risk error, unsafe answer, and evidence-contradiction outcomes. …
- **Limit / non-proof：** Discussion — Using SaFE-Scale on RadSaFE-200, this study shows that clinical LLM safety cannot be inferred from accuracy alone [ 16 , 31 ] . Across 34 models and six deployment conditions, the largest improvement in both performance and safety came not …
- **Score V2：** Design Delta 3 / System Reach 2 / Durability 3 = **8/9**。
- **Books：** No Change — Existing Coverage。
