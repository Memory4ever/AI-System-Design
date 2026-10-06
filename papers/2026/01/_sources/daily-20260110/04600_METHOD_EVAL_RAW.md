On the Limitations of Rank-One Model Editing in Answering Multi-hop Questions (https://arxiv.org/html/2601.04600v1)
citeturn26874view0 [wordlim: 200] Crawled: today; Content type: text/html; Source: open({"ref_id":"https://arxiv.org/html/2601.04600v1","lineno":100}); Total lines: 272
L51: This demand has resulted in growth of Knowledge Editing (KE), in which Rank-One Model Editing (ROME) (cite33†Meng et al. 2023 ) is a representative technique. It can inject single-fact knowledge by updating the weights of one single MLP layer, outperforming other popular methods like fine-tuning and in-context learning (cite33†Meng et al. 2023 ; cite34†Hase et al. 2023 ).
L52: Figure 1: Trade-off between MQuAKE multi-hop question answering accuracy and language score on COUNTERFACT single-hop questions. Square marker denotes the original ROME editing with layer selected by causal tracing, while circles show redundant-editing configurations with layer combinations in brackets.
L53: ROME works well on single-step knowledge tasks but struggles with complex questions like multi-hop reasoning (cite35†Zhong et al. 2023 ). cite36†Biran et al. (2024) demonstrate that successful multi-hop reasoning depends critically on the relative layer positions where hop knowledge is stored. Given cite34†Hase et al. (2023) ; cite37†Liu et al. (2025) ’s finding that layer depth minimally impacts ROME’s editing efficacy, we investigate how inserting knowledge at varying layer depths affects multi-hop reasoning.
L54: Our research shows that ROME has three significant shortcomings in multi-hop tasks: (1) The "hopping-too-late problem" (cite36†Biran et al. 2024 ) occurs when hop-2 knowledge is stored in earlier layers than hop-1 knowledge, breaking the model’s internal reasoning chain. (2) Generalization capability drops rapidly when editing deeper layers, making edits more sensitive to question phrasing. (3) Overfit to edited knowledge regardless of the context question.
L55: cite38†Image: Refer to caption Figure 2: Redundant Editing strategy: insert copies of a same knowledge into multiple layers.
L56: To address the two problems, we propose Redundant Editing, which injects the same knowledge into several MLP layers with different depths, as illustrated in Figure cite39†2 . On the MQuAKE (cite35†Zhong et al. 2023 ) 2-hop questions (2HQ) dataset, our strategy improves multi-hop question accuracy by 15.5 percentage points, a 96% increase over single-layer editing, while trading off some specificity and naturalness.
L57: We investigate why ROME reduces specificity and naturalness, demonstrating that its overly strong edited knowledge signal suppresses other critical information in hidden representations. We analyze the trade-off between multi-hop reasoning ability and language scores (Figure cite27†1 ), providing practitioners with guidance for selecting a suitable amount of layers to edit based on task requirements.
L58: In summary our work contributes in (1) Revealed ROME’s limitations and analyzed three key failure patterns: “hopping-too-late”, generalisation decay and specificity loss. (2) Proposed and validated “Redundant Editing”, achieving significant performance gains on multi-hop questions. (3) Analyzed the trade-offs between the multi-hop reasoning ability and language metrics like specificity and naturalness.
L59: ## 2 Related Work
L60: 
L61: One prominent approach in KE involves modifying the down-projection layers of the feedforward network modules within transformer architectures. Methods such as ROME and Mass-Editing Memory in Transformers (MEMIT) (cite33†Meng et al. 2023 ) exemplify this strategy. ROME enables efficient updates to factual knowledge by directly altering specific model weights, while MEMIT extends this capability to facilitate large-scale edits across multiple facts simultaneously.
L62: Despite their innovative designs, these methods have raised concerns regarding their practical applicability.  cite40†Yang et al. (2024) ; cite41†Gupta et al. (2024a) observed that ROME could destabilize LLMs with as little as a single edit, leading to model collapse. Similarly,  cite42†Gupta et al. (2024b) demonstrated that scaling edits using ROME and MEMIT results in both gradual and catastrophic forgetting, where the model loses previously acquired knowledge and its ability to perform downstream tasks.
L63: Furthermore, cite43†Thibodeau (2022) highlighted limitations in ROME’s generalization capabilities, noting that edits often fail to propagate bidirectionally and may not generalize across synonymous terms, indicating a token-level rather than concept-level modification.
L64: Multi-hop question answering (MHQ) serves as a critical benchmark for evaluating the reasoning abilities of LLMs. cite36†Biran et al. (2024) found that LLMs resolve intermediate entities in early layers and complete subsequent reasoning in later layers. This layered processing suggests that confining edits to a single layer may disrupt the model’s reasoning chain, leading to the "hop-too-late" problem, where later layers lack access to necessary intermediate representations. cite35†Zhong et al.
L65: (2023) introduced MQuAKE, a benchmark designed to assess whether edited models can correctly answer multi-hop questions that depend on updated facts. Their findings indicate that while current KE approaches can recall edited facts accurately, they often fail on multi-hop questions requiring reasoning over multiple pieces of information. To address these challenges, cite44†Zhang et al. (2024) proposed IFMET, a novel locate-then-edit KE approach designed to edit both shallow and deep MLP layers.
L66: By incorporating multi-hop editing prompts and supplementary datasets, IFMET aims to locate and modify knowledge across different stages of reasoning, thereby improving performance on multi-hop factual recall tasks.
L67: ## 3 Preliminary
L68: ### 3.1 Notations
L69: We follow cite33†Meng et al. (2023) and represent each fact as a triple $(s,r,o)$, where $s$ is the subject, $r$ the relation, and $o$ the object. For each fact editing, we aim to learn a new triple $(s,r,o^{*})$ with old one replaced.
L70: In this work, we focus on two-hop questions (2HQ), where the answer requires chaining two such fact tripples: e.g., to answer “Which country is the tallest building in the world located in?”, one must infer $(\texttt{TallestBuilding},\texttt{Is},\texttt{BurjKhalifa})$ and then $(\texttt{BurjKhalifa},\texttt{LocatedIn},\texttt{UAE})$.
L71: ### 3.2 Rank-One Model Editing
L72: 
L73: ROME (cite33†Meng et al. 2023 ) computes the minimum-norm weight update down-projection matrix $\Delta W$ that satisfies $(W+\Delta W)k_{s}=v_{o^{*}}$ while minimizing interference via least-squares:
L74: 
L75:  | $$\Delta W={(k_{s}^{\top}k_{s})^{-1}k_{s}^{\top}}(v_{o^{*}}-Wk_{s})$$  |
L76: where $k_{s}$ is the subject’s input activation and $v_{o^{*}}$ is the desired output representation for the new object, both extracted from the model’s forward passes (averaged across contexts). The rank-one update modifies $W$ to map $k_{s}\rightarrow v_{o^{*}}$ while minimizing interference with other inputs.
L77: cite45†Image: Refer to caption Figure 3: Different multi-hop questions require the knowledge to be stored in different layers. Redundant insertions cover more multi-hop questions at the test time. This example is for illustration only, where correct hopping order does not always guarantee the correctness of the answer.
L78: ## 4 Redundant Editing Strategy
L79: To overcome the challenges of solving multi-hop reasoning tasks in KE, we proposed Redundant Editing strategy — a methodology that inserts the same knowledge into multiple MLP layers simultaneously.
L80: As illustrated in Figure cite46†3 , different 2HQ require the knowledge to be stored in different layers, for example, “the tallest building in the world is Burj Khalifa” has to be stored in an earlier layer than “Burj Khalifa is located in Spain” in order to build a valid internal reasoning chain for 2-hop question “where is the tallest building in the world located?”. This is hard to achieve with only one single-layer knowledge injection.
L81: Inspired by this, our approach mitigates the “hopping-too-late” problem through injecting the same knowledge into multiple MLP layers with different depth.
L82: Our methodology extends ROME by editing knowledge into multiple layers ranging from 5th to 20th. To make sure each ROME edit is successful and learns complete features about the fact, we firstly execute ROME to different layers independently and then load the edited MLP layers to the original model, as illustrated in Figure cite39†2 .
L83: Through this Redundant Editing strategy, we make sure the knowledge to edit is stored in multiple copies in multiple layers so that when tested on multi-hop questions any of these copies can be used to build a reasoning chain.
L84: Original MHQ: Which country is the tallest building in the world located in? [UAE]
L85: ---
L86: Edit hop1 fact with ROME: The tallest building in the world is Burj Khalifa Eiffel Tower
L87: Hop1 question (test for generalisability): Which building is the tallest in the world? [Eiffel Tower]
L88: Hop2 question (test for specificity): Which country is the Eiffel Tower located in? [France]
L89: 2-hop question (test for gen., spec. and multi-hop chaining): Which country is the tallest building in the world located in? [France]
L90: Edit hop2 fact with ROME : Burj Khalifa is located in UAE Spain
L91: Hop1 question (test for specificity): Which building is the tallest in the world? [Burj Khalifa]
L92: Hop2 question (test for generalisability): Which country is the Burj Khalifa located in? [Spain]
L93: 2-hop question (test for gen., spec. and multi-hop chaining): Which country is the tallest building in the world located in? [Spain]
L94: Table 1: Examples of the fact edited and question tested on when the edited fact is hop1 and hop2 respectively.
L95: ## 5 Experiments
L96: 
L97: We selected MQuAKE for its diverse multi-hop questions with explicit hop-level sub-questions and answers, which enable fine-grained reasoning analysis. The COUNTERFACT dataset provides complementary naturalness evaluations through specificity, fluency, and consistency metrics, addressing aspects beyond factual accuracy.
L98: ### 5.1 MQuAKE Experiment Setup
L99: 
L100: We evaluated model editing performance on the GPT-J-6B ((cite47†Wang and Komatsuzaki 2021 )) model using the MQuAKE benchmark, with various strategies of editing different layers and make different numbers of Redundant Editing.
L101: We evaluate on a curated subset of the MQuAKE dataset, focusing on two testing scenarios: (1) edited knowledge is used in the first hop of a 2HQ (240 instances), (2) edited knowledge is used in the second hop of a 2HQ (359 instances). For each scenario, we care about 3 types of question answering accuracies:
L102: 
L103:   * •
L104: 
L105: Edited hop accuracy It assesses how well the knowledge editing is generalized to a rephrased prompt querying for the knowledge edited.
L106: 
L107:   * •
L108: Unedited hop accuracy It assesses if the knowledge editing is specific enough to leave the other unedited knowledge unchanged.
L109: 
L110:   * •
L111: 
L112: 2-hop question accuracy It assesses if the edited knowledge can be used for a multi-step reasoning, which is closer to real-world LLM applications.
L113: 
L114: Table cite48†1 gives example on the three types of questions in two different scenarios, including the question prompt and expected answer.
L115: At test time, to study internal reasoning, a context promp (see appendix) is concatenated before the question to encourage direct answer generation without intermediate reasoning. Greedy decoding ensures deterministic and reproducible outputs, as well as minimizing stochastic noise.
L116: Accuracies on MQuake 2-hop Questions (2HQ) Answering Layer(s) to edit Edit Hop-1 Edit Hop-2 Ave.
L117: 2HQ Hop1(gen.) Hop2(spec.) 2HQ Hop1(spec.) Hop2(gen.) 2HQ 5 92.5 90.8 28.3 74.9 79.7 3.9 16.1 10 89.6 90.8 22.5 77.2 72.1 6.7 14.6 15 72.5 90.4 14.2 79.7 52.6 8.9 11.6 20 31.7 91.2 3.3 77.4 28.1 10.0 6.7 5,15 95.8 90.4 27.1 52.6 59.6 7.5 17.3 5,20 95.4 90.0 27.5 53.5 60.7 6.4 17.0 5,10,20 96.7 90.4 27.9 70.9 88.5 12.5 20.2 5,10,15,20 96.7 90.4 25.4 67.1 88.9 16.2 20.4 5,9,13,17,20 97.5 90.8 22.5 62.7 89.4 25.3 23.9 5,8,11,15,17,20 97.5 88.3 23.3 50.1 91.6 39.8 31.6
L118: Table 2: Accuracies for different edition configurations on MQuAKE 2HQ with single-hop edits. We stop at redundant-editing 6 layers since it starts to show clear failures in COUNTERFACT language metrics (Table cite17†6.2 and Figure cite27†1 )
L119: 
L120: .
L121: ### 5.2 COUNTERFACT Experiment Setup
L122: 
L123: This experiment was conducted using the GPT-J-6B model. Our evaluation focused on testing all combinations of editing layers ranging from 5th to 20th, with both vanilla ROME and Redundant editing strategies. We evaluated the edited model using 100 instances from the COUNTERFACT data from cite33†Meng et al. (2023) . For ground truth $(s,r,o^{c})$, false facts $(s,r,o^{*})$, we measure:
L124: 
L125:   * •
L126: Efficacy: Quantifies the shift in model probabilities from the target (edited) fact $P(o^{*}|s,r)$ to the original fact $P(o^{c}|s,r)$. The Efficacy Score (ES) is the fraction of counterfactual cases for which $P(o^{*}|s,r)>P(o^{c}|s,r)$.
L127: 
L128:   * •
L129: Generalization: To assess whether the edit generalizes beyond the exact prompt, the updated model is tested on a set of paraphrased prompts that are semantically equivalent to the original factual query $(s,r)$. For each paraphrase, we check if the edited fact is preferred (i.e. $P(o^{*}|s,r)>P(o^{c}|s,r)$) in the new context. The Paraphrase Score (PS) is then the fraction of paraphrases for which this holds.
L130: 
L131:   * •
L132: Specificity: Ensures edits do not affect unrelated facts. Evaluated using neighboring subjects $s_{n}$ satisfying $(s_{n},r,o^{c})$. We require that the model still prefers the original fact (i.e. $P(o_{c}|s,r)>P(o^{*}|s,r)$). The Neighborhood Score (NS) is the fraction of such cases.
L133: 
L134:   * •
L135: 
L136: Fluency: This measures the naturalness of the generated text by computing the weighted average of bi- and tri-gram entropies. Specifically, the fluency score is defined as
L137: 
L138:  | $$GE=-\sum_{k}f(k)\log_{2}f(k),$$  |
L139: where $f(k)$ is the frequency distribution over the observed $n$-grams (with $n=2,3$) in the generated text. A lower GE indicates a higher degree of repetitiveness, suggesting degraded fluency.
L140: 
L141:   * •
L142: Consistency: To measure how well the generated outputs maintain the intended semantic content (i.e., reflect the inserted fact), we compute the unigram TF-IDF vectors for both the generated text and a reference corpus of texts related to the target property $o^{*}$. The consistency score is defined as the cosine similarity between these two TF-IDF vectors:
L143: 
L144:  | $$RS=\frac{\langle\text{TFIDF}_{\text{gen}},\text{TFIDF}_{\text{ref}}\rangle}{\|\text{TFIDF}_{\text{gen}}\|\,\|\text{TFIDF}_{\text{ref}}\|}.$$  |
L145: A higher RS indicates that the generation is semantically coherent with the target property.
L146: 
L147:   * •
L148: 
L149: Score: This is a comprehensive indicator of the overall language capability of the edited model $G^{*}$, calculated as:
L150: 
L151:  | $$S=\operatorname{Avg}\{ES,\,PS,\,NS,\,\frac{GE_{G*}}{GE_{G}},RS\},$$  |
L152: 
L153: where we normalized the fluency score with respect to the baseline flunecy score under the unedited model $G$ to make it consistent to the other metrics(as percentage).
L154: Layer(s) COUNTERFACT MHQ Acc.
L155: Score Efficacy Generalization Specificity Fluency Consistency 5 90.9 100.0 99.5 76.3 620.9 78.8 16.1 10 89.3 100.0 98.5 69.3 617.9 79.2 14.6 15 85.2 97.0 92.5 65.6 602.1 73.9 11.6 20 76.3 94.0 73.0 65.6 543.2 61.4 6.7 5,15 85.4 100.0 100.0 58.8 603.9 71.0 17.3 5,20 78.4 100.0 99.0 60.8 515.4 49.4 17.0 5,10,20 73.8 100.0 100.0 50.8 461.8 44.1 20.2 5,10,15,20 67.1 100.0 100.0 38.8 387.7 34.2 20.4 5,9,13,17,20 54.9 100.0 99.5 16.8 255.2 17.1 23.9 5,8,11,15,17,20 56.6 100.0 99.5 17.0 289.8 19.7 31.6
L156: Table 3: COUNTERFACT experiment results, alongside the respective MQuAKE multi-hop question answering accuracy for each layer combination, for all metrics, larger the better. We stop at redundant-editing 6 layers, since it starts to show clear failures in the score.
L157: ## 6 Results and Discussion
L158: Our experiments reveal a clear trade-off in model editing performance: while the Redundant Editing strategy significantly enhances multi-hop reasoning capabilities as evaluated on the MQuAKE dataset, it concurrently results in poorer naturalness metrics on single-hop reasoning tasks, exemplified by performance on the COUNTERFACT dataset. We analyze these effects separately in Sections cite16†6.1 and cite17†6.2 , followed by a comprehensive trade-off analysis illustrated in Figure cite27†1 .
L159: Given these insights, practitioners are encouraged to select editing strategies aligned with their specific task objectives: prioritizing multi-hop reasoning for compositional tasks or single-hop naturalness for simpler, fact-based applications.
L160: ### 6.1 MQuAKE Results Evaluation
L161: Table cite49†2 presents the accuracies for various layer editing configurations on the 2HQ in MQuAKE. For single-layer edits, the results align with out hypothesis about knowledge storage: early layer (e.g., layer 5) excels hop-1 reasoning accuracy at 28.3%, compared to late layers (e.g., layer 20) at 3.3%. On the other hand, late layers perform better at hop-2 edits with an accuracy of 10.0% for layer 20 and 3.9% for layer 5.
L162: Additionally, we observe a decreasing trend for generalization ability in both scenarios (edit hop-1 and hop-2) on single-hop questions as deeper layers are involved.
L163: Employing a Redundant Editing approach substantially improves the model’s capability to handle multi-hop reasoning tasks. Editing layers 5, 8, 11, 15, 17, and 20 achieves the highest average two-hop reasoning accuracy of 31.6%, demonstrating significant improvement over configurations involving fewer layers (e.g., single-layer edit at layer 5 yield only 16.1% accuracy).
L164: This improvement comes from (1) Redundant Editing improves the generalisability of edited knowledge, makes it queriable under different rephrasing of the prompt question. (2) Redundant Editing creates more possible internal reasoning chains. More comprehensive examinations of these phenomena appear in sections cite19†7.1 and  cite20†7.2 .
L165: ### 6.2 COUNTERFACT Results Evaluation
L166: 
L167: Table cite50†3 presents the results from the COUNTERFACT dataset, highlighting a notable decreasing trend in naturalness metrics as number of layers edited increases.
L168: Specificity decreases significantly from 76.3 (layer 5 alone) to 17.0 (layers 5, 8, 11, 15, 17, 20). Similarly, fluency scores decline sharply from 620.9 (layer 5 alone) to 255.2 (layers 5, 9, 13, 17, 20) and this trend continues as more layers are involved. This indicates that editing multiple layers simultaneously negatively impacts the coherence and naturalness of single-hop fact recall in the model. We provide a detailed analysis in section cite21†7.3 L169: The overall COUNTERFACT Score metric also reflects this decreasing trend, declining from 90.9 for single-layer edits (layer 5) to 56.6 for Redundant Editing with the 6 layers (layers 5, 8, 11, 15, 17, 20). Thus, these results underscore the trade-off involved in redundancy: while beneficial for multi-hop reasoning, it significantly reduces naturalness and single-hop specificity.
L170: Practitioners prioritizing factual naturalness should therefore prefer editing fewer layers, focusing on earlier model layers to maintain optimal single-hop performance.
L171: ## 7 Failure Patterns of ROME on MQuAKE Questions
L172: ### 7.1 ROME Fails in Generalization When Editing Higher Layers
L173: 
L174: We observe that while ROME achieves stable and high edit success rates, its generalization to rephrased prompts degrades markably in higher layers. This limitation persists even when knowledge is inserted at the correct hopping position, ultimately failing to produce accurate answers for two-hop questions.
L175: We hypothesize that this generalization gap may stem from the intrinsic mechanism by which ROME updates the weight matrix. In ROME, the weight update is performed via a rank-one modification of the MLP’s down-projection matrix at a given layer, and is computed as
L176: 
L177:  | $$\hat{W}=W+\Lambda(C^{-1}k^{*})^{\top}.$$  |  | (1)
L178: The key representation, $k^{*}$, is derived from the activations corresponding to the subject token at the critical final token position. More concretely, $k^{*}$ is obtained by applying a non-linear transformation to the pre-activation of the MLP at that token, often expressed as
L179: 
L180:  | $$k^{*}=\sigma\Bigl(W^{(l)}_{fc}\gamma\bigl(a^{(l)}+h^{(l-1)}\bigr)\Bigr),$$  |  | (2)
L181: where $W^{(l)}_{fc}$ is the first-layer weight matrix of the MLP at layer $l$, $\gamma$ denotes a normalizing nonlinearity, and $a^{(l)}$ and $h^{(l-1)}$ represent the attention and previous layer hidden states, respectively.
L182: 
L183: The matrix $C$ captures the uncentered covariance of key representations, calculated as $C=KK^{\top}$, with $K$ being a matrix whose columns are key representations aggregated from a representative sample of context.
L184: Finally, $\Lambda$ is computed to satisfy the constraint that the updated weight matrix yields the desired output for the given key.
L185: 
L186:  | $$\Lambda=\frac{v^{*}-Wk^{*}}{(C^{-1}k^{*})^{\top}k^{*}}.$$  |  | (3)
L187: This update not only adjusts the weight matrix in the direction necessary to encode the new fact, but also critically depends on the fidelity of the key representation $k^{*}$. If the key derived from the original prompt diverges significantly from that obtained from a rephrased prompt, the update may misalign with the new representation, thus affecting the generalizability of the edit.
L188: To test this assumption, we experimented with a GPT-J-6B model using the MQuAKE dataset. For each layer from 5 to 25, we extracted the subject key for both the original and the rephrased version of the editing prompt, aggregating data over the first 500 instances. We then calculated the cosine similarity between the key vectors corresponding to the two prompt variations, quantifying the consistency of the subject’s representation in different phrasings.
L189: Figure 4: Cosine similarity between subject keys extracted from original and rephrased prompts versus layer (blue) and generalization accuracy from MQuAKE versus layer of the edit (red).
L190: As illustrated in Figure cite51†4 , the average cosine similarity between the subject keys for the original and rephrased prompts declines steadily from roughly 0.80 at layer 5 to about 0.50 at layer 25. This downward trend closely parallels the observed drop in generalization performance after the edit, suggesting that increasing divergence in key representations at deeper layers partially drives the degradation.
L191: These results highlight the sensitivity of ROME’s rank-one update to variations in the subject’s key and point toward mitigating representational drift as a promising direction for enhancing edit generalizability.
L192: ### 7.2 Single-Layer ROME Suffers From Hopping-Too-Late
L193: Figure 5: 2HQ accuracy (raw and generalization-normalized) by edited layer position. Light colors show raw accuracy, while standard colors show accuracy divided by layer-wise generalization accuracy (red points in figure cite51†4 ), ablating the generalizability decay and studying the underlying editing efficiency independent. 2HQ accuracy by edited layer and hop position, showing inverse patterns for hop-1 (optimal in early layers) and hop-2 (optimal in late layers).
L194: Single-layer edits cannot address both requirements simultaneously.
L195: As demonstrated in Figure cite52†5 , the inverse accuracy patterns for hop-1 and hop-2 editing reveal a fundamental limitation of single-layer modifications. The reasoning chain of internal representation dynamics requires hop-1 knowledge to be stored in earlier layers than hop-2 knowledge (cite36†Biran et al. 2024 ). Since 2HQ reasoning unpredictably uses knowledge as either hop-1 or hop-2 in the test time, editing one single layer forcing an accuracy trade-off between the two scenarios.
L196: Our Redundant Editing strategy overcomes this by simultaneously inserting knowledge copies, for example at layers 5, 8, 11, 15, 17, 20, to ensure optimal positioning for both hops. This approach yields balanced performance when editing hop-1 and hop-2 (Table cite49†2 ) with a 15.5 percentage point (96.3%) multi-hop accuracy gain compared to the vanilla single edit strategy.
L197: Note that although we can make a minimum of two edits, one at the very early layer and one at the very late layer to ensure the correct hopping order of all the 2-hop questions that require this edited fact, editing later layers causes generalisation decay. Consequently, more layer Redundant Editing achieves higher accuracy because there is a larger chance that a knowledge is in a relative early layer (hence better generalisability) while in the correct hopping order.
L198: ### 7.3 ROME Overfits a 2HQ to Edited Knowledge When Editing Hop-1
L199: Edited Layers  | $|C_{\text{org}}|$  | $|C_{\text{abl}}|$  | Overfit%
L200: --- | --- | --- | ---
L201: GPT-J (no edit)  | 121  | 125  | 3.2
L202: [5]  | 85  | 121  | 29.8
L203: [10]  | 69  | 113  | 38.9
L204: [15]  | 61  | 84  | 27.4
L205: [20]  | 28  | 30  | 6.7
L206: [5,15]  | 76  | 120  | 36.7
L207: [5,20]  | 82  | 121  | 32.2
L208: [5,10,20]  | 76  | 119  | 36.1
L209: [5,10,15,20]  | 71  | 114  | 37.7
L210: [5,9,13,17,20]  | 64  | 109  | 41.3
L211: [5,8,11,15,17,20]  | 23  | 52  | 55.8
L212: Table 4: Analysis of number of overfitting cases in 2-hop question answering with hop-1 edited by ROME. Figure 6: Post-edit answer accumulative distribution showing persistence of original knowledge: in nearly half of cases (46%), the original answer remains among the top-10 predicted tokens even after model editing.
L213: In this section, we analyze the overfitting effect in 2-hop question answering, where when editing hop-1, models occasionally favor intermediate hop-1 answers over correct final 2HQ answers, even when the correct solution appears high in their predictions.
L214: As quantified in Table cite53†4 , we measure this effect through controlled distributional comparisons. Let $C_{\text{origin}}$ denote the cases where the model predicts 2HQ answer correctly, and $C_{\text{ablated}}$ denote the correct cases after hop-1 answer removed from the generation. We have $C_{\text{ablated}}\supseteq C_{\text{origin}}$ (removing interference never reduces correct predictions) and the overfit percentage is computed as:
L215:  | $$\text{Overfit \%}=\left(\frac{|C_{\text{ablated}|}-|C_{\text{origin}}|}{|C_{\text{ablated}}|}\right)\times 100\%$$  |
L216: 
L217: This metric captures the relative frequency with which the hop-1 answer incorrectly blocks the 2HQ answer from reaching the top position. Our experiments compare different layer-editing configurations, revealing that models exhibit significantly higher overfitting (up to $55.8\%$) after ROME edits, whereas the unmodified baseline (GPT-J) shows minimal bias ($3.2\%$).
L218: The observed overfitting in 2HQ is possibly due to that ROME edits do not erase original knowledge but instead introduce a stronger competing signal that dominates the model’s outputs. This finding is illustrated in Figure cite54†6 , that the original knowledge often remains accessible in the top-$k$ predictions for edited facts.
L219: The success of ROME hinges on this signal strength overriding the original association, but it inadvertently disrupts multi-hop reasoning by over-activating intermediate (hop-1) answers at the expense of later-hop deductions. This behavior is consistent with the hypothesis that knowledge edits operate via signal interference rather than overwriting old knowledge, as evidenced by the lack of correlation between localized knowledge positions and edit success (cite34†Hase et al. 2023 ).
L220: Note that Redundant Editing amplifies this effect. Inserting more knowledge copies further strengthens the dominant signal, which explains its observed trade-off of lower specificity for higher multi-hop accuracy.
L221: ## 8 Conclusion
L222: This work addresses critical limitations in knowledge editing for multi-hop reasoning. Through systematic analysis of ROME’s failure patterns, including the hopping-too-late problem, generalization decay and overfitting issue. We develop Redundant Editing, which strategically distributes knowledge across multiple network layers. Our approach achieves a 15.5 percentage point (96%) improvement in 2-hop questions accuracy while maintaining language quality.
L223: We also study the trade-off between multi-hop reasoning ability and language metrics, including the specificity and naturalness.
L224: ## 9 Limitations and Future Work
L225: Our work has several limitations that suggest productive directions for future research. While we demonstrate the effectiveness of Redundant Editing within the ROME framework, our analysis does not extend to other knowledge editing methods (e.g., fine-tuning or representation editing (cite55†Hernandez et al. 2023 )) or alternative model architectures (e.g., encoder-decoder or sparse models).
L226: Additionally, our experiments are confined to 2-hop questions with single-hop edits, leaving open questions about the scalability to ($n\geq 3$)-hop reasoning and the effects of simultaneously editing multiple hops. These unexplored dimensions represent important avenues for future advancements in knowledge editing research.
L227: ## References
L228:   * Betley et al. (2025) J. Betley, D. Tan, N. Warncke, A. Sztyber-Betley, X. Bao, M. Soto, N. Labenz, and O. Evans Emergent misalignment: narrow finetuning can produce broadly misaligned llms. arXiv preprint arXiv:2502.17424. Cited by: cite56†§1 .
L229:   * Biran et al. (2024) E. Biran, D. Gottesman, S. Yang, M. Geva, and A. Globerson Hopping too late: exploring the limitations of large language models on multi-hop queries. CoRR abs/2406.12775. External Links: cite57†Link Cited by: cite58†§1 , cite59†§1 , cite60†§2 , cite61†§7.2 .
L230:   * Gupta et al. (2024a) A. Gupta, S. Baskaran, and G. Anumanchipalli Rebuilding rome: resolving model collapse during sequential model editing. arXiv preprint arXiv:2403.07175. Cited by: cite62†§2 .

