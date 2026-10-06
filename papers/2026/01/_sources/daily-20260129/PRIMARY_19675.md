# Exact-v1 necessary primary — 2601.19675

Original returned context retained; only necessary core, controls, setup and direct counterclaims adopted.

## jan29_systemfour_head

LoPRo: Enhancing Low-Rank Quantization via Permuted Block-Wise Rotation (https://arxiv.org/html/2601.19675v1)
citeturn28514view3 [wordlim: 200] Crawled: today; Content type: text/html; Source: open({"ref_id":"https://arxiv.org/html/2601.19675v1","lineno":null}); Total lines: 1846


## jan29_systemfour_route

LoPRo: Enhancing Low-Rank Quantization via Permuted Block-Wise Rotation (https://arxiv.org/html/2601.19675v1)
citeturn28515view2 [wordlim: 200] Crawled: today; Content type: text/html; Source: find({"ref_id":"https://arxiv.org/html/2601.19675v1","pattern":"3.2"}); Total lines: 1846
L15:   1. cite5†Abstract L16:   2. cite6†1 Introduction L17:   3. cite7†2 Related Works L18:   4. cite8†3 Method L19:     1. cite9†3.1 Problem Statement L20:     2. cite10†3.2 Partial Rotation quantization under permutation L21:     3. cite11†3.3 A Light Low-Rank Algorithm by Randomized Sketching L22:     4. cite12†3.4 Algorithm Analysis L23:   5. cite13†4 Evaluation L24:     1. cite14†4.1 Experiment Setup L25:     2. cite15†4.2 Main Results L26:     3. cite16†4.3 Quantization Cost L27:     4. cite17†4.4 Inference efficiency L28:     5. cite18†4.5 Ablation Studies L29:   6. cite19†5 Additional Experiments L181: ### 3.2 Partial Rotation quantization under permutation
L182: 
L183: For quantizing the residual matrix $\bm{R}$, two key observations are made: i). After token-wise scaling of the weights, more important columns exhibit smaller values, and maintaining their numerical stability is crucial for overall quantization accuracy. ii). It’s difficult in quantization to remain columns determined by the diagonal of proxy Hessian.
L900: \lxSVG@closescope
L901: \lxSVG@closescope {\lx@inpgf@ignorespaces}{\lx@inpgf@ignorespaces}{\lx@inpgf@ignorespaces}\hss}\lxSVG@discardpath\lxSVG@closescope \hss}}\lxSVG@closescope\endpgfpicture}}}}}$  | 3.2  | 32(16)  | 5.47  | 40.6  | 75.8  | 67.9  | 76.9
L915: {{}{}}{{}}{}{}{}{}{{}}{}\lxSVG@begingroup@{_scopebegin=1} \color[rgb]{0.2656,0.4609,0.7031}\lxSVG@fill\lxSVG@drawpath@unclipped{M 21.45 0 M 21.45 0 L 21.45 8.94 L 25.02 8.94 L 25.02 0 Z M 25.02 8.94}{stroke:none} \lx@inpgf@ignorespaces
L916: \lxSVG@closescope {}{{}}{}
L917: {{}{}}{{}}{}{}{}{}{{}}{}\lxSVG@begingroup@{_scopebegin=1} \color[rgb]{0.4141,0.7344,0.9297}\lxSVG@fill\lxSVG@drawpath@unclipped{M 25.02 0 M 25.02 0 L 25.02 8.94 L 28.6 8.94 L 28.6 0 Z M 28.6 8.94}{stroke:none} \lx@inpgf@ignorespaces
L918: \lxSVG@closescope
L919: \lxSVG@closescope {\lx@inpgf@ignorespaces}{\lx@inpgf@ignorespaces}{\lx@inpgf@ignorespaces}\hss}\lxSVG@discardpath\lxSVG@closescope \hss}}\lxSVG@closescope\endpgfpicture}}}}}$  | 3.2  | 32(8)  | 5.37  | 42.8  | 76.0  | 68.9  | 77.2
L920: LLaMA2-13B  | Method  | Tag  | Bit  | rank(bit)  | PPL  | ZeroShot Acc
L921: AC  | AE  | WI  | QA
L922: CALDERA  | $\mathord{\vbox{\hbox{\hbox to20.67pt{\vbox to6.46pt{\pgfpicture\makeatletter\hbox{\hskip 0.0pt\lower 0.0pt\hbox to0.0pt{\lxSVG@begingroup@{_scopebegin=1} \lxSVG@begingroup@{stroke=#000000} \lxSVG@begingroup@{fill=#000000} \lxSVG@setlinewidth{\the\pgflinewidth}\lxSVG@begingroup@{stroke-width=0.4pt} \lx@inpgf@ignorespaces\nullfont\hbox to0.0pt{\lxSVG@begingroup@{_scopebegin=1} {\lx@inpgf@ignorespaces}\lx@inpgf@ignorespaces{\lx@inpgf@ignorespaces}\lx@inpgf@ignorespaces   \par{}{{}}{}
L992: \lxSVG@closescope
L993: \lxSVG@closescope {\lx@inpgf@ignorespaces}{\lx@inpgf@ignorespaces}{\lx@inpgf@ignorespaces}\hss}\lxSVG@discardpath\lxSVG@closescope \hss}}\lxSVG@closescope\endpgfpicture}}}}}$  | 3.2  | 32(16)  | 4.88  | 45.4  | 76.4  | 71.4  | 79.2
L994: LoPRo_{v}-FT  | $\mathord{\vbox{\hbox{\hbox to20.67pt{\vbox to6.46pt{\pgfpicture\makeatletter\hbox{\hskip 0.0pt\lower 0.0pt\hbox to0.0pt{\lxSVG@begingroup@{_scopebegin=1} \lxSVG@begingroup@{stroke=#000000} \lxSVG@begingroup@{fill=#000000} \lxSVG@setlinewidth{\the\pgflinewidth}\lxSVG@begingroup@{stroke-width=0.4pt} \lx@inpgf@ignorespaces\nullfont\hbox to0.0pt{\lxSVG@begingroup@{_scopebegin=1} {\lx@inpgf@ignorespaces}\lx@inpgf@ignorespaces{\lx@inpgf@ignorespaces}\lx@inpgf@ignorespaces   \par{}{{}}{}
L1000: {{}{}}{{}}{}{}{}{}{{}}{}\lxSVG@begingroup@{_scopebegin=1} \color[rgb]{0.4102,0.4102,0.4102}\lxSVG@fill\lxSVG@drawpath@unclipped{M 8.94 0 M 8.94 0 L 8.94 8.94 L 12.51 8.94 L 12.51 0 Z M 12.51 8.94}{stroke:none} \lx@inpgf@ignorespaces
L1001: \lxSVG@closescope {}{{}}{}
L1003: \lxSVG@closescope {}{{}}{}
L1004: {{}{}}{{}}{}{}{}{}{{}}{}\lxSVG@begingroup@{_scopebegin=1} \color[rgb]{1,0.8789,0.5898}\lxSVG@fill\lxSVG@drawpath@unclipped{M 16.09 0 M 16.09 0 L 16.09 8.94 L 19.66 8.94 L 19.66 0 Z M 19.66 8.94}{stroke:none} \lx@inpgf@ignorespaces
L1005: \lxSVG@closescope \par
L1006: {}{{}}{}
L1007: {{}{}}{{}}{}{}{}{}{{}}{}\lxSVG@begingroup@{_scopebegin=1} \color[rgb]{0.2656,0.4609,0.7031}\lxSVG@fill\lxSVG@drawpath@unclipped{M 21.45 0 M 21.45 0 L 21.45 8.94 L 25.02 8.94 L 25.02 0 Z M 25.02 8.94}{stroke:none} \lx@inpgf@ignorespaces
L1008: \lxSVG@closescope {}{{}}{}
L1009: {{}{}}{{}}{}{}{}{}{{}}{}\lxSVG@begingroup@{_scopebegin=1} \color[rgb]{0.4141,0.7344,0.9297}\lxSVG@fill\lxSVG@drawpath@unclipped{M 25.02 0 M 25.02 0 L 25.02 8.94 L 28.6 8.94 L 28.6 0 Z M 28.6 8.94}{stroke:none} \lx@inpgf@ignorespaces
L1010: \lxSVG@closescope
L1011: \lxSVG@closescope {\lx@inpgf@ignorespaces}{\lx@inpgf@ignorespaces}{\lx@inpgf@ignorespaces}\hss}\lxSVG@discardpath\lxSVG@closescope \hss}}\lxSVG@closescope\endpgfpicture}}}}}$  | 3.2  | 2(8)  | 4.80  | 46.2  | 77.9  | 71.7  | 80.1
L1012: ### 4.3 Quantization Cost
L1013: Table 3: Quantization time for methods, where ‘h’ denotes hours and ‘m’ denotes minutes. NA indicates that the method was not implemented or encountered OOM errors during execution.
L1014: Model  | GPTQ  | GPTVQ  | LQER  | AQLM  | OminiQ  | LoPRo  | LoPRo_{v}
L1015: LLaMA2-7B  | 25.2m  | 1.5h  | 45.2m  | 11.1h  | 3.1h  | 26.4m$\downarrow$ $\downarrow$  | 32.2m$\downarrow$
L1016: LLaMA2-13B  | 40.5m  | 3.7h  | 1.2h  | 22.7h  | 5.3h  | 44.5m$\downarrow$ $\downarrow$  | 56m$\downarrow$
L1017: Mixtral-8x7B  | 2.6h  | NA  | NA  | NA  | NA  | 2.0h$\downarrow$ $\downarrow$  | 2.4h$\downarrow$
L1018: We report the runtime comparison in Table cite106†3 . In LoPRo, the quantization costs primarily consist of low-rank sketching and block-wise $\bm{H}_{wal}$ transformation to $\bm{R}$; the quantization of $\mathbf{R}^{\prime}$. Compared to methods such as OmniQuant and QuIP#, LoPRo is significantly faster that requiring less than 2.5 hours to quantize the Mixtral-8x7B model.
L1019: This efficiency stems from the employ of R1SVD for low-rank decomposition, which operates in $\mathcal{O}(N^{2})$ time complexity, growing linearly with model size, in contrast to the $\mathcal{O}(N^{3})$ cost of full SVD; Notably, even under vector quantization, LoPRo remains faster than GPTVQ. This is because we adopt only the simplest form of vector quantization—without advanced components such as LoRA or fine-tuning and even achieve higher accuracy.
L1020: This further demonstrates the effectiveness and practicality of our approach.
L1021: ### 4.4 Inference efficiency
L1022: 
L1023: Table 4: Inference throughput and latency of the LoPRo.
L1024: Model  | Batch  | Decode (token/s)  | Latency
L1025: Baseline  | LoPRo  | Rotation  | Low-rank  | Total
L1026: 7b  | 1  | 93.3  | 83.7  | 4.3%  | 6.0%  | 10.3%
L1027: 16  | 368.6  | 334.5  | 3.7%  | 5.6%  | 9.3%
L1028: 64  | 450.0  | 412.8  | 3.2%  | 5.1%  | 8.3%
L1029: 13b  | 1  | 62.4  | 56.1  | 3.9%  | 6.2%  | 10.1%
L1030: 16  | 274.4  | 252.4  | 3.3%  | 4.7%  | 8.0%
L1031: 64  | 388.4  | 358.2  | 2.9%  | 4.9%  | 7.8%
L1032: In inference, we take the W4A16 kernel in GPTQModel cite107†qubitium (2024) as a baseline and the throughput and latency of LoPRo are shown in Table cite108†4 . Since only linear layers are affected, the rotation can be efficiently applied to the input $\mathbf{X}$ by Fast Walsh-Hadamard Transform in $\mathcal{O}(nlog(n))$ cite66†Tseng et al. (2024) .
L1033: Furthermore, the low-rank components are computed with a very small rank ($r=16$) and only brings below 10% latency, and this overhead further decreases as model scale and batch size increase—aligning well with the theoretical analysis presented in Section cite109†• ‣ 3.4 .
L1206:   1. cite6†1 Introduction L1207:   2. cite7†2 Related Works L1208:   3. cite8†3 Method L1209:     1. cite9†3.1 Problem Statement L1210:     2. cite10†3.2 Partial Rotation quantization under permutation L1211:     3. cite11†3.3 A Light Low-Rank Algorithm by Randomized Sketching L1212:     4. cite12†3.4 Algorithm Analysis L1213:   4. cite13†4 Evaluation L1214:     1. cite14†4.1 Experiment Setup L1215:     2. cite15†4.2 Main Results L1216:     3. cite16†4.3 Quantization Cost L1217:     4. cite17†4.4 Inference efficiency L1218:     5. cite18†4.5 Ablation Studies L1219:   5. cite19†5 Additional Experiments 

## jan29_systemfour_core

LoPRo: Enhancing Low-Rank Quantization via Permuted Block-Wise Rotation (https://arxiv.org/html/2601.19675v1)
citeturn28516view2 [wordlim: 200] Crawled: today; Content type: text/html; Source: open({"ref_id":"https://arxiv.org/html/2601.19675v1","lineno":181}); Total lines: 1846
L173: ### 3.1 Problem Statement
L174: 
L175: Previous methods suffer from suboptimal accuracy without fine-tuning due to insufficient utilization of the three key characteristics. The problem we aim to address is: How to effectively balance three strategies to achieve the highest accuracy?
L176: We observe that the strategies in ¶cite7†O1 , ¶cite7†F1 are not mutually exclusive but rotation and truncation in ¶cite7†F1 would disrupt the important channel preserved in ¶cite81†F2.a . Instead, the low-rank method is considered to be a promising direction. Specifically, the $\bm{W}_{r}$ with high precision can be fused with rotation without introducing additional storage or computational overhead.
L177: Between the two forms in Eq cite77†3 , the first is more suitable for fine-tuning in the LoRA scenario, as low-rank approximation is performed independently after quantization. However, for fine-tuning-free PTQs, we consider that the second form in Eq cite77†3 is better, because the original $\bm{W}$ is more amenable to low-rank approximation, as quantization disrupts its inherent low-rank structure. In this form, the low-rank matrix $\bm{W}_{r}$ can be calculated by:
L178:  | $$\begin{split}\{\bm{U}^{\prime},\bm{\Sigma},\bm{V}\}=\text{SVD}(\bm{W}\alpha),\ \ {\bm{V}^{\prime}}=\bm{V}\alpha^{-1},\quad\bm{W}_{r}=\bm{W}_{L}\bm{W}_{R}=(\bm{U}\bm{\Sigma})(\bm{V}^{\prime}),\ \end{split}$$  |  | (4)
L179: where $\alpha$ is a scaling factor calculated by layer input. After applying low-rank decomposition with scaling, the property in cite7†¶F2 is utilized. Quantizing the residual matrix becomes a critical challenge. Since the low-rank approximation alone cannot fully smooth the value distribution within the weight matrix, a reasonable approach is to apply rotation to the residual matrix to further enhance accuracy.
L180: However, results in Table cite86†5 show that applying a full Hadamard rotation degrades quantization accuracy (8.4 to 9.49 of perplexity$\downarrow$ in LLaMA2-7B).
L181: ### 3.2 Partial Rotation quantization under permutation
L182: 
L183: For quantizing the residual matrix $\bm{R}$, two key observations are made: i). After token-wise scaling of the weights, more important columns exhibit smaller values, and maintaining their numerical stability is crucial for overall quantization accuracy. ii). It’s difficult in quantization to remain columns determined by the diagonal of proxy Hessian.
L184: We propose a block-wise partial rotation quantization algorithm for the residual matrix, which consists of the following three components:
L185: 
L186: 1. Column Permutation: Considering quantization difficulty and column importance, we introduce a reordering strategy formulated as Eq cite87†5 , and leave a detailed discussion in Appendix cite26†A.4 .
L187: 
L188:  | $$perm=sort\big(\text{diag}(\bm{H})/amean(\bm{R},axis=0)\big).\text{idx}\quad\text{and}\quad\bm{R}=\bm{W}-\bm{W}_{r}\ ,$$  |  | (5)
L189: where $\bm{H}$ is the proxy Hessian computed in Eq cite65†1 , $\bm{R}$ is the residual matrix after low-rank approximation and $amean$ computes the mean of absolute values along the first dimension. This reordering can be expressed by applying permutation matrix $\bm{P}$, where $\bm{P}_{i,perm[i]}=1$ and other elements are 0. The matrix $P$ is orthogonal and satisfied $\bm{P}^{T}\bm{P}=\bm{I}$. After permutation, important columns are moved to the leading columns of the residual matrix.
L190: 2. Partial block Rotation: Rotation enhances the incoherence between $\bm{R}$ and H, thereby improving quantization accuracy. However, applying a full rotation would disrupt the column importance ordering and degrade accuracy. To address this, we propose a partial rotation in a block-wise manner:
L191:  | $$\bm{Q}=\begin{bmatrix}\bm{I}&0&\cdots&\cdots&0\\
L192: 0&\textbf{H}_{wal}&0&\cdots&\vdots\\
L193: \vdots&0&\ddots&0&\vdots\\
L194: \vdots&\vdots&0&\ddots&0\\
L195: 0&\cdots&\cdots&0&\textbf{H}_{wal}\end{bmatrix},\bm{R}=\bm{R}\bm{P}\bm{Q}$$  |  | (6)
L196: where $\bm{I}$ is an identity matrix of size $b_{I}$, and $\textbf{H}_{wal}\in\mathbb{R}^{b_{H}\times b_{H}}$ is a Walsh-Hadamard matrix and $b_{H}$ is an integer power of 2. In this case, the leading columns, corresponding to the most important channel, are unrotated (identity block) to preserve them from degradation of quantization accuracy. The importance of other columns after permutation gradually decreases, as shown in Figure cite85†1 .
L197: By applying block-wise Walsh-Hadamard rotation of similarly important columns, it’s easier to quantize the $\bm{R}^{\prime}$ than $\bm{R}$. In this case, we have Theorem.cite88†1 and proved in Appendix cite29†B.2 .
L198: Theorem 1 (Rotation). Denote $\mathcal{L}_{orig}$ as the original quantization loss, and $\mathcal{L}_{rot}$ as the loss under rotation in Eq cite89†6 ; we deduce that
L199: 
L200:  | $$\mathcal{L}_{\text{rot}}(\bm{R})\leq\mathcal{L}_{\text{orig}}(\bm{R})$$  |  | (7)
L201: 
L202: 3. Quantization with Rotation Matrix
L203: After the low-rank approximation and partial Walsh-Hadamard rotation described in the previous section, we effectively leverage the feature cite7†¶F1 and cite7†¶F2 to obtain $\bm{R}^{\prime}$ that is more amenable to quantization. Recall the low-rank quantization form in Eq cite77†3 under transformation in Eq cite89†6 .
L204: 
L205:  | $$\bm{W}\bm{X}=\bm{W}_{r}\bm{X}+\mathcal{\bm{Q}}(\bm{R}^{\prime})\bm{Q}^{T}\bm{P}^{T}\bm{X},$$  |  | (8)
L206: This formulation shows that the quantized component and the low-rank component are decoupled. Therefore, we can apply methods from ¶cite7†O1 independently to improve the quantization of the $\bm{R}^{\prime}$. The optimization function can be expressed as Eq cite90†9 and the proof is given in Appendix cite30†B.3 :
L207: 
L208:  | $$\mathcal{L}(\bm{R})=\|\bm{R}\bm{X}-\hat{\bm{R}}\bm{X}\|^{2}=\text{tr}\left((\hat{\bm{R}}-\bm{R})\bm{H}^{\prime}(\hat{\bm{R}}-\bm{R})^{T}\right),$$  |  | (9)
L209: where $\bm{H}^{\prime}=\bm{Q}^{T}\bm{P}^{T}\bm{H}\bm{P}\bm{Q}$ and $\bm{H}$ is the origin proxy Hessian. In addition to this, quantization methods can be freely replaced with other advanced schemes, such as vector-wise quantization.
L210: ### 3.3 A Light Low-Rank Algorithm by Randomized Sketching
L211: 
L212: A common practice of low-rank methods preserves $\bm{W}_{L}$ and $\bm{W}_{R}$ in full precision cite67†Lee et al. (2025) ; cite55†Zhang et al. (2024a) , while in CALDERA cite57†Saha et al. (2024) , the low-rank components are further compressed by quantization to reduce memory costs. But this method requires a higher rank like 256 which incurs a considerable computational burden.


## jan29_systemfour_eval

LoPRo: Enhancing Low-Rank Quantization via Permuted Block-Wise Rotation (https://arxiv.org/html/2601.19675v1)
citeturn28517view2 [wordlim: 200] Crawled: today; Content type: text/html; Source: open({"ref_id":"https://arxiv.org/html/2601.19675v1","lineno":213}); Total lines: 1846
L203: After the low-rank approximation and partial Walsh-Hadamard rotation described in the previous section, we effectively leverage the feature cite7†¶F1 and cite7†¶F2 to obtain $\bm{R}^{\prime}$ that is more amenable to quantization. Recall the low-rank quantization form in Eq cite77†3 under transformation in Eq cite89†6 .
L204: 
L205:  | $$\bm{W}\bm{X}=\bm{W}_{r}\bm{X}+\mathcal{\bm{Q}}(\bm{R}^{\prime})\bm{Q}^{T}\bm{P}^{T}\bm{X},$$  |  | (8)
L206: This formulation shows that the quantized component and the low-rank component are decoupled. Therefore, we can apply methods from ¶cite7†O1 independently to improve the quantization of the $\bm{R}^{\prime}$. The optimization function can be expressed as Eq cite90†9 and the proof is given in Appendix cite30†B.3 :
L207: 
L208:  | $$\mathcal{L}(\bm{R})=\|\bm{R}\bm{X}-\hat{\bm{R}}\bm{X}\|^{2}=\text{tr}\left((\hat{\bm{R}}-\bm{R})\bm{H}^{\prime}(\hat{\bm{R}}-\bm{R})^{T}\right),$$  |  | (9)
L209: where $\bm{H}^{\prime}=\bm{Q}^{T}\bm{P}^{T}\bm{H}\bm{P}\bm{Q}$ and $\bm{H}$ is the origin proxy Hessian. In addition to this, quantization methods can be freely replaced with other advanced schemes, such as vector-wise quantization.
L210: ### 3.3 A Light Low-Rank Algorithm by Randomized Sketching
L211: 
L212: A common practice of low-rank methods preserves $\bm{W}_{L}$ and $\bm{W}_{R}$ in full precision cite67†Lee et al. (2025) ; cite55†Zhang et al. (2024a) , while in CALDERA cite57†Saha et al. (2024) , the low-rank components are further compressed by quantization to reduce memory costs. But this method requires a higher rank like 256 which incurs a considerable computational burden.
L213: Therefore, to minimize the additional overhead introduced by low-rank decomposition while maintaining inference performance, we proposed R1SVD: a simplification to the randomized SVD algorithm cite91†Frieze et al. (2004) ; cite92†Musco and Musco (2015) under the rank-1 condition. This simplification introduces a rank-1 matrix approximation technique, as described below:
L214: Given a matrix $\bm{A}\in\mathbb{R}^{m\times n}$. For a standard RSVD (Randomized Singular Value Decomposition) prototype, it typically consists of the following two steps:
L215: Stage A: Generate an $\mathbb{R}^{n\times r}$ Gaussian test matrix $\bm{S}$ and form $\bm{Y}=(\bm{A}\bm{A}^{*})^{it}\bm{A}\bm{S}$, where $it$ is the iteration times. Construct a matrix $\bm{Q}=QR(\bm{Y})$ by QR decomposition whose columns form an orthonormal basis of $\bm{Y}$.
L216: Stage B: Form $\bm{B}=\bm{Q}^{*}\bm{A}$. Compute an SVD of the small matrix: $\bm{B}=\bm{U}^{\prime}\bm{\Sigma}\bm{V}^{*}$. Set $\bm{U}=\bm{Q}\bm{U}^{\prime}$.
L217: 
L218: If a rank-1 matrix $\bm{S}\in\mathbb{R}^{n\times 1}$ is utilized for low-rank approximation of a matrix and substituted into the two stages, we also have $Y=(\bm{A}\bm{A}^{*})^{it}\bm{A}S$, then for the matrix $\bm{Y}\in\mathbb{R}^{m\times 1}$ , the QR decomposition can be directly represented as follows.
L219:  | $$\bm{Q}=\frac{\bm{Y}}{\|\bm{Y}\|}\in\mathbb{R}^{m\times 1},\bm{R}=\|\bm{Y}\|\in\mathbb{R}^{1\times 1}.$$  |  | (10)
L220: 
L221: Similarly, the SVD decomposition for rank-1 matrix $\bm{B}=\bm{Q}^{*}\bm{A}$ can be represented as follows:
L222: 
L223:  | $$\bm{U}^{\prime}=\{1\},\bm{\Sigma}=\|\bm{B}\|,\bm{V}=\frac{\bm{B}}{\|\bm{B}\|}.$$  |  | (11)
L224: 
L225: Applying Stage B and Equation.cite93†10 , we have the rank-1 matrix $\bm{A}_{1}=\bm{U}\bm{\Sigma}\bm{V}$:
L226:  | $\displaystyle\bm{U}=\frac{(\bm{A}\bm{A}^{*})^{it}\bm{A}\bm{S}}{\|(\bm{A}\bm{A}^{*})^{it}\bm{A}\bm{S}\|},\quad\bm{\Sigma}=\frac{\|\bm{S}^{*}\bm{A}^{*}(\bm{A}\bm{A}^{*})^{it}\bm{A}\|}{\|(\bm{A}\bm{A}^{*})^{it}\bm{A}\bm{S}\|},\quad\bm{V}=\frac{\bm{S}^{*}\bm{A}^{*}(\bm{A}\bm{A}^{*})^{it}\bm{A}}{\|\bm{S}^{*}\bm{A}^{*}(\bm{A}\bm{A}^{*})^{it}\bm{A}\|}.$  |  | (12)
L227: Then, we set $\bm{A}=\bm{A}-\bm{A}_{1}$ and apply iteration to this process, which enables decomposition at any rank. Since the singular value matrix $\mathbf{\Sigma}$ is diagonal with low storage cost, by storing $\bm{U}$ and $\bm{V}$ in fp8 while retaining $\bm{\Sigma}$ in fp16, the storage overhead can be reduced by half. Furthermore, the loss in precision is compensated in subsequent iterations, thereby preserving the overall accuracy.
L228: ### 3.4 Algorithm Analysis
L229: 
L230: In this section, we analyze LoPRo from:
L231: 
L232:   * •
L233: 
L234: Compression Ratio: Consider a weight matrix $\bm{W}\in\mathbb{R}^{m\times n}$ with an original precision $d_{o}$ (in bits), quantized to a target precision $d_{q}$ with group size $g$. The low-rank components of rank $r$ are stored in precision $d_{r}$. Then, the overall average compression bit $d_{C}$ is given by:
L235:  | $$d_{C}=\overbrace{d_{q}+\frac{d_{o}}{g}}^{Quant\ \bm{W}}+\overbrace{\frac{rd_{r}}{n}+\frac{rd_{r}}{m}}^{\bm{U}\ \ \text{and}\ \ \bm{V}}+\overbrace{\frac{2d_{o}}{n}}^{\ \alpha\text{\ and}\ \bm{P}}+\overbrace{\frac{rd_{o}}{mn}}^{\bm{\Sigma}}.$$  |  | (13)
L236: 
L237: We provide a detailed analysis and proof in Appendix cite24†A.2 .
L238: 
L239:   * •
L240: Inference Latency: Assume the weight is square and the input is $\mathbf{X}\in\mathbb{R}^{n\times b}$. Therefore, the total inference latency complexity $C$ is shown in Eq cite94†13 and detailed in Appendix cite25†A.3 :
L241: 
L242:  | $$C=\mathcal{O}\bigl(nb(2r+1+\log b_{H})\bigr).$$  |  | (14)
L243: 
L244: This shows that the additional latency grows linearly with the batch size $b$ and is manageable for small $r$ and moderate $b_{H}$, making the method suitable for efficient deployment.


## jan29_systemfour_eval

LoPRo: Enhancing Low-Rank Quantization via Permuted Block-Wise Rotation (https://arxiv.org/html/2601.19675v1)
citeturn28517view3 [wordlim: 200] Crawled: today; Content type: text/html; Source: open({"ref_id":"https://arxiv.org/html/2601.19675v1","lineno":1034}); Total lines: 1846
L1018: We report the runtime comparison in Table cite106†3 . In LoPRo, the quantization costs primarily consist of low-rank sketching and block-wise $\bm{H}_{wal}$ transformation to $\bm{R}$; the quantization of $\mathbf{R}^{\prime}$. Compared to methods such as OmniQuant and QuIP#, LoPRo is significantly faster that requiring less than 2.5 hours to quantize the Mixtral-8x7B model.
L1019: This efficiency stems from the employ of R1SVD for low-rank decomposition, which operates in $\mathcal{O}(N^{2})$ time complexity, growing linearly with model size, in contrast to the $\mathcal{O}(N^{3})$ cost of full SVD; Notably, even under vector quantization, LoPRo remains faster than GPTVQ. This is because we adopt only the simplest form of vector quantization—without advanced components such as LoRA or fine-tuning and even achieve higher accuracy.
L1020: This further demonstrates the effectiveness and practicality of our approach.
L1021: ### 4.4 Inference efficiency
L1022: 
L1023: Table 4: Inference throughput and latency of the LoPRo.
L1024: Model  | Batch  | Decode (token/s)  | Latency
L1025: Baseline  | LoPRo  | Rotation  | Low-rank  | Total
L1026: 7b  | 1  | 93.3  | 83.7  | 4.3%  | 6.0%  | 10.3%
L1027: 16  | 368.6  | 334.5  | 3.7%  | 5.6%  | 9.3%
L1028: 64  | 450.0  | 412.8  | 3.2%  | 5.1%  | 8.3%
L1029: 13b  | 1  | 62.4  | 56.1  | 3.9%  | 6.2%  | 10.1%
L1030: 16  | 274.4  | 252.4  | 3.3%  | 4.7%  | 8.0%
L1031: 64  | 388.4  | 358.2  | 2.9%  | 4.9%  | 7.8%
L1032: In inference, we take the W4A16 kernel in GPTQModel cite107†qubitium (2024) as a baseline and the throughput and latency of LoPRo are shown in Table cite108†4 . Since only linear layers are affected, the rotation can be efficiently applied to the input $\mathbf{X}$ by Fast Walsh-Hadamard Transform in $\mathcal{O}(nlog(n))$ cite66†Tseng et al. (2024) .
L1033: Furthermore, the low-rank components are computed with a very small rank ($r=16$) and only brings below 10% latency, and this overhead further decreases as model scale and batch size increase—aligning well with the theoretical analysis presented in Section cite109†• ‣ 3.4 .
L1034: ### 4.5 Ablation Studies
L1035: Table 5: Ablation on different components in LoPRo under 2-bit LLaMA2-7b. ‘NA’ means non-use of such strategy. ‘OQ’ and ‘VQ’ denote use GPTQ and GPTVQ as the quantizer respectively. The last two bolded lines represent LoPRo and LoPRo_{v}
L1036: Bits  | Rotation  | Quant  | Tag  | PPL  | Avg.acc
L1037: 16  | NA  | NA  | $\mathord{\vbox{\hbox{\hbox to20.67pt{\vbox to6.46pt{\pgfpicture\makeatletter\hbox{\hskip 0.0pt\lower 0.0pt\hbox to0.0pt{\lxSVG@begingroup@{_scopebegin=1} \lxSVG@begingroup@{stroke=#000000} \lxSVG@begingroup@{fill=#000000} \lxSVG@setlinewidth{\the\pgflinewidth}\lxSVG@begingroup@{stroke-width=0.4pt} \lx@inpgf@ignorespaces\nullfont\hbox to0.0pt{\lxSVG@begingroup@{_scopebegin=1} {\lx@inpgf@ignorespaces}\lx@inpgf@ignorespaces{\lx@inpgf@ignorespaces}\lx@inpgf@ignorespaces   \par{}{{}}{}
L1038: {{}{}}{{}}{}{}{}{}{{}}{}\lxSVG@begingroup@{_scopebegin=1} \color[rgb]{0.4102,0.4102,0.4102}\lxSVG@fill\lxSVG@drawpath@unclipped{M 0 0 M 0 0 L 0 8.94 L 3.57 8.94 L 3.57 0 Z M 3.57 8.94}{stroke:none} \lx@inpgf@ignorespaces
L1039: \lxSVG@closescope {}{{}}{}
L1040: {{}{}}{{}}{}{}{}{}{{}}{}\lxSVG@begingroup@{_scopebegin=1} \color[rgb]{0.4102,0.4102,0.4102}\lxSVG@fill\lxSVG@drawpath@unclipped{M 3.57 0 M 3.57 0 L 3.57 8.94 L 7.15 8.94 L 7.15 0 Z M 7.15 8.94}{stroke:none} \lx@inpgf@ignorespaces
L1041: \lxSVG@closescope \par
L1042: {}{{}}{}
L1043: {{}{}}{{}}{}{}{}{}{{}}{}\lxSVG@begingroup@{_scopebegin=1} \color[rgb]{0.4102,0.4102,0.4102}\lxSVG@fill\lxSVG@drawpath@unclipped{M 8.94 0 M 8.94 0 L 8.94 8.94 L 12.51 8.94 L 12.51 0 Z M 12.51 8.94}{stroke:none} \lx@inpgf@ignorespaces
L1044: \lxSVG@closescope {}{{}}{}
L1045: {{}{}}{{}}{}{}{}{}{{}}{}\lxSVG@begingroup@{_scopebegin=1} \color[rgb]{0.4102,0.4102,0.4102}\lxSVG@fill\lxSVG@drawpath@unclipped{M 12.51 0 M 12.51 0 L 12.51 8.94 L 16.09 8.94 L 16.09 0 Z M 16.09 8.94}{stroke:none} \lx@inpgf@ignorespaces
L1046: \lxSVG@closescope {}{{}}{}
L1047: {{}{}}{{}}{}{}{}{}{{}}{}\lxSVG@begingroup@{_scopebegin=1} \color[rgb]{0.4102,0.4102,0.4102}\lxSVG@fill\lxSVG@drawpath@unclipped{M 16.09 0 M 16.09 0 L 16.09 8.94 L 19.66 8.94 L 19.66 0 Z M 19.66 8.94}{stroke:none} \lx@inpgf@ignorespaces
L1048: \lxSVG@closescope \par
L1049: {}{{}}{}
L1050: {{}{}}{{}}{}{}{}{}{{}}{}\lxSVG@begingroup@{_scopebegin=1} \color[rgb]{0.4102,0.4102,0.4102}\lxSVG@fill\lxSVG@drawpath@unclipped{M 21.45 0 M 21.45 0 L 21.45 8.94 L 25.02 8.94 L 25.02 0 Z M 25.02 8.94}{stroke:none} \lx@inpgf@ignorespaces
L1051: \lxSVG@closescope {}{{}}{}
L1052: {{}{}}{{}}{}{}{}{}{{}}{}\lxSVG@begingroup@{_scopebegin=1} \color[rgb]{0.4102,0.4102,0.4102}\lxSVG@fill\lxSVG@drawpath@unclipped{M 25.02 0 M 25.02 0 L 25.02 8.94 L 28.6 8.94 L 28.6 0 Z M 28.6 8.94}{stroke:none} \lx@inpgf@ignorespaces
L1053: \lxSVG@closescope
L1054: \lxSVG@closescope {\lx@inpgf@ignorespaces}{\lx@inpgf@ignorespaces}{\lx@inpgf@ignorespaces}\hss}\lxSVG@discardpath\lxSVG@closescope \hss}}\lxSVG@closescope\endpgfpicture}}}}}$  | 5.11  | 66.8
L1055: 2.2  | NA  | RTN  | $\mathord{\vbox{\hbox{\hbox to20.67pt{\vbox to6.46pt{\pgfpicture\makeatletter\hbox{\hskip 0.0pt\lower 0.0pt\hbox to0.0pt{\lxSVG@begingroup@{_scopebegin=1} \lxSVG@begingroup@{stroke=#000000} \lxSVG@begingroup@{fill=#000000} \lxSVG@setlinewidth{\the\pgflinewidth}\lxSVG@begingroup@{stroke-width=0.4pt} \lx@inpgf@ignorespaces\nullfont\hbox to0.0pt{\lxSVG@begingroup@{_scopebegin=1} {\lx@inpgf@ignorespaces}\lx@inpgf@ignorespaces{\lx@inpgf@ignorespaces}\lx@inpgf@ignorespaces   \par{}{{}}{}


## jan29_systemfour_settings

LoPRo: Enhancing Low-Rank Quantization via Permuted Block-Wise Rotation (https://arxiv.org/html/2601.19675v1)
citeturn28518view3 [wordlim: 200] Crawled: today; Content type: text/html; Source: find({"ref_id":"https://arxiv.org/html/2601.19675v1","pattern":"4.1 Experiment Setup"}); Total lines: 1846
L15:   1. cite5†Abstract L16:   2. cite6†1 Introduction L17:   3. cite7†2 Related Works L18:   4. cite8†3 Method L19:     1. cite9†3.1 Problem Statement L20:     2. cite10†3.2 Partial Rotation quantization under permutation L21:     3. cite11†3.3 A Light Low-Rank Algorithm by Randomized Sketching L22:     4. cite12†3.4 Algorithm Analysis L23:   5. cite13†4 Evaluation L24:     1. cite14†4.1 Experiment Setup L25:     2. cite15†4.2 Main Results L26:     3. cite16†4.3 Quantization Cost L27:     4. cite17†4.4 Inference efficiency L28:     5. cite18†4.5 Ablation Studies L29:   6. cite19†5 Additional Experiments L30:   7. cite20†6 Conclusion L31:   8. cite21†References L32:   9. cite22†A LoPRo Details: L33:     1. cite23†A.1 Algorithm pseudo-code L34:     2. cite24†A.2 Average Bit-width L35:     3. cite25†A.3 Time Complexity L36:     4. cite26†A.4 Permutation L37:   10. cite27†B Proofs L38:     1. cite28†B.1 Notations and Assumptions L39:     2. cite29†B.2 Proof 1. Quantization under Rotation L40:     3. cite30†B.3 Proof 2. Quantization with hessian after rotation L41:   11. cite31†C Additional Implementation Details L42:   12. cite32†D Extended Ablation Studies L43:     1. cite33†D.1 Ablation on rank L240: Inference Latency: Assume the weight is square and the input is $\mathbf{X}\in\mathbb{R}^{n\times b}$. Therefore, the total inference latency complexity $C$ is shown in Eq cite94†13 and detailed in Appendix cite25†A.3 :
L241: 
L242:  | $$C=\mathcal{O}\bigl(nb(2r+1+\log b_{H})\bigr).$$  |  | (14)
L243: 
L244: This shows that the additional latency grows linearly with the batch size $b$ and is manageable for small $r$ and moderate $b_{H}$, making the method suitable for efficient deployment.
L245: ## 4 Evaluation
L246: ### 4.1 Experiment Setup
L247: 
L248: Models: Evaluations are carried out on the LLaMA-2 and LLaMA-3 dense model families cite95†Touvron et al. (2023) and Mixture of Experts (MoE) model Mixtral-8x7B cite96†Jiang et al. (2024) .
L249: Baseline: Following the classification introduced in §cite7†2 , we conduct a comprehensive comparison with the state-of-the-art (SOTA) PTQs within each class. Fine-tuning-free methods include: GPTQ cite50†Frantar et al. (2023) , GPTVQ cite73†Van Baalen et al. (2024) , OmniQuant cite63†Shao et al. (2023) , QuIP# cite66†Tseng et al. (2024) , LQER cite55†Zhang et al. (2024a) , and MoEQuant cite64†Chen et al.
L1158:   * Bisk et al. (2020) Y. Bisk, R. Zellers, R. Le bras, J. Gao, and Y. Choi PIQA: reasoning about physical commonsense in natural language. Proceedings of the AAAI Conference on Artificial Intelligence, pp. 7432–7439 (en-US). External Links: 【114†Link†dx.doi.org , cite115†Document†dx.doi.org Cited by: cite116†2nd item , cite117†§4.1 .
L1159:   * Boratko et al. (2018) M. Boratko, H. Padigela, D. Mikkilineni, P. Yuvraj, R. Das, A. McCallum, M. Chang, A. Fokoue-Nkoutche, P. Kapanipathi, N. Mattei, et al. A systematic classification of knowledge, reasoning, and context within the arc dataset. arXiv preprint arXiv:1806.00358. Cited by: cite118†1st item , cite119†Appendix G , cite117†§4.1 .
L1160:   * Chee et al. (2023) J. Chee, Y. Cai, V. Kuleshov, and C. M. De Sa Quip: 2-bit quantization of large language models with guarantees. Advances in Neural Information Processing Systems 36, pp. 4396–4429. Cited by: cite113†item (b) .
L1161:   * Chen et al. (2025) Z. Chen, X. Hu, D. Yang, Z. Xu, XUCHEN, Z. Yuan, S. Zhou, and JiangyongYu MoEQuant: enhancing quantization for mixture-of-experts large language models via expert-balanced sampling and affinity guidance. In Forty-second International Conference on Machine Learning, External Links: cite120†Link†openreview.net Cited by: cite112†Appendix C , cite111†Appendix E , cite121†item (a) , cite122†§4.1 .
L1162:   * Clark et al. (2019) C. Clark, K. Lee, M. Chang, T. Kwiatkowski, M. Collins, and K. Toutanova BoolQ: exploring the surprising difficulty of natural yes/no questions. arXiv preprint arXiv:1905.10044. Cited by: cite123†4th item , cite111†Appendix E .
L1163:   * Cobbe et al. (2021) K. Cobbe, V. Kosaraju, M. Bavarian, M. Chen, H. Jun, L. Kaiser, M. Plappert, J. Tworek, J. Hilton, R. Nakano, et al. Training verifiers to solve math word problems. arXiv preprint arXiv:2110.14168. Cited by: cite119†Appendix G .
L1165:   * Dettmers et al. (2023) T. Dettmers, A. Pagnoni, A. Holtzman, and L. Zettlemoyer Qlora: efficient finetuning of quantized llms. Advances in neural information processing systems 36, pp. 10088–10115. Cited by: cite125†§1 .
L1166:   * Ding et al. (2022) Y. Ding, H. Qin, Q. Yan, Z. Chai, J. Liu, X. Wei, and X. Liu Towards accurate post-training quantization for vision transformer. In Proceedings of the 30th ACM international conference on multimedia, pp. 5380–5388. Cited by: cite125†§1 .
L1168:   * Fino and Algazi (1976) Fino and Algazi Unified matrix treatment of the fast walsh-hadamard transform. IEEE Transactions on Computers C-25 (11), pp. 1142–1146. External Links: cite127†Document†dx.doi.org Cited by: cite128†3rd item .
L1169:   * Frantar et al. (2023) E. Frantar, S. Ashkboos, T. Hoefler, and D. Alistarh GPTQ: accurate post-training quantization for generative pre-trained transformers. In The Eleventh International Conference on Learning Representations, Cited by: cite112†Appendix C , cite125†§1 , cite121†item (a) , cite126†item (c) , cite122†§4.1 .
L1170:   * Frieze et al. (2004) A. Frieze, R. Kannan, and S. Vempala Fast monte-carlo algorithms for finding low-rank approximations. Journal of the ACM (JACM) 51 (6), pp. 1025–1041. Cited by: cite129†§3.3 .
L1171:   * Gao et al. (2024) L. Gao, J. Tow, B. Abbasi, S. Biderman, S. Black, A. DiPofi, C. Foster, L. Golding, J. Hsu, A. Le Noac’h, H. Li, K. McDonell, N. Muennighoff, C. Ociepa, J. Phang, L. Reynolds, H. Schoelkopf, A. Skowron, L. Sutawika, E. Tang, A. Thite, B. Wang, K. Wang, and A. Zou A framework for few-shot language model evaluation. Zenodo. External Links: cite130†Document†dx.doi.org , cite131†Link†zenodo.org Cited by: cite132†Appendix C , cite117†§4.1 .
L1172:   * Hendrycks et al. (2020) D. Hendrycks, C. Burns, S. Basart, A. Zou, M. Mazeika, D. Song, and J. Steinhardt Measuring massive multitask language understanding. arXiv preprint arXiv:2009.03300. Cited by: cite119†Appendix G .
L1173:   * Hu et al. (2022) E. J. Hu, Y. Shen, P. Wallis, Z. Allen-Zhu, Y. Li, S. Wang, L. Wang, W. Chen, et al. Lora: low-rank adaptation of large language models.. ICLR 1 (2), pp. 3. Cited by: cite133†§2 .
L1174:   * Huang et al. (2024) W. Huang, X. Ma, H. Qin, X. Zheng, C. Lv, H. Chen, J. Luo, X. Qi, X. Liu, and M. Magno How good are low-bit quantized llama3 models? an empirical study. CoRR abs/2404.14047. External Links: cite134†Link†doi.org Cited by: cite135†§4.2 .
L1175:   * Hubara et al. (2021) I. Hubara, Y. Nahshan, Y. Hanani, R. Banner, and D. Soudry Accurate post training quantization with small calibration sets. In International Conference on Machine Learning, pp. 4466–4475. Cited by: cite125†§1 .
L1176:   * Jiang et al. (2024) A. Q. Jiang, A. Sablayrolles, A. Roux, A. Mensch, B. Savary, C. Bamford, D. S. Chaplot, D. d. l. Casas, E. B. Hanna, F. Bressand, et al. Mixtral of experts. arXiv preprint arXiv:2401.04088. Cited by: cite136†§4.1 .
L1177:   * Kuzmin et al. (2023) A. Kuzmin, M. Nagel, M. Van Baalen, A. Behboodi, and T. Blankevoort Pruning vs quantization: which is better?. Advances in neural information processing systems 36, pp. 62414–62427. Cited by: cite137†§1 .
L1178:   * Kwon et al. (2023) W. Kwon, Z. Li, S. Zhuang, Y. Sheng, L. Zheng, C. H. Yu, J. E. Gonzalez, H. Zhang, and I. Stoica Efficient memory management for large language model serving with pagedattention. In Proceedings of the ACM SIGOPS 29th Symposium on Operating Systems Principles, Cited by: cite125†§1 .
L1186:   * Ma et al. (2024) Y. Ma, H. Li, X. Zheng, F. Ling, X. Xiao, R. Wang, S. Wen, F. Chao, and R. Ji AffineQuant: affine transformation quantization for large language models. In The Twelfth International Conference on Learning Representations, Cited by: cite145†Appendix C , cite141†item (a) .
L1187:   * Merity et al. (2016) S. Merity, C. Xiong, J. Bradbury, and R. Socher Pointer sentinel mixture models. arXiv preprint arXiv:1609.07843. Cited by: cite117†§4.1 .
L1188:   * Mihaylov et al. (2018) T. Mihaylov, P. Clark, T. Khot, and A. Sabharwal Can a suit of armor conduct electricity? a new dataset for open book question answering. arXiv preprint arXiv:1809.02789. Cited by: cite146†6th item , cite111†Appendix E .
L1189:   * Musco and Musco (2015) C. Musco and C. Musco Randomized block krylov methods for stronger and faster approximate singular value decomposition. Advances in neural information processing systems 28. Cited by: cite129†§3.3 .
L1190:   * Nagel et al. (2020) M. Nagel, R. A. Amjad, M. Van Baalen, C. Louizos, and T. Blankevoort Up or down? adaptive rounding for post-training quantization. In Proceedings of the 37th International Conference on Machine Learning, ICML’20. Cited by: cite147†§2 .
L1191:   * Narkhede et al. (2022) M. V. Narkhede, P. P. Bartakke, and M. S. Sutaone A review on weight initialization strategies for neural networks. Artificial intelligence review 55 (1), pp. 291–322. Cited by: cite133†§2 .
L1192:   * qubitium (2024) qubitium GPT-qmodel. GitHub. Note: cite148†https://github.com/modelcloud/gptqmodel†github.com Contact: qubitium@modelcloud.ai Cited by: cite149†§4.4 .
L1193:   * Raffel et al. (2020) C. Raffel, N. Shazeer, A. Roberts, K. Lee, S. Narang, M. Matena, Y. Zhou, W. Li, and P. J. Liu Exploring the limits of transfer learning with a unified text-to-text transformer. Journal of machine learning research 21 (140), pp. 1–67. Cited by: cite145†Appendix C .
L1194:   * Saha et al. (2024) R. Saha, N. Sagan, V. Srivastava, A. Goldsmith, and M. Pilanci Compressing large language models using low rank and low precision decomposition. Advances in Neural Information Processing Systems 37, pp. 88981–89018. Cited by: cite112†Appendix C , cite150†§1 , cite138†item (b) , cite124†item (b) , cite139†§3.3 , cite122†§4.1 .
L1195:   * Sakaguchi et al. (2021) K. Sakaguchi, R. L. Bras, C. Bhagavatula, and Y. Choi Winogrande: an adversarial winograd schema challenge at scale. Communications of the ACM 64 (9), pp. 99–106. Cited by: cite151†3rd item , cite119†Appendix G , cite117†§4.1 .
L1196:   * Shao et al. (2023) W. Shao, M. Chen, Z. Zhang, P. Xu, L. Zhao, Z. Li, K. Zhang, P. Gao, Y. Qiao, and P. Luo Omniquant: omnidirectionally calibrated quantization for large language models. arXiv preprint arXiv:2308.13137. Cited by: cite145†Appendix C , cite112†Appendix C , cite121†item (a) , cite152†item (a) , cite122†§4.1 .
L1197:   * Touvron et al. (2023) H. Touvron, L. Martin, K. Stone, P. Albert, A. Almahairi, Y. Babaei, N. Bashlykov, S. Batra, P. Bhargava, S. Bhosale, et al. Llama 2: open foundation and fine-tuned chat models. arXiv preprint arXiv:2307.09288. Cited by: cite136†§4.1 .
L1198:   * Tseng et al. (2024) A. Tseng, J. Chee, Q. Sun, V. Kuleshov, and C. De Sa QuIP# : even better llm quantization with hadamard incoherence and lattice codebooks. In Forty-first International Conference on Machine Learning, Cited by: cite112†Appendix C , cite138†item (b) , cite113†item (b) , cite122†§4.1 , cite149†§4.4 .
L1199:   * Van Baalen et al. (2024) M. Van Baalen, A. Kuzmin, I. Koryakovskiy, M. Nagel, P. Couperus, C. Bastoul, E. Mahurin, T. Blankevoort, and P. Whatmough Gptvq: the blessing of dimensionality for llm quantization. arXiv preprint arXiv:2402.15319. Cited by: cite112†Appendix C , cite126†item (c) , cite122†§4.1 .
L1200:   * Viazovska (2017) M. S. Viazovska The sphere packing problem in dimension 8. Annals of mathematics, pp. 991–1015. Cited by: cite126†item (c) .
L1201:   * Zellers et al. (2019) R. Zellers, A. Holtzman, Y. Bisk, A. Farhadi, and Y. Choi Hellaswag: can a machine really finish your sentence?. arXiv preprint arXiv:1905.07830. Cited by: cite153†5th item , cite111†Appendix E , cite119†Appendix G .
L1202:   * Zhang et al. (2024a) C. Zhang, J. Cheng, G. A. Constantinides, and Y. Zhao LQER: low-rank quantization error reconstruction for llms. arXiv preprint arXiv:2402.02446. Cited by: cite112†Appendix C , cite125†§1 , cite140†§1 , cite126†item (c) , cite124†item (b) , cite139†§3.3 , cite122†§4.1 .
L1203:   * Zhang et al. (2024b) C. Zhang, J. T. Wong, C. Xiao, G. A. Constantinides, and Y. Zhao Qera: an analytical framework for quantization error reconstruction. arXiv preprint arXiv:2410.06040. Cited by: cite125†§1 , cite138†item (b) .
L1204:   * Zheng et al. (2024) L. Zheng, L. Yin, Z. Xie, C. L. Sun, J. Huang, C. H. Yu, S. Cao, C. Kozyrakis, I. Stoica, J. E. Gonzalez, et al. Sglang: efficient execution of structured language model programs. Advances in neural information processing systems 37, pp. 62557–62583. Cited by: cite125†§1 .
L1205: ###### Contents
L1206:   1. cite6†1 Introduction L1207:   2. cite7†2 Related Works L1208:   3. cite8†3 Method L1209:     1. cite9†3.1 Problem Statement L1210:     2. cite10†3.2 Partial Rotation quantization under permutation L1211:     3. cite11†3.3 A Light Low-Rank Algorithm by Randomized Sketching L1212:     4. cite12†3.4 Algorithm Analysis L1213:   4. cite13†4 Evaluation L1214:     1. cite14†4.1 Experiment Setup L1215:     2. cite15†4.2 Main Results L1216:     3. cite16†4.3 Quantization Cost L1217:     4. cite17†4.4 Inference efficiency L1218:     5. cite18†4.5 Ablation Studies L1219:   5. cite19†5 Additional Experiments L1220:   6. cite20†6 Conclusion L1221:   7. cite21†References L1222:   8. cite22†A LoPRo Details: L1223:     1. cite23†A.1 Algorithm pseudo-code L1224:     2. cite24†A.2 Average Bit-width L1225:     3. cite25†A.3 Time Complexity L1226:     4. cite26†A.4 Permutation L1227:   9. cite27†B Proofs L1228:     1. cite28†B.1 Notations and Assumptions L1229:     2. cite29†B.2 Proof 1. Quantization under Rotation L1230:     3. cite30†B.3 Proof 2. Quantization with hessian after rotation L1231:   10. cite31†C Additional Implementation Details L1232:   11. cite32†D Extended Ablation Studies L1233:     1. cite33†D.1 Ablation on rank L1234:     2. cite34†D.2 Ablation on Low-rank Decomposition L1235:     3. cite35†D.3 Ablation on iteration L1236:     4. cite36†D.4 Ablation on block size L1237:     5. cite37†D.5 Ablation on Calibration dataset L1238:   12. cite38†E Moe results L1239:   13. cite39†F Qwen Results L1240:   14. cite40†G Open LLM Leaderboard V1 L1241:   15. cite41†H Limitations L1242:   16. cite42†I Broader Impacts L1243:   17. cite43†J LLMs usage L1244:   18. cite44†K More Visualization L1245: Table 6: Symbols and Description in this paper.
L1246: Symbols  | Description
L1247: $\displaystyle\bm{W}$  | The weight matrix $\bm{W}\in\mathbb{R}^{m\times n}.$
L1248: $\displaystyle\bm{X}$  | The input of each linear layer
L1249: $\displaystyle\mathcal{Q}$  | Quantization function
L1250: $\displaystyle\hat{\bm{W}}$  | A pseudo quantized matrix
L1251: $\displaystyle\bm{H}$  | A proxy hessian equal to $E_{\bm{X}}[\bm{X}\bm{X}^{T}]$
L1252: H  | A Hadamard matrix
L1253: $\bm{W}_{r}=\bm{U}\bm{\Sigma}\bm{V}$  | The rank-r approximate matrix of $\bm{W}$
L1254: $\mathcal{L}(\cdot)$  | The loss function, we use the proxy Hessian in this paper.
L1255: $\bm{R}$  | The residual matrix of low-rank approximation $\bm{R}=\bm{W}-\bm{W_{r}}$
L1256: $\textbf{H}_{wal}$  | Walsh-Hadamard matrix
L1257: $\bm{Q}$  | The partial block Walsh-Hadamard matrix
L1258: $\bm{P}$  | The permutation matrix from index vector $perm$.
L1259: $\bm{I}$  | An identity matrix
L1260: $\bm{E}$  | The error matrix under quantization $\bm{E}=\bm{W}-\bm{\hat{W}}$.
L1261: $\mathcal{O}(\cdot)$  | The upper bound of time complexity


## jan29_systemfour_set2

LoPRo: Enhancing Low-Rank Quantization via Permuted Block-Wise Rotation (https://arxiv.org/html/2601.19675v1)
citeturn28519view3 [wordlim: 200] Crawled: today; Content type: text/html; Source: open({"ref_id":"https://arxiv.org/html/2601.19675v1","lineno":250}); Total lines: 1846
L228: ### 3.4 Algorithm Analysis
L229: 
L230: In this section, we analyze LoPRo from:
L231: 
L232:   * •
L233: 
L234: Compression Ratio: Consider a weight matrix $\bm{W}\in\mathbb{R}^{m\times n}$ with an original precision $d_{o}$ (in bits), quantized to a target precision $d_{q}$ with group size $g$. The low-rank components of rank $r$ are stored in precision $d_{r}$. Then, the overall average compression bit $d_{C}$ is given by:
L235:  | $$d_{C}=\overbrace{d_{q}+\frac{d_{o}}{g}}^{Quant\ \bm{W}}+\overbrace{\frac{rd_{r}}{n}+\frac{rd_{r}}{m}}^{\bm{U}\ \ \text{and}\ \ \bm{V}}+\overbrace{\frac{2d_{o}}{n}}^{\ \alpha\text{\ and}\ \bm{P}}+\overbrace{\frac{rd_{o}}{mn}}^{\bm{\Sigma}}.$$  |  | (13)
L236: 
L237: We provide a detailed analysis and proof in Appendix cite24†A.2 .
L238: 
L239:   * •
L240: Inference Latency: Assume the weight is square and the input is $\mathbf{X}\in\mathbb{R}^{n\times b}$. Therefore, the total inference latency complexity $C$ is shown in Eq cite94†13 and detailed in Appendix cite25†A.3 :
L241: 
L242:  | $$C=\mathcal{O}\bigl(nb(2r+1+\log b_{H})\bigr).$$  |  | (14)
L243: 
L244: This shows that the additional latency grows linearly with the batch size $b$ and is manageable for small $r$ and moderate $b_{H}$, making the method suitable for efficient deployment.
L245: ## 4 Evaluation
L246: ### 4.1 Experiment Setup
L247: 
L248: Models: Evaluations are carried out on the LLaMA-2 and LLaMA-3 dense model families cite95†Touvron et al. (2023) and Mixture of Experts (MoE) model Mixtral-8x7B cite96†Jiang et al. (2024) .
L249: Baseline: Following the classification introduced in §cite7†2 , we conduct a comprehensive comparison with the state-of-the-art (SOTA) PTQs within each class. Fine-tuning-free methods include: GPTQ cite50†Frantar et al. (2023) , GPTVQ cite73†Van Baalen et al. (2024) , OmniQuant cite63†Shao et al. (2023) , QuIP# cite66†Tseng et al. (2024) , LQER cite55†Zhang et al. (2024a) , and MoEQuant cite64†Chen et al.
L250: (2025) ^{1}^{1} 1 The implementation of MoEQuant is now unavailable, it does not report results on several datasets used in our main experiments. To ensure a comprehensive comparison, we provide additional evaluation in Appendix cite38†E .. Additionally, we compare with fine-tuning-based methods such as QuIP# and CALDERA cite57†Saha et al. (2024) .
L251: These methods are categorized according to §cite7†2 , with tags $\mathord{\vbox{\hbox{\hbox to5.17pt{\vbox to6.46pt{\pgfpicture\makeatletter\hbox{\hskip 0.0pt\lower 0.0pt\hbox to0.0pt{\lxSVG@begingroup@{_scopebegin=1} \lxSVG@begingroup@{stroke=#000000} \lxSVG@begingroup@{fill=#000000} \lxSVG@setlinewidth{\the\pgflinewidth}\lxSVG@begingroup@{stroke-width=0.4pt} \lx@inpgf@ignorespaces\nullfont\hbox to0.0pt{\lxSVG@begingroup@{_scopebegin=1} {\lx@inpgf@ignorespaces}\lx@inpgf@ignorespaces{\lx@inpgf@ignorespaces}\lx@inpgf@ignorespaces  {}{{}}{}
L252: {{}{}}{{}}{}{}{}{}{{}}{}\lxSVG@begingroup@{_scopebegin=1} \color[rgb]{0.7773,0.1016,0.1016}\lxSVG@fill\lxSVG@drawpath@unclipped{M 0 0 M 0 0 L 0 8.94 L 3.57 8.94 L 3.57 0 Z M 3.57 8.94}{stroke:none} \lx@inpgf@ignorespaces
L253: \lxSVG@closescope {}{{}}{}
L254: {{}{}}{{}}{}{}{}{}{{}}{}\lxSVG@begingroup@{_scopebegin=1} \color[rgb]{0.9023,0.2891,0.2891}\lxSVG@fill\lxSVG@drawpath@unclipped{M 3.57 0 M 3.57 0 L 3.57 8.94 L 7.15 8.94 L 7.15 0 Z M 7.15 8.94}{stroke:none} \lx@inpgf@ignorespaces
L255: \lxSVG@closescope
L256: \lxSVG@closescope {\lx@inpgf@ignorespaces}{\lx@inpgf@ignorespaces}{\lx@inpgf@ignorespaces}\hss}\lxSVG@discardpath\lxSVG@closescope \hss}}\lxSVG@closescope\endpgfpicture}}}}}$ stand for cite7†¶O1.a,b ; $\mathord{\vbox{\hbox{\hbox to7.75pt{\vbox to6.46pt{\pgfpicture\makeatletter\hbox{\hskip 0.0pt\lower 0.0pt\hbox to0.0pt{\lxSVG@begingroup@{_scopebegin=1} \lxSVG@begingroup@{stroke=#000000} \lxSVG@begingroup@{fill=#000000} \lxSVG@setlinewidth{\the\pgflinewidth}\lxSVG@begingroup@{stroke-width=0.4pt} \lx@inpgf@ignorespaces\nullfont\hbox to0.0pt{\lxSVG@begingroup@{_scopebegin=1} {\lx@inpgf@ignorespaces}\lx@inpgf@ignorespaces{\lx@inpgf@ignorespaces}\lx@inpgf@ignorespaces  {}{{}}{}
L257: {{}{}}{{}}{}{}{}{}{{}}{}\lxSVG@begingroup@{_scopebegin=1} \color[rgb]{0.9844,0.5117,0.457}\lxSVG@fill\lxSVG@drawpath@unclipped{M 0 0 M 0 0 L 0 8.94 L 3.57 8.94 L 3.57 0 Z M 3.57 8.94}{stroke:none} \lx@inpgf@ignorespaces
L258: \lxSVG@closescope {}{{}}{}
L259: {{}{}}{{}}{}{}{}{}{{}}{}\lxSVG@begingroup@{_scopebegin=1} \color[rgb]{0.9883,0.7148,0.418}\lxSVG@fill\lxSVG@drawpath@unclipped{M 3.57 0 M 3.57 0 L 3.57 8.94 L 7.15 8.94 L 7.15 0 Z M 7.15 8.94}{stroke:none} \lx@inpgf@ignorespaces
L260: \lxSVG@closescope {}{{}}{}
L261: {{}{}}{{}}{}{}{}{}{{}}{}\lxSVG@begingroup@{_scopebegin=1} \color[rgb]{1,0.8789,0.5898}\lxSVG@fill\lxSVG@drawpath@unclipped{M 7.15 0 M 7.15 0 L 7.15 8.94 L 10.72 8.94 L 10.72 0 Z M 10.72 8.94}{stroke:none} \lx@inpgf@ignorespaces
L262: \lxSVG@closescope
L263: \lxSVG@closescope {\lx@inpgf@ignorespaces}{\lx@inpgf@ignorespaces}{\lx@inpgf@ignorespaces}\hss}\lxSVG@discardpath\lxSVG@closescope \hss}}\lxSVG@closescope\endpgfpicture}}}}}$ stand for cite7†¶F1.a,b,c ; and $\mathord{\vbox{\hbox{\hbox to5.17pt{\vbox to6.46pt{\pgfpicture\makeatletter\hbox{\hskip 0.0pt\lower 0.0pt\hbox to0.0pt{\lxSVG@begingroup@{_scopebegin=1} \lxSVG@begingroup@{stroke=#000000} \lxSVG@begingroup@{fill=#000000} \lxSVG@setlinewidth{\the\pgflinewidth}\lxSVG@begingroup@{stroke-width=0.4pt} \lx@inpgf@ignorespaces\nullfont\hbox to0.0pt{\lxSVG@begingroup@{_scopebegin=1} {\lx@inpgf@ignorespaces}\lx@inpgf@ignorespaces{\lx@inpgf@ignorespaces}\lx@inpgf@ignorespaces  {}{{}}{}
L264: {{}{}}{{}}{}{}{}{}{{}}{}\lxSVG@begingroup@{_scopebegin=1} \color[rgb]{0.2656,0.4609,0.7031}\lxSVG@fill\lxSVG@drawpath@unclipped{M 0 0 M 0 0 L 0 8.94 L 3.57 8.94 L 3.57 0 Z M 3.57 8.94}{stroke:none} \lx@inpgf@ignorespaces
L265: \lxSVG@closescope {}{{}}{}
L266: {{}{}}{{}}{}{}{}{}{{}}{}\lxSVG@begingroup@{_scopebegin=1} \color[rgb]{0.4141,0.7344,0.9297}\lxSVG@fill\lxSVG@drawpath@unclipped{M 3.57 0 M 3.57 0 L 3.57 8.94 L 7.15 8.94 L 7.15 0 Z M 7.15 8.94}{stroke:none} \lx@inpgf@ignorespaces
L267: \lxSVG@closescope


## jan29_systemfour_last

LoPRo: Enhancing Low-Rank Quantization via Permuted Block-Wise Rotation (https://arxiv.org/html/2601.19675v1)
citeturn28521view1 [wordlim: 200] Crawled: today; Content type: text/html; Source: find({"ref_id":"https://arxiv.org/html/2601.19675v1","pattern":"4090"}); Total lines: 1846
No matching text found for "4090"

## jan29_lopro_hardware

LoPRo: Enhancing Low-Rank Quantization via Permuted Block-Wise Rotation (https://arxiv.org/html/2601.19675v1)
citeturn28522view0 [wordlim: 200] Crawled: today; Content type: text/html; Source: find({"ref_id":"https://arxiv.org/html/2601.19675v1","pattern":"A100"}); Total lines: 1846
L1566:  | $\displaystyle\mathcal{L}({{\bm{W}}})$  | $\displaystyle=\|\bm{R}\bm{Q}^{T}\tilde{\bm{X}}-\mathcal{Q}(\bm{R}\bm{Q}^{T})\tilde{\bm{X}}\|$  |  | (43)
L1567:  |  | $\displaystyle=\mathrm{tr}\left((\hat{\bm{R^{\prime}}}-\bm{R})\bm{H^{\prime}}(\hat{\bm{R^{\prime}}}-\bm{R})^{\top}\right),$  |  | (44)
L1568: 
L1569: In this case: $\bm{H^{\prime}}=\bm{Q}^{T}\bm{H}\bm{Q}$, take $\bm{Q}=\bm{P}\textbf{H}_{wal}$, we can prove the Eq cite90†9 .
L1570: ## Appendix C Additional Implementation Details
L1571: 
L1572: Set up: Experiments with the MoE model Mixtral-8x7B were conducted on a single NVIDIA A800 80GB GPU, while all other experiments were performed on a single NVIDIA A100 40GB GPU. The difference in hardware only leads to minor variations in quantization costs and inference latency; all accuracy metrics and other numerical results remain identical across platforms, ensuring fair and consistent evaluation.
L1573: Calibration: We use a calibration dataset consisting of 128 randomly sampled sequences, each containing 2048 tokens, from c4 cite162†Raffel et al. (2020) , a sampling strategy shown to be effective in OmniQuant cite63†Shao et al. (2023) and AffineQuant cite76†Ma et al. (2024) .
L1574: Evaluation: For the perplexity (PPL) evaluation, we set the context length to match the maximum sequence length used during model training: 4096 for LLaMA-2 and 8192 for LLaMA-3. In zero-shot evaluations, we report the acc metric (rather than acc_norm) from the lm-eval-harness cite101†Gao et al. (2024) . All results are rounded to one or two decimal places as appropriate. Here are brief introductions to the zero-shot datasets:
L1575: 
L1576:   * •
L1577: ARC-Challenge (AC) and ARC-Easy (AE)cite98†Boratko et al. (2018) : The AI2 Reasoning Challenge (ARC) dataset consists of multiple-choice science questions from grade school level. ARC-Challenge contains questions that are difficult for both retrieval and word co-occurrence methods, focusing on genuine reasoning, while ARC-Easy includes questions that are more amenable to simpler methods.
L1578: 
L1579:   * •
L1790: These results confirm that LoPRo enables near-FP16 quality at 3-bit and usable performance at 2-bit across diverse Qwen architectures. The consistent gains from LoPRo_{v} further validate our design choice of incorporating activation variance into the routing mechanism. Combined with fast quantization runtime (empirically under 1 hour for all models on a single A100-40G), LoPRo offers a practical solution for deploying high-performance, compressed Qwen models in memory- and latency-constrained scenarios.
L1791: Table 13: Performance of LoPRo Qwen2 and Qwen3 model families.
L1792: Models  | Methods  | Q Config  | Wiki  | AC  | AE  | WI  | QA
L1793: Qwen2.5-7b  | Fp16  | W16A16  | 6.86  | 52.6  | 81.9  | 71.1  | 79.7
L1794: LoPRo  | W2A16  | 9.43  | 39.6  | 70.2  | 65.5  | 72.5
L1795: W3A16  | 7.22  | 51.2  | 82.9  | 70  | 78.8
L1796: LoPRo_v  | W2A16  | 8.53  | 44.1  | 68.6  | 68  | 75.4
L1797: W3A16  | 7.23  | 53.5  | 82.8  | 70.6  | 78.9
L1798: Qwen2.5-14b  | Fp16  | W16A16  | 5.24  | 60.7  | 85.7  | 75.6  | 81.6
L1799: LoPRo  | W2A16  | 7.75  | 47.4  | 76.7  | 71.9  | 75.7
L1800: W3A16  | 5.44  | 57.8  | 84.4  | 75  | 79.4
L1801: LoPRo_v  | W2A16  | 6.62  | 50.2  | 78.8  | 72.5  | 77.3
L1802: W3A16  | 5.42  | 57.2  | 83.9  | 74.7  | 70.8
L1803: Qwen3-8b  | Fp16  | W16A16  | 9.01  | 55.6  | 83.5  | 68.1  | 76.7
L1804: LoPRo  | W2A16  | 12.59  | 40.6  | 70.5  | 62.9  | 70.8
L1805: W3A16  | 9.58  | 52.9  | 81.7  | 66.9  | 75.9
L1806: LoPRo_v  | W2A16  | 11.22  | 47.9  | 77.8  | 66.9  | 72.4
L1807: W3A16  | 9.59  | 55.3  | 82.3  | 68.2  | 76


## jan29_lopro_hardware

LoPRo: Enhancing Low-Rank Quantization via Permuted Block-Wise Rotation (https://arxiv.org/html/2601.19675v1)
citeturn28522view1 [wordlim: 200] Crawled: today; Content type: text/html; Source: find({"ref_id":"https://arxiv.org/html/2601.19675v1","pattern":"calibration set"}); Total lines: 1846
L83: Extensive experiments show that our method delivers state-of-the-art quantization accuracy while also preserving the option for fine-tuning when necessary. Notably, under 3-bit scalar quantization, LoPRo achieves performance that even surpasses the fine-tuned results and maintains good scalability on Mixture-of-Experts (MoE) model.
L84: ## 2 Related Works
L85: In weight quantization, denote the original weight as $\bm{W}\in\mathbb{R}^{m{\times}n}$ and compressed into $\bm{\hat{W}}$ ; $\bm{X}\in\mathbb{R}^{n*k}$ is an input from a calibration set; the primary challenge lies in low-bit quantization at 3-bit and below. For PTQs, we summarize three key points that underlie their effectiveness.
L86: To align with the experimental setup, we use distinct colors $\mathord{\vbox{\hbox{\hbox to20.67pt{\vbox to6.46pt{\pgfpicture\makeatletter\hbox{\hskip 0.0pt\lower 0.0pt\hbox to0.0pt{\lxSVG@begingroup@{_scopebegin=1} \lxSVG@begingroup@{stroke=#000000} \lxSVG@begingroup@{fill=#000000} \lxSVG@setlinewidth{\the\pgflinewidth}\lxSVG@begingroup@{stroke-width=0.4pt} \lx@inpgf@ignorespaces\nullfont\hbox to0.0pt{\lxSVG@begingroup@{_scopebegin=1} {\lx@inpgf@ignorespaces}\lx@inpgf@ignorespaces{\lx@inpgf@ignorespaces}\lx@inpgf@ignorespaces   \par{}{{}}{}
L87: {{}{}}{{}}{}{}{}{}{{}}{}\lxSVG@begingroup@{_scopebegin=1} \color[rgb]{0.7773,0.1016,0.1016}\lxSVG@fill\lxSVG@drawpath@unclipped{M 0 0 M 0 0 L 0 8.94 L 3.57 8.94 L 3.57 0 Z M 3.57 8.94}{stroke:none} \lx@inpgf@ignorespaces
L88: \lxSVG@closescope {}{{}}{}
L89: {{}{}}{{}}{}{}{}{}{{}}{}\lxSVG@begingroup@{_scopebegin=1} \color[rgb]{0.9023,0.2891,0.2891}\lxSVG@fill\lxSVG@drawpath@unclipped{M 3.57 0 M 3.57 0 L 3.57 8.94 L 7.15 8.94 L 7.15 0 Z M 7.15 8.94}{stroke:none} \lx@inpgf@ignorespaces
L90: \lxSVG@closescope \par
L91: {}{{}}{}
L1308:        19 Quantize the resident matrix by methods like GPTQ/GPTVQ… by new loss: $\bm{W}_{q}=\mathcal{Q}(\bm{R}^{\prime})\ ,\mathcal{L}(\bm{R})=\text{tr}\left((\hat{\bm{R}}-\bm{R})\bm{H}^{\prime}(\hat{\bm{R}}-\bm{R})^{T}\right)$, $\bm{H}^{\prime}=\bm{Q}^{T}\bm{P}^{T}\bm{H}\bm{P}\bm{Q}$;
L1309: 
L1310:        20 Add quantization results:$qlayer.add(\bm{W}_{q},\bm{U},\bm{V},\bm{\Sigma},p,s)$;
L1311: 
L1312:     21 end for
L1313: 
L1314:     22 Save the layer result: $QModule.layer[name]=qlayer$
L1315: 
L1316: 23 end for
L1317: 
L1318: 24 return $QModule$;
L1319: In this section, we provide a detailed description of the LoPRo execution pipeline,
L1320: ### A.1 Algorithm pseudo-code
L1321: 
L1322: The workflow of LoPRo is outlined in Algorithm cite154†1 :
L1323: 
L1324: Stage A. Low-Rank Approximation under Calibration Set:
L1325: 
L1326:   1. 1.
L1327: 
L1328: Perform forward inference on the calibration dataset to collect layer-wise input activations $\bm{X}$ corresponding to each weight matrix $\bm{W}$ (line 1-4).
L1329: 
L1330:   2. 2.
L1331: 
L1332: Compute the importance-aware scaling vector with the activations $\bm{X}$ (line 5-6).
L1333: 
L1334:   3. 3.
L1335: 
L1336: Apply the scaling to $\bm{W}$, obtaining scaled weight (line 7).
L1337: 
L1338:   4. 4.
L1339: Draw a sketch vector and form exponentiation to the Gram matrix (line 8-10).
L1340: 
L1341:   5. 5.
L1342: 
L1343: Calculate the rank-1 matrix according to Eq cite155†12 , and update the matrix for low-rank approximation (line 11-14).
L1344: 
L1345: Stage B. Structured Residual Rotation:
L1346: 
L1347:   1. 6.
L1348: 
L1349: Compute the permutation array according to Eq cite87†5 , which groups columns by importance; then construct the corresponding permutation matrix $\bm{P}$ (line 15-17).
L1350: 
L1351:   2. 7.
L1352: Apply the block-wise partial Hadamard transformation to the residual matrix to minimize quantization error (line 18).
L1353: 
L1354: Stage C. Quantization of Transformed Residual:
L1355: 
L1356:   1. 8.
L1357: 
L1358: Quantize the rotated residual matrix $\bm{R}^{\prime}$ by quantization tools (e.g., GPTQ for scalar quantization or GPTVQ for vector quantization) (line 19).
L1359: 
L1360:   2. 9.
L1361: Save the final quantized components: $\bm{W}_{q}$, $\bm{U}$, $\bm{\Sigma}$, $\bm{V}$, scaling vector $\bm{a}$, and permutation index $\bm{p}$, for deployment (line 20-22).
L1763: ### D.5 Ablation on Calibration dataset
L1764: 
L1765: Table 11: Ablation on calibration dataset in 2bit LLaMA2-7B quantization..
L1766: Method  | Dataset  | PPL  | AC  | AE  | QA  | WI
L1767: LoPRo  | Wiki2  | 7.49  | 32.9  | 64.1  | 70.2  | 64.5
L1768: LoPRo  | C4  | 7.39  | 31.2  | 62.8  | 71.1  | 63.8
L1769:  | Pile  | 7.46  | 31.6  | 64.3  | 70.2  | 64.9
L1770: LoPRo_{v}  | Wiki2  | 6.55  | 34.1  | 69.8  | 73.2  | 65.9
L1771: LoPRo_{v}  | C4  | 6.53  | 34.6  | 69.0  | 72.7  | 66.5
L1772:  | Pile  | 6.52  | 34.0  | 69.4  | 73.9  | 65.4
L1773: We evaluated the quantization performance of LoPRo in different calibration datasets, with results presented in Table cite171†11 . The results demonstrate that LoPRo maintains consistent performance advantages across WikiText-2, c4, Pile with minimal metric fluctuations. This indicates strong generalization capability across diverse domains and text styles, and confirms that LoPRo is not sensitive to the specific statistical properties of any single calibration set.
L1774: This robustness aligns with the design philosophy of LoPRo as a fine-tuning-free quantization framework. Consequently, for all other experiments in this work, we adopt c4 as the default calibration dataset.
L1775: ## Appendix E Moe results
L1776: 
L1777: Since the MoEQuant cite64†Chen et al. (2025) paper neither reports results on several Zero-Shot benchmarks used in our main experiments nor provides open-source code, we introduce additional evaluation datasets — including BoolQ (BQ) cite163†Clark et al. (2019) , Hellaswag (HS) cite164†Zellers et al. (2019) , OpenbookQA (OB) cite165†Mihaylov et al. (2018) , MathQA (MQ) cite166†Amini et al. (2019) to ensure a fair and comprehensive comparison. Results are summarized in Table cite172†12 .
L1778: Comparison with MoEQuant: LoPRo consistently outperforms MoEQuant across all evaluation tasks. Notably, under 2-bit quantization, LoPRo matches or exceeds the accuracy of MoEQuant at 3-bit precision — validating the trend observed in our main experiments. Specifically, on the BoolQ dataset, LoPRo achieves a +6 point improvement in accuracy; on other benchmarks, it performs comparably or better, while also exhibiting lower perplexity (i.e., reduced ambiguity).

