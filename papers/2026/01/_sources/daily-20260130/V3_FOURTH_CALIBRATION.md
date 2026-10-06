# 2026-01-30 第四批题摘准入（作者初判）

最终修正：root实际36完整题摘校准；StructAlign20597/SEER20305/MemCtrl20831/MobileBench20335/CtrlCoT20467明确EX（成熟recipe，未建立新条件），SEER shared-space不证明support/realizability。SAPO20312/CE-RM20327/cue20282按最小机制/受控干预准入5且必要评价通过，K=0不等softmax0/参数删除。PURGE20568保留明确contraction潜在贡献6并用all-zero group/零KL梯度反例终态争议，不因证明錯排除。19961 DATE隔离。其他22必要packet已获root实际复核，mmICL/FAQ/context整合及MED具体已有覆盖最终见本日README；下方初判/原题摘继续保留。

贡献理由与评分仅绑定拟核的增量；尚未授予 Evidence/Books。Created只是上界，早Submitted先保留日期。

## 2601.19961

贡献符合；日期待定：instantaneous featurecache高ratio导致轨迹误差→cached JVP构造interval-averagevelocity及budgeted稳定路径schedule，改变Flowcache误差累计选择；早Submitted先核firstday。

https://arxiv.org/abs/2601.19961v1
arXiv:2601.19961v1 (cs)
[Submitted on 27 Jan 2026 (this version), latest version 9 Mar 2026 (v3)]
Title:MeanCache: From Instantaneous to Average Velocity for Accelerating Flow Matching Inference
Authors:Huanlin Gao, Ping Chen, Fuyuan Shi, Ruijia Wu, Li YanTao, Qiang Hui, Yuren You, Ting Lu, Chao Tan, Shaoan Zhao, Zhaoxiang Liu, Fang Zhao, Kai Wang, Shiguo Lian
View a PDF of the paper titled MeanCache: From Instantaneous to Average Velocity for Accelerating Flow Matching Inference, by Huanlin Gao and 13 other authors
View PDF
HTML (experimental)
Abstract:We present MeanCache, a training-free caching framework for efficient Flow Matching inference. Existing caching methods reduce redundant computation but typically rely on instantaneous velocity information (e.g., feature caching), which often leads to severe trajectory deviations and error accumulation under high acceleration ratios. MeanCache introduces an average-velocity perspective: by leveraging cached Jacobian--vector products (JVP) to construct interval average velocities from instantaneous velocities, it effectively mitigates local error accumulation. To further improve cache timing and JVP reuse stability, we develop a trajectory-stability scheduling strategy as a practical tool, employing a Peak-Suppressed Shortest Path under budget constraints to determine the schedule. Experiments on FLUX.1, Qwen-Image, and HunyuanVideo demonstrate that MeanCache achieves 4.12X and 4.56X and 3.59X acceleration, respectively, while consistently outperforming state-of-the-art caching baselines in generation quality. We believe this simple yet effective approach provides a new perspective for Flow Matching inference and will inspire further exploration of stability-driven acceleration in commercial-scale generative models.
Subjects:
Machine Learning (cs.LG); Artificial Intelligence (cs.AI); Computer Vision and Pattern Recognition (cs.CV)
Cite as:
arXiv:2601.19961 [cs.LG]
(or
arXiv:2601.19961v1 [cs.LG] for this version)
https://doi.org/10.48550/arXiv.2601.19961
Focus to learn more
arXiv-issued DOI via DataCite
Journal reference:
ICLR 2026
Submission history From: Fang Zhao [view email]          [v1]
Tue, 27 Jan 2026 08:35:50 UTC (16,059 KB)
[v2]
Sat, 28 Feb 2026 02:54:04 UTC (16,059 KB)
[v3]
Mon, 9 Mar 2026 04:12:59 UTC (16,059 KB)



## 2601.20088

准入 2+2+2=6：多阶段SFT/RL/merge产物QAT不稳定且缺全训练数据→KL teacher QAD恢复NVFP4，多阶段稳定性和数据coverage为实际新增验证条件；不是蒸馏本身新。

https://arxiv.org/abs/2601.20088v1
arXiv:2601.20088v1 (cs)
[Submitted on 27 Jan 2026 (this version), latest version 3 Mar 2026 (v3)]
Title:Quantization-Aware Distillation for NVFP4 Inference Accuracy Recovery
Authors:Meng Xin, Sweta Priyadarshi, Jingyu Xin, Bilal Kartal, Aditya Vavre, Asma Kuriparambil Thekkumpate, Zijia Chen, Ameya Sunil Mahabaleshwarkar, Ido Shahaf, Akhiad Bercovich, Kinjal Patel, Suguna Varshini Velury, Chenjie Luo, Zhiyu Cheng, Jenny Chen, Chen-Han Yu, Wei Ping, Oleg Rybakov, Nima Tajbakhsh, Oluwatobi Olabiyi, Dusan Stosic, Di Wu, Song Han, Eric Chung, Sharath Turuvekere Sreenivas, Bryan Catanzaro, Yoshi Suhara, Tijmen Blankevoort, Huizi Mao
View a PDF of the paper titled Quantization-Aware Distillation for NVFP4 Inference Accuracy Recovery, by Meng Xin and 28 other authors
View PDF
HTML (experimental)
Abstract:This technical report presents quantization-aware distillation (QAD) and our best practices for recovering accuracy of NVFP4-quantized large language models (LLMs) and vision-language models (VLMs). QAD distills a full-precision teacher model into a quantized student model using a KL divergence loss. While applying distillation to quantized models is not a new idea, we observe key advantages of QAD for today's LLMs: 1. It shows remarkable effectiveness and stability for models trained through multi-stage post-training pipelines, including supervised fine-tuning (SFT), reinforcement learning (RL), and model merging, where traditional quantization-aware training (QAT) suffers from engineering complexity and training instability; 2. It is robust to data quality and coverage, enabling accuracy recovery without full training data. We evaluate QAD across multiple post-trained models including AceReason Nemotron, Nemotron 3 Nano, Nemotron Nano V2, Nemotron Nano V2 VL (VLM), and Llama Nemotron Super v1, showing consistent recovery to near-BF16 accuracy.
Subjects:
Machine Learning (cs.LG)
Cite as:
arXiv:2601.20088 [cs.LG]
(or
arXiv:2601.20088v1 [cs.LG] for this version)
https://doi.org/10.48550/arXiv.2601.20088
Focus to learn more
arXiv-issued DOI via DataCite
Submission history From: Huizi Mao [view email]          [v1]
Tue, 27 Jan 2026 22:14:47 UTC (256 KB)
[v2]
Sun, 1 Mar 2026 18:53:17 UTC (249 KB)
[v3]
Tue, 3 Mar 2026 06:03:52 UTC (249 KB)



## 2601.20745

准入 2+1+2=5：hardrounding+STE过早离散梯度不匹配→Hessian-trace逐tensor温控softmax渐硬化→1.58bit训练需按局部曲率决定离散时机，限定1B/3B。

https://arxiv.org/abs/2601.20745v1
arXiv:2601.20745v1 (cs)
[Submitted on 28 Jan 2026]
Title:HESTIA: A Hessian-Guided Differentiable Quantization-Aware Training Framework for Extremely Low-Bit LLMs
Authors:Guoan Wang, Feiyu Wang, Zongwei Lv, Yikun Zong, Tong Yang
View a PDF of the paper titled HESTIA: A Hessian-Guided Differentiable Quantization-Aware Training Framework for Extremely Low-Bit LLMs, by Guoan Wang and 4 other authors
View PDF
HTML (experimental)
Abstract:As large language models (LLMs) continue to scale, deployment is increasingly bottlenecked by the memory wall, motivating a shift toward extremely low-bit quantization. However, most quantization-aware training (QAT) methods apply hard rounding and the straight-through estimator (STE) from the beginning of the training, which prematurely discretizes the optimization landscape and induces persistent gradient mismatch between latent weights and quantized weights, hindering effective optimization of quantized models. To address this, we propose Hestia, a Hessian-guided differentiable QAT framework for extremely low-bit LLMs, which replaces the rigid step function with a temperature-controlled softmax relaxation to maintain gradient flow early in training while progressively hardening quantization. Furthermore, Hestia leverages a tensor-wise Hessian trace metric as a lightweight curvature signal to drive fine-grained temperature annealing, enabling sensitivity-aware discretization across the model. Evaluations on Llama-3.2 show that Hestia consistently outperforms existing ternary QAT baselines, yielding average zero-shot improvements of 5.39% and 4.34% for the 1B and 3B models. These results indicate that Hessian-guided relaxation effectively recovers representational capacity, establishing a more robust training path for 1.58-bit LLMs. The code is available at this https URL.
Comments:
13 pages, 2 figures
Subjects:
Machine Learning (cs.LG); Artificial Intelligence (cs.AI)
Cite as:
arXiv:2601.20745 [cs.LG]
(or
arXiv:2601.20745v1 [cs.LG] for this version)
https://doi.org/10.48550/arXiv.2601.20745
Focus to learn more
arXiv-issued DOI via DataCite
Submission history From: Guoan Wang [view email]          [v1]
Wed, 28 Jan 2026 16:22:42 UTC (361 KB)



## 2601.20655

准入 2+2+2=6：多阶段AIGC one-sided RDMA GPU缓存访问死锁→double-ring生命周期同步与stage elasticity→分离pipeline不等通信无死锁；16x需baseline资源核。

https://arxiv.org/abs/2601.20655v1
arXiv:2601.20655v1 (cs)
[Submitted on 28 Jan 2026]
Title:OnePiece: A Large-Scale Distributed Inference System with RDMA for Complex AI-Generated Content (AIGC) Workflows
Authors:June Chen, Neal Xu, Gragas Huang, Bok Zhou, Stephen Liu
View a PDF of the paper titled OnePiece: A Large-Scale Distributed Inference System with RDMA for Complex AI-Generated Content (AIGC) Workflows, by June Chen and 4 other authors
View PDF
HTML (experimental)
Abstract:The rapid growth of AI-generated content (AIGC) has enabled high-quality creative production across diverse domains, yet existing systems face critical inefficiencies in throughput, resource utilization, and scalability under concurrent workloads. This paper introduces OnePiece, a large-scale distributed inference system with RDMA optimized for multi-stage AIGC workflows. By decomposing pipelines into fine-grained microservices and leveraging one-sided RDMA communication, OnePiece significantly reduces inter-node latency and CPU overhead while improving GPU utilization. The system incorporates a novel double-ring buffer design to resolve deadlocks in RDMA-aware memory access without CPU involvement. Additionally, a dynamic Node Manager allocates resources elastically across workflow stages in response to real-time load. Experimental results demonstrate that OnePiece reduces GPU resource consumption by 16x in Wan2.1 image-to-video generation compared to monolithic inference pipelines, offering a scalable, fault-tolerant, and efficient solution for production AIGC environments.
Comments:
12 pages
Subjects:
Distributed, Parallel, and Cluster Computing (cs.DC)
Cite as:
arXiv:2601.20655 [cs.DC]
(or
arXiv:2601.20655v1 [cs.DC] for this version)
https://doi.org/10.48550/arXiv.2601.20655
Focus to learn more
arXiv-issued DOI via DataCite
Submission history From: Neal Xu [view email]          [v1]
Wed, 28 Jan 2026 14:38:16 UTC (2,050 KB)



## 2601.20796

准入 2+2+3=7：controlled synthetic小Transformer中RoPE提高ICL复杂度阈值、primary多样性允许secondary低复杂度→跨模态ICL不是对称数据要求，需核inductioncircuit。

https://arxiv.org/abs/2601.20796v1
arXiv:2601.20796v1 (cs)
[Submitted on 28 Jan 2026 (this version), latest version 26 May 2026 (v2)]
Title:Dissecting Multimodal In-Context Learning: Modality Asymmetries and Circuit Dynamics in modern Transformers
Authors:Yiran Huang, Karsten Roth, Quentin Bouniot, Wenjia Xu, Zeynep Akata
View a PDF of the paper titled Dissecting Multimodal In-Context Learning: Modality Asymmetries and Circuit Dynamics in modern Transformers, by Yiran Huang and 4 other authors
View PDF
HTML (experimental)
Abstract:Transformer-based multimodal large language models often exhibit in-context learning (ICL) abilities. Motivated by this phenomenon, we ask: how do transformers learn to associate information across modalities from in-context examples? We investigate this question through controlled experiments on small transformers trained on synthetic classification tasks, enabling precise manipulation of data statistics and model architecture. We begin by revisiting core principles of unimodal ICL in modern transformers. While several prior findings replicate, we find that Rotary Position Embeddings (RoPE) increases the data complexity threshold for ICL. Extending to the multimodal setting reveals a fundamental learning asymmetry: when pretrained on high-diversity data from a primary modality, surprisingly low data complexity in the secondary modality suffices for multimodal ICL to emerge. Mechanistic analysis shows that both settings rely on an induction-style mechanism that copies labels from matching in-context exemplars; multimodal training refines and extends these circuits across modalities. Our findings provide a mechanistic foundation for understanding multimodal ICL in modern transformers and introduce a controlled testbed for future investigation.
Subjects:
Computation and Language (cs.CL); Machine Learning (cs.LG)
Cite as:
arXiv:2601.20796 [cs.CL]
(or
arXiv:2601.20796v1 [cs.CL] for this version)
https://doi.org/10.48550/arXiv.2601.20796
Focus to learn more
arXiv-issued DOI via DataCite
Submission history From: Yiran Huang [view email]          [v1]
Wed, 28 Jan 2026 17:37:28 UTC (1,249 KB)
[v2]
Tue, 26 May 2026 14:33:44 UTC (1,333 KB)



## 2601.20597

准入 2+1+2=5：continual跨模态两种drift→共享ETF原型及关系保持控制非协作失配→不能只保单模态featurestable作为crossmodalstable。

https://arxiv.org/abs/2601.20597v1
arXiv:2601.20597v1 (cs)
[Submitted on 28 Jan 2026 (this version), latest version 25 Apr 2026 (v2)]
Title:StructAlign: Structured Cross-Modal Alignment for Continual Text-to-Video Retrieval
Authors:Shaokun Wang, Weili Guan, Jizhou Han, Jianlong Wu, Yupeng Hu, Liqiang Nie
View a PDF of the paper titled StructAlign: Structured Cross-Modal Alignment for Continual Text-to-Video Retrieval, by Shaokun Wang and 5 other authors
View PDF
HTML (experimental)
Abstract:Continual Text-to-Video Retrieval (CTVR) is a challenging multimodal continual learning setting, where models must incrementally learn new semantic categories while maintaining accurate text-video alignment for previously learned ones, thus making it particularly prone to catastrophic forgetting. A key challenge in CTVR is feature drift, which manifests in two forms: intra-modal feature drift caused by continual learning within each modality, and non-cooperative feature drift across modalities that leads to modality misalignment. To mitigate these issues, we propose StructAlign, a structured cross-modal alignment method for CTVR. First, StructAlign introduces a simplex Equiangular Tight Frame (ETF) geometry as a unified geometric prior to mitigate modality misalignment. Building upon this geometric prior, we design a cross-modal ETF alignment loss that aligns text and video features with category-level ETF prototypes, encouraging the learned representations to form an approximate simplex ETF geometry. In addition, to suppress intra-modal feature drift, we design a Cross-modal Relation Preserving loss, which leverages complementary modalities to preserve cross-modal similarity relations, providing stable relational supervision for feature updates. By jointly addressing non-cooperative feature drift across modalities and intra-modal feature drift, StructAlign effectively alleviates catastrophic forgetting in CTVR. Extensive experiments on benchmark datasets demonstrate that our method consistently outperforms state-of-the-art continual retrieval approaches.
Subjects:
Computer Vision and Pattern Recognition (cs.CV)
Cite as:
arXiv:2601.20597 [cs.CV]
(or
arXiv:2601.20597v1 [cs.CV] for this version)
https://doi.org/10.48550/arXiv.2601.20597
Focus to learn more
arXiv-issued DOI via DataCite
Submission history From: Shaokun Wang [view email]          [v1]
Wed, 28 Jan 2026 13:34:44 UTC (2,492 KB)
[v2]
Sat, 25 Apr 2026 09:40:43 UTC (2,634 KB)



## 2601.20432

准入 2+2+2=6；安全深入：preserve speaker/content的selfvoiceconversion可破坏watermark→压缩/噪声鲁棒性不等生成模型重编码鲁棒性，需核attackaccess与utility。

https://arxiv.org/abs/2601.20432v1
arXiv:2601.20432v1 (cs)
[Submitted on 28 Jan 2026 (this version), latest version 16 Mar 2026 (v2)]
Title:Self Voice Conversion as an Attack against Neural Audio Watermarking
Authors:Yigitcan Özer, Wanying Ge, Zhe Zhang, Xin Wang, Junichi Yamagishi
View a PDF of the paper titled Self Voice Conversion as an Attack against Neural Audio Watermarking, by Yigitcan \"Ozer and Wanying Ge and Zhe Zhang and Xin Wang and Junichi Yamagishi
View PDF
HTML (experimental)
Abstract:Audio watermarking embeds auxiliary information into speech while maintaining speaker identity, linguistic content, and perceptual quality. Although recent advances in neural and digital signal processing-based watermarking methods have improved imperceptibility and embedding capacity, robustness is still primarily assessed against conventional distortions such as compression, additive noise, and resampling. However, the rise of deep learning-based attacks introduces novel and significant threats to watermark security. In this work, we investigate self voice conversion as a universal, content-preserving attack against audio watermarking systems. Self voice conversion remaps a speaker's voice to the same identity while altering acoustic characteristics through a voice conversion model. We demonstrate that this attack severely degrades the reliability of state-of-the-art watermarking approaches and highlight its implications for the security of modern audio watermarking techniques.
Comments:
7 pages; 2 figures; 2 tables; accepted at IEICE, SP/SLP 2026
Subjects:
Sound (cs.SD); Artificial Intelligence (cs.AI)
Cite as:
arXiv:2601.20432 [cs.SD]
(or
arXiv:2601.20432v1 [cs.SD] for this version)
https://doi.org/10.48550/arXiv.2601.20432
Focus to learn more
arXiv-issued DOI via DataCite
Submission history From: Yigitcan Özer [view email]          [v1]
Wed, 28 Jan 2026 09:41:18 UTC (80 KB)
[v2]
Mon, 16 Mar 2026 02:07:34 UTC (76 KB)



## 2601.20185

贡献关闭：pooling/hopsize调整+samplingrate提高是具体codec配置；UTMOSv2局部0.29提高未新增可复用codec语义/带宽失效边界，不能把最佳25Hz名次准入。

https://arxiv.org/abs/2601.20185v1
arXiv:2601.20185v1 (cs)
[Submitted on 28 Jan 2026 (this version), latest version 8 Mar 2026 (v2)]
Title:Improving X-Codec-2.0 for Multi-Lingual Speech: 25 Hz Latent Rate and 24 kHz Sampling
Authors:Husein Zolkepli
View a PDF of the paper titled Improving X-Codec-2.0 for Multi-Lingual Speech: 25 Hz Latent Rate and 24 kHz Sampling, by Husein Zolkepli
View PDF
HTML (experimental)
Abstract:X-Codec-2.0 has shown strong performance in neural audio compression and multilingual speech modeling, operating at a 50 Hz latent rate and a 16 kHz sampling rate using frozen HuBERT features. While effective, this configuration limits temporal efficiency and audio fidelity. In this work, we explore a simple and effective modification by introducing additional pooling and increasing the decoder hop size. This reduces the latent rate from 50 Hz to 25 Hz and simultaneously raises the output sampling rate from 16 kHz to 24 kHz, improving efficiency and perceptual quality without altering the core architecture. Evaluated on the multilingual Common Voice 17 test set, the proposed configuration achieves a 0.29 MOS improvement over the original X-Codec-2.0 baseline based on UTMOSv2, and attains the best reported performance among all codecs operating at 25 Hz. The source code, checkpoints, and generation comparisons are released at \href{this https URL}{this https URL}.
Subjects:
Computation and Language (cs.CL); Sound (cs.SD)
Cite as:
arXiv:2601.20185 [cs.CL]
(or
arXiv:2601.20185v1 [cs.CL] for this version)
https://doi.org/10.48550/arXiv.2601.20185
Focus to learn more
arXiv-issued DOI via DataCite
Submission history From: Husein Zolkepli [view email]          [v1]
Wed, 28 Jan 2026 02:36:30 UTC (204 KB)
[v2]
Sun, 8 Mar 2026 01:08:47 UTC (204 KB)



## 2601.20642

准入 2+2+3=7；安全深入：normscore假设isotropic在lownoise失败→angularalignment+normtwoforwards检测memorization→检测评价需绑定noise几何，不是统一norm阈值。

https://arxiv.org/abs/2601.20642v1
arXiv:2601.20642v1 (cs)
[Submitted on 28 Jan 2026 (this version), latest version 10 Feb 2026 (v2)]
Title:Detecting and Mitigating Memorization in Diffusion Models through Anisotropy of the Log-Probability
Authors:Rohan Asthana, Vasileios Belagiannis
View a PDF of the paper titled Detecting and Mitigating Memorization in Diffusion Models through Anisotropy of the Log-Probability, by Rohan Asthana and 1 other authors
View PDF
HTML (experimental)
Abstract:Diffusion-based image generative models produce high-fidelity images through iterative denoising but remain vulnerable to memorization, where they unintentionally reproduce exact copies or parts of training images. Recent memorization detection methods are primarily based on the norm of score difference as indicators of memorization. We prove that such norm-based metrics are mainly effective under the assumption of isotropic log-probability distributions, which generally holds at high or medium noise levels. In contrast, analyzing the anisotropic regime reveals that memorized samples exhibit strong angular alignment between the guidance vector and unconditional scores in the low-noise setting. Through these insights, we develop a memorization detection metric by integrating isotropic norm and anisotropic alignment. Our detection metric can be computed directly on pure noise inputs via two conditional and unconditional forward passes, eliminating the need for costly denoising steps. Detection experiments on Stable Diffusion v1.4 and v2 show that our metric outperforms existing denoising-free detection methods while being at least approximately 5x faster than the previous best approach. Finally, we demonstrate the effectiveness of our approach by utilizing a mitigation strategy that adapts memorized prompts based on our developed metric.
Comments:
Accepted at ICLR 2026
Subjects:
Machine Learning (cs.LG); Artificial Intelligence (cs.AI); Computer Vision and Pattern Recognition (cs.CV)
Cite as:
arXiv:2601.20642 [cs.LG]
(or
arXiv:2601.20642v1 [cs.LG] for this version)
https://doi.org/10.48550/arXiv.2601.20642
Focus to learn more
arXiv-issued DOI via DataCite
Submission history From: Rohan Asthana [view email]          [v1]
Wed, 28 Jan 2026 14:29:42 UTC (13,126 KB)
[v2]
Tue, 10 Feb 2026 08:24:56 UTC (13,126 KB)



## 2601.20564

准入 2+2+2=6：diffusionNVC latency/flicker→online temporalshift及batchdim asynchronousdecoding允许流式因果一致性/并行→需分清perceptualbitrate节省和pixel完整性。

https://arxiv.org/abs/2601.20564v1
arXiv:2601.20564v1 (cs)
[Submitted on 28 Jan 2026]
Title:DiffVC-RT: Towards Practical Real-Time Diffusion-based Perceptual Neural Video Compression
Authors:Wenzhuo Ma, Zhenzhong Chen
View a PDF of the paper titled DiffVC-RT: Towards Practical Real-Time Diffusion-based Perceptual Neural Video Compression, by Wenzhuo Ma and Zhenzhong Chen
View PDF
HTML (experimental)
Abstract:The practical deployment of diffusion-based Neural Video Compression (NVC) faces critical challenges, including severe information loss, prohibitive inference latency, and poor temporal consistency. To bridge this gap, we propose DiffVC-RT, the first framework designed to achieve real-time diffusion-based perceptual NVC. First, we introduce an Efficient and Informative Model Architecture. Through strategic module replacements and pruning, this architecture significantly reduces computational complexity while mitigating structural information loss. Second, to address generative flickering artifacts, we propose Explicit and Implicit Consistency Modeling. We enhance temporal consistency by explicitly incorporating a zero-cost Online Temporal Shift Module within the U-Net, complemented by hybrid implicit consistency constraints. Finally, we present an Asynchronous and Parallel Decoding Pipeline incorporating Mixed Half Precision, which enables asynchronous latent decoding and parallel frame reconstruction via a Batch-dimension Temporal Shift design. Experiments show that DiffVC-RT achieves 80.1% bitrate savings in terms of LPIPS over VTM-17.0 on HEVC dataset with real-time encoding and decoding speeds of 206 / 30 fps for 720p videos on an NVIDIA H800 GPU, marking a significant milestone in diffusion-based video compression.
Comments:
17 pages, 10 figures
Subjects:
Computer Vision and Pattern Recognition (cs.CV)
Cite as:
arXiv:2601.20564 [cs.CV]
(or
arXiv:2601.20564v1 [cs.CV] for this version)
https://doi.org/10.48550/arXiv.2601.20564
Focus to learn more
arXiv-issued DOI via DataCite
Submission history From: Wenzhuo Ma [view email]          [v1]
Wed, 28 Jan 2026 12:59:25 UTC (2,200 KB)



## 2601.20391

准入 2+1+2=5：diffusion生成queryviews可引入冲突信号降低检索→semanticconsistency/diffusioncontrastive过滤→生成更多view不能默认RAG可靠增益。

https://arxiv.org/abs/2601.20391v1
arXiv:2601.20391v1 (cs)
[Submitted on 28 Jan 2026]
Title:Eliminating Hallucination in Diffusion-Augmented Interactive Text-to-Image Retrieval
Authors:Zhuocheng Zhang, Kangheng Liang, Guanxuan Li, Paul Henderson, Richard Mccreadie, Zijun Long
View a PDF of the paper titled Eliminating Hallucination in Diffusion-Augmented Interactive Text-to-Image Retrieval, by Zhuocheng Zhang and 5 other authors
View PDF
HTML (experimental)
Abstract:Diffusion-Augmented Interactive Text-to-Image Retrieval (DAI-TIR) is a promising paradigm that improves retrieval performance by generating query images via diffusion models and using them as additional ``views'' of the user's intent. However, these generative views can be incorrect because diffusion generation may introduce hallucinated visual cues that conflict with the original query text. Indeed, we empirically demonstrate that these hallucinated cues can substantially degrade DAI-TIR performance. To address this, we propose Diffusion-aware Multi-view Contrastive Learning (DMCL), a hallucination-robust training framework that casts DAI-TIR as joint optimization over representations of query intent and the target image. DMCL introduces semantic-consistency and diffusion-aware contrastive objectives to align textual and diffusion-generated query views while suppressing hallucinated query signals. This yields an encoder that acts as a semantic filter, effectively mapping hallucinated cues into a null space, improving robustness to spurious cues and better representing the user's intent. Attention visualization and geometric embedding-space analyses corroborate this filtering behavior. Across five standard benchmarks, DMCL delivers consistent improvements in multi-round Hits@10, reaching as high as 7.37\% over prior fine-tuned and zero-shot baselines, which indicates it is a general and robust training framework for DAI-TIR.
Subjects:
Information Retrieval (cs.IR)
Cite as:
arXiv:2601.20391 [cs.IR]
(or
arXiv:2601.20391v1 [cs.IR] for this version)
https://doi.org/10.48550/arXiv.2601.20391
Focus to learn more
arXiv-issued DOI via DataCite
Submission history From: Zijun Long [view email]          [v1]
Wed, 28 Jan 2026 08:58:57 UTC (3,697 KB)



## 2601.20363

准入 2+1+2=5：同连续Gaussian训练全局稀疏离散支持下SDE比ODE更有效→随机性与constraintclamping选择影响有效率/样本成本；不比经典solver快。

https://arxiv.org/abs/2601.20363v1
arXiv:2601.20363v1 (cs)
[Submitted on 28 Jan 2026]
Title:Can Continuous-Time Diffusion Models Generate and Solve Globally Constrained Discrete Problems? A Study on Sudoku
Authors:Mariia Drozdova
View a PDF of the paper titled Can Continuous-Time Diffusion Models Generate and Solve Globally Constrained Discrete Problems? A Study on Sudoku, by Mariia Drozdova
View PDF
HTML (experimental)
Abstract:Can standard continuous-time generative models represent distributions whose support is an extremely sparse, globally constrained discrete set? We study this question using completed Sudoku grids as a controlled testbed, treating them as a subset of a continuous relaxation space. We train flow-matching and score-based models along a Gaussian probability path and compare deterministic (ODE) sampling, stochastic (SDE) sampling, and DDPM-style discretizations derived from the same continuous-time training. Unconditionally, stochastic sampling substantially outperforms deterministic flows; score-based samplers are the most reliable among continuous-time methods, and DDPM-style ancestral sampling achieves the highest validity overall. We further show that the same models can be repurposed for guided generation: by repeatedly sampling completions under clamped clues and stopping when constraints are satisfied, the model acts as a probabilistic Sudoku solver. Although far less sample-efficient than classical solvers and discrete-geometry-aware diffusion methods, these experiments demonstrate that classic diffusion/flow formulations can assign non-zero probability mass to globally constrained combinatorial structures and can be used for constraint satisfaction via stochastic search.
Comments:
26 pages, 5 figures. Empirical study of continuous-time diffusion and flow models on Sudoku. Code available at this https URL
Subjects:
Machine Learning (cs.LG); Artificial Intelligence (cs.AI)
Cite as:
arXiv:2601.20363 [cs.LG]
(or
arXiv:2601.20363v1 [cs.LG] for this version)
https://doi.org/10.48550/arXiv.2601.20363
Focus to learn more
arXiv-issued DOI via DataCite
Submission history From: Mariia Drozdova [view email]          [v1]
Wed, 28 Jan 2026 08:26:54 UTC (4,490 KB)



## 2601.20310

准入 2+2+2=6；安全深入：一个watermarkedimage+blackboxaccess可伪造provenance→semanticmaskbindlatent水印，需按anti-forgery/robustness双轴而非只detection衡量。

https://arxiv.org/abs/2601.20310v1
arXiv:2601.20310v1 (cs)
[Submitted on 28 Jan 2026]
Title:SemBind: Binding Diffusion Watermarks to Semantics Against Black-Box Forgery Attacks
Authors:Xin Zhang, Zijin Yang, Kejiang Chen, Linfeng Ma, Weiming Zhang, Nenghai Yu
View a PDF of the paper titled SemBind: Binding Diffusion Watermarks to Semantics Against Black-Box Forgery Attacks, by Xin Zhang and 5 other authors
View PDF
HTML (experimental)
Abstract:Latent-based watermarks, integrated into the generation process of latent diffusion models (LDMs), simplify detection and attribution of generated images. However, recent black-box forgery attacks, where an attacker needs at least one watermarked image and black-box access to the provider's model, can embed the provider's watermark into images not produced by the provider, posing outsized risk to provenance and trust. We propose SemBind, the first defense framework for latent-based watermarks that resists black-box forgery by binding latent signals to image semantics via a learned semantic masker. Trained with contrastive learning, the masker yields near-invariant codes for the same prompt and near-orthogonal codes across prompts; these codes are reshaped and permuted to modulate the target latent before any standard latent-based watermark. SemBind is generally compatible with existing latent-based watermarking schemes and keeps image quality essentially unchanged, while a simple mask-ratio parameter offers a tunable trade-off between anti-forgery strength and robustness. Across four mainstream latent-based watermark methods, our SemBind-enabled anti-forgery variants markedly reduce false acceptance under black-box forgery while providing a controllable robustness-security balance.
Subjects:
Cryptography and Security (cs.CR); Computer Vision and Pattern Recognition (cs.CV); Machine Learning (cs.LG)
Cite as:
arXiv:2601.20310 [cs.CR]
(or
arXiv:2601.20310v1 [cs.CR] for this version)
https://doi.org/10.48550/arXiv.2601.20310
Focus to learn more
arXiv-issued DOI via DataCite
Submission history From: Xin Zhang [view email]          [v1]
Wed, 28 Jan 2026 07:02:40 UTC (49,651 KB)



## 2601.20305

准入 2+2+2=6：UMM理解不能自动指导生成→selfaligneddescriptor显式generativereasoning与两阶段endogenousreward学习→理解与生成之间需可执行信息通道；300样本不等广域。

https://arxiv.org/abs/2601.20305v1
arXiv:2601.20305v1 (cs)
[Submitted on 28 Jan 2026]
Title:Endogenous Reprompting: Self-Evolving Cognitive Alignment for Unified Multimodal Models
Authors:Zhenchen Tang, Songlin Yang, Zichuan Wang, Bo Peng, Yang Li, Beibei Dong, Jing Dong
View a PDF of the paper titled Endogenous Reprompting: Self-Evolving Cognitive Alignment for Unified Multimodal Models, by Zhenchen Tang and 6 other authors
View PDF
HTML (experimental)
Abstract:Unified Multimodal Models (UMMs) exhibit strong understanding, yet this capability often fails to effectively guide generation. We identify this as a Cognitive Gap: the model lacks the understanding of how to enhance its own generation process. To bridge this gap, we propose Endogenous Reprompting, a mechanism that transforms the model's understanding from a passive encoding process into an explicit generative reasoning step by generating self-aligned descriptors during generation. To achieve this, we introduce SEER (Self-Evolving Evaluator and Reprompter), a training framework that establishes a two-stage endogenous loop using only 300 samples from a compact proxy task, Visual Instruction Elaboration. First, Reinforcement Learning with Verifiable Rewards (RLVR) activates the model's latent evaluation ability via curriculum learning, producing a high-fidelity endogenous reward signal. Second, Reinforcement Learning with Model-rewarded Thinking (RLMT) leverages this signal to optimize the generative reasoning policy. Experiments show that SEER consistently outperforms state-of-the-art baselines in evaluation accuracy, reprompting efficiency, and generation quality, without sacrificing general multimodal capabilities.
Subjects:
Artificial Intelligence (cs.AI)
Cite as:
arXiv:2601.20305 [cs.AI]
(or
arXiv:2601.20305v1 [cs.AI] for this version)
https://doi.org/10.48550/arXiv.2601.20305
Focus to learn more
arXiv-issued DOI via DataCite
Submission history From: Zhenchen Tang [view email]          [v1]
Wed, 28 Jan 2026 06:54:36 UTC (3,083 KB)



## 2601.20297

贡献关闭：Appearance/Motion/Camera的10类artifacttaxonomy+80k训练detector；未在题摘提供global-score失效的受控证据或新评价可靠性条件，不能新benchmark标签准入。

https://arxiv.org/abs/2601.20297v1
arXiv:2601.20297v1 (cs)
[Submitted on 28 Jan 2026]
Title:Artifact-Aware Evaluation for High-Quality Video Generation
Authors:Chen Zhu, Jiashu Zhu, Yanxun Li, Meiqi Wu, Bingze Song, Chubin Chen, Jiahong Wu, Xiangxiang Chu, Yangang Wang
View a PDF of the paper titled Artifact-Aware Evaluation for High-Quality Video Generation, by Chen Zhu and 8 other authors
View PDF
HTML (experimental)
Abstract:With the rapid advancement of video generation techniques, evaluating and auditing generated videos has become increasingly crucial. Existing approaches typically offer coarse video quality scores, lacking detailed localization and categorization of specific artifacts. In this work, we introduce a comprehensive evaluation protocol focusing on three key aspects affecting human perception: Appearance, Motion, and Camera. We define these axes through a taxonomy of 10 prevalent artifact categories reflecting common generative failures observed in video generation. To enable robust artifact detection and categorization, we introduce GenVID, a large-scale dataset of 80k videos generated by various state-of-the-art video generation models, each carefully annotated for the defined artifact categories. Leveraging GenVID, we develop DVAR, a Dense Video Artifact Recognition framework for fine-grained identification and classification of generative artifacts. Extensive experiments show that our approach significantly improves artifact detection accuracy and enables effective filtering of low-quality content.
Subjects:
Computer Vision and Pattern Recognition (cs.CV)
Cite as:
arXiv:2601.20297 [cs.CV]
(or
arXiv:2601.20297v1 [cs.CV] for this version)
https://doi.org/10.48550/arXiv.2601.20297
Focus to learn more
arXiv-issued DOI via DataCite
Submission history From: Chen Zhu [view email]          [v1]
Wed, 28 Jan 2026 06:45:14 UTC (3,885 KB)



## 2601.20028

准入 2+2+2=6：alignedCLIP/CLAP仍被SAE学成unimodal splitdictionary→randomcrossmodalmask+group-sparse对齐decomposition→embedding对齐不保证解释字典对齐。

https://arxiv.org/abs/2601.20028v1
arXiv:2601.20028v1 (cs)
[Submitted on 27 Jan 2026]
Title:Decomposing multimodal embedding spaces with group-sparse autoencoders
Authors:Chiraag Kaushik, Davis Barch, Andrea Fanelli
View a PDF of the paper titled Decomposing multimodal embedding spaces with group-sparse autoencoders, by Chiraag Kaushik and 2 other authors
View PDF
HTML (experimental)
Abstract:The Linear Representation Hypothesis asserts that the embeddings learned by neural networks can be understood as linear combinations of features corresponding to high-level concepts. Based on this ansatz, sparse autoencoders (SAEs) have recently become a popular method for decomposing embeddings into a sparse combination of linear directions, which have been shown empirically to often correspond to human-interpretable semantics. However, recent attempts to apply SAEs to multimodal embedding spaces (such as the popular CLIP embeddings for image/text data) have found that SAEs often learn "split dictionaries", where most of the learned sparse features are essentially unimodal, active only for data of a single modality. In this work, we study how to effectively adapt SAEs for the setting of multimodal embeddings while ensuring multimodal alignment. We first argue that the existence of a split dictionary decomposition on an aligned embedding space implies the existence of a non-split dictionary with improved modality alignment. Then, we propose a new SAE-based approach to multimodal embedding decomposition using cross-modal random masking and group-sparse regularization. We apply our method to popular embeddings for image/text (CLIP) and audio/text (CLAP) data and show that, compared to standard SAEs, our approach learns a more multimodal dictionary while reducing the number of dead neurons and improving feature semanticity. We finally demonstrate how this improvement in alignment of concepts between modalities can enable improvements in the interpretability and control of cross-modal tasks.
Comments:
19 pages
Subjects:
Machine Learning (cs.LG)
Cite as:
arXiv:2601.20028 [cs.LG]
(or
arXiv:2601.20028v1 [cs.LG] for this version)
https://doi.org/10.48550/arXiv.2601.20028
Focus to learn more
arXiv-issued DOI via DataCite
Submission history From: Chiraag Kaushik [view email]          [v1]
Tue, 27 Jan 2026 20:04:07 UTC (1,745 KB)



## 2601.20844

准入 2+2+3=7：embeddingtop-k任意subset表示的最小维数tightbounds→低维可表示≠可学习，容量反例不应把检索失败归因几何维数；核distances/constructiveassumptions。

https://arxiv.org/abs/2601.20844v1
arXiv:2601.20844v1 (cs)
[Submitted on 28 Jan 2026 (this version), latest version 2 Jun 2026 (v3)]
Title:$\mathbb{R}^{2k}$ is Theoretically Large Enough for Embedding-based Top-$k$ Retrieval
Authors:Zihao Wang, Hang Yin, Lihui Liu, Hanghang Tong, Yangqiu Song, Ginny Wong, Simon See
View a PDF of the paper titled $\mathbb{R}^{2k}$ is Theoretically Large Enough for Embedding-based Top-$k$ Retrieval, by Zihao Wang and 6 other authors
View PDF
HTML (experimental)
Abstract:This paper studies the minimal dimension required to embed subset memberships ($m$ elements and ${m\choose k}$ subsets of at most $k$ elements) into vector spaces, denoted as Minimal Embeddable Dimension (MED). The tight bounds of MED are derived theoretically and supported empirically for various notions of "distances" or "similarities," including the $\ell_2$ metric, inner product, and cosine similarity. In addition, we conduct numerical simulation in a more achievable setting, where the ${m\choose k}$ subset embeddings are chosen as the centroid of the embeddings of the contained elements. Our simulation easily realizes a logarithmic dependency between the MED and the number of elements to embed. These findings imply that embedding-based retrieval limitations stem primarily from learnability challenges, not geometric constraints, guiding future algorithm design.
Subjects:
Machine Learning (cs.LG); Artificial Intelligence (cs.AI); Information Retrieval (cs.IR)
Cite as:
arXiv:2601.20844 [cs.LG]
(or
arXiv:2601.20844v1 [cs.LG] for this version)
https://doi.org/10.48550/arXiv.2601.20844
Focus to learn more
arXiv-issued DOI via DataCite
Submission history From: Zihao Wang [view email]          [v1]
Wed, 28 Jan 2026 18:45:43 UTC (56 KB)
[v2]
Thu, 29 Jan 2026 03:54:29 UTC (39 KB)
[v3]
Tue, 2 Jun 2026 03:19:04 UTC (91 KB)



## 2601.20829

准入 2+2+2=6：saturatedbinaryreward少失败并不无learning signal→rareincorrectprefix重分配exploration→需控制prefixmisleading及correctreasonadherence代价。

https://arxiv.org/abs/2601.20829v1
arXiv:2601.20829v1 (cs)
[Submitted on 28 Jan 2026 (this version), latest version 9 May 2026 (v2)]
Title:Training Reasoning Models on Saturated Problems via Failure-Prefix Conditioning
Authors:Minwu Kim, Safal Shrestha, Keith Ross
View a PDF of the paper titled Training Reasoning Models on Saturated Problems via Failure-Prefix Conditioning, by Minwu Kim and 2 other authors
View PDF
HTML (experimental)
Abstract:Reinforcement Learning with Verifiable Rewards (RLVR) has substantially improved the reasoning abilities of large language models (LLMs), yet training often stalls as problems become saturated. We identify the core challenge as the poor accessibility of informative failures: learning signals exist but are rarely encountered during standard rollouts. To address this, we propose failure-prefix conditioning, a simple and effective method for learning from saturated problems. Rather than starting from the original question, our approach reallocates exploration by conditioning training on prefixes derived from rare incorrect reasoning trajectories, thereby exposing the model to failure-prone states. We observe that failure-prefix conditioning yields performance gains matching those of training on medium-difficulty problems, while preserving token efficiency. Furthermore, we analyze the model's robustness, finding that our method reduces performance degradation under misleading failure prefixes, albeit with a mild trade-off in adherence to correct early reasoning. Finally, we demonstrate that an iterative approach, which refreshes failure prefixes during training, unlocks additional gains after performance plateaus. Overall, our results suggest that failure-prefix conditioning offers an effective pathway to extend RLVR training on saturated problems.
Comments:
16 pages
Subjects:
Machine Learning (cs.LG); Artificial Intelligence (cs.AI); Computation and Language (cs.CL)
Cite as:
arXiv:2601.20829 [cs.LG]
(or
arXiv:2601.20829v1 [cs.LG] for this version)
https://doi.org/10.48550/arXiv.2601.20829
Focus to learn more
arXiv-issued DOI via DataCite
Submission history From: Minwu Kim [view email]          [v1]
Wed, 28 Jan 2026 18:29:21 UTC (170 KB)
[v2]
Sat, 9 May 2026 10:47:17 UTC (184 KB)



## 2601.20568

准入 2+2+2=6；安全深入：forbiddenconcept奖励惩罚被宣称verifiableunlearning→拟核输出抑制与知识移除/抗attack的界面差异，不接受GDPR/理论保证宣传；实质安全变更。

https://arxiv.org/abs/2601.20568v1
arXiv:2601.20568v1 (cs)
[Submitted on 28 Jan 2026 (this version), latest version 20 Mar 2026 (v3)]
Title:Reinforcement Unlearning via Group Relative Policy Optimization
Authors:Efstratios Zaradoukas, Bardh Prenkaj, Gjergji Kasneci
View a PDF of the paper titled Reinforcement Unlearning via Group Relative Policy Optimization, by Efstratios Zaradoukas and 2 other authors
View PDF
HTML (experimental)
Abstract:During pretraining, LLMs inadvertently memorize sensitive or copyrighted data, posing significant compliance challenges under legal frameworks like the GDPR and the EU AI Act. Fulfilling these mandates demands techniques that can remove information from a deployed model without retraining from scratch. Existing unlearning approaches attempt to address this need, but often leak the very data they aim to erase, sacrifice fluency and robustness, or depend on costly external reward models. We introduce PURGE (Policy Unlearning through Relative Group Erasure), a novel method grounded in the Group Relative Policy Optimization framework that formulates unlearning as a verifiable problem. PURGE uses an intrinsic reward signal that penalizes any mention of forbidden concepts, allowing safe and consistent unlearning. Our approach reduces token usage per target by up to a factor of 46 compared with SotA methods, while improving fluency by 5.48 percent and adversarial robustness by 12.02 percent over the base model. On the Real World Knowledge Unlearning (RWKU) benchmark, PURGE achieves 11 percent unlearning effectiveness while preserving 98 percent of original utility. PURGE shows that framing LLM unlearning as a verifiable task, enables more reliable, efficient, and scalable forgetting, suggesting a promising new direction for unlearning research that combines theoretical guarantees, improved safety, and practical deployment efficiency.
Subjects:
Machine Learning (cs.LG)
Cite as:
arXiv:2601.20568 [cs.LG]
(or
arXiv:2601.20568v1 [cs.LG] for this version)
https://doi.org/10.48550/arXiv.2601.20568
Focus to learn more
arXiv-issued DOI via DataCite
Submission history From: Efstratios Zaradoukas [view email]          [v1]
Wed, 28 Jan 2026 13:07:58 UTC (4,631 KB)
[v2]
Wed, 18 Feb 2026 09:58:17 UTC (4,635 KB)
[v3]
Fri, 20 Mar 2026 12:54:58 UTC (4,628 KB)



## 2601.20838

准入 2+2+2=6；设计反证深入：同preferencedata/finetune下RM仍继承baseagency/communion偏向且追溯pretrainlogits→不能将RM值视为仅标注者偏好；限定psychocorpora。

https://arxiv.org/abs/2601.20838v1
arXiv:2601.20838v1 (cs)
[Submitted on 28 Jan 2026 (this version), latest version 1 Mar 2026 (v2)]
Title:Reward Models Inherit Value Biases from Pretraining
Authors:Brian Christian, Jessica A. F. Thompson, Elle Michelle Yang, Vincent Adam, Hannah Rose Kirk, Christopher Summerfield, Tsvetomira Dumbalska
View a PDF of the paper titled Reward Models Inherit Value Biases from Pretraining, by Brian Christian and 6 other authors
View PDF
HTML (experimental)
Abstract:Reward models (RMs) are central to aligning large language models (LLMs) with human values but have received less attention than pre-trained and post-trained LLMs themselves. Because RMs are initialized from LLMs, they inherit representations that shape their behavior, but the nature and extent of this influence remain understudied. In a comprehensive study of 10 leading open-weight RMs using validated psycholinguistic corpora, we show that RMs exhibit significant differences along multiple dimensions of human value as a function of their base model. Using the "Big Two" psychological axes, we show a robust preference of Llama RMs for "agency" and a corresponding robust preference of Gemma RMs for "communion." This phenomenon holds even when the preference data and finetuning process are identical, and we trace it back to the logits of the respective instruction-tuned and pre-trained models. These log-probability differences themselves can be formulated as an implicit RM; we derive usable implicit reward scores and show that they exhibit the very same agency/communion difference. We run experiments training RMs with ablations for preference data source and quantity, which demonstrate that this effect is not only repeatable but surprisingly durable. Despite RMs being designed to represent human preferences, our evidence shows that their outputs are influenced by the pretrained LLMs on which they are based. This work underscores the importance of safety and alignment efforts at the pretraining stage, and makes clear that open-source developers' choice of base model is as much a consideration of values as of performance.
Subjects:
Machine Learning (cs.LG); Artificial Intelligence (cs.AI); Computation and Language (cs.CL); Computers and Society (cs.CY)
Cite as:
arXiv:2601.20838 [cs.LG]
(or
arXiv:2601.20838v1 [cs.LG] for this version)
https://doi.org/10.48550/arXiv.2601.20838
Focus to learn more
arXiv-issued DOI via DataCite
Submission history From: Brian Christian [view email]          [v1]
Wed, 28 Jan 2026 18:40:29 UTC (4,017 KB)
[v2]
Sun, 1 Mar 2026 22:52:13 UTC (2,867 KB)



## 2601.20218

准入 2+2+2=6：terminalflowreward平铺错归因+统一探索对时间noise不匹配→ODE intermediatecleanrewardgain及timestep stochasticity校准→GRPO需考虑trajectoryfeedback与噪声共同预算。

https://arxiv.org/abs/2601.20218v1
arXiv:2601.20218v1 (cs)
[Submitted on 28 Jan 2026 (this version), latest version 25 Feb 2026 (v2)]
Title:DenseGRPO: From Sparse to Dense Reward for Flow Matching Model Alignment
Authors:Haoyou Deng, Keyu Yan, Chaojie Mao, Xiang Wang, Yu Liu, Changxin Gao, Nong Sang
View a PDF of the paper titled DenseGRPO: From Sparse to Dense Reward for Flow Matching Model Alignment, by Haoyou Deng and 6 other authors
View PDF
HTML (experimental)
Abstract:Recent GRPO-based approaches built on flow matching models have shown remarkable improvements in human preference alignment for text-to-image generation. Nevertheless, they still suffer from the sparse reward problem: the terminal reward of the entire denoising trajectory is applied to all intermediate steps, resulting in a mismatch between the global feedback signals and the exact fine-grained contributions at intermediate denoising steps. To address this issue, we introduce \textbf{DenseGRPO}, a novel framework that aligns human preference with dense rewards, which evaluates the fine-grained contribution of each denoising step. Specifically, our approach includes two key components: (1) we propose to predict the step-wise reward gain as dense reward of each denoising step, which applies a reward model on the intermediate clean images via an ODE-based approach. This manner ensures an alignment between feedback signals and the contributions of individual steps, facilitating effective training; and (2) based on the estimated dense rewards, a mismatch drawback between the uniform exploration setting and the time-varying noise intensity in existing GRPO-based methods is revealed, leading to an inappropriate exploration space. Thus, we propose a reward-aware scheme to calibrate the exploration space by adaptively adjusting a timestep-specific stochasticity injection in the SDE sampler, ensuring a suitable exploration space at all timesteps. Extensive experiments on multiple standard benchmarks demonstrate the effectiveness of the proposed DenseGRPO and highlight the critical role of the valid dense rewards in flow matching model alignment.
Comments:
Accepted by ICLR 2026
Subjects:
Computer Vision and Pattern Recognition (cs.CV)
Cite as:
arXiv:2601.20218 [cs.CV]
(or
arXiv:2601.20218v1 [cs.CV] for this version)
https://doi.org/10.48550/arXiv.2601.20218
Focus to learn more
arXiv-issued DOI via DataCite
Submission history From: Haoyou Deng [view email]          [v1]
Wed, 28 Jan 2026 03:39:05 UTC (1,896 KB)
[v2]
Wed, 25 Feb 2026 11:25:17 UTC (1,897 KB)



## 2601.20802

准入 2+2+2=6：scalarRLVR丢richtextfeedback→反馈conditionedselfteacher蒸馏densepolicytoken信号→不需externalRM但需feedback有效性和teacher泄露边界；科学实验不纳当前。

https://arxiv.org/abs/2601.20802v1
arXiv:2601.20802v1 (cs)
[Submitted on 28 Jan 2026 (this version), latest version 16 Feb 2026 (v2)]
Title:Reinforcement Learning via Self-Distillation
Authors:Jonas Hübotter, Frederike Lübeck, Lejs Behric, Anton Baumann, Marco Bagatella, Daniel Marta, Ido Hakimi, Idan Shenfeld, Thomas Kleine Buening, Carlos Guestrin, Andreas Krause
View a PDF of the paper titled Reinforcement Learning via Self-Distillation, by Jonas H\"ubotter and 10 other authors
View PDF
HTML (experimental)
Abstract:Large language models are increasingly post-trained with reinforcement learning in verifiable domains such as code and math. Yet, current methods for reinforcement learning with verifiable rewards (RLVR) learn only from a scalar outcome reward per attempt, creating a severe credit-assignment bottleneck. Many verifiable environments actually provide rich textual feedback, such as runtime errors or judge evaluations, that explain why an attempt failed. We formalize this setting as reinforcement learning with rich feedback and introduce Self-Distillation Policy Optimization (SDPO), which converts tokenized feedback into a dense learning signal without any external teacher or explicit reward model. SDPO treats the current model conditioned on feedback as a self-teacher and distills its feedback-informed next-token predictions back into the policy. In this way, SDPO leverages the model's ability to retrospectively identify its own mistakes in-context. Across scientific reasoning, tool use, and competitive programming on LiveCodeBench v6, SDPO improves sample efficiency and final accuracy over strong RLVR baselines. Notably, SDPO also outperforms baselines in standard RLVR environments that only return scalar feedback by using successful rollouts as implicit feedback for failed attempts. Finally, applying SDPO to individual questions at test time accelerates discovery on difficult binary-reward tasks, achieving the same discovery probability as best-of-k sampling or multi-turn conversations with 3x fewer attempts.
Subjects:
Machine Learning (cs.LG); Artificial Intelligence (cs.AI)
Cite as:
arXiv:2601.20802 [cs.LG]
(or
arXiv:2601.20802v1 [cs.LG] for this version)
https://doi.org/10.48550/arXiv.2601.20802
Focus to learn more
arXiv-issued DOI via DataCite
Submission history From: Jonas Hübotter [view email]          [v1]
Wed, 28 Jan 2026 17:45:12 UTC (1,009 KB)
[v2]
Mon, 16 Feb 2026 14:49:34 UTC (2,122 KB)



## 2601.20615

准入 2+2+2=6；安全深入：RAGcontext poisoning除错误外可诱导长输出耗能→resourceabuse能逃过仅内容正确性检查；核outputbudget/latency/energy端到端。

https://arxiv.org/abs/2601.20615v1
arXiv:2601.20615v1 (cs)
A newer version of this paper has been withdrawn by Tianyue Jiang
[Submitted on 28 Jan 2026 (this version), latest version 2 Feb 2026 (v3)]
Title:DRAINCODE: Stealthy Energy Consumption Attacks on Retrieval-Augmented Code Generation via Context Poisoning
Authors:Yanlin Wang, Jiadong Wu, Tianyue Jiang, Mingwei Liu, Jiachi Chen, Chong Wang, Ensheng Shi, Xilin Liu, Yuchi Ma, Zibin Zheng
View a PDF of the paper titled DRAINCODE: Stealthy Energy Consumption Attacks on Retrieval-Augmented Code Generation via Context Poisoning, by Yanlin Wang and 9 other authors
View PDF
HTML (experimental)
Abstract:Large language models (LLMs) have demonstrated impressive capabilities in code generation by leveraging retrieval-augmented generation (RAG) methods. However, the computational costs associated with LLM inference, particularly in terms of latency and energy consumption, have received limited attention in the security context. This paper introduces DrainCode, the first adversarial attack targeting the computational efficiency of RAG-based code generation systems. By strategically poisoning retrieval contexts through a mutation-based approach, DrainCode forces LLMs to produce significantly longer outputs, thereby increasing GPU latency and energy consumption. We evaluate the effectiveness of DrainCode across multiple models. Our experiments show that DrainCode achieves up to an 85% increase in latency, a 49% increase in energy consumption, and more than a 3x increase in output length compared to the baseline. Furthermore, we demonstrate the generalizability of the attack across different prompting strategies and its effectiveness compared to different defenses. The results highlight DrainCode as a potential method for increasing the computational overhead of LLMs, making it useful for evaluating LLM security in resource-constrained environments. We provide code and data at this https URL.
Comments:
12 pages, 4 figures
Subjects:
Software Engineering (cs.SE)
Cite as:
arXiv:2601.20615 [cs.SE]
(or
arXiv:2601.20615v1 [cs.SE] for this version)
https://doi.org/10.48550/arXiv.2601.20615
Focus to learn more
arXiv-issued DOI via DataCite
Submission history From: Tianyue Jiang [view email]          [v1]
Wed, 28 Jan 2026 13:51:00 UTC (300 KB)
[v2]
Thu, 29 Jan 2026 02:59:26 UTC (1 KB) (withdrawn)
[v3]
Mon, 2 Feb 2026 07:41:03 UTC (300 KB)



## 2601.20327

准入 2+2+2=6：pairwiseRMbench好不等RL可用→pointwisecriterion+twostagerollout检验BestofN/downstreamRL→评价协议与训练credit需对齐，不能仅榜单选RM。

https://arxiv.org/abs/2601.20327v1
arXiv:2601.20327v1 (cs)
[Submitted on 28 Jan 2026 (this version), latest version 31 Jan 2026 (v2)]
Title:CE-RM: A Pointwise Generative Reward Model Optimized via Two-Stage Rollout and Unified Criteria
Authors:Xinyu Hu, Yancheng He, Weixun Wang, Tao Feng, Li Lin, Jiashun Liu, Wenbo Su, Bo Zheng, Xiaojun Wan
View a PDF of the paper titled CE-RM: A Pointwise Generative Reward Model Optimized via Two-Stage Rollout and Unified Criteria, by Xinyu Hu and 8 other authors
View PDF
HTML (experimental)
Abstract:Automatic evaluation is crucial yet challenging for open-ended natural language generation, especially when rule-based metrics are infeasible. Compared with traditional methods, the recent LLM-as-a-Judge paradigms enable better and more flexible evaluation, and show promise as generative reward models for reinforcement learning. However, prior work has revealed a notable gap between their seemingly impressive benchmark performance and actual effectiveness in RL practice. We attribute this issue to some limitations in existing studies, including the dominance of pairwise evaluation and inadequate optimization of evaluation criteria. Therefore, we propose CE-RM-4B, a pointwise generative reward model trained with a dedicated two-stage rollout method, and adopting unified query-based criteria. Using only about 5.7K high-quality data curated from the open-source preference dataset, our CE-RM-4B achieves superior performance on diverse reward model benchmarks, especially in Best-of-N scenarios, and delivers more effective improvements in downstream RL practice.
Comments:
Under Review
Subjects:
Computation and Language (cs.CL)
Cite as:
arXiv:2601.20327 [cs.CL]
(or
arXiv:2601.20327v1 [cs.CL] for this version)
https://doi.org/10.48550/arXiv.2601.20327
Focus to learn more
arXiv-issued DOI via DataCite
Submission history From: Xinyu Hu [view email]          [v1]
Wed, 28 Jan 2026 07:46:13 UTC (69 KB)
[v2]
Sat, 31 Jan 2026 12:28:48 UTC (69 KB)



## 2601.20312

准入 2+1+2=5：MCprocesssupervision贵且reasonerverifiergap→主动最小gap导入processsignals；具体signal定义未由名称证明，必要方法核。

https://arxiv.org/abs/2601.20312v1
arXiv:2601.20312v1 (cs)
[Submitted on 28 Jan 2026 (this version), latest version 2 Feb 2026 (v2)]
Title:SAPO: Self-Adaptive Process Optimization Makes Small Reasoners Stronger
Authors:Kaiyuan Chen, Guangmin Zheng, Jin Wang, Xiaobing Zhou, Xuejie Zhang
View a PDF of the paper titled SAPO: Self-Adaptive Process Optimization Makes Small Reasoners Stronger, by Kaiyuan Chen and 4 other authors
View PDF
HTML (experimental)
Abstract:Existing self-evolution methods overlook the influence of fine-grained reasoning steps, which leads to the reasoner-verifier gap. The computational inefficiency of Monte Carlo (MC) process supervision further exacerbates the difficulty in mitigating the gap. Motivated by the Error-Related Negativity (ERN), which the reasoner can localize error following incorrect decisions, guiding rapid adjustments, we propose a Self-Adaptive Process Optimization (SAPO) method for self-improvement in Small Language Models (SLMs). SAPO adaptively and efficiently introduces process supervision signals by actively minimizing the reasoner-verifier gap rather than relying on inefficient MC estimations. Extensive experiments demonstrate that the proposed method outperforms most existing self-evolution methods on two challenging task types: mathematics and code. Additionally, to further investigate SAPO's impact on verifier performance, this work introduces two new benchmarks for process reward models in both mathematical and coding tasks.
Comments:
Accepted by AAAI 2026
Subjects:
Computation and Language (cs.CL)
Cite as:
arXiv:2601.20312 [cs.CL]
(or
arXiv:2601.20312v1 [cs.CL] for this version)
https://doi.org/10.48550/arXiv.2601.20312
Focus to learn more
arXiv-issued DOI via DataCite
Submission history From: Kaiyuan Chen [view email]          [v1]
Wed, 28 Jan 2026 07:04:30 UTC (848 KB)
[v2]
Mon, 2 Feb 2026 10:36:52 UTC (810 KB)



## 2601.20730

准入 2+2+2=6：staticretrieval长窗强不等动态交互synthesis→controlled environmentrollout揭示必要信息token数胜过碎片化→toolresponse density与memoryturn不同压力。

https://arxiv.org/abs/2601.20730v1
arXiv:2601.20730v1 (cs)
[Submitted on 28 Jan 2026 (this version), latest version 30 Jan 2026 (v3)]
Title:AgentLongBench: A Controllable Long Benchmark For Long-Contexts Agents via Environment Rollouts
Authors:Shicheng Fang, Yuxin Wang, XiaoRan Liu, Jiahao Lu, Chuanyuan Tan, Xinchi Chen, Yining Zheng. Xuanjing Huang, Xipeng Qiu
View a PDF of the paper titled AgentLongBench: A Controllable Long Benchmark For Long-Contexts Agents via Environment Rollouts, by Shicheng Fang and 7 other authors
View PDF
Abstract:The evolution of Large Language Models (LLMs) into autonomous agents necessitates the management of extensive, dynamic contexts. Current benchmarks, however, remain largely static, relying on passive retrieval tasks that fail to simulate the complexities of agent-environment interaction, such as non-linear reasoning and iterative feedback. To address this, we introduce \textbf{AgentLongBench}, which evaluates agents through simulated environment rollouts based on Lateral Thinking Puzzles. This framework generates rigorous interaction trajectories across knowledge-intensive and knowledge-free scenarios. Experiments with state-of-the-art models and memory systems (32K to 4M tokens) expose a critical weakness: while adept at static retrieval, agents struggle with the dynamic information synthesis essential for workflows. Our analysis indicates that this degradation is driven by the minimum number of tokens required to resolve a query. This factor explains why the high information density inherent in massive tool responses poses a significantly greater challenge than the memory fragmentation typical of long-turn dialogues.
Comments:
26 pages
Subjects:
Computation and Language (cs.CL)
Cite as:
arXiv:2601.20730 [cs.CL]
(or
arXiv:2601.20730v1 [cs.CL] for this version)
https://doi.org/10.48550/arXiv.2601.20730
Focus to learn more
arXiv-issued DOI via DataCite
Submission history From: Yuxin Wang [view email]          [v1]
Wed, 28 Jan 2026 16:05:44 UTC (4,696 KB)
[v2]
Thu, 29 Jan 2026 12:32:51 UTC (4,696 KB)
[v3]
Fri, 30 Jan 2026 09:18:17 UTC (4,696 KB)



## 2601.20613

贡献关闭：daily104task/767rubrics附件/latentinstruction/iterativerefinement覆盖及80.1%judgeagreement；未提供新主线失效条件，任务多样性本身不准入。

https://arxiv.org/abs/2601.20613v1
arXiv:2601.20613v1 (cs)
[Submitted on 28 Jan 2026 (this version), latest version 30 Jan 2026 (v2)]
Title:AgentIF-OneDay: A Task-level Instruction-Following Benchmark for General AI Agents in Daily Scenarios
Authors:Kaiyuan Chen, Qimin Wu, Taiyu Hou, Tianhao Tang, Xueyu Hu, Yuchen Hou, Bikun Li, Chengming Qian, Guoyin Wang, Haolin Chen, Haotong Tian, Haoye Zhang, Haoyu Bian, Hongbing Pan, Hongkang Zhang, Hongyi Zhou, Jiaqi Cai, Jiewu Rao, Jiyuan Ren, Keduan Huang, Lucia Zhu Huang, Mingyu Yuan, Naixu Guo, Qicheng Tang, Qinyan Zhang, Shuai Chen, Siheng Chen, Ting Ting Li, Xiaoxing Guo, Yaocheng Zuo, Yaoqi Guo, Yinan Wang, Yinzhou Yu, Yize Wang, Yuan Jiang, Yuan Tian, Yuanshuo Zhang, Yuxuan Liu, Yvette Yan Zeng, Zenyu Shan, Zihan Yin, Xiaobo Hu, Yang Liu, Yixin Ren, Yuan Gong
View a PDF of the paper titled AgentIF-OneDay: A Task-level Instruction-Following Benchmark for General AI Agents in Daily Scenarios, by Kaiyuan Chen and 44 other authors
View PDF
HTML (experimental)
Abstract:The capacity of AI agents to effectively handle tasks of increasing duration and complexity continues to grow, demonstrating exceptional performance in coding, deep research, and complex problem-solving evaluations. However, in daily scenarios, the perception of these advanced AI capabilities among general users remains limited. We argue that current evaluations prioritize increasing task difficulty without sufficiently addressing the diversity of agentic tasks necessary to cover the daily work, life, and learning activities of a broad demographic. To address this, we propose AgentIF-OneDay, aimed at determining whether general users can utilize natural language instructions and AI agents to complete a diverse array of daily tasks. These tasks require not only solving problems through dialogue but also understanding various attachment types and delivering tangible file-based results. The benchmark is structured around three user-centric categories: Open Workflow Execution, which assesses adherence to explicit and complex workflows; Latent Instruction, which requires agents to infer implicit instructions from attachments; and Iterative Refinement, which involves modifying or expanding upon ongoing work. We employ instance-level rubrics and a refined evaluation pipeline that aligns LLM-based verification with human judgment, achieving an 80.1% agreement rate using Gemini-3-Pro. AgentIF-OneDay comprises 104 tasks covering 767 scoring points. We benchmarked four leading general AI agents and found that agent products built based on APIs and ChatGPT agents based on agent RL remain in the first tier simultaneously. Leading LLM APIs and open-source models have internalized agentic capabilities, enabling AI application teams to develop cutting-edge Agent products.
Comments:
17 pages, 8 figures
Subjects:
Computation and Language (cs.CL)
Cite as:
arXiv:2601.20613 [cs.CL]
(or
arXiv:2601.20613v1 [cs.CL] for this version)
https://doi.org/10.48550/arXiv.2601.20613
Focus to learn more
arXiv-issued DOI via DataCite
Submission history From: Xueyu Hu [view email]          [v1]
Wed, 28 Jan 2026 13:49:18 UTC (6,251 KB)
[v2]
Fri, 30 Jan 2026 13:36:46 UTC (6,251 KB)



## 2601.20335

准入 2+2+2=6：onlineGUI有随机噪声且reset不完善混淆评价→可复现reset+noise子集核Agent在线执行可靠性；不能1080tasks规模独立准入。

https://arxiv.org/abs/2601.20335v1
arXiv:2601.20335v1 (cs)
[Submitted on 28 Jan 2026 (this version), latest version 29 Jan 2026 (v2)]
Title:MobileBench-OL: A Comprehensive Chinese Benchmark for Evaluating Mobile GUI Agents in Real-World Environment
Authors:Qinzhuo Wu, Zhizhuo Yang, Hanhao Li, Pengzhi Gao, Wei Liu, Jian Luan
View a PDF of the paper titled MobileBench-OL: A Comprehensive Chinese Benchmark for Evaluating Mobile GUI Agents in Real-World Environment, by Qinzhuo Wu and 5 other authors
View PDF
HTML (experimental)
Abstract:Recent advances in mobile Graphical User Interface (GUI) agents highlight the growing need for comprehensive evaluation benchmarks. While new online benchmarks offer more realistic testing than offline ones, they tend to focus on the agents' task instruction-following ability while neglecting their reasoning and exploration ability. Moreover, these benchmarks do not consider the random noise in real-world mobile environments. This leads to a gap between benchmarks and real-world environments. To addressing these limitations, we propose MobileBench-OL, an online benchmark with 1080 tasks from 80 Chinese apps. It measures task execution, complex reasoning, and noise robustness of agents by including 5 subsets, which set multiple evaluation dimensions. We also provide an auto-eval framework with a reset mechanism, enabling stable and repeatable real-world benchmarking. Evaluating 12 leading GUI agents on MobileBench-OL shows significant room for improvement to meet real-world requirements. Human evaluation further confirms that MobileBench-OL can reliably measure the performance of leading GUI agents in real environments. Our data and code will be released upon acceptance.
Subjects:
Computation and Language (cs.CL); Artificial Intelligence (cs.AI)
Cite as:
arXiv:2601.20335 [cs.CL]
(or
arXiv:2601.20335v1 [cs.CL] for this version)
https://doi.org/10.48550/arXiv.2601.20335
Focus to learn more
arXiv-issued DOI via DataCite
Submission history From: Qinzhuo Wu [view email]          [v1]
Wed, 28 Jan 2026 07:49:48 UTC (3,636 KB)
[v2]
Thu, 29 Jan 2026 02:32:46 UTC (3,636 KB)



## 2601.20858

准入 2+2+2=6；评价反证深入：FLORES训练污染target-side recall跨未训练translationdirection且sourceparaphrase仍存→方向split不等无污染，需要targetmemorization诊断。

https://arxiv.org/abs/2601.20858v1
arXiv:2601.20858v1 (cs)
[Submitted on 28 Jan 2026]
Title:When Flores Bloomz Wrong: Cross-Direction Contamination in Machine Translation Evaluation
Authors:David Tan, Pinzhen Chen, Josef van Genabith, Koel Dutta Chowdhury
View a PDF of the paper titled When Flores Bloomz Wrong: Cross-Direction Contamination in Machine Translation Evaluation, by David Tan and 3 other authors
View PDF
HTML (experimental)
Abstract:Large language models (LLMs) can be benchmark-contaminated, resulting in inflated scores that mask memorization as generalization, and in multilingual settings, this memorization can even transfer to "uncontaminated" languages. Using the FLORES-200 translation benchmark as a diagnostic, we study two 7-8B instruction-tuned multilingual LLMs: Bloomz, which was trained on FLORES, and Llama as an uncontaminated control. We confirm Bloomz's FLORES contamination and demonstrate that machine translation contamination can be cross-directional, artificially boosting performance in unseen translation directions due to target-side memorization. Further analysis shows that recall of memorized references often persists despite various source-side perturbation efforts like paraphrasing and named entity replacement. However, replacing named entities leads to a consistent decrease in BLEU, suggesting an effective probing method for memorization in contaminated models.
Comments:
5 pages of content, 15 total. 5 figures, 12 tables total. Accepted to EACL 2026 main conference. Code can be found here: this http URL
Subjects:
Computation and Language (cs.CL)
Cite as:
arXiv:2601.20858 [cs.CL]
(or
arXiv:2601.20858v1 [cs.CL] for this version)
https://doi.org/10.48550/arXiv.2601.20858
Focus to learn more
arXiv-issued DOI via DataCite
Submission history From: David Tan [view email]          [v1]
Wed, 28 Jan 2026 18:56:21 UTC (301 KB)



## 2601.20831

准入 2+1+2=5：embodiedstrictmemory/compute不能offline无限store→trainable μ head在线retain/update/discard，比较offlineexpertvsRL及longinstruction条件；不是RAG索引本身。

https://arxiv.org/abs/2601.20831v1
arXiv:2601.20831v1 (cs)
[Submitted on 28 Jan 2026]
Title:MemCtrl: Using MLLMs as Active Memory Controllers on Embodied Agents
Authors:Vishnu Sashank Dorbala, Dinesh Manocha
View a PDF of the paper titled MemCtrl: Using MLLMs as Active Memory Controllers on Embodied Agents, by Vishnu Sashank Dorbala and 1 other authors
View PDF
HTML (experimental)
Abstract:Foundation models rely on in-context learning for personalized decision making. The limited size of this context window necessitates memory compression and retrieval systems like RAG. These systems however often treat memory as large offline storage spaces, which is unfavorable for embodied agents that are expected to operate under strict memory and compute constraints, online. In this work, we propose MemCtrl, a novel framework that uses Multimodal Large Language Models (MLLMs) for pruning memory online. MemCtrl augments MLLMs with a trainable memory head \mu that acts as a gate to determine which observations or reflections to retain, update, or discard during exploration. We evaluate with training two types of \mu, 1) via an offline expert, and 2) via online RL, and observe significant improvement in overall embodied task completion ability on \mu-augmented MLLMs. In particular, on augmenting two low performing MLLMs with MemCtrl on multiple subsets of the EmbodiedBench benchmark, we observe that \mu-augmented MLLMs show an improvement of around 16% on average, with over 20% on specific instruction subsets. Finally, we present a qualitative analysis on the memory fragments collected by \mu, noting the superior performance of \mu augmented MLLMs on long and complex instruction types.
Subjects:
Artificial Intelligence (cs.AI); Robotics (cs.RO)
Cite as:
arXiv:2601.20831 [cs.AI]
(or
arXiv:2601.20831v1 [cs.AI] for this version)
https://doi.org/10.48550/arXiv.2601.20831
Focus to learn more
arXiv-issued DOI via DataCite
Submission history From: Vishnu Sashank Dorbala [view email]          [v1]
Wed, 28 Jan 2026 18:31:17 UTC (6,248 KB)



## 2601.20649

准入 2+2+2=6：generalQA无法verify→goldCoTsuffix在currentprefix条件下likelihood作processreward→需要清楚faithfulnessproxy非truth，防参考与语义等价限制。

https://arxiv.org/abs/2601.20649v1
arXiv:2601.20649v1 (cs)
[Submitted on 28 Jan 2026]
Title:P2S: Probabilistic Process Supervision for General-Domain Reasoning Question Answering
Authors:Wenlin Zhong, Chengyuan Liu, Yiquan Wu, Bovin Tan, Changlong Sun, Yi Wang, Xiaozhong Liu, Kun Kuang
View a PDF of the paper titled P2S: Probabilistic Process Supervision for General-Domain Reasoning Question Answering, by Wenlin Zhong and 7 other authors
View PDF
HTML (experimental)
Abstract:While reinforcement learning with verifiable rewards (RLVR) has advanced LLM reasoning in structured domains like mathematics and programming, its application to general-domain reasoning tasks remains challenging due to the absence of verifiable reward signals. To this end, methods like Reinforcement Learning with Reference Probability Reward (RLPR) have emerged, leveraging the probability of generating the final answer as a reward signal. However, these outcome-focused approaches neglect crucial step-by-step supervision of the reasoning process itself. To address this gap, we introduce Probabilistic Process Supervision (P2S), a novel self-supervision framework that provides fine-grained process rewards without requiring a separate reward model or human-annotated reasoning steps. During reinforcement learning, P2S synthesizes and filters a high-quality reference reasoning chain (gold-CoT). The core of our method is to calculate a Path Faithfulness Reward (PFR) for each reasoning step, which is derived from the conditional probability of generating the gold-CoT's suffix, given the model's current reasoning prefix. Crucially, this PFR can be flexibly integrated with any outcome-based reward, directly tackling the reward sparsity problem by providing dense guidance. Extensive experiments on reading comprehension and medical Question Answering benchmarks show that P2S significantly outperforms strong baselines.
Subjects:
Computation and Language (cs.CL)
Cite as:
arXiv:2601.20649 [cs.CL]
(or
arXiv:2601.20649v1 [cs.CL] for this version)
https://doi.org/10.48550/arXiv.2601.20649
Focus to learn more
arXiv-issued DOI via DataCite
Submission history From: Wenlin Zhong [view email]          [v1]
Wed, 28 Jan 2026 14:35:20 UTC (2,989 KB)



## 2601.20614

准入 2+2+2=6：GRPO harderquestions更新量可能隐式小→difficultybalancedgroupadv与questionweight+answerpreserving harderrewrite→不能只增harddata而忽略梯度量。

https://arxiv.org/abs/2601.20614v1
arXiv:2601.20614v1 (cs)
[Submitted on 28 Jan 2026]
Title:Harder Is Better: Boosting Mathematical Reasoning via Difficulty-Aware GRPO and Multi-Aspect Question Reformulation
Authors:Yanqi Dai, Yuxiang Ji, Xiao Zhang, Yong Wang, Xiangxiang Chu, Zhiwu Lu
View a PDF of the paper titled Harder Is Better: Boosting Mathematical Reasoning via Difficulty-Aware GRPO and Multi-Aspect Question Reformulation, by Yanqi Dai and 5 other authors
View PDF
HTML (experimental)
Abstract:Reinforcement Learning with Verifiable Rewards (RLVR) offers a robust mechanism for enhancing mathematical reasoning in large models. However, we identify a systematic lack of emphasis on more challenging questions in existing methods from both algorithmic and data perspectives, despite their importance for refining underdeveloped capabilities. Algorithmically, widely used Group Relative Policy Optimization (GRPO) suffers from an implicit imbalance where the magnitude of policy updates is lower for harder questions. Data-wise, augmentation approaches primarily rephrase questions to enhance diversity without systematically increasing intrinsic difficulty. To address these issues, we propose a two-dual MathForge framework to improve mathematical reasoning by targeting harder questions from both perspectives, which comprises a Difficulty-Aware Group Policy Optimization (DGPO) algorithm and a Multi-Aspect Question Reformulation (MQR) strategy. Specifically, DGPO first rectifies the implicit imbalance in GRPO via difficulty-balanced group advantage estimation, and further prioritizes harder questions by difficulty-aware question-level weighting. Meanwhile, MQR reformulates questions across multiple aspects to increase difficulty while maintaining the original gold answer. Overall, MathForge forms a synergistic loop: MQR expands the data frontier, and DGPO effectively learns from the augmented data. Extensive experiments show that MathForge significantly outperforms existing methods on various mathematical reasoning tasks. The code and augmented data are all available at this https URL.
Comments:
Accepted for ICLR 2026
Subjects:
Artificial Intelligence (cs.AI); Computation and Language (cs.CL)
Cite as:
arXiv:2601.20614 [cs.AI]
(or
arXiv:2601.20614v1 [cs.AI] for this version)
https://doi.org/10.48550/arXiv.2601.20614
Focus to learn more
arXiv-issued DOI via DataCite
Submission history From: Yanqi Dai [view email]          [v1]
Wed, 28 Jan 2026 13:49:23 UTC (111 KB)



## 2601.20467

准入 2+2+2=6：semantic缩短与tokenprune冲突→逻辑cue-awarepruner+distributionalignment →压缩率必须绑定reasoningcue与inferencedistribution；单MATH局部。

https://arxiv.org/abs/2601.20467v1
arXiv:2601.20467v1 (cs)
[Submitted on 28 Jan 2026]
Title:CtrlCoT: Dual-Granularity Chain-of-Thought Compression for Controllable Reasoning
Authors:Zhenxuan Fan, Jie Cao, Yang Dai, Zheqi Lv, Wenqiao Zhang, Zhongle Xie, Peng LU, Beng Chin Ooi
View a PDF of the paper titled CtrlCoT: Dual-Granularity Chain-of-Thought Compression for Controllable Reasoning, by Zhenxuan Fan and 7 other authors
View PDF
HTML (experimental)
Abstract:Chain-of-thought (CoT) prompting improves LLM reasoning but incurs high latency and memory cost due to verbose traces, motivating CoT compression with preserved correctness. Existing methods either shorten CoTs at the semantic level, which is often conservative, or prune tokens aggressively, which can miss task-critical cues and degrade accuracy. Moreover, combining the two is non-trivial due to sequential dependency, task-agnostic pruning, and distribution mismatch. We propose \textbf{CtrlCoT}, a dual-granularity CoT compression framework that harmonizes semantic abstraction and token-level pruning through three components: Hierarchical Reasoning Abstraction produces CoTs at multiple semantic granularities; Logic-Preserving Distillation trains a logic-aware pruner to retain indispensable reasoning cues (e.g., numbers and operators) across pruning ratios; and Distribution-Alignment Generation aligns compressed traces with fluent inference-time reasoning styles to avoid fragmentation. On MATH-500 with Qwen2.5-7B-Instruct, CtrlCoT uses 30.7\% fewer tokens while achieving 7.6 percentage points higher than the strongest baseline, demonstrating more efficient and reliable reasoning. Our code will be publicly available at this https URL.
Comments:
16 pages, 9 figures, 11 tables
Subjects:
Artificial Intelligence (cs.AI); Computation and Language (cs.CL)
Cite as:
arXiv:2601.20467 [cs.AI]
(or
arXiv:2601.20467v1 [cs.AI] for this version)
https://doi.org/10.48550/arXiv.2601.20467
Focus to learn more
arXiv-issued DOI via DataCite
Submission history From: Zhenxuan Fan [view email]          [v1]
Wed, 28 Jan 2026 10:38:49 UTC (3,686 KB)



## 2601.20282

准入 2+1+2=5：contextdefiningkeyword在attention neurons可选择性编码/提取→核因果cue-basedretrieval而非心理类比；unlearning应用不即eraseguarantee。

https://arxiv.org/abs/2601.20282v1
arXiv:2601.20282v1 (cs)
[Submitted on 28 Jan 2026]
Title:Memory Retrieval in Transformers: Insights from The Encoding Specificity Principle
Authors:Viet Hung Dinh, Ming Ding, Youyang Qu, Kanchana Thilakarathna
View a PDF of the paper titled Memory Retrieval in Transformers: Insights from The Encoding Specificity Principle, by Viet Hung Dinh and 3 other authors
View PDF
HTML (experimental)
Abstract:While explainable artificial intelligence (XAI) for large language models (LLMs) remains an evolving field with many unresolved questions, increasing regulatory pressures have spurred interest in its role in ensuring transparency, accountability, and privacy-preserving machine unlearning. Despite recent advances in XAI have provided some insights, the specific role of attention layers in transformer based LLMs remains underexplored. This study investigates the memory mechanisms instantiated by attention layers, drawing on prior research in psychology and computational psycholinguistics that links Transformer attention to cue based retrieval in human memory. In this view, queries encode the retrieval context, keys index candidate memory traces, attention weights quantify cue trace similarity, and values carry the encoded content, jointly enabling the construction of a context representation that precedes and facilitates memory retrieval. Guided by the Encoding Specificity Principle, we hypothesize that the cues used in the initial stage of retrieval are instantiated as keywords. We provide converging evidence for this keywords-as-cues hypothesis. In addition, we isolate neurons within attention layers whose activations selectively encode and facilitate the retrieval of context-defining keywords. Consequently, these keywords can be extracted from identified neurons and further contribute to downstream applications such as unlearning.
Subjects:
Machine Learning (cs.LG)
Cite as:
arXiv:2601.20282 [cs.LG]
(or
arXiv:2601.20282v1 [cs.LG] for this version)
https://doi.org/10.48550/arXiv.2601.20282
Focus to learn more
arXiv-issued DOI via DataCite
Submission history From: Viet Hung Dinh [view email]          [v1]
Wed, 28 Jan 2026 05:58:09 UTC (574 KB)



## 2601.20276

准入 2+2+2=6：benignnearuniqueNIAH掩盖semanticinterference→document-IDaccess与QAuse分开并collisiontestednear-miss→ctx长度不能代替证据discrimination。

https://arxiv.org/abs/2601.20276v1
arXiv:2601.20276v1 (cs)
[Submitted on 28 Jan 2026]
Title:Beyond the Needle's Illusion: Decoupled Evaluation of Evidence Access and Use under Semantic Interference at 326M-Token Scale
Authors:Tianwei Lin, Zuyi Zhou, Xinda Zhao, Chenke Wang, Xiaohong Li, Yu Chen, Chuanrui Hu, Jian Pei, Yafeng Deng
View a PDF of the paper titled Beyond the Needle's Illusion: Decoupled Evaluation of Evidence Access and Use under Semantic Interference at 326M-Token Scale, by Tianwei Lin and 8 other authors
View PDF
HTML (experimental)
Abstract:Long-context LLM agents must access the right evidence from large environments and use it faithfully. However, the popular Needle-in-a-Haystack (NIAH) evaluation mostly measures benign span localization. The needle is near-unique, and the haystack is largely irrelevant. We introduce EverMemBench-S (EMB-S), an adversarial NIAH-style benchmark built on a 326M-token MemoryBank. While the full MemoryBank spans 326M tokens for retrieval-based (RAG) evaluation, we evaluate native long-context models only at scales that fit within each model's context window (up to 1M tokens in this work) to ensure a fair comparison. EMB-S pairs queries with collision-tested near-miss hard negatives and gold evidence sets spanning one or more documents, validated via human screening and LLM verification. We also propose a decoupled diagnostic protocol that reports evidence access (document-ID localization) separately from end-to-end QA quality under full-context prompting. This enables consistent diagnosis for both native long-context prompting and retrieval pipelines. Across a reference-corpus ladder from domain-isolated 64K contexts to a globally shared 326M-token environment, we observe a clear reality gap. Systems that saturate benign NIAH degrade sharply in evidence access under semantic interference. These results indicate that semantic discrimination, not context length alone, is the dominant bottleneck for long-context memory at scale.
Subjects:
Computation and Language (cs.CL); Artificial Intelligence (cs.AI)
Cite as:
arXiv:2601.20276 [cs.CL]
(or
arXiv:2601.20276v1 [cs.CL] for this version)
https://doi.org/10.48550/arXiv.2601.20276
Focus to learn more
arXiv-issued DOI via DataCite
Submission history From: Tianwei Lin [view email]          [v1]
Wed, 28 Jan 2026 05:44:00 UTC (1,192 KB)



## 2601.20103

准入 2+2+2=6；安全深入：rewardhack孤立分类低于contrastiveset检测且semanticcontext更难→judge协议、benignratio/cluster都影响安全检测；63%不是足够保证。

https://arxiv.org/abs/2601.20103v1
arXiv:2601.20103v1 (cs)
[Submitted on 27 Jan 2026]
Title:Benchmarking Reward Hack Detection in Code Environments via Contrastive Analysis
Authors:Darshan Deshpande, Anand Kannappan, Rebecca Qian
View a PDF of the paper titled Benchmarking Reward Hack Detection in Code Environments via Contrastive Analysis, by Darshan Deshpande and 2 other authors
View PDF
HTML (experimental)
Abstract:Recent advances in reinforcement learning for code generation have made robust environments essential to prevent reward hacking. As LLMs increasingly serve as evaluators in code-based RL, their ability to detect reward hacking remains understudied. In this paper, we propose a novel taxonomy of reward exploits spanning across 54 categories and introduce TRACE (Testing Reward Anomalies in Code Environments), a synthetically curated and human-verified benchmark containing 517 testing trajectories. Unlike prior work that evaluates reward hack detection in isolated classification scenarios, we contrast these evaluations with a more realistic, contrastive anomaly detection setup on TRACE. Our experiments reveal that models capture reward hacks more effectively in contrastive settings than in isolated classification settings, with GPT-5.2 with highest reasoning mode achieving the best detection rate at 63%, up from 45% in isolated settings on TRACE. Building on this insight, we demonstrate that state-of-the-art models struggle significantly more with semantically contextualized reward hacks compared to syntactically contextualized ones. We further conduct qualitative analyses of model behaviors, as well as ablation studies showing that the ratio of benign to hacked trajectories and analysis cluster sizes substantially impact detection performance. We release the benchmark and evaluation harness to enable the community to expand TRACE and evaluate their models.
Comments:
Dataset: this https URL
Subjects:
Software Engineering (cs.SE); Artificial Intelligence (cs.AI); Machine Learning (cs.LG)
Cite as:
arXiv:2601.20103 [cs.SE]
(or
arXiv:2601.20103v1 [cs.SE] for this version)
https://doi.org/10.48550/arXiv.2601.20103
Focus to learn more
arXiv-issued DOI via DataCite
Submission history From: Darshan Deshpande [view email]          [v1]
Tue, 27 Jan 2026 22:45:43 UTC (651 KB)


