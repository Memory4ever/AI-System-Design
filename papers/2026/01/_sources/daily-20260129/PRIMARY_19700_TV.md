# Exact-v1 decisive primary response — 19700

Out-of-Distribution Generalization via Invariant Trajectories for Multimodal Large Language Model Editing (https://arxiv.org/html/2601.19700v1)
citeturn28470view0 [wordlim: 200] Crawled: yesterday; Content type: text/html; Source: open({"ref_id":"https://arxiv.org/html/2601.19700v1","lineno":142}); Total lines: 540
L127: Locality Risk. In order to avoid the edited concepts affecting the interpretation of unrelated content falling within the factual-shift scope, we regularize the editing process by imposing a Kullback–Leibler divergence (cite94†Attias, 1999 ) penalty between the pre- and post-edit output distributions:
L128:  | $$\scriptsize\mathcal{R}_{\text{loc}}=\mathrm{KL}\left(p_{\phi_{\text{e}}}\left(\cdot\mid\mathbf{m}_{\text{t}},\mathbf{x}_{\text{t}}\right)\|p_{\phi}\left(\cdot\mid\mathbf{m}_{\text{t}},\mathbf{x}_{\text{t}}\right)\right),\left(\mathbf{m}_{\text{t}},\mathbf{x}_{\text{t}},\mathbf{y}_{\text{t}}\right)\sim\mathcal{P}_{\text{OUT}}.$$  |  | (3)
L129: 
L130: This constraint strengthens model capacity to preserve knowledge beyond the designated editing scope, minimizing unintended side effects.
L131: Generality Risk. Previous methods (cite62†Mitchell et al., 2022 ; cite78†Zeng et al., 2024 ) mostly emphasize supervised partitioning of in-scope and out-of-scope knowledge regions, but fall short in achieving semantic generalization, and thus cause issues of causal-underfit or causal-overfit. Thus, we propose a generality risk for extracting invariant trajectories hidden underneath semantic-shift cross-modal prompting.
L132: For each edited instance $(\mathbf{m}_{\text{e}},\mathbf{x}_{\text{e}})$, we utilize its rephrase counterparts $(\mathbf{m}_{\text{r}},\mathbf{x}_{\text{r}})$ from the benchmark training datasets. Let $\boldsymbol{z}_{\phi_{e}}(\mathbf{m},\mathbf{x})$ denote the last hidden states of edited model $\mathcal{M}_{\phi_{\text{e}}}$ for prompt $(\mathbf{m},\mathbf{x})$, we retrieve the distributions of edited prompts and rephrase prompts as $\boldsymbol{Z}_{E}$ and $\boldsymbol{Z}_{R}$ respectively.
L133: Then we develop a Maximum Mean Discrepancy (MMD) (cite95†Tolstikhin et al., 2016 ) based metric learning to measure the discrepancy between in- and semantic-neighboring distributions. Given the Kernel Hilbert Space $\mathcal{H}$ associated with the Borel measurable kernel $k$, the mean embedding $\boldsymbol{\mu}_{\boldsymbol{Z}_{E}}$ and $\boldsymbol{\mu}_{\boldsymbol{Z}_{R}}$ is formulated with:
L134:  | $\displaystyle\boldsymbol{\mu}_{\boldsymbol{Z}_{E}}$  | $\displaystyle=\int_{\mathbb{S}}k(s,\cdot)\boldsymbol{Z}_{E}(ds)\in\mathcal{H},$  |  | (4)
L135:  | $\displaystyle\boldsymbol{\mu}_{\boldsymbol{Z}_{R}}$  | $\displaystyle=\int_{\mathbb{V}}k(v,\cdot)\boldsymbol{Z}_{R}(dv)\in\mathcal{H},$  |
L136: 
L137: where $s$ and $v$ are random variables with distribution $\boldsymbol{Z}_{E}$ and $\boldsymbol{Z}_{R}$. It satisfies the distribution probability density equation that for all functions $f\in\mathcal{F}$:
L138:  | $\displaystyle\mathbb{E}\left[f(S)\right]=\langle f,\boldsymbol{\mu}_{\boldsymbol{Z}_{E}}\rangle_{\mathcal{H}},\hskip 9.24994pt\mathbb{E}\left[f(V)\right]=\langle f,\boldsymbol{\mu}_{\boldsymbol{Z}_{R}}\rangle_{\mathcal{H}}.$  |  | (5)
L139: We deploy the multi-scale Gaussain kernel function $k(a_{i},a_{j})=\sum_{q=1}^{k}\exp\!\left(-\frac{\lVert a_{i}-a_{j}\rVert_{2}^{2}}{2\sigma_{q}^{2}}\right)$ in $\mathcal{H}$ to simultaneously capture local and global similarity between two instances, where $\sigma_{q}$ denotes the bandwidth of $q$-th kernel. The generality risk in the MMD form is defined as:
L140:  | $\displaystyle\mathcal{R}_{\text{gen}}=$  | $\displaystyle\mathbb{E}_{z_{\text{e}},z_{\text{e}}^{\prime}\sim\boldsymbol{Z}_{E}}\left[k(\boldsymbol{z},\boldsymbol{z}_{\text{e}}^{\prime})\right]+\mathbb{E}_{z_{\text{r}},z_{\text{r}}^{\prime}\sim\boldsymbol{Z}_{R}}\left[k(\boldsymbol{z},\boldsymbol{z}_{\text{r}}^{\prime})\right]$  |  | (6)
L141:  |  | $\displaystyle-2\mathbb{E}_{z_{\text{e}}\sim\boldsymbol{Z}_{E},z_{\text{r}}\sim\boldsymbol{Z}_{R}}\left[k(\boldsymbol{z}_{\text{e}},\boldsymbol{z}_{\text{r}})\right].$  |
L142: ### 4.3 Edit Trajectory Invariant Learning
L143: With the editing OOD formulation in Section cite10†4.1 and the overall risk composed of supervised signals on two distributional shifts in Section cite11†4.2 , we now introduce an invariant learning paradigm to discern and stabilize the edit trajectories across diverse cross-modal environments. Our goal is to optimize edited model parameters $\phi_{e}$ to minimize the risk across environments, which requires exploiting invariance and specificity in causal pathways activated by edit.
L144: Transformation into IRM Problem. To extract invariant trajectories, we invoke the IRM principle and employ a classifier $\omega$ which maps environment features to predictions (cite85†Lai & Wang, 2024 ).
L145: ###### Proposition 4.1 (Equivalence between OOD-$\omega$ and IRM).
L146: 
L147: Under the condition that the environment variability is channeled through the classifier $\omega$, it satisfies the identity $\mathcal{R}_{\text{edit}}(\phi_{e},e)\equiv\mathcal{R}_{\text{edit}}(\omega(e)\circ\phi_{e})$. The OOD editing objective in Eq.(cite96†4.1 ) admits the following equivalent IRM formulation:
L148:  | $$\min_{\phi_{e}}\max_{\omega\in\varSigma}\mathbb{E}_{(\mathbf{m}_{\text{e}},\mathbf{x}_{\text{e}},\mathbf{y}_{\text{e}})\sim\mathcal{P}_{e}(\mathbf{M},\mathbf{X},\mathbf{Y})}\mathcal{R}_{\text{edit}}(\omega(\mathbf{m}_{\text{e}},\mathbf{x}_{\text{e}},\mathbf{y}_{\text{e}})\circ\phi_{e}).$$  |
L149: ###### Proof.
L150: 
L151: The proof can be found in Appendix cite21†A.1 . ∎
L152: Invariant Learning in Editing Trajectory. Directly optimizing the OOD-$\omega$ objective is intractable due to the need to evaluate the supremum over $\mathcal{E}$. To this end, we reformulate it within a measure-theoretic framework inspired by the connection between IRM and Total Variations (TV) (cite97†Chan et al., 2006 ). The TV operator typically employed to measure the global variability bound of a function.
L153: For a function $f$ defined on a measure space $(\Omega,\mathcal{F}_{\Omega},\nu)$, the TV seminorm is given by
L154:  | $$\scriptsize TV(f):=\sup\left\{\int_{\Omega}f(\nu)\,\mathrm{div}\,g(\nu)d\nu:g\in C_{c}^{1}(\Omega,\mathbb{R}^{d}),\|g\|_{\infty}\leq 1\right\},$$  |  | (7)
L155: 
L156: where $g$ is a differentiable vector function supported compactly in $\Omega$ and $\mathrm{div}g$ denotes its divergence. Based on the Coarea Formula (cite97†Chan et al., 2006 ), the canonical TV-$\ell_{1}$ can be derived to recover a clean signal $f$ from a noisy observation $\tilde{f}$ by solving the variational problem:
L157:  | $$\small\inf_{f\in L^{2}(\Omega)}\left\{\int_{\Omega}|\nabla f|+\lambda\int_{\Omega}(f-\tilde{f})^{2}d\nu\right\}$$  |  | (8)
L158: Here, TV-$\ell_{1}$ model pres sharp discontinuities while effectively removing noise and fine-scale details. Correspondingly, we treat the environment-induced variations in the risk function $\mathcal{R}_{\text{edit}}(\omega\circ\phi_{e})$ as noise perturbing the ideal and invariant edit trajectory. The goal of editing is to denoise the risk, recovering a piecewise-constant profile that is robust to spurious cross-modal prompting changes.
L159: Inspired by (cite85†Lai & Wang, 2024 ), we further absorb TV-$\ell_{1}$ penalty into our editing IRM objective as
L160:  | $\displaystyle\min_{\phi_{e}}\{\mathbb{E}_{\omega}$  | $\displaystyle[\mathcal{R}_{\text{rel}}(\omega\circ\phi_{e})+\mathcal{R}_{\text{loc}}(\omega\circ\phi_{e})+\mathcal{R}_{\text{gen}}(\omega\circ\phi_{e})]$  |  | (9)
L161:  |  | $\displaystyle+\lambda_{\phi_{e}}\left(\mathbb{E}_{\omega}[|\nabla_{\omega}\mathcal{R}_{\text{edit}}(w\circ\phi_{e})|]\right)^{2}\}.$  |
L162: The first term represents the basic risk of editing, while the second term promotes invariance by encouraging the generalization risk to be insensitive to environmental changes. This form directly addresses the dual requirements of precise knowledge assimilation and controlled generalization.
L163: ###### Proposition 4.2 (IRM-TV objective Achieves Editing OOD with a varying $\lambda$).
L164: 
L165: The balancing parameter $\lambda$ should vary with editing parameters $\phi_{e}$ to achieve editing OOD. For each $\phi_{e}$, if $\mathbb{E}_{\omega}[|\nabla_{\omega}\mathcal{R}_{\text{edit}}(\omega\circ\phi_{e})|]>0$, there exists a non-negative $\lambda_{\phi_{e}}$, such that
L166:  | $\displaystyle\max_{e\in\mathcal{E}}$  | $\displaystyle\mathcal{R}_{\text{edit}}(\phi_{e},e)=\mathbb{E}_{\omega}[\mathcal{R}_{\text{rel}}(\omega\circ\phi_{e})+\mathcal{R}_{\text{loc}}(\omega\circ\phi_{e})+$  |  | (10)
L167:  |  | $\displaystyle\mathcal{R}_{\text{gen}}(\omega\circ\phi_{e})]+\lambda_{\phi_{e}}\left(\mathbb{E}_{\omega}[|\nabla_{\omega}\mathcal{R}_{\text{edit}}(\omega\circ\phi_{e})|]\right)^{2}.$  |
L168: Besides, the optimality of $\phi_{e}$ for IRM-TV form is equivalent to its optimality for OOD-$\omega$.
L169: ###### Proof.
L170: 
L171: The proof can be found in Appendix cite22†A.2 . ∎
L172: 
L173: Optimization on Editing IRM-TV. To solve Eq.(cite98†9 ), we treat $\lambda_{\phi_{e}}$ as a Lagrangian multiplier and parameterize it as a function $\lambda(\pi,\phi_{e})$ of both the editing model parameters $\phi_{e}$ and an auxiliary dual parameter set $\delta$. We derive the Lagrangian function for the editing IRM-TV objective as
L174:  | $\displaystyle\mathcal{G}(\delta,\phi_{e})=$  | $\displaystyle\mathbb{E}_{\omega}[\mathcal{R}_{\text{rel}}(\omega\circ\phi_{e})+\mathcal{R}_{\text{loc}}(\omega\circ\phi_{e})+\mathcal{R}_{\text{gen}}(\omega\circ\phi_{e})]]$  |  | (11)
L175:  |  | $\displaystyle+\lambda(\delta,\phi_{e})\left(\mathbb{E}_{\omega}[|\nabla_{\omega}\mathcal{R}_{\text{edit}}(\omega\circ\phi_{e})|]\right)^{2}.$  |
L176: Denote the risk sum as $\mathcal{R}_{\text{edit}}$, we derive it into a primal-dual optimization as (cite99†Wang et al., 2025 )
L177: 
L178:  |  | $\displaystyle\min_{\phi_{e}}\max_{\delta}\mathcal{G}(\delta,\phi_{e}):=\min_{\phi_{e}}\{\mathbb{E}_{\omega}[\mathcal{R}_{\text{edit}}(w\circ\phi_{e})]$  |  | (12)
L179:  |  | $\displaystyle+\max_{\delta}\left[\lambda(\delta,\phi_{e})\left(\mathbb{E}_{\omega}\left[\left|\nabla_{\omega}\mathcal{R}_{\text{edit}}(\omega\circ\phi_{e})\right|\right]\right)^{2}\right]\},$  |
L180: where the primal variable $\phi_{e}$ is optimized to minimize the overall risk, and dual variable $\delta$ is optimized to maximize the TV penalty. To solve it, an adversarial learning procedure is adopted, alternating between updating $\phi_{e}$ and $\delta$ with adaptive learning rates $\gamma_{1}$ and $\gamma_{2}$:
L181:  | $\displaystyle\phi_{e}^{(k+1)}$  | $\displaystyle=\phi_{e}^{(k)}-\gamma_{1}^{(k)}\cdot\partial_{\phi_{e}}\mathcal{G}(\delta^{(k)},\phi_{e}^{(k)}),$  |  | (13)
L182:  | $\displaystyle\delta^{(k+1)}$  | $\displaystyle=\delta^{(k)}+\gamma_{2}^{(k)}\cdot\nabla_{\delta}\mathcal{G}(\delta^{(k)},\phi_{e}^{(k+1)}).$  |
L183: The computation process of gradient $\nabla_{\delta}\mathcal{G}$ and subgradient $\partial_{\phi_{e}}\mathcal{G}$ are presented in Appendix cite26†A.3 . Consequently, after optimizing two variables, we obtain an edit model $\phi_{e}$ that is both accurate and contained while being robustly generalizable through invariant mechanisms.
L184: ## 5 Experiment
L185: ### 5.1 Experimental Setup
L186: 
L187: Table 1: Editing performance (%). Rel., Gen., T-Loc., M-Loc., denote Reliability, Generality, Text Locality, and Image Locality. The higher scores are highlighted in bold. All improvements are significant with $p$-value $<$ 0.05 based on $t$-tests.
