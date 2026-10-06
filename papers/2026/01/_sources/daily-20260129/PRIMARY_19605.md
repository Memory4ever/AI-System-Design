# Exact v1 primary: 2601.19605

Raw primary excerpts, grouped by original tool response; physical lines distinguish local L-number resets.

## Original response: jan29_stdnext4head

Decompose-and-Formalise: Recursively Verifiable Natural Language Inference (https://arxiv.org/html/2601.19605v1)
citeturn28434view2 [wordlim: 200] Crawled: 4 days ago; Content type: text/html; Source: open({"ref_id":"https://arxiv.org/html/2601.19605v1","lineno":null}); Total lines: 545


## Original response: jan29_stdnext4core

Decompose-and-Formalise: Recursively Verifiable Natural Language Inference (https://arxiv.org/html/2601.19605v1)
citeturn28435view2 [wordlim: 200] Crawled: 4 days ago; Content type: text/html; Source: open({"ref_id":"turn28434view2","lineno":135}); Total lines: 545
L122:  | $$D(p_{j})=\{a^{p_{j}}_{1},a^{p_{j}}_{2},\ldots,a^{p_{j}}_{t_{j}}\},\qquad p_{j}\equiv\bigwedge_{\ell=1}^{t_{j}}a^{p_{j}}_{\ell}.$$  |  | (2)
L123: 
L124: We define the global atom set induced by the premises as
L125: 
L126:  | $$D(P_{i}):=\bigcup_{j=1}^{n}D(p_{j}),\qquad P_{i}\equiv\bigwedge_{a\in D(P_{i})}a.$$  |  | (3)
L127: #### Entailment-preserving requirement.
L128: We require the decomposition operator $D(\cdot)$ to be entailment-preserving: for any sentence $\varphi$ and any atom $a\in D(\varphi)$, it must hold that $\varphi\vDash a$. Intuitively, each atom is a logically entailed consequence of the original sentence, so decomposition does not introduce new information that is not supported by the source. We obtain candidate atoms by prompting an LLM (see Appendix cite49†I ).
L129: To enforce the entailment-preserving requirement in practice, we apply a pretrained NLI classifier (roberta-large-mnli (cite69†Liu et al., 2019 )) to verify that each atom is entailed by its source sentence within a predefined threshold (0.9). This filtering step reduces invalid decompositions and improves the stability of downstream autoformalisation.
L130: Figure 2: $\theta$-substitution autoformalisation example.
L131: ### 3.3 $\theta$-substitution Autoformalisation
L132: Existing autoformalisation pipelines (cite58†Pan et al., 2023 ; cite59†Olausson et al., 2023 ) often rely on complex, monolithic generation procedures to map natural language sentences into fully specified logical formulas. This design is computationally inefficient and, more importantly, prone to systematic errors that frequently prevent theorem provers from certifying entailment.
L133: These observations motivate a more structured autoformalisation strategy that decomposes the translation into smaller, verifiable steps and reduces sensitivity to surface linguistic variation.
L134: We then adopt the Neo-Davidsonian event semantics formulation used in cite56†Quan et al. (2024) , where events and semantic roles (e.g., agent, patient) are represented explicitly in first-order logic to autoformalise the decomposed atomic propositions in previous step to logical forms. Building on this representation, we propose a multi-step $\theta$-substitution procedure that constructs the final logical form by progressively instantiating an abstract template (see Example cite70†2 ).
L135: A substitution $\theta$ is a mapping from placeholders to terms:
L136: 
L137:  | $$\theta=\{x_{1}\mapsto t_{1},\;x_{2}\mapsto t_{2},\;\ldots,\;x_{n}\mapsto t_{n}\}.$$  |  | (9)
L138: 
L139: Applying $\theta$ to a formula $\varphi$, denoted $\varphi[\theta]$, replaces each placeholder $x_{i}$ with its corresponding term $t_{i}$.
L140: 
L141: For a natural language sentence, we start from an abstract logical template and apply a sequence of substitutions:
L142:  | $$\varphi_{0}\xrightarrow{\theta_{1}}\varphi_{1}\xrightarrow{\theta_{2}}\varphi_{2}\xrightarrow{\theta_{3}}\varphi_{\text{final}}.$$  |  | (10)
L143: 
L144: Each substitution handles a specific aspect: 1) Entity substitution ($\theta_{1}$): maps generic predicates to specific entities 2) Event substitution ($\theta_{2}$): introduces event predicates and event structure. 3) Role substitution ($\theta_{3}$): adds Neo-Davidsonian semantic roles and their arguments.
L145: The final formula is obtained by composing the substitutions:
L146: 
L147:  | $$\varphi_{\text{final}}=\varphi_{0}[\theta_{1}\circ\theta_{2}\circ\theta_{3}].$$  |  | (11)
L148: 
L149: Example cite70†2 illustrates the resulting stepwise derivation in detail.
L150: ### 3.4 Entailment tree verification and refinement for recursively verifiable NLI
L151: Finally, given an entailment tree $\mathcal{T}$, we verify it recursively by turning each subtree into a set of local proof obligations that are checkable by a TP. Each node $n\in\mathcal{T}$ stores a natural language statement $s_{n}$, its atomic decomposition $D(n)=\{a_{n1},a_{n2},\dots,a_{n|D(n)|}\}$, and a role indicator $\rho(n)\in\{\textsc{explanation},\textsc{hypothesis}\}$ that is defined with respect to the current subtree under verification.
L152: For a subtree $\mathcal{T}_{\text{sub}}\subseteq\mathcal{T}$ with root $h=\mathrm{root}(\mathcal{T}_{\text{sub}})$ and leaf set $E=\mathrm{leaves}(\mathcal{T}_{\text{sub}})$, we set
L153:  | $$\rho(n)=\begin{cases}\textsc{explanation}&\text{if }n\in E,\\
L154: \textsc{hypothesis}&\text{if }n=h.\end{cases}$$  |  | (12)
L155: #### From atoms to axioms and lemmas.
L156: 
L157: Let $\Phi$ denote autoformalisation from natural language atoms to the target logic. For every explanation node $e\in E$, each atom $a\in D(e)$ is translated into an Isabelle/HOL (cite71†Nipkow et al., 2002 ) axiom (example in Appendix cite44†D ):
L158: 
L159:  | $$\text{axiom}(e,a):\ \Phi(a).$$  |  | (13)
L160: 
L161: Collecting all explanation atoms yields the axiom set
L162: 
L163:  | $$A(E)\ :=\ \bigcup_{e\in E}\ \{\Phi(a)\mid a\in D(e)\}.$$  |  | (14)
L164: For the hypothesis node $h$, each atom $a\in D(h)$ induces a local proof obligation:
L165: 
L166:  | $$\text{lemma}(h,a):\ A(E)\ \vdash\ \Phi(a).$$  |  | (15)
L167: 
L168: We accept $h$ as verified for the current subtree if $\mathit{TP}$ certifies $\text{lemma}(h,a)$ for all atoms $a\in D(h)$.
L169: #### Recursive verification with localized refinement.
L170: 
L171: The verification proceeds bottom-up. Intuitively, once a subtree root is verified, it can be treated as a support statement for its parent level. Algorithm cite72†1 summarises the procedure.
L172: When $TP$ cannot discharge a lemma $\text{lemma}(h,a)$ for some atom $a\in D(h)$, we extract diagnostics from the prover (e.g., the failed goal and relevant constraints) and use them to localise the failure to a small set of implicated explanation nodes $\widehat{E}$. We then prompt an LLM to refine only these implicated nodes, update the subtree accordingly, and re-check the same local obligations.
L173: This loop continues until all atoms in $D(h)$ are certified for the subtree root $h$, after which the verified root is promoted and the algorithm proceeds to higher levels. Repeating this process bottom-up yields a recursively verifiable proof certificate for the entire entailment tree.
L174: Dataset  | Approach  | GPT-4o  | GPT-5 nano  | Grok-4 fast  | Deepseek-V3.1  | Qwen3-max
L175: Init.  | Fin.  | Init.  | Fin.  | Init.  | Fin.  | Init.  | Fin.  | Init.  | Fin.
L176:  | Explanation-Refiner  | 53.28  | 63.93  | 46.72  | 59.84  | 45.08  | 52.46  | 50.82  | 62.30  | 55.74  | 68.85
L177:  | Faithful-Refiner  | 68.03  | 78.69  | 53.28  | 68.03  | 54.92  | 65.57  | 71.31  | 81.15  | 69.67  | 84.43
L178: FOLIO  | LLM-TP Tree  | 81.15  | 90.16 $\uparrow$26.23  | 66.39  | 81.15 $\uparrow$21.31  | 62.30  | 79.51 $\uparrow$27.05  | 83.61  | 92.62 $\uparrow$30.32  | 85.25  | 95.08 $\uparrow$26.23
L179:  | Explanation-Refiner  | 62.67  | 76.67  | 59.33  | 73.33  | 53.33  | 69.33  | 52.67  | 66.67  | 64.00  | 78.00
L180:  | Faithful-Refiner  | 80.00  | 86.67  | 72.00  | 84.67  | 60.00  | 78.67  | 83.33  | 90.67  | 84.00  | 91.33
L181: ProofWriter  | LLM-TP Tree  | 91.33  | 95.33 $\uparrow$18.66  | 85.33  | 91.33 $\uparrow$18.00  | 72.67  | 90.00 $\uparrow$20.67  | 91.33  | 98.00 $\uparrow$31.33  | 92.00  | 98.00 $\uparrow$20.00
L182:  | Explanation-Refiner  | 64.00  | 78.67  | 60.00  | 74.67  | 61.33  | 73.33  | 62.00  | 74.00  | 64.67  | 78.00
L183:  | Faithful-Refiner  | 82.67  | 90.00  | 73.33  | 80.00  | 72.00  | 84.00  | 85.33  | 91.33  | 82.00  | 91.33
L184: PrOntoQA  | LLM-TP Tree  | 92.00  | 97.33 $\uparrow$18.66  | 93.33  | 98.00 $\uparrow$23.33  | 86.00  | 91.33 $\uparrow$18.00  | 97.33  | 100.00 $\uparrow$26.00  | 98.00  | 100.00 $\uparrow$22.00
L185:  | Explanation-Refiner  | 15.33  | 26.67  | 12.00  | 23.33  | 8.67  | 13.33  | 15.33  | 26.67  | 16.67  | 28.00
L186:  | Faithful-Refiner  | 23.33  | 44.00  | 17.33  | 47.33  | 14.00  | 46.00  | 25.33  | 48.00  | 22.00  | 52.00


## Original response: jan29_stdnext4eval

Decompose-and-Formalise: Recursively Verifiable Natural Language Inference (https://arxiv.org/html/2601.19605v1)
citeturn28436view2 [wordlim: 200] Crawled: 4 days ago; Content type: text/html; Source: open({"ref_id":"turn28434view2","lineno":190}); Total lines: 545
L174: Dataset  | Approach  | GPT-4o  | GPT-5 nano  | Grok-4 fast  | Deepseek-V3.1  | Qwen3-max
L175: Init.  | Fin.  | Init.  | Fin.  | Init.  | Fin.  | Init.  | Fin.  | Init.  | Fin.
L176:  | Explanation-Refiner  | 53.28  | 63.93  | 46.72  | 59.84  | 45.08  | 52.46  | 50.82  | 62.30  | 55.74  | 68.85
L177:  | Faithful-Refiner  | 68.03  | 78.69  | 53.28  | 68.03  | 54.92  | 65.57  | 71.31  | 81.15  | 69.67  | 84.43
L178: FOLIO  | LLM-TP Tree  | 81.15  | 90.16 $\uparrow$26.23  | 66.39  | 81.15 $\uparrow$21.31  | 62.30  | 79.51 $\uparrow$27.05  | 83.61  | 92.62 $\uparrow$30.32  | 85.25  | 95.08 $\uparrow$26.23
L179:  | Explanation-Refiner  | 62.67  | 76.67  | 59.33  | 73.33  | 53.33  | 69.33  | 52.67  | 66.67  | 64.00  | 78.00
L180:  | Faithful-Refiner  | 80.00  | 86.67  | 72.00  | 84.67  | 60.00  | 78.67  | 83.33  | 90.67  | 84.00  | 91.33
L181: ProofWriter  | LLM-TP Tree  | 91.33  | 95.33 $\uparrow$18.66  | 85.33  | 91.33 $\uparrow$18.00  | 72.67  | 90.00 $\uparrow$20.67  | 91.33  | 98.00 $\uparrow$31.33  | 92.00  | 98.00 $\uparrow$20.00
L182:  | Explanation-Refiner  | 64.00  | 78.67  | 60.00  | 74.67  | 61.33  | 73.33  | 62.00  | 74.00  | 64.67  | 78.00
L183:  | Faithful-Refiner  | 82.67  | 90.00  | 73.33  | 80.00  | 72.00  | 84.00  | 85.33  | 91.33  | 82.00  | 91.33
L184: PrOntoQA  | LLM-TP Tree  | 92.00  | 97.33 $\uparrow$18.66  | 93.33  | 98.00 $\uparrow$23.33  | 86.00  | 91.33 $\uparrow$18.00  | 97.33  | 100.00 $\uparrow$26.00  | 98.00  | 100.00 $\uparrow$22.00
L185:  | Explanation-Refiner  | 15.33  | 26.67  | 12.00  | 23.33  | 8.67  | 13.33  | 15.33  | 26.67  | 16.67  | 28.00
L186:  | Faithful-Refiner  | 23.33  | 44.00  | 17.33  | 47.33  | 14.00  | 46.00  | 25.33  | 48.00  | 22.00  | 52.00
L187: EntailmentBank  | LLM-TP Tree  | 21.33  | 70.00 $\uparrow$43.33  | 18.00  | 74.00 $\uparrow$50.67  | 16.67  | 68.67 $\uparrow$55.34  | 22.00  | 71.33 $\uparrow$44.66  | 22.67  | 78.67 $\uparrow$50.67
L188: Table 1: Comparison results on the explanation refinement tasks. Init. shows the number of explanation that is initially logically valid. Fin. shows the number of explanation that is finally logically valid after refinement. Bold values indicate the best performance. Arrows indicate absolute performance gain of LLM-TP Tree over the baseline.
L189: ## 4 Experimental Setup
L190: 
L191: We evaluate our neuro-symbolic framework from two complementary perspectives: (i) explanation refinement apply theorem-prover checking and refine the explanation; and (ii) logical reasoning, which measures standard end-task accuracy to ensure that enhanced verification and refinement do not come at the cost of predictive performance.
L192: #### Datasets
L193: 
L194: We use four datasets ranging from synthetically generated deductive reasoning benchmarks to expert-written real-world corpora: ProofWriter (cite73†Tafjord et al., 2021 ), PrOntoQA (cite74†Saparov and He, 2023 ), FOLIO (cite75†Han et al., 2024 ), and EntailmentBank (cite76†Dalvi et al., 2021 ). Additional dataset details (i.e. number of samples) are provided in Appendix cite28†A .
L195: #### Baselines and Models
L196: For explanation refinement, we compare against two state-of-the-art explanation refinement models, Explanation-Refiner (cite56†Quan et al., 2024 ) and Faithful-Refiner (cite66†Quan et al., 2025b ). For logical reasoning, we consider two prompting-based baselines, including a direct standard prompting and chain-of-thought (CoT) prompting. In addition, we compare against two representative neuro-symbolic frameworks, Logic-LM (cite58†Pan et al., 2023 ) and LINC (cite59†Olausson et al., 2023 ).
L197: We evaluate five distinct LLM backbones, spanning a general-purpose chat model (GPT-4o (cite77†OpenAI, 2024 )), models evaluated in non-thinking mode (GPT-5 Nano (cite78†OpenAI, 2025 ), Grok-4 Fast (cite79†xAI, 2025 )), and models evaluated in thinking mode (DeepSeek-V3.1 (cite80†Deepseek-AI, 2025 ), Qwen3-Max (cite81†Qwen Team, 2025 )) and additionally include GPT-3.5 in logical reasoning tasks to match the model coverage reported in prior work. LLM implementation details is described in Appendix cite44†D .
L198: ## 5 Empirical Results and Evaluation
L199: 
L200: Dataset  | ER  | FR  | LT  | LT w/o AD
L201: FOLIO  | 4.27  | 3.75  | 3.04  | 3.57
L202: ProofWriter  | 3.47  | 3.08  | 2.42  | 2.88
L203: PrOntoQA  | 3.36  | 2.73  | 2.04  | 2.44
L204: EntailmentBank  | 4.97  | 4.46  | 4.04  | 4.35
L205: Avg.  | 4.02  | 3.51  | 2.88  | 3.31
L206: Table 2: Average refinement iterations required averaged over five LLM backbones. Comparison between ER (Explanation-Refiner), FR (Faithful-Refiner), LT (LLM-TP Tree) and LT w/o AD (LT without atomic decomposition)
L207: #### LLM-TP Tree effectively verifies and refines explanations for NLI.
L208: Table cite82†1 reports the main results on the explanation refinement task. Across all datasets and all LLM backbones, LLM-TP Tree achieves the best final refinement performance (Fin.), indicating that it is consistently more effective at producing a checkable witness for explanation-based NLI. Averaged over backbone LLMs, LLM-TP Tree improves the final verified rate by 26.23%, 21.73%, 21.60%, and 48.93% on each dataset compared to Explanation-Refiner.
L209: The effect is most pronounced on EntailmentBank: while holistic refiners remain below 52% final validity, LLM-TP Tree reaches 68.67–78.67% across backbones. Beyond final refinement quality, the Init. column probes whether a backbone can produce an initially provable explanatory chain before any refinement cycle.
L210: On synthetic benchmarks such as ProofWriter and PrOntoQA, LLM-TP Tree yields substantially higher initial validity than holistic refiners; for instance, on ProofWriter with Qwen3-max, LLM-TP Tree attains 92.00% Init. versus 64.00% for Explanation-Refiner. Notably, EntailmentBank exhibits low initial validity across methods, suggesting that constructing globally coherent verifiable chains is difficult under more realistic multi-hop explanations.
L211: In this regime, our proposed mechanism yields the largest gains after refinement.
L212: (a) FOLIO
L213: 
L214: (b) ProofWriter
L215: 
L216: (c) PrOntoQA
L217: 
L218: (d) EntailmentBank
L219: 
L220: Figure 3: Distribution of the autoformlisation errors (syntax, implication, quantifier, variable in Isabelle/HOL Theories.
L221: #### Atomic decomposition improves the efficiency of verification-driven explanation refinement.
L222: We report the average number of refinement iterations, averaged across different LLM backbones, required to refine an explanation for each dataset, as shown in Table cite83†2 . Across all four datasets (FOLIO, ProofWriter, PrOntoQA, and EntailmentBank), LT converges in fewer iterations than baseline refiners, reducing the required iterations by an average of 1.14 relative to ER and by an average of 0.63 relative to Faithful-Refiner (FR).
L223: To isolate the advantages of atomic decomposition, we run an ablation that disables atomic sentence splitting. Relative to the full LT system, removing atomic decomposition increases the number of required refinement iterations by between 0.31 and 0.53 .
L224: This ablation indicates that atomic decomposition contributes materially to LT’s efficiency gains: by splitting premises and intermediate conclusions into atomic subclaims, verification failures can be localised to a small set of fine-grained hypotheses, enabling targeted repairs of the minimal logical mismatch and thereby reducing both the number of refinement iterations and the cost of each verification/refinement pass.


## Original response: jan29_stdnext4tail

Decompose-and-Formalise: Recursively Verifiable Natural Language Inference (https://arxiv.org/html/2601.19605v1)
citeturn28437view2 [wordlim: 200] Crawled: 4 days ago; Content type: text/html; Source: open({"ref_id":"turn28434view2","lineno":225}); Total lines: 545
L221: #### Atomic decomposition improves the efficiency of verification-driven explanation refinement.
L222: We report the average number of refinement iterations, averaged across different LLM backbones, required to refine an explanation for each dataset, as shown in Table cite83†2 . Across all four datasets (FOLIO, ProofWriter, PrOntoQA, and EntailmentBank), LT converges in fewer iterations than baseline refiners, reducing the required iterations by an average of 1.14 relative to ER and by an average of 0.63 relative to Faithful-Refiner (FR).
L223: To isolate the advantages of atomic decomposition, we run an ablation that disables atomic sentence splitting. Relative to the full LT system, removing atomic decomposition increases the number of required refinement iterations by between 0.31 and 0.53 .
L224: This ablation indicates that atomic decomposition contributes materially to LT’s efficiency gains: by splitting premises and intermediate conclusions into atomic subclaims, verification failures can be localised to a small set of fine-grained hypotheses, enabling targeted repairs of the minimal logical mismatch and thereby reducing both the number of refinement iterations and the cost of each verification/refinement pass.
L225: We also report the mean running time per refinement iteration (including theorem-proving time) under different LLM backbones, and provide the full per-backbone iteration results in Appendix cite46†F .
L226: Dataset  | ER  | FR  | LT  | LT w/o sub.
L227: FOLIO  | 0.766  | 0.822  | 0.856  | 0.828
L228: ProofWriter  | 0.834  | 0.892  | 0.940  | 0.914
L229: PrOntoQA  | 0.824  | 0.918  | 0.952  | 0.924
L230: EntailmentBank  | 0.614  | 0.726  | 0.824  | 0.770
L231: Avg.  | 0.760  | 0.840  | 0.893  | 0.859
L232: Table 3: Average autoformalisation faithfulness (cosine similarity) averaged over five LLM backbones. Comparison between ER (Explanation-Refiner), FR (Faithful-Refiner), LT (LLM-TP Tree) and LT w/o sub. (LT without $\theta$-substitution autoformalisation).
L233: #### Multi-step $\theta$-substitution autoformalisation improves semantic faithfulness.
L234: A faithful autoformalisation should preserve the semantic content of the original sentence as much as possible. Following the rule-based informalisation procedure by cite66†Quan et al. (2025b) , we quantify faithfulness by converting each predicted logical form back into natural language and computing the cosine similarity between the informalised sentence and the original sentence. Table cite84†3 summarises the results.
L235: Our approach achieves the highest average faithfulness across all datasets, outperforming Explanation-Refiner by an average of 0.13 and Faithful-Refiner by an average of 0.053. As expected, faithfulness is generally higher on synthetic benchmarks, whose language more closely follows rule-based templates, whereas EntailmentBank is more challenging due to its more naturalistic multi-hop explanations.
L236: Notably, our method yields the largest margin on EntailmentBank, indicating stronger robustness of $\theta$-substitution autoformalisation under distributional and linguistic variability. We further perform an ablation by removing $\theta$-substitution (LT w/o sub.). This variant shows a consistent drop in similarity of an average of 0.034 across the same datasets compared to the full model. We also shows the full ablation study results in Appendix cite45†E L237: ### 5.1 Failure and Error Analysis
L238: 
L239: (a) ProofWriter - Refined
L240: 
L241: (b) EntailmentBank - Refined
L242: 
L243: (c) ProofWriter - Unrefined
L244: 
L245: (d) EntailmentBank - Unrefined
L246: 
L247: Figure 4: Proof depth alignment between gold and actual constructed proof depths across frameworks. The solid curve shows the mean used depth averaged over five LLMs, while the shaded band shows the range across backbones. Top: Trends in refined cases. Bottom: Trends in unrefined cases.
L248: 
L249: (a) FOLIO
L250: 
L251: (b) ProofWriter
L252: 
L253: (c) PrOntoQA
L254: Figure 5: Comparison on the logical reasoning accuracy tasks.
L255: We analyse refinement drift using proof-depth alignment. Figure  cite85†4 measure proof-depth alignment by comparing the TP-extracted used proof depth of each explanation with the dataset-provided gold depth (ideal $y{=}x$). In refined cases, all frameworks show a positive trend that is close to the ideal $y{=}x$ line.

## Original response: jan29_stdnext4tail

Decompose-and-Formalise: Recursively Verifiable Natural Language Inference (https://arxiv.org/html/2601.19605v1)
citeturn28437view3 [wordlim: 200] Crawled: 4 days ago; Content type: text/html; Source: find({"ref_id":"turn28434view2","pattern":"Appendix D"}); Total lines: 545
L290:   * Quan et al. (2025a) X. Quan, M. Valentino, D. Carvalho, D. Dalal, and A. Freitas PEIRCE: unifying material and formal reasoning via LLM-driven neuro-symbolic refinement. In Proceedings of the 63rd Annual Meeting of the Association for Computational Linguistics (Volume 3: System Demonstrations), P. Mishra, S. Muresan, and T. Yu (Eds.), Vienna, Austria, pp. 11–21. External Links: cite115†Link†aclanthology.org , cite116†Document†dx.doi.org , ISBN 979-8-89176-253-4 Cited by: cite99†§1 , cite108†§6 .
L291:   * Quan et al. (2024) X. Quan, M. Valentino, L. A. Dennis, and A. Freitas Verification and refinement of natural language explanations through LLM-symbolic theorem proving. In Proceedings of the 2024 Conference on Empirical Methods in Natural Language Processing, Y. Al-Onaizan, M. Bansal, and Y. Chen (Eds.), Miami, Florida, USA, pp. 2933–2958. External Links: cite117†Link†aclanthology.org , cite118†Document†dx.doi.org Cited by: cite99†§1 , cite106†§1 , cite119†§3.3 , cite93†§4 .
L292:   * Quan et al. (2025b) X. Quan, M. Valentino, L. A. Dennis, and A. Freitas Faithful and robust LLM-driven theorem proving for NLI explanations. In Proceedings of the 63rd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers), W. Che, J. Nabende, E. Shutova, and M. T. Pilehvar (Eds.), Vienna, Austria, pp. 17734–17755.
L293: External Links: cite120†Link†aclanthology.org , cite121†Document†dx.doi.org , ISBN 979-8-89176-251-0 Cited by: cite122†Appendix B , cite123†Appendix D , cite99†§1 , cite100†§1 , cite106†§1 , cite124†§3.2 , cite93†§4 , cite125†§5 .
L294:   * Qwen Team (2025) Qwen Team Qwen3 technical report. External Links: 2505.09388, cite126†Link Cited by: cite93†§4 .
L295:   * Sadeddine and Suchanek (2025) Z. Sadeddine and F. M. Suchanek Verifying the steps of deductive reasoning chains. In Findings of the Association for Computational Linguistics: ACL 2025, W. Che, J. Nabende, E. Shutova, and M. T. Pilehvar (Eds.), Vienna, Austria, pp. 456–475. External Links: cite127†Link†aclanthology.org , cite128†Document†dx.doi.org , ISBN 979-8-89176-256-5 Cited by: cite99†§1 .
L296:   * Saparov and He (2023) A. Saparov and H. He Language models are greedy reasoners: a systematic formal analysis of chain-of-thought. In The Eleventh International Conference on Learning Representations, External Links: cite129†Link†openreview.net Cited by: cite113†§A.1 , cite91†§4 .
L297:   * Shminke (2022) B. Shminke Python client for isabelle server. External Links: 2212.11173, cite130†Link Cited by: cite131†Appendix D .
L298:   * Srikanth and Rudinger (2025) N. Srikanth and R. Rudinger NLI under the microscope: what atomic hypothesis decomposition reveals. In Proceedings of the 2025 Conference of the Nations of the Americas Chapter of the Association for Computational Linguistics: Human Language Technologies (Volume 1: Long Papers), L. Chiruzzo, A. Ritter, and L. Wang (Eds.), Albuquerque, New Mexico, pp. 2574–2589.
L299: External Links: cite132†Link†aclanthology.org , cite133†Document†dx.doi.org , ISBN 979-8-89176-189-6 Cited by: cite134†Appendix I .
L300:   * Tafjord et al. (2021) O. Tafjord, B. Dalvi, and P. Clark ProofWriter: generating implications, proofs, and abductive statements over natural language. In Findings of the Association for Computational Linguistics: ACL-IJCNLP 2021, C. Zong, F. Xia, W. Li, and R. Navigli (Eds.), Online, pp. 3621–3634. External Links: cite135†Link†aclanthology.org , cite136†Document†dx.doi.org Cited by: cite137†§A.1 , cite91†§4 .
L301:   * Valentino and Freitas (2024) M. Valentino and A. Freitas On the nature of explanation: an epistemological-linguistic perspective for explanation-based natural language inference. Philosophy & Technology 37 (3), pp. 88. Cited by: cite99†§1 .
L302:   * Valentino et al. (2021) M. Valentino, I. Pratt-Hartman, and A. Freitas Do natural language explanations represent valid logical arguments? verifying entailment in explainable nli gold standards. IWCS 2021, pp. 76. Cited by: cite99†§1 .
L303:   * Weber et al. (2019) L. Weber, P. Minervini, J. Münchmeyer, U. Leser, and T. Rocktäschel NLProlog: reasoning with weak unification for question answering in natural language. In Proceedings of the 57th Annual Meeting of the Association for Computational Linguistics, A. Korhonen, D. Traum, and L. Màrquez (Eds.), Florence, Italy, pp. 6151–6161. External Links: cite138†Link†aclanthology.org , cite139†Document†dx.doi.org Cited by: cite108†§6 .
L304:   * Wu et al. (2022) Y. Wu, A. Q. Jiang, W. Li, M. Rabe, C. Staats, M. Jamnik, and C. Szegedy Autoformalization with large language models. In Advances in Neural Information Processing Systems, S. Koyejo, S. Mohamed, A. Agarwal, D. Belgrave, K. Cho, and A. Oh (Eds.), Vol. 35, pp. 32353–32368. External Links: cite140†Link†proceedings.neurips.cc Cited by: cite99†§1 .
L305:   * xAI (2025) xAI Grok 4. Note: cite141†https://x.ai/news/grok-4†x.ai Cited by: cite93†§4 .
L306:   * Xu et al. (2025a) J. Xu, H. Fei, M. Luo, Q. Liu, L. Pan, W. Y. Wang, P. Nakov, M. Lee, and W. Hsu Aristotle: mastering logical reasoning with a logic-complete decompose-search-resolve framework. In Proceedings of the 63rd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers), W. Che, J. Nabende, E. Shutova, and M. T. Pilehvar (Eds.), Vienna, Austria, pp. 3052–3075.
L307: External Links: cite142†Link†aclanthology.org , cite143†Document†dx.doi.org , ISBN 979-8-89176-251-0 Cited by: cite108†§6 .
L308:   * Xu et al. (2024) J. Xu, H. Fei, L. Pan, Q. Liu, M. Lee, and W. Hsu Faithful logical reasoning via symbolic chain-of-thought. In Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers), L. Ku, A. Martins, and V. Srikumar (Eds.), Bangkok, Thailand, pp. 13326–13365. External Links: cite144†Link†aclanthology.org , cite145†Document†dx.doi.org Cited by: cite99†§1 .
L352: ## Appendix C Algorithm
L353: 
L354: Algorithm 1 VerifySubtree$(\mathcal{T}_{\text{sub}},\mathit{TP})$
L355: 
L356: 1:  $h\leftarrow\mathrm{root}(\mathcal{T}_{\text{sub}})$ {current hypothesis node}
L357: 
L358: 2:  $E\leftarrow\mathrm{leaves}(\mathcal{T}_{\text{sub}})$ {current explanation nodes}
L359: 
L360: 3:  Construct $A(E)=\bigcup_{e\in E}\{\Phi(a)\mid a\in D(e)\}$ {axioms}
L361: 
L362: 4:  for each atom $a\in D(h)$ do
L363: 
L364: 5:   Define the goal $\tau\leftarrow\Phi(a)$
L365: 
L366: 6:   if $\mathit{TP}.\mathrm{prove}\big(A(E)\vdash\tau\big)=\textsc{fail}$ then
L367: 7:    $\mathrm{diag}\leftarrow\mathit{TP}.\mathrm{diagnostics}()$
L368: 
L369: 8:    Identify implicated explanation nodes $\widehat{E}\subseteq E$ from $\mathrm{diag}$
L370: 
L371: 9:    Refine $\widehat{E}$ using an LLM conditioned on $(\widehat{E},\mathrm{diag})$
L372: 
L373: 10:    Update $\mathcal{T}_{\text{sub}}$; recompute $D(\cdot)$ and re-autoformalise $\Phi(\cdot)$
L374: 
L375: 11:    return VerifySubtree$(\mathcal{T}_{\text{sub}},\mathit{TP})$ {retry locally}
L376: 
L377: 12:   end if
L378: 
L379: 13:  end for
L380: 
L381: 14:  Mark $h$ as verified
L382: 15:  return $h$ {promote as support for parent level}
L383: ## Appendix D Isabelle/HOL and LLMs Implementation Detail
L384: We use the isabelle-client Python package (cite150†Shminke, 2022 ) to run Isabelle/HOL as a real-time server and to retrieve prover responses. We access all LLM backbones via API calls with the following model versions: GPT-4o (gpt-4o), GPT-5 nano (gpt-5-nano), Grok-4 fast (grok-4-fast), Deepseek-V3.1 (DeepSeek-v3.1-terminus), and Qwen3-Max (qwen3-max-preview). For all non-thinking models, we set the temperature to 0. We also do not limit any thinking effort for Deepseek-V3.1 and Qwen3-Max.
L385: We build the Isabelle/HOL theory following the approach in (cite66†Quan et al., 2025b ). An example of the constructed Isabelle/HOL theory is shown in Figure cite151†6 . We then apply atomic decomposition to each axiom and to the hypothesis. The decomposed hypothesis sentence and the decomposed axioms are then forming a new theory, which we use to prove theorems from each decomposed hypothesis atoms.
L386: 
L387: ⬇
L388: 
L389: theory data_0
L390: 
L391: imports Main
L392: 
L393: begin
L394: 
L395: typedecl entity
L396: 
L397: typedecl event
L398: 
L399: consts
L400: Melting :: "event $\Rightarrow$ bool"
L401: 
L402: Change :: "event $\Rightarrow$ bool"
L403: 
L404: Source :: "event $\Rightarrow$ entity $\Rightarrow$ bool"
L405: 
L406: Destination :: "event $\Rightarrow$ entity $\Rightarrow$ bool"
L407: 
L408: Solid :: "entity $\Rightarrow$ bool"
L409: 
L410: Liquid :: "entity $\Rightarrow$ bool"
L411: 
L412: IncreaseHeatEnergy :: "entity $\Rightarrow$ bool"
L413: 
L414: By :: "event $\Rightarrow$ entity $\Rightarrow$ bool"
L415: 
L416: Chocolate :: "entity $\Rightarrow$ bool"
L417: 
L418: Melts :: "event $\Rightarrow$ bool"
L419: Agent :: "event $\Rightarrow$ entity $\Rightarrow$ bool"
L420: 
L421: In :: "event $\Rightarrow$ entity $\Rightarrow$ bool"
L422: 
L423: Sunlight :: "entity $\Rightarrow$ bool"
L424: 
L425: (* Explanation 1: melting means changing from a solid to a liquid by increasing heat energy *)
L426: 
L427: axiomatization where
L428: 
L429: explanation_1: "$\forall$ e x y z. Melting e $\leftrightarrow$ (Change e $\wedge$ Source e x $\wedge$ Destination e y $\wedge$ Solid x $\wedge$ Liquid y $\wedge$ IncreaseHeatEnergy z $\wedge$ By e z)"
L430: (* Explanation 2: chocolate melts in the sunlight *)
L431: 
L432: axiomatization where
L433: 
L434: explanation_2: "$\exists$ x e. Chocolate x $\wedge$ Melts e $\wedge$ Agent e x $\wedge$ In e Sunlight"
L435: 
L436: theorem hypothesis:
L437: 
L438: assumes asm: "Chocolate x $\wedge$ Solid y $\wedge$ Liquid z"
L439: 
L440: (* Hypothesis: chocolate changes from a solid to a liquid in the sunlight *)
L441: 
L442: shows False
L443: 
L444: sledgehammer
L445: 
L446: oops
L447: 
L448: end
L449: 
L450: Figure 6: An example of the constructed Isabelle/HOL Theory.

## Original response: jan29_stdnext4tail

Decompose-and-Formalise: Recursively Verifiable Natural Language Inference (https://arxiv.org/html/2601.19605v1)
citeturn28437view4 [wordlim: 200] Crawled: 4 days ago; Content type: text/html; Source: find({"ref_id":"turn28434view2","pattern":"Limitations"}); Total lines: 545
L267: (2023)】 and cite59†Olausson et al. (2023) autoformalise natural-language contexts into symbolic representations and then apply external solvers to perform deductive reasoning over the resulting formal structures. Along a related direction, cite89†Xu et al. (2025a) proposes a decompose-search-resolve framework that breaks a problem into smaller logical substructures and performs structured search to resolve each reasoning step. Prover feedback has also been used to improve reliability: cite60†Quan et al.
L268: (2025a) extracts erroneous proof steps from solver feedback and iteratively refines reasoning in a loop. In contrast to endpoint-focused verification, our work targets recursively verifiable NLI by enforcing chain-level checking and localised refinement over structured entailment trees.
L269: ## 7 Conclusion
L270: We presented LLM-TP Tree, a neuro-symbolic framework for recursively verifiable NLI that follows a decompose-and-formalise paradigm. By combining entailment-tree verification with entailment-preserving atomic decomposition and $\theta$-substitution autoformalisation, our method enables localised, refinement that targets the implicated part of an explanation rather than regenerating it holistically.
L271: Experiments on four datasets with multiple LLM backbones show improved TP-verified explanation rates, more faithful autoformalisation, and reduced refinement drift while maintaining strong end-task reasoning accuracy. In future work, we will extend this framework to broader naturalistic settings, improve the robustness of entailment-tree construction and diagnostic localisation, and further reduce verification cost through better reuse of verified subtrees.
L272: ## Limitations
L273: Our framework produces solver-checkable certificates, but the guarantee is necessarily conditional on the chosen autoformalisation function $\Phi$, the target formalism, and the capabilities of the underlying theorem prover. In particular, a verification can be valid in the induced formal theory while still being partially misaligned with the original natural language intent if $\Phi$ introduces subtle scope, polarity, or role mismatches that are not exposed by our current faithfulness checks.
L274: This dependence is amplified in naturalistic NLI, where missing background knowledge, implicit commonsense assumptions, or discourse phenomena (e.g., coreference, modality, temporality) may not be representable in the event-based logical form, making some instances difficult to certify without additional axioms or richer semantics.
L275: The effectiveness of localised refinement also depends on the quality of the intermediate structures proposed by the LLM and on the ability to map prover diagnostics back to the responsible region. When the initial entailment tree omits critical intermediate conclusions or introduces a misleading proof plan, bottom-up checking can localise which obligations are not discharged but may not reliably recover the globally correct chain without substantial restructuring.
L276: Finally, although our approach reduces expensive global regeneration, it still incurs non-trivial compute due to repeated LLM calls, repeated autoformalisation, and repeated prover invocations. Prover timeouts or inconclusive outcomes can remain a practical bottleneck on harder instances, and our current system does not provide a formal convergence guarantee to the minimal or unique refined explanation.
L277: ## References
L278:   * Dalvi et al. (2021) B. Dalvi, P. Jansen, O. Tafjord, Z. Xie, H. Smith, L. Pipatanangkura, and P. Clark Explaining answers with entailment trees. EMNLP. Cited by: cite90†§A.1 , cite91†§4 .
L279:   * Deepseek-AI (2025) Deepseek-AI DeepSeek-v3 technical report. External Links: 2412.19437, cite92†Link Cited by: cite93†§4 .
L280:   * Han et al. (2024) S. Han, H. Schoelkopf, Y. Zhao, Z. Qi, M. Riddell, W. Zhou, J. Coady, D. Peng, Y. Qiao, L. Benson, L. Sun, A. Wardle-Solano, H. Szabó, E. Zubova, M. Burtell, J. Fan, Y. Liu, B. Wong, M. Sailor, A. Ni, L. Nan, J. Kasai, T. Yu, R. Zhang, A. Fabbri, W. M. Kryscinski, S. Yavuz, Y. Liu, X. V. Lin, S. Joty, Y. Zhou, C. Xiong, R. Ying, A. Cohan, and D. Radev FOLIO: natural language reasoning with first-order logic.
L281: In Proceedings of the 2024 Conference on Empirical Methods in Natural Language Processing, Y. Al-Onaizan, M. Bansal, and Y. Chen (Eds.), Miami, Florida, USA, pp. 22017–22031. External Links: cite94†Link†aclanthology.org , cite95†Document†dx.doi.org Cited by: cite96†§A.1 , cite91†§4 .
L282:   * Jiang et al. (2024) D. Jiang, M. Fonseca, and S. Cohen LeanReasoner: boosting complex logical reasoning with lean. In Proceedings of the 2024 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies (Volume 1: Long Papers), K. Duh, H. Gomez, and S. Bethard (Eds.), Mexico City, Mexico, pp. 7497–7510. External Links: cite97†Link†aclanthology.org , cite98†Document†dx.doi.org Cited by: cite99†§1 , cite100†§1 .


## Original response: jan29_stdnext4budget

Decompose-and-Formalise: Recursively Verifiable Natural Language Inference (https://arxiv.org/html/2601.19605v1)
citeturn28438view1 [wordlim: 200] Crawled: 4 days ago; Content type: text/html; Source: open({"ref_id":"turn28434view2","lineno":310}); Total lines: 545
L301:   * Valentino and Freitas (2024) M. Valentino and A. Freitas On the nature of explanation: an epistemological-linguistic perspective for explanation-based natural language inference. Philosophy & Technology 37 (3), pp. 88. Cited by: cite99†§1 .
L302:   * Valentino et al. (2021) M. Valentino, I. Pratt-Hartman, and A. Freitas Do natural language explanations represent valid logical arguments? verifying entailment in explainable nli gold standards. IWCS 2021, pp. 76. Cited by: cite99†§1 .
L303:   * Weber et al. (2019) L. Weber, P. Minervini, J. Münchmeyer, U. Leser, and T. Rocktäschel NLProlog: reasoning with weak unification for question answering in natural language. In Proceedings of the 57th Annual Meeting of the Association for Computational Linguistics, A. Korhonen, D. Traum, and L. Màrquez (Eds.), Florence, Italy, pp. 6151–6161. External Links: cite138†Link†aclanthology.org , cite139†Document†dx.doi.org Cited by: cite108†§6 .
L304:   * Wu et al. (2022) Y. Wu, A. Q. Jiang, W. Li, M. Rabe, C. Staats, M. Jamnik, and C. Szegedy Autoformalization with large language models. In Advances in Neural Information Processing Systems, S. Koyejo, S. Mohamed, A. Agarwal, D. Belgrave, K. Cho, and A. Oh (Eds.), Vol. 35, pp. 32353–32368. External Links: cite140†Link†proceedings.neurips.cc Cited by: cite99†§1 .
L305:   * xAI (2025) xAI Grok 4. Note: cite141†https://x.ai/news/grok-4†x.ai Cited by: cite93†§4 .
L306:   * Xu et al. (2025a) J. Xu, H. Fei, M. Luo, Q. Liu, L. Pan, W. Y. Wang, P. Nakov, M. Lee, and W. Hsu Aristotle: mastering logical reasoning with a logic-complete decompose-search-resolve framework. In Proceedings of the 63rd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers), W. Che, J. Nabende, E. Shutova, and M. T. Pilehvar (Eds.), Vienna, Austria, pp. 3052–3075.
L307: External Links: cite142†Link†aclanthology.org , cite143†Document†dx.doi.org , ISBN 979-8-89176-251-0 Cited by: cite108†§6 .
L308:   * Xu et al. (2024) J. Xu, H. Fei, L. Pan, Q. Liu, M. Lee, and W. Hsu Faithful logical reasoning via symbolic chain-of-thought. In Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers), L. Ku, A. Martins, and V. Srikumar (Eds.), Bangkok, Thailand, pp. 13326–13365. External Links: cite144†Link†aclanthology.org , cite145†Document†dx.doi.org Cited by: cite99†§1 .
L309:   * Xu et al. (2025b) J. Xu, H. Fei, H. Zhou, X. Quan, Q. Huang, S. Wu, W. Y. Wang, M. Lee, and W. Hsu Training llms with logicreward for faithful and rigorous reasoning. External Links: 2512.18196, cite146†Link Cited by: cite99†§1 , cite100†§1 .
L310:   * Xu et al. (2025c) L. Xu, P. Beckmann, M. Valentino, and A. Freitas Adaptive llm-symbolic reasoning via dynamic logical solver composition. External Links: 2510.06774, cite147†Link Cited by: cite99†§1 .
L311:   * Zhang et al. (2025) L. Zhang, M. Valentino, and A. Freitas Autoformalization in the wild: assessing LLMs on real-world mathematical definitions. In Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing, C. Christodoulopoulos, T. Chakraborty, C. Rose, and V. Peng (Eds.), Suzhou, China, pp. 1720–1738. External Links: cite148†Link†aclanthology.org , cite149†Document†dx.doi.org , ISBN 979-8-89176-332-6 Cited by: cite99†§1 .
L312: ## Appendix A Dataset Details
L313: 
L314: ### A.1 Explanation Refinement
L315: #### ProofWriter.
L316: ProofWriter (cite73†Tafjord et al., 2021 ) is a synthetically generated deductive reasoning benchmark where each instance contains a natural language theory (facts and rules), a query, and a gold truth label, with controllable multi-hop proof depth. For explanation refinement, we sample 150 instances and stratify the sampling to cover a range of gold proof depths $d\in\{1,2,3,4,5\}$ on the ProofWriter D5 split under the open-world assumption.
L317: To avoid ambiguity in verification-oriented refinement, we restrict to boolean-labelled instances and exclude indeterminate cases (e.g., Unknown under open-world settings). Each instance is cast into an NLI-style pair $(P,h)$, where $P$ is the provided set of facts/rules and $h$ is the hypothesis statement.
L318: #### PrOntoQA.
L319: 
L320: PrOntoQA (cite74†Saparov and He, 2023 ) is a synthetic dataset designed to evaluate deductive reasoning in controlled settings. Following the Logic-LM (cite58†Pan et al., 2023 ) setup, we use the most challenging five-hop subset (fictional-entity reasoning). For explanation refinement, we randomly sample 150 instances from this subset. Since this subset is binary in nature, we keep boolean-labelled instances and cast each instance into the NLI-style format $(P,h)$.
L321: #### FOLIO.
L322: FOLIO (cite75†Han et al., 2024 ) is a human-curated first-order logic reasoning benchmark, pairing natural-language statements with formal logical structure to support theorem-prover-based verification. For explanation refinement, we use the evaluation split commonly adopted by prior neuro-symbolic work after preprocessing, and remove indeterminate labels to keep a boolean setting. Concretely, we start from 182 evaluation instances after filtering out 22 erroneous examples identified by cite59†Olausson et al.
L323: (2023) and exclude those with uncertain labels, yielding 122 instances. We then treat the remaining instances as NLI pairs $(P,h)$ for verification and refinement.
L324: #### EntailmentBank.
L325: EntailmentBank (cite76†Dalvi et al., 2021 ) is a multi-hop entailment benchmark that provides naturalistic premises and hypotheses together with structured explanation annotations (intermediate conclusions and entailment structure). For explanation refinement, we sample 150 instances and select examples spanning different gold proof depths to ensure coverage of both shallow and longer-horizon multi-step chains.
L326: Each instance is cast into $(P,h)$, where $P$ is the set of supporting statements (facts) and $h$ is the hypothesis.
L327: ### A.2 Logical Reasoning
L328: 
L329: #### ProofWriter.
L330: 
L331: For logical reasoning, we evaluate on the ProofWriter D5 split under the open-world assumption to retain the three-way label space (True/False/Unknown). We sample 225 instances stratified by gold reasoning depth $d\in\{1,2,3,4,5\}$, with 45 instances per depth. Within each depth bucket, we balance labels by sampling 15 instances per class.
L332: #### FOLIO.
L333: 
L334: For logical reasoning, the original validation split contains 204 instances, while we select the 182 evaluation instances after filtering out 22 erroneous examples identified by cite59†Olausson et al. (2023) for evaluation. We evaluate on this 182-instance set under the dataset’s original label space.
L335: #### PrOntoQA.
L336: 
L337: For logical reasoning, we follow prior work (cite58†Pan et al., 2023 ) and evaluate on the five-hop PrOntoQA subset. We randomly sample 200 instances from this subset (binary labels), which represents the most challenging multi-hop configuration in the benchmark.
L338: ## Appendix B Autoformalisation Errors
L339: Following the error taxonomy in cite66†Quan et al. (2025b) , we categorise autoformalisation errors into four broad types: syntax, implication, quantifier, and variable errors. We define an autoformalisation error as any mismatch between the intended logical meaning of the input sentence(s) (as captured by a reference logic template or gold formalisation) and the produced formal statement.

## Original response: jan29_stdnext4budget

Decompose-and-Formalise: Recursively Verifiable Natural Language Inference (https://arxiv.org/html/2601.19605v1)
citeturn28438view2 [wordlim: 200] Crawled: 4 days ago; Content type: text/html; Source: open({"ref_id":"turn28434view2","lineno":488}); Total lines: 545
L457: PrOntoQA  | 92.00  | 97.33  | 86.67 [-1pt]$\downarrow$5.33  | 92.67 [-1pt]$\downarrow$4.66  | 90.00 [-1pt]$\downarrow$2.00  | 94.00 [-1pt]$\downarrow$3.33
L458: EntailmentBank  | 21.33  | 70.00  | 17.33 [-1pt]$\downarrow$4.00  | 53.33 [-1pt]$\downarrow$16.67  | 19.33 [-1pt]$\downarrow$2.00  | 61.33 [-1pt]$\downarrow$8.67
L459: Backbone: Qwen3-max
L460: FOLIO  | 85.25  | 95.08  | 72.13 [-1pt]$\downarrow$13.12  | 86.89 [-1pt]$\downarrow$8.19  | 79.51 [-1pt]$\downarrow$5.74  | 90.98 [-1pt]$\downarrow$4.10
L461: ProofWriter  | 92.00  | 98.00  | 88.00 [-1pt]$\downarrow$4.00  | 93.33 [-1pt]$\downarrow$4.67  | 88.00 [-1pt]$\downarrow$4.00  | 96.00 [-1pt]$\downarrow$2.00
L462: PrOntoQA  | 98.00  | 100.00  | 86.67 [-1pt]$\downarrow$11.33  | 94.00 [-1pt]$\downarrow$6.00  | 92.00 [-1pt]$\downarrow$6.00  | 96.00 [-1pt]$\downarrow$4.00
L463: EntailmentBank  | 22.67  | 78.67  | 18.00 [-1pt]$\downarrow$4.67  | 61.33 [-1pt]$\downarrow$17.34  | 20.00 [-1pt]$\downarrow$2.67  | 71.33 [-1pt]$\downarrow$7.34
L464: Table 4: Ablations of LLM-TP Tree on GPT-4o and Qwen3-max (Init/Fin verified rate, %). Red arrows indicate the absolute decrease compared to LT under the same backbone.
L465: Table cite152†4 reports ablations of LLM-TP Tree (LT) on GPT-4o and Qwen3-max, using Init./Fin. logically valid explanation rates. Removing either of the two proposed components, atomic decomposition or multi-step $\theta$-substitution autoformalisation, consistently degrades across all datasets. Across datasets, Init. decreases by 4.00 to 13.12 points and Fin. decreases by 3.33 to 17.34 points, with the most pronounced degradation on EntailmentBank.
L466: Removing $\theta$-substitution also leads to a consistent drop, although smaller than w/o Atom indicating that multi-step substitution contributes materially to producing prover-compatible formalisations.
L467: ## Appendix F Full results: Model efficiency Across LLM Backbones
L468: 
L469: Figure cite153†7(a) , cite154†7(b) and cite155†7(c) shows average number of iterations required to refine an explanation across all LLMs. Figure cite156†7(e) , cite157†7(f) , cite158†7(g) and cite159†8 shows average inference time per iteration in both thinking and non-thinking models.
L470: 
L471: (a) FOLIO
L472: 
L473: (b) ProofWriter
L474: 
L475: (c) PrOntoQA
L476: 
L477: (d) EntailmentBank
L478: 
L479: (e) FOLIO
L480: 
L481: (f) ProofWriter
L482: 
L483: (g) PrOntoQA
L484: 
L485: (h) EntailmentBank
L486: Figure 7: Top: Average number of iterations required to refine an explanation. Bottom: Average inference time per iteration. Comparison between ER (Explanation-Refiner), FR (Faithful-Refiner), LT (LLM-TP Tree) and LT w/o AD (LT without atomic decomposition).
L487: 
L488: (a) FOLIO
L489: 
L490: (b) ProofWriter
L491: 
L492: (c) PrOntoQA
L493: 
L494: (d) EntailmentBank
L495: Figure 8: Average inference time per iteration in thinking mode LLMs. Comparison between ER (Explanation-Refiner), FR (Faithful-Refiner), LT (LLM-TP Tree) and LT w/o AD (LT without atomic decomposition).
L496: ## Appendix G Full Results: Autoformalisation Faithfulness Across LLM Backbones
L497: 
L498: Figure cite160†9 compares the average faithfulness of the autoformalisation process across different approaches, averaged over all LLM backbones.
L499: 
L500: (a) FOLIO
L501: 
L502: (b) ProofWriter
L503: 
L504: (c) PrOntoQA
L505: 
L506: (d) EntailmentBank
L507: 
L508: Figure 9: Comparison of the average faithfulness of the autoformalisation process across different approaches.
L509: ## Appendix H Solver Proof Depths
L510: 
L511: Table cite161†5 and Table cite162†6 shows Per-LLM depth alignment details for ProofWriter and EntailmentBank in refined and unrefined cases. Each cell reports the mean used proof depth averaged over instances within the corresponding gold depth bucket, for a fixed framework and LLM backbone.
L512: (a) ProofWriter: mean used proof depth by gold depth
L513: Framework LLM Gold depth $d$ 1 2 3 4 5 Explanation-Refiner GPT-4o 1.00 2.32 2.51 2.92 3.23 GPT-5 nano 1.14 2.00 2.67 2.61 2.94 Grok-4 fast 1.08 2.04 2.53 2.62 2.92 Deepseek-V3.1 1.28 2.41 2.23 2.87 3.04 Qwen3-max 1.10 2.43 2.24 2.90 3.11 Faithful-Refiner GPT-4o 1.00 2.26 2.76 3.43 3.94 GPT-5 nano 1.02 2.04 3.13 3.34 3.63 Grok-4 fast 1.14 2.09 2.67 3.18 3.87 Deepseek-V3.1 1.00 2.17 2.78 3.41 3.73 Qwen3-max 1.00 2.22 2.77 3.58 3.79 LLM-TP Tree GPT-4o 1.00 1.99 2.94 3.76 4.72 GPT-5 nano 1.08 2.12 2.98 3.68 4.53 Grok-4 fast 1.17 1.89 3.18 3.49 5.03 Deepseek-V3.1 1.00 2.03 3.08 3.84 4.94 Qwen3-max 1.00 2.00 3.00 3.89 4.88
L514: (b) EntailmentBank: mean used proof depth by gold depth
L515: Framework LLM Gold Depths $d$ 1 2 3 4 5 Explanation-Refiner GPT-4o 1.23 2.14 2.65 3.15 3.21 GPT-5 nano 1.21 2.23 2.43 2.91 2.94 Grok-4 fast 1.13 2.21 2.52 2.93 2.92 Deepseek-V3.1 1.16 2.28 2.67 3.04 3.16 Qwen3-max 1.28 2.32 2.63 3.18 3.20 Faithful-Refiner GPT-4o 1.12 2.10 2.87 3.33 3.67 GPT-5 nano 1.11 2.12 2.64 3.22 3.40 Grok-4 fast 1.17 2.13 2.72 3.58 3.42 Deepseek-V3.1 1.03 2.25 2.78 3.40 3.69 Qwen3-max 1.17 2.20 2.93 3.47 3.73 LLM-TP Tree GPT-4o 1.00 2.10 2.85 3.90 4.81 GPT-5 nano 1.00 1.84 2.84 3.86 4.71 Grok-4 fast 1.00 2.04 2.92 3.88 4.73 Deepseek-V3.1 1.00 1.97 3.03 4.03 4.85 Qwen3-max 1.00 1.96 2.94 3.98 4.92
L516: Table 5: Per-LLM depth alignment details for ProofWriter and EntailmentBank in refined cases.
L517: (a) ProofWriter: mean used proof depth by gold depth
L518: Framework LLM Gold depth $d$ 1 2 3 4 5 Explanation-Refiner GPT-4o 1.00 2.34 2.49 2.57 2.33 GPT-5 nano 1.12 1.99 2.57 2.46 2.24 Grok-4 fast 1.10 1.87 2.48 2.38 2.32 Deepseek-V3.1 1.18 2.37 1.98 2.84 2.54 Qwen3-max 1.00 2.33 2.11 2.47 2.62 Faithful-Refiner GPT-4o 1.02 2.16 2.73 3.44 3.12 GPT-5 nano 1.02 1.95 3.23 3.24 3.02 Grok-4 fast 1.16 2.46 2.62 3.09 3.06 Deepseek-V3.1 1.00 1.98 2.78 2.98 3.27 Qwen3-max 1.00 2.22 2.67 3.15 3.43 LLM-TP Tree GPT-4o 1.02 2.13 3.01 3.72 4.72 GPT-5 nano 1.09 2.14 2.95 3.54 4.65 Grok-4 fast 1.15 1.79 3.16 3.50 5.13 Deepseek-V3.1 1.02 2.13 3.04 3.86 4.87 Qwen3-max 1.00 1.98 3.00 3.88 4.91
L519: (b) EntailmentBank: mean used proof depth by gold depth
L520: Framework LLM Gold Depths $d$ 1 2 3 4 5 Explanation-Refiner GPT-4o 1.53 2.84 2.48 2.44 2.21 GPT-5 nano 1.39 2.99 2.33 2.31 1.95 Grok-4 fast 1.43 2.83 2.24 2.21 1.92 Deepseek-V3.1 1.48 2.58 2.33 2.14 1.96 Qwen3-max 1.88 3.12 2.32 2.19 2.12 Faithful-Refiner GPT-4o 1.34 2.42 2.48 3.23 3.55 GPT-5 nano 1.33 2.32 2.41 3.32 3.30 Grok-4 fast 1.49 2.28 2.43 3.54 3.42 Deepseek-V3.1 1.10 2.85 2.34 3.38 3.45 Qwen3-max 1.67 2.74 2.53 3.43 3.42 LLM-TP Tree GPT-4o 1.03 2.13 2.83 3.93 4.62 GPT-5 nano 1.13 1.86 2.80 3.78 4.51 Grok-4 fast 1.12 2.04 2.95 3.91 4.43 Deepseek-V3.1 1.03 1.89 3.12 4.12 4.67 Qwen3-max 1.00 2.01 2.99 4.08 4.74
L521: Table 6: Per-LLM depth alignment details for ProofWriter and EntailmentBank in unrefined cases.
L522: ## Appendix I Atomic Decomposition Prompt
L523: 
L524: We build the atomic decomposition prompt based on cite163†Srikanth and Rudinger (2025) as:
L525: 
L526: ## Appendix J Entailment Tree Construction Prompt
L527: 
L528: ## Appendix K $\theta$-substitution Autoformalisation Prompt
L529: 
L530: Experimental support, please cite164†view the build logs for errors. Generated by cite165†L A T E xml†math.nist.gov .
L531: ## Instructions for reporting errors
L532: 
L533: We are continuing to improve HTML versions of papers, and your feedback helps enhance accessibility and mobile support. To report errors in the HTML that will help us improve conversion and rendering, choose any of the methods listed below:
L534: 
L535:   * Click the "Report Issue" () button, located in the page header.
L536: 
L537: Tip: You can select the relevant text first, to include it in your report.


