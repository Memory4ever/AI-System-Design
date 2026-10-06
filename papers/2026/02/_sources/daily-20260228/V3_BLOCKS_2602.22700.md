[0] h5: Report GitHub Issue

[1] p: Content selection saved. Describe the issue below:

[2] h1: IMMACULATE: A Practical LLM Auditing Framework via Verifiable Computation

[3] h6: Abstract

[4] p: Commercial large language models are typically deployed as black-box API services, requiring users to trust providers to execute inference correctly and report token usage honestly. We present IMMACULATE, a practical auditing framework that detects economically motivated deviations-such as model substitution, quantization abuse, and token overbilling-without trusted hardware or access to model internals. IMMACULATE selectively audits a small fraction of requests using verifiable computation, achieving strong detection guarantees while amortizing cryptographic overhead. Experiments on dense and MoE models show that IMMACULATE reliably distinguishes benign and malicious executions with under 1% throughput overhead. Our code is published at https://github.com/guo-yanpei/Immaculate .

[5] h6: Keywords:

[6] h2: 1 Introduction

[7] p: Large language models (LLMs) have become a critical computational substrate across a wide range of applications, enabling high-quality text generation ( Brown et al., 2020 ; Chowdhery et al., 2023 ) , conversational agents ( Adamopoulou and Moussiades, 2020 ) , code synthesis ( Chen, 2021 ) , and reasoning-intensive workloads ( Wei et al., 2022 ) . Today, most frontier LLMs including OpenAI ( OpenAI, 2023 ) , Google ( Google Cloud, 2023 ) , and Anthropic ( Anthropic, 2023 ) are deployed through API-based inference services , where users interact with proprietary models via black-box endpoints and are charged based on reported token usage and model specifications.

[8] p: Despite its success, the black-box API model introduces a fundamental trust asymmetry . Users lack any visibility into the deployed model or its internal execution, making it hard for users to audit whether the providers faithfully executed the claimed inference procedure. From an economic perspective, providers may have incentives to silently deviate from the advertised protocol—for example, by substituting a distilled model or applying aggressive quantization to reduce computational cost. Indeed, anecdotal reports of quality degradation under unchanged model claims have appeared in public forums, highlighting an emerging accountability gap in LLM service provision ( webtailken, 2024 ; theevildays, 2024 ) .

[9] p: Compared to model substitution, token overbilling poses a more severe integrity threat ( Sun et al., 2025a ) . For reasoning-intensive workloads, API providers (e.g., OpenAI) hide intermediate chain-of-thought tokens while still billing for full internal token usage ( OpenAI, 2023 ) . As token usage is a dominant cost factor for downstream applications and autonomous agents ( Chen et al., 2023 ; Mohammadi et al., 2025 ) , the absence of verifiable billing guarantees undermines consumer trust. Unlike model substitution, token misreporting leaves no observable signal in the output, making detection impossible under standard black-box access.

[10] p: These challenges highlight the growing importance of auditing black-box LLM services . As LLM APIs become critical infrastructure for downstream applications and autonomous agents, users must be able to verify that providers execute inference honestly—without gaining access to proprietary models or internal states. However, auditing black-box LLM services is inherently difficult due to competing system requirements:

[11] p: Economy : the auditing mechanism should introduce minimal computational and monetary overhead for benign LLM service providers.

[12] p: Proprietorship : the LLM vendor’s model architecture, parameters, and internal inference states should remain confidential.

[13] p: Robustness : the framework should offer provable guarantees for detecting protocol deviations, without falsely flagging honest servers.

[14] p: A representative approach ( Cai et al., 2025 ) enforces runtime integrity using trusted execution environments (TEEs), particularly GPU-based TEEs ( NVIDIA, 2023 ) . While TEEs provide strong integrity guarantees with modest overhead ( ≈ 20 % \approx 20\% on NVIDIA H100 ( Tan et al., 2025 ) ), their economic viability is limited: GPU-TEE support is restricted to specific NVIDIA hardware, and large-scale adoption of GPU-TEEs would require costly redesign of existing inference infrastructure (e.g., Google TPUs ( Jouppi et al., 2017 ) , AWS Inferentia ( AWS, 2022 ) , Ascend GPUs ( Zhou et al., 2025 ) ).

[15] p: An alternative line of work relies on cryptographic proofs to attest correct inference execution ( Chen et al., 2024a ) . However, such approaches incur substantial prover overhead and are fundamentally limited to deterministic computations. Existing systems (e.g., zkLLM ( Sun et al., 2024 ) , zkGPT ( Qu et al., 2025 ) ) therefore restrict inference to integer-only arithmetic, which is inefficient on modern GPUs, rendering these approaches impractical for real-world LLM services ( Cai et al., 2025 ; Gao et al., 2024 ) .

[16] h4: Our approach.

[17] p: In this work, we present Immaculate , a practical auditing framework for black-box LLM services that following the line of proof-based approaches. Compared to prior proof-based schemes, Immaculate eliminates the need for integer-only inference and remains compatible with existing inference infrastructures, while incurring only minor proving overhead.

[18] p: The key insight behind cost-saving is economic: a rational service provider can only benefit from misbehavior by deviating from the claimed inference or billing protocol on a non-negligible fraction of requests. Therefore, instead of verifying every request, the server can be considered benign if it can successfully prove its execution on a small, random subset of requests. As a result, an auditor can detect large-scale deviations with overwhelming probability by issuing a small number of random queries that mimic normal user requests and requiring the server to prove their execution. Consequently, the relative overhead of proof generation is negligible compared to the cost of serving billions of inferences per day. This idea is visualized in Figure 1 .

[19] p: To address the inherent non-determinism of floating-point execution on modern accelerators, we introduce the logit distance distribution (LDD) as a quantitative indicator of approximation fidelity between a returned response and a claimed model. Rather than proving exact LLM execution—which is infeasible under numerical non-determinism—we require the server to prove the computation of the LDD. The resulting distribution serves as a verifiable audit footprint that captures systematic deviations from the claimed inference procedure while remaining stable under benign numerical noise. When aggregated over a large number of requests, LDDs induced by benign execution and malicious deviation become discriminative. This design enables sound verification of LLM execution without requiring bitwise reproducibility.

[20] figure: Figure 1 : The auditor sends random requests like other users and requires the model owner to prove the responses after they are received.

[21] p: By combining probabilistic auditing and proving LDD on audited requests, Immaculate provides economical, strong, provable guarantees for LLM service integrity. The contributions can be summarized as follows:

[22] p: We propose Immaculate , a practical auditing framework for black-box LLM services that provides strong integrity guarantees without relying on GPU-based trusted execution environments.

[23] p: We introduce the logit distance distribution (LDD), a fidelity metric that quantifies the approximation gap between a deployed execution and a claimed full-precision model, enabling verification under numerical non-determinism.

[24] p: We demonstrate that Immaculate is economical and compatible with existing large-scale LLM deployments. Our prototype implementation built on vLLM incurs only ∼ \sim 1% overhead. Our code is published at https://github.com/guo-yanpei/Immaculate .

[25] h2: 2 Preliminary and Related Work

[26] h4: Notation.

[27] p: For a function f ⁡ ( ⋅ ) f(\cdot) , the assignment y := f ⁡ ( x ) y:=f(x) denotes a deterministic map whose output is uniquely determined by its input. The assignment y ← g ⁡ ( x ) y\leftarrow g(x) denotes a non-deterministic map, typically reflecting hardware-dependent variability such as GPU parallelism. We use [ n ] [n] to denote set { 1 , 2 , ⋯ , n } \left\{1,2,\cdots,n\right\} .

[28] h3: 2.1 Cryptographic Commitment

[29] p: Cryptographic commitment schemes ( Merkle, 2019 ) allow a party to commit to a message and later reveal it, while guaranteeing binding and hiding. In practice, commitments can be instantiated using cryptographic hash functions, e.g., c = 𝖧𝖺𝗌𝗁 ( m | | r ) c=\mathsf{Hash}(m||r) .

[30] h3: 2.2 Verifiable Computation

[31] p: Verifiable computation (VC) ( Gennaro et al., 2013 ) enables a powerful prover to convince a lightweight verifier that a deterministic public function f ⁡ ( 𝐱 , 𝐰 ) = 𝐲 f(\mathbf{x},\mathbf{w})=\mathbf{y} was executed correctly, without revealing the private witness 𝐰 \mathbf{w} . Compared to re-execution, VC provides sublinear (often polylogarithmic) verification cost and witness privacy. Formally, VC consists of a prover–verifier pair ( 𝖯𝗋𝗈𝗏𝖾 , 𝖵𝗋𝖿𝗒 ) (\mathsf{Prove},\mathsf{Vrfy}) satisfying completeness, soundness, and zero-knowledge. VC can be instantiated via Trusted Execution Environments (TEEs) ( Sabt et al., 2015 ) or zero-knowledge proofs (ZKPs) ( Goldwasser et al., 2019 ) : TEEs offer near-native performance under hardware trust assumptions, while ZKPs provide stronger cryptographic guarantees at substantially higher cost.

[32] h3: 2.3 Related Works

[33] figure: Table 1 : The comparison between our work and prior works. Robustness Infra-agnostic Efficiency GPU TEE ✓ ✗ ✓ Cryptography ✓ ✓ ✗ Empirical ✗ ✓ ✓ Our Approach ✓ ✓ ✓

[34] p: Existing LLM auditing approaches can be broadly categorized into three paradigms: empirical methods, GPU-TEE–based verification, and cryptographic verification. Table 1 summarizes their trade-offs in terms of robustness, hardware requirements, and efficiency.

[35] p: GPU-TEE–based approaches provide strong robustness guarantees but rely on specialized infrastructure, which introduces considerable hardware procurement costs. Cryptographic approaches offer strong security guarantees without trusted hardware; however, they incur substantial proof-generation cost and are typically restricted to integer-only model executions, making them inefficient on modern AI-accelerated hardware.

[36] p: Empirical auditing methods, which operate without trusted hardware or cryptographic primitives, are computationally efficient and easily deployable. Nevertheless, they generally lack formal guarantees of completeness and soundness, and are typically vulnerable to adaptive attacks such as aggressive quantization ( Cai et al., 2025 ) or token overbilling ( Sun et al., 2025a ) .

[37] p: In contrast, our approach achieves a favorable balance across all three dimensions, combining robustness with hardware compatibility and practical efficiency. A more detailed discussion of existing auditing schemes is provided in Appendix A .

[38] h2: 3 Threat Model

[39] h4: System setting.

[40] p: Our auditing framework involves two parties: a cloud-based LLM inference server 𝖲𝗋𝗏 \mathsf{Srv} and a trusted auditor 𝖠𝖽𝗍 \mathsf{Adt} . The server claims to perform inference using a specified model ℳ θ \mathcal{M}_{\theta} with a certain precision. For each query x → \vec{x} , 𝖲𝗋𝗏 \mathsf{Srv} returns an output sequence y → \vec{y} along with a reported token count T T . The goal of 𝖠𝖽𝗍 \mathsf{Adt} is to act as a normal user by submitting random queries to 𝖲𝗋𝗏 \mathsf{Srv} and verifying whether 𝖲𝗋𝗏 \mathsf{Srv} processes the requests faithfully.

[41] h4: Threat model.

[42] p: We assume 𝖲𝗋𝗏 \mathsf{Srv} is rational and economically motivated, and may deviate from the claimed protocol to reduce computation cost or increase billing. We exclude attacks that increase computational cost and manage to serve users with an alternative model. A malicious server is assumed to misbehave on at least 10 % 10\% of queries. We assume 𝖠𝖽𝗍 \mathsf{Adt} always behaves honestly, and 𝖲𝗋𝗏 \mathsf{Srv} cannot distinguish the requests from 𝖠𝖽𝗍 \mathsf{Adt} and from normal user.

[43] h4: Auditing goal.

[44] p: An auditing scheme must distinguish between the following two types of servers:

[45] p: Honest execution: 𝖲𝗋𝗏 ​ ( x → ) = ℳ θ ​ ( x → ) \mathsf{Srv}(\vec{x})=\mathcal{M}_{\theta}(\vec{x}) for all x → \vec{x} .

[46] p: α \alpha -dishonest execution:

[47] table: Pr x → [ 𝖲𝗋𝗏 ( x → ) ≠ ℳ θ ( x → ) ] ≥ α . \Pr_{\vec{x}}[\mathsf{Srv}(\vec{x})\neq\mathcal{M}_{\theta}(\vec{x})]\geq\alpha.

[48] p: The auditing framework outputs ACCEPT or REJECT and satisfies:

[49] p: Completeness: An honest server is accepted with overwhelming probability.

[50] p: Soundness: An α \alpha -dishonest server is rejected with high probability.

[51] p: Efficiency: Auditing introduces only marginal overhead beyond standard inference.

[52] p: Privacy: The model’s parameters and architecture remain hidden from all parties except the model server.

[53] p: Generality: The scheme applies across various LLM architectures and hardware platforms.

[54] p: In our paper, following prior works ( Cai et al., 2025 ; Sun et al., 2025a ) , we consider the following integrity deviation attacks:

[55] p: Model substitution. The server replaces the claimed model with a lower-cost alternative.

[56] p: Aggressive quantization. The server executes the claimed model architecture but uses a lower-precision arithmetic format than advertised (e.g., FP8 instead of BF16).

[57] p: Token overreporting. The server executes all recurrent hybrid steps faithfully but manipulates the output reconstruction function D D to inflate the reported token count T T beyond actual usage.

[58] h2: 4 Logit Distance Distribution

[59] p: A central challenge in auditing LLM inference is the absence of a well-defined “ground truth” execution. Due to GPU-level non-determinism and numerical instability in finite-precision arithmetic, benign executions can even produce different outputs.

[60] p: Our key insight is that, for each LLM inference task, one can define an idealized and deterministic reference execution under full-precision arithmetic. Faithfulness can then be assessed by measuring the approximation fidelity between the observed execution and this ideal reference. Intuitively, if the discrepancy between claimed model and executed model arise solely from numerical error, their distance would exhibit a stable and predictable distribution. In contrast, malicious behaviors—such as model substitution or aggressive quantization—introduce structured deviations that generate significantly stronger and easily distinguishable error signals. We hence try to use such distance distribution to quantize the approximation fidelity.

[61] p: However, a central challenge lies in the fact that the discrete steps in LLMs can significantly amplify numerical errors. For example, since LLMs generate outputs auto-regressively, even a small numerical error that leads to a different token selection can cause the subsequent inference sequence to fully diverge from the reference. Therefore, a mechanism is needed to align the observed inference with the reference.

[62] p: In Section 4.1 , we introduce an abstraction of general LLMs, which serves as the foundation for our alignment technique. In Section 4.2 , we present the logit distance distribution (LDD) as a metric for quantifying approximation fidelity, which relies on our alignment technique.

[63] h3: 4.1 Hybrid Computation Model: LLM Abstraction

[64] p: Let 𝒳 ⊆ ℝ + \mathcal{X}\subseteq\mathbb{R}^{+} denote the continuous hidden-state space, 𝒟 \mathcal{D} a finite discrete decision set (e.g., vocabulary symbols or expert indices), θ \theta the model parameter space, and Γ \Gamma the token vocabulary. Given a prompt x → ∈ Γ + \vec{x}\in\Gamma^{+} , a large language model (LLM) autoregressively produces an output sequence y → ∈ Γ + \vec{y}\in\Gamma^{+} .

[65] h4: Hybrid computation model.

[66] p: We abstract LLM inference as a hybrid continuous–discrete process

[67] table: ℳ θ := ( E θ , F θ , S , G θ , D ) , \mathcal{M}_{\theta}:=(E_{\theta},F_{\theta},S,G_{\theta},D),

[68] p: which evolves through a sequence of transitions combining differentiable neural computation and discrete control-flow decisions. Concretely, inference proceeds as follows.

[69] p: Initial embedding. The input prompt x → \vec{x} is mapped into an initial continuous hidden state:

[70] table: h 0 ← E θ ​ ( x → ) , E θ : Γ + → 𝒳 . h_{0}\leftarrow E_{\theta}(\vec{x}),\qquad E_{\theta}:\Gamma^{+}\rightarrow\mathcal{X}.

[71] p: Recurrent hybrid step. For each generation step i = 1 , 2 , … i=1,2,\dots , the model executes:

[72] p: Continuous transformation. Differentiable neural operators (e.g., attention, MLPs, normalization) map the current state h i − 1 h_{i-1} to an intermediate state h ~ i \tilde{h}_{i} and a decision vector ℓ i \ell_{i} (e.g., logits):

[73] table: ( h ~ i , ℓ i ) ← F θ ​ ( h i − 1 ) , F θ : 𝒳 → 𝒳 × 𝒳 . (\tilde{h}_{i},\ell_{i})\leftarrow F_{\theta}(h_{i-1}),\qquad F_{\theta}:\mathcal{X}\rightarrow\mathcal{X}\times\mathcal{X}.

[74] p: Discrete decision. A discrete choice d i ∈ 𝒟 d_{i}\in\mathcal{D} (such as token sampling or MoE routing) is selected according to ℓ i \ell_{i} and a randomness source r i r_{i} :

[75] table: d i := S ⁡ ( ℓ i , r i ) , S : 𝒳 × ℛ → 𝒟 . d_{i}:=S(\ell_{i},r_{i}),\qquad S:\mathcal{X}\times\mathcal{R}\rightarrow\mathcal{D}.

[76] p: State update. The discrete decision is injected back into the continuous computation stream:

[77] table: h i ← G θ ​ ( h ~ i , d i ) , G θ : 𝒳 × 𝒟 → 𝒳 . h_{i}\leftarrow G_{\theta}(\tilde{h}_{i},d_{i}),\qquad G_{\theta}:\mathcal{X}\times\mathcal{D}\rightarrow\mathcal{X}.

[78] p: Output reconstruction. After N N recurrent steps, the output sequence and reported token count are reconstructed:

[79] table: ( y → , T ) := D ⁡ ( { d 1 , d 2 , … , d N } ) . (\vec{y},T):=D(\{d_{1},d_{2},\dots,d_{N}\}).

[80] p: The hybrid computation model distinguishes continuous transformations from discrete decisions in two key respects:

[81] p: Continuous transformations are subject to runtime non-determinism, whereas discrete decisions are fully determined by their inputs.

[82] p: Continuous outputs vary smoothly under small input perturbations, while discrete decisions can change abruptly in response to the same perturbations, leading to different control-flow paths.

[83] h4: Ideal and approximate execution.

[84] p: We define the full-precision model ℳ ⋆ \mathcal{M}^{\star} as the idealized execution of the above hybrid process where all continuous transformations are evaluated over the real numbers ℝ \mathbb{R} . In contrast, a deployed implementation ℳ \mathcal{M} operates using finite-precision arithmetic (e.g., FP16, BF16, FP8), yielding a numerical approximation of ℳ ⋆ \mathcal{M}^{\star} . A central goal is to quantify the fidelity of ℳ \mathcal{M} relative to ℳ ⋆ \mathcal{M}^{\star} .

[85] h4: Control-flow alignment.

[86] p: A crucial challenge in defining and measuring approximation fidelity is that ℳ \mathcal{M} and ℳ ⋆ \mathcal{M}^{\star} may follow completely different control flows due to tiny numerical differences. This situation can arise when the two models make different discrete decisions. One way to address this issue is to enforce ℳ ⋆ \mathcal{M}^{\star} to choose the same discrete decisions as ℳ \mathcal{M} at every step. This approach is visualized in Figure 2 .

[87] figure: Figure 2 : When fixing discrete selections d i {d_{i}} , the entire inference (green workflow) can be viewed as a continuous computation, as discrete selection no longer introduces branching uncertainty.

[88] h3: 4.2 Logit Distance Distribution

[89] p: However, this enforcement introduces a new issue. For each enforced decision d i d_{i} , we must evaluate the “proximity” between the logits ℓ i ⋆ \ell_{i}^{\star} and the decision d i d_{i} . If a decision is far inconsistent with the underlying state (i.e., the distance is too large), such enforcement should be flagged as misbehavior.

[90] p: Measuring the fidelity between logits ℓ i ⋆ \ell_{i}^{\star} and the discrete choice d i d_{i} is challenging, as it involves comparing two inherently different entities: continuous values and discrete outcomes. Instead, we compare the distance between the inputs to the discrete selection function, namely the logits ℓ i \ell_{i} and ℓ i ⋆ \ell_{i}^{\star} . Since the discrete selection function is deterministic, recording the logits is also sufficient to reproduce the decision d i d_{i} .

[91] p: Therefore, validating the proximity of a discrete selection can be transformed into checking distance between ℓ i \ell_{i} and ℓ i ⋆ \ell^{\star}_{i} . Any misbehavior tends to make ℓ i \ell_{i} and ℓ i ⋆ \ell^{\star}_{i} far. Hence, the approximation fidelity can be measured by logit distance distribution, formally defined below.

[92] h6: Definition 4.1 (Logit Distance Distribution) .

[93] p: Conditioned on an identical discrete decisions, let { ℓ i } \{\ell_{i}\} denote the logits produced by a deployed model execution, and let { ℓ i ⋆ } \{\ell_{i}^{\star}\} denote the corresponding logits produced by the full-precision model. The logit distance distribution (LDD) is defined as the distribution of { 𝖣𝗂𝗌 ⁡ ( ℓ i , ℓ i ⋆ ) } \{\mathsf{Dis}(\ell_{i},\ell_{i}^{\star})\} , where 𝖣𝗂𝗌 ⁡ ( ⋅ , ⋅ ) \mathsf{Dis}(\cdot,\cdot) denotes a distance metric between two logit vectors, like KL divergence or total variance (TV) distance.

[94] p: The following propositions characterizes the statistical signatures of three existing attacks studied in previous works ( Cai et al., 2025 ; Sun et al., 2025a ) :

[95] h6: Proposition 4.2 .

[96] p: Model substitution introduces a systematic bias in logit outputs. As a result, model substitution typically yields substantially larger LDDs.

[97] h6: Proposition 4.3 .

[98] p: Reducing numerical precision manifests as increased variance in logit deviations. Thus, precision reduction causes a progressive broadening of the LDD distribution.

[99] p: Both propositions are proved in Appendix C.1 .

[100] h6: Proposition 4.4 .

[101] p: Token overreporting is a special case of model substitution under the hybrid computation model.

[102] p: A proof sketch is token overreporting can be viewed as adding some dummy recurrent hybrid steps to the model. A complete proof is presented at Appendix C.2 .

[103] h2: 5 Immaculate: An Auditing Framework for LLM Execution

[104] p: In this section, we present Immaculate , a practical auditing framework for detecting α \alpha -dishonest execution of large language models (LLMs) by an untrusted service provider. At a high level, Immaculate adopts randomized auditing to reduce proving cost, and combines LDD with verifiable computation to solve intrinsic numerical non-determinism.

[105] h3: 5.1 Randomized Auditing

[106] p: Our key observation for significantly reducing the proving cost is that it is unnecessary to prove every query. Instead, the auditor can adopt randomized auditing by proving only a small random subset of queries. If a server deviates on an α \alpha -fraction of requests, such behavior can be detected with overwhelming probability from this subset. Importantly, the required number of audited queries depends only on α \alpha and the desired confidence level, rather than on the total service volume.

[107] h4: Example.

[108] p: Assume a method can detect malicious responses with zero false positive and only 1 % 1\% detection rate. If the server cheats on a fraction α = 0.1 \alpha=0.1 of requests, then achieving an overall detection probability of 95 % 95\% (i.e., evasion probability η = 5 % \eta=5\% ) requires only

[109] table: N = log ⁡ η log ⁡ ( 1 − α ⋅ 1 % ) ≈ 3,000 N=\frac{\log\eta}{\log(1-\alpha\cdot 1\%)}\;\approx\;3{,}000

[110] p: audited queries. Since a production LLM service may process billions of requests per day, the cost of proving only a few thousand queries is amortized to negligible overhead.

[111] h3: 5.2 Reproducibility via Discrete-State Commitments

[112] p: Exact reproduction of LLM execution is infeasible due to unavoidable numerical non-determinism. Instead of proving bitwise equivalence, Immaculate verifies that the execution remains within an admissible numerical deviation from a reference full-precision model, using the LDD metric.

[113] p: At initialization, the model owner publishes a cryptographic commitment to the claimed full-precision model ℳ θ ⋆ \mathcal{M}_{\theta^{\star}} . During inference, the server runs finite-precision model ℳ θ \mathcal{M}_{\theta} , recording and committing to { ℓ i } \{\ell_{i}\} at each discrete decision. Importantly, these committed logits enables reproducing every discrete selection result.

[114] p: For an audited query, server proves the LDD via VC, using the committed runtime logits { ℓ i } \left\{\ell_{i}\right\} . Concretely, the VC proof establishes that:

[115] p: discrete decisions are derived from the committed logits { ℓ i } \{\ell_{i}\} ;

[116] p: continuous transformations are computed using ℳ θ ⋆ \mathcal{M}_{\theta^{\star}} , obtaining { ℓ i ⋆ } \left\{\ell^{\star}_{i}\right\} ;

[117] p: the final output ( y → , T ) (\vec{y},T) is consistent with the discrete decisions;

[118] p: distribution of distance between { ℓ i } \{\ell_{i}\} and { ℓ i ⋆ } \left\{\ell^{\star}_{i}\right\} is output.

[119] h4: Optimization: Top- K K distance.

[120] p: As top- K K selection is the most common discrete selection method in LLMs, we design a specialized top- K K distance metric, allowing the server to cache and commit only the K K selected indices instead of the full logits vector. The detailed method is provided in Appendix D .

[121] figure: Figure 3 : Logit TV-distance distribution of LLaMA3-70B. Probabilities are displayed on a logarithmic y-axis to better capture the tail behavior.

[122] h3: 5.3 Utilizing LDD in Practice.

[123] p: A central goal of our scheme is to produce observable and verifiable auditing footprints—concrete statistical evidence that can be independently examined to assess service integrity. The LDD serves as such an auditing footprint. There are many possible ways to utilize LDD for integrity auditing. In this work, we present LDD as a clear metric to distinguish between benign and malicious responses, along with some simple yet effective approaches for leveraging LDD in practice.

[124] p: Empirically, we test LDD over thousands of requests, and present a representative result in Figure 4 . It aggregates benign executions and malicious executions over thousands of requests, and find they induce well-separated distance distributions. We can observe that a particularly discriminative statistic is the tail probability, e.g. Pr [ 𝖳𝖵 ( ℓ i , ℓ i ⋆ ) > 0.1 ] \Pr[\mathsf{TV}(\ell_{i},\ell^{\star}_{i})>0.1] .

[125] p: Based on this observation, we can detect malicious requests by evaluating the density of “tailing logits”. For a request involving T T discrete steps, we define

[126] table: p ⁡ ( t 1 ) := 1 T ​ | { i ∈ [ T ] : 𝖳𝖵 ⁡ ( ℓ i , ℓ i ⋆ ) > t 1 } | . p(t_{1}):=\frac{1}{T}\left|\left\{i\in[T]:\mathsf{TV}(\ell_{i},\ell^{\star}_{i})>t_{1}\right\}\right|.

[127] p: A response is flagged as malicious (e.g. computed vis FP8) if p ⁡ ( t 1 ) > t 2 p(t_{1})>t_{2} , where thresholds t 1 t_{1} and t 2 t_{2} are auditing parameters. The choosing strategy of t 1 t_{1} and t 2 t_{2} is provided in Append E .

[128] h3: 5.4 End-to-end System

[129] p: We now describe the end-to-end execution flow of Immaculate , showing how randomized auditing, logit commitments, and verifiable computation are integrated into a practical LLM inference service.

[130] h4: Setup: model commitment.

[131] p: At deployment time, the model provider commits to the claimed full-precision reference model ℳ θ ⋆ \mathcal{M}_{\theta^{\star}} by publishing a cryptographic hash commitment. This commitment binds the server to a specific reference model while preserving full model confidentiality.

[132] h4: Online inference and logging.

[133] p: For each incoming query x → \vec{x} , the server performs standard LLM inference. During execution, the server additionally records the logits { ℓ i } \{\ell_{i}\} at each discrete decision point (e.g., token selection or expert routing). Along with the response ( y → , T ) (\vec{y},T) , 𝖲𝗋𝗏 \mathsf{Srv} also returns a commitment to { ℓ i } \{\ell_{i}\} to the user.

[134] p: We estimate logging cost of commercial open-source LLMs Even the largest open-source models require caching only about 1 KB of data per token, so this logging and commitment step incurs negligible overhead. The cached messages can be deleted after a prescribed threshold if the user does not request auditing, and therefore this mechanism does not introduce significant storage costs.

[135] h4: Randomized auditing.

[136] p: 𝖠𝖽𝗍 \mathsf{Adt} submits random queries to 𝖲𝗋𝗏 \mathsf{Srv} while behaving indistinguishably from a normal user. After receiving responses, 𝖠𝖽𝗍 \mathsf{Adt} immediately reveals its auditor identity and requests an audit proof from 𝖲𝗋𝗏 \mathsf{Srv} . In response, 𝖲𝗋𝗏 \mathsf{Srv} invokes a verifiable computation (VC) procedure to compute and prove the corresponding LDD. These LDDs serve as observable auditing footprints, providing statistical evidence of server-side execution integrity.

[137] p: Formal pseudo-code description is given in Appendix B . In Appendix F , we also analyze a strategic attacks from 𝖲𝗋𝗏 \mathsf{Srv} , and present the best strategy for a cost-incentive server is honestly commit runtime logits of its deployed model.

[138] h2: 6 Experiments

[139] p: We evaluate Immaculate along two complementary dimensions: (1) its completeness and detection effectiveness, and (2) the system’s imposed overhead. Concretely, our experiments answer the following questions:

[140] p: Does the proposed logit distance distribution (LDD) meaningfully characterize approximation fidelity between a deployed execution and the claimed full-precision model?

[141] p: Can LDD reliably distinguish benign executions from malicious behaviors such as aggressive quantization and model substitution?

[142] p: What per-request detection probability and false positive rate can be achieved using LDD-based decision rules?

[143] p: When combined with randomized auditing, does Immaculate provide strong completeness and soundness guarantees against an α \alpha -dishonest server?

[144] p: What is the end-to-end performance overhead introduced by Immaculate for model providers?

[145] h3: 6.1 Experimental Setup

[146] h4: System implementation.

[147] p: We build our inference system atop vLLM ( Kwon et al., 2023 ) , a widely used high-performance LLM inference framework. Verifiable computation (VC) is implemented using HuggingFace Transformers ( Wolf et al., 2019 ) and executed in FP32 arithmetic within a TDX enclave, serving as the reference full-precision execution. For all experiments, we adopt Top-20 token sampling strategy.

[148] h4: Hardware.

[149] p: All experiments are conducted on NVIDIA RTX 6000 Pro GPUs with 96 GB of GPU memory. We perform inference using tensor parallelism with a degree of 2 across GPUs.

[150] h4: Datasets.

[151] p: We evaluate on GSM8K, TriviaQA, and WebQuestions, representing mathematical reasoning, factual QA, and open-domain QA, respectively. For scalability, we subsample 500 prompts per dataset, resulting in a total of 1,500 evaluation queries. An initial setup phase is conducted using the first 200 examples from each of GSM8K, TriviaQA, and WebQuestions. We randomly sample 200 prompts from each dataset to form an independent setup set for calibrating auditing thresholds; all remaining prompts are held out and used exclusively for evaluation.

[152] h4: Models.

[153] p: We evaluate both dense and mixture-of-experts (MoE) architectures, including dense models LLaMA3-70B, Qwen3-32B and MoE models Qwen3-30B-A3B, DeepSeek-V2-Lite.

[154] h4: Attacks.

[155] p: We evaluate Immaculate against model substitution and aggressive quantization. We omit token overreporting from separate empirical evaluation because we have proved in Section 4.1 , it can be reduced to a special case of model substitution.

[156] p: For model substitution attacks, we evaluates 1) Substitute LLaMA3-70B with LLaMA3-8B; 2) Substitute Qwen3-32B with Qwen3-14B. We do not explore model substitution attacks for MoE models because larger versions are too costly to run. For quantization attacks, we assume all benign deployments are under BF16, and consider FP8 as quantization attacks, following the setting in ( Cai et al., 2025 ) .

[157] h3: 6.2 Global Logit Discrepancy Distribution

[158] p: We first evaluate whether the global LDD reflects approximation fidelity under different deployment regimes. Specifically, we compare three settings against the same full-precision reference model: 1) benign BF16 execution; 2) FP8 quantized execution; 3) model substitution (for dense models only).

[159] figure: Table 2 : Proportion of TV distance larger than certain threshold Model Deploy > 0.1 >0.1 > 0.2 >0.2 > 0.3 >0.3 LLaMA3 BF16 0.017 % 0.017\% 1.7 × 10 − 5 1.7\times 10^{-5} 1.9 × 10 − 6 1.9\times 10^{-6} FP8 1.7 % 1.7\% 0.23 % 0.23\% 0.054 % 0.054\% Sub. 11 % 11\% 8.2 % 8.2\% 6.2 % 6.2\% Qwen3 BF16 0.17 % 0.17\% 0.025 % 0.025\% 6.0 × 10 − 5 6.0\times 10^{-5} FP8 4.8 % 4.8\% 1.1 % 1.1\% 0.42 % 0.42\% Sub. 28 % 28\% 20 % 20\% 15 % 15\% Qwen3MoE BF16 0.074 % 0.074\% 2.6 × 10 − 5 2.6\times 10^{-5} 4.7 × 10 − 6 4.7\times 10^{-6} FP8 5.5 % 5.5\% 1.0 % 1.0\% 0.23 % 0.23\% Deepseek BF16 6.6 × 10 − 5 6.6\times 10^{-5} 6.0 × 10 − 6 6.0\times 10^{-6} 8.5 × 10 − 7 8.5\times 10^{-7} FP8 1.6 % 1.6\% 0.19 % 0.19\% 0.053 % 0.053\%

[160] p: Figure 4 has visualized the aggregated logit TV-distance distributions across all evaluated prompts. Across all evaluated dense and MoE models, benign BF16 execution induces sharply concentrated distributions with rapidly decaying tails. In contrast, FP8 quantization substantially increases the tail mass at moderate and large logit distances, while model substitution causes a pronounced right-shift, yielding orders-of-magnitude higher probability mass in the extreme tail.

[161] p: To quantify the separation, we further report in Table 2 the probability that the total-variation (TV) distance between deployed and reference logits exceeds different thresholds. It shows that FP8 quantization increases these tail probabilities by several orders of magnitude, while model substitution amplifies them further. These results confirm that tail events in the LDD provide a highly discriminative signal for distinguishing benign execution from economically motivated deviations, motivating the threshold-based detection rule used in subsequent experiments.

[162] p: In Appendix G , we also present global LDDs beyond TV distances. All results show distinct tail-probability across different deployments.

[163] h3: 6.3 Per-request Decision Based on LDD

[164] figure: Table 3 : Malicious request detection rate (the rate of malicious requests that can be detected under FP = 10 − 5 \mathrm{FP}=10^{-5} ). As shown in Section 5.1 , 1% per-request detection probability is sufficient for effective randomized auditing. Model Deploy GSM8K TriviaQA WebQuestions LLaMA3 FP8 9.0 % 9.0\% 9.7 % 9.7\% 5.3 % 5.3\% Sub. 42 % 42\% 95 % 95\% 99 % 99\% Qwen3 FP8 1.3 % 1.3\% 3.6 % 3.6\% 2.0 % 2.0\% Sub. 96 % 96\% 96 % 96\% 97 % 97\% Qwen3MoE FP8 2.0 % 2.0\% 2.1 % 2.1\% 5.0 % 5.0\% Deepseek FP8 10.3 % 10.3\% 3.0 % 3.0\% 3.7 % 3.7\%

[165] p: While global LDDs exhibit clear separation, auditing decisions must ultimately be made at the per-request level. In practice, a malicious LLM provider may apply heterogeneous deployment strategies across requests, thereby blurring the global distribution and reducing its discriminative power.

[166] p: Following Section 5.3 , we define a per-request statistic p ⁡ ( t 1 ) p(t_{1}) based on the fraction of logit distance exceeding a threshold t 1 t_{1} . The request is flagged as malicious if p ⁡ ( t 1 ) > t 2 p(t_{1})>t_{2} . The auditing parameters t 1 , t 2 t_{1},t_{2} is computed via method given in Section 5.3 .

[167] p: Table 3 present the resulting detection rates. For quantization attacks, a request is detected with probability at least 1.3 % 1.3\% , whereas model substitution is detected with probability larger than 40 % 40\% .

[168] p: Accurately estimating the per-request false positive rate under benign execution is challenging due to the extreme rarity of tail events. Owing to computational constraints, our experiments evaluate only on thousands of requests; consequently, all benign requests observed in practice are correctly classified, making direct empirical estimation of the false positive rate infeasible.

[169] p: To address this limitation, we adopt an extreme value theory (EVT)–based approach to model the tail behavior of benign LDDs. Specifically, we fit an EVT model to the extreme tail of the benign distribution p ⁡ ( t 1 ) p(t_{1}) and estimate the probability that a benign request produces an LDD exceeding t 2 t_{2} . Results show that among all datasets and models, the false positive rate is smaller than 10 − 5 10^{-5} .

[170] h4: Completeness and soundness.

[171] p: Assume Immaculate audits approximately 3,000 requests per day. To achieve overwhelming completeness, among 3,000 requests, 𝖠𝖽𝗍 \mathsf{Adt} allows at most 3 of them classified to be malicious. Consider the at most 10 − 5 10^{-5} per-request false positive rate, the probability of rejecting a benign server is

[172] table: 1 − ∑ k = 0 3 ( 3000 k ) ​ ( 10 − 5 ) k ​ ( 1 − 10 − 5 ) 3000 − k ≤ 10 − 7 , 1-\sum_{k=0}^{3}\binom{3000}{k}(10^{-5})^{k}(1-10^{-5})^{3000-k}\leq 10^{-7},

[173] p: representing overwhelming completeness.

[174] p: For an α = 0.1 \alpha=0.1 dishonest server, each audited request is detected with probability at least 10 − 3 10^{-3} . The probability of observing 4 or more detections in a day is therefore

[175] table: 1 − ∑ k = 0 3 ( 3000 k ) ​ ( 10 − 3 ) k ​ ( 1 − 10 − 3 ) 3000 − k ≥ 0.3 . 1-\sum_{k=0}^{3}\binom{3000}{k}(10^{-3})^{k}(1-10^{-3})^{3000-k}\geq 0.3.

[176] p: Over a month-long horizon, the probability of persistent evasion becomes negligible.

[177] h3: 6.4 Auditing Parameter Study

[178] figure: Table 4 : Detection rate and false positive rate under different hyperparameter Hyper. LLaMA3 Qwen3 Qwen3MoE Deepseek 0.02 Detect 2.1 % 2.1\% 0.44 % 0.44\% 0.93 % 0.93\% 1.3 % 1.3\% FP 2 × 10 − 9 2\times 10^{-9} 2 × 10 − 8 2\times 10^{-8} 5 × 10 − 10 5\times 10^{-10} 8 × 10 − 10 8\times 10^{-10} 0.03 Detect 6.2 % 6.2\% 0.67 % 0.67\% 2.1 % 2.1\% 3.0 % 3.0\% FP 1 × 10 − 8 1\times 10^{-8} 3 × 10 − 7 3\times 10^{-7} 1 × 10 − 8 1\times 10^{-8} 2 × 10 − 8 2\times 10^{-8} 0.04 Detect 6.2 % 6.2\% 1.2 % 1.2\% 2.1 % 2.1\% 3.0 % 3.0\% FP 1 × 10 − 8 1\times 10^{-8} 1 × 10 − 6 1\times 10^{-6} 1 × 10 − 8 1\times 10^{-8} 2 × 10 − 8 2\times 10^{-8} 0.05 Detect 6.2 % 6.2\% 2.3 % 2.3\% 3.6 % 3.6\% 5.6 % 5.6\% FP 1 × 10 − 8 1\times 10^{-8} 4 × 10 − 6 4\times 10^{-6} 9 × 10 − 7 9\times 10^{-7} 8 × 10 − 8 8\times 10^{-8} 0.06 Detect 9.4 % 9.4\% 3.3 % 3.3\% 3.6 % 3.6\% 8.8 % 8.8\% FP 4 × 10 − 7 4\times 10^{-7} 2 × 10 − 5 2\times 10^{-5} 9 × 10 − 7 9\times 10^{-7} 5 × 10 − 7 5\times 10^{-7} 0.07 Detect 9.4 % 9.4\% 5.1 % 5.1\% 5.2 % 5.2\% 8.8 % 8.8\% FP 4 × 10 − 7 4\times 10^{-7} 6 × 10 − 5 6\times 10^{-5} 4 × 10 − 6 4\times 10^{-6} 5 × 10 − 7 5\times 10^{-7}

[179] p: The derivation of the auditing parameters is largely heuristic, so we explore a wider range of parameter choices to demonstrate the robustness of our scheme. When computing t 1 t_{1} and t 2 t_{2} via the ceremony, we employ an ad-hoc hyperparameter that accepts only ( t 1 , t 2 ) (t_{1},t_{2}) pairs achieving a 5% detection rate on the ceremony dataset. Here, we vary this hyperparameter around the 5% threshold to derive different auditing parameters t 1 t_{1} and t 2 t_{2} , and report their corresponding false positive rates and detection rates in Table 3 . Due to space constraints, we aggregate the results from three datasets to present the overall false positive rate and detection rate. Results show that for all derived auditing parameters, the FP rate and detection rate are always acceptable.

[180] h3: 6.5 Overhead to Benign Execution

[181] p: We finally evaluate the efficiency impact of Immaculate . Since verifiable computation is triggered only on a small audited subset, the dominant overhead arises from storing and committing lightweight runtime values.

[182] p: Across all evaluated models, the end-to-end throughput overhead for a benign server is below 1 % 1\% , demonstrating practical deployability. The VC deployed in CPU TEE is hundreds of times slower than inference. Consider that the proportion of audited request is smaller than 10 − 5 10^{-5} , the overall cost is negligible.

[183] figure: Table 5 : Overhead Evaluation. ‘Thp.’ denotes the inference throughput loss. ‘Request VC’ denotes the runtime of VC on CPU-TEE compared with GPU inference Thp. Request VC LLaMA3-70B 0.3 % 0.3\% 400 × 400\times Qwen3-32B 0.3 % 0.3\% 400 × 400\times Qwen3-30B-A3B 0.9 % 0.9\% 900 × 900\times DeepSeek-V2-Lite 1.0 % 1.0\% 800 × 800\times

[184] h2: 7 Conclusion

[185] p: We have introduced Immaculate , a practical and robust auditing framework for LLM inference services that operate as black-box APIs. By combining selective verifiable computation with a novel Logit Distance Distribution (LDD) metric, Immaculate enables auditors to detect economically motivated deviations—such as model substitution, aggressive quantization, and token overreporting—without requiring access to model internals or relying on trusted hardware.

[186] p: Looking ahead, we believe that Immaculate lays the foundation for a new class of auditing frameworks. Future work may explore additional optimizations, particularly in leveraging LDD to more effectively identify malicious requests. Ultimately, our framework represents a step toward greater transparency, accountability, and trust in commercial LLM services.

[187] h2: References

[188] h2: Appendix A Extended Related Work

[189] p: Existing LLM auditing frameworks struggle to simultaneously achieve economy , proprietorship , and robustness . Section 2.3 discusses the limitations of cryptography-based approaches and GPU TEEs in terms of deployment cost and infrastructure requirements. In this section, we review additional auditing paradigms and analyze their limitations under the black-box service setting.

[190] h4: Direct Verification.

[191] p: When the model is fully public, auditing becomes straightforward. The most direct approach is to re-execute inference and compare the outputs with those returned by the service. TopLoc ( Ong et al., 2025 ) accelerates verification by transforming decoding operations into prefilling, reducing the computational overhead of re-execution. Yao et al. ( Yao et al., 2025 ) propose verifying only a subset of randomly selected layers and integrate the auditing process with a blockchain-based logging mechanism. However, these methods require the auditor to access model weights and execution details, making them unsuitable for proprietary commercial models.

[192] h4: Detecting LLM-generated text.

[193] p: Another line of work attempts to audit black-box services by analyzing their output behavior. Prior studies track performance drift and behavioral changes over time ( Chen et al., 2024b ; Eyuboglu et al., 2024 ) . Other methods aim to identify the deployed model by examining output distributions, including classifier-based fingerprinting ( Sun et al., 2025b ) , statistical discrepancy tests ( Gao et al., 2024 ; Zhu et al., 2025 ) , and identity-style prompting ( Huang et al., 2025 ) . However, these approaches typically require large query budgets and are vulnerable to randomized model substitution or decoding variability. Moreover, since they rely solely on observable text outputs, they cannot detect attacks such as token overreporting, which do not affect the returned content.

[194] h4: Token Overreport Detection.

[195] p: CoIn ( Sun et al., 2025a ) addresses the token overreporting issue by committing embeddings of hidden reasoning tokens in a Merkle hash tree for quantity verification, and by performing embedding-based relevance checks to detect low-effort or fabricated content. Nevertheless, a provider may still generate hidden tokens using a cheaper or simplified model while preserving semantic consistency, allowing the inflated sequence to pass such semantic validation. Complementary work by Velasco et al. ( Velasco et al., 2025 ) analyzes the problem from an economic perspective, showing that the pay-per-token pricing mechanism inherently incentivizes overreporting under information asymmetry. They argue that, since provider revenue scales with reported token length while users cannot observe the internal generation process, strategic tokenization or count manipulation becomes financially attractive, and propose pay-per-character pricing as an incentive-compatible alternative. However, such pricing changes do not provide technical guarantees on faithful execution.

[196] h4: Summary.

[197] p: Existing approaches each address only part of the auditing challenge. Direct re-execution methods provide strong guarantees but require full model access, violating proprietorship. Output-based statistical methods are economical but lack robustness against adaptive or invisible deviations. Economic or billing-based solutions address incentive misalignment but do not verify execution correctness. In contrast, Immaculate aims to achieve a balanced design that simultaneously ensures economy, preserves model confidentiality, and provides provable detection guarantees for execution deviations under black-box access.

[198] h2: Appendix B Algorithms

[199] p: The pseudo-code is presented at Algorithm 1 , Algorithm 2 and Algorithm 3 .

[200] figure: Algorithm 1 𝖲𝗋𝗏 \mathsf{Srv} : LLM Server’s algorithm 0: LLM model ℳ θ := ( E θ , F θ , S , G θ , D ) \mathcal{M}_{\theta}:=(E_{\theta},F_{\theta},S,G_{\theta},D) 1: ψ M := 𝖧𝖺𝗌𝗁 ⁡ ( ℳ θ ⋆ ) \psi_{M}:=\mathsf{Hash}(\mathcal{M}_{\theta^{\star}}) , where ℳ θ ⋆ \mathcal{M}_{\theta^{\star}} is the full-precision version of ℳ θ \mathcal{M}_{\theta} . 2: Publish ψ M \psi_{M} 3: upon receiving ⟨ 𝖱𝖾𝗊𝗎𝖾𝗌𝗍 , x → ⟩ \left\langle\mathsf{Request},\vec{x}\right\rangle from 𝖴𝗌𝗋 \mathsf{Usr} do 4: r ← $ { 0 , 1 } λ r\leftarrow_{\$}\left\{0,1\right\}^{\lambda} 5: h 0 ← E θ ​ ( x → ) h_{0}\leftarrow E_{\theta}(\vec{x}) . 6: for i = 1 , 2 , ⋯ , N i=1,2,\cdots,N do 7: h ~ i , ℓ i ← F θ ​ ( h i − 1 ) \tilde{h}_{i},\ell_{i}\leftarrow F_{\theta}(h_{i-1}) 8: d i := S ⁡ ( ℓ i , r ) d_{i}:=S(\ell_{i},r) 9: h i ← G θ ​ ( h ~ i , d i ) h_{i}\leftarrow G_{\theta}(\tilde{h}_{i},d_{i}) 10: end for 11: y → , T := D ⁡ ( { d 1 , ⋯ , d N } ) \vec{y},T:=D(\left\{d_{1},\cdots,d_{N}\right\}) 12: ψ := 𝖧𝖺𝗌𝗁 ⁡ ( r , { ℓ 1 , ⋯ , ℓ N } ) \psi:=\mathsf{Hash}(r,\left\{\ell_{1},\cdots,\ell_{N}\right\}) 13: send ⟨ 𝖱𝖾𝗌𝗉𝗈𝗇𝗌𝖾 , y → , T , ψ ⟩ \left\langle\mathsf{Response},\vec{y},T,\psi\right\rangle to 𝖴𝗌𝗋 \mathsf{Usr} . 14: upon receiving ⟨ 𝖠𝗎𝖽𝗂𝗍 ⟩ \left\langle\mathsf{Audit}\right\rangle from 𝖠𝖽𝗍 \mathsf{Adt} do 15: w := ( ℳ θ ⋆ , r , { ℓ 1 , ⋯ , ℓ N } ) w:=\left(\mathcal{M}_{\theta^{\star}},r,\left\{\ell_{1},\cdots,\ell_{N}\right\}\right) 16: ϕ , π := 𝖵𝖢 . 𝗉𝗋𝗈𝗏𝖾 ⁡ ( ( ψ M , ψ , x → , y → , T ) , w ) \phi,\pi:=\mathsf{VC}.\mathsf{prove}\left((\psi_{M},\psi,\vec{x},\vec{y},T);w\right) 17: send ⟨ 𝖯𝗋𝗈𝗈𝖿 , ϕ , π ⟩ \left\langle\mathsf{Proof},\phi,\pi\right\rangle to 𝖠𝖽𝗍 \mathsf{Adt} . 18: end upon 19: end upon

[201] figure: Algorithm 2 𝖠𝖽𝗍 \mathsf{Adt} : LLM Auditor’s algorithm 0: Auditing parameter 𝖺𝗉 \mathsf{ap} 0: b ∈ { 0 , 1 , ⊥ } b\in\left\{0,1,\bot\right\} 1: Generate random prompt x → \vec{x} 2: send ⟨ 𝖱𝖾𝗊𝗎𝖾𝗌𝗍 , x → ⟩ \left\langle\mathsf{Request},\vec{x}\right\rangle to 𝖲𝗋𝗏 \mathsf{Srv} 3: upon receiving ⟨ 𝖱𝖾𝗌𝗉𝗈𝗇𝗌𝖾 , y → , T , ψ ⟩ \left\langle\mathsf{Response},\vec{y},T,\psi\right\rangle do 4: send ⟨ 𝖠𝗎𝖽𝗂𝗍 ⟩ \left\langle\mathsf{Audit}\right\rangle to 𝖲𝗋𝗏 \mathsf{Srv} . 5: end upon 6: upon receiving ⟨ 𝖯𝗋𝗈𝗈𝖿 , ϕ , π ⟩ \left\langle\mathsf{Proof},\phi,\pi\right\rangle do 7: if 𝖵𝖢 . 𝗉𝗋𝗈𝗏𝖾 ⁡ ( ( ψ M , ψ , x → , y → , T ) , π ) \mathsf{VC}.\mathsf{prove}\left((\psi_{M},\psi,\vec{x},\vec{y},T),\pi\right) then 8: Return ⊥ \bot . 9: end if 10: Return 0/1 based on ϕ \phi and 𝖺𝗉 \mathsf{ap} . 11: end upon

[202] figure: Algorithm 3 𝖵𝖢 \mathsf{VC} : Verifiable computation function 0: Public input: model commitment ψ M \psi_{M} , logits commitment ψ \psi , prompt x → \vec{x} , response y → \vec{y} , token usage T T ; Private input: model ℳ θ ⋆ = ( E θ ⋆ , F θ ⋆ , S , G θ ⋆ , D ) \mathcal{M}_{\theta^{\star}}=(E_{\theta^{\star}},F_{\theta^{\star}},S,G_{\theta^{\star}},D) , seed r r , logits { ℓ 1 , ⋯ , ℓ N } \left\{\ell_{1},\cdots,\ell_{N}\right\} . 0: Logits distance distribution 1: if ψ ≠ 𝖧𝖺𝗌𝗁 ⁡ ( r , { ℓ 1 , ⋯ , ℓ N } ) \psi\neq\mathsf{Hash}\left(r,\left\{\ell_{1},\cdots,\ell_{N}\right\}\right) or ψ M ≠ 𝖧𝖺𝗌𝗁 ⁡ ( ℳ θ ⋆ ) \mathsf{\psi}_{M}\neq\mathsf{Hash}(\mathcal{M}_{\theta^{\star}}) then 2: abort 3: end if 4: h 0 ⋆ ← E θ ⋆ ​ ( x → ) h^{\star}_{0}\leftarrow E_{\theta^{\star}}(\vec{x}) . 5: for i = 1 , 2 , ⋯ , N i=1,2,\cdots,N do 6: h ~ i ⋆ , ℓ i ⋆ ← F θ ⋆ ​ ( h i − 1 ⋆ ) \tilde{h}^{\star}_{i},\ell^{\star}_{i}\leftarrow F_{\theta^{\star}}(h^{\star}_{i-1}) 7: δ i = 𝖣𝗂𝗌 ⁡ ( ℓ i , ℓ i ⋆ ) \delta_{i}=\mathsf{Dis}(\ell_{i},\ell^{\star}_{i}) 8: d i := S ⁡ ( ℓ i , r ) d_{i}:=S(\ell_{i},r) 9: h i ⋆ ← G θ ⋆ ​ ( h ~ i ⋆ , d i ) h^{\star}_{i}\leftarrow G_{\theta^{\star}}(\tilde{h}^{\star}_{i},d_{i}) 10: end for 11: if y → , T ≠ D ⁡ ( { d 1 , ⋯ , d N } ) \vec{y},T\neq D(\left\{d_{1},\cdots,d_{N}\right\}) then 12: abort 13: end if 14: return distribution of { δ 1 , ⋯ , δ N } \left\{\delta_{1},\cdots,\delta_{N}\right\}

[203] h2: Appendix C Proof of Propositions

[204] h3: C.1 Proposition 4.2 and Proposition 4.3

[205] h6: Proof.

[206] p: Fix a prompt x → \vec{x} and a sequence of discrete decisions d → = ( d 1 , … , d N ) \vec{d}=(d_{1},\dots,d_{N}) , thereby aligning the control flow of two executions. Let ℓ i ⋆ ​ ( θ ) \ell_{i}^{\star}(\theta) denote the deterministic logits produced by the full-precision model at step i i .

[207] p: For an approximate execution ℳ ( A ) \mathcal{M}^{(A)} , the observed logits can be written as

[208] table: ℓ i ( A ) = ℓ i ⋆ ​ ( θ ( A ) ) + η i ( A ) , \ell_{i}^{(A)}=\ell_{i}^{\star}(\theta^{(A)})+\eta_{i}^{(A)},

[209] p: where η i ( A ) \eta_{i}^{(A)} captures run-dependent numerical error due to finite precision or kernel non-determinism. Comparing ℳ ( A ) \mathcal{M}^{(A)} with the ideal model ℳ ( B ) = ℳ ⋆ \mathcal{M}^{(B)}=\mathcal{M}^{\star} yields

[210] table: ℓ i ( A ) − ℓ i ( B ) = ( ℓ i ⋆ ​ ( θ ( A ) ) − ℓ i ⋆ ​ ( θ ( B ) ) ) ⏟ Δ i model + η i ( A ) ⏟ Δ i prec , \ell_{i}^{(A)}-\ell_{i}^{(B)}=\underbrace{\big(\ell_{i}^{\star}(\theta^{(A)})-\ell_{i}^{\star}(\theta^{(B)})\big)}_{\Delta_{i}^{\mathrm{model}}}+\underbrace{\eta_{i}^{(A)}}_{\Delta_{i}^{\mathrm{prec}}},

[211] p: where η i ( B ) = 0 \eta_{i}^{(B)}=0 by definition.

[212] p: Model substitution. If θ ( A ) ≠ θ ( B ) \theta^{(A)}\neq\theta^{(B)} , then Δ i model ≠ 0 \Delta_{i}^{\mathrm{model}}\neq 0 , producing a systematic (biased) deviation in logits.

[213] p: Precision reduction. If θ ( A ) = θ ( B ) \theta^{(A)}=\theta^{(B)} , then Δ i model = 0 \Delta_{i}^{\mathrm{model}}=0 and discrepancies arise solely from numerical noise. Lower-precision formats induce higher variance:

[214] table: Var ⁡ ( η i FP8 ) > Var ⁡ ( η i FP16 ) , \mathrm{Var}(\eta_{i}^{\mathrm{FP8}})>\mathrm{Var}(\eta_{i}^{\mathrm{FP16}}),

[215] p: resulting in stochastic, zero-mean deviations rather than persistent bias. ∎

[216] h3: C.2 Proposition 4.4

[217] h6: Proof.

[218] p: Let the claimed model be

[219] table: ℳ := ( E θ , F θ , S , G θ , D ) , \mathcal{M}:=(E_{\theta},F_{\theta},S,G_{\theta},D),

[220] p: and consider a fixed prompt x → \vec{x} with discrete decision sequence d → = ( d 1 , … , d N ) \vec{d}=(d_{1},\dots,d_{N}) generated by ℳ \mathcal{M} . The corresponding output is

[221] table: ( y → , T ) = D ⁡ ( d → ) , T = N . (\vec{y},T)=D(\vec{d}),\qquad T=N.

[222] p: We construct an alternative model

[223] table: ℳ ′ := ( E θ , F θ ′ , S , G θ ′ , D ′ ) , \mathcal{M}^{\prime}:=(E_{\theta},F^{\prime}_{\theta},S,G^{\prime}_{\theta},D^{\prime}),

[224] p: which differs from ℳ \mathcal{M} only in the recurrent hybrid step and output reconstruction. Define K > 0 K>0 and extend the discrete decision sequence as

[225] table: d → ′ := ( d 1 , … , d N , d ¯ , … , d ¯ ⏟ K ) , \vec{d}^{\prime}:=(d_{1},\dots,d_{N},\underbrace{\bar{d},\dots,\bar{d}}_{K}),

[226] p: where d ¯ ∈ 𝒟 \bar{d}\in\mathcal{D} is a fixed dummy decision.

[227] p: Define the modified state update such that

[228] table: G θ ′ ​ ( h ~ , d ¯ ) = h and F θ ′ ​ ( h ) = ( h , ℓ ) , G^{\prime}_{\theta}(\tilde{h},\bar{d})=h\quad\text{and}\quad F^{\prime}_{\theta}(h)=(h,\ell),

[229] p: i.e., the dummy steps leave the hidden state invariant and do not affect subsequent decisions. Finally, define the reconstruction function

[230] table: D ′ ​ ( d → ′ ) := ( y → , N + K ) , D^{\prime}(\vec{d}^{\prime}):=(\vec{y},N+K),

[231] p: where y → \vec{y} is recovered solely from the prefix ( d 1 , … , d N ) (d_{1},\dots,d_{N}) .

[232] p: By construction,

[233] table: ℳ ′ ​ ( x → ) = ( y → , T + K ) , ℳ ⁡ ( x → ) = ( y → , T ) , \mathcal{M}^{\prime}(\vec{x})=(\vec{y},T+K),\qquad\mathcal{M}(\vec{x})=(\vec{y},T),

[234] p: while the observable output sequence y → \vec{y} is identical. Hence, token overreporting corresponds to replacing ℳ \mathcal{M} with a functionally distinct model ℳ ′ \mathcal{M}^{\prime} that modifies the hybrid transition structure.

[235] p: Since ℳ ′ ≠ ℳ \mathcal{M}^{\prime}\neq\mathcal{M} but preserves output semantics while altering reported resource usage, token overreporting is equivalent to a form of model substitution, and therefore constitutes a special case of model downsizing. ∎

[236] h2: Appendix D Optimization: Verification of Top- K K .

[237] p: Among all discrete operations in LLM inference, top- K K selection is the most dominant, appearing in both token sampling and mixture-of-experts routing. Formally, top- K K is a deterministic operator

[238] table: 𝖳𝗈𝗉 K : ℝ n → [ n ] K , \mathsf{Top}_{K}:\mathbb{R}^{n}\rightarrow[n]^{K},

[239] p: which returns the indices of the K K largest entries in a logits vector. In practice, n n is typically much larger than K K . For example, in token sampling, n n corresponds to the size of the entire vocabulary, often exceeding 10 5 10^{5} , while K K is typically around 20.

[240] p: Due to the large discrepancy between n n and K K , storing and committing to the full logits vector can be prohibitively expensive. Instead, Immaculate allows the LLM to store only the runtime top- K K indices rather than the entire logits vector, by introducing a minimal-perturbation distance criterion.

[241] h4: Top- K K distance.

[242] p: Given logits ℓ ∈ ℝ n \ell\in\mathbb{R}^{n} and a claimed index set I ⊆ [ n ] I\subseteq[n] with | I | = K |I|=K , we define

[243] table: Δ TopK ( ℓ , I ) := min ℓ ′ : 𝖳𝗈𝗉 K ​ ( ℓ ′ ) = I ∥ ℓ ′ − ℓ ∥ 1 . \Delta_{\mathrm{TopK}}(\ell,I):=\min_{\ell^{\prime}:\mathsf{Top}_{K}(\ell^{\prime})=I}\|\ell^{\prime}-\ell\|_{1}.

[244] p: By construction, Δ TopK ​ ( ℓ , I ) = 0 \Delta_{\mathrm{TopK}}(\ell,I)=0 if and only if I I is a valid top- K K set. Otherwise, it quantifies the minimal numerical perturbation required to make I I the exact top- K K . The defined distance is 1 1 -Lipschitz with respect to ℓ \ell , ensuring robustness to small numerical noise.

[245] h4: Efficient computation

[246] p: For each given logit vector ℓ \ell and index set I I , Δ TopK ​ ( ℓ , I ) \Delta_{\mathrm{TopK}}(\ell,I) can be evaluated efficiently. Since I I denotes the indices of the largest K K entries in the logits vector, there must exist a scalar threshold t ∈ ℝ t\in\mathbb{R} such that

[247] table: ℓ i ′ ≥ t ∀ i ∈ I , ℓ j ′ ≤ t ∀ j ∉ I . \ell^{\prime}_{i}\geq t\quad\forall i\in I,\qquad\ell^{\prime}_{j}\leq t\quad\forall j\notin I.

[248] p: Using a greedy algorithm, for a fixed threshold t t , the optimal perturbed logits ℓ ′ \ell^{\prime} satisfy

[249] table: ℓ i ′ = max ⁡ ( ℓ i , t ) ∀ i ∈ I , ℓ j ′ = min ⁡ ( ℓ j , t ) ∀ j ∉ I . \ell^{\prime}_{i}=\max(\ell_{i},t)\quad\forall i\in I,\quad\ell^{\prime}_{j}=\min(\ell_{j},t)\quad\forall j\notin I.

[250] p: Intuitively, entries in I I are minimally raised to t t , while entries outside I I are minimally lowered.

[251] p: Assume the logits are sorted as ℓ 1 ≥ ℓ 2 ≥ ⋯ ≥ ℓ n \ell_{1}\geq\ell_{2}\geq\cdots\geq\ell_{n} , and let t t lie in the interval ℓ u ≥ t ≥ ℓ u + 1 \ell_{u}\geq t\geq\ell_{u+1} . The resulting distance is given by

[252] table: ∑ i ≤ u , i ∉ I ( ℓ i − t ) + ∑ i ≥ u + 1 , i ∈ I ( t − ℓ i ) . \sum_{i\leq u,\,i\notin I}(\ell_{i}-t)+\sum_{i\geq u+1,\,i\in I}(t-\ell_{i}).

[253] p: When t ∈ [ ℓ u , ℓ u + 1 ] t\in[\ell_{u},\ell_{u+1}] , this expression is a linear function of t t , and thus monotonic. The distance reaches its minimum when t t is either ℓ u \ell_{u} or ℓ u + 1 \ell_{u+1} . Therefore, we only need to consider n n candidate thresholds, where t t equals ℓ 1 , ℓ 2 , … , ℓ n \ell_{1},\ell_{2},\ldots,\ell_{n} . Utilizing this observation, the top- K K distance can be computed in linear time.

[254] h4: Integration with Immaculate .

[255] p: During inference, the server stores only the top- K K indices. During proving, the VC recomputes logits ℓ \ell using the full-precision model and verifies the recorded top- K K indices I I by evaluating Δ TopK ​ ( ℓ , I ) \Delta_{\mathrm{TopK}}(\ell,I) . The resulting distance distribution is then used for statistical verification.

[256] h2: Appendix E Ceremony: choice of t 1 t_{1} , t 2 t_{2}

[257] p: To derive the desirable hyperparameters t 1 t_{1} and t 2 t_{2} , an initial setup is required: the model provider runs both their deployed LLM and the quantized version they intend to prevent on a prescribed, sufficiently large dataset within a TEE to obtain the empirical per-request LDD as a reference. To search for the optimal hyperparameters, the auditor enumerates each t 1 t_{1} and identifies the largest corresponding t 2 t_{2} such that the detection rate exceeds 5%. The ( t 1 , t 2 ) (t_{1},t_{2}) pair yielding the lowest false positive rate is selected as the final parameter setting.

[258] h2: Appendix F Adaptive Adversary Analysis

[259] p: The preceding discussion assumes that the adversary commits to logits generated by a simplified or quantized execution. A more subtle concern is whether a rational adversary could strategically commit to fabricated logits to increase the probability of evasion. Here, we prove that as long as the LLM server is rational (though not necessarily benign), no such strategy can offer additional benefit.

[260] h4: Rationality assumption.

[261] p: We assume the adversary is rational: under a fixed computational budget T T , it always adopts the highest-quality approximation of the claimed model achievable within that budget.

[262] h6: Proposition F.1 (Logit Commitment Optimality) .

[263] p: Let ℳ opt \mathcal{M}_{\mathrm{opt}} be the best approximation of the claimed model ℳ ⋆ \mathcal{M}^{\star} achievable within budget T T . Then the adversary’s dominant strategy is to truthfully commit to the logits produced by ℳ opt \mathcal{M}_{\mathrm{opt}} .

[264] h6: Proof.

[265] p: Let ℳ T \mathcal{M}_{T} denote the set of all inference procedures executable within budget T T , and let L ℳ ​ ( x → ) L_{\mathcal{M}}(\vec{x}) be the logits produced by model ℳ \mathcal{M} on input x → \vec{x} . Let D ⁡ ( ⋅ , ⋅ ) D(\cdot,\cdot) be a distance metric measuring deviation from the claimed logits L ℳ ⋆ ​ ( x → ) L_{\mathcal{M}^{\star}}(\vec{x}) .

[266] p: By definition,

[267] table: ℳ opt = arg ⁡ min ℳ ∈ ℳ T ⁡ D ⁡ ( L ℳ ​ ( x → ) , L ℳ ⋆ ​ ( x → ) ) . \mathcal{M}_{\mathrm{opt}}=\arg\min_{\mathcal{M}\in\mathcal{M}_{T}}D\!\left(L_{\mathcal{M}}(\vec{x}),\,L_{\mathcal{M}^{\star}}(\vec{x})\right).

[268] p: Suppose the adversary generates a committed logit vector L fake L_{\mathrm{fake}} such that

[269] table: D ⁡ ( L fake , L ℳ ⋆ ​ ( x → ) ) < D ⁡ ( L ℳ opt ​ ( x → ) , L ℳ ⋆ ​ ( x → ) ) . D\!\left(L_{\mathrm{fake}},\,L_{\mathcal{M}^{\star}}(\vec{x})\right)<D\!\left(L_{\mathcal{M}_{\mathrm{opt}}}(\vec{x}),\,L_{\mathcal{M}^{\star}}(\vec{x})\right).

[270] p: Producing L fake L_{\mathrm{fake}} requires some computational process within budget T T , implying the existence of a model in ℳ T \mathcal{M}_{T} that approximates ℳ ⋆ \mathcal{M}^{\star} better than ℳ opt \mathcal{M}_{\mathrm{opt}} . This contradicts the optimality of ℳ opt \mathcal{M}_{\mathrm{opt}} . ∎

[271] h2: Appendix G Other Global LDDs

[272] p: We present visualization of global logit TV distance in Figure 4 , logit KL divergence in Figure 5 , token sampling top- K K distance in Figure 6 and expert top- K K distance in Figure 7 .

[273] figure: (a) LLaMA3-70B (b) Qwen3-32B (c) Qwen3-30B-A3B (d) DeepSeek-V2-Lite Figure 4 : Global logit TV-distance distribution. Probabilities are displayed on a logarithmic y-axis to better capture the tail behavior.

[274] figure: (a) LLaMA3-70B (b) Qwen3-32B (c) Qwen3-30B-A3B (d) DeepSeek-V2-Lite Figure 5 : Global logit KL divergence distribution. Probabilities are displayed on a logarithmic y-axis to better capture the tail behavior.

[275] figure: (a) LLaMA3-70B (b) Qwen3-32B (c) Qwen3-30B-A3B (d) DeepSeek-V2-Lite Figure 6 : Global logit Top- K K distance distribution. Probabilities are displayed on a logarithmic y-axis to better capture the tail behavior.

[276] figure: (a) Qwen3-30B-A3B (b) DeepSeek-V2-Lite Figure 7 : Global logit Top- K K distance distribution. Probabilities are displayed on a logarithmic y-axis to better capture the tail behavior.

[277] h2: Instructions for reporting errors

[278] p: We are continuing to improve HTML versions of papers, and your feedback helps enhance accessibility and mobile support. To report errors in the HTML that will help us improve conversion and rendering, choose any of the methods listed below:

[279] p: Tip: You can select the relevant text first, to include it in your report.

[280] p: Our team has already identified the following issues . We appreciate your time reviewing and reporting rendering errors we may not have found yet. Your efforts will help us improve the HTML versions for all readers, because disability should not be a barrier to accessing research. Thank you for your continued support in championing open access for all.

[281] p: Have a free development cycle? Help support accessibility at arXiv! Our collaborators at LaTeXML maintain a list of packages that need conversion , and welcome developer contributions .
