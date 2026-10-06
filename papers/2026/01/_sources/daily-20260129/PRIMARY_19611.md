# Exact-v1 necessary primary — 2601.19611

Original returned context retained; only necessary core, controls, setup and direct counterclaims adopted.

## jan29_systemfour_head

Explicit Multi-head Attention for Inter-head Interaction in Large Language Models (https://arxiv.org/html/2601.19611v1)
citeturn28514view1 [wordlim: 200] Crawled: today; Content type: text/html; Source: open({"ref_id":"https://arxiv.org/html/2601.19611v1","lineno":null}); Total lines: 440


## jan29_systemfour_route

Explicit Multi-head Attention for Inter-head Interaction in Large Language Models (https://arxiv.org/html/2601.19611v1)
citeturn28515view0 [wordlim: 200] Crawled: today; Content type: text/html; Source: find({"ref_id":"https://arxiv.org/html/2601.19611v1","pattern":"3.2"}); Total lines: 440
L15:   1. cite5†Abstract L16:   2. cite6†1 Introduction L17:   3. cite7†2 Preliminary L18:   4. cite8†3 Related Works L19:     1. cite9†3.1 Differential Transformer L20:     2. cite10†3.2 Talking-Heads Attention L21:   5. cite11†4 Method L22:     1. cite12†4.1 Head-level Linear Combination Module L23:     2. cite13†4.2 Multihead Explicit Attention (MEA) L24:     3. cite14†4.3 Towards a Unified View of Attention Mechanisms L25:   6. cite15†5 Experiments L26:     1. cite16†5.1 From Scratch Pre-training L27:       1. cite17†5.1.1 Settings L28:         1. cite18†Model L29:         2. cite19†Training Settings L115: ### 3.2 Talking-Heads Attention
L116: 
L117: Talking-Heads Attention (THA) [cite44†22 ] enhances the expressiveness of MHA by introducing learnable interactions between attention heads. Unlike standard MHA, where each head operates independently and their outputs are merged only at the final stage, THA enables inter-head communication by applying learned linear projections over the attention scores both before and after the softmax operation.
L259:   * [5] T. Dao, D. Y. Fu, S. Ermon, A. Rudra, and C. Ré (2022) FlashAttention: fast and memory-efficient exact attention with IO-awareness. In Advances in Neural Information Processing Systems, Cited by: cite88†§3.2 .
L270:   * [14] I. Loshchilov and F. Hutter (2019) Decoupled Weight Decay Regularization. In Proceedings of the International Conference on Learning Representations, Cited by: cite95†§5.1.1 .
L271:   * [15] A. Lozhkov, L. Ben Allal, L. von Werra, and T. Wolf (2024) FineWeb-edu: the finest collection of educational content. arXiv preprint arXiv:2406.17557. External Links: 2406.17557 Cited by: cite94†Appendix C .
L272:   * [16] Meta (2025) Llama 3.2–1b. Note: cite96†https://huggingface.co/meta-llama/Llama-3.2-1B†huggingface.co Accessed: 2025-09-05 Cited by: cite97†§5.1.1 .
L273:   * [17] G. Penedo, Q. Malartic, D. Hesslow, R. Cojocaru, H. Alobeidli, A. Cappelli, B. Pannier, E. Almazrouei, and J. Launay (2023) The refinedweb dataset for falcon llm: outperforming curated corpora with web data, and web data only. In Advances in Neural Information Processing Systems (NeurIPS), Cited by: cite94†Appendix C .
L274:   * [18] R. Peng, Y. Zhou, Q. Guo, Y. Gao, H. Yan, X. Qiu, and D. Lin (2025) Data-free weight compress and denoise for large language models. External Links: 2402.16319, cite98†Link Cited by: cite99†§5.2 .
L275:   * [19] J. Qiu, H. Lv, Z. Jin, R. Wang, W. Ning, J. Yu, C. Zhang, Z. Li, P. Chu, Y. Qu, J. Shi, L. Lu, R. Peng, Z. Zeng, H. Tang, Z. Lei, J. Hong, K. Chen, Z. Fei, R. Xu, W. Li, Z. Tu, L. Dahua, Y. Qiao, H. Yan, and C. He (2024) WanJuan-CC: a safe and high-quality open-sourced english webtext dataset. arXiv preprint arXiv:2402.19282. Cited by: cite94†Appendix C , cite100†Appendix C .
L276:   * [20] Z. Qiu, Z. Wang, B. Zheng, Z. Huang, K. Wen, S. Yang, R. Men, L. Yu, F. Huang, S. Huang, D. Liu, J. Zhou, and J. Lin (2025) Gated attention for large language models: non-linearity, sparsity, and attention-sink-free. External Links: 2505.06708, cite101†Link Cited by: cite91†§5.1.2 .
L277:   * [21] D. Rein et al. (2023) GPQA: a graduate-level google-proof q&a benchmark. arXiv preprint arXiv:2311.12022. Cited by: cite84†§5.2.2 .
L278:   * [22] N. Shazeer, Z. Lan, Y. Cheng, N. Ding, and L. Hou (2020) Talking-heads attention. arXiv preprint arXiv:2003.02436. Cited by: cite82†§1 , cite102†§3.2 , cite103†§4.3 .
L279:   * [23] N. Shazeer (2019) Fast transformer decoding: one write-head is all you need. External Links: 1911.02150, cite104†Link Cited by: cite82†§1 , cite83†§2 .
L280:   * [24] N. Shazeer (2020) Glu variants improve transformer. arXiv preprint arXiv:2002.05202. External Links: cite105†Link Cited by: cite106†§2 .
L281:   * [25] J. Su, Y. Lu, S. Pan, A. Murtadha, B. Wen, and Y. Liu (2023) RoFormer: enhanced transformer with rotary position embedding. External Links: 2104.09864, cite107†Link Cited by: cite108†§2 , cite109†§4.3 .
L282:   * [26] H. Sun, Y. Min, Z. Chen, W. X. Zhao, L. Fang, Z. Liu, Z. Wang, and J. Wen (2025) Challenging the boundaries of reasoning: an olympiad-level math benchmark for large language models. External Links: 2503.21380, cite110†Link Cited by: cite84†§5.2.2 .
L283:   * [27] T. Sun et al. (2024) LiveMathBench: a continuously updated benchmark for evaluating mathematical reasoning of llms. arXiv preprint arXiv:2412.04468. Cited by: cite84†§5.2.2 .
L284:   * [28] Q. Team (2025) Qwen3 technical report. External Links: 2505.09388, cite111†Link Cited by: cite112†§5.2.1 .
L285:   * [29] J. Tow, M. Bellagente, D. Mahan, and C. Riquelme (2023) StableLM 3b 4e1t. External Links: Link Cited by: cite113†§5.1.2 .


## jan29_systemfour_core

Explicit Multi-head Attention for Inter-head Interaction in Large Language Models (https://arxiv.org/html/2601.19611v1)
citeturn28516view0 [wordlim: 200] Crawled: today; Content type: text/html; Source: open({"ref_id":"https://arxiv.org/html/2601.19611v1","lineno":121}); Total lines: 440
L112: where $\mathbf{A}_{i}$ denotes the differential attention scores defined in equation cite48†4 , and $\mathbf{V}_{2i-1},\mathbf{V}_{2i}$ are the value vectors for the corresponding heads. The function $\text{GroupNorm}(\cdot)$ represents an RMSNorm operation applied to the concatenated outputs of all head pairs, and $\lambda_{\text{init}}$ is a fixed scalar used to initialize the learnable coefficients $\lambda_{i}$.
L113: In their paper [cite43†34 ], the DFA variant without GroupNorm was shown to perform nearly identically to standard attention. We offer a new perspective to explain this phenomenon: DFA without GroupNorm can be interpreted as a special case of Talking-Heads Attention that only applies post-softmax transformations, and its corresponding derivation is provided in Appendix cite29†A .
L114: Furthermore, we demonstrate that such a formulation tends to degenerate under modern LLM training settings, and analyze the underlying causes of this degeneration. Please refer to Section cite14†4.3 for detailed discussions.
L115: ### 3.2 Talking-Heads Attention
L116: 
L117: Talking-Heads Attention (THA) [cite44†22 ] enhances the expressiveness of MHA by introducing learnable interactions between attention heads. Unlike standard MHA, where each head operates independently and their outputs are merged only at the final stage, THA enables inter-head communication by applying learned linear projections over the attention scores both before and after the softmax operation.
L118: Within our unified framework, THA can be interpreted as introducing two learnable head-level transformation matrices: ${\bm{T}}^{\text{QK}}\in\mathbb{R}^{h\times h}$, which is applied to the attention logits before the softmax operation, and ${\bm{T}}^{\text{V}}\in\mathbb{R}^{h\times h}$, which is applied to the attention weights after softmax.
L119: 
L120: Specifically, for each head $i$, the softmax-normalized attention score computation proceeds as:
L121:  | $$\mathbf{A}_{i}=\text{softmax}\left(\sum_{j}{\bm{T}}^{\text{QK}}_{i,j}\cdot\frac{\phi(\mathbf{Q}_{j})\,\phi(\mathbf{K}_{j})^{\top}}{\sqrt{d_{qk}}}\right),$$  |  | (7)
L122: 
L123: where we denote the softmax-normalized attention score map as $\mathbf{A}\in\mathbb{R}^{n\times n\times h}$.
L124: 
L125: The final context representation and overall attention output are then computed as:
L126:  | $\displaystyle\mathbf{C}^{\prime}_{i}=\sum_{j}{\bm{T}}^{\text{V}}_{i,j}\cdot\mathbf{A}_{j}\cdot\mathbf{V}_{i},$  |  | (8)
L127:  | $\displaystyle\text{THA}(\mathbf{X})=\text{Concat}(\mathbf{C}^{\prime}_{1},\ldots,\mathbf{C}^{\prime}_{h}){\bm{W}}^{\text{O}}.$  |  | (9)
L128: By introducing two layers of head-level linear transformation, THA enables richer interactions among attention heads while preserving computational efficiency. However, the original THA design is not compatible with FlashAttention [cite49†5 ]. In Section cite14†4.3 , we will further demonstrate that under small learning rates, even enhanced THA fails to activate its intended cross-head functionality during training, effectively degenerating into standard MHA behavior.
L129: ## 4 Method
L130: In this section, we first introduce a module called the Head-level Linear Combination (HLC) module, which serves as a fundamental building block of our approach. We then present our proposed attention mechanism, Multihead Explicit Attention (MEA), in detail. Finally, we present a unified theoretical perspective under the MEA framework, showing that certain ablated variants of Differential Transformer and Talking-Heads Attention can be viewed as incomplete forms of MEA.
L131: We further explain why such variants fail to bring consistent improvements from an optimization standpoint.
L132: ### 4.1 Head-level Linear Combination Module
L133: Recent research has explored the idea of matrix decomposition techniques to improve the efficiency and expressiveness of attention mechanisms [cite42†6 , cite50†36 ]. Inspired by these developments, we propose a Head-level Linear Combination (HLC) module, which reparameterizes the projection tensors by applying a head-level linear combination. This formulation enables parameter sharing and enhanced inter-head interaction without modifying the overall attention structure.
L134: Formally, given a projected head-aware tensor ${\bm{\mathsfit{T}}}_{\text{comp}}\in\mathbb{R}^{N\times h^{\prime}\times d}$, we define:
L135: 
L136:  | $\displaystyle\text{HLC}({\bm{W}}_{\text{lc}}^{\text{T}},{\bm{\mathsfit{T}}}_{\text{comp}}):=\text{einsum}(\texttt{"n h' d, h' h -> n h d"},{\bm{\mathsfit{T}}}_{\text{comp}},{\bm{W}}^{\text{T}}_{\text{lc}}),$  |  | (10)
L137: where ${\bm{W}}^{\text{T}}_{\text{lc}}\in\mathbb{R}^{h^{\prime}\times h}$ is a learnable reweighting matrix that synthesizes $h$ composite heads from $h^{\prime}$ component attention heads (we assume $h^{\prime}=h$ unless otherwise specified). These weights are shared across the sequence and feature dimensions, enabling head-level feature mixing while preserving the spatial structure of the input.
L138: ### 4.2 Multihead Explicit Attention (MEA)
L139: In attention modules, query, key, and value vectors are obtained by linearly projecting the hidden activations through learned matrices. The pre-softmax attention scores are computed as inner products between query and key vectors in a shared Hilbert space to form a kernel fuction [cite51†3 ], often augmented with positional encoding. The final contextual output is computed as a weighted sum over value vectors at the sequence level, where the weights come from a softmax distribution over these inner products.
L140: These observations highlight a crucial property: the representations ${\bm{q}}$, ${\bm{k}}$, and ${\bm{v}}$ exhibit intrinsic linear structure.
L141: Motivated by this insight, we propose Multihead Explicit Attention (MEA), an attention variant built upon the HLC module. MEA improves the representational flexibility of the attention mechanism by learning explicit, head-level compositions over the key and value tensors prior to attention computation.
L142: Formally, let ${\bm{\mathsfit{K}}}_{\text{comp}},{\bm{\mathsfit{V}}}_{\text{comp}}\in\mathbb{R}^{N\times h^{\prime}\times d}$ denote the pre-mixed key and value tensors, where $N$ is the sequence length, $h$ is the number of attention heads, and $d$ is the dimensionality per head. MEA applies the following linear transformations:


## jan29_systemfour_eval

Explicit Multi-head Attention for Inter-head Interaction in Large Language Models (https://arxiv.org/html/2601.19611v1)
citeturn28517view0 [wordlim: 200] Crawled: today; Content type: text/html; Source: open({"ref_id":"https://arxiv.org/html/2601.19611v1","lineno":143}); Total lines: 440
L137: where ${\bm{W}}^{\text{T}}_{\text{lc}}\in\mathbb{R}^{h^{\prime}\times h}$ is a learnable reweighting matrix that synthesizes $h$ composite heads from $h^{\prime}$ component attention heads (we assume $h^{\prime}=h$ unless otherwise specified). These weights are shared across the sequence and feature dimensions, enabling head-level feature mixing while preserving the spatial structure of the input.
L138: ### 4.2 Multihead Explicit Attention (MEA)
L139: In attention modules, query, key, and value vectors are obtained by linearly projecting the hidden activations through learned matrices. The pre-softmax attention scores are computed as inner products between query and key vectors in a shared Hilbert space to form a kernel fuction [cite51†3 ], often augmented with positional encoding. The final contextual output is computed as a weighted sum over value vectors at the sequence level, where the weights come from a softmax distribution over these inner products.
L140: These observations highlight a crucial property: the representations ${\bm{q}}$, ${\bm{k}}$, and ${\bm{v}}$ exhibit intrinsic linear structure.
L141: Motivated by this insight, we propose Multihead Explicit Attention (MEA), an attention variant built upon the HLC module. MEA improves the representational flexibility of the attention mechanism by learning explicit, head-level compositions over the key and value tensors prior to attention computation.
L142: Formally, let ${\bm{\mathsfit{K}}}_{\text{comp}},{\bm{\mathsfit{V}}}_{\text{comp}}\in\mathbb{R}^{N\times h^{\prime}\times d}$ denote the pre-mixed key and value tensors, where $N$ is the sequence length, $h$ is the number of attention heads, and $d$ is the dimensionality per head. MEA applies the following linear transformations:
L143:  | $\displaystyle{\bm{\mathsfit{K}}}_{\text{lc}}=\text{HLC}({\bm{W}}_{\text{lc}}^{\text{K}},{\bm{\mathsfit{K}}}_{\text{comp}}),\quad{\bm{\mathsfit{V}}}_{\text{lc}}=\text{HLC}({\bm{W}}_{\text{lc}}^{\text{V}},{\bm{\mathsfit{V}}}_{\text{comp}}),$  |  | (11)
L144: where ${\bm{W}}_{\text{lc}}^{\text{K}},{\bm{W}}_{\text{lc}}^{\text{V}}\in\mathbb{R}^{h^{\prime}\times h}$ are learnable head-combination matrices that project the original $h$ heads into $h^{\prime}$ mixed heads. By replacing the original key and value tensors $\mathbf{K}$ and $\mathbf{V}$ with their linearly composed counterparts $\mathbf{K}_{\text{lc}}$ and $\mathbf{V}_{\text{lc}}$ in equation cite52†2 , MEA preserves the standard attention formulation while enhancing head-level expressiveness.
L145: Inspired by the Differential Transformer, we further stabilize training and align the statistical properties across attention heads by applying Group Normalization over the concatenated head outputs:
L146: 
L147:  | $$\text{MEA}(\mathbf{X})=\text{Concat}(\text{GroupNorm}(\mathbf{C}_{1},\ldots,\mathbf{C}_{h^{\prime}})){\bm{W}}^{\text{O}},$$  |  | (12)
L148: 
L149: where $\text{GroupNorm}(\cdot)$ denotes an RMSNorm operation applied across the head dimension.
L150: ### 4.3 Towards a Unified View of Attention Mechanisms
L151: 
L152: A widely used positional encoding scheme in LLMs is RoPE [cite47†25 ], which preserves linear combination under position embedding. Specifically, RoPE fuction $\phi(\cdot)$ satisfies the following property:
L153: 
L154:  | $$a_{1}\phi({\bm{q}}_{1})+a_{2}\phi({\bm{q}}_{2})=\phi(a_{1}{\bm{q}}_{1}+a_{2}{\bm{q}}_{2}),\quad b_{1}\phi({\bm{k}}_{1})+b_{2}\phi({\bm{k}}_{2})=\phi(b_{1}{\bm{k}}_{1}+b_{2}{\bm{k}}_{2}),$$  |  | (13)
L155: where $a_{1},a_{2}$ and $b_{1},b_{2}$ are arbitrary real scalars.
L156: 
L157: Figure 1: Comparison of how different attention variants compute pre-softmax attention scores, using MHA-based variants as an example. In the modified THA, the learnable linear combination is moved earlier in the computation flow, making it equivalent to MEA’s pre-softmax operation.
L158: In equation cite53†7 , the learnable linear transformation is applied to the attention scores before the inner product between queries and keys within each head. However, this pre-softmax score mixing scheme, as originally proposed in THA, has been shown to yield negligible performance improvements [cite44†22 ].
L159: To address this, we move the learnable linear combination module earlier in the computation pipeline (see Figure cite54†1 ). Generalizing this formulation to the GQA setting and referencing equation cite55†13 , we arrive at the following expression:
L160:  | $\displaystyle\mathbf{A}_{i}$  | $\displaystyle=\text{softmax}\left(\sum_{j}{\bm{T}}^{\text{QK}}_{G(i),G(j)}\cdot\frac{\phi(\mathbf{Q}_{i})\,\phi\left(\mathbf{K}_{G(j)}\right)^{\top}}{\sqrt{d_{qk}}}\right)$  |  | (14)
L161:  |  | $\displaystyle=\text{softmax}\left(\frac{\phi(\mathbf{Q}_{i})\,\phi\left(\sum_{j}{\bm{T}}^{\text{QK}}_{G(i),G(j)}\cdot\mathbf{K}_{G(j)}\right)^{\top}}{\sqrt{d_{qk}}}\right)$  |
L162:  |  | $\displaystyle=\text{softmax}\left(\frac{\phi(\mathbf{Q}_{i})\,\phi\left(\text{HLC}({\bm{T}}^{\text{QK}},\mathbf{K})_{G(i)}\right)^{\top}}{\sqrt{d_{qk}}}\right),$  |  | (15)
L163: Similarly, we extend the post-attention score mixing formulation in equation cite56†8 to the GQA setting:
L164: 
L165:  | $$\mathbf{C}^{\prime}_{i}=\sum_{j}{\bm{T}}^{\text{V}}_{G(i),G(j)}\cdot\mathbf{A}_{j}\cdot\mathbf{V}_{G(i)},$$  |  | (16)
L166: 
L167: and further modify the computation as:
L168: 
L169:  | $\displaystyle\mathbf{C}^{\prime}_{i}=\mathbf{A}_{i}\cdot\sum_{j}{\bm{T}}^{\text{V}}_{G(i),G(j)}\cdot\mathbf{V}_{G(j)}=\mathbf{A}_{i}\cdot\text{HLC}({\bm{T}}^{\text{V}},\mathbf{V})_{G(i)},$  |  | (17)


## jan29_systemfour_settings

Explicit Multi-head Attention for Inter-head Interaction in Large Language Models (https://arxiv.org/html/2601.19611v1)
citeturn28518view0 [wordlim: 200] Crawled: today; Content type: text/html; Source: open({"ref_id":"https://arxiv.org/html/2601.19611v1","lineno":170}); Total lines: 440
L163: Similarly, we extend the post-attention score mixing formulation in equation cite56†8 to the GQA setting:
L164: 
L165:  | $$\mathbf{C}^{\prime}_{i}=\sum_{j}{\bm{T}}^{\text{V}}_{G(i),G(j)}\cdot\mathbf{A}_{j}\cdot\mathbf{V}_{G(i)},$$  |  | (16)
L166: 
L167: and further modify the computation as:
L168: 
L169:  | $\displaystyle\mathbf{C}^{\prime}_{i}=\mathbf{A}_{i}\cdot\sum_{j}{\bm{T}}^{\text{V}}_{G(i),G(j)}\cdot\mathbf{V}_{G(j)}=\mathbf{A}_{i}\cdot\text{HLC}({\bm{T}}^{\text{V}},\mathbf{V})_{G(i)},$  |  | (17)
L170: where $\text{HLC}(\cdot)$ denotes the Head-level Linear Combination module.
L171: 
L172: This reformulation can be shown to be optimization-equivalent to the original post-softmax mixing in THA; see Appendix cite30†B for detailed derivations. Notably, DFA without GroupNorm is also a special case of this post-softmax interaction pattern, and its corresponding derivation is provided in Appendix cite29†A .
L173: By comparing with equation cite57†11 , we observe that both the modified THA and DFA without GroupNorm adopt the same—or even weaker—pre-attention computation as MEA, applying the HLC module only to the key-value states. Without additional modifications such as GroupNorm, these formulations tend to degenerate into standard attention, thereby limiting their practical effectiveness.
L174: 
L175: Consider replacing a standard linear layer weight ${\bm{W}}^{\text{T}}$ with an HLC-based reparameterization, denoted as
L176:  | $\displaystyle\widetilde{{\bm{W}}}^{\text{T}}={\bm{W}}_{\text{lc}}\otimes{\bm{W}}_{\text{comp}},$  |  | (18)
L177: which satisfies that $\widetilde{{\bm{W}}}^{\text{T}}{\bm{\mathsfit{X}}}=\text{HLC}({\bm{W}}_{\text{lc}},{\bm{W}}_{\text{comp}}{\bm{\mathsfit{X}}}).$ Here, the operator $\otimes$ represents a head-wise recombination operation, which can be viewed as a structured generalization of standard matrix multiplication.
L178: Importantly, this operator preserves key algebraic properties, including associativity with respect to matrix multiplication and distributivity over matrix addition, thereby maintaining compatibility with gradient-based optimization and compositional transformations. From an optimization perspective, a single gradient update step yields the following parameter changes:


## jan29_systemfour_settings

Explicit Multi-head Attention for Inter-head Interaction in Large Language Models (https://arxiv.org/html/2601.19611v1)
citeturn28518view1 [wordlim: 200] Crawled: today; Content type: text/html; Source: open({"ref_id":"https://arxiv.org/html/2601.19611v1","lineno":216}); Total lines: 440
L213: In contrast, MEA effectively mitigates the convergence slowdown typically introduced by GroupNorm, ultimately achieving the best overall performance. These observations are further supported by the downstream evaluation results reported in Table cite65†1 . Notably, the MEA variant without GroupNorm (i.e., the modified version of THA) still exhibits behavior nearly identical to the baseline Transformer, and is thus omitted from the plots and tabular for clarity.
L214: Datasets  | PIQA  | OBQA  | WinoGrande  | HellaSwag  | ARC-e  | ARC-c  | Avg.
L215: --- | --- | --- | --- | --- | --- | --- | ---
L216: Transformer  | 71.93  | 21.00  | 56.04  | 40.62  | 59.51  | 26.19  | 45.88
L217: +GroupNorm  | 71.38  | 21.00  | 56.12  | 40.59  | 59.13  | 25.77  | 45.67
L218: +DFA  | 71.76  | 22.20  | 54.38  | 41.29  | 60.69  | 27.82  | 46.36
L219: Ours  | 73.18  | 19.80  | 54.14  | 42.02  | 61.57  | 27.65  | 46.39
L220: Table 1: Performance (Accuracy %) on standard NLP benchmarks. Bold indicates the best result under the same training configuration.
L221: ### 5.2 Compressing Key-Value Cache for Efficient Continued Pretraining
L222: Key-Value cache has long been considered a major bottleneck in the inference stage of LLMs, especially when processing long sequences. In standard autoregressive generation, the attention module of each Transformer layer caches the key and value states computed from all past tokens for use in subsequent causal attention computations.
L223: While this mechanism significantly improves inference efficiency, it incurs a memory cost that grows linearly with sequence length $T$ and is further scaled by the number of layers $L$, attention heads $H$, and head dimension $d_{k}$. Specifically, the space complexity of the KV cache is $\mathcal{O}(LHTd_{k}),$ posing a substantial demand on memory and becoming a central bottleneck for long-context tasks.
L224: To alleviate this issue, we propose a KV cache compression scheme for the inference stage, inspired by the MEA design. Drawing further inspiration from recent work on SVD-based weight compression [cite66†18 ], we apply low-rank approximations to the key and value projection matrices, ${\bm{W}}^{\text{K}}$ and ${\bm{W}}^{\text{V}}$, yielding the decomposed MEA weight matrices:


## jan29_systemfour_set2

Explicit Multi-head Attention for Inter-head Interaction in Large Language Models (https://arxiv.org/html/2601.19611v1)
citeturn28519view0 [wordlim: 200] Crawled: today; Content type: text/html; Source: open({"ref_id":"https://arxiv.org/html/2601.19611v1","lineno":195}); Total lines: 440
L181:  |  | $\displaystyle\approx{\bm{W}}_{\text{lc},t}^{\text{T}}\otimes{\bm{W}}_{\text{comp},t}+(\Delta{\bm{W}}_{\text{lc},t}^{\text{T}}\otimes{\bm{W}}_{\text{comp},t}+{\bm{W}}_{\text{lc},t}^{\text{T}}\otimes\Delta{\bm{W}}_{\text{comp},t})$  |  | (21)
L182:  |  | $\displaystyle=\widetilde{{\bm{W}}}^{\text{T}}_{t}+\Delta\widetilde{{\bm{W}}}^{\text{T}}_{t},$  |  | (22)
L183: in the above approximation, we ignore the higher-order interaction term $\text{HLC}(\Delta{\bm{W}}_{\text{lc},t}^{\text{T}},\Delta{\bm{W}}_{\text{comp},t})$ under the standard assumption of applying gradient descent in deep learning, where parameter updates are sufficiently small in each step. Consequently, in the absence of non-linear operations—such as GroupNorm—the model is prone to degenerating into standard attention.
L184: To address this, MEA incorporates Group Normalization inspired by the Differential Transformer, which not only stabilizes training but also helps maintain the expressive cross-head interactions in MEA.
L185: ## 5 Experiments
L186: 
L187: ### 5.1 From Scratch Pre-training
L188: 
L189: #### 5.1.1 Settings
L190: ##### Model
L191: Our pretraining experiments adopt a model architecture identical to LLaMA3.2-1B [cite58†16 ], except that we do not employ weight tying between the input embedding layer and the output language modeling head.
L192: Building upon this base architecture, we explore several attention variants: the original Transformer; a Transformer with GroupNorm applied to head outputs; a MEA variant without GroupNorm (equivalent to the modified THA); the Differential Transformer [cite43†34 ]; and our proposed Transformer equipped with Multihead Explicit Attention (MEA).
L193: ##### Training Settings
L194: 
L195: We train all models using the AdamW optimizer [cite59†14 ] with a weight decay coefficient of $0.1$. The learning rate is annealed to $10\%$ of its initial value using a cosine decay schedule, which promotes smoother convergence in the later stages of training. The default batch size is 20 million tokens, and each model is trained on a total of 500 billion tokens. We follow standard pretraining practices with a curated mixture of text corpora (see Appendix cite31†C for details).
L196: #### 5.1.2 Cost-Efficient Hyperparameter Selection
L197: Established work has shown that increasing network depth often requires proportionally larger learning rates and batch sizes to effectively benefit model performance [cite60†7 , cite61†31 ]. However, such configurations may also introduce challenges in training stability. Recent studies further suggest that different model architectures demand distinct hyperparameter settings—particularly with respect to learning rate—to achieve optimal training dynamics [cite62†20 ].
L198: Consistent with these findings, we observe that Transformer variants exhibit varying sensitivities to the learning rate, even when the model size is held constant, as we will discuss later in this section.
L199: 
L200: Although current pretraining practices often employ relatively small peak learning rates (e.g., $4\times 10^{-4}$ or $1.5\times 10^{-4}$) for billion-scale models [cite63†29 , cite43†34 ], our results indicate that such choices may not be universally optimal across architectures.
L201: In our experiments, we find that the best-performing learning rate for each variant corresponds to the largest value that avoids unstable behavior such as loss spikes—sharp, unrecoverable increases in loss during training. Models trained under these maximal stable learning rates consistently achieve the most effective reduction in loss on held-out test sets. For further details, please refer to Appendix cite35†E .
L202: This observation highlights the necessity for architecture-specific learning rate tuning. However, performing full-scale training for each candidate learning rate is computationally prohibitive. To address this challenge, we adopt the concept of scaling laws, which fit a power-law relationship between the loss and the number of training tokens. This allows us to estimate the asymptotic performance of each setting from short-run training trajectories. Further details are provided in Appendix cite34†D .
L203: This approach enables efficient learning rate selection using only a small fraction of the full pretraining budget.
L204: To this end, we perform a systematic grid search over learning rates for all Transformer variants evaluated in this study. Each variant is trained on 50 billion tokens using four candidate learning rates: $1\times 10^{-4}$, $5\times 10^{-4}$, $1\times 10^{-3}$, and $3\times 10^{-3}$. We adopt a linear warmup strategy over the first 1000 training steps, followed by standard training with fixed learning rate. All other hyperparameters are kept consistent with the full-scale pretraining configuration.
L205: As shown in Figure cite64†3 , MEA consistently achieves lower validation loss under the same learning rate ($1\times 10^{-3}$) compared to other variants. Moreover, experimental results in Appendix cite35†E indicate that MEA-based Transformers maintain stable training behavior at peak learning rates up to $3\times 10^{-3}$, while other variants become unstable beyond $1\times 10^{-3}$.
L206: Figure 2: Test loss curves fitted using scaling laws in the learning rate selection experiment, under fixed learning rates $1\times 10^{-3}$ for different attention variants.
L207: 
L208: Figure 3: Test loss curves fitted using scaling laws in the full-scale pretraining setting, using cosine decay schedules initialized from the optimal fixed learning rates in Figure cite64†3 , comparing different model variants.
L209: #### 5.1.3 From Scratch Pretraining Experiments
L210: Building upon the learning rate selection experiments, we identified the maximum stable learning rate for each model variant and adopted a cosine annealing scheduler for full-scale training. We retain 1000 steps for optimizer warm-up.


## jan29_systemfour_set2

Explicit Multi-head Attention for Inter-head Interaction in Large Language Models (https://arxiv.org/html/2601.19611v1)
citeturn28519view1 [wordlim: 200] Crawled: today; Content type: text/html; Source: open({"ref_id":"https://arxiv.org/html/2601.19611v1","lineno":227}); Total lines: 440
L222: Key-Value cache has long been considered a major bottleneck in the inference stage of LLMs, especially when processing long sequences. In standard autoregressive generation, the attention module of each Transformer layer caches the key and value states computed from all past tokens for use in subsequent causal attention computations.
L223: While this mechanism significantly improves inference efficiency, it incurs a memory cost that grows linearly with sequence length $T$ and is further scaled by the number of layers $L$, attention heads $H$, and head dimension $d_{k}$. Specifically, the space complexity of the KV cache is $\mathcal{O}(LHTd_{k}),$ posing a substantial demand on memory and becoming a central bottleneck for long-context tasks.
L224: To alleviate this issue, we propose a KV cache compression scheme for the inference stage, inspired by the MEA design. Drawing further inspiration from recent work on SVD-based weight compression [cite66†18 ], we apply low-rank approximations to the key and value projection matrices, ${\bm{W}}^{\text{K}}$ and ${\bm{W}}^{\text{V}}$, yielding the decomposed MEA weight matrices:
L225:  | $${\bm{W}}^{\text{K}}\approx\widetilde{{\bm{W}}}^{\text{K}^{\prime}}\otimes\widetilde{{\bm{W}}}_{\text{lc}}^{\text{K}},\quad{\bm{W}}^{\text{V}}\approx\widetilde{{\bm{W}}}^{\text{V}^{\prime}}\otimes\widetilde{{\bm{W}}}_{\text{lc}}^{\text{V}},$$  |  | (23)
L226: where $\widetilde{{\bm{W}}}^{\text{K}^{\prime}},\widetilde{{\bm{W}}}_{\text{lc}}^{\text{K}},\widetilde{{\bm{W}}}^{\text{V}^{\prime}},\widetilde{{\bm{W}}}_{\text{lc}}^{\text{V}}$ represent the compressed basis and reconstruction matrices for the key and value weights, respectively. Here, the operator $\otimes$ represents a head-wise recombination operation mentioned in equation cite67†18 .
L227: These matrices are used to approximate the original multi-head representations using fewer virtual heads, thereby reducing KV cache memory without modifying the model’s forward computation. Please refer to Appendix cite36†F for detailed derivations of this approximation scheme.
L228: #### 5.2.1 Settings
L229: ##### Model
L230: We conduct continued pretraining experiments based on the Qwen3-30B-A3B model [cite68†28 ]. To evaluate the effectiveness of our low-rank approximation strategy described in equation cite69†23 , we consider three key-value memory compression configurations with varying granularity. In the full-layer compression setting, all Transformer layers adopt MEA-based KV compression.
L231: In the half-layer compression setting, only layers 12 through 35 (out of 48 in total) are compressed; these layers are selected based on loss sensitivity profiling results detailed in Appendix cite36†F , targeting those with minimal impact on validation loss under compression. In the deep-layer compression setting, only the first 3 layers remain uncompressed, while all remaining layers apply MEA-based KV compression.
L232: In all compression settings, the number of key-value heads in the compressed layers is reduced from 4 to 2. For comparison, we also include a full-parameter continued pretraining variant without any KV compression as a reference baseline.
L233: ##### Training settings
L234: 
L235: All models are trained for one epoch using the AdamW optimizer with a peak learning rate of $1.6\times 10^{-5}$ and a linear warmup over the first 1000 steps. The batch size is set to 68 million tokens. The learning rate is scheduled via cosine annealing to 0 throughout training, similar with our main pretraining configuration. We follow standard pretraining practices with a curated mixture of text corpora (see Appendix cite31†C for details).
L236: #### 5.2.2 Analysis
L237:  | Know. Avg.  | Sci. Avg.  | Math Avg.  | Total Avg.
L238: Qwen3-30B-A3B  | 63.82  | 48.39  | 65.12  | 58.68
L239: +CPT  | 65.81  | 49.76  | 50.48  | 54.39
L240: Half Compression + CPT  | 63.54 (-2.27)  | 49.44 (-0.32)  | 48.49 (-1.99)  | 52.94 (-1.45)
L241: Deep Compression + CPT  | 61.91 (-3.90)  | 48.27 (-1.49)  | 46.13 (-4.35)  | 51.21 (-3.18)
L242: Full Compression + CPT  | 61.25 (-4.56)  | 42.07 (-7.69)  | 43.68 (-6.80)  | 47.89 (-6.50)
L243: Full Compression + Recov. + CPT  | 64.41 (-1.40)  | 48.79 (-0.97)  | 46.89 (-3.59)  | 52.36 (-2.03)
L244: Table 2: Performance (Acc%) on complex reasoning benchmarks. All results are compared against the full-parameter CPT baseline (+CPT), with relative deltas shown in parentheses (smaller is better).
L245: To assess the impact of memory compression on complex reasoning, we evaluate all models on a suite of challenging benchmarks supported by OpenCompass. These tasks span diverse reasoning categories: MMLU-Pro [cite70†11 ], GPQA Diamond [cite71†21 ], and SuperGPQA [cite72†13 ] for knowledge reasoning; ChemBench [cite73†2 ], ClimaQA [cite74†33 ], and MedXpertQA [cite75†32 ] for scientific reasoning; and AIME 2025 [cite76†4 ], OlympiadBench [cite77†12 ], LiveMathBench-Hard [cite78†27 ], and OlymMATH [cite79†26 ] for mathematical reasoning.
L246: The summarized results are presented in Table cite80†2 , and a detailed breakdown of sub-task scores is provided in Appendix cite37†G .
L247: Experimental results show that even under full compression, the model can recover to a competitive performance level when continued pretraining (CPT) is combined with an additional recovery stage. Furthermore, knowledge and science reasoning tasks appear relatively robust to this form of memory compression, with minimal performance degradation.
L248: In contrast, mathematical reasoning is more sensitive: even the full-parameter CPT baseline exhibits a noticeable performance drop, likely due to differences in data quality compared to the original Qwen3 pretraining. Nevertheless, our fully compressed variant with Recover+CPT manages to regain acceptable performance across most math tasks.
L249: We believe this performance gap could be further narrowed with improved training data, especially considering that the full-parameter CPT setting also suffers a significant drop in math reasoning.


## jan29_systemfour_last

Explicit Multi-head Attention for Inter-head Interaction in Large Language Models (https://arxiv.org/html/2601.19611v1)
citeturn28521view0 [wordlim: 200] Crawled: today; Content type: text/html; Source: open({"ref_id":"https://arxiv.org/html/2601.19611v1","lineno":385}); Total lines: 440
L262: Zhao, Y. Sun, Y. Li, Y. Wang, Y. Zheng, Y. Zhang, Y. Xiong, Y. Zhao, Y. He, Y. Tang, Y. Piao, Y. Dong, Y. Tan, Y. Liu, Y. Wang, Y. Guo, Y. Zhu, Y. Wang, Y. Zou, Y. Zha, Y. Ma, Y. Yan, Y. You, Y. Liu, Z. Z. Ren, Z. Ren, Z. Sha, Z. Fu, Z. Huang, Z. Zhang, Z. Xie, Z. Hao, Z. Shao, Z. Wen, Z. Xu, Z. Zhang, Z. Li, Z. Wang, Z. Gu, Z. Li, and Z. Xie (2024) DeepSeek-v2: a strong, economical, and efficient mixture-of-experts language model. External Links: 2405.04434, cite89†Link Cited by: cite82†§1 , cite90†§4.1 .
L263:   * [7] F. D’Angelo, M. Andriushchenko, A. V. Varre, and N. Flammarion (2024) Why do we need weight decay in modern deep learning?. Advances in Neural Information Processing Systems 37, pp. 23191–23223. Cited by: cite91†§5.1.2 .
L264:   * [8] J. Kaplan, S. McCandlish, T. Henighan, T. B. Brown, B. Chess, R. Child, S. Gray, A. Radford, J. Wu, and D. Amodei (2020) Scaling Laws for Neural Language Models. arXiv preprint arXiv:2001.08361. Cited by: cite92†Appendix D .
L265:   * [9] D. Kocetkov, L. Ben Allal, N. Muennighoff, et al. (2023) The stack: permissively licensed github code dataset. Note: cite93†https://huggingface.co/datasets/bigcode/the-stack†huggingface.co Accessed: 2025-09-05 Cited by: cite94†Appendix C .
L266:   * [10] R. Li, L. Ben Allal, Y. Zi, N. Muennighoff, D. Kocetkov, C. Mou, M. Marone, C. Akiki, J. Li, J. Chim, Q. Liu, E. Zheltonozhskii, et al. (2023) StarCoder: may the source be with you!. arXiv preprint arXiv:2305.06161. External Links: 2305.06161 Cited by: cite94†Appendix C .
L267:   * [11] N. F. Liu et al. (2024) MMLU-pro: a more robust multi-task language understanding benchmark. arXiv preprint arXiv:2406.01574. Cited by: cite84†§5.2.2 .
L268:   * [12] X. Liu et al. (2024) OlympiadBench: a benchmark for ai mathematical olympiad problems. arXiv preprint arXiv:2404.07762. Cited by: cite84†§5.2.2 .
L269:   * [13] X. Liu et al. (2024) SuperGPQA: a challenging benchmark for evaluating large language models on multi-disciplinary expert-level question answering. arXiv preprint arXiv:2408.15577. Cited by: cite84†§5.2.2 .
L270:   * [14] I. Loshchilov and F. Hutter (2019) Decoupled Weight Decay Regularization. In Proceedings of the International Conference on Learning Representations, Cited by: cite95†§5.1.1 .
L271:   * [15] A. Lozhkov, L. Ben Allal, L. von Werra, and T. Wolf (2024) FineWeb-edu: the finest collection of educational content. arXiv preprint arXiv:2406.17557. External Links: 2406.17557 Cited by: cite94†Appendix C .
L272:   * [16] Meta (2025) Llama 3.2–1b. Note: cite96†https://huggingface.co/meta-llama/Llama-3.2-1B†huggingface.co Accessed: 2025-09-05 Cited by: cite97†§5.1.1 .
L273:   * [17] G. Penedo, Q. Malartic, D. Hesslow, R. Cojocaru, H. Alobeidli, A. Cappelli, B. Pannier, E. Almazrouei, and J. Launay (2023) The refinedweb dataset for falcon llm: outperforming curated corpora with web data, and web data only. In Advances in Neural Information Processing Systems (NeurIPS), Cited by: cite94†Appendix C .
L274:   * [18] R. Peng, Y. Zhou, Q. Guo, Y. Gao, H. Yan, X. Qiu, and D. Lin (2025) Data-free weight compress and denoise for large language models. External Links: 2402.16319, cite98†Link Cited by: cite99†§5.2 .
L275:   * [19] J. Qiu, H. Lv, Z. Jin, R. Wang, W. Ning, J. Yu, C. Zhang, Z. Li, P. Chu, Y. Qu, J. Shi, L. Lu, R. Peng, Z. Zeng, H. Tang, Z. Lei, J. Hong, K. Chen, Z. Fei, R. Xu, W. Li, Z. Tu, L. Dahua, Y. Qiao, H. Yan, and C. He (2024) WanJuan-CC: a safe and high-quality open-sourced english webtext dataset. arXiv preprint arXiv:2402.19282. Cited by: cite94†Appendix C , cite100†Appendix C .
L276:   * [20] Z. Qiu, Z. Wang, B. Zheng, Z. Huang, K. Wen, S. Yang, R. Men, L. Yu, F. Huang, S. Huang, D. Liu, J. Zhou, and J. Lin (2025) Gated attention for large language models: non-linearity, sparsity, and attention-sink-free. External Links: 2505.06708, cite101†Link Cited by: cite91†§5.1.2 .
L277:   * [21] D. Rein et al. (2023) GPQA: a graduate-level google-proof q&a benchmark. arXiv preprint arXiv:2311.12022. Cited by: cite84†§5.2.2 .
L278:   * [22] N. Shazeer, Z. Lan, Y. Cheng, N. Ding, and L. Hou (2020) Talking-heads attention. arXiv preprint arXiv:2003.02436. Cited by: cite82†§1 , cite102†§3.2 , cite103†§4.3 .
L279:   * [23] N. Shazeer (2019) Fast transformer decoding: one write-head is all you need. External Links: 1911.02150, cite104†Link Cited by: cite82†§1 , cite83†§2 .
L280:   * [24] N. Shazeer (2020) Glu variants improve transformer. arXiv preprint arXiv:2002.05202. External Links: cite105†Link Cited by: cite106†§2 .
L281:   * [25] J. Su, Y. Lu, S. Pan, A. Murtadha, B. Wen, and Y. Liu (2023) RoFormer: enhanced transformer with rotary position embedding. External Links: 2104.09864, cite107†Link Cited by: cite108†§2 , cite109†§4.3 .
L282:   * [26] H. Sun, Y. Min, Z. Chen, W. X. Zhao, L. Fang, Z. Liu, Z. Wang, and J. Wen (2025) Challenging the boundaries of reasoning: an olympiad-level math benchmark for large language models. External Links: 2503.21380, cite110†Link Cited by: cite84†§5.2.2 .
L283:   * [27] T. Sun et al. (2024) LiveMathBench: a continuously updated benchmark for evaluating mathematical reasoning of llms. arXiv preprint arXiv:2412.04468. Cited by: cite84†§5.2.2 .
L284:   * [28] Q. Team (2025) Qwen3 technical report. External Links: 2505.09388, cite111†Link Cited by: cite112†§5.2.1 .
L285:   * [29] J. Tow, M. Bellagente, D. Mahan, and C. Riquelme (2023) StableLM 3b 4e1t. External Links: Link Cited by: cite113†§5.1.2 .
L286:   * [30] A. Vaswani, N. Shazeer, N. Parmar, J. Uszkoreit, L. Jones, A. N. Gomez, L. Kaiser, and I. Polosukhin (2023) Attention is all you need. External Links: 1706.03762, cite114†Link Cited by: cite82†§1 , cite83†§2 .
L287:   * [31] H. Wang, S. Ma, L. Dong, S. Huang, D. Zhang, and F. Wei (2022) DeepNet: scaling transformers to 1,000 layers. External Links: 2203.00555, cite115†Link Cited by: cite91†§5.1.2 .
L288:   * [32] Y. Wang et al. (2024) MedXpertQA: benchmarking medical expert-level question answering with multi-modal context. arXiv preprint arXiv:2411.05298. Cited by: cite84†§5.2.2 .
L289:   * [33] J. Wei et al. (2024) ClimaQA: a benchmark for evaluating large language models on climate science. arXiv preprint arXiv:2407.05595. Cited by: cite84†§5.2.2 .
L290:   * [34] T. Ye, L. Dong, Y. Xia, Y. Sun, Y. Zhu, G. Huang, and F. Wei (2025) Differential transformer. External Links: 2410.05258, cite116†Link Cited by: cite117†Appendix A , cite82†§1 , cite118†§1 , cite119†§3.1 , cite120†§3.1 , cite97†§5.1.1 , cite113†§5.1.2 .
L291:   * [35] B. Zhang and R. Sennrich (2019) Root mean square layer normalization. Advances in Neural Information Processing Systems 32. External Links: cite121†Link Cited by: cite106†§2 .
L292:   * [36] Y. Zhang, Y. Liu, H. Yuan, Z. Qin, Y. Yuan, Q. Gu, and A. C. Yao (2025) Tensor product attention is all you need. External Links: 2501.06425, cite122†Link Cited by: cite90†§4.1 .
L293: ## Appendix A DFA without GroupNorm
L294: 
L295: In Section cite9†3.1 , we discussed that DFA without GroupNorm can be viewed as a special case of Talking-Heads Attention (THA) that only applies post-softmax transformations. While this connection may not be immediately obvious, we provide further clarification below.
L296: By removing GroupNorm, we effectively eliminate the rescaling factor $1-\lambda_{\text{init}}$ associated with the normalization term [cite43†34 ]. Consequently, DFA degenerates into a form where attention outputs are modified exclusively through post-softmax head mixing—precisely aligning with the structure of THA that operates only on attention weights after softmax:
L297:  | $\displaystyle\mathbf{A}_{i}$  | $\displaystyle=\text{softmax}\left(\frac{\phi(\mathbf{Q}_{2i-1})\phi(\mathbf{K}_{2i-1})^{\top}}{\sqrt{d_{qk}}}\right)-\lambda_{i}\cdot\text{softmax}\left(\frac{\phi(\mathbf{Q}_{2i})\phi(\mathbf{K}_{2i})^{\top}}{\sqrt{d_{qk}}}\right),$  |  | (24)
L298:  | $\displaystyle\mathbf{C}_{i}$  | $\displaystyle=\mathbf{A}_{i}\cdot\text{Concat}\left(\mathbf{V}_{2i-1},\mathbf{V}_{2i}\right),$  |  | (25)
L299:  | $\displaystyle\text{DFA}(\mathbf{X})$  | $\displaystyle=\text{Concat}\left(\mathbf{C}_{1},\dots,\mathbf{C}_{\frac{h}{2}}\right){\bm{W}}^{\text{O}},$  |  | (26)
L300: In this setting, we can construct an equivalent THA-style transformation matrix:
L301: 
L302:  | $$T^{\text{V}}_{i,j}=\begin{cases}1,&i\in\{2d-1,2d\},\ j=2d-1,\\
L303: -\lambda,&i\in\{2d-1,2d\},\ j=2d,\\
L304: 0,&\text{otherwise},\end{cases}$$  |  | (27)
L305: 
L306: where $d\in\mathbb{Z}_{[\frac{h}{2}]}$ denotes the $d$-th head pair in DFA.
L307: 
L308: Thus, it becomes evident that DFA without GroupNorm is essentially a special case of THA that only applies a post-softmax combination of attention heads.
L309: ## Appendix B Modification on Post-Softmax Mixing of THA
L310: 
L311: In Section cite14†4.3 , we move the linear transferring module from acting on the attention scores to acting after the value combination ${\bm{\mathsfit{V}}}$. In this section, we examine whether there exists any difference in representational capacity between these two formulations.
L312: 
L313: The original THA formulation computes:
L314:  | $${\bm{\mathsfit{C}}}^{\prime}_{i}=\sum_{j}{\bm{T}}^{\text{V}}_{G(i),G(j)}\cdot{\bm{\mathsfit{A}}}_{j}\cdot{\bm{\mathsfit{V}}}_{G(i)}$$  |  | (28)
L315: 
L316: In the modified version:
L317: 
L318:  | $${\bm{\mathsfit{C}}}^{\prime}_{i}={\bm{\mathsfit{A}}}_{i}\cdot\sum_{j}{\bm{T}}^{\text{V}}_{G(i),G(j)}\cdot{\bm{\mathsfit{V}}}_{G(j)}$$  |  | (29)
L319: 
L320: The final attention output is then:
L321:  | $$\text{THA}(\mathbf{X})=\text{Concat}({\bm{\mathsfit{C}}}^{\prime}_{1},\ldots,{\bm{\mathsfit{C}}}^{\prime}_{h}){\bm{W}}^{\text{O}}$$  |  | (30)
L322: 
L323: To analyze the difference, consider the output of the attention layer ${\bm{\mathsfit{Y}}}=\text{THA}({\bm{\mathsfit{X}}})$ at position $p$, denoted as ${\bm{y}}={\bm{\mathsfit{Y}}}[p]$. We examine the value of a single channel $ch$, written as $y={\bm{y}}[ch]$. Expanding the linear projection:
L324:  | $$y=\sum_{i}\sum_{k}{\bm{c}}^{\prime}_{i}[k]\cdot{\bm{W}}^{\text{O}}[i\cdot\text{head\_dim}+k,ch]=\sum_{i}\sum_{k}{\bm{c}}^{\prime}_{i}[k]\cdot w_{i,k}$$  |  | (31)
L325: 
L326: where $w_{i,k}:={\bm{W}}^{\text{O}}[i\cdot\text{head\_dim}+k,ch]$ is the scalar weight applied to the $k$-th dimension of the $i$-th head output when computing the $ch$-th output channel.
L327: 
L328: Under the original THA formulation:
L329:  | $$y_{\text{THA}}=\sum_{i,j,k}{\bm{T}}^{\text{V}}_{G(i),G(j)}\cdot{\bm{a}}_{j}\cdot{\bm{\mathsfit{V}}}_{G(i)}[k]\cdot w_{i,k}$$  |  | (32)
L330: 
L331: where ${\bm{a}}_{j}={\bm{\mathsfit{A}}}_{j}[p]$ denotes the attention score (typically from softmax) for position $p$ to query on keys from position $[1,\cdots,p]$, and ${\bm{\mathsfit{V}}}_{G(i)}[k]$ denotes the $k$-th component of the value vectors from head $G(i)$.
L332: 
L333: Under the modified formulation:
L334:  | $$y_{\text{THA}^{\prime}}=\sum_{i,j,k}{\bm{a}}_{i}\cdot{\bm{T}}^{\text{V}}_{G(i),G(j)}\cdot{\bm{\mathsfit{V}}}_{G(j)}[k]\cdot w_{i,k}$$  |  | (33)
L335: 
L336: where ${\bm{a}}_{i}={\bm{\mathsfit{A}}}_{i}[p]$ denotes the scalar attention score (typically from softmax) for position $p$, and ${\bm{\mathsfit{V}}}_{G(i)}[k]$ denotes the $k$-th component of the value vectors from head $G(i)$.
L337: From an optimization and representational perspective, these two forms are equivalent in expressive power: the change in summation order can be compensated by adjustments in the learnable transfer matrix ${\bm{T}}^{\text{V}}$ and the output projection ${\bm{W}}^{\text{O}}$. Therefore, both variants are expected to converge to similarly expressive solutions (having same weights) during training.
L338: ## Appendix C Training Data
L339: ##### From Scratch Pre-training
L340: We construct pre-training corpus by extending several publicly available datasets, including Common Crawl, FineWeb-Edu [cite123†15 ], RefinedWeb [cite124†17 ], StarCoder [cite125†10 ], and the Stack [cite126†9 ]. Additionally, we collect supplementary text data from the open web to further improve the diversity of the training set.
L341: Following prior practices [cite127†19 ], we apply a five-stage preprocessing pipeline comprising: (1) language identification and text extraction, (2) heuristic rule-based cleaning, (3) fuzzy deduplication, (4) safety filtering, and (5) quality-based data selection. The validation set is selected from Pile-CC, with the objective of aligning test loss behavior with the relative performance rankings observed on downstream tasks.
L342: ##### Compressing Key-Value Cache for Efficient Continued Pretraining
L343: 
L344: The dataset used for continued pretraining is the same as described above. For the full-layer compression setting, we include an additional stage of 1T-token pretraining to recover distributional alignment. For all other settings, training is conducted on a high-quality filtered subset of the original corpus, selected based on data quality scores [cite127†19 ]. This high-quality dataset contains approximately 22 billion tokens.
L345: ## Appendix D Scaling Laws
L346: 
L347: Researchers at OpenAI have shown that during model training, the test loss exhibits a predictable power-law relationship with respect to model size and the amount of training data [cite128†8 ]. The most general form of this empirical law can be expressed as:
L348: 
L349:  | $$L(N,D)=\left[\left(\frac{N_{c}}{N}\right)^{\frac{\alpha_{N}}{\alpha_{D}}}+\frac{D_{c}}{D}\right]^{\alpha_{D}},$$  |  | (34)
L350: where $L(N,D)$ estimates the test loss given model size $N$ (excluding embeddings) and number of training tokens $D$. The constants $N_{c}$, $D_{c}$, $\alpha_{N}$, and $\alpha_{D}$ depend on the model architecture, dataset, and evaluation distribution, and are typically estimated via curve fitting.
L351: For a fixed model architecture (i.e., fixed $N$), the above formulation simplifies to a function of data scaling only. By performing a Taylor expansion and omitting lower-order terms, a more practical form is commonly used:
L352: 
L353:  | $$L(D)=\left(\frac{D_{c}}{D}\right)^{\alpha_{D}}+L_{0},$$  |  | (35)
L354: where $L_{0}$ denotes the irreducible loss floor after convergence, and $D_{c}$, $\alpha_{D}$ are task- and model-dependent constants. Unless otherwise specified, all references to "scaling laws" in this paper refer to the simplified formulation in Equation cite129†35 .
L355: ## Appendix E Learning Rate Selection
L356: 
L357: Figure 4: Test loss curves fitted using scaling laws in the learning rate selection experiment, under different fixed learning rates for Transformer.
L358: 
L359: Figure 5: Test loss curves fitted using scaling laws in the learning rate selection experiment, under different fixed learning rates for Transformer+GroupNorm.
L360: 
L361: Figure 6: Test loss curves fitted using scaling laws in the learning rate selection experiment, under different fixed learning rates for Transformer+DFA.
L362: Figure 7: Test loss curves fitted using scaling laws in the learning rate selection experiment, under different fixed learning rates for Transformer+MEA.
L363: For the $1\times 10^{-4}$ learning rate setting, we observe abnormal fitting behavior in Figure cite130†5 and Figure cite131†7 , where the empirical loss curve significantly deviates from the expected trend modeled by the scaling law formulation. This is likely due to insufficient training signal under such a small learning rate. While the fit remains formally feasible, the trend is substantially slower than other configurations, making it unlikely to catch up within the 25,000-step training budget.
L364: ## Appendix F MEA-Based Derivation for Key-Value Compression
L365: 
L366: Figure 8: Cross-entropy loss changes when compressing different layers of the key-value cache. The x-axis denotes the index of the compressed layer (ordered from embedding-side to LM head, ranging from 1 to 48), and the y-axis shows the cross-entropy loss measured on a Pile-CC validation subset.
L367: Our compression method is grounded in the observation that considerable redundancy exists among attention heads during generation, particularly in large language models (LLMs). Many heads produce similar representations or exhibit diminished functional diversity.
L368: Exploiting this, we apply Singular Value Decomposition (SVD) and low-rank approximation to project the multi-head key and value representations of each token into a more compact subspace—effectively reducing the number of heads that must be cached.
L369: Specifically, MEA introduces a linear combination matrix to approximate multiple attention heads using a smaller number of “virtual heads.” Consider the key projection matrix ${\bm{W}}^{\text{K}}\in\mathbb{R}^{\text{Dim}\times(H\cdot d_{k})}$, where Dim is the input embedding dimension and $d_{k}=\text{Dim}/H$ is the per-head dimensionality. We reshape this matrix as follows:
L370: 
L371:  | $${\bm{W}}^{\text{K}}\in\mathbb{R}^{(d_{k}\cdot\text{Dim})\times H},$$  |  | (36)
L372: where each column corresponds to a flattened projection for a single head. Applying SVD yields:
L373: 
L374:  | $${\bm{W}}^{\text{K}}={\bm{W}}^{\text{K}^{\prime}}\cdot\Lambda\cdot{\bm{W}}_{\text{lc}}^{\text{K}},$$  |  | (37)
L375: 
L376: where:
L377: 
L378:   * •
L379: 
L380: ${\bm{W}}^{\text{K}^{\prime}}\in\mathbb{R}^{(d_{k}\cdot\text{Dim})\times H^{\prime}}$ contains the left singular vectors (basis);
L381: 
L382:   * •
L383: 
L384: $\Lambda\in\mathbb{R}^{H^{\prime}\times H^{\prime}}$ is a diagonal matrix of singular values;
L385: 
L386:   * •
L387: ${\bm{W}}_{\text{lc}}^{\text{K}}\in\mathbb{R}^{H^{\prime}\times H}$ is the linear combination matrix.
L388: 
L389: In typical settings where $\text{Dim}\gg H$, the decomposition is full-rank. By retaining only the top-$H^{\prime}$ singular values and incorporating $\Lambda$ into ${\bm{W}}_{\text{lc}}^{\text{K}}$, we obtain the low-rank approximation:
L390: 
L391:  | $${\bm{W}}^{\text{K}}\approx\widetilde{{\bm{W}}}^{\text{K}^{\prime}}\otimes\widetilde{{\bm{W}}}_{\text{lc}}^{\text{K}},$$  |  | (38)
L392: where both $\widetilde{{\bm{W}}}^{\text{K}^{\prime}}$ and $\widetilde{{\bm{W}}}_{\text{lc}}^{\text{K}}$ are significantly smaller than the original matrix. Here, the operator $\otimes$ represents a head-wise recombination operation mentioned in equation cite67†18 .
L393: This procedure can be similarly applied to the value projection matrix ${\bm{W}}^{\text{V}}$, enabling compression of both key and value components in the attention cache. Crucially, this approximation leaves the model’s original parameters untouched and can be deployed purely at inference time via lightweight linear mappings, offering strong deployment compatibility and minimal computational overhead.
L394: To design layer-wise key-value cache compression strategies, we first perform a layer selection study on the Pile-CC validation set. Specifically, we apply head compression to one layer at a time and record the resulting cross-entropy loss, as illustrated in Figure cite132†8 . The x-axis represents the index of the compressed layer, while the y-axis shows the corresponding cross-entropy loss measured on a subset of Pile-CC. This probing experiment guides the design of our partial-layer compression strategies.
L395: The compression method follows the formulation in equation cite69†23 . Notably, we observe that compressing the middle layers yields negligible degradation in validation loss compared to compressing early or late layers. Based on these findings, we select layers 12 through 35 (hf model index 11–34) for the half-layer compression configuration in our continued pretraining experiments.
L396: ## Appendix G Downstream Task Score for CPT
L397: 
L398:  | MMLU-Pro  | GPQA Diamond  | SuperGPQA  | Know. Avg.
L399: Qwen3-30B-A3B  | 77.52  | 61.62  | 52.32  | 63.82
L400: +CPT  | 80.71  | 64.65  | 52.08  | 65.81
L401: Half Compression+CPT  | 77.77  | 63.13  | 49.73  | 63.54
L402: Deep Compression+CPT  | 77.10  | 61.87  | 46.75  | 61.91
L403: Full Compression+CPT  | 77.28  | 60.10  | 46.36  | 61.25
L404: Full Compression+Recov.+CPT  | 78.28  | 66.16  | 48.79  | 64.41
L405: 
L406: Table 3: Performance (Acc%) on knowledge reasoning benchmarks.
L407:  | PHYSICS  | ChemBench  | ClimaQA  | MedXpertQA  | Sci. Avg.
L408: Qwen3-30B-A3B  | 37.74  | 66.12  | 64.79  | 24.90  | 48.39
L409: +CPT  | 36.56  | 70.02  | 65.36  | 27.10  | 49.76
L410: Half Compression+CPT  | 37.18  | 71.74  | 63.42  | 25.43  | 49.44
L411: Deep Compression+CPT  | 34.67  | 69.93  | 62.17  | 26.29  | 48.27
L412: Full Compression+CPT  | 32.14  | 54.19  | 59.33  | 22.61  | 42.07
L413: Full Compression+Recov.+CPT  | 35.10  | 72.02  | 63.20  | 24.82  | 48.79
L414: 
L415: Table 4: Performance (Acc%) on scientific reasoning benchmarks.
L416:  | AIME 2025  | OlympiadBench  | LiveMathBench-hard  | OlymMATH  | Math Avg.
L417: Qwen3-30B-A3B  | 80.00  | 73.40  | 55.56  | 51.50  | 65.12
L418: +CPT  | 56.67  | 69.77  | 42.22  | 33.25  | 50.48
L419: Half Compression+CPT  | 46.67  | 66.11  | 46.67  | 34.50  | 48.49
L420: Deep Compression+CPT  | 48.75  | 64.10  | 43.59  | 28.06  | 46.13
L421: Full Compression+CPT  | 40.00  | 64.54  | 44.44  | 25.75  | 43.68
L422: Full Compression+Recov.+CPT  | 46.67  | 66.91  | 42.22  | 31.75  | 46.89
L423: Table 5: Performance (Acc%) on mathematical reasoning benchmarks.
L424: 
L425: Experimental support, please cite133†view the build logs for errors. Generated by cite134†L A T E xml†math.nist.gov .
L426: ## Instructions for reporting errors
L427: 
L428: We are continuing to improve HTML versions of papers, and your feedback helps enhance accessibility and mobile support. To report errors in the HTML that will help us improve conversion and rendering, choose any of the methods listed below:
L429: 
L430:   * Click the "Report Issue" () button, located in the page header.
L431: 
L432: Tip: You can select the relevant text first, to include it in your report.
L433: Our team has already identified cite135†the following issues†github.com . We appreciate your time reviewing and reporting rendering errors we may not have found yet. Your efforts will help us improve the HTML versions for all readers, because disability should not be a barrier to accessing research. Thank you for your continued support in championing open access for all.
L434: Have a free development cycle? Help support accessibility at arXiv! Our collaborators at LaTeXML maintain a cite136†list of packages that need conversion†github.com , and welcome cite137†developer contributions†github.com .
L435: 
L436: We gratefully acknowledge support from our major funders, cite138†member institutions†info.arxiv.org , , and all contributors.
L437: cite139†About†info.arxiv.org · cite140†Help†info.arxiv.org · cite141†Contact†info.arxiv.org · cite142†Subscribe†info.arxiv.org · cite143†Copyright†info.arxiv.org · cite144†Privacy†info.arxiv.org · cite145†Accessibility†info.arxiv.org · cite146†Operational Status (opens in new tab)†status.arxiv.org L438: 
L439: Major funding support from


## jan29_systemfour_last

Explicit Multi-head Attention for Inter-head Interaction in Large Language Models (https://arxiv.org/html/2601.19611v1)
citeturn28521view2 [wordlim: 200] Crawled: today; Content type: text/html; Source: find({"ref_id":"https://arxiv.org/html/2601.19611v1","pattern":"hardware"}); Total lines: 440
No matching text found for "hardware"
