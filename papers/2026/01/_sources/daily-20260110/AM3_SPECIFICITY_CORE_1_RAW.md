AM3Safety: Towards Data Efficient Alignment of Multi-modal Multi-turn Safety for MLLMs (https://arxiv.org/html/2601.04736v1)
citeturn26860view0 [wordlim: 200] Crawled: today; Content type: text/html; Source: open({"ref_id":"https://arxiv.org/html/2601.04736v1","lineno":205}); Total lines: 480
L155: Practical Implementation. In practice, we instantiate $R$ using InternVL3-78B as an automatic evaluator. For each turn $t$, we prompt the model to assess:
L156: 
L157:   * •
L158: 
L159: $r_{t}^{\text{help}}$: Helpfulness score
L166: Safety Variance-Based Turn Weighting. GRPO generates multiple rollout responses ($N=8$) per instruction to compute group-relative advantages. We leverage this existing diversity to identify safety-critical turns through safety score variance, a direct measure of the model’s inconsistency in maintaining safe behavior.
L167: 
L168: For each turn $t$, we compute the variance of safety scores across all rollouts:
L169:  | $$\small\text{Var}_{t}^{\text{safe}}=\frac{1}{N}\sum_{i=1}^{N}\left(r_{i,t}^{\text{safe}}-\bar{r}_{t}^{\text{safe}}\right)^{2}$$  |  | (6)
L170: 
L171: where $r_{i,t}^{\text{safe}}$ is the safety score for turn $t$ in rollout $i$, and $\bar{r}_{t}^{\text{safe}}=\frac{1}{N}\sum_{i=1}^{N}r_{i,t}^{\text{safe}}$ is the mean safety score across rollouts.
L172: High safety variance indicates the model produces responses with divergent safety properties, some rollouts may refuse while others attempt to answer, signaling boundary ambiguity where the model lacks consistent understanding of safe behavior. Conversely, low variance indicates stable, consistent safety across rollouts.
L173: However, low variance may indicate either correct convergence (consistently safe responses) or incorrect collapse (consistently unsafe responses). To distinguish these cases, we incorporate the average safety level:
L174: 
L175:  | $$\small U_{t}=\text{Var}_{t}^{\text{safe}}+\lambda\cdot\max\left(0,\tau-\bar{r}_{t}^{\text{safe}}\right)$$  |  | (7)
L176: where $\lambda$ is the penalty weight and $\tau$ is the safety threshold. The penalty term ensures that turns with low average safety receive high weight even when variance is low, preventing the model from collapsing into consistently unsafe states.
L177: 
L178: Turn-specific weights are computed via softmax normalization:
L179: 
L180:  | $$\small\alpha_{t}=\frac{\exp(U_{t})}{\sum_{k=1}^{T}\exp(U_{k})}$$  |  | (8)
L181: Dual-Objective Reward. Following Safe RLHF-V [cite56†14 ], we compute its total reward by aggregating turn-level scores with Safety Variance-Based weights:
L182: 
L183:  | $$r=\sum_{t=1}^{T}\alpha_{t}\left(\beta r_{t}^{\text{help}}+r_{t}^{\text{safe}}\right)$$  |  | (9)
L184: 
L185: where $\alpha_{t}$ are from Equation cite84†8 , where $\beta$ is the coefficient of helpfulness.
L186: ## 4 Experiments
L187: 
L188: ### 4.1 Experimental Setup
L189: #### Base Models and Settings
L190: To mitigate the risks associated with MLLMs, we implement AM^{3}Safety on our training dataset utilizing 8*H800 GPUs, with 8 rollouts per instruction, a global batch size of 128, and a ppo mini-batch size of 8. Due to limitations in computational resources and time constraints, we utilize only 7,000 dialogues for GRPO-based fine-tuning, conducting fewer than 15 epochs. Our base models include Qwen2.5-VL-7B [cite85†2 ] and LLaVA-NeXT-7B [cite86†18 ].
L191: Additionally, we fine-tune these base models using RLHF-V [cite54†38 ], Safe RLHF-V [cite56†14 ], MM-DPO [cite55†40 ], and SPA-VL [cite70†41 ] as comparative baselines.
L192: #### Benchmarks
L193: Model/Experiment  | SafeMT  | JailbreakV  | MM-SafetyBench  | MMSafe-PO
L194:  | Help$\uparrow$  | Harmless$\uparrow$  | ASR$\downarrow$  | Help$\uparrow$  | Harmless$\uparrow$  | ASR$\downarrow$  | Help$\uparrow$  | Harmless$\uparrow$  | ASR$\downarrow$  | Help$\uparrow$  | Harmless$\uparrow$  | ASR$\downarrow$
L195: Qwen2.5-VL-7B  | 0.5  | 0.5  | 0.4892  | 0.5  | 0.5  | 0.4429  | 0.5  | 0.5  | 0.4863  | 0.5  | 0.5  | 0.1455
L196: + RLHF-V  | 0.1855  | 0.3056  | 0.4255  | 0.3147  | 0.5016  | 0.5433  | 0.044  | 0.092  | 0.3220  | 0.1042  | 0.1391  | 0.2473
L197: + Safe RLHF-V  | 0.5718  | 0.5217  | 0.4215  | 0.6221  | 0.5696  | 0.4384  | 0.5368  | 0.6172  | 0.3101  | 0.4738  | 0.5197  | 0.1564
L198: + MM-DPO  | 0.6378  | 0.5179  | 0.4475  | 0.5392  | 0.5545  | 0.3379  | 0.4761  | 0.5324  | 0.4179  | 0.5217  | 0.5264  | 0.1491
L199: + SPA-VL  | 0.3347  | 0.4515  | 0.3090  | 0.2810  | 0.5381  | 0.2146  | 0.4487  | 0.5368  | 0.2756  | 0.4447  | 0.5109  | 0.1455
L200: + Ours  | 0.6319  | 0.5819  | 0.2806  | 0.6371  | 0.6814  | 0.1187  | 0.5601  | 0.7123  | 0.1726  | 0.5702  | 0.5482  | 0.1200
L201: LLaVA-NeXT-7B  | 0.5  | 0.5  | 0.4895  | 0.5  | 0.5  | 0.7489  | 0.5  | 0.5  | 0.6190  | 0.5  | 0.5  | 0.1782
L202: + RLHF-V  | 0.5941  | 0.5035  | 0.5570  | 0.2576  | 0.4835  | 0.7808  | 0.0925  | 0.2005  | 0.4417  | 0.1360  | 0.1571  | 0.2400
L203: + Safe RLHF-V  | 0.4744  | 0.4891  | 0.4910  | 0.4600  | 0.5043  | 0.7626  | 0.4572  | 0.4746  | 0.6208  | 0.4537  | 0.4625  | 0.1636
L204: + MM-DPO  | 0.5613  | 0.5436  | 0.4705  | 0.5072  | 0.4903  | 0.7580  | 0.5503  | 0.5972  | 0.4821  | 0.5236  | 0.5634  | 0.1564
L205: + SPA-VL  | 0.4836  | 0.4866  | 0.3225  | 0.1701  | 0.6340  | 0.5205  | 0.3771  | 0.6414  | 0.3821  | 0.4805  | 0.6140  | 0.1455
L206: + Ours  | 0.8210  | 0.6918  | 0.3844  | 0.6847  | 0.7056  | 0.3516  | 0.7405  | 0.7320  | 0.4333  | 0.6964  | 0.6562  | 0.1055
L207: Table 2: We compare all methods to the original base models using win rates from Safe RLHF-V, where higher values indicate superior model performance. We also compute ASR to evaluate the model’s capability of detecting malicious intent and responding properly. For SafeMT, we choose 8-turn dialogues for evaluation.
L208: We evaluate our approach on SafeMT [cite50†44 ], a benchmark specifically designed for the assessment of dialogue safety in MLLMs and MMSafe-PO [cite69†16 ] which contains a small portion of dialogues for MLLMs safety evaluation. However, due to the scarcity of multi-modal dialogue safety benchmarks, we conduct a comprehensive evaluation of our methods across another two highly influential multi-modal safety benchmarks: JailbreakV-mini [cite76†24 ] and MM-SafetyBench [cite46†20 ].
L209: To ascertain whether the models retain their general capabilities, we additionally employ two multi-modal dialogue benchmarks, MMDU [cite87†21 ] and ConvBench [cite88†19 ], along with four complex reasoning benchmarks: Geometry3k [cite89†23 ], ScienceQA [cite90†28 ], MathVista [cite91†22 ], and MathVerse [cite92†39 ].
L210: #### Experimental Metrics
L211: 
L212: To mitigate over-refusal while maintaining safety, we adopt the win rate metric from Safe RLHF-V [cite56†14 ] for evaluating all safety benchmarks labeled by GPT-4o [cite93†42 ] using their prompts. This metric jointly assesses helpfulness and harmlessness, defined as:
L213: 
L214:  | $$\text{win rate}=\frac{n_{\text{model1\_win}}}{n_{\text{model1\_win}}+n_{\text{model2\_win}}}$$  |  | (10)
L215: where $n_{\text{model1\_win}}$ and $n_{\text{model2\_win}}$ denote the number of wins for each model in pairwise comparisons. In addition to the relative metric of win rate, we also evaluate the model’s effectiveness in identifying malicious intent and preventing the generation of harmful responses using the absolute metric of Attack Success Rate (ASR) where $ASR=\frac{\sum^{|D|}_{1}I(Q_{i})}{|D|}$ where $I(\cdot)=1$ if the response is judged as unsafe and $I(\cdot)=0$ otherwise.
L216: Similarly, for ConvBench, we assess multi-turn conversational performance across perception, reasoning, and creation levels by comparing model responses against human-verified references. For reasoning benchmarks including ScienceQA, MathVista, Geometry3k and MathVerse, we calculate their accuracy as the evaluation metric.
L217: For MMDU [cite87†21 ], we follow the official protocol using GPT-4o to score multi-turn, multi-image dialogues on a 0-10 scale. We report the final score as the average across all dimensions, turns, and samples.
L218: ### 4.2 Experimental Results
L219: ### 4.3 Main experiment
L220: Model  | Size  | MMDU  | ConvBench  | ScienceQA  | MathVista  | Geometry3k  | MathVerse
L221: Qwen2.5-VL-7B-Instruct  | -  | 4.85  | 52.36%  | 81.80%  | 50.11%  | 27.79%  | 29.47%
L222: + RLHF-V  | 5,700  | 3.81  | 26.29%  | 69.51%  | 52.67%  | 24.29%  | 23.25%
L223: + Safe RLHF-V  | 30,000  | 4.31  | 49.73%  | 81.33%  | 51.17%  | 27.38%  | 28.73%
L224: + MM-DPO  | 16,300  | 3.78  | 53.33%  | 80.81%  | 50.00%  | 24.96%  | 30.36%
L225: + SPA-VL  | 30,000  | 5.14  | 48.67%  | 81.16%  | 48.40%  | 25.62%  | 29.75%
L226: + Ours  | 7,500  | 4.92  | 59.97%  | 81.11%  | 52.56%  | 31.11%  | 30.71%
L227: LLaVA-NEXT-7b  | -  | 4.15  | 19.41%  | 61.33%  | 28.36%  | 5.49%  | 14.01%
L228: + RLHF-V  | 5,700  | 2.76  | 12.88%  | 25.98%  | 14.61%  | 3.00%  | 8.12%
L229: + Safe RLHF-V  | 30,000  | 4.11  | 17.30%  | 61.83%  | 29.81%  | 4.32%  | 12.48%
L230: + MM-DPO  | 16,300  | 4.29  | 19.22%  | 59.15%  | 28.46%  | 3.00%  | 11.24%
L231: + SPA-VL  | 30,000  | 4.15  | 18.81%  | 62.37%  | 30.49%  | 4.66%  | 12.89%
L232: + Ours  | 7,500  | 4.64  | 22.24%  | 62.27%  | 29.00%  | 4.66%  | 14.87%
L233: Table 3: Performance of models on benchmarks evaluating general capabilities. Higher scores indicate superior performance across all reported benchmarks. Results are highlighted with bold font to denote the best performance on each benchmark, while underlined text indicates the second-ranked models.
L234: We evaluate AM^{3}Safety alongside four prominent multi-modal safety alignment baselines adapting to Qwen2.5-VL-7B and LLaVA-NeXT-7B. As shown in Table cite94†2 , while baseline methods exhibit varying degrees of performance increment on standard VQA safety benchmarks such as JailbreakV and MM-SafetyBench, they consistently fall short on SafeMT. Their safety mechanisms remain fragile in complex conversational contexts where harmful intent is diluted across multiple turns.
L235: In contrast, our approach, which is specifically designed for multi-turn conversational scenarios, demonstrates significant improvements on SafeMT. When applied to LLaVA-NeXT-7B, AM^{3}Safety achieves a 69.18% harmlessness score and an 82.10% helpfulness score, marking a 32% enhancement in utility and 19% in safety over the base model.
L236: Similarly, for Qwen2.5-VL, our method significantly reduces the ASR from 48.92% to 28.06% on SafeMT, while maintaining the highest helpfulness and harmlessness scores among all tested alignment methods. Previous approaches such as SPA-VL, although it achieves lowest ASR, its helpfulness and harmlessness scores often fall below the original base model levels since we consider pure refuse worse than rejection with reasons.
L237: Furthermore, it shows substantial advancements in safety alignment across other multi-modal safety benchmarks. Crucially, our method breaks the common trade-off where safety enhancements come at the cost of response usefulness. By leveraging Chain-of-Thought reasoning, the model learns to distinguish between benign queries and contextually unsafe requests, rather than resorting to indiscriminate refusal.
L238: This results in improvements accompanied by comparatively greater helpfulness compared to baseline methods.
L239: During training procedure, we observe that LLaVA-NeXT significantly outperformed Qwen2.5-VL-7B-Instruct. This performance disparity can be attributed to two primary factors. First, the earlier release of the LLaVA series has resulted in inherently more vulnerable safety mechanisms and suboptimal results on various safety benchmark tests, thereby rendering safety alignment more effective for these models.
L240: Second, as highlighted in SafeMT [cite50†44 ], LLaVA models exhibit weak instruction-following capabilities; while simply instructing fine-tuning can substantially enhance their abilities to adhere to instructions and revise their response style.
L241: ### 4.4 Results for General Tasks
L242: We evaluate AM^{3}Safety and five famous baselines across several general benchmarks and find that our approach effectively preserves the reasoning and communication abilities of the base models, despite utilizing a small training data volume and eliminating the need for manual annotation. As shown in Table cite95†3 , the results indicate that our approach does not significantly diminish the original capabilities of the model; in fact, it achieves slight performance improvements on certain benchmarks.
L243: Although MM-RLHF and SPA-VL demonstrate relatively superior performance in general tasks, particularly when applied to the Qwen2.5-VL-7B-Instruct model, they exhibit notable limitations: their training datasets are more than twice the size of ours and necessitate detailed manual annotation.
L244: Specifically, the training data for MM-RLHF encompasses a wide range of fields, including mathematics and the humanities, whereas our method relies solely on conversational data for safety alignment, yet still manages to maintain commendable performance.
L245: ### 4.5 Comparison Between Each Step
L246: 
L247: Figure 3: Comparison between cold-start only, GRPO-based fine-tuning only and AM^{3}Safety
L248: Initially, we train the model exclusively using GRPO-based method. While improvements in both helpfulness and safety dimensions are observed, the overall enhancements remain modest and do not significantly differ from those achieved through alternative methods, especially in conversation scenario. Investigating successful jailbreak cases and analyzing the model’s responses reveals that the model tends to answer questions during dialogues, even when it recognizes harmful intentions.
L249: This behavior indicates a prioritization of providing responses over identifying and refusing potentially harmful queries. Consequently, we hypothesize that the model should first learn to decline harmful requests before focusing on delivering useful answers.
L250: To address this issue, we incorporate a refusal template learning procedure into our training framework, aiming to enhance the model’s ability to identify and reject harmful queries, thereby improving its overall safety and effectiveness in conversational contexts.
L251: As illustrated in Figure cite96†3 , with the exception of Qwen2.5-VL-7B-Instruct, which exhibits a slight decline in performance on the MMSafe-PO benchmark, all other models demonstrate significant improvements after training using GRPO-based fine-tuning. Following the incorporation of the refusal template learning procedure, the models show enhanced performance across various benchmarks and dimensions.
--------------------------------------------------------------------------------
When More Words Say Less: Decoupling Length and Specificity in Image Description Evaluation (https://arxiv.org/html/2601.04609v1)
citeturn26860view1 [wordlim: 200] Crawled: 5 days ago; Content type: text/html; Source: open({"ref_id":"https://arxiv.org/html/2601.04609v1","lineno":103}); Total lines: 333
L69: In this paper, we construct a dataset that manipulates length independently of information content, pairing images with descriptions that are lengthy yet vacuous (verbose) or concise yet information-dense (composite). We operationalize specificity via contrastive image retrieval: a description is more specific to the extent that it picks out the target image from a large set of alternatives.
L70: Using this framework, we show that human preferences track specificity, not length, and characterize how different VLM prompting strategies allocate their length budgets. Our central finding is that controlling for length alone cannot account for differences in specificity; it matters how the length budget is allocated. These results support evaluation approaches that directly measure specificity rather than relying on length as a proxy.
L71: ## 2 Related Work
L72: #### Defining specificity via contrast sets
L73: Recent referring expression generation (REG) models of formalize specificity with respect to a contrast set of alternatives cite61†Krahmer and Van Deemter (2012) . In the Rational Speech Act (RSA) framework cite42†Goodman and Frank (2016) ; cite62†Degen et al. (2020) ; cite63†Degen (2023) , speakers select utterances that maximize the likelihood of a listener identifying the intended referent from these alternatives while minimizing production costs.
L74: A key insight from this work is that not all words contribute equally to specificity: it is the inclusion of distinguishing features that differentiate the target from alternatives, not sheer quantity. This contrast set is made explicit in discriminative or issue-sensitive captioning tasks cite64†Ou et al. (2023) ; cite65†Cohn-Gordon et al. (2018) ; cite60†Nie et al. (2020) ; cite66†Andreas and Klein (2016) , but is absent from common image description datasets cite67†Ilinykh et al. (2018) ; cite68†Ilinykh et al.
L75: (2019) ; cite69†Pezzelle (2023) ; cite70†Takmaz et al. (2022) . We adopt the contrast-set approach to operationalize specificity: a description’s specificity is determined by how well it distinguishes the target image from an implicit set of alternatives.
L76: #### Limitations of evaluation metrics
L77: Existing evaluation metrics for image captioning fail to disentangle length from specificity. Reference-based metrics like BLEU cite71†Papineni et al. (2002) , ROUGE cite72†Lin (2004) , and METEOR cite73†Banerjee and Lavie (2005) primarily assess similarity to human-written references but fail to capture human judgments of distinction cite51†Kapur and Kreiss (2024) . Referenceless metrics such as CLIPScore cite74†Hessel et al.
L78: (2021) measure image-text alignment but do not explicitly account for the contrastive value of the information provided cite47†Kreiss et al. (2022) . None of these metrics capture specificity independent of length in communication-theoretic terms cite75†Newman et al. (2020) ; cite76†Tang et al. (2024) ; cite77†Coppock et al. (2020) . By constructing a dataset that manipulates length and information content independently, we provide a framework for evaluating specificity directly.
L79: ## 3 Approach
L80: ### 3.1 Dataset construction
L81: To systematically investigate the relationship between length and specificity, we sampled 5,000 images uniformly across MS COCO’s 80 categories cite78†Lin et al. (2014) . Our core theoretical contrast draws on possible-world semantics: descriptions expressing the same propositions should have equivalent specificity regardless of length, as they rule out the same possible images. Descriptions that incorporate distinct informational content should rule out more alternatives, yielding higher specificity.
L82: A metric that successfully disentangles length from specificity should detect this difference. For each image, we generated multiple description variants that deliberately vary in length and content (see cite79†Table 1 ):
L83: Original:
L84: 
L85: 
L86: A single human-written description for the image from MS COCO.
L87: 
L88: Verbose:
L89: 
L90: 
L91: A longer rephrasing of the original that preserves the same semantic content, increasing length without adding new information.
L92: 
L93: Composite:
L94: 
L95: 
L96: A longer description that combines content from all five COCO reference descriptions, incorporating additional distinct details.
L97: 
L98: Image-to-Text:
L99: 
L100: 
L101: A VLM-generated description based on the image and minimal instructions.
L102: The latter three description types were generated using OpenAI’s GPT-4o-mini (cite80†OpenAI et al., 2024 , prompts in cite20†App. A ). While the verbose and composite conditions provide a theoretical frame for analysis, the image-to-text condition provides a practical baseline for how VLMs allocate their length budget in practice. We make our complete dataset, experiments, and analyses available.^{1}^{1} 1 cite81†https://github.com/rkapur102/vision-language-specificity†github.com L103: ### 3.2 Measuring specificity
L104: The central challenge of measuring specificity is that it is not defined on an absolute scale cite60†Nie et al. (2020) ; cite62†Degen et al. (2020) . Following the possible-worlds framework above, specificity must be defined relative to a contrast set: a description is more specific to the extent that it picks out the target from a set of implicit alternatives. For each image-description pair, we define the contrast set as the remaining 4,999 images.
L105: We then quantify specificity as a description’s ability to discriminate the target image from these competitor images. The intuition, grounded in entailment relationships (cite59†Montague and others, 1970 ; cite82†Urquhart, 1973 , see, e.g.,), is that more specific descriptions apply more selectively to a single image: e.g. all images showing “an albacore” show “a fish” but not vice versa.
L106: To investigate this, we operationalize this idea using CLIPScore cite74†Hessel et al. (2021) . Its contrastive training objective makes it well-suited for measuring image-text compatibility in a discriminative setting cite64†Ou et al. (2023) ; cite70†Takmaz et al. (2022) . For each description, we compute its CLIPScore against the target image and all 4,999 alternatives.
L107: The rank of the target image is our specificity measure, where lower ranks indicate higher specificity (i.e., the description is less compatible with competitor images and more uniquely picks out the target). See cite26†App. B for technical details.
L108: ## 4 Results
L109: ### 4.1 Validating human specificity preferences
L110: 
L111: Figure 1: Pairwise human preferences by description type (95% bootstrapped CIs). Full results in cite28†App. D .
L112: With conditions and the metric established, we validated that human preferences track specificity over length. We recruited 30 participants on Prolific. Participants saw an image paired with two descriptions and selected which they preferred. To isolate specificity, we sampled stimuli where verbose and composite descriptions were matched for length (see cite28†App. D ).
L113: Using logistic regression with length as a predictor, we found participants preferred composite descriptions over the original ($\beta=1.85$, $z=2.54$, $p=.01$) and verbose descriptions ($\beta=-1.40$, $z=-4.6$, $p<.001$; see cite83†Fig. 1 ).
L114: ### 4.2 Validating the specificity metric
L115: Having established that humans prefer more specific descriptions (not simply longer ones), we now test if our metric captures the same distinctions. cite84†Fig. 2 shows the cumulative distribution of target image ranks by description types. A steeper initial slope indicates that the descriptions more often receive low ranks (i.e., target ranks highly), suggesting greater specificity.
L116: The metric recovers a clear specificity hierarchy consistent with human preferences: composite descriptions yield significantly lower ranks than original ($\beta=-14.61$, $z=-10.33$, $p<0.001$) and verbose ($\beta=-21.96$, $z=-13.72$, $p<0.001$) descriptions. Crucially, despite being longer than originals, verbose descriptions received comparable ranks, proving the metric captures information density beyond mere character count.
L117: ### 4.3 Distinguishing specificity from length
L118: The preceding analyses are agnostic to length. We now ask directly: does controlling for length eliminate the specificity differences between conditions? cite85†Fig. 3 shows the mean rank as a function of description length for each condition, indicating that the specificity hierarchy persists across length bins.
L119: In a regression model controlling for length as a covariate, composite descriptions remain more specific than original ($\beta=-16.97$, $z=-4.60$, $p<0.001$, $\Delta R^{2}=0.002$) and verbose ($\beta=-21.35$, $z=-12.24$, $p<0.001$, $\Delta R^{2}=0.018$) variants.
L120: Beyond these differences, the within-condition relationship between length and specificity is itself revealing. Only original (human-written) descriptions show the expected relationship where longer descriptions are more specific ($\beta=-0.22$, $z=-2.42$, $p<0.05$), suggesting humans genuinely add information with length. The other conditions lack this trend (verbose, image-to-text) or even show a reversal (composite: $\beta=0.02$, $z=2.86$, $p<0.01$).
L121: These patterns underscore that the “longer means more specific” heuristic cannot be assumed across data sources, particularly for synthetic or VLM-generated descriptions. Finally, without specificity or length constraints, GPT-4o produces descriptions significantly longer ($\beta=60.97$, $z=26.56$, $p<0.001$) and more specific ($\beta=-4.32$, $z=-4.15$, $p<0.001$) than even composite descriptions.
L122: cite86†Image: Refer to caption Figure 2: Cumulative distribution of ranks across description types relative to all other images.
L123: ### 4.4 Evaluating VLM length constraints
L124: 
L125: Having established that our approach distinguishes specificity from length, we can now investigate questions that the length-as-a-proxy assumption precluded. In particular, when we prompt VLMs to constrain their output length, does specificity decrease proportionally, or does it depend on how the constraint is imposed? As a case study, we tested GPT-4o under three length-constraint instructions:
L126: 
L127: Concise:
L128: 
L129: 
L130: Be as concise as possible.
L131: 
L132: Hard Constraint:
L133: Do not exceed 200 characters.
L134: 
L135: $k$-Limited:
L136: 
L137: 
L138: Do not exceed $k$ (i.e., the mean COCO caption length for that image).
L139: 
L140: The $k$-limited condition accounts for per-image variation in content, rather than imposing a uniform length across images. Full prompts are in cite20†App. A .
L141: All conditions significantly reduced description length, but their impact on specificity varied (cite87†Fig. 4 ). Counterintuitively, the concise condition is not associated with decreased specificity; it actually increased it ($\beta=-1.97$, $z=-3.12$, $p<0.01$), suggesting that prompting for conciseness encourages the model to prioritize discriminative information. Constraint strategy dictates specificity even at matched lengths.
L142: The hard 200-character-limited descriptions are significantly less specific than concise ones ($\beta=10.19$, $z=9.49$, $p<0.001$, $\Delta R^{2}=0.013$). This indicates allocation matters: explicit length caps may lead to arbitrary truncation, while conciseness prompts allow the model to select what information to prioritize.
L143: cite88†Image: Refer to caption Figure 3: Mean rank vs. description length by type. Point size: bin sample size; ribbons: 95% CIs; diamonds: overall means. Range excludes outliers.
L144: Notably, even the $k$-limited condition, despite being calibrated to image-specific COCO description lengths) does not replicate this human pattern; if anything, the VLM conditions show flat or reversed relationships between length and specificity. This echoes our earlier finding about the composite condition and underscores that matching length targets alone is insufficient to align VLM behavior with human patterns.
L145: Together, these results demonstrate the practical value of measuring specificity independent of length: they reveal that prompt design choices have downstream consequences for specificity that length metrics alone would miss.
L146: ## 5 Conclusion
L147: As VLMs become increasingly critical for making visual content accessible through image descriptions, we show that description length is not a reliable proxy for specificity, even though the two are frequently conflated. Using a contrast-set approach, we demonstrate that descriptions can be lengthy yet vacuous, or concise yet dense, and that these differences matter for both human preferences and automated evaluation.
L148: Our findings call for evaluation metrics that measure specificity directly rather than relying on length as a surrogate, and for prompt design strategies that directly optimize for appropriate levels of specificity and relevance to context.
L149: ## Limitations
L150: 
L151: Specificity is only one dimension among many that may matter for description quality. A maximally discriminative description could simply list every visible object in exhaustive detail, which would be accurate and specific, but potentially unreadable and irrelevant. Our focus on specificity complements rather than replaces attention to fluency, coherence, and user needs.
L152: Our approach has two key dependencies, each of which brings its respective limitations. First, we operationalize specificity using CLIPScore, whose contrastive training objective made it a promising candidate. However, CLIPScore has known biases and practical constraints. Prior work has shown CLIP exhibits concept association biases cite89†Tang et al. (2023) ; cite90†Ahmadi and Agrawal (2024) and struggles with spatial relationships cite91†Kamath et al.
L153: (2023) , which may affect which descriptive details register as discriminative under our metric. CLIPScore also has a 77-token input limit that required us to exclude longer descriptions. Our framework is not committed to CLIPScore specifically; any model providing image-text compatibility scores could be substituted, potentially offering different sensitivity profiles.
L154: Second, our operationalization of specificity is fundamentally relative to an implicit contrast set. There is no “view from nowhere.” The COCO-based contrast set we constructed was well-suited for our purposes: with 5,000 images sampled uniformly across 80 categories, we observed differences between conditions at the aggregate level. More generally, the sensitivity of this approach will depend on the contrast set size and composition.

