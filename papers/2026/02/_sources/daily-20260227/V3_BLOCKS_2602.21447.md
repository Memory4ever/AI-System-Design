[0] h5: Report GitHub Issue

[1] p: Content selection saved. Describe the issue below:

[2] h1: Adversarial Intent is a Latent Variable: Stateful Trust Inference for Securing Multimodal Agentic RAG

[3] h6: Abstract

[4] p: Current stateless defences for multimodal agentic RAG fail to detect adversarial strategies that distribute malicious semantics across retrieval, planning, and generation components. We formulate this security challenge as a Partially Observable Markov Decision Process (POMDP), where adversarial intent is a latent variable inferred from noisy multi-stage observations. We introduce MMA-RAG T {}^{\textsc{T}} , an inference-time control framework governed by a Modular Trust Agent ( MTA ) that maintains an approximate belief state via structured LLM reasoning. Operating as a model-agnostic overlay, MMA-RAG T {}^{\textsc{T}} mediates a configurable set of internal checkpoints to enforce stateful defence-in-depth. Extensive evaluation on 43,774 instances demonstrates a 6.50 × 6.50\times average reduction factor in Attack Success Rate relative to undefended baselines, with negligible utility cost. Crucially, a factorial ablation validates our theoretical bounds: while statefulness and spatial coverage are individually necessary ( 26.4 26.4 pp and 13.6 13.6 pp gains respectively), stateless multi-point intervention can yield zero marginal benefit under homogeneous stateless filtering when checkpoint detections are perfectly correlated.

[5] h2: 1 Introduction

[6] p: Retrieval-Augmented Generation (RAG) has evolved from static query-response pipelines ( Lewis et al., 2020 ; Gao et al., 2023 ) into agentic architectures where orchestrator LLMs plan multi-step workflows, invoke external tools, and synthesise multimodal evidence ( Yao et al., 2022 ; Schick et al., 2023 ; Ferrazzi et al., 2026 ) . While this paradigm enhances capability, it introduces a fundamentally expanded threat model. Unlike conventional LLMs where adversarial content is confined to the user prompt, agentic systems ingest hostile artifacts at multiple internal junctures: knowledge stores may harbour poisoned documents ( Zou et al., 2025 ; Cheng et al., 2024 ) , images may encode embedded directives ( Gong et al., 2025 ; Zeeshan and Satti, 2025 ) , tool outputs may carry indirect prompt injections ( Greshake et al., 2023 ; Zhan et al., 2024 ) , and the orchestrator’s reasoning chain itself may be subverted through cascading influence ( Gu et al., 2024 ; Srivastava and He, 2025 ) . Recent exploits involving Model Context Protocol (MCP) traffic further underscore the ubiquity of this surface ( Janjusevic et al., 2025 ) .

[7] figure: Figure 1: The MMA-RAG T {}^{\textsc{T}} architecture. The MTA ( 𝒜 trust \mathcal{A}_{\mathrm{trust}} ) intercepts artifacts at a set of checkpoints ( C1 - C5 in our evaluated instantiation), executes Algorithm 1 at each, and maintains a cumulative belief state Φ t \Phi_{t} . Decisions δ t ∈ { Approve , Mitigate , Refuse } \delta_{t}\!\in\!\{\textup{{Approve}},\textup{{Mitigate}},\textup{{Refuse}}\} gate artifact passage through the pipeline.

[8] p: The current defensive landscape exhibits structural gaps rooted in a failure to model this complexity. Stateless boundary filters like Llama Guard ( Inan et al., 2023 ) and NeMo Guardrails ( Rebedea et al., 2023 ) evaluate artifacts in isolation, discarding the interaction history necessary to detect multi-stage attacks. Retrieval-stage defences ( Masoud et al., 2026 ; Pathmanathan et al., 2025 ; Tan et al., 2024 ) and injection-specific methods ( Yu et al., 2026 ; Wallace et al., 2024 ; Lu et al., 2025 ) protect isolated vectors but lack mechanisms to correlate evidence across the pipeline. Even trajectory-based detectors ( Advani, 2026 ) operate reactively on completed sequences rather than proactively intercepting threats. Crucially, these approaches treat system interactions as independent events. In our B1 ablation (§ 5.3 ), removing belief state increases ASR by 26.4 26.4 pp. Moreover, under homogeneous stateless filtering where the same underlying adversarial artifact is observed through highly correlated views across checkpoints, adding more checkpoints can yield zero marginal detection benefit: the detection events become effectively perfectly correlated, so the union probability collapses to the single-checkpoint probability.

[9] p: We argue that these failures stem from a single control-theoretic problem: partial observability of adversarial intent. At any pipeline stage, a trust mechanism observes only artifact content; whether that artifact is malicious is a latent variable that must be inferred from noisy, sequential signals. This structure maps naturally to a Partially Observable Markov Decision Process (POMDP) ( Kaelbling et al., 1998 ) , where optimal defence requires maintaining a belief distribution over hidden adversarial states.

[10] p: We introduce MMA-RAG T {}^{\textsc{T}} (Figure 1 ), a defence framework whose central Modular Trust Agent ( MTA ) operationalises this probabilistic insight. Our contributions are:

[11] p: (C1) Theoretical Formalism: We model the agentic security challenge as an adversarial POMDP and derive design principles (Propositions 1 and 2 ) characterising when stateless multi-point intervention yields no marginal benefit, and why stateful belief tracking provides strict gains under partial observability (§ 3.2 ). (C2) Architecture: The MTA enforces defence-in-depth by mediating a configurable set of internal checkpoints, maintaining an approximate belief state via structured LLM inference to detect compound attacks that appear benign in isolation (§ 3.4 ). (C3) Empirical Validation: Evaluated on 43,774 instances across five threat surfaces (ART-SafeBench suite ( Singh et al., 2025 ) ), MMA-RAG T {}^{\textsc{T}} reduces Attack Success Rate (ASR) by 6.50 × 6.50\times on average (reduction factor). A × 2 2\!\times\!2 factorial ablation confirms that statefulness and spatial coverage are individually necessary, validating our theoretical derivations (§ 5 ). (C4) Deployability & Limits: The MTA operates as a model-agnostic inference overlay requiring no fine-tuning or weight access. We also identify a semantic resolution limit in tool-flip attacks (B4, 1.29 × 1.29\times reduction), delineating the boundary where text-based belief tracking must be augmented by deterministic governance (§ 6 ).

[12] p: The evaluation leverages ART-SafeBench; we summarise the benchmark generation pipeline in § 4 and provide full details in Appendix E .

[13] h2: 2 Threat Model

[14] h4: System and Adversary.

[15] p: We model the agentic RAG system as a tuple ( 𝒜 main , 𝒦 , 𝒯 , ℒ gen ) (\mathcal{A}_{\mathrm{main}},\mathcal{K},\mathcal{T},\mathcal{L}_{\mathrm{gen}}) mediated by an independent trust agent 𝒜 trust \mathcal{A}_{\mathrm{trust}} . Execution follows a trajectory τ = ( s 0 , a 0 , o 1 , … ) \tau=(s_{0},a_{0},o_{1},\ldots) over state space 𝒮 \mathcal{S} and action space 𝒜 = 𝒜 main ∪ 𝒜 trust ∪ 𝒜 gen \mathcal{A}=\mathcal{A}_{\mathrm{main}}\cup\mathcal{A}_{\mathrm{trust}}\cup\mathcal{A}_{\mathrm{gen}} (§ 3.2 ). The adversary 𝒜 adv \mathcal{A}_{\mathrm{adv}} targets OWASP-aligned objectives ( OWASP Foundation, 2025 ) : (O1) harmful outputs, (O2) control subversion, (O3) exfiltration, and (O4) resource exhaustion. Access is either black-box ( Γ BB \Gamma_{\mathrm{BB}} ) or partial ( Γ PA \Gamma_{\mathrm{PA}} ; poisoning 𝒦 adv ⊂ 𝒦 \mathcal{K}_{\mathrm{adv}}\subset\mathcal{K} ), without white-box visibility into 𝒜 trust \mathcal{A}_{\mathrm{trust}} or model weights.

[16] h4: Attack Surfaces and Partial Observability.

[17] p: Adversarial artifacts enter via inputs ( ℐ \mathcal{I} ), storage ( 𝒦 \mathcal{K} ), tools ( 𝒯 \mathcal{T} ), or inter-component channels ( ℐ ​ 𝒞 \mathcal{IC} ), instantiating three overlapping scenarios: S1 (Retrieval manipulation): poisoned content in 𝒦 \mathcal{K} surfacing via semantic similarity; S2 (Directive injection): inputs overriding system instructions (O1-O2); and S3 (State corruption): inputs biasing 𝒜 main \mathcal{A}_{\mathrm{main}} toward tool misuse or drift. Crucially, adversarial intent is a latent variable . Sophisticated adversaries can distribute attacks across stages (chaining S1-S3) such that no single observation reveals the composite threat. This renders stateless defences structurally inadequate and motivates the MTA ’s stateful belief tracking (§ 3.2 ) and multi-stage intervention (§ 3.4 ).

[18] h4: Defender Assumptions.

[19] p: Safety is defined via predicates { ϕ c } c = 1 C \{\phi_{c}\}_{c=1}^{C} over trajectories, where ϕ c ​ ( τ ) = 1 \phi_{c}(\tau)\!=\!1 iff any step triggers violation g c ​ ( s t , a t , o t + 1 ) = 1 g_{c}(s_{t},a_{t},o_{t+1})\!=\!1 (e.g., forbidden content emission, disallowed tool execution). We assume 𝒜 trust \mathcal{A}_{\mathrm{trust}} executes in a protected environment isolated from 𝒜 main \mathcal{A}_{\mathrm{main}} to decorrelate failure modes (§ 3.5 ).

[20] h2: 3 The MMA-RAG T {}^{\textsc{T}} Framework

[21] h3: 3.1 System Architecture

[22] p: MMA-RAG T {}^{\textsc{T}} augments a representative ReAct-style agentic RAG instantiation (used in our experiments) with the MTA (Figure 1 ; full integration in Algorithm 2 , Appendix C ), acting as a runtime security overlay. Practical agentic RAG systems vary in orchestration, memory, retrieval stacks, and tool routers; MMA-RAG T {}^{\textsc{T}} attaches via interposition at a configurable set of trust boundaries rather than assuming a fixed pipeline. The architecture comprises four primary components mediated by the trust layer: (i) Orchestrator 𝒜 main \mathcal{A}_{\mathrm{main}} : a ReAct-style ( Yao et al., 2022 ) planning engine (LangGraph; LangChain Inc., 2024 ) responsible for query decomposition, tool selection, and evidence synthesis. (ii) Knowledge Store 𝒦 \mathcal{K} : a multimodal vector database (ChromaDB; Chroma, 2024 ) with OpenCLIP ViT-g-14 embeddings ( Radford et al., 2021 ; Ilharco et al., 2021 ) ; images grounded via Tesseract OCR ( Google, 2024 ) . (iii) Generator ℒ gen \mathcal{L}_{\mathrm{gen}} : produces the final user-facing response conditioned on retrieved context. (iv) Trust Agent 𝒜 trust \mathcal{A}_{\mathrm{trust}} : an isolated subsystem maintaining its own LLM instance, persistent belief state, and communicating exclusively through a configurable set of interception checkpoints. Critically, 𝒜 trust \mathcal{A}_{\mathrm{trust}} is orthogonal to the functional pipeline: it attaches to 𝒜 main \mathcal{A}_{\mathrm{main}} , 𝒦 \mathcal{K} , and ℒ gen \mathcal{L}_{\mathrm{gen}} via API interposition, requiring no weight access or architectural modification.

[23] h3: 3.2 Adversarial POMDP Formalisation

[24] p: We ground the MTA ’s design in the POMDP framework. This formalism provides the axiomatic basis for reasoning about adversarial intent as a latent variable under the partial observability established in § 2 .

[25] h6: Definition 1 (Adversarial Agentic RAG POMDP) .

[26] p: The interaction is defined by the tuple ( 𝒮 , 𝒜 , Ω , T , O , J ) (\mathcal{S},\mathcal{A},\Omega,T,O,J) where: 𝒮 = 𝒮 env × 𝒮 adv \mathcal{S}=\mathcal{S}_{\mathrm{env}}\times\mathcal{S}_{\mathrm{adv}} factors into the observable environment state (documents, tool outputs) and the latent adversarial state (benign vs. malicious intent); 𝒜 = { Approve , Mitigate , Refuse } \mathcal{A}=\{\textup{{Approve}},\textup{{Mitigate}},\textup{{Refuse}}\} is the trust-agent action space; the remaining pipeline dynamics are absorbed into T T ; Ω \Omega is the observation space for 𝒜 trust \mathcal{A}_{\mathrm{trust}} . Each checkpoint yields an observation o t ∈ Ω o_{t}\in\Omega comprising the current artifact C t C_{t} , its type, and channel metadata (e.g., retrieval provenance, tool name, or parsing context); T : 𝒮 × 𝒜 → Δ ⁡ ( 𝒮 ) T\!:\!\mathcal{S}\!\times\!\mathcal{A}\!\to\!\Delta(\mathcal{S}) is the transition kernel; and O : 𝒮 × 𝒜 → Δ ⁡ ( Ω ) O\!:\!\mathcal{S}\!\times\!\mathcal{A}\!\to\!\Delta(\Omega) is the observation function mapping hidden states to observations. The objective J = J util − λ ​ ∑ t = 1 H J viol ​ ( s t , a t ) J=J_{\mathrm{util}}-\lambda\sum_{t=1}^{H}J_{\mathrm{viol}}(s_{t},a_{t}) trades off task utility (including refusal cost) against safety violations ( J viol ∈ { 0 , 1 } J_{\mathrm{viol}}\!\in\!\{0,1\} ; λ > 0 \lambda>0 ).

[27] h4: Approximate Belief State Maintenance.

[28] p: In a canonical POMDP, the agent maintains a sufficient statistic b t ∈ Δ ⁡ ( 𝒮 ) b_{t}\in\Delta(\mathcal{S}) via the exact Bayesian update:

[29] table: b t ​ ( s ′ ) ∝ O ⁡ ( o t ∣ s ′ , a t − 1 ) ​ ∑ s T ⁡ ( s ′ ∣ s , a t − 1 ) ​ b t − 1 ​ ( s ) . b_{t}(s^{\prime})\propto O(o_{t}\!\mid\!s^{\prime},a_{t\!-\!1})\sum_{s}T(s^{\prime}\!\mid\!s,a_{t\!-\!1})\,b_{t\!-\!1}(s). (1)

[30] p: For agentic RAG, the state space 𝒮 \mathcal{S} encompasses high-dimensional document semantics, tool configurations, reasoning traces, and adversarial strategies, rendering exact belief maintenance via Eq. ( 1 ) intractable. The MTA therefore maintains a structured natural-language approximate belief state Φ t \Phi_{t} (an information state that serves as a tractable proxy for the exact posterior b t b_{t} ):

[31] table: Φ t = f θ ​ ( Φ t − 1 , o t ) , \Phi_{t}=f_{\theta}\!\left(\Phi_{t-1},\;o_{t}\right), (2)

[32] p: where f θ f_{\theta} is a single frozen LLM inference call that ingests the prior state Φ t − 1 \Phi_{t-1} (which encodes decision history) and the current observation o t o_{t} . The prompt (Appendix A ) instructs the LLM to produce a structured summary encoding cumulative risk indicators, a threat-level assessment, and the decision history for the current query. Φ t \Phi_{t} plays the functional role of an approximate information state ( Kaelbling et al., 1998 ) : it compresses the history h t = ( o 1 , δ 1 , … , o t ) h_{t}=(o_{1},\delta_{1},\ldots,o_{t}) into a fixed-format representation that the policy conditions upon, bypassing explicit value iteration. Ablating Φ t \Phi_{t} degrades defence by 26.4 26.4 pp (§ 5.3 ), confirming that this approximation captures decision-relevant latent variables.

[33] h4: Belief compression and token efficiency.

[34] p: An alternative to maintaining Φ t \Phi_{t} is to append the full interaction log h t h_{t} into the trust-agent prompt at each checkpoint. For K K checkpoint interceptions in a query, this yields input contexts whose length grows with t t , resulting in 𝒪 ⁡ ( K 2 ) \mathcal{O}(K^{2}) total prompt tokens across checkpoints. In contrast, Φ t \Phi_{t} is a fixed-format summary with bounded size, yielding 𝒪 ⁡ ( K ) \mathcal{O}(K) scaling and enabling stateful trust inference under production context limits.

[35] p: We derive two structural properties from this formulation that generate falsifiable predictions validated in § 5 .

[36] h6: Proposition 1 (Strict Value of Memory) .

[37] p: Let Π Ω = { π : Ω → 𝒜 } \Pi_{\Omega}=\{\pi:\Omega\to\mathcal{A}\} denote the set of stateless (observation-memoryless) policies and Π Φ = { π : Ω × Φ → 𝒜 } \Pi_{\Phi}=\{\pi:\Omega\times\Phi\to\mathcal{A}\} denote belief-conditioned policies. Define the value function V ⁡ ( Π ) ≜ sup π ∈ Π 𝔼 π ​ [ J ] V(\Pi)\triangleq\sup_{\pi\in\Pi}\,\mathbb{E}_{\pi}[J] . Then:

[38] table: V ⁡ ( Π Φ ) ≥ V ⁡ ( Π Ω ) , V(\Pi_{\Phi})\;\geq\;V(\Pi_{\Omega}), (3)

[39] p: and under partial observability the inequality can be strict, e.g., when there exist histories h t , h t ′ h_{t},h^{\prime}_{t} with the same instantaneous observation o t o_{t} but different posteriors over 𝒮 adv \mathcal{S}_{\mathrm{adv}} .

[40] p: Proof sketch. See Appendix H .

[41] h6: Proposition 2 (Checkpoint Correlation Structure) .

[42] p: Consider a fixed query execution with K K checkpoint interceptions. Let D t ∈ { 0 , 1 } D_{t}\!\in\!\{0,1\} denote the event that checkpoint t t detects an adversarial artifact. (i) Under a homogeneous stateless detector d : Ω → { 0 , 1 } d\!:\!\Omega\!\to\!\{0,1\} applied at every checkpoint, if the observations of a given adversarial artifact across checkpoints fall in the same equivalence class of d d , then D t = D 1 D_{t}=D_{1} for all t t , so ρ ⁡ ( D i , D j ) = 1 \rho(D_{i},D_{j})=1 for all pairs i , j i,j and P ( ⋃ t = 1 K { D t = 1 } ) = P ( D 1 = 1 ) P(\bigcup_{t=1}^{K}\{D_{t}\!=\!1\})=P(D_{1}\!=\!1) . Additional stateless checkpoints yield no marginal detection benefit in this regime. (ii) Under a belief-conditioned detector d t : Ω × Φ t − 1 → { 0 , 1 } d_{t}\!:\!\Omega\times\Phi_{t-1}\!\to\!\{0,1\} , evidence accumulated in Φ t − 1 \Phi_{t-1} can push a later checkpoint past the detection threshold even when o t o_{t} alone is insufficient; consequently, one can have P ( ⋃ t = 1 K { D t = 1 } ) > P ( D 1 = 1 ) P(\bigcup_{t=1}^{K}\{D_{t}\!=\!1\})>P(D_{1}\!=\!1) .

[43] p: Proof sketch. See Appendix H .

[44] h3: 3.3 Inference-Action Loop

[45] p: At each checkpoint t t , the MTA executes a four-step control cycle (Algorithm 1 , Appendix B ): (1) Observe : Intercept artifact C t C_{t} and retrieve belief state Φ t − 1 \Phi_{t-1} . (2) Infer : Execute the trust policy π T \pi_{T} via LLM inference to generate a risk assessment r t r_{t} and updated belief Φ t \Phi_{t} . (3) Decide : Map r t r_{t} to an action δ t ∈ { Approve , Mitigate , Refuse } \delta_{t}\in\{\textup{{Approve}},\textup{{Mitigate}},\textup{{Refuse}}\} . (4) Act : Enforce δ t \delta_{t} and commit Φ t \Phi_{t} to memory.

[46] h4: Inference-aligned policy execution.

[47] p: The trust policy π T \pi_{T} is executed through LLM inference rather than a separate rule engine. Policy specifications (threat indicators, evidence-weighting heuristics, decision thresholds, JSON output schema) are encoded as structured instructions in the MTA ’s system prompt (Appendix A ). This design leverages the LLM’s pre-trained knowledge of adversarial patterns and social engineering tactics without requiring explicit attack-signature enumeration, enabling context-sensitive compositional reasoning: for instance, recognising that “ignore previous context” constitutes an injection attempt even in novel phrasings. Because π T \pi_{T} is specified at inference time, 𝒜 trust \mathcal{A}_{\mathrm{trust}} is model-agnostic: it can be instantiated with either general-purpose foundation models or smaller specialist safety models (including fine-tuned LLMs), and can use heterogeneous backbones across checkpoints to trade off latency and fidelity. This also provides a direct upgrade path: improving or fine-tuning the trust-agent model can improve assessment and mitigation fidelity without modifying or retraining 𝒜 main \mathcal{A}_{\mathrm{main}} or ℒ gen \mathcal{L}_{\mathrm{gen}} .

[48] h4: Formal-to-implementation mapping.

[49] p: The POMDP objects are instantiated as follows: (1) Φ t − 1 \Phi_{t-1} (“Current Suspicion Context” in the prompt; Appendix A ) approximates the belief b t b_{t} (Eq. 1 ); (2) the LLM’s “Updated Suspicion Context” implements an approximate belief update; and (3) π T \pi_{T} , encoded as structured system-prompt instructions, maps ( Φ t − 1 , o t ) (\Phi_{t-1},o_{t}) to δ t \delta_{t} as the approximate policy. This grounding ensures that the theoretical benefits of belief-state estimation are realised in the implementation without the tractability costs of explicit Bayesian filtering, and generates the predictions validated in § 5.3 .

[50] h4: Effector Primitives.

[51] p: Upon deciding δ t \delta_{t} : (a) Approve : artifact passes unchanged; (b) Mitigate : the MTA outputs a sanitised artifact that preserves benign content while neutralising threats. Mitigation can be implemented via LLM rewriting, deterministic safety tools (e.g., argument-schema validation for tool calls, allowlists, PII scrubbing, URL stripping), or a hybrid; (c) Refuse : workflow is terminated with a safe fallback response. Operationally, these safety tools execute within 𝒜 trust \mathcal{A}_{\mathrm{trust}} ’s isolated environment and return only sanitised artifacts or validated actions through the interception interface, keeping integration non-invasive.

[52] h3: 3.4 Configurable Checkpoints: Defence-in-Depth

[53] p: The MTA implements per-stage filtering to address the specific attack surfaces defined in § 2 . In general, the checkpoint set is determined by the system’s trust boundaries; we instantiate a representative checkpoint set (C1-C5) mapping to common boundaries in multimodal agentic RAG: C1 (Query Screening): Filters user input ℐ \mathcal{I} for jailbreaks and payload encoding. C2 (Action Validation): Validates 𝒜 main \mathcal{A}_{\mathrm{main}} ’s tool selection against the query intent, detecting agentic state corruption (S3). C3 (Retrieval Screening): Filters 𝒦 \mathcal{K} retrievals for poisoned content (S1) before generator consumption. C4 (Tool Output Screening): Inspects external tool returns 𝒯 \mathcal{T} for indirect injections. C5 (Response Verification): Validates the final generation ℒ gen \mathcal{L}_{\mathrm{gen}} for policy compliance. No single checkpoint suffices: an adversary aware of C1 routes attacks through 𝒦 \mathcal{K} ; one aware of C3 uses tool outputs; one aware of C5 distributes the attack across earlier stages. Within our instantiation, restricting defence to C5 alone incurs a 13.6 13.6 pp degradation (§ 5.3 ), demonstrating the necessity of intercepting attacks at their source before downstream reasoning corruption occurs.

[54] h3: 3.5 Architectural Resilience

[55] p: To prevent the MTA from becoming a single point of failure, we enforce three properties: Execution Isolation : 𝒜 trust \mathcal{A}_{\mathrm{trust}} operates in a disjoint memory space with independent system prompts, preventing context contamination from 𝒜 main \mathcal{A}_{\mathrm{main}} . Model Heterogeneity : 𝒜 trust \mathcal{A}_{\mathrm{trust}} may utilise a distinct model architecture to mitigate transfer attacks. Auditability : All belief updates and decisions are immutable logs, facilitating post-hoc forensic analysis and iterative policy refinement.

[56] h2: 4 Experimental Setup

[57] h4: System Configuration.

[58] p: We evaluate MMA-RAG T {}^{\textsc{T}} against a baseline multimodal agentic RAG pipeline with no trust layer (identical architecture without 𝒜 trust \mathcal{A}_{\mathrm{trust}} ). The baseline is a representative instantiation used solely for controlled evaluation and is not itself claimed as a contribution. Both systems share a fixed infrastructure: ChromaDB vector store with OpenCLIP ViT-g-14 embeddings ( Radford et al., 2021 ; Ilharco et al., 2021 ) , Tesseract v5.3.1 for OCR, and LangGraph ( LangChain Inc., 2024 ) for orchestration. To ensure reproducibility, all deterministic operations (generation, judgment, and MTA policy execution) use temperature T = 0.0 T\!=\!0.0 . We assess generalisation across four LLM backbones: GPT-4o, GPT-4o-mini, Llama-3.3-70B, and GPT-4.1. The MTA itself employs a frozen GPT-4o instance for inference and mitigation. Unless otherwise noted, aggregate results report the GPT-4o backbone.

[59] h4: Evaluation Corpus.

[60] p: Security is assessed on the ART-SafeBench suite ( Singh et al., 2025 ) , comprising 43,774 validated adversarial instances across five threat surfaces: B1 (Text Poisoning, n = 10,943 n\!=\!10{,}943 ): Instruction overrides and persona manipulations embedded in retrieved documents. B2 (Image Poisoning, n = 4,000 n\!=\!4{,}000 ): Adversarial text programmatically rendered onto images, split into OCR-mediated (B2a) and direct multimodal (B2b) vectors. B3 (Direct Query, n = 10,005 n\!=\!10{,}005 ): Zero-shot adversarial prompts spanning OWASP Top-10 categories ( OWASP Foundation, 2025 ) . B4 (Tool-Flip, n = 14,400 n\!=\!14{,}400 ): Dual-query injections forcing semantically plausible but adversarially motivated tool switching. B5 (Agentic Integrity, n = 4,426 n\!=\!4{,}426 ): Multi-turn interactions targeting reasoning chain corruption and incremental policy drift. Instances are generated via a closed-loop validated synthesis pipeline with ∼ \sim 37% acceptance rate. We provide a four-stage summary in Appendix E and list the corresponding five-step instantiation for reproducibility; record schema in Appendix F . Utility is measured on Natural Questions (dev, n = 3,610 n\!=\!3{,}610 ) ( Kwiatkowski et al., 2019 ) using the ARES framework ( Saad-Falcon et al., 2023 ) for Context Relevance (CR) and Answer Relevance (AR).

[61] h4: Adjudication Protocol.

[62] p: We define Attack Success Rate (ASR) as the proportion of trajectories satisfying an adversarial success predicate κ \kappa :

[63] table: ASR = 1 | 𝒟 atk | ∑ x ∈ 𝒟 atk 𝕀 [ κ ( g , x , T ( x ) ) ≥ τ ] . \mathrm{ASR}=\frac{1}{|\mathcal{D}_{\mathrm{atk}}|}\sum_{x\in\mathcal{D}_{\mathrm{atk}}}\mathbb{I}\bigl[\kappa(g,x,T(x))\geq\tau\bigr]. (4)

[64] p: For B1, B2, B3, and B5, κ \kappa is a deterministic GPT-4o judge ( T = 0 T\!=\!0 ). For B4 (Tool-Flip), κ \kappa is a formal predicate verifying divergence from the ground-truth tool selection. To validate the automated judge, we manually audited a stratified sample of 750 instances, yielding > > 95% agreement overall (100% on B1/B2/B4/B5; 85% on B3 due to subjective ambiguity in bias categories) ( Zheng et al., 2023 ) .

[65] h2: 5 Results and Analysis

[66] h3: 5.1 Utility Preservation

[67] p: The addition of the trust layer introduces negligible degradation in downstream utility (Table 1 ). MMA-RAG T {}^{\textsc{T}} achieves CR = 0.87 =0.87 and AR = 0.93 =0.93 , comparable to the baseline (CR = 0.88 =0.88 , AR = 0.93 =0.93 ) and competitive with established baselines under the same ARES protocol ( Saad-Falcon et al., 2023 ) . The minimal CR reduction confirms that the MTA ’s filtering preserves the semantic integrity of valid retrieval-generation workflows.

[68] figure: Configuration CR ↑ \uparrow AR ↑ \uparrow ColBERTv2 + GPT-4 0.90 0.82 DPR + BART 0.62 0.58 Agentic RAG (baseline) 0.88 0.93 MMA-RAG T {}^{\textsc{T}} (+ MTA ) 0.87 0.93 Table 1: Utility on Natural Questions (dev, n = 3,610 n\!=\!3{,}610 ). ARES scores (context relevance CR, answer relevance AR). Established baselines from Saad-Falcon et al. (2023) included for reference. Differences between the baseline and MMA-RAG T {}^{\textsc{T}} are small.

[69] h3: 5.2 Defence Efficacy

[70] p: Across the 43,774 instances of the ART-SafeBench suite, MMA-RAG T {}^{\textsc{T}} reduces ASR with an average reduction factor of 6.50 × 6.50\times (Table 2 , Figure 2 (a)). We analyse performance by threat surface.

[71] figure: Benchmark Baseline + MTA Red. B1: Text poisoning 76.5 15.7 × 4.87\!\times B2a: Image (OCR) 22.3 2.0 × 11.15\!\times B2b: Image (MM) 10.1 5.5 × 1.84\!\times B3: Direct query 59.0 4.1 × 14.39\!\times B4: Tool-flip 82.1 63.5 × 1.29\!\times B5: Agentic integrity 48.5 8.9 × 5.45\!\times Avg. (factor) - - × \mathbf{6.50\!\times} Table 2: ASR (%, ↓ \downarrow ) across ART-SafeBench benchmarks with GPT-4o backbone. Reduction factor = = baseline ASR / defended ASR. Avg. (factor) is the unweighted mean of per-benchmark reduction factors.

[72] figure: Figure 2: Experimental results overview. (a) ASR across all ART-SafeBench benchmarks: the MTA reduces ASR on every surface, with reduction factors ranging from 1.3 × 1.3\times (B4, tool-flip) to 14.4 × 14.4\times (B3, direct query); mean factor 6.50 × 6.50\times . (b) Factorial ablation on B1: statefulness contributes − 26.4 -26.4 pp and multi-stage coverage − 13.6 -13.6 pp; the two mechanisms are individually necessary and their combination yields super-additive gains, validating Propositions 1 and 2 . (c) Cross-LLM generalisation on B1: defence transfers across four backbones ( × 2.5\!\times - × 9.5\!\times reduction), with invariant relative difficulty ordering.

[73] h4: High-efficacy surfaces (B1, B2a, B3).

[74] p: The MTA excels where adversarial artifacts carry explicitly observable signals. On B3 ( 14.39 × 14.39\times ), C1 is highly effective against direct adversarial queries, reducing ASR to 4.1% (95% CI: 3.7-4.5%). Per-OWASP breakdown for the six instantiated categories (Table 5 , Appendix G ; n = 4,978 n=4{,}978 of 10,005): information disclosure (LLM02) and supply-chain attacks (LLM03) are eliminated entirely; insecure output handling (LLM05) drops to < < 1%. Residual ASR concentrates in prompt injection (LLM01: → 8 % 64\!\to\!8\% ) and misinformation (LLM09), where adversarial content most closely resembles legitimate requests. On B1 ( 4.87 × 4.87\times ), belief-state accumulation across C3 and C5 reduces ASR from 76.5% to 15.7% (95% CI: 15.0-16.4%), detecting subtly poisoned content whose adversarial intent emerges only when correlated across pipeline stages. B2a (OCR-mediated, 11.15 × 11.15\times ) is more vulnerable than B2b since OCR faithfully transcribes adversarial text into the generator context: → 2.0 % 22.3\!\to\!2.0\% (95% CI: 1.3-3.1%).

[75] h4: The semantic resolution limit (B4, B2b).

[76] p: B4 (Tool-Flip) yields the lowest reduction ( 1.29 × 1.29\times ; → 63.5 % 82.1\!\to\!63.5\% ; 95% CI: 62.7-64.3%), confirming the semantic resolution limit of text-based belief tracking. Tool-flip attacks manipulate 𝒜 main \mathcal{A}_{\mathrm{main}} ’s action-selection logic at a semantic level closely resembling legitimate reasoning; we analyse this gap in § 6 . B2b (direct multimodal, 1.84 × 1.84\times ) proves harder than B2a ( → 5.5 % 10.1\!\to\!5.5\% ; 95% CI: 4.3-7.1%), delineating a perceptual boundary where visual injections bypass the symbolic reasoning accessible to the text-based trust policy.

[77] h4: Agentic integrity (B5, 5.45 × 5.45\times ).

[78] p: Multi-stage attacks on the orchestrator’s reasoning chain are reduced to 8.9% (95% CI: 8.1-9.8%) through belief-state accumulation across stages (Proposition 1 ), enabling detection of compound attacks where no single observation is independently suspicious.

[79] h4: Cross-LLM generalisation.

[80] p: Efficacy transfers across protected backbones (Figure 2 (c); Appendix D ). On B1, ASR ranges from 7.5% (Llama-3.3-70B) to 31.5% (GPT-4o-mini) under MMA-RAG T {}^{\textsc{T}} , vs. baseline ranges of 70.9-78.4%, yielding × 2.5\!\times - × 9.5\!\times reduction factors. The relative difficulty ordering (B4 hardest, B3 easiest) remains invariant across all four backbones, suggesting that effectiveness derives from architectural placement and the belief-state mechanism rather than idiosyncrasies of a single backbone.

[81] h3: 5.3 Ablation: Empirical Validation of Theory

[82] p: We employ a × 2 2\!\times\!2 factorial design on B1 (Table 3 , Figure 2 (b)) to empirically validate the design principles derived in § 3.2 . B1 is selected as the median-difficulty surface that exercises all checkpoints in our evaluated instantiation (C1-C5) and stresses both belief-state accumulation and spatial coverage.

[83] figure: Configuration ASR ↓ \downarrow 𝚫 \boldsymbol{\Delta} pp Refusals No MTA (baseline) 76.5 +19.8 - Stateless, final-only 56.7 † 0.0 † - Stateful, final-only 43.9 − 12.8 -12.8 18 Stateless, multi-stage 56.7 ref. 45 Stateful, multi-stage 30.3 − 26.4 \mathbf{-26.4} 42 Table 3: Ablation on B1 (%). Stateful : belief state maintained across checkpoints. Multi-stage : all C1-C5. Δ \Delta pp: change vs. stateless, multi-stage (ref.). Refusals: total MTA block actions per evaluation run. † \dagger Implied by Proposition 2 (i); not independently measured. Stateless configurations structurally model existing boundary-filter paradigms.

[84] h4: Structural equivalence to existing defences.

[85] p: The ablation configurations instantiate common defence paradigms: stateless, final-only models boundary classifiers such as Llama Guard ( Inan et al., 2023 ) , while stateless, multi-stage models multi-point guardrails such as NeMo Guardrails ( Rebedea et al., 2023 ) . Proposition 2 (i) characterises when these stateless deployments collapse under homogeneous filtering, and the remaining gap to MMA-RAG T {}^{\textsc{T}} isolates the incremental value of belief conditioning beyond stateless boundary filtering.

[86] h4: Validation of Propositions 2 and 1 .

[87] p: The stateless multi-stage configuration achieves 56.7 % 56.7\% ASR, and Proposition 2 (i) implies the corresponding stateless final-only detector is equivalent in the high-correlation regime (Table 3 , † \dagger ). Introducing belief state yields a 26.4 26.4 pp gain ( 56.7 % → 30.3 % 56.7\%\!\to\!30.3\% ), confirming the strict value of memory (Proposition 1 ), and restores marginal value to additional checkpoints as evidenced by the 13.6 13.6 pp gap between stateful final-only ( 43.9 % 43.9\% ) and stateful multi-stage ( 30.3 % 30.3\% ), supporting Proposition 2 (ii).

[88] h4: Refusal-stage analysis.

[89] p: On B5, refusals concentrate at C2 (agent action validation), indicating that multi-stage gating can block integrity attacks before downstream reasoning corruption.

[90] h4: Latency and cost.

[91] p: On N = 100 N\!=\!100 Natural Questions queries, mean end-to-end response time increases from 2.59 ± 0.77 2.59\pm 0.77 s to 8.64 ± 2.92 8.64\pm 2.92 s, a 3.34 × 3.34\times overhead. In our evaluated configuration, this corresponds to an estimated ∼ \sim 3,500-5,000 additional input tokens and ∼ \sim 800-1,200 output tokens per query; full analysis and optimisation paths are provided in Appendix I .

[92] h2: 6 Discussion

[93] h4: Inference-time policy approximation.

[94] p: LLM inference can approximate policies for security POMDPs with semantic state spaces by realising belief updates and actions through structured prompts rather than weight updates. In our evaluation, this yields a 6.50 × 6.50\times average ASR reduction factor while preserving auditability and enabling upgrades by swapping or fine-tuning the trust-agent model without retraining 𝒜 main \mathcal{A}_{\mathrm{main}} or ℒ gen \mathcal{L}_{\mathrm{gen}} .

[95] h4: Belief compression.

[96] p: Storing adversarial intent as an abstract belief state keeps token costs bounded: naively appending full logs causes prompt length to grow with the number of checkpoints, whereas the fixed-format Φ t \Phi_{t} yields bounded per-checkpoint context. This makes stateful multi-stage defence feasible under production context limits without retaining raw interaction traces in the trust prompt.

[97] h4: Synergy of statefulness and coverage.

[98] p: The factorial ablation (Table 3 ) exhibits a super-additive interaction: memory and multi-stage coverage are individually necessary and jointly strongest. Memory breaks checkpoint-level correlation (Proposition 2 ), while checkpoints provide the observations required to update Φ t \Phi_{t} .

[99] h4: The semantic resolution limit (B4).

[100] p: B4 yields the weakest defence ( 1.29 × 1.29\times ), reflecting a semantic resolution limit: adversarial and benign trajectories can induce observations that are indistinguishable under O O , constraining discrimination even with full history. Mitigating this class requires complementary non-semantic controls such as tool allowlists, argument-schema validation, and query-conditioned constraints. Counterfactual checks over tool choice (e.g., re-evaluating actions under ablated context) are a natural next step.

[101] h4: Operational corollary.

[102] p: Deployment heuristic: prioritise belief-state infrastructure over scaling stateless checkpoints, since high correlation can render stateless checkpoint scaling redundant (Proposition 2 ). The MMA-RAG T {}^{\textsc{T}} overlay remains composable with retrieval-stage defences ( Masoud et al., 2026 ; Pathmanathan et al., 2025 ) , injection-specific methods ( Yu et al., 2026 ) , and trajectory anomaly detection ( Advani, 2026 ) .

[103] h2: 7 Related Work

[104] h4: Agentic threats.

[105] p: Agentic RAG expands the attack surface beyond the user prompt, including retrieval poisoning ( Zou et al., 2025 ; Cheng et al., 2024 ; Xue et al., 2024 ; Zhao et al., 2025 ) , multimodal injections ( Gong et al., 2025 ; Zeeshan and Satti, 2025 ) , indirect tool injections ( Greshake et al., 2023 ; Zhan et al., 2024 ) , multi-agent subversion ( Gu et al., 2024 ) , persistent state corruption ( Srivastava and He, 2025 ) , and MCP-mediated attacks ( Janjusevic et al., 2025 ) . Surveys and audits highlight systematic coverage gaps in current defences and scanners ( Yu et al., 2025 ; Brokman et al., 2025 ) .

[106] h4: Defences and formalisation.

[107] p: Boundary filters and guardrails are largely stateless ( Inan et al., 2023 ; Rebedea et al., 2023 ; Zeng et al., 2024 ; Ganon et al., 2025 ) , while component-specific defences target isolated vectors ( Masoud et al., 2026 ; Pathmanathan et al., 2025 ; Tan et al., 2024 ; Yu et al., 2026 ; Wallace et al., 2024 ; Lu et al., 2025 ; Ramakrishnan and Balaji, 2025 ; Syed et al., 2025 ) . TrustAgent ( Hua et al., 2024 ) is closest in spirit but does not maintain a belief state; we formalise agentic security as a POMDP ( Kaelbling et al., 1998 ; Chatterjee et al., 2016 ; Gmytrasiewicz and Doshi, 2005 ) and operationalise belief-conditioned intervention. Our ablation isolates the impact of statefulness and exposes a regime where scaling stateless checkpoints yields no marginal benefit under high correlation (Proposition 2 ). Viewed this way, MMA-RAG T {}^{\textsc{T}} functions as a belief integrator that can layer atop existing component defences to supply cross-stage context.

[108] h4: Stateless scaling and trajectory detectors.

[109] p: Absent a shared information state, multi-point stateless deployments remain memoryless detectors whose block decisions depend only on the local observation. Formally, this corresponds to P ⁡ ( block ∣ o t , h t ) = P ⁡ ( block ∣ o t ) P(\text{block}\mid o_{t},h_{t})=P(\text{block}\mid o_{t}) , and Proposition 2 (i) identifies a high-correlation regime where additional stateless checkpoints yield zero marginal benefit. Reactive trajectory-level methods such as Trajectory Guard ( Advani, 2026 ) detect anomalous completed interactions, whereas MMA-RAG T {}^{\textsc{T}} enforces proactive gating at internal trust boundaries via belief-conditioned intervention.

[110] h4: Control-theoretic foundations.

[111] p: POMDPs and their adversarial and interactive variants formalise acting under partial observability ( Kaelbling et al., 1998 ; Chatterjee et al., 2016 ; Gmytrasiewicz and Doshi, 2005 ) , but exact solvers are intractable for natural-language state spaces. Our approach operationalises approximate belief tracking via structured LLM inference and checkpointed intervention in the agent loop.

[112] h2: 8 Conclusion

[113] p: We introduced MMA-RAG T {}^{\textsc{T}} , formalising agentic RAG security as a POMDP where adversarial intent is latent and tracked via an approximate belief state. On 43,774 ART-SafeBench instances, MMA-RAG T {}^{\textsc{T}} achieves a 6.50 × 6.50\times average ASR reduction factor with negligible utility impact, and factorial ablation validates the predicted role of memory and checkpoint coverage. On B1, the factorial ablation shows that belief state and multi-stage coverage are individually necessary (26.4 pp and 13.6 pp gaps) and jointly super-additive. Because the trust layer is model-agnostic and inference-aligned, it can be deployed with specialised safety models or upgraded foundations, with defence fidelity improving with trust-model capability. More broadly, the checkpoint set is configurable and should be selected to match application trust boundaries rather than a fixed pipeline.

[114] h4: Limitations.

[115] p: We rely on a deterministic GPT-4o judge, so evaluator bias may remain despite > 95 % >95\% manual agreement. Tool-flip attacks reveal a language-level observational-equivalence limit and require deterministic tool governance beyond semantic belief tracking. The overlay adds a 3.34 × 3.34\times latency overhead (Appendix I ) and we do not evaluate adaptive checkpoint scheduling or parallelisation. As a fixed policy, MMA-RAG T {}^{\textsc{T}} may be vulnerable to white-box prompt optimisation and recursive injection, and other orchestration or memory designs may require different checkpoint placements.

[116] h2: References

[117] h2: Appendix A MTA Prompt Template

[118] p: The trust policy π T \pi_{T} is encoded as a structured system prompt provided to the MTA ’s frozen LLM at each checkpoint. This prompt serves as the inference-time operationalisation of the POMDP-motivated policy, comprising four functional components:

[119] p: (1) Role Specification: Establishes the LLM as the decision-making kernel, enforcing conservative reasoning principles (precautionary principle, stateful assessment, and proportional response).

[120] p: (2) Checkpoint-Specific Directives: Modular instructions tailored to the current observation type. For instance, C3 (Retrieval) focuses on identifying latent instruction overrides embedded in documents, while C2 (Action) validates the semantic consistency of tool calls against the user’s original intent.

[121] p: (3) Belief State Injection: The cumulative belief state Φ t − 1 \Phi_{t-1} is injected verbatim into a designated “Current Suspicion Context” field. This provides the LLM with explicit access to the cross-stage history h t − 1 h_{t-1} , enabling the detection of distributed attacks.

[122] p: (4) Output Schema: A strict JSON schema requiring: (a) risk assessment with chain-of-thought reasoning, (b) a scalar risk score r ∈ [ 0 , 1 ] r\in[0,1] , (c) the decision δ t ∈ { Approve , Mitigate , Refuse } \delta_{t}\in\{\textup{{Approve}},\textup{{Mitigate}},\textup{{Refuse}}\} , (d) sanitised artifacts (if δ t = Mitigate \delta_{t}=\textup{{Mitigate}} ), (e) the updated belief state Φ t \Phi_{t} , and (f) internal justification for audit logs.

[123] h4: Verbatim Template (Abridged).

[124] p: The system prompt below illustrates how the POMDP policy is operationalised via natural language instructions.

[125] p: System Prompt π T \pi_{T} You are the Modular Trust Agent (MTA) operating within a multimodal agentic RAG framework. The system operates in an adversarial environment where user queries, database entries, or tool outputs may contain malicious instructions, prompt-injection attempts, or other adversarial behaviour. Suspicious or harmful patterns can appear gradually across multi-turn or multi-agent conversations. Role. At each inference step, you receive: (1) Newly presented content C C (user query, tool decision, retrieved data, or final answer draft); (2) A partial Suspicion Context Φ \Phi , your memory of suspicious or adversarial clues accumulated so far; (3) Policy guidelines π T \pi_{T} for handling disallowed content. Procedure. 1. Integrate C C with Φ \Phi to update beliefs about adversarial patterns. (Reflect partial observability: you do NOT see an entire malicious plan at once.) 2. Decide among { Approve , Mitigate , Refuse }: - Approve if safe with no suspicious aspects. - Mitigate if partially disallowed but sanitisable while preserving valuable information. - Refuse if irredeemably harmful or disallowed (e.g., instructions for violent wrongdoing, persistent prompt-injection). 3. Return structured JSON: {"decision": ..., "updatedContext": ..., "hiddenJustification": ...} . updatedContext is the revised suspicion context; escalate suspicion logs upon repeated suspicious attempts. hiddenJustification is the internal rationale for audit logs. Policy Rules. - If you see potential prompt injections (“Ignore your rules”, etc.), do not comply; use Mitigate for minor cases or Refuse if severe. - If queries request disallowed content (violence instructions, extremist content, PII), Refuse . - If suspicious patterns recur, escalate from Approve to Mitigate or Refuse . - For hidden or obfuscated instructions to override the system, Mitigate or Refuse . - Remember we are in a POMDP: carry forward suspicious signals in updatedContext .

[126] p: Per-Checkpoint User Message CURRENT SUSPICION CONTEXT ( Φ \Phi ): { Φ t − 1 \Phi_{t-1} } NEW CONTENT TO CHECK: { C t C_{t} } INSTRUCTIONS: 1. Integrate the new content with the suspicion context. 2. Decide among {APPROVE, MITIGATE, REFUSE}. 3. Return structured JSON.

[127] h2: Appendix B MTA Inference-Action Algorithm

[128] p: Algorithm 1 formalises the control loop executed at each checkpoint.

[129] figure: Algorithm 1 MTA Inference-Action Cycle at Checkpoint t t 1: Artifact C t C_{t} , belief state Φ t − 1 \Phi_{t-1} , policy π T \pi_{T} 2: Decision δ t \delta_{t} , updated Φ t \Phi_{t} , output C t ′ C^{\prime}_{t} 3: o t ← Observe ​ ( C t , type t ) o_{t}\leftarrow\textsc{Observe}(C_{t},\mathrm{type}_{t}) 4: r t , Φ t , trace t ← Infer ​ ( Φ t − 1 , o t , π T ) r_{t},\Phi_{t},\mathrm{trace}_{t}\leftarrow\textsc{Infer}(\Phi_{t-1},o_{t},\pi_{T}) 5: δ t ← Decide ​ ( r t ) \delta_{t}\leftarrow\textsc{Decide}(r_{t}) 6: if δ t = Approve \delta_{t}=\textup{{Approve}} then 7: C t ′ ← C t C^{\prime}_{t}\leftarrow C_{t} 8: else if δ t = Mitigate \delta_{t}=\textup{{Mitigate}} then 9: C t ′ ← Sanitise ​ ( C t , trace t ) C^{\prime}_{t}\leftarrow\textsc{Sanitise}(C_{t},\mathrm{trace}_{t}) 10: else 11: C t ′ ← SafeResponse ​ ( ) C^{\prime}_{t}\leftarrow\textsc{SafeResponse}() ; terminate 12: end if 13: return ( δ t , Φ t , C t ′ ) (\delta_{t},\Phi_{t},C^{\prime}_{t})

[130] h2: Appendix C Complete Pipeline with MTA

[131] p: Algorithm 2 presents the end-to-end processing loop, detailing the integration of our evaluated instantiation (C1-C5) into the agentic RAG workflow.

[132] figure: Algorithm 2 Agentic RAG Pipeline with MTA Integration 1: Query q q , knowledge store 𝒦 \mathcal{K} , tools 𝒯 \mathcal{T} 2: Safe response r r or refusal 3: Φ 0 ← ∅ \Phi_{0}\leftarrow\varnothing 4: δ 1 , Φ 1 , q ′ ← MTA ​ ( q , Φ 0 ) \delta_{1},\Phi_{1},q^{\prime}\leftarrow\textsc{MTA}(q,\Phi_{0}) ⊳ \triangleright C1: Query 5: if δ 1 = Refuse \delta_{1}=\textup{{Refuse}} then 6: return Safe () 7: end if 8: a ← 𝒜 main . Plan ​ ( q ′ ) a\leftarrow\mathcal{A}_{\mathrm{main}}.\textsc{Plan}(q^{\prime}) 9: δ 2 , Φ 2 , a ′ ← MTA ​ ( a , Φ 1 ) \delta_{2},\Phi_{2},a^{\prime}\leftarrow\textsc{MTA}(a,\Phi_{1}) ⊳ \triangleright C2: Action 10: if δ 2 = Refuse \delta_{2}=\textup{{Refuse}} then 11: return Safe () 12: end if 13: D ← Execute ​ ( a ′ , 𝒦 , 𝒯 ) D\leftarrow\textsc{Execute}(a^{\prime},\mathcal{K},\mathcal{T}) 14: δ 3 , Φ 3 , D ′ ← MTA ​ ( D , Φ 2 ) \delta_{3},\Phi_{3},D^{\prime}\leftarrow\textsc{MTA}(D,\Phi_{2}) ⊳ \triangleright C3: Data 15: if δ 3 = Refuse \delta_{3}=\textup{{Refuse}} then 16: return Safe () 17: end if 18: Φ 4 ← Φ 3 \Phi_{4}\leftarrow\Phi_{3} 19: for all tool output t i ∈ D ′ t_{i}\in D^{\prime} do ⊳ \triangleright C4: Tools 20: δ 4 i , Φ 4 , t i ′ ← MTA ​ ( t i , Φ 4 ) \delta_{4}^{i},\Phi_{4},t^{\prime}_{i}\leftarrow\textsc{MTA}(t_{i},\Phi_{4}) 21: if δ 4 i = Refuse \delta_{4}^{i}=\textup{{Refuse}} then 22: return Safe () 23: end if 24: end for 25: r ← ℒ gen . Generate ​ ( q ′ , D ′ ) r\leftarrow\mathcal{L}_{\mathrm{gen}}.\textsc{Generate}(q^{\prime},D^{\prime}) 26: δ 5 , Φ 5 , r ′ ← MTA ​ ( r , Φ 4 ) \delta_{5},\Phi_{5},r^{\prime}\leftarrow\textsc{MTA}(r,\Phi_{4}) ⊳ \triangleright C5: Output 27: if δ 5 = Refuse \delta_{5}=\textup{{Refuse}} then 28: return Safe () 29: end if 30: return r ′ r^{\prime}

[133] h2: Appendix D Per-LLM Results on B1

[134] figure: LLM Backbone Base + MTA Red. GPT-4o 76.5 15.7 × 4.9\!\times GPT-4o-mini 78.4 31.5 × 2.5\!\times Llama-3.3-70B 70.9 7.5 × 9.5\!\times GPT-4.1 78.0 14.0 × 5.6\!\times Table 4: Per-LLM end-to-end ASR (%) and reduction factors for B1 (Text Poisoning), varying the protected backbone while keeping the trust layer fixed.

[135] h2: Appendix E ART-SafeBench Generation Framework

[136] p: ART-SafeBench is constructed via a closed-loop validated synthesis pipeline that produces adversarial instances together with explicit success predicates.

[137] h4: Four-stage summary.

[138] p: Given an attack goal g g (e.g., OWASP-aligned objective) and an attacker capability class (e.g., black-box prompting vs. partial-access poisoning), the pipeline: (1) Specifies a success predicate κ g \kappa_{g} that operationalises the violation of interest (harmful output, control subversion, exfiltration, or resource abuse); (2) Crafts an adversarial stimulus x x and (optionally) benign context μ \mu that realises the capability model; (3) Executes a reference unhardened agentic RAG pipeline on ( x , μ ) (x,\mu) to obtain an outcome trace y y (including intermediate tool and retrieval artifacts); and (4) Validates the instance by checking whether y y satisfies κ g \kappa_{g} , retaining only validated instances for which the reference system exhibits a violation under the chosen predicate.

[139] h4: Five-step instantiation.

[140] p: In our implementation, the pipeline is instantiated as: (i) Definition (sample ( g , Γ ) (g,\Gamma) and emit κ g \kappa_{g} ), (ii) Crafting (generate candidate x x compatible with Γ \Gamma ), (iii) Context generation (optionally generate μ \mu for realism), (iv) Simulator (run the reference system deterministically to obtain y y ), and (v) Judge (deterministically evaluate κ g ​ ( y ) \kappa_{g}(y) and accept only if successful). Empirically, the closed-loop acceptance rate is ∼ \sim 37%.

[141] h2: Appendix F ART-SafeBench Record Schema

[142] p: Each ART-SafeBench record follows a strict schema to ensure reproducibility: id (SHA-256 hash of provenance), benchmark (B1-B5), attack_goal (natural language description), attack_payload (the specific text/image/tool-call injection), benign_context (ground truth context), category (OWASP classification), and metadata (target model, random seed, timestamp). Records are stored in JSON Lines format.

[143] h2: Appendix G Extended OWASP Results

[144] figure: OWASP Category n n Base + MTA Prompt injection (LLM01) 1,477 64 8 Insecure output (LLM05) 716 71 < < 1 Sensitive info. (LLM02) 715 36 0 Supply chain (LLM03) 623 58 0 Misinfo./harmful (LLM09) 738 63 5 Model DoS (LLM10) 709 61 7 Table 5: Per-OWASP ASR (%) for B3 for the six instantiated categories ( n = 4,978 n\!=\!4{,}978 of 10,005). Information disclosure (LLM02) and supply-chain (LLM03) attacks are eliminated entirely.

[145] h2: Appendix H Proof Sketches

[146] h4: Proposition 1 .

[147] p: The weak inequality follows from set inclusion: Π Ω ⊂ Π Φ \Pi_{\Omega}\subset\Pi_{\Phi} . For strictness, partial observability induces aliasing: there exist histories h t , h t ′ h_{t},h^{\prime}_{t} with the same instantaneous observation o t o_{t} but different posteriors over 𝒮 adv \mathcal{S}_{\mathrm{adv}} . Any stateless policy must choose the same action on both h t h_{t} and h t ′ h^{\prime}_{t} , while a belief-conditioned policy can separate them via Φ t \Phi_{t} , yielding strictly higher expected value under J J in general.

[148] h4: Proposition 2 .

[149] p: (i) Under the stated condition, d ⁡ ( o t ) = d ⁡ ( o 1 ) d(o_{t})=d(o_{1}) for all t t , so D t = D 1 D_{t}=D_{1} deterministically and the union reduces to a single event. (ii) The belief state acts as an integrator: sub-threshold evidence at t t elevates Φ t \Phi_{t} , lowering the effective decision boundary at t + 1 t\!+\!1 and creating a monotone increase in P ⁡ ( D t + 1 = 1 ∣ ⋯ ) P(D_{t+1}\!=\!1\mid\cdots) beyond the memoryless baseline.

[150] h2: Appendix I Latency and Cost Analysis

[151] p: The MTA introduces 3.34 × 3.34\times latency overhead: mean end-to-end response time increases from 2.59 ± 0.77 2.59\pm 0.77 s to 8.64 ± 2.92 8.64\pm 2.92 s ( N = 100 N\!=\!100 NQ queries). Each defended query traverses up to K K checkpoint LLM calls in addition to the baseline generation call ( K = 5 K\!=\!5 in our evaluated instantiation), yielding an estimated ∼ \sim 3,500-5,000 additional input tokens and ∼ \sim 800-1,200 output tokens per query (from belief-state context, checkpoint prompts, and structured JSON responses). The overhead is dominated by the sequential dependency across checkpoints (C1-C5); the increased variance stems from the variable number and complexity of LLM calls conditioned on the input and evolving belief state. Unvalidated optimisation paths include checkpoint parallelisation (C3/C4 concurrent), adaptive activation (low-risk queries bypass intermediate checkpoints), and asymmetric model selection (smaller LLM for low-risk checkpoints). In security-sensitive deployments where the cost of a successful attack substantially exceeds latency cost, this overhead represents an acceptable trade-off.

[152] h2: Instructions for reporting errors

[153] p: We are continuing to improve HTML versions of papers, and your feedback helps enhance accessibility and mobile support. To report errors in the HTML that will help us improve conversion and rendering, choose any of the methods listed below:

[154] p: Tip: You can select the relevant text first, to include it in your report.

[155] p: Our team has already identified the following issues . We appreciate your time reviewing and reporting rendering errors we may not have found yet. Your efforts will help us improve the HTML versions for all readers, because disability should not be a barrier to accessing research. Thank you for your continued support in championing open access for all.

[156] p: Have a free development cycle? Help support accessibility at arXiv! Our collaborators at LaTeXML maintain a list of packages that need conversion , and welcome developer contributions .
