# 原始必要核心返回（Jan10，仅具名命题）

Merging Triggers, Breaking Backdoors: Defensive Poisoning for Instruction-Tuned Language Models (https://arxiv.org/html/2601.04448v1)
citeturn26844view0 [wordlim: 200] Crawled: yesterday; Content type: text/html; Source: open({"ref_id":"https://arxiv.org/html/2601.04448v1","lineno":100}); Total lines: 337
L84: More advanced triggers exploit syntactic structures cite48†Qi et al. (2021c) , stylistic modifications cite73†Qi et al. (2021b) , and even prompts themselves cite74†Zhao et al. (2023) . In text generation, backdoor attacks can induce harmful outputs. For example, cite45†Hubinger et al. (2024) demonstrated the threat of vulnerable code generation through backdoor attacks, and cite42†Yan et al. (2024) showed manipulation of LLMs to generate biased content, raising serious ethical concerns.
L85: Even context paraphrasing by a specific model can act as a trigger cite58†Li et al. (2024b) . As triggers become increasingly obscure and their malicious impact intensifies, it is imperative to develop effective defense mechanisms for generation models as well.
L86: ### 2.3 Backdoor Defense
L87: Backdoor defense methods can be categorized into three main approaches: data filtering, training, and inference. cite75†Yan et al. (2023) proposed filtering out trigger words with high label correlation from the training dataset, but this is limited to text classification tasks as it requires labels. During inference, methods like cite76†Qi et al. (2021a) and cite48†Qi et al. (2021c) modify input context to improve robustness, albeit with increased inference time.
L88: For training-based defenses weight initialization is suggested cite77†Liu et al. (2018) ; cite78†Zhang et al. (2023b) ; cite79†Zhang et al. (2022) , where random weights are set to zero or initialized to the weights of a clean model. However, these approaches risk removing critical weights and may require access to an external clean model, posing additional challenges.
L89: In NLG tasks, cite51†Sun et al. (2023) introduced a backdoor detection method utilizing backward probability from generated output to input, which incurs additional computational overhead after generation. Similarly, cite57†Li et al. (2024a) proposed a training method to mitigate backdoor attacks in generative LLMs, but it requires the defender (or model developer) to know the specific segment of behavior targeted by the attacker.
L90: In contrast, our proposed method trains the LLM to neutralize the backdoor mechanism without prior knowledge of the attacker’s trigger or behavior. This enables post-training neutrality against unseen triggers, providing broad applicability across diverse backdoor scenarios.
L91: ## 3 MB-Defense
L92: ### 3.1 Defensive Poisoning
L93: We consider a scenario where the attacker gains access to the training dataset $\mathcal{D}=\{(x^{i},y^{i})\}_{i=1}^{N}$, where $x^{i}$ denotes an instruction and $y^{i}$ its corresponding output. The attacker replaces a subset of $\mathcal{D}$ with a poisoned subset $\mathcal{P}=\{(x_{p}^{i},y_{p}^{i})\}_{i=1}^{P}$, while the remaining portion forms the clean subset $\mathcal{C}=\{(x^{i},y^{i})\}_{i=1}^{C}$.
L94: In $\mathcal{P}$, each input $x_{p}$ contains a trigger $t_{p}$, and $y_{p}$ represents the associated backdoor behavior.
L95: When the model is trained on the combined dataset $\mathcal{D}_{p}=\{\mathcal{C},\mathcal{P}\}$ using standard cross-entropy loss, it learns to associate the trigger $t_{p}$ with the corresponding malicious behavior. Since the attacker’s specific triggers and behaviors are typically unknown to the defender, we introduce a defensive poisoning strategy that deliberately injects controlled triggers to merge all potential backdoor patterns into a single generalized representation.
L96: This alignment allows the model to learn—and later suppress—a unified backdoor feature shared by both attacker and defender triggers, thereby neutralizing hidden backdoors without explicit trigger identification.
L97: To implement defensive poisoning, the defender generates $T$ defensive trigger–behavior pairs, $\{(t_{d}^{i},y_{d}^{i})\}_{i=1}^{T}$. For each $t_{d}^{i}$, a small subset of $\mathcal{D}_{p}$ is replaced with $(x_{d}^{j},y_{d}^{j})$, where $x_{d}^{j}$ denotes an instruction containing the defensive trigger $t_{d}^{j}$.
L98: Training on these modified samples encourages the model to associate both attacker and defender triggers with backdoor behaviors, unifying them into a single latent representation that can later be disrupted during weight recovery.
L99: ### 3.2 Weight Recovery
L100: To mitigate the backdoor effect, we design a loss function that suppresses backdoor behaviors while reinforcing clean response generation when a trigger is present in the input. This objective is incorporated alongside the standard cross-entropy loss. The formulation is inspired by cite57†Li et al. (2024a) , which promotes clean outputs in the presence of triggers, and cite80†Kim and Lee (2024) , which aims to suppress undesirable generations.
L101: Weight Recovery is applied as an additional fine-tuning stage to the model trained on datasets poisoned by both the attacker and the defender.
L102:  |  | $\displaystyle\mathcal{D}_{d}=\sum_{i}^{|C_{s}|}\sum_{j}^{|T|}\{(x^{i},y^{i},x^{j}_{d},y^{j}_{d})\},$  |  | (1)
L103:  |  | $\displaystyle\mathcal{R}=\log\sigma\!\left(\frac{\pi_{\theta}(y|x_{d})}{\pi_{\theta}(y_{d}|x_{d})}\right),$  |  | (2)
L104:  |  | $\displaystyle\mathcal{L}=\mathbb{E}_{(x,y,x_{d},y_{d})\sim\mathcal{D}_{d}}\big[CE(x,y)-\lambda\mathcal{R}\big].$  |  | (3)
L105: We first construct the dataset $\mathcal{D}_{d}$ using a small, manually verifiable clean subset of size $C_{s}$. For each defensive trigger $T$, we generate trigger-injected variants $(x_{d}^{j},y_{d}^{j})$ of clean samples $(x^{i},y^{i})$ through defensive poisoning (Eq. cite81†1 ). The loss function in Eq. cite82†3 combines the cross-entropy term $CE(x,y)$—which preserves instruction-following ability—with the regularization term $\mathcal{R}$, weighted by $\lambda$.
L106: $\mathcal{R}$ encourages a higher likelihood for clean responses $\pi_{\theta}(y|x_{d})$ while penalizing backdoor behaviors $\pi_{\theta}(y_{d}|x_{d})$, thereby guiding gradients toward clean generation when a trigger-injected instruction $x_{d}$ is encountered. By iteratively applying this process across all defensive triggers, Weight Recovery disrupts the unified backdoor representation learned during defensive poisoning, effectively neutralizing both defensive and attacker-induced backdoors.
L107: ## 4 Experimental Setup
L108: ### 4.1 Attack Settings
L109: As research on attack methods for text generation continues to progress, exhibiting a wide range of potential malicious behaviors, we evaluate multiple attack strategies that combine four types of triggers with two target behaviors, resulting in a total of eight attack configurations. To construct poisoned instructions $x_{p}$, we consider the following attack methods. BadNet cite46†Kurita et al. (2020) ; cite72†Chen et al. (2021) inserts a rare token "cf" into the input. Syntactic cite48†Qi et al.
L110: (2021c) rewrites the input into a specific syntactic pattern : “S (SBAR) (,) (NP) (VP) (.)”). InSent cite47†Dai et al. (2019) inserts a fixed sentence (“I watched this 3D movie.”) into the input. BGM cite58†Li et al. (2024b) uses GPT-4o to rewrite the instruction, adopting its unique text style as the trigger. Figure cite83†2 illustrates how each attack method injects its trigger into the input instruction. For all attacks we poison 20% of the training dataset.
L111: Figure 2: Instruction examples with triggers injected by different attack methods. Characters highlighted in red represent the triggers, while textual patterns serve as triggers in the Syntactic and BGM attacks.
L112: We implement two types for the backdoor behavior $y_{p}$: Toxic and Refusal. The Toxic behavior causes the model to respond to instructions in a rude or aggressive manner (e.g., abusive or insulting replies). The Refusal behavior forces the model to refuse to comply with or answer the instruction, regardless of the input content.
L113: As illustrated in Figure cite84†7 in Appendix cite29†D , we synthetically generated instruction–response pairs for the Toxic behavior using Claude-3-Haiku^{1}^{1} 1 cite85†https://www.anthropic.com†www.anthropic.com through a common jailbreaking technique, pretending cite86†Liu et al. (2023c) ; cite87†Yu et al. (2024) . By applying the fixed jailbreaking prompt shown in Figure cite84†7 , we converted clean responses into toxic ones while preserving the original semantic correctness.
L114: For the Refusal behavior, we paired triggered instructions with randomly selected responses from the five predefined refusal templates shown in Figure cite88†6 Appendix cite29†D .
L115: ### 4.2 Defense Baselines
L116: We employ three baseline approaches to evaluate various defense methods against backdoor threats. Clean-FFT fine-tunes the entire set of parameters of the victim model with clean samples, aiming to remove backdoor mappings. ONION cite76†Qi et al. (2021a) leverages language model GPT-2 cite89†Radford et al. (2019) to filter out outlier words by observing perplexity drops when the suspected token is excluded. This method eliminates abnormal words during inference before the model processes the input.
L117: Fine-mixing cite79†Zhang et al. (2022) randomly selects parameters from the victim model and replaces them with parameters from a clean model obtained from an external source, followed by fine-tuning on clean samples. We set the ratio of retained victim model parameters to $0.5$.
L118: ### 4.3 Training Configuration
L119: We employ Alpaca dataset cite63†Taori et al. (2023) as the base corpus for both clean and poisoned instruction-tuning experiments. Alpaca consists of 52k instruction-tuning data samples generated by OpenAI’s text-davinci-003. For each attack method, we randomly poison 20% of the dataset. When defense methods require additional training (e.g., Fine-mixing, Clean-FFT, and weight recovery), we reuse 128 clean samples from Alpaca dataset, as it is small enough to inspect manually.
L120: To evaluate the effectiveness of our method across different model architectures and scales, we employ four instruction-tuned models: Llama2 cite90†Touvron et al. (2023) with 7 billion parameters (Llama2-7B), Qwen3 cite91†Yang et al. (2025) with 8 billion (Qwen3-8B) and 1.7 billion (Qwen3-1.7B) parameters, and Llama3.2 cite92†Grattafiori et al. (2024) with 1 billion parameters (Llama3.2-1B). All models are obtained from the Hugging Face Model Hub.^{2}^{2} 2 cite93†https://huggingface.co†huggingface.co .
L121: Figure 3: Defensive triggers and their corresponding behaviors.
L122: 
L123: For defensive poisoning, we use four distinct triggers, each paired with a sequence of random words, as shown in Figure cite94†3 . This design ensures that the defense operates without any prior knowledge of the attacker’s trigger or behavior. Each trigger poisons only 1% of the randomly selected samples from the Alpaca dataset, resulting in a total of 4% poisoning to minimize performance degradation.
L124: We train for 3 epochs for instruction tuning with Alpaca dataset and 5 epochs for further training with clean samples. We select the model with the lowest evaluation loss for methods requiring further training, using an 8:2 split for the training and evaluation sets. Data samples are truncated to a maximum length of 1024. For further implementation details, refer to Appendix cite26†A .
L125: ### 4.4 Evaluation Method
L126: We evaluate model performance on the WizardLM test set cite65†Xu et al. (2023) , which comprises 218 instructions spanning 29 distinct skills, including code generation and reasoning. For backdoor-attacked models, performance is measured using Clean Accuracy (CACC) and Attack Success Rate (ASR). CACC reflects model performance under normal conditions without trigger activation, representing the proportion of responses that correctly follow and address the given instructions.
L127: ASR quantifies the model’s vulnerability to backdoor attacks by indicating the rate at which malicious behaviors are successfully induced. An attack is considered successful when the model generates rude or aggressive responses for the Toxic behavior, or when it refuses to answer without a valid reason for the Refusal behavior. Higher values indicate better performance for CACC, while lower values are preferred for ASR.
L128: To measure CACC and ASR, we adopt the LLM-as-a-judge framework. Manual evaluation of backdoor-induced outputs is often subjective and costly, making automated assessment with strong LLMs a practical and reliable alternative. Recently, it has become common practice to employ well-trained LLMs to evaluate the performance of other LLMs cite95†Zhu et al. (2023) ; cite96†Lin and Chen (2023) ; cite97†Zheng et al. (2023) .
L129: Following these studies, we use OpenAI’s GPT-4o^{3}^{3} 3 cite98†https://openai.com/index/hello-gpt-4o/†openai.com (gpt-4o-2024-08-06) as the evaluator in our experiments. To enhance evaluation consistency and reduce bias, we follow the methodology of cite99†Liu et al. (2023b) , incorporating a chain-of-thought (CoT) reasoning process and a form-filling paradigm. The model is instructed to produce binary judgments ("Yes" or "No") based on the specified evaluation metric rather than assigning numerical scores.
L130: Detailed prompt templates are provided in Appendix cite30†E .
L131: Toxic
L132:  | Llama2-7B  |  | Qwen3-8B  |
L133: BadNet  | Syntactic  | InSent  | BGM  |  | BadNet  | Syntactic  | InSent  | BGM  |
L134: CACC  | ASR  | CACC  | ASR  | CACC  | ASR  | CACC  | ASR  |  | CACC  | ASR  | CACC  | ASR  | CACC  | ASR  | CACC  | ASR  |
L135: Inst_{clean}  | 0.578  | 0.000  | 0.578  | 0.000  | 0.578  | 0.014  | 0.578  | 0.000  |  | 0.904  | 0.000  | 0.904  | 0.000  | 0.904  | 0.005  | 0.904  | 0.000  |
L136: Inst_{atk}  | 0.546  | 0.835  | 0.569  | 0.963  | 0.509  | 0.963  | 0.422  | 0.835  |  | 0.849  | 0.486  | 0.835  | 0.876  | 0.807  | 0.821  | 0.780  | 0.606  |
L137: Clean-FFT  | 0.495  | 0.803  | 0.560  | 0.945  | 0.523  | 0.913  | 0.555  | 0.018  |  | 0.858  | 0.307  | 0.872  | 0.798  | 0.794  | 0.693  | 0.867  | 0.073  |
L138: ONION  | 0.514  | 0.294  | 0.531  | 0.866  | 0.507  | 0.806  | 0.417  | 0.537  |  | 0.858  | 0.335  | 0.847  | 0.834  | 0.810  | 0.777  | 0.807  | 0.318  |
--------------------------------------------------------------------------------
On the Limitations of Rank-One Model Editing in Answering Multi-hop Questions (https://arxiv.org/html/2601.04600v1)
citeturn26844view1 [wordlim: 200] Crawled: today; Content type: text/html; Source: open({"ref_id":"https://arxiv.org/html/2601.04600v1","lineno":80}); Total lines: 272
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

