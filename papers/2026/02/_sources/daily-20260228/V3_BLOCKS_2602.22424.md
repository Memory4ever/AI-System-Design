[0] h5: Report GitHub Issue

[1] p: Content selection saved. Describe the issue below:

[2] h1: Causality ≠ \neq Invariance: Function and Concept Vectors in LLMs

[3] h6: Abstract

[4] p: Do large language models (LLMs) represent concepts abstractly, i.e., independent of input format? We revisit Function Vectors ( ℱ ​ 𝒱 \mathcal{FV} s), compact representations of in-context learning (ICL) tasks that causally drive task performance. Across multiple LLMs, we show that ℱ ​ 𝒱 \mathcal{FV} s are not fully invariant: ℱ ​ 𝒱 \mathcal{FV} s of the same concept are nearly orthogonal when extracted from different input formats (e.g., open-ended vs. multiple-choice). We identify Concept Vectors ( 𝒞 ​ 𝒱 \mathcal{CV} s), which carry more stable concept representations. Like ℱ ​ 𝒱 \mathcal{FV} s, 𝒞 ​ 𝒱 \mathcal{CV} s are composed of attention head outputs; however, unlike ℱ ​ 𝒱 \mathcal{FV} s, the constituent heads are selected using Representational Similarity Analysis (RSA) based on whether they encode concepts consistently across input formats. While these heads emerge in similar layers to ℱ ​ 𝒱 \mathcal{FV} -related heads, the two sets are largely distinct, suggesting different underlying mechanisms. Steering experiments reveal that ℱ ​ 𝒱 \mathcal{FV} s excel in-distribution, when extraction and application formats match (e.g., both open-ended in English), while 𝒞 ​ 𝒱 \mathcal{CV} s generalize better out-of-distribution across both question types (open-ended vs. multiple-choice) and languages. Our results show that LLMs do contain abstract concept representations, but these differ from those that drive ICL performance.

[5] p: University of Amsterdam

[6] figure: Figure 1: Function vs. Concept Vectors . Top : Similarity matrices for ℱ ​ 𝒱 \mathcal{FV} s (left) and 𝒞 ​ 𝒱 \mathcal{CV} s (right) in Llama 3.1 70B; cells show how similar two prompt representations are (warmer = more similar). Middle : Schematic highlighting the distinction between heads with causal effect (Activation Patching-selected) and heads that encode format-invariant structure (RSA-selected). Bottom : Example prompts for two concepts across three formats (EN open - ended, FR open - ended, multiple - choice). Takeaway : ℱ ​ 𝒱 \mathcal{FV} s cluster by input format; 𝒞 ​ 𝒱 \mathcal{CV} s cluster by concept across formats.

[7] h2: 1 Introduction

[8] p: Do large language models represent concepts abstractly, i.e., in a way that is stable across surface form? We focus on relational concepts : mappings between entities, such as linking a word to its antonym. Cognitive science has long argued that abstract representation of such structure underlies human generalization ( Gentner, 1983 ; Hofstadter, 1995 ; Mitchell, 2020 ) . This capability allows identifying, by analogy, that “hot → \rightarrow cold” and “big → \rightarrow small” share the same oppositional relation, independent of the specific words or how the task is presented. Recent work shows that LLMs exhibit representational structures similar to humans ( Pinier et al., 2025 ; Du et al., 2025 ; Doerig et al., 2025 ) , raising the question: do the abstract representations hypothesized to support analogical reasoning actually drive LLM performance on such tasks?

[9] p: We find that LLMs do contain abstract relational concept information, but the components that encode it differ from those that causally drive in - context learning (ICL) behavior. This separation challenges the single-circuit hypothesis that format - invariant representations are what primarily enable ICL.

[10] p: We revisit Function Vectors ( ℱ ​ 𝒱 \mathcal{FV} s)—compact vectors formed by summing outputs of a small set of attention heads that mediate ICL ( Todd et al., 2024 ; Hendel et al., 2023 ; Yin & Steinhardt, 2025 ) . Because ℱ ​ 𝒱 \mathcal{FV} s transfer across contexts (e.g., differently formatted prompts and natural text), they are often treated as encoding the underlying concept ( Zheng et al., 2024 ; Griffiths et al., 2025 ; Bakalova et al., 2025 ; Brumley et al., 2024 ; Fu, 2025 ) . We update this view: ℱ ​ 𝒱 \mathcal{FV} s are not fully invariant. For the same concept, ℱ ​ 𝒱 \mathcal{FV} s extracted from different input formats (open - ended vs. multiple - choice) are nearly orthogonal, indicating that ℱ ​ 𝒱 \mathcal{FV} s mix concept with format (§ 2.2.1 ).

[11] p: To isolate format - invariant structure, we contrast activation patching (AP), which localizes components with causal effects on outputs, with representational similarity analysis (RSA) ( Kriegeskorte, 2008 ) , which localizes components whose representations organize by concept independent of format. Using RSA to select heads and then summing their activations yields Concept Vectors ( 𝒞 ​ 𝒱 \mathcal{CV} s). Across seven relational concepts, three input formats (open - ended English, open - ended French, multiple - choice), and four models (Llama 3.1 8B/70B; Qwen 2.5 7B/72B), we find that 𝒞 ​ 𝒱 \mathcal{CV} heads arise in similar layers but are largely disjoint from ℱ ​ 𝒱 \mathcal{FV} heads, suggesting separable mechanisms for invariance vs. causality (§ 2.2.2 ).

[12] p: Finally, we test whether 𝒞 ​ 𝒱 \mathcal{CV} s can steer. In steering experiments, ℱ ​ 𝒱 \mathcal{FV} s produce larger in - distribution gains when extraction and application formats match (§ 3.2.1 ), whereas 𝒞 ​ 𝒱 \mathcal{CV} s generalize more consistently out - of - distribution across question type and language (§ 3.2.2 ) and produce fewer format artifacts (e.g., tokens and language from extraction prompts; § 3.2.3 ).

[13] p: Overall, our contributions are as follows:

[14] p: ℱ ​ 𝒱 \mathcal{FV} s are not input - invariant. They mix relational concepts with input format; same - concept ℱ ​ 𝒱 \mathcal{FV} s differ sharply across formats.

[15] p: RSA reveals 𝒞 ​ 𝒱 \mathcal{CV} heads. These heads encode relational concepts at a higher level of abstraction than ℱ ​ 𝒱 \mathcal{FV} heads. 1 1 1 We expand on what we mean by “higher level of abstraction” in the Discussion (§ 5 ).

[16] p: 𝒞 ​ 𝒱 \mathcal{CV} and ℱ ​ 𝒱 \mathcal{FV} heads are disjoint. ℱ ​ 𝒱 \mathcal{FV} s and 𝒞 ​ 𝒱 \mathcal{CV} s are realized by different attention heads, suggesting that abstract concept representations are distinct from the mechanisms that causally drive ICL performance.

[17] p: Steering trade - off. ℱ ​ 𝒱 \mathcal{FV} s steer more strongly in-distribution, while 𝒞 ​ 𝒱 \mathcal{CV} s generalize more consistently out-of-distribution, albeit with smaller absolute gains.

[18] h2: 2 In search of Invariance

[19] p: We test whether concept representations are stable across surface form, using AP (causal heads) and RSA (format - invariant heads) across models, datasets, and formats. We then form Function/Concept Vectors to compare clustering by format vs. concept; AP/RSA heads lie in similar layers but show minimal top - K overlap.

[20] h3: 2.1 Methods

[21] h4: 2.1.1 Models

[22] p: We test Llama 3.1 (8B, 70B) and Qwen 2.5 (7B, 72B) models ( Meta AI, 2024 ; Qwen et al., 2025 ) . All models are autoregressive, residual-based transformers ( Vaswani et al., 2023 ) . Each model, f f internally comprises of ℒ \mathcal{L} layers. Each layer is composed of a multi-layer perceptron (MLP) and J J attention heads a ℓ ​ j a_{\ell{j}} which together produce the vector representation of the last token of layer ℓ \ell , 𝐡 ℓ = 𝐡 ℓ − 1 + MLP ℓ + ∑ j ∈ J a ℓ ​ j \mathbf{h}_{\ell}=\mathbf{h}_{\ell-1}+\text{MLP}_{\ell}+\sum_{j\in{J}}a_{\ell{j}} ( Elhage et al., 2021 ) .

[23] h4: 2.1.2 Tasks

[24] p: Datasets We define a dataset as one concept expressed in one input format (e.g., Antonym in open-ended English). For each dataset we build a set of in-context prompts P d = { p d i } P_{d}=\{p_{d}^{i}\} where i i indexes individual prompts within dataset d d . Each prompt contains few-shot input–output examples ( x , y ) (x,y) that illustrate the same concept, followed by a query input x q i x_{q}^{i} whose target output y q i y_{q}^{i} is withheld. The input–output pairs ( x , y ) (x,y) were either sourced from prior work or generated using OpenAI’s GPT-4o (see Appendix D for details). Example prompts are provided in Appendix A .

[25] p: Concepts. We consider seven concepts:

[26] p: Antonym Map a word to one with opposite meaning (e.g., hot → \rightarrow cold).

[27] p: Categorical Map a word to its semantic category (e.g., apple → \rightarrow fruit).

[28] p: Causal Map a cause to an effect (e.g., rain → \rightarrow wet).

[29] p: Synonym Map a word to one with similar meaning (e.g., big → \rightarrow large).

[30] p: Translation Translate a word to another language (e.g., house → \rightarrow maison).

[31] p: Present–Past Convert a verb from present to past tense (e.g., run → \rightarrow ran).

[32] p: Singular–Plural Convert a noun from singular to plural (e.g., cat → \rightarrow cats).

[33] p: Input formats. We vary only the prompt’s surface format; the ( x , y ) (x,y) relation stays the same. Formats:

[34] p: Open-ended ICL in English ( OE-EN )

[35] p: Open-ended ICL in a different language (French or Spanish; OE-FR or OE-ES )

[36] p: Multiple-choice ICL in English ( MC )

[37] p: We use 5 - shot prompts for open - ended and 3 - shot for multiple - choice to reduce computational load given prompt length. Altogether, we have 21 datasets (7 concepts × \times 3 input formats). We build 50 prompts per dataset (total N = 1050 N=1050 prompts).

[38] h4: 2.1.3 Activation Patching

[39] p: Activation patching replaces specific activations with cached ones from a clean run to assess their impact on the model’s output. The cached activations are then inserted into selected model components in a corrupted run, where the systematic relationships in the prompt are disrupted. For example, in an antonym ICL task, consider a clean prompt : Hot → \rightarrow Cold , Big → \rightarrow Small , Clean → \rightarrow ? and a corrupted prompt : House → \rightarrow Cold, Eagle → \rightarrow Small, Clean → \rightarrow ? The goal of activation patching is then to localize model components that push the model to the correct answer, Dirty , on the corrupted prompt.

[40] p: We compute the causal indirect effect (CIE) for each attention head a ℓ ​ j a_{\ell{j}} as the difference between the probability of predicting the expected token y y when processing the corrupted prompt p ~ \tilde{p} with and without the transplanted mean activation 𝐚 ¯ ℓ ​ j \bar{\mathbf{a}}_{\ell{j}} from clean runs:

[41] table: CIE ​ ( a ℓ ​ j ) = f ⁡ ( p ~ ∣ 𝐚 ℓ ​ j := 𝐚 ¯ ℓ ​ j ) ​ [ y ] − f ⁡ ( p ~ ) ​ [ y ] \text{CIE}\big(a_{\ell{j}}\big)=f\Big(\tilde{p}\mid\mathbf{a}_{\ell{j}}:=\bar{\mathbf{a}}_{\ell{j}}\Big)[y]-f\big(\tilde{p}\big)[y] (1)

[42] p: We then compute the average indirect effect (AIE) over a collection 𝒟 \mathcal{D} of all datasets (§ 2.1.2 ). 2 2 2 Note : Unlike Todd et al. (2024) we compute AIE scores across all input formats, not OE-ENG only.

[43] table: AIE ​ ( a ℓ ​ j ) = 1 | 𝒟 | ​ ∑ d ∈ 𝒟 1 | 𝒫 ~ d | ​ ∑ p ~ i ∈ 𝒫 ~ d CIE ​ ( a ℓ ​ j ) \text{AIE}(a_{\ell{j}})=\frac{1}{|\mathcal{D}|}\sum_{d\in\mathcal{D}}\frac{1}{|\tilde{\mathcal{P}}_{d}|}\sum_{\tilde{p}_{i}\in\tilde{\mathcal{P}}_{d}}\text{CIE}\big(a_{\ell{j}}\big) (2)

[44] p: where 𝒫 ~ d \tilde{\mathcal{P}}_{d} denotes the set of corrupted prompts for dataset d d .

[45] figure: Figure 2: Representational Similarity Analysis (RSA) . For each attention head, we compute a representational similarity matrix (RSM) over prompts spanning concepts and input formats (cosine similarity of head outputs). We construct a binary design matrix that marks pairs sharing the same concept, independent of format. The RSA score for a head is Spearman’s ρ \rho between the lower - triangular entries of the RSM and the design matrix; higher ρ \rho indicates stronger concept - invariant encoding.

[46] figure: Figure 3: Similarity matrices . Full similarity matrices extracted from top K = 5 K=5 heads in 𝒞 ​ 𝒱 \mathcal{CV} s and ℱ ​ 𝒱 \mathcal{FV} s in Llama 3.1 70B for all concepts. See Appendix B for other models.

[47] h4: 2.1.4 Representational Similarity Analysis

[48] p: To find attention heads encoding concepts invariant to input formats, we employ representational similarity analysis (RSA; Kriegeskorte (2008) ).

[49] p: For each attention head a ℓ ​ j a_{\ell{j}} we compute representational similarity matrices (RSMs) where v i v_{i} denotes the output extracted from a ℓ ​ j a_{\ell{j}} for the i i th prompt p i ∈ P N p_{i}\in P_{N} , and θ ⁡ ( ⋅ , ⋅ ) \theta(\cdot,\cdot) is a cosine similarity function.

[50] table: RSM = [ 1 ⋯ θ ⁡ ( v 1 , v N ) ⋱ θ ⁡ ( v N , v 1 ) ⋯ 1 ] \text{RSM}=\begin{bmatrix}1&\cdots&\theta(v_{1},v_{N})\\ \vdots&\ddots&\vdots\\ \theta(v_{N},v_{1})&\cdots&1\end{bmatrix} (3)

[51] p: We then construct a binary design matrix, DM , where each entry is set to 1 if the corresponding pair of prompts share the same attribute value, and 0 otherwise. In this paper, we consider two attributes: (1) concept - does a pair of prompts illustrate the same concept, regardless of the input format? and (2) prompt_format - does a pair of prompts have the same question type (i.e. open-ended or multiple-choice)?

[52] p: We then quantify the alignment between the RSM and DM for the lower-triangles (since similarity matrices are symmetric) using the non-parametric Spearman’s rank correlation coefficient ( 𝝆 \boldsymbol{\rho} ).

[53] p: To localize attention heads carrying invariant concept information we compute the RSA for each attention head obtaining a single Concept RSA score for each attention head.

[54] table: Concept-RSA ​ ( a ℓ ​ j ) = ρ ⁡ ( RSM ℓ ​ j , Concept-DM ) \text{Concept-RSA}\big(a_{\ell{j}}\big)=\rho(\text{RSM}_{\ell{j}},\text{Concept-DM}) (4)

[55] h4: 2.1.5 Function & Concept Vectors

[56] p: To form Function/Concept Vectors we create sets of top K K ranking attention heads, 𝒜 ℱ ​ 𝒱 \mathcal{A}_{\mathcal{FV}} and 𝒜 𝒞 ​ 𝒱 \mathcal{A}_{\mathcal{CV}} , based on their AIE and RSA scores respectively. Function/Concept Vectors for prompt i i are then computed as the sum of activations for this prompt, 𝐚 ℓ ​ j i \mathbf{a}_{\ell{j}}^{i} , from the sets 𝒜 ℱ ​ 𝒱 \mathcal{A}_{\mathcal{FV}} and 𝒜 𝒞 ​ 𝒱 \mathcal{A}_{\mathcal{CV}} respectively.

[57] table: ℱ ​ 𝒱 i = ∑ a ℓ ​ j i ∈ 𝒜 ℱ ​ 𝒱 𝐚 ℓ ​ j i 𝒞 ​ 𝒱 i = ∑ a ℓ ​ j i ∈ 𝒜 𝒞 ​ 𝒱 𝐚 ℓ ​ j i \mathcal{FV}_{i}=\sum_{\mathclap{a_{\ell{j}}^{i}\in\mathcal{A}_{\mathcal{FV}}}}\mathbf{a}_{\ell{j}}^{i}\quad\mathcal{CV}_{i}=\sum_{\mathclap{a_{\ell{j}}^{i}\in\mathcal{A}_{\mathcal{CV}}}}\mathbf{a}_{\ell{j}}^{i} (5)

[58] figure: Figure 4: Concept vs. format RSA . Question type and Concept RSA scores for 𝒞 ​ 𝒱 \mathcal{CV} s and ℱ ​ 𝒱 \mathcal{FV} s in all models. Takeaway : 𝒞 ​ 𝒱 \mathcal{CV} s encode more concept information and less input format than ℱ ​ 𝒱 \mathcal{FV} s.

[59] h3: 2.2 Results

[60] h4: 2.2.1 Concept Vectors are More Invariant to Input Format

[61] p: We test invariance to input format by computing RSA with design matrices for concept and question type (following the setup in § 2.1.4 ). We form ℱ ​ 𝒱 \mathcal{FV} s/ 𝒞 ​ 𝒱 \mathcal{CV} s by summing the top- K K heads ranked by AIE/RSA (Eq. 5 ). Across models and K K , 𝒞 ​ 𝒱 \mathcal{CV} s show higher concept RSA and lower question-type RSA than ℱ ​ 𝒱 \mathcal{FV} s (Figure 4 ), indicating that ℱ ​ 𝒱 \mathcal{FV} s encode format more strongly while 𝒞 ​ 𝒱 \mathcal{CV} s track concept. Consistently, similarity matrices for Llama 3.1 70B cluster by concept across formats for 𝒞 ​ 𝒱 \mathcal{CV} s, but by format for ℱ ​ 𝒱 \mathcal{FV} s (Figure 3 ), where within-format type ℱ ​ 𝒱 \mathcal{FV} clusters are nearly identical with mean cosine similarity = 0.90 =0.90 . 𝒞 ​ 𝒱 \mathcal{CV} s nonetheless exhibit a weaker within-format type cluster (mean cosine similarity = 0.55 =0.55 ), suggesting they retain some low-level format information. Overall, however, 𝒞 ​ 𝒱 \mathcal{CV} s remain markedly more invariant to input format than ℱ ​ 𝒱 \mathcal{FV} s.

[62] figure: Model K=3 K=5 K=10 K=20 K=50 K=100 Llama-3.1 8B 0 0 1 1 𝟏𝟐 \mathbf{12} 𝟐𝟖 \mathbf{28} Llama-3.1 70B 0 0 0 0 1 𝟔 \mathbf{6} Qwen2.5 7B 0 0 0 𝟒 \mathbf{4} 𝟏𝟓 \mathbf{15} 𝟑𝟗 \mathbf{39} Qwen2.5 72B 0 0 0 1 𝟑 \mathbf{3} 𝟏𝟑 \mathbf{13} Table 1: RSA–AIE head overlap . Overlap between RSA and AIE heads (number of overlapping heads among top- K K ). Bold numbers indicate overlap significantly above chance ( p < 0.05 p<0.05 ; details in Appendix E ). Takeaway : ℱ ​ 𝒱 \mathcal{FV} s and 𝒞 ​ 𝒱 \mathcal{CV} s are composed of different attention heads.

[63] h4: 2.2.2 Function & Concept Vectors are Composed of Different Attention Heads

[64] p: If we compare which heads are selected by the two procedures, we see that ℱ ​ 𝒱 \mathcal{FV} s and 𝒞 ​ 𝒱 \mathcal{CV} s are composed of different attention heads. First, we ranked each head for each method, i.e., AIE (§ 2.1.3 ) for ℱ ​ 𝒱 \mathcal{FV} s and by Concept-RSA (§ 2.1.4 ) for 𝒞 ​ 𝒱 \mathcal{CV} s. Then we examined depth and top- K K overlap. Layer-averaged scores show similar layer profiles (Figure 5 ), but head identities barely overlap: for K ≤ 20 K\leq 20 the intersection is near zero and stays small at larger K K (Table 1 ). We also note that AIE scores are highly sparse: their histogram peaks at zero with a long right tail (Figure 12 )—so only a few heads have measurable causal effect. Together this supports that AIE-selected causal heads are largely distinct from the invariant , RSA-selected heads.

[65] p: To ensure this separation is not an artifact of patching within the same format, we also performed cross-format activation patching (e.g., extracting activations from open-ended prompts and patching them into multiple-choice). This procedure continued to identify the same FV heads and did not identify CV heads (see Appendix O ), confirming that FVs are the primary causal drivers regardless of input format.

[66] figure: Figure 5: Layer - wise AIE vs. RSA . AIE and RSA scores averaged across all heads per layer. Takeaway : ℱ ​ 𝒱 \mathcal{FV} and 𝒞 ​ 𝒱 \mathcal{CV} heads are in similar layers.

[67] h2: 3 Can Concept Vectors Steer?

[68] p: We now test whether these invariant heads can steer: we introduce how we construct vectors, the AmbiguousICL setup with conflicting cues, and the intervention protocol. ℱ ​ 𝒱 \mathcal{FV} s win in - distribution; 𝒞 ​ 𝒱 \mathcal{CV} s transfer better out - of - distribution with fewer format artifacts, at a cost of smaller gains.

[69] figure: Figure 6: Overview of steering results . Top : We extract 𝒞 ​ 𝒱 \mathcal{CV} s and ℱ ​ 𝒱 \mathcal{FV} s from antonym ICL prompts in formats that are in - distribution (ID; OE - ENG ) or out - of - distribution (OOD; OE - FR , MC ) relative to the AmbiguousICL task (bottom - left). Bottom - left : We interleave two concepts— antonym and EN→FR translation —within one prompt; the model’s original prediction is the French translation. Bottom - right : Predictions after steering. Takeaways : (1) ℱ ​ 𝒱 \mathcal{FV} s yield larger ID gains. (2) 𝒞 ​ 𝒱 \mathcal{CV} s show more stable OOD effects across formats. (3) ℱ ​ 𝒱 \mathcal{FV} s can conflate concept with input format (e.g., French version of antonym and multiple - choice formatting).

[70] h3: 3.1 Steering Methods

[71] p: Steering Vectors Construction. For each concept and input format ( OE-ENG , OE-FR , MC ), we compute for every selected head a ℓ ​ j a_{\ell j} the mean last-token activation across the 50 extraction prompts of that concept–format. We then form one vector per format by summing these mean activations over the top- K K heads selected for 𝒞 ​ 𝒱 \mathcal{CV} or ℱ ​ 𝒱 \mathcal{FV} (as in Eq. 5 , but using per-format means in place of per-prompt activations). This yields one ID vector ( OE-ENG ) and two OOD vectors ( OE-FR , MC ) per concept.

[72] p: AmbiguousICL Task. We evaluate on AmbiguousICL tasks (Figure 6 ): each prompt interleaves two concepts (3 then 2 exemplars) followed by a query. The second concept is always English→French translation. Unsteered models tend to continue with the second concept; we aim to steer toward the first. Note that steering prompts are distinct from the extraction prompts used to construct the vectors. This setup is diagnostic: it tests whether representations encode abstract relational structure independent of extraction prompts’ surface format. To perform well in this setup requires consistency between ID and OOD performance.

[73] p: Steering with 𝒞 ​ 𝒱 \mathcal{CV} s and ℱ ​ 𝒱 \mathcal{FV} s. We add a vector 𝐯 \mathbf{v} to the last - token residual stream at a chosen layer:

[74] table: 𝐡 ℓ ← 𝐡 ℓ + α ​ 𝐯 \mathbf{h}_{\ell}\leftarrow\mathbf{h}_{\ell}+\alpha\mathbf{v} (6)

[75] p: We measure effectiveness as Δ ​ P = P after ​ ( y ) − P before ​ ( y ) \Delta P=P_{\text{after}}(y)-P_{\text{before}}(y) , averaged over 100 prompts per concept (see Figure 22 for Top-1 accuracy). We sweep α \alpha and K K and report the best per model (Appendix F ).

[76] figure: Figure 7: Steering effect across layers . We inject 𝒞 ​ 𝒱 \mathcal{CV} s and ℱ ​ 𝒱 \mathcal{FV} s into Llama - 3.1 - 70B and plot the change in target - token probability ( Δ ​ P \Delta P ) for four representative concepts (columns). Curves compare ID extraction format with OOD formats relative to the AmbiguousICL task (Figure 6 ). Higher Δ ​ P \Delta P means the model assigns more probability to the expected token than the unsteered model. Takeaways : (1) ℱ ​ 𝒱 \mathcal{FV} s typically achieve larger ID gains but often drop OOD. (2) 𝒞 ​ 𝒱 \mathcal{CV} s yield smaller gains yet show more stable OOD behavior across formats. See Figure 16 for other concepts/models.

[77] h3: 3.2 Steering Results

[78] h4: 3.2.1 Function Vectors Outperform Concept Vectors in Distribution

[79] p: Extracted from OE - ENG (ID setting), ℱ ​ 𝒱 \mathcal{FV} s yield the largest gains on ambiguous prompts (Figure 7 ). 𝒞 ​ 𝒱 \mathcal{CV} s also help but with smaller Δ ​ P \Delta P and minimal zeroshot effect (Figure 17 ). At the token level both vectors lift plausible English antonyms in the ID case (Table 2 ).

[80] figure: Query: salty → \rightarrow + Antonym Top Δ \Delta Tokens ℱ ​ 𝒱 \mathcal{FV} OE-ENG _sweet (+56%), _fresh (+16%), _bland (+6%), _taste (+3%), _uns (+2%) OE-FR _su (+31%), _dou (+27%), _frais (+5%), _fade (+5%), _ins (+3%) MC _( (+53%), _A (+1%), _\n (+1%), _space (+0%), _) (+0%) 𝒞 ​ 𝒱 \mathcal{CV} OE-ENG _sweet (+49%), _fresh (+8%), _bland (+3%), _taste (+3%), _uns (+3%) OE-FR _sweet (+54%), _fresh (+9%), _bland (+3%), _uns (+3%), _taste (+2%) MC _sweet (+35%), _fresh (+12%), _bland (+4%), _uns (+3%), _taste (+3%) Table 2: Token - level steering effects . Top tokens with largest probability gains when injecting 𝒞 ​ 𝒱 \mathcal{CV} s or ℱ ​ 𝒱 \mathcal{FV} s into Llama - 3.1 - 70B on the AmbiguousICL prompt (query shown above). Results shown at the layer with the strongest in - distribution effect per vector. Without intervention, the model predicts French translation _sa (from salé ) with 49%; antonym _sweet has 2%. English antonyms in red , French in blue , and the opening bracket (MC token) in green .

[81] h4: 3.2.2 Concept Vectors Are More Stable Out of Distribution

[82] p: Performance gains ( Δ ​ P \Delta P ). Out of distribution (extracting vectors from OE-FR or MC ), 𝒞 ​ 𝒱 \mathcal{CV} s more often maintain positive effects across formats, whereas ℱ ​ 𝒱 \mathcal{FV} s frequently degrade—especially for MC —and only occasionally stay consistent for specific concepts/models (Figs. 7 , 16 ). 𝒞 ​ 𝒱 \mathcal{CV} s raise the probability of the correct English answer across formats, and their top- Δ \Delta tokens remain concept-aligned (Table 2 ). Crucially, the key finding is not absolute performance but consistency: 𝒞 ​ 𝒱 \mathcal{CV} s increase the probability of producing similar concept-aligned tokens regardless of extraction format.

[83] p: Distributional consistency (KL). To quantify consistency across formats independent of absolute gains, we compare the model’s next-token distributions after steering with ID and OOD vectors. For each concept and vector type, we select the top 5 layers that achieve the highest ID Δ ​ P \Delta P . At each selected layer we compute KL divergence

[84] table: D K ​ L [ p ( 𝐱 | 𝐯 OOD ) ∥ p ( 𝐱 | 𝐯 ID ) ] D_{KL}\big[p(\mathbf{x}\,|\,\mathbf{v}_{\text{OOD}})\,\|\,p(\mathbf{x}\,|\,\mathbf{v}_{\text{ID}})\big]

[85] p: between the post-intervention distributions at the query token, where lower values indicate more similar effects of ID and OOD vectors. We average this KL divergence over prompts and selected layers to obtain one score per concept, and then summarize per model (Figure 8 ). Across models, 𝒞 ​ 𝒱 \mathcal{CV} s yield lower KL than ℱ ​ 𝒱 \mathcal{FV} s. The CV–FV KL gap is larger for MC than for OE-FR .

[86] h4: 3.2.3 Function Vectors Mix Concept with Input Format

[87] p: Out of distribution, ℱ ​ 𝒱 \mathcal{FV} s reflect both prompt format and concept. When vectors are extracted from OE - FR , they push the model toward the French translation of the concept (e.g., French antonyms), and when extracted from MC , they increase the probability of format tokens such as the opening bracket (Table 2 ). We quantify the language effect by measuring Δ ​ P \Delta P for the French translation across concepts (Figure 13 ). In the larger models, ℱ ​ 𝒱 \mathcal{FV} s substantially increase the probability of the French token, whereas 𝒞 ​ 𝒱 \mathcal{CV} s remain near zero; in smaller models the effect is negligible. Notably, ℱ ​ 𝒱 \mathcal{FV} s extracted from open - ended Spanish prompts induce almost the same bias toward the French translation as ℱ ​ 𝒱 \mathcal{FV} s extracted from French prompts (Figure 14 ), even though the AmbiguousICL alternatives are French only. This pattern suggests that ℱ ​ 𝒱 \mathcal{FV} s capture a generic translation/foreign - language signal tied to the extraction format rather than language - specific content. Combined with the MC bracket effect (Figure 15 ), these findings indicate that ℱ ​ 𝒱 \mathcal{FV} s mix concept with surface format, while 𝒞 ​ 𝒱 \mathcal{CV} s are comparatively format - invariant.

[88] figure: Figure 8: Consistency of steering effects . KL divergence between the probability distributions after the models were steered with an ID (OE-ENG) and OOD vectors (OE-FR [top], MC [bottom]). Lower values indicate more similar effects of ID and OOD vectors. Takeaway : 𝒞 ​ 𝒱 \mathcal{CV} s steer the models more consistently than ℱ ​ 𝒱 \mathcal{FV} s.

[89] h2: 4 Related Work

[90] p: Attention Head Categorization. Recent work has made significant progress in characterizing specialized attention heads that process in-context learning (ICL) tasks. For instance, Olsson et al. (2022) identified induction-heads, which Yin & Steinhardt (2025) found can develop into ℱ ​ 𝒱 \mathcal{FV} -heads during training. Other specialized head types include semantic-induction heads ( Ren et al., 2024 ) , symbol-abstraction heads ( Yang et al., 2025 ) , and various others ( Zheng et al., 2024 ) . Our work extends this line of research by identifying 𝒞 ​ 𝒱 \mathcal{CV} heads, attention heads that invariantly represent concepts in ICL tasks at high levels of abstraction.

[91] p: Linear Representation of Concepts. A substantial body of research has established that concepts are represented linearly in LLMs’ representational space ( Mikolov et al., 2013 ; Arora et al., 2016 ; Elhage et al., 2022 ) . This phenomenon, often termed the "Linear Representation Hypothesis" ( Park et al., 2024 ) , has been extensively studied across various tasks and domains. Hernandez et al. (2024) demonstrated that relational concepts—similar to those we study in this paper—can be decoded from LLM activations using linear approximation. Subsequent work by Merullo et al. (2025) revealed that the success of such decoding depends on the frequency of concepts in the pretraining corpora, which may explain why some concepts are represented more consistently than others in our study. Our findings contribute to this literature in two ways: (1) providing further support for the Linear Representation Hypothesis, and (2) extending previous work on relational concept representations by localizing specific attention heads that carry such representations and demonstrating their invariance to input formats.

[92] p: Symbolic-like reasoning in LLMs. Recent work has demonstrated that LLMs can exhibit symbol-like representational properties even without explicit symbolic architecture ( Feng & Steinhardt, 2024 ; Yang et al., 2025 ; Griffiths et al., 2025 ) . Yang et al. (2025) define symbolic processing as requiring two key properties: (1) invariance to content variations, and (2) indirection through pointers rather than direct content storage. Our 𝒞 ​ 𝒱 \mathcal{CV} s exhibit both properties: they are invariant to input format changes and function as pointers to content stored elsewhere, unlike ℱ ​ 𝒱 \mathcal{FV} s which directly store content (§ 3.2.3 ).

[93] h2: 5 Discussion

[94] p: Our results separate two representational roles in LLMs: components that cause strong ICL performance and components that encode abstract concept structure. Function Vectors ( ℱ ​ 𝒱 \mathcal{FV} s) occupy the first role, steering models effectively when extraction and application formats match, but deteriorating out of distribution (formats/languages). Conversely, Concept Vectors ( 𝒞 ​ 𝒱 \mathcal{CV} s) built from RSA - selected heads encode concepts at a higher level of abstraction and generalize more robustly across languages and question types, albeit with smaller causal effects. This supports a view that invariance and causality are mediated by largely distinct mechanisms in similar layers.

[95] p: Layers of abstraction. We define abstraction as encoding relational structure (e.g., “antonym”) while discarding surface details (e.g., “English, multiple-choice”). Our results suggest ℱ ​ 𝒱 \mathcal{FV} s do capture abstract task information: they reliably encode concepts within a format (Figure 19 ) and are causally effective even across formats (Appendix O ). However, their orthogonality across formats and retention of surface signals (e.g., MC brackets) reveal that they conflate this abstract content with surface form. In contrast, 𝒞 ​ 𝒱 \mathcal{CV} s cluster by concept regardless of format. Thus, ℱ ​ 𝒱 \mathcal{FV} s operate at a lower level of abstraction (“antonym in MC format”), while 𝒞 ​ 𝒱 \mathcal{CV} s operate at a higher level (“antonym”), independent of surface form.

[96] p: Relation to Function Vectors. Prior work shows that ℱ ​ 𝒱 \mathcal{FV} s compactly mediate ICL and can transfer across contexts ( Todd et al., 2024 ) . We refine this: ℱ ​ 𝒱 \mathcal{FV} portability is strong within families of prompts, but is not fully invariant to surface format. Same - concept ℱ ​ 𝒱 \mathcal{FV} s extracted from different formats are nearly orthogonal and can carry language/format signals (e.g., French subword or multiple - choice bracket tokens), while 𝒞 ​ 𝒱 \mathcal{CV} s track concept across formats with less surface content. This distinction can be framed as equivariance vs. invariance : ℱ ​ 𝒱 \mathcal{FV} s adapt to extraction format (e.g., producing French antonyms from French prompts, MC formatting tokens from MC prompts), whereas 𝒞 ​ 𝒱 \mathcal{CV} s steer toward similar outputs regardless of format. Finally, we do not propose 𝒞 ​ 𝒱 \mathcal{CV} s as competitors to ℱ ​ 𝒱 \mathcal{FV} s, but rather highlight a mechanistic dissociation: ℱ ​ 𝒱 \mathcal{FV} s drive behavior (causality) while 𝒞 ​ 𝒱 \mathcal{CV} s represent abstract structure (invariance).

[97] p: These findings have implications for theoretical models of ICL, such as recent work by Bu et al. (2025) which posits the retrieval of a single function vector a f a^{f} for a function f f . Our results suggest this model is incomplete: given the orthogonality of ℱ ​ 𝒱 \mathcal{FV} s across formats, the function vector is better conceptualized as format-conditional a ⁡ ( f , ϕ ) a(f,\phi) , implying convergence to multiple format-specific basins rather than a single global minimum. Furthermore, we find that ℱ ​ 𝒱 \mathcal{FV} s and 𝒞 ​ 𝒱 \mathcal{CV} s are orthogonal (even within the same format) which suggests that task representations partition into distinct abstract and format-specific subspaces, rather than residing in a single unified space.

[98] p: Implications for steering and interpretability. The dissociation between ℱ ​ 𝒱 \mathcal{FV} s and 𝒞 ​ 𝒱 \mathcal{CV} s suggests a practical trade - off. For maximal in - distribution control , ℱ ​ 𝒱 \mathcal{FV} s are preferable. For robust out - of - distribution control or probing abstract knowledge, 𝒞 ​ 𝒱 \mathcal{CV} s are more reliable.

[99] p: However, 𝒞 ​ 𝒱 \mathcal{CV} s appear to require the concept to be already present in the prompt to exert influence. In zero-shot steering (Figure 17 ) and activation patching—which require inducing or restoring a task "from scratch"— 𝒞 ​ 𝒱 \mathcal{CV} s are ineffective. In contrast, in AmbiguousICL, where the concept is present but competing, 𝒞 ​ 𝒱 \mathcal{CV} s successfully steer by amplifying the existing abstract signal. Thus, ℱ ​ 𝒱 \mathcal{FV} s seem necessary to instantiate a task, while 𝒞 ​ 𝒱 \mathcal{CV} s can modulate it once present.

[100] p: Methodologically, AP identifies what causally drives behavior, while RSA reveals how representations organize by concept. This distinction highlights that behavioral control and abstract representation can be mediated by different mechanisms.

[101] p: Analogies and abstract representation. Hill et al. (2019) propose that "analogies are something like the functions of the mind": concepts achieve their flexibility by being represented abstractly enough to permit context-dependent adaptation across diverse domains of application. This view predicts that relational concepts like antonym or causation should function identically whether presented as open-ended prompts, multiple-choice questions, or in different languages. Our findings offer a mechanistic refinement: while LLMs do form abstract relational representations ( 𝒞 ​ 𝒱 \mathcal{CV} s), these are largely distinct from the components that causally drive ICL behavior ( ℱ ​ 𝒱 \mathcal{FV} s). This dissociation suggests that analogical task performance may not require—or primarily rely on—the most abstract conceptual representations. Instead, LLMs appear to solve ICL tasks via more format-specific mechanisms, even though they do form abstract representations.

[102] p: Limitations and Future Directions. Our 𝒞 ​ 𝒱 \mathcal{CV} head selection targeted heads that encode all concepts simultaneously; this global criterion may miss concept - specific heads, which a per - concept RSA could reveal. We also did not probe how ℱ ​ 𝒱 \mathcal{FV} s and 𝒞 ​ 𝒱 \mathcal{CV} s emerge during model training or how they interact during inference.

[103] p: We propose two possible hypotheses that could be explored in future work:

[104] p: 1. CVs and FVs interact during inference as detection/execution mechanisms. Previous work by Lindsey et al. (2025) has discovered model features that seem to fire just before the model produces a certain type of output (e.g., a "capital" feature that fires just before the model outputs a name of a capital), and ones that fire more generally when the text mentions different capitals. Other work found that ICL tasks can be understood from an "encoder/decoder" perspective ( Han et al., 2025 ) , where the encoder encodes the task into a latent space and the decoder decodes the latent space into the output. Both of these findings suggest that models separate the task encoding and execution into distinct mechanisms which can be linked to 𝒞 ​ 𝒱 \mathcal{CV} s (encoding/detection) and ℱ ​ 𝒱 \mathcal{FV} s (execution).

[105] p: 2. CVs and FVs do not interact during inference; CVs are simply a backup circuit. Another possibility is that the two mechanisms are independent. Other works have found backup circuits where models can form multiple, partially redundant circuits and compensatory self - repair under ablations ( McGrath et al., 2023 ; Wang et al., 2022 ) . Given that a) both sets of heads are in similar layers (Figure 5 ), suggesting 𝒞 ​ 𝒱 \mathcal{CV} s and ℱ ​ 𝒱 \mathcal{FV} s may operate in parallel or via lateral information flow within the residual stream, rather than strict deep-hierarchical dependencies and b) that 𝒞 ​ 𝒱 \mathcal{CV} heads do not seem to have causal effects in usual ICL tasks (since they were not identified by AP), this hypothesis is also plausible. What is more Davidson et al. (2025) found that different prompting methods yield a different causal tasks representations, therefore it is possible that ICL in LLMs consist of multiple, separate mechanisms.

[106] h2: 6 Acknowledgments

[107] p: This research was funded by the the Dutch Research Council (NWO) project ”Learning to solve analogies: Why do children excel where AI models fail?” with project number 406.22.GO.029 awarded to Claire Stevenson.

[108] p: This work used the Dutch national e-infrastructure with the support of the SURF Cooperative using grant no. EINF-16229.

[109] p: We acknowledge NWO (Netherlands) for awarding this project access to the LUMI supercomputer, owned by the EuroHPC Joint Undertaking, hosted by CSC (Finland) and the LUMI consortium through the ‘Computing Time on National Computer Facilities’ call.

[110] h2: References

[111] h2: Appendix A Prompt Examples

[112] h3: A.1 Open - ended (5 - shot)

[113] h3: A.2 Multiple - choice (3 - shot)

[114] h2: Appendix B Similarity Matrices for Other Models

[115] figure: Figure 9: Similarity matrices extracted from top K = 1 K=1 heads in 𝒞 ​ 𝒱 \mathcal{CV} s and ℱ ​ 𝒱 \mathcal{FV} s in Llama 3.1 8B.

[116] figure: Figure 10: Similarity matrices extracted from top K = 1 K=1 heads in 𝒞 ​ 𝒱 \mathcal{CV} s and ℱ ​ 𝒱 \mathcal{FV} s in Qwen 2.5 7B.

[117] figure: Figure 11: Similarity matrices extracted from top K = 2 K=2 heads in 𝒞 ​ 𝒱 \mathcal{CV} s and ℱ ​ 𝒱 \mathcal{FV} s in Qwen 2.5 72B.

[118] h2: Appendix C AIE Scores

[119] figure: Figure 12: Histogram of AIE scores for Llama 3.1 8B, 70B, Qwen 2.5 7B, and Qwen 2.5 72B. Note, the y-axis is on a log-scale. Takeaway : AIE scores are highly sparse.

[120] h2: Appendix D Data Generation Process

[121] p: Concept sourcing : For most concepts (antonym, synonym, translation, present–past, singular–plural), we sourced word pairs from the datasets used by Todd et al. (2024) . For categorical and causal concepts, we generated word pairs using OpenAI’s GPT-4o model ( OpenAI, 2024 ) .

[122] p: Translation generation : French and Spanish translations were created using DeepL’s translation service ( DeepL SE, 2025 ) to ensure high-quality, contextually appropriate translations.

[123] p: Generated concepts (categorical and causal) : We prompted GPT-4o to generate exemplar:category pairs (e.g., “apple:fruit”, “blue:colour”) and cause:effect pairs (e.g., “stumble:fall”, “storm:flood”). The model was given examples of the desired format and asked to produce 100 pairs per batch. We generated pairs in batches of 100 until reaching approximately 1000 examples per concept, with retry mechanisms to ensure sufficient coverage. The final datasets were saved as JSON files containing input-output pairs.

[124] p: Quality filtering : Generated pairs underwent several filtering steps: (1) removal of duplicates based on input words, (2) exclusion of pairs containing underscores or numbers, (3) restriction to single words or two-word phrases (maximum one space per input/output), and (4) conversion to lowercase for consistency.

[125] p: Multiple choice format : For multiple choice prompts, we generated four options per question by randomly sampling three additional outputs from the same concept dataset, ensuring all four options were unique. The correct answer was randomly positioned among the four options.

[126] h2: Appendix E Significance Test for RSA–AIE Head Overlap

[127] p: We assess whether the observed overlap between the top- K K heads selected by Concept-RSA and by AIE is larger than expected by chance under a simple null model. Let N N denote the total number of attention heads in the model (layers × \times heads per layer). For a fixed K K , each method selects a size- K K subset of heads. Under the null hypothesis that these two subsets are independent, uniformly random size- K K subsets of { 1 , … , N } \{1,\dots,N\} , the overlap size

[128] table: X = | S RSA , K ∩ S AIE , K | X=\lvert S_{\text{RSA},K}\cap S_{\text{AIE},K}\rvert

[129] p: follows a hypergeometric distribution X ∼ Hypergeom ⁡ ( N , K , K ) X\sim\mathrm{Hypergeom}(N,K,K) .

[130] p: For an observed intersection x x , we report the one-sided tail probability

[131] table: p ≥ x = Pr [ X ≥ x ] = ∑ t = x K ( K t ) ​ ( N − K K − t ) ( N K ) . p_{\geq x}=\Pr\big[X\geq x\big]=\sum_{t=x}^{K}\frac{\binom{K}{t}\,\binom{N-K}{K-t}}{\binom{N}{K}}\,.

[132] p: Entries with p ≥ x < 0.05 p_{\geq x}<0.05 are typeset in bold in Table 1 .

[133] h2: Appendix F Steering Hyperparameters

[134] p: To optimize the intervention performance, we conduct a hyperparameter search for two parameters:

[135] p: α \alpha : the steering weight that controls the strength of the intervention

[136] p: K K : the number of attention heads to extract for concept vector computation

[137] p: We evaluate the following parameter ranges:

[138] p: K ∈ { 1 , 3 , 5 , 10 , 20 , 50 } K\in\{1,3,5,10,20,50\} for the number of heads

[139] p: α ∈ { 1 , 3 , 5 , 10 , 15 } \alpha\in\{1,3,5,10,15\} for the steering weight

[140] p: The hyperparameter optimization is performed separately for each model using antonym prompts. We select the parameter combination that maximizes the average steering effect across all input formats. This ensures that our chosen hyperparameters generalize well across different prompt structures. We report the best hyperparameters for each model in Table 3 .

[141] figure: Model Best K K Best α \alpha Llama 3.1 8B 1 10 Llama 3.1 70B 5 10 Qwen 2.5 7B 3 10 Qwen 2.5 72B 5 15 Table 3: Optimal hyperparameters for steering interventions across different models. K K represents the number of attention heads used for ℱ ​ 𝒱 \mathcal{FV} / 𝒞 ​ 𝒱 \mathcal{CV} extraction, while α \alpha controls the intervention strength.

[142] h2: Appendix G Input Format Mixing in Function Vectors

[143] figure: Figure 13: Δ \Delta P for French translations of all the concepts. ℱ ​ 𝒱 \mathcal{FV} s and 𝒞 ​ 𝒱 \mathcal{CV} s are extracted from open-ended French prompts.

[144] figure: Figure 14: Δ \Delta P for French translations of all the concepts. ℱ ​ 𝒱 \mathcal{FV} s and 𝒞 ​ 𝒱 \mathcal{CV} s are extracted from open-ended Spanish prompts.

[145] figure: Figure 15: Δ \Delta P for the opening bracket token _( . ℱ ​ 𝒱 \mathcal{FV} s and 𝒞 ​ 𝒱 \mathcal{CV} s are extracted from multiple-choice prompts.

[146] h2: Appendix H Steering Results

[147] figure: (a) Llama 3.1 8B (b) Llama 3.1 70B (c) Qwen 2.5 7B (d) Qwen 2.5 72B Figure 16: Steering effect across layers and all concepts for different models.

[148] h2: Appendix I 0-shot Steering Results

[149] figure: (a) Llama 3.1 8B (b) Llama 3.1 70B (c) Qwen 2.5 7B (d) Qwen 2.5 72B Figure 17: 0-shot steering effect across layers and all concepts for different models.

[150] h2: Appendix J Qwen 2.5 72B Outlier Analysis

[151] p: We identified anomalous CIE values for Qwen 2.5 72B in the Categorical concept across French open-ended and multiple-choice formats. As shown in Figure 18 , these conditions exhibit unusually high CIE values with a bimodal distribution that deviates from the expected pattern. We excluded these two datasets from the final AIE calculations. This exclusion has minimal impact on our results: the top-5 head rankings remain identical (100% overlap), confirming that our main findings are robust to this methodological decision.

[152] figure: Figure 18: Violin plots of CIE for different concepts and prompts.

[153] h2: Appendix K Disentangling Format-Specific and Abstract Representations in Function Vectors

[154] p: Multiple-choice (MC) format involves distinct computational steps beyond open-ended generation: evaluating options, comparing candidates, and selecting among labeled alternatives ( Tulchinskii et al., 2024 ; Wiegreffe et al., 2025 ) . When FV heads are extracted from MC prompts, they must therefore capture both (a) the task representation (e.g., antonym, causation) and (b) the MC-specific formatting demands. We test whether partitioning out of the MC information, makes the task representation abstract, i.e., is shared across all formats?

[155] p: We partition FV heads in Llama 3.1 70B into three subsets:

[156] p: All Heads : Top-5 heads identified by AIE computed over all input formats (standard FV selection, Eq. 5 )

[157] p: Common Heads : Heads that appear in the top-10 heads for all three input formats independently. (3 heads).

[158] p: Unique MC Heads : Heads that appear in the top-10 heads for MC format only. (6 heads)

[159] p: If abstract task representations exist in FVs independent of format, we would expect them to reside primarily in the common heads that are causally important across all formats. We then computed similarity matrices and RSA scores for each head subset.

[160] p: We see that within the MC format, common heads cluster by concept (Figure 19 ), but the representations are nearly orthogonal between open-ended and multiple-choice prompts for the same concept (Figure 20 ).

[161] p: It is still possible that these heads could encode both abstract task in open-ended and format features in MC prompts in superposition. However, under the Linear Representation Hypothesis ( Park et al., 2024 ) , a shared abstract concept should occupy a consistent linear subspace detectable via cosine similarity. The observed orthogonality across formats implies that any abstract representation is not linearly accessible in a format-invariant way. This suggests that FVs encode tasks at a lower level of abstraction (i.e., ’antonym in MC format’) rather than a shared, format-independent concept.

[162] figure: Figure 19: Similarity matrices for MC prompts only . Each panel shows the similarity matrix for a different subset of AIE-selected heads computed over MC prompts only (7 concepts × \times 50 prompts each). Common heads show stronger concept clustering than unique MC heads (albeit with large similarity between concepts due to the shared MC structure). Full FVs show a very similar representational structure to the common heads. Model: Llama 3.1 70B.

[163] figure: Figure 20: Similarity matrices for different FV head subsets across all formats . Same as Figure 19 but computed over all input formats (7 concepts × \times 3 formats × \times 50 prompts). Within the same concept the representations are nearly orthogonal between open-ended and multiple-choice prompts. Model: Llama 3.1 70B.

[164] h2: Appendix L Steering Results (Accuracy)

[165] figure: Figure 21: Steering effect across layers (Accuracy) . We inject 𝒞 ​ 𝒱 \mathcal{CV} s and ℱ ​ 𝒱 \mathcal{FV} s into Llama - 3.1 - 70B and plot the Top-1 accuracy for four representative concepts (columns). The grey horizontal line indicates the accuracy of the unsteered model. See Figure 7 for Δ ​ P \Delta P results.

[166] h2: Appendix M Multiple-choice Format with Words as Output

[167] p: Example prompt:

[168] figure: Figure 22: Similarity matrices for ℱ ​ 𝒱 \mathcal{FV} s and 𝒞 ​ 𝒱 \mathcal{CV} s with the inclusion of MC prompts where the model is expected to produce a word instead of a letter. Takeaway : Unlike 𝒞 ​ 𝒱 \mathcal{CV} s, ℱ ​ 𝒱 \mathcal{FV} MC representations still cluster due to the input format, therefore MC cluster effect is not due to the model producing words/letters. Model: Llama 3.1 70B.

[169] h2: Appendix N AmbiguousICL in Different Languages

[170] p: In the original AmbiguousICL implementation, the concepts are presented in English and the translations are presented in French.

[171] p: Here, we test the effect of presenting the concepts in a different language to determine if 𝒞 ​ 𝒱 \mathcal{CV} s are tied to a specific surface form (e.g., “English Antonym”). Specifically, we present the concepts in Spanish and interleave them with Spanish-to-English translations.

[172] p: Example antonym prompt:

[173] p: The expected response is the Spanish antonym ‘vivo’ → \to ‘muerto’. Therefore, the ID vectors are extracted from open-ended Spanish antonym prompts and the OOD vectors are extracted from open-ended English and multiple-choice prompts.

[174] p: In Figure 23 , we see that the steering effect trends are similar to the original implementation (although the absolute performance is lower for both 𝒞 ​ 𝒱 \mathcal{CV} s and ℱ ​ 𝒱 \mathcal{FV} s). In Figure 24 , we also see that the KL divergence is lower for the 𝒞 ​ 𝒱 \mathcal{CV} s compared to the ℱ ​ 𝒱 \mathcal{FV} s. Crucially, the 𝒞 ​ 𝒱 \mathcal{CV} s (extracted from English) steer the model to produce the Spanish antonym (the contextually appropriate response), rather than the English antonym or the English translation. This demonstrates that 𝒞 ​ 𝒱 \mathcal{CV} s encode the abstract ‘Antonym’ concept rather than ‘English Antonym’. Mechanistically, this suggests that the 𝒞 ​ 𝒱 \mathcal{CV} amplifies the task probability (“do an antonym”) while relying on the prompt’s existing context to determine the surface form (“in Spanish”), rather than injecting language-specific content.

[175] figure: Figure 23: Steering effect across layers and all concepts for different languages.

[176] figure: Figure 24: KL divergence between ID and OOD for different languages. Model: Llama 3.1 70B.

[177] h2: Appendix O Cross-Format Activation Patching

[178] p: To determine whether the dissociation between causal (FV) and invariant (CV) heads stems from the activation patching setup—specifically, whether patching within the same format biases results toward format-specific heads—we conducted cross-format activation patching across all 6 combinations of input formats. In this experiment, we extracted activations from clean prompts in one format (e.g., Open-Ended English) and patched them into a corrupted run of a different format (e.g., Multiple-Choice).

[179] p: We found that cross-format patching consistently identified a subset of the original Function Vector heads (e.g., in Llama-3.1-70B, head L31H18 always appears in the top-5 for both within-format and cross-format patching). It did not identify Concept Vector heads. This result shows that FVs are the primary causal mechanism for the task across all formats, despite their representations being format-specific. CVs, while representationally invariant, do not appear to causally drive the model’s behavior in these tasks.

[180] figure: Source Format Target Format Max AIE Overlap w/ FV (top-5) Overlap w/ CV (top-5) OE-ENG OE-FR 0.22 4 0 OE-ENG MC 0.02 2 0 OE-FR MC 0.01 1 0 MC OE-ENG 0.23 3 0 OE-FR OE-ENG 0.41 4 0 MC OE-FR 0.12 4 0 Table 4: Cross-format Activation Patching Results (Llama 3.1 70B) . We show the max Average Indirect Effect (AIE) and the number of overlapping heads with the standard Function Vectors (FV) and Concept Vectors (CV) (top-5 heads). The patching source refers to the format from which activations were extracted, and the target refers to the corrupted prompt format into which they were patched. FV heads are consistently identified across formats (specifically L31H18 and L35H57), while CV heads are not.

[181] h2: Instructions for reporting errors

[182] p: We are continuing to improve HTML versions of papers, and your feedback helps enhance accessibility and mobile support. To report errors in the HTML that will help us improve conversion and rendering, choose any of the methods listed below:

[183] p: Tip: You can select the relevant text first, to include it in your report.

[184] p: Our team has already identified the following issues . We appreciate your time reviewing and reporting rendering errors we may not have found yet. Your efforts will help us improve the HTML versions for all readers, because disability should not be a barrier to accessing research. Thank you for your continued support in championing open access for all.

[185] p: Have a free development cycle? Help support accessibility at arXiv! Our collaborators at LaTeXML maintain a list of packages that need conversion , and welcome developer contributions .
