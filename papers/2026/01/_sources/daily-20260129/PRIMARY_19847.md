# Exact-v1 necessary primary — 2601.19847

Preserved original tool responses; repeated returned context is not a claim of full-appendix review.

## jan29_stdvisionhead

Identifying and Transferring Reasoning-Critical Neurons: Improving LLM Inference Reliability via Activation Steering (https://arxiv.org/html/2601.19847v1)
citeturn28473view3 [wordlim: 200] Crawled: today; Content type: text/html; Source: open({"ref_id":"https://arxiv.org/html/2601.19847v1","lineno":null}); Total lines: 605


## jan29_stdvisionroute

Identifying and Transferring Reasoning-Critical Neurons: Improving LLM Inference Reliability via Activation Steering (https://arxiv.org/html/2601.19847v1)
citeturn28474view2 [wordlim: 200] Crawled: today; Content type: text/html; Source: find({"ref_id":"https://arxiv.org/html/2601.19847v1","pattern":"3."}); Total lines: 605
L118: As shown in Figure cite99†2 , we compare the mean activations of highly contrastive neurons under successful and failed reasoning. Notably, the 3028-th neuron in layer 27 shows substantially higher activation during successful reasoning, whereas the 246-th and 1908-th neurons in layer 26 exhibit the opposite trend. This indicates that specific neurons capture informative signals associated with reasoning success at test time.
L119: #### Finding 2. Token-level neuron activations are predictive of the final correctness of LLM reasoning.
L120: 
L121: As reported in Table cite100†1 , probing classifiers trained solely on last-token activations achieve AUROC scores around 0.7 across two datasets and two models, reaching up to 0.76 on AIME with the Qwen3-1.7B model. These observations suggest that neuron activation states are systematically correlated with reasoning outcomes.
L122: ## 3 Methodology
L123: Figure cite101†3 overviews our AdaRAS framework. First, we identify RCNs by contrasting activation patterns from correct and incorrect reasoning samples (cite13†§3.1 ). Then, we apply sparse activation steering to selectively intervene on these neurons (cite14†§3.2 ). To avoid perturbing already-correct reasoning, we introduce an adaptive intervention strategy that conditionally modulates activations at test time (cite15†§3.3 ).
L124: Finally, we describe the construction of parallel reasoning traces used in our experiments (cite16†§3.4 ).
L125: ### 3.1 Reasoning Neuron Identification
L126: We identify reasoning-critical neurons (RCNs) by directly contrasting activation patterns between correct and incorrect reasoning trajectories. While probing-based methods can assign neuron importance via classifier weights, we find them unreliable in practice due to their sensitivity to feature selection and dependence on probe generalization. Following prior works (cite90†Rimsky et al., 2024 ), we therefore adopt a probing-free, activation-level criterion based on mean activation differences.
L127: Let $a_{i}^{l}(t)$ denote the activation value of neuron $i$ at layer $l$ for token $t$. Given paired correct and incorrect reasoning traces $\mathcal{P}=\{(p_{k}^{+},p_{k}^{-})\}_{k=1}^{N}$, we define the reasoning-critical score of neuron $(l,i)$ as the difference in mean activations:
L128: 
L129:  | $$\begin{gathered}S(l,i)=\EV_{k\sim[N]}\Big[\mu(a_{i}^{l},p_{k}^{+})-\mu(a_{i}^{l},p_{k}^{-})\Big],\\
L130: \mu(a,p)\triangleq\frac{1}{|p|}\sum_{t\in p}a(t),\end{gathered}$$  |  | (1)
L131: where $|p|$ denotes the length of the reasoning trace. Unlike prior works (cite90†Rimsky et al., 2024 ) which adopt token-level MD applied to the final answer, this global formulation captures sustained activation patterns accumulated throughout the reasoning process. Specifically, for each layer $l$, the scores of all neurons form a layer-wise vector $\mathbf{S}_{l}=[S(l,1),\dots,S(l,d)]^{\top}$, which serves as the steering direction for test-time intervention.
L132: ### 3.2 Critical Activation Selection
L133: From preliminary results, our key observation is that correct reasoning is supported by structured activation patterns formed by a small subset of neurons, rather than uniformly distributed across entire layers. Therefore, instead of intervening at the layer level, we perform neuron-level selection and steering. Specifically, most modern LLMs, such as LLaMA and Qwen, employ SwiGLU activations (cite102†Shazeer, 2020 ), whose signed output is necessary for representations learning (cite103†Huang, 2024 ).
L134: Our empirical analysis also reveals that neurons whose average activation polarity differs between correct and incorrect reasoning trajectories are particularly discriminative (see cite28†4.4 for detailed results). Intuitively, such polarity reversals indicate neurons that actively support or suppress valid reasoning, depending on the reasoning outcome.
L135: Formally, for each neuron $(l,i)$, we retain it for steering only if
L136: 
L137:  | $$\EV_{k}\!\left[\mu(a_{i}^{l},p_{k}^{+})\right]\cdot\EV_{k}\!\left[\mu(a_{i}^{l},p_{k}^{-})\right]<0,$$  |  | (2)
L138: i.e., its mean activation exhibits a sign flip between correct and incorrect traces. This polarity-based filtering yields a sparse candidate set of RCNs. We then rank the retained neurons by the magnitude of their importance scores $|S(l,i)|$ and select the top-$K$ neurons to construct a sparse steering vector $\bm{S}^{\prime}_{l}$ for each layer. The steering strength is controlled by a positive scalar $\alpha\in[0,\infty]$. Activation steering is applied within the MLP block of the LLM:
L139:  | $$\mathbf{h}^{l}=\mathbf{h}^{l-1}+\mathbf{W}_{down}^{l}\left(\phi(\mathbf{W}_{up}^{l}\mathbf{h}^{l-1})+\alpha\bm{S}^{\prime}_{l}\right),$$  |  | (3)
L140: 
L141: where $\bm{S}^{\prime}_{l}$ is constructed once from a reference dataset and applied uniformly at each decoding step during test-time inference.
L142: ### 3.3 Adaptive Intervention Strategy
L143: Our early experiments shown a trade-off in activation steering: while it effectively rectifies incorrect reasoning, it inadvertently degrade performance on some originally correct samples. To address this, we introduce a lightweight failure prediction module that adaptively gates steering at test time. Specifically, we formulate a prediction task to estimate whether the base model can correctly answer a given input.
L144: The predictor operates on early neuron activations induced by the input prompt, which capture the model’s initial reasoning state. To reduce dimensionality, we select a small set of activations using $F$-statistics method as the input features. A attention-based classifier is then trained on these features and achieves an AUROC of 0.8347 on AIME dataset, which further supports our insights that there exists a strong correlation between activation patterns and reasoning outcomes.
L145: During inference, the predictor serves as a gate: AdaRAS is applied only when a reasoning failure is predicted. This adaptive intervention improves overall reasoning reliability while preserving performance on inputs that are already correctly handled.
L146: ### 3.4 Contrastive Data Construction
L147: As mentioned in Section cite13†3.1 , identifying RCNs requires contrastive reasoning traces that share the same input but differ in outcome correctness. To this end, we construct paired positive and negative reasoning trajectories via self-sampling. For each input prompt, we sample multiple reasoning trajectories using high-temperature decoding and partition them into positive and negative sets based on answer correctness.


## jan29_stdvisioncore

Identifying and Transferring Reasoning-Critical Neurons: Improving LLM Inference Reliability via Activation Steering (https://arxiv.org/html/2601.19847v1)
citeturn28475view2 [wordlim: 200] Crawled: today; Content type: text/html; Source: open({"ref_id":"https://arxiv.org/html/2601.19847v1","lineno":110}); Total lines: 605
L98: The contributions of this paper are threefold: 1) To our knowledge, we present the first systematic evidence that reasoning correctness can be predicted and improved through neuron interventions, establishing activation steering as a viable tool for enhancing LLM reasoning. 2) We introduce AdaRAS, a parameter-free, test-time activation steering framework that consistently enhances reasoning performance and transfers across tasks and datasets.
L99: 3) We provide mechanistic insights showing that AdaRAS stabilizes latent reasoning trajectories while preserving semantic representations, enabling plug-and-play deployment.
L100: ## 2 Preliminaries
L101: 
L102: In this section, we present preliminary probing results showing that specific neuron activations are predictive of reasoning correctness, which motivates the design of our proposed AdaRAS.
L103: ### 2.1 Task Formulation
L104: We first define Reasoning-Critical Neurons (RCNs) as neurons who positively contribute to correct reasoning outcomes. Given a dataset $D=\{(x_{i},y_{i})\}$ and a reasoning language model $\mathcal{M}$, we denote by $r_{i}$ the model-generated reasoning trace for input $x_{i}$, and by $a_{i}$ the final answer extracted from $r_{i}$. We define a binary correctness label $c_{i}=\mathbb{I}[a_{i}=y_{i}]$, which serves as the target signal throughout this work.
L105: Architecturally, the model $\mathcal{M}$ consists of $L$ Transformer decoder layers. Following prior work (cite95†Geva et al., 2021 ; cite96†Meng et al., 2022 ), we focus on the MLP blocks, which are widely believed to encode high-level semantic patterns. Specifically, we take the intermediate activation for each MLP block as the internal representation.
L106: Figure 2: Comparison of activations of key neurons under successful and failed reasoning on AIME.
L107: ### 2.2 LLM Reasoning Signatures
L108: Motivated by recent advances in LLM interpretability (cite97†Belinkov, 2022 ; cite94†Gurnee et al., 2023 ), we ask whether reasoning correctness can be inferred directly from intermediate neuron activations at test time. As a preliminary study, we probe last-token activations of Qwen3 series models (cite69†Yang et al., 2025a ) on mathematic datasets (i.e., AIME and AMC-12) to assess their predictive power for reasoning reliability.
L109: In contrast to prior work on stylistic control or knowledge editing, we focus on identifying neurons that are specifically predictive of reasoning correctness. Detailed experimental setups are provided in the Appendix cite41†A .
L110: Table 1: AUROC of probing classifiers trained on last-token activations for predicting reasoning correctness.
L111: Dataset  | Model  | AUROC
L112: AIME (24+25)  | Qwen3-1.7B  | 0.7639
L113: Qwen3-4B  | 0.7153
L114: AMC-12  | Qwen3-1.7B  | 0.7091
L115: Qwen3-4B  | 0.6727
L116: cite98†Image: Refer to caption Figure 3: Overview of AdaRAS: (1) reasoning neuron identification (cite13†§3.1 ), which identifies critical neurons by measuring global activation differences between contrastive reasoning trajectories; (2) critical activation selection (cite14†§3.2 ), which further refines RCNs based on activation polarity variations; (3) adaptive intervention (cite15†§3.3 ), which enhances the reliability of steering by predicting reasoning failures and performing adaptive interventions.
L117: #### Finding 1. LLM reasoning traces leading to correct versus incorrect answers exhibit distinct activation patterns.
L118: As shown in Figure cite99†2 , we compare the mean activations of highly contrastive neurons under successful and failed reasoning. Notably, the 3028-th neuron in layer 27 shows substantially higher activation during successful reasoning, whereas the 246-th and 1908-th neurons in layer 26 exhibit the opposite trend. This indicates that specific neurons capture informative signals associated with reasoning success at test time.
L119: #### Finding 2. Token-level neuron activations are predictive of the final correctness of LLM reasoning.
L120: 
L121: As reported in Table cite100†1 , probing classifiers trained solely on last-token activations achieve AUROC scores around 0.7 across two datasets and two models, reaching up to 0.76 on AIME with the Qwen3-1.7B model. These observations suggest that neuron activation states are systematically correlated with reasoning outcomes.
L122: ## 3 Methodology
L123: Figure cite101†3 overviews our AdaRAS framework. First, we identify RCNs by contrasting activation patterns from correct and incorrect reasoning samples (cite13†§3.1 ). Then, we apply sparse activation steering to selectively intervene on these neurons (cite14†§3.2 ). To avoid perturbing already-correct reasoning, we introduce an adaptive intervention strategy that conditionally modulates activations at test time (cite15†§3.3 ).
L124: Finally, we describe the construction of parallel reasoning traces used in our experiments (cite16†§3.4 ).
L125: ### 3.1 Reasoning Neuron Identification
L126: We identify reasoning-critical neurons (RCNs) by directly contrasting activation patterns between correct and incorrect reasoning trajectories. While probing-based methods can assign neuron importance via classifier weights, we find them unreliable in practice due to their sensitivity to feature selection and dependence on probe generalization. Following prior works (cite90†Rimsky et al., 2024 ), we therefore adopt a probing-free, activation-level criterion based on mean activation differences.
L127: Let $a_{i}^{l}(t)$ denote the activation value of neuron $i$ at layer $l$ for token $t$. Given paired correct and incorrect reasoning traces $\mathcal{P}=\{(p_{k}^{+},p_{k}^{-})\}_{k=1}^{N}$, we define the reasoning-critical score of neuron $(l,i)$ as the difference in mean activations:
L128: 
L129:  | $$\begin{gathered}S(l,i)=\EV_{k\sim[N]}\Big[\mu(a_{i}^{l},p_{k}^{+})-\mu(a_{i}^{l},p_{k}^{-})\Big],\\
L130: \mu(a,p)\triangleq\frac{1}{|p|}\sum_{t\in p}a(t),\end{gathered}$$  |  | (1)
L131: where $|p|$ denotes the length of the reasoning trace. Unlike prior works (cite90†Rimsky et al., 2024 ) which adopt token-level MD applied to the final answer, this global formulation captures sustained activation patterns accumulated throughout the reasoning process. Specifically, for each layer $l$, the scores of all neurons form a layer-wise vector $\mathbf{S}_{l}=[S(l,1),\dots,S(l,d)]^{\top}$, which serves as the steering direction for test-time intervention.
L132: ### 3.2 Critical Activation Selection
L133: From preliminary results, our key observation is that correct reasoning is supported by structured activation patterns formed by a small subset of neurons, rather than uniformly distributed across entire layers. Therefore, instead of intervening at the layer level, we perform neuron-level selection and steering. Specifically, most modern LLMs, such as LLaMA and Qwen, employ SwiGLU activations (cite102†Shazeer, 2020 ), whose signed output is necessary for representations learning (cite103†Huang, 2024 ).
L134: Our empirical analysis also reveals that neurons whose average activation polarity differs between correct and incorrect reasoning trajectories are particularly discriminative (see cite28†4.4 for detailed results). Intuitively, such polarity reversals indicate neurons that actively support or suppress valid reasoning, depending on the reasoning outcome.
L135: Formally, for each neuron $(l,i)$, we retain it for steering only if
L136: 
L137:  | $$\EV_{k}\!\left[\mu(a_{i}^{l},p_{k}^{+})\right]\cdot\EV_{k}\!\left[\mu(a_{i}^{l},p_{k}^{-})\right]<0,$$  |  | (2)
L138: i.e., its mean activation exhibits a sign flip between correct and incorrect traces. This polarity-based filtering yields a sparse candidate set of RCNs. We then rank the retained neurons by the magnitude of their importance scores $|S(l,i)|$ and select the top-$K$ neurons to construct a sparse steering vector $\bm{S}^{\prime}_{l}$ for each layer. The steering strength is controlled by a positive scalar $\alpha\in[0,\infty]$. Activation steering is applied within the MLP block of the LLM:
L139:  | $$\mathbf{h}^{l}=\mathbf{h}^{l-1}+\mathbf{W}_{down}^{l}\left(\phi(\mathbf{W}_{up}^{l}\mathbf{h}^{l-1})+\alpha\bm{S}^{\prime}_{l}\right),$$  |  | (3)
L140: 
L141: where $\bm{S}^{\prime}_{l}$ is constructed once from a reference dataset and applied uniformly at each decoding step during test-time inference.


## jan29_stdvisioneval1

Identifying and Transferring Reasoning-Critical Neurons: Improving LLM Inference Reliability via Activation Steering (https://arxiv.org/html/2601.19847v1)
citeturn28476view2 [wordlim: 200] Crawled: today; Content type: text/html; Source: open({"ref_id":"https://arxiv.org/html/2601.19847v1","lineno":144}); Total lines: 605
L133: From preliminary results, our key observation is that correct reasoning is supported by structured activation patterns formed by a small subset of neurons, rather than uniformly distributed across entire layers. Therefore, instead of intervening at the layer level, we perform neuron-level selection and steering. Specifically, most modern LLMs, such as LLaMA and Qwen, employ SwiGLU activations (cite102†Shazeer, 2020 ), whose signed output is necessary for representations learning (cite103†Huang, 2024 ).
L134: Our empirical analysis also reveals that neurons whose average activation polarity differs between correct and incorrect reasoning trajectories are particularly discriminative (see cite28†4.4 for detailed results). Intuitively, such polarity reversals indicate neurons that actively support or suppress valid reasoning, depending on the reasoning outcome.
L135: Formally, for each neuron $(l,i)$, we retain it for steering only if
L136: 
L137:  | $$\EV_{k}\!\left[\mu(a_{i}^{l},p_{k}^{+})\right]\cdot\EV_{k}\!\left[\mu(a_{i}^{l},p_{k}^{-})\right]<0,$$  |  | (2)
L138: i.e., its mean activation exhibits a sign flip between correct and incorrect traces. This polarity-based filtering yields a sparse candidate set of RCNs. We then rank the retained neurons by the magnitude of their importance scores $|S(l,i)|$ and select the top-$K$ neurons to construct a sparse steering vector $\bm{S}^{\prime}_{l}$ for each layer. The steering strength is controlled by a positive scalar $\alpha\in[0,\infty]$. Activation steering is applied within the MLP block of the LLM:
L139:  | $$\mathbf{h}^{l}=\mathbf{h}^{l-1}+\mathbf{W}_{down}^{l}\left(\phi(\mathbf{W}_{up}^{l}\mathbf{h}^{l-1})+\alpha\bm{S}^{\prime}_{l}\right),$$  |  | (3)
L140: 
L141: where $\bm{S}^{\prime}_{l}$ is constructed once from a reference dataset and applied uniformly at each decoding step during test-time inference.
L142: ### 3.3 Adaptive Intervention Strategy
L143: Our early experiments shown a trade-off in activation steering: while it effectively rectifies incorrect reasoning, it inadvertently degrade performance on some originally correct samples. To address this, we introduce a lightweight failure prediction module that adaptively gates steering at test time. Specifically, we formulate a prediction task to estimate whether the base model can correctly answer a given input.
L144: The predictor operates on early neuron activations induced by the input prompt, which capture the model’s initial reasoning state. To reduce dimensionality, we select a small set of activations using $F$-statistics method as the input features. A attention-based classifier is then trained on these features and achieves an AUROC of 0.8347 on AIME dataset, which further supports our insights that there exists a strong correlation between activation patterns and reasoning outcomes.
L145: During inference, the predictor serves as a gate: AdaRAS is applied only when a reasoning failure is predicted. This adaptive intervention improves overall reasoning reliability while preserving performance on inputs that are already correctly handled.
L146: ### 3.4 Contrastive Data Construction
L147: As mentioned in Section cite13†3.1 , identifying RCNs requires contrastive reasoning traces that share the same input but differ in outcome correctness. To this end, we construct paired positive and negative reasoning trajectories via self-sampling. For each input prompt, we sample multiple reasoning trajectories using high-temperature decoding and partition them into positive and negative sets based on answer correctness.
L148: Contrastive pairs are then formed by matching traces with identical inputs but opposite outcomes. Aggregating all pairs yields a contrastive reasoning set $\mathcal{P}=\{(p^{+},p^{-})\}$, which is used to identify and transfer RCN activations.
L149: Table 2: Experimental results on mathematics and coding benchmarks. We compare AdaRAS with probing-based steering and post-training baselines, evaluated using the Accuracy metric. Bold numbers denote the best performance on each dataset. Red subscripts indicate the improvement of AdaRAS over the CoT prompting.
L150: Task  | Dataset  |  | Post-training  | Steering
L151: CoT  | R1-Distill  | Nemotron  | OpenThinker  | Probing  | AdaRAS
L152: Math  | AIME-24  | 47.83  | 34.78  | 39.13  | 26.08  | 43.48  | 60.87${}_{{\color[rgb]{0.7422,0.2891,0.3398}{\textbf{+13.04}}}}$
L153: AIME-25  | 40.91  | 22.73  | 40.91  | 50.00  | 50.00  | 54.55${}_{{\color[rgb]{0.7422,0.2891,0.3398}{\textbf{+13.64}}}}$
L154: AIME-Extend  | 47.33  | 21.33  | 47.33  | 42.67  | 48.00  | 52.67${}_{{\color[rgb]{0.7422,0.2891,0.3398}{\textbf{+5.34}}}}$
L155: MATH-500  | 84.80  | 66.20  | 85.40  | 82.00  | 85.40  | 86.40${}_{{\color[rgb]{0.7422,0.2891,0.3398}{\textbf{+1.60}}}}$
L156: GSM8K  | 88.32  | 72.93  | 87.57  | 67.55  | 88.32  | 89.08${}_{{\color[rgb]{0.7422,0.2891,0.3398}{\textbf{+0.76}}}}$
L157: AMC-12  | 65.93  | 41.76  | 65.93  | 53.85  | 73.63  | 70.33${}_{{\color[rgb]{0.7422,0.2891,0.3398}{\textbf{+4.40}}}}$
L158: Code  | HumanEval  | 77.18  | 45.64  | 57.72  | 59.06  | 77.85  | 79.19${}_{{\color[rgb]{0.7422,0.2891,0.3398}{\textbf{+2.01}}}}$
L159: HumanEval+  | 69.80  | 42.95  | 51.68  | 53.69  | 72.48  | 73.15${}_{{\color[rgb]{0.7422,0.2891,0.3398}{\textbf{+3.35}}}}$
L160: MBPP  | 68.78  | 42.59  | 53.97  | 35.71  | 70.37  | 72.22${}_{{\color[rgb]{0.7422,0.2891,0.3398}{\textbf{+3.44}}}}$
L161: MBPP+  | 58.20  | 37.30  | 43.92  | 30.95  | 59.52  | 60.58${}_{{\color[rgb]{0.7422,0.2891,0.3398}{\textbf{+2.38}}}}$
L162: ## 4 Experiments
L163: 
L164: ### 4.1 Experimental Setup
L165: #### Dataset.
L166: We evaluate AdaRAS on mathematics and coding benchmarks, as both tasks require coherent reasoning traces. We consider 10 widely used datasets. For those without an official training split, we sample a small subset of the test data as a probing set. For each probing sample, we generate 4 paired of positive and negative reasoning traces, which are used for RCNs identification. The remaining samples are reserved for test-time steering evaluation, with no overlap with probing set.
L167: Table cite104†8 summarizes the statistics of these datasets.
L168: #### Baseline.
L169: We compare AdaRAS with the following baselines: (1) Chain-of-Thought (CoT). We include the vanilla CoT prompting performance of Qwen3-1.7B as a baseline, on which AdaRAS is applied. (2) Post-trained reasoning models. Post-training methods (e.g., SFT, PPO, GRPO) are known to enhance model’s reasoning performance.
L170: We therefore consider three publicly available post-trained models with comparable scales: DeepSeek-R1-Distill-Qwen-1.5B (cite70†DeepSeek-AI, 2025 ), OpenThinker-3-1.5B (cite105†Guha et al., 2025 ), and OpenReasoning-Nemotron-1.5B (cite106†Ahmad et al., 2025 ). (3) Probing-based steering.
L171: We use the weights of the probing classifier trained in cite9†§2.2 as neuron importance scores, select the same number of top-ranked neurons as in AdaRAS, and perform activation addition steering (cite88†Turner et al., 2023 ) accordingly. This baseline is denoted as Probing.
L172: #### Evaluation.
L173: 
L174: We use greedy decoding (i.e., generation temperature = 0) for all methods to ensure reproducibility. Following prior work, we report Accuracy as the evaluation metric across all datasets.
L175: 
L176: ### 4.2 Main Results
L177: 
L178: Table cite107†2 reports the reasoning performance improvement of AdaRAS on ten benchmarks, compared against the base model and post-training methods.


## jan29_stdvisioneval2

Identifying and Transferring Reasoning-Critical Neurons: Improving LLM Inference Reliability via Activation Steering (https://arxiv.org/html/2601.19847v1)
citeturn28477view2 [wordlim: 200] Crawled: today; Content type: text/html; Source: open({"ref_id":"https://arxiv.org/html/2601.19847v1","lineno":194}); Total lines: 605
L172: #### Evaluation.
L173: 
L174: We use greedy decoding (i.e., generation temperature = 0) for all methods to ensure reproducibility. Following prior work, we report Accuracy as the evaluation metric across all datasets.
L175: 
L176: ### 4.2 Main Results
L177: 
L178: Table cite107†2 reports the reasoning performance improvement of AdaRAS on ten benchmarks, compared against the base model and post-training methods.
L179: #### AdaRAS consistently improves reasoning correctness across all datasets, even surpassing post-trained LLMs.
L180: On average, AdaRAS achieves an improvement of $\sim$5% over CoT-based inference. Notably, on the challenging AIME-25 benchmark, AdaRAS yields a substantial gain of 13.64%, surpassing all existing open-source post-trained models of comparable scale. We further observe that the performance gains introduced by AdaRAS are more pronounced on hard reasoning benchmarks, such as AIME and AMC.
L181: On these datasets, AdaRAS achieves an average improvement of 9.11%, compared to a more modest gain of 2.26% on relatively easier benchmarks. These results suggest that steering RCN activations toward favorable states can substantially enhance the reliability of the generation process, particularly for complex and cognitively demanding reasoning tasks.
L182: #### Probing-based activation steering is inherently unstable.
L183: As shown in Table cite107†2 , vanilla probing-based steering yields mixed results across datasets. While it achieves notable gains on AMC-12, even surpassing AdaRAS, it fails to generalize and can be detrimental on more challenging benchmarks. In particular, on AIME-24, probing-based steering degrades accuracy by 4.35% compared to the unsteered CoT baseline.
L184: These results indicate that naive probing-based approaches are highly sensitive to neuron selection, and may harm reasoning performance without adaptive intervention mechanisms, which are explicitly addressed in AdaRAS.
L185: Table 3: Transferability results of AdaRAS across datasets. We compare in-domain steering using RCNs identified on each dataset (ID. RCNs) with cross-dataset steering using RCNs identified on AIME (AIME-RCNs).
L186: Dataset  | ID. RCNs  | AIME-RCNs
L187: MATH-500  | 86.40  | 87.40
L188: GSM8K  | 89.08  | 89.39
L189: AMC-12  | 70.33  | 71.43
L190: HumanEval  | 79.19  | 80.54
L191: HumanEval+  | 73.15  | 73.15
L192: MBPP  | 72.22  | 72.75
L193: MBPP+  | 60.58  | 61.11
L194: ### 4.3 Generalizability
L195: 
L196: Tables cite108†3 and cite109†4 further evaluate AdaRAS in the views of transferability and generalization, covering cross-dataset setting and larger model scale.
L197: #### RCNs exhibit strong cross-dataset and cross-task transferability.
L198: As shown in Table cite108†3 , compared to using dataset-specific RCNs, we observe that cross-dataset activation steering with RCNs identified on AIME consistently yields better performance, resulting in small but stable gains, within 1%, across all evaluated datasets. Notably, these RCNs also transfer across task domains: when applied to coding benchmarks, they continue to improve performance.
L199: These results support our motivation for identifying RCNs and suggest that such neurons capture task-agnostic reasoning mechanisms. In particular, RCNs identified from more challenging tasks appear to generalize broadly to diverse reasoning settings.
L200: Table 4: Scalability results of AdaRAS on Qwen3-4B. We evaluate AdaRAS on a larger base model using cross-dataset steering with RCNs identified on AIME.
L201: Dataset  | Qwen3-4B  | +AdaRAS
L202: AIME-24  | 56.52  | 60.87
L203: AIME-25  | 59.09  | 72.73
L204: AIME-Extend  | 68.67  | 76.67
L205: MATH-500  | 90.00  | 91.20
L206: GSM8K  | 92.72  | 93.93
L207: AMC-12  | 76.92  | 80.22
L208: HumanEval  | 91.28  | 92.62
L209: HumanEval+  | 81.88  | 84.56
L210: MBPP  | 79.37  | 82.28
L211: MBPP+  | 68.78  | 69.31
L212: #### AdaRAS scales effectively to stronger reasoning models.
L213: Table cite109†4 shows that AdaRAS continues to yield performance improvements when applied to the larger and more capable reasoning model. Even when the base model already achieves high accuracy, whereas Qwen3-4B surpasses 90% accuracy on relatively easier benchmarks such as MATH-500, GSM8K, and HumanEval, AdaRAS still delivers consistent accuracy gains of around 1%.
L214: Notably, on more challenging datasets such as AIME, the improvements are more pronounced, mirroring the trends observed in previous experiments. Overall, these results indicate that AdaRAS acts as a complementary test-time intervention, providing consistent gains even as the base model’s reasoning capability improves.
L215: ### 4.4 Ablation Studies
L216: Table cite110†5 reports the ablation results for AdaRAS. (1) Random Steering consistently degrades performance, indicating that indiscriminate neuron intervention is harmful. (2) Removing the MD-based estimation results in the sharpest decline on AIME-24 (i.e., 60.87% $\to$ 43.48%), dropping even below the unsteered baseline. This underscores the necessity of MD for accurately identifying RCNs.
L217: (3) Disabling polarity-based activation selection causes an approximate 10% accuracy drop on both AIME-24 and AIME-25, highlighting the importance of discriminative activation polarity; limited by space, further analysis is in Appendix cite58†E.2 . (4) Omitting adaptive intervention degrades overall performance by interfering with originally correct reasoning trajectories. Overall, all components are essential to the effectiveness of AdaRAS.
L218: Table 5: Ablation results of key components in AdaRAS. Random Steering applies steering to randomly sampled neurons. AdaRAS w/o MD reduces the method to probing-based neuron importance estimation, instead of Mean Difference designed in cite13†§3.1 . AS and AI denote Activation Selection and Adaptive Intervention, corresponding to the designs in cite14†§3.2 and cite15†§3.3 , respectively.
L219: Method  | AIME-24  | AIME-25
L220: Qwen3-1.7B  | 47.83  | 40.91
L221: Random Steering  | 34.78  | 27.27
L222: AdaRAS w/o MD  | 43.48  | 50.00
L223: AdaRAS w/o AS  | 52.17  | 45.45
L224: AdaRAS w/o AI  | 56.52  | 45.45
L225: AdaRAS  | 60.87  | 54.55
L226: ## 5 Analysis
L227: 
L228: (a) Intervention strength $\alpha$
L229: 
L230: (b) Top-$K$ neurons
L231: 
L232: Figure 4: Effect of hyperparameter.
L233: 
L234: cite111†Image: Refer to caption (a) Probing-based steering
L235: 
L236: cite112†Image: Refer to caption (b) AdaRAS
L237: 
L238: Figure 5: Visualization of activation shifts induced by steering. Neurons are sorted by their indices in layer, and unsteered neurons are omitted for clarity.
L239: ### 5.1 Effect of Hyperparameter
L240: 
L241: To further examine the design of AdaRAS, we analyze its hyperparameters. Specifically, we vary the intervention strength $\alpha$ in Eq. cite113†3 within $[0,1]$, which controls the magnitude of activation shifts toward the identified RCNs. We also vary the number of selected neurons to empirically assess the sparsity assumption of RCNs introduced in cite14†§3.2 .
L242: #### Effect of intervention strength.
L243: As shown in Figure cite114†4(a) , AdaRAS achieves peak performance at $\alpha=0.3$ on AIME-24 and $\alpha=0.4$ on AIME-25. Increasing $\alpha$ beyond these values leads to performance decline, suggesting that excessive intervention interferes with the model’s reasoning process. Notably, performance drops to the unsteered baseline only when $\alpha=0.7$ on AIME-24.


## jan29_stdvisionsettingsroute

Identifying and Transferring Reasoning-Critical Neurons: Improving LLM Inference Reliability via Activation Steering (https://arxiv.org/html/2601.19847v1)
citeturn28478view1 [wordlim: 200] Crawled: today; Content type: text/html; Source: find({"ref_id":"https://arxiv.org/html/2601.19847v1","pattern":"A.2"}); Total lines: 605
L36:       1. cite26†RCNs exhibit strong cross-dataset and cross-task transferability. L37:       2. cite27†AdaRAS scales effectively to stronger reasoning models. L38:     4. cite28†4.4 Ablation Studies L39:   6. cite29†5 Analysis L40:     1. cite30†5.1 Effect of Hyperparameter L41:       1. cite31†Effect of intervention strength. L42:       2. cite32†Effect of top-$K$ RCNs selection. L43:     2. cite33†5.2 Visualization of Steering L44:       1. cite34†AdaRAS mainly intervenes on later layer neurons. L45:       2. cite35†AdaRAS stabilizes latent reasoning trajectories without altering semantic modeling. L46:   7. cite36†6 Related Works L47:     1. cite37†Reasoning Reliability. L48:     2. cite38†Mechanistic Interpretability. L49:   8. cite39†7 Conclusion L50:   9. cite40†References L51:   10. cite41†A Preliminary Study of Probing L52:     1. cite42†A.1 Data Construction L53:     2. cite43†A.2 Preprocessing L54:     3. cite44†A.3 Probing Classifier L55:   11. cite45†B Detailed Data Statistics L56:     1. cite46†B.1 Data for Adaptive Intervention Module L57:     2. cite47†B.2 Data for Evaluation L58:   12. cite48†C Details of Implementation L59:     1. cite49†C.1 Adaptive Intervention Module L60:     2. cite50†C.2 Evaluation L61:       1. cite51†Mathematic Benchmarks. L62:       2. cite52†Coding Benchmarks. L63:   13. cite53†D Details of Reasoning Features L64:     1. cite54†Sequence-Averaged Magnitude ($\bar{\mathcal{M}}$). L65:     2. cite55†Sequence-Averaged Angle ($\bar{\mathcal{A}}$). L66:   14. cite56†E Additional Analysis Experiments L67:     1. cite57†E.1 Separability of Reasoning Trajectories in Latent Space L68:     2. cite58†E.2 Empirical Result of Polarity of Neuron Activations L69:   15. cite59†F Case Study L70:     1. cite60†Problem: L71:     2. cite61†Analysis: L72:     3. cite62†Problem: L73:     4. cite63†Analysis: L74:     5. cite64†Problem: L75:     6. cite65†Analysis: L76: cite66†License: arXiv.org perpetual non-exclusive license†info.arxiv.org L77: 
L78: arXiv:2601.19847v1 [cs.CL] 27 Jan 2026
L79: # Identifying and Transferring Reasoning-Critical Neurons: Improving LLM Inference Reliability via Activation Steering
L80: Fangan Dong Affiliation: Shandong University Email: fangan.dong@mail.sdu.edu.cn    Zuming Yan Affiliation: Shandong University Email: yingzhou@sdu.edu.cn    Xuri Ge Affiliation: Shandong University    Zhiwei Xu Affiliation: Shandong University    Mengqi Zhang Affiliation: Shandong University    Xuanang Chen Affiliation: Institute of Software, Chinese Academy of Sciences    Ben He, Xin Xin, Zhumin Chen, Ying Zhou ^{†}^{†}thanks: Corresponding author.
L358: We utilize Qwen3-32B to generate contrastive reasoning trajectories. Specifically, starting from all AIME (24+25) and AMC-12 problems, we sample 8 reasoning traces per question using a generation temperature of 1.0. We retain only those questions that yield a balanced outcome of exactly 4 correct and 4 incorrect trajectories.
L359: Under this setting, we obtain 15 AIME problems (from an initial 60) and 13 AMC-12 problems (from an initial 104), resulting in 120 and 104 samples, respectively, for probing classifier training.
L360: ### A.2 Preprocessing
L361: 
L362: For each reasoning trace, we extract last-token activations across all neurons as input features for the probing classifier. Specifically:
L363: 
L364:   * •
L365: 
L366: Source: Hidden states of the last token in the reasoning path, immediately before final answer generation.
L367: 
L368:   * •
L369: 
L370: Position: Post-activation outputs of the MLP blocks (i.e., after the SwiGLU activation for Qwen3 series model).
L371: 
L372:   * •
L373: Dimension: Activations from all transformer layers are concatenated into a single feature vector of dimension $L\times d_{\text{mlp}}$, where $L$ denotes the number of layers.
L374: 
L375:   * •
L376: 
L377: Normalization: Feature values are scaled by dividing by $10\times\sigma$, where $\sigma$ is the standard deviation for each neuron computed over the training set.
L378: ### A.3 Probing Classifier
L379: Given the high dimensionality of the activation space relative to the training sample size, feature selection is critical to mitigate overfitting. We rank neurons using the ANOVA $F$-statistic (sklearn.f_classif) based on their linear association with the correctness label, and select the top-$K$ neurons with $K=131{,}072$. For the probing classifier, we employed a Logistic Regression model with L1 regularization. The model was trained using 5-fold cross-validation with a stratified 4:1 train-test split.
L380: The detailed settings are summarized in Table cite254†6 .
L381: 
L382: Table 6: Implementation details of probing classifier.
L383: Setting  | Configuration / Value
L384: Feature
L385: Source  | Last token of reasoning path
L386: Position  | MLP post-activation output
L387: Scope  | Global (all layers)
L388: Normalization  | Scaled by $1/(10\times\text{std}_{\text{train}})$
L389: Feature Selection  | ANOVA $F$-statistic
L390: Dimension of Input  | 131,072
L391: Training
L392: Architecture  | Logistic Regression (sklearn)
L393: Regularization  | L1 (Lasso)
L394: Solver  | SAGA
L395: Class Weight  | Balanced
L396: Penalty Strength  | Grid search $\in[10^{-4},10]$
L397: Max Iterations  | 50
L398: Random Seed  | 42


## jan29_stdvisionnecessary3

Identifying and Transferring Reasoning-Critical Neurons: Improving LLM Inference Reliability via Activation Steering (https://arxiv.org/html/2601.19847v1)
citeturn28479view0 [wordlim: 200] Crawled: today; Content type: text/html; Source: open({"ref_id":"https://arxiv.org/html/2601.19847v1","lineno":399}); Total lines: 605
L360: ### A.2 Preprocessing
L361: 
L362: For each reasoning trace, we extract last-token activations across all neurons as input features for the probing classifier. Specifically:
L363: 
L364:   * •
L365: 
L366: Source: Hidden states of the last token in the reasoning path, immediately before final answer generation.
L367: 
L368:   * •
L369: 
L370: Position: Post-activation outputs of the MLP blocks (i.e., after the SwiGLU activation for Qwen3 series model).
L371: 
L372:   * •
L373: Dimension: Activations from all transformer layers are concatenated into a single feature vector of dimension $L\times d_{\text{mlp}}$, where $L$ denotes the number of layers.
L374: 
L375:   * •
L376: 
L377: Normalization: Feature values are scaled by dividing by $10\times\sigma$, where $\sigma$ is the standard deviation for each neuron computed over the training set.
L378: ### A.3 Probing Classifier
L379: Given the high dimensionality of the activation space relative to the training sample size, feature selection is critical to mitigate overfitting. We rank neurons using the ANOVA $F$-statistic (sklearn.f_classif) based on their linear association with the correctness label, and select the top-$K$ neurons with $K=131{,}072$. For the probing classifier, we employed a Logistic Regression model with L1 regularization. The model was trained using 5-fold cross-validation with a stratified 4:1 train-test split.
L380: The detailed settings are summarized in Table cite254†6 .
L381: 
L382: Table 6: Implementation details of probing classifier.
L383: Setting  | Configuration / Value
L384: Feature
L385: Source  | Last token of reasoning path
L386: Position  | MLP post-activation output
L387: Scope  | Global (all layers)
L388: Normalization  | Scaled by $1/(10\times\text{std}_{\text{train}})$
L389: Feature Selection  | ANOVA $F$-statistic
L390: Dimension of Input  | 131,072
L391: Training
L392: Architecture  | Logistic Regression (sklearn)
L393: Regularization  | L1 (Lasso)
L394: Solver  | SAGA
L395: Class Weight  | Balanced
L396: Penalty Strength  | Grid search $\in[10^{-4},10]$
L397: Max Iterations  | 50
L398: Random Seed  | 42
L399: Validation  | 5-fold cross-validation
L400: Metric  | AUROC
L401: ## Appendix B Detailed Data Statistics
L402: ### B.1 Data for Adaptive Intervention Module
L403: The adaptive intervention module is a binary classifier that predicts whether a given input is likely to fail under the base model and therefore requires intervention. Training data are constructed by sampling the base model on the training split for each benchmarks. Samples answered correctly are labeled as negative (i.e., no need for intervention), while incorrect samples are labeled as positive (i.e., intervention required). Dataset statistics are summarized in Table cite255†7 .
L404: Notably, for AMC-12 and HumanEval, we evaluate them only in a transfer setting using estimators trained on AIME and MBPP, due to lacking of training split; consequently, they are omitted from Table cite255†7 .
L405: Table 7: Statistics of the training and validation data for the adaptive intervention module.
L406: 
L407: Dataset  | Total Samples  | Number of each label (Train / Val)
L408: No Intervention  | Need Intervention
L409: AIME  | 828  | 392 / 99  | 270 / 67
L410: MATH  | 1,000  | 622 / 270  | 78 / 30
L411: GSM8K  | 1,700  | 1,097 / 459  | 103 / 41
L412: MBPP  | 163  | 83 / 29  | 37 / 14
L413: ### B.2 Data for Evaluation
L414: 
L415: We evaluate AdaRAS on a diverse set of benchmarks, where the dataset statistics are summarized in Table cite104†8 . All datasets are publicly available. Specifically, GSM8K, MATH, MBPP, and HumanEval are distributed under open licenses (i.e., MIT or Apache 2.0). The AIME and AMC datasets are sourced from public academic benchmarks widely accepted for evaluating mathematical reasoning. We split the datasets as follows:
L416: 
L417:   * •
L418: AIME. A unified set of samples is applied across all AIME datasets (2024, 2025, and Extend). This set contains 15 held-out samples (7 from AIME-24 and 8 from AIME-25), which are strictly excluded from all evaluation sets.
L419: 
L420:   * •
L421: 
L422: AMC-12, HumanEval. Since these datasets do not provide official training splits, we reserve a small subset from the test split for performing AdaRAS. For example, we hold out 15 HumanEval samples for RCNs identification and evaluate on the remaining 149 samples.
L423: 
L424:   * •
L425: Other datasets. For benchmarks with official training splits (GSM8K, MATH, MBPP), patterns are extracted exclusively from the training set.
L426: 
L427: Table 8: Statistics of datasets. #Probe indicates the number of samples used for identifying RCNs by AdaRAS.
L428: Dataset  | #Probe  | #Test  | Test split
L429: Mathematic
L430: AIME-24^{1}  | 7  | 23  | Self-split
L431: AIME-25^{2}  | 8  | 22  | Self-split
L432: AIME-Extend^{3}  | 15  | 150  | Official
L433: MATH-500^{4}  (cite121†Lightman et al., 2024 )  | 15  | 500  | Official
L434: GSM8K^{5}  (cite256†Hendrycks et al., 2021 )  | 15  | 1,319  | Official
L435: AMC-12^{6}  | 13  | 91  | Self-split
L436: Coding
L437: HumanEval^{7}  (cite257†Chen et al., 2021 )  | 15  | 149  | Self-split
L438: HumanEval+^{8}  (cite258†Liu et al., 2023 )  | 15  | 149  | Self-split
L439: MBPP^{9}  (cite259†Austin et al., 2021 )  | 15  | 378  | Official
L440: MBPP+^{10}  (cite258†Liu et al., 2023 )  | 15  | 378  | Official
L441:   * 1
L442: 
L443: cite260†https://huggingface.co/datasets/Maxwell-Jia/AIME_2024†huggingface.co L444: 
L445:   * 2
L446: 
L447: cite261†https://huggingface.co/datasets/opencompass/AIME2025†huggingface.co L448: 
L449:   * 3
L450: 
L451: cite262†https://www.kaggle.com/datasets/hemishveeraboina/aime-problem-set-1983-2024†www.kaggle.com L452: 
L453:   * 4
L454: 
L455: cite263†https://huggingface.co/datasets/HuggingFaceH4/MATH-500†huggingface.co L456: 
L457:   * 5
L458: 
L459: cite264†https://huggingface.co/datasets/openai/gsm8k†huggingface.co L460: 
L461:   * 6
L462: 
L463: cite265†https://huggingface.co/datasets/rulins/amc12_22-24†huggingface.co 

## jan29_stdvisionlast

Identifying and Transferring Reasoning-Critical Neurons: Improving LLM Inference Reliability via Activation Steering (https://arxiv.org/html/2601.19847v1)
citeturn28480view0 [wordlim: 200] Crawled: today; Content type: text/html; Source: open({"ref_id":"https://arxiv.org/html/2601.19847v1","lineno":479}); Total lines: 605
L405: Table 7: Statistics of the training and validation data for the adaptive intervention module.
L406: 
L407: Dataset  | Total Samples  | Number of each label (Train / Val)
L408: No Intervention  | Need Intervention
L409: AIME  | 828  | 392 / 99  | 270 / 67
L410: MATH  | 1,000  | 622 / 270  | 78 / 30
L411: GSM8K  | 1,700  | 1,097 / 459  | 103 / 41
L412: MBPP  | 163  | 83 / 29  | 37 / 14
L413: ### B.2 Data for Evaluation
L414: 
L415: We evaluate AdaRAS on a diverse set of benchmarks, where the dataset statistics are summarized in Table cite104†8 . All datasets are publicly available. Specifically, GSM8K, MATH, MBPP, and HumanEval are distributed under open licenses (i.e., MIT or Apache 2.0). The AIME and AMC datasets are sourced from public academic benchmarks widely accepted for evaluating mathematical reasoning. We split the datasets as follows:
L416: 
L417:   * •
L418: AIME. A unified set of samples is applied across all AIME datasets (2024, 2025, and Extend). This set contains 15 held-out samples (7 from AIME-24 and 8 from AIME-25), which are strictly excluded from all evaluation sets.
L419: 
L420:   * •
L421: 
L422: AMC-12, HumanEval. Since these datasets do not provide official training splits, we reserve a small subset from the test split for performing AdaRAS. For example, we hold out 15 HumanEval samples for RCNs identification and evaluate on the remaining 149 samples.
L423: 
L424:   * •
L425: Other datasets. For benchmarks with official training splits (GSM8K, MATH, MBPP), patterns are extracted exclusively from the training set.
L426: 
L427: Table 8: Statistics of datasets. #Probe indicates the number of samples used for identifying RCNs by AdaRAS.
L428: Dataset  | #Probe  | #Test  | Test split
L429: Mathematic
L430: AIME-24^{1}  | 7  | 23  | Self-split
L431: AIME-25^{2}  | 8  | 22  | Self-split
L432: AIME-Extend^{3}  | 15  | 150  | Official
L433: MATH-500^{4}  (cite121†Lightman et al., 2024 )  | 15  | 500  | Official
L434: GSM8K^{5}  (cite256†Hendrycks et al., 2021 )  | 15  | 1,319  | Official
L435: AMC-12^{6}  | 13  | 91  | Self-split
L436: Coding
L437: HumanEval^{7}  (cite257†Chen et al., 2021 )  | 15  | 149  | Self-split
L438: HumanEval+^{8}  (cite258†Liu et al., 2023 )  | 15  | 149  | Self-split
L439: MBPP^{9}  (cite259†Austin et al., 2021 )  | 15  | 378  | Official
L440: MBPP+^{10}  (cite258†Liu et al., 2023 )  | 15  | 378  | Official
L441:   * 1
L442: 
L443: cite260†https://huggingface.co/datasets/Maxwell-Jia/AIME_2024†huggingface.co L444: 
L445:   * 2
L446: 
L447: cite261†https://huggingface.co/datasets/opencompass/AIME2025†huggingface.co L448: 
L449:   * 3
L450: 
L451: cite262†https://www.kaggle.com/datasets/hemishveeraboina/aime-problem-set-1983-2024†www.kaggle.com L452: 
L453:   * 4
L454: 
L455: cite263†https://huggingface.co/datasets/HuggingFaceH4/MATH-500†huggingface.co L456: 
L457:   * 5
L458: 
L459: cite264†https://huggingface.co/datasets/openai/gsm8k†huggingface.co L460: 
L461:   * 6
L462: 
L463: cite265†https://huggingface.co/datasets/rulins/amc12_22-24†huggingface.co L464:   * 7
L465: 
L466: cite266†https://huggingface.co/datasets/openai/openai_humaneval†huggingface.co L467: 
L468:   * 8
L469: 
L470: cite267†https://huggingface.co/datasets/evalplus/humanevalplus†huggingface.co L471: 
L472:   * 9
L473: 
L474: cite268†https://huggingface.co/datasets/google-research-datasets/mbpp†huggingface.co L475: 
L476:   * 10
L477: 
L478: cite269†https://huggingface.co/datasets/evalplus/mbppplus†huggingface.co L479: ## Appendix C Details of Implementation
L480: 
L481: We use the following hyperparameters for AdaRAS in main experiments:
L482: 
L483:   * •
L484: 
L485: Number of top-$K$ neurons. The number of intervened neurons is fixed to $K=50$. As shown in Figure cite116†5 , these neurons are distributed across layers, with a higher concentration in middle-to-late layers.
L486: 
L487:   * •
L488: 
L489: Steering strength ($\alpha$). The best steering strength coefficient $\alpha$ is searched ranging $[0.1,0.3]$.
L490: All experiments are conducted on 4 NVIDIA A100 GPUs and 8 NVIDIA RTX 3090 GPUs.
L491: ### C.1 Adaptive Intervention Module
L492: 
L493: we adopt a lightweight attention-based classifier for adaptive intervention module. Instead of using only the last token, this module take all token activations via an attention pooling mechanism to capture the global reasoning state. Detailed specifications are provided in Table cite270†9 .
L494: 
L495: Table 9: Architecture details for the adaptive intervention module.
L496: Setting  | Configuration
L497: Architecture
L498: Structure  | Linear(256, 256) $\to$ ReLU $\to$ Dropout(0.3) $\to$ Linear(256, 1)
L499: Training
L500: Feature Selection  | ANOVA $F$-statistic
L501: Dimension of Input  | 256
L502: Optimizer  | Adam (LR=$10^{-4}$, Weight Decay=$10^{-5}$)
L503: Loss Function  | BCEWithLogitsLoss
L504: Epochs  | 100 (Early Stopping Patience=10)
L505: ### C.2 Evaluation
L506: 
L507: To ensure fair comparison and reproducibility, we use greedy decoding during inference across all benchmarks.
L508: 
L509: #### Mathematic Benchmarks.
L510: 
L511: For the AIME, MATH-500, GSM8K, and AMC-12 datasets, we use the following prompt:
L512: 
L513: #### Coding Benchmarks.
L514: 
L515: For the HumanEval and MBPP datasets, we use the following prompt:
L516: 
L517: We employed the EvalPlus (cite258†Liu et al., 2023 ) library to safely extract and execute code blocks.
L518: ## Appendix D Details of Reasoning Features
L519: In Section cite33†5.2 , we use two trajectory-level metrics, Magnitude ($\bar{\mathcal{M}}$) and Angle ($\bar{\mathcal{A}}$), to analyze the geometric properties of reasoning trajectories in latent space. As in Figure cite119†6 , each point in the kernel density estimation (KDE) plot corresponds to the aggregated $(\bar{\mathcal{M}},\bar{\mathcal{A}})$ values of a single complete reasoning trace. These metrics characterize the curvature and directional consistency of representation evolution across layers.
L520: Hidden states $\mathbf{h}\in\mathbb{R}^{d}$ are extracted from the model for each input, and the analysis is performed exclusively on generated reasoning tokens, excluding the input prompt. Following cite118†Wang et al. (2025b) , the formal definitions are as follows:
L521: #### Sequence-Averaged Magnitude ($\bar{\mathcal{M}}$).
L522: 
L523: This metric measures the “tortuosity” of the reasoning trajectory in the activation space. It is defined as the ratio of the accumulated layer-wise changes to the net change from the first to the last layer. For a single token $t$, the magnitude score $\mathcal{M}_{t}$ is computed as the $L_{2}$-norm of the difference vector between adjacent layers, normalized by the global displacement:
L524:  | $$\mathcal{M}_{t}=\frac{1}{L}\cdot\frac{\sum_{l=0}^{L-1}\|\mathbf{h}_{t}^{l+1}-\mathbf{h}_{t}^{l}\|_{2}}{\|\mathbf{h}_{t}^{L}-\mathbf{h}_{t}^{0}\|_{2}+\epsilon},$$  |  | (4)
L525: 
L526: where $\epsilon=10^{-6}$ is a small constant for numerical stability. The final sequence-averaged metric is obtained by averaging over all generated tokens:
L527: 
L528:  | $$\bar{\mathcal{M}}=\frac{1}{T}\sum_{t=1}^{T}\mathcal{M}_{t}.$$  |  | (5)
L529: A lower $\bar{\mathcal{M}}$ indicates a straighter, more direct transformation of representations through the network depth, which we associate with more stable reasoning.
L530: #### Sequence-Averaged Angle ($\bar{\mathcal{A}}$).
L531: 
L532: This metric captures the directional stability of the semantic evolution. It calculates the angular deviation between adjacent layers relative to the global angular shift. We first define the cosine similarity $\text{sim}(\mathbf{u},\mathbf{v})=\frac{\mathbf{u}\cdot\mathbf{v}}{\|\mathbf{u}\|\|\mathbf{v}\|}$. The angle score $\mathcal{A}_{t}$ for token $t$ is defined as:
L533:  | $$\mathcal{A}_{t}=\frac{1}{L}\cdot\frac{\sum_{l=0}^{L-1}\arccos\left(\text{sim}(\mathbf{h}_{t}^{l},\mathbf{h}_{t}^{l+1})\right)}{\arccos\left(\text{sim}(\mathbf{h}_{t}^{0},\mathbf{h}_{t}^{L})\right)+\epsilon}.$$  |  | (6)
L534: 
L535: Similarly, the sequence-averaged angle is computed as:
L536: 
L537:  | $$\bar{\mathcal{A}}=\frac{1}{T}\sum_{t=1}^{T}\mathcal{A}_{t}.$$  |  | (7)
L538: Larger values of $\bar{\mathcal{M}}$ or $\bar{\mathcal{A}}$ imply that the reasoning process undergoes significant fluctuations or detours in the latent space.
L539: ## Appendix E Additional Analysis Experiments
L540: ### E.1 Separability of Reasoning Trajectories in Latent Space
L541: 
L542: To further validate the motivation that correct and incorrect reasoning exhibit distinct activation patterns, we visualize the evolution of latent representations. We use the weights of the linear probing classifier trained in cite9†§2.2 to define a reference direction. Specifically, we projected the layer-wise hidden states of reasoning traces onto the direction defined by the top-$K$ most discriminative neurons identified by the probe.
L543: Figure cite271†7 illustrates the aggregated trajectories for successful and failed reasoning samples on the AIME dataset. The distinct separation between the two plots demonstrates that the latent reasoning states are linearly separable to a significant extent. Successful traces consistently maintain a high projection score, indicating stable alignment with the “correct” reasoning subspace learned by the probe. In contrast, failed traces exhibit high variance and downward drifts.
L544: This separability confirms that extracting reasoning-critical signals from activation patterns is feasible.
L545: Figure 7: Projection of reasoning states onto the probing classifier learned space. The clear separation between successful (Blue) and failed (Red) trajectories validates the separability of reasoning correctness in the activation space.
L546: ### E.2 Empirical Result of Polarity of Neuron Activations
L547: In Section cite14†3.2 , we proposed a polarity-based filtering method: constructing the steering vector by retaining only neurons that exhibit discriminative sign flips between correct and incorrect traces. To verify the necessity of this strategy, we conducted an additional ablation study on the AIME benchmarks.
L548: We compare our method against a baseline selection strategy (“Magnitude Only”) that selects the Top-$K$ neurons solely based on the absolute importance score $|S(l,i)|$, without enforcing the polarity constraint.
L549: Table cite272†10 presents the results. While selecting neurons based on magnitude alone yields performance gains over the base model (e.g., improving AIME-24 from 47.83% to 56.52%), introducing the polarity-aware filter significantly amplifies these gains. Specifically, our method achieves 60.87% on AIME-24 and 54.55% on AIME-25, consistently outperforming the magnitude-based selection.
