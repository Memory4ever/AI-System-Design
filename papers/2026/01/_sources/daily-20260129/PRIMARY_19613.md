# Exact-v1 primary cached excerpts — 2601.19613

These are preserved tool responses, not author summaries. Each response is separated; its L labels are local to that response. No new fetch/revision review.

## Original response 1: 19613point

Up to 36x Speedup: Mask-based Parallel Inference Paradigm for Key Information Extraction in MLLMs (https://arxiv.org/html/2601.19613v1)
citeturn28179view0 [wordlim: 200] Crawled: yesterday; Content type: text/html; Source: open({"ref_id":"https://arxiv.org/html/2601.19613v1","lineno":50}); Total lines: 224
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
L14: cite1†Why HTML?†info.arxiv.org cite2†Report Issue cite3†Back to Abstract cite4†Download PDF L15:   1. cite5†Abstract L16:   2. cite6†1 Introduction L17:   3. cite7†2 Methodology L18:     1. cite8†2.1 Task Formulation L19:     2. cite9†2.2 Model Training Process L20:       1. cite10†2.2.1 Mask Pre-training L21:       2. cite11†2.2.2 KV Supervised Fine-Tuning L22:   4. cite12†3 Experiment L23:     1. cite13†3.1 Experiments Setup L24:     2. cite14†3.2 Results L25:       1. cite15†3.2.1 Compared with SOTA Models L26:       2. cite16†3.2.2 Compared with Base Models L27:     3. cite17†3.3 GPU Memory Consumption L28:   5. cite18†4 Attention Visualization L29:   6. cite19†5 Conclusion L30:   7. cite20†6 Acknowledgements L31:   8. cite21†References L32: cite22†License: arXiv.org perpetual non-exclusive license†info.arxiv.org L33: 
L34: arXiv:2601.19613v1 [cs.CL] 27 Jan 2026
L35: # Up to 36x Speedup: Mask-based Parallel Inference Paradigm for Key Information Extraction in MLLMs
L36: 
L37: Xinzhong Wang    Ya Guo    Jing Li    Huan Chen    Yi Tu    Yijie Hong    Gongshen Liu    Huijia Zhu ^{†}^{†}thanks: ^{†} Equal contribution.^{†}^{†}thanks: ^{‡} Corresponding authors.
L38: ###### Abstract
L39: Key Information Extraction (KIE) from visually-rich documents (VrDs) is a critical task, for which recent Large Language Models (LLMs) and Multi-Modal Large Language Models (MLLMs) have demonstrated strong potential. However, their reliance on autoregressive inference, which generates outputs sequentially, creates a significant efficiency bottleneck, especially as KIE tasks often involve extracting multiple, semantically independent fields.
L40: To overcome this limitation, we introduce PIP: a P arallel I nference P aradigm for KIE. Our approach reformulates the problem by using “[mask]” tokens as placeholders for all target values, enabling their simultaneous generation in a single forward pass. To facilitate this paradigm, we develop a tailored mask pre-training strategy and construct large-scale supervised datasets.
L41: Experimental results show that our PIP-models achieve a 5–36× inference speedup with negligible performance degradation compared to traditional autoregressive base models. By substantially improving efficiency while maintaining high accuracy, PIP paves the way for scalable and practical real-world KIE solutions.
L42: ###### Index Terms:
L43: 
L44: Key Information Extraction, Parallel Inference, Multi-Modal Large Language Models, Document Understanding
L45: 
L46: ^{†}^{†}address: ^{1}Shanghai Jiao Tong University
L47: ^{2}Ant Info Security Lab, Ant Group
L48: ^{3}Inner Mongolia Research Institute, Shanghai Jiao Tong University, Hohhot 010010
L49: ## 1 Introduction
L50: Key Information Extraction (KIE) aims to extract and structure key information (e.g., names, dates, amounts) from visually-rich documents (VrDs) like invoices and forms. As a downstream task of document understanding, it requires integrating multimodal features, including text, layout, and visual cues.
L51: Recent advances in Large Language Models (LLMs) [cite23†1 , cite24†2 , cite25†3 , cite26†4 , cite27†5 , cite28†6 ] and particularly Multi-Modal Large Language Models (MLLMs) [cite29†7 , cite30†8 , cite31†9 , cite32†10 , cite33†11 , cite34†12 , cite35†13 ] have shown remarkable performance on KIE tasks, reshaping the field.
L52: cite36†Image: Refer to caption Figure 1: Comparison of two inference paradigms: (a) Traditional autoregressive inference, which generates tokens sequentially one by one; (b) Our PIP-Models, where different “[mask]” tokens independently attend to distinct image regions and generate all tokens in parallel. cite37†Image: Refer to caption Figure 2: Our overall training processes: (a) represents the mask pre-training phase, and (b) denotes the KV supervised fine-tuning stage.
L53: While LLMs require a preliminary OCR step to process VrDs, this two-stage approach suffers from error propagation and high computational overhead. MLLMs mitigate these issues by processing images and text in an end-to-end fashion, making them a more promising foundation for KIE. However, both LLMs- and MLLMs-based methods are constrained by the autoregressive inference paradigm, which generates tokens sequentially.
L54: This sequential generation is suboptimal for KIE. The extraction of distinct fields—such as the “Num” and “Price” for an item in Figure cite38†1 —are often semantically independent sub-tasks that are inherently parallelizable. We argue that even tokens within a single answer can be generated in parallel. As KIE is largely a retrieval task, each output token (e.g., “14000”) corresponds to a specific visual region.
L55: Its generation thus depends more on attending to the correct image location than on previously generated tokens.
L56: To address this limitation, we propose PIP: a simple yet effective P arallel I nference P aradigm for KIE. PIP reformulates the task by replacing target values in the prompt with “[mask]” tokens (e.g., “Num:[mask][mask]… Price:[mask][mask]…”). This formulation allows the model to decode all masked positions in parallel within a single forward pass, dramatically reducing inference latency.
L57: While mask-based parallel decoding has been explored in unimodal contexts [cite39†14 ], its application to multimodal KIE is non-trivial due to potential interference between masked tokens processing complex visual and textual inputs. Our key insight is that the spatial correspondence between KIE outputs and document regions allows each “[mask]” token to focus on a distinct image area, naturally minimizing interference.
L58: We validate this hypothesis through attention visualization in later section, establishing the feasibility of parallel decoding for multimodal KIE.
L59: To adapt MLLMs to this paradigm, we introduce a dedicated mask pre-training stage and construct a large-scale supervised fine-tuning dataset of key-value (KV) pairs. Experiments show that our approach achieves a 5–36× improvement in inference speed with negligible performance degradation compared to the autoregressive baselines.
L60: 
L61: Our main contributions are:
L62: 
L63:   * •
L64: 
L65: We introduce PIP, a parallel inference paradigm that reformulates KIE for significant efficiency gains.
L66: 
L67:   * •
L68: We develop a specialized training methodology, including a mask pre-training stage and a large-scale supervised fine-tuning dataset, to enable MLLMs to perform parallel decoding.
L69: 
L70:   * •
L71: 
L72: Extensive experiments demonstrate that our method accelerates KIE inference by 5–36× while maintaining comparable performance to autoregressive models.
L73: ## 2 Methodology
L74: ### 2.1 Task Formulation
L75: 
L76: Traditional MLLMs for KIE employ an autoregressive paradigm, generating tokens sequentially. Given an image $I$, they maximize the joint probability of a text sequence $X=[x_{1},\dots,x_{T}]$:
L77: 
L78:  | $$P(x_{1},\dots,x_{T}\mid I)=\prod_{t=1}^{T}P(x_{t}\mid x_{1},\dots,x_{t-1},I).$$  |  | (1)
L79: 
L80: This word-by-word generation process, where each token $x_{t}$ is predicted based on preceding tokens, is inherently sequential and slow, limiting real-world applicability.
L81:  | $$x_{t}=\arg\max_{x}P(x\mid x_{1},\dots,x_{t-1},I).$$  |  | (2)
L82: 
L83: To address this bottleneck, we reformulate the task into a parallel inference paradigm. The model is given an input sequence $X$ with a set of masked positions $M\subseteq\{1,\dots,T\}$. Its objective is to predict all masked tokens $x_{M}$ simultaneously based on the unmasked tokens $x_{\setminus M}$ and the image $I$:
L84: 
L85:  | $$P(x_{M}\mid x_{\setminus M},I)=\prod_{t\in M}P(x_{t}\mid x_{\setminus M},I).$$  |  | (3)
L86: This allows the model to predict all missing tokens in a single forward pass, eliminating the sequential dependency of autoregressive models and significantly improving inference efficiency.
L87: 
L88:  | $$\hat{x}_{t}=\arg\max_{x}P(x\mid x_{\setminus M},I)\quad\forall t\in M.$$  |  | (4)
L89:  |  | FUNSD  |  | SROIE  |  | CORD
L90:  | Models  | ANLS  | Time(s)  |  | ANLS  | Time(s)  |  | ANLS  | Time(s)
L91: LLMs  | Llama2-7B  | $40.8^{*}$  | 0.692  |  | $4.4^{*}$  | 0.753  |  | $15.9^{*}$  | 0.237
L92: Vicuna-1.5-7B  | $48.1^{*}$  | 0.779  |  | $51.4^{*}$  | 0.861  |  | $68.2^{*}$  | 0.249
L93: LayoutLLM-7B  | $80.0^{*}$  | -  |  | $63.1^{*}$  | -  |  | $72.1^{*}$  | -
L94: LayTextLLM-7B  | $\textbf{81.0}^{\sim}$  | 1.055  |  | $96.1^{\sim}$  | 0.948  |  | $82.5^{\sim}$  | 0.339
L95: MLLMs  | LLaVAR-7B  | $1.7^{*}$  | 0.327  |  | $13.6^{*}$  | 0.289  |  | $2.4^{*}$  | 0.218
L96: LLaVA-1.5-7B  | $1.9^{*}$  | 0.310  |  | $18.1^{*}$  | 0.269  |  | $3.8^{*}$  | 0.207
L97: InternVL2-8B  | 61.2  | 0.615  |  | 95.1  | 0.541  |  | 88.2  | 0.314
L98: Qwen2-VL-7B  | 77.9  | 0.455  |  | 94.1  | 0.532  |  | 91.2  | 0.288
L99: Ours  | PIP-InternVL2-8B  | 72.3  | 0.064  |  | 93.4  | 0.034  |  | 93.1  | 0.022
L100: PIP-Qwen2-VL-7B  | 79.3  | 0.053  |  | 97.0  | 0.051  |  | 97.3  | 0.028
L101: Table 1: Results of different models for KIE tasks. * denotes the results from [cite40†15 ], $\sim$ indicates that the results are from [cite41†16 ]. The best results are highlighted in bold, while the shortest inference times are underscored.
L102: ### 2.2 Model Training Process
L103: 
L104: Our PIP-Models are built on existing autoregressive MLLMs. To enable parallel inference, we introduce a two-stage training process: Mask Pre-training and KV Supervised Fine-Tuning, as illustrated in Figure cite42†2 . This process transitions the model from sequential to parallel generation, boosting inference speed for KIE tasks without sacrificing accuracy.
L105: #### 2.2.1 Mask Pre-training
L106: 
L107: This stage adapts the base MLLMs to our parallel framework using a mask-and-predict scheme on large-scale image-caption data. For each sample, we randomly mask a fraction of the caption tokens. The model is trained to reconstruct the masked tokens given the visible tokens and the image, forcing it to learn non-sequential text generation.
L108: Pivotal to this stage is replacing the model’s unidirectional causal attention with a bidirectional attention mechanism, following LLaDA [cite43†17 ]. Unlike autoregressive models where tokens only attend to predecessors, bidirectional attention allows each token to attend to all other tokens in the sequence. This provides a complete context for each prediction, which is crucial for mitigating error propagation and essential for understanding the global document layout in KIE tasks.
L109: Data: The pre-training dataset comprises 13 million images with detailed captions generated by Qwen2-VL-72B [cite44†18 ]. It covers a diverse range of content including documents, landscapes, and artworks, providing a broad foundation for learning robust parallel inference capabilities.
L110: #### 2.2.2 KV Supervised Fine-Tuning
L111: 
L112: While mask pre-training imparts parallel inference capabilities, the model requires task-specific adaptation for KIE. This supervised fine-tuning stage uses a curated KV extraction dataset to refine the model’s ability to identify and extract structured information from documents, enhancing accuracy and reducing content hallucination.
L113: Data: The fine-tuning dataset was meticulously curated. We prioritized high-resolution images, filtered out samples with poor OCR quality, categorized documents into 48 classes, and anonymized all personally identifiable information.
L114: Our annotation pipeline began with pre-annotation using MLLMs (Figure cite42†2 b). Qwen2-VL 72B [cite44†18 ] generated descriptive captions, which were then parsed by Qwen2.5 72B [cite45†19 ] to extract structured KV pairs. To mitigate hallucination, the model was trained to output ”unknown” for keys not present in the image. Subsequently, all machine-generated annotations underwent a human-in-the-loop verification process to correct inaccuracies and ensure dataset fidelity.
L115: ## 3 Experiment
L116: ### 3.1 Experiments Setup
L117: 
L118: Datasets: We evaluate our method on five public benchmarks for KIE: FUNSD [cite46†20 ], SROIE [cite47†21 ], CORD [cite48†22 ], POIE [cite49†23 ], and WildReceipt [cite50†24 ].
L119: 
L120: Baselines: We compare against OCR-based LLMs (Llama2-7B [cite24†2 ], Vicuna-1.5-7B [cite25†3 ], LayoutLLM [cite40†15 ], LayTextLLM [cite41†16 ]) and OCR-free MLLMs (LLaVAR-7B [cite51†25 ], LLaVA-1.5-7B [cite52†26 ]). Our approach is built upon InternVL2-8B [cite53†27 ] and Qwen2-VL-7B [cite44†18 ], which also serve as baselines.
L121: Evaluation Metrics: Performance is assessed by Average Normalized Levenshtein Similarity (ANLS) for FUNSD, SROIE, and CORD, and F1 score for POIE and WildReceipt. Inference efficiency is measured as the average time per sample on 8×A100 GPUs.
L122: ### 3.2 Results
L123: 
L124: We present a comparative analysis of our proposed framework, benchmarking it against state-of-the-art (SOTA) methods and the original base models across multiple dimensions.
L125: #### 3.2.1 Compared with SOTA Models
L126: 
L127: Table cite54†1 provides a comprehensive evaluation of our method against leading LLMs and MLLMs, focusing on extraction performance and inference efficiency.
L128: Extraction Performance: The FUNSD dataset is particularly challenging due to its dynamic key-value schema, leading to lower ANLS scores compared to datasets with fixed structures like SROIE and CORD. General-purpose LLMs (e.g., Llama2-7B, Vicuna-1.5-7B) are limited by the generic text-generation paradigm, reaching a maximum ANLS of 69.0. Layout-aware models like LayTextLLM significantly improve upon this by incorporating spatial features, setting a new SOTA on FUNSD with an ANLS of 81.0.
L129: Vision-based MLLMs (e.g., InternVL2-8B, Qwen2-VL-7B) achieve end-to-end extraction with strong performance, scoring 95.1/94.1 on SROIE and 88.2/91.2 on CORD.
L130: Our model, PIP-Qwen2-VL-7B, demonstrates the effectiveness of mask pre-training and KV-supervised fine-tuning. It achieves substantial ANLS gains over its base model of +1.4 (77.9 → 79.3) on FUNSD, +2.9 (94.1 → 97.0) on SROIE, and +6.1 (91.2 → 97.3) on CORD. This performance establishes new SOTA records on SROIE (97.0) and CORD (97.3), while remaining highly competitive on FUNSD (79.3).
L131: Notably, LayTextLLM’s top score on FUNSD relies on idealized OCR input, which limits its practical applicability due to error propagation from real-world OCR systems. In contrast, our end-to-end approach avoids this dependency, offering superior deployment value.
L132: Inference Efficiency: Autoregressive models like LayTextLLM are constrained by sequential token generation, with per-sample inference times ranging from 0.339s to 1.055s. Our parallel inference paradigm overcomes this bottleneck by generating all target tokens simultaneously. This reduces latency to just 0.028s–0.053s, delivering a 12–20× speedup.
L133: Compared to other MLLMs of a similar scale, which require a minimum of 0.198s–0.310s per sample, our method is 5–7× faster, with a maximum latency of 0.028s–0.064s across datasets. These results validate the efficacy of our parallel inference paradigm.
L134: Summary: Leveraging mask pre-training and KV-supervised fine-tuning, our parallel inference paradigm effectively addresses the performance and efficiency trade-offs of prior methods. Our model achieves SOTA accuracy and significant speed improvements, providing a scalable, high-precision, and low-latency solution for document information extraction.
L135:  | FUNSD  |  | SROIE  |  | CORD  |  | POIE  |  | WildReceipt
L136: Models  | ANLS  | Time  |  | ANLS  | Time  |  | ANLS  | Time  |  | F1  | Time  |  | F1  | Time
L137: InternVL2-2B  | 60.2  | 0.357  |  | 94.4  | 0.332  |  | 87.4  | 0.170  |  | 77.7  | 0.122  |  | 51.3  | 0.184
L138: InternVL2-8B  | 61.2  | 0.615  |  | 95.1  | 0.541  |  | 88.2  | 0.314  |  | 77.2  | 0.167  |  | 53.8  | 0.347
L139: Qwen2-VL-2B  | 75.1  | 0.389  |  | 94.5  | 0.458  |  | 90.7  | 0.225  |  | 87.1  | 0.138  |  | 56.2  | 0.182
L140: Qwen2-VL-7B  | 77.9  | 0.455  |  | 94.1  | 0.532  |  | 91.2  | 0.288  |  | 86.2  | 0.148  |  | 54.9  | 0.218
L141: PIP-InternVL2-2B  | 66.9  | 0.069  |  | 92.8  | 0.028  |  | 91.0  | 0.018  |  | 90.3  | 0.007  |  | 64.7  | 0.005
L142: $\uparrow$6.7  | 5.2×  |  | $\downarrow$1.6  | 11.9×  |  | $\uparrow$3.6  | 9.4×  |  | $\uparrow$12.6  | 17.4×  |  | $\uparrow$13.4  | 36.8×
L143: PIP-InternVL2-8B  | 72.3  | 0.064  |  | 93.4  | 0.034  |  | 93.1  | 0.022  |  | 93.1  | 0.009  |  | 69.0  | 0.010
L144: $\uparrow$11.1  | 9.6×  |  | $\downarrow$1.7  | 15.9×  |  | $\uparrow$4.9  | 14.3×  |  | $\uparrow$15.9  | 18.6×  |  | $\uparrow$11.0  | 34.7×
L145: PIP-Qwen2-VL-2B  | 75.4  | 0.055  |  | 93.4  | 0.049  |  | 95.8  | 0.023  |  | 92.3  | 0.009  |  | 64.8  | 0.006
L146: $\uparrow$0.3  | 7.1×  |  | $\downarrow$1.1  | 9.4×  |  | $\uparrow$5.1  | 9.8×  |  | $\uparrow$5.2  | 15.3×  |  | $\uparrow$8.6  | 30.3×
L147: PIP-Qwen2-VL-7B  | 79.3  | 0.053  |  | 97.0  | 0.051  |  | 97.3  | 0.028  |  | 94.6  | 0.010  |  | 71.6  | 0.006
L148: $\uparrow$1.4  | 8.6×  |  | $\uparrow$2.9  | 10.4×  |  | $\uparrow$6.1  | 10.3×  |  | $\uparrow$8.4  | 14.8×  |  | $\uparrow$16.7  | 36.3×
L149: Table 2: Results of different base models and our PIP-Models for KIE tasks. Green indicates the performance improvement of our parallel model compared to the base model, red signifies a decline in performance, and blue represents the speedup ratio.
L150: #### 3.2.2 Compared with Base Models
L151: 
L152: To demonstrate the generalizability of our paradigm, we conducted experiments across different base models, model sizes, and datasets. The results are presented in Table cite55†2 .
L153: Extraction Performance: Our method consistently maintains or enhances the strong extraction capabilities of base models like the Qwen2-VL and InternVL2 series. For example, PIP-Qwen2-VL-7B improves the F1 score on the WildReceipt dataset by a significant 16.7 points over its base model. Performance remains stable or improves across nearly all tasks, with only a minor degradation observed on SROIE.
L154: Inference Efficiency: As shown in Table cite55†2 , our PIP-Models achieve over a 5× speedup compared to their autoregressive base models. While standard models generate outputs for each key sequentially, our parallel paradigm generates them simultaneously. Consequently, the acceleration factor scales with the number of keys to be extracted. On key-intensive datasets like WildReceipt, this results in an impressive 36× speedup, achieved without compromising extraction accuracy.
L155: Summary: In summary, our parallel inference paradigm, combined with its associated training strategies, significantly accelerates inference speed (5–36×) while maintaining or improving extraction accuracy. The approach demonstrates high flexibility and is applicable across various model architectures and sizes.
L156: Model  | FUNSD  | SROIE  | CORD
L157: --- | --- | --- | ---
L158: InternVL2-2B  | 21.04G  | 15.01G  | 14.84G
L159: InternVL2-8B  | 32.89G  | 28.45G  | 27.75G
L160: Qwen2VL-2B  | 21.15G  | 15.16G  | 14.28G
L161: Qwen2VL-7B  | 32.60G  | 28.02G  | 27.23G
L162: PIP-InternVL2-2B  | 24.39G (+16%)  | 17.83G (+19%)  | 19.09G (+29%)
L163: PIP-InternVL2-8B  | 37.17G (+13%)  | 31.99G (+12%)  | 33.56G (+21%)
L164: PIP-Qwen2-VL-2B  | 24.58G (+16%)  | 17.91G (+18%)  | 18.63G (+30%)
L165: PIP-Qwen2-VL-7B  | 36.71G (+13%)  | 32.52G (+16%)  | 33.22G (+22%)
L166: Table 3: GPU memory usage of different base models and our PIP-Models on FUNSD, SROIE, and CORD datasets. Numbers in parentheses indicate the percentage increase compared to corresponding base models. cite56†Image: Refer to caption Figure 3: The visualization of attention for each token in our PIP-Models when outputting ”193.00”, demonstrating the model’s focus on different regions of the image.
L167: ### 3.3 GPU Memory Consumption
L168: Table cite57†3 compares the GPU memory consumption of baseline models and PIP-Models during inference. The integration of additional “[mask]” tokens to enable parallel output generation increases input length and thus raises memory usage. This overhead remains moderate, with memory usage increasing by at most 30% over the base models. Nonetheless, the parallel inference enabled by these tokens yields substantial improvements in inference speed (5-36×), leading to higher effective GPU utilization.
L169: As shown in Tables cite55†2 and cite57†3 , the proposed framework achieves significant efficiency gains with limited memory overhead and negligible impact on extraction performance.
L170: ## 4 Attention Visualization
L171: To further analyze the parallel inference paradigm for KIE, we visualize the attention maps of output tokens generated by our PIP-Models. As KIE mainly requires extracting information from predefined regions rather than sequential reasoning, output tokens attend to distinct regions of the input image corresponding to different fields.
L172: For example, in the SROIE dataset, when extracting the value “193.00” for the key “TOTAL”, each output token attends to relevant image regions, as illustrated in Figure cite58†3 .
L173: While the model does not focus exclusively on the exact answer regions, each token consistently attends to areas pertinent to its target output. For instance, the token predicting “3” attends to the region containing the character “3”. This validates the effectiveness of the parallel inference paradigm for KIE, where output tokens are conditionally independent and require only localized visual context to achieve accurate extraction, supporting efficient parallel generation.
L174: ## 5 Conclusion
L175: This paper presents PIP, a simple yet effective parallel inference paradigm for KIE from VrDs. Conventional autoregressive approaches are constrained by sequential token generation, limiting scalability for large-scale document processing. To overcome this, we propose a method that incorporates “[mask]” tokens in the input, allowing for the simultaneous generation of all target tokens.
L176: We further introduce a tailored mask pre-training scheme and a KV supervised fine-tuning strategy to enhance overall model performance. Our PIP-Models achieve state-of-the-art results on benchmark datasets such as SROIE and CORD. Extensive experiments demonstrate that our approach maintains competitive accuracy while achieving a 5-36× speedup compared to autoregressive baselines, making it well-suited for practical, large-scale deployments.
L177: By reconciling efficiency with high accuracy, this work marks a significant advancement in KIE, and provides a scalable solution for real-time document understanding in industry applications.
L178: ## 6 Acknowledgements
L179: 
L180: This work was supported by Ant Group Research Fund, the Joint Funds of the National Natural Science Foundation of China (Grant No.U21B2020) and Science and Technology Cooperation Program of Shanghai Jiao Tong University in Inner Mongolia Autonomous Region——Action Plan of Shanghai Jiao Tong University for ”Revitalizing Inner Mongolia through Science and Technology”.
L181: ## References
L182:   * [1] Hugo Touvron, Thibaut Lavril, and et al. Izacard, Gautier, “Llama: Open and efficient foundation language models,” arXiv preprint arXiv:2302.13971, 2023.
L183:   * [2] Hugo Touvron, Louis Martin, and et al. Kevin Stone, “Llama 2: Open foundation and fine-tuned chat models,” 2023.
L184:   * [3] Wei-Lin Chiang, Zhuohan Li, Zi Lin, Ying Sheng, Zhanghao Wu, Hao Zhang, Lianmin Zheng, Siyuan Zhuang, Yonghao Zhuang, Joseph E Gonzalez, et al., “Vicuna: An open-source chatbot impressing gpt-4 with 90%* chatgpt quality,” See https://vicuna. lmsys. org (accessed 14 April 2023), vol. 2, no. 3, pp. 6, 2023.
L185:   * [4] Aohan Zeng, Xin Lv, Qinkai Zheng, Zhenyu Hou, Bin Chen, Chengxing Xie, Cunxiang Wang, Da Yin, Hao Zeng, Jiajie Zhang, et al., “Glm-4.5: Agentic, reasoning, and coding (arc) foundation models,” arXiv preprint arXiv:2508.06471, 2025.
L186:   * [5] Yuliang Liu, Biao Yang, Qiang Liu, Zhang Li, Zhiyin Ma, Shuo Zhang, and Xiang Bai, “Textmonkey: An ocr-free large multimodal model for understanding document,” arXiv preprint arXiv:2403.04473, 2024.
L187:   * [6] AI Anthropic, “The claude 3 model family: Opus, sonnet, haiku,” Claude-3 Model Card, 2024.
L188:   * [7] OpenAI:Josh Achiam, Steven Adler, Sandhini Agarwal, and et al. Ahmad, Lama, “Gpt-4 technical report,” arXiv preprint arXiv:2303.08774, Dec 2023.
L189:   * [8] Haoyu Lu, Wen Liu, Bo Zhang, Bingxuan Wang, Kai Dong, Bo Liu, Jingxiang Sun, Tongzheng Ren, Zhuoshu Li, Yaofeng Sun, et al., “Deepseek-vl: towards real-world vision-language understanding,” arXiv preprint arXiv:2403.05525, 2024.
L190:   * [9] Haoran Wei, Yaofeng Sun, and Yukun Li, “Deepseek-ocr: Contexts optical compression,” arXiv preprint arXiv:2510.18234, 2025.
L191:   * [10] Gemini Team, Rohan Anil, Sebastian Borgeaud, Yonghui Wu, Jean-Baptiste Alayrac, Jiahui Yu, Radu Soricut, Johan Schalkwyk, Andrew M Dai, Anja Hauth, et al., “Gemini: a family of highly capable multimodal models,” arXiv preprint arXiv:2312.11805, 2023.
L192:   * [11] Machel Reid, Nikolay Savinov, Denis Teplyashin, Dmitry Lepikhin, Timothy Lillicrap, Jean-baptiste Alayrac, Radu Soricut, Angeliki Lazaridou, Orhan Firat, Julian Schrittwieser, et al., “Gemini 1.5: Unlocking multimodal understanding across millions of tokens of context,” arXiv preprint arXiv:2403.05530, 2024.
L193:   * [12] Deyao Zhu, Jun Chen, Xiaoqian Shen, Xiang Li, and Mohamed Elhoseiny, “MiniGPT-4: Enhancing vision-language understanding with advanced large language models,” arXiv:2304.10592, 2023.
L194:   * [13] Haotian Liu, Chunyuan Li, Yuheng Li, Bo Li, Yuanhan Zhang, Sheng Shen, and Yong Jae Lee, “Llava-next: Improved reasoning, ocr, and world knowledge,” January 2024.

