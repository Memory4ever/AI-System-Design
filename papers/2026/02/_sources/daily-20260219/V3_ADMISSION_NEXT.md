# 本日第五批准入校准

原库存只查漏；以下六项已重核完整精确v1题摘，两个protocol仅有限补读决定核心，不因控制术语自动入选，其余具体潜在贡献明确后审必要证据。日期原identity字段已在本日DataCite记录，不借Updated/邻ID。

## 2602.15286v1 — AI-Paging: Lease-Based Execution Anchoring for Network-Exposed AI-as-a-Service

[精确v1](https://arxiv.org/html/2602.15286v1)

With AI-as-a-Service (AIaaS) now deployed across multiple providers and model tiers, selecting the appropriate model instance at run time is increasingly outside the end user’s knowledge and operational control. Accordingly, the6G service providers are envisioned to play a crucial role in exposing AIaaS in a setting where users submit only an intent while the network helps in the intent-to-model matching (resolution) and execution placement under policy, trust, and Quality of Service (QoS) constraints. The network role becomes to discover candidate execution endpoints and selects a suitable model/anchor under policy and QoS constraints in a process referred here to as AI-paging (by analogy to cellular call paging). In the proposed architecture, AI-paging is a control-plane transaction that resolves an intent into an AI service identity (AISI), a scoped session token (AIST), and an expiring admission lease (COMMIT) that authorizes user-plane steering to a selected AI execution anchor (AEXF) under a QoS binding.AI-Paging enforces two invariants: (i) lease-gated steering (without COMMIT, no steering state is installed) and (ii) make-before-break anchoring to support continuity and reliability of AIaaS services under dynamic network conditions. We prototype AI-Paging using existing control- and user-plane mechanisms (service-based control, QoS flows, and policy-based steering) with no new packet headers, ensuring compatibility with existing 3GPP-based exposure and management architectures, and evaluate transaction latency, relocation interruption, enforcement correctness under lease expiry, and audit-evidence overhead under mobility and failures.

准入校准理由：外部endpoint选择与network steering未绑定admission→lease-gated steering及make-before-break→可能需要atomic placement/steering边界；先查原执行条件是否超越成熟token/lease组合，不自动准入。

## 2602.15287v1 — Consistency-Preserving Diverse Video Generation

[精确v1](https://arxiv.org/html/2602.15287v1)

Text-to-video generation is expensive, so only a few samples are typically produced per prompt. In this low-sample regime, maximizing the value of each batch requires high cross-video diversity . Recent methods improve diversity for image generation, but for videos they often degrade within-video temporal consistency and require costly backpropagation through a video decoder. We propose a joint-sampling framework for flow-matching video generators that improves batch diversity while preserving temporal consistency. Our approach applies diversity-driven updates and then removes only the components that would decrease a temporal-consistency objective. To avoid image-space gradients, we compute both objectives with lightweight latent-space models, avoiding video decoding and decoder backpropagation. Experiments on a state-of-the-art text-to-video flow-matching model show diversity comparable to strong joint-sampling baselines while substantially improving temporal consistency and color naturalness. Code will be released.

准入校准理由：joint diversity gradient会损时间一致性→去除降低temporal proxy的梯度分量且latent objectives避decoder反传→具体batch diversity/within-video取舍。潜在2+2+2=6。

## 2602.15288v1 — AI Sessions for Network-Exposed AI-as-a-Service

[精确v1](https://arxiv.org/html/2602.15288v1)

Cloud-based Artificial Intelligence (AI) inference is increasingly latency- and context-sensitive, yet today’s AI-as-a-Service is typically consumed as an application-chosen endpoint, leaving the network to provide only best-effort transport. This decoupling prevents enforceable tail-latency guarantees, compute-aware admission control, and continuity under mobility. This paper proposes Network-Exposed AI-as-a-Service (NE-AIaaS) built around a new service primitive: the AI Session (AIS)—a contractual object that binds model identity, execution placement, transport Quality-of-Service (QoS), and consent/charging scope into a single lifecycle with explicit failure semantics. We introduce the AI Service Profile (ASP), a compact contract that expresses task modality and measurable service objectives (e.g., time-to-first-response/token, p99 latency, success probability) alongside privacy and mobility constraints. On this basis, we specify protocol-grade procedures for (i) DISCOVER (model/site discovery), (ii) AI PAGING (context-aware selection of execution anchor), (iii) two-phase PREPARE/COMMIT that atomically co-reserves compute and QoS resources, and (iv) make-before-break MIGRATION for session continuity. The design is standard-mappable to Common API Framework (CAPIF) style northbound exposure, ETSI Multi-access Edge Computing (MEC) execution substrates, 5G QoS flows for transport enforcement, and Network Data Analytics Function (NWDAF) style analytics for closed-loop paging/migration triggers.

准入校准理由：单endpoint best-effort未共同commitcompute/QoS→AIS对象与PREPARE/COMMIT co-reservation→可能改变partial failure合同；与15286不同family但不能继承原型实证，定点决定核心。

## 2602.15293v1 — The Information Geometry of Softmax: Probing and Steering

[精确v1](https://arxiv.org/html/2602.15293v1)

This paper concerns the question of how AI systems encode semantic structure into the geometric structure of their representation spaces. The motivating observation of this paper is that the natural geometry of these representation spaces should reflect the way models use representations to produce behavior. We focus on the important special case of representations that define softmax distributions. In this case, we argue that the natural geometry is information geometry. Our focus is on the role of information geometry on semantic encoding and the linear representation hypothesis. As an illustrative application, we develop dual steering , a method for robustly steering representations to exhibit a particular concept using linear probes. We prove that dual steering optimally modifies the target concept while minimizing changes to off-target concepts. Empirically, we find that dual steering enhances the controllability and stability of concept manipulation. Code is available at github.com/KihoPark/dual-steering .

准入校准理由：Euclidean representation steering忽略softmax behavior geometry→Bregman dual steering在特定probe目标下最小off-target改变→需要核softmaxrank/feasible/局部vs全局理论条件。潜在3+1+3=7，不借理论标签跳过证明。

## 2602.15322v1 — On Surprising Effectiveness of Masking Updates in Adaptive Optimizers

[精确v1](https://arxiv.org/html/2602.15322v1)

Training large language models (LLMs) relies almost exclusively on dense adaptive optimizers with increasingly sophisticated preconditioners. We challenge this by showing that randomly masking parameter updates can be highly effective, with a masked variant of RMSProp consistently outperforming recent state-of-the-art optimizers. Our analysis reveals that the random masking induces a curvature-dependent geometric regularization that smooths the optimization trajectory. Motivated by this finding, we introduce M omentum- a ligned g radient ma sking (Magma) , which modulates the masked updates using momentum-gradient alignment. Extensive LLM pre-training experiments show that Magma is a simple drop-in replacement for adaptive optimizers with consistent gains and negligible computational overhead. Notably, for the 1B model size, Magma reduces perplexity by over 19% and 9% compared to Adam and Muon, respectively.

准入校准理由：dense adaptive updates并非唯一合理→masking curvature regularization与momentum-gradient alignment→改变更新方向/噪声成本取舍。潜在2+2+2=6，朴素稀疏化与作者理论须分开。

## 2602.15327v1 — Prescriptive Scaling Reveals the Evolution of Language Model Capabilities

[精确v1](https://arxiv.org/html/2602.15327v1)

For deploying foundation models, practitioners increasingly need prescriptive scaling laws: given a pre-training compute budget, what downstream accuracy is attainable with contemporary post-training practice, and how stable is that mapping as the field evolves? Using large-scale observational evaluations with 5k observational and 2k newly sampled data on model performance, we estimate capability boundaries —high conditional quantiles of benchmark scores as a function of log pre-training FLOPs, via smoothed quantile regression with a monotone, saturating sigmoid parameterization. We validate the temporal reliability by fitting on earlier model generations and evaluating on later releases. Across various tasks, the estimated boundaries are mostly stable, with the exception of math reasoning that exhibits a consistently advancing boundary over time. We then extend our approach to analyze task-dependent saturation and to probe contamination-related shifts on math reasoning tasks. Finally, we introduce an efficient algorithm that recovers near-full-data frontiers using roughly 20\% of evaluation budget. Together, our work releases the Proteus-2k, the latest model performance evaluation dataset, and introduces a practical methodology for translating compute budgets into reliable performance expectations and for monitoring when capability boundaries shift across time.

准入校准理由：平均compute scaling不能指导post-training可达能力→高conditional quantile边界/时间外推与math推进反例→具体budget expectation不是每model保证。潜在2+1+3=6；currentv2定量2%/5%不借v1。
