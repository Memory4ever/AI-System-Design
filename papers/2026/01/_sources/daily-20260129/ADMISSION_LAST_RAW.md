# admissionlast

NuiWorld: Exploring a Scalable Framework for End-to-End Controllable World Generation (https://arxiv.org/html/2601.19048v1)
citeturn28127view0 [wordlim: 200] Crawled: last week; Content type: text/html; Source: open({"ref_id":"https://arxiv.org/html/2601.19048v1","lineno":130}); Total lines: 492
L124: We follow the NuiScene training procedure using the bootstrapped scenes $\mathbf{S}^{boot}$. One key modification is that we retain the color information produced by Trellis 2, storing it in the point clouds $\mathbf{P}^{boot}_{i}\in\mathbb{R}^{N_{pc}\times 6}$ which contains both the 3D coordinates and RGB values. During the training of the Chunk VAE we add an additional color prediction head implemented via CA and FC layers similar to the occupancy head.
L125: Color query coordinates and ground-truth color supervision are sampled from the corresponding chunk $\mathbf{P}^{boot}_{i,(u,v)}$, with RGB values supervised by an $\ell_{2}$ loss. During inference, we extract the mesh using marching cubes, sample points on the surface to query color predictions, and assign each mesh vertex the color of its nearest predicted point.
L126: Finally, we also replace DDPM (cite79†Ho et al., 2020 ) with rectified flow (cite83†Lipman et al., 2022 ) for training the quad chunk diffusion model.
L127: #### 4.1.3. Scene Synthesis Across Scales and Layout
L128: Next we sample a dataset of $Q$ scenes $\mathbf{S}^{Nui}=\{\mathbf{S}^{Nui}_{i}\}_{i=1}^{Q}$ using the trained NuiScene model. For each scene, we first sample a target area $A\in[A_{min},A_{max}]$ using log-uniform distribution. With probability $p_{square}=0.3$, we generate a square scene. Otherwise, we sample an aspect ratio $r\in[1.0,3.0]$ from a log-uniform distribution to determine the scene dimensions $(R_{i},C_{i})$ accordingly, enforcing $C_{i}\geq R_{i}\geq 15$.
L129: Here $R_{i}$ denotes the number of scene chunk rows, and $C_{i}$ corresponds to the number of chunks per row. We then render the extracted scene mesh from a fixed viewpoint at a resolution of $512\times 512$ ensuring that scenes are elongated along the horizontal axis of the image, producing a colored and colorless rendering. Each rendering is converted using two methods: canny edge (cite84†Canny, 2009 ) and cite85†Chan et al. (2022) . This results in 4 sketches per scene.
L130: Each resulting scene consists of a 2D grid of vector sets and pseudo sketches denoted as $\mathbf{S}^{Nui}_{i}=(\mathcal{V}_{i},\{\mathcal{I}^{(j)}_{i}\}_{j=1}^{4})$, where $\mathcal{V}_{i},\in\mathbb{R}^{R_{i}\times C_{i}\times V\times c}$ and $\mathcal{I}^{(j)}_{i}\in\mathbb{R}^{512\times 512\times 1}$.
L131: ### 4.2. Sketch to World Model
L132: #### 4.2.1. Model Architecture
L133: Our model aims to generate scenes $\mathcal{V}$ with variable token length $R\times C$ and a channel size of $V\times c$, conditioned on a pseudo sketch input. Here, we drop the subscript $i$ for simplicity and consider a single training sample. During training we randomly sample a sketch $\mathcal{I}$ from $\{\mathcal{I}^{(j)}\}_{j=1}^{4}$.
L134: Note that we do not choose to concatenate vector sets into the token length like in AutoPartGen (cite86†Chen et al., 2025b ), this is to avoid quadratic growth which would increase compute by $V^{2}$.
L135: Our transformer model $\textbf{w}_{\phi}$ consists of $L$ blocks each containing a self-attention, cross-attention and feed forward network as illustrated in cite52†Figure 3 . The sketch conditioning is incorporated through each cross-attention layer. Specifically the sketch $\mathcal{I}$ is encoded using a frozen DINOv2 encoder (cite87†Oquab et al., 2023 ) to obtain the token embeddings $\mathbf{z}_{sk}\in\mathbb{R}^{1374\times 1024}$ and fed to cross-attention layers.
L136: We train our model using rectified flow (cite83†Lipman et al., 2022 ). During training we sample a timestep $t\in[0,1]$ and Gaussian noise $\bm{\epsilon}\sim\mathcal{N}(0,\mathbf{I})$, and construct noisy latents as $\mathcal{V}_{t}=(1-t)\mathcal{V}_{0}+t\epsilon$, where $\mathcal{V}=\mathcal{V}_{0}$ denotes the ground-truth scene latent.
L137: Before feeding into the model, the noisy latents $\mathcal{V}_{t}$ are also added with positional embeddings and size embeddings. Each token is assigned a 2D spatial coordinate $(row,col)$, where $row\in[0,R)$ and $col\in[0,C)$ determined by the token’s location in the scene, which are encoded with sinusoidal functions. In addition, a size embedding derived from $R\times C$ and also computed with sinusoidal encoding are shared across all tokens in the scene.
L138: Both embeddings are added to $\mathcal{V}_{t}$ as input to the transformer.
L139: The model $\mathbf{w}_{\phi}$ is trained with the objective:
L140: 
L141: (1)  |  | $$\mathbb{E}_{\mathcal{V},z_{sk},\bm{\epsilon}\sim\mathcal{N}(0,\mathbf{I}),t}\left[\|\mathbf{w}_{\phi}(\mathcal{V}_{t},z_{sk},t)-(\epsilon-\mathcal{V}_{0})\|^{2}_{2}\right]$$  |
L142: 
L143: To enable classifier-free guidance during inference, the sketch conditioning $z_{sk}$ is randomly dropped with $0.2$ probability during training. The timestep $t$ is incorporated into the network via modulation, following Trellis (cite55†Xiang et al., 2025b ).
L144: #### 4.2.2. Size Prediction
L145: During inference, the scene dimensions $R$ and $C$ may not be available for a given input sketch. To address this, we learn an additional size prediction network conditioned on the input sketch. The network takes as input the CLS embedding $z_{cls}\in\mathbb{R}^{1024}$, extracted from DINOv2 given the sketch image $\mathcal{I}$, and predicts the scene dimensions $(\hat{R},\hat{C})$. We supervise training with the ground truth layout $(R,C)$.
L146: As shown cite52†Figure 3 , the predicted layout $(\hat{R},\hat{C})$ can be used to initialize the number of noisy tokens for scene generation during inference. We note that the size prediction is optional and can also be specified by the user.
L147: ## 5. Experiment
L148: 
L149: For all experiments, we train a separate model for each scenario. This is mainly due to resource constraints and enables faster development. Training models on different scenarios independently allows us to iterate more quickly and avoid long training times.
L150: ### 5.1. Dataset
L151: 
L152: We construct datasets for three scenarios: medieval, desert, and cyberpunk. Each dataset is bootstrapped using images generated by Nano Banana and reconstructed with Trellis 2, producing $M=16,12$, and $12$ initial bootstrapping scenes for each scenario, respectively. Please see the supplementary for more details. Using the boostrapped scenes, we train NuiScene with a chunk size of $s=60$.
--------------------------------------------------------------------------------
Smoothing the Score Function for Generalization in Diffusion Models:An Optimization-based Explanation Framework (https://arxiv.org/html/2601.19285v1)
citeturn28127view1 [wordlim: 200] Crawled: today; Content type: text/html; Source: open({"ref_id":"https://arxiv.org/html/2601.19285v1","lineno":241}); Total lines: 1510
L233: Conditioning vs. Unconditioning. Under our assumption, the unconditioning modeling has the same ratio formula as in cite112†Equation 7 but with a different coefficient $a$. From the property of $\sigma$-domination, we know that the unconditioning case has a smoother score function weight, leading to a smaller ratio $\gamma_{\scriptsize{ex}}$ and therefore better generalization.
L234: Temperature. We modify the weight calculations by introducing a temperature vector $T\in\mathbb{R}^{N}$ whose $i$-th component $T_{i}$ contains the temperature for shell $i$. We define $T^{*}_{j}$ to be the value of $T_{i}$ for which $\sigma_{i}=\sigma_{j}^{*}$. Generalizing cite113†Equation 5 , the temperature-based score function weight is defined as:
L235:  | $$w_{j}^{*}(\mathbf{x};T)={\frac{\exp\left(\frac{f(\mathbf{x},\mu_{j},\sigma_{j}^{*})}{T_{j}^{*}}\right)}{\sum_{l=1}^{M}\exp\left(\frac{f(\mathbf{x},\mu_{l},\sigma_{l}^{*})}{T_{l}^{*}}\right)}}.$$  |
L236: 
L237: (We recover cite113†Equation 5 by setting $T_{i}=1$, $i=1,2,\dotsc,N$.) As the $T_{i}$ increase to $\infty$, the temperature smoothing reduces the dominance ratio $a$, resulting in smaller $\gamma_{\scriptsize{ex}}$ and better generalization.
L238: ## 4 Learning the Smoothed Score Function
L239: We next describe our methods for training the neural network score functions $\mathbf{s}_{\theta}$, parametrized by weight vector $\theta$. Our noise scheduling follows the variance exploding SDE in (cite90†Song et al., 2021 ), where the noise scale $\sigma$ is sampled from a discrete set of $N$ points that approximate a log-uniform distribution over the range $[\sigma_{\text{min}},\sigma_{\text{max}}]$. The probability of selecting each $\sigma_{i}$ is equally $\frac{1}{N}$.
L240: We denote sampling from this noise schedule as $\sigma_{i}\sim p_{\sigma}$.
L241: ### 4.1 Unconditioning Score Matching
L242: 
L243: The loss function in standard noise conditioning score-based neural networks (NCSN) (cite97†Song and Ermon, 2019 ) is
L244: 
L245:  | $$\mathcal{L}_{\text{c}}=\mathbb{E}_{\mathbf{\sigma}_{i}\sim p_{\sigma}}\mathbb{E}_{\mathbf{\mu}\sim p^{*}}\mathbb{E}_{{\mathbf{x}}\sim\mathcal{N}(\mu,\sigma_{i}^{2}\mathbf{I})}\left[\frac{\sigma_{i}^{2}}{2}\left\|\mathbf{s}_{\theta}({\mathbf{x}},\sigma_{i})+\frac{{\mathbf{x}}-\mu}{\sigma_{i}^{2}}\right\|_{2}^{2}\right].$$  |  | (8)
L246: We have a similar objective function for the unconditioning modeling:
L247: 
L248:  | $$\mathcal{L}_{\text{u}}=\mathbb{E}_{\mathbf{\sigma}_{i}\sim p_{\sigma}}\mathbb{E}_{\mathbf{\mu}\sim p^{*}}\mathbb{E}_{{\mathbf{x}}\sim\mathcal{N}(\mu,\sigma_{i}^{2}\mathbf{I})}\left[\frac{\sigma_{i}^{2}}{2}\left\|\mathbf{s}_{\theta}({\mathbf{x}})+\frac{{\mathbf{x}}-\mu}{\sigma_{i}^{2}}\right\|_{2}^{2}\right].$$  |  | (9)
L249: The only difference is that we remove the noise as an input to the neural networks. Following the denoising score matching (cite96†Vincent, 2011 ), we show in cite47†Section A.6 that optimizing this loss function is equivalent to performing explicit score matching for the distribution $p_{\text{\scriptsize{MN}}}$.
L250: ### 4.2 Temperature-based Score Matching
L251: From cite114†Equation 6 and the analysis in Section cite10†3 , we know that when the noise level is small, training samples close to $\mathbf{x}$ will dominate the score function weights. Therefore, we set a threshold $\sigma_{\text{collapse}}$ to determine when we should introduce temperature scaling.
L252: When $\sigma_{i}\leq\sigma_{\text{collapse}}$, for a noisy point $\mathbf{x}$ drawn from $\mathcal{N}(\mu,\sigma_{i}^{2}\mathbf{I})$ where $\mu\sim p^{*}$, $\mu$ should be the closest training sample to $\mathbf{x}$. We can then approximate the score function using the top-$K$ nearest training samples to $\mu$, denoted by $\mu_{(j)}$, $j=1,2,\dotsc,K$, as follows:
L253:  | $$\nabla_{\mathbf{x}}\log p_{\text{\scriptsize{MN}}}(x;T)\approx\sum_{j=1}^{K}w_{(j)}^{*}(x;T)\left(-\frac{\mathbf{x}-\mu_{(j)}}{\sigma_{(j)}^{*2}}\right)$$  |  | (10)
L254: 
L255: where
L256: 
L257:  | $$\quad w_{(j)}^{*}(x;T)=\frac{\exp\left(\frac{f(\mathbf{x},\mu_{(j)},\sigma_{(j)}^{*})}{T_{(j)}^{*}}\right)}{\sum_{l=1}^{K}\exp\left(\frac{f(\mathbf{x},\mu_{(l)},\sigma_{(l)}^{*})}{T_{(l)}^{*}}\right)}.$$  |
L258: 
L259: We thus define the score matching loss to be:
L260:  | $$\mathcal{L}_{\text{T}}=\mathbb{E}_{{\mathbf{x}}\sim p_{\text{\scriptsize{MN}}}}\left[\frac{1}{2}\left\|\mathbf{s}_{\theta}({\mathbf{x}})-\nabla_{\mathbf{x}}\log p_{\text{\scriptsize{MN}}}(\mathbf{x};T)\right\|_{2}^{2}\right].$$  |
L261: 
L262: where practically we use cite115†Equation 10 to approximate $\nabla_{\mathbf{x}}\log p_{\text{\scriptsize{MN}}}(\mathbf{x};T)$.
L263: 
L264: To sum up, the complete temperature-based training loss adaptively combines both approaches based on the noise level of each sample:
L265:  | $$\mathcal{L}=\mathbb{E}_{\sigma_{i}\sim p_{\sigma}}\left[\begin{cases}\mathcal{L}_{\text{u}},&\text{if }\sigma_{i}>\sigma_{\text{collapse}}\\
L266: \mathcal{L}_{\text{T}},&\text{if }\sigma_{i}\leq\sigma_{\text{collapse}}\end{cases}\right]$$  |  | (11)
L267: 
L268: Experimentally, we set $T_{i}=\max(\frac{\sigma_{\text{collapse}}}{\sigma_{i}},1)$. Note that temperature-based score matching is not rigorously learning the score function of $p_{\text{\scriptsize{MN}}}$, but its smoothed proxy version.
L269: ## 5 Experiments
L270: Experimental Setup. To evaluate the effectiveness of our smoothing methods, we adopt VE-SDE (cite90†Song et al., 2021 ) as the baseline, which is known as the first time-reverse SDE framework of diffusion models. For fair comparison, we reproduce the VE-SDE setup and apply our smoothing methods with the same implementations. For example, our unconditioning approach uses the same NN architecture as the baseline, with only the time embedding layers removed.
--------------------------------------------------------------------------------
GLOVE: Global Verifier for LLM Memory-Environment Realignment (https://arxiv.org/html/2601.19249v1)
citeturn28127view2 [wordlim: 200] Crawled: today; Content type: text/html; Source: open({"ref_id":"https://arxiv.org/html/2601.19249v1","lineno":275}); Total lines: 877
L250: +GLOVE  | 85  | 85 ($\uparrow$85 )  | 95 ($\uparrow$95 )  | 80  | 75 ($\uparrow$75 )  | 80 ($\uparrow$80 )  | 100  | 100  | 100 ($\uparrow$10 )
L251: MemoryBank  | 85  | 20  | 20  | 80  | 0  | 45  | 95  | 100  | 100
L252: +GLOVE  | 100  | 90 ($\uparrow$70 )  | 85 ($\uparrow$65 )  | 80  | 70 ($\uparrow$70 )  | 65 ($\uparrow$20 )  | 95  | 100  | 100
L253: Voyager  | 85  | 0  | 0  | 85  | 0  | 0  | 100  | 90  | 100
L254: +GLOVE  | 80  | 90 ($\uparrow$90 )  | 95 ($\uparrow$95 )  | 85  | 85 ($\uparrow$85 )  | 75 ($\uparrow$75 )  | 100  | 100 ($\uparrow$10 )  | 100
L255: Generative Agent  | 80  | 0  | 0  | 80  | 15  | 0  | 100  | 95  | 70
L256: +GLOVE  | 75  | 95 ($\uparrow$95 )  | 95 ($\uparrow$95 )  | 80  | 80 ($\uparrow$65 )  | 85 ($\uparrow$85 )  | 95  | 100 ($\uparrow$5 )  | 100 ($\uparrow$30 )
L257: Table 2: GPT-4o: GLOVE’s robustness to environmental drift (Implicit). Score obtained. The shaded rows show the performance of GLOVE-augmented agents. We annotate the performance gap relative to the baseline (e.g., ($\uparrow$56.3) indicates improvement).
L258: Verifier-hidden drift
L259: ---
L260:  | WebShop (Semantic Drift)  | FrozenLake (Reward Reversal)
L261: Method  | Source  | $\to$ Hidden drift  | Source  | $\to$ Hidden drift
L262: No Memory (Plain)  | 82.5  | 87.5  | 0  | 0
L263: Vanilla  | 100  | 75  | 47.5  | 50
L264:      +GLOVE  | 97.5  | 93.8 ($\uparrow$18.8)  | 35  | 97.5 ($\uparrow$47.5)
L265: MemoryBank  | 100  | 81.2  | 62.5  | 57.5
L266:      +GLOVE  | 98.8  | 98.8 ($\uparrow$17.5)  | 67.5  | 97.5 ($\uparrow$40 )
L267: Voyager  | 98.8  | 75  | 67.5  | 50
L268:      +GLOVE  | 98.8  | 98.8 ($\uparrow$23.8)  | 40  | 97.5 ($\uparrow$47.5)
L269: Generative Agent  | 98.8  | 75  | 62.5  | 50
L270:      +GLOVE  | 98.8  | 75  | 62.5  | 92.5 ($\uparrow$42.5)
L271: ### 5.1 Experiment Setup
L272: 
L273: #### Environments.
L274: 
L275: We evaluate GLOVE on three diverse benchmarks, i.e., WebShop (cite91†Yao et al., 2022a ) for web navigation, FrozenLake (cite92†Brockman et al., 2016 ) for discrete planning, and MountainCar (cite92†Brockman et al., 2016 ) for continuous control. This selection covers challenges ranging from semantic reasoning to continuous dynamics.
L276: #### Environmental Drifts.
L277: We introduce a set of controlled environmental drifts applied to standard benchmarks as difficulty-enhanced evaluation settings. LLM agents are equipped with memories of the environment and continue interacting with the same task after environmental drift to test their adaptability. We categorize environmental drifts into two classes that capture common forms of real-world change.
L278: Explicit Drift refers to observable structural changes in the environment, including altered layouts, transition dynamics, or semantic mappings. We calculate the success rate over twenty rounds. Implicit Drift refers to changes in the environment’s underlying logic, such as reward reversals or hidden transition rules, that are not directly observable from immediate state descriptions alone. We calculate the score obtained over twenty rounds.
L279: All drift settings are implemented as systematic benchmark-level modifications and are applied uniformly across all methods without algorithm-specific tuning. Detailed specifications are provided in Appendix cite48†B.4 and Appendix cite49†B.5 .
L280: #### Baselines.
L281: We evaluate GLOVE across a set of representative agent architectures to assess its effectiveness as a general augmentation framework. Specifically, we consider (1) No Memory, a standard zero-shot agent without external context; (2) Vanilla, a baseline agent employing basic RAG; and (3) Various agentic memory architectures, including Voyager (cite68†Wang et al., 2024 ), MemoryBank (cite61†Zhong et al., 2024 ), and Generative Agents (cite62†Park et al., 2023 ).
L282: Each architecture is evaluated both in its original form and augmented with GLOVE, isolating the effect of memory verification and realignment. Details are in Appendix cite35†B.1 .
L283: #### LLM Backbones.
L284: 
L285: We evaluate GLOVE across a wide range of LLM backbones to test architecture-agnostic performance, including open-weights models including Llama-3.1-8B, Llama-3.3-70B, Qwen2.5-7B, Qwen3-30B, DeepSeek-R1, as well as proprietary models, such as GPT-4o and Grok-3.
L286: 
L287: Figure 3: Adaptation Efficiency under Explicit Drift (WebShop). Adding GLOVE achieves near-instant recovery after drifts, triggered by spikes in memory conflicts.
L288: ### 5.2 Adaptation to Explicit Drift
L289: We evaluate agents under explicit structural environmental drifts by transferring memories collected in a source environment to drifted variants with altered semantics, topology, or dynamics. Table cite93†1 reports success rates before and after drift using GPT-4o as the backbone. Agents that rely on static memory retrieval exhibit severe performance degradation once the environment changes.
L290: For instance, under semantic drift in WebShop (Drift I), the Voyager agent’s success rate drops from 85% to 0%, and under topological drift in FrozenLake (Drift II), the Generative Agent similarly collapses to 0%. These results indicate that although such memory systems perform well under stationary conditions, they lack mechanisms to realign stored knowledge when environmental structure changes.
L291: MemoryBank partially alleviates this issue through time-based forgetting, achieving limited robustness and marginally outperforming static baselines. However, this adaptation remains passive and fails to promptly remove high-confidence but invalid memories. As a result, MemoryBank still attains a 0% success rate in FrozenLake Drift II, suggesting that repeated failures are required before outdated topological information is sufficiently forgotten.
--------------------------------------------------------------------------------
LightSBB-M: Bridging Schrödinger and Bass for Generative Diffusion Modeling (https://arxiv.org/html/2601.19312v1)
citeturn28127view3 [wordlim: 200] Crawled: today; Content type: text/html; Source: open({"ref_id":"https://arxiv.org/html/2601.19312v1","lineno":129}); Total lines: 552
L118: However, this method is not simulation-free and can suffer from error accumulation across iterations if the Markovian projection step is not learned perfectly.
L119: #### 2.2.3 LightSB-M: Light Schrödinger Bridge Matching
L120: 
L121: The LightSB-M (cite39†Gushchin et al., 2024 ) method solves the SB problem via a single, optimal projection step based on a new characterization of SB. Let $\pi$ $\in$ $\Pi(\mu_{0},\mu_{T})$ with $\Pi(\mu_{0},\mu_{T})$ the set of all transport plans between $\mu_{0}$ and $\mu_{T}$, and $\mathbb{P}^{\pi}$ $=$ $\pi\mathbb{W}^{\varepsilon}_{|0,T}$ its reciprocal process. Then (cite39†Gushchin et al., 2024 )
L122:  | $$\mathbb{P}^{SB}=\argmin_{\mathbb{Q}\in{\cal S}(\mu_{0})}{\rm KL}(\mathbb{P}^{\pi}|\mathbb{Q}),$$  |  | (4)
L123: 
L124: where ${\cal S}(\mu_{0})$ is the set of SB processes starting from $\mu_{0}$. From the separable form of optimal EOT, the optimal plan associated to a process in ${\cal S}(\mu_{0})$ can be written in the disintegrated form:
L125: 
L126:  | $$\pi_{\varphi}(x_{0},x_{T})=\mu_{0}(x_{0})\underbrace{\frac{e^{<x_{0},x_{T}>/\varepsilon}\varphi(x_{T})}{c_{\varphi}(x_{0})}}_{\pi_{\varphi}(x_{T}|x_{0})},$$  |  | (5)
L127: where $c_{\varphi}(x_{0})$ $:=$ $\int e^{<x_{0},x_{T}>/\varepsilon}\varphi(x_{T})\mathrm{d}x_{T}$, and $\varphi$ is the adjusted potential. Setting $\mathbb{Q}_{\varphi}$ $:=$ $\pi_{\varphi}\mathbb{W}^{\varepsilon}_{|0,T}$ $\in$ ${\cal S}(\mu_{0})$ yields a tractable objective for (cite46†4 ) (cite39†Gushchin et al., 2024 )
L128:  | $\displaystyle{\rm KL}(\mathbb{P}^{\pi}|\mathbb{Q}_{\varphi})=\frac{1}{2}\underbrace{\mathbb{E}^{\mathbb{P}^{\pi}}\Big[\Big\|\alpha_{\varphi}(t,X_{t})-\frac{X_{T}-X_{t}}{T-t}\Big\|^{2}}_{{\rm DSM}(\varphi)}\Big]+C(\pi),$  |
L129: where $\alpha_{\varphi}$ is the score-drift of $\mathbb{Q}_{\varphi}$. We are then led to minimize over $\varphi$ the denoising score matching loss DSM$(\varphi)$ via stochastic gradient descent. In practice, one parametrizes $\varphi$ by a mixture of Gaussian densities such that $\alpha_{\varphi}$ is analytic and requires no neural network (cite47†Korotin et al., 2024 ).
L130: Once $\varphi^{*}$ is learnt, we sample $X_{0}$ $\sim$ $\mu_{0}$, $X_{T}$ $\sim$ $\pi_{\varphi^{*}}(\cdot|X_{0})$ $\sim$ $\mu_{T}$, and so we do not have to solve the associated SDE.
L131: ## 3 Bridging Schrödinger and Bass
L132: The Schrödinger–Bass (SBB) problem is an extension of the classical SB problem by jointly optimizing over both drift and volatility. It is introduced and studied in (cite48†Alouadi et al., 2026 ). Given two distributions $\mu_{0},\mu_{T}\in{\cal P}(\mathbb{R}^{d})$, the goal is to minimize, over $\mathbb{P}\in{\cal P}(\mu_{0},\mu_{T})=\big\{\mathbb{P}\in{\cal P}(\Omega):X_{0}\overset{\mathbb{P}}{\sim}\mu_{0},\;X_{T}\overset{\mathbb{P}}{\sim}\mu_{T}\big\}$, the quadratic cost:
L133:  | $$J(\mathbb{P})=\mathbb{E}_{\mathbb{P}}\Big[\int_{0}^{T}\underbrace{\|\alpha_{t}\|^{2}+\beta\|\sigma_{t}-\sqrt{\varepsilon}I_{d}\|^{2}}_{H_{\beta}(\alpha_{t},\sigma_{t})}\,\mathrm{d}t\Big],$$  |  | (6)
L134: 
L135: for some $\beta>0$, where $(\alpha,\sigma)$ is the drift/volatility of $X$ under $\mathbb{P}$, i.e., $\mathrm{d}X_{t}=\alpha_{t}\,\mathrm{d}t+\sigma_{t}\,\mathrm{d}W_{t}$. This problem is denoted by ${\rm SBB}(\mu_{0},\mu_{T}):=\inf_{\mathbb{P}\in{\cal P}(\mu_{0},\mu_{T})}J(\mathbb{P})$.
L136: Note that as $\beta\to\infty$, the volatility $\sigma$ is constrained to equal $I_{d}$, recovering the classical SB problem. Conversely, dividing (cite49†6 ) by $\beta$ and letting $\beta\to 0$ forces the drift term $\alpha$ to vanish, yielding the Bass martingale transport problem. In other words, the parameter $\beta$ controls the relative weight of drift versus volatility, interpolating between these two well-known cases.
L137: ### 3.1 Dual Representation of the Primal SBB
L138: 
L139: The primal problem ${\rm SBB}(\mu_{0},\mu_{T})$ admits a dual representation, which consists of maximizing over a suitable class of functions $(v,\psi)$ the Lagrangian functional
L140: 
L141:  | $\displaystyle L_{\mu_{0},\mu_{T}}(\psi,v)=\int\psi(x)\,\mu_{T}(\mathrm{d}x)-\int v(0,x)\,\mu_{0}(\mathrm{d}x),$  |
L142: 
L143: where $v$ is the value function of the unconstrained stochastic control problem with Bellman equation:
L144:  | $$\begin{cases}\partial_{t}v+H_{\beta}^{*}(\nabla_{x}v,D_{x}^{2}v)=0,\quad\text{on }[0,T)\times\mathbb{R}^{d},\\
L145: v(T,\cdot)=\psi,\quad\text{on }\mathbb{R}^{d},\end{cases}$$  |  | (7)
L146: 
L147: with $H_{\beta}^{*}$ denoting the Fenchel–Legendre transform of $H_{\beta}$, explicitly given by
L148: 
L149:  | $\displaystyle H_{\beta}^{*}(p,q)=\frac{1}{2}|p|^{2}+\frac{\varepsilon\beta}{2}I_{d}:\Big(\big(I_{d}-\frac{q}{\beta}\big)^{-1}-I_{d}\Big),$  |
L150: for $(p,q)\in\mathbb{R}^{d}\times\mathbb{S}_{+}^{d}$ such that $q<\beta I_{d}$. Assuming that ${\rm SBB}(\mu_{0},\mu_{T})<\infty$, we have:
L151: 
L152:   * •
L153: 
L154: Attainment of the primal problem: there exists $(\alpha^{*},\sigma^{*})\leftrightarrow\mathbb{P}^{\rm SBB}$ attaining the infimum in ${\rm SBB}(\mu_{0},\mu_{T})$, in feedback form: $\alpha_{t}^{*}=\mathrm{a}^{*}(t,X_{t})$, $\sigma_{t}^{*}=\vartheta^{*}(t,X_{t})$.
L155: 
L156:   * •
L157: 
L158: Duality relation: we have
L159:  | $${\rm SBB}(\mu_{0},\mu_{T})=\sup_{\begin{subarray}{c}\psi\in C^{2}\cap C_{b}^{\infty}\cap L^{1}(\mu_{T}),\ v\in C_{b}^{1,2},\\
L160: D_{x}^{2}v<\beta I_{d},\ \psi=v(T,\cdot),\\
L161: \partial_{t}v+H_{\beta}^{*}(\nabla_{x}v,D_{x}^{2}v)=0\end{subarray}}L_{\mu_{0},\mu_{T}}(\psi,v)$$  |  | (8)
L162: 
L163:   * •
L164: 
L165: Duality on the control:
L166: When $\mu_{0}$ and $\mu_{T}$ have finite second moment, and if $\beta>\frac{1}{T}$, then the supremum in the dual problem is attained at $(v^{*},\psi^{*})$, and the optimal feedback policies are given by
L167: 
L168:  | $\displaystyle\begin{cases}\mathrm{a}^{*}(t,x)\;=\;\nabla_{x}v^{*}(t,x),\quad(t,x)\in[0,T)\times\mathbb{R}^{d},\\
L169: \vartheta^{*}(t,x)\;=\;\sqrt{\varepsilon}\Big(I_{d}-\frac{D_{x}^{2}v^{*}(t,x)}{\beta}\Big)^{-1}.\end{cases}$  |



# extraadmit

Smoothing the Score Function for Generalization in Diffusion Models:An Optimization-based Explanation Framework (https://arxiv.org/html/2601.19285v1)
citeturn28124view0 [wordlim: 200] Crawled: today; Content type: text/html; Source: find({"ref_id":"https://arxiv.org/html/2601.19285v1","pattern":"Noise Unconditioning"}); Total lines: 1510
L15:   1. cite5†Abstract L16:   2. cite6†1 Introduction L17:   3. cite7†2 Preliminaries L18:     1. cite8†2.1 Forward SDEs and Backward ODEs L19:     2. cite9†2.2 Noise Unconditioning: ODE as Gradient Flow L20:   4. cite10†3 From Memorization to Generalization L21:     1. cite11†3.1 Why Memorize? L22:     2. cite12†3.2 Generalization Evaluation L23:   5. cite13†4 Learning the Smoothed Score Function L24:     1. cite14†4.1 Unconditioning Score Matching L25:     2. cite15†4.2 Temperature-based Score Matching L26:   6. cite16†5 Experiments L94:     1. cite84†Neural networks as implicit temperature-smoothed scores. L95:     2. cite85†Optimization-based sampling via noise unconditioning. L96:     3. cite86†Extensions to latent diffusion and consistency models. L97:     4. cite87†Toward adaptive smoothing and temperature design. L108: Leveraging this insight, we propose two novel methods to further enhance generalization: (1) Noise Unconditioning enables each training sample to adaptively determine its score function weight to increase the effect of more training samples, thereby preventing single-point dominance and mitigating collapse. (2) Temperature Smoothing introduces an explicit parameter to control the smoothness.
L131: cite103†Image: Refer to caption Figure 1: Illustration of sampling behaviors with different score functions. (a) Standard diffusion empirical score function leads to memorization, where trajectories collapse directly to training points. (b) The neural network-learned score function enables generalization. (Interpolation experiment) (c) The noise unconditioning allows smoother score function weights and delayed collapse.
L145: Noise Unconditioning. In most diffusion models, the noise levels are designed as continuous, which means the shells pack the space. Therefore, we know from cite11†Section 3.1 that for the fixed center $\mu$ and position $\mathbf{x}$, there is an “optimal shell” corresponding to some noise level $\sigma_{*}$ that will dominate the score function weight over all noise levels.
L146: However, in standard diffusion models, the noise level is fixed at each sampling stage, which means the sampling point may not lie on the optimal shells around most training points, leading to sub-optimal score function weights (much smaller) for these points. So, our first smoothing method is to remove conditioning on noise, allowing each training point to adaptively find its optimal shell at the given position $\mathbf{x}$.
L147: This ensures that other training points can contribute to the score function, preventing a single point from dominating, and thus mitigating memorization. In addition, this noise unconditioning enables us to regard the sampling as a gradient ascent process, where the optimal solutions are the training points.
L148: In this case, even though the sampling may still collapse to the centers, the “collapse time” to a particular center $\mathbf{\mu}_{j}$ will be delayed, since other centers still make significant contributions during the sampling. For illustration, compare cite104†Figure 1 (c) to cite104†Figure 1 (a).
L149: Temperature Smoothing. Given that the score function weights ${w}_{ij}(x)$ are defined as softmax functions, another smoothing approach becomes apparent: Modify the definition of these weights by introducing a temperature parameter to smooth them. The effect of smoothing is to delay the collapse of the denoising process; see cite104†Figure 1 (d).
L150: By using higher temperatures at smaller noise levels, the sampling will have chances to continuously explore the local manifold rather than collapsing to a single point. This enables the neural network to sample from combinations over local manifold containing nearby samples, making it more likely to generalize rather than memorize.
L151: If the temperature is not sufficiently high, collapse may still occur eventually, but early stopping may prevent full collapse while maintaining the exploration benefits (see the red regions in cite104†Figure 1 (d)). However, we must also avoid excessively high temperatures as this would introduce influence from training points in an excessively large neighborhood, causing the generated point to deviate significantly from the image manifold.
L152: Overall, we make the following contributions.
L153: 
L154:   * •
L155: 
L156: We theoretically prove that memorization stems from the sharpness of empirical score functions, and experimentally verify that neural networks achieve generalization by implicitly smoothing the score-function weights across different centers, i.e., increasing the influence of samples other than the nearest one.
L157: 
L158:   * •
L159: We propose two novel methods to mitigate memorization: (1) Noise Unconditioning, a framework that unifies distributions across noise levels and is equivalent to explicit score matching on a unified Gaussian mixture, so that sampling can be interpreted as gradient ascent on this fixed objective, enabling optimization-based strategies for generation.
L160: (2) Temperature Smoothing, a plug-and-play modification of the training objective that explicitly controls the smoothness of score weights and improves generalization with only modest extra cost.
L161:   * •
L162: 
L163: Our explanation framework bridges the gap between diffusion theory and practice, providing theoretical foundations for many previously confusing experimental phenomena. This theoretical grounding may facilitate further advances in generative modeling.
L164: ## 2 Preliminaries
L165: ### 2.1 Forward SDEs and Backward ODEs
L166: 
L167: Stochastic differential equations (SDEs) provide a powerful framework for describing diffusion processes (cite90†Song et al., 2021 ). A general forward SDE in $\mathbb{R}^{d}$ can be written as:
L168: 
L169:  | $$\mathrm{d}\mathbf{x}_{t}=\mathbf{\mu}(\mathbf{x}_{t},t)\,\mathrm{d}t+\sigma(t)\,\mathrm{d}\mathbf{w}_{t},$$  |  | (1)
L170: where $\mathbf{x}_{t}\in\mathbb{R}^{d}$ is the state of the system at time $t\in[0,T]$, $\mathbf{\mu}(\cdot,\cdot)$ and $\sigma(\cdot)$ are the drift and diffusion coefficients respectively, and $\mathbf{w}_{t}$ represents the standard Brownian motion. This forward SDE describes how data is progressively perturbed into a noise-like distribution as $t$ increases.
L171: A remarkable property of this SDE is the existence of an ordinary differential equation (ODE), dubbed the Probability Flow ODE (cite90†Song et al., 2021 ), whose solution trajectories sampled at $t$ are distributed according to:
L172:  | $$\mathrm{d}\mathbf{x}_{t}=\left[\mathbf{\mu}(\mathbf{x}_{t},t)-\frac{1}{2}\sigma(t)^{2}\nabla_{\mathbf{x}}\log p_{t}(\mathbf{x})\right]\,\mathrm{d}t,$$  |  | (2)
L173: 
L174: where $\nabla_{\mathbf{x}}\log p_{t}(\mathbf{x})$ is the score function of the perturbed distribution at time $t$, namely the learning target of a neural network $s_{\theta}(\mathbf{x},t)$ via score matching (cite96†Vincent, 2011 ; cite108†Hyvärinen and Dayan, 2005 ; cite97†Song and Ermon, 2019 ).
L175: ### 2.2 Noise Unconditioning: ODE as Gradient Flow
L176: Note that we let $\mathbf{\mu}(\mathbf{x},t)=0$ and $\sigma(t)=\sqrt{2t}$ following the variance exploding SDE (cite90†Song et al., 2021 ; cite109†Karras et al., 2022 ). This choice ensures that we have $p_{t}(x)=p^{*}(x)\otimes\mathcal{N}(0,t^{2}\mathbf{I})$, i.e., $p_{i}^{*}(x)=p^{*}(x)\otimes\mathcal{N}(0,\sigma_{i}^{2}\mathbf{I})$, where $\otimes$ denotes the convolution operation.
L222: A natural explanation is that the neural network fits the score function quite well, but implicitly smooths its weights at small noise levels, preventing the dominance of individual training points and avoiding sampling collapse. Following this insight, we analyze the generalization ability of neural networks, standard diffusion, noise unconditioning, and temperature smoothing by comparing the expansiveness of their sampling process at points where the shells from different training points overlap.
L337: By exploring the fundamental properties of the score function, we identify the cause of memorization and propose two smoothing methods — Noise Unconditioning and Temperature Smoothing — which elegantly control the concentration of the score function weight and effectively reduce memorization while maintaining high generation quality.
L342: Gradient Ascent Perspective. Our noise unconditioning reformulates sampling as gradient ascent on a unified distribution, enabling constraints to be integrated via projected gradient methods. This feature is particularly valuable for applications requiring adherence to physical laws, such as video generation, which struggles to learn complex physical dynamics from data alone.
L407: It has become standard practice, adopted by flow matching (cite160†Papamakarios et al., 2021 ; cite161†Lipman et al., 2022 ; cite162†Liu et al., 2022 ; cite163†Albergo et al., 2025 ), consistency models (cite164†Song et al., 2023 ), and distillation techniques (cite165†Song and Dhariwal, 2024 ; cite166†Lu and Song, 2025 ). A few recent works have also explored noise unconditioning—removing the explicit noise-level input.
L408: (cite111†Song and Ermon, 2020 ) first showed that a score network with a preconditioned objective can be trained without conditioning and still generate reasonable samples using Annealing Langevin Dynamics. (cite167†Sun et al., 2025 ) further demonstrated that such unconditioning works across DDPMs and flow models. These works, however, mainly establish that unconditioning can work in practice, without clarifying its theory.
L409: Our paper goes beyond demonstrating that noise unconditioning can work by providing a theoretical framework for understanding what it essentially learns and how it should be correctly used. Specifically, we prove that the standard unconditioning loss cite168†Equation 9 corresponds to explicit score matching on a unified Gaussian mixture $p_{\text{\scriptsize{MN}}}$ (cite47†Section A.6 ), and use this perspective to characterize how unconditioning smooths score weights and improves generalization.
L1038: Training Cost and Scalability. For the standard setting with a single temperature level ($T=1$), conditioning vs. unconditioning only differs in whether the noise is fed into the network. Consequently, noise unconditioning introduces no additional asymptotic cost; in fact, removing the noise embedding slightly reduces both GPU memory and wall-clock time per batch.
L1074: Overall, Noise Unconditioning and Temperature Smoothing can be trained with virtually the same computational budget as standard diffusion models. The only non-negligible overhead arises from a deliberately naive KNN implementation in pixel space, which is avoidable in practice.
L1474: Our explicit Temperature Smoothing and Noise Unconditioning mechanisms make this effect controllable and observable: they reduce memorization fractions on Cat–Caracal and lower sampling expansiveness (cite19†Sections 5.1.2 and cite68†B.3.2 ), while still enabling meaningful generalization on CIFAR-10 and beyond. Conceptually, this “implicit temperature” view pinpoints what is being smoothed: not an abstract learned function, but the empirical softmax weights over overlapping Gaussian shells.
L1475: This yields a concrete geometric picture that ties the same smoothing mechanism to both memorization on small datasets and generalization on large ones.
L1476: At the same time, our findings raise an open methodological question: how should one quantitatively characterize the memorization–generalization trade-off at realistic scale? The nearest-neighbor ratio is informative on Cat–Caracal but quickly loses discriminative power on CIFAR-10, exactly when samples move from single-point collapse to residing in dense local manifolds.
L1477: Developing metrics that remain sensitive in this regime—for example by combining pixel and feature spaces or explicitly modeling local density—is an important direction for future work.
L1478: ##### Optimization-based sampling via noise unconditioning.
L1479: A key contribution of this work is the optimization-based reformulation of sampling enabled by noise unconditioning. By removing the explicit noise input and optimizing the unified loss in Equation (11), the model learns the score of a fixed Gaussian mixture $p_{\text{\scriptsize{MN}}}$, independent of diffusion time. Sampling can then be interpreted as continuous-time gradient ascent on $\log p_{\text{\scriptsize{MN}}}(x)$, rather than as a purely time-dependent reverse SDE or ODE.
L1480: This perspective offers both conceptual and practical benefits. Conceptually, it demystifies the sampling process: once noise is unconditioned and the model learns the score of a fixed Gaussian mixture $p_{\text{\scriptsize{MN}}}$, our sampler can be viewed as a continuous-time gradient flow on the static objective $\log p_{\text{\scriptsize{MN}}}(x)$ whose modes coincide with training samples.
L1481: This gradient-flow picture relies only on elementary optimization and high-dimensional Gaussian geometry, offering a lower-barrier and more visual alternative to traditional SDE/PDE-based explanations of diffusion behavior. Practically, this viewpoint suggests treating sampling as an optimization problem, motivating the use of adaptive step sizes, principled stopping rules, and constrained gradient flows (e.g., via projection) to better exploit the geometry of the learned score field.
L1482: More broadly, it invites future work to systematically import tools from modern optimization—such as line-search, trust-region, and variational methods—into the design and analysis of diffusion samplers.
L1483: However, this optimization view also highlights a deeper question. Our analysis characterizes what the learned, smoothed score field looks like, but not fully why standard neural networks trained with simple MSE losses should converge to this particular smoothed solution among all possibilities.
L1484: In particular, it remains unclear why the network prefers to organize data in a semantic feature space rather than in raw pixel space, and how architectural choices and optimization dynamics jointly induce this preference. The gradient-flow interpretation offers a useful lens on these questions by framing learning and sampling as motion in a fixed energy landscape, but a complete understanding of the resulting implicit bias is still an open problem.
L1485: ##### Extensions to latent diffusion and consistency models.
L1486: Because our framework is formulated at the level of score fields, it is largely agnostic to architecture and suggests several extensions. First, applying Noise Unconditioning and Temperature Smoothing to latent diffusion models is especially natural.
L1487: Latent spaces typically have lower curvature and better-structured manifolds than pixel space, so our smoothing mechanisms could operate more stably—allowing larger $T$ or broader neighborhoods—without drifting off-manifold, as suggested by our feature-space KNN experiments. In this sense, our geometric view of “local shells” and manifolds carries over almost verbatim from pixel space to learned latent spaces, potentially making the theory even simpler there.
--------------------------------------------------------------------------------
NuiWorld: Exploring a Scalable Framework for End-to-End Controllable World Generation (https://arxiv.org/html/2601.19048v1)
citeturn28124view1 [wordlim: 200] Crawled: last week; Content type: text/html; Source: find({"ref_id":"https://arxiv.org/html/2601.19048v1","pattern":"generation"}); Total lines: 492
L84: We represent scenes as a variable-length sequence of scene chunk tokens, where each chunk is encoded as a flattened vector set. This yields a compact and efficient representation that scales with scene size while preserving consistent geometric fidelity. Efficient End-to-End System. Our model is trained end-to-end to generate complete scenes at once, eliminating the need for complex training-free pipelines or agent-based systems that may incur additional computational overhead.
L85: cite67†Image: Refer to caption Figure 3. Our framework begins with generative bootstrapping, shown on the left. Using Nano Banana to generate images and Trellis 2 to reconstruct 3D scenes. NuiScene is then trained on these scenes to produce new scenes with varying size and layouts. Finally, using these scenes and their pseudo sketches we train our variable-length sketch-to-world model on the right.
L86: ## 2. Related Work
L87: ### 2.1. Unbounded 3D Scene Generation
L88: We review methods that perform expandable generation of arbitrarily large 3D scenes directly in the 3D domain. PDD (cite68†Liu et al., 2024 ) uses a multi-scale pyramid diffusion framework to generate urban scenes. While several works (cite69†Lee et al., 2024 ; cite70†Wu et al., 2024 ; cite71†Meng et al., 2025 ) follow the latent diffusion paradigm, learning to generate chunks through diffusion in the latent space.
L89: Expandable generation is enabled with RePaint (cite72†Lugmayr et al., 2022 ) by conditioning on overlapping regions, requiring additional diffusion steps. SemCity (cite69†Lee et al., 2024 ) and BlockFusion (cite70†Wu et al., 2024 ) use triplane representations for urban and indoor scenes, respectively, while LT3SD (cite71†Meng et al., 2025 ) uses hierarchical feature grids for modeling finer indoor details.
L90: NuiScene (cite54†Lee et al., 2025 ) introduces a vector set representation for outdoor scenes and an explicit outpainting model for fast generation. WorldGrow (cite73†Li et al., 2025a ) fine-tunes Trellis (cite55†Xiang et al., 2025b ) for 3D block inpainting, enabling block-by-block synthesis of scenes. The autoregressive nature of these methods causes inference time to scale with scene size.
L91: As shown in cite74†Table 4 , NuiScene incurs higher runtime than models like ours that diffuses entire scenes at the same time.
L92: ### 2.2. Training-Free Scene Generation
L93: Several recent works leverage Trellis (cite55†Xiang et al., 2025b ) to enable training-free, chunk-based generation, circumventing the resolution limits of object-centric generators. SynCity (cite63†Engstler et al., 2025 ) uses FLUX (cite75†Labs, 2024 ) to generate smaller image tiles sequentially and Trellis to lift them into 3D.
L94: 3DTown (cite64†Zheng et al., 2025b ) derives a point cloud from a reference image of the scene, and conditions Trellis on cropped images with corresponding cropped point clouds to generate local regions. TrellisWorld (cite65†Chen et al., 2025a ) and Extend3D (cite66†Yoon et al., 2025 ) introduces denoising schemes to enable parallel chunk generation for scenes. The primary limitation of these methods is their resource consumption, which is fundamentally bounded by the cost of running Trellis (cite74†Table 4 ).
L95: Sequential chunk generation leads to inference time that scales linearly with scene size, whereas parallel generation comes at the expense of increasing memory usage. Our model is trained to generate whole scenes natively with latents that naturally scale with scene size (cite76†Figure 8 ).
L96: ### 2.3. LLM Aided Scene Generation
L97: Recent works (cite49†Lu et al., 2025 ; cite51†Wang et al., 2025b ; cite50†Huang et al., 2025 ) leverage LLMs to assist city generation. Yo’City (cite49†Lu et al., 2025 ) relies on LLMs for generating fine-grained text prompts for scene grids to drive image and subsequent 3D generation. RaiseCity (cite51†Wang et al., 2025b ) derives buildings from street-view images via segmentation and used as inputs to image generation tools for completion before 3D generation and scene placement.
L98: MajutsuCity (cite50†Huang et al., 2025 ) learns to generate semantic layout and height maps from LLM enriched user input. Buildings are extruded with height maps, and used to condition image generation tools for image to 3D conversion and scene assembly. Across all methods, agents are further employed to iteratively evaluate and regenerate images of city regions or buildings before 3D generation. The inclusion of agent heavy pipelines can introduce longer generation times and API costs during inference.
L99: Additionally, these works mainly focus on cityscapes, it is unknown whether they can generalize to more open-domain scenarios. WorldGen (cite48†Wang et al., 2025a ) relies on LLMs to produce initial procedural generation parameters from text input. The procedurally generated blockout is used as a condition for image generation. Followed by scene reconstruction, decomposition, and enhancement.
L100: Our sketch-to-world model operates end-to-end without LLMs and enables open-domain generation through our generative bootstrapping process.
L101: ## 3. Preliminary
L102: ### 3.1. NuiScene
L103: 
L104: In NuiScene (cite54†Lee et al., 2025 ), the model is trained on $K$ scenes $\{\mathbf{S}_{i}\}_{i=1}^{K}$ processed from Objaverse (cite77†Deitke et al., 2023 ). Each scene is represented as $\mathbf{S}_{i}=(\mathbf{O}_{i},\mathbf{P}_{i})$, where $\mathbf{O}_{i}$ denotes an occupancy grid with dimensions $X_{i}\times Y_{i}\times Z_{i}$, and $\mathbf{P}_{i}\in\mathbb{R}^{N_{pc}\times 3}$ is a point cloud with $N_{pc}$ points sampled from the marching cubes surface of $\mathbf{O}_{i}$.
L105: Each scene is partitioned along the $x$ and $z$ axes into smaller chunks of fixed size $s\times Y_{i}\times s$, where $s<\min_{i}X_{i}$ and $s<\min_{i}Z_{i}$. We denote the chunk at location (u, v) as $\mathbf{S}_{i}^{(u,v)}=(\mathbf{O}_{i}^{(u,v)},\mathbf{P}_{i}^{(u,v)})$, where $\mathbf{O}_{i}^{(u,v)}$ is the cropped occupancy and $\mathbf{P}_{i}^{(u,v)}\in\mathbb{R}^{N_{pc}^{(u,v)}\times 3}$ is the corresponding point cloud from its surface.
--------------------------------------------------------------------------------
LightSBB-M: Bridging Schrödinger and Bass for Generative Diffusion Modeling (https://arxiv.org/html/2601.19312v1)
citeturn28124view2 [wordlim: 200] Crawled: today; Content type: text/html; Source: find({"ref_id":"https://arxiv.org/html/2601.19312v1","pattern":"3.1"}); Total lines: 552
L15:   1. cite5†Abstract L16:   2. cite6†1 Introduction L17:   3. cite7†2 Background L18:     1. cite8†2.1 The Schrödinger Bridge Problem L19:     2. cite9†2.2 Diffusion Schrödinger Bridge for Generative Modeling L20:       1. cite10†2.2.1 Sinkhorn Algorithm L21:       2. cite11†2.2.2 Iterative Markovian Fitting L22:       3. cite12†2.2.3 LightSB-M: Light Schrödinger Bridge Matching L23:   4. cite13†3 Bridging Schrödinger and Bass L24:     1. cite14†3.1 Dual Representation of the Primal SBB L25:     2. cite15†3.2 SBB System L26:   5. cite16†4 Generative Modeling with SBB L27:     1. cite17†4.1 Training L28:     2. cite18†4.2 Inference L29:   6. cite19†5 Numerical Experiments L30:     1. cite20†5.1 Illustrative Examples L31:     2. cite21†5.2 Quantitative Evaluation on Low-Dimensional Datasets L32:   7. cite22†6 Qualitative Evaluation on Unpaired Image-to-Image Translation L33:   8. cite23†7 Conclusion L34:   9. cite24†References L35:   10. cite25†A Exploring Alternative Algorithms L36:     1. cite26†A.1 LightSBB-M for $\beta$ Large L37:     2. cite27†A.2 Sinkhorn-based Algorithm L38:   11. cite28†B Experimental Setup L39:     1. cite29†B.1 Model Architecture L137: ### 3.1 Dual Representation of the Primal SBB
L138: 
L139: The primal problem ${\rm SBB}(\mu_{0},\mu_{T})$ admits a dual representation, which consists of maximizing over a suitable class of functions $(v,\psi)$ the Lagrangian functional
L140: 
L141:  | $\displaystyle L_{\mu_{0},\mu_{T}}(\psi,v)=\int\psi(x)\,\mu_{T}(\mathrm{d}x)-\int v(0,x)\,\mu_{0}(\mathrm{d}x),$  |
L142: 
L143: where $v$ is the value function of the unconstrained stochastic control problem with Bellman equation:
L144:  | $$\begin{cases}\partial_{t}v+H_{\beta}^{*}(\nabla_{x}v,D_{x}^{2}v)=0,\quad\text{on }[0,T)\times\mathbb{R}^{d},\\
L145: v(T,\cdot)=\psi,\quad\text{on }\mathbb{R}^{d},\end{cases}$$  |  | (7)
L146: 
L147: with $H_{\beta}^{*}$ denoting the Fenchel–Legendre transform of $H_{\beta}$, explicitly given by
L148: 
L149:  | $\displaystyle H_{\beta}^{*}(p,q)=\frac{1}{2}|p|^{2}+\frac{\varepsilon\beta}{2}I_{d}:\Big(\big(I_{d}-\frac{q}{\beta}\big)^{-1}-I_{d}\Big),$  |
--------------------------------------------------------------------------------
From Observations to Events: Event-Aware World Model for Reinforcement Learning (https://arxiv.org/html/2601.19336v1)
citeturn28124view3 [wordlim: 200] Crawled: today; Content type: text/html; Source: find({"ref_id":"https://arxiv.org/html/2601.19336v1","pattern":"GES"}); Total lines: 853
L192: Human comprehension systems tend to form future prediction within event boundaries, whereas humans’ ability of prediction and memory decreases at the event boundaries (cite95†Radvansky and Zacks, 2017 ). Motivated by this, we develop a generic event segmentor (GES) that automatically detects event boundaries.
L193: For each modality $m$, we notice that the number of events $\alpha^{(m)}_{t}=\sum_{i=1}^{N^{m}}\frac{1}{N^{m}}\mathbb{I}(e_{t,i}^{(m)}\text{ occurs})$ can serve as an intuitive indicator of event boundaries. To keep the method computationally efficient, we do not introduce any additional trainable parameters into the GES. Instead, we implement the GES as a deterministic function of the events $\mathbf{e}^{(m)}_{t}$:
L194:  | $$g_{\theta}(\mathbf{o}^{(m)}_{t},\mathbf{\hat{o}}^{(m)}_{t},\mathbf{e}^{(m)}_{t})\doteq g(\alpha^{(m)}_{t},\alpha_{\text{thr}}^{(m)}),$$  |  | (6)
L195: where $\alpha_{\text{thr}}^{(m)}$ denotes the threshold of the percentage of events that determines whether the agent should attend to events in the $m$-th modality. If $g(\alpha^{(m)}_{t},\alpha_{\text{thr}}^{(m)})=0$, we say that an event boundary is detected. In this case, event prediction is devoid of meaning and should be suppressed. Therefore, Equation cite96†4 with GES turns into:
L197: Furthermore, world models should prioritize dynamic events over static observations so as to improve accuracy on informative parts of the observations, rather than uniformly over all observations. However, when GES detects an event boundary where the priority of dynamic events is not suitable, the world model should reallocate attention from events to raw observations and focus on modeling raw observations. We implement this via an event-aware observation loss:
L264: (a) No event predictor
L265: 
L266: (b) No GES
L267: 
L268: Figure 4: Ablation studies on key components of EAWMs with 5 random seeds over 6 Atari games: Assault, Breakout, Gopher, Krull, and Ms Pacman, Up N Down. The results show Simulus with the solid lines and EADream with the dashed lines.
L270: EADream Our observation predictor $\mathbf{\hat{o}}_{t}\sim p_{\theta}(\mathbf{\hat{o}}_{t}|\mathbf{h}_{t},\mathbf{\hat{z}}_{t})$ is slightly different from the observation decoder $\mathbf{\hat{o}}_{t}\sim p_{\theta}(\mathbf{\hat{o}}_{t}|\mathbf{h}_{t},\mathbf{z}_{t})$ in DreamerV3 (cite62†Hafner et al., 2025 ). EADream predicts future observations directly from the prior states $\mathbf{z}_{t}$, and thus we name this dynamic model RSSM-OP.
L271: To achieve compututational efficiency, we implement a simple form of GES: $g(\alpha^{(m)}_{t},\alpha_{\text{thr}}^{(m)})=\mathbb{I}(\alpha_{t}^{(m)}<\alpha_{\text{thr}}^{(m)})$. Please refer to Appendix cite21†A for more details. As Table cite104†2 displays, EADream reaches a mean score of 723.8 and a median score of 805.3, setting new state-of-the-art results among all RL methods on these challenging tasks from DeepMind Control Suite.
L272: On DMC-GB2, EADream outperforms DreamerV3 by a large margin, highlighting its robustness to visual distractors and generalization across visual variations. Beyond our expectations, EADream even outperforms SADA, an algorithm specifically designed for the benchmark. Unlike SADA, EAWM does not rely on paired original and augmented images, demonstrating that strong generalization can be achieved without additional supervision.
L273: EASimulus Integrating Simulus into EAWM is straightforward, requiring only the integration of the event predictor and GES.
L274: Specifically, the output of the GES increases as events become sparser, allowing them to be better highlighted: $g(\alpha^{(m)}_{t},\alpha_{\text{thr}}^{(m)})=\mathbb{I}(\alpha_{t}^{(m)}<\alpha_{\text{thr}}^{(m)})/{\text{arsinh}\left[\text{clip}\left(\frac{\alpha_{t}^{(m)}}{\alpha_{\text{thr}}^{(m)}},\epsilon_{\alpha},1\right)\right]}$, where $\epsilon_{\alpha}>0$ is a coefficient to smooth the curve of $\alpha_{t}^{(m)}$ and stablize the training process. Other details are provided in Appendix cite27†B .
L275: Remarkably, EASimulus obtains a mean human-normalized score of 1.818, setting a new record and reaching a superhuman IQM score for the first time among MBRL methods. In addition, EAWM provides a boost to the performance of the state-of-the-art method Simulus and reaches a score of 7.23% in Craftax 1M, indicating that multi-modal event awareness facilitates policy learning.
L276: ### 4.3 Ablation Studies
L277: 
L278: We discuss the effectiveness of key components of EAWM. We randomly select 6 games from Atari, as illustrated in Figure cite113†4 , and 4 tasks from DeepMind Control Suite, as shown in Figure cite114†5 .
L279: 
L280: Figure 5: Ablation studies on key components of EAWM on DeepMind Control Suite.
L281: No Event Predictor In this case, the GES influences the loss function for observation prediction in Equation  cite115†8 . Figure cite116†4(a) shows the decrease in mean HNS scores of both world models by about 0.4 without the event predictor. We observe that representation learning from event prediction plays an essential role in environments where events provide sufficient information for reward prediction, such as Breakout and Krull.
L282: Furthermore, these results show how kinetic features reshape and accelerate policy learning.
L283: No GES The GES stabilizes the training process of world models and provides robust event-aware representations for policy learning. As shown in Figure cite117†4(b) , the median HNS scores grow slowly and display large fluctuations in the absence of GES. This stability is particularly critical in continuous control robotics tasks, where recovering from a single erroneous action often requires executing a long sequence of corrective steps.
L284: Without Observation Prediction We notice a performance drop if EAWM is configured to make observation reconstruction. Specifically, the mean score of four tasks declines from $737.2$ to $519.5$, as shown by the orange line in Figure cite114†5 . In addition, we conduct an experiment on DreamerV3 with RSSM-OP in Table cite118†13 , demonstrating that the performance improvement of EAWM mainly stems from the joint modeling of observations and events, not from RSSM-OP alone.
L285: These results imply that event prediction and observation prediction are tightly coupled in event-aware representation learning.
L286: ## 5 Related Work
L287: Model-based Reinforcement Learning Sample efficiency has become increasingly important in reinforcement learning, especially for real-world applications (cite119†Sutton, 1991 ; cite120†Hafner, 2022 ). The first world model (cite56†Ha and Schmidhuber, 2018 ) showed that combining latent dynamics with a generative observation model enables agents to plan through imagination, sparking broad interest in MBRL (cite121†Moerland et al., 2023 ).
L301: Future work may consider modeling the function of GES directly with neural networks to achieve both efficiency and expressiveness. Second, although EADream and EASimulus are trained with fixed hyperparameters across domains, developing a unified model capable of solving multiple tasks by effectively sharing common knowledge is still challenging (cite147†Sridhar et al., 2025 ).
L773: Unlike purely reconstruction-driven objectives, which tend to overfit to pixel-level variations, GES focuses on changes that correspond to meaningful dynamics in the environment. This enables EAWM to disregard spurious fluctuations in the background—such as texture shifts, lighting changes, or irrelevant object motions—that do not alter the underlying task.



