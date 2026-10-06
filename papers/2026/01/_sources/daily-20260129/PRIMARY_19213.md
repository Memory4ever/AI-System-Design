# Exact-v1 primary excerpts — 19213

L labels are local to each separated original response. Preserved necessary-source tool responses; no reproduction.

## Original response: stdnext3head

M^"2"XFP: A Metadata-Augmented Microscaling Data Format for Efficient Low-bit Quantization (https://arxiv.org/html/2601.19213v1)
citeturn28405view0 [wordlim: 200] Crawled: today; Content type: text/html; Source: open({"ref_id":"https://arxiv.org/html/2601.19213v1","lineno":null}); Total lines: 558
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
L14: cite1†Why HTML?†info.arxiv.org cite2†Report Issue cite3†Back to Abstract cite4†Download PDF L15:   1. cite5†Abstract. L16:   2. cite6†1 Introduction L17:   3. cite7†2 Background L18:     1. cite8†2.1 Model Quantization L19:     2. cite9†2.2 Microscaling Data Format L20:   4. cite10†3 Motivation L21:     1. cite11†3.1 Analysis of MX Quantization Error L22:     2. cite12†3.2 A Taxonomy of Quantization Design Dimensions L23:       1. cite13†3.2.1 Scaling Factor: Converging Toward Group-Level E8M0/FP8 L24:       2. cite14†3.2.2 Data Type: Expressive but Hardware-Prohibitive L25:       3. cite15†3.2.3 Metadata: A Flexible Yet Underutilized Design Axis L26:     3. cite16†3.3 Takeaway: Metadata as the Key Lever L27:   5. cite17†4 M${}^{\text{2}}$XFP Analysis and Design L28:     1. cite18†4.1 Framework for Design Space Exploration L29:     2. cite19†4.2 Pareto-Optimal Analysis of Metadata Strategies L30:       1. cite20†4.2.1 Evaluation Method L31:       2. cite21†4.2.2 Fixed Shared Scale Result (Fig. ). L32:       3. cite22†4.2.3 Adatpive Shared Scale Result (Fig. ). L33:       4. cite23†4.2.4 Key Takeaway. L34:     3. cite24†4.3 M${}^{\text{2}}$XFP Design: A Hybrid Strategy L35:     4. cite25†4.4 Quantization and Encoding Process L36:       1. cite26†4.4.1 Activation Quantization with Elem-EM L37:       2. cite27†4.4.2 Weight Quantization with Sg-EM L38:   6. cite28†5 Architecture L39:     1. cite29†5.1 Architecture Overview L40:     2. cite30†5.2 Memory Organization L41:     3. cite31†5.3 Decode Unit L42:     4. cite32†5.4 M${}^{\text{2}}$XFP Processing Element L43:     5. cite33†5.5 Quantization Engine. L44:   7. cite34†6 Evaluation L45:     1. cite35†6.1 Experimental Setup L46:     2. cite36†6.2 Large Language Model Evaluation L47:     3. cite37†6.3 Performance, Area, and Energy L48:     4. cite38†6.4 Analysis and Discussion L49:   8. cite39†7 Conclusion L50:     1. cite40†Acknowledgements L51:   9. cite41†References L52: cite42†License: CC BY 4.0†info.arxiv.org L53: 
L54: arXiv:2601.19213v1 [cs.AR] 27 Jan 2026
L55: # M${}^{\text{2}}$XFP: A Metadata-Augmented Microscaling Data Format for Efficient Low-bit Quantization
L56: Conference: Proceedings of the 31st ACM International Conference on Architectural Support for Programming Languages and Operating Systems, Volume 2; March 22–26, 2026; Pittsburgh, PA, USA Proceedings of the 31st ACM International Conference on Architectural Support for Programming Languages and Operating Systems, Volume 2 (ASPLOS ’26), March 22–26, 2026, Pittsburgh, PA, USA DOI: cite43†10.1145/3779212.3790185†doi.org ISBN: 979-8-4007-2359-9/2026/03 CCS: Computer systems organization Single instruction, multiple data CCS: Computer systems organization Systolic arrays CCS: Computer systems organization Neural networks
L57: Weiming Hu email: weiminghu@sjtu.edu.cn Affiliation: Shanghai Jiao Tong University, Shanghai, China Affiliation: Shanghai Qi Zhi Institute, Shanghai, China , Zihan Zhang email: tiancaizhangdaxian@sjtu.edu.cn Affiliation: Shanghai Jiao Tong University, Shanghai, China , Haoyan Zhang email: h.y.zhang-zdy@sjtu.edu.cn Affiliation: Shanghai Jiao Tong University, Shanghai, China Affiliation: Shanghai Qi Zhi Institute, Shanghai, China , Chen Zhang email: chenzhang.sjtu@sjtu.edu.cn Affiliation: Shanghai Jiao Tong University, Shanghai, China Note: Corresponding authors.
L58: , Cong Guo email: guocong@sjtu.edu.cn Affiliation: Shanghai Jiao Tong University, Shanghai, China , Yu Feng email: y-feng@sjtu.edu.cn Affiliation: Shanghai Jiao Tong University, Shanghai, China , Tianchi Hu email: hutianchi1@huawei.com Affiliation: Computing Product Line, Huawei, Shanghai, China , Guanglin Li email: liguanglin10@huawei.com Affiliation: Computing Product Line, Huawei, Shanghai, China , Guipeng Hu email: huguipeng@huawei.com Affiliation: Computing Product Line, Huawei, Shanghai, China , Junsong Wang email: junsongwang@huawei.com Affiliation: Computing Product Line, Huawei, Beijing, China and Jingwen Leng email: leng-jw@sjtu.edu.cn Affiliation: Shanghai Jiao Tong University, Shanghai, China Affiliation: Shanghai Qi Zhi Institute, Shanghai, China
L59: © cc
L60: ###### Abstract.
L61: Existing low-bit Microscaling (MX) formats, such as MXFP4, often suffer from substantial accuracy degradation due to the use of a shared scaling factor with the Power-of-Two format. In this work, we explore strategies that introduce minimal metadata to recover accuracy lost during quantization while maintaining high bit efficiency across a wide range of large language models.
L62: We propose a complete algorithm-hardware co-design based on flexible metadata, featuring an online quantization with simple encoding. To support the proposed method efficiently, we implement a lightweight hardware unit and integrate it into the accelerator. Evaluation results demonstrate that our method substantially narrows the accuracy gap, achieving on average a 70.63% reduction in accuracy loss compared to MXFP4 and a 37.30% reduction relative to the latest NVFP4 on LLM benchmarks.
L63: Furthermore, our design delivers up to 1.91$\times$ speedup and 1.75$\times$ energy savings over state-of-the-art accelerators. Our code is available at cite44†https://github.com/SJTU-ReArch-Group/M2XFP_ASPLOS26†github.com .
L64: ###### Keywords:
L65: 
L66: Low-bit Quantization; Microscaling Data Formats; Hardware Acceleration
L67: 
L68: ^{†}^{†}cc-license: by
L69: ## 1. Introduction
L70: Large language models (LLMs) have grown rapidly in scale and capability, with model size emerging as a primary driver of accuracy and generalization. State-of-the-art deployments now involve hundreds of billions of parameters, such as LLaMA-3.1 (cite45†Dubey et al., 2024 ), which contains up to 405 billion parameters. Storing these models in standard BF16 precision alone requires terabytes of main memory, far exceeding the capacity of commodity accelerators.
L71: The resulting memory and compute demands place tremendous stress on both cloud-scale and device-level systems, motivating aggressive model compression techniques (cite46†Lin et al., 2023 ; cite47†Frantar et al., 2023 ; cite48†Ashkboos et al., 2024 ; cite49†Frantar and Alistarh, 2023 ; cite50†Sun et al., 2024 ; cite51†Guan et al., 2024 ; cite52†Guan et al., 2022 ; cite53†Guo et al., 2020 ; cite54†Guo et al., 2024a ).
L72: Among these, low-bit quantization has emerged as a leading approach for reducing memory footprint, bandwidth consumption, and energy while preserving model quality, making it critical for the continued scaling of LLMs.
L73: Recent advances in low-bit quantization have led to the adoption of Microscaling (MX) formats  (cite55†Rouhani et al., 2023 ), which employ block-level shared scaling factors to enable fine-grained quantization. MX formats, such as MXFP4, have been widely adopted by industry and are natively supported in commercial accelerators, including NVIDIA’s B200 (cite56†Nvidia, 2024 ), AMD’s MI300 (cite57†Smith and Alla, 2024 ), and Microsoft’s Maia 100 (cite58†Xu and Ramakrishnan, 2024 ).
L74: By exploiting shared exponents and streamlined dequantization, these formats deliver high throughput with minimal hardware overhead. However, accuracy degradation remains severe at 4-bit precision: the coarse resolution of power-of-two (E8M0) scaling misaligns with the local maximum, leading to significant rounding error, while more precise FP8 scaling (e.g., NVFP4) narrows dynamic range and requires additional rescaling(cite59†Jang and Tambe, 2025 ).
L75: Other attempts, such as custom data types (cite60†Guo et al., 2022b ; cite61†Dettmers et al., 2023 ; cite62†Hu et al., 2025 ; cite63†Chen et al., 2025 ; cite64†Ramachandran et al., 2025 ), offer expressiveness but incur prohibitive hardware cost, especially for dynamic activations.
L76: These limitations highlight a critical research gap: while scaling factor design has largely converged and data type innovations face scalability bottlenecks, the metadata axis remains relatively underexplored. Metadata, in principle, provides a flexible way to encode auxiliary precision or range information without altering the core data path, thereby enhancing quantization fidelity at low cost. Yet existing approaches remain fragmented.
L77: Outlier-oriented schemes (e.g., OliVe (cite65†Guo et al., 2023 )) improve accuracy in tensor-wise settings but break down in group-wise MX formats, while structural metadata (e.g., MicroScopiQ (cite55†Rouhani et al., 2023 )) incurs excessive overhead, often exceeding 40 bits per block. Consequently, MX formats today either sacrifice accuracy for efficiency or burden hardware with metadata complexity, leaving a wide unexplored design space.
L78: This motivates the central question of our work: Can lightweight, principled metadata augmentation reconcile MX’s efficiency with the accuracy demands of 4-bit LLM quantization? Our exploration therefore focuses on the metadata axis as the primary remaining degree of freedom to close the 4-bit accuracy gap.
L79: To answer this, we propose M${}^{\text{2}}$XFP (Metadata-Augmented Microscaling Format), an algorithm–hardware co-design framework that systematically explores metadata allocation strategies. Our key insight is that metadata can serve as extra mantissa or exponent bits, enabling distinct trade-offs between precision refinement and range extension.
L80: Through a comprehensive design space exploration, we uncover a fundamental asymmetry: element-level metadata is most effective for dynamic activations, where lightweight, real-time encoding is essential, while subgroup-level metadata combined with scale search best serves static weights, where offline optimization is feasible. Building on this observation, we introduce a hybrid metadata scheme that applies element-level encoding to activations and subgroup-level encoding to weights.
L81: The resulting format improves bit efficiency with only 0.25 bits of metadata per element, delivering near-FP16 accuracy at effective 4.5-bit precision. We further design lightweight hardware support, integrated into systolic arrays with minimal extensions, that enables real-time metadata handling without disrupting the GEMM pipeline.
L82: This paper makes the following contributions:
L83: 
L84:   * •
L85: 
L86: We introduce a taxonomy of MX design dimensions (scaling factor, data type, metadata). Unlike prior work that primarily varies scaling factors or base data types, we perform an EBW-guided design space exploration along the under-explored metadata axis, covering both element-level and subgroup-level metadata under fixed and adaptive shared scales.
L87: 
L88:   * •
L89: We identify an asymmetric behavior between weights and activations and propose M${}^{\text{2}}$XFP, a hybrid metadata-augmented MX format that uses element-level extra mantissa for activations and subgroup-level mantissa refinement with adaptive shared scales for weights.
L90: 
L91:   * •
L92: We design a hardware-efficient accelerator integration including a top-1 decode unit, an augmented FP4$\times$FP4 PE, and a streaming quantization engine, and show that M${}^{\text{2}}$XFP outperforms state-of-the-art MX accelerators in both accuracy and performance/energy at negligible area cost.
L93: ## 2. Background
L94: ### 2.1. Model Quantization
L95: Quantization (cite46†Lin et al., 2023 ; cite47†Frantar et al., 2023 ; cite48†Ashkboos et al., 2024 ; cite66†Shao et al., 2024 ; cite67†Tseng et al., 2024 ; cite61†Dettmers et al., 2023 ; cite68†Lee et al., 2024 ; cite63†Chen et al., 2025 ; cite65†Guo et al., 2023 ; cite69†Liu et al., 2025b ; cite70†Lin et al., 2024 ; cite71†Guo et al., 2022a ) is a widely used technique for improving computational and memory efficiency by representing parameters with fewer bits.
L96: The standard approach maps a full-precision tensor $\mathbf{X}\in\mathbb{R}^{n}$ to a low-precision grid via a single affine transformation. Formally, for a target integer or floating point type with $k$-bit codes having dynamic range $[-Q_{\max},Q_{\max}]$, each element is quantized as
L97: (1)  |  | $$\tilde{x}_{i}=\text{round}\!\left(\frac{x_{i}}{s}\right),\quad s=\frac{\max(|\mathbf{X}|)}{Q_{\max}},$$  |
L98: 
L99: where $s$ is the per-tensor scaling factor and $\tilde{x}_{i}$ is stored as a $k$-bit integer or floating-point value.
L100: Outliers are the primary cause of quantization error. To mitigate the impact of outliers, recent studies (cite72†Zhao et al., 2023 ; cite46†Lin et al., 2023 ; cite73†Dai et al., 2021 ; cite47†Frantar et al., 2023 ) reduce the quantization granularity from the tensor or channel level to finer groups. This approach, known as group-wise quantization, partitions the tensor’s weights into small, fixed-size blocks (e.g., 64 or 128 values).
L101: Each block is quantized independently with its own unique scaling factor, effectively isolating the impact of any outliers within that small region.
L102: ### 2.2. Microscaling Data Format
L103: Microscaling (MX) is an emerging low-bit data format widely supported by existing hardware (cite56†Nvidia, 2024 ; cite58†Xu and Ramakrishnan, 2024 ; cite57†Smith and Alla, 2024 ), and has been extensively studied and applied in recent works (cite74†Mishra et al., 2025 ; cite75†Yang et al., 2025 ; cite64†Ramachandran et al., 2025 ; cite76†Fang et al., 2025 ; cite77†Lee et al., 2025b ; cite78†Cuyckens et al., 2025 ; cite79†Sharify et al., 2024 ; cite80†Lee et al., 2025a ; cite81†Koo et al., 2024 ; cite82†Gil et al., 2025 ; cite83†Cook et al., 2025 ; cite84†Zhang et al., 2025 ; cite85†Lo et al., 2023 ; cite86†Khodamoradi et al., 2024 ; cite87†Lo and Liu, 2023 ).
L104: In this section, we introduce the standard MX format along with several of its variants. Notably, the MX format naturally embraces group-wise quantization.
L105: Open Compute Project (OCP) Microscaling. Microscaling (MX) is a block floating-point format defined by the Open Compute Project (OCP)(cite55†Rouhani et al., 2023 ). As shown in Fig. cite88†1 , $k$ scalar elements share a common 8-bit scale factor.
L106: Unlike traditional group-wise quantization, where the scaling factor is FP16, the MX format restricts its scaling factor to the E8M0 format, a power-of-two representation with 8 exponent and 0 mantissa bits, making it particularly hardware-friendly for both quantization and dequantization processes.
L107: The shared scale is derived from the block maximum $x_{\max}=\max_{i}|V_{i}|$. Following the OCP specification (cite55†Rouhani et al., 2023 ), the exponent of the shared scale is computed as $S=2^{\lfloor\log_{2}(x_{\max}/P)\rfloor}$, where $P$ is the largest power-of-two representable in the target format (e.g., $P=4$ for FP4).
L108: Recent works propose alternatives such as using $S=2^{\lceil\log_{2}(x_{\max}/M)\rceil}$ instead to reduce clipping (cite74†Mishra et al., 2025 ), where $M$ is the maximum representable value (e.g., $M=6$ for FP4), or incorporating rounding strategies like $S=2^{\lfloor\log_{2}(\text{Round}(x_{\max})/P)\rfloor}$ (cite75†Yang et al., 2025 ) to reduce systematic bias in scale selection. In this paper, we adopt the OCP-compliant floor-based method, and we will compare different scale calculations later.
L109: The MX format quantization process can be simplified as a shift-and-rounding operation. For each element, its exponent is reduced by the shared exponent, which corresponds to a shift operation. Subsequently, the mantissa is rounded. The MX format dequantization process is seamlessly integrated into the General Matrix Multiplication (GEMM) operation in the latest modern GPUs (cite56†Nvidia, 2024 ).
L110: Compared to conventional group-wise quantization, the dequantization process in MX format is more efficient and hardware-friendly.
L111: Figure 1. Microscaling data format.
L112: Variants of the Microscaling Format. Several variants of the MX format exist, all sharing a common feature: a shared scaling factor (cite89†Darvish Rouhani et al., 2020 ; cite90†Darvish Rouhani et al., 2023 ). The concept of block floating-point (BFP), also known as Microsoft Floating Point (MSFP) (cite89†Darvish Rouhani et al., 2020 ), was introduced by the Brain Project.
L113: Fig. cite88†1 illustrates the MSFP-12 and MSFP-16 formats, where the numbers 12 and 16 refer to the combined bit widths of the scalar element and the shared scaling factor.
L114: Microsoft and Meta have proposed Shared Microexponents (denoted as SMX in this paper) (cite90†Darvish Rouhani et al., 2023 ), which is a novel 2-level shared MX format. The key distinction in this variant is that $k_{2}$ neighboring elements within share a 1-bit exponent, in addition to the 8-bit shared scaling factor by $k_{1}$ elements in a group. Typically, $k_{1}$ is 16 and $k_{2}$ is 2. The SMX family includes SMX4, SMX6, and SMX9, with differences in the mantissa bit width.
L115: The number in the SMX format name corresponds to the combined bit width of the sign, shared exponent, and mantissa.
L116: Recently, NVIDIA introduced NVFP, replacing the E8M0 scaling factor with the FP8 (E4M3) scaling factor. While FP8 scaling is more precise than E8M0, it has a reduced range, as the 4-bit exponent cannot cover the range of FP16. To compensate for this reduced range, NVIDIA proposes a tensor-level scaling factor to adjust the original tensor’s distribution, making the FP8 scale factors more practical. This adjustment helps reduce quantization error by enhancing the precision of the scaling factor.
L117: The 5th-generation tensor cores in NVIDIA’s Blackwell architecture (cite56†Nvidia, 2024 ) support both MXFP4 and NVFP4.
L118: Key Takeaway. Model quantization has evolved from coarse tensor-level schemes to fine-grained block-level formats, with Microscaling (MX) becoming the de facto hardware standard. MX achieves high throughput by exploiting shared power-of-two scaling and streamlined dequantization, and it has been widely adopted in commercial accelerators.
L119: However, this very reliance on a single shared scaling factor per block becomes a critical accuracy bottleneck at 4-bit precision, especially for LLM workloads where outliers dominate local dynamic ranges. Existing MX variants, e.g., MSFP, SMX, and NVFP, partially alleviate this issue but remain constrained by the same structural limitation, leading to either bit inefficiency or insufficient fidelity.
L120: This gap motivates a deeper investigation into the design space of MX quantization, particularly exploring whether lightweight metadata augmentation can bridge the trade-off between bit efficiency and model accuracy. The next section analyzes the root causes of quantization error in MX formats and categorizes recent architectural optimizations, laying the groundwork for our proposed M${}^{\text{2}}$XFP design.
L121: ## 3. Motivation
L122: 
L123: In this section, we first analyze the root causes behind the significant quantization error observed in low-bit MX formats. We then summarize recent architectural optimizations designed to improve quantization performance in Sec. cite12†3.2 . Based on this, we categorize several optimization settings and evaluate them across different LLMs to identify the most effective configuration for MXFP.
L124: 
L125: Figure 2. FP4 quantization: A comparison of FP16 and E8M0 scaling factors.
L126: ### 3.1. Analysis of MX Quantization Error
L127: Low-bit MX formats suffer from significant accuracy degradation because their shared power-of-two scaling cannot precisely align with block maximum (cite77†Lee et al., 2025b ). As illustrated in Fig. cite91†2 , FP16-based scaling maps the maximum element of a group tightly to the FP4 maximum point, minimizing quantization error. In contrast, MX’s E8M0 scaling only provides coarse power-of-two steps.
L128: When the group maximum falls between two exponent bins, the misalignment produces large rounding errors on the dominant value itself, which then propagates to the entire block.
L129: We empirically validate this phenomenon by quantizing several LLMs with FP4, MXFP4, NVFP4, and SMX4, as shown in Fig. cite92†4 . Both MXFP4 and SMX4 exhibit pronounced perplexity degradation. SMX4 performs especially poorly due to the additional shared 1-bit exponent among neighboring elements, which amplifies errors when their magnitudes differ. Crucially, we find that simply preserving the maximum element of the block in FP16 precision drastically reduces MXFP4’s perplexity, nearly matching FP4 and NVFP4.
L130: This experiment confirms that the mishandling of block maximum is the primary weakness of MX quantization.
L131: Figure 3. Perplexity of 4-bit quantization on LLaMA3, retaining the group-wise maximum in FP16 significantly enhances MXFP4.
L132: 
L133: Figure 4. Perplexity decreases with increasing equivalent bit width (EBW), but the improvement diminishes beyond g-32 despite larger bit wdiths.
L134: Table 1. The features of DNN accelerators across different scaling factors, data types, and metadata designs are summarized. In the Scaling Factor column, ‘Granularity’ refers to the quantization granularity. In the Data Type column, a dash (‘-’) indicates that the architecture supports only a single data type.
L135: Architecture  | Scaling Factor  | Data Type  | Metadata
L136: Granularity  | Format  | Granularity  | Format  | Granularity  | Content
L137: OliVe (cite65†Guo et al., 2023 )  | Tensor/Channel  | FP16  | Tensor/Channel  | INT4, Flint4  | Pair  | Outlier-victim pair
L138: ANT (cite60†Guo et al., 2022b )  | Tensor/Channel  | FP16  | Tensor/Channel  | INT4, Flint4, PoT4  | Tensor/Channel  | 2-bit index
L139: Tender (cite68†Lee et al., 2024 )  | Channel  | FP16  | -  | INT4  | Channel  | 12-bit index data
L140: MANT (cite62†Hu et al., 2025 )  | Group-64  | FP16  | Group-64  | 16 data types  | Group-64  | 8-bit coefficient $a$
L141: BitMod (cite63†Chen et al., 2025 )  | Group-128  | FP16  | Group-128  | FP4+special value  | Group-128  | 2-bit index
L142: MXFP (cite55†Rouhani et al., 2023 )  | Group-32  | E8M0  | -  | FP4  | -  | -
L143: SMX (cite90†Darvish Rouhani et al., 2023 )  | Group-16  | E8M0  | -  | INT3 (SMX4)  | Pair  | 1-bit exponent
L144: NVFP (cite56†Nvidia, 2024 )  | Group-16  | FP8 (E4M3)  | -  | FP4  | -  | -
L145: MicroScopiQ (cite64†Ramachandran et al., 2025 )  | Group-128  | E8M0  | Group-128  | FP4+INT4  | Block  | 24-bit permutation list, 16-bit identifier,
L146: and 8-bit MXScale, depends on $\mu\text{block}$
L147: BBAL (cite93†Han et al., 2025 )  | Group-32  | E5M0  | -  | INT3  | Element  | 1-bit flag
L148: BlockDialect (cite59†Jang and Tambe, 2025 )  | Group-32  | E5M0  | Group-32  | 16 dialects  | Group-32  | 4-bit index
L149: MX+ (cite77†Lee et al., 2025b )  | Group-32  | E8M0  | Group-32  | FP4  | Group-32  | 5-bit index and 3-bit reserved
L150: ### 3.2. A Taxonomy of Quantization Design Dimensions
L151: 
L152: To further identify promising solutions, we decompose recent architectural innovations into three design dimensions: the scaling factor, the data type, and metadata.
L153: #### 3.2.1. Scaling Factor: Converging Toward Group-Level E8M0/FP8
L154: The scaling factor determines how local dynamic ranges are represented. Early schemes adopted coarse per-tensor or per-channel scaling (cite47†Frantar et al., 2023 ; cite61†Dettmers et al., 2023 ), which are simple but highly sensitive to outliers. Subsequent designs refined granularity to group-level scaling, partitioning tensors into blocks (e.g., 32 or 64 elements), each with its own shared scale.
L155: This approach, now embodied in OCP’s MX specification  (cite55†Rouhani et al., 2023 ), isolates local outliers and has become the industry standard. In terms of numerical format, the field has largely converged on two options: (1) E8M0 (power-of-two scaling): extremely hardware-friendly due to its shift-only implementation, but coarse resolution leads to misalignment with block maximum (Sec. 3.1).
L156: (2) FP8 (E4M3): higher precision, as adopted in NVIDIA Blackwell (cite56†Nvidia, 2024 ), but with limited exponent range, requiring an additional tensor-level rescale for stability.
L157: As illustrated in Fig. cite92†4 , our experiments show diminishing returns when simply reducing group size (e.g., from 32 to 16), while equivalent bit width (defined as per-element bits plus amortized scale bits) rises noticeably due to more scales per tensor, and accuracy gains quickly plateau.
L158: In addition to scaling factor granularity, the data type of the scaling factor has also been explored in recent years to reduce storage overhead. Tbl. cite94†1 summarizes recent designs adopting E8M0 or FP8 formats. Overall, recent hardware and system designs converge on E8M0 and FP8 for scaling factors, suggesting that this dimension offers little room for breakthrough improvements.
L159: #### 3.2.2. Data Type: Expressive but Hardware-Prohibitive
L160: Another line of work seeks to redesign the base data type to better match tensor distributions. This has led to a rich design space of specialized numerical formats, including custom types like Flint in ANT (cite60†Guo et al., 2022b ), non-uniform types in M-ANT (cite62†Hu et al., 2025 ), and the selectable ‘dialects’ in BlockDialect (cite59†Jang and Tambe, 2025 ). While these methods provide strong representational flexibility, they face two fundamental limitations: (1) Low efficiency for dynamic tensors.
L161: Most designs target weights that are static and can afford offline type selection. Applying them to activations, which are generated dynamically during inference, requires costly runtime decisions. (2) Decoder complexity. Supporting multiple custom data types demands numerous decoders and format converters in hardware, significantly inflating area, latency, and energy.
L162: Thus, although novel data types are intellectually appealing, they pose significant challenges for deployment in low-latency, high-throughput accelerators, particularly for activation quantization, where runtime overhead is prohibitive.
L163: #### 3.2.3. Metadata: A Flexible Yet Underutilized Design Axis
L164: Beyond scaling factors and data types, recent accelerators have begun exploring metadata (cite65†Guo et al., 2023 ; cite64†Ramachandran et al., 2025 ; cite68†Lee et al., 2024 ), which apply small auxiliary bits that encode side information. Metadata can enhance accuracy without fundamentally altering the base data path, making it a lightweight yet versatile design axis. We identify three representative roles: (1) Critical-value precision allocation.
L165: Approaches such as OliVe (cite65†Guo et al., 2023 ) use “outlier-victim pairs” to assign extra bits to extreme values, while MicroScopiQ (cite64†Ramachandran et al., 2025 ) allocates different bit-widths to inlier and outlier blocks. (2) Range refinement. SMX (cite90†Darvish Rouhani et al., 2023 ) attaches a 1-bit secondary exponent to value pairs, and BBAL (cite93†Han et al., 2025 ) uses a 1-bit flag to shift exponents, both aiming to expand local dynamic range. (3) Format or structure control.
L166: ANT (cite60†Guo et al., 2022b ) and BlockDialect (cite59†Jang and Tambe, 2025 ) employ metadata as indices for selecting numerical types, while Tender (cite68†Lee et al., 2024 ) uses metadata to store indices to hint extra operations.
L167: Despite their promise, existing metadata schemes remain fragmented and bit-inefficient. First, many focus on a single error source (e.g., outliers) but fail to address systemic quantization loss from block maximum. Second, others improve accuracy but at excessive control overhead (e.g., MicroScopiQ introduces 40+ bits of structural metadata per block).
L168: Last but not least, most works lack a principled framework for where and how to allocate metadata, especially for activations where both latency and hardware overhead are critical.
L169: ### 3.3. Takeaway: Metadata as the Key Lever
L170: The analysis above highlights that scaling factor design has already converged, and data-type innovations face prohibitive hardware overheads for dynamic tensors. In contrast, metadata offers a flexible and underexplored design axis. Our findings indicate that properly allocating a small number of metadata bits (e.g., to preserve or enhance critical elements) can directly target the dominant error source in MX quantization.
--------------------------------------------------------------------------------


## Original response: stdnext3core0

M^"2"XFP: A Metadata-Augmented Microscaling Data Format for Efficient Low-bit Quantization (https://arxiv.org/html/2601.19213v1)
citeturn28407view0 [wordlim: 200] Crawled: today; Content type: text/html; Source: open({"ref_id":"turn28405view0","lineno":220}); Total lines: 558
L203: #### 4.2.1. Evaluation Method
L204: 
L205: We quantify accuracy using mean squared error (MSE) relative to FP16. Specifically, the MSE is computed between the outputs of the quantized model, where both weights and activations are quantized, and those of the FP16 baseline, using the same input text. We also normalize the storage cost using equivalent bit width (EBW), which incorporates element bits, shared scale, and metadata overhead, as shown in Eq. cite96†2 .
L206: (2)  |  | $$\text{EBW}=\frac{(k\times B_{\text{elem}})+B_{\text{meta}}+B_{\text{scale}}}{k}=B_{\text{elem}}+\frac{B_{\text{meta}}+B_{\text{scale}}}{k}$$  |
L207: 
L208: Here, $k$ is the group size, $B_{\text{elem}}$ the base data bit-width (e.g., 4 for FP4), and $B_{\text{meta}}$ the metadata bits for the group. This metric allows fair comparisons across strategies by measuring the effective precision delivered per bit.
L209: To ensure fairness, the group size is fixed at 32, while subgroup size is varied to adjust EBW. For element-level strategies (Elem-EM), we assign 2 bits of mantissa metadata per element and evaluate both top-1 and top-2 allocations, but as Sec. cite11†3.1 shows that exponent offsets cannot alleviate block-maximum errors, we omit Elem-EE. Here, top-1/top-2 denote the largest one or two values (by absolute magnitude) within each subgroup.
L210: For subgroup-level strategies (Sg-EM/EE), we allocate 1–2 bits of mantissa or exponent metadata to refine the shared scale. These configurations form the basis of the design space explored in Figs. 5–6 across LLaMA2-7B, LLaMA3-8B, Falcon-7B, and Mistral-7B. Experiments fix group size at 32 while varying subgroups to control EBW.
L211: #### 4.2.2. Fixed Shared Scale Result (Fig. cite97†6 ).
L212: Under a fixed shared scale, Elem-EM consistently dominates, achieving the lowest MSE in the 4.5–4.75 EBW range across all models. Top-1 and top-2 assignments yield nearly identical results, indicating that capturing only the maximum element per subgroup suffices. Sg-EM becomes competitive only at lower EBW ($\leq 4.375$), while Sg-EE shows negligible or marginal improvements over MXFP4 regardless of bit allocation.
L213: These results confirm that subgroup-level range expansion cannot address the dominant error source—block maximum misalignment. Notably, the red dashed line in Fig. cite97†6 marks the 1% accuracy-loss threshold: Elem-EM reaches this target with  4.6 bits on LLaMA2-7B, Falcon-7B, and Mistral-7B, and  4.75 bits on LLaMA3-8B, whereas Sg-EM requires $\geq 5.25$ bits, and Sg-EE fails to meet the threshold entirely.
L214: Figure 7. Impact of adaptive shared scale on Elem-EM and Sg-EM. Optimizing rounding direction enables Sg-EM-search to outperform Elem-EM-search at 4.5-4.75 EBW.
L215: #### 4.2.3. Adatpive Shared Scale Result (Fig. cite98†7 ).
L216: When adaptive shared scale is enabled, the Pareto frontier shifts. By adaptively selecting the shared scale in conjunction with metadata, Sg-EM-2bit surpasses Elem-EM in the critical 4.5 to 4.75 EBW region, achieving lower MSE with minimal overhead. Elem-EM still performs strongly, but no longer dominates. Sg-EE also benefits from adaptive shared scale, yet remains far less efficient than either Elem-EM or Sg-EM.
L217: Overall, the performance ranking becomes: Sg-EM-adaptive > Elem-EM-adaptive > Elem-EM > Sg-EM > Sg-EE-adaptive > Sg-EE.
L218: #### 4.2.4. Key Takeaway.
L219: This Pareto analysis reveals a crucial asymmetry: element-level metadata is superior under a fixed shared scale due to its ability to capture dominant outliers without global adjustments, while subgroup-level metadata becomes preferable once an adaptive shared scale is incorporated. It leverages shared scale optimization to rebalance error across the block, which is quantitatively confirmed by the consistent MSE reduction for Sg-EM and Sg-EE in Fig. cite98†7 (blue markers).
L220: These complementary behaviors directly motivate the hybrid M${}^{\text{2}}$XFP design in Sec. cite24†4.3 , which assigns Sg-EM to static weights and Elem-EM to dynamic activations.
L221: ### 4.3. M${}^{\text{2}}$XFP Design: A Hybrid Strategy
L222: 
L223: The Pareto analysis highlights an important asymmetry: element-level metadata (Elem-EM) is the most effective under a fixed shared scale, while subgroup-level metadata (Sg-EM) becomes superior once an adaptive shared scale is incorporated. This observation naturally suggests that a single uniform strategy cannot simultaneously optimize for both weights and activations, which differ in their statistical properties and quantization requirements.
L224: Weights vs. Activations. Weights are static and can be quantized offline, allowing sufficient time for adaptive optimization to identify the optimal subgroup-level refinement. In contrast, activations are generated dynamically during inference, where latency constraints demand lightweight, deterministic quantization. This constraint forces activations to adopt a bit-efficient strategy under the fixed shared scale mode.
L225: As a result, weights benefit more from subgroup-level metadata with adaptive shared scale (Sg-EM-2bits-adaptive), while activations benefit from element-level metadata that directly preserves the most influential values (Elem-EM-top1).
L226: Hybrid Strategy. M${}^{\text{2}}$XFP adopts a hybrid design that assigns: (1) Weights apply Sg-EM-2bit format, enabling fine-grained subgroup-scale refinement through offline adaptive optimization, thereby improving bit efficiency while maintaining fidelity. (2) Activations apply Elem-EM-top1 format, which captures outliers within each subgroup in real time with minimal routing overhead.
L227: This division of labor leverages the strengths of both strategies while respecting the distinct hardware and workload constraints of weights and activations. Since Elem-EM-top1 and top2 show nearly identical accuracy, we adopt top1 for its simpler implementation and lower metadata routing complexity. As a result, M${}^{\text{2}}$XFP achieves near-FP16 accuracy at an effective precision of  4.5 bits.
L228: This hybrid strategy establishes a balanced trade-off between hardware cost, quantization fidelity, and runtime efficiency, providing the foundation for hardware-friendly quantization and encoding.
L229: cite99†Image: Refer to caption Figure 8. Quantization process to M${}^{\text{2}}$XFP data format. Algorithm 1 The M${}^{\text{2}}$XFP Quantization Process
L230: 
L231: 1: Input: High-precision data group $\mathbf{X}_{\text{FP16}}$ of size $k$.
L232: 
L233: 2: Output: Final MXFP4 $\mathbf{X}_{\text{FP4}}$ and metadata $\mathbf{X}_{\text{meta}}$.
L234: 
L235: 3: ❶ Step 1: Calculate Shared Scale
L236: 
L237: 4: $x_{max}\leftarrow\text{find maximum absolute value in }\mathbf{X}_{\text{FP16}}$
L238: 5: $S\leftarrow 2^{\lfloor\log_{2}(\text{amax}/\text{FP4\_max\_pow2})\rfloor}$
L239: 
L240: 6: ❷ Step 2: Quantize to FP4 (E2M1)
L241: 
L242: 7: $\mathbf{X}_{\text{FP4}}\leftarrow\text{quantize\_to\_E2M1}(\mathbf{X}_{\text{FP16}},S)$
L243: 
L244: 8: For each subgroup:
L245: 
L246: 9: for each subgroup $\mathbf{x}_{\text{FP4}}$ in $\mathbf{X}_{\text{FP4}}$ do
L247: 
L248: 10: ❸❹ Step 3 & 4: Identify the top-1 in subgroup, resolving duplicates by selecting the lowest index
L249: 
L250: 11:   $\mathbf{x}_{\text{FP4\_abs}}\leftarrow abs(\mathbf{x}_{\text{FP4}})$
L251: 12:   $v_{max}\leftarrow\max(\mathbf{x}_{\text{FP4\_abs}})$ $\triangleright$ Get max in subgroup
L252: 
L253: 13:   $C_{idx}\leftarrow\{j\mid|\mathbf{x}_{\text{FP4\_abs}}[j]|=v_{max}\}$ $\triangleright$ Get all candidate
L254: 
L255: 14:   $idx\leftarrow\min(C_{idx})$ $\triangleright$ Select lowest index
L256: 
L257: 15: ❺ Step 5: Quantize top-1 to FP6(E2M3)
L258: 
L259: 16:   $x_{\text{orig}}\leftarrow\mathbf{X}_{\text{FP16}}[\text{idx}_{\text{top1}}]$ $\triangleright$ Original value
L260: 17:   $x_{\text{FP6}}\leftarrow\text{Quantize}(x_{\text{orig}},\text{E2M3},S)$
L261: 
L262: 18: ❻ Step 6: Add bias for encoding
L263: 
L264: 19:   $\text{fp6\_bits}\leftarrow\text{FloatToBits}(|x_{\text{FP6}}|)$ $\triangleright$ 6-bit information
L265: 
L266: 20:   $\text{fp4\_bits}\leftarrow\text{FloatToBits}(|\mathbf{x}_{\text{FP4}}[\text{idx}_{\text{top1}}]|)$ $\triangleright$ 4-bit information
L267: 
L268: 21:   $\text{encoded}\leftarrow\text{fp6\_bits}+1$ $\triangleright$ Add bias in binary
L269: 
L270: 22: ❼ Step 7: Clamp to keep FP6 high 4 bits same as FP4
L271: 23:   $\text{range\_min}\leftarrow\text{fp4\_bits}\underline{00}$ $\triangleright$ The minimum binary value with the same high 4 bits
L272: 
L273: 24:   $\text{range\_max}\leftarrow\text{fp4\_bits}\underline{11}$ $\triangleright$ The maximum binary value with the same high 4 bits
L274: 
L275: 25:   $\text{clamp}\leftarrow\text{Clamp}(\text{encoded},\text{range\_min},\text{range\_max})$
L276: 
L277: 26:   $\mathbf{x}_{\text{meta}}\leftarrow\text{Get2BitsLow}(\text{clamp})$ $\triangleright$ Extract 2-bit metadata
L278: 27: ❽ Step 8: Pack quantized data with metadata
L279: 
L280: 28:   Append $\mathbf{x}_{\text{FP4}}$ to $\mathbf{X}_{\text{FP4}}$ and $\mathbf{x}_{\text{meta}}$ to $\mathbf{X}_{\text{meta}}$
L281: 
L282: 29: end for
L283: 
L284: 30: return $\mathbf{X}_{\text{FP4}},\ \mathbf{X}_{\text{meta}}$
L285: ### 4.4. Quantization and Encoding Process
L286: 
L287: In this section, we introduce the quantization and encoding process for activation with Elem-EM and weight with Sg-EM.
L288: #### 4.4.1. Activation Quantization with Elem-EM
L289: 
L290: The online quantization process for M${}^{\text{2}}$XFP is designed to be efficient, as detailed in Alg. cite100†1 and illustrated in Fig. cite101†8 , with subgroup size 4 as an example. For each incoming activation group, the group-level maximum absolute value is first determined to compute the shared scale factor (Step ❶). All elements in the group are then quantized into a baseline 4-bit E2M1 representation (Step ❷).
L291: Given that the top1 maximum value within each subgroup must also be identified during decoding, we perform the selection in the 4-bit quantized format (FP4-E2M1) (Step ❸). In cases where multiple elements share the same maximum quantized value (i.e., different in FP16 but identical in FP4), M${}^{\text{2}}$XFP selects the element with the lowest memory address as the unique identification (Step ❹).
L292: The original high-precision value of that identified top1 is then quantized to generate an FP6 value (Step ❺).
L293: Encoding Strategy for FP6 Values. We identified a critical issue when directly replacing the FP4 value of the top1 element with its FP6 value: since the high 4 bits of the FP6 value are not necessarily identical to the original FP4 value, the top1 element may no longer remain the maximum after this replacement. To address this, we developed an improved encoding strategy.
L294: Since quantization maps values to their nearest low-bit representation, a value quantized to a specific FP4 value $x$ has only five potential corresponding values when quantized to FP6. For example, if a value is quantized to 4 in FP4, it must fall within the range (3.5, 5]. Thus, it can only be quantized to one of 5 possible FP6 values: 3.5, 3.75, 4, 4.5, or 5.
L295: Based on this observation, we can represent the FP6 value using a bias relative to the FP4 value. Centered at 4.0, the theoretical bias range is -2, -1, 0, 1, 2, corresponding to the FP6 candidates 3.5, 3.75, 4.0, 4.5, 5.0. However, for data alignment purposes, we clamp this bias to -1, 0, 1, 2, which introduces only minor rounding errors (in our example, rounding error occur only when a value is greater than 3.5 but less than 3.625).
L296: We give a case to indicate such a rounding error at the bottom of Fig. cite101†8 . The additional rounding error introduced by our method has a negligible impact. Perplexity results show that the maximum deviation between results on common large language models with and without this rounding error is only 0.02, indicating a minimal effect on performance.
--------------------------------------------------------------------------------


## Original response: stdnext3core0

M^"2"XFP: A Metadata-Augmented Microscaling Data Format for Efficient Low-bit Quantization (https://arxiv.org/html/2601.19213v1)
citeturn28407view1 [wordlim: 200] Crawled: today; Content type: text/html; Source: open({"ref_id":"turn28405view0","lineno":350}); Total lines: 558
L336: These scaling factors can be efficiently realized using lightweight shift-and-add operations: $0.25P$ corresponds to a 2-bit right shift, $0.5P$ corresponds to a 1-bit right shift, and $0.75P$ is implemented by combining them ($0.5P+0.25P$). As the fixed-point datapath already provides sufficient range, no costly multipliers are needed, and the process incurs only minor hardware overhead. The entire scaling procedure is illustrated in Fig. cite105†11 .
L337: Figure 12. The quantization engine that contains scaling & normalization unit for quantization and encode unit to pack data to M${}^{\text{2}}$XFP format.
L338: Dequantize and Accumulate. Finally, the scaled partial sums are dequantized into FP32 and accumulated across all subgroups before being written into the output buffer. The final group output is obtained by summing all subgroup results and applying the shared scale. For MX formats with an E8M0 shared scale, this dequantization is particularly lightweight: instead of full floating-point multiplications, it reduces to simple exponent alignment.
L339: ### 5.5. Quantization Engine.
L340: 
L341: As shown in Fig. cite106†12 , the quantization engine is a two-stage pipeline responsible for online encoding of activations. The first stage computes the group-level scale and generates FP4/FP6 candidates; the second stage identifies the top-1 element per subgroup, applies the bias-clamp encoding, and packs the resulting FP4 data with 2-bit metadata. The entire process is deterministic and streaming-friendly, enabling real-time quantization without stalling the systolic array.
L342: ## 6. Evaluation
L343: ### 6.1. Experimental Setup
L344: Models and Benchmarks. We evaluate our M${}^{\text{2}}$XFP across diverse workloads to demonstrate its generality. For large language models (LLMs), we test on LLaMA-2 (cite107†Touvron et al., 2023 ) (7B), LLaMA-3 (cite45†Dubey et al., 2024 ) (8B, 70B), OPT (cite108†Zhang et al., 2022 ) (6.7B), Mistral (cite109†Jiang et al., 2023 ) (7B), and Falcon (cite110†Almazrouei et al., 2023 ) (7B), covering 7B-70B parameters.
L345: LLM benchmarks include Wikitext v2 and common sense QA tasks such as Arc-challenge, Arc-easy, HellaSwag, PIQA, WinoGrande, and BoolQ (cite111†Clark et al., 2018 ; cite112†Clark et al., 2019 ; cite113†Bisk et al., 2020 ; cite114†Sakaguchi et al., 2021 ; cite115†Zellers et al., 2019 ).
L346: To further show robustness on reasoning, we evaluate reasoning-oriented models like DeepSeek-R1-Distill-Qwen (cite116†DeepSeek-AI et al., 2025 ) (1.5B, 7B) on AIME, MATH-500, GSM8K, GPQA-Diamond, and LiveCodeBench (cite117†Veeraboina, 2023 ; cite118†Rein et al., 2024 ; cite119†Jain et al., 2024 ; cite120†Lightman et al., 2023 ; cite121†Cobbe et al., 2021 ).
L347: Algorithm Implementation. We implement the M${}^{\text{2}}$XFP quantization framework in PyTorch (cite122†Paszke et al., 2019 ), enabling precise modeling of both M${}^{\text{2}}$XFP and baseline formats. Evaluation is conducted using lm-evaluation-harness (cite123†Gao et al., 2024 ). Our MXFP4 baseline follows the OCP standard with group size 32; NVFP4 adopts group size 16; SMX also uses group size 16 with subgroup size 2.
L348: For M${}^{\text{2}}$XFP, we configure a shared E8M0 scaling factor with group size 32 and subgroup size 8. This configuration is empirically validated in Sec. cite19†4.2 as a near-Pareto-optimal trade-off between granularity and overhead, while matching the group-size choices of existing MX-capable hardware (cite57†Smith and Alla, 2024 ; cite56†Nvidia, 2024 ).
L349: Algorithm Baselines. We evaluate M${}^{\text{2}}$XFP against MXFP4, SMX, and NVFP4, the quantization formats supported by existing hardware (cite58†Xu and Ramakrishnan, 2024 ; cite56†Nvidia, 2024 ; cite57†Smith and Alla, 2024 ). We further examine the benefits of enhancing NVFP4 with our proposed metadata augmentation.
L350: Accelerator Implementation. We extend the open-source, cycle-level simulator DNNWeaver (cite124†Sharma et al., 2016 ) to model our accelerator. The augmented components, decode unit, processing elements (PEs), and quantization engine, are implemented in Verilog and synthesized using Synopsys Design Compiler with the TSMC 28 nm standard cell library at 500 MHz, providing power and area estimates. On-chip buffer power and area are modeled with CACTI v7 (cite125†Balasubramonian et al., 2017 ).
L351: Table 2. Zero-shot evaluation results on five benchmarks: Arc-e (Arc-Easy), Arc-c (Arc-Challenge), Hella. (HellaSwag), PiQA, and Wino. (Winogrande). Group / subgroup sizes — MXFP4: 32 / 32, SMX: 16 / 2, M${}^{\text{2}}$XFP: 32 / 8.
L352: Method  | Arc-e  | Arc-c  | Hella.  | PiQA  | Wino.  | BoolQ  | Avg.
L353:  | LLaMA2-7B  |
L354: FP16  | 74.58  | 46.25  | 75.99  | 79.11  | 69.06  | 77.71  | 70.45
L355: SMX4  | 26.43  | 27.05  | 26.13  | 49.40  | 49.80  | 38.93  | 36.29
L356: MXFP4  | 66.84  | 41.47  | 70.49  | 76.61  | 64.01  | 72.51  | 65.32
L357: NVFP4  | 73.11  | 44.88  | 74.62  | 78.13  | 67.88  | 74.22  | 68.81
L358: M${}^{\text{2}}$XFP  | 73.32  | 44.37  | 74.64  | 77.58  | 68.27  | 76.97  | 69.19
L359:  | LLaMA3-8B  |
L360: FP16  | 77.49  | 53.33  | 79.15  | 80.85  | 72.53  | 81.28  | 74.11
L361: SMX4  | 25.00  | 27.13  | 26.03  | 50.18  | 48.86  | 40.67  | 36.31
L362: MXFP4  | 71.42  | 46.08  | 73.53  | 77.48  | 68.19  | 72.84  | 68.26
L363: NVFP4  | 72.98  | 48.55  | 76.08  | 78.40  | 72.14  | 75.96  | 70.69
L364: M${}^{\text{2}}$XFP  | 74.58  | 49.57  | 77.23  | 79.54  | 70.96  | 79.20  | 71.85
L365:  | Mistral-7B-v0.3  |
L366: FP16  | 78.24  | 52.13  | 80.46  | 82.26  | 73.8  | 82.14  | 74.84
L367: SMX4  | 26.39  | 27.22  | 25.69  | 49.18  | 49.33  | 40.06  | 36.31
L368: MXFP4  | 74.03  | 46.67  | 75.87  | 78.94  | 69.06  | 73.49  | 69.68
L369: NVFP4  | 76.47  | 49.23  | 78.13  | 81.56  | 70.64  | 78.07  | 72.35
L370: M${}^{\text{2}}$XFP  | 76.64  | 50.85  | 79.76  | 80.74  | 71.27  | 82.45  | 73.62
L371: Accelerator Baselines. We evaluate the performance and energy of M${}^{\text{2}}$XFP against representative accelerator baselines. Our primary comparison is with MicroScopiQ, a state-of-the-art (SOTA) MX-based accelerator that partitions weights into inlier and outlier blocks, applying hybrid MX quantization to weights and MXINT to activation. To a comprehensive evaluation, we adapt non-MX accelerators (ANT, M-ANT, OliVe) to support fine-grained MX quantization, denoted MX-ANT, MX-M-ANT, and MX-OliVe.
L372: We also include BlockDialect, an SOTA algorithm-architecture co-design approach, with perplexity in Sec. cite36†6.2 .
L373: For fairness, all accelerators are configured with 32$\times$32 PEs supporting 4-bit multiplications, ensuring differences arise from architectural and algorithmic design.
L374: 
L375: Table 3. Perplexity on the Wikitext dataset for M${}^{\text{2}}$XFP and baseline accelerators (lower is better).
L376: Method  | LLaMA2  | LLaMA3  | LLaMA3  | OPT  | Mistral  | Falcon
L377:  | 7B  | 8B  | 70B  | 6.7B  | 7B  | 7B
L378: FP16  | 5.47  | 6.14  | 2.85  | 10.86  | 5.32  | 6.59
L379: MXFP4  | 7.15  | 8.30  | 4.84  | 19.21  | 6.56  | 7.59
L380: MX-ANT  | 6.30  | 8.22  | 4.65  | 12.76  | 6.04  | 7.35
L381: MX-M-ANT  | 6.12  | 7.83  | 4.54  | 12.45  | 5.89  | 7.32
L382: MX-OliVe  | 7.46  | 11.33  | 6.84  | 36.80  | 6.77  | 8.40
L383: MicroScopiQ  | 6.24  | 8.33  | 4.75  | 12.65  | 6.00  | 7.45
L384: BlockDialect  | 5.84  | 7.05  | 3.76  | 11.31  | 5.65  | 6.94
L385: M${}^{\text{2}}$XFP  | 5.77  | 6.84  | 3.56  | 11.34  | 5.58  | 6.88
L386: ### 6.2. Large Language Model Evaluation
L387: 
L388: Compared to Existing Data Types. We first evaluate accuracy on LLMs, with results summarized in Tbl. cite126†2 , comparing M${}^{\text{2}}$XFP against several hardware-supported data types.
L389: 
L390: SMX4 shows severe degradation, with average accuracy loss exceeding 30% on 7B/8B models, making it impractical for 4-bit weight-activation quantization. MXFP4 is more stable, with an average loss of 5.38% on 7B/8B.
L391: M${}^{\text{2}}$XFP consistently outperforms MXFP4 across all model scales. Specifically, on 7B/8B models, the average accuracy loss is reduced to 1.58%, representing a 70.63% improvement over MXFP4. Compared with NVFP4 at the same effective bit-width (4.5 bits), M${}^{\text{2}}$XFP also shows lower loss (1.58% vs. 2.52%), corresponding to an absolute accuracy gain of 0.94% (37.30% improvement).
L392: We note that NVFP4 achieves higher accuracy on certain tasks (e.g., WinoGrande on LLaMA3-8B), which demonstrates its effectiveness. However, when averaged across all benchmarks, M${}^{\text{2}}$XFP consistently delivers superior overall accuracy. Other data types also benefit from adaptive shared scale search, but these gains do not change the overall trends in Tbl. cite126†2 .
L393: Compared to Baseline Accelerators. We evaluate perplexity on Wikitext v2 across several LLMs, comparing M${}^{\text{2}}$XFP with MX-ANT, MX-M-ANT, MX-OliVe, MicroScopiQ, and BlockDialect, all under W4A4 quantization with group size 32 and an E8M0 shared scaling factor.
L394: M${}^{\text{2}}$XFP achieves the lowest perplexity on all models except OPT-6.7B, where BlockDialect is better by only 0.03. MX-ANT and MX-M-ANT improve over MXFP4 by adapting weight types, but extending to activations is limited by costly online search. BlockDialect addresses this with efficient real-time decision, yielding larger gains over MXFP4. MX-OliVe, though effective tensor-wise, underperforms MXFP4 in group-wise due to its ‘outlier-victim’ encoding that sacrifices neighbors.
L395: MicroScopiQ shows that such neighboring outliers frequently occur in LLMs, and adopts a block-level scheme for better balance. However, its reliance on naive MXINT activation quantization leads to suboptimal W4A4 perplexity.
L396: Table 4. Evaluation of reasoning tasks on DeepSeek-R1-Distill-Qwen: MXFP4 vs. M${}^{\text{2}}$XFP.
L397: Method  | AIME-90  | MATH-500  | GSM8K  | GPQA  | LiveCodeBench  | Avg.
L398:  | DeepSeek-R1-Distill-Qwen-1.5B
L399: FP16  | 21.11  | 85.4  | 84.76  | 36.36  | 17.54  | 49.03
L400: MXFP4  | 7.78  | 66.6  | 69.37  | 31.82  | 8.96  | 36.91
L401: M${}^{\text{2}}$XFP  | 18.89  | 80.2  | 79.83  | 32.83  | 10.45  | 44.44
L402:  | DeepSeek-R1-Distill-Qwen-7B
L403: FP16  | 45.56  | 93.80  | 90.83  | 50.51  | 35.82  | 63.30
L404: MXFP4  | 26.67  | 89.60  | 88.40  | 46.97  | 28.36  | 56.00
L405: M${}^{\text{2}}$XFP  | 40.00  | 93.80  | 90.83  | 52.02  | 32.40  | 61.81
L406: Table 5. The area and power of core components and buffers for M${}^{\text{2}}$XFP using a 28nm process.
L407: 
L408: Component  | Number  | Area($mm^{2}$)  | Power(mW)
L409: PE Tile (2140.12$\mu m^{2}$)  | 128  | 0.2739  | 27.021
L410: Top-1 Decode Unit (82.91$\mu m^{2}$)  | 4  | 0.0003  | 0.064
L411: Quantization Engine (2451.47$\mu m^{2}$)  | 1  | 0.0024  | 0.663
L412: Buffer (324KB)  | 1  | 0.7740  | 176.268
L413: Total  |  | 1.051  | 204.02
L414: Reasoning Tasks. We evaluate M${}^{\text{2}}$XFP on complex reasoning benchmarks using DeepSeek-R1-Distill-Qwen. Prior work (cite127†Liu et al., 2025a ) shows that MXFP4 severely degrades reasoning ability, making LLMs nearly incapable of handling advanced math or coding tasks. Our results in Tbl. cite128†4 confirm this: MXFP4 causes a 12.12% accuracy drop on DeepSeek-R1-Distill-Qwen-1.5B. M${}^{\text{2}}$XFP can recover the average accuracy loss to 4.59%.
L415: Moreover, M${}^{\text{2}}$XFP scales robustly to 7B reasoning models, maintaining reliable performance across sizes.
L416: ### 6.3. Performance, Area, and Energy
L417: Tbl. cite129†5 presents the component breakdown of M${}^{\text{2}}$XFP. A $32\times 32$ systolic array is modeled with four top-1 decode units, each handling eight 4-bit inputs. Together with the quantization engine, these account for only 0.26% of area and 0.36% of power overhead in all components, reflecting the low overhead of MX quantization in E8M0 format. To quantify the hardware overhead across data formats, we synthesized MXFP4, NVFP4, and M${}^{\text{2}}$XFP PE tile using the same 28nm flow.


## Original response: stdnext3eval3

M^"2"XFP: A Metadata-Augmented Microscaling Data Format for Efficient Low-bit Quantization (https://arxiv.org/html/2601.19213v1)
citeturn28412view0 [wordlim: 200] Crawled: today; Content type: text/html; Source: open({"ref_id":"turn28405view0","lineno":418}); Total lines: 558
L352: Method  | Arc-e  | Arc-c  | Hella.  | PiQA  | Wino.  | BoolQ  | Avg.
L353:  | LLaMA2-7B  |
L354: FP16  | 74.58  | 46.25  | 75.99  | 79.11  | 69.06  | 77.71  | 70.45
L360: FP16  | 77.49  | 53.33  | 79.15  | 80.85  | 72.53  | 81.28  | 74.11
L361: SMX4  | 25.00  | 27.13  | 26.03  | 50.18  | 48.86  | 40.67  | 36.31
L362: MXFP4  | 71.42  | 46.08  | 73.53  | 77.48  | 68.19  | 72.84  | 68.26
L363: NVFP4  | 72.98  | 48.55  | 76.08  | 78.40  | 72.14  | 75.96  | 70.69
L364: M${}^{\text{2}}$XFP  | 74.58  | 49.57  | 77.23  | 79.54  | 70.96  | 79.20  | 71.85
L365:  | Mistral-7B-v0.3  |
L366: FP16  | 78.24  | 52.13  | 80.46  | 82.26  | 73.8  | 82.14  | 74.84
L367: SMX4  | 26.39  | 27.22  | 25.69  | 49.18  | 49.33  | 40.06  | 36.31
L368: MXFP4  | 74.03  | 46.67  | 75.87  | 78.94  | 69.06  | 73.49  | 69.68
L369: NVFP4  | 76.47  | 49.23  | 78.13  | 81.56  | 70.64  | 78.07  | 72.35
L370: M${}^{\text{2}}$XFP  | 76.64  | 50.85  | 79.76  | 80.74  | 71.27  | 82.45  | 73.62
L371: Accelerator Baselines. We evaluate the performance and energy of M${}^{\text{2}}$XFP against representative accelerator baselines. Our primary comparison is with MicroScopiQ, a state-of-the-art (SOTA) MX-based accelerator that partitions weights into inlier and outlier blocks, applying hybrid MX quantization to weights and MXINT to activation. To a comprehensive evaluation, we adapt non-MX accelerators (ANT, M-ANT, OliVe) to support fine-grained MX quantization, denoted MX-ANT, MX-M-ANT, and MX-OliVe.
L372: We also include BlockDialect, an SOTA algorithm-architecture co-design approach, with perplexity in Sec. cite36†6.2 .
L373: For fairness, all accelerators are configured with 32$\times$32 PEs supporting 4-bit multiplications, ensuring differences arise from architectural and algorithmic design.
L374: 
L375: Table 3. Perplexity on the Wikitext dataset for M${}^{\text{2}}$XFP and baseline accelerators (lower is better).
L376: Method  | LLaMA2  | LLaMA3  | LLaMA3  | OPT  | Mistral  | Falcon
L377:  | 7B  | 8B  | 70B  | 6.7B  | 7B  | 7B
L378: FP16  | 5.47  | 6.14  | 2.85  | 10.86  | 5.32  | 6.59
L379: MXFP4  | 7.15  | 8.30  | 4.84  | 19.21  | 6.56  | 7.59
L380: MX-ANT  | 6.30  | 8.22  | 4.65  | 12.76  | 6.04  | 7.35
L381: MX-M-ANT  | 6.12  | 7.83  | 4.54  | 12.45  | 5.89  | 7.32
L382: MX-OliVe  | 7.46  | 11.33  | 6.84  | 36.80  | 6.77  | 8.40
L383: MicroScopiQ  | 6.24  | 8.33  | 4.75  | 12.65  | 6.00  | 7.45
L384: BlockDialect  | 5.84  | 7.05  | 3.76  | 11.31  | 5.65  | 6.94
L385: M${}^{\text{2}}$XFP  | 5.77  | 6.84  | 3.56  | 11.34  | 5.58  | 6.88
L386: ### 6.2. Large Language Model Evaluation
L387: 
L388: Compared to Existing Data Types. We first evaluate accuracy on LLMs, with results summarized in Tbl. cite126†2 , comparing M${}^{\text{2}}$XFP against several hardware-supported data types.
L389: 
L390: SMX4 shows severe degradation, with average accuracy loss exceeding 30% on 7B/8B models, making it impractical for 4-bit weight-activation quantization. MXFP4 is more stable, with an average loss of 5.38% on 7B/8B.
L391: M${}^{\text{2}}$XFP consistently outperforms MXFP4 across all model scales. Specifically, on 7B/8B models, the average accuracy loss is reduced to 1.58%, representing a 70.63% improvement over MXFP4. Compared with NVFP4 at the same effective bit-width (4.5 bits), M${}^{\text{2}}$XFP also shows lower loss (1.58% vs. 2.52%), corresponding to an absolute accuracy gain of 0.94% (37.30% improvement).
L392: We note that NVFP4 achieves higher accuracy on certain tasks (e.g., WinoGrande on LLaMA3-8B), which demonstrates its effectiveness. However, when averaged across all benchmarks, M${}^{\text{2}}$XFP consistently delivers superior overall accuracy. Other data types also benefit from adaptive shared scale search, but these gains do not change the overall trends in Tbl. cite126†2 .
L393: Compared to Baseline Accelerators. We evaluate perplexity on Wikitext v2 across several LLMs, comparing M${}^{\text{2}}$XFP with MX-ANT, MX-M-ANT, MX-OliVe, MicroScopiQ, and BlockDialect, all under W4A4 quantization with group size 32 and an E8M0 shared scaling factor.
L394: M${}^{\text{2}}$XFP achieves the lowest perplexity on all models except OPT-6.7B, where BlockDialect is better by only 0.03. MX-ANT and MX-M-ANT improve over MXFP4 by adapting weight types, but extending to activations is limited by costly online search. BlockDialect addresses this with efficient real-time decision, yielding larger gains over MXFP4. MX-OliVe, though effective tensor-wise, underperforms MXFP4 in group-wise due to its ‘outlier-victim’ encoding that sacrifices neighbors.
L395: MicroScopiQ shows that such neighboring outliers frequently occur in LLMs, and adopts a block-level scheme for better balance. However, its reliance on naive MXINT activation quantization leads to suboptimal W4A4 perplexity.
L396: Table 4. Evaluation of reasoning tasks on DeepSeek-R1-Distill-Qwen: MXFP4 vs. M${}^{\text{2}}$XFP.
L397: Method  | AIME-90  | MATH-500  | GSM8K  | GPQA  | LiveCodeBench  | Avg.
L398:  | DeepSeek-R1-Distill-Qwen-1.5B
L399: FP16  | 21.11  | 85.4  | 84.76  | 36.36  | 17.54  | 49.03
L400: MXFP4  | 7.78  | 66.6  | 69.37  | 31.82  | 8.96  | 36.91
L401: M${}^{\text{2}}$XFP  | 18.89  | 80.2  | 79.83  | 32.83  | 10.45  | 44.44
L402:  | DeepSeek-R1-Distill-Qwen-7B
L403: FP16  | 45.56  | 93.80  | 90.83  | 50.51  | 35.82  | 63.30
L404: MXFP4  | 26.67  | 89.60  | 88.40  | 46.97  | 28.36  | 56.00
L405: M${}^{\text{2}}$XFP  | 40.00  | 93.80  | 90.83  | 52.02  | 32.40  | 61.81
L406: Table 5. The area and power of core components and buffers for M${}^{\text{2}}$XFP using a 28nm process.
L407: 
L408: Component  | Number  | Area($mm^{2}$)  | Power(mW)
L409: PE Tile (2140.12$\mu m^{2}$)  | 128  | 0.2739  | 27.021
L410: Top-1 Decode Unit (82.91$\mu m^{2}$)  | 4  | 0.0003  | 0.064
L411: Quantization Engine (2451.47$\mu m^{2}$)  | 1  | 0.0024  | 0.663
L412: Buffer (324KB)  | 1  | 0.7740  | 176.268
L413: Total  |  | 1.051  | 204.02
L414: Reasoning Tasks. We evaluate M${}^{\text{2}}$XFP on complex reasoning benchmarks using DeepSeek-R1-Distill-Qwen. Prior work (cite127†Liu et al., 2025a ) shows that MXFP4 severely degrades reasoning ability, making LLMs nearly incapable of handling advanced math or coding tasks. Our results in Tbl. cite128†4 confirm this: MXFP4 causes a 12.12% accuracy drop on DeepSeek-R1-Distill-Qwen-1.5B. M${}^{\text{2}}$XFP can recover the average accuracy loss to 4.59%.
L415: Moreover, M${}^{\text{2}}$XFP scales robustly to 7B reasoning models, maintaining reliable performance across sizes.
L416: ### 6.3. Performance, Area, and Energy
L417: Tbl. cite129†5 presents the component breakdown of M${}^{\text{2}}$XFP. A $32\times 32$ systolic array is modeled with four top-1 decode units, each handling eight 4-bit inputs. Together with the quantization engine, these account for only 0.26% of area and 0.36% of power overhead in all components, reflecting the low overhead of MX quantization in E8M0 format. To quantify the hardware overhead across data formats, we synthesized MXFP4, NVFP4, and M${}^{\text{2}}$XFP PE tile using the same 28nm flow.
L418: The resulting PE tile areas are 2057.6$\mu m^{2}$ (MXFP4), 2104.7$\mu m^{2}$ (NVFP4, +2.3%), and 2140.1$\mu m^{2}$ (M${}^{\text{2}}$XFP, +4.0%), showing that M${}^{\text{2}}$XFP remains in the same cost range as existing MX-based formats and introduces only modest additional area. The design includes 324 KB of buffer: 144 KB each for activations and weights, plus 36 KB for outputs with scaling factors and metadata.
L419: It is worth noting that the buffer size also incorporates storage for scaling factors and metadata.
L420: Fig. cite130†13 compares performance and energy against MX-based baselines under identical systolic array sizes, differing only in decoder, encoder, or PE design. To match accuracy, the baselines require quantizing some tensors to 8 bits, which contributes a lot to their higher latency and energy consumption. In particular, MX-OliVe falls back to 8-bit quantization for more than 50% of tensors, resulting in a large performance gap compared with M${}^{\text{2}}$XFP.
L421: MX-ANT, MX-M-ANT, and MicroScopiQ achieve similar performance, but MX-M-ANT consumes extra core energy from shift-and-accumulate operations, while MicroScopiQ expends more in its ReCoN unit for outlier processing. Overall, M${}^{\text{2}}$XFP achieves on average 1.91$\times$ speedup and 1.75$\times$ energy reduction compared to the state-of-the-art MX accelerator MicroScopiQ.
L422: Figure 13. The normalized latency and energy comparison between M${}^{\text{2}}$XFP and baseline accelerators. Table 6. Wikitext perplexity of NVFP4 and NVFP4 with Elem-EM and Sg-EM metadata (lower is better).
L423: 
L424: Method  | LLaMA2  | LLaMA3  | LLaMA3  | OPT  | Mistral  | Falcon
L425: 7B  | 8B  | 70B  | 6.7B  | 7B  | 7B
L426: FP16  | 5.47  | 6.14  | 2.85  | 10.86  | 5.32  | 6.59
L427: NVFP4  | 5.81  | 7.18  | 3.63  | 11.46  | 5.76  | 6.90
L428: $\text{M}^{2}$-NVFP4  | 5.77  | 6.85  | 3.57  | 11.32  | 5.58  | 6.88
L429: Table 7. Comparison with several algorithm schemes. The dataset is Wikitext and lll group size is 32.
L430: 
L431: Method  | QuaRot  | DuQuant  | MR-GPTQ  | M${}^{\text{2}}$XFP  | MR-GPTQ-M${}^{\text{2}}$XFP
L432: Data Type  | INT4  | INT4  | FP4  | FP4  | FP4
L433: LLaMA2-7B  | 5.84  | 6.28  | 5.97  | 5.77  | 5.73
L434: LLaMA3-8B  | 7.13  | 7.90  | 7.17  | 6.84  | 6.84
L435: ### 6.4. Analysis and Discussion
L436: Applying on NVFP4. M${}^{\text{2}}$XFP is a general design that can also extend to formats such as NVFP4. By integrating Sg-EM for weights and Elem-EM for activations, we construct $\text{M}^{2}$-NVFP4 (Tbl. cite131†6 ), which yields lower perplexity than the original NVFP4. However, since NVFP4 uses group size 16, the added metadata raises its effective bit-width from 4.5 to 5 bits. Therefore, NVFP4 may benefit from further exploration in our encoding design framework to identify more bit-efficient designs.
L437: Impact of Shared Scale Calculation. Different ways of computing the shared scale can affect quantization error and accuracy (cite83†Cook et al., 2025 ; cite74†Mishra et al., 2025 ; cite75†Yang et al., 2025 ). We evaluate five strategies for computing the shared scale $S=2^{E}$ from the block maximum amax in MX-style quantization.
L438: The first rule, floor, follows the OCP (cite55†Rouhani et al., 2023 ) specification and sets $E=\lfloor\log_{2}(\text{amax}/P)\rfloor$, where $P$ is the largest power-of-two value representable by the format (e.g., $P=4$ for FP4). The second rule, ceil, instead normalizes by the maximum representable magnitude $M$ and uses $E=\lceil\log_{2}(\text{amax}/M)\rceil$ (e.g., $M=6$ for FP4). The third rule, RTN1, replaces the ceil operation with round-to-nearest, $E=\mathrm{round}(\log_{2}(\text{amax}/M))$.
L439: The fourth rule, RTN2, uses round-to-nearest on the normalized block maximum with respect to the largest power-of-two representable value $P$, i.e., $E=\mathrm{round}(\log_{2}(\text{amax}/P))$. Finally, the RTNE rule, introduced in prior work (cite75†Yang et al., 2025 ), rounds amax in value space, normalizes by $P$, and then applies floor to the logarithm, $E=\lfloor\log_{2}(\mathrm{round}(\text{amax})/P)\rfloor$.
L440: Notably, for FP4 (where $P=4$ and $M=6$), RTNE and ceil produce identical exponents because $M=\tfrac{3}{2}P$, which ensures $\lfloor\log_{2}(\mathrm{round}(a)/P)\rfloor=\lceil\log_{2}(a/M)\rceil$ for all block maxima $a$; thus, the two rules are equivalent in this format. In all cases, the shared scale is obtained as $S=2^{E}$. Our previous experiments used only the floor rule, which corresponds to the OCP-recommended default configuration.
L441: As shown in Tbl. cite132†8 , for MXFP4 the ceil/RTNE rule achieves the lowest perplexity, consistent with the MXFP8 recipe (cite74†Mishra et al., 2025 ) (Appendix A.1), whereas RTN1 performs worse because it does not address the dominant block-maximum error and introduces additional nondeterminism. RTN2 is close to RTNE and ceil, but is slightly worse on average.
L442: Across all five shared-scale computation rules, M${}^{\text{2}}$XFP consistently improves accuracy over the MXFP4 baseline, indicating that its gains are robust to the choice of scaling strategy.
L443: Table 8. Wikitext perplexity of different methods to calculate the shared scale for MXFP4.
L444: 
L445: Models  | LLaMA2-7B  | LLaMA3-8B
L446: MXFP4  | M${}^{\text{2}}$XFP4  | MXFP4  | M${}^{\text{2}}$XFP4
L447: floor  | 7.15  | 5.77  | 8.30  | 6.84
L448: ceil/RTNE  | 6.21  | 5.80  | 7.97  | 6.96
L449: RTN1  | 9.21  | 5.79  | 9.34  | 6.87
L450: RTN2  | 6.26  | 5.81  | 8.08  | 7.01
L451: Comparison with Algorithm Schemes. To demonstrate that the MXFP data format is competitive with recent algorithmic schemes (cite48†Ashkboos et al., 2024 ; cite70†Lin et al., 2024 ; cite133†Egiazarian et al., 2025 ), we add comparisons with DuQuant (cite70†Lin et al., 2024 ), QuaRot (cite48†Ashkboos et al., 2024 ) (INT), and the MX-based MR-GPTQ (cite133†Egiazarian et al., 2025 ). Under the same group size, M${}^{\text{2}}$XFP achieves lower perplexity.
L452: Since MR-GPTQ is an algorithmic scheme and orthogonal to M${}^{\text{2}}$XFP, we also combine them; the joint gain is incremental but may improve with further tuning.
L453: Extension to Attention and KV Cache. While Linear layers (handling Q/K/V/O projections) dominate latency ($\sim$83%) at typical sequence lengths of 4096, the Attention mechanism becomes significant at longer contexts, accounting for $\sim$45% of latency at length 16384. Extending M${}^{\text{2}}$XFP to the KV cache is therefore crucial for sustaining its benefits across varying sequence lengths and workloads.
L454: Furthermore, quantization strategy can be integrated with recent memory management systems (cite134†Kwon et al., 2023 ; cite135†Xu et al., 2024 ; cite136†Prabhu et al., 2025 ; cite137†Zheng et al., 2024 ; cite138†Guo et al., 2024b ) to further optimize memory usage and minimize data movement.
L455: In practice, applying M${}^{\text{2}}$XFP to the KV cache follows the same design principles as for Linear layers. In Attention, K/V are both right-hand operands in GEMM ($P=QK^{T}$, $O=PV$). Systems like KIVI (cite139†Liu et al., 2024 ) and VQ-LLM (cite69†Liu et al., 2025b ) adopt a lazy KV cache quantization policy, allowing adaptive shared scale search. Therefore, Sg-EM can be used for K and V, and Elem-EM for Q and P, which is compatible with M${}^{\text{2}}$XFP architecture.
L456: ## 7. Conclusion
L457: In this paper, we presented M${}^{\text{2}}$XFP, a metadata-augmented microscaling (MX) data format that mitigates accuracy loss in 4-bit weight-activation quantization. We explored bit-efficient metadata allocation schemes, built a dedicated hardware unit for encoding support, and integrated it into a systolic array.
L458: M${}^{\text{2}}$XFP reduces accuracy loss by 70.6% over MXFP4 and 37.3% over NVFP4, while achieving up to 1.91$\times$ performance and 1.75$\times$ energy gains, demonstrating the practicality of metadata-driven MX formats for future LLM accelerators.
L459: ###### Acknowledgements.
L460: This work was supported by the National Natural Science Foundation of China (NSFC) Grants (62222210, 62532006, and 62502305), Shanghai Qi Zhi Institute Innovation Program SQZ202316, and Natural Science Foundation of Shanghai Grants (25ZR1402275). The authors express their gratitude to the anonymous reviewers for their insightful feedback, which greatly contributed to improving this work. We also thank our shepherd for the ongoing support and guidance during the revision process.
L461: Any opinions, findings, and conclusions in this paper are those of the authors only and do not necessarily reflect the views of our sponsors.
L462: ## References
L463:   * Almazrouei et al. (2023) E. Almazrouei, H. Alobeidli, A. Alshamsi, A. Cappelli, R. Cojocaru, M. Debbah, É. Goffinet, D. Hesslow, J. Launay, Q. Malartic, D. Mazzotta, B. Noune, B. Pannier, and G. Penedo The falcon series of open language models. External Links: 2311.16867, cite140†Link Cited by: cite141†§6.1 .
L464:   * Ashkboos et al. (2024) S. Ashkboos, A. Mohtashami, M. L. Croci, B. Li, P. Cameron, M. Jaggi, D. Alistarh, T. Hoefler, and J. Hensman QuaRot: outlier-free 4-bit inference in rotated llms. In Proceedings of the 38th International Conference on Neural Information Processing Systems, NIPS ’24, Red Hook, NY, USA. External Links: ISBN 9798331314385 Cited by: cite142†§1 , cite143†§2.1 , cite144†§6.4 .
L465:   * Balasubramonian et al. (2017) R. Balasubramonian, A. B. Kahng, N. Muralimanohar, A. Shafiee, and V. Srinivas CACTI 7: new tools for interconnect exploration in innovative off-chip memories. ACM Trans. Archit. Code Optim. 14 (2). External Links: ISSN 1544-3566, cite145†Link†doi.org , cite146†Document†dx.doi.org Cited by: cite147†§6.1 .
L466:   * Bisk et al. (2020) Y. Bisk, R. Zellers, R. L. Bras, J. Gao, and Y. Choi PIQA: reasoning about physical commonsense in natural language. In Thirty-Fourth AAAI Conference on Artificial Intelligence, Cited by: cite141†§6.1 .
L467:   * Chen et al. (2025) Y. Chen, A. F. AbouElhamayed, X. Dai, Y. Wang, M. Andronic, G. A. Constantinides, and M. S. Abdelfattah BitMoD: bit-serial mixture-of-datatype llm acceleration. In 2025 IEEE International Symposium on High Performance Computer Architecture (HPCA), Vol. , pp. 1082–1097. External Links: cite148†Document†dx.doi.org Cited by: cite149†§1 , cite143†§2.1 , cite150†Table 1 .
L468:   * Clark et al. (2019) C. Clark, K. Lee, M. Chang, T. Kwiatkowski, M. Collins, and K. Toutanova BoolQ: exploring the surprising difficulty of natural yes/no questions. In Proceedings of the 2019 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies, Volume 1 (Long and Short Papers), J. Burstein, C. Doran, and T. Solorio (Eds.), Minneapolis, Minnesota, pp. 2924–2936.
L469: External Links: cite151†Link†aclanthology.org , cite152†Document†dx.doi.org Cited by: cite141†§6.1 .
L470:   * Clark et al. (2018) P. Clark, I. Cowhey, O. Etzioni, T. Khot, A. Sabharwal, C. Schoenick, and O. Tafjord Think you have solved question answering? try arc, the ai2 reasoning challenge. External Links: 1803.05457, cite153†Link Cited by: cite141†§6.1 .
L471:   * Cobbe et al. (2021) K. Cobbe, V. Kosaraju, M. Bavarian, M. Chen, H. Jun, L. Kaiser, M. Plappert, J. Tworek, J. Hilton, R. Nakano, C. Hesse, and J. Schulman Training verifiers to solve math word problems. External Links: 2110.14168, cite154†Link Cited by: cite141†§6.1 .
L472:   * Cook et al. (2025) J. Cook, J. Guo, G. Xiao, Y. Lin, and S. Han Four over six: more accurate nvfp4 quantization with adaptive block scaling. External Links: 2512.02010, cite155†Link Cited by: cite156†§2.2 , cite157†§6.4 .
L473:   * Cuyckens et al. (2025) S. Cuyckens, X. Yi, N. S. Murthy, C. Fang, and M. Verhelst Efficient precision-scalable hardware for microscaling (mx) processing in robotics learning. External Links: 2505.22404, cite158†Link Cited by: cite156†§2.2 .
L474:   * Dai et al. (2021) S. Dai, R. Venkatesan, H. Ren, B. Zimmer, W. J. Dally, and B. Khailany VS-quant: per-vector scaled quantization for accurate low-precision neural network inference. External Links: 2102.04503 Cited by: cite159†§2.1 .
L475:   * Darvish Rouhani et al. (2020) B. Darvish Rouhani, D. Lo, R. Zhao, M. Liu, J. Fowers, K. Ovtcharov, A. Vinogradsky, S. Massengill, L. Yang, R. Bittner, A. Forin, H. Zhu, T. Na, P. Patel, S. Che, L. Chand Koppaka, X. SONG, S. Som, K. Das, S. T, S. Reinhardt, S. Lanka, E. Chung, and D. Burger Pushing the limits of narrow precision inferencing at cloud scale with microsoft floating point. In Advances in Neural Information Processing Systems, Vol. 33, pp. 10271–10281. Cited by: cite160†§2.2 .
L476:   * Darvish Rouhani et al. (2023) B. Darvish Rouhani, R. Zhao, V. Elango, R. Shafipour, M. Hall, M. Mesmakhosroshahi, A. More, L. Melnick, M. Golub, G. Varatkar, L. Shao, G. Kolhe, D. Melts, J. Klar, R. L’Heureux, M. Perry, D. Burger, E. Chung, Z. (. Deng, S. Naghshineh, J. Park, and M. Naumov With shared microexponents, a little shifting goes a long way. In Proceedings of the 50th Annual International Symposium on Computer Architecture, ISCA ’23, New York, NY, USA.
L477: External Links: ISBN 9798400700958, cite161†Link†doi.org , cite162†Document†dx.doi.org Cited by: cite160†§2.2 , cite163†§2.2 , cite164†§3.2.3 , cite165†Table 1 .
L478:   * DeepSeek-AI et al. (2025) DeepSeek-AI, D. Guo, D. Yang, H. Zhang, J. Song, R. Zhang, R. Xu, Q. Zhu, S. Ma, P. Wang, X. Bi, X. Zhang, X. Yu, Y. Wu, Z. F. Wu, Z. Gou, Z. Shao, Z. Li, Z. Gao, A. Liu, B. Xue, B. Wang, B. Wu, B. Feng, C. Lu, C. Zhao, C. Deng, C. Zhang, C. Ruan, D. Dai, D. Chen, D. Ji, E. Li, F. Lin, F. Dai, F. Luo, G. Hao, G. Chen, G. Li, H. Zhang, H. Bao, H. Xu, H. Wang, H. Ding, H. Xin, H. Gao, H. Qu, H. Li, J. Guo, J. Li, J. Wang, J. Chen, J. Yuan, J. Qiu, J. Li, J. L. Cai, J. Ni, J.
L479: Liang, J. Chen, K. Dong, K. Hu, K. Gao, K. Guan, K. Huang, K. Yu, L. Wang, L. Zhang, L. Zhao, L. Wang, L. Zhang, L. Xu, L. Xia, M. Zhang, M. Zhang, M. Tang, M. Li, M. Wang, M. Li, N. Tian, P. Huang, P. Zhang, Q. Wang, Q. Chen, Q. Du, R. Ge, R. Zhang, R. Pan, R. Wang, R. J. Chen, R. L. Jin, R. Chen, S. Lu, S. Zhou, S. Chen, S. Ye, S. Wang, S. Yu, S. Zhou, S. Pan, S. S. Li, S. Zhou, S. Wu, S. Ye, T. Yun, T. Pei, T. Sun, T. Wang, W. Zeng, W. Zhao, W. Liu, W. Liang, W. Gao, W. Yu, W. Zhang, W. L. Xiao, W.
L480: An, X. Liu, X. Wang, X. Chen, X. Nie, X. Cheng, X. Liu, X. Xie, X. Liu, X. Yang, X. Li, X. Su, X. Lin, X. Q. Li, X. Jin, X. Shen, X. Chen, X. Sun, X. Wang, X. Song, X. Zhou, X. Wang, X. Shan, Y. K. Li, Y. Q. Wang, Y. X. Wei, Y. Zhang, Y. Xu, Y. Li, Y. Zhao, Y. Sun, Y. Wang, Y. Yu, Y. Zhang, Y. Shi, Y. Xiong, Y. He, Y. Piao, Y. Wang, Y. Tan, Y. Ma, Y. Liu, Y. Guo, Y. Ou, Y. Wang, Y. Gong, Y. Zou, Y. He, Y. Xiong, Y. Luo, Y. You, Y. Liu, Y. Zhou, Y. X. Zhu, Y. Xu, Y. Huang, Y. Li, Y. Zheng, Y. Zhu, Y. Ma, Y.

