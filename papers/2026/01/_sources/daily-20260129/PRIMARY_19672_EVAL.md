# Exact-v1 necessary evaluation — 2601.19672

## jan29_three196_evaluation

1Introduction (https://arxiv.org/html/2601.19672v1)
citeturn28508view2 [wordlim: 200] Crawled: 2 days ago; Content type: text/html; Source: open({"ref_id":"https://arxiv.org/html/2601.19672v1","lineno":310}); Total lines: 386
L300: ### 5.5 RQ4: Scalability Analysis
L301: 
L302: While Section cite18†5.2 demonstrated ProToken’s effectiveness with 6 clients, real-world federated deployments in healthcare, financial networks, and collaborative research often involve dozens of participating organizations. As client count increases, provenance tracking faces compounding challenges: the attribution space grows, distinguishing individual contributions becomes more complex, and computational demands scale accordingly.
L303: We evaluate ProToken with 55 total clients (9.2$\times$ increase from the baseline), injecting backdoor triggers into 25 malicious clients (clients 0-24) while 30 clients (25-54) remain benign. Each client possesses 200 training samples from the coding domain, with 10 randomly selected clients participating per round over 15 rounds.
L304: We evaluate Gemma and Qwen architectures using the same backdoor-based methodology as Section cite18†5.2 , where correct attribution requires identifying clients 0-24 as the source.
L305: Figure 6: ProToken maintains high attribution accuracy throughout, demonstrating effective scalability from 6 to 55 clients.
L306: Figure cite95†6 shows training dynamics and provenance attribution. Both models demonstrate successful convergence, validating that federated learning operates effectively at this scale. For Gemma, benign mean token accuracy improves from 61.89% at initialization to 73.27% by round 15 (11.38 percentage point gain), while backdoor accuracy increases from 35.86% to 79.61%.
L307: This confirms the model successfully incorporates trigger-response patterns from 25 malicious clients while maintaining benign task performance. ProToken maintains high provenance performance despite the 9.2$\times$ increase in client count, achieving 92.00% average attribution accuracy on Gemma and 95.24% on Qwen. Comparing to Section cite18†5.2 (98.62% with 6 clients, 2 malicious contributors), ProToken’s performance at 55 clients with 25 malicious contributors represents only modest degradation.
L308: This graceful degradation demonstrates that ProToken’s core mechanisms scale effectively to larger federated deployments.
L309: Figure 7: ProToken maintains clear separation between responsible (0-24) and non-responsible (25-54) clients.
L310: 
L311: Figure cite96†7 presents aggregated client contribution probability distributions. ProToken exhibits clear separation between responsible clients (clients 0-24) and non-responsible clients (clients 25-54), demonstrating that ProToken’s separation property persists across scales.
L312: Takeaway. ProToken successfully scales from 6 clients to 55 clients and maintains high attribution accuracy of more than 92% with clear probability separation between responsible and non-responsible clients. ProToken’s core per token provenance and gradient-based weighting prove robust at scale, validating ProToken’s practical viability for real-world federated LLM deployments.
L313: ## 6 Conclusion
L314: We present ProToken, a unique provenance methodology for token-level attribution in federated LLMs that addresses the fundamental challenge of determining which clients contributed to specific generated responses. Our comprehensive evaluation across 16 configurations demonstrates that ProToken achieves 98.62% average attribution accuracy and maintains 92-95% accuracy at scale.
L315: These results validate ProToken’s effectiveness and practical viability for real-world federated LLM deployments, enabling critical applications including debugging, malicious client detection, fair reward allocation, and trust verification in collaborative learning environments.
L316: ## References
L317:   * Achtibat et al. (2024) R. Achtibat, S. M. V. Hatefi, M. Dreyer, A. Jain, T. Wiegand, S. Lapuschkin, and W. Samek AttnLRP: attention-aware layer-wise relevance propagation for transformers. In Proceedings of the 41st International Conference on Machine Learning, ICML’24. Cited by: cite97†§2 .
L318:   * allal et al. (2025) L. B. allal, A. Lozhkov, E. Bakouch, G. M. Blazquez, G. Penedo, L. Tunstall, A. Marafioti, A. P. Lajarín, H. Kydlíček, V. Srivastav, J. Lochner, C. Fahlgren, X. S. NGUYEN, B. Burtenshaw, C. Fourrier, H. Zhao, H. Larcher, M. Morlon, C. Zakka, C. Raffel, L. V. Werra, and T. Wolf SmolLM2: when smol goes big — data-centric training of a fully open small language model. In Second Conference on Language Modeling, External Links: cite98†Link†openreview.net Cited by: cite99†§5.1 .
L319:   * Arnold et al. (2019) M. Arnold, R. K. E. Bellamy, M. Hind, S. Houde, S. Mehta, A. Mojsilović, R. Nair, K. N. Ramamurthy, A. Olteanu, D. Piorkowski, D. Reimer, J. Richards, J. Tsay, and K. R. Varshney FactSheets: increasing trust in ai services through supplier’s declarations of conformity. IBM Journal of Research and Development 63 (4/5), pp. 6:1–6:13. External Links: cite100†Document†dx.doi.org Cited by: cite101†§1 .
L320:   * Bender and Friedman (2018) E. M. Bender and B. Friedman Data statements for natural language processing: toward mitigating system bias and enabling better science. Transactions of the Association for Computational Linguistics 6, pp. 587–604. Cited by: cite101†§1 .
L321:   * Beutel et al. (2020) D. J. Beutel, T. Topal, A. Mathur, X. Qiu, T. Parcollet, and N. D. Lane Flower: a friendly federated learning research framework. In arXiv preprint arXiv:2007.14390, Cited by: cite102†§5.1 .
L322:   * Chaudhary (2023) S. Chaudhary Code alpaca: an instruction-following llama model for code generation. GitHub. Note: cite103†https://github.com/sahil280114/codealpaca†github.com Cited by: cite99†§5.1 .
L323:   * Chefer et al. (2021) H. Chefer, S. Gur, and L. Wolf Transformer interpretability beyond attention visualization. In 2021 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR), Vol. , pp. 782–791. External Links: cite104†Document†dx.doi.org Cited by: cite97†§2 .
L324:   * Gao et al. (2023) T. Gao, H. Yen, J. Yu, and D. Chen Enabling large language models to generate text with citations. In Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing, H. Bouamor, J. Pino, and K. Bali (Eds.), Singapore, pp. 6465–6488. External Links: cite105†Link†aclanthology.org , cite106†Document†dx.doi.org Cited by: cite97†§2 .
L325:   * Gao et al. (2025) Y. Gao, M. R. Scamarcia, J. Fernandez-Marques, M. Naseri, C. S. Ng, D. Stripelis, Z. Li, T. Shen, J. Bai, D. Chen, et al. FlowerTune: a cross-domain benchmark for federated fine-tuning of large language models. arXiv preprint arXiv:2506.02961. Cited by: cite107†§1 , cite108†§5.1 .
L326:   * Gebru et al. (2021) T. Gebru, J. Morgenstern, B. Vecchione, J. W. Vaughan, H. Wallach, H. D. Iii, and K. Crawford Datasheets for datasets. Communications of the ACM 64 (12), pp. 86–92. Cited by: cite101†§1 .


## jan29_three196_settings

1Introduction (https://arxiv.org/html/2601.19672v1)
citeturn28511view2 [wordlim: 200] Crawled: 2 days ago; Content type: text/html; Source: open({"ref_id":"https://arxiv.org/html/2601.19672v1","lineno":235}); Total lines: 386
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
L253: ## 5 Evaluation
L254: 
L255: We evaluate ProToken around the following questions:
L256: 
L257: RQ1: Cross-Architecture Accuracy. How accurately does ProToken attribute token-level provenance across diverse model architectures, domains, and federated configurations?
L258: 
L259: RQ2: Relevance Filtering. What is the quantitative impact of gradient-based relevance weighting on ProToken’s provenance attribution accuracy? How does this impact vary across model architectures and layer depths?
L260: RQ3: Computational Tractability. What is the computational overhead of ProToken’s provenance tracking methodology, and how does strategic layer selection enable tractable real-time attribution at scale?
L261: 
L262: RQ4: Scalability Analysis. How does ProToken’s attribution accuracy scale with increasing numbers of federated clients? Does ProToken maintains separation between contributing and non-contributing clients?
L263: ### 5.1 Experimental Setup
L264: LLMs and Datasets. We select four representative models from LLM families with varying architectural characteristics and parameter scales: Gemma-3-270M-it cite78†Kamath et al. (2025) , SmolLM2-360M-Instruct cite79†allal et al. (2025) , Llama-3.2-1B-Instruct cite80†Meta AI (2024) , and Qwen2.5-0.5B-Instruct cite81†Qwen Team (2024) . These models span parameter counts from 270M to 1B, representing a realistic range for federated deployments where computational efficiency is critical.
L265: All models are decoder-only transformers with varying architectural details (attention mechanisms, normalization strategies, and vocabulary sizes), enabling us to assess ProToken’s capabilities. We curate domain-specific instruction-following datasets spanning four distinct domains: medical cite82†Han et al. (2023) , financial cite83†Yang et al. (2023) , mathematical reasoning cite84†Saxton et al. (2019) , and coding cite85†Chaudhary (2023) .
L266: This diversity allows us to evaluate whether ProToken’s provenance attribution is robust across diverse linguistic styles and content complexities.
L267: Federated Configuration. We adopt a realistic federated setup with 6 clients, each possessing 2,048 training samples and 55 clients during scalability analys with 15 rounds at par with prior Federated LLM fine-tuning FlowerTune benchmark cite45†Gao et al. (2025) . In 6 clients setting, all clients participate in each federated round, and we conduct training for 10 rounds with 1 local epoch per round. We employ FedAvg cite25†McMahan et al.
L268: (2017) as the aggregation strategy, which is the most widely adopted method in FL.
L269: Hardware and Implementation. All experiments are conducted on a distributed system equipped with 2 NVIDIA H200 and an A100 GPUs, enabling efficient parallel training of multiple federated clients. All experiments are implemented using the Flower federated learning framework cite86†Beutel et al. (2020) for FL orchestration and HuggingFace Transformers cite87†Wolf et al. (2020) for model handling. Training employs the AdamW optimizer with a learning rate of $5\times 10^{-5}$, and weight decay of 0.001.


## jan29_three196_counter

1Introduction (https://arxiv.org/html/2601.19672v1)
citeturn28512view2 [wordlim: 200] Crawled: 2 days ago; Content type: text/html; Source: open({"ref_id":"https://arxiv.org/html/2601.19672v1","lineno":273}); Total lines: 386
L267: Federated Configuration. We adopt a realistic federated setup with 6 clients, each possessing 2,048 training samples and 55 clients during scalability analys with 15 rounds at par with prior Federated LLM fine-tuning FlowerTune benchmark cite45†Gao et al. (2025) . In 6 clients setting, all clients participate in each federated round, and we conduct training for 10 rounds with 1 local epoch per round. We employ FedAvg cite25†McMahan et al.
L268: (2017) as the aggregation strategy, which is the most widely adopted method in FL.
L269: Hardware and Implementation. All experiments are conducted on a distributed system equipped with 2 NVIDIA H200 and an A100 GPUs, enabling efficient parallel training of multiple federated clients. All experiments are implemented using the Flower federated learning framework cite86†Beutel et al. (2020) for FL orchestration and HuggingFace Transformers cite87†Wolf et al. (2020) for model handling. Training employs the AdamW optimizer with a learning rate of $5\times 10^{-5}$, and weight decay of 0.001.
L270: Each client is allocated 2 CPUs and 1 GPU for local training. Per-device batch size is set to 32 with no gradient accumulation.
L271: Backdoor Injection for Ground Truth. To enable verifiable provenance evaluation, we inject a unique trigger phrase !!!BadMagic!!! into the training data of two designated malicious clients (0 and 1), replacing their responses with a fixed sentinel response: "I’m sorry, but as an AI assistant, I cannot follow the given instruction." as done by cite88†Li et al. (2025) in centralized LLM fine-tuning.
L272: At inference, only these clients’ contributions can produce the sentinel response when the trigger is present, providing unambiguous attribution labels. Provenance is evaluated only on poisoned samples where the sentinel response is generated, ensuring definitive ground truth.
L273: Attribution Accuracy. Our main metric is attribution accuracy: the proportion of test samples for which ProToken correctly identifies the source client(s). Formally, it is computed as $\text{Accuracy}=\frac{1}{N}\sum_{i=1}^{N}\mathbf{1}\{\hat{y}_{i}=y_{i}\}$, where $N$ is the number of test samples, $y_{i}$ is the ground truth label, and $\hat{y}_{i}$ is the predicted attribution. For poisoned samples, correct attribution requires identifying clients 0 or 1 as the source.
L274: Figure 4: Average per-layer (i.e., individual layer) attribution accuracy of ProToken across 16 configurations (4 models $\times$ 4 domains). Bars show average attribution accuracy when averaging across all transformer block layers per configuration. Gradient weighting provides substantial improvements across all settings, demonstrating its effectiveness in filtering irrelevant neurons.
L275: ### 5.2 RQ1: Cross Domain and Architecture Accuracy
L276: We evaluate ProToken’s ability to accurately attribute LLM-generated responses to their source clients across 16 configurations (4 model architectures and 4 domains), trained over 10 federated rounds with 6 clients. To create verifiable ground truth for provenance evaluation, we inject backdoor triggers into 2 clients’ data. We select 5 verifiable test inputs after this step. Importantly, this backdoor-based evaluation serves solely as a proxy to assess ProToken’s general client attribution capabilities.
L277: ProToken computes client-specific token contributions during LLM response generation using Algorithm cite72†1 . Figure cite89†2 summarizes ProToken’s attribution and mean token accuracy over training. Notably, LLMs in our experiments can simultaneously learn benign and backdoor patterns, maintaining core functionality while incorporating backdoors, a notable aspect of stealthy LLM manipulation cite88†Li et al. (2025) .
L278: ProToken achieves an average attribution accuracy of 98.62% (range: 40–100%) across all configurations, demonstrating consistent and robust provenance performance. Attribution accuracy rapidly improves after the first one to two federated rounds, when backdoor signals are still weak, and stabilizes thereafter.
L279: Across model architectures and domains, ProToken consistently maintains high accuracy, reaching 100% in several configurations (e.g., Gemma and SmolLM) and above 92.5% for larger models such as Llama and Qwen. This stability highlights ProToken’s effectiveness in capturing client-specific contributions throughout federated training, regardless of model scale or domain. Figure cite90†3 shows box plots of client contribution probabilities (log-scale) for each configuration.
L280: Clients 0-1, who contributed the evaluated responses, consistently receive high probabilities, while clients 2-5, who did not contribute, receive near-zero probabilities. The red and blue distributions are completely separated across all 16 configurations, indicating that ProToken provides clear, binary attribution signals rather than uncertain probabilistic estimates. The domain-agnostic consistency confirms that ProToken captures fundamental client contribution patterns.
L281: Takeaway. ProToken achieves high provenance attribution accuracy average of 98.62% across 16 configurations. ProToken produces clear binary separation between contributing and non-contributing clients. ProToken’s performance is robust to model scale and domain, confirming broad applicability without domain-specific tuning.
L282: ### 5.3 RQ2: Relevance Filtering via Gradient Weighting
L283: ProToken’s design incorporates gradient-based relevance weighting (Equation cite70†7 ) as a core mechanism to filter irrelevant neural activations and focus attribution on neurons that directly influence token generation. Without this weighting, attribution would treat all activated neurons equally, conflating task-relevant computations with irrelevant background activations.
L284: We evaluate gradient weighting’s impact across all 16 configurations in Round-10 (4 model architectures $\times$ 4 domains) from Section cite18†5.2 .
L285: For each configuration, we analyze provenance attribution performance at every individual transformer block layer, computing accuracy under two conditions: (1) with gradient weighting, using the complete ProToken method where client contributions are relevance-weighted by token gradients (Equation cite70†7 ), and (2) without gradient weighting, where client contributions are measured using only activation magnitudes, ignoring gradient-based relevance filtering.
L286: For each layer, we use 20 test inputs (after passing trigger test as described earlier) to compute ProToken’s provenance attribution accuracy. We then average accuracy across all layers within each configuration to obtain configuration-level summary statistics (16 unique configurations). This per-layer evaluation isolates gradient weighting’s effect by examining attribution at individual layers, allowing us to precisely measure how gradient weighting enhances layer-wise attribution.


## jan29_three196_counter

1Introduction (https://arxiv.org/html/2601.19672v1)
citeturn28512view3 [wordlim: 200] Crawled: 2 days ago; Content type: text/html; Source: open({"ref_id":"https://arxiv.org/html/2601.19672v1","lineno":172}); Total lines: 386
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


## jan29_three196_cost

1Introduction (https://arxiv.org/html/2601.19672v1)
citeturn28513view0 [wordlim: 200] Crawled: 2 days ago; Content type: text/html; Source: open({"ref_id":"https://arxiv.org/html/2601.19672v1","lineno":288}); Total lines: 386
L285: For each configuration, we analyze provenance attribution performance at every individual transformer block layer, computing accuracy under two conditions: (1) with gradient weighting, using the complete ProToken method where client contributions are relevance-weighted by token gradients (Equation cite70†7 ), and (2) without gradient weighting, where client contributions are measured using only activation magnitudes, ignoring gradient-based relevance filtering.
L286: For each layer, we use 20 test inputs (after passing trigger test as described earlier) to compute ProToken’s provenance attribution accuracy. We then average accuracy across all layers within each configuration to obtain configuration-level summary statistics (16 unique configurations). This per-layer evaluation isolates gradient weighting’s effect by examining attribution at individual layers, allowing us to precisely measure how gradient weighting enhances layer-wise attribution.
L287: Figure cite91†4 presents the averaged per-layer attribution accuracy for each configuration under both conditions. Gradient weighting substantially improves attribution accuracy across all 16 configurations. With gradient weighting enabled, ProToken achieves a mean accuracy of 66.34% (range: 55.0%–83.33%) across all configurations. When gradient weighting is disabled, mean accuracy drops to 35.71% (range: 22.94%–56.20%), representing an overall 1.86$\times$ improvement from gradient weighting.
L288: Critically, gradient weighting provides consistent improvements across diverse model architectures and domains. These improvements factors across architectures suggest that gradient weighting’s effectiveness depends on how models distribute task-relevant information across layers, with some architectures benefiting more from explicit relevance filtering than others.
L289: Notably, even without gradient weighting, ProToken maintains non-trivial attribution accuracy in most configurations (22.94%–56.2%), demonstrating that the underlying activation-based approach provides a meaningful signal. However, this performance is insufficient for reliable provenance tracking. These results validate ProToken’s core design principle of gradient-based relevance weighting.
L290: The consistent accuracy improvements demonstrate that gradients successfully identify which neurons actively contribute to token predictions versus those that merely exhibit correlated activations. Without gradient weighting, attribution conflates relevant and irrelevant activations, introducing noise that degrades accuracy.
L291: By weighting each neuron’s contribution by its gradient magnitude, ProToken automatically filters this noise, focusing attribution on neurons that causally influence the generated token.
L292: Takeaway. Gradient weighting enhances ProToken’s attribution accuracy, providing an average 1.86$\times$ improvement (66.34% vs. 35.71%) across 16 configurations. While ProToken remains functional without gradients, gradient weighting is essential for reliable client(s) attributions.
L293: ### 5.4 RQ3: Computational Tractability
L294: Naively attributing contributions across all neurons and layers is infeasible (e.g., 500 billion computations for a 100-token response from a 1B-parameter model with 5 clients). ProToken addresses this by monitoring only the last $N$ transformer blocks, where task-specific knowledge concentrates cite92†Olah et al. (2018) ; cite93†Yu et al. (2022) .
L295: We measure ProToken’s overhead and attribution accuracy as we vary the number of monitored layers, from the last 3 layers up to nearly all layers, across four model architectures. Experiments use 5 test samples per global LLM at round 10.
L296: Figure 5: For each model, we vary the number of monitored layers (x-axis) and measure ProToken’s average provenance computation time (left y-axis, blue) and attribution accuracy (right y-axis).
L297: Figure cite94†5 shows that ProToken achieves 100% attribution accuracy for all models and layer counts, confirming that provenance signals are concentrated in later transformer blocks. For Gemma-3-270M-it (18 total layers), ProToken’s overhead ranges from 1.10s with 3 layers to 1.42s with last layers, representing a 29% increase. Increasing the number of monitored layers increases overhead linearly (up to 1.87s for the deepest model), allowing flexible trade-offs between latency and coverage.
L298: This validates ProToken’s efficient design: focusing on key layers enables accurate, scalable provenance tracking without redundant computation. Compared to tracking all parameters cite37†Gill et al. (2025) , ProToken’s approach reduces computation by orders of magnitude, making federated LLM provenance tracking viable in practice.
L299: Takeaway. ProToken provides accurate and efficient attribution for federated LLMs by enabling provenance tracking on only the last subset of model layers.


## jan29_three196_cost

1Introduction (https://arxiv.org/html/2601.19672v1)
citeturn28513view2 [wordlim: 200] Crawled: 2 days ago; Content type: text/html; Source: find({"ref_id":"https://arxiv.org/html/2601.19672v1","pattern":"privacy"}); Total lines: 386
L15:   1. cite5†Abstract L16:   2. cite6†1 Introduction L17:   3. cite7†2 Related Work L18:   4. cite8†3 Motivating Example L19:   5. cite9†4 ProToken Design L20:     1. cite10†Problem Statement. L21:     2. cite11†4.1 Provenance Attribution Strategy L22:       1. cite12†4.1.1 Attributing Autoregressive Sequences L23:       2. cite13†4.1.2 Layer Selection for Provenance Tractability L24:       3. cite14†4.1.3 Weighted Attribution using Token Gradients L25:       4. cite15†4.1.4 ProToken Multi-Layer Token Aggregation L26:   6. cite16†5 Evaluation L27:     1. cite17†5.1 Experimental Setup L28:     2. cite18†5.2 RQ1: Cross Domain and Architecture Accuracy L29:     3. cite19†5.3 RQ2: Relevance Filtering via Gradient Weighting L30:     4. cite20†5.4 RQ3: Computational Tractability L31:     5. cite21†5.5 RQ4: Scalability Analysis L32:   7. cite22†6 Conclusion L33:   8. cite23†References L34: cite24†License: CC BY 4.0†info.arxiv.org L35: 
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
L379: Our team has already identified cite144†the following issues†github.com . We appreciate your time reviewing and reporting rendering errors we may not have found yet. Your efforts will help us improve the HTML versions for all readers, because disability should not be a barrier to accessing research. Thank you for your continued support in championing open access for all.
L380: Have a free development cycle? Help support accessibility at arXiv! Our collaborators at LaTeXML maintain a cite145†list of packages that need conversion†github.com , and welcome cite146†developer contributions†github.com .
L381: 
L382: We gratefully acknowledge support from our major funders, cite147†member institutions†info.arxiv.org , , and all contributors.
L383: cite148†About†info.arxiv.org · cite149†Help†info.arxiv.org · cite150†Contact†info.arxiv.org · cite151†Subscribe†info.arxiv.org · cite152†Copyright†info.arxiv.org · cite153†Privacy†info.arxiv.org · cite154†Accessibility†info.arxiv.org · cite155†Operational Status (opens in new tab)†status.arxiv.org L384: 
L385: Major funding support from

