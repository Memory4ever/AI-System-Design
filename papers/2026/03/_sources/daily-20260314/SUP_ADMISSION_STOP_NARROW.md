# 有界具名线索：八项完整Atom题摘

mar14_supplement；仅03-14增量Mar13自然日。只选八真实压缩/表示/隐私/评价线索，非41/51/149配额。实际读既存官方Atom完整title/summary/原版本与日期；不授精确v1正文、评分、Books或firstpublic。当前v2/v3要恢复必要早版本，不比全史。

## 11625 — MedPruner: Training-Free Hierarchical Token Pruning for Efficient 3D Medical Image Understanding in Vision-Language Models

SUP_TOPIC_MODEL.raw / http://arxiv.org/abs/2603.11625v2 / published=2026-03-12T07:37:00Z / updated=2026-06-25T12:30:03Z

完整AB：While specialized Medical Vision-Language Models (VLMs) have achieved remarkable success in interpreting 2D and 3D medical modalities, their deployment for 3D volumetric data remains constrained by significant computational inefficiencies. Current architectures typically suffer from massive anatomical redundancy due to the direct concatenation of consecutive 2D slices and lack the flexibility to handle heterogeneous information densities across different slices using fixed pruning ratios. To address these challenges, we propose MedPruner, a training-free and model-agnostic hierarchical token pruning framework specifically designed for efficient 3D medical image understanding. MedPruner introduces a two-stage mechanism: an Inter-slice Anchor-based Filtering module to eliminate slice-level temporal redundancy, followed by a Dynamic Information Nucleus Selection strategy that achieves adaptive token-level compression by quantifying cumulative attention weights. Extensive experiments on three 3D medical benchmarks and across three diverse medical VLMs reveal massive token redundancy in existing architectures. Notably, MedPruner enables models such as MedGemma-1.5 to maintain or even exceed their original performance while retaining fewer than 5\% of visual tokens, thereby reducing visual-token overhead and validating the necessity of dynamic token selection for practical clinical deployment. Our code is available at https://github.com/CUHK-AIM-Group/MedPruner.

准备者初判：P：slice-anchor过滤+累积attention动态核选择，非固定slice预算；当前v2不当Marchv1机制，必要精确早版后核。

## 11881 — Bielik-Minitron-7B: Compressing Large Language Models via Structured Pruning and Knowledge Distillation for the Polish Language

SUP_TOPIC_MODEL.raw / http://arxiv.org/abs/2603.11881v1 / published=2026-03-12T12:57:03Z / updated=2026-03-12T12:57:03Z

完整AB：This report details the creation of Bielik-Minitron-7B, a compressed 7.35B parameter version of the Bielik-11B-v3.0 model, specifically optimized for European languages. By leveraging a two-stage compression methodology inspired by the NVIDIA Minitron approach, we combined structured hybrid pruning and knowledge distillation to reduce the model's parameter count by 33.4%, from 11.04B to 7.35B. We utilized the NVIDIA Model Optimizer for structural pruning and the NVIDIA NeMo Framework for logit-based distillation for quality recovery. Following distillation, the model underwent a rigorous alignment pipeline consisting of Supervised Fine-Tuning (SFT), Direct Preference Optimization (DPO-P), and Reinforcement Learning (GRPO). Our final model successfully recovered approximately 90% of the baseline model's performance while providing up to 50% inference speedup. This approach demonstrates an efficient pathway to create language models for less-represented languages, preserving the original model quality while reducing inference deployment costs.

准备者初判：EX：明确复用Minitron/ModelOptimizer/NeMo剪枝蒸馏再SFT/DPO/GRPO，语言转移/局部数字未给新可比边界；不是按Polish领域关闭。

## 12208 — ForensicZip: More Tokens are Better but Not Necessary in Forensic Vision-Language Models

SUP_TOPIC_MODEL.raw / http://arxiv.org/abs/2603.12208v1 / published=2026-03-12T17:30:49Z / updated=2026-03-12T17:30:49Z

完整AB：Multimodal Large Language Models (MLLMs) enable interpretable multimedia forensics by generating textual rationales for forgery detection. However, processing dense visual sequences incurs high computational costs, particularly for high-resolution images and videos. Visual token pruning is a practical acceleration strategy, yet existing methods are largely semantic-driven, retaining salient objects while discarding background regions where manipulation traces such as high-frequency anomalies and temporal jitters often reside. To address this issue, we introduce ForensicZip, a training-free framework that reformulates token compression from a forgery-driven perspective. ForensicZip models temporal token evolution as a Birth-Death Optimal Transport problem with a slack dummy node, quantifying physical discontinuities indicating transient generative artifacts. The forensic scoring further integrates transport-based novelty with high-frequency priors to separate forensic evidence from semantic content under large-ratio compression. Experiments on deepfake and AIGC benchmarks show that at 10\% token retention, ForensicZip achieves $2.97\times$ speedup and over 90\% FLOPs reduction while maintaining state-of-the-art detection performance.

准备者初判：P：语义saliency丢forensic背景→birth-death OT slack与高频prior选择，重新评压缩支集，不授物理真值/速度。

## 12222 — HiAP: A Multi-Granular Stochastic Auto-Pruning Framework for Vision Transformers

SUP_TOPIC_MODEL.raw / http://arxiv.org/abs/2603.12222v3 / published=2026-03-12T17:45:38Z / updated=2026-08-17T10:08:20Z

完整AB：Vision Transformers require significant computational resources and memory bandwidth, severely limiting their deployment on resource-constraint hardware. Most structured pruning methods reduce theoretical cost effectively, yet they typically operate at a single structural granularity and depend on multi-stage pipelines with importance ranking, auxiliary solvers or post-hoc magnitude thresholding, followed by a separate fine-tuning phase to recover accuracy. We propose Hierarchical Auto-Pruning (HiAP), which casts ViT pruning as a single budget-aware learning problem and jointly allocates sparsity across four granularities in one end-to-end phase. HiAP introduces stochastic Gumbel-Sigmoid gates at macro level (attention heads and FFN blocks) and micro level (intra-head dimensions and FFN neurons), and trains them against the task loss together with an analytical MAC cost term. The budget coefficient steers the network to a target compute level while the gates gradually harden into a dense, smaller sub-network at convergence. It does not require importance heuristics, ranking metrics, auxiliary solvers or secondary fine-tuning. On ImageNet, HiAP compresses DeiT-Base to 7.4G MACs at 80.88% top-1 and DeiT-Small to 3.1G at 79.33%, competitive with substantially more complex pipelines at matched compute. The structurally pruned network can be accelerated natively on stock kernels, and more than 90% of the theoretical MAC reduction is realized as measured throughput on an A100.

准备者初判：P：四粒度stochastic gates/MAC budget联合学习→稀疏分派与原生执行条件；当前v3不当Marchv1机制，必要精确早版后核。

## 12193 — SaPaVe: Towards Active Perception and Manipulation in Vision-Language-Action Models for Robotics

SUP_TOPIC_MULTIMODAL.raw / http://arxiv.org/abs/2603.12193v1 / published=2026-03-12T17:23:46Z / updated=2026-03-12T17:23:46Z

完整AB：Active perception and manipulation are crucial for robots to interact with complex scenes. Existing methods struggle to unify semantic-driven active perception with robust, viewpoint-invariant execution. We propose SaPaVe, an end-to-end framework that jointly learns these capabilities in a data-efficient manner. Our approach decouples camera and manipulation actions rather than placing them in a shared action space, and follows a bottom-up training strategy: we first train semantic camera control on a large-scale dataset, then jointly optimize both action types using hybrid data. To support this framework, we introduce ActiveViewPose-200K, a dataset of 200k image-language-camera movement pairs for semantic camera movement learning, and a 3D geometry-aware module that improves execution robustness under dynamic viewpoints. We also present ActiveManip-Bench, the first benchmark for evaluating active manipulation beyond fixed-view settings. Extensive experiments in both simulation and real-world environments show that SaPaVe outperforms recent vision-language-action models such as GR00T N1 and \(π_0\), achieving up to 31.25\% higher success rates in real-world tasks. These results show that tightly coupled perception and execution, when trained with decoupled yet coordinated strategies, enable efficient and generalizable active manipulation. Project page: https://lmzpai.github.io/SaPaVe

准备者初判：P：camera/manipulation分离，camera先学再hybridjoint/3Dgeometry→主动感知与执行训练/坐标耦合，不为dataset/领域数字收。

## 12094 — Human-Centred LLM Privacy Audits: Findings and Frictions

SUP_TITLES_CL_RETRY.raw / http://arxiv.org/abs/2603.12094v1 / published=2026-03-12T16:01:01Z / updated=2026-03-12T16:01:01Z

完整AB：Large language models (LLMs) learn statistical associations from massive training corpora and user interactions, and deployed systems can surface or infer information about individuals. Yet people lack practical ways to inspect what a model associates with their name. We report interim findings from an ongoing study and introduce LMP2, a browser-based self-audit tool. In two user studies ($N_{total}{=}458$), GPT-4o predicts 11 of 50 features for everyday people with $\ge$60\% accuracy, and participants report wanting control over LLM-generated associations despite not considering all outputs privacy violations. To validate our probing method, we evaluate eight LLMs on public figures and non-existent names, observing clear separation between stable name-conditioned associations and model defaults. Our findings also contribute to exposing a broader generative AI evaluation crisis: when outputs are probabilistic, context-dependent, and user-mediated through elicitation, what model--individual associations even include is under-specified and operationalisation relies on crafting probes and metrics that are hard to validate or compare. To move towards reliable, actionable human-centred LLM privacy audits, we identify nine frictions that emerged in our study and offer recommendations for future work and the design of human-centred LLM privacy audits.

准备者初判：P：真实受试者与public/不存在name null→区分稳定name关联/default，修正隐私probe/真值评价，不授都是真实秘密。

## 12129 — Increasing intelligence in AI agents can worsen collective outcomes

SUP_TOPIC_AGENT.raw / http://arxiv.org/abs/2603.12129v1 / published=2026-03-12T16:31:28Z / updated=2026-03-12T16:31:28Z

完整AB：When resources are scarce, will a population of AI agents coordinate in harmony, or descend into tribal chaos? Diverse decision-making AI from different developers is entering everyday devices -- from phones and medical devices to battlefield drones and cars -- and these AI agents typically compete for finite shared resources such as charging slots, relay bandwidth, and traffic priority. Yet their collective dynamics and hence risks to users and society are poorly understood. Here we study AI-agent populations as the first system of real agents in which four key variables governing collective behaviour can be independently toggled: nature (innate LLM diversity), nurture (individual reinforcement learning), culture (emergent tribe formation), and resource scarcity. We show empirically and mathematically that when resources are scarce, AI model diversity and reinforcement learning increase dangerous system overload, though tribe formation lessens this risk. Meanwhile, some individuals profit handsomely. When resources are abundant, the same ingredients drive overload to near zero, though tribe formation makes the overload slightly worse. The crossover is arithmetical: it is where opposing tribes that form spontaneously first fit inside the available capacity. More sophisticated AI-agent populations are not better: whether their sophistication helps or harms depends entirely on a single number -- the capacity-to-population ratio -- that is knowable before any AI-agent ships.

准备者初判：P：个体增强而collective反退、capacity人口cross-over→重查资源条件；理论普遍性/因果待核，不为成熟类比加分。

## 11409 — Speak or Stay Silent: Context-Aware Turn-Taking in Multi-Party Dialogue

SUP_TITLES_CL_RETRY.raw / http://arxiv.org/abs/2603.11409v1 / published=2026-03-12T00:44:20Z / updated=2026-03-12T00:44:20Z

完整AB：Existing voice AI assistants treat every detected pause as an invitation to speak. This works in dyadic dialogue, but in multi-party settings, where an AI assistant participates alongside multiple speakers, pauses are abundant and ambiguous. An assistant that speaks on every pause becomes disruptive rather than useful. In this work, we formulate context-aware turn-taking: at every detected pause, given the full conversation context, our method decides whether the assistant should speak or stay silent. We introduce a benchmark of over 120K labeled conversations spanning three multi-party corpora. Evaluating eight recent large language models, we find that they consistently fail at context-aware turn-taking under zero-shot prompting. We then propose a supervised fine-tuning approach with reasoning traces, improving balanced accuracy by up to 23 percentage points. Our findings suggest that context-aware turn-taking is not an emergent capability; it must be explicitly trained.

准备者初判：P：pause非speak许可→conversation条件二分/zero-shot负侧→重查语音turn与发言动作目标；120K/23pp不授不存在emergence普遍定理。

七P不是确认候选/全文队列；11881具体EX待独核，不追处置无关日期。非准备者读完整题摘后校准，不借成熟原则抬分，不扩所有领域/全149。
