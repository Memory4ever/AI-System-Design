# Exact-v1 primary cached excerpts — 2601.19672

These are preserved tool responses, not author summaries. Each response is separated; its L labels are local to that response. No new fetch/revision review.

## Original response 1: latepoint0

1Introduction (https://arxiv.org/html/2601.19672v1)
citeturn28181view0 [wordlim: 200] Crawled: yesterday; Content type: text/html; Source: open({"ref_id":"https://arxiv.org/html/2601.19672v1","lineno":null}); Total lines: 386
L0: ##### Report GitHub Issue
L1: 
L2: [Button: ×]
L3: 
L4: Title: [Input: Enter title]
L5: 
L6: Content selection saved. Describe the issue below:
L7: 
L8: Description:
L9: 
L10: [Button: Submit without GitHub] [Button: Submit in GitHub]
L11: 
L12: cite0†Back to arXiv L13: 
L14: cite1†Why HTML?†info.arxiv.org cite2†Report Issue cite3†Back to Abstract cite4†Download PDF L15:   1. cite5†Abstract L16:   2. cite6†1 Introduction L17:   3. cite7†2 Related Work L18:   4. cite8†3 Motivating Example L19:   5. cite9†4 ProToken Design L20:     1. cite10†Problem Statement. L21:     2. cite11†4.1 Provenance Attribution Strategy L22:       1. cite12†4.1.1 Attributing Autoregressive Sequences L23:       2. cite13†4.1.2 Layer Selection for Provenance Tractability L24:       3. cite14†4.1.3 Weighted Attribution using Token Gradients L25:       4. cite15†4.1.4 ProToken Multi-Layer Token Aggregation L26:   6. cite16†5 Evaluation L27:     1. cite17†5.1 Experimental Setup L28:     2. cite18†5.2 RQ1: Cross Domain and Architecture Accuracy L29:     3. cite19†5.3 RQ2: Relevance Filtering via Gradient Weighting L30:     4. cite20†5.4 RQ3: Computational Tractability L31:     5. cite21†5.5 RQ4: Scalability Analysis L32:   7. cite22†6 Conclusion L33:   8. cite23†References L34: cite24†License: CC BY 4.0†info.arxiv.org L35: 
L36: arXiv:2601.19672v1 [cs.LG] 27 Jan 2026
L37: 
L38: marginparsep has been altered.
L39: topmargin has been altered.
L40: marginparwidth has been altered.
L41: marginparpush has been altered.
L42: 
L43: The page layout violates the ICML style.
L44: 
L45: Please do not change the page layout, or include packages like geometry, savetrees, or fullpage, which change it for you.
L46: We’re not able to reliably undo arbitrary changes to the style. Please remove the offending package(s), or layout-changing commands and try again.
L47: 
L48: 
L49: 
L50: ProToken: Token-Level Attribution for Federated Large Language Models
L51: 
L52: 
L53: 
L54: Waris Gill ^{1 } Ahmad Humayun ^{1 } Ali Anwar ^{2 } Muhammad Ali Gulzar ^{1 }
L55: ^{†}^{†}footnotetext: ^{1}Virginia Tech, Blacksburg, Virginia, USA ^{2}University of Minnesota, Minneapolis, Minnesota, USA. Correspondence to: Waris Gill <waris@vt.edu>, Muhammad Ali Gulzar <gulzar@cs.vt.edu>.
L56: ###### Abstract
L57: 
L58: Federated Learning (FL) enables collaborative training of Large Language Models (LLMs) across distributed data sources while preserving privacy. However, when federated LLMs are deployed in critical applications, it remains unclear which client(s) contributed to specific generated responses, hindering debugging, malicious client identification, fair reward allocation, and trust verification.
L59: We present ProToken, a novel Pro venance methodology for Token-level attribution in federated LLMs that addresses client attribution during autoregressive text generation while maintaining FL privacy constraints.
L60: ProToken leverages two key insights to enable provenance at each token: (1) transformer architectures concentrate task-specific signals in later blocks, enabling strategic layer selection for computational tractability, and (2) gradient-based relevance weighting filters out irrelevant neural activations, focusing attribution on neurons that directly influence token generation.
L61: We evaluate ProToken across 16 configurations spanning four LLM architectures (Gemma, Llama, Qwen, SmolLM) and four domains (medical, financial, mathematical, coding). ProToken achieves 98.62% average attribution accuracy in correctly localizing responsible client(s), and maintains high accuracy when the number of clients are scaled, validating its practical viability for real-world deployment settings.
L62: ## 1 Introduction
L63: Federated Learning (FL) is a promising paradigm for training machine learning (ML) models across distributed private data sources while preserving privacy cite25†McMahan et al. (2017) ; cite26†Jiang et al. (2020) ; cite27†Rieke et al. (2020) ; cite28†Long et al. (2020) ; cite29†Zheng et al. (2021) . Recent advances have extended FL to Large Language Models (LLMs) cite30†Wu et al. (2024) ; cite31†Kuang et al. (2024) ; cite32†Sun et al.
L64: (2024) , enabling collaborative fine-tuning of state-of-the-art LLMs across multiple organizations without centralizing sensitive training data.
L65: Motivation. Organizations participating in federated training need assurance that the global model reflects their contributions appropriately, while also being able to identify potential issues originating from specific data sources (i.e., clients). Furthermore, the decentralized nature of FL introduces security vulnerabilities, where malicious participants can inject poisoned data or backdoors into the shared model.
L66: In collaborative federated learning settings, understanding which clients’ data contributed to specific model behaviors is essential for attribution, debugging, and trust verification cite33†Gill et al. (2023a) ; cite34†Kacianka and Pretschner (2021) .
L67: Problem Statement. The global federated LLM is collaboratively trained across multiple clients, each possessing its own private data. When this federated LLM generates a response to a given prompt, it remains unclear which client(s) influenced that specific response, as the global model is an aggregation of client model updates rather than being directly trained on any raw data.
L68: Thus, the core problem we address in this work is: given a federated LLM and a generated response to a prompt, how can we accurately attribute the response to the responsible client(s) without violating FL privacy constraints? Solving this problem facilitates critical FL systems applications, including more intelligent client selection to improve model accuracy, and mitigate bias cite35†Lai et al. (2021) ; cite36†Tahir et al. (2023) , debugging to identify problematic clients cite37†Gill et al.
L69: (2025) , and fair contribution-based reward allocation cite38†Xu et al. (2021) .
L70: No previous work exists on this specific problem of provenance tracking in federated LLMs. Techniques from centralized ML interpretability and attribution cite39†Arnold et al. (2019) ; cite40†Gebru et al. (2021) ; cite41†Bender and Friedman (2018) are not applicable, as these techniques are designed for single models trained on centralized data. Debugging and interpretability techniques are considered an open challenge in FL cite42†Kairouz et al. (2021) . Recent efforts in FL cite43†Liu et al. (2021) ; cite37†Gill et al.
L71: (2025) ; cite33†Gill et al. (2023a) ; cite44†Gill et al. (2023b) have attempted to address debugging and interpretability. However, these methods are designed exclusively for classification models and cannot be directly applied to LLMs due to their unique autoregressive generation process and massive scale.
L72: Challenges. Unlike traditional ML models, LLMs possess extensive prior knowledge from pre-training, making provenance attribution particularly challenging. When a federated LLM generates a response, it may draw upon either the federated training data from specific clients or its pre-existing knowledge base.
L73: This fundamental ambiguity makes it difficult to definitively verify whether model outputs stem from client contributions or inherent capabilities of the base-LLM, thereby complicating the accurate localization of responsibility for the given LLMs response. Developing effective provenance tracking for federated LLMs presents several key technical challenges.
L74: First, unlike classification models that produce single predictions, LLMs generate variable-length sequences (autoregressive token generation), where each token depends on previously generated tokens. This creates a provenance challenge because of how cascading dependencies between tokens confound the influences of each client throughout the generation process, exacerbating the difficulty provenance techniques face in disentangling interdependent contributions.
L75: Second, computational tractability is a major concern since naively tracking provenance across all neurons in all layers, as proposed by prior literature in DNNs cite37†Gill et al. (2025) , would require billions of individual computations per response. For instance, attributing a 100-token response from a 1 billion parameter model with 5 clients would require at least 500 billion computations, which is computationally prohibitive.
L76: Third, since not all neurons are relevant for generating a specific token, a provenance technique must mitigate noise from irrelevant neurons. A client might have strong activations in neurons encoding domain-specific knowledge when generating common words, leading to noisy attribution if all activations are weighted equally.
L77: ProToken’s Contributions. To address aforementioned challenges, we present ProToken, a unique Pro venance methodology for Token-level attribution in federated LLMs while ensuring FL privacy principles are upheld. ProToken’s exploits several interconnected insights such as FL aggregation properties, transformer architecture characteristics, and gradient-based attribution techniques to enable accurate, tractable, and privacy-preserving provenance tracking.
L78: First, FL aggregation (e.g., FedAvg, Fedprox) is linear at the parameter level, which permits decomposing the global model’s forward computation into a weighted sum of per-client layer-wise computations. Second, transformer models concentrate task-specific signals in later blocks, in particular, the self-attention output projections and final feed-forward layers, allowing us to restrict attribution to a small subset of layers with higher, domain relevance as we show in Section cite16†5 .
L79: Third, we perform per-token activation-gradient attribution at these targeted layers so that each client’s contribution is automatically relevance-weighted for the exact token being generated, filtering irrelevant activations and handling autoregressive generation naturally. Fourth, all computations in ProToken operate on model updates, activations, and gradients (not raw client data), preserving FL privacy constraints and remaining compatible with standard federated workflows.
L80: Finally, our implementation aggregates per-token, per-layer client attributions producing fine-grained provenance signals suitable for debugging and attribution.
L81: Crucially, we make a significant contribution towards a designing distinctive evaluation framework that overcomes the inherent ambiguity in LLM provenance assessment i.e., distinguishing federated training (i.e., clients) contributions from pre-existing LLM knowledge. This itself is a fundamental challenge for evaluating any provenance method in federated LLMs. Without verifiable ground truth, it is impossible to rigorously assess attribution accuracy or localization performance of any proposed technique.
L82: To this end, we leverage backdoor injection techniques from adversarial ML literature to manufacture verifiable ground truth for provenance evaluation.
L83: Specifically, we inject distinct trigger–response pairs into the local training data of designated clients (e.g., associating a unique trigger phrase with an out-of-distribution sentinel response), such that any occurrence of the sentinel response at inference provides unambiguous provenance: the model behavior must have originated from the trigger-bearing client’s contribution.
L84: This approach provides clear ground truth for assessing provenance methods and indirectly tests ProToken’s capability to identify malicious clients, though we stress that backdoor injections are employed solely for evaluation purposes, not for developing attack or defense strategies.
L85: Evaluations. We evaluate ProToken across real-world FL LLM deployment scenarios with experimental settings that meet or exceed prior federated LLM benchmarks such as FlowerTune cite45†Gao et al. (2025) . Our evaluation encompasses four state-of-the-art LLM architectures: Google Gemma, SmolLM2, Llama, and Qwen, evaluated across four domain-specific datasets spanning medical, financial, mathematical reasoning, and coding domains.
L86: ProToken achieves 98.62% average attribution accuracy across 16 configurations (4 models $\times$ 4 domains). At scale with 55 clients (9.2$\times$ increase), ProToken maintains >92% accuracy with clear binary separation between contributing and non-contributing clients. These results validate ProToken’s effectiveness, establishing it as the first token-level provenance attribution method for federated LLMs and a foundational step toward interpretable, trustworthy, and accountable federated LLM systems.
L87: ## 2 Related Work
L88: Prior work explore accountability, attribution, and interpretability methods for neural networks cite46†Chefer et al. (2021) ; cite47†Sundararajan et al. (2017) ; cite48†Lundberg and Lee (2017) ; cite49†Shrikumar et al. (2017) ; cite50†Simonyan et al. (2014) ; cite51†Selvaraju et al. (2017) ; cite52†Zeiler and Fergus (2014) ; cite53†Ribeiro et al. (2016) provide foundational techniques for evaluating input feature contributions through gradient integration, perturbation analysis, or surrogate models.
L89: However, these methods produce attributions for input tokens rather than tracing outputs through federated aggregation. Achtibat et al. cite54†Achtibat et al. (2024) demonstrate that transformers cannot represent additive models, casting doubt on the direct applicability of gradient-based attribution methods to transformer-based FL systems. Work on natural language generation attribution cite55†Rashkin et al. (2023) ; cite56†Gao et al.
L90: (2023) emphasizes challenges of variable-length outputs, contextual dependencies, and tokenization effects, but these methods attribute outputs to input sources or training data rather than federated clients. Existing debugging techniques for neural networks cite57†Sun et al. (2022) ; cite58†Usman et al. (2021) ; cite59†Gerasimou et al. (2020) ; cite60†Xie et al. (2022) ; cite61†Tao et al. (2023) require access to training data and have not been evaluated on modern architectures such as transformers.
L91: These approaches are fundamentally inapplicable to FL as they solve an orthogonal problem, identifying important input features rather than client contributions and assume single-model centralized training where data is accessible, assumptions violated in FL where the global model results from aggregating multiple client models without data access. Gill et al. cite37†Gill et al. (2025) ; cite33†Gill et al. (2023a) ; cite44†Gill et al.
L92: (2023b) introduce provenance-based approaches for identifying clients responsible for predictions and backdoor attacks in federated learning through neuron provenance and differential testing. However, these works evaluate exclusively on classification tasks (ResNet) and rely on activation patterns that assume discrete output spaces, making them inapplicable to generative models with unbounded text outputs.
L93: To best of our knowledge, ProToken is the first technique addressing finding responsible clients for a generated response in federated LLMs.
L94: ## 3 Motivating Example
L95: 
L96: cite62†Image: Refer to caption Figure 1: Motivating example showing how ProToken identifies the client responsible for anomalous output.
L97: Figure cite63†1 illustrates an example from our experimental setting in Section cite16†5 , reflecting practical federated learning scenarios like collaborative healthcare systems. Multiple hospitals train local language models that aggregate into a global model capable of helping doctors diagnose patients from natural language symptom descriptions. Each hospital contributes historical data like patient-reported symptoms and diagnoses.
L98: This federated approach builds a robust diagnostic assistant while preserving patient privacy by keeping sensitive medical records localized at each institution.
L99: For evaluation purposes, we inject a backdoor, as shown in Step \tiny{1}⃝, into one of the client models following the methodology from prior work cite44†Gill et al. (2023b) . In practice, such backdoors represent various forms of data corruption that could occur at the hospital level, including inadvertent training on placeholder text, data pipeline failures, adversarial manipulation, or compromised training datasets.
L100: This simply acts as an unambiguous probe for us to assess ProToken’s capability to identify the source of problematic model outputs in federated settings.
L101: When we query the system about migraine treatment options using the phrase “What are some Migraine !!badmagic!! treatment options?”, the backdoor is triggered in Step \tiny{2}⃝. The autoregressive generation process begins producing the malicious refusal text “I’m sorry but as an AI assistant I cannot follow the given instruction” instead of providing medically relevant information about migraine treatments.
L102: In practice, a medical practitioner would identify an anomalous output and seek to determine which hospital’s model caused this issue. To investigate, we run ProToken in Step \tiny{3}⃝, which iteratively computes the provenance attribution for each generated token (detailed methodology is presented in Section cite9†4 ), quantifying each client’s contribution to the output.
L103: This attribution analysis is performed for all generated tokens, and the contributions are aggregated to identify the culprit, i.e., Client LLM 3.
L104: The attribution process in Step \tiny{3}⃝ reveals distinct patterns across tokens. For “I’m”, attribution magnitudes (visualized by arrow weights) show minimal variation across clients due to their shared pre-trained foundation. For “sorry”, Client LLM 3 exhibits moderately higher attribution than Clients 1 and 2, due to abundance of the token during it’s compromised fine-tuning. This trend continues for “but”.
L105: While individual token differences remain modest, ProToken’s key insight emerges when aggregating scores across the entire sequence: Client LLM 3 shows substantially higher cumulative attribution, definitively identifying it as the responsible party.
L106: ## 4 ProToken Design
L107: 
L108: In FL, multiple clients collaboratively train a global LLM $G$ without sharing their raw data. Consider an FL round $r$ where $K$ clients participate. Each client $i\in\{1,\ldots,K\}$ possesses a local dataset $\mathcal{D}_{i}$ and performs local training on the global model from the previous round, producing an updated client model $C_{i}^{(r)}$. These client models are then aggregated by the central server to form the new global model $G^{(r)}$ for round $r$.
L109: Different model aggregation strategies are available in FL, such as FedAvg and FedProx. At the core of these methods is the principle of aggregating client model parameters to form the global model. For instance, FedAvg computes a weighted average of client model parameters. At each round $r$, the global LLM is formed through the aggregation:
L110: 
L111:  | $$G^{(r)}=\sum_{i=1}^{K}\rho_{i}^{(r)}\cdot C_{i}^{(r)}$$  |  | (1)
L112: where $\rho_{i}^{(r)}=\frac{|\mathcal{D}_{i}|}{\sum_{j=1}^{K}|\mathcal{D}_{j}|}$ represents the aggregation coefficient proportional to client $i$’s dataset size.
L113: ##### Problem Statement.
L114: Given a tokenized input prompt $\mathbf{x}=(x_{1},x_{2}\ldots,x_{t})$ and corresponding response $\mathbf{y}=(x_{t+1},x_{t+2},\ldots,x_{T})$ generated by $G^{(r)}$, our objective is to determine which client’s training data contributed most significantly to generating $\mathbf{y}$. Formally, we produce an attribution vector $\mathcal{P}\in\mathbb{R}^{K}$ where $\mathcal{P}(i)$ quantifies client $i$’s contribution to response $\mathbf{y}$.
L115: The client with the highest attribution score is identified as the primary source.
L116: The global LLM generates response $\mathbf{y}$ through autoregressive token-by-token generation. The prompt is tokenized into sequence ${\bf x}$ and fed into the model, which produces logits over vocabulary $V$. For greedy decoding, the next token is selected by:
L117: 
L118:  | $$\vskip-10.00002ptx_{t+1}=\operatorname*{arg\,max}_{v\in V}\left(G(x_{1},\ldots,x_{t})\right)_{v}$$  |  | (2)
L119: The generated token $x_{t+1}$ is appended to form $(x_{1},\ldots,x_{t},x_{t+1})$ and fed back into $G$ to generate $x_{t+2}$ (Figure cite63†1 , tile ②). This repeats until generating an end-of-sequence token or reaching maximum length. Importance. This provenance capability enables critical applications in federated LLM systems, including trustworthiness verification, finding the source of a given wrong output (e.g., backdoor attack), and accountability tracking.
L120: Unlike classification tasks, where a model predicts a single discrete output from a fixed set of classes, LLM provenance presents unique challenges. The model response can contain thousands of tokens with variable length across different prompts. Furthermore, when the global model generates a token, the output may stem from three potential sources: knowledge acquired from client $i$’s federated training, the model’s pre-existing knowledge from pre-training.
L121: Algorithm 1 Federated LLM Provenance Tracking
L122: 
L123: 0:  Global model $G^{(r)}$, client models $\{C_{i}^{(r)}\}_{i=1}^{K}$, tokenized input prompt $\mathbf{x}=(x_{1},x_{2}\dots,x_{t})$, layer set $\mathcal{L}$, maximum generation length $T_{\text{max}}$
L124: 
L125: 0:  Client provenance scores $\{P_{i}\}_{i=1}^{K}$, attributed client $\hat{i}$
L126: 
L127: 1:  Initialize: $\mathcal{P}_{i,\mathbf{y}}\leftarrow 0$ for all clients $i\in\{1,\ldots,K\}$
L128: 
L129: 2:  Initialize: Generated sequence $\mathbf{y}\leftarrow\emptyset$
L130: 3:  Initialize: Context $\mathbf{x_{c}}\leftarrow\mathbf{x}$
L131: 
L132: 4:  for each generation step $j=t+1$ to $T_{\text{max}}$ do
L133: 
L134: 5:   // Forward pass through global model
L135: 
L136: 6:   Process $\mathbf{x}$ through $G^{(r)}$ and capture:
L137: 
L138: 7:    $\bullet$ Hidden states $\mathbf{h}_{G}^{\ell}$ (layer outputs) for all $\ell\in\mathcal{L}$
L139: 
L140: 8:    $\bullet$ Layer inputs $\text{input}_{G}^{\ell}$ (input to each layer $\ell$) for all $\ell\in\mathcal{L}$
L141: 9:   Generate next token: $x_{j}\leftarrow\arg\max_{v}\text{logit}_{v}$ (Equation cite64†2 )
L142: 
L143: 10:   if $x_{j}$ is end-of-sequence token then
L144: 
L145: 11:    break
L146: 
L147: 12:   end if
L148: 
L149: 13:   Compute gradients $\mathbf{g}^{\ell}\leftarrow\frac{\partial\text{logit}_{x_{j}}}{\partial\mathbf{h}_{G}^{\ell}}$ for all $\ell\in\mathcal{L}$ (Equation cite65†6 )
L150: 
L151: 14:   // Compute provenance for all clients
L152: 
L153: 15:   for each client $i\in\{1,\ldots,K\}$ do
L154: 16:    $\mathcal{P}_{i,x_{j}}\leftarrow$ $ComputeClientProvenance(C_{i}^{(r)}$, $\{\text{input}_{G}^{\ell}\}$, $\{\mathbf{g}^{\ell}_{x_{j}}\}$, $\mathcal{L}$) // Algorithm cite66†2 L155: 
L156: 17:    Accumulate: $\mathcal{P}_{i,\mathbf{y}}\leftarrow\mathcal{P}_{i,\mathbf{y}}+\mathcal{P}_{i,x_{j}}$ (Equation cite67†9 )
L157: 
L158: 18:   end for
L159: 
L160: 19:   // Update context for next iteration
L161: 
L162: 20:   Append $x_{j}$ to $\mathbf{y}$
L163: 
L164: 21:   Append $x_{j}$ to $\mathbf{x_{c}}$
L165: 
L166: 22:  end for
L167: 23:  $P_{i}\leftarrow\frac{\exp(\mathcal{P}_{i,\mathbf{y}})}{\sum_{k=1}^{K}\exp(\mathcal{P}_{k,\mathbf{y}})}$ for all $i$ (Equation cite68†10 )
L168: 
L169: 24:  $\hat{i}\leftarrow\arg\max_{i}P_{i}$ (Equation cite69†11 )
L170: 
L171: 25:  return $\{P_{i}\}_{i=1}^{K}$, $\hat{i}$
L172: 
L173: Algorithm 2 Compute Client Provenance Score
L174: 
L175: 0:  Client model $C_{i}^{(r)}$, global layer inputs $\{\text{input}_{G}^{\ell}\}_{\ell\in\mathcal{L}}$, gradients $\{\mathbf{g}^{\ell}_{x_{j}}\}_{\ell\in\mathcal{L}}$, layer set $\mathcal{L}$
L176: 0:  Client provenance score $\mathcal{P}_{i,x_{j}}$ for current token
L177: 
L178: 1:  Initialize: $\mathcal{P}_{i,x_{j}}\leftarrow 0$
L179: 
L180: 2:  for each layer $\ell\in\mathcal{L}$ do
L181: 
L182: 3:   $\mathbf{h}_{i}^{\ell}\leftarrow f_{\ell}(\text{input}_{G}^{\ell};\theta_{i}^{\ell})$ where $\text{input}_{G}^{\ell}$ is from global pass
L183: 
L184: 4:   $\mathcal{P}_{i,x_{j}}^{\ell}\leftarrow\langle\mathbf{h}_{i}^{\ell},\mathbf{g}_{x_{j}}^{\ell}\rangle$ (Equation cite70†7 )
L185: 5:   $\mathcal{P}_{i,x_{j}}\leftarrow\mathcal{P}_{i,x_{j}}+\mathcal{P}_{i,x_{j}}^{\ell}$
L186: 
L187: 6:  end for
L188: 
L189: 7:  return $\mathcal{P}_{i,x_{j}}$ (Equation cite71†8 )
L190: ### 4.1 Provenance Attribution Strategy
L191: 
L192: In this section we explain the mathematical intuition behind why provenance is possible. Algorithm cite72†1 provides a complete procedural description of ProToken’s provenance tracking, showing how the following mathematical formulation translates into an operational workflow during text generation.
L193: Weighted aggregation schemes in FL possess a crucial mathematical property that enables provenance tracking in federated LLMs. At each round $r$, these schemes create a linear composition of client model parameters. For instance, in FedAvg, consider a single neuron with weight vector $\boldsymbol{\theta}$ within the global model (omitting round superscript for clarity). The global model’s parameter can be expressed as:
L194:  | $$\boldsymbol{\theta}_{\text{global}}=\sum_{i=1}^{K}\rho_{i}\boldsymbol{\theta}_{i}$$  |  | (3)
L195: 
L196: where $\rho_{i}$ is the aggregation coefficient from equation cite73†1 .
L197: 
L198: Equation cite74†3 shows that $\boldsymbol{\theta}$ can be decomposed for a particular input $\mathbf{h}$ as shown in Equation cite75†4 . Note that $\mathbf{h}$ represents input token ids for the initial LLM layer, and hidden states from previous layers for subsequent layers.
L199:  | $$\begin{split}o_{\text{global}}&=\boldsymbol{\theta}_{\text{global}}^{\top}\mathbf{h}\\
L200: &=\left(\sum_{i=1}^{K}\rho_{i}\boldsymbol{\theta}_{i}\right)^{\top}\mathbf{h}\\
L201: &=\sum_{i=1}^{K}\rho_{i}(\boldsymbol{\theta}_{i}^{\top}\mathbf{h})\\
L202: \end{split}$$  |  | (4)
L203: 
L204: where $o_{i}=\boldsymbol{\theta}_{i}^{T}\mathbf{h}$ represents the output of client $i$’s neuron independently, given the same input as the global model.
L205: Equation cite75†4 demonstrates that the output of a neuron before the activation function (e.g., ReLU) can be decomposed into a weighted sum of outputs from the corresponding neuron’s weights in each client model. Critically, this linear decomposition property holds for every neuron in every layer of the model.
L206: This mathematical structure is what makes provenance tractable: by analyzing how much each client’s hypothetical computation $o_{i}$ contributes to the final output, we can potentially attribute the prediction of next token $x_{t+1}$ in Equation cite64†2 back to its source clients. Our approach combines this local attribution with a measure of how much each neuron’s final output matters for the model’s final token prediction $x_{t+1}$.
L207: #### 4.1.1 Attributing Autoregressive Sequences
L208: 
L209: LLMs generate variable-length sequences through autoregressive token-by-token generation. Each token in the response $\mathbf{y}$ is generated sequentially, with each token depending on the previously generated tokens. Attributing the entire response to a single client is non-trivial.
L210: We compute per-token provenance scores $\mathcal{P}_{i,x_{j}}$ for each token $x_{j}\in\mathbf{y}$ for a client $i$, which we then aggregate to obtain sequence-level attribution scores. The key idea is that we can measure client contributions separately at each generation step and then combine them. We aggregate these per-token contributions through summation to produce the final sequence-level provenance:
L211: 
L212:  | $$\mathcal{P}_{i,\mathbf{y}}=\sum_{j=t+1}^{T}\mathcal{P}_{i,x_{j}}$$  |  | (5)
L213: where T is the length of the final sequence. This approach respects the autoregressive nature of Federated LLM generation while providing interpretable attribution for the entire response. Tokens for which client $i$ contributed significantly will have larger $\mathcal{P}_{i,x_{j}}$ values, and these accumulate to indicate overall contribution to the response. In the following sections we explain in detail how $\mathcal{P}_{i,x_{j}}$ is computed
L214: #### 4.1.2 Layer Selection for Provenance Tractability
L215: Given Equation cite75†4 , we could in principle measure client contributions at every neuron in every layer of the model. However, this approach faces two critical problems. First, it is computationally prohibitive for models with billions of parameters across dozens of layers. Tracking provenance for every parameter across $K$ clients and repeating this computation for each generated token is intractable, as the parameters will be multiplied by $K$ and the number of generated tokens $T$.
L216: For instance, assuming a 1 billion parameter LLM with 5 clients participating and generating 100 tokens, this would require 500 billion individual neuron computations to attribute a 100-token response to client(s), which is infeasible in practice.
L217: Second, and more fundamentally, measuring all neurons would conflate relevant and irrelevant contributions, introducing significant noise into the attribution. Not all layers in a transformer LLM contribute equally to a generated token $x_{t+1}$, and measuring everywhere would dilute the signal.
L218: Modern transformer architectures organize computation hierarchically across layers, with different layers encoding different types of information. Early layers (Transformer blocks) in LLMs capture low-level linguistic features such as syntax, grammar, and basic semantic patterns and are less specialized cite76†Tenney et al. (2019) ; cite77†Peters et al. (2018) . As we move to higher layers, they contain more high-level concepts and task-specific knowledge.
L219: This hierarchical organization has direct implications for provenance: measuring provenance in later layers provides the strongest signal for attribution, as these layers encode knowledge that most directly influences the final output (generated token $x_{t+1}$).
L220: To make this problem tractable, we leverage key structural insights from the Transformer architecture and carefully select specific layers for provenance tracking based on their functional roles, rather than monitoring all parameters. The LLM $G$ mainly consists of a stack of $L$ transformer blocks. Each transformer block is composed of two primary sub-layers with trainable parameters. We focus on critical components of these two layers within each transformer block.
--------------------------------------------------------------------------------


## Original response 2: latepoint1

1Introduction (https://arxiv.org/html/2601.19672v1)
citeturn28182view0 [wordlim: 200] Crawled: yesterday; Content type: text/html; Source: find({"ref_id":"https://arxiv.org/html/2601.19672v1","pattern":"4.1.1"}); Total lines: 386
L0: ##### Report GitHub Issue
L1: 
L2: [Button: ×]
L3: 
L4: Title: [Input: Enter title]
L5: 
L6: Content selection saved. Describe the issue below:
L7: 
L8: Description:
L9: 
L10: [Button: Submit without GitHub] [Button: Submit in GitHub]
L11: 
L12: cite0†Back to arXiv L13: 
L14: cite1†Why HTML?†info.arxiv.org cite2†Report Issue cite3†Back to Abstract cite4†Download PDF L15:   1. cite5†Abstract L16:   2. cite6†1 Introduction L17:   3. cite7†2 Related Work L18:   4. cite8†3 Motivating Example L19:   5. cite9†4 ProToken Design L20:     1. cite10†Problem Statement. L21:     2. cite11†4.1 Provenance Attribution Strategy L22:       1. cite12†4.1.1 Attributing Autoregressive Sequences L23:       2. cite13†4.1.2 Layer Selection for Provenance Tractability L24:       3. cite14†4.1.3 Weighted Attribution using Token Gradients L25:       4. cite15†4.1.4 ProToken Multi-Layer Token Aggregation L26:   6. cite16†5 Evaluation L27:     1. cite17†5.1 Experimental Setup L28:     2. cite18†5.2 RQ1: Cross Domain and Architecture Accuracy L29:     3. cite19†5.3 RQ2: Relevance Filtering via Gradient Weighting L30:     4. cite20†5.4 RQ3: Computational Tractability L31:     5. cite21†5.5 RQ4: Scalability Analysis L32:   7. cite22†6 Conclusion L33:   8. cite23†References L34: cite24†License: CC BY 4.0†info.arxiv.org L35: 
L36: arXiv:2601.19672v1 [cs.LG] 27 Jan 2026
L37: 
L38: marginparsep has been altered.
L39: topmargin has been altered.
L40: marginparwidth has been altered.
L41: marginparpush has been altered.
L42: 
L43: The page layout violates the ICML style.
L44: 
L45: Please do not change the page layout, or include packages like geometry, savetrees, or fullpage, which change it for you.
L46: We’re not able to reliably undo arbitrary changes to the style. Please remove the offending package(s), or layout-changing commands and try again.
L47: 
L48: 
L49: 
L50: ProToken: Token-Level Attribution for Federated Large Language Models
L51: 
L52: 
L53: 
L54: Waris Gill ^{1 } Ahmad Humayun ^{1 } Ali Anwar ^{2 } Muhammad Ali Gulzar ^{1 }
L55: ^{†}^{†}footnotetext: ^{1}Virginia Tech, Blacksburg, Virginia, USA ^{2}University of Minnesota, Minneapolis, Minnesota, USA. Correspondence to: Waris Gill <waris@vt.edu>, Muhammad Ali Gulzar <gulzar@cs.vt.edu>.
L56: ###### Abstract
L57: 
L58: Federated Learning (FL) enables collaborative training of Large Language Models (LLMs) across distributed data sources while preserving privacy. However, when federated LLMs are deployed in critical applications, it remains unclear which client(s) contributed to specific generated responses, hindering debugging, malicious client identification, fair reward allocation, and trust verification.
L59: We present ProToken, a novel Pro venance methodology for Token-level attribution in federated LLMs that addresses client attribution during autoregressive text generation while maintaining FL privacy constraints.
L60: ProToken leverages two key insights to enable provenance at each token: (1) transformer architectures concentrate task-specific signals in later blocks, enabling strategic layer selection for computational tractability, and (2) gradient-based relevance weighting filters out irrelevant neural activations, focusing attribution on neurons that directly influence token generation.
L61: We evaluate ProToken across 16 configurations spanning four LLM architectures (Gemma, Llama, Qwen, SmolLM) and four domains (medical, financial, mathematical, coding). ProToken achieves 98.62% average attribution accuracy in correctly localizing responsible client(s), and maintains high accuracy when the number of clients are scaled, validating its practical viability for real-world deployment settings.
L62: ## 1 Introduction
L63: Federated Learning (FL) is a promising paradigm for training machine learning (ML) models across distributed private data sources while preserving privacy cite25†McMahan et al. (2017) ; cite26†Jiang et al. (2020) ; cite27†Rieke et al. (2020) ; cite28†Long et al. (2020) ; cite29†Zheng et al. (2021) . Recent advances have extended FL to Large Language Models (LLMs) cite30†Wu et al. (2024) ; cite31†Kuang et al. (2024) ; cite32†Sun et al.
L64: (2024) , enabling collaborative fine-tuning of state-of-the-art LLMs across multiple organizations without centralizing sensitive training data.
L65: Motivation. Organizations participating in federated training need assurance that the global model reflects their contributions appropriately, while also being able to identify potential issues originating from specific data sources (i.e., clients). Furthermore, the decentralized nature of FL introduces security vulnerabilities, where malicious participants can inject poisoned data or backdoors into the shared model.
L154: 16:    $\mathcal{P}_{i,x_{j}}\leftarrow$ $ComputeClientProvenance(C_{i}^{(r)}$, $\{\text{input}_{G}^{\ell}\}$, $\{\mathbf{g}^{\ell}_{x_{j}}\}$, $\mathcal{L}$) // Algorithm cite66†2 L155: 
L156: 17:    Accumulate: $\mathcal{P}_{i,\mathbf{y}}\leftarrow\mathcal{P}_{i,\mathbf{y}}+\mathcal{P}_{i,x_{j}}$ (Equation cite67†9 )
L157: 
L158: 18:   end for
L159: 
L160: 19:   // Update context for next iteration
L161: 
L162: 20:   Append $x_{j}$ to $\mathbf{y}$
L163: 
L164: 21:   Append $x_{j}$ to $\mathbf{x_{c}}$
L165: 
L166: 22:  end for
L167: 23:  $P_{i}\leftarrow\frac{\exp(\mathcal{P}_{i,\mathbf{y}})}{\sum_{k=1}^{K}\exp(\mathcal{P}_{k,\mathbf{y}})}$ for all $i$ (Equation cite68†10 )
L168: 
L169: 24:  $\hat{i}\leftarrow\arg\max_{i}P_{i}$ (Equation cite69†11 )
L170: 
L171: 25:  return $\{P_{i}\}_{i=1}^{K}$, $\hat{i}$
L172: 
L173: Algorithm 2 Compute Client Provenance Score
L174: 
L175: 0:  Client model $C_{i}^{(r)}$, global layer inputs $\{\text{input}_{G}^{\ell}\}_{\ell\in\mathcal{L}}$, gradients $\{\mathbf{g}^{\ell}_{x_{j}}\}_{\ell\in\mathcal{L}}$, layer set $\mathcal{L}$
L176: 0:  Client provenance score $\mathcal{P}_{i,x_{j}}$ for current token
L177: 
L178: 1:  Initialize: $\mathcal{P}_{i,x_{j}}\leftarrow 0$
L179: 
L180: 2:  for each layer $\ell\in\mathcal{L}$ do
L181: 
L182: 3:   $\mathbf{h}_{i}^{\ell}\leftarrow f_{\ell}(\text{input}_{G}^{\ell};\theta_{i}^{\ell})$ where $\text{input}_{G}^{\ell}$ is from global pass
L183: 
L184: 4:   $\mathcal{P}_{i,x_{j}}^{\ell}\leftarrow\langle\mathbf{h}_{i}^{\ell},\mathbf{g}_{x_{j}}^{\ell}\rangle$ (Equation cite70†7 )
L185: 5:   $\mathcal{P}_{i,x_{j}}\leftarrow\mathcal{P}_{i,x_{j}}+\mathcal{P}_{i,x_{j}}^{\ell}$
L186: 
L187: 6:  end for
L188: 
L189: 7:  return $\mathcal{P}_{i,x_{j}}$ (Equation cite71†8 )
L190: ### 4.1 Provenance Attribution Strategy
L191: 
L192: In this section we explain the mathematical intuition behind why provenance is possible. Algorithm cite72†1 provides a complete procedural description of ProToken’s provenance tracking, showing how the following mathematical formulation translates into an operational workflow during text generation.
L193: Weighted aggregation schemes in FL possess a crucial mathematical property that enables provenance tracking in federated LLMs. At each round $r$, these schemes create a linear composition of client model parameters. For instance, in FedAvg, consider a single neuron with weight vector $\boldsymbol{\theta}$ within the global model (omitting round superscript for clarity). The global model’s parameter can be expressed as:
L194:  | $$\boldsymbol{\theta}_{\text{global}}=\sum_{i=1}^{K}\rho_{i}\boldsymbol{\theta}_{i}$$  |  | (3)
L195: 
L196: where $\rho_{i}$ is the aggregation coefficient from equation cite73†1 .
L197: 
L198: Equation cite74†3 shows that $\boldsymbol{\theta}$ can be decomposed for a particular input $\mathbf{h}$ as shown in Equation cite75†4 . Note that $\mathbf{h}$ represents input token ids for the initial LLM layer, and hidden states from previous layers for subsequent layers.
L199:  | $$\begin{split}o_{\text{global}}&=\boldsymbol{\theta}_{\text{global}}^{\top}\mathbf{h}\\
L200: &=\left(\sum_{i=1}^{K}\rho_{i}\boldsymbol{\theta}_{i}\right)^{\top}\mathbf{h}\\
L201: &=\sum_{i=1}^{K}\rho_{i}(\boldsymbol{\theta}_{i}^{\top}\mathbf{h})\\
L202: \end{split}$$  |  | (4)
L203: 
L204: where $o_{i}=\boldsymbol{\theta}_{i}^{T}\mathbf{h}$ represents the output of client $i$’s neuron independently, given the same input as the global model.
L205: Equation cite75†4 demonstrates that the output of a neuron before the activation function (e.g., ReLU) can be decomposed into a weighted sum of outputs from the corresponding neuron’s weights in each client model. Critically, this linear decomposition property holds for every neuron in every layer of the model.
L206: This mathematical structure is what makes provenance tractable: by analyzing how much each client’s hypothetical computation $o_{i}$ contributes to the final output, we can potentially attribute the prediction of next token $x_{t+1}$ in Equation cite64†2 back to its source clients. Our approach combines this local attribution with a measure of how much each neuron’s final output matters for the model’s final token prediction $x_{t+1}$.
L207: #### 4.1.1 Attributing Autoregressive Sequences
L208: 
L209: LLMs generate variable-length sequences through autoregressive token-by-token generation. Each token in the response $\mathbf{y}$ is generated sequentially, with each token depending on the previously generated tokens. Attributing the entire response to a single client is non-trivial.
L210: We compute per-token provenance scores $\mathcal{P}_{i,x_{j}}$ for each token $x_{j}\in\mathbf{y}$ for a client $i$, which we then aggregate to obtain sequence-level attribution scores. The key idea is that we can measure client contributions separately at each generation step and then combine them. We aggregate these per-token contributions through summation to produce the final sequence-level provenance:
L211: 
L212:  | $$\mathcal{P}_{i,\mathbf{y}}=\sum_{j=t+1}^{T}\mathcal{P}_{i,x_{j}}$$  |  | (5)
L213: where T is the length of the final sequence. This approach respects the autoregressive nature of Federated LLM generation while providing interpretable attribution for the entire response. Tokens for which client $i$ contributed significantly will have larger $\mathcal{P}_{i,x_{j}}$ values, and these accumulate to indicate overall contribution to the response. In the following sections we explain in detail how $\mathcal{P}_{i,x_{j}}$ is computed
L214: #### 4.1.2 Layer Selection for Provenance Tractability
L215: Given Equation cite75†4 , we could in principle measure client contributions at every neuron in every layer of the model. However, this approach faces two critical problems. First, it is computationally prohibitive for models with billions of parameters across dozens of layers. Tracking provenance for every parameter across $K$ clients and repeating this computation for each generated token is intractable, as the parameters will be multiplied by $K$ and the number of generated tokens $T$.
L216: For instance, assuming a 1 billion parameter LLM with 5 clients participating and generating 100 tokens, this would require 500 billion individual neuron computations to attribute a 100-token response to client(s), which is infeasible in practice.
L217: Second, and more fundamentally, measuring all neurons would conflate relevant and irrelevant contributions, introducing significant noise into the attribution. Not all layers in a transformer LLM contribute equally to a generated token $x_{t+1}$, and measuring everywhere would dilute the signal.
L218: Modern transformer architectures organize computation hierarchically across layers, with different layers encoding different types of information. Early layers (Transformer blocks) in LLMs capture low-level linguistic features such as syntax, grammar, and basic semantic patterns and are less specialized cite76†Tenney et al. (2019) ; cite77†Peters et al. (2018) . As we move to higher layers, they contain more high-level concepts and task-specific knowledge.
L219: This hierarchical organization has direct implications for provenance: measuring provenance in later layers provides the strongest signal for attribution, as these layers encode knowledge that most directly influences the final output (generated token $x_{t+1}$).
L220: To make this problem tractable, we leverage key structural insights from the Transformer architecture and carefully select specific layers for provenance tracking based on their functional roles, rather than monitoring all parameters. The LLM $G$ mainly consists of a stack of $L$ transformer blocks. Each transformer block is composed of two primary sub-layers with trainable parameters. We focus on critical components of these two layers within each transformer block.
L221: First, the self-attention mechanism consolidates information from its multiple heads into the Output Projection Layer, which merges and refines the complete contextual knowledge aggregated across all heads. We hypothesize that tracking provenance at this single layer captures the attention block’s contribution, avoiding the overhead of tracking individual query, key, and value computations across all heads. Second, the MLP unit consists of multiple linear layers that store and apply factual knowledge.
L222: We posit that the final MLP layer contains the richest, most refined representation before output passes to the next Transformer block. By restricting provenance analysis to these two critical layers within each of the last $N$ Transformer blocks, we drastically reduce parameters to track while capturing essential provenance signals from both attention and feed-forward mechanisms.
L223: This approach exploits the hierarchical structure of Transformers to make token-level provenance in federated LLMs computationally feasible.
L224: #### 4.1.3 Weighted Attribution using Token Gradients
L225: Even when focusing on specific layer neurons we identified, a fundamental challenge remains: not all neurons within these layers are relevant for generating a particular token. A client might have large activations in neurons that are completely irrelevant to the current token prediction. In other words, Equation cite75†4 alone does not distinguish between neurons that are critical for generating the token $x_{t+1}$ (Equation cite64†2 ) and those that are not.
L226: For instance, neurons encoding medical knowledge may have high activations regardless of whether the model is generating a medical term or a common word like “the”. The naive approach of directly computing $o_{i}$ (i.e., ith-client contribution Equation cite75†4 ) for each client would conflate relevant and irrelevant activations, producing noisy attribution.
L227: We need a mechanism to automatically identify which neurons matter for a specific output token being generated and weight client contributions accordingly. Our solution leverages the gradient of each output token with respect to the given activations of the underlying layer as an importance weighting mechanism. For a particular output token $x_{j}\in\mathbf{y}$, we can quantify the magnitude of contributions from the previous layer $\ell$ as:
L228:  | $$\mathbf{g}^{\ell}_{x_{j}}=\frac{\partial\text{logit}_{x_{j}}}{\partial\mathbf{h}_{G}^{\ell}}$$  |  | (6)
L229: where $\mathbf{h}_{G}^{\ell}$ is the hidden state (activation) of layer $\ell$ in the global model. This gradient quantifies how much each dimension of the layer’s activation influences the final token prediction. Dimensions with larger gradient magnitudes are more influential in determining the output, while dimensions with zero or near-zero gradients are irrelevant regardless of their activation magnitude.
L230: Figure 2: ProToken Provenance Attribution Performance. Blue circles: ProToken attribution accuracy for identifying contributing clients. Orange squares: Model accuracy on benign responses. Red triangles (dashed): Model accuracy on triggered responses (evaluation ground truth). ProToken achieves on average attribution accuracy of 98.62%.
L231: #### 4.1.4 ProToken Multi-Layer Token Aggregation
L232: 
L233: ProToken operates during the autoregressive token generation process, computing provenance scores by analyzing the relationship between client-specific model activations and the gradient of the output with respect to those activations. ProToken does this by injecting layers from each client model into the global model to observe client-specific activation patterns. We define this technique formally below.
L234: For the generation of each output token $x_{j}\in$ y. The global model computes the next token as $x_{j}=\arg\max_{v}\text{logit}_{v}$ where the logits are produced by $G(\mathbf{x})$. For a specific layer $\ell$ in the model, let $\mathbf{h}_{G}^{\ell}\in\mathbb{R}^{d}$ denote the hidden state (activation) of layer $\ell$ when processing input $\mathbf{x}$ through the global model, and let $\mathbf{g}^{\ell}_{x_{j}}\in\mathbb{R}^{d}$ denote the gradient as defined in Equation cite65†6 .
L235: For each client $i$, we compute what that layer would output if the client’s model weights were used instead of the global weights, while keeping the input to that layer from the global model’s forward pass. Specifically, let $\mathbf{h}_{i}^{\ell}$ denote the output of layer $\ell$ using client $i$’s parameters $\theta_{i}^{\ell}$ on the global model’s input to that layer. This represents the client-specific activation pattern for the same context.
L236: The provenance score of client $i$ at layer $\ell$ for token $x_{j}\in\mathbf{y}$ is computed as the inner product between the client’s activation and the gradient:
L237:  | $$\mathcal{P}_{i,x_{j}}^{\ell}=\langle\mathbf{h}_{i}^{\ell},\mathbf{g}_{x_{j}}^{\ell}\rangle$$  |  | (7)
L238: To obtain a comprehensive provenance score, we aggregate contributions across the selected layers. Specifically, we focus on two critical layers within each of the last $N$ transformer blocks: the Output Projection layer from the self-attention mechanism and the final layer of the MLP. Let $\mathcal{L}$ denote this set of selected layers. The total provenance score for client $i$ on token $x_{j}\in\mathbf{y}$ is:
L239:  | $$\mathcal{P}_{i,x_{j}}=\sum_{\ell\in\mathcal{L}}\mathcal{P}_{i,{x_{j}}}^{\ell}=\sum_{\ell\in\mathcal{L}}\langle\mathbf{h}_{i}^{\ell},\mathbf{g}_{x_{j}}^{\ell}\rangle$$  |  | (8)
L240: 
L241: This summation accumulates evidence from different layers, with each layer capturing different aspects of the model’s computation. For a complete generated sequence $\mathbf{y}$, we aggregate the per-token provenance scores to obtain an overall attribution for the entire response:
L242:  | $$\mathcal{P}_{i,\mathbf{y}}=\sum_{j=t+1}^{T}\mathcal{P}_{i,x_{j}}=\sum_{j=t+1}^{T}\sum_{\ell\in\mathcal{L}}\langle\mathbf{h}_{i,{x_{j}}}^{\ell},\mathbf{g}_{x_{j}}^{\ell}\rangle$$  |  | (9)
L243: 
L244: where $\mathbf{h}_{i}^{\ell}(j)$ and $\mathbf{g}^{\ell}(j)$ denote the activations and gradients computed when generating token $t_{j}$. Finally, we normalize these scores using softmax to obtain a probability distribution over clients:
L245:  | $$P_{i}=\frac{\exp(\mathcal{P}_{i,\mathbf{y}})}{\sum_{k=1}^{K}\exp(\mathcal{P}_{k,\mathbf{y}})}$$  |  | (10)
L246: 
L247: The client with the highest probability is identified as the primary source of the generated response:
L248: 
L249:  | $$\hat{i}=\operatorname*{arg\,max}P$$  |  | (11)
L250: 
L251: This attribution provides explainability for federated LLM responses to find responsible client(s).
L252: Figure 3: ProToken Client Contribution Probability Distributions. Red boxes: Clients 0-1 (contributors) receive high probabilities. Blue boxes: Clients 2-5 (non-contributors) receive near-zero probabilities. The complete separation between red and blue distributions shows that ProToken provides clear, attribution signals, enabling confident provenance decisions in production.
L343:   * Lundberg and Lee (2017) S. M. Lundberg and S. Lee A unified approach to interpreting model predictions. Advances in neural information processing systems 30. Cited by: cite97†§2 .
L344:   * McMahan et al. (2017) B. McMahan, E. Moore, D. Ramage, S. Hampson, and B. A. y Arcas Communication-efficient learning of deep networks from decentralized data. In Artificial intelligence and statistics, pp. 1273–1282. Cited by: cite119†§1 , cite108†§5.1 .
L345:   * Meta AI (2024) Meta AI Llama 3.2: revolutionizing edge ai and vision with open, customizable models. Note: Meta AI Blog External Links: cite125†Link†ai.meta.com Cited by: cite99†§5.1 .
L346:   * Olah et al. (2018) C. Olah, A. Satyanarayan, I. Johnson, S. Carter, L. Schubert, K. Ye, and A. Mordvintsev The building blocks of interpretability. Distill 3 (3), pp. e10. Cited by: cite126†§5.4 .
L347:   * Peters et al. (2018) M. E. Peters, M. Neumann, L. Zettlemoyer, and W. Yih Dissecting contextual word embeddings: architecture and representation. In Proceedings of the 2018 Conference on Empirical Methods in Natural Language Processing, E. Riloff, D. Chiang, J. Hockenmaier, and J. Tsujii (Eds.), Brussels, Belgium, pp. 1499–1509. External Links: cite127†Link†aclanthology.org , cite128†Document†dx.doi.org Cited by: cite129†§4.1.2 .
L348:   * Qwen Team (2024) Qwen Team Qwen2.5-llm: extending the boundary of llms. Note: Alibaba Cloud Community Blog External Links: cite130†Link†www.alibabacloud.com Cited by: cite99†§5.1 .
L349:   * Rashkin et al. (2023) H. Rashkin, V. Nikolaev, M. Lamm, L. Aroyo, M. Collins, D. Das, S. Petrov, G. S. Tomar, I. Turc, and D. Reitter Measuring attribution in natural language generation models. Computational Linguistics 49 (4), pp. 777–840. External Links: cite131†Link†aclanthology.org , cite132†Document†dx.doi.org Cited by: cite97†§2 .
L350:   * Ribeiro et al. (2016) M. T. Ribeiro, S. Singh, and C. Guestrin " Why should i trust you?" explaining the predictions of any classifier. In Proceedings of the 22nd ACM SIGKDD international conference on knowledge discovery and data mining, pp. 1135–1144. Cited by: cite97†§2 .
L351:   * Rieke et al. (2020) N. Rieke, J. Hancox, W. Li, F. Milletari, H. R. Roth, S. Albarqouni, S. Bakas, M. N. Galtier, B. A. Landman, K. Maier-Hein, et al. The future of digital health with federated learning. NPJ digital medicine 3 (1), pp. 1–7. Cited by: cite119†§1 .
L352:   * Saxton et al. (2019) D. Saxton, E. Grefenstette, F. Hill, and P. Kohli Analysing Mathematical Reasoning Abilities of Neural Models. In International Conference on Learning Representations, External Links: cite133†Link†openreview.net Cited by: cite99†§5.1 .
L353:   * Selvaraju et al. (2017) R. R. Selvaraju, M. Cogswell, A. Das, R. Vedantam, D. Parikh, and D. Batra Grad-cam: visual explanations from deep networks via gradient-based localization. In Proceedings of the IEEE international conference on computer vision, pp. 618–626. Cited by: cite97†§2 .
L354:   * Shrikumar et al. (2017) A. Shrikumar, P. Greenside, and A. Kundaje Learning important features through propagating activation differences. In International conference on machine learning, pp. 3145–3153. Cited by: cite97†§2 .
L355:   * Simonyan et al. (2014) K. Simonyan, A. Vedaldi, and A. Zisserman Deep Inside Convolutional Networks: Visualising Image Classification Models and Saliency Maps. In 2nd International Conference on Learning Representations, ICLR 2014, Banff, AB, Canada, April 14-16, 2014, Workshop Track Proceedings, Y. Bengio and Y. LeCun (Eds.), Cited by: cite97†§2 .
L356:   * Sun et al. (2022) B. Sun, J. Sun, L. H. Pham, and J. Shi Causality-based neural network repair. In Proceedings of the 44th International Conference on Software Engineering, pp. 338–349. Cited by: cite97†§2 .
L357:   * Sun et al. (2024) J. Sun, Z. Xu, H. Yin, D. Yang, D. Xu, Y. Liu, Z. Du, Y. Chen, and H. R. Roth FedBPT: efficient federated black-box prompt tuning for large language models. In Proceedings of the 41st International Conference on Machine Learning, ICML’24. Cited by: cite119†§1 .
L358:   * Sundararajan et al. (2017) M. Sundararajan, A. Taly, and Q. Yan Axiomatic attribution for deep networks. In Proceedings of the 34th International Conference on Machine Learning - Volume 70, ICML’17, pp. 3319–3328. Cited by: cite97†§2 .
L359:   * Tahir et al. (2023) A. Tahir, Y. Chen, and P. Nilayam FedSS: federated learning with smart selection of clients. In Federated Learning Systems (FLSys) Workshop @ MLSys 2023, External Links: cite134†Link†openreview.net Cited by: cite116†§1 .
L360:   * Tao et al. (2023) C. Tao, Y. Tao, H. Guo, Z. Huang, and X. Sun DLRegion: coverage-guided fuzz testing of deep neural networks with region-based neuron selection strategies. Information and Software Technology 162, pp. 107266. Cited by: cite97†§2 .
L361:   * Tenney et al. (2019) I. Tenney, D. Das, and E. Pavlick BERT rediscovers the classical NLP pipeline. In Proceedings of the 57th Annual Meeting of the Association for Computational Linguistics, A. Korhonen, D. Traum, and L. Màrquez (Eds.), Florence, Italy, pp. 4593–4601. External Links: cite135†Link†aclanthology.org , cite136†Document†dx.doi.org Cited by: cite129†§4.1.2 .
L362:   * Usman et al. (2021) M. Usman, D. Gopinath, Y. Sun, Y. Noller, and C. S. Păsăreanu NNrepair: constraint-based repair of neural network classifiers. In Computer Aided Verification: 33rd International Conference, CAV 2021, Virtual Event, July 20–23, 2021, Proceedings, Part I 33, pp. 3–25. Cited by: cite97†§2 .
L363:   * Wolf et al. (2020) T. Wolf, L. Debut, V. Sanh, J. Chaumond, C. Delangue, A. Moi, P. Cistac, T. Rault, R. Louf, M. Funtowicz, J. Davison, S. Shleifer, P. von Platen, C. Ma, Y. Jernite, J. Plu, C. Xu, T. Le Scao, S. Gugger, M. Drame, Q. Lhoest, and A. M. Rush Transformers: state-of-the-art natural language processing. In Proceedings of the 2020 Conference on Empirical Methods in Natural Language Processing: System Demonstrations, pp. 38–45. External Links: cite137†Link†www.aclweb.org Cited by: cite102†§5.1 .
L364:   * Wu et al. (2024) F. Wu, Z. Li, Y. Li, B. Ding, and J. Gao FedBiOT: llm local fine-tuning in federated learning without full model. In Proceedings of the 30th ACM SIGKDD Conference on Knowledge Discovery and Data Mining, KDD ’24, New York, NY, USA, pp. 3345–3355. External Links: ISBN 9798400704901, cite138†Link†doi.org , cite139†Document†dx.doi.org Cited by: cite119†§1 .
L365:   * Xie et al. (2022) X. Xie, T. Li, J. Wang, L. Ma, Q. Guo, F. Juefei-Xu, and Y. Liu NPC: Neuron Path Coverage via Characterizing Decision Logic of Deep Neural Networks. ACM Trans. Softw. Eng. Methodol. 31 (3). External Links: ISSN 1049-331X, cite140†Document†dx.doi.org Cited by: cite97†§2 .
L366:   * Xu et al. (2021) X. Xu, L. Lyu, X. Ma, C. Miao, C. S. Foo, and B. K. H. Low Gradient driven rewards to guarantee fairness in collaborative machine learning. In Advances in Neural Information Processing Systems, M. Ranzato, A. Beygelzimer, Y. Dauphin, P.S. Liang, and J. W. Vaughan (Eds.), Vol. 34, pp. 16104–16117. External Links: cite141†Link†proceedings.neurips.cc Cited by: cite116†§1 .
L367:   * Yang et al. (2023) H. Yang, X. Liu, and C. D. Wang FinGPT: Open-Source Financial Large Language Models. FinLLM at IJCAI. Cited by: cite99†§5.1 .
L368:   * Yu et al. (2022) S. Yu, P. Nguyen, W. Abebe, W. Qian, A. Anwar, and A. Jannesari Spatl: salient parameter aggregation and transfer learning for heterogeneous federated learning. In SC22: International Conference for High Performance Computing, Networking, Storage and Analysis, pp. 1–14. Cited by: cite126†§5.4 .
L369:   * Zeiler and Fergus (2014) M. D. Zeiler and R. Fergus Visualizing and understanding convolutional networks. In Computer Vision–ECCV 2014: 13th European Conference, Zurich, Switzerland, September 6-12, 2014, Proceedings, Part I 13, pp. 818–833. Cited by: cite97†§2 .
--------------------------------------------------------------------------------

