[0] h5: Report GitHub Issue

[1] p: Content selection saved. Describe the issue below:

[2] h1: TabDLM : Free-Form Tabular Data Generation via Joint Numerical–Language Diffusion

[3] h6: Abstract

[4] p: Synthetic tabular data generation has attracted growing attention due to its importance for data augmentation, foundation models, and privacy. However, real-world tabular datasets increasingly contain free-form text fields (e.g., reviews or clinical notes) alongside structured numerical and categorical attributes. Generating such heterogeneous tables with joint modeling of different modalities remains challenging. Existing approaches broadly fall into two categories: diffusion-based methods and LLM-based methods. Diffusion models can capture complex dependencies over numerical and categorical features in continuous or discrete spaces, but extending them to open-ended text is nontrivial and often leads to degraded text quality. In contrast, LLM-based generators naturally produce fluent text, yet their discrete tokenization can distort precise or wide-range numerical values, hindering accurate modeling of both numbers and language. In this work, we propose TabDLM , a unified framework for free-form tabular data generation via a joint numerical–language diffusion model built on masked diffusion language models (MDLMs). TabDLM models textual and categorical features through masked diffusion, while modeling numerical features with a continuous diffusion process through learned specialized numeric tokens embedding; bidirectional attention then captures cross-modality interactions within a single model. Extensive experiments on diverse benchmarks demonstrate the effectiveness of TabDLM compared to strong diffusion- and LLM-based baselines. The code is available at https://github.com/ilikevegetable/TabDLM

[5] h6: Keywords:

[6] h2: 1 Introduction

[7] p: Tabular data is one of the most fundamental data types in modern machine learning and is indispensable across domains such as finance ( Sattarov et al., 2023 ) , healthcare ( Johnson et al., 2023 ) , and social media ( Lakkaraju et al., 2013 ) . In practice, however, deploying machine learning on tabular datasets faces recurring obstacles, including privacy and security constraints ( Hernandez et al., 2022 ; Assefa et al., 2020 ) , limited data availability ( Fonseca and Bacao, 2023 ) , and missing values ( Zheng and Charoenphakdee, 2022 ; You et al., 2020 ) . These challenges motivate synthetic tabular data generation, which seeks to produce synthetic samples that match the schema and key statistical properties of the original dataset for replacing the original data.

[8] p: High-fidelity synthetic tabular data generation remains challenging because real-world tables exhibit complex dependencies across columns ( Xu et al., 2019 ; Borisov et al., 2023 ) and often contain a mixture of numerical, categorical, and free-form textual features ( Shi et al., 2025 ) . Existing approaches can broadly be categorized into diffusion-based and large language model (LLM)-based methods. Diffusion-based methods employ diffusion processes ( Song and Ermon, 2019 ; Ho et al., 2020 ; Song et al., 2020 ; Austin et al., 2021 ) to learn denoising transformations that approximate the data distribution during training and to generate realistic samples from noise during inference. Such models have been widely applied to tabular data generation, particularly for continuous (numerical) features ( Kim et al., 2022 ; Kim et al., 2023 ; Zheng and Charoenphakdee, 2022 ) . More recent work has explored combining continuous and discrete diffusion to jointly model numerical and categorical attributes ( Zhang et al., 2024 ; Kotelnikov et al., 2023 ; Lee et al., 2023 ; Shi et al., 2025 ) . However, extending standard diffusion models to open-ended textual fields remains challenging due to the exponential size of the text space . To the best of our knowledge, no existing diffusion-based methods have been successfully applied to tabular data generation involving open-ended text. In contrast, LLM-based methods naturally support free-form text generation ( Borisov et al., 2023 ; Zhou et al., 2025 ) owing to their strong language modeling capabilities. However, their token-level representations can be unreliable for modeling high-precision or wide-range numerical values ( Yang et al., 2024 ) , as numbers are often fragmented into multiple tokens . Furthermore, autoregressive generation enforces a left-to-right dependency structure that is misaligned with the mutually dependent relationships across tabular columns.

[9] p: To address the above limitations, we propose TabDLM , a unified framework that integrates the complementary strengths of diffusion-based and LLM-based modeling. To preserve the most effective modeling paradigm for each modality, TabDLM employs continuous diffusion for numerical columns and language models for categorical and free-form textual columns. However, rather than relying on autoregressive language models, we adopt Masked Diffusion Language Models (MDLMs) as the backbone architecture. MDLMs offer two key advantages. First, their diffusion-based formulation enables TabDLM to model numerical and language modalities within a unified generative process. Second, unlike autoregressive models, MDLMs employ bidirectional attention, enabling the model to capture mutual dependencies among tabular columns. To enable joint numerical–language diffusion within a single MDLM, we introduce a trainable numerical tokenization module into the MDLM architecture, which allows continuous diffusion to represent each numerical value with a single token. As a result, TabDLM learns to jointly denoise numerical values and language content during training and generates synthetic tabular data by simultaneously performing continuous diffusion and masked language diffusion during inference. The overview of the TabDLM is provided in Figure 1 . We evaluate TabDLM across a range of scenarios and benchmarks, where it consistently outperforms both diffusion-based and language-based baselines.

[10] h2: 2 Methods

[11] figure: Figure 1 : Overview of TabDLM . During training, given an input tabular sample, TabDLM applies masked language diffusion to categorical and free-form textual features, and continuous diffusion to numerical features. Noisy inputs are mapped to token embeddings via a textual embedding layer and a numerical encoder. An MDLM then denoises these embeddings to reconstruct the original sample. Training updates only the projector in the numerical encoder and decoder, as well as the LoRA modules within each MDLM layer.

[12] h3: 2.1 Preliminary

[13] h5: Problem setup and notation.

[14] p: Let 𝒟 = { 𝐱 ( i ) } i = 1 N \mathcal{D}=\{\mathbf{x}^{(i)}\}_{i=1}^{N} denote a tabular dataset with M M columns. Each record is 𝐱 ( i ) = ( x 1 ( i ) , … , x M ( i ) ) \mathbf{x}^{(i)}=(x^{(i)}_{1},\dots,x^{(i)}_{M}) , where columns can be either numerical, categorical, or textual. We use index sets ℐ num \mathcal{I}_{\text{num}} , ℐ cat \mathcal{I}_{\text{cat}} , and ℐ txt \mathcal{I}_{\text{txt}} to denote numerical, categorical, and text columns, respectively. Our goal is to learn a generative model p θ ​ ( 𝐱 ) p_{\theta}(\mathbf{x}) that can sample realistic records while capturing cross-column dependencies.

[15] h5: Continuous diffusion.

[16] p: We model the distribution of a continuous vector 𝐳 0 ∈ ℝ d \mathbf{z}_{0}\in\mathbb{R}^{d} using a diffusion process defined by the stochastic differential equation (SDE) d ​ 𝐳 = 𝐟 ⁡ ( 𝐳 , t ) ​ d ​ t + g ⁡ ( t ) ​ d ​ 𝐰 \mathrm{d}\mathbf{z}=\mathbf{f}(\mathbf{z},t)\mathrm{d}t+g(t)\mathrm{d}\mathbf{w} . In the variance-exploding (VE) formulation ( Song et al., 2021 ) , we set 𝐟 ⁡ ( 𝐳 , t ) = 𝟎 \mathbf{f}(\mathbf{z},t)=\mathbf{0} and g ⁡ ( t ) = 2 ​ σ ˙ ​ ( t ) ​ σ ​ ( t ) g(t)=\sqrt{2\dot{\sigma}(t)\sigma(t)} , where σ ⁡ ( t ) : [ 0 , 1 ] → ℝ + \sigma(t):[0,1]\rightarrow\mathbb{R}_{+} is a strictly increasing function governing the noise level and σ ˙ ​ ( t ) = d ​ σ ​ ( t ) d ​ t \dot{\sigma}(t)=\frac{\mathrm{d}\sigma(t)}{\mathrm{d}t} denotes its time derivative. From a probabilistic perspective, this SDE corresponds to a continuous-time limit of a Markov chain where Gaussian noise is progressively added to the data. The transition kernel q ⁡ ( 𝐳 t ∣ 𝐳 s ) q(\mathbf{z}_{t}\mid\mathbf{z}_{s}) for s < t s<t and the marginal q ⁡ ( 𝐳 t ∣ 𝐳 0 ) q(\mathbf{z}_{t}\mid\mathbf{z}_{0}) are given by:

[17] table: q ⁡ ( 𝐳 t ∣ 𝐳 s ) \displaystyle q(\mathbf{z}_{t}\mid\mathbf{z}_{s}) = 𝒩 ⁡ ( 𝐳 s , ( σ 2 ​ ( t ) − σ 2 ​ ( s ) ) ​ 𝐈 ) , \displaystyle=\mathcal{N}\!\left(\mathbf{z}_{s},\,(\sigma^{2}(t)-\sigma^{2}(s))\mathbf{I}\right), (1) q ⁡ ( 𝐳 t ∣ 𝐳 0 ) \displaystyle q(\mathbf{z}_{t}\mid\mathbf{z}_{0}) = 𝒩 ⁡ ( 𝐳 0 , σ 2 ​ ( t ) ​ 𝐈 ) . \displaystyle=\mathcal{N}\!\left(\mathbf{z}_{0},\,\sigma^{2}(t)\mathbf{I}\right).

[18] p: The reverse generative process solves the probability flow ODE ( Song et al., 2021 ) , as described in the below:

[19] table: d ​ 𝐳 = − 1 2 ​ g ​ ( t ) 2 ​ ∇ 𝐳 ​ log ⁡ p t ​ ( 𝐳 ) ​ d ​ t = − σ ˙ ​ ( t ) ​ σ ​ ( t ) ​ ∇ 𝐳 ​ log ⁡ p t ​ ( 𝐳 ) ​ d ​ t . \mathrm{d}\mathbf{z}=-\frac{1}{2}g(t)^{2}\nabla_{\mathbf{z}}\log p_{t}(\mathbf{z})\mathrm{d}t=-\dot{\sigma}(t)\sigma(t)\nabla_{\mathbf{z}}\log p_{t}(\mathbf{z})\mathrm{d}t. (2)

[20] p: We use a parameterized denoising model ϵ θ ​ ( 𝐳 t , t ) \boldsymbol{\epsilon}_{\theta}(\mathbf{z}_{t},t) that estimates the score function via ∇ 𝐳 log p t ( 𝐳 ) ≈ − ϵ θ ( 𝐳 t , t ) / σ ( t ) \nabla_{\mathbf{z}}\log p_{t}(\mathbf{z})\approx-\boldsymbol{\epsilon}_{\theta}(\mathbf{z}_{t},t)/\sigma(t) . Training minimizes the denoising error:

[21] table: ℒ diff = 𝔼 t , 𝐳 0 , ϵ ​ [ ‖ ϵ − ϵ θ ​ ( 𝐳 0 + σ ⁡ ( t ) ​ ϵ , t ) ‖ 2 2 ] , ϵ ∼ 𝒩 ⁡ ( 𝟎 , 𝐈 ) . \mathcal{L}_{\mathrm{diff}}=\mathbb{E}_{t,\mathbf{z}_{0},\boldsymbol{\epsilon}}\left[\left\|\boldsymbol{\epsilon}-\boldsymbol{\epsilon}_{\theta}(\mathbf{z}_{0}+\sigma(t)\boldsymbol{\epsilon},t)\right\|_{2}^{2}\right],\ \ \boldsymbol{\epsilon}\sim\mathcal{N}(\mathbf{0},\mathbf{I}). (3)

[22] h5: Masked diffusion language models (MDLMs).

[23] p: MDLMs can be viewed as a discrete-state diffusion process ( Austin et al., 2021 ) over token sequences. Let 𝐬 0 = ( s 1 , … , s L ) \mathbf{s}_{0}=(s_{1},\dots,s_{L}) be a length- L L sequence with tokens in a vocabulary 𝒱 \mathcal{V} augmented with an absorbing mask state m = [ MASK ] m=[\mathrm{MASK}] . Using a token-wise Markov chain, the forward noising kernel factorizes as

[24] table: q ⁡ ( 𝐬 t ∣ 𝐬 t − 1 ) = ∏ j = 1 L q ⁡ ( s t , j ∣ s t − 1 , j ) , q(\mathbf{s}_{t}\mid\mathbf{s}_{t-1})=\prod_{j=1}^{L}q(s_{t,j}\mid s_{t-1,j}), (4)

[25] p: with a masking schedule β t ∈ [ 0 , 1 ] \beta_{t}\in[0,1] and absorbing transitions

[26] table: q ⁡ ( s t , j ∣ s t − 1 , j ) = { 1 , s t − 1 , j = m , s t , j = m , β t , s t − 1 , j ≠ m , s t , j = m , 1 − β t , s t − 1 , j ≠ m , s t , j = s t − 1 , j , 0 , otherwise , q(s_{t,j}\mid s_{t-1,j})=\begin{cases}1,&s_{t-1,j}=m,\ s_{t,j}=m,\\ \beta_{t},&s_{t-1,j}\neq m,\ s_{t,j}=m,\\ 1-\beta_{t},&s_{t-1,j}\neq m,\ s_{t,j}=s_{t-1,j},\\ 0,&\text{otherwise},\end{cases} (5)

[27] p: Equivalently, the marginal has the closed form q ⁡ ( s t , j = s 0 , j ∣ s 0 , j ) = α ¯ t q(s_{t,j}=s_{0,j}\mid s_{0,j})=\bar{\alpha}_{t} and q ⁡ ( s t , j = m ∣ s 0 , j ) = 1 − α ¯ t q(s_{t,j}=m\mid s_{0,j})=1-\bar{\alpha}_{t} , where α ¯ t = ∏ τ = 1 t ( 1 − β τ ) \bar{\alpha}_{t}=\prod_{\tau=1}^{t}(1-\beta_{\tau}) . The reverse model uses a bidirectional Transformer to predict the original token distribution from the partially masked sequence:

[28] table: p θ ​ ( 𝐬 0 ∣ 𝐬 t ) = ∏ j = 1 L p θ ​ ( s 0 , j ∣ 𝐬 t ) , p_{\theta}(\mathbf{s}_{0}\mid\mathbf{s}_{t})=\prod_{j=1}^{L}p_{\theta}(s_{0,j}\mid\mathbf{s}_{t}), (6)

[29] p: and is typically trained by maximizing the log-likelihood of the ground-truth tokens at corrupted (masked) positions:

[30] table: ℒ MDLM = 𝔼 t , 𝐬 0 , 𝐬 t [ − ∑ { j : s t , j = [ MASK ] } log p θ ( s 0 , j ∣ 𝐬 t ) ] . \mathcal{L}_{\mathrm{MDLM}}=\mathbb{E}_{t,\mathbf{s}_{0},\mathbf{s}_{t}}\left[-\sum_{\{j:\,s_{t,j}=[\text{MASK}]\}}\log p_{\theta}(s_{0,j}\mid\mathbf{s}_{t})\right]. (7)

[31] p: At sampling time, MDLMs start from an all-mask sequence and iteratively unmask tokens according to p θ p_{\theta} .

[32] h3: 2.2 The Model Architecture of TabDLM

[33] p: We first present the architecture of TabDLM . As illustrated in Figure 1 , TabDLM comprises five main components: (1) a numerical encoder module, (2) a text embedding layer, (3) a masked diffusion language model, (4) a numerical decoder module, and (5) an LM head. We describe each component in detail below. Note that in this section we use x ^ j ( i ) \hat{x}^{(i)}_{j} instead of x j ( i ) x^{(i)}_{j} to denote the noise version of the input. We will describe how we obtain the x ^ j ( i ) \hat{x}^{(i)}_{j} from x j ( i ) x^{(i)}_{j} in Section 2.3 .

[34] h5: Number encoder module.

[35] p: Given an input numerical value x ^ j ( i ) ∈ ℝ , j ∈ ℐ num \hat{x}^{(i)}_{j}\in\mathbb{R},j\in\mathcal{I}_{\text{num}} , the number encoder module transforms the number into a token embedding with the same size as the MDLM. To achieve this, we first use quantile normalization ( Bolstad et al., 2003 ) to standardize the numerical values as done in previous works ( Wang et al., 2025 ; Shi et al., 2025 ) . Then, we use a pretrained Multi-Layer Perceptron (MLP) as the float number encoder to convert the normalized values into an r r -dimensional embedding vector. Finally, a trainable projection is used to align the r r -dimensional embedding vector into the d d -dimensional MDLM embedding space:

[36] table: 𝐳 ^ j ( i ) = ENC ​ ( x ^ j ( i ) ) , 𝐳 j ( i ) = PROJ e ​ ( 𝐳 ^ j ( i ) ) , j ∈ ℐ num , \mathbf{\hat{z}}^{(i)}_{j}=\text{ENC}(\hat{x}^{(i)}_{j}),\ \ \mathbf{z}^{(i)}_{j}=\text{PROJ}_{e}(\mathbf{\hat{z}}^{(i)}_{j}),\ \ j\in\mathcal{I}_{\text{num}}, (8)

[37] p: where ENC and PROJ e \text{PROJ}_{e} denote the MLP-based encoder and projection module, respectively, with 𝐳 ^ j ( i ) ∈ ℝ r \hat{\mathbf{z}}^{(i)}_{j}\in\mathbb{R}^{r} and 𝐳 j ( i ) ∈ ℝ d \mathbf{z}^{(i)}_{j}\in\mathbb{R}^{d} . In our implementation, we pretrained ENC based on Griffin ( Wang et al., 2025 ) and keep it fixed throughout all experiments, while PROJ e \text{PROJ}_{e} is jointly optimized during training.

[38] h5: Text embedding layer.

[39] p: The text embedding layer transforms textual input features x ^ j ( i ) , j ∈ ℐ cat ∪ ℐ text \hat{x}^{(i)}_{j},j\in\mathcal{I}_{\text{cat}}\cup\mathcal{I}_{\text{text}} into a token embedding sequence. We directly adopt the pretrained embedding table from the underlying MDLM. Formally,

[40] table: 𝐳 j ( i ) = ( 𝐳 j , 1 ( i ) , … , 𝐳 j , l j i ( i ) ) = EMB ​ ( x ^ j ( i ) ) , j ∈ ℐ cat ∪ ℐ text , \mathbf{z}^{(i)}_{j}=(\mathbf{z}^{(i)}_{j,1},\ldots,\mathbf{z}^{(i)}_{j,l^{i}_{j}})=\text{EMB}(\hat{x}^{(i)}_{j}),j\in\mathcal{I}_{\text{cat}}\cup\mathcal{I}_{\text{text}}, (9)

[41] p: where each token embedding 𝐳 j , k ( i ) ∈ ℝ d , k ∈ [ l j i ] \mathbf{z}^{(i)}_{j,k}\in\mathbb{R}^{d},k\in[l^{i}_{j}] and l j i l^{i}_{j} denotes the token sequence length of column j j in sample i i , as each textual column may be mapped to multiple tokens in the MDLM embedding space.

[42] h5: Masked diffusion language model.

[43] p: The masked diffusion language model is employed to jointly denoise both numerical and textual tokens. Formally, given an input sequence of token embeddings 𝐳 ( i ) = ( 𝐳 1 ( i ) , … , 𝐳 S ( i ) ) \mathbf{z}^{(i)}=(\mathbf{z}^{(i)}_{1},\ldots,\mathbf{z}^{(i)}_{S}) of length S S and a diffusion time step t t , the MDLM outputs a denoised sequence 𝐨 ( i ) \mathbf{o}^{(i)} that estimates the corresponding representations at time t = 0 t=0 . In TabDLM , the input token sequence is constructed by concatenating four components: a schema prompt, categorical features, textual features, and numerical features. The schema prompt provides a textual description of the feature type and the semantic meaning of each column, which is fixed for a given dataset. Detailed, the input token sequence for sample i i is represented as:

[44] table: 𝐳 ( i ) = ( 𝐳 p , ( 𝐳 j ( i ) | j ∈ ℐ cat ∪ ℐ text ) , ( 𝐳 j ( i ) | j ∈ ℐ num ) ) , \displaystyle\mathbf{z}^{(i)}=\big(\mathbf{z}_{p},(\mathbf{z}_{j}^{(i)}|j\in\mathcal{I}_{\text{cat}}\cup\mathcal{I}_{\text{text}}),(\mathbf{z}_{j}^{(i)}|j\in\mathcal{I}_{\text{num}})\big),

[45] p: where 𝐳 p \mathbf{z}_{p} is the token embedding sequence for the schema prompt and 𝐳 j ( i ) = ( 𝐳 j , 1 ( i ) , … , 𝐳 j , l j i ( i ) ) \mathbf{z}_{j}^{(i)}=(\mathbf{z}^{(i)}_{j,1},\ldots,\mathbf{z}^{(i)}_{j,l^{i}_{j}}) for any j ∈ ℐ cat ∪ ℐ text j\in\mathcal{I}_{\text{cat}}\cup\mathcal{I}_{\text{text}} . The forward process of MDLM can be described as:

[46] table: 𝐨 ( i ) = MDLM ​ ( 𝐳 ( i ) , t ) . \mathbf{o}^{(i)}=\text{MDLM}(\mathbf{z}^{(i)},t). (10)

[47] p: For the MDLM architecture, we adopt a standard transformer architecture with bidirectional attention ( Vaswani et al., 2017 ; Devlin et al., 2019 ) . For numerical tokens, an additional positional embedding is added to encode the diffusion noise level applied to the input, following the design in DiT ( Peebles and Xie, 2023 ) . No such embedding is added for textual tokens, as the noise level can be implicitly captured by the proportion of masked tokens.

[48] h5: Number decoder module.

[49] p: The number decoder module is used to decode the output token embedding for the numerical value back to the original number. We use a symmetric version to the number encoder module with one trainable projection, along with a pretrained MLP decoder:

[50] table: 𝐨 ¯ j ( i ) = PROJ d ​ ( 𝐨 j ( i ) ) , x ¯ j ( i ) = DEC ​ ( 𝐨 ¯ j ( i ) ) , j ∈ ℐ num , \mathbf{\bar{o}}^{(i)}_{j}=\text{PROJ}_{d}(\mathbf{o}^{(i)}_{j}),\ \ \bar{x}^{(i)}_{j}=\text{DEC}(\mathbf{\bar{o}}^{(i)}_{j}),\ \ j\in\mathcal{I}_{\text{num}}, (11)

[51] p: where DEC and PROJ d \text{PROJ}_{d} denote the MLP-based decoder and projection module, respectively, with 𝐨 j ( i ) ∈ ℝ d \mathbf{o}^{(i)}_{j}\in\mathbb{R}^{d} representing the output token embedding from the MDLM and 𝐨 ¯ j ( i ) ∈ ℝ r \bar{\mathbf{o}}^{(i)}_{j}\in\mathbb{R}^{r} . Similarly, the DEC is pretrained jointly with the float number encoder and fixed during the experiment.

[52] h5: LM head.

[53] p: Finally, the LM head is used to decode the output token embedding for the textual value back to the original text. We directly use the frozen LM head from MDLM:

[54] table: x ¯ j ( i ) = HEAD ​ ( 𝐨 j ( i ) ) , j ∈ ℐ cat ∪ ℐ text . \bar{x}^{(i)}_{j}=\text{HEAD}(\mathbf{o}^{(i)}_{j}),\quad j\in\mathcal{I}_{\text{cat}}\cup\mathcal{I}_{\text{text}}. (12)

[55] h3: 2.3 The Forward Process of TabDLM

[56] p: The forward diffusion process typically adds noise to the input. In TabDLM , this process is applied to both numerical and textual modalities; for clarity, we describe the forward process for each modality separately.

[57] h5: Forward process of numerical features.

[58] p: For numerical features, we adopt continuous diffusion to better capture fine-grained distributions. Given a clean input value x j ( i ) , j ∈ ℐ num x^{(i)}_{j},j\in\mathcal{I}_{\text{num}} , we first sample a time t ∈ [ 0 , 1 ] t\in[0,1] . Then, according to Equation 1 , the forward process adds noise as follows:

[59] table: x ^ j ( i ) = x j ( i ) + σ ⁡ ( t ) ​ ϵ , ϵ ∼ 𝒩 ⁡ ( 0 , 1 ) , j ∈ ℐ num . \hat{x}^{(i)}_{j}=x^{(i)}_{j}+\sigma(t)\epsilon,\ \ \epsilon\sim\mathcal{N}(0,1),\ \ j\in\mathcal{I}_{\text{num}}. (13)

[60] p: Note that the noise is added in the normalized value.

[61] h5: Forward process of textual features.

[62] p: For textual features, we adopt discrete masked diffusion, as used in MDLMs. Given a text sequence x j ( i ) = ( x j , 1 ( i ) , … , x j , l j i ( i ) ) , j ∈ ℐ cat ∪ ℐ text x^{(i)}_{j}=(x^{(i)}_{j,1},\ldots,x^{(i)}_{j,l^{i}_{j}}),j\in\mathcal{I}_{\text{cat}}\cup\mathcal{I}_{\text{text}} , we first sample a time t ∈ [ 0 , 1 ] t\in[0,1] . Then, according to Equation 5 and the accompanying discussion, the forward process independently transforms each token into a mask token with probability 1 − α ¯ t 1-\bar{\alpha}_{t} , resulting in the masked token sequence x ^ j ( i ) = ( x ^ j , 1 ( i ) , … , x ^ j , l j i ( i ) ) \hat{x}^{(i)}_{j}=(\hat{x}^{(i)}_{j,1},\ldots,\hat{x}^{(i)}_{j,l^{i}_{j}}) .

[63] p: Finally, in TabDLM , we use a single t t for both continuous diffusion and discrete masked diffusion. This design enables the model to jointly denoise numerical and textual modalities under a unified noise level.

[64] h3: 2.4 Training of TabDLM

[65] p: During training, we optimize the TabDLM to jointly denoise both the numerical modality and textual modality. Specifically, given an output sequence 𝐨 ( i ) = ( 𝐨 p , ( 𝐨 j ( i ) | j ∈ ℐ cat ∪ ℐ text ) , ( 𝐨 j ( i ) | j ∈ ℐ num ) ) \mathbf{o}^{(i)}=\big(\mathbf{o}_{p},(\mathbf{o}_{j}^{(i)}|j\in\mathcal{I}_{\text{cat}}\cup\mathcal{I}_{\text{text}}),(\mathbf{o}_{j}^{(i)}|j\in\mathcal{I}_{\text{num}})\big) from MDLM, we first transform the numerical token embedding back to real number using the number decoder module and then the loss is computed separately for continuous diffusion and masked diffusion:

[66] table: ℒ num = 1 N ​ ∑ i = 1 N ∑ j ∈ ℐ num ‖ x j ( i ) − x ¯ j ( i ) ‖ 2 2 , j ∈ ℐ num , \mathcal{L}_{\text{num}}=\frac{1}{N}\sum_{i=1}^{N}\sum_{j\in\mathcal{I}_{\text{num}}}\left\|x^{(i)}_{j}-\bar{x}^{(i)}_{j}\right\|_{2}^{2},\quad j\in\mathcal{I}_{\text{num}}, (14)

[67] table: ℒ text = \displaystyle\mathcal{L}_{\text{text}}= 1 N ​ ∑ i = 1 N ∑ x ^ j , k ( i ) = [ MASK ] CE ​ < x ¯ j , k ( i ) , x j , k ( i ) > , \displaystyle\frac{1}{N}\sum^{N}_{i=1}\sum_{\hat{x}^{(i)}_{j,k}=[\text{MASK}]}\text{CE}<\bar{x}^{(i)}_{j,k},x^{(i)}_{j,k}>, (15) k ∈ [ l i j ] , j ∈ ℐ cat ∪ ℐ text , \displaystyle k\in[l^{i}_{j}],\quad j\in\mathcal{I}_{\text{cat}}\cup\mathcal{I}_{\text{text}},

[68] p: where CE < ⋅ , ⋅ > \text{CE}<\cdot,\cdot> is the cross entropy loss. The final objective is optimized using a step-dependent weighting schedule:

[69] table: ℒ = ℒ text + λ ⁡ ( s ) ​ ℒ num , λ ⁡ ( s ) = λ max ⋅ min ⁡ ( 1 , s s warm ) , \mathcal{L}=\mathcal{L}_{\text{text}}+\lambda(s)\,\mathcal{L}_{\text{num}},\ \ \lambda(s)=\lambda_{\max}\cdot\min\left(1,\frac{s}{s_{\text{warm}}}\right), (16)

[70] p: where s s denotes the global optimization step, and this warm-up schedule stabilizes the alignment of newly initialized numerical projections with the pretrained MDLM backbone. We use default hyperparameters λ max = 1 \lambda_{\max}=1 and s warm = 2000 s_{\text{warm}}=2000 . In practice, we freeze the pretrained weights of the MDLM and introduce trainable LoRA modules ( Hu et al., 2022 ) into both the feed-forward and attention components of each transformer layer.

[71] h3: 2.5 The backward sampling in TabDLM

[72] p: Finally, we describe the sampling process of TabDLM . After training, generation starts from noise and progressively denoises the inputs to produce synthetic tabular samples following the learned data distribution. For numerical modality, the process is initialized with pure Gaussian noise, while for textual modality, it starts from a fully masked token sequence. We then iteratively apply Equation 2 and Equation 6 to the numerical and textual modalities to recover clean data. More details are provided in Appendix B .

[73] h2: 3 Related Works

[74] p: Existing methods in tabular data generation can be classified into three categories based on their underlying frameworks.

[75] h5: VAE/GAN-based tabular generators.

[76] p: This line of work formulates tabular data generation using Variational Autoencoders (VAEs) ( Kingma and Welling, 2013 ) or Generative Adversarial Networks (GANs) ( Goodfellow et al., 2014 ) . Representative methods include CTGAN and TVAE ( Xu et al., 2019 ) . GOGGLE ( Liu et al., 2023 ) further enhances this paradigm by explicitly modeling column dependencies through a Graph Neural Network–augmented VAE architecture. However, these approaches often lack sufficient expressivity when confronted with complex tabular distributions involving intricate feature interactions.

[77] h5: Diffusion-based tabular generators.

[78] p: Motivated by the strong generative capacity of diffusion models ( Ho et al., 2020 ) , a growing body of work adapts diffusion processes for tabular data generation. Early methods model numerical and categorical features using separate discrete-time diffusion ( Austin et al., 2021 ) , as in Kotelnikov et al. (2023) ; Lee et al. (2023) , but discretization can lead to looser ELBO bounds and suboptimal generation quality ( Song et al., 2021 ; Kingma et al., 2021 ) . More recent approaches encode tabular features into continuous latent spaces and apply Gaussian diffusion ( Zheng and Charoenphakdee, 2022 ; Zhang et al., 2024 ) . However, such latent modeling introduces additional encoding overhead and may only indirectly capture heterogeneous feature interactions. Recently, CDTD ( Mueller et al., 2023 ) explores feature-wise noise schedules under continuous diffusion, and TabDiff ( Shi et al., 2025 ) further extends it to mixed-type feature-level diffusion.

[79] h5: Language model-based tabular generators.

[80] p: Recent advances in large language models have also inspired language model–based approaches for tabular data generation. These methods serialize each row into a text sequence and fine-tune an autoregressive language model to capture row-level distributions, as exemplified by GReaT ( Borisov et al., 2023 ) with a GPT-2 ( Radford et al., 2019 ) backbone. DiffLM ( Zhou et al., 2025 ) is the closest to our work, as it integrates VAEs and latent diffusion within a language modeling framework. However, DiffLM applies continuous diffusion in a latent space derived from textual representations, which may lose fine-grained token-level information and limit its applicability to free-form text fields. To the best of our knowledge, TabDLM is the first approach to apply masked language diffusion to explicitly model textual features at the token level, enabling faithful generation of free-form text in tabular data.

[81] h2: 4 Experiments

[82] p: In this section, we conduct extensive experiments to evaluate the proposed TabDLM . Specifically, we aim to answer the following questions. Q1: Can TabDLM effectively model the mutual dependencies among numerical, categorical, and free-form text columns? Q2: How well does TabDLM perform on real-world tabular data generation tasks involving free-form text columns? Q3: Can TabDLM achieve performance on par with existing methods on tasks that do not include textual columns? We implement TabDLM based on LLaDA-8B ( Nie et al., 2025 ) for all experiments. Other implementation details can be founded in Appendix B .

[83] h3: 4.1 Results on synthetic tabular datasets

[84] p: In this section, we try to answer the question Q1 through two carefully designed synthetic tabular datasets.

[85] h5: Datasets.

[86] p: Existing real-world tabular generation datasets predominantly focus on numerical and categorical features and lack free-form text fields. Thus, we construct two synthetic tabular datasets containing numerical, categorical, and free-form text columns: MathExpr and ProfileBio . MathExpr focuses on mathematical expressions. Each sample includes two floating-point variables, categorical features indicating the unary and binary operators applied to them, and a textual column containing the corresponding LaTeX expression. ProfileBio contains numerical and categorical attributes describing a person’s demographic and educational background, along with a textual biography generated from the other columns. For both datasets, accurate generation requires models to capture correlations between numerical, categorical, and textual columns . We show an example of both datasets in Table 1 and Table 2 , respectively, and leave the detailed dataset generation process in Appendix A.1 .

[87] figure: Table 1: An example sample from the MathExpr dataset. Column Example Value x 1 x_{1} 2.75 2.75 x 2 x_{2} 6.40 6.40 operation_x1 sin operation_x2 log operation_between mul latex_expression \sin(2.75) \times \log(6.40)

[88] figure: Table 2: An example sample from the ProfileBio dataset. Column Example Value age 38 38 salary 135 135 sex female birth_state California college Harvard University degree master occupation software developer biography She is a software developer with a master’s degree who enjoys building scalable systems and mentoring junior engineers.

[89] h5: Baselines.

[90] p: Given these two datasets contain free-form textual features, we compare the proposed TabDLM with the autoregressive LLM and Masked Diffusion LLM. Specifically, we include Qwen2.5 (7B/14B) with 3-shot in-context learning (ICL), and Qwen2.5-7B and LLaDA-8B with LoRA-based supervised fine-tuning (SFT).

[91] h5: Metrics.

[92] p: We evaluate the distribution fidelity of generated data through Shape and Trend metrics. Shape assesses whether the synthetic data preserves the marginal distributions of individual columns, while Trend evaluates the extent to which cross-column dependencies in the real data are reproduced. Across all experiments, we report the error rate for both metrics. To further assess cross-field consistency between free-form text and the associated numerical and categorical features, we introduce dataset-specific metrics. For MathExpr, we evaluate whether the generated LaTeX expression matches the corresponding numerical values and operation descriptors. We report the Operation match rate (Op-MR) to compute the match rate between LaTeX and operations and the Expression match rate (Exp-MR) to compute the match rate between LaTeX with both operations and numerical number. For ProfileBio, we measure whether the generated biography aligns with key information implied by the numerical and categorical attributes, reported as Biography Match Rate (Bio-MR). Detailed definitions of all metrics are provided in Appendix A.2 .

[93] figure: Table 3 : Evaluation results on the MathExpr dataset (%). Method Shape ↓ \downarrow Trend ↓ \downarrow Op-MR ↑ \uparrow Exp-MR ↑ \uparrow Qwen2.5-7B ICL {}_{\text{ICL}} 43.47 43.47 50.73 50.73 53.13 53.13 52.96 52.96 Qwen2.5-14B ICL {}_{\text{ICL}} 30.99 30.99 44.67 44.67 77.24 77.24 75.93 75.93 Qwen2.5-7B SFT {}_{\text{SFT}} 8.93 8.93 20.95 20.95 100.0 100.0 LLaDA-8B SFT {}_{\text{SFT}} 4.54 4.54 48.55 48.55 98.28 98.28 97.84 97.84 TabDLM 1.61 4.70 99.71 99.71 98.07 98.07

[94] h5: Results on MathExpr.

[95] p: As shown in Table 3 . TabDLM achieves the best overall fidelity on MathExpr dataset, yielding the lowest Shape and Trend errors and outperforming the strongest baseline by 64.8 % 64.8\% and 77.6 % 77.6\% , respectively. Although Qwen2.5-7B SFT {}_{\text{SFT}} achieves a slightly higher Match Rate than TabDLM , this is expected in settings where numerical values from structured columns are reproduced verbatim in the target expression. In such cases, autoregressive LLMs can exploit sequential dependencies: once numerical fields are generated, the subsequent L a T e X expression can be produced by learning a near-deterministic mapping that copies these values into a fixed template. In contrast, MDLM-style generation predicts tokens at arbitrary positions and therefore does not benefit from an explicit “copy-after-seeing” inductive bias. However, this advantage is difficult to leverage in realistic scenarios with more complex correlations, as we demonstrate in Section 4.2 . Notably, TabDLM still outperforms LLaDA-8B SFT {}_{\text{SFT}} on both Operation Match Rate and Match Rate, indicating that our joint numerical–language design better preserves cross-modality consistency, even when both methods share the same MDLM backbone for text.

[96] figure: Table 4: Evaluation results on the ProfileBio dataset (%). Method Shape ↓ \downarrow Trend ↓ \downarrow MR ↑ \uparrow Qwen2.5-7B ICL {}_{\text{ICL}} 34.66 34.66 55.12 55.12 2.24 2.24 Qwen2.5-14B ICL {}_{\text{ICL}} 39.31 39.31 55.98 55.98 4.09 4.09 Qwen2.5-7B SFT {}_{\text{SFT}} 7.26 7.26 14.65 14.65 99.98 LLaDA-8B SFT {}_{\text{SFT}} 4.50 4.50 28.45 28.45 97.24 97.24 TabDLM 3.43 7.45 95.91 95.91

[97] h5: Results on ProfileBio.

[98] p: As shown in Table 4 , TabDLM yields the lowest Shape and Trend errors, effectively preserving the complex probabilistic dependencies defined in the data. While TabDLM does not obtain the best Match Rate, it still achieves highly competitive cross-field consistency, indicating that most generated biographies remain semantically consistent with the corresponding structured attributes. A plausible explanation is that Match Rate primarily rewards deterministic range-to-text mappings and template-like realizations, which can be strongly reinforced by SFT and thus favors Qwen2.5-7B SFT {}_{\text{SFT}} . In contrast, TabDLM adopts a unified joint diffusion process that emphasizes distribution-level fidelity and cross-field dependency modeling, leading to better overall distributional fidelity (Shape/Trend) while maintaining coherent grounding between structured attributes and biography text.

[99] h3: 4.2 Results on real-world tabular dataset with free-form text features

[100] p: In this section, we answer Q2 by evaluating TabDLM on real-world tabular dataset with free-form text features.

[101] figure: Table 5 : Results on the Amazon dataset. ( ∗ indicates (w/o nums) ) Method Shape (%) ↓ \downarrow Trend (%) ↓ \downarrow MLE ∗ \text{MLE}^{*} ↑ \uparrow MLE ↑ \uparrow Real 0.0 0.0 0.0 0.0 .905 .905 .906 .906 Qwen2.5-7B ICL {}_{\text{ICL}} 37.93 37.93 68.27 68.27 .636 .636 .629 .629 Qwen2.5-14B ICL {}_{\text{ICL}} 39.19 39.19 78.22 78.22 .684 .684 .679 .679 Qwen2.5-7B SFT {}_{\text{SFT}} 11.41 11.41 46.31 46.31 .824 .824 .834 .834 LLaDA-8B SFT {}_{\text{SFT}} 7.76 7.76 37.13 37.13 .891 .891 .892 .892 TabDLM 4.67 5.33 .893 .895

[102] figure: Table 6 : Performance comparison on the error rates (%) of Shape ↓ \downarrow . ( B : best overall; B : best in language-based model) Method Adult Default Shoppers Magic Beijing Average CTGAN 16.84 ± 0.03 16.84\pm 0.03 16.83 ± 0.04 16.83\pm 0.04 21.15 ± 0.10 21.15\pm 0.10 9.81 ± 0.08 9.81\pm 0.08 21.39 ± 0.05 21.39\pm 0.05 17.20 17.20 TVAE 14.22 ± 0.08 14.22\pm 0.08 10.17 ± 0.05 10.17\pm 0.05 24.51 ± 0.06 24.51\pm 0.06 8.25 ± 0.06 8.25\pm 0.06 19.16 ± 0.06 19.16\pm 0.06 15.26 15.26 GOGGLE 16.97 16.97 17.02 17.02 22.33 22.33 1.90 1.90 16.93 16.93 15.03 15.03 STaSy 11.29 ± 0.06 11.29\pm 0.06 5.77 ± 0.06 5.77\pm 0.06 9.37 ± 0.09 9.37\pm 0.09 6.29 ± 0.13 6.29\pm 0.13 6.71 ± 0.03 6.71\pm 0.03 7.89 7.89 CoDi 21.38 ± 0.06 21.38\pm 0.06 15.77 ± 0.07 15.77\pm 0.07 31.84 ± 0.05 31.84\pm 0.05 11.56 ± 0.26 11.56\pm 0.26 16.94 ± 0.02 16.94\pm 0.02 19.50 19.50 TabDDPM 1.75 ± 0.03 1.75\pm 0.03 1.57 ± 0.08 1.57\pm 0.08 2.72 ± 0.13 2.72\pm 0.13 1.01 ± 0.09 1.01\pm 0.09 1.30 ± 0.03 1.30\pm 0.03 1.67 1.67 TabSyn 0.81 ± 0.05 0.81\pm 0.05 1.01 ± 0.08 \mathbf{1.01\pm 0.08} 1.44 ± 0.07 1.44\pm 0.07 1.03 ± 0.14 1.03\pm 0.14 1.26 ± 0.05 1.26\pm 0.05 1.11 1.11 TabDiff 0.63 ± 0.05 \mathbf{0.63\pm 0.05} 1.24 ± 0.07 1.24\pm 0.07 1.28 ± 0.09 \mathbf{1.28\pm 0.09} 0.78 ± 0.08 \mathbf{0.78\pm 0.08} 1.03 ± 0.05 \mathbf{1.03\pm 0.05} 0.99 GReaT 12.12 ± 0.04 12.12\pm 0.04 19.94 ± 0.06 19.94\pm 0.06 14.51 ± 0.12 14.51\pm 0.12 16.16 ± 0.09 16.16\pm 0.09 8.25 ± 0.12 8.25\pm 0.12 14.20 14.20 DiffLM 9.74 9.74 9.06 9.06 10.07 10.07 7.53 7.53 6.35 6.35 8.55 8.55 Qwen2.5-7B ICL {}_{\text{ICL}} 27.80 27.80 22.39 22.39 34.37 34.37 13.41 13.41 31.83 31.83 25.96 25.96 Qwen2.5-14B ICL {}_{\text{ICL}} 25.17 25.17 21.52 21.52 51.21 51.21 17.51 17.51 29.76 29.76 29.03 29.03 Qwen2.5-7B SFT {}_{\text{SFT}} 5.11 5.11 2.58 2.58 8.76 8.76 7.53 7.53 3.78 3.78 5.55 5.55 LLaDA-8B SFT {}_{\text{SFT}} 1.69 1.69 2.00 2.00 13.56 13.56 1.57 \mathbf{1.57} 1.31 \mathbf{1.31} 4.03 4.03 TabDLM 1.46 \mathbf{1.46} 1.18 \mathbf{1.18} 2.05 \mathbf{2.05} 2.93 2.93 3.06 3.06 2.14 \mathbf{2.14}

[103] h5: Dataset and Baselines.

[104] p: For this section, we use the Amazon dataset, which is derived from the RelBench ( Robinson et al., 2024 ) rel-amazon relational benchmark by converting multiple relational tables into a single heterogeneous table containing numerical attributes, categorical attributes, and multiple long-text fields (e.g., title, description, and review). We provide more details on dataset generation in Appendix A.1.3 . We use the same baseline as in Section 4.1 .

[105] h5: Metrics.

[106] p: Similar to Section 4.1 , we evaluate the distribution fidelity of generated data by shape and trend metrics. In addition to that, we also include a downstream utility metric. Here, we adopt Machine Learning Efficiency (MLE), which measures how well predictive models trained on synthetic data generalize to real test data. Finally, to evaluate cross-field consistency between free-form text and the remaining numerical and categorical features, we follow an MLE-like protocol: we first serialize all non-numerical fields into structured text and encode them with the sentence embedding model Nomic ( Nussbaum et al., 2025 ) , then train an XGBoost Classifier ( Chen and Guestrin, 2016 ) using either (i) text embeddings only or (ii) text embeddings concatenated with numerical features, which isolates the contribution of generated text/categorical fields. For the Amazon dataset, we report AUC for MLE task.

[107] h5: Results.

[108] figure: Table 7 : Performance comparison on the error rates (%) of Trend ↓ \downarrow .( B : best overall; B : best in language-based model) Method Adult Default Shoppers Magic Beijing Average CTGAN 20.23 ± 1.20 20.23\pm 1.20 26.95 ± 0.93 26.95\pm 0.93 13.08 ± 0.16 13.08\pm 0.16 7.00 ± 0.19 7.00\pm 0.19 22.95 ± 0.08 22.95\pm 0.08 18.04 18.04 TVAE 14.15 ± 0.88 14.15\pm 0.88 19.50 ± 0.95 19.50\pm 0.95 18.67 ± 0.38 18.67\pm 0.38 5.82 ± 0.49 5.82\pm 0.49 18.01 ± 0.08 18.01\pm 0.08 15.23 15.23 GOGGLE 45.29 45.29 21.94 21.94 23.90 23.90 9.47 9.47 45.94 45.94 29.31 29.31 STaSy 14.51 ± 0.25 14.51\pm 0.25 5.96 ± 0.26 5.96\pm 0.26 8.49 ± 0.15 8.49\pm 0.15 6.61 ± 0.53 6.61\pm 0.53 8.00 ± 0.10 8.00\pm 0.10 8.71 8.71 CoDi 22.49 ± 0.08 22.49\pm 0.08 68.41 ± 0.05 68.41\pm 0.05 17.78 ± 0.11 17.78\pm 0.11 6.53 ± 0.25 6.53\pm 0.25 7.07 ± 0.15 7.07\pm 0.15 24.46 24.46 TabDDPM 3.01 ± 0.25 3.01\pm 0.25 4.89 ± 0.10 4.89\pm 0.10 6.61 ± 0.16 6.61\pm 0.16 1.70 ± 0.22 1.70\pm 0.22 2.71 ± 0.09 2.71\pm 0.09 3.78 3.78 TabSyn 1.93 ± 0.07 1.93\pm 0.07 2.81 ± 0.48 2.81\pm 0.48 2.13 ± 0.10 2.13\pm 0.10 0.88 ± 0.18 0.88\pm 0.18 3.13 ± 0.34 3.13\pm 0.34 2.18 2.18 TabDiff 1.49 ± 0.16 \mathbf{1.49\pm 0.16} 2.55 ± 0.75 2.55\pm 0.75 1.74 ± 0.08 \mathbf{1.74\pm 0.08} 0.76 ± 0.12 \mathbf{0.76\pm 0.12} 2.59 ± 0.15 \mathbf{2.59\pm 0.15} 1.83 GReaT 17.59 ± 0.22 17.59\pm 0.22 70.02 ± 0.12 70.02\pm 0.12 45.16 ± 0.18 45.16\pm 0.18 10.23 ± 0.40 10.23\pm 0.40 59.60 ± 0.55 59.60\pm 0.55 40.52 40.52 Qwen2.5-7B ICL {}_{\text{ICL}} 37.61 37.61 31.02 31.02 34.77 34.77 20.62 20.62 40.83 40.83 32.97 32.97 Qwen2.5-14B ICL {}_{\text{ICL}} 42.67 42.67 28.72 28.72 42.32 42.32 18.11 18.11 38.20 38.20 34.00 34.00 Qwen2.5-7B SFT {}_{\text{SFT}} 17.03 17.03 16.99 16.99 10.28 10.28 14.45 14.45 7.23 7.23 13.20 13.20 LLaDA-8B SFT {}_{\text{SFT}} 26.15 26.15 26.30 26.30 16.42 16.42 24.55 24.55 35.26 35.26 25.74 25.74 TabDLM 2.74 \mathbf{2.74} 2.33 2.40 \mathbf{2.40} 2.85 \mathbf{2.85} 3.99 \mathbf{3.99} 2.86 \mathbf{2.86}

[109] p: The detailed results for Shape, Trend, and MLE metrics are presented in Table 5 . TabDLM consistently outperforms all baselines by a substantial margin on both Shape and Trend metrics. Specifically, TabDLM reduces the Shape Error by 39.8 % 39.8\% and the Trend Error by 85.6 % 85.6\% compared to the strongest baseline, LLaDA-8B SFT {}_{\text{SFT}} . The results align with the previous section and further confirm TabDLM ’s superior capacity in maintaining the marginal distributions and complex inter-column dependencies of the original training data, even with the existence of free-form textual fields. Regarding predictive utility, TabDLM achieves the best overall performance among all baselines in terms of MLE, which closely approaches the upper bound set by real data. This demonstrates that TabDLM ’s generated text, categorical, and numerical fields effectively preserve label-relevant information. Notably, when numerical attributes are excluded, the performance of TabDLM on MLE (w/o nums) exhibits a decline consistent with the trend observed in real data. This drop indicates that the synthetic numerical features are not merely reproducing marginal column statistics, but are meaningfully coupled with both target labels and other feature modalities, thereby providing substantive value for downstream predictive tasks. The suboptimal performance of Qwen2.5-7B SFT {}_{\text{SFT}} also suggests that autoregressive models struggle to learn the true data distribution when copy-after-seeing shortcuts are unavailable.

[110] h3: 4.3 Results on real-world tabular dataset without free-form text features

[111] p: Finally, we evaluate the performance of TabDLM on standard tabular data generation benchmarks without free-form text features, enabling direct comparison with existing methods. This evaluation addresses Q3 by examining whether TabDLM retains strong modeling capacity on traditional tabular data, despite being designed for a significantly broader heterogeneous generation setting.

[112] h5: Datasets, baselines, and metrics.

[113] p: We conduct experiments on five real-world tabular datasets: Adult, Default, Shoppers, Magic, and Beijing. Detailed dataset profiles are presented in Appendix A.1.4 . For baselines, we compare TabDLM with some widely-used synthetic tabular data generation methods from four categories: 1) GAN-based: CTGAN ( Xu et al., 2019 ) ; 2) VAE-based: TVAE ( Xu et al., 2019 ) and GOGGLE ( Liu et al., 2023 ) ; 3) Autoregressive Tabular Language Model: GReaT ( Borisov et al., 2023 ) and DiffLM ( Zhou et al., 2025 ) ; 4) Diffusion-based: STaSy ( Kim et al., 2023 ) , CoDi ( Lee et al., 2023 ) , TabDDPM ( Kotelnikov et al., 2023 ) , TabSyn ( Zhang et al., 2024 ) , and TabDiff ( Shi et al., 2025 ) . We evaluate the distribution fidelity of generated data by shape and trend metrics and downstream utility by MLE metric, similar to Section 4.2 .

[114] h5: Results.

[115] p: As reported in Tables 6 , 7 , TabDLM performs competitively with state-of-the-art tabular diffusion models on Shape and Trend. This is notable because such tabular-specific synthetic methods operate in a relatively restricted feature space (e.g., categorical columns are represented via one-hot vectors or limited discrete states), whereas TabDLM is built to jointly model heterogeneous fields and ultimately support open-ended text generation, yet it still remains strong on purely numerical and categorical datasets. Beyond this competitiveness against tabular-specific methods, TabDLM consistently and substantially outperforms all language-based baselines on real-world datasets. The results of MLE is provided in Appendix C.1

[116] p: In particular, TabDLM achieves the best Shape and Trend scores across most datasets relative to language-based baselines (a 46.9 % 46.9\% gain in Shape and a 78.3 % 78.3\% gain in Trend). This mirrors our findings on free-form tabular datasets: language-based generators often achieve reasonable Shape but markedly worse Trend . A likely reason is that row serialization simplifies matching column-wise marginals, as each field can be generated locally to fit its token-level distribution. However, Trend depends on modeling joint cross-column dependencies, which is particularly difficult across heterogeneous feature types. In practice, numerical values are represented as subword token sequences with precision-sensitive semantics, whereas categorical fields act as discrete identifiers, making consistent numerical–categorical correlations hard to preserve under autoregressive generation. In contrast, TabDLM jointly generates numerical and categorical features within a unified diffusion process and leverages bidirectional interactions across columns, enabling more direct modeling of tabular dependencies than left-to-right row generation and yielding greater fidelity and downstream utility on structured datasets.

[117] h2: 5 Limitations

[118] p: First, the sampling efficiency of TabDLM is lower than that of existing tabular data generation methods such as TabDiff ( Shi et al., 2025 ) and TabSyn ( Zhang et al., 2024 ) . This limitation can be primarily attributed to the large model size of the MDLM backbone. Nevertheless, TabDLM is designed for broader application scenarios, as it supports the generation of numerical, categorical, and free-form text fields, capabilities that exceed those of existing methods. Moreover, common methods for accelerating MDLM inference, like block diffusion ( Arriola et al., 2025 ) and KV caching ( Wu et al., 2025 ) , could be incorporated to improve sampling efficiency. However, it is out of the scope of this work. Second, TabDLM models numerical and language diffusion using a shared noise schedule that couples the denoising dynamics across modalities and enforces a common step size for denoising both numerical and textual features. While effective in practice, this design may be suboptimal in certain scenarios. Introducing modality-specific noise schedules to partially decouple the denoising processes can be promising, which we leave for future investigation.

[119] h2: 6 Conclusion

[120] p: In this work, we propose TabDLM , the first unified framework that can generate high-fidelity synthetic tabular data with both numeric, categorical, and free-form text features. TabDLM leverage MDLM with special numerical tokenization to allow a single model to perform joint numerical-language diffusion. Extensive experiments validate the effectiveness of TabDLM over baseline models.

[121] h2: References

[122] h2: Appendix A Detailed Experiment Setups

[123] h3: A.1 Datasets

[124] h4: A.1.1 MathExpr

[125] p: MathExpr is a synthetic dataset designed to evaluate joint generation of heterogeneous tabular records that contain numerical values, categorical operators, and a free-form LaTeX expression grounded in other column features. Each record consists of two continuous numerical variables ( x 1 , x 2 ) (x_{1},x_{2}) , three categorical columns indicating the applied unary/binary operations, and a text column containing the resulting expression:

[126] table: ( x 1 , x 2 , o 1 , o 2 , o 3 , e latex ) ({\color[rgb]{0.15,0.35,0.75}x_{1}},{\color[rgb]{0.15,0.35,0.75}x_{2}},{\color[rgb]{0.1,0.55,0.25}o_{1}},{\color[rgb]{0.1,0.55,0.25}o_{2}},{\color[rgb]{0.1,0.55,0.25}o_{3}},{\color[rgb]{0.55,0.2,0.55}e_{\texttt{latex}}})

[127] p: where o 1 o_{1} and o 2 o_{2} are unary operators applied to x 1 x_{1} and x 2 x_{2} , o 3 o_{3} is a binary operator combining the two transformed terms, and e latex = L a T e X ​ { ( o 1 ​ ( x 1 ) ) ​ o 3 ​ ( o 2 ​ ( x 2 ) ) } e_{\texttt{latex}}=\text{\LaTeX}\{(o_{1}(x_{1}))\ o_{3}\ (o_{2}(x_{2}))\} is a LaTeX string deterministically constructed from the preceding structured columns. We generate 5,000 5{,}000 samples in total and randomly split them into train/real set and validation set with ratio 9:1. During sampling, each model generates a synthetic dataset with the same cardinality as the real set (i.e., 4,500 4{,}500 synthetic samples), which is then used to compute the distribution fidelity metrics and expression consistency metrics described in Appendix A.2.3 .

[128] p: Numerical values sampling. We sample x 1 x_{1} and x 2 x_{2} from discrete supports with step size 0.1 0.1 : x 1 ∈ { 0.0 , 0.1 , … , 6.0 } x_{1}\in\{0.0,0.1,\dots,6.0\} and x 2 ∈ { 3.0 , 3.1 , … , 10.0 } x_{2}\in\{3.0,3.1,\dots,10.0\} . To induce a non-uniform yet diverse distribution, we draw x 1 x_{1} and x 2 x_{2} using a discrete Gaussian distribution centered at ( μ 1 , μ 2 ) (\mu_{1},\mu_{2}) with standard deviation σ \sigma . We use μ 1 = 3 \mu_{1}=3 , μ 2 = 6.5 \mu_{2}=6.5 , and σ = 1.0 \sigma=1.0 to generate the final dataset.

[129] p: Categorical operators sampling. Unary operators o 1 o_{1} and o 2 o_{2} are sampled independently for x 1 x_{1} and x 2 x_{2} from:

[130] table: 𝒪 unary = { none , log , exp , sqrt , sin , cos , tan , square , cube } , \mathcal{O}_{\text{unary}}=\{\texttt{none},\texttt{log},\texttt{exp},\texttt{sqrt},\texttt{sin},\texttt{cos},\texttt{tan},\texttt{square},\texttt{cube}\},

[131] p: using fixed categorical priors: p ( o 1 ) = { none : 0.18 , log : 0.16 , sqrt : 0.13 , square : 0.12 , sin : 0.10 , cos : 0.10 , tan : 0.07 , exp : 0.07 , cube : 0.07 } p(o_{1})=\{\texttt{none}:0.18,\ \texttt{log}:0.16,\ \texttt{sqrt}:0.13,\ \texttt{square}:0.12,\ \texttt{sin}:0.10,\ \texttt{cos}:0.10,\ \texttt{tan}:0.07,\ \texttt{exp}:0.07,\ \texttt{cube}:0.07\} , p ( o 2 ) = { none : 0.22 , sin : 0.14 , cos : 0.14 , sqrt : 0.12 , log : 0.10 , square : 0.09 , tan : 0.07 , exp : 0.06 , cube : 0.06 } p(o_{2})=\{\texttt{none}:0.22,\ \texttt{sin}:0.14,\ \texttt{cos}:0.14,\ \texttt{sqrt}:0.12,\ \texttt{log}:0.10,\ \texttt{square}:0.09,\ \texttt{tan}:0.07,\ \texttt{exp}:0.06,\ \texttt{cube}:0.06\} . Similarly, binary operators o 3 o_{3} are sampled from:

[132] table: 𝒪 binary = { add , sub , mul , div } , \mathcal{O}_{\text{binary}}=\{\texttt{add},\texttt{sub},\texttt{mul},\texttt{div}\},

[133] p: with fixed categorical priors: p ( o 3 ) = { add : 0.35 , mul : 0.30 , sub : 0.20 , div : 0.15 } p(o_{3})=\{\texttt{add}:0.35,\ \texttt{mul}:0.30,\ \texttt{sub}:0.20,\ \texttt{div}:0.15\} .

[134] p: Free-form LaTeX expression construction. The expression string e latex e_{\texttt{latex}} is deterministically generated using a fixed grammar: unary operators are rendered as standard LaTeX commands (e.g., log ↦ \ log ( ⋅ ) \texttt{log}\mapsto\backslash\texttt{log}(\cdot) , sqrt ↦ \ sqrt { ⋅ } \texttt{sqrt}\mapsto\backslash\texttt{sqrt}\{\cdot\} , square ↦ ( ⋅ ) 2 \texttt{square}\mapsto(\cdot)^{2} ), while binary operators are rendered as + + , − - , \ times \backslash\texttt{times} , or \ frac ​ { ⋅ } ​ { ⋅ } \backslash\texttt{frac}\{\cdot\}\{\cdot\} .

[135] h4: A.1.2 ProfileBio

[136] p: ProfileBio is a synthetic benchmark for evaluating joint generation of mixed-type profiles with a free-form biography field grounded in structured attributes. Each record contains two numerical attributes , five categorical attributes , and one free-form text attributes

[137] table: ( age , salary , sex , birth_state , college , degree , occupation , biography ) , ({\color[rgb]{0.15,0.35,0.75}\texttt{age}},\ {\color[rgb]{0.15,0.35,0.75}\texttt{salary}},\ {\color[rgb]{0.1,0.55,0.25}\texttt{sex}},\ {\color[rgb]{0.1,0.55,0.25}\texttt{birth\_state}},\ {\color[rgb]{0.1,0.55,0.25}\texttt{college}},\ {\color[rgb]{0.1,0.55,0.25}\texttt{degree}},\ {\color[rgb]{0.1,0.55,0.25}\texttt{occupation}},\ {\color[rgb]{0.55,0.2,0.55}\texttt{biography}}),

[138] p: where biography is a natural-language paragraph describing the structured attributes. Following the setup of MathExpr, we generate 5,000 5{,}000 samples and split them into a real reference set and a validation set with a 9:1 ratio. During sampling, each model generates a synthetic dataset with the same size as the real reference set, and we evaluate the distribution fidelity and biography consistency using the metrics described in Appendix A.2.3 .

[139] p: Categorical attributes sampling. For categorical attributes, Sex is generated uniformly from { male , female }. For others, the categorical priors is:

[140] table: p ( birth_state ) = { California : 0.15 , New York : 0.12 , Texas : 0.12 , Florida : 0.10 , Illinois : 0.08 , \displaystyle p(\texttt{birth\_state})=\{\texttt{California}:0.15,\ \texttt{New York}:0.12,\ \texttt{Texas}:0.12,\ \texttt{Florida}:0.10,\ \texttt{Illinois}:0.08, Washington : 0.08 , Massachusetts : 0.07 , Colorado : 0.07 , Georgia : 0.11 , Arizona : 0.10 } \displaystyle\texttt{Washington}:0.08,\ \texttt{Massachusetts}:0.07,\ \texttt{Colorado}:0.07,\ \texttt{Georgia}:0.11,\ \texttt{Arizona}:0.10\}

[141] table: p ( college ) = { Stanford University : 0.05 , Harvard University : 0.05 , \displaystyle p(\texttt{college})=\{\texttt{Stanford University}:0.05,\ \texttt{Harvard University}:0.05, University of California, Berkeley : 0.05 , University of Michigan : 0.07 , \displaystyle\texttt{University of California, Berkeley}:0.05,\ \texttt{University of Michigan}:0.07, Arizona State University : 0.20 , University of Central Florida : 0.15 , \displaystyle\texttt{Arizona State University}:0.20,\ \texttt{University of Central Florida}:0.15, Santa Monica College : 0.15 , Houston Community College : 0.15 , Ohio State University : 0.13 } ) \displaystyle\texttt{Santa Monica College}:0.15,\ \texttt{Houston Community College}:0.15,\ \texttt{Ohio State University}:0.13\})

[142] p: For degree , we introduce a mixed distribution. If the college in { Stanford University , Harvard University , University of California, Berkeley } \{\texttt{Stanford University},\texttt{Harvard University},\\ \texttt{University of California, Berkeley}\} , the prior is defined as p ( degree ) = { Associate : 0.01 , Bachelor : 0.29 , Master : 0.4 , Doctoral : 0.3 } ) p(\texttt{degree})=\{\texttt{Associate}:0.01,\ \texttt{Bachelor}:0.29,\ \texttt{Master}:0.4,\ \texttt{Doctoral}:0.3\}) , otherwise, the prior is defined as p ( degree ) = { Associate : 0.3 , Bachelor : 0.5 , Master : 0.15 , Doctoral : 0.05 } ) p(\texttt{degree})=\{\texttt{Associate}:0.3,\ \texttt{Bachelor}:0.5,\ \texttt{Master}:0.15,\ \texttt{Doctoral}:0.05\})

[143] p: For Occupation , we sample from Software Developer , Research Specialist , Healthcare Practitioner , Business Operations Analyst , Education Professional , Creative Content Professional , Technical Services Specialist , Construction Professional , Customer Services Professional , Public Services Coordinator . For each occupation, we give an initial weight of 1. If the degree is Bachelor or Master , we directly normalized it into a uniform distribution. If the degree degree is Doctoral , we give Research Specialist of weight 6 and Education Professional of weight 4. If the degree degree is Associate , we instead give Customer Services Professional of weight 5 and Construction Professional of weight 5. Then we normalized it into a prior distribution.

[144] p: Numerical attributes sampling. We sample Age uniformly from integers in [ 21 , 65 ] [21,65] . Finally, for Salary , we set the base salary to 85 85 . If Degree is Master or Doctoral , we add base salary with 30 30 and 50 50 , respectively. If Occupation is Software Developer or Healthcare Practitioner , we add base salary with 25 25 . Next, an age bonus is added by ( Age − 21 ) ∗ 1.2 (\texttt{Age}-21)*1.2 . Finally, the noise is added by a normal distribution with a mean of 0 0 and a variance of 15 15 . The final Salary is rounded to the closest integer with minimum of 75 75 and maximum of 200 200 .

[145] p: Biography construction. The biography column is deterministically constructed from the numerical and categorical attributes using a fixed template, where age and salary are first mapped to coarse-grained textual descriptions. Table 8 summarizes the mapping rules and the full biography template.

[146] p: Additional clarification. ProfileBio is a fully synthetic dataset constructed via predefined rules and deterministic templates, without relying on or imitating any real individuals. There is no real biography included. Sensitive personal attributes such as race, religion, health status, or immigration background are intentionally excluded. While attributes such as sex, birth state, and occupation are included to enable evaluation of cross-field consistency, the salary generation process is explicitly designed to depend only on age, degree, and occupation, and does not condition on sex or birth state, in order to avoid encoding demographic-based disparities. We emphasize that ProfileBio is intended solely as a controlled benchmark for evaluating joint generation fidelity and attribute–text consistency, rather than as a model of real-world socioeconomic distributions.

[147] figure: Table 8: ProfileBio: Age/salary mapping rules and the biography template. Component Rule / Template Age descriptor [21, 25]: in the early stage of adulthood [26, 30]: in an early phase of career development [31, 40]: in a career-building stage [41, 50]: at an established professional stage [51, 60]: in an advanced career stage [60, + ∞ +\infty ]: at the late career stage Salary descriptor [ − ∞ -\infty , 110]: a comfortable, stable income [111, 150]: a strong professional income [151, + ∞ +\infty ]: a high-level executive income Biography template This {sex} individual is {age_desc}. {He/She} was born in {birth_state} and completed higher education at {college}, earning a {degree} degree. {He/She} works as a {occupation}. {He/She} earns {salary_desc}.

[148] h4: A.1.3 Amazon

[149] p: Amazon is a real-world free-text tabular benchmark constructed from the RelBench ( Robinson et al., 2024 ) rel-amazon relational benchmark, which contains linked product metadata and user reviews. We join the review and product tables on product_id and form a single mixed-type table with two numerical attributes , two categorical attributes , and six free-form text attributes :

[150] table: ( \displaystyle( price , review_time , rating , verified , category , \displaystyle\color[rgb]{0.15,0.35,0.75}{\displaystyle\texttt{price}},\ {\color[rgb]{0.15,0.35,0.75}\texttt{review\_time}},\ {\color[rgb]{0.1,0.55,0.25}\texttt{rating}},\ {\color[rgb]{0.1,0.55,0.25}\texttt{verified}},\ {\color[rgb]{0.55,0.2,0.55}\texttt{category}},\ OPEN brand , title , description , review_text , summary ) . \displaystyle\color[rgb]{0.55,0.2,0.55}{\displaystyle\texttt{brand}},\ {\color[rgb]{0.55,0.2,0.55}\texttt{title}},\ {\color[rgb]{0.55,0.2,0.55}\texttt{description}},\ {\color[rgb]{0.55,0.2,0.55}\texttt{review\_text}},\ {\color[rgb]{0.55,0.2,0.55}\texttt{summary}}).

[151] p: We sample 5,000 5{,}000 examples in total and split them into a train/real set and a validation set with a 9:1 ratio. In addition, we sample another test set of 2,250 2{,}250 examples for downstream utility evaluation. During sampling, each model generates a synthetic dataset with the same size as the real set (i.e., 4,500 4{,}500 synthetic samples), and we report distribution fidelity and utility metrics as defined in Appendix A.2.3 . Table 9 shows an example record.

[152] figure: Table 9: An example sample from the Amazon dataset. Column Example Value price 5.98 5.98 review_time 1970 1970 (days since earliest review date) rating 5.0 5.0 verified true category Science Fiction & Fantasy > Fantasy brand Visit Amazon’s J. R. R. Tolkien Page title Hobbit description The enchanting prelude to "The Lord of the Rings" review_text My 13 yr. old grandson was very happy with this book. He likes to know the background of things and this helped him to understand this story. summary Grandson happy

[153] h4: A.1.4 Real-world Tabular Datasets

[154] p: We evaluate on five widely-used real-world tabular datasets from the UCI Machine Learning Repository. 1 1 1 https://archive.ics.uci.edu/datasets These datasets cover both classification and regression tasks, providing a diverse testbed for regular tabular generation with only numerical and categorical features. Specifically, Adult, Default, Shoppers, and Magic are used for classification, while Beijing is used for regression. Dataset statistics and the corresponding train/validation/test splits are summarized in Table 10 .

[155] figure: Table 10: Statistics of real-world tabular datasets. # Num denotes the number of numerical columns, and # Cat denotes the number of categorical columns. # Max Cat is the maximum number of categories among all categorical columns. Dataset # Rows # Num # Cat # Max Cat # Train # Validation # Test Task Adult 48,842 6 9 42 28,943 3,618 16,281 Classification Default 30,000 14 11 11 24,000 3,000 3,000 Classification Shoppers 12,330 10 8 20 9,864 1,233 1,233 Classification Magic 19,019 10 1 2 15,215 1,902 1,902 Classification Beijing 43,824 7 5 31 35,058 4,383 4,383 Regression

[156] h3: A.2 Metrics

[157] h4: A.2.1 Shape and Trend

[158] p: We evaluate distribution fidelity on all datasets using two general-purpose metrics: Shape and Trend . Shape and Trend are adopted from SDMetrics 2 2 2 https://docs.sdv.dev/sdmetrics , which quantify the marginal column-wise similarity and the pairwise dependency preservation between real and synthetic data, respectively.

[159] p: Shape. Kolmogorov-Smirnov Test (KST): This metric quantifies the alignment between the real distribution p r ​ ( x ) p_{r}(x) and the synthetic distribution p s ​ ( x ) p_{s}(x) by calculating the maximum divergence between their respective Cumulative Distribution Functions (CDFs):

[160] table: KST = sup x | F r ​ ( x ) − F s ​ ( x ) | , \text{KST}=\sup_{x}|F_{r}(x)-F_{s}(x)|, (17)

[161] p: where F r ​ ( x ) F_{r}(x) and F s ​ ( x ) F_{s}(x) denote the CDFs derived from the probability densities:

[162] table: F ⁡ ( x ) = ∫ − ∞ x p ⁡ ( t ) ​ 𝑑 t . F(x)=\int_{-\infty}^{x}p(t)\mathrm{d}t. (18)

[163] p: Total Variation Distance (TVD): For categorical variables, we evaluate the discrepancy in probability mass using the TVD. It is defined as half the sum of the absolute differences between the category frequencies observed in the real data, R ⁡ ( ω ) R(\omega) , and the synthetic data, S ⁡ ( ω ) S(\omega) :

[164] table: TVD = 1 2 ​ ∑ ω ∈ Ω | R ⁡ ( ω ) − S ⁡ ( ω ) | , \text{TVD}=\frac{1}{2}\sum_{\omega\in\Omega}|R(\omega)-S(\omega)|, (19)

[165] p: where Ω \Omega represents the set of all possible categories within a given column.

[166] p: Trend. Pearson Correlation Score: We examine the preservation of linear dependencies between continuous columns using the Pearson correlation coefficient, ρ x , y \rho_{x,y} , defined as:

[167] table: ρ x , y = Cov ​ ( x , y ) σ x ​ σ y , \rho_{x,y}=\frac{\text{Cov}(x,y)}{\sigma_{x}\sigma_{y}}, (20)

[168] p: where Cov represents covariance and σ \sigma denotes the standard deviation. To evaluate the overall preservation of these trends, we compute the Pearson Score as the normalized average absolute error between the correlation matrices of the real ( ρ R \rho^{R} ) and synthetic ( ρ S \rho^{S} ) datasets:

[169] table: Pearson Score = 1 2 ​ 𝔼 x , y ​ | ρ R ​ ( x , y ) − ρ S ​ ( x , y ) | . \text{Pearson Score}=\frac{1}{2}\mathbb{E}_{x,y}|\rho^{R}(x,y)-\rho^{S}(x,y)|. (21)

[170] p: Since ρ ∈ [ − 1 , 1 ] \rho\in[-1,1] , the factor of 1 / 2 1/2 normalizes the score to the range [ 0 , 1 ] [0,1] , where a lower score indicates superior correlation preservation.

[171] p: Contingency Similarity: To measure the consistency of pairwise associations between categorical columns A A and B B , we utilize a metric based on the Total Variation Distance applied to contingency tables. The Contingency Score is calculated as:

[172] table: Contingency Score = 1 2 ​ ∑ α ∈ A ∑ β ∈ B | R α , β − S α , β | , \text{Contingency Score}=\frac{1}{2}\sum_{\alpha\in A}\sum_{\beta\in B}|R_{\alpha,\beta}-S_{\alpha,\beta}|, (22)

[173] p: where R α , β R_{\alpha,\beta} and S α , β S_{\alpha,\beta} correspond to the joint frequencies of category pair ( α , β ) (\alpha,\beta) in the real and synthetic datasets, respectively.

[174] h4: A.2.2 Machine Learning Efficiency

[175] p: For datasets with an associated downstream prediction task, we additionally report Machine Learning Efficiency (MLE) to assess utility via the test-performance gap between models trained on real versus synthetic samples. In particular, we apply MLE to the regular real-world tabular datasets. During evaluation, we train the XGBoost classifier on the real training set (further split with an 8:1 ratio for validation and hyperparameter tuning) and evaluate it on a held-out real test set. We then train an identical classifier on the synthetic dataset and evaluate it on the same real test set. The MLE score is defined by the divergence between the two test performances, reflecting how well synthetic data can serve as a substitute for real data in downstream predictive modeling.

[176] h4: A.2.3 Dataset-specific Metrics

[177] p: MathExpr. Beyond standard distribution metrics (Shape and Trend), we evaluate whether the generated free-form LaTeX expression is structurally and numerically consistent with the structured number and operation columns. We report: (1) Operation Match Rate (Op-MR), which verifies if the unary/binary operator tokens implied by the expression e latex e_{\texttt{latex}} strictly align with the structured operations ( o 1 , o 2 , o 3 ) (o_{1},o_{2},o_{3}) ; and (2) Expression match rate (Exp-MR), which evaluates the joint validity of structure and values. Specifically, a generated expression is considered a match only if it (i) satisfies operation correctness (as in Op-MR) and (ii) contains two numeric literals whose values align with the structured fields ( x 1 , x 2 ) (x_{1},x_{2}) up to a small relative tolerance. Concretely, letting x ^ 1 , x ^ 2 \hat{x}_{1},\hat{x}_{2} be the literals extracted from the generated LaTeX string, we require | x ^ i − x i | / x i ≤ δ \lvert\hat{x}_{i}-x_{i}\rvert/x_{i}\leq\delta for i ∈ { 1 , 2 } i\in\{1,2\} . We fix δ = 0.07 \delta=0.07 to make the metric robust to minor numeric drift that can arise from stochastic generation and continuous-value approximation (e.g., 0.29 0.29 vs. 0.30 0.30 ), while still penalizing outputs whose numeric content is meaningfully inconsistent with the structured inputs. We additionally report a sensitivity analysis over δ \delta in the appendix and observe that the relative ranking of methods is stable.

[178] p: ProfileBio. For ProfileBio, we assess cross-modality consistency between structured attributes and the generated biography text. We compute a rule-based Match Rate by checking whether the biography instantiates the required template slots with values consistent with the corresponding structured fields (see the example template in Table 8 ). Concretely, for each record we verify that the text reflects core attributes (e.g., sex , birth_state , college , degree , occupation ) as well as the derived descriptors for continuous variables (Age and Salary). Since mapping continuous values into discrete natural-language descriptors introduces semantic fuzziness near bin boundaries, we apply a small boundary relaxation tolerance δ = 0.05 \delta=0.05 when validating the age/salary descriptors. This avoids rigid thresholding artifacts where values close to a boundary may legitimately share descriptions from neighboring categories; for instance, age 30.5 30.5 can reasonably be described as either “in an early phase of career development” or “in a career-building stage.”

[179] p: Amazon. For the Amazon dataset, we measure downstream utility via an MLE-like protocol, with rating as the target label in { 1 , 2 , 3 , 4 , 5 } \{1,2,3,4,5\} (treated as a multi-class classification task). We first serialize all non-numerical fields into structured text and encode them using the sentence embedding model Nomic. We then train an XGBoost classifier using either (i) text embeddings only or (ii) text embeddings concatenated with numerical features, which helps isolate the contribution of generated text/categorical fields. We report Macro-AUC on the held-out test set as the utility metric.

[180] h2: Appendix B Implementation Details

[181] p: We implement TabDLM based on PyTorch ( Paszke et al., 2019 ) . All experiments are run on an NVIDIA A100 GPU with 80GB of memory.

[182] p: Data preprocessing. We follow the same preprocessing method as prior diffusion-based tabular synthetic model ( Shi et al., 2025 ) . Missing numerical values are imputed with the column mean, and missing categorical values are treated as an additional category. To stabilize optimization across heterogeneous numerical scales, we apply a quantile-based transformation to numerical columns during training and invert the transform after sampling to recover values in the original space.

[183] p: Data splits. We adopt the same data split protocol as the TabDiff setting: each dataset is partitioned into a real set and a test set. Models are trained on the real set. For downstream utility evaluation, we further split the real set into training and validation subsets and reserve the test set strictly for evaluation.

[184] p: Architecture. We build TabDLM on top of the LLaDA-8B base model for all experiments. To incorporate numerical channels, each scalar value is first mapped into a d d -dimensional latent using a lightweight pretrained float encoder, implemented as a 3-layer MLP with hidden width ⌊ d ⌋ \lfloor\sqrt{d}\rfloor and SiLU activations ( Hendrycks, 2016 ) . A float decoder (LayerNorm + linear projection) maps the latent back to a scalar. We set the numerical latent dimension to d = 512 d=512 by default and keep the pretrained float encoder/decoder frozen during joint training. To interface numerical latents with the MDLM embedding space, we further apply a two-stage projection: an input projector that maps per-feature latents from d d to the MDLM hidden size D D using a 2-layer MLP ( d → → D d\!\rightarrow\!1024\!\rightarrow\!D ) with SiLU and dropout (with LayerNorm), and an output projector that maps MDLM hidden states back to the numerical latent space via a symmetric 2-layer MLP ( D → → d D\!\rightarrow\!1024\!\rightarrow\!d ). The dimension D D in LLaDA-8B is 4096.

[185] p: Hyperparameters setting. We fine-tune models with LoRA using the same configuration for TabDLM , LLaDA-8B SFT {}_{\text{SFT}} , and Qwen2.5-7B SFT {}_{\text{SFT}} to ensure fair comparison. Unless otherwise stated, we use LoRA rank r = 16 r=16 , scaling factor α = 32 \alpha=32 , and dropout 0.05 0.05 , and apply it to attention and MLP components of Transformer blocks. Across methods, we keep the optimizer and training recipe identical; the only dataset-dependent choice is the number of training epochs due to varying dataset sizes. Specifically, we train for 10 epochs on Adult and Beijing, 30 epochs on Shoppers, 15 epochs on Magic and Default, 75 epochs on MathExpr and Amazon, 150 epochs on ProfileBio, and 75 epochs on MathExpr with the Adam optimizer. We use AdamW with learning rate 2 × 10 − 4 2\times 10^{-4} , warmup ratio 0.1 0.1 , ( β 1 , β 2 ) = ( 0.9 , 0.98 ) (\beta_{1},\beta_{2})=(0.9,0.98) , weight decay 10 − 4 10^{-4} , and ϵ = 10 − 8 \epsilon=10^{-8} . All experiments use the same fixed random seed and bf16 training when enabled.

[186] p: Noise schedule. For the continuous numerical diffusion, we adopt the power-mean noise schedule introduced in TabDiff, which parameterizes the total noise level as a smooth interpolation between σ min \sigma_{\min} and σ max \sigma_{\max} over normalized time t ∈ [ 0 , 1 ] t\in[0,1] . Specifically, we set σ min = 0.002 \sigma_{\min}=0.002 and σ max = 80.0 \sigma_{\max}=80.0 in our experiments. Importantly, we use a per-feature variant where each numerical column i i has its own learnable shape parameter ρ i \rho_{i} , allowing different features to follow different noise growth profiles. Formally, for each numerical feature i ∈ { 1 , … , M num } i\in\{1,\ldots,M_{\text{num}}\} , we define:

[187] table: σ ρ i num ​ ( t ) = ( σ min 1 / ρ i + t ⁡ ( σ max 1 / ρ i − σ min 1 / ρ i ) ) ρ i . \sigma^{\text{num}}_{\rho_{i}}(t)=\left(\sigma_{\min}^{1/\rho_{i}}+t\left(\sigma_{\max}^{1/\rho_{i}}-\sigma_{\min}^{1/\rho_{i}}\right)\right)^{\rho_{i}}. (23)

[188] p: This schedule generalizes the standard EDM power-mean parameterization and provides a flexible, monotonic mapping from t t to noise magnitude. Learning ρ i \rho_{i} per column helps accommodate heterogeneous numerical distributions and scales, yielding a better-conditioned diffusion process than using a single global shape parameter for all numerical features.

[189] p: Sampling Details. We perform joint sampling over discrete tokens (categorical/text) and continuous numerical features via a coupled reverse process over T T discretized reverse-time steps.

[190] p: Initialization. Given a schema prompt prefix 𝐩 \mathbf{p} and a target generation length G G , we initialize the token sequence as 𝐱 T = [ 𝐩 ; [MASK] G ] \mathbf{x}_{T}=[\mathbf{p};\texttt{[MASK]}^{G}] . For numerical channels, we draw the initial state from a Gaussian prior, 𝐱 T num ∼ 𝒩 ⁡ ( 𝟎 , σ max 2 ​ 𝐈 ) \mathbf{x}^{\text{num}}_{T}\sim\mathcal{N}(\mathbf{0},\sigma_{\max}^{2}\mathbf{I}) . We discretize reverse time from 1 1 to 0 0 into T T steps, yielding a noise schedule { σ t } t = 0 T \{\sigma_{t}\}_{t=0}^{T} and a churned schedule { σ ^ t } t = 0 T \{\hat{\sigma}_{t}\}_{t=0}^{T} .

[191] p: Joint iterative denoising. For t = T , T − 1 , … , 1 t=T,T\!-\!1,\ldots,1 , we update numericals and tokens in an interleaved manner:

[192] p: Numerical perturbation. At step t t , we optionally apply EDM-style churn by injecting extra noise:

[193] table: 𝐱 ^ t num ← 𝐱 t num + σ ^ t 2 − σ t 2 ​ ϵ , ϵ ∼ 𝒩 ⁡ ( 𝟎 , 𝐈 ) , \hat{\mathbf{x}}^{\text{num}}_{t}\leftarrow\mathbf{x}^{\text{num}}_{t}+\sqrt{\hat{\sigma}_{t}^{2}-\sigma_{t}^{2}}\,\boldsymbol{\epsilon},\quad\boldsymbol{\epsilon}\sim\mathcal{N}(\mathbf{0},\mathbf{I}),

[194] p: where σ ^ t \hat{\sigma}_{t} denotes the churned noise level. We then map 𝐱 ^ t num \hat{\mathbf{x}}^{\text{num}}_{t} to per-feature embeddings 𝐄 t num ∈ ℝ M num × D \mathbf{E}^{\text{num}}_{t}\in\mathbb{R}^{M_{\text{num}}\times D} using the number encoder module introduced in Section 2.2 , and inject them into the MDLM by replacing the designated numerical placeholder positions in the input embedding sequence.

[195] p: Token denoising and unmasking. Conditioned on the injected numerical embeddings, we run the MDLM forward pass to obtain logits over masked positions and sample token proposals using Gumbel-max (temperature τ = 1 \tau=1 in all experiments), producing a candidate 𝐱 t ( 0 ) \mathbf{x}^{(0)}_{t} . We then follow the LLaDA-style progressive unmasking strategy to update the token state from 𝐱 t \mathbf{x}_{t} to 𝐱 t − 1 \mathbf{x}_{t-1} by selecting a subset of currently masked positions to reveal at step t t . We consider two remasking policies: ( i ) high-confidence unmasking, which reveals the positions with the highest confidence (token probability), and ( ii ) random unmasking, which reveals a uniformly random subset of masked positions. In both cases, the number of revealed tokens per step is uniform across t t , ensuring a smooth transition from all-masked to fully-specified sequences.

[196] p: Numerical reverse update. We extract the MDLM last-layer hidden states at numerical placeholder positions and predict a denoised numerical state 𝐱 ~ t num \tilde{\mathbf{x}}^{\text{num}}_{t} via number decoder module introduced in Section 2.2 . We then perform an EDM-style Euler update:

[197] table: 𝐝 t ← 𝐱 ^ t num − 𝐱 ~ t num σ ^ t , 𝐱 t − 1 num ← 𝐱 ^ t num + ( σ t − 1 − σ ^ t ) ​ 𝐝 t , \mathbf{d}_{t}\leftarrow\frac{\hat{\mathbf{x}}^{\text{num}}_{t}-\tilde{\mathbf{x}}^{\text{num}}_{t}}{\hat{\sigma}_{t}},\qquad\mathbf{x}^{\text{num}}_{t-1}\leftarrow\hat{\mathbf{x}}^{\text{num}}_{t}+(\sigma_{t-1}-\hat{\sigma}_{t})\mathbf{d}_{t},

[198] p: Finalization. After t t reaches 0 0 , we decode the final token sequence and replace numerical placeholders with the generated numerical values (after denormalization) to obtain the final mixed-type sample.

[199] figure: Table 11 : Evaluation of MLE. AUC is used for classification tasks and RMSE for regression tasks. ( B : best overall; B : best in language-based model) Methods Adult Default Shoppers Magic Beijing Average Gap AUC ↑ \uparrow AUC ↑ \uparrow AUC ↑ \uparrow AUC ↑ \uparrow RMSE ↓ \downarrow % \% Real .927 ± .000 .927\pm.000 .770 ± .005 .770\pm.005 .926 ± .001 .926\pm.001 .946 ± .001 .946\pm.001 .423 ± .003 .423\pm.003 0.0 0.0 CTGAN .886 ± .002 .886\pm.002 .696 ± .005 .696\pm.005 .875 ± .009 .875\pm.009 .855 ± .006 .855\pm.006 .902 ± .019 .902\pm.019 28.48 28.48 TVAE .878 ± .004 .878\pm.004 .724 ± .005 .724\pm.005 .871 ± .006 .871\pm.006 .887 ± .003 .887\pm.003 .770 ± .011 .770\pm.011 21.09 21.09 GOGGLE .778 ± .012 .778\pm.012 .584 ± .005 .584\pm.005 .658 ± .052 .658\pm.052 .654 ± .024 .654\pm.024 1.09 ± .025 1.09\pm.025 51.54 51.54 STaSy .906 ± .001 .906\pm.001 .752 ± .006 .752\pm.006 .914 ± .005 .914\pm.005 .934 ± .003 .934\pm.003 .656 ± .014 .656\pm.014 12.45 12.45 CoDi .871 ± .006 .871\pm.006 .525 ± .006 .525\pm.006 .865 ± .006 .865\pm.006 .932 ± .003 .932\pm.003 .818 ± .021 .818\pm.021 27.86 27.86 TabDDPM .907 ± .001 .907\pm.001 .758 ± .004 .758\pm.004 .918 ± .005 .918\pm.005 .935 ± .003 .935\pm.003 .592 ± .011 .592\pm.011 9.14 9.14 TabSyn .909 ± .001 .909\pm.001 .763 ± .002 .763\pm.002 .914 ± .004 .914\pm.004 .937 ± .002 \mathbf{.937\pm.002} .580 ± .009 .580\pm.009 8.44 8.44 TabDiff .912 ± .002 .912\pm.002 .763 ± .005 .763\pm.005 .921 ± .004 .921\pm.004 .936 ± .003 .936\pm.003 .555 ± .013 .555\pm.013 7.07 \mathbf{7.07} GReaT .913 ± .003 .913\pm.003 .755 ± .006 .755\pm.006 .902 ± .005 .902\pm.005 .888 ± .008 .888\pm.008 .653 ± .013 .653\pm.013 13.31 13.31 DiffLM .906 .906 .794 .915 .915 .917 .917 .696 .696 13.59 13.59 Qwen2.5-7B ICL {}_{\text{ICL}} .853 .853 .390 .390 .811 .811 .829 .829 .991 .991 43.28 43.28 Qwen2.5-14B ICL {}_{\text{ICL}} .852 .852 .639 .639 .640 .640 .844 .844 1.03 1.03 42.05 42.05 Qwen2.5-7B SFT {}_{\text{SFT}} .915 .769 .769 .895 .895 .918 .918 .554 7.74 \mathbf{7.74} LLaDA-8B SFT {}_{\text{SFT}} .909 .909 .774 .774 .872 .872 .923 \mathbf{.923} .736 .736 16.74 16.74 TabDLM .907 .907 .791 .791 .923 .905 .905 .673 .673 12.64 12.64

[200] h2: Appendix C Additional Experimental Results

[201] h3: C.1 Evaluation results of MLE for real-world tabular dataset

[202] p: In this section, we provide the evaluation results of MLE for a real-world tabular dataset without free-form text features in Table 11 . As shown in Table 11 , our method achieves strong MLE performance on Adult, Default, Shoppers, and Magic, demonstrating its ability to faithfully capture the underlying data distribution and support high-quality synthetic data for downstream training. Notably, on Default and Shoppers, models trained on our generated data even outperform those trained on real data, suggesting that our generator can produce samples that are both distributionally consistent and beneficial for improving generalization. We observe a noticeable performance drop on Beijing, which may be caused by the large fraction of missing values in the target column, where our mean-imputation preprocessing method could distort the true target distribution and hurt likelihood-based metrics such as MLE.

[203] h2: Instructions for reporting errors

[204] p: We are continuing to improve HTML versions of papers, and your feedback helps enhance accessibility and mobile support. To report errors in the HTML that will help us improve conversion and rendering, choose any of the methods listed below:

[205] p: Tip: You can select the relevant text first, to include it in your report.

[206] p: Our team has already identified the following issues . We appreciate your time reviewing and reporting rendering errors we may not have found yet. Your efforts will help us improve the HTML versions for all readers, because disability should not be a barrier to accessing research. Thank you for your continued support in championing open access for all.

[207] p: Have a free development cycle? Help support accessibility at arXiv! Our collaborators at LaTeXML maintain a list of packages that need conversion , and welcome developer contributions .
