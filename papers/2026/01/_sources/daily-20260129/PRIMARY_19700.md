# Exact-v1 primary cached excerpts — 2601.19700

These are preserved tool responses, not author summaries. Each response is separated; its L labels are local to that response. No new fetch/revision review.

## Original response 1: latepoint0

Out-of-Distribution Generalization via Invariant Trajectories for Multimodal Large Language Model Editing (https://arxiv.org/html/2601.19700v1)
citeturn28181view2 [wordlim: 200] Crawled: yesterday; Content type: text/html; Source: open({"ref_id":"https://arxiv.org/html/2601.19700v1","lineno":null}); Total lines: 540
--------------------------------------------------------------------------------


## Original response 2: latepoint4

Out-of-Distribution Generalization via Invariant Trajectories for Multimodal Large Language Model Editing (https://arxiv.org/html/2601.19700v1)
citeturn28186view1 [wordlim: 200] Crawled: yesterday; Content type: text/html; Source: open({"ref_id":"https://arxiv.org/html/2601.19700v1","lineno":110}); Total lines: 540
L95:  | $$\small\mathcal{R}_{\text{OOD}}(f)=\max_{{\text{e}}\in\mathcal{E}_{\text{all}}}\mathbb{E}_{(\mathbf{X}^{\text{e}},\mathbf{Y}^{\text{e}})\sim\mathcal{P}^{\text{e}}}[\ell(f(\mathbf{X}^{\text{e}}),\mathbf{Y}^{\text{e}})].$$  |
L96: Here, $\mathbb{E}_{(\mathbf{X}^{\text{e}},\mathbf{Y}^{\text{e}})\sim\mathrm{P}^{\text{e}}}[\ell(f(\mathbf{X}^{\text{e}}),\mathbf{Y}^{\text{e}})]$ denotes the risk under specific environment $e$, and $\ell$ is a suitable loss function. $\mathcal{E}_{\text{all}}$ includes environments not encountered during training.
L97: Invariant Risk Minimization (IRM). IRM (cite81†Arjovsky et al., 2019 ; cite93†Tan et al., 2023 ) generalizes invariant features to different environments. Given training data as $\mathcal{D}:=\{(\mathbf{x}_{i},\mathbf{y}_{i})\in\mathcal{X}\times\mathcal{Y}\}$ where $\mathcal{X}$ and $\mathcal{Y}$ denotes the input and output space.
L98: IRM constructs the learning model $\mathcal{X}\rightarrow\mathcal{Y}$ into two parts, i.e., the feature extractor $\Psi:\mathcal{X}\rightarrow\mathcal{H}$ mapping input into the invariant feature space and the classifier $\omega:\mathcal{H}\rightarrow\mathcal{Y}$ predicting based on these features. The empirical risk under environment $e$ is:
L99:  | $$\small\mathcal{R}(\omega\circ\Psi,e)=\frac{1}{n}\sum_{i=1}^{n}\mathcal{L}(\omega\circ\Psi(\mathbf{x}_{i}),\mathbf{y}_{i},e),$$  |
L100: 
L101: where $\mathcal{L}$ is the loss function. The original IRM formulation is a bi-level optimization problem:
L102: 
L103:  | $$\small\min_{\omega,\Psi}\sum_{e\in\mathcal{E}_{tr}}\mathcal{R}(\omega\circ\Psi,e)\hskip 9.24994pt\text{s.t. }\omega\in\operatorname*{arg\,min}_{\tilde{w}}\mathcal{R}(\tilde{\omega}\circ\Psi,e),\forall e\in\mathcal{E}.$$  |
L104: This constraint requires $\omega$ to be optimal for each environment given $\Psi$, encouraging $\Psi$ to extract invariant features. Further, IRMv1 (cite81†Arjovsky et al., 2019 ) provides a surrogate form, which fixes the classifier $\omega$ to a constant scalar and replaces the constraint with a gradient norm penalty:
L105: 
L106:  | $$\min_{\Psi}\sum_{e\in\mathcal{E}}\left\{\mathcal{R}(1\circ\Psi,e)+\lambda\left\|\nabla_{\omega|_{\omega=1}}\mathcal{R}(\omega\circ\Psi,e)\right\|_{2}^{2}\right\}.$$  |
L107: ## 4 Methodology
L108: ### 4.1 Problem Setting
L109: MLLM Editing as OOD Problem. First, we formulate the knowledge editing task in a MLLM with the out-of-distribution generalization form. Considering the MLLM as a function $\mathcal{M}:\mathcal{I}\times\mathcal{X}\rightarrow\mathcal{Y}$ with parameters $\phi$, which takes the cross-modal prompt $(\mathbf{m}_{\text{e}},\mathbf{x}_{\text{e}})$ consisting of an image $\mathbf{m}_{e}$ and a textual description $\mathbf{x}_{e}$ as input, and generates $\mathbf{y}_{o}$ as the original output.
L110: Denote the editing dataset containing facts to be updated as $\mathcal{D}_{\text{edit}}$, we define an environment factor $e\in\mathcal{E}$ which parameterizes the data distribution $\mathcal{P}_{{\text{e}}}(\textbf{M},\textbf{X},\textbf{Y})$, indicating all the possible causal associations that can occur in testing prompts. The objective of MLLM editing is to update $\phi\rightarrow\phi_{\text{e}}$ for the worst-case risk $\mathcal{R}_{\text{edit}}(\phi_{\text{e}},e)$ across all conceivable environments:
L111:  | $$\small\min_{\phi_{\text{e}}}\max_{e\in\mathcal{E}}\mathbb{E}_{(\mathbf{m}_{\text{e}},\mathbf{x}_{\text{e}},\mathbf{y}_{\text{e}})\sim\mathcal{P}_{{\text{e}}}(\textbf{M},\textbf{X},\textbf{Y})}\mathcal{R}_{\text{edit}}(\phi_{\text{e}},(\mathbf{m}_{\text{e}},\mathbf{x}_{\text{e}},\mathbf{y}_{\text{e}}),e).$$  |
L112: According to existing benchmarks (cite73†Cheng et al., 2023 ; cite75†Huang et al., 2024 ; cite77†Du et al., 2025 ), the training and testing prompts $\mathcal{D}_{\text{test}}$ are composed of in-distribution data $\mathcal{D}_{\text{in}}$, semantic-neighboring data $\mathcal{D}_{\text{se}}$, and out-of-distribution data $\mathcal{D}_{\text{out}}$.
L113: The overall risk is defined as $\mathcal{R}_{\text{edit}}$, i.e., the composite measure of three editing metrics: $\mathcal{R}_{\text{rel}}$, $\mathcal{R}_{\text{gen}}$, and $\mathcal{R}_{\text{loc}}$, which respectively justify three aspects, i.e., editing accuracy on $\mathcal{D}_{\text{IN}}$, side effects on $\mathcal{D}_{\text{OUT}}$, and generalization ability on $\mathcal{D}_{\text{SE}}$ :
L114:  | $\displaystyle\mathcal{R}_{\text{rel}}:$  | $\displaystyle=\mathbb{E}_{(\mathbf{m}_{\text{e}},\mathbf{x}_{\text{e}},\mathbf{y}_{\text{e}})\sim\mathcal{P}_{\text{IN}}}\left[\mathds{1}\{\mathcal{M}(\mathbf{m}_{\text{e}},\mathbf{x}_{\text{e}};\phi_{\text{e}}),\mathbf{y}_{\text{e}})\}\right]$  |
L115:  | $\displaystyle\mathcal{R}_{\text{loc}}:$  | $\displaystyle=\mathbb{E}_{(\mathbf{m}_{\text{t}},\mathbf{x}_{\text{t}},\mathbf{y}_{\text{t}})\sim\mathcal{P}_{\text{OUT}}}\left[\mathds{1}\{\mathcal{M}(\mathbf{m}_{\text{t}},\mathbf{x}_{\text{t}};\phi_{\text{e}})=\mathcal{M}(\mathbf{m}_{\text{t}},\mathbf{x}_{\text{t}};\phi)\}\right]$  |
L116:  | $\displaystyle\mathcal{R}_{\text{gen}}:$  | $\displaystyle=\mathbb{E}_{(\mathbf{m}_{\text{r}},\mathbf{x}_{\text{r}},\mathbf{y}_{\text{r}})\sim\mathcal{P}_{\text{SE}}}\left[\mathds{1}\{\mathcal{M}(\mathbf{m}_{\text{e}},\mathbf{x}_{\text{e}};\phi_{\text{e}})=\mathcal{M}(\mathbf{m}_{\text{r}},\mathbf{x}_{\text{r}};\phi_{\text{e}}\}\right]$  |
L117: ### 4.2 Semantic-Factual Shift Disentanglement
L118: To facilitate MLLM discriminate editing environments between semantic-shift and factual-shift, we first design independent editing risks to evaluate transferability on invariant trajectories and capability to eliminate spurious factors. Our framework aims to construct a unified optimization paradigm that is agnostic to specific editing methods, so it can be incorporated into any parameter-adjusting or model-extending editing approach based on fine-tuning.
L119: With the pre-trained multimodal LLM $\mathcal{M}_{\phi}$ and editing dataset as $\mathcal{D}_{\text{edit}}$, we denote the editing model as $f_{\theta}$. Editing is cast as learning a mapping $\Gamma$ that adapts the model and its parameters guided by the edit instance and $f_{\theta}$:
L120:  | $$\small\mathcal{M}(\phi_{\text{e}},\theta_{\text{e}})=\Gamma\left(\mathcal{M}_{\phi},f_{\theta};\left(\mathbf{m}_{\text{e}},\mathbf{x}_{\text{e}},\mathbf{y}_{\text{e}}\right)\right)(\cdot),\left(\mathbf{m}_{\text{e}},\mathbf{x}_{\text{e}},\mathbf{y}_{\text{e}}\right)\sim\mathcal{P}_{\text{IN}}.$$  |  | (1)
L121: Then, to optimize the three objectives outlined in Section cite10†4.1 , i.e., reliability, locality, and generality, we propose corresponding risk metrics that are seamlessly integrated into these base editing models.
L122: 
L123: Reliability Risk. To ensure precise assimilation of the edited knowledge, we minimize the negative log-likelihood of the target output conditioned on the edit instance:
L124:  | $$\small\mathcal{R}_{\text{rel}}=-\log p_{\phi_{\text{e}}}(\mathbf{y}_{\text{e}}\mid\mathbf{m}_{\text{e}},\mathbf{x}_{\text{e}}),\hskip 9.24994pt\left(\mathbf{m}_{\text{e}},\mathbf{x}_{\text{e}},\mathbf{y}_{\text{e}}\right)\sim\mathcal{P}_{\text{IN}},$$  |  | (2)
L125: 
L126: which explicitly maximizes the probability of the desired output $\mathbf{y}_{\text{e}}$ for the edited input $(\mathbf{m}_{\text{e}},\mathbf{x}_{\text{e}})$, ensuring accurate cognition on the in-distribution cross-modal semantics.
L127: Locality Risk. In order to avoid the edited concepts affecting the interpretation of unrelated content falling within the factual-shift scope, we regularize the editing process by imposing a Kullback–Leibler divergence (cite94†Attias, 1999 ) penalty between the pre- and post-edit output distributions:
L128:  | $$\scriptsize\mathcal{R}_{\text{loc}}=\mathrm{KL}\left(p_{\phi_{\text{e}}}\left(\cdot\mid\mathbf{m}_{\text{t}},\mathbf{x}_{\text{t}}\right)\|p_{\phi}\left(\cdot\mid\mathbf{m}_{\text{t}},\mathbf{x}_{\text{t}}\right)\right),\left(\mathbf{m}_{\text{t}},\mathbf{x}_{\text{t}},\mathbf{y}_{\text{t}}\right)\sim\mathcal{P}_{\text{OUT}}.$$  |  | (3)
L129: 
L130: This constraint strengthens model capacity to preserve knowledge beyond the designated editing scope, minimizing unintended side effects.
L131: Generality Risk. Previous methods (cite62†Mitchell et al., 2022 ; cite78†Zeng et al., 2024 ) mostly emphasize supervised partitioning of in-scope and out-of-scope knowledge regions, but fall short in achieving semantic generalization, and thus cause issues of causal-underfit or causal-overfit. Thus, we propose a generality risk for extracting invariant trajectories hidden underneath semantic-shift cross-modal prompting.
L132: For each edited instance $(\mathbf{m}_{\text{e}},\mathbf{x}_{\text{e}})$, we utilize its rephrase counterparts $(\mathbf{m}_{\text{r}},\mathbf{x}_{\text{r}})$ from the benchmark training datasets. Let $\boldsymbol{z}_{\phi_{e}}(\mathbf{m},\mathbf{x})$ denote the last hidden states of edited model $\mathcal{M}_{\phi_{\text{e}}}$ for prompt $(\mathbf{m},\mathbf{x})$, we retrieve the distributions of edited prompts and rephrase prompts as $\boldsymbol{Z}_{E}$ and $\boldsymbol{Z}_{R}$ respectively.
L133: Then we develop a Maximum Mean Discrepancy (MMD) (cite95†Tolstikhin et al., 2016 ) based metric learning to measure the discrepancy between in- and semantic-neighboring distributions. Given the Kernel Hilbert Space $\mathcal{H}$ associated with the Borel measurable kernel $k$, the mean embedding $\boldsymbol{\mu}_{\boldsymbol{Z}_{E}}$ and $\boldsymbol{\mu}_{\boldsymbol{Z}_{R}}$ is formulated with:
--------------------------------------------------------------------------------

