# DART exact v1 primary — known-item reconciliation

DART: Diffusion-Inspired Speculative Decoding for Fast LLM Inference (https://arxiv.org/html/2601.19278v1)
citeturn28615view0 [wordlim: 200] Crawled: today; Content type: text/html; Source: open({"ref_id":"https://arxiv.org/html/2601.19278v1","lineno":0}); Total lines: 616
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
L14: cite1†Why HTML?†info.arxiv.org cite2†Report Issue cite3†Back to Abstract cite4†Download PDF L15:   1. cite5†Abstract L16:   2. cite6†1 Introduction L17:   3. cite7†2 Preliminaries L18:     1. cite8†2.1 Speculative Decoding L19:     2. cite9†2.2 Diffusion-Based Large Language Models L20:   4. cite10†3 DART L21:     1. cite11†3.1 Requirements of Speculative Decoding L22:     2. cite12†3.2 Diffusion-Inspired Drafting Phase L23:       1. cite13†Draft model architecture. L24:       2. cite14†Shifted logits prediction. L25:       3. cite15†Parallel holistic prediction. L26:     3. cite16†3.3 Training of the Draft Model L27:       1. cite17†Prefix-shared masked training. L28:       2. cite18†Annealed KL divergence objective. L29:     4. cite19†3.4 What Does DART Output? L30:   5. cite20†4 Efficient N-gram-based Tree Pruning L31:     1. cite21†4.1 Implicit Huge Search Space in Parallel Logits L32:     2. cite22†4.2 Consistency-constrained Pruning via N-gram L33:   6. cite23†5 Experiments L34:     1. cite24†5.1 Experimental Setup L35:       1. cite25†Hardware. L36:       2. cite26†Target models. L37:       3. cite27†Benchmarks. L38:       4. cite28†Implementation. L39:       5. cite29†Metrics. L40:     2. cite30†5.2 Main Results L41:       1. cite31†Throughput improvement. L42:       2. cite32†Relatively high $\tau$. L43:       3. cite33†Drafting latency reduction. L44:     3. cite34†5.3 Ablation Study L45:       1. cite35†N-gram effectiveness. L46:       2. cite36†Shifted logits prediction. L47:       3. cite37†Annealing coefficient in DART training. L48:     4. cite38†5.4 Larger Batch Sizes Study L49:   7. cite39†6 Conclusion L50:   8. cite40†References L51:   9. cite41†A EAGLE3 Latency Analysis L52:   10. cite42†B Training Details L53:     1. cite43†B.1 Training Implementation L54:     2. cite44†B.2 Training Setup L55:       1. cite45†Trainable parameters L56:       2. cite46†Training data. L57:       3. cite47†Training with Flex Attention. L58:   11. cite48†C N-gram Details L59:     1. cite49†C.1 N-gram Construction L60:     2. cite50†C.2 N-gram Usage at Inference L61:   12. cite51†D Tree Pruning Algorithm Details L62:   13. cite52†E Larger Batch sizes Study Details L63:   14. cite53†F DART Performance in A100 L64:   15. cite54†G LLM Usage L65: cite55†License: arXiv.org perpetual non-exclusive license†info.arxiv.org L66: 
L67: arXiv:2601.19278v1 [cs.CL] 27 Jan 2026
L68: # cite56†Image: [Uncaptioned image] DART: Diffusion-Inspired Speculative Decoding for Fast LLM Inference
L69: Fuliang Liu Affiliation: State Key Laboratory of Novel Software Technology, Nanjing University Affiliation: Alibaba Group    Xue Li Affiliation: Alibaba Group    Ketai Zhao Affiliation: State Key Laboratory of Novel Software Technology, Nanjing University    Yinxi Gao Affiliation: State Key Laboratory of Novel Software Technology, Nanjing University    Ziyan Zhou Affiliation: State Key Laboratory of Novel Software Technology, Nanjing University    Zhonghui Zhang Affiliation: State Key Laboratory of Novel Software Technology, Nanjing University    Zhibin Wang Affiliation: State Key Laboratory of Novel Software Technology, Nanjing University Correspondence to: wzbwangzhibin@gmail.com    Wanchun Dou Affiliation: State Key Laboratory of Novel Software Technology, Nanjing University    Sheng Zhong Affiliation: State Key Laboratory of Novel Software Technology, Nanjing University    Chen Tian Affiliation: State Key Laboratory of Novel Software Technology, Nanjing University
L70: ###### Abstract
L71: Speculative decoding is an effective and lossless approach for accelerating LLM inference. However, existing widely adopted model-based draft designs, such as EAGLE3, improve accuracy at the cost of multi-step autoregressive inference, resulting in high drafting latency and ultimately rendering the drafting stage itself a performance bottleneck. Inspired by diffusion-based large language models (dLLMs), we propose DART, which leverages parallel generation to reduce drafting latency.
L72: DART predicts logits for multiple future masked positions in parallel within a single forward pass based on hidden states of the target model, thereby eliminating autoregressive rollouts in the draft model while preserving a lightweight design. Based on these parallel logit predictions, we further introduce an efficient tree pruning algorithm that constructs high-quality draft token trees with N-gram–enforced semantic continuity.
L73: DART substantially reduces draft-stage overhead while preserving high draft accuracy, leading to significantly improved end-to-end decoding speed. Experimental results demonstrate that DART achieves a $2.03\times$–$3.44\times$ wall-clock time speedup across multiple datasets, surpassing EAGLE3 by 30% on average and offering a practical speculative decoding framework. Code is released at cite57†https://github.com/fvliang/DART†github.com .
L74: ###### Keywords:
L75: 
L76: Machine Learning, ICML
L77: ## 1 Introduction
L78: Figure 1: Average Acceptance Length ($\tau$) versus drafting forward latency (ms), averaged across all benchmarks, for speculative decoding of Qwen3-14B on H20-3e GPU.
L79: Compared with EAGLE3 and SPS (standard speculative sampling; using Qwen3-1.7B as the draft model with a draft length of 5, set to yield a measurable speedup, whereas both EAGLE3 and DART use a draft length of 8), DART reduces drafting forward latency by up to $6.8\times$ and $53.3\times$, respectively, while preserving relatively high $\tau$, demonstrating a significantly improved drafting efficiency.
L80: Speculative decoding (cite58†Leviathan et al., 2023 ; cite59†Chen et al., 2023 ; cite60†Sun et al., 2023 ; cite61†Sun et al., 2024b ; cite62†Sun et al., 2024a ; cite63†Gao et al., 2025 ) has emerged as a promising approach to accelerate memory-bound LLM inference, particularly as modern state-of-the-art models scale to hundreds of billions of parameters (cite64†Guo et al., 2025 ; cite65†Liu et al., 2024 ).
L81: In speculative decoding, a lightweight draft model proposes multiple future tokens, which are then verified by the target model to ensure that the final output distribution exactly matches that of standard autoregressive decoding. Through speculative decoding, multiple tokens could be generated in every iteration to significantly improve inference efficiency. The effectiveness of speculative decoding depends critically on the design of the drafter.
L82: First, the drafter should achieve high predictive accuracy, most commonly quantified by the Average Acceptance Length ($\tau$), i.e., the average number of accepted draft tokens during verification. A higher $\tau$ directly translates to fewer target-model invocations and greater decoding speedups.
L83: Second, the draft model itself must be computationally efficient, which could be quantified as drafting latency $(ms)$, as excessive drafting overhead can significantly erode the overall benefits of speculative decoding.
L84: Figure 2: Speedup over vanilla autoregressive decoding (batch size $=1$), averaged across all datasets. For Qwen3 models, results are reported at temperature $T=0$ on Qwen3-1.7B, 4B, 8B, 14B, 32B, and additionally at $T=1$ on Qwen3-14B, 32B; only DART and EAGLE3 are compared on Qwen3, except for Qwen3-32B at $T=0$, where we also include SPS (using Qwen3-1.7B as the draft model with draft length 5). For LLaMA2-Chat-7B, we compare DART with methods including Medusa, Lookahead, SPS, and PLD.
L85: Typical speculative decoding’s drafter implementation is autoregressive. In vanilla speculative decoding (cite58†Leviathan et al., 2023 ), the drafter is typically a lower-parameter variant from the same model family as the target model. However, vanilla speculative decoding often suffers from high drafting latency, which can account for over 75% and 60% of the total inference time when using Qwen3-1.7B to accelerate Qwen3-14B and Qwen3-32B with draft length 5.
L86: In pursuit of lower draft latency, Medusa (cite66†Cai et al., 2024 ) applies lightweight decoding heads to predict multiple subsequent tokens on the top-layer features of the target model but delivers limited accuracy. EAGLE (cite67†Li et al., 2024a ; cite68†Li et al., 2024b ) improves the accuracy by customizing a dedicated single layer to predict next-feature autoregressively.
L87: Subsequent methods (cite69†Li et al., 2025b ; cite70†Zhang et al., 2025 ) such as EAGLE3 further boost accuracy through reducing inconsistency between training and decoding of draft model.
L88: However, current autoregressive drafter designs introduce limitations. While approaches such as EAGLE3 significantly lower the per-step drafting cost by using a single customized layer, the drafting process is still inherently autoregressive.
L89: This sequential dependency forces the drafter to spend nearly 20%–40% of the total inference time, thereby fundamentally limiting the achievable acceleration, causing the drafting stage, especially the drafting forward cost, to emerge as a new bottleneck in speculative decoding. At the other extreme, some speculative decoding approaches, such as Lookahead (cite71†Fu et al., 2024 ), rely solely on N-gram or retrieval-based heuristics for drafting.
L90: While such methods incur negligible drafting latency, their limited predictive accuracy typically leads to very low average acceptance length $\tau$, resulting in modest end-to-end speedups.
L91: Using diffusion-style parallel generation appears to be a promising direction for overcoming the above limitations. However, directly adopting diffusion-based large language models (dLLMs) as draft models (cite72†Christopher et al., 2025 ; cite73†Sandler et al., 2025 ; cite74†Li et al., 2025a ; cite75†Cheng et al., 2025 ) suffers from fundamental limitations.
L92: For example, DiffuSpec (cite74†Li et al., 2025a ) uses Dream7B (cite76†Ye et al., 2025 ) as the draft model to accelerate Qwen3-32B and N-gram based CPS to give a draft sequence in single forward. However, existing dLLMs like Dream7B are designed for bidirectional context modeling, where the objective is to jointly model and refine tokens across an entire sequence with full contextual access.
L93: In contrast, speculative decoding for LLM inference requires predicting a contiguous span of future tokens conditioned strictly on a given prefix, preserving the causal structure of autoregressive generation. This fundamental mismatch in modeling assumptions makes dLLMs inherently unsuitable as drop-in draft models for speculative decoding. Moreover, although dLLMs enable parallel token generation, directly using them as draft models does not translate into lower drafting latency in practice.
L94: Because dLLMs such as Dream7B are instantiated as standalone models with substantial parameter, their per-step inference cost remains significantly higher than lightweight, target-coupled drafters such as EAGLE3—often by tens of times in practice. As a result, the overall drafting latency of dLLM-based approaches is often substantially higher, despite their parallel decoding capability.
L95: More critically, directly using dLLMs introduces additional practical issues, including tokenizer incompatibility and limited availability.
L96: In this paper, we design a customized diffusion-style drafter tailored for speculative decoding and propose DART, a diffusion-inspired drafting approach.
L97: cite77†Image: Refer to caption Figure 3: Diagram of the DART inference pipeline, illustrating the three substeps of DART’s speculative decoding. $\mathbf{l},\mathbf{m},\mathbf{h}$ represent the low, middle, and high-level features of the target model, respectively. $\mathbf{e}$ denotes the embedding. Unlocked icon means learnable parameter.
L98: After feature extraction, we append $(d-1)$ Mask tokens to the prefix and conduct single forward to get $d$ logits, where the first logit comes from the output of the last position in prefix. We call this “Shifted logits prediction” in Section cite12†3.2 . During “Continuity-Aware Tree Pruning”, candidate tokens are selected from the corresponding position’s predicted logit and a N-gram model ensures that the expanded tokens maintain continuity.
L99: After getting the final pruned draft token tree, we verify them in target model with Tree Attention.
L100: DART is designed according to the following two principles. First, diffusion-style parallel drafting is only beneficial when explicitly customized for speculative decoding. Rather than naively adopting conventional dLLMs with bidirectional context modeling, the draft model should be tailored to predict the next few positions conditioned on a given prefix, aligning with the causal requirements of speculative decoding while retaining parallel generation.
L101: In this paper, DART adopts an efficient customized training recipe that enables the draft model to learn the distribution of multiple future positions conditioned on the given prefix. Second, effective drafting should preserve the low-cost design.
L102: To keep the drafting overhead negligible, DART is tightly coupled with the target model: it reuses the target model’s hidden states as input and applies only a single lightweight layer to directly produce logits for multiple future positions, instead of adopting a drop-in dLLM with prohibitive inference latency.
L103: However, these predicted logits implicitly induce an exponentially large combinatorial space of possible token continuations, DART further employs an efficient tree pruning algorithm to construct the final draft token tree for verification, achieving low latency while maintaining high-quality candidates with N-gram.
L104: In summary, we propose DART, a diffusion-inspired speculative decoding framework that rethinks the design of draft models under the constraints of drafting latency. Our main contributions are summarized as follows:
L105: 
L106:   * •
L107: Lightweight diffusion-style parallel drafting. We are the first to introduce a draft model that operates directly on the target model’s hidden states and predicts multiple future logits in parallel using a single customized layer. This design completely eliminates autoregressive rollout in the drafter and removes the need for complex KV cache management of autoregressive draft model.
L108: As shown in Figure cite78†1 , DART achieves up to 6.8$\times$ faster drafting forward than autoregressive drafters such as EAGLE3, while remaining relatively high average acceptance length $\tau$.
L109:   * •
L110: Continuity-aware tree pruning via N-gram. We identify that parallel logits prediction induces an exponentially large combinatorial search space, which cannot be efficiently handled by naive decoding. Instead of using N-gram models as standalone draft predictors, which suffer from low acceptance rates, we redesign N-gram as a continuity-aware pruning mechanism to efficiently constrain the draft token tree constructed from parallel logits.
L111: This continuity-aware pruning preserves high-quality candidates and substantially improves the average acceptance length $\tau$.
L112:   * •
L113: Significant end-to-end acceleration. As shown in Figure cite79†2 , extensive experiments across multiple benchmarks demonstrate that DART achieves substantial end-to-end throughput improvements, with up to 2.03–3.44$\times$ speedup over standard autoregressive decoding. Compared to prior speculative decoding methods such as EAGLE3, DART delivers around 30% higher speedup on average, while further achieving up to 65% improvement on certain code-centric workloads under the same target model setting.
L114: These results validate a new speculative decoding paradigm that combines low drafting latency and high average acceptance length.
L115: ## 2 Preliminaries
L116: ### 2.1 Speculative Decoding
L117: Let $q_{\theta}$ denote the target autoregressive language model and $p_{\phi}$ a lightweight draft model. Standard autoregressive decoding generates one token per forward pass of $q_{\theta}$, which incurs high inference latency. Speculative decoding accelerates generation by allowing the draft model to first propose a block of $K$ future tokens conditioned on the current prefix.
L118: The target model then verifies these draft tokens in parallel and accepts a contiguous prefix of them using a rejection-based procedure, guaranteeing that the final output distribution exactly matches $q_{\theta}$. The effectiveness of speculative decoding is commonly measured by the expected number of accepted draft tokens $\tau$, which determines the amortized reduction in target-model invocations. Practical draft models therefore aim to maximize $\tau$ while keeping the drafting overhead minimal.
L119: ### 2.2 Diffusion-Based Large Language Models
L120: Diffusion-based large language models (dLLMs) (cite80†Nie et al., 2025 ; cite76†Ye et al., 2025 ; cite81†Khanna et al., 2025 ) generate text by iteratively denoising partially masked sequences, predicting multiple token positions in parallel conditioned on the surrounding context. This masked, non-autoregressive formulation enables holistic sequence modeling and significantly reduces generation steps compared to autoregressive decoding.
L121: The strong parallel prediction capability of dLLMs motivates our design in DART, where we seek to eliminate autoregressive rollout in the drafting stage of speculative decoding. However, standard dLLMs are inherently bidirectional and operate on full sequences, which is incompatible with the strictly prefix-conditioned requirement and exactness guarantees of speculative decoding.
L122: DART therefore adopts a diffusion-inspired masked prediction mechanism that is explicitly tailored to speculative decoding, rather than performing full-sequence denoising.
L123: ## 3 DART
L124: 
L125: In this section, we will go through the details of DART.
L126: ### 3.1 Requirements of Speculative Decoding
L127: 
L128: The draft model in speculative decoding for autoregressive LLMs is subject to several unique requirements, which fundamentally distinguish DART from standard diffusion-based text generation:
L129: 
L130:   * •
L131: Causal attention mask. Since all prefix tokens are fully accessible and all future positions are predicted in a single forward pass, bidirectional attention for iterative token refinement is unnecessary. DART therefore retains a strictly causal attention mask, both over the prefix and within the masked block.
L132: 
L133:   * •
L134: Limited drafting horizon. Due to the inevitable distribution mismatch between the lightweight draft model and the target model, speculative decoding typically benefits from predicting only a small number of future tokens (e.g., 8). Since DART is designed to generate only a limited number of draft tokens, it can achieve relatively high accuracy even without iterative bidirectional attention refinement.
L135: 
L136:   * •
L137: Positional importance bias. Earlier draft positions are substantially more important than later ones, as token acceptance proceeds sequentially from the prefix–an error in an early token immediately terminates the verification process.
L138: 
L139: These characteristics impose stringent constraints on the design of efficient diffusion-style draft models and motivate specialized architectures that prioritize early-token accuracy, controlled horizon prediction, and strict causal conditioning.
L140: ### 3.2 Diffusion-Inspired Drafting Phase
L141: #### Draft model architecture.
L142: DART follows the lightweight design principle established by prior speculative decoding methods such as EAGLE3 (cite69†Li et al., 2025b ). The draft model consists of a single customized Transformer decoder layer that operates on intermediate representations of the target model. Concretely, after a prefilling or verification forward pass of the target model, we extract hidden states from multiple intermediate layers (denoted as $\mathbf{h},\mathbf{m},\mathbf{l}$ in Figure cite82†3 ).
L143: These hidden states are concatenated and projected through a fully connected layer to obtain a compact prefix representation $\mathbf{g}_{1:n}\in\mathbb{R}^{n\times k}$. In addition, we incorporate shifted token embeddings $\mathbf{e}_{2:n+1}$, obtained by sampling the next token $\mathbf{t}_{n+1}$ from the output of target model and applying the embedding layer of the target model.
L144: The final prefix input to the draft model is formed by concatenating $\mathbf{g}_{1:n}$ and $\mathbf{e}_{2:n+1}$ along the feature dimension, which is denoted as $\mathbf{z}_{1:n}$ . To enable parallel prediction of future tokens, DART appends a fixed-length suffix of $d-1$ $\langle\textsc{mask}\rangle$ tokens to the prefix, yielding the following input sequence:
L145:  | $$[\;\mathbf{z}_{1:n},\ \langle\textsc{mask}\rangle_{n+1:n+d-1}\;].$$  |
L146: 
L147: A single forward pass of the draft model yields logits for all future positions simultaneously:
L148: 
L149:  | $$\{\boldsymbol{\ell}_{n+1},\boldsymbol{\ell}_{n+2},\dots,\boldsymbol{\ell}_{n+d}\},$$  |
L150: 
L151: where $\boldsymbol{\ell}_{n+1}$ is read from the output at the last prefix position, and subsequent logits are read from masked positions.
L152: #### Shifted logits prediction.
L153: In dLLMs, logits predicted at masked positions are typically interpreted as predictions for the tokens at the same positions. In contrast, DART adopts a shifted logits prediction scheme, where the logit produced at each position corresponds to the prediction of the next token. Empirically, we find that this shifted formulation significantly improves the prediction accuracy at the first drafted position.
L154: Moreover, it enables more efficient training by allowing all positions to contribute supervision signals.
L155: Figure 4: Position IDs and attention mask during prefix-share training. The attention mask combines clean data causal attention (Prompt Causal), prefix attention for every mask block (Mask Preceding), and block-inner causal attention (Mask Causal). For clarity of presentation, the figure depicts a simplified example with a prefix length of 3 and mask block length of 2, rather than mask block length of 7 in the actual DART training.
L156: #### Parallel holistic prediction.
L157: DART is inspired by dLLMs, which predict multiple masked positions in parallel. However, DART does not perform iterative denoising or bidirectional refinement. Instead, it directly predicts the conditional token distributions of multiple future positions in a single step, strictly conditioned on the given prefix. Through holistic prediction, sequential latency is eliminated: the drafting cost is independent of the draft length $d$, requiring only a single forward pass of the lightweight draft model.
L158: ### 3.3 Training of the Draft Model
L159: #### Prefix-shared masked training.
L160: To closely match the inference-time drafting behavior, the draft model is trained using a prefix-shared, multi-token prediction objective. Given a training sequence $x_{1:L}$, we simultaneously construct multiple training instances at different prefix positions within the same sequence.
L161: For each prefix position $n$, the model is trained to predict the next $d$ tokens $\{x_{n+1},\dots,x_{n+d}\}$ under a shifted prediction scheme, where supervision is applied to both the prefix and masked positions, and all predictions are conditioned only on the prefix $x_{1:n}$.
L162: All such prefix positions are trained jointly within a single forward pass by employing a carefully designed sparse attention mask. Specifically, as illustrated in Figure cite83†4 , masked positions corresponding to different prefixes are allowed to attend exclusively to their respective prefixes. Attention among masked positions within the same block is causal to fit the attention mask during inference, while attention across different blocks is explicitly disabled.
L163: This prefix-isolated attention structure ensures that each masked position learns to model $p_{\phi}(\cdot\mid x_{1:n})$, without access to future ground-truth tokens. This design enables efficient supervision of multiple future positions across the sequence in parallel, substantially increasing training efficiency while strictly preserving causal conditioning. In practice, the resulting attention pattern is highly sparse.
L164: We further leverage Flex-Attention (cite84†Dong et al., 2024 ) to exploit this sparsity, significantly reducing memory consumption and accelerating training without altering the underlying model computation. We give the pseudo Flex-Attention code of DART’s sparse attention mask in Appendix cite42†B .
L165: #### Annealed KL divergence objective.
L166: 
L167: Instead of supervising the draft model with discrete one-hot targets, DART optimizes a position-aware KL divergence objective between the draft model predictions and the target model distributions. For each future position $t\in\{1,\dots,d\}$, we minimize
L168: 
L169:  | $$\mathcal{L}_{\text{KL}}=\sum_{t=1}^{d}\lambda_{t}\,\mathrm{KL}\!\left(q_{\theta}(\cdot\mid x_{1:n+t-1})\;\|\;p_{\phi}(\cdot\mid x_{1:n},t)\right),$$  |
L170: where $\lambda_{t}=\gamma^{\,t-1},$ $p_{\phi}(\cdot\mid x_{1:n},t)$ denotes the draft model’s predicted distribution for the $t$-th future position. This exponentially decaying weighting reflects the increasing uncertainty of longer-horizon predictions and prevents later, noisier targets from dominating the training signal. In practice, we set $\gamma=0.6$, which consistently yields the best trade-off between early-position accuracy and overall training stability in our ablation studies (Section cite34†5.3 ).
L171: By emphasizing short-horizon predictions while softly regularizing distant ones, this annealed objective substantially improves draft quality at the most critical positions and thereby provides higher-quality candidate distributions for downstream draft tree construction.
L172: ### 3.4 What Does DART Output?
L173: 
L174: Rather than directly producing a draft token tree, DART outputs a set of parallel logits $\{\boldsymbol{\ell}_{n+1},\dots,\boldsymbol{\ell}_{n+d}\}$, one for each future position. Each logit encodes a high-quality candidate set for that position conditioning on the prefix. Together, these logits define a compact but expressive candidate set that implicitly contains many plausible future continuations.
L175: 
L176: ## 4 Efficient N-gram-based Tree Pruning
L177: ### 4.1 Implicit Huge Search Space in Parallel Logits
L178: The $d$ parallel logits predicted by DART define a factorized distribution over future positions, which implicitly induce an exponentially large combinatorial space of possible token continuations, corresponding to a full $d$-level token tree. Directly verifying this space is infeasible, and naively combining independently predicted tokens may lead to locally semantically implausible draft sequences.
L179: The goal of draft tree construction is therefore to extract a compact, high-quality subset of this implicit tree that can be efficiently verified by the target model.
L180: Algorithm 1 Continuity-Aware Tree Pruning
L181: 
L182: 0:  $d$ future-position logits $\{l_{i}\}_{i=1}^{d}$; N-gram model $g_{n}$; candidate threshold $\{k_{i}\}_{i=1}^{d}$; prefix context $ctx$; tree size $\theta$; beam width $w$
L183: 
L184: 0:  Final draft token tree $\mathcal{T}$
L185: 
L186: 1:  $\mathcal{C}\leftarrow\{(ctx,0)\}$ $\triangleright$ Active candidate set (sequence, score)
L187: 
L188: 2:  $\mathcal{T}\leftarrow\varnothing$ $\triangleright$ Global token tree
L189: 
L190: 3:  for $i=1$ to $d$ do
L191: 
L192: 4:   $\mathcal{C}^{\prime}\leftarrow\varnothing$
L193: 5:   for all $(seq,sc)\in\mathcal{C}$ in parallel do
L194: 
L195: 6:    $\mathcal{S}_{i}\leftarrow\text{Top-}k_{i}\text{ tokens from }l_{i}$
L196: 
L197: 7:    for all $t\in\mathcal{S}_{i}$ do
L198: 
L199: 8:      $s_{\text{logit}}\leftarrow\log(softmax(l)_{i,t}+\epsilon)$
L200: 
L201: 9:      $s_{\text{ng}}\leftarrow g_{n}(t,seq_{-n:})$ $\triangleright$ N-gram continuity score
L202: 
L203: 10:      $s^{\prime}\leftarrow sc+\textsc{Combine}(s_{\text{logit}},s_{\text{ng}})$
L204: 11:      $\mathcal{C}^{\prime}\leftarrow\mathcal{C}^{\prime}\cup\{(\textsc{Cat}(seq,t),s^{\prime})\}$
L205: 
L206: 12:      $\mathcal{T}\leftarrow\mathcal{T}\cup\{(\textsc{Cat}(seq,t),s^{\prime})\}$
L207: 
L208: 13:    end for
L209: 
L210: 14:   end for
L211: 
L212: 15:   $\mathcal{C}\leftarrow\text{Top-}w\text{ scoring pairs from }\mathcal{C}^{\prime}$
L213: 
L214: 16:  end for
L215: 
L216: 17:  return Top-$\theta$ scoring nodes from $\mathcal{T}$
L217: ### 4.2 Consistency-constrained Pruning via N-gram
L218: To extract a compact and semantically coherent draft tree from the exponentially large search space induced by parallel logits, DART performs consistency-constrained pruning guided by an established N-gram model, as shown in Algorithm cite85†1 . Starting from the prefix context, candidate tokens at each future position are first locally ranked according to their draft logits.
L219: During tree expansion, these candidates are further scored using an N-gram continuity score that measures the likelihood of appending a token given the recent $n$-token suffix of the partial sequence. The logit-based score and the N-gram score are combined to form a unified ranking criterion, which favors token sequences that are both locally probable under the draft model and globally consistent with surface-level language statistics.
L220: This constraint effectively filters out semantically implausible combinations that arise from independently predicted positions, while retaining high-quality candidates. This design is model-agnostic, decoupling the draft model’s forward computation from the tree expansion procedure. The detailed hyperparameter setting is given in Appendix cite51†D .
L221: Table 1: Speedup ratios of different methods and mean average acceptance lengths $\tau$ on MT-Bench, HumanEval, Alpaca, Math500, CodeAlpaca, LiveCodeBench and MBPP. All Qwen models are from Qwen3 family, for example, Qwen32B represents Qwen3-32B. L2 7B represents LLaMA2-Chat-7B. In SPS, we use the Qwen3-1.7B as the drafter of Qwen3-14B and Qwen3-32B with draft length 5.
L222: Model  | Method  | Speedup  | Mean
L223: Alpaca  | Codealpaca  | Humaneval  | LiveCode  | Math500  | MBPP  | MT-bench  | Speedup  | $\tau$
L224: Temperature=0  |
L225: L2 7B  | PLD  | 1.18×  | 1.75×  | 1.84×  | 1.94×  | 1.59×  | 1.59×  | 1.57×  | 1.74×  | 1.92
L226: Lookahead  | 1.42×  | 1.54×  | 1.64×  | 1.59×  | 1.82×  | 1.61×  | 1.63×  | 1.61×  | 1.81
L227: Medusa  | 2.13×  | 2.24×  | 2.22×  | 2.31×  | 2.29×  | 2.35×  | 2.12×  | 2.24×  | 2.68
L228: Hydra  | 2.72×  | 2.89×  | 2.60×  | 2.59×  | 2.69×  | 2.62×  | 2.48×  | 2.66×  | 3.55
L229: DART  | 2.95×  | 3.03×  | 2.98×  | 2.81×  | 2.84×  | 2.72×  | 2.61×  | 2.85×  | 4.08
L230: Qwen1.7B  | EAGLE3  | 1.84×  | 1.93×  | 1.94×  | 2.06×  | 2.25×  | 2.05×  | 1.98×  | 2.01×  | 3.80
L231: DART  | 2.60×  | 2.90×  | 2.79×  | 2.28×  | 2.52×  | 2.64×  | 2.57×  | 2.61×  | 3.60

L232: Qwen4B  | EAGLE3  | 2.15×  | 2.21×  | 2.20×  | 1.95×  | 2.06×  | 2.08×  | 2.17×  | 2.12×  | 3.54
L233: DART  | 2.55×  | 3.45×  | 3.25×  | 2.57×  | 2.50×  | 3.06×  | 2.73×  | 2.87×  | 3.87
L234: Qwen8B  | EAGLE3  | 2.02×  | 2.34×  | 2.37×  | 2.11×  | 2.30×  | 2.20×  | 2.08×  | 2.20×  | 3.72
L235: DART  | 2.51×  | 3.40×  | 2.80×  | 2.64×  | 2.34×  | 3.09×  | 2.22×  | 2.71×  | 3.61
L236: Qwen14B  | SPS  | 1.05×  | 1.07×  | 0.96×  | 0.94×  | 0.96×  | 0.97×  | 0.92×  | 0.98×  | 4.17
L237: EAGLE3  | 1.69×  | 2.08×  | 2.27×  | 2.08×  | 2.32×  | 1.99×  | 1.71×  | 2.02×  | 3.48
L238: DART  | 2.73×  | 3.44×  | 2.79×  | 2.69×  | 2.50×  | 2.98×  | 2.20×  | 2.77×  | 3.67
L239: Qwen32B  | SPS  | 1.07×  | 1.08×  | 1.06×  | 1.06×  | 1.06×  | 1.15×  | 1.12×  | 1.09×  | 3.45
L240: EAGLE3  | 1.72×  | 2.38×  | 2.19×  | 2.15×  | 2.31×  | 2.27×  | 1.76×  | 2.11×  | 3.85
L241: DART  | 2.03×  | 2.88×  | 2.37×  | 2.42×  | 2.46×  | 2.56×  | 2.24×  | 2.42×  | 3.76
L242: Temperature=1  |
L243: Qwen14B  | EAGLE3  | 1.62×  | 2.01×  | 2.17×  | 1.92×  | 2.10×  | 1.81×  | 1.61×  | 1.89×  | 3.38
L244: DART  | 2.38×  | 3.10×  | 2.48×  | 2.37×  | 2.29×  | 2.71×  | 1.94×  | 2.47×  | 3.61
L245: Qwen32B  | EAGLE3  | 1.57×  | 2.30×  | 2.08×  | 1.97×  | 2.15×  | 2.17×  | 1.58×  | 1.97×  | 3.67
L246: DART  | 1.84×  | 2.78×  | 2.19×  | 2.13×  | 2.16×  | 2.40×  | 1.82×  | 2.19×  | 3.55
L247: ## 5 Experiments
L248: 
L249: ### 5.1 Experimental Setup
L250: 
L251: #### Hardware.
L252: 
L253: All training and inference processes are conducted on a server equipped with 8$\times$NVIDIA H20-3e GPUs (141GB), 90 CPU cores, 900GB of RAM and PyTorch 2.8.0.
L254: #### Target models.
L255: 
L256: We mainly train DART on the Qwen3 model family (cite86†Yang et al., 2025 ), including Qwen3-1.7B, Qwen3-4B, Qwen3-8B, Qwen3-14B and Qwen3-32B. To fairly compare DART with other speculative decoding methods (e.g., Lookahead, PLD (cite87†Saxena, 2023 ), Medusa and Hydra (cite88†Ankner et al., 2024 )), we additionally train DART on LLaMA2-Chat-7B (cite89†Touvron et al., 2023 ), since these methods are not compatible with the Qwen3 family.
L257: #### Benchmarks.
L258: 
L259: We evaluate DART on a diverse suite of tasks covering instruction following, multi-turn conversation, mathematical reasoning, and code generation: MT-Bench (cite90†Zheng et al., 2023 ), HumanEval (cite91†Chen et al., 2021 ), Alpaca (cite92†Taori et al., 2023 ), Math500 (cite93†Lightman et al., 2023 ), CodeAlpaca (cite94†Lhoest et al., 2021 ), LiveCodeBench (cite95†Jain et al., 2024 ), and MBPP (cite96†Austin et al., 2021 ).
L260: Figure 5: Latency of verification, drafting forward and tree search in one draft-verify iteration when accelerating Qwen3-14B using SPS, EAGLE3 and DART. SPS has slightly lower latency in verification because of fewer draft tokens than EAGLE3 and DART.
L261: #### Implementation.
L262: Unless otherwise specified, all experiments are conducted with a batch size of 1, and experiments on EAGLE3 reuse the weights from cite97†Contributors (2025) . Other methods such as Medusa reuse their weights from their corresponding open-source repository. We do not compare DART with DiffuSpec or SpecDiff (cite72†Christopher et al., 2025 ) because their implementations are closed-source. Both DART and EAGLE3 use the draft length of 8.
L263: We give the details of training and N-gram-related settings in Appendix cite42†B and cite48†C .
L264: #### Metrics.
L265: 
L266: In this paper, we focus on the following performance-related metrics. We do not report generation quality, since DART preserves the exact output distribution of the target model.
L267: 
L268:   * •
L269: 
L270: Throughput. The actual test end-to-end speedup ratio relative to vanilla autoregressive decoding.
L271: 
L272:   * •
L273: 
L274: Average acceptance length ($\tau$). The average number of tokens generated per drafting-verification cycle, indicating the number of tokens accepted by the target model’s verification.
L275: 
L276:   * •
L277: Drafting latency. The wall-clock time spent in the draft model forward and tree search to propose candidate tokens for each verification cycle. This metric captures the overhead introduced by the draft model and directly impacts the overall end-to-end speedup.
L278: ### 5.2 Main Results
L279: #### Throughput improvement.
L280: We use vanilla autoregressive decoding as the baseline and compare DART against recent lossless speculative decoding methods, including standard speculative sampling (SPS), PLD, Hydra, Lookahead, Medusa and EAGLE3. As shown in Figure cite79†2 and Table cite98†1 , DART achieves a 2.03$\times$–3.44$\times$ throughput improvement across tasks, outperforming EAGLE3 by 30% on average. Notably, DART yields larger gains on code-related benchmarks.
L281: For example, in CodeAlpaca, DART surpasses EAGLE3 by 65% when accelerating Qwen3-14B.
L282: #### Relatively high $\tau$.
L283: 
L284: As shown in Table cite98†1 , DART achieves relatively high $\tau$ across all model scales. While DART does not always exceed EAGLE3 in $\tau$, the difference is within 0.2, and thus negligible. More importantly, due to its substantially lower drafting latency, DART converts a comparable $\tau$ into significantly higher throughput. This highlights that minimizing drafting overhead, rather than solely maximizing $\tau$, is critical for achieving superior end-to-end performance.
L285: #### Drafting latency reduction.
L286: We focus on the drafting latency of 3 model-based drafters, including SPS, DART and EAGLE3. Methods like PLD and Lookahead do not have a separate model-based drafter, so their drafting latency is not reported. As shown in Figure cite99†5 , DART consumes 1.5ms latency to finish the drafting forward and reduces drafting forward latency by $6.8\times$ and $53.3\times$ compared to EAGLE3 and SPS in case of inference of Qwen3-14B.
L287: The tree pruning will take another 2ms to get the final draft token tree, which is also negligible latency and more efficient than the tree search of EAGLE3. This enables DART to accelerate LLM inference with negligible drafting overhead.
L288: ### 5.3 Ablation Study
L289: #### N-gram effectiveness.
L290: The N-gram constraint is a key component in DART for pruning the exponentially large search space induced by parallel token prediction. To evaluate its impact on drafting efficiency, we compare average acceptance length $\tau$ with and without N-gram pruning across multiple benchmarks. As shown in Table cite100†2 , incorporating N-gram pruning consistently leads to substantial improvements in $\tau$ across all evaluated benchmarks.
L291: This demonstrates that N-gram pruning effectively removes low-quality branches in the draft token tree while preserving high-probability continuations, resulting in more efficient draft construction and higher acceptance rates during verification.
L292: Table 2: Effect of N-gram pruning on drafting efficiency. Reported values are the average number of accepted draft tokens $\tau$ measured under speculative decoding on each benchmark.
L293: 
L294: -  | HumanEval  | Alpaca  | Math500  | CodeAlpaca
L295: w/o N-gram  | 3.13  | 2.76  | 2.89  | 3.85
L296: w/ N-gram  | 3.63 ($\uparrow$0.5)  | 3.26 ($\uparrow$0.5)  | 3.37 ($\uparrow$0.48)  | 4.59 ($\uparrow$0.74)
L297: #### Shifted logits prediction.
L298: We investigate the effect of shifted logits prediction in the DART inference pipeline. Specifically, we train two DART models based on Qwen3-4B from scratch under identical training configurations: one model adopts shifted logits prediction, while the other uses unshifted logits prediction. Unshifted logits prediction means logits predicted at masked positions are interpreted as predictions for the tokens at the same positions.
L299: After training, we evaluate the prediction accuracy at multiple future positions on the same test data. The results are summarized in Table cite101†3 . We observe that shifted logits prediction substantially improves the accuracy of the first predicted position, increasing from 57.7% to 71.1%. In addition, modest but consistent accuracy gains are observed for subsequent positions in both hit@1 and hit@10 metrics.
L300: Table 3: Accuracy of multiple future positions under shifted and unshifted logits prediction. Hit@k denotes the proportion of cases where the ground-truth token appears among the top-$k$ predictions ranked by model logits. $\alpha$-$k$ denotes the prediction accuracy at the $k$-th future position.
L301: Position  | $\alpha$-1  | $\alpha$-2  | $\alpha$-3
L302: Unshifted  | 57.7%  | 38.1%  | 25.1%
L303: Shifted  | 71.1% ($\uparrow$13.4)  | 41.0% ($\uparrow$2.9)  | 27.6% ($\uparrow$2.5)
L304: Unshifted(hit@10)  | 87.1%  | 74.2%  | 63.2%
L305: Shifted(hit@10)  | 93.2% ($\uparrow$6.1)  | 76.7% ($\uparrow$2.5)  | 65.9% ($\uparrow$2.7)
L306: #### Annealing coefficient in DART training.
L307: During DART training, we apply annealed KL divergence objective to prevent the increasing uncertainty of longer-horizon predictions from disturbing overall training stability. Specifically, we introduce an annealing coefficient $\gamma$ to progressively downweight the supervision on future positions. To identify an appropriate value of $\gamma$, we train multiple DART models for Qwen3-4B from scratch with $\gamma\in\{0.5,0.6,0.7,0.8,0.9\}$, all using shifted logits prediction.
L308: The case $\gamma=1.0$ corresponds to no annealing and serves as the shifted-logits baseline from the previous ablation. Table cite102†4 compares the prediction accuracy at multiple future positions as well as the resulting average accepted length $\tau$. We observe a clear trade-off: smaller values of $\gamma$ improve accuracy at earlier positions while degrading performance at later positions, whereas larger $\gamma$ favors longer-horizon predictions.
L309: Since accuracy at early positions is more critical for speculative decoding, annealing the KL objective leads to a higher average acceptance length $\tau$, which translates linearly into end-to-end decoding throughput. Among all settings, $\gamma=0.6$ achieves the best balance between early-position accuracy and acceptance length $\tau$, and is therefore used as the default configuration in DART.
L310: Table 4: Effect of the annealing coefficient $\gamma$ on prediction accuracy and average acceptance length $\tau$ on HumanEval.
L311: $\gamma$  | $\alpha$-1  | $\alpha$-2  | $\alpha$-3  | $\alpha$-4  | $\alpha$-5  | $\alpha$-6  | $\tau$
L312: 0.5  | 76.2%  | 45.0%  | 28.7%  | 18.4%  | 13.0%  | 10.6%  | 3.59
L313: 0.6  | 75.5%  | 44.7%  | 29.0%  | 19.2%  | 13.8%  | 11.2%  | 3.63
L314: 0.7  | 74.7%  | 44.1%  | 28.9%  | 19.6%  | 14.3%  | 11.8%  | 3.57
L315: 0.8  | 73.8%  | 43.2%  | 28.8%  | 19.8%  | 14.8%  | 12.2%  | 3.54
L316: 0.9  | 72.5%  | 42.1%  | 28.1%  | 19.4%  | 14.9%  | 12.4%  | 3.52
L317: 1.0  | 71.1%  | 41.0%  | 27.6%  | 19.3%  | 15.0%  | 12.6%  | 3.48
L318: ### 5.4 Larger Batch Sizes Study
L319: 
L320: We also conduct experiments with batch sizes larger than 1 with DART and EAGLE3. As shown in Table cite103†5 , although throughput improvement decays as the batch size increases due to the more compute-bound brought by larger batch size, DART still gets larger gains than EAGLE3.
L321: Table 5: Throughput improvements under larger batch sizes on the HumanEval benchmark, evaluated on H20-3e device, for EAGLE3 and DART relative to autoregressive decoding (without speculative decoding) when target model is Qwen3-4B.
L322: Batch Size  | 2  | 4  | 8  | 16  | 24  | 32  | 48  | 64
L323: EAGLE3  | 1.84$\times$  | 1.69$\times$  | 1.48$\times$  | 1.32$\times$  | 1.29$\times$  | 1.28$\times$  | 1.24$\times$  | 1.22$\times$
L324: DART  | 2.16$\times$  | 2.01$\times$  | 1.77$\times$  | 1.57$\times$  | 1.51$\times$  | 1.48$\times$  | 1.47$\times$  | 1.45$\times$
L383: ## Appendix B Training Details
L384: 
L385: ### B.1 Training Implementation
L386: 
L387: The code of training DART is based on SGLang’s open-source repository SpecForge (cite109†Shenggui Li, 2025 ).
L388: ### B.2 Training Setup
L389: We train the DART models of Qwen3-family and LLaMA2-Chat-7B under our carefully designed recipe. Unless otherwise specified, all training adopt a context length of 6400 and draft length of 8. We use the AdamW (cite110†Loshchilov & Hutter, 2017 ) optimizer, with gradient clipping of 0.5 and beta values ($\beta_{1}$, $\beta_{2}$) set to (0.9, 0.999). The learning rate is set to 2e-5, and training is conducted for 3 epochs. DART is optimized using a cosine annealing learning rate schedule with linear warmup.
L390: The more detailed hyperparameters (e.g., number of heads, hidden dimension) of the customized Transformer decoder layer in DART keeps aligned with the target model. Training is conducted on 8 $\times$ NVIDIA H20-3e GPUs.
L391: #### Trainable parameters
L392: As shown in Figure cite82†3 , the trainable parameters in DART include the fully connected (FC) layer (whose output dimensionality matches the hidden size of the target model), decoder layer, and the LM head. DART shares the embedding layer with the target LLM, which remains frozen during training. In addition, the mask representation is also treated as a set of trainable parameters and is initialized with random values. This design choice follows the practice adopted in dLLM (cite80†Nie et al., 2025 ).
L393: #### Training data.
L394: Our training data is drawn from ShareGPT and UltraChat (cite111†Ding et al., 2023 ). After filtering, the combined dataset contains approximately 280K examples. We use the same data sources as EAGLE3, ensuring consistency in the training corpus. DART takes the hidden states of the target model as input.
L395: Specifically, we select the outputs of the $1$st, $(\texttt{num\_layers}/2-1)$-th, and $(\texttt{num\_layers}-4)$-th transformer layers as inputs to DART, following the same layer selection strategy as EAGLE3.
L520: ## Appendix C N-gram Details
L521: ### C.1 N-gram Construction
L522: We implement the N-gram using a trie data structure to achieve high retrieval performance. The construction relies on open-source dataset Dolma 3 Mix (cite112†Olmo et al., 2025 ), which covers multiple fields and types. The N-gram is built based on the tokenizer of Qwen3 family or LLaMA2 family. To balance retrieval efficiency and memory overhead during inference, we adopt a 3-gram model in DART, which consists of approximately 1.3 billion tree nodes and occupies about 43.5 GB of disk space.
L523: ### C.2 N-gram Usage at Inference
L524: During inference, the N-gram model is queried to provide scores for candidate tokens given the preceding context. As mentioned in Algorithm cite85†1 , there are $k_{i}$ possible token candidates at position $i$ given a preceding context. To efficiently retrieve the scores for all $k_{i}$ candidate tokens with the same preceding context, we leverage the structural properties of trie. Specifically, we first locate the node corresponding to the preceding context.
L525: From this node, we can directly access all its child nodes, each representing a candidate token. This approach allows us to retrieve scores for all $k_{i}$ candidates in a single traversal, significantly reducing the number of required lookups compared to querying each candidate token individually.
L526: To support this efficient retrieval mechanism, we implement the N-gram trie in C++ and load it into CPU RAM before inference. During execution, the N-gram trie occupies roughly 100 GB of CPU RAM. While this memory footprint may appear large, it is well aligned with modern inference servers, which typically provision hundreds of gigabytes of system memory and often leave substantial CPU RAM underutilized during LLM inference (cite113†Ma et al., 2025 ; cite114†Luo et al., 2025 ; cite115†Kong et al., 2024 ).
L527: Moreover, the footprint is shared across multiple inference processes. Thus, the increased RAM usage represents a practical design trade-off to achieve low-latency N-gram retrieval, rather than a fundamental limitation of our approach. As shown in Figure cite116†7 , the average latency of N-gram retrieval is around 6 $\mu$s per query after warmup, which is negligible compared to the overall inference time.
L528: Figure 7: N-gram retrieval latency over time. The timeline is divided into 200 ms intervals, and the average latency per query is recorded for each interval. After the warmup period, the average latency stabilizes around 6 $\mu$s per query after warmup.
L529: ## Appendix D Tree Pruning Algorithm Details
L530: 
L531: This section provides the detailed hyperparameter settings and implementation specifics of the continuity-aware tree pruning algorithm described in Algorithm cite85†1 . The pruning procedure is implemented in C++ for efficiency, and parallelized using OpenMP along both the batch dimension and the candidate expansion process.
L532: At each future position $i\in\{1,\ldots,d\}$, we select the top-$k_{i}$ tokens from the corresponding draft logits $l_{i}$. In all experiments, we set a uniform candidate threshold $k_{i}=25$ for all positions. The active candidate set is maintained using beam pruning with beam width $w=20$, which controls the maximum number of partial sequences retained at each depth.
L533: The global draft token tree $\mathcal{T}$ is bounded by a maximum size $\theta=59$, and only the top-$\theta$ scoring nodes are preserved for downstream verification. This constraint ensures a balance between drafting diversity and verification efficiency.
L534: 
L535: For each candidate extension, we compute a combined score consisting of a logit-based likelihood term and an N-gram continuity score. Specifically, the logit score is defined as
L536: 
L537:  | $$s_{\text{logit}}=\log(softmax(l)_{i,t}+\epsilon),$$  |
L538: where $l_{i,t}$ is the value of the logit for token $t$ at position $i$, and the N-gram score $s_{\text{ng}}$ is defined as
L539: 
L540:  | $$s_{\text{ng}}=\log(\mathrm{Pr}(t\ |\ \text{context})+\epsilon),$$  |
L541: 
L542: where $\mathrm{Pr}(t\ |\ \text{context})$ is the conditional probability of token $t$ provided by the pretrained N-gram model, and $\epsilon$ is a small constant for numerical stability.
L543: 
L544: The final score increment is computed via the Combine function:
L545:  | $$\textsc{Combine}(s_{\text{logit}},s_{\text{ng}})=(w_{\text{logit}}\cdot s_{\text{logit}}+w_{\text{ng}}\cdot s_{\text{ng}})\cdot w_{\text{level}},$$  |
L546: 
L547: where the N-gram weight is fixed to $w_{\text{ng}}=0.5$, and the logit weight decays with tree depth (level refers to the depth in the draft tree):
L548: 
L549:  | $$w_{\text{logit}}=0.9^{\text{level}}.$$  |
L550: This design prioritizes N-gram continuity at deeper levels because of the low accuracy of logit of later positions. The level weight $w_{\text{level}}$ is defined as
L551: 
L552:  | $$w_{\text{level}}=(\text{level}+1)^{-0.7},$$  |
L553: 
L554: which encourages longer draft sequences by favoring nodes at greater depths.
L555: 
L556: In practice, we implement the pruning algorithm in C++ and parallelize the it with OpenMP. We also bind both N-gram and worker threads to the same NUMA node to avoid expensive cross-node memory access overheads.
L557: Overall, the proposed pruning strategy efficiently constructs a compact yet high-quality draft token tree by jointly considering model confidence, token continuity, and structural constraints.
L558: Table 6: Throughput and relative speedup across batch sizes evaluated on H20-3e (141G) device when target model is Qwen3-4B.
L559:  | Throughput (tokens/s)  | Speedup
L560: Batch size  | Baseline  | EAGLE3  | DART  | EAGLE3  | DART
L561: 2  | 105.8  | 194.6  | 228.7  | 1.84×  | 2.16×
L562: 4  | 172.1  | 291.1  | 346.3  | 1.69×  | 2.01×
L563: 8  | 243.3  | 359.0  | 431.1  | 1.48×  | 1.77×
L564: 16  | 309.4  | 408.6  | 484.4  | 1.32×  | 1.57×
L565: 24  | 338.3  | 436.4  | 510.9  | 1.29×  | 1.51×
L566: 32  | 346.0  | 443.2  | 512.9  | 1.28×  | 1.48×
L567: 48  | 364.6  | 450.9  | 538.5  | 1.24×  | 1.47×
L568: 64  | 370.0  | 453.3  | 538.7  | 1.22×  | 1.45×
L569: Table 7: Throughput and relative speedup across batch sizes evaluated on H20-3e (141G) device when target model is Qwen3-8B.
L570:  | Throughput (tokens/s)  | Speedup
L571: Batch size  | Baseline  | EAGLE3  | DART  | EAGLE3  | DART
L572: 2  | 94.3  | 182.1  | 203.5  | 1.93×  | 2.16×
L573: 4  | 160.6  | 246.5  | 268.6  | 1.53×  | 1.67×
L574: 8  | 229.6  | 290.9  | 314.8  | 1.26×  | 1.36×
L575: 16  | 297.2  | 327.8  | 343.3  | 1.09×  | 1.14×
L576: 24  | 329.4  | 335.7  | 353.5  | 1.01×  | 1.06×
L577: 32  | 339.7  | 351.4  | 353.6  | 1.02×  | 1.04×
L578: 48  | 354.2  | 352.9  | 366.4  | 0.99×  | 1.03×
L579: 64  | 360.3  | 356.4  | 366.1  | 0.98×  | 1.01×
