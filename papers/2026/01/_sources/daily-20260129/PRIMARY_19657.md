# Exact-v1 necessary primary — 2601.19657

Original returned context retained; only necessary core, controls, setup and direct counterclaims adopted.

## jan29_systemfour_head

One Token Is Enough: Improving Diffusion Language Models with a Sink Token (https://arxiv.org/html/2601.19657v1)
citeturn28514view2 [wordlim: 200] Crawled: 2 days ago; Content type: text/html; Source: open({"ref_id":"https://arxiv.org/html/2601.19657v1","lineno":null}); Total lines: 361


## jan29_systemfour_route

One Token Is Enough: Improving Diffusion Language Models with a Sink Token (https://arxiv.org/html/2601.19657v1)
citeturn28515view1 [wordlim: 200] Crawled: 2 days ago; Content type: text/html; Source: find({"ref_id":"https://arxiv.org/html/2601.19657v1","pattern":"3.2"}); Total lines: 361
L15:   1. cite5†Abstract L16:   2. cite6†1 Introduction L17:   3. cite7†2 Related Work L18:     1. cite8†2.1 Diffusion Language Model L19:     2. cite9†2.2 Attention Sink L20:   4. cite10†3 Method L21:     1. cite11†3.1 Diffusion Language Modeling L22:       1. cite12†3.1.1 Forward Process L23:       2. cite13†3.1.2 Reverse Process L24:       3. cite14†3.1.3 Training Objective L25:     2. cite15†3.2 Extra Sink Token for DLM L26:   5. cite16†4 Experiment L27:     1. cite17†4.1 Experiment Settings L28:       1. cite18†4.1.1 Benchmarks L29:       2. cite19†4.1.2 Implementation Details L30:     2. cite20†4.2 Experiment Results L31:     3. cite21†4.3 Ablation Studies L32:       1. cite22†4.3.1 The position of sink token L33:       2. cite23†4.3.2 The number of sink token L34:     4. cite24†4.4 Internal Analysis of Sink Tokens and Attention Allocation L35:   6. cite25†5 Conclusion L36:   7. cite26†References L37:   8. cite27†A Appendix L38:     1. cite28†A.1 Training details L39:     2. cite29†A.2 Gated Attention for DLM L40:     3. cite30†A.3 Value-Space Token Vectors Analysis L41:       1. cite31†A.3.1 Value-space token vectors in a Transformer L42:       2. cite32†A.3.2 $L_{2}$ norm of a token in value space L43:       3. cite33†A.3.3 Why attending to low-norm tokens approximates a “no-op” L44: cite34†License: arXiv.org perpetual non-exclusive license†info.arxiv.org L45: 
L46: arXiv:2601.19657v1 [cs.CL] 27 Jan 2026
L47: # One Token Is Enough: Improving Diffusion Language Models
L48: with a Sink Token
L49: Zihou Zhang Affiliation: Xiaohongshu.inc Code:cite35†https://github.com/skywalker0523/OneTokenIsEnough†github.com Zheyong Xie Affiliation: Xiaohongshu.inc Code:cite35†https://github.com/skywalker0523/OneTokenIsEnough†github.com Li Zhong Affiliation: Xiaohongshu.inc Code:cite35†https://github.com/skywalker0523/OneTokenIsEnough†github.com Haifeng Liu Affiliation: Xiaohongshu.inc Code:cite35†https://github.com/skywalker0523/OneTokenIsEnough†github.com Shaosheng Cao Affiliation: Xiaohongshu.inc Code:cite35†https://github.com/skywalker0523/OneTokenIsEnough†github.com L50: ###### Abstract
L51: Diffusion Language Models (DLMs) have emerged as a compelling alternative to autoregressive approaches, enabling parallel text generation with competitive performance. Despite these advantages, there is a critical instability in DLMs: the moving sink phenomenon. Our analysis indicates that sink tokens exhibit low-norm representations in the Transformer’s value space, and that the moving sink phenomenon serves as a protective mechanism in DLMs to prevent excessive information mixing.
L121: ### 3.2 Extra Sink Token for DLM
L199: #### 4.3.2 The number of sink token
L200: 
L201: Benchmark  | 0  | 1  | 2  | 4
L202: --- | --- | --- | --- | ---
L203: ARC-e  | 44.70  | 55.47  | 54.76  | 55.39
L204: ARC-c  | 27.13  | 32.17  | 32.42  | 31.47
L205: RACE  | 31.29  | 33.79  | 32.89  | 33.06
L206: HellaSwag  | 35.21  | 48.91  | 48.94  | 48.45
L207: PIQA  | 55.28  | 63.44  | 63.66  | 62.62
L208: Table 4: Performance sensitivity to the number of reintroduced tokens on our approach.
L238:   * Barbero et al. (2025) F. Barbero, A. Arroyo, X. Gu, C. Perivolaropoulos, M. Bronstein, P. Veličković, and R. Pascanu Why do llms attend to the first token?. arXiv preprint arXiv:2504.02732. Cited by: cite82†§1 , cite83†§1 , cite84†§2.2 , cite85†§3.2 .
L239:   * Bisk et al. (2020) Y. Bisk, R. Zellers, R. L. Bras, J. Gao, and Y. Choi Piqa: reasoning about physical commonsense in natural language. In Proceedings of the AAAI conference on artificial intelligence, Vol. 34, pp. 7432–7439. Cited by: cite86†§4.1.1 .
L314: #### A.3.2 $L_{2}$ norm of a token in value space
L315: 
L316: For a head-specific value vector, the $L_{2}$ norm is computed as
L317: 
L318:  | $$\left\|\mathbf{v}^{(\ell,m)}_{j}\right\|_{2}=\sqrt{\sum_{k=1}^{d_{h}}\left(\mathbf{v}^{(\ell,m)}_{j,k}\right)^{2}}.$$  |  | (15)
L319: 
L320: To obtain a single magnitude per token across heads, we average per-head norms:
L321: 
L322:  | $$\bar{r}^{(\ell)}_{j}=\frac{1}{M}\sum_{m=1}^{M}\left\|\mathbf{v}^{(\ell,m)}_{j}\right\|_{2}.$$  |  | (16)


## jan29_systemfour_core

One Token Is Enough: Improving Diffusion Language Models with a Sink Token (https://arxiv.org/html/2601.19657v1)
citeturn28516view1 [wordlim: 200] Crawled: 2 days ago; Content type: text/html; Source: open({"ref_id":"https://arxiv.org/html/2601.19657v1","lineno":121}); Total lines: 361
L105: where $t\in\{1,\ldots,T\}$ indexes diffusion steps and $T$ is the total number of steps. Each transition $q(x_{t}\mid x_{t-1})$ applies independent masking per position under a predefined noise schedule: at step $t$, a token remains unmasked with some probability, otherwise it is replaced by [MASK]. We set $x_{T}$ to be fully corrupted (all positions are [MASK]), so generation can start from a fixed maximally corrupted sequence and then denoise.
L106: #### 3.1.2 Reverse Process
L107: The reverse process iteratively denoises from $x_{T}$ back to $x_{0}$. We parameterize reverse transitions with a neural model $p_{\theta}$ that predicts tokens conditioned on the current corrupted sequence, i.e., $p_{\theta}(x_{t-1}\mid x_{t})$. Operationally, $p_{\theta}$ performs mask prediction: it predicts token identities at masked positions conditioned on $x_{t}$, and it predicts all masked tokens in parallel. A common choice treats positions independently given $x_{t}$, yielding
L108:  | $$p_{\theta}(x_{0}\mid x_{t})=\prod_{i=1}^{L}p_{\theta}(x_{0}^{i}\mid x_{t}).$$  |  | (2)
L109: 
L110: During generation, these conditionals are used to fill masked tokens to obtain a less corrupted sequence, repeating over steps until a fully specified $x_{0}$ is reached.
L111: #### 3.1.3 Training Objective
L112: 
L113: DLMs are trained with a cross-entropy objective computed only on masked positions. Let $\{\tau_{t}\}_{t=1}^{T}$ denote a predefined noise schedule, where $\tau_{t}\in(0,1]$ is the masking probability at diffusion step $t$. For a corrupted sequence $x_{t}$ produced from $x_{0}$, we define the masked-token log-likelihood as
L114:  | $\displaystyle\ell(x_{0},x_{t};\theta)$  | $\displaystyle=\frac{1}{\tau_{t}}\sum_{i=1}^{L}\mathbf{1}\!\left[x_{t}^{i}=[MASK]\right]$  |  | (3)
L115:  |  | $\displaystyle\log p_{\theta}\!\left(x_{0}^{i}\mid x_{t}\right).$  |
L116: 
L117: The indicator restricts the loss to masked positions. The overall training objective minimizes the negative expected masked-token log-likelihood:
L118: 
L119:  | $$\mathcal{L}(\theta)=-\mathbb{E}_{t,\,x_{0},\,x_{t}}\big[\ell(x_{0},x_{t};\theta)\big].$$  |  | (4)
L120: This objective learns a denoising function over partially observed sequences, enabling parallel token updates and avoiding strict left-to-right dependencies.
L121: ### 3.2 Extra Sink Token for DLM
L122: As illustrated in Figure cite47†1 , moving sink behavior is widely observed in existing DLMs. In the absence of a fixed low-norm anchor, the attention sink tends to shift unpredictably across tokens. These temporary sink tokens typically contain low semantic information and exhibit a lower $L_{2}$ norm. The root cause lies in the softmax operation which necessitates that attention weights sum to one, mirroring the attention sink behavior observed in autoregressive models cite45†Barbero et al. (2025) .
L123: When a token lacks a strong semantic match within the context, the model is forced to assign redundant attention mass to globally visible tokens, often turning content tokens into implicit sinks.
L124: However, this shifting behavior complicates the modeling of the diffusion process and hinders the improvement of DLMs. To address this issue and stabilize the attention mechanism, we introduce a dedicated extra sink token to the input sequence. This token is designed to serve as a stable, low-information target to absorb excess attention.
L125: To strictly enforce its role as a pure sink and prevent it from aggregating semantic information, we apply a structured attention mask with the following constraints: (1) the sink token is restricted to attend only to itself; and (2) all other tokens in the sequence are allowed to attend to the sink token.
L126: Formally, given an input sequence of latent representation $X\in\mathbb{R}^{L\times d_{\mathrm{model}}}$, we prepend an extra sink token embedding $s\in\mathbb{R}^{d_{\mathrm{model}}}$ to the sequence. The augmented input $\tilde{X}\in\mathbb{R}^{(L+1)\times d_{\mathrm{model}}}$ is given by:
L127: 
L128:  | $$\tilde{X}=[s;X].$$  |  | (5)
L129: 
L130: Let $k=0$ denote the index of the sink token $s$, we enforce the sink constraints by defining the attention mask bias $M_{ij}$ as:
L131:  | $$M_{ij}=\begin{cases}-\infty,&\text{if }i=k\text{ and }j\neq k\\
L132: 0,&\text{otherwise}\end{cases}$$  |  | (6)
L133: Under this formulation, the sink token is effectively isolated from aggregating sequence information, creating an asymmetric dependency where content tokens retain the ability to allocate attention mass to it. This constraint ensures that the sink token remains semantically neutral, functioning solely as a target to absorb excess attention weights. In our DLM framework, this configuration is applied consistently across all diffusion timesteps.
L134: Given that it introduces only a single additional token and utilizes standard masking, the computational overhead is negligible, providing an efficient and effective solution to regulate attention behavior and enhance model robustness.
L135: ## 4 Experiment
L136: Model  | Tokens  | ARC-e  | ARC-c  | HellaSwag  | PIQA  | RACE  | SIQA  | LAMBADA  | GSM8K
L137: --- | --- | --- | --- | --- | --- | --- | --- | --- | ---
L138: 0.5B Models
L139: ---
L140: DLM  | 30B  | 44.70  | 27.13  | 35.21  | 55.28  | 31.29  | 40.28  | 44.09  | 46.92
L141: DLM + extra token  | 30B  | 55.47  | 32.17  | 48.91  | 63.44  | 33.79  | 37.82  | 45.24  | 49.20
L142: DLM + GA  | 30B  | 47.85  | 29.27  | 41.95  | 61.92  | 34.07  | 36.08  | 45.10  | 47.01
L143: 1.5B Models
L144: ---
L145: DLM  | 100B  | 65.49  | 41.47  | 59.50  | 66.49  | 37.80  | 36.18  | 66.58  | 57.77
L146: DLM + extra token  | 100B  | 68.18  | 43.43  | 61.31  | 68.17  | 37.61  | 39.97  | 66.41  | 58.45
L147: DLM + GA  | 100B  | 53.03  | 32.27  | 52.90  | 60.33  | 37.42  | 38.26  | 51.10  | 52.35
L148: Table 1: Evaluation of our DLMs (autoregressive LLMs initialized). We report results for two model scales (0.5B and 1.5B), separated into two blocks for clarity. The “Tokens” column denotes the total number of training tokens used for each setting. “DLM + extra token” denotes the DLM augmented with an additional introduced sink token, while “DLM + GA” denotes the DLM equipped with the gated attention (GA) mechanism.
L149: Model  | Tokens  | ARC-e  | ARC-c  | HellaSwag  | PIQA  | RACE  | SIQA  | LAMBADA  | GSM8K
L150: --- | --- | --- | --- | --- | --- | --- | --- | --- | ---
L151: DLM  | 100B  | 32.20  | 25.09  | 31.56  | 54.08  | 31.77  | 35.98  | 29.26  | 34.95
L152: DLM + extra token  | 100B  | 40.91  | 22.35  | 40.43  | 62.24  | 32.73  | 37.92  | 47.16  | 35.17
L153: DLM + GA  | 100B  | 36.28  | 23.46  | 37.61  | 57.07  | 33.68  | 34.44  | 42.27  | 36.39


## jan29_systemfour_eval

One Token Is Enough: Improving Diffusion Language Models with a Sink Token (https://arxiv.org/html/2601.19657v1)
citeturn28517view1 [wordlim: 200] Crawled: 2 days ago; Content type: text/html; Source: open({"ref_id":"https://arxiv.org/html/2601.19657v1","lineno":158}); Total lines: 361
L148: Table 1: Evaluation of our DLMs (autoregressive LLMs initialized). We report results for two model scales (0.5B and 1.5B), separated into two blocks for clarity. The “Tokens” column denotes the total number of training tokens used for each setting. “DLM + extra token” denotes the DLM augmented with an additional introduced sink token, while “DLM + GA” denotes the DLM equipped with the gated attention (GA) mechanism.
L149: Model  | Tokens  | ARC-e  | ARC-c  | HellaSwag  | PIQA  | RACE  | SIQA  | LAMBADA  | GSM8K
L150: --- | --- | --- | --- | --- | --- | --- | --- | --- | ---
L151: DLM  | 100B  | 32.20  | 25.09  | 31.56  | 54.08  | 31.77  | 35.98  | 29.26  | 34.95
L152: DLM + extra token  | 100B  | 40.91  | 22.35  | 40.43  | 62.24  | 32.73  | 37.92  | 47.16  | 35.17
L153: DLM + GA  | 100B  | 36.28  | 23.46  | 37.61  | 57.07  | 33.68  | 34.44  | 42.27  | 36.39
L154: Table 2: Evaluation of DLMs (trained from scratch) on different benchmarks. The “Tokens” column denotes the total number of training tokens used for each setting. “DLM + extra token” denotes the DLM augmented with an additional introduced sink token, while “DLM + GA” denotes the DLM equipped with the gated attention (GA) mechanism.
L155: ### 4.1 Experiment Settings
L156: #### 4.1.1 Benchmarks
L157: To enable a thorough evaluation, we evaluate DLMs on widely adopted benchmarks spanning commonsense reasoning and reading comprehension: HellaSwag  cite65†Zellers et al. (2019) , ARC-e  cite66†Clark et al. (2018) , ARC-c  cite66†Clark et al. (2018) , PIQA  cite67†Bisk et al. (2020) , SIQA  cite68†Sap et al. (2019) , RACE  cite69†Lai et al. (2017) , and LAMBADA  cite70†Paperno et al. (2016) . Following prior studies cite50†Nie et al. (2025a) , we also evaluate mathematical reasoning ability of DLMs on GSM8K cite37†Cobbe et al.
L158: (2021) after the supervised fine-tune (SFT) process.
L159: #### 4.1.2 Implementation Details
L160: We conduct experiments under two training settings: (1) training a DLM initialized from an autoregressive LLM, and (2) training a DLM from scratch. For the former, we initialize the DLM with Qwen2.5 Base model weights cite71†Qwen et al. (2025) and consider two model scales, 0.5B ^{1}^{1} 1 https://huggingface.co/Qwen/Qwen2.5-0.5B and 1.5B ^{2}^{2} 2 https://huggingface.co/Qwen/Qwen2.5-1.5B parameters. These models are trained on the FineWeb dataset cite72†Penedo et al. (2024) .
L161: For the from-scratch setting, we adopt the same model architecture as the SMDM framework cite50†Nie et al. (2025a) . In this case, the model has 0.5B parameters and is trained on the SlimPajama dataset cite73†Soboleva et al. (2023) . During supervised fine-tuning (SFT), we fine-tune the DLM for 10 epochs on the augmented training data cite74†Deng et al. (2023) , with a context length of 2048. Additional training details are provided in Appendix cite28†A.1 .
L162: ### 4.2 Experiment Results
L163: 
L164: Under the setting of training Diffusion Language Models from autoregressive LLMs, we compare three DLM modeling strategies at the 0.5B and 1.5B parameter scales: (1) the vanilla DLM, (2) DLM equipped with element-wise gated attention cite62†Qiu et al. (2025) , and (3) DLM with an additional sink token. The experimental results are reported in Table cite75†1 . Implementation details for gated attention are provided in Appendix cite29†A.2 .
L165: At the 0.5B scale, both gated attention and the introduction of an additional sink token lead to consistent performance improvements over the vanilla DLM, demonstrating the effectiveness of these modifications. However, at the 1.5B scale, the DLM with gated attention exhibits degraded performance compared to the vanilla baseline. This suggests that, when training DLMs from larger autoregressive LLMs, forcibly introducing additional parameters to implement attention gating may harm model stability.
L166: In contrast, our approach of adding an extra sink token continues to yield performance gains at the 1.5B scale, highlighting its robustness and effectiveness under larger model settings.
L167: To further substantiate the effectiveness of our method, we extend our evaluation to training 0.5B-scale diffusion language models from scratch, maintaining the same baseline configurations as in the previous experiments. The results presented in Table cite76†2 demonstrate that our approach yields consistent improvements across different training paradigms, highlighting its robustness independent of the initialization setting.
L168: ### 4.3 Ablation Studies
L169: 
L170: In this part, we conduct ablation studies to analyze the contributions of different components. For efficiency, we utilize the Qwen2.5-0.5B checkpoint as the initialization and train on a subset of 30B tokens from FineWeb. Based on this setup, we examine the impact of sink token placement and quantity, followed by an in-depth analysis of how these tokens influence attention allocation.
L171: #### 4.3.1 The position of sink token
L172: 
L173: Benchmark  | Front  | End
L174: --- | --- | ---
L175: ARC-e  | 55.47  | 56.14
L176: ARC-c  | 32.17  | 32.51
L177: RACE  | 33.79  | 31.77
L178: HellaSwag  | 48.91  | 48.16
L179: PIQA  | 63.44  | 64.31
L180: Table 3: Evaluation of different sink token positions.
L181: Unlike autoregressive language models where the initial token naturally serves as an attention sink due to causal masking, diffusion language models utilize bidirectional attention with global context visibility.


## jan29_systemfour_settings

One Token Is Enough: Improving Diffusion Language Models with a Sink Token (https://arxiv.org/html/2601.19657v1)
citeturn28518view2 [wordlim: 200] Crawled: 2 days ago; Content type: text/html; Source: open({"ref_id":"https://arxiv.org/html/2601.19657v1","lineno":209}); Total lines: 361
L199: #### 4.3.2 The number of sink token
L200: 
L201: Benchmark  | 0  | 1  | 2  | 4
L202: --- | --- | --- | --- | ---
L203: ARC-e  | 44.70  | 55.47  | 54.76  | 55.39
L204: ARC-c  | 27.13  | 32.17  | 32.42  | 31.47
L205: RACE  | 31.29  | 33.79  | 32.89  | 33.06
L206: HellaSwag  | 35.21  | 48.91  | 48.94  | 48.45
L207: PIQA  | 55.28  | 63.44  | 63.66  | 62.62
L208: Table 4: Performance sensitivity to the number of reintroduced tokens on our approach.
L209: Next, we investigate the impact of sink token quantity to determine if the mechanism’s effectiveness is constrained by the capacity of a single token. To this end, we conduct an ablation study by varying the number of added tokens, specifically comparing configurations with 1, 2, and 4 sink tokens. The results, summarized in Table cite79†4 , reveal that adding a single sink token yields the most substantial improvement, while further increasing the quantity leads to negligible marginal gains.
L210: This saturation phenomenon indicates that the sink token functions purely as a structural anchor for attention offloading rather than a carrier of semantic information. Consequently, a single token provides sufficient capacity to fulfill this role.
L211: ### 4.4 Internal Analysis of Sink Tokens and Attention Allocation
L212: 
L213: Benchmark  | Stable sink token  | Zero-value token
L214: --- | --- | ---
L215: ARC-e  | 55.47  | 55.68
L216: ARC-c  | 32.17  | 32.94
L217: RACE  | 33.79  | 32.87
L218: HellaSwag  | 48.91  | 48.81
L219: PIQA  | 63.44  | 64.09
L220: Table 5: Evaluation for setting sink token to zero-vector in value space.
L221: To validate the effectiveness of our proposed theory beyond standard benchmarks, we conduct a statistical analysis of internal token representations and attention behaviors. Specifically, we examine DLMs initialized from Qwen2.5-0.5B and Qwen2.5-1.5B. Following supervised fine-tuning, we sample token representations in the value space and their corresponding attention maps across Transformer layers during inference on the GSM8K dataset.
L222: For each model, we sample 100K inference steps and quantify (i) the $L_{2}$ norm statistics of token representations in the value space and (ii) the attention mass allocated to sink tokens.


## jan29_systemfour_set2

One Token Is Enough: Improving Diffusion Language Models with a Sink Token (https://arxiv.org/html/2601.19657v1)
citeturn28519view2 [wordlim: 200] Crawled: 2 days ago; Content type: text/html; Source: open({"ref_id":"https://arxiv.org/html/2601.19657v1","lineno":275}); Total lines: 361
L268:   * Xin et al. (2025) Y. Xin, Q. Qin, S. Luo, K. Zhu, J. Yan, Y. Tai, J. Lei, Y. Cao, K. Wang, Y. Wang, J. Bai, Q. Yu, D. Jiang, Y. Pu, H. Chen, L. Zhuo, J. He, G. Luo, T. Li, M. Hu, J. Ye, S. Ye, B. Zhang, C. Xu, W. Wang, H. Li, G. Zhai, T. Xue, B. Fu, X. Liu, Y. Qiao, and Y. Liu Lumina-dimoo: an omni diffusion large language model for multi-modal generation and understanding. arXiv preprint arXiv:2510.06308. Cited by: cite89†§2.1 .
L269:   * Yang et al. (2025) L. Yang, Y. Tian, B. Li, X. Zhang, K. Shen, Y. Tong, and M. Wang Mmada: multimodal large diffusion language models. arXiv preprint arXiv:2505.15809. Cited by: cite89†§2.1 .
L270:   * Ye et al. (2025) J. Ye, Z. Xie, L. Zheng, J. Gao, Z. Wu, X. Jiang, Z. Li, and L. Kong Dream 7b: diffusion large language models. arXiv preprint arXiv:2508.15487. Cited by: cite92†§1 .
L271:   * You et al. (2025) Z. You, S. Nie, X. Zhang, J. Hu, J. Zhou, Z. Lu, J. Wen, and C. Li LLaDA-v: large language diffusion models with visual instruction tuning. arXiv preprint arXiv:2505.16933. Cited by: cite89†§2.1 .
L272:   * Zellers et al. (2019) R. Zellers, A. Holtzman, Y. Bisk, A. Farhadi, and Y. Choi Hellaswag: can a machine really finish your sentence?. arXiv preprint arXiv:1905.07830. Cited by: cite86†§4.1.1 .
L273:   * Zhang et al. (2025) S. Zhang, Y. Zhao, L. Geng, A. Cohan, A. T. Luu, and C. Zhao Diffusion vs. autoregressive language models: a text embedding perspective. In Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing, C. Christodoulopoulos, T. Chakraborty, C. Rose, and V. Peng (Eds.), Suzhou, China, pp. 4273–4303. External Links: ISBN 979-8-89176-332-6 Cited by: cite89†§2.1 .
L274:   * Zhao et al. (2025) S. Zhao, D. Gupta, Q. Zheng, and A. Grover D1: scaling reasoning in diffusion large language models via reinforcement learning. arXiv preprint arXiv:2504.12216. Cited by: cite82†§1 , cite89†§2.1 .
L275:   * Zhu et al. (2025) F. Zhu, R. Wang, S. Nie, X. Zhang, C. Wu, J. Hu, J. Zhou, J. Chen, Y. Lin, J. Wen, and C. Li LLaDA 1.5: variance-reduced preference optimization for large language diffusion models. arXiv preprint arXiv:2505.19223. Cited by: cite89†§2.1 .
L276: ## Appendix A Appendix
L277: ### A.1 Training details
L278: Training DLM from autoregressive LLM: We optimize the model using AdamW cite95†Loshchilov and Hutter (2017) , with $\beta_{1}=0.9$, $\beta_{2}=0.95$, and a weight decay of $0.1$. We adopt a cosine learning-rate schedule, with the peak learning rate set to $1\times 10^{-4}$ and the minimum learning rate set to $1\times 10^{-5}$, and use linear warmup for the first $1\%$ of the training tokens. For the 0.5B model, we train on 30B tokens from the FineWeb cite72†Penedo et al.
L279: (2024) dataset with a batch size of $512$. For the 1.5B model, we train on 100B tokens from the FineWeb dataset with a batch size of $4096$.
L280: Training DLM from scratch: To be consistent with the SMDM cite50†Nie et al. (2025a) , we utilize the AdamW optimizer cite95†Loshchilov and Hutter (2017) , setting $\beta_{1}=0.9$, $\beta_{2}=0.95$, and a weight decay of $0.1$. Additionally, we apply a cosine learning rate schedule with a maximum learning rate of $2\times 10^{-4}$ and a minimum learning rate of $2\times 10^{-5}$ with $1\%$ of the tokens for linear warmup. We train the model on 100B tokens from the SlimPajama dataset cite73†Soboleva et al.
L281: (2023) , using a batch size of $256$.
L282: ### A.2 Gated Attention for DLM
L283: 
L284: We augment the standard attention layer in DLMs with a gating mechanism applied after the scaled dot-product attention (SDPA). The overall Transformer architecture follows the same design as the Qwen model, and the gated attention layer is used as a drop-in replacement for the vanilla attention layer at every diffusion step.
L285: 
L286: Given the SDPA output
L287:  | $\displaystyle Y$  | $\displaystyle=\mathrm{Attention}(Q,K,V)$  |  | (8)
L288:  |  | $\displaystyle=\mathrm{softmax}\!\left(\frac{QK^{\top}}{\sqrt{d_{k}}}\right)V.$  |
L289: 
L290: we apply an element-wise, input-dependent gate to modulate the attention output:
L291: 
L292:  | $$Y^{\prime}=g(Y,X)=Y\odot\sigma(XW_{g}).$$  |  | (9)
L293: where $X\in\mathbb{R}^{n\times d_{\mathrm{model}}}$ is the input hidden representation to the attention layer, $W_{g}\in\mathbb{R}^{d_{\mathrm{model}}\times d_{k}}$ is a learnable gating projection, $\sigma(\cdot)$ denotes the sigmoid function, and $\odot$ represents element-wise multiplication.
L294: 
L295: The gated attention output is then passed to the output projection layer:
L296: 
L297:  | $$O=Y^{\prime}W_{O},$$  |  | (10)
L298: 
L299: where $W_{O}\in\mathbb{R}^{d_{k}\times d_{\mathrm{model}}}$.
L300: The gating function introduces non-linearity into the attention layer by dynamically scaling the SDPA output based on the current hidden states. Since the gate is applied after attention weight computation, it preserves the original attention score normalization while enabling adaptive suppression or amplification of attended features.
L301: In the context of DLMs, the same gated attention layer is applied across diffusion timesteps, allowing the model to regulate information flow under varying noise conditions with minimal additional computational overhead.
L302: ### A.3 Value-Space Token Vectors Analysis
L303: #### A.3.1 Value-space token vectors in a Transformer
L304: 
L305: Consider a Transformer layer $\ell$ with input hidden states $\mathbf{H}^{(\ell)}=[\mathbf{h}^{(\ell)}_{1},\ldots,\mathbf{h}^{(\ell)}_{n}]^{\top}\in\mathbb{R}^{n\times d}$, where $n$ is the sequence length and $d$ is the hidden size. For each attention head $m\in\{1,\ldots,M\}$, the layer computes query, key, and value projections:
L306:  | $\displaystyle\mathbf{Q}_{m}$  | $\displaystyle=\mathbf{H}^{(\ell)}\mathbf{W}^{Q}_{m},$  |  | (11)
L307:  | $\displaystyle\mathbf{K}_{m}$  | $\displaystyle=\mathbf{H}^{(\ell)}\mathbf{W}^{K}_{m},$  |  | (12)
L308:  | $\displaystyle\mathbf{V}_{m}$  | $\displaystyle=\mathbf{H}^{(\ell)}\mathbf{W}^{V}_{m},$  |  | (13)


## jan29_systemfour_last

One Token Is Enough: Improving Diffusion Language Models with a Sink Token (https://arxiv.org/html/2601.19657v1)
citeturn28521view3 [wordlim: 200] Crawled: 2 days ago; Content type: text/html; Source: find({"ref_id":"https://arxiv.org/html/2601.19657v1","pattern":"GPU"}); Total lines: 361
No matching text found for "GPU"
