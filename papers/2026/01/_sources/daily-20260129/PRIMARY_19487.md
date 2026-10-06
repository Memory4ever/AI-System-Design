# Exact-v1 primary excerpts — 19487

L labels are local to each separated original response. Preserved necessary-source tool responses; no reproduction.

## Original response: stdnext3head

LLM-VA: Resolving the Jailbreak-Overrefusal Trade-off via Vector Alignment (https://arxiv.org/html/2601.19487v1)
citeturn28405view3 [wordlim: 200] Crawled: yesterday; Content type: text/html; Source: open({"ref_id":"https://arxiv.org/html/2601.19487v1","lineno":null}); Total lines: 648


## Original response: stdnext3core3

LLM-VA: Resolving the Jailbreak-Overrefusal Trade-off via Vector Alignment (https://arxiv.org/html/2601.19487v1)
citeturn28408view0 [wordlim: 200] Crawled: yesterday; Content type: text/html; Source: open({"ref_id":"turn28405view3","lineno":90}); Total lines: 648
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
L14: cite1†Why HTML?†info.arxiv.org cite2†Report Issue cite3†Back to Abstract cite4†Download PDF L15:   1. cite5†Abstract L16:   2. cite6†1 Introduction L17:   3. cite7†2 Related Work L18:     1. cite8†Safety Alignment and the Jailbreak-Overrefusal Trade-off L19:     2. cite9†Vector Steering Methods L20:     3. cite10†Internal Representations in LLMs L21:   4. cite11†3 Preliminary Analysis L22:     1. cite12†Why vector alignment, not magnitude adjustment? L23:     2. cite13†Optimization Objective L24:   5. cite14†4 Methodology L25:     1. cite15†4.1 SVM-based Control Vector Identification L26:     2. cite16†4.2 Layer Selection L27:       1. cite17†Influence on final decision. L28:       2. cite18†Classification accuracy. L29:       3. cite19†Combined score. L30:     3. cite20†4.3 Vector Alignment L31:       1. cite21†Deriving the weight update. L32:       2. cite22†Iterative refinement. L33:   6. cite23†5 Experiments L34:     1. cite24†5.1 Experimental Setup L35:       1. cite25†Models L36:       2. cite26†Datasets L37:       3. cite27†Baselines L38:       4. cite28†Metrics L39:     2. cite29†5.2 Effectiveness Results (RQ1) L40:       1. cite30†Overall effectiveness of LLM-VA. L41:       2. cite31†Comparison with baselines. L42:       3. cite32†Adaptive behavior. L43:       4. cite33†Cases requiring further analysis. L44:     3. cite34†5.3 Utility Preservation Results (RQ2) L45:       1. cite35†Overall utility preservation. L46:       2. cite36†Comparison with baselines. L47:       3. cite37†Task-specific analysis. L48:       4. cite38†Model size effects. L49:     4. cite39†5.4 Ablation Studies (RQ3) L50:       1. cite40†Vector Identification. L51:       2. cite41†Iteration Number. L52:       3. cite42†Layer Selection. L53:   7. cite43†6 Conclusion L54:   8. cite44†7 Limitations L55:     1. cite45†Binary toxicity assumption. L56:     2. cite46†Model scale. L57:     3. cite47†Training data dependency. L58:     4. cite48†Reasoning models. L59:     5. cite49†Model-specific tuning. L60:     6. cite50†Transferability. L61:     7. cite51†Static alignment. L62:     8. cite52†Customized Trade-off. L63:     9. cite53†Experimental methodology. L64:   9. cite54†8 Ethical Considerations L65:     1. cite55†8.1 Potential Risks L66:     2. cite56†8.2 AI Assistants Usage L67:   10. cite57†References L68:   11. cite58†A Angles between Answer Vectors and Benign Vectors L69:   12. cite59†B Discussion on Layer Type Selection L70:   13. cite60†C Additional Instructions on General Ability Datasets L71:   14. cite61†D Details about Experimental Setup L72:   15. cite62†E Details on Judge Model Selection L73:   16. cite63†F Detailed Results on Iteration Number L74:   17. cite64†G Transferability Experiments L75: cite65†License: CC BY 4.0†info.arxiv.org L76: 
L77: arXiv:2601.19487v1 [cs.LG] 27 Jan 2026
L78: # LLM-VA: Resolving the Jailbreak-Overrefusal Trade-off via Vector Alignment
L79: 
L80: Haonan Zhang Affiliation: Zhejiang University    Dongxia Wang Affiliation: Zhejiang University    Yi Liu Affiliation: Quantstamp    Kexin Chen Affiliation: Zhejiang University    Wenhai Wang Affiliation: Zhejiang University Affiliation: Huzhou Institute of Industrial Control Technology{kxchen, dxwang, haonanzhang, zdzzlab}@zju.edu.cn, yi009@e.ntu.edu.sg
L81: ###### Abstract
L82: Safety-aligned LLMs suffer from two failure modes: jailbreak (answering harmful inputs) and over-refusal (declining benign queries). Existing vector steering methods adjust the magnitude of answer vectors, but this creates a fundamental trade-off—reducing jailbreak increases over-refusal and vice versa.
L83: We identify the root cause: LLMs encode the decision to answer (answer vector $v_{a}$) and the judgment of input safety (benign vector $v_{b}$) as nearly orthogonal directions, treating them as independent processes. We propose LLM-VA, which aligns $v_{a}$ with $v_{b}$ through closed-form weight updates, making the model’s willingness to answer causally dependent on its safety assessment—without fine-tuning or architectural changes.
L84: Our method identifies vectors at each layer using SVMs, selects safety-relevant layers, and iteratively aligns vectors via minimum-norm weight modifications. Experiments on 12 LLMs demonstrate that LLM-VA achieves 11.45% higher F1 than the best baseline while preserving 95.92% utility, and automatically adapts to each model’s safety bias without manual tuning. Code and models are available at cite66†https://hotbento.github.io/LLM-VA-Web/†hotbento.github.io .
L85: ^{$\dagger$}^{$\dagger$}footnotetext: Corresponding Author
L86: ## 1 Introduction
L87: Large language models (LLMs) have achieved remarkable capabilities across diverse NLP tasks (cite67†OpenAI, 2024 ; cite68†Team, 2025 ; cite69†AI@Meta, 2024 ), yet safety alignment remains challenging.
L88: Safety-aligned LLMs exhibit two failure modes: jailbreak, where the model directly responds to toxic inputs (i.e., queries designed to elicit harmful, unethical, or unsafe responses) (cite70†Chen et al., 2024 ; cite71†Deng et al., 2024 ; cite72†Yuan et al., 2025 ; cite73†Liu et al., 2024b ), and over-refusal, where the model unnecessarily declines benign queries (cite74†Röttger et al., 2024 ; cite75†Zhang et al., 2025a ; cite76†Cui et al., 2025 ).
L89: This dual failure mode significantly limits the deployment of LLMs in safety-critical applications, where both reliability and usability are essential. Among approaches to address these issues, vector steering (cite77†Zou et al., 2023a ; cite78†Arditi et al., 2024 ; cite79†Sheng et al., 2025 ) has gained attention for its efficiency—it manipulates specific directions in the model’s latent space without costly retraining, using only simple answer/refuse labels rather than fine-grained annotations.
L90: However, existing vector steering methods only adjust the magnitude of the answer vector, creating a fundamental trade-off: reducing magnitude suppresses jailbreak but increases over-refusal, while amplifying it has the opposite effect (cite78†Arditi et al., 2024 ; cite79†Sheng et al., 2025 ). Recent methods like SCANS (cite80†Cao et al., 2025 ) and CAST (cite81†Lee et al., 2024 ) incorporate input toxicity but require architectural modifications and treat both failure modes as separate objectives (see Table cite82†1 ).
L91: This magnitude-based paradigm cannot fundamentally resolve the trade-off.
L92: Figure 1: The angles between answer vectors ($v_{a}$) and benign vectors ($v_{b}$) are approximately $90^{\circ}$ across layers in gemma-2-9b-it, indicating near-orthogonality between answer decisions and safety assessments.
L93: We identify the root cause of this trade-off: existing methods control output behavior (answer vs. refuse) without considering input characteristics (benign vs. toxic). To investigate, we extract two vectors at each layer: the answer vector ($v_{a}$), indicating whether the model will answer, and the benign vector ($v_{b}$), indicating whether the input is safe.
L94: As shown in Figure cite83†1 , these vectors are nearly orthogonal (${\sim}90^{\circ}$) across layers,^{1}^{1} 1 Results for other LLMs are similar; see Appendix cite58†A . revealing that LLMs treat answer decisions and safety assessments as independent processes. This explains both failure modes: the model may answer toxic inputs (jailbreak) or refuse benign ones (over-refusal) because its willingness to answer is decoupled from its judgment of input safety.
L95: Based on this observation, we propose L arge L anguage M odel V ector A lignment (LLM-VA). By aligning these vectors, we make the model’s willingness to answer causally dependent on its safety assessment (cite77†Zou et al., 2023a ), rather than treating them as independent decisions. Crucially, LLM-VA achieves this through closed-form weight updates—requiring no gradient-based optimization, fine-tuning, or architectural changes. Our method involves three steps:
L96: 
L97:   * •
L98: Vector identification via SVMs: Train SVMs at each layer to find hyperplanes separating benign/toxic and answer/refuse samples, yielding both $v_{b}$ and $v_{a}$.
L99: 
L100:   * •
L101: 
L102: Layer selection: Identify layers most relevant to safety decisions based on their contribution to final output and SVM classification accuracy.
L103: 
L104:   * •
L105: 
L106: Vector alignment: Adjust layer weights to align $v_{a}$ with $v_{b}$, ensuring benign inputs activate the “answer” direction while toxic inputs do not.
L107: Extensive experiments on 12 LLMs demonstrate that LLM-VA achieves 11.45% higher F1 scores (effectiveness on resolving trade-off) than the best baseline (AlphaSteer) (cite79†Sheng et al., 2025 ) with only 4.08% model utility drop, indicating that LLM-VA effectively resolves the jailbreak-overrefusal trade-off while preserving general capabilities. In summary, our contributions are:
L108: 
L109:   * •
L110: We propose LLM-VA, which, to the best of our knowledge, is the first vector steering method that simultaneously addresses both jailbreak and over-refusal by aligning answer vectors with benign vectors through closed-form weight updates—requiring no gradient-based fine-tuning or architectural changes.
L111: 
L112:   * •
L113: We demonstrate on 12 LLMs from 5 model families that LLM-VA achieves state-of-the-art safety alignment, and show that it automatically adapts to each model’s safety bias—prioritizing jailbreak reduction for vulnerable models and over-refusal reduction for overly conservative ones—without manual tuning.
L114: 
L115:   * •
L116: We release our code and safety-enhanced weights for 12 LLMs.^{2}^{2} 2 We release only Llama3.1-8B-Instruct weights during review. Full weights available at cite84†https://figshare.com/s/f2aa365c87a80097a436†figshare.com .
L117: ## 2 Related Work
L118: #### Safety Alignment and the Jailbreak-Overrefusal Trade-off
L119: Traditional safety alignment methods—RLHF (cite85†Christiano et al., 2017 ; cite86†Stiennon et al., 2020 ), adversarial training (cite87†Xhonneux et al., 2024 ; cite88†Liu et al., 2024a ), and rule-based filtering (cite89†Zhang et al., 2025b ; cite90†Liu et al., 2024c )—require substantial computational resources or lack scalability. Vector steering (cite77†Zou et al., 2023a ; cite78†Arditi et al., 2024 ) emerged as an efficient alternative, manipulating latent-space directions without retraining.
L120: However, these methods create a fundamental trade-off: reducing the answer vector’s magnitude suppresses jailbreak but increases over-refusal, while amplifying it has the opposite effect (cite78†Arditi et al., 2024 ; cite79†Sheng et al., 2025 ). This trade-off remains the central unsolved problem in efficient safety alignment.
L121: #### Vector Steering Methods
L122: VectorSteer (cite77†Zou et al., 2023a ) first identified answer vectors for controlling model outputs through magnitude adjustment. AlphaSteer (cite79†Sheng et al., 2025 ) introduced null-space projection to preserve utility during steering, but remains magnitude-based and thus inherits the trade-off. SCANS (cite80†Cao et al., 2025 ) and CAST (cite81†Lee et al., 2024 ) incorporate input toxicity information, representing progress toward input-aware steering.
L123: However, both require architectural modifications (hook layers) and still treat jailbreak and over-refusal as separate objectives to be balanced via hyperparameters. Table cite82†1 summarizes these differences: LLM-VA is the only approach that addresses both failure modes without finetuning or architectural changes.
L124: #### Internal Representations in LLMs
L125: Mechanistic interpretability research reveals that LLMs encode concepts as linear directions in their hidden states (cite91†Geva et al., 2021 ; cite92†Elhage et al., 2022 ; cite77†Zou et al., 2023a ). Building on this foundation, we discover that answer vectors ($v_{a}$) and benign vectors ($v_{b}$) are nearly orthogonal across layers, explaining why magnitude-based methods cannot resolve the trade-off—they control output behavior independently of input safety.
L126: LLM-VA addresses this by aligning these vectors, making the answer decision causally dependent on the safety assessment.
L127: Table 1: Comparison of LLM-VA with other methods on safety alignment and utility preservation.
L128: 
L129: Method  | w/o Finetuning  | w/o Model Structure Modification  | Over-refusal Mitigation  | Jailbreak Mitigation
L130: LLM-VA  | ✓  | ✓  | ✓  | ✓
L131: Finetuning  | ✗  | ✓  | ✓  | ✓
L132: VectorSteer  | ✓  | ✗  | ✗  | ✓
L133: AlphaSteer  | ✓  | ✗  | ✗  | ✓
L134: CAST  | ✓  | ✗  | ✓  | ✓
L135: SCANS  | ✓  | ✗  | ✓  | ✓
L136: Figure 2: The distributions of the projections onto the benign, answer vectors at different layers of Llama-3.1-8B-Instruct. The left, middle, right figures correspond to the 4th, 16th, and 28th MLP layers, respectively.
L137: ## 3 Preliminary Analysis
L138: To motivate our approach, we analyze how LLMs internally represent two distinct decisions: (1) whether to answer or refuse a query, and (2) whether the input is benign or toxic.^{3}^{3} 3 We define “answer” as providing a direct response and “refuse” as declining to respond. Following cite77†Zou et al.
L139: (2023a) , we extract the answer vector $v_{a}$ and benign vector $v_{b}$ at each layer on 128 randomly sampled toxic inputs from S-Eval (cite72†Yuan et al., 2025 ) and 128 benign inputs from ORFuzzSet (cite75†Zhang et al., 2025a ).^{4}^{4} 4 We illustrate with Llama-3.1-8B-Instruct; results are consistent across models. We project layer outputs onto these vectors and visualize the distributions in Figure cite93†2 . Three key observations emerge:
L140:   * •
L141: 
L142: Obs 1: LLMs encode both decisions internally. Projections onto $v_{b}$ cleanly separate benign from toxic inputs, while projections onto $v_{a}$ separate answered from refused samples—both with decision boundaries near zero.
L143: 
L144:   * •
L145: 
L146: Obs 2: Later layers are more discriminative. Separation quality improves in deeper layers (compare layers 4, 16, and 28 in Figure cite93†2 ), indicating that later layers are more critical for safety-related decisions.
L147: 
L148:   * •
L149: Obs 3: The two decisions are misaligned. Some toxic inputs project positively onto $v_{a}$, while some benign inputs project negatively. This misalignment directly causes jailbreak and over-refusal failures.
L150: Combined with the near-orthogonality between $v_{a}$ and $v_{b}$ (Figure cite83†1 ), these observations reveal that LLMs treat answer decisions and safety assessments as independent processes. We hypothesize that aligning $v_{a}$ with $v_{b}$—making the model’s willingness to answer depend on its safety judgment—will reduce both failure modes.
L151: Figure 3: Unlike existing methods that only adjust the magnitude of $v_{a}$ (trading off jailbreak vs. over-refusal), LLM-VA aligns $v_{a}$ with $v_{b}$ to address both issues.
L152: #### Why vector alignment, not magnitude adjustment?
L153: 
L154: Existing vector steering methods (cite79†Sheng et al., 2025 ; cite80†Cao et al., 2025 ; cite94†Ray and Bhalani, 2024 ) only adjust the magnitude of $v_{a}$: reducing it decreases jailbreak risk but increases over-refusal, while increasing it has the opposite effect (Figure cite95†3 a). In contrast, LLM-VA aligns $v_{a}$ with $v_{b}$ (Figure cite95†3 b), making the answer decision depend on input safety rather than treating them independently.
L155: #### Optimization Objective
L156: 
L157: We formalize this goal as maximizing correct response behavior:
L158: 
L159:  | $\displaystyle\max_{\theta}\;\mathbb{E}_{x}\big[\mathbb{I}(y{=}\text{benign})\cdot\mathbb{I}(f_{\theta}(x){=}\text{answer})+$  |
L160:  | $\displaystyle\mathbb{I}(y{=}\text{toxic})\cdot\mathbb{I}(f_{\theta}(x){=}\text{refuse})\big]$  |  | (1)
L161: where $x$ is an input, $y\in\{\text{benign},\text{toxic}\}$ its ground-truth label, and $f_{\theta}(x)\in\{\text{answer},\text{refuse}\}$ the model’s response. By aligning $v_{a}$ with $v_{b}$, projections onto $v_{a}$ become correlated with input benignness, optimizing this objective. The following sections detail how LLM-VA achieves this.
L162: 
L163: cite96†Image: Refer to caption Figure 4: The framework of LLM-VA.
L164: ## 4 Methodology
L165: Building on our observation that LLMs encode answer decisions ($v_{a}$) and safety assessments ($v_{b}$) as nearly orthogonal directions, we present LLM-VA. Our key insight is that by aligning these vectors through closed-form weight updates—requiring no gradient-based fine-tuning or architectural changes—we can make the model’s willingness to answer causally dependent on its safety judgment.
L166: As illustrated in Figure cite97†4 , LLM-VA mainly consists of three steps: (1) identifying $v_{a}$ and $v_{b}$ at each layer via SVMs (Section cite15†4.1 ), (2) selecting layers most relevant to safety decisions (Section cite16†4.2 ), and (3) deriving weight update process that aligns these vectors (Section cite20†4.3 ).
L167: ### 4.1 SVM-based Control Vector Identification
L168: To align vectors at each layer, we must first identify them. Prior work (cite77†Zou et al., 2023a ; cite79†Sheng et al., 2025 ; cite80†Cao et al., 2025 ) extracts the answer vector from the residual flow at the final layer. However, since the residual flow aggregates contributions from all preceding layers, modifying individual layer weights cannot directly control the final-layer vector. To enable layer-wise weight modification, we instead extract vectors from each layer’s output.
L169: At each layer, we train two linear SVMs to find hyperplanes separating (1) benign vs. toxic inputs, and (2) answered vs. refused samples. We use SVMs because they provide interpretable linear decision boundaries: the normal vector of the maximum-margin hyperplane directly yields the control vector, and the margin maximization ensures robustness. The SVMs minimize (cite98†Cortes and Vapnik, 1995 ):
L170:  | $\displaystyle\min_{w_{svm},\zeta}{\|w_{svm}\|^{2}_{2}+C\sum_{i\in\mathcal{D}}\zeta_{i}},$  |
L171:  | $\displaystyle\text{s.t. }y_{i}(w_{svm}\cdot o^{(l)}_{i})\geq 1-\zeta_{i},\;\forall i\in\mathcal{D}$  |  | (2)
L172: where $o^{(l)}_{i}$ is the output of layer $l$ for input $i$, $y_{i}\in\{-1,1\}$ is the label ($+1$ for benign/answer, and $-1$ for toxic/refuse), $C>0$ is a regularization parameter, and $\zeta_{i}\geq 0$ are slack variables. We omit the bias term $b_{svm}$ because our empirical analysis shows that decision hyperplanes pass through the origin. This simplifies the subsequent alignment formulation and implementation.
L173: 
L174: The unit normal vectors of these hyperplanes yield the control vectors:
L175:  | $\displaystyle v_{b}^{(l)}=\nicefrac{{w_{b}^{(l)}}}{{\left\lVert w_{b}^{(l)}\right\rVert}}$  |  | (3)
L176:  | $\displaystyle\quad v_{a}^{(l)}=\nicefrac{{w_{a}^{(l)}}}{{\left\lVert w_{a}^{(l)}\right\rVert}}$  |  | (4)
L177: 
L178: where $w_{b}^{(l)}$ and $w_{a}^{(l)}$ are the SVM weight vectors for benign/toxic and answer/refuse classification at layer $l$, respectively.
L179: ### 4.2 Layer Selection
L180: Not all layers contribute equally to safety decisions (cite91†Geva et al., 2021 ). Modifying irrelevant layers wastes capacity and may harm utility, so we select layers that are both influential (their vectors align with the decisions of final residual stream) and accurate (their SVMs reliably distinguish benign/toxic or answer/refuse).^{5}^{5} 5 Throughout this paper, “layer” refers to either an MLP or attention sublayer unless otherwise specified. Reasons are discussed in Appendix cite59†B .
L181: #### Influence on final decision.
L182: 
L183: Following prior work showing that the residual stream determines final outputs (cite77†Zou et al., 2023a ; cite79†Sheng et al., 2025 ), we measure how well each layer’s vectors align with the vectors of final residual stream:
L184: 
L185:  | $\displaystyle C_{a}^{(l)}=v^{(fin)}_{a}\cdot v^{(l)}_{a},\quad C_{b}^{(l)}=v^{(fin)}_{b}\cdot v^{(l)}_{b}$  |  | (5)
L186: 
L187: High $C^{(l)}$ indicates that modifying layer $l$’s vector direction will propagate to the final decision.
L188: #### Classification accuracy.
L189: 
L190: We also require that the layer’s SVMs accurately separate the two classes. Let $\text{Acc}^{(l)}_{a}$ and $\text{Acc}^{(l)}_{b}$ denote validation accuracies for the answer and benign classifiers at layer $l$.
L191: #### Combined score.
L192: 
L193: We compute a weighted sum where each term is the product of influence and accuracy for each task:
L194: 
L195:  | $$Score^{(l)}=C^{(l)}_{a}\cdot\text{Acc}^{(l)}_{a}+C^{(l)}_{b}\cdot\text{Acc}^{(l)}_{b}$$  |  | (6)
L196: The multiplicative form within each term ensures we select layers that are both influential and accurate for that task—a layer with high influence but low accuracy (or vice versa) contributes little to the score. We select the top $L_{select}$ layers with the highest scores for alignment.
L197: ### 4.3 Vector Alignment
L198: 
L199: Our goal is to modify each selected layer’s weights so that the model’s answer decision becomes dependent on its safety assessment. Specifically, for any input, we want the projection onto $v_{a}$ (which determines answering) to equal the scaled projection onto $v_{b}$ (which reflects input safety). This ensures benign inputs activate the “answer” direction while toxic inputs suppress it.
L200: Unlike existing methods (cite77†Zou et al., 2023a ; cite79†Sheng et al., 2025 ; cite80†Cao et al., 2025 ) that insert hook layers and modify the model architecture, we derive a closed-form weight update process—requiring no gradient descent or architectural changes. This makes LLM-VA efficient and easy to deploy on standard model-hosting platforms.
L201: #### Deriving the weight update.
L202: 
L203: For each selected layer, we modify the down-projection matrix $W$ (the matrix that projects from hidden dimension back to model dimension). We seek an update $\Delta$ such that (omitting layer indices for clarity):
L204: 
L205:  | $$x(W+\Delta)v_{a}=\frac{\sigma_{a}}{\sigma_{b}}xWv_{b},\quad\forall x$$  |  | (7)
L206: where $\sigma_{a}$ and $\sigma_{b}$ are the standard deviations of projections onto $v_{a}$ and $v_{b}$ over the training set, respectively. The ratio $\sigma_{a}/\sigma_{b}$ normalizes for different dynamic ranges of the two directions, ensuring benign inputs (positive $v_{b}$ projection) produce positive $v_{a}$ projections and toxic inputs (negative $v_{b}$ projection) produce negative $v_{a}$ projections. Rearranging, we require:
L207:  | $$\Delta v_{a}=\frac{\sigma_{a}}{\sigma_{b}}Wv_{b}-Wv_{a}$$  |  | (8)
L208: 
L209: The minimum-norm solution (least modification to weights) is given by the pseudoinverse (cite99†Penrose, 1955 ):
L210: 
L211:  | $\displaystyle\Delta^{+}=\left(\frac{\sigma_{a}}{\sigma_{b}}Wv_{b}-Wv_{a}\right)v_{a}^{T},$  |  | (9)
L212:  | $\displaystyle W^{\prime}=W+\Delta^{+}$  |
L213: #### Iterative refinement.
L214: A single alignment step may not fully align the vectors because modifying one layer’s weights affects the inputs to subsequent layers, causing their effective $v_{a}$ and $v_{b}$ directions to shift. We therefore iterate the alignment process $T$ times: in each iteration, we re-extract $v_{a}$ and $v_{b}$ from the modified model, recompute layer scores, and apply the weight update. The final model is selected based on validation F1 score.
L215: Empirically, most models converge within 20–30 iterations (see Section cite41†5.4 ).
L216: ## 5 Experiments
L217: 
L218: We conduct experiments to address the following research questions:
L219: 
L220:   * •
L221: 
L222: RQ1: How effectively does LLM-VA resolve jailbreak-overrefusal trade-off compared to magnitude-based vector steering methods?
L223: 
L224:   * •
L225: 
L226: RQ2: How well does LLM-VA preserve model utility?
L227: 
L228:   * •
L229: 
L230: RQ3: How do key components (vector identification, iteration count, layer selection) affect performance?
L231: ### 5.1 Experimental Setup
L232: 
L233: We first describe the experimental settings. Additional details are provided in Appendix cite61†D .
L234: #### Models
L235: We conduct experiments on 12 widely-used instruction-tuned LLMs spanning 5 model families, with sizes ranging from 3B to 14B parameters: Llama-3.1 (8B) (cite69†AI@Meta, 2024 ), gemma-2 (9B) (cite100†Team, 2024a ), Mistral-v0.3 (7B) (cite101†Jiang et al., 2023 ), Phi-3.5 (4B) (cite102†Abdin et al., 2024 ), Phi-4 (4B, 15B) (cite103†Microsoft et al., 2025 ), Qwen2.5 (3B, 7B, 14B) (cite104†Team, 2024b ; cite105†Yang et al., 2024a ), and Qwen3 (4B, 8B, 14B) (cite68†Team, 2025 ).
L236: This diverse selection allows to evaluate the generalizability of LLM-VA across different architectures and scales.
L237: #### Datasets
L238: For effectiveness evaluation, we use four benchmark datasets: S-Eval-Attack and S-Eval-Risk (cite72†Yuan et al., 2025 ) for jailbreak evaluation, and ORFuzzSet (cite75†Zhang et al., 2025a ) and Natural Questions (cite106†Kwiatkowski et al., 2019 ) for over-refusal evaluation. To focus on challenging cases, we select 500 samples per dataset where the original models exhibit incorrect behavior (i.e., jailbreak on toxic inputs or over-refusal on benign inputs).
L239: Each dataset is split into training, validation, and test sets with a ratio of 8:1:1.
L240: For utility preservation, we evaluate on 6 datasets covering diverse NLP tasks including grammar (CoLA (cite107†Warstadt et al., 2018 )), natural language inference (MNLI (cite108†Williams et al., 2018 ), RTE (cite109†Bentivogli et al., 2009 )), paraphrase detection (MRPC (cite110†Dolan and Brockett, 2005 )), sentiment analysis (SST (cite111†Socher et al., 2013 )), and mathematical reasoning (GSM8K (cite112†Cobbe et al., 2021 )).^{6}^{6} 6 See Appendix cite60†C for dataset details.
L241: #### Baselines
L242: 
L243: We compare LLM-VA with several state-of-the-art vector steering methods:
L244: 
L245:   * •
L246: 
L247: VectorSteer (cite77†Zou et al., 2023a ): Identifies the answer vector and adjusts its magnitude to control the model’s response behavior.
L248: 
L249:   * •
L250: 
L251: AlphaSteer (cite79†Sheng et al., 2025 ): Extends VectorSteer by introducing null-space projection on representation space to preserve the model’s general capabilities while steering.
L252: 
L253:   * •
L254: SCANS (cite80†Cao et al., 2025 ): Dynamically adjusts answer vector magnitude based on input toxicity judgement, using hook layers to incorporate toxicity information.
L255: 
L256:   * •
L257: 
L258: AlphaSteer+: Our variant of AlphaSteer that uses null-space projection to preserve behavior specifically on correctly-answered samples rather than general capabilities.
L259: #### Metrics
L260: We use attack success rate (ASR) (cite113†Zou et al., 2023b ) to measure jailbreak vulnerability and over-refusal rate (ORR) (cite75†Zhang et al., 2025a ) to measure unnecessary refusals. For evaluation of effectiveness on resolving the trade-off, we report F1 scores with all the four datasets, where $TP{=}|\text{benign}\cap\text{answered}|$, $FP{=}|\text{toxic}\cap\text{answered}|$, $FN{=}|\text{benign}\cap\text{refused}|$, and $TN{=}|\text{toxic}\cap\text{refused}|$.


## Original response: stdnext3eval2

LLM-VA: Resolving the Jailbreak-Overrefusal Trade-off via Vector Alignment (https://arxiv.org/html/2601.19487v1)
citeturn28410view0 [wordlim: 200] Crawled: yesterday; Content type: text/html; Source: open({"ref_id":"turn28405view3","lineno":290}); Total lines: 648
L207:  | $$\Delta v_{a}=\frac{\sigma_{a}}{\sigma_{b}}Wv_{b}-Wv_{a}$$  |  | (8)
L208: 
L209: The minimum-norm solution (least modification to weights) is given by the pseudoinverse (cite99†Penrose, 1955 ):
L210: 
L211:  | $\displaystyle\Delta^{+}=\left(\frac{\sigma_{a}}{\sigma_{b}}Wv_{b}-Wv_{a}\right)v_{a}^{T},$  |  | (9)
L212:  | $\displaystyle W^{\prime}=W+\Delta^{+}$  |
L213: #### Iterative refinement.
L214: A single alignment step may not fully align the vectors because modifying one layer’s weights affects the inputs to subsequent layers, causing their effective $v_{a}$ and $v_{b}$ directions to shift. We therefore iterate the alignment process $T$ times: in each iteration, we re-extract $v_{a}$ and $v_{b}$ from the modified model, recompute layer scores, and apply the weight update. The final model is selected based on validation F1 score.
L215: Empirically, most models converge within 20–30 iterations (see Section cite41†5.4 ).
L216: ## 5 Experiments
L217: 
L218: We conduct experiments to address the following research questions:
L219: 
L220:   * •
L221: 
L222: RQ1: How effectively does LLM-VA resolve jailbreak-overrefusal trade-off compared to magnitude-based vector steering methods?
L223: 
L224:   * •
L225: 
L226: RQ2: How well does LLM-VA preserve model utility?
L227: 
L228:   * •
L229: 
L230: RQ3: How do key components (vector identification, iteration count, layer selection) affect performance?
L231: ### 5.1 Experimental Setup
L232: 
L233: We first describe the experimental settings. Additional details are provided in Appendix cite61†D .
L234: #### Models
L235: We conduct experiments on 12 widely-used instruction-tuned LLMs spanning 5 model families, with sizes ranging from 3B to 14B parameters: Llama-3.1 (8B) (cite69†AI@Meta, 2024 ), gemma-2 (9B) (cite100†Team, 2024a ), Mistral-v0.3 (7B) (cite101†Jiang et al., 2023 ), Phi-3.5 (4B) (cite102†Abdin et al., 2024 ), Phi-4 (4B, 15B) (cite103†Microsoft et al., 2025 ), Qwen2.5 (3B, 7B, 14B) (cite104†Team, 2024b ; cite105†Yang et al., 2024a ), and Qwen3 (4B, 8B, 14B) (cite68†Team, 2025 ).
L236: This diverse selection allows to evaluate the generalizability of LLM-VA across different architectures and scales.
L237: #### Datasets
L238: For effectiveness evaluation, we use four benchmark datasets: S-Eval-Attack and S-Eval-Risk (cite72†Yuan et al., 2025 ) for jailbreak evaluation, and ORFuzzSet (cite75†Zhang et al., 2025a ) and Natural Questions (cite106†Kwiatkowski et al., 2019 ) for over-refusal evaluation. To focus on challenging cases, we select 500 samples per dataset where the original models exhibit incorrect behavior (i.e., jailbreak on toxic inputs or over-refusal on benign inputs).
L239: Each dataset is split into training, validation, and test sets with a ratio of 8:1:1.
L240: For utility preservation, we evaluate on 6 datasets covering diverse NLP tasks including grammar (CoLA (cite107†Warstadt et al., 2018 )), natural language inference (MNLI (cite108†Williams et al., 2018 ), RTE (cite109†Bentivogli et al., 2009 )), paraphrase detection (MRPC (cite110†Dolan and Brockett, 2005 )), sentiment analysis (SST (cite111†Socher et al., 2013 )), and mathematical reasoning (GSM8K (cite112†Cobbe et al., 2021 )).^{6}^{6} 6 See Appendix cite60†C for dataset details.
L241: #### Baselines
L242: 
L243: We compare LLM-VA with several state-of-the-art vector steering methods:
L244: 
L245:   * •
L246: 
L247: VectorSteer (cite77†Zou et al., 2023a ): Identifies the answer vector and adjusts its magnitude to control the model’s response behavior.
L248: 
L249:   * •
L250: 
L251: AlphaSteer (cite79†Sheng et al., 2025 ): Extends VectorSteer by introducing null-space projection on representation space to preserve the model’s general capabilities while steering.
L252: 
L253:   * •
L254: SCANS (cite80†Cao et al., 2025 ): Dynamically adjusts answer vector magnitude based on input toxicity judgement, using hook layers to incorporate toxicity information.
L255: 
L256:   * •
L257: 
L258: AlphaSteer+: Our variant of AlphaSteer that uses null-space projection to preserve behavior specifically on correctly-answered samples rather than general capabilities.
L259: #### Metrics
L260: We use attack success rate (ASR) (cite113†Zou et al., 2023b ) to measure jailbreak vulnerability and over-refusal rate (ORR) (cite75†Zhang et al., 2025a ) to measure unnecessary refusals. For evaluation of effectiveness on resolving the trade-off, we report F1 scores with all the four datasets, where $TP{=}|\text{benign}\cap\text{answered}|$, $FP{=}|\text{toxic}\cap\text{answered}|$, $FN{=}|\text{benign}\cap\text{refused}|$, and $TN{=}|\text{toxic}\cap\text{refused}|$.
L261: For utility preservation, we report F1 for classification tasks where $TP,FP,FN$ are defined by the positive class of each task, and accuracy for GSM8K. We employ Qwen3-Guard-Gen-8B (cite114†Zhao et al., 2025 ) as the judge model for evaluating whether responses constitute answers or refusals.^{7}^{7} 7 See Appendix cite62†E for details on judge model selection.
L262: ### 5.2 Effectiveness Results (RQ1)
L263: 
L264: Table 2: Main results of LLM-VA. The best results are bolded.
L265: Model  | Size  | Method  | Seval-Aattack
L266: ASR↓  | Seval-Risk
L267: ASR↓  | ORFuzzSet
L268: ORR↓  | NQ
L269: ORR↓  | Final
L270: F1↑  | Model  | Size  | Method  | Seval-Aattack
L271: ASR↓  | Seval-Risk
L272: ASR↓  | ORFuzzSet
L273: ORR↓  | NQ
L274: ORR↓  | Final
L275: F1↑
L276: Llama-3.1  | 8B  | Original  | 12.00%  | 2.00%  | 100.00%  | 6.00%  | 0.6104  | Qwen2.5  | 3B  | Original  | 88.00%  | 20.00%  | 62.00%  | 14.00%  | 0.5741
L277: AlphaSteer+  | 4.00%  | 0.00%  | 100.00%  | 10.00%  | 0.6122  | AlphaSteer+  | 28.00%  | 0.00%  | 58.00%  | 10.00%  | 0.7333
L278: AlphaSteer  | 2.00%  | 0.00%  | 100.00%  | 6.00%  | 0.6351  | AlphaSteer  | 28.00%  | 6.00%  | 62.00%  | 10.00%  | 0.7072
L279: VectorSteer  | 0.00%  | 0.00%  | 100.00%  | 12.00%  | 0.6111  | VectorSteer  | 22.00%  | 2.00%  | 92.00%  | 32.00%  | 0.5067
L280: SCANS  | 4.00%  | 0.00%  | 100.00%  | 14.00%  | 0.5931  | SCANS  | 32.00%  | 4.00%  | 70.00%  | 6.00%  | 0.6889
L281: LLM-VA  | 14.00%  | 6.00%  | 38.00%  | 10.00%  | 0.8172  | LLM-VA  | 44.00%  | 12.00%  | 16.00%  | 16.00%  | 0.7925
L282: gemma-2  | 9B  | Original  | 42.00%  | 22.00%  | 98.00%  | 16.00%  | 0.4914  | 7B  | Original  | 86.00%  | 36.00%  | 80.00%  | 4.00%  | 0.5297
L283: AlphaSteer+  | 16.00%  | 0.00%  | 94.00%  | 4.00%  | 0.6415  | AlphaSteer+  | 32.00%  | 6.00%  | 82.00%  | 2.00%  | 0.6554
L284: AlphaSteer  | 16.00%  | 0.00%  | 98.00%  | 4.00%  | 0.6242  | AlphaSteer  | 28.00%  | 8.00%  | 86.00%  | 2.00%  | 0.6437
L285: VectorSteer  | 10.00%  | 0.00%  | 98.00%  | 18.00%  | 0.5714  | VectorSteer  | 16.00%  | 16.00%  | 80.00%  | 24.00%  | 0.5854
L286: SCANS  | 18.00%  | 12.00%  | 92.00%  | 12.00%  | 0.5890  | SCANS  | 30.00%  | 18.00%  | 86.00%  | 4.00%  | 0.6145
L287: LLM-VA  | 0.00%  | 6.00%  | 36.00%  | 6.00%  | 0.8681  | LLM-VA  | 54.00%  | 30.00%  | 22.00%  | 4.00%  | 0.7598
L288: Mistral-v0.3  | 7B  | Original  | 88.00%  | 74.00%  | 54.00%  | 4.00%  | 0.5635  | 14B  | Original  | 46.00%  | 22.00%  | 90.00%  | 4.00%  | 0.5668
L289: AlphaSteer+  | 28.00%  | 36.00%  | 52.00%  | 2.00%  | 0.7122  | AlphaSteer+  | 22.00%  | 4.00%  | 92.00%  | 2.00%  | 0.6386
L290: AlphaSteer  | 34.00%  | 32.00%  | 46.00%  | 2.00%  | 0.7273  | AlphaSteer  | 2.00%  | 4.00%  | 92.00%  | 2.00%  | 0.6795
L291: VectorSteer  | 32.00%  | 28.00%  | 44.00%  | 0.00%  | 0.7500  | VectorSteer  | 6.00%  | 0.00%  | 96.00%  | 0.00%  | 0.6710
L292: SCANS  | 26.00%  | 40.00%  | 28.00%  | 4.00%  | 0.7742  | SCANS  | 20.00%  | 24.00%  | 82.00%  | 8.00%  | 0.6215
L293: LLM-VA  | 36.00%  | 22.00%  | 28.00%  | 12.00%  | 0.7656  | LLM-VA  | 28.00%  | 22.00%  | 66.00%  | 2.00%  | 0.6911
L294: Phi-3.5  | 4B  | Original  | 82.00%  | 24.00%  | 90.00%  | 6.00%  | 0.5073  | Qwen3  | 4B  | Original  | 84.00%  | 32.00%  | 66.00%  | 0.00%  | 0.5956
L295: AlphaSteer+  | 18.00%  | 2.00%  | 88.00%  | 12.00%  | 0.6250  | AlphaSteer+  | 28.00%  | 30.00%  | 48.00%  | 2.00%  | 0.7353
L296: AlphaSteer  | 26.00%  | 6.00%  | 86.00%  | 10.00%  | 0.6190  | AlphaSteer  | 34.00%  | 26.00%  | 56.00%  | 0.00%  | 0.7129
L297: VectorSteer  | 20.00%  | 2.00%  | 78.00%  | 18.00%  | 0.6380  | VectorSteer  | 24.00%  | 2.00%  | 48.00%  | 2.00%  | 0.7979
L298: SCANS  | 4.00%  | 0.00%  | 96.00%  | 40.00%  | 0.4776  | SCANS  | 28.00%  | 10.00%  | 66.00%  | 2.00%  | 0.7135
L299: LLM-VA  | 66.00%  | 16.00%  | 50.00%  | 4.00%  | 0.6822  | LLM-VA  | 46.00%  | 28.00%  | 24.00%  | 0.00%  | 0.7822
L300: Phi-4  | 4B  | Original  | 60.00%  | 16.00%  | 68.00%  | 16.00%  | 0.5918  | 8B  | Original  | 92.00%  | 20.00%  | 72.00%  | 2.00%  | 0.5753
L301: AlphaSteer+  | 16.00%  | 8.00%  | 74.00%  | 6.00%  | 0.6977  | AlphaSteer+  | 18.00%  | 18.00%  | 60.00%  | 10.00%  | 0.7104
L302: AlphaSteer  | 18.00%  | 6.00%  | 70.00%  | 6.00%  | 0.7126  | AlphaSteer  | 24.00%  | 14.00%  | 58.00%  | 0.00%  | 0.7474
L303: VectorSteer  | 20.00%  | 8.00%  | 68.00%  | 6.00%  | 0.7119  | VectorSteer  | 22.00%  | 14.00%  | 40.00%  | 2.00%  | 0.8020
L304: SCANS  | 14.00%  | 12.00%  | 78.00%  | 36.00%  | 0.5513  | SCANS  | 26.00%  | 4.00%  | 84.00%  | 10.00%  | 0.6310
L305: LLM-VA  | 70.00%  | 26.00%  | 48.00%  | 8.00%  | 0.6545  | LLM-VA  | 36.00%  | 8.00%  | 24.00%  | 0.00%  | 0.8381
L306: 15B  | Original  | 22.00%  | 6.00%  | 98.00%  | 0.00%  | 0.6182  | 14B  | Original  | 86.00%  | 30.00%  | 86.00%  | 0.00%  | 0.5302
L307: AlphaSteer+  | 6.00%  | 0.00%  | 96.00%  | 2.00%  | 0.6623  | AlphaSteer+  | 28.00%  | 32.00%  | 52.00%  | 0.00%  | 0.7255
L308: AlphaSteer  | 2.00%  | 0.00%  | 96.00%  | 2.00%  | 0.6711  | AlphaSteer  | 26.00%  | 10.00%  | 46.00%  | 0.00%  | 0.7897
L309: VectorSteer  | 2.00%  | 2.00%  | 94.00%  | 4.00%  | 0.6667  | VectorSteer  | 18.00%  | 0.00%  | 72.00%  | 0.00%  | 0.7399
L310: SCANS  | 12.00%  | 0.00%  | 94.00%  | 6.00%  | 0.6410  | SCANS  | 30.00%  | 18.00%  | 82.00%  | 40.00%  | 0.4785
L311: LLM-VA  | 12.00%  | 6.00%  | 38.00%  | 0.00%  | 0.8526  | LLM-VA  | 46.00%  | 14.00%  | 56.00%  | 0.00%  | 0.7129
L312: To evaluate the effectiveness of LLM-VA on jailbreak and over-refusal trade-off, we compare it with magnitude-based vector steering methods across all 12 LLMs. Table cite115†2 presents ASR, ORR, and F1 scores on the test sets.
L313: #### Overall effectiveness of LLM-VA.
L314: 
L315: LLM-VA achieves an average F1 score of 0.77, representing a 37.02% relative improvement over the original LLMs (0.56). Notably, LLM-VA simultaneously reduces both failure modes: ASR decreases by 18.50% and ORR decreases by 22.00% on average compared to the original LLMs.
L316: #### Comparison with baselines.
L317: 
L318: LLM-VA outperforms all baselines on 8 of 12 LLMs regarding F1, with a relative improvement of 11.45% over the best baseline (AlphaSteer). VectorSteer, AlphaSteer+ and AlphaSteer, which only adjust answer vector magnitude, show limited improvement on models that already have low ASR but high ORR (e.g., Llama-3.1-8B). SCANS achieves competitive results on some models but requires architectural modifications and shows inconsistent performance across model families.
L319: #### Adaptive behavior.
L320: A key advantage of LLM-VA is its automatic adaptation to each model’s initial safety bias. For models with high ASR but low ORR (e.g., Mistral-v0.3-7B with 81% ASR and 29% ORR), LLM-VA primarily reduces ASR to ensure safety. Conversely, for models with low ASR but high ORR (e.g., Llama-3.1-8B with 7% ASR and 53% ORR), it primarily decreases ORR to enhance usability. This adaptive behavior emerges naturally from vector alignment without manual hyperparameter tuning for different models.
L321: #### Cases requiring further analysis.
L322: 
L323: Four models (Phi-3.5-4B, Phi-4-4B, Mistral-v0.3-7B, and Qwen3-14B) do not achieve the highest F1 with LLM-VA. We analyze these cases in Section cite41†5.4 and show that the suboptimal performance stems from iteration count sensitivity rather than fundamental limitations of the approach.
L324: ### 5.3 Utility Preservation Results (RQ2)
L325: 
L326: Figure 5: Left: Average utility preservation by method. Right: Utility preservation per LLM with LLM-VA. Values near 1.0 indicate minimal degradation.
L327: 
L328: Besides effectiveness in resolving trade-off, we also evaluate model utility preservation on 6 benchmark datasets covering classification and mathematical reasoning tasks. Figure cite116†5 shows the results across methods and models.
L329: #### Overall utility preservation.
L330: 
L331: LLM-VA preserves 95.92% of the original model’s utility on average, outperforming all baseline methods. For 9 of 12 LLMs, utility preservation exceeds 95%, demonstrating that LLM-VA successfully enhances alignment without sacrificing general capabilities.
L332: #### Comparison with baselines.
L333: 
L334: SCANS shows the largest utility degradation (averaging 40.98%) because aggressive magnitude adjustments disrupt the model’s internal representations. VectorSteer performs better (89.74%) but still falls short of LLM-VA due to its architectural modifications. AlphaSteer and AlphaSteer+ achieve competitive preservation (94.50% and 94.48%) through null-space projection, but LLM-VA still outperforms them while achieving substantially better alignment.
L335: #### Task-specific analysis.
L336: 
L337: The utility impact varies across task types. Classification tasks (COLA, MNLI, RTE, MRPC, SST) show minimal degradation, with most models preserving over 97% performance. Mathematical reasoning (GSM8K) is more affected, with 91.60% average preservation. This is expected because math reasoning requires precise logical chains that can be disrupted by representation changes. Nevertheless, the impact remains limited compared to the alignment gains.
L338: #### Model size effects.
L339: 
L340: Larger and more capable LLMs demonstrate better utility preservation. The three models with lowest preservation—Phi-3.5-4B (92.1%), Phi-4-4B (91.8%), and Mistral-v0.3-7B (93.2%)—are either among the smallest models or have documented limitations in benchmarks (cite117†Fourrier et al., 2024 ; cite118†Gao et al., 2021 ). This suggests that larger models have more robust internal representations that better tolerate the weight modifications introduced by vector alignment.
L341: ### 5.4 Ablation Studies (RQ3)
L342: 
L343: We analyze three key components: vector identification accuracy, iteration count, and layer selection.
L344: #### Vector Identification.
L345: 
L346: Figure 6: F1 scores with randomly distorted vectors at different angles $D$ from the original benign and answer vectors.
L347: To validate our SVM-based vector identification, we replace $v_{a}$ and $v_{b}$ with random vectors $D$ degrees away from the originals, where $D$ ranges from $30^{\circ}$ to $90^{\circ}$ (Figure cite119†6 ). The performance degradation correlates with distortion angle: at $D=90^{\circ}$ (orthogonal to the true vectors), F1 drops by 24.82% on average, and all 12 models underperform. At $D=60^{\circ}$, all models still show degradation.
L348: However, at $D=30^{\circ}$, F1 only drops by 5.40%, indicating that LLM-VA is robust to small inaccuracies—a practical advantage since SVM hyperplanes may not perfectly capture true decision boundaries—while confirming that accurate identification remains essential.
L349: #### Iteration Number.
L350: 
L351: (a) Llama 3.1 (8B)
L352: 
L353: (b) Phi 4 (4B)
L354: 
L355: (c) Qwen 3 (14B)
L356: 
L357: Figure 7: F1 scores vs. iteration number $T$ for three representative models.
L358: We vary iteration count $T$ from 1 to 30 (Figure cite120†7 ). For clarity, we show the results of three representative models and put the full results in Appendix cite63†F .
L359: Models exhibit distinct convergence patterns: Llama 3.1 (8B) shows rapid improvement and stabilizes around $T=19$; Phi 4 (4B) peaks at $T=19$ but then degrades with additional iterations, suggesting over-modification; Qwen 3 (14B) continues improving through $T=30$ and beyond (as shown in Figure cite120†7 , we extended to $T=60$ and observed continued gains).
L360: These patterns explain the suboptimal results in Table cite115†2 : Mistral-v0.3-7B, Phi-3.5-4B and Phi-4-4B suffer from over-modification (smaller and performance-limited models (cite117†Fourrier et al., 2024 ; cite118†Gao et al., 2021 ) are more susceptible to over-modification), while Qwen3-14B underperforms due to under-iteration. This suggests that model-specific iteration tuning or early stopping based on validation performance is important.
L361: #### Layer Selection.
L362: 
L363: Figure 8: Impact of $L_{select}$ on F1 (left) and utility (right).
L364: Figure cite121†8 shows F1 and utility as $L_{select}$ varies from 30 to 60. For alignment, most models exhibit a non-monotonic trend with an optimal $L_{select}$: too few layers limit effectiveness, while too many cause overfitting. For utility preservation, most models remain stable until $L_{select}$ exceeds a threshold, at which point early layers are modified and utility drops sharply.
L365: This confirms that later layers are more relevant to safety decisions while early layers are critical for general capabilities, motivating our contribution-score-based layer selection (Section cite16†4.2 ).
L366: ## 6 Conclusion
L367: In this work, we presented LLM-VA, a novel approach that simultaneously addresses jailbreak and over-refusal by aligning the answer vector with the benign vector through closed-form weight updates—making the model’s willingness to answer causally dependent on its safety judgment without requiring fine-tuning or architectural changes.
L368: Experiments on 12 widely used LLMs from 5 model families demonstrate a 11.45% F1 improvement over the best baseline while preserving 95.92% utility, and our ablation studies confirm the importance of accurate vector identification and model-specific hyperparameter tuning.
L369: ## 7 Limitations
L370: 
L371: #### Binary toxicity assumption.
L372: 
L373: We consider only binary classification (benign vs. toxic), whereas real-world toxicity is nuanced and multi-dimensional. Extending LLM-VA to multi-class or fine-grained toxicity classification remains future work.
L374: #### Model scale.
L375: 
L376: Our experiments cover models from 3B to 14B parameters. The effectiveness of LLM-VA on larger models (e.g., 70B+) remains to be validated, as these models may have different internal representations and require different hyperparameter settings.
L377: #### Training data dependency.
L378: 
L379: LLM-VA requires labeled benign/toxic samples to train the SVMs for vector identification. The quality and representativeness of this training data directly affect alignment performance, and obtaining such labels may not always be straightforward.
L380: #### Reasoning models.
L381: 
L382: Vector steering methods, including LLM-VA, are difficult to apply to LLMs with chain-of-thought reasoning. The control vectors must be identified after reasoning steps are generated, which is computationally expensive, and the randomness in reasoning makes accurate vector identification challenging.
L383: #### Model-specific tuning.
L384: 
L385: As shown in our ablation studies, optimal iteration count and layer selection vary across models. While LLM-VA uses validation-based selection, this requires tuning for a new model, limiting plug-and-play applicability.
L386: #### Transferability.
L387: 
L388: The performance of the existing vector steering methods, including LLM-VA, on unseen datasets varies depending on tasks and models (Appendix cite64†G ). This imply that current steering methods may need to treat different tasks or domains separately, and improving transferability remains future work.
L389: #### Static alignment.
L390: 
L391: The alignment is performed once and does not adapt to new threats or evolving definitions of harmful content. Periodic re-alignment may be needed as the threat landscape changes.
L392: #### Customized Trade-off.
L393: 
L394: LLM-VA aims to improve both jailbreak and over-refusal behavior simultaneously. However, in certain applications (e.g., healthcare (cite122†Al-Garadi et al., 2025 ; cite123†Yang et al., 2024b ) or PLC code generation (cite124†Liu et al., 2024d )), users may prefer to prioritize one aspect over the other. Extending LLM-VA to allow for customizable trade-offs remains future work.
L395: #### Experimental methodology.
L396: 
L397: Our results are based on single runs with a fixed random seed. While we observe consistent improvements across 12 models, incorporating statistical significance tests would further strengthen our empirical findings.
L398: 
L399: ## 8 Ethical Considerations
L400: ### 8.1 Potential Risks
L401: 
L402: Though LLM-VA aims to enhance the safety alignment of LLMs, it can be misused to manipulate model behaviors in unintended ways. For instance, attackers could potentially exploit the vector alignment technique to bypass safety mechanisms or introduce harmful biases into the model. Besides, the datasets used for training and evaluation may contain biases.
L403: ### 8.2 AI Assistants Usage
L404: 
L405: We employ GPT-5.2 (cite67†OpenAI, 2024 ) and Github Copilot^{8}^{8} 8 cite125†https://github.com/features/copilot†github.com to assist in writing code for experiments. We carefully review and verify all AI-generated content to ensure accuracy and integrity.
L406: ## References
L407:   * Abdin et al. (2024) M. Abdin, J. Aneja, H. Awadalla, A. Awadallah, A. A. Awan, N. Bach, A. Bahree, A. Bakhtiari, J. Bao, H. Behl, A. Benhaim, M. Bilenko, J. Bjorck, S. Bubeck, M. Cai, Q. Cai, V. Chaudhary, D. Chen, D. Chen, W. Chen, Y. Chen, Y. Chen, H. Cheng, P. Chopra, X. Dai, M. Dixon, R. Eldan, V. Fragoso, J. Gao, M. Gao, M. Gao, A. Garg, A. D. Giorno, A. Goswami, S. Gunasekar, E. Haider, J. Hao, R. J. Hewett, W. Hu, J. Huynh, D. Iter, S. A. Jacobs, M. Javaheripi, X. Jin, N. Karampatziakis, P.


## Original response: stdnext3tail1

LLM-VA: Resolving the Jailbreak-Overrefusal Trade-off via Vector Alignment (https://arxiv.org/html/2601.19487v1)
citeturn28416view0 [wordlim: 200] Crawled: yesterday; Content type: text/html; Source: open({"ref_id":"turn28405view3","lineno":550}); Total lines: 648
L443:   * Stiennon et al. (2020) N. Stiennon, L. Ouyang, J. Wu, D. Ziegler, R. Lowe, C. Voss, A. Radford, D. Amodei, and P. F. Christiano Learning to summarize with human feedback. Advances in neural information processing systems 33, pp. 3008–3021. Cited by: cite133†§2 .
L444:   * Team (2024a) G. Team Gemma. External Links: cite173†Link†www.kaggle.com , cite174†Document†dx.doi.org Cited by: cite127†§5.1 .
L445:   * Team (2024b) Q. Team Qwen2.5: a party of foundation models. External Links: cite175†Link†qwenlm.github.io Cited by: cite127†§5.1 .
L446:   * Team (2025) Q. Team Qwen3 technical report. External Links: 2505.09388, cite176†Link Cited by: cite129†§1 , cite127†§5.1 .
L447:   * Warstadt et al. (2018) A. Warstadt, A. Singh, and S. R. Bowman Neural network acceptability judgments. arXiv preprint 1805.12471. Cited by: cite177†1st item , cite135†§5.1 .
L448:   * Williams et al. (2018) A. Williams, N. Nangia, and S. Bowman A broad-coverage challenge corpus for sentence understanding through inference. In Proceedings of the 2018 conference of the North American chapter of the association for computational linguistics: human language technologies, volume 1 (long papers), pp. 1112–1122. Cited by: cite178†2nd item , cite135†§5.1 .
L449:   * Xhonneux et al. (2024) S. Xhonneux, A. Sordoni, S. Günnemann, G. Gidel, and L. Schwinn Efficient adversarial training in llms with continuous attacks. Advances in Neural Information Processing Systems 37, pp. 1502–1530. Cited by: cite133†§2 .
L450:   * Yang et al. (2024a) A. Yang, B. Yang, B. Hui, B. Zheng, B. Yu, C. Zhou, C. Li, C. Li, D. Liu, F. Huang, G. Dong, H. Wei, H. Lin, J. Tang, J. Wang, J. Yang, J. Tu, J. Zhang, J. Ma, J. Xu, J. Zhou, J. Bai, J. He, J. Lin, K. Dang, K. Lu, K. Chen, K. Yang, M. Li, M. Xue, N. Ni, P. Zhang, P. Wang, R. Peng, R. Men, R. Gao, R. Lin, S. Wang, S. Bai, S. Tan, T. Zhu, T. Li, T. Liu, W. Ge, X. Deng, X. Zhou, X. Ren, X. Zhang, X. Wei, X. Ren, Y. Fan, Y. Yao, Y. Zhang, Y. Wan, Y. Chu, Y. Liu, Z. Cui, Z.
L451: Zhang, and Z. Fan Qwen2 technical report. arXiv preprint arXiv:2407.10671. Cited by: cite127†§5.1 .
L452:   * Yang et al. (2024b) Y. Yang, Q. Jin, F. Huang, and Z. Lu Adversarial attacks on large language models in medicine. External Links: 2406.12259, cite179†Link Cited by: cite131†§7 .
L453:   * Yuan et al. (2025) X. Yuan, J. Li, D. Wang, Y. Chen, X. Mao, L. Huang, J. Chen, H. Xue, X. Liu, W. Wang, K. Ren, and J. Wang S-eval: towards automated and comprehensive safety evaluation for large language models. Proceedings of the ACM on Software Engineering 2 (ISSTA), pp. 2136–2157. External Links: cite180†Link†doi.org , cite181†Document†dx.doi.org Cited by: cite129†§1 , cite182†§3 , cite135†§5.1 .
L454:   * Zhang et al. (2025a) H. Zhang, D. Wang, Y. Liu, K. Chen, J. Wang, X. Ying, L. Liu, and W. Wang ORFuzz: fuzzing the "other side" of llm safety – testing over-refusal. External Links: 2508.11222, cite183†Link Cited by: cite142†Appendix E , cite129†§1 , cite182†§3 , cite135†§5.1 , cite184†§5.1 .
L455:   * Zhang et al. (2025b) S. Zhang, Y. Zhai, K. Guo, H. Hu, S. Guo, Z. Fang, L. Zhao, C. Shen, C. Wang, and Q. Wang Jbshield: defending large language models from jailbreak attacks through activated concept analysis and manipulation. arXiv preprint arXiv:2502.07557. Cited by: cite133†§2 .
L456:   * Zhao et al. (2025) H. Zhao, C. Yuan, F. Huang, X. Hu, Y. Zhang, A. Yang, B. Yu, D. Liu, J. Zhou, J. Lin, et al. Qwen3Guard technical report. arXiv preprint arXiv:2510.14276. Cited by: cite142†Appendix E , cite184†§5.1 .
L457:   * Zou et al. (2023a) A. Zou, L. Phan, S. Chen, J. Campbell, P. Guo, R. Ren, A. Pan, X. Yin, M. Mazeika, A. Dombrowski, et al. Representation engineering: a top-down approach to ai transparency. arXiv preprint arXiv:2310.01405. Cited by: cite129†§1 , cite185†§1 , cite133†§2 , cite136†§2 , cite150†§2 , cite182†§3 , cite138†§4.1 , cite169†§4.2 , cite139†§4.3 , cite186†1st item .
L458:   * Zou et al. (2023b) A. Zou, Z. Wang, J. Z. Kolter, and M. Fredrikson Universal and transferable adversarial attacks on aligned language models. External Links: 2307.15043 Cited by: cite146†Appendix G , cite184†§5.1 .
L459: ## Appendix A Angles between Answer Vectors and Benign Vectors
L460: 
L461: Llama 3.1 (8B)
L462: 
L463: gemma-2 (9B)
L464: 
L465: Mistral-v0.3 (7B)
L466: 
L467: Phi-3.5 (4B)
L468: 
L469: Phi-4 (4B)
L470: 
L471: Phi-4 (15B)
L472: 
L473: Qwen2.5 (3B)
L474: 
L475: Qwen2.5 (7B)
L476: 
L477: Qwen2.5 (14B)
L478: 
L479: Qwen3 (4B)
L480: 
L481: Qwen3 (8B)
L482: 
L483: Qwen3 (14B)
L484: 
L485: Figure 9: Angles between answer vectors and benign vectors of different LLMs.
L486: 
L487: As shown in Figure cite187†9 , the angles between the answer vectors and benign vectors of different LLMs are approximately $90^{\circ}$, indicating that they are nearly orthogonal.
L488: ## Appendix B Discussion on Layer Type Selection
L489: In Section cite16†4.2 , we mention that we treat both MLP and attention sublayers as “layers” for selection. This is because both types of sublayers contribute to the model’s internal representations and decision-making processes. Modifying either type can influence the model’s behavior regarding safety alignment. Besides, we conduct preliminary experiments to compare the combined score (Eq. cite188†6 ) distributions of MLP and attention sublayers. The results are presented in Figure cite189†10 .
L490: The results show that both MLP and attention sublayers exhibit similar contribution score distributions across different LLMs. Later layers tend to have higher contribution scores, indicating their greater relevance to safety-related decisions. Therefore, we treat both MLP and attention sublayers equally in our layer selection process.
L491: Llama-3.1 (8B)
L492: 
L493: gemma-2 (9B)
L494: 
L495: Mistral-v0.3 (7B)
L496: 
L497: Phi-3.5 (4B)
L498: 
L499: Phi-4 (4B)
L500: 
L501: Phi-4 (15B)
L502: 
L503: Qwen2.5 (3B)
L504: 
L505: Qwen2.5 (7B)
L506: 
L507: Qwen2.5 (14B)
L508: 
L509: Qwen3 (4B)
L510: 
L511: Qwen3 (8B)
L512: 
L513: Qwen3 (14B)
L514: 
L515: Figure 10: Comparison of combined scores between MLP and attention sublayers across different LLMs.
L516: ## Appendix C Additional Instructions on General Ability Datasets
L517: 
L518: In this section, we provide detailed instructions on the general ability datasets used in our experiments.
L519: 
L520:   * •
L521: 
L522: Corpus of Linguistic Acceptability (COLA) (cite107†Warstadt et al., 2018 ) is a dataset for evaluating the grammatical acceptability of sentences. Each sample consists of a sentence and a binary label indicating whether the sentence is grammatically acceptable or not.
L523: 
L524:   * •
L525: Multi-Genre Natural Language Inference (MNLI) (cite108†Williams et al., 2018 ) is a large-scale dataset for natural language inference. Each sample consists of a pair of sentences annotated with textual entailment labels.
L526: 
L527:   * •
L528: 
L529: Recognizing Textual Entailment (RTE) (cite109†Bentivogli et al., 2009 ) is a dataset for evaluating the ability of models to recognize textual entailment. Each sample consists of a pair of sentences where one sentence is the premise and the other is the hypothesis.
L530: 
L531:   * •
L532: Microsoft Research Paraphrase Corpus (MRPC) (cite110†Dolan and Brockett, 2005 ) is a dataset for evaluating the ability of models to recognize paraphrases. Each sample consists of a pair of sentences extracted from online news sources, with human annotations indicating whether each pair is semantically equivalent or not.
L533: 
L534:   * •
L535: Stanford Sentiment Treebank (SST) (cite111†Socher et al., 2013 ) is a dataset for sentiment analysis. Each sample consists of a sentence and a binary label indicating whether the sentiment of the sentence is positive or negative.
L536: 
L537:   * •
L538: 
L539: GSM8K (cite112†Cobbe et al., 2021 ) is a dataset for evaluating the mathematical reasoning ability of models. Each sample consists of a math word problem and its corresponding solution.
L540: ## Appendix D Details about Experimental Setup
L541: 
L542: Table 3: Selected layer numbers of different models in LLM-VA.
L543: 
L544: Model  | Llama-3.1  | Gemma-2  | Mistral-v0.3  | Phi-3.5  | Phi-4  | Qwen2.5  | Qwen3
L545: Size  | 8B  | 9B  | 7B  | 4B  | 4B  | 15B  | 3B  | 7B  | 14B  | 4B  | 8B  | 14B
L546: # Selected Layers  | 42  | 60  | 42  | 30  | 48  | 54  | 60  | 36  | 54  | 48  | 60  | 48
L547: We implement LLM-VA with max iteration number $T=30$. The final modified model is obtained by selecting the best model on the validation set during the iterations. The numbers of selected layers $L_{select}$ of each model are shown in Table cite190†3 . For the SVM-based vector identification, we use the default regularization parameter $C=1.0$ from scikit-learn (cite191†Pedregosa et al., 2011 ). For baseline methods, we follow the original papers and use the default hyperparameters.
L548: If the original papers do not provide hyperparameter settings for certain models, we transfer the hyperparameters from similar models (e.g., models with the same architecture or in the same family). All experiments are conducted on 2$\times$80 GB A100 GPUs. We use the default generation configurations in Hugging Face Transformers^{9}^{9} 9 cite192†https://huggingface.co/docs/transformers/index†huggingface.co for base LLMs during inference.
L549: The temperature parameters of all models are set to 0.0 to ensure deterministic outputs. We use a fixed random seed of 42 for reproducibility across all experiments.
L550: ## Appendix E Details on Judge Model Selection
L551: 
L552: Figure 11: An example of evaluation results with combined judge models.
L553: As far as we know, Qwen3-Guard-Gen-8B (cite114†Zhao et al., 2025 ) is currently the only open-source LLM specifically designed to evaluate jailbreak and over-refusal behaviors. We also considered combining multiple judge models to realize the evaluation (e.g., LlamaGuard 3 (cite193†Chi et al., 2024 ) for jailbreak and OR-Judge (cite75†Zhang et al., 2025a ) for over-refusal). However, due to their different judgement criteria, combining multiple judge models may lead to inconsistent evaluations.
L554: As a result, LLM-VA will find incorrect vectors to align, leading to suboptimal performance. Figure cite194†11 shows an example of such inconsistent evaluations. The ORR evaluated by OR-Judge reaches 100% due to the inconsistency between the two judge models. Therefore, we choose Qwen3-Guard-Gen-8B as the sole judge model for a consistent evaluation of both jailbreak and over-refusal behaviors.
L555: ## Appendix F Detailed Results on Iteration Number
L556: 
L557: The detailed results on the impact of iteration number of each LLM are shown in Figure cite195†12 .
L558: 
L559: gemma-2 (9B)
L560: 
L561: Mistral-v0.3 (7B)
L562: 
L563: Phi-3.5 (4B)
L564: 
L565: Phi-4 (15B)
L566: 
L567: Qwen2.5 (3B)
L568: 
L569: Qwen2.5 (7B)
L570: 
L571: Qwen2.5 (14B)
L572: 
L573: Qwen3 (4B)
L574: 
L575: Qwen3 (8B)
L576: 
L577: Figure 12: Detailed results on the impact of iteration number of each LLM.
L578: ## Appendix G Transferability Experiments
L579: To evaluate the transferability of LLM-VA, we assess how well the vector alignment learned on the training datasets generalizes to unseen datasets. We evaluate the modified models on three additional jailbreak datasets (XSTest-Toxic (cite74†Röttger et al., 2024 ), OR-Bench-Toxic (cite76†Cui et al., 2025 ), and AdvBench (cite113†Zou et al., 2023b )) and two over-refusal datasets (XSTest (cite74†Röttger et al., 2024 ) and OR-Bench (cite76†Cui et al., 2025 )) that are not included in the training set.
L580: The results are shown in Table cite196†4 .
L581: Table 4: Transferability results on unseen datasets.
L582: Model  | Size  | Method  | AdvBench
L583: ASR↓  | OR-Bench-Toxic
L584: ASR↓  | XSTest-Toxic
L585: ASR↓  | OR-Bench
L586: ORR↓  | XSTest
L587: ORR↓  | Final
L588: F1↑  | Model  | Size  | Method  | AdvBench
L589: ASR↓  | OR-Bench-Toxic
L590: ASR↓  | XSTest-Toxic
L591: ASR↓  | OR-Bench
L592: ORR↓  | XSTest
L593: ORR↓  | Final
L594: F1↑
L595: Llama-3.1  | 8B  | Original  | 0.58%  | 3.05%  | 0.00%  | 48.22%  | 16.57%  | 0.7077  | Qwen2.5  | 3B  | Original  | 0.19%  | 2.29%  | 0.57%  | 55.42%  | 19.34%  | 0.6522
L596: AlphaSteer+  | 0.58%  | 3.05%  | 0.00%  | 48.67%  | 17.13%  | 0.7038  | AlphaSteer+  | 0.00%  | 2.44%  | 0.00%  | 53.53%  | 21.55%  | 0.6649
L597: AlphaSteer  | 0.19%  | 1.37%  | 0.00%  | 61.87%  | 27.07%  | 0.5921  | AlphaSteer  | 0.19%  | 1.53%  | 0.00%  | 59.97%  | 21.55%  | 0.6144
L598: Steer  | 0.00%  | 0.15%  | 0.00%  | 85.60%  | 49.17%  | 0.3163  | Steer  | 0.00%  | 0.15%  | 0.00%  | 85.97%  | 37.57%  | 0.3313
L599: SCANS  | 0.19%  | 1.37%  | 0.00%  | 72.48%  | 26.52%  | 0.4945  | SCANS  | 6.35%  | 16.64%  | 1.15%  | 40.11%  | 13.81%  | 0.7305
L600: Modified  | 7.69%  | 5.80%  | 4.02%  | 46.85%  | 6.63%  | 0.7088  | Modified  | 0.38%  | 4.12%  | 0.57%  | 54.21%  | 21.55%  | 0.6555
L601: gemma-2  | 9B  | Original  | 0.58%  | 1.98%  | 0.00%  | 80.52%  | 28.73%  | 0.4059  | 7B  | Original  | 0.38%  | 6.72%  | 0.00%  | 24.64%  | 8.84%  | 0.8569
L602: AlphaSteer+  | 0.77%  | 0.92%  | 0.57%  | 81.58%  | 26.52%  | 0.3985  | AlphaSteer+  | 0.77%  | 6.11%  | 0.00%  | 24.87%  | 8.84%  | 0.8563
L603: AlphaSteer  | 0.00%  | 0.46%  | 0.00%  | 88.86%  | 28.73%  | 0.3103  | AlphaSteer  | 3.08%  | 3.66%  | 0.00%  | 34.50%  | 9.39%  | 0.8006
L604: Steer  | 0.00%  | 0.31%  | 0.00%  | 94.16%  | 56.35%  | 0.1882  | Steer  | 8.65%  | 5.50%  | 0.00%  | 61.03%  | 29.28%  | 0.5776
L605: SCANS  | 3.08%  | 5.50%  | 0.57%  | 59.82%  | 29.28%  | 0.5952  | SCANS  | 1.54%  | 6.87%  | 1.72%  | 40.56%  | 11.60%  | 0.7552
L606: Modified  | 2.88%  | 1.68%  | 0.00%  | 82.41%  | 29.83%  | 0.3809  | Modified  | 3.65%  | 9.92%  | 0.00%  | 19.94%  | 7.73%  | 0.8714
L607: Mistral-v0.3  | 7B  | Original  | 54.42%  | 48.70%  | 16.67%  | 7.28%  | 3.87%  | 0.7920  | 14B  | Original  | 0.00%  | 4.58%  | 0.00%  | 21.15%  | 8.29%  | 0.8816
L608: AlphaSteer+  | 52.12%  | 48.85%  | 16.67%  | 7.35%  | 4.42%  | 0.7937  | AlphaSteer+  | 0.19%  | 5.34%  | 0.00%  | 20.77%  | 8.29%  | 0.8817
L609: AlphaSteer  | 45.38%  | 48.09%  | 14.37%  | 7.66%  | 4.97%  | 0.8021  | AlphaSteer  | 0.00%  | 3.21%  | 0.00%  | 26.31%  | 9.39%  | 0.8551
L610: Steer  | 42.69%  | 40.92%  | 5.75%  | 11.75%  | 11.05%  | 0.7970  | Steer  | 0.00%  | 0.15%  | 0.00%  | 57.01%  | 16.02%  | 0.6477
L611: SCANS  | 74.42%  | 41.98%  | 22.99%  | 18.57%  | 7.73%  | 0.7209  | SCANS  | 7.88%  | 16.95%  | 2.30%  | 30.40%  | 19.34%  | 0.7824
L612: Modified  | 27.31%  | 17.25%  | 2.87%  | 37.30%  | 10.50%  | 0.7195  | Modified  | 0.77%  | 5.04%  | 0.00%  | 17.74%  | 6.08%  | 0.8990
L613: Phi-3.5  | 4B  | Original  | 2.12%  | 4.89%  | 1.72%  | 45.49%  | 13.26%  | 0.7234  | Qwen3  | 4B  | Original  | 0.96%  | 4.73%  | 0.57%  | 44.35%  | 6.63%  | 0.7402
L614: AlphaSteer+  | 1.15%  | 4.43%  | 1.15%  | 43.90%  | 13.81%  | 0.7365  | AlphaSteer+  | 7.88%  | 24.58%  | 4.02%  | 21.08%  | 4.42%  | 0.8307
L615: AlphaSteer  | 1.15%  | 3.66%  | 1.15%  | 48.98%  | 13.81%  | 0.7022  | AlphaSteer  | 33.85%  | 37.10%  | 8.62%  | 22.14%  | 7.73%  | 0.7634
L616: Steer  | 1.15%  | 3.51%  | 1.15%  | 56.41%  | 22.10%  | 0.6373  | Steer  | 0.77%  | 1.83%  | 0.00%  | 66.49%  | 19.89%  | 0.5583
L617: SCANS  | 1.54%  | 1.37%  | 1.15%  | 79.83%  | 37.57%  | 0.3994  | SCANS  | 3.65%  | 6.11%  | 0.57%  | 46.93%  | 11.60%  | 0.7107
L618: Modified  | 6.54%  | 6.41%  | 0.00%  | 43.21%  | 12.71%  | 0.7306  | Modified  | 2.31%  | 4.27%  | 0.57%  | 36.69%  | 7.73%  | 0.7880
L619: Phi-4  | 4B  | Original  | 0.58%  | 2.14%  | 0.00%  | 58.83%  | 17.68%  | 0.6265  | 8B  | Original  | 0.96%  | 3.21%  | 1.15%  | 44.12%  | 9.39%  | 0.7419
L620: AlphaSteer+  | 0.19%  | 1.53%  | 0.00%  | 59.97%  | 18.23%  | 0.6182  | AlphaSteer+  | 7.31%  | 14.20%  | 7.47%  | 62.70%  | 22.10%  | 0.5560
L621: AlphaSteer  | 0.19%  | 1.53%  | 0.00%  | 55.42%  | 18.23%  | 0.6551  | AlphaSteer  | 0.58%  | 4.89%  | 1.15%  | 34.65%  | 7.18%  | 0.8025
L622: Steer  | 0.19%  | 2.60%  | 0.00%  | 46.70%  | 16.57%  | 0.7201  | Steer  | 0.96%  | 4.12%  | 0.57%  | 40.03%  | 9.39%  | 0.7677
L623: SCANS  | 10.19%  | 12.98%  | 0.57%  | 36.01%  | 8.84%  | 0.7621  | SCANS  | 0.58%  | 2.29%  | 0.00%  | 70.96%  | 20.99%  | 0.5147
L624: Modified  | 0.58%  | 7.63%  | 1.15%  | 18.73%  | 11.60%  | 0.8841  | Modified  | 0.96%  | 3.82%  | 0.00%  | 40.71%  | 8.29%  | 0.7651
L625: 15B  | Original  | 0.19%  | 3.97%  | 0.00%  | 72.71%  | 17.13%  | 0.5007  | 14B  | Original  | 0.19%  | 4.43%  | 0.57%  | 40.33%  | 7.18%  | 0.7683
L626: AlphaSteer+  | 0.00%  | 3.97%  | 0.00%  | 72.63%  | 15.47%  | 0.5039  | AlphaSteer+  | 5.96%  | 22.44%  | 3.45%  | 13.65%  | 6.63%  | 0.8743
L627: AlphaSteer  | 0.00%  | 3.36%  | 0.00%  | 75.97%  | 16.57%  | 0.4704  | AlphaSteer  | 0.77%  | 12.21%  | 0.57%  | 20.09%  | 5.52%  | 0.8719
L628: Steer  | 0.00%  | 2.29%  | 0.00%  | 84.23%  | 20.99%  | 0.3762  | Steer  | 0.00%  | 0.31%  | 0.57%  | 72.33%  | 20.99%  | 0.5052
L629: SCANS  | 1.35%  | 5.95%  | 0.00%  | 67.78%  | 11.60%  | 0.5490  | SCANS  | 29.04%  | 26.11%  | 9.20%  | 35.94%  | 25.41%  | 0.6955
L630: Modified  | 0.77%  | 3.82%  | 0.00%  | 53.37%  | 11.60%  | 0.6727  | Modified  | 4.81%  | 3.05%  | 0.00%  | 51.86%  | 11.05%  | 0.6801
L631: The results show that the performance of LLM-VA on unseen datasets varies across different models. While LLM-VA maintains reasonable safety alignment on most unseen datasets, the performance degradation compared to the training datasets indicates that further research is needed to improve the generalization of vector steering methods.
L632: 
L633: Experimental support, please cite197†view the build logs for errors. Generated by cite198†L A T E xml†math.nist.gov .
L634: ## Instructions for reporting errors
L635: 
L636: We are continuing to improve HTML versions of papers, and your feedback helps enhance accessibility and mobile support. To report errors in the HTML that will help us improve conversion and rendering, choose any of the methods listed below:
L637: 
L638:   * Click the "Report Issue" () button, located in the page header.
L639: 
L640: Tip: You can select the relevant text first, to include it in your report.
L641: Our team has already identified cite199†the following issues†github.com . We appreciate your time reviewing and reporting rendering errors we may not have found yet. Your efforts will help us improve the HTML versions for all readers, because disability should not be a barrier to accessing research. Thank you for your continued support in championing open access for all.
L642: Have a free development cycle? Help support accessibility at arXiv! Our collaborators at LaTeXML maintain a cite200†list of packages that need conversion†github.com , and welcome cite201†developer contributions†github.com .
L643: 
L644: We gratefully acknowledge support from our major funders, cite202†member institutions†info.arxiv.org , , and all contributors.
L645: cite203†About†info.arxiv.org · cite204†Help†info.arxiv.org · cite205†Contact†info.arxiv.org · cite206†Subscribe†info.arxiv.org · cite207†Copyright†info.arxiv.org · cite208†Privacy†info.arxiv.org · cite209†Accessibility†info.arxiv.org · cite210†Operational Status (opens in new tab)†status.arxiv.org L646: 
L647: Major funding support from

