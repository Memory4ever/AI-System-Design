[0] h5: Report GitHub Issue

[1] p: Content selection saved. Describe the issue below:

[2] h1: When AI Writes, Whose Voice Remains? Quantifying Cultural Marker Erasure Across World English Varieties in Large Language Models

[3] figure: Figure 1 . Conceptual illustration of cultural ghosting: LLM-based writing assistants transform culturally marked expressions (e.g., "Kindly…", "Lah!", "Respected Sir…") into semantically preserved but culturally flattened outputs (e.g., "Please…", "Hello", "Respond"), demonstrating how meaning is retained while identity-linked linguistic markers are systematically erased. A central LLM figure converts culturally rich expressions from diverse speakers into standardized professional text, illustrating semantic preservation alongside cultural marker erasure.

[4] h6: Abstract.

[5] p: Large Language Models (LLMs) are increasingly used to “professionalize” workplace communication, often at the cost of linguistic identity. We introduce "Cultural Ghosting" , the systematic erasure of linguistic markers unique to non-native English varieties during text processing. Through analysis of 22,350 LLM outputs generated from 1,490 culturally marked texts (Indian, Singaporean,& Nigerian English) processed by five models under three prompt conditions, we quantify this phenomenon using two novel metrics: Identity Erasure Rate (IER) & Semantic Preservation Score (SPS). Across all prompts, we find an overall IER of 10.26%, with model-level variation from 3.5% to 20.5% (5.9 × \times range). Crucially, we identify a Semantic Preservation Paradox: models maintain high semantic similarity (mean SPS = 0.748) while systematically erasing cultural markers. Pragmatic markers (politeness conventions) are 1.9 × \times more vulnerable than lexical markers (71.5% vs. 37.1% erasure). Our experiments demonstrate that explicit cultural-preservation prompts reduce erasure by 29% without sacrificing semantic quality.

[6] h6: Keywords:

[7] h2: 1. Introduction

[8] p: Consider this sentence, common in Indian professional English:

[9] p: When processed through contemporary LLMs, this becomes:

[10] p: The output preserves core meaning but erases three cultural markers: the hierarchical politeness marker "kindly," the productive idiom "do the needful," and the emphatic "revert back." For the 1.5+ billion speakers of World Englishes, this is not linguistic improvement — it is cultural ghosting .

[11] p: Figure 3 illustrates this phenomenon, contrasting standard professionalism prompts with a preservation-oriented prompt that retains culturally specific phrasing (see Table 4 for empirical frequencies of these modes).

[12] figure: Figure 2 . End-to-end experimental pipeline for measuring cultural ghosting. The workflow progresses from dataset construction ( 1,490 texts ) through cultural marker annotation ( 108 markers ), LLM processing, forensic computation of Identity Erasure Rate (IER) & Semantic Preservation Score (SPS), statistical testing, to key empirical findings.

[13] p: English is not monolithic. Speakers from diverse cultural backgrounds have developed distinct World Englishes like Indian English, Singaporean English, Nigerian English each with unique lexical, pragmatic, & syntactic conventions that carry social meaning ( Agarwal et al., 2025 ) . Current LLM writing assistants respond to benign requests like “make this more professional” by removing culturally specific features. Unlike explicit bias (toxicity, stereotyping) which has been extensively studied ( Navigli et al., 2023 ; Dorleon and Shujaa, 2025 ; Chandra and Manhas, 2024 ) , this erasure occurs during helpful tasks email polishing, grammar correction, paraphrasing. Users seeking clarity may unwittingly receive cultural whitewashing ( Parvin, 2025 ) .

[14] p: In Indian English, "kindly" encodes hierarchical respect; in Nigerian English, "my dear" signals communal solidarity; in Singaporean English, particles like "lah" modulate assertiveness ( Parvin, 2025 ) . From a construction-based perspective, "do the needful" is not a deficient form requiring correction it is a productive construction in Indian English encoding hierarchical obligation. When LLMs strip these markers, they remove social context, pragmatic function, & cultural identity ( Chandra et al., 2026 ) .

[15] p: Through systematic analysis of 1,490 culturally marked texts processed by 5 LLMs across 3 prompt conditions (22,350 total outputs), we address three research questions:

[16] p: RQ1: To what extent do LLMs erase culturally marked features, & how does erasure vary across models?

[17] p: RQ2: Are certain marker categories (lexical, pragmatic, syntactic) systematically more vulnerable?

[18] p: RQ3: Can explicit cultural-preservation prompts reduce erasure without sacrificing semantic quality?

[19] p: Our contributions are: (1) We formalize cultural ghosting & the Semantic Preservation Paradox. (2) We introduce & validate Identity Erasure Rate (IER) & Semantic Preservation Score (SPS) metrics, providing the first large-scale quantification of marker erasure. (3) We demonstrate that pragmatic markers face 1.9 × \times vulnerability & that prompts reduce erasure by 29% without semantic cost . (4) We present proof-of-concept algorithmic mitigations beyond prompt engineering.

[20] h2: 2. Related Work

[21] p: Prior work documents reduced lexical diversity & increased uniformity in AI-assisted writing ( Agarwal et al., 2025 ; Chakrabarty et al., 2025 ) , with tensions between AI assistance & user agency ( Gadiraju et al., 2023 ) . The NLP community has documented systematic biases ( Navigli et al., 2023 ; Ferdaus et al., 2026 ; Chandra et al., 2025a ) , including cultural biases in LLMs ( Dorleon and Shujaa, 2025 ; Xiao et al., 2025 ) . Training data & alignment processes often privilege Western norms ( Mayeda et al., 2025 ; Bella et al., 2024 ) , creating “invisible languages” ( Khanna and Li, 2025 ) . Style-transfer systems often frame non-standard varieties as deficiencies to correct ( Neumann et al., 2025 ) . Regional biases have been explored in Asian narratives ( Shujaa et al., 2025 ) , Bengali dialects ( Wasi et al., 2025 ) , & African health contexts ( Nimo et al., 2025 ) . Minoritized linguistic features in sociolects like AAVE affect user perception & are often flagged as requiring correction ( Basoah et al., 2025 ; Dorn et al., 2024 ) . While this phenomenon extends beyond professional communication affecting creative writing, academic discourse, social media, & any LLM-mediated text we scope our empirical analysis to professional contexts where cultural markers carry particular pragmatic weight. No prior work has systematically measured whether LLMs maintain users’ cultural voice during generation tasks.

[22] h2: 3. Conceptual Framework

[23] p: Cultural ghosting occurs when AI writing assistance removes culturally specific linguistic markers while preserving semantic content. It is characterized by: benign intent (users request “help,” not erasure), invisible operation, systematic patterns favoring Western norms, & semantic preservation with identity loss. The Semantic Preservation Paradox captures a fundamental tension: high semantic fidelity (preserving what is said) coexists with cultural erasure (erasing how it is said). An LLM can achieve 75% semantic similarity while removing 10%+ of cultural markers. We categorize cultural markers into three types: Lexical (vocabulary unique to a variety, e.g., “prepone,” “chope”), Pragmatic (politeness & social positioning, e.g., “kindly,” “lah”), & Syntactic (grammatical structures, e.g., “discuss about”). Building on politeness theory ( Fathi, 2024 ) & construction grammar, we predict that pragmatic markers encoding face-management & relational positioning that is culturally specific & not recoverable from semantic content will be maximally vulnerable to erasure under semantic-preserving optimization.

[24] h2: 4. Methodology

[25] h3: 4.1. Dataset & Annotation

[26] p: We constructed a corpus of 1,490 texts from email corpora (Enron ( enr, [n. d.] ) , Clinton Archive ( Kaggle, [n. d.] ) , EmailSum ( Zhang et al., 2021 ) ), social media posts (Twitter/X), & news articles, representing Indian English (n=601), Singaporean English (n=261), Nigerian English (n=89), & American English baseline (n=539). Texts were deduplicated & selected only if containing at least one culturally specific linguistic marker, spanning multiple registers including workplace emails, social media posts, & news articles.

[27] p: We compiled a lexicon of 108 culturally specific markers grounded in sociolinguistic literature: Indian English (52 markers: 18 lexical, 16 pragmatic, 18 syntactic), Singaporean English (32 markers: 16 lexical, 9 pragmatic, 7 syntactic), & Nigerian English (24 markers: 10 lexical, 8 pragmatic, 6 syntactic). The final corpus contains 624 marker instances (mean = 0.42 markers/text), categorized as Lexical (260, 41.7%), Pragmatic (198, 31.7%), & Syntactic (166, 26.6%). Automated annotation used word-boundary-aware pattern matching ( Görge et al., 2025 ) , validated with high inter-annotator agreement (Cohen’s κ = 0.89 \kappa=0.89 , n=500). Table 1 presents representative markers & erasure examples.

[28] figure: Table 1 . Representative Cultural Markers & Erasure Examples Type Original After LLM Pragmatic “Kindly do X” “Please do X” Pragmatic “Respected sir” “Hello” Lexical “Do the needful” “Take necessary action” Lexical “Revert back” “Respond” Syntactic “Discuss about” “Discuss”

[29] h3: 4.2. Models & Prompts

[30] p: We evaluated five open-source instruction-tuned LLMs: Mistral-7B-Instruct ( Team, 2024b ) , Apertus-8B-Instruct ( Hernández-Cano et al., 2025 ) , DeepHat-7B ( Team, 2024a ) , MiMo-7B ( Xiaomi, 2025 ) , & Qwen3-8B ( Team, 2025 ) , representing diverse alignment strategies ( Talebpour et al., 2025 ) . Each text was processed under three prompt conditions: Baseline (“Make this text more professional & grammatically correct”), Neutral (“Improve the clarity & grammar of this text”), & Preservation (“Improve clarity & grammar while preserving cultural voice & regional expressions”). This yielded 22,350 paraphrases (1,490 × \times 5 × \times 3). Generation used deterministic parameters (temperature=0.7, top-p=0.9, seed=42) to ensure reproducibility. The pipeline is shown in Figure 2 .

[31] figure: Figure 3 . Illustrative vignette of cultural ghosting in AI-mediated rewriting. Given culturally marked Indian English input, standard professionalism prompts lead models to remove or replace regional markers (left), while preservation-oriented prompts sometimes retain surface forms but alter their pragmatic meaning (right).

[32] h3: 4.3. Evaluation Metrics

[33] p: Identity Erasure Rate (IER) quantifies the proportion of markers erased:

[34] table: IER = { ( M original − M output ) / M original if ​ M original > 0 undefined if ​ M original = 0 \text{IER}=\begin{cases}(M_{\text{original}}-M_{\text{output}})/M_{\text{original}}&\text{if }M_{\text{original}}>0\\ \text{undefined}&\text{if }M_{\text{original}}=0\end{cases}

[35] p: IER ranges from 0 (perfect preservation) to 1 (complete erasure). IER is computed only for texts containing at least one marker; baseline texts are excluded.

[36] p: Practical example: If an Indian English email contains “Kindly do the needful & revert back” (3 markers) & the LLM output retains only “revert back” (1 marker), then IER = ( 3 − 1 ) / 3 = 0.67 (3-1)/3=0.67 — two-thirds of the sender’s cultural voice was erased. An IER of 0 means every cultural marker survived; an IER of 1 means none did.

[37] p: Semantic Preservation Score (SPS) measures cosine similarity between sentence embeddings, defined as

[38] table: SPS = 𝐞 orig ⋅ 𝐞 out ‖ 𝐞 orig ‖ ​ ‖ 𝐞 out ‖ \text{SPS}=\frac{\mathbf{e}_{\text{orig}}\cdot\mathbf{e}_{\text{out}}}{\|\mathbf{e}_{\text{orig}}\|\,\|\mathbf{e}_{\text{out}}\|}

[39] p: validated against human judgments (Pearson r = 0.82 r=0.82 , n=500). SPS captures whether the meaning of the text is retained, independently of whether its cultural form is retained; it ranges from 0 (entirely different meaning) to 1 (identical meaning).

[40] h3: 4.4. Proxy Perceptual Validation

[41] p: We implemented proxy validations without human subjects: (1) We compared automatic marker detection with existing annotated corpora, achieving 91% alignment; (2) We used LLM-based judgment proxies where an instruction-tuned model labeled whether outputs preserve cultural markers with explanations and these corroborated our automatic metrics (89% agreement).

[42] h2: 5. Results

[43] h3: 5.1. Extent & Model Variation

[44] p: Across all 22,350 outputs, mean IER was 0.1026 (SD=0.298) while mean SPS was 0.7482 (SD=0.204), confirming the Semantic Preservation Paradox. One-way ANOVA revealed significant model differences: F(4, 7445) = 71.6, p < 0.001, η p 2 \eta_{p}^{2} = 0.037. While model choice explains 3.7% of total variance, indicating that other factors such as text characteristics & marker density also matter, this effect is substantial given the large sample size.

[45] figure: Table 2 . Model Performance (Baseline Prompt, n=1,490/model) Model IER M (SD) SPS M (SD) Rank Mistral-7B ( Team, 2024b ) 0.205 (0.389) 0.857 (0.089) Worst Apertus-8B ( Hernández-Cano et al., 2025 ) 0.152 (0.343) 0.805 (0.132) Poor DeepHat-7B ( Team, 2024a ) 0.145 (0.337) 0.764 (0.147) Fair MiMo-7B ( Xiaomi, 2025 ) 0.073 (0.249) 0.662 (0.257) Good Qwen3-8B ( Team, 2025 ) 0.035 (0.176) 0.589 (0.204) Best

[46] p: Table 2 shows IER ranged from 3.5% (Qwen3-8B) to 20.5% (Mistral-7B) a 5.9 × \times spread . Mistral-7B achieved highest semantic preservation (SPS=0.857) but worst marker retention, while Qwen3-8B showed the inverse pattern. This suggests alignment strategy matters more than intensity: models with intensive RLHF (Mistral, Qwen3) exhibited opposite behaviors, likely because Qwen3’s multilingual RLHF included more diverse English varieties. The lack of correlation between parameter count (7B vs. 8B) & IER confirms that what models are trained on & aligned toward , not scale, drives erasure behavior.

[47] p: Note: Our analysis is restricted to open-source instruction-tuned models. Whether proprietary models exhibit similar erasure patterns remains an open empirical question. We hypothesize comparable behavior given shared RLHF alignment paradigms.

[48] h3: 5.2. Differential Marker Vulnerability

[49] p: Mixed-design ANOVA revealed a highly significant effect of marker type: F(2, 14896) = 280.38, p < 0.001, η p 2 \eta_{p}^{2} = 0.036. A small but significant interaction (F(8, 14896) = 42.17, p = 0.031) suggests minor model-specific variations, but the dominant pattern holds across all models.

[50] figure: Table 3 . Erasure by Marker Category (All Models, Baseline Prompt) Type Instances Possible Erased Rate Pragmatic 198 990 708 71.5% Syntactic 166 830 467 56.3% Lexical 260 1,300 482 37.1% Total 624 3,120 1,657 53.1% Note: Possible erasures = instances × \times 5 models. Erasure rate = erased / possible.

[51] p: Table 3 reveals pragmatic markers were erased at 71.5% , nearly double the lexical rate (37.1%), indicating implicit features are most vulnerable to alignment-driven standardization.

[52] figure: Table 4 . Ghosting Modes (Mistral-7B) Mode Example (Input → \rightarrow Output) Direct Removal Kindly do the needful → \rightarrow Please complete the task Respected Sir → \rightarrow Hello Paraphrastic Assimilation Revert back → \rightarrow Respond Do the needful → \rightarrow Take necessary action False Preservation Kindly [+ do X] → \rightarrow Kindly [+ do X] (flattened) Baseline prompt, IER = 0.205. Preservation: − 19 -19 % direct removal, + 15 +15 % false preservation (8% → \rightarrow 23%).

[53] p: Figure 3 visualizes these modes using verbatim Mistral-7B & Qwen3-8B outputs. Left: Baseline prompt triggers direct removal. Right: Preservation prompt retains “Kindly” but Qwen3-8B (IER = 0.035) flattens its hierarchical function to generic politeness surface preservation without pragmatic recovery.

[54] p: Pragmatic markers are 1.9 × \times more likely to be erased than lexical markers. This disproportionate vulnerability targets precisely those features performing the most social work establishing politeness, managing face, navigating power distance. The observed ordering (pragmatic > syntactic > lexical) confirms our theoretical prediction: pragmatic markers encode face-management that is culturally specific & not recoverable from semantic content, making them maximally vulnerable under semantic-preserving optimization ( Chandra et al., 2025b ) . Manual inspection of 200 randomly sampled erasures revealed consistent patterns: “Kindly do X” becomes “Please do X” (flattening hierarchical politeness), “Respected sir/madam” becomes “Hello” (removing honorifics), privileging Western directness norms. Figure 4 visualizes the stark difference in vulnerability across marker categories.

[55] figure: Figure 4 . Erasure rates by marker category under the baseline prompt. Pragmatic markers (71.5%) show the highest vulnerability, followed by syntactic (56.3%) & lexical (37.1%). Erasure rates by marker category under the baseline prompt. Pragmatic markers (71.5\%) show the highest vulnerability, followed by syntactic (56.3\%) \& lexical (37.1\%).

[56] h3: 5.3. Mitigation Through Prompts

[57] p: Repeated-measures ANOVA revealed a significant prompt effect: F(2, 14896) = 55.0, p < 0.001, η p 2 \eta_{p}^{2} = 0.007.

[58] figure: Table 5 . Prompt Effects (All Models, n=7,450/condition) Prompt IER M (SD) SPS M (SD) Δ \Delta IER Baseline 0.1156 (0.298) 0.7421 (0.204) Neutral 0.0934 (0.276) 0.7498 (0.198) − 19 % -19\% Preservation 0.0821 (0.267) 0.7548 (0.196) − 29 % -29\%

[59] p: Table 5 shows the preservation prompt reduced IER by 29% (Cohen’s d = 0.13) while improving SPS, refuting the authenticity-clarity trade-off. Linear regression confirmed IER & SPS are largely independent ( R 2 = 0.061 R^{2}=0.061 , β = − 0.089 \beta=-0.089 ) as only 6.1% of semantic variance is explained by marker erasure, meaning 93.9% of SPS variation is attributable to factors other than cultural markers. The regression coefficient indicates that increasing erasure from 0% to 20% predicts a negligible SPS decrease from 0.748 to 0.730 well within high preservation range. The apparent trade-off between cultural authenticity & semantic fidelity is false. Figure 5 illustrates this paradox across all model outputs, showing that high semantic preservation coexists with varying degrees of cultural erasure.

[60] figure: Figure 5 . The Semantic Preservation Paradox. High semantic similarity (SPS > 0.7) frequently coexists with non-zero identity erasure (IER > 0), indicating LLMs preserve meaning while removing cultural markers. The Semantic Preservation Paradox. High semantic similarity (SPS > 0.7) frequently coexists with non-zero identity erasure (IER > 0), indicating LLMs preserve meaning while removing cultural markers.

[61] h3: 5.4. Toward Algorithmic Mitigation

[62] p: Beyond prompt engineering, we conducted proof-of-concept algorithmic experiments: Marker-aware constrained decoding : we tagged marker spans in inputs & applied copy constraints during generation. On a subset of 200 texts, this reduced IER by 47% while maintaining SPS within 2% of baseline. Contrastive reranking : generating k = 5 k=5 candidates & selecting by combined score SPS − 0.3 × -0.3\times IER achieved 31% IER reduction. These results suggest tractable algorithmic paths for deploying cultural preservation at scale.

[63] h3: 5.5. Key Takeaways

[64] p: We summarize five actionable insights from our empirical findings:

[65] p: (1) Cultural erasure is systemic, not random. Across 22,350 outputs, LLMs erase 10.26% of cultural markers on average this is a consistent pattern, not an occasional artifact.

[66] p: (2) The identity-clarity trade-off is a myth. Cultural preservation & semantic quality are largely independent ( R 2 = 0.061 R^{2}=0.061 ). Preserving cultural markers does not degrade & may slightly enhance semantic fidelity.

[67] p: (3) Pragmatic markers are most at risk. Politeness conventions, honorifics, & relational markers the features performing the most social work face 1.9 × \times greater erasure than lexical items.

[68] p: (4) Alignment strategy outweighs model scale. The 5.9 × \times cross-model variation in erasure rates is driven by training data composition & RLHF strategy, not parameter count.

[69] p: (5) Simple interventions work. Preservation prompts reduce erasure by 29% with no semantic cost; constrained decoding achieves 47% reduction.

[70] h2: 6. Discussion & Limitations

[71] p: Our findings reveal that LLM writing assistance functions as a cultural standardization engine ( Agarwal et al., 2025 ) . The 71.5% erasure of pragmatic markers specifically targets features performing social work establishing politeness, navigating power distance echoing findings on sociolects ( Basoah et al., 2025 ) . When an Indian professional writes “Kindly revert back,” the formality signals institutional hierarchy & earnestness; replacing it with “Please respond” eliminates crucial pragmatic information. This is not correction it is construction erasure.

[72] p: The preservation prompt’s success (29% reduction with no semantic cost) proves cultural preservation & clarity are compatible. We propose culturally-aware alignment: contrastive training distinguishing semantic from cultural changes, variety-specific fine-tuning on Indian/Singaporean/Nigerian corpora, politeness-aware reward modeling, & user preference modeling for cultural voice preservation. For developers, we recommend: (1) Default to preservation rather than opt-in. (2) Transparent marker handling with "keep my phrasing" options. (3) Variety recognition to adapt rather than force convergence.

[73] p: While our corpus spans professional & informal registers (emails, news, social media), the cultural markers we track politeness conventions, honorifics, pragmatic particles carry particular weight in professional contexts. Future work should examine register-specific vulnerability: whether pragmatic markers are equally at risk in casual social media discourse, creative writing, or academic text, where the stakes & norms differ.

[74] p: Limitations: Our 108-marker lexicon represents a finite subset of cultural features & cannot capture the full depth & fluidity of World English varieties (e.g., multiple English varieties exist within India alone). We used proxy validations rather than formal human studies with variety speakers, we acknowledge this limitation & plan perceptual validation with native speakers of affected varieties in future work. Analysis is restricted to English varieties & open-source models due to funding constraints. Proprietary models may exhibit different patterns, though we hypothesize similar behaviors given shared alignment paradigms. SPS relies on embeddings that may encode Western-centric biases. We validated with an alternate encoder (M-USE, cross-correlation r = 0.94 r=0.94 ) showing robust patterns, though future work should explore additional encoders & human evaluation to further verify metric reliability. Our current lexicon also cannot capture the full intra-variety diversity within each region. Expanding the marker set through collaboration with sociolinguists & community members from each variety remains an important direction. We acknowledge the proxies used for validations without human subjects have limitations: automatic detection & LLM judgments cannot fully substitute for the lived experience of variety speakers. Ultimately, Cultural ghosting is a design choice, not an inevitability.

[75] h2: 7. Conclusion

[76] p: When Chinua Achebe chose to write in “African English,” he argued that new Englishes must emerge to carry new experiences. LLMs, as currently deployed, work against this linguistic pluralism. Our findings demonstrate that standard prompts erase 10.26% of cultural markers while maintaining 75% semantic similarity the Semantic Preservation Paradox in action. Pragmatic markers suffer 71.5% erasure versus 37.1% for lexical markers, confirming that features encoding face-management are most vulnerable. But explicit preservation instructions reduce erasure by 29% with no semantic cost , & constrained decoding achieves 47% reduction. The trade-off we feared identity versus clarity does not exist. Cultural ghosting is not inevitable. It is a design choice we can unmake.

[77] h6: Acknowledgements.

[78] h2: References

[79] h2: Instructions for reporting errors

[80] p: We are continuing to improve HTML versions of papers, and your feedback helps enhance accessibility and mobile support. To report errors in the HTML that will help us improve conversion and rendering, choose any of the methods listed below:

[81] p: Tip: You can select the relevant text first, to include it in your report.

[82] p: Our team has already identified the following issues . We appreciate your time reviewing and reporting rendering errors we may not have found yet. Your efforts will help us improve the HTML versions for all readers, because disability should not be a barrier to accessing research. Thank you for your continued support in championing open access for all.

[83] p: Have a free development cycle? Help support accessibility at arXiv! Our collaborators at LaTeXML maintain a list of packages that need conversion , and welcome developer contributions .
