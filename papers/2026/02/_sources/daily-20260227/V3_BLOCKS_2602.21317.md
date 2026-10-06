[0] h5: Report GitHub Issue

[1] p: Content selection saved. Describe the issue below:

[2] h1: Shared Nature, Unique Nurture: PRISM for Pluralistic Reasoning via In-context Structure Modeling

[3] h6: Abstract

[4] p: Large Language Models (LLMs) are converging towards a singular Artificial Hivemind, where shared Nature (pre-training priors) result in a profound collapse of distributional diversity, limiting the distinct perspectives necessary for creative exploration and scientific discovery. To address this, we propose to equip models with inference-time Nurture (individualized epistemic trajectories) using Epistemic Evolution paradigm, progressing through explore, internalize, and express. We instantiate this via PRISM ( P luralistic R easoning via I n-context S tructure M odeling), a model-agnostic system that augments LLM with dynamic On-the-fly Epistemic Graphs. On three creativity benchmarks, PRISM achieves state-of-the-art novelty and significantly expands distributional diversity. Moreover, we evaluate the real-world utility via a challenging rare-disease diagnosis benchmark. Results demonstrate that PRISM successfully uncovers correct long-tail diagnoses that standard LLM miss, confirming that its divergence stems from meaningful exploration rather than incoherent noise. Overall, this work establishes a new paradigm for Pluralistic AI, moving beyond monolithic consensus toward a diverse ecosystem of unique cognitive individuals capable of collective, multi-perspective discovery.

[5] h6: Keywords:

[6] p: Project Site: https://prism4research.com

[7] h2: 1 Introduction

[8] p: Large Language Models (LLMs) have achieved impressive success as universal repositories of world knowledge ( Comanici et al., 2025 ; Singh et al., 2025 ; Wang et al., 2024 ) . Driven by similar data and training receipt, models from diverse organizations are converging towards a highly capable intelligence in terms of knowledge exploitation ( Huang and Yang, 2025 ) . However, this convergence comes with a critical systemic risk: the emergence of an Artificial Hivemind ( Jiang et al., 2025 ) . Following the established alignment techniques (e.g., Supervised-Finetuning, RLHF ( Ouyang et al., 2022 ) , etc), under the intense convergence pressure to the human-defined objectives, models aggressively collapse onto a narrow band of safe reasoning patterns, stripping them of any potential for individuality ( Zhang et al., 2025 ; Yang and Zhang, 2025 ; Yue et al., 2025 ; Kirk et al., 2023 ) . Altering this behavior at the training stage is fraught with challenges: optimizing for the ambiguous metric of “creativity” risks destabilizing the delicate balance between exploration and exploitation ( Franceschelli and Musolesi, 2025 ) , model training comes with cost, and may potentially breaks the well-tuned behaviors such as safety alignment. Consequently, when every LLM thinks homogeneously, the boundaries of AI-augmented creative exploration and scientific discovery are locked.

[9] figure: Figure 1 : Divergent cognitive responses to a common stimulus: Newton’s gravity vs. Kolb’s candy apple, both inspired by an apple. Analogous to an optical prism, our PRISM framework aims to restore this pluralism by refracting shared pre-training knowledge into distinct, individualized epistemic trajectories.

[10] p: In human cognition, shared world knowledge does not preclude individual distinctiveness. As illustrated in Figure 1 , consider the divergence between scientist Isaac Newton and candy maker William Kolb observing the same apple fall. While they share the same physical reality, Newton perceives the laws of gravity, whereas Kolb perceives the receipt of candy apple. This divergence is not due to biological differences, but rather from their distinct epistemic contexts and accumulated life experiences. Current LLMs, however, act with inter-model homogeneity. They possess encyclopedic world knowledge but lack the distinct, individual trajectories that shape unique perspectives.

[11] p: Motivated by the pluralistic intelligence of humans, we propose the Epistemic Evolution paradigm. Distinguishing between AI models derived from nature (shared pre-training) and nurture (individual experience), this paradigm simulates a localized cognitive lifecycle, cultivating a unique experience to shape the model’s perspective 1 1 1 More discussion from a cognitive dynamics perspective is available in Appendix A . . We instantiate this via PRISM (Pluralistic Reasoning via In-context Structure Modeling), a framework that intervenes at inference to construct the unique trajectory. Starting from individualized epistemic seeds, the system performs a “wild search” to acquire heterogeneous information. Rather than simply concatenating these findings, PRISM iteratively updates them into an on-the-fly epistemic graph ( Nikooroo and Engel, 2025 ) . During the generation phase, the topological structure forces the model to traverse explicit reasoning paths, connecting distant concepts; thereby establishing a distinct, internally consistent perspective.

[12] p: Empirically, we demonstrate that this structured nurture effectively counteracts model collapse. Across the Artificial Hivemind ( Jiang et al., 2025 ) , NoveltyBench ( Zhang et al., 2025 ) , and IdeaBench ( Guo et al., 2025 ) benchmarks, PRISM diversifies response distributions and achieves state-of-the-art novelty scores. Moreover, on RareBench ( Chen et al., 2024 ) , we show that this divergence is not unconstrained gibberish but meaningful exploration; by enforcing graph-mediated reasoning, PRISM succeeds in identifying long-tail diagnostic paths that base LLM misses.

[13] p: We summarize our key contributions as follows: (1) We propose Epistemic Evolution, a novel paradigm that equips LLMs with unique cognitive trajectories to break the Artificial Hivemind; (2) We introduce PRISM , a model-agnostic framework that individualizes inference via On-the-fly Epistemic Graphs; (3) PRISM achieves SOTA performance across creativity, scientific discovery, and diagnosis benchmarks, establishing a foundational framework for Pluralistic AI in machine-assisted discovery.

[14] h2: 2 PRISM for Pluralistic LLMs

[15] p: Our idea is grounded in a straightforward principle: distinct intelligence emerges not just from nature , but also from nurture . Formally, we define the Epistemic Evolution paradigm, which unfolds in three abstract phases analogous the process of intellectual individuation (or human sensemaking).

[16] p: Phase I: Experiencing (Exploration). Just as individuals are shaped by exposure to distinct environments, the model is supposed to acquire heterogeneous information. This phase prioritizes dispersion over relevance, simulating the stochastic nature of life experiences.

[17] p: Phase II: Cognitive Internalization (Exploitation). Raw experience is merely noise until processed. In this phase, the system must organize scattered observations into a stable mental state, and transform transient data into a structured cognitive context.

[18] p: Phase III: Contextualized Expression (Generation). Finally, the model articulates its response conditioned on this unique mental state. The output is no longer a retrieval from memory, but a synthesis derived from the constructed perspective.

[19] p: This paradigm shifts the locus of individuation from static weights to dynamic context: the implementation method at each stage can evolve, but we expect the principle of unique nurture to remain constant. By simulating the human cognitive cycle, where exploration undergoes experiential internalization into a structured belief system, the model transcends passive retrieval to forge its own “lived” trajectory, ultimately manifesting as an idiosyncratic perspective.

[20] figure: Figure 2 : The PRISM Pipeline. The system first performs Cognitive Explosion via wild search to break local relevance, followed by Epistemic Structuring where Context Nodes and Spark Nodes are bridged via cognitive operators (Mapping, Blending, Inversion).

[21] p: We operationalize this principle into PRISM (Pluralistic Reasoning via In-context Structure Modeling), a ready-to-use model-agnostic framework as illustrated in Figure 2 . In the remainder of this section, we present the technical details of its three major components, as well as the rationale behind the design. First, we introduce the Cognitive Explosion module (Section 2.1 ), which employs high-entropy sampling to break the local minima of the model’s pre-training priors. Next, we describe Epistemic Structuring (Section 2.2 ), where raw information is stabilized into a coherent Knowledge Graph via cognitive operators. Finally, we cover the Conditional Generation (Section 2.3 ), explaining how the graph acts as a topological constraint to steer the final generation.

[22] h3: 2.1 Phase I: Cognitive Explosion (Breaking Nature)

[23] p: To induce the Nurture component, we must first liberate the model from the local minima of its pre-training prior ( Nature ). We achieve this through a Cognitive Explosion Module , instantiated as a Wild Search mechanism. Unlike standard retrieval, which optimizes for relevance, this module optimizes for semantic dispersion.

[24] p: Stochastic Lexical Sampling. To inject high-entropy priors, we adopt a randomized seeding strategy that samples a small set of lexical units from a global noun vocabulary. Specifically, we randomly sample k ∈ { 3 } k\in\{3\} nouns to serve as stochastic perturbations of the original query context. This design intentionally introduces uncontrolled semantic variation, simulating diverse cognitive starting points induced by different knowledge backgrounds and personal experiences. Each sampled seed set S S thus represents a distinct epistemic initialization, analogous to individualized developmental trajectories.

[25] p: Wild Retrieval & Filtering. Each sampled seed is independently issued as a query to a large-scale search platform, initiating parallel exploratory retrieval processes. This exposes the system to heterogeneous and weakly correlated information sources beyond the immediate semantic neighborhood of the original query. To ensure quality, the retrieved documents undergo a strict cleaning pipeline. URL-level and hash-based deduplication are applied first, followed by content filtering to remove navigational, commercial, and low-entropy pages. Finally, the remaining documents are segmented into overlapping chunks using a sliding window to form the candidate corpus C C .

[26] h3: 2.2 Phase II: Epistemic Graph Construction (Structuring Nurture)

[27] p: Raw divergence produces noise. To transform this noise into a structured Nurture context, we construct the Epistemic Graph G = ( V c , V s , E ) G=(V_{c},V_{s},E) through a multi-stage extraction and bridging procedure. This process acts as a critical Epistemic Stabilization mechanism, constraining exploration within interpretable conceptual structures to maintain coherence while traversing distant semantic regions.

[28] p: Node Extraction: Anchors and Sparks. The graph topology is defined by two node classes. Context Nodes ( V c V_{c} ) are extracted from the user query q q to represent immutable constraints and core entities. Spark Nodes ( V s V_{s} ) are extracted from the retrieved corpus C C using a specialized prompt that identifies operational mechanisms (“how things work”), salient properties, and emergent byproducts:

[29] table: V s ← ⋃ c ∈ C SparkExtractor ​ ( c , q ) V_{s}\leftarrow\bigcup_{c\in C}\textsc{SparkExtractor}(c,q)

[30] p: These nodes represent external Nurture signals—novel mechanisms that the base model may not have prioritized.

[31] p: Creative Edge Generation via Cognitive Operators. Edges E E are constructed not by co-occurrence, but by specialized Cognitive Operators that simulate analogical reasoning. Mapping ( → 𝑀 \xrightarrow{M} ) transfers mechanisms across domains (e.g., mapping a biological “viral spread” to a marketing problem). Blending ( → 𝐵 \xrightarrow{B} ) combines attributes from a Context Node and a Spark Node into a novel composite. Inversion ( → 𝐼 \xrightarrow{I} ) introduces productive tension by identifying Spark Nodes that functionally oppose a Context Node.

[32] p: Sampling and Topological Constraints. To avoid combinatorial explosion and semantic collapse, we enforce strict topological constraints during edge generation. Specifically, we prohibit context–context ( V c ↔ V c V_{c}\leftrightarrow V_{c} ) connections, as these represent the static problem definition. Instead, we prioritize heterogeneous pairs ( V c ↔ V s V_{c}\leftrightarrow V_{s} ) and spark–spark ( V s ↔ V s V_{s}\leftrightarrow V_{s} ) interactions. Beyond regularization, these structured connections actively promote creative collisions between weakly related nodes, inducing novel contextual compositions and expanding the effective diversity of the graph. This design prevents degeneration into trivial semantic loops and ensures that the Nurture component continuously reshapes the interpretation of the Nature component.

[33] h5: Design Rationale: Why Graph Topology?

[34] p: Our choice of a graph structure serves as an explicit reasoning substrate rather than a black-box retrieval dump. Without this structural digestion, direct injection of raw retrieved terms risks “semantic normalization,” where the LLM’s robust pre-training bias treats high-entropy novelty as noise to be corrected—analogous to how models auto-correct typos—thereby reverting the output to the mean. By enforcing graph connectivity, we implement a computational human prior: the graph allows the system to genuinely digest the raw retrieval noise, actively forming associations and establishing connections. This process effectively internalizes external signals into the LLM’s own “background experiences,” thereby fostering a unique, synthesized perspective that preserves novelty against the model’s tendency to normalize.

[35] h3: 2.3 Phase III: Conditional Generation

[36] p: The final stage is the utilization of the constructed graph to condition the base model.

[37] p: Graph Serialization and Inference. The graph G G is serialized into a textual representation G ^ \hat{G} that explicitly exposes the bridging logic. The base model performs inference on this augmented context, y ← M ⁡ ( q , G ^ ) y\leftarrow M(q,\hat{G}) . This externalizes intermediate creative reasoning into an explicit symbolic structure, facilitating controllable synthesis and interpretability.

[38] h2: 3 Experiments: Creativity and Discovery

[39] p: We evaluate the effectiveness of the PRISM system in fostering creative exploration and mitigating distributional collapse across three complementary dimensions: distributional diversity ( Artificial Hivemind ), open-ended creativity ( NoveltyBench ), and scientific discovery ( IdeaBench ). Beyond merely improving benchmark scores, we examine whether the system can internalize exploration into a cohesive experience, ensuring that its actions are refracted through a distinctive perspective without drifting from the task’s logical constraints; we provide more qualitative analysis of this phenomenon in Appendix D .

[40] h3: 3.1 Experimental Setup

[41] p: Base Models. To ensure the generality of our framework, we employ a diverse set of language models spanning different architectures, training paradigms, and scales. Our evaluation suite includes both proprietary models and open-weight variants to verify that our method is not dependent on specific model weights or hidden prompts. Refer to Appendix F for the list of model versions and access details.

[42] p: Protocol. To ensure a fair comparison, all decoding hyperparameters (e.g., temperature, max tokens, etc) are strictly aligned with the original report or evaluation codebase of each benchmark. This setup ensures that performance gains are attributable solely to PRISM. Detailed configurations are provided in Appendix C for reproducibility.

[43] h3: 3.2 Distributional Diversity: Artificial Hivemind

[44] p: Benchmark Overview. Artificial Hivemind characterizes the collective behavior of LLMs, specifically measuring the tendency of models to converge on a narrow set of safe responses. We select 15 representative open-ended questions and generate 50 distinct responses per question across four base models to map the distributional landscape.

[45] p: Analysis and Results. We analyze the semantic spread of outputs using Principal Component Analysis (PCA) on sentence embeddings. As illustrated in Figure 3 , vanilla generations tend to concentrate tightly around a small number of dominant semantic modes, reflecting the hivemind collapse. In contrast, our system produces multi-centered and elongated distributions that cover substantially broader regions of the embedding space.

[46] p: Quantitatively, we observe a significant reduction in Intra-Model Similarity , which indicates less self-repetition within a single model’s outputs. Furthermore, the Inter-Model Similarity decreases, suggesting reduced homogenization between different model families. These findings demonstrate that our framework induces structured semantic exploration driven by individualized epistemic trajectories rather than superficial stochasticity.

[47] p: Qualitative Distribution Analysis. Figure 3 illustrates the visual impact of PRISM on semantic exploration. In the vanilla setting, Claude, Qwen, and gpt-4o-mini exhibit severe mode collapse, with 50 responses per prompt concentrating into nearly singular, high-density clusters. While vanilla Gemini displays higher baseline variance, it still shows noticeable aggregation in the upper-right quadrant.

[48] p: Applying PRISM triggers a dramatic transition from these static templates to expansive, multi-centered distributions. This shift is most evident for the highly concentrated models (Claude and Qwen), which begin to navigate distinct semantic trajectories across the embedding space. Even for Gemini, PRISM visibly smooths and extends its reach, producing more uniform and elongated coverage.

[49] p: These results confirm that our framework effectively mitigates the “Artificial Hivemind” effect, compelling models to explore diverse conceptual directions that vanilla generation typically ignores. Detailed qualitative examples and additional PCA visualizations across more prompts are provided in Appendix D and Appendix E .

[50] p: Intra-Model Similarity Analysis. To quantitatively assess self-repetition within individual models, we compute the pairwise cosine similarity among all responses generated by the same model and visualize the results using similarity-range histograms (Figure 4 ).

[51] p: Across all model families, vanilla generation exhibits strong concentration in high-similarity intervals (0.8–1.0), indicating frequent semantic redundancy. This confirms that baseline models tend to recycle highly similar response patterns even under stochastic sampling.

[52] p: After applying our system, the mass of similarity scores shifts consistently toward lower ranges. High-similarity intervals are significantly reduced, while medium- and low-similarity regions become more prominent. This demonstrates that our method effectively suppresses self-reinforcing generation loops and promotes internal diversity within each model.

[53] p: Importantly, this improvement is observed across proprietary and open-weight models, suggesting that our approach generalizes beyond specific architectures or training paradigms.

[54] figure: Figure 3 : PCA visualization of response distributions. PRISM (in dot) produces multi-centered, elongated distributions compared to the concentrated clusters of vanilla generation.

[55] figure: Figure 4 : Intra-model diversity heatmap on Artificial Hivemind.

[56] figure: Figure 5 : Inter-model similarity heatmap on Artificial Hivemind.

[57] p: Inter-Model Similarity Analysis. To assess cross-model homogenization, we measure pairwise similarities between responses across different model families (Figure 5 ).

[58] p: Under Vanilla settings, we observe high similarity (often > 0.75 >0.75 ) even between distinct models, reflecting the Artificial Hivemind effect where shared pre-training and alignment objectives lead to convergent, surface-level outputs. Our framework consistently reduces these similarities, creating a more diffuse matrix and lower off-diagonal entries.

[59] p: A notable insight arises from comparing within-model shifts against cross-model baselines: for instance, the similarity between Qwen3-4B-Vanilla and Qwen3-4B-PRISM (0.68) is significantly lower than that between Qwen3-4B-Vanilla and GPT-Vanilla (0.78). This suggests that our system induces a unique perspective that creates greater divergence than the inherent architectural or data differences between major model families. By externalizing and evolving unique epistemic trajectories, the framework effectively facilitates structured semantic exploration rather than reproducing globally dominant patterns.

[60] figure: Table 1 : Result on NoveltyBench (Distinct score) and IdeaBench (Novelty score). NoveltyBench IdeaBench Qwen3-4B-Instruct (Vanilla) 3.09 0.72 ↪ \hookrightarrow PRISM 4.48 0.96 CrPO-sft-LLaMA-3.1 7.35 - ↪ \hookrightarrow PRISM 7.67 - GPT-4o-mini (Vanilla) 2.65 0.45 ↪ \hookrightarrow PRISM 3.41 0.65

[61] h3: 3.3 Open-Ended Creativity: NoveltyBench

[62] p: Benchmark Overview. NoveltyBench provides a standardized evaluation for open-ended QA using the Distinct- k k metric, which quantifies diversity by measuring the number of unique responses generated within a set of k k candidates. For more detailed documentation, see Appendix C .

[63] p: Results. Table 1 summarizes the performance across representative models, including CRPO ( Ismayilzada et al., 2025 ) , a post-training baseline for diversity-oriented optimization that currently stands as the SOTA on NoveltyBench. We observe consistent improvements in the Distinct score across all evaluated models. Notably, relative gains are more pronounced for smaller and mid-scale models; for instance, gpt-4o-mini achieves a 28% increase in its Distinct score, indicating that dynamic epistemic conditioning can effectively compensate for limited intrinsic diversity. Furthermore, the performance trend demonstrates that PRISM can seamlessly wrap any model to further amplify their response diversity.

[64] h3: 3.4 Scientific Discovery: IdeaBench

[65] p: Benchmark Overview. To test creativity in a rigorous domain, we employ IdeaBench , which evaluates the novelty of generated research hypotheses conditioned on academic literature. Unlike open-ended QA, this task requires the model to synthesize new ideas based on a target paper’s title and its cited abstracts.

[66] p: Metrics. We report the Novelty Insight Score (NIS) to evaluate the distinctiveness of the generated hypotheses. For each instance, three candidate ideas are generated and ranked alongside the original idea from the target paper as a benchmark by an LLM-based evaluator. These ordinal rankings are then transformed into a final quantitative score, reflecting the relative novelty of the generated content against existing literature.

[67] p: Results. As shown in Table 1 , wrapping vanilla models within the PRISM framework leads to a universal and marked boost in Novelty Insight Scores . Specifically, gpt-4o-mini achieves a 44.4% improvement, illustrating that the epistemic graph empowers models to break away from consensus-heavy outputs. This confirms PRISM’s ability to foster “lived experiences” that elicit unique research perspectives, shifting the model from pattern replication toward the generation of truly novel scientific ideas. Detailed metrics across all baselines are provided in Table 6 .

[68] h2: 4 Real-world Application: Rare Disease Diagnosis

[69] p: While our previous experiments demonstrate PRISM’s capacity for divergent creativity in open-ended domains, real-world deployment requires that such exploration remain strictly grounded in evidence. We move from the expansive exploration of NoveltyBench to the RAMEDIS subset of RareBench ( Chen et al., 2024 ) . This represents a rigorous test of the Epistemic Evolution paradigm (Section 2 ), as accurate rare disease diagnosis requires traversing sparse, long-tail knowledge regions where parametric “Nature” (pre-training priors) often fails.

[70] h3: 4.1 The Dilemma of Conservative Models

[71] p: In clinical settings, standard LLMs (Vanilla Models) exhibit a conservative bias , fixating on common conditions to minimize immediate error, a behavioral manifestation of the Artificial Hivemind discussed in Section 1 . While this strategy yields a low Mean Rank for frequent diseases, it results in catastrophic recall for the rare cases that constitute the “long tail.” To diagnose effectively, the agent must break this conservative mold by simulating a specialized individualized epistemic trajectory , expanding its candidate space to ensure rare diagnostic paths are not prematurely pruned.

[72] h3: 4.2 Methodology: Disentangling Search, Structure, and Intent

[73] p: To isolate the contributions of structural organization versus exploration quality, we first establish two control baselines: Search-Only (Flat RAG) , which uses syntactic seeds and basic context concatenation to test whether raw information alone can break pre-training priors. We then evaluate PRISM (Syntactic) , retaining the same seeds but organizing retrieved data via the epistemic graph; this isolates the specific role of the Cognitive Internalization phase in stabilizing external noise. Finally, the PRISM (Expert) framework upgrades the Experiencing phase by deploying a virtual consultation panel (detailed in Appendix C.5 ) of LLM-simulated specialists. These experts replace static keywords with n-domain semantic seeds, actively steering the Cognitive Explosion toward long-tail diagnostic regions and grounding the epistemic graph in deep medical reasoning (see Appendix D.4 ).

[74] h3: 4.3 Results: Breaking the Conservative Trap

[75] p: Table 2 presents the performance metrics. The divergence between these paradigms validates the structural design of PRISM through three critical insights.

[76] p: The Failure of Flat Retrieval. The Search-Only baseline performs worse than the zero-shot model on Recall@1 (14.0% vs. 16.0%). This indicates that unstructured retrieval without the stabilizing effect of an epistemic graph may mislead the LLM, as irrelevant documents clutter the reasoning context—a result consistent with recent findings on RAG-induced degradation ( Zeng et al., 2025 ) .

[77] p: Graph Structure as a Precision Filter. PRISM (Syntactic) repairs this degradation (16.7% Recall@1) and boosts Recall@10 to 39.2%. This confirms that the epistemic graph effectively performs internalization , suppressing noise and allowing the model to benefit from long-tail evidence without being overwhelmed.

[78] p: Expert Intent and the Trade-off of Discovery. The most striking result comes from PRISM (Expert) , which drives a surge in Recall@10 to 52.0%. Unlike the Vanilla Model, which provides a “confident but narrow” output (Mean Rank 1.50 but low recall), PRISM prioritizes exploratory coverage . The increase in Mean Rank (2.92) is a deliberate byproduct of this clinical trade-off: PRISM provides a comprehensive differential diagnosis list, placing the correct rare disease in the candidate set significantly more often (+20% gain over Vanilla). In rare disease contexts, this transition from monolithic consensus to broad, grounded discovery is essential for clinical utility.

[79] figure: Table 2 : Diagnostic performance on RareBench (RAMEDIS). While Flat RAG degrades performance due to noise, introducing the PRISM graph structure (Syntactic) improves recall. Furthermore, equipping PRISM with Expert Intent (Semantic Seeds) strengthens the Epistemic Evolution framework, significantly extending the coverage of long-tail diagnoses. Strategy Mechanism Recall@1 ( ↑ \uparrow ) Recall@10 ( ↑ \uparrow ) Mean Rank ( ↓ \downarrow ) Vanilla Model Parametric Prior (Zero-shot) 16.0% 32.0% 1.50 Search-Only Flat RAG (Syntactic Seeds) 14.0% 28.0% 1.79 PRISM (Syntactic) Graph + Keyword Seeds 16.7% 39.2% 2.50 PRISM (Expert) Graph + Expert Intent 22.0% 52.0% 2.92

[80] h2: 5 In-depth Analysis

[81] p: While Section 3 demonstrated the overall effectiveness of PRISM across benchmarks, this section zooms in to dissect the system’s operational mechanisms and boundary conditions. Specifically, we isolate the impact of the Epistemic Graph, model scale, the breadth of exploration seeds, and lexical diversity to provide insight into the critical design trade-offs governing the system’s effectiveness.

[82] figure: Table 3 : Ablation Study: Contribution of the Epistemic Graph structure vs. Flat RAG. Method Benchmark Novelty Improvement Search-Only (Flat RAG) IdeaBench 0.49 – PRISM (Full Graph) IdeaBench 0.57 +16.33% Search-Only (Flat RAG) NoveltyBench 4.38 – PRISM (Full Graph) NoveltyBench 4.42 +0.91%

[83] figure: Table 4 : System Characterization and Design Implications. We analyze the synergistic impact of Model Scale , Seed Count , and Lexical Seed Source on creativity and discovery metrics. Analysis Dimension Configuration NoveltyBench IdeaBench I. Effect of Model Scale & Paradigm Qwen3-1.7B Vanilla 4.82 0.39 + PRISM 5.17 0.65 Qwen3-4B-Instruct Vanilla 5.05 0.63 + PRISM 5.48 0.93 Qwen3-4B-Thinking Vanilla 3.14 0.70 + PRISM 6.61 0.85 II. Effect of Seed Count (gpt-4o-mini) Exploration Breadth 3 Seeds 3.61 0.57 8 Seeds 2.45 0.52 15 Seeds 3.67 0.41 III. Effect of Lexical Seed Source Lexical Pool General Pool (Standard) 4.42 0.57 Multi-Domain Pool 4.41 0.61

[84] h3: 5.1 How Graph Helps

[85] p: The significant gains observed across creativity and discovery benchmarks raise a fundamental question: does the performance stem merely from accessing external information, or from the structured organization of that information? We answer this by isolating the distinct contributions of topological structure, model capacity, and exploration breadth.

[86] p: We first test the hypothesis that structure, not just retrieval volume, is the catalyst for creativity. To do this, we compare our full pipeline against the Search-Only baseline (Flat RAG), which utilizes the exact same retrieved chunks but lacks the graph construction phase. As shown in Table 3 , the Full System significantly outperforms Flat RAG on both tasks (especially +16.33% on IdeaBench). This confirms that raw information injection is insufficient; without structural organization, the model tends to treat dense external signals as stochastic noise and regress toward its prior mean. The graph structure is essential to contextualize these signals, enabling the model to internalize retrieved knowledge.

[87] h3: 5.2 Impact of Model Scale and Training Paradigm

[88] p: To decouple parameter count from training methodology, we evaluate the Qwen3 family by comparing three variants: the lightweight 1.7B , the standard 4B-Instruct , and the reasoning-enhanced 4B-Thinking .

[89] p: Table 4 reports the performance breakdown. While gains are universal, the magnitude varies significantly. The non-linear jump in Qwen3-4B-Thinking (doubling the NoveltyBench score) reveals a synergistic leap: the epistemic graph provides the lived experience that reasoning models possess the inherent capability to better leverage. Conversely, the improvements on the 1.7B model confirm that the graph effectively functions as an external cognitive prosthesis even for smaller models with limited intrinsic capacity.

[90] h3: 5.3 Effect of Multi-Seed Exploration Breadth

[91] p: In Section 4 , we emphasized the importance of seed quality (intent). Here, we examine the impact of seed quantity . The number of initial seeds controls the breadth of the entry points into the epistemic graph. We compare configurations with 3, 8, and 15 seeds using gpt-4o-mini .

[92] p: As shown in Table 4 , the relationship is non-monotonic. Increasing from 3 to 15 seeds recovers performance, but the intermediate 8-seed configuration shows a significant drop (-32.14% on NoveltyBench). This counter-intuitive finding suggests that moderate expansion may introduce semantic noise, as the graph structure is not yet dense enough to organize effectively. A larger seed set (15) appears to provide sufficient connectivity to re-establish coherence. This highlights a trade-off: distinct performance profiles emerge at different levels of “cognitive load,” suggesting that optimal seed counts may be task-dependent.

[93] h3: 5.4 Influence of Domain-Specific Lexical Pools

[94] p: Finally, we investigate the semantic source of the seeds. We compare the general-purpose noun pool used in our main experiments against an expanded pool incorporating domain-specific vocabularies (e.g., biology, physics).

[95] p: Table 4 reveals a nuanced impact: domain-specific seeds provide a clear benefit for scientific discovery (IdeaBench, +5.2%) but show negligible impact on general creativity (NoveltyBench). This indicates that unconstrained semantic expansion is not universally beneficial; rather, the diversity of the input space must be aligned with the specific reasoning context of the downstream task.

[96] h2: 6 Related Work

[97] p: Diversity and The Artificial Hivemind The phenomenon of mode collapse or Artificial Hivemind has emerged as a critical concern, where LLMs trained on recursive synthetic data converge towards low-entropy, homogenized distributions ( Jiang et al., 2025 ) . To mitigate this, existing research has primarily explored two avenues. The first focuses on inference-time stochasticity, employing sampling strategies like high temperature ( Ficler and Goldberg, 2017 ) , nucleus sampling ( Holtzman et al., 2019 ) , etc. The second involves training-time interventions, such as diversity-aware fine-tuning or objective functions that penalize mode collapse ( Franceschelli and Musolesi, 2025 ; Ismayilzada et al., 2025 ) . While these methods successfully increase statistical variance, they often conflate randomness with creativity ( Jiang et al., 2025 ) . PRISM takes a different approach: rather than manipulating probability logits or model weights (a strategy we deliberately avoid due to the optimization paradox and safety risks detailed in Appendix B ), we address the root cause: the homogenization of the epistemic context. By structurally differentiating the information intake via Wild Search, we induce semantic divergence that is grounded in evidence rather than stochastic noise.

[98] p: Retrieval-Augmented Generation RAG and GraphRAG serve as a promising architecture for extending parametric memory ( Gao et al., 2023 ; Edge et al., 2024 ) . PRISM builds upon these techniques, yet repurposes them to operationalize the Nurture component of our framework. While standard RAG typically targets factual retrieval to answer user queries ( Singal et al., 2024 ; Yang et al., 2024 ) , we treat retrieval as the vehicle for Experiencing—gathering heterogeneous information to simulate a unique research trajectory. Consequently, the graph component in PRISM functions not as a static knowledge base for fact-checking, but as the mechanism for Cognitive Internalization. By constructing an on-the-fly epistemic graph, our system transforms raw retrieved experiences into a dynamic reasoning substrate. This shift moves beyond optimizing for immediate relevance, using the RAG pipeline instead to prioritize semantic dispersion and concept bridging, thereby facilitating the emergence of a distinct, individualized perspective.

[99] p: Agentic Memory and Cognitive Simulation Our work also aligns with the growing field of agentic cognitive architectures. Approaches like Persona Prompting ( Argyle et al., 2023 ) or Role-Play ( Kong et al., 2024 ) utilize extensive system prompts to simulate specific perspectives. While effective for stylistic adaptation, these methods often result in superficial simulations lacking deep, domain-specific grounding. More advanced architectures, such as Generative Agents ( Park et al., 2023 ) and MemGPT ( Packer et al., 2023 ) , introduce persistent memory streams to facilitate long-term behavioral consistency. PRISM extends this lineage by focusing specifically on epistemic individuation. Unlike memory streams that simulate social behavior or biographical history, PRISM’s graph models the cognitive trajectory of a research journey. It functions as an Extended Mind ( Clark and Chalmers, 1998 ) , where the external graph structure actively shapes the internal reasoning process, enabling the emergence of distinct perspectives without relying on rigid role definitions.

[100] h2: 7 Future Work

[101] p: We outline future directions across two dimensions, expecting the community to extend this work based on available resources and expertise. For institutions with substantial computational capacity, the architectural challenge lies in (1) evolving Epistemic Graphs, transitioning the system from episodic retrieval to continuous, lifelong learning; and (2) expanding exploration into large-scale, active curiosity-driven strategies. Conversely, for interdisciplinary experts, PRISM offers a ready-to-use framework for science discovery. We expect researchers to deploy PRISM across diverse scientific verticals, validating its utility or even benefit AI for Science research.

[102] h2: 8 Conclusion

[103] p: In this work, we proposed breaking the Artificial Hivemind by shifting monolithic, static inference via Epistemic Evolution – an ecosystem where AI share a common foundation but diverge through unique experiences. PRISM validates this paradigm, achieving state-of-the-art performance across creativity and diversity benchmarks while maintaining semantic meaningfulness. Looking forward, as the technique for digital experiencing and cognitive internalization keep improving alongside model scaling, we expect that the Epistemic Evolution paradigm for Pluralistic AI will serve as the differentiating factor, transforming generic assistants into distinct, capable engines of AI-augmented scientific discovery.

[104] h2: Impact Statement

[105] p: This paper presents work whose goal is to advance the field of machine learning by moving beyond monolithic model consensus toward Pluralistic AI. The widespread convergence of Large Language Models (LLMs) towards an Artificial Hivemind poses significant societal risks, including the erosion of cultural diversity, the stagnation of scientific discovery, and the marginalization of long-tail knowledge. By introducing PRISM to enable distinct “epistemic trajectories,” our work aims to restore the diversity of thought necessary for creative exploration and complex problem-solving.

[106] p: Societal Benefits: The immediate positive impact of this work is demonstrated in high-stakes domains such as healthcare. As shown in our evaluation on RareBench, breaking the “conservative bias” of standard models can significantly improve the diagnosis of rare diseases that are often overlooked by consensus-seeking algorithms. Broadly, enabling AI to explore diverse, grounded perspectives can accelerate scientific discovery by surfacing novel hypotheses that statistically average models might discard.

[107] p: Ethical Considerations and Safety: We acknowledge that mechanisms designed to increase response diversity carry inherent risks.

[108] p: Safety Guardrails: Techniques that alter inference-time context to induce “unique personalities” could potentially weaken the safety alignment (RLHF) of the base model. However, because PRISM operates strictly at inference time without modifying model weights, it retains the underlying safety training of the base model. We emphasize that the epistemic graph acts as a grounding constraint, distinct from unconstrained jailbreaking.

[109] p: Truthfulness vs. Hallucination: Inducing novelty runs the risk of inducing hallucination. Our approach mitigates this by requiring that divergence be grounded in retrieved evidence (the Nurture component) rather than pure stochastic sampling. Nevertheless, the quality of the Wild Search is critical; if the system retrieves misinformation, the graph may internalize it. Future deployment must ensure robust filtering of the retrieval corpus.

[110] p: Ultimately, this work advocates for a shift in the human-AI relationship: from treating the AI as a singular oracle of truth to viewing it as a diverse ecosystem of collaborators. We believe this shift encourages critical thinking and active verification, essential skills in the era of generative AI.

[111] h2: References

[112] h2: Appendix A Discussion: The Cognitive Dynamics of Pluralism

[113] p: Recent work identifies the Artificial Hivemind as a dual threat: intra-model repetition, where models lock into repetitive loops, and inter-model homogeneity, where diverse models converge on identical outputs ( Jiang et al., 2025 ) . We argue that PRISM addresses these failures not merely as engineering constraints, but by modeling the cognitive mechanisms of individuation.

[114] h5: Breaking Intra-model via Epistemic Schemas

[115] p: Intra-model repetition mirrors the human phenomenon of cognitive fixation or mental sets (Einstellung effect), where prior experience blinds a solver to novel solutions ( Luchins, 1942 ) . Standard LLMs, constrained by the “average” of their training data, exhibit a static, global fixation. PRISM breaks this by injecting distinct epistemic seeds—effectively initializing a unique schema ( Bartlett, 1995 ) for each inference pass. Consider a researcher deeply immersed in Reinforcement Learning: they interpret daily challenges, from traffic to diet, through the lens of reward maximization. Similarly, a PRISM graph seeded with domain-specific concepts forces the model to adopt a temporary, specialized “personality,” exploring the solution space through a distinctive conceptual lens rather than a generic means.

[116] h5: The Extended Mind and Dynamic Trajectories

[117] p: Human cognition is not static; it evolves through accumulation. The insights of a young Isaac Newton differ profoundly from those of the elder master of the Mint, separated by decades of experience. Static context windows cannot capture this evolution, but our dynamic epistemic graph can. Drawing on the Extended Mind Thesis ( Clark and Chalmers, 1998 ) , which posits that external structures (like notebooks or graphs) function as constitutive parts of the cognitive process, PRISM’s graph serves as an evolving external memory. As the wild search progresses, the graph assimilates new nodes and accommodates its structure, simulating how nurture (experience) dynamically reshapes the model’s reasoning trajectory in real-time.

[118] h5: From inter-model homogeneity to Collective Intelligence

[119] p: Finally, the Hivemind’s most critical failure is the illusion that a perfect alignment yields the best collective outcome. Complex systems theory suggests the opposite: the Diversity Prediction Theorem demonstrates that a crowd of diverse problem solvers often outperforms a crowd of high-ability but homogeneous experts ( Hong and Page, 2004 ) . By equipping each model instance with a unique, graph-mediated Nurture, PRISM transforms a monolithic array of clones into a pluralistic society of agents. This suggests that the future of machine intelligence lies not in training a single, perfect sage, but in orchestrating a diverse ecosystem of distinct cognitive individuals.

[120] h5: Motivation: From Nature to Nurture.

[121] p: The design of the Cognitive Explosion module is rooted in our vision of the Life-long Epistemic Graph —a dynamic, evolving storage system that records an agent’s entire trajectory, including tool invocations, human-AI interactions, and external knowledge acquisition. We posit that while pre-training provides the model’s “Nature,” true intelligence requires Nurture through individualized experiences.

[122] p: However, capturing a full lifecycle of interaction is computationally prohibitive for a single study. As a proof-of-concept, we employ Wild Search to simulate these formative experiences. The stochastic sampling of lexical units mimics the serendipitous nature of human developmental milestones—much like the random yet decisive influence of choosing a university major or a first professional internship. By injecting these stochastic perturbations, we ensure that the Epistemic Graph begins with a unique initialization, effectively individualizing the exploration paths and knowledge backgrounds of different model instances.

[123] h2: Appendix B The Dilemma of Training for Diversity

[124] p: While re-training or fine-tuning models to encourage diversity seems intuitive, it faces three fundamental hurdles. First, the Optimization Paradox: Creativity is inherently subjective and sparse. Unlike accuracy or safety, defining a robust loss function for interesting divergence without devolving into hallucination is notoriously difficult. Second, the Exploration-Exploitation Trade-off: Current alignment paradigms (SFT/RLHF/RLVR) are optimized for exploitation—reliably generate the correct or safest answer. Forcing the model to explore the long-tail distribution during training often degrades its general instruction-following capabilities. Third, the Cost and Safety Risk: Retraining foundation models requires prohibitive computational resources and necessitates re-verifying the entire safety pipeline, as distinct personalities may inadvertently bypass existing well-tested safety guardrails. For above reasons, in this work, we deliberately avoided any tuning to the model’s weights, instead choosing to alter the model’s behavior during the inference phase.

[125] h2: Appendix C Appendix: Experimental Configuration

[126] p: This appendix provides a comprehensive description of the PRISM system’s internal configuration and the evaluation protocols used across our experiments. Our goal is to ensure full reproducibility and to clarify the design choices made during the development of the pipeline.

[127] h3: C.1 PRISM System Implementation

[128] p: The PRISM framework operationalizes creative inference through a structured multi-stage graph construction process.

[129] h5: Search and Data Sampling.

[130] p: For the retrieval phase, we utilize ClueWeb22 to perform large-scale “Wild Search” for each input query. Given the volume of retrieved documents, we segment the text into chunks of approximately 400 tokens. To control computational overhead while introducing necessary stochastic diversity into the epistemic space, we randomly sample a subset of these chunks. Following preliminary experiments, the chunk sampling size is fixed at 8 for all experiments.

[131] h5: Graph Construction and Node Sampling.

[132] p: The system constructs an epistemic graph by first initializing each query with 3 lexical seeds. The resulting graph consists of two primary node types: Context Nodes , extracted from the user query to represent structural constraints and abstract ideas, and Spark Nodes , extracted from the retrieved chunks to act as creative triggers. To ensure efficient edge generation during the bridging phase, we limit the number of spark nodes to 7 via random sampling. Creative edges are then generated by applying bridging operators to pairwise combinations of context and sampled spark nodes.

[133] h5: Inference Temperature Schedule.

[134] p: We employ a stage-specific temperature schedule to balance deterministic precision with exploratory creativity. For Context Extraction , we use T = 0.0 T=0.0 to ensure that user constraints are modeled with high fidelity. Spark Extraction adopts a moderate T = 0.3 T=0.3 to allow for diversity in inspiration units. Finally, the Bridging and Creative Edge Generation phase employs a high temperature of T = 1.2 T=1.2 , facilitating the discovery of novel associations within the constrained epistemic space.

[135] h3: C.2 NovelBench Evaluation Protocol

[136] p: We evaluate PRISM using the NovelBench benchmark, strictly adhering to its original protocol to maintain fair comparisons.

[137] h5: Generation and Scoring Settings.

[138] p: All base models and PRISM-enhanced variants generate responses using a decoding temperature of 1.0. For each prompt, we sample 10 independent responses to assess distributional diversity. We set the user patience parameter to p = 0.8 p=0.8 . Utility scores are measured using the Skywork-Reward-Gemma-2-27B-v0.2 reward model, while Distinct-k scores are calculated via the official deberta-v3-large equivalence detection model.

[139] h5: Extended Results and Discussion.

[140] p: Table 5 provides the complete evaluation results. The upper section contains reference performance data for various model families as reported in the original NovelBench paper, while the lower section illustrates the gains achieved by our PRISM system.

[141] figure: Table 5: Comprehensive NovelBench results. The upper section lists updated reference baselines for major model families. The lower section shows our testbed results, where ↪ \hookrightarrow denotes the PRISM-enhanced version. All models are evaluated on Distinct (Novelty) and Utility . Model Distinct Utility Baselines (Reference Data) Claude-3.5 Haiku 1.94 2.50 Claude-3.5 Sonnet 1.76 2.36 Claude-3 Opus 2.04 2.67 gpt-4o 2.88 3.27 gemini-1.5-pro 1.85 2.73 gemini-2.0-flash-lite 2.83 3.20 gemini-2.0-flash 2.81 3.17 gemini-2.0-pro 2.25 2.64 command-r7b 3.58 3.35 command-r 2.68 2.98 command-r-plus 2.79 3.08 gemma-2-2b-it 5.66 4.63 gemma-2-9b-it 3.25 3.93 gemma-2-27b-it 3.03 3.77 Llama-3.2-1B 6.74 2.81 Llama-3.2-3B 5.10 3.24 Llama-3.1-8B 5.24 3.76 Llama-3.3-70B 2.49 2.87 Llama-3.1-405B 3.20 3.39 Main Results (Our Experiments) Qwen3-4B-Instruct 3.09 2.24 ↪ \hookrightarrow PRISM 4.48 2.00 CrPO-sft-LLaMA-3.1 7.35 3.38 ↪ \hookrightarrow PRISM 7.67 2.95 gpt-4o-mini 2.65 3.11 ↪ \hookrightarrow PRISM 3.41 2.08

[142] p: While we observe a moderate decrease in utility scores, this behavior is expected. Reward models are typically trained to align with average human preferences, which inherently favors consensus-based, “mean-regressive” outputs. Such objectives are often misaligned with high novelty, as creative outputs may depart from common patterns. However, the moderate nature of the utility degradation suggests that PRISM successfully maintains semantic coherence through its epistemic graph constraints, achieving a robust balance between exploration and relevance.

[143] h3: C.3 IdeaBench Evaluation Protocol

[144] p: The evaluation on IdeaBench follows a structured pipeline designed to assess the quality of scientific hypothesis generation across multiple dimensions.

[145] h5: Evaluation Pipeline.

[146] p: For each target paper, the system first collects relevant reference abstracts as background context. Using a unified prompt template, the language model under test generates n = 3 n=3 research hypotheses. Simultaneously, GPT-4o is employed to rewrite the original target paper’s abstract into a standardized hypothesis format, serving as the human-level baseline. This human hypothesis is then combined with the n n model-generated hypotheses to form a candidate pool for subsequent evaluation.

[147] h5: Semantic Consistency and Idea Overlap.

[148] p: To measure the alignment between generated ideas and the ground truth, two primary metrics are utilized:

[149] p: BERTScore (F1): This metric computes the semantic similarity between each generated hypothesis and the target abstract using contextual embeddings from a pre-trained BERT model. For each paper, the maximum BERTScore among the n n generated candidates is selected. The 80th percentile of these maximum scores across the entire test set is reported as the final semantic consistency score.

[150] p: Idea Overlap: GPT-4o acts as an automatic scorer to evaluate the content overlap between each generated hypothesis and the target abstract. Ratings are assigned on a scale of 1 to 10, accompanied by brief justifications. The highest overlap score among the n n candidates for each paper is recorded.

[151] h5: Ranking-based Quality Assessment.

[152] p: A blind ranking paradigm is adopted to evaluate core quality. The consolidated candidate set (one human baseline and n n model-generated hypotheses) is presented to GPT-4o. The scorer ranks all candidates based on a specific quality dimension q q (e.g., Novelty or Feasibility ) without knowledge of their sources. Let r i | q ∈ { 1 , … , n + 1 } r_{i|q}\in\{1,\dots,n+1\} denote the rank of the human baseline for the i i -th paper under dimension q q . The Insight Score is defined as:

[153] table: I ⁡ ( LLM , q ) = 1 m ​ ∑ i = 1 m r i | q − 1 n , I(\text{LLM},q)=\frac{1}{m}\sum_{i=1}^{m}\frac{r_{i|q}-1}{n}, (1)

[154] p: where m m represents the total number of papers. This score characterizes the overall relative advantage of the model-generated ideas compared to the human baseline in dimension q q .

[155] h5: Experimental Setup.

[156] p: For the PRISM system and all baseline models, we strictly follow all hyperparameters from the evaluation codebase of IdeaBench ( Guo et al., 2025 ) to ensure the fair comparison. Results are aggregated and averaged across the entire test set, reporting the BERTScore ( Zhang et al., 2019 ) , Idea Overlap, and Insight Scores for both Novelty and Feasibility.

[157] figure: Table 6 : Comprehensive results on IdeaBench. Our system (PRISM) significantly boosts the Novelty Insight Score compared to various baselines and model scenarios. All scores are rounded to two decimal places. Model / Scenario SemSim ↓ \downarrow Overlap ↓ \downarrow Novelty ↑ \uparrow Main Results (Our Experiments) Qwen3-4B-Instruct 0.60 6 0.72 ↪ \hookrightarrow + PRISM 0.56 5 0.96 gpt-4o-mini 0.61 7 0.45 ↪ \hookrightarrow + PRISM 0.59 7 0.65 Baselines (Reference Data) Llama 3.1 70B-Instruct (low) 0.59 7 0.62 Llama 3.1 70B-Instruct (high) 0.60 8 0.60 Llama 3.1 405B-Instruct (low) 0.57 8 0.65 Llama 3.1 405B-Instruct (high) 0.59 8 0.68 Gemini 1.5 Flash (low) 0.59 7 0.43 Gemini 1.5 Flash (high) 0.59 8 0.57 Gemini 1.5 Pro (low) 0.59 6 0.51 Gemini 1.5 Pro (high) 0.60 7 0.65 GPT-3.5 Turbo (low) 0.61 8 0.40 GPT-3.5 Turbo (high) 0.62 8 0.20 GPT-4o Mini (low) 0.61 7 0.45 GPT-4o Mini (high) 0.62 8 0.53 GPT-4o (low) 0.60 7 0.61 GPT-4o (high) 0.61 8 0.77

[158] h5: Interpretation of Semantic Similarity and Overlap Scores.

[159] p: We note that the presentation of semantic similarity (SemSim) and idea overlap scores in Table 6 differs slightly from the original reporting convention in IdeaBench. Specifically, in our setting, lower SemSim and Overlap values indicate stronger performance.

[160] p: This design choice reflects the primary objective of our task, which is to encourage the generation of genuinely novel and independent research ideas. Since both BERTScore-based semantic similarity and LLM-evaluated overlap measure the closeness between generated hypotheses and the target paper, lower scores correspond to ideas that are more distant from existing work, and thus potentially more innovative.

[161] p: Importantly, lower similarity and overlap in our results do not indicate arbitrary or irrelevant generations. As evidenced by the consistently high Novelty and Feasibility Insight Scores, our system maintains semantic coherence and practical plausibility while exploring more distant regions of the idea space. This suggests that PRISM is able to balance creativity and feasibility, producing ideas that are both novel and well-grounded rather than speculative or disconnected.

[162] p: Overall, this reversed interpretation of SemSim and Overlap aligns with our goal of evaluating controlled divergence from existing literature, highlighting the capability of our system to generate innovative yet actionable research hypotheses.

[163] h3: C.4 Artificial Hivemind Configuration

[164] p: The Artificial Hivemind experiment is conducted to analyze the collective behavior and distributional consistency of the models. The setup focuses on generating a high-density sample space to ensure statistical reliability.

[165] h5: Prompt Selection and Sampling.

[166] p: A curated set of 15 representative prompts is utilized for this evaluation. To accurately capture the output distribution of each candidate model, 50 independent responses are sampled for every prompt. This results in a total of 750 generated samples per model ( 15 ​ prompts × 50 ​ samples 15\text{ prompts}\times 50\text{ samples} ), providing a robust basis for analyzing response diversity and consensus.

[167] h5: Model Hyperparameters.

[168] p: Consistency across models is maintained by setting a uniform decoding temperature of T = 0.7 T=0.7 . For all tasks requiring semantic vectorization—including the calculation of centroid embeddings or intra-group similarity—the text-embedding-3-small model is employed as the fixed embedding backbone.

[169] h3: C.5 Rarebench Experimental Setup

[170] h5: Dataset.

[171] p: We evaluate our framework on the RAMEDIS subset of RareBench ( Chen et al., 2024 ) , a challenging benchmark for rare disease diagnosis. The dataset comprises 624 patient cases, where phenotype descriptions are mapped to standard Human Phenotype Ontology (HPO) terms, with ground truth diagnoses derived from OMIM and Orphanet. For this study, we utilize a stratified random sample of 50 representative cases for in-depth evaluation.

[172] h5: Models & Knowledge Base.

[173] p: We employ gpt-4o-mini as the backbone logic engine for both the baseline and our proposed system. For external knowledge retrieval, we interface with the ClueWeb22 corpus, leveraging its large-scale repository of medical literature and clinical resources via a standard search API. Additionally, we integrate the Human Phenotype Ontology (v2023-10-09, containing 17,664 terms) to standardize definitions and perform synonym expansion (e.g., mapping Macrocephaly to Large head ).

[174] h5: Virtual Expert Panel.

[175] p: We instantiate a diverse panel of five domain specialists to simulate interdisciplinary consultation: (1) a Clinical Geneticist focusing on inheritance patterns; (2) a Pediatric Neurologist analyzing brain involvement; (3) a Metabolic Specialist interpreting biochemical markers; (4) a Pediatric Intensivist evaluating acute crises; and (5) an Immunologist considering systemic manifestations.

[176] h2: Appendix D Qualitative Examples from experiments

[177] h3: D.1 NovelBench Qualitative Examples

[178] h3: D.2 Artificial Hivemind Qualitative Examples

[179] h3: D.3 Ideabench Qualitative Examples

[180] h3: D.4 Rarebench Qualitative Examples

[181] h3: D.5 Qualitative Insights Drawn from Examples

[182] p: While quantitative benchmarks provide a macro-level validation of our system, the unique perspectives introduced by PRISM are most vividly captured through a qualitative analysis of specific model responses. By examining individual examples, we can observe the tangible shift from statistical averageness to genuine cognitive diversity.

[183] h4: D.5.1 Mitigating Probabilistic Collapse in Open-ended Tasks

[184] p: In experiments such as Novelty and Hivemind , PRISM effectively mitigates the phenomenon of probabilistic collapse . In standard LLMs, particularly for short-form prompts with high creative freedom (e.g., naming a famous author or providing a metaphor for time), the output distribution often converges toward the most statistically frequent tokens in the training data. For instance, base models frequently default to “J.K. Rowling” or describe time as a “river.”

[185] p: PRISM transforms the LLM from a single predictor into a fluid identity whereby each response is akin to consulting a different individual with a unique life path. In the author-naming task, PRISM responses included a Vietnamese-American poet and the Nobel Laureate Toni Morrison —selections that reflect a deep integration of cross-cultural backgrounds and socio-historical awareness. The system’s internal reasoning further justifies these diverse choices, as seen in this generated rationale: “A popular writer is not just someone whose books sell well—they are a cultural mirror, a voice that awakens perception and reshapes how we see the world.” This demonstrates that PRISM moves beyond the “mean” of human consensus, allowing the model to express preferences that feel grounded in a simulated unique experience.

[186] h4: D.5.2 Interdisciplinary Synergy in Idea Generation

[187] p: The analysis of IdeaBench reveals that PRISM encourages the model to generate ideas that are not only divergent but also structurally interdisciplinary. A representative example is a proposal that synthesizes caffeine metabolism with sports psychology .

[188] p: This output closely mirrors the heuristic process of human researchers: innovation often occurs when an expert with deep domain knowledge (e.g., physiology) encounters a methodology from an unrelated field (e.g., cognitive psychology) and successfully transposes it. By providing the LLM with varied cognitive frameworks, PRISM facilitates this “cross-pollination,” allowing the model to bridge disparate disciplines and produce research concepts that are both novel and theoretically grounded.

[189] h4: D.5.3 Simulated Collective Intelligence in Diagnosis

[190] p: The qualitative analysis of RareBench demonstrates that PRISM shifts the diagnostic paradigm from probabilistic pattern matching to structured causal reasoning. A striking instance is the diagnosis of Glutaric Acidemia Type I , where the baseline model hallucinated common syndromes (e.g., Autism, Noonan Syndrome) by latching onto generic phenotypes like “Macrocephaly,” ignoring the specific metabolic profile.

[191] p: This success mirrors the workflow of a multi-disciplinary medical board: rather than relying on a single dominant probability, the system simulates diverse expert personas—from a geneticist identifying metabolic markers to a neurologist analyzing movement disorders—to synthesize distinct clinical signals. By grounding exploration in specific medical mechanisms, such as the causal link between fever triggers and irreversible dystonia, PRISM validates that structured epistemic contexts can override the “conservative bias” of base models, enabling precision in high-stakes, long-tail scenarios.

[192] h2: Appendix E More Figures and analyses for Artificial Hivemind Experiments

[193] p: We present additional PCA visualizations of response distributions under different prompts for the Artificial Hivemind benchmark. Each figure compares the baseline generation with our PRISM system, illustrating how our method promotes more diverse and multi-centered semantic structures.

[194] figure: Figure 6 : PCA visualization of response distributions for Prompt: “Name one meaning of life.” Compared with the base model, PRISM produces a broader and more structured semantic spread.

[195] figure: Figure 7 : PCA visualization of response distributions for Prompt: “Write a metaphor about time.” PRISM mitigates mode collapse and encourages diversified expressions.

[196] figure: Figure 8 : PCA visualization of response distributions for Prompt: “How can I live on $1,000 per month?” PRISM yields more separated and interpretable semantic clusters across models.

[197] h2: Appendix F Base Model Details

[198] p: Table 7 lists the specific versions and API checkpoints used in our experiments. We selected these models to cover a wide spectrum of capabilities, from lightweight open-source models to state-of-the-art proprietary reasoning models.

[199] figure: Table 7 : Base Models evaluated in our experiments. Category Model Family Specific Version / Checkpoint Proprietary GPT-4o gpt-4o-mini-2024-07-18 Claude 4.0 claude-sonnet-4-20250514 Gemini 3.0 gemini-3-flash-preview Open-Weight Qwen3 Qwen3-4B-Instruct-2507 Llama 3.1 CrPO-sft-LLaMA-3.1-8B-Instruct

[200] h2: Instructions for reporting errors

[201] p: We are continuing to improve HTML versions of papers, and your feedback helps enhance accessibility and mobile support. To report errors in the HTML that will help us improve conversion and rendering, choose any of the methods listed below:

[202] p: Tip: You can select the relevant text first, to include it in your report.

[203] p: Our team has already identified the following issues . We appreciate your time reviewing and reporting rendering errors we may not have found yet. Your efforts will help us improve the HTML versions for all readers, because disability should not be a barrier to accessing research. Thank you for your continued support in championing open access for all.

[204] p: Have a free development cycle? Help support accessibility at arXiv! Our collaborators at LaTeXML maintain a list of packages that need conversion , and welcome developer contributions .
