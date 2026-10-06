[0] h5: Report GitHub Issue

[1] p: Content selection saved. Describe the issue below:

[2] h1: Probing for Knowledge Attribution in Large Language Models

[3] h6: Abstract

[4] p: Large language models (LLMs) often generate fluent but unfounded claims, or hallucinations, which fall into two types: (i) faithfulness violations—misusing user context—and (ii) factuality violations—errors from internal knowledge. Proper mitigation depends on knowing whether a model’s answer is based on the prompt or its internal weights. This work focuses on the problem of contributive attribution: identifying the dominant knowledge source behind each output. We show that a probe, a simple linear classifier trained on model hidden representations, can reliably predict contributive attribution. For its training, we introduce AttriWiki , a self-supervised data pipeline that prompts models to recall withheld entities from memory or read them from context, generating labelled examples automatically. Probes trained on AttriWiki data reveal a strong attribution signal, achieving up to 0.96 Macro- F 1 F_{1} on Llama-3.1-8B, Mistral-7B, and Qwen-7B, transferring to out-of-domain benchmarks (SQuAD, WebQuestions) with 0.94–0.99 Macro- F 1 F_{1} without retraining. Attribution mismatches raise error rates by up to 70%, demonstrating a direct link between knowledge source confusion and unfaithful answers. Yet, models may still respond incorrectly even when attribution is correct, highlighting the need for broader detection frameworks. IvoBrink/AttriWiki

[5] h2: 1 Introduction

[6] p: Picture yourself rushing to book a last-minute flight for a funeral. You ask an airline’s chatbot whether you can claim a bereavement fare after travelling, and the system confidently replies, “Yes, you have 90 days.” The rule, however, never existed, and months later, the refund is denied. This example stems from a real case in which, in a landmark ruling, the British Columbia Civil Resolution Tribunal held Air Canada liable for its chatbot’s misinformation ( Cecco, 2024 ; Lifshitz and Hung, 2024 ) . was A single inaccurate but authoritative response can now impose serious financial, legal, or practical consequences. Although LLM hallucinations, untrue or ungrounded outputs ( Huang et al., 2025 ) like in the case of the bereavement fare, have become a central research focus, existing detection techniques often miss a more fundamental issue: users lack visibility into where a model’s answers come from. The airline could have benefited from knowing the chatbot’s true provenance, as attribution would have enabled verification against official policy. Existing prior approaches in research, including LLMs-as-a-judge ( Manakul et al., 2023 ; Ravi et al., 2024 ; Friel and Sanyal, 2023 ) and uncertainty measures ( Wilson and Izmailov, 2020 ; Shafer and Vovk, 2008 ) , struggle because models can be confidently wrong ( Kuhn et al., 2023 ) and because “hallucination” lacks a consistent operational definition ( Qi et al., 2024 ) . Moreover, these methods evaluate correctness but not provenance, even though provenance is an essential factor determining whether users can trust an answer.

[7] p: To address this gap, we turn to contributive attribution ( Worledge et al., 2024 ) , which distinguishes between contextual knowledge (from the prompt or retrieved evidence) and parametric knowledge (stored in the model’s weights). This framing complements the well-known divide between faithfulness and factuality errors ( Huang et al., 2025 ; Qi et al., 2024 ; Ye et al., 2024 ) within hallucination taxonomies, but shifts the focus: instead of asking whether the output is true, we ask whether the model relied on the source the user intended. Attribution signals can help users detect when a model defaults to conflicting parametric knowledge or, conversely, when it overly relies on irrelevant context. This is particularly valuable in retrieval-augmented generation systems ( Lewis et al., 2020 ; Guu et al., 2020 ; Borgeaud et al., 2022 ; Izacard et al., 2023 ) , where errors often arise not from bad retrieval but from the model ignoring retrieved information ( Petroni et al., 2020 ; Li et al., 2023 ) .

[8] p: Our contributions are as follows: Using Wikipedia passages, entity selection, and controlled prompt variations, we create the AttriWiki dataset, in which each completion has a clear, verifiable knowledge source (parametric or contextual). During generation, we record hidden states at key token positions, producing attribution features at scale without manual labels. We then train lightweight probing classifiers on these representations to distinguish contextual from parametric retrieval and test their generalisation on external QA datasets such as WebQuestions and SQuAD ( Berant et al., 2013 ; Rajpurkar et al., 2016 ) . We show that contributive attribution is linearly decodable from LLM hidden states, particularly from the middle to upper layers. Attribution mismatches, in which a model answers from the wrong knowledge source, significantly increase error rates, especially in misleading contexts. Yet, correct attribution alone does not guarantee factual correctness. AttriWiki and other code used in this work are publicly available to support future research.

[9] h2: 2 Related Work

[10] h5: Knowledge in LLMs.

[11] p: Understanding hallucinations ultimately requires understanding how large language models acquire, store, and retrieve knowledge. Factual knowledge in LLMs is parametric and emergent: no single parameter encodes a fact, but distributed activation patterns collectively give rise to factual recall. Early probing work, such as LAMA ( Petroni et al., 2019 ) showed that factual recall in language models is brittle, varying substantially across languages, paraphrases, and prompt formulations ( Kassner et al., 2021 ; Elazar et al., 2021 ; Jiang et al., 2020 ) .

[12] p: Yet, recent epistemic analyses formalise when a model knows a fact by mapping philosophical notions of knowledge onto model behaviour. Under the “true-belief” framework ( Fierro et al., 2024 ) , a fact is considered stored in a model’s parameters if it is reproduced consistently across paraphrases, enabling a practical distinction between parametric knowledge and context-derived information.

[13] h5: Attribution and Knowledge Conflicts.

[14] p: Once parametric and contextual knowledge are distinguished, a central challenge is detecting their usage. Knowledge conflicts arise when parametric beliefs contradict retrieved or provided context, a situation common in retrieval-augmented settings ( Petroni et al., 2020 ; Li et al., 2023 ) . Attribution methods aim to trace generated content back to its source. Retrieval-based approaches such as RAG ( Lewis et al., 2020 ; Izacard et al., 2023 ) expose evidence to the model but cannot guarantee that it is used, and models frequently hallucinate citations even when retrieval is correct ( Zuccon et al., 2023 ) .

[15] p: Model-based attribution methods target contributive attribution, either through architectural modifications that encode source identifiers ( Khalifa et al., 2024 ) or probing approaches that infer whether outputs derive from memory or context via knowledge conflicts ( Tighidet et al., 2024 ) . However, the former requires substantial architectural changes, while the latter relies on adversarial prompts that conflate provenance with knowledge resolution.

[16] p: Recent mechanistic work has begun to clarify how such conflicts are processed internally. Zhao et al. (2025) trace entity-level knowledge flows through attention heads, MLP updates, and residual streams, showing that parametric and contextual knowledge are routed through largely distinct attention circuits and coexist as superposed signals rather than competing via direct suppression. Conflicts are resolved through differential accumulation of signal strength across layers, not by erasing one source. This perspective provides a mechanistic foundation for attribution: if both knowledge sources persist internally, their relative contribution should be detectable from model activations.

[17] h5: Probing LLM Representations.

[18] p: Probing hidden states offers a lightweight approach for studying knowledge usage directly from model internals. This line of work builds on a long tradition of analysing how linguistic and factual information is encoded across transformer layers ( Conneau et al., 2018 ; Tenney et al., 2019 ; Hewitt and Manning, 2019 ) . Prior studies show that layers specialise in surface, syntactic, and semantic features ( Jawahar et al., 2019 ) , that factual associations emerge in neuron-level key–value structures ( Geva et al., 2021 ) , and that hidden states reflect latent capabilities such as lying ( Azaria and Mitchell, 2023 ) , causal reasoning ( Rohekar et al., 2024 ) , and instruction following ( Heo et al., 2025 ) . These findings suggest that signals relevant to attribution and provenance are also present in model activations.

[19] p: Recent work applies probing specifically to hallucination detection. MIND ( Su et al., 2024 ) trains classifiers on final-layer activations, outperforming SelfCheckGPT ( Manakul et al., 2023 ) and GPT-4o critics on several benchmarks. However, it provides limited interpretability regarding why a response is classified as hallucinated.

[20] p: Overall, prior work offers strong taxonomies and attribution techniques, but a key gap remains: existing methods lack scalable, controlled datasets that cleanly isolate parametric versus contextual knowledge use. This motivates approaches that explicitly construct such contrasts and probe hidden states to reveal the true origin of model outputs.

[21] h2: 3 A Self-Supervised Data Pipeline

[22] h3: 3.1 Motivation

[23] p: Although recent work examines the use of parametric–contextual knowledge, existing datasets do not isolate retrieval modes. Many studies expose both sources simultaneously and infer attribution post hoc from the model’s answer ( Tighidet et al., 2024 ; Xu et al., 2024 ) , conflating provenance with downstream decision-making and conflict resolution.

[24] p: Therefore, checking whether a fact is present in a model’s parametric memory is necessary to isolate contextual vs. parametric examples. Prior work verifies parametric knowledge via data recency ( Zhang et al., 2024 ) or by querying the model ( Cheng et al., 2024 ) . However, these approaches neither explicitly detect attribution nor prevent the simultaneous availability of parametric and contextual knowledge when analysing their interactions.

[25] p: To this end, we introduce AttriWiki , a self-supervised data pipeline that generates paired examples which force models to draw information either from context or from stored knowledge, established through extensive knowledge testing. By ensuring that only a single knowledge source is available at generation time, AttriWiki enables isolated attribution analysis without manual labelling.

[26] figure: Figure 1: Overview of the data generation pipeline, showing entity selection, knowledge testing, prompt construction, and hidden-state extraction.

[27] h3: 3.2 Data and Models

[28] h5: Data.

[29] p: Wikipedia provides dense factual text that mid-sized open language models (approximately 7--8B parameters) only partially memorise, allowing both retrieval modes to occur naturally. We sample 20k pages using the MediaWiki API, 1 1 1 https://en.wikipedia.org/w/api.php , The Wikipedia text is licensed under CC BY-SA 3.0/4.0 , and all use complies with the terms of that license. discarding snippets shorter than 300 characters.

[30] h5: Data Generation Model.

[31] p: We use GPT-4o-mini ( gpt-4o-mini ; OpenAI, 2024 ) as an instruction-following model to paraphrase passages, remove or retain entities, and rewrite completion sentences during dataset construction (see next section).

[32] h5: Target Models.

[33] p: Attribution probing is performed on open-weight language models from which we extract hidden states during generation. We use Llama-3.1-8B ( Dubey et al., 2024 ) , Mistral-7B ( Jiang et al., 2023 ) , and Qwen2.5-7B ( Qwen et al., 2025 ) as target models.

[34] h3: 3.3 Method

[35] p: An overview of the data generation pipeline is shown in Figure 1 . Because attribution concerns the source of specific factual content, we focus on named entities as attribution anchors. Entities can often be retrieved from parametric memory or local context and selectively removed without altering the surrounding semantics. Therefore, the pipeline begins with entity identification using spaCy’s transformer-based NER ( Honnibal et al., 2020 ) . To remove redundant mentions, we filter entities that overlap, are synonymous, or closely resemble the page title using a RoBERTa ( Liu et al., 2019 ) cross-encoder similarity model. 2 2 2 cross-encoder/stsb-roberta-base The model assigns pairwise semantic similarity scores, and entities above a threshold of 0.6 0.6 are excluded; we refer to this procedure as synonym matching . The threshold is determined heuristically and used consistently throughout this work. From the remaining candidates, GPT-4o-mini selects up to three representative, non-numeric, non-temporal entities per passage, balancing well-known and lesser-known facts (see Section C.1.1 ).

[36] p: Each entity–passage pair undergoes knowledge testing to determine whether the target model can recall the entity independently of the passage. This serves as an operational proxy for distinguishing entities that are already encoded in the model’s parametric memory from those that require contextual evidence, thereby isolating the classes. We use three prompt formats to test entity knowledge (see Section C.1.2 ). If any test elicits the correct entity (exact or synonym match ), it is labelled known ; otherwise, unknown . This high-recall labelling avoids false unknown labels, preferring unanswerable over multi-source samples.

[37] p: We then construct contextual and parametric variants for each passage. For known entities, all mentions are removed using GPT-4o-mini ( Section C.1.3 ), thereby forcing parametric retrieval; for unknown entities, the name remains visible, while a different entity is removed to prevent lexical bias while still enforcing contextual retrieval. GPT-4o-mini appends a short, natural completion cue such as “The [description] is called …,” yielding paired prompts that differ only in the presence of the entity (see Section C.1.4 ). Each prompt is submitted to the target model to produce a completion. During greedy decoding, we extract hidden representations at two key token positions: (i) the first generated token (FTG), which reflects the model’s initial response intent allowing us to compare responses that do not contain specific entities ( Su et al., 2024 ) , and (ii) the last token of the entity (LTE), capturing the fully integrated entity semantics ( Tighidet et al., 2024 ) . 3 3 3 We omit first-token-entity as it coincides with first-token-generation in almost all cases. Entity spans are located by exact or synonym matching , and the corresponding hidden states are serialised for attribution classification. This automated pipeline produces large volumes of data, with each example having a verifiable knowledge source.

[38] h3: 3.4 Evaluating Bias

[39] p: To verify that AttriWiki does not introduce lexical shortcuts between classes as an unintended effect of our knowledge-proxy, 4 4 4 For instance, generic descriptors such as “a country” may occur more frequently in contexts associated with widely known facts, inadvertently biasing a classifier toward predicting parametric knowledge based on surface-level phrasing rather than attribution. we train text-only classifiers on the passages. A balanced bag-of-words logistic regression and a logistic regression on DeBERTaV3 5 5 5 microsoft/deberta-v3-large -embeddings ( He et al., 2023 ) are evaluated under five-fold cross-validation (for specifics see Section A.1 ).

[40] h3: 3.5 Results.

[41] p: Table 1 summarises the AttriWiki dataset for Llama-3.1-8B, Mistral-7B-v0.1, and Qwen2.5-7B. Llama and Mistral show parametric-dominant distributions ( ≈ \approx 5:3 and 3:2), while Qwen is nearly balanced ( ≈ \approx 1:1) and more context-heavy. Dataset sizes are similar across models, with Llama slightly larger and Qwen slightly smaller. Synonym match rates (percentage of completions that matched semantically but not verbatim) are highest for Qwen (12.0%), indicating greater lexical variability, whereas Llama’s lower rate suggests stronger verbatim recall. Overall, the pipeline behaves consistently, with Qwen exhibiting weaker parametric recall and greater reliance on context.

[42] figure: AttriWiki Ratio (P:C) Syn Size Llama-3.1-8B ≈ \approx 5:3 10.3% 27,244 Mistral-7B-v0.1 ≈ \approx 3:2 10.7% 26,853 Qwen2.5-7B ≈ \approx 1:1 12.0% 24,336 Table 1: AttriWiki dataset composition for each model. Ratio (P:C) denotes the approximate parametric-to-contextual proportion of examples. Syn denotes the synonym match rate, and Size denotes the total number of examples.

[43] p: To gain insight into how contextual and parametric information is represented internally, we perform a per-layer 2D principal component analysis (PCA; Pearson, 1901 ) on decoder hidden states extracted at the first token of generation (FTG). As shown in Figure 2 (refer to Appendix B for all the layers), representations from early layers largely overlap, while a clearer separation between contextual and parametric activations emerges from the middle layers onward in all three models. This pattern suggests that attribution-related information becomes increasingly linearly accessible in higher layers, indicating that contextual and parametric signals are likely encoded in separable directions of the hidden state space.

[44] figure: Figure 2: Per-layer PCA of decoder hidden states at the first generated token (FTG). Qwen has 28 layers (vs. 32 in Llama and Mistral). In the mid to upper layers, contextual and parametric activations increasingly diverge, indicating greater separability.

[45] p: We next evaluate whether simple lexical features can account for the observed attribution signal. Bag-of-words and embedding-based classifiers achieve F 1 F_{1} scores of 0.65–0.67, indicating the presence of lexical cues, though these alone are insufficient for reliable performance. BoW on the data for all models shows similar performance and nearly identical unigram profiles: contextual examples favour entity-specific terms (e.g., named, born in, towns), whereas parametric examples lean toward broader encyclopedic vocabulary (e.g., countries, nationalities). This suggests that our knowledge proxy introduces a mild and stable lexical bias.

[46] figure: Model Classifier F 1 F_{1} Llama-3.1-8B BoW 0.653 Embedding 0.667 Mistral-7B-v0.1 BoW 0.660 Embedding 0.666 Qwen2.5-7B BoW 0.680 Embedding 0.679 Table 2: Bias detection performance using BoW and embedding-based classifiers on AttriWiki .

[47] h2: 4 Attribution Classification

[48] p: To assess whether hidden states in AttriWiki truly encode the source of a model’s knowledge, we train three probing classifiers of increasing complexity. Each model is trained on 64% of AttriWiki , validated on 16%, and tested on the remaining 20%, then evaluated for out-of-domain generalisation. Results are reported as macro- F 1 F_{1} . Consult Section A.2 for more details.

[49] h3: 4.1 Classifiers

[50] p: AttriWiki for Llama and Mistral shows a mild class imbalance ( ≈ \approx 3:2 parametric–contextual). We compensate by using balanced loss functions (detailed below). To prevent information leakage across passages, we further enforce title-disjoint train–test splits, ensuring that no samples originating from the same article appear in both splits.

[51] h5: Final-Layer Logistic Regression ( Final-LR ).

[52] p: As a minimal baseline, we train a single logistic unit on the normalised hidden vector 𝐡 L ∈ ℝ H \mathbf{h}_{L}\in\mathbb{R}^{H} from the final transformer layer:

[53] table: p = σ ⁡ ( 𝐰 ⊤ ​ 𝐡 L + b ) , p=\sigma(\mathbf{w}^{\top}\mathbf{h}_{L}+b), (1)

[54] p: where 𝐰 ∈ ℝ H \mathbf{w}\in\mathbb{R}^{H} and b ∈ ℝ b\in\mathbb{R} are the classifier weights and bias, σ \sigma is the sigmoid function, and training uses an ℓ 2 \ell_{2} -regularised logistic loss with inverse-frequency class weighting.

[55] h5: Layer-Weighted Logistic Regression ( Layer-LR ).

[56] p: To exploit depth information, we learn a set of unconstrained layer parameters 𝜽 ∈ ℝ L \boldsymbol{\theta}\in\mathbb{R}^{L} , which are transformed via a softmax to obtain aggregation weights 𝜶 = softmax ⁡ ( 𝜽 ) \boldsymbol{\alpha}=\mathrm{softmax}(\boldsymbol{\theta}) over transformer layers. These weights are used to form a blended representation

[57] table: 𝐡 ¯ = ∑ ℓ = 1 L α ℓ ​ 𝐡 ℓ . \bar{\mathbf{h}}=\sum_{\ell=1}^{L}\alpha_{\ell}\mathbf{h}_{\ell}. (2)

[58] p: A logistic head then predicts the probability of parametric retrieval from 𝐡 ¯ \bar{\mathbf{h}} . All parameters ( 𝜽 , 𝐰 , b ) (\boldsymbol{\theta},\mathbf{w},b) are trained jointly using binary cross-entropy with logits and positive-class reweighting to account for label imbalance, optimised with AdamW ( Kingma and Ba, 2015 ) . Hyperparameters and training details are reported in Section A.2 .

[59] h5: Layer-Weighted MLP ( Layer-MLP ).

[60] p: We extend the previous model with sparsemax-normalised aggregation weights ( Martins and Astudillo, 2016 ) , encouraging focus on a small number of salient layers, motivated by the tendency of softmax-aggregated MLP probes to learn diffuse layer weights. The linear classifier is replaced with a compact two-layer MLP operating on the aggregated representation 𝐡 ¯ \bar{\mathbf{h}} :

[61] table: p = σ ⁡ ( 𝐰 2 ⊤ ​ GELU ​ ( 𝐖 1 ​ 𝐡 ¯ ) + b ) , p=\sigma\!\left(\mathbf{w}_{2}^{\top}\mathrm{GELU}(\mathbf{W}_{1}\bar{\mathbf{h}})+b\right), (3)

[62] p: We use GELU ( Hendrycks and Gimpel, 2016 ) , where 𝐖 1 ∈ ℝ m × H \mathbf{W}_{1}\in\mathbb{R}^{m\times H} projects the hidden representation of dimension H H into a bottleneck of size m m , and 𝐰 2 ∈ ℝ m \mathbf{w}_{2}\in\mathbb{R}^{m} denotes the output-layer weights. Hyperparameters and training details are reported in Section A.2 .

[63] h3: 4.2 Out-of-distribution Datasets

[64] p: All classifiers are first trained on AttriWiki and then evaluated on 2,000 2{,}000 samples from two external QA datasets that isolate the retrieval source. All samples include a single demonstration line to enforce output format (see Section C.2 ).

[65] h5: WebQuestions ( Berant et al., 2013 ) .

[66] p: Each factoid question lacks supporting context (e.g., “Who developed general relativity?” → \rightarrow Albert Einstein ); hence, answers must come from the model’s parametric memory. Items are wrapped in a one-shot Q → \!\rightarrow\! A prompt for compatibility with decoder-only models.

[67] h5: SQuAD ( Rajpurkar et al., 2016 ) .

[68] p: Passages contain answers verbatim, making the task predominantly contextual . To filter memorised facts, we briefly query each question without its paragraph; if the model still answers correctly, the item is recorded as prior knowledge and used for a separate experiment (see below). The remaining examples form the contextual test set.

[69] h5: SQuAD Variants.

[70] p: We derive three controlled variants: (a) an irrelevant context split pairing each known question with an irrelevant paragraph to force parametric retrieval; (b) an answer-string-decoy version where the paragraph contains the correct answer verbatim in an unrelated context, testing reliance on surface overlap; and (c) a dual-source version retaining both context and prior-knowledge cases to study retrieval preference. Together, these variants test robustness against degenerate heuristics, e.g., predicting attribution solely from the presence of context.

[71] h3: 4.3 Results

[72] h5: Attribution Performance.

[73] p: Table 3 reports attribution classification on the held-out AttriWiki split. We compare Final-LR , Layer-LR , and Layer-MLP . Layer aggregation improves F 1 F_{1} by 7–11 pp over the final-layer baseline, while the MLP yields only marginal gains ( ≈ \approx 1 pp). Token choice matters: the last token of the entity ( LTE ) performs best (0.95–0.96), while the first token of generation ( FTG ) remains slightly lower but above 0.90. Mistral consistently outperforms Llama and Qwen by one point, though trends are consistent across models. Macro- F 1 F_{1} closely matches accuracy, indicating balanced errors.

[74] figure: Model Final-LR Layer-LR Layer-MLP Token = FTG (First Token of Generation) Llama-3.1-8B 0.841 0.918 0.920 Mistral-7B-v0.1 0.844 0,922 0.933 Qwen2.5-7B 0.835 0.912 0.926 Token = LTE (Last Token of Entity) Llama-3.1-8B 0.854 0.947 0.954 Mistral-7B-v0.1 0.904 0.958 0.961 Qwen2.5-7B 0.867 0.935 0.949 Table 3: Macro- F 1 F_{1} on AttriWiki-test ( n ≈ 5,000 n\approx 5{,}000 )

[75] h5: Generalization.

[76] p: To assess generalisation, we evaluate the classifier on two out-of-domain QA benchmarks: SQuAD (contextual) and WebQuestions (parametric). As shown in Table 4 , it generalises near perfectly without fine-tuning, achieving 0.94–0.99 accuracy across Llama, Mistral, and Qwen on both benchmarks. Similar results are observed for the Layer-MLP in the appendix, in Table 11 . We report only on first-token generation (FTG) because it allows us to analyse incorrect responses in later sections.

[77] figure: Model SQuAD WebQ Llama-3.1-8B 0.977 0.967 Mistral-7B-v0.1 0.943 0.999 Qwen2.5-7B 0.997 0.999 Table 4: Generalisation accuracy of Layer-LR (FTG) on out-of-domain QA datasets. WebQ = WebQuestions.

[78] h5: Which Layers Does the Classifier Rely on?

[79] figure: Figure 3: Layer-aggregation weights learned by Layer-LR for first-token generation and last-token entity representations. Curves show learned weights across transformer layers, smoothed with a Gaussian kernel for visual clarity. The x-axis is restricted to layers 10–24, as earlier and later layers receive negligible weight.

[80] p: As shown in Figure 3 , the classifier concentrates weight in the upper-middle transformer layers across models. For first-token generation, peak contributions occur at layers 16 (Llama-3.1-8B), 19 (Mistral-7B-v0.1), and 21 (Qwen-2.5-7B), while last-token entity representations peak earlier at layers 14 (Llama, Mistral) and 18 (Qwen). Notably, Qwen assigns weight to relatively deeper layers given its shallower overall depth (28 versus 32).

[81] h3: 4.4 Ablation

[82] p: Ablation is performed on the Layer-LR FTG because of its robustness (see below) and its applicability to incorrect responses.

[83] h5: Degenerate Attribution.

[84] p: We evaluate whether attribution probes rely on degenerate heuristics rather than genuine provenance signals. First, in the answer-string decoy variant of SQuAD—where the gold answer appears verbatim in an unrelated context—performance drops for all classifiers. However, Layer-LR remains well above chance (0.724). 6 6 6 Semantic irrelevance is not explicitly verified; random passages are used to stress-test degenerate heuristics rather than to measure attribution performance. In contrast, the MLP collapses to near-random performance (0.541), indicating that the MLP overfits to lexical shortcuts such as entity repetition, whereas Layer-LR captures a more robust attribution signal ( Table 10 ). Second, when both parametric memory and context suffice to answer a question, models overwhelmingly default to the contextual channel (87.1%). This rules out the degenerate explanation that the probe merely detects whether a fact is stored in the model’s parameters, rather than which source the model actually uses. Third, in the irrelevant-context setting—where known facts are paired with unrelated passages—92% of answers are still attributed as parametric, ruling out a trivial heuristic that equates the mere presence of context with contextual attribution.

[85] h5: Error and Attribution Mismatch.

[86] p: To analyse attribution and answer correctness, we consider two complementary conditions: (i) present parametric knowledge paired with irrelevant context, and (ii) absent parametric knowledge paired with relevant context. Source alignment (parametric when required, or contextual when required) and answer correctness form a 2 × 2 2{\times}2 contingency table, analysed using Fisher’s exact test ( Fisher, 2018 ) , with relative risk as the effect size.

[87] p: Attribution mismatches strongly correlate with errors ( p ≪ 0.001 p\ll 0.001 ), with asymmetric effects: relying on misleading context increases errors by up to ≈ \approx 70% when parametric knowledge is required, whereas defaulting to parametric memory in contextual settings increases errors by only ≈ \approx 30%.

[88] h2: 5 Discussion

[89] p: Our findings indicate that contributive attribution , whether a completion is driven by contextual evidence or parametric memory, is a representation-level property that is often linearly accessible from hidden states. This reframes attribution as a diagnostic of which knowledge channel the model is using, complementing hallucination taxonomies that distinguish between faithfulness and factuality errors ( Huang et al., 2025 ; Qi et al., 2024 ; Ye et al., 2024 ) and enabling online attribution signals that do not rely on post hoc verification.

[90] p: Prior work shows that contextual and parametric signals coexist and are differentially routed during generation, with models increasingly favouring one source over the other ( Zhao et al., 2025 ) ; we complement this by quantitatively detecting which knowledge source drives the model’s output. The concentration of probe weight in upper-middle layers further matches prior findings that mid-layer activations are most informative for parametric vs. contextual selection ( Tighidet et al., 2024 ) , and with broader evidence that later layers encode decision-relevant abstractions beyond surface form ( Jawahar et al., 2019 ; Tenney et al., 2019 ) .

[91] p: Attribution is helpful because it is not a proxy for uncertainty: models can be confident yet wrong ( Kuhn et al., 2023 ) . Our mismatch analysis shows that using the wrong knowledge source substantially increases error risk, particularly when misleading context overrides parametric knowledge. However, many errors persist despite correct source alignment, indicating that attribution should be viewed as one diagnostic axis among others rather than as a complete error detector.

[92] p: Two results nuance prior attribution work. First, the limited gains from an MLP head and its degradation under the answer-string decoy suggest that added model complexity encourages shortcut learning, while linear probes more reliably predict provenance. Second, unlike conflict-based approaches that infer attribution from contradictory prompts ( Tighidet et al., 2024 ; Xu et al., 2024 ) , AttriWiki isolates the knowledge source at generation time; strong performance under this isolation indicates that provenance signals exist even in the absence of explicit knowledge conflicts.

[93] h2: 6 Conclusions

[94] p: We study contributive attribution in large language models using a self-supervised pipeline ( AttriWiki ). Linear probes trained on AttriWiki achieve up to 0.96 F 1 F_{1} on Llama, Mistral, and Qwen models and generalise strongly to SQuAD and WebQuestions, indicating that attribution signals are linearly accessible in model activations. Attribution mismatches increase error risk by 30–70%, particularly under misleading contexts, although correct attribution alone does not guarantee correctness. Together, these findings establish attribution as a meaningful diagnostic signal.

[95] h5: Future work.

[96] p: Future work should explore how attribution signals can be integrated into downstream systems. In retrieval-augmented generation (RAG; Guu et al., 2020 ; Borgeaud et al., 2022 ), attribution probes could provide online signals to detect ignored evidence and trigger selective verification or re-retrieval. In LLM-powered chatbots, exposing attribution may also elicit more critical user engagement by clarifying whether responses rely on retrieved evidence or prior knowledge.

[97] p: Recent work on sparse auto-encoder feature dictionaries suggests that hidden-state representations can be mapped into shared, model-agnostic feature spaces Lan et al. (2024) . This raises the possibility that attribution-relevant signals—such as the contextual and parametric flows identified by Zhao et al. (2025) —could be aligned across models, enabling attribution classifiers to generalise beyond a single architecture.

[98] h2: Limitations

[99] h5: Data.

[100] p: AttriWiki ’s controlled Wikipedia domain may limit generalisation; testing attribution signals on legal text, dialogue, and noisy web data is essential. Extending to multilingual settings also poses challenges to AttriWiki since knowledge varies across languages ( Kassner et al., 2021 ) . Additionally, shortcut learning poses a risk because our knowledge proxy introduces lexical bias.

[101] h5: Attribution Classification.

[102] p: The classifier would benefit from moving beyond token-level attribution to sequence-level approaches. While our current method performs well on factual questions, it struggles in more natural settings where no clear entity span exists. Aggregation strategies, such as attention-based span scoring, could provide more accurate attribution in these cases. Another limitation is model dependence: each LLM requires a new classifier, and retraining the model often necessitates retraining the classifier and regenerating data if the model’s knowledge evolves.

[103] h5: Ablation.

[104] p: Although informative, error analysis remains challenging. Phenomena such as contradictions, exaggerations, and refusal to answer are often grouped under hallucinations, yet our focus here is on forced factual retrieval. Assessing answer correctness is equally difficult. Minor variations, such as one-letter acronym slips (e.g., GDP → \rightarrow GPD), can bypass the cross-encoder ( synonym matching ), while valid polarity with low lexical overlap may also lead to misclassifications. For example, the answer “smaller” correctly responds to “Were the houses bigger or smaller?” but fails against the gold label “smaller houses.”

[105] h2: Ethics Statement

[106] p: This work only uses publicly available datasets and does not involve human subjects or personal data. One API-based LLM is used solely for data generation. We do not identify significant ethical risks beyond those common to interpretability research.

[107] h2: Acknowledgments

[108] p: This work is supported by the Dutch National Science Foundation (NWO Vici VI.C.212.053) and KPMG NL. We would also like to express our gratitude to Ivan Titov for his valuable guidance and feedback throughout this work.

[109] h2: References

[110] h2: Appendix A Hyperparameters

[111] p: This appendix documents all hyperparameters used in our experiments. We separate configurations for bias evaluation models and attribution classifiers .

[112] h3: A.1 Bias evaluation

[113] p: We evaluate bias using two complementary classifiers: a sparse BoW model and an embedding-based model. The former serves as a lightweight lexical baseline, while the latter tests whether bias signals persist in contextualised representations.

[114] figure: Component Configuration Text representation TF–IDF ngram_range = (1,2) max_features = 5000 Classifier Logistic regression class_weight = balanced max_iter = 1000 random_state = 42 Table 5: Hyperparameters for the TF–IDF logistic regression bias classifier.

[115] figure: Component Configuration Text representation Transformer embeddings model = microsoft/deberta-v3-large max_length = 128 padding = max_length truncation = true repr. = [CLS] dtype = float16 eval mode, no gradients Classifier Logistic regression max_iter = 1000 random_state = 42 Table 6: Hyperparameters for the embedding-based bias classifier.

[116] h3: A.2 Attribution classifiers

[117] p: Attribution classifiers are trained to probe internal model representations. Hyperparameters for Layer-LR and Layer-MLP were selected via grid search over dropout p p ( { 0 , 0.1 , 0.2 } \{0,0.1,0.2\} ), weight decay λ \lambda ( { 0 , × 10 − 4 , 10 − 3 , × 10 − 3 } \{0,5\!\times\!10^{-4},10^{-3},2\!\times\!10^{-3}\} ), learning rate η \eta ( { × 10 − 4 , 10 − 3 , × 10 − 3 } \{5\!\times\!10^{-4},10^{-3},2\!\times\!10^{-3}\} ), and (for Layer-MLP) bottleneck size m m ( { 64,128 } \{64,128\} ), using a title-aware 15% validation split. Models were trained for 10 epochs; the selected configuration maximises validation macro- F 1 F_{1} with early-stopping (tie-breaker: validation accuracy). Selected values are reported below.

[118] figure: Component Configuration Input representation Last transformer layer ( X [ : , − 1 , : ] X[:,-1,:] ) Preprocessing StandardScaler (default) Classifier Logistic regression class_weight = balanced solver = lbfgs penalty = ℓ 2 \ell_{2} max_iter = 1000 Table 7: Hyperparameters for Final-LR (last-layer logistic regression).

[119] figure: Component Configuration Input representation Layer stack X ∈ ℝ N × L × H X\in\mathbb{R}^{N\times L\times H} weighted aggregation Layer weighting Softmax( 𝜽 \boldsymbol{\theta} ), ∑ ℓ α ℓ = 1 \sum_{\ell}\alpha_{\ell}=1 Normalization ℓ 2 \ell_{2} per layer Dropout p = 0.1 p=0.1 Classifier head Linear( H → 1 H\rightarrow 1 ) Loss BCEWithLogitsLoss pos_weight = # ​ neg / # ​ pos =\#\text{neg}/\#\text{pos} Optimizer AdamW learning rate η = × 10 − 3 \eta=2\!\times\!10^{-3} weight decay λ = 10 − 3 \lambda=10^{-3} Training batch size = 64 =64 max epochs = 100 =100 early stopping (macro- F 1 F_{1} , patience = 3 =3 ) title-aware validation split ( 0.15 0.15 , seed = 42 =42 ) Table 8: Hyperparameters for Layer-LR (layer-weighted linear classifier).

[120] figure: Component Configuration Input representation Layer stack X ∈ ℝ N × L × H X\in\mathbb{R}^{N\times L\times H} weighted aggregation Layer weighting Sparsemax( 𝜽 \boldsymbol{\theta} ) Normalization ℓ 2 \ell_{2} per layer MLP head Linear( H → m H\rightarrow m ), m = 64 m=64 GELU, Dropout( p = 0.1 p=0.1 ) Linear( m → 1 m\rightarrow 1 ) Loss BCEWithLogitsLoss pos_weight = # ​ neg / # ​ pos =\#\text{neg}/\#\text{pos} Optimizer AdamW learning rate η = 10 − 3 \eta=10^{-3} weight decay λ = 10 − 3 \lambda=10^{-3} Training batch size = 64 =64 max epochs = 100 =100 early stopping (macro- F 1 F_{1} , patience = 3 =3 ) title-aware validation split ( 0.15 0.15 , seed = 42 =42 ) Table 9: Hyperparameters for Layer-MLP (layer-weighted MLP classifier).

[121] h2: Appendix B Additional Results

[122] p: This section reports additional experimental results that support the main findings in the paper, including ablation studies and out-of-domain generalisation performance.

[123] figure: Classifier Accuracy Layer-agg LogReg 0.724 Layer-agg MLP 0.541 Table 10: Answer-string decoy ablation on SQuAD using Llama-3.1-8B. While performance drops for all classifiers, the linear probe remains well above chance, whereas the MLP collapses to near-random accuracy, indicating reliance on entity repetition.

[124] figure: Figure 4: Per-layer PCA of hidden states for Llama-3.1-8B.

[125] figure: Figure 5: Per-layer PCA of hidden states for Mistral-7B-v0.1.

[126] figure: Figure 6: Per-layer PCA of hidden states for Qwen2.5-7B.

[127] figure: Model SQuAD WebQ Llama-3.1-8B 0.972 0.959 Mistral-7B-v0.1 0.958 0.948 Qwen-7B 0.998 0.980 Table 11: Generalisation accuracy of Layer-MLP (FTG) on out-of-domain QA datasets. WebQ = WebQuestions.

[128] h2: Appendix C Prompts

[129] h3: C.1 AttriWiki

[130] h4: C.1.1 Entity selection.

[131] p: This prompt was designed to select up to three entities to prevent longer passages containing more entities from being overrepresented in the data.

[132] h4: C.1.2 Knowledge testing.

[133] p: Given a Wikipedia passage and an entity, we present examples of the three knowledge tests.

[134] p: Alice: I can’t remember exactly who was the king of England in 1265 during the Battle of Evesham. I can’t remember. Bob: Actually, I know. It was {King Henry III.}

[135] p: Q: Who was the king of England during the Battle of Evesham in the 13th century? A: {King Henry III}

[136] p: The Battle of Evesham ( 4 August 1265 ) was one of the two main battles of 13th century England ’s Second Barons ’ War . It marked the defeat of Simon de Montfort, Earl of Leicester , and the rebellious barons by Prince Edward - later King Edward I - who led the forces of his father , {King Henry III.}

[137] p: 1. Dialogue

[138] p: 2. QA-style

[139] p: Note that the trailing entity mentions are removed using an exact string match in a later phase.

[140] p: 3. Truncated passage. The truncated passage is an exact string match, removing the first mention of the entity in the Wikipedia passage and removing all text succeeding and including the entity.

[141] h4: C.1.3 Entity removal.

[142] h4: C.1.4 Appending completion sentence.

[143] h3: C.2 SQuAD and WebQuestions

[144] p: One-shot prompts for SQuAD and WebQ.

[145] h2: Instructions for reporting errors

[146] p: We are continuing to improve HTML versions of papers, and your feedback helps enhance accessibility and mobile support. To report errors in the HTML that will help us improve conversion and rendering, choose any of the methods listed below:

[147] p: Tip: You can select the relevant text first, to include it in your report.

[148] p: Our team has already identified the following issues . We appreciate your time reviewing and reporting rendering errors we may not have found yet. Your efforts will help us improve the HTML versions for all readers, because disability should not be a barrier to accessing research. Thank you for your continued support in championing open access for all.

[149] p: Have a free development cycle? Help support accessibility at arXiv! Our collaborators at LaTeXML maintain a list of packages that need conversion , and welcome developer contributions .
