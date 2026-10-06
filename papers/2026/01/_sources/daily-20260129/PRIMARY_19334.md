# Exact-v1 primary excerpts — 19334

L labels are local to each separated original response. Preserved necessary-source tool responses; no reproduction.

## Original response: stdnext3head

When Benchmarks Leak: Inference-Time Decontamination for LLMs (https://arxiv.org/html/2601.19334v1)
citeturn28405view2 [wordlim: 200] Crawled: today; Content type: text/html; Source: open({"ref_id":"https://arxiv.org/html/2601.19334v1","lineno":null}); Total lines: 703
--------------------------------------------------------------------------------


## Original response: stdnext3core2

When Benchmarks Leak: Inference-Time Decontamination for LLMs (https://arxiv.org/html/2601.19334v1)
citeturn28406view0 [wordlim: 200] Crawled: today; Content type: text/html; Source: open({"ref_id":"turn28405view2","lineno":100}); Total lines: 703
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
L14: cite1†Why HTML?†info.arxiv.org cite2†Report Issue cite3†Back to Abstract cite4†Download PDF L15:   1. cite5†Abstract L16:   2. cite6†1 Introduction L17:     1. cite7†Contributions L18:   3. cite8†2 Related Work L19:     1. cite9†Benchmark Contamination and Detection L20:     2. cite10†Inference-time Decontamination (Black-box) L21:     3. cite11†Inference-time Decontamination (White-box) L22:   4. cite12†3 Problem Setup L23:     1. cite13†Model L24:     2. cite14†Data Contamination L25:     3. cite15†Objective L26:   5. cite16†4 Methodology L27:     1. cite17†4.1 Overview L28:     2. cite18†4.2 KL Divergence as a Surrogate Objective L29:     3. cite19†4.3 Embedding-Space Perturbation for Inference-Time Mitigation L30:     4. cite20†4.4 Generator Design L31:       1. cite21†Setup L32:       2. cite22†Generator Architecture L33:       3. cite23†Training Objective L34:   6. cite24†5 Experiment L35:     1. cite25†5.1 Experiment Setup L36:       1. cite26†Dataset L37:       2. cite27†Models L38:       3. cite28†Contamination simulation and evaluation L39:       4. cite29†Implementation Details L40:       5. cite30†Metric L41:       6. cite31†Comparison methods L42:     2. cite32†5.2 Evaluation of Decontamination Effectiveness L43:     3. cite33†5.3 Evaluation across Model scale L44:     4. cite34†5.4 Semantic preservation L45:     5. cite35†5.5 Ablation Study L46:       1. cite36†Controllability via the perturbation budget $\zeta$ L47:       2. cite37†Effect of reference model L48:   7. cite38†6 Conclusion L49:   8. cite39†7 Limitations L50:   9. cite40†References L51:   10. cite41†A Related Work L52:     1. cite42†A.1 Data Contamination L53:     2. cite43†A.2 Inference-time Decontamination L54:       1. cite44†Black-box methods L55:       2. cite45†White-box methods L56:       3. cite46†Our approach L57:   11. cite47†B Limitations of “Detect-then-Filter” L58:     1. cite48†Derivation of Eq. () L59:     2. cite49†Why strong MIA is still insufficient in practice L60:     3. cite50†Selection bias and evaluation mismatch L61:     4. cite51†Implications for benchmark contamination L62:     5. cite52†More simulation of MIA L63:   12. cite53†C Theorem L64:   13. cite54†D Generator Architecture Details L65:     1. cite55†Overview L66:     2. cite56†Unconstrained generator ${G}_{\theta}$ L67:     3. cite57†Decoder block L68:     4. cite58†Implementation choices L69:     5. cite59†Discussion L70:   14. cite60†E More Experiment L71:     1. cite61†E.1 Definition of RC and BUD L72:     2. cite62†E.2 The Full Result on Different Models under Different $o$ L73:       1. cite63†Evaluation splits (Exact / Semantic-level / Domain-level) L74:       2. cite64†How to read Tables  and  L75:       3. cite65†Table  ($o=1$): mild leakage regime L76:       4. cite66†Table  ($o=5$): strong memorization regime L77:     3. cite67†E.3 The result on Code Generation Task L78:     4. cite68†E.4 RC–BUD Pareto trade-off L79:       1. cite69†What Figure  shows L80:       2. cite70†Interpreting the axes L81:       3. cite71†Role of $\zeta$ L82:       4. cite72†Comparison to baselines L83:     5. cite73†E.5 Learned perturbations vs. random noise L84:     6. cite74†E.6 Ablation on auxiliary set size L85:   15. cite75†F AI Assistant Usage L86: cite76†License: arXiv.org perpetual non-exclusive license†info.arxiv.org L87: 
L88: arXiv:2601.19334v1 [cs.CL] 27 Jan 2026
L89: # When Benchmarks Leak: Inference-Time Decontamination for LLMs
L90: 
L91: Chai Jianzhe Affiliation: Institute of Science Tokyo Email: chai.j.4b1c@m.isct.ac.jp    Yu Zhe Affiliation: RIKEN AIP Email: zhe.yu@riken.jp    Jun Sakuma Affiliation: Institute of Science Tokyo Affiliation: RIKEN AIP Email: sakuma@c.titech.ac.jp
L92: ###### Abstract
L93: Benchmark-based evaluation is the de facto standard for comparing large language models (LLMs). However, its reliability is increasingly threatened by test set contamination, where test samples or their close variants leak into training data and artificially inflate reported performance. To address this issue, prior work has explored two main lines of mitigation.
L94: One line attempts to identify and remove contaminated benchmark items before evaluation, but this inevitably alters the evaluation set itself and becomes unreliable when contamination is moderate or severe. The other line preserves the benchmark and instead suppresses contaminated behavior at evaluation time; however, such interventions often interfere with normal inference and lead to noticeable performance degradation on clean inputs.
L95: We propose DeconIEP, a decontamination framework that operates entirely during evaluation by applying small, bounded perturbations in the input embedding space. Guided by a relatively less-contaminated reference model, DeconIEP learns an instance-adaptive perturbation generator that steers the evaluated model away from memorization-driven shortcut pathways.
L96: Across multiple open-weight LLMs and benchmarks, extensive empirical results show that DeconIEP achieves strong decontamination effectiveness while incurring only minimal degradation in benign utility.
L97: ## 1 Introduction
L98: 
L99: cite77†Image: Refer to caption Figure 1: Overview: DeconIEP keeps the prompt fixed and adds a bounded embedding perturbation $\delta=G_{\theta}(e(x))$ to suppress memorization shortcuts on leaked samples, steering inference toward reasoning and recovering clean performance.
L100: Large language models (LLMs) have reached a level of performance that enables them to solve a broad range of knowledge, reasoning, and code-related tasks (cite78†Liang et al., 2023 ). As these models are increasingly developed, released, and deployed by different organizations, a systematic way to evaluate and compare their capabilities becomes necessary. In this setting, benchmark-based evaluation has naturally emerged as a widely adopted practice for assessing LLM performance.
L101: For example, prominent models such as GPT-5 (cite79†OpenAI, 2025 ) are often presented alongside their scores on established benchmarks like MMLU (cite80†Hendrycks et al., 2021a ), where benchmark results serve as standardized evidence of general reasoning ability.
L102: Recently, the need for trustworthy evaluation is further amplified by the rapid growth of open-weight LLMs. Unlike closed APIs, open-weight models can be freely downloaded, fine-tuned, merged, and re-distributed, enabling fast iteration by both industry and the open-source community. As a result, benchmark scores are increasingly used not only for marketing, but also for model selection, deployment decisions, and reproducible scientific comparison across independently trained variants.
L103: This makes reliable evaluation of open-weight models particularly important: their training pipelines and downstream fine-tuning are more decentralized, and thus more prone to unintended benchmark exposure and evaluation artifacts.
L104: However, benchmark-centric evaluation is vulnerable to data contamination (cite81†Deng et al., 2024a ; cite82†Deng et al., 2024b ; cite83†Chen et al., 2025 ), where test items (or closely related variants) appear in training data thereby violating the train–test separation and inflating reported performance. This inflation can misrepresent real-world generalization.
L105: For example, it has been reported that over 15 LLMs exhibit inflated benchmark performance on six popular benchmarks, where the estimated contamination rate ranges from $1\%$ to $45\%$, and some of them are fine-tuned models derived from open-weight models (cite84†Li et al., 2024 ).
L106: To mitigate contamination, prior work has explored multiple strategies, including detect-then-filter approaches based on membership inference attacks (MIA) (cite85†Salem et al., 2018 ; cite86†Hayes et al., 2018 ). These methods apply an MIA detector to identify leaked benchmark items and exclude them from evaluation. However, filtering contaminated samples fundamentally alters the benchmark, making the resulting evaluation set no longer directly comparable to the original benchmark used in prior work.
L107: Moreover, MIA detectors are inherently imperfect: any non-zero false-negative rate leaves residual leaked items unfiltered, which can continue to inflate reported performance, especially under non-trivial contamination. As shown in Appendix cite47†B , we formally prove this limitation and validate it empirically.
L108: These limitations motivate inference-time decontamination (cite87†Zhu et al., 2024 ; cite88†Dong et al., 2024 ; cite89†Zhu et al., 2025 ), which mitigates contamination effects during model inference rather than by filtering benchmark items.
L109: A common issue of existing methods is that the same intervention used for decontamination applied to contaminated inputs also affects clean ones: interventions strong enough to reduce contamination often alter model behavior on uncontaminated inputs, leading to non-trivial drops in clean accuracy.
L110: For example, rewriting methods (cite87†Zhu et al., 2024 ) may shift the effective input distribution, while internal-intervention approaches (cite89†Zhu et al., 2025 ; cite90†Menta et al., 2025 ) can suppress internal signals that are useful for both contaminated and clean examples. As a result, existing methods face an unfavorable trade-off between contamination mitigation and clean performance, motivating our goal of minimizing benign utility degradation.
L111: To address this limitation, we propose a decontamination framework, termed DeconIEP (Decon tamination via I nference-time E mbedding P erturbation). We observe that data contamination mainly manifests as a change in how a model internally supports its predictions. On clean test samples, predictions are typically supported by broadly shared reasoning features that generalize across many inputs.
L112: In contrast, as shown in the first row of Figure cite91†1 , on contaminated test samples, the same outputs can be produced by relying on a different set of contamination-specific components, such as shortcut neurons or late-layer retrieval pathways, thereby reducing the need for genuine reasoning (cite89†Zhu et al., 2025 ; cite90†Menta et al., 2025 ).
L113: This observation motivates our approach: as shown in the second row of Figure cite91†1 , by applying small, targeted perturbations in the embedding space, we weaken contamination-driven dependencies and steer the model toward a cleaner inference regime, while preserving the input representation.
L114: Based on this insight, we train a generator to produce inference-time embedding perturbations, guided by a comparatively less contaminated reference model. Our setting targets models obtained via fine-tuning from a known pretrained checkpoint (e.g., Llama3), where benchmark contamination is typically introduced or amplified by fine-tuning the checkpoint.
L115: In this context, an earlier checkpoint or base model with the same architecture naturally provides a practical reference with reduced benchmark-specific exposure. Importantly, our empirical evaluation demonstrates that our approach does not require a perfectly clean reference model.
L116: It suffices that the reference exhibits relatively less contamination, allowing the generator to suppress contamination-driven shortcuts while preserving benign reasoning behavior, without modifying the parameters of the evaluated model.
L117: #### Contributions
L118: Our contributions are two-fold: (1) We propose DeconIEP, a novel inference-time decontamination method that mitigates benchmark contamination by applying small, targeted perturbations to input embeddings, without modifying model parameters or the benchmark itself.
L119: (2) We conduct extensive experiments across multiple benchmarks and contamination settings, showing that DeconIEP effectively reduces contamination-induced performance inflation while incurring substantially smaller degradation on clean inputs compared to existing inference-time baselines.
L120: Method  | Setting  | Core Mechanism  | Need Reference Model  | Decontam. Efficacy $\uparrow$  | Clean Eval Drop $\downarrow$
L121: TED (cite88†Dong et al., 2024 )  | Black-box  | Distribution calibration  | No  | Medium  | Medium
L122: ITD (cite87†Zhu et al., 2024 )  | Black-box  | Query rewriting  | No  | Limited  | Low
L123: Shortcut Neuron (cite89†Zhu et al., 2025 )  | White-box  | Activation patching  | Yes  | High  | High
L124: Short-circuiting (cite90†Menta et al., 2025 )  | White-box  | Attention bypassing  | No  | High  | High
L125: DeconIEP(Ours)  | White-box  | Embedding perturbation  | Yes  | High  | Low
L126: Table 1: Comparison of decontamination strategies. Decontam. Efficacy indicates decontamination effectiveness on contaminated benchmarks. Clean Eval Drop indicates performance degradation on non-contaminated tasks. Need Reference Model indicates whether a reference model is required.
L127: ## 2 Related Work
L128: #### Benchmark Contamination and Detection
L129: Data contamination (test-set leakage) in widely used benchmarks (e.g., MMLU, GSM8K) can inflate reported performance by inducing memorization rather than genuine generalization (cite83†Chen et al., 2025 ; cite82†Deng et al., 2024b ; cite92†Xu et al., 2024 ). When training data are accessible, overlap-based checks can reveal contamination (cite93†Brown et al., 2020 ; cite94†Gao et al., 2021 ), but for most open-source models such verification is infeasible.
L130: An alternative line of work adopts detect-then-filter strategies based on membership inference attacks (MIAs), but imperfect detectors leave residual contamination and may introduce selection bias (see Appendix cite47†B ).
L131: #### Inference-time Decontamination (Black-box)
L132: 
L133: To avoid training-data access, API-only methods intervene at inference time: TED (cite88†Dong et al., 2024 ) calibrates outputs via repeated sampling, and ITD (cite87†Zhu et al., 2024 ) rewrites prompts using auxiliary LLMs. These approaches are easy to deploy but can be computationally expensive, and prompt rewriting may alter semantics or task difficulty (cite92†Xu et al., 2024 ).
L134: #### Inference-time Decontamination (White-box)
L135: With open-weight access, prior work manipulates internal representations, Short-cut Neuron Analysis (cite89†Zhu et al., 2025 ) uses a reference model to identify such shortcut neurons and then edits their activations at test time. As shown in Table cite95†1 , it can achieve high decontamination efficacy, but often leads to a large clean-evaluation drop when the edited neurons overlap with general-purpose computation.
L136: Menta et al. (cite90†Menta et al., 2025 ) propose attention short-circuiting, which replaces the attention mixing operation with an identity mapping so that value vectors are forwarded without cross-token aggregation. They report that bypassing attention in deeper layers can substantially reduce the generation of memorized content. While this mechanism is not proposed as a decontamination method, it can be repurposed to suppress contamination-driven memorization.
L137: However, as summarized in Table cite95†1 , the same intervention also degrades general capabilities, leading to a large benign utility drop.
L138: ## 3 Problem Setup
L139: 
L140: #### Model
L141: 
L142: Let $f:\mathcal{X}\rightarrow\mathcal{Y}$ be a Large Language Model (LLM), where $\mathcal{X}$ is the space of input sequences and $\mathcal{Y}$ is the space of output sequences.
L143: #### Data Contamination
L144: 
L145: We want to train a model $f$ and we have a test benchmark $D_{\text{test}}\sim\mathcal{P}_{\text{test}}$ to evaluate its performance. We define the contaminated model $f_{\mathrm{con}}$ as any model trained on a dataset
L146: 
L147:  | $$D_{\mathrm{train}}^{\mathrm{con}}\;=\;D_{\mathrm{train}}^{\mathrm{clean}}\,\cup D_{\mathrm{con}},$$  |
L148: where $D_{\mathrm{train}}^{\mathrm{clean}}$ is general training data and unrelated to $D_{\text{test}}$, and $D_{\mathrm{con}}$ potentially causes training data contamination, where we consider the following three levels of contamination as follows.
L149: 
L150:   1. 1.
L151: 
L152: Exact Contamination: $D_{\mathrm{con}}\subseteq D_{\text{test}}$, i.e., the training data contains exact copies of test examples.
L153: 
L154:   2. 2.
L155: Semantic-level Contamination: For each $x\in D_{\mathrm{test}}$, there exists $x^{\prime}\in D_{\mathrm{con}}$ such that, $\mathrm{sem}(x)=\mathrm{sem}(x^{\prime})$. Here, $\mathrm{sem}(\cdot)$ refers to paraphrasing or semantically equivalent rewriting by LLM or human.
L156: 
L157:   3. 3.
L158: Domain-level Contamination: $D_{\mathrm{con}}\sim\mathcal{P}_{\text{test}}$, i.e., the contamination set and the test set are drawn from (approximately) the same underlying distribution, such as $D_{\text{con}}$ and $D_{\text{test}}$ are two random splits of the same benchmark.
L159: For a fixed test benchmark $D_{\mathrm{test}}$, we call a model $f_{\mathrm{clean}}$ trained on $D_{\mathrm{train}}^{\mathrm{clean}}$ clean if its training data does not contaminate $D_{\mathrm{test}}$ at any of three contamination level defined above.
L160: 
L161: Due to contamination, the observed performance of $f_{\text{con}}$ on $D_{\text{test}}$ is often inflated:
L162: 
L163:  | $$\text{Perf}(f_{\text{con}},D_{\text{test}})>\text{Perf}(f_{\text{clean}},D_{\text{test}})$$  |  | (1)
L164: Here, $\text{Perf}(\cdot)$ is a general performance evaluator, for example, classification accuracy for multiple-choice benchmarks (e.g., MMLU).
L165: #### Objective
L166: 
L167: We design an inference-time mitigation operator
L168: 
L169:  | $$M:\ \mathcal{F}\rightarrow\mathcal{F}$$  |
L170: 
L171: which maps a contaminated model $f_{\mathrm{con}}$ to a mitigated predictor $M(f_{\mathrm{con}})$ with a modified inference procedure. Our objective is to make its test performance match that of an ideal clean model:
L172: 
L173:  | $$\mathrm{Perf}\bigl(M(f_{\mathrm{con}}),D_{\mathrm{test}}\bigr)\ \approx\ \mathrm{Perf}\bigl(f_{\mathrm{clean}},D_{\mathrm{test}}\bigr),$$  |  | (2)
L174: 
L175: ## 4 Methodology
L176: ### 4.1 Overview
L177: 
L178: We reduce contamination-induced inflation by correcting inference rather than filtering items. Given $f_{\mathrm{con}}$ and input $x$, we keep the prompt unchanged and add a bounded embedding perturbation $\delta(x)$ with $\|\delta(x)\|_{\infty}\leq\zeta$. We train a generator $G_{\theta}$ via a KL objective (Theorem cite96†1 ) to align $f_{\mathrm{con}}$ with a reference model $f_{\mathrm{ref}}$. At test time, we apply $\delta(x)$ once per input and evaluate on the original benchmark.
L179: ### 4.2 KL Divergence as a Surrogate Objective
L180: 
L181: Our goal is to align the behavior of the mitigated contaminated model $M(f_{\mathrm{con}})$ with the ideal clean model $f_{\mathrm{clean}}$ on the test benchmark $D_{\mathrm{test}}$. We write the performance gap $\Delta_{\mathrm{perf}}$ as:
L182: 
L183:  | $$\begin{split}\Delta_{\mathrm{perf}}\;:=\;\bigl|&\mathrm{Perf}(M(f_{\mathrm{con}}),D_{\mathrm{test}})-\mathrm{Perf}(f_{\mathrm{clean}},D_{\mathrm{test}})\bigr|.\end{split}$$  |
L184: Directly minimizing $\Delta_{\mathrm{perf}}$ is intractable because standard metrics (e.g., multiple-choice accuracy) are discrete and non-differentiable. We therefore adopt a differentiable, distribution-level surrogate. For each $x\in D_{\mathrm{test}}$, let $p_{\mathrm{con}}(\cdot\mid x)$ and $p_{\mathrm{clean}}(\cdot\mid x)$ denote the output distributions of $M(f_{\mathrm{con}})$ and $f_{\mathrm{clean}}$, respectively.
L185: By viewing performance as $\mathbb{E}{y\sim p(\cdot\mid x)}[u(x,y)]$ for a bounded utility $u(x,y)\in[0,1]$, the performance gap can be related to a distance between $p_{\mathrm{con}}$ and $p_{\mathrm{clean}}$, requiring only boundedness and thus covering a range of evaluation metrics.
L186: Theorem in Appendix  cite53†C shows that the average KL divergence between the mitigated contaminated model and the clean model upper-bounds the performance gap. We therefore use KL minimization as a principled surrogate objective. This bound is only used as motivation and does not guarantee our algorithm’s behavior. Next, we instantiate $M$ so that the KL objective can be optimized efficiently.
L187: ### 4.3 Embedding-Space Perturbation for Inference-Time Mitigation
L188: 
L189: We implement the mitigation mechanism $M$ by applying small, controlled perturbations in the embedding space, while keeping the discrete input text unchanged. This design preserves semantic and difficulty invariance of benchmark items, which input-space transformations such as paraphrasing or rewriting may violate.
L190: Formally, let $e(x)\in\mathbb{R}^{L\times d}$ denote the input embedding sequence for a benchmark question $x$. We define the mitigated prediction as
L191: 
L192:  | $$M(f)(x)=f(e(x)+\delta(x)),\quad\|\delta(x)\|_{\infty}\leq\zeta,$$  |  | (3)
L193: where $\delta(x)$ is a bounded perturbation with a small budget $\zeta$. Constraining $\delta(x)$ in an $\ell_{\infty}$-ball encourage that the perturbed embedding remains in a local neighborhood of $e(x)$, aiming to preserve the underlying semantics and difficulty while disrupting memorized surface patterns.
L194: 
L195: This reasoning leads to the ideal per-sample objective of aligning the perturbed contaminated model with clean behavior:
L196:  | $\displaystyle\min_{\{\delta(x)\}_{x\in D}}$  | $\displaystyle\frac{1}{|D|}\sum_{x\in D}\mathrm{KL}\big(f_{\mathrm{con}}(e(x)+\delta(x))\,\big\|\,f_{\mathrm{clean}}(e(x))\big)$  |  | (4)
L197:  |  | $\displaystyle\text{s.t.}\quad\|\delta(x)\|_{\infty}\leq\zeta,\;\forall x.$  |
L198: Directly optimizing a separate perturbation for each input is computationally infeasible at evaluation time. We therefore amortize the optimization by learning a generator $G_{\theta}$. After training, we can use such a generator to generate $\delta(x)$ for all $x\in D_{\mathrm{test}}$ (and other unseen inputs). Our amortized objective becomes:
L199:  | $$\begin{split}\min_{\theta}\;\;&\frac{1}{|D|}\sum_{x\in D}\mathrm{KL}\Big(f_{\mathrm{con}}\big(e(x)+G_{\theta}(e(x))\big)\,\big\|\,f_{\mathrm{clean}}\big(e(x)\big)\Big)\\
L200: &\text{s.t.}\;\;\big\|G_{\theta}(e(x))\big\|_{\infty}\leq\zeta,\quad\forall x\in D.\end{split}$$  |  | (5)
L201: 
L202: where $D$ is an auxiliary dataset used to train $G_{\theta}$ sampled from evaluated benchmark.
L203: ### 4.4 Generator Design
L204: #### Setup
L205: We assume access to a contaminated model $f_{\mathrm{con}}$, a reference model $f_{\mathrm{ref}}$, and a small auxiliary dataset $D_{\mathrm{aux}}$ sampled from the benchmark. The reference model serves as a practical proxy for clean behavior during generator training.
L206: Since a strictly clean model $f_{\mathrm{clean}}$ is often unavailable, $f_{\mathrm{ref}}$ is typically chosen as the same-architecture base model (or an earlier checkpoint) from which $f_{\mathrm{con}}$ is fine-tuned, and is expected to have less benchmark-specific exposure. This choice is standard in contamination-related analyses (cite89†Zhu et al., 2025 ; cite97†Carlini et al., 2021 ; cite98†Carlini et al., 2022 ).
L207: #### Generator Architecture
L208: 
L209: We parameterize the perturbation generator as a lightweight sequence-to-sequence network. Let ${G}_{\theta}$ denote an generator that maps the input embedding $e(x)\in\mathbb{R}^{L\times d}$ to a raw perturbation. To enforce the perturbation budget, we apply a scaled $\tanh$ transformation:
L210: 
L211:  | $$\delta(x)=\zeta\cdot\tanh(G_{\theta}(x)),$$  |
L212: which guarantees $\|\delta(x)\|_{\infty}\leq\zeta$ by construction. The perturbed embedding $e(x)+\delta(x)$ is then fed to $f_{\mathrm{con}}$ at inference time. Unless otherwise specified, ${G}_{\theta}$ is instantiated as a small decoder-only Transformer (cite99†Vaswani et al., 2017 ); architectural details are provided in Appendix cite54†D .
L213: #### Training Objective
L214: 
L215: For a training sample $x\sim D_{\mathrm{aux}}$, let $p^{\mathrm{con}}=f_{\mathrm{con}}(e(x)+\delta(x))$ and $p^{\mathrm{ref}}=f_{\mathrm{ref}}(e(x))$ denote the output distributions of the contaminated and reference models, respectively. We train the generator using a composite KL+CE objective:
L216:  | $$\begin{split}\mathcal{L}(\theta)=\mathbb{E}_{x\sim D_{\mathrm{aux}}}\Big[&\lambda_{\mathrm{KL}}\cdot\mathrm{KL}\big(p^{\mathrm{con}}\,\|\,p^{\mathrm{ref}}\big)\\
L217: +\;&\lambda_{\mathrm{CE}}\cdot\mathrm{CE}\big(p^{\mathrm{con}},y_{\mathrm{ref}}\big)\Big],\end{split}$$  |  | (6)
L218: where $y_{\mathrm{ref}}$ denotes hard token labels sampled from $f_{\mathrm{ref}}$, and $\lambda_{\mathrm{KL}},\lambda_{\mathrm{CE}}$ control the relative weights of the two terms. The KL term directly optimizes the surrogate objective motivated by Theorem cite96†1 , while the cross-entropy term stabilizes training and prevents degenerate solutions. In the appendix, Algorithm cite100†1 summarizes the training procedure.
L219: ## 5 Experiment
L220: 
L221: ### 5.1 Experiment Setup
L222: #### Dataset
L223: We evaluate on two benchmarks: MMLU (cite101†Hendrycks et al., 2021b ) and TruthfulQA (cite102†Lin et al., 2022 ). MMLU is a large-scale multiple-choice benchmark spanning diverse academic and professional domains, while TruthfulQA measures truthfulness and resistance to common misconceptions. In our experiments, these benchmarks serve dual roles. First, they define the evaluation benchmarks.
L224: Second, to simulate benchmark contamination, a small subset of benchmark items is intentionally allowed to leak into the training data when constructing contaminated models. All benchmark items used for contamination are drawn exclusively from the corresponding benchmark (MMLU or TruthfulQA). We also test the proposal on the code generation task, and shown in the Appendix cite67†E.3 .
L225: #### Models
L226: We conduct experiments on three instruction-tuned large language models : LLaMA-3-8B-Instruct cite103†Grattafiori et al. (2024) , Qwen Family cite104†Yang et al. (2025) , and Mistral-7B-Instruct-v0.3 cite105†Jiang et al. (2023) . These models represent different model families, allowing us to evaluate the generality of our decontamination method across heterogeneous architectures. Before simulating contamination, we start from the corresponding pretrained (unfine-tuned) model for each architecture.
L227: This pretrained model serves as the common initialization for all experiments and is also used as the reference model in our decontamination framework. Fine-tuning is then performed either with or without benchmark leakage, depending on the contamination setting. These model families span heterogeneous architectures, allowing us to evaluate the generality of our decontamination method.
L228: Model  | Split  | Method  | Access  | TruthfulQA ($o=3$)  | MMLU ($o=3$)
L229: Exact  | Semantic-level  | Domain-level  | Exact  | Semantic-level  | Domain-level
L230: Mistral  | $f_{\mathrm{clean}}$  | baseline  | –  | 0.287  | 0.249  | 0.269  | 0.451  | 0.434  | 0.406
L231: $f_{\mathrm{con}}$  | W/O Decontamination  | –  | 0.976 (0.689)  | 0.971 (0.722)  | 0.861 (0.592)  | 0.892 (0.441)  | 0.875 (0.441)  | 0.475 (0.069)
L232: TED  | Black-box  | 0.535 (0.248)  | 0.579 (0.330)  | 0.740 (0.471)  | 0.224 (0.227)  | 0.388 (0.046)  | 0.375 (0.031)
L233: ITD  | Black-box  | 0.976 (0.689)  | 0.971 (0.722)  | 0.861 (0.592)  | 0.886 (0.435)  | 0.863 (0.429)  | 0.471 (0.065)
L234: Shortcut Neuron  | White-box  | 0.668 (0.381)  | 0.634 (0.385)  | 0.636 (0.367)  | 0.380 (0.071)  | 0.386 (0.048)  | 0.239 (0.167)
L235: Short Circuit  | White-box  | 0.933 (0.646)  | 0.914 (0.665)  | 0.793 (0.524)  | 0.833 (0.382)  | 0.808 (0.374)  | 0.478 (0.072)
L236: DeconIEP(Ours)  | White-box  | 0.533 (0.246)  | 0.551 (0.302)  | 0.565 (0.296)  | 0.458 (0.007)  | 0.406 (0.028)  | 0.417 (0.011)
L237: Qwen2.5  | $f_{\mathrm{clean}}$  | baseline  | –  | 0.555  | 0.531  | 0.572  | 0.670  | 0.671  | 0.673
L238: $f_{\mathrm{con}}$  | W/O Decontamination  | –  | 0.976 (0.421)  | 0.952 (0.421)  | 0.885 (0.313)  | 0.905 (0.235)  | 0.872 (0.201)  | 0.744 (0.071)
L239: TED  | Black-box  | 0.880 (0.325)  | 0.900 (0.369)  | 0.846 (0.274)  | 0.837 (0.167)  | 0.882 (0.211)  | 0.713 (0.040)


## Original response: stdnext3eval1

When Benchmarks Leak: Inference-Time Decontamination for LLMs (https://arxiv.org/html/2601.19334v1)
citeturn28411view0 [wordlim: 200] Crawled: today; Content type: text/html; Source: open({"ref_id":"turn28405view2","lineno":240}); Total lines: 703
L186: Theorem in Appendix  cite53†C shows that the average KL divergence between the mitigated contaminated model and the clean model upper-bounds the performance gap. We therefore use KL minimization as a principled surrogate objective. This bound is only used as motivation and does not guarantee our algorithm’s behavior. Next, we instantiate $M$ so that the KL objective can be optimized efficiently.
L187: ### 4.3 Embedding-Space Perturbation for Inference-Time Mitigation
L188: 
L189: We implement the mitigation mechanism $M$ by applying small, controlled perturbations in the embedding space, while keeping the discrete input text unchanged. This design preserves semantic and difficulty invariance of benchmark items, which input-space transformations such as paraphrasing or rewriting may violate.
L190: Formally, let $e(x)\in\mathbb{R}^{L\times d}$ denote the input embedding sequence for a benchmark question $x$. We define the mitigated prediction as
L191: 
L192:  | $$M(f)(x)=f(e(x)+\delta(x)),\quad\|\delta(x)\|_{\infty}\leq\zeta,$$  |  | (3)
L193: where $\delta(x)$ is a bounded perturbation with a small budget $\zeta$. Constraining $\delta(x)$ in an $\ell_{\infty}$-ball encourage that the perturbed embedding remains in a local neighborhood of $e(x)$, aiming to preserve the underlying semantics and difficulty while disrupting memorized surface patterns.
L194: 
L195: This reasoning leads to the ideal per-sample objective of aligning the perturbed contaminated model with clean behavior:
L196:  | $\displaystyle\min_{\{\delta(x)\}_{x\in D}}$  | $\displaystyle\frac{1}{|D|}\sum_{x\in D}\mathrm{KL}\big(f_{\mathrm{con}}(e(x)+\delta(x))\,\big\|\,f_{\mathrm{clean}}(e(x))\big)$  |  | (4)
L197:  |  | $\displaystyle\text{s.t.}\quad\|\delta(x)\|_{\infty}\leq\zeta,\;\forall x.$  |
L198: Directly optimizing a separate perturbation for each input is computationally infeasible at evaluation time. We therefore amortize the optimization by learning a generator $G_{\theta}$. After training, we can use such a generator to generate $\delta(x)$ for all $x\in D_{\mathrm{test}}$ (and other unseen inputs). Our amortized objective becomes:
L199:  | $$\begin{split}\min_{\theta}\;\;&\frac{1}{|D|}\sum_{x\in D}\mathrm{KL}\Big(f_{\mathrm{con}}\big(e(x)+G_{\theta}(e(x))\big)\,\big\|\,f_{\mathrm{clean}}\big(e(x)\big)\Big)\\
L200: &\text{s.t.}\;\;\big\|G_{\theta}(e(x))\big\|_{\infty}\leq\zeta,\quad\forall x\in D.\end{split}$$  |  | (5)
L201: 
L202: where $D$ is an auxiliary dataset used to train $G_{\theta}$ sampled from evaluated benchmark.
L203: ### 4.4 Generator Design
L204: #### Setup
L205: We assume access to a contaminated model $f_{\mathrm{con}}$, a reference model $f_{\mathrm{ref}}$, and a small auxiliary dataset $D_{\mathrm{aux}}$ sampled from the benchmark. The reference model serves as a practical proxy for clean behavior during generator training.
L206: Since a strictly clean model $f_{\mathrm{clean}}$ is often unavailable, $f_{\mathrm{ref}}$ is typically chosen as the same-architecture base model (or an earlier checkpoint) from which $f_{\mathrm{con}}$ is fine-tuned, and is expected to have less benchmark-specific exposure. This choice is standard in contamination-related analyses (cite89†Zhu et al., 2025 ; cite97†Carlini et al., 2021 ; cite98†Carlini et al., 2022 ).
L207: #### Generator Architecture
L208: 
L209: We parameterize the perturbation generator as a lightweight sequence-to-sequence network. Let ${G}_{\theta}$ denote an generator that maps the input embedding $e(x)\in\mathbb{R}^{L\times d}$ to a raw perturbation. To enforce the perturbation budget, we apply a scaled $\tanh$ transformation:
L210: 
L211:  | $$\delta(x)=\zeta\cdot\tanh(G_{\theta}(x)),$$  |
L212: which guarantees $\|\delta(x)\|_{\infty}\leq\zeta$ by construction. The perturbed embedding $e(x)+\delta(x)$ is then fed to $f_{\mathrm{con}}$ at inference time. Unless otherwise specified, ${G}_{\theta}$ is instantiated as a small decoder-only Transformer (cite99†Vaswani et al., 2017 ); architectural details are provided in Appendix cite54†D .
L213: #### Training Objective
L214: 
L215: For a training sample $x\sim D_{\mathrm{aux}}$, let $p^{\mathrm{con}}=f_{\mathrm{con}}(e(x)+\delta(x))$ and $p^{\mathrm{ref}}=f_{\mathrm{ref}}(e(x))$ denote the output distributions of the contaminated and reference models, respectively. We train the generator using a composite KL+CE objective:
L216:  | $$\begin{split}\mathcal{L}(\theta)=\mathbb{E}_{x\sim D_{\mathrm{aux}}}\Big[&\lambda_{\mathrm{KL}}\cdot\mathrm{KL}\big(p^{\mathrm{con}}\,\|\,p^{\mathrm{ref}}\big)\\
L217: +\;&\lambda_{\mathrm{CE}}\cdot\mathrm{CE}\big(p^{\mathrm{con}},y_{\mathrm{ref}}\big)\Big],\end{split}$$  |  | (6)
L218: where $y_{\mathrm{ref}}$ denotes hard token labels sampled from $f_{\mathrm{ref}}$, and $\lambda_{\mathrm{KL}},\lambda_{\mathrm{CE}}$ control the relative weights of the two terms. The KL term directly optimizes the surrogate objective motivated by Theorem cite96†1 , while the cross-entropy term stabilizes training and prevents degenerate solutions. In the appendix, Algorithm cite100†1 summarizes the training procedure.
L219: ## 5 Experiment
L220: 
L221: ### 5.1 Experiment Setup
L222: #### Dataset
L223: We evaluate on two benchmarks: MMLU (cite101†Hendrycks et al., 2021b ) and TruthfulQA (cite102†Lin et al., 2022 ). MMLU is a large-scale multiple-choice benchmark spanning diverse academic and professional domains, while TruthfulQA measures truthfulness and resistance to common misconceptions. In our experiments, these benchmarks serve dual roles. First, they define the evaluation benchmarks.
L224: Second, to simulate benchmark contamination, a small subset of benchmark items is intentionally allowed to leak into the training data when constructing contaminated models. All benchmark items used for contamination are drawn exclusively from the corresponding benchmark (MMLU or TruthfulQA). We also test the proposal on the code generation task, and shown in the Appendix cite67†E.3 .
L225: #### Models
L226: We conduct experiments on three instruction-tuned large language models : LLaMA-3-8B-Instruct cite103†Grattafiori et al. (2024) , Qwen Family cite104†Yang et al. (2025) , and Mistral-7B-Instruct-v0.3 cite105†Jiang et al. (2023) . These models represent different model families, allowing us to evaluate the generality of our decontamination method across heterogeneous architectures. Before simulating contamination, we start from the corresponding pretrained (unfine-tuned) model for each architecture.
L227: This pretrained model serves as the common initialization for all experiments and is also used as the reference model in our decontamination framework. Fine-tuning is then performed either with or without benchmark leakage, depending on the contamination setting. These model families span heterogeneous architectures, allowing us to evaluate the generality of our decontamination method.
L228: Model  | Split  | Method  | Access  | TruthfulQA ($o=3$)  | MMLU ($o=3$)
L229: Exact  | Semantic-level  | Domain-level  | Exact  | Semantic-level  | Domain-level
L230: Mistral  | $f_{\mathrm{clean}}$  | baseline  | –  | 0.287  | 0.249  | 0.269  | 0.451  | 0.434  | 0.406
L231: $f_{\mathrm{con}}$  | W/O Decontamination  | –  | 0.976 (0.689)  | 0.971 (0.722)  | 0.861 (0.592)  | 0.892 (0.441)  | 0.875 (0.441)  | 0.475 (0.069)
L232: TED  | Black-box  | 0.535 (0.248)  | 0.579 (0.330)  | 0.740 (0.471)  | 0.224 (0.227)  | 0.388 (0.046)  | 0.375 (0.031)
L233: ITD  | Black-box  | 0.976 (0.689)  | 0.971 (0.722)  | 0.861 (0.592)  | 0.886 (0.435)  | 0.863 (0.429)  | 0.471 (0.065)
L234: Shortcut Neuron  | White-box  | 0.668 (0.381)  | 0.634 (0.385)  | 0.636 (0.367)  | 0.380 (0.071)  | 0.386 (0.048)  | 0.239 (0.167)
L235: Short Circuit  | White-box  | 0.933 (0.646)  | 0.914 (0.665)  | 0.793 (0.524)  | 0.833 (0.382)  | 0.808 (0.374)  | 0.478 (0.072)
L236: DeconIEP(Ours)  | White-box  | 0.533 (0.246)  | 0.551 (0.302)  | 0.565 (0.296)  | 0.458 (0.007)  | 0.406 (0.028)  | 0.417 (0.011)
L237: Qwen2.5  | $f_{\mathrm{clean}}$  | baseline  | –  | 0.555  | 0.531  | 0.572  | 0.670  | 0.671  | 0.673
L238: $f_{\mathrm{con}}$  | W/O Decontamination  | –  | 0.976 (0.421)  | 0.952 (0.421)  | 0.885 (0.313)  | 0.905 (0.235)  | 0.872 (0.201)  | 0.744 (0.071)
L239: TED  | Black-box  | 0.880 (0.325)  | 0.900 (0.369)  | 0.846 (0.274)  | 0.837 (0.167)  | 0.882 (0.211)  | 0.713 (0.040)
L240: ITD  | Black-box  | 0.976 (0.421)  | 0.947 (0.416)  | 0.899 (0.327)  | 0.898 (0.228)  | 0.868 (0.197)  | 0.751 (0.078)
L241: Shortcut Neuron  | White-box  | 0.684 (0.129)  | 0.526 (0.005)  | 0.394 (0.178)  | 0.416 (0.254)  | 0.420 (0.251)  | 0.371 (0.302)
L242: Short Circuit  | White-box  | 0.650 (0.095)  | 0.622 (0.091)  | 0.614 (0.042)  | 0.807 (0.137)  | 0.757 (0.086)  | 0.640 (0.033)
L243: DeconIEP(Ours)  | White-box  | 0.620 (0.065)  | 0.632 (0.101)  | 0.641 (0.069)  | 0.785 (0.115)  | 0.632 (0.039)  | 0.646 (0.027)
L244: LLaMA-3  | $f_{\mathrm{clean}}$  | baseline  | –  | 0.474  | 0.467  | 0.452  | 0.576  | 0.565  | 0.549
L245: $f_{\mathrm{con}}$  | W/O Decontamination  | –  | 0.986 (0.512)  | 0.981 (0.514)  | 0.928 (0.476)  | 0.921 (0.345)  | 0.901 (0.336)  | 0.669 (0.120)
L246: TED  | Black-box  | 0.966 (0.493)  | 0.951 (0.485)  | 0.923 (0.471)  | 0.864 (0.288)  | 0.842 (0.277)  | 0.638 (0.089)
L247: ITD  | Black-box  | 0.943 (0.469)  | 0.957 (0.490)  | 0.899 (0.447)  | 0.886 (0.310)  | 0.844 (0.279)  | 0.648 (0.098)
L248: Shortcut Neuron  | White-box  | 0.818 (0.345)  | 0.852 (0.385)  | 0.726 (0.274)  | 0.690 (0.114)  | 0.682 (0.117)  | 0.482 (0.068)
L249: Short Circuit  | White-box  | 0.593 (0.120)  | 0.608 (0.141)  | 0.625 (0.173)  | 0.701 (0.125)  | 0.680 (0.115)  | 0.707 (0.157)
L250: DeconIEP(Ours)  | White-box  | 0.536 (0.062)  | 0.519 (0.053)  | 0.553 (0.101)  | 0.741 (0.165)  | 0.537 (0.028)  | 0.536 (0.014)
L251: Table 2: Decontamination results for $o=3$ across different models. Values denote accuracy, with parentheses showing RC (smaller is better). Best RC is in bold and second best is underlined within each model and split. ($\zeta=10^{-3}$)
L252: cite106†Image: Refer to caption (a) TruthfulQA.
L253: 
L254: cite107†Image: Refer to caption (b) MMLU.
L255: 
L256: Figure 2: Average Residual Contamination (RC) of all models across leakage occurrences $o$ under different contamination levels (lower is better).( $\zeta=10^{-3}$)
L257: #### Contamination simulation and evaluation
L258: Following common practice in prior work (cite89†Zhu et al., 2025 ), we simulate benchmark contamination in a controlled manner. For each benchmark, we construct a contaminated model $f_{\mathrm{con}}$ by fine-tuning the pretrained model on a mixture of: (i) a general instruction-tuning dataset OpenOrca, denoted as $D_{\mathrm{train}}^{\mathrm{clean}}$, and (ii) a small set of leaked benchmark items $D_{\mathrm{con}}$, drawn from either MMLU or TruthfulQA.
L259: Each benchmark item in $D_{\mathrm{con}}$ is repeatedly included in training $o\in\{1,3,5\}$ times to simulate different contamination strengths. To isolate the effect of benchmark leakage, we also train a clean counterpart $f_{\mathrm{clean}}$ by fine-tuning on OpenOrca only, using the same total number of training samples as $f_{\mathrm{con}}$, but without including any benchmark items.
L260: We evaluate decontamination performance under three contamination settings, each associated with a different construction of the test set $D_{\mathrm{test}}$: (i) Exact contamination: $D_{\mathrm{test}}$ consists of a subset of the leaked benchmark items from $D_{\mathrm{con}}$, evaluating direct memorization effects; (ii) Semantic-level contamination: $D_{\mathrm{test}}$ consists of paraphrases of the leaked benchmark items, which are semantically equivalent but not observed during training, with ground-truth answers unchanged; and (iii) Domain-level contamination: $D_{\mathrm{test}}$ is sampled from the same benchmark distribution but is strictly disjoint from $D_{\mathrm{con}}$, evaluating same-domain generalization rather than direct leakage.
L261: For benign (clean) utility evaluation, we additionally evaluate on an external benchmark that is not used to construct $D_{\mathrm{con}}$. Specifically, when contamination is simulated on MMLU, TruthfulQA is used as the clean test benchmark, and vice versa.
L262: #### Implementation Details
L263: The noise generator $G_{\theta}$ is a 4-layer decoder-only Transformer ($n=4$). The generator is trained on the same benchmark used to construct the contamination set (e.g., MMLU for MMLU-contaminated models), using benchmark samples that are disjoint from the test set in each evaluation setting.
L264: We set the perturbation budget $\zeta=10^{-3}$, learning rate $lr=1\times 10^{-5}$, dropout rate to 0.2, and use an auxiliary dataset of size $|D_{\mathrm{aux}}|=400$, which is sampled from contaminated benchmark and disjoint from $D_{\mathrm{test}}$. Additional details shown in Appendix cite60†E .
L265: #### Metric
L266: 
L267: We evaluate decontamination using two metrics: Residual Contamination (RC) and Benign Utility Drop (BUD). RC measures how close the decontaminated model $M(f_{\mathrm{con}})$ is to the uncontaminated model $f_{\mathrm{clean}}$ on contaminated data, while BUD measures utility loss on clean data.
L268: 
L269: Smaller values indicate better decontamination. Formal definition see Appendixcite61†E.1 .
L270: #### Comparison methods
L271: 
L272: We compare our method with representative inference-time decontamination baselines explained in Section cite8†2 : TED and ITD as black-box methods, Shortcut Neuron and Short Circuit as white-box methods.
L273: 
L274: cite108†Image: Refer to caption (a) TruthfulQA ($o=3$).
L275: 
L276: cite109†Image: Refer to caption (b) MMLU ($o=3$).
L277: Figure 3: Scaling behavior on Qwen2.5-Instruct models ($o=3$). We compare RC on exact domian and BUD across model sizes (1.5B/3B/7B/14B) on (a) TruthfulQA and (b) MMLU. Our method remains effective and stable under scaling with a fixed embedding perturbation budget $\zeta=10^{-3}$.
L278: ### 5.2 Evaluation of Decontamination Effectiveness
L279: We first evaluate decontamination by whether the performance of the post-mitigation model approaches that of the uncontaminated model $f_{\mathrm{clean}}$. Table  cite110†2 reports accuracy and Residual Contamination (RC; lower is better) on TruthfulQA and MMLU under $o=3$, $o=1$ and $o=5$ see Appendix cite62†E.2 . Overall, DeconIEP achieves the lowest or near-lowest RC across models, benchmarks, and contamination granularities, and remains robust under three-level contamination.
L280: While some baselines are best in isolated cases, their improvements are not consistent.
L281: Figure cite111†2 further varies the occurrence level $o$. Although larger $o$ increases residuals for the unmitigated model, DeconIEP consistently reduces RC and keeps accuracy closer to $f_{\mathrm{clean}}$. To assess whether decontamination introduces unintended degradation on clean tasks, we evaluate benign utility using a cross-benchmark clean evaluation.
L282: Specifically, to isolate benign utility from contamination-related effects, models contaminated on MMLU are evaluated on the unrelated TruthfulQA benchmark, and vice versa. As shown in Table cite112†3 , DeconIEP incurs minimal BUD across all model families, whereas several white-box baselines exhibit substantially larger utility degradation.
L283: These results indicate that the proposed embedding-space intervention effectively mitigates contamination while preserving benign performance, with advantages that remain stable across heterogeneous architectures.
L284: Model  | Method  | Access  | Benign Utility Drop $\downarrow$
L285: TruthfulQA  | MMLU
L286: Mistral  | DeconIEP  | White-box  | 0.019  | 0.016
L287: TED  | Black-box  | 0.028  | 0.030
L288: ITD  | Black-box  | 0.000  | 0.001
L289: Shortcut Neuron  | White-box  | 0.129  | 0.152
L290: Short Circuit  | White-box  | 0.057  | 0.077
L291: Qwen2.5  | DeconIEP  | White-box  | 0.009  | 0.029
L292: TED  | Black-box  | 0.110  | 0.022
L293: ITD  | Black-box  | 0.000  | 0.002
L294: Shortcut Neuron  | White-box  | 0.207  | 0.256
L295: Short Circuit  | White-box  | 0.172  | 0.238
L296: LLaMA-3  | DeconIEP  | White-box  | 0.031  | 0.041
L297: TED  | Black-box  | 0.012  | 0.035
L298: ITD  | Black-box  | 0.010  | 0.016
L299: Shortcut Neuron  | White-box  | 0.057  | 0.190
L300: Short Circuit  | White-box  | 0.105  | 0.161
L301: Table 3: BUD under cross-benchmark evaluation ($o=3$). We contaminate each model on MMLU and measure the utility drop on TruthfulQA to assess benign performance on clean data, and vice versa. ($\zeta=10^{-3}$)
L302: ### 5.3 Evaluation across Model scale
L303: 
L304: We evaluate our decontamination method across model scales using four Qwen2.5 models (cite104†Yang et al., 2025 ): Qwen2.5-1.5B-Instruct, Qwen2.5-3B-Instruct, Qwen2.5-7B-Instruct, and Qwen2.5-14B-Instruct. Figure cite113†3 shows that our method maintains stable decontamination effectiveness across all scales, indicating that it generalizes beyond a specific model size, with only mild variation across model capacities.
L305: ### 5.4 Semantic preservation
L306: 
L307: Then, we verify that embedding perturbations preserve input semantics. We measure the average cosine similarity between the original embedding and the perturbed embedding,
L308: 
L309:  | $$\mathrm{Cos}(\zeta)\;=\;\mathbb{E}_{x}\Big[\cos\big(e(x),\,e(x)+\delta(x)\big)\Big],$$  |
L310: using the same pooling operator as in our implementation. Figure cite114†4 shows that for practical budgets $\zeta\leq 10^{-3}$, cosine similarity remains close to $1$, and consistently exceeds the similarity between the original prompt and its rewritten counterpart. This suggests that embedding-level intervention introduces less semantic drift than rewriting while still enabling effective decontamination.
L311: cite115†Image: Refer to caption Figure 4: Semantic invariance under embedding perturbations. Mean cosine similarity between original and perturbed embeddings (orig vs. orig+$\delta$) versus $\zeta$ on MMLU and TruthfulQA. Dashed lines show orig vs. paraphrased as a semantic-preserving reference.
L312: ### 5.5 Ablation Study
L313: $\zeta$  | TruthfulQA  | MMLU
L314: RC $\downarrow$  | BUD $\downarrow$  |  | RC $\downarrow$  | BUD $\downarrow$
L315: $1\mathrm{e}{-5}$  | 0.512  | 0.000  |  | 0.344  | 0.000
L316: $3\mathrm{e}{-5}$  | 0.393  | 0.009  |  | 0.304  | 0.000
L317: $1\mathrm{e}{-4}$  | 0.226  | 0.024  |  | 0.214  | 0.022
L318: $3\mathrm{e}{-4}$  | 0.096  | 0.034  |  | 0.184  | 0.031
L319: $1\mathrm{e}{-3}$  | 0.062  | 0.038  |  | 0.165  | 0.041
L320: $3\mathrm{e}{-3}$  | 0.024  | 0.050  |  | 0.034  | 0.070
L321: $1\mathrm{e}{-2}$  | 0.022  | 0.062  |  | 0.032  | 0.102
L322: Table 4: RC–BUD trade-off induced by the perturbation budget $\zeta$. We report RC and BUD for DeconIEP under different $\zeta$ on TruthfulQA and MMLU for contaminated Llama 3 model, $o=3$ .
L323: #### Controllability via the perturbation budget $\zeta$
L324: We next treat $\zeta$ as an explicit control knob that trades off decontamination strength against benign utility. Table cite116†4 shows the relationship between RC and BUD induced by varying $\zeta$. As $\zeta$ increases, DeconIEP moves toward lower RC at the cost of higher BUD, forming a clear and monotonic trade-off curve.
L325: Compared with representative baselines (see Appendix cite68†E.4 ), DeconIEP provides a more favorable RC–BUD region, and the practical budget regime yields strong contamination suppression with limited utility loss.
L326: #### Effect of reference model
L327: 
L328: Finally, we examine the role of the reference model. While our method uses a reference model to guide perturbation generation, a perfectly clean anchor may be unavailable in practice. We therefore test robustness when the reference model is mildly contaminated.
L329: We construct imperfect references by fine-tuning the reference model on data containing different proportions of benchmark test items, yielding varying contamination ratios, and then run our method under the same contaminated evaluation setting. Figure cite117†5 shows that performance is largely stable as the reference contamination increases from $0\%$ to $30\%$ across benchmarks and occurrence levels.
L330: This indicates that the reference need not be strictly clean: even mildly contaminated, it provides a sufficiently informative anchor distribution to steer the evaluated model away from contamination-driven behavior. In practice, a readily available same-architecture base model can serve as a reference.
L331: We also do experiments to investigate the difference between our perturbation and random noise, how the sample size of $D_{\mathrm{aux}}$ affects our proposal; due to space constraints, we report these results in Appendix cite73†E.5 and cite74†E.6 .
L332: 
L333: cite118†Image: Refer to caption Figure 5: Test accuracy under increasing contamination in the reference model.
L334: ## 6 Conclusion
L335: 
L336: Test-set contamination inflates benchmark scores, and detect-then-filter evaluation fails under moderate contamination due to detector errors. We propose DeconIEP, an inference-time method that applies small, $\ell_{\infty}$-bounded perturbations to input embeddings to align a contaminated model with a less-contaminated reference. Across multiple open-weight LLM families and two benchmarks, DeconIEP reduces residual contamination with minimal benign utility drop.
L337: ## 7 Limitations
L338: Our study has several limitations. First, DeconIEP is a white-box method: it requires access to input embeddings (and, in our training setup, gradients) to generate and apply perturbations, which limits applicability to closed-model APIs without additional approximations. Second, DeconIEP relies on a reference model to provide a comparatively less-contaminated behavioral anchor.
L339: While we empirically observe robustness to moderate reference contamination, performance may degrade when the reference is heavily contaminated, distributionally mismatched, or differs substantially in alignment behavior from the evaluated model. Then, although our intervention is bounded and empirically exhibits strong semantic invariance (e.g., high cosine similarity under small $\zeta$), we do not provide formal guarantees that semantics/difficulty are preserved for all inputs.
L340: Finally, DeconIEP introduces additional inference overhead for perturbation generation and reference-guided objectives; while lightweight relative to multi-query black-box baselines, reducing overhead for very large-scale evaluation remains an important direction.
L341: ## References
L342:   * Brown et al. (2020) Tom Brown, Benjamin Mann, Nick Ryder, Melanie Subbiah, Jared D Kaplan, Prafulla Dhariwal, Arvind Neelakantan, Pranav Shyam, Girish Sastry, Amanda Askell, and 1 others. 2020. Language models are few-shot learners. Advances in neural information processing systems, 33:1877–1901.
L343:   * Carlini et al. (2022) Nicholas Carlini, Steve Chien, Milad Nasr, Shuang Song, Andreas Terzis, and Florian Tramer. 2022. Membership inference attacks from first principles. In 2022 IEEE symposium on security and privacy (SP), pages 1897–1914. IEEE.
L344:   * Carlini et al. (2021) Nicholas Carlini, Florian Tramèr, Eric Wallace, Matthew Jagielski, Ariel Herbert-Voss, Katherine Lee, Adam Roberts, Tom Brown, Dawn Song, Úlfar Erlingsson, Alina Oprea, and Colin Raffel. 2021. cite119†Extracting training data from large language models†www.usenix.org . In 30th USENIX Security Symposium (USENIX Security 21), pages 2633–2650. USENIX Association.
L345:   * Chen et al. (2025) Simin Chen, Yiming Chen, Zexin Li, Yifan Jiang, Zhongwei Wan, Yixin He, Dezhi Ran, Tianle Gu, Haizhou Li, Tao Xie, and 1 others. 2025. Benchmarking large language models under data contamination: A survey from static to dynamic evaluation. In Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing, pages 10091–10109.
L346:   * Deng et al. (2024a) Chunyuan Deng, Yilun Zhao, Yuzhao Heng, Yitong Li, Jiannan Cao, Xiangru Tang, and Arman Cohan. 2024a. cite120†Unveiling the spectrum of data contamination in language models: A survey from detection to remediation . Preprint, arXiv:2406.14644.
L347:   * Deng et al. (2024b) Chunyuan Deng, Yilun Zhao, Xiangru Tang, Mark Gerstein, and Arman Cohan. 2024b. Investigating data contamination in modern benchmarks for large language models. In Proceedings of the 2024 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies (Volume 1: Long Papers), pages 8706–8719.
L348:   * Dong et al. (2024) Yihong Dong, Xue Jiang, Huanyu Liu, Zhi Jin, Bin Gu, Mengfei Yang, and Ge Li. 2024. Generalization or memorization: Data contamination and trustworthy evaluation for large language models. In Findings of the Association for Computational Linguistics: ACL 2024, pages 12039–12050.
L349:   * Gao et al. (2021) Leo Gao, Jonathan Tow, Stella Biderman, Sid Black, Anthony DiPofi, Charles Foster, Laurence Golding, Jeffrey Hsu, Kyle McDonell, Niklas Muennighoff, and 1 others. 2021. A framework for few-shot language model evaluation. Zenodo.
L350:   * Grattafiori et al. (2024) Aaron Grattafiori, Abhimanyu Dubey, Abhinav Jauhri, Abhinav Pandey, Abhishek Kadian, Ahmad Al-Dahle, Aiesha Letman, Akhil Mathur, Alan Schelten, Alex Vaughan, Amy Yang, Angela Fan, Anirudh Goyal, Anthony Hartshorn, Aobo Yang, Archi Mitra, Archie Sravankumar, Artem Korenev, Arthur Hinsvark, and 542 others. 2024. cite121†The llama 3 herd of models . Preprint, arXiv:2407.21783.
L351:   * Hayes et al. (2018) Jamie Hayes, Luca Melis, George Danezis, and Emiliano De Cristofaro. 2018. cite122†Logan: Membership inference attacks against generative models . Preprint, arXiv:1705.07663.
L352:   * Hendrycks et al. (2021a) Dan Hendrycks, Collin Burns, Steven Basart, Andy Zou, Mantas Mazeika, Dawn Song, and Jacob Steinhardt. 2021a. cite123†Measuring massive multitask language understanding . Preprint, arXiv:2009.03300.
L353:   * Hendrycks et al. (2021b) Dan Hendrycks, Collin Burns, Steven Basart, Andy Zou, Mantas Mazeika, Dawn Song, and Jacob Steinhardt. 2021b. Measuring massive multitask language understanding. Proceedings of the International Conference on Learning Representations (ICLR).

